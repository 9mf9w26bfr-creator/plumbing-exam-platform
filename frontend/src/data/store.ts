import { initialChapters, initialUnits, initialQuestions } from './seedData';
import { TextbookChapter, ExamUnit, Question, QuestionStatus, QuestionCreatePayload } from '../types';

const chapters: TextbookChapter[] = [...initialChapters];
const units: ExamUnit[] = [...initialUnits];
let questions: Question[] = [...initialQuestions];

export const dataStore = {
  getChapters() {
    return chapters.map((ch) => ({
      ...ch,
      question_count: questions.filter(
        (q) =>
          q.status === 'Published' &&
          q.chapters?.some((c) => c.chapter_id === ch.id)
      ).length,
    }));
  },

  getUnits() {
    return units.map((u) => ({
      ...u,
      question_count: questions.filter(
        (q) => q.status === 'Published' && q.units?.includes(u.id)
      ).length,
    }));
  },

  getQuestionsByChapter(chapterId: number, subTopicId?: string | null) {
    return questions.filter((q) => {
      if (q.status !== 'Published') return false;
      const match = q.chapters?.find((c) => c.chapter_id === chapterId);
      if (!match) return false;
      if (subTopicId) {
        return match.sub_topic_id === subTopicId;
      }
      return true;
    });
  },

  getQuestionsByUnit(unitId: string) {
    return questions.filter(
      (q) => q.status === 'Published' && q.units?.includes(unitId)
    );
  },

  getMockExam(limit: number = 10, unitId?: string | null) {
    let published = questions.filter((q) => q.status === 'Published');
    if (unitId && unitId !== 'all') {
      published = published.filter((q) => q.units?.includes(unitId));
    }
    const shuffled = [...published].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, Math.min(limit, published.length));
  },

  getCMSStats() {
    const stats: Record<string, number> = {
      Draft: 0,
      AI_Reviewed: 0,
      Technically_Verified: 0,
      Published: 0,
      total: questions.length,
    };
    questions.forEach((q) => {
      if (stats[q.status] !== undefined) {
        stats[q.status] += 1;
      }
    });
    return stats;
  },

  getCMSQuestions(filters?: {
    status?: QuestionStatus;
    keyword?: string;
    chapter_id?: number;
    unit_id?: string;
  }) {
    return questions.filter((q) => {
      if (filters?.status && q.status !== filters.status) return false;
      if (filters?.chapter_id) {
        if (!q.chapters?.some((c) => c.chapter_id === filters.chapter_id))
          return false;
      }
      if (filters?.unit_id) {
        if (!q.units?.includes(filters.unit_id)) return false;
      }
      if (filters?.keyword) {
        const kw = filters.keyword.toLowerCase();
        const en = q.content_en.toLowerCase();
        const zh = q.content_zh.toLowerCase();
        const ref = (q.source_reference || '').toLowerCase();
        if (!en.includes(kw) && !zh.includes(kw) && !ref.includes(kw)) {
          return false;
        }
      }
      return true;
    });
  },

  createQuestion(payload: QuestionCreatePayload) {
    const id = `q-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
    const newQ: Question = {
      id,
      content_en: payload.content_en,
      content_zh: payload.content_zh,
      options_en: payload.options_en,
      options_zh: payload.options_zh,
      correct_answer: payload.correct_answer,
      explanation_en: payload.explanation_en,
      explanation_zh: payload.explanation_zh,
      status: payload.status || 'Draft',
      source_reference: payload.source_reference,
      chapters: (payload.chapter_ids || []).map((c) => ({
        chapter_id: c.chapter_id,
        sub_topic_id: c.sub_topic_id || '',
      })),
      units: payload.unit_ids || [],
    };
    questions.unshift(newQ);
    return newQ;
  },

  updateQuestionStatus(id: string, status: QuestionStatus) {
    const q = questions.find((item) => item.id === id);
    if (!q) throw new Error('Question not found');
    if (
      (status === 'Technically_Verified' || status === 'Published') &&
      (!q.source_reference || q.source_reference.trim().length < 5)
    ) {
      throw new Error(
        'Constitution Rule 3: Valid source_reference is required before advancing to Technically Verified or Published.'
      );
    }
    q.status = status;
    return q;
  },

  deleteQuestion(id: string) {
    questions = questions.filter((item) => item.id !== id);
    return { success: true, id };
  },
};
