'use client';

import React from 'react';
import { Question } from '../types';
import { useLanguage } from '../context/LanguageContext';
import { Award, CheckCircle2, XCircle, RotateCcw, AlertTriangle, ArrowRight } from 'lucide-react';

interface ExamResultModalProps {
  total: number;
  score: number;
  wrongQuestions: Question[];
  onRetake: () => void;
  onGoToWrong: () => void;
  onExit: () => void;
}

export const ExamResultModal: React.FC<ExamResultModalProps> = ({
  total,
  score,
  wrongQuestions,
  onRetake,
  onGoToWrong,
  onExit,
}) => {
  const { language, t } = useLanguage();
  const percentage = Math.round((score / total) * 100);
  const isPassed = percentage >= 60;

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      {/* Result Card */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl text-center space-y-6">
        <div className="inline-flex p-4 rounded-2xl bg-slate-800/80 border border-slate-700/60 mx-auto">
          <Award
            className={`w-14 h-14 ${
              isPassed ? 'text-emerald-400' : 'text-rose-400'
            }`}
          />
        </div>

        <div>
          <span
            className={`inline-block px-3 py-1 rounded-full text-xs font-mono font-bold uppercase tracking-wider mb-2 border ${
              isPassed
                ? 'bg-emerald-950/80 text-emerald-300 border-emerald-800'
                : 'bg-rose-950/80 text-rose-300 border-rose-800'
            }`}
          >
            {isPassed ? t('passed') : t('failed')}
          </span>
          <h1 className="text-3xl font-black text-white tracking-tight">
            {percentage}%
          </h1>
          <p className="text-sm text-slate-400 mt-1">
            {language === 'zh'
              ? `總共 ${total} 題，答對 ${score} 題，答錯 ${wrongQuestions.length} 題`
              : `Total ${total} questions, ${score} correct, ${wrongQuestions.length} incorrect`}
          </p>
        </div>

        {/* C&G Standard Notice */}
        <div className="p-3 bg-slate-950 rounded-xl border border-slate-800/80 text-xs text-slate-400 font-mono">
          {t('passThresholdNotice')} (≥ 60% PASS)
        </div>

        {/* Quick Stats Grid */}
        <div className="grid grid-cols-2 gap-3 pt-2">
          <div className="bg-slate-800/50 border border-slate-700/50 p-4 rounded-xl flex items-center space-x-3">
            <CheckCircle2 className="w-6 h-6 text-emerald-400 shrink-0" />
            <div className="text-left">
              <div className="text-xs text-slate-400">{t('correct')}</div>
              <div className="text-lg font-bold font-mono text-emerald-300">{score}</div>
            </div>
          </div>
          <div className="bg-slate-800/50 border border-slate-700/50 p-4 rounded-xl flex items-center space-x-3">
            <XCircle className="w-6 h-6 text-rose-400 shrink-0" />
            <div className="text-left">
              <div className="text-xs text-slate-400">{t('incorrect')}</div>
              <div className="text-lg font-mono font-bold text-rose-300">
                {wrongQuestions.length}
              </div>
            </div>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-4 border-t border-slate-800">
          {wrongQuestions.length > 0 && (
            <button
              onClick={onGoToWrong}
              className="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white text-xs font-bold shadow-md transition flex items-center justify-center space-x-2"
            >
              <AlertTriangle className="w-4 h-4" />
              <span>{t('reviewMistakes')} ({wrongQuestions.length})</span>
            </button>
          )}

          <button
            onClick={onRetake}
            className="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 transition flex items-center justify-center space-x-2"
          >
            <RotateCcw className="w-4 h-4" />
            <span>{t('retakeExam')}</span>
          </button>

          <button
            onClick={onExit}
            className="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold transition flex items-center justify-center space-x-2"
          >
            <span>{language === 'zh' ? '返回主頁' : 'Back to Home'}</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
};
