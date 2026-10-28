'use client';

import React, { useState, useEffect } from 'react';
import { Navbar } from '../components/Navbar';
import { ChapterList } from '../components/ChapterList';
import { UnitList } from '../components/UnitList';
import { QuizPlayer } from '../components/QuizPlayer';
import { MockExamConfig } from '../components/MockExamConfig';
import { ExamResultModal } from '../components/ExamResultModal';
import { WrongQuestionsView } from '../components/WrongQuestionsView';
import { AnalyticsView } from '../components/AnalyticsView';
import { CMSDashboard } from '../components/CMSDashboard';
import { TextbookChapter, ExamUnit, Question, WrongQuestionRecord, QuizSessionState } from '../types';
import { api } from '../services/api';
import { storage } from '../services/storage';
import { useLanguage } from '../context/LanguageContext';
import { RotateCcw, Play, Clock, X } from 'lucide-react';

export default function Home() {
  const { language, t } = useLanguage();

  const [activeTab, setActiveTab] = useState<string>('chapters');
  const [chapters, setChapters] = useState<TextbookChapter[]>([]);
  const [units, setUnits] = useState<ExamUnit[]>([]);
  const [loadingData, setLoadingData] = useState<boolean>(true);
  const [wrongCount, setWrongCount] = useState<number>(0);
  const [lastActiveSession, setLastActiveSession] = useState<QuizSessionState | null>(null);
  const [activeSessions, setActiveSessions] = useState<Record<string, QuizSessionState>>({});

  // Prompt when clicking an item that has an in-progress session
  const [resumePrompt, setResumePrompt] = useState<{
    session: QuizSessionState;
    onConfirm: () => void;
    onCancel: () => void;
  } | null>(null);

  // Active Quiz State
  const [quizState, setQuizState] = useState<{
    questions: Question[];
    title: string;
    subtitle?: string;
    mode: 'practice' | 'mock';
    targetType: 'chapter' | 'unit' | 'mock';
    targetId: string | number;
    subTopicId?: string;
    durationMinutes?: number;
    initialIndex?: number;
    initialSelectedAnswers?: Record<string, string>;
    initialShowExplanation?: Record<string, boolean>;
    initialFlagged?: Record<string, boolean>;
    initialTimeLeft?: number;
  } | null>(null);

  // Mock Result State
  const [mockResult, setMockResult] = useState<{
    total: number;
    score: number;
    wrongQuestions: Question[];
  } | null>(null);

  const loadInitialData = async () => {
    try {
      setLoadingData(true);
      const [chData, uData] = await Promise.all([
        api.getChapters(),
        api.getUnits(),
      ]);
      setChapters(chData);
      setUnits(uData);
    } catch (e) {
      console.error('Failed to load initial chapters/units:', e);
    } finally {
      setLoadingData(false);
      refreshWrongCount();
      refreshSessions();
    }
  };

  const refreshWrongCount = () => {
    const list = storage.getWrongQuestions();
    setWrongCount(list.length);
  };

  const refreshSessions = () => {
    const last = storage.getLastActiveSession();
    setLastActiveSession(last);
    const all = storage.getAllActiveSessions();
    setActiveSessions(all);
  };

  useEffect(() => {
    loadInitialData();
  }, []);

  const handleResumeSession = (session: QuizSessionState) => {
    setQuizState({
      questions: session.questions,
      title: session.title,
      subtitle: session.subtitle,
      mode: session.mode,
      targetType: session.targetType,
      targetId: session.targetId,
      subTopicId: session.subTopicId,
      durationMinutes: session.durationMinutes,
      initialIndex: session.currentIndex,
      initialSelectedAnswers: session.selectedAnswers,
      initialShowExplanation: session.showExplanation,
      initialFlagged: session.flagged,
      initialTimeLeft: session.timeLeft,
    });
  };

  // Practice by Chapter
  const handleSelectChapter = async (chapterId: number, subTopicId?: string) => {
    const sessionKey = `chapter_${chapterId}${subTopicId ? '_' + subTopicId : ''}`;
    const saved = storage.getQuizSession(sessionKey);

    if (saved && saved.questions && saved.questions.length > 0) {
      setResumePrompt({
        session: saved,
        onConfirm: () => {
          handleResumeSession(saved);
          setResumePrompt(null);
        },
        onCancel: async () => {
          storage.clearQuizSession(sessionKey);
          setResumePrompt(null);
          await startFreshChapter(chapterId, subTopicId);
        },
      });
      return;
    }

    await startFreshChapter(chapterId, subTopicId);
  };

  const startFreshChapter = async (chapterId: number, subTopicId?: string) => {
    try {
      setLoadingData(true);
      const questions = await api.getQuestionsByChapter(chapterId, subTopicId);
      const ch = chapters.find((c) => c.id === chapterId);
      const title = subTopicId
        ? `Chapter ${chapterId} (${subTopicId}) - ${ch?.title}`
        : `Chapter ${chapterId} - ${ch?.title}`;

      setQuizState({
        questions,
        title,
        mode: 'practice',
        targetType: 'chapter',
        targetId: chapterId,
        subTopicId,
        initialIndex: 0,
      });
    } catch (e) {
      console.error(e);
      alert(language === 'zh' ? '加載題目失敗，請確認後端服務已啟動。' : 'Failed to load questions.');
    } finally {
      setLoadingData(false);
    }
  };

  // Practice by Unit
  const handleSelectUnit = async (unitId: string) => {
    const sessionKey = `unit_${unitId}`;
    const saved = storage.getQuizSession(sessionKey);

    if (saved && saved.questions && saved.questions.length > 0) {
      setResumePrompt({
        session: saved,
        onConfirm: () => {
          handleResumeSession(saved);
          setResumePrompt(null);
        },
        onCancel: async () => {
          storage.clearQuizSession(sessionKey);
          setResumePrompt(null);
          await startFreshUnit(unitId);
        },
      });
      return;
    }

    await startFreshUnit(unitId);
  };

  const startFreshUnit = async (unitId: string) => {
    try {
      setLoadingData(true);
      const questions = await api.getQuestionsByUnit(unitId);
      const u = units.find((item) => item.id === unitId);
      const title = `${unitId}: ${u?.title}`;

      setQuizState({
        questions,
        title,
        mode: 'practice',
        targetType: 'unit',
        targetId: unitId,
        initialIndex: 0,
      });
    } catch (e) {
      console.error(e);
      alert(language === 'zh' ? '加載題目失敗，請確認後端服務已啟動。' : 'Failed to load questions.');
    } finally {
      setLoadingData(false);
    }
  };

  // Start Mock Exam
  const handleStartMockExam = async (count: number, durationMinutes: number) => {
    const sessionKey = 'mock_mock_session';
    const saved = storage.getQuizSession(sessionKey);

    if (saved && saved.questions && saved.questions.length > 0 && (saved.timeLeft === undefined || saved.timeLeft > 0)) {
      setResumePrompt({
        session: saved,
        onConfirm: () => {
          handleResumeSession(saved);
          setResumePrompt(null);
        },
        onCancel: async () => {
          storage.clearQuizSession(sessionKey);
          setResumePrompt(null);
          await startFreshMock(count, durationMinutes);
        },
      });
      return;
    }

    await startFreshMock(count, durationMinutes);
  };

  const startFreshMock = async (count: number, durationMinutes: number) => {
    try {
      setLoadingData(true);
      const questions = await api.getMockExam(count);
      setQuizState({
        questions,
        title: language === 'zh' ? 'City & Guilds 全真模擬測試' : 'City & Guilds Simulated Mock Exam',
        mode: 'mock',
        targetType: 'mock',
        targetId: 'mock_session',
        durationMinutes,
        initialIndex: 0,
      });
    } catch (e) {
      console.error(e);
      alert(language === 'zh' ? '加載模擬試卷失敗，請確認後端已啟動。' : 'Failed to load mock exam.');
    } finally {
      setLoadingData(false);
    }
  };

  // Redo Wrong Questions
  const handlePracticeWrong = (records: WrongQuestionRecord[]) => {
    const questions = records.map((r) => r.question);
    setQuizState({
      questions,
      title: language === 'zh' ? '錯題本專項補強練習' : 'Mistakes Retest Drill',
      mode: 'practice',
      targetType: 'mock',
      targetId: 'wrong_retest',
      initialIndex: 0,
    });
  };

  const handleExitQuiz = () => {
    setQuizState(null);
    refreshWrongCount();
    refreshSessions();
  };

  const handleCompleteMock = (result: {
    total: number;
    score: number;
    wrongQuestions: Question[];
  }) => {
    setQuizState(null);
    setMockResult(result);
    refreshWrongCount();
    refreshSessions();
  };

  // Total Published Questions count across chapters
  const totalPublishedQuestions = chapters.reduce(
    (sum, c) => sum + (c.question_count || 0),
    0
  );

  return (
    <div className="min-h-screen flex flex-col bg-slate-950 text-slate-100">
      <Navbar
        activeTab={activeTab}
        setActiveTab={(tab) => {
          setQuizState(null);
          setMockResult(null);
          setActiveTab(tab);
          refreshWrongCount();
        }}
        wrongCount={wrongCount}
        hideMobileBottomBar={!!quizState}
      />

      <main className="flex-1 max-w-7xl w-full mx-auto px-3 sm:px-6 lg:px-8 py-3.5 sm:py-8 pb-24 md:pb-8">
        {/* Global Resume Notification Banner when returning after disconnect / exit */}
        {!quizState && !mockResult && lastActiveSession && (
          <div className="bg-gradient-to-r from-amber-950/70 via-slate-900 to-cyan-950/70 border border-amber-500/40 rounded-xl p-3 sm:p-4 mb-4 sm:mb-6 shadow-xl flex flex-col sm:flex-row sm:items-center justify-between gap-3 animate-in fade-in duration-200">
            <div className="flex items-start space-x-3">
              <div className="p-2 rounded-lg bg-amber-500/20 text-amber-400 shrink-0 mt-0.5">
                <RotateCcw className="w-5 h-5 animate-pulse" />
              </div>
              <div>
                <div className="flex items-center space-x-2">
                  <span className="text-xs font-mono font-bold uppercase tracking-wider text-amber-400">
                    {t('resumeBannerTitle')}
                  </span>
                  <span className="text-[10px] bg-amber-900/60 text-amber-200 px-1.5 py-0.2 rounded border border-amber-700/60 font-mono">
                    {lastActiveSession.mode === 'mock' ? t('examMode') : t('practiceMode')}
                  </span>
                </div>
                <p className="text-sm font-bold text-white mt-0.5">
                  {lastActiveSession.title}
                </p>
                <p className="text-xs text-slate-400">
                  {language === 'zh'
                    ? `中途退出/斷線自動留存：上次答題進度停留在第 ${lastActiveSession.currentIndex + 1} 題 / 共 ${lastActiveSession.questions.length} 題`
                    : `Disconnected or exited: Saved at Question ${lastActiveSession.currentIndex + 1} / ${lastActiveSession.questions.length}`}
                </p>
              </div>
            </div>

            <div className="flex items-center space-x-2 self-end sm:self-auto shrink-0">
              <button
                onClick={() => handleResumeSession(lastActiveSession)}
                className="px-4 py-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 active:scale-95 text-slate-950 font-bold text-xs rounded-lg shadow-md transition flex items-center space-x-1.5"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>
                  {language === 'zh'
                    ? `從第 ${lastActiveSession.currentIndex + 1} 題繼續`
                    : `Resume from Q${lastActiveSession.currentIndex + 1}`}
                </span>
              </button>
              <button
                onClick={() => {
                  storage.clearQuizSession(lastActiveSession.sessionKey);
                  refreshSessions();
                }}
                className="px-2.5 py-2 bg-slate-800 hover:bg-slate-700 active:scale-95 text-slate-400 hover:text-slate-200 text-xs rounded-lg border border-slate-700 transition"
                title={t('discard')}
              >
                <X className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        )}

        {/* Modal Prompt when user clicks on an item with existing saved session */}
        {resumePrompt && (
          <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
            <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 max-w-md w-full shadow-2xl space-y-4 animate-in zoom-in-95 duration-150">
              <div className="flex items-center space-x-3 text-amber-400">
                <div className="p-2 bg-amber-500/20 rounded-lg">
                  <RotateCcw className="w-5 h-5" />
                </div>
                <h3 className="text-base font-bold text-white">{t('resumeTitle')}</h3>
              </div>
              <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                {language === 'zh'
                  ? `您之前在「${resumePrompt.session.title}」中途退出或斷線，系統已自動留存答題進度至第 ${resumePrompt.session.currentIndex + 1} 題（共 ${resumePrompt.session.questions.length} 題）。您想要：`
                  : `You exited or disconnected during "${resumePrompt.session.title}". Progress is saved at Question ${resumePrompt.session.currentIndex + 1} of ${resumePrompt.session.questions.length}. Would you like to:`}
              </p>
              <div className="space-y-2 pt-2">
                <button
                  onClick={resumePrompt.onConfirm}
                  className="w-full py-2.5 px-4 rounded-xl bg-cyan-600 hover:bg-cyan-500 active:scale-98 text-white text-xs sm:text-sm font-bold shadow-md transition flex items-center justify-center space-x-2"
                >
                  <Play className="w-4 h-4 fill-current" />
                  <span>
                    {language === 'zh'
                      ? `從第 ${resumePrompt.session.currentIndex + 1} 題繼續作答`
                      : `Resume from Question ${resumePrompt.session.currentIndex + 1}`}
                  </span>
                </button>
                <button
                  onClick={resumePrompt.onCancel}
                  className="w-full py-2.5 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 active:scale-98 text-slate-300 text-xs sm:text-sm font-semibold border border-slate-700 transition flex items-center justify-center space-x-2"
                >
                  <RotateCcw className="w-3.5 h-3.5" />
                  <span>{t('startFresh')}</span>
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Active Quiz Player */}
        {quizState ? (
          <QuizPlayer
            questions={quizState.questions}
            title={quizState.title}
            subtitle={quizState.subtitle}
            mode={quizState.mode}
            targetType={quizState.targetType}
            targetId={quizState.targetId}
            subTopicId={quizState.subTopicId}
            initialTimeMinutes={quizState.durationMinutes || 20}
            initialIndex={quizState.initialIndex ?? 0}
            initialSelectedAnswers={quizState.initialSelectedAnswers}
            initialShowExplanation={quizState.initialShowExplanation}
            initialFlagged={quizState.initialFlagged}
            initialTimeLeft={quizState.initialTimeLeft}
            onExit={handleExitQuiz}
            onCompleteMock={handleCompleteMock}
          />
        ) : mockResult ? (
          /* Mock Exam Result Modal View */
          <ExamResultModal
            total={mockResult.total}
            score={mockResult.score}
            wrongQuestions={mockResult.wrongQuestions}
            onRetake={() => {
              setMockResult(null);
              setActiveTab('mock');
            }}
            onGoToWrong={() => {
              setMockResult(null);
              setActiveTab('wrong');
            }}
            onExit={() => {
              setMockResult(null);
              setActiveTab('chapters');
            }}
          />
        ) : (
          /* Main Tab Views */
          <div>
            {activeTab === 'chapters' && (
              <ChapterList
                chapters={chapters}
                onSelectChapter={handleSelectChapter}
                loading={loadingData}
                activeSessions={activeSessions}
              />
            )}

            {activeTab === 'units' && (
              <UnitList
                units={units}
                onSelectUnit={handleSelectUnit}
                loading={loadingData}
                activeSessions={activeSessions}
              />
            )}

            {activeTab === 'mock' && (
              <MockExamConfig
                totalAvailable={totalPublishedQuestions}
                onStartExam={handleStartMockExam}
              />
            )}

            {activeTab === 'wrong' && (
              <WrongQuestionsView
                onPracticeWrong={handlePracticeWrong}
                onRefreshCount={refreshWrongCount}
              />
            )}

            {activeTab === 'analytics' && (
              <AnalyticsView chapters={chapters} units={units} />
            )}

            {activeTab === 'cms' && (
              <CMSDashboard
                chapters={chapters}
                units={units}
                onRefreshData={() => {
                  loadInitialData();
                  refreshWrongCount();
                }}
              />
            )}
          </div>
        )}
      </main>

      {/* Engineering Footer */}
      <footer className="border-t border-slate-900 bg-slate-950 pt-5 pb-24 md:pb-6 text-center text-xs text-slate-500 space-y-2 px-4">
        <div className="flex flex-wrap justify-center items-center gap-x-4 gap-y-1 font-mono text-[11px]">
          <span>Project Constitution Compliant</span>
          <span>•</span>
          <span>Rule A: Schema Invariant</span>
          <span>•</span>
          <span>Rule B: Tailwind Engineering Design</span>
          <span>•</span>
          <span>Rule C: Shared Question ID (Dual-lingual Entity)</span>
        </div>
        <p>City & Guilds 6035 / 8202 Plumbing & Heating Qualification Practice System</p>
      </footer>
    </div>
  );
}
