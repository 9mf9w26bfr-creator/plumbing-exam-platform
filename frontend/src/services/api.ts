import {
  TextbookChapter,
  ExamUnit,
  Question,
  CMSStats,
  QuestionCreatePayload,
  QuestionUpdatePayload,
  QuestionStatus,
} from '../types';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || '/api';

export const api = {
  // Chapters
  async getChapters(): Promise<TextbookChapter[]> {
    const res = await fetch(`${API_BASE}/chapters`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch chapters');
    return res.json();
  },

  async getChapter(id: number): Promise<TextbookChapter> {
    const res = await fetch(`${API_BASE}/chapters/${id}`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch chapter');
    return res.json();
  },

  // Units
  async getUnits(): Promise<ExamUnit[]> {
    const res = await fetch(`${API_BASE}/units`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch units');
    return res.json();
  },

  async getUnit(id: string): Promise<ExamUnit> {
    const res = await fetch(`${API_BASE}/units/${id}`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch unit');
    return res.json();
  },

  // Questions for learners (strictly Published)
  async getQuestionsByChapter(chapterId: number, subTopicId?: string): Promise<Question[]> {
    let url = `${API_BASE}/questions/by-chapter/${chapterId}`;
    if (subTopicId) url += `?sub_topic_id=${encodeURIComponent(subTopicId)}`;
    const res = await fetch(url, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch chapter questions');
    return res.json();
  },

  async getQuestionsByUnit(unitId: string): Promise<Question[]> {
    const res = await fetch(`${API_BASE}/questions/by-unit/${encodeURIComponent(unitId)}`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch unit questions');
    return res.json();
  },

  async getMockExam(limit: number = 10): Promise<Question[]> {
    const res = await fetch(`${API_BASE}/questions/mock-exam?limit=${limit}`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch mock exam');
    return res.json();
  },

  async getQuestion(id: string): Promise<Question> {
    const res = await fetch(`${API_BASE}/questions/${id}`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch question');
    return res.json();
  },

  // CMS Endpoints
  async getCMSStats(): Promise<CMSStats> {
    const res = await fetch(`${API_BASE}/cms/stats`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch CMS stats');
    return res.json();
  },

  async getCMSQuestions(params?: {
    status?: QuestionStatus;
    keyword?: string;
    chapter_id?: number;
    unit_id?: string;
  }): Promise<Question[]> {
    const query = new URLSearchParams();
    if (params?.status) query.append('status', params.status);
    if (params?.keyword) query.append('keyword', params.keyword);
    if (params?.chapter_id) query.append('chapter_id', String(params.chapter_id));
    if (params?.unit_id) query.append('unit_id', params.unit_id);

    const res = await fetch(`${API_BASE}/cms/questions?${query.toString()}`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch CMS questions');
    return res.json();
  },

  async createQuestion(payload: QuestionCreatePayload): Promise<Question> {
    const res = await fetch(`${API_BASE}/cms/questions`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.detail || 'Failed to create question');
    }
    return res.json();
  },

  async updateQuestion(id: string, payload: QuestionUpdatePayload): Promise<Question> {
    const res = await fetch(`${API_BASE}/cms/questions/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.detail || 'Failed to update question');
    }
    return res.json();
  },

  async updateQuestionStatus(id: string, status: QuestionStatus): Promise<Question> {
    const res = await fetch(`${API_BASE}/cms/questions/${id}/status`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status }),
    });
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.detail || 'Failed to change question status');
    }
    return res.json();
  },

  async deleteQuestion(id: string): Promise<void> {
    const res = await fetch(`${API_BASE}/cms/questions/${id}`, {
      method: 'DELETE',
    });
    if (!res.ok) throw new Error('Failed to delete question');
  },
};
