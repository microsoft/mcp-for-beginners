# Sử dụng máy chủ nâng cao

Có hai loại máy chủ khác nhau được cung cấp trong MCP SDK: máy chủ thông thường và máy chủ cấp thấp. Thông thường, bạn sẽ sử dụng máy chủ thông thường để thêm các tính năng vào nó. Tuy nhiên, trong một số trường hợp, bạn có thể muốn dựa vào máy chủ cấp thấp, chẳng hạn như:

- Kiến trúc tốt hơn. Có thể tạo một kiến trúc sạch với cả máy chủ thông thường và máy chủ cấp thấp, nhưng có thể cho rằng việc này dễ dàng hơn một chút với máy chủ cấp thấp.
- Khả năng sử dụng tính năng. Một số tính năng nâng cao chỉ có thể được sử dụng với máy chủ cấp thấp. Bạn sẽ thấy điều này trong các chương sau khi chúng ta thêm tính năng lấy mẫu và gợi ý.

## Máy chủ thông thường vs máy chủ cấp thấp

Dưới đây là cách tạo một MCP Server với máy chủ thông thường:

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

Điểm mấu chốt là bạn cần thêm rõ ràng từng công cụ, tài nguyên hoặc gợi ý mà bạn muốn máy chủ có. Không có gì sai với cách này.

### Cách tiếp cận máy chủ cấp thấp

Tuy nhiên, khi bạn sử dụng cách tiếp cận máy chủ cấp thấp, bạn cần suy nghĩ khác đi, cụ thể là thay vì đăng ký từng công cụ, bạn sẽ tạo hai trình xử lý cho mỗi loại tính năng (công cụ, tài nguyên hoặc gợi ý). Ví dụ, đối với công cụ, chỉ cần có hai hàm như sau:

- Liệt kê tất cả các công cụ. Một hàm sẽ chịu trách nhiệm cho tất cả các lần cố gắng liệt kê công cụ.
- Xử lý việc gọi tất cả các công cụ. Tương tự, chỉ có một hàm xử lý các yêu cầu gọi công cụ.

Nghe có vẻ ít công việc hơn đúng không? Thay vì đăng ký từng công cụ, tôi chỉ cần đảm bảo rằng công cụ được liệt kê khi tôi liệt kê tất cả các công cụ và được gọi khi có yêu cầu gọi công cụ.

Hãy xem cách mã trông như thế nào:

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

Ở đây, chúng ta có một hàm trả về danh sách các tính năng. Mỗi mục trong danh sách công cụ hiện có các trường như `name`, `description` và `inputSchema` để tuân theo kiểu trả về. Điều này cho phép chúng ta đặt định nghĩa công cụ và tính năng ở nơi khác. Chúng ta có thể tạo tất cả các công cụ trong một thư mục công cụ và làm tương tự với tất cả các tính năng của bạn, vì vậy dự án của bạn có thể được tổ chức như sau:

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

Thật tuyệt, kiến trúc của chúng ta có thể được làm cho trông khá sạch sẽ.

Còn việc gọi công cụ thì sao, có phải cũng là ý tưởng tương tự, một trình xử lý để gọi một công cụ bất kỳ? Đúng vậy, chính xác, đây là mã cho việc đó:

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

Như bạn thấy từ mã trên, chúng ta cần phân tích công cụ để gọi, và với các tham số nào, sau đó tiến hành gọi công cụ.

## Cải thiện cách tiếp cận với xác thực

Cho đến nay, bạn đã thấy cách tất cả các đăng ký để thêm công cụ, tài nguyên và gợi ý có thể được thay thế bằng hai trình xử lý này cho mỗi loại tính năng. Còn điều gì khác chúng ta cần làm? Chúng ta nên thêm một hình thức xác thực để đảm bảo rằng công cụ được gọi với các tham số đúng. Mỗi runtime có giải pháp riêng cho việc này, ví dụ Python sử dụng Pydantic và TypeScript sử dụng Zod. Ý tưởng là chúng ta làm như sau:

- Di chuyển logic tạo tính năng (công cụ, tài nguyên hoặc gợi ý) vào thư mục chuyên dụng của nó.
- Thêm cách xác thực yêu cầu đến, chẳng hạn yêu cầu gọi một công cụ.

### Tạo một tính năng

Để tạo một tính năng, chúng ta cần tạo một tệp cho tính năng đó và đảm bảo rằng nó có các trường bắt buộc của tính năng đó. Các trường này khác nhau một chút giữa công cụ, tài nguyên và gợi ý.

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

Ở đây bạn có thể thấy cách chúng ta thực hiện:

- Tạo một schema sử dụng Pydantic `AddInputModel` với các trường `a` và `b` trong tệp *schema.py*.
- Cố gắng phân tích yêu cầu đến để có kiểu `AddInputModel`, nếu có sự không khớp trong các tham số, điều này sẽ gây lỗi:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Bạn có thể chọn đặt logic phân tích này trong chính hàm gọi công cụ hoặc trong hàm trình xử lý.

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

- Trong trình xử lý xử lý tất cả các lần gọi công cụ, chúng ta cố gắng phân tích yêu cầu đến thành schema được định nghĩa của công cụ:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    nếu điều đó thành công, chúng ta tiếp tục gọi công cụ thực tế:

    ```typescript
    const result = await tool.callback(input);
    ```

Như bạn thấy, cách tiếp cận này tạo ra một kiến trúc tuyệt vời vì mọi thứ đều có vị trí của nó, tệp *server.ts* rất nhỏ chỉ để kết nối các trình xử lý yêu cầu và mỗi tính năng nằm trong thư mục tương ứng của nó, ví dụ tools/, resources/ hoặc /prompts.

Tuyệt vời, hãy thử xây dựng điều này tiếp theo.

