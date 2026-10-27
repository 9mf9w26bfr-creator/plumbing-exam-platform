import { TextbookChapter, ExamUnit, Question } from '../types';

export const initialChapters: TextbookChapter[] = [
  {
    id: 1,
    title: 'Health and safety practices and systems',
    sub_topics: [
      { id: '1.1', title_en: 'Health and safety legislation & regulations', title_zh: '健康與安全法規與條例' },
      { id: '1.2', title_en: 'Personal protective equipment (PPE)', title_zh: '個人防護裝備 (PPE)' },
      { id: '1.3', title_en: 'Safe working at height & ladders', title_zh: '高空作業安全與梯子規範' },
      { id: '1.4', title_en: 'Hazard identification and risk assessment', title_zh: '危險源識別與風險評估' }
    ],
    question_count: 1
  },
  {
    id: 2,
    title: 'Common processes and techniques',
    sub_topics: [
      { id: '2.1', title_en: 'Hand and power tools safety and maintenance', title_zh: '手動與電動工具安全及維護' },
      { id: '2.2', title_en: 'Pipe jointing techniques (soldering, compression)', title_zh: '管道連接技術 (焊接、卡壓)' },
      { id: '2.3', title_en: 'Pipe bending and clipping', title_zh: '管道彎曲與管卡固定' }
    ],
    question_count: 1
  },
  {
    id: 3,
    title: 'Scientific principles',
    sub_topics: [
      { id: '3.1', title_en: 'Units of measurement (SI Units)', title_zh: '國際單位制與測量單位' },
      { id: '3.2', title_en: 'Properties of water & state changes', title_zh: '水的物理性質與狀態改變' },
      { id: '3.3', title_en: 'Pressure and head calculation', title_zh: '水壓與水頭計算' },
      { id: '3.4', title_en: 'Heat transfer (conduction, convection, radiation)', title_zh: '熱傳遞原理 (傳導、對流、輻射)' }
    ],
    question_count: 1
  },
  {
    id: 4,
    title: 'Planning and supervision',
    sub_topics: [
      { id: '4.1', title_en: 'Material estimating and ordering', title_zh: '材料預估與採購' },
      { id: '4.2', title_en: 'Liaison with other building trades', title_zh: '與其他建築工種的協同溝通' }
    ],
    question_count: 0
  },
  {
    id: 5,
    title: 'Cold water systems',
    sub_topics: [
      { id: '5.1', title_en: 'Direct and indirect cold water supply', title_zh: '直接式與間接式冷水供水系統' },
      { id: '5.2', title_en: 'Cold water storage cisterns (CWSC)', title_zh: '冷水儲水箱規格與安裝' },
      { id: '5.3', title_en: 'Water regulations and backflow prevention', title_zh: '水事法規與防回流污染等級 (Fluid Categories)' }
    ],
    question_count: 1
  },
  {
    id: 6,
    title: 'Hot water systems',
    sub_topics: [
      { id: '6.1', title_en: 'Vented hot water storage systems', title_zh: '開式(通風型)熱水儲水系統' },
      { id: '6.2', title_en: 'Unvented hot water storage & safety controls', title_zh: '閉式(承壓型)熱水儲水系統與三級安全保護' },
      { id: '6.3', title_en: 'Legionella prevention and TMV regulation', title_zh: '軍團菌防治與恆溫混水閥 (TMV) 控制' }
    ],
    question_count: 2
  },
  {
    id: 7,
    title: 'Central heating systems',
    sub_topics: [
      { id: '7.1', title_en: 'Heat emitters and pipe sizing', title_zh: '散熱器類型與管徑計算' },
      { id: '7.2', title_en: 'System controls (S-Plan, Y-Plan, TRVs)', title_zh: '供暖控制系統 (S-Plan, Y-Plan, 恆溫閥)' }
    ],
    question_count: 1
  },
  {
    id: 8,
    title: 'Rainwater systems',
    sub_topics: [
      { id: '8.1', title_en: 'Gutters and downpipes sizing', title_zh: '天溝與落水管尺寸規劃' },
      { id: '8.2', title_en: 'Rainwater harvesting principles', title_zh: '雨水收集利用基本原理' }
    ],
    question_count: 0
  },
  {
    id: 9,
    title: 'Sanitation systems',
    sub_topics: [
      { id: '9.1', title_en: 'Sanitary appliances installation', title_zh: '衛生器具安裝要求與間距' },
      { id: '9.2', title_en: 'Discharge stack systems and trap seal loss', title_zh: '排水立管系統與存水彎水封防破壞' }
    ],
    question_count: 1
  },
  {
    id: 10,
    title: 'Domestic fuel systems',
    sub_topics: [
      { id: '10.1', title_en: 'Fuel storage and supply guidelines', title_zh: '燃料儲存與輸送指引' },
      { id: '10.2', title_en: 'Combustion and ventilation requirements', title_zh: '燃燒與通風要求' }
    ],
    question_count: 1
  },
  {
    id: 11,
    title: 'Electrical principles and processes for building services engineering',
    sub_topics: [
      { id: '11.1', title_en: 'Basic electrical safety and safe isolation', title_zh: '電氣安全基礎與安全隔離五步法' },
      { id: '11.2', title_en: 'Bathroom zoning (Zone 0, 1, 2) and IP ratings', title_zh: '浴室電氣分區 (Zone 0, 1, 2) 與 IP 防護等級' },
      { id: '11.3', title_en: 'Equipotential bonding and earthing', title_zh: '等電位聯結與接地保護' }
    ],
    question_count: 1
  }
];

