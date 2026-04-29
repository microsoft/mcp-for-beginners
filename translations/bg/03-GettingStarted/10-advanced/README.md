# Разширено използване на сървър

В MCP SDK са изложени два различни типа сървъри – обикновен сървър и ниско ниво сървър. Обикновено използвате редовния сървър, за да добавяте функции към него. В някои случаи обаче искате да разчитате на ниско ниво сървър, например:

- По-добра архитектура. Възможно е да се създаде чиста архитектура както с обикновения сървър, така и с ниско ниво сървър, но може да се заяви, че с ниско ниво сървър е малко по-лесно.
- Наличност на функции. Някои напреднали функции могат да се използват само с ниско ниво сървър. Това ще видите в следващите глави, когато добавяме семплиране и елцитация.

## Обикновен сървър срещу ниско ниво сървър

Ето как изглежда създаването на MCP сървър с обикновения сървър

**Python**

```python
mcp = FastMCP("Demo")

# Добавете инструмент за събиране
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

// Добавете инструмент за събиране
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

Идеята е, че изрично добавяте всеки инструмент, ресурс или подканата, която искате сървърът да притежава. Няма нищо лошо в това.

### Подход с ниско ниво сървър

Обаче, когато използвате подхода с ниско ниво сървър, трябва да мислите различно. Вместо да регистрирате всеки инструмент, вие създавате по два обработващи функции за всеки тип функция (инструменти, ресурси или подканвания). Например, инструментите имат само две функции така:

- Изброяване на всички инструменти. Една функция отговаря за всички опити за изброяване на инструменти.
- Обработка на повикване на всички инструменти. Отново, има само една функция, която обработва повиквания към инструмент.

Звучи като потенциално по-малко работа, нали? Така вместо да регистрирам инструмент, просто трябва да се уверя, че инструментът е включен при изброяване на всички инструменти и че се извиква при входяща заявка за повикване на инструмент.

Нека да видим как изглежда кода сега:

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
  // Върнете списъка с регистрирани инструменти
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

Тук имаме функция, която връща списък с функции. Всеки запис в списъка с инструменти вече има полета като `name`, `description` и `inputSchema`, за да съвпада с очаквания тип за връщане. Това ни позволява да поставим нашите инструменти и дефиниции на функции на друго място. Сега можем да създадем всичките си инструменти в папка tools и същото важи и за всички ваши функции, така че проектът ви може изведнъж да бъде организиран по следния начин:

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

Това е страхотно, архитектурата ни може да бъде доста чиста.

А какво за повикване на инструменти, същата ли е идеята – един обработващ, който да повиква инструмент, без значение кой инструмент? Да, точно така, ето кода за това:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools е речник с имена на инструменти като ключове
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
    
    // аргументи: request.params.arguments
    // TODO извикайте инструмента,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Както виждате от горния код, трябва да извадим инструмента, който ще се повиква, и с какви аргументи, след което трябва да продължим с повикването на инструмента.

## Подобряване на подхода чрез валидация

До тук видяхте как всички ваши регистрации за добавяне на инструменти, ресурси и подканвания могат да бъдат заменени с тези два обработващи функции на тип функция. Какво още трябва да направим? Трябва да добавим някаква форма на валидация, за да сме сигурни, че инструментът се извиква с правилните аргументи. Всяка runtime среда има свое собствено решение за това, например Python използва Pydantic, а TypeScript използва Zod. Идеята е да направим следното:

- Да преместим логиката за създаване на функция (инструмент, ресурс или подкан) в посветена папка.
- Да добавим начин за валидация на входяща заявка, която например иска да извика инструмент.

### Създаване на функция

За да създадем функция, ще ни трябва да създадем файл за тази функция и да се уверим, че притежава задължителните полета, които се изискват за тази функция. Които полета са различни за инструменти, ресурси и подканвания.

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
        # Проверете входните данни с помощта на модел Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: добавете Pydantic, за да можем да създадем AddInputModel и да валидираме аргументите

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Тук можете да видите как правим следното:

- Създаваме схема с помощта на Pydantic `AddInputModel` с полета `a` и `b` във файла *schema.py*.
- Опитваме се да парснем входящата заявка като тип `AddInputModel`, ако има несъответствие в параметрите, това ще доведе до грешка:

   ```python
   # add.py
    try:
        # Проверка на входните данни с помощта на Pydantic модел
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Можете да изберете дали да поставите тази логика за парсване вътре в самото повикване на инструмента или във функцията обработвач.

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

- В обработващата функция, която се занимава с всички повиквания на инструменти, сега се опитваме да парснем входящата заявка според дефинираната от инструмента схема:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ако това стане успешно, продължаваме с повикването на реалния инструмент:

    ```typescript
    const result = await tool.callback(input);
    ```

Както виждате, този подход създава страхотна архитектура, тъй като всичко е на място, *server.ts* е много малък файл, който просто свързва обработващите функции, а всяка функция е в съответната си папка – tools/, resources/ или prompts/.

Страхотно, нека опитаме да го построим по-нататък.

