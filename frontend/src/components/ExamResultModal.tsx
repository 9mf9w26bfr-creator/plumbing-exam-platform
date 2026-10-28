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
    <div className="max-w-xl mx-auto space-y-4 sm:space-y-6 pb-20 md:pb-6 px-1">
      {/* Result Card */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-8 shadow-2xl text-center space-y-5 sm:space-y-6">
        <div className="inline-flex p-3 sm:p-4 rounded-2xl bg-slate-800/80 border border-slate-700/60 mx-auto">
          <Award
            className={`w-12 h-12 sm:w-14 sm:h-14 ${
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
          <h1 className="text-3xl sm:text-4xl font-black text-white tracking-tight">
            {percentage}%
          </h1>
          <p className="text-xs sm:text-sm text-slate-400 mt-1">
            {language === 'zh'
              ? `總共 ${total} 題，答對 ${score} 題，答錯 ${wrongQuestions.length} 題`
              : `Total ${total} questions, ${score} correct, ${wrongQuestions.length} incorrect`}
          </p>
        </div>

        {/* C&G Standard Notice */}
        <div className="p-3 bg-slate-950 rounded-xl border border-slate-800/80 text-[11px] sm:text-xs text-slate-400 font-mono">
          {t('passThresholdNotice')} (≥ 60% PASS)
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-2 gap-2 sm:gap-3">
          <div className="bg-slate-800/50 border border-slate-700/50 p-3 sm:p-4 rounded-xl flex items-center space-x-2.5">
            <CheckCircle2 className="w-5 h-5 sm:w-6 sm:h-6 text-emerald-400 shrink-0" />
            <div className="text-left">
              <div className="text-[10px] sm:text-xs text-slate-400">{t('correct')}</div>
              <div className="text-base sm:text-lg font-bold font-mono text-emerald-300">{score}</div>
            </div>
          </div>
          <div className="bg-slate-800/50 border border-slate-700/50 p-3 sm:p-4 rounded-xl flex items-center space-x-2.5">
            <XCircle className="w-5 h-5 sm:w-6 sm:h-6 text-rose-400 shrink-0" />
            <div className="text-left">
              <div className="text-[10px] sm:text-xs text-slate-400">{t('incorrect')}</div>
              <div className="text-base sm:text-lg font-mono font-bold text-rose-300">
                {wrongQuestions.length}
              </div>
            </div>
          </div>
        </div>

        {/* Action Buttons (Mobile-First Stacked) */}
        <div className="flex flex-col sm:flex-row items-stretch justify-center gap-2 sm:gap-3 pt-3 border-t border-slate-800">
          {wrongQuestions.length > 0 && (
            <button
              onClick={onGoToWrong}
              className="py-3 px-4 rounded-xl bg-rose-600 hover:bg-rose-500 active:scale-98 text-white text-xs font-bold shadow-md transition flex items-center justify-center space-x-1.5"
            >
              <AlertTriangle className="w-4 h-4" />
              <span>{t('reviewMistakes')} ({wrongQuestions.length})</span>
            </button>
          )}

          <button
            onClick={onRetake}
            className="py-3 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 active:scale-98 text-slate-200 text-xs font-semibold border border-slate-700 transition flex items-center justify-center space-x-1.5"
          >
            <RotateCcw className="w-4 h-4" />
            <span>{t('retakeExam')}</span>
          </button>

          <button
            onClick={onExit}
            className="py-3 px-4 rounded-xl bg-cyan-600 hover:bg-cyan-500 active:scale-98 text-white text-xs font-bold transition flex items-center justify-center space-x-1.5"
          >
            <span>{language === 'zh' ? '返回主頁' : 'Back to Home'}</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
};
