# การใช้งานเซิร์ฟเวอร์ขั้นสูง

ใน MCP SDK มีเซิร์ฟเวอร์สองประเภทที่เปิดให้ใช้งาน คือ เซิร์ฟเวอร์ปกติและเซิร์ฟเวอร์ระดับต่ำ โดยปกติคุณจะใช้เซิร์ฟเวอร์ปกติเพื่อเพิ่มฟีเจอร์ต่างๆ แต่ในบางกรณี คุณอาจต้องใช้เซิร์ฟเวอร์ระดับต่ำ เช่น:

- สถาปัตยกรรมที่ดีกว่า เป็นไปได้ที่จะสร้างสถาปัตยกรรมที่สะอาดด้วยเซิร์ฟเวอร์ปกติและเซิร์ฟเวอร์ระดับต่ำ แต่สามารถกล่าวได้ว่าเซิร์ฟเวอร์ระดับต่ำอาจทำให้การสร้างง่ายขึ้นเล็กน้อย
- ความพร้อมใช้งานของฟีเจอร์ ฟีเจอร์ขั้นสูงบางอย่างสามารถใช้งานได้เฉพาะกับเซิร์ฟเวอร์ระดับต่ำ คุณจะเห็นสิ่งนี้ในบทต่อๆ ไปเมื่อเราเพิ่มการสุ่มตัวอย่างและการกระตุ้น

## เซิร์ฟเวอร์ปกติ vs เซิร์ฟเวอร์ระดับต่ำ

นี่คือลักษณะการสร้าง MCP Server ด้วยเซิร์ฟเวอร์ปกติ

**Python**

```python
mcp = FastMCP("Demo")

# Add an addition tool
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

// Add an addition tool
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

จุดสำคัญคือคุณต้องเพิ่มเครื่องมือ ทรัพยากร หรือคำสั่งที่คุณต้องการให้เซิร์ฟเวอร์มีอย่างชัดเจน ซึ่งไม่มีอะไรผิดปกติในวิธีนี้  

### วิธีการใช้เซิร์ฟเวอร์ระดับต่ำ

อย่างไรก็ตาม เมื่อคุณใช้วิธีการเซิร์ฟเวอร์ระดับต่ำ คุณต้องคิดในมุมมองที่แตกต่างออกไป โดยแทนที่จะลงทะเบียนเครื่องมือแต่ละตัว คุณจะสร้างตัวจัดการสองตัวต่อประเภทฟีเจอร์ (เครื่องมือ ทรัพยากร หรือคำสั่ง) ตัวอย่างเช่น เครื่องมือจะมีเพียงสองฟังก์ชันดังนี้:

- การแสดงรายการเครื่องมือทั้งหมด ฟังก์ชันหนึ่งจะรับผิดชอบการแสดงรายการเครื่องมือทั้งหมด
- การจัดการการเรียกใช้เครื่องมือทั้งหมด ที่นี่ก็มีเพียงฟังก์ชันเดียวที่จัดการการเรียกใช้เครื่องมือ

ฟังดูเหมือนงานน้อยลงใช่ไหม? ดังนั้นแทนที่จะลงทะเบียนเครื่องมือ คุณเพียงแค่ต้องตรวจสอบให้แน่ใจว่าเครื่องมือถูกแสดงในรายการเมื่อคุณแสดงรายการเครื่องมือทั้งหมด และถูกเรียกใช้เมื่อมีคำขอเข้ามาเพื่อเรียกใช้เครื่องมือ

ลองดูว่ารหัสตอนนี้มีลักษณะอย่างไร:

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
                    "a": {"type": "number", "description": "nubmer to add"}, 
                    "b": {"type": "number", "description": "nubmer to add"}
                },
                "required": ["query"],
            },
        )
    ]
```

