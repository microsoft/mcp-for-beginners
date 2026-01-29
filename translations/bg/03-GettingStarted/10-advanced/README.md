# Разширено използване на сървъра

В MCP SDK има два различни типа сървъри: обикновен сървър и ниско ниво сървър. Обикновено използвате обикновения сървър, за да добавите функции към него. В някои случаи обаче може да искате да разчитате на ниско ниво сървър, например:

- По-добра архитектура. Възможно е да се създаде чиста архитектура както с обикновения сървър, така и с ниско ниво сървър, но може да се твърди, че е малко по-лесно с ниско ниво сървър.
- Наличност на функции. Някои разширени функции могат да се използват само с ниско ниво сървър. Ще видите това в следващите глави, когато добавяме семплиране и събиране на данни.

## Обикновен сървър срещу ниско ниво сървър

Ето как изглежда създаването на MCP сървър с обикновения сървър:

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

Тук ясно добавяте всеки инструмент, ресурс или подканва, които искате сървърът да има. Няма нищо лошо в това.

### Подход с ниско ниво сървър

Когато използвате подхода с ниско ниво сървър, трябва да мислите по различен начин, а именно вместо да регистрирате всеки инструмент, създавате два обработващи функции за всеки тип функция (инструменти, ресурси или подканви). Например за инструментите има само две функции, както следва:

- Списък с всички инструменти. Една функция отговаря за всички опити за изброяване на инструменти.
- Обработка на извиквания към всички инструменти. Тук също има само една функция, която обработва извикванията към инструмент.

Това звучи като потенциално по-малко работа, нали? Вместо да регистрирам инструмент, просто трябва да се уверя, че инструментът е включен в списъка, когато изброявам всички инструменти, и че е извикан, когато има входящо искане за извикване на инструмент.

Нека да видим как изглежда кодът сега:

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

Тук вече имаме функция, която връща списък с функции. Всеки запис в списъка с инструменти има полета като `name`, `description` и `inputSchema`, за да отговаря на типа на връщане. Това ни позволява да поставим дефинициите на инструментите и функциите другаде. Сега можем да създадем всички наши инструменти в папка за инструменти, както и всички функции, така че проектът ни да бъде организиран по следния начин:

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

А какво да кажем за извикването на инструменти? Същата идея ли е, една обработваща функция за извикване на инструмент, който и да е инструмент? Да, точно така, ето кода за това:

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

Както виждате от горния код, трябва да извлечем инструмента, който да бъде извикан, и с какви аргументи, след което да продължим с извикването на инструмента.

## Подобряване на подхода с валидиране

Досега видяхте как всички ваши регистрации за добавяне на инструменти, ресурси и подканви могат да бъдат заменени с тези две обработващи функции за всеки тип функция. Какво друго трябва да направим? Е, трябва да добавим някаква форма на валидиране, за да се уверим, че инструментът се извиква с правилните аргументи. Всеки runtime има свое собствено решение за това, например Python използва Pydantic, а TypeScript използва Zod. Идеята е да направим следното:

- Преместим логиката за създаване на функция (инструмент, ресурс или подканва) в специална папка.
- Добавим начин за валидиране на входящо искане, например за извикване на инструмент.

### Създаване на функция

За да създадем функция, трябва да създадем файл за тази функция и да се уверим, че тя има задължителните полета, изисквани за тази функция. Кои полета се различават малко между инструменти, ресурси и подканви.

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

Тук можете да видите как правим следното:

- Създаваме схема с Pydantic `AddInputModel` с полета `a` и `b` във файл *schema.py*.
- Опитваме се да парсираме входящото искане, за да бъде от тип `AddInputModel`. Ако има несъответствие в параметрите, това ще доведе до грешка:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
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

- В обработващата функция, която се занимава с всички извиквания на инструменти, се опитваме да парсираме входящото искане в дефинираната схема на инструмента:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ако това работи, продължаваме с извикването на самия инструмент:

    ```typescript
    const result = await tool.callback(input);
    ```

Както виждате, този подход създава страхотна архитектура, тъй като всичко си има място, *server.ts* е много малък файл, който само свързва обработващите функции, а всяка функция е в съответната си папка, например tools/, resources/ или prompts/.

Страхотно, нека опитаме да изградим това следващо.

## Упражнение: Създаване на ниско ниво сървър

В това упражнение ще направим следното:

