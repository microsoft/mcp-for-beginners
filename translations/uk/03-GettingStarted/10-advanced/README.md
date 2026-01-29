# Розширене використання серверів

У MCP SDK є два типи серверів: звичайний сервер і сервер низького рівня. Зазвичай ви використовуєте звичайний сервер для додавання функцій. Однак у деяких випадках вам може знадобитися сервер низького рівня, наприклад:

- Краща архітектура. Можна створити чисту архітектуру як зі звичайним сервером, так і з сервером низького рівня, але можна стверджувати, що з сервером низького рівня це трохи простіше.
- Доступність функцій. Деякі розширені функції можна використовувати лише з сервером низького рівня. Ви побачите це в наступних розділах, коли ми додамо вибірку та еліцитацію.

## Звичайний сервер vs сервер низького рівня

Ось як виглядає створення MCP Server зі звичайним сервером:

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

Суть полягає в тому, що ви явно додаєте кожен інструмент, ресурс або підказку, які хочете, щоб сервер мав. У цьому немає нічого поганого.

### Підхід сервера низького рівня

Однак, використовуючи підхід сервера низького рівня, вам потрібно мислити інакше, а саме: замість реєстрації кожного інструменту ви створюєте два обробники для кожного типу функцій (інструменти, ресурси або підказки). Наприклад, для інструментів є лише дві функції:

- Перелік усіх інструментів. Одна функція відповідає за всі спроби перерахувати інструменти.
- Обробка викликів усіх інструментів. Тут також є лише одна функція, яка обробляє виклики до інструменту.

Це звучить як потенційно менше роботи, чи не так? Замість реєстрації інструменту, мені просто потрібно переконатися, що інструмент перераховується, коли я перераховую всі інструменти, і що він викликається, коли надходить запит на виклик інструменту.

Давайте подивимося, як тепер виглядає код:

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

Тут ми маємо функцію, яка повертає список функцій. Кожен запис у списку інструментів тепер має поля, такі як `name`, `description` і `inputSchema`, щоб відповідати типу повернення. Це дозволяє нам розміщувати визначення інструментів і функцій в іншому місці. Тепер ми можемо створити всі наші інструменти в папці інструментів, і те ж саме стосується всіх ваших функцій, тому ваш проект може бути організований приблизно так:

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

Чудово, наша архітектура може виглядати досить чисто.

А як щодо виклику інструментів? Чи це та сама ідея — один обробник для виклику інструменту, будь-якого інструменту? Так, саме так, ось код для цього:

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

Як видно з наведеного вище коду, нам потрібно розібрати, який інструмент викликати, з якими аргументами, а потім продовжити виклик інструменту.

## Покращення підходу за допомогою валідації

На даний момент ви бачили, як усі ваші реєстрації для додавання інструментів, ресурсів і підказок можна замінити цими двома обробниками для кожного типу функцій. Що ще нам потрібно зробити? Ну, ми повинні додати якусь форму валідації, щоб переконатися, що інструмент викликається з правильними аргументами. Кожне середовище виконання має своє рішення для цього, наприклад, Python використовує Pydantic, а TypeScript — Zod. Ідея полягає в наступному:

- Перенести логіку створення функції (інструменту, ресурсу або підказки) до її спеціальної папки.
- Додати спосіб перевірки вхідного запиту, наприклад, на виклик інструменту.

### Створення функції

Щоб створити функцію, нам потрібно створити файл для цієї функції та переконатися, що він має обов’язкові поля, необхідні для цієї функції. Які поля відрізняються між інструментами, ресурсами та підказками.

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

Тут ви можете побачити, як ми робимо наступне:

- Створюємо схему за допомогою Pydantic `AddInputModel` з полями `a` і `b` у файлі *schema.py*.
- Намагаємося розібрати вхідний запит, щоб він був типу `AddInputModel`. Якщо є невідповідність параметрів, це призведе до помилки:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Ви можете вибрати, чи розміщувати цю логіку розбору у самому виклику інструменту чи у функції обробника.

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

- У обробнику, який обробляє всі виклики інструментів, ми тепер намагаємося розібрати вхідний запит у визначену схему інструменту:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    якщо це працює, то ми продовжуємо викликати фактичний інструмент:

    ```typescript
    const result = await tool.callback(input);
    ```

Як видно, цей підхід створює чудову архітектуру, оскільки все має своє місце: *server.ts* — це дуже маленький файл, який лише підключає обробники запитів, а кожна функція знаходиться у своїй відповідній папці, тобто tools/, resources/ або /prompts.

Чудово, давайте спробуємо побудувати це далі.

## Вправа: Створення сервера низького рівня