**TypeScript**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return the list of registered tools
  return {
    tools: [{
        name="add",
        description="Add two numbers",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "nubmer to add"}, 
                "b": {"type": "number", "description": "nubmer to add"}
            },
            "required": ["query"],
        }
    }]
  };
});
```

ที่นี่เรามีฟังก์ชันที่คืนค่ารายการฟีเจอร์ แต่ละรายการในรายการเครื่องมือมีฟิลด์เช่น `name`, `description` และ `inputSchema` เพื่อให้สอดคล้องกับประเภทการคืนค่า สิ่งนี้ช่วยให้เราสามารถกำหนดเครื่องมือและฟีเจอร์ไว้ที่อื่นได้ เราสามารถสร้างเครื่องมือทั้งหมดในโฟลเดอร์เครื่องมือ และทำเช่นเดียวกันกับฟีเจอร์ทั้งหมด ดังนั้นโครงงานของคุณสามารถจัดระเบียบได้ดังนี้:

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

ยอดเยี่ยม สถาปัตยกรรมของเราสามารถทำให้ดูสะอาดมากขึ้น

แล้วการเรียกใช้เครื่องมือล่ะ? เป็นแนวคิดเดียวกันใช่ไหม ตัวจัดการหนึ่งตัวสำหรับการเรียกใช้เครื่องมือใดๆ? ใช่ ถูกต้อง นี่คือรหัสสำหรับสิ่งนั้น:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is a dictionary with tool names as keys
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
    // TODO call the tool, 

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

จากรหัสด้านบน คุณจะเห็นว่าเราต้องแยกเครื่องมือที่จะเรียกใช้ และอาร์กิวเมนต์ที่จะใช้ จากนั้นเราต้องดำเนินการเรียกใช้เครื่องมือ

## ปรับปรุงวิธีการด้วยการตรวจสอบความถูกต้อง

จนถึงตอนนี้ คุณได้เห็นว่าการลงทะเบียนทั้งหมดของคุณเพื่อเพิ่มเครื่องมือ ทรัพยากร และคำสั่งสามารถถูกแทนที่ด้วยตัวจัดการสองตัวต่อประเภทฟีเจอร์ แล้วเราต้องทำอะไรอีก? เราควรเพิ่มรูปแบบการตรวจสอบความถูกต้องเพื่อให้แน่ใจว่าเครื่องมือถูกเรียกใช้ด้วยอาร์กิวเมนต์ที่ถูกต้อง แต่ละ runtime มีโซลูชันของตัวเองสำหรับสิ่งนี้ เช่น Python ใช้ Pydantic และ TypeScript ใช้ Zod แนวคิดคือเราทำดังนี้:

- ย้ายตรรกะสำหรับการสร้างฟีเจอร์ (เครื่องมือ ทรัพยากร หรือคำสั่ง) ไปยังโฟลเดอร์เฉพาะของมัน
- เพิ่มวิธีการตรวจสอบคำขอที่เข้ามา เช่น การเรียกใช้เครื่องมือ

### สร้างฟีเจอร์

ในการสร้างฟีเจอร์ เราจะต้องสร้างไฟล์สำหรับฟีเจอร์นั้นและตรวจสอบให้แน่ใจว่ามีฟิลด์ที่จำเป็นสำหรับฟีเจอร์นั้น ฟิลด์ที่จำเป็นจะแตกต่างกันเล็กน้อยระหว่างเครื่องมือ ทรัพยากร และคำสั่ง

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
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we can create an AddInputModel and validate args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ที่นี่คุณจะเห็นว่าเราทำดังนี้:

- สร้าง schema โดยใช้ Pydantic `AddInputModel` พร้อมฟิลด์ `a` และ `b` ในไฟล์ *schema.py*
- พยายามแปลงคำขอที่เข้ามาให้เป็นประเภท `AddInputModel` หากมีความไม่ตรงกันในพารามิเตอร์จะเกิดข้อผิดพลาด:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

คุณสามารถเลือกว่าจะใส่ตรรกะการแปลงนี้ในตัวเรียกใช้เครื่องมือเองหรือในฟังก์ชันตัวจัดการ

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

- ในตัวจัดการที่จัดการการเรียกใช้เครื่องมือทั้งหมด เราจะพยายามแปลงคำขอที่เข้ามาให้เป็น schema ที่กำหนดไว้ของเครื่องมือ:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    หากสำเร็จ เราจะดำเนินการเรียกใช้เครื่องมือจริง:

    ```typescript
    const result = await tool.callback(input);
    ```

จากที่เห็น วิธีนี้สร้างสถาปัตยกรรมที่ยอดเยี่ยม เนื่องจากทุกอย่างมีที่ของมัน *server.ts* เป็นไฟล์ขนาดเล็กที่เพียงแค่เชื่อมต่อกับตัวจัดการคำขอ และแต่ละฟีเจอร์อยู่ในโฟลเดอร์ของมัน เช่น tools/, resources/ หรือ /prompts

ยอดเยี่ยม ลองสร้างสิ่งนี้กันต่อไป

## แบบฝึกหัด: สร้างเซิร์ฟเวอร์ระดับต่ำ

ในแบบฝึกหัดนี้ เราจะทำดังนี้:

1. สร้างเซิร์ฟเวอร์ระดับต่ำที่จัดการการแสดงรายการเครื่องมือและการเรียกใช้เครื่องมือ
1. ใช้สถาปัตยกรรมที่คุณสามารถสร้างต่อได้
1. เพิ่มการตรวจสอบความถูกต้องเพื่อให้แน่ใจว่าการเรียกใช้เครื่องมือของคุณได้รับการตรวจสอบอย่างเหมาะสม

### -1- สร้างสถาปัตยกรรม

สิ่งแรกที่เราต้องจัดการคือสถาปัตยกรรมที่ช่วยให้เราขยายได้เมื่อเพิ่มฟีเจอร์ นี่คือลักษณะของมัน:

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

ตอนนี้เราได้ตั้งค่าสถาปัตยกรรมที่ช่วยให้เราสามารถเพิ่มเครื่องมือใหม่ในโฟลเดอร์เครื่องมือได้อย่างง่ายดาย คุณสามารถเพิ่มไดเรกทอรีย่อยสำหรับทรัพยากรและคำสั่งได้ตามต้องการ

### -2- สร้างเครื่องมือ

มาดูกันว่าการสร้างเครื่องมือมีลักษณะอย่างไรต่อไป ก่อนอื่นต้องสร้างในไดเรกทอรีย่อย *tool* ดังนี้:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we can create an AddInputModel and validate args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

สิ่งที่เราเห็นคือการกำหนดชื่อ คำอธิบาย schema อินพุตโดยใช้ Pydantic และตัวจัดการที่จะถูกเรียกใช้เมื่อเครื่องมือนี้ถูกเรียกใช้ สุดท้าย เราเปิดเผย `tool_add` ซึ่งเป็น dictionary ที่มีคุณสมบัติทั้งหมดนี้

นอกจากนี้ยังมี *schema.py* ที่ใช้กำหนด schema อินพุตที่ใช้โดยเครื่องมือของเรา:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

เรายังต้องเติม *__init__.py* เพื่อให้แน่ใจว่าไดเรกทอรีเครื่องมือถูกปฏิบัติเป็นโมดูล นอกจากนี้เราต้องเปิดเผยโมดูลภายในดังนี้:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

เราสามารถเพิ่มไฟล์นี้ได้เมื่อเพิ่มเครื่องมือใหม่

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

ที่นี่เราสร้าง dictionary ที่ประกอบด้วยคุณสมบัติ:

- name, ชื่อของเครื่องมือ
- rawSchema, schema Zod ที่จะใช้ตรวจสอบคำขอที่เข้ามาเพื่อเรียกใช้เครื่องมือนี้
- inputSchema, schema นี้จะใช้โดยตัวจัดการ
- callback, ใช้เรียกใช้เครื่องมือ

นอกจากนี้ยังมี `Tool` ที่ใช้แปลง dictionary นี้เป็นประเภทที่ตัวจัดการเซิร์ฟเวอร์ MCP สามารถยอมรับได้ และมีลักษณะดังนี้:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

และมี *schema.ts* ที่เราเก็บ schema อินพุตสำหรับแต่ละเครื่องมือ ซึ่งมีลักษณะดังนี้ โดยมีเพียง schema เดียวในปัจจุบัน แต่เมื่อเราเพิ่มเครื่องมือ เราสามารถเพิ่มรายการเพิ่มเติมได้:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ยอดเยี่ยม ลองดำเนินการจัดการการแสดงรายการเครื่องมือกันต่อไป

### -3- จัดการการแสดงรายการเครื่องมือ

ต่อไป เพื่อจัดการการแสดงรายการเครื่องมือ เราต้องตั้งค่าตัวจัดการคำขอสำหรับสิ่งนั้น นี่คือสิ่งที่เราต้องเพิ่มในไฟล์เซิร์ฟเวอร์ของเรา:

**Python**

```python
# code omitted for brevity
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

