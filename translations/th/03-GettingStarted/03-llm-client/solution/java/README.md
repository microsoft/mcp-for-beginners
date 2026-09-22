# ลูกค้าเครื่องคิดเลข LLM

> [!NOTE]
> โซลูชันนี้เชื่อมต่อกับบริการเครื่องคิดเลข HTTP+SSE เดิมของหลักสูตรและ
> มุ่งเป้าไปที่ SDK API MCP `2025-11-25` ไม่ใช่ตัวอย่าง `2026-07-28` Streamable HTTP
> 

แอปพลิเคชัน Java ที่สาธิตวิธีใช้ LangChain4j เพื่อเชื่อมต่อกับบริการเครื่องคิดเลข MCP (Model Context Protocol) ผ่าน API ที่เข้ากันได้กับ MiniMax OpenAI

## สิ่งที่ต้องมี

- Java 21 หรือสูงกว่า
- Maven 3.6+ (หรือติดตั้ง Maven wrapper ที่ให้มา)
- คีย์ API MiniMax
- บริการเครื่องคิดเลข MCP ที่กำลังทำงานอยู่บน `http://localhost:8080`

## วิธีรับ API Key

แอปพลิเคชันนี้ใช้ MiniMax API ที่เข้ากันได้กับ OpenAI ทำตามขั้นตอนเหล่านี้เพื่อรับคีย์และจุดสิ้นสุด:

### 1. เลือกจุดสิ้นสุด
1. ใช้ `https://api.minimax.io/v1` สำหรับจุดสิ้นสุดทั่วโลก
2. ใช้ `https://api.minimaxi.com/v1` สำหรับจุดสิ้นสุดในจีน

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

1. **โคลนหรือไปที่ไดเรกทอรีโปรเจกต์**

2. **ติดตั้ง dependencies**:
   ```cmd
   mvnw clean install
   ```
   หรือหากคุณติดตั้ง Maven ไว้ทั่วระบบ:
   ```cmd
   mvn clean install
   ```

3. **ตั้งค่าตัวแปรแวดล้อม** (ดูส่วน "วิธีรับ API Key" ข้างต้น)

4. **เริ่มบริการเครื่องคิดเลข MCP**:
   ให้แน่ใจว่าบริการเครื่องคิดเลข MCP ของบทที่ 1 กำลังทำงานอยู่ที่ `http://localhost:8080/sse` ซึ่งควรจะเปิดอยู่ก่อนเริ่มต้นไคลเอนต์

## การรันแอปพลิเคชัน

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## สิ่งที่แอปพลิเคชันทำ

แอปนี้แสดงการโต้ตอบหลักสามแบบกับบริการเครื่องคิดเลข:

1. **การบวก**: คำนวณผลบวกของ 24.5 และ 17.3
2. **รากที่สอง**: คำนวณรากที่สองของ 144
3. **ช่วยเหลือ**: แสดงฟังก์ชันเครื่องคิดเลขที่มีให้ใช้

## ผลลัพธ์ที่คาดหวัง

เมื่อรันสำเร็จ คุณควรเห็นผลลัพธ์ที่คล้ายกับ:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## การแก้ไขปัญหา

### ปัญหาทั่วไป

1. **"ตัวแปรสภาพแวดล้อม OPENAI_API_KEY ยังไม่ถูกตั้งค่า"**
   - ตรวจสอบว่าคุณได้ตั้งค่าตัวแปรสภาพแวดล้อม `OPENAI_API_KEY` แล้ว
   - รีสตาร์ทเทอร์มินัลหรือ command prompt หลังตั้งค่า

2. **"ปฏิเสธการเชื่อมต่อไปยัง localhost:8080"**
   - ตรวจสอบว่ามีบริการเครื่องคิดเลข MCP รันอยู่ที่พอร์ต 8080
   - ตรวจสอบว่ามีบริการอื่นใช้งานพอร์ต 8080 หรือไม่

3. **"การรับรองตัวตนล้มเหลว"**
   - ตรวจสอบว่าคีย์ API ของคุณถูกต้อง
   - ตรวจสอบว่า `OPENAI_BASE_URL` ตรงกับจุดสิ้นสุดที่คุณต้องการใช้

4. **ข้อผิดพลาดการ build ของ Maven**
   - ตรวจสอบว่าคุณใช้ Java 21 หรือสูงกว่า: `java -version`
   - ลองทำความสะอาด build: `mvnw clean`

### การดีบัก

เพื่อเปิดใช้งานการบันทึก debug ให้เพิ่มอาร์กิวเมนต์ JVM ดังต่อไปนี้ตอนรัน:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## การตั้งค่า

แอปพลิเคชันตั้งค่าให้:
- ใช้ MiniMax-M3 เป็นค่าปริยาย; ตั้งค่า `MINIMAX_MODEL_ID` เพื่อเลือก `MiniMax-M3` หรือ `MiniMax-M2.7`
- เชื่อมต่อกับ `OPENAI_BASE_URL` เมื่อมีการตั้งค่า; มิฉะนั้นใช้ `https://api.minimaxi.com/v1` เมื่อ `MINIMAX_REGION=cn_zh`, หรือใช้ `https://api.minimax.io/v1` เป็นค่าปริยาย
- เชื่อมต่อกับบริการ MCP ที่ `http://localhost:8080/sse`
- ใช้เวลาหมดเวลา 60 วินาทีสำหรับคำขอ

## Dependencies

dependencies สำคัญที่ใช้ในโปรเจกต์นี้:
- **LangChain4j**: สำหรับการรวม AI และการจัดการเครื่องมือ
- **LangChain4j MCP**: สำหรับการสนับสนุน Model Context Protocol
- **LangChain4j OpenAI official**: สำหรับการรวม MiniMax API ที่เข้ากันได้กับ OpenAI
- **Spring Boot**: สำหรับเฟรมเวิร์กแอปและการฉีดพึ่งพา

## ใบอนุญาต

โปรเจกต์นี้ได้รับอนุญาตภายใต้ใบอนุญาต Apache License 2.0 - ดูไฟล์ [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) สำหรับรายละเอียด

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->