# 项目总规则 (Project Constitution)

## 1. 核心指导原则
本项目旨在构建一个专门针对英国水暖及供暖行业（C&G Level 2/3）的在线考试与练习平台。系统的核心在于科学的知识点组织与严格的质量控制。

## 2. 三项绝对规则 (The Three Absolute Rules)

### 规则一：教材目录与考试单元分离 (Separation of Concerns)
教材章节（Textbook Chapters）是**知识组织方式**，资格单元（Qualification Units）是**考试组织方式**。
两者在系统中必须分开管理，不能混为一谈。系统的底层数据结构必须支持多对多的映射。

### 规则二：中英双语共享核心 ID (Shared Question ID)
中英文题目并非独立的两道题，而是同一知识实体的两种语言表现。
**任何一道题目，其中英文版本必须共享同一个 `Question ID`**。双语切换仅在前端渲染层进行，数据库中统一管理。

### 规则三：严格的审核工作流 (Strict Review Workflow)
题目必须经过审核才能进入正式题库。状态机如下：
`Draft` (草稿) → `AI Reviewed` (AI 初审) → `Technically Verified` (技术核实) → `Published` (正式发布)
*特别注意*：涉及健康安全 (Health & Safety)、电气安全 (Electrical Safety)、水事法规 (Water Regs) 及其他现行技术要求的题目，必须核对可靠来源文档，严禁仅依靠 AI 自行判断。

## 3. 双轨练习模式 (Dual-Track Practice System)
系统不应是单纯的章节选择题网站，必须采用两套相互关联的题库索引：
*   **A. 按教材章节练习**：用户按具体的书籍章节与小节刷题（如：Chapter 3 -> SI Units）。
*   **B. 按考试单元练习**：用户按官方考试代码刷题（如：Health & Safety, Scientific Principles）。
*   同一道原创题目可以同时关联一个教材章节和一个或多个经过核实的学习目标，不重复存储。
