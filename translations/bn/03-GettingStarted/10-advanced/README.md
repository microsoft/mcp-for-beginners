# উন্নত সার্ভার ব্যবহারের পদ্ধতি

MCP SDK তে দুই ধরনের সার্ভার আছে, আপনার সাধারণ সার্ভার এবং নিম্ন-স্তরের সার্ভার। সাধারণত, আপনি ফিচার যোগ করার জন্য সাধারণ সার্ভার ব্যবহার করবেন। কিন্তু কিছু ক্ষেত্রে, আপনি নিম্ন-স্তরের সার্ভারের উপর নির্ভর করতে চান, যেমন:

- উন্নত আর্কিটেকচার। একটি পরিষ্কার আর্কিটেকচার তৈরি করা সম্ভব সাধারণ সার্ভার এবং নিম্ন-স্তরের সার্ভার উভয়ের সাথে, তবে একটু সহজ হতে পারে নিম্ন-স্তরের সার্ভার দিয়ে।
- ফিচার উপলব্ধতা। কিছু উন্নত ফিচার শুধুমাত্র নিম্ন-স্তরের সার্ভারের মাধ্যমে ব্যবহার করা যায়। পরে আমরা স্যাম্পলিং এবং এলিসিটেশন যোগ করার সময় এটি দেখবেন।

## সাধারণ সার্ভার বনাম নিম্ন-স্তরের সার্ভার

এখানে MCP সার্ভার তৈরির উদাহরণ সাধারণ সার্ভারের জন্য দেওয়া হলো

**Python**

