'use client';

import React, { createContext, useContext, useState, useEffect } from 'react';

type Language = 'zh' | 'en';

interface LanguageContextType {
  language: Language;
  setLanguage: (lang: Language) => void;
  toggleLanguage: () => void;
  t: (key: string) => string;
}

const translations: Record<string, { zh: string; en: string }> = {
  // App brand & navigation
  platformTitle: { zh: '英國水暖工模擬考試平台', en: 'UK Plumbing Exam Platform' },
  platformSub: { zh: 'City & Guilds 6035 / 8202 雙軌知識庫', en: 'City & Guilds 6035 / 8202 Knowledge System' },
  tabChapters: { zh: '教材章節練習', en: 'Textbook Chapters' },
  tabUnits: { zh: '考試單元練習', en: 'Exam Units' },
  tabMock: { zh: '全真模擬考', en: 'Mock Exam' },
  tabWrong: { zh: '錯題本', en: 'Mistake Notebook' },
  tabAnalytics: { zh: '掌握度分析', en: 'Mastery Analytics' },
  tabCMS: { zh: '題目審核後台', en: 'CMS Review' },

  // General & actions
  loading: { zh: '加載中...', en: 'Loading...' },
  back: { zh: '返回', en: 'Back' },
  next: { zh: '下一題', en: 'Next Question' },
  prev: { zh: '上一題', en: 'Previous Question' },
  submit: { zh: '提交考卷', en: 'Submit Exam' },
  confirm: { zh: '確認', en: 'Confirm' },
  cancel: { zh: '取消', en: 'Cancel' },
  reset: { zh: '重置', en: 'Reset' },
  filter: { zh: '篩選', en: 'Filter' },
  search: { zh: '搜索...', en: 'Search...' },
  all: { zh: '全部', en: 'All' },
  save: { zh: '保存', en: 'Save' },
  status: { zh: '狀態', en: 'Status' },
  actions: { zh: '操作', en: 'Actions' },

  // Practice & Quiz
  practiceMode: { zh: '練習模式', en: 'Practice Mode' },
  examMode: { zh: '全真模擬測試', en: 'Simulated Exam Mode' },
  question: { zh: '題目', en: 'Question' },
  explanation: { zh: '技術解析', en: 'Technical Explanation' },
  sourceRef: { zh: '法規與規範出處', en: 'Standard & Regulatory Reference' },
  checkAnswer: { zh: '查看答案解析', en: 'Check Explanation' },
  hideAnswer: { zh: '收起解析', en: 'Hide Explanation' },
  correct: { zh: '回答正確', en: 'Correct Answer' },
  incorrect: { zh: '回答錯誤', en: 'Incorrect Answer' },
  yourAnswer: { zh: '你的答案', en: 'Your Answer' },
  correctAnswer: { zh: '正確答案', en: 'Correct Answer' },
  flagForReview: { zh: '標記複查', en: 'Flag for Review' },
  unflag: { zh: '取消標記', en: 'Unflag' },
  timeLeft: { zh: '剩餘時間', en: 'Time Remaining' },
  questionIndex: { zh: '答題卡', en: 'Question Palette' },
  noQuestionsFound: { zh: '當前分類暫無已發布題目', en: 'No published questions found in this category' },
  startPractice: { zh: '開始練習', en: 'Start Practice' },
  questionsAvailable: { zh: '道可用題目', en: 'questions available' },

  // Exam result
  examCompleted: { zh: '模擬考試結束', en: 'Mock Exam Completed' },
  score: { zh: '得分', en: 'Score' },
  passStatus: { zh: '考覈結果', en: 'Assessment Result' },
  passed: { zh: '考試合格 (PASS)', en: 'PASS' },
  failed: { zh: '未通過 (FAIL)', en: 'FAIL' },
  passThresholdNotice: { zh: '英國 City & Guilds 6035 及格標準通常為 60%~70%', en: 'City & Guilds 6035 pass benchmark is typically 60%~70%' },
  reviewMistakes: { zh: '查看錯題分析', en: 'Review Mistakes' },
  retakeExam: { zh: '重新測驗', en: 'Retake Exam' },

  // Mistake notebook
  wrongTitle: { zh: '個人錯題本 (本機自動留存)', en: 'Personal Mistake Notebook (Stored Locally)' },
  wrongEmpty: { zh: '目前沒有做錯的題目！繼續保持！', en: 'No mistakes recorded yet. Keep up the good work!' },
  clearAllWrong: { zh: '清空錯題本', en: 'Clear Mistake Book' },
  removeMistake: { zh: '已掌握，移除', en: 'Mastered, Remove' },
  redoWrongQuestions: { zh: '重新練習所有錯題', en: 'Re-practice Mistakes' },

  // Analytics
  masterySummary: { zh: '學習成效與掌握度雷達分析', en: 'Learning Mastery & Analytics' },
  totalQuestionsAttempted: { zh: '總做題量', en: 'Questions Attempted' },
  overallAccuracy: { zh: '整體正確率', en: 'Overall Accuracy' },
  chapterMastery: { zh: '按 11 本教材章節掌握度', en: 'Mastery by 11 Textbook Chapters' },
  unitMastery: { zh: '按 10 大考綱單元掌握度', en: 'Mastery by 10 Qualification Units' },

  // CMS
  cmsTitle: { zh: '題庫內容審核工作流 (CMS Review Flow)', en: 'Question CMS & Verification Flow' },
  cmsSub: { zh: '嚴格遵循三項核心規則：草稿 → AI初審 → 技術核實 (強制附法規) → 正式發布', en: 'Constitution Rule 3: Draft → AI Reviewed → Technically Verified (Ref Required) → Published' },
  addQuestion: { zh: '新建原創題目', en: 'Create New Question' },
  filterAllStatus: { zh: '所有狀態', en: 'All Statuses' },
  stageDraft: { zh: 'Draft (草稿)', en: 'Draft' },
  stageAIRewiewed: { zh: 'AI Reviewed (AI 初審)', en: 'AI Reviewed' },
  stageVerified: { zh: 'Technically Verified (技術核實)', en: 'Technically Verified' },
  stagePublished: { zh: 'Published (正式發布)', en: 'Published' },
  promoteNext: { zh: '推進入下一階段', en: 'Promote Stage' },
  demoteDraft: { zh: '退回草稿', en: 'Demote to Draft' },
  sourceRequiredNotice: { zh: '注意：進入「技術核實」及「正式發布」必須附帶權威法規/規範出處 (Rule 3)', en: 'Notice: Advancing to Verified or Published requires mandatory standard reference (Rule 3)' },

  // Session recovery & Unfinished test resume
  resumeTitle: { zh: '發現未完成的測驗進度', en: 'Unfinished Quiz Session Detected' },
  resumeDesc: { zh: '系統檢測到您之前中途退出或斷線，是否從上次中斷的題目繼續？', en: 'System detected that you previously disconnected or exited. Would you like to resume from where you left off?' },
  resumeFromQ: { zh: '繼續上次進度', en: 'Resume Previous Session' },
  startFresh: { zh: '重新開始', en: 'Start Fresh' },
  resumeBannerTitle: { zh: '未完成的測驗進度', en: 'In-Progress Quiz' },
  resumeBannerAction: { zh: '點擊繼續做題', en: 'Click to Resume' },
  discard: { zh: '放棄記錄', en: 'Discard' },
  inProgress: { zh: '進行中', en: 'In Progress' },
  autoSavedTip: { zh: '做題進度已即時自動留存，中途退出或斷線可隨時原題繼續', en: 'Progress auto-saved in real-time. Safe to exit or disconnect anytime.' },

  // Unit-Based Mock Exams
  mockUnitTab: { zh: '按 Units 單元專項全真模考', en: 'Unit-by-Unit Mock Exams' },
  mockAllTab: { zh: '全科綜合全真大考 (All-Units)', en: 'Comprehensive Full Mock Exam' },
  selectUnitToExam: { zh: '選擇要進行模擬考核的認證單元 (Units)', en: 'Select Qualification Unit for Timed Exam' },
  startUnitMock: { zh: '開始單元全真模考', en: 'Start Unit Mock Exam' },
  startAllMock: { zh: '開始全科綜合大考', en: 'Start Full Mock Exam' },
  selectedUnit: { zh: '當前選擇單元', en: 'Selected Unit' },
  allCategories: { zh: '所有分類', en: 'All Categories' },
};

