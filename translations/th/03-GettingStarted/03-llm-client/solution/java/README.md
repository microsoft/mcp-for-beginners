# Calculator LLM Client

แอปพลิเคชัน Java ที่แสดงตัวอย่างการใช้ LangChain4j เพื่อเชื่อมต่อกับบริการเครื่องคิดเลข MCP (Model Context Protocol) พร้อมการผสานรวมกับ GitHub Models

## ข้อกำหนดเบื้องต้น

- Java 21 ขึ้นไป
- Maven 3.6+ (หรือใช้ Maven wrapper ที่แนบมา)
- บัญชี GitHub ที่มีสิทธิ์เข้าถึง GitHub Models
- บริการเครื่องคิดเลข MCP ที่รันอยู่บน `http://localhost:8080`

## การขอรับ GitHub Token

แอปนี้ใช้ GitHub Models ซึ่งต้องใช้ GitHub personal access token ทำตามขั้นตอนเหล่านี้เพื่อรับ token ของคุณ:

### 1. เข้าถึง GitHub Models
1. ไปที่ [GitHub Models](https://github.com/marketplace/models)
2. ลงชื่อเข้าใช้ด้วยบัญชี GitHub ของคุณ
3. ขอสิทธิ์เข้าถึง GitHub Models หากยังไม่ได้รับ

### 2. สร้าง Personal Access Token
1. ไปที่ [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. คลิก "Generate new token" → "Generate new token (classic)"
3. ตั้งชื่อ token ให้ชัดเจน (เช่น "MCP Calculator Client")
4. กำหนดวันหมดอายุตามต้องการ
5. เลือก scope ดังนี้:
   - `repo` (ถ้าต้องการเข้าถึง repository ส่วนตัว)
   - `user:email`
6. คลิก "Generate token"
7. **สำคัญ**: คัดลอก token ทันที - คุณจะไม่สามารถดูได้อีกครั้ง!

### 3. ตั้งค่าตัวแปรสภาพแวดล้อม

#### บน Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### บน Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### บน macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## การตั้งค่าและติดตั้ง

1. **โคลนหรือไปยังไดเรกทอรีโปรเจกต์**

2. **ติดตั้ง dependencies**:
   ```cmd
   mvnw clean install
   ```
   หรือถ้าคุณติดตั้ง Maven ไว้ในระบบแล้ว:
   ```cmd
   mvn clean install
   ```

3. **ตั้งค่าตัวแปรสภาพแวดล้อม** (ดูหัวข้อ "การขอรับ GitHub Token" ข้างต้น)

4. **เริ่มบริการ MCP Calculator**:
   ตรวจสอบให้แน่ใจว่าบริการ MCP calculator จากบทที่ 1 กำลังรันอยู่ที่ `http://localhost:8080/sse` ก่อนเริ่มใช้งาน client

## การรันแอปพลิเคชัน

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## แอปพลิเคชันทำอะไร

แอปนี้แสดงตัวอย่างการโต้ตอบหลัก 3 แบบกับบริการเครื่องคิดเลข:

1. **การบวก**: คำนวณผลรวมของ 24.5 และ 17.3
2. **การหารากที่สอง**: คำนวณรากที่สองของ 144
3. **ช่วยเหลือ**: แสดงฟังก์ชันเครื่องคิดเลขที่มีให้ใช้งาน

## ผลลัพธ์ที่คาดหวัง

เมื่อรันสำเร็จ คุณจะเห็นผลลัพธ์คล้ายกับ:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## การแก้ไขปัญหา

### ปัญหาที่พบบ่อย

1. **"GITHUB_TOKEN environment variable not set"**
   - ตรวจสอบว่าคุณได้ตั้งค่าตัวแปรสภาพแวดล้อม `GITHUB_TOKEN` แล้ว
   - รีสตาร์ทเทอร์มินัลหรือ command prompt หลังตั้งค่า

2. **"Connection refused to localhost:8080"**
   - ตรวจสอบว่าบริการ MCP calculator กำลังรันบนพอร์ต 8080
   - ตรวจสอบว่าบริการอื่นไม่ได้ใช้พอร์ต 8080 อยู่

3. **"Authentication failed"**
   - ตรวจสอบว่า token GitHub ของคุณถูกต้องและมีสิทธิ์ที่เหมาะสม
   - ตรวจสอบว่าคุณมีสิทธิ์เข้าถึง GitHub Models

4. **ข้อผิดพลาดในการ build ด้วย Maven**
   - ตรวจสอบว่าใช้ Java 21 ขึ้นไป: `java -version`
   - ลองทำความสะอาด build: `mvnw clean`

### การดีบัก

เพื่อเปิดใช้งานการบันทึก debug ให้เพิ่มอาร์กิวเมนต์ JVM ต่อไปนี้เมื่อรัน:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## การตั้งค่า

แอปพลิเคชันตั้งค่าให้:
- ใช้ GitHub Models กับโมเดล `gpt-4.1-nano`
- เชื่อมต่อกับบริการ MCP ที่ `http://localhost:8080/sse`
- ตั้งเวลาหมดเวลา (timeout) สำหรับคำขอ 60 วินาที
- เปิดใช้งานการบันทึกคำขอ/คำตอบเพื่อช่วยดีบัก

## Dependencies

ไลบรารีหลักที่ใช้ในโปรเจกต์นี้:
- **LangChain4j**: สำหรับการผสาน AI และจัดการเครื่องมือ
- **LangChain4j MCP**: สำหรับรองรับ Model Context Protocol
- **LangChain4j GitHub Models**: สำหรับการผสานรวม GitHub Models
- **Spring Boot**: สำหรับเฟรมเวิร์กแอปพลิเคชันและการฉีดพึ่งพา

## ใบอนุญาต

โปรเจกต์นี้ได้รับอนุญาตภายใต้ Apache License 2.0 - ดูรายละเอียดได้ที่ไฟล์ [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้