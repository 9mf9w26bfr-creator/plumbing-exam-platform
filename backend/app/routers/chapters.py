from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.app.database import get_db
from backend.app.models import TextbookChapter, QuestionChapterMapping, Question, QuestionStatus
from backend.app.schemas import TextbookChapterResponse

router = APIRouter(prefix="/api/chapters", tags=["Chapters"])


@router.get("", response_model=List[TextbookChapterResponse])
def get_chapters(db: Session = Depends(get_db)):
    chapters = db.query(TextbookChapter).order_by(TextbookChapter.id).all()
    result = []
    for ch in chapters:
        # Count published questions only for normal practice
        count = (
            db.query(func.count(Question.id))
            .join(QuestionChapterMapping, Question.id == QuestionChapterMapping.question_id)
            .filter(
                QuestionChapterMapping.chapter_id == ch.id,
                Question.status == QuestionStatus.Published
            )
            .scalar()
        )
        result.append(
            TextbookChapterResponse(
                id=ch.id,
                title=ch.title,
                sub_topics=ch.sub_topics,
                question_count=count or 0
            )
        )
    return result


@router.get("/{chapter_id}", response_model=TextbookChapterResponse)
def get_chapter(chapter_id: int, db: Session = Depends(get_db)):
    chapter = db.query(TextbookChapter).filter(TextbookChapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    count = (
        db.query(func.count(Question.id))
        .join(QuestionChapterMapping, Question.id == QuestionChapterMapping.question_id)
        .filter(
            QuestionChapterMapping.chapter_id == chapter.id,
            Question.status == QuestionStatus.Published
        )
        .scalar()
    )
    return TextbookChapterResponse(
        id=chapter.id,
        title=chapter.title,
        sub_topics=chapter.sub_topics,
        question_count=count or 0
    )
