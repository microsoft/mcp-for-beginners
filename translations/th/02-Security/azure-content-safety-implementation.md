<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b6c746d9e190deba4d8765267ffb94e",
  "translation_date": "2025-07-17T08:57:25+00:00",
  "source_file": "02-Security/azure-content-safety-implementation.md",
  "language_code": "th"
}
-->
# การใช้งาน Azure Content Safety กับ MCP

เพื่อเสริมความปลอดภัยของ MCP จากการโจมตีแบบ prompt injection, การโจมตีด้วยเครื่องมือที่เป็นอันตราย และช่องโหว่เฉพาะของ AI แนะนำให้ผสานรวม Azure Content Safety อย่างจริงจัง

## การผสานรวมกับ MCP Server

ในการผสานรวม Azure Content Safety กับ MCP server ของคุณ ให้เพิ่มตัวกรอง content safety เป็น middleware ในกระบวนการจัดการคำขอ:

1. เริ่มต้นตัวกรองในช่วงเริ่มต้นของเซิร์ฟเวอร์
2. ตรวจสอบคำขอเครื่องมือทั้งหมดที่เข้ามาก่อนการประมวลผล
3. ตรวจสอบการตอบกลับทั้งหมดก่อนส่งกลับไปยังลูกค้า
4. บันทึกและแจ้งเตือนเมื่อพบการละเมิดความปลอดภัย
5. ดำเนินการจัดการข้อผิดพลาดอย่างเหมาะสมเมื่อการตรวจสอบ content safety ล้มเหลว

วิธีนี้ช่วยป้องกันได้อย่างมีประสิทธิภาพจาก:
- การโจมตีแบบ prompt injection
- ความพยายามโจมตีด้วยเครื่องมือที่เป็นอันตราย
- การขโมยข้อมูลผ่านอินพุตที่เป็นอันตราย
- การสร้างเนื้อหาที่เป็นอันตราย

## แนวทางปฏิบัติที่ดีที่สุดสำหรับการผสานรวม Azure Content Safety

1. **รายการบล็อกแบบกำหนดเอง**: สร้างรายการบล็อกเฉพาะสำหรับรูปแบบการโจมตี MCP injection
2. **ปรับระดับความรุนแรง**: ปรับเกณฑ์ความรุนแรงตามกรณีการใช้งานและความเสี่ยงที่ยอมรับได้ของคุณ
3. **ครอบคลุมอย่างครบถ้วน**: ใช้การตรวจสอบ content safety กับอินพุตและเอาต์พุตทั้งหมด
4. **เพิ่มประสิทธิภาพการทำงาน**: พิจารณาการใช้แคชสำหรับการตรวจสอบ content safety ที่ทำซ้ำ
5. **กลไกสำรอง**: กำหนดพฤติกรรมสำรองที่ชัดเจนเมื่อบริการ content safety ไม่พร้อมใช้งาน
6. **ข้อเสนอแนะสำหรับผู้ใช้**: ให้ข้อเสนอแนะที่ชัดเจนแก่ผู้ใช้เมื่อเนื้อหาถูกบล็อกเนื่องจากข้อกังวลด้านความปลอดภัย
7. **ปรับปรุงอย่างต่อเนื่อง**: อัปเดตรายการบล็อกและรูปแบบอย่างสม่ำเสมอตามภัยคุกคามที่เกิดขึ้นใหม่

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้