# 고급 서버 사용법

MCP SDK에는 일반 서버와 로우 레벨 서버라는 두 가지 유형의 서버가 노출되어 있습니다. 일반적으로는 정규 서버를 사용하여 기능을 추가합니다. 그러나 다음과 같은 경우에는 로우 레벨 서버에 의존하고자 할 수 있습니다:

- 더 나은 아키텍처. 정규 서버와 로우 레벨 서버 모두로 깔끔한 아키텍처를 만들 수 있지만, 로우 레벨 서버가 약간 더 쉽다고 주장할 수 있습니다.
- 기능 가용성. 일부 고급 기능은 로우 레벨 서버에서만 사용할 수 있습니다.
    이후 챕터에서 다루는 Elicitation과 MCP `2026-07-28`에서 더 이상 사용되지 않는 레거시 Sampling 기능이 이에 해당합니다.


## 정규 서버 대 로우 레벨 서버

다음은 정규 서버로 MCP 서버를 생성하는 모습입니다.

**Python**

```python
mcp = FastMCP("Demo")

# 덧셈 도구 추가
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

요점은 서버가 가지길 원하는 각 도구, 리소스 또는 프롬프트를 명시적으로 추가한다는 것입니다. 전혀 문제될 게 없습니다.  

### 로우 레벨 서버 접근법

그러나 로우 레벨 서버 접근법을 사용할 때는 이를 다르게 생각해야 합니다. 각 도구, 리소스 또는 프롬프트에 대해 각각 두 개의 핸들러를 만듭니다. 예를 들어 도구는 다음과 같은 두 개의 함수만 가집니다:

- 모든 도구 나열하기. 한 함수가 모든 도구 나열 시도를 처리합니다.
- 도구 호출 처리. 이 경우도 호출 요청 처리 함수가 하나뿐입니다.

그럼 작업량이 줄어들 것 같지 않나요? 도구를 등록하는 대신, 모든 도구를 나열할 때 목록에 포함되도록 하고, 도구 호출 요청이 들어왔을 때 호출되도록 하면 됩니다.

이제 코드가 어떻게 보이는지 살펴보겠습니다:

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

이제 기능 목록을 반환하는 함수가 있습니다. 도구 목록의 각 항목은 반환 타입에 맞춰 `name`, `description`, `inputSchema` 등의 필드를 가집니다. 덕분에 도구와 기능 정의를 다른 곳에 두고, 도구를 모두 tools 폴더에 만들 수 있으며, 기능들도 각각의 폴더에 배치할 수 있습니다. 그래서 프로젝트가 다음과 같이 정리될 수 있습니다:

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

훌륭합니다. 깔끔한 아키텍처를 만들 수 있습니다.

도구 호출은 어떨까요? 같은 아이디어인가요, 어떤 도구든 호출하는 하나의 핸들러가 있나요? 네, 맞습니다. 다음은 이에 대한 코드입니다:

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
    // TODO 도구를 호출합니다,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

위 코드를 보면 호출할 도구와 어떤 인수로 호출할지 파싱한 다음 도구를 호출해야 함을 알 수 있습니다.

## 검증을 통한 접근법 개선

지금까지 도구, 리소스, 프롬프트 추가를 각 기능 유형별 두 개 핸들러로 대체할 수 있다는 것을 보았습니다. 그 외에 우리가 해야 할 일은 무엇일까요? 도구 호출 시 인수가 올바른지 검증하는 방법을 추가해야 합니다. 각 런타임마다 이 문제에 대한 해법이 있는데, 예를 들어 파이썬은 Pydantic, 타입스크립트는 Zod를 사용합니다. 아이디어는 다음과 같습니다:

- 기능(도구, 리소스, 프롬프트) 생성 로직을 전용 폴더로 옮깁니다.
- 도구 호출 요청과 같은 들어오는 요청을 검증하는 방법을 추가합니다.

### 기능 생성하기

기능을 생성하려면 해당 기능 전용 파일을 만들고 필수 필드가 포함되도록 해야 합니다. 도구, 리소스, 프롬프트 사이에 필드는 약간 차이가 있습니다.

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
        # Pydantic 모델을 사용하여 입력값을 검증합니다
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic을 추가하여 AddInputModel을 만들고 인수를 검증할 수 있도록 합니다

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

다음과 같은 작업을 수행하는 모습을 볼 수 있습니다:

- Pydantic의 `AddInputModel` 스키마를 <em>schema.py</em>에 필드 `a`와 `b`로 생성합니다.
- 들어오는 요청을 `AddInputModel` 타입으로 파싱을 시도합니다. 매개변수가 일치하지 않으면 오류가 납니다.

   ```python
   # add.py
    try:
        # Pydantic 모델을 사용하여 입력값 검증
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

이 파싱 로직을 도구 호출 안에 두거나 핸들러 함수 안에 둘 수도 있습니다.

**TypeScript**

