'use client';

import React, { useState } from 'react';
import { useLanguage } from '../context/LanguageContext';
import { Timer, ShieldAlert, Play } from 'lucide-react';

interface MockExamConfigProps {
  onStartExam: (count: number, durationMinutes: number) => void;
  totalAvailable: number;
}

export const MockExamConfig: React.FC<MockExamConfigProps> = ({
  onStartExam,
  totalAvailable,
}) => {
  const { language, t } = useLanguage();
  const [questionCount, setQuestionCount] = useState<number>(10);
  const [duration, setDuration] = useState<number>(20);

  return (
    <div className="max-w-3xl mx-auto space-y-6">
      {/* Header */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-sm">
        <div className="flex items-center space-x-2 text-cyan-400 text-xs font-mono font-semibold uppercase tracking-wider mb-2">
          <Timer className="w-4 h-4" />
          <span>City & Guilds 6035 / 8202 Simulated Assessment</span>
        </div>
        <h1 className="text-2xl font-bold text-white tracking-tight">
          {language === 'zh'
            ? '全真模擬考試環境設置'
            : 'Simulated Timed Mock Examination'}
        </h1>
        <p className="text-sm text-slate-400 mt-1">
          {language === 'zh'
            ? '依照英國 City & Guilds 考試標準，隨機從已發布（Published）題庫中抽題。考試過程提供倒計時與答題卡索引。'
            : 'Simulates real examination conditions with random published questions, strict countdown timer, and exam palette.'}
        </p>
      </div>

      {/* Settings Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Question Count */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 space-y-4">
          <div className="flex items-center justify-between">
            <span className="text-sm font-bold text-white">
              {language === 'zh' ? '題目數量' : 'Number of Questions'}
            </span>
            <span className="text-xs font-mono text-cyan-400">
              {totalAvailable} {t('questionsAvailable')}
            </span>
          </div>
          <div className="grid grid-cols-3 gap-2">
            {[5, 10, 20].map((num) => (
              <button
                key={num}
                onClick={() => setQuestionCount(num)}
                className={`py-3 rounded-lg text-sm font-mono font-bold border transition ${
                  questionCount === num
                    ? 'bg-cyan-600 text-white border-cyan-500 shadow-sm'
                    : 'bg-slate-800 text-slate-300 border-slate-700 hover:border-slate-600'
                }`}
              >
                {num} Qs
              </button>
            ))}
          </div>
        </div>

        {/* Time Limit */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 space-y-4">
          <div className="flex items-center justify-between">
            <span className="text-sm font-bold text-white">
              {language === 'zh' ? '考試時限' : 'Time Limit'}
            </span>
            <span className="text-xs font-mono text-slate-400">
              ~2 {language === 'zh' ? '分鐘/題' : 'mins/Q'}
            </span>
          </div>
          <div className="grid grid-cols-3 gap-2">
            {[10, 20, 40].map((mins) => (
              <button
                key={mins}
                onClick={() => setDuration(mins)}
                className={`py-3 rounded-lg text-sm font-mono font-bold border transition ${
                  duration === mins
                    ? 'bg-cyan-600 text-white border-cyan-500 shadow-sm'
                    : 'bg-slate-800 text-slate-300 border-slate-700 hover:border-slate-600'
                }`}
              >
                {mins} Mins
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* C&G Guidelines Alert */}
      <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-5 space-y-3">
        <h3 className="text-xs font-mono uppercase font-bold text-slate-300 flex items-center space-x-2">
          <ShieldAlert className="w-4 h-4 text-cyan-400" />
          <span>{language === 'zh' ? '評估標準與考場規則' : 'Assessment Standards & Instructions'}</span>
        </h3>
        <ul className="text-xs text-slate-400 space-y-1.5 list-disc list-inside">
          <li>
            {language === 'zh'
              ? '及格分數基準線 (Pass Mark) 設為 60%。達到 80% 及以上為 Distinction 優秀級別。'
              : 'Pass threshold is 60%. A score of 80% or higher is graded as Distinction.'}
          </li>
          <li>
            {language === 'zh'
              ? '做題期間可隨時切換中/英雙語對照，不會丟失已選答案或干擾計時。'
              : 'You can toggle bilingual EN/ZH mode at any time without resetting selected choices.'}
          </li>
          <li>
            {language === 'zh'
              ? '交卷後將自動為您匯總錯題並存入個人本機錯題本，方便後續針對性補強。'
              : 'Mistakes will be automatically compiled into your local Mistake Notebook.'}
          </li>
        </ul>
      </div>

      {/* Start Button */}
      <button
        onClick={() => onStartExam(questionCount, duration)}
        className="w-full py-4 rounded-xl bg-gradient-to-r from-cyan-600 to-cyan-500 hover:from-cyan-500 hover:to-cyan-400 text-white font-bold text-base shadow-lg shadow-cyan-950/40 flex items-center justify-center space-x-2 transition"
      >
        <Play className="w-5 h-5 fill-white" />
        <span>{language === 'zh' ? '立即進入模擬考試' : 'Start Simulated Exam'}</span>
      </button>
    </div>
  );
};
