# Разширено използване на сървъра

В MCP SDK има два различни типа сървъри, вашият обикновен сървър и ниско ниво сървър. Обикновено бихте използвали обикновения сървър, за да добавяте функции към него. В някои случаи обаче искате да разчитате на ниско ниво сървър, например:

- По-добра архитектура. Възможно е да се създаде чиста архитектура както с обикновен сървър, така и с ниско ниво сървър, но може да се спори, че е малко по-лесно с ниско ниво сървър.
- Наличност на функции. Някои разширени функции могат да се използват само с ниско ниво сървър. Това ще видите в по-късните глави, когато добавяме семплиране и извличане.

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

Идеята е, че изрично добавяте всеки инструмент, ресурс или подканващ елемент, който искате да има сървърът. Няма нищо лошо в това.

### Подход с ниско ниво сървър

Въпреки това, когато използвате подход с ниско ниво сървър, трябва да мислите по различен начин. Вместо да регистрирате всеки инструмент, вие създавате два обработващи функции за всеки тип функция (инструменти, ресурси или подканващи елементи). Например инструментите имат само две функции, като например:

- Изброяване на всички инструменти. Една функция би била отговорна за всички опити да се изброят инструментите.
- Обработване на повиквания към всички инструменти. Също така има само една функция, която обработва повиквания към даден инструмент.

Звучи като потенциално по-малко работа, нали? Вместо да регистрирам инструмент, просто трябва да гарантирам, че инструментът е в списъка при изброяване на всички инструменти и че се извиква, когато има входяща заявка за извикване на инструмент.

Нека видим как сега изглежда кодът:

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

Тук вече имаме функция, която връща списък с функции. Всеки запис в списъка с инструменти вече има полета като `name`, `description` и `inputSchema`, за да отговаря на типа на връщаната стойност. Това ни позволява да поставим нашите инструменти и дефиниция на функция на друго място. Сега можем да създадем всички наши инструменти в папка tools и същото важи за всички ваши функции, така че вашият проект може внезапно да бъде организиран по следния начин:

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

Това е страхотно, архитектурата ни може да изглежда доста чиста.

Какво да кажем за извикването на инструменти, същата ли е идеята, един обработващ за извикване на инструмент, без значение кой? Да, точно така, ето кода за това:

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

Както виждате от горния код, трябва да извадим инструмента, който ще се извика, и с какви аргументи, след което трябва да продължим с извикването на инструмента.

## Подобряване на подхода с валидиране

Досега видяхте как всички ваши регистрации за добавяне на инструменти, ресурси и подканващи елементи могат да бъдат заменени с тези две обработващи функции за всеки тип функция. Какво още трябва да направим? Трябва да добавим някаква форма на валидиране, за да гарантираме, че инструментът се извиква с правилните аргументи. Всеки runtime има свое собствено решение за това, например Python използва Pydantic, а TypeScript използва Zod. Идеята е, че правим следното:

- Преместваме логиката за създаване на функция (инструмент, ресурс или подканващ елемент) в неговата специализирана папка.
- Добавяме начин да валидираме входяща заявка, например за извикване на инструмент.

### Създаване на функция

За да създадем функция, ще трябва да създадем файл за тази функция и да се уверим, че има задължителните полета, изисквани за тази функция. Които полета се различават малко между инструменти, ресурси и подканващи елементи.

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
        # Валидирайте входните данни с помощта на Pydantic модел
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

тук можете да видите как правим следното:

- Създаваме схема чрез Pydantic `AddInputModel` с полета `a` и `b` във файл *schema.py*.
- Опитваме се да парсираме входящата заявка да е от тип `AddInputModel`, ако има несъответствие в параметрите това ще доведе до грешка:

   ```python
   # add.py
    try:
        # Валидирайте входа, използвайки Pydantic модел
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Можете да изберете дали да поставите тази логика за парсиране в самото извикване на инструмента или в обработващата функция.

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

- В обработващата функция, която се занимава с всички повиквания на инструменти, сега се опитваме да парсираме входящата заявка в дефинираната от инструмента схема:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ако това сработи, тогава продължаваме с извикването на действителния инструмент:

    ```typescript
    const result = await tool.callback(input);
    ```

Както виждате, този подход създава отлична архитектура, тъй като всичко има своето място, *server.ts* е много малък файл, който само свързва обработващите заявки, а всяка функция е в съответната си папка, т.е. tools/, resources/ или /prompts.

Страхотно, нека опитаме да изградим това по-нататък.

## Упражнение: Създаване на ниско ниво сървър

В това упражнение ще направим следното:

1. Създаване на ниско ниво сървър, който обработва извеждането на инструменти и извикването на инструменти.
1. Имплементиране на архитектура, върху която можете да изграждате.
1. Добавяне на валидиране, за да осигурите правилната валидация на извикванията на вашите инструменти.

### -1- Създаване на архитектура

Първото, което трябва да адресираме, е архитектура, която да ни помогне да скалираме с добавянето на повече функции, ето как изглежда:

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

Сега сме настроили архитектура, която гарантира, че можем лесно да добавяме нови инструменти в папка tools. Чувствайте се свободни да направите същото за ресурси и подканващи елементи.

### -2- Създаване на инструмент

Нека видим как изглежда създаването на инструмент. Първо, той трябва да се създаде в своята подпапка *tool*, например така:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Валидирайте входа с помощта на Pydantic модел
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

Виждате тук как дефинираме име, описание и входна схема с Pydantic и обработваща функция, която ще се извика, когато този инструмент бъде повикан. Накрая експонираме `tool_add`, който е речник, съдържащ всички тези свойства.

Също така има *schema.py*, който се използва за дефиниране на входната схема за нашия инструмент:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Нужно е също да попълним *__init__.py*, за да се гарантира, че директорията с инструментите се третира като модул. Освен това трябва да експонираме модулите в нея по следния начин:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Можем да продължим да добавяме към този файл, докато добавяме нови инструменти.

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

Тук създаваме речник, състоящ се от свойства:

- name, това е името на инструмента.
- rawSchema, това е схемата Zod, която ще се използва за валидиране на входящите заявки към този инструмент.
- inputSchema, тази схема ще се използва от обработващата функция.
- callback, това се използва за извикване на инструмента.

Има и `Tool`, който се използва за конвертиране на този речник в тип, който mcp сървър обработващ приема, и изглежда така:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Има и *schema.ts*, където съхраняваме входните схеми за всеки инструмент, която изглежда така с единствена схема в момента, но когато добавяме инструменти, можем да добавим повече записи:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Страхотно, нека пристъпим към обработката на изброяването на инструментите след това.

### -3- Обработване на изброяване на инструменти

Следващото, за да обработим изброяването на инструментите, трябва да настроим обработваща заявка за това. Ето какво трябва да добавим във файла на сървъра:

**Python**

```python
# кодът е пропуснат за краткост
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

Тук добавяме декоратора `@server.list_tools` и реализиращата функция `handle_list_tools`. В последната трябва да произведем списък с инструменти. Обърнете внимание, че всеки инструмент трябва да има име, описание и inputSchema.

**TypeScript**

За да настроим обработващата заявка за изброяване на инструменти, трябва да извикаме `setRequestHandler` на сървъра със схема, която отговаря на това, което искаме да направим - в този случай `ListToolsRequestSchema`.

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
// кодът е съкратен за краткост
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Върни списъка с регистрирани инструменти
  return {
    tools: tools
  };
});
```

Страхотно, вече сме решили частта за изброяване на инструменти, нека видим как можем да извикваме инструменти след това.

### -4- Обработване на извикване на инструмент

За да извикаме инструмент, трябва да настроим още една обработваща заявка, този път съсредоточена върху заявка, която уточнява кой функция да бъде извикана и с какви аргументи.

**Python**

Нека използваме декоратора `@server.call_tool` и го имплементираме с функция като `handle_call_tool`. В тази функция трябва да извадим името на инструмента, аргументите му и да гарантираме, че аргументите са валидни за посочения инструмент. Можем да валидираме аргументите тук или по-надолу в самия инструмент.

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

- Името на инструмента вече е налично като входен параметър `name`, което е вярно и за нашите аргументи под формата на речника `arguments`.

- Инструментът се извиква с `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Валидирането на аргументите се прави в собствеността `handler`, която сочи към функция; ако това не сработи, ще бъде вдигнато изключение.

Ето, вече имаме пълно разбиране за изброяване и извикване на инструменти с помощта на ниско ниво сървър.

Вижте [пълния пример](./code/README.md) тук

## Задача

Разширете предоставения ви код с няколко инструмента, ресурси и подканващи елементи и помислете колко забелязвате, че трябва да добавяте само файлове в директорията tools и никъде другаде.

*Не е дадено решение*

## Обобщение

В тази глава видяхме как работи подходът с ниско ниво сървър и как това може да ни помогне да създадем хубава архитектура, върху която да продължим да изграждаме. Обсъдихме и валидиране и ви беше показано как да работите с библиотеки за валидиране, за да създавате схеми за валидиране на входните данни.

## Какво следва

- Следващо: [Прост автентикация](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия оригинален език трябва да се счита за официален източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, възникнали от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->