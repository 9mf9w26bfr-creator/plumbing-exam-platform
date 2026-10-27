# 功能与验收要求 (Requirements)

## 1. 核心功能模块
1.  **双轨练习模式 (Dual Index Practice)**:
    *   **章节模式**: 用户可选择具体教材章节（如 Chapter 3: Scientific Principles）和子节点（如 Energy, Heat and Power）进行随机抽题。
    *   **单元模式**: 用户可直接选择考试单元（如 Health & Safety, Cold Water Systems）。注意：Environmental Revision 作为经过大纲核实的复习分类存在，而非凭空创建的 Level 2 考试单元。
2.  **双语切换 (Bilingual Toggle)**:
    *   做题界面提供一键切换中/英题目和选项的功能，不刷新页面，保持当前做题状态。
3.  **审核与发布后台 (CMS Workflow)**:
    *   提供题目管理的 CRUD 界面，支持状态管理 (`Draft` → `AI Reviewed` → `Technically Verified` → `Published`)。
4.  **错题本与数据分析 (Analytics)**:
    *   记录用户的错题，支持按章节或按考试单元生成掌握度雷达图。

## 2. 验收标准
*   同一道题目不能在数据库中存在两条记录（中英必须在同一记录中）。
*   题目未达到 `Published` 状态绝对不能出现在普通用户的练习流中。
