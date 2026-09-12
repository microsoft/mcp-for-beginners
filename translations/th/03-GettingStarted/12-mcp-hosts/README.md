# การตั้งค่าลูกค้าโฮสต์ MCP ที่ได้รับความนิยม

> [!NOTE]
> การกำหนดค่าโฮสต์ที่ชี้ไปยัง `/sse` เป็นตัวอย่าง HTTP+SSE แบบเก่าสำหรับ
> MCP `2025-11-25` สำหรับ MCP `2026-07-28` ให้เลือก Streamable HTTP ในโฮสต์ที่
> รองรับและใช้จุดสิ้นสุดที่เซิร์ฟเวอร์กำหนดค่าไว้

ไกด์นี้ครอบคลุมวิธีการกำหนดค่าและใช้งานเซิร์ฟเวอร์ MCP กับแอปโฮสต์ AI ยอดนิยม แต่ละโฮสต์มีวิธีการกำหนดค่าของตัวเอง แต่เมื่อกำหนดค่าแล้ว ทั้งหมดจะติดต่อกับเซิร์ฟเวอร์ MCP โดยใช้โปรโตคอลมาตรฐานเดียวกัน

## โฮสต์ MCP คืออะไร?

**โฮสต์ MCP** คือแอปพลิเคชัน AI ที่สามารถเชื่อมต่อกับเซิร์ฟเวอร์ MCP เพื่อขยายความสามารถของมัน คิดว่าเป็น "ส่วนหน้าที่" ผู้ใช้โต้ตอบด้วย ขณะที่เซิร์ฟเวอร์ MCP ให้เครื่องมือและข้อมูล "ส่วนหลัง"

