# day5_cot.py - Day 5: Chain-of-Thought (CoT) Prompting & Multi-Step Reasoning Pipeline

# =============================================================
# PART 1: Concept & CoT System Prompt Setup (Warm-Up)
# =============================================================
problem_statement = "ส่ง 1,500 Input Tokens และ 500 Output Tokens (อัตรา: Input $0.001/1k, Output $0.003/1k, $1 = 36 บาท) รวมเป็นเงินกี่บาท?"

# TODO 1: พิมพ์ System Prompt สั่งให้ AI ต้องคิดแบบทีละสเต็ปก่อนตอบเสมอ
# (คำใบ้: ใส่ข้อความภาษาอังกฤษว่า "You are a logic engine. Always think step-by-step before answering.")
system_prompt = "You are a logic engine. always think step by step before answering."


# =============================================================
# PART 2: Main Challenge - Reasoning Validation Function
# =============================================================
# เขียนฟังก์ชันตรวจเช็กว่าขั้นตอนการคิด (Reasoning Steps) มีความละเอียดเพียงพอหรือไม่ (ต้องมีอย่างน้อย 3 ขั้นตอน)

def validate_cot_reasoning(steps_list):
    # TODO 2: พิมพ์เงื่อนไข if / else เช็กว่าจำนวนสมาชิกใน steps_list มีตั้งแต่ 3 ขึ้นไปหรือไม่ (ใช้อักขระ >=)
    if len(steps_list) >= 3:
        return True
    else:
        return False


# จำลองขั้นตอนการคิดที่สกัดออกมาจาก AI (กรณีผ่านเกณฑ์)
ai_steps_pass = [
    "Step 1: Input cost = (1500 / 1000) * 0.001 = $0.0015",
    "Step 2: Output cost = (500 / 1000) * 0.003 = $0.0015",
    "Step 3: Total USD = $0.0015 + $0.0015 = $0.0030",
    "Step 4: Total THB = $0.0030 * 36 = 0.108 Baht"
]

# จำลองขั้นตอนการคิดที่สั้นเกินไป (กรณีไม่ผ่านเกณฑ์)
ai_steps_fail = [
    "Step 1: รวมทั้งหมดคิดเป็น 0.108 บาท"
]


# =============================================================
# PART 3: Execution & Logic Testing
# =============================================================
print("=== Day 5: Chain-of-Thought (CoT) Verification ===\n")

# ทดสอบกรณีที่ 1: รายการขั้นตอนครบถ้วน
if validate_cot_reasoning(ai_steps_pass):
    print("[TEST 1 PASSED] Valid Reasoning Chain detected:")
    for step in ai_steps_pass:
        print(f"   -> {step}")
else:
    print("[TEST 1 FAILED] Reasoning chain is too short!")

print("\n" + "="*50 + "\n")

# TODO 3: เขียนคำสั่ง if / else สำหรับทดสอบกรณีที่ 2 (ai_steps_fail) 
if validate_cot_reasoning(ai_steps_fail):
    print("[TEST 2 PASSED] Valid Reasoning Chain")
else:
    print("[TEST 2 REJECTED] Steps incomplete!")
# =============================================================
# PART 2: Main Challenge - CoT Reasoning & Answer Extractor
# =============================================================
print("\n" + "="*50)
print("=== PART 2: Real CoT Pipeline Processing ===\n")

# ข้อความตอบกลับจำลองจาก AI ที่ใช้เทคนิค CoT
raw_ai_response = """
Reasoning Steps:
1. คำนวณ Tokens รวม: 1500 + 500 = 2000 tokens
2. คำนวณราคา USD: (1500/1000)*0.001 + (500/1000)*0.003 = 0.003 USD
3. แปลงเป็นเงินบาท: 0.003 * 36 = 0.108 บาท
FINAL ANSWER: 0.108 บาท
"""

def extract_final_answer(response_text):
    # TODO 4: เขียนตรรกะตรวจสอบว่าในข้อความตอบกลับมีคำว่า "FINAL ANSWER:" อยู่หรือไม่
    # (คำใบ้: ใช้ตัวดำเนินการ in ในการเช็กข้อความ)
    if "FINAL ANSWER:" in response_text:
        # สกัดเอาข้อความส่วนหลังคำว่า FINAL ANSWER:
        parts = response_text.split("FINAL ANSWER:")
        return parts[1].strip()
    else:
        return "No explicit final answer found."

# TODO 5: เรียกใช้ฟังก์ชัน extract_final_answer โดยส่งตัวแปร raw_ai_response เข้าไป
final_result = extract_final_answer(raw_ai_response)

print(f"Extracted Final Answer: {final_result}")    