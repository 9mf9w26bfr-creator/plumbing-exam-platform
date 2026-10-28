'use client';

import React from 'react';
import { ExamUnit, QuizSessionState } from '../types';
import { useLanguage } from '../context/LanguageContext';
import { GraduationCap, ArrowRight, ShieldCheck, Cpu, Leaf, Briefcase, RotateCcw } from 'lucide-react';

interface UnitListProps {
  units: ExamUnit[];
  onSelectUnit: (unitId: string) => void;
  loading: boolean;
  activeSessions?: Record<string, QuizSessionState>;
}

export const UnitList: React.FC<UnitListProps> = ({
  units,
  onSelectUnit,
  loading,
  activeSessions,
}) => {
  const { language, t } = useLanguage();

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[300px] space-y-3">
        <div className="w-8 h-8 border-4 border-cyan-500 border-t-transparent rounded-full animate-spin"></div>
        <p className="text-xs sm:text-sm text-slate-400">{t('loading')}</p>
      </div>
    );
  }

  const getCategoryIcon = (cat: string) => {
    switch (cat.toLowerCase()) {
      case 'core':
        return <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />;
      case 'technical':
        return <Cpu className="w-3.5 h-3.5 text-cyan-400" />;
      case 'professional':
        return <Briefcase className="w-3.5 h-3.5 text-amber-400" />;
      case 'environmental revision':
        return <Leaf className="w-3.5 h-3.5 text-lime-400" />;
      default:
        return <GraduationCap className="w-3.5 h-3.5 text-cyan-400" />;
    }
  };

  const getCategoryBadgeClass = (cat: string) => {
    switch (cat.toLowerCase()) {
      case 'core':
        return 'bg-emerald-950/80 text-emerald-300 border-emerald-800';
      case 'technical':
        return 'bg-cyan-950/80 text-cyan-300 border-cyan-800';
      case 'professional':
        return 'bg-amber-950/80 text-amber-300 border-amber-800';
      case 'environmental revision':
        return 'bg-lime-950/80 text-lime-300 border-lime-800';
      default:
        return 'bg-slate-800 text-slate-300 border-slate-700';
    }
  };

  return (
    <div className="space-y-4 sm:space-y-6 pb-20 md:pb-6">
      {/* Track B Header (Mobile-Optimized) */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-6 shadow-sm">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <div className="flex items-center space-x-1.5 text-cyan-400 text-[10px] sm:text-xs font-mono font-semibold uppercase tracking-wider mb-1">
              <GraduationCap className="w-3.5 h-3.5" />
              <span>Track B: Qualification Unit Mapping (考綱認證單元體系)</span>
            </div>
            <h1 className="text-lg sm:text-2xl font-bold text-white tracking-tight">
              {language === 'zh'
                ? '按 City & Guilds 6035/8202 官方考證代碼刷題'
                : 'Practice by Qualification Units (6035/8202)'}
            </h1>
            <p className="text-xs sm:text-sm text-slate-400 mt-1">
              {language === 'zh'
                ? '聚焦資格考核單元。涵蓋健康安全、冷熱水、電氣原理等考綱單元及環保複習分類。'
                : 'Aligned with official C&G assessment criteria. Core & technical modules.'}
            </p>
          </div>

          <div className="flex items-center space-x-2 bg-slate-800/80 border border-slate-700/60 rounded-lg px-3 py-1.5 self-start sm:self-auto shrink-0">
            <span className="text-[11px] text-slate-400">
              {language === 'zh' ? '考綱單元數:' : 'Total Units:'}
            </span>
            <span className="text-xs sm:text-sm font-bold font-mono text-cyan-400">10 Units</span>
          </div>
        </div>
      </div>

      {/* Units Grid (1 col on mobile, 2 on tablet, 3 on desktop) */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 sm:gap-4">
        {units.map((unit) => {
          const session = activeSessions ? activeSessions['unit_' + unit.id] : undefined;

          return (
            <div
              key={unit.id}
              className={`bg-slate-900/90 border rounded-xl p-4 sm:p-5 flex flex-col justify-between transition-all duration-200 hover:shadow-lg group ${
                session
                  ? 'border-amber-500/50 hover:border-amber-400/80 shadow-amber-950/20'
                  : 'border-slate-800 hover:border-slate-700 hover:shadow-cyan-950/20'
              }`}
            >
              <div>
                <div className="flex items-center justify-between mb-2 sm:mb-3">
                  <div className="flex items-center space-x-1.5">
                    <span className="text-[11px] font-mono font-semibold px-2 py-0.5 rounded-md bg-slate-800 text-cyan-300 border border-slate-700">
                      {unit.id}
                    </span>
                    {session && (
                      <span className="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded bg-amber-950 text-amber-300 border border-amber-800 flex items-center space-x-1">
                        <span className="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse"></span>
                        <span>Q{session.currentIndex + 1}/{session.questions.length}</span>
                      </span>
                    )}
                  </div>
                  <span className={`text-[10px] font-mono px-2 py-0.5 rounded border flex items-center space-x-1 ${getCategoryBadgeClass(unit.category)}`}>
                    {getCategoryIcon(unit.category)}
                    <span>{unit.category}</span>
                  </span>
                </div>

                <h2 className="text-sm sm:text-base font-bold text-white group-hover:text-cyan-300 transition-colors">
                  {unit.title}
                </h2>

                <p className="text-xs text-slate-400 mt-1.5 line-clamp-2">
                  {unit.id === 'Unit_ENV'
                    ? (language === 'zh' ? '經大綱核實之節能環保複習分類，非獨立 L2 考單元' : 'Syllabus-verified energy conservation & eco-revision category')
                    : (language === 'zh' ? 'C&G 6035 / 8202 核心評估單元模塊' : 'Standard C&G 6035/8202 core assessment module')}
                </p>
              </div>

              <div className="mt-4 pt-3 border-t border-slate-800/80 flex items-center justify-between gap-2">
                <span className="text-[11px] text-slate-400">
                  <span className="text-cyan-400 font-bold mr-1">
                    {unit.question_count || 0}
                  </span>
                  {t('questionsAvailable')}
                </span>
                <button
                  onClick={() => onSelectUnit(unit.id)}
                  className={`flex items-center space-x-1.5 py-2 px-3.5 rounded-lg text-xs font-bold transition shadow-sm active:scale-95 border ${
                    session
                      ? 'bg-gradient-to-r from-amber-600 to-amber-700 hover:from-amber-500 hover:to-amber-600 text-slate-950 border-amber-500'
                      : 'bg-cyan-600 hover:bg-cyan-500 text-white border-cyan-500'
                  }`}
                >
                  {session ? (
                    <>
                      <RotateCcw className="w-3.5 h-3.5" />
                      <span>{language === 'zh' ? `從第 ${session.currentIndex + 1} 題繼續` : `Resume (Q${session.currentIndex + 1})`}</span>
                    </>
                  ) : (
                    <>
                      <span>{t('startPractice')}</span>
                      <ArrowRight className="w-3.5 h-3.5" />
                    </>
                  )}
                </button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
