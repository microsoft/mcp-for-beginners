# การใช้งานเซิร์ฟเวอร์ขั้นสูง

มีเซิร์ฟเวอร์สองประเภทที่เปิดเผยใน MCP SDK คือ เซิร์ฟเวอร์ปกติและเซิร์ฟเวอร์ระดับต่ำ โดยปกติคุณจะใช้เซิร์ฟเวอร์ปกติเพื่อเพิ่มฟีเจอร์ต่าง ๆ แต่ในบางกรณี คุณอาจต้องพึ่งพาเซิร์ฟเวอร์ระดับต่ำ เช่น:

- สถาปัตยกรรมที่ดีขึ้น เป็นไปได้ที่จะสร้างสถาปัตยกรรมที่สะอาดทั้งกับเซิร์ฟเวอร์ปกติและเซิร์ฟเวอร์ระดับต่ำ แต่สามารถโต้แย้งได้ว่าสะดวกกว่าเล็กน้อยในเซิร์ฟเวอร์ระดับต่ำ
- ความพร้อมใช้งานของฟีเจอร์ บางฟีเจอร์ขั้นสูงสามารถใช้ได้เฉพาะกับ
    เซิร์ฟเวอร์ระดับต่ำ บทต่อไปจะครอบคลุมการดึงข้อมูลและฟีเจอร์การสุ่มตัวอย่างแบบเก่า
    ซึ่งเลิกใช้ใน MCP `2026-07-28`

## เซิร์ฟเวอร์ปกติกับเซิร์ฟเวอร์ระดับต่ำ

นี่คือวิธีการสร้าง MCP Server ด้วยเซิร์ฟเวอร์ปกติ

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

ประเด็นคือคุณต้องเพิ่มเครื่องมือ, แหล่งข้อมูล หรือพรอมต์ทีละรายการที่คุณต้องการให้เซิร์ฟเวอร์มี ไม่มีอะไรผิดกับวิธีนี้  

### วิธีเซิร์ฟเวอร์ระดับต่ำ

อย่างไรก็ตาม เมื่อใช้วิธีเซิร์ฟเวอร์ระดับต่ำ คุณต้องคิดแตกต่าง แทนที่จะลงทะเบียนเครื่องมือแต่ละชิ้น คุณสร้างตัวจัดการสองตัวต่อแต่ละประเภทของฟีเจอร์ (เครื่องมือ, แหล่งข้อมูล หรือพรอมต์) เช่น เครื่องมือจะมีเพียงสองฟังก์ชันแบบนี้:

- การแสดงรายการเครื่องมือทั้งหมด ฟังก์ชันหนึ่งจะรับผิดชอบการแสดงรายการเครื่องมือทั้งหมด
- การจัดการการเรียกเครื่องมือ ที่นี่ก็มีเพียงฟังก์ชันเดียวจัดการการเรียกใช้งานเครื่องมือ

ฟังดูน่าจะงานน้อยกว่าใช่ไหม? แทนที่จะลงทะเบียนเครื่องมือฉันแค่ต้องแน่ใจว่าเครื่องมือถูกแสดงรายการเวลาฉันแสดงรายการเครื่องมือทั้งหมด และมันถูกเรียกตอนมีคำขอเรียกเครื่องมือเข้ามา

มาดูว่าตอนนี้โค้ดเป็นอย่างไร:

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

ตอนนี้เรามีฟังก์ชันที่คืนรายการฟีเจอร์ รายการใน tools แต่ละรายการมีฟิลด์อย่าง `name`, `description` และ `inputSchema` เพื่อให้สอดคล้องกับชนิดข้อมูลที่คืน นี่ช่วยให้เราวางเครื่องมือและนิยามฟีเจอร์ได้ที่อื่นได้ เราสามารถสร้างเครื่องมือทั้งหมดในโฟลเดอร์ tools และทำเช่นเดียวกันสำหรับฟีเจอร์ทั้งหมดของคุณ ทำให้โครงการของคุณถูกจัดระเบียบแบบนี้ได้:

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

