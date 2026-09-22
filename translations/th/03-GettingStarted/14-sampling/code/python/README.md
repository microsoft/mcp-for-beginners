# รันตัวอย่าง

> [!WARNING]
> ตัวอย่างนี้ใช้ Sampling ที่ถูกเลิกใช้และจุดสิ้นสุด HTTP+SSE แบบเดิม มันถูก
> เก็บไว้เพื่อความเข้ากันได้กับ MCP `2025-11-25` การใช้งานใหม่ควรเรียก
> ผู้ให้บริการ LLM โดยตรงและใช้ Streamable HTTP สำหรับการรับส่งข้อมูล MCP ระยะไกล

## สร้างสภาพแวดล้อมเสมือน

```sh
python -m venv venv
source ./venv/bin/activate
```

## ติดตั้ง dependencies

```sh
pip install "mcp[cli]"
```

## รันเซิร์ฟเวอร์

```sh
uvicorn server:app --port 8000
```

## ทดสอบเซิร์ฟเวอร์ด้วย GitHub Copilot และ VS Code

เพิ่มรายการเข้าไปใน mcp.json ดังนี้:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

ตรวจสอบให้แน่ใจว่าคลิก "start" บนเซิร์ฟเวอร์แล้ว

ใน GitHub Copilot ให้วาง prompt ดังต่อไปนี้:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

ครั้งแรกคุณจะถูกถามว่าต้องการยอมรับการกระทำ Sampling หรือไม่ จากนั้นจะถูกถามให้ยอมรับเครื่องมือเพื่อรัน "create_blog" คุณควรเห็นการตอบกลับคล้ายกับ:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->