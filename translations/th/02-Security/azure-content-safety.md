# ความปลอดภัยขั้นสูงของ MCP ด้วย Azure Content Safety

Azure Content Safety มีเครื่องมือทรงพลังหลายอย่างที่ช่วยเพิ่มความปลอดภัยให้กับการใช้งาน MCP ของคุณ:

## Prompt Shields

AI Prompt Shields ของ Microsoft ให้การปกป้องที่แข็งแกร่งจากการโจมตีแบบ prompt injection ทั้งโดยตรงและโดยอ้อม ผ่าน:

1. **การตรวจจับขั้นสูง**: ใช้การเรียนรู้ของเครื่องเพื่อระบุคำสั่งที่เป็นอันตรายซ่อนอยู่ในเนื้อหา
2. **การเน้นจุดสำคัญ**: แปลงข้อความนำเข้าเพื่อช่วยให้ระบบ AI แยกแยะระหว่างคำสั่งที่ถูกต้องกับข้อมูลภายนอก
3. **ตัวคั่นและการทำเครื่องหมายข้อมูล**: กำหนดขอบเขตระหว่างข้อมูลที่เชื่อถือได้และข้อมูลที่ไม่น่าเชื่อถือ
4. **การผสานรวมกับ Content Safety**: ทำงานร่วมกับ Azure AI Content Safety เพื่อตรวจจับความพยายามเจลเบรกและเนื้อหาที่เป็นอันตราย
5. **การอัปเดตอย่างต่อเนื่อง**: Microsoft อัปเดตกลไกการป้องกันอย่างสม่ำเสมอเพื่อต่อสู้กับภัยคุกคามใหม่ๆ

## การใช้งาน Azure Content Safety กับ MCP

แนวทางนี้ให้การปกป้องหลายชั้น:
- สแกนข้อมูลนำเข้าก่อนประมวลผล
- ตรวจสอบผลลัพธ์ก่อนส่งกลับ
- ใช้บล็อกลิสต์สำหรับรูปแบบที่เป็นอันตรายที่รู้จัก
- ใช้โมเดล Content Safety ของ Azure ที่อัปเดตอย่างต่อเนื่อง

## แหล่งข้อมูล Azure Content Safety

หากต้องการเรียนรู้เพิ่มเติมเกี่ยวกับการใช้งาน Azure Content Safety กับเซิร์ฟเวอร์ MCP ของคุณ ให้ดูแหล่งข้อมูลอย่างเป็นทางการเหล่านี้:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - เอกสารอย่างเป็นทางการของ Azure Content Safety
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - เรียนรู้วิธีป้องกันการโจมตีแบบ prompt injection
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - เอกสารอ้างอิง API สำหรับการใช้งาน Content Safety
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - คู่มือเริ่มต้นใช้งานด้วย C#
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - ไลบรารีสำหรับลูกค้าในหลายภาษาโปรแกรม
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - คำแนะนำเฉพาะสำหรับการตรวจจับและป้องกันความพยายามเจลเบรก
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - แนวทางปฏิบัติที่ดีที่สุดสำหรับการใช้งาน Content Safety อย่างมีประสิทธิภาพ

สำหรับการใช้งานที่ลึกซึ้งยิ่งขึ้น ดูได้จาก [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md) ของเรา

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้