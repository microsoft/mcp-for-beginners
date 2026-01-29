# 고급 서버 사용법

MCP SDK에는 일반 서버와 저수준 서버라는 두 가지 유형의 서버가 있습니다. 일반적으로는 일반 서버를 사용하여 기능을 추가합니다. 하지만 특정 경우에는 저수준 서버를 사용하는 것이 필요할 때가 있습니다. 예를 들어:

- 더 나은 아키텍처. 일반 서버와 저수준 서버를 사용하여 깔끔한 아키텍처를 만드는 것이 가능하지만, 저수준 서버를 사용하는 것이 약간 더 쉬울 수 있습니다.
- 기능 가용성. 일부 고급 기능은 저수준 서버에서만 사용할 수 있습니다. 이후 챕터에서 샘플링 및 유도 기능을 추가하면서 이를 확인할 수 있습니다.

## 일반 서버 vs 저수준 서버

일반 서버를 사용하여 MCP 서버를 생성하는 방법은 다음과 같습니다.

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

여기서 중요한 점은 서버에 추가하려는 각 도구, 리소스 또는 프롬프트를 명시적으로 추가한다는 것입니다. 이 방식에는 문제가 없습니다.

### 저수준 서버 접근 방식

하지만 저수준 서버 접근 방식을 사용할 때는 각 도구를 등록하는 대신, 기능 유형(도구, 리소스 또는 프롬프트)별로 두 개의 핸들러를 생성해야 한다는 점에서 다르게 생각해야 합니다. 예를 들어 도구의 경우 다음과 같은 두 가지 함수만 필요합니다:

- 모든 도구 나열. 한 함수는 모든 도구를 나열하려는 시도를 처리합니다.
- 모든 도구 호출 처리. 여기에서도 도구 호출을 처리하는 단 하나의 함수만 있습니다.

이 방식이 더 적은 작업처럼 들리지 않나요? 도구를 등록하는 대신, 모든 도구를 나열할 때 도구가 나열되도록 하고, 도구를 호출하려는 요청이 들어올 때 도구가 호출되도록 하면 됩니다.

코드가 어떻게 보이는지 살펴보겠습니다:

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

이제 기능 목록을 반환하는 함수가 있습니다. 도구 목록의 각 항목은 `name`, `description`, `inputSchema`와 같은 필드를 포함하여 반환 유형을 준수해야 합니다. 이를 통해 도구 및 기능 정의를 다른 곳에 배치할 수 있습니다. 이제 모든 도구를 도구 폴더에 생성하고, 모든 기능도 동일하게 처리하여 프로젝트를 다음과 같이 깔끔하게 구성할 수 있습니다:

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

훌륭합니다. 아키텍처를 깔끔하게 만들 수 있습니다.

도구 호출은 어떨까요? 동일한 아이디어로, 하나의 핸들러가 어떤 도구든 호출하는 방식인가요? 네, 맞습니다. 다음은 그 코드입니다:

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

위 코드에서 볼 수 있듯이, 호출할 도구와 그에 필요한 인수를 파싱한 후 도구를 호출하는 과정을 진행해야 합니다.

## 검증을 통한 접근 방식 개선

지금까지 도구, 리소스 및 프롬프트를 추가하기 위한 모든 등록을 기능 유형별로 두 개의 핸들러로 대체하는 방법을 살펴보았습니다. 그 외에 무엇을 해야 할까요? 도구가 올바른 인수로 호출되었는지 확인하기 위한 검증 형태를 추가해야 합니다. 각 런타임에는 이를 위한 자체 솔루션이 있습니다. 예를 들어 Python은 Pydantic을 사용하고 TypeScript는 Zod를 사용합니다. 아이디어는 다음과 같습니다:

- 기능(도구, 리소스 또는 프롬프트)을 생성하는 로직을 전용 폴더로 이동합니다.
- 예를 들어 도구를 호출하려는 요청을 검증하는 방법을 추가합니다.

### 기능 생성

기능을 생성하려면 해당 기능에 대한 파일을 생성하고 해당 기능에 필요한 필수 필드를 포함해야 합니다. 필드는 도구, 리소스 및 프롬프트에 따라 약간 다릅니다.

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

여기서 다음을 수행하는 방법을 볼 수 있습니다:

- *schema.py* 파일에서 `AddInputModel`을 사용하여 `a`와 `b` 필드가 포함된 Pydantic 스키마를 생성합니다.
- 들어오는 요청을 `AddInputModel` 유형으로 파싱하려고 시도합니다. 매개변수에 불일치가 있으면 오류가 발생합니다:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

이 파싱 로직을 도구 호출 자체에 넣을지 핸들러 함수에 넣을지는 선택할 수 있습니다.

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

- 모든 도구 호출을 처리하는 핸들러에서 들어오는 요청을 도구의 정의된 스키마로 파싱하려고 시도합니다:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    성공하면 실제 도구를 호출합니다:

    ```typescript
    const result = await tool.callback(input);
    ```

이 접근 방식은 모든 것이 제자리에 있는 훌륭한 아키텍처를 생성합니다. *server.ts*는 요청 핸들러를 연결하는 작은 파일일 뿐이며, 각 기능은 도구/, 리소스/ 또는 /prompts와 같은 해당 폴더에 있습니다.

