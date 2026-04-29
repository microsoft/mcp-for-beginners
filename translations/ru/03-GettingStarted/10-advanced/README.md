# Продвинутое использование сервера

В MCP SDK представлены два разных типа серверов: обычный сервер и низкоуровневый сервер. Обычно вы используете обычный сервер для добавления функций. Однако в некоторых случаях вы хотите положиться на низкоуровневый сервер, например:

- Лучшая архитектура. Можно создать чистую архитектуру с использованием и обычного, и низкоуровневого сервера, но можно утверждать, что с низкоуровневым сервером это несколько проще.
- Доступность функций. Некоторые продвинутые функции могут использоваться только с низкоуровневым сервером. Вы увидите это в следующих главах, когда мы добавим сэмплирование и элицитацию.

## Обычный сервер vs низкоуровневый сервер

Вот как выглядит создание MCP сервера с обычным сервером

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

Суть в том, что вы явно добавляете каждый инструмент, ресурс или подсказку, которые хотите иметь на сервере. В этом нет ничего плохого.

### Подход низкоуровневого сервера

Однако при использовании низкоуровневого сервера нужно мыслить иначе. Вместо регистрации каждого инструмента вы создаёте по два обработчика для каждого типа функций (инструменты, ресурсы или подсказки). Например, для инструментов есть две функции:

- Список всех инструментов. Одна функция отвечает за все попытки получить список инструментов.
- Обработка вызова всех инструментов. Здесь также только одна функция обрабатывает вызовы к инструментам.

Звучит как меньшая работа, правда? Вместо регистрации инструмента нужно просто убедиться, что инструмент перечислен при выгрузке списка всех инструментов, и что он вызывается при входящем запросе на вызов инструмента.

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

Здесь теперь есть функция, которая возвращает список функций. Каждая запись в списке инструментов имеет поля `name`, `description` и `inputSchema` в соответствии с типом возвращаемого значения. Это позволяет поместить определение инструментов и функций в другое место. Теперь мы можем создать все инструменты в папке tools, и то же самое касается всех ваших функций, так что ваш проект внезапно может выглядеть так:

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

Это здорово, наша архитектура может выглядеть очень чистой.

Как насчёт вызова инструментов — та же идея? Один обработчик для вызова любого инструмента? Да, именно так, вот код для этого:

**Python**

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
    // TODO вызвать инструмент,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Как видно из кода выше, нам нужно разобрать, какой инструмент вызвать и с какими аргументами, а затем перейти к вызову инструмента.

## Улучшение подхода с помощью валидации

До сих пор вы видели, как все ваши регистрации для добавления инструментов, ресурсов и подсказок могут быть заменены двумя обработчиками на каждый тип функций. Что еще нужно сделать? Нам следует добавить некоторую форму валидации, чтобы гарантировать, что инструмент вызывается с правильными аргументами. Каждый runtime имеет своё решение для этого, например Python использует Pydantic, а TypeScript — Zod. Идея состоит в следующем:

- Переместить логику создания функции (инструмент, ресурс или подсказка) в её выделенную папку.
- Добавить способ валидировать входящий запрос, например, для вызова инструмента.

### Создание функции

Для создания функции нужно создать файл для этой функции и убедиться, что в нем есть обязательные поля, требуемые для этой функции. Эти поля немного отличаются между инструментами, ресурсами и подсказками.

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

здесь вы видите, как мы делаем следующее:

- Создаём схему с помощью Pydantic `AddInputModel` с полями `a` и `b` в файле *schema.py*.
- Пытаемся разобрать входящий запрос как тип `AddInputModel`, если есть несоответствие параметров — это приведёт к сбою:

   ```python
   # add.py
    try:
        # Проверить ввод с помощью модели Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Вы можете решить, размещать ли эту логику разборки непосредственно в вызове инструмента или в обработчике.

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

- В обработчике для всех вызовов инструментов мы пытаемся разбить входящий запрос в определённую схему инструмента:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    если этот разбор прошёл успешно, тогда мы переходим к вызову самого инструмента:

    ```typescript
    const result = await tool.callback(input);
    ```

Как видно, такой подход создаёт хорошую архитектуру, где всё расположено по своим местам, *server.ts* — это очень небольшой файл, который только связывает обработчики запросов, а каждая функция находится в своей соответствующей папке: tools/, resources/ или prompts/.

Отлично, давайте попробуем это построить далее.

## Упражнение: Создание низкоуровневого сервера

В этом упражнении мы сделаем следующее:

1. Создадим низкоуровневый сервер, который обрабатывает список инструментов и вызов инструментов.
1. Реализуем архитектуру, на которую можно будет опираться.
1. Добавим валидацию, чтобы убедиться, что вызовы ваших инструментов корректны.

### -1- Создаём архитектуру

Первое, что нужно сделать — архитектура, которая помогает нам масштабироваться при добавлении большего количества функций, вот как она выглядит:

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

Теперь мы настроили архитектуру, которая гарантирует, что мы можем легко добавлять новые инструменты в папку tools. Не стесняйтесь добавлять подкаталоги для ресурсов и подсказок.

### -2- Создание инструмента

Далее посмотрим, как создаётся инструмент. Сначала его нужно создать в поддиректории *tool* так:

**Python**

```python
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

