# Chapter 7 Part 2: Additional 50 Questions (Questions 41 to 90)
from .utils import make_q

def get_part2_questions():
    questions = []
    
    data = [
        # 41. Heat loss calculations
        ("7.1",
         "In domestic heating design under BS EN 12831, what is the fundamental formula used to calculate the fabric heat conduction loss (Q in Watts) through an external building element?",
         "根據英國/歐洲供暖設計標準 BS EN 12831，計算房屋外圍護結構（外牆、屋頂、窗戶）織物熱傳導損失（Q，單位為瓦特 W）的基本物理公式是什麼？",
         {"A": "Q = Mass × Velocity", "B": "Q = U-value × Area (m²) × Temperature difference (ΔT in Kelvin or °C)", "C": "Q = Voltage × Current", "D": "Q = Volume ÷ Pressure"},
         {"A": "Q = 質量 × 速度", "B": "Q = 傳熱係數 (U-value, W/m²K) × 構件表面積 (m²) × 內外溫差 (ΔT, K 或 °C)", "C": "Q = 電壓 × 電流", "D": "Q = 體積 ÷ 壓力"},
         "B", "Fabric heat loss formula: Q = U × A × ΔT. Multiplying the element's thermal transmittance (U) by its surface area (A) and the design temperature gradient (ΔT) gives heat loss in Watts.", "建築圍護結構散熱基本公式：Q = U × A × ΔT。U 值越小保溫越好；窗戶或外牆面積越大、室內外溫差越懸殊，每小時散失的熱量（瓦特 W）就越高。", "BS EN 12831 Energy performance of buildings; C&G Unit 207"),

        # 42. Room design temperatures
        ("7.1",
         "According to CIBSE Domestic Heating Design Guide, what are the standard design internal comfort temperatures for a living room and a bedroom respectively in the UK?",
         "根據英國特許特許建造設備工程師學會（CIBSE）住宅供暖設計指南，英國客廳（Living Room）與臥室（Bedroom）的標準室內基準設計舒適溫度分別是多少？",
         {"A": "Living room 15°C, Bedroom 12°C", "B": "Living room 21°C, Bedroom 18°C", "C": "Living room 28°C, Bedroom 25°C", "D": "Living room 10°C, Bedroom 20°C"},
         {"A": "客廳 15°C，臥室 12°C", "B": "客廳 21°C，臥室 18°C", "C": "客廳 28°C，臥室 25°C", "D": "客廳 10°C，臥室 20°C"},
         "B", "Standard UK room design temperatures: Living areas 21°C, Bedrooms 18°C, Hallways/stairs 18°C, Bathrooms 22°C (for occupant comfort when undressed).", "CIBSE 標準室內設計溫度：客廳需長時間靜坐放鬆，設定 21°C；臥室有被褥保暖，設定 18°C；走廊過道 18°C；浴室因人脫衣洗浴，需更高設定為 22°C。", "CIBSE Domestic Heating Design Guide; BS EN 12831"),

        # 43. Delta T correction factor
        ("7.1",
         "If a radiator is rated at 2,000 Watts under standard Delta T 50°C, what happens to its actual heat output if operating in a low-temperature system at Delta T 30°C?",
         "若某組暖氣片在標準 ΔT 50°C 工況下的額定散熱量為 2,000 W，當它運行在進水溫更低的低溫供暖系統（ΔT 30°C，修正係數約為 0.51）時，其散熱量大約變為多少？",
         {"A": "It increases to 4,000 Watts", "B": "It drops to approximately 1,020 Watts (roughly half of its rated output)", "C": "It remains exactly 2,000 Watts", "D": "It drops to 0 Watts"},
         {"A": "散熱量增加到 4,000 W", "B": "散熱量大幅衰減至約 1,020 W（大約僅為額定標稱輸出的一半）", "C": "散熱量依然保持精確的 2,000 W 不變", "D": "散熱量徹底降為 0 W"},
         "B", "At ΔT 30, the correction factor is approx 0.515. Radiator output is non-linear: 2000 W × 0.515 ≈ 1030 W. Radiators must be significantly upsized on low-temperature circuits.", "散熱器輸出隨水溫非線性衰減：ΔT 30 時修正係數約 0.51。原本 2000W 的大暖氣片只能釋放約 1020W 熱量，因此熱泵或冷凝低溫系統必須配備大散熱片。", "BS EN 442 Correction Factors; Stelrad Radiator Technical Manual"),

        # 44. Pipe sizing by heat capacity
        ("7.1",
         "In a traditional wet central heating system operating at a 20°C temperature drop (Delta T 20°C), what is the maximum recommended heating load typically carried by a 15mm copper pipe?",
         "在設計供回水溫差為 20°C（ΔT 20°C）的傳統雙管供暖系統中，一根標準 15mm 紫銅供水支管通常最大推薦承載多大功率的散熱器熱負荷？",
         {"A": "Up to approximately 6 kW (6,000 Watts)", "B": "Up to 50 kW", "C": "Up to 100 kW", "D": "Up to 0.5 kW only"},
         {"A": "最大約 6 kW (6,000 瓦特)", "B": "最高可達 50 kW", "C": "最高可達 100 kW", "D": "僅限 0.5 kW"},
         "A", "At ΔT 20°C with velocity around 0.8 m/s, 15mm copper can transport roughly 5.5 to 6.0 kW of heat. 22mm carries up to ~18 kW, and 28mm carries up to ~35 kW.", "水暖管徑負荷速查（ΔT 20°C）：15mm 銅管極限承載約 6 kW（帶 3-4 組普通暖氣片）；22mm 幹管承載約 18 kW；28mm 主幹管承載約 35 kW。", "Copper Development Association Guide; Domestic Heating Design Guide"),

        # 45. Pipe velocity limits
        ("7.1",
         "Why must water velocity inside domestic central heating pipework generally be designed between 0.5 m/s and 1.5 m/s?",
         "為什麼家用中央供暖管道內的水流流速通常必須嚴格設計控制在 0.5 m/s 至 1.5 m/s 的安全合理區間內？",
         {"A": "Below 0.5 m/s air and debris cannot be swept away, while above 1.5 m/s excessive water noise (hissing) and pipe erosion occur", "B": "Faster water makes the boiler explode", "C": "Slower water freezes immediately", "D": "Regulations require water to move at sonic speed"},
         {"A": "低於 0.5 m/s 管內氣泡和微沉澱無法被水流帶走造成氣塞氣堵；高於 1.5 m/s 則會引發劇烈的管道水流噪聲（嘶嘶聲）並加劇銅管內壁沖刷腐蝕減薄", "B": "流速過快會引發壁掛爐爆炸", "C": "流速低於 0.5 m/s 水流會瞬間結冰", "D": "法規強制要求水流必須達到音速"},
         "A", "Velocities below 0.5 m/s cause air bubbles and sediment to settle in horizontal pipes. Velocities exceeding 1.5 m/s generate audible noise and erode copper elbows.", "水暖流速黃金區間：0.5 - 1.5 m/s。太慢了排不走氣泡，氣塞暖氣片不熱；太快了水流在彎頭處發出惱人的呼嘯嘶嘶聲，且長時間會沖穿銅管薄壁造成暗漏。", "BS EN 12828 Heating systems in buildings; C&G Unit 207"),

        # 46. Radiator valve types
        ("7.1",
         "When connecting central heating pipework emerging vertically from a timber floor directly into the bottom side connections of a panel radiator, which type of radiator valve body must be selected?",
         "當供回水銅管從木地板下方垂直向上穿出地面，直接接入散熱器兩側底部的進出水口時，應選用何種閥體結構形狀的散熱器閥門？",
         {"A": "Straight valve (In-line)", "B": "Angled valve (90-degree bend between inlet and outlet tail)", "C": "Corner valve only", "D": "Gate valve"},
         {"A": "直通閥 (Straight valve)", "B": "直角角閥 (Angled valve - 入口與出水接嘴呈 90 度垂直拐角)", "C": "僅限特種轉角閥", "D": "大口徑閘閥"},
         "B", "Angled valves feature a 90° turn, perfect for pipes coming up through floorboards to meet horizontal radiator side connections. Straight valves are used when pipes run along skirting horizontally.", "閥門選型常識：管道由地板垂直向上走、水平接入暖氣片，使用 90° 角閥（Angled Valve）；管道若沿踢腳線水平走明管，則使用直通閥（Straight Valve）。", "C&G Unit 207 Central Heating Fittings"),

        # 47. Radiator mounting height
        ("7.1",
         "What is the recommended minimum clearance distance between the underside of a wall-mounted panel radiator and the finished floor level?",
         "壁掛安裝鋼製板式散熱器暖氣片時，散熱器底部邊緣與完成面地板（Finished Floor Level）之間推薦保持的最小淨空距離是多少？",
         {"A": "At least 100mm to 150mm (to allow unobstructed natural convective air inflow)", "B": "Zero mm (flush touching the carpet)", "C": "500mm", "D": "1,000mm"},
         {"A": "至少 100mm 至 150mm（以確保冷空氣自底部無阻礙順暢吸入對流鰭片）", "B": "0 mm（直接緊貼地毯坐落在地面上）", "C": "500mm", "D": "1,000mm"},
         "A", "Radiators heat mainly by convection. A minimum 100-150mm clearance allows cool floor-level air to be drawn smoothly into the bottom of the convector fins.", "對流散熱物理要求：暖氣片就像熱氣煙囪，必須在底部留出 100-150mm 的空間讓地面冷空氣順暢流入翅片。緊貼地面會掐死對流進風，導致散熱量暴跌 30% 以上。", "BS EN 442 Installation Guidance; C&G Unit 207"),

        # 48. Radiator location under windows
        ("7.1",
         "Why are domestic central heating radiators traditionally mounted directly beneath external window sills?",
         "在傳統建築供暖佈局中，散熱器暖氣片為什麼普遍優先推薦安裝在對外窗戶的窗台正下方？",
         {"A": "To block sunlight from entering", "B": "To intercept and neutralize cold downdrafts descending from the cold window glass, warming the air immediately and creating even room temperature distribution", "C": "Because pipes cannot be routed anywhere else", "D": "To dry the window curtains"},
         {"A": "阻擋室外陽光照進室內", "B": "及時攔截並中和由冰冷窗玻璃表面自然下沉形成的冷風下沉氣流（Cold Downdraft），使其被暖氣片熱浮力托起混和加熱，形成全屋均勻舒適的溫度場", "C": "因為水管只能鋪設在窗台下", "D": "用來烘乾窗簾布"},
         "B", "Cold window glass cools adjacent air, which drops to the floor as a cold draft. Placing the radiator beneath the window warms this air, counteracting drafts and circulating warm air into the room.", "暖通氣流組織原理：窗戶是房屋保溫最脆弱的薄弱點，冷空氣沿玻璃下落流向腳面形成刺骨穿堂風。窗下暖氣片升騰的熱空氣第一時間阻斷冷氣流，大大改善舒適度。", "CIBSE Domestic Heating Design Guide; C&G Unit 207"),

        # 49. Radiator reflective foil
        ("7.1",
         "What is the energy-saving benefit of installing reflective radiator foil (or radiator reflector panels) on the external wall directly behind a radiator?",
         "在靠外牆安裝的暖氣片背部牆面上加裝「專用鋁箔隔熱反光板 (Radiator Reflective Foil)」具有何種顯著節能效益？",
         {"A": "It generates free electricity", "B": "It reflects radiant heat back into the living room rather than allowing it to be conducted and lost wastefully through the cold solid external wall", "C": "It eliminates the need for a boiler", "D": "It cools the room in winter"},
         {"A": "自發產生免費電能", "B": "將暖氣片背面朝向外牆發射的紅外熱輻射反射回室內生活空間，防止高溫熱量直接通過冰冷的未保溫外牆大量導熱散失至室外", "C": "使系統不再需要燃氣壁掛爐", "D": "在冬天為房間強制降溫"},
         "B", "External walls behind radiators can reach high temperatures, causing high transmission heat loss. Reflective foil bounces radiant heat back into the room, reducing wall heat loss by up to 30%.", "隔熱反光板原理：暖氣片背對牆壁高溫烘烤，外牆溫度飆升導致大量熱量穿牆逃逸。反光箔能反射 95% 的熱輻射回屋內，對無外牆保溫的老舊實心磚房節能尤為顯著。", "Energy Saving Trust Guidance; Approved Document L1"),

        # 50. Column radiators thermal inertia
        ("7.1",
         "Compared to modern thin steel panel radiators, what is the thermal characteristic of traditional cast iron or multi-column sectional radiators?",
         "與現代輕薄型鋼製板式散熱器相比，傳統鑄鐵散熱器或多柱式重型散熱器具有何種熱力學特性？",
         {"A": "Zero heat capacity", "B": "Much larger internal water volume and heavy metallic mass, resulting in high thermal inertia (slow to heat up, but retaining and emitting heat for a long time after shutdown)", "C": "Instantaneous heating within 5 seconds", "D": "Inability to heat water"},
         {"A": "完全零熱容", "B": "內部容水量巨大且金屬壁厚自重重，具有極高的「熱惰性」（升溫響應慢，但在壁掛爐停機後能長時間持續蓄熱並緩慢放熱）", "C": "通水 5 秒鐘即可瞬間達到最高溫度", "D": "完全無法向水傳遞熱量"},
         "B", "Cast iron and column radiators have high water content and heavy mass. They take longer to warm up (high thermal mass) but continue releasing gentle radiant warmth long after the boiler turns off.", "熱工特性對比：鋼板散熱器容水量小升溫極快；鑄鐵柱式散熱器自重重、存水量大，熱得慢、冷得也慢（熱惰性大），能提供平穩持久的輻射保溫體驗。", "BS EN 442; C&G Unit 207"),

        # 51. Fan convector emitters
        ("7.1",
         "What is an electric 'Fan Convector' (or kickspace heater) commonly installed beneath kitchen base units?",
         "在現代廚房櫥櫃底座踢腳板下方廣泛安裝的「風機盤管對流散熱器 (Kickspace Fan Convector)」，其工作原理是什麼？",
         {"A": "A microwave food warmer", "B": "A compact, finned copper tube heat exchanger connected to the central heating circuit, equipped with an electric fan that forces warm air out across the floor", "C": "A refrigerator compressor", "D": "A gas burner installed inside the cabinet"},
         {"A": "微波食物加熱器", "B": "接入供暖水管網的小型緊湊型銅管鋁翅片換熱器，內置低噪聲微型電動風機，強制抽取冷風吹過翅片，並將強勁暖風從踢腳線水平吹向地面", "C": "廚房冰箱壓縮機", "D": "安裝在櫥櫃內部的燃氣明火燃燒器"},
         "B", "Fan convectors use a miniature heat exchanger coil and an electric fan to blow high volumes of warm air through plinth grilles, delivering high heat output where wall space is unavailable.", "廚房牆面全做滿了櫥櫃沒有空間掛暖氣片。踢腳線風機盤管巧妙利用櫥櫃底部死角，由溫控開關感知熱水進入後自動開動風機強制吹風，散熱強勁小巧。", "Smith's Environmental Products Technical Manual; C&G Unit 207"),

        # 52. Towel rails summer heating
        ("7.1",
         "What is the operational purpose of installing a 'Dual-Fuel' towel rail in a domestic bathroom?",
         "在家庭浴室安裝「雙能源毛巾架 (Dual-Fuel Towel Rail)」的核心使用功能是什麼？",
         {"A": "To burn diesel and gas", "B": "It operates on the central heating wet circuit in winter, and uses an integrated electric heating element to dry towels in summer when the main central heating boiler is switched off", "C": "To boil bath water", "D": "To power the bathroom lighting"},
         {"A": "同時燃燒柴油和天然氣", "B": "冬季由中央供暖熱水迴路正常供暖；夏季全屋採暖停運時，利用內置的電加熱棒單獨通電烘乾毛巾，無需為烘一條毛巾而開啟全屋壁掛爐", "C": "用來加熱洗澡水", "D": "給浴室照明燈具發電"},
         "B", "Dual-fuel towel rails connect to heating pipework for winter efficiency, but contain an electric cartridge element with an isolation T-piece so damp towels can be dried year-round.", "雙能源實用性：英國夏天通常關閉供暖，但浴室毛巾依然潮濕容易發霉。雙能源毛巾架帶有電熱棒，夏天插電單獨加熱毛巾架，既方便又避免全屋大鍋爐無端浪費空燒。", "Domestic Heating Design Guide; C&G Unit 207"),

        # 53. UFH pipe EVOH barrier
        ("7.1",
         "Under DIN 4726, why must plastic pipework installed in Underfloor Heating (UFH) systems incorporate an EVOH (Ethylene Vinyl Alcohol) oxygen barrier layer?",
         "根據歐洲標準 DIN 4726，安裝在水地暖（UFH）中的塑料盤管（如 PE-RT 或 PEX）為什麼必須具備「EVOH 阻氧層 (Oxygen Barrier)」？",
         {"A": "To make the pipe purple", "B": "To stop atmospheric oxygen from diffusing through the permeable plastic pipe wall into the heating water, which would cause rapid corrosion of steel boilers and radiators", "C": "To keep the water carbonated", "D": "To increase water speed"},
         {"A": "將管材染成紫色以便於識別", "B": "阻斷大氣中的微觀氧分子透過塑料管壁微孔滲透溶入供暖水循環中，杜絕溶解氧對管網中鑄鐵水泵、鋼製鍋爐及暖氣片引發劇烈氧化腐蝕", "C": "保持水質呈碳酸充氣狀態", "D": "提升水流的流速"},
         "B", "Standard plastics are permeable to oxygen molecules. Oxygen ingress leads to intense electrolytic corrosion of metallic components. EVOH layers provide an impermeable gas barrier.", "塑料阻氧鐵律：一般塑料管在微觀上像篩子一樣透氧。若不用 EVOH 阻氧管，空氣中的氧氣會日夜滲入封閉水系統中，把壁掛爐熱交換器和鋼製暖氣片徹底鏽爛成黑泥。", "DIN 4726 Oxygen tightness; BS EN 1264; C&G Unit 207"),

        # 54. UFH loop length limits
        ("7.1",
         "What is the maximum recommended continuous circuit length for a single loop of 16mm Underfloor Heating (UFH) pipe, and why?",
         "在家庭水地暖施工中，一根 16mm 外徑的單路地暖盤管推薦的「最大連續敷設長度」通常是多少？為什麼不能無限盤長？",
         {"A": "Max 500 meters", "B": "Max 100 to 110 meters (to prevent excessive hydraulic friction resistance, excessive pressure drop, and uneven temperature loss)", "C": "Max 10 meters only", "D": "Unlimited length"},
         {"A": "最大可達 500 米", "B": "最大不超過 100 至 110 米（防止沿程水力摩擦阻力過大、水壓降超標以及盤管尾端水溫衰減過大導致冷熱不均）", "C": "最大僅能盤 10 米", "D": "長度沒有任何限制"},
         "B", "Exceeding ~100-110m for 16mm pipe creates excessive hydraulic resistance. Standard circulator pumps cannot push sufficient flow, resulting in cold floor zones and starved circuits.", "地暖水力極限：單迴路盤管超長（超過 100-110m），阻力損失呈幾何級暴增，地暖泵推不動，水流循環極其遲緩，熱水流到半截就涼了，造成地面一半熱一半冰。", "BS EN 1264-4; Polypipe / Uponor UFH Installation Manuals"),

        # 55. UFH pipe spacing
        ("7.1",
         "In modern screeded Underfloor Heating installations, what is the standard pipe center-to-center spacing typically used for standard residential living spaces?",
         "在現代澆築水泥砂漿層的水地暖安裝中，標準住宅客廳與起居生活空間通常採用的盤管中心間距（Pipe Centers）是多少？",
         {"A": "150mm to 200mm centers", "B": "500mm centers", "C": "25mm centers", "D": "1,000mm centers"},
         {"A": "150mm 至 200mm 間距", "B": "500mm 間距", "C": "25mm 間距", "D": "1,000mm 間距"},
         "A", "Standard residential spacing is typically 200mm (or 150mm in areas with higher heat loss or for low-temperature heat pump systems). Spacings closer than 100mm cause pipe kinking.", "地暖間距標準：常規保溫良好住宅多採 200mm 間距；熱泵低溫系統或高熱損大落地窗區域縮密至 150mm 或 100mm。過寬（>250mm）人踩上去會有冷熱條紋斑馬感。", "BS EN 1264-2; Domestic Heating Design Guide"),

        # 56. UFH screed curing
        ("7.1",
         "Why must Underfloor Heating (UFH) NEVER be turned on at full operating temperature immediately after new sand-and-cement screed is poured?",
         "在剛澆築完水泥砂漿地暖回填層（Screed）後，為什麼絕對嚴禁立刻將水地暖系統開啟至高溫滿負荷烘烤？",
         {"A": "Water will leak out of the screed", "B": "Rapid thermal expansion and violent moisture evaporation will crack, shatter, and permanently destroy the structural integrity of the screed and finished flooring", "C": "It will freeze the cement", "D": "Electricity will spark"},
         {"A": "地暖水會從砂漿中滲漏出來", "B": "急劇的熱脹冷縮與內部水分暴烈蒸發會造成回填砂漿層劇烈開裂、粉化碎裂，徹底摧毀地面結構強度並導致後期鋪設的瓷磚空鼓斷裂", "C": "會導致水泥發生冰凍", "D": "會在水泥內部引發電火花"},
         "B", "Screed must cure naturally for at least 21 days (sand/cement) before initial heating. Heating must then start at low temperature (e.g. 25°C) and rise slowly by 5°C per day to prevent cracking.", "水泥固化鐵律：常規砂漿需自然養護 21-28 天。首次烘地必須遵循階梯緩慢升溫程序：第一天 25°C，隨後每天微調提升 5°C，讓殘留水分溫和排出，防止地面爆裂。", "BS 8204-1 Screeds, bases and in situ floorings; BS EN 1264-4"),

        # 57. UFH perimeter insulation
        ("7.1",
         "What is the mechanical and thermal function of the flexible foam 'Perimeter Edge Strip' installed around all walls before pouring an underfloor heating screed?",
         "在澆築水地暖回填層之前，沿房間四周所有牆腳底部必須粘貼一圈高彈性發泡塑料「邊界膨脹保溫條 (Perimeter Edge Strip)」，其雙重功能是什麼？",
         {"A": "To decorate the room baseboards", "B": "To accommodate thermal expansion of the heated screed slab without cracking walls, and to stop lateral heat transmission loss into external wall structures", "C": "To keep mice out", "D": "To stick the carpet to the wall"},
         {"A": "用作踢腳線的裝飾邊條", "B": "吸收和緩衝加熱時水泥地面產生的微膨脹位移（防止膨脹頂裂四周牆體），並阻斷地面熱量向冰冷外牆發生橫向傳導散失（消除冷熱橋）", "C": "防止老鼠在牆腳打洞", "D": "將地毯邊緣粘死在牆上"},
         "B", "The edge strip acts as an expansion joint allowing the floor slab to expand smoothly when heated, while thermally isolating the screed from cold external walls to prevent thermal bridging.", "邊界保溫條的作用：熱脹冷縮吸震墊！熱砂漿受熱會向四周膨脹，若無緩衝棉會頂爆踢腳線與內隔牆；同時它切斷了地面高溫向外牆傳遞的熱橋，降低無謂熱損。", "BS EN 1264-4; Building Regulations Approved Document L1"),

        # 58. Regular Heat-Only Boiler
        ("7.1",
         "What three separate external water storage and expansion vessels are required for a traditional 'Heat-Only' (Regular / Conventional) open-vented central heating boiler system?",
         "在一套傳統的「常規純熱壁掛爐（Heat-Only / Regular Boiler）開式重力系統」中，必須在閣樓和熱水櫃中配套安裝哪三個獨立的容器/設備？",
         {"A": "Three gas bottles", "B": "A Cold Water Storage Cistern (CWSC), a Feed and Expansion (F&E) Cistern, and a vented Hot Water Cylinder", "C": "A heat pump, a radiator, and a fan", "D": "Only a pressurized red vessel"},
         {"A": "三個燃氣儲罐", "B": "高位冷水儲水箱 (CWSC)、供暖專用補水膨脹水箱 (F&E Cistern)、以及帶盤管的開式通氣熱水儲水罐 (Vented Cylinder)", "C": "熱泵、暖氣片與風機", "D": "僅需一個紅色膨脹罐"},
         "B", "A regular system requires a large CWSC in the loft for domestic hot water feed, a small F&E tank in the loft to replenish and vent heating water, and a copper cylinder in the airing cupboard.", "常規爐（老式開式系統）標配：閣樓上一大一小兩個水箱（大的是給生活熱水補水的 CWSC，小的是給供暖系統補水膨脹的 F&E 箱），外加熱水櫃裡的銅熱水水罐。", "C&G 6035 Unit 207; Textbook Ch 7"),

        # 59. System Boiler definition
        ("7.1",
         "What core central heating components are built directly inside a 'System Boiler' casing, eliminating the need for an F&E cistern in the roof space?",
         "相比常規壁掛爐，現代「系統壁掛爐 (System Boiler)」機殼內部自帶集成了哪些核心供暖水力組件，從而徹底省去了閣樓裡的供暖 F&E 補水水箱？",
         {"A": "An electric shower and pump", "B": "A circulating pump, an expansion vessel, and a 3-bar pressure relief valve (PRV)", "C": "A domestic hot water coil only", "D": "A water meter and water softener"},
         {"A": "即熱式電淋浴器與增壓泵", "B": "內置循環水泵、密閉式膨脹罐（Expansion Vessel）以及 3 bar 安全洩壓閥（PRV）", "C": "僅內置一組生活熱水換熱盤管", "D": "自帶自來水水表與軟水機"},
         "B", "A system boiler incorporates the circulator pump, expansion vessel, PRV, and pressure gauge inside its chassis, operating as a sealed circuit connected directly to an unvented or vented cylinder.", "系統爐特點：本質上是「自帶密封供暖套件」的鍋爐。水泵、膨脹罐、安全閥全塞在機器肚子裡，出廠就是封閉承壓系統，閣樓完全不用擺放骯髒生鏽的供暖補水箱。", "BS EN 12828; C&G Unit 207 Heating Systems"),

        # 60. Combi Boiler definition
        ("7.1",
         "What is the defining operational characteristic of a 'Combination (Combi) Boiler'?",
         "在英國住宅市場佔據主流的「組合式壁掛爐 (Combi Boiler)」，其最核心的運行特點是什麼？",
         {"A": "It heats only swimming pools", "B": "It provides space heating for radiators and instantaneous domestic hot water on demand directly from the cold mains, requiring neither hot water cylinders nor cold loft cisterns", "C": "It stores 500 litres of water internally", "D": "It runs entirely on wood chips"},
         {"A": "只能用於加熱室外游泳池", "B": "兼具全屋暖氣片供暖與「即開即熱生活熱水」功能；利用自來水市政主管水壓直接即時加熱熱水，既不需要熱水水罐，也不需要在閣樓擺放任何水箱", "C": "機身內部常備儲存 500 升熱水", "D": "完全依靠燃燒木屑顆粒發熱"},
         "B", "Combi boilers heat domestic hot water instantaneously via an internal secondary plate heat exchanger whenever a hot tap opens, saving space by dispensing with loft tanks and hot water cylinders.", "組合爐（Combi）最大優點就是「省空間」：沒有閣樓水箱，沒有熱水水櫃。打開水龍頭，自來水流過板式換熱器秒變熱水，關閉水龍頭立刻切換回暖氣片供暖。", "Domestic Heating Design Guide; C&G Unit 207"),

        # 61. Combi DHW pre-heat mode
        ("7.1",
         "What is the trade-off of enabling the 'DHW Pre-Heat' (Comfort Mode) feature on a domestic combi boiler?",
         "在現代家用組合式壁掛爐上開啟「生活熱水預熱功能 (DHW Pre-Heat / Comfort Mode)」時，其帶來的體驗提升與能耗代價是什麼？",
         {"A": "It cuts gas consumption by 90%", "B": "It delivers hot water to the taps more quickly by firing the burner periodically to keep the primary heat exchanger warm, but uses additional gas during standby", "C": "It permanently disables the space heating", "D": "It cools the hot water down to freezing"},
         {"A": "能夠削減 90% 的天然氣消耗量", "B": "壁掛爐在待機時會定期短暫點火，將內部板式換熱器始終維持在溫熱狀態，極大縮短開龍頭時出熱水的等待時間，但會略微增加待機保溫燃氣消耗", "C": "會永久切斷散熱器的採暖功能", "D": "會把流出的熱水降低到冰點"},
         "B", "Pre-heat eliminates the cold delay by keeping the heat exchanger warm. Eco mode disables this, saving gas by firing only when a hot tap actually opens.", "預熱功能權衡：開啟 Comfort 預熱，機器自己偷偷燒火保溫，一開龍頭立刻有熱水，體驗爽快但多耗燃氣；關閉（Eco 模式）則開龍頭後需等待數十秒，但更省燃氣費。", "Manufacturers Technical Manuals (Worcester Bosch / Vaillant); C&G Unit 207"),

        # 62. Combi cold water requirements
        ("7.1",
         "Why is a combination boiler NOT recommended for a large detached house with three simultaneously used power showers?",
         "為什麼對於帶有 3 間同時使用淋浴花灑的大戶型豪宅別墅，資深水暖工程師通常不推薦安裝單台家用組合式壁掛爐（Combi）？",
         {"A": "Combi boilers cannot heat houses with more than two rooms", "B": "A combi produces instantaneous DHW based on burner kW output, meaning simultaneous open hot taps share the fixed flow rate, causing drastic water starvation and temperature fluctuations", "C": "Combi boilers only work with bathtubs", "D": "Regulations prohibit combis in large houses"},
         {"A": "組合式壁掛爐無法給超過兩個房間的房屋供暖", "B": "組合爐即熱熱水出水流量受制於即時燃燒器功率（如 30kW 約出水 12 L/min），若多個花灑同時打開，有限的流量被嚴重瓜分，會導致水流極小且忽冷忽熱", "C": "組合爐只能搭配浴缸放水", "D": "英國建築法規明文禁止豪宅使用組合爐"},
         "B", "Combi DHW flow rate is strictly limited by boiler kW capacity (e.g., 30kW delivers ~12 L/min at 35°C rise). Multiple outlets open at once drop pressure and scald/freeze users. Cylinders are preferred.", "Combi 的硬傷是「多點用水互搶」：一台 30kW 爐子一分鐘最多出 12 升熱水，一個人洗澡很舒服；如果樓下有人洗碗、另一人又開花灑，水流瞬間分薄變涓涓細流，甚至被凍得尖叫。", "Domestic Heating Design Guide; C&G Unit 207"),

        # 63. Low water pressure switch
        ("7.1",
         "What is the protective function of the 'Low Water Pressure Switch' fitted inside sealed system boilers?",
         "安裝在密封系統壁掛爐內部的「低水壓安全保護開關 (Low Water Pressure Switch)」的保護功能是什麼？",
         {"A": "To vent flue gases", "B": "To lock out the boiler burner and pump if system pressure drops below a safe threshold (typically ~0.5 to 0.7 bar), preventing dry-firing and catastrophic heat exchanger melting", "C": "To boost water pressure to 10 bar", "D": "To inject chemical inhibitor automatically"},
         {"A": "排出煙道廢氣", "B": "當供暖管網缺水漏水導致水壓跌破安全極限（通常為 0.5 至 0.7 bar）時，主動切斷燃燒器點火並停轉水泵，杜絕乾燒（Dry-firing）燒毀昂貴的主換熱器", "C": "自動將管網水壓加壓到 10 bar", "D": "全自動向管道注入化學阻垢劑"},
         "B", "Running a boiler without water causes localized boiling and melts aluminum/stainless heat exchangers within minutes. The pressure sensor cuts burner electrical interlock to protect the appliance.", "乾燒保護安全底線：若水暖管漏水漏空了，沒有水吸收火焰熱量，幾分鐘內換熱器就會燒穿報廢甚至引發火災。低壓開關感知到水壓不足立刻亮紅燈報警鎖死（Lockout）。", "BS EN 12828; Gas Safe Technical Bulletins"),

        # 64. Overheat thermostat
        ("7.1",
         "What is the operational function of the 'Overheat Thermostat' (high-limit thermal cut-out) fitted directly to a boiler primary flow pipe?",
         "緊貼安裝在壁掛爐主出水管上的「過熱超溫保護溫控器 (Overheat Thermostat / High Limit Cut-out)」具有何種應急保護機制？",
         {"A": "It turns on the heating in winter", "B": "It is an independent fail-safe safety sensor that permanently trips and locks out the boiler (requiring manual reset) if water temperature exceeds approximately 95°C to 105°C", "C": "It measures gas consumption", "D": "It cools the boiler with cold water"},
         {"A": "在冬天自動啟動供暖", "B": "這是一個獨立的故障安全極限傳感器，若水溫異常飆升突破 95°C 至 105°C 的危險極限，它會強制切斷燃氣閥供電鎖定停機，且必須由人工手動復位（Manual Reset）", "C": "計量燃氣消耗立方數", "D": "自動注入冷水為鍋爐降溫"},
         "B", "If the control thermostat fails closed, water would boil explosively into steam. The high-limit overheat stat acts as an ultimate fail-safe, cutting burner power before steam generates.", "防汽化終極防線：主控板溫控失靈持續燒火會把水燒成高壓蒸汽炸裂管路！過熱溫控器是機械雙金屬片或專用熱敏斷路器，一旦破百即刻鎖死，必須排查故障後手動按下復位鈕。", "BS EN 12828; Gas Safety (Installation and Use) Regulations 1998"),

        # 65. Concentric balanced flue
        ("7.1",
         "What is the structural configuration and safety principle of a 'Room-Sealed Concentric Balanced Flue' used on modern domestic gas boilers?",
         "現代家用燃氣壁掛爐廣泛配備的「房間密封同軸平衡式煙道 (Room-Sealed Concentric Balanced Flue)」具有何種雙層結構與安全原理？",
         {"A": "A single copper pipe routed up an open chimney", "B": "A pipe-within-a-pipe system where the internal duct discharges toxic flue gases outside while the outer concentric annulus simultaneously draws fresh combustion air from outside into the sealed boiler casing", "C": "An open window with a fan", "D": "A flexible hose exhausting into the roof attic"},
         {"A": "沿著開式煙囪敷設的單根紫銅排煙管", "B": "「管中管」同軸雙層結構：內層管道向室外強排高溫燃燒廢氣，外層夾套通道同時從室外吸入新鮮助燃空氣，燃燒全程與室內空氣徹底物理隔離密封", "C": "一扇敞開的窗戶外加排風扇", "D": "通往閣樓夾層內部排氣的軟管"},
         "B", "Room-sealed balanced flues draw all combustion air from outdoors and expel flue exhaust outdoors. The living space is 100% sealed from burner combustion, eliminating carbon monoxide poisoning risks.", "同軸平衡煙道安全革命：雙層管套在一起，外吸室外氧氣、內排燃燒廢氣，完全不消耗屋內的一絲氧氣，就算煙道有毒廢氣泄漏也不可能進入室內，從物理上根絕了一氧化碳中毒！", "BS 5440-1 Flueing and ventilation; C&G Unit 207"),

        # 66. Flue terminal clearances BS 5440-1
        ("7.1",
         "Under BS 5440-1, what is the minimum required clearance distance between a horizontal fanned-draught boiler flue terminal and an openable window, door, or air brick?",
         "根據英國排煙標準 BS 5440-1，強制機械風壓壁掛爐水平煙道外牆終端排氣口，距離可開啟的窗戶、通風門或通風磚的最小安全間距是多少？",
         {"A": "Minimum 300mm", "B": "Minimum 5,000mm", "C": "Zero mm (directly inside the window frame)", "D": "Minimum 50mm"},
         {"A": "至少 300mm", "B": "至少 5,000mm", "C": "0 mm（直接對準窗戶縫隙排氣）", "D": "至少 50mm"},
         "A", "BS 5440-1 Table C.1 dictates a minimum 300mm clearance from openable windows/doors for fan-flued boilers up to 70 kW, preventing combustion gases from re-entering the building.", "煙道間距金科玉律：水平風機排煙口距離可開啟窗戶邊緣、門框或通風磚不得少於 300mm；若距離低於此數，有毒酸性煙氣會從窗縫倒灌室內，造成人員窒息與鉛中毒危險。", "BS 5440-1:2008 Installation of flues and ventilation; C&G Unit 207"),

        # 67. Condensing flue fall
        ("7.1",
         "Why must horizontal concentric flue runs on modern condensing boilers always be installed with a continuous upward fall away from the boiler (typically a minimum gradient of 3 degrees or 52mm per meter)?",
         "在安裝現代高效冷凝壁掛爐的水平同軸煙道時，為什麼煙道必須嚴格保持向外「向上傾斜」（即由外牆終端向鍋爐方向保持至少 3 度或每米 52mm 的倒坡度）？",
         {"A": "To let rainwater run down the outside wall", "B": "To ensure acidic condensate forming within the flue continuously flows safely backwards into the boiler's internal condensate trap and drain rather than dripping and damaging external walls", "C": "To make smoke rise faster", "D": "To allow birds to build nests inside"},
         {"A": "讓室外雨水順著外牆往下流", "B": "確保在煙道內冷凝析出的酸性冷凝水能順著倒坡一路倒流回壁掛爐內部的冷凝水收集收集器排出，防止酸水從外牆終端下滴腐蝕外牆磚面或滴傷行人", "C": "讓煙霧因浮力排得更快", "D": "方便小鳥在煙道口築巢"},
         "B", "Condensing flue gases extract so much heat that water vapor condenses inside the plastic flue pipe. Flues must pitch back towards the boiler (min 52mm/m) so acidic runoff drains safely inside.", "冷凝煙道倒坡鐵律：冷凝爐排煙溫度低（僅約 55°C），煙氣中的水蒸氣在煙管內壁大量凝結成酸性水滴。若向外溜坡，酸水會滴滴答答腐蝕外牆磚和人行道；倒流進鍋爐由專門排水管排出才是正道。", "BS 5440-1; Boiler Manufacturers Installation Instructions"),

        # 68. Condensate disposal options
        ("7.1",
         "Under Approved Document H and BS 6798, what is the preferred method for disposing of acidic boiler condensate wastewater?",
         "根據英國建築法規 Approved Document H 及 BS 6798，處理壁掛爐排出的酸性冷凝廢水（pH 3.5 - 5.0）的最優先推薦途徑是什麼？",
         {"A": "Draining directly into clean rainwater rainwater butt for drinking", "B": "Connecting internally to the domestic foul soil stack or waste pipework above an effective water seal trap", "C": "Pumping it into the gas meter", "D": "Spraying it over the garden lawn"},
         {"A": "直接排入用於飲用集水的潔淨雨水桶", "B": "優先在室內直接接入家庭污水管道（Soil Stack）或洗手盆/洗滌槽的排水排污支管（且必須位於有效水封存水彎的上游）", "C": "抽打到燃氣表內部", "D": "噴灑在花園草坪上澆灌花草"},
         "B", "Internal termination into foul drainage is preferred because internal pipes never freeze. External connections must only be used if internal routes are impossible, requiring larger insulated pipes.", "冷凝水排放優先序：室內污水管（Soil Pipe）是最優解！室內溫度常年高於冰點，永遠不會凍死。接入排水管時必須接在存水彎上方，防止下水道惡臭沼氣沿冷凝管反串回鍋爐內部。", "BS 6798:2014 Specification for installation of gas-fired boilers; Approved Doc H"),

        # 69. External condensate freezing
        ("7.1",
         "If an external boiler condensate pipe MUST be installed outside due to architectural constraints, what two critical precautions are mandatory under BS 6798 to prevent winter freezing?",
         "因建築格局限制壁掛爐冷凝水排水管「必須穿牆敷設到室外」時，根據 BS 6798 標準，必須採取哪兩項強制防護工藝以防止嚴冬結冰凍堵？",
         {"A": "Paint the pipe red and use rubber hose", "B": "Increase pipe diameter to a minimum of 32mm outside and insulate with external-grade, UV-resistant Class O waterproof insulation", "C": "Reduce pipe to 10mm and run it for 50 meters", "D": "Plug the end of the pipe with a cork"},
         {"A": "將管子刷成紅色並使用普通橡膠軟管", "B": "出牆處立刻將管徑放大擴徑至至少 32mm 外徑，且全程包裹室外專用抗紫外線、閉孔防水的 Class O 級厚壁保溫保溫套管（或加裝電伴熱帶）", "C": "將管徑縮小到 10mm 且長距離拉線 50 米", "D": "拿軟木塞將管口直接封死堵住"},
         "B", "Small external pipes freeze solid in sub-zero temperatures, causing boiler lockout. BS 6798 mandates upsizing to at least 32mm ID and insulating thoroughly to prevent ice blockages.", "室外冷凝管凍結慘劇：每年大雪嚴冬成千上萬戶冷凝爐報警停機，全因室外細水管結冰凍成實心冰棍！出牆必須立刻擴大到 32mm 粗管，並套上防水抗曬橡塑保溫棉，坡度儘可能陡峭直下。", "BS 6798:2014 Section 8; HHIC Condensate Discharge Guidelines"),

        # 70. F&E Cistern location and capacity
        ("7.1",
         "In an open-vented central heating system, what is the minimum required water capacity of the Feed and Expansion (F&E) cistern under BS 5449?",
         "在傳統開式重力補水供暖系統中，根據 BS 5449 標準，閣樓中的補水膨脹水箱（F&E Cistern）推薦的最小水容量通常是多少？",
         {"A": "At least 18 to 20 litres actual working capacity (sufficient to accommodate the thermal expansion of total system water volume)", "B": "1 litre", "C": "5,000 litres", "D": "100,000 litres"},
         {"A": "實際有效工作容積至少為 18 至 20 升（足以容納全屋採暖管網全部存水受熱膨脹後的增量體積）", "B": "1 升", "C": "5,000 升", "D": "100,000 升"},
         "A", "Water expands approx 4% when heated from 10°C to 80°C. A 100-litre system expands by 4 litres. An 18-20L F&E tank accommodates water expansion without spilling down the overflow.", "膨脹箱容積原理：水從冷水燒到 80°C 體積會自然膨脹約 4%。若全屋暖氣管存水 200 升，受熱後就會多出 8 升水。小於 18L 的水箱水面會漲滿溢流管白白漏水，必須留足膨脹安全裕量。", "BS 5449 Forced circulation hot water central heating systems; C&G Unit 207"),

        # 71. Pumping over causes
        ("7.1",
         "What is the defect termed 'Pumping Over' in an open-vented central heating system, and what is its most common physical cause?",
         "在開式供暖系統中，俗稱的「水泵反向頂溢/泵越 (Pumping Over)」是指何種故障現象？其最常見的管路力學原因是什麼？",
         {"A": "Water pumping out of the kitchen tap", "B": "Heating water is forced out of the top of the open vent pipe and continuously discharges into the F&E cistern, often caused by a blocked cold feed pipe or an incorrectly sited circulator pump", "C": "Boiler producing electricity", "D": "Radiators filling with kerosene"},
         {"A": "自來水從廚房水龍頭噴射出來", "B": "循環水泵將高溫熱水直接從通氣膨脹管（Open Vent）頂部彎頭壓出、持續傾瀉噴入閣樓 F&E 水箱中；常因冷補水管結垢堵死或水泵安裝在通氣管與補水管中間引發負壓失衡造成", "C": "壁掛爐自發對外發電", "D": "暖氣片內部灌滿了煤油"},
         "B", "Pumping over pumps aerated, scalding water into the plastic loft cistern, causing tank softening and driving continuous oxygen corrosion throughout the system.", "泵越的危害極大：熱水像噴泉一樣從通氣管噴進水箱，不僅可能把塑料水箱燙軟塌陷引發天花板漏水，還會把水箱裡的氧氣大量捲入管網中，導致全屋暖氣片迅速爛穿生鏽。", "C&G 6035 Unit 207; Plumbing & Heating Engineer Manual"),

        # 72. Neutral point definition
        ("7.1",
         "In an open-vented wet central heating system, what is the hydraulic significance of the 'Neutral Point'?",
         "在開式水力供暖管路佈局中，「水力中性點 (Neutral Point)」具有何種關鍵的流體力學意義？",
         {"A": "The point where water turns into gas", "B": "The junction where the cold feed pipe connects to the circuit; at this point, the system dynamic pressure remains completely unchanged whether the circulator pump is running or stopped", "C": "The electrical neutral wire terminal", "D": "The center of the boiler burner"},
         {"A": "水分子沸騰汽化的臨界點", "B": "冷補水管接入主循環迴路的匯合節點；在此點處，無論水泵啟動高速運轉還是徹底停機，該點處的動態水壓永遠等於高位水箱靜壓，保持絕對恆定不變", "C": "電路接線排上的零線接線柱", "D": "壁掛爐燃燒器的幾何中心"},
         "B", "The neutral point is the open connection to atmospheric pressure (via the F&E tank). Pressure at this point is strictly governed by static head and cannot be altered by pump head.", "水力中性點定律：冷補水管與大氣連通，其接管點壓力永遠死死被閣樓水箱的靜水頭錨定。水泵只能以中性點為基準，在泵後產生正壓（推力），在泵前產生負壓（吸力）。", "C&G Unit 207 Open Vented Hydraulics; BS 5449"),

        # 73. Pump position relative to cold feed
        ("7.1",
         "To maintain positive hydraulic pressure throughout all radiators and prevent air being drawn down the open vent pipe, where should the circulator pump be positioned relative to the cold feed and open vent pipes?",
         "為了確保全屋所有散熱器管網全程處於正壓狀態、並杜絕開式通氣管吸入空氣（Pumping down），循環水泵應當安裝在冷補水管與通氣管的哪個相對位置？",
         {"A": "Between the open vent and the cold feed", "B": "Immediately downstream of the close-coupled open vent and cold feed connections, pumping away from both towards the system", "C": "On the return pipe pumping towards the open vent", "D": "Inside the F&E tank"},
         {"A": "安裝在通氣管與冷補水管兩者正中間", "B": "緊隨緊湊並接的通氣管與冷補水管的下游位置，方向朝向遠離二者的全屋採暖管網方向泵出熱水（Pumping Away）", "C": "安裝在回水管上朝向通氣管方向打水", "D": "直接浸泡在閣樓 F&E 水箱內部"},
         "B", "Pumping away from the cold feed ensures the entire downstream system operates under positive pressure relative to atmosphere, preventing air-pulling and aeration.", "黃金管路佈局（Close-coupled）：通氣管在先、冷補水在後（兩者間距 <150mm），水泵緊跟在冷補水後方朝外推水。如此一來全系統都是正壓，通氣管永遠不會吸氣氣塞。", "BS 5449 Section 3; Domestic Heating Design Guide"),

        # 74. Pumping down phenomenon
        ("7.1",
         "What catastrophic issue occurs if a heating pump is installed such that it creates negative pressure (suction) at the base of an open vent pipe ('Pumping Down')?",
         "若供暖水泵安裝錯誤，在通氣管底部產生了劇烈的流體負壓抽吸效應（即「吸空 / Pumping Down」現象），會引發何種災難性後果？",
         {"A": "Air is drawn continuously down the open vent into the heating system, causing massive air locks, pump cavitation, and ferocious internal oxidation corrosion", "B": "The radiators turn to ice", "C": "The gas bill drops to zero", "D": "Boiler produces oxygen gas"},
         {"A": "大量空氣被持續從敞開的通氣管口強行抽吸進供暖管網中，造成全屋頻繁嚴重氣塞、水泵氣蝕空轉損壞、以及金屬管壁暴烈氧化腐蝕爛穿", "B": "暖氣片瞬間凝結成冰塊", "C": "燃氣賬單徹底清零", "D": "壁掛爐自發電解產生純氧氣"},
         "A", "Suction pulls atmospheric air down the open vent, dissolving vast quantities of oxygen into the water. This rapidly corrodes steel radiators into black magnetite sludge and destroys the pump.", "吸空氣（Pumping Down）是開式系統的隱形殺手：負壓把屋頂空氣像抽水煙一樣吸入管道，水泵打出全是泡沫牛奶水，水泵葉輪被氣蝕打爛，管道幾個月就鏽爛漏水。", "BS 5449; C&G 6035 Unit 207"),

        # 75. Sealed system pressure test
        ("7.1",
         "When pressure testing a newly installed sealed central heating pipework system before connecting sensitive boiler components or after isolating the 3-bar safety valve, what test pressure is recommended under BS EN 12828 / BS 5449?",
         "在對新安裝的密封承壓供暖管網進行水壓強度打壓試驗時（已隔離保護敏感鍋爐配件與 3 bar 洩壓閥），根據規範通常推薦施加多大測試水壓並保壓檢驗？",
         {"A": "0.1 bar for 10 seconds", "B": "1.5 times the maximum system working pressure (typically 1.5 to 2.0 bar, or up to 3 bar proof test)", "C": "100 bar", "D": "No testing is permitted"},
         {"A": "0.1 bar 測試 10 秒鐘", "B": "最大系統設計工作水壓的 1.5 倍（通常冷態打壓至 1.5 至 2.0 bar，或專項管網承壓耐壓試驗 3 bar）", "C": "100 bar", "D": "法規禁止進行任何打壓試驗"},
         "B", "Sealed circuits normally operate between 1.0 and 1.5 bar cold (rising to ~2.0 bar hot). Testing at 1.5 times working pressure verifies structural joint tightness without exceeding component ratings.", "密封管網打壓驗收：常規冷態注水至 1.0 - 1.2 bar；打壓檢漏通常升壓至 1.5 - 2.0 bar 保持 1 小時指針不降為合格。切記不能盲目猛打超 3 bar，否則會頂開壁掛爐安全洩壓閥狂噴水。", "BS EN 12828 Heating systems in buildings; C&G Unit 207"),

        # 76. Benchmark checklist
        ("7.1",
         "What is the statutory and warranty importance of the 'Benchmark Commissioning Checklist' found at the back of every boiler installation manual in the UK?",
         "在英國每台燃氣壁掛爐安裝手冊末頁附帶的「Benchmark 試運行調試簽字清單」，具有何種法定地位與廠家質保重要性？",
         {"A": "It is an optional advertisement flyer", "B": "It is a mandatory compliance document under Building Regulations Part L; failure to complete and sign it invalidates the manufacturer warranty and breaches Building Regulations", "C": "It is a receipt for scrap metal", "D": "It is for painting instructions only"},
         {"A": "這是一份無關緊要的廠家商業宣傳彩頁", "B": "這是英國建築法規 Part L 認證法定的強制竣工驗收文件；安裝技師若未完整填寫簽字並登記防腐劑添加記錄，鍋爐原廠超長質保將徹底失效，且通不過建築驗收", "C": "這是一張廢舊金屬收購憑證", "D": "這是一份純油漆粉刷施工說明"},
         "B", "Benchmark is the national code of practice. Completing it confirms the system was flushed, cleansed, inhibited, balanced, and combusted to standards. Without it, warranties are void.", "Benchmark 簽字清單是英國供暖「身份證」：上面必須填寫煙氣分析儀 CO/CO2 比值、系統化學清洗與加註阻垢劑品牌日期、供回水溫差。沒這份清單，大廠 10 年質保直接變成廢紙。", "Benchmark Scheme Code of Practice; Building Regulations Approved Document L1"),

        # 77. Programmable room thermostats
        ("7.2",
         "What is the operational function of a '7-Day Programmable Room Thermostat' compared to a simple mechanical dial thermostat?",
         "相比老式單一旋鈕機械溫控器，現代「7 天可編程室內溫控器 (7-Day Programmable Thermostat)」提供了何種核心智能節能控溫功能？",
         {"A": "It only measures humidity", "B": "It allows independent target temperatures to be scheduled across multiple time bands for every individual day of the week (e.g. weekday workday vs weekend schedules)", "C": "It cooks meals automatically", "D": "It requires manual winding every morning"},
         {"A": "它只能單純測量室內空氣濕度", "B": "允許用戶針對一週內星期一至星期日的每一天，按不同時段自由設定多個獨立目標溫度（例如工作日白天低溫節能、早晚及週末高溫舒適）", "C": "能夠全自動烹飪早晚三餐", "D": "每天早晨必須人工手動擰發條上弦"},
         "B", "Programmable thermostats combine time and temperature control, preventing empty homes being heated during working hours while maintaining comfortable warmth when occupants are present.", "7 天可編程是節能利器：工作日白天家裡沒人自動降到 15°C 保溫；下午下班前提前半小時自動升到 21°C；週末全天保持舒適，比全天恆溫死燒節省 20% 以上燃氣。", "Building Regulations Approved Document L1; Energy Saving Trust"),

        # 78. Smart thermostats features
        ("7.2",
         "What advanced energy-saving feature is provided by modern smart thermostats (such as Nest, Hive, or Tado) using smartphone GPS technology?",
         "現代互聯網智能溫控器（如 Nest、Hive、Tado）利用用戶手機的 GPS 定位技術，實現了何種前沿的「地理圍欄 (Geo-fencing)」節能功能？",
         {"A": "It tracks the user's phone calls", "B": "It senses when all occupants have physically left the property and automatically sets the heating to eco/away mode, ramping back up only as someone travels home", "C": "It charges money every time a door opens", "D": "It locks the front door"},
         {"A": "監聽記錄用戶的日常通話內容", "B": "全自動感應所有家庭成員是否已攜帶手機離家外出，人走自動將供暖切入節能離家模式；感應到家庭成員正在返家途中時提前點火預熱", "C": "每次開門向用戶扣費", "D": "自動將大門反鎖鎖死"},
         "B", "Geofencing uses mobile device location to automatically switch heating off when the home is unoccupied, eliminating wasted energy and ensuring the property is warm upon return.", "地理圍欄節能黑科技：出門上班人走空了，溫控器通過手機定位自動判定無人，立刻調低供暖；下班在回家地鐵上，溫控器提前把家裡燒暖，完全零人工干預。", "Domestic Heating Design Guide; Smart Thermostat Standards"),

        # 79. Optimum start algorithm
        ("7.2",
         "In modern heating controls, how does an 'Optimum Start' (Adaptive Start) algorithm operate?",
         "在現代智能供暖控制器中，「自適應最佳啟動算法 (Optimum Start Algorithm)」的工作邏輯是什麼？",
         {"A": "It starts the boiler at midnight every night", "B": "It monitors indoor and outdoor temperature trends and automatically calculates the exact time the boiler must fire so the room reaches target temperature precisely at the requested hour", "C": "It runs the circulator pump backwards", "D": "It ignites the boiler with a match"},
         {"A": "每天午夜 0 點準時啟動壁掛爐點火", "B": "持續監測室內外溫差與房間升溫速率曲線，動態精準計算壁掛爐必須提前多少分鐘點火，以確保房間在設定的時間點「剛好分秒不差達到目標舒適溫度」", "C": "驅動循環水泵反方向倒轉", "D": "使用火柴手動引燃壁掛爐"},
         "B", "Instead of a fixed start time (e.g. 6:30 AM), Optimum Start learns thermal response. On mild mornings it fires late (6:45 AM); on freezing mornings it fires early (6:00 AM) to reach 21°C by 7:00 AM.", "最佳啟動自學習算法：老式定時器不論嚴冬暖冬死板 6:30 開機。自適應溫控器會自己計算：外面零下 5 度就提前到 6:00 點火，外面 10 度就推遲到 6:45 點火，保證 7:00 準確達到 21°C，省氣極致。", "BS EN 12098 Controls for heating systems; Approved Doc L1"),

        # 80. Frost and pipe thermostats wiring
        ("7.2",
         "How should an external Frost Thermostat and an associated Pipe Thermostat be wired in circuit to protect a boiler in an unheated garage from freezing?",
         "當燃氣壁掛爐安裝在無暖氣的外車庫中時，為了可靠實現低溫防凍保護，外裝的「環境防凍溫控器 (Frost Stat)」與「管道溫控器 (Pipe Stat)」在電氣上應如何串聯/並聯接線？",
         {"A": "Wired in parallel across mains voltage", "B": "The frost stat is wired in series with the pipe stat (frost stat makes on temperature drop <5°C, pipe stat satisfies and breaks when heating water reaches ~25°C to prevent overheating)", "C": "Wired directly into the kitchen lighting circuit", "D": "No wiring, operated by wind"},
         {"A": "直接與 230V 市電完全並聯", "B": "防凍溫控器與管道溫控器「互相串聯」控制壁掛爐：環境溫控在氣溫低於 5°C 時閉合點火；管道溫控在水管燒到約 25°C 時及時斷開熄火，防止把車庫燒太熱", "C": "直接串接在廚房吊燈照明電路上", "D": "完全不需要任何接線，靠自然風力感應"},
         "B", "Frost stat senses cold air (<5°C) and calls for heat to stop freezing. The series-wired pipe stat cuts the boiler when circulating water hits ~25-30°C, preventing the boiler running continuously.", "車庫防凍經典雙溫控串聯：環境防凍溫控（<5°C 閉合啟動壁掛爐打水）；若無管道溫控，壁掛爐會一直燒到 80°C 浪費燃氣！串聯管道溫控（燒到 25°C 斷開），既防止水管結冰又極度省氣。", "Honeywell Domestic Heating Wiring Guide; C&G Unit 207"),

        # 81. Y-Plan wiring colours
        ("7.2",
         "In standard Honeywell Y-Plan wiring, what is the function of the ORANGE wire emerging from the 3-port mid-position valve head?",
         "在英國標準 Honeywell Y-Plan 供暖電路中，從 3 通中位電動閥執行器頭部引出的「橙色線 (Orange Wire)」的電氣控制功能是什麼？",
         {"A": "Earth grounding connection", "B": "Switched live output to fire the boiler burner and central heating circulator pump", "C": "Permanent 230V mains live supply", "D": "Neutral wire"},
         {"A": "底盤保護接地線", "B": "微動開關輸出的「受控火線 (Switched Live)」，用於向燃氣壁掛爐點火端子與循環水泵輸出 230V 啟動運行供電", "C": "230V 市電常火線", "D": "工作零線"},
         "B", "The orange wire is energized by the valve's internal microswitch once the valve completes travel to heating or mid-position, feeding 230V switched live directly to boiler terminal SL and pump.", "英國水暖電工必背口訣：閥門橙色線是「向壁掛爐報喜的點火線」！無論是二通閥還是三通閥，內部微動開關閉合後，橙色線帶上 230V 電壓，壁掛爐和水泵立刻點火運轉。", "Honeywell Wiring Specification Y-Plan; C&G Unit 207/208"),

        # 82. S-Plan wiring colours
        ("7.2",
         "In standard S-Plan wiring, what are the functions of the GREY and ORANGE auxiliary switch wires on a 5-wire 2-port zone valve?",
         "在標準 5 芯線 2 通電動分區閥（S-Plan）中，「灰色線 (Grey)」與「橙色線 (Orange)」內部連接的微動開關具有何種控制邏輯？",
         {"A": "Grey is neutral and Orange is earth", "B": "Grey is supplied with a permanent live (230V); when the valve motor drives the valve fully open, an internal microswitch connects Grey to Orange, sending switched live to the boiler and pump", "C": "They are for speaker audio", "D": "They measure water hardness"},
         {"A": "灰色是工作零線，橙色是保護接地線", "B": "灰色線接入 230V 常火線；當閥門電機將水路徹底推至全開位置時，內部微動開關閉合將灰色線與橙色線接通，由橙色線向壁掛爐和水泵輸出點火啟動信號", "C": "用來連接音響音頻信號", "D": "用以實時測量水質硬度"},
         "B", "Grey is the dry contact supply feed (normally linked to permanent live). When the motor opens the brass ball/paddle, the mechanical cam trips the switch, electrifying Orange to fire the heat source.", "S-Plan 閥門五芯線解密：棕色（電機進電火線）、藍色（零線）、綠黃（地線）；灰色與橙色是內置無源微動開關的兩端。只有水路真正開到位了，灰橙才接通點火，絕不乾燒！", "Honeywell / Drayton 2-Port Motorized Valve Installation Guide"),

        # 83. Motorized valve actuator replacement
        ("7.2",
         "What is the massive servicing advantage of modern 'Demountable / Interchangeable' motorized zone valve actuators (e.g. Honeywell V4043 / Drayton Actuator)?",
         "現代主流供暖電動分區閥（如 Honeywell 或 Drayton 二通閥/三通閥）採用「分體可拆卸執行器電機頭 (Demountable Head)」設計，帶來了何種革命性的維修優勢？",
         {"A": "The head can be made of glass", "B": "The electrical motor head can be unclipped and replaced in minutes without draining down the water in the central heating pipework system", "C": "It eliminates the need for electricity", "D": "It doubles the water temperature"},
         {"A": "電機頭可以改用透明玻璃製造", "B": "在電氣執行器電機燒毀損壞時，維修水暖工只需按壓卡扣拆下更換電氣頭，全程「完全不需要將全屋供暖管網內部的存水排空洩壓」", "C": "徹底擺脫對任何電力的依賴", "D": "使水溫翻倍升高"},
         "B", "Demountable actuators separate the dry electrical motor from the wet brass hydraulic valve body. Replacing a burnt-out motor head takes two screws or a push-button without draining down water.", "水暖工的福音：以前換個閥門要排空全屋幾百升黑水，加藥排氣折騰半天。現代電動閥是「水電分離」結構，卡扣一按拿下壞電機換個新的，5 分鐘搞定且一滴水都不會漏！", "Honeywell / Horstmann Valve Service Manuals; C&G Unit 207"),

        # 84. Thermoelectric UFH actuators
        ("7.2",
         "What type of actuators are universally installed on the return manifold ports of Underfloor Heating (UFH) circuits, and what is their normal resting position?",
         "安裝在水地暖（UFH）回水分水器各支路閥口上的微型執行器，普遍採用何種驅動原理？其斷電停機時的默認機械狀態是什麼？",
         {"A": "Pneumatic pistons that are normally open", "B": "Electrothermic wax/paraffin element actuators that are Normally Closed (NC) when de-energized", "C": "Nuclear drives that stay spinning", "D": "Manual brass handwheels only"},
         {"A": "常開式氣動活塞執行器", "B": "電熱蠟包熱膨脹驅動執行器 (Electrothermal Wax Actuator)，在斷電無信號時處於「常閉狀態 (Normally Closed - NC)」", "C": "持續旋轉的微型核動力驅動器", "D": "純手動旋轉銅手輪"},
         "B", "UFH manifolds use electrothermal actuators containing paraffin wax that expands when heated electrically. Being Normally Closed (NC), circuits safely shut off when room stats are satisfied.", "地暖電熱執行器原理：內部裝有特殊石蠟。溫控器要熱給電，發熱電阻加熱蠟包，石蠟膨脹慢慢頂開閥桿通水（無任何機械齒輪噪聲）；斷電冷卻後彈簧自動把閥門頂回常閉關閉。", "BS EN 1264-4; Uponor / Heatmiser UFH Controls Guide"),

        # 85. Automatic air vent maintenance
        ("7.2",
         "What is the operational maintenance procedure for the small knurled plastic cap fitted on top of an Automatic Air Vent (AAV) in a central heating system?",
         "安裝在壁掛爐頂部或供暖管路最高處的「全自動自動排氣閥 (Automatic Air Vent - AAV)」頂端的小塑料滾花排氣帽，在正常運行時應當處於何種狀態？",
         {"A": "Glued shut permanently with silicone", "B": "Loosened by half a turn to allow trapped air to vent automatically, but closed tightly if weeping water or during long-term unattended operation", "C": "Removed and thrown away", "D": "Filled with grease"},
         {"A": "用玻璃膠永久死死封死", "B": "逆時針擰鬆半圈至一圈，使內部浮子排氣孔暢通以自動排出氣體；但若發現有微滲水或長期無人照看時可手動擰緊封閉防漏", "C": "拆下來直接扔進垃圾桶", "D": "內部注滿高溫潤滑脂"},
         "B", "The knurled cap covers the vent orifice. Loosening it allows the internal float mechanism to release escaping air bubbles continuously. Tightening it seals the vent against potential dirt leaks.", "自動排氣閥小帽子玄機：新系統注水排氣時必須擰鬆一圈，裡面浮子下沉氣體噗噗排出；平時運行微鬆；若閥芯日久被黑泥卡住滲水，擰死小帽子可作應急截止閥防止泡水地板。", "C&G Unit 207 Heating Commissioning; Flamco Technical Documentation"),

        # 86. Plate heat exchanger descaling
        ("7.2",
         "When a domestic combi boiler fails to deliver adequately hot domestic water and cycles on and off rapidly in DHW mode, what maintenance action often restores heat transfer on the secondary plate heat exchanger?",
         "當家用組合壁掛爐生活熱水水溫上不去、且在放熱水時壁掛爐頻繁頻繁開關點火（短週期短循環）時，對二次不銹鋼板式換熱器實施何種維護保養往往能排除故障？",
         {"A": "Paint the boiler white", "B": "Remove the plate heat exchanger and chemically descale/flush it using an acidic descaling solution (or replace the fouled plate pack)", "C": "Cut the gas pipe", "D": "Fill the system with sand"},
         {"A": "把鍋爐外殼刷上白漆", "B": "拆卸下不銹鋼板式換熱器，使用專用酸性除垢清洗劑進行循環浸泡酸洗除垢（或直接更換嚴重結垢淤堵的新板換）", "C": "直接拿鋼鋸切斷燃氣管道", "D": "向採暖系統內部灌入細沙"},
         "B", "Secondary plate exchangers foul with limescale on the DHW side and magnetite sludge on the heating side. Restricted heat transfer causes primary water to overheat, triggering burner cycling.", "板換結垢短循環病因：水垢糊滿生活熱水側、黑泥堵塞供暖側，熱量傳不出去！壁掛爐主回路幾秒內飆到 85°C 觸發超溫停機，水溫立刻變涼，隨後重啟週而復始。拆下酸洗或換新立竿見影。", "Gas Safe Register Technical Guidelines; C&G Unit 207"),

        # 87. Micro-bubble de-aerator
        ("7.2",
         "What is the mechanical operating principle of an in-line 'Micro-Bubble De-aerator' (such as a SpiroVent or Flamcovent) installed on the primary flow pipe?",
         "安裝在壁掛爐主供水管上的在線「微氣泡脫氣排氣閥 (Micro-Bubble De-aerator，如 SpiroVent)」具有何種水力分離原理？",
         {"A": "It compresses air into diamonds", "B": "It passes hot water through an expanded chamber filled with spiro-tubes or PALL rings, dramatically lowering velocity and forcing microscopic dissolved air bubbles to coalesce, rise, and vent out", "C": "It injects air into the radiators", "D": "It powers the water circulator"},
         {"A": "將空氣高壓壓縮成鑽石", "B": "讓高溫水流流經內部擴容腔體中特製的銅絲螺旋網（Spiro-tubes）或鮑爾環，驟降流速形成微紊流，迫使水中溶解的微觀微氣泡聚集成大氣泡並向上浮升自動排出", "C": "主動向全屋暖氣片內部注氣", "D": "給水泵循環供電"},
         "B", "Hot water holds less dissolved air than cold water. Micro-bubble de-aerators capture microscopic bubbles at the hottest point (boiler flow) before they can travel and corrode steel radiators.", "高溫脫氣物理原理：水越熱，溶在水裡的氣體越想逃逸！在出水最熱處裝脫氣閥，特殊螺旋銅絲網讓微如粉塵的小氣泡撞擊聚合成大泡飄出排氣閥，全屋管道安靜無聲絕無氣泡噪聲。", "BS EN 12828; Spirotech Technical Design Manual"),

        # 88. Boiler kettleing noise
        ("7.2",
         "What is the root cause of an alarming loud rumbling, whistling, and banging noise (known as 'Kettling') inside a central heating boiler heat exchanger?",
         "在中央供暖壁掛爐主換熱器內部發出刺耳的類似水壺燒開水般的嘯叫、隆隆轟鳴與金屬敲擊爆裂聲（俗稱「鍋爐燒水壺效應 / Kettling」），其根本物理病因是什麼？",
         {"A": "The boiler fan singing", "B": "Localized overheating and boiling of water trapped underneath dense insulating layers of limescale and magnetite sludge baked onto the heat exchanger surface", "C": "Pipes made of wood", "D": "Normal operation of condensing boilers"},
         {"A": "鍋爐風機在低溫下自發唱歌共振", "B": "高硬度水垢與磁性黑泥板結烘烤在熱交換器金屬表面形成絕熱硬殼，底層水流過熱被困在硬殼下急劇劇烈沸騰汽化、氣泡破裂引發的微觀水錘爆炸爆鳴聲", "C": "供暖管道採用了原木製造", "D": "冷凝壁掛爐出廠自帶的正常工作聲音"},
         "B", "Sludge and limescale act as thermal insulation. Heat builds up until water under the crust flash-boils into steam bubbles that collapse violently (cavitation), creating loud kettling noises.", "水壺效應（Kettling）慘象：換熱器結了厚厚水垢黑泥，熱量散不出去，金屬燒到好幾百度，泥殼底下的水瞬間化為高壓蒸汽炸開泥殼！聲音就像茶壺燒開水一樣尖叫咆哮，極易燒炸換熱器。", "BS 7593:2019; Sentinel / Fernox Boiler Noise Troubleshooting Guide"),

        # 89. Radiator cold in middle/bottom
        ("7.2",
         "During a winter service inspection, a plumber discovers that a radiator is scalding hot along the very top edge, but completely cold across the bottom and middle. What does this diagnosis indicate?",
         "在冬季供暖檢修中，水暖技師發現某組暖氣片最頂部邊緣滾燙，但整個中下部大面積區域卻冰涼透頂。這種典型的故障特徵確診了何種病因？",
         {"A": "Air trapped in the top of the radiator", "B": "Dense, heavy magnetite sludge (Fe3O4) has accumulated in a pyramid shape across the bottom of the radiator, totally blocking water flow through lower waterways", "C": "The boiler is turned off", "D": "The lockshield is leaking air"},
         {"A": "散熱器頂部積聚了大量游離空氣", "B": "沉重密實的黑色四氧化三鐵磁性腐蝕黑泥（Magnetite Sludge）在散熱器底部堆積成了金字塔狀泥堆，徹底堵死了底層全部水流通道，熱水只能走頂端直通小道流過", "C": "燃氣壁掛爐處於徹底關閉狀態", "D": "鎖閉閥正在向外劇烈漏氣"},
         "B", "Sludge settles by gravity at the bottom. The classic pyramid symptom (hot top, cold belly/bottom) proves sludge has silted up the emitter waterways, requiring chemical flushing or removal to rinse.", "水暖診斷經典口訣：若是「上涼下熱」是氣阻，排氣就好；若是「上燙下冰（底涼腰涼）」則是黑泥沉澱封死！黑渣比水重全沉在底板，必須加入清洗劑動力沖洗或拆下來搬到院子裡用膠皮管猛衝。", "BS 7593:2019 Code of Practice; C&G Unit 207"),

        # 90. Radiator pin stuck down
        ("7.2",
         "When a single radiator remains completely cold despite the heating system operating at full power, and removing the plastic TRV head reveals that the small metal valve actuator pin is depressed fully into the brass body, how should the plumber safely rectify the stuck pin?",
         "當供暖系統全負荷運轉時某組暖氣片依然冰涼，拆下 TRV 溫控手輪後發現暴露的小金屬閥桿頂針被卡死深陷在銅閥體內部無法彈起。水暖工應當如何規範安全地修復彈起卡死的頂針？",
         {"A": "Pull the pin violently with heavy pliers until it breaks off", "B": "Gently tap the outer brass hex body or lightly tap the exposed pin with a small spanner until internal spring tension pops the pin back up to its open position (using silicone lubricant if required)", "C": "Heat the valve to red heat with a gas torch", "D": "Drill a hole through the radiator panel"},
         {"A": "拿大力虎鉗死命向外猛拽金屬針直到拔斷", "B": "拿小活動扳手輕輕敲擊銅閥體側面六角螺母震動閥芯，或拿金屬面垂直輕磕頂針端部，利用內部不銹鋼彈簧的回彈力將閥針彈回敞開位置（輔以專用矽油潤滑）", "C": "用動火焊槍把整個閥門燒到通紅", "D": "用衝擊鑽在散熱器面板上鑽孔"},
         "B", "Tapping the brass valve body frees the internal rubber washer and spring without scoring the precision stainless steel pin. Gripping with pliers damages the pin, causing water leaks around the gland seal.", "TRV 卡針救援技巧：切忌用老虎鉗硬拔！硬拔會把精密不銹鋼頂針夾出劃痕毀壞 O 型密封圈導致噴水。拿小扳手輕輕敲擊銅閥體幾下，內部震動會讓彈簧自然將頂針頂出彈起，暖氣片秒熱。", "Danfoss / Drayton TRV Servicing Guidelines; C&G Unit 207")
    ]

    for sub_id, stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref in data:
        questions.append(make_q(7, sub_id, ["Unit_207"], stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref))

    return questions
