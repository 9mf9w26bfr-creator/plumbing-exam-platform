'use client';

import React from 'react';
import { TextbookChapter } from '../types';
import { useLanguage } from '../context/LanguageContext';
import { BookOpen, Layers, ArrowRight, CheckCircle2 } from 'lucide-react';

interface ChapterListProps {
  chapters: TextbookChapter[];
  onSelectChapter: (chapterId: number, subTopicId?: string) => void;
  loading: boolean;
}

export const ChapterList: React.FC<ChapterListProps> = ({
  chapters,
  onSelectChapter,
  loading,
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

  const totalQuestions = chapters.reduce((acc, c) => acc + (c.question_count || 0), 0);

  return (
    <div className="space-y-4 sm:space-y-6 pb-20 md:pb-6">
      {/* Track A Header (Mobile-Optimized) */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-6 shadow-sm">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <div className="flex items-center space-x-1.5 text-cyan-400 text-[10px] sm:text-xs font-mono font-semibold uppercase tracking-wider mb-1">
              <Layers className="w-3.5 h-3.5" />
              <span>Track A: Knowledge Architecture (教材章節體系)</span>
            </div>
            <h1 className="text-lg sm:text-2xl font-bold text-white tracking-tight">
              {language === 'zh'
                ? '按 11 本教科書章節進行知識點專項練習'
                : 'Practice by 11 Textbook Chapters'}
            </h1>
            <p className="text-xs sm:text-sm text-slate-400 mt-1">
              {language === 'zh'
                ? '來源於 City & Guilds 權威教材目錄結構。每章精選擴充 50+ 道場景真題。'
                : 'Based on The City & Guilds Textbook Book 1. 50+ scenario questions per chapter.'}
            </p>
          </div>

          <div className="flex items-center space-x-2 bg-slate-800/80 border border-slate-700/60 rounded-lg px-3 py-1.5 self-start sm:self-auto shrink-0">
            <span className="text-[11px] text-slate-400">
              {language === 'zh' ? '題庫總量:' : 'Total Questions:'}
            </span>
            <span className="text-xs sm:text-sm font-bold font-mono text-cyan-400">
              {totalQuestions} {language === 'zh' ? '道題' : 'Qs'}
            </span>
          </div>
        </div>
      </div>

      {/* Chapters Grid (1 col on mobile, 2 on tablet, 3 on desktop) */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 sm:gap-4">
        {chapters.map((chapter) => (
          <div
            key={chapter.id}
            className="bg-slate-900/90 border border-slate-800 hover:border-slate-700 rounded-xl p-4 sm:p-5 flex flex-col justify-between transition-all duration-200 hover:shadow-lg hover:shadow-cyan-950/20 group"
          >
            <div>
              <div className="flex items-center justify-between mb-2 sm:mb-3">
                <span className="text-[11px] font-mono font-semibold px-2 py-0.5 rounded-md bg-cyan-950 text-cyan-300 border border-cyan-800/60">
                  Chapter {chapter.id}
                </span>
                <span className="text-[11px] font-medium text-slate-400">
                  <span className="text-cyan-400 font-bold mr-1">
                    {chapter.question_count || 0}
                  </span>
                  {t('questionsAvailable')}
                </span>
              </div>

              <h2 className="text-sm sm:text-base font-bold text-white group-hover:text-cyan-300 transition-colors line-clamp-2">
                {chapter.title}
              </h2>

              {/* Sub-topics list (Thumb-friendly touch chips) */}
              {chapter.sub_topics && chapter.sub_topics.length > 0 && (
                <div className="mt-3 space-y-1.5">
                  <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider">
                    {language === 'zh' ? '點擊小節直達練習 (Sub-topics):' : 'Tap Sub-topic:'}
                  </div>
                  <div className="flex flex-wrap gap-1.5 pt-0.5">
                    {chapter.sub_topics.map((sub) => (
                      <button
                        key={sub.id}
                        onClick={() => onSelectChapter(chapter.id, sub.id)}
                        className="text-[11px] text-slate-300 hover:text-cyan-300 active:bg-cyan-950 bg-slate-800 active:scale-95 px-2.5 py-1 rounded-md border border-slate-700/80 hover:border-cyan-700/60 transition flex items-center text-left"
                        title={language === 'zh' ? sub.title_zh : sub.title_en}
                      >
                        <span className="text-cyan-400 font-mono font-semibold mr-1">{sub.id}</span>
                        <span className="truncate max-w-[150px] xs:max-w-[180px]">
                          {language === 'zh' ? sub.title_zh : sub.title_en}
                        </span>
                      </button>
                    ))}
                  </div>
                </div>
              )}
            </div>

            {/* Action Footer (Full width tap area) */}
            <div className="mt-4 pt-3 border-t border-slate-800/80">
              <button
                onClick={() => onSelectChapter(chapter.id)}
                className="w-full flex items-center justify-center space-x-2 py-2.5 px-3 bg-slate-800 hover:bg-cyan-600 active:bg-cyan-650 active:scale-[0.99] text-slate-200 hover:text-white rounded-lg text-xs font-bold transition border border-slate-700 hover:border-cyan-500 shadow-sm"
              >
                <BookOpen className="w-3.5 h-3.5" />
                <span>
                  {language === 'zh'
                    ? `開始整章練習 (Ch ${chapter.id} · ${chapter.question_count || 0}題)`
                    : `Practice Chapter ${chapter.id} (${chapter.question_count || 0} Qs)`}
                </span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
