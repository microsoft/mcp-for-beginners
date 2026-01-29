# รันตัวอย่าง

## ติดตั้ง dependencies

```sh
npm install
```

## สร้างโปรเจกต์

```sh
npm run build
```

## สร้าง tokens

```sh
npm run generate
```

การดำเนินการนี้จะสร้าง token ในไฟล์ *.env* ซึ่ง client จะอ่านข้อมูลจากไฟล์นี้

## รันโค้ด

เริ่มต้นเซิร์ฟเวอร์ด้วย:

```sh
npm start
```

รัน client ใน terminal แยกต่างหากด้วย:

```sh
npm run client
```

ใน terminal ของเซิร์ฟเวอร์ คุณควรเห็นผลลัพธ์ที่คล้ายกับ:

```text
User exists
User has required scopes
Middleware executed
```

และใน terminal ของ client คุณควรเห็นผลลัพธ์ที่คล้ายกับ:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### การเปลี่ยนแปลง

มาทำความเข้าใจเกี่ยวกับ scopes กันก่อน ค้นหาไฟล์ *server.ts* และโค้ดนี้:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

โค้ดนี้ระบุว่า token ที่ส่งมาจะต้องมี "User.Read" ลองเปลี่ยนเป็น "User.Write" จากนั้นรันคำสั่ง `npm run build` และรีสตาร์ทเซิร์ฟเวอร์ด้วย `npm start` คุณควรเห็นการตรวจสอบสิทธิ์ล้มเหลว เนื่องจากเราไม่มี scope นี้ (เรามี User.Read และ Admin.Write):

ตอนนี้ client จะแสดงข้อความว่า

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

และคุณจะเห็นใน terminal ของเซิร์ฟเวอร์ว่าแสดงข้อความว่า:

```text
User exists
```

และมันจะไม่ดำเนินการต่อจากจุดนี้

คุณสามารถเพิ่ม scope "User.Write" และรันคำสั่ง `npm run generate` แล้วรัน client ใหม่ หรือเปลี่ยนโค้ดเซิร์ฟเวอร์กลับไปเป็นแบบเดิม

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้