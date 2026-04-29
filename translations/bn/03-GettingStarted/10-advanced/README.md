# উন্নত সার্ভার ব্যবহারের

MCP SDK-তে দুই ধরনের সার্ভার উন্মুক্ত আছে, আপনার স্বাভাবিক সার্ভার এবং লো-লেভেল সার্ভার। সাধারণত, আপনি ফিচার যুক্ত করার জন্য রেগুলার সার্ভার ব্যবহার করবেন। তবে কিছু ক্ষেত্রে, আপনি লো-লেভেল সার্ভারের উপর নির্ভর করতে চাইবেন, যেমন:

- উন্নত স্থাপত্য। পরিষ্কার স্থাপত্য তৈরি করা সম্ভব রেগুলার সার্ভার এবং লো-লেভেল সার্ভার দুইটিতেই, তবে বলা যেতে পারে যে লো-লেভেল সার্ভারে এটা কিছুটা সহজ।
- ফিচার উপলব্ধতা। কিছু উন্নত ফিচার কেবল লো-লেভেল সার্ভারের মাধ্যমে ব্যবহার করা যায়। পরবর্তী অধ্যায়ে, যেমন স্যাম্পলিং এবং এলিসিটেশন যুক্ত করার সময় এটা দেখা যাবে।

## রেগুলার সার্ভার বনাম লো-লেভেল সার্ভার

রেগুলার সার্ভার দিয়ে MCP সার্ভার তৈরি কেমন দেখায়, তা হলো:

**Python**

