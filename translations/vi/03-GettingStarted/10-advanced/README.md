# Sử dụng máy chủ nâng cao

Có hai loại máy chủ khác nhau được cung cấp trong MCP SDK, máy chủ thông thường và máy chủ cấp thấp. Thông thường, bạn sẽ sử dụng máy chủ thông thường để thêm các tính năng. Tuy nhiên, trong một số trường hợp, bạn sẽ muốn dựa vào máy chủ cấp thấp như:

- Kiến trúc tốt hơn. Có thể tạo kiến trúc sạch với cả máy chủ thông thường và máy chủ cấp thấp nhưng có thể nói rằng điều đó dễ dàng hơn một chút với máy chủ cấp thấp.
- Tính năng có sẵn. Một số tính năng nâng cao chỉ có thể sử dụng với máy chủ cấp thấp. Bạn sẽ thấy điều này trong các chương sau khi chúng ta thêm sampling và elicitation.

## Máy chủ thông thường so với máy chủ cấp thấp

Đây là cách tạo một MCP Server với máy chủ thông thường

**Python**

```python
mcp = FastMCP("Demo")

# Thêm một công cụ phép cộng
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

// Thêm một công cụ phép cộng
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

Ý tưởng là bạn rõ ràng thêm từng công cụ, tài nguyên hoặc prompt mà bạn muốn máy chủ có. Không có gì sai với điều đó.

### Cách tiếp cận với máy chủ cấp thấp

Tuy nhiên, khi bạn sử dụng cách tiếp cận máy chủ cấp thấp, bạn cần suy nghĩ khác đi. Thay vì đăng ký từng công cụ, bạn tạo hai bộ xử lý cho mỗi loại tính năng (tools, resources hoặc prompts). Ví dụ như công cụ chỉ có hai hàm như sau:

- Liệt kê tất cả công cụ. Một hàm sẽ chịu trách nhiệm cho tất cả các yêu cầu liệt kê công cụ.
- Xử lý gọi tất cả công cụ. Ở đây cũng chỉ có một hàm xử lý các lời gọi tới một công cụ.

Nghe có vẻ ít công việc hơn đúng không? Thay vì đăng ký một công cụ, tôi chỉ cần đảm bảo công cụ được liệt kê khi tôi liệt kê tất cả công cụ và được gọi khi có yêu cầu gọi công cụ.

Hãy xem mã bây giờ như thế nào:

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

Ở đây chúng ta có một hàm trả về danh sách các tính năng. Mỗi mục trong danh sách công cụ hiện có các trường như `name`, `description` và `inputSchema` để tuân thủ kiểu trả về. Điều này cho phép chúng ta đặt định nghĩa công cụ và tính năng ở nơi khác. Bây giờ ta có thể tạo tất cả công cụ trong thư mục tools và tương tự với tất cả tính năng của bạn để dự án đột nhiên được tổ chức như sau:

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

Thật tuyệt, kiến trúc của chúng ta có thể được làm cho trông khá gọn gàng.

Còn việc gọi công cụ thì sao, có phải cũng là ý tưởng đó, một bộ xử lý gọi một công cụ, bất kể công cụ nào? Đúng rồi, đây là mã cho việc đó:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools là một từ điển với các tên công cụ là khóa
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

Như bạn có thể thấy trong mã trên, chúng ta cần phân tích để lấy công cụ cần gọi, và với các tham số nào, rồi sau đó gọi công cụ đó.

## Cải thiện cách tiếp cận với xác thực

Cho đến nay, bạn đã thấy cách tất cả các đăng ký để thêm công cụ, tài nguyên và prompt có thể được thay thế bằng hai bộ xử lý cho mỗi loại tính năng. Còn điều gì khác cần làm? Chúng ta nên thêm một số dạng xác thực để đảm bảo công cụ được gọi với các tham số đúng. Mỗi runtime có giải pháp riêng cho điều này, ví dụ Python dùng Pydantic và TypeScript dùng Zod. Ý tưởng là chúng ta làm như sau:

- Di chuyển logic tạo tính năng (công cụ, tài nguyên hoặc prompt) vào thư mục riêng của nó.
- Thêm cách để xác thực một yêu cầu đầu vào, ví dụ như gọi một công cụ.

### Tạo một tính năng

Để tạo một tính năng, chúng ta sẽ cần tạo một file cho tính năng đó và đảm bảo nó có các trường bắt buộc của tính năng. Các trường này khác nhau một chút giữa công cụ, tài nguyên và prompt.

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
        # Xác thực đầu vào bằng mô hình Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: thêm Pydantic, để chúng ta có thể tạo AddInputModel và xác thực các đối số

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ở đây bạn có thể thấy cách chúng ta làm như sau:

- Tạo schema với Pydantic `AddInputModel` có các trường `a` và `b` trong file *schema.py*.
- Cố gắng phân tích yêu cầu đầu vào thành kiểu `AddInputModel`, nếu có sự không phù hợp tham số thì sẽ gây lỗi:

   ```python
   # add.py
    try:
        # Xác thực đầu vào bằng mô hình Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Bạn có thể chọn đặt logic phân tích này trong lời gọi công cụ hoặc trong hàm bộ xử lý.

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

- Trong bộ xử lý xử lý tất cả các lời gọi công cụ, bây giờ chúng ta cố gắng phân tích yêu cầu đầu vào thành schema định nghĩa cho công cụ:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    nếu điều đó thành công thì ta tiếp tục gọi công cụ thực tế:

    ```typescript
    const result = await tool.callback(input);
    ```

Như bạn thấy, cách tiếp cận này tạo ra kiến trúc tuyệt vời vì mọi thứ đều có chỗ riêng, *server.ts* là một file rất nhỏ chỉ để kết nối các bộ xử lý yêu cầu và mỗi tính năng trong thư mục tương ứng của nó như tools/, resources/ hoặc prompts/.

