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
import { TextbookChapter, ExamUnit, Question, WrongQuestionRecord } from '../types';
import { api } from '../services/api';
import { storage } from '../services/storage';
import { useLanguage } from '../context/LanguageContext';

export default function Home() {
  const { language } = useLanguage();

  const [activeTab, setActiveTab] = useState<string>('chapters');
  const [chapters, setChapters] = useState<TextbookChapter[]>([]);
  const [units, setUnits] = useState<ExamUnit[]>([]);
  const [loadingData, setLoadingData] = useState<boolean>(true);
  const [wrongCount, setWrongCount] = useState<number>(0);

  // Active Quiz State
  const [quizState, setQuizState] = useState<{
    questions: Question[];
    title: string;
    mode: 'practice' | 'mock';
    targetType: 'chapter' | 'unit' | 'mock';
    targetId: string | number;
    durationMinutes?: number;
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
    }
  };

  const refreshWrongCount = () => {
    const list = storage.getWrongQuestions();
    setWrongCount(list.length);
  };

  useEffect(() => {
    loadInitialData();
  }, []);

  // Practice by Chapter
  const handleSelectChapter = async (chapterId: number, subTopicId?: string) => {
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
    });
  };

  const handleExitQuiz = () => {
    setQuizState(null);
    refreshWrongCount();
  };

  const handleCompleteMock = (result: {
    total: number;
    score: number;
    wrongQuestions: Question[];
  }) => {
    setQuizState(null);
    setMockResult(result);
    refreshWrongCount();
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
        {/* Active Quiz Player */}
        {quizState ? (
          <QuizPlayer
            questions={quizState.questions}
            title={quizState.title}
            mode={quizState.mode}
            targetType={quizState.targetType}
            targetId={quizState.targetId}
            initialTimeMinutes={quizState.durationMinutes || 20}
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
              />
            )}

            {activeTab === 'units' && (
              <UnitList
                units={units}
                onSelectUnit={handleSelectUnit}
                loading={loadingData}
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
