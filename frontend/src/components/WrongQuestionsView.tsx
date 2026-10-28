'use client';

import React, { useState, useEffect } from 'react';
import { WrongQuestionRecord } from '../types';
import { storage } from '../services/storage';
import { useLanguage } from '../context/LanguageContext';
import {
  AlertTriangle,
  Trash2,
  CheckCircle2,
  XCircle,
  RotateCcw,
  FileText,
  Filter
} from 'lucide-react';

interface WrongQuestionsViewProps {
  onPracticeWrong: (records: WrongQuestionRecord[]) => void;
  onRefreshCount: () => void;
}

export const WrongQuestionsView: React.FC<WrongQuestionsViewProps> = ({
  onPracticeWrong,
  onRefreshCount,
}) => {
  const { language, t } = useLanguage();
  const [records, setRecords] = useState<WrongQuestionRecord[]>([]);
  const [selectedUnit, setSelectedUnit] = useState<string>('all');

  const loadData = () => {
    const data = storage.getWrongQuestions();
    setRecords(data);
    onRefreshCount();
  };

  useEffect(() => {
    loadData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleRemove = (id: string) => {
    storage.removeWrongQuestion(id);
    loadData();
  };

  const handleClearAll = () => {
    if (confirm(language === 'zh' ? '確認清空所有錯題記錄？' : 'Clear all wrong questions?')) {
      storage.clearWrongQuestions();
      loadData();
    }
  };

  const filteredRecords = records.filter((r) => {
    if (selectedUnit === 'all') return true;
    return r.question.units?.includes(selectedUnit);
  });

  const allUnits = Array.from(
    new Set(records.flatMap((r) => r.question.units || []))
  );

  return (
    <div className="space-y-4 sm:space-y-6 max-w-4xl mx-auto pb-20 md:pb-6">
      {/* Header */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-6 shadow-sm flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <div className="flex items-center space-x-1.5 text-rose-400 text-[10px] sm:text-xs font-mono font-semibold uppercase tracking-wider mb-1">
            <AlertTriangle className="w-3.5 h-3.5" />
            <span>Mistake Diagnostics (個人錯題本)</span>
          </div>
          <h1 className="text-lg sm:text-2xl font-bold text-white tracking-tight">
            {t('wrongTitle')}
          </h1>
          <p className="text-xs text-slate-400 mt-0.5">
            {language === 'zh'
              ? '自動記錄答錯的題目，支持手機端快速翻閱與錯題專項重測。'
              : 'Automatically persists questions answered incorrectly.'}
          </p>
        </div>

        {records.length > 0 && (
          <div className="flex items-center space-x-2 self-stretch sm:self-auto">
            <button
              onClick={() => onPracticeWrong(filteredRecords)}
              disabled={filteredRecords.length === 0}
              className="flex-1 sm:flex-initial flex items-center justify-center space-x-1.5 py-2.5 px-3.5 rounded-lg bg-rose-600 hover:bg-rose-500 active:scale-95 text-white text-xs font-bold shadow-sm transition disabled:opacity-50"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              <span>{t('redoWrongQuestions')} ({filteredRecords.length})</span>
            </button>
            <button
              onClick={handleClearAll}
              className="p-2.5 rounded-lg bg-slate-800 hover:bg-slate-700 active:scale-95 text-slate-400 hover:text-rose-400 border border-slate-700 transition"
              title={t('clearAllWrong')}
            >
              <Trash2 className="w-4 h-4" />
            </button>
          </div>
        )}
      </div>

      {/* Filter Bar (Horizontal touch scroll on mobile) */}
      {records.length > 0 && allUnits.length > 0 && (
        <div className="flex items-center space-x-1.5 overflow-x-auto pb-1 text-xs scrollbar-none">
          <Filter className="w-3.5 h-3.5 text-slate-500 shrink-0" />
          <button
            onClick={() => setSelectedUnit('all')}
            className={`px-3 py-1.5 rounded-md font-medium transition shrink-0 text-xs active:scale-95 ${
              selectedUnit === 'all'
                ? 'bg-cyan-600 text-white'
                : 'bg-slate-800 text-slate-400 hover:bg-slate-700'
            }`}
          >
            {t('all')} ({records.length})
          </button>
          {allUnits.map((u) => {
            const count = records.filter((r) => r.question.units?.includes(u)).length;
            return (
              <button
                key={u}
                onClick={() => setSelectedUnit(u)}
                className={`px-2.5 py-1.5 rounded-md font-mono font-medium transition shrink-0 text-xs active:scale-95 ${
                  selectedUnit === u
                    ? 'bg-cyan-600 text-white'
                    : 'bg-slate-800 text-slate-400 hover:bg-slate-700'
                }`}
              >
                {u} ({count})
              </button>
            );
          })}
        </div>
      )}

      {/* Records List or Empty State */}
      {records.length === 0 ? (
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-8 sm:p-12 text-center space-y-3">
          <div className="w-12 h-12 rounded-full bg-emerald-950/80 border border-emerald-800/80 flex items-center justify-center mx-auto text-emerald-400">
            <CheckCircle2 className="w-6 h-6" />
          </div>
          <h2 className="text-base sm:text-lg font-bold text-white">{t('wrongEmpty')}</h2>
          <p className="text-xs text-slate-400 max-w-sm mx-auto">
            {language === 'zh'
              ? '目前沒有答錯的記錄，前往教材章節或考試單元開始練習吧！'
              : 'You have no recorded mistakes. Practice chapters or units!'}
          </p>
        </div>
      ) : (
        <div className="space-y-3 sm:space-y-4">
          {filteredRecords.map((item, idx) => {
            const q = item.question;
            const content = language === 'zh' ? q.content_zh || q.content_en : q.content_en || q.content_zh;
            const explanation = language === 'zh' ? q.explanation_zh || q.explanation_en : q.explanation_en || q.explanation_zh;
            const options = language === 'zh' ? q.options_zh || q.options_en : q.options_en || q.options_zh;

            return (
              <div
                key={q.id}
                className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-5 shadow-sm space-y-3"
              >
                <div className="flex items-center justify-between gap-2 border-b border-slate-800/80 pb-2.5">
                  <div className="flex flex-wrap items-center gap-1.5">
                    <span className="font-mono text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-400">
                      #{idx + 1}
                    </span>
                    {q.units?.map((u) => (
                      <span
                        key={u}
                        className="font-mono text-[10px] px-1.5 py-0.5 rounded bg-cyan-950 text-cyan-300 border border-cyan-800/60"
                      >
                        {u}
                      </span>
                    ))}
                    {q.chapters?.map((ch) => (
                      <span
                        key={ch.chapter_id}
                        className="font-mono text-[10px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700"
                      >
                        Ch {ch.chapter_id}
                      </span>
                    ))}
                  </div>

                  <button
                    onClick={() => handleRemove(q.id)}
                    className="flex items-center space-x-1 text-[11px] text-slate-400 hover:text-emerald-400 active:scale-95 transition"
                  >
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                    <span>{t('removeMistake')}</span>
                  </button>
                </div>

                {/* Question stem */}
                <div className="text-xs sm:text-sm font-medium text-slate-200 leading-relaxed">
                  {content}
                </div>

                {/* Answer comparison */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                  <div className="p-2.5 rounded-lg bg-rose-950/40 border border-rose-900/60 flex items-start space-x-2">
                    <XCircle className="w-4 h-4 text-rose-400 shrink-0 mt-0.5" />
                    <div>
                      <div className="text-rose-300 font-semibold text-[11px] mb-0.5">
                        {t('yourAnswer')}: {item.selected_answer}
                      </div>
                      <div className="text-slate-400 text-xs">
                        {options?.[item.selected_answer] || '未作答 (Unanswered)'}
                      </div>
                    </div>
                  </div>

                  <div className="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-900/60 flex items-start space-x-2">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                    <div>
                      <div className="text-emerald-300 font-semibold text-[11px] mb-0.5">
                        {t('correctAnswer')}: {q.correct_answer}
                      </div>
                      <div className="text-slate-400 text-xs">
                        {options?.[q.correct_answer]}
                      </div>
                    </div>
                  </div>
                </div>

                {/* Explanation */}
                <div className="p-3 rounded-lg bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5">
                  <div className="leading-relaxed">
                    <span className="font-semibold text-cyan-400 mr-1">
                      {t('explanation')}:
                    </span>
                    {explanation}
                  </div>
                  {q.source_reference && (
                    <div className="flex items-center space-x-1.5 text-cyan-400 font-mono text-[10px] pt-1 border-t border-slate-900">
                      <FileText className="w-3.5 h-3.5 text-cyan-300 shrink-0" />
                      <span>{q.source_reference}</span>
                    </div>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
