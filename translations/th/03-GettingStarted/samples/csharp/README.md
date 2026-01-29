# บริการเครื่องคิดเลขพื้นฐาน MCP

บริการนี้ให้การทำงานเครื่องคิดเลขพื้นฐานผ่านโปรโตคอล Model Context Protocol (MCP) ออกแบบมาเป็นตัวอย่างง่ายๆ สำหรับผู้เริ่มต้นที่กำลังเรียนรู้การใช้งาน MCP

สำหรับข้อมูลเพิ่มเติม ดูที่ [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## คุณสมบัติ

บริการเครื่องคิดเลขนี้มีความสามารถดังนี้:

1. **การคำนวณเลขคณิตพื้นฐาน**:
   - การบวกเลขสองจำนวน
   - การลบเลขจำนวนหนึ่งออกจากอีกจำนวนหนึ่ง
   - การคูณเลขสองจำนวน
   - การหารเลขจำนวนหนึ่งด้วยอีกจำนวนหนึ่ง (พร้อมตรวจสอบการหารด้วยศูนย์)

## การใช้ประเภท `stdio`
  
## การตั้งค่า

1. **ตั้งค่า MCP Servers**:
   - เปิด workspace ของคุณใน VS Code
   - สร้างไฟล์ `.vscode/mcp.json` ในโฟลเดอร์ workspace เพื่อกำหนดค่า MCP servers ตัวอย่างการตั้งค่า:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - คุณจะถูกขอให้ระบุ root ของ GitHub repository ซึ่งสามารถดึงได้จากคำสั่ง `git rev-parse --show-toplevel`

## การใช้งานบริการ

บริการนี้เปิดเผย API endpoints ผ่านโปรโตคอล MCP ดังนี้:

- `add(a, b)`: บวกเลขสองจำนวนเข้าด้วยกัน
- `subtract(a, b)`: ลบเลขตัวที่สองออกจากตัวแรก
- `multiply(a, b)`: คูณเลขสองจำนวน
- `divide(a, b)`: หารเลขตัวแรกด้วยตัวที่สอง (พร้อมตรวจสอบหารด้วยศูนย์)
- isPrime(n): ตรวจสอบว่าเลขเป็นจำนวนเฉพาะหรือไม่

## ทดสอบกับ Github Copilot Chat ใน VS Code

1. ลองส่งคำขอบริการผ่านโปรโตคอล MCP เช่น:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. เพื่อให้แน่ใจว่าใช้เครื่องมือนี้ ให้เพิ่ม #MyCalculator ใน prompt เช่น:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## เวอร์ชันแบบ Container

โซลูชันก่อนหน้านี้เหมาะสำหรับผู้ที่ติดตั้ง .NET SDK และมี dependencies ครบถ้วนแล้ว แต่ถ้าคุณต้องการแชร์โซลูชันหรือรันในสภาพแวดล้อมอื่น คุณสามารถใช้เวอร์ชันแบบ container ได้

1. เริ่มต้น Docker และตรวจสอบให้แน่ใจว่ากำลังทำงานอยู่
1. จากเทอร์มินัล ไปที่โฟลเดอร์ `03-GettingStarted\samples\csharp\src`
1. เพื่อสร้าง Docker image สำหรับบริการเครื่องคิดเลข ให้รันคำสั่งนี้ (แทนที่ `<YOUR-DOCKER-USERNAME>` ด้วยชื่อผู้ใช้ Docker Hub ของคุณ):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. หลังจากสร้าง image เสร็จแล้ว ให้ทำการอัปโหลดไปยัง Docker Hub โดยรันคำสั่งนี้:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## การใช้เวอร์ชัน Dockerized

1. ในไฟล์ `.vscode/mcp.json` ให้แทนที่การตั้งค่า server ด้วยดังนี้:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   จากการตั้งค่านี้ คุณจะเห็นว่าคำสั่งคือ `docker` และ args คือ `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc` โดย flag `--rm` จะลบ container หลังจากหยุดทำงาน และ flag `-i` ช่วยให้คุณโต้ตอบกับ standard input ของ container ได้ อาร์กิวเมนต์สุดท้ายคือชื่อ image ที่เราสร้างและอัปโหลดไปยัง Docker Hub

## ทดสอบเวอร์ชัน Dockerized

เริ่ม MCP Server โดยคลิกปุ่ม Start เล็กๆ เหนือ `"mcp-calc": {` และเหมือนเดิม คุณสามารถขอให้บริการเครื่องคิดเลขทำการคำนวณให้คุณได้เลย

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้