У цій вправі ми зробимо наступне:

1. Створимо сервер низького рівня, який обробляє перелік інструментів і виклики інструментів.
1. Реалізуємо архітектуру, яку можна розширювати.
1. Додамо валідацію, щоб переконатися, що виклики ваших інструментів правильно перевіряються.

### -1- Створення архітектури

Перше, що нам потрібно вирішити, це архітектура, яка допоможе нам масштабуватися, коли ми додаємо більше функцій. Ось як це виглядає:

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

Тепер ми налаштували архітектуру, яка гарантує, що ми можемо легко додавати нові інструменти в папку інструментів. Ви можете додати підкаталоги для ресурсів і підказок.

### -2- Створення інструменту

Давайте подивимося, як виглядає створення інструменту. Спочатку його потрібно створити у підкаталозі *tool*, наприклад:

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

Тут ми бачимо, як ми визначаємо ім’я, опис, схему вводу за допомогою Pydantic і обробник, який буде викликаний, коли цей інструмент буде викликано. Нарешті, ми експортуємо `tool_add`, який є словником, що містить усі ці властивості.

Також є *schema.py*, який використовується для визначення схеми вводу, що використовується нашим інструментом:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Нам також потрібно заповнити *__init__.py*, щоб переконатися, що каталог інструментів розглядається як модуль. Крім того, нам потрібно експортувати модулі всередині нього, наприклад:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Ми можемо продовжувати додавати до цього файлу, коли додаємо більше інструментів.

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

Тут ми створюємо словник, що складається з властивостей:

- name — це ім’я інструменту.
- rawSchema — це схема Zod, яка буде використовуватися для перевірки вхідних запитів на виклик цього інструменту.
- inputSchema — ця схема буде використовуватися обробником.
- callback — використовується для виклику інструменту.

Також є `Tool`, який використовується для перетворення цього словника у тип, який може прийняти обробник сервера MCP, і він виглядає так:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

І є *schema.ts*, де ми зберігаємо схеми вводу для кожного інструменту, який виглядає так, з лише однією схемою на даний момент, але коли ми додаємо інструменти, можемо додати більше записів:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Чудово, давайте перейдемо до обробки переліку наших інструментів.

### -3- Обробка переліку інструментів

Далі, щоб обробити перелік наших інструментів, нам потрібно налаштувати обробник запитів для цього. Ось що нам потрібно додати до нашого серверного файлу:

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

Тут ми додаємо декоратор `@server.list_tools` і реалізуємо функцію `handle_list_tools`. У останній нам потрібно створити список інструментів. Зверніть увагу, що кожен інструмент повинен мати ім’я, опис і inputSchema.

**TypeScript**

Щоб налаштувати обробник запитів для переліку інструментів, нам потрібно викликати `setRequestHandler` на сервері зі схемою, яка відповідає тому, що ми намагаємося зробити, у цьому випадку `ListToolsRequestSchema`.

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

Чудово, тепер ми вирішили питання переліку інструментів, давайте подивимося, як ми можемо викликати інструменти.

### -4- Обробка виклику інструменту

Щоб викликати інструмент, нам потрібно налаштувати ще один обробник запитів, цього разу зосереджений на обробці запиту, який вказує, яку функцію викликати і з якими аргументами.

**Python**

Давайте використаємо декоратор `@server.call_tool` і реалізуємо його за допомогою функції, наприклад, `handle_call_tool`. У цій функції нам потрібно розібрати ім’я інструменту, його аргументи та переконатися, що аргументи є дійсними для даного інструменту. Ми можемо перевірити аргументи у цій функції або далі у фактичному інструменті.

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

Ось що відбувається:

- Ім’я нашого інструменту вже присутнє як вхідний параметр `name`, що також стосується наших аргументів у вигляді словника `arguments`.

- Інструмент викликається за допомогою `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Перевірка аргументів відбувається у властивості `handler`, яка вказує на функцію. Якщо перевірка не пройде, буде піднято виняток.

Ось так ми отримали повне розуміння переліку та виклику інструментів за допомогою сервера низького рівня.

Дивіться [повний приклад](./code/README.md) тут.

## Завдання

Розширте код, який вам було надано, додавши кілька інструментів, ресурсів і підказок, і подумайте, як ви помітили, що вам потрібно лише додавати файли в каталог інструментів і ніде більше.

*Рішення не надано*

## Підсумок

У цьому розділі ми побачили, як працює підхід сервера низького рівня і як це може допомогти нам створити гарну архітектуру, яку можна продовжувати розвивати. Ми також обговорили валідацію і вам було показано, як працювати з бібліотеками валідації для створення схем для перевірки вводу.

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.