```python
mcp = FastMCP("Demo")

# একটি যোগ টুল যোগ করুন
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

// একটি যোগ করার সরঞ্জাম যুক্ত করুন
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

মূল কথা হল আপনি স্পষ্টভাবে প্রতিটি টুল, রিসোর্স বা প্রম্পট যোগ করেন যা সার্ভারে চান। এতে সমস্যা নেই।  

### নিম্ন-স্তরের সার্ভার পন্থা

যখন আপনি নিম্ন-স্তরের সার্ভার ব্যবহার করবেন তখন আলাদা ভাবে চিন্তা করতে হবে। প্রতিটি টুল নিবন্ধন করার পরিবর্তে, আপনি ফিচার টাইপ (টুলস, রিসোর্স, প্রম্পট) প্রতি দুইটি হ্যান্ডলার তৈরি করবেন। যেমন টুলস এর ক্ষেত্রে, শুধু দুটি ফাংশন থাকবে:

- সমস্ত টুলের তালিকা দেখানো। এক ফাংশন সব টুল তালিকা দেখানোর চেষ্টা করবে।
- সকল টুল কলের হ্যান্ডেলিং। এখানে শুধু একটি ফাংশন একটি টুল কলের জন্য দায়িত্বশীল।

এটি কম কাজের মনে হচ্ছে, তাই না? টুল নিবন্ধন করার বদলে, আপনাকে শুধু নিশ্চিত করতে হবে টুলের তালিকায় টুলটি থাকে এবং কল আসলে কল করা হয়।

চলুন দেখে নেই কোড এখন কেমন দেখাচ্ছে:

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
  // নিবন্ধিত সরঞ্জামগুলির তালিকা ফিরিয়ে দিন
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

এখানে একটি ফাংশন আছে যা ফিচারগুলোর তালিকা রিটার্ন করে। টুলস তালিকার প্রতিটি এন্ট্রি এখন `name`, `description` এবং `inputSchema` এর মতো ফিল্ড আছে যেখানে টুলস ও ফিচারের ডেফিনিশন আলাদা জায়গায় রাখা যাবে। এখন আমরা টুলসমূহ tools ফোল্ডারে রাখতে পারি এবং একইভাবে ফিচারগুলোর জন্য আলাদা ফোল্ডার রাখতে পারি, ফলে প্রজেক্ট এমনভাবে সাজানো যাবে:

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

দারুণ, আমাদের আর্কিটেকচার এখন বেশ পরিষ্কার হতে পারে।

টুল কল করার ব্যাপারটা কেমন, একই ধারণা, একটা হ্যান্ডলার দ্বারা যেকোনো টুল কল করা যাবে? হ্যাঁ, ঠিক তেমনই, এখানে কোডটি:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools হল একটি অভিধান যেখানে কী হিসেবে টুলের নাম রয়েছে
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
    
    // আর্গুমেন্ট: request.params.arguments
    // TODO টুলটি কল করুন,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

উপরের কোড থেকে দেখা যাচ্ছে, আমাদের টুল কল করতে হলে কোন টুল কল করা হচ্ছে এবং কোন আর্গুমেন্ট দিয়ে কল করা হচ্ছে তা বিশ্লেষণ করতে হবে, তারপর টুল কল করতে হবে।

## ভ্যালিডেশন সহ পন্থার উন্নতি

এখন পর্যন্ত, আপনি দেখেছেন কিভাবে টুল, রিসোর্স এবং প্রম্পট যোগ করার জন্য প্রতিটি ফিচার টাইপের জন্য দুটি হ্যান্ডলার দিয়ে নিবন্ধন প্রতিস্থাপন করা যায়। আর কি করা দরকার? অবশ্যই ভ্যালিডেশন যোগ করতে হবে যেন টুল সঠিক আর্গুমেন্ট দিয়ে কল হয়। প্রতিটি রানটাইমের নিজস্ব সমাধান আছে, যেমন Python এ Pydantic এবং TypeScript এ Zod ব্যবহার হয়। ধারণাটি হলো:

- একটি ফিচার (টুল, রিসোর্স বা প্রম্পট) তৈরি করার লজিক dedicated ফোল্ডারে রাখা।
- একটি পদ্ধতি যোগ করা যেটা ইনকামিং রিকোয়েস্টটি সঠিক কিনা যাচাই করে, যেমন টুল কলের ক্ষেত্রে।

### একটি ফিচার তৈরি করা

ফিচার তৈরির জন্য একটি ফাইল তৈরি করতে হবে এবং নিশ্চিত করতে হবে এর আবশ্যক ফিল্ডগুলো আছে। ফিল্ডগুলো টুল, রিসোর্স এবং প্রম্পট এর মধ্যে কিছুটা আলাদা হয়।

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

    # TODO: Pydantic যোগ করুন, যাতে আমরা একটি AddInputModel তৈরি করতে এবং আর্গুমেন্ট যাচাই করতে পারি

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

এখানে আপনি দেখতে পাচ্ছেন আমরা:

- *schema.py* ফাইলে `AddInputModel` Pydantic স্কিমা তৈরি করেছি যার ফিল্ড `a` ও `b` আছে।
- ইনকামিং রিকোয়েস্টকে `AddInputModel` টাইপে পার্স করার চেষ্টা করি, যদি প্যারামিটার মিল না হয় তবে ক্র্যাশ হবে:

   ```python
   # add.py
    try:
        # Pydantic মডেল ব্যবহার করে ইনপুট যাচাই করুন
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

আপনি চাইলে এই পার্সিং লজিক টুল কলের ভিতরে অথবা হ্যান্ডলার ফাংশনে রাখতে পারেন।

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

- সমস্ত টুল কল হ্যান্ডলারের মধ্যে, ইনকামিং রিকোয়েস্টকে টুলের সংজ্ঞায়িত স্কিমায় পার্স করার চেষ্টা করছি:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

যদি এটি সফল হয়, তাহলে টুল কল করি:

    ```typescript
    const result = await tool.callback(input);
    ```

দেখতে পাচ্ছেন এই পন্থা চমৎকার আর্কিটেকচার তৈরি করে কারণ সবকিছু তার জায়গায় আছে, *server.ts* খুব ছোট ফাইল যা শুধু রিকোয়েস্ট হ্যান্ডলার যুক্ত করে এবং প্রতিটি ফিচার নিজের ফোল্ডারে যেমন tools/, resources/ বা prompts/ থাকে।

