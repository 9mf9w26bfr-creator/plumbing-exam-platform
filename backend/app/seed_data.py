import json
import os
import uuid
from backend.app.database import SessionLocal, engine, Base
from backend.app.models import (
    Question, TextbookChapter, ExamUnit,
    QuestionChapterMapping, QuestionUnitMapping, QuestionStatus
)


def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # Check if already seeded with at least 50 questions
        if db.query(Question).count() >= 500:
            print("Database already contains comprehensive question bank, skipping seeding.")
            return

        # If has old small data, clear to upgrade
        if db.query(Question).count() > 0:
            print("Upgrading database to comprehensive 550-question bank...")
            db.query(QuestionChapterMapping).delete()
            db.query(QuestionUnitMapping).delete()
            db.query(Question).delete()
            db.query(TextbookChapter).delete()
            db.query(ExamUnit).delete()
            db.commit()

        print("Seeding textbook chapters...")
        chapters_data = [
            {"id": 1, "title": "Health and safety practices and systems", "sub_topics": [{"id": "1.1", "title_en": "Health and safety legislation & regulations", "title_zh": "健康与安全法规与条例"}, {"id": "1.2", "title_en": "Personal protective equipment (PPE)", "title_zh": "个人防护装备 (PPE)"}, {"id": "1.3", "title_en": "Safe working at height & ladders", "title_zh": "高空作业安全与梯子规范"}, {"id": "1.4", "title_en": "Hazard identification and risk assessment", "title_zh": "危险源识别与风险评估"}]},
            {"id": 2, "title": "Common processes and techniques", "sub_topics": [{"id": "2.1", "title_en": "Hand and power tools safety and maintenance", "title_zh": "手动与电动工具安全及维护"}, {"id": "2.2", "title_en": "Pipe jointing techniques (soldering, compression)", "title_zh": "管道连接技术 (焊接、卡压)"}, {"id": "2.3", "title_en": "Pipe bending and clipping", "title_zh": "管道弯曲与管卡固定"}]},
            {"id": 3, "title": "Scientific principles", "sub_topics": [{"id": "3.1", "title_en": "Units of measurement (SI Units)", "title_zh": "国际单位制与测量单位"}, {"id": "3.2", "title_en": "Properties of water & state changes", "title_zh": "水的物理性质与状态改变"}, {"id": "3.3", "title_en": "Pressure and head calculation", "title_zh": "水压与水头计算"}, {"id": "3.4", "title_en": "Heat transfer (conduction, convection, radiation)", "title_zh": "热传递原理 (传导、对流、辐射)"}]},
            {"id": 4, "title": "Planning and supervision", "sub_topics": [{"id": "4.1", "title_en": "Material estimating and ordering", "title_zh": "材料预估与采购"}, {"id": "4.2", "title_en": "Liaison with other building trades", "title_zh": "与其他建筑工种的协同沟通"}]},
            {"id": 5, "title": "Cold water systems", "sub_topics": [{"id": "5.1", "title_en": "Direct and indirect cold water supply", "title_zh": "直接式与间接式冷水供水系统"}, {"id": "5.2", "title_en": "Cold water storage cisterns (CWSC)", "title_zh": "冷水储水箱规格与安装"}, {"id": "5.3", "title_en": "Water regulations and backflow prevention", "title_zh": "水事法规与防回流污染等级 (Fluid Categories)"}]},
            {"id": 6, "title": "Hot water systems", "sub_topics": [{"id": "6.1", "title_en": "Vented hot water storage systems", "title_zh": "开式(通风型)热水储水系统"}, {"id": "6.2", "title_en": "Unvented hot water storage & safety controls", "title_zh": "闭式(承压型)热水储水系统与三级安全保护"}, {"id": "6.3", "title_en": "Legionella prevention and TMV regulation", "title_zh": "军团菌防治与恒温混水阀 (TMV) 控制"}]},
            {"id": 7, "title": "Central heating systems", "sub_topics": [{"id": "7.1", "title_en": "Heat emitters and pipe sizing", "title_zh": "散热器类型与管径计算"}, {"id": "7.2", "title_en": "System controls (S-Plan, Y-Plan, TRVs)", "title_zh": "供暖控制系统 (S-Plan, Y-Plan, 恒温阀)"}]},
            {"id": 8, "title": "Rainwater systems", "sub_topics": [{"id": "8.1", "title_en": "Gutters and downpipes sizing", "title_zh": "天沟与落水管尺寸规划"}, {"id": "8.2", "title_en": "Rainwater harvesting principles", "title_zh": "雨水收集利用基本原理"}]},
            {"id": 9, "title": "Sanitation systems", "sub_topics": [{"id": "9.1", "title_en": "Sanitary appliances installation", "title_zh": "卫生器具安装要求与间距"}, {"id": "9.2", "title_en": "Discharge stack systems and trap seal loss", "title_zh": "排水立管系统与存水弯水封防破坏"}]},
            {"id": 10, "title": "Domestic fuel systems", "sub_topics": [{"id": "10.1", "title_en": "Fuel storage and supply guidelines", "title_zh": "燃料储存与输送指引"}, {"id": "10.2", "title_en": "Combustion and ventilation requirements", "title_zh": "燃烧与通风要求"}]},
            {"id": 11, "title": "Electrical principles and processes for building services engineering", "sub_topics": [{"id": "11.1", "title_en": "Basic electrical safety and safe isolation", "title_zh": "电气安全基础与安全隔离五步法"}, {"id": "11.2", "title_en": "Bathroom zoning (Zone 0, 1, 2) and IP ratings", "title_zh": "浴室电气分区 (Zone 0, 1, 2) 与 IP 防护等级"}, {"id": "11.3", "title_en": "Equipotential bonding and earthing", "title_zh": "等电位联结与接地保护"}]}
        ]

        for ch in chapters_data:
            db.add(TextbookChapter(id=ch["id"], title=ch["title"], sub_topics=ch["sub_topics"]))

        print("Seeding qualification exam units...")
        units_data = [
            {"id": "Unit_201", "title": "Health & Safety", "category": "Core"},
            {"id": "Unit_202", "title": "Scientific Principles", "category": "Core"},
            {"id": "Unit_203", "title": "Common Plumbing Processes", "category": "Core"},
            {"id": "Unit_204", "title": "Cold Water Systems", "category": "Technical"},
            {"id": "Unit_205", "title": "Hot Water Systems", "category": "Technical"},
            {"id": "Unit_206", "title": "Sanitation & Drainage", "category": "Technical"},
            {"id": "Unit_207", "title": "Central Heating Systems", "category": "Technical"},
            {"id": "Unit_208", "title": "Electrical Principles", "category": "Technical"},
            {"id": "Unit_209", "title": "Communication / Planning", "category": "Professional"},
            {"id": "Unit_ENV", "title": "Environmental Revision", "category": "Environmental Revision"}
        ]

        for u in units_data:
            db.add(ExamUnit(id=u["id"], title=u["title"], category=u["category"]))

        db.flush()

        # Load 550 questions from questions_bank.json
        bank_path = os.path.join(os.path.dirname(__file__), "data", "questions_bank.json")
        if os.path.exists(bank_path):
            with open(bank_path, "r", encoding="utf-8") as f:
                questions_data = json.load(f)
        else:
            questions_data = []

        print(f"Seeding {len(questions_data)} comprehensive scenario questions...")

        for q_item in questions_data:
            q = Question(
                id=q_item["id"],
                content_en=q_item["content_en"],
                content_zh=q_item["content_zh"],
                options_en=q_item["options_en"],
                options_zh=q_item["options_zh"],
                correct_answer=q_item["correct_answer"],
                explanation_en=q_item.get("explanation_en"),
                explanation_zh=q_item.get("explanation_zh"),
                status=QuestionStatus.Published if q_item.get("status") == "Published" else QuestionStatus.Draft,
                source_reference=q_item.get("source_reference")
            )
            db.add(q)
            db.flush()

            # Chapter mappings
            for ch in q_item.get("chapters", []):
                db.add(QuestionChapterMapping(
                    question_id=q.id,
                    chapter_id=ch["chapter_id"],
                    sub_topic_id=ch.get("sub_topic_id", "")
                ))

            # Unit mappings
            for u_id in q_item.get("units", []):
                db.add(QuestionUnitMapping(
                    question_id=q.id,
                    unit_id=u_id
                ))

        db.commit()
        print(f"Successfully seeded database with {len(questions_data)} questions.")
    except Exception as e:
        db.rollback()
        print(f"Seeding error: {e}")
        raise e
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
