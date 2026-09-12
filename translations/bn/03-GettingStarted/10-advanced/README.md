# উন্নত সার্ভার ব্যবহার

MCP SDK-তে দুই ধরনের সার্ভার প্রদর্শিত হয়েছে, আপনার নিয়মিত সার্ভার এবং লো-লেভেল সার্ভার। সাধারণত, আপনি এতে ফিচার যুক্ত করতে নিয়মিত সার্ভার ব্যবহার করবেন। তবে কিছু ক্ষেত্রে, আপনি লো-লেভেল সার্ভারের উপর নির্ভর করতে চাইবেন যেমন:

- উন্নত স্থাপত্য। নিয়মিত সার্ভার এবং একটি লো-লেভেল সার্ভার উভয়ের মাধ্যমে একটি পরিচ্ছন্ন স্থাপত্য তৈরি করা সম্ভব, তবে কিছুটা সহজ বলা যেতে পারে লো-লেভেল সার্ভারের মাধ্যমে।
- ফিচার প্রাপ্যতা। কিছু উন্নত ফিচার শুধুমাত্র
    লো-লেভেল সার্ভার দিয়ে ব্যবহার করা যায়। পরবর্তী অধ্যায়ে
    Elicitation এবং legacy Sampling ফিচার আলোচনা করা হয়েছে, যা MCP `2026-07-28`-এ নিষিদ্ধ করা হয়েছে।

## নিয়মিত সার্ভার বনাম লো-লেভেল সার্ভার

নিয়মিত সার্ভার দিয়ে MCP সার্ভার তৈরি কেমন দেখায় এখানে:

**Python**

