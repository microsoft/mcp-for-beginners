# การรันตัวอย่างนี้

ตัวอย่างนี้เกี่ยวข้องกับการมี LLM อยู่บนฝั่งไคลเอนต์ โดย LLM ต้องการให้คุณรันใน Codespaces หรือให้คุณตั้งค่า personal access token ใน GitHub เพื่อใช้งาน

## -1- ติดตั้ง dependencies

```bash
npm install
```

## -3- รันเซิร์ฟเวอร์

```bash
npm run build
```

## -4- รันไคลเอนต์

```sh
npm run client
```

คุณควรเห็นผลลัพธ์ที่คล้ายกับ:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้