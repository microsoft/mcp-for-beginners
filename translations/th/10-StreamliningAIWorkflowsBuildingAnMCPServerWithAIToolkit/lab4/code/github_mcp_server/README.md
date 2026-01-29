# Weather MCP Server

นี่คือตัวอย่าง MCP Server ที่เขียนด้วย Python ซึ่งมีเครื่องมือเกี่ยวกับสภาพอากาศพร้อมการตอบกลับจำลอง สามารถใช้เป็นโครงสร้างพื้นฐานสำหรับ MCP Server ของคุณเอง โดยมีฟีเจอร์ดังนี้:

- **Weather Tool**: เครื่องมือที่ให้ข้อมูลสภาพอากาศจำลองตามตำแหน่งที่ระบุ
- **Git Clone Tool**: เครื่องมือที่ใช้โคลน repository ของ git ไปยังโฟลเดอร์ที่กำหนด
- **VS Code Open Tool**: เครื่องมือที่เปิดโฟลเดอร์ใน VS Code หรือ VS Code Insiders
- **Connect to Agent Builder**: ฟีเจอร์ที่ช่วยให้คุณเชื่อมต่อ MCP Server กับ Agent Builder เพื่อการทดสอบและดีบัก
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: ฟีเจอร์ที่ช่วยให้คุณดีบัก MCP Server โดยใช้ MCP Inspector

## เริ่มต้นใช้งาน Weather MCP Server Template

