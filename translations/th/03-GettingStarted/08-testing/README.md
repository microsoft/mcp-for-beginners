## การทดสอบและการดีบัก

ก่อนที่คุณจะเริ่มทดสอบเซิร์ฟเวอร์ MCP ของคุณ สิ่งสำคัญคือต้องเข้าใจเครื่องมือที่มีอยู่และแนวทางปฏิบัติที่ดีที่สุดสำหรับการดีบัก การทดสอบอย่างมีประสิทธิภาพช่วยให้เซิร์ฟเวอร์ของคุณทำงานตามที่คาดหวังและช่วยให้คุณระบุและแก้ไขปัญหาได้อย่างรวดเร็ว ส่วนต่อไปนี้จะสรุปวิธีการที่แนะนำสำหรับการตรวจสอบการทำงานของ MCP ของคุณ

## ภาพรวม

บทเรียนนี้ครอบคลุมวิธีการเลือกแนวทางการทดสอบที่เหมาะสมและเครื่องมือทดสอบที่มีประสิทธิภาพที่สุด

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- อธิบายแนวทางต่างๆ สำหรับการทดสอบได้
- ใช้เครื่องมือต่างๆ เพื่อทดสอบโค้ดของคุณอย่างมีประสิทธิภาพ

## การทดสอบ MCP Servers

MCP มีเครื่องมือช่วยให้คุณทดสอบและดีบักเซิร์ฟเวอร์ของคุณได้:

- **MCP Inspector**: เครื่องมือบรรทัดคำสั่งที่สามารถใช้งานได้ทั้งในรูปแบบ CLI และแบบมีอินเทอร์เฟซกราฟิก
- **การทดสอบด้วยตนเอง**: คุณสามารถใช้เครื่องมืออย่าง curl เพื่อส่งคำขอเว็บได้ แต่เครื่องมือใดที่สามารถส่ง HTTP ได้ก็ใช้ได้เช่นกัน
- **การทดสอบหน่วย**: คุณสามารถใช้เฟรมเวิร์กทดสอบที่คุณชื่นชอบเพื่อทดสอบฟีเจอร์ของทั้งเซิร์ฟเวอร์และไคลเอนต์

### การใช้ MCP Inspector

เราได้อธิบายการใช้งานเครื่องมือนี้ในบทเรียนก่อนหน้าแล้ว แต่ขอพูดถึงภาพรวมสั้นๆ เครื่องมือนี้สร้างด้วย Node.js และคุณสามารถใช้งานได้โดยเรียกใช้คำสั่ง `npx` ซึ่งจะดาวน์โหลดและติดตั้งเครื่องมือชั่วคราว จากนั้นจะลบข้อมูลหลังจากทำงานเสร็จ

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) ช่วยคุณ:

- **ค้นหาความสามารถของเซิร์ฟเวอร์**: ตรวจจับทรัพยากร เครื่องมือ และพรอมต์ที่มีโดยอัตโนมัติ
- **ทดสอบการทำงานของเครื่องมือ**: ลองใช้พารามิเตอร์ต่างๆ และดูผลลัพธ์แบบเรียลไทม์
- **ดูข้อมูลเมตาของเซิร์ฟเวอร์**: ตรวจสอบข้อมูลเซิร์ฟเวอร์ สคีมา และการตั้งค่า

การใช้งานเครื่องมือทั่วไปจะมีลักษณะดังนี้:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

คำสั่งข้างต้นจะเริ่มต้น MCP พร้อมอินเทอร์เฟซกราฟิกและเปิดเว็บอินเทอร์เฟซในเบราว์เซอร์ของคุณ คุณจะเห็นแดชบอร์ดที่แสดงเซิร์ฟเวอร์ MCP ที่ลงทะเบียนไว้ เครื่องมือ ทรัพยากร และพรอมต์ที่มี อินเทอร์เฟซนี้ช่วยให้คุณทดสอบการทำงานของเครื่องมือแบบโต้ตอบ ตรวจสอบข้อมูลเมตาของเซิร์ฟเวอร์ และดูผลลัพธ์แบบเรียลไทม์ ทำให้การตรวจสอบและดีบักการใช้งาน MCP ของคุณง่ายขึ้น

หน้าตาของอินเทอร์เฟซเป็นแบบนี้: ![Inspector](../../../../translated_images/th/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

คุณยังสามารถรันเครื่องมือนี้ในโหมด CLI โดยเพิ่มอาร์กิวเมนต์ `--cli` ตัวอย่างการรันเครื่องมือในโหมด "CLI" ที่แสดงรายการเครื่องมือทั้งหมดบนเซิร์ฟเวอร์:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### การทดสอบด้วยตนเอง

นอกจากการใช้เครื่องมือ inspector เพื่อทดสอบความสามารถของเซิร์ฟเวอร์แล้ว อีกวิธีที่คล้ายกันคือการรันไคลเอนต์ที่สามารถใช้ HTTP ได้ เช่น curl

ด้วย curl คุณสามารถทดสอบ MCP servers โดยตรงผ่านคำขอ HTTP:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

จากตัวอย่างการใช้ curl ข้างต้น คุณจะใช้คำขอ POST เพื่อเรียกใช้เครื่องมือโดยส่ง payload ที่ประกอบด้วยชื่อเครื่องมือและพารามิเตอร์ ใช้วิธีที่เหมาะสมกับคุณที่สุด เครื่องมือ CLI โดยทั่วไปจะใช้งานได้รวดเร็วและสามารถเขียนสคริปต์ได้ ซึ่งมีประโยชน์ในสภาพแวดล้อม CI/CD

### การทดสอบหน่วย

สร้างการทดสอบหน่วยสำหรับเครื่องมือและทรัพยากรของคุณเพื่อให้แน่ใจว่าทำงานได้ตามที่คาดหวัง นี่คือตัวอย่างโค้ดทดสอบ

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Mark the whole module for async tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Create a couple of test tools
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test without cursor parameter (omitted)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test with cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test with cursor as string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test with empty string cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

โค้ดข้างต้นทำสิ่งต่อไปนี้:

- ใช้เฟรมเวิร์ก pytest ที่ช่วยให้คุณสร้างการทดสอบในรูปแบบฟังก์ชันและใช้คำสั่ง assert
- สร้าง MCP Server ที่มีเครื่องมือสองตัวแตกต่างกัน
- ใช้คำสั่ง `assert` เพื่อตรวจสอบเงื่อนไขบางอย่างว่าถูกต้องหรือไม่

ดูไฟล์ฉบับเต็มได้ที่ [full file here](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

จากไฟล์ข้างต้น คุณสามารถทดสอบเซิร์ฟเวอร์ของคุณเองเพื่อให้แน่ใจว่าความสามารถถูกสร้างขึ้นตามที่ควรจะเป็น

SDK หลักๆ ทุกตัวมีส่วนทดสอบที่คล้ายกัน ดังนั้นคุณสามารถปรับใช้กับ runtime ที่คุณเลือกได้

## ตัวอย่าง

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## แหล่งข้อมูลเพิ่มเติม

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## ต่อไป

- ถัดไป: [Deployment](../09-deployment/README.md)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลนี้