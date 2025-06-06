<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b0de03f7a3ff0204d8356bc61325c459",
  "translation_date": "2025-06-02T20:04:18+00:00",
  "source_file": "05-AdvancedTopics/mcp-sampling/README.md",
  "language_code": "th"
}
-->
## การสุ่มแบบกำหนดผลลัพธ์แน่นอน

สำหรับแอปพลิเคชันที่ต้องการผลลัพธ์ที่สม่ำเสมอ การสุ่มแบบกำหนดผลลัพธ์แน่นอนจะช่วยให้ได้ผลลัพธ์ที่ทำซ้ำได้ วิธีการคือการใช้ค่า random seed ที่คงที่และตั้งค่า temperature เป็นศูนย์

มาดูตัวอย่างการใช้งานเพื่อแสดงการสุ่มแบบกำหนดผลลัพธ์แน่นอนในภาษาการเขียนโปรแกรมต่างๆ

## การกำหนดค่าการสุ่มแบบไดนามิก

การสุ่มอย่างชาญฉลาดจะปรับพารามิเตอร์ตามบริบทและความต้องการของแต่ละคำขอ นั่นหมายถึงการปรับค่า temperature, top_p และ penalties อย่างไดนามิกตามประเภทงาน ความชอบของผู้ใช้ หรือประสิทธิภาพที่ผ่านมา

มาดูวิธีการใช้งานการสุ่มแบบไดนามิกในภาษาการเขียนโปรแกรมต่างๆ

## ต่อไปคืออะไร

- [Scaling](../mcp-scaling/README.md)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญที่เป็นมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดจากการใช้การแปลฉบับนี้