Tuyệt vời, hãy thử xây dựng điều này tiếp theo.

## Bài tập: Tạo máy chủ cấp thấp

Trong bài tập này, chúng ta sẽ làm những việc sau:

1. Tạo một máy chủ cấp thấp xử lý liệt kê công cụ và gọi công cụ.
1. Triển khai kiến trúc mà bạn có thể xây dựng thêm.
1. Thêm xác thực để đảm bảo các lời gọi công cụ của bạn được xác thực đúng cách.

### -1- Tạo một kiến trúc

Điều đầu tiên cần làm là một kiến trúc giúp ta mở rộng khi thêm nhiều tính năng hơn, nó trông như sau:

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

Bây giờ chúng ta đã thiết lập kiến trúc đảm bảo có thể dễ dàng thêm các công cụ mới trong thư mục tools. Bạn có thể theo đó để thêm các thư mục con cho resources và prompts.

### -2- Tạo một công cụ

Hãy xem việc tạo một công cụ trông như thế nào. Đầu tiên, nó cần được tạo trong thư mục con *tool* như sau:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Xác thực đầu vào bằng cách sử dụng mô hình Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: thêm Pydantic, để chúng ta có thể tạo AddInputModel và xác thực các đối số

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Ở đây ta thấy cách định nghĩa tên, mô tả và schema đầu vào dùng Pydantic cùng bộ xử lý được gọi khi công cụ được gọi. Cuối cùng, ta công khai `tool_add` là một dictionary chứa tất cả thuộc tính này.

Còn có *schema.py* được dùng để định nghĩa schema đầu vào cho công cụ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Ta cũng cần bổ sung *__init__.py* để đảm bảo thư mục tools được coi là một module. Ngoài ra, cần công khai các module trong đó như sau:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Chúng ta có thể tiếp tục bổ sung file này khi thêm các công cụ mới.

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

Ở đây ta tạo một dictionary gồm các thuộc tính:

- name, tên công cụ.
- rawSchema, schema Zod dùng để xác thực các yêu cầu gọi công cụ này.
- inputSchema, schema này sẽ được dùng bởi handler.
- callback, dùng để gọi công cụ.

Còn có `Tool` dùng để chuyển dictionary này thành kiểu mà bộ xử lý mcp server có thể chấp nhận, nhìn như sau:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Và có *schema.ts* nơi ta lưu các schemas đầu vào cho từng công cụ, hiện tại chỉ có một schema nhưng khi thêm công cụ ta có thể thêm nhiều mục hơn:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Tuyệt vời, giờ hãy tiếp tục xử lý việc liệt kê các công cụ.

### -3- Xử lý liệt kê công cụ

Tiếp theo, để xử lý liệt kê công cụ, ta cần thiết lập một bộ xử lý yêu cầu cho việc đó. Đây là những gì cần thêm vào file server:

**Python**

```python
# mã nguồn bị bỏ qua cho gọn gàng
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

Ở đây, ta thêm decorator `@server.list_tools` cùng hàm triển khai `handle_list_tools`. Trong hàm này, ta cần tạo ra một danh sách công cụ. Lưu ý mỗi công cụ cần có tên, mô tả và inputSchema.

**TypeScript**

Để thiết lập bộ xử lý yêu cầu liệt kê công cụ, ta gọi `setRequestHandler` trên server với một schema phù hợp với tác vụ ta muốn làm, trong trường hợp này là `ListToolsRequestSchema`.

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
// mã đã bị bỏ qua để ngắn gọn
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Trả về danh sách các công cụ đã đăng ký
  return {
    tools: tools
  };
});
```

Tuyệt vời, giờ ta đã xong phần liệt kê công cụ, tiếp theo hãy xem cách gọi công cụ.

### -4- Xử lý gọi công cụ

Để gọi công cụ, ta cần thiết lập một bộ xử lý yêu cầu nữa, lần này tập trung vào xử lý một yêu cầu chỉ rõ công cụ cần gọi và với tham số nào.

**Python**

Hãy dùng decorator `@server.call_tool` và triển khai với hàm như `handle_call_tool`. Trong hàm này, ta cần phân tích tên công cụ, tham số và đảm bảo tham số hợp lệ cho công cụ đó. Ta có thể xác thực tham số trong hàm này hoặc ngay trong công cụ thực tế.

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

- Tên công cụ đã có trong tham số đầu vào `name`, và tham số `arguments` là một dictionary tham số cho công cụ.

- Công cụ được gọi với `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Việc xác thực tham số diễn ra trong thuộc tính `handler` trỏ tới một hàm, nếu thất bại sẽ ném ra ngoại lệ.

Vậy là ta đã hiểu rõ cách liệt kê và gọi công cụ dùng máy chủ cấp thấp.

Xem [ví dụ đầy đủ](./code/README.md) tại đây

## Bài tập

Mở rộng mã bạn đã có với một số công cụ, tài nguyên và prompt và nhận thấy bạn chỉ cần thêm các files trong thư mục tools và không cần ở chỗ khác.

*Không có đáp án*

## Tóm tắt

Trong chương này, ta đã thấy cách hoạt động của cách tiếp cận máy chủ cấp thấp và cách nó giúp ta tạo ra kiến trúc đẹp mà ta có thể tiếp tục xây dựng. Ta cũng bàn về xác thực và bạn được hướng dẫn cách làm việc với các thư viện xác thực để tạo schema cho việc xác thực đầu vào.

## Tiếp theo

- Tiếp theo: [Xác thực đơn giản](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn thông tin chính thống. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu nhầm hoặc hiểu sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->