ยอดเยี่ยม สถาปัตยกรรมของเราดูสะอาดขึ้นมาก

แล้วสำหรับการเรียกใช้เครื่องมือ ไอเดียเดียวกันใช่ไหม ตัวจัดการตัวเดียวสำหรับเรียกเครื่องมือใดก็ได้? ใช่เลย นี่คือโค้ดสำหรับตรงนั้น:

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

จากโค้ดด้านบน เราต้องแยกเครื่องมือที่จะเรียกและอาร์กิวเมนต์ที่ใช้ แล้วจึงดำเนินการเรียกใช้งานเครื่องมือ

## การปรับปรุงวิธีการด้วยการตรวจสอบความถูกต้อง

จนถึงตอนนี้ คุณเห็นว่าการลงทะเบียนเพื่อเพิ่มเครื่องมือ แหล่งข้อมูล และพรอมต์ทั้งหมดสามารถแทนที่ด้วยตัวจัดการสองตัวต่อแต่ละประเภทฟีเจอร์ได้ เราต้องทำอะไรต่อ? เราควรเพิ่มการตรวจสอบความถูกต้องเพื่อให้แน่ใจว่าเครื่องมือถูกเรียกด้วยอาร์กิวเมนต์ที่ถูกต้อง ในแต่ละ runtime ก็จะมีโซลูชันของตัวเอง เช่น Python ใช้ Pydantic และ TypeScript ใช้ Zod โดยแนวคิดคือเราทำตามนี้:

- ย้ายตรรกะการสร้างฟีเจอร์ (เครื่องมือ, แหล่งข้อมูล หรือพรอมต์) ไปยังโฟลเดอร์เฉพาะของมัน
- เพิ่มวิธีการตรวจสอบคำขอที่เข้ามาเช่นการเรียกใช้เครื่องมือ

### สร้างฟีเจอร์

เพื่อสร้างฟีเจอร์ เราต้องสร้างไฟล์สำหรับฟีเจอร์นั้นและให้แน่ใจว่ามีฟิลด์บังคับที่จำเป็นของฟีเจอร์นั้น ซึ่งฟิลด์จะแตกต่างกันเล็กน้อยระหว่างเครื่องมือ, แหล่งข้อมูล และพรอมต์

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

ที่นี่คุณเห็นว่าเราทำตามนี้:

