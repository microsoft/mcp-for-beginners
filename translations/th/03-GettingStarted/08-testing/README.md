## การทดสอบและการดีบัก

ก่อนที่คุณจะเริ่มทดสอบเซิร์ฟเวอร์ MCP ของคุณ สิ่งสำคัญคือต้องเข้าใจเครื่องมือที่มีและแนวทางปฏิบัติที่ดีที่สุดสำหรับการดีบัก การทดสอบที่มีประสิทธิภาพช่วยให้เซิร์ฟเวอร์ของคุณทำงานตามที่คาดหวังและช่วยให้คุณระบุและแก้ไขปัญหาได้อย่างรวดเร็ว ส่วนต่อไปนี้สรุปแนวทางที่แนะนำสำหรับการตรวจสอบการใช้งาน MCP ของคุณ

## ภาพรวม

บทเรียนนี้จะกล่าวถึงวิธีการเลือกแนวทางการทดสอบที่เหมาะสมและเครื่องมือทดสอบที่มีประสิทธิภาพที่สุด

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- อธิบายแนวทางต่าง ๆ สำหรับการทดสอบ
- ใช้เครื่องมือต่าง ๆ เพื่อทดสอบโค้ดของคุณอย่างมีประสิทธิภาพ


## การทดสอบเซิร์ฟเวอร์ MCP

MCP มีเครื่องมือช่วยให้คุณทดสอบและดีบักเซิร์ฟเวอร์ของคุณ:

- **MCP Inspector**: เครื่องมือบรรทัดคำสั่งที่สามารถใช้งานได้ทั้งในโหมด CLI และโหมดภาพ
- **การทดสอบแบบแมนนวล**: คุณสามารถใช้เครื่องมือเช่น curl เพื่อรันคำร้องเว็บ แต่เครื่องมือใด ๆ ที่สามารถรัน HTTP ได้ก็ใช้ได้
- **การทดสอบยูนิต**: คุณสามารถใช้เฟรมเวิร์กการทดสอบที่คุณชื่นชอบเพื่อทดสอบฟีเจอร์ของทั้งเซิร์ฟเวอร์และไคลเอ็นต์

### การใช้ MCP Inspector

เราได้อธิบายการใช้งานเครื่องมือนี้ในบทเรียนก่อนหน้านี้ แต่ขอพูดถึงภาพรวมเล็กน้อย มันเป็นเครื่องมือที่สร้างขึ้นใน Node.js และคุณสามารถใช้โดยการเรียก `npx` executable ที่จะดาวน์โหลดและติดตั้งเครื่องมือนี้ชั่วคราวและจะลบออกเองหลังจากที่ทำงานเสร็จ

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) ช่วยให้คุณ:

- **ค้นพบความสามารถของเซิร์ฟเวอร์**: ตรวจจับทรัพยากร เครื่องมือ และพรอมต์ที่มีโดยอัตโนมัติ
- **ทดสอบการทำงานของเครื่องมือ**: ลองพารามิเตอร์ต่าง ๆ และดูคำตอบแบบเรียลไทม์
- **ดูข้อมูลเมตาของเซิร์ฟเวอร์**: ตรวจสอบข้อมูลเซิร์ฟเวอร์ โครงสร้างข้อมูล และการตั้งค่า

การรันเครื่องมือทั่วไปจะเป็นดังนี้:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

คำสั่งข้างต้นจะเริ่มเซิร์ฟเวอร์ MCP และอินเทอร์เฟซภาพรวม พร้อมเปิดเว็บอินเทอร์เฟซในเบราว์เซอร์ของคุณ คุณจะเห็นแดชบอร์ดแสดงเซิร์ฟเวอร์ MCP ที่ลงทะเบียนไว้ เครื่องมือที่พร้อมใช้งาน ทรัพยากร และพรอมต์ อินเทอร์เฟซนี้ช่วยให้คุณทดสอบการทำงานของเครื่องมือแบบโต้ตอบ ตรวจสอบข้อมูลเมตาเซิร์ฟเวอร์ และดูคำตอบแบบเรียลไทม์ ทำให้ง่ายต่อการตรวจสอบและดีบักการใช้งานเซิร์ฟเวอร์ MCP ของคุณ

