import { Question, WrongQuestionRecord, UserProgressStat, QuizSessionState } from '../types';

const WRONG_STORAGE_KEY = 'plumbing_exam_wrong_questions';
const PROGRESS_STORAGE_KEY = 'plumbing_exam_progress_stats';
const SESSION_PREFIX = 'plumbing_exam_session_';
const LAST_SESSION_KEY = 'plumbing_exam_last_session_key';

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

  // Active Quiz Session Persistence (for reload, disconnect, and exit recovery)
  saveQuizSession(session: QuizSessionState): void {
    if (typeof window === 'undefined') return;
    try {
      session.updatedAt = Date.now();
      const key = `${SESSION_PREFIX}${session.sessionKey}`;
      localStorage.setItem(key, JSON.stringify(session));
      localStorage.setItem(LAST_SESSION_KEY, session.sessionKey);
    } catch (e) {
      console.error('Failed to save quiz session', e);
    }
  },

  getQuizSession(sessionKey: string): QuizSessionState | null {
    if (typeof window === 'undefined') return null;
    try {
      const key = `${SESSION_PREFIX}${sessionKey}`;
      const data = localStorage.getItem(key);
      return data ? JSON.parse(data) : null;
    } catch {
      return null;
    }
  },

  getLastActiveSession(): QuizSessionState | null {
    if (typeof window === 'undefined') return null;
    try {
      const lastKey = localStorage.getItem(LAST_SESSION_KEY);
      if (!lastKey) return null;
      const session = this.getQuizSession(lastKey);
      if (!session) return null;
      // Discard if older than 14 days
      if (Date.now() - session.updatedAt > 14 * 24 * 60 * 60 * 1000) {
        this.clearQuizSession(lastKey);
        return null;
      }
      return session;
    } catch {
      return null;
    }
  },

  getAllActiveSessions(): Record<string, QuizSessionState> {
    if (typeof window === 'undefined') return {};
    const result: Record<string, QuizSessionState> = {};
    try {
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.startsWith(SESSION_PREFIX)) {
          const raw = localStorage.getItem(k);
          if (raw) {
            try {
              const session: QuizSessionState = JSON.parse(raw);
              if (session && session.sessionKey) {
                result[session.sessionKey] = session;
              }
            } catch {
              // ignore invalid entry
            }
          }
        }
      }
    } catch {
      // ignore
    }
    return result;
  },

  clearQuizSession(sessionKey: string): void {
    if (typeof window === 'undefined') return;
    try {
      const key = `${SESSION_PREFIX}${sessionKey}`;
      localStorage.removeItem(key);
      const lastKey = localStorage.getItem(LAST_SESSION_KEY);
      if (lastKey === sessionKey) {
        localStorage.removeItem(LAST_SESSION_KEY);
      }
    } catch (e) {
      console.error('Failed to clear quiz session', e);
    }
  },
};
