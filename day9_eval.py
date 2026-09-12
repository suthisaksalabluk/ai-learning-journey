# day9_eval.py - Day 9: LLM-as-a-Judge & Automated Evaluation

# 1. ข้อมูลการทดสอบ (Question, AI Answer, Expected Gold Reference)
eval_dataset = [
    {
        "question": "Python คืออะไร?",
        "ai_answer": "Python เป็นภาษาโปรแกรมระดับสูงที่เน้นความอ่านง่าย",
        "score": 5
    },
    {
        "question": "Git ใช้ทำอะไร?",
        "ai_answer": "Git เป็นโปรแกรมแต่งรูปภาพ",
        "score": 1
    }
]

# 2. ฟังก์ชันประเมินผ่าน-ไม่ผ่าน (Evaluator Function)
def evaluate_ai_response(item):
    score = item["score"]
    
    # TODO 1: พิมพ์เงื่อนไข if เช็กว่าคะแนน (score) มากกว่าหรือเท่ากับ 4 หรือไม่
    if score >= 4:
        status = "PASSED (High Accuracy)"
    else:
        status = "FAILED (Hallucination/Incorrect)"
        
    # TODO 2: พิมพ์ f-string สรุปผลการประเมิน
    # (คำใบ้: f"Q: {item['question']} | Score: {score}/5 -> Status: {status}")
    result_text = f"Q: {item['question']} | Score: {score}/5 -> Status: {status}"
    return result_text

# =============================================================
# EXECUTION & EVALUATION SUITE
# =============================================================
print("=== Day 9: Automated LLM Evaluation Suite ===\n")

passed_count = 0

for data in eval_dataset:
    # TODO 3: เรียกใช้ฟังก์ชัน evaluate_ai_response โดยส่งตัวแปร data เข้าไป
    eval_report = evaluate_ai_response(data)
    print(eval_report)
    
    if "PASSED" in eval_report:
        passed_count += 1

print("\n" + "="*50)
print(f"Total Evaluated: {len(eval_dataset)} | Passed: {passed_count} | Failed: {len(eval_dataset) - passed_count}")

if passed_count > 0:
    print("[EVAL SUCCESS] Automated evaluation pipeline verified!")