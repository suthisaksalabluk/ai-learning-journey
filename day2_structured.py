# day2_structured.py - ตัวอย่างการจัดการ Structured Output & Schema Control

import json

# 1. จำลองข้อความดิบ (Raw Output) ที่ได้รับกลับมาจาก LLM
raw_ai_response = """
{
    "status": "success",
    "data": {
        "topic": "Tokenomics Analysis",
        "english_efficiency": "4.11 chars/token",
        "thai_efficiency": "1.52 chars/token",
        "recommendation": "Use English for system prompts to optimize context window."
    }
}
"""

# 2. ตรวจสอบและแปลงข้อความให้เป็น JSON Object (Parsing & Validation)
try:
    parsed_data = json.loads(raw_ai_response)
    print("=== 1. JSON Parsing & Schema Validation ===")
    print(f"Status: {parsed_data['status']}")
    print(f"Topic: {parsed_data['data']['topic']}")
    print(f"Recommendation: {parsed_data['data']['recommendation']}\n")
except json.JSONDecodeError as e:
    print(f"Error: ข้อมูลที่ได้ไม่อยู่ในรูปแบบ JSON ที่ถูกต้อง - {e}\n")

# 3. แปลงข้อมูลเชิงโครงสร้างให้อยู่ในรูปตาราง Markdown
print("=== 2. Structured Markdown Table Output ===")
markdown_table = f"""
| Metric | English Text | Thai Text |
| :--- | :--- | :--- |
| Efficiency | {parsed_data['data']['english_efficiency']} | {parsed_data['data']['thai_efficiency']} |
| Impact | Standard Cost | ~2.5x Higher Cost |
"""
print(markdown_table.strip())