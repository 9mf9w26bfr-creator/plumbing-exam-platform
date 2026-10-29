'use client';

import React, { useState } from 'react';
import { ExamUnit, QuizSessionState } from '../types';
import { useLanguage } from '../context/LanguageContext';
import {
  Timer,
  ShieldAlert,
  Play,
  GraduationCap,
  Layers,
  Cpu,
  ShieldCheck,
  Briefcase,
  Leaf,
  RotateCcw,
  CheckCircle2,
} from 'lucide-react';

interface MockExamConfigProps {
  units: ExamUnit[];
  totalAvailable: number;
  onStartExam: (count: number, durationMinutes: number, unitId?: string) => void;
  activeSessions?: Record<string, QuizSessionState>;
}

export const MockExamConfig: React.FC<MockExamConfigProps> = ({
  units,
  totalAvailable,
  onStartExam,
  activeSessions,
}) => {
  const { language, t } = useLanguage();

  // Mode: 'unit' (Unit-by-Unit) vs 'all' (Comprehensive All-Units)
  const [examScope, setExamScope] = useState<'unit' | 'all'>('unit');
  const [selectedUnitId, setSelectedUnitId] = useState<string>(units[0]?.id || 'Unit_201');
  const [selectedCategory, setSelectedCategory] = useState<string>('all');

  // Question count and duration
  const [questionCount, setQuestionCount] = useState<number>(30);
  const [duration, setDuration] = useState<number>(45);

  const selectedUnit = units.find((u) => u.id === selectedUnitId) || units[0];

  const categories = [
    { id: 'all', label_zh: '全部單元 (10)', label_en: 'All Units (10)' },
    { id: 'Core', label_zh: 'Core 核心基礎', label_en: 'Core Principles' },
    { id: 'Technical', label_zh: 'Technical 專業水暖', label_en: 'Technical Systems' },
    { id: 'Professional', label_zh: 'Professional 規劃溝通', label_en: 'Planning' },
    { id: 'Environmental Revision', label_zh: 'Env 節能環保', label_en: 'Environmental' },
  ];

  const filteredUnits = units.filter((u) => {
    if (selectedCategory === 'all') return true;
    return u.category.toLowerCase() === selectedCategory.toLowerCase();
  });

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

  const handleSelectUnit = (unitId: string) => {
    setSelectedUnitId(unitId);
    const u = units.find((item) => item.id === unitId);
    const maxQ = u?.question_count || 50;
    // Auto-adjust default question count according to unit size
    if (questionCount > maxQ) {
      setQuestionCount(Math.min(30, maxQ));
    }
  };

  const handleLaunch = () => {
    if (examScope === 'unit') {
      onStartExam(questionCount, duration, selectedUnitId);
    } else {
      onStartExam(questionCount, duration, 'all');
    }
  };

  const activeUnitSession = activeSessions ? activeSessions[`mock_${selectedUnitId}`] : undefined;
  const activeAllSession = activeSessions ? activeSessions['mock_all'] : undefined;

  return (
    <div className="max-w-4xl mx-auto space-y-4 sm:space-y-6 pb-20 md:pb-6">
      {/* Header */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-6 shadow-sm">
        <div className="flex items-center space-x-1.5 text-cyan-400 text-[10px] sm:text-xs font-mono font-semibold uppercase tracking-wider mb-1.5">
          <Timer className="w-3.5 h-3.5" />
          <span>City & Guilds 6035 / 8202 Assessment Center</span>
        </div>
        <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
          {language === 'zh'
            ? '全真模擬考試環境設置 (Mock Exam Center)'
            : 'Simulated Timed Mock Examination Center'}
        </h1>
        <p className="text-xs sm:text-sm text-slate-400 mt-1">
          {language === 'zh'
            ? '嚴格遵循英國 City & Guilds 考試標準：支持按 10 大考綱單元（Units）分開獨立模考，或進行跨單元綜合大考。'
            : 'Strictly aligned with City & Guilds benchmarks: take unit-by-unit mock exams or full cross-unit exams.'}
        </p>
      </div>

      {/* Scope Selector Tabs: Unit-by-Unit vs Comprehensive */}
      <div className="bg-slate-900/90 border border-slate-800 p-1.5 rounded-xl grid grid-cols-2 gap-1.5">
        <button
          onClick={() => {
            setExamScope('unit');
            setQuestionCount(30);
            setDuration(45);
          }}
          className={`py-2.5 px-3 rounded-lg text-xs sm:text-sm font-bold flex items-center justify-center space-x-2 transition ${
            examScope === 'unit'
              ? 'bg-cyan-600 text-white shadow-md shadow-cyan-950/40'
              : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
          }`}
        >
          <GraduationCap className="w-4 h-4" />
          <span>{language === 'zh' ? '按 Units 單元專項全真模考' : 'Unit-by-Unit Mock Exams'}</span>
        </button>

        <button
          onClick={() => {
            setExamScope('all');
            setQuestionCount(50);
            setDuration(75);
          }}
          className={`py-2.5 px-3 rounded-lg text-xs sm:text-sm font-bold flex items-center justify-center space-x-2 transition ${
            examScope === 'all'
              ? 'bg-cyan-600 text-white shadow-md shadow-cyan-950/40'
              : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
          }`}
        >
          <Layers className="w-4 h-4" />
          <span>{language === 'zh' ? '全科綜合全真大考 (All-Units)' : 'Comprehensive Full Mock Exam'}</span>
        </button>
      </div>

      {/* Mode A: Unit-by-Unit Selection View */}
      {examScope === 'unit' && (
        <div className="space-y-4">
          {/* Category Filter Pills */}
          <div className="flex items-center space-x-1.5 overflow-x-auto pb-1 text-xs">
            {categories.map((cat) => (
              <button
                key={cat.id}
                onClick={() => setSelectedCategory(cat.id)}
                className={`px-3 py-1.5 rounded-lg font-medium whitespace-nowrap transition active:scale-95 border ${
                  selectedCategory === cat.id
                    ? 'bg-cyan-950 text-cyan-300 border-cyan-700/80 font-bold'
                    : 'bg-slate-900/80 text-slate-400 border-slate-800 hover:text-slate-200 hover:bg-slate-800'
                }`}
              >
                {language === 'zh' ? cat.label_zh : cat.label_en}
              </button>
            ))}
          </div>

          {/* Unit Cards Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-2.5 sm:gap-3">
            {filteredUnits.map((unit) => {
              const isSelected = selectedUnitId === unit.id;
              const session = activeSessions ? activeSessions[`mock_${unit.id}`] : undefined;

              return (
                <div
                  key={unit.id}
                  onClick={() => handleSelectUnit(unit.id)}
                  className={`p-3.5 sm:p-4 rounded-xl border transition-all cursor-pointer relative select-none ${
                    isSelected
                      ? 'bg-gradient-to-br from-cyan-950/60 to-slate-900 border-cyan-500 shadow-md shadow-cyan-950/30 ring-1 ring-cyan-500/50'
                      : 'bg-slate-900/90 border-slate-800 hover:border-slate-700 hover:bg-slate-850'
                  }`}
                >
                  <div className="flex items-start justify-between gap-2">
                    <div className="flex items-center space-x-1.5">
                      <span className="font-mono font-bold text-xs px-2 py-0.5 rounded bg-slate-800 text-cyan-300 border border-slate-700">
                        {unit.id}
                      </span>
                      <span className={`text-[10px] font-mono px-2 py-0.5 rounded border flex items-center space-x-1 ${getCategoryBadgeClass(unit.category)}`}>
                        {getCategoryIcon(unit.category)}
                        <span>{unit.category}</span>
                      </span>
                    </div>

                    <div className="flex items-center space-x-1.5">
                      {session && (
                        <span className="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded bg-amber-950 text-amber-300 border border-amber-800 flex items-center space-x-1">
                          <span className="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse"></span>
                          <span>Q{session.currentIndex + 1}/{session.questions.length}</span>
                        </span>
                      )}
                      {isSelected && (
                        <CheckCircle2 className="w-4 h-4 text-cyan-400 shrink-0" />
                      )}
                    </div>
                  </div>

                  <h3 className={`text-xs sm:text-sm font-bold mt-2 leading-snug ${isSelected ? 'text-white' : 'text-slate-200'}`}>
                    {unit.title}
                  </h3>

                  <div className="mt-2.5 flex items-center justify-between text-[11px] text-slate-400 border-t border-slate-800/80 pt-2 font-mono">
                    <span>
                      {language === 'zh' ? '題庫可用：' : 'Question Pool: '}{' '}
                      <strong className="text-cyan-400">{unit.question_count || 0}</strong> {language === 'zh' ? '道真題' : 'Qs'}
                    </span>
                    <span className="text-slate-500">
                      {language === 'zh' ? '及格率基準 60%' : '60% Pass Benchmark'}
                    </span>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Selected Unit Active Parameters Panel */}
          {selectedUnit && (
            <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-5 space-y-4">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
                <div>
                  <span className="text-[10px] font-mono uppercase tracking-wider text-cyan-400 font-bold">
                    {language === 'zh' ? '已選模考單元' : 'Selected Unit for Examination'}
                  </span>
                  <h2 className="text-base sm:text-lg font-bold text-white">
                    {selectedUnit.id} - {selectedUnit.title}
                  </h2>
                </div>
                <div className="text-xs font-mono text-slate-400 bg-slate-800 px-2.5 py-1 rounded-md border border-slate-700 self-start sm:self-auto">
                  {language === 'zh' ? '單元題庫容納量' : 'Unit Capacity'}: <span className="text-cyan-400 font-bold">{selectedUnit.question_count || 0}</span> 題
                </div>
              </div>

              {/* Parameters Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
                {/* Question count */}
                <div className="space-y-2">
                  <div className="flex items-center justify-between text-xs">
                    <span className="font-bold text-slate-200">
                      {language === 'zh' ? '抽考題目數量' : 'Number of Questions'}
                    </span>
                    <span className="text-slate-400 font-mono">
                      {questionCount} {language === 'zh' ? '道題' : 'Qs'}
                    </span>
                  </div>
                  <div className="grid grid-cols-3 gap-2">
                    {[15, 30, Math.min(50, selectedUnit.question_count || 50)].map((count) => (
                      <button
                        key={count}
                        onClick={() => setQuestionCount(count)}
                        className={`py-2.5 rounded-lg text-xs font-mono font-bold border transition active:scale-95 ${
                          questionCount === count
                            ? 'bg-cyan-600 text-white border-cyan-500 shadow-md shadow-cyan-950/40'
                            : 'bg-slate-800 text-slate-300 border-slate-700 hover:border-slate-600'
                        }`}
                      >
                        {count} Qs
                      </button>
                    ))}
                  </div>
                </div>

                {/* Duration */}
                <div className="space-y-2">
                  <div className="flex items-center justify-between text-xs">
                    <span className="font-bold text-slate-200">
                      {language === 'zh' ? '考試倒計時限制' : 'Time Limit'}
                    </span>
                    <span className="text-slate-400 font-mono">
                      ~{(duration / questionCount).toFixed(1)} {language === 'zh' ? '分鐘/題' : 'mins/Q'}
                    </span>
                  </div>
                  <div className="grid grid-cols-3 gap-2">
                    {[20, 45, 60].map((mins) => (
                      <button
                        key={mins}
                        onClick={() => setDuration(mins)}
                        className={`py-2.5 rounded-lg text-xs font-mono font-bold border transition active:scale-95 ${
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
            </div>
          )}
        </div>
      )}

      {/* Mode B: Comprehensive All-Units Exam */}
      {examScope === 'all' && (
        <div className="space-y-4">
          <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-5 space-y-4">
            <div className="border-b border-slate-800 pb-3">
              <span className="text-[10px] font-mono uppercase tracking-wider text-cyan-400 font-bold">
                {language === 'zh' ? '全科跨單元大考模式' : 'Comprehensive Cross-Unit Mode'}
              </span>
              <h2 className="text-base sm:text-lg font-bold text-white mt-0.5">
                City & Guilds 6035 / 8202 {language === 'zh' ? '畢業全真大考' : 'Comprehensive Final Mock Exam'}
              </h2>
              <p className="text-xs text-slate-400 mt-1">
                {language === 'zh'
                  ? `從全部 10 大考綱單元（共 ${totalAvailable} 道題庫）中隨機按權重抽取，完整模擬英國官方大考。`
                  : `Draws weighted random questions across all 10 qualification units (${totalAvailable} total Qs).`}
              </p>
            </div>

            {/* Parameters Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
              {/* Question Count */}
              <div className="space-y-2">
                <div className="flex items-center justify-between text-xs">
                  <span className="font-bold text-slate-200">
                    {language === 'zh' ? '全科抽考題量' : 'Exam Questions'}
                  </span>
                  <span className="text-slate-400 font-mono">{questionCount} Qs</span>
                </div>
                <div className="grid grid-cols-3 gap-2">
                  {[20, 50, 100].map((count) => (
                    <button
                      key={count}
                      onClick={() => setQuestionCount(count)}
                      className={`py-2.5 rounded-lg text-xs font-mono font-bold border transition active:scale-95 ${
                        questionCount === count
                          ? 'bg-cyan-600 text-white border-cyan-500 shadow-md shadow-cyan-950/40'
                          : 'bg-slate-800 text-slate-300 border-slate-700 hover:border-slate-600'
                      }`}
                    >
                      {count} Qs
                    </button>
                  ))}
                </div>
              </div>

              {/* Duration */}
              <div className="space-y-2">
                <div className="flex items-center justify-between text-xs">
                  <span className="font-bold text-slate-200">
                    {language === 'zh' ? '全科考試時長' : 'Exam Duration'}
                  </span>
                  <span className="text-slate-400 font-mono">{duration} Mins</span>
                </div>
                <div className="grid grid-cols-3 gap-2">
                  {[30, 75, 120].map((mins) => (
                    <button
                      key={mins}
                      onClick={() => setDuration(mins)}
                      className={`py-2.5 rounded-lg text-xs font-mono font-bold border transition active:scale-95 ${
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
          </div>
        </div>
      )}

      {/* Guidelines Card */}
      <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-4 sm:p-5 space-y-2.5">
        <h3 className="text-xs font-mono uppercase font-bold text-slate-300 flex items-center space-x-1.5">
          <ShieldAlert className="w-4 h-4 text-cyan-400" />
          <span>{language === 'zh' ? '英國考評標準與答題須知' : 'Assessment Standards & Instructions'}</span>
        </h3>
        <ul className="text-xs text-slate-400 space-y-1.5 list-disc list-inside leading-relaxed">
          <li>
            {language === 'zh'
              ? '及格分數基準線 (Pass Mark) 設為 60%。達到 80% 及以上為 Distinction 優秀等第。'
              : 'Pass benchmark is 60%. Distinction benchmark is 80%+.'}
          </li>
          <li>
            {language === 'zh'
              ? '答題進度已開啟即時自動留存，若中途網路斷線或切換手機 APP，系統會保留剩餘時間與已答答案，隨時可原題繼續。'
              : 'Real-time session auto-save enabled. Safe against disconnections or app switching.'}
          </li>
          <li>
            {language === 'zh'
              ? '交卷後將自動產生成績診斷報告，答錯題目將自動納入個人本機錯題本，支援隨時反覆重練。'
              : 'Detailed diagnostic report upon submission. Mistakes automatically saved to your local notebook.'}
          </li>
        </ul>
      </div>

      {/* Start Button (Mobile-First Thumb Accessible) */}
      <button
        onClick={handleLaunch}
        className="w-full py-4 rounded-xl bg-gradient-to-r from-cyan-600 to-cyan-500 hover:from-cyan-500 active:scale-[0.99] text-white font-bold text-sm sm:text-base shadow-lg shadow-cyan-950/50 flex items-center justify-center space-x-2 transition min-h-[48px]"
      >
        <Play className="w-5 h-5 fill-white" />
        <span>
          {examScope === 'unit'
            ? (language === 'zh'
                ? `進入 ${selectedUnit?.id} 專項全真模考 (${questionCount} 題 · ${duration} 分鐘)`
                : `Start ${selectedUnit?.id} Mock Exam (${questionCount} Qs · ${duration} Mins)`)
            : (language === 'zh'
                ? `進入全科跨單元綜合大考 (${questionCount} 題 · ${duration} 分鐘)`
                : `Start Comprehensive Exam (${questionCount} Qs · ${duration} Mins)`)}
        </span>
      </button>
    </div>
  );
};
