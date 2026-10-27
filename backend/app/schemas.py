from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from backend.app.models import QuestionStatus


class SubTopicItem(BaseModel):
    id: str
    title_en: str
    title_zh: str


class TextbookChapterResponse(BaseModel):
    id: int
    title: str
    sub_topics: List[Dict[str, Any]]
    question_count: Optional[int] = 0

    class Config:
        from_attributes = True


class ExamUnitResponse(BaseModel):
    id: str
    title: str
    category: str
    question_count: Optional[int] = 0

    class Config:
        from_attributes = True


class QuestionResponse(BaseModel):
    id: str
    content_en: str
    content_zh: str
    options_en: Dict[str, str]
    options_zh: Dict[str, str]
    correct_answer: str
    explanation_en: Optional[str] = None
    explanation_zh: Optional[str] = None
    status: QuestionStatus
    source_reference: Optional[str] = None
    chapters: Optional[List[Dict[str, Any]]] = []
    units: Optional[List[str]] = []

    class Config:
        from_attributes = True


class QuestionCreate(BaseModel):
    content_en: str
    content_zh: str
    options_en: Dict[str, str]
    options_zh: Dict[str, str]
    correct_answer: str
    explanation_en: Optional[str] = None
    explanation_zh: Optional[str] = None
    status: QuestionStatus = QuestionStatus.Draft
    source_reference: Optional[str] = None
    chapter_ids: Optional[List[Dict[str, Any]]] = []  # [{"chapter_id": 3, "sub_topic_id": "3.1"}]
    unit_ids: Optional[List[str]] = []                # ["Unit_201", "Unit_202"]


class QuestionUpdate(BaseModel):
    content_en: Optional[str] = None
    content_zh: Optional[str] = None
    options_en: Optional[Dict[str, str]] = None
    options_zh: Optional[Dict[str, str]] = None
    correct_answer: Optional[str] = None
    explanation_en: Optional[str] = None
    explanation_zh: Optional[str] = None
    status: Optional[QuestionStatus] = None
    source_reference: Optional[str] = None
    chapter_ids: Optional[List[Dict[str, Any]]] = None
    unit_ids: Optional[List[str]] = None


class QuestionStatusUpdate(BaseModel):
    status: QuestionStatus
    reviewer_notes: Optional[str] = None
