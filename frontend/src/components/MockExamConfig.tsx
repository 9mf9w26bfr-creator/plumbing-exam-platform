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
  const [questionCount, setQuestionCount] = useState<number>(20);
  const [duration, setDuration] = useState<number>(30);

  return (
    <div className="max-w-3xl mx-auto space-y-4 sm:space-y-6 pb-20 md:pb-6">
      {/* Header */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-6 shadow-sm">
        <div className="flex items-center space-x-1.5 text-cyan-400 text-[10px] sm:text-xs font-mono font-semibold uppercase tracking-wider mb-1.5">
          <Timer className="w-3.5 h-3.5" />
          <span>City & Guilds 6035 / 8202 Simulated Assessment</span>
        </div>
        <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
          {language === 'zh'
            ? '全真模擬考試環境設置'
            : 'Simulated Timed Mock Examination'}
        </h1>
        <p className="text-xs sm:text-sm text-slate-400 mt-1">
          {language === 'zh'
            ? '依照英國 City & Guilds 考試標準，隨機從 550+ 道題庫中動態抽題。配備嚴格倒計時與答題卡。'
            : 'Simulates official test conditions with random draws from 550+ questions, strict timer, and palette.'}
        </p>
      </div>

      {/* Settings Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
        {/* Question Count (Thumb-friendly touch) */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-5 space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-xs sm:text-sm font-bold text-white">
              {language === 'zh' ? '題目數量' : 'Number of Questions'}
            </span>
            <span className="text-[11px] font-mono text-cyan-400">
              {totalAvailable} {t('questionsAvailable')}
            </span>
          </div>
          <div className="grid grid-cols-3 gap-2">
            {[10, 20, 50].map((num) => (
              <button
                key={num}
                onClick={() => setQuestionCount(num)}
                className={`py-3 rounded-xl text-xs sm:text-sm font-mono font-bold border transition active:scale-95 ${
                  questionCount === num
                    ? 'bg-cyan-600 text-white border-cyan-500 shadow-md shadow-cyan-950/40'
                    : 'bg-slate-800 text-slate-300 border-slate-700 hover:border-slate-600'
                }`}
              >
                {num} Qs
              </button>
            ))}
          </div>
        </div>

        {/* Time Limit */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-5 space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-xs sm:text-sm font-bold text-white">
              {language === 'zh' ? '考試時限' : 'Time Limit'}
            </span>
            <span className="text-[11px] font-mono text-slate-400">
              ~1.5 {language === 'zh' ? '分鐘/題' : 'mins/Q'}
            </span>
          </div>
          <div className="grid grid-cols-3 gap-2">
            {[15, 30, 60].map((mins) => (
              <button
                key={mins}
                onClick={() => setDuration(mins)}
                className={`py-3 rounded-xl text-xs sm:text-sm font-mono font-bold border transition active:scale-95 ${
                  duration === mins
                    ? 'bg-cyan-600 text-white border-cyan-500 shadow-md shadow-cyan-950/40'
                    : 'bg-slate-800 text-slate-300 border-slate-700 hover:border-slate-600'
                }`}
              >
                {mins} Mins
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Guidelines Accordion / Card */}
      <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-4 sm:p-5 space-y-2.5">
        <h3 className="text-xs font-mono uppercase font-bold text-slate-300 flex items-center space-x-1.5">
          <ShieldAlert className="w-4 h-4 text-cyan-400" />
          <span>{language === 'zh' ? '評估標準與考場規則' : 'Assessment Standards & Instructions'}</span>
        </h3>
        <ul className="text-xs text-slate-400 space-y-1.5 list-disc list-inside leading-relaxed">
          <li>
            {language === 'zh'
              ? '及格分數基準線 (Pass Mark) 設為 60%。達到 80% 及以上為 Distinction 優秀。'
              : 'Pass benchmark is 60%. Distinction benchmark is 80%+.'}
          </li>
          <li>
            {language === 'zh'
              ? '手機端支援底部快捷直達答題卡、隨時標記複查、一鍵切換中/英題幹。'
              : 'Mobile friendly: bottom question palette, flag review, instant bilingual toggle.'}
          </li>
          <li>
            {language === 'zh'
              ? '交卷後將自動為您匯總錯題並存入個人本機錯題本，隨時發起錯題專項重測。'
              : 'Mistakes will be automatically saved to your local Mistake Notebook for targeted retesting.'}
          </li>
        </ul>
      </div>

      {/* Start Button (Mobile Thumb Friendly) */}
      <button
        onClick={() => onStartExam(questionCount, duration)}
        className="w-full py-4 rounded-xl bg-gradient-to-r from-cyan-600 to-cyan-500 hover:from-cyan-500 active:scale-[0.99] text-white font-bold text-sm sm:text-base shadow-lg shadow-cyan-950/50 flex items-center justify-center space-x-2 transition"
      >
        <Play className="w-5 h-5 fill-white" />
        <span>
          {language === 'zh'
            ? `立即進入模擬考試 (${questionCount} 題 · ${duration} 分鐘)`
            : `Start Simulated Exam (${questionCount} Qs · ${duration} Mins)`}
        </span>
      </button>
    </div>
  );
};