## Упражнение: Създаване на ниско ниво сървър

В това упражнение ще направим следното:

1. Създадем ниско ниво сървър, който обработва изброяване на инструменти и повикване на инструменти.
1. Реализираме архитектура, върху която можете да изграждате.
1. Добавим валидация, за да сме сигурни, че повикванията на вашите инструменти са валидирани правилно.

### -1- Създаване на архитектура

Първото нещо, което трябва да адресираме, е архитектура, която да ни помогне да мащабираме с добавянето на повече функции, ето как изглежда тя:

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

Сега сме настроили архитектура, която гарантира, че можем лесно да добавяме нови инструменти в папката tools. Чувствайте се свободни да следвате това, за да добавите подпапки за ресурси и подканвания.

### -2- Създаване на инструмент

Нека разгледаме как изглежда създаването на инструмент. Първо, той трябва да бъде създаден в своята поддиректория *tool* така:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Валутирайте въвеждането с помощта на Pydantic модел
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: добавете Pydantic, за да можем да създадем AddInputModel и да валидираме аргументите

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Тук виждаме как дефинираме име, описание и схема на входа с помощта на Pydantic, както и обработващ, който ще бъде извикан, когато този инструмент бъде повикан. Накрая експонираме `tool_add`, който е речник, съдържащ всички тези свойства.

Има и *schema.py*, който се използва за дефиниране на схемата за вход на нашия инструмент:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Също така трябва да попълним *__init__.py*, за да се уверим, че директорията tools се третира като модул. Освен това трябва да експонираме модулите вътре в нея по следния начин:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Можем да продължим да добавяме към този файл, докато добавяме повече инструменти.

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

Тук създаваме речник, съдържащ свойства:

- name – това е името на инструмента.
- rawSchema – това е Zod схемата, която ще се използва за валидиране на входящите заявки за повикване на този инструмент.
- inputSchema – тази схема ще се използва от обработващата функция.
- callback – това се използва за извикване на инструмента.

Има и `Tool`, който се използва за конвертиране на този речник в тип, който обработващата функция на mcp сървъра може да приеме и изглежда така:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Има и *schema.ts*, където съхраняваме схемите за вход за всеки инструмент, която изглежда така, към момента с една схема, но докато добавяме инструменти, можем да добавим повече записи:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Страхотно, нека преминем към обработката на изброяване на нашите инструменти.

### -3- Обработка на изброяване на инструменти

Следващото, за да обработим изброяването на инструментите, трябва да настроим обработващ функция за заявката. Ето какво трябва да добавим във файла на сървъра:

**Python**

```python
# кодът е съкратен за краткост
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

Тук добавяме декоратора `@server.list_tools` и реализиращата функция `handle_list_tools`. В последната трябва да произведем списък с инструменти. Забележете как всеки инструмент трябва да има име, описание и inputSchema.

**TypeScript**

За да настроим обработващата функция за изброяване на инструменти, трябва да извикаме `setRequestHandler` на сървъра с подходяща схема според това, което се опитваме да направим, в този случай `ListToolsRequestSchema`.

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
// кодът е пропуснат за краткост
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Върнете списъка с регистрирани инструменти
  return {
    tools: tools
  };
});
```

Страхотно, вече решихме частта за изброяване на инструменти, нека видим как бихме могли да ги извикваме след това.

### -4- Обработка на повикване на инструмент

За да извикаме инструмент, трябва да настроим още една обработваща функция за заявка, този път фокусирана върху заявка, която посочва коя функция да се извика и с какви аргументи.

**Python**

Нека използваме декоратора `@server.call_tool` и го реализираме с функция като `handle_call_tool`. В тази функция трябва да извлечем името на инструмента, неговите аргументи и да се уверим, че аргументите са валидни за конкретния инструмент. Можем да валидираме аргументите тук или по-нататък в самия инструмент.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools е речник с имена на инструменти като ключове
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # извикайте инструмента
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Ето какво се случва:

- Нашето име на инструмент вече е налично като входен параметър `name`, същото важи и за нашите аргументи под формата на речника `arguments`.

- Инструментът се извиква с `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Валидацията на аргументите се случва в свойството `handler`, което сочи към функция; ако тя се провали, ще бъде хвърлено изключение.

Ето, вече имаме пълно разбиране за изброяване и повикване на инструменти с помощта на ниско ниво сървър.

Вижте [пълния пример](./code/README.md) тук

## Задача

Разширете кода, който сте получили, с няколко инструмента, ресурси и подканвания и наблюдавайте как забелязвате, че трябва да добавяте файлове само в директорията tools и никъде другаде.

*Няма дадено решение*

## Обобщение

В тази глава разгледахме как работи подходът с ниско ниво сървър и как това може да ни помогне да създадем хубава архитектура, върху която можем да продължим да строим. Обсъдихме и валидацията и ви беше показано как да работите с библиотеки за валидация, за да създавате схеми за проверка на входните данни.

## Какво следва

- Следва: [Проста автентикация](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->