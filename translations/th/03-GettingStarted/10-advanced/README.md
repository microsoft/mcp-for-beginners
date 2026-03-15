# การใช้งานเซิร์ฟเวอร์ขั้นสูง

มีเซิร์ฟเวอร์สองประเภทที่เปิดเผยใน MCP SDK คือ เซิร์ฟเวอร์ปกติและเซิร์ฟเวอร์ระดับล่าง โดยปกติคุณจะใช้เซิร์ฟเวอร์ปกติเพื่อเพิ่มฟีเจอร์เข้าไป แต่ในบางกรณี คุณอาจต้องพึ่งพาเซิร์ฟเวอร์ระดับล่าง เช่น:

- สถาปัตยกรรมที่ดีขึ้น สามารถสร้างสถาปัตยกรรมที่สะอาดได้ด้วยทั้งเซิร์ฟเวอร์ปกติและระดับล่าง แต่สามารถโต้แย้งได้ว่าสะดวกกว่าเล็กน้อยเมื่อใช้เซิร์ฟเวอร์ระดับล่าง
- ความพร้อมใช้งานของฟีเจอร์ ฟีเจอร์ขั้นสูงบางอย่างสามารถใช้ได้เฉพาะกับเซิร์ฟเวอร์ระดับล่างเท่านั้น คุณจะเห็นตัวอย่างนี้ในบทต่อๆ ไปเมื่อเราทำการเพิ่มการสุ่มตัวอย่างและการกระตุ้น

## เซิร์ฟเวอร์ปกติกับเซิร์ฟเวอร์ระดับล่าง

นี่คือลักษณะการสร้าง MCP Server ด้วยเซิร์ฟเวอร์ปกติ

**Python**

```python
mcp = FastMCP("Demo")

# เพิ่มเครื่องมือบวก
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

**TypeScript**

```typescript
const server = new McpServer({
  name: "demo-server",
  version: "1.0.0"
});

// เพิ่มเครื่องมือบวก
server.registerTool("add",
  {
    title: "Addition Tool",
    description: "Add two numbers",
    inputSchema: { a: z.number(), b: z.number() }
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);
```

ประเด็นคือคุณเพิ่มแต่ละเครื่องมือ แหล่งข้อมูล หรือพรอมต์ที่คุณต้องการให้เซิร์ฟเวอร์มีอย่างชัดเจน ไม่มีอะไรผิดปกติกับวิธีนี้

### วิธีการเซิร์ฟเวอร์ระดับล่าง

อย่างไรก็ตาม เมื่อคุณใช้วิธีเซิร์ฟเวอร์ระดับล่าง คุณต้องคิดต่างออกไป แทนที่จะลงทะเบียนแต่ละเครื่องมือ คุณจะสร้างสองตัวจัดการแยกตามประเภทฟีเจอร์ (เครื่องมือ แหล่งข้อมูล หรือพรอมต์) เช่น สำหรับเครื่องมือ จะมีสองฟังก์ชันดังนี้:

- การแสดงรายการเครื่องมือทั้งหมด ฟังก์ชันหนึ่งจะรับผิดชอบการพยายามทั้งหมดในการแสดงรายการเครื่องมือ
- การจัดการการเรียกใช้เครื่องมือทั้งหมด ที่นี่ก็เช่นกัน มีเพียงฟังก์ชันเดียวที่จัดการการเรียกใช้เครื่องมือ

ฟังดูเหมือนงานจะน้อยลงใช่ไหม? ดังนั้นแทนที่จะลงทะเบียนเครื่องมือ ฉันแค่ต้องแน่ใจว่าเครื่องมือได้รับการแสดงรายการเมื่อฉันแสดงเครื่องมือทั้งหมด และถูกเรียกเมื่อมีคำขอเรียกเครื่องมือเข้ามา

มาดูโค้ดเป็นอย่างไรตอนนี้:

**Python**

```python
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="add",
            description="Add two numbers",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "number to add"}, 
                    "b": {"type": "number", "description": "number to add"}
                },
                "required": ["query"],
            },
        )
    ]
