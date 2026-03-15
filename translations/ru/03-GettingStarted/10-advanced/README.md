# Расширенное использование сервера

В SDK MCP представлены два разных типа серверов: стандартный сервер и низкоуровневый сервер. Обычно вы используете обычный сервер для добавления к нему функций. Однако в некоторых случаях желательно использовать низкоуровневый сервер, например:

- Лучшая архитектура. Можно создать чистую архитектуру и с обычным сервером, и с низкоуровневым сервером, но можно утверждать, что с низкоуровневым сервером это немного проще.
- Доступность функций. Некоторые продвинутые функции можно использовать только с низкоуровневым сервером. Вы увидите это в следующих главах, когда мы добавим сэмплирование и вызываемые подсказки.

## Обычный сервер против низкоуровневого сервера

Вот как создаётся MCP сервер с обычным сервером

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

Суть в том, что вы явно добавляете каждый инструмент, ресурс или подсказку, которую хотите иметь на сервере. В этом нет ничего плохого.  

### Подход низкоуровневого сервера

Однако при использовании подхода низкоуровневого сервера необходимо мыслить иначе. Вместо регистрации каждого инструмента вы создаёте два обработчика для каждого типа функций (инструменты, ресурсы или подсказки). Например, у инструментов всего две функции:

- Вывод списка всех инструментов. Одна функция отвечает за все попытки получить список инструментов.
- Обработка вызовов всех инструментов. Здесь также есть всего одна функция, обрабатывающая вызовы инструмента.

Звучит как потенциально меньше работы, не так ли? Вместо регистрации инструмента, достаточно убедиться, что инструмент присутствует в списке при выводе всех инструментов и вызывается при поступлении запроса на вызов инструмента.

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

Теперь у нас есть функция, которая возвращает список функций. Каждая запись в списке инструментов имеет поля, такие как `name`, `description` и `inputSchema` для соответствия типу возвращаемого значения. Это позволяет нам хранить определение инструментов и функций в другом месте. Теперь мы можем создать все наши инструменты в папке tools и так же поступать со всеми функциями, поэтому ваш проект может быть организован так:

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

Отлично, наша архитектура может выглядеть довольно аккуратно.

А как насчёт вызова инструментов, это та же идея — один обработчик для вызова инструмента, любого инструмента? Да, именно так, вот код для этого:

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

Как видно из кода выше, нам нужно распарсить, какой инструмент вызвать и с какими аргументами, а потом перейти к вызову инструмента.

## Улучшение подхода с помощью валидации

До сих пор вы видели, как все регистрации для добавления инструментов, ресурсов и подсказок можно заменить двумя обработчиками на каждый тип функций. Что еще нужно сделать? Нужно добавить какую-то форму проверки, чтобы гарантировать, что инструмент вызывается с правильными аргументами. Каждая среда выполнения имеет собственное решение: например, Python использует Pydantic, TypeScript — Zod. Идея заключается в следующем:

- Перенести логику создания функции (инструмент, ресурс или подсказка) в отдельную папку.
- Добавить способ валидации входящего запроса на вызов инструмента, например.

### Создание функции

Чтобы создать функцию, необходимо создать файл для этой функции и убедиться, что в нем есть обязательные поля, требуемые для этой функции. Эти поля несколько различаются между инструментами, ресурсами и подсказками.

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
        # Проверить входные данные с помощью модели Pydantic
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

здесь видно, как мы делаем следующее:

