# Розширене використання сервера

Існують два різні типи серверів, доступних у MCP SDK, ваш звичайний сервер та низькорівневий сервер. Зазвичай ви б використовували звичайний сервер, щоб додавати до нього функції. Однак у деяких випадках вам може знадобитися покладатися на низькорівневий сервер, наприклад:

- Краще архітектура. Можна створити чисту архітектуру як за допомогою звичайного сервера, так і низькорівневого, але можна стверджувати, що це трохи простіше з низькорівневим сервером.
- Доступність функцій. Деякі розширені функції можна використовувати лише з низькорівневим сервером. Ви побачите це в наступних розділах, коли ми додаватимемо вибірку та еліцитацію.

## Звичайний сервер проти низькорівневого сервера

Ось як виглядає створення MCP Server із звичайним сервером

**Python**

```python
mcp = FastMCP("Demo")

# Додайте інструмент додавання
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

Ідея в тому, що ви явно додаєте кожен інструмент, ресурс або підказку, яку хочете, щоб сервер мав. Немає в цьому нічого поганого.  

### Підхід низькорівневого сервера

Однак, коли ви використовуєте підхід низькорівневого сервера, вам потрібно мислити інакше. Замість того, щоб реєструвати кожен інструмент окремо, ви створюєте два обробники на тип функції (інструменти, ресурси або підказки). Тобто, наприклад, для інструментів тепер лише дві функції:

- Перелік усіх інструментів. Одна функція відповідає за всі спроби отримати список інструментів.
- Обробка виклику будь-якого інструменту. Тут також є лише одна функція, яка обробляє виклики інструментів.

Звучить як менше роботи, правда? Тож замість реєстрації інструменту мені потрібно переконатися, що інструмент відображений, коли я отримую список усіх інструментів, і що він викликається, коли надходить запит на виклик інструменту.

Подивімося, як тепер виглядає код:

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

Тут тепер у нас функція, що повертає список функцій. Кожен запис у списку інструментів зараз має поля, як-от `name`, `description` та `inputSchema`, щоб відповідати типу повернення. Це дає нам змогу розміщувати інструменти та визначення функцій в іншому місці. Тепер ми можемо створити всі наші інструменти у папці tools і так само для усіх ваших функцій — ваш проєкт може бути організований так:

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

Це чудово, наша архітектура може виглядати досить чистою.

А як щодо виклику інструментів, чи те саме? Один обробник для виклику будь-якого інструменту? Так, саме так, ось код для цього:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools — це словник із назвами інструментів у якості ключів
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

Як видно з наведеного коду, нам потрібно витягти інструмент для виклику та з якими аргументами, а потім перейти до виклику цього інструменту.

## Покращення підходу за допомогою перевірки правильності (валідації)

Поки що ви побачили, як усі ваші реєстрації для додавання інструментів, ресурсів та підказок можна замінити цими двома обробниками на тип функції. Що ще потрібно зробити? Ну, варто додати якусь форму перевірки, щоб упевнитися, що інструмент викликається з правильними аргументами. Кожне середовище виконання має своє рішення для цього, наприклад Python використовує Pydantic, а TypeScript — Zod. Ідея полягає в наступному:

- Перенести логіку створення функції (інструменту, ресурсу або підказки) у її власну папку.
- Додати спосіб перевірки вхідних запитів, які наприклад просять викликати інструмент.

### Створення функції

Щоб створити функцію, нам потрібно створити файл для цієї функції і переконатися, що в ньому є обов’язкові поля, необхідні для цієї функції. Поля трішки відрізняються між інструментами, ресурсами та підказками.

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

Тут ви можете побачити, як ми робимо наступне:

- Створюємо схему за допомогою Pydantic — `AddInputModel` з полями `a` та `b` у файлі *schema.py*.
- Прагнемо розпарсити вхідний запит як тип `AddInputModel`, якщо параметри не співпадають — це призведе до помилки:

   ```python
   # add.py
    try:
        # Перевірте введені дані за допомогою моделі Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Ви можете вибрати, чи розміщувати цю логіку розбору в виклику інструменту або в обробнику.

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

- В обробнику, що працює з усіма викликами інструментів, тепер намагаємося розпарсити вхідний запит за схемою, визначеною для інструменту:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    якщо це спрацює, тоді переходимо до виклику власне інструменту:

    ```typescript
    const result = await tool.callback(input);
    ```

Як видно, цей підхід створює чудову архітектуру, адже все має своє місце: *server.ts* — дуже маленький файл, що лише з’єднує обробники запитів, а кожна функція знаходиться у своїй відповідній папці, наприклад tools/, resources/ або prompts/.

