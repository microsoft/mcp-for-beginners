# Розширене використання сервера

У MCP SDK представлені два різні типи серверів: ваш звичайний сервер і низькорівневий сервер. Зазвичай ви використовуєте звичайний сервер для додавання до нього функцій. Проте в деяких випадках ви хочете покладатися на низькорівневий сервер, наприклад:

- Краща архітектура. Можливо створити чисту архітектуру із використанням і звичайного сервера, і низькорівневого сервера, але можна стверджувати, що це трохи простіше з низькорівневим сервером.
- Наявність функцій. Деякі розширені функції можуть використовуватись тільки з низькорівневим сервером. Ви побачите це у наступних розділах, коли ми додамо семплювання та еліцитацію.

## Звичайний сервер проти низькорівневого сервера

Ось як виглядає створення MCP серверу зі звичайним сервером

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

// Додайте інструмент додавання
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

Суть у тому, що ви явно додаєте кожен інструмент, ресурс або запит, який хочете, щоб сервер підтримував. Тут немає нічого поганого.

### Підхід з низькорівневим сервером

Проте, коли ви використовуєте підхід низькорівневого сервера, потрібно думати інакше. Замість реєстрації кожного інструмента, ви створюєте по два обробники на тип функції (інструменти, ресурси або запити). Наприклад, у разі інструментів є лише дві функції:

- Перелік усіх інструментів. Одна функція відповідає за всі спроби отримати список інструментів.
- Обробка виклику інструментів. Також тут лише одна функція, що опрацьовує виклики інструментів.

Звучить як потенційно менше роботи, правда? Отже, замість реєстрації інструмента, просто потрібно переконатися, що він перелічується при запиті списку інструментів і що він викликається при надходженні запиту на виклик інструмента.

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

Тут у нас є функція, що повертає список функцій. Кожен запис у списку інструментів тепер має поля `name`, `description` та `inputSchema` відповідно до типу повернення. Це дозволяє розміщувати визначення інструментів і функцій у іншому місці. Тепер ми можемо створити всі наші інструменти у папці tools і так само для всіх інших функцій, тож ваш проєкт може бути організований ось так:

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

А що з викликом інструментів, чи та сама ідея — один обробник для виклику будь-якого інструмента? Так, саме так, ось код для цього:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools є словником з назвами інструментів як ключі
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

Як бачите з наведеного коду, нам потрібно розпарсити, який інструмент викликати і з якими аргументами, а потім здійснити виклик цього інструмента.

## Поліпшення підходу через валідацію

Поки що ви побачили, як усі ваші реєстрації для додавання інструментів, ресурсів та запитів можна замінити цими двома обробниками на тип функції. Що ще треба зробити? Ну, варто додати якусь форму валідації, щоб переконатися, що інструмент викликається з правильними аргументами. Кожне середовище виконання має своє рішення для цього, наприклад Python використовує Pydantic, а TypeScript – Zod. Ідея в тому, що ми робимо таке:

- Переносимо логіку створення функції (інструмент, ресурс або запит) у відповідну папку.
- Додаємо спосіб перевірки вхідного запиту, наприклад, що викликає інструмент.

### Створення функції

Щоб створити функцію, потрібно створити файл для цієї функції і переконатися, що в ньому є необхідні обов’язкові поля. Ці поля дещо відрізняються між інструментами, ресурсами і запитами.

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
        # Перевірка введення за допомогою моделі Pydantic
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

Тут можна побачити, як ми робимо наступне:

- Створюємо схему за допомогою Pydantic `AddInputModel` з полями `a` і `b` у файлі *schema.py*.
- Прагнемо розпарсити вхідний запит як тип `AddInputModel`; якщо параметри не співпадають, це спричинить помилку:

   ```python
   # add.py
    try:
        # Перевірте вхідні дані за допомогою моделі Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Ви можете обрати, чи розміщувати цю логіку парсингу безпосередньо у виклику інструмента або в обробнику.

**TypeScript**

```typescript
// сервер.ts
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

       // @ts-ігнорувати
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

// схема.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// додати.ts
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

- В обробнику, що опрацьовує всі виклики інструментів, ми тепер намагаємося розпарсити вхідний запит у визначену для цього інструмента схему:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    якщо це вдається, тоді виконуємо виклик самого інструмента:

    ```typescript
    const result = await tool.callback(input);
    ```

Як бачите, цей підхід створює гарну архітектуру, адже все має своє місце, *server.ts* — дуже маленький файл, який лише підключає обробники запитів, а кожна функція розміщена у відповідній папці, тобто tools/, resources/ або prompts/.