```python
mcp = FastMCP("Demo")

# একটি সংযোজন টুল যোগ করুন
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

// একটি যোগ যোগ করার টুল যোগ করুন
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

মূলত এই কথা হচ্ছে যে আপনি স্পষ্টভাবে প্রতিটি টুল, রিসোর্স বা প্রম্পট যোগ করেন যা আপনি সার্ভারে চান। এতে কিছু ভুল নেই।

### লো-লেভেল সার্ভার পদ্ধতি

তবে লো-লেভেল সার্ভার পদ্ধতি ব্যবহার করলে আপনাকে ভিন্নভাবে ভাবতে হবে। প্রতিটি টুল নিবন্ধন করার পরিবর্তে, আপনি ফিচার টাইপ প্রতি দুটি হ্যান্ডলার তৈরি করবেন (টুল, রিসোর্স বা প্রম্পট)। যেমন টুলের জন্য কেবল দুইটি ফাংশন থাকবে:

- সব টুল তালিকা করা। একটি ফাংশন সমস্ত টুল তালিকা করার চেষ্টা পরিচালনা করবে।
- সব টুল কল পরিচালনা করা। এখানে মাত্র একটি ফাংশন টুল কল হ্যান্ডল করবে।

এটা সম্ভবত কম কাজ বলে শোনাচ্ছে, তাই না? টুল নিবন্ধন করার পরিবর্তে আমাকে শুধু নিশ্চিত করতে হবে যে টুলটি সব টুল তালিকা করার সময় তালিকাভুক্ত আছে এবং এটি কল করার অনুরোধ এলে কল করা হয়।

চলুন কোড এখন কেমন দেখাচ্ছে দেখি:

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
  // নিবন্ধিত সরঞ্জামগুলির তালিকা ফেরত দিন
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

এখানে একটি ফাংশন আছে যা ফিচারগুলোর তালিকা রিটার্ন করে। টুল তালিকার প্রতিটি এন্ট্রিতে এখন নাম, বিবরণ এবং ইনপুটস্কিমা মতো ফিল্ড থাকে যা রিটার্ন টাইপ অনুসরণ করে। এর ফলে আমরা টুল এবং ফিচার ডেফিনিশন অন্যত্র রাখতে পারি। আমরা এখন সব টুল একটি tools ফোল্ডারে রাখতে পারি এবং একইভাবে সব ফিচারের জন্য, তাই আপনার প্রকল্প হঠাৎ এভাবে সংগঠিত হতে পারে:

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

দারুন, আমাদের স্থাপত্য বেশ পরিষ্কার হতে পারে।

টুল কল করার ব্যাপারে কী, তখন কি একই ধারণা, একই হ্যান্ডলার যেকোনো টুল কল করতে? হ্যাঁ, ঠিক তাই, কোড হলো:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools হল একটি অভিধান যার কী হিসাবে টুলের নাম রয়েছে
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
    
    // আর্গুমেন্টস: request.params.arguments
    // TODO টুলটি কল করুন,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

উপরের কোড থেকে দেখা যাচ্ছে, আমাদের টুল কল করার জন্য কোন টুল এবং কোন আর্গুমেন্ট দিয়ে কল করতে হবে সেটা পার্স করতে হয় এবং তারপর টুল কল করতে হয়।

## ভ্যালিডেশন সহ পদ্ধতি উন্নয়ন

এখন পর্যন্ত আপনি দেখেছেন কিভাবে টুল, রিসোর্স এবং প্রম্পট যোগ করার রেজিস্ট্রেশন দুইটি হ্যান্ডলার দ্বারা প্রতিস্থাপিত হতে পারে। আর কী করতে হবে? অবশ্যই কিছু ধরনের ভ্যালিডেশন যোগ করতে হবে যাতে টুল সঠিক আর্গুমেন্ট দিয়ে কল হচ্ছে তা নিশ্চিত হয়। পৃথক রUNTIME এর নিজস্ব সমাধান আছে, যেমন Python পিড্যান্টিক ব্যবহার করে এবং TypeScript Zod ব্যবহার করে। ধারণাটি হলো নিচের কাজগুলো করা:

- একটি ফিচার (টুল, রিসোর্স বা প্রম্পট) তৈরি করার লজিক সেই নির্দিষ্ট ফোল্ডারে স্থানান্তর করা।
- একটি উপায় যোগ করা যাতে আসা অনুরোধ ভ্যালিডেট করা যায়, যেমন টুল কল করার অনুরোধ।

### একটি ফিচার তৈরি করা

একটি ফিচার তৈরি করতে, ওই ফিচারের জন্য একটি ফাইল তৈরি করতে হবে এবং নিশ্চিত করতে হবে যে সেখানে ঐ ফিচারের জন্য প্রয়োজনীয় বাধ্যতামূলক ক্ষেত্র আছে। কোন ফিল্ডগুলো টুল, রিসোর্স এবং প্রম্পটের মধ্যে কিছুটা আলাদা।

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
        # Pydantic মডেল ব্যবহার করে ইনপুট যাচাই করুন
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic যোগ করুন, তাই আমরা একটি AddInputModel তৈরি করতে এবং আর্গুমেন্ট যাচাই করতে পারি

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

এখানে কী হচ্ছে:

- পিড্যান্টিক দিয়ে একটি স্কিমা তৈরি করা `AddInputModel` নামে, যেখানে ফিল্ড `a` এবং `b` রয়েছে ফাইল *schema.py*-এ।
- আসা অনুরোধকে `AddInputModel` টাইপ হিসাবে পার্স করার চেষ্টা করা, যদি প্যারামিটার আপনতর হয় তাহলে এটি ক্র্যাশ করবে:

   ```python
   # add.py
    try:
        # Pydantic মডেল ব্যবহার করে ইনপুট যাচাই করুন
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

আপনি চাইলেই পার্সিং লজিক টুল কলেই রাখতে পারেন বা হ্যান্ডলার ফাংশনে।

**TypeScript**

