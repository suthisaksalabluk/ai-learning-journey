# day10_tools.py - Day 10: Function Calling & Tool Selection Foundations

# 1. รายชื่อ เครื่องมือ (Tools) ที่มีในระบบ
available_tools = {
    "get_weather": "ดึงข้อมูลสภาพอากาศล่าสุด",
    "calculate_math": "คำนวณตัวเลขและสมการทางคณิตศาสตร์"
}

# 2. ฟังก์ชัน Router จำลองการเลือก Tool ของ AI
def route_user_intent(user_query):
    query = user_query.lower()
    
    if "คำนวณ" in query or "บวก" in query or "คูณ" in query:
        return "calculate_math"
    # TODO 1: พิมพ์คำว่า elif เพื่อสร้างเงื่อนไขตรวจสอบถัดไป
    elif "อากาศ" in query or "ฝน" in query:
        return "get_weather"
    else:
        return "general_chat"

# 3. ฟังก์ชันจำลองการเรียกใช้ Tool จริง
def execute_tool(tool_name):
    # TODO 2: พิมพ์คำสั่ง in เพื่อเช็กว่า tool_name อยู่ใน available_tools หรือไม่
    if tool_name in available_tools:
        return f"Executing Tool [{tool_name}]: {available_tools[tool_name]}"
    return "No specialized tool needed. Responding via LLM base knowledge."

# =============================================================
# EXECUTION & TOOL ROUTING TEST
# =============================================================
print("=== Day 10: AI Function Calling & Tool Selection ===\n")

user_question = "วันนี้ฝนจะตกไหม อยากเช็กสภาพอากาศ"

# รันขั้นตอนที่ 1: เลือก Tool
selected_tool = route_user_intent(user_question)
print(f"[User Query]: {user_question}")
print(f"[Selected Tool]: {selected_tool}\n")

# รันขั้นตอนที่ 2: เรียกใช้งาน Tool
# TODO 3: เรียกใช้ฟังก์ชัน execute_tool โดยส่งตัวแปร selected_tool เข้าไป
execution_result = execute_tool(selected_tool)
print(f"[Tool Execution Result]: {execution_result}\n")

if "get_weather" in selected_tool:
    print("[FUNCTION CALLING SUCCESS] AI successfully selected and routed to the correct tool!")