```python
mcp = FastMCP("Demo")

# একটি যোগ করার সরঞ্জাম যোগ করুন
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

// একটি সংযোজন সরঞ্জাম যোগ করুন
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

মূল পয়েন্ট হল আপনি স্পষ্টভাবে প্রতিটি টুল, রিসোর্স বা প্রম্পট সার্ভারে যুক্ত করছেন যেটা আপনি চান। এতে কিছু ভুল নেই।  

### লো-লেভেল সার্ভার পদ্ধতি

তবে, যখন আপনি লো-লেভেল সার্ভার পদ্ধতি ব্যবহার করেন তখন এটি ভিন্নভাবে ভাবতে হবে। প্রতিটি টুল, রিসোর্স বা প্রম্পটের জন্য দুইটি হ্যান্ডলার তৈরি করতে হবে। যেমন, টুলগুলোর জন্য দুইটি ফাংশন থাকবে:

- সব টুলের তালিকা দেওয়া। একটি ফাংশন হবে সব টুল তালিকা প্রদানের জন্য।
- টুল কল হ্যান্ডল করা। এখানে একটি ফাংশন থাকবে যেটা টুল কল গুলো হ্যান্ডল করবে।

এটা কম কাজের মতো মনে হচ্ছে, তাই না? অর্থাৎ টুল রেজিস্টার করার বদলে, আমাকে শুধু নিশ্চিত করতে হবে যে টুল তালিকাভুক্ত আছে যখন সব টুল তালিকা দেখানো হয় এবং যখন টুল কল করার অনুরোধ আসে তখন কল হয়। 

এখন দেখি কোড কেমন দেখাচ্ছে:

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
  // নিবন্ধিত সরঞ্জামগুলির তালিকা প্রদান করুন
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

এখন আমাদের কাছে একটি ফাংশন আছে যা ফিচারগুলোর তালিকা ফেরত দেয়। টুল তালিকার প্রতিটি এন্ট্রিতে যেমন `name`, `description` এবং `inputSchema` ফিল্ড রয়েছে যা ফেরত দেয়ার টাইপ অনুসরণ করে। এটি আমাদের টুল এবং ফিচার ডিফিনিশন অন্য কোথাও রাখার সুযোগ দেয়। এখন আমরা সব টুল `tools` ফোল্ডারে রাখতে পারি এবং একইভাবে আপনার সব ফিচারও যাতে আলাদা আলাদা ফোল্ডারে থাকে, তাই আপনার প্রজেক্টের সংগঠন এমন হতে পারে:

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

এটা দারুণ, আমাদের স্থাপত্যকে অনেক পরিষ্কার ভাবে সাজানো যায়।

টুল কল করার ব্যাপারে, এটা কি একই ধারণা? একটি হ্যান্ডলার যেকোনো টুল কল করবে? হ্যাঁ, ঠিক তাই, এখানে সেই কোড:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # টুলগুলি একটি অভিধান যার চাবি হিসেবে টুলের নাম রয়েছে
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

উপরের কোড থেকে দেখা যাচ্ছে, আমাদের টুল এবং আর্গুমেন্ট পার্স করতে হবে এবং তারপর টুল কল করতে হবে।

## স্বীকৃতি দিয়ে পদ্ধতি উন্নতকরণ

এখন পর্যন্ত, আপনি দেখেছেন কিভাবে আপনার সব রেজিস্ট্রেশন—টুল, রিসোর্স এবং প্রম্পট যোগ করার জন্য—প্রতিটি ফিচার টাইপের জন্য এই দুই হ্যান্ডলার দ্বারা প্রতিস্থাপিত হতে পারে। আর কি করা উচিত? অবশ্যই, কিছু যাচাইকরণ যুক্ত করা উচিত যাতে টুল সঠিক আর্গুমেন্ট নিয়ে কল হয়। প্রতিটি রানটাইমের নিজস্ব সমাধান আছে, যেমন Python Pydantic ব্যবহার করে এবং TypeScript Zod ব্যবহার করে। ধারণা হলো আমরা নিম্নলিখিত করব:

- একটি ফিচার (টুল, রিসোর্স বা প্রম্পট) তৈরি করার লজিক সেটাই সংশ্লিষ্ট ফোল্ডারে স্থানান্তরিত করব।
- আগত অনুরোধ যাচাই করার উপায় যোগ করব, যেমন একটি টুল কল করার অনুরোধ।

### একটি ফিচার তৈরি করা

একটি ফিচার তৈরি করতে হবে, ফিচারের জন্য একটি ফাইল তৈরি করতে হবে এবং অবশ্যই সেটাতে ওই ফিচারের জন্য প্রয়োজনীয় বাধ্যতামূলক ফিল্ড থাকতে হবে। টুল, রিসোর্স এবং প্রম্পট ফিল্ডের মধ্যে কিছু পার্থক্য আছে।

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

    # TODO: Pydantic যোগ করুন, যাতে আমরা একটি AddInputModel তৈরি করতে পারি এবং args যাচাই করতে পারি

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

এখানে দেখানো হয়েছে কিভাবে আমরা নিম্নলিখিত কাজ করি:

- Pydantic ব্যবহার করে *schema.py* ফাইলে `AddInputModel` স্কিমা তৈরি করা হয়েছে যার ফিল্ড `a` এবং `b`।
- আগত অনুরোধকে `AddInputModel` টাইপে পার্স করার চেষ্টা করা হয়, যদি প্যারামিটার মেল না খায় তবে ক্র্যাশ হবে:

   ```python
   # add.py
    try:
        # Pydantic মডেল ব্যবহার করে ইনপুট যাচাই করুন
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

পার্সিং লজিক সরাসরি টুল কলেই বা হ্যান্ডলার ফাংশনে রাখতে পারেন।

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

       // @ts-অমর্যাদা
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

- সব টুল কল হ্যান্ডলারের ভেতরে এখন আমরা আগত অনুরোধ টুলের নির্ধারিত স্কিমাতে পার্স করার চেষ্টা করি:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    তা কাজ করলে আমরা আসল টুল কল করি:

    ```typescript
    const result = await tool.callback(input);
    ```

