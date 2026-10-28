# Chapter 11 Part 2: Additional 50 Questions (Questions 31 to 80)
from .utils import make_q

def get_part2_questions():
    questions = []
    
    data = [
        # 31. BS 7671 Section 701 Bathroom Zones definition
        ("11.5",
         "Under BS 7671 Section 701 (Locations containing a bath or shower), what are the designated electrical safety zones recognized in domestic bathrooms?",
         "根據英國電工法規 BS 7671 第 701 節（包含浴缸或淋浴的潮濕場所），家庭浴室內部劃分為哪三個法定電氣安全分區？",
         {"A": "Alpha, Beta, and Gamma", "B": "Zone 0, Zone 1, and Zone 2 (with the remaining room space designated as Outside the Zones)", "C": "Zone 1, Zone 2, Zone 3, and Zone 4", "D": "Hot Zone, Cold Zone, and Wet Zone"},
         {"A": "Alpha 區、Beta 區、以及 Gamma 區", "B": "Zone 0 (0區)、Zone 1 (1區)、以及 Zone 2 (2區)（其餘超出上述邊界的浴室空間統稱為分區外空間 Outside Zones）", "C": "Zone 1、Zone 2、Zone 3、以及 Zone 4", "D": "熱水區、冷水區、以及潮濕區"},
         "B", "BS 7671 Section 701 classifies bathrooms into Zone 0 (submerged), Zone 1 (spray/splash above tray/bath to 2.25m), and Zone 2 (0.6m perimeter radius around Zone 1 up to 2.25m).", "浴室電氣三防區必背：Zone 0（水底下，浴缸或底盤內部）；Zone 1（浴缸底盤正上方至 2.25 米淋浴噴淋區）；Zone 2（Zone 1 向外延伸 60 公分半徑的防濺緩衝區）。2 區之外叫分區外（Outside zones）。", "BS 7671:2018 Section 701; C&G Unit 208"),

        # 32. Zone 0 dimensions and IP rating
        ("11.5",
         "Under BS 7671 Section 701, what is the boundary definition of 'Zone 0' in a domestic bathroom, and what MINIMUM Ingress Protection (IP) rating is mandatory for any electrical equipment installed within it?",
         "根據 BS 7671 第 701 節規定，家庭浴室內的「Zone 0 (0區)」是指何處空間範圍？安裝在該分區內的任何電氣設備必須具備的「最低防水防護等級 (IP Rating)」是多少？",
         {"A": "The ceiling; IP20", "B": "The interior of the bathtub or shower basin; minimum IPX7 (protection against total water immersion up to 1 meter depth)", "C": "Behind the mirror; IP00", "D": "Outside the front door; IP68"},
         {"A": "浴室吊頂石膏板天花板；IP20", "B": "浴缸或淋浴底盤內部的盛水浸沒空間；最低強制防護等級為 IPX7 (具備抵禦深入 1 米水深完全浸泡的卓越水密性能)", "C": "浴室梳妝鏡背後；IP00", "D": "浴室大門外側；IP68"},
         "B", "Zone 0 is the physical water-holding tub/basin. Because equipment is submerged under water, it demands at least IPX7 (immersion-proof) and may only be powered by 12V AC SELV.", "Zone 0 浸水區防護鐵律：0 區就是洗澡時泡在水裡的缸底！人整個泡在水裡，皮膚電阻幾乎為零。任何水下燈具必須達到 IPX7（耐 1 米水浸泡），且電壓嚴禁超 12V 安全特低電壓（SELV）！", "BS 7671:2018 Regulation 701.32 & 701.512.2; BS EN 60529"),

        # 33. Zone 0 allowable voltage and equipment
        ("11.5",
         "What is the maximum permissible electrical operating voltage and supply safety type allowed for any electrical equipment (e.g. whirlpool bath jets) located inside Zone 0?",
         "在浴室 Zone 0 (0區) 盛水內部，法規允許安裝的電氣設備（如水療衝浪浴缸水下噴頭）的「最高允許工作電壓與供電安全制式」是什麼？",
         {"A": "230 Volts AC mains supply", "B": "Safety Extra-Low Voltage (SELV) not exceeding 12 Volts AC rms or 30 Volts ripple-free DC, with the safety isolation source situated outside Zones 0, 1, and 2", "C": "10,000 Volts DC", "D": "400 Volts 3-phase"},
         {"A": "230 伏特市電交流高壓直供", "B": "安全特低電壓 (SELV)，額定工作電壓「不超過 12 伏特交流電 (12V AC) 或 30 伏特無紋波直流電 (30V DC)」，且其隔離安全變壓器電源必須深藏在 0、1、2 區之外！", "C": "10,000 伏特直流電", "D": "400 伏特工業三相動力電"},
         "B", "Zone 0 allows only SELV max 12V AC (or 30V DC). The safety isolating transformer must be sited outside Zones 0, 1, and 2 (e.g. in the ceiling void or outside the bathroom entirely).", "0 區 12V 生命極限：水下絕對嚴禁進 230V 市電！只能用 12V SELV（安全特低電壓）。變壓器本體必須裝在天花板頂上或浴室門外，只有 12V 弱電能進浴缸底，就算電線皮破了人摸到也絕對死不了！", "BS 7671:2018 Regulation 701.55; C&G Unit 208"),

        # 34. Zone 1 dimensions and IP rating
        ("11.5",
         "Under BS 7671 Section 701, what are the spatial dimensions of 'Zone 1' in a bathroom containing a shower tray, and what MINIMUM IP rating is required for electrical fixtures (e.g. an electric shower)?",
         "根據 BS 7671 第 701 節規定，在帶有淋浴底盤的浴室中，「Zone 1 (1區)」的立體空間邊界如何界定？安裝在該分區內的電氣設備（如即熱式電淋浴器）法定的「最低 IP 防護等級」是多少？",
         {"A": "From the floor to 5 meters; IP00", "B": "Vertically above the shower tray to a height of 2.25 meters above the finished floor level (or the highest shower head if higher); minimum rating IPX4 (or IPX5 if subjected to water jets)", "C": "Under the wooden floorboards; IP65", "D": "Around the toilet seat; IP20"},
         {"A": "從地面向上延伸至 5 米高空；IP00", "B": "淋浴底盤正上方垂直投影、自完成面地面向上延伸至「2.25 米高處」（若花灑固定點更高則延伸至花灑最高點）；法定最低防護等級為 IPX4 (防濺型，若會遭受高壓水柱衝洗則升級為 IPX5)", "C": "木地板下方暗處；IP65", "D": "馬桶圈周圍；IP20"},
         "B", "Zone 1 is the active showering zone up to 2.25m high. Fixtures must be minimum IPX4 (splash-proof from all angles). If high-pressure water cleaning jets are used, IPX5 is mandatory.", "Zone 1 淋浴噴霧區必背：花灑下洗澡的區域！從地面向上打到 2.25 米（洗澡水漫天飛舞的地方）。裝在裡面的即熱電熱水器、排風扇最低必須是 IPX4（防任何角度水花潑濺），嚴禁用普通不防水電器！", "BS 7671:2018 Regulation 701.32.3 & 701.512.2"),

        # 35. Zone 1 allowable equipment
        ("11.5",
         "Under BS 7671 Regulation 701.55, which electrical equipment is PERMITTED to be installed inside Zone 1 of a domestic bathroom?",
         "根據 BS 7671 第 701.55 條規定，在浴室 Zone 1 (1區) 內部，被法律明確允許固定安裝的電氣設備有哪些？",
         {"A": "Standard 13A domestic socket outlets and electric toasters", "B": "Fixed and permanently connected equipment specifically rated for Zone 1: electric instantaneous showers, water heaters, shower waste pumps, low-voltage luminaires, and SELV equipment (min IPX4)", "C": "Television sets and microwaves", "D": "Open electric bar fires"},
         {"A": "標準 13A 家用三孔插座與烤麵包機", "B": "通過認證且永久硬線連接的專用電氣設備：即熱式電淋浴器 (Electric Showers)、貯水式電熱水器、淋浴強排污水泵、特種防水低壓照明燈具、以及 SELV 特低電壓設備（最低防護等級 IPX4）", "C": "台式液晶電視機與微波爐", "D": "外露發熱電爐絲的電暖氣"},
         "B", "Zone 1 permits only fixed appliances rated for the environment (electric showers, water heaters, shower waste pumps) with min IPX4. Standard 230V socket-outlets are strictly forbidden.", "1 區准入電器清單：除了洗澡必須的即熱電淋浴器、淋浴底盤強排泵、防水吸頂燈外，嚴禁裝任何普通插座開關！電淋浴器出廠密封達到 IPX4，且必須由專門硬線固定接線，普通插頭插座一律槍斃！", "BS 7671:2018 Regulation 701.55; C&G Unit 208"),

        # 36. Zone 2 dimensions and IP rating
        ("11.5",
         "Under BS 7671 Section 701, what are the spatial limits of 'Zone 2' in a domestic bathroom, and what is its minimum required IP rating?",
         "根據 BS 7671 規定，家庭浴室內的「Zone 2 (2區)」空間範圍邊界如何劃定？其最低法定 IP 防護等級是多少？",
         {"A": "Inside the bedroom wardrobe; IP20", "B": "Extends 0.60 meters (600mm) horizontally beyond the outer perimeter of Zone 1, and vertically up to a height of 2.25 meters above the finished floor; minimum rating IPX4", "C": "Under the kitchen sink; IP68", "D": "There is no Zone 2"},
         {"A": "臥室大衣櫃內部；IP20", "B": "自 Zone 1 外邊界水平向外延伸「0.60 米 (600mm)」，垂直高度自地面延伸至「2.25 米」高度處；最低防護等級為 IPX4 (防濺水型)", "C": "廚房洗菜盆下方；IP68", "D": "現代電工法規已取消 2 區"},
         "B", "Zone 2 extends 0.6m beyond the bath/shower rim up to 2.25m height. Water splashes can reach this zone, requiring minimum IPX4 splash-proof equipment.", "Zone 2 緩衝防濺區必背：站在浴缸邊緣，向外量 60 公分（0.6 米）、高 2.25 米這一圈！水滴和濕手容易甩到這裡，防護等級依然必須是 IPX4！可以裝帶隔離變壓器的刮鬍刀插座、專用防水壁燈。", "BS 7671:2018 Regulation 701.32.4 & 701.512.2"),

        # 37. Shaver supply units in Zone 2
        ("11.5",
         "What specific type of electrical socket is legally permitted to be installed inside Zone 2 of a domestic bathroom?",
         "在家庭浴室的 Zone 2 (2區) 範圍內，法律唯一允許安裝的插座類電氣附件是什麼？",
         {"A": "A standard 13A switched double socket outlet", "B": "A dedicated Shaver Supply Unit incorporating an internal safety isolating transformer complying with BS EN 61558-2-5 (limited to 20VA-50VA)", "C": "A 32A industrial commando socket", "D": "An electric car charging socket"},
         {"A": "標準 13A 帶開關雙位家用市電插座", "B": "符合 BS EN 61558-2-5 標準、內置雙重絕緣安全隔離變壓器的專用「刮鬍刀專用插座 (Shaver Supply Unit)」(功率死死限制在 20VA 至 50VA 之間)", "C": "32A 工業重型防水公母插座", "D": "大功率電動汽車直流充電插座"},
         "B", "Regulation 701.512.3 prohibits standard sockets in Zone 2, but expressly permits shaver units complying with BS EN 61558-2-5. An isolating transformer breaks the earth loop, making accidental contact non-fatal.", "刮鬍刀插座唯一特權必考：浴室鏡子旁唯一的插座！它肚子裡藏著個 1:1 隔離變壓器，電壓是浮動的、完全不對地形成迴路！即使手濕摸到插孔，電流也不會順著人體流向大地，因此法規特批允許裝在 2 區！", "BS 7671:2018 Regulation 701.512.3; BS EN 61558-2-5"),

        # 38. Standard 230V sockets outside zones
        ("11.5",
         "Under BS 7671 (18th Edition including Amendment 2:2022), under what strict distance and protection rules are standard 230V 13A socket-outlets permitted in a large domestic bathroom?",
         "根據 BS 7671（第 18 版及 2022 年修正案 2）規定，在面積寬敞的大型家庭浴室中，普通 230V 家用三孔插座在何種距離與防護要求下才被法規允許安裝？",
         {"A": "Inside the bathtub submerged in water", "B": "Permitted ONLY if installed at least 2.5 meters (formerly 3.0 meters) horizontally from the outer boundary of Zone 1, and the circuit MUST be protected by a 30mA RCD", "C": "Directly next to the shower head without RCD", "D": "Sockets are banned in all rooms"},
         {"A": "直接安裝在浴缸內壁浸沒在水中", "B": "必須距離 Zone 1 淋浴邊界水平距離「至少 2.5 米以外」（2022 年修正案由原 3.0 米縮小至 2.5 米），且該插座電路必須由 30mA 漏保（RCD）實施快速跳閘保護！", "C": "直接裝在花灑正下方且不設漏保", "D": "英國建築法規在所有房間內全面取締插座"},
         "B", "Amendment 2 (2022) reduced the minimum distance from 3.0m to 2.5m from Zone 1. Standard 230V socket-outlets are prohibited in small UK bathrooms because typical dimensions cannot satisfy the 2.5m clearance.", "浴室普通插座 2.5 米紅線：英國小浴室絕不見插座！因為新法規放寬後也死死卡定：普通 13A 插座離花灑 Zone 1 邊緣必須至少 2.5 米遠（防人拿吹風機掉進浴缸）！且必須配備 30mA 漏保。小衛生間根本不夠尺寸！", "BS 7671:2018+A2:2022 Regulation 701.512.3"),

        # 39. Pull-cord ceiling switches in bathrooms
        ("11.5",
         "Why are ceiling-mounted 'Pull-Cord' switches (for lighting or shower isolation) permitted inside bathroom zones, whereas traditional wall-mounted plate switches are prohibited?",
         "在家庭浴室內，天花板吊頂「拉線式開關 (Pull-Cord Switch)」被法規允許安裝在潮濕分區內，而傳統牆壁普通翹板開關卻被嚴令禁止，其核心安全防護原理是什麼？",
         {"A": "Pull cords are cheaper than wall switches", "B": "The pull cord is made of flexible non-conducting nylon/polyester cord (an electrical insulator); the user's wet hand operates the mechanical cord without physically touching the live switch mechanism mounted safely at high ceiling level", "C": "Pull cords generate light without electricity", "D": "Wall switches shatter in steam"},
         {"A": "拉線開關在市場上的採購價格比牆壁開關便宜", "B": "拉繩採用高絕緣非導電尼龍繩製成（純電氣絕緣體）；洗浴人員濕淋淋的手只觸碰絕緣吊繩，而帶電的 230V 機械開關金屬本體被高高固定在天花板頂上，人體與帶電高壓被物理空間徹底隔絕！", "C": "拉線開關在拉動時能自發熒光照明無需電力", "D": "牆壁開關面板遇水蒸氣會自發碎裂"},
         "B", "Regulation 701.512.3: Standard plate switches are banned in Zones 1 and 2. Pull-cord switches isolate the user by putting a non-conductive insulating cord between wet fingers and the 230V live contacts.", "浴室拉繩開關保命絕緣體：洗完澡滿身是水，濕手去按牆上 230V 塑料板開關，水順著縫隙流進去會把人當場電死！拉繩開關把帶電的開關本體死死釘在 2.4 米天花板上，手裡抓的是一根尼龍繩，百分之百絕緣！", "BS 7671:2018 Regulation 701.512.3; C&G Unit 208"),

        # 40. Electric shower cable sizing
        ("11.5",
         "Why does a high-output domestic electric instantaneous shower (e.g. 9.5 kW or 10.5 kW) typically require a heavy 10 mm² twin and earth cable rather than a standard 2.5 mm² or 6 mm² cable?",
         "一台高功率家用即熱式電淋浴花灑（如 9.5 kW 或 10.5 kW），為什麼通常必須使用粗達「10 mm² 的雙芯帶接地護套電纜 (10mm² Twin & Earth)」，而嚴禁使用普通的 2.5 mm² 或 6 mm² 電線？",
         {"A": "10mm² cable is easier to bend", "B": "A 10.5 kW load draws approximately 45.6 Amps at 230V (I = P ÷ V); high current causes severe I²R overheating, voltage drop, and fire in smaller cables, particularly when routed through thermally insulated roof joists", "C": "10mm² cable conducts water to the shower", "D": "Regulations require all wires to be 10mm²"},
         {"A": "10 mm² 粗電纜柔軟極易隨意彎曲", "B": "一台 10.5 kW 電器在 230V 電壓下的滿負荷運行電流高達約 45.6 安培 (I = P ÷ V)！如此巨大的電流若流經較細電線，焦耳熱效應 (I²R) 會讓電線瞬間燒得滾燙融化外皮引發閣樓大火，必須用 10mm² 粗線！", "C": "10 mm² 粗電纜內部自帶微型自來水輸水通道", "D": "英國法規強制全屋所有電線一律統一採用 10 mm²"},
         "B", "Current calculation: I = P / V = 10,500W ÷ 230V = 45.65 Amps. Factoring in derating for thermal loft insulation (Installation Method 101), 6mm² cable will overheat and burn. 10mm² copper is essential.", "電淋浴粗電線必考計算：10.5 千瓦除以 230 伏 = 45.6 安培！電流比全屋其他電器加起來還大！若用細電線，電線像電爐絲一樣發紅，閣樓保溫棉立刻起火把房子燒光！必須拉 10 平方專用粗銅線！", "BS 7671 Appendix 4 Current-carrying capacities; C&G Unit 208")
    ]

    for sub_id, stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref in data:
        questions.append(make_q(11, sub_id, ["Unit_208"], stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref))

    return questions