ที่นี่เราเพิ่ม decorator `@server.list_tools` และฟังก์ชันที่ใช้ `handle_list_tools` ในฟังก์ชันหลัง เราต้องสร้างรายการเครื่องมือ สังเกตว่าแต่ละเครื่องมือต้องมีชื่อ คำอธิบาย และ inputSchema   

**TypeScript**

ในการตั้งค่าตัวจัดการคำขอสำหรับการแสดงรายการเครื่องมือ เราต้องเรียก `setRequestHandler` บนเซิร์ฟเวอร์พร้อม schema ที่เหมาะสมกับสิ่งที่เรากำลังทำ ในกรณีนี้คือ `ListToolsRequestSchema` 

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
// code omitted for brevity
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return the list of registered tools
  return {
    tools: tools
  };
});
```

ยอดเยี่ยม ตอนนี้เราได้แก้ไขส่วนการแสดงรายการเครื่องมือแล้ว ลองดูว่าการเรียกใช้เครื่องมือมีลักษณะอย่างไรต่อไป

### -4- จัดการการเรียกใช้เครื่องมือ

ในการเรียกใช้เครื่องมือ เราต้องตั้งค่าตัวจัดการคำขออีกตัวหนึ่ง คราวนี้เน้นที่การจัดการคำขอที่ระบุว่าต้องการเรียกใช้ฟีเจอร์ใดและด้วยอาร์กิวเมนต์ใด

**Python**

ลองใช้ decorator `@server.call_tool` และนำไปใช้ด้วยฟังก์ชันเช่น `handle_call_tool` ในฟังก์ชันนั้น เราต้องแยกชื่อเครื่องมือ อาร์กิวเมนต์ และตรวจสอบให้แน่ใจว่าอาร์กิวเมนต์ถูกต้องสำหรับเครื่องมือที่ระบุ เราสามารถตรวจสอบความถูกต้องของอาร์กิวเมนต์ในฟังก์ชันนี้หรือในขั้นตอนถัดไปในเครื่องมือจริง

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is a dictionary with tool names as keys
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # invoke the tool
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

นี่คือสิ่งที่เกิดขึ้น:

- ชื่อเครื่องมือของเราอยู่ในพารามิเตอร์อินพุต `name` ซึ่งเป็นจริงสำหรับอาร์กิวเมนต์ในรูปแบบของ dictionary `arguments`

- เครื่องมือถูกเรียกใช้ด้วย `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` การตรวจสอบความถูกต้องของอาร์กิวเมนต์เกิดขึ้นใน property `handler` ซึ่งชี้ไปที่ฟังก์ชัน หากล้มเหลวจะเกิดข้อยกเว้น

ตอนนี้เราเข้าใจการแสดงรายการและการเรียกใช้เครื่องมือโดยใช้เซิร์ฟเวอร์ระดับต่ำอย่างครบถ้วน

ดู [ตัวอย่างเต็ม](./code/README.md) ที่นี่

## งานที่ได้รับมอบหมาย

ขยายรหัสที่คุณได้รับด้วยเครื่องมือ ทรัพยากร และคำสั่งจำนวนหนึ่ง และสะท้อนให้เห็นว่าคุณสังเกตเห็นว่าคุณเพียงแค่ต้องเพิ่มไฟล์ในไดเรกทอรีเครื่องมือและไม่ต้องเพิ่มที่อื่น

*ไม่มีการให้คำตอบ*

## สรุป

ในบทนี้ เราได้เห็นวิธีการเซิร์ฟเวอร์ระดับต่ำทำงานและวิธีที่สามารถช่วยเราสร้างสถาปัตยกรรมที่ดีที่เราสามารถสร้างต่อได้ เราได้พูดคุยเกี่ยวกับการตรวจสอบความถูกต้อง และคุณได้เห็นวิธีการทำงานกับไลบรารีการตรวจสอบความถูกต้องเพื่อสร้าง schema สำหรับการตรวจสอบอินพุต

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้