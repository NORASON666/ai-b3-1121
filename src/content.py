# 2026-11-21 B3 數位教學指引儲備講師培訓工作坊（中教大）下午試講
# 主軸：把《115 年中小學教師數位與 AI 教學指引》三個模組，接到臺北市的教室與酷AI
# Nora 的風格：少講理論，每個概念都配一則真實新聞或一張圖
# 每頁一個 dict：t=版型；sup=[...] 為該頁補充資料（S 鍵）；notes 為講稿（N 鍵）
# 版權：新聞只放標題、媒體、日期與一句摘要＋原文連結；教宗羽絨外套圖為 Midjourney 生成、Wikimedia Commons 標示 Public domain

SHOT = "assets/shots/"
ILL = "assets/illus/"


def news(outlet, date, head, line, url):
    return {"outlet": outlet, "date": date, "head": head, "line": line, "url": url}


S = [
    {"t": "cover",
     "notes": "大家好，我是臺北市數位學習中心的周凡淇。我的試講想做一件事：把今天的公版內容，接到臺北老師每天的教室。理論我少講，每個概念都配一則新聞或一張圖。"},

    # ── 開場：臺北在指引裡的位置
    {"t": "shotText", "kicker": "先看一張圖", "title": "教育部推薦名單上，有臺北",
     "img": "a2_list.png",
     "text": ["指引 p.67：優先選用**教育部建置或推薦**的數位學習平臺",
              "A2 數位學習平臺推薦名單：**臺北酷課雲**（115.10.16 起）",
              "和因材網、酷英並列",
              "**酷AI** 就是酷課雲裡的 AI 學習系統"],
     "src": "pads.moe.edu.tw/teacher_list.php（2026-11-21 截圖）",
     "notes": "指引說優先用教育部建置或推薦的平臺。這是教育部 A2 推薦名單，臺北酷課雲 115 年 10 月 16 日起列入。我等一下講的酷AI，就是酷課雲裡的 AI 學習系統。（注意：名單寫的是酷課雲，用詞是推薦，不是認證。）",
     "sup": [{"kind": "官方資料", "evidence": "正式文件", "title": "A2 數位學習平臺推薦名單（教育部 AI 人才方舟計畫網站）",
              "points": ["教育部因材網、Cool English 酷英、PaGamO、加分吧、HiTeach：115.09.01–118.12.31",
                         "臺北酷課雲、Yory 優歷：115.10.16–118.12.31",
                         "頁面用詞是「推薦」，沒有「認證」；名單上沒有「酷AI」這個名字"],
              "source": "教育部 AI 人才方舟計畫－數位學習輔導團隊", "url": "https://pads.moe.edu.tw/teacher_list.php"}]},

    {"t": "stats", "kicker": "臺北的教育型 AI", "title": "酷AI：已經在教室裡的 AI",
     "stats": [("77 萬", "人次使用", "2026-01 跨縣市記者會公布的累計數字"),
               ("3 縣市", "簽 MOU 共享", "連江、雲林、澎湖"),
               ("253 校", "到校研習", "339 場、17,844 人次（2023-10～2026-04）")],
     "notes": "酷AI 累計 77 萬人次使用。今年 1 月和連江、雲林、澎湖簽 MOU，開放跨縣市共享。中心這兩年半到 253 所學校辦了 339 場研習。",
     "sup": [{"kind": "數據來源", "evidence": "正式文件", "title": "數字出處",
              "points": ["77 萬人次、3 縣市 MOU：2026-01-26 酷AI 教學手冊發布暨跨縣市合作簽署記者會（林奕華副市長主持）",
                         "339 場、17,844 人次、253 校：數位學習中心研習推廣紀錄（2023-10～2026-04）",
                         "對照：e度到 2025-08 超過 70 萬人次（模組三公版簡報）"]}]},

    # ── 模組一
    {"t": "divider", "kicker": "模組一", "title": "指引裡的臺北", "sub": "公版自己就舉了臺北", "img": "guide_trend4.png",
     "notes": "模組一我只講一件事：公版簡報裡其實已經有臺北。"},

    {"t": "shotText", "kicker": "模組一｜四個趨勢", "title": "趨勢四：臺灣在地實踐",
     "img": "guide_trend4.png",
     "text": ["公版寫：**酷英網導入 CoolE Bot**，實現適性化對話",
              "酷英是臺北市建置、全國使用的英語平臺",
              "臺北還有**酷AI**：各學科、個人化學習路徑",
              "講趨勢時，舉老師**看得到、明天就能用**的例子"],
     "src": "模組一公版簡報 p.16",
     "notes": "公版的趨勢四，臺灣在地實踐舉的就是酷英網的 CoolE Bot。到臺北學校講，我會接著說：臺北還有酷AI，涵蓋各學科。舉老師明天就能登入的例子，比講國外案例有感。"},

    {"t": "shot2", "kicker": "模組一｜臺北的例子", "title": "酷AI：從統一進度，走向個人化路徑",
     "imgs": ["kuai_06.png", "kuai_07.png"],
     "src": "《2026 酷AI 系統新增功能介紹》（2026-01-26 記者會）",
     "notes": "左邊是個人化學習路徑：智慧推薦影片、個人化試題、互動影片。右邊是學生端：AI 助教推薦影片和試題、答題即時批改、AI 小幫手解惑。"},

    # ── 模組二
    {"t": "divider", "kicker": "模組二", "title": "七大風險", "sub": "用新聞看，不用背", "img": "pope_puffer_ai.jpg",
     "notes": "模組二的七大風險，我不讓老師背口訣，直接看新聞。"},

    {"t": "newsimg", "kicker": "模組二｜錯假訊息 STEP", "title": "這張照片，你會轉傳嗎？",
     "img": "pope_puffer_ai.jpg",
     "items": [("S 看來源", "誰發的？原始出處在哪？"), ("T 看時間", "什麼時候的事？"),
               ("E 看證據", "有其他媒體、官方證實嗎？"), ("P 看觀點", "不同來源怎麼說？")],
     "foot": "答案：AI 生成（Midjourney，2023-03），當時在網路瘋傳",
     "src": "圖：Wikimedia Commons〈Pope Francis in puffy winter jacket〉，Public domain",
     "notes": "先別看下面的答案。請老師想：你會轉傳嗎？……這張是 2023 年 3 月用 Midjourney 生成的，當時很多人信以為真。用 STEP 四步走一次：來源是誰？時間？有沒有其他證據？不同媒體怎麼說？",
     "sup": [{"kind": "新聞", "evidence": "媒體報導", "title": "教宗羽絨外套假照片（CBS News）",
              "points": ["2023 年 3 月以 Midjourney 生成，在社群瘋傳",
                         "製作者說只是練習，但和其他傳言一起流傳，形成假敘事",
                         "同類事件：2023-05「五角大廈爆炸」AI 假圖，美股一度下跌"],
              "url": "https://www.cbsnews.com/news/pope-francis-puffer-jacket-fake-photos-deepfake-power-peril-of-ai"}]},

    {"t": "news", "kicker": "模組二｜錯假訊息 STEP", "title": "5 秒，就能偷走你的聲音",
     "items": [news("TechNews 科技新報", "2026-06-11", "5 秒音檔就能「偷走你的聲音」", "美中接連爆發 AI 變聲詐騙，以「親友出事」開場，催你在查證前匯款", "https://technews.tw/2026/06/11/ai-voice-cloning-scams/"),
               news("刑事警察局預防科", "2026", "深偽能即時模仿親屬的聲音與影像", "生成式 AI 把詐騙改造成近乎全自動的攻擊", "https://www.bnext.com.tw/article/89781/2026-ai-scam-trends-security")],
     "foot": "課堂最簡單的一招：跟家人約好一個「暗號」",
     "notes": "AI 變聲只要 5 秒音檔。公版講師示範的「爺爺接到哥哥電話」就是這種。上午有位老師分享得很好：對孩子最有用的不是一套查證流程，而是跟家人約好暗號。",
     "sup": [{"kind": "新聞", "evidence": "媒體報導", "title": "AI 變聲詐騙",
              "points": ["TechNews 2026-06-11：取得約 5 秒語音就可能產生以假亂真的聲音",
                         "數位時代整理刑事局說法：深偽可即時模仿親屬聲音與影像"],
              "talk": "接到家人說出事要匯錢，先掛掉，用原本存的電話打回去確認。", "url": "https://technews.tw/2026/06/11/ai-voice-cloning-scams/"}]},

    {"t": "news", "kicker": "模組二｜AI 幻覺 FACT", "title": "律師相信 AI，罰 5,000 美元",
     "items": [news("TechNews 科技新報", "2026-09-29", "律師用 ChatGPT，書狀出現不存在的警察證人", "美國新墨西哥州謀殺案上訴，律師被裁藐視法庭、罰 5,000 美元並移送懲戒", "https://finance.technews.tw/2026/09/29/lawyer-cites-fake-witnesses-in-murder-case-and-blames-chatgpt/"),
               news("TechNews 科技新報", "2025", "AI 假判例全球追查", "ChatGPT 問世以來，全球已記錄超過 500 起法律文件引用 AI 虛構內容", "https://technews.tw/?p=1465513")],
     "foot": "F 找出可疑 → A 追問依據 → C 查證比對 → T 修正轉化",
     "notes": "連專業律師都會被 AI 騙。新墨西哥州的律師用 ChatGPT 整理筆錄，書狀裡冒出不存在的證人。這就是 FACT：找出可疑、追問依據、查證比對、修正。",
     "sup": [{"kind": "新聞", "evidence": "媒體報導", "title": "AI 幻覺進法院",
              "points": ["2026-09 新墨西哥州：虛構證人與證詞，罰 5,000 美元、移送律師紀律委員會",
                         "美國律師協會立場：用 AI 不違規，但律師對內容正確負最終責任"],
              "limits": ["「超過 500 起」為媒體整理的統計，引用時說「媒體統計」"],
              "url": "https://finance.technews.tw/2026/09/29/lawyer-cites-fake-witnesses-in-murder-case-and-blames-chatgpt/"}]},

    {"t": "news", "kicker": "模組二｜認知卸載 THINK", "title": "用 AI 寫完，自己卻記不得",
     "items": [news("MIT Media Lab", "2025-06", "Your Brain on ChatGPT", "54 人寫作實驗：用 AI 組的腦部連結最弱，也最難引用自己剛寫的句子", "https://www.media.mit.edu/publications/your-brain-on-chatgpt/"),
               news("OECD", "2026-01", "Digital Education Outlook 2026", "有通用 AI 時作業品質較好；拿掉 AI 考試，優勢消失甚至反轉", "https://www.oecd.org/en/publications/oecd-digital-education-outlook-2026_062a7394-en.html")],
     "foot": "T 先試試 → H 只要提示 → I 自己說明 → N 換題再做 → K 確認自己懂",
     "notes": "MIT 的實驗：用 ChatGPT 寫作文的那組，腦部連結最弱，而且很難引用自己剛寫的句子。OECD 今年的報告也說：有 AI 時作業看起來比較好，拿掉 AI 考試就打回原形。所以 THINK 的第一步是先自己試。",
     "sup": [{"kind": "研究", "evidence": "研究報告", "title": "認知卸載的證據",
              "points": ["MIT Media Lab（Kosmyna 等，2025-06）：54 位受試者，分 AI、搜尋、純人腦三組，以 EEG 量測",
                         "OECD Digital Education Outlook 2026：通用型 GenAI 提升作業表現，但移除後在考試中優勢消失，有時反轉；有教學設計的教育型工具才有持續的學習效果"],
              "limits": ["MIT 研究是預印本、尚未同儕審查、樣本小，不能說「ChatGPT 傷害大腦」",
                         "公版提到的「17%」出自媒體對土耳其實驗的報導，OECD 頁面本身沒有這個數字，引用前要查原文"],
              "url": "https://www.media.mit.edu/publications/your-brain-on-chatgpt/"}]},

    {"t": "news", "kicker": "模組二｜隱私與資訊安全 SAFE", "title": "工程師把原始碼貼給 ChatGPT",
     "items": [news("iThome", "2023-04", "三星員工把機密輸入 ChatGPT", "20 天內 3 起：程式原始碼、設備量測資料、會議紀錄", "https://www.ithome.com.tw/news/156291"),
               news("數位時代", "2023-05", "三星禁止員工使用生成式 AI", "資料存在外部伺服器，難以取回或刪除", "https://www.bnext.com.tw/article/75096/samsung-ban-ai-gpt-may-23")],
     "foot": "臺北的做法：用單一身分驗證登入酷AI，學生不必另外註冊商用帳號",
     "notes": "三星的工程師為了抓 bug，把整份原始碼貼給 ChatGPT。換到學校，就是老師把學生成績、名單貼進商用 AI。注意事項 2.1 說不得用個人帳號處理學生資料。臺北的做法是讓師生用單一身分驗證登入酷AI，不用另外辦商用帳號。",
     "sup": [{"kind": "新聞", "evidence": "媒體報導", "title": "三星 ChatGPT 外洩事件（2023）",
              "points": ["半導體部門 20 天內 3 起：原始碼除錯、測試序列最佳化、會議錄音摘要",
                         "2023-05 全面限制員工使用生成式 AI"],
              "talk": "老師最常犯的版本：把全班成績表貼進 AI 請它分析。",
              "url": "https://www.ithome.com.tw/news/156291"}]},

    {"t": "news", "kicker": "模組二｜情感依附錯位 CARE", "title": "陪伴型 AI，禁止未成年開放聊天",
     "items": [news("NBC News", "2024-10", "14 歲少年與聊天機器人對話後輕生，母親提告", "訴狀指控平臺設計刻意讓使用者產生情感依附", "https://www.nbcnews.com/tech/characterai-lawsuit-florida-teen-death-rcna176791"),
               news("eWEEK", "2026-01", "Character.AI 與 Google 和解多起訴訟", "2025-10 起，未滿 18 歲不能再和角色開放式聊天", "https://www.eweek.com/news/google-character-ai-teen-suicide-lawsuits/")],
     "foot": "C 覺察情緒 → A 知道 AI 沒有真感情 → R 找真人求助 → E 回到真實互動",
     "notes": "這是最沉重的一則。美國 14 歲少年長期和聊天機器人對話後輕生，家長提告；平臺後來禁止未成年開放式聊天。國小到高中都要談：AI 可以陪你練習表達，但遇到重要情緒要找真人。",
     "sup": [{"kind": "新聞", "evidence": "媒體報導", "title": "Character.AI 訴訟",
              "points": ["2025-05 聯邦法官裁定訴訟可以進行", "2025-10 宣布未滿 18 歲不能再進行開放式角色聊天", "2026-01 報導與多個家庭和解，條件未公開"],
              "limits": ["訴狀內容是指控，未經判決證實；涉及自殺議題，對學生講要依年齡調整，避免細節"],
              "url": "https://www.nbcnews.com/tech/characterai-lawsuit-florida-teen-death-rcna176791"}]},

    {"t": "shotText", "kicker": "模組二｜由 AI Ask 到 AI Agent", "title": "公版列的工具，我每天都在用",
     "img": "guide_agent_tools.png",
     "text": ["公版 p.30：Codex、**Claude Code**、Claude Cowork、Gemini CLI……",
              "中心的實例：用 AI Agent 批次產製**酷AI 課程包**",
              "全市 250 校報表：一套參數化範本 × 每校資料",
              "**風險同一套**：工具安全、內容安全、學生身心安全"],
     "src": "模組二公版簡報 p.30",
     "notes": "公版列的 AI Agent 工具，Claude Code、Codex，就是我們中心每天在用的。我們用它批次產製酷AI 的課程包，也用一套範本產出全市 250 校的報表。重點不是工具多強，而是：給 AI 一個目標，它自己規劃步驟，人負責驗收。"},

    # ── 模組三
    {"t": "divider", "kicker": "模組三", "title": "教育型 AI", "sub": "公版用 e度，臺北用酷AI", "img": "guide_table41.png",
     "notes": "模組三的示例全部是因材網、e度。到臺北，我換成酷AI。"},

    {"t": "table", "kicker": "模組三｜表 4-1 套到臺北", "title": "教育型 AI 的特徵，酷AI 怎麼對？",
     "head": ["表 4-1 的特徵", "通用型 AI", "酷AI"],
     "rows": [["設計目的", "使用者要什麼就做什麼", "對應課綱單元的學習活動"],
              ["登入與資料", "個人帳號、各平臺年齡限制", "臺北市單一身分驗證"],
              ["教師角色", "老師看不到過程", "老師開課、看作答結果與課後分析"],
              ["教育部", "需學校自行評估", "酷課雲列入 A2 推薦名單"]],
     "notes": "用公版的表 4-1 對照：通用型 AI 是使用者要什麼就給什麼；酷AI 從課綱單元出發，用單一身分驗證登入，老師開課、看得到學生作答與課後分析。",
     "sup": [{"kind": "對照", "evidence": "講者整理", "title": "對照依據",
              "points": ["表 4-1：指引第四章〈教育型 AI 與通用型 AI 比較表〉",
                         "酷AI 登入方式：臺北市校園單一身分驗證、教育雲端帳號（2026-09 實測）",
                         "A2 推薦名單：臺北酷課雲 115.10.16 起"]}]},

    {"t": "shot2", "kicker": "模組三｜AIPACK 四學", "title": "學生自學 → 老師看數據 → 精準推薦",
     "imgs": ["kuai_08.png", "kuai_09.png"],
     "src": "《2026 酷AI 系統新增功能介紹》",
     "notes": "對到公版的四學：學生自學時 AI 助教產生個人強化練習；老師端課後分析、推薦評量、看學習診斷報表，再決定導學要補什麼。"},

    {"t": "shot2", "kicker": "模組三｜學科融合", "title": "程式、臺語、英語口說",
     "imgs": ["kuai_10.png", "kuai_11.png", "kuai_12.png"],
     "src": "《2026 酷AI 系統新增功能介紹》",
     "notes": "公版說趨勢四是學科融合。酷AI 的例子：Scratch 作品 AI 即時批改、臺語 AI 語音練習、英語 AI 互動口說。"},

    {"t": "cards", "kicker": "模組三｜普及化與平權化", "title": "上午的問題：誰付得起 AI？",
     "cols": 2,
     "cards": [("愛沙尼亞 AI Leap", "2025-09 起，政府提供高中生與教師免費的 ChatGPT Edu\n首年約 2 萬名學生", "國家買單"),
               ("臺北酷AI", "全市師生用單一身分驗證就能用\n2026-01 與連江、雲林、澎湖簽 MOU 共享", "城市分享")],
     "foot": "數位平權：不是每位老師自己付費，而是公共平臺讓每個孩子都用得到",
     "notes": "上午講師問誰有付費 AI，我們這裡很多人舉手，但一線老師多半沒有。愛沙尼亞的做法是國家買單；臺北的做法是公共平臺，而且分享給離島與偏鄉縣市。",
     "sup": [{"kind": "新聞", "evidence": "官方資料", "title": "愛沙尼亞 AI Leap",
              "points": ["2025-09-01 起，首年約 20,000 名 10–11 年級學生與 3,000 名教師", "以 ChatGPT Edu 為基礎，教育部、大學與 OpenAI 合作調整"],
              "url": "https://hm.ee/en/news/estonia-announces-groundbreaking-national-initiative-ai-leap-programme-bring-ai-tools-all"}]},

    {"t": "shotText", "kicker": "研習之後", "title": "隔天，英文老師自己做了 App",
     "img": "sanxing_app.jpg",
     "text": ["2026-11-18 三興國小 2 小時 AI 研習",
              "隔天：英文老師做出**單字複習 App**，放上 Google Sites",
              "課堂上：平板個人練習＋大屏全班複習",
              "數位科技不是目的，是讓老師**明天就能用**"],
     "src": "三興國小教務主任 2026-11-19 提供",
     "notes": "最後分享一個上週的例子。三興國小研習完隔天，英文老師就自己做了單字複習 App，放上 Google Sites，在課堂用平板和大屏複習。這是我覺得研習最好的成果：老師明天就用得上。"},

    {"t": "closing",
     "notes": "我的試講到這裡。總結一句：講指引時，少講理論、多給老師看得到的新聞和工具；到臺北，就用酷AI 當例子。謝謝大家。"},
]
