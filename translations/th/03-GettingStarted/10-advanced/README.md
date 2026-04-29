# การใช้งานเซิร์ฟเวอร์ขั้นสูง

มีเซิร์ฟเวอร์สองประเภทที่เปิดเผยใน MCP SDK คือ เซิร์ฟเวอร์ปกติและเซิร์ฟเวอร์ระดับต่ำ โดยปกติแล้ว คุณจะใช้เซิร์ฟเวอร์ปกติเพื่อเพิ่มฟีเจอร์ต่างๆ ให้กับมัน แต่ในบางกรณี คุณอาจต้องพึ่งพาเซิร์ฟเวอร์ระดับต่ำ เช่น:

- สถาปัตยกรรมที่ดีกว่า สามารถสร้างสถาปัตยกรรมที่สะอาดทั้งกับเซิร์ฟเวอร์ปกติและเซิร์ฟเวอร์ระดับต่ำได้ แต่ถกเถียงกันได้ว่าง่ายกว่าเล็กน้อยกับเซิร์ฟเวอร์ระดับต่ำ
- ความพร้อมของฟีเจอร์ ฟีเจอร์ขั้นสูงบางอย่างสามารถใช้ได้เฉพาะกับเซิร์ฟเวอร์ระดับต่ำเท่านั้น คุณจะเห็นสิ่งนี้ในบทต่อๆ ไปเมื่อเราเพิ่มการสุ่มตัวอย่างและการดึงข้อมูล

## เซิร์ฟเวอร์ปกติเผชิญกับเซิร์ฟเวอร์ระดับต่ำ

นี่คือตัวอย่างการสร้าง MCP Server ด้วยเซิร์ฟเวอร์ปกติ

**Python**