- Создаём схему с помощью Pydantic `AddInputModel` с полями `a` и `b` в файле *schema.py*.
- Пытаемся распарсить входящий запрос как тип `AddInputModel`, если параметры не совпадают, это приведёт к сбою:

   ```python
   # add.py
    try:
        # Проверить ввод с использованием модели Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Можно выбрать, где именно разместить эту логику парсинга — в самом вызове инструмента или в функции-обработчике.

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

- В обработчике, который обрабатывает все вызовы инструментов, мы пытаемся распарсить входящий запрос в определённую для инструмента схему:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    если это работает, то переходим к вызову самого инструмента:

    ```typescript
    const result = await tool.callback(input);
    ```

Как вы видите, такой подход создаёт отличную архитектуру, так как всё имеет своё место, файл *server.ts* очень небольшой и только связывает обработчики запросов, а каждая функция находится в своей папке, например tools/, resources/ или prompts/.

Отлично, теперь давайте попробуем создать это.

## Упражнение: Создание низкоуровневого сервера

В этом упражнении мы сделаем следующее:

1. Создадим низкоуровневый сервер, обрабатывающий вывод списка инструментов и вызов инструментов.
1. Реализуем архитектуру, на которой можно будет строить дальше.
1. Добавим валидацию, чтобы гарантировать правильность вызовов инструментов.

### -1- Создание архитектуры

Первое, что нам нужно сделать — создать архитектуру, которая поможет масштабироваться по мере добавления функций, она выглядит так:

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

Теперь у нас настроена архитектура, которая позволяет легко добавлять новые инструменты в папку tools. Не стесняйтесь создавать подобные подпапки для ресурсов и подсказок.

### -2- Создание инструмента

Далее посмотрим, как создаётся инструмент. Сначала его нужно создать в своей подпапке *tool* так:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Проверить входные данные с помощью модели Pydantic
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

Здесь мы определяем имя, описание и схему ввода с помощью Pydantic, а также обработчик, который вызывается, когда инструмент вызывается. В конце экспортируем `tool_add`, который является словарём со свойствами.

Также есть *schema.py*, где определяется схема ввода для нашего инструмента:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Нужно также заполнить *__init__.py*, чтобы папка tools рассматривалась как модуль. Кроме того, необходимо экспортировать модули из неё так:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Мы можем дополнять этот файл по мере добавления инструментов.

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
- rawSchema — Zod схема, которая будет использоваться для валидации входящих запросов на вызов инструмента.
- inputSchema — эта схема будет использоваться обработчиком.
- callback — вызывается для выполнения инструмента.

Также есть тип `Tool`, который преобразует этот словарь в тип, который принимает обработчик MCP сервера, он выглядит так:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

И есть *schema.ts*, где хранятся схемы ввода для каждого инструмента, сейчас только одна схема, но по мере добавления инструментов будет больше:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Отлично, теперь займемся обработкой вывода списка инструментов.

### -3- Обработка вывода списка инструментов

Далее, чтобы обработать вывод списка инструментов, нужно настроить обработчик запросов. Вот что нужно добавить в файл сервера:

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

Здесь мы добавляем декоратор `@server.list_tools` и реализуем функцию `handle_list_tools`. В этой функции нужно создать список инструментов. Обратите внимание, что каждый инструмент должен иметь name, description и inputSchema.   

**TypeScript**

Чтобы настроить обработчик запроса для вывода списка инструментов, нужно вызвать `setRequestHandler` на сервере с подходящей схемой, в нашем случае `ListToolsRequestSchema`. 

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

Отлично, теперь задача вывода списка инструментов решена, перейдём к вызову инструментов.

### -4- Обработка вызова инструмента

Для вызова инструмента нужно настроить ещё один обработчик запросов, который обрабатывает запросы, указывающие, какую функцию вызвать и с какими аргументами.

**Python**

Используем декоратор `@server.call_tool` и реализуем функцию `handle_call_tool`. Внутри неё нужно распарсить имя инструмента, аргументы и проверить, что аргументы валидны для данного инструмента. Валидировать можно здесь или непосредственно в самом инструменте.

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
        # вызвать инструмент
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Вот что происходит:

- Имя инструмента уже есть во входящем параметре `name`, аргументы передаются в виде словаря `arguments`.

- Инструмент вызывается как `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Валидация аргументов происходит в свойстве `handler`, ссылающемся на функцию; если валидация не пройдёт, возникнет исключение.

Вот теперь у нас есть полное понимание работы с выводом списка и вызовом инструментов с помощью низкоуровневого сервера.

Смотрите [полный пример](./code/README.md) здесь

## Домашнее задание

Расширьте предоставленный код, добавив несколько инструментов, ресурсов и подсказок, и понаблюдайте, что для этого достаточно добавлять файлы только в папку tools и больше нигде.

*Решение не предоставляется*

## Итоги

В этой главе мы рассмотрели, как работает подход низкоуровневого сервера и как с его помощью можно создать чистую архитектуру для дальнейшего развития. Мы также обсудили валидацию и показали, как работать с библиотеками валидации для создания схем для проверки входных данных.

## Что дальше

- Далее: [Простая аутентификация](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неверное толкование, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->