```

**TypeScript**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // ส่งกลับรายการเครื่องมือที่ลงทะเบียนแล้ว
  return {
    tools: [{
        name="add",
        description="Add two numbers",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "number to add"}, 
                "b": {"type": "number", "description": "number to add"}
            },
            "required": ["query"],
        }
    }]
  };
});
```

ที่นี่เรามีฟังก์ชันที่คืนค่ารายการฟีเจอร์ รายการแต่ละรายการในเครื่องมือมีฟิลด์เช่น `name`, `description` และ `inputSchema` เพื่อให้ตรงกับชนิดที่คืนค่าได้ ซึ่งทำให้เราวางนิยามเครื่องมือและฟีเจอร์ไว้ที่อื่นได้ เราสามารถสร้างเครื่องมือทั้งหมดไว้ในโฟลเดอร์ tools และทำแบบเดียวกันกับฟีเจอร์อื่นๆ เพื่อให้โปรเจกต์ของคุณจัดระเบียบได้ดังนี้:

```text
app
--| tools
----| add
----| substract
--| resources
----| products
----| schemas
--| prompts
----| product-description
```

นั่นยอดเยี่ยม สถาปัตยกรรมของเราสามารถดูสะอาดเรียบร้อยมากขึ้น

แล้วการเรียกใช้เครื่องมือ เป็นแบบเดียวกันใช่ไหม คือมีตัวจัดการเดียวสำหรับเรียกเครื่องมือใดก็ได้? ใช่เลย นี่คือโค้ดสำหรับส่วนนี้:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools เป็นพจนานุกรมที่มีชื่อเครื่องมือเป็นคีย์
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

**TypeScript**

```typescript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { params: { name } } = request;
    let tool = tools.find(t => t.name === name);
    if(!tool) {
        return {
            error: {
                code: "tool_not_found",
                message: `Tool ${name} not found.`
            }
       };
    }
    
    // อาร์กิวเมนต์: request.params.arguments
    // TODO เรียกใช้เครื่องมือ,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

ตามที่คุณเห็นจากโค้ดด้านบน เราต้องแยกเครื่องมือที่จะเรียกและอาร์กิวเมนต์ จากนั้นดำเนินการเรียกเครื่องมือนั้น

## การปรับปรุงวิธีการด้วยการตรวจสอบความถูกต้อง

จนถึงตอนนี้ คุณได้เห็นวิธีที่การลงทะเบียนทั้งหมดเพื่อเพิ่มเครื่องมือ แหล่งข้อมูล และพรอมต์ สามารถแทนที่ได้ด้วยสองตัวจัดการนี้ต่อหนึ่งประเภทฟีเจอร์ เราต้องทำอะไรเพิ่ม? เราควรเพิ่มการตรวจสอบความถูกต้องเพื่อให้แน่ใจว่าเครื่องมือถูกเรียกด้วยอาร์กิวเมนต์ที่ถูกต้อง รุ่นรันไทม์แต่ละตัวมีวิธีแก้ปัญหาของตัวเอง เช่น Python ใช้ Pydantic และ TypeScript ใช้ Zod แนวคิดคือเราทำดังต่อไปนี้:

- ย้ายตรรกะสำหรับสร้างฟีเจอร์ (เครื่องมือ แหล่งข้อมูล หรือพรอมต์) ไปยังโฟลเดอร์ที่จัดทำขึ้นเฉพาะ
- เพิ่มวิธีการตรวจสอบคำขอที่เข้ามาเพื่อเรียกใช้เครื่องมือ

### สร้างฟีเจอร์

ในการสร้างฟีเจอร์ เราจะต้องสร้างไฟล์สำหรับฟีเจอร์นั้นและทำให้แน่ใจว่ามีฟิลด์บังคับที่จำเป็นของฟีเจอร์นั้น ซึ่งฟิลด์จะแตกต่างกันเล็กน้อยระหว่างเครื่องมือ แหล่งข้อมูล และพรอมต์

**Python**

```python
# schema.py
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float

# add.py

