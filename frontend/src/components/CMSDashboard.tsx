'use client';

import React, { useState, useEffect } from 'react';
import {
  Question,
  QuestionStatus,
  CMSStats,
  TextbookChapter,
  ExamUnit,
  QuestionCreatePayload,
} from '../types';
import { api } from '../services/api';
import { useLanguage } from '../context/LanguageContext';
import {
  ShieldCheck,
  CheckCircle2,
  AlertCircle,
  Plus,
  Search,
  FileText,
  Trash2,
  ArrowRight,
  RotateCcw,
  X
} from 'lucide-react';

interface CMSDashboardProps {
  chapters: TextbookChapter[];
  units: ExamUnit[];
  onRefreshData: () => void;
}

export const CMSDashboard: React.FC<CMSDashboardProps> = ({
  chapters,
  units,
  onRefreshData,
}) => {
  const { language, t } = useLanguage();

  const [stats, setStats] = useState<CMSStats | null>(null);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [loading, setLoading] = useState(true);
  const [statusFilter, setStatusFilter] = useState<string>('all');
  const [searchKeyword, setSearchKeyword] = useState<string>('');
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

  // Form state
  const [formData, setFormData] = useState<QuestionCreatePayload>({
    content_en: '',
    content_zh: '',
    options_en: { A: '', B: '', C: '', D: '' },
    options_zh: { A: '', B: '', C: '', D: '' },
    correct_answer: 'A',
    explanation_en: '',
    explanation_zh: '',
    status: 'Draft',
    source_reference: '',
    chapter_ids: [{ chapter_id: 1, sub_topic_id: '1.1' }],
    unit_ids: ['Unit_201'],
  });

  const loadCMSData = async () => {
    try {
      setLoading(true);
      setErrorMsg(null);
      const [sData, qData] = await Promise.all([
        api.getCMSStats(),
        api.getCMSQuestions({
          status: statusFilter === 'all' ? undefined : (statusFilter as QuestionStatus),
          keyword: searchKeyword.trim() || undefined,
        }),
      ]);
      setStats(sData);
      setQuestions(qData);
    } catch (e: unknown) {
      setErrorMsg((e as Error).message || 'Failed to load CMS data');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadCMSData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [statusFilter]);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    loadCMSData();
  };

  const handleStatusTransition = async (id: string, targetStatus: QuestionStatus) => {
    try {
      setErrorMsg(null);
      await api.updateQuestionStatus(id, targetStatus);
      await loadCMSData();
      onRefreshData();
    } catch (err: unknown) {
      setErrorMsg((err as Error).message || 'Status transition failed');
    }
  };

  const handleDelete = async (id: string) => {
    if (confirm(language === 'zh' ? '確認刪除此題目記錄？' : 'Delete this question?')) {
      try {
        setErrorMsg(null);
        await api.deleteQuestion(id);
        await loadCMSData();
        onRefreshData();
      } catch (err: unknown) {
        setErrorMsg((err as Error).message || 'Delete failed');
      }
    }
  };

  const handleCreateQuestion = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      setErrorMsg(null);
      await api.createQuestion(formData);
      setShowCreateModal(false);
      setFormData({
        content_en: '',
        content_zh: '',
        options_en: { A: '', B: '', C: '', D: '' },
        options_zh: { A: '', B: '', C: '', D: '' },
        correct_answer: 'A',
        explanation_en: '',
        explanation_zh: '',
        status: 'Draft',
        source_reference: '',
        chapter_ids: [{ chapter_id: 1, sub_topic_id: '1.1' }],
        unit_ids: ['Unit_201'],
      });
      await loadCMSData();
      onRefreshData();
    } catch (err: unknown) {
      setErrorMsg((err as Error).message || 'Failed to create question');
    }
  };

  const getStatusBadge = (status: QuestionStatus) => {
    switch (status) {
      case 'Draft':
        return (
          <span className="px-2 py-0.5 rounded-full text-[10px] sm:text-xs font-mono font-bold bg-slate-800 text-slate-300 border border-slate-700">
            Draft
          </span>
        );
      case 'AI_Reviewed':
        return (
          <span className="px-2 py-0.5 rounded-full text-[10px] sm:text-xs font-mono font-bold bg-indigo-950 text-indigo-300 border border-indigo-800">
            AI Reviewed
          </span>
        );
      case 'Technically_Verified':
        return (
          <span className="px-2 py-0.5 rounded-full text-[10px] sm:text-xs font-mono font-bold bg-amber-950 text-amber-300 border border-amber-800">
            Verified
          </span>
        );
      case 'Published':
        return (
          <span className="px-2 py-0.5 rounded-full text-[10px] sm:text-xs font-mono font-bold bg-emerald-950 text-emerald-300 border border-emerald-800">
            Published
          </span>
        );
    }
  };

  return (
    <div className="space-y-4 sm:space-y-6 max-w-6xl mx-auto pb-20 md:pb-6">
      {/* Header */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-6 shadow-sm flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <div className="flex items-center space-x-1.5 text-cyan-400 text-[10px] sm:text-xs font-mono font-semibold uppercase tracking-wider mb-1">
            <ShieldCheck className="w-3.5 h-3.5" />
            <span>Constitution Rule 3 Enforcement (題目審核工作流)</span>
          </div>
          <h1 className="text-lg sm:text-2xl font-bold text-white tracking-tight">
            {t('cmsTitle')}
          </h1>
          <p className="text-xs text-slate-400 mt-0.5">
            {t('cmsSub')}
          </p>
        </div>

        <button
          onClick={() => setShowCreateModal(true)}
          className="flex items-center justify-center space-x-1.5 py-2.5 px-4 rounded-lg bg-cyan-600 hover:bg-cyan-500 active:scale-95 text-white text-xs font-bold shadow-md transition self-stretch sm:self-auto"
        >
          <Plus className="w-4 h-4" />
          <span>{t('addQuestion')}</span>
        </button>
      </div>

      {/* Error Message Toast */}
      {errorMsg && (
        <div className="bg-rose-950/80 border border-rose-800 text-rose-200 p-3 sm:p-4 rounded-xl text-xs flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <AlertCircle className="w-4 h-4 text-rose-400 shrink-0" />
            <span>{errorMsg}</span>
          </div>
          <button
            onClick={() => setErrorMsg(null)}
            className="text-rose-400 hover:text-white font-bold ml-2 p-1"
          >
            ✕
          </button>
        </div>
      )}

      {/* Pipeline Status Cards (2x2 on Mobile) */}
      {stats && (
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 sm:gap-3">
          <button
            onClick={() => setStatusFilter(statusFilter === 'Draft' ? 'all' : 'Draft')}
            className={`p-3 rounded-xl border text-left transition active:scale-98 ${
              statusFilter === 'Draft'
                ? 'bg-slate-800 border-slate-600 ring-2 ring-slate-500'
                : 'bg-slate-900 border-slate-800 hover:border-slate-700'
            }`}
          >
            <div className="text-[10px] sm:text-xs text-slate-400 font-mono">1. Draft (草稿)</div>
            <div className="text-lg sm:text-xl font-bold font-mono text-slate-200 mt-0.5">
              {stats.Draft}
            </div>
          </button>

          <button
            onClick={() => setStatusFilter(statusFilter === 'AI_Reviewed' ? 'all' : 'AI_Reviewed')}
            className={`p-3 rounded-xl border text-left transition active:scale-98 ${
              statusFilter === 'AI_Reviewed'
                ? 'bg-indigo-950/80 border-indigo-700 ring-2 ring-indigo-500'
                : 'bg-slate-900 border-slate-800 hover:border-slate-700'
            }`}
          >
            <div className="text-[10px] sm:text-xs text-indigo-400 font-mono">2. AI Reviewed</div>
            <div className="text-lg sm:text-xl font-bold font-mono text-indigo-300 mt-0.5">
              {stats.AI_Reviewed}
            </div>
          </button>

          <button
            onClick={() =>
              setStatusFilter(
                statusFilter === 'Technically_Verified' ? 'all' : 'Technically_Verified'
              )
            }
            className={`p-3 rounded-xl border text-left transition active:scale-98 ${
              statusFilter === 'Technically_Verified'
                ? 'bg-amber-950/80 border-amber-700 ring-2 ring-amber-500'
                : 'bg-slate-900 border-slate-800 hover:border-slate-700'
            }`}
          >
            <div className="text-[10px] sm:text-xs text-amber-400 font-mono">3. Verified</div>
            <div className="text-lg sm:text-xl font-bold font-mono text-amber-300 mt-0.5">
              {stats.Technically_Verified}
            </div>
          </button>

          <button
            onClick={() => setStatusFilter(statusFilter === 'Published' ? 'all' : 'Published')}
            className={`p-3 rounded-xl border text-left transition active:scale-98 ${
              statusFilter === 'Published'
                ? 'bg-emerald-950/80 border-emerald-700 ring-2 ring-emerald-500'
                : 'bg-slate-900 border-slate-800 hover:border-slate-700'
            }`}
          >
            <div className="text-[10px] sm:text-xs text-emerald-400 font-mono">4. Published</div>
            <div className="text-lg sm:text-xl font-bold font-mono text-emerald-300 mt-0.5">
              {stats.Published}
            </div>
          </button>
        </div>
      )}

      {/* Search & Filter Bar */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-3 sm:p-4 flex flex-col sm:flex-row gap-2.5 sm:gap-3 items-stretch sm:items-center justify-between">
        <form onSubmit={handleSearch} className="relative w-full sm:w-80">
          <input
            type="text"
            value={searchKeyword}
            onChange={(e) => setSearchKeyword(e.target.value)}
            placeholder={language === 'zh' ? '搜索題幹或法規出處...' : 'Search stem or reference...'}
            className="w-full pl-8 pr-3 py-2 bg-slate-800 border border-slate-700 rounded-lg text-xs text-white placeholder-slate-400 focus:outline-none focus:border-cyan-500"
          />
          <Search className="w-3.5 h-3.5 text-slate-400 absolute left-2.5 top-2.5" />
        </form>

        <div className="flex items-center space-x-1.5 overflow-x-auto pb-0.5 text-xs scrollbar-none">
          <button
            onClick={() => setStatusFilter('all')}
            className={`px-2.5 py-1 rounded-md font-medium shrink-0 transition text-[11px] ${
              statusFilter === 'all'
                ? 'bg-cyan-600 text-white'
                : 'bg-slate-800 text-slate-400 hover:bg-slate-700'
            }`}
          >
            {t('all')} ({stats?.total || 0})
          </button>
          {(['Draft', 'AI_Reviewed', 'Technically_Verified', 'Published'] as QuestionStatus[]).map(
            (st) => (
              <button
                key={st}
                onClick={() => setStatusFilter(st)}
                className={`px-2 py-1 rounded-md font-mono shrink-0 transition text-[11px] ${
                  statusFilter === st
                    ? 'bg-cyan-600 text-white'
                    : 'bg-slate-800 text-slate-400 hover:bg-slate-700'
                }`}
              >
                {st === 'AI_Reviewed' ? 'AI' : st === 'Technically_Verified' ? 'Verified' : st}
              </button>
            )
          )}
        </div>
      </div>

      {/* Questions Review List */}
      {loading ? (
        <div className="flex flex-col items-center justify-center min-h-[200px] space-y-2">
          <div className="w-8 h-8 border-4 border-cyan-500 border-t-transparent rounded-full animate-spin"></div>
          <span className="text-xs text-slate-400">{t('loading')}</span>
        </div>
      ) : questions.length === 0 ? (
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-8 text-center text-xs sm:text-sm text-slate-400">
          {language === 'zh' ? '未找到符合條件的題目' : 'No questions found'}
        </div>
      ) : (
        <div className="space-y-3 sm:space-y-4">
          {questions.slice(0, 30).map((q) => (
            <div
              key={q.id}
              className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-5 shadow-sm space-y-3 transition hover:border-slate-700"
            >
              {/* Card Meta & Badges */}
              <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-2.5">
                <div className="flex flex-wrap items-center gap-1.5">
                  {getStatusBadge(q.status)}
                  <span className="font-mono text-[10px] text-slate-400 bg-slate-800 px-1.5 py-0.5 rounded border border-slate-700">
                    ID: {q.id.slice(0, 6)}...
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
                  onClick={() => handleDelete(q.id)}
                  className="p-1 rounded-lg bg-slate-800 hover:bg-rose-950 text-slate-400 hover:text-rose-400 transition"
                  title="Delete Question"
                >
                  <Trash2 className="w-3.5 h-3.5" />
                </button>
              </div>

              {/* Bilingual Comparison Display */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-2.5 text-xs">
                <div className="bg-slate-950/60 p-3 rounded-lg border border-slate-800/80 space-y-1.5">
                  <div className="text-[10px] font-mono uppercase text-cyan-400 font-bold">
                    English Stem & Options:
                  </div>
                  <div className="text-slate-200 font-medium leading-relaxed">{q.content_en}</div>
                  <div className="space-y-0.5 pt-1 text-[11px] text-slate-400 font-mono">
                    {Object.entries(q.options_en || {}).map(([k, v]) => (
                      <div
                        key={k}
                        className={k === q.correct_answer ? 'text-emerald-400 font-bold' : ''}
                      >
                        {k}: {v} {k === q.correct_answer && '✓'}
                      </div>
                    ))}
                  </div>
                </div>

                <div className="bg-slate-950/60 p-3 rounded-lg border border-slate-800/80 space-y-1.5">
                  <div className="text-[10px] font-mono uppercase text-cyan-400 font-bold">
                    中文題幹與選項:
                  </div>
                  <div className="text-slate-200 font-medium leading-relaxed">{q.content_zh}</div>
                  <div className="space-y-0.5 pt-1 text-[11px] text-slate-400 font-mono">
                    {Object.entries(q.options_zh || {}).map(([k, v]) => (
                      <div
                        key={k}
                        className={k === q.correct_answer ? 'text-emerald-400 font-bold' : ''}
                      >
                        {k}: {v} {k === q.correct_answer && '✓'}
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              {/* Source Reference */}
              <div className="p-2.5 bg-slate-950 rounded-lg border border-slate-800/80 flex items-start space-x-1.5 text-[11px]">
                <FileText className="w-3.5 h-3.5 text-cyan-400 shrink-0 mt-0.5" />
                <div className="text-slate-300">
                  <span className="font-bold text-cyan-400 mr-1 uppercase font-mono">
                    {language === 'zh' ? '法規/規範出處:' : 'Source Ref:'}
                  </span>
                  {q.source_reference ? (
                    <span className="font-mono text-slate-200">{q.source_reference}</span>
                  ) : (
                    <span className="text-rose-400 font-mono italic">
                      [未填寫法規出處，禁止發布]
                    </span>
                  )}
                </div>
              </div>

              {/* Workflow Actions (Mobile Touch Friendly) */}
              <div className="pt-2 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-2 text-xs">
                <div className="flex flex-wrap items-center gap-1.5 w-full sm:w-auto">
                  {q.status === 'Draft' && (
                    <button
                      onClick={() => handleStatusTransition(q.id, 'AI_Reviewed')}
                      className="flex-1 sm:flex-initial px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 active:scale-95 text-white font-semibold flex items-center justify-center space-x-1 text-xs"
                    >
                      <span>推進 AI初審</span>
                      <ArrowRight className="w-3 h-3" />
                    </button>
                  )}

                  {q.status === 'AI_Reviewed' && (
                    <button
                      onClick={() => handleStatusTransition(q.id, 'Technically_Verified')}
                      className="flex-1 sm:flex-initial px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 active:scale-95 text-white font-semibold flex items-center justify-center space-x-1 text-xs"
                    >
                      <span>技術核實 (Verified)</span>
                      <ArrowRight className="w-3 h-3" />
                    </button>
                  )}

                  {q.status === 'Technically_Verified' && (
                    <button
                      onClick={() => handleStatusTransition(q.id, 'Published')}
                      className="flex-1 sm:flex-initial px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 active:scale-95 text-white font-semibold flex items-center justify-center space-x-1 text-xs"
                    >
                      <span>正式發布 (Publish)</span>
                      <CheckCircle2 className="w-3 h-3" />
                    </button>
                  )}

                  {q.status !== 'Draft' && (
                    <button
                      onClick={() => handleStatusTransition(q.id, 'Draft')}
                      className="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 active:scale-95 text-slate-400 hover:text-slate-200 border border-slate-700 flex items-center space-x-1 text-xs"
                    >
                      <RotateCcw className="w-3 h-3" />
                      <span>{t('demoteDraft')}</span>
                    </button>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Create New Question Modal (Mobile Fullscreen or Centered) */}
      {showCreateModal && (
        <div className="fixed inset-0 bg-black/85 backdrop-blur-sm z-50 flex items-end sm:items-center justify-center p-0 sm:p-4 overflow-y-auto">
          <div className="bg-slate-900 border-t sm:border border-slate-800 rounded-t-2xl sm:rounded-2xl max-w-3xl w-full p-4 sm:p-6 shadow-2xl space-y-4 max-h-[92vh] overflow-y-auto">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div>
                <h3 className="text-base sm:text-lg font-bold text-white flex items-center space-x-2">
                  <ShieldCheck className="w-4 h-4 sm:w-5 sm:h-5 text-cyan-400" />
                  <span>{language === 'zh' ? '錄入新原創題目 (共享 Question ID)' : 'Create Original Question (Shared ID)'}</span>
                </h3>
                <p className="text-[10px] sm:text-xs text-slate-400 mt-0.5">
                  遵循 Rule C：中英雙語題目同時保存，共享同一個 UUID 實體。
                </p>
              </div>
              <button
                onClick={() => setShowCreateModal(false)}
                className="p-1.5 text-slate-400 hover:text-white"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <form onSubmit={handleCreateQuestion} className="space-y-3.5 text-xs sm:text-sm">
              {/* Question Stems */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div className="space-y-1">
                  <label className="text-slate-300 font-semibold text-xs">English Question Stem *</label>
                  <textarea
                    required
                    rows={2}
                    value={formData.content_en}
                    onChange={(e) => setFormData({ ...formData, content_en: e.target.value })}
                    placeholder="Enter scenario-based question in English..."
                    className="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-white text-xs focus:outline-none focus:border-cyan-500"
                  />
                </div>
                <div className="space-y-1">
                  <label className="text-slate-300 font-semibold text-xs">中文題幹 (繁體/簡體) *</label>
                  <textarea
                    required
                    rows={2}
                    value={formData.content_zh}
                    onChange={(e) => setFormData({ ...formData, content_zh: e.target.value })}
                    placeholder="輸入對應的中文場景化題幹..."
                    className="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-white text-xs focus:outline-none focus:border-cyan-500"
                  />
                </div>
              </div>

              {/* Options A, B, C, D */}
              <div className="space-y-1.5">
                <label className="text-slate-300 font-semibold block text-xs">
                  Options (A, B, C, D) & Correct Answer Selector *
                </label>
                {(['A', 'B', 'C', 'D'] as const).map((opt) => (
                  <div key={opt} className="grid grid-cols-12 gap-1.5 items-center">
                    <div className="col-span-2 sm:col-span-1 font-mono font-bold text-cyan-400 text-center text-xs">
                      [{opt}]
                    </div>
                    <div className="col-span-5 sm:col-span-5">
                      <input
                        type="text"
                        required
                        placeholder={`Option ${opt} EN`}
                        value={formData.options_en[opt] || ''}
                        onChange={(e) =>
                          setFormData({
                            ...formData,
                            options_en: { ...formData.options_en, [opt]: e.target.value },
                          })
                        }
                        className="w-full bg-slate-800 border border-slate-700 rounded-lg p-1.5 text-white text-[11px] focus:outline-none focus:border-cyan-500"
                      />
                    </div>
                    <div className="col-span-4 sm:col-span-5">
                      <input
                        type="text"
                        required
                        placeholder={`選項 ${opt} 中文`}
                        value={formData.options_zh[opt] || ''}
                        onChange={(e) =>
                          setFormData({
                            ...formData,
                            options_zh: { ...formData.options_zh, [opt]: e.target.value },
                          })
                        }
                        className="w-full bg-slate-800 border border-slate-700 rounded-lg p-1.5 text-white text-[11px] focus:outline-none focus:border-cyan-500"
                      />
                    </div>
                    <div className="col-span-1 text-center">
                      <input
                        type="radio"
                        name="correct_answer"
                        checked={formData.correct_answer === opt}
                        onChange={() => setFormData({ ...formData, correct_answer: opt })}
                        className="cursor-pointer text-cyan-500"
                      />
                    </div>
                  </div>
                ))}
              </div>

              {/* Source Reference & Mappings */}
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5 pt-1">
                <div className="space-y-1">
                  <label className="text-slate-300 font-semibold text-xs">
                    法規/規範出處 (Source Ref) *
                  </label>
                  <input
                    type="text"
                    required
                    value={formData.source_reference}
                    onChange={(e) => setFormData({ ...formData, source_reference: e.target.value })}
                    placeholder="如 BS 7671, Water Regs 1999"
                    className="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-white text-xs focus:outline-none focus:border-cyan-500"
                  />
                </div>

                <div className="space-y-1">
                  <label className="text-slate-300 font-semibold text-xs">教材章節 (Chapter)</label>
                  <select
                    value={formData.chapter_ids?.[0]?.chapter_id || 1}
                    onChange={(e) =>
                      setFormData({
                        ...formData,
                        chapter_ids: [
                          {
                            chapter_id: parseInt(e.target.value),
                            sub_topic_id: `${e.target.value}.1`,
                          },
                        ],
                      })
                    }
                    className="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-white text-xs"
                  >
                    {chapters.map((ch) => (
                      <option key={ch.id} value={ch.id}>
                        Ch {ch.id}: {ch.title}
                      </option>
                    ))}
                  </select>
                </div>

                <div className="space-y-1">
                  <label className="text-slate-300 font-semibold text-xs">考綱單元 (Unit)</label>
                  <select
                    value={formData.unit_ids?.[0] || 'Unit_201'}
                    onChange={(e) =>
                      setFormData({
                        ...formData,
                        unit_ids: [e.target.value],
                      })
                    }
                    className="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-white text-xs"
                  >
                    {units.map((u) => (
                      <option key={u.id} value={u.id}>
                        {u.id}: {u.title}
                      </option>
                    ))}
                  </select>
                </div>
              </div>

              {/* Submit / Cancel Buttons */}
              <div className="flex justify-end space-x-2 pt-3 border-t border-slate-800">
                <button
                  type="button"
                  onClick={() => setShowCreateModal(false)}
                  className="px-4 py-2 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs font-semibold"
                >
                  {t('cancel')}
                </button>
                <button
                  type="submit"
                  className="px-5 py-2 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold shadow-md active:scale-95"
                >
                  {language === 'zh' ? '保存為草稿 (Draft)' : 'Save as Draft'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
