# 고급 서버 사용법

MCP SDK에는 두 가지 종류의 서버가 있습니다. 일반 서버와 저수준 서버입니다. 보통은 일반 서버를 사용하여 기능을 추가합니다. 하지만 다음과 같은 경우에는 저수준 서버에 의존하고 싶을 수 있습니다:

- 더 나은 아키텍처. 일반 서버와 저수준 서버 모두를 사용해 깔끔한 아키텍처를 만들 수 있지만, 저수준 서버가 조금 더 쉽다고 할 수 있습니다.
- 기능 가용성. 일부 고급 기능들은 저수준 서버에서만 사용할 수 있습니다. 샘플링 및 유도 기능 추가와 같은 후속 장에서 이를 확인할 수 있습니다.

## 일반 서버 vs 저수준 서버

다음은 일반 서버로 MCP 서버를 생성하는 모습입니다.

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

// 추가 도구를 추가하십시오
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

핵심은 서버가 갖길 원하는 각 도구, 리소스 또는 프롬프트를 명시적으로 추가한다는 점입니다. 이는 전혀 문제가 없습니다.

### 저수준 서버 접근법

그러나 저수준 서버 접근법을 사용할 때는 생각을 다르게 해야 합니다. 각 도구를 등록하는 대신 기능 유형(도구, 리소스, 프롬프트)마다 두 개의 핸들러를 만듭니다. 예를 들어 도구의 경우 다음 두 함수만 존재합니다:

- 모든 도구 나열. 한 함수가 도구를 나열하는 모든 시도를 담당합니다.
- 모든 도구 호출 처리. 이 함수는 도구 호출을 처리하는 단 하나의 함수입니다.

이게 더 적은 작업처럼 들리죠? 도구를 등록하는 대신 모든 도구 목록에 도구가 포함되도록 하고 도구 호출 요청이 들어올 때 호출되도록 하면 됩니다.

코드가 어떻게 보이는지 살펴봅시다.

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

여기 이제 기능 목록을 반환하는 함수가 있습니다. 도구 목록의 각 항목은 반환 유형에 맞게 `name`, `description`, `inputSchema`와 같은 필드를 갖고 있습니다. 이를 통해 도구 및 기능 정의를 다른 위치에 둘 수 있습니다. 이제 도구는 tools 폴더에 모두 두고, 다른 기능들도 마찬가지로 구성할 수 있으므로 프로젝트 구조가 다음과 같이 정리될 수 있습니다.

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

아주 좋습니다. 우리가 만든 아키텍처는 꽤 깔끔해 보일 수 있습니다.

도구 호출은 어떨까요? 동일한 개념으로 하나의 핸들러가 모든 도구 호출을 처리하나요? 맞습니다. 다음은 이에 대한 코드입니다.

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools는 도구 이름을 키로 가진 딕셔너리입니다
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

위 코드에서 볼 수 있듯이 호출할 도구와 인수를 파싱한 후 도구를 호출합니다.

## 검증을 통한 접근법 개선

지금까지 도구, 리소스, 프롬프트 등록을 각 기능 유형별 두 개의 핸들러로 대체하는 방법을 보았습니다. 다음으로 해야 할 일은 무엇일까요? 도구가 올바른 인수로 호출되는지 확인할 수 있도록 검증 로직을 추가해야 합니다. 런타임마다 각각의 솔루션이 있으며 예를 들어 Python은 Pydantic을, TypeScript는 Zod를 사용합니다. 다음을 수행할 수 있습니다:

- 기능(도구, 리소스, 프롬프트)을 생성하는 로직을 해당 폴더로 이동합니다.
- 예를 들어 도구 호출 요청이 올바른지 검증하는 방법을 추가합니다.

### 기능 생성

기능을 생성하려면 해당 기능에 대한 파일을 만들고 필수 필드를 포함하는지 확인해야 합니다. 도구, 리소스, 프롬프트에 따라 필드가 다소 다릅니다.

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
        # Pydantic 모델을 사용하여 입력값 검증
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic 추가하여 AddInputModel을 생성하고 인자를 검증할 수 있도록 하기

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

여기에서 다음 작업을 수행합니다:

