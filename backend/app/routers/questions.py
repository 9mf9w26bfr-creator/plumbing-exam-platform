import random
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.models import (
    Question, QuestionChapterMapping, QuestionUnitMapping, QuestionStatus
)
from backend.app.schemas import QuestionResponse

router = APIRouter(prefix="/api/questions", tags=["Questions"])


def build_question_response(q: Question, db: Session) -> QuestionResponse:
    ch_maps = db.query(QuestionChapterMapping).filter(QuestionChapterMapping.question_id == q.id).all()
    u_maps = db.query(QuestionUnitMapping).filter(QuestionUnitMapping.question_id == q.id).all()

    chapters = [{"chapter_id": m.chapter_id, "sub_topic_id": m.sub_topic_id} for m in ch_maps]
    units = [m.unit_id for m in u_maps]

    return QuestionResponse(
        id=str(q.id),
        content_en=q.content_en,
        content_zh=q.content_zh,
        options_en=q.options_en,
        options_zh=q.options_zh,
        correct_answer=q.correct_answer,
        explanation_en=q.explanation_en,
        explanation_zh=q.explanation_zh,
        status=q.status,
        source_reference=q.source_reference,
        chapters=chapters,
        units=units
    )


@router.get("/by-chapter/{chapter_id}", response_model=List[QuestionResponse])
def get_questions_by_chapter(
    chapter_id: int,
    sub_topic_id: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Retrieve published questions for a specific textbook chapter and optional sub-topic."""
    query = (
        db.query(Question)
        .join(QuestionChapterMapping, Question.id == QuestionChapterMapping.question_id)
        .filter(
            QuestionChapterMapping.chapter_id == chapter_id,
            Question.status == QuestionStatus.Published
        )
    )

    if sub_topic_id:
        query = query.filter(QuestionChapterMapping.sub_topic_id == sub_topic_id)

    questions = query.all()
    return [build_question_response(q, db) for q in questions]


@router.get("/by-unit/{unit_id}", response_model=List[QuestionResponse])
def get_questions_by_unit(
    unit_id: str,
    db: Session = Depends(get_db)
):
    """Retrieve published questions for a specific qualification unit."""
    query = (
        db.query(Question)
        .join(QuestionUnitMapping, Question.id == QuestionUnitMapping.question_id)
        .filter(
            QuestionUnitMapping.unit_id == unit_id,
            Question.status == QuestionStatus.Published
        )
    )

    questions = query.all()
    return [build_question_response(q, db) for q in questions]


@router.get("/mock-exam", response_model=List[QuestionResponse])
def get_mock_exam(
    limit: int = Query(default=10, ge=1, le=50),
    db: Session = Depends(get_db)
):
    """Generate a timed mock exam draw from all published questions."""
    questions = db.query(Question).filter(Question.status == QuestionStatus.Published).all()
    if not questions:
        return []

    sampled = random.sample(questions, min(limit, len(questions)))
    return [build_question_response(q, db) for q in sampled]


@router.get("/{question_id}", response_model=QuestionResponse)
def get_question(question_id: str, db: Session = Depends(get_db)):
    """Retrieve a single published question by ID."""
    q = db.query(Question).filter(Question.id == question_id).first()
    if not q or q.status != QuestionStatus.Published:
        raise HTTPException(status_code=404, detail="Question not found or not published")
    return build_question_response(q, db)