- สร้าง schema โดยใช้ Pydantic `AddInputModel` มีฟิลด์ `a` และ `b` ในไฟล์ *schema.py*
- พยายามแปลงคำขอที่เข้ามาเป็นชนิด `AddInputModel` ถ้าอาร์กิวเมนต์ไม่ตรงกันโค้ดนี้จะล้มเหลว:

   ```python
   # add.py
    try:
        # ตรวจสอบความถูกต้องของข้อมูลเข้าโดยใช้โมเดล Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

คุณสามารถเลือกว่าจะใส่ตรรกะการแปลงนี้ในตัวเรียกเครื่องมือเองหรือในฟังก์ชันตัวจัดการ

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

- ในตัวจัดการที่จัดการการเรียกเครื่องมือทั้งหมด เราพยายามแปลงคำขอที่เข้ามาเป็น schema ของเครื่องมือ:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ถ้าสำเร็จเราก็เรียกเครื่องมือจริง:

    ```typescript
    const result = await tool.callback(input);
    ```

ดังที่คุณเห็น วิธีนี้สร้างสถาปัตยกรรมที่ดีเพราะทุกอย่างมีที่ของมัน บน *server.ts* เป็นไฟล์เล็ก ๆ ที่เชื่อมโยงตัวจัดการคำขอและแต่ละฟีเจอร์อยู่ในโฟลเดอร์ของตัวมันเอง เช่น tools/, resources/ หรือ /prompts

เยี่ยม เรามาลองสร้างนี้ดูต่อไป

## แบบฝึกหัด: สร้างเซิร์ฟเวอร์ระดับต่ำ

ในแบบฝึกหัดนี้ เราจะทำดังนี้:

1. สร้างเซิร์ฟเวอร์ระดับต่ำที่จัดการการแสดงรายการเครื่องมือและการเรียกเครื่องมือ
1. นำสถาปัตยกรรมที่คุณสร้างได้ไปใช้
1. เพิ่มการตรวจสอบความถูกต้องเพื่อให้แน่ใจว่าการเรียกเครื่องมือถูกตรวจสอบอย่างเหมาะสม

### -1- สร้างสถาปัตยกรรม

สิ่งแรกที่เราต้องแก้ไขคือสถาปัตยกรรมที่ช่วยให้เราขยายระบบได้เมื่อเพิ่มฟีเจอร์ นี่คือลักษณะ:

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

ตอนนี้เราตั้งค่าสถาปัตยกรรมที่ทำให้เพิ่มเครื่องมือใหม่ในโฟลเดอร์ tools ได้ง่าย คุณสามารถเพิ่มไดเรกทอรีย่อยสำหรับ resources และ prompts ได้ตามต้องการ

### -2- สร้างเครื่องมือ

มาดูการสร้างเครื่องมือกันก่อน ต้องสร้างในไดเรกทอรีย่อย *tool* ดังนี้:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ตรวจสอบข้อมูลเข้าโดยใช้โมเดล Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: เพิ่ม Pydantic เพื่อที่เราจะสามารถสร้าง AddInputModel และตรวจสอบความถูกต้องของ args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

สิ่งที่เห็นคือการนิยามชื่อ, คำอธิบาย และ schema การป้อนข้อมูลด้วย Pydantic และตัวจัดการที่ถูกเรียกเมื่อตัวเครื่องมือนี้ถูกเรียก ท้ายสุดเราก็เปิดเผย `tool_add` ซึ่งเป็นดิกชันนารีเก็บคุณสมบัติเหล่านี้ทั้งหมด

ยังมี *schema.py* ที่ใช้กำหนด schema การป้อนข้อมูลที่เครื่องมือของเราใช้:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

เรายังต้องเติม *__init__.py* เพื่อให้ไดเรกทอ tools ถูกมองว่าเป็นโมดูลด้วย นอกจากนี้ต้องเปิดเผยโมดูลภายในนี้ด้วย เช่นนี้:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

เราสามารถเพิ่มไฟล์นี้ได้เรื่อย ๆ เมื่อเพิ่มเครื่องมือใหม่

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

ที่นี่เราสร้างดิกชันนารีประกอบด้วยคุณสมบัติ:

- name ชื่อของเครื่องมือ
- rawSchema คือ schema ของ Zod ที่ใช้ตรวจสอบคำขอเรียกใช้เครื่องมือนี้
- inputSchema schema นี้ใช้ในตัวจัดการ
- callback ใช้ในการเรียกเครื่องมือ

ยังมี `Tool` ที่ใช้แปลงดิกชันนารีนี้เป็นชนิดที่ตัวจัดการเซิร์ฟเวอร์ mcp รับได้ ซึ่งดูแบบนี้:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

และมี *schema.ts* ซึ่งเก็บ schema การป้อนข้อมูลของเครื่องมือแต่ละตัว ดูประมาณนี้และตอนนี้มี schema เดียว แต่ถ้าเพิ่มเครื่องมือก็เพิ่มรายการได้:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

เยี่ยม เรายังไปจัดการรายการเครื่องมือกันต่อ

### -3- จัดการการแสดงรายการเครื่องมือ

ต่อไป สำหรับการจัดการแสดงรายการเครื่องมือ เราต้องตั้งค่าตัวจัดการคำขอ นี่คือสิ่งที่ต้องเพิ่มในไฟล์เซิร์ฟเวอร์:

**Python**

```python
# โค้ดถูกตัดออกเพื่อความสั้นกระชับ
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

