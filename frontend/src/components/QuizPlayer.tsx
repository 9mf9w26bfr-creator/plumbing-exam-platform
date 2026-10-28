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
  FileText,
  Grid,
  X
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
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [mode]);

  if (!questions || questions.length === 0) {
    return (
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 sm:p-8 text-center max-w-xl mx-auto space-y-4 my-8">
        <AlertCircle className="w-10 h-10 sm:w-12 sm:h-12 text-amber-400 mx-auto" />
        <h2 className="text-lg sm:text-xl font-bold text-white">{t('noQuestionsFound')}</h2>
        <p className="text-xs sm:text-sm text-slate-400">
          {language === 'zh'
            ? '該分類下尚無已發布（Published）的題目，請在題目審核後台進行核實與發布。'
            : 'No published questions found in this category.'}
        </p>
        <button
          onClick={onExit}
          className="px-4 py-2 bg-slate-800 hover:bg-slate-700 active:scale-95 text-white rounded-lg text-xs font-semibold transition"
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
    if (mode === 'practice' && isAnswered) return;

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

  const formatTime = (secs: number) => {
    const mins = Math.floor(secs / 60);
    const s = secs % 60;
    return `${mins.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

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
    <div className="max-w-4xl mx-auto space-y-3 sm:space-y-4 pb-20 sm:pb-6">
      {/* Top Mobile-Sticky Bar */}
      <div className="bg-slate-900/95 backdrop-blur border border-slate-800 rounded-xl p-3 sm:p-4 shadow-sm sticky top-14 sm:top-16 z-30">
        <div className="flex items-center justify-between gap-2">
          {/* Left: Back & Progress */}
          <div className="flex items-center space-x-2 sm:space-x-3 truncate">
            <button
              onClick={onExit}
              className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 active:scale-90 text-slate-300 transition shrink-0"
              title={t('back')}
            >
              <ArrowLeft className="w-4 h-4 sm:w-5 sm:h-5" />
            </button>
            <div className="truncate">
              <div className="flex items-center space-x-1.5">
                <span className="text-[10px] sm:text-xs font-mono font-bold uppercase tracking-wider text-cyan-400">
                  {mode === 'mock' ? t('examMode') : t('practiceMode')}
                </span>
                <span className="text-slate-600">•</span>
                <span className="text-[11px] sm:text-xs text-slate-400 font-mono font-bold">
                  {currentIndex + 1} / {questions.length}
                </span>
              </div>
              <h2 className="text-xs sm:text-sm font-bold text-white tracking-tight truncate max-w-[180px] xs:max-w-xs sm:max-w-md">
                {title}
              </h2>
            </div>
          </div>

          {/* Right: Timer & Tools */}
          <div className="flex items-center space-x-1.5 sm:space-x-2 shrink-0">
            {/* Mock Timer */}
            {mode === 'mock' && (
              <div
                className={`flex items-center space-x-1 px-2 py-1 sm:px-2.5 sm:py-1.5 rounded-md font-mono text-xs font-bold border ${
                  timeLeft < 300
                    ? 'bg-rose-950/90 text-rose-300 border-rose-800 animate-pulse'
                    : 'bg-slate-800 text-cyan-300 border-slate-700'
                }`}
              >
                <Timer className="w-3.5 h-3.5" />
                <span>{formatTime(timeLeft)}</span>
              </div>
            )}

            {/* Instant Bilingual Switch */}
            <button
              onClick={toggleLanguage}
              className="flex items-center space-x-1 px-2 py-1 sm:px-2.5 sm:py-1.5 rounded-md bg-slate-800 hover:bg-slate-700 active:scale-95 border border-slate-700 text-xs font-medium text-slate-200 transition"
              title="Instant language toggle"
            >
              <Globe className="w-3 h-3 text-cyan-400" />
              <span className="font-mono text-[11px]">{language === 'zh' ? '繁中' : 'EN'}</span>
            </button>

            {/* Palette Trigger */}
            <button
              onClick={() => setShowPalette(true)}
              className="p-1.5 sm:px-2.5 sm:py-1.5 rounded-md bg-slate-800 hover:bg-slate-700 active:scale-95 text-slate-300 border border-slate-700 text-xs font-semibold flex items-center space-x-1"
              title={t('questionIndex')}
            >
              <Grid className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">{t('questionIndex')}</span>
            </button>
          </div>
        </div>

        {/* Linear Progress Bar */}
        <div className="w-full bg-slate-800 h-1 rounded-full mt-2.5 overflow-hidden">
          <div
            className="bg-cyan-500 h-full transition-all duration-300"
            style={{ width: `${((currentIndex + 1) / questions.length) * 100}%` }}
          ></div>
        </div>
      </div>

      {/* Main Question Card (Touch-First) */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-7 shadow-lg space-y-4 sm:space-y-6">
        {/* Question Header & Badges */}
        <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
          <div className="flex flex-wrap items-center gap-1.5">
            <span className="px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-mono text-[11px] font-bold border border-slate-700">
              Q{currentIndex + 1}
            </span>
            {currentQuestion.units?.map((u) => (
              <span
                key={u}
                className="px-1.5 py-0.5 rounded bg-cyan-950 text-cyan-300 border border-cyan-800/60 font-mono text-[10px] sm:text-xs"
              >
                {u}
              </span>
            ))}
            {currentQuestion.chapters?.map((ch) => (
              <span
                key={ch.chapter_id}
                className="px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700 font-mono text-[10px] sm:text-xs"
              >
                Ch {ch.chapter_id}
              </span>
            ))}
          </div>

          {/* Flag Button */}
          <button
            onClick={handleToggleFlag}
            className={`flex items-center space-x-1 px-2 py-1 rounded-md text-[11px] font-medium border transition active:scale-95 ${
              flagged[qId]
                ? 'bg-amber-950 text-amber-300 border-amber-700'
                : 'bg-slate-800/60 text-slate-400 border-slate-700/60 hover:text-slate-200'
            }`}
          >
            <Flag className={`w-3 h-3 ${flagged[qId] ? 'fill-amber-400 text-amber-400' : ''}`} />
            <span>{flagged[qId] ? t('unflag') : t('flagForReview')}</span>
          </button>
        </div>

        {/* Question Text */}
        <div className="text-base sm:text-lg font-medium text-slate-100 leading-relaxed select-text">
          {questionContent}
        </div>

        {/* Touch-Friendly Options (Min-Height 48px) */}
        <div className="space-y-2.5 sm:space-y-3 pt-1">
          {Object.entries(currentOptions || {}).map(([key, value]) => {
            const isSelected = currentSelection === key;
            const isCorrectOption = key === currentQuestion.correct_answer;

            let optionStyle =
              'border-slate-800 bg-slate-800/40 hover:bg-slate-800/80 active:bg-slate-800 text-slate-200';
            let badgeStyle = 'bg-slate-800 text-slate-400 border-slate-700';

            if (mode === 'practice' && isRevealed) {
              if (isCorrectOption) {
                optionStyle = 'border-emerald-600 bg-emerald-950/50 text-emerald-100 shadow-emerald-950/30';
                badgeStyle = 'bg-emerald-600 text-white border-emerald-500';
              } else if (isSelected && !isCorrectOption) {
                optionStyle = 'border-rose-600 bg-rose-950/50 text-rose-100 shadow-rose-950/30';
                badgeStyle = 'bg-rose-600 text-white border-rose-500';
              }
            } else if (isSelected) {
              optionStyle = 'border-cyan-500 bg-cyan-950/50 text-cyan-100 ring-1 ring-cyan-500/50';
              badgeStyle = 'bg-cyan-600 text-white border-cyan-500';
            }

            return (
              <button
                key={key}
                onClick={() => handleSelectOption(key)}
                className={`w-full text-left p-3.5 sm:p-4 rounded-xl border transition-all flex items-start space-x-3 active:scale-[0.99] select-none min-h-[50px] ${optionStyle}`}
              >
                <span
                  className={`w-7 h-7 rounded-lg flex items-center justify-center font-mono font-bold text-xs shrink-0 border mt-0.5 transition ${badgeStyle}`}
                >
                  {key}
                </span>
                <span className="text-sm sm:text-base leading-snug flex-1 pt-0.5">
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
          <div className="mt-4 sm:mt-6 p-4 sm:p-5 rounded-xl bg-slate-950 border border-slate-800 space-y-3 animate-in fade-in-50 duration-200">
            <div className="flex items-center justify-between border-b border-slate-800/80 pb-2">
              <div className="flex items-center space-x-2">
                {isCorrect ? (
                  <CheckCircle2 className="w-4 h-4 sm:w-5 sm:h-5 text-emerald-400" />
                ) : (
                  <XCircle className="w-4 h-4 sm:w-5 sm:h-5 text-rose-400" />
                )}
                <span
                  className={`text-xs sm:text-sm font-bold ${
                    isCorrect ? 'text-emerald-400' : 'text-rose-400'
                  }`}
                >
                  {isCorrect ? t('correct') : t('incorrect')}
                </span>
                <span className="text-[11px] sm:text-xs text-slate-400 font-mono">
                  ({t('correctAnswer')}: {currentQuestion.correct_answer})
                </span>
              </div>
            </div>

            {/* Explanation text */}
            <div className="text-xs sm:text-sm text-slate-300 leading-relaxed">
              <span className="font-semibold text-cyan-300 mr-1.5">
                {t('explanation')}:
              </span>
              {currentExplanation}
            </div>

            {/* Source Reference */}
            {currentQuestion.source_reference && (
              <div className="pt-2 flex items-start space-x-2 text-[11px] sm:text-xs text-cyan-400 font-mono bg-cyan-950/40 p-2.5 rounded border border-cyan-900/60">
                <FileText className="w-3.5 h-3.5 shrink-0 mt-0.5 text-cyan-300" />
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
      </div>

      {/* Fixed Mobile Bottom Action Bar (Thumb-Accessible) */}
      <div className="fixed bottom-0 left-0 right-0 z-30 bg-slate-900/98 backdrop-blur border-t border-slate-800 p-2.5 sm:relative sm:p-0 sm:bg-transparent sm:border-0">
        <div className="max-w-4xl mx-auto flex items-center justify-between gap-2">
          {/* Previous Button */}
          <button
            onClick={() => setCurrentIndex((prev) => Math.max(0, prev - 1))}
            disabled={currentIndex === 0}
            className="flex-1 sm:flex-initial flex items-center justify-center space-x-1.5 py-3 sm:py-2 px-4 rounded-xl text-xs sm:text-sm font-semibold bg-slate-800 hover:bg-slate-700 active:bg-slate-750 text-slate-300 disabled:opacity-30 disabled:cursor-not-allowed transition border border-slate-700"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>{t('prev')}</span>
          </button>

          {/* Center Mobile Palette Button */}
          <button
            onClick={() => setShowPalette(true)}
            className="sm:hidden flex items-center justify-center space-x-1 py-3 px-3 rounded-xl text-xs font-mono font-bold bg-slate-800 text-cyan-300 border border-slate-700"
          >
            <Grid className="w-3.5 h-3.5" />
            <span>{currentIndex + 1}/{questions.length}</span>
          </button>

          {/* Next or Submit Button */}
          {currentIndex === questions.length - 1 ? (
            mode === 'mock' ? (
              <button
                onClick={() => setShowConfirmSubmit(true)}
                className="flex-1 sm:flex-initial flex items-center justify-center space-x-1.5 py-3 sm:py-2 px-5 rounded-xl text-xs sm:text-sm font-bold bg-emerald-600 hover:bg-emerald-500 active:scale-98 text-white shadow-md shadow-emerald-950/40 transition"
              >
                <Send className="w-4 h-4" />
                <span>{t('submit')}</span>
              </button>
            ) : (
              <button
                onClick={onExit}
                className="flex-1 sm:flex-initial flex items-center justify-center space-x-1.5 py-3 sm:py-2 px-5 rounded-xl text-xs sm:text-sm font-bold bg-cyan-600 hover:bg-cyan-500 active:scale-98 text-white shadow-md shadow-cyan-950/40 transition"
              >
                <span>{language === 'zh' ? '完成練習' : 'Finish Practice'}</span>
              </button>
            )
          ) : (
            <button
              onClick={() => setCurrentIndex((prev) => Math.min(questions.length - 1, prev + 1))}
              className="flex-1 sm:flex-initial flex items-center justify-center space-x-1.5 py-3 sm:py-2 px-5 rounded-xl text-xs sm:text-sm font-semibold bg-cyan-600 hover:bg-cyan-500 active:bg-cyan-650 active:scale-98 text-white shadow-md shadow-cyan-950/40 transition"
            >
              <span>{t('next')}</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>

      {/* Mobile-First Bottom Sheet Drawer for Question Palette (答題卡) */}
      {showPalette && (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex flex-col justify-end sm:justify-center items-center p-0 sm:p-4 animate-in fade-in duration-150">
          <div className="bg-slate-900 border-t sm:border border-slate-800 rounded-t-2xl sm:rounded-2xl max-w-lg w-full max-h-[85vh] flex flex-col shadow-2xl animate-in slide-in-from-bottom-6 duration-200">
            {/* Drawer Header */}
            <div className="p-4 border-b border-slate-800 flex items-center justify-between">
              <div>
                <h3 className="text-base font-bold text-white flex items-center space-x-2">
                  <Grid className="w-4 h-4 text-cyan-400" />
                  <span>{t('questionIndex')}</span>
                </h3>
                <p className="text-[11px] text-slate-400 mt-0.5">
                  {language === 'zh' ? '點擊題號快速直達題目' : 'Tap any question number to jump'}
                </p>
              </div>
              <button
                onClick={() => setShowPalette(false)}
                className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Legend */}
            <div className="px-4 py-2.5 bg-slate-950/70 border-b border-slate-800 flex items-center justify-around text-xs text-slate-300">
              <span className="flex items-center space-x-1.5">
                <span className="w-2.5 h-2.5 rounded bg-cyan-600 inline-block"></span>
                <span>{language === 'zh' ? '已作答' : 'Answered'}</span>
              </span>
              <span className="flex items-center space-x-1.5">
                <span className="w-2.5 h-2.5 rounded bg-amber-500 inline-block"></span>
                <span>{language === 'zh' ? '已標記' : 'Flagged'}</span>
              </span>
              <span className="flex items-center space-x-1.5">
                <span className="w-2.5 h-2.5 rounded bg-slate-800 border border-slate-700 inline-block"></span>
                <span>{language === 'zh' ? '未作答' : 'Unanswered'}</span>
              </span>
            </div>

            {/* Questions Grid (Thumb-friendly scrolling) */}
            <div className="p-4 overflow-y-auto flex-1 overscroll-contain">
              <div className="grid grid-cols-5 sm:grid-cols-8 gap-2">
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
                      className={`h-11 sm:h-10 rounded-xl text-xs font-mono font-bold transition flex items-center justify-center relative active:scale-95 border ${
                        isCurr
                          ? 'ring-2 ring-cyan-400 border-cyan-400 bg-cyan-950 text-cyan-200'
                          : answered
                          ? 'bg-cyan-600/30 text-cyan-200 border-cyan-500/50'
                          : 'bg-slate-800/80 text-slate-400 border-slate-700/80'
                      }`}
                    >
                      <span>{idx + 1}</span>
                      {isFlag && (
                        <span className="absolute top-1 right-1 w-2 h-2 rounded-full bg-amber-400"></span>
                      )}
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Drawer Footer */}
            <div className="p-3 border-t border-slate-800 bg-slate-950/60 text-center">
              <button
                onClick={() => setShowPalette(false)}
                className="w-full py-2.5 rounded-xl bg-slate-800 text-slate-200 font-semibold text-xs active:bg-slate-700"
              >
                {t('cancel')}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Confirm Submit Dialog for Mock Exam (Mobile Bottom-aligned or Centered) */}
      {showConfirmSubmit && (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 max-w-sm sm:max-w-md w-full shadow-2xl space-y-4">
            <h3 className="text-base sm:text-lg font-bold text-white">
              {language === 'zh' ? '確認提交考卷？' : 'Submit Mock Exam?'}
            </h3>
            <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
              {language === 'zh'
                ? `您已完成 ${Object.keys(selectedAnswers).length} / ${questions.length} 題。交卷後將立即計算評分、PASS/FAIL 及格判定並自動匯出錯題本。`
                : `You answered ${Object.keys(selectedAnswers).length} of ${questions.length} questions. An assessment diagnostic report will be generated immediately.`}
            </p>
            <div className="flex space-x-2 pt-2">
              <button
                onClick={() => setShowConfirmSubmit(false)}
                className="flex-1 py-2.5 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 active:scale-95 text-xs font-semibold"
              >
                {t('cancel')}
              </button>
              <button
                onClick={() => {
                  setShowConfirmSubmit(false);
                  handleFinishExam();
                }}
                className="flex-1 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 active:scale-95 text-white text-xs font-bold shadow-md shadow-emerald-950/40"
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