```python
mcp = FastMCP("Demo")

# เพิ่มเครื่องมือสำหรับบวก
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

// เพิ่มเครื่องมือการบวก
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

ประเด็นคือคุณจะต้องเพิ่มเครื่องมือ ทรัพยากร หรือ prompt ที่คุณต้องการให้เซิร์ฟเวอร์มีอย่างชัดเจน ไม่มีอะไรผิดกับเรื่องนี้

### แนวทางเซิร์ฟเวอร์ระดับต่ำ

อย่างไรก็ตาม เมื่อคุณใช้แนวทางเซิร์ฟเวอร์ระดับต่ำ คุณต้องคิดต่างออกไป แทนที่จะลงทะเบียนเครื่องมือแต่ละตัว คุณจะสร้างตัวจัดการสองตัวต่อประเภทฟีเจอร์ (เครื่องมือ, ทรัพยากร หรือ prompt) เช่น เครื่องมือจะมีแค่สองฟังก์ชั่นดังนี้:

- แสดงรายการเครื่องมือทั้งหมด ฟังก์ชั่นหนึ่งจะรับผิดชอบการพยายามแสดงรายการเครื่องมือทั้งหมด
- จัดการการเรียกใช้เครื่องมือทั้งหมด ที่นี่ก็มีแค่ฟังก์ชั่นเดียวจัดการการเรียกใช้เครื่องมือ

ฟังดูเหมือนงานที่น้อยลงใช่ไหม? แทนที่จะลงทะเบียนเครื่องมือ ฉันแค่ต้องมั่นใจว่าเครื่องมือแสดงเมื่อแสดงรายการเครื่องมือทั้งหมด และเรียกใช้เมื่อมีคำขอเรียกใช้เครื่องมือเข้ามา

ลองดูโค้ดตอนนี้ดูว่าเป็นอย่างไร:

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
  // ส่งคืนรายการเครื่องมือที่ลงทะเบียนแล้ว
  return {
    tools: [{
        name: "add",
        description: "Add two numbers",
        inputSchema: {
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

ตรงนี้เรามีฟังก์ชั่นที่ส่งกลับรายการฟีเจอร์ รายการในเครื่องมือแต่ละตัวมีฟิลด์เช่น `name`, `description` และ `inputSchema` เพื่อให้ตรงกับชนิดส่งกลับ วิธีนี้ช่วยให้เราวางเครื่องมือและการกำหนดฟีเจอร์ไว้ที่อื่นได้ เราสามารถสร้างเครื่องมือทั้งหมดของเราในโฟลเดอร์เครื่องมือ และเช่นเดียวกันกับฟีเจอร์ทั้งหมด โครงการของคุณก็จะถูกจัดระเบียบแบบนี้ได้:

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

เยี่ยมมาก สถาปัตยกรรมของเราจะดูสะอาดขึ้นมาก

แล้วการเรียกใช้เครื่องมือเป็นแนวคิดเดียวกันไหม ใช้ตัวจัดการเดียวเพื่อเรียกเครื่องมือไหนก็ได้? ใช่ ถูกต้อง นี่คือโค้ดตัวอย่าง:

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
    
    // args: request.params.arguments
    // TODO เรียกใช้เครื่องมือ,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

อย่างที่เห็นในโค้ดด้านบน เราต้องแยกเครื่องมือที่จะเรียก และกับอาร์กิวเมนต์อะไร จากนั้นเราต้องดำเนินการเรียกเครื่องมือ

## ปรับปรุงแนวทางด้วยการตรวจสอบข้อมูล

จนถึงตอนนี้ คุณเห็นว่าเราสามารถแทนที่การลงทะเบียนเพื่อเพิ่มเครื่องมือ ทรัพยากร และ prompt ได้ด้วยตัวจัดการสองตัวต่อประเภทฟีเจอร์ แล้วเราต้องทำอะไรอีก? ควรเพิ่มการตรวจสอบข้อมูลบางรูปแบบเพื่อให้แน่ใจว่าเครื่องมือถูกเรียกด้วยอาร์กิวเมนต์ที่ถูกต้อง รันไทม์แต่ละตัวมีวิธีแก้ปัญหาของตัวอย่างเช่น Python ใช้ Pydantic และ TypeScript ใช้ Zod แนวคิดคือเราทำดังนี้:

- ย้ายตรรกะสำหรับการสร้างฟีเจอร์ (เครื่องมือ ทรัพยากร หรือ prompt) ไปยังโฟลเดอร์เฉพาะของฟีเจอร์นั้น
- เพิ่มวิธีการตรวจสอบคำขอที่เข้ามาเช่นการเรียกเครื่องมือ

### สร้างฟีเจอร์

เพื่อสร้างฟีเจอร์ เราต้องสร้างไฟล์สำหรับฟีเจอร์นั้นและต้องมั่นใจว่ามีฟิลด์สำคัญที่ฟีเจอร์ต้องการ ซึ่งฟิลด์จะแตกต่างกันระหว่างเครื่องมือ ทรัพยากร และ prompt เล็กน้อย

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
        # ตรวจสอบความถูกต้องของข้อมูลนำเข้าโดยใช้โมเดล Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: เพิ่ม Pydantic เพื่อให้เราสามารถสร้าง AddInputModel และตรวจสอบความถูกต้องของ args ได้

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ตรงนี้คุณจะเห็นว่าเราทำสิ่งต่อไปนี้:

- สร้าง schema ด้วย Pydantic `AddInputModel` โดยมีฟิลด์ `a` และ `b` ในไฟล์ *schema.py*
- พยายามแปลงคำขอที่เข้ามาเป็นชนิด `AddInputModel` หากพารามิเตอร์ไม่ตรงกันโค้ดนี้จะเกิดข้อผิดพลาด:

   ```python
   # add.py
    try:
        # ตรวจสอบความถูกต้องของข้อมูลนำเข้าด้วยโมเดล Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

คุณสามารถเลือกว่าวางตรรกะแปลงนี้ไว้ในตัวเรียกเครื่องมือเอง หรือในฟังก์ชั่นตัวจัดการ

**TypeScript**

