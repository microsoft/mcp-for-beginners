# Расширенное использование сервера

В MCP SDK предоставляются два типа серверов: обычный сервер и сервер низкого уровня. Обычно вы используете обычный сервер для добавления функций. Однако в некоторых случаях может потребоваться сервер низкого уровня, например:

- **Лучшая архитектура.** Хотя чистую архитектуру можно создать как с обычным сервером, так и с сервером низкого уровня, можно утверждать, что с сервером низкого уровня это сделать немного проще.
- **Доступность функций.** Некоторые продвинутые функции доступны только с сервером низкого уровня. Вы увидите это в следующих главах, когда мы будем добавлять выборку и сбор данных.

## Обычный сервер vs сервер низкого уровня

Вот как выглядит создание MCP-сервера с использованием обычного сервера:

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

Суть в том, что вы явно добавляете каждый инструмент, ресурс или подсказку, которые хотите использовать на сервере. В этом нет ничего плохого.

### Подход с сервером низкого уровня

Однако при использовании подхода с сервером низкого уровня нужно мыслить иначе: вместо регистрации каждого инструмента вы создаете два обработчика для каждого типа функций (инструменты, ресурсы или подсказки). Например, для инструментов это будет выглядеть так:

- **Список всех инструментов.** Одна функция отвечает за все попытки получить список инструментов.
- **Обработка вызова инструментов.** Здесь также есть только одна функция, которая обрабатывает вызовы инструментов.

Звучит как меньше работы, верно? Вместо регистрации инструмента нужно лишь убедиться, что инструмент отображается в списке всех инструментов и вызывается при поступлении запроса на его использование.

Давайте посмотрим, как это выглядит в коде:

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

Здесь у нас есть функция, которая возвращает список функций. Каждый элемент в списке инструментов содержит поля, такие как `name`, `description` и `inputSchema`, чтобы соответствовать типу возвращаемого значения. Это позволяет вынести определение инструментов и функций в отдельные файлы. Теперь мы можем создать все инструменты в папке *tools*, а остальные функции организовать аналогично, чтобы структура проекта выглядела, например, так:

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

Отлично, наша архитектура может быть организована довольно чисто.

А как насчет вызова инструментов? Это та же идея — один обработчик для вызова любого инструмента? Да, именно так. Вот пример кода:

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

Как видно из приведенного выше кода, нам нужно извлечь инструмент для вызова, а также его аргументы, а затем выполнить вызов инструмента.

## Улучшение подхода с помощью валидации

До сих пор вы видели, как можно заменить регистрацию инструментов, ресурсов и подсказок двумя обработчиками для каждого типа функций. Что еще нужно сделать? Следует добавить валидацию, чтобы убедиться, что инструмент вызывается с правильными аргументами. У каждого языка программирования есть свои решения для этого: например, Python использует Pydantic, а TypeScript — Zod. Идея заключается в следующем:

- Вынести логику создания функции (инструмента, ресурса или подсказки) в соответствующую папку.
- Добавить способ проверки входящего запроса, например, на вызов инструмента.

### Создание функции

Чтобы создать функцию, нужно создать файл для этой функции и убедиться, что он содержит обязательные поля, необходимые для этой функции. Набор полей немного отличается для инструментов, ресурсов и подсказок.

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

Здесь вы видите, как мы делаем следующее:

- Создаем схему с помощью Pydantic `AddInputModel` с полями `a` и `b` в файле *schema.py*.
- Пытаемся преобразовать входящий запрос в тип `AddInputModel`. Если параметры не совпадают, произойдет ошибка:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Вы можете выбрать, где разместить эту логику преобразования: в самом вызове инструмента или в функции-обработчике.

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

- В обработчике, который обрабатывает все вызовы инструментов, мы пытаемся преобразовать входящий запрос в схему, определенную для инструмента:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Если преобразование прошло успешно, мы вызываем сам инструмент:

    ```typescript
    const result = await tool.callback(input);
    ```

