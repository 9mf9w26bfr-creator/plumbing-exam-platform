import {
  TextbookChapter,
  ExamUnit,
  Question,
  CMSStats,
  QuestionCreatePayload,
  QuestionUpdatePayload,
  QuestionStatus,
} from '../types';

const rawEnvUrl = (process.env.NEXT_PUBLIC_API_URL || '').trim();
// Ignore placeholder URLs
const isPlaceholder =
  !rawEnvUrl ||
  rawEnvUrl.includes('your-backend-api') ||
  rawEnvUrl.includes('your-api-domain') ||
  rawEnvUrl === 'http://localhost:8000/api';

const PRIMARY_API_BASE = isPlaceholder ? '/api' : rawEnvUrl;

async function requestWithFallback(path: string, options?: RequestInit): Promise<Response> {
  const primaryUrl = `${PRIMARY_API_BASE}${path}`;
  try {
    const res = await fetch(primaryUrl, options);
    if (res.ok) return res;
    // If primary returned error and primary is not /api, fallback to built-in serverless /api
    if (PRIMARY_API_BASE !== '/api') {
      const fallbackRes = await fetch(`/api${path}`, options);
      if (fallbackRes.ok) return fallbackRes;
    }
    return res;
  } catch {
    // If network failed on primary (e.g. DNS failure on placeholder), fallback to /api
    if (PRIMARY_API_BASE !== '/api') {
      return await fetch(`/api${path}`, options);
    }
    throw new Error('Network error: failed to fetch');
  }
}

export const api = {
  // Chapters
  async getChapters(): Promise<TextbookChapter[]> {
    const res = await requestWithFallback('/chapters', { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch chapters');
    return res.json();
  },

  async getChapter(id: number): Promise<TextbookChapter> {
    const res = await requestWithFallback(`/chapters/${id}`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch chapter');
    return res.json();
  },

  // Units
  async getUnits(): Promise<ExamUnit[]> {
    const res = await requestWithFallback('/units', { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch units');
    return res.json();
  },

  async getUnit(id: string): Promise<ExamUnit> {
    const res = await requestWithFallback(`/units/${id}`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch unit');
    return res.json();
  },

  // Questions for learners (strictly Published)
  async getQuestionsByChapter(chapterId: number, subTopicId?: string): Promise<Question[]> {
    let path = `/questions/by-chapter/${chapterId}`;
    if (subTopicId) path += `?sub_topic_id=${encodeURIComponent(subTopicId)}`;
    const res = await requestWithFallback(path, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch chapter questions');
    return res.json();
  },

  async getQuestionsByUnit(unitId: string): Promise<Question[]> {
    const res = await requestWithFallback(`/questions/by-unit/${encodeURIComponent(unitId)}`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch unit questions');
    return res.json();
  },

  async getMockExam(limit: number = 10, unitId?: string): Promise<Question[]> {
    let path = `/questions/mock-exam?limit=${limit}`;
    if (unitId && unitId !== 'all') {
      path += `&unit_id=${encodeURIComponent(unitId)}`;
    }
    const res = await requestWithFallback(path, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch mock exam');
    return res.json();
  },

  async getQuestion(id: string): Promise<Question> {
    const res = await requestWithFallback(`/questions/${id}`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch question');
    return res.json();
  },

  // CMS Endpoints
  async getCMSStats(): Promise<CMSStats> {
    const res = await requestWithFallback('/cms/stats', { cache: 'no-store' });
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

    const path = `/cms/questions?${query.toString()}`;
    const res = await requestWithFallback(path, { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to fetch CMS questions');
    return res.json();
  },

  async createQuestion(payload: QuestionCreatePayload): Promise<Question> {
    const res = await requestWithFallback('/cms/questions', {
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
    const res = await requestWithFallback(`/cms/questions/${id}`, {
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
    const res = await requestWithFallback(`/cms/questions/${id}/status`, {
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
    const res = await requestWithFallback(`/cms/questions/${id}`, {
      method: 'DELETE',
    });
    if (!res.ok) throw new Error('Failed to delete question');
  },
};
