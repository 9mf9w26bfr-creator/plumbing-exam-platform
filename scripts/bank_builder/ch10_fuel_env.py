# Chapter 10: Domestic fuel systems & Environmental technologies (Part 1: Questions 1 to 35)
from .utils import make_q

def get_questions():
    questions = []
    
    data = [
        # 10.1 Gas Characteristics, Pressures & LPG
        ("10.1",
         "What is the chemical composition and relative density (specific gravity compared to air = 1.0) of Natural Gas supplied through the UK mains gas network?",
         "在英國城市天然氣管網中供應的「管道天然氣 (Natural Gas)」，其主要化學成分及其相對於空氣（空氣=1.0）的相對密度是多少？",
         {"A": "Carbon Monoxide, relative density 2.5", "B": "Methane (CH4, approx 90-95%), relative density approx 0.6 (lighter than air, naturally rises and disperses)", "C": "Pure Hydrogen, relative density 1.5", "D": "Oxygen, relative density 1.0"},
         {"A": "一氧化碳，相對密度為 2.5", "B": "甲烷 (CH4，佔比約 90-95%)，相對密度約為 0.6 (比空氣輕，泄漏時自然向上飄浮擴散)", "C": "純氫氣，相對密度為 1.5", "D": "純氧氣，相對密度為 1.0"},
         "B", "Natural gas is predominantly Methane (CH4) with a specific gravity of ~0.6. Being lighter than air, escaping natural gas rises to the ceiling and disperses easily through high-level vents.", "天然氣物理特性必考：主要成分是甲烷（CH4），相對密度僅約 0.6（空氣是 1.0）。因為比空氣輕，家裡一旦漏氣，天然氣會第一時間像氣球一樣飄向天花板，開頂部高窗能快速散氣，不易沉底。", "BS 6891 Specification for installation of low pressure gas pipework; C&G Unit 207"),

        ("10.1",
         "What is the standard nominal standing/operating pressure of Natural Gas at the meter outlet governor in a typical UK domestic installation?",
         "在英國標準家庭住宅燃氣工程中，安裝在入戶燃氣表出口調壓閥處的管道天然氣標準標稱工作壓力是多少？",
         {"A": "21 millibar (21 mbar / approx 210 mm water gauge)", "B": "10 bar", "C": "0.1 mbar", "D": "1,000 bar"},
         {"A": "21 毫巴 (21 mbar，約合 210 毫米水柱高度水壓)", "B": "10 bar 高壓", "C": "0.1 mbar 微壓", "D": "1,000 bar 超高壓"},
         "A", "The UK low-pressure gas network delivers gas to the domestic meter at 21 mbar (±2 mbar). Permissible pressure drop across internal pipework to appliances is strictly limited to 1 mbar.", "家用天然氣標準工作水壓：表後調壓器默認恆定輸出 21 mbar（毫巴）。法規嚴格規定：從燃氣表一路走到最遠的壁掛爐或燃氣灶，沿程管道摩擦阻力壓降嚴禁超過 1 mbar（設備前至少保證 20 mbar）！", "BS 6891; Gas Safety (Installation and Use) Regulations 1998"),

        ("10.1",
         "Under British Standards BS 6891, what is the MAXIMUM permissible operating pressure drop between the gas meter outlet and any connected gas appliance running at full rate?",
         "根據英國標準 BS 6891，當燃氣用具在全負荷滿負荷點火燃燒時，從燃氣表出口到任何連接用具之間的「管道最大允許運行壓力降（Pressure Drop）」極限是多少？",
         {"A": "Maximum 1.0 millibar (1.0 mbar) pressure drop", "B": "Maximum 10 mbar", "C": "Maximum 100 mbar", "D": "Zero drop allowed at all times"},
         {"A": "最大不超過 1.0 毫巴 (1.0 mbar) 壓力降", "B": "最大允許 10 mbar 壓降", "C": "最大允許 100 mbar 壓降", "D": "在任何時候絕對不允許有任何微小壓降"},
         "A", "BS 6891 mandates that gas pipework sizing must ensure no more than a 1 mbar drop between the meter (21 mbar) and the appliance inlet (min 20 mbar) under full simultaneous firing demand.", "燃氣壓降 1 mbar 紅線必考：為什麼管徑要算得準？如果管子太細（如全走 15mm 細銅管），壁掛爐滿負荷大火一開，管道摩擦阻力過大，爐前水壓瞬間跌破 19 mbar 甚至熄火！表到爐子全程壓降嚴禁超 1 mbar！", "BS 6891 Section 6; Gas Safe Technical Handbook"),

        ("10.1",
         "What is the chemical formula and relative density of commercial Propane LPG (stored in red cylinders or bulk outdoor tanks)?",
         "存放在紅色鋼瓶或室外散裝大儲罐中的「商業丙烷液化石油氣 (Propane LPG)」，其化學式及相對於空氣的相對密度是多少？",
         {"A": "C3H8, relative density approx 1.5 (significantly heavier than air, sinks and collects at ground level)", "B": "CH4, relative density 0.6", "C": "CO2, relative density 0.1", "D": "H2O, relative density 1.0"},
         {"A": "C3H8 (丙烷)，相對密度約為 1.5 (顯著比空氣重，泄漏時迅速下沉並在地面凹坑積聚)", "B": "CH4，相對密度為 0.6", "C": "CO2，相對密度為 0.1", "D": "H2O，相對密度為 1.0"},
         "A", "Commercial Propane is C3H8. With a relative density of ~1.5, leaking LPG is heavier than air. It flows like invisible water across floors and pools dangerously in cellars, drains, and trenches.", "丙烷 LPG 沉底致命特性：丙烷分子式 C3H8，比空氣重一半（比重 1.5）！一旦漏氣，它不像天然氣往上飄，而是像水一樣貼著地面流淌，灌滿地下室、排水溝和電纜溝，一旦遇到火花就是毀滅性大爆炸！", "UKLPG Code of Practice 1; BS 5482-1; C&G Unit 207"),

        ("10.1",
         "What is the boiling point of commercial Propane at atmospheric pressure, and why is it preferred over Butane for outdoor winter storage in the UK?",
         "在標準大氣壓下，商業丙烷的沸點是多少？為什麼在英國寒冬室外，丙烷被絕對優先選用、而丁烷卻無法使用？",
         {"A": "Boiling point approx -42°C (it gasifies reliably even in sub-zero freezing winter conditions down to -40°C)", "B": "Boiling point +100°C", "C": "Boiling point 0°C", "D": "Boiling point +50°C"},
         {"A": "沸點約為 -42°C (即使在英國零下極寒冰凍低溫下，瓶內液體依然能可靠自發沸騰汽化為氣體供應燃燒)", "B": "沸點為 +100°C", "C": "沸點為 0°C", "D": "沸點為 +50°C"},
         "A", "Propane boils at -42°C, meaning it vaporizes easily into gas outdoors in deep UK winters. Butane boils at -0.5°C; below freezing, liquid butane ceases vaporizing, cutting off gas completely.", "丙烷耐低溫真理：丙烷沸點低達 -42°C，外面下鵝毛大雪零下十度，罐子裡的丙烷依然像開水一樣咕嚕咕嚕沸騰產氣；而丁烷沸點只有 -0.5°C，冬天擺在室外直接凍成死水不產氣！室外儲罐一律用丙烷！", "UKLPG CoP 1; C&G Unit 207 Domestic Gas Principles"),

        ("10.1",
         "What is the standard operating pressure for domestic commercial Propane gas supply systems in the UK?",
         "在英國家庭與商用丙烷（Propane）液化氣供氣系統中，調壓閥輸出的標準標稱工作壓力是多少？",
         {"A": "37 millibar (37 mbar)", "B": "21 millibar", "C": "28 millibar", "D": "200 bar"},
         {"A": "37 毫巴 (37 mbar)", "B": "21 毫巴", "C": "28 毫巴", "D": "200 bar"},
         "A", "Propane appliances operate at 37 mbar (compared to 28 mbar for Butane and 21 mbar for Natural Gas). Regulators for propane cylinders are colour-coded red with screw-on left-hand POL threads.", "燃氣壓力速記：管道天然氣用 21 mbar；室內藍瓶丁烷用 28 mbar；室外紅瓶丙烷用 37 mbar！三種燃氣壓力和噴嘴孔徑完全不同，絕對不能混用！", "BS EN 12864 Low pressure non-adjustable regulators; UKLPG Code 1"),

        ("10.1",
         "Why do cylinder valves and regulator fittings for combustible fuel gases like Propane feature LEFT-HAND threads (POL fittings)?",
         "為什麼在可燃燃料氣體（如丙烷 LPG）的鋼瓶閥門與減壓閥連接管件螺紋上，強制採用「反扣 / 左旋螺紋 (Left-Hand Thread)」設計？",
         {"A": "To make them look antique", "B": "As a critical fail-safe fool-proofing safety mechanism to physically prevent combustible gas fittings from being accidentally cross-connected into oxygen or inert gas equipment", "C": "Because right-hand threads are illegal", "D": "To screw in faster"},
         {"A": "使管件看起來更具古典機械美感", "B": "作為至關重要的防呆防錯安全防護機制：從物理結構上徹底杜絕可燃氣體配件被誤插誤擰到氧氣、壓縮空氣或惰性氣體管路上引發火災爆炸", "C": "因為英國法律禁止製造右旋螺紋", "D": "為了讓水暖工擰螺紋時速度更快"},
         "B", "Left-hand threads (marked with notched nuts) physically prevent dangerous cross-connections. Fuel gas hoses cannot be screwed onto oxygen torches or inert regulators, eliminating accidental explosion risks.", "反扣螺紋救命防呆：凡是易燃可燃氣體（乙炔、丙烷），接頭螺母上全開有防偽刻槽，且全是「反時針向左擰緊」的反扣！這樣一來，工人在現場就算閉著眼睛，也絕對不可能把易燃氣瓶接上氧氣表引起爆炸！", "BS 341 Transportable gas container valves; BCGA Code of Practice"),

        ("10.1",
         "Why is it STRICTLY ILLEGAL to site an LPG cylinder or LPG appliance in an underground cellar, basement, or sunken lightwell?",
         "為什麼法律絕對嚴禁將液化石油氣鋼瓶（LPG）或 LPG 燃氣用具安裝在「地下室、半地下地窖或下沉式天井」中？",
         {"A": "LPG bottles rust underground", "B": "Because LPG is heavier than air (density 1.5 to 2.0); any leak will sink by gravity into the basement, cannot dissipate naturally, and will accumulate into a massive explosive air-fuel bomb", "C": "Rats eat LPG bottles", "D": "Basements have too much natural light"},
         {"A": "液化氣鋼瓶在地下潮濕環境下極易生鏽", "B": "因為 LPG 比空氣重得多（密度 1.5 至 2.0）；一旦發生任何微小洩漏，氣體會在重力下像流水一樣順著樓梯沉底積聚在地下室底層，根本無法自然排走，隨時被電燈開關電火花引發毀滅性大爆炸！", "C": "老鼠會咬穿鋼製液化氣瓶壁", "D": "地下室光線過於充足影響氣體質量"},
         "B", "LPG pools in low areas like liquid. Basement installations have no natural gravity escape route for heavy gas. An electrical spark from a light switch or freezer motor detonates the pooled gas.", "地下室禁止 LPG 鐵律：天然氣輕飄飄從窗戶走了，而液化氣像水銀一樣往坑裡鑽！地下室是個密封大坑，氣體沉在腳底越積越厚，全家毫無察覺。一開燈或者冰箱壓縮機打個電火花，整個房子瞬間被炸平！", "Gas Safety (Installation and Use) Regulations 1998 Regulation 30; UKLPG Code 1"),

        ("10.1",
         "What foul-smelling chemical odorant is artificially injected into odorless Natural Gas and LPG so that leaks can be immediately detected by human smell at concentrations far below the lower explosive limit?",
         "在本身無色無味的天然氣與液化石油氣中，人為強制注入了何種具有刺鼻惡臭的大蒜/臭雞蛋味「化學加臭劑」，以便人體嗅覺在濃度遠低於爆炸下限前就能立刻察覺漏氣？",
         {"A": "Perfumed lavender oil", "B": "Mercaptans (such as Ethyl Mercaptan or Tert-Butyl Mercaptan / THT)", "C": "Pure gasoline", "D": "Bleach disinfectant"},
         {"A": "芬芳的薰衣草精油", "B": "硫醇類化合物（如乙硫醇 Ethyl Mercaptan 或叔丁基硫醇 THT）", "C": "高辛烷值汽油", "D": "含氯消毒漂白水"},
         "B", "Pure hydrocarbons have zero smell. Mercaptans impart a pungent, unpleasant sulfurous odor (detectable at <1% gas concentration), ensuring occupants smell leaks before gas reaches the lower explosive limit (5%).", "加臭劑嗅覺警報：純天然氣就像純淨水一樣沒有任何味道！幾千立方漏滿屋子你也聞不到。加了微量的硫醇，只要空氣裡有 0.5% 的微漏，人立刻聞到濃烈刺鼻的爛洋蔥臭雞蛋味，第一時間逃生報警！", "BS EN ISO 13734 Natural gas - Organic sulfur compounds; C&G Unit 207"),

        # 10.2 Combustion Chemistry, Flues & Approved Document J
        ("10.2",
         "What are the non-toxic chemical products of COMPLETE combustion when a hydrocarbon fuel gas (Methane) burns with a stoichiometric supply of fresh air/oxygen?",
         "當烴類燃料氣體（甲烷 CH4）在充足的新鮮助燃空氣/氧氣中實現「完全燃燒 (Complete Combustion)」時，化學反應生成的無毒產物是什麼？",
         {"A": "Carbon Monoxide and pure sulfur", "B": "Carbon Dioxide (CO2), Water Vapour (H2O), and Heat energy (CH4 + 2O2 → CO2 + 2H2O + Heat)", "C": "Solid soot and black smoke", "D": "Hydrogen cyanide gas"},
         {"A": "劇毒一氧化碳與純固體硫磺", "B": "二氧化碳 (CO2)、水蒸氣 (H2O) 以及釋放出的熱能（反應式：CH4 + 2O2 → CO2 + 2H2O + 熱能）", "C": "固體碳黑粉塵與滾滾黑煙", "D": "劇毒氰化氫氣體"},
         "B", "Complete combustion: CH4 + 2O2 → CO2 + 2H2O. Adequate oxygen oxidizes all carbon to CO2 and all hydrogen to water vapor. The flame is crisp, stable, and translucent blue.", "完全燃燒化學方程式必考：CH4 + 2O2 → CO2 + 2H2O + 熱量！只要氧氣餵得飽，燃燒產物只有溫室氣體二氧化碳和水蒸氣。火焰呈現清澈、緊湊、安靜的亮藍色，熱效率最高且絕不釋放一氧化碳！", "BS 5440-2; Approved Document J; C&G Unit 207 Heating Science"),

        ("10.2",
         "What dangerous toxic gas and visible physical byproducts are produced during INCOMPLETE combustion of gas due to severe lack of combustion air or dirty, blocked burners?",
         "當燃氣燃燒因進風量嚴重匱乏、或燃燒器噴嘴髒堵結碳導致「不完全燃燒 (Incomplete Combustion)」時，會劇烈釋放出何種致命劇毒氣體與可見副產物？",
         {"A": "Carbon Monoxide (CO), free unburned Carbon soot particles, aldehydes, and yellowish floppy flames", "B": "Liquid oxygen and ice", "C": "Pure gold dust", "D": "Water only"},
         {"A": "劇毒一氧化碳 (CO)、游離未燃燒碳黑顆粒（Soot 煙灰）、刺激性醛類物質，且火焰呈現無力飄忽的黃色/橘色軟火", "B": "液態氧氣與冰塊", "C": "純金金粉", "D": "純淨的蒸餾水"},
         "A", "Incomplete combustion occurs when oxygen is restricted: 2CH4 + 3O2 → 2CO + 4H2O. Carbon monoxide (deadly poison) is generated alongside yellow lazy flames and black carbon soot deposits.", "不完全燃燒的死亡詛咒：空氣不夠時，碳原子無法氧化成 CO2，被腰斬成致命的「一氧化碳（CO）」！同時伴隨大量未燃燒碳黑（黑煙灰把換熱器糊死）。火焰呈現飄忽無力、呼噠呼噠發黃發橙的病態特徵！", "BS 5440-2; Approved Document J Section 1; C&G Unit 207"),

        ("10.2",
         "Why is Carbon Monoxide (CO) physiologically lethal to human beings at microscopic concentrations in breathable air?",
         "為什麼一氧化碳（CO）氣體即使在空氣中僅有微量濃度，也會對人體生理造成迅速致命的中毒死亡？",
         {"A": "It freezes human skin instantly", "B": "CO binds to hemoglobin in red blood cells with approximately 200 times the chemical affinity of oxygen, forming Carboxyhemoglobin (COHb) and starving the brain and vital organs of oxygen", "C": "It breaks human bones", "D": "It dissolves human teeth"},
         {"A": "它能瞬間凍傷人體皮膚表皮", "B": "一氧化碳與人體紅細胞中血紅蛋白的結合親和力比氧氣「高達約 200 倍」，搶先奪走血紅蛋白生成高濃度的碳氧血紅蛋白 (COHb)，切斷大腦與全身重要器官的氧氣輸送造成內窒息死亡", "C": "它能瞬間折斷人體骨骼", "D": "它能迅速溶解人體牙齒"},
         "B", "Hemoglobin has a fatal affinity for CO (~200x greater than O2). Breathing just 0.1% (1000 ppm) CO creates lethal COHb levels within an hour, causing irreversible brain death without coughing.", "隱形殺手 CO 奪命醫學原理：一氧化碳是個搶座霸王！它搶血紅蛋白的速度比氧氣快 200 倍！一旦吸入，紅細胞全部被 CO 霸佔再也運不了氧氣。人體大腦在不知不覺中缺氧壞死，頭暈嗜睡，隨後在睡夢中無聲無息死亡！", "Health and Safety Executive (HSE) CO Safety Guidance; Approved Document J"),

        ("10.2",
         "Under British Standards BS EN 50291 and Approved Document J, where is a Carbon Monoxide (CO) Alarm legally mandated to be fitted in domestic dwellings?",
         "根據英國/歐洲標準 BS EN 50291 及建築法規 Approved Document J 規定，家庭住宅中的「一氧化碳報警器 (CO Alarm)」必須被法律強制安裝在何種位置？",
         {"A": "Inside the garden shed only", "B": "In any room containing a fixed combustion appliance (gas boiler, gas fire, oil boiler, or wood-burning stove), sited between 1m and 3m horizontally from the appliance", "C": "Under water in the fish pond", "D": "Inside the kitchen refrigerator"},
         {"A": "僅允許安裝在花園工具木棚內", "B": "在任何安裝有固定燃燒用具（如燃氣壁掛爐、燃氣壁爐、燃油鍋爐、或燃木爐灶）的房間內，且與用具保持 1 米至 3 米的水平合理距離", "C": "浸泡在觀賞魚池的水底", "D": "放置在廚房電冰箱內部"},
         "B", "Building Regs Part J requires an audible BS EN 50291 CO alarm in every room housing a combustion appliance. Wall-mounted alarms should sit above window/door heads, 1-3m horizontally from the appliance.", "一氧化碳報警器法定安裝規則：凡是燒火的地方（燃氣爐、燃木壁爐），必須裝通過 BS EN 50291 認證的報警器！裝在牆上時要高於門窗上沿、距離壁掛爐水平 1 到 3 米。英國租賃法規規定房東沒裝一律違法重罰！", "Building Regulations Approved Document J Section 2; BS EN 50291"),

        ("10.2",
         "What is the operational distinction between an 'Open-Flued' appliance and a 'Room-Sealed' (Balanced Flue) appliance under Approved Document J?",
         "根據建築法規 Approved Document J，老式「開式排煙用具 (Open-Flued)」與現代主流「房間密封式/平衡式排煙用具 (Room-Sealed)」有何本質的空氣隔離區別？",
         {"A": "Open-flued appliances burn coal only", "B": "Open-flued appliances draw combustion air directly from the living room and rely on chimney thermal stack effect, whereas room-sealed appliances draw 100% of combustion air from outdoors via a sealed concentric duct", "C": "Room-sealed appliances have no chimney", "D": "Open-flued appliances require electricity"},
         {"A": "開式煙道用具只能用來燃燒煤炭", "B": "開式排煙用具直接從「室內生活房間內吸取氧氣助燃」，依賴自然煙囪抽力排煙；而房間密封用具則通過雙層同軸密閉管道「100% 完全從室外吸入新鮮空氣並排向室外」", "C": "房間密封用具完全沒有任何排煙管道", "D": "開式用具必須依靠高壓電驅動"},
         "B", "Open-flued appliances consume room air, risking CO spillback if kitchen extract fans create room negative pressure. Room-sealed appliances are 100% isolated from room air, guaranteeing absolute indoor safety.", "開式與密閉式生死對決：老式開式爐子天天跟人搶屋裡氧氣，廚房抽油煙機一開甚至會把煙囪廢氣倒抽回客廳！現代房間密封（Room-Sealed）是管中管，吸氣排氣全在室外閉環循環，屋內哪怕門窗全封死也絕對零風險！", "Approved Document J Section 1; BS 5440-1; C&G Unit 207"),

        ("10.2",
         "Under BS 5440-1, what safety accessory must be fitted over an external horizontal fan-flued boiler terminal if it is positioned less than 2.0 meters above ground level?",
         "根據英國排煙標準 BS 5440-1，若燃氣壁掛爐的室外水平強制排煙煙道終端口、安裝在距離室外地面「小於 2.0 米的高度」時，排煙口外部必須強制加裝何種金屬防護配件？",
         {"A": "A decorative bird nest", "B": "A heavy-duty galvanised wire Terminal Guard securely fixed over the terminal", "C": "A wooden plank glued to the wall", "D": "A plastic trash bag"},
         {"A": "裝飾性小鳥木質巢穴", "B": "經過牢固膨脹螺栓錨固的重型熱鍍鋅金屬防護金屬網罩 (Terminal Guard)", "C": "用膠水粘在外牆上的薄木板", "D": "黑色塑料垃圾袋"},
         "B", "Terminals below 2.0m are accessible to children and pedestrians. The exhaust reaches high temperatures (>60°C). A terminal guard prevents contact burns and stops objects being stuffed into the flue.", "煙道防護罩 2 米紅線必考：煙道口排出的高溫廢氣足足六七十度！如果裝在離地 2 米以下（人手摸得到、小孩打球碰得到的高度），必須用四顆螺絲死死釘上鍍鋅鐵絲網罩！既防止路人燙傷，又防止頑童往煙管塞網球！", "BS 5440-1:2008 Section 8; Gas Safe Register Guidance"),

        # 10.3 Oil Fired Systems & Storage Tanks (BS 5410)
        ("10.3",
         "Under British Standards BS 2869, what class of liquid fuel oil is universally specified for domestic domestic vaporizing and pressure-jet central heating boilers in the UK?",
         "根據英國燃料油標準 BS 2869，在全英無天然氣管網覆蓋的農村家庭中，家用壓力噴霧式燃油壁掛爐普遍指定的標準燃油型號是什麼？",
         {"A": "Heavy crude bitumen", "B": "Class C2 Kerosene (commonly known as 28-second burning oil)", "C": "Class D Gas Oil (35-second red diesel)", "D": "Pure refined aviation jet fuel"},
         {"A": "未加工的重質原油瀝青", "B": "Class C2 煤油 (Kerosene，業內俗稱 28 秒燃燒油)", "C": "Class D 瓦斯油 (35 秒紅色農用柴油)", "D": "純航空高辛烷值噴氣燃油"},
         "B", "UK domestic oil boilers burn Class C2 Kerosene (28-sec oil). It is cleaner-burning and lower viscosity than Class D Gas Oil (red diesel), which is reserved for commercial or agricultural heaters.", "家用燃油常識：英國農村幾百萬戶家庭不通天然氣，全燒煤油（Kerosene C2，俗稱 28 秒油）！它黏度極低、燃燒極其乾淨無積碳；而 35 秒柴油（Class D 紅柴油）黏度大、煙大，只給工廠拖拉機使用。", "BS 2869 Fuel oils for agricultural, domestic and industrial engines and boilers; C&G Unit 207"),

        ("10.3",
         "Under the Control of Pollution (Oil Storage) Regulations and BS 5410-1, what is an 'Integrally Bunded Oil Storage Tank' installed at domestic properties?",
         "根據英國防污染法規（油類儲存）與 BS 5410-1 標準，家用「一體化雙層防溢防護油罐 (Bunded Oil Tank)」具有何種雙層外殼安全構造？",
         {"A": "A single-layer plastic bottle", "B": "A tank-within-a-tank construction where the secondary outer containment wall has at least 110% storage capacity of the inner fuel tank, capturing any leaks or spillage", "C": "A tank buried 50 meters under rock", "D": "A tank made of open timber slats"},
         {"A": "單層薄壁塑料大桶", "B": "「罐中罐」雙層安全構造：外層二級防護容納外殼的容積「至少達到內部主油箱容積的 110% 以上」，能 100% 兜住內部油箱破裂、穿刺或溢流出的全部燃油", "C": "深埋在岩石下方 50 米處的油罐", "D": "由敞開式木條拼接而成的油箱"},
         "B", "A bunded tank provides a catchment reservoir holding 110% of the inner tank volume. If the inner vessel cracks, fuel spills safely into the interstitial outer chamber without contaminating local soil or aquifers.", "雙層防溢油箱（Bunded Tank）環保鐵律：煤油一旦漏進花園土壤，會順著地下水毒死整片地下水源，環境署治理罰款高達幾十萬鎊！雙層油箱外層是個大套盆（容量是內膽 110%），內膽破了外盆穩穩接住，滴油不漏！", "BS 5410-1 Code of practice for oil firing installations; OFTEC Technical Book 3"),

        ("10.3",
         "Under Approved Document J and OFTEC standards, what is the MINIMUM fire-separation clearance distance required between an external domestic oil tank and a non-fire-rated building boundary or timber fence?",
         "根據英國建築法規 Approved Document J 與 OFTEC（燃油工程技術協會）標準，室外家用儲油罐距離「非耐火建築邊界、木柵欄籬笆」的法定最小防火隔離間距是多少？",
         {"A": "Minimum 760mm clearance (unless a 30-minute fire barrier wall is constructed)", "B": "Zero mm (touching the wooden fence)", "C": "100 meters", "D": "10mm"},
         {"A": "至少 760mm (0.76 米) 安全防火間距 (除非在油罐與籬笆之間砌築一道耐火極限不低於 30 分鐘的實心防火隔牆)", "B": "0 mm (緊貼木質花園籬笆安裝)", "C": "100 米超大間距", "D": "10mm"},
         "A", "BS 5410-1 mandates at least 760mm clearance from combustible boundaries/fences to prevent garden fires spreading to the oil tank. If closer than 760mm, a 30-minute fire-rated wall must shield the tank.", "油罐籬笆 760mm 防火紅線：隔壁花園鄰居烤肉失火常燒焦木籬笆！儲油罐若挨著籬笆放，高溫會引爆幾千升煤油！法規強制要求油罐離木柵欄至少 760mm；若花園太小非要挨著放，必須砌一道 30 分鐘耐火磚牆！", "BS 5410-1 Section 8; OFTEC Technical Information TI/136; Approved Document J"),

        ("10.3",
         "Under BS 5410-1, what is the minimum clearance distance between a domestic oil storage tank and an external building wall with NON-FIRE-RATED openings (e.g. windows, doors, boiler flues, or eaves)?",
         "根據 BS 5410-1 規定，家用儲油罐距離建築外牆上「非耐火門窗孔洞、可開啟窗戶或屋簷簷口」的最小法定安全間距是多少？",
         {"A": "Minimum 1.8 meters clearance", "B": "Minimum 50 meters", "C": "Directly under the bedroom window (zero mm)", "D": "50mm"},
         {"A": "至少 1.8 米 (1.8m) 安全間距", "B": "至少 50 米", "C": "直接安裝在臥室窗戶正下方 (0 mm)", "D": "50mm"},
         "A", "The tank must be at least 1.8m from unrated windows, doors, or openable vents. In a fire, flames venting from windows would otherwise directly engulf the tank, driving catastrophic BLEVE explosions.", "油罐窗戶 1.8 米生死間距：屋裡失火玻璃炸碎，火舌會從窗戶瘋狂向外噴！若油罐離窗戶太近（<1.8m），烈火直接炙烤油罐引發毀滅性大爆炸！油罐必須遠離所有非防火門窗、屋簷至少 1.8 米！", "BS 5410-1 Table 1; Approved Document J Section 4"),

        ("10.3",
         "What is the mechanical function of an external 'Remote-Acting Fire Valve' (such as a Teddington capillary fire valve) installed on the oil fuel supply line where it enters a property?",
         "安裝在進戶燃油供油管道穿牆入戶處的「外裝遠程毛細管式機械防火切斷閥 (Remote Acting Fire Valve)」，具有何種關鍵的火災應急防護功能？",
         {"A": "It pumps water onto the roof", "B": "Its sensor phial installed inside the boiler casing detects fire (tripping at 65°C to 85°C); the melting liquid/wax triggers a spring-loaded brass valve OUTSIDE the building, shutting off oil flow before it reaches the blaze", "C": "It sounds a musical alarm", "D": "It filters water out of oil"},
         {"A": "向建築屋頂自動抽水噴淋", "B": "其安裝在鍋爐內部的溫感探頭在感知到火災異常高溫時（65°C 至 85°C 觸發），利用毛細管液壓釋放，自動擊發位於「室外建築外牆處」的高強度機械彈簧切斷閥，在燃油進入火場前從源頭死死掐斷供油！", "C": "演奏悅耳的音樂報警聲", "D": "過濾燃油中的微量水分"},
         "B", "If a boiler catches fire, the internal sensor trips. A high-tensile spring snaps the valve shut on the external wall, cutting the fuel supply outside so burning oil cannot feed the house fire.", "防火切斷閥（Fire Valve）救命構造：細銅管把室外閥門和鍋爐肚子連在一起。鍋爐一旦起火燒到 65-85°C，感溫包液體膨脹激發卡扣，室外的機械閥門「啪」一聲彈簧擊發死死鎖死供油管！在室外斷油，火勢瞬間熄滅！", "BS 5410-1 Section 9; OFTEC Technical Information TI/138"),

        # 10.4 Gas Statutory Regulations & Gas Safe Register
        ("10.4",
         "Under UK Law, what statutory regulation governs all installation, maintenance, and servicing of domestic and commercial gas fittings?",
         "在英國現行法律體系中，法定監管所有家庭與商用燃氣用具安裝、維護與檢修的最高法律規範是什麼？",
         {"A": "The Road Traffic Act 1988", "B": "The Gas Safety (Installation and Use) Regulations 1998 (commonly referred to as GSIUR 1998)", "C": "The Food Safety Act 1990", "D": "The Animal Welfare Act 2006"},
         {"A": "1988 年英國道路交通安全法", "B": "1998 年燃氣安全（安裝與使用）法規 (Gas Safety (Installation and Use) Regulations 1998，簡稱 GSIUR 1998)", "C": "1990 年食品衛生安全法", "D": "2006 年動物福利保護法"},
         "B", "GSIUR 1998 is the overarching criminal statute enforcing gas safety across Great Britain. Breaching GSIUR (such as working on gas appliances without Gas Safe registration) carries severe unlimited fines and imprisonment.", "英國燃氣天條 GSIUR 1998：英國所有跟煤氣打交道的活，全歸《1998 燃氣安全法規》死死管轄！無證動煤氣、裝壁掛爐不合規，在英國屬於嚴重刑事犯罪，一經起訴罰款無上限直接坐牢入獄！", "Health and Safety at Work etc. Act 1974; Gas Safety (Installation and Use) Regs 1998"),

        ("10.4",
         "Under Regulation 3 of GSIUR 1998, what registration is LEGALLY MANDATORY for any business or self-employed plumber working on gas appliances or gas pipework in Great Britain?",
         "根據 GSIUR 1998 第 3 條規定，在英國境內從事任何燃氣管道、燃氣壁掛爐等燃氣用具施工的企業或個體水暖工，法律強制要求必須持有何種官方註冊資格？",
         {"A": "Driver and Vehicle Licensing Agency (DVLA)", "B": "Gas Safe Register (having passed ACS competency assessments and holding a valid Gas Safe ID card with appropriate appliance categories)", "C": "Royal Automobile Club (RAC)", "D": "National Trust membership"},
         {"A": "英國機動車駕駛與車輛牌照局（DVLA）駕照", "B": "英國燃氣安全註冊局官方認證 (Gas Safe Register - 必須通過 ACS 全國燃氣資質考核，並持有在有效期內標明具體用具准入類別的 Gas Safe 執業胸卡)", "C": "皇家汽車俱樂部（RAC）會員卡", "D": "英國國家名勝古蹟信託會員卡"},
         "B", "Gas Safe Register is the official gas registration body (replacing CORGI in 2009). Working on gas for hire or reward without active Gas Safe registration is a strict criminal offence in the UK.", "Gas Safe 唯一合法燃氣執照：2009 年全面取代老 CORGI。任何水暖工只要碰燃氣管、摸壁掛爐，必須佩戴這張帶二維碼的黃色磁卡！每 5 年必須重考 ACS 資格，無證動煤氣必被 HSE 抓去法庭坐牢！", "Gas Safety (Installation and Use) Regulations 1998 Reg 3(1); Gas Safe Register Rules"),

        ("10.4",
         "Under Regulation 36 of GSIUR 1998, what is a landlord's strict statutory obligation regarding gas safety in rented residential accommodation?",
         "根據 GSIUR 1998 第 36 條規定，英國各類民居出租房房東對出租物業內的燃氣安全負有何種法定義務？",
         {"A": "Landlords are exempt from gas safety", "B": "Must have an annual gas safety check completed by a Gas Safe engineer for every appliance/flue, obtain a Landlord Gas Safety Record (LGSR / CP12), and provide a copy to existing tenants within 28 days (and to new tenants before move-in)", "C": "Paint the boiler every year", "D": "Turn off gas permanently"},
         {"A": "房東完全豁免於任何燃氣安全監管責任", "B": "必須聘請 Gas Safe 註冊工程師每年對屋內所有燃氣用具及煙道實施一次法定年檢，取得「房東燃氣安全檢驗合格證書 (LGSR / CP12)」，並在 28 天內將副本送達現有租客（新租客入住前必須出示）", "C": "每年把壁掛爐外殼油漆粉刷一遍", "D": "永久切斷出租房的天然氣供應"},
         "B", "Regulation 36 mandates annual safety checks (CP12 certificates). Landlords failing to produce CP12s cannot legally serve Section 21 eviction notices and face hefty criminal prosecution.", "房東 CP12 燃氣安全年檢鐵律：英國租房法規極其嚴格！房東每年必須花錢請燃氣工程師做氣密、煙氣分析檢查，簽發 CP12 證書。新租客進門第一天必須看這張紙，沒給證書房東連驅逐不良租客的權利都沒有！", "Gas Safety (Installation and Use) Regulations 1998 Regulation 36; Landlord and Tenant Act"),

        ("10.4",
         "Under BS 6891, what is the maximum permissible pressure drop when conducting a 2-minute Gas Tightness (Soundness) Test on a NEW domestic gas installation at 20 mbar test pressure?",
         "根據 BS 6891 標準，在對一套「全新安裝的家庭燃氣管網」進行 20 mbar 測試壓力的 2 分鐘氣密性打壓試驗（Tightness Test）時，允許的「最大壓力降」是多少？",
         {"A": "ZERO pressure drop (0 mbar) - not even the slightest movement on the water manometer is legally permitted on new pipework", "B": "Drop of 10 mbar", "C": "Drop of 5 mbar", "D": "Drop of 50 mbar"},
         {"A": "絕對零壓降 (0 mbar) - 水柱壓力計在整整 2 分鐘內絕對不允許有哪怕半毫米的絲毫微小下降！", "B": "允許下降 10 mbar", "C": "允許下降 5 mbar", "D": "允許下降 50 mbar"},
         "A", "For new gas pipework, the pass standard is absolute zero pressure drop over the 2-minute test period. Any drop indicates an active combustible gas leak that must be traced and rectified immediately.", "新裝燃氣管零容忍（0 壓降）：水柱打到 20 mbar，等 1 分鐘讓管內氣溫穩定；隨後拿秒表精確計時 2 分鐘！新管道必須是絕對 100% 氣密，水柱只要稍微動彈一丁點，立刻判為不合格，必須刷肥皂水查漏！", "BS 6891 Specification for the installation and maintenance of low pressure gas pipework; IGEM/UP/1B"),

        ("10.4",
         "Where is the domestic Emergency Control Valve (ECV) fitted, and what must a consumer or plumber do if an uncontrollable gas leak is detected?",
         "家庭「燃氣緊急切斷總閥 (Emergency Control Valve - ECV)」安裝在何處？當室內聞到嚴重燃氣洩漏且無法控制時，用戶或技師必須採取的標準應急行動是什麼？",
         {"A": "Turn on all electric lights to see the gas", "B": "The ECV is located immediately upstream of the gas meter; turn the handle 90 degrees across the pipe to OFF, extinguish naked flames, open all doors/windows, do NOT operate electrical switches, evacuate, and call the National Gas Emergency Service (0800 111 999)", "C": "Light a candle to burn the leak", "D": "Pour water into the gas meter"},
         {"A": "打開全屋所有電燈開關以照亮並觀察氣體洩漏點", "B": "ECV 緊靠安裝在燃氣表進口上游管道上；迅速將手柄旋轉 90 度與管道垂直切換至 OFF 關閉、熄滅所有明火、徹底開門開窗通風、嚴禁扳動任何室內電器電燈開關、全員撤離到室外並立即撥打英國國家燃氣應急熱線 (0800 111 999)！", "C": "點燃一支蠟燭試圖燒光洩漏氣體", "D": "向燃氣表內部注入自來水"},
         "B", "The handle turns quarter-turn to isolate. Flips, doorbells, or mobile phones can spark an explosion. Evacuating immediately and dialling 0800 111 999 dispatches emergency first responders within 1 hour.", "煤氣洩漏救命六步口訣：1. 關表前總閥（扳轉 90 度橫過水管）；2. 掐滅明火；3. 大開門窗通風；4. 絕對嚴禁碰任何電燈開關、門鈴甚至在屋裡打電話（火花能引爆全屋）；5. 全員撤出屋外；6. 撥打 0800 111 999！", "Gas Safety (Installation and Use) Regs 1998; National Gas Emergency Service Standards"),

        # 10.5 Renewable Technologies: Solar Thermal & Heat Pumps
        ("10.5",
         "In domestic Solar Thermal hot water installations, what is the engineering difference in solar absorption efficiency between a 'Flat Plate Collector' and an 'Evacuated Tube Collector'?",
         "在家庭太陽能熱水系統中，「平板型太陽能集熱器 (Flat Plate)」與「真空玻璃管型集熱器 (Evacuated Tube)」在集熱吸熱效率上有何本質工程差異？",
         {"A": "Flat plates are made of paper", "B": "Evacuated tubes eliminate convective and conductive heat loss via a vacuum envelope surrounding heat pipes, maintaining high solar collection efficiency even in freezing ambient temperatures and overcast UK winter skies", "C": "Flat plates generate nuclear power", "D": "Evacuated tubes freeze in summer"},
         {"A": "平板集熱器是由厚吸水紙板製成的", "B": "真空管集熱器利用雙層玻璃管內部的「高真空絕熱層」徹底阻斷了熱傳導與熱對流散失，在嚴寒冰凍低溫以及英國陰天散射光照條件下，依然能保持極高的集熱轉化效率", "C": "平板集熱器能自發產生核裂變發電", "D": "真空管在炎熱夏天會自發結冰"},
         "B", "Evacuated tubes act like a thermos flask. The internal vacuum prevents heat radiating back to cold outdoor air, delivering far higher winter efficiency than glazed flat panels.", "真空管吸熱黑科技：就像保溫瓶內膽一樣！雙層玻璃中間抽成絕對真空，吸了熱量根本散不出去。即使外面大雪紛飛零下五度、天空陰沉，真空管裡依然能燒出五六十度的熱水，極其適合英國多陰雨氣候！", "BS EN 12975 Thermal solar systems and components; C&G Unit ENV"),

        ("10.5",
         "Why must domestic Solar Thermal closed-loop primary collector circuits be filled with a specialist Propylene Glycol anti-freeze solution rather than plain water or automotive Ethylene Glycol?",
         "為什麼家用太陽能熱水封閉循環迴路中，必須灌注專用的「食品級丙二醇防凍熱媒液 (Propylene Glycol)」，而絕對嚴禁直接加純水或汽車專用乙二醇防凍液？",
         {"A": "Propylene glycol makes water sparkle", "B": "Propylene glycol protects solar collectors from sub-zero freezing down to -25°C while being non-toxic (safe if a coil pinhole leak cross-contaminates domestic drinking water), unlike lethal toxic ethylene glycol", "C": "Plain water explodes in sunlight", "D": "Ethylene glycol cools the sun"},
         {"A": "丙二醇能讓自來水自發閃爍發光", "B": "丙二醇能為室外集熱板提供深達 -25°C 的超強防凍保護，且屬於「無毒食品級安全配方」（萬一水罐盤管發生砂眼穿孔內漏，絕不會因毒死飲用水而致命），杜絕了汽車乙二醇劇毒致死慘劇", "C": "純水在陽光照射下會劇烈爆炸", "D": "乙二醇能反向為太陽降溫"},
         "B", "Automotive antifreeze (ethylene glycol) is a lethal poison. Solar thermal circuits interface directly with domestic drinking water cylinders. Using non-toxic propylene glycol guarantees safety during heat exchanger failure.", "太陽能導熱油食品級安全底線：車用防凍液（乙二醇）劇毒，喝一小勺就能致死！太陽能熱水盤管泡在全家洗澡喝水的熱水罐裡。若盤管爛穿微漏，只有無毒食品級丙二醇（Propylene Glycol）才絕不會毒死全家人！", "BS EN 12976 Factory made solar systems; Water Supply (Water Fittings) Regs 1999"),

        ("10.5",
         "What is the phenomenon of 'Stagnation' in a solar thermal heating system, and how does the primary circuit safely accommodate it?",
         "在太陽能熱水系統中，什麼是「熱停滯 / 悶曬汽化現象 (Stagnation)」，封閉管路是通過何種防護組件安全吸收消化高溫高壓蒸汽的？",
         {"A": "The sun stops shining forever", "B": "Occurs when hot water storage reaches maximum temperature in summer and the solar circulator pump shuts down; intense solar radiation vaporizes the trapped glycol in the roof collectors into steam, buffered safely into a dedicated solar expansion vessel", "C": "Water turns to ice in summer", "D": "The panels catch fire"},
         {"A": "太陽永久停止發光發熱", "B": "夏季全家外出度假無人用水、水罐燒滿 85°C 極限水溫後循環泵強制停機保護；樓頂集熱板在烈日暴曬下溫度飆升突破 200°C，封閉管內的防凍液瞬間汽化沸騰為高壓蒸汽，蒸汽被安全推入專用高溫太陽能膨脹罐中緩衝", "C": "水在盛夏酷暑自發凝結成冰", "D": "太陽能電池板自發引燃大火"},
         "B", "When the cylinder is full, the pump stops to prevent scalding. Collectors reach stagnation (>200°C), turning glycol to steam. Solar-rated high-temperature expansion vessels and 6-bar PRVs absorb the surge safely.", "悶曬汽化考驗（Stagnation）：夏天全家去西班牙度假兩星期，水罐早就滾燙燒滿了，水泵自動停轉防燙傷。樓頂集熱板在烈日下乾燒到 200°C！藥水化為高壓蒸汽，必須配備耐 130°C 高溫太陽能膨脹罐和安全閥抗壓！", "BS EN 12977; MCS Solar Thermal Standards; C&G Unit ENV"),

        ("10.5",
         "What is the fundamental thermodynamic principle of an Air Source Heat Pump (ASHP) used for domestic space and water heating?",
         "用於家庭供暖與生活熱水的「空氣源熱泵 (Air Source Heat Pump - ASHP)」，其逆卡諾循環熱力學基本原理是什麼？",
         {"A": "It burns air using electric sparks", "B": "It uses an electric compressor to circulate a low-boiling-point refrigerant, extracting low-grade latent thermal energy from outdoor ambient air (even down to -20°C) and upgrading it to useful high-grade heat for radiators or underfloor heating", "C": "It generates heat by friction from fan blades", "D": "It cools the house in winter"},
         {"A": "利用電火花將室外空氣直接點燃燃燒", "B": "利用電動壓縮機驅動超低沸點環保製冷劑循環流動，從室外冰冷的環境空氣中（即使在零下 -20°C 低溫下）吸收低品位潛在熱能，通過壓縮升溫升壓昇華為高品位熱能，供室內地暖或暖氣片採暖", "C": "依靠風扇葉片高速旋轉與空氣劇烈摩擦生熱", "D": "在冬天為房屋室內強制吹冷風降溫"},
         "B", "Heat pumps do not create heat by burning fuel; they act as a refrigerator in reverse. Liquid refrigerant boils at -40°C in the outdoor coil, absorbs heat from cold air, is compressed hot, and transfers heat to water.", "熱泵是能量搬運工：它不是電爐絲燒水，而是「空調制熱反著轉」！冷媒在零下幾十度就能沸騰吸熱，從室外零度空氣中瘋狂吸走熱量；壓縮機像打氣筒一樣一壓縮，冷媒瞬間飆到 50-60°C，把水燒熱。花 1 度電搬來 3-4 度熱！", "BS EN 14511 Air conditioners, liquid chilling packages and heat pumps; MCS MIS 3005"),

        ("10.5",
         "What does a 'Coefficient of Performance' (COP) rating of 3.5 indicate for an Air Source Heat Pump?",
         "若某台空氣源熱泵標稱的「性能係數 (Coefficient of Performance - COP)」為 3.5，在能效物理學上代表何種精確含義？",
         {"A": "It uses 3.5 times more gas than a boiler", "B": "For every 1.0 kilowatt (kW) of electrical energy consumed by the compressor and pumps, the heat pump produces 3.5 kW of thermal heat output delivered into the central heating system (350% efficiency)", "C": "It breaks down after 3.5 days", "D": "It cools the room by 3.5 degrees"},
         {"A": "消耗的天然氣量是普通壁掛爐的 3.5 倍", "B": "熱泵壓縮機與水泵每消耗「1.0 千瓦 (kW)」的輸入電能，就能向室內供暖水系統實時輸出「3.5 千瓦 (kW)」的龐大熱量（等效能源利用轉化率高達 350%）", "C": "機器運轉 3.5 天後會自發損壞報廢", "D": "將室內房間溫度精確降低 3.5 度"},
         "B", "COP is Heat Output divided by Electrical Input. A COP of 3.5 means 350% efficiency: 1 kW of paid electricity captures 2.5 kW of free ambient air heat to deliver 3.5 kW total warmth.", "COP 數值越高越省錢：普通電暖器 1 度電換 1 度熱（COP 1.0）；壁掛爐燒氣效率 90%（COP 0.9）。熱泵 COP 達到 3.5，意味著你交 1 度電費，大自然免費送你 2.5 度熱，家裡白拿 3.5 度熱！極致節能！", "BS EN 14825; MCS Heat Pump Installation Standard MIS 3005; C&G Unit ENV"),

        ("10.5",
         "What is the 'Seasonal Coefficient of Performance' (SCOP) of a heat pump system, and why is it more realistic than a static COP rating?",
         "熱泵系統的「季節性能係數 (Seasonal Coefficient of Performance - SCOP)」是指什麼？為什麼它比實驗室單點靜態 COP 更能真實反映全年運行成本？",
         {"A": "The cost of painting the heat pump", "B": "The weighted average energy efficiency calculated across an entire year's heating season, factoring in fluctuating winter air temperatures, defrost cycles, and variable heating demands", "C": "The speed of the outdoor fan", "D": "The weight of the outdoor unit in summer"},
         {"A": "熱泵外機每年油漆翻新的保養費用", "B": "綜合考量全年度整個供暖季室外溫差劇烈波動（嚴冬極寒、春秋微冷）、外機主動化霜除霜能耗、以及室內動態負荷變化，計算出的「全年綜合加權平均能效比」", "C": "室外散熱風扇在各個季節的轉速", "D": "熱泵外機在夏季的物理自重重量"},
         "B", "COP fluctuates daily (high in autumn, lower in deep freeze). SCOP integrates the full heating season over thousands of hours, giving consumers an honest prediction of annual running costs and carbon emissions.", "SCOP 季節平均能效真金白銀：COP 是實驗室 7°C 測的靚照；但冬天外面零下 5 度外機會結霜，能效會降。SCOP 把整個冬天的嚴寒、回暖、化霜全算在一起平均！SCOP 若有 3.2，說明全年實打實花 1 度電得 3.2 度熱！", "BS EN 14825 Testing under part load conditions; C&G Unit ENV"),

        ("10.5",
         "Why does an Air Source Heat Pump achieve substantially higher efficiency (higher COP) when connected to an Underfloor Heating (UFH) system than when connected to traditional small radiators?",
         "當空氣源熱泵接入低溫地板輻射採暖（水地暖 UFH）系統時，為什麼其運行能效（COP）遠遠高於接入傳統老式小面積散熱器暖氣片？",
         {"A": "UFH uses less water than radiators", "B": "UFH distributes heat across massive surface area, requiring low water flow temperatures (35°C to 40°C); lower flow temperatures reduce compressor pressure lift, allowing the heat pump to operate at peak thermodynamic efficiency", "C": "Radiators reflect heat away", "D": "Heat pumps only work with timber floors"},
         {"A": "水地暖管網內部的水容量比暖氣片小得多", "B": "水地暖覆蓋全屋巨大散熱面積，僅需「35°C 至 40°C」的超低溫熱水即可滿足供熱；出水溫度越低，熱泵壓縮機做功溫差壓比越小，壓縮機運轉極其輕鬆，能效 COP 呈爆發式提升！", "C": "暖氣片會把熱泵產生的熱量反向彈出窗外", "D": "熱泵只能與純實木木地板搭配工作"},
         "B", "Compressor physics: For every 1°C reduction in required flow temperature, heat pump efficiency rises ~2.5%. UFH runs at 35°C (COP ~4.0), whereas small old radiators demand 70°C (COP drops to ~2.2).", "熱泵降溫提效天生一對：出水溫度每降低 1°C，熱泵節省約 2.5% 電！老暖氣片面積小，逼著熱泵燒到 70°C 滾燙水，壓縮機累吐血 COP 跌到 2.0；地暖整層樓板都是散熱面，35°C 溫水就暖洋洋，COP 直衝 4.0！", "MCS MIS 3005; Domestic Heating Design Guide; C&G Unit ENV"),

        ("10.5",
         "What is a Ground Source Heat Pump (GSHP) with a closed 'Horizontal Slinky Loop' ground collector array?",
         "在家庭地源熱泵（GSHP）系統中，所謂的「水平地埋管盤管矩陣 (Horizontal Slinky Loop Array)」具有何種埋設構造？",
         {"A": "A vertical hole drilled 5,000 meters into magma", "B": "Overlapping coils of high-density polyethylene (HDPE) pipe laid horizontally in excavated trenches approximately 1.2 to 1.5 meters below ground level, circulating glycol to absorb stable solar/geothermal ground heat", "C": "Pipes laid on top of the lawn exposed to rain", "D": "A swimming pool full of salt"},
         {"A": "向地下垂直開鑿 5000 米深達岩漿層的超深鑽孔", "B": "在花園草坪下方開挖 1.2 米至 1.5 米深的平溝，將高密度聚乙烯（HDPE）抗壓盤管按彈簧圈狀相互重疊鋪設在溝底，循環防凍液以持續吸取地下恆定土壤地熱能", "C": "直接將水管隨意搭放在草坪表面任由風吹雨淋", "D": "灌滿食用鹽的室外露天游泳池"},
         "B", "Slinky coils maximize pipe length per meter of trench. Buried below the frost line at 1.2-1.5m, the subsoil maintains a stable 8°C-12°C all year, providing an unflinching heat source regardless of freezing air.", "彈簧地埋管（Slinky Loop）省地精髓：1.2-1.5 米深土層常年恆溫 8-12°C（不管地面下多大暴雪）！把塑料管像彈簧拉花一樣盤在溝底，大大增加與泥土接觸面積，泥土熱量源源不斷被吸走送進屋內，全年 COP 超穩定！", "BS EN 14511; Ground Source Heat Pump Association (GSHPA) Standards; C&G Unit ENV"),

        ("10.5",
         "What is a 'Thermal Store' (Accumulator Buffer Tank) installed in conjunction with biomass pellet boilers or heat pumps?",
         "在生物質木屑顆粒壁掛爐（Biomass）或多熱源熱泵系統中，加裝的「高保溫蓄熱水罐 / 緩衝儲熱水箱 (Thermal Store / Accumulator Tank)」具有何種系統平衡功能？",
         {"A": "A giant refrigerator", "B": "A heavily insulated, large-volume water vessel that acts as a central thermal battery, storing excess heat generated during peak boiler firing and smoothing intermittent heat delivery to variable heating and DHW zones", "C": "A tank for storing motor petrol", "D": "A domestic washing machine"},
         {"A": "巨型廚房冷凍冰箱", "B": "大容量、超厚保溫層的儲熱水箱，充當「水力與熱能蓄電池」樞紐：暫存鍋爐滿負荷高溫燃燒時釋放的多餘熱量，消除壁掛爐頻繁短週期啟停短循環，平穩向多迴路地暖與生活熱水調度供熱", "C": "用來常年儲存汽車汽油的鋼罐", "D": "家用滾筒式全自動洗衣機"},
         "B", "Biomass boilers take 20+ minutes to ignite and burn best at 100% capacity. Thermal stores buffer this heat, letting the boiler burn cleanly for hours, then distributing stored heat to heating circuits as needed.", "緩衝水箱（能量蓄電池）：顆粒燃木爐不像燃氣爐說開就開，點一次火要十幾分鐘，滿火燒最乾淨省柴！蓄熱罐像大電池一樣把幾百升滾燙熱水存起來，家裡哪裡要熱隨時調用，徹底杜絕壁掛爐頻繁熄火點火爛機器！", "BS EN 12828; C&G Unit ENV Renewable Technologies"),

        ("10.5",
         "What is a 'Defra-Exempt' (Ecodesign Ready) wood-burning stove under the Clean Air Act 1993?",
         "根據英國 1993 年清潔空氣法案（Clean Air Act 1993）與生態設計（Ecodesign）標準，所謂的「Defra 認證豁免燃木火爐 (Defra-Exempt Stove)」是指何種環保爐具？",
         {"A": "A stove that burns plastic bags", "B": "An engineered solid fuel appliance rigorously tested and certified to burn seasoned wood logs with ultra-low particulate emissions (PM2.5), legally permitting its operation inside designated Smoke Control Areas", "C": "A gas fire disguised as wood", "D": "An electric fan heater"},
         {"A": "專門用於在室內焚燒塑料垃圾袋的廢物爐", "B": "通過英國環境食品和鄉村事務部（Defra）嚴格檢測認證的高效固體燃料爐具，燃燒乾燥原木時顆粒微粒（PM2.5）排放極低，被法律允許在城市法定的「煙塵控制區 (Smoke Control Areas)」內合法點火燃燒", "C": "偽裝成原木柴火造型的天然氣明火壁爐", "D": "普通便攜式電動暖風機"},
         "B", "Smoke Control Areas ban burning smoky wood. Defra-exempt stoves feature secondary/tertiary tertiary pre-heated combustion air that re-burns smoke gases, meeting stringent Ecodesign clean air limits.", "Defra 城市壁爐通行證：倫敦等大城市全境都是「控煙區（Smoke Control Area）」，敢隨便點木頭冒黑煙會被市政大額罰款！Defra 豁免爐肚子裡有二次進風二次燃燒技術，把黑煙當燃料再燒一次，只出熱氣無黑煙，合法合規！", "Clean Air Act 1993; Defra Smoke Control Area Regulations; Approved Document J")
    ]

    for sub_id, stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref in data:
        questions.append(make_q(10, sub_id, ["Unit_ENV", "Unit_207"], stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref))

    from .ch10_part2 import get_part2_questions
    questions.extend(get_part2_questions())

    return questions
