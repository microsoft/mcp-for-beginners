# Sử dụng máy chủ nâng cao

Có hai loại máy chủ khác nhau được cung cấp trong MCP SDK, máy chủ thông thường và máy chủ cấp thấp. Thông thường, bạn sẽ sử dụng máy chủ thông thường để thêm tính năng. Tuy nhiên, trong một số trường hợp bạn muốn dựa vào máy chủ cấp thấp như:

- Kiến trúc tốt hơn. Có thể tạo một kiến trúc sạch với cả máy chủ thông thường và máy chủ cấp thấp nhưng có thể nói rằng nó hơi dễ hơn một chút với máy chủ cấp thấp.
- Tính năng có sẵn. Một số tính năng nâng cao chỉ có thể sử dụng với máy chủ cấp thấp. Bạn sẽ thấy điều này trong các chương sau khi chúng ta thêm sampling và elicitation.

## Máy chủ thông thường vs máy chủ cấp thấp

Đây là cách tạo một MCP Server với máy chủ thông thường

**Python**

```python
mcp = FastMCP("Demo")

# Thêm một công cụ cộng
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

// Thêm một công cụ cộng
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

Ý tưởng là bạn thêm rõ ràng từng công cụ, tài nguyên hoặc prompt mà bạn muốn máy chủ có. Không có gì sai với điều đó.

### Phương pháp máy chủ cấp thấp

Tuy nhiên, khi bạn sử dụng phương pháp máy chủ cấp thấp bạn cần suy nghĩ khác đi. Thay vì đăng ký từng công cụ, bạn thay vào đó tạo hai trình xử lý cho mỗi loại tính năng (công cụ, tài nguyên hoặc prompt). Ví dụ, công cụ chỉ có hai chức năng như sau:

- Liệt kê tất cả công cụ. Một chức năng sẽ chịu trách nhiệm cho mọi cố gắng liệt kê các công cụ.
- Xử lý gọi tất cả các công cụ. Ở đây cũng vậy, chỉ có một chức năng xử lý các cuộc gọi đến một công cụ.

Nghe có vẻ ít công việc hơn phải không? Vì vậy thay vì đăng ký một công cụ, tôi chỉ cần đảm bảo công cụ đó được liệt kê khi tôi liệt kê tất cả công cụ và nó được gọi khi có yêu cầu gọi công cụ đến.

Hãy xem bây giờ mã trông như thế nào:

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
  // Trả về danh sách các công cụ đã đăng ký
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

Ở đây bây giờ chúng ta có một hàm trả về danh sách các tính năng. Mỗi mục trong danh sách công cụ hiện có các trường như `name`, `description` và `inputSchema` để tuân thủ kiểu trả về. Điều này cho phép chúng ta đặt công cụ và định nghĩa tính năng ở nơi khác. Bây giờ chúng ta có thể tạo tất cả công cụ trong thư mục tools và tương tự cho tất cả tính năng để dự án của bạn đột nhiên được tổ chức như sau:

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

Thật tuyệt, kiến trúc của chúng ta có thể được làm cho khá gọn gàng.

Còn việc gọi công cụ thì sao, có phải cũng ý tưởng đó, một trình xử lý gọi một công cụ, bất kỳ công cụ nào? Đúng vậy, đây là mã cho việc đó:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools là một từ điển với tên công cụ làm khóa
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
    // TODO gọi công cụ,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Như bạn có thể thấy từ mã trên, chúng ta cần phân tích công cụ được gọi, và với các đối số gì, rồi sau đó cần tiến hành gọi công cụ.

## Cải thiện phương pháp với việc xác thực

Cho đến nay, bạn đã thấy tất cả việc đăng ký để thêm công cụ, tài nguyên và prompt có thể được thay thế bằng hai trình xử lý này cho mỗi loại tính năng. Vậy chúng ta cần làm gì nữa? Chúng ta nên thêm một hình thức xác thực để đảm bảo công cụ được gọi với các đối số đúng. Mỗi runtime có giải pháp riêng cho điều này, ví dụ Python sử dụng Pydantic và TypeScript sử dụng Zod. Ý tưởng là chúng ta làm như sau:

- Chuyển logic tạo tính năng (công cụ, tài nguyên hoặc prompt) sang thư mục riêng của nó.
- Thêm cách để xác thực yêu cầu đến ví dụ như gọi một công cụ.

### Tạo một tính năng

Để tạo một tính năng, chúng ta cần tạo một file cho tính năng đó và đảm bảo nó có các trường bắt buộc cần thiết của tính năng. Các trường khác nhau một chút giữa công cụ, tài nguyên và prompt.

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
        # Xác thực đầu vào sử dụng mô hình Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: thêm Pydantic, để chúng ta có thể tạo một AddInputModel và xác thực các đối số

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ở đây bạn có thể thấy cách ta làm như sau:

- Tạo một schema bằng Pydantic `AddInputModel` với các trường `a` và `b` trong file *schema.py*.
- Cố gắng phân tích yêu cầu đến thành kiểu `AddInputModel`, nếu có sự không khớp trong tham số thì sẽ gây lỗi:

   ```python
   # add.py
    try:
        # Xác thực đầu vào sử dụng mô hình Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Bạn có thể chọn đặt logic phân tích này trong chính cuộc gọi công cụ hoặc trong hàm trình xử lý.

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

- Trong trình xử lý xử lý tất cả cuộc gọi công cụ, chúng ta cố gắng phân tích yêu cầu đến thành schema đã định nghĩa của công cụ:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    nếu thành công thì chúng ta tiếp tục gọi công cụ thật:

    ```typescript
    const result = await tool.callback(input);
    ```

Như bạn thấy, phương pháp này tạo ra một kiến trúc tuyệt vời khi mọi thứ đều có chỗ của nó, *server.ts* là một file rất nhỏ chỉ nối các trình xử lý yêu cầu và mỗi tính năng nằm trong thư mục riêng của nó, ví dụ tools/, resources/ hoặc prompts/.

Tuyệt, hãy thử xây dựng điều này tiếp theo.

## Bài tập: Tạo một máy chủ cấp thấp

Trong bài tập này, chúng ta sẽ làm những việc sau:

1. Tạo một máy chủ cấp thấp xử lý liệt kê công cụ và gọi công cụ.
1. Triển khai kiến trúc bạn có thể xây dựng tiếp.
1. Thêm xác thực để đảm bảo các cuộc gọi công cụ của bạn được xác thực đúng.

### -1- Tạo kiến trúc

Điều đầu tiên cần giải quyết là một kiến trúc giúp chúng ta mở rộng khi thêm nhiều tính năng hơn, trông như sau:

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

Bây giờ chúng ta đã thiết lập một kiến trúc đảm bảo chúng ta có thể dễ dàng thêm công cụ mới trong thư mục tools. Bạn có thể theo dõi để thêm thư mục con cho resources và prompts.

### -2- Tạo một công cụ

Hãy xem việc tạo một công cụ như thế nào. Đầu tiên nó cần được tạo trong thư mục con *tool* như sau:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Xác thực đầu vào sử dụng mô hình Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: thêm Pydantic, để chúng ta có thể tạo AddInputModel và xác thực các tham số đầu vào

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Bạn thấy cách chúng ta định nghĩa tên, mô tả và input schema sử dụng Pydantic và một trình xử lý sẽ được gọi khi công cụ này được gọi. Cuối cùng, chúng ta cung cấp `tool_add` là một dictionary chứa tất cả các thuộc tính này.

Cũng có *schema.py* để định nghĩa input schema dùng cho công cụ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Chúng ta cũng cần điền *__init__.py* để đảm bảo thư mục tools được coi là một module. Thêm vào đó, cần công khai các module bên trong như sau:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Chúng ta có thể tiếp tục thêm vào file này khi thêm các công cụ khác.

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

Ở đây chúng ta tạo một đối tượng gồm các thuộc tính:

- name, tên của công cụ.
- rawSchema, schema Zod, dùng để xác thực các yêu cầu gọi công cụ này.
- inputSchema, schema này sẽ được trình xử lý dùng.
- callback, dùng để gọi công cụ.

Cũng có `Tool` dùng để chuyển dictionary này thành kiểu mà trình xử lý MCP server có thể chấp nhận như sau:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Và có *schema.ts* nơi chúng ta lưu các input schemas cho mỗi công cụ, hiện tại chỉ có một schema nhưng khi thêm nhiều công cụ ta có thể thêm nhiều mục hơn:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Tuyệt, hãy tiếp tục xử lý việc liệt kê công cụ của chúng ta.

### -3- Xử lý liệt kê công cụ

Tiếp theo, để xử lý việc liệt kê công cụ, chúng ta cần thiết lập một trình xử lý yêu cầu. Đây là những gì cần thêm vào file server:

**Python**

```python
# mã đã được lược bỏ để ngắn gọn
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

Ở đây, chúng ta thêm decorator `@server.list_tools` và hàm thực thi `handle_list_tools`. Trong hàm này, chúng ta cần tạo danh sách công cụ. Lưu ý mỗi công cụ cần có tên, mô tả và inputSchema.

**TypeScript**

Để thiết lập trình xử lý yêu cầu liệt kê công cụ, chúng ta gọi `setRequestHandler` trên server với schema phù hợp với yêu cầu, ở đây là `ListToolsRequestSchema`.

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
// mã bị bỏ qua để ngắn gọn
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Trả về danh sách các công cụ đã đăng ký
  return {
    tools: tools
  };
});
```

Tuyệt, giờ chúng ta đã giải quyết phần liệt kê công cụ, cùng xem cách gọi công cụ tiếp theo.

### -4- Xử lý gọi công cụ

Để gọi công cụ, chúng ta cần thiết lập một trình xử lý yêu cầu khác, lần này tập trung xử lý yêu cầu chỉ định tính năng nào được gọi và với đối số gì.

**Python**

Chúng ta dùng decorator `@server.call_tool` và triển khai với hàm như `handle_call_tool`. Bên trong hàm, ta cần phân tích tên công cụ, đối số và đảm bảo đối số hợp lệ với công cụ đó. Ta có thể xác thực đối số trong hàm này hoặc bên trong công cụ.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools là một từ điển với tên công cụ làm khóa
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # gọi công cụ
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Đây là những gì xảy ra:

- Tên công cụ đã có sẵn dưới dạng tham số `name`, còn đối số là trong dictionary `arguments`.

- Công cụ được gọi với `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Việc xác thực đối số xảy ra trong thuộc tính `handler` trỏ tới một hàm, nếu không hợp lệ sẽ gây ngoại lệ.

Vậy là, ta đã hiểu đầy đủ về cách liệt kê và gọi công cụ sử dụng máy chủ cấp thấp.

Xem [ví dụ đầy đủ](./code/README.md) tại đây

## Bài tập

Mở rộng mã bạn đã được cung cấp với một số công cụ, tài nguyên và prompt và suy ngẫm về việc bạn chỉ cần thêm các file trong thư mục tools mà không phải chỗ khác.

*Không có giải pháp cung cấp*

## Tóm tắt

Trong chương này, chúng ta đã thấy cách phương pháp máy chủ cấp thấp hoạt động và cách nó giúp ta tạo một kiến trúc đẹp có thể tiếp tục xây dựng. Chúng ta cũng đã thảo luận về xác thực và bạn được hướng dẫn cách làm việc với thư viện xác thực để tạo schema cho xác thực input.

## Tiếp theo

- Tiếp theo: [Xác thực đơn giản](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn đáng tin cậy nhất. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->