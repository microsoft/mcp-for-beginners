# উন্নত সার্ভার ব্যবহার

MCP SDK-তে দুটি ভিন্ন ধরনের সার্ভার রয়েছে: সাধারণ সার্ভার এবং লো-লেভেল সার্ভার। সাধারণত, আপনি সাধারণ সার্ভার ব্যবহার করে এতে ফিচার যোগ করবেন। তবে কিছু ক্ষেত্রে, আপনাকে লো-লেভেল সার্ভারের উপর নির্ভর করতে হতে পারে, যেমন:

- উন্নত আর্কিটেকচার। সাধারণ সার্ভার এবং লো-লেভেল সার্ভার উভয় ব্যবহার করে একটি পরিষ্কার আর্কিটেকচার তৈরি করা সম্ভব, তবে লো-লেভেল সার্ভার ব্যবহার করলে এটি কিছুটা সহজ হতে পারে।
- ফিচার উপলব্ধতা। কিছু উন্নত ফিচার শুধুমাত্র লো-লেভেল সার্ভারের মাধ্যমে ব্যবহার করা যায়। আপনি পরবর্তী অধ্যায়ে এটি দেখতে পাবেন যখন আমরা স্যাম্পলিং এবং এলিসিটেশন যোগ করব।

## সাধারণ সার্ভার বনাম লো-লেভেল সার্ভার

সাধারণ সার্ভার ব্যবহার করে MCP সার্ভার তৈরি করার উদাহরণ এখানে দেওয়া হলো:

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

এখানে মূল বিষয় হলো, আপনি স্পষ্টভাবে প্রতিটি টুল, রিসোর্স বা প্রম্পট যোগ করেন যা আপনি সার্ভারে রাখতে চান। এতে কোনো সমস্যা নেই।  

### লো-লেভেল সার্ভার পদ্ধতি

তবে, যখন আপনি লো-লেভেল সার্ভার পদ্ধতি ব্যবহার করেন, তখন আপনাকে ভিন্নভাবে চিন্তা করতে হবে। এখানে প্রতিটি ফিচার টাইপ (টুল, রিসোর্স বা প্রম্পট) এর জন্য দুটি হ্যান্ডলার তৈরি করতে হয়। উদাহরণস্বরূপ, টুলের ক্ষেত্রে দুটি ফাংশন থাকে:

- সমস্ত টুল তালিকাভুক্ত করা। একটি ফাংশন সমস্ত টুল তালিকাভুক্ত করার প্রচেষ্টার জন্য দায়ী।
- সমস্ত টুল কল করার হ্যান্ডলিং। এখানে, একটি ফাংশন টুল কল করার অনুরোধ হ্যান্ডল করে।

এটি কি কম কাজের মতো শোনাচ্ছে? তাহলে, টুল রেজিস্টার করার পরিবর্তে, আমাকে শুধু নিশ্চিত করতে হবে যে টুলটি তালিকাভুক্ত হয়েছে এবং এটি কল করার অনুরোধ এলে কার্যকর হচ্ছে। 

চলুন দেখি কোডটি এখন কেমন দেখাচ্ছে:

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

এখানে আমরা একটি ফাংশন তৈরি করেছি যা ফিচারের একটি তালিকা ফেরত দেয়। টুলের তালিকার প্রতিটি এন্ট্রিতে এখন `name`, `description` এবং `inputSchema` এর মতো ফিল্ড রয়েছে যা রিটার্ন টাইপের সাথে সামঞ্জস্যপূর্ণ। এটি আমাদের টুল এবং ফিচার সংজ্ঞা অন্যত্র রাখার সুযোগ দেয়। আমরা এখন আমাদের সমস্ত টুল একটি টুল ফোল্ডারে এবং একইভাবে সমস্ত ফিচার রাখতে পারি, ফলে আমাদের প্রকল্পটি এমনভাবে সংগঠিত হতে পারে:

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

এটি চমৎকার, আমাদের আর্কিটেকচারকে বেশ পরিষ্কার দেখানো যেতে পারে।

টুল কল করার ক্ষেত্রে কী হবে, এটি কি একই ধারণা, একটি হ্যান্ডলার যেকোনো টুল কল করার জন্য? হ্যাঁ, ঠিক তাই। এর কোডটি এখানে দেওয়া হলো:

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

উপরের কোড থেকে দেখা যাচ্ছে, আমাদের টুলটি কল করার জন্য এবং কোন আর্গুমেন্ট দিয়ে কল করা হচ্ছে তা পার্স করতে হবে, তারপর টুলটি কল করার প্রক্রিয়া চালিয়ে যেতে হবে।

## পদ্ধতির উন্নতি: ভ্যালিডেশন যোগ করা

এখন পর্যন্ত, আপনি দেখেছেন কীভাবে টুল, রিসোর্স এবং প্রম্পট যোগ করার জন্য সমস্ত রেজিস্ট্রেশন প্রতিটি ফিচার টাইপের জন্য দুটি হ্যান্ডলার দিয়ে প্রতিস্থাপন করা যায়। এরপর কী করতে হবে? আমাদের কিছু ভ্যালিডেশন যোগ করা উচিত যাতে নিশ্চিত করা যায় যে টুলটি সঠিক আর্গুমেন্ট দিয়ে কল করা হচ্ছে। প্রতিটি রানটাইমের নিজস্ব সমাধান রয়েছে, যেমন Python-এ Pydantic এবং TypeScript-এ Zod ব্যবহার করা হয়। ধারণাটি হলো আমরা নিম্নলিখিত কাজগুলো করি:

- একটি ফিচার (টুল, রিসোর্স বা প্রম্পট) তৈরি করার লজিক তার নির্ধারিত ফোল্ডারে সরিয়ে নেওয়া।
- একটি ইনকামিং অনুরোধ যাচাই করার উপায় যোগ করা, যেমন টুল কল করার অনুরোধ।

### একটি ফিচার তৈরি করা

একটি ফিচার তৈরি করতে, আমাদের সেই ফিচারের জন্য একটি ফাইল তৈরি করতে হবে এবং নিশ্চিত করতে হবে যে এতে সেই ফিচারের জন্য প্রয়োজনীয় ফিল্ডগুলো রয়েছে। টুল, রিসোর্স এবং প্রম্পটের ক্ষেত্রে ফিল্ডগুলো কিছুটা ভিন্ন।

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

এখানে আপনি দেখতে পাচ্ছেন আমরা কীভাবে নিম্নলিখিত কাজগুলো করি:

- *schema.py* ফাইলে Pydantic `AddInputModel` ব্যবহার করে `a` এবং `b` ফিল্ড সহ একটি স্কিমা তৈরি করা।
- ইনকামিং অনুরোধকে `AddInputModel` টাইপে পার্স করার চেষ্টা করা। যদি প্যারামিটারে কোনো অসঙ্গতি থাকে, এটি ক্র্যাশ করবে:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

আপনি এই পার্সিং লজিকটি টুল কলের মধ্যে বা হ্যান্ডলার ফাংশনে রাখতে পারেন।

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

- সমস্ত টুল কলের জন্য হ্যান্ডলারে, আমরা এখন ইনকামিং অনুরোধকে টুলের সংজ্ঞায়িত স্কিমায় পার্স করার চেষ্টা করি:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    যদি এটি কাজ করে, তাহলে আমরা প্রকৃত টুলটি কল করার দিকে এগিয়ে যাই:

    ```typescript
    const result = await tool.callback(input);
    ```

যেমনটি আপনি দেখতে পাচ্ছেন, এই পদ্ধতি একটি চমৎকার আর্কিটেকচার তৈরি করে যেখানে সবকিছু তার জায়গায় থাকে। *server.ts* একটি খুব ছোট ফাইল যা শুধুমাত্র অনুরোধ হ্যান্ডলার সেটআপ করে এবং প্রতিটি ফিচার তাদের নিজ নিজ ফোল্ডারে থাকে, যেমন tools/, resources/ বা prompts/।

চমৎকার, চলুন এটি তৈরি করার চেষ্টা করি।

## অনুশীলন: একটি লো-লেভেল সার্ভার তৈরি করা

এই অনুশীলনে, আমরা নিম্নলিখিত কাজগুলো করব:

1. টুল তালিকাভুক্ত করা এবং টুল কল করার জন্য একটি লো-লেভেল সার্ভার তৈরি করা।
1. একটি আর্কিটেকচার বাস্তবায়ন করা যা আপনি তৈরি করতে পারেন।
1. নিশ্চিত করা যে আপনার টুল কল সঠিকভাবে যাচাই করা হচ্ছে।

### -1- একটি আর্কিটেকচার তৈরি করা

প্রথমে আমাদের একটি আর্কিটেকচার ঠিক করতে হবে যা আমাদের আরও ফিচার যোগ করার সাথে সাথে স্কেল করতে সাহায্য করবে। এটি দেখতে এমন হবে:

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

এখন আমরা একটি আর্কিটেকচার সেটআপ করেছি যা নিশ্চিত করে যে আমরা সহজেই টুল ফোল্ডারে নতুন টুল যোগ করতে পারি। রিসোর্স এবং প্রম্পটের জন্য সাবডিরেক্টরি যোগ করতে চাইলে এটি অনুসরণ করতে পারেন।

### -2- একটি টুল তৈরি করা

চলুন দেখি একটি টুল তৈরি করা কেমন দেখায়। প্রথমে এটি তার *tool* সাবডিরেক্টরিতে তৈরি করতে হবে, যেমন:

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

এখানে আমরা দেখতে পাচ্ছি কীভাবে আমরা নাম, বিবরণ, Pydantic ব্যবহার করে একটি ইনপুট স্কিমা এবং একটি হ্যান্ডলার সংজ্ঞায়িত করি যা এই টুলটি কল করার সময় কার্যকর হবে। শেষে, আমরা `tool_add` প্রকাশ করি যা এই সমস্ত প্রপার্টি ধারণ করে একটি ডিকশনারি।

এছাড়াও *schema.py* ব্যবহার করা হয় আমাদের টুলের ইনপুট স্কিমা সংজ্ঞায়িত করতে:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

আমাদের *__init__.py* ফাইলটি পূরণ করতে হবে যাতে টুল ডিরেক্টরিটি একটি মডিউল হিসেবে বিবেচিত হয়। এছাড়াও, আমাদের এর মধ্যে থাকা মডিউলগুলো প্রকাশ করতে হবে, যেমন:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

আমরা আরও টুল যোগ করার সাথে সাথে এই ফাইলটি আপডেট করতে পারি।

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

এখানে আমরা একটি ডিকশনারি তৈরি করি যা নিম্নলিখিত প্রপার্টি ধারণ করে:

- name, এটি টুলের নাম।
- rawSchema, এটি Zod স্কিমা, এটি ইনকামিং অনুরোধ যাচাই করতে ব্যবহার করা হবে।
- inputSchema, এই স্কিমা হ্যান্ডলার দ্বারা ব্যবহার করা হবে।
- callback, এটি টুল কার্যকর করতে ব্যবহার করা হবে।

এছাড়াও `Tool` ব্যবহার করা হয় এই ডিকশনারিকে একটি টাইপে রূপান্তর করতে যা MCP সার্ভার হ্যান্ডলার গ্রহণ করতে পারে এবং এটি দেখতে এমন:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

এবং *schema.ts* যেখানে আমরা প্রতিটি টুলের ইনপুট স্কিমা সংরক্ষণ করি, এটি দেখতে এমন:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

চমৎকার, চলুন আমাদের টুল তালিকাভুক্ত করার কাজটি পরবর্তী ধাপে নিয়ে যাই।

### -3- টুল তালিকাভুক্ত করা হ্যান্ডল করা

পরবর্তী ধাপে, আমাদের টুল তালিকাভুক্ত করার জন্য একটি অনুরোধ হ্যান্ডলার সেটআপ করতে হবে। আমাদের সার্ভার ফাইলে এটি যোগ করতে হবে:

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

