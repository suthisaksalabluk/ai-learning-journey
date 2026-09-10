# day3_prompts.py - Guided Coding: System Prompts & Parameter Tuning

# 1. กำหนด System Prompt (บทบาท AI) และ User Prompt (คำถาม)
system_prompt = "You are an expert Python tutor."
user_prompt = "How do I print text in Python?"

# 2. ตั้งค่า Parameter
# TODO 1: พิมพ์เติมตัวเลข 0.2 หลังเครื่องหมาย = เพื่อตั้งค่าให้ AI ตอบเน้นความแม่นยำ
temperature = 0.2

# 3. สร้างเงื่อนไขตรวจสอบโหมดการทำงาน
# TODO 2: พิมพ์คำสั่ง if เติมในช่องว่างเพื่อเช็กว่าถ้า temperature น้อยกว่า 0.5
if temperature < 0.5:
    mode = "Precise & Deterministic"
else:
    mode = "Creative & Diverse"

# 4. รวมข้อมูลเป็น Payload
payload = {
    "system": system_prompt,
    "user": user_prompt,
    "temperature": temperature,
    "mode": mode
}

print("=== Day 3: Prompt & Parameter Config ===")
print(f"Role: {payload['system']}")
print(f"Prompt: {payload['user']}")
print(f"Config: Temp {payload['temperature']} -> {payload['mode']}")