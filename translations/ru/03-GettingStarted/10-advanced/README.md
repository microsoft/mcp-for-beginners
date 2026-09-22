# Расширенное использование сервера

В MCP SDK представлены два различных типа серверов: обычный сервер и низкоуровневый сервер. Обычно для добавления функций используется обычный сервер. Однако в некоторых случаях стоит использовать низкоуровневый сервер, например:

- Лучшая архитектура. Создать чистую архитектуру можно и с обычным сервером, и с низкоуровневым, но можно утверждать, что с низкоуровневым это сделать немного проще.
- Доступность функций. Некоторые продвинутые функции доступны только с
    низкоуровневым сервером. В последующих главах рассматриваются функции Elicitation и устаревший Sampling,
    который устарел в MCP `2026-07-28`.

## Обычный сервер vs низкоуровневый сервер

Вот как выглядит создание сервера MCP с обычным сервером

**Python**

```python
mcp = FastMCP("Demo")

# Добавить инструмент сложения
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

// Добавить инструмент сложения
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

Суть в том, что вы явно добавляете каждый инструмент, ресурс или подсказку, которую хотите видеть на сервере. В этом нет ничего плохого.  

### Подход низкоуровневого сервера

Однако при использовании низкоуровневого сервера необходимо думать иначе. Вместо регистрации каждого инструмента вы создаёте два обработчика на каждый тип функции (инструменты, ресурсы или подсказки). Например, у инструментов есть всего две функции:

- Перечисление всех инструментов. Одна функция отвечает за все попытки вывести список инструментов.
- Обработка вызова инструментов. Здесь также есть одна функция, обрабатывающая вызовы инструментов.

Звучит как меньшая работа, правда? Вместо регистрации инструмента нужно лишь убедиться, что инструмент отображён при запросе списка всех инструментов и что он вызывается при поступлении запроса на вызов инструмента.

Давайте посмотрим, как теперь выглядит код:

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
  // Вернуть список зарегистрированных инструментов
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

Теперь у нас есть функция, возвращающая список функций. Каждая запись в списке инструментов содержит поля `name`, `description` и `inputSchema` согласно типу возвращаемого значения. Это позволяет разместить определения инструментов и функций в отдельном месте. Теперь мы можем создавать все инструменты в папке tools, то же касается всех ваших функций, и проект может быть организован следующим образом:

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

Это великолепно, наша архитектура может выглядеть достаточно чисто.

Как насчёт вызова инструментов – та же идея, один обработчик для вызова любого инструмента? Да, именно так, вот код для этого:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools — это словарь с названиями инструментов в качестве ключей
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
    // TODO вызов инструмента,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Как видно из кода выше, нам нужно распарсить, какой инструмент вызвать и с какими аргументами, а затем выполнить вызов инструмента.

## Улучшение подхода с помощью валидации

До сих пор вы видели, как все регистрации на добавление инструментов, ресурсов и подсказок можно заменить двумя обработчиками на каждый тип функции. Что ещё нужно сделать? Следует добавить какую-то форму валидации, чтобы убедиться, что инструмент вызывается с правильными аргументами. Каждый рантайм имеет собственное решение, например Python использует Pydantic, а TypeScript — Zod. Идея в следующем:

- Переместить логику создания функции (инструмента, ресурса или подсказки) в её выделенную папку.
- Добавить способ проверки входящего запроса, например, на вызов инструмента.

### Создание функции

Чтобы создать функцию, нужно создать файл для неё и убедиться, что в нём есть обязательные поля, необходимые для этой функции. Поля немного различаются между инструментами, ресурсами и подсказками.

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
        # Проверить ввод с помощью модели Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: добавить Pydantic, чтобы мы могли создать AddInputModel и проверить аргументы

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

здесь показано, как мы делаем следующее:

- Создаём схему с использованием Pydantic `AddInputModel` с полями `a` и `b` в файле *schema.py*.
- Пытаемся распарсить входящий запрос как тип `AddInputModel`, если параметры не совпадают, произойдёт ошибка:

   ```python
   # add.py
    try:
        # Проверка входных данных с использованием модели Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Вы можете выбрать, размещать ли эту логику парсинга в самом вызове инструмента или в функции-обработчике.

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

- В обработчике всех вызовов инструментов теперь пытаемся распарсить входящий запрос в схему, определённую для инструмента:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    если это удаётся, продолжаем вызов самого инструмента:

    ```typescript
    const result = await tool.callback(input);
    ```

Как видите, такой подход создаёт отличную архитектуру: всё на своих местах, *server.ts* — очень маленький файл, который только связывает обработчики запросов, а каждая функция находится в соответствующей папке, то есть tools/, resources/ или prompts/.

