import uuid
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.app.database import get_db
from backend.app.models import (
    Question, QuestionChapterMapping, QuestionUnitMapping, QuestionStatus
)
from backend.app.schemas import QuestionResponse, QuestionCreate, QuestionUpdate, QuestionStatusUpdate
from backend.app.routers.questions import build_question_response

router = APIRouter(prefix="/api/cms", tags=["CMS Review Workflow"])


@router.get("/stats")
def get_cms_stats(db: Session = Depends(get_db)):
    """Summary of question counts per review status."""
    stats = {}
    for st in QuestionStatus:
        cnt = db.query(func.count(Question.id)).filter(Question.status == st).scalar()
        stats[st.value] = cnt or 0
    stats["total"] = sum(stats.values())
    return stats


@router.get("/questions", response_model=List[QuestionResponse])
def list_cms_questions(
    status: Optional[QuestionStatus] = None,
    keyword: Optional[str] = None,
    chapter_id: Optional[int] = None,
    unit_id: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Retrieve questions across all statuses for reviewer dashboard."""
    query = db.query(Question)

    if status:
        query = query.filter(Question.status == status)

    if keyword:
        term = f"%{keyword}%"
        query = query.filter(
            (Question.content_en.ilike(term)) |
            (Question.content_zh.ilike(term)) |
            (Question.source_reference.ilike(term))
        )

    if chapter_id:
        query = query.join(QuestionChapterMapping, Question.id == QuestionChapterMapping.question_id)\
                     .filter(QuestionChapterMapping.chapter_id == chapter_id)

    if unit_id:
        query = query.join(QuestionUnitMapping, Question.id == QuestionUnitMapping.question_id)\
                     .filter(QuestionUnitMapping.unit_id == unit_id)

    questions = query.all()
    return [build_question_response(q, db) for q in questions]


@router.get("/questions/{question_id}", response_model=QuestionResponse)
def get_cms_question(question_id: str, db: Session = Depends(get_db)):
    q = db.query(Question).filter(Question.id == question_id).first()
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    return build_question_response(q, db)


@router.post("/questions", response_model=QuestionResponse)
def create_cms_question(payload: QuestionCreate, db: Session = Depends(get_db)):
    """Create a new bilingual question entity with shared UUID (Rule C)."""
    new_id = str(uuid.uuid4())
    question = Question(
        id=new_id,
        content_en=payload.content_en,
        content_zh=payload.content_zh,
        options_en=payload.options_en,
        options_zh=payload.options_zh,
        correct_answer=payload.correct_answer,
        explanation_en=payload.explanation_en,
        explanation_zh=payload.explanation_zh,
        status=payload.status or QuestionStatus.Draft,
        source_reference=payload.source_reference
    )
    db.add(question)
    db.flush()

    if payload.chapter_ids:
        for ch in payload.chapter_ids:
            mapping = QuestionChapterMapping(
                question_id=new_id,
                chapter_id=ch["chapter_id"],
                sub_topic_id=ch.get("sub_topic_id", "")
            )
            db.add(mapping)

    if payload.unit_ids:
        for u_id in payload.unit_ids:
            mapping = QuestionUnitMapping(
                question_id=new_id,
                unit_id=u_id
            )
            db.add(mapping)

    db.commit()
    db.refresh(question)
    return build_question_response(question, db)


@router.put("/questions/{question_id}", response_model=QuestionResponse)
def update_cms_question(
    question_id: str,
    payload: QuestionUpdate,
    db: Session = Depends(get_db)
):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    if payload.content_en is not None:
        question.content_en = payload.content_en
    if payload.content_zh is not None:
        question.content_zh = payload.content_zh
    if payload.options_en is not None:
        question.options_en = payload.options_en
    if payload.options_zh is not None:
        question.options_zh = payload.options_zh
    if payload.correct_answer is not None:
        question.correct_answer = payload.correct_answer
    if payload.explanation_en is not None:
        question.explanation_en = payload.explanation_en
    if payload.explanation_zh is not None:
        question.explanation_zh = payload.explanation_zh
    if payload.status is not None:
        question.status = payload.status
    if payload.source_reference is not None:
        question.source_reference = payload.source_reference

    # Update chapter mappings if provided
    if payload.chapter_ids is not None:
        db.query(QuestionChapterMapping).filter(QuestionChapterMapping.question_id == question_id).delete()
        for ch in payload.chapter_ids:
            db.add(QuestionChapterMapping(
                question_id=question_id,
                chapter_id=ch["chapter_id"],
                sub_topic_id=ch.get("sub_topic_id", "")
            ))

    # Update unit mappings if provided
    if payload.unit_ids is not None:
        db.query(QuestionUnitMapping).filter(QuestionUnitMapping.question_id == question_id).delete()
        for u_id in payload.unit_ids:
            db.add(QuestionUnitMapping(
                question_id=question_id,
                unit_id=u_id
            ))

    db.commit()
    db.refresh(question)
    return build_question_response(question, db)


@router.post("/questions/{question_id}/status", response_model=QuestionResponse)
def advance_question_status(
    question_id: str,
    payload: QuestionStatusUpdate,
    db: Session = Depends(get_db)
):
    """Enforce review lifecycle state machine (Draft -> AI_Reviewed -> Technically_Verified -> Published)."""
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    target_status = payload.status

    # Rule 3 Validation: source_reference is mandatory for Technically_Verified and Published
    if target_status in [QuestionStatus.Technically_Verified, QuestionStatus.Published]:
        if not question.source_reference or len(question.source_reference.strip()) < 5:
            raise HTTPException(
                status_code=400,
                detail="Constitution Rule 3: Valid source_reference (e.g. BS 7671, Water Regs 1999) is required before moving to Technically Verified or Published."
            )

    question.status = target_status
    db.commit()
    db.refresh(question)
    return build_question_response(question, db)


@router.delete("/questions/{question_id}")
def delete_cms_question(question_id: str, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    db.query(QuestionChapterMapping).filter(QuestionChapterMapping.question_id == question_id).delete()
    db.query(QuestionUnitMapping).filter(QuestionUnitMapping.question_id == question_id).delete()
    db.delete(question)
    db.commit()
    return {"message": "Question deleted successfully", "id": question_id}
