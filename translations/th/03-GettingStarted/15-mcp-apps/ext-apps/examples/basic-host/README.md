# Example: Basic Host

ตัวอย่างอ้างอิงที่แสดงวิธีการสร้างแอปโฮสต์ MCP ที่เชื่อมต่อกับเซิร์ฟเวอร์ MCP และแสดง UI ของเครื่องมือใน sandbox ที่ปลอดภัย

โฮสต์ขั้นพื้นฐานนี้ยังสามารถใช้ทดสอบ MCP Apps ในระหว่างการพัฒนาแบบโลคอลได้อีกด้วย

## ไฟล์สำคัญ

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - โฮสต์ UI React พร้อมการเลือกเครื่องมือ กรอกพารามิเตอร์ และจัดการ iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - ตัวแทน iframe ด้านนอกพร้อมการตรวจสอบความปลอดภัยและการส่งต่อข้อความสองทิศทาง
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - ตรรกะหลัก: การเชื่อมต่อเซิร์ฟเวอร์ การเรียกใช้เครื่องมือ และการตั้งค่า AppBridge

## การเริ่มต้นใช้งาน

```bash
npm install
npm run start
# เปิด http://localhost:8080
```

โดยค่าเริ่มต้น แอปโฮสต์จะพยายามเชื่อมต่อกับเซิร์ฟเวอร์ MCP ที่ `http://localhost:3001/mcp` คุณสามารถกำหนดพฤติกรรมนี้ได้โดยตั้งค่าตัวแปรแวดล้อม `SERVERS` ด้วยอาร์เรย์ JSON ของ URL เซิร์ฟเวอร์:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## สถาปัตยกรรม

ตัวอย่างนี้ใช้รูปแบบ sandbox แบบ double-iframe เพื่อแยก UI ออกจากกันอย่างปลอดภัย:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**ทำไมต้องใช้ iframe สองตัว?**

- iframe ด้านนอกทำงานบนต้นทางที่แยกต่างหาก (พอร์ต 8081) ป้องกันการเข้าถึงโดยตรงกับโฮสต์
- iframe ด้านในรับ HTML ผ่าน `srcdoc` และถูกจำกัดด้วยแอตทริบิวต์ sandbox
- ข้อความไหลผ่าน iframe ด้านนอกซึ่งจะตรวจสอบและส่งต่อข้อความสองทิศทาง

สถาปัตยกรรมนี้ช่วยให้มั่นใจได้ว่าแม้ว่ารหัส UI ของเครื่องมือจะประสงค์ร้าย ก็ไม่สามารถเข้าถึง DOM, คุกกี้ หรือบริบท JavaScript ของแอปโฮสต์ได้

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลโดยระบบอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อนได้ เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่ถูกต้องและเชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์มืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดเกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->