좋습니다. 이제 이를 구축해 봅시다.

## 실습: 저수준 서버 생성

이 실습에서는 다음을 수행합니다:

1. 도구 나열 및 호출을 처리하는 저수준 서버를 생성합니다.
1. 확장 가능한 아키텍처를 구현합니다.
1. 도구 호출이 적절히 검증되도록 검증을 추가합니다.

### -1- 아키텍처 생성

먼저, 더 많은 기능을 추가할 때 확장 가능한 아키텍처를 설정해야 합니다. 다음과 같은 모습입니다:

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

이제 도구 폴더에 새 도구를 쉽게 추가할 수 있는 아키텍처를 설정했습니다. 리소스 및 프롬프트에 대해 하위 디렉토리를 추가할 수도 있습니다.

### -2- 도구 생성

다음으로 도구를 생성하는 방법을 살펴보겠습니다. 먼저, 도구를 *tool* 하위 디렉토리에 생성해야 합니다:

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

여기서 우리는 이름, 설명, Pydantic을 사용한 입력 스키마 정의, 도구가 호출될 때 실행될 핸들러를 정의하는 방법을 볼 수 있습니다. 마지막으로, 이러한 속성을 모두 포함하는 딕셔너리 `tool_add`를 노출합니다.

또한 도구에서 사용하는 입력 스키마를 정의하는 *schema.py*도 있습니다:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

*__init__.py*를 채워 도구 디렉토리가 모듈로 처리되도록 해야 합니다. 추가적으로, 다음과 같이 모듈을 노출해야 합니다:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

도구를 추가할 때 이 파일을 계속 업데이트할 수 있습니다.

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

여기서 우리는 다음 속성으로 구성된 딕셔너리를 생성합니다:

- name: 도구의 이름입니다.
- rawSchema: Zod 스키마로, 들어오는 요청을 검증하는 데 사용됩니다.
- inputSchema: 핸들러에서 사용하는 스키마입니다.
- callback: 도구를 호출하는 데 사용됩니다.

또한 이 딕셔너리를 MCP 서버 핸들러가 수락할 수 있는 유형으로 변환하는 `Tool`도 있습니다. 이는 다음과 같습니다:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

그리고 각 도구의 입력 스키마를 저장하는 *schema.ts*도 있습니다. 현재는 하나의 스키마만 있지만 도구를 추가할 때 더 많은 항목을 추가할 수 있습니다:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

좋습니다. 이제 도구 나열을 처리하는 방법으로 넘어갑시다.

### -3- 도구 나열 처리

다음으로, 도구를 나열하려면 요청 핸들러를 설정해야 합니다. 서버 파일에 다음을 추가해야 합니다:

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

여기서 `@server.list_tools` 데코레이터와 구현 함수 `handle_list_tools`를 추가합니다. 후자의 경우 도구 목록을 생성해야 합니다. 각 도구는 이름, 설명 및 inputSchema를 가져야 한다는 점에 유의하세요.

**TypeScript**

도구를 나열하기 위한 요청 핸들러를 설정하려면 서버에서 `ListToolsRequestSchema`와 같은 스키마를 사용하여 `setRequestHandler`를 호출해야 합니다.

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

좋습니다. 이제 도구 나열 부분을 해결했으니 도구 호출 방법을 살펴보겠습니다.

### -4- 도구 호출 처리

도구를 호출하려면 요청 핸들러를 설정해야 합니다. 이번에는 어떤 기능을 호출할지와 어떤 인수를 사용할지 지정하는 요청을 처리하는 데 초점을 맞춥니다.

**Python**

`@server.call_tool` 데코레이터를 사용하고 `handle_call_tool`과 같은 함수로 구현합니다. 해당 함수 내에서 도구 이름, 인수를 파싱하고 해당 도구에 대해 인수가 유효한지 확인해야 합니다. 인수 검증은 이 함수에서 또는 실제 도구에서 수행할 수 있습니다.

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

여기서 일어나는 일은 다음과 같습니다:

- 도구 이름은 이미 입력 매개변수 `name`으로 제공되며, 인수는 `arguments` 딕셔너리 형태로 제공됩니다.

- 도구는 `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`로 호출됩니다. 인수 검증은 `handler` 속성에서 수행되며, 이는 함수로 연결됩니다. 실패하면 예외가 발생합니다.

이제 저수준 서버를 사용하여 도구를 나열하고 호출하는 전체 과정을 이해했습니다.

[전체 예제](./code/README.md)를 여기에서 확인하세요.

## 과제

제공된 코드를 확장하여 여러 도구, 리소스 및 프롬프트를 추가하고, 도구 디렉토리에 파일만 추가하면 된다는 점을 반영해 보세요.

*해결책 없음*

## 요약

이 챕터에서는 저수준 서버 접근 방식이 어떻게 작동하는지, 그리고 이를 통해 계속 확장 가능한 깔끔한 아키텍처를 만드는 방법을 살펴보았습니다. 또한 검증에 대해 논의하고, 입력 검증을 위한 스키마를 생성하기 위해 검증 라이브러리를 사용하는 방법을 배웠습니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.