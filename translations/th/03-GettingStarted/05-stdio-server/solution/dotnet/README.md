# MCP stdio Server - .NET Solution

> **⚠️ สำคัญ**: โซลูชันนี้ได้รับการอัปเดตให้ใช้ **stdio transport** ตามคำแนะนำใน MCP Specification 2025-06-18 โดย transport แบบ SSE เดิมถูกยกเลิกแล้ว

## ภาพรวม

โซลูชัน .NET นี้แสดงวิธีการสร้าง MCP server โดยใช้ stdio transport ในปัจจุบัน ซึ่ง stdio transport มีความเรียบง่าย ปลอดภัยมากขึ้น และให้ประสิทธิภาพที่ดีกว่าเมื่อเทียบกับวิธี SSE ที่ถูกยกเลิก

## สิ่งที่ต้องเตรียม

- .NET 9.0 SDK หรือใหม่กว่า
- ความเข้าใจพื้นฐานเกี่ยวกับ .NET dependency injection

## คำแนะนำการตั้งค่า

### ขั้นตอนที่ 1: คืนค่า dependencies

```bash
dotnet restore
```

### ขั้นตอนที่ 2: สร้างโปรเจกต์

```bash
dotnet build
```

## การรันเซิร์ฟเวอร์

เซิร์ฟเวอร์ stdio ทำงานแตกต่างจากเซิร์ฟเวอร์ HTTP แบบเดิม โดยจะสื่อสารผ่าน stdin/stdout แทนการเริ่มต้นเว็บเซิร์ฟเวอร์:

```bash
dotnet run
```

**สำคัญ**: เซิร์ฟเวอร์อาจดูเหมือนค้าง - นี่เป็นเรื่องปกติ! เซิร์ฟเวอร์กำลังรอข้อความ JSON-RPC จาก stdin

## การทดสอบเซิร์ฟเวอร์

### วิธีที่ 1: ใช้ MCP Inspector (แนะนำ)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

สิ่งนี้จะ:
1. เปิดเซิร์ฟเวอร์ของคุณเป็น subprocess
2. เปิดอินเทอร์เฟซเว็บสำหรับการทดสอบ
3. ให้คุณทดสอบเครื่องมือเซิร์ฟเวอร์ทั้งหมดแบบโต้ตอบ

### วิธีที่ 2: การทดสอบผ่าน command line โดยตรง

คุณสามารถทดสอบได้โดยการเปิด Inspector โดยตรง:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### เครื่องมือที่มีให้ใช้งาน

เซิร์ฟเวอร์มีเครื่องมือดังนี้:

- **AddNumbers(a, b)**: บวกตัวเลขสองตัว
- **MultiplyNumbers(a, b)**: คูณตัวเลขสองตัว  
- **GetGreeting(name)**: สร้างข้อความทักทายแบบส่วนตัว
- **GetServerInfo()**: รับข้อมูลเกี่ยวกับเซิร์ฟเวอร์

### การทดสอบกับ Claude Desktop

เพื่อใช้เซิร์ฟเวอร์นี้กับ Claude Desktop ให้เพิ่มการตั้งค่านี้ใน `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## โครงสร้างโปรเจกต์

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## ความแตกต่างสำคัญระหว่าง HTTP/SSE

**stdio transport (ปัจจุบัน):**
- ✅ ตั้งค่าง่ายกว่า - ไม่ต้องใช้เว็บเซิร์ฟเวอร์
- ✅ ปลอดภัยกว่า - ไม่มี HTTP endpoints
- ✅ ใช้ `Host.CreateApplicationBuilder()` แทน `WebApplication.CreateBuilder()`
- ✅ ใช้ `WithStdioTransport()` แทน `WithHttpTransport()`
- ✅ เป็น console application แทน web application
- ✅ ประสิทธิภาพดีกว่า

**HTTP/SSE transport (ถูกยกเลิก):**
- ❌ ต้องใช้ ASP.NET Core web server
- ❌ ต้องตั้งค่า routing ด้วย `app.MapMcp()`
- ❌ การตั้งค่าและ dependencies ซับซ้อนกว่า
- ❌ มีข้อพิจารณาด้านความปลอดภัยเพิ่มเติม
- ❌ ถูกยกเลิกใน MCP 2025-06-18

## ฟีเจอร์สำหรับการพัฒนา

- **Dependency Injection**: รองรับ DI เต็มรูปแบบสำหรับ services และ logging
- **Structured Logging**: การบันทึก log ที่เหมาะสมไปยัง stderr โดยใช้ `ILogger<T>`
- **Tool Attributes**: การกำหนดเครื่องมือที่สะอาดด้วย `[McpServerTool]` attributes
- **Async Support**: เครื่องมือทั้งหมดรองรับการทำงานแบบ async
- **Error Handling**: การจัดการข้อผิดพลาดและการบันทึก log อย่างมีประสิทธิภาพ

## เคล็ดลับสำหรับการพัฒนา

- ใช้ `ILogger` สำหรับ logging (อย่าเขียนไปยัง stdout โดยตรง)
- สร้างโปรเจกต์ด้วย `dotnet build` ก่อนการทดสอบ
- ทดสอบด้วย Inspector เพื่อการ debug แบบภาพ
- การบันทึก log ทั้งหมดจะไปยัง stderr โดยอัตโนมัติ
- เซิร์ฟเวอร์รองรับสัญญาณ shutdown อย่างมีประสิทธิภาพ

โซลูชันนี้เป็นไปตาม MCP specification ปัจจุบัน และแสดงแนวทางปฏิบัติที่ดีที่สุดสำหรับการใช้งาน stdio transport ด้วย .NET

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้