Чудово, тепер спробуємо це побудувати.

## Вправа: Створення низькорівневого сервера

У цій вправі ми зробимо таке:

1. Створимо низькорівневий сервер, що обробляє список інструментів і виклики інструментів.
2. Реалізуємо архітектуру, на якій можна буде будувати надалі.
3. Додамо перевірку, щоб забезпечити коректність викликів інструментів.

### -1- Створення архітектури

Перше, що потрібно зробити — це архітектура, що допоможе нам масштабуватися при додаванні нових функцій, ось як вона виглядає:

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

Тепер ми налаштували архітектуру, яка забезпечує легке додавання нових інструментів у папці tools. Вільно додавайте туди підпапки для resources та prompts.

### -2- Створення інструменту

Подивимося, як виглядає створення інструменту. По-перше, він має бути створений у власній підпапці tool, ось так:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Перевірити вхідні дані за допомогою моделі Pydantic
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

Тут ми визначаємо ім’я, опис і вхідну схему за допомогою Pydantic та обробник, який буде викликаний при виклику цього інструменту. Нарешті, ми експортуємо `tool_add`, який є словником, що містить усі ці властивості.

Також є файл *schema.py*, де визначається вхідна схема, що використовується у нашому інструменті:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Також потрібно наповнити *__init__.py*, щоб каталог tools розглядався як модуль. Крім того, потрібно експортувати модулі в ньому ось так:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Ми можемо додавати до цього файлу нові інструменти у міру потреби.

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

Тут ми створюємо словник з такими властивостями:

- name — ім’я інструменту.
- rawSchema — схема Zod, яка використовується для перевірки вхідних запитів на виклик цього інструменту.
- inputSchema — ця схема використовується обробником.
- callback — функція, яка виконує виклик інструменту.

Також існує тип `Tool`, який конвертує цей словник у тип, що може прийняти обробник сервера mcp, і він виглядає так:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

І є *schema.ts*, де зберігаються вхідні схеми для кожного інструменту, наразі з однією схемою, але по мірі додавання нових інструментів там з’являтимуться нові записи:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Чудово, тепер перейдемо до обробки списку інструментів.

### -3- Обробка списку інструментів

Для обробки списку інструментів нам потрібно налаштувати обробник запитів для цього. Ось що потрібно додати у файл сервера:

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

Тут додаємо декоратор `@server.list_tools` і реалізуємо функцію `handle_list_tools`. В останній потрібно сформувати список інструментів. Зверніть увагу, що кожен інструмент має мати ім’я, опис та поле inputSchema.   

**TypeScript**

Щоб налаштувати обробник запитів на список інструментів, потрібно викликати `setRequestHandler` на сервері із схемою, що відповідає тому, що ми хочемо зробити, в даному випадку `ListToolsRequestSchema`. 

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

Чудово, тепер ми розв’язали частину зі списком інструментів, давайте подивимося, як ми можемо викликати інструменти.

### -4- Обробка виклику інструменту

Для виклику інструменту потрібно налаштувати ще один обробник, який працюватиме з запитом, що вказує, який саме інструмент викликати і з якими аргументами.

**Python**

Використаємо декоратор `@server.call_tool` і реалізуємо функцію на кшталт `handle_call_tool`. У цій функції нам потрібно витягти ім’я інструменту, його аргументи і переконатися, що аргументи підходять конкретному інструменту. Перевірку можна робити тут або у власне самому інструменті.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools — це словник з іменами інструментів у вигляді ключів
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

- Ім’я інструменту вже присутнє як вхідний параметр `name`, а аргументи — у словнику `arguments`.

- Інструмент викликається рядком `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Перевірка аргументів відбувається у властивості `handler`, яка посилається на функцію; якщо вона не виконана, виникне виключення.

Отже, тепер ми маємо повне розуміння, як отримати список інструментів і викликати їх за допомогою низькорівневого сервера.

Дивіться [повний приклад](./code/README.md) тут

## Завдання

Розширте наданий вам код кількома інструментами, ресурсами і підказками та помітьте, що вам потрібно додавати файли лише у папку tools і ніде більше. 

*Розв’язок не надається*

## Підсумок

У цьому розділі ми побачили, як працює підхід низькорівневого сервера і як він допомагає створити гарну архітектуру, на якій можна продовжувати будувати. Ми також обговорили перевірку вхідних даних і вам показали, як працювати з бібліотеками для валідації, створюючи схеми для перевірки вхідних даних.

## Що далі

- Далі: [Проста автентифікація](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ його рідною мовою слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->