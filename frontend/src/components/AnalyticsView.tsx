'use client';

import React, { useState, useEffect } from 'react';
import { TextbookChapter, ExamUnit } from '../types';
import { storage } from '../services/storage';
import { useLanguage } from '../context/LanguageContext';
import {
  BarChart3,
  TrendingUp,
  AlertTriangle,
  BookOpen,
  GraduationCap,
  Target
} from 'lucide-react';

interface AnalyticsViewProps {
  chapters: TextbookChapter[];
  units: ExamUnit[];
}

export const AnalyticsView: React.FC<AnalyticsViewProps> = ({
  chapters,
  units,
}) => {
  const { language, t } = useLanguage();
  const [stats, setStats] = useState(storage.getProgressStats());
  const [activeTab, setActiveTab] = useState<'chapters' | 'units'>('chapters');

  useEffect(() => {
    setStats(storage.getProgressStats());
  }, []);

  const overallAccuracy =
    stats.totalAttempted > 0
      ? Math.round((stats.correctCount / stats.totalAttempted) * 100)
      : 0;

  const getAccuracy = (correct: number, total: number) => {
    if (!total || total === 0) return 0;
    return Math.round((correct / total) * 100);
  };

  const getStatusBadge = (accuracy: number, total: number) => {
    if (total === 0) {
      return (
        <span className="text-[10px] sm:text-[11px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-400 border border-slate-700">
          {language === 'zh' ? '未開始' : 'Not Started'}
        </span>
      );
    }
    if (accuracy >= 80) {
      return (
        <span className="text-[10px] sm:text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800">
          {language === 'zh' ? '精通' : 'Mastered'}
        </span>
      );
    }
    if (accuracy >= 60) {
      return (
        <span className="text-[10px] sm:text-[11px] font-mono px-2 py-0.5 rounded bg-cyan-950 text-cyan-300 border border-cyan-800">
          {language === 'zh' ? '合格' : 'Pass'}
        </span>
      );
    }
    return (
      <span className="text-[10px] sm:text-[11px] font-mono px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-800">
        {language === 'zh' ? '需強化' : 'Revision'}
      </span>
    );
  };

  return (
    <div className="space-y-4 sm:space-y-6 max-w-5xl mx-auto pb-20 md:pb-6">
      {/* Header */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-6 shadow-sm">
        <div className="flex items-center space-x-1.5 text-cyan-400 text-[10px] sm:text-xs font-mono font-semibold uppercase tracking-wider mb-1.5">
          <BarChart3 className="w-3.5 h-3.5" />
          <span>Knowledge Diagnostics & Competency Radar</span>
        </div>
        <h1 className="text-lg sm:text-2xl font-bold text-white tracking-tight">
          {t('masterySummary')}
        </h1>
        <p className="text-xs text-slate-400 mt-0.5">
          {language === 'zh'
            ? '多維度分析 11 本教材章節與 10 大考綱單元的掌握度與正確率。'
            : 'Multi-dimensional diagnostic metrics across the 11 chapters and 10 qualification units.'}
        </p>
      </div>

      {/* Top Metrics Cards (Stacked on Mobile) */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5 sm:gap-4">
        <div className="bg-slate-900 border border-slate-800 p-4 rounded-xl shadow-sm space-y-1">
          <div className="flex items-center justify-between text-xs text-slate-400 font-medium">
            <span>{t('totalQuestionsAttempted')}</span>
            <Target className="w-4 h-4 text-cyan-400" />
          </div>
          <div className="text-2xl font-black font-mono text-white">
            {stats.totalAttempted}
          </div>
          <p className="text-[10px] text-slate-400">
            {language === 'zh' ? '累計作答題目次數' : 'Total attempted'}
          </p>
        </div>

        <div className="bg-slate-900 border border-slate-800 p-4 rounded-xl shadow-sm space-y-1">
          <div className="flex items-center justify-between text-xs text-slate-400 font-medium">
            <span>{t('overallAccuracy')}</span>
            <TrendingUp className="w-4 h-4 text-emerald-400" />
          </div>
          <div className="text-2xl font-black font-mono text-emerald-400">
            {overallAccuracy}%
          </div>
          <p className="text-[10px] text-slate-400">
            {language === 'zh' ? `答對 ${stats.correctCount} 題` : `${stats.correctCount} correct answers`}
          </p>
        </div>

        <div className="bg-slate-900 border border-slate-800 p-4 rounded-xl shadow-sm space-y-1">
          <div className="flex items-center justify-between text-xs text-slate-400 font-medium">
            <span>{language === 'zh' ? '目前錯題本題目' : 'Mistakes in Notebook'}</span>
            <AlertTriangle className="w-4 h-4 text-rose-400" />
          </div>
          <div className="text-2xl font-black font-mono text-rose-400">
            {storage.getWrongQuestions().length}
          </div>
          <p className="text-[10px] text-slate-400">
            {language === 'zh' ? '待攻克薄弱考點' : 'Pending revision'}
          </p>
        </div>
      </div>

      {/* Track Toggle */}
      <div className="flex border-b border-slate-800">
        <button
          onClick={() => setActiveTab('chapters')}
          className={`flex-1 sm:flex-initial flex items-center justify-center space-x-1.5 py-3 px-4 text-xs sm:text-sm font-semibold border-b-2 transition ${
            activeTab === 'chapters'
              ? 'border-cyan-500 text-cyan-400 bg-slate-900/50'
              : 'border-transparent text-slate-400 hover:text-slate-200'
          }`}
        >
          <BookOpen className="w-3.5 h-3.5" />
          <span>{t('chapterMastery')}</span>
        </button>
        <button
          onClick={() => setActiveTab('units')}
          className={`flex-1 sm:flex-initial flex items-center justify-center space-x-1.5 py-3 px-4 text-xs sm:text-sm font-semibold border-b-2 transition ${
            activeTab === 'units'
              ? 'border-cyan-500 text-cyan-400 bg-slate-900/50'
              : 'border-transparent text-slate-400 hover:text-slate-200'
          }`}
        >
          <GraduationCap className="w-3.5 h-3.5" />
          <span>{t('unitMastery')}</span>
        </button>
      </div>

      {/* Chapters Breakdown */}
      {activeTab === 'chapters' && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3 sm:gap-4">
          {chapters.map((ch) => {
            const data = stats.byChapter[ch.id] || { total: 0, correct: 0 };
            const acc = getAccuracy(data.correct, data.total);
            return (
              <div
                key={ch.id}
                className="bg-slate-900 border border-slate-800 rounded-xl p-4 space-y-2.5"
              >
                <div className="flex items-center justify-between">
                  <span className="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-slate-800 text-cyan-300 border border-slate-700">
                    Chapter {ch.id}
                  </span>
                  {getStatusBadge(acc, data.total)}
                </div>

                <div className="text-xs sm:text-sm font-bold text-white line-clamp-1">
                  {ch.title}
                </div>

                <div className="space-y-1">
                  <div className="flex justify-between text-[11px] font-mono text-slate-400">
                    <span>
                      {data.correct} / {data.total} {language === 'zh' ? '題正確' : 'correct'}
                    </span>
                    <span className="font-bold text-slate-200">{acc}%</span>
                  </div>
                  <div className="w-full h-2 rounded-full bg-slate-800 overflow-hidden">
                    <div
                      className={`h-full transition-all duration-500 ${
                        acc >= 80
                          ? 'bg-emerald-500'
                          : acc >= 60
                          ? 'bg-cyan-500'
                          : data.total === 0
                          ? 'bg-slate-700'
                          : 'bg-rose-500'
                      }`}
                      style={{ width: `${acc}%` }}
                    ></div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Units Breakdown */}
      {activeTab === 'units' && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3 sm:gap-4">
          {units.map((u) => {
            const data = stats.byUnit[u.id] || { total: 0, correct: 0 };
            const acc = getAccuracy(data.correct, data.total);
            return (
              <div
                key={u.id}
                className="bg-slate-900 border border-slate-800 rounded-xl p-4 space-y-2.5"
              >
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-1.5">
                    <span className="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-slate-800 text-cyan-300 border border-slate-700">
                      {u.id}
                    </span>
                    <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-800 text-slate-400 border border-slate-700">
                      {u.category}
                    </span>
                  </div>
                  {getStatusBadge(acc, data.total)}
                </div>

                <div className="text-xs sm:text-sm font-bold text-white line-clamp-1">
                  {u.title}
                </div>

                <div className="space-y-1">
                  <div className="flex justify-between text-[11px] font-mono text-slate-400">
                    <span>
                      {data.correct} / {data.total} {language === 'zh' ? '題正確' : 'correct'}
                    </span>
                    <span className="font-bold text-slate-200">{acc}%</span>
                  </div>
                  <div className="w-full h-2 rounded-full bg-slate-800 overflow-hidden">
                    <div
                      className={`h-full transition-all duration-500 ${
                        acc >= 80
                          ? 'bg-emerald-500'
                          : acc >= 60
                          ? 'bg-cyan-500'
                          : data.total === 0
                          ? 'bg-slate-700'
                          : 'bg-rose-500'
                      }`}
                      style={{ width: `${acc}%` }}
                    ></div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
