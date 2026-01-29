# Calculator HTTP Streaming Demo

โปรเจกต์นี้สาธิตการสตรีม HTTP โดยใช้ Server-Sent Events (SSE) กับ Spring Boot WebFlux ประกอบด้วยแอปพลิเคชันสองตัว:

- **Calculator Server**: เว็บเซอร์วิสแบบ reactive ที่ทำการคำนวณและสตรีมผลลัพธ์ผ่าน SSE
- **Calculator Client**: แอปพลิเคชันไคลเอนต์ที่รับข้อมูลจาก endpoint แบบสตรีม

## สิ่งที่ต้องเตรียม

- Java 17 ขึ้นไป
- Maven 3.6 ขึ้นไป

## โครงสร้างโปรเจกต์

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## วิธีการทำงาน

1. **Calculator Server** เปิดเผย endpoint `/calculate` ที่:
   - รับพารามิเตอร์ query: `a` (ตัวเลข), `b` (ตัวเลข), `op` (การดำเนินการ)
   - รองรับการดำเนินการ: `add`, `sub`, `mul`, `div`
   - ส่ง Server-Sent Events ที่แสดงความคืบหน้าและผลลัพธ์ของการคำนวณ

2. **Calculator Client** เชื่อมต่อกับเซิร์ฟเวอร์และ:
   - ส่งคำขอเพื่อคำนวณ `7 * 5`
   - รับข้อมูลสตรีมมิ่งตอบกลับ
   - แสดงผลแต่ละอีเวนต์บนคอนโซล

## การรันแอปพลิเคชัน

### ตัวเลือกที่ 1: ใช้ Maven (แนะนำ)

#### 1. เริ่มต้น Calculator Server

เปิดเทอร์มินัลและไปที่ไดเรกทอรีของเซิร์ฟเวอร์:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

เซิร์ฟเวอร์จะเริ่มทำงานที่ `http://localhost:8080`

คุณจะเห็นผลลัพธ์ประมาณนี้:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. รัน Calculator Client

เปิด **เทอร์มินัลใหม่** และไปที่ไดเรกทอรีของไคลเอนต์:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

ไคลเอนต์จะเชื่อมต่อกับเซิร์ฟเวอร์ ทำการคำนวณ และแสดงผลลัพธ์แบบสตรีมมิ่ง

### ตัวเลือกที่ 2: ใช้ Java โดยตรง

#### 1. คอมไพล์และรันเซิร์ฟเวอร์:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. คอมไพล์และรันไคลเอนต์:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## การทดสอบเซิร์ฟเวอร์ด้วยตนเอง

คุณสามารถทดสอบเซิร์ฟเวอร์โดยใช้เว็บเบราว์เซอร์หรือ curl:

### ใช้เว็บเบราว์เซอร์:
เข้าไปที่: `http://localhost:8080/calculate?a=10&b=5&op=add`

### ใช้ curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## ผลลัพธ์ที่คาดหวัง

เมื่อรันไคลเอนต์ คุณจะเห็นผลลัพธ์แบบสตรีมมิ่งคล้ายกับ:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## การดำเนินการที่รองรับ

- `add` - การบวก (a + b)
- `sub` - การลบ (a - b)
- `mul` - การคูณ (a * b)
- `div` - การหาร (a / b, คืนค่า NaN หาก b = 0)

## เอกสารอ้างอิง API

### GET /calculate

**พารามิเตอร์:**
- `a` (จำเป็น): ตัวเลขตัวแรก (double)
- `b` (จำเป็น): ตัวเลขตัวที่สอง (double)
- `op` (จำเป็น): การดำเนินการ (`add`, `sub`, `mul`, `div`)

**การตอบกลับ:**
- Content-Type: `text/event-stream`
- ส่ง Server-Sent Events ที่แสดงความคืบหน้าและผลลัพธ์ของการคำนวณ

**ตัวอย่างคำขอ:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**ตัวอย่างการตอบกลับ:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## การแก้ไขปัญหา

### ปัญหาที่พบบ่อย

1. **พอร์ต 8080 ถูกใช้งานแล้ว**
   - หยุดแอปพลิเคชันอื่นที่ใช้พอร์ต 8080
   - หรือเปลี่ยนพอร์ตเซิร์ฟเวอร์ในไฟล์ `calculator-server/src/main/resources/application.yml`

2. **เชื่อมต่อถูกปฏิเสธ**
   - ตรวจสอบให้แน่ใจว่าเซิร์ฟเวอร์กำลังทำงานก่อนเริ่มไคลเอนต์
   - ตรวจสอบว่าเซิร์ฟเวอร์เริ่มทำงานสำเร็จที่พอร์ต 8080

3. **ปัญหาชื่อพารามิเตอร์**
   - โปรเจกต์นี้ตั้งค่า Maven compiler ด้วย flag `-parameters`
   - หากเจอปัญหาการผูกพารามิเตอร์ ให้แน่ใจว่าโปรเจกต์ถูกสร้างด้วยการตั้งค่านี้

### การหยุดแอปพลิเคชัน

- กด `Ctrl+C` ในเทอร์มินัลที่รันแต่ละแอปพลิเคชัน
- หรือใช้คำสั่ง `mvn spring-boot:stop` หากรันเป็น background process

## เทคโนโลยีที่ใช้

- **Spring Boot 3.3.1** - เฟรมเวิร์กสำหรับแอปพลิเคชัน
- **Spring WebFlux** - เฟรมเวิร์กเว็บแบบ reactive
- **Project Reactor** - ไลบรารี reactive streams
- **Netty** - เซิร์ฟเวอร์แบบ non-blocking I/O
- **Maven** - เครื่องมือสร้างโปรเจกต์
- **Java 17+** - ภาษาโปรแกรม

## ขั้นตอนถัดไป

ลองแก้ไขโค้ดเพื่อ:
- เพิ่มการดำเนินการทางคณิตศาสตร์เพิ่มเติม
- เพิ่มการจัดการข้อผิดพลาดสำหรับการดำเนินการที่ไม่ถูกต้อง
- เพิ่มการบันทึกคำขอ/การตอบกลับ
- เพิ่มระบบยืนยันตัวตน
- เพิ่ม unit tests

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้