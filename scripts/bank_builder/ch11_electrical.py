# Chapter 11: Electrical principles and processes (Part 1: Questions 1 to 40)
from .utils import make_q

def get_questions():
    questions = []
    
    data = [
        # 11.1 Fundamental Electrical Quantities, Ohm's Law & Power
        ("11.1",
         "Under SI units, what are the three fundamental electrical quantities, their standard symbols, and their corresponding units of measurement?",
         "在國際單位制（SI）電氣度量衡體系中，電氣三大基本物理量、其通用物理符號以及標準計量單位是什麼？",
         {"A": "Weight (W in kg), Speed (S in m/s), and Temperature (T in °C)", "B": "Voltage / Electromotive Force (V in Volts), Current (I in Amperes), and Electrical Resistance (R in Ohms Ω)", "C": "Pressure (P in bar), Flow (Q in L/min), and Volume (V in Litres)", "D": "Power (P in Amps), Voltage (V in Watts), and Current (C in Volts)"},
         {"A": "重量 (W，公斤 kg)、速度 (S，米/秒 m/s)、以及溫度 (T，攝氏度 °C)", "B": "電壓 / 電動勢 (V，單位為伏特 Volts)、電流 (I，單位為安培 Amperes)、以及電阻 (R，單位為歐姆 Ohms Ω)", "C": "水壓 (P，巴 bar)、水流量 (Q，升/分)、以及容積 (V，升 Litres)", "D": "功率 (P，安培)、電壓 (V，瓦特)、以及電流 (C，伏特)"},
         "B", "The core electrical triad is: Electromotive force (V, Volts), Flow of electrons / Current (I, Amps), and Opposition to current / Resistance (R, Ohms Ω).", "電學鐵三角基本概念必考：電壓 V（推動電子流動的水壓，伏特）；電流 I（每秒流過導線的電子流量，安培）；電阻 R（管道內部阻礙電流的阻力，歐姆 Ω）。", "BS 7671 Requirements for Electrical Installations; C&G Unit 208"),

        ("11.1",
         "What is Ohm's Law formula used to calculate the electric current (I) flowing through a heating element with known resistance (R) connected across a voltage supply (V)?",
         "根據經典歐姆定律（Ohm's Law），當已知負載電阻（R）且兩端施加已知電壓（V）時，計算流經該負載電路電流（I）的物理公式是什麼？",
         {"A": "I = V × R", "B": "I = V ÷ R (Current = Voltage divided by Resistance)", "C": "I = R ÷ V", "D": "I = V + R"},
         {"A": "I = V × R", "B": "I = V ÷ R (電流 = 電壓除以電阻)", "C": "I = R ÷ V", "D": "I = V + R"},
         "B", "Ohm's Law triangle: V = I × R; therefore, I = V / R and R = V / I. Current is directly proportional to voltage and inversely proportional to resistance.", "歐姆定律公式變換：V = I × R。求電流時：I = V / R；求電阻時：R = V / I。電壓越高電流越大，電阻越大電流越小。水暖電工必背算式！", "BS 7671; City & Guilds Unit 208 Electrical Science"),

        ("11.1",
         "If a 230V domestic immersion heater heating element has a measured electrical resistance of 17.6 Ohms, what current (I) does it draw under full load?",
         "若某台額定供電 230V 的家庭熱水浸入式電加熱棒（Immersion Heater），實測其內部電阻絲阻值為 17.6 歐姆，該加熱棒在滿負荷工作時汲取的電流是多少？",
         {"A": "13.07 Amperes (approx 13 Amps, since I = 230V ÷ 17.6Ω)", "B": "100 Amps", "C": "0.5 Amps", "D": "4,048 Amps"},
         {"A": "13.07 安培 (約合 13 安培，計算式：I = 230V ÷ 17.6Ω ≈ 13.07A)", "B": "100 安培", "C": "0.5 安培", "D": "4,048 安培"},
         "A", "Calculation: I = V ÷ R = 230 ÷ 17.6 = 13.068 A ≈ 13 Amps. This is why a standard 3kW domestic immersion heater requires a dedicated 13A or 16A fused supply.", "帶入歐姆定律計算：I = V / R = 230 / 17.6 = 13.07 安培。這正是英國標準 3kW 電熱水棒必須由獨立 13A 保險絲或 16A 空開單獨供電的原因！", "BS 7671; C&G Unit 208 Practical Calculations"),

        ("11.1",
         "What is the standard formula used to calculate Electrical Power (P in Watts) from Voltage (V in Volts) and Current (I in Amperes)?",
         "在純電阻性交流電路中，根據電壓（V）與電流（I）計算電功率（P，單位為瓦特 Watts）的基本公式是什麼？",
         {"A": "P = V ÷ I", "B": "P = V × I (Power = Voltage multiplied by Current)", "C": "P = I ÷ V", "D": "P = V - I"},
         {"A": "P = V ÷ I", "B": "P = V × I (功率 = 電壓乘以電流)", "C": "P = I ÷ V", "D": "P = V - I"},
         "B", "Electric power formula: P = V × I. Combined with Ohm's Law (V = IR), power can also be expressed as P = I²R or P = V² / R.", "電功率計算黃金公式：P = V × I（瓦特 = 伏特 × 安培）。結合歐姆定律還可推導為 P = I²R 或 P = V² / R。水暖工核算電器功率和選配電線必備！", "BS 7671 Section 131; C&G Unit 208"),

        ("11.1",
         "What is the standard nominal Single-Phase AC mains supply voltage and frequency delivered to domestic properties across the UK?",
         "在全英國居民家庭住宅中，國家電網入戶供應的標準「單相交流市電電壓與頻率」基準參數是多少？",
         {"A": "110 Volts DC, 60 Hz", "B": "230 Volts AC (within +10% / -6% tolerance), 50 Hz", "C": "415 Volts AC, 100 Hz", "D": "12 Volts AC, 25 Hz"},
         {"A": "110 伏特直流電，60 赫茲", "B": "230 伏特交流電 (法定允許偏差範圍為 +10% / -6%，即 216.2V 至 253V)，頻率為 50 赫茲 (50 Hz)", "C": "415 伏特交流電，100 赫茲", "D": "12 伏特交流電，25 赫茲"},
         "B", "UK harmonized domestic supply is 230V AC single-phase at 50 Hz (historically 240V). Three-phase commercial supplies operate at 400V (historically 415V).", "英國市電標準參數必背：單相交流電 230V、頻率 50Hz！法規允許波動區間為 216.2V 至 253V。商業工廠動力電則是三相 400V 50Hz。", "Electricity Safety, Quality and Continuity Regulations (ESQCR) 2002; BS 7671"),

        ("11.1",
         "If a 9.5 kW electric instantaneous shower runs continuously for 30 minutes, how many kilowatt-hours (kWh) of electrical energy are consumed?",
         "一台功率為 9.5 kW 的即熱式電淋浴花灑連續全負荷運轉沖涼 30 分鐘（0.5 小時），累計消耗了多少「千瓦·時（kWh，即度電）」的電能量？",
         {"A": "4.75 kWh (since Energy = 9.5 kW × 0.5 hours = 4.75 kWh)", "B": "95 kWh", "C": "19 kWh", "D": "0.5 kWh"},
         {"A": "4.75 kWh (即 4.75 度電，計算式：電能 = 9.5 kW × 0.5 小時 = 4.75 kWh)", "B": "95 kWh", "C": "19 kWh", "D": "0.5 kWh"},
         "A", "Energy consumed (kWh) = Power (kW) × Time (hours) = 9.5 kW × 0.5 hr = 4.75 kWh. Multiplying this by the electricity unit cost gives the total cost of the shower.", "電能計算公式：千瓦時（度） = 功率（kW） × 時間（小時）。9.5 kW 衝半個小時（0.5h） = 4.75 度電。若一度電 30 便士，洗一次澡電費約 1.43 英鎊！", "BS 7671; C&G Unit 208 Energy Calculations"),

        ("11.1",
         "Which group of materials lists items that are all excellent electrical CONDUCTORS?",
         "下列哪組物質全部屬於導電性能極佳的優良「電氣導體 (Electrical Conductors)」？",
         {"A": "Dry timber, PVC plastic, and glass", "B": "Copper, Aluminium, Silver, and Gold", "C": "Rubber, porcelain, and distilled water", "D": "Dry air, silicone, and nylon"},
         {"A": "乾燥木材、PVC 塑料、以及石英玻璃", "B": "紫銅 (Copper)、金屬鋁 (Aluminium)、純銀 (Silver)、以及純金 (Gold)", "C": "硫化橡膠、高溫陶瓷、以及純淨蒸餾水", "D": "乾燥空氣、硅膠、以及尼龍塑料"},
         "B", "Metals possess free outer valence electrons that drift easily under electric potential, making silver, copper, and aluminium premier electrical conductors.", "導體常識必考：金屬原子外層電子自由漂移，是優良導體！銀導電最好但太貴，紫銅性價比最高（全屋電線水管全用銅），鋁自重輕用於高壓架空輸電線。", "BS 7671 Section 132; C&G Unit 208"),

        ("11.1",
         "Which group of materials lists items that are all excellent electrical INSULATORS?",
         "下列哪組物質全部屬於能牢固阻止電流通過的優質「電氣絕緣體 (Electrical Insulators)」？",
         {"A": "Copper, brass, and steel", "B": "Polyvinyl Chloride (PVC), rubber, porcelain, ceramic, and glass", "C": "Tap water, salt water, and carbon", "D": "Aluminium, lead, and wet earth"},
         {"A": "紫銅、黃銅、以及低碳鋼", "B": "聚氯乙烯塑料 (PVC)、硫化橡膠、電工陶瓷、特種瓷料、以及高絕緣玻璃", "C": "普通自來水、食鹽水、以及碳素石墨", "D": "金屬鋁、重金屬鉛、以及潮濕泥土"},
         "B", "Insulators possess tightly bound valence electrons that resist electron flow, used for cable sheathing (PVC), tool handles (rubber), and overhead wire hangers (ceramic/glass).", "絕緣體常識必考：原子被核死死鎖住，電子根本動不了！PVC 塑料做電線皮，橡膠做手套扳手絕緣柄，陶瓷做高壓電線杆絕緣子，死死攔截電流，保護人身安全！", "BS 7671; C&G Unit 208"),

        ("11.1",
         "In a simple electrical SERIES circuit containing three resistors (R1 = 10Ω, R2 = 20Ω, R3 = 30Ω), what is the total combined circuit resistance (R_total)?",
         "在一個由三個電阻相互「串聯 (Series Circuit)」組成的電路中（R1 = 10Ω，R2 = 20Ω，R3 = 30Ω），該電路的總等效電阻是多少？",
         {"A": "60 Ohms (since R_total = R1 + R2 + R3 = 10 + 20 + 30 = 60Ω)", "B": "5.45 Ohms", "C": "6,000 Ohms", "D": "0 Ohms"},
         {"A": "60 歐姆 (計算式：總電阻 R = R1 + R2 + R3 = 10 + 20 + 30 = 60Ω)", "B": "5.45 歐姆", "C": "6,000 歐姆", "D": "0 歐姆"},
         "A", "In series circuits, resistances add directly: R_total = R1 + R2 + R3 = 10 + 20 + 30 = 60 Ohms. The same current flows through all components, while voltage divides across each resistor.", "串聯電路定律必背：串聯電阻像長跑接力，電阻直接相加（R = R1 + R2 + R3）！總電阻越串越大；電流處處相等；電壓按阻值比例分壓。如聖誕樹老彩燈串聯，壞一顆全滅！", "BS 7671; C&G Unit 208 Electrical Circuits"),

        ("11.1",
         "What is the key electrical characteristic of a PARALLEL circuit configuration used in domestic wiring installations?",
         "在家庭室內照明與插座普遍採用的「並聯電路 (Parallel Circuit)」中，其最核心的電氣特性是什麼？",
         {"A": "Current is identical in all branches, but voltage changes", "B": "Full mains voltage (230V) is applied across every individual connected appliance branch, and switching off one appliance does not interrupt power to the others", "C": "Total resistance increases every time a device is plugged in", "D": "No current flows anywhere"},
         {"A": "各支路中的電流絕對相同，但電壓隨時大幅波動", "B": "每一個獨立負載電器支路兩端均能獲得完整的 230V 滿額市電電壓，且關閉或拔掉其中任何一個電器、絕對不會切斷其他電器的供電運轉！", "C": "每多插入一個用電器，全屋總電阻就成倍暴增", "D": "全系統任何地方均無任何電流流動"},
         "B", "Parallel wiring ensures every appliance receives full 230V. Total circuit current is the sum of branch currents (I_total = I1 + I2), and devices operate independently without affecting each other.", "並聯電路家庭標配：客廳關燈，臥室燈不會滅，因為是並聯！每個插座兩端都是足足 230V。並聯支路越多，全屋總電阻越小，總電流越大（I = I1 + I2 + I3）。", "BS 7671 Section 132; C&G Unit 208"),

        # 11.2 Magnetism, Solenoids, Relays & Transformers
        ("11.2",
         "What electromagnetic device utilizes an electric coil winding to pull an internal ferrous plunger and snap-open a gas or water valve?",
         "利用通電螺線管線圈產生電磁吸力、拉動內部金屬鐵芯活塞以瞬間開啟燃氣或水路的電磁執行組件稱為什麼？",
         {"A": "A thermal expansion wax capsule", "B": "A Solenoid Valve (Electromagnetic Solenoid)", "C": "A manual brass handwheel", "D": "A bi-metallic strip"},
         {"A": "熱膨脹石蠟包溫控閥芯", "B": "電磁閥 (Solenoid Valve / 螺線管電磁執行器)", "C": "純手動旋轉純黃銅手輪", "D": "雙金屬機械感溫片"},
         "B", "A solenoid converts electrical energy directly into linear mechanical motion. When energized, the electromagnetic coil lifts an iron plunger against spring pressure to open gas or water valves.", "電磁閥工作原理必考：壁掛爐燃氣開關、洗衣機進水閥 100% 全是電磁閥！線圈一通電立刻化為強力電磁鐵，把裡面的鐵芯拔起開通氣水；斷電時彈簧啪的一聲把閥門死死按回關閉！", "BS EN 161 Automatic shut-off valves for gas burners; C&G Unit 208"),

        ("11.2",
         "What is an electrical 'Relay' or 'Contactor' commonly used in heating and heat pump control circuits?",
         "在家庭中央採暖與熱泵控制系統中，廣泛採用的「電氣繼電器 (Relay) / 接觸器 (Contactor)」的核心電氣控制功能是什麼？",
         {"A": "A device that converts electricity to steam", "B": "An electrically operated electromagnetic switch that uses a low-voltage or low-current control signal (e.g. from a room thermostat or PCB) to switch a high-current load (e.g. an electric heater or compressor)", "C": "A battery charger", "D": "A mechanical water filter"},
         {"A": "將電能直接轉化為高壓蒸汽的設備", "B": "一種電磁驅動的開關：利用微弱的低電壓/小電流控制信號（如室內溫控器或主板芯片弱電），安全間接切換並接通高電壓、大電流動力負載（如 3kW 加熱棒或熱泵大功率壓縮機）", "C": "汽車蓄電池充電器", "D": "機械管道水質過濾器"},
         "B", "Relays isolate sensitive control circuits from heavy power circuits. A 5V or 24V signal energizes the relay coil, closing heavy silver-faced contacts to safely power a 230V 16A compressor.", "繼電器小控大核心原理：溫控器電腦板太嬌貴，承受不起十幾安培大電流！主板輸出微弱信號吸合繼電器線圈，繼電器裡結實的厚銀觸點合閘，帶動大功率壓縮機運轉，弱電強電徹底物理隔離！", "BS EN 61810 Electromechanical elementary relays; C&G Unit 208"),

        ("11.2",
         "On UK construction sites, why do portable power tools operate at 110V supplied from a specialist 230V-to-110V 'Centre-Tapped-to-Earth' (CTE) safety transformer?",
         "在英國所有建築工地施工現場，水暖電工手持電動工具為什麼強制要求使用由 230V 轉 110V「中心點接地 (Centre Tapped to Earth - CTE)」隔離變壓器供電？",
         {"A": "110V tools are cheaper to buy", "B": "Because the secondary winding is center-tapped to earth, limiting the maximum potential shock voltage between any live conductor and earth ground to just 55 Volts (a non-lethal touch voltage)", "C": "110V batteries weigh less than 230V", "D": "Regulations ban electricity completely"},
         {"A": "因為 110V 電動工具在市場上的採購價格便宜得多", "B": "因為變壓器次級輸出繞組在中央抽頭點直接接地，將任何一根火線導線與真實大地之間的「最大觸電接觸電壓死死限制在僅僅 55 伏特 (55V)」，即使工人踩在泥地裡電纜被割破也絕不致命！", "C": "110V 的電池重量比 230V 輕得多", "D": "法規禁止工地使用任何電能"},
         "B", "Centre-Tapped-to-Earth (CTE) reduces shock voltage to 55V (110V ÷ 2 = 55V to earth). 55V is below the human ventricular fibrillation threshold, making accidental shocks on muddy sites non-fatal.", "工地黃色 110V 變壓器救命真理必考：工地全是鋼筋爛泥，人踩在水裡若被 230V 擊中必死無疑！黃色變壓器中間點接地（CTE）：兩頭電壓 110V，但每根線對地只有 55V！人摸到 55V 電壓只會麻一下，心臟絕不室顫停跳！", "BS 7671 Section 704 Construction and demolition sites; BS EN 61558-2-23"),

        # 11.3 Safe Electrical Isolation Procedure (HSE Guidance Note GS38)
        ("11.3",
         "Under the Electricity at Work Regulations 1989 and HSE Guidance Note GS38, what is the FIRST formal operational step before carrying out any maintenance work on an electrical heating appliance?",
         "根據英國 1989 年工作用電法規與 HSE GS38 指南，在對任何電加熱電器、壁掛爐實施檢修作業前，標準的「第一步法定前置操作程序」是什麼？",
         {"A": "Cut all cables with wire cutters immediately", "B": "Seek permission from the client/occupant, notify that the supply will be disconnected, and correctly identify the specific circuit and point of isolation for that appliance", "C": "Lick the live terminal with human tongue to see if it sparks", "D": "Turn on all hot water taps"},
         {"A": "拿鋼絲鉗立刻將所有外露電線全部一剪兩斷", "B": "徵得業主/客戶同意，告知即將實施斷電，並精確辨識出該電器設備專屬的受控供電配電迴路與具體隔離斷開點", "C": "用舌頭舔舐火線接線柱看是否有火花", "D": "大開全屋所有洗澡熱水水龍頭"},
         "B", "Step 1 of Safe Isolation: Gain permission from the client, communicate that power will be switched off (stopping data loss or medical disruptions), and trace the correct circuit breaker/isolator.", "安全隔離第一步（確認與告知）：不能二話不說直接拉閘！萬一客戶家裡開著透析機或正在開越洋視頻會議，隨便拉閘釀大禍！必須先向客戶打招呼確認，並在配電箱上精確找到對應那一路空開！", "Electricity at Work Regulations 1989 Reg 12; HSE Guidance Note GS38"),

        ("11.3",
         "What physical safety kit must a plumber apply to a circuit breaker or rotary isolator after switching it off during safe electrical isolation?",
         "在安全電氣隔離程序中，水暖技師將空開開關或旋轉隔離器切換至 OFF 斷開位置後，必須物理加裝何種「鎖定安全套件 (Lock-off Kit)」？",
         {"A": "A piece of chewing gum stuck on the switch", "B": "A dedicated padlock lock-off bracket with a unique safety padlock (key retained exclusively in the plumber's pocket) and a prominent 'DANGER - DO NOT OPERATE' warning tag", "C": "A strip of transparent tape", "D": "No lock or tag is needed"},
         {"A": "黏在開關按鈕表面的一塊口香糖", "B": "專用開關機械鎖死支架、掛上一把唯一的專屬安全掛鎖（鑰匙必須死死裝在水暖工自己的貼身口袋裡）、並懸掛醒目的「危險 - 嚴禁合閘」警告標籤牌！", "C": "普通透明文具膠帶紙", "D": "完全無需安裝任何掛鎖或標籤"},
         "B", "Lockout/Tagout (LOTO): Securing the switch with an individual padlock ensures nobody else (e.g. homeowner or apprentice) can turn the circuit back on while the plumber has their hands inside the boiler.", "上鎖掛牌（LOTO）保命規則必考：很多水暖工被電死，就是因為他在樓上修鍋爐，樓下不知道的業主隨手一推電閘！必須裝專用塑料夾子扣住空開、掛上黃色掛鎖，鑰匙揣在自己兜裡，任何人也休想合閘！", "HSE Guidance Note GS38; Electricity at Work Regulations 1989"),

        ("11.3",
         "Under HSE Guidance Note GS38, why is a dedicated, battery-independent Two-Pole Voltage Indicator (such as a Martindale VI-13800) required to prove dead, rather than a non-contact voltage pen or digital multimeter?",
         "根據 HSE GS38 規範，在驗證線路完全斷電無電（Proving Dead）時，為什麼強制要求使用專用雙極電壓檢測儀（如 Martindale），而嚴禁使用感應測電筆或檔位萬用表？",
         {"A": "Voltage pens cost too much money", "B": "Non-contact pens can be blinded by shielded cables, and multimeters have complex rotary selector switches that can blow up or falsely read 0V if accidentally set to the wrong range or amps jack", "C": "Two-pole testers are made of solid gold", "D": "Multimeters attract lightning"},
         {"A": "感應測電筆在市場上的售價過於昂貴", "B": "感應測電筆易受金屬屏蔽電纜屏蔽導致假陰性漏報；而萬用表有複雜旋鈕檔位，若學徒不慎撥錯至電流檔（Amps）或電阻檔會引發高溫弧光短路爆炸，或因量程錯誤顯示 0V 誤導殺人！", "C": "雙極電壓測試儀是由純金金屬打造而成", "D": "萬用表會在室內主動吸引雷擊"},
         "B", "GS38 mandates approved two-pole testers without switches, batteries, or fuses that could give false-dead readings. Non-contact pens give lethal false negatives; multimeters risk flashover on wrong ranges.", "感應電筆與萬用表殺人陷阱：感應測電筆隔著皮線往往不亮，你以為沒電一摸當場電死！萬用表插錯插孔一測直接在手裡炸成大火球！GS38 認證雙極測電儀沒有任何開關檔位，插上去有電就亮燈，最可靠！", "HSE Guidance Note GS38 Electrical test equipment for use on low voltage installations"),

        ("11.3",
         "Under HSE GS38, what are the three mandatory design features of compliant test leads and probes on an approved voltage indicator?",
         "根據英國 HSE GS38 安全標準，合格的低壓電氣測試表筆與測試導線必須具備哪三大強制安全構造？",
         {"A": "Painted red, made of glass, and 10 meters long", "B": "Fused test leads (e.g. 500mA ceramic HBC fuses), finger guards / barrier ribs to stop fingers slipping onto live brass, and exposed metal probe tips limited to maximum 2mm to 4mm (with retractable spring sleeves)", "C": "Bare uninsulated wire probes with sharp 100mm spikes", "D": "Rubber suction cups on the tips"},
         {"A": "外表全部刷成紅色、由玻璃製成、且長度達到 10 米", "B": "內置高分斷陶瓷保險絲（500mA HBC 熔斷器）、筆身自帶防滑擋手護翼（防止手指滑向帶電金屬部）、以及外露金屬探針長度嚴格限制在「最大 2mm 至 4mm 以內」（配備伸縮彈簧絕緣護套）", "C": "完全無絕緣層的裸露金屬表筆，帶有 100 毫米長鋒利金屬尖刺", "D": "探針尖端帶有吸盤玩具"},
         "B", "GS38 probe requirements: 1. Max 2-4mm exposed metal (prevents bridging terminals and creating dead shorts); 2. Finger guards; 3. In-line high-breaking-capacity (HBC) fuses in leads.", "GS38 安全表筆三大鐵律必考：1. 針頭金屬外露不超 4 毫米（太長會在相鄰端子間打火短路）；2. 筆桿有防滑擋手圈（手指滑不過去）；3. 導線肚子裡藏著陶瓷高分斷保險絲，短路時瞬間熔斷防爆炸！", "HSE Guidance Note GS38 Section 7; BS EN 61243-3"),

        ("11.3",
         "What is the complete, correct sequence of the 'Proving Dead' 3-stage validation process using a dedicated Proving Unit and a GS38 voltage indicator?",
         "在安全電氣隔離中，使用專用校驗單元（Proving Unit）與 GS38 測電儀實施「驗電驗無電」的標準三步循環校驗流程是什麼？",
         {"A": "Touch the live wire once, then start work", "B": "1. Test the voltage indicator on a known proving unit to confirm it lights up; 2. Test ALL conductor combinations for dead (L-N, L-E, N-E); 3. RE-TEST the voltage indicator on the proving unit to prove the tester did not fail during the test", "C": "Test the wire, throw the tester away, and work", "D": "Look at the wire with a magnifying glass"},
         {"A": "用手指輕觸一下火線確認無電，隨後立刻開始維修", "B": "1. 先在已知帶電的校驗單元（Proving Unit）上測試測電儀，確認指示燈正常點亮；2. 隨後精準檢測被測線路的所有導線組合（火對零 L-N、火對地 L-E、零對地 N-E），確認均為 0V 無電；3. 「立刻將測電儀再次插回校驗單元二次校驗」，確認測電儀自身在剛才檢測過程中沒有損壞失效！", "C": "隨便測一下電線，把測電儀扔進工具包開始施工", "D": "拿放大鏡仔細端詳電線外皮顏色"},
         "B", "The 3-stage proving rule is absolute: Prove tester works on Proving Unit -> Test circuit dead -> Re-prove tester works on Proving Unit. If the internal tester fuse blew during stage 2, stage 3 catches it.", "三步驗電生死閉環必考：先測校驗盒（確認表是好的）→ 測待修電路全方位無電（火零、火地、零地）→ 再次測校驗盒（確認剛才表沒壞）！萬一測電儀剛好在測電路時壞了亮不了燈，沒做第三步你就會誤判無電摸上去送命！", "HSE Guidance Note GS38 Section 10; Electricity at Work Regulations 1989"),

        ("11.3",
         "When testing a single-phase 230V circuit for dead at the appliance terminal block, what THREE conductor combination tests must be verified to read zero volts?",
         "在單相 230V 家用電器接線端子排處進行驗電時，必須逐一檢測並確認哪「三種導線組合」全部絕對為零伏特無電？",
         {"A": "Line to Neutral (L-N), Line to Earth (L-E), and Neutral to Earth (N-E)", "B": "Water pipe to gas pipe only", "C": "Neutral to Neutral only", "D": "Earth to Earth only"},
         {"A": "火線對零線 (Line to Neutral - L-N)、火線對地線 (Line to Earth - L-E)、以及零線對地線 (Neutral to Earth - N-E)", "B": "自來水管對燃氣管", "C": "零線對零線", "D": "地線對地線"},
         "B", "All 3 paths must be verified dead: L to N, L to E, and N to E. A floating neutral or back-fed neutral conductor can carry lethal 230V to earth even if the line breaker is open.", "三維全方位測零電壓必考：火對零、火對地、零對地！千萬不要以為只測火線沒電就安全了，下水道零線萬一在變壓器端接觸不良（懸浮零線），零線上可能帶有要命的 230V 反饋電壓！三組全部測完顯示 0V 才准動手！", "BS 7671 Section 132; HSE Guidance Note GS38; C&G Unit 208"),

        # 11.4 Earthing, Protective Bonding & Shock Protection
        ("11.4",
         "At approximately what electrical shock current passing across the human heart does potentially fatal Ventricular Fibrillation (cardiac arrest) typically occur in human adults?",
         "當流經人體心臟的交流觸電電流達到大約多少毫安（mA）時，人體通常會突發致命的心室纖顫（心臟失控抽搐停止泵血），若不及時跳閘會在幾分鐘內致死？",
         {"A": "At approximately 30 to 50 milliamperes (30-50 mA)", "B": "100,000 Amperes", "C": "0.0001 mA", "D": "10 Amperes"},
         {"A": "大約僅需 30 至 50 毫安 (30-50 mA)", "B": "100,000 安培超大電流", "C": "0.0001 毫安微電流", "D": "10 安培"},
         "A", "Physiological shock thresholds: 1mA = tickle threshold; 10mA = cannot-let-go muscle tetanus; 30mA = ventricular fibrillation threshold. This is why safety RCDs are calibrated to trip at 30mA.", "人體觸電生死電流階梯：1mA 有點麻；10mA 手肌肉痙攣抓死電線鬆不開手；30mA 心臟瞬間心室纖顫停跳！這就是為什麼全世界所有漏電保護器（RCD）全部死死定格在 30mA 必須跳閘的原因！", "BS 7671 Regulation 411.3.3; IEC 60479-1 Effects of current on human beings"),

        ("11.4",
         "Under BS 7671 (18th Edition), what is the function of 'Main Protective Bonding' connected to incoming metallic plumbing services (water, gas, oil)?",
         "根據英國電工法規 BS 7671（第 18 版）規定，連接在入戶自來水管、燃氣管、燃油金屬管上的「主等電位聯結 (Main Protective Bonding)」的核心保護功能是什麼？",
         {"A": "To charge water with static electricity", "B": "To connect extraneous metallic service pipework to the property's Main Earthing Terminal (MET), equalizing electric potential during electrical faults so that no lethal touch voltage can exist between pipes and exposed metal appliances", "C": "To filter sediment out of the water pipes", "D": "To heat up the incoming copper pipes"},
         {"A": "為自來水管充入靜電以殺滅細菌", "B": "將入戶的金屬管道（外界可導電部分）與全屋主接地端子排（MET）做金屬跨接，在發生漏電接地故障時將全屋所有金屬水管、氣管電位死死拉平到同一電位（等電位），杜絕人體同時觸摸水管與電器時被電死！", "C": "過濾自來水管內部的泥沙雜質", "D": "通電加熱入戶冰冷的自來水銅管"},
         "B", "Main bonding clamps metallic pipes to the Main Earthing Terminal (MET). If an electrical fault occurs, everything rises to the same voltage simultaneously, keeping touch voltage near zero and preventing electric shock.", "等電位聯結保命真諦必考：如果水管是 0 伏、漏電的洗衣機外殼是 230 伏，人一隻手洗手一隻手摸洗衣機，230V 電壓直接穿透心臟電死！把水管和地線死死連在一起，兩邊電壓永遠一樣平，沒有電位差就絕沒有觸電！", "BS 7671:2018 Regulation 411.3.1.2; C&G Unit 208"),

        ("11.4",
         "Under BS 7671 Table 54.8, what is the MINIMUM cross-sectional area of the copper earthing conductor required for Main Protective Bonding in a domestic installation with a standard PME (TN-C-S) supply?",
         "根據 BS 7671 表 54.8 規定，在全英最普及的 PME（TN-C-S 系統）供電民居中，連接水管燃氣管的「主保護接地等電位聯結銅導線」，法定的最小截面積是多少？",
         {"A": "Minimum 10 mm² copper conductor (with green/yellow PVC sheath)", "B": "1.0 mm²", "C": "100 mm²", "D": "0.5 mm²"},
         {"A": "至少 10 mm² 截面積的多股紫銅線 (配備綠黃雙色 PVC 絕緣外皮)", "B": "1.0 mm² 細導線", "C": "100 mm² 粗電纜", "D": "0.5 mm²"},
         "A", "For standard domestic PME supplies with supply neutral conductor up to 35mm², main bonding conductors must be at least 10mm² copper (Regulation 544.1.1) to safely carry diverted network circulating currents.", "10 平方主接地線必考數字：自來水總管和燃氣表旁邊那根粗粗的黃綠色地線，截面積必須是足足 10mm²！太細的線（如 2.5 或 4 平方）在電網零線斷裂故障時，會被巨大的回流電流直接燒紅燒融引發火災！", "BS 7671:2018 Regulation 544.1.1 & Table 54.8"),

        ("11.4",
         "Under BS 7671, WHERE on an incoming metallic domestic water supply pipe must the main protective bonding connection clamp be fitted?",
         "根據 BS 7671 規範，入戶自來水金屬水管的主等電位接地夾，必須精確安裝在何處？",
         {"A": "Upstairs on the bathroom shower rose", "B": "Within 600mm of the internal water meter or point of entry into the building, BEFORE any branch pipework, and on hard bare metal downstream of the main stopcock", "C": "Outside under the street pavement", "D": "Inside the hot water cylinder"},
         {"A": "在二樓浴室淋浴花灑噴頭處", "B": "在室內水表或管道穿入建築物室內牆皮點「600mm (0.6 米) 範圍以內」，且必須在任何分支分流管道之前、在主水閥下游的裸露乾淨金屬管壁上牢牢卡緊！", "C": "在室外公共街道馬路的人行道石板下", "D": "熱水儲水水罐內部"},
         "B", "Regulation 544.1.2: Main bonding must be within 600mm of point of entry or internal meter, before any branch pipe. This ensures that opening a downstream fitting cannot sever the property's primary earthing path.", "入戶 600mm 禁分叉原則必考：主地線必須卡在進屋水管 60 公分之內，且必須在分叉出第一個三通之前！否則萬一以後有人鋸斷了後面某個水龍頭，整棟樓的接地保護全被扯斷了！必須在源頭牢牢鎖死！", "BS 7671:2018 Regulation 544.1.2; C&G Unit 208"),

        ("11.4",
         "What statutory safety warning label must be permanently displayed at every BS 951 pipe earthing bonding clamp connection?",
         "在每個符合 BS 951 標準的管道接地金屬抱箍夾旁，必須強制永久懸掛何種法定的金屬/塑料警告安全標籤牌？",
         {"A": "'Danger: High Voltage Electricity'", "B": "'Safety Electrical Connection - Do Not Remove' (embossed or stamped clearly on an embossed metal/plastic tag)", "C": "'Turn Off After Use'", "D": "'Hot Surface Do Not Touch'"},
         {"A": "「危險：高壓電」", "B": "「安全電氣連接 - 嚴禁拆除 (Safety Electrical Connection - Do Not Remove)」(字樣清晰凸印在專用金屬標牌或耐候塑料吊牌上)", "C": "「使用後請隨手關閉」", "D": "「高溫表面，請勿觸摸」"},
         "B", "Regulation 514.13.1 mandates the standardized wording: 'Safety Electrical Connection - Do Not Remove' at all bonding points, warning homeowners and decorators not to undo the critical safety clamp.", "接地警告牌八個大字必考：水管接地夾上必須掛著小銅牌，印著「Safety Electrical Connection - Do Not Remove」！就是警告不懂電的業主和裝修油漆工，千萬別手欠把它當廢鐵絲拆了，拆了會死人！", "BS 7671:2018 Regulation 514.13.1; BS 951 Clamps for earthing and bonding"),

        ("11.4",
         "Why must a plumber ALWAYS attach a 'Temporary Earth Continuity Bonding Strap' across a section of metal pipework BEFORE cutting it with a pipe cutter or hacksaw?",
         "為什麼水暖技師在用割刀或鋼鋸切斷任何金屬水管/燃氣管之前，必須「強制在切割點兩側跨接一根臨時等電位跨接導線 (Temporary Continuity Strap)」？",
         {"A": "To keep the pipe warm", "B": "If an electrical fault exists or circulating neutral current is flowing through the metallic pipework, cutting the pipe breaks the path; without a bypass strap, the plumber's body bridges the gap and suffers a fatal 230V electric shock", "C": "To prevent water splashing on boots", "D": "To sharpen the hacksaw blade"},
         {"A": "為切割部位的銅管保溫防凍", "B": "若房屋存在未察覺的電氣漏電故障或電網零線電流正借道金屬水管流向大地，切斷水管會瞬間打斷電流通路；若無臨時跨接線，水暖工兩隻手分別抓著切口兩端，人體直接充當導線承受 230V 穿心電流當場被電死！", "C": "防止管內存水噴濺打濕施工工鞋", "D": "自動打磨鋒利鋼鋸條的鋸齒"},
         "B", "Plumbing safety rule: Severing a pipe breaks earth continuity. If stray current is flowing, the voltage bridges across the open gap. A temporary jump-lead bonds the two halves, keeping the plumber alive.", "鋸水管救命跨接線必考：很多水暖工慘死在水管上！因為水管連著地線，鄰居家漏電可能正順著你家水管跑。你拿鋼鋸把管子一鋸開，兩截管子中間有 230V 壓差，你的胸口和手就是導線，當場電死在水槽下！先夾好跨接線再鋸管！", "HSE Guidance Note PM29 Electrical hazards on pipes; C&G Unit 208"),

        ("11.4",
         "Under what conditions does the 18th Edition of BS 7671 permit the omission of Supplementary Bonding in a domestic bathroom?",
         "根據 BS 7671（第 18 版）法規鬆綁條款，在何種嚴格前提條件下，家庭浴室內部允許「免除額外安裝輔助等電位跨接線 (Supplementary Bonding)」？",
         {"A": "If the bathroom has wooden floorboards only", "B": "If all final circuits in the bathroom are protected by 30mA RCDs (with disconnection under 40ms) AND all extraneous metal parts are effectively bonded back to the Main Earthing Terminal", "C": "If there is no shower in the room", "D": "Supplementary bonding is always illegal"},
         {"A": "只要浴室鋪設了純實木木地板", "B": "只要浴室內的所有低壓供電迴路均已全面配備「30mA 漏電保護器 (RCD)」防護、且全屋所有外露金屬水管等均已可靠連入總等電位聯結主接地網！", "C": "只要該浴室內不安裝淋浴花灑", "D": "輔助等電位在任何情況下均被法律禁止安裝"},
         "B", "Regulation 701.415.2 permits omitting bathroom supplementary bonding IF: 1. All bathroom circuits have 30mA RCD protection; 2. Main protective bonding is in place; 3. Earth continuity resistance is verified.", "第 18 版浴室地線鬆綁條款：以前裝修要把浴缸、水龍頭、金屬管全拉綠黃明線串起來，奇醜無比。現在新法規規定：只要配電箱裡全裝了 30mA 漏保（RCD），且入戶總水管接地完好，浴室裡就不用再拉明地線了！", "BS 7671:2018 Regulation 701.415.2; C&G Unit 208"),

        # 11.5 Overcurrent Devices, RCDs & Fuses
        ("11.5",
         "What is the operational function of a Residual Current Device (RCD conforming to BS EN 61008) fitted inside a domestic consumer unit?",
         "安裝在家用配電箱（Consumer Unit）內部的「剩餘電流動作保護器 (RCD - 符合 BS EN 61008)」，其核心觸電保護功能是什麼？",
         {"A": "To measure electricity consumption in units", "B": "It continuously monitors and balances the current in the Line and Neutral conductors; if an imbalance (earth leakage) of 30mA is detected (e.g. current leaking through a human body to ground), it trips and cuts power within 40 milliseconds", "C": "To keep the cables cold", "D": "To increase mains voltage to 400V"},
         {"A": "精確計量家庭每月的用電度數", "B": "實時嚴密比對火線（Line）流出與零線（Neutral）流回的電流矢量平衡；一旦發現流出流回電流差值達到 30mA（意味著有電流正穿過人體或絕緣破損洩漏入大地），在 40 毫秒內瞬間自動跳閘切斷電源！", "C": "為配電箱內部的銅導線散熱降溫", "D": "將市電電壓強行升高到 400V"},
         "B", "RCDs operate on current imbalance (Kirchhoff's law). If current leaving via Line does not return via Neutral, it is leaking to Earth. A 30mA RCD disconnects within 40ms, saving lives from cardiac fibrillation.", "RCD 漏電保護器救命毫秒差：火線出去 10 安培，零線就必須回來 10 安培。如果零線只回來 9.97 安培，差了 30mA 跑哪去了？正穿過摸電線的人流進了泥地！RCD 在 40 毫秒（0.04秒，人還沒反應過來）內瞬間彈開切斷電源，保住性命！", "BS EN 61008; BS 7671 Regulation 411.3.3"),

        ("11.5",
         "Under BS EN 60898, what are the tripping characteristics of a 'Type B' and a 'Type C' Miniature Circuit Breaker (MCB) respectively?",
         "根據 BS EN 60898 標準，家用配電箱中的「Type B 型」與「Type C 型」微型微型斷路器（MCB）在瞬時磁脫扣倍數上有何區別？",
         {"A": "Type B is for battery; Type C is for copper", "B": "Type B trips magnetically at 3 to 5 times full rated current (ideal for domestic resistive heating and lighting); Type C trips at 5 to 10 times rated current (designed for inductive motor loads with high inrush currents e.g. heat pumps)", "C": "Type B never trips; Type C trips every 5 minutes", "D": "Type B is 12V; Type C is 10,000V"},
         {"A": "Type B 專門用於蓄電池；Type C 專門用於紫銅導線", "B": "Type B 型在額定電流的「3 至 5 倍」時瞬時磁跳閘（適用於家庭普通純電阻性採暖與常規照明）；Type C 型在「5 至 10 倍」時瞬時磁脫扣（專為具備較大啟動衝擊電流的感性電機設備，如空氣源熱泵、大功率增壓水泵設計）", "C": "Type B 終身永不跳閘；Type C 每隔 5 分鐘跳閘一次", "D": "Type B 額定 12V；Type C 額定 10,000V"},
         "B", "Type B (3-5x In) handles domestic resistive circuits without nuisance tripping. Type C (5-10x In) tolerates the brief inductive inrush surge when heat pump compressors or motor pumps start up.", "空開 B 型與 C 型選型考點：普通電暖器電燈用 B 型空開（靈敏度高，超載 3-5 倍立刻跳）；但熱泵壓縮機、大水泵啟動瞬間電機線圈有巨大衝擊電流（啟動浪涌），用 B 型會一開機就跳！必須換 C 型空開（抗 5-10 倍浪涌不誤跳）！", "BS EN 60898-1; BS 7671 Section 411; C&G Unit 208"),

        ("11.5",
         "What is an 'RCBO' (BS EN 61009) installed in modern domestic consumer units?",
         "現代家庭配電箱中廣泛採用的「RCBO (複合型漏電斷路器 - 符合 BS EN 61009)」，集成了哪兩大保護裝置的雙重功能？",
         {"A": "A radio transmitter and clock", "B": "A single modular device combining the overcurrent/short-circuit protection of an MCB with the earth leakage protection of an RCD in one single din-rail module", "C": "A manual light switch and bell", "D": "A fuse and battery"},
         {"A": "無線電廣播收音機與電子時鐘", "B": "將微型斷路器（MCB）的過載短路保護、與漏電保護器（RCD）的接地漏電保護「二合一完美集成」在單個標準導軌模塊內的獨立全功能保護斷路器", "C": "手動照明開關與門鈴", "D": "保險絲與充電電池複合體"},
         "B", "An RCBO merges an MCB and an RCD. If a fault occurs on one circuit (e.g. immersion heater leaks to earth), only that individual RCBO trips, leaving lighting and freezers running across all other circuits.", "RCBO 獨立二合一神器：以前半個配電箱共用一個大 RCD，一個插座漏電，全家跳閘陷入黑暗、冰箱化凍！RCBO 是一路一個獨立保險箱：兼具過載 + 漏電雙重功能，哪路出事只跳哪一路，絕不株連全屋其他電器！", "BS EN 61009 Residual current operated circuit-breakers with integral overcurrent protection"),

        ("11.5",
         "What fuse rating is universally specified inside the 13A switched Fused Connection Spur (FCU) supplying a domestic central heating gas boiler and its external controls?",
         "在家庭中央採暖燃氣壁掛爐及其外部溫控聯動電路的專用 13A 熔斷保護接線盒（Fused Spur）內部，全英標準指定的保險絲管額定電流是多少？",
         {"A": "A 3-Ampere cartridge fuse (BS 1362)", "B": "A 100-Ampere fuse", "C": "A 32-Ampere fuse", "D": "No fuse is required"},
         {"A": "3 安培 (3A) 專用陶瓷管保險絲 (符合 BS 1362 標準)", "B": "100 安培重載保險絲", "C": "32 安培大容量保險絲", "D": "完全不需要安裝任何保險絲"},
         "A", "Boiler manufacturers and BS 7671 dictate that central heating controls and boilers must be protected by a 3A fuse. A 13A fuse will not blow quickly enough to protect sensitive PCB electronics during an internal short.", "壁掛爐 3A 保險絲鐵律必考：壁掛爐開關盒外表雖然是個 13A 盒子，但肚子裡必須裝「3 安培（3A，紅色小保險絲）」！壁掛爐主板全是微電子芯片，若無知換成 13A 粗保險絲，短路時主板直接燒穿化成灰保險絲都不斷！必須嚴格 3A！", "BS 1362; BS 7671; Domestic Heating Design Guide; C&G Unit 208")
    ]

    for sub_id, stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref in data:
        questions.append(make_q(11, sub_id, ["Unit_208"], stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref))

    from .ch11_part2 import get_part2_questions
    questions.extend(get_part2_questions())

    return questions
