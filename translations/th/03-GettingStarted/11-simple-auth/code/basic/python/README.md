# รันตัวอย่าง

ตัวอย่างนี้เริ่มต้น MCP Server พร้อมกับ middleware ที่ตรวจสอบว่า Authorization header นั้นถูกต้องหรือไม่

## ติดตั้ง dependencies

```bash
pip install "mcp[cli]" 
```

## เริ่มเซิร์ฟเวอร์

```bash
python server.py
```

เริ่มต้น client ใน terminal อื่น

```bash
python client.py
```

คุณควรเห็นผลลัพธ์ที่คล้ายกับ:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

ซึ่งหมายความว่า credential ที่ถูกส่งผ่านนั้นได้รับการอนุญาต

ลองเปลี่ยน credential ใน `client.py` เป็น "secret-token2" แล้วคุณควรเห็นข้อความนี้เป็นส่วนหนึ่งของการตอบกลับ:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

ซึ่งหมายความว่าคุณได้รับการตรวจสอบสิทธิ์ (คุณมี credential) แต่ credential นั้นไม่ถูกต้อง

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้