Чудово, давайте спробуємо створити це далі.

## Вправа: Створення низькорівневого сервера

У цій вправі ми зробимо таке:

1. Створимо низькорівневий сервер, який обробляє перелік інструментів і виклики інструментів.
2. Запровадимо архітектуру, на якій можна будується.
3. Додамо валідацію, щоб впевнитися, що виклики інструментів коректно перевіряються.

### -1- Створення архітектури

Перше, що потрібно зробити, — це архітектура, що допомагає масштабуватися при додаванні нових функцій. Ось як це виглядає:

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

Тепер ми налаштували архітектуру, що забезпечує легке додавання нових інструментів у папку tools. Не соромтеся додавати підпапки для ресурсів та запитів.

### -2- Створення інструмента

Далі подивимось, як виглядає створення інструмента. По-перше, він має бути створений у відповідній підпапці tools так:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Перевірити вхідні дані за допомогою моделі Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: додати Pydantic, щоб ми могли створити AddInputModel і перевіряти аргументи

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Тут видно, як ми визначаємо назву, опис і схему вхідних даних за допомогою Pydantic та обробник, який викликається при виклику інструмента. Врешті-решт ми експортуємо `tool_add` — словник з усіма цими властивостями.

Також є *schema.py*, який визначає схему вхідних даних, що використовує наш інструмент:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Також потрібно заповнити *__init__.py*, щоб каталог tools розглядався як модуль. Крім того, потрібно експортувати з нього модулі ось так:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Цей файл можна розширювати додаючи більше інструментів.

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

Тут ми створюємо словник зі властивостями:

- name — назва інструмента.
- rawSchema — схема Zod, що використовується для валідації вхідних викликів інструмента.
- inputSchema — ця схема використовуватиметься обробником.
- callback — функція, що викликає інструмент.

Також є `Tool`, який конвертує цей словник у тип, який може приймати обробник mcp сервера, ось як це виглядає:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

І є *schema.ts*, де зберігаються схеми вхідних даних кожного інструмента. Наразі там лише одна схема, але з часом можна додавати більше:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Добре, тепер перейдемо до обробки переліку наших інструментів.

### -3- Обробка переліку інструментів

Для обробки переліку інструментів нам потрібно встановити обробник запиту для цього. Ось що потрібно додати у файл сервера:

**Python**

```python
# код опущено заради стислості
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

Тут ми додаємо декоратор `@server.list_tools` і функцію-обробник `handle_list_tools`. У ній потрібно повернути список інструментів. Зверніть увагу, що кожен інструмент повинен мати ім’я, опис і inputSchema.

**TypeScript**

Щоб встановити обробник запиту для переліку інструментів, треба викликати `setRequestHandler` на сервері зі схемою, що відповідає завданню, у цьому випадку `ListToolsRequestSchema`.

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
// код опущено заради стислості
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Повернути список зареєстрованих інструментів
  return {
    tools: tools
  };
});
```

Гарно, ми опрацювали частину переліку інструментів, давайте подивимось, як можна викликати інструменти.

### -4- Обробка виклику інструмента

Для виклику інструмента потрібно встановити ще один обробник запитів, який опрацьовує запит із вказанням, яку функцію викликати і з якими аргументами.

**Python**

Використаємо декоратор `@server.call_tool` і реалізуємо функцію `handle_call_tool`. У цій функції потрібно розпарсити ім’я інструмента, його аргументи та перевірити, чи є ці аргументи валідними для зазначеного інструмента. Валідацію можна зробити тут або безпосередньо в інструменті.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools є словником із назвами інструментів як ключами
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

- Ім’я інструмента є вхідним параметром `name`, а аргументи — у словнику `arguments`.

- Інструмент викликається за допомогою `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Перевірка аргументів відбувається у властивості `handler`, що посилається на функцію; якщо валідація не проходить, буде викликана помилка.

Отже, ми отримали повне розуміння переліку і виклику інструментів із використанням низькорівневого сервера.

Повний приклад можна знайти [тут](./code/README.md)

## Завдання

Розширте код, який вам дали, додавши низку інструментів, ресурсів і запитів, і зауважте, що потрібно додавати файли лише у папку tools і ніде більше.

*Розв’язок не надається*

## Підсумок

У цьому розділі ми розглянули, як працює підхід з низькорівневим сервером і як він може допомогти створити приємну архітектуру, на якій можна будувати далі. Також ми обговорили валідацію і показали, як працювати з бібліотеками валідації для створення схем перевірки вхідних даних.

## Що далі

- Далі: [Проста автентифікація](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильне тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->