from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ตรวจสอบข้อมูลนำเข้าด้วยโมเดล Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: เพิ่ม Pydantic เพื่อให้เราสามารถสร้าง AddInputModel และตรวจสอบ args ได้

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ที่นี่คุณจะเห็นวิธีการทำดังนี้:

- สร้างสกีมาโดยใช้ Pydantic `AddInputModel` โดยมีฟิลด์ `a` และ `b` ในไฟล์ *schema.py*
- พยายามแยกคำขอที่เข้ามาให้เป็นชนิด `AddInputModel` หากพารามิเตอร์ไม่ตรงกัน จะทำให้เกิดข้อผิดพลาด:

   ```python
   # add.py
    try:
        # ตรวจสอบความถูกต้องของข้อมูลเข้าโดยใช้โมเดล Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

คุณสามารถเลือกว่าจะใส่ตรรกะการแยกนี้ในตัวเรียกเครื่องมือเอง หรือตัวฟังก์ชันจัดการ

**TypeScript**

```typescript
// server.ts
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { params: { name } } = request;
    let tool = tools.find(t => t.name === name);
    if (!tool) {
       return {
        error: {
            code: "tool_not_found",
            message: `Tool ${name} not found.`
        }
       };
    }
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);

       // @ts-ignore
       const result = await tool.callback(input);

       return {
          content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
      };
    } catch (error) {
       return {
          error: {
             code: "invalid_arguments",
             message: `Invalid arguments for tool ${name}: ${error instanceof Error ? error.message : String(error)}`
          }
    };
   }

});

// schema.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// add.ts
import { Tool } from "./tool.js";
import { MathInputSchema } from "./schema.js";
import { zodToJsonSchema } from "zod-to-json-schema";

export default {
    name: "add",
    rawSchema: MathInputSchema,
    inputSchema: zodToJsonSchema(MathInputSchema),
    callback: async ({ a, b }) => {
        return {
            content: [{ type: "text", text: String(a + b) }]
        };
    }
} as Tool;
```

- ในตัวจัดการที่จัดการการเรียกใช้เครื่องมือทั้งหมด ตอนนี้เราพยายามแยกคำขอที่เข้ามาให้ตรงกับสกีมาที่เครื่องมือนิยามไว้:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    หากสำเร็จ เราจะดำเนินการเรียกเครื่องมือ:

    ```typescript
    const result = await tool.callback(input);
    ```

ตามที่คุณเห็น วิธีนี้สร้างสถาปัตยกรรมที่ดีเพราะทุกอย่างมีที่ของมัน *server.ts* เป็นไฟล์ขนาดเล็กที่เชื่อมต่อกับตัวจัดการคำขอเท่านั้น และแต่ละฟีเจอร์อยู่ในโฟลเดอร์ที่เกี่ยวข้อง เช่น tools/, resources/ หรือ /prompts

ยอดเยี่ยม มาลองสร้างสิ่งนี้กันต่อ

## แบบฝึกหัด: สร้างเซิร์ฟเวอร์ระดับล่าง

ในแบบฝึกหัดนี้ เราจะทำดังนี้:

1. สร้างเซิร์ฟเวอร์ระดับล่างที่จัดการการแสดงรายการเครื่องมือและการเรียกเครื่องมือ
2. ใช้สถาปัตยกรรมที่สามารถขยายเพิ่มเติมได้
3. เพิ่มการตรวจสอบความถูกต้องเพื่อให้แน่ใจว่าการเรียกเครื่องมือของคุณถูกต้อง

### -1- สร้างสถาปัตยกรรม

สิ่งแรกที่เราต้องจัดการคือสถาปัตยกรรมที่ช่วยให้เราขยายตัวได้เมื่อต้องการเพิ่มฟีเจอร์ นี่คือลักษณะ:

**Python**

```text
server.py
--| tools
----| __init__.py
----| add.py
----| schema.py
client.py
```

**TypeScript**

```text
server.ts
--| tools
----| add.ts
----| schema.ts
client.ts
```

ตอนนี้เราได้ตั้งค่าสถาปัตยกรรมที่ช่วยให้เพิ่มเครื่องมือใหม่ได้ง่ายในโฟลเดอร์ tools แล้ว คุณสามารถเพิ่มโฟลเดอร์ย่อยสำหรับ resources และ prompts ได้ตามต้องการ

### -2- สร้างเครื่องมือ

มาดูวิธีสร้างเครื่องมือกันก่อน เครื่องมือต้องถูกสร้างในโฟลเดอร์ย่อย *tool* ดังนี้:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ตรวจสอบอินพุตโดยใช้โมเดล Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: เพิ่ม Pydantic เพื่อให้เราสามารถสร้าง AddInputModel และตรวจสอบ args ได้

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

เราจะเห็นวิธีนิยามชื่อ คำอธิบาย และสกีมาของอินพุตโดยใช้ Pydantic และตัวจัดการที่จะถูกเรียกเมื่อเครื่องมือนี้ถูกใช้ สุดท้ายเราจะเปิดเผย `tool_add` ซึ่งเป็นดิกชันนารีที่เก็บคุณสมบัติเหล่านี้ทั้งหมด

นอกจากนี้ยังมี *schema.py* ที่ใช้สำหรับกำหนดสกีมาของอินพุตที่ใช้โดยเครื่องมือของเรา:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

เรายังต้องเติม *__init__.py* เพื่อให้โฟลเดอร์ tools ถูกมองว่าเป็นโมดูล นอกจากนี้ยังต้องเปิดเผยโมดูลภายในตามนี้:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

เราสามารถเพิ่มไฟล์นี้ตอนเราเพิ่มเครื่องมือมากขึ้น

**TypeScript**

```typescript
import { Tool } from "./tool.js";
import { MathInputSchema } from "./schema.js";
import { zodToJsonSchema } from "zod-to-json-schema";