## Bài tập: Tạo một máy chủ cấp thấp

Trong bài tập này, chúng ta sẽ thực hiện:

1. Tạo một máy chủ cấp thấp xử lý việc liệt kê công cụ và gọi công cụ.
1. Triển khai một kiến trúc bạn có thể xây dựng thêm.
1. Thêm xác thực để đảm bảo các lần gọi công cụ của bạn được xác thực đúng.

### -1- Tạo một kiến trúc

Điều đầu tiên chúng ta cần giải quyết là một kiến trúc giúp chúng ta mở rộng khi thêm nhiều tính năng hơn, đây là cách nó trông như thế nào:

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

Bây giờ chúng ta đã thiết lập một kiến trúc đảm bảo rằng chúng ta có thể dễ dàng thêm các công cụ mới vào thư mục công cụ. Hãy thoải mái làm theo điều này để thêm các thư mục con cho tài nguyên và gợi ý.

### -2- Tạo một công cụ

Hãy xem việc tạo một công cụ trông như thế nào tiếp theo. Đầu tiên, nó cần được tạo trong thư mục con *tool* như sau:

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

Ở đây chúng ta thấy cách định nghĩa tên, mô tả, một schema đầu vào sử dụng Pydantic và một trình xử lý sẽ được gọi khi công cụ này được gọi. Cuối cùng, chúng ta cung cấp `tool_add` là một từ điển chứa tất cả các thuộc tính này.

Cũng có *schema.py* được sử dụng để định nghĩa schema đầu vào được sử dụng bởi công cụ của chúng ta:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Chúng ta cũng cần điền *__init__.py* để đảm bảo thư mục công cụ được coi là một module. Ngoài ra, chúng ta cần cung cấp các module bên trong nó như sau:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Chúng ta có thể tiếp tục thêm vào tệp này khi thêm nhiều công cụ hơn.

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

Ở đây chúng ta tạo một từ điển gồm các thuộc tính:

- name, đây là tên của công cụ.
- rawSchema, đây là schema Zod, nó sẽ được sử dụng để xác thực các yêu cầu đến để gọi công cụ này.
- inputSchema, schema này sẽ được sử dụng bởi trình xử lý.
- callback, được sử dụng để gọi công cụ.

Cũng có `Tool` được sử dụng để chuyển đổi từ điển này thành kiểu mà trình xử lý máy chủ MCP có thể chấp nhận và nó trông như sau:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Và có *schema.ts* nơi chúng ta lưu trữ các schema đầu vào cho mỗi công cụ, trông như sau với chỉ một schema hiện tại nhưng khi thêm công cụ, chúng ta có thể thêm nhiều mục hơn:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Tuyệt vời, hãy tiếp tục xử lý việc liệt kê các công cụ tiếp theo.

### -3- Xử lý việc liệt kê công cụ

Tiếp theo, để xử lý việc liệt kê các công cụ, chúng ta cần thiết lập một trình xử lý yêu cầu cho việc đó. Đây là những gì chúng ta cần thêm vào tệp máy chủ:

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

Ở đây chúng ta thêm decorator `@server.list_tools` và hàm thực hiện `handle_list_tools`. Trong hàm này, chúng ta cần tạo danh sách các công cụ. Lưu ý rằng mỗi công cụ cần có tên, mô tả và inputSchema.

**TypeScript**

Để thiết lập trình xử lý yêu cầu cho việc liệt kê công cụ, chúng ta cần gọi `setRequestHandler` trên máy chủ với một schema phù hợp với những gì chúng ta đang cố gắng làm, trong trường hợp này là `ListToolsRequestSchema`.

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

Tuyệt vời, bây giờ chúng ta đã giải quyết phần liệt kê công cụ, hãy xem cách chúng ta có thể gọi công cụ tiếp theo.

### -4- Xử lý việc gọi một công cụ

Để gọi một công cụ, chúng ta cần thiết lập một trình xử lý yêu cầu khác, lần này tập trung vào xử lý yêu cầu chỉ định tính năng nào để gọi và với các tham số nào.

**Python**

Hãy sử dụng decorator `@server.call_tool` và thực hiện nó với một hàm như `handle_call_tool`. Trong hàm đó, chúng ta cần phân tích tên công cụ, các tham số của nó và đảm bảo rằng các tham số hợp lệ cho công cụ được chỉ định. Chúng ta có thể xác thực các tham số trong hàm này hoặc ở phần sau trong chính công cụ.

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

Đây là những gì diễn ra:

- Tên công cụ của chúng ta đã có sẵn dưới dạng tham số đầu vào `name`, điều này cũng đúng với các tham số dưới dạng từ điển `arguments`.

- Công cụ được gọi với `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Việc xác thực các tham số diễn ra trong thuộc tính `handler` trỏ đến một hàm, nếu thất bại, nó sẽ gây ra ngoại lệ.

Vậy là chúng ta đã hiểu đầy đủ về việc liệt kê và gọi công cụ sử dụng máy chủ cấp thấp.

Xem [ví dụ đầy đủ](./code/README.md) tại đây.

## Bài tập

Mở rộng mã bạn đã được cung cấp với một số công cụ, tài nguyên và gợi ý, và suy ngẫm về việc bạn chỉ cần thêm tệp vào thư mục công cụ mà không cần thay đổi ở nơi khác.

*Không có giải pháp được cung cấp*

## Tóm tắt

Trong chương này, chúng ta đã thấy cách tiếp cận máy chủ cấp thấp hoạt động và cách nó có thể giúp chúng ta tạo một kiến trúc tốt để tiếp tục xây dựng. Chúng ta cũng đã thảo luận về xác thực và bạn đã được hướng dẫn cách làm việc với các thư viện xác thực để tạo schema cho việc xác thực đầu vào.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.