'use client';

import React from 'react';
import { TextbookChapter } from '../types';
import { useLanguage } from '../context/LanguageContext';
import { BookOpen, Layers, ArrowRight } from 'lucide-react';

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
        <p className="text-sm text-slate-400">{t('loading')}</p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Track A Header */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 sm:p-6 shadow-sm">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex items-center space-x-2 text-cyan-400 text-xs font-mono font-semibold uppercase tracking-wider mb-1">
              <Layers className="w-4 h-4" />
              <span>Track A: Knowledge Architecture (教材章節體系)</span>
            </div>
            <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              {language === 'zh'
                ? '按 11 本教科書章節進行知識點專項練習'
                : 'Practice by 11 Textbook Chapters'}
            </h1>
            <p className="text-sm text-slate-400 mt-1">
              {language === 'zh'
                ? '來源於 City & Guilds 權威教材目錄結構。支持整章隨機抽題或深入特定子章節。'
                : 'Based on The City & Guilds Textbook: Plumbing Book 1. Select a chapter or specific sub-topic.'}
            </p>
          </div>
          <div className="flex items-center bg-slate-800/80 border border-slate-700/60 rounded-lg px-4 py-2 self-start md:self-auto">
            <span className="text-xs text-slate-400 mr-2">
              {language === 'zh' ? '教材總章數:' : 'Total Chapters:'}
            </span>
            <span className="text-sm font-bold font-mono text-cyan-400">11 Chapters</span>
          </div>
        </div>
      </div>

      {/* Chapters Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {chapters.map((chapter) => (
          <div
            key={chapter.id}
            className="bg-slate-900/90 border border-slate-800 hover:border-slate-700 rounded-xl p-5 flex flex-col justify-between transition-all duration-200 hover:shadow-lg hover:shadow-cyan-950/20 group"
          >
            <div>
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-mono font-semibold px-2.5 py-1 rounded-md bg-cyan-950 text-cyan-300 border border-cyan-800/60">
                  Chapter {chapter.id}
                </span>
                <span className="text-xs font-medium text-slate-400">
                  <span className="text-cyan-400 font-bold mr-1">
                    {chapter.question_count || 0}
                  </span>
                  {t('questionsAvailable')}
                </span>
              </div>

              <h2 className="text-base font-bold text-white group-hover:text-cyan-300 transition-colors line-clamp-2">
                {chapter.title}
              </h2>

              {/* Sub-topics list */}
              {chapter.sub_topics && chapter.sub_topics.length > 0 && (
                <div className="mt-4 space-y-1.5">
                  <div className="text-xs font-mono text-slate-400 uppercase tracking-wider">
                    {language === 'zh' ? '核心小節 (Sub-topics):' : 'Key Sub-topics:'}
                  </div>
                  <div className="flex flex-wrap gap-1.5 pt-1">
                    {chapter.sub_topics.map((sub) => (
                      <button
                        key={sub.id}
                        onClick={() => onSelectChapter(chapter.id, sub.id)}
                        className="text-[11px] text-slate-300 hover:text-cyan-300 bg-slate-800 hover:bg-slate-750 px-2 py-1 rounded border border-slate-700/60 hover:border-cyan-700/60 transition flex items-center text-left"
                        title={language === 'zh' ? sub.title_zh : sub.title_en}
                      >
                        <span className="text-cyan-400 font-mono mr-1">{sub.id}</span>
                        <span className="truncate max-w-[170px]">
                          {language === 'zh' ? sub.title_zh : sub.title_en}
                        </span>
                      </button>
                    ))}
                  </div>
                </div>
              )}
            </div>

            {/* Action Footer */}
            <div className="mt-5 pt-4 border-t border-slate-800/80 flex items-center justify-between">
              <button
                onClick={() => onSelectChapter(chapter.id)}
                className="w-full flex items-center justify-center space-x-2 py-2 px-3 bg-slate-800 hover:bg-cyan-600 text-slate-200 hover:text-white rounded-lg text-xs font-semibold transition border border-slate-700 hover:border-cyan-500"
              >
                <BookOpen className="w-3.5 h-3.5" />
                <span>{language === 'zh' ? `開始整章練習 (Ch ${chapter.id})` : `Practice Chapter ${chapter.id}`}</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