Как видите, этот подход позволяет создать отличную архитектуру, где все находится на своих местах: файл *server.ts* становится очень компактным и только связывает обработчики запросов, а каждая функция находится в своей папке, например, *tools/*, *resources/* или *prompts/*.

Отлично, давайте попробуем построить это.

## Упражнение: Создание сервера низкого уровня

В этом упражнении мы сделаем следующее:

1. Создадим сервер низкого уровня, обрабатывающий список инструментов и их вызовы.
2. Реализуем архитектуру, которую можно будет расширять.
3. Добавим валидацию, чтобы убедиться, что вызовы инструментов корректны.

### -1- Создание архитектуры

Первое, что нужно сделать, — это создать архитектуру, которая позволит масштабироваться по мере добавления новых функций. Вот как это выглядит:

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

Теперь у нас есть архитектура, которая позволяет легко добавлять новые инструменты в папку *tools*. Вы можете следовать этому подходу, чтобы добавить подкаталоги для ресурсов и подсказок.

### -2- Создание инструмента

Давайте посмотрим, как выглядит создание инструмента. Сначала его нужно создать в подкаталоге *tools*, например:

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

Здесь мы видим, как определяются имя, описание, схема ввода с использованием Pydantic и обработчик, который будет вызываться при использовании этого инструмента. Наконец, мы экспортируем `tool_add`, который является словарем, содержащим все эти свойства.

Также есть файл *schema.py*, который используется для определения схемы ввода, используемой нашим инструментом:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Нам также нужно заполнить *__init__.py*, чтобы папка *tools* рассматривалась как модуль. Кроме того, нужно экспортировать модули внутри нее, например:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Мы можем добавлять в этот файл новые инструменты по мере необходимости.

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

Здесь мы создаем словарь, содержащий свойства:

- **name** — имя инструмента.
- **rawSchema** — схема Zod, которая будет использоваться для проверки входящих запросов.
- **inputSchema** — схема, которая будет использоваться обработчиком.
- **callback** — функция, вызывающая инструмент.

Также есть `Tool`, который используется для преобразования этого словаря в тип, который может принять обработчик MCP-сервера:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

И есть файл *schema.ts*, где хранятся схемы ввода для каждого инструмента. Пока там только одна схема, но по мере добавления инструментов можно добавлять новые записи:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Отлично, давайте перейдем к обработке списка инструментов.

### -3- Обработка списка инструментов

Чтобы обработать список инструментов, нужно настроить обработчик запросов. Вот что нужно добавить в файл сервера:

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

Здесь мы добавляем декоратор `@server.list_tools` и реализуем функцию `handle_list_tools`. В последней мы создаем список инструментов. Обратите внимание, что у каждого инструмента должны быть поля `name`, `description` и `inputSchema`.

**TypeScript**

Чтобы настроить обработчик запросов для списка инструментов, нужно вызвать `setRequestHandler` на сервере с использованием схемы, соответствующей задаче, например, `ListToolsRequestSchema`.

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

Отлично, теперь мы решили задачу отображения списка инструментов. Давайте посмотрим, как можно вызывать инструменты.

### -4- Обработка вызова инструмента

Чтобы вызвать инструмент, нужно настроить еще один обработчик запросов, который будет обрабатывать запросы с указанием функции для вызова и аргументов.

**Python**

Используем декоратор `@server.call_tool` и реализуем функцию, например, `handle_call_tool`. Внутри этой функции нужно извлечь имя инструмента, его аргументы и убедиться, что аргументы корректны для данного инструмента. Проверку можно выполнить либо в этой функции, либо в самом инструменте.

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

Вот что здесь происходит:

- Имя инструмента уже доступно как входной параметр `name`, то же самое касается аргументов в виде словаря `arguments`.

- Инструмент вызывается с помощью `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Проверка аргументов происходит в свойстве `handler`, которое указывает на функцию. Если проверка не пройдет, будет вызвано исключение.

Теперь у нас есть полное понимание того, как отображать список инструментов и вызывать их с использованием сервера низкого уровня.

См. [полный пример](./code/README.md) здесь.

## Задание

Расширьте предоставленный код, добавив несколько инструментов, ресурсов и подсказок, и обратите внимание, что вам нужно добавлять файлы только в папку *tools* и нигде больше.

*Решение не предоставлено*

## Итог

В этой главе мы рассмотрели, как работает подход с сервером низкого уровня, и как он помогает создать удобную архитектуру, которую можно развивать. Мы также обсудили валидацию и показали, как использовать библиотеки валидации для создания схем проверки входных данных.

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.