এখানে আমরা `@server.list_tools` ডেকোরেটর এবং `handle_list_tools` ইমপ্লিমেন্টিং ফাংশন যোগ করি। পরেরটিতে, আমাদের টুলের একটি তালিকা তৈরি করতে হবে। লক্ষ্য করুন প্রতিটি টুলে `name`, `description` এবং `inputSchema` থাকতে হবে।  

**TypeScript**

টুল তালিকাভুক্ত করার জন্য অনুরোধ হ্যান্ডলার সেটআপ করতে, আমাদের সার্ভারে `setRequestHandler` কল করতে হবে একটি স্কিমা সহ যা আমরা করতে চাই, এই ক্ষেত্রে `ListToolsRequestSchema`।

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

চমৎকার, এখন আমরা টুল তালিকাভুক্ত করার অংশটি সমাধান করেছি। চলুন টুল কল করার অংশটি দেখি।

### -4- টুল কল করা হ্যান্ডল করা

টুল কল করতে, আমাদের আরেকটি অনুরোধ হ্যান্ডলার সেটআপ করতে হবে, এইবার একটি অনুরোধের সাথে কাজ করার জন্য যা নির্দিষ্ট করে কোন ফিচার কল করতে হবে এবং কোন আর্গুমেন্ট দিয়ে।

**Python**

চলুন `@server.call_tool` ডেকোরেটর ব্যবহার করি এবং এটি `handle_call_tool` ফাংশন দিয়ে ইমপ্লিমেন্ট করি। সেই ফাংশনের মধ্যে, আমাদের টুলের নাম, এর আর্গুমেন্ট এবং নিশ্চিত করতে হবে যে আর্গুমেন্টগুলো সংশ্লিষ্ট টুলের জন্য বৈধ। আমরা এই ফাংশনে বা ডাউনস্ট্রিমে টুলে আর্গুমেন্ট যাচাই করতে পারি।

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

এখানে যা ঘটছে:

- আমাদের টুলের নাম ইতিমধ্যেই ইনপুট প্যারামিটার `name` হিসেবে উপস্থিত, যা আমাদের আর্গুমেন্টের জন্যও সত্য `arguments` ডিকশনারি আকারে।

- টুলটি `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` দিয়ে কল করা হয়। আর্গুমেন্ট যাচাই `handler` প্রপার্টিতে ঘটে যা একটি ফাংশনের দিকে নির্দেশ করে। যদি এটি ব্যর্থ হয়, এটি একটি এক্সসেপশন তুলবে। 

এখানে, এখন আমরা টুল তালিকাভুক্ত করা এবং লো-লেভেল সার্ভার ব্যবহার করে টুল কল করার সম্পূর্ণ ধারণা বুঝতে পারি।

সম্পূর্ণ উদাহরণটি [এখানে](./code/README.md) দেখুন।

## অ্যাসাইনমেন্ট

আপনাকে দেওয়া কোডটি প্রসারিত করুন এবং একাধিক টুল, রিসোর্স এবং প্রম্পট যোগ করুন। লক্ষ্য করুন যে আপনি শুধুমাত্র টুল ডিরেক্টরিতে ফাইল যোগ করতে হবে এবং অন্য কোথাও নয়। 

*কোনো সমাধান দেওয়া হয়নি*

## সারসংক্ষেপ

এই অধ্যায়ে, আমরা দেখেছি কীভাবে লো-লেভেল সার্ভার পদ্ধতি কাজ করে এবং এটি কীভাবে আমাদের একটি সুন্দর আর্কিটেকচার তৈরি করতে সাহায্য করে যা আমরা ক্রমাগত তৈরি করতে পারি। আমরা ভ্যালিডেশন নিয়ে আলোচনা করেছি এবং আপনাকে দেখানো হয়েছে কীভাবে ইনপুট যাচাই করার জন্য ভ্যালিডেশন লাইব্রেরি ব্যবহার করে স্কিমা তৈরি করতে হয়।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।