যেমন দেখা যায়, এই পদ্ধতিতে একটি দারুণ স্থাপত্য তৈরি হয় কারণ সবকিছুই তাদের নিজ নিজ জায়গায় থাকে, *server.ts* একটি ছোট ফাইল যা শুধুমাত্র রিকোয়েস্ট হ্যান্ডলার সংযুক্ত করে এবং প্রতিটি ফিচার তাদের নিজ নিজ ফোল্ডারে থাকে যেমন tools/, resources/ বা prompts/।

দারুণ, চলুন এবার এটা তৈরি করার চেষ্টা করি।

## অনুশীলন: একটি লো-লেভেল সার্ভার তৈরি করা

এই অনুশীলনে, আমরা নিম্নলিখিত কাজ করব:

১। একটি লো-লেভেল সার্ভার তৈরি করব যা টুল তালিকা দেখানো এবং টুল কল হ্যান্ডেল করবে।
১। একটি স্থাপত্য তৈরি করব যা আপনি ভবিষ্যতে বাড়াতে পারবেন।
১। যাচাইকরণ যুক্ত করব যাতে আপনার টুল কল সঠিকভাবে যাচাই করা হয়।

### -1- একটি স্থাপত্য তৈরি করা

প্রথমে আমাদের এমন একটি স্থাপত্য সেটআপ করতে হবে যা ফিচার বাড়ানো সহজ করবে, এটির রূপ নিচের মতো:

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

এখন আমরা একটি স্থাপত্য সজ্জিত করেছি যা সহজে নতুন টুল `tools` ফোল্ডারে যুক্ত করার সুযোগ দেয়। রিসোর্স এবং প্রম্পটের জন্য সাবডিরেক্টরি যোগ করতেও পারেন।

### -2- একটি টুল তৈরি করা

এখন দেখি টুল তৈরি কেমন হবে। প্রথমে এটি তার *tool* সাবডিরেক্টরিতে তৈরি করতে হবে, নিম্নরূপ:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic মডেল ব্যবহার করে ইনপুট যাচাই করুন
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic যোগ করুন, যাতে আমরা একটি AddInputModel তৈরি করতে পারি এবং আর্গুমেন্টগুলি যাচাই করতে পারি

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

এখানে দেখা যাচ্ছে আমরা কিভাবে নাম, বর্ণনা, এবং ইনপুট স্কিমা Pydantic দিয়ে ডিফাইন করি এবং একটি হ্যান্ডলার থাকে যে টুল কল হলে চালিত হবে। সবশেষে `tool_add` নামের ডিকশনারি এক্সপোজ করি যা এসব প্রপার্টি ধারণ করে।

*schema.py* ফাইলও আছে যা টুলের ইনপুট স্কিমা নির্ধারণে ব্যবহৃত হয়:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

আমরা *__init__.py* ফাইলও পূরণ করব যাতে tools ডিরেক্টরি মডিউল হিসেবে বিবেচিত হয়। পাশাপাশি, এর ভিতরের মডিউলগুলো প্রকাশ করতে হবে এভাবে:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

আরো টুল যোগ করলে এই ফাইলে আমরা আরো এন্ট্রি যোগ করব।

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

এখানে একটি ডিকশনারি তৈরি করা হয়েছে যা প্রপার্টি ধারণ করে:

- name, টুলটির নাম।
- rawSchema, Zod স্কিমা যা ইনকামিং টুল কল অনুরোধ যাচাইতে ব্যবহৃত হয়।
- inputSchema, হ্যান্ডলার ব্যবহার করে এই স্কিমা।
- callback, টুল কল করতে যেটা ব্যবহৃত হয়।

পাশাপাশি একটি `Tool` আছে যা এই ডিকশনারিকে একটি টাইপে রূপান্তর করে যেটা mcp সার্ভার হ্যান্ডলার গ্রহণ করতে পারে, মানে এটি এরকম:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

*schema.ts* ফাইলেও ইনপুট স্কিমা আছে যা প্রতিটি টুলের জন্য সংরক্ষিত, বর্তমানে একটি স্কিমা আছে, ভবিষ্যতে টুল বাড়ালে আরো থাকবে:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

দারুণ, এবার দেখি কিভাবে টুল তালিকা পরিচালনা করা যায়।