দারুণ, দেখুন আমরা এটা পরবর্তী ধাপে তৈরি করব।

## অনুশীলনঃ নিম্ন-স্তরের সার্ভার তৈরি

এই অনুশীলনে আমরা করব:

1. টুল তালিকা এবং টুল কল করার নিম্ন-স্তরের সার্ভার তৈরি করা।
2. এমন একটি আর্কিটেকচার বাস্তবায়ন যেটার উপর আপনি নির্মাণ করতে পারবেন।
3. ভ্যালিডেশন যোগ করা যাতে আপনার টুল কল সঠিকভাবে যাচাই হয়।

### -1- একটি আর্কিটেকচার তৈরি করা

প্রথমে এমন একটি আর্কিটেকচার দরকার যা আমাদের নতুন ফিচার সহজে যোগ করার সুযোগ দেয়, দেখতে এরকম:

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

এখন আমরা এমন আর্কিটেকচার তৈরি করেছি যা tools ফোল্ডারে সহজে নতুন টুল যোগ করার সুবিধা দেয়। রিসোর্স এবং প্রম্পটের জন্য সাবডিরেক্টরি যোগ করতে পারেন।

### -2- একটি টুল তৈরি করা

টুল তৈরি কেমন হয় দেখা যাক। প্রথমে এটি তার *tool* সাবডিরেক্টরিতে তৈরি করতে হবে:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ইনপুট পিড্যান্টিক মডেল ব্যবহার করে যাচাই করুন
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: পিড্যান্টিক যোগ করুন, যাতে আমরা একটি AddInputModel তৈরি করতে পারি এবং আর্গুমেন্ট যাচাই করতে পারি

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

এখানে আমরা নাম, বর্ণনা এবং ইনপুট স্কিমা Pydantic ব্যবহার করে সংজ্ঞায়িত করি এবং সেই সাথে একটি হ্যান্ডলার যা টুল কল হলে সক্রিয় হবে। শেষে `tool_add` এক dict যা সব প্রোপার্টি ধারণ করে।

আরো একটি *schema.py* আছে যা টুলের ইনপুট স্কিমা ডিফাইন করে:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

আমাদের *__init__.py* ফাইলও প্রয়োজন যাতে tools ডিরেক্টরিকে মডিউল হিসেবে আচরণ করা হয় এবং মডিউল এক্সপোজ করা হয়:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

আমরা যত টুল যোগ করব, এই ফাইলে নতুন এন্ট্রি যোগ করে যেতে পারি।

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

এখানে একটি dict তৈরি করছি যার প্রোপার্টিস হল:

- name, টুলের নাম।
- rawSchema, Zod স্কিমা যা টুল কল ইনকামিং রিকোয়েস্ট যাচাই করবে।
- inputSchema, যা হ্যান্ডলার ব্যবহার করবে।
- callback, যেটা টুল কার্যকর করবে।

আরো একটি `Tool` টাইপ আছে যা এই dict কে mcp সার্ভার হ্যান্ডলার গ্রহণযোগ্য টাইপে রূপান্তর করে:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

এবং একটা *schema.ts* আছে যেখানে প্রতিটি টুলের ইনপুট স্কিমা রাখা হয়। এখন শুধু একটি স্কিমা আছে, নতুন টুল যোগ করলে নতুন এন্ট্রি যুক্ত হবে:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

দারুণ, এখন টুল তালিকা হ্যান্ডলিং শুরু করা যাক।

### -3- টুল তালিকা হ্যান্ডলিং করা

টুল তালিকা হ্যান্ডল করার জন্য সার্ভারে একটি রিকোয়েস্ট হ্যান্ডলার সেট করতে হবে। যা আমাদের সার্ভার ফাইলে যোগ করতে হবে:

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

