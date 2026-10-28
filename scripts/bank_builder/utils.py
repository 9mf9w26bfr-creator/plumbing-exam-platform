import uuid

def make_q(ch_id, sub_id, unit_ids, stem_en, stem_zh, opts_en, opts_zh, ans, exp_en, exp_zh, ref):
    assert ans in ["A", "B", "C", "D"], f"Invalid answer key: {ans}"
    assert len(opts_en) == 4 and set(opts_en.keys()) == {"A", "B", "C", "D"}, "opts_en must have A, B, C, D"
    assert len(opts_zh) == 4 and set(opts_zh.keys()) == {"A", "B", "C", "D"}, "opts_zh must have A, B, C, D"
    
    return {
        "id": str(uuid.uuid4()),
        "content_en": stem_en.strip(),
        "content_zh": stem_zh.strip(),
        "options_en": opts_en,
        "options_zh": opts_zh,
        "correct_answer": ans,
        "explanation_en": exp_en.strip(),
        "explanation_zh": exp_zh.strip(),
        "status": "Published",
        "source_reference": ref.strip(),
        "chapters": [{"chapter_id": ch_id, "sub_topic_id": str(sub_id)}],
        "units": unit_ids
    }
