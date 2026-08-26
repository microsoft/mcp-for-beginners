# ลูกค้าเครื่องคิดเลข LLM

แอปพลิเคชัน Java ที่สาธิตวิธีใช้ LangChain4j เพื่อเชื่อมต่อกับบริการเครื่องคิดเลข MCP (Model Context Protocol) ผ่าน API ที่เข้ากันได้กับ MiniMax OpenAI

## สิ่งที่ต้องเตรียม

- Java 21 หรือสูงกว่า
- Maven 3.6+ (หรือใช้ Maven wrapper ที่มาในแพ็กเกจ)
- คีย์ MiniMax API
- บริการเครื่องคิดเลข MCP ที่กำลังทำงานอยู่บน `http://localhost:8080`

## การรับคีย์ API

แอปพลิเคชันนี้ใช้ API ที่เข้ากันได้กับ MiniMax OpenAI ทำตามขั้นตอนเหล่านี้เพื่อรับคีย์และ endpoint ของคุณ:

### 1. เลือก endpoint
1. ใช้ `https://api.minimax.io/v1` สำหรับ endpoint ทั่วโลก
2. ใช้ `https://api.minimaxi.com/v1` สำหรับ endpoint ประเทศจีน

### 2. สร้างคีย์ API
1. สร้างคีย์ MiniMax API จากบัญชี MiniMax ของคุณ
2. เก็บคีย์ไว้ในที่ปลอดภัย

### 3. ตั้งค่าตัวแปรแวดล้อม

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

## การตั้งค่าและการติดตั้ง

1. **โคลน หรือเข้าไปยังไดเรกทอรีโปรเจกต์**

2. **ติดตั้ง dependencies**:
   ```cmd
   mvnw clean install
   ```
   หรือถ้าคุณติดตั้ง Maven ไว้ทั่วระบบ:
   ```cmd
   mvn clean install
   ```

3. **ตั้งค่าตัวแปรแวดล้อม** (ดูที่หัวข้อ "การรับคีย์ API" ข้างต้น)

4. **เริ่มต้นบริการ MCP Calculator**:
   ตรวจสอบให้แน่ใจว่าบริการ MCP calculator ในบทที่ 1 กำลังทำงานอยู่บน `http://localhost:8080/sse` ควรเปิดบริการนี้ก่อนเริ่มไคลเอนต์

## การรันแอปพลิเคชัน

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## แอปพลิเคชันทำอะไร

แอปพลิเคชันสาธิตการโต้ตอบหลักสามอย่างกับบริการเครื่องคิดเลข:

1. **การบวก**: คำนวณผลรวมของ 24.5 และ 17.3
2. **รากที่สอง**: คำนวณรากที่สองของ 144
3. **ช่วยเหลือ**: แสดงฟังก์ชันเครื่องคิดเลขที่มีให้ใช้งาน

## ผลลัพธ์ที่คาดหวัง

เมื่อรันสำเร็จ คุณควรเห็นผลลัพธ์ที่คล้ายกับ:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## การแก้ไขปัญหา

### ปัญหาทั่วไป

1. **"ตัวแปรแวดล้อม OPENAI_API_KEY ยังไม่ได้ตั้งค่า"**
   - ตรวจสอบว่าคุณได้ตั้งค่าตัวแปรแวดล้อม `OPENAI_API_KEY` แล้ว
   - รีสตาร์ทเทอร์มินัล/คอนโซลหลังจากตั้งค่าตัวแปรเสร็จ

2. **"เชื่อมต่อ localhost:8080 ถูกปฏิเสธ"**
   - ตรวจสอบว่าบริการ MCP calculator กำลังรันบนพอร์ต 8080
   - ตรวจสอบว่าไม่มีบริการอื่นใช้พอร์ต 8080 อยู่

3. **"การตรวจสอบสิทธิ์ล้มเหลว"**
   - ตรวจสอบว่าคีย์ API ของคุณถูกต้อง
   - ตรวจสอบว่า `OPENAI_BASE_URL` ตรงกับ endpoint ที่คุณตั้งใจใช้

4. **ข้อผิดพลาดในการ build Maven**
   - ตรวจสอบให้แน่ใจว่าคุณใช้ Java 21 หรือสูงกว่า: `java -version`
   - ลองล้างการ build ด้วยคำสั่ง: `mvnw clean`

### การดีบัก

เพื่อเปิดใช้งานการล็อกดีบัก ให้เพิ่มอาร์กิวเมนต์ JVM ต่อไปนี้เมื่อรัน:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## การตั้งค่า

แอปพลิเคชันตั้งค่าให้:
- ใช้ MiniMax-M3 เป็นค่าเริ่มต้น หรือ MiniMax-M2.7 เมื่อมีการตั้งค่า `MINIMAX_MODEL_ID`
- เชื่อมต่อกับ `OPENAI_BASE_URL` เมื่อถูกตั้งค่า; หากไม่กำหนด ให้ใช้ `https://api.minimaxi.com/v1` เมื่อ `MINIMAX_REGION=cn_zh` หรือ `https://api.minimax.io/v1` เป็นค่าเริ่มต้น
- เชื่อมต่อกับบริการ MCP ที่ `http://localhost:8080/sse`
- ใช้การหมดเวลา 60 วินาทีสำหรับคำขอ

## ไลบรารีที่ใช้

ไลบรารีหลักที่ใช้ในโปรเจกต์นี้:
- **LangChain4j**: สำหรับการผนวก AI และการจัดการเครื่องมือ
- **LangChain4j MCP**: สำหรับการสนับสนุน Model Context Protocol
- **LangChain4j OpenAI official**: สำหรับการผนวก MiniMax API ที่เข้ากันได้กับ OpenAI
- **Spring Boot**: สำหรับเฟรมเวิร์กแอปพลิเคชันและการฉีดพึ่งพา

## ใบอนุญาต

โปรเจกต์นี้ได้รับอนุญาตภายใต้ใบอนุญาต Apache License 2.0 - ดูรายละเอียดได้ในไฟล์ [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->