- *schema.py* 파일에 Pydantic `AddInputModel` 스키마를 만들고 필드 `a`와 `b`를 포함합니다.
- 들어오는 요청을 `AddInputModel` 타입으로 파싱을 시도합니다. 인자 불일치가 있으면 오류가 발생합니다.

   ```python
   # add.py
    try:
        # Pydantic 모델을 사용하여 입력값 검증
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

이 파싱 로직을 도구 호출 내에 두거나 핸들러 함수에 둘지 선택할 수 있습니다.

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

- 모든 도구 호출을 처리하는 핸들러에서는 들어오는 요청을 도구의 정의된 스키마로 파싱을 시도합니다.

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    성공하면 실제 도구를 호출합니다:

    ```typescript
    const result = await tool.callback(input);
    ```

보시다시피, 이 접근법은 모든 요소가 각자의 위치에 있어 훌륭한 아키텍처를 만듭니다. *server.ts*는 요청 핸들러만 연결하는 매우 작은 파일이고, 각각의 기능은 tools/, resources/, prompts/과 같은 각자의 폴더에 있습니다.

좋습니다. 이제 이를 구축해 봅시다.

## 연습: 저수준 서버 생성하기

이번 연습에서는 다음을 수행합니다:

1. 도구 목록화 및 도구 호출을 처리하는 저수준 서버 생성.
2. 확장 가능한 아키텍처 구현.
3. 도구 호출이 정상적으로 검증되도록 검증 추가.

### -1- 아키텍처 생성

먼저 기능이 늘어날 때 확장 가능한 아키텍처를 설계해야 합니다. 다음과 같습니다.

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

이제 tools 폴더에 쉽게 새 도구를 추가할 수 있는 아키텍처를 구축했습니다. 필요하면 resources, prompts용 하위 디렉터리를 추가하세요.

### -2- 도구 생성

도구를 만드는 과정을 살펴보겠습니다. 우선 *tool* 하위 디렉터리에 생성해야 합니다.

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic 모델을 사용하여 입력 값 검증
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic을 추가하여 AddInputModel을 만들고 인수를 검증할 수 있도록 하기

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

여기서는 Pydantic으로 이름, 설명, 입력 스키마를 정의하고 도구 호출 시 실행되는 핸들러를 만듭니다. 마지막으로 `tool_add`라는 딕셔너리로 이 속성들을 노출합니다.

또한 입력 스키마를 정의하는 *schema.py* 파일도 있습니다:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

*__init__.py*를 채워서 tools 폴더가 모듈로 인식되도록 해야 하며 내부 모듈도 노출해야 합니다:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

도구를 추가할 때마다 이 파일에 계속 추가하면 됩니다.

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

여기서 프로퍼티로 구성된 딕셔너리를 만듭니다:

- name: 도구 이름.
- rawSchema: Zod 스키마로, 도구 호출 요청 검증에 사용.
- inputSchema: 핸들러에 의해 사용되는 스키마.
- callback: 도구 호출용 함수.

`Tool` 타입은 이 딕셔너리를 mcp 서버 핸들러가 받을 수 있는 타입으로 변환하며 다음과 같습니다:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

또한 *schema.ts*가 있으며, 각 도구의 입력 스키마를 저장합니다. 현재 하나의 스키마만 있지만 도구가 추가될수록 항목을 늘릴 수 있습니다:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

좋습니다. 이제 도구 목록화 처리를 진행해 보겠습니다.

### -3- 도구 목록 처리

도구 목록을 처리하기 위해 요청 핸들러를 추가해야 합니다. 서버 파일에 다음을 추가하세요:

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

`@server.list_tools` 데코레이터와 `handle_list_tools` 함수를 추가합니다. 이 함수에서는 도구 목록을 만들어야 하며, 각 도구는 이름, 설명, inputSchema가 포함되어야 합니다.

**TypeScript**

도구 목록화 요청 핸들러를 등록하려면 서버에서 `setRequestHandler`를 호출하고 수행하려는 작업에 맞는 스키마(`ListToolsRequestSchema`)를 사용해야 합니다.

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
  // 등록된 도구 목록 반환
  return {
    tools: tools
  };
});
```

잘했습니다. 도구 목록화 문제를 해결했습니다. 다음으로 도구 호출을 어떻게 처리하는지 봅시다.

### -4- 도구 호출 처리

도구를 호출하려면, 이번에는 어떤 기능을 호출할지, 어떤 인수와 함께 호출할지를 지정하는 요청을 처리하는 핸들러를 설정해야 합니다.

**Python**

`@server.call_tool` 데코레이터를 사용하고 `handle_call_tool` 같은 함수를 구현합니다. 이 함수 내에서 도구 이름, 인수를 파싱하고 인수가 해당 도구에 적합한지 확인합니다. 인수 검증을 이 함수에서 하거나 실제 도구 내에서 할 수 있습니다.

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

작동 방식은 다음과 같습니다:

- 도구 이름은 입력 매개변수 `name`에 이미 포함되어 있고, 인수는 `arguments` 딕셔너리 형태입니다.
- 도구는 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`로 호출됩니다. 인수 검증은 함수인 `handler` 속성에서 이루어지며 실패 시 예외가 발생합니다.

이제 저수준 서버를 이용해 도구 목록화 및 호출하는 과정을 완전히 이해했습니다.

전체 예시는 [여기](./code/README.md)를 참조하세요.

## 과제

지금까지 받은 코드를 여러 도구, 리소스, 프롬프트로 확장하고, tools 디렉터리에 파일만 추가하면 된다는 점을 어떻게 느끼는지 성찰해 보세요.

*해답 없음*

## 요약

이번 장에서는 저수준 서버 접근법이 어떻게 동작하는지, 그리고 이를 통해 계속 확장 가능한 깔끔한 아키텍처를 만드는 방법을 살펴보았습니다. 또한 검증에 관해 다루었으며, 입력 검증을 위한 스키마를 만드는 데 사용하는 검증 라이브러리 활용법도 소개했습니다.

## 다음 단계

- 다음: [간단한 인증](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 이용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있음을 양지해 주시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 내용에 대해서는 전문 번역가의 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 어떠한 오해나 잘못된 해석에 대해서도 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->