```typescript
// সার্ভার.ts
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

       // @ts-অবজ্ঞা
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

// স্কিমা.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// যোগ করুন.ts
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

- সব টুল কল পরিচালনা করা হ্যান্ডলারে, আমরা আসা অনুরোধ টুলের নির্ধারিত স্কিমায় পার্স করার চেষ্টা করি:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    যদি সেটা সফল হয়, তাহলে আসল টুল কলের দিকে এগিয়ে যাই:

    ```typescript
    const result = await tool.callback(input);
    ```

এখান থেকে দেখা যাচ্ছে, এই পদ্ধতি একটি দারুন স্থাপত্য তৈরি করে কারণ সবকিছুই তার স্থান পায়। *server.ts* একটি খুব ছোট ফাইল যা শুধু রিকুয়েস্ট হ্যান্ডলার ওয়্যার করে এবং প্রতিটি ফিচার তাদের নিজ নিজ ফোল্ডারে থাকে যেমন tools/, resources/ বা prompts/।

দারুন, এখন চেষ্টা করি এটা তৈরি করতে।

## অনুশীলন: লো-লেভেল সার্ভার তৈরি

এই অনুশীলনে, আমরা করব:

1. লো-লেভেল সার্ভার তৈরি করব যা টুল তালিকা হ্যান্ডেল করতে এবং টুল কল করতে পারবে।
2. এমন একটি স্থাপত্য তৈরি করব যা পরে সহজে বাড়ানো যাবে।
3. যাচাই যোগ করব যাতে টুল কল সঠিকভাবে ভ্যালিডেটেড হয়।

### -1- একটি স্থাপত্য তৈরি করা

প্রথম কাজ হল এমন একটি স্থাপত্য তৈরি করা যা সহজে স্কেল করা যায় নতুন ফিচার যোগ করার সময়, এরকম দেখাচ্ছে:

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

এখন আমরা একটি স্থপতিত্ব স্থাপন করেছি যা নিশ্চিত করে আমরা সহজে tools ফোল্ডারে নতুন টুল যোগ করতে পারব। রিসোর্স এবং প্রম্পটের জন্যও সাবডিরেক্টরি যোগ করতে পারেন।

### -2- একটি টুল তৈরি করা

চলুন দেখি টুল তৈরি কেমন হয়। প্রথমে এটি এর *tool* সাবডিরেক্টরিতে তৈরি করতে হবে যেমন:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic মডেল ব্যবহার করে ইনপুট যাচাই করুন
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic যোগ করুন, তাই আমরা একটি AddInputModel তৈরি করতে এবং আর্গুমেন্টগুলি যাচাই করতে পারি

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

এখানে আমরা নাম, বর্ণনা এবং ইনপুট স্কিমা পিড্যান্টিক দিয়ে ডিফাইন করি এবং একটি হ্যান্ডলার থাকে যা কল করা হলে চালিত হয়। শেষ পর্যন্ত `tool_add` নামে একটি ডিকশনারি প্রকাশ করি যা এই প্রপার্টিগুলো ধরে রাখে।

সাথে আছে *schema.py* যা আমাদের টুলের ইনপুট স্কিমা সংজ্ঞায়িত করে:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

আমাদের *__init__.py* ফাইল পপুলেট করতেও হবে যাতে tools ডিরেক্টরি একটি মডিউল হিসেবে বিবেচিত হয়। সাথে এর মডিউলগুলোও এক্সপোজ করতে হবে যেমন:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

আমরা যত বেশি টুল যোগ করব, এই ফাইল আপডেট করতে পারব।

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

এখানে একটি ডিকশনারি তৈরি করা হয়েছে যার প্রপার্টি:

- name, টুলের নাম।
- rawSchema, Zod স্কিমা যা টুল কলের আসা অনুরোধ যাচাই করবে।
- inputSchema, হ্যান্ডলার ব্যবহৃত স্কিমা।
- callback, টুল কল করার ফাংশন।

সাথে `Tool` টাইপটি যা এই ডিকশনারি থেকে মঞ্চ নেয় এবং মcp সার্ভার হ্যান্ডলার গ্রহণ করতে পারে, এভাবে:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

এবং একটি *schema.ts* আছে যেখানে প্রতিটি টুলের ইনপুট স্কিমা থাকে, যা এখন মাত্র একটি আছে, কিন্তু আমরা আরও টুল যোগ করলে আরও স্কিমা যোগ করতে পারব:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

দারুন, এখন আমাদের টুল তালিকা পরিচালনা শুরু করি।

### -3- টুল তালিকা পরিচালনা

টুল তালিকা পরিচালনার জন্য রিকুয়েস্ট হ্যান্ডলার সেটআপ করতে হবে। সার্ভার ফাইলে যা যোগ করতে হবে:

**Python**

```python
# সংক্ষিপ্ততার জন্য কোড বাদ দেওয়া হয়েছে
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

