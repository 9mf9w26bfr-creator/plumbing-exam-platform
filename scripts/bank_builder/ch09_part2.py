# Chapter 9 Part 2: Additional 48 Questions (Questions 43 to 90)
from .utils import make_q

def get_part2_questions():
    questions = []
    
    data = [
        # 43. Push-fit jointing thermal allowance
        ("9.2",
         "When installing ring-seal (push-fit) polypropylene or PVC soil and waste pipework, what is the mandatory thermal expansion allowance procedure during joint assembly?",
         "在組裝承插式橡膠圈密封（Push-fit）塑料下水支管或排污立管時，為了預留熱脹冷縮伸縮縫，標準的管道插入與回拉工藝是什麼？",
         {"A": "Push the pipe fully home to the bottom of the socket and leave it jammed tight", "B": "Push the pipe fully home to the socket stop, mark the pipe with a pencil at the socket face, and pull the pipe back out by approximately 10mm", "C": "Melt the rubber ring with a blowlamp", "D": "Glue the rubber ring with superglue"},
         {"A": "將管子死命推到底、緊緊頂死在承插口底端", "B": "將管子完全推到底碰觸到底部止動台階，用鉛筆在承口外沿處畫上一道標記線，隨後將管子平穩向外回拉約 10mm (預留 10 毫米伸縮縫)", "C": "拿噴燈火焰烘烤橡膠密封圈", "D": "拿 502 強力膠把橡膠圈與管子粘死"},
         "B", "Plastic expands significantly with hot water discharge. Inserting fully and withdrawing by 10mm provides a critical expansion gap, preventing the pipe from buckling, snaking, or popping out.", "回拉 10mm 防熱脹鐵律：熱水一放塑料管會立刻伸長！若頂到底插死，熱水一燙管子無處伸展，整根管道會像蛇一樣扭曲變形甚至把接頭撐爆。鉛筆畫線回拉 10mm，是英國水暖工基本功！", "BS EN 12056-2; BS EN 1451; C&G Unit 206 Practical Skills"),

        # 44. Chamfering and silicone lubricant
        ("9.2",
         "Why must cut plain ends of push-fit waste pipes always be deburred and chamfered at approximately 45 degrees, and lubricated with silicone spray or silicone grease before insertion?",
         "在切割塑料下水管平口後，為什麼管端外沿必須徹底刮除毛刺並銼削出 45 度倒角（Chamfer），且必須塗抹專用硅油潤滑劑後方可插入？",
         {"A": "To make the pipe lighter", "B": "A square, sharp cut edge will snag, tear, dislodge, or roll the internal rubber ring seal out of its seating groove, causing catastrophic hidden water leakage", "C": "To help the pipe dissolve in water", "D": "To conduct electricity"},
         {"A": "減輕塑料管材的自重", "B": "未倒角的鋒利直角管端在強行插入時會直接刮傷、撕裂內部橡膠密封圈，甚至把橡膠圈從密封槽內硬生生推出翻轉脫位，造成隱蔽性嚴重大漏水", "C": "幫助塑料管道在水中自然溶解", "D": "增強管道的導電性能"},
         "B", "Square edges grab the elastomeric ring, puckering or dislodging it. A 45° chamfer and silicone lubricant allows the spigot to slide smoothly through the seal without disturbing its seat.", "倒角潤滑雙保險：平頭管子生硬硬往裡捅，橡膠圈 100% 被推翻或劃爛！銼刀倒 45° 斜邊、噴上硅油，管子像抹了油一樣順滑滑入，橡膠圈服服帖帖坐在密封槽裡，保證幾十年滴水不漏。", "BS EN 12056-2; C&G Unit 206 Plumbing Skills"),

        # 45. Universal compression waste fittings
        ("9.2",
         "What is the unique mechanical versatility of a 'Universal Compression Waste Fitting' (such as a McAlpine compression bend or coupler)?",
         "以 McAlpine 為代表的「萬能卡壓式塑料排水管件 (Universal Compression Fitting)」，具有何種獨特的管道兼容連接優勢？",
         {"A": "It can only be used on glass pipes", "B": "Its internal cone washer and threaded compression nut can mechanically grip and watertight seal onto different pipe materials, including polypropylene, ABS, MuPVC, and metric/imperial copper", "C": "It welds pipes using ultrasonic waves", "D": "It requires no tightening"},
         {"A": "只能用於連接鋼化玻璃排水管", "B": "利用內部特製的錐形聚乙烯密封圈與鎖緊螺母，能夠強大兼容並機械夾緊各種不同材質外徑的管材（包括 PP 聚丙烯、ABS、PVC、公制與英制紫銅下水管）", "C": "利用超聲波將管道熔接", "D": "完全不需要用手擰緊"},
         "B", "Universal compression fittings adapt between disparate materials (solvent weld ABS, push-fit PP, copper) without specialized glues or adaptors, making them indispensable in maintenance.", "萬能卡壓接頭是維修神器：老房子裝修常遇到亂七八糟的管子——有膠粘的、有插接的、還有銅下水管。萬能接頭螺母一擰，橡膠錐形環抱死管外壁，不管管徑差一兩毫米或材質不同，統統咬死密封！", "BS EN 274; McAlpine Plumbing Products Catalogue; C&G Unit 206"),

        # 46. Mechanical flexible adaptor couplings
        ("9.2",
         "When connecting a modern 110mm PVC underground drainage pipe to an old 4-inch Salt-Glazed Vitrified Clay pipe, what fitting is legally approved under BS EN 295-4?",
         "當需要將現代 110mm PVC 塑料地下排水管接入老舊的 4 英寸「耐酸陶瓷粘土管 (Salt-Glazed Clay Pipe)」時，根據 BS EN 295-4 標準，法規認可的專業過渡連接管件是什麼？",
         {"A": "Wrap the joint with soaked bread", "B": "An elastomeric Flexible Mechanical Coupling (such as a Fernco adaptor) featuring stainless steel worm-drive jubilee clamping bands", "C": "Fill the gap with ordinary silicone mastic", "D": "Hammer the clay pipe into pieces"},
         {"A": "用浸濕的麵包渣包裹接頭", "B": "帶有不銹鋼蝸輪卡箍的專用柔性橡膠異徑機械套管接頭 (Flexible Coupling，如 Fernco 抱箍接頭)", "C": "在縫隙中隨意塗抹普通廚衛玻璃膠", "D": "用鐵錘將陶瓷管砸碎"},
         "B", "Clay and PVC have different outside diameters and expansion rates. Flexible elastomeric sleeve adaptors with stainless steel jubilee clips provide an airtight, watertight, flexible joint.", "不同管材對接必備：老陶瓷管外壁粗糙且外徑偏大，塑料管外徑 110mm，兩者根本套不上。Fernco 橡膠厚套管一套，兩頭不銹鋼喉箍死死擰緊，既抗剪切又防漏，還能吸收地面微小沉降。", "BS EN 295-4; Building Regulations Approved Document H1 Section 2"),

        # 47. Strap-on boss vs solvent-weld boss
        ("9.2",
         "How is a new 40mm waste branch pipe properly introduced into an existing, installed 110mm PVC soil stack without cutting out a whole section of the vertical stack?",
         "在一根既有的 110mm PVC 排污垂直立管上新增一個 40mm 廚衛排水支管時，在不安裝切割整根立管的前提下，水暖工應當採用何種標準管件工藝完成開孔接入？",
         {"A": "Smash a hole with a hammer and push the pipe through", "B": "Drill a hole using the correct hole-saw, then solvent-weld or strap a 110mm Boss Pipe Upstand / Strap-on Boss fitting over the hole, inserting a 40mm rubber boss adaptor bung", "C": "Pave over the stack with plaster", "D": "Burn a hole with a blowlamp"},
         {"A": "用鐵錘直接砸出一個破洞並把管子硬塞進去", "B": "使用精準規格的開孔器在立管上開孔，隨後在孔位上膠粘專用「鞍形馬鞍接頭 (Strap-on Boss)」或熔接短接管件，並塞入匹配的 40mm 橡膠異徑密封轉接套 (Boss Adaptor)", "C": "拿石膏把立管完全抹平掩蓋", "D": "用噴燈烈火將塑料管燒穿一個洞"},
         "B", "Strap-on or clip bosses clamp over hole-sawn openings. The insert rubber boss bung accepts 32mm, 40mm, or 50mm waste pipes, providing a clean, factory-sealed connection.", "立管開孔接管規範：拿專用開孔鑽打出圓孔，抹上膠水把馬鞍形短接頭扣在立管上，裡面塞進橡膠變徑皮圈，40mm 水管抹點硅油一插即合，乾淨利落絕不破壞立管結構強度。", "BS EN 1329; Polypipe / Terrain Soil Systems Manual"),

        # 48. Underground foul drainage pipe color and BS standard
        ("9.2",
         "Under British Standards BS EN 1401-1, what is the standard color of plastic PVC-U pipes manufactured specifically for underground gravity foul and surface water drainage?",
         "根據英國/歐洲標準 BS EN 1401-1，專門用於地下重力排污與雨水埋地管網的硬質 PVC-U 塑料管材，其出廠標準色標是什麼？",
         {"A": "Golden Brown (Terracotta / Orange-Brown)", "B": "Bright pink", "C": "Pure white", "D": "Transparent glass"},
         {"A": "金棕色 / 陶土橘褐色 (Golden Brown / Terracotta)", "B": "亮粉紅色", "C": "純白色", "D": "透明玻璃色"},
         "A", "Underground gravity drainage pipes are coloured golden brown/terracotta. This universal colour coding allows groundworkers and excavators to immediately identify drainage pipes in trenches.", "地下排水管專用橘褐色：英國地上立管一般是灰色或黑色；一旦鑽入地下，埋地排污管統一全是醒目的「陶土橘褐色 (Terracotta)」。挖土機挖開土方一眼就能認出這是排污管道，防誤挖挖爆！", "BS EN 1401-1 Plastics piping systems for underground drainage; C&G Unit 206"),

        # 49. Minimum gradient for 110mm underground foul drains
        ("9.2",
         "Under Building Regulations Approved Document H1 Section 2, what is the MINIMUM recommended gradient for an underground 110mm foul drain serving a domestic dwelling?",
         "根據英國建築法規 Approved Document H1 第 2 節規定，連接家庭住宅的 110mm 地下排污暗管，推薦敷設的「最小排水坡度」是多少？",
         {"A": "1:80 (approx 12.5mm fall per meter) or steeper (e.g. 1:40), provided flow velocity is sufficient", "B": "1:1000", "C": "1:1 (45-degree angle)", "D": "Completely flat (1:0)"},
         {"A": "1:80 (即每米下坡約 12.5mm)，在流量充足時推薦採用 1:40 (每米 25mm)", "B": "1:1000 極緩坡", "C": "1:1 垂直急坡", "D": "完全零坡度絕對水平"},
         "A", "Approved Document H1 permits 110mm foul drains to be laid at 1:80 (or 1:40 for low flow/single WC). This ensures self-cleansing velocity of at least 0.75 m/s to prevent solids settling.", "地下 110mm 排污坡度（1:80 至 1:40）：地下排水全靠重力自潔！坡度至少保證 1:80（每米落 12.5mm）；如果只接了一個馬桶流量較小，推薦做成 1:40（每米落 25mm），保證流速超 0.75m/s 衝走糞渣。", "Building Regulations Approved Document H1 Table 6; BS EN 752"),

        # 50. Minimum gradient for 160mm underground drains
        ("9.2",
         "Under Approved Document H1, what is the minimum permissible gradient for a larger 160mm (6-inch) underground foul drain serving multiple properties?",
         "根據 Approved Document H1 規定，服務於多戶家庭的更大口徑 160mm（6 英寸）地下排污主管，允許採用的最小設計坡度是多少？",
         {"A": "1:150 (approx 6.7mm fall per meter)", "B": "1:10", "C": "1:1", "D": "1:5000"},
         {"A": "1:150 (即每米均勻下坡約 6.7mm)", "B": "1:10", "C": "1:1", "D": "1:5000"},
         "A", "Larger pipes with greater sustained water volume maintain hydraulic self-cleansing velocity at shallower falls. A 160mm drain requires a minimum gradient of 1:150.", "大管徑坡度規律：管子越粗、集中匯水流量越大，水力水力半徑越大，阻力相對越小。因此 160mm 主管的坡度可以放緩到 1:150，依然能保持足夠的流速衝刷泥沙。", "Building Regulations Approved Document H1 Table 6; BS EN 752"),

        # 51. Bedding and haunching pea shingle
        ("9.2",
         "Under Approved Document H1 and BS EN 1610, what bedding specification is required beneath flexible 110mm PVC-U pipes in a typical trench excavation?",
         "根據 Approved Document H1 及 BS EN 1610 規定，在管溝中鋪設 110mm PVC-U 柔性塑料地下排水管時，管底支撐墊層（Bedding）的標準規格是什麼？",
         {"A": "Large jagged boulders and broken bricks", "B": "A minimum 100mm uniform bed of granular material (such as 10mm single-sized pea gravel / crushed stone conforming to BS EN 12620)", "C": "Soft garden peat soil", "D": "Pipes placed directly on jagged rock without bedding"},
         {"A": "大塊尖銳巨石與建築碎磚頭", "B": "厚度至少 100mm 的均勻粒料墊層（如符合 BS EN 12620 標準的 10mm 單一粒徑洗淨豌豆石子 / 碎石沙粒）", "C": "鬆軟的花園草炭土", "D": "不作任何墊層，直接將管子硬砸在尖銳岩石上"},
         "B", "Flexible plastic pipes rely on uniform support. A 100mm pea shingle bed prevents point loads from puncturing the pipe wall and allows accurate fall alignment before haunching.", "管底 100mm 豆石墊層必考：塑料管身柔韌，若直接扔在碎石溝底，尖銳石頭會像刀子一樣刺破管壁！必須鋪一層 10 公分厚、圓滾滾乾淨的 10mm 小豆石（Pea Shingle），管子坐上去受力均勻無比。", "Building Regulations Approved Document H1 Section 2.41; BS EN 1610"),

        # 52. Backfilling and side-fill surround
        ("9.2",
         "When backfilling around a flexible underground drainage pipe with pea gravel, how far above the crown (top) of the pipe should the granular material extend before normal trench spoil is backfilled?",
         "在管溝中用豆石顆粒材料對柔性地下排水管實施「兩側護管（Haunching）與管頂覆蓋」時，粒料必須高出管頂（Crown）至少多少高度後方可回填原生土？",
         {"A": "At least 100mm above the crown of the pipe", "B": "Directly flush with the garden surface 3 meters up", "C": "Zero mm (stop at the pipe centerline)", "D": "50 meters"},
         {"A": "至少高出管頂外表面（Crown）「100mm (10 公分)」以上", "B": "一路全部填滿石子直至 3 米高的花園地表", "C": "0 mm (石子只填到管子半腰中心線)", "D": "50 米"},
         "B", "The pipe must be enveloped in pea shingle to at least 100mm above its crown. This protective surround shields the pipe from heavy stones and compaction shocks when backfilling the trench.", "石子覆蓋超管頂 100mm：石子不僅要塞滿管子兩側腰部（Haunching），還必須厚厚蓋過管頂 10 公分！形成一個全方位的保護石子外殼後，上方才能倒回大泥土和夯實，絕不砸癟管道。", "Building Regulations Approved Document H1 Section 2.42; BS EN 1610 Construction of drains"),

        # 53. Protection of pipes under shallow cover
        ("9.2",
         "Under Approved Document H1, what structural protection is required for an underground drainage pipe laid beneath a vehicular driveway with LESS than 600mm of cover to the finished surface?",
         "根據 Approved Document H1 規定，當地下排水管道穿越車行車道下方、且管頂至完成面地表的埋深「不足 600mm」時，必須採取何種抗壓結構保護措施？",
         {"A": "Leave the pipe bare", "B": "Reinforced concrete paving slabs bridging over the trench with a compressible layer, or full mass concrete encasement (minimum 100mm all round) with flexible joints", "C": "Paint the pipe with silver paint", "D": "Remove the pipe entirely"},
         {"A": "完全不作任何防護措施", "B": "在管溝上方架設跨越受力的鋼筋混凝土抗壓板（下墊可壓縮隔震層），或對管道實施全斷面混凝土包封（四週混凝土厚度至少 100mm，並在接頭處預留柔性膨脹縫）", "C": "在塑料管外表面刷一層銀粉漆", "D": "徹底拆除該排水管道"},
         "B", "Heavy vehicles exert intense dynamic wheel loads. Shallow pipes (<600mm) will crush without protection. Bridging slabs or concrete encasement deflect heavy axle loads into stable trench walls.", "淺埋行車過車防爆防護：車道上卡車好幾噸重！埋深若小於 60 公分，車輪碾壓直接把塑料管踩扁壓爆！必須打一圈混凝土厚外殼（Concrete encasement）或在溝頂架設鋼筋混凝土跨越蓋板，把重壓分散到兩側硬土層。", "Building Regulations Approved Document H1 Section 2.44; BS EN 1610"),

        # 54. Pipes passing through external walls
        ("9.2",
         "When an underground drainage pipe passes through an external load-bearing masonry wall, how must the penetration be constructed under Approved Document H1 to accommodate differential settlement?",
         "當地下排水管道穿過建築物外圍承重磚牆基礎時，根據 Approved Document H1 規範，穿牆孔洞應當如何構造以適應房屋與管網的不均勻沉降？",
         {"A": "Brick the pipe rigidly tight into the wall with mortar", "B": "Build an opening lintel bridging over the pipe with a minimum 50mm clearance all round (masked with flexible sheet material), or install short 'Rocker Pipes' (max 600mm) with flexible joints adjacent to the wall", "C": "Chop the pipe off at the wall face", "D": "Glue the pipe to the bricks"},
         {"A": "用高標號水泥砂漿將管子死死砌死在磚牆孔洞裡", "B": "在管道上方砌築承重過梁（Lintel），四周預留至少 50mm 的自由沉降淨空縫隙（外蒙柔性密封板）；或在距牆面 150mm 內安裝短節「搖擺管 (Rocker Pipe，長度不超 600mm)」配備柔性接頭", "C": "在牆面處把水管切斷", "D": "用強力膠水將塑料管與紅磚粘在一起"},
         "B", "Buildings settle into soil over time; drainage pipes move independently. Mortaring a pipe rigid into a foundation wall will snap the pipe in shear. Rocker pipes or bridged lintels prevent sheared pipes.", "穿牆沉降斷管預防：房屋自重大地基天天在下沉，而室外排污管躺在土裡不動。若把管子用水泥糊死在牆裡，沉降力會像鍘刀一樣把塑料管咔嚓剪斷！必須做過梁留 50mm 縫、或接兩節 600mm 搖擺短管吸收沉降差。", "Building Regulations Approved Document H1 Section 2.52; NHBC Chapter 5.3"),

        # 55. Inspection chamber spacing and max depth
        ("9.2",
         "Under Approved Document H1 Table 11, what is the MAXIMUM depth permitted for a standard 450mm diameter plastic non-man-entry Inspection Chamber?",
         "根據 Approved Document H1 表 11 規定，標準 450mm 直徑的塑料「非人員進入型地面檢查井 (Inspection Chamber)」允許開挖的「最大安裝深度」是多少？",
         {"A": "Maximum 1.2 meters depth (or up to 3.0m if fitted with a restrictor ring preventing human access)", "B": "Maximum 50 meters", "C": "100 millimeters only", "D": "Unlimited depth"},
         {"A": "最大深度 1.2 米 (若井口加裝小於 350mm 的防墜落防鑽入收口限制環，則可深至 3.0 米)", "B": "最大深度 50 米", "C": "僅限 100 毫米深度", "D": "深度沒有任何限制"},
         "A", "Plastic mini-chambers allow rodding from ground level. Beyond 1.2m, reaching rods becomes difficult, and to prevent children falling into 450mm shafts, a 350mm restrictor ring is mandatory down to 3m.", "450mm 塑料檢查井深度極限：常規下水井最大深 1.2 米，拿疏通杆站在地面就能捅通。若超過 1.2 米（最深至 3 米），井口必須套上縮口防護環（孔徑收窄到 350mm），防止小孩或工人不慎失足跌落窒息井底。", "Building Regulations Approved Document H1 Table 11; BS EN 13598"),

        # 56. Internal inspection chamber covers
        ("9.2",
         "When an underground foul drainage inspection chamber MUST be located internally inside a habitable room or commercial building, what specification of cover is LEGALLY MANDATORY under Approved Document H1?",
         "當地下排污管道檢查井「必須安裝在有人居住的室內或商業建築地面下方」時，根據法規規定，井蓋構造有何強制性法律要求？",
         {"A": "A loose wooden timber board", "B": "An airtight, mechanically screw-down, double-sealed cover and frame (grease/rubber sealed) with secure lifting keys", "C": "An open iron grate allowing air to circulate into the bedroom", "D": "No cover is permitted"},
         {"A": "隨意搭蓋一塊鬆垮的木板", "B": "機械螺絲擰緊鎖定、帶有雙道橡膠密封圈/潤滑脂的「氣密型重型螺栓封閉井蓋與底座 (Airtight Double-Sealed Cover)」", "C": "通風透氣、任由下水道氣體竄入臥室的開口式鐵篦子", "D": "法規禁止安裝任何蓋子"},
         "B", "Internal chambers are a major hazard. Sewer gases (methane, toxic H2S) or sewer surcharge could invade the living space. Covers inside buildings must be mechanically bolted with dual gas-tight seals.", "室內下水井蓋安全大忌：客廳廚房地板底下若有檢查井，絕對嚴禁隨便扣個蓋子！必須採用「雙膠條機械螺栓鎖死氣密井蓋」。四角螺絲死死咬緊，萬一下水道倒反水、或毒氣瀰漫，絕對封死在地下，一絲臭氣都進不來。", "Building Regulations Approved Document H1 Section 2.49; BS EN 124"),

        # 57. Air test on underground drainage
        ("9.2",
         "Under BS EN 1610 and Approved Document H1, what is the procedure and pass criteria for an on-site 'Air Pressure Test' on a newly laid underground foul drainage pipe run?",
         "根據 BS EN 1610 及 Approved Document H1 規定，對新鋪設的地下排污管道實施「現場氣密性打氣試驗 (Air Test)」時，標準的測試步驟與合格判斷標準是什麼？",
         {"A": "Pump air until the pipes explode", "B": "Plug all open pipe ends, pump air via a hand bulb until a U-tube water manometer reads 100mm water gauge (WG), wait 5 mins for stabilization, then the pressure must not fall below 75mm WG over a subsequent 5-minute test period", "C": "Blow into the pipe with human breath for 2 seconds", "D": "No pressure drop is allowed within 1 second"},
         {"A": "持續打氣加壓直到管道爆炸為止", "B": "封堵全部管口，拿皮虎打氣至 U 型水柱壓力計讀數達到 100mm 水柱高度，靜置 5 分鐘待氣溫穩定，隨後在正式記錄的 5 分鐘測試期內，水柱高度下降不得超過 25mm（即讀數不得跌破 75mm WG）", "C": "用嘴對著管子吹氣 2 秒鐘", "D": "在 1 秒鐘內不允許有任何微小壓降"},
         "B", "Air test criteria: Pump to 100mm WG. Max allowable drop is 25mm over 5 minutes (remaining ≥75mm WG). A drop exceeding 25mm indicates loose joint seals, cracked pipes, or displaced rubber rings.", "排水氣密打壓必考標準：U 型管水柱打到 100mm 高！等 5 分鐘讓空氣冷卻；隨後看 5 分鐘，水柱下降嚴禁超 25mm（指針必須穩在 75mm 以上）為合格。若指針狂掉，說明橡膠圈沒插好或管壁有暗裂！", "Building Regulations Approved Document H1 Section 2.60; BS EN 1610"),

        # 58. Water test on underground drainage
        ("9.2",
         "Under Approved Document H1, what test head of water is applied when performing an on-site 'Water Test' on a section of newly laid underground drainage pipework?",
         "在對新裝地下排水管道實施更嚴苛的「現場充水水壓閉水試驗 (Water Test)」時，管道最高端應當承受多少試驗靜水水頭（Head of Water）？",
         {"A": "Filled to provide a minimum 1.5-meter head of water (15 kPa) above the invert at the top end (and max 2.4-meter head at the low end)", "B": "100 meters head of water", "C": "1 millimeter of water", "D": "Boiling water only"},
         {"A": "注水至管道最高端管底內表面（Invert）上方至少承受 1.5 米靜水頭壓力 (15 kPa)，且最低端受壓不超過 2.4 米水頭", "B": "100 米超高壓水頭", "C": "1 毫米微量存水", "D": "僅能使用沸騰熱水試驗"},
         "B", "Water testing applies 1.5m to 2.4m head of water. Plugs are fitted at both ends and an elbow tube rises 1.5m at the upper manhole. Water is left to condition for 2 hours, topped up, then monitored for 30 mins.", "閉水打水試驗標準：兩頭堵死，上頭豎起管子灌水灌到 1.5 米高水柱！塑料管泡水靜置半小時排盡氣泡，補滿水刻度；隨後觀測 30 分鐘，測量漏水量是否在每米管道允許的幾十毫升微量極限內。", "Building Regulations Approved Document H1 Section 2.61; BS EN 1610"),

        # 59. Urinal automatic siphonic flush cistern
        ("9.2",
         "Under the Water Supply (Water Fittings) Regulations 1999, what automatic control device is legally required to restrict water consumption on an auto-flush urinal cistern in a public building?",
         "根據英國 1999 水法規規定，在公共衛生間的自動虹吸小便器衝水水箱供水管路上，必須強制加裝何種節水控制裝置？",
         {"A": "A continuous free-flowing open tap", "B": "An automatic time-controlled solenoid valve or a Passive Infrared (PIR) presence sensor valve that stops flushing when the building is unoccupied", "C": "A coin-operated lock on the pipe", "D": "No controls permitted"},
         {"A": "完全不設防、24 小時晝夜長流水的直通水龍頭", "B": "自動定時電磁閥或人體被動紅外（PIR）感應閥門，在夜間或建築物無人使用期間自動切斷補水停止沖洗", "C": "在水管上加裝投幣投幣鎖", "D": "法規禁止安裝任何控制閥"},
         "B", "Uncontrolled auto-siphons flush every 15-20 minutes 24/7/365, wasting up to 100,000 litres of clean drinking water annually in empty schools or offices. Water Regs mandate occupancy sensors.", "小便池節水死命令：老式虹吸水箱不管白天黑夜每 15 分鐘自己嘩嘩衝一次，一年在空樓裡白白衝掉幾十噸自來水！水法規強制加裝紅外 PIR 感應閥：有人進廁所才開水充水，人走樓空自動關閉水路，極致節水！", "Water Supply (Water Fittings) Regulations 1999 Schedule 2 Section 10; C&G Unit 206"),

        # 60. Waterless urinals
        ("9.2",
         "How does a 'Waterless Urinal' operate without requiring any flushing water while completely eliminating foul sewer odors?",
         "現代環保「無水小便斗 (Waterless Urinal)」在完全不消耗一滴自來水沖洗的前提下，是如何阻隔下水道惡臭返味的？",
         {"A": "It burns urine with a gas flame", "B": "It utilizes a replaceable cartridge containing a scented sealant liquid (lighter than urine) or a one-way silicone valve; urine passes through easily, while the barrier seals out all sewer gases", "C": "It freezes waste with electricity", "D": "It exhausts air with a loud turbine"},
         {"A": "利用燃氣明火將尿液當場高溫焚化", "B": "利用可更換的專用濾芯，內裝比重比尿液更輕的專用天然芳香隔離密封液（或一向單向自閉硅膠瓣）；尿液下沉穿透流入下水道，漂浮在頂部的隔離液將下水道惡臭 100% 封閉在下方", "C": "利用電力將排泄物急凍成冰", "D": "自帶大功率高速渦輪風機向外抽風"},
         "B", "The barrier liquid floats on top because its relative density is lower than urine. Urine sinks through the liquid, but foul air cannot penetrate upwards through the oily liquid seal.", "無水小便斗浮油阻臭黑科技：油比水輕！特製的藍色密封油浮在濾芯最上層。人體尿液密度大，自動穿過油層漏入排污管；而下水道臭氣卻絕對穿不透這層浮油屏障，一年能為大樓省下幾十萬升自來水！", "BS 6465-1 Sanitary installations; Armitage Shanks / Urimat Technical Guides"),

        # 61. WC pan connector types
        ("9.2",
         "When connecting a modern horizontal-outlet WC pan (P-trap spigot) into an underground drainage pipe socket in the floor slightly misaligned with the pan spigot, which pan connector fitting is used?",
         "當現代後排橫出水馬桶（P-trap）的出水管接嘴、與木地板下方預留的排污管插口中心線存在 20mm 至 40mm 的微小中心距偏差時，水暖工應當選用何種專用馬桶連接器？",
         {"A": "A straight rigid connector forced with a hammer", "B": "An Offset Pan Connector (providing a factory-molded 20mm or 40mm offset throw) or an approved Flexible Extendable Pan Connector", "C": "A soft paper towel roll", "D": "A copper elbow soldered tight"},
         {"A": "拿直口硬質接頭用鐵錘強行歪扭敲進去", "B": "偏心馬桶連接器 (Offset Pan Connector - 出廠預設 20mm 或 40mm 偏心錯位)，或經認證的柔性伸縮可變形馬桶排污管", "C": "一捲衛生紙紙巾紙筒", "D": "紫銅彎頭高溫焊死"},
         "B", "Offset pan connectors allow up to 40mm misalignment adjustment without placing mechanical shearing stress on the fragile ceramic toilet spigot. Flexible finned connectors provide multi-angle alignment.", "馬桶對位偏心接頭：瓷磚貼完，往往發現地面排污管口比馬桶後屁股偏了兩三公分，硬懟會把馬桶陶瓷嘴崩裂！選用 20mm 或 40mm 的偏心彎頭，轉個角度正好嚴絲合縫套入，橡膠多層密封翅片死死密封。", "BS 5627 Plastics connectors for water closets; McAlpine Plumbing Catalog"),

        # 62. Wall-hung WC structural frame load rating
        ("9.2",
         "Under British Standards BS EN 997 and BS EN 14055, what minimum static structural load must a wall-hung WC steel frame (such as a Geberit Duofix frame) safely support without failure or detachment?",
         "根據英國/歐洲標準 BS EN 997 及 BS EN 14055，暗裝壁掛式馬桶鋼結構支撐承重架（如 Geberit Duofix 鋼架），法規強制要求必須能夠安全承受多大的靜態測試載荷？",
         {"A": "At least 400 kg (4.0 kN / approx 63 stone)", "B": "Only 5 kg", "C": "100,000 kg", "D": "No load capacity required"},
         {"A": "至少 400 公斤 (4.0 kN 靜止載荷，約合 63 英石)", "B": "僅需承受 5 公斤", "C": "100,000 公斤重載", "D": "完全不需要任何承重標準要求"},
         "A", "Wall-hung toilet frames are tested to hold a static test load of 400 kg (4 kN) applied to the front edge of the pan. This guarantees the toilet will never tear off the wall, even under heavy occupant loads.", "壁掛馬桶 400 公斤安全紅線：很多人擔心懸空馬桶坐塌摔傷。歐洲標準極其變態：剛性鋼架在出廠認證時，馬桶前端懸臂處死死壓上 400 公斤（四個壯漢自重）重物保持不變形，結實如坦克！", "BS EN 997 WC pans with integral trap; Geberit Duofix Specification"),

        # 63. Anti-flood backwater valves
        ("9.2",
         "What is an 'Anti-Flood Backwater Valve' (conforming to BS EN 13564) installed in low-lying basement drainage runs, and what disaster does it prevent?",
         "安裝在低窪地下室排污管道上的「防倒灌止回閥 (Anti-Flood Backwater Valve - 符合 BS EN 13564)」，能夠防止何種災難性洪澇事故？",
         {"A": "It stops cold air freezing the kitchen floor", "B": "It contains one or two automatic mechanical non-return flaps (and a manual emergency shut-off lock) that allow domestic sewage to flow outward, but automatically snap shut if external municipal sewers surcharge, preventing backflow of raw sewage into the basement", "C": "It cleans drinking water", "D": "It pumps gas into the sewer"},
         {"A": "阻擋室外冷空氣凍結廚房地板", "B": "內置一道或雙道自動機械單向防倒灌閥瓣（外加人工手動應急鎖死板）：平時家庭污水順暢向外排放，一旦暴雨時市政大下水道水位暴漲倒灌，閥瓣被倒流水壓自動拍死封閉，杜絕公共糞水淹沒地下室", "C": "淨化自來水供人直飲", "D": "向地下管道內部強行注射天然氣"},
         "B", "In low-lying flood plains or basements below street level, surcharged municipal sewers push millions of gallons of black sewage backward into homes. Backwater valves slam shut to isolate the property.", "地下室防反水救命閥：遇上百年一遇暴雨，街上公共下水道憋爆，污水會順著下水管瘋狂倒灌進地勢低的半地下室！裝上防倒灌閥，一旦水流反向，不銹鋼擋板立刻自動落下卡死，保住全家幾十萬豪華裝修。", "BS EN 13564 Anti-flooding devices for buildings; Approved Document H1"),

        # 64. Grease traps for commercial kitchens
        ("9.2",
         "Under Building Regulations Approved Document H1 Section 2.21, why are commercial food establishments (restaurants, hotels, canteens) legally required to install a certified 'Grease Separator' (Grease Trap)?",
         "根據英國建築法規 Approved Document H1 第 2.21 節規定，為什麼所有商業餐飲場所（餐廳、酒店、學校食堂）在排入下水道前被法律強制要求加裝經過認證的「隔油池 / 隔油器 (Grease Trap)」？",
         {"A": "To extract motor oil for sports cars", "B": "To cool and separate Fats, Oils, and Grease (FOG) by gravity flotation before they enter public sewers, preventing fat solidification from forming catastrophic massive 'Fatbergs' that choke municipal sewer networks", "C": "To flavour cooking soups", "D": "To generate steam power"},
         {"A": "提煉機油供跑車使用", "B": "在熱洗碗水排入公共下水道前，通過重力浮選冷卻技術將浮油、動物脂肪與餐飲油脂（FOG）攔截撇除，杜絕油脂在冰冷公共管道中硬化板結生成堵死整條街的巨型「下水道油脂山 (Fatbergs)」", "C": "用提取的廢油為廚房煲湯調味", "D": "利用油脂餘熱產生蒸汽發電"},
         "B", "Hot liquid animal fat congeals into rock-hard white lard when meeting cold sewer walls. Mixed with wet wipes, this forms multi-ton 'fatbergs' costing millions to clear. Grease traps capture FOG at source.", "嚴打餐飲下水道油脂山（Fatbergs）：倫敦下水道曾挖出過重達幾百噸、長達幾百米的巨大油脂山！全是餐廳倒的熱油在地下凝結，像水泥一樣堵死整條街。法規強制餐飲店必須裝隔油池，定期撈油回收！", "Building Regulations Approved Document H1 Section 2.21; BS EN 1825"),

        # 65. Petrol and oil interceptors
        ("9.2",
         "Under Environment Agency PPG3 guidelines and BS EN 858, what type of interceptor is legally required for surface water drainage discharging from petrol filling stations and commercial car parks?",
         "根據英國環境署（EA）PPG3 治污指南與 BS EN 858 標準，在加油站前庭廣場與大型商用停車場的地面雨水排放管道上，必須強制安裝何種環保設施？",
         {"A": "A domestic washing machine", "B": "A Class 1 Full Retention (or Bypass) Petrol/Oil Interceptor featuring automatic closure devices and coalescing foam coalescers", "C": "A wooden water tub", "D": "No environmental protection is required"},
         {"A": "家用滾筒洗衣機", "B": "一級全截留型（Class 1 Full Retention）或旁通型油水分離攔截井 (Petrol/Oil Interceptor)，自帶自動浮子切斷保護閥與聚結填料板", "C": "敞開式木質洗腳盆", "D": "不需要安裝任何環境保護設備"},
         "B", "Fuel spills and dripped engine oil washed down yard drains would poison natural rivers. Class 1 separators strip oil down to <5 mg/litre using coalescing media and automatic drop-valves.", "加油站隔油井環保底線：雨水沖洗停車場帶有劇毒汽油機油。若直排河道會毒死整條河的魚蝦！Class 1 隔油井讓油水分離，油浮在水面，水下排；一旦浮油過厚，自動浮球落座鎖死排污口，環保局定期抽查！", "BS EN 858 Separator systems for light liquids; Environment Agency PPG3"),

        # 66. Cesspools vs Septic Tanks vs Treatment Plants
        ("9.2",
         "What is the fundamental engineering difference between an impervious 'Cesspool' and a 'Septic Tank' in rural off-mains sanitation?",
         "在遠離市政下水道的英國偏遠鄉村非管網排污工程中，「完全密封化糞集水坑 (Cesspool)」與「兩格式生物化糞池 (Septic Tank)」有何本質的工程原理區別？",
         {"A": "Cesspools clean water to bottled quality; septic tanks do not", "B": "A cesspool is a completely sealed holding chamber that stores all raw sewage with zero treatment or discharge (requiring frequent tanker pumping), whereas a septic tank partially clarifies sewage via anaerobic digestion and discharges settled liquid effluent to a ground drainage infiltration field", "C": "There is no difference", "D": "Cesspools are built in clouds"},
         {"A": "集水坑能將污水淨化到礦泉水直飲標準；化糞池則不能", "B": "Cesspool 是個「完全密封只存不排」的死大罐，對污水不做任何排放，幾週注滿後必須花重金叫吸糞車抽走；而 Septic Tank 是「帶消化排放的沉澱池」，黑水在池內厭氧分解沉澱後，清亮溢流水排入花園地下滲濾田消納", "C": "兩者完全是同一種設備的不同叫法", "D": "集水坑是建造在大氣雲層中的"},
         "B", "Cesspools only hold waste until full (costly emptyings). Septic tanks settle solids, digest organic matter anaerobically, and discharge liquid effluent into underground subsoil drainage mounds.", "Cesspool 與 Septic Tank 區別必考：Cesspool 就是個死密封大水桶，全家人大便全裝裡面，一滿了就要花幾百鎊叫抽糞車來抽！Septic Tank 是活的：大便沉底被細菌吃了爛成灰，上層水慢慢滲進地下石子田回歸自然。", "Building Regulations Approved Document H2 Section 1; BS 6297"),

        # 67. Package Sewage Treatment Plants
        ("9.2",
         "Under Environment Agency General Binding Rules and BS EN 12566-3, what is the superior performance of a modern 'Package Sewage Treatment Plant' compared to a traditional septic tank?",
         "根據英國環境署（EA）法規與 BS EN 12566-3 標準，現代「一體化微動力污水生化處理裝置 (Package Sewage Treatment Plant)」，相比於傳統老式化糞池具有何種突破性的淨化效能？",
         {"A": "It converts sewage into solid gold bricks", "B": "It utilizes active powered aeration (mechanical compressors or rotating discs) to cultivate aerobic bacteria, producing clean, non-polluting treated effluent that can legally discharge directly into a flowing river or stream without an infiltration field", "C": "It generates radioactive steam", "D": "It cools the air"},
         {"A": "能將糞便污水全自動提煉成純金金磚", "B": "利用微型氣泵主動強制曝氣（Aeration）高效培養好氧微生物，將有機物徹底生化分解氧化，排出的出水清澈透明無污染，被法律允許直接合法排入天然流動河流小溪中（無需土壤滲透田）", "C": "會向環境釋放放射性蒸汽", "D": "為周圍空氣強制降溫"},
         "B", "Treatment plants use electric air blowers to supercharge aerobic digestion. The effluent is clean (BOD <20mg/L, Suspended Solids <30mg/L), permitting legal discharge into local watercourses under EA rules.", "一體化污水處理器（微動力神機）：老式化糞池出水發臭，嚴禁直接排入河流！現代污水罐插電打氧，好氧菌狂吃糞便，排出來的水像山泉水一樣清亮，達到英國環境署嚴苛排放標準，可以直接放進門口小河溝養魚！", "Environment Agency General Binding Rules for Small Sewage Discharges; BS EN 12566-3"),

        # 68. Rodding eyes and drain cleaning access
        ("9.2",
         "What is a 'Rodding Eye' (Clearing Access Point) installed at the head of a horizontal foul drain run, and what is its maintenance function?",
         "在地下排污平管起點頂端或轉彎盲端安裝的「清通孔 / 管道疏通檢查口 (Rodding Eye)」，具有何種關鍵的日常維護功能？",
         {"A": "A decorative post for hanging coats", "B": "A removable airtight threaded cap providing direct axial access into the pipe barrel for inserting flexible steel drain rods to clear obstructions downstream without digging up the garden", "C": "A periscope for watching worms", "D": "An entrance for pet cats"},
         {"A": "用作掛衣服大衣的裝飾金屬立柱", "B": "一個帶有橡膠密封螺紋的可拆卸檢修蓋口，允許水暖維護人員將柔性鋼質疏通杆（Drain Rods）順直直接插入管腔內部向前捅通堵塞物，無需大興土木開挖破壞花園草坪", "C": "用來觀測地下蚯蚓活動的潛望鏡", "D": "專為家養寵物貓進出的地下暗道"},
         "B", "Rodding eyes provide direct inline entry for mechanical rods. They must be positioned at changes of direction or gradient to allow rodding tools to push through to the next downstream inspection chamber.", "清通口（Rodding Eye）是水暖工的好朋友：下水管一堵，總不能把花園水泥砸開！在管道盡頭留個清通斜口，平時擰緊密封；堵了把蓋子擰開，接上十幾米長的疏通杆一節節捅進去，黑泥手紙瞬間捅散沖走！", "Building Regulations Approved Document H1 Section 2; BS EN 752"),

        # 69. High-pressure water jetting (HPWJ)
        ("9.2",
         "When clearing heavily encrusted fat, grease, and hard scale from underground foul drainage sewers, why is High-Pressure Water Jetting (HPWJ) preferred over manual drain rods?",
         "在清理地下排污管道內頑固板結的油脂塊、水垢與硬化泥沙死堵時，為什麼「高壓水射流射線清洗技術 (HPWJ)」遠遠優於手動金屬疏通杆？",
         {"A": "Manual rods make too much electricity", "B": "HPWJ uses specialized retro-thrust nozzles blasting water at 2,000 to 4,000 psi, which both propels the hose forward along the drain and scours the full 360-degree internal pipe wall surface back to bare plastic", "C": "HPWJ fills the pipes with dry sand", "D": "Manual rods are banned worldwide"},
         {"A": "手動疏通杆會自發產生危險的感應電", "B": "高壓水射流利用 2,000 至 4,000 psi（超 150-250 bar）的超高壓水流，通過後向噴射推進噴頭自動沿管道爬行，360 度全方位強烈剝離切割管壁上所有油脂硬垢，將管腔徹底洗淨恢復如新", "C": "高壓水槍會向管道灌入大量乾燥細沙", "D": "手動疏通杆在全世界已被全面禁止使用"},
         "B", "Manual rods only poke a small pencil-thin hole through blockages, which quickly clogs again. HPWJ retro-jets strip away all fats, scale, and tree roots, flushing them downstream cleanly.", "高壓水疏通是真乾淨：手動杆子只是在厚油泥中間捅個小窟窿，過兩天又糊死了；高壓水龍頭屁股後面有幾個倒噴水孔，像火箭推進一樣自己鑽進管道深處，暴烈水刀把管壁 360 度刮得乾乾淨淨，連老樹根都能切斷！", "Water Jetting Association (WJA) Code of Practice; C&G Unit 206"),

        # 70. Drain clearance rodding safety
        ("9.2",
         "When manually assembling and rotating flexible polypropylene drain rods inside an underground foul drainage pipe, in which direction must the rods ALWAYS be rotated?",
         "使用傳統螺紋連接的聚丙烯疏通杆（Drain Rods）在地下管道內旋轉疏通作業時，水暖工必須死死記住「始終朝哪個方向旋轉疏通杆」？",
         {"A": "Always clockwise (to the right)", "B": "Always anti-clockwise (to the left)", "C": "Direction does not matter", "D": "Rods must never be rotated"},
         {"A": "永遠只能朝「順時針方向 (Clockwise - 向右擰)」旋轉！", "B": "始終朝逆時針方向 (Anti-clockwise - 向左擰) 旋轉", "C": "旋轉方向無關緊要，隨意正反亂擰", "D": "疏通杆在任何情況下嚴禁有任何旋轉動作"},
         "A", "Plumbing safety rule: Standard drain rods screw together with right-hand clockwise threads. Rotating anti-clockwise unscrews the rods inside the pipe, leaving lost rods jammed underground requiring expensive excavation.", "捅下水道第一鐵律（只能順時針擰）：疏通杆全是一截截螺絲扣擰在一起的。在管道深處如果手欠逆時針轉了一下，前頭十幾米杆子直接脫扣斷在管子裡！掏不出來只能花幾千鎊把花園砸開挖土，血的教訓！", "C&G Unit 206 Safety and Drainage Practice; City & Guilds 6035 Textbook"),

        # 71. Kinetic water ram / plunger
        ("9.2",
         "What is the operational safety precaution when using a compressed-air 'Kinetic Water Ram' to clear a local blockage in a domestic sanitary waste pipe?",
         "在家庭衛生器具排水支管堵塞、使用壓縮空氣「動力管道衝擊槍 (Kinetic Water Ram)」實施氣壓衝擊疏通時，必須對周圍相鄰管口採取何種關鍵安全防護工藝？",
         {"A": "Open all taps fully to overflow the room", "B": "Firmly block and hold down all overflow openings and adjacent connected appliance wastes with damp cloths to prevent explosive blow-out of foul water into the technician's face", "C": "Heat the pipe with a gas torch", "D": "No precaution is necessary"},
         {"A": "將衛生間所有水龍頭全部開到最大", "B": "必須用厚濕抹布將該器具的溢水孔（Overflow）以及同一管路相鄰連通的所有其他下水口死死堵死壓牢，防止強烈衝擊氣波將惡臭污水和糞渣從溢水孔像散彈槍一樣爆噴糊滿一臉！", "C": "用動火焊槍把塑料下水管加熱", "D": "完全無需採取任何防護措施"},
         "B", "Kinetic rams generate a sudden shockwave through water. Open overflows or parallel basin traps act as relief vents, blasting contaminated black water straight out into the room unless sealed tight.", "衝擊槍防噴臉血淚教訓：水是不可壓縮的！氣壓槍打出一記重拳，衝擊波在水裡傳導，如果你忘了堵洗手盆上面的溢水小孔，整管黑臭泥湯會瞬間從溢水孔噴出兩米高，糊得技師滿頭滿臉！必須用濕布按死所有孔！", "C&G Unit 206 Drainage Maintenance Tools"),

        # 72. Siphonic WC pans
        ("9.2",
         "How did a traditional double-trap siphonic WC pan achieve its powerful flush action?",
         "在英國傳統「雙水封虹吸式坐便器 (Double-Trap Siphonic WC)」中，它是如何利用雙重水封在馬桶內部產生強大虹吸抽吸力的？",
         {"A": "It used a gasoline engine", "B": "Flushing water passing through an aspirator nozzle created a low-pressure vacuum between the first and second water seals, triggering an immediate powerful siphonic pull that extracted pan contents", "C": "It boiled the water", "D": "It used dry powder"},
         {"A": "利用微型汽油發動機抽吸", "B": "衝水水流穿過射流抽氣噴嘴時，在第一道水封與第二道水封之間的夾層密閉腔內產生負壓真空，瞬間誘發強勁的虹吸效應將整個馬桶便池內的污物排空吸入管道中", "C": "將池內存水加熱沸騰", "D": "利用乾燥化學粉末滅火"},
         "B", "Double trap siphonic pans used an aspirator to evacuate air between the two traps, dropping pressure and creating a ferocious siphonic vortex. They have largely been superseded by washdown pans to save water.", "雙水封虹吸馬桶原理：前後兩個存水彎夾著一個密封空氣倉。水箱水一衝，射流器把夾層空氣抽走形成真空，馬桶像龍捲風吸盤一樣把大便瞬間吸光！缺點是結構複雜且極費水，現代多改用節水衝落式。", "BS 5503 Specification for vitreous china washdown and siphonic WC pans; C&G Unit 206"),

        # 73. Washdown WC pans
        ("9.2",
         "What is the operational mechanism of a modern standard domestic 'Washdown' WC pan?",
         "現代普遍採用的標準家庭「衝落式直衝坐便器 (Washdown WC Pan)」的工作機制是什麼？",
         {"A": "Sewage is dissolved by chemicals", "B": "The kinetic gravitational force and swirling turbulence of the incoming flush water cascades around the rim and directly drives waste out over the trap weir by momentum", "C": "An electric elevator lifts waste out", "D": "It uses compressed gas cylinders"},
         {"A": "利用高濃度化學藥劑將固體排泄物溶解", "B": "完全依靠水箱水流下墜時的天然「重力勢能、衝刷動能與環形出水孔水流紊流」，直接將池內糞便以物理推力推過存水彎溢流堰口進入立管", "C": "利用小型電動升降機將污物提升出池", "D": "依賴高壓壓縮氣瓶推動"},
         "B", "Washdown pans rely on water momentum from the cistern to push solids over the trap weir into the soil pipe. Washdown pans operate efficiently with low water volumes (4 to 6 litres).", "衝落式馬桶（Washdown）是全球主流：原理簡單粗暴——水從高處落下轉化為巨大動能，水流順著馬桶圈小孔噴出，像瀑布一樣把糞便硬生生推過存水彎。沒有任何死角、不怕卡頭髮，4 升小水量就能衝乾淨！", "BS EN 997 WC pans and WC suites with integral trap; C&G Unit 206"),

        # 74. Rimless WC technology
        ("9.2",
         "What is the sanitary and hygiene advantage of modern 'Rimless' WC pans compared to traditional boxed-rim pans?",
         "相比於傳統帶有內捲回折箱形衝水圈的老式馬桶，現代廣泛推廣的「無邊框/無水圈坐便器 (Rimless WC)」具有何種革命性的衛生優勢？",
         {"A": "Rimless toilets produce ice", "B": "The smooth internal ceramic contour eliminates hidden, unglazed crevices beneath the rim where bacteria, lime scale, and fecal deposits accumulate, allowing 100% surface visibility and effortless wipe-clean hygiene", "C": "They eliminate the need for water", "D": "They weigh 500 kg"},
         {"A": "無圈馬桶在衝水時能自發製造冰塊", "B": "光滑平整的內壁流線型陶瓷構造徹底消除了老式馬桶邊緣暗藏、未施釉的藏污納垢死角，杜絕了細菌、尿鹼水垢和黑霉斑的滋生堆積，實現了 100% 全面可視且一擦即淨的極致衛生", "C": "完全不需要使用任何自來水沖洗", "D": "馬桶自重高達 500 公斤"},
         "B", "Traditional box-rims conceal hard-to-clean crevices that harbour germs. Rimless bowls shoot water smoothly around an open, fully glazed contour, delivering superior hygiene with no hidden ledges.", "無邊框（Rimless）衛生革命：老馬桶邊緣底下有個向內凹的小溝槽，刷子伸不進去，久而久之裡面積滿發黑發黃的尿垢惡臭不堪！無邊框馬桶光溜溜沒有任何死角，水流像海浪一樣全覆蓋旋洗，抹布一擦乾淨如新！", "BS EN 997; Ideal Standard / Twyford Technical Innovation Guides"),

        # 75. Soil stack cowl vs weather slate
        ("9.2",
         "When an open soil and vent stack penetrates through a pitched slate roof to outside atmosphere, what roofing component ensures a 100% watertight roof penetration?",
         "當敞開式排污通氣立管穿透斜屋面石板瓦排向室外大氣時，水暖工在屋頂瓦面處必須安裝何種構件以確保屋面穿管部位 100% 絕對防水防漏雨？",
         {"A": "Wrap the pipe with duct tape", "B": "A Lead Roof Slate (Lead Weather Slate with a welded lead sleeve or flexible EPDM flashing cone) interlaced into the slate courses", "C": "Pour loose cement on the slates", "D": "No flashing is needed"},
         {"A": "拿普通布基膠帶纏繞穿牆孔隙", "B": "鉛板穿管防雨瓦 (Lead Weather Slate - 帶有焊接一體化鉛筒護套或耐候 EPDM 彈性密封錐套的純鉛瓦片)，插疊編織進屋頂瓦片排水層中", "C": "在瓦片表面直接傾倒鬆散的水泥砂漿", "D": "穿孔處完全不需要做任何防水泛水處理"},
         "B", "A lead weather slate incorporates a flat lead base woven into surrounding roof tiles and an upstand sleeve that clamps around the PVC pipe with a rubber weathering collar, shedding all rainwater.", "屋頂穿管防水鉛皮瓦（Weather Slate）：屋頂開洞最怕漏大雨！鉛皮瓦底板像魚鱗一樣深深插進瓦片底下，中間豎起一個鉛筒套住立管，管口扣上一個橡膠傘帽（Weathering collar）。雨水順瓦滑走，滴水不進閣樓！", "BS EN 12588; Lead Sheet Training Academy Manual; Approved Document H1"),

        # 76. Macerator installation electrical requirements
        ("9.2",
         "Under BS 7671 (IET Wiring Regulations), how must a domestic wastewater macerator pump (e.g. Saniflo) situated in a bathroom or cloakroom be connected to the electrical supply?",
         "根據英國電工法規 BS 7671（第 18 版），安裝在衛生間或洗手間內的污水粉碎提升器（Saniflo），必須通過何種規範方式接入室內供電線路？",
         {"A": "Plugged into a loose 13A socket next to the shower tray", "B": "Connected to an unswitched/switched 13A fused connection spur (FCU) located outside Zone 2, protected by a 30mA Residual Current Device (RCD)", "C": "Wired directly to the electric cooker cable", "D": "Powered by car battery clips"},
         {"A": "插在緊挨著淋浴房底盤旁邊的普通 13A 鬆動牆壁插座上", "B": "接入安裝在「防濺 2 區（Zone 2）以外安全區域」的 13A 熔斷保護接線支路（Fused Connection Unit - FCU），且該電路必須配備 30mA 剩餘電流動作保護器（RCD）", "C": "直接纏繞搭接在廚房大功率電磁灶的粗電纜上", "D": "使用汽車電瓶鱷魚夾供電"},
         "B", "Macerators must be permanently connected via a fused spur (typically outside zone 2 or outside the bathroom), protected by a 30mA RCD to protect occupants from fatal electric shock in wet conditions.", "粉碎泵電工安全規範：衛生間水汽大，嚴禁隨便插普通三腳插頭！粉碎泵必須走專用硬線接入帶保險絲的專用開關盒（FCU），且配電箱必須有 30mA 漏電保護器（RCD），防止電機泡水漏電擊死如廁人員！", "BS 7671:2018 Section 701; Saniflo Installation & Electrical Safety Instructions"),

        # 77. Soil stack offset guidelines
        ("9.2",
         "If an offset is unavoidable on a multi-storey vertical soil stack (to bypass an architectural beam), what design rules apply under Approved Document H1?",
         "因建築結構大樑避讓、導致多層建築排水立管必須在半腰做「管道拐彎錯位橫移 (Offset)」時，根據 Approved Document H1 規定，該錯位彎管有何嚴格水力設計限制？",
         {"A": "Use two sharp 90-degree knuckle elbows", "B": "Use large-radius bends (or 45-degree bends), and avoid connecting any sanitary appliances to the stack within 600mm above or below the offset", "C": "Reduce pipe diameter to 32mm", "D": "Turn the stack upside down"},
         {"A": "使用兩個急促的 90 度死角直角彎頭拐彎", "B": "必須採用大曲率順滑大彎（或 45 度鈍角彎），且在「錯位彎頭上方 600mm 及下方 600mm」範圍內，絕對嚴禁接入任何衛生器具排水支管！", "C": "在錯位處將立管管徑大幅縮減至 32mm", "D": "將整根立管倒置安裝"},
         "B", "Offsets create severe turbulent back-pressure as falling water hits the slope. Large-radius or 45° bends cushion flow. Sanitary connections are prohibited within 600mm of the offset to stop trap blow-out.", "立管錯位 600mm 禁接區必考：立管一旦橫移拐彎，水流從垂直變成斜衝，會在彎頭處激起劇烈的背壓氣囊！若在彎頭上下 60 公分內接了馬桶或地漏，衝擊波會把水封直接轟出！必須避讓 600mm 且用 45° 慢彎。", "Building Regulations Approved Document H1 Section 1.28; BS EN 12056-2"),

        # 78. Deep foul manhole safety
        ("9.2",
         "Under Confined Spaces Regulations 1997, what safety procedures are MANDATORY before a drainage engineer enters an underground foul drainage manhole deeper than 1.5 meters?",
         "根據英國 1997 年受限空間法規（Confined Spaces Regulations 1997），在排水工程師下入「深度超過 1.5 米的地下排污檢查井/人孔」作業之前，必須強制執行何種生命安全程序？",
         {"A": "Jump in immediately without informing anyone", "B": "Atmospheric gas testing (4-gas monitor for O2, CO, H2S, and LEL methane), continuous forced ventilation, safety harness with tripod recovery winch, and a trained top-man stationed at the surface", "C": "Smoke a cigarette to check for gas", "D": "Drink a glass of milk"},
         {"A": "在不通知任何人的情況下獨自直接跳入井底", "B": "實施嚴密氣體檢測（使用四合一便攜氣體探測儀檢測氧氣 O2、一氧化碳 CO、劇毒硫化氫 H2S 及可燃甲烷 LEL）、持續機械強行鼓風通風、佩戴全身安全吊帶配備三腳架救援絞盤、且井口必須常設專職地面監護員！", "C": "在井口點燃一支香煙看是否有瓦斯燃燒", "D": "在下井前喝下一大杯純牛奶"},
         "B", "Deep foul sewers harbour lethal toxic gases: Hydrogen Sulphide (deadly in seconds) and explosive Methane, plus oxygen depletion. Gas monitoring, breathing apparatus/winch, and a top-man are legal imperatives.", "下排污井下水道生死紅線：下水道裡的硫化氫（H2S）是隱形殺手，幾秒鐘就能讓人嗅覺麻痺昏迷窒息死亡！嚴禁盲目下井！必須拿氣體檢測儀探測、鼓風機死命往裡吹新鮮風、身上綁著三腳架絞盤繩子，井口留人死守！", "Confined Spaces Regulations 1997; Health and Safety Executive (HSE) Guidance"),

        # 79. Drainage fall formula calculation
        ("9.2",
         "If an underground foul drain run of 110mm pipe is 24 meters long and must be laid at a uniform gradient of 1:80, what is the total vertical fall (drop) in level required between the head and the outlet?",
         "若某段 110mm 地下排污暗管的總水平長度為 24 米，設計坡度嚴格要求為 1:80，則該段管道起點與末端之間的「總垂直落差（Fall）」應當精確為多少？",
         {"A": "300mm (0.3 meters)", "B": "1,000mm", "C": "24mm", "D": "80mm"},
         {"A": "300mm (即 0.3 米垂直下坡落差)", "B": "1,000mm", "C": "24mm", "D": "80mm"},
         "A", "Calculation: Total Fall = Distance ÷ Gradient = 24,000mm ÷ 80 = 300mm. The downstream invert must be precisely 300mm lower than the upstream invert.", "坡度落差基本數學題：總落差 = 總長度 ÷ 坡度比值。24 米 = 24,000mm。24,000 ÷ 80 = 300mm。水暖工拿水準儀測量：管尾必須比管頭精確低 30 公分！", "BS EN 752; C&G Unit 206 Practical Mathematics"),

        # 80. French drain vs land drain pipe type
        ("9.2",
         "What specific pipe design is used for agricultural and building foundation sub-soil land drainage (French drains)?",
         "在建築地基周邊防潮與農田地下降水盲溝中，專門敷設何種特製的「地下盲降集水管」？",
         {"A": "Solid high-pressure cast-iron pipe with no holes", "B": "Perforated corrugated plastic coil pipe (PVC or PE) wrapped in geotextile filter fabric or coconut coir", "C": "Glazed ceramic sanitary pipes glued tight", "D": "Rubber radiator hose"},
         {"A": "毫無孔隙的高壓實心耐壓鑄鐵管", "B": "管壁密布透水微孔的打孔波紋塑料盤管 (Perforated Corrugated Land Drain Pipe)，外包透水土工布或天然椰殼纖維防淤套", "C": "接頭完全膠粘封死的耐酸陶瓷排污管", "D": "汽車發動機橡膠散熱軟管"},
         "B", "Perforated land drain coils have hundreds of slots along their length. Subsurface groundwater seeps through the slots into the pipe, which channels the collected water away to a soakaway or ditch.", "打孔盲管集水原理：管壁上全是密密麻麻的小細縫！埋在碎石溝裡，地下水就像遇到海綿一樣從孔隙爭先恐後鑽進管子裡，順著波紋管嘩嘩排向遠方花園滲坑，徹底排乾地基積水！", "BS 4962 Specification for plastics pipes and fittings for subsoil drainage; C&G Unit 206"),

        # 81. Basin waste pop-up mechanism
        ("9.2",
         "What is a 'Click-Clack' (Spring-Loaded Push-Button) basin waste fitting, and why has it largely superseded mechanical rod linkage pop-up wastes?",
         "現代家庭洗手盆普遍配備的「彈跳式下水器 (Click-Clack / Push-Button Waste)」，相比老式後置金屬拉桿式下水器具有何種顯著優勢？",
         {"A": "It requires electricity", "B": "It operates via an internal stainless steel spring-loaded brass clicker mechanism directly depressed by hand, eliminating complex, clumsy metal articulating rods behind the tap that loosen and jam over time", "C": "It is made of wood", "D": "It cannot be opened once closed"},
         {"A": "必須依賴交流電驅動彈跳", "B": "利用內部自帶的高彈性不銹鋼彈簧黃銅彈跳閥芯，人手直接向下按壓即可自鎖閉合或彈起排水；徹底淘汰了龍頭後背笨重複雜、日久極易鬆動脫落卡死的金屬連動拉桿機構", "C": "完全採用純木材手工雕刻", "D": "一旦按下去閉合後終身再也無法彈起打開"},
         "B", "Click-clack wastes contain an internal spring cartridge. Pressing the chrome plug clicks it closed; pressing again springs it open. It simplifies installation by dispensing with awkward linkage rods behind the basin.", "彈跳下水器人性化設計：老式馬桶水龍頭後面帶個細長鐵絲拉桿，水盆下面空間窄，四五個卡扣幾個月就生鏽卡死脫扣。按壓彈跳下水器用手輕輕一按就關水、再按就彈開排水，結構簡單結實，維修幾分鐘換個閥芯搞定！", "BS EN 274; C&G Unit 206 Sanitary Appliances"),

        # 82. Trap clearing and hair removal
        ("9.2",
         "When a domestic shower trap or basin bottle trap drains very sluggishly with standing water in the tray, what is the most common physical obstruction, and how should it be professionally cleared?",
         "當家庭淋浴底盤或洗手盆下水極其緩慢、底盤內嚴重存水滯水時，最常見的物理堵塞物是什麼？水暖技師標準的現場疏通工藝是什麼？",
         {"A": "The pipe is filled with gold coins", "B": "Human hair entwined with solidified soap scum and body grease; remove the top chrome grille, extract the internal removable trap cup/baffle using pliers or a hook, wash clear with water, and re-seat", "C": "Boil the shower tray with a blowlamp", "D": "Smash the shower tray"},
         {"A": "下水管道被大量金幣塞滿", "B": "人體脫落的長頭髮與凝固的肥皂沫、人體油脂殘渣相互纏繞結成的厚重毛氈狀堵塞物；用手或小起子拆下頂部不銹鋼蓋板，提起內部可拆卸的防臭濾筒/水封杯，拿鉤子勾出頭髮並清水沖洗乾淨後復位", "C": "用動火噴燈直接烘烤塑料淋浴底盤", "D": "拿鐵錘砸碎淋浴底盤"},
         "B", "Shampoos and hairs combine into a felt-like mat that traps soap grease. Modern shower traps feature a top-access removable dip cup. Lifting the cup allows immediate hair removal from inside the room.", "淋浴下水慢元兇（頭髮肥皂氈）：洗澡掉的頭髮和沐浴露油垢在水封筒裡結成厚厚一層毛氈！現代淋浴地漏全做成「頂部可拆洗式」：摳開銀色大蓋子，裡面有個白色塑料小提桶，拔出來一把扯掉頭髮洗淨塞回去，下水立刻狂飆！", "C&G Unit 206 Maintenance; McAlpine Shower Trap Technical Sheet"),

        # 83. WC pan flush pipe cone
        ("9.2",
         "What is the function of the rubber 'Flush Pipe Cone' (rubber external/internal bung) connecting a low-level cistern downpipe into the back of a WC pan?",
         "在分體低水箱抽水馬桶中，連接沖水管（Flush Pipe）與馬桶陶瓷後背進水孔的「橡膠衝水管密封膠塞 / 喇叭膠圈 (Flush Cone)」，具有何種密封功能？",
         {"A": "To conduct electricity", "B": "To create a flexible, 100% watertight compression seal between the plastic/copper flush pipe and the internal ceramic socket, absorbing vibrational flush shocks without water weeping down the bathroom wall", "C": "To heat incoming cold water", "D": "To filter flush water"},
         {"A": "在沖水管與陶瓷之間傳導接地電流", "B": "在塑料/金屬沖水管與馬桶陶瓷進水孔插口之間形成高彈性、100% 絕對水密的壓緊密封屏障，吸收衝水時的水流震動衝擊，杜絕衝水時水滴沿浴室後牆滲漏水痕", "C": "為冰冷的衝水加溫加熱", "D": "過濾沖洗自來水中的雜質"},
         "B", "The flush cone compresses into the ceramic spigot aperture. When the cistern discharges, the sudden surge of water pushes the rubber ribs outwards against the porcelain, sealing tightly under flush pressure.", "馬桶進水橡膠皮圈（Flush Cone）：水箱一放水，十幾升水猛烈衝下！若接縫硬碰硬水會漫牆淌。錐形橡膠喇叭套塞進馬桶背後瓷孔，水流一壓橡膠圈向外膨脹越壓越緊，幾十年滴水不漏。", "BS 1125 WC flushing cisterns; C&G Unit 206"),

        # 84. Air testing failure troubleshooting
        ("9.2",
         "During an on-site air pressure test on an unvented above-ground soil stack, the U-tube water manometer level plummets to zero within 10 seconds. What is the standard troubleshooting method to pinpoint the leak?",
         "在對新安裝的室內排水立管進行氣密性打壓試驗時，U 型水柱壓力表讀數在 10 秒內瞬間暴跌歸零。水暖工應當採用何種標準檢漏工藝快速定位漏氣點？",
         {"A": "Ignite a match and walk along the pipe looking for fire", "B": "Apply a soapy water solution (or specialized leak detection spray) with a paintbrush over every joint, socket, boss adaptor, and mechanical bung, watching for expanding bubbles", "C": "Smash all the pipes with a hammer", "D": "Leave the leak forever"},
         {"A": "劃著一根燃燒的火柴沿著塑料管道尋找火源", "B": "拿毛刷蘸取高發泡肥皂水溶液（或專用微泡沫檢漏噴劑），逐一塗抹在每個管件承插口、橡膠變徑套、機械密封塞邊緣，仔細觀察哪裡產生持續鼓起的肥皂氣泡", "C": "用鐵錘將所有管道全部砸得粉碎", "D": "對嚴重漏氣視而不見、直接封板裝修"},
         "B", "Soapy water immediately blows prominent frothy bubbles where air escapes. Common culprits are displaced rubber seals, solvent-weld sockets missing cement on the underside, or loose test plugs.", "打壓漏氣刷肥皂水必殺技：嚴禁拿明火照！拿刷子蘸著洗潔精水往每個管子接頭刷一圈，哪裡漏氣哪裡立刻吐出一串串白泡泡！十有八九是哪個接頭膠水漏抹了半圈、或是管塞沒擰緊，一眼看穿！", "BS EN 12056-2 Testing; C&G Unit 206 Practical Fault Finding"),

        # 85. Concealed cistern pneumatic flush
        ("9.2",
         "How does a 'Pneumatic Dual-Flush Push Button' trigger the flush valve inside a concealed toilet cistern mounted inside a stud partition wall?",
         "安裝在石膏板輕鋼龍骨隔牆外飾面上的「氣動雙檔沖水面板按鈕」，是如何遙控觸發深藏在暗裝水箱內部的衝水閥閥芯的？",
         {"A": "Via high-voltage electric wires that shock the valve", "B": "Depressing the silicone button compresses a small puff of air down narrow, flexible silicone airline tubes (typically clear and blue for dual flush), actuating an internal pneumatic piston bellows inside the flush valve mechanism", "C": "Using radio waves from a satellite", "D": "Using wooden sticks"},
         {"A": "通過高壓電線放電電擊觸發閥門", "B": "按下按鈕時，內部微型硅膠氣囊壓縮出一小股微弱脈衝氣壓，沿著細小柔軟的雙色硅膠氣管（如透明管代表全衝、藍色管代表半衝）傳遞，推動暗裝水箱閥芯內部的微型氣動波紋活塞起吊排水", "C": "利用外太空軍用衛星無線電波", "D": "依靠暗埋在牆壁裡的長木棍機械推動"},
         "B", "Pneumatic buttons provide flexible remote installation up to 1-2 meters from the concealed cistern. Pushing the button pushes an air puff down tiny plastic tubes to trip the mechanical flush latch.", "氣動沖水按鈕的巧妙：暗裝水箱藏在牆壁裡，按鈕可以裝在牆上任何順手的地方！按鈕屁股後面接兩根極細的小軟皮管，一按按鈕一吹氣，空氣順著管子推動水箱裡的氣動小活塞，完全零漏電、絲滑安靜！", "BS 1125; Geberit / Grohe Concealed Cistern Service Manuals"),

        # 86. Secondary ventilation stack
        ("9.2",
         "In very tall high-rise residential towers (over 10 storeys), what system is installed parallel to the soil stack to handle massive air displacements and prevent induced siphonage?",
         "在超過 10 層以上的超高層住宅大廈中，為了吞吐巨量空氣位移、徹底消除全樓誘發虹吸抽吸水封，在主排水立管旁邊並行加裝了何種專用通氣管道？",
         {"A": "A parallel gas pipe", "B": "A Secondary Ventilating Stack (Parallel Ventilating Pipe) cross-connected to the main soil discharge stack at regular floor intervals (typically every alternate floor) with 45-degree swept links", "C": "A chimney for open coal fires", "D": "No extra pipes are ever permitted"},
         {"A": "並聯一根粗大的天然氣燃氣管道", "B": "專用輔助副通氣立管 (Secondary Ventilating Stack - 副立管)，且每隔一層（或每層）通過 45 度向上傾斜的順水連接支管與主排水立管實施跨接連通（跨越通氣管）", "C": "專供燃煤壁爐排煙的磚煙囪", "D": "法律嚴禁在大樓內加裝任何多餘管道"},
         "B", "Falling sewage in 10-storey stacks drags massive air currents down. Cross-connecting to a parallel dry vent stack recirculates air, equalizing pressures across all floors and protecting bottom traps.", "超高層副通氣管（通氣大動脈）：十幾層樓污水砸下來就像高鐵進隧道，活塞風壓極其恐怖！旁邊並排拉一根乾通氣管，兩三層架個 45° 梯子管連通。下頭的高壓空氣順著副管爬回樓上補氣，全樓氣壓徹底平衡！", "BS EN 12056-2 System I; Institute of Plumbing Design Guide"),

        # 87. Drainage pipe clipping and bracket supports
        ("9.2",
         "What is the maximum recommended horizontal support clip spacing for 32mm and 40mm plastic waste pipes under BS EN 12056-2?",
         "根據 BS EN 12056-2 標準，32mm 與 40mm 塑料排水細管水平敷設時，相鄰支撐管卡（Pipe Clips）之間推薦的最大水平支撐間距是多少？",
         {"A": "Maximum 0.5 meters (500mm) apart", "B": "Maximum 10 meters apart", "C": "Maximum 50mm", "D": "Pipes need no support clips"},
         {"A": "最大間距不超過 0.5 米 (500mm)", "B": "最大間距 10 米", "C": "最大間距 50mm", "D": "排水橫管完全不需要打卡子支撐"},
         "A", "Plastic waste pipes become soft and pliable when hot water (from washing machines, baths) runs through. Support brackets must not exceed 500mm on horizontal runs, otherwise pipes sag, creating water traps.", "塑料小管半米一打卡鐵律：洗碗洗澡全是熱水！PVC 或 PP 塑料管一遇 60°C 熱水立馬變軟。如果卡子打太稀（例如一兩米一個），管子立刻受熱塌腰下墜，凹下去形成一個個水窪積油堵死！必須 50 公分打一個卡！", "BS EN 12056-2 Section 7; C&G Unit 206"),

        # 88. Drain smell diagnosis in bathrooms
        ("9.2",
         "A homeowner complains of a persistent rotten-egg sewer smell in a newly renovated ensuite bathroom, but all traps are full of water. What hidden installation fault is frequently diagnosed?",
         "某業主投訴新裝修的套房浴室內常年瀰漫著一股刺鼻的臭雞蛋下水道惡臭，但技師檢查發現全屋所有洗手盆浴缸存水彎裡全部注滿了清水、水封完好無損。這種情況最常確診為何種隱蔽安裝缺陷？",
         {"A": "The tiles are made of real eggs", "B": "The Air Admittance Valve (AAV) rubber diaphragm is missing, damaged, wedged open with plaster grit, or an unsealed boss adaptor cap was left completely open inside the stud partition boxing", "C": "The cold water tap is running backwards", "D": "The mirror is emitting sewer gas"},
         {"A": "牆面瓷磚是由真雞蛋蛋殼烘烤製成的", "B": "暗裝進氣閥（AAV）內部密封橡膠膜片在施工時缺失、卡入石膏水泥砂粒未復位、或者立管預留的某個皮圈開口插頭在包管封板前被學徒忘記封堵！", "C": "自來水冷水龍頭在反向抽風", "D": "浴室梳妝鏡在向室內源源不斷散發沼氣"},
         "B", "If water traps are intact, foul gas is leaking through dry joints. An unsealed boss cap or an AAV stuck open with dry plaster dust allows unmitigated sewer gas into the hollow stud wall and room.", "水封沒乾為什麼還臭？十有八九是乾式漏氣！很多學徒在封石膏板前，立管上留的馬鞍接頭塑料塞忘記擰緊、或者進氣閥裡進了木屑泥巴把橡膠膜片卡開了一條縫。下水道毒氣全順著吊頂空腔往臥室灌！", "C&G Unit 206 Fault Finding; NHBC Standards 8.1"),

        # 89. Grease buildup in kitchen wastes
        ("9.2",
         "Why should boiling water and chemical caustic soda (sodium hydroxide) be used with extreme caution when attempting to clear grease blockages in domestic plastic waste pipes?",
         "當試圖清除家庭廚房塑料下水管道內堆積的頑固油脂死堵時，為什麼嚴禁將大壺沸騰開水與高濃度強鹼化學疏通劑（氫氧化鈉片鹼）狂暴混合倒入管道中？",
         {"A": "It will turn plastic pipes into glass", "B": "The violent exothermic chemical reaction generates extreme boiling heat (exceeding 100°C) that will soften, warp, melt, and detach PVC/push-fit plastic pipes, spraying scalding corrosive caustic lye onto the technician", "C": "It freezes the drain into ice", "D": "It smells like flowers"},
         {"A": "強鹼會將塑料下水管轉化為透明鋼化玻璃", "B": "片鹼遇水劇烈放熱並伴隨暴烈化學沸騰（溫度瞬間破百度），會直接將薄壁塑料下水管燙軟塌陷、接頭橡膠圈融化脫膠，甚至引發腐蝕性強鹼沸水像火山一樣反噴灼傷眼睛皮膚！", "C": "會將管道當場凝固結冰", "D": "化學反應會釋放芬芳的花香味"},
         "B", "Caustic soda reacting with water generates intense exothermic heat. Thin-wall PVC pipes soften at ~70°C. Water flash-boils, blowing boiling, eye-destroying caustic lye out of the sink.", "片鹼通水管危險警告：很多人無知猛倒片鹼再倒開水，幾秒鐘水管裡高達 120°C，塑料管當場像煮爛的麵條一樣化掉脫落，滾燙的強鹼水直接從天花板漏下把人重度化學燒傷甚至雙眼失明！必須嚴格防護！", "HSE Chemical Safety Guidelines; C&G Unit 206 Safety"),

        # 90. Final sanitation commissioning test
        ("9.2",
         "What is the final statutory operational test conducted during the commissioning of a completed above-ground sanitary pipework installation under Approved Document H1?",
         "根據 Approved Document H1 標準，在全屋地上衛生器具排水管網安裝完畢後，竣工交付驗收時實施的最終法定「系統衛生通水運行調試 (Performance Testing)」程序是什麼？",
         {"A": "Pour paint down all appliances", "B": "Fill and simultaneously discharge combinations of appliances (e.g. WC flushed while basin discharges) and measure the residual water seal in all traps, confirming at least 25mm to 50mm of water seal is permanently retained in every trap", "C": "Cut all pipes open to inspect with a torch", "D": "Never run water through the system"},
         {"A": "向全屋所有衛生器具內傾倒彩色油漆", "B": "將衛生器具放滿水並實施多器具同時排水聯動測試（如一邊放滿面盆拔塞、一邊同時按壓馬桶衝水），隨後精準測量各器具存水彎內殘留水封高度，確認每件器具「永久保留的水封深度至少仍在 25mm 至 50mm 以上」", "C": "拿鋸子把全屋所有管道切開用手電筒逐一觀察", "D": "嚴禁向系統內部通水驗收"},
         "B", "Commissioning verifies hydraulic integrity. Appliances are discharged simultaneously under worst-case loading. Traps must retain at least 25mm (and preferably >50mm) of water seal to guarantee an unbroken gas barrier.", "排水驗收終極大考（極限連環衝水）：放滿一水池水、猛地拔掉塞子，同時狠狠按兩次馬桶衝水！大水呼嘯而下；水排完後拿尺子伸進存水彎一量——水封殘留深度必須穩穩在 25mm 以上（最好超 50mm），才算驗收合格！", "Building Regulations Approved Document H1 Section 1.35; BS EN 12056-2 Testing")
    ]

    for sub_id, stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref in data:
        questions.append(make_q(9, sub_id, ["Unit_206"], stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref))

    return questions
