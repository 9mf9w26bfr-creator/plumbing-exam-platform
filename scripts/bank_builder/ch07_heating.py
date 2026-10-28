# Chapter 7: Central heating systems (90 Questions)
from .utils import make_q

def get_questions():
    questions = []
    
    data = [
        # 7.1 Heat Emitters, Radiator Types & Sizing
        ("7.1",
         "Under BS EN 442, what is the design temperature difference (Delta T or ΔT) traditionally used as the testing baseline for rating the heat output of domestic radiators?",
         "根據歐洲/英國標準 BS EN 442，傳統燃氣壁掛爐供暖系統中，用於標定散熱器暖氣片熱輸出額定瓦特數的標準設計溫差（Delta T 或 ΔT）是多少？",
         {"A": "Delta T 20°C (ΔT 20)", "B": "Delta T 50°C (ΔT 50 - Mean water temp 70°C minus room temp 20°C)", "C": "Delta T 80°C (ΔT 80)", "D": "Delta T 100°C"},
         {"A": "Delta T 20°C (ΔT 20)", "B": "Delta T 50°C (ΔT 50，即散熱器平均水溫 70°C 減去室內基準設計溫度 20°C)", "C": "Delta T 80°C", "D": "Delta T 100°C"},
         "B", "BS EN 442 defines standard Delta T 50 based on flow 75°C, return 65°C (mean water temp 70°C), and room temperature 20°C (70 - 20 = 50°C ΔT).", "BS EN 442 散熱器行業標準定額：出水 75°C、回水 65°C（平均水溫 70°C），室內 20°C，算得標準溫差 ΔT 50。散熱器廠家彩頁標註的瓦特數默認均以此為準。", "BS EN 442 Radiators and convectors; C&G Unit 207"),

        ("7.1",
         "When designing a low-temperature heating system operating with a heat pump (flow 45°C, return 35°C, room 20°C, Delta T 20°C), how does the required radiator size compare to a standard Delta T 50 system?",
         "當供暖系統改用低溫空氣源熱泵運行時（出水 45°C、回水 35°C、室溫 20°C，設計溫差 ΔT 降至 20°C），為達到相同供熱量，散熱器散熱表面積相比於傳統 ΔT 50 系統需要擴大多少？",
         {"A": "Radiators can be halved in size", "B": "Radiator surface area must be approximately 2 to 2.5 times larger (or fan convectors used)", "C": "Radiator size remains identical", "D": "Radiators must be removed completely"},
         {"A": "暖氣片尺寸可以直接縮小一半", "B": "散熱器暖氣片散熱面積必須擴大至大約 2 至 2.5 倍（或改用低溫風機盤管），以補償低水溫下的散熱衰減", "C": "暖氣片尺寸完全不需做任何變更", "D": "必須將所有暖氣片全部徹底拆除"},
         "B", "At lower ΔT, radiant and convective heat emission falls sharply. Radiators must be roughly double in size to deliver equivalent heat to the room.", "低溫供暖散熱定律：水溫越低散熱越慢。在 ΔT 20 工況下，相同暖氣片的散熱瓦特數衰減超過 60%，必須換裝加大加厚散熱器才能保證房間溫暖。", "MCS Heat Pump Design Guide (MIS 3005); BS EN 442"),

        ("7.1",
         "In standard radiator terminology, what configuration represents a 'Type 22' (K2) panel radiator?",
         "在現代鋼製板式散熱器行業術語中，「Type 22 (或稱 K2)」散熱器代表何種內部結構構造？",
         {"A": "Single water panel with no convector fins", "B": "Double water panels with double internal corrugated convector fins", "C": "Triple water panels with single fin", "D": "A radiator with 22 pipes"},
         {"A": "單水道散熱面板，無內部對流散熱鰭片 (Type 10 / P1)", "B": "雙層水道散熱面板，且兩層面板中間夾裝雙排波紋狀對流散熱翅片 (Double Panel, Double Convector - Type 22 / K2)", "C": "三層散熱面板配單層翅片", "D": "帶有 22 根鋼管的散熱器"},
         "B", "Type 22 features two water-carrying panels and two rows of welded zig-zag convector fins, maximizing convective airflow output in compact depth.", "散熱器命名規則：第一位數字代表水道水板層數，第二位代表內部對流翅片排數。Type 22 即「雙板雙翅片」，散熱效率極高，是英國家用主流型號。", "BS EN 442; Stelrad / Purmo Radiator Technical Catalogues"),

        ("7.1",
         "What is the mechanical function of corrugated steel 'Convector Fins' spot-welded between the panels of a domestic radiator?",
         "點焊在鋼製散熱器水道面板背部夾層內的波紋狀金屬「對流翅片 (Convector Fins)」，其核心物理功能是什麼？",
         {"A": "To make the radiator heavier", "B": "To vastly increase the total conductive contact surface area exposed to room air, driving vigorous natural convection heat transfer", "C": "To filter room dust", "D": "To reflect sunlight"},
         {"A": "單純增加散熱器的自重防止晃動", "B": "極大擴展金屬與室內空氣接觸的熱傳導表面積，煙囪效應加速引導冷空氣自下而上流過翅片，形成強勁的自然熱對流循環散熱", "C": "吸附過濾房間內的懸浮粉塵", "D": "反射室外強烈陽光"},
         "B", "Convector fins increase heat transfer surface area up to 300%, transforming modern panel radiators into powerful natural convective air warmers.", "雖然俗稱「Radiator 輻射器」，但加裝對流翅片後，暖氣片 75% 以上的熱量是依靠被翅片加熱的對流熱風（Convection）在房間內循環傳遞的。", "BS EN 442; C&G Unit 207 Central Heating"),

        ("7.1",
         "What is a 'Two-Pipe Central Heating System' compared to an obsolete one-pipe loop?",
         "與老舊淘汰的單管串聯系統（One-pipe system）相比，現代普遍採用的「雙管並聯供暖系統 (Two-Pipe System)」的核心水力優勢是什麼？",
         {"A": "Two-pipe systems require no boiler", "B": "Separate flow and return pipes run in parallel, ensuring every radiator in the property receives water at the same high boiler supply temperature rather than progressively cooler water", "C": "It uses double the electricity", "D": "Water never leaves the radiators"},
         {"A": "雙管系統完全不需要燃氣壁掛爐", "B": "供水管與回水管全程獨立並聯敷設，確保管網中每組暖氣片進水都能直接獲得鍋爐輸出同等高溫的供水，杜絕了單管串聯時下游暖氣片水溫逐個衰減變涼的致命弊端", "C": "耗電量成倍增加", "D": "水流永遠在暖氣片內部靜止不動"},
         "B", "Two-pipe systems deliver hot water at boiler flow temperature to every emitter, returning cooled water via a common return. In one-pipe systems, return mixes into flow, cooling down-circuit.", "單管系統「吃前面剩下的溫水」，越往後越涼；雙管並聯系統每組暖氣片進口均為純熱水供水，出水匯入回水幹管，各房間溫度均勻可控。", "Domestic Heating Design Guide; C&G Unit 207"),

        ("7.1",
         "What is a 'Microbore' central heating pipework system?",
         "在家庭中央供暖管路佈置中，「微口徑章魚式供暖系統 (Microbore System)」具有何種工藝特徵？",
         {"A": "A system using 100mm underground mains", "B": "Central flow and return distribution manifolds that distribute heating water to individual radiators via small-diameter, flexible copper or plastic pipe coils (typically 8mm or 10mm outside diameter)", "C": "A system without pipes", "D": "A system for heating water with microwaves"},
         {"A": "全系統採用 100mm 地下大口徑管道", "B": "由中央供回水分水器（Manifolds）作為核心樞紐，通過 8mm 或 10mm 柔軟可彎曲的小口徑紫銅或塑料盤管，像章魚爪一樣單管直達單獨向每組暖氣片獨立供水", "C": "完全無管道的空氣供暖系統", "D": "利用微波爐微波加熱水流的系統"},
         "B", "Microbore uses 8mm or 10mm soft coils running from central manifolds directly to radiators, eliminating underfloor joints and enabling rapid installation.", "微口徑章魚式系統（8-10mm 管徑）盤管極易穿過木地板下穿管，中間零接頭絕無暗埋漏水風險，施工快捷，但對水質清潔度與水力平衡要求極高。", "C&G 6035 Unit 207 Textbook Ch 7"),

        ("7.1",
         "What is the function of an Underfloor Heating (UFH) blending (mixing) valve manifold assembly connected to a high-temperature boiler system?",
         "當低溫地板輻射採暖（水地暖 UFH）接入輸出 75°C 高溫水的壁掛爐系統時，地暖分集水器前加裝的「混水溫控閥組 (Blending Valve Assembly)」的功用是什麼？",
         {"A": "To boil the floorboards", "B": "To blend hot boiler water with cooler UFH return water, regulating flow temperature down to a safe 35°C to 45°C to protect floor finishes from thermal warping and cracking", "C": "To filter air out of the floor", "D": "To increase pressure to 50 bar"},
         {"A": "將木地板直接烘烤至沸騰溫度", "B": "將壁掛爐輸出的高溫供水與地暖冷回水按比例精密混合，將進入地暖盤管的水溫精準下調調和至 35°C 至 45°C 的低溫安全區，防止實木地板受熱開裂變形或瓷磚空鼓拱起", "C": "抽走地板夾層內的空氣", "D": "將地暖水壓升至 50 bar"},
         "B", "UFH requires low water temperatures (35-45°C) to prevent damaging wooden timber joists and causing occupant foot discomfort. Blending valves recirculate return water to temper the flow.", "地暖是低溫大流量供暖：進水超 50°C 人踩上去燙腳，且會烤裂木地板。恆溫混水閥抽取低溫回水混入高溫進水，實現閉環精準溫控。", "BS EN 1264 Floor heating systems and components; C&G Unit 207"),

        ("7.1",
         "What is the purpose of 'Hydronic Balancing' across all radiators in a domestic central heating system using their lockshield valves?",
         "在中央供暖系統調試中，利用散熱器回水端的「平衡調節鎖定閥 (Lockshield Valve)」對全屋暖氣片實施「水力平衡調試 (Hydronic Balancing)」的核心目的是什麼？",
         {"A": "To make all radiators identical in color", "B": "To adjust water flow resistance through each radiator so that every emitter achieves its designated flow rate and designed temperature drop (Delta T, typically 11°C or 20°C), preventing radiators near the boiler from starving distant radiators", "C": "To increase the system electricity bill", "D": "To vent air from the boiler"},
         {"A": "確保全屋所有暖氣片顏色完全一致", "B": "調節每組暖氣片的局部通流阻力，使各暖氣片水流量與其散熱負荷精確匹配，均勻達到預設的供回水溫差（如 ΔT 11°C 或 20°C），徹底消除「近水樓台先熱、遠端暖氣片冰涼」的水力失調現象", "C": "成倍增加全屋供電電費", "D": "為壁掛爐手動排氣"},
         "B", "Water takes the path of least resistance. Unbalanced systems circulate all water through the nearest radiator while distant radiators stay cold. Balancing throttles lockshields to distribute heat evenly.", "未經平衡的水暖網是災難：水流抄近道全往離鍋爐最近的暖氣片跑，樓上遠端房間凍得發抖。關小近端鎖閉閥、開大遠端，全屋才能均勻升溫。", "BS EN 14336 Heating systems in buildings - Installation and commissioning; C&G Unit 207"),

        ("7.1",
         "What is the standard design temperature drop (Delta T) between flow and return across an individual domestic radiator in a traditional boiler system?",
         "在傳統非冷凝或常規燃氣壁掛爐供暖系統中，每組散熱器進出水口之間的標準設計供回水溫差（Delta T）通常是多少？",
         {"A": "1°C", "B": "11°C (e.g. Flow 75°C, Return 64°C, traditionally used for system sizing)", "C": "40°C", "D": "80°C"},
         {"A": "1°C (流量過大)", "B": "11°C (約 20°F，例如進水 75°C、出水 64°C，傳統水暖調試基準溫差)", "C": "40°C", "D": "80°C"},
         "B", "Traditional UK wet central heating systems were designed around an 11°C (20°F) temperature drop across radiators, ensuring stable laminar/turbulent heat transfer.", "經典英國水暖平衡基準：暖氣片進水 75°C，回水 64°C，溫差剛好 11°C。調試時拿紅外測溫槍照進出水管，微調鎖閉閥使溫差穩定在 11°C 即為平衡到位。", "C&G 6035 Unit 207 Textbook Ch 7"),

        ("7.1",
         "When commissioning a modern condensing boiler system under BS 7593 / HHIC guidelines, what larger temperature drop (Delta T) between system flow and return is recommended to maximise condensing boiler efficiency?",
         "在調試現代高效冷凝燃氣壁掛爐系統時，行業協會（HHIC）推薦系統總供回水溫差（Delta T）擴大至多少，以確保回水低於露點最大化冷凝能效？",
         {"A": "5°C", "B": "20°C (e.g. Flow 70°C, Return 50°C, ensuring return is well below the 54°C dew-point)", "C": "50°C", "D": "100°C"},
         {"A": "5°C", "B": "20°C (例如供水 70°C、回水 50°C，確保回水深度跌破 54°C 露點溫度以實現持續冷凝)", "C": "50°C", "D": "100°C"},
         "B", "Modern condensing boilers operate at peak efficiency with a 20°C ΔT. A 50°C return temperature guarantees the latent heat in flue gases is recovered.", "現代冷凝爐要求「大溫差、小流量」：供水 70°C、回水 50°C（溫差 20°C）。50°C 的冰涼回水流入主換熱器，才能徹底冷卻排煙使水蒸氣結露凝結，熱效率飆升。", "Heating and Hotwater Industry Council (HHIC); Domestic Heating Design Guide"),

        # 7.2 System Controls: S-Plan, Y-Plan, Interlock & Water Treatment
        ("7.2",
         "What is an 'S-Plan' central heating and hot water control system?",
         "在英國中央供暖控制電路體系中，經典的「S-Plan 控制系統」的核心管路與閥門配置特徵是什麼？",
         {"A": "A single motorized diverter valve sharing heating and hot water", "B": "A system utilizing TWO independent 2-port spring-return motorized zone valves (one dedicated to the heating circuit, one dedicated to the hot water cylinder)", "C": "A gravity-only system without any electrical controls", "D": "A system controlled only by an open fire"},
         {"A": "採用單一的三通分流閥共享暖氣與熱水", "B": "採用「兩台完全獨立的 2 通（2-Port）彈簧復位電動分區閥門」（一台專門控制暖氣管路，另一台專門控制熱水水罐盤管）", "C": "完全無任何電氣控制的純重力對流系統", "D": "僅由壁爐火堆手動控制的系統"},
         "B", "S-Plan features two separate 2-port zone valves providing fully independent control of heating and domestic hot water. Both can run simultaneously or separately.", "S-Plan 是全英最經典、最穩定可靠的控制架構：暖氣一個閥、熱水一個閥，互不干涉。開暖氣不影響燒熱水，夏天關暖氣單獨燒水，擴展三區採暖（S-Plan Plus）極其方便。", "Honeywell Domestic Central Heating Controls Guide; C&G Unit 207"),

        ("7.2",
         "What is a 'Y-Plan' central heating and hot water control system?",
         "在供暖電氣控制體系中，廣泛應用的「Y-Plan 控制系統」的核心特徵是什麼？",
         {"A": "A system powered by yellow batteries", "B": "A system using a SINGLE 3-port mid-position motorized valve to divert primary water to Heating Only (Port A), Hot Water Only (Port B), or Mid-Position shared to both simultaneously", "C": "A system where all radiators are painted yellow", "D": "A system with no boiler"},
         {"A": "由黃色蓄電池供電的低壓系統", "B": "全系統僅採用「單個 3 通三位電動閥 (3-Port Mid-position Valve)」：通過電機與內部微動電阻聯動，切換實現單獨暖氣 (A口)、單獨熱水 (B口) 或中間位雙供 (AB雙開)", "C": "所有散熱器全部塗成黃色的系統", "D": "完全沒有鍋爐的系統"},
         "B", "Y-Plan uses one 3-port mid-position valve. It offers three distinct operating states: Hot Water only, Heating only, or Both simultaneously.", "Y-Plan 節省成本（僅需一個閥），但接線邏輯複雜：靠閥內二極管微動開關在中間位平衡電壓維持開度，若閥芯水垢卡阻維修難度高於 S-Plan。", "Honeywell Y-Plan Wiring Specification; C&G Unit 207"),

        ("7.2",
         "Under Building Regulations Approved Document L1, what is the mandatory requirement known as 'Boiler Interlock'?",
         "根據英國建築節能法規 Approved Document L1 強制規定，什麼是所有供暖系統必須具備的「壁掛爐聯鎖控制 (Boiler Interlock)」？",
         {"A": "A physical padlock locked around the boiler casing", "B": "An electrical wiring control arrangement ensuring the boiler and circulator pump are automatically switched OFF when there is no demand for heat from either the room thermostat or the cylinder thermostat", "C": "A valve that locks the water inside the radiator", "D": "An anti-theft alarm on the gas meter"},
         {"A": "鎖在壁掛爐外殼上的一把實體防盜掛鎖", "B": "一種電氣電路控制接線聯鎖機制，確保當室內溫控器與熱水罐溫控器均達到預設溫度（無熱負荷需求）時，壁掛爐燃燒器與循環水泵必須「完全強制自動關停」", "C": "將水鎖死在散熱器內部的自鎖閥門", "D": "燃氣表上的防盜防撬報警器"},
         "B", "Boiler interlock is an electrical control interlock (not a physical lock). If rooms are warm and hot water is satisfied, the boiler MUST shut down, eliminating dry cycling.", "聯鎖是節能鐵律：若僅靠散熱器恆溫閥截斷而無牆面溫控器聯鎖，各房閥門雖關閉，鍋爐卻因未得信號仍在自發反覆燃燒打轉。聯鎖徹底杜絕這種能源大浪費。", "Building Regulations Approved Document L1 Section 5; C&G Unit 207"),

        ("7.2",
         "Why should a Thermostatic Radiator Valve (TRV) NEVER be installed on the radiator in the same room / hallway where the master wall-mounted Room Thermostat is located?",
         "為什麼在安裝有全屋主牆面溫控器（Master Room Thermostat）的同一個房間或走廊內，該處的暖氣片上絕對嚴格禁止安裝「散熱器恆溫閥 (TRV)」？",
         {"A": "The radiator will explode", "B": "The two temperature sensors will 'fight' each other: if the TRV shuts off before the wall thermostat is satisfied, the wall thermostat will never reach setpoint, forcing the boiler to fire continuously 24/7", "C": "It is an electrical shock hazard", "D": "The TRV will turn blue"},
         {"A": "暖氣片會因超壓發生爆炸", "B": "兩個溫控設備會發生致命的「相互打架/控制衝突」：若暖氣片上的 TRV 提前感知水溫關死，主牆面溫控器周圍永遠達不到設定室溫，導致信號無法切斷，壁掛爐被迫 24 小時晝夜長開瘋狂空燒", "C": "存在嚴重的觸電致死風險", "D": "TRV 閥頭會自動變藍"},
         "B", "Installing a TRV in the reference room defeats the boiler interlock. The room stat never sees warm air, trapping the boiler in continuous maximum burn.", "主溫控房間暖氣片必須採用手動雙聯閥（Wheelhead）全開！若被 TRV 自行關閉，主溫控器永遠等不來暖氣，下達持續點火指令，全家其他房間被活活烤焦，燃氣費飆升。", "Domestic Building Services Compliance Guide; C&G Unit 207"),

        ("7.2",
         "What is the operational function of an Automatic Differential Bypass Valve (ABV) in a modern central heating system under Building Regulations Part L?",
         "根據建築法規 Part L 強制要求，在現代中央供暖系統中加裝「自動差壓旁通閥 (Automatic Bypass Valve - ABV)」的核心功用是什麼？",
         {"A": "To vent air to the outside", "B": "To maintain a minimum design flow rate of water through the boiler heat exchanger as individual TRVs close across the house, preventing pump cavitation, boiler lockouts, and pipe whistle", "C": "To dump water down the sewer", "D": "To increase room temperature"},
         {"A": "將管內空氣排向室外", "B": "當全屋各房間暖氣片的 TRV 恆溫閥隨室溫上升逐個關閉時，自動感應壓差並打開旁通管路，維持穿過壁掛爐主換熱器的法定最低循環流量，保護水泵免於卡死憋壓並防止鍋爐乾燒停機", "C": "將系統水全部洩入下水道", "D": "手動提升房間室溫"},
         "B", "When TRVs close, circuit resistance spikes. An ABV modulates open to sustain minimum water flow across the boiler, preventing burner cycling on high-limit overheat.", "若無旁通閥，全屋 TRV 關閉瞬間水流完全斷絕，水泵頂著死堵狂轉過熱，壁掛爐瞬間乾燒炸鍋。差壓閥在阻力超標時自發開啟短路循環，平穩過渡保護設備。", "Domestic Building Services Compliance Guide; BS EN 12828"),

        ("7.2",
         "Under BS 7593:2019, what protective device is now permanently MANDATORY on all domestic central heating system installations in the UK?",
         "根據英國國家標準 BS 7593:2019 最新強制規範，在全英所有新建或更換壁掛爐的家庭供暖系統中，哪一種保護配件被提升為法定的「永久強制必裝件」？",
         {"A": "A water softener", "B": "An in-line magnetic system filter (fitted on the primary heating return pipe upstream of the boiler)", "C": "A copper expansion vessel", "D": "A secondary bronze pump"},
         {"A": "全自動離子交換軟水機", "B": "在線磁性系統過濾器 (In-line Magnetic System Filter，強制安裝在緊鄰壁掛爐前端的採暖回水主管道上)", "C": "純銅膨脹水箱", "D": "輔助青銅增壓泵"},
         "B", "BS 7593:2019 mandates an in-line magnetic filter on the heating return to capture black iron oxide sludge (magnetite) before it enters high-efficiency boiler heat exchangers.", "2019年修訂的 BS 7593 將在線磁性過濾器（如 MagnaClean / Fernox TF1）列為法律強制項：其內部強磁芯能在黑渣黑泥流回鍋爐前將其 100% 捕獲吸附，保護高效換熱器。", "BS 7593:2019 Code of practice for preparation, commissioning and maintenance; HHIC"),

        ("7.2",
         "What is 'Magnetite' (black iron oxide sludge - Fe3O4) formed inside a wet central heating system?",
         "在供暖水力管網內部自發生成的「磁鐵礦黑泥/黑渣 (Magnetite - 黑色四氧化三鐵 Fe3O4)」是怎樣形成的？",
         {"A": "Dirt blown in through the boiler flue", "B": "A heavy, abrasive, magnetic black sludge produced by the internal electrolytic chemical corrosion of steel radiator panels in the presence of water and dissolved oxygen", "C": "Sand mixed in by the plumber", "D": "Decomposed plastic"},
         {"A": "由室外強風通過鍋爐煙道倒灌吹入的沙塵", "B": "鋼製散熱器暖氣片內壁在水與微量溶解氧的共同作用下，發生電化學內腐蝕剝落而生成的極細、具高磨損性與強磁性的黑色氧化鐵淤泥", "C": "施工人員不慎倒入口內的泥沙", "D": "塑料管道老化降解產物"},
         "B", "Magnetite is magnetic black iron oxide sludge (Fe3O4) formed by internal radiator corrosion. It settles in boiler heat exchangers and circulator impellers, causing blockages and noisy failure.", "黑泥是壁掛爐的「頭號殺手」：鋼製散熱器生鏽脫落的氧化鐵沉渣顆粒極細且具強磁性，隨水流流經壁掛爐微小換熱扁管和水泵磁電機時會死死吸附結垢，導致燒穿換熱器。", "BS 7593:2019; Sentinel / Fernox Water Treatment Guides"),

        ("7.2",
         "Under BS 7593:2019, how often must the chemical corrosion and scale inhibitor concentration in a domestic central heating system be formally tested and refreshed?",
         "根據 BS 7593:2019 供暖水維保法規，中央供暖系統內部注入的化學緩蝕阻垢劑（Chemical Inhibitor）濃度，法定必須每隔多久重新檢測並補充足量？",
         {"A": "Once every 50 years", "B": "Tested annually during scheduled boiler servicing, and full re-dosing / top-up refreshed at least every 5 years", "C": "Never", "D": "Every 24 hours"},
         {"A": "每 50 年檢測一次", "B": "在每年例行壁掛爐年檢保養時必須使用試劑或儀器檢測其有效濃度，且至少每 5 年必須進行一次全系統藥劑全量補投與更新", "C": "永久無需任何檢測補充", "D": "每 24 小時添加一次"},
         "B", "Inhibitor chemicals degrade over time. BS 7593 requires annual concentration testing (using dip strips or test kits) and mandatory refreshing of chemical dosing every 5 years.", "緩蝕劑分子會隨時間推移逐漸被腐蝕反應消耗失效。規範強制年檢拿試紙測濃度，低於閾值必須立即補加一瓶藥劑，且每 5 年必須全面重新加註，終身保護管網。", "BS 7593:2019 Section 8 Maintenance of domestic heating systems"),

        ("7.2",
         "What three sequential commissioning steps are mandatory for chemical water treatment under BS 7593:2019 before signing off a new boiler installation?",
         "根據 BS 7593:2019 標準，在正式驗收簽發一台新壁掛爐之前，供暖水路系統必須依序嚴格落實哪「三步法」標準清洗工藝？",
         {"A": "Paint the boiler, polish the taps, wipe the floor", "B": "1. Cleanse (flush with proprietary system cleaner to remove flux and installation swarf); 2. In-line magnetic filter installation; 3. Inhibit (dose with certified chemical corrosion and scale inhibitor)", "C": "Fill with tap water and leave forever", "D": "Drain the system and leave empty"},
         {"A": "給鍋爐刷漆、拋光水龍頭、擦拭地板", "B": "第一步：化學清洗（加入專用系統清洗劑動態循環徹底沖刷剝離焊劑殘渣、切削油與鐵鏽）；第二步：安裝磁性過濾器；第三步：加註經認證的化學緩蝕阻垢保護劑 (Inhibitor)", "C": "注滿自來水後永久封閉不管", "D": "將系統水全部排空保持乾涸"},
         "B", "BS 7593 mandates: 1. Chemical cleaning and power flushing, 2. Installing an in-line magnetic filter, and 3. Dosing certified corrosion inhibitor (tested with an on-site test kit).", "三步法缺一不可：不洗管路殘留的酸性焊膏幾個月就會腐蝕穿孔主換熱器；不安裝磁性過濾器黑渣無法排出；不加保護劑鋼製暖氣片會加速生鏽。正規調試必須出具加藥憑證。", "BS 7593:2019; Benchmark Commissioning Checklist"),

        ("7.2",
         "What is a 'Motorized Diverter Valve' in a W-Plan central heating system?",
         "在供暖控制工程中，採用「W-Plan 系統架構」時使用的三通切換閥（Diverter Valve）具有何種控制特性？",
         {"A": "It directs water to either hot water OR heating exclusively (priority hot water), but never to both simultaneously", "B": "It generates hot water using solar power", "C": "It controls gas pressure", "D": "It stops water hammer"},
         {"A": "它是一種「二選一」的優先切換閥：要麼將全部熱水專供生活熱水水罐（熱水優先模式），要麼全部專供暖氣片採暖，兩者「絕對無法同時雙開供暖」", "B": "利用太陽能製造高溫熱水", "C": "調節管內燃氣壓力", "D": "消除管內水錘衝擊"},
         "A", "A diverter valve (W-Plan) directs flow to Port A OR Port B exclusively. It provides priority hot water (diverting all boiler capacity to heat the cylinder rapidly before heating rooms).", "W-Plan 奉行「生活熱水絕對優先」：洗澡燒水時二通閥完全切斷暖氣片，鍋爐全功率幾分鐘燒熱水箱，水箱一滿立即翻轉閥板恢復暖氣供熱，系統成本極低。", "C&G 6035 Unit 207 Textbook Ch 7")
    ]

    for sub_id, stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref in data:
        questions.append(make_q(7, sub_id, ["Unit_207"], stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref))

    # Add 70 more questions to reach 90 for Chapter 7
    extra_c7 = [
        # Pipe Sizing, Hydraulics & Radiator Deep-Dive
        ("7.1",
         "Why is 15mm copper tube generally limited to carrying a maximum heating load of approx 4.5 kW to 6.0 kW under standard 11°C Delta T conditions?",
         "在標準供回水溫差 11°C 的家用供暖系統中，為什麼 15mm 銅管分支幹管推薦承載的最大供熱負荷上限通常被限制在 4.5 kW 至 6.0 kW 左右？",
         {"A": "The copper pipe melts at 6 kW", "B": "Exceeding this heat capacity requires a water flow rate where fluid velocity exceeds 1.0 m/s to 1.5 m/s, causing excessive frictional resistance head loss and audible water flow hiss/noise in living rooms", "C": "It makes the room too cold", "D": "15mm copper pipe cannot hold hot water"},
         {"A": "銅管在 6 kW 熱負荷下會自發融化", "B": "超過此散熱負荷所需輸送的水流量，會迫使 15mm 細管內的水流流速飆升突破 1.0 至 1.5 m/s 極限，造成沿程水頭阻力損失急劇飆升並在臥室產生刺耳的水流嘶嘶流動噪音", "C": "會使房間室溫變得過於寒冷", "D": "15mm 銅管無法承受熱水輸送"},
         "B", "Flow equation Q = m·c·ΔT. High heat loads through narrow 15mm pipes increase velocity above acoustic limits (>1.0 m/s), creating severe pump head loss and noisy pipes.", "管徑與流速水力平衡：流速超過 1 米/秒，水流摩擦管壁會發出如同蛇吐信般的滋滋水聲，且阻力劇增導致末端暖氣片吃不到水。大於 6 kW 負荷必須升級為 22mm 銅管。", "Domestic Heating Design Guide; C&G Unit 207"),

        ("7.1",
         "What copper pipe diameter is universally standard for primary flow and return distribution mains running between the boiler and heating manifolds in typical domestic dwellings?",
         "在典型英國家用住宅中央供暖工程中，連接壁掛爐與各分區閥門/分水器之間的供回水主幹管，普遍標準採用的銅管外徑是多少？",
         {"A": "10 mm", "B": "15 mm", "C": "22 mm (or 28 mm for large boilers exceeding 24 kW)", "D": "54 mm"},
         {"A": "10 mm (微口徑支管)", "B": "15 mm (單組暖氣片支管)", "C": "22 mm (或鍋爐功率超過 24 kW 時採用 28 mm 主幹管)", "D": "54 mm (商用管徑)"},
         "C", "22mm copper handles heat outputs up to approx 12-15 kW at standard design velocities, while 28mm is specified for outputs up to 25-30 kW from modern system boilers.", "主幹管負責全屋熱量總動脈。22mm 管承載 15 kW、28mm 管承載 30 kW，若主幹管誤用 15mm 粗製濫造，全屋水力循環將遭遇嚴重瓶頸卡阻，暖氣片大面積不熱。", "Domestic Heating Design Guide Table 4.1; C&G Unit 207"),

        ("7.1",
         "What is a 'Type 11' (K1) panel radiator?",
         "在鋼製板式散熱器產品代碼中，「Type 11 (K1)」散熱器具有何種幾何截面外觀？",
         {"A": "Single water-carrying front panel with a single row of welded internal convector fins", "B": "Double panels with no fins", "C": "Cast iron column radiator", "D": "A radiator with 11 tubes"},
         {"A": "單層水道前面板，背部焊接單排金屬對流散熱鰭片 (Single Panel, Single Convector - Type 11 / K1)", "B": "雙層面板無鰭片", "C": "老式鑄鐵柱形散熱器", "D": "由 11 根管組成的散熱器"},
         "A", "Type 11 (K1) features a slim profile comprising one water panel and one layer of convective fins, ideal for narrow hallways and small powder rooms.", "Type 11 是最纖薄的標準對流暖氣片（厚度僅約 50-60mm）：單板單翅片，厚度薄不佔過道空間，適合安裝在空間狹窄的小走廊、樓梯間或衛生間。", "BS EN 442; Stelrad Technical Specifications"),

        ("7.1",
         "What is a 'Type 21' (P+) panel radiator?",
         "散熱器規格中的「Type 21 (又稱 P+ 型)」散熱器，其內部構造是怎樣的？",
         {"A": "Double water-carrying panels (front and back) with a SINGLE row of internal convector fins between them", "B": "Single panel with triple fins", "C": "A radiator made of lead", "D": "A ceiling fan"},
         {"A": "雙層水道面板（前後各一塊），且兩層面板中間僅夾裝「單排 (Single Row)」對流散熱鰭片 (Type 21 / P+)", "B": "單塊面板配三排翅片", "C": "金屬鉛製造的散熱器", "D": "吊頂排風扇"},
         "A", "Type 21 (P+) provides double water panels with one internal fin row, delivering intermediate heat output between a slim Type 11 and a deep Type 22.", "Type 21（P+）是兼顧厚度與散熱量的折中產品：外觀為前後雙水板，中間單翅片，厚度比 Type 22 薄約 30%，在窗台深度受限時廣泛替代 Type 22。", "BS EN 442; Radiator Engineering Manual"),

        ("7.1",
         "What is a 'Type 33' (K3) panel radiator?",
         "高熱負荷場所專用的「Type 33 (K3 型)」超強散熱器，其內部由幾層面板和翅片疊加而成？",
         {"A": "Triple water-carrying panels with TRIPLE rows of internal convector fins", "B": "Single panel with 33 fins", "C": "A radiator 33 meters long", "D": "Three pipes welded together"},
         {"A": "三層水道面板（前中後三塊），且夾層內焊接「三排 (Triple Rows)」對流散熱鰭片 (Type 33 / K3)", "B": "單層面板焊接 33 個翅片", "C": "長達 33 米的超長暖氣片", "D": "三根水管簡單焊接"},
         "A", "Type 33 (K3) features three water panels and three fin rows, producing massive heat output in compact wall widths, ideal for low-temp heat pump conversions.", "Type 33（三板三翅片）是暖氣片中的「巨無霸」：厚度超過 160mm，散熱量是同長度普通單板的近 3 倍，在老房改裝低溫熱泵而牆面長度有限時是救命稻草。", "BS EN 442; Heat Pump Emitter Sizing Guide"),

        ("7.1",
         "Under British Standards BS EN 12831, what four core variables are required to calculate the design heat loss (in Watts) of a room through external fabric?",
         "根據歐洲/英國標準 BS EN 12831 建築熱負荷計算方法，計算一個房間圍護結構傳熱散熱損失（瓦特 W）時，必須代入哪四個核心計算參數？",
         {"A": "Fabric surface area (A), thermal transmittance (U-value), internal design temperature (T_int), and external design temperature (T_ext)", "B": "Plumber weight, pipe length, boiler price, wall color", "C": "Water hardness, copper density, gas pressure, wind speed only", "D": "Room volume multiplied by 1000"},
         {"A": "圍護構件表面積 (A)、傳熱係數 (U-value)、室內設計計算溫度 (T_int) 以及室外冬季計算溫度 (T_ext)", "B": "水暖工體重、管道長度、鍋爐售價及牆面顏色", "C": "水質硬度、純銅密度、燃氣表壓及風速", "D": "房間體積直接粗暴乘以 1000"},
         "A", "Fabric heat loss equation: Q_fabric = Area (m²) × U-value (W/m²K) × (T_internal - T_external). Added to ventilation heat loss, this gives total room heating demand.", "熱負荷科學計算基本公式：傳熱散熱量 = 面積 × U 值 × 內外溫差 ΔT。再加上門窗通風滲透熱損失（Q_vent），兩者之和即為該房間所需的散熱器精確匹配功率。", "BS EN 12831 Heating systems in buildings - Method for calculation of design heat load"),

        ("7.1",
         "What is the standard design internal room temperature recommended by CIBSE and Building Regulations for domestic living rooms in the UK?",
         "根據英國特許建築設備工程師學會 (CIBSE) 及建築法規推薦，住宅起居客廳（Living Room）冬季標準室內設計計算溫度是多少？",
         {"A": "15°C", "B": "18°C", "C": "21°C", "D": "28°C"},
         {"A": "15°C", "B": "18°C (臥室標準推薦溫度)", "C": "21°C (起居客廳標準舒適計算溫度)", "D": "28°C"},
         "C", "CIBSE Domestic Heating Design Guide recommends: Living rooms 21°C, Bedrooms 18°C, Bathrooms 22°C, Hallways/Kitchens 18°C.", "CIBSE 標準室內計算溫標：客廳為人體久坐放鬆場所標準取 21°C；臥室有被褥取 18°C；浴室人體脫衣洗澡取最高 22°C；廚房走廊有活動取 18°C。", "CIBSE Guide A: Environmental design; Domestic Heating Design Guide"),

        ("7.1",
         "If a domestic bathroom requires 1,200 Watts of design heat output under Delta T 50, but the property operates on a low-temperature heat pump with a radiator correction factor of 0.45, what catalog rated output (at Delta T 50) must the selected radiator have?",
         "某住宅衛生間經熱負荷計算需 1,200 W 散熱量（原 ΔT 50 基準）。若該住宅改為低溫空氣源熱泵供暖，查表得散熱器修正係數為 0.45。則技師在暖氣片廠家樣冊上，必須選用標定功率為多少瓦（ΔT 50 標定）的散熱器？",
         {"A": "540 Watts", "B": "1,200 Watts", "C": "2,667 Watts (1,200 W / 0.45)", "D": "10,000 Watts"},
         {"A": "540 瓦特", "B": "1,200 瓦特", "C": "2,667 瓦特 (計算：1,200 ÷ 0.45 ≈ 2,667 W)", "D": "10,000 瓦特"},
         "C", "Catalog Output = Design Heat Required / Correction Factor = 1200 W / 0.45 = 2,666.7 Watts. A radiator rated at ~2.7 kW at ΔT 50 is needed to emit 1.2 kW at low temp.", "修正選型計算：樣冊標註額定功率 = 房間實際需熱量 ÷ 修正係數 = 1200 ÷ 0.45 ≈ 2667 W。在低水溫下唯有選裝這台看似「超大」的暖氣片，實際出熱才剛好夠用。", "BS EN 442 Selection Tables; MCS MIS 3005"),

        ("7.1",
         "When installing a TRV on a radiator, what feature on modern bi-directional TRVs prevents the valve from chattering/hammering regardless of which pipe end it is installed on?",
         "在現代散熱器上安裝具備「雙向流動自適應 (Bi-directional)」特性的優質恆溫閥（TRV）時，閥芯內部的何種機械設計徹底消除了因水流方向反向引起的閥瓣高頻拍打水錘噪聲？",
         {"A": "A built-in electric motor", "B": "A spring-damped, balanced dual-seat or contoured conical jumper that prevents fluid hydrodynamic forces from violently slamming the washer shut against flow", "C": "A manual lock", "D": "An air vent"},
         {"A": "內置微型電動機", "B": "帶彈簧阻尼的動態平衡閥瓣或特製流線錐形閥芯，徹底消除了流體動壓反向將橡膠平閥片強行猛烈吸撞閥座引發的連續機槍式拍打水錘噪聲（Chatter）", "C": "手動機械鎖緊插銷", "D": "自帶自動排氣閥"},
         "B", "Old directional TRVs hammered if water flowed backward over the seat. Modern bi-directional TRVs utilize balanced hydrodynamic seats, operating quietly in either flow direction.", "老式 TRV 嚴格區分進回水，裝反了水流會像機關槍一樣瘋狂敲打；現代雙向 TRV 採用流線型對稱閥瓣，無論裝在進水端還是回水端，水流衝擊均受阻尼平衡，靜音運行。", "BS EN 215 Thermostatic radiator valves; Drayton / Danfoss Technical Guides"),

        ("7.1",
         "What is the number '0' or '*' setting on a standard domestic Thermostatic Radiator Valve head designed to represent?",
         "在普通家用散熱器恆溫控制閥頭（TRV）刻度盤上，標註的數字「0」或「雪花符號 (*)」代表何種法定保護工況？",
         {"A": "The radiator is heated to maximum 100°C", "B": "Frost Protection mode (the valve shuts off fully during normal ambient temps, but automatically cracks open if room temperature falls below approx 6°C to 8°C to prevent pipe freezing)", "C": "The valve is broken", "D": "The boiler switches to solar mode"},
         {"A": "散熱器全速加熱至 100°C 沸點", "B": "防凍保護模式 (Frost Protection)：在常溫下閥門完全關死停暖；一旦室內氣溫驟降至約 6°C 至 8°C 冰點邊緣時，閥芯自動微啟通水，防止房間管道結冰凍裂", "C": "代表閥門內部已損壞報廢", "D": "壁掛爐自動切換為太陽能模式"},
         "B", "The asterisk (*) frost setting keeps the valve closed to save fuel, but opens automatically if the space approaches freezing (6-8°C), preventing catastrophic burst pipes in vacant rooms.", "雪花檔絕不是完全切斷：它是全屋防凍衛士。冬天空置臥室開雪花檔，房間不供熱省燃氣；但半夜寒潮降溫至 7°C 時它自動開水防凍，白天回溫又自動關閉。", "BS EN 215; C&G Unit 207"),

        # 7.2 System Controls & Water Treatment Deep-Dive
        ("7.2",
         "In standard S-Plan wiring, which control device sends the 230V switched live call signal to the Brown wire of the heating zone valve?",
         "在英國標準的 S-Plan 供暖控制接線體系中，是哪一個溫控設備直接向採暖分區閥的「棕色導線 (Brown)」發送 230V 供電信號以驅動閥門電機開啟？",
         {"A": "The gas meter", "B": "The Room Thermostat (or programmable room stat call terminal)", "C": "The cylinder thermostat", "D": "The kitchen cooker"},
         {"A": "室外燃氣計量表", "B": "室內牆面溫控器 (Room Thermostat) 或可編程溫控器的點火輸出端子 (Call Terminal)", "C": "熱水水罐溫控器", "D": "廚房燃氣烹飪灶具"},
         "B", "The room thermostat senses low air temperature and switches 230V power to the heating zone valve's Brown wire. Once open, the valve's end-switch fires the boiler and pump.", "控制鏈條：定時器通電 → 房間溫控器檢測室溫低 → 觸點閉合將火線送到電動閥棕線 → 電機開閥到位頂合微動開關 → 橙線給電點火壁掛爐與水泵。", "Honeywell S-Plan Wiring Diagram; BS 7671"),

        ("7.2",
         "In standard S-Plan wiring, which control device sends the 230V call signal to the Brown wire of the hot water zone valve?",
         "在 S-Plan 接線電路中，是哪一個控制元件負責向熱水專用分區閥的「棕色線」輸出 230V 動作指令以驅動熱水開閥？",
         {"A": "The bathroom light switch", "B": "The Cylinder Thermostat (terminal 1 / Call for heat terminal)", "C": "The master room stat", "D": "The garden tap"},
         {"A": "浴室照明燈開關", "B": "水罐表面溫控器 (Cylinder Thermostat) 的「求熱端子 (Terminal 1 / Call Terminal)」", "C": "客廳主牆面溫控器", "D": "花園室外龍頭"},
         "B", "The cylinder thermostat monitors stored water temperature. When water drops below setpoint (e.g. <60°C), it routes 230V to the hot water valve motor.", "熱水控制鏈條：定時器熱水通道給電 → 水罐溫控器感知水溫低於 60°C → 內部觸點 1 閉合輸出 230V 驅動熱水二通閥電機開閥 → 閥門到位閉合微動開關點火壁掛爐。", "Honeywell Controls Wiring Specification; C&G Unit 207"),

        ("7.2",
         "What is an 'S-Plan Plus' system commonly installed in large residential properties?",
         "在英國大中型豪華別墅住宅中，廣泛採用的「S-Plan Plus 控制系統」具有何種多迴路擴展特徵？",
         {"A": "A system using solar electricity only", "B": "A system using THREE or more 2-port motorized zone valves (typically two separate space heating zones e.g. upstairs bedrooms and downstairs living, plus one hot water cylinder zone)", "C": "A system without radiators", "D": "A system with three boilers running simultaneously"},
         {"A": "完全依靠太陽能光伏供電的系統", "B": "採用「三台或更多台獨立 2 通電動分區閥」的系統（通常至少劃分為兩個獨立採暖溫區，如樓上臥室區、樓下客廳生活區，外加一個獨立熱水水罐分區）", "C": "完全不配置任何暖氣片的系統", "D": "三台壁掛爐同時並聯點火的系統"},
         "B", "S-Plan Plus provides independent zoning complying with Part L (>150m² properties require independent living and sleeping heating zones), each controlled by its own 2-port valve.", "Part L 節能法規規定：建築面積超 150 平方米的新建住宅必須實行樓層分區控溫。S-Plan Plus 用 3 個閥門分別控制樓上、樓下和生活熱水，節省 15% 以上燃氣。", "Building Regulations Approved Document L1 Section 5; C&G Unit 207"),

        ("7.2",
         "What happens in a Y-Plan system if the electrical supply to the 3-port mid-position valve head is completely severed or switched off?",
         "在 Y-Plan 供暖控制系統中，若驅動 3 通中位閥電機的電線被切斷或定時器全部關閉處於無電狀態時，閥門內部彈簧會將閥板自動復位到哪個端口？",
         {"A": "Port A (Heating only)", "B": "Port B (Hot Water only) via mechanical spring-return", "C": "Mid-position permanently", "D": "All ports close 100%"},
         {"A": "A 端口 (僅供暖氣)", "B": "B 端口 (僅供生活熱水 - 通過內部機械彈簧自動復位)", "C": "永久死鎖在中間位", "D": "所有端口 100% 全部關閉封死"},
         "B", "A 3-port mid-position valve is spring-return to Port B (Hot Water). When totally de-energized, mechanical springs pull the paddle across to rest in the Hot Water position.", "Y-Plan 閥門默認狀態：在斷電無控制信號時，內置高強機械彈簧自動將橡膠閥瓣拉回覆位，封閉 A 口（暖氣），敞開 B 口（熱水），確保熱水通道永遠具備通流釋放安全路徑。", "Honeywell 3-Port Mid-Position Valve V4073A Technical Sheet"),

        ("7.2",
         "When power flushing an existing, heavily-sludged central heating system using an acidic chemical flushing agent (such as Fernox F5 or Sentinel X800), how should each radiator be cleaned for maximum velocity?",
         "使用強效脈衝清洗泵（Power Flushing Machine）對重度結垢淤堵的供暖管網進行化學動力清洗時，現場應當如何操作各暖氣片閥門以確保獲得最大沖刷流速？",
         {"A": "Leave all radiators fully open at the same time", "B": "Isolate all radiators across the property, then open and flush ONE radiator at a time to focus 100% of the pump's scouring flow velocity through that single emitter", "C": "Remove all radiators from the walls and flush in the garden", "D": "Boil the radiators with a blowlamp"},
         {"A": "將全屋所有暖氣片的閥門全部敞開同時沖刷", "B": "將全屋其他所有暖氣片全部關死，集中水泵 100% 的全部揚程與紊流沖刷動能，「一次只單獨開啟並徹底沖洗一組暖氣片」，逐組循環沖刷乾淨", "C": "將全屋散熱器全部拆下搬到花園草坪沖洗", "D": "用噴燈烈焰烘烤暖氣片"},
         "B", "Power flushing requires concentrating full pump turbulence through individual radiators one by one. Opening all radiators dissipates velocity, preventing sludge mobilization.", "「逐個擊破」是動力清洗鐵律：若所有閥門全開，大流量被分散流速大幅衰減，根本衝不動沉澱在暖氣片底部的板結黑泥。唯有關閉其他全開一組，暴烈紊流才能將黑渣連根拔起。", "BS 7593:2019 Appendix A; Kamco Power Flushing Code of Practice"),

        ("7.2",
         "What is the function of the permanent earth bonding strap fitted across the copper pipes on either side of an in-line central heating magnetic filter?",
         "在供暖管道上安裝在線磁性過濾器時，為什麼常在過濾器前後兩側的金屬銅管之間跨接一條專用「等電位接地跨接導線 (Earth Continuity Bonding Strap)」？",
         {"A": "To charge the filter magnets with electricity", "B": "To maintain electrical earth continuity across the pipework circuit if the filter body (plastic or isolated) is removed for cleaning or replacement, protecting personnel from electric shock", "C": "To filter sediment", "D": "To heat up the filter"},
         {"A": "為過濾器內部的強磁鐵充磁", "B": "保持管道電氣保護接地線路的連續性；當塑料材質的過濾器被拆卸下來清洗排污時，跨接線能維持管道兩端電氣通路不中斷，防止施工人員觸電致死", "C": "輔助吸附微細泥沙", "D": "給過濾器通電加熱"},
         "B", "Plumbing pipework often acts as extraneous conductive parts. Inserting a non-metallic filter breaks electrical continuity unless a green/yellow earth link is bridged across the gap.", "BS 7671 電氣安全底線：若水管充當了等電位聯結通路，切開管子裝入塑料過濾器就會造成接地中斷。跨接綠黃接地線，確保日後技師拆下過濾器清洗時絕不會遭意外漏電擊傷。", "BS 7671:2018 Regulation 543.3; C&G Unit 207/208"),

        ("7.1",
         "What is the purpose of an 'Air Bleed Vent' (air release plug) fitted to the top corner of every panel radiator?",
         "安裝在每組板式散熱器暖氣片頂部角落的「手動排氣閥嘴 (Air Bleed Vent / Valve)」的核心功用是什麼？",
         {"A": "To pour inhibitor into the radiator", "B": "To vent trapped air and non-condensable gases (such as hydrogen formed by internal corrosion) that accumulate at the top of the radiator, restoring full hot water contact across the emitter face", "C": "To drain all water out of the radiator", "D": "To increase water pressure"},
         {"A": "用以向散熱器內部加注化學阻垢劑", "B": "排出積聚在暖氣片頂部的游離空氣與不凝性氣體（如金屬電化學內腐蝕釋放出的易燃氫氣），消除氣囊氣阻，使高溫熱水重新注滿散熱器頂部表面", "C": "將暖氣片內部的存水全部排乾", "D": "提升管網內部的工作水壓"},
         "B", "Air rises to the top of radiators, forming cold zones where heat cannot emit. Venting using a radiator key bleeds trapped gases until a steady stream of water emerges.", "氣體比水輕自然飄向頂端。若暖氣片「上半截冰涼、下半截滾燙」，99% 是氣塞！用排氣鑰匙逆時針擰開半圈，嘶嘶排盡空氣直到水滴滲出，頂部立即溫暖如初。", "C&G Unit 207 Central Heating Maintenance"),

        ("7.2",
         "Why is a build-up of air and gas inside radiators in an untreated central heating system often highly flammable (containing Hydrogen gas)?",
         "在未添加化學防腐阻垢劑的老舊供暖系統中，從暖氣片頂部排氣孔排出的積聚氣體，為什麼往往具有「易燃爆炸性」（富含高濃度氫氣 H2）？",
         {"A": "Natural gas leaks through the boiler heat exchanger into the water", "B": "Internal anaerobic electrolytic corrosion of steel radiators produces Hydrogen gas as a chemical byproduct (3Fe + 4H2O → Fe3O4 + 4H2↑)", "C": "The water has decomposed into oxygen and kerosene", "D": "Electricity creates hydrogen"},
         {"A": "燃氣管道的天然氣穿透鍋爐換熱器滲漏進了水裡", "B": "鋼製散熱器內壁在無氧環境下發生電化學酸性腐蝕，鐵與水分子反應生成四氧化三鐵（黑渣）的同時，化學副產物大量析出並釋放高純度易燃的「氫氣 (Hydrogen Gas)」", "C": "水在低溫下自發分解為氧氣和煤油", "D": "水泵運轉電解水產生了氫氣"},
         "B", "Corrosion chemistry: 3Fe + 4H2O → Fe3O4 (magnetite) + 4H2 (hydrogen gas). Trapped radiator gas in corroding systems is hydrogen and will ignite if exposed to naked flames.", "水暖經典化學反應：鐵金屬在水中生鏽時，會將水中的氫離子置換還原為純氫氣（H2）。排氣時若有學徒在旁邊嘴叼香煙或點打火機照亮，噴出的氣體會瞬間被點燃爆燃燒傷面部！", "BS 7593:2019; C&G Unit 207 Heating Science"),

        ("7.1",
         "What tool is used to adjust the internal spindle of a radiator Lockshield Valve during system balancing?",
         "在對散熱器進行水力平衡調試時，水暖工使用何種專用工具旋轉並精細微調「鎖閉平衡閥 (Lockshield Valve)」的內部無手輪閥桿？",
         {"A": "A large sledgehammer", "B": "An adjustable spanner or dedicated lockshield key (radiator spud / gland wrench)", "C": "A blowlamp", "D": "A hacksaw"},
         {"A": "重型八角大鐵錘", "B": "活口扳手、套筒扳手或專用鎖閉閥調節鑰匙 (Lockshield Key)", "C": "高溫動火噴燈", "D": "鋼鋸條"},
         "B", "Lockshield valves lack plastic handwheels to prevent occupants altering the balance. The rectangular brass stem is adjusted with a spanner or key.", "鎖閉閥故意做成無手輪光桿（蓋上塑料防拆罩），就是防範業主隨意擰動破壞全屋水力平衡。技師拿下保護罩，拿小活口微調半圈即可設定阻力。", "BS EN 215; C&G Unit 207 Commissioning"),

        ("7.2",
         "Under BS 7593:2019, what should be done with a central heating system containing an old, incompatible chemical inhibitor before dosing a new brand of inhibitor?",
         "根據 BS 7593:2019 水質標準，在一套已含有老舊未知化學藥劑的供暖系統中加注全新品牌的緩蝕劑前，必須執行何種前置清理工藝？",
         {"A": "Pour the new chemical directly on top of the old one", "B": "Thoroughly flush the entire system with clean mains water to completely drain and remove the legacy chemical residues, preventing unpredictable chemical coagulation or precipitation", "C": "Boil the system at 100°C for a week", "D": "Do nothing"},
         {"A": "不經任何處理，直接將新品牌的化學藥水混合倒入老藥水裡面", "B": "使用潔淨自來水對全系統進行徹底的反覆沖洗與排空，完全清洗乾淨既有殘留化學成分，防止不同化學配方混合發生酸鹼拮抗中和、化學絮凝結塊或沉澱失效", "C": "在 100°C 沸點下連續烘煮系統一整週", "D": "完全無需做任何清理動作"},
         "B", "Different chemical brands utilize different organic/inorganic inhibitor technologies (molybdates vs silicates). Mixing brands can cause chemical clashes, forming jelly sludges.", "不同藥廠配方迥異：有的呈弱鹼性，有的含鉬酸鹽或矽酸鹽。雜亂混加會引發化學絮凝反應，生成膠狀果凍果凍泥堵死水泵，換藥前必須拿清水沖乾淨。", "BS 7593:2019 Section 7; Fernox / Sentinel Application Notes")
    ]

    for sub_id, stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref in extra_c7:
        questions.append(make_q(7, sub_id, ["Unit_207"], stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref))

    from .ch07_part2 import get_part2_questions
    questions.extend(get_part2_questions())

    return questions