ที่นี่เราเพิ่มเดคอเรเตอร์ `@server.list_tools` และฟังก์ชัน `handle_list_tools` ในนั้นเราต้องสร้างรายการเครื่องมือ สังเกตว่าแต่ละเครื่องมือจำเป็นต้องมีชื่อ, คำอธิบาย และ inputSchema  

**TypeScript**

การตั้งค่าตัวจัดการคำขอแสดงรายการเครื่องมือ เราต้องเรียก `setRequestHandler` ในเซิร์ฟเวอร์โดยใช้ schema ที่เหมาะสมกับสิ่งที่พยายามทำ ในกรณีนี้คือ `ListToolsRequestSchema`

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
// โค้ดถูกตัดเพื่อความกระชับ
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // ส่งคืนรายการเครื่องมือที่ลงทะเบียนแล้ว
  return {
    tools: tools
  };
});
```

เยี่ยม ตอนนี้แก้ปัญหาส่วนการแสดงรายการเครื่องมือแล้ว มาดูต่อว่าการเรียกเครื่องมือจะทำอย่างไร

### -4- จัดการการเรียกเครื่องมือ

ในการเรียกเครื่องมือ เราต้องตั้งค่าตัวจัดการคำขออีกตัว คราวนี้เน้นจัดการคำขอที่ระบุฟีเจอร์และอาร์กิวเมนต์ที่จะใช้เรียก

**Python**

ใช้เดคอเรเตอร์ `@server.call_tool` และเขียนฟังก์ชัน `handle_call_tool` ในฟังก์ชันนี้ เราต้องแยกชื่อเครื่องมือ อาร์กิวเมนต์ แล้วตรวจสอบความถูกต้องของอาร์กิวเมนต์สำหรับเครื่องมือที่ระบุ เราสามารถตรวจสอบความถูกต้องในฟังก์ชันนี้หรือในเครื่องมือเองก็ได้

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
        # เรียกใช้งานเครื่องมือ
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

สิ่งที่เกิดขึ้นคือ:

- ชื่อเครื่องมือมีอยู่แล้วในพารามิเตอร์ป้อนข้อมูล `name` และอาร์กิวเมนต์อยู่ในดิกชันนารี `arguments`

- เครื่องมือถูกเรียกด้วย `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` การตรวจสอบความถูกต้องของอาร์กิวเมนต์เกิดขึ้นในคุณสมบัติ `handler` ซึ่งชี้ไปที่ฟังก์ชัน ถ้าล้มเหลวจะเกิดข้อยกเว้น

นี่คือความเข้าใจครบถ้วนเกี่ยวกับการแสดงรายการและการเรียกใช้เครื่องมือโดยใช้เซิร์ฟเวอร์ระดับต่ำ

ดู [ตัวอย่างเต็ม](./code/README.md) ที่นี่

## งานมอบหมาย

ขยายโค้ดที่ได้รับด้วยเครื่องมือ แหล่งข้อมูล และพรอมต์จำนวนหนึ่ง และสะท้อนการสังเกตว่าคุณแค่ต้องเพิ่มไฟล์ในไดเรกทอ tools เท่านั้น ไม่ต้องเพิ่มที่อื่น

*ไม่มีคำตอบให้*

## สรุป

ในบทนี้ เราได้เห็นวิธีเซิร์ฟเวอร์ระดับต่ำทำงานอย่างไรและวิธีที่ช่วยให้เราสร้างสถาปัตยกรรมที่ดีที่ต่อยอดได้ นอกจากนี้เรายังพูดถึงการตรวจสอบความถูกต้องและแสดงวิธีใช้ไลบรารีตรวจสอบความถูกต้องเพื่อสร้าง schema สำหรับการตรวจสอบข้อมูลนำเข้า

## ต่อไปคืออะไร

- ต่อไป: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->