Отлично, давайте теперь попробуем построить это.

## Упражнение: создание низкоуровневого сервера

В этом упражнении мы сделаем следующее:

1. Создадим низкоуровневый сервер, который обрабатывает перечисление инструментов и вызовы инструментов.
1. Реализуем архитектуру, на которой можно строить дальше.
1. Добавим валидацию, чтобы убедиться, что вызовы инструментов правильно проверены.

### -1- Создание архитектуры

Первое, что нужно учесть — это архитектура, которая поможет нам масштабироваться при добавлении новых функций, вот как она выглядит:

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

Теперь у нас настроена архитектура, которая обеспечит простое добавление новых инструментов в папку tools. По желанию можете добавить подкаталоги для ресурсов и подсказок.

### -2- Создание инструмента

Посмотрим, как создать инструмент. Сначала его нужно создать в поддиректории *tool*, вот так:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Проверить входные данные с использованием модели Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: добавить Pydantic, чтобы мы могли создать AddInputModel и проверить аргументы

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Здесь мы определяем name, description и input schema с использованием Pydantic, а также обработчик, который будет вызван при вызове этого инструмента. Наконец, мы экспортируем `tool_add` — словарь, содержащий все эти свойства.

Также есть файл *schema.py*, в котором определяется входная схема, используемая нашим инструментом:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Нам также нужно заполнить *__init__.py*, чтобы директория tools воспринималась как модуль. Кроме того, нужно экспортировать модули в нём вот так:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Мы можем дополнять этот файл по мере добавления новых инструментов.

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

Здесь мы создаём словарь с свойствами:

- name — имя инструмента.
- rawSchema — Zod-схема, будет использоваться для проверки входящих запросов на вызов этого инструмента.
- inputSchema — схема, которая будет использоваться обработчиком.
- callback — используется для вызова инструмента.

Есть также тип `Tool`, который преобразует этот словарь в тип, принимаемый обработчиком сервера mcp, и он выглядит так:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

В *schema.ts* хранятся схемы ввода для каждого инструмента, сейчас только одна, но по мере добавления инструментов их количество можно увеличивать:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Отлично, переходим к обработке списка наших инструментов.

### -3- Обработка списка инструментов

Далее, чтобы обрабатывать запросы на вывод списка инструментов, нужно настроить обработчик запросов. Вот что нужно добавить в файл сервера:

**Python**

```python
# код опущен для краткости
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

Здесь мы добавляем декоратор `@server.list_tools` и функцию-реализацию `handle_list_tools`. В ней нужно сформировать список инструментов. Обратите внимание, что каждый инструмент должен содержать name, description и inputSchema.   

**TypeScript**

Для настройки обработчика запроса на вывод инструментов нужно вызвать `setRequestHandler` на сервере с соответствующей схемой, в данном случае `ListToolsRequestSchema`.

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
// код опущен для краткости
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Возвращает список зарегистрированных инструментов
  return {
    tools: tools
  };
});
```

Отлично, мы разобрались с выводом списка инструментов, теперь посмотрим, как можно обрабатывать вызовы инструментов.

### -4- Обработка вызова инструмента

Для вызова инструмента нужно настроить ещё один обработчик запросов, который будет принимать запрос с указанием, какую функцию вызывать и с какими аргументами.

**Python**

Используем декоратор `@server.call_tool` и реализуем его функцией `handle_call_tool`. В этой функции нам нужно распарсить имя инструмента, его аргументы и проверить их корректность для данного инструмента. Валидация аргументов может быть выполнена здесь либо позже, в самом инструменте.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools — это словарь с именами инструментов в качестве ключей
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # вызовите инструмент
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Вот что происходит:

- Имя инструмента уже присутствует во входном параметре `name`, а аргументы — в словаре `arguments`.

- Инструмент вызывается через `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Валидация аргументов осуществляется в свойстве `handler`, которое указывает на функцию, если оно не проходит — возникает исключение.

Теперь у нас есть полное понимание процесса перечисления и вызова инструментов с использованием низкоуровневого сервера.

Смотрите [полный пример](./code/README.md) здесь

## Задание

Расширьте данный код набором инструментов, ресурсов и подсказок и обратите внимание, что вам необходимо лишь добавлять файлы в директорию tools и больше нигде.

*Решение не предоставляется*

## Итоги

В этой главе мы увидели, как работает подход с низкоуровневым сервером и как он помогает создавать удобную архитектуру для дальнейшей разработки. Также обсудили валидацию и показали, как работать с библиотеками валидации для создания схем проверки ввода.

## Что дальше

- Далее: [Простая аутентификация](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->