# day8_rag_basic.py - Day 8: RAG Foundations (Search & Context Augmentation)

# 1. ฐานข้อมูลความรู้ (Knowledge Base / Context Store)
knowledge_base = [
    {"topic": "Python", "content": "Python เป็นภาษาโปรแกรมที่อ่านง่าย เหมาะสำหรับงาน Data Science และ AI"},
    {"topic": "Git", "content": "Git เป็นระบบ Version Control สำหรับติดตามการเปลี่ยนแปลงของไฟล์โค้ด"},
    {"topic": "RAG", "content": "RAG ย่อมาจาก Retrieval-Augmented Generation ช่วยดึงเอกสารมาเสริมคำตอบ AI"}
]

# 2. ฟังก์ชันค้นหาข้อมูลที่เกี่ยวข้อง (Retriever)
def search_knowledge_base(query):
    for item in knowledge_base:
        # TODO 1: พิมพ์คำว่า in เพื่อเช็กว่าชื่อ topic อยู่ในคำถามหรือไม่ (ใช้อักษรตัวพิมพ์เล็ก)
        if item["topic"].lower() in query.lower():
            return item["content"]
    return "ไม่พบข้อมูลที่เกี่ยวข้องในระบบ"

# 3. ฟังก์ชันประกอบ Prompt (Augmentation)
def build_augmented_prompt(user_query, retrieved_context):
    # TODO 2: พิมพ์ f-string นำ context และ query มาเติมในโครงสร้าง Prompt
    # (คำใบ้: f"Context: {retrieved_context}\nQuestion: {user_query}")
    augmented_prompt = f"Context: {retrieved_context}\nQuestion: {user_query}"
    return augmented_prompt

# =============================================================
# EXECUTION & RAG SIMULATION
# =============================================================
print("=== Day 8: RAG System Simulation ===\n")

user_question = "อยากรู้ว่า RAG คืออะไร?"

# 1. Retrieve Step (ค้นหาข้อมูล)
# TODO 3: เรียกใช้ฟังก์ชัน search_knowledge_base โดยส่งตัวแปร user_question เข้าไป
context = search_knowledge_base(user_question)
print(f"[1. Retrieved Context]: {context}\n")

# 2. Augment Step (รวมข้อมูลเข้ากับคำถาม)
final_prompt = build_augmented_prompt(user_question, context)
print(f"[2. Final Augmented Prompt to AI]:\n{final_prompt}\n")

if "Retrieval-Augmented Generation" in final_prompt:
    print("[RAG SUCCESS] Context successfully retrieved and augmented!")