export default {
    name: "add",
    rawSchema: MathInputSchema,
    inputSchema: zodToJsonSchema(MathInputSchema),
    callback: async ({ a, b }) => {
        return {
            content: [{ type: "text", text: String(a + b) }]
        };
    }
} as Tool;
```

ที่นี่ เราสร้างดิกชันนารีประกอบด้วยคุณสมบัติ:

- name คือชื่อเครื่องมือ
- rawSchema คือสกีมาของ Zod ที่ใช้ตรวจสอบคำขอที่เข้ามาเรียกเครื่องมือนี้
- inputSchema สกีมานี้จะถูกใช้โดยตัวจัดการ
- callback ใช้เพื่อเรียกใช้เครื่องมือ

นอกจากนี้ยังมี `Tool` ที่ใช้แปลงดิกชันนารีนี้เป็นชนิดที่ตัวจัดการเซิร์ฟเวอร์ mcp รับได้ ลักษณะดังนี้:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

และมี *schema.ts* ที่เราเก็บสกีมอินพุตสำหรับแต่ละเครื่องมือ ลักษณะเป็นดังนี้ โดยตอนนี้มีเพียงสกีมเดียวแต่เมื่อตอนเพิ่มเครื่องมือ เราสามารถเพิ่มรายการได้มากขึ้น:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ดีมาก เรามาต่อเรื่องการจัดการการแสดงรายการเครื่องมือกัน

### -3- จัดการการแสดงรายการเครื่องมือ

ต่อมา เพื่อจัดการการแสดงรายการเครื่องมือ เราต้องตั้งค่าตัวจัดการคำขอ สำหรับนี่เราต้องเพิ่มสิ่งนี้ในไฟล์เซิร์ฟเวอร์ของเรา:

**Python**

```python
# โค้ดถูกตัดทอนเพื่อความกระชับ
from tools import tools

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    tool_list = []
    print(tools)

    for tool in tools.values():
        tool_list.append(
            types.Tool(
                name=tool["name"],
                description=tool["description"],
                inputSchema=pydantic_to_json(tool["input_schema"]),
            )
        )
    return tool_list
