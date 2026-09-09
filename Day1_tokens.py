# day1_tokens.py - โปรแกรมประมาณการ Token เบื้องต้นสำหรับ LLM

def analyze_tokenomics(text: str, language_label: str) -> None:
    char_count = len(text)
    word_count = len(text.split())
    
    # คำนวณอัตราส่วนประมาณการ (English ~4 chars/token, Thai ~1.5 chars/token)
    has_thai = any('\u0e00' <= char <= '\u0e7f' for char in text)
    if has_thai:
        estimated_tokens = int(char_count / 1.5)
    else:
        estimated_tokens = int(char_count / 4.0)
        
    print(f"--- {language_label} Analysis ---")
    print(f"ข้อความ: \"{text}\"")
    print(f"จำนวนตัวอักษร (Characters): {char_count}")
    print(f"จำนวนคำ (Words): {word_count}")
    print(f"ประเมินจำนวน Token (Estimated Tokens): {estimated_tokens}")
    print(f"อัตราส่วน Efficiency: {char_count / estimated_tokens:.2f} chars/token\n")

# ข้อความทดสอบที่มีความหมายใกล้เคียงกัน
english_sample = "Artificial Intelligence models process text using tokenization algorithms."
thai_sample = "โมเดลปัญญาประดิษฐ์ประมวลผลข้อความโดยใช้ อัลกอริทึมการตัดโทเคน"

analyze_tokenomics(english_sample, "English Text")
analyze_tokenomics(thai_sample, "Thai Text")