```typescript
// เซิร์ฟเวอร์.ts
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

// สคีมา.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// เพิ่ม.ts
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

- ในตัวจัดการที่จัดการการเรียกเครื่องมือทั้งหมด ตอนนี้เราพยายามแปลงคำขอที่เข้ามาเป็น schema ที่เครื่องมือกำหนด:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    หากสำเร็จ เราจะดำเนินการเรียกเครื่องมือจริง:

    ```typescript
    const result = await tool.callback(input);
    ```

อย่างที่เห็น แนวทางนี้สร้างสถาปัตยกรรมที่ดีเพราะทุกอย่างมีที่ของมัน *server.ts* เป็นไฟล์เล็กๆ ที่เชื่อมตัวจัดการคำขอ ส่วนฟีเจอร์แต่ละอย่างอยู่ในโฟลเดอร์ของตัวเอง เช่น tools/, resources/ หรือ /prompts

เยี่ยมมาก ลองสร้างสิ่งนี้กันต่อไป

## แบบฝึกหัด: สร้างเซิร์ฟเวอร์ระดับต่ำ

ในการฝึกนี้ เราจะทำสิ่งต่อไปนี้:

1. สร้างเซิร์ฟเวอร์ระดับต่ำจัดการการแสดงรายการเครื่องมือและการเรียกใช้เครื่องมือ
2. สร้างสถาปัตยกรรมที่คุณสามารถต่อยอดได้
3. เพิ่มการตรวจสอบเพื่อให้แน่ใจว่าการเรียกใช้เครื่องมือของคุณถูกต้อง

### -1- สร้างสถาปัตยกรรม

สิ่งแรกที่เราต้องทำคือสถาปัตยกรรมที่ช่วยให้เราสามารถขยายได้เมื่อเพิ่มฟีเจอร์ นี่คือลักษณะ:

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

ตอนนี้เราตั้งค่าสถาปัตยกรรมให้สามารถเพิ่มเครื่องมือใหม่ในโฟลเดอร์ tools ได้อย่างง่ายดาย คุณสามารถเพิ่มโฟลเดอร์ย่อยสำหรับ resources และ prompts ตามต้องการ

### -2- สร้างเครื่องมือ

มาดูว่าการสร้างเครื่องมือเป็นอย่างไร ก่อนอื่นต้องสร้างในโฟลเดอร์ *tool* ของตัวอย่างนั้นดังนี้:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ตรวจสอบข้อมูลนำเข้าด้วยโมเดล Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: เพิ่ม Pydantic เพื่อที่เราจะสามารถสร้าง AddInputModel และตรวจสอบ args ได้

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ที่นี่เราเห็นวิธีการกำหนดชื่อ รายละเอียด และ input schema โดยใช้ Pydantic และตัวจัดการที่จะถูกเรียกใช้เมื่อเครื่องมือนี้ถูกเรียก สุดท้าย เราเปิดเผย `tool_add` ซึ่งเป็นพจนานุกรมที่เก็บคุณสมบัติเหล่านี้ทั้งหมด

มีไฟล์ *schema.py* ที่ใช้กำหนด input schema สำหรับเครื่องมือของเรา:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

เรายังต้องเติม *__init__.py* ให้โฟลเดอร์ tools ถูกมองเป็นโมดูล และเปิดเผยโมดูลภายในดังนี้:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

เราสามารถเพิ่มเข้าไปในไฟล์นี้ได้เรื่อยๆ เมื่อเพิ่มเครื่องมือ

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

เราสร้างพจนานุกรมที่มีคุณสมบัติ:

- name คือชื่อเครื่องมือ
- rawSchema คือ schema ของ Zod ใช้ตรวจสอบคำขอที่เข้ามาเพื่อเรียกเครื่องมือนี้
- inputSchema schema นี้ใช้โดยตัวจัดการ
- callback ใช้เรียกเครื่องมือ

ยังมี `Tool` ที่ใช้แปลงพจนานุกรมนี้เป็นชนิดที่ตัวจัดการ mcp server รับได้ และหน้าตาดังนี้:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

และไฟล์ *schema.ts* ที่เก็บ input schemas ของแต่ละเครื่องมือที่มีลักษณะตรงนี้ ปัจจุบันมี schema เดียว แต่เมื่อเพิ่มเครื่องมือก็เพิ่มรายการได้:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ดีมาก ลองดำเนินการต่อเพื่อจัดการการแสดงรายการของเรา

### -3- จัดการการแสดงรายการเครื่องมือ

จากนั้น เพื่อจัดการการแสดงรายการเครื่องมือ เราต้องตั้งค่าตัวจัดการคำขอสำหรับส่วนนี้ นี่คือสิ่งที่ต้องเพิ่มในไฟล์เซิร์ฟเวอร์ของเรา:

**Python**

```python
# โค้ดถูกตัดออกเพื่อความกระชับ
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