এখানে আমরা `@server.list_tools` ডেকোরেটর এবং প্রয়োগকারী ফাংশন `handle_list_tools` যোগ করেছি। এতে টুলের নাম, বর্ণনা এবং ইনপুটস্কিমা থাকা নিশ্চিত করতে হবে।

**TypeScript**

টুল তালিকা করার রিকুয়েস্ট হ্যান্ডলার সেটআপ করতে, সার্ভারে `setRequestHandler` কল করতে হবে, যেটা `ListToolsRequestSchema` জাতীয় স্কিমা ব্যবহার করে:

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
// সংক্ষিপ্ততার জন্য কোড বাদ দেওয়া হয়েছে
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // নিবন্ধিত টুলগুলির তালিকা ফেরত দিন
  return {
    tools: tools
  };
});
```

দারুন, এখন টুল তালিকা সমস্যা আমরা সমাধান করেছি, দেখব কীভাবে টুল কল করতে হবে।

### -4- টুল কল পরিচালনা

একটি টুল কল করতে আরেকটি রিকুয়েস্ট হ্যান্ডলার সেটআপ করতে হবে, যা নির্দিষ্ট করবে কোন ফিচার কল হবে এবং কী আর্গুমেন্টে।

**Python**

`@server.call_tool` ডেকোরেটর ব্যবহার করি এবং `handle_call_tool` নামের ফাংশন লিখি। এই ফাংশনে টুলের নাম ও আর্গুমেন্ট পার্স করতে হবে এবং নিশ্চিত করতে হবে আর্গুমেন্টগুলো বৈধ। যাচাই এই ফাংশনে কিংবা টুল কলের সময় করতে পারি।

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # টুলস হলো একটি অভিধান যেখানে টুল নামগুলি কী হিসেবে থাকে
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # টুলটি চালান
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

এটা হচ্ছে:

- টুলের নাম `name` নামে ইনপুট প্যারামিটার হিসেবে আগেই আছে, এবং `arguments` ডিকশনারিতে আর্গুমেন্ট গুলো।

- টুলটি `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` দিয়ে কল করা হয়। আর্গুমেন্ট যাচাই `handler` প্রপার্টিতে হয়, যা একটি ফাংশন নির্দেশ করে, যদি ব্যর্থ হয় তাহলে এক্সেপশন উঠবে।

এখন আমরা সম্পূর্ণ বুঝে গেছি কিভাবে লো-লেভেল সার্ভার ব্যবহার করে টুল তালিকা এবং কল করা হয়।

[সম্পূর্ণ উদাহরণ](./code/README.md) এখানে দেখুন

## অ্যাসাইনমেন্ট

আপনার দেওয়া কোডে অনেকগুলি টুল, রিসোর্স এবং প্রম্পট যোগ করুন এবং লক্ষ্য করুন যে আপনাকে শুধু tools ডিরেক্টরিতে ফাইল যোগ করতে হচ্ছে, অন্য কোথাও নয়।

*কোন সমাধান দেওয়া নেই*

## সারাংশ

এই অধ্যায়ে আমরা দেখেছি কিভাবে লো-লেভেল সার্ভার পদ্ধতি কাজ করে এবং কীভাবে এটি একটি সুন্দর স্থাপত্য তৈরি করতে সাহায্য করে যেটাতে আমরা নির্মাণ চালিয়ে যেতে পারি। আমরা যাচাই আলোচনা করেছি এবং দেখিয়েছি কিভাবে ভ্যালিডেশন লাইব্রেরি ব্যবহার করে ইনপুট যাচাইয়ের স্কিমা তৈরি করতে হয়।

## পরবর্তী কী

- পরবর্তী: [সহজ প্রমাণীকরণ](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই ডকুমেন্টটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। যদিও আমরা সঠিকতার চেষ্টা করি, অনুগ্রহ করে বুঝুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ডকুমেন্টটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ প্রয়োজনীয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনও ভুলবোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->