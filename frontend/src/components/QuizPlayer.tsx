'use client';

import React, { useState, useEffect } from 'react';
import { Question } from '../types';
import { useLanguage } from '../context/LanguageContext';
import { storage } from '../services/storage';
import {
  Globe,
  ArrowLeft,
  ArrowRight,
  Flag,
  CheckCircle2,
  XCircle,
  AlertCircle,
  Timer,
  Send,
  FileText
} from 'lucide-react';

interface QuizPlayerProps {
  questions: Question[];
  title: string;
  subtitle?: string;
  mode: 'practice' | 'mock';
  targetType: 'chapter' | 'unit' | 'mock';
  targetId: string | number;
  initialTimeMinutes?: number;
  onExit: () => void;
  onCompleteMock?: (result: {
    total: number;
    score: number;
    correctAnswers: number;
    wrongQuestions: Question[];
    answers: Record<string, string>;
  }) => void;
}

export const QuizPlayer: React.FC<QuizPlayerProps> = ({
  questions,
  title,
  mode,
  targetType,
  targetId,
  initialTimeMinutes = 20,
  onExit,
  onCompleteMock,
}) => {
  const { language, toggleLanguage, t } = useLanguage();

  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState<Record<string, string>>({});
  const [showExplanation, setShowExplanation] = useState<Record<string, boolean>>({});
  const [flagged, setFlagged] = useState<Record<string, boolean>>({});
  const [timeLeft, setTimeLeft] = useState(initialTimeMinutes * 60);
  const [showPalette, setShowPalette] = useState(false);
  const [showConfirmSubmit, setShowConfirmSubmit] = useState(false);

  // Timer for Mock Exam
  useEffect(() => {
    if (mode !== 'mock') return;
    const interval = setInterval(() => {
      setTimeLeft((prev) => {
        if (prev <= 1) {
          clearInterval(interval);
          handleFinishExam();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(interval);
  }, [mode]);

  if (!questions || questions.length === 0) {
    return (
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-8 text-center max-w-xl mx-auto space-y-4">
        <AlertCircle className="w-12 h-12 text-amber-400 mx-auto" />
        <h2 className="text-xl font-bold text-white">{t('noQuestionsFound')}</h2>
        <p className="text-sm text-slate-400">
          {language === 'zh'
            ? '該分類下尚無已發布（Published）的題目，請在題目審核後台進行核實與發布。'
            : 'No questions have reached the Published state for this selection. Review and publish questions in CMS.'}
        </p>
        <button
          onClick={onExit}
          className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-lg text-sm transition"
        >
          {t('back')}
        </button>
      </div>
    );
  }

  const currentQuestion = questions[currentIndex];
  const qId = currentQuestion.id;
  const currentSelection = selectedAnswers[qId];
  const isAnswered = currentSelection !== undefined;
  const isCorrect = currentSelection === currentQuestion.correct_answer;
  const isRevealed = mode === 'practice' ? showExplanation[qId] || isAnswered : false;

  // Handle Option Select
  const handleSelectOption = (key: string) => {
    if (mode === 'practice' && isAnswered) return; // in practice mode, locks upon answering

    const updatedAnswers = { ...selectedAnswers, [qId]: key };
    setSelectedAnswers(updatedAnswers);

    if (mode === 'practice') {
      const correct = key === currentQuestion.correct_answer;
      setShowExplanation((prev) => ({ ...prev, [qId]: true }));
      storage.recordAnswer(currentQuestion, correct);
      if (!correct) {
        storage.addWrongQuestion(currentQuestion, key, targetType, targetId);
      }
    }
  };

  const handleToggleFlag = () => {
    setFlagged((prev) => ({ ...prev, [qId]: !prev[qId] }));
  };

  const handleFinishExam = () => {
    let score = 0;
    const wrongs: Question[] = [];

    questions.forEach((q) => {
      const ans = selectedAnswers[q.id];
      const correct = ans === q.correct_answer;
      storage.recordAnswer(q, correct);
      if (correct) {
        score += 1;
      } else {
        wrongs.push(q);
        storage.addWrongQuestion(q, ans || 'NONE', targetType, targetId);
      }
    });

    if (onCompleteMock) {
      onCompleteMock({
        total: questions.length,
        score,
        correctAnswers: score,
        wrongQuestions: wrongs,
        answers: selectedAnswers,
      });
    }
  };

  // Format Timer mm:ss
  const formatTime = (secs: number) => {
    const mins = Math.floor(secs / 60);
    const s = secs % 60;
    return `${mins.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  // Content resolution based on current language
  const questionContent =
    language === 'zh'
      ? currentQuestion.content_zh || currentQuestion.content_en
      : currentQuestion.content_en || currentQuestion.content_zh;

  const currentOptions =
    language === 'zh'
      ? currentQuestion.options_zh || currentQuestion.options_en
      : currentQuestion.options_en || currentQuestion.options_zh;

  const currentExplanation =
    language === 'zh'
      ? currentQuestion.explanation_zh || currentQuestion.explanation_en
      : currentQuestion.explanation_en || currentQuestion.explanation_zh;

  return (
    <div className="max-w-4xl mx-auto space-y-4">
      {/* Top Header Card */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 shadow-sm flex items-center justify-between gap-3">
        <div className="flex items-center space-x-3">
          <button
            onClick={onExit}
            className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition"
            title={t('back')}
          >
            <ArrowLeft className="w-5 h-5" />
          </button>
          <div>
            <div className="flex items-center space-x-2">
              <span className="text-xs font-mono font-bold uppercase tracking-wider text-cyan-400">
                {mode === 'mock' ? t('examMode') : t('practiceMode')}
              </span>
              <span className="text-slate-600">•</span>
              <span className="text-xs text-slate-400 font-mono">
                {currentIndex + 1} / {questions.length}
              </span>
            </div>
            <h2 className="text-base font-bold text-white tracking-tight truncate max-w-sm sm:max-w-md">
              {title}
            </h2>
          </div>
        </div>

        <div className="flex items-center space-x-2 sm:space-x-3">
          {/* Mock Timer */}
          {mode === 'mock' && (
            <div
              className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg font-mono text-xs sm:text-sm font-bold border ${
                timeLeft < 300
                  ? 'bg-rose-950/80 text-rose-300 border-rose-800 animate-pulse'
                  : 'bg-slate-800 text-cyan-300 border-slate-700'
              }`}
            >
              <Timer className="w-4 h-4" />
              <span>{formatTime(timeLeft)}</span>
            </div>
          )}

          {/* Quick Bilingual Switch for Question */}
          <button
            onClick={toggleLanguage}
            className="flex items-center space-x-1 px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-medium text-slate-200 transition"
            title="Instant toggle question language without resetting answers"
          >
            <Globe className="w-3.5 h-3.5 text-cyan-400" />
            <span className="font-mono">{language === 'zh' ? '繁中' : 'EN'}</span>
          </button>

          {/* Question Palette Button */}
          <button
            onClick={() => setShowPalette(!showPalette)}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold border transition ${
              showPalette
                ? 'bg-cyan-600 text-white border-cyan-500'
                : 'bg-slate-800 hover:bg-slate-700 text-slate-300 border-slate-700'
            }`}
          >
            {t('questionIndex')}
          </button>
        </div>
      </div>

      {/* Palette Drawer */}
      {showPalette && (
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 shadow-md space-y-3">
          <div className="flex items-center justify-between text-xs text-slate-400 border-b border-slate-800 pb-2">
            <span className="font-semibold text-slate-200">{t('questionIndex')}</span>
            <div className="flex items-center space-x-3">
              <span className="flex items-center space-x-1">
                <span className="w-2.5 h-2.5 rounded-full bg-cyan-600 inline-block"></span>
                <span>{language === 'zh' ? '已答' : 'Answered'}</span>
              </span>
              <span className="flex items-center space-x-1">
                <span className="w-2.5 h-2.5 rounded-full bg-amber-500 inline-block"></span>
                <span>{language === 'zh' ? '已標記' : 'Flagged'}</span>
              </span>
              <span className="flex items-center space-x-1">
                <span className="w-2.5 h-2.5 rounded-full bg-slate-800 border border-slate-700 inline-block"></span>
                <span>{language === 'zh' ? '未答' : 'Unanswered'}</span>
              </span>
            </div>
          </div>
          <div className="grid grid-cols-6 sm:grid-cols-10 gap-2">
            {questions.map((q, idx) => {
              const answered = selectedAnswers[q.id] !== undefined;
              const isFlag = flagged[q.id];
              const isCurr = idx === currentIndex;
              return (
                <button
                  key={q.id}
                  onClick={() => {
                    setCurrentIndex(idx);
                    setShowPalette(false);
                  }}
                  className={`h-9 rounded-lg text-xs font-mono font-bold transition flex items-center justify-center relative border ${
                    isCurr
                      ? 'ring-2 ring-cyan-400 border-cyan-400 bg-cyan-950 text-cyan-200'
                      : answered
                      ? 'bg-cyan-600/30 text-cyan-200 border-cyan-500/50'
                      : 'bg-slate-800 text-slate-400 border-slate-700 hover:border-slate-600'
                  }`}
                >
                  <span>{idx + 1}</span>
                  {isFlag && (
                    <span className="absolute -top-1 -right-1 w-2 h-2 rounded-full bg-amber-400"></span>
                  )}
                </button>
              );
            })}
          </div>
        </div>
      )}

      {/* Main Question Card */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 sm:p-7 shadow-lg space-y-6">
        {/* Question Header & Badges */}
        <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-4">
          <div className="flex flex-wrap items-center gap-2">
            <span className="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-mono text-xs font-bold border border-slate-700">
              #{currentIndex + 1}
            </span>
            {currentQuestion.units?.map((u) => (
              <span
                key={u}
                className="px-2 py-0.5 rounded bg-cyan-950 text-cyan-300 border border-cyan-800/60 font-mono text-xs"
              >
                {u}
              </span>
            ))}
            {currentQuestion.chapters?.map((ch) => (
              <span
                key={ch.chapter_id}
                className="px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700 font-mono text-xs"
              >
                Ch {ch.chapter_id} {ch.sub_topic_id && `(${ch.sub_topic_id})`}
              </span>
            ))}
          </div>

          {/* Flag Button */}
          <button
            onClick={handleToggleFlag}
            className={`flex items-center space-x-1.5 px-2.5 py-1 rounded-md text-xs font-medium border transition ${
              flagged[qId]
                ? 'bg-amber-950 text-amber-300 border-amber-700'
                : 'bg-slate-800/60 text-slate-400 border-slate-700/60 hover:text-slate-200'
            }`}
          >
            <Flag className={`w-3.5 h-3.5 ${flagged[qId] ? 'fill-amber-400 text-amber-400' : ''}`} />
            <span>{flagged[qId] ? t('unflag') : t('flagForReview')}</span>
          </button>
        </div>

        {/* Question Text */}
        <div className="text-base sm:text-lg font-medium text-slate-100 leading-relaxed">
          {questionContent}
        </div>

        {/* Options List */}
        <div className="space-y-3 pt-2">
          {Object.entries(currentOptions || {}).map(([key, value]) => {
            const isSelected = currentSelection === key;
            const isCorrectOption = key === currentQuestion.correct_answer;

            let optionStyle =
              'border-slate-800 bg-slate-800/40 hover:bg-slate-800/80 hover:border-slate-700 text-slate-200';
            let badgeStyle = 'bg-slate-800 text-slate-400 border-slate-700';

            if (mode === 'practice' && isRevealed) {
              if (isCorrectOption) {
                optionStyle = 'border-emerald-600 bg-emerald-950/40 text-emerald-100';
                badgeStyle = 'bg-emerald-600 text-white border-emerald-500';
              } else if (isSelected && !isCorrectOption) {
                optionStyle = 'border-rose-600 bg-rose-950/40 text-rose-100';
                badgeStyle = 'bg-rose-600 text-white border-rose-500';
              }
            } else if (isSelected) {
              optionStyle = 'border-cyan-500 bg-cyan-950/40 text-cyan-100 shadow-sm';
              badgeStyle = 'bg-cyan-600 text-white border-cyan-500';
            }

            return (
              <button
                key={key}
                onClick={() => handleSelectOption(key)}
                className={`w-full text-left p-4 rounded-xl border transition-all flex items-start space-x-3 group ${optionStyle}`}
              >
                <span
                  className={`w-7 h-7 rounded-lg flex items-center justify-center font-mono font-bold text-xs shrink-0 border transition ${badgeStyle}`}
                >
                  {key}
                </span>
                <span className="text-sm sm:text-base pt-0.5 leading-snug flex-1">
                  {value}
                </span>
                {mode === 'practice' && isRevealed && isCorrectOption && (
                  <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />
                )}
                {mode === 'practice' && isRevealed && isSelected && !isCorrectOption && (
                  <XCircle className="w-5 h-5 text-rose-400 shrink-0 mt-0.5" />
                )}
              </button>
            );
          })}
        </div>

        {/* Practice Mode Explanation Box */}
        {mode === 'practice' && isRevealed && (
          <div className="mt-6 p-5 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
            <div className="flex items-center justify-between border-b border-slate-800/80 pb-2">
              <div className="flex items-center space-x-2">
                {isCorrect ? (
                  <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                ) : (
                  <XCircle className="w-5 h-5 text-rose-400" />
                )}
                <span
                  className={`text-sm font-bold ${
                    isCorrect ? 'text-emerald-400' : 'text-rose-400'
                  }`}
                >
                  {isCorrect ? t('correct') : t('incorrect')}
                </span>
                <span className="text-xs text-slate-400 font-mono">
                  ({t('correctAnswer')}: {currentQuestion.correct_answer})
                </span>
              </div>
            </div>

            {/* Explanation text */}
            <div className="text-sm text-slate-300 leading-relaxed">
              <span className="font-semibold text-cyan-300 mr-2">
                {t('explanation')}:
              </span>
              {currentExplanation}
            </div>

            {/* Source standard reference citation */}
            {currentQuestion.source_reference && (
              <div className="pt-2 flex items-start space-x-2 text-xs text-cyan-400 font-mono bg-cyan-950/40 p-2.5 rounded border border-cyan-900/60">
                <FileText className="w-4 h-4 shrink-0 mt-0.5 text-cyan-300" />
                <div>
                  <span className="font-bold uppercase tracking-wider text-cyan-300">
                    {t('sourceRef')}:
                  </span>{' '}
                  {currentQuestion.source_reference}
                </div>
              </div>
            )}
          </div>
        )}

        {/* Navigation Bar */}
        <div className="pt-4 border-t border-slate-800 flex items-center justify-between">
          <button
            onClick={() => setCurrentIndex((prev) => Math.max(0, prev - 1))}
            disabled={currentIndex === 0}
            className="flex items-center space-x-1.5 px-4 py-2 rounded-lg text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 disabled:opacity-40 disabled:cursor-not-allowed transition"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>{t('prev')}</span>
          </button>

          {currentIndex === questions.length - 1 ? (
            mode === 'mock' ? (
              <button
                onClick={() => setShowConfirmSubmit(true)}
                className="flex items-center space-x-1.5 px-5 py-2 rounded-lg text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white shadow-sm transition"
              >
                <Send className="w-4 h-4" />
                <span>{t('submit')}</span>
              </button>
            ) : (
              <button
                onClick={onExit}
                className="flex items-center space-x-1.5 px-5 py-2 rounded-lg text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white shadow-sm transition"
              >
                <span>{language === 'zh' ? '完成練習' : 'Finish Practice'}</span>
              </button>
            )
          ) : (
            <button
              onClick={() => setCurrentIndex((prev) => Math.min(questions.length - 1, prev + 1))}
              className="flex items-center space-x-1.5 px-4 py-2 rounded-lg text-xs font-semibold bg-cyan-600 hover:bg-cyan-500 text-white shadow-sm transition"
            >
              <span>{t('next')}</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>

      {/* Confirm Submit Dialog for Mock Exam */}
      {showConfirmSubmit && (
        <div className="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 max-w-md w-full shadow-2xl space-y-4">
            <h3 className="text-lg font-bold text-white">
              {language === 'zh' ? '確認提交考卷？' : 'Submit Mock Exam?'}
            </h3>
            <p className="text-sm text-slate-300">
              {language === 'zh'
                ? `您已完成 ${Object.keys(selectedAnswers).length} / ${questions.length} 題。提交後將立即計算評分並生成詳細診斷報告。`
                : `You answered ${Object.keys(selectedAnswers).length} of ${questions.length} questions. An assessment diagnostic report will be generated immediately.`}
            </p>
            <div className="flex justify-end space-x-3 pt-2">
              <button
                onClick={() => setShowConfirmSubmit(false)}
                className="px-4 py-2 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs font-semibold"
              >
                {t('cancel')}
              </button>
              <button
                onClick={() => {
                  setShowConfirmSubmit(false);
                  handleFinishExam();
                }}
                className="px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold shadow-sm"
              >
                {t('confirm')}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
