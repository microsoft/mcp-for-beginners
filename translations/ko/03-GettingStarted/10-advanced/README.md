# 고급 서버 사용법

MCP SDK에는 두 가지 유형의 서버가 있습니다. 일반 서버와 저수준 서버(low-level server)입니다. 보통은 일반 서버를 사용하여 기능을 추가합니다. 하지만 때때로 저수준 서버를 사용해야 할 때가 있는데, 예를 들면 다음과 같은 경우입니다:

- 더 나은 아키텍처. 일반 서버와 저수준 서버를 함께 사용해서 깨끗한 아키텍처를 만들 수 있지만, 저수준 서버를 사용할 때 조금 더 쉽다고 할 수 있습니다.
- 기능 가용성. 일부 고급 기능은 저수준 서버에서만 사용할 수 있습니다. 이후 장에서 샘플링과 유도(elicitation)를 추가하며 이를 확인할 수 있습니다.

## 일반 서버 vs 저수준 서버

아래는 일반 서버로 MCP 서버를 생성하는 예시입니다.

**Python**

```python
mcp = FastMCP("Demo")

# 추가 도구를 추가하세요
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

// 추가 도구를 추가하세요
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

요점은 서버가 가지길 원하는 각 도구, 리소스 또는 프롬프트를 명시적으로 추가한다는 것입니다. 이는 잘못된 방법이 아닙니다.

### 저수준 서버 접근법

하지만 저수준 서버 접근법을 사용할 때는 생각을 다르게 해야 합니다. 각 도구를 등록하는 대신, 기능 유형별로(도구, 리소스 또는 프롬프트) 두 개의 핸들러를 만듭니다. 예를 들어 도구의 경우 두 개의 함수만 존재합니다:

- 모든 도구 나열. 모든 도구 나열 시도를 담당하는 하나의 함수.
- 도구 호출 처리. 도구 호출을 처리하는 하나의 함수.

훨씬 적은 작업처럼 들리죠? 도구 등록 대신 모두 도구 목록에 포함시키고 도구 호출 요청이 들어올 때 호출되도록 하면 됩니다.

이제 코드가 어떻게 보이는지 살펴봅시다.

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
  // 등록된 도구 목록을 반환합니다
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

여기서는 기능 목록을 반환하는 함수가 있습니다. 도구 목록의 각 항목은 `name`, `description`, `inputSchema`와 같은 필드를 포함하여 반환 타입에 맞춥니다. 이를 통해 도구와 기능 정의를 다른 곳에 둘 수 있습니다. 모든 도구를 tools 폴더에 만들고 다른 기능들도 각자의 폴더에 모아 프로젝트를 다음과 같이 구성할 수 있습니다:

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

아주 좋군요. 깔끔한 아키텍처를 만들 수 있습니다.

도구 호출은 어떤가요? 역시 하나의 핸들러가 어떤 도구든 호출하는 방식인가요? 맞습니다. 호출 코드는 다음과 같습니다.

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools는 도구 이름을 키로 갖는 사전입니다
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
    // TODO 도구를 호출하세요,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

위 코드를 보면 호출할 도구와 인자를 파싱한 다음 도구를 호출하는 것을 알 수 있습니다.

## 검증을 통한 접근법 개선

지금까지는 각 기능 유형별로 두 개의 핸들러로 도구, 리소스, 프롬프트 등록을 대체하는 방법을 보았습니다. 그 외 무엇을 해야 하나요? 도구가 올바른 인자로 호출되는지 검증하는 절차가 필요합니다. 각 런타임마다 해결책이 다릅니다. 예를 들어 Python은 Pydantic을, TypeScript는 Zod를 사용합니다. 아이디어는 다음과 같습니다:

- 기능(도구, 리소스 또는 프롬프트)을 만드는 로직을 전용 폴더로 분리합니다.
- 예를 들어 도구 호출 요청이 들어올 때 이를 검증하는 방법을 추가합니다.

### 기능 만들기

기능을 만들려면 해당 기능 파일을 생성하고 필수 필드를 포함했는지 확인해야 합니다. 이 필드는 도구, 리소스, 프롬프트마다 조금 다릅니다.

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
        # Pydantic 모델을 사용하여 입력을 검증합니다
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic을 추가하여 AddInputModel을 만들고 인수를 검증할 수 있게 합니다

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

여기서는 다음을 수행합니다.

- Pydantic을 사용해 `AddInputModel` 스키마를 만들고, *schema.py* 파일에 필드 `a`와 `b`를 정의합니다.
- 들어오는 요청을 `AddInputModel` 타입으로 파싱 시도합니다. 파라미터가 맞지 않으면 오류가 발생합니다:

   ```python
   # add.py
    try:
        # Pydantic 모델을 사용하여 입력 유효성 검사
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

이 파싱 로직을 도구 호출 자체에 두거나 핸들러 함수에 둘지 선택할 수 있습니다.

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

- 모든 도구 호출을 처리하는 핸들러에서 요청을 도구 정의된 스키마로 파싱 시도합니다:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    성공하면 실제 도구를 호출합니다:

    ```typescript
    const result = await tool.callback(input);
    ```

