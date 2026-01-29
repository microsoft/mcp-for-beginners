# การใช้งานตัวอย่างนี้

## -1- ติดตั้ง dependencies

```bash
dotnet restore
```

## -2- รันตัวอย่าง

```bash
dotnet run
```

## -3- ทดสอบตัวอย่าง

เปิด terminal แยกต่างหากก่อนที่จะรันคำสั่งด้านล่าง (ตรวจสอบให้แน่ใจว่าเซิร์ฟเวอร์ยังคงทำงานอยู่)

เมื่อเซิร์ฟเวอร์ทำงานใน terminal หนึ่ง ให้เปิด terminal อีกอันและรันคำสั่งต่อไปนี้:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

คำสั่งนี้จะเริ่มต้นเว็บเซิร์ฟเวอร์พร้อมอินเทอร์เฟซแบบภาพที่ช่วยให้คุณสามารถทดสอบตัวอย่างได้

> ตรวจสอบให้แน่ใจว่าได้เลือก **Streamable HTTP** เป็นประเภทการส่งข้อมูล และ URL คือ `http://localhost:3001/mcp`

เมื่อเซิร์ฟเวอร์เชื่อมต่อแล้ว:

- ลองแสดงรายการเครื่องมือและรัน `add` โดยใช้ args 2 และ 4 คุณควรเห็นผลลัพธ์เป็น 6
- ไปที่ resources และ resource template แล้วเรียก "greeting" พิมพ์ชื่อเข้าไป คุณควรเห็นข้อความต้อนรับพร้อมชื่อที่คุณให้มา

### การทดสอบในโหมด CLI

คุณสามารถเปิดใช้งานโดยตรงในโหมด CLI โดยรันคำสั่งต่อไปนี้:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

คำสั่งนี้จะแสดงรายการเครื่องมือทั้งหมดที่มีอยู่ในเซิร์ฟเวอร์ คุณควรเห็นผลลัพธ์ดังนี้:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

หากต้องการเรียกใช้งานเครื่องมือ ให้พิมพ์:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

คุณควรเห็นผลลัพธ์ดังนี้:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> โดยปกติแล้วการรัน inspector ในโหมด CLI จะเร็วกว่าในเบราว์เซอร์มาก
> อ่านเพิ่มเติมเกี่ยวกับ inspector [ที่นี่](https://github.com/modelcontextprotocol/inspector)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้