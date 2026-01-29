# การใช้งานตัวอย่างนี้

แนะนำให้ติดตั้ง `uv` แต่ไม่จำเป็นต้องติดตั้ง ดู [คำแนะนำ](https://docs.astral.sh/uv/#highlights)

## -1- ติดตั้ง dependencies

```bash
npm install
```

## -3- รันตัวอย่าง

```bash
npm run build
```

## -4- ทดสอบตัวอย่าง

เมื่อเซิร์ฟเวอร์กำลังทำงานในหนึ่ง terminal ให้เปิด terminal อีกอันและรันคำสั่งต่อไปนี้:

```bash
npm run inspector
```

คำสั่งนี้จะเริ่มต้นเว็บเซิร์ฟเวอร์พร้อมอินเทอร์เฟซแบบภาพที่ช่วยให้คุณสามารถทดสอบตัวอย่างได้

เมื่อเซิร์ฟเวอร์เชื่อมต่อแล้ว:

- ลองแสดงรายการเครื่องมือและรัน `add` โดยใช้ args 2 และ 4 คุณควรเห็นผลลัพธ์เป็น 6
- ไปที่ resources และ resource template แล้วเรียก "greeting" พิมพ์ชื่อที่คุณต้องการ คุณควรเห็นข้อความต้อนรับพร้อมชื่อที่คุณให้มา

### การทดสอบในโหมด CLI

Inspector ที่คุณรันนั้นเป็นแอป Node.js และ `mcp dev` เป็น wrapper ที่ครอบคลุมมัน

คุณสามารถเปิดใช้งานโดยตรงในโหมด CLI โดยรันคำสั่งต่อไปนี้:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

คำสั่งนี้จะแสดงรายการเครื่องมือทั้งหมดที่มีอยู่ในเซิร์ฟเวอร์ คุณควรเห็นผลลัพธ์ดังนี้:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

หากต้องการเรียกใช้งานเครื่องมือ ให้พิมพ์:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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
> โดยปกติการรัน inspector ในโหมด CLI จะเร็วกว่าในเบราว์เซอร์มาก
> อ่านเพิ่มเติมเกี่ยวกับ inspector [ที่นี่](https://github.com/modelcontextprotocol/inspector)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้