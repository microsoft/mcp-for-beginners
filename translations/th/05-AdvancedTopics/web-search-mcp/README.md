# บทเรียน: การสร้าง Web Search MCP Server

บทนี้จะแสดงวิธีการสร้าง AI agent ที่ใช้งานได้จริง ซึ่งผสานรวมกับ API ภายนอก จัดการกับข้อมูลหลากหลายประเภท จัดการข้อผิดพลาด และประสานงานเครื่องมือต่างๆ หลายตัว — ทั้งหมดในรูปแบบที่พร้อมใช้งานในงานจริง คุณจะได้เห็น:

- **การผสานรวมกับ API ภายนอกที่ต้องมีการยืนยันตัวตน**
- **การจัดการข้อมูลหลากหลายประเภทจากหลายจุดเชื่อมต่อ**
- **กลยุทธ์การจัดการข้อผิดพลาดและการบันทึกที่แข็งแกร่ง**
- **การประสานงานเครื่องมือหลายตัวในเซิร์ฟเวอร์เดียว**

เมื่อจบบทนี้ คุณจะมีประสบการณ์จริงกับรูปแบบและแนวทางปฏิบัติที่จำเป็นสำหรับแอปพลิเคชัน AI และ LLM ขั้นสูง

## บทนำ

ในบทเรียนนี้ คุณจะได้เรียนรู้วิธีสร้าง MCP server และ client ขั้นสูงที่ขยายความสามารถของ LLM ด้วยข้อมูลเว็บแบบเรียลไทม์โดยใช้ SerpAPI ทักษะนี้สำคัญมากสำหรับการพัฒนา AI agent ที่สามารถเข้าถึงข้อมูลล่าสุดจากเว็บได้

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- ผสานรวม API ภายนอก (เช่น SerpAPI) เข้ากับ MCP server อย่างปลอดภัย
- ใช้เครื่องมือหลายตัวสำหรับการค้นหาเว็บ ข่าว สินค้า และถาม-ตอบ
- แยกวิเคราะห์และจัดรูปแบบข้อมูลเชิงโครงสร้างเพื่อใช้กับ LLM
- จัดการข้อผิดพลาดและควบคุมอัตราการเรียก API อย่างมีประสิทธิภาพ
- สร้างและทดสอบ MCP client ทั้งแบบอัตโนมัติและแบบโต้ตอบ

## Web Search MCP Server

ส่วนนี้แนะนำสถาปัตยกรรมและฟีเจอร์ของ Web Search MCP Server คุณจะเห็นว่า FastMCP และ SerpAPI ถูกใช้ร่วมกันอย่างไรเพื่อขยายความสามารถของ LLM ด้วยข้อมูลเว็บแบบเรียลไทม์

### ภาพรวม

การใช้งานนี้มีเครื่องมือสี่ตัวที่แสดงให้เห็นถึงความสามารถของ MCP ในการจัดการงานที่ขับเคลื่อนด้วย API ภายนอกหลากหลายอย่างปลอดภัยและมีประสิทธิภาพ:

- **general_search**: สำหรับผลลัพธ์เว็บทั่วไป
- **news_search**: สำหรับข่าวสารล่าสุด
- **product_search**: สำหรับข้อมูลอีคอมเมิร์ซ
- **qna**: สำหรับคำตอบคำถามสั้นๆ

### ฟีเจอร์
- **ตัวอย่างโค้ด**: มีบล็อกโค้ดเฉพาะภาษา เช่น Python (และขยายได้ง่ายไปยังภาษาอื่น) โดยใช้ code pivots เพื่อความชัดเจน

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

ก่อนรัน client ควรเข้าใจว่าเซิร์ฟเวอร์ทำอะไรบ้าง ไฟล์ [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) เป็นการใช้งาน MCP server ที่เปิดเผยเครื่องมือสำหรับค้นหาเว็บ ข่าว สินค้า และถาม-ตอบ โดยผสานรวมกับ SerpAPI เซิร์ฟเวอร์จะจัดการคำขอที่เข้ามา เรียก API แยกวิเคราะห์ผลลัพธ์ และส่งผลลัพธ์ที่จัดรูปแบบแล้วกลับไปยัง client

คุณสามารถดูการใช้งานเต็มได้ใน [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py)