```mermaid
flowchart LR
    User[👤 ผู้ใช้] --> Host[🖥️ โฮสต์ MCP]
    Host --> S1[เซิร์ฟเวอร์ MCP A]
    Host --> S2[เซิร์ฟเวอร์ MCP B]
    Host --> S3[เซิร์ฟเวอร์ MCP C]
    
    subgraph "โฮสต์ยอดนิยม"
        H1[Claude เดสก์ท็อป]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## ความต้องการเบื้องต้น

- เซิร์ฟเวอร์ MCP ที่จะเชื่อมต่อ (ดู [บทที่ 3.1 - เซิร์ฟเวอร์แรก](../01-first-server/README.md))
- แอปโฮสต์ที่ติดตั้งบนระบบของคุณ
- ความคุ้นเคยพื้นฐานกับไฟล์กำหนดค่า JSON

---

## 1. Claude Desktop

**Claude Desktop** คือแอปพลิเคชันเดสก์ท็อปอย่างเป็นทางการของ Anthropic ที่รองรับ MCP โดยตรง

### การติดตั้ง

1. ดาวน์โหลด Claude Desktop จาก [claude.ai/download](https://claude.ai/download)
2. ติดตั้งและลงชื่อเข้าใช้ด้วยบัญชี Anthropic ของคุณ

### การกำหนดค่า

Claude Desktop ใช้ไฟล์กำหนดค่า JSON เพื่อกำหนดค่าเซิร์ฟเวอร์ MCP

**ตำแหน่งไฟล์กำหนดค่า:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**ตัวอย่างการกำหนดค่า:**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### ตัวเลือกการกำหนดค่า

| ฟิลด์ | คำอธิบาย | ตัวอย่าง |
|-------|-------------|---------|
| `command` | ไฟล์ที่ใช้เรียกใช้งาน | `"python"`, `"node"`, `"npx"` |
| `args` | อาร์กิวเมนต์บรรทัดคำสั่ง | `["-m", "my_server"]` |
| `env` | ตัวแปรสภาพแวดล้อม | `{"API_KEY": "xxx"}` |
| `cwd` | ไดเรกทอรีทำงาน | `"/path/to/server"` |

### ทดสอบการตั้งค่าของคุณ

1. บันทึกไฟล์กำหนดค่า
2. ปิดและเปิด Claude Desktop ใหม่ทั้งหมด
3. เปิดบทสนทนาใหม่
4. มองหาไอคอน 🔌 บ่งชี้เซิร์ฟเวอร์เชื่อมต่อแล้ว
5. ลองขอให้ Claude ใช้เครื่องมือของคุณ

### การแก้ไขปัญหา Claude Desktop

**เซิร์ฟเวอร์ไม่แสดง:**
- ตรวจสอบไวยากรณ์ไฟล์กำหนดค่าด้วยตัวตรวจสอบ JSON
- ตรวจสอบให้แน่ใจว่าเส้นทาง command ถูกต้อง
- ตรวจสอบบันทึก Claude Desktop: ช่วยเหลือ → แสดงบันทึก

**เซิร์ฟเวอร์แครชเมื่อเริ่มต้น:**
- ทดสอบเซิร์ฟเวอร์ของคุณด้วยตนเองในเทอร์มินัลก่อน
- ตรวจสอบว่าตัวแปรสภาพแวดล้อมตั้งค่าอย่างถูกต้อง
- ตรวจสอบว่าติดตั้ง dependencies ครบถ้วน

---

## 2. VS Code กับ GitHub Copilot

VS Code รองรับ MCP ผ่านส่วนขยาย GitHub Copilot Chat

### ความต้องการเบื้องต้น

1. ติดตั้ง VS Code 1.99 ขึ้นไป
2. ติดตั้งส่วนขยาย GitHub Copilot
3. ติดตั้งส่วนขยาย GitHub Copilot Chat

### การกำหนดค่า

VS Code ใช้ไฟล์ `.vscode/mcp.json` ใน workspace หรือการตั้งค่าผู้ใช้ของคุณ

**การกำหนดค่า workspace** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**การตั้งค่าผู้ใช้** (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### การใช้งาน MCP ใน VS Code

1. เปิดแผง Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. พิมพ์ `@` เพื่อดูเครื่องมือ MCP ที่พร้อมใช้งาน
3. ใช้ภาษาธรรมชาติเพื่อเรียกใช้เครื่องมือ: "คำนวณ 25 * 48 โดยใช้เครื่องคิดเลข"

### การแก้ไขปัญหา VS Code

**เซิร์ฟเวอร์ MCP ไม่โหลด:**
- ตรวจสอบแผง Output → "MCP" เพื่อดูบันทึกข้อผิดพลาด
- โหลดหน้าต่างใหม่: Ctrl+Shift+P → "Developer: Reload Window"
- ยืนยันว่าเซิร์ฟเวอร์ทำงานได้แบบสแตนด์อโลนก่อน

---

## 3. Cursor

**Cursor** คือโปรแกรมแก้ไขโค้ดที่เน้น AI เป็นหลักพร้อมการสนับสนุน MCP ในตัว

### การติดตั้ง

1. ดาวน์โหลด Cursor จาก [cursor.sh](https://cursor.sh)
2. ติดตั้งและลงชื่อเข้าใช้

### การกำหนดค่า

Cursor ใช้รูปแบบการกำหนดค่าคล้ายกับ Claude Desktop

**ตำแหน่งไฟล์กำหนดค่า:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**ตัวอย่างการกำหนดค่า:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### การใช้งาน MCP ใน Cursor

1. เปิดแชท AI ของ Cursor (Ctrl+L / Cmd+L)
2. เครื่องมือ MCP จะปรากฏโดยอัตโนมัติในคำแนะนำ
3. ขอให้ AI ทำงานโดยใช้เซิร์ฟเวอร์ที่เชื่อมต่ออยู่

---

## 4. Cline (แบบเทอร์มินัล)

**Cline** คือไคลเอนต์ MCP แบบเทอร์มินัล เหมาะสำหรับเวิร์กโฟลว์บรรทัดคำสั่ง

### การติดตั้ง

```bash
npm install -g @anthropic/cline
```

### การกำหนดค่า

Cline ใช้ตัวแปรสภาพแวดล้อมและอาร์กิวเมนต์บรรทัดคำสั่ง

**การใช้ตัวแปรสภาพแวดล้อม:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**การใช้อาร์กิวเมนต์บรรทัดคำสั่ง:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**ไฟล์กำหนดค่า** (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### การใช้งาน Cline

```bash
# เริ่มเซสชันแบบโต้ตอบ
cline

# คิวรีเดี่ยวกับ MCP
cline "Calculate the square root of 144 using the calculator"