এখানে আমরা `@server.list_tools` ডেকোরেটর ব্যবহার করেছি এবং `handle_list_tools` ফাংশন ইমপ্লিমেন্ট করেছি। এতে টুলের নাম, বর্ণনা এবং `inputSchema` সহ টুলের তালিকা তৈরী করা হয়।

**TypeScript**

টুলের তালিকা হ্যান্ডল করার জন্য সার্ভারে `setRequestHandler` কল দিতে হবে উপযুক্ত স্কিমা দিয়ে, এখানে `ListToolsRequestSchema`:

```typescript
// ইন্ডেক্স.টি এস
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// সার্ভার.টি এস
// সংক্ষিপ্ততার জন্য কোড বাদ দেওয়া হয়েছে
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // নিবন্ধিত টুলগুলির তালিকা ফেরত দিন
  return {
    tools: tools
  };
});
```

দারুণ, এখন টুল তালিকা করার কাজ শেষ, চলুন টুল কল কিভাবে করব দেখি।

### -4- টুল কল হ্যান্ডল করা

টুল কল করার জন্য আরেকটি রিকোয়েস্ট হ্যান্ডলার সেট করতে হবে যা ফিচার কল করার জন্য এবং কোন আর্গুমেন্ট দিয়ে কল করতে হবে তা হ্যান্ডল করবে।

**Python**

`@server.call_tool` ডেকোরেটর দিয়ে `handle_call_tool` ফাংশন ইমপ্লিমেন্ট করুন। ফাংশনের মধ্যে টুল নাম এবং আর্গুমেন্ট পার্স করতে হবে এবং যাচাই করতে হবে আর্গুমেন্ট বৈধ কিনা। যাচাই ফাংশনে অথবা টুলে পরে করা যেতে পারে।

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools হল একটি অভিধান যার কীগুলো হলো টুলের নাম
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # টুলটি আহ্বান করুন
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

ব্যাখ্যা:

- টুল নাম `name` প্যারামিটারে আছে এবং আর্গুমেন্ট হচ্ছে `arguments` ডিকশনারি।
- টুল কল হয় `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` দিয়ে। আর্গুমেন্টের যাচাই ফাংশনে, ব্যর্থ হলে এক্সসেপশন যাবে।

এখন আমরা নিম্ন-স্তরের সার্ভার দিয়ে টুল তালিকা এবং কল সম্পূর্ণ বুঝতে পেরেছি।

দেখুন [সম্পূর্ণ উদাহরণ](./code/README.md) এখানে

## অ্যাসাইনমেন্ট

কোডে আরো কিছু টুল, রিসোর্স ও প্রম্পট যোগ করুন এবং লক্ষ্য করুন যে শুধুমাত্র tools ডিরেক্টরিতে ফাইল যোগ করলেই হচ্ছে অন্য কোথাও নয়।

*কোন সমাধান নেই*

## সারাংশ

এই অধ্যায়ে দেখেছি নিম্ন-স্তরের সার্ভার পদ্ধতি কিভাবে কাজ করে এবং কিভাবে এটি সুন্দর আর্কিটেকচার তৈরি করে যা উপর ভিত্তি করে আমরা আরো তৈরি করতে পারি। এছাড়াও যাচাইপত্র (validation) এর গুরুত্ব ও ইনপুট যাচাইয়ের জন্য স্কিমা তৈরির পদ্ধতি আলোচনা করেছি।

## পরবর্তী

- পরবর্তী: [সরল অথেনটিকেশন](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**বিস্ময়াদিবাস**:
এই নথিটি এআই অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে দয়া করে বিবেচনা করুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অপ্রাসঙ্গিকতা থাকতে পারে। মূল নথির মাতৃভাষায় থাকা সংস্করনটিকে কর্তৃত্বসূত্র হিসেবে গণ্য করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব দ্বারাও অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোন বিভ্রূতি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->