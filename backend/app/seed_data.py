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
        # Check if already seeded
        if db.query(TextbookChapter).count() > 0:
            print("Database already contains data, skipping seeding.")
            return

        print("Seeding textbook chapters...")
        # 11 Textbook Chapters according to TEXTBOOK_CONTENTS.md
        chapters_data = [
            {
                "id": 1,
                "title": "Health and safety practices and systems",
                "sub_topics": [
                    {"id": "1.1", "title_en": "Health and safety legislation & regulations", "title_zh": "健康与安全法规与条例"},
                    {"id": "1.2", "title_en": "Personal protective equipment (PPE)", "title_zh": "个人防护装备 (PPE)"},
                    {"id": "1.3", "title_en": "Safe working at height & ladders", "title_zh": "高空作业安全与梯子规范"},
                    {"id": "1.4", "title_en": "Hazard identification and risk assessment", "title_zh": "危险源识别与风险评估"}
                ]
            },
            {
                "id": 2,
                "title": "Common processes and techniques",
                "sub_topics": [
                    {"id": "2.1", "title_en": "Hand and power tools safety and maintenance", "title_zh": "手动与电动工具安全及维护"},
                    {"id": "2.2", "title_en": "Pipe jointing techniques (soldering, compression)", "title_zh": "管道连接技术 (焊接、卡压)"},
                    {"id": "2.3", "title_en": "Pipe bending and clipping", "title_zh": "管道弯曲与管卡固定"}
                ]
            },
            {
                "id": 3,
                "title": "Scientific principles",
                "sub_topics": [
                    {"id": "3.1", "title_en": "Units of measurement (SI Units)", "title_zh": "国际单位制与测量单位"},
                    {"id": "3.2", "title_en": "Properties of water & state changes", "title_zh": "水的物理性质与状态改变"},
                    {"id": "3.3", "title_en": "Pressure and head calculation", "title_zh": "水压与水头计算"},
                    {"id": "3.4", "title_en": "Heat transfer (conduction, convection, radiation)", "title_zh": "热传递原理 (传导、对流、辐射)"}
                ]
            },
            {
                "id": 4,
                "title": "Planning and supervision",
                "sub_topics": [
                    {"id": "4.1", "title_en": "Material estimating and ordering", "title_zh": "材料预估与采购"},
                    {"id": "4.2", "title_en": "Liaison with other building trades", "title_zh": "与其他建筑工种的协同沟通"}
                ]
            },
            {
                "id": 5,
                "title": "Cold water systems",
                "sub_topics": [
                    {"id": "5.1", "title_en": "Direct and indirect cold water supply", "title_zh": "直接式与间接式冷水供水系统"},
                    {"id": "5.2", "title_en": "Cold water storage cisterns (CWSC)", "title_zh": "冷水储水箱规格与安装"},
                    {"id": "5.3", "title_en": "Water regulations and backflow prevention", "title_zh": "水事法规与防回流污染等级 (Fluid Categories)"}
                ]
            },
            {
                "id": 6,
                "title": "Hot water systems",
                "sub_topics": [
                    {"id": "6.1", "title_en": "Vented hot water storage systems", "title_zh": "开式(通风型)热水储水系统"},
                    {"id": "6.2", "title_en": "Unvented hot water storage & safety controls", "title_zh": "闭式(承压型)热水储水系统与三级安全保护"},
                    {"id": "6.3", "title_en": "Legionella prevention and TMV regulation", "title_zh": "军团菌防治与恒温混水阀 (TMV) 控制"}
                ]
            },
            {
                "id": 7,
                "title": "Central heating systems",
                "sub_topics": [
                    {"id": "7.1", "title_en": "Heat emitters and pipe sizing", "title_zh": "散热器类型与管径计算"},
                    {"id": "7.2", "title_en": "System controls (S-Plan, Y-Plan, TRVs)", "title_zh": "供暖控制系统 (S-Plan, Y-Plan, 恒温阀)"}
                ]
            },
            {
                "id": 8,
                "title": "Rainwater systems",
                "sub_topics": [
                    {"id": "8.1", "title_en": "Gutters and downpipes sizing", "title_zh": "天沟与落水管尺寸规划"},
                    {"id": "8.2", "title_en": "Rainwater harvesting principles", "title_zh": "雨水收集利用基本原理"}
                ]
            },
            {
                "id": 9,
                "title": "Sanitation systems",
                "sub_topics": [
                    {"id": "9.1", "title_en": "Sanitary appliances installation", "title_zh": "卫生器具安装要求与间距"},
                    {"id": "9.2", "title_en": "Discharge stack systems and trap seal loss", "title_zh": "排水立管系统与存水弯水封防破坏"}
                ]
            },
            {
                "id": 10,
                "title": "Domestic fuel systems",
                "sub_topics": [
                    {"id": "10.1", "title_en": "Fuel storage and supply guidelines", "title_zh": "燃料储存与输送指引"},
                    {"id": "10.2", "title_en": "Combustion and ventilation requirements", "title_zh": "燃烧与通风要求"}
                ]
            },
            {
                "id": 11,
                "title": "Electrical principles and processes for building services engineering",
                "sub_topics": [
                    {"id": "11.1", "title_en": "Basic electrical safety and safe isolation", "title_zh": "电气安全基础与安全隔离五步法"},
                    {"id": "11.2", "title_en": "Bathroom zoning (Zone 0, 1, 2) and IP ratings", "title_zh": "浴室电气分区 (Zone 0, 1, 2) 与 IP 防护等级"},
                    {"id": "11.3", "title_en": "Equipotential bonding and earthing", "title_zh": "等电位联结与接地保护"}
                ]
            }
        ]

        for ch in chapters_data:
            chapter = TextbookChapter(
                id=ch["id"],
                title=ch["title"],
                sub_topics=ch["sub_topics"]
            )
            db.add(chapter)

        print("Seeding qualification exam units...")
        # 10 Qualification Units based on QUALIFICATION_MAPPING.md
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
            unit = ExamUnit(
                id=u["id"],
                title=u["title"],
                category=u["category"]
            )
            db.add(unit)

        db.flush()

        print("Seeding realistic scenario-based bilingual C&G questions...")
        # Strictly complying with Rule C (single question entity, shared UUID, simultaneous EN and ZH insertion)
        # Questions with various statuses: Published, Technically_Verified, AI_Reviewed, Draft
        questions_data = [
            {
                "id": str(uuid.uuid4()),
                "content_en": "A plumbing engineer is testing water pressure at the base of a 15-meter tall commercial building. The cold water storage cistern is situated at roof level. Neglecting pipe friction, what is the static pressure at the lowest outlet?",
                "content_zh": "一名水暖工程师正在一栋15米高的商业建筑底部测试水压。冷水储水箱设在屋顶。在忽略管壁摩擦的情况下，最低出水点处的静态水压是多少？",
                "options_en": {
                    "A": "0.15 bar (15 kPa)",
                    "B": "1.5 bar (150 kPa)",
                    "C": "15.0 bar (1500 kPa)",
                    "D": "0.5 bar (50 kPa)"
                },
                "options_zh": {
                    "A": "0.15 bar (15 kPa)",
                    "B": "1.5 bar (150 kPa)",
                    "C": "15.0 bar (1500 kPa)",
                    "D": "0.5 bar (50 kPa)"
                },
                "correct_answer": "B",
                "explanation_en": "Static water pressure equals 1 metre head = 0.1 bar (approx 9.81 kPa, commonly rounded to 10 kPa in C&G level 2 exams). Therefore, 15 m static head = 15 x 0.1 bar = 1.5 bar (150 kPa).",
                "explanation_zh": "静态水压换算规则为：1米水头约产生 0.1 bar (约 10 kPa) 的压力。因此，15米静态水头产生的压力为 15 × 0.1 bar = 1.5 bar (150 kPa)。",
                "status": QuestionStatus.Published,
                "source_reference": "C&G 6035 Unit 202; Textbook Chapter 3 Scientific Principles (p. 112)",
                "chapter_mapping": {"chapter_id": 3, "sub_topic_id": "3.3"},
                "unit_mappings": ["Unit_202", "Unit_204"]
            },
            {
                "id": str(uuid.uuid4()),
                "content_en": "Under The Water Supply (Water Fittings) Regulations 1999, what fluid category describes water that represents a serious health hazard due to the presence of pathogens or toxic chemicals, such as in bidets with flexible spray hoses below the spillover level?",
                "content_zh": "根据《1999年供水（水配件）条例》，哪一个流体风险等级（Fluid Category）定义了因存在病原体或有毒化学物质而对人体健康构成严重危害的水质（例如喷头低于溢流边缘的妇洗器软管）？",
                "options_en": {
                    "A": "Fluid Category 2",
                    "B": "Fluid Category 3",
                    "C": "Fluid Category 4",
                    "D": "Fluid Category 5"
                },
                "options_zh": {
                    "A": "流体类别 2 (Fluid Category 2)",
                    "B": "流体类别 3 (Fluid Category 3)",
                    "C": "流体类别 4 (Fluid Category 4)",
                    "D": "流体类别 5 (Fluid Category 5)"
                },
                "correct_answer": "D",
                "explanation_en": "Fluid Category 5 represents a serious health hazard because of the concentration of pathogenic organisms or radioactive or very toxic substances. A Type AB or AA air gap is mandatory.",
                "explanation_zh": "流体类别 5 代表因含有高致病微生物、放射性物质或剧毒物质而对人体健康构成严重危害的等级。此类风险必须使用物理空气隔断（如 Type AA 或 Type AB 空气间隙）防回流。",
                "status": QuestionStatus.Published,
                "source_reference": "The Water Supply (Water Fittings) Regulations 1999, Schedule 1 & BS EN 1717",
                "chapter_mapping": {"chapter_id": 5, "sub_topic_id": "5.3"},
                "unit_mappings": ["Unit_204"]
            },
            {
                "id": str(uuid.uuid4()),
                "content_en": "According to BS 7671 (Requirements for Electrical Installations), what is the minimum IP rating required for electrical equipment installed inside Zone 1 of a room containing a bath or shower basin where water jets are not likely?",
                "content_zh": "根据 BS 7671 电气安装规范，在包含浴缸或淋浴的浴室 Zone 1 区域内，如果不太可能受到喷水冲击，安装的电气设备所要求的最低 IP 防水防护等级是多少？",
                "options_en": {
                    "A": "IPX0",
                    "B": "IPX2",
                    "C": "IPX4",
                    "D": "IPX7"
                },
                "options_zh": {
                    "A": "IPX0 (无防水)",
                    "B": "IPX2 (防滴水)",
                    "C": "IPX4 (防溅水)",
                    "D": "IPX7 (防短时间浸水)"
                },
                "correct_answer": "C",
                "explanation_en": "BS 7671 Section 701 dictates that equipment installed in Zone 1 must have a minimum degree of protection of IPX4 (or IPX5 if water jets are likely for cleaning). Zone 0 requires IPX7.",
                "explanation_zh": "BS 7671 第 701 节规定，在浴室 Zone 1 区域安装的电气设备必须至少具备 IPX4（防溅水）防护等级；若可能存在清洁喷水，则须达到 IPX5。Zone 0 区域要求达到 IPX7。",
                "status": QuestionStatus.Published,
                "source_reference": "BS 7671:2018+A2:2022 Section 701; C&G Unit 208",
                "chapter_mapping": {"chapter_id": 11, "sub_topic_id": "11.2"},
                "unit_mappings": ["Unit_208", "Unit_204"]
            },
            {
                "id": str(uuid.uuid4()),
                "content_en": "An apprentice is using an unvented hot water cylinder. What temperature does the temperature and pressure relief valve (T&P valve) typically open at to prevent catastrophic explosion if all electrical thermostats fail?",
                "content_zh": "一名学徒正在调试一套闭式（承压型）热水储水缸。当所有电气温控器均失效时，温度与压力安全阀（T&P Valve）通常在什么温度下自动开启，以防止储水缸发生灾难性超温爆炸？",
                "options_en": {
                    "A": "60°C to 65°C",
                    "B": "75°C to 80°C",
                    "C": "90°C to 95°C",
                    "D": "120°C to 125°C"
                },
                "options_zh": {
                    "A": "60°C 至 65°C",
                    "B": "75°C 至 80°C",
                    "C": "90°C 至 95°C",
                    "D": "120°C 至 125°C"
                },
                "correct_answer": "C",
                "explanation_en": "Building Regulations Approved Document G3 specifies three levels of safety for unvented hot water cylinders. The final mechanical relief device (T&P valve) operates at 90-95°C (and typically 10 bar pressure) to discharge expanding water safely via a tundish.",
                "explanation_zh": "英国建筑规范 Approved Document G3 对闭式热水缸规定了三级安全防护。最终机械安全泄压装置（T&P 阀）设定在 90°C-95°C（且通常伴随 10 bar 压力限制）开启，通过放水漏斗（Tundish）安全排泄膨胀高温水。",
                "status": QuestionStatus.Published,
                "source_reference": "Building Regulations Approved Document G (Section G3); BS EN 12897",
                "chapter_mapping": {"chapter_id": 6, "sub_topic_id": "6.2"},
                "unit_mappings": ["Unit_205"]
            },
            {
                "id": str(uuid.uuid4()),
                "content_en": "To prevent the colonisation and growth of Legionella pneumophila bacteria in domestic hot water storage, what is the minimum temperature at which water should be stored inside a hot water cylinder?",
                "content_zh": "为防止军团菌（Legionella pneumophila）在生活热水储水系统中滋生与繁殖，热水储水缸内的水温至少应维持在多少摄氏度？",
                "options_en": {
                    "A": "40°C",
                    "B": "50°C",
                    "C": "60°C",
                    "D": "75°C"
                },
                "options_zh": {
                    "A": "40°C",
                    "B": "50°C",
                    "C": "60°C",
                    "D": "75°C"
                },
                "correct_answer": "C",
                "explanation_en": "HSE Approved Code of Practice L8 and Building Regs Approved Document G specify that hot water should be stored at 60°C or above. Legionella bacteria proliferate between 20°C and 45°C and are killed within minutes at 60°C.",
                "explanation_zh": "HSE 实践守则 L8 及建筑规范 Approved Document G 要求储水温度不得低于 60°C。军团菌在 20°C 至 45°C 之间极易繁殖，而在 60°C 环境下可在数分钟内被彻底消灭。",
                "status": QuestionStatus.Published,
                "source_reference": "HSE ACoP L8; Approved Document G; HSG274 Part 2",
                "chapter_mapping": {"chapter_id": 6, "sub_topic_id": "6.3"},
                "unit_mappings": ["Unit_205", "Unit_201"]
            },
            {
                "id": str(uuid.uuid4()),
                "content_en": "When using a leaning ladder to access a flat roof scaffolding platform, what is the correct angle of inclination according to HSE guidelines (or the '1 in 4 rule')?",
                "content_zh": "根据 HSE 安全生产指引，在搭设直梯登上平屋顶作业平台时，梯子与地面的推荐倾斜角度（即“1比4比例法则”）是多少？",
                "options_en": {
                    "A": "60 degrees",
                    "B": "75 degrees",
                    "C": "45 degrees",
                    "D": "85 degrees"
                },
                "options_zh": {
                    "A": "60 度",
                    "B": "75 度 (约 1:4 比例)",
                    "C": "45 度",
                    "D": "85 度"
                },
                "correct_answer": "B",
                "explanation_en": "The Health and Safety Executive (HSE) specifies the 1 in 4 rule for leaning ladders: 1 unit out for every 4 units up, which creates an inclination angle of approximately 75 degrees.",
                "explanation_zh": "HSE 规定便携式斜梯必须遵循 1:4 法则（垂直升高 4 米，梯脚外移 1 米），对应的安全摆放仰角约为 75 度，确保梯子既不会向后倾翻也不会向外滑脱。",
                "status": QuestionStatus.Published,
                "source_reference": "Work at Height Regulations 2005; HSE INDG455 Safe use of ladders",
                "chapter_mapping": {"chapter_id": 1, "sub_topic_id": "1.3"},
                "unit_mappings": ["Unit_201"]
            },
            {
                "id": str(uuid.uuid4()),
                "content_en": "In a domestic single stack drainage system, what is the primary cause of 'induced siphonage' in a washbasin trap?",
                "content_zh": "在室内单立管重力排水系统中，导致洗手盆存水弯产生“诱导虹吸（Induced Siphonage）”失封的主要原因是什么？",
                "options_en": {
                    "A": "Slow discharge from the basin itself pulling water through momentum",
                    "B": "High water velocity down the main discharge stack creating negative pressure in the branch pipe",
                    "C": "Wind blowing over the external vent pipe creating a suction effect",
                    "D": "Capillary action caused by hair caught over the trap weir"
                },
                "options_zh": {
                    "A": "洗手盆自身排水速度过慢产生的自重拉力",
                    "B": "主排水立管中大量水流快速下落，在支管入口处形成瞬时负压",
                    "C": "室外屋顶通风管上方强风产生的文丘里吸吮效应",
                    "D": "跨越存水弯水封堰的毛发引起的毛细吸水现象"
                },
                "correct_answer": "B",
                "explanation_en": "Induced siphonage occurs when the rapid discharge of water from an upper appliance passes down the main vertical discharge stack, creating negative air pressure which draws out the water seal of lower branch appliances.",
                "explanation_zh": "诱导虹吸是指上方器具大量排水流经垂直排水主立管时，高速水栓带走空气形成负压波，从而将相连支管存水弯中的水封吸走破坏。",
                "status": QuestionStatus.Published,
                "source_reference": "BS EN 12056-2; Approved Document H Drainage and waste disposal",
                "chapter_mapping": {"chapter_id": 9, "sub_topic_id": "9.2"},
                "unit_mappings": ["Unit_206"]
            },
            {
                "id": str(uuid.uuid4()),
                "content_en": "Which copper pipe jointing method requires the application of flux to prevent oxidation of the metal surfaces during heating?",
                "content_zh": "哪一种铜管连接方法必须涂抹助焊剂（Flux），以在加热过程中防止金属表面氧化并促进熔融焊料的毛细润湿？",
                "options_en": {
                    "A": "Type A compression joint",
                    "B": "Type B manipulate compression joint",
                    "C": "Capillary solder joint",
                    "D": "Push-fit mechanical joint"
                },
                "options_zh": {
                    "A": "Type A 非扩口卡压接头",
                    "B": "Type B 扩口机械卡套接头",
                    "C": "毛细焊锡焊接接头 (Capillary solder joint)",
                    "D": "免工具快插接头 (Push-fit)"
                },
                "correct_answer": "C",
                "explanation_en": "Capillary end-feed and integral solder ring fittings require active chemical flux to clean copper oxide and prevent surface oxidation when heated by a blowlamp.",
                "explanation_zh": "毛细软钎焊与预置焊料环接头必须使用助焊剂，在喷灯高温加热状态下清除氧化膜并保持铜管表面洁净，使熔融焊锡能顺利发生毛细润湿填充。",
                "status": QuestionStatus.Published,
                "source_reference": "C&G 6035 Unit 203; Textbook Chapter 2 Common Processes (p. 68)",
                "chapter_mapping": {"chapter_id": 2, "sub_topic_id": "2.2"},
                "unit_mappings": ["Unit_203"]
            },
            {
                "id": str(uuid.uuid4()),
                "content_en": "A plumber is calculating heat emissions for a central heating radiator. If the temperature of water entering the radiator is 75°C, the return temperature is 65°C, and the room design temperature is 20°C, what is the mean water temperature (MWT) and delta T (ΔT)?",
                "content_zh": "水暖工正在计算中央供暖散热器的热输出。若供水进水温度为 75°C，回水温度为 65°C，房间设计室温为 20°C，则平均水温 (MWT) 和温差 (ΔT) 分别是多少？",
                "options_en": {
                    "A": "MWT = 70°C, ΔT = 50°C",
                    "B": "MWT = 75°C, ΔT = 55°C",
                    "C": "MWT = 65°C, ΔT = 45°C",
                    "D": "MWT = 70°C, ΔT = 10°C"
                },
                "options_zh": {
                    "A": "平均水温 MWT = 70°C, ΔT = 50°C",
                    "B": "平均水温 MWT = 75°C, ΔT = 55°C",
                    "C": "平均水温 MWT = 65°C, ΔT = 45°C",
                    "D": "平均水温 MWT = 70°C, ΔT = 10°C"
                },
                "correct_answer": "A",
                "explanation_en": "Mean Water Temperature (MWT) = (Flow + Return) / 2 = (75 + 65) / 2 = 70°C. Delta T (ΔT) = MWT - Room Temperature = 70°C - 20°C = 50°C (standard British/European test condition BS EN 442).",
                "explanation_zh": "平均水温 MWT = (进水 75°C + 回水 65°C) / 2 = 70°C。散热温差 ΔT = MWT - 室温 = 70°C - 20°C = 50°C，此为 BS EN 442 标准测试基准工况。",
                "status": QuestionStatus.Published,
                "source_reference": "BS EN 442; C&G Unit 207 Central Heating Systems",
                "chapter_mapping": {"chapter_id": 7, "sub_topic_id": "7.1"},
                "unit_mappings": ["Unit_207", "Unit_202"]
            },
            {
                "id": str(uuid.uuid4()),
                "content_en": "Under Building Regulations Approved Document L, what is the maximum specific fan power and minimum seasonal efficiency required for replacing a condensing gas boiler in an existing domestic dwelling?",
                "content_zh": "根据英国建筑法规 Approved Document L（能耗节约），在既有住宅中更换冷凝燃气锅炉时，其 ErP 最低季节性能效指标（SEDBUK/seasonal efficiency）通常要求达到多少？",
                "options_en": {
                    "A": "78%",
                    "B": "86%",
                    "C": "92%",
                    "D": "98%"
                },
                "options_zh": {
                    "A": "78%",
                    "B": "86%",
                    "C": "92%",
                    "D": "98%"
                },
                "correct_answer": "C",
                "explanation_en": "Approved Document L (Conservation of fuel and power) requires new and replacement domestic natural gas boilers to achieve a minimum seasonal space heating efficiency of 92% (ErP A-rating).",
                "explanation_zh": "Approved Document L 规定既有住宅更换天然气锅炉的最低季节性采暖能效要求达到 92%（对应 ErP A 级能效），以显著降低碳排放与燃料消耗。",
                "status": QuestionStatus.Published,
                "source_reference": "Building Regulations Approved Document L1B Conservation of Fuel and Power",
                "chapter_mapping": {"chapter_id": 10, "sub_topic_id": "10.2"},
                "unit_mappings": ["Unit_ENV", "Unit_207"]
            },
            # Technically Verified question (demonstrating workflow)
            {
                "id": str(uuid.uuid4()),
                "content_en": "What is the mandatory procedure when carrying out Safe Isolation on a single-phase domestic central heating programmer before performing electrical maintenance?",
                "content_zh": "在对单相家用中央供暖温控编程器进行电气检修前，执行“安全隔离（Safe Isolation）”的法定规范操作步骤是什么？",
                "options_en": {
                    "A": "Turn off the fused spur switch and tape it with insulating tape",
                    "B": "Isolate the supply, lock off with padlock and danger notice, test proving unit, test circuits with voltage indicator, and re-test proving unit",
                    "C": "Remove the neutral fuse and check current with an ammeter clamp",
                    "D": "Switch off the main consumer unit without proving the voltage indicator"
                },
                "options_zh": {
                    "A": "仅关闭带熔断器的双极开关并用绝缘胶带贴住",
                    "B": "断开电源，上锁加挂警告标牌，使用校验器校准验电器，检测待测电路确认无电，再次使用校验器核实验电器",
                    "C": "拔出零线保险丝并使用钳形表测量回路电流",
                    "D": "直接切断总配电箱主开关，无需对验电器进行前后校验"
                },
                "correct_answer": "B",
                "explanation_en": "Safe isolation requires: 1. Permission & identify source; 2. Isolate and lock off (LOTO); 3. Prove test instrument on proving unit; 4. Test between all conductors (L-N, L-E, N-E); 5. Re-prove test instrument on proving unit to ensure it did not fail during test.",
                "explanation_zh": "电气安全隔离五步闭环流程：1. 确认断电范围；2. 隔离并挂锁上标签（LOTO）；3. 使用检验器（Proving Unit）校准双极电压测试仪；4. 全面测试所有导线对间电压；5. 再次在检验器上复测验电器功能正常。",
                "status": QuestionStatus.Technically_Verified,
                "source_reference": "Electricity at Work Regulations 1989; HSE Guidance Note GS38; BS 7671",
                "chapter_mapping": {"chapter_id": 11, "sub_topic_id": "11.1"},
                "unit_mappings": ["Unit_208", "Unit_201"]
            },
            # AI Reviewed question (demonstrating workflow)
            {
                "id": str(uuid.uuid4()),
                "content_en": "What is the recommended minimum clearance distance between the overflow warning pipe invert and the top water level in a domestic cold water storage cistern (CWSC)?",
                "content_zh": "在室内冷水储水箱（CWSC）中，溢水报警管（Warning pipe）管底标高与正常最高工作水位之间的推荐最小垂直净距是多少？",
                "options_en": {
                    "A": "10 mm",
                    "B": "25 mm",
                    "C": "50 mm",
                    "D": "75 mm"
                },
                "options_zh": {
                    "A": "10 mm",
                    "B": "25 mm",
                    "C": "50 mm",
                    "D": "75 mm"
                },
                "correct_answer": "B",
                "explanation_en": "The Water Supply Regulations specify that the warning pipe invert should be positioned at least 25 mm above the operating water shut-off level to prevent nuisance splashing and overflow.",
                "explanation_zh": "《水条例》及规范要求报警溢流管内底应高出浮球阀关闭时的最高静止水位至少 25 mm，防止正常波动时溢水。",
                "status": QuestionStatus.AI_Reviewed,
                "source_reference": "Water Supply (Water Fittings) Regulations 1999, G24.1",
                "chapter_mapping": {"chapter_id": 5, "sub_topic_id": "5.2"},
                "unit_mappings": ["Unit_204"]
            },
            # Draft question (demonstrating workflow)
            {
                "id": str(uuid.uuid4()),
                "content_en": "Which device must be fitted to an unvented hot water supply system to absorb the expansion volume of water as it is heated from 10°C to 65°C?",
                "content_zh": "在闭式承压生活热水系统中，必须配置何种装置以吸收水从 10°C 加热至 65°C 过程中产生的体积热膨胀？",
                "options_en": {
                    "A": "Open vent pipe over CWSC",
                    "B": "Diaphragm expansion vessel or internal air bubble",
                    "C": "Check valve",
                    "D": "Automatic air vent"
                },
                "options_zh": {
                    "A": "储水箱上方的开放式膨胀管",
                    "B": "隔膜式膨胀罐或内部充气气囊 (Expansion Vessel)",
                    "C": "单向止回阀",
                    "D": "自动排气阀"
                },
                "correct_answer": "B",
                "explanation_en": "Water expands by approximately 3-4% when heated from 10°C to 65°C. In an unvented system, this expansion must be accommodated by a pre-charged diaphragm expansion vessel or internal air bubble.",
                "explanation_zh": "水由 10°C 升高至 65°C 体积膨胀约 3%~4%。闭式承压系统必须依靠带有预充氮气/空气的隔膜膨胀罐或储水缸顶部的空气囊缓冲吸收膨胀量。",
                "status": QuestionStatus.Draft,
                "source_reference": "Building Regulations Approved Document G3",
                "chapter_mapping": {"chapter_id": 6, "sub_topic_id": "6.2"},
                "unit_mappings": ["Unit_205"]
            }
        ]

        for q_item in questions_data:
            q = Question(
                id=q_item["id"],
                content_en=q_item["content_en"],
                content_zh=q_item["content_zh"],
                options_en=q_item["options_en"],
                options_zh=q_item["options_zh"],
                correct_answer=q_item["correct_answer"],
                explanation_en=q_item["explanation_en"],
                explanation_zh=q_item["explanation_zh"],
                status=q_item["status"],
                source_reference=q_item["source_reference"]
            )
            db.add(q)
            db.flush()

            # Chapter mapping
            ch_map = QuestionChapterMapping(
                question_id=q.id,
                chapter_id=q_item["chapter_mapping"]["chapter_id"],
                sub_topic_id=q_item["chapter_mapping"]["sub_topic_id"]
            )
            db.add(ch_map)

            # Unit mappings
            for u_id in q_item["unit_mappings"]:
                u_map = QuestionUnitMapping(
                    question_id=q.id,
                    unit_id=u_id
                )
                db.add(u_map)

        db.commit()
        print(f"Successfully seeded {len(chapters_data)} chapters, {len(units_data)} units, and {len(questions_data)} questions.")
    except Exception as e:
        db.rollback()
        print(f"Seeding error: {e}")
        raise e
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
