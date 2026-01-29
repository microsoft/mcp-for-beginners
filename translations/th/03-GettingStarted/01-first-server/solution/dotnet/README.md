# การใช้งานตัวอย่างนี้

## -1- ติดตั้ง dependencies

```bash
dotnet restore
```

## -3- รันตัวอย่าง

```bash
dotnet run
```

## -4- ทดสอบตัวอย่าง

เมื่อเซิร์ฟเวอร์กำลังทำงานในหนึ่ง terminal ให้เปิด terminal อีกอันและรันคำสั่งต่อไปนี้:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

สิ่งนี้จะเริ่มต้นเว็บเซิร์ฟเวอร์พร้อมอินเทอร์เฟซแบบภาพที่ช่วยให้คุณทดสอบตัวอย่างได้

เมื่อเซิร์ฟเวอร์เชื่อมต่อแล้ว:

- ลองแสดงรายการเครื่องมือและรัน `add` โดยใช้ args 2 และ 4 คุณควรเห็นผลลัพธ์เป็น 6
- ไปที่ resources และ resource template แล้วเรียก "greeting" พิมพ์ชื่อเข้าไป คุณควรเห็นข้อความต้อนรับพร้อมชื่อที่คุณให้มา

### การทดสอบในโหมด CLI

คุณสามารถเปิดใช้งานโดยตรงในโหมด CLI โดยรันคำสั่งต่อไปนี้:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

สิ่งนี้จะแสดงรายการเครื่องมือทั้งหมดที่มีในเซิร์ฟเวอร์ คุณควรเห็นผลลัพธ์ดังนี้:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

เพื่อเรียกใช้งานเครื่องมือ ให้พิมพ์:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

คุณควรเห็นผลลัพธ์ดังนี้:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
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