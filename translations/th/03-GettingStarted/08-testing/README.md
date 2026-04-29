## การทดสอบและดีบัก

ก่อนที่คุณจะเริ่มทดสอบเซิร์ฟเวอร์ MCP ของคุณ สิ่งสำคัญคือการเข้าใจเครื่องมือที่มีอยู่และแนวทางปฏิบัติที่ดีที่สุดสำหรับการดีบัก การทดสอบที่มีประสิทธิภาพช่วยให้เซิร์ฟเวอร์ของคุณทำงานตามที่คาดหวังและช่วยให้คุณระบุและแก้ไขปัญหาได้อย่างรวดเร็ว ส่วนถัดไปนี้จะสรุปวิธีที่แนะนำสำหรับการตรวจสอบการทำงานของการติดตั้ง MCP ของคุณ

## ภาพรวม

บทเรียนนี้ครอบคลุมถึงวิธีการเลือกแนวทางการทดสอบที่เหมาะสมและเครื่องมือทดสอบที่มีประสิทธิภาพที่สุด

## วัตถุประสงค์การเรียนรู้

เมื่อคุณเรียนบทนี้จบแล้ว คุณจะสามารถ:

- อธิบายแนวทางต่าง ๆ สำหรับการทดสอบ
- ใช้เครื่องมือต่าง ๆ เพื่อทดสอบโค้ดของคุณอย่างมีประสิทธิภาพ


## การทดสอบเซิร์ฟเวอร์ MCP

MCP มีเครื่องมือที่ช่วยให้คุณทดสอบและดีบักเซิร์ฟเวอร์ของคุณได้:

- **MCP Inspector**: เครื่องมือบรรทัดคำสั่งที่สามารถใช้งานได้ทั้งในรูปแบบ CLI และแบบเครื่องมือเชิงภาพ
- **การทดสอบด้วยตนเอง**: คุณสามารถใช้เครื่องมืออย่าง curl เพื่อรันคำขอเว็บ แต่เครื่องมือใด ๆ ที่สามารถรัน HTTP ได้ก็ใช้ได้
- **การทดสอบหน่วย**: คุณสามารถใช้เฟรมเวิร์กการทดสอบที่คุณชอบเพื่อทดสอบคุณสมบัติของเซิร์ฟเวอร์และไคลเอนต์ทั้งสอง

### การใช้ MCP Inspector

เราได้อธิบายการใช้งานเครื่องมือนี้ในบทเรียนก่อนหน้าแล้ว แต่ขอพูดถึงโดยสังเขปอีกครั้ง เป็นเครื่องมือที่สร้างด้วย Node.js และคุณสามารถใช้ได้โดยเรียกใช้คำสั่ง `npx` ซึ่งจะดาวน์โหลดและติดตั้งเครื่องมือชั่วคราวและจะลบตัวเองเมื่อรันคำขอของคุณเสร็จแล้ว

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) ช่วยคุณ:

- **ค้นพบความสามารถของเซิร์ฟเวอร์**: ตรวจจับทรัพยากร เครื่องมือ และพรอมต์ที่มีอยู่โดยอัตโนมัติ
- **ทดสอบการทำงานของเครื่องมือ**: ทดลองพารามิเตอร์ต่าง ๆ และดูผลตอบกลับแบบเรียลไทม์
- **ดูข้อมูลเมตาของเซิร์ฟเวอร์**: ตรวจสอบข้อมูลเซิร์ฟเวอร์ สคีมา และการตั้งค่า

การรันเครื่องมือแบบทั่วไปดูเหมือนดังนี้:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

คำสั่งข้างต้นจะเริ่มต้น MCP และอินเทอร์เฟซแบบภาพ พร้อมเปิดอินเทอร์เฟซเว็บในเบราว์เซอร์ของคุณ คุณจะเห็นแดชบอร์ดที่แสดงเซิร์ฟเวอร์ MCP ที่ลงทะเบียน เครื่องมือ ทรัพยากร และพรอมต์ที่มีอยู่ อินเทอร์เฟซนี้ช่วยให้คุณโต้ตอบทดสอบการทำงานของเครื่องมือ ตรวจสอบข้อมูลเมตาของเซิร์ฟเวอร์ และดูการตอบสนองแบบเรียลไทม์ ทำให้ง่ายต่อการตรวจสอบและดีบักการติดตั้งเซิร์ฟเวอร์ MCP ของคุณ

