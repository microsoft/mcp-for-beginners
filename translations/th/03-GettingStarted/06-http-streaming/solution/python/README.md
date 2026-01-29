# การรันตัวอย่างนี้

นี่คือวิธีการรันเซิร์ฟเวอร์และไคลเอนต์ HTTP แบบสตรีมมิ่งแบบคลาสสิก รวมถึงเซิร์ฟเวอร์และไคลเอนต์ MCP สตรีมมิ่งโดยใช้ Python

### ภาพรวม

- คุณจะตั้งค่าเซิร์ฟเวอร์ MCP ที่ส่งการแจ้งเตือนความคืบหน้าไปยังไคลเอนต์ขณะประมวลผลรายการต่างๆ
- ไคลเอนต์จะแสดงการแจ้งเตือนแต่ละรายการแบบเรียลไทม์
- คู่มือนี้ครอบคลุมถึงข้อกำหนดเบื้องต้น การตั้งค่า การรัน และการแก้ไขปัญหา

### ข้อกำหนดเบื้องต้น

- Python 3.9 หรือใหม่กว่า
- แพ็กเกจ Python `mcp` (ติดตั้งด้วย `pip install mcp`)

### การติดตั้งและตั้งค่า

1. โคลน repository หรือดาวน์โหลดไฟล์โซลูชัน

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **สร้างและเปิดใช้งาน virtual environment (แนะนำ):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **ติดตั้ง dependencies ที่จำเป็น:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### ไฟล์

- **เซิร์ฟเวอร์:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **ไคลเอนต์:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### การรันเซิร์ฟเวอร์ HTTP สตรีมมิ่งแบบคลาสสิก

1. ไปที่ไดเรกทอรีโซลูชัน:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. เริ่มเซิร์ฟเวอร์ HTTP สตรีมมิ่งแบบคลาสสิก:

   ```pwsh
   python server.py
   ```

3. เซิร์ฟเวอร์จะเริ่มต้นและแสดงผลดังนี้:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### การรันไคลเอนต์ HTTP สตรีมมิ่งแบบคลาสสิก

1. เปิด terminal ใหม่ (เปิดใช้งาน virtual environment และไดเรกทอรีเดียวกัน):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. คุณจะเห็นข้อความที่สตรีมแสดงผลตามลำดับ:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### การรันเซิร์ฟเวอร์ MCP สตรีมมิ่ง

1. ไปที่ไดเรกทอรีโซลูชัน:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. เริ่มเซิร์ฟเวอร์ MCP ด้วย streamable-http transport:
   ```pwsh
   python server.py mcp
   ```
3. เซิร์ฟเวอร์จะเริ่มต้นและแสดงผลดังนี้:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### การรันไคลเอนต์ MCP สตรีมมิ่ง

1. เปิด terminal ใหม่ (เปิดใช้งาน virtual environment และไดเรกทอรีเดียวกัน):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. คุณจะเห็นการแจ้งเตือนแสดงผลแบบเรียลไทม์ขณะที่เซิร์ฟเวอร์ประมวลผลแต่ละรายการ:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### ขั้นตอนการดำเนินการที่สำคัญ

1. **สร้างเซิร์ฟเวอร์ MCP โดยใช้ FastMCP**
2. **กำหนดเครื่องมือที่ประมวลผลรายการและส่งการแจ้งเตือนโดยใช้ `ctx.info()` หรือ `ctx.log()`**
3. **รันเซิร์ฟเวอร์ด้วย `transport="streamable-http"`**
4. **สร้างไคลเอนต์ที่มี message handler เพื่อแสดงการแจ้งเตือนเมื่อได้รับ**

### การอธิบายโค้ด
- เซิร์ฟเวอร์ใช้ฟังก์ชันแบบ async และ MCP context เพื่อส่งการอัปเดตความคืบหน้า
- ไคลเอนต์มี message handler แบบ async เพื่อแสดงการแจ้งเตือนและผลลัพธ์สุดท้าย

### เคล็ดลับและการแก้ไขปัญหา

- ใช้ `async/await` สำหรับการดำเนินการที่ไม่บล็อก
- จัดการข้อยกเว้นในทั้งเซิร์ฟเวอร์และไคลเอนต์เพื่อความเสถียร
- ทดสอบด้วยไคลเอนต์หลายตัวเพื่อดูการอัปเดตแบบเรียลไทม์
- หากพบข้อผิดพลาด ตรวจสอบเวอร์ชัน Python และตรวจสอบว่าได้ติดตั้ง dependencies ทั้งหมดแล้ว

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้