이 방식은 훌륭한 아키텍처를 만듭니다. *server.ts* 파일은 요청 핸들러 연결만 하는 아주 작은 파일이고, 각 기능은 각각의 폴더(도구는 tools/, 리소스는 resources/, 프롬프트는 prompts/)에 있습니다.

좋습니다. 다음으로 이를 직접 만들어 봅시다.

## 연습: 저수준 서버 만들기

이번 연습에서는 다음을 할 것입니다:

1. 도구 나열과 호출을 처리하는 저수준 서버 생성.
2. 확장이 용이한 아키텍처 구현.
3. 도구 호출이 적절히 검증되도록 검증 추가.

### -1- 아키텍처 생성

먼저, 기능이 늘어날 때 확장 가능한 아키텍처를 만듭니다. 다음과 같습니다:

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

이제 tools 폴더에 도구를 쉽게 추가할 수 있는 아키텍처가 마련되었습니다. 리소스와 프롬프트도 마찬가지로 하위 디렉터리를 추가해도 좋습니다.

### -2- 도구 만들기

이제 도구 생성 방법을 보겠습니다. 먼저 도구는 tools 하위 디렉터리에 생성해야 합니다.

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic 모델을 사용하여 입력값을 검증합니다
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic을 추가하여 AddInputModel을 만들고 args를 검증할 수 있도록 합니다

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

여기서는 이름, 설명, 입력 스키마를 Pydantic으로 정의하고, 도구 호출 시 실행되는 핸들러를 정의합니다. 마지막으로 `tool_add` 사전에 모든 속성을 담아 노출합니다.

또한 입력 스키마를 정의하는 <em>schema.py</em>가 있습니다:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

tools 디렉터리를 모듈로 취급하도록 <em>__init__.py</em>도 작성해야 합니다. 모듈 내 노출도 다음과 같이 합니다:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

더 많은 도구를 추가하면서 이 파일에도 계속 추가할 수 있습니다.

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

여기서는 다음 속성으로 이루어진 사전을 생성합니다:

- name: 도구 이름.
- rawSchema: Zod 스키마로, 도구 호출 요청 검증용.
- inputSchema: 핸들러에서 사용하는 스키마.
- callback: 도구를 호출하는 함수.

또한 mcp 서버 핸들러가 받을 수 있는 타입으로 변환하는 `Tool` 타입이 있습니다:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

그리고 각 도구의 입력 스키마를 저장하는 <em>schema.ts</em>가 있으며 현재는 하나의 스키마만 있지만 도구가 늘면 항목을 추가할 수 있습니다:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

좋습니다. 이제 도구 나열 처리를 이어서 구현해 봅시다.

### -3- 도구 나열 처리

도구 나열을 처리하려면 요청 핸들러를 설정해야 합니다. 서버 파일에 추가할 내용은 다음과 같습니다:

**Python**

```python
# 간결함을 위해 코드 생략
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

데코레이터 `@server.list_tools`와 구현 함수 `handle_list_tools`를 추가했습니다. 이 함수는 도구 목록을 반환하며, 각 도구는 name, description, inputSchema가 있어야 합니다.

**TypeScript**

도구 나열 요청 핸들러를 설정하려면 `setRequestHandler`를 호출하고, 처리할 작업에 맞는 스키마(`ListToolsRequestSchema`)를 전달합니다.

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
// 간결함을 위해 코드를 생략함
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 등록된 도구 목록을 반환합니다
  return {
    tools: tools
  };
});
```

잘했습니다. 도구 나열 부분을 해결했으니 이제 도구 호출 방법을 살펴봅시다.

### -4- 도구 호출 처리

도구를 호출하려면, 이번에는 호출할 기능과 인자를 명시하는 요청을 다룰 또 다른 요청 핸들러를 설정해야 합니다.

**Python**

데코레이터 `@server.call_tool`을 사용하고 `handle_call_tool` 함수로 구현해봅시다. 이 함수 내에서 도구 이름과 인자를 파싱하고 인자가 적합한지 검증해야 합니다. 인자 검증은 이 함수나 실제 도구 내에서 할 수 있습니다.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools는 도구 이름을 키로 가지는 사전입니다
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # 도구를 호출합니다
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

설명:

- 도구 이름은 입력 매개변수 `name`으로 이미 제공됩니다. 인자는 `arguments` 사전 형태입니다.
- 실제 도구 호출은 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`로 이루어집니다. 인자 검증은 이 `handler` 함수 내에서 수행되고, 실패하면 예외가 발생합니다.

이제 저수준 서버를 이용해 도구 나열과 호출을 완전히 이해했습니다.

[전체 예제](./code/README.md)를 확인하세요.

## 과제

배포된 코드를 확장하여 여러 도구, 리소스, 프롬프트를 추가하고 tools 디렉터리에 파일만 추가하면 된다는 점을 체감해보세요.

*해답 제공하지 않음*

## 요약

이번 장에서는 저수준 서버 접근법이 어떻게 작동하는지, 좋은 아키텍처를 계속 구축하는데 어떻게 도움이 되는지 보았습니다. 또한 검증이 어떻게 이루어지는지, 검증 라이브러리를 사용해 입력 검증 스키마를 만드는 방법도 배웠습니다.

## 다음 내용

- 다음: [간단 인증](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어의 공식 문서로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오해에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->