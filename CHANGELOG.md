# 版本记录 (Changelog)

## [1.1.0] - Web Mock Exam Platform Implementation (2026-10-27)
*   **後端架構 (FastAPI + SQLAlchemy + Pydantic)**:
    *   嚴格按照 `DATABASE_SCHEMA.md` 實現 5 張核心表結構，無任何違規字段增刪 (Rule A)。
    *   提供雙軌索引 API：`/api/questions/by-chapter/{chapter_id}` 與 `/api/questions/by-unit/{unit_id}` (Rule 1)。
    *   全真模擬考試接口 `/api/questions/mock-exam`，嚴格僅提供 Published 狀態的合格題目。
    *   CMS 審核流水線 API：實現 `Draft` → `AI_Reviewed` → `Technically_Verified` → `Published` 狀態機，推進入核實階段強制檢查 `source_reference` (Rule 3)。
    *   數據庫種子導入腳本：嚴格遵守中英共享同一 `Question ID` 實體 (Rule C & Rule 2)。
*   **前端架構 (Next.js 14 + TypeScript + Tailwind CSS)**:
    *   具備現代工程感的乾淨界面風格 (Rule B)。
    *   雙軌練習導航：按 11 本權威教材章節 (Chapter & Sub-topics) 或 10 大考綱單元 (Qualification Units)。
    *   無刷新一鍵切換中/英雙語對照 (Bilingual Toggle Context)，答題狀態與倒計時無縫保持。
    *   全真模擬考試：動態倒計時、答題卡矩陣 (Palette)、複查標記 (Flag)、自動診斷報告與及格判定 (C&G 60% 標準)。
    *   本地錯題本 (Mistake Notebook)：自動記錄並持久化錯題，支持專項重測與攻克後移除。
    *   掌握度數據分析 (Mastery Analytics)：按章節與考綱單元統計正確率、做題量與掌握度分級。
    *   CMS 題庫審核工作台：題目生命週期狀態轉換、雙語題目錄入模態框、權威法規出處校驗。

## [1.0.0] - Initial Constitution
*   创建了项目开发宪法。
*   确立了教材与考试单元分离的核心原则。
*   定义了中英双语共享 Question ID 的数据库架构。
*   制定了题库状态机审核流程 (Draft -> Published)。
