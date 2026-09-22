# Розширене використання сервера

У MCP SDK є два різні типи серверів: ваш звичайний сервер і низькорівневий сервер. Зазвичай ви використовуєте звичайний сервер для додавання функцій. Але в деяких випадках ви хочете покладатися на низькорівневий сервер, наприклад:

- Краща архітектура. Можна створити чисту архітектуру як зі звичайним сервером, так і з низькорівневим сервером, але можна стверджувати, що з низькорівневим сервером це трохи простіше.
- Доступність функцій. Деякі просунуті функції можна використовувати лише з
    низькорівневим сервером. Наступні розділи охоплюють Elicitation та застарілу функцію Sampling,
    яка застаріла в MCP `2026-07-28`.

## Звичайний сервер проти низькорівневого сервера

Ось як виглядає створення MCP Server зі звичайним сервером

**Python**

```python
mcp = FastMCP("Demo")

# Додати інструмент для додавання
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

// Додати інструмент додавання
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

Ідея в тому, що ви явно додаєте кожен інструмент, ресурс або запит, які хочете, щоб сервер мав. У цьому немає нічого поганого.  

### Підхід низькорівневого сервера

Однак при використанні низькорівневого серверного підходу потрібно думати інакше. Замість реєстрації кожного інструмента ви створюєте два обробники на тип функції (інструменти, ресурси або запити). Наприклад, інструменти мають лише дві функції:

- Перелічення усіх інструментів. Одна функція відповідає за всі спроби вивести інструменти.
- Обробка викликів усіх інструментів. Тут теж є лише одна функція для обробки викликів інструмента.

Звучить потенційно менше роботи, так? Тож замість реєстрації інструмента, мені потрібно лише переконатися, що інструмент перелічений при виведенні усіх інструментів і що його викликають при надходженні запиту на виклик інструмента. 

Давайте подивимось, як тепер виглядає код:

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
  // Повернути список зареєстрованих інструментів
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

Тепер у нас є функція, яка повертає список функцій. Кожен запис у списку інструментів тепер має поля `name`, `description` і `inputSchema` відповідно до типу повернення. Це дозволяє розміщувати наші інструменти та визначення функцій окремо. Ми можемо створити всі наші інструменти в папці tools і те саме стосується всіх ваших функцій, тож ваш проект може бути організований ось так:

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

Чудово, нашу архітектуру можна зробити досить чистою.

А що з викликом інструментів, чи це також одна ідея — один обробник для виклику інструмента, будь-якого інструмента? Так, саме так, ось код для цього:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools є словником з іменами інструментів як ключами
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
    // TODO викликати інструмент,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Як видно з наведеного коду, нам потрібно розпарсити, який інструмент викликати і з якими аргументами, а потім перейти до виклику інструмента.

## Покращення підходу за допомогою валідації

Дотепер ви бачили, як усі ваші реєстрації для додавання інструментів, ресурсів та запитів можна замінити цими двома обробниками на тип функції. Що ще потрібно зробити? Нам слід додати якусь форму валідації, щоб переконатися, що інструмент викликають з правильними аргументами. Кожне середовище виконання має своє рішення для цього, наприклад Python використовує Pydantic, а TypeScript — Zod. Ідея полягає в тому, що ми робимо наступне:

- Переносимо логіку створення функції (інструмент, ресурс або запит) в окрему папку.
- Додаємо спосіб перевірки вхідного запиту, наприклад, на виклик інструмента.

### Створення функції

Щоб створити функцію, нам потрібно створити файл для цієї функції та переконатися, що він має обов’язкові поля, потрібні для цієї функції. Поля дещо відрізняються між інструментами, ресурсами та запитами.

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
        # Перевірка вхідних даних за допомогою моделі Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: додати Pydantic, щоб ми могли створити AddInputModel і перевірити аргументи

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Тут видно, як ми робимо таке:

- Створюємо схему за допомогою Pydantic `AddInputModel` з полями `a` та `b` у файлі *schema.py*.
- Намагання розпарсити вхідний запит як тип `AddInputModel`, якщо параметри не співпадають, відбудеться збій:

   ```python
   # add.py
    try:
        # Перевірте вхідні дані за допомогою моделі Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Ви можете вибрати, чи поміщати цю логіку парсингу в сам виклик інструмента або в обробник.

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

- В обробнику, що працює з усіма викликами інструментів, ми намагаємось розпарсити вхідний запит у визначену інструментом схему:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    якщо це вдається, то переходимо до виклику самого інструмента:

    ```typescript
    const result = await tool.callback(input);
    ```

Як бачимо, цей підхід створює відмінну архітектуру, оскільки все має своє місце, *server.ts* є дуже маленьким файлом, який лише підключає обробники запитів, а кожна функція знаходиться у відповідних папках: tools/, resources/ або prompts/.

