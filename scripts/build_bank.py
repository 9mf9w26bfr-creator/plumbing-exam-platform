import sys
import json
import os

sys.path.append('scripts')
from bank_builder import (
    ch01_safety, ch02_processes, ch03_science, ch04_planning,
    ch05_coldwater, ch06_hotwater, ch07_heating, ch08_rainwater,
    ch09_sanitation, ch10_fuel_env, ch11_electrical
)

def build():
    modules = [
        ch01_safety, ch02_processes, ch03_science, ch04_planning,
        ch05_coldwater, ch06_hotwater, ch07_heating, ch08_rainwater,
        ch09_sanitation, ch10_fuel_env, ch11_electrical
    ]
    
    all_questions = []
    seen_ids = set()
    
    for mod in modules:
        qs = mod.get_questions()
        for q in qs:
            qid = q['id']
            if qid in seen_ids:
                raise ValueError(f"Duplicate question id found: {qid}")
            seen_ids.add(qid)
            
            # Validation
            assert len(q['options_en']) == 4, f"Invalid options_en in {qid}"
            assert len(q['options_zh']) == 4, f"Invalid options_zh in {qid}"
            assert q['correct_answer'] in ['A', 'B', 'C', 'D'], f"Invalid answer in {qid}"
            assert q['content_en'] and q['content_zh'], f"Empty stem in {qid}"
            assert q['source_reference'], f"Missing source_reference in {qid}"
            
            all_questions.append(q)
            
    print(f"Successfully assembled {len(all_questions)} validated questions.")
    
    # Write to frontend
    frontend_path = 'frontend/src/data/questions_bank.json'
    with open(frontend_path, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
    print(f"Written to {frontend_path}")
    
    # Write to backend
    os.makedirs('backend/app/data', exist_ok=True)
    backend_path = 'backend/app/data/questions_bank.json'
    with open(backend_path, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
    print(f"Written to {backend_path}")

if __name__ == '__main__':
    build()