Здесь видно, как мы определяем имя, описание и схему ввода с помощью Pydantic, а также обработчик, который вызывается, когда этот инструмент вызывается. Наконец, мы экспортируем `tool_add`, словарь, содержащий все эти свойства.

Есть также *schema.py*, который используется для определения схемы ввода нашего инструмента:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Нужно также заполнить *__init__.py*, чтобы обеспечить обработку директории tools как модуля. Кроме того, нужно экспортировать модули внутри, вот так:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Мы можем продолжать добавлять записи в этот файл по мере добавления инструментов.

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

Здесь мы создаём словарь, состоящий из свойств:

- name — имя инструмента.
- rawSchema — схема Zod, используется для валидации входящих запросов для вызова этого инструмента.
- inputSchema — схема, которая используется обработчиком.
- callback — вызывается для запуска инструмента.

Также есть `Tool`, который преобразует этот словарь в тип, который может принять обработчик mcp сервера, и выглядит это так:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

И есть *schema.ts*, где хранится схемы ввода для каждого инструмента, сейчас там только одна схема, но по мере добавления инструментов там появится больше записей:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Отлично, теперь давайте перейдём к обработке списка инструментов.

### -3- Обработка списка инструментов

Далее, чтобы обработать список инструментов, нам нужно настроить обработчик запросов для этого. Вот что нужно добавить в наш серверный файл:

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

Здесь мы добавляем декоратор `@server.list_tools` и реализуем функцию `handle_list_tools`. В последней нужно сформировать список инструментов. Обратите внимание, что для каждого инструмента необходимы поля имени, описания и inputSchema.

**TypeScript**

Чтобы настроить обработчик запросов для списка инструментов, нужно вызвать `setRequestHandler` на сервере с схемой, подходящей под задачу, в данном случае `ListToolsRequestSchema`.

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
  // Вернуть список зарегистрированных инструментов
  return {
    tools: tools
  };
});
```

Отлично, теперь мы решили задачу по списку инструментов, посмотрим, как можно вызывать инструменты.

### -4- Обработка вызова инструмента

Для вызова инструмента нужно настроить ещё один обработчик запросов, который обрабатывает запрос, указывающий, какую функцию вызвать и с какими аргументами.

**Python**

Используем декоратор `@server.call_tool` и реализуем функцию, например `handle_call_tool`. В ней нужно разобрать имя инструмента, его аргументы и удостовериться, что аргументы валидны для данного инструмента. Валидацию аргументов можно делать либо в этой функции, либо в самом инструменте.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools - это словарь с названиями инструментов в качестве ключей
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # вызов инструмента
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Вот что происходит:

- Имя инструмента уже есть как параметр `name`, а аргументы — в словаре `arguments`.

- Инструмент вызывается так: `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Валидация аргументов происходит в функции, на которую указывает свойство `handler`; если валидация не пройдёт — будет выброшено исключение.

Вот теперь мы полностью понимаем, как работает список и вызов инструментов с использованием низкоуровневого сервера.

Смотрите [полный пример](./code/README.md) здесь

## Задание

Расширьте данный код несколькими инструментами, ресурсами и подсказками и обратите внимание, что вам нужно добавлять файлы только в директории tools и нигде более.

*Решение не предоставляется*

## Итоги

В этой главе мы рассмотрели, как работает подход низкоуровневого сервера и как он помогает создать хорошую архитектуру, на которую можно опираться. Мы также обсудили валидацию и показали, как работать с библиотеками валидации для создания схем проверки ввода.

## Что дальше

- Далее: [Простая аутентификация](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, пожалуйста, учтите, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->