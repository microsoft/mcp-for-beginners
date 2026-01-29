# การรันตัวอย่างนี้

แนะนำให้ติดตั้ง `uv` แต่ไม่จำเป็น ดู [คำแนะนำ](https://docs.astral.sh/uv/#highlights)

## -0- สร้างสภาพแวดล้อมเสมือน

```bash
python -m venv venv
```

## -1- เปิดใช้งานสภาพแวดล้อมเสมือน

```bash
venv\Scrips\activate
```

## -2- ติดตั้ง dependencies

```bash
pip install "mcp[cli]"
```

## -3- รันตัวอย่าง


```bash
python client.py
```

คุณควรเห็นผลลัพธ์ที่คล้ายกับ:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
                    INFO     Processing request of type ReadResourceRequest                                                                            server.py:534
CALL TOOL
                    INFO     Processing request of type CallToolRequest                                                                                server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้