const getInitialLanguage = (): Language => {
  if (typeof window === 'undefined') return 'zh';
  const saved = localStorage.getItem('plumbing_exam_lang');
  if (saved === 'en' || saved === 'zh') {
    return saved;
  }
  try {
    const navLang = (
      navigator.language ||
      (navigator.languages && navigator.languages[0]) ||
      ''
    ).toLowerCase();
    if (navLang.startsWith('zh')) {
      return 'zh';
    }
    return 'en';
  } catch {
    return 'zh';
  }
};

const LanguageContext = createContext<LanguageContextType>({
  language: 'zh',
  setLanguage: () => {},
  toggleLanguage: () => {},
  t: (key) => key,
});

export const LanguageProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [language, setLanguageState] = useState<Language>('zh');

  useEffect(() => {
    const initial = getInitialLanguage();
    setLanguageState(initial);

    const handleLangChange = () => {
      const saved = localStorage.getItem('plumbing_exam_lang');
      if (!saved) {
        setLanguageState(getInitialLanguage());
      }
    };

    window.addEventListener('languagechange', handleLangChange);
    return () => window.removeEventListener('languagechange', handleLangChange);
  }, []);

  const setLanguage = (lang: Language) => {
    setLanguageState(lang);
    localStorage.setItem('plumbing_exam_lang', lang);
  };

  const toggleLanguage = () => {
    const nextLang = language === 'zh' ? 'en' : 'zh';
    setLanguage(nextLang);
  };

  const t = (key: string): string => {
    if (translations[key]) {
      return translations[key][language] || key;
    }
    return key;
  };

  return (
    <LanguageContext.Provider value={{ language, setLanguage, toggleLanguage, t }}>
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = () => useContext(LanguageContext);
