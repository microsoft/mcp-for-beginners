# Calculator LLM Client

แอปพลิเคชัน Java ที่แสดงตัวอย่างวิธีใช้ LangChain4j เพื่อเชื่อมต่อกับบริการเครื่องคิดเลข MCP (Model Context Protocol) ผ่าน API MiniMax ที่รองรับ OpenAI

## ข้อกำหนดเบื้องต้น

- Java 21 หรือสูงกว่า
- Maven 3.6+ (หรือใช้ Maven wrapper ที่มาพร้อม)
- กุญแจ API MiniMax
- บริการเครื่องคิดเลข MCP ที่รันอยู่บน `http://localhost:8080`

## การรับกุญแจ API

แอปพลิเคชันนี้ใช้ MiniMax API ที่รองรับ OpenAI ทำตามขั้นตอนเหล่านี้เพื่อรับกุญแจและจุดเชื่อมต่อของคุณ:

### 1. เลือกจุดเชื่อมต่อ
1. ใช้ `https://api.minimax.io/v1` สำหรับจุดเชื่อมต่อทั่วโลก
2. ใช้ `https://api.minimaxi.com/v1` สำหรับจุดเชื่อมต่อในประเทศจีน

### 2. สร้างกุญแจ API
1. สร้างกุญแจ API MiniMax จากบัญชี MiniMax ของคุณ
2. เก็บกุญแจไว้อย่างปลอดภัย

### 3. ตั้งค่าตัวแปรสภาพแวดล้อม

#### บน Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### บน Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### บน macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## การตั้งค่าและติดตั้ง

1. **โคลน หรือไปที่ไดเรกทอรีโปรเจกต์**

2. **ติดตั้ง dependencies**:
   ```cmd
   mvnw clean install
   ```
   หรือหากคุณติดตั้ง Maven ไว้ทั่วระบบ:
   ```cmd
   mvn clean install
   ```

3. **ตั้งค่าตัวแปรสภาพแวดล้อม** (ดูที่ส่วน "การรับกุญแจ API" ข้างต้น)

4. **เริ่มบริการเครื่องคิดเลข MCP**:
   ตรวจสอบให้แน่ใจว่าคุณมีบริการเครื่องคิดเลข MCP จากบทที่ 1 รันอยู่ที่ `http://localhost:8080/sse` ซึ่งจะต้องเริ่มก่อนที่จะรันไคลเอนต์

## การรันแอปพลิเคชัน

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## สิ่งที่แอปพลิเคชันทำ

แอปพลิเคชันสาธิตสามการโต้ตอบหลักกับบริการเครื่องคิดเลข:

1. **การบวก**: คำนวณผลรวมของ 24.5 และ 17.3
2. **รากที่สอง**: คำนวณรากที่สองของ 144
3. **ความช่วยเหลือ**: แสดงฟังก์ชันเครื่องคิดเลขที่มีให้ใช้

## ผลลัพธ์ที่คาดหวัง

เมื่อรันสำเร็จ คุณจะเห็นผลลัพธ์คล้ายกับ:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## การแก้ไขปัญหา

### ปัญหาทั่วไป

1. **"ตัวแปรสภาพแวดล้อม OPENAI_API_KEY ยังไม่ได้ตั้งค่า"**
   - ตรวจสอบว่าคุณได้ตั้งค่าตัวแปรสภาพแวดล้อม `OPENAI_API_KEY` แล้ว
   - รีสตาร์ทเทอร์มินัล/คอมมานด์พรอมต์หลังตั้งค่าตัวแปร

2. **"เชื่อมต่อกับ localhost:8080 ถูกปฏิเสธ"**
   - ตรวจสอบว่าบริการเครื่องคิดเลข MCP กำลังรันบนพอร์ต 8080
   - ตรวจสอบว่าบริการอื่นแย่งใช้พอร์ต 8080 หรือไม่

3. **"การยืนยันตัวตนล้มเหลว"**
   - ตรวจสอบกุญแจ API ของคุณว่าถูกต้องหรือไม่
   - ตรวจสอบว่า `OPENAI_BASE_URL` ตรงกับจุดเชื่อมต่อที่คุณต้องการใช้

4. **ข้อผิดพลาดการสร้าง Maven**
   - ตรวจสอบว่าคุณใช้ Java 21 หรือสูงกว่า: `java -version`
   - ลองทำความสะอาดการสร้างโปรเจกต์: `mvnw clean`

### การดีบัก

เพื่อเปิดใช้งานการบันทึกดีบัก ให้เพิ่มอาร์กิวเมนต์ JVM ต่อไปนี้เวลารัน:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## การกำหนดค่า

แอปพลิเคชันถูกตั้งค่าให้:
- ใช้ MiniMax-M3 เป็นค่าเริ่มต้น; ตั้งค่า `MINIMAX_MODEL_ID` เพื่อเลือก `MiniMax-M3` หรือ `MiniMax-M2.7`
- เชื่อมต่อกับ `OPENAI_BASE_URL` เมื่อมีการตั้งค่า; หากไม่ตั้งค่า ใช้ `https://api.minimaxi.com/v1` เมื่อ `MINIMAX_REGION=cn_zh` หรือใช้ `https://api.minimax.io/v1` เป็นค่าเริ่มต้น
- เชื่อมต่อกับบริการ MCP ที่ `http://localhost:8080/sse`
- ใช้ timeout 60 วินาทีสำหรับคำขอ

## Dependencies

Dependencies สำคัญที่ใช้ในโปรเจกต์นี้:
- **LangChain4j**: สำหรับการรวม AI และการจัดการเครื่องมือ
- **LangChain4j MCP**: สำหรับรองรับ Model Context Protocol
- **LangChain4j OpenAI official**: สำหรับการรวม MiniMax API ที่รองรับ OpenAI
- **Spring Boot**: สำหรับกรอบงานแอปพลิเคชันและการฉีดพึ่งพา

## ใบอนุญาต

โปรเจกต์นี้ได้รับอนุญาตภายใต้ใบอนุญาต Apache License 2.0 - ดูรายละเอียดได้ที่ไฟล์ [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->