Чудово, давайте спробуємо це побудувати далі. 

## Вправа: Створення низькорівневого сервера

У цій вправі ми зробимо таке:

1. Створимо низькорівневий сервер, який обробляє перелік інструментів і виклики інструментів.
1. Реалізуємо архітектуру, на якій можна розвиватися.
1. Додамо валідацію, щоб переконатися, що виклики інструментів проходять коректну перевірку.

### -1- Створення архітектури

Перш за все нам потрібно зробити архітектуру, яка допоможе нам масштабуватись при додаванні нових функцій, ось як вона виглядає:

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

Тепер ми налаштували архітектуру, що дозволяє легко додавати нові інструменти в папку tools. Ви можете додати підпапки для resources і prompts.

### -2- Створення інструмента

Далі подивимось, як створюється інструмент. По-перше, його потрібно створити у власній підпапці *tool* так:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Перевірити введення за допомогою моделі Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: додати Pydantic, щоб ми могли створити AddInputModel і перевірити аргументи

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Тут ми визначаємо ім'я, опис і вхідну схему за допомогою Pydantic, а також обробник, який буде викликаний, коли цей інструмент буде викликатися. Нарешті, ми експонуємо `tool_add`, що є словником із цими властивостями.

Є також *schema.py*, який визначає схему введення для нашого інструмента:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Ми також повинні наповнити *__init__.py*, щоб каталог інструментів розглядався як модуль. Крім того, потрібно експонувати модулі всередині нього так:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Ми можемо додавати до цього файлу, коли додаємо нові інструменти.

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

- name, це ім'я інструмента.
- rawSchema, це Zod схема, яка використовується для валідації вхідних запитів на виклик цього інструмента.
- inputSchema, цю схему використовує обробник.
- callback, використовується для виклику інструмента.

Є також тип `Tool`, який перетворює цей словник у тип, прийнятний для обробника mcp сервера, і він виглядає так:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

І є *schema.ts*, де зберігаємо схеми введення для кожного інструмента, який зараз має одну схему, але з часом ми можемо додавати більше:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Чудово, тепер перейдемо до обробки переліку інструментів.

### -3- Обробка переліку інструментів

Далі, щоб обробити перелік інструментів, нам потрібно встановити обробник запитів для цього. Ось що потрібно додати у файл сервера:

**Python**

```python
# код опущено для стислості
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

Тут ми додаємо декоратор `@server.list_tools` і реалізуємо функцію `handle_list_tools`. У ній нам потрібно повернути список інструментів. Зверніть увагу, що кожен інструмент має мати ім’я, опис і inputSchema.   

**TypeScript**

Для налаштування обробника запитів для переліку інструментів потрібно викликати `setRequestHandler` на сервері із схемою, що відповідає тому, що ми хочемо зробити — тут це `ListToolsRequestSchema`.

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
// код опущено для стислості
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Повернути список зареєстрованих інструментів
  return {
    tools: tools
  };
});
```

Чудово, тепер ми розв’язали задачу переліку інструментів, подивимось, як ми можемо викликати інструменти.

### -4- Обробка виклику інструмента

Щоб викликати інструмент, нам потрібно налаштувати ще один обробник запитів, цього разу для обробки запиту, в якому вказано, яку функцію викликати і з якими аргументами.

**Python**

Використаємо декоратор `@server.call_tool` і реалізуємо його функцією `handle_call_tool`. Усередині цієї функції потрібно розпарсити ім’я інструмента, його аргументи та переконатися, що аргументи дійсні для цього інструмента. Валідацію можна зробити в цій функції або пізніше в самому інструменті.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools - це словник з назвами інструментів як ключами
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # викликати інструмент
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Ось що відбувається:

- Ім'я нашого інструмента вже є вхідним параметром `name`, а аргументи у вигляді словника `arguments`.

- Інструмент викликається за допомогою `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Валідація аргументів відбувається в властивості `handler`, яка є функцією; якщо валідація не пройшла, буде викликана помилка.

Отже, тепер у нас повне розуміння переліку та виклику інструментів з використанням низькорівневого сервера.

Дивіться [повний приклад](./code/README.md) тут

## Завдання

Розширте наданий код кількома інструментами, ресурсами та запитами та задумайтесь, що вам потрібно лише додавати файли в каталог tools і ніде більше. 

*Рішення не надається*

## Підсумок

У цьому розділі ми побачили, як працює підхід низькорівневого сервера і як він може допомогти створити чисту архітектуру, яку можна розвивати далі. Ми також обговорили валідацію і показали, як працювати з бібліотеками валідації для створення схем валідації введення.

## Що далі

- Наступне: [Проста аутентифікація](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->