```

ที่นี่ เราเพิ่มดีคอเรเตอร์ `@server.list_tools` และฟังก์ชัน `handle_list_tools` ที่ทำงานในฟังก์ชันนี้ เราต้องสร้างรายการเครื่องมือ สังเกตว่าแต่ละเครื่องมือต้องมีชื่อ คำอธิบาย และ inputSchema

**TypeScript**

เพื่อสร้างตัวจัดการคำขอสำหรับแสดงรายการเครื่องมือ เราต้องเรียก `setRequestHandler` บนเซิร์ฟเวอร์พร้อมสกีมที่เหมาะสมกับสิ่งที่เราทำ ในกรณีนี้คือ `ListToolsRequestSchema`

```typescript
// index.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// server.ts
// โค้ดถูกละไว้เพื่อความกระชับ
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // ส่งคืนรายการเครื่องมือที่ลงทะเบียนแล้ว
  return {
    tools: tools
  };
});
```

ดี ตอนนี้เราแก้ไขงานการแสดงรายการเครื่องมือแล้ว มาดูวิธีการเรียกเครื่องมือกันต่อ

### -4- จัดการการเรียกเครื่องมือ

เพื่อเรียกเครื่องมือ เราต้องตั้งค่าตัวจัดการคำขออีกตัว โดยเน้นกับคำขอที่ระบุว่าจะเรียกฟีเจอร์ใดและด้วยอาร์กิวเมนต์อะไร

**Python**

ให้ใช้ดีคอเรเตอร์ `@server.call_tool` และนิยามฟังก์ชัน `handle_call_tool` ภายในฟังก์ชันนี้ เราต้องแยกชื่อเครื่องมือ อาร์กิวเมนต์ และตรวจสอบว่าอาร์กิวเมนต์ถูกต้องสำหรับเครื่องมือหรือไม่ เราสามารถตรวจสอบอาร์กิวเมนต์ในฟังก์ชันนี้หรือจะทำในตัวเครื่องมือเลยก็ได้

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools เป็นพจนานุกรมที่มีชื่อเครื่องมือเป็นคีย์
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # เรียกใช้เครื่องมือ
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

นี่คือสิ่งที่เกิดขึ้น:

- ชื่อเครื่องมือของเราอยู่ในพารามิเตอร์เข้าชื่อ `name` และอาร์กิวเมนต์เป็นดิกชันนารี `arguments`

- เครื่องมือถูกเรียกใช้ด้วย `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` การตรวจสอบความถูกต้องของอาร์กิวเมนต์เกิดขึ้นในฟิลด์ `handler` ซึ่งชี้ไปที่ฟังก์ชัน หากล้มเหลวจะเกิดข้อผิดพลาด

ตอนนี้เรามีความเข้าใจเต็มที่เกี่ยวกับการแสดงรายการและการเรียกเครื่องมือโดยใช้เซิร์ฟเวอร์ระดับล่าง

ดู [ตัวอย่างเต็ม](./code/README.md) ได้ที่นี่

## การบ้าน

ขยายโค้ดที่คุณได้รับด้วยเครื่องมือ แหล่งข้อมูล และพรอมต์จำนวนหนึ่ง และสะท้อนว่าคุณสังเกตได้ว่าแค่เพิ่มไฟล์ในโฟลเดอร์ tools เท่านั้น ไม่ต้องเพิ่มที่อื่น

*ไม่มีคำตอบให้*

## สรุป

ในบทนี้ เราได้เห็นว่าวิธีเซิร์ฟเวอร์ระดับล่างทำงานอย่างไรและช่วยสร้างสถาปัตยกรรมที่ดีที่สามารถต่อยอดได้ เราได้พูดถึงการตรวจสอบความถูกต้อง และแสดงวิธีใช้ไลบรารีตรวจสอบเพื่อสร้างสกีมาสำหรับตรวจสอบอินพุต

## ต่อไป

- ถัดไป: [การตรวจสอบสิทธิ์แบบง่าย](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้ถูกแปลโดยใช้บริการแปลภาษาด้วยปัญญาประดิษฐ์ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ผลลัพธ์ที่ถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญสูง ขอแนะนำให้ใช้การแปลโดยผู้เชี่ยวชาญด้านภาษามนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->