ตัวอย่างด้านล่างนี้แสดงหน้าตาอินเทอร์เฟซ: ![Inspector](../../../../translated_images/th/connect.141db0b2bd05f096.webp)

คุณยังสามารถรันเครื่องมือนี้ในโหมด CLI โดยเพิ่มแอตทริบิวต์ `--cli` นี่คือตัวอย่างการรันเครื่องมือในโหมด "CLI" ซึ่งจะแสดงรายการเครื่องมือทั้งหมดบนเซิร์ฟเวอร์:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### การทดสอบแบบแมนนวล

นอกจากการรันเครื่องมือ inspector เพื่อทดสอบความสามารถของเซิร์ฟเวอร์แล้ว แนวทางที่คล้ายกันคือการรันไคลเอ็นต์ที่สามารถใช้ HTTP เช่น curl

ด้วย curl คุณสามารถทดสอบเซิร์ฟเวอร์ MCP ได้โดยตรงผ่านคำร้องขอ HTTP:

```bash
# ตัวอย่าง: ข้อมูลเมตาของเซิร์ฟเวอร์ทดสอบ
curl http://localhost:3000/v1/metadata

# ตัวอย่าง: เรียกใช้เครื่องมือ
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

จากตัวอย่างการใช้งาน curl ข้างต้น คุณใช้คำขอ POST เพื่อเรียกเครื่องมือโดยส่งพารามิเตอร์ที่ประกอบด้วยชื่อเครื่องมือและพารามิเตอร์ของมัน ใช้วิธีที่เหมาะสมกับคุณที่สุด โดยทั่วไป เครื่องมือ CLI จะใช้งานได้รวดเร็วกว่าและเหมาะสำหรับการสคริปต์ ซึ่งมีประโยชน์ในสภาพแวดล้อม CI/CD

### การทดสอบยูนิต

สร้างการทดสอบยูนิตสำหรับเครื่องมือและทรัพยากรของคุณเพื่อให้แน่ใจว่าพวกมันทำงานตามที่คาดหวัง นี่คือตัวอย่างโค้ดทดสอบ

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

    # สร้างเครื่องมือทดสอบสองสามชิ้น
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # ทดสอบโดยไม่มีพารามิเตอร์เคอร์เซอร์ (ละไว้)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # ทดสอบด้วย cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # ทดสอบด้วย cursor เป็นสตริง
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # ทดสอบด้วยเคอร์เซอร์เป็นสตริงว่าง
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

โค้ดด้านบนทำสิ่งต่อไปนี้:

- ใช้เฟรมเวิร์ก pytest ซึ่งช่วยให้คุณสร้างการทดสอบเป็นฟังก์ชันและใช้คำสั่ง assert
- สร้างเซิร์ฟเวอร์ MCP พร้อมเครื่องมือสองตัวที่แตกต่างกัน
- ใช้คำสั่ง `assert` เพื่อตรวจสอบเงื่อนไขบางอย่าง

ดู [ไฟล์เต็มที่นี่](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

จากไฟล์ข้างต้น คุณสามารถทดสอบเซิร์ฟเวอร์ของคุณเองเพื่อให้แน่ใจว่าฟีเจอร์ถูกสร้างขึ้นตามที่ควรจะเป็น

ทุก SDK สำคัญมีส่วนทดสอบที่คล้ายกันดังนั้นคุณสามารถปรับแต่งให้เหมาะกับ runtime ที่คุณเลือก

## ตัวอย่าง 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## แหล่งข้อมูลเพิ่มเติม

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## ต่อไป

- ต่อไป: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาดั้งเดิมถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->