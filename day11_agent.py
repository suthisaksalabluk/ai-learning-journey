# day11_agent.py - Day 11: Autonomous AI Agent Loop & Memory State

# 1. สถานะและหน่วยความจำของ Agent (Memory & State Control)
agent_state = {
    "task": "รวบรวมข้อมูลและสรุปรายงาน AI",
    "step": 0,
    "max_steps": 3,
    "status": "RUNNING"
}

# 2. ฟังก์ชันจำลองการทำงานแต่ละสเต็ป (Think -> Act -> Observe)
def run_agent_step(current_step):
    steps_log = [
        "Step 1: [Think] ต้องค้นหาข้อมูลล่าสุด -> [Act] Search Web",
        "Step 2: [Think] ได้ข้อมูลแล้ว -> [Act] Summarize Content",
        "Step 3: [Think] สรุปเสร็จเรียบร้อย -> [Act] Complete Task"
    ]
    return steps_log[current_step]

print("=== Day 11: Autonomous AI Agent Execution Loop ===\n")

# TODO 1: พิมพ์คำว่า while เพื่อสั่งให้ Agent ทำงานวนลูปตราบใดที่ status ยังเป็น "RUNNING"
while agent_state["status"] == "RUNNING":
    current_step = agent_state["step"]
    action_log = run_agent_step(current_step)
    print(f"[Agent Action Log] {action_log}")
    
    # อัปเดตจำนวนรอบการทำงาน
    agent_state["step"] += 1
    
    # TODO 2: พิมพ์คำสั่ง if เพื่อเช็กว่าทำครบตาม max_steps หรือยัง
    if agent_state["step"] >= agent_state["max_steps"]:
        agent_state["status"] = "FINISHED"

# TODO 3: พิมพ์ชื่อตัวแปร agent_state ในช่องว่างทั้งสองจุด เพื่อดึงค่า task และ status มาแสดงผล
print(f"\n[Agent Final Memory]: Task={agent_state['task']} | Status={agent_state['status']}")

if agent_state["status"] == "FINISHED":
    print("\n[AGENT SUCCESS] Autonomous Loop completed all tasks safely!")