# day6_chaining.py - Day 6: Prompt Chaining & Multi-Step AI Pipelines

# ข้อมูลดิบที่ต้องการประมวลผล
raw_article = "ผู้ใช้สนใจเรียนเขียนโปรแกรมและ AI ตั้งแต่พื้นฐาน โดยเน้นการฝึกปฏิบัติวันละ 90 นาทีอย่างมีวินัย"

# =============================================================
# STEP 1: Fact Extraction (สกัดประเด็นสำคัญ)
# =============================================================
def step1_extract_facts(text):
    # TODO 1: พิมพ์ f-string นำตัวแปร text มาต่อในข้อความสั่งสกัดประเด็น
    # (คำใบ้: f"Extract key points from: {text}")
    prompt = f"Extract key points from: {text}"
    
    # จำลองผลลัพธ์ที่สกัดได้จาก AI Step 1
    ai_output_step1 = "- หัวข้อ: เรียนโปรแกรมมิ่งและ AI จากศูนย์\n- รูปแบบ: ฝึกปฏิบัติ 90 นาที/วัน"
    return ai_output_step1

# =============================================================
# STEP 2: Executive Summary Generation (สร้างสรุปผู้บริหาร)
# =============================================================
def step2_generate_summary(extracted_facts):
    # TODO 2: พิมพ์ f-string นำตัวแปร extracted_facts มาต่อในคำสั่งสร้างสรุป
    # (คำใบ้: f"Create executive summary based on: {extracted_facts}")
    prompt = f"Create executive summary based on: {extracted_facts}"
    
    # จำลองผลลัพธ์ที่สรุปได้จาก AI Step 2 (รับผลจาก Step 1 มาใช้)
    ai_output_step2 = f"=== EXECUTIVE SUMMARY ===\n{extracted_facts}\nStatus: APPROVED"
    return ai_output_step2

# =============================================================
# MAIN PIPELINE EXECUTION (ร้อยต่อท่อทำงาน)
# =============================================================
print("=== Day 6: Prompt Chaining Execution ===\n")

# 1. รัน Step 1
facts = step1_extract_facts(raw_article)
print(f"[Step 1 Output - Extracted Facts]:\n{facts}\n")

# 2. รัน Step 2 โดยเอาผลลัพธ์จาก Step 1 (ตัวแปร facts) ส่งต่อเข้าไปเป็น Input
# TODO 3: พิมพ์ชื่อฟังก์ชัน step2_generate_summary แล้วส่งตัวแปร facts เข้าไปในวงเล็บ
final_summary = step2_generate_summary(facts)

print(f"[Step 2 Output - Final Chained Result]:\n{final_summary}\n")

# ตรวจสอบการเชื่อมต่อ Pipeline
if "APPROVED" in final_summary:
    print("[PIPELINE SUCCESS] Multi-step prompt chaining completed!")
else:
    print("[PIPELINE FAILED] Chain broken!")