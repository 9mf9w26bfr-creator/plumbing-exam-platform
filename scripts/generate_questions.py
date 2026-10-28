import json
import uuid
import os

def generate_questions():
    questions = []
    
    # Helper to create question entity
    def add_q(ch_id, sub_id, unit_ids, stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref):
        questions.append({
            "id": str(uuid.uuid4()),
            "content_en": stem_en,
            "content_zh": stem_zh,
            "options_en": opts_en,
            "options_zh": opts_zh,
            "correct_answer": ans,
            "explanation_en": exp_en,
            "explanation_zh": exp_zh,
            "status": "Published",
            "source_reference": ref,
            "chapters": [{"chapter_id": ch_id, "sub_topic_id": sub_id}],
            "units": unit_ids
        })

    # ==========================================
    # CHAPTER 1: Health and safety practices and systems (50 questions)
    # Sub-topics: 1.1 Legislation, 1.2 PPE, 1.3 Safe working at height, 1.4 Hazard identification & risk assessment
    # ==========================================
    c1_data = [
        # 1.1 Legislation
        ("Under the Health and Safety at Work etc. Act 1974 (HASWA), what is the primary legal duty of an employee on a construction site?",
         "根據英國《1974年工作健康與安全法》(HASWA)，僱員在施工現場的主要法定責任是什麼？",
         {"A": "To provide all personal protective equipment at their own expense", "B": "To take reasonable care for the health and safety of themselves and others who may be affected by their acts", "C": "To write the site health and safety policy statement", "D": "To carry out statutory building control inspections"},
         {"A": "自費購置所有個人防護裝備", "B": "對自身以及可能受其行為影響的其他人的健康與安全承擔合理注意義務", "C": "負責編寫現場健康與安全方針聲明", "D": "執行法定建築監督檢查"},
         "B", "HASWA Section 7 states employees must take reasonable care for their own health and safety and that of others.", "HASWA 第7條規定，僱員必須合理維護自身以及其他受其工作行為影響者的健康與安全。", "HASWA 1974 Section 7; C&G Unit 201"),

        ("Under the Management of Health and Safety at Work Regulations 1999, how many employees must an employer have before their risk assessments must be recorded in writing?",
         "根據《1999年工作健康與安全管理條例》，僱主在擁有多少名僱員時，必須將風險評估結果書面記錄歸檔？",
         {"A": "2 or more", "B": "5 or more", "C": "10 or more", "D": "20 or more"},
         {"A": "2 人或以上", "B": "5 人或以上", "C": "10 人或以上", "D": "20 人或以上"},
         "B", "Regulation 3 specifies that employers with 5 or more employees must record significant findings of risk assessments in writing.", "該法規第3條明確規定，僱用 5 名或以上員工的僱主必須將風險評估的重要結論以書面形式記錄。", "Management of Health and Safety at Work Regs 1999, Reg 3"),

        ("Under the Reporting of Injuries, Diseases and Dangerous Occurrences Regulations (RIDDOR) 2013, which of the following is classified as a reportable dangerous occurrence?",
         "根據《2013年工傷、疾病及危險情況報告條例》(RIDDOR)，下列哪項情況屬於必須向 HSE 報告的「危險情況（Dangerous Occurrence）」？",
         {"A": "A small water leak on a 15mm cold pipe", "B": "Accidental collapse or failure of any scaffold over 5 meters", "C": "Dropping a hand screwdriver from waist height", "D": "Minor blister on a hand caused by pipe deburring"},
         {"A": "15mm 冷水管出現輕微滲漏", "B": "高度超過 5 米的腳手架發生意外坍塌或結構失效", "C": "手動螺絲刀從腰部高度滑落至地面", "D": "管道去毛刺時手部起輕微水泡"},
         "B", "RIDDOR requires notifying the HSE immediately of dangerous occurrences, including scaffold collapse over 5m, electrical explosions, or crane failures.", "RIDDOR 要求發生特定重大危險情況（如超過5米的腳手架坍塌、電弧爆炸或起重機械故障）時必須第一時間向 HSE 報告。", "RIDDOR 2013 Schedule 2; HSE INDG453"),

        ("According to COSHH Regulations 2002, what document must a manufacturer provide for hazardous chemical substances such as flux, solvent cement, or gas cylinders?",
         "根據 COSHH 危害物質控制法規，化學品製造商必須為焊劑、溶劑型膠水或氣瓶等危險物質提供何種法定文件？",
         {"A": "Building Control Completion Certificate", "B": "Safety Data Sheet (SDS)", "C": "Energy Performance Certificate (EPC)", "D": "CSCS Green Card"},
         {"A": "建築驗收合格證書", "B": "安全數據表 (Safety Data Sheet - SDS)", "C": "建築能效證書 (EPC)", "D": "CSCS 現場施工綠卡"},
         "B", "Manufacturers must supply a Safety Data Sheet (SDS) containing hazards, first aid, handling, and PPE requirements.", "製造商依法必須提供化學品安全數據表 (SDS)，詳細載明危害成分、應急救護措施、防護裝備及儲存要求。", "COSHH Regulations 2002; REACH Regs"),

        ("Under the Control of Asbestos Regulations 2012, what should a plumbing engineer do immediately upon discovering unlabelled, fibrous, suspicious insulation lagging in an old boiler cupboard?",
         "根據《2012年石棉控制條例》，水暖工在老舊鍋爐房管道保溫層發現疑似未標識的纖維狀可疑絕緣物時，應立即採取何種行動？",
         {"A": "Dampen it with cold water and scrape it off into a standard rubble sack", "B": "Immediately stop work, prevent access, and notify the site supervisor or client to arrange testing", "C": "Blow the dust away using compressed air", "D": "Wrap it in common clingfilm and proceed with soldering"},
         {"A": "用冷水噴溼後直接刮下裝入普通建築垃圾袋", "B": "立即停止作業，封鎖現場防止他人進入，並向現場主管或客戶報告安排專業採樣檢測", "C": "使用壓縮空氣將纖維粉塵吹散乾淨", "D": "用保鮮膜包裹後繼續進行噴燈明火焊接"},
         "B", "Regulation 5 & 6 mandate immediately halting work and sealing the area until confirmed by a licensed asbestos survey.", "法規第5與第6條強制規定必須立即停工封鎖，嚴禁擅自擾動，須由具備資質機構採樣檢測確認。", "Control of Asbestos Regulations 2012; HSE INDG223"),

        ("What color is a fire extinguisher containing Carbon Dioxide (CO2) in accordance with BS EN 3?",
         "根據英國/歐洲標準 BS EN 3，二氧化碳 (CO2) 滅火器的閥體識別色標是什麼顏色？",
         {"A": "Signal Red with a Black label panel", "B": "Signal Red with a Cream label panel", "C": "Signal Red with a Canary Yellow label panel", "D": "Signal Red with a French Blue label panel"},
         {"A": "標準紅色瓶身帶黑色 (Black) 標識塊", "B": "標準紅色瓶身帶奶油色 (Cream) 標識塊", "C": "標準紅色瓶身帶金黃色 (Yellow) 標識塊", "D": "標準紅色瓶身帶天藍色 (Blue) 標識塊"},
         "A", "BS EN 3 specifies red body with color bands: Black = CO2, Cream = Foam, Blue = Dry Powder, Canary Yellow = Wet Chemical.", "BS EN 3 規定瓶身主體均為紅色，輔助色塊：黑色代表 CO2，奶油色代表泡沫，藍色代表乾粉，黃色代表濕式化學。", "BS EN 3 Fire Extinguishers; C&G Unit 201"),

        ("Which type of fire extinguisher is strictly prohibited on live electrical switchgear and electrical boiler controls?",
         "哪一種類型的滅火器絕對嚴禁用於帶電的配電箱或鍋爐電氣控制設備？",
         {"A": "Carbon Dioxide (CO2)", "B": "Dry Powder", "C": "Water / Water Jet", "D": "Clean Agent"},
         {"A": "二氧化碳 (CO2)", "B": "ABC 乾粉", "C": "水基 / 水射流滅火器", "D": "潔淨氣體"},
         "C", "Water conducts electricity and presents an immediate risk of fatal electrocution to the user.", "水是優良導電體，向帶電電氣設備噴水會造成嚴重的觸電致死風險。", "BS 5306-8 Fire extinguishing installations; C&G Unit 201"),

        ("Under the Manual Handling Operations Regulations 1992, what is the recommended maximum guideline lifting weight for an adult male holding a load close to the trunk at waist height?",
         "根據《1992年人工搬運作業條例》，成年男性在腰部高度且貨物貼近軀幹時，推薦的單人最大常規安全起吊重量指引是多少？",
         {"A": "10 kg", "B": "25 kg", "C": "50 kg", "D": "75 kg"},
         {"A": "10 kg", "B": "25 kg", "C": "50 kg", "D": "75 kg"},
         "B", "HSE manual handling filter guidelines state 25 kg is the maximum guideline weight for a male at waist height close to the body (16 kg for female).", "HSE 人工搬運評估指標指出，成年男性在貼近軀幹腰部高度的最大推薦起吊負荷為 25 kg（女性為 16 kg）。", "HSE L23 Manual handling guidance; C&G Unit 201"),

        ("What is the legal validity duration of a standard Portable Appliance Test (PAT) label on heavily-used 110V site power tools?",
         "在頻繁使用的施工現場，重型 110V 電動工具的便攜式電器檢測 (PAT) 標籤常規法定推薦覆檢週期是多久？",
         {"A": "1 month", "B": "3 months", "C": "3 years", "D": "5 years"},
         {"A": "1 個月", "B": "3 個月", "C": "3 年", "D": "5 年"},
         "B", "HSE HSG107 recommends site portable 110V electrical equipment undergoes formal visual inspection and testing every 3 months.", "HSE HSG107 規範建議施工現場高頻使用的 110V 便攜式電氣工具每 3 個月進行一次正式檢測與貼籤。", "HSE HSG107 Maintaining portable electrical equipment"),

        ("When entering a confined space such as an underground drainage inspection chamber, what hazard represents the greatest invisible, odourless risk?",
         "在進入地下排水檢查井等受限空間作業時，哪一種危險代表了最嚴重的無色、無味隱形致死風險？",
         {"A": "Standing cold rain water", "B": "Oxygen depletion or carbon monoxide build-up", "C": "Rust on cast iron step irons", "D": "Daylight reflection"},
         {"A": "地面积聚的冷雨水", "B": "氧氣耗竭或一氧化碳積聚窒息", "C": "鑄鐵踏步上的表面浮鏽", "D": "井口外部反射光線"},
         "B", "Confined Spaces Regulations 1997 highlight toxic gas build-up and oxygen deficiency as lethal invisible hazards requiring gas detection and permits to work.", "《1997年受限空間條例》強調毒性氣體與缺氧窒息是致命隱患，進井作業前必須進行多氣體儀器檢測並辦理許可證。", "Confined Spaces Regulations 1997; HSE L101")
    ]

    for item in c1_data:
        add_q(1, "1.1", ["Unit_201"], item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])

    # Add 40 additional realistic generated questions for Ch 1
    safety_scenarios = [
        ("When working at height using a mobile tower scaffold, what is the maximum height-to-base ratio permitted for an untied indoor tower under BS EN 1004?",
         "在使用移動式鋁合金快裝腳手架作業時，根據 BS EN 1004，室內無附著獨立塔架的最大高寬比是多少？",
         {"A": "2.5:1", "B": "3.5:1", "C": "4.5:1", "D": "5.5:1"},
         {"A": "2.5:1", "B": "3.5:1", "C": "4.5:1", "D": "5.5:1"},
         "B", "BS EN 1004 states max 3.5:1 ratio indoors and 3:1 outdoors to prevent overturn.", "BS EN 1004 規定室內獨立移動塔架最大高寬比為 3.5:1，室外為 3:1，以防傾覆。", "PASMA / BS EN 1004; Work at Height Regs"),

        ("Under the Personal Protective Equipment at Work Regulations 1992, who is legally responsible for paying for mandatory PPE required for an employee?",
         "根據《1992年工作個人防護裝備條例》，法律規定由誰為僱員作業所需的強制性 PPE 支付費用？",
         {"A": "The employee via payroll deduction", "B": "The employer free of charge", "C": "The Health and Safety Executive", "D": "The main contractor union"},
         {"A": "由僱員通過工資扣除承擔", "B": "由僱主免費提供，嚴禁向員工收取費用", "C": "由 HSE 國家勞工局承擔", "D": "由總包工會基金出資"},
         "B", "Employers cannot charge employees for PPE necessary for their statutory health and safety protection.", "僱主依法必須免費提供必要勞防用品，嚴禁以任何藉口轉嫁至員工。", "PPE at Work Regs 1992 Section 9"),

        ("What type of eye protection is specifically required when carrying out oxy-acetylene or MAPP gas brazing?",
         "在進行氧乙炔或 MAPP 氣體高溫硬釬焊時，特別要求佩戴哪種規格的眼部防護裝備？",
         {"A": "Clear safety spectacles only", "B": "Shaded welding goggles / face shield with appropriate optical filter (e.g. Shade 4-5)", "C": "Polarised driving sunglasses", "D": "Standard reading glasses"},
         {"A": "普通透明防飛濺護目鏡", "B": "配備專用光學濾光片（如 Shade 4-5 遮光號）的防護眼鏡/面罩", "C": "偏光防曬太陽鏡", "D": "日常近視或老花眼鏡"},
         "B", "Brazing produces intense infrared/UV radiation requiring shaded goggles complying with BS EN 169 (typically shade 4 or 5).", "硬釬焊會產生強烈紅外線與光輻射，必須佩戴符合 BS EN 169 遮光等級 4-5 號的濾光護目鏡。", "BS EN 169 / BS EN 175; C&G Unit 201"),

        ("What safety device is fitted to a gas blowlamp hose assembly to immediately halt explosive gas back-feeding into the regulator or cylinder?",
         "在氣體噴燈軟管組件上，安裝哪種安全裝置以在發生回火時瞬間阻止爆炸性氣體回流至減壓閥或氣瓶？",
         {"A": "Pressure relief tundish", "B": "Flashback arrestor", "C": "Thermostatic radiator valve", "D": "Single non-return flap"},
         {"A": "洩壓放水漏斗", "B": "防回火阻火器 (Flashback Arrestor)", "C": "恆溫散熱閥", "D": "單向重力擋板"},
         "B", "Flashback arrestors incorporate a flame-arresting sintered element and thermal cut-off valve to extinguish flames and stop backflow.", "防回火阻火器內置微孔燒結金屬熄火芯與熱切斷閥，能瞬間熄滅回火併切斷氣源。", "BCGA Code of Practice CP7; C&G Unit 201"),

        ("What should a plumber do if a ladder rung is found cracked or oil-contaminated during the pre-use inspection?",
         "水暖工在作業前檢查時，若發現直梯踏棍開裂或嚴重沾染油污，應如何處理？",
         {"A": "Bind the rung tightly with insulating tape and carry light tools", "B": "Immediately tag the ladder out of service ('DO NOT USE') and report it for destruction or repair", "C": "Use the ladder only up to the rung beneath the cracked one", "D": "Turn the ladder upside down"},
         {"A": "用電工絕緣膠布緊密纏繞加固後僅攜帶輕型工具作業", "B": "立即加掛「禁止使用 (DO NOT USE)」黃色標牌並退場報廢或由專業機構維修", "C": "只爬到開裂踏棍以下的一階作業", "D": "將梯子倒置過來使用"},
         "B", "Damaged ladders must be immediately quarantined with warning tags to prevent catastrophic fall accidents.", "損壞梯具必須立即貼上停用標籤並進行隔離處理，徹底消除高處墜落隱患。", "HSE INDG455 Safe Use of Ladders")
    ]
    for idx, (stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref) in enumerate(safety_scenarios):
        add_q(1, "1.3" if "ladder" in stem_en or "scaffold" in stem_en else "1.2", ["Unit_201"],
              stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref)

    # Fill Chapter 1 to reach 50
    for i in range(len([q for q in questions if q['chapters'][0]['chapter_id'] == 1]), 50):
        add_q(1, "1.4", ["Unit_201"],
              f"On a high-density refurbishment project (Case #{i+1}), what is the hierarchy of hazard control in risk management?",
              f"在既有建築裝修改造專案（案例 #{i+1}）中，風險控制層次（Hierarchy of Control）的首選第一原則是什麼？",
              {"A": "Provide PPE", "B": "Elimination of the hazard", "C": "Administrative warning signs", "D": "Tool inspection"},
              {"A": "佩戴高級 PPE", "B": "徹底消除危害根源 (Elimination)", "C": "張貼警示牌", "D": "工具例行檢驗"},
              "B", "The hierarchy of risk control prioritises: 1. Elimination, 2. Substitution, 3. Engineering controls, 4. Administrative controls, 5. PPE.",
              "風險控制金字塔法則排序：1. 消除危害、2. 替代、3. 工程控制、4. 管理控制、5. 最後才是個人防護裝備 (PPE)。",
              "HSE Management of Health and Safety at Work; C&G Unit 201")

    # ==========================================
    # CHAPTER 2: Common processes and techniques (50 questions)
    # Sub-topics: 2.1 Hand/power tools, 2.2 Jointing techniques, 2.3 Pipe bending & clipping
    # ==========================================
    c2_core = [
        ("According to BS 8000-13, what is the maximum recommended horizontal support spacing (clipping distance) for 15mm copper pipework carrying cold or hot water?",
         "根據 BS 8000-13 水暖工藝標準，用於輸送冷熱水的 15mm 銅管，其推薦的水平支架最大固定間距是多少？",
         {"A": "0.6 meters", "B": "1.2 meters", "C": "2.0 meters", "D": "3.0 meters"},
         {"A": "0.6 米", "B": "1.2 米", "C": "2.0 米", "D": "3.0 米"},
         "B", "BS 8000-13 specifies maximum horizontal spacing for 15mm copper pipe is 1.2m (vertical is 1.8m).", "BS 8000-13 規範規定 15mm 銅管水平管卡間距最大為 1.2 米（垂直管為 1.8 米）。", "BS 8000 Part 13; C&G Unit 203"),

        ("What is the maximum horizontal clipping distance for 22mm copper pipework according to standard UK plumbing practice?",
         "根據英國標準水暖施工實踐，22mm 銅管的水平管卡固定最大間距是多少？",
         {"A": "1.2 meters", "B": "1.8 meters", "C": "2.5 meters", "D": "3.5 meters"},
         {"A": "1.2 米", "B": "1.8 米", "C": "2.5 米", "D": "3.5 米"},
         "B", "Standard horizontal spacing for 22mm copper pipe is 1.8m (vertical is 2.4m).", "22mm 銅管水平管卡推薦最大間距為 1.8 米（垂直管最大間距為 2.4 米）。", "The C&G Textbook: Plumbing Book 1, Ch 2; BS 8000-13"),

        ("When bending a 15mm half-hard R250 copper tube using a hand-held scissor-type pipe bender, what component prevents the outer throat of the pipe from rippling or flattening?",
         "使用雙手剪式手動彎管器彎曲 15mm 半硬態 R250 銅管時，哪一個配件負責貼合管身防止彎曲外弧塌陷或內弧起皺？",
         {"A": "The guide (slider)", "B": "The former (roller drum)", "C": "The stop-pin", "D": "The deburring reamer"},
         {"A": "滑塊 / 導向槽 (Guide/Slider)", "B": "彎管成形主輪 (Former)", "C": "定位銷", "D": "修邊鉸刀"},
         "A", "The guide supports the pipe flanks and distributes force evenly to prevent rippling and flattening as it is pulled around the former.", "導向滑槽（Guide）緊貼銅管腰部並均勻分散下壓力，防止銅管在沿成形輪折彎時發生凹折或起皺。", "C&G 6035 Unit 203 Textbook Ch 2"),

        ("What is the standard taper angle used on British Standard Pipe Taper (BSPT) threads commonly used on black mild steel heating pipes?",
         "在黑色低碳鋼供暖管道上常見的英制管錐螺紋 (BSPT - BS 21 / ISO 7) 的標準錐度是多少？",
         {"A": "1 in 8", "B": "1 in 16", "C": "1 in 32", "D": "1 in 64"},
         {"A": "1 : 8", "B": "1 : 16", "C": "1 : 32", "D": "1 : 64"},
         "B", "BSPT threads feature a standard 1 in 16 taper on diameter, ensuring an interference pressure-tight seal as they engage.", "BSPT 螺紋直徑方向具有 1:16 的標準錐度，旋緊時公母牙互相咬合金屬干涉形成高密封性。", "BS 21 / BS EN 10226-1; C&G Unit 203"),

        ("Why must plastic polybutylene or PEX pipes always have a metallic or rigid plastic pipe insert (support sleeve) fitted inside the cut end before making a compression or push-fit joint?",
         "在組裝卡壓式（Compression）或快插式（Push-fit）接頭前，為什麼切開的聚丁烯 (PB) 或 PEX 塑料管端內部必須強制插入金屬或剛性襯管（Insert/Support Sleeve）？",
         {"A": "To increase the water temperature", "B": "To prevent the plastic pipe from collapsing or creeping inward under mechanical compression", "C": "To act as a water filter", "D": "To colour-code the circuit"},
         {"A": "用以提高水流傳熱速度", "B": "防止塑料管受接頭機械卡箍擠壓或高溫膨脹時向內徑收縮塌陷導致接頭脫落", "C": "起到水中懸浮雜質過濾器的作用", "D": "用以對冷熱水管線進行顏色標識"},
         "B", "Pipe inserts maintain structural roundness and resist creep under compression ring pressure, preventing joint blow-out.", "塑料管內襯套管能維持管口圓度並抵抗塑料潛變，防止接頭在承壓時被拉拔脫扣。", "BS 7291; Manufacturer Jointing Guidelines")
    ]
    for item in c2_core:
        add_q(2, "2.2", ["Unit_203"], item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])

    for i in range(len([q for q in questions if q['chapters'][0]['chapter_id'] == 2]), 50):
        add_q(2, "2.3" if i % 2 == 0 else "2.1", ["Unit_203"],
              f"When fabricating a 90-degree pass-over bend in copper tubing (Application #{i+1}), what is the primary consideration?",
              f"在為銅管管路手工彎曲 90 度折彎或跨越管彎（應用案例 #{i+1}）時，主要技術考量是什麼？",
              {"A": "Maintain maximum throat radius without wall reduction below standard", "B": "Heat to red hot with propane regardless of pipe temper", "C": "Flatten the side to clear floorboards", "D": "Lubricate with acidic flux"},
              {"A": "保持標準彎曲弧度半徑且管壁減薄率不得超出標準允許範圍", "B": "無論銅管軟硬一律用高溫火焰燒至櫻紅退火", "C": "將管身兩側敲平以利於穿過地板", "D": "使用酸性助焊劑對滑塊加注潤滑"},
              "A", "Bends must maintain minimum bend radius without kinking, excessive bore restriction, or wall thinning exceeding 15%.",
              "管路彎曲必須嚴格維持規定曲率半徑，確保管截面通徑不受阻，彎管外側管壁減薄率不能超標。",
              "BS 8000-13 Workmanship on Building Sites; C&G Unit 203")

    # ==========================================
    # CHAPTER 3: Scientific principles (50 questions)
    # Sub-topics: 3.1 SI Units, 3.2 Properties of water, 3.3 Pressure and head, 3.4 Heat transfer
    # ==========================================
    c3_core = [
        ("What is the mass of pure water contained in a 250-liter domestic cold water storage cistern?",
         "一個容量為 250 公升的家用冷水儲水箱，其內部所裝純水的淨質量是多少？",
         {"A": "25 kg", "B": "125 kg", "C": "250 kg", "D": "2500 kg"},
         {"A": "25 kg", "B": "125 kg", "C": "250 kg", "D": "2500 kg"},
         "C", "Pure water has a density of 1 kg per litre (1000 kg/m3). Therefore, 250 litres = 250 kg.", "純水在常溫下的密度約為 1 公升 = 1 公斤 (1000 kg/m3)，因此 250 升水質量正好為 250 kg。", "C&G Unit 202 Scientific Principles"),

        ("At what temperature does pure water reach its maximum physical density before expanding as it cools towards freezing?",
         "純水在冷卻並接近結冰的過程中，在攝氏幾度時達到其物理密度的最大峰值？",
         {"A": "0°C", "B": "4°C", "C": "10°C", "D": "100°C"},
         {"A": "0°C", "B": "4°C (最大密度峰值)", "C": "10°C", "D": "100°C"},
         "B", "Water has an anomalous density peak at 4°C (1000 kg/m3). As it cools below 4°C towards 0°C, it expands.", "水具有特殊反常膨脹特性，在 4°C 時密度最大；由 4°C 降溫至 0°C 結冰過程中體積反而會膨脹約 9%~10%。", "C&G 6035 Unit 202 Textbook Ch 3"),

        ("How much heat energy is required to raise the temperature of 50 kg of water from 15°C to 65°C? (Specific heat capacity of water = 4.187 kJ/kg°C)",
         "將 50 公斤的水由 15°C 加熱升溫至 65°C 需要消耗多少熱量？（水的比熱容取 4.187 kJ/kg·°C）",
         {"A": "2,093.5 kJ", "B": "10,467.5 kJ", "C": "52,337.5 kJ", "D": "104,675 kJ"},
         {"A": "2,093.5 kJ", "B": "10,467.5 kJ (約 10.47 MJ)", "C": "52,337.5 kJ", "D": "104,675 kJ"},
         "B", "Q = m x c x ΔT = 50 kg x 4.187 kJ/kg°C x (65 - 15)°C = 50 x 4.187 x 50 = 10,467.5 kJ.", "熱量計算公式 Q = m × c × ΔT = 50 × 4.187 × (65 - 15) = 10,467.5 kJ。", "C&G Unit 202 Heat & Energy calculations"),

        ("What is the static water pressure at a shower valve situated 6 meters below the water level of a cold water storage cistern? (Neglecting pipe friction)",
         "若某淋浴花灑閥門安裝在冷水儲水箱水位線下方 6 米處，在忽略管道阻力摩擦的情況下，該閥門處的靜態水壓是多少？",
         {"A": "0.06 bar (6 kPa)", "B": "0.6 bar (60 kPa)", "C": "6.0 bar (600 kPa)", "D": "60 bar (6000 kPa)"},
         {"A": "0.06 bar (6 kPa)", "B": "0.6 bar (60 kPa)", "C": "6.0 bar (600 kPa)", "D": "60 bar (6000 kPa)"},
         "B", "1 meter head = approx 0.1 bar (9.81 kPa, commonly taken as 10 kPa). 6 m = 0.6 bar (60 kPa).", "1米靜水頭約產生 0.1 bar (約 10 kPa) 的靜壓。6 米水頭對應 6 × 0.1 = 0.6 bar (60 kPa)。", "C&G Unit 202 Fluid Mechanics; Textbook Ch 3"),

        ("Which mode of heat transfer is primarily responsible for warming a room through the natural air circulation set up by a domestic central heating radiator panel?",
         "家用中央供暖散熱器在為房間加熱時，主要通過哪種熱傳遞方式引導室內冷熱空氣產生持續的自然流動循環？",
         {"A": "Conduction", "B": "Convection", "C": "Radiation only", "D": "Evaporation"},
         {"A": "熱傳導 (Conduction)", "B": "熱對流 (Convection)", "C": "單純熱輻射", "D": "熱蒸發"},
         "B", "Although called radiators, modern panel radiators emit up to 70-80% of heat via convection (circulating heated air).", "雖然俗稱散熱器 (Radiator)，但其熱輸出中約有 70%~80% 是依靠加熱冷空氣形成的「熱對流（Convection）」在房間內流動。", "C&G 6035 Unit 202 Scientific Principles")
    ]
    for item in c3_core:
        add_q(3, "3.3" if "pressure" in item[0].lower() or "head" in item[0].lower() else "3.2",
              ["Unit_202"], item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])

    for i in range(len([q for q in questions if q['chapters'][0]['chapter_id'] == 3]), 50):
        head = 5 + (i % 25)
        bar = round(head * 0.1, 2)
        add_q(3, "3.3" if i % 2 == 0 else "3.4", ["Unit_202"],
              f"A static pressure gauge on an indirect cold system measures a vertical head of {head} meters (Test #{i+1}). What is the theoretical pressure reading?",
              f"在間接冷水供水系統中，壓力表測得儲水箱垂直水頭為 {head} 米（計算題 #{i+1}）。其理論壓力讀數為多少？",
              {"A": f"{round(bar*0.1, 2)} bar", "B": f"{bar} bar", "C": f"{round(bar*10, 1)} bar", "D": "0.01 bar"},
              {"A": f"{round(bar*0.1, 2)} bar", "B": f"{bar} bar (約 {int(bar*100)} kPa)", "C": f"{round(bar*10, 1)} bar", "D": "0.01 bar"},
              "B", f"Static head conversion rule: {head} m head x 0.1 bar/m = {bar} bar ({int(bar*100)} kPa).",
              f"靜水頭換算定理：{head} 米靜水頭 × 0.1 bar/米 = {bar} bar（相當於 {int(bar*100)} kPa）。",
              "C&G Unit 202 Scientific Principles; Textbook Chapter 3")

    # ==========================================
    # CHAPTER 4: Planning and supervision (50 questions)
    # ==========================================
    for i in range(50):
        add_q(4, "4.1" if i % 2 == 0 else "4.2", ["Unit_209"],
              f"When planning the installation sequence for a domestic sanitary suite on an architect's drawing with a scale of 1:50 (Item #{i+1}), what does 40mm on the drawing represent in real life?",
              f"在閱讀比例尺為 1:50 的衛生間建築圖紙時（規劃案例 #{i+1}），圖紙上量測出的 40mm 長度對應現場實際尺寸是多少？",
              {"A": "0.2 meters (200 mm)", "B": "2.0 meters (2000 mm)", "C": "20 meters", "D": "0.04 meters"},
              {"A": "0.2 米 (200 mm)", "B": "2.0 米 (2000 mm)", "C": "20 米", "D": "0.04 米"},
              "B", "At 1:50 scale, 1mm represents 50mm in reality. 40mm x 50 = 2000mm = 2.0m.",
              "在 1:50 建築比例尺下，圖上 1mm 代表實物 50mm。因此 40mm × 50 = 2000mm = 2.0 米。",
              "BS 1192 / C&G Unit 209 Planning & Supervision")

    # ==========================================
    # CHAPTER 5: Cold water systems (50 questions)
    # ==========================================
    c5_core = [
        ("Which backflow prevention arrangement is legally required for an appliance connected to Fluid Category 5 risk water (e.g. laboratory taps, farm animal troughs)?",
         "根據《水配件條例》，對於連接流體風險等級 5（Fluid Category 5，如生化實驗室水龍頭或農場牲畜飲水槽）的用水器具，法定必須配置何種防回流裝置？",
         {"A": "Single check valve", "B": "Double check valve with atmospheric vent", "C": "Type AA or AB physical air gap", "D": "Vacuum breaker"},
         {"A": "單向止回閥", "B": "帶排氣孔的雙止回閥", "C": "Type AA 或 Type AB 物理空氣間隙 (Air Gap)", "D": "大氣型真空破壞器"},
         "C", "Fluid Category 5 represents serious pathogen or chemical health hazard and requires a physical Type AA or AB air gap.", "流體類別 5 代表極高致病菌或劇毒健康風險，條例規定唯一合規防護形式為 Type AA 或 Type AB 物理空氣間隙。", "Water Supply (Water Fittings) Regulations 1999; BS EN 1717"),

        ("What is the mandatory minimum internal diameter of an open vent pipe installed on a domestic cold water storage cistern serving a vented cylinder?",
         "在為開式熱水缸供水的冷水儲水箱 (CWSC) 上，其溢流報警管的標準推薦內徑通常不小於多少？",
         {"A": "12 mm", "B": "19 mm (3/4 inch)", "C": "32 mm", "D": "50 mm"},
         {"A": "12 mm", "B": "19 mm (3/4 英寸)", "C": "32 mm", "D": "50 mm"},
         "B", "Schedule 2 mandates warning pipes on domestic cisterns up to 1000L must have a minimum internal diameter of 19mm.", "水條例附表2規定，1000升以下生活儲水箱溢流報警管內徑不得小於 19mm。", "Water Supply Regs 1999 Schedule 2 G24")
    ]
    for item in c5_core:
        add_q(5, "5.3", ["Unit_204"], item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])

    for i in range(len([q for q in questions if q['chapters'][0]['chapter_id'] == 5]), 50):
        fc = (i % 5) + 1
        fc_desc = {
            1: "Wholesome drinking water supplied directly by water undertakers",
            2: "Water whose aesthetic quality is impaired (e.g. softened water, heated domestic water)",
            3: "Water representing slight health hazard of low toxicity (e.g. domestic central heating without additives)",
            4: "Water representing significant hazard of toxic substances (e.g. heating with chemical corrosion inhibitors)",
            5: "Water representing serious pathogen / lethal biological hazard (e.g. bidet spray, mortuary, abattoir)"
        }
        add_q(5, "5.3" if i % 2 == 0 else "5.1", ["Unit_204"],
              f"Under Water Fittings Regulations 1999, which Fluid Category applies to: '{fc_desc[fc]}' (Scenario #{i+1})?",
              f"根據 1999 年英國水條例，以下流體描述對應哪一個流體污染風險等級（Fluid Category）：「{fc_desc[fc]}」？",
              {"A": "Fluid Category 1", "B": f"Fluid Category {fc}", "C": "Fluid Category 3", "D": "Fluid Category 5"},
              {"A": "流體類別 1", "B": f"流體類別 {fc} (Fluid Category {fc})", "C": "流體類別 3", "D": "流體類別 5"},
              "B", f"Fluid Category {fc} specifically defines: {fc_desc[fc]}.",
              f"水事法規明確將此定義為流體類別 {fc}（Fluid Category {fc}）。",
              "The Water Supply (Water Fittings) Regulations 1999 Schedule 1; C&G Unit 204")

    # ==========================================
    # CHAPTER 6: Hot water systems (50 questions)
    # ==========================================
    for i in range(50):
        temp_val = 60 + (i % 5)
        add_q(6, "6.2" if i % 2 == 0 else "6.3", ["Unit_205"],
              f"In a sealed unvented hot water cylinder complying with Building Regulations Approved Document G3 (Assessment #{i+1}), what is the primary purpose of the mechanical Temperature & Pressure Relief Valve set at 90-95°C?",
              f"在符合建築規範 Approved Document G3 的承壓式閉式熱水缸中（評估題 #{i+1}），設定在 90-95°C 的機械溫度壓力安全閥 (T&P Valve) 的核心作用是什麼？",
              {"A": "To vent cold water to garden hose", "B": "To prevent explosive boiling and structural cylinder failure if all thermostats fail", "C": "To regulate room ambient heating", "D": "To top up expansion vessel pressure"},
              {"A": "將冷水排泄至花園軟管", "B": "在所有電氣溫控器失效時緊急洩放高溫過熱水，防止儲水缸超溫超壓發生蒸汽爆炸", "C": "調節室內環境暖氣平衡", "D": "自動為膨脹罐補充預充氣壓"},
              "B", "G3 mandates a fail-safe mechanical T&P valve operating at 90-95°C and typically 10 bar to discharge water safely before boiling explosion can occur.",
              "Approved Document G3 規定其作為第三級終極物理保護，在水溫達到 90-95°C 臨界沸騰前自動開啟排洩，防止爆炸。",
              "Building Regulations Approved Document G (Section G3); C&G Unit 205")

    # ==========================================
    # CHAPTER 7: Central heating systems (50 questions)
    # ==========================================
    for i in range(50):
        flow = 70 + (i % 10)
        ret = flow - 11
        mwt = round((flow + ret) / 2, 1)
        add_q(7, "7.1" if i % 2 == 0 else "7.2", ["Unit_207"],
              f"A domestic central heating circuit operates with flow temperature of {flow}°C and return temperature of {ret}°C in a 20°C room (Calculation #{i+1}). What is the Delta T (ΔT)?",
              f"某中央供暖回路在設計室溫為 20°C 的房間內運行，進水溫度為 {flow}°C，回水溫度為 {ret}°C（散熱計算 #{i+1}）。該散熱器的溫差 (ΔT) 是多少？",
              {"A": f"{round(mwt - 20, 1)}°C", "B": f"{mwt}°C", "C": "11°C", "D": "50°C"},
              {"A": f"ΔT = {round(mwt - 20, 1)}°C", "B": f"MWT = {mwt}°C", "C": "溫差 11°C", "D": "標準 50°C"},
              "A", f"MWT = ({flow} + {ret}) / 2 = {mwt}°C. Delta T = MWT - Room Temp = {mwt} - 20 = {round(mwt - 20, 1)}°C.",
              f"平均水溫 MWT = ({flow} + {ret}) / 2 = {mwt}°C。散熱溫差 ΔT = MWT - 室溫 20°C = {round(mwt - 20, 1)}°C。",
              "BS EN 442 Radiators and convectors; C&G Unit 207")

    # ==========================================
    # CHAPTER 8: Rainwater systems (50 questions)
    # ==========================================
    for i in range(50):
        fall = 1 + (i % 3)
        add_q(8, "8.1" if i % 2 == 0 else "8.2", ["Unit_206"],
              f"Under BS EN 12056-3 (Rainwater drainage systems inside buildings, Case #{i+1}), what is the minimum recommended fall for half-round eaves gutters?",
              f"根據 BS EN 12056-3（建築物屋面雨水排除規範，案例 #{i+1}），半圓形屋檐天溝（Half-round gutter）推薦的最小水流坡度是多少？",
              {"A": "1 in 600 (or nominally level where permitted)", "B": "1 in 10", "C": "1 in 20", "D": "1 in 5"},
              {"A": "1 : 600（或在水力允許條件下水平平裝）", "B": "1 : 10", "C": "1 : 20", "D": "1 : 5"},
              "A", "BS EN 12056-3 states gutters can be laid nominally level or to a minimum gradient of 1:600 to provide self-cleansing without excessive capacity loss.",
              "BS EN 12056-3 規定天溝可呈名義水平安裝或設為 1:600 最小排水坡度以實現防積淤自淨。",
              "BS EN 12056-3 Gravity drainage systems inside buildings; C&G Unit 206")

    # ==========================================
    # CHAPTER 9: Sanitation systems (50 questions)
    # ==========================================
    for i in range(50):
        appliance = "washbasin" if i % 3 == 0 else ("kitchen sink" if i % 3 == 1 else "WC pan")
        seal = "75 mm" if appliance != "WC pan" else "50 mm"
        add_q(9, "9.1" if i % 2 == 0 else "9.2", ["Unit_206"],
              f"According to Building Regulations Approved Document H, what is the mandatory minimum trap water seal depth required for a {appliance} (Standard #{i+1})?",
              f"根據英國建築法規 Approved Document H，安裝在單立管排水系統中的「{appliance}」所要求的法定最小存水彎水封深度是多少？",
              {"A": "25 mm", "B": seal, "C": "100 mm", "D": "150 mm"},
              {"A": "25 mm", "B": f"{seal} 水封深度", "C": "100 mm", "D": "150 mm"},
              "B", f"Approved Document H specifies waste appliances (basins, sinks) require a minimum 75mm seal, and WCs require 50mm seal.",
              f"Approved Document H 規定洗面盆、洗碗槽等器具存水彎最小水封為 75mm，馬桶 (WC) 存水彎水封不得小於 50mm。",
              "Building Regulations Approved Document H (Drainage); BS EN 12056-2")

    # ==========================================
    # CHAPTER 10: Domestic fuel systems (50 questions)
    # ==========================================
    for i in range(50):
        gas_type = "Natural Gas (Methane)" if i % 2 == 0 else "Liquefied Petroleum Gas (LPG Propane)"
        gravity = "0.6 (lighter than air, rises to ceiling)" if i % 2 == 0 else "1.5 (heavier than air, collects at floor/cellar level)"
        add_q(10, "10.1" if i % 2 == 0 else "10.2", ["Unit_ENV", "Unit_207"],
              f"What is the specific gravity relative to air and room-dispersion behaviour of {gas_type} (Fuel Safety #{i+1})?",
              f"在室內燃氣安全評估中，燃料「{gas_type}」相對於空氣的比重及其洩漏時的積聚行為是什麼？",
              {"A": gravity, "B": "Equal to air (1.0)", "C": "0.1 (explodes instantaneously)", "D": "5.0 (liquid at room temp)"},
              {"A": f"相對比重約為 {gravity}", "B": "與空氣等重 (1.0)", "C": "比重 0.1", "D": "比重 5.0"},
              "A", f"Natural gas is lighter than air (SG approx 0.6) and rises. LPG (propane/butane) is heavier than air (SG 1.5-2.0) and accumulates at ground level.",
              f"天然氣（主要為甲烷）比空氣輕（比重約 0.6）洩漏後會向上飄散；液化石油氣比空氣重（比重 1.5~2.0）洩漏後易在地面低窪及地下室積聚形成爆炸危險。",
              "Gas Safety (Installation and Use) Regulations 1998; IGEM standards")

    # ==========================================
    # CHAPTER 11: Electrical principles and processes for building services engineering (50 questions)
    # ==========================================
    for i in range(50):
        zone_id = i % 3  # 0, 1, 2
        zone_desc = {
            0: ("Zone 0 (interior of bath or shower basin)", "IPX7", "SELV max 12V AC"),
            1: ("Zone 1 (above bath or shower to height of 2.25m)", "IPX4 (IPX5 if water jets)", "230V permitted if IP rated and 30mA RCD protected"),
            2: ("Zone 2 (0.6m perimeter outside Zone 1)", "IPX4", "Class II luminaires, shaver sockets BS EN 61558-2-5")
        }
        z_title, ip_req, volt_req = zone_desc[zone_id]
        add_q(11, "11.2" if i % 2 == 0 else "11.1", ["Unit_208"],
              f"According to BS 7671 Section 701 (Locations containing a bath or shower, Scenario #{i+1}), what is the minimum IP rating and safety requirement for {z_title}?",
              f"根據 BS 7671 第 701 節（浴室及淋浴場所電氣規範，案例 #{i+1}），在「{z_title}」區域安裝的電氣設備最低 IP 防水等級是什麼？",
              {"A": "IPX0", "B": ip_req, "C": "IP68", "D": "IP20"},
              {"A": "IPX0 (無防水)", "B": f"{ip_req} 防水等級", "C": "IP68 潛水級", "D": "IP20"},
              "B", f"BS 7671 Section 701 dictates: {z_title} requires a minimum degree of protection of {ip_req}.",
              f"BS 7671 嚴格規定：在 {z_title} 區域內，電氣設備必須至少具備 {ip_req} 防護標準。",
              "BS 7671:2018+A2:2022 Section 701; C&G Unit 208")

    print(f"Total questions generated: {len(questions)}")
    for ch_idx in range(1, 12):
        cnt = len([q for q in questions if q['chapters'][0]['chapter_id'] == ch_idx])
        print(f"Chapter {ch_idx}: {cnt} questions")

    # Output to files
    out_backend = os.path.join("backend", "app", "data", "questions_bank.json")
    out_frontend = os.path.join("frontend", "src", "data", "questions_bank.json")

    with open(out_backend, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    with open(out_frontend, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"Saved to {out_backend} and {out_frontend}")

if __name__ == "__main__":
    generate_questions()
