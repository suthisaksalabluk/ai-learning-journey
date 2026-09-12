# day7_guardrails.py - Day 7: AI Guardrails & Output Validation

# รายการคำต้องห้ามที่ไม่ต้องการให้ AI ตอบออกมา (Forbidden Words)
forbidden_words = ["error", "unknown", "confidential"]

def apply_guardrails(ai_response):
    # TODO 1: พิมพ์คำสั่ง len เพื่อเช็กว่าความยาวของข้อความน้อยกว่า 10 ตัวอักษรหรือไม่
    if len(ai_response) < 10:
        return False, "REJECTED: Response too short!"
    
    # วนลูปเช็กว่ามีคำต้องห้ามอยู่ในข้อความตอบกลับหรือไม่
    for word in forbidden_words:
        # TODO 2: พิมพ์คำว่า in ในช่องว่างเพื่อเช็กคำต้องห้ามใน ai_response
        if word in ai_response.lower():
            return False, f"REJECTED: Contains forbidden word '{word}'"
            
    return True, "PASSED: Safe and valid response"

# =============================================================
# TESTING GUARDRAILS SYSTEM
# =============================================================
print("=== Day 7: AI Guardrails & Safety Test ===\n")

# เคสทดสอบที่ 1: ผ่านเกณฑ์
response_1 = "การประมวลผลข้อมูลเสร็จสิ้นตามมาตรฐาน"
# เคสทดสอบที่ 2: มีคำต้องห้าม (error)
response_2 = "เกิดข้อผิดพลาด internal error ในระบบ"

# รันการทดสอบเคสที่ 1
is_valid_1, message_1 = apply_guardrails(response_1)
print(f"[Test 1] Output: {response_1}\n  -> Result: {message_1}\n")

# TODO 3: เรียกใช้ฟังก์ชัน apply_guardrails กับตัวแปร response_2
is_valid_2, message_2 = apply_guardrails(response_2)
print(f"[Test 2] Output: {response_2}\n  -> Result: {message_2}\n")

if is_valid_1 and not is_valid_2:
    print("[SYSTEM CHECK] Guardrails are functioning perfectly!")