ที่นี่ เราเพิ่มตัวตกแต่ง `@server.list_tools` และฟังก์ชั่น `handle_list_tools` ซึ่งในนั้นเราต้องสร้างรายการเครื่องมือ สังเกตว่าแต่ละเครื่องมือจะต้องมีชื่อ คำอธิบาย และ inputSchema

**TypeScript**

เพื่อกำหนดตัวจัดการคำขอสำหรับการแสดงรายการเครื่องมือ เราต้องเรียกใช้ `setRequestHandler` บนเซิร์ฟเวอร์พร้อม schema ที่เหมาะสมกับสิ่งที่เราต้องการทำ ซึ่งในกรณีนี้คือ `ListToolsRequestSchema`

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

เยี่ยม ตอนนี้เราจัดการเรื่องแสดงรายการเครื่องมือแล้ว มาดูว่าการเรียกใช้เครื่องมือจะทำอย่างไรต่อ

### -4- จัดการการเรียกใช้เครื่องมือ

เพื่อเรียกใช้เครื่องมือ เราต้องตั้งค่าตัวจัดการคำขออีกตัวที่เน้นจัดการคำขอที่ระบุว่าฟีเจอร์ที่จะเรียกใช้อะไร และกับอาร์กิวเมนต์ใด

**Python**

มาใช้ตัวตกแต่ง `@server.call_tool` และใช้งานด้วยฟังก์ชั่น `handle_call_tool` ภายในฟังก์ชั่นนี้ เราต้องแยกชื่อเครื่องมือ อาร์กิวเมนต์ และตรวจสอบให้อาร์กิวเมนต์ถูกต้องสำหรับเครื่องมือที่ระบุ เราสามารถตรวจสอบอาร์กิวเมนต์ในฟังก์ชั่นนี้หรือในเครื่องมือจริงๆ ด้านล่าง

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools เป็นพจนานุกรมที่มีชื่อเครื่องมือเป็นกุญแจ
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

สิ่งที่เกิดขึ้นคือ:

- ชื่อเครื่องมืออยู่ในตัวแปร input `name` แล้ว ซึ่งจะถูกใช้กับอาร์กิวเมนต์ในพจนานุกรม `arguments`

- เครื่องมือถูกเรียกด้วย `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` การตรวจสอบความถูกต้องของอาร์กิวเมนต์เกิดขึ้นในคุณสมบัติ `handler` ที่ชี้ไปยังฟังก์ชั่น หากล้มเหลวจะเกิดข้อยกเว้น

ตอนนี้เราเข้าใจครบถ้วนเรื่องการแสดงรายการและเรียกใช้เครื่องมือด้วยเซิร์ฟเวอร์ระดับต่ำ

ดู [ตัวอย่างเต็ม](./code/README.md) ได้ที่นี่

## งานมอบหมาย

ขยายโค้ดที่ได้รับด้วยเครื่องมือ ทรัพยากร และ prompt หลายตัว และลองพิจารณาดูว่าคุณจะต้องเพิ่มไฟล์ได้เพียงในไดเรกทอรี tools เท่านั้นและไม่มีที่อื่น

*ไม่มีการให้คำตอบ*

## สรุป

ในบทนี้ เราเห็นว่าแนวทางเซิร์ฟเวอร์ระดับต่ำทำงานอย่างไรและช่วยสร้างสถาปัตยกรรมที่ดีที่เราสามารถเพิ่มต่อได้อย่างไร นอกจากนี้ยังพูดถึงการตรวจสอบข้อมูล และคุณได้รับการแนะนำวิธีการใช้ไลบรารีตรวจสอบเพื่อสร้าง schema สำหรับตรวจสอบข้อมูลนำเข้า

## ต่อไปคืออะไร

- ถัดไป: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**คำปฏิเสธความรับผิดชอบ**:  
เอกสารนี้ได้ถูกแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรืความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยผู้เชี่ยวชาญที่เป็นมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->