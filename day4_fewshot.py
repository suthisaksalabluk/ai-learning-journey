# day4_fewshot.py - Few-Shot Prompting & Context Management

# 1. นิยามโครงสร้าง Few-Shot Examples (ตัวอย่างสำหรับสอน AI)
few_shot_examples = [
    {"input": "สินค้าจัดส่งเร็วมาก ประทับใจสุดๆ", "output": "POSITIVE"},
    {"input": "สินค้าชำรุด ใช้งานไม่ได้เลย", "output": "NEGATIVE"}
]

# 2. ข้อความใหม่ที่ต้องการวัดผล
user_input = "บริการดีมาก แต่กล่องพัสดุยับไปหน่อย"

# TODO 1: พิมพ์ใส่เครื่องหมายวงเล็บเหลี่ยม [ ] เพื่อสร้าง List ครอบตัวแปรทั้งสอง
context_history = [few_shot_examples, user_input]

# 3. ประกอบ Context Window และ Few-Shot Prompts
prompt_text = "Classify sentiment as POSITIVE, NEGATIVE, or NEUTRAL.\n\n"

for example in few_shot_examples:
    prompt_text += f"Text: {example['input']}\nSentiment: {example['output']}\n\n"

prompt_text += f"Text: {user_input}\nSentiment:"

# TODO 2: พิมพ์ชื่อฟังก์ชัน len เพื่อคำนวณจำนวนตัวอักษรทั้งหมดใน Context Window
total_chars = len (prompt_text)

print("=== Day 4: Few-Shot Prompt & Context ===")
print(f"Generated Prompt:\n{prompt_text}\n")
print(f"Total Context Length: {total_chars} characters")