นี่คือตัวอย่างหน้าตา: ![Inspector](../../../../translated_images/th/connect.141db0b2bd05f096.webp)

คุณยังสามารถรันเครื่องมือนี้ในโหมด CLI โดยเพิ่มแอตทริบิวต์ `--cli` ตัวอย่างนี้คือการรันเครื่องมือในโหมด "CLI" ซึ่งจะแสดงรายการเครื่องมือทั้งหมดบนเซิร์ฟเวอร์:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### การทดสอบด้วยตนเอง

นอกจากการรันเครื่องมือ inspector เพื่อทดสอบความสามารถของเซิร์ฟเวอร์แล้ว วิธีที่คล้ายกันคือการรันไคลเอนต์ที่สามารถใช้ HTTP เช่น curl

ด้วย curl คุณสามารถทดสอบเซิร์ฟเวอร์ MCP โดยตรงด้วยคำขอ HTTP ดังนี้:

```bash
# ตัวอย่าง: ข้อมูลเมตาของเซิร์ฟเวอร์ทดสอบ
curl http://localhost:3000/v1/metadata

# ตัวอย่าง: เรียกใช้เครื่องมือ
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

จากตัวอย่างการใช้ curl ข้างต้น คุณจะใช้คำขอ POST เพื่อเรียกใช้เครื่องมือโดยใช้ payload ที่ประกอบด้วยชื่อเครื่องมือและพารามิเตอร์ ใช้วิธีที่เหมาะกับคุณที่สุด เครื่องมือ CLI โดยทั่วไปมักจะใช้ได้เร็วกว่าและง่ายต่อการเขียนสคริปต์ซึ่งมีประโยชน์ในสภาพแวดล้อม CI/CD

### การทดสอบหน่วย

สร้างการทดสอบหน่วยสำหรับเครื่องมือและทรัพยากรของคุณเพื่อให้แน่ใจว่าทำงานตามที่คาดหวัง นี่คือตัวอย่างโค้ดการทดสอบ

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# ทำเครื่องหมายโมดูลทั้งหมดสำหรับการทดสอบแบบอะซิงค์
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # สร้างเครื่องมือทดสอบสองสามตัว
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # ทดสอบโดยไม่มีพารามิเตอร์ cursor (ละไว้)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # ทดสอบโดยใช้ cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # ทดสอบโดยใช้ cursor เป็นสตริง
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # ทดสอบโดยใช้ cursor เป็นสตริงว่าง
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

โค้ดข้างต้นทำสิ่งต่อไปนี้:

- ใช้เฟรมเวิร์ก pytest ที่ให้คุณสร้างการทดสอบเป็นฟังก์ชันและใช้คำสั่ง assert
- สร้างเซิร์ฟเวอร์ MCP ที่มีเครื่องมือสองตัวแตกต่างกัน
- ใช้คำสั่ง `assert` เพื่อตรวจสอบว่ามีเงื่อนไขบางประการได้รับการปฏิบัติ

ดูไฟล์เต็มได้ที่ [full file here](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

จากไฟล์ข้างต้น คุณสามารถทดสอบเซิร์ฟเวอร์ของคุณเองเพื่อให้แน่ใจว่าความสามารถถูกสร้างขึ้นตามที่ควร

SDK หลักทั้งหมดมีส่วนการทดสอบที่คล้ายกันเพื่อให้คุณสามารถปรับใช้กับ runtime ที่คุณเลือกได้

## ตัวอย่าง

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## แหล่งข้อมูลเพิ่มเติม

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## ต่อไปคือ

- ถัดไป: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามทำให้ถูกต้องที่สุด แต่โปรดรับทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ ขอแนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->