> **ข้อกำหนดเบื้องต้น**
>
> ในการรัน MCP Server บนเครื่องพัฒนาของคุณ คุณจะต้องมี:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (จำเป็นสำหรับเครื่องมือ git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) หรือ [VS Code Insiders](https://code.visualstudio.com/insiders/) (จำเป็นสำหรับเครื่องมือ open_in_vscode)
> - (*ตัวเลือก - หากคุณต้องการใช้ uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## เตรียมสภาพแวดล้อม

มีสองวิธีในการตั้งค่าสภาพแวดล้อมสำหรับโปรเจกต์นี้ คุณสามารถเลือกวิธีใดก็ได้ตามความสะดวกของคุณ

> หมายเหตุ: รีโหลด VSCode หรือ terminal เพื่อให้แน่ใจว่า Python จาก virtual environment ถูกใช้งานหลังจากสร้าง virtual environment

| วิธี | ขั้นตอน |
| ---- | ------- |
| ใช้ `uv` | 1. สร้าง virtual environment: `uv venv` <br>2. รันคำสั่งใน VSCode "***Python: Select Interpreter***" และเลือก Python จาก virtual environment ที่สร้างขึ้น <br>3. ติดตั้ง dependencies (รวม dev dependencies): `uv pip install -r pyproject.toml --extra dev` |
| ใช้ `pip` | 1. สร้าง virtual environment: `python -m venv .venv` <br>2. รันคำสั่งใน VSCode "***Python: Select Interpreter***" และเลือก Python จาก virtual environment ที่สร้างขึ้น<br>3. ติดตั้ง dependencies (รวม dev dependencies): `pip install -e .[dev]` | 

หลังจากตั้งค่าสภาพแวดล้อมแล้ว คุณสามารถรันเซิร์ฟเวอร์บนเครื่องพัฒนาของคุณผ่าน Agent Builder ในฐานะ MCP Client เพื่อเริ่มต้น:
1. เปิด VS Code Debug panel เลือก `Debug in Agent Builder` หรือกด `F5` เพื่อเริ่มดีบัก MCP Server
2. ใช้ AI Toolkit Agent Builder เพื่อทดสอบเซิร์ฟเวอร์ด้วย [prompt นี้](../../../../../../../../../../../open_prompt_builder) เซิร์ฟเวอร์จะเชื่อมต่อกับ Agent Builder โดยอัตโนมัติ
3. คลิก `Run` เพื่อทดสอบเซิร์ฟเวอร์ด้วย prompt

**ยินดีด้วย**! คุณได้รัน Weather MCP Server บนเครื่องพัฒนาของคุณผ่าน Agent Builder ในฐานะ MCP Client สำเร็จแล้ว
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## สิ่งที่รวมอยู่ใน Template

| โฟลเดอร์ / ไฟล์ | เนื้อหา                                     |
| --------------- | ------------------------------------------ |
| `.vscode`       | ไฟล์ VSCode สำหรับการดีบัก                |
| `.aitk`         | การตั้งค่าสำหรับ AI Toolkit               |
| `src`           | โค้ดต้นฉบับสำหรับ Weather MCP Server     |

## วิธีดีบัก Weather MCP Server

> หมายเหตุ:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) เป็นเครื่องมือสำหรับนักพัฒนาเพื่อการทดสอบและดีบัก MCP Server
> - โหมดดีบักทั้งหมดรองรับ breakpoints คุณสามารถเพิ่ม breakpoints ในโค้ดของเครื่องมือได้

## เครื่องมือที่มีอยู่

### Weather Tool
เครื่องมือ `get_weather` ให้ข้อมูลสภาพอากาศจำลองสำหรับตำแหน่งที่ระบุ

| พารามิเตอร์ | ประเภท | คำอธิบาย |
| ------------ | ------ | --------- |
| `location`   | string | ตำแหน่งที่ต้องการข้อมูลสภาพอากาศ (เช่น ชื่อเมือง รัฐ หรือพิกัด) |

### Git Clone Tool
เครื่องมือ `git_clone_repo` ใช้โคลน repository ของ git ไปยังโฟลเดอร์ที่กำหนด

| พารามิเตอร์      | ประเภท | คำอธิบาย |
| ----------------- | ------ | --------- |
| `repo_url`        | string | URL ของ git repository ที่ต้องการโคลน |
| `target_folder`   | string | เส้นทางไปยังโฟลเดอร์ที่ repository จะถูกโคลน |

เครื่องมือจะคืนค่า JSON object ที่มี:
- `success`: Boolean ที่บ่งบอกว่าการดำเนินการสำเร็จหรือไม่
- `target_folder` หรือ `error`: เส้นทางของ repository ที่ถูกโคลนหรือข้อความแสดงข้อผิดพลาด

### VS Code Open Tool
เครื่องมือ `open_in_vscode` ใช้เปิดโฟลเดอร์ในแอปพลิเคชัน VS Code หรือ VS Code Insiders

| พารามิเตอร์      | ประเภท | คำอธิบาย |
| ----------------- | ------ | --------- |
| `folder_path`     | string | เส้นทางไปยังโฟลเดอร์ที่ต้องการเปิด |
| `use_insiders`    | boolean (ตัวเลือก) | ใช้ VS Code Insiders แทน VS Code ปกติหรือไม่ |

เครื่องมือจะคืนค่า JSON object ที่มี:
- `success`: Boolean ที่บ่งบอกว่าการดำเนินการสำเร็จหรือไม่
- `message` หรือ `error`: ข้อความยืนยันหรือข้อความแสดงข้อผิดพลาด

| โหมดดีบัก       | คำอธิบาย | ขั้นตอนการดีบัก |
| ---------------- | --------- | ---------------- |
| Agent Builder    | ดีบัก MCP Server ใน Agent Builder ผ่าน AI Toolkit | 1. เปิด VS Code Debug panel เลือก `Debug in Agent Builder` และกด `F5` เพื่อเริ่มดีบัก MCP Server<br>2. ใช้ AI Toolkit Agent Builder เพื่อทดสอบเซิร์ฟเวอร์ด้วย [prompt นี้](../../../../../../../../../../../open_prompt_builder) เซิร์ฟเวอร์จะเชื่อมต่อกับ Agent Builder โดยอัตโนมัติ<br>3. คลิก `Run` เพื่อทดสอบเซิร์ฟเวอร์ด้วย prompt |
| MCP Inspector    | ดีบัก MCP Server โดยใช้ MCP Inspector | 1. ติดตั้ง [Node.js](https://nodejs.org/)<br> 2. ตั้งค่า Inspector: `cd inspector` && `npm install` <br> 3. เปิด VS Code Debug panel เลือก `Debug SSE in Inspector (Edge)` หรือ `Debug SSE in Inspector (Chrome)` กด F5 เพื่อเริ่มดีบัก<br> 4. เมื่อ MCP Inspector เปิดในเบราว์เซอร์ คลิกปุ่ม `Connect` เพื่อเชื่อมต่อ MCP Server นี้<br> 5. จากนั้นคุณสามารถ `List Tools` เลือกเครื่องมือ ป้อนพารามิเตอร์ และ `Run Tool` เพื่อดีบักโค้ดเซิร์ฟเวอร์ของคุณ<br> |

## พอร์ตเริ่มต้นและการปรับแต่ง

| โหมดดีบัก       | พอร์ต | คำจำกัดความ | การปรับแต่ง | หมายเหตุ |
| ---------------- | ----- | ------------ | ----------- | -------- |
| Agent Builder    | 3001  | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | แก้ไข [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) เพื่อเปลี่ยนพอร์ตด้านบน | N/A |
| MCP Inspector    | 3001 (Server); 5173 และ 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | แก้ไข [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) เพื่อเปลี่ยนพอร์ตด้านบน | N/A |

## ข้อเสนอแนะ

หากคุณมีข้อเสนอแนะหรือคำแนะนำสำหรับ template นี้ โปรดเปิด issue ใน [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้