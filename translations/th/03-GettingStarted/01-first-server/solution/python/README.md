# การรันตัวอย่างนี้

แนะนำให้ติดตั้ง `uv` แต่ไม่จำเป็นต้องทำตามเสมอไป ดู [คำแนะนำ](https://docs.astral.sh/uv/#highlights)

## -0- สร้าง virtual environment

```bash
python -m venv venv
```

## -1- เปิดใช้งาน virtual environment

```bash
venv\Scripts\activate
```

## -2- ติดตั้ง dependencies

```bash
pip install "mcp[cli]"
```

## -3- รันตัวอย่าง

```bash
mcp run server.py
```

## -4- ทดสอบตัวอย่าง

เมื่อเซิร์ฟเวอร์กำลังทำงานในหนึ่ง terminal ให้เปิด terminal อีกอันและรันคำสั่งต่อไปนี้:

```bash
mcp dev server.py
```

สิ่งนี้จะเริ่มต้นเว็บเซิร์ฟเวอร์พร้อมอินเทอร์เฟซแบบภาพที่ช่วยให้คุณทดสอบตัวอย่างได้

เมื่อเซิร์ฟเวอร์เชื่อมต่อแล้ว:

- ลองแสดงรายการเครื่องมือและรัน `add` พร้อมอาร์กิวเมนต์ 2 และ 4 คุณควรเห็นผลลัพธ์เป็น 6

- ไปที่ resources และ resource template แล้วเรียกใช้ get_greeting พิมพ์ชื่อเข้าไป คุณควรเห็นข้อความต้อนรับที่มีชื่อที่คุณใส่

### การทดสอบในโหมด CLI

ตัว inspector ที่คุณรันอยู่นั้นจริง ๆ แล้วเป็นแอป Node.js และ `mcp dev` เป็น wrapper ที่ครอบมันไว้

คุณสามารถเปิดใช้งานโดยตรงในโหมด CLI ได้โดยรันคำสั่งต่อไปนี้:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

สิ่งนี้จะแสดงรายการเครื่องมือทั้งหมดที่มีอยู่ในเซิร์ฟเวอร์ คุณควรเห็นผลลัพธ์ดังนี้:

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

หากต้องการเรียกใช้เครื่องมือ ให้พิมพ์:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้