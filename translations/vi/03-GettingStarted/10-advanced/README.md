# Sử dụng máy chủ nâng cao

Có hai loại máy chủ khác nhau được cung cấp trong MCP SDK, máy chủ thông thường và máy chủ cấp thấp. Thông thường, bạn sẽ sử dụng máy chủ thông thường để thêm các tính năng cho nó. Tuy nhiên trong một số trường hợp, bạn muốn dựa vào máy chủ cấp thấp như:

- Kiến trúc tốt hơn. Có thể tạo một kiến trúc sạch với cả máy chủ thông thường và máy chủ cấp thấp nhưng có thể lập luận rằng nó hơi dễ dàng hơn với máy chủ cấp thấp.
- Khả năng tính năng. Một số tính năng nâng cao chỉ có thể sử dụng với
    máy chủ cấp thấp. Các chương sau sẽ đề cập đến Elicitation và tính năng Sampling kế thừa,
    tính năng này bị ngừng sử dụng trong MCP `2026-07-28`.

## Máy chủ thông thường vs máy chủ cấp thấp

Đây là cách tạo một MCP Server với máy chủ thông thường

**Python**

```python
mcp = FastMCP("Demo")

# Thêm một công cụ cộng thêm
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

Ý chính là bạn thêm rõ ràng từng công cụ, tài nguyên hoặc prompt mà bạn muốn máy chủ có. Không có gì sai với điều đó.  

### Cách tiếp cận máy chủ cấp thấp

Tuy nhiên, khi sử dụng cách tiếp cận máy chủ cấp thấp bạn cần suy nghĩ khác đi. Thay vì đăng ký từng công cụ, bạn thay vào đó tạo hai handler cho mỗi loại tính năng (công cụ, tài nguyên hoặc prompt). Ví dụ như công cụ sẽ có hai hàm như sau:

- Liệt kê tất cả công cụ. Một hàm chịu trách nhiệm cho tất cả các lần cố gắng liệt kê công cụ.
- Xử lý gọi tất cả công cụ. Ở đây cũng chỉ có một hàm xử lý gọi đến một công cụ

Nghe có vẻ công việc ít hơn đúng không? Vậy thay vì đăng ký một công cụ, tôi chỉ cần đảm bảo công cụ được liệt kê khi tôi liệt kê tất cả công cụ và nó được gọi khi có yêu cầu gọi một công cụ. 

Hãy xem mã lúc này trông như thế nào:

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

Đây bây giờ chúng ta có một hàm trả về danh sách các tính năng. Mỗi mục trong danh sách công cụ hiện có các trường như `name`, `description` và `inputSchema` để tuân theo kiểu trả về. Điều này cho phép chúng ta đặt công cụ và định nghĩa tính năng ở nơi khác. Chúng ta giờ có thể tạo tất cả công cụ trong một thư mục tools và tương tự cho tất cả tính năng của bạn, dự án của bạn có thể được tổ chức như sau:

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

Thật tuyệt, kiến trúc của chúng ta có thể được tạo ra khá sạch sẽ.

Còn việc gọi công cụ thì sao, có phải ý tưởng giống nhau không, một handler để gọi một công cụ, bất kể công cụ nào? Đúng rồi, đây là mã cho việc đó:

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

Như bạn thấy trong mã trên, chúng ta cần phân tích công cụ để gọi và các đối số với nó, rồi sau đó tiến hành gọi công cụ.

## Cải thiện cách tiếp cận với xác thực

Cho đến nay, bạn đã thấy cách tất cả các đăng ký để thêm công cụ, tài nguyên và prompt có thể được thay thế bằng hai handler cho mỗi loại tính năng. Vậy còn gì chúng ta cần làm? Chúng ta nên thêm một hình thức xác thực để đảm bảo công cụ được gọi với các đối số đúng. Mỗi runtime có giải pháp riêng cho việc này, ví dụ Python sử dụng Pydantic và TypeScript sử dụng Zod. Ý tưởng là chúng ta làm như sau:

- Di chuyển logic tạo một tính năng (công cụ, tài nguyên hoặc prompt) vào thư mục riêng biệt của nó.
- Thêm cách để xác thực yêu cầu đến ví dụ gọi một công cụ.

### Tạo một tính năng

Để tạo một tính năng, chúng ta sẽ cần tạo một tệp cho tính năng đó và đảm bảo nó có các trường bắt buộc cần thiết cho tính năng đó. Các trường khác nhau một chút giữa công cụ, tài nguyên và prompt.

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

ở đây bạn có thể thấy cách chúng ta làm như sau:

- Tạo một schema dùng Pydantic `AddInputModel` với các trường `a` và `b` trong tệp *schema.py*.
- Cố gắng phân tích yêu cầu đến thành kiểu `AddInputModel`, nếu có sự không khớp tham số thì sẽ gây lỗi:

   ```python
   # add.py
    try:
        # Xác thực đầu vào sử dụng mô hình Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Bạn có thể chọn đặt logic phân tích này trong chính hàm gọi công cụ hoặc trong hàm handler.

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

- Trong handler xử lý tất cả các lần gọi công cụ, giờ ta cố gắng phân tích yêu cầu đến thành theo schema đã định nghĩa của công cụ:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    nếu thành công thì ta tiếp tục gọi công cụ thực tế:

    ```typescript
    const result = await tool.callback(input);
    ```

Như bạn thấy, cách tiếp cận này tạo ra một kiến trúc tuyệt vời vì mọi thứ đều có chỗ của nó, tệp *server.ts* rất nhỏ chỉ để kết nối các handler yêu cầu và mỗi tính năng nằm trong thư mục riêng của nó ví dụ tools/, resources/ hoặc prompts/.