1. Създадем ниско ниво сървър, който обработва списъка с инструменти и извикванията на инструменти.
1. Реализираме архитектура, върху която можем да надграждаме.
1. Добавим валидиране, за да се уверим, че извикванията на инструменти са правилно валидирани.

### -1- Създаване на архитектура

Първото нещо, което трябва да адресираме, е архитектура, която ни помага да мащабираме, докато добавяме повече функции. Ето как изглежда:

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

Сега сме настроили архитектура, която гарантира, че можем лесно да добавяме нови инструменти в папката за инструменти. Чувствайте се свободни да следвате това, за да добавите поддиректории за ресурси и подканви.

### -2- Създаване на инструмент

Нека видим как изглежда създаването на инструмент. Първо, той трябва да бъде създаден в поддиректорията *tool*, както следва:

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

Тук виждаме как дефинираме име, описание, схема за вход с Pydantic и обработваща функция, която ще бъде извикана, когато този инструмент бъде извикан. Накрая излагаме `tool_add`, който е речник, съдържащ всички тези свойства.

Има и *schema.py*, който се използва за дефиниране на схемата за вход, използвана от нашия инструмент:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Трябва също да попълним *__init__.py*, за да гарантираме, че папката за инструменти се третира като модул. Освен това трябва да изложим модулите в нея, както следва:

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

Тук създаваме речник, състоящ се от свойства:

- name, това е името на инструмента.
- rawSchema, това е Zod схемата, която ще се използва за валидиране на входящи искания за извикване на този инструмент.
- inputSchema, тази схема ще се използва от обработващата функция.
- callback, това се използва за извикване на инструмента.

Има и `Tool`, който се използва за преобразуване на този речник в тип, който обработващата функция на MCP сървъра може да приеме, и изглежда така:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Има и *schema.ts*, където съхраняваме схемите за вход за всеки инструмент, който изглежда така с една схема в момента, но докато добавяме инструменти, можем да добавяме повече записи:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Страхотно, нека продължим с обработката на списъка с нашите инструменти.

### -3- Обработка на списъка с инструменти

Следващото, за да обработим списъка с инструменти, трябва да настроим обработваща функция за искания за това. Ето какво трябва да добавим към нашия сървър файл:

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

Тук добавяме декоратора `@server.list_tools` и имплементиращата функция `handle_list_tools`. В последната трябва да произведем списък с инструменти. Обърнете внимание как всеки инструмент трябва да има име, описание и inputSchema.

**TypeScript**

За да настроим обработваща функция за искания за списък с инструменти, трябва да извикаме `setRequestHandler` на сървъра със схема, която съответства на това, което се опитваме да направим, в този случай `ListToolsRequestSchema`.

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

Страхотно, сега сме решили частта за списъка с инструменти, нека разгледаме как можем да извикваме инструменти.

### -4- Обработка на извикване на инструмент

За да извикаме инструмент, трябва да настроим друга обработваща функция, този път фокусирана върху обработката на искане, което уточнява коя функция да бъде извикана и с какви аргументи.

**Python**

Нека използваме декоратора `@server.call_tool` и го имплементираме с функция като `handle_call_tool`. В рамките на тази функция трябва да извлечем името на инструмента, неговите аргументи и да се уверим, че аргументите са валидни за съответния инструмент. Можем да валидираме аргументите в тази функция или по-надолу в самия инструмент.

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

Ето какво се случва:

- Името на нашия инструмент вече е налично като входен параметър `name`, което е вярно и за нашите аргументи под формата на речника `arguments`.

- Инструментът се извиква с `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Валидирането на аргументите се случва в свойството `handler`, което сочи към функция. Ако това се провали, ще бъде хвърлена грешка.

Ето, сега имаме пълно разбиране за списъка и извикването на инструменти с ниско ниво сървър.

Вижте [пълния пример](./code/README.md) тук.

## Задача

Разширете кода, който ви е даден, с няколко инструмента, ресурси и подканви и размишлявайте върху това как забелязвате, че трябва да добавяте файлове само в папката за инструменти и никъде другаде.

*Решение не е предоставено*

## Обобщение

В тази глава разгледахме как работи подходът с ниско ниво сървър и как това може да ни помогне да създадем добра архитектура, върху която можем да надграждаме. Също така обсъдихме валидирането и ви беше показано как да работите с библиотеки за валидиране, за да създавате схеми за входно валидиране.

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.