export const initialUnits: ExamUnit[] = [
  { id: 'Unit_201', title: 'Health & Safety', category: 'Core', question_count: 2 },
  { id: 'Unit_202', title: 'Scientific Principles', category: 'Core', question_count: 2 },
  { id: 'Unit_203', title: 'Common Plumbing Processes', category: 'Core', question_count: 1 },
  { id: 'Unit_204', title: 'Cold Water Systems', category: 'Technical', question_count: 2 },
  { id: 'Unit_205', title: 'Hot Water Systems', category: 'Technical', question_count: 2 },
  { id: 'Unit_206', title: 'Sanitation & Drainage', category: 'Technical', question_count: 1 },
  { id: 'Unit_207', title: 'Central Heating Systems', category: 'Technical', question_count: 2 },
  { id: 'Unit_208', title: 'Electrical Principles', category: 'Technical', question_count: 1 },
  { id: 'Unit_209', title: 'Communication / Planning', category: 'Professional', question_count: 0 },
  { id: 'Unit_ENV', title: 'Environmental Revision', category: 'Environmental Revision', question_count: 1 }
];

export const initialQuestions: Question[] = [
  {
    id: '1a111111-0000-4000-8000-000000000001',
    content_en: 'A plumbing engineer is testing water pressure at the base of a 15-meter tall commercial building. The cold water storage cistern is situated at roof level. Neglecting pipe friction, what is the static pressure at the lowest outlet?',
    content_zh: '一名水暖工程師正在一棟15米高的商業建築底部測試水壓。冷水儲水箱設在屋頂。在忽略管壁摩擦的情況下，最低出水點處的靜態水壓是多少？',
    options_en: {
      A: '0.15 bar (15 kPa)',
      B: '1.5 bar (150 kPa)',
      C: '15.0 bar (1500 kPa)',
      D: '0.5 bar (50 kPa)'
    },
    options_zh: {
      A: '0.15 bar (15 kPa)',
      B: '1.5 bar (150 kPa)',
      C: '15.0 bar (1500 kPa)',
      D: '0.5 bar (50 kPa)'
    },
    correct_answer: 'B',
    explanation_en: 'Static water pressure equals 1 metre head = 0.1 bar (approx 9.81 kPa, commonly rounded to 10 kPa in C&G level 2 exams). Therefore, 15 m static head = 15 x 0.1 bar = 1.5 bar (150 kPa).',
    explanation_zh: '靜態水壓換算規則為：1米水頭約產生 0.1 bar (約 10 kPa) 的壓力。因此，15米靜態水頭產生的壓力為 15 × 0.1 bar = 1.5 bar (150 kPa)。',
    status: 'Published',
    source_reference: 'C&G 6035 Unit 202; Textbook Chapter 3 Scientific Principles (p. 112)',
    chapters: [{ chapter_id: 3, sub_topic_id: '3.3' }],
    units: ['Unit_202', 'Unit_204']
  },
  {
    id: '1a111111-0000-4000-8000-000000000002',
    content_en: 'Under The Water Supply (Water Fittings) Regulations 1999, what fluid category describes water that represents a serious health hazard due to the presence of pathogens or toxic chemicals, such as in bidets with flexible spray hoses below the spillover level?',
    content_zh: '根據《1999年供水（水配件）條例》，哪一個流體風險等級（Fluid Category）定義了因存在病原體或有毒化學物質而對人體健康構成嚴重危害的水質（例如噴頭低於溢流邊緣的婦洗器軟管）？',
    options_en: {
      A: 'Fluid Category 2',
      B: 'Fluid Category 3',
      C: 'Fluid Category 4',
      D: 'Fluid Category 5'
    },
    options_zh: {
      A: '流體類別 2 (Fluid Category 2)',
      B: '流體類別 3 (Fluid Category 3)',
      C: '流體類別 4 (Fluid Category 4)',
      D: '流體類別 5 (Fluid Category 5)'
    },
    correct_answer: 'D',
    explanation_en: 'Fluid Category 5 represents a serious health hazard because of the concentration of pathogenic organisms or radioactive or very toxic substances. A Type AB or AA air gap is mandatory.',
    explanation_zh: '流體類別 5 代表因含有高致病微生物、放射性物質或劇毒物質而對人體健康構成嚴重危害的等級。此類風險必須使用物理空氣隔斷（如 Type AA 或 Type AB 空氣間隙）防回流。',
    status: 'Published',
    source_reference: 'The Water Supply (Water Fittings) Regulations 1999, Schedule 1 & BS EN 1717',
    chapters: [{ chapter_id: 5, sub_topic_id: '5.3' }],
    units: ['Unit_204']
  },
  {
    id: '1a111111-0000-4000-8000-000000000003',
    content_en: 'According to BS 7671 (Requirements for Electrical Installations), what is the minimum IP rating required for electrical equipment installed inside Zone 1 of a room containing a bath or shower basin where water jets are not likely?',
    content_zh: '根據 BS 7671 電氣安裝規範，在包含浴缸或淋浴的浴室 Zone 1 區域內，如果不太可能受到噴水衝擊，安裝的電氣設備所要求的最低 IP 防水防護等級是多少？',
    options_en: {
      A: 'IPX0',
      B: 'IPX2',
      C: 'IPX4',
      D: 'IPX7'
    },
    options_zh: {
      A: 'IPX0 (無防水)',
      B: 'IPX2 (防滴水)',
      C: 'IPX4 (防濺水)',
      D: 'IPX7 (防短時間浸水)'
    },
    correct_answer: 'C',
    explanation_en: 'BS 7671 Section 701 dictates that equipment installed in Zone 1 must have a minimum degree of protection of IPX4 (or IPX5 if water jets are likely for cleaning). Zone 0 requires IPX7.',
    explanation_zh: 'BS 7671 第 701 節規定，在浴室 Zone 1 區域安裝的電氣設備必須至少具備 IPX4（防濺水）防護等級；若可能存在清潔噴水，則須達到 IPX5。Zone 0 區域要求達到 IPX7。',
    status: 'Published',
    source_reference: 'BS 7671:2018+A2:2022 Section 701; C&G Unit 208',
    chapters: [{ chapter_id: 11, sub_topic_id: '11.2' }],
    units: ['Unit_208', 'Unit_204']
  },
  {
    id: '1a111111-0000-4000-8000-000000000004',
    content_en: 'An apprentice is using an unvented hot water cylinder. What temperature does the temperature and pressure relief valve (T&P valve) typically open at to prevent catastrophic explosion if all electrical thermostats fail?',
    content_zh: '一名學徒正在調試一套閉式（承壓型）熱水儲水缸。當所有電氣溫控器均失效時，溫度與壓力安全閥（T&P Valve）通常在什麼溫度下自動開啟，以防止儲水缸發生災難性超溫爆炸？',
    options_en: {
      A: '60°C to 65°C',
      B: '75°C to 80°C',
      C: '90°C to 95°C',
      D: '120°C to 125°C'
    },
    options_zh: {
      A: '60°C 至 65°C',
      B: '75°C 至 80°C',
      C: '90°C 至 95°C',
      D: '120°C 至 125°C'
    },
    correct_answer: 'C',
    explanation_en: 'Building Regulations Approved Document G3 specifies three levels of safety for unvented hot water cylinders. The final mechanical relief device (T&P valve) operates at 90-95°C (and typically 10 bar pressure) to discharge expanding water safely via a tundish.',
    explanation_zh: '英國建築規範 Approved Document G3 對閉式熱水缸規定了三級安全防護。最終機械安全洩壓裝置（T&P 閥）設定在 90°C-95°C（且通常伴隨 10 bar 壓力限制）開啟，通過放水漏斗（Tundish）安全排洩膨脹高溫水。',
    status: 'Published',
    source_reference: 'Building Regulations Approved Document G (Section G3); BS EN 12897',
    chapters: [{ chapter_id: 6, sub_topic_id: '6.2' }],
    units: ['Unit_205']
  },
  {
    id: '1a111111-0000-4000-8000-000000000005',
    content_en: 'To prevent the colonisation and growth of Legionella pneumophila bacteria in domestic hot water storage, what is the minimum temperature at which water should be stored inside a hot water cylinder?',
    content_zh: '為防止軍團菌（Legionella pneumophila）在生活熱水儲水系統中滋生與繁殖，熱水儲水缸內的水溫至少應維持在多少攝氏度？',
    options_en: {
      A: '40°C',
      B: '50°C',
      C: '60°C',
      D: '75°C'
    },
    options_zh: {
      A: '40°C',
      B: '50°C',
      C: '60°C',
      D: '75°C'
    },
    correct_answer: 'C',
    explanation_en: 'HSE Approved Code of Practice L8 and Building Regs Approved Document G specify that hot water should be stored at 60°C or above. Legionella bacteria proliferate between 20°C and 45°C and are killed within minutes at 60°C.',
    explanation_zh: 'HSE 實踐守則 L8 及建築規範 Approved Document G 要求儲水溫度不得低於 60°C。軍團菌在 20°C 至 45°C 之間極易繁殖，而在 60°C 環境下可在數分鐘內被徹底消滅。',
    status: 'Published',
    source_reference: 'HSE ACoP L8; Approved Document G; HSG274 Part 2',
    chapters: [{ chapter_id: 6, sub_topic_id: '6.3' }],
    units: ['Unit_205', 'Unit_201']
  },
  {
    id: '1a111111-0000-4000-8000-000000000006',
    content_en: 'When using a leaning ladder to access a flat roof scaffolding platform, what is the correct angle of inclination according to HSE guidelines (or the \'1 in 4 rule\')?',
    content_zh: '根據 HSE 安全生產指引，在搭設直梯登上平屋頂作業平臺時，梯子與地面的推薦傾斜角度（即“1比4比例法則”）是多少？',
    options_en: {
      A: '60 degrees',
      B: '75 degrees',
      C: '45 degrees',
      D: '85 degrees'
    },
    options_zh: {
      A: '60 度',
      B: '75 度 (約 1:4 比例)',
      C: '45 度',
      D: '85 度'
    },
    correct_answer: 'B',
    explanation_en: 'The Health and Safety Executive (HSE) specifies the 1 in 4 rule for leaning ladders: 1 unit out for every 4 units up, which creates an inclination angle of approximately 75 degrees.',
    explanation_zh: 'HSE 規定便攜式斜梯必須遵循 1:4 法則（垂直升高 4 米，梯腳外移 1 米），對應的安全擺放仰角約為 75 度，確保梯子既不會向後傾翻也不會向外滑脫。',
    status: 'Published',
    source_reference: 'Work at Height Regulations 2005; HSE INDG455 Safe use of ladders',
    chapters: [{ chapter_id: 1, sub_topic_id: '1.3' }],
    units: ['Unit_201']
  },
  {
    id: '1a111111-0000-4000-8000-000000000007',
    content_en: 'In a domestic single stack drainage system, what is the primary cause of \'induced siphonage\' in a washbasin trap?',
    content_zh: '在室內單立管重力排水系統中，導致洗手盆存水彎產生“誘導虹吸（Induced Siphonage）”失封的主要原因是什麼？',
    options_en: {
      A: 'Slow discharge from the basin itself pulling water through momentum',
      B: 'High water velocity down the main discharge stack creating negative pressure in the branch pipe',
      C: 'Wind blowing over the external vent pipe creating a suction effect',
      D: 'Capillary action caused by hair caught over the trap weir'
    },
    options_zh: {
      A: '洗手盆自身排水速度過慢產生的自重拉力',
      B: '主排水立管中大量水流快速下落，在支管入口處形成瞬時負壓',
      C: '室外屋頂通風管上方強風產生的文丘里吸吮效應',
      D: '跨越存水彎水封堰的毛發引起的毛細吸水現象'
    },
    correct_answer: 'B',
    explanation_en: 'Induced siphonage occurs when the rapid discharge of water from an upper appliance passes down the main vertical discharge stack, creating negative air pressure which draws out the water seal of lower branch appliances.',
    explanation_zh: '誘導虹吸是指上方器具大量排水流經垂直排水主立管時，高速水栓帶走空氣形成負壓波，從而將相連支管存水彎中的水封吸走破壞。',
    status: 'Published',
    source_reference: 'BS EN 12056-2; Approved Document H Drainage and waste disposal',
    chapters: [{ chapter_id: 9, sub_topic_id: '9.2' }],
    units: ['Unit_206']
  },
  {
    id: '1a111111-0000-4000-8000-000000000008',
    content_en: 'Which copper pipe jointing method requires the application of flux to prevent oxidation of the metal surfaces during heating?',
    content_zh: '哪一種銅管連接方法必須塗抹助焊劑（Flux），以在加熱過程中防止金屬表面氧化並促進熔融焊料的毛細潤濕？',
    options_en: {
      A: 'Type A compression joint',
      B: 'Type B manipulate compression joint',
      C: 'Capillary solder joint',
      D: 'Push-fit mechanical joint'
    },
    options_zh: {
      A: 'Type A 非擴口卡壓接頭',
      B: 'Type B 擴口機械卡套接頭',
      C: '毛細焊錫焊接接頭 (Capillary solder joint)',
      D: '免工具快插接頭 (Push-fit)'
    },
    correct_answer: 'C',
    explanation_en: 'Capillary end-feed and integral solder ring fittings require active chemical flux to clean copper oxide and prevent surface oxidation when heated by a blowlamp.',
    explanation_zh: '毛細軟釬焊與預置焊料環接頭必須使用助焊劑，在噴燈高溫加熱狀態下清除氧化膜並保持銅管表面潔淨，使熔融焊錫能順利發生毛細潤濕填充。',
    status: 'Published',
    source_reference: 'C&G 6035 Unit 203; Textbook Chapter 2 Common Processes (p. 68)',
    chapters: [{ chapter_id: 2, sub_topic_id: '2.2' }],
    units: ['Unit_203']
  },
  {
    id: '1a111111-0000-4000-8000-000000000009',
    content_en: 'A plumber is calculating heat emissions for a central heating radiator. If the temperature of water entering the radiator is 75°C, the return temperature is 65°C, and the room design temperature is 20°C, what is the mean water temperature (MWT) and delta T (ΔT)?',
    content_zh: '水暖工正在計算中央供暖散熱器的熱輸出。若供水進水溫度為 75°C，回水溫度為 65°C，房間設計室溫為 20°C，則平均水溫 (MWT) 和溫差 (ΔT) 分別是多少？',
    options_en: {
      A: 'MWT = 70°C, ΔT = 50°C',
      B: 'MWT = 75°C, ΔT = 55°C',
      C: 'MWT = 65°C, ΔT = 45°C',
      D: 'MWT = 70°C, ΔT = 10°C'
    },
    options_zh: {
      A: '平均水溫 MWT = 70°C, ΔT = 50°C',
      B: '平均水溫 MWT = 75°C, ΔT = 55°C',
      C: '平均水溫 MWT = 65°C, ΔT = 45°C',
      D: '平均水溫 MWT = 70°C, ΔT = 10°C'
    },
    correct_answer: 'A',
    explanation_en: 'Mean Water Temperature (MWT) = (Flow + Return) / 2 = (75 + 65) / 2 = 70°C. Delta T (ΔT) = MWT - Room Temperature = 70°C - 20°C = 50°C (standard British/European test condition BS EN 442).',
    explanation_zh: '平均水溫 MWT = (進水 75°C + 回水 65°C) / 2 = 70°C。散熱溫差 ΔT = MWT - 室溫 = 70°C - 20°C = 50°C，此為 BS EN 442 標準測試基準工況。',
    status: 'Published',
    source_reference: 'BS EN 442; C&G Unit 207 Central Heating Systems',
    chapters: [{ chapter_id: 7, sub_topic_id: '7.1' }],
    units: ['Unit_207', 'Unit_202']
  },
  {
    id: '1a111111-0000-4000-8000-000000000010',
    content_en: 'Under Building Regulations Approved Document L, what is the maximum specific fan power and minimum seasonal efficiency required for replacing a condensing gas boiler in an existing domestic dwelling?',
    content_zh: '根據英國建築法規 Approved Document L（能耗節約），在既有住宅中更換冷凝燃氣鍋爐時，其 ErP 最低季節性能效指標（SEDBUK/seasonal efficiency）通常要求達到多少？',
    options_en: {
      A: '78%',
      B: '86%',
      C: '92%',
      D: '98%'
    },
    options_zh: {
      A: '78%',
      B: '86%',
      C: '92%',
      D: '98%'
    },
    correct_answer: 'C',
    explanation_en: 'Approved Document L (Conservation of fuel and power) requires new and replacement domestic natural gas boilers to achieve a minimum seasonal space heating efficiency of 92% (ErP A-rating).',
    explanation_zh: 'Approved Document L 規定既有住宅更換天然氣鍋爐的最低季節性采暖能效要求達到 92%（對應 ErP A 級能效），以顯著降低碳排放與燃料消耗。',
    status: 'Published',
    source_reference: 'Building Regulations Approved Document L1B Conservation of Fuel and Power',
    chapters: [{ chapter_id: 10, sub_topic_id: '10.2' }],
    units: ['Unit_ENV', 'Unit_207']
  },
  {
    id: '1a111111-0000-4000-8000-000000000011',
    content_en: 'What is the mandatory procedure when carrying out Safe Isolation on a single-phase domestic central heating programmer before performing electrical maintenance?',
    content_zh: '在對單相家用中央供暖溫控編程器進行電氣檢修前，執行“安全隔離（Safe Isolation）”的法定規範操作步驟是什麼？',
    options_en: {
      A: 'Turn off the fused spur switch and tape it with insulating tape',
      B: 'Isolate the supply, lock off with padlock and danger notice, test proving unit, test circuits with voltage indicator, and re-test proving unit',
      C: 'Remove the neutral fuse and check current with an ammeter clamp',
      D: 'Switch off the main consumer unit without proving the voltage indicator'
    },
    options_zh: {
      A: '僅關閉帶熔斷雙極開關並用絕緣膠帶貼住',
      B: '斷開電源，上鎖加掛警告標牌，使用校驗器校準驗電器，檢測待測電路確認無電，再次使用校驗器核實驗電器',
      C: '拔出零線保險絲並使用鉗形表測量回路電流',
      D: '直接切斷總配電箱主開關，無需對驗電器進行前後校驗'
    },
    correct_answer: 'B',
    explanation_en: 'Safe isolation requires: 1. Permission & identify source; 2. Isolate and lock off (LOTO); 3. Prove test instrument on proving unit; 4. Test between all conductors (L-N, L-E, N-E); 5. Re-prove test instrument on proving unit to ensure it did not fail during test.',
    explanation_zh: '電氣安全隔離五步閉環流程：1. 確認斷電範圍；2. 隔離並掛鎖上標簽（LOTO）；3. 使用檢驗器（Proving Unit）校準雙極電壓測試儀；4. 全面測試所有導線對間電壓；5. 再次在檢驗器上復測驗電器功能正常。',
    status: 'Technically_Verified',
    source_reference: 'Electricity at Work Regulations 1989; HSE Guidance Note GS38; BS 7671',
    chapters: [{ chapter_id: 11, sub_topic_id: '11.1' }],
    units: ['Unit_208', 'Unit_201']
  },
  {
    id: '1a111111-0000-4000-8000-000000000012',
    content_en: 'What is the recommended minimum clearance distance between the overflow warning pipe invert and the top water level in a domestic cold water storage cistern (CWSC)?',
    content_zh: '在室內冷水儲水箱（CWSC）中，溢水報警管（Warning pipe）管底標高與正常最高工作水位之間的推薦最小垂直凈距是多少？',
    options_en: {
      A: '10 mm',
      B: '25 mm',
      C: '50 mm',
      D: '75 mm'
    },
    options_zh: {
      A: '10 mm',
      B: '25 mm',
      C: '50 mm',
      D: '75 mm'
    },
    correct_answer: 'B',
    explanation_en: 'The Water Supply Regulations specify that the warning pipe invert should be positioned at least 25 mm above the operating water shut-off level to prevent nuisance splashing and overflow.',
    explanation_zh: '《水條例》及規範要求報警溢流管內底應高出浮球閥關閉時的最高靜止水位至少 25 mm，防止正常波動時溢水。',
    status: 'AI_Reviewed',
    source_reference: 'Water Supply (Water Fittings) Regulations 1999, G24.1',
    chapters: [{ chapter_id: 5, sub_topic_id: '5.2' }],
    units: ['Unit_204']
  },
  {
    id: '1a111111-0000-4000-8000-000000000013',
    content_en: 'Which device must be fitted to an unvented hot water supply system to absorb the expansion volume of water as it is heated from 10°C to 65°C?',
    content_zh: '在閉式承壓生活熱水系統中，必須配置何種裝置以吸收水從 10°C 加熱至 65°C 過程中產生的體積熱膨脹？',
    options_en: {
      A: 'Open vent pipe over CWSC',
      B: 'Diaphragm expansion vessel or internal air bubble',
      C: 'Check valve',
      D: 'Automatic air vent'
    },
    options_zh: {
      A: '儲水箱上方的開放式膨脹管',
      B: '隔膜式膨脹罐或內部充氣氣囊 (Expansion Vessel)',
      C: '單向止回閥',
      D: '自動排氣閥'
    },
    correct_answer: 'B',
    explanation_en: 'Water expands by approximately 3-4% when heated from 10°C to 65°C. In an unvented system, this expansion must be accommodated by a pre-charged diaphragm expansion vessel or internal air bubble.',
    explanation_zh: '水由 10°C 升高至 65°C 體積膨脹約 3%~4%。閉式承壓系統必須依靠帶有預充氮氣/空氣的隔膜膨脹罐或儲水缸頂部的空氣囊緩衝吸收膨脹量。',
    status: 'Draft',
    source_reference: 'Building Regulations Approved Document G3',
    chapters: [{ chapter_id: 6, sub_topic_id: '6.2' }],
    units: ['Unit_205']
  }
];