```typescript
// 서버.ts
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

       // @ts-무시
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

// 스키마.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// 추가.ts
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

- 모든 도구 호출을 처리하는 핸들러에서, 들어오는 요청을 도구가 정의한 스키마로 파싱해 봅니다:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    파싱이 성공하면 실제 도구를 호출합니다:

    ```typescript
    const result = await tool.callback(input);
    ```

이 접근법은 매우 좋은 아키텍처를 만듭니다. 각 기능이 위치를 분명히 하여 *server.ts* 파일은 매우 작고 요청 핸들러 연결만 하며, 각 기능은 tools/, resources/, prompts/ 폴더 안에 각각 있습니다.

좋습니다. 다음으로 이것을 구현해 봅시다.

## 연습: 로우 레벨 서버 만들기

이 연습에서는 다음을 수행합니다:

1. 도구 나열과 호출을 처리하는 로우 레벨 서버를 만듭니다.
1. 확장 가능한 아키텍처를 구현합니다.
1. 도구 호출이 올바르게 검증되도록 검증 기능을 추가합니다.

### -1- 아키텍처 만들기

먼저 해결해야 할 것은, 기능이 추가됨에 따라 쉽게 확장 가능한 아키텍처입니다. 다음과 같이 생겼습니다:

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

이제 tools 폴더에 새로운 도구를 쉽게 추가할 수 있는 아키텍처를 설정했습니다. 리소스와 프롬프트 하위 디렉토리도 같은 방식으로 추가할 수 있습니다.

### -2- 도구 생성하기

도구를 만드는 모습은 다음과 같습니다. 먼저 도구 전용 *tool* 하위 디렉터리에 생성해야 합니다:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic 모델을 사용하여 입력값 검증
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic 추가, AddInputModel 생성 및 args 검증 가능하게 만들기

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

여기에선 Pydantic으로 이름, 설명, 입력 스키마 정의와, 도구 호출 시 실행될 핸들러가 정의되어 있습니다. 마지막으로 `tool_add`라는 사전으로 이 속성들을 노출합니다.

또한 도구 입력 스키마 정의용 *schema.py* 파일도 있습니다:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

*__init__.py* 파일도 채워서 tools 디렉터리가 모듈로 인식되도록 해야 하며, 모듈 내 코드를 노출하도록 다음과 같이 작성합니다:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

도구가 더 늘어나면 이 파일도 계속 추가해 나가면 됩니다.

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

여기서는 다음과 같은 속성을 가진 딕셔너리를 만듭니다:

- name, 도구 이름입니다.
- rawSchema, Zod 스키마로 도구 호출 요청을 검증하는 데 사용됩니다.
- inputSchema, 핸들러에서 사용되는 스키마입니다.
- callback, 도구를 실제 호출하는 함수입니다.

`Tool`이라는 유형 변환기가 있어, 이 딕셔너리를 MCP 서버 핸들러가 받아들일 수 있는 타입으로 바꿉니다:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

그리고 현재 하나의 스키마만 가진 <em>schema.ts</em>는 각 도구별 입력 스키마를 저장하며, 도구가 늘어나면 항목도 추가합니다:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

이제 도구 목록을 다루는 부분을 처리해 봅시다.

### -3- 도구 목록 처리

도구 목록을 처리하기 위한 요청 핸들러를 설정해야 합니다. 서버 파일에 추가할 내용은 다음과 같습니다:

**Python**

```python
# 간결함을 위해 코드 생략됨
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

여기서는 `@server.list_tools` 데코레이터와 구현 함수 `handle_list_tools`를 추가합니다. 이후 함수에서 도구 목록을 만들어야 하며, 각 도구는 이름, 설명, inputSchema를 가져야 합니다.  

**TypeScript**

도구 목록 요청을 처리하려면, 서버의 `setRequestHandler`에 맞는 스키마(`ListToolsRequestSchema`)와 함께 호출해야 합니다.

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
// 간결함을 위해 코드 생략
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 등록된 도구 목록을 반환합니다
  return {
    tools: tools
  };
});
```

이제 도구 목록 나열 문제는 해결했으니 다음은 도구 호출을 살펴봅시다.

### -4- 도구 호출 처리

도구를 호출하려면, 이번에는 어떤 기능을 어떤 인수로 호출할지 명시하는 요청을 처리하는 핸들러를 구성해야 합니다.

**Python**

`@server.call_tool` 데코레이터를 쓰고, `handle_call_tool`과 같은 함수로 구현합시다. 함수 내부에서 도구 이름과 인수를 꺼내 도구에 맞는 인수인지 검증해야 합니다. 인수 검증을 이 함수에서 하거나 도구 내부에서 할 수 있습니다.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools는 도구 이름을 키로 하는 딕셔너리입니다
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

처리 과정은 다음과 같습니다:

- 도구 이름은 이미 입력 매개변수 `name`으로 있으며, 인수는 `arguments` 사전 형태입니다.

- 도구 호출은 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`로 실행합니다. 인수 검증은 `handler` 속성에 지정된 함수 내에서 이뤄지며, 실패 시 예외가 발생합니다.

이렇게 해서 저수준 서버를 사용한 도구 목록화 및 호출 방식을 완벽하게 이해했습니다.

[전체 예제](./code/README.md)를 참고하세요

## 과제

도구, 리소스, 프롬프트를 여러 개 추가하면서, tools 디렉터리에 파일만 추가하면 된다는 점을 체감해 보세요.

*해답은 제공되지 않습니다*

## 요약

이번 장에서는 저수준 서버 접근법이 어떻게 작동하는지, 이를 통해 확장 가능한 깔끔한 아키텍처를 만들 수 있음을 보았습니다. 또한 검증을 다루면서 입력 검증 스키마 생성을 위해 검증 라이브러리를 사용하는 법도 배웠습니다.

## 다음은 무엇인가요

- 다음: [간단한 인증](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->