export type QuestionStatus = 'Draft' | 'AI_Reviewed' | 'Technically_Verified' | 'Published';

export interface SubTopic {
  id: string;
  title_en: string;
  title_zh: string;
}

export interface TextbookChapter {
  id: number;
  title: string;
  sub_topics: SubTopic[];
  question_count?: number;
}

export interface ExamUnit {
  id: string;
  title: string;
  category: string;
  question_count?: number;
}

export interface QuestionChapterMapping {
  chapter_id: number;
  sub_topic_id: string;
}

export interface Question {
  id: string;
  content_en: string;
  content_zh: string;
  options_en: Record<string, string>;
  options_zh: Record<string, string>;
  correct_answer: string;
  explanation_en?: string;
  explanation_zh?: string;
  status: QuestionStatus;
  source_reference?: string;
  chapters?: QuestionChapterMapping[];
  units?: string[];
}

export interface QuestionCreatePayload {
  content_en: string;
  content_zh: string;
  options_en: Record<string, string>;
  options_zh: Record<string, string>;
  correct_answer: string;
  explanation_en?: string;
  explanation_zh?: string;
  status: QuestionStatus;
  source_reference?: string;
  chapter_ids?: { chapter_id: number; sub_topic_id?: string }[];
  unit_ids?: string[];
}

export type QuestionUpdatePayload = Partial<QuestionCreatePayload>;

export interface CMSStats {
  Draft: number;
  AI_Reviewed: number;
  Technically_Verified: number;
  Published: number;
  total: number;
}

export interface WrongQuestionRecord {
  question: Question;
  selected_answer: string;
  timestamp: number;
  mode: 'chapter' | 'unit' | 'mock';
  target_id: string | number;
}

export interface UserProgressStat {
  totalAttempted: number;
  correctCount: number;
  byChapter: Record<number, { total: number; correct: number }>;
  byUnit: Record<string, { total: number; correct: number }>;
}

export interface QuizSessionState {
  sessionKey: string;
  title: string;
  subtitle?: string;
  mode: 'practice' | 'mock';
  targetType: 'chapter' | 'unit' | 'mock';
  targetId: string | number;
  subTopicId?: string;
  durationMinutes?: number;
  timeLeft?: number;
  currentIndex: number;
  questions: Question[];
  selectedAnswers: Record<string, string>;
  showExplanation: Record<string, boolean>;
  flagged: Record<string, boolean>;
  updatedAt: number;
}
