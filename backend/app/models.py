import uuid
from enum import Enum as PyEnum
from sqlalchemy import Column, String, Text, Integer, JSON, Enum, ForeignKey
from sqlalchemy.types import TypeDecorator, CHAR
from backend.app.database import Base


class GUID(TypeDecorator):
    """Platform-independent GUID/UUID type.
    Uses PostgreSQL's UUID type, otherwise uses CHAR(36), storing as stringified hex values.
    """
    impl = CHAR(36)
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == "postgresql":
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return str(uuid.UUID(str(value)))
            return str(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        return str(value)


class QuestionStatus(str, PyEnum):
    Draft = "Draft"
    AI_Reviewed = "AI_Reviewed"
    Technically_Verified = "Technically_Verified"
    Published = "Published"


class Question(Base):
    __tablename__ = "questions"

    id = Column(GUID(), primary_key=True, default=lambda: str(uuid.uuid4()))
    content_en = Column(Text, nullable=False)
    content_zh = Column(Text, nullable=False)
    options_en = Column(JSON, nullable=False)
    options_zh = Column(JSON, nullable=False)
    correct_answer = Column(String(10), nullable=False)
    explanation_en = Column(Text, nullable=True)
    explanation_zh = Column(Text, nullable=True)
    status = Column(Enum(QuestionStatus), default=QuestionStatus.Draft, nullable=False)
    source_reference = Column(String(500), nullable=True)


class TextbookChapter(Base):
    __tablename__ = "textbook_chapters"

    id = Column(Integer, primary_key=True, autoincrement=False)
    title = Column(String(255), nullable=False)
    sub_topics = Column(JSON, nullable=False)


class ExamUnit(Base):
    __tablename__ = "exam_units"

    id = Column(String(100), primary_key=True)
    title = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)


class QuestionChapterMapping(Base):
    __tablename__ = "question_chapter_mapping"

    # Composite primary key or foreign key mapping
    question_id = Column(GUID(), ForeignKey("questions.id", ondelete="CASCADE"), primary_key=True)
    chapter_id = Column(Integer, ForeignKey("textbook_chapters.id", ondelete="CASCADE"), primary_key=True)
    sub_topic_id = Column(String(100), primary_key=True)


class QuestionUnitMapping(Base):
    __tablename__ = "question_unit_mapping"

    question_id = Column(GUID(), ForeignKey("questions.id", ondelete="CASCADE"), primary_key=True)
    unit_id = Column(String(100), ForeignKey("exam_units.id", ondelete="CASCADE"), primary_key=True)
