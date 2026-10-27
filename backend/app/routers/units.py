from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.app.database import get_db
from backend.app.models import ExamUnit, QuestionUnitMapping, Question, QuestionStatus
from backend.app.schemas import ExamUnitResponse

router = APIRouter(prefix="/api/units", tags=["Units"])


@router.get("", response_model=List[ExamUnitResponse])
def get_units(db: Session = Depends(get_db)):
    units = db.query(ExamUnit).order_by(ExamUnit.id).all()
    result = []
    for u in units:
        count = (
            db.query(func.count(Question.id))
            .join(QuestionUnitMapping, Question.id == QuestionUnitMapping.question_id)
            .filter(
                QuestionUnitMapping.unit_id == u.id,
                Question.status == QuestionStatus.Published
            )
            .scalar()
        )
        result.append(
            ExamUnitResponse(
                id=u.id,
                title=u.title,
                category=u.category,
                question_count=count or 0
            )
        )
    return result


@router.get("/{unit_id}", response_model=ExamUnitResponse)
def get_unit(unit_id: str, db: Session = Depends(get_db)):
    unit = db.query(ExamUnit).filter(ExamUnit.id == unit_id).first()
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    count = (
        db.query(func.count(Question.id))
        .join(QuestionUnitMapping, Question.id == QuestionUnitMapping.question_id)
        .filter(
            QuestionUnitMapping.unit_id == unit.id,
            Question.status == QuestionStatus.Published
        )
        .scalar()
    )
    return ExamUnitResponse(
        id=unit.id,
        title=unit.title,
        category=unit.category,
        question_count=count or 0
    )