# แสดงรายการเครื่องมือที่มีอยู่
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** คือโปรแกรมแก้ไขโค้ด AI อีกตัวที่มีการสนับสนุน MCP

### การติดตั้ง

1. ดาวน์โหลด Windsurf จาก [codeium.com/windsurf](https://codeium.com/windsurf)
2. ติดตั้งและสร้างบัญชีผู้ใช้

### การกำหนดค่า

การกำหนดค่า Windsurf จัดการผ่าน UI การตั้งค่า:

1. เปิดการตั้งค่า (Ctrl+, / Cmd+,)
2. ค้นหา "MCP"
3. คลิก "แก้ไขใน settings.json"

**ตัวอย่างการกำหนดค่า:**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## การเปรียบเทียบประเภทการขนส่ง

โฮสต์แต่ละตัวรองรับกลไกการขนส่งที่แตกต่างกัน:

| โฮสต์ | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (อินพุต/เอาท์พุตมาตรฐาน): เหมาะสำหรับเซิร์ฟเวอร์ท้องถิ่นที่เริ่มโดยโฮสต์
**SSE/HTTP**: เหมาะสำหรับเซิร์ฟเวอร์ระยะไกลหรือเซิร์ฟเวอร์ที่แชร์ระหว่างลูกค้าหลายราย

---

## การแก้ไขปัญหาทั่วไป

### เซิร์ฟเวอร์ไม่เริ่มทำงาน

1. **ทดสอบเซิร์ฟเวอร์ด้วยตนเองก่อน:**
   ```bash
   # สำหรับ Python
   python -m your_server_module
   
   # สำหรับ Node.js
   node /path/to/server/index.js
   ```

2. **ตรวจสอบเส้นทางคำสั่ง:**
   - ใช้เส้นทางสัมบูรณ์เมื่อเป็นไปได้
   - ตรวจสอบว่าไฟล์ที่เรียกใช้งานอยู่ใน PATH ของคุณ

3. **ตรวจสอบ dependencies:**
   ```bash
   # ไพธอน
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### เซิร์ฟเวอร์เชื่อมต่อแต่เครื่องมือไม่ทำงาน

1. **ตรวจสอบบันทึกเซิร์ฟเวอร์** - โฮสต์ส่วนใหญ่มีตัวเลือกบันทึก
2. **ตรวจสอบการลงทะเบียนเครื่องมือ** - ใช้ MCP Inspector ในการทดสอบ
3. **ตรวจสอบสิทธิ์** - เครื่องมือบางอย่างต้องการสิทธิ์ไฟล์/เครือข่าย

### ตัวแปรสภาพแวดล้อมไม่ถูกส่งผ่าน

- โฮสต์บางตัวล้างค่าตัวแปรสภาพแวดล้อม
- ใช้ฟิลด์ `env` ในการกำหนดค่าอย่างชัดเจน
- หลีกเลี่ยงการเก็บข้อมูลที่ละเอียดอ่อนในไฟล์กำหนดค่า (ใช้การจัดการความลับ)

---

## แนวทางปฏิบัติด้านความปลอดภัยที่ดีที่สุด

1. **อย่าคอมมิตคีย์ API** ลงในไฟล์กำหนดค่า
2. **ใช้ตัวแปรสภาพแวดล้อม** สำหรับข้อมูลที่ละเอียดอ่อน
3. **จำกัดสิทธิ์เซิร์ฟเวอร์** ให้เฉพาะที่จำเป็น
4. **ตรวจทานโค้ดเซิร์ฟเวอร์** ก่อนให้สิทธิ์เข้าถึงระบบของคุณ
5. **ใช้ allowlists** สำหรับการเข้าถึงระบบไฟล์และเครือข่าย

---

## ขั้นตอนถัดไป

- [3.13 - การดีบั๊กด้วย MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - สร้างเซิร์ฟเวอร์ MCP แรกของคุณ](../01-first-server/README.md)
- [บทที่ 5 - หัวข้อขั้นสูง](../../05-AdvancedTopics/README.md)

---

## แหล่งข้อมูลเพิ่มเติม

- [เอกสาร Claude Desktop MCP](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [ส่วนขยาย VS Code MCP](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [เอกสาร MCP - การขนส่ง](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [ทะเบียนเซิร์ฟเวอร์ MCP อย่างเป็นทางการ](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->