นี่คือตัวอย่างสั้นๆ ของการกำหนดและลงทะเบียนเครื่องมือในเซิร์ฟเวอร์:

### Python Server

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **การผสานรวม API ภายนอก**: แสดงการจัดการคีย์ API และคำขอภายนอกอย่างปลอดภัย
- **การแยกวิเคราะห์ข้อมูลเชิงโครงสร้าง**: แสดงวิธีแปลงผลลัพธ์ API ให้เหมาะกับ LLM
- **การจัดการข้อผิดพลาด**: มีการจัดการข้อผิดพลาดอย่างแข็งแกร่งพร้อมบันทึกที่เหมาะสม
- **Client โต้ตอบได้**: รวมทั้งการทดสอบอัตโนมัติและโหมดโต้ตอบสำหรับการทดสอบ
- **การจัดการบริบท**: ใช้ MCP Context สำหรับบันทึกและติดตามคำขอ

## ข้อกำหนดเบื้องต้น

ก่อนเริ่มต้น ให้แน่ใจว่าสภาพแวดล้อมของคุณถูกตั้งค่าอย่างถูกต้องตามขั้นตอนเหล่านี้ เพื่อให้แน่ใจว่าติดตั้ง dependencies ครบถ้วนและตั้งค่าคีย์ API อย่างถูกต้องสำหรับการพัฒนาและทดสอบที่ราบรื่น

- Python 3.8 ขึ้นไป
- SerpAPI API Key (สมัครได้ที่ [SerpAPI](https://serpapi.com/) - มีแผนฟรี)

## การติดตั้ง

เริ่มต้นด้วยการตั้งค่าสภาพแวดล้อมตามขั้นตอนนี้:

1. ติดตั้ง dependencies โดยใช้ uv (แนะนำ) หรือ pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. สร้างไฟล์ `.env` ที่โฟลเดอร์โปรเจกต์หลัก พร้อมใส่คีย์ SerpAPI ของคุณ:

```
SERPAPI_KEY=your_serpapi_key_here
```

## การใช้งาน

Web Search MCP Server เป็นส่วนหลักที่เปิดเผยเครื่องมือสำหรับค้นหาเว็บ ข่าว สินค้า และถาม-ตอบ โดยผสานรวมกับ SerpAPI เซิร์ฟเวอร์จะจัดการคำขอที่เข้ามา เรียก API แยกวิเคราะห์ผลลัพธ์ และส่งผลลัพธ์ที่จัดรูปแบบแล้วกลับไปยัง client

คุณสามารถดูการใช้งานเต็มได้ใน [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py)

### การรันเซิร์ฟเวอร์

เพื่อเริ่ม MCP server ให้ใช้คำสั่งนี้:

```bash
python server.py
```

เซิร์ฟเวอร์จะทำงานในรูปแบบ stdio-based MCP server ที่ client สามารถเชื่อมต่อได้โดยตรง

### โหมดของ Client

client (`client.py`) รองรับสองโหมดสำหรับการโต้ตอบกับ MCP server:

- **โหมดปกติ**: รันการทดสอบอัตโนมัติที่เรียกใช้เครื่องมือทั้งหมดและตรวจสอบผลลัพธ์ เหมาะสำหรับตรวจสอบว่าเซิร์ฟเวอร์และเครื่องมือทำงานถูกต้อง
- **โหมดโต้ตอบ**: เริ่มอินเทอร์เฟซเมนูที่ให้คุณเลือกและเรียกใช้เครื่องมือเอง ป้อนคำค้นหา และดูผลลัพธ์แบบเรียลไทม์ เหมาะสำหรับสำรวจความสามารถของเซิร์ฟเวอร์และทดลองกับอินพุตต่างๆ

คุณสามารถดูการใช้งานเต็มได้ใน [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py)

### การรัน Client

รันการทดสอบอัตโนมัติ (ซึ่งจะเริ่มเซิร์ฟเวอร์ให้อัตโนมัติ):

```bash
python client.py
```

หรือรันในโหมดโต้ตอบ:

```bash
python client.py --interactive
```

### การทดสอบด้วยวิธีต่างๆ

มีหลายวิธีในการทดสอบและโต้ตอบกับเครื่องมือที่เซิร์ฟเวอร์ให้มา ขึ้นอยู่กับความต้องการและวิธีการทำงานของคุณ

#### การเขียนสคริปต์ทดสอบเองด้วย MCP Python SDK
คุณยังสามารถสร้างสคริปต์ทดสอบของตัวเองโดยใช้ MCP Python SDK:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

ในบริบทนี้ "สคริปต์ทดสอบ" หมายถึงโปรแกรม Python ที่คุณเขียนเองเพื่อทำหน้าที่เป็น client สำหรับ MCP server แทนที่จะเป็น unit test อย่างเป็นทางการ สคริปต์นี้ช่วยให้คุณเชื่อมต่อกับเซิร์ฟเวอร์ เรียกใช้เครื่องมือใดก็ได้พร้อมพารามิเตอร์ที่เลือก และตรวจสอบผลลัพธ์ วิธีนี้เหมาะสำหรับ:
- การสร้างต้นแบบและทดลองเรียกใช้เครื่องมือ
- ตรวจสอบการตอบสนองของเซิร์ฟเวอร์ต่ออินพุตต่างๆ
- อัตโนมัติการเรียกใช้เครื่องมือซ้ำๆ
- สร้างเวิร์กโฟลว์หรือการผสานรวมของคุณเองบน MCP server

คุณสามารถใช้สคริปต์ทดสอบเพื่อทดลองคำค้นหาใหม่ๆ แก้ไขบั๊กของเครื่องมือ หรือใช้เป็นจุดเริ่มต้นสำหรับการอัตโนมัติขั้นสูง ด้านล่างคือตัวอย่างการใช้ MCP Python SDK เพื่อสร้างสคริปต์แบบนี้:

## คำอธิบายเครื่องมือ

คุณสามารถใช้เครื่องมือต่อไปนี้ที่เซิร์ฟเวอร์ให้มาเพื่อทำการค้นหาและสอบถามประเภทต่างๆ เครื่องมือแต่ละตัวอธิบายไว้พร้อมพารามิเตอร์และตัวอย่างการใช้งาน

ส่วนนี้ให้รายละเอียดเกี่ยวกับเครื่องมือแต่ละตัวและพารามิเตอร์ของมัน

### general_search

ทำการค้นหาเว็บทั่วไปและส่งผลลัพธ์ที่จัดรูปแบบแล้วกลับมา

**วิธีเรียกใช้เครื่องมือนี้:**

คุณสามารถเรียก `general_search` จากสคริปต์ของคุณเองโดยใช้ MCP Python SDK หรือโต้ตอบผ่าน Inspector หรือโหมด client แบบโต้ตอบ นี่คือตัวอย่างโค้ดโดยใช้ SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

หรือในโหมดโต้ตอบ เลือก `general_search` จากเมนูและป้อนคำค้นหาตามที่ระบบถาม

**พารามิเตอร์:**
- `query` (string): คำค้นหา

**ตัวอย่างคำขอ:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

ค้นหาบทความข่าวล่าสุดที่เกี่ยวข้องกับคำค้นหา

**วิธีเรียกใช้เครื่องมือนี้:**

คุณสามารถเรียก `news_search` จากสคริปต์ของคุณเองโดยใช้ MCP Python SDK หรือโต้ตอบผ่าน Inspector หรือโหมด client แบบโต้ตอบ นี่คือตัวอย่างโค้ดโดยใช้ SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

หรือในโหมดโต้ตอบ เลือก `news_search` จากเมนูและป้อนคำค้นหาตามที่ระบบถาม

**พารามิเตอร์:**
- `query` (string): คำค้นหา

**ตัวอย่างคำขอ:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

ค้นหาสินค้าที่ตรงกับคำค้นหา

**วิธีเรียกใช้เครื่องมือนี้:**

คุณสามารถเรียก `product_search` จากสคริปต์ของคุณเองโดยใช้ MCP Python SDK หรือโต้ตอบผ่าน Inspector หรือโหมด client แบบโต้ตอบ นี่คือตัวอย่างโค้ดโดยใช้ SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

หรือในโหมดโต้ตอบ เลือก `product_search` จากเมนูและป้อนคำค้นหาตามที่ระบบถาม

**พารามิเตอร์:**
- `query` (string): คำค้นหาสินค้า

**ตัวอย่างคำขอ:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

รับคำตอบโดยตรงสำหรับคำถามจากเครื่องมือค้นหา

**วิธีเรียกใช้เครื่องมือนี้:**

คุณสามารถเรียก `qna` จากสคริปต์ของคุณเองโดยใช้ MCP Python SDK หรือโต้ตอบผ่าน Inspector หรือโหมด client แบบโต้ตอบ นี่คือตัวอย่างโค้ดโดยใช้ SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

หรือในโหมดโต้ตอบ เลือก `qna` จากเมนูและป้อนคำถามตามที่ระบบถาม

**พารามิเตอร์:**
- `question` (string): คำถามที่ต้องการคำตอบ

**ตัวอย่างคำขอ:**

```json
{
  "question": "what is artificial intelligence"
}
```

## รายละเอียดโค้ด

ส่วนนี้ให้ตัวอย่างโค้ดและข้อมูลอ้างอิงสำหรับการใช้งานเซิร์ฟเวอร์และไคลเอนต์

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

ดูรายละเอียดการใช้งานเต็มใน [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) และ [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py)

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## แนวคิดขั้นสูงในบทนี้

ก่อนเริ่มสร้าง นี่คือแนวคิดขั้นสูงที่สำคัญซึ่งจะปรากฏตลอดบทนี้ การเข้าใจแนวคิดเหล่านี้จะช่วยให้คุณตามเนื้อหาได้แม้จะยังไม่คุ้นเคย:

- **การประสานงานเครื่องมือหลายตัว**: หมายถึงการรันเครื่องมือต่างๆ หลายตัว (เช่น ค้นหาเว็บ ข่าว สินค้า และถาม-ตอบ) ใน MCP server เดียว ช่วยให้เซิร์ฟเวอร์ของคุณจัดการงานหลากหลาย ไม่ใช่แค่หนึ่งอย่าง
- **การจัดการอัตราการเรียก API**: API ภายนอกหลายตัว (เช่น SerpAPI) จำกัดจำนวนคำขอที่คุณสามารถส่งในช่วงเวลาหนึ่ง โค้ดที่ดีจะตรวจสอบขีดจำกัดนี้และจัดการอย่างเหมาะสม เพื่อไม่ให้แอปของคุณล่มเมื่อถึงขีดจำกัด
- **การแยกวิเคราะห์ข้อมูลเชิงโครงสร้าง**: ผลลัพธ์ API มักซับซ้อนและมีโครงสร้างซ้อนกัน แนวคิดนี้คือการแปลงผลลัพธ์เหล่านั้นให้อยู่ในรูปแบบที่สะอาดและใช้งานง่าย เหมาะสำหรับ LLM หรือโปรแกรมอื่นๆ
- **การกู้คืนจากข้อผิดพลาด**: บางครั้งเกิดปัญหา เช่น เครือข่ายล่ม หรือ API ไม่ส่งข้อมูลตามที่คาดไว้ การกู้คืนจากข้อผิดพลาดหมายถึงโค้ดของคุณสามารถจัดการกับปัญหาเหล่านี้และยังให้ข้อมูลที่เป็นประโยชน์ แทนที่จะล่ม
- **การตรวจสอบพารามิเตอร์**: คือการตรวจสอบว่าอินพุตทั้งหมดที่ส่งเข้าเครื่องมือถูกต้องและปลอดภัย รวมถึงการตั้งค่าค่าดีฟอลต์และตรวจสอบชนิดข้อมูล ซึ่งช่วยป้องกันบั๊กและความสับสน

ส่วนนี้จะช่วยคุณวินิจฉัยและแก้ไขปัญหาทั่วไปที่อาจเจอขณะทำงานกับ Web Search MCP Server หากเจอข้อผิดพลาดหรือพฤติกรรมที่ไม่คาดคิดในขณะใช้งาน MCP Server นี้ ส่วนแก้ไขปัญหานี้มีคำแนะนำสำหรับปัญหาที่พบบ่อยที่สุด ควรอ่านก่อนขอความช่วยเหลือเพิ่มเติม เพราะมักแก้ปัญหาได้รวดเร็ว

## การแก้ไขปัญหา

เมื่อทำงานกับ Web Search MCP Server คุณอาจเจอปัญหาบ้างเป็นเรื่องปกติเมื่อพัฒนาโดยใช้ API ภายนอกและเครื่องมือใหม่ๆ ส่วนนี้ให้คำแนะนำแก้ไขปัญหาที่พบบ่อย เพื่อให้คุณกลับมาทำงานได้เร็ว หากเจอข้อผิดพลาด เริ่มจากที่นี่: คำแนะนำด้านล่างครอบคลุมปัญหาที่ผู้ใช้ส่วนใหญ่เจอและมักแก้ไขได้โดยไม่ต้องขอความช่วยเหลือเพิ่มเติม

### ปัญหาที่พบบ่อย

ด้านล่างคือปัญหาที่พบบ่อยพร้อมคำอธิบายและวิธีแก้ไข:

1. **ไม่มี SERPAPI_KEY ในไฟล์ .env**
   - หากเห็นข้อผิดพลาด `SERPAPI_KEY environment variable not found` หมายความว่าแอปของคุณหา API key สำหรับเข้าถึง SerpAPI ไม่เจอ ให้สร้างไฟล์ชื่อ `.env` ที่โฟลเดอร์โปรเจกต์หลัก (ถ้ายังไม่มี) และเพิ่มบรรทัด `SERPAPI_KEY=your_serpapi_key_here` โดยเปลี่ยน `your_serpapi_key_here` เป็นคีย์จริงจากเว็บไซต์ SerpAPI

2. **ข้อผิดพลาดโมดูลไม่พบ**
   - ข้อผิดพลาดเช่น `ModuleNotFoundError: No module named 'httpx'` หมายความว่ามีแพ็กเกจ Python ที่จำเป็นยังไม่ได้ติดตั้ง ปกติเกิดจากยังไม่ได้ติดตั้ง dependencies ให้แก้ไขโดยรันคำสั่ง `pip install -r requirements.txt` ในเทอร์มินัลเพื่อดาวน์โหลดและติดตั้งทุกอย่างที่โปรเจกต์ต้องการ

3. **ปัญหาการเชื่อมต่อ**
   - หากเจอข้อผิดพลาดเช่น `Error during client execution` มักหมายความว่า client เชื่อมต่อกับเซิร์ฟเวอร์ไม่ได้ หรือเซิร์ฟเวอร์ไม่ได้รันตามที่คาด ตรวจสอบให้แน่ใจว่า client และ server เป็นเวอร์ชันที่เข้ากันได้ และไฟล์ `server.py` อยู่ในโฟลเดอร์ถูกต้องและกำลังรันอยู่ การรีสตาร์ททั้งเซิร์ฟเวอร์และ client ก็ช่วยได้เช่นกัน

4. **ข้อผิดพลาด SerpAPI**
   - หากเห็นข้อความ `Search API returned error status: 401` หมายความว่าคีย์ SerpAPI ของคุณหายไป ไม่ถูกต้อง หรือหมดอายุ ให้ไปที่แดชบอร์ด SerpAPI ตรวจสอบคีย์และอัปเดตไฟล์ `.env` หากจำเป็น หากคีย์ถูกต้องแต่ยังเจอปัญหา ให้ตรวจสอบว่าแผนบริการฟรีของคุณยังมีโควต้าเหลือหรือไม่

### โหมดดีบัก

โดยปกติแอปจะบันทึกเฉพาะข้อมูลสำคัญ หากต้องการดูรายละเอียดมากขึ้น (เช่น เพื่อวินิจฉัยปัญหายากๆ) คุณสามารถเปิดโหมด DEBUG ได้ ซึ่งจะแสดงข้อมูลขั้นตอนต่างๆ ของแอปมากขึ้น

**ตัวอย่าง: ผลลัพธ์ปกติ**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**ตัวอย่าง: ผลลัพธ์โหมด DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

สังเกตว่าโหมด DEBUG จะแสดงบรรทัดเพิ่มเติมเกี่ยวกับคำขอ HTTP การตอบกลับ และรายละเอียดภายในอื่นๆ ซึ่งช่วยได้มากในการแก้ไขปัญหา
เพื่อเปิดใช้งานโหมด DEBUG ให้ตั้งค่าระดับการบันทึกเป็น DEBUG ที่ด้านบนของไฟล์ `client.py` หรือ `server.py` ของคุณ:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## ต่อไปคืออะไร

- [5.10 การสตรีมแบบเรียลไทม์](../mcp-realtimestreaming/README.md)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้