Tuyệt vời, hãy thử xây dựng tiếp theo sau đây. 

## Bài tập: Tạo máy chủ cấp thấp

Trong bài tập này, chúng ta sẽ làm những việc sau:

1. Tạo một máy chủ cấp thấp xử lý liệt kê công cụ và gọi công cụ.
1. Triển khai một kiến trúc bạn có thể phát triển tiếp.
1. Thêm xác thực để đảm bảo các lần gọi công cụ được xác thực đúng cách.

### -1- Tạo kiến trúc

Điều đầu tiên chúng ta cần giải quyết là kiến trúc giúp ta dễ mở rộng khi thêm nhiều tính năng, đây là cách nó trông như sau:

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

Giờ ta đã thiết lập kiến trúc đảm bảo ta có thể dễ dàng thêm công cụ mới trong thư mục tools. Bạn có thể theo cách này để thêm thư mục con cho resources và prompts.

### -2- Tạo công cụ

Tiếp theo, hãy xem việc tạo một công cụ trông như thế nào. Đầu tiên, nó cần được tạo trong thư mục con *tool* như sau:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Xác thực đầu vào bằng cách sử dụng mô hình Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: thêm Pydantic, để chúng ta có thể tạo một AddInputModel và xác thực các arg

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Điều ta thấy ở đây là cách định nghĩa tên, mô tả và schema đầu vào sử dụng Pydantic cùng handler sẽ được gọi khi công cụ này được gọi. Cuối cùng, ta expose `tool_add` là một dictionary chứa tất cả các thuộc tính này.

Còn có *schema.py* dùng để định nghĩa schema đầu vào của công cụ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Chúng ta cũng cần điền *__init__.py* để đảm bảo thư mục tools được coi là một module. Thêm vào đó, ta cần expose các module bên trong như sau:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Ta có thể tiếp tục thêm vào tệp này khi thêm nhiều công cụ hơn.

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

- name, đây là tên công cụ.
- rawSchema, đây là schema Zod, sẽ được dùng để xác thực các yêu cầu gọi công cụ.
- inputSchema, schema này được dùng bởi handler.
- callback, đây dùng để gọi công cụ.

Còn có `Tool` được dùng để chuyển đổi dictionary này thành kiểu mà handler của mcp server có thể chấp nhận, nó trông như thế này:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Và có *schema.ts* nơi lưu các schema đầu vào cho từng công cụ, hiện tại chỉ có một schema nhưng khi thêm công cụ có thể thêm nhiều mục:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Tuyệt, hãy tiếp tục xử lý việc liệt kê công cụ.

### -3- Xử lý liệt kê công cụ

Tiếp theo, để xử lý việc liệt kê công cụ, ta cần thiết lập một handler cho yêu cầu đó. Đây là những gì cần thêm vào tệp server:

**Python**

```python
# mã được bỏ qua để ngắn gọn
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

Ở đây, ta thêm decorator `@server.list_tools` và hàm triển khai `handle_list_tools`. Trong hàm này, ta cần tạo ra danh sách công cụ. Lưu ý mỗi công cụ cần có name, description và inputSchema.   

**TypeScript**

Để thiết lập handler yêu cầu liệt kê công cụ, ta gọi `setRequestHandler` trên server với một schema phù hợp với mục đích, trong trường hợp này là `ListToolsRequestSchema`. 

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
// mã đã bỏ qua để ngắn gọn
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Trả về danh sách các công cụ đã đăng ký
  return {
    tools: tools
  };
});
```

Tuyệt, giờ ta đã xử lý phần liệt kê công cụ, hãy xem cách gọi công cụ tiếp theo.

### -4- Xử lý gọi một công cụ

Để gọi một công cụ, ta cần thiết lập một handler yêu cầu khác, lần này tập trung vào xử lý yêu cầu xác định gọi tính năng nào và với những đối số gì.

**Python**

Hãy dùng decorator `@server.call_tool` và triển khai nó với hàm `handle_call_tool`. Trong hàm này, ta cần phân tích tên công cụ, đối số của nó và đảm bảo các đối số hợp lệ với công cụ đang được gọi. Ta có thể xác thực đối số trong hàm này hoặc ở phía bên dưới trong chính công cụ.

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

Đây là những gì diễn ra:

- Tên công cụ đã có dưới dạng tham số đầu vào `name`, tương tự đối số nằm trong dictionary `arguments`.

- Công cụ được gọi với `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Việc xác thực đối số diễn ra trong thuộc tính `handler` trỏ đến một hàm, nếu thất bại sẽ ném ngoại lệ. 

Vậy là ta đã hiểu đầy đủ về cách liệt kê và gọi công cụ dùng máy chủ cấp thấp.

Xem [ví dụ đầy đủ](./code/README.md) tại đây

## Bài tập

Mở rộng mã bạn đã có với một số công cụ, tài nguyên và prompt và nhận thấy bạn chỉ cần thêm file trong thư mục tools mà không cần ở nơi khác. 

*Không có giải pháp được cung cấp*

## Tóm tắt

Trong chương này, chúng ta đã thấy cách tiếp cận máy chủ cấp thấp hoạt động ra sao và cách nó giúp ta tạo ra kiến trúc đẹp mà ta có thể tiếp tục phát triển. Chúng ta cũng thảo luận về xác thực và bạn được chỉ dẫn cách làm việc với thư viện xác thực để tạo schema kiểm tra đầu vào.

## Tiếp theo

- Tiếp theo: [Xác thực đơn giản](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->