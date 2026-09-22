# Разширено използване на сървъри

В MCP SDK са изложени два различни типа сървъри: нормален сървър и нискониво сървър. Обикновено използвате обикновения сървър, за да добавите функции към него. В някои случаи обаче искате да разчитате на нискониво сървър, например:

- По-добра архитектура. Възможно е да се създаде чиста архитектура с обикновения сървър и нисконивo сървър, но може да се каже, че е малко по-лесно с нискониво сървър.
- Наличност на функции. Някои разширени функции могат да се използват само с
    нискониво сървър. По-късните глави разглеждат Elicitation и остарялата Sampling
    функция, която е остаряла в MCP `2026-07-28`.

## Обикновен сървър срещу нискониво сървър

Ето как изглежда създаването на MCP Сървър с обикновения сървър

**Python**

```python
mcp = FastMCP("Demo")

# Добавете инструмент за добавяне
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

// Добавете инструмент за добавяне
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

Идеята е, че явно добавяте всеки инструмент, ресурс или подканващ елемент, който искате да има сървърът. Няма нищо лошо в това.  

### Подход с нискониво сървър

Обаче, когато използвате подхода с нискониво сървър, трябва да мислите по различен начин. Вместо да регистрирате всеки инструмент, вие вместо това създавате два обработващи метода за всеки тип функция (инструменти, ресурси или подканващи елементи). Например инструментите имат само две функции, както следва:

- Изброяване на всички инструменти. Една функция е отговорна за всички опити за изброяване на инструменти.
- обработване на повикванията към инструментите. Тук също има само една функция, която обработва повиквания към инструмент.

Това звучи като потенциално по-малко работа, нали? Вместо да регистрирам инструмент, трябва само да се уверя, че инструментът е включен, когато изброявам всички инструменти и че се извиква, когато има входяща заявка за извикване на инструмент. 

Нека да видим как сега изглежда кодът:

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
  // Върнете списъка на регистрираните инструменти
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

Тук вече имаме функция, която връща списък с функции. Всеки запис в списъка с инструменти има полета като `name`, `description` и `inputSchema`, за да отговаря на типа на връщане. Това ни позволява да поставяме нашите инструменти и дефиниции на функции другаде. Сега можем да създаваме всички наши инструменти в папка tools и същото важи за всички ваши функции, така вашият проект може внезапно да бъде организиран по следния начин:

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

Това е страхотно, нашата архитектура може да изглежда много чиста.

А какво ще кажем за извикването на инструменти, същата ли е идеята, един обработващ метод за извикване на инструмент, който и да е инструмент? Да, точно така, ето кода за това:

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
    
    // args: request.params.arguments
    // TODO извикайте инструмента,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Както виждате от горния код, трябва да разпарсим инструмента, който да извикаме, и с какви аргументи, след което трябва да продължим с извикването на инструмента.

## Подобряване на подхода с валидация

Досега видяхте как всички ваши регистрации за добавяне на инструменти, ресурси и подканващи могат да бъдат заменени с тези два обработващи метода за всеки тип функция. Какво още трябва да направим? Трябва да добавим някаква форма на валидация, за да се уверим, че инструментът се извиква с правилните аргументи. Всеки runtime има своето решение за това, например Python използва Pydantic, а TypeScript използва Zod. Идеята е да направим следното:

- Преместим логиката за създаване на функция (инструмент, ресурс или подканващ елемент) в специална папка.
- Добавим начин за валидиране на входяща заявка, която например иска да извика инструмент.

### Създаване на функция

За да създадем функция, ще трябва да създадем файл за тази функция и да се уверим, че има задължителните полета, изисквани за тази функция. Които полета се различават леко между инструменти, ресурси и подканващи.

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
        # Валидирайте входа, като използвате Pydantic модел
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

- Създаваме схема с помощта на Pydantic `AddInputModel` с полета `a` и `b` във файл *schema.py*.
- Опитваме се да разпарсим входящата заявка като тип `AddInputModel`, ако има несъответствие на параметрите, това ще доведе до срив:

   ```python
   # add.py
    try:
        # Валидирайте входните данни с помощта на Pydantic модел
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Можете да изберете дали да поставите тази логика за парсване в самото извикване на инструмента или във функцията обработчик.

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

- В обработващата функция, която обработва всички повиквания на инструменти, сега се опитваме да разпарсим входящата заявка според дефинираната от инструмента схема:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ако това работи, продължаваме към извикването на самия инструмент:

    ```typescript
    const result = await tool.callback(input);
    ```

Както виждате, този подход създава отлична архитектура, тъй като всичко има своето място, *server.ts* е много малък файл, който само свързва обработващите заявки, а всяка функция е в съответната си папка, т.е. tools/, resources/ или /prompts.

Страхотно, нека опитаме да изградим това сега. 

## Упражнение: Създаване на нискониво сървър

В това упражнение ще направим следното:

1. Създаване на нискониво сървър, който обработва изброяването на инструменти и извикването на инструменти.
1. Реализиране на архитектура, върху която можете да градите.
1. Добавяне на валидация, за да се гарантира, че извикванията на вашите инструменти са правилно валидирани.

### -1- Създаване на архитектура

Първото нещо, което трябва да решим, е архитектура, която ни помага да мащабираме, когато добавяме повече функции, ето как изглежда тя:

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

Сега имаме настроена архитектура, която гарантира, че лесно можем да добавяме нови инструменти в папката tools. Можете да последвате това и да добавите поддиректории за ресурси и подканващи.

### -2- Създаване на инструмент

Нека видим как изглежда създаването на инструмент след това. Първо, той трябва да бъде създаден в своята поддиректория *tool* по следния начин:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Валидация на входните данни с помощта на Pydantic модел
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

Това, което виждаме тук, е как дефинираме име, описание и входна схема с помощта на Pydantic и обработчик, който ще бъде извикан, когато този инструмент бъде извикан. Накрая излагаме `tool_add`, който е речник, съдържащ всички тези свойства.

Има и *schema.py*, който се използва за дефиниране на входната схема, използвана от нашия инструмент:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Също така трябва да попълним *__init__.py*, за да гарантираме, че директорията tools се третира като модул. Освен това трябва да излагаме модулите в нея по този начин:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Можем да продължим да добавяме в този файл, докато добавяме повече инструменти.

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

- name, това е името на инструмента.
- rawSchema, това е Zod схемата, ще се използва за валидиране на входящи заявки за извикване на този инструмент.
- inputSchema, тази схема се използва от обработчика.
- callback, това се използва за извикване на инструмента.

Има и `Tool`, който се използва за превръщане на този речник в тип, който обработчикът на mcp сървъра може да приеме, и изглежда така:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Има и *schema.ts*, където съхраняваме входните схеми за всеки инструмент, която изглежда така с единствена схема в момента, но с добавяне на инструменти можем да добавим още записи:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Страхотно, нека продължим с обработката на изброяването на нашите инструменти след това.

### -3- Обработване на изброяване на инструменти

Следващото, за да обработваме изброяването на нашите инструменти, трябва да настроим обработваща заявка за това. Ето какво трябва да добавим към нашия сървър файл:

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

Тук добавяме декоратор `@server.list_tools` и реализираща функция `handle_list_tools`. В последната трябва да произведем списък с инструменти. Обърнете внимание, че всеки инструмент трябва да има име, описание и inputSchema.   

**TypeScript**

За да настроим обработващата заявка за изброяване на инструменти, трябва да извикаме `setRequestHandler` на сървъра със схема, която отговаря на това, което искаме да правим, в този случай `ListToolsRequestSchema`. 

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

Страхотно, сега сме решили частта с изброяването на инструменти, нека видим как бихме могли да извикваме инструменти след това.

### -4- Обработване на извикване на инструмент

За извикване на инструмент трябва да настроим още един обработващ заявка, този път фокусиран върху обработка на заявка, указваща кой функция да се извика и с какви аргументи.

**Python**

Нека използваме декоратора `@server.call_tool` и го реализираме с функция като `handle_call_tool`. В тази функция трябва да разпарсим името на инструмента, неговите аргументи и да гарантираме, че аргументите са валидни за конкретния инструмент. Можем да валидираме аргументите или във функцията, или по-надолу в самия инструмент.

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

- Името на нашия инструмент вече присъства като входен параметър `name`, което е вярно за нашите аргументи във вид на речника `arguments`.

- Инструментът се извиква с `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Валидирането на аргументите се извършва в `handler` свойството, което сочи към функция, ако това се провали, ще се вдигне изключение. 

Ето, сега имаме пълно разбиране за изброяване и извикване на инструменти с помощта на нискониво сървър.

Вижте [пълния пример](./code/README.md) тук

## Задача

Разширете кода, който сте получили, с няколко инструмента, ресурси и подканващи и размислете как забелязвате, че трябва да добавяте файлове само в директория tools и никъде другаде. 

*Няма предоставено решение*

## Обобщение

В тази глава видяхме как работи подходът с нискониво сървър и как това може да ни помогне да създадем добра архитектура, върху която да продължаваме да градим. Обсъдихме и валидацията и ви показахме как да работите с библиотеки за валидация, за да създавате схеми за входна валидация.

## Какво следва

- Следва: [Проста автентикация](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->