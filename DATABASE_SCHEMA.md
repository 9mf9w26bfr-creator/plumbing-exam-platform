# 数据库设计 (Database Schema)

## 核心表结构

### 1. `questions` (题目主表)
*   `id`: UUID (主键)
*   `content_en`: Text (英文题干)
*   `content_zh`: Text (中文题干)
*   `options_en`: JSON (英文选项)
*   `options_zh`: JSON (中文选项)
*   `correct_answer`: String (正确答案键值，如 'A')
*   `explanation_en`: Text (英文解析)
*   `explanation_zh`: Text (中文解析)
*   `status`: Enum ('Draft', 'AI_Reviewed', 'Technically_Verified', 'Published')
*   `source_reference`: String (参考规范或法规出处)

### 2. `textbook_chapters` (教材章节表)
*   `id`: Int (如 3)
*   `title`: String (如 "Scientific principles")
*   `sub_topics`: JSON (小节列表)

### 3. `exam_units` (资格单元表)
*   `id`: String (如 "Unit_201")
*   `title`: String (如 "Health & Safety")
*   `category`: String (如 "Core", "Environmental Revision")

### 4. `question_chapter_mapping` (题目-章节映射表)
*   `question_id`: UUID
*   `chapter_id`: Int
*   `sub_topic_id`: String

### 5. `question_unit_mapping` (题目-单元映射表)
*   `question_id`: UUID
*   `unit_id`: String
