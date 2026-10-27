import { Question, WrongQuestionRecord, UserProgressStat } from '../types';

const WRONG_STORAGE_KEY = 'plumbing_exam_wrong_questions';
const PROGRESS_STORAGE_KEY = 'plumbing_exam_progress_stats';

export const storage = {
  getWrongQuestions(): WrongQuestionRecord[] {
    if (typeof window === 'undefined') return [];
    try {
      const data = localStorage.getItem(WRONG_STORAGE_KEY);
      return data ? JSON.parse(data) : [];
    } catch {
      return [];
    }
  },

  addWrongQuestion(
    question: Question,
    selectedAnswer: string,
    mode: 'chapter' | 'unit' | 'mock',
    targetId: string | number
  ): void {
    if (typeof window === 'undefined') return;
    try {
      const existing = this.getWrongQuestions();
      const filtered = existing.filter((item) => item.question.id !== question.id);
      filtered.unshift({
        question,
        selected_answer: selectedAnswer,
        timestamp: Date.now(),
        mode,
        target_id: targetId,
      });
      localStorage.setItem(WRONG_STORAGE_KEY, JSON.stringify(filtered));
    } catch (e) {
      console.error('Failed to save wrong question', e);
    }
  },

  removeWrongQuestion(questionId: string): void {
    if (typeof window === 'undefined') return;
    try {
      const existing = this.getWrongQuestions();
      const updated = existing.filter((item) => item.question.id !== questionId);
      localStorage.setItem(WRONG_STORAGE_KEY, JSON.stringify(updated));
    } catch (e) {
      console.error('Failed to remove wrong question', e);
    }
  },

  clearWrongQuestions(): void {
    if (typeof window === 'undefined') return;
    localStorage.removeItem(WRONG_STORAGE_KEY);
  },

  getProgressStats(): UserProgressStat {
    if (typeof window === 'undefined') {
      return { totalAttempted: 0, correctCount: 0, byChapter: {}, byUnit: {} };
    }
    try {
      const data = localStorage.getItem(PROGRESS_STORAGE_KEY);
      return data
        ? JSON.parse(data)
        : { totalAttempted: 0, correctCount: 0, byChapter: {}, byUnit: {} };
    } catch {
      return { totalAttempted: 0, correctCount: 0, byChapter: {}, byUnit: {} };
    }
  },

  recordAnswer(question: Question, isCorrect: boolean): void {
    if (typeof window === 'undefined') return;
    try {
      const current = this.getProgressStats();
      current.totalAttempted += 1;
      if (isCorrect) current.correctCount += 1;

      // Track by chapters
      if (question.chapters) {
        question.chapters.forEach((ch) => {
          if (!current.byChapter[ch.chapter_id]) {
            current.byChapter[ch.chapter_id] = { total: 0, correct: 0 };
          }
          current.byChapter[ch.chapter_id].total += 1;
          if (isCorrect) current.byChapter[ch.chapter_id].correct += 1;
        });
      }

      // Track by units
      if (question.units) {
        question.units.forEach((u) => {
          if (!current.byUnit[u]) {
            current.byUnit[u] = { total: 0, correct: 0 };
          }
          current.byUnit[u].total += 1;
          if (isCorrect) current.byUnit[u].correct += 1;
        });
      }

      localStorage.setItem(PROGRESS_STORAGE_KEY, JSON.stringify(current));
    } catch (e) {
      console.error('Failed to record progress', e);
    }
  },
};
