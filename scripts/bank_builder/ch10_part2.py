# Chapter 10 Part 2: Additional 35 Questions (Questions 36 to 70)
from .utils import make_q

def get_part2_questions():
    questions = []
    
    data = [
        # 36. Gas meter installation components
        ("10.1",
         "What three core control and safety components are installed directly adjacent to a domestic UK gas meter?",
         "在英國家庭自來燃氣表安裝節點處，緊貼燃氣表出入口直接配套安裝了哪三大核心控制與安全組件？",
         {"A": "A microwave, a toaster, and an iron", "B": "An Emergency Control Valve (ECV), a Meter Pressure Governor (regulator), and a Meter Bracket / mounting bar with earth bonding clamp", "C": "A water meter, a pump, and a filter", "D": "Three electrical switches"},
         {"A": "微波爐、烤麵包機以及電熨斗", "B": "緊急切斷總閥 (ECV)、燃氣表出口調壓閥 (Governor)、以及帶有電氣等電位接地夾的專用儀表固定安裝支架", "C": "自來水水表、加壓水泵以及砂濾器", "D": "三個家用照明電氣開關"},
         "B", "The meter installation incorporates the 1/4-turn ECV on the inlet riser, the factory-set 21 mbar governor, and a rigid meter bracket to prevent pipe strain, bonded with a 10mm² green/yellow earth cable.", "燃氣表三件套必考：表前有緊急球閥（ECV）；表後有 21 mbar 穩壓閥（Governor）；儀表掛在鍍鋅鋼支架上防受力下沉，並死死卡上一根 10mm² 粗黃綠接地線！", "BS 6400 Specification for installation of domestic gas meters; BS 6891"),

        # 37. Gas pipe materials
        ("10.1",
         "Which three piping materials are fully approved for domestic gas pipework installations within dwellings under BS 6891?",
         "根據英國標準 BS 6891，在家庭建築室內被法規明確批准用於敷設燃氣管道的三種管材是什麼？",
         {"A": "Lead pipe, rubber garden hose, and PVC sewer pipe", "B": "Copper tube (BS EN 1057), Corrugated Stainless Steel Tubing (CSST to BS EN 15266), and low-carbon steel pipe (BS EN 10255)", "C": "Soft silicone tube and clear glass tube", "D": "Aluminium foil and paper tubing"},
         {"A": "老舊有毒鉛管、普通花園澆水橡膠軟管、以及 PVC 塑料下水排污管", "B": "半硬紫銅管 (BS EN 1057)、不銹鋼波紋燃氣軟管 (CSST - 符合 BS EN 15266)、以及低碳厚壁鍍鋅/黑鐵鋼管 (BS EN 10255)", "C": "柔軟硅膠管與透明玻璃管", "D": "廚房鋁箔紙卷管與防潮紙管"},
         "B", "Approved internal gas materials are copper (half-hard R250), yellow-jacketed CSST, and carbon steel. Lead is strictly banned for new work; plastics (MDPE) are forbidden above ground indoors.", "室內燃氣管材合法清單：銅管（最常用，黃銅件壓接或釬焊）、帶黃色塑料防護套的 CSST 不銹鋼波紋管、以及老式螺紋黑鐵管。嚴禁使用鉛管！黃色塑料管（PE）絕對嚴禁進屋！", "BS 6891 Section 5 Materials; Gas Safe Register Guidance"),

        # 38. Yellow PE gas pipe rule
        ("10.1",
         "Why is yellow Medium Density Polyethylene (MDPE) pipe STRICTLY PROHIBITED from being routed above ground or entering inside a domestic dwelling?",
         "為什麼亮黃色的中密度聚乙烯（MDPE）燃氣專用塑料管，被法律絕對嚴禁明露敷設在室外地面以上、或直接穿牆進入家庭室內？",
         {"A": "MDPE is too expensive", "B": "MDPE softens, melts, and combusts rapidly at low fire temperatures (releasing high-pressure gas into structural house fires) and degrades under outdoor ultraviolet (UV) solar radiation", "C": "MDPE dissolves in natural gas", "D": "MDPE makes loud whistle noises"},
         {"A": "因為 MDPE 塑料管材造價極其昂貴", "B": "MDPE 塑料遇火在高溫下極易迅速軟化、熔化並爆裂助燃（在房屋火災中瞬間釋放高壓燃氣引發毀滅性大爆燃），且在室外紫外線（UV）直射下會快速脆化開裂", "C": "MDPE 塑料在天然氣中會自發溶解", "D": "MDPE 管道在通氣時會發出刺耳呼嘯噪聲"},
         "B", "Plastic gas pipes have zero fire resistance. In a house fire, an internal plastic pipe melts within 60 seconds, torching the room with high-pressure fuel. PE must transition to copper outside before entering.", "黃色塑料管不進屋鐵律：室外地下埋管全用黃色塑料管（耐腐蝕不漏氣）；但嚴禁進屋！若進屋一旦廚房著火，塑料管一分鐘就被烤化噴出熊熊燃氣大火柱！必須在室外表箱裡轉成金屬銅管再穿牆進屋！", "BS 6891 Section 5.3; IGEM/TD/4 PE gas pipelines"),

        # 39. Gas pipe jointing methods
        ("10.1",
         "Under BS 6891, what solder specification is permitted when joining domestic low-pressure copper gas installations using capillary fittings?",
         "根據 BS 6891 標準，在家庭低壓紫銅燃氣管道毛細管件對接錫焊時，法規允許採用的焊錫焊料規格是什麼？",
         {"A": "Lead-based solder containing 50% lead", "B": "Lead-free soft solder complying with BS EN ISO 9453 (e.g. 99C copper-tin alloy) or hard silver brazing alloys", "C": "Pure chewing gum", "D": "Wax candle drippings"},
         {"A": "含鉛量高達 50% 的老式含鉛焊料", "B": "符合 BS EN ISO 9453 標準的無鉛環保軟焊料（如 99C 錫銅共晶合金）或高強度硬釬焊銀釬料", "C": "普通食用薄荷口香糖", "D": "燃燒的蠟燭熔滴油灰"},
         "B", "Modern gas installations permit lead-free soft solder (BS EN ISO 9453) or silver brazing. Using soft solder requires careful flux cleanup to avoid green verdigris corrosion on copper joints.", "燃氣錫焊無鉛標準：現代燃氣銅管允許用 99C 無鉛焊錫（也可用燃氣卡壓件或銀釬焊）。切記嚴禁用老式含鉛錫焊！且焊完必須用濕抹布把酸性焊膏（Flux）擦乾淨，否則幾個月後銅管表面長滿綠鏽腐蝕沙眼。", "BS 6891; BS EN ISO 9453; C&G Unit 207"),

        # 40. Gas pipe clipping and bracket supports
        ("10.1",
         "Under BS 6891 Table 3, what is the maximum recommended support bracket spacing for horizontal runs of 15mm and 22mm copper gas pipework?",
         "根據 BS 6891 表 3 規定，15mm 與 22mm 紫銅燃氣管道在室內水平明裝敷設時，相鄰支撐管卡（Pipe Clips）之間的最大允許間距是多少？",
         {"A": "15mm: max 1.5m intervals; 22mm: max 2.0m intervals", "B": "15mm: max 10 meters; 22mm: max 20 meters", "C": "15mm: max 50mm; 22mm: max 100mm", "D": "Gas pipes must hang free without clips"},
         {"A": "15mm 管：最大間距 1.5 米 (1500mm)；22mm 管：最大間距 2.0 米 (2000mm)", "B": "15mm 管：最大 10 米；22mm 管：最大 20 米", "C": "15mm 管：最大 50mm；22mm 管：最大 100mm", "D": "燃氣管道法規嚴禁打卡子，必須懸空任其晃動"},
         "A", "Gas pipework must be securely clipped to prevent vibration fatigue and sagging: 15mm copper every 1.5m horizontally (2.0m vertically); 22mm copper every 2.0m horizontally (2.5m vertically).", "燃氣管卡間距必考：燃氣管震顫會把接頭震裂漏氣！15mm 細管水平每 1.5 米打一個卡；22mm 粗管水平每 2.0 米打一個卡。卡子打得牢，管線筆直不下垂，防止被重物撞擊變形引發漏氣！", "BS 6891 Table 3 Spacing of supports; C&G Unit 207"),

        # 41. Gas pipes in cavity walls
        ("10.1",
         "Why is it STRICTLY FORBIDDEN to route an un-sleeved gas pipe within the unventilated cavity of an external cavity wall?",
         "為什麼法律嚴禁將無護套保護的金屬燃氣管道明暗敷設在「外牆空腔夾層（Cavity Wall）」內部？",
         {"A": "Pipes will feel lonely inside the cavity", "B": "Any pinhole corrosion leak would silently discharge combustible gas into the enclosed wall cavity, travelling unseen across the entire building envelope until ignited into an explosive structural collapse", "C": "Gas loses its pressure in cavities", "D": "Cavity bricks melt in gas"},
         {"A": "金屬管道在空腔內部容易感到孤獨", "B": "任何微小的腐蝕沙眼洩漏，會將無臭/微臭的易燃氣體源源不斷充斥進封閉的牆體空腔夾層中，沿著整棟房屋外牆內襯盲目四處擴散，一旦被電氣火花引燃，整棟大樓外牆會像被炸藥包定點爆破一樣粉碎性坍塌！", "C": "燃氣在空腔內部會自發喪失所有壓力", "D": "夾心保溫磚塊遇燃氣會瞬間融化"},
         "B", "Cavity walls act like secret chimneys. Trapped gas fills the hollow space between brick leaves. An explosion blows the outer masonry leaf completely off the building. Pipes may only pass STRAIGHT through inside continuous sleeves.", "夾心牆禁走燃氣管鐵律：空心磚牆是全樓連通的死角！若在空腔裡拉煤氣管，漏了氣誰也聞不到，氣體灌滿整棟樓的牆壁夾層。等發現時一開開關，整面外牆直接被炸飛崩塌！只准垂直打洞「穿過」夾層，嚴禁在空腔裡走管！", "BS 6891 Section 8.3; Gas Safety (Installation and Use) Regs 1998"),

        # 42. Gas pipe sleeves
        ("10.1",
         "When a copper gas pipe passes through an external solid masonry wall, what construction standards are mandatory for the protective pipe sleeve under BS 6891?",
         "當紫銅燃氣管道水平穿透外圍實心磚石牆體時，根據 BS 6891 規定，外穿的專用金屬保護套管（Sleeve）有何強制性施工規範？",
         {"A": "Paper sleeve glued with honey", "B": "The sleeve must be copper or steel (extending flush or slightly past the finished wall faces), contain NO joints inside the sleeve, and have the annular gap sealed with a flexible non-hardening fireproof mastic", "C": "PVC sleeve stuffed with dry leaves", "D": "No sleeve is required"},
         {"A": "塗抹了蜂蜜的防潮紙質套管", "B": "套管材質必須採用銅管或鋼管（長度平齊或略微探出牆面）、且「套管內部絕對嚴禁留有任何管道焊接/卡壓接頭」，管道與套管之間的環形縫隙必須用防火、抗老化柔性密封膠密封封死", "C": "塞滿乾燥落葉的普通 PVC 塑料套管", "D": "直接用水泥把銅管埋死，無需套管"},
         "B", "Sleeves prevent corrosive cement touching copper and allow thermal movement. Joints inside sleeves are strictly illegal because leaks cannot be detected. Annular gaps are sealed to stop gas tracking into buildings.", "穿牆套管三戒律必考：1. 必須用金屬鋼套管或銅套管（不能用塑料）；2. 套管肚子裡「絕對不准有任何接頭（必須是整根光管）」；3. 縫隙用阻火柔性密封膠填實，防止室外一旦漏氣順著穿牆洞縫隙鑽進臥室客廳！", "BS 6891 Section 8.2; Gas Safe Technical Bulletins"),

        # 43. Gas purge procedure
        ("10.1",
         "What is the statutory purpose of the 'Gas Purging' procedure (under IGEM/UP/1B) conducted after successfully tightness testing a newly installed gas pipework system?",
         "在對新安裝的家庭燃氣管網成功通過氣密打壓試驗後，根據英國燃氣工程師學會規範 IGEM/UP/1B，實施「燃氣置換排空吹掃工藝 (Gas Purging)」的法定目的是什麼？",
         {"A": "To fill the pipes with scented smoke", "B": "To safely displace and vent 100% of the air/nitrogen trapped inside the pipework with combustible gas without releasing explosive air-gas mixtures into the room, preparing appliances for safe ignition", "C": "To freeze the pipes with nitrogen", "D": "To test the water meter"},
         {"A": "向管道內部灌滿芬芳的香薰煙霧", "B": "安全有序地用天然氣將全套管道內部殘留的 100% 全部空氣/氮氣徹底置換並排向室外，杜絕在室內密閉空間形成危險的空燃比爆炸混合氣體，確保後續燃氣用具能夠順暢一次點火成功", "C": "利用低溫液氮將金屬管道急速冷凍", "D": "校準自來水水表讀數"},
         "B", "Purging replaces inert air with pure fuel gas. If an appliance tries to light with air in the pipe, delayed ignition causes an explosive pop. Purging vents air through a hose directly outside until pure gas emerges.", "燃氣放散置換必備工藝：新裝的管子肚子裡全是空氣！若直接點壁掛爐，打火打半天打不著（全在吹空氣），等燃氣一過來「轟」的一聲爆燃炸飛外殼！必須拿軟管引到窗外安全排氣，直到放出的全是純天然氣，再點火絲滑安全！", "IGEM/UP/1B Purging procedures for small installations; BS 6891"),

        # 44. Gas appliance classification Type A, B, C
        ("10.2",
         "Under European and British standards, what are the characteristics of a 'Type C' gas appliance?",
         "在歐洲與英國燃氣用具分類體系中，所謂的「Type C 類燃氣用具」具有何種標準定義與構造特徵？",
         {"A": "A flueless portable gas camping stove", "B": "A Room-Sealed appliance where the combustion circuit (air inlet, combustion chamber, heat exchanger, and flue outlet) is completely isolated and sealed from the room in which the appliance is installed", "C": "An open coal fire with an open chimney", "D": "An electric oven"},
         {"A": "露營使用的無煙道便攜式野營氣爐", "B": "「房間密封型用具 (Room-Sealed Appliance)」：整個燃燒系統迴路（包括助燃進風口、密封燃燒室、主換熱器、以及同軸排煙口）與該用具所安裝的室內房間空氣徹底物理隔絕密封！", "C": "帶有開式磚砌煙囪的開口式燃煤壁爐", "D": "純電能驅動的廚房烤箱"},
         "B", "Type A = Flueless (e.g. cookers); Type B = Open-flued (takes air from room, vents to chimney); Type C = Room-sealed (balanced flue, 100% sealed from room). Modern combi/system boilers are Type C.", "燃氣用具三大分類必背：Type A（無煙道，如廚房燃氣灶，直接把廢氣排在廚房）；Type B（開式煙道，從屋裡吸氧、煙囪排氣）；Type C（密閉式，室外吸氧室外排煙，現代壁掛爐 100% 全是 Type C，最安全）！", "PD CR 1749 European scheme for the classification of gas appliances; BS EN 1749"),

        # 45. Flueless gas appliances ventilation requirements
        ("10.2",
         "Under BS 5440-2 and Approved Document J, what permanent air ventilation is required in a kitchen housing a domestic gas hob or cooker if the room volume is LESS than 5 cubic meters (5 m³)?",
         "根據 BS 5440-2 與建築法規 Approved Document J 規定，當廚房安裝有家用無煙道燃氣灶具、且該廚房房間總體積「小於 5 立方米 (5 m³)」時，法規對該房間的永久性通風有何極端限制？",
         {"A": "No gas cooker is permitted to be installed at all in a room under 5 m³", "B": "No ventilation is required", "C": "A small crack in the door is fine", "D": "Only an open window is required"},
         {"A": "在總體積小於 5 立方米的極度狹小房間內，法律「絕對嚴禁安裝任何燃氣灶具/燃氣烹飪設備」！", "B": "完全不需要做任何通風措施", "C": "門縫留個小縫隙即可滿足要求", "D": "僅需一扇普通的可開啟窗戶"},
         "A", "BS 5440-2 strictly prohibits flueless cooking appliances in rooms under 5 m³ (due to rapid oxygen starvation and deadly CO buildup). For rooms 5-10 m³, an openable window plus a 50cm²-100cm² permanent vent is mandatory.", "極小廚房禁止裝燃氣灶：小於 5 立方米（像個小儲藏間）的地方，嚴禁裝燃氣灶！人進去一開火，兩分鐘屋裡氧氣就被燒光窒息昏迷，隨後一氧化碳超標毒死人！5 到 10 立方米則強制開通風磚（100cm² 永久進風口）！", "BS 5440-2 Installation of flues and ventilation; Approved Document J"),

        # 46. Electronic combustion gas analyzer (ECGA)
        ("10.2",
         "When commissioning a modern condensing domestic gas boiler under BS 7967, what is the maximum permissible Carbon Monoxide to Carbon Dioxide ratio (CO/CO2 ratio) measured in the flue exhaust by an Electronic Combustion Gas Analyser (ECGA)?",
         "根據英國標準 BS 7967，在對現代冷凝燃氣壁掛爐實施試運行調試時，使用電子煙氣分析儀（ECGA）測得的排煙廢氣中「一氧化碳與二氧化碳比值 (CO/CO2 Ratio)」，法定最大允許極限值是多少？",
         {"A": "Maximum 0.0040 (or manufacturer limit, typically <0.004)", "B": "100.0", "C": "1.0", "D": "0.5"},
         {"A": "最大不超過 0.0040 (即百萬分比比值極小，通常嚴格要求小於 0.004，部分老舊設備極限不超 0.008)", "B": "允許高達 100.0", "C": "允許高達 1.0", "D": "允許高達 0.5"},
         "A", "BS 7967 dictates that safe modern boilers must operate with a CO/CO2 ratio typically below 0.004 (40 ppm CO per 1% CO2). A ratio exceeding 0.004 indicates dangerous incomplete combustion requiring immediate burner adjustment.", "煙氣分析比值 0.004 終極紅線：工程師調爐子不是看肉眼，必須插煙氣分析儀！CO/CO2 比值必須穩穩壓在 0.004 以下（也就是一萬個二氧化碳裡最多只能有 4 個一氧化碳）！若比值超標，說明缺氧燃燒嚴重，隨時毒死人，立刻關停！", "BS 7967 Carbon monoxide in dwellings; Gas Safe Technical Guidance"),

        # 47. Stoichiometric air requirement
        ("10.2",
         "Approximately how many cubic meters of fresh atmospheric air are theoretically required to achieve complete stoichiometric combustion of 1.0 cubic meter of Natural Gas (Methane)?",
         "在燃燒化學理論上，完全充分燃燒「1.0 立方米 (1 m³)」的管道天然氣（甲烷），大約需要理論消耗多少立方米的新鮮大氣助燃空氣？",
         {"A": "Approximately 9.5 to 10.0 cubic meters of air (since air is only ~21% oxygen)", "B": "0.1 cubic meters", "C": "1,000 cubic meters", "D": "1.0 cubic meter"},
         {"A": "大約需要 9.5 至 10.0 立方米的空氣 (因為普通大氣中氧氣體積分數僅佔約 21%)", "B": "僅需 0.1 立方米空氣", "C": "需要 1,000 立方米空氣", "D": "需要 1.0 立方米空氣"},
         "A", "Burning 1m³ CH4 requires 2m³ pure Oxygen (CH4 + 2O2 → CO2 + 2H2O). Because ambient air contains only ~21% O2, you must supply 2 ÷ 0.21 ≈ 9.6m³ of raw atmospheric air for every 1m³ of gas burned.", "燃氣吃風比例 1:10 必背常識：燒 1 方天然氣，理論上要 2 方純氧氣。但大氣裡 78% 全是沒用的氮氣、只有 21% 是氧氣！所以燒 1 個立方燃氣，爐子必須吞進去整整 10 個立方的巨量空氣！進風口一堵，立馬缺氧釋放劇毒 CO！", "BS 5440-2; Approved Document J; C&G Unit 207 Combustion Science"),

        # 48. Open-flued draught diverter
        ("10.2",
         "What is the mechanical function of the 'Draught Diverter' (or draught break) built into the top of an open-flued domestic gas appliance?",
         "內置在老式開式煙道燃氣用具排煙口頂部的「防風排煙罩 / 倒風分流阻斷器 (Draught Diverter)」，具有何種雙向氣流隔離保護功能？",
         {"A": "To compress flue gas into water", "B": "It prevents wind downdraughts in the chimney from blowing down and destabilizing or extinguishing the burner flames, and prevents excessive chimney updraught from drawing excess heat out of the heat exchanger", "C": "To store hot water", "D": "To power an electric fan"},
         {"A": "將排出的煙氣高壓壓縮成水滴", "B": "雙向流體阻斷：杜絕煙囪頂部狂風向下「倒灌風 (Downdraught)」直接吹滅或吹歪燃燒室底部的火苗；同時防止煙囪拔風抽力過大時將換熱器內部的熱量過度抽吸浪費", "C": "用來常年儲存洗澡熱水", "D": "為微型電動排風扇供電"},
         "B", "A draught diverter introduces room air into the flue path via an open skirt. It isolates burner combustion aerodynamics from external chimney pressure swings, preventing flame roll-out and blowout.", "防倒風罩雙向調壓閥：冬天煙囪頂上大風往下颳，若直通爐膛會把火焰生生吹滅漏氣！防風罩側面敞開，倒風順著兩側自然撇出散掉；而煙囪抽得太猛時又從室內吸點涼風補上，保證爐膛裡火苗永遠安安靜靜燃燒！", "BS 5440-1; Approved Document J Section 1; C&G Unit 207"),

        # 49. Chimney flue liners Class 1 vs Class 2
        ("10.2",
         "Under Approved Document J, what is the material difference between a 'Class 1' flexible stainless steel chimney liner and a 'Class 2' liner?",
         "根據英國建築法規 Approved Document J，耐火「Class 1 級」柔性雙層不銹鋼煙道內襯管、與「Class 2 級」內襯管在耐溫耐腐蝕上有何本質區別？",
         {"A": "Class 1 is made of plastic; Class 2 is made of copper", "B": "Class 1 liners (high-grade 316/904 stainless steel) are certified for high-temperature solid fuel (wood burning stoves, coal, multi-fuel), whereas Class 2 liners (grade 316) are strictly limited to lower-temperature gas burning appliances only", "C": "Class 1 is banned in the UK", "D": "There is no difference"},
         {"A": "Class 1 是塑料製造；Class 2 是紫銅製造", "B": "Class 1 內襯管（雙層高耐腐蝕 316/904 特種不銹鋼）通過高溫耐受認證，專用於「燃木火爐、煤炭、多燃料固體燃料壁爐」；而 Class 2 內襯管僅被允許用於排煙溫度較低的「燃氣專用用具」", "C": "Class 1 內襯管在全英國已被明令取締禁止", "D": "兩者沒有任何物理與化學耐溫區別"},
         "B", "Wood burning produces corrosive creosote and flue temperatures exceeding 500°C. Solid fuel demands heavy-gauge Class 1 (316/904 or twin-wall 904/904). Installing a Class 2 gas liner on a wood stove causes rapid burn-through and house fires.", "煙道內襯等級生死界限：柴火爐子煙氣高達五六百度且含強腐蝕焦油！若把薄薄的燃氣煙管（Class 2）插在木柴壁爐上，幾個月就被燒穿大洞引發閣樓火災！燒木頭必須用特厚耐腐蝕的 Class 1（904 雙層不銹鋼）重型內膽管！", "BS EN 1856-2 Chimneys - Metal flue liners; Approved Document J"),

        # 50. Spillage test on open-flued appliances
        ("10.2",
         "What standard commissioning procedure is conducted under BS 5440-1 using a smoke match to verify that an open-flued gas appliance is discharging its combustion products safely up the chimney?",
         "根據 BS 5440-1 標準，在對開式煙道燃氣用具進行驗收時，使用「點燃的發煙火柴（Smoke Match）」實施的「防煙氣倒灌逸出試驗 (Spillage Test)」標準步驟是什麼？",
         {"A": "Drop the match inside the fuel tank", "B": "Light the appliance, run for 5 minutes to establish natural chimney thermal updraught, hold a lit smoke match along the edge of the draught diverter relief opening, and observe that 100% of the smoke is drawn smoothly into the flue without drifting into the room", "C": "Blow the smoke into the user's face", "D": "Burn a newspaper in the room"},
         {"A": "將燃燒的火柴直接扔進燃油儲罐內部", "B": "點火啟動燃氣用具並全火連續燃燒 5 分鐘以建立煙囪自然熱浮力抽力，隨後將點燃的發煙火柴橫放在防風排煙罩邊緣開口處，親眼觀察「100% 的全部白煙是否被順暢吸入煙囪抽走」，且絕無任何煙霧反撲逸入室內房間！", "C": "將發煙火柴的濃煙對著用戶面部吹氣", "D": "在房間地板上點燃一大張舊報紙"},
         "B", "The spillage test verifies chimney draw. If smoke drifts into the room after 5 minutes of heating, combustion gases (and deadly CO) are spilling indoors. The appliance must be immediately shut down and condemned.", "防煙氣倒灌試驗必考：點火大燒 5 分鐘，煙囪被烤熱形成上升熱氣流；拿發煙火柴放在防風罩口，白煙應該像被吸塵器吸走一樣「唰」的一下全被拽進煙囪！若煙霧在屋裡打轉甚至往臉上撲，說明煙囪堵死，立刻關停下達危險禁令！", "BS 5440-1 Section 9; Gas Safe Register Spillage Testing Procedures"),

        # 51. Oil tank single-skin vs bunded rules
        ("10.3",
         "Under Environment Agency pollution prevention guidelines and BS 5410-1, in which environmental situation is an Integrally Bunded domestic oil tank STRICTLY MANDATORY (single-skin tank strictly prohibited)?",
         "根據英國環境署（EA）防污染法規與 BS 5410-1 規定，在何種嚴苛的地理環境條件下，「一體化雙層防溢油罐 (Bunded Tank)」是絕對強制的（嚴禁使用單層塑料油桶）？",
         {"A": "On top of a mountain above clouds", "B": "Where the oil tank is sited within 10 meters of an inland watercourse (river, stream, ditch), within 50 meters of a drinking water borehole/well, or over loose gravel and ground sloping towards water", "C": "Inside a garage", "D": "On sunny days only"},
         {"A": "在海拔高於雲層的雪山山頂", "B": "當儲油罐距離內陸天然水體（河流、小溪、敞開排水明溝、湖泊池塘）「在 10 米以內」、或距離飲用水自備井/地下水取水鑽孔「在 50 米以內」的任何敏感生態涉水區域！", "C": "在封閉的家庭獨立車庫內部", "D": "僅限在晴朗乾燥的天氣條件下"},
         "B", "Oil in water is catastrophic: 1 litre of oil contaminates 1 million litres of drinking water. Bunded tanks are legally mandatory near rivers (within 10m) and wells (within 50m) to stop ecological disasters.", "雙層油罐強制環境紅線：水邊 10 米、水井 50 米！一滴柴油能污染上萬升自來水，若單層塑料桶破裂，幾千升油直接衝進小溪毒死全村水源！在任何靠近小河、湖泊、池塘 10 米內的地方，法律強制必須裝雙層防護油罐！", "Control of Pollution (Oil Storage) (England) Regs 2001; BS 5410-1"),

        # 52. Oil tank sight gauge vs ultrasonic Watchman
        ("10.3",
         "What is a modern wireless 'Ultrasonic Fuel Tank Level Gauge' (such as an Apollo or Watchman gauge) used on domestic oil storage tanks?",
         "在現代家用儲油罐上廣泛配備的「超聲波無線油位指示器 (Ultrasonic Tank Gauge，如 Watchman)」，具有何種便捷與防漏優勢？",
         {"A": "A glass dipstick that breaks easily", "B": "An ultrasonic transmitter screwed into the top of the tank that bounces sound waves off the oil surface, wirelessly transmitting the real-time fuel level percentage to an electronic plug-in LCD receiver inside the home kitchen", "C": "A wooden stick dropped inside", "D": "An electric wire that ignites oil"},
         {"A": "極易碰碎破裂的透明玻璃觀測細管", "B": "安裝在油罐頂部的超聲波傳感器，向下發射超聲波脈衝探測燃油液麵反射距離，將剩餘油量百分比無線傳輸至廚房牆壁插座上的液晶顯示接收器上，無需業主冒著嚴寒去花園拿木棍探油", "C": "每次手動扔進油箱的一根長木棍", "D": "直接浸泡在燃油中通電的發熱電線"},
         "B", "Watchman ultrasonic transmitters eliminate messy manual dipsticks and fragile external sight tubes (which historically perverted and spilled fuel). Occupants monitor fuel levels from comfort inside the house.", "無線超聲波油位計（Watchman）革命：以前看油要冒雪掀開蓋子拿木棍捅，或者看老式塑料透明軟管（軟管老化一碰就碎漏一地油）。超聲波從頂部打回音波，在廚房坐著看插座上的小屏幕就知道還剩幾格油，及時叫油車送油！", "OFTEC Technical Book 3; Watchman / Apollo Sonic Product Manuals"),

        # 53. Oil de-aerator Tigerloop
        ("10.3",
         "What is the operational function of an automatic in-line Oil De-aerator (such as a 'Tigerloop') fitted on the suction supply pipework of a domestic pressure-jet oil boiler?",
         "安裝在家庭壓力噴霧式燃油壁掛爐進油管道上的在線「自動除氣除泡器 (Oil De-aerator，俗稱 Tigerloop)」，具有何種核心水力功能？",
         {"A": "It converts oil into natural gas", "B": "It allows a clean single-pipe oil feed from the distant tank while acting as a closed-loop de-aerating chamber at the boiler, automatically venting tiny air bubbles out of the suction line and eliminating the costly, leak-prone underground two-pipe return line", "C": "It freezes dirty oil", "D": "It powers the boiler pump electrically"},
         {"A": "將重質燃油在線裂解轉化為天然氣", "B": "允許從室外油罐只敷設「單根單管進油」，而在鍋爐前充當微型除氣室：全自動將吸油管內析出的微小氣泡排向室外，消除了管內氣塞氣阻，並省去了容易發生地下暗漏的老式雙管回油管！", "C": "將含有雜質的髒燃油急凍成固體", "D": "完全依靠自身電力驅動燃油油泵"},
         "B", "Tigerloops eliminate two-pipe suction lines. In a 1-pipe system, trapped air bubbles cause oil pump cavitation and flame lockout. The Tigerloop vents air bubbles harmlessly, providing a pristine single-pipe feed.", "Tigerloop 神仙配件必考：老式燃油爐必須拉兩根銅管（一進一回），回油管埋在地下萬一腐蝕漏油神不知鬼不覺。裝了 Tigerloop，外面只拉一根進油管！它像個小浮球濾杯，把油裡的小氣泡自動排走，油泵吸油永遠平穩，絕不熄火！", "OFTEC Technical Information TI/139; Tigerholm Technical Guidelines"),

        # 54. Oil burner filter micron rating
        ("10.3",
         "Why is a fine primary in-line oil filter (typically with a 50-micron paper or washable stainless steel mesh element) MANDATORY on the fuel supply line before reaching an oil burner?",
         "在燃油管道進入燃油燃燒器之前，管路上為什麼必須強制安裝一個孔徑精細（通常為 50 微米濾紙或不銹鋼濾網）的「專用進油過濾器」？",
         {"A": "To extract drinking water from fuel", "B": "Pressure-jet burner atomizing nozzles feature microscopic metering slots (apertures as small as 0.2mm); microscopic dust, rust, and tank silt would instantly choke the nozzle, causing immediate flame failure and boiler lockout", "C": "To color the oil purple", "D": "To cool the oil down to 0°C"},
         {"A": "從燃油中提煉提取出純淨飲用水", "B": "燃油壁掛爐的噴霧霧化噴嘴內部開有極其精密的微觀旋流槽（孔徑小至 0.2 毫米）；油箱裡的微細鐵鏽、泥沙微粒會瞬間將噴嘴完全堵死，導致燃燒器噴不出油當場熄火停機！", "C": "將燃油顏色染成紫色以便識別", "D": "將燃油溫度冷卻降低至 0°C"},
         "B", "Pressure jet nozzles spray atomized oil mist at ~10 bar through microscopic orifices. Without a 50-micron filter, fine sediment from the storage tank clogs the nozzle slot within hours.", "50 微米過濾器保護心臟：燃油壁掛爐的噴嘴就像醫院的注射器針頭一樣細！十幾公斤高壓把油擠成薄霧點火。如果油裡有一顆沙子，噴嘴立刻被卡死噴不出油。外裝一個 50 微米過濾器把所有髒雜質全部死死濾掉！", "OFTEC Technical Book 3; Danfoss Burner Components Handbook"),

        # 55. Oil burner nozzle markings
        ("10.3",
         "On a replacement oil burner pressure-jet nozzle stamped with '0.60 80° H', what do these three critical engineering designations specify?",
         "在燃油壁掛爐壓力噴霧噴嘴黃銅外殼上激光雕刻的標記「0.60 80° H」，分別精確代表何種燃油噴射性能參數？",
         {"A": "0.60 US Gallons per hour throughput at 7 bar, 80-degree spray cone angle, and 'H' indicates a Hollow cone spray pattern", "B": "60 mm diameter, 80 bar pressure, and Heavy oil", "C": "0.60 litres per minute, 80°C temperature, and High speed", "D": "0.60 horsepower, 80 minutes burn time, and Heat only"},
         {"A": "0.60 代表在 7 bar 基準油壓下每小時噴出 0.60 美制加侖燃油；80° 代表噴出的霧化圓錐角為 80 度；字母 H 代表「空心圓錐噴霧模式 (Hollow Cone)」", "B": "直徑 60 毫米、工作壓力 80 bar、且僅限燃用重油", "C": "每分鐘流量 0.60 升、燃油溫度 80°C、且屬於高速運轉型", "D": "功率 0.60 馬力、燃燒時間 80 分鐘、且僅供供暖"},
         "A", "Nozzle marking decoded: '0.60' = throughput in US Gallons/hr at 100 psi (7 bar); '80°' = spray angle; 'H' = Hollow spray pattern (distributes oil to outer perimeter; 'S' = Solid cone for smaller combustion chambers).", "噴嘴三維密碼必考：0.60 是流量（每小時噴 0.6 美國加侖，決定壁掛爐輸出多少千瓦）；80° 是霧化角度（火苗噴開有多寬，決定火苗胖瘦）；H 是形狀（空心噴霧，讓火苗像空心花一樣展開，S 是實心噴霧）。更換噴嘴必須一模一樣！", "Danfoss / Delavan Oil Burner Nozzle Application Guide; C&G Unit 207"),

        # 56. Oil burner photocell flame failure
        ("10.3",
         "What is the protective operating principle of the optical 'Photocell' (flame sensor) installed inside an automatic pressure-jet oil burner?",
         "安裝在家用全自動壓力噴霧式燃油燃燒器內部核心的「光電管火焰感應器 (Photocell)」，具有何種熄火保護機制？",
         {"A": "It takes photographs of the user", "B": "It contains a light-sensitive cadmium sulfide (CdS) resistor that senses visible light from the active flame; if the flame fails to ignite or blows out, the resistance changes, causing the control box to lock out the fuel solenoid within seconds", "C": "It creates electric sparks for lighting", "D": "It cools the boiler casing"},
         {"A": "在點火時自動為操作人員拍照存檔", "B": "內置高靈敏度硫化鎘（CdS）光敏電阻，實時緊盯監測燃燒火焰發出的可見光；若點火未成功或燃燒中途火焰意外熄滅，光敏阻值瞬間暴增，主控盒在 2-5 秒內立刻關閉電磁閥並鎖死停機（Lockout）！", "C": "為壁掛爐點火持續提供高壓電火花", "D": "為壁掛爐外殼提供水冷降溫"},
         "B", "If an oil burner pumps fuel without flame, it sprays vaporized kerosene onto red-hot combustion walls, driving catastrophic delayed explosive detonation. The photocell cuts oil within ~2 seconds of flame loss.", "光敏眼（Photocell）防爆靈魂：油泵每分鐘都在往爐膛裡狂噴霧化煤油！若火滅了還繼續噴，滿爐子全是高壓易燃油氣，等下次點火會直接把整座房子炸塌！光敏電阻一看不見亮光，兩秒內死死掐斷供油電磁閥鎖死報警！", "BS EN 267 Automatic forced draught burners for liquid fuels; OFTEC Book 3"),

        # 57. Heat pump defrost cycle
        ("10.5",
         "Why does an outdoor Air Source Heat Pump (ASHP) periodically initiate an automatic 'Defrost Cycle' during damp UK winter days when ambient air is between 0°C and 5°C?",
         "在氣溫處於 0°C 至 5°C 之間潮濕陰冷的英國冬季，室外空氣源熱泵（ASHP）為什麼會每隔一段時間自動啟動「化霜除霜程序 (Defrost Cycle)」？",
         {"A": "To make ice cream", "B": "Moisture in the damp air condenses and freezes into a solid blanket of frost across the sub-zero outdoor evaporator fins, blocking airflow; the heat pump temporarily reverses refrigerant flow to melt the ice quickly", "C": "To heat the garden lawn", "D": "Because the compressor has failed"},
         {"A": "為家庭自發製作冰淇淋甜品", "B": "潮濕空氣中的水分子在低於冰點的室外換熱器翅片表面凝結結霜成厚厚冰被，徹底堵死空氣流通通道；熱泵自動短暫反轉製冷劑流向，抽取管網熱量迅速將翅片上的厚冰融化化水排走", "C": "為室外花園草坪提供表面熱量", "D": "因為內部壓縮機發生了不可逆損壞"},
         "B", "At 0-5°C ambient, the outdoor coil runs at -5°C to -10°C, causing heavy frost buildup. Ice chokes the fan airflow, halting heat extraction. Reversing the cycle sends hot gas into the outdoor coil to melt the ice.", "潮濕化霜物理原理：很多人以為零下十度最愛結霜，其實 2-4°C 潮濕陰雨天結霜最瘋狂！空氣濕度 90%，冷媒在零下幾度，水氣一碰翅片立刻結成厚雪球，風透不過去了。熱泵自動反向調轉閥門，把熱氣打回外機，兩分鐘把冰化得嘩嘩淌！", "BS EN 14511; MCS Heat Pump Guide MIS 3005; C&G Unit ENV"),

        # 58. Heat pump buffer tank
        ("10.5",
         "What is the primary hydraulic purpose of installing a 'Buffer Tank' (Buffer Cylinder) in an Air Source Heat Pump central heating circuit?",
         "在空氣源熱泵供暖水系統中，加裝「緩衝水箱 (Buffer Tank / Volume Cylinder)」的最核心水力功能是什麼？",
         {"A": "To store drinking water for the kitchen", "B": "To ensure the heating circuit contains the minimum required water volume (typically 10-15 litres per kW) to prevent compressor short-cycling and provide thermal energy during winter defrost cycles without chilling the house", "C": "To generate electricity", "D": "To filter sediment"},
         {"A": "為廚房水槽常年儲存潔淨飲用水", "B": "確保供暖循環管網中始終具備系統製造商規定的「最低循環存水容積（通常為每 kW 功率需 10-15 升存水）」：徹底防止壓縮機頻繁短週期啟停短循環，並為冬季化霜提供充足熱量（防止化霜時抽走暖氣片熱量讓房間變冷）", "C": "利用溫差發電對外供電", "D": "過濾系統水質中的粗砂雜質"},
         "B", "Heat pumps require minimum volume (~12 L/kW) to avoid short-cycling when TRVs close. During defrost, the heat pump steals heat from water; a buffer tank prevents radiators getting cold during the 3-minute thaw.", "緩衝水箱雙重使命必考：1. 防短循環：各房間溫控閥一旦關閉，水管水太少，熱泵一分鐘就燒熱熄火、兩分鐘又開機（壓縮機幾個月就折騰壞）；2. 化霜能量庫：外機化霜要從室內水裡偷熱化冰，緩衝水箱頂上，客廳暖氣片紋絲不涼！", "MCS MIS 3005 Heat Pump Design; Heat Pump Manufacturers Engineering Manuals"),

        # 59. Heat pump Legionella pasteurization cycle
        ("10.5",
         "Because domestic heat pumps typically heat hot water cylinders to approximately 50°C for peak COP efficiency, how is the biological risk of deadly Legionella pneumophila bacteria eliminated under ACoP L8?",
         "由於空氣源熱泵為了保持最高 COP 能效，通常僅將生活熱水水罐加熱至約 50°C，根據英國軍團菌控制法規 ACoP L8，系統是如何徹底消除「嗜肺軍團菌」致命生物滋生風險的？",
         {"A": "By adding chlorine bleach into the bath every night", "B": "The heat pump controller automatically triggers a periodic 'Legionella Pasteurization Cycle' (typically weekly), activating an electric immersion heater to boost the cylinder water temperature to at least 60°C to 65°C for one hour", "C": "By cooling the water to freezing point", "D": "Legionella cannot survive in heat pump systems"},
         {"A": "每天晚上向洗澡浴缸中倒入消毒漂白水", "B": "熱泵智能控制器自動定期執行「軍團菌高溫巴氏殺菌程序 (Pasteurization Cycle，通常每週一次)」：主動啟動水罐內置的大功率輔助電加熱棒（Immersion Heater），將全罐水溫強制提升至「60°C 至 65°C」並保持至少 1 小時，將細菌徹底燙死！", "C": "將水罐溫度急凍降低至冰點", "D": "軍團菌在熱泵系統中天生無法存活"},
         "B", "Legionella multiplies between 20°C and 45°C. At 60°C, 90% of bacteria die in 2 minutes; at 65°C, in seconds. An automated weekly immersion boost to 60°C ensures safe, pathogen-free domestic hot water.", "軍團菌高溫殺菌法規底線：軍團菌最喜歡 30-45°C 的溫水！熱泵平時省電燒 50°C，細菌容易暗中滋生。熱泵自帶定時任務：每週日半夜自動開電加熱棒，把水罐一口氣燒到 60°C 甚至 65°C 煮一個小時，殺光所有病菌！", "HSE Approved Code of Practice L8; Building Regulations Approved Document G3"),

        # 60. Heat pump anti-vibration mountings
        ("10.5",
         "What two installation precautions are mandatory under MCS MIS 3005 to prevent low-frequency compressor vibration noise from transmitting into a dwelling structure?",
         "根據 MCS MIS 3005 標準，在安裝室外空氣源熱泵主機時，必須採取哪兩項強制防震降噪工藝以杜絕壓縮機低頻震動共振傳入建築住宅結構？",
         {"A": "Glue the heat pump directly to the living room window glass", "B": "Mount the heat pump on resilient rubber anti-vibration mounting feet on a solid independent concrete plinth, and connect water pipework using flexible stainless steel braided anti-vibration hoses", "C": "Tie the unit to a wooden fence with string", "D": "Wrap the outdoor fan in heavy towels"},
         {"A": "用玻璃膠將熱泵主機直接粘在客廳窗玻璃上", "B": "將主機安裝在獨立堅固的室外混凝土基座上的專用「高彈性防震橡膠阻尼腳墊」上，並使用「不銹鋼編織防震柔性軟管」與室內供回水硬銅管相連接", "C": "拿麻繩把熱泵外機捆綁在木花園籬笆上", "D": "拿厚毛巾將室外旋轉風扇包裹"},
         "B", "Compressors vibrate at ~50 Hz. Bolting rigidly to walls or using rigid copper pipes turns house walls into giant acoustic speakers. Anti-vibration feet and braided flexi-hoses isolate all mechanical vibrations.", "防震消音兩大法寶必考：壓縮機是個大發動機！若直接用鐵螺絲釘在外牆上、硬銅管直接接進屋，整棟樓的臥室客廳會嗡嗡作響像開飛機一樣！底座必須踩著厚橡膠減震墊，進出水管必須接一段波紋金屬軟管，隔斷所有共振！", "MCS Installation Standard MIS 3005; British Standard BS EN 14511"),

        # 61. Monobloc heat pump anti-freeze valves
        ("10.5",
         "In an Air Source Heat Pump 'Monobloc' system where heating water circulates directly through the outdoor unit, what device protects the outdoor heat exchanger from bursting if a prolonged power failure occurs during deep winter?",
         "在供暖水直接循環流經室外主機的「一體式空氣源熱泵 (Monobloc)」系統中，若冬季嚴寒大雪天遭遇全屋長時間斷電停機，應配備何種安全保護裝置以防室外換熱器凍裂報廢？",
         {"A": "Mechanical Anti-Freeze Dump Valves (which automatically snap open by thermostatic expansion when water temperature drops below ~3°C, draining outdoor water)", "B": "A gas blowlamp pointing at the unit", "C": "A bucket of boiling water poured on the unit", "D": "A paper blanket"},
         {"A": "機械式低溫自動排空防凍閥 (Anti-Freeze Valve - 內部溫感閥芯在水溫跌至約 3°C 臨界點時自動機械打開，將室外主機內部的存水排空洩盡)", "B": "一把對準外機持續噴火的動火焊槍", "C": "向外機定期澆下一桶沸騰開水", "D": "蓋上一條保溫紙被"},
         "B", "Monobloc pipes run outdoors. During a winter power cut, pumps stop and stagnant water freezes solid in hours, cracking the £3,000 brazed plate heat exchanger. Mechanical antifreeze dump valves drain water before it freezes.", "一體機防凍閥救命神機：分體機走冷媒不怕凍，一體機（Monobloc）可是直接把熱水管通到天寒地凍的室外！大雪天萬一停電水泵不轉，室外水管幾小時就凍成鐵棍撐爆昂貴主機！防凍閥感應到水溫跌破 3°C，立刻自動開閥洩光室外存水！", "Caleffi / Reliance Antifreeze Valve Technical Specifications; MCS MIS 3005"),

        # 62. Hybrid heat pump systems
        ("10.5",
         "What is a 'Hybrid Heat Pump' central heating system, and how does its smart control logic optimize domestic energy costs?",
         "什麼是「雙能源混動熱泵供暖系統 (Hybrid Heat Pump System)」，其內置的智能控制邏輯是如何優化家庭燃氣與電費支出的？",
         {"A": "It runs on diesel fuel and coal", "B": "It combines an Air Source Heat Pump with a high-efficiency gas condensing boiler; a smart controller monitors outdoor temperatures and real-time gas/electricity tariffs, dynamically firing whichever heat source is cheapest and most efficient at that exact moment", "C": "It is an electric car charger", "D": "It heats only during full moons"},
         {"A": "同時燃燒柴油與煤炭的混合系統", "B": "將空氣源熱泵與高效燃氣冷凝壁掛爐有機結合並聯：智能主控器動態監測室外實時氣溫與電費/天然氣即時價格，在春秋溫和時開熱泵極致節能，在嚴寒極寒或高電價峰段自動無縫切換壁掛爐大火供暖，哪種便宜開哪種！", "C": "專為電動汽車充電的家用充電樁", "D": "僅在滿月之夜才啟動加熱的系統"},
         "B", "When outdoor air is mild (>5°C), the heat pump is cheapest (COP >3.5). In freezing sub-zero weather or during peak electricity tariff spikes, the gas boiler fires instead, ensuring lowest running costs.", "混動熱泵（省錢精靈）：白天電價便宜、室外 10 度，熱泵開動，COP 飈到 4.0，幾乎零成本；晚上外面零下 5 度、或者遇上電費高峰期，電腦自動關熱泵、點燃天然氣壁掛爐轟轟燒大火！既不換大散熱器，又把電費氣費壓到最低！", "Baxi / Worcester Bosch Hybrid Heat Pump Technical Guides; C&G Unit ENV"),

        # 63. Solar thermal collector glazing
        ("10.5",
         "Under BS EN 12975, what type of glass is exclusively specified for the front glazing of high-performance flat plate solar thermal collectors?",
         "根據 BS EN 12975 標準，在高性能平板型太陽能集熱器的採光正面上，指定採用何種特種玻璃以確保最大光能透過率與抗衝擊強度？",
         {"A": "Ordinary thin green picture-frame glass", "B": "Low-Iron Tempered (Toughened) Solar Safety Glass (transmitting over 90% of solar radiation and resisting severe hailstone impacts)", "C": "Frosted bathroom privacy glass", "D": "Opaque dark lead glass"},
         {"A": "普通發綠色的廉價相框薄玻璃", "B": "超白低鐵鋼化太陽能專用安全玻璃 (Low-Iron Tempered Glass - 太陽輻射全光譜透光率超 90% 以上，且具備極強的抗冰雹衝擊抗砸強度)", "C": "浴室防窺磨砂毛玻璃", "D": "完全不透光的深色防核輻射鉛玻璃"},
         "B", "Iron impurities give ordinary glass a greenish tint that absorbs and blocks solar radiation. Low-iron glass maximizes solar transmission (>91%), and thermal tempering resists severe hailstone impacts.", "超白低鐵鋼化玻璃必考：普通窗戶玻璃側著看發綠，因為含鐵量高，會把太陽光吸收反彈掉！太陽能專用玻璃把鐵雜質全部提純拔除，像水晶一樣透明，透光率破 91%，而且高溫鋼化過，冰雹砸上去蹦蹦跳絕不碎裂！", "BS EN 12975 Solar collectors; C&G Unit ENV Renewable Technologies"),

        # 64. Solar thermal pump station components
        ("10.5",
         "What essential hydraulic and safety components are integrated inside a pre-fabricated 'Solar Pump Station' mounted adjacent to the solar hot water cylinder?",
         "緊靠太陽能熱水儲罐安裝的一體化「太陽能專用雙管水泵工作站 (Solar Pump Station)」外殼內部，自帶集成了哪些核心水力與安全配件？",
         {"A": "A gas burner and a toaster", "B": "A high-temperature solar circulator pump, mechanical flow meter (sight glass with flow regulator), two isolation ball valves with integrated non-return check valves and temperature gauges, a 6-bar safety relief valve, and a pressure gauge", "C": "A domestic washing machine", "D": "A water softener only"},
         {"A": "燃氣燃燒器與廚房吐司機", "B": "高溫專用太陽能循環泵、機械流量計（帶刻度視鏡流量調節閥）、兩個自帶內置止回閥與紅藍溫度計的截止球閥、6 bar 專用安全洩壓閥、以及管網壓力表", "C": "家用滾筒洗衣機", "D": "自來水離子交換軟水機"},
         "B", "Solar stations bundle flow/return valves, 6-bar PRV, flow meter, and pump into an insulated EPP foam casing. The integrated check valves prevent reverse thermosiphoning of cylinder heat to cold roof panels at night.", "太陽能工作站黑箱子揭秘：泡沫保溫箱裡麻雀雖小五臟俱全！有抗 130°C 的專用循環水泵、看流量的小視鏡、6 bar 安全閥。最重要的是裡面自帶兩個單向止回閥，防止半夜沒太陽時，水罐裡的熱水偷偷倒流回樓頂把天空給加熱了！", "BS EN 12976; Resol / PAW Solar Station Technical Handbooks"),

        # 65. Greywater vs Blackwater definition
        ("10.5",
         "In domestic water conservation and environmental engineering, what is the precise legal distinction between 'Greywater' and 'Blackwater'?",
         "在家庭節水工程與可持續環境排水法規中，「灰水 (Greywater)」與「黑水 (Blackwater)」的法定劃分邊界是什麼？",
         {"A": "Greywater is rainwater; Blackwater is clean tap water", "B": "Greywater is wastewater originating from baths, showers, washbasins, and laundry washing machines; Blackwater is heavily contaminated wastewater originating from WCs (toilets), bidets, and food waste kitchen sinks", "C": "There is no distinction", "D": "Greywater comes only from cars"},
         {"A": "灰水是天然雨水；黑水是自來水公司潔淨自來水", "B": "灰水是指來自「浴缸、淋浴底盤、洗手盆、以及洗衣機」的生活洗浴洗滌廢水；黑水是指來自「抽水馬桶 (WC)、婦洗器、以及含有大量油脂菜葉的廚房洗滌槽」的重污染高病原體污水！", "C": "兩者在法律與衛生標準上沒有任何區別", "D": "灰水是指沖洗汽車排放的泥水"},
         "B", "Greywater contains low pathogen loads and soap residues, making it easily treatable on-site for toilet flushing. Blackwater carries heavy biological pathogen risks (feces) and putrefying grease, requiring foul sewer treatment.", "灰水與黑水生死邊界必考：洗澡水、洗手水、洗衣服水叫「灰水（Greywater）」，相對乾淨，過濾消毒後可以拿來二次沖馬桶；而馬桶大便水和廚房洗菜洗肉水叫「黑水（Blackwater）」，充滿大腸桿菌和油脂腐殖物，必須直奔排污管！", "BS 8525-1 Greywater systems; Building Regulations Approved Document H"),

        # 66. Greywater recycling treatment
        ("10.5",
         "Under British Standard BS 8525, what biological/physical treatment stages are typically employed in a domestic Greywater Recycling system before water is reused for toilet flushing?",
         "根據英國標準 BS 8525 規定，家庭灰水回收利用系統在將淋浴廢水回用於沖廁之前，通常必須經過哪幾道物理與生化處理工序？",
         {"A": "Boiling with nuclear power", "B": "Coarse hair/lint filtration, biological aeration or membrane filtration (MBR), settling, and chemical disinfection (chlorine dosing or UV sterilization)", "C": "Adding sugar to the water", "D": "No treatment is required"},
         {"A": "利用核能將廢水整體高溫煮沸", "B": "粗效毛髮與織物纖維過濾、好氧生物曝氣或超濾膜生物反應器（MBR）、固液沉澱分離、以及最終化學消毒（氯片消毒或紫外線 UV 殺菌）", "C": "向水箱中加入食用白糖", "D": "完全無需經過任何淨化處理直接使用"},
         "B", "Raw greywater stored for >24 hours turns black and breeds anaerobic bacteria. Filtration removes hair, aeration digests soap scum, and UV/chlorine prevents bacterial regrowth in toilet cisterns.", "灰水不處理就是毒水：洗澡水放滿 24 小時，裡面的皮屑油脂會發酵成黑臭死水！系統先用金屬網濾掉頭髮，微孔膜把肥皂沫濾乾淨，最後打紫外線或加顆氯片消毒，水質清亮無臭，再送進馬桶水箱才不發臭！", "BS 8525-1 Greywater systems - Code of practice; C&G Unit ENV"),

        # 67. Domestic water-saving fittings
        ("10.5",
         "Under Building Regulations Approved Document G2, what is the mandatory maximum daily water consumption target per person across new UK domestic dwellings?",
         "根據英國建築法規 Approved Document G2 規定，在英格蘭境內新建住宅中，法定強制要求的每人每日最大生活用水總定額（Water Consumption Target）是多少？",
         {"A": "Maximum 125 litres per person per day (or 110 L/person/day where required by local planning)", "B": "5,000 litres per person per day", "C": "1 litre per person per day", "D": "No water limit applies"},
         {"A": "每人每天法定最高不超過 125 升 (125 L/person/day)，若地方規劃有嚴格節水政策時收緊至 110 升/人/天", "B": "每人每天 5,000 升大容量配額", "C": "每人每天僅限 1 升極端配額", "D": "英國法規對新建住宅用水總量毫無限制"},
         "A", "Part G2 sets a baseline maximum of 125 L/person/day (often tightened to 110 L by local councils). Plumbers achieve this using 4/2.6L dual flush WCs, aerated 8 L/min showerheads, and tap flow regulators.", "新建房節水 125 升死標準必考：新房驗收必須拿水暖計算表算總分！每人每天不能超過 125 升自來水（嚴苛地區 110 升）。水暖工必須配節水龍頭（裝起泡器每分鐘 4 升）、節水花灑（每分鐘 8 升）、以及雙檔節水馬桶！", "Building Regulations Approved Document G Section G2; Water Calculator Regulations"),

        # 68. Energy Performance Certificates (EPC)
        ("10.5",
         "What is an Energy Performance Certificate (EPC) required under the Energy Performance of Buildings Regulations when a domestic property is constructed, sold, or rented?",
         "根據英國建築能源性能法規，當家庭住宅進行新建、出售或出租時，法定的「房屋能源性能證書 (EPC)」具有何種能效評級標準？",
         {"A": "A tax bill for car parking", "B": "An official asset rating assessing the fabric insulation and heating efficiency of a property on a standardized scale from Band A (most efficient, low running costs) down to Band G (least efficient, high fuel bills)", "C": "A certificate proving the house is built of stone", "D": "A receipt for buying furniture"},
         {"A": "機動車路邊停車的市政罰款單", "B": "官方出具的法定房屋能效資產評級報告：基於建築圍護結構保溫與採暖系統綜合能效，按統一能效等級劃分標準，由最高「Band A 級 (最節能、能耗成本極低)」一路排至最低「Band G 級 (極度耗能、燃氣賬單昂貴)」", "C": "證明房屋完全由純天然花崗岩石塊壘砌的證書", "D": "購買全套客廳傢俱的商業發票憑據"},
         "B", "EPCs measure theoretical energy performance using SAP software. UK Minimum Energy Efficiency Standards (MEES) prohibit landlords from renting out properties with an EPC rating below Band E.", "EPC 房屋能效身份證：租房買房第一眼看 EPC 彩色條形圖！A 級最綠最省錢，G 級最紅最費氣。英國法律規定出租房最低必須達到 E 級以上；否則房東不准出租！加裝保溫棉、換高效冷凝爐或熱泵能讓評級大幅飆升！", "Energy Performance of Buildings (England and Wales) Regulations 2012; MEES Regulations"),

        # 69. Microgeneration Certification Scheme (MCS)
        ("10.5",
         "Why must a domestic heat pump or solar thermal installation be carried out by a certified Microgeneration Certification Scheme (MCS) installer in the UK?",
         "在英國家庭安裝空氣源熱泵或太陽能熱水系統時，為什麼必須由持有「微型發電認證計劃 (MCS)」資質的專業認證工程企業施工並出具證書？",
         {"A": "MCS installers provide free furniture", "B": "MCS certification proves the installation complies with national engineering standards (e.g. MIS 3005) and is the legally required prerequisite for the homeowner to claim UK government funding grants (such as the £7,500 Boiler Upgrade Scheme grant)", "C": "Uncertified installations are punished by jail", "D": "MCS is a brand of paint"},
         {"A": "MCS 認證企業施工會免費贈送客廳傢俱", "B": "MCS 認證證書是工程質量符合國家權威標準（如 MIS 3005）的法定憑證，且是業主合法申領英國政府鉅額補貼（如高達 7,500 英鎊的 Boiler Upgrade Scheme 鍋爐升級補貼款）的「強制前置法定必備條件」！", "C": "無資質安裝會在第二天被判處入獄", "D": "MCS 是一家生產外牆塗料的品牌商標"},
         "B", "Without MCS certification, homeowners are barred from the £7,500 government Boiler Upgrade Scheme (BUS) grant. MCS verifies rigorous design, correct heat-loss sizing, acoustic calculations, and commissioning.", "MCS 認證價值 7500 鎊大紅包：英國政府補貼 7,500 英鎊鼓勵大家拔掉老煤氣爐換熱泵。但錢不是隨便給的！安裝公司和設備必須具備 MCS 雙重認證，拿不到 MCS 竣工註冊編號，一分錢補貼都拿不到！", "Microgeneration Certification Scheme Standards; Boiler Upgrade Scheme (BUS) Regulations"),

        # 70. Hazardous waste management for plumbing
        ("10.5",
         "Under the Hazardous Waste Regulations 2005 and Environmental Protection Act 1990, what strict legal duty applies to a heating engineer when disposing of drained heating glycol, legacy lead pipes, or waste fuel oil?",
         "根據英國 2005 年危險廢物法規與 1990 年環境保護法，水暖供熱工程師在現場拆除清理廢棄的供暖防凍乙二醇、老舊有毒鉛水管、或廢棄燃油時，負有何種嚴格的法律「處置注意義務 (Duty of Care)」？",
         {"A": "Pour it down the nearest public rainwater drain on the street", "B": "Must classify, store safely, transport with a registered waste carrier, complete a statutory Hazardous Waste Consignment Note, and ensure disposal occurs at a licensed environmental recycling facility (never dumped in drains or fly-tipped)", "C": "Bury the waste in the customer's garden under turf", "D": "Throw it in the regular domestic household dustbin"},
         {"A": "直接傾倒在馬路邊距離最近的室外公共雨水箅子地漏中", "B": "必須依法分類安全儲存、聘請持有合法執照的註冊廢物運輸商、簽署法定「危險廢物交接聯單 (Hazardous Waste Consignment Note)」、並確保送達有資質的環保專項處理中心（嚴禁傾倒進下水道或野外非法拋棄）", "C": "在客戶花園草坪下挖坑深埋", "D": "直接扔進客戶生活垃圾塑料桶中任由環衛車收走"},
         "B", "Dumping toxic glycol, lead, or oil into drains is a major environmental crime carrying unlimited fines. Heating engineers have a strict Duty of Care tracked by Consignment Notes to registered disposal sites.", "環保處置注意義務（違法直排罰款無上限）：廢機油、含鉛老水管、防凍液屬於法定危險廢物（Hazardous Waste）！誰敢偷倒進馬路雨水溝，環保署通過排污口追查上門，企業和個人會被處以天價罰款甚至吊銷執照！必須填寫五聯單合規送站！", "Hazardous Waste (England and Wales) Regulations 2005; Environmental Protection Act 1990 s.34")
    ]

    for sub_id, stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref in data:
        questions.append(make_q(10, sub_id, ["Unit_ENV", "Unit_207"], stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref))

    return questions