### -3- টুল তালিকা হ্যান্ডল করা

এবার টুল তালিকা পরিচালনার জন্য একটি রিকোয়েস্ট হ্যান্ডলার সেটআপ করতে হবে। আমাদের সার্ভার ফাইলে নিচের কোড যোগ করতে হবে:

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

এখানে, আমরা `@server.list_tools` ডেকোরেটর এবং `handle_list_tools` ফাংশন যুক্ত করেছি। এতে টুলের তালিকা তৈরি করতে হয়। দেখুন প্রতিটি টুলে নাম, বর্ণনা এবং inputSchema থাকতে হবে।  

**TypeScript**

টুল তালিকা হ্যান্ডলারের জন্য, সার্ভারে `setRequestHandler` কল করতে হবে যেটি একটি সঠিক স্কিমা নেয় যে কাজটি করছে, এখানে `ListToolsRequestSchema`।

```typescript
// ইনডেক্স.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// সার্ভার.ts
// সংক্ষিপ্ততার জন্য কোড বাদ দেওয়া হয়েছে
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // নিবন্ধিত টুলগুলির তালিকা ফেরত দিন
  return {
    tools: tools
  };
});
```

দারুণ, এখন টুল তালিকা দেখানোর অংশ সমাধান হলো, চালিয়ে যাই টুল কল করার পদ্ধতিতে।

### -4- টুল কল হ্যান্ডল করা

টুল কল করার জন্য আরেকটি রিকোয়েস্ট হ্যান্ডলার সেটআপ করতে হবে যা ফিচার এবং আর্গুমেন্ট নির্দিষ্ট অনুরোধ পরিচালনা করবে।

**Python**

`@server.call_tool` ডেকোরেটর ব্যবহার করে `handle_call_tool` ফাংশন তৈরি করুন। সেখানে টুল নাম, আর্গুমেন্ট পার্স করতে হবে এবং যাচাই করতে হবে আর্গুমেন্ট সঠিক কিনা। যাচাই এই ফাংশনে বা টুলের ভেতরে দুই জায়গায় হতে পারে।

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools হল একটি অভিধান যেখানে টুলগুলির নামগুলি কী হিসেবে থাকে
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

এখানে যা হয়:

- টুল নাম ইতোমধ্যে `name` ইনপুট প্যারামিটার হিসেবে আছে এবং `arguments` ডিকশনারি আকারে আর্গুমেন্ট।

- টুল কল করা হয় `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` দিয়ে। আর্গুমেন্ট যাচাই `handler` ফাংশনে হয়, ব্যর্থ হলে exception উঠবে। 

এইভাবে আমরা লো-লেভেল সার্ভার ব্যবহার করে টুল তালিকা দেখা এবং কল করার পূর্ণ ধারণা পেলাম।

সম্পূর্ণ উদাহরণ দেখতে এখানে ক্লিক করুন [full example](./code/README.md)

## দায়িত্ব

আপনাকে দেওয়া কোডে আরও টুল, রিসোর্স এবং প্রম্পট যোগ করুন এবং লক্ষ্য করুন কিভাবে আপনাকে শুধু tools ডিরেক্টরিতে ফাইল যোগ করতে হয়, অন্য কোথাও নয়।

*কোন সমাধান দেওয়া হয়নি*

## সারসংক্ষেপ

এই অধ্যায়ে আমরা দেখলাম লো-লেভেল সার্ভার পদ্ধতি কিভাবে কাজ করে এবং কিভাবে এটি আমাদের একটি সুন্দর স্থাপত্য তৈরি করতে সাহায্য করে যা আমরা তৈরি করে যেতে পারি। আমরা যাচাইকরণ নিয়ে আলোচনা করেছি এবং দেখানো হয়েছে কিভাবে যাচাইকরণ লাইব্রেরি ব্যবহার করে ইনপুট যাচাইকরণের স্কিমা তৈরি করা যায়।

## পরবর্তী কী

- পরবর্তী: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->