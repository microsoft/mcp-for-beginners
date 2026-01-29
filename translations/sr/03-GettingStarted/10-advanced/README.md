# Напредна употреба сервера

Постоје две различите врсте сервера које MCP SDK пружа: ваш уобичајени сервер и сервер на ниском нивоу. Уобичајено је да користите регуларни сервер за додавање функција. Међутим, у неким случајевима, можда ћете желети да се ослоните на сервер на ниском нивоу, као што су:

- Боља архитектура. Могуће је креирати чисту архитектуру и са регуларним сервером и са сервером на ниском нивоу, али се може тврдити да је то мало лакше са сервером на ниском нивоу.
- Доступност функција. Неке напредне функције могу се користити само са сервером на ниском нивоу. Ово ћете видети у каснијим поглављима када додамо узорковање и елицитацију.

## Регуларни сервер vs сервер на ниском нивоу

Ево како изгледа креирање MCP сервера са регуларним сервером:

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

Суштина је у томе да експлицитно додате сваки алат, ресурс или упит који желите да сервер има. Ништа лоше у томе.

### Приступ серверу на ниском нивоу

Међутим, када користите приступ серверу на ниском нивоу, потребно је да размишљате другачије, наиме, уместо да региструјете сваки алат, креирате два хендлера за сваку врсту функције (алати, ресурси или упити). На пример, за алате постоје само две функције, као што је приказано:

- Листање свих алата. Једна функција би била одговорна за све покушаје листања алата.
- Обрада позива свих алата. Овде такође постоји само једна функција која обрађује позиве алата.

Звучи као потенцијално мање посла, зар не? Уместо да региструјем алат, само треба да се уверим да је алат наведен када листам све алате и да се позива када стигне захтев за позив алата.

Хајде да погледамо како сада изгледа код:

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

Овде сада имамо функцију која враћа листу функција. Сваки унос у листи алата сада има поља као што су `name`, `description` и `inputSchema` да би се придржавао типа повратне вредности. Ово нам омогућава да наше алате и дефиниције функција поставимо на друго место. Сада можемо креирати све наше алате у директоријуму за алате, а исто важи и за све ваше функције, тако да ваш пројекат може одједном бити организован овако:

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

Сјајно, наша архитектура може изгледати прилично чисто.

Шта је са позивањем алата, да ли је то онда иста идеја, један хендлер за позив алата, било ког алата? Да, тачно, ево кода за то:

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

Као што можете видети из горњег кода, потребно је да издвојимо алат који треба позвати, са којим аргументима, а затим да наставимо са позивом алата.

## Побољшање приступа са валидацијом

До сада сте видели како се све ваше регистрације за додавање алата, ресурса и упита могу заменити овим двема хендлерима по врсти функције. Шта још треба да урадимо? Па, требало би да додамо неки облик валидације како бисмо осигурали да се алат позива са исправним аргументима. Сваки рунтајм има своје решење за ово, на пример Python користи Pydantic, а TypeScript користи Zod. Идеја је да урадимо следеће:

- Пренесемо логику за креирање функције (алата, ресурса или упита) у њен посвећени директоријум.
- Додамо начин за валидацију долазног захтева који, на пример, тражи позив алата.

### Креирање функције

Да бисмо креирали функцију, потребно је да креирамо датотеку за ту функцију и да се уверимо да има обавезна поља која се захтевају за ту функцију. Која поља се разликују између алата, ресурса и упита.

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

Овде можете видети како радимо следеће:

- Креирамо шему користећи Pydantic `AddInputModel` са пољима `a` и `b` у датотеци *schema.py*.
- Покушавамо да парсирамо долазни захтев да буде типа `AddInputModel`, ако постоји неслагање у параметрима, ово ће се срушити:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Можете изабрати да ли ћете ову логику парсирања ставити у сам позив алата или у функцију хендлера.

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

- У хендлеру који се бави свим позивима алата, сада покушавамо да парсирамо долазни захтев у дефинисану шему алата:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ако то успе, онда настављамо са позивом стварног алата:

    ```typescript
    const result = await tool.callback(input);
    ```

Као што можете видети, овај приступ ствара одличну архитектуру јер све има своје место, *server.ts* је веома мала датотека која само повезује хендлере захтева, а свака функција је у свом директоријуму, тј. tools/, resources/ или /prompts.

Сјајно, хајде да покушамо да изградимо ово следеће.

## Вежба: Креирање сервера на ниском нивоу

У овој вежби, урадићемо следеће:

1. Креирати сервер на ниском нивоу који обрађује листање алата и позивање алата.
1. Имплементирати архитектуру на којој можете градити.
1. Додати валидацију како бисте осигурали да су ваши позиви алата правилно валидирани.

### -1- Креирање архитектуре

Прва ствар коју треба да решимо је архитектура која нам помаже да се скалирамо како додајемо више функција, ево како изгледа:

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

Сада смо поставили архитектуру која осигурава да можемо лако додати нове алате у директоријум за алате. Слободно следите ово да додате поддиректоријуме за ресурсе и упите.

### -2- Креирање алата

Хајде да видимо како изгледа креирање алата. Прво, потребно је да буде креиран у свом поддиректоријуму *tool* овако:

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

Овде видимо како дефинишемо име, опис, шему уноса користећи Pydantic и хендлер који ће бити позван када се овај алат позове. На крају, излажемо `tool_add`, који је речник који садржи сва ова својства.

Постоји и *schema.py* који се користи за дефинисање шеме уноса коју користи наш алат:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Такође треба да попунимо *__init__.py* како бисмо осигурали да се директоријум алата третира као модул. Поред тога, треба да изложимо модуле унутар њега овако:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Можемо наставити да додајемо у ову датотеку како додајемо више алата.

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

Овде креирамо речник који се састоји од својстава:

- name, ово је име алата.
- rawSchema, ово је Zod шема, користиће се за валидацију долазних захтева за позив овог алата.
- inputSchema, ова шема ће се користити од стране хендлера.
- callback, користи се за позивање алата.

Постоји и `Tool` који се користи за конвертовање овог речника у тип који MCP сервер хендлер може прихватити и изгледа овако:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

А ту је и *schema.ts* где чувамо шеме уноса за сваки алат, који изгледа овако са само једном шемом тренутно, али како додајемо алате можемо додати више уноса:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Сјајно, хајде да наставимо са обрадом листања наших алата.

### -3- Обрада листања алата

Да бисмо обрадили листање наших алата, потребно је да поставимо хендлер захтева за то. Ево шта треба да додамо у нашу сервер датотеку:

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

Овде додајемо декоратор `@server.list_tools` и имплементациону функцију `handle_list_tools`. У овој функцији, потребно је да произведемо листу алата. Обратите пажњу на то како сваки алат треба да има име, опис и inputSchema.

**TypeScript**

Да бисмо поставили хендлер захтева за листање алата, потребно је да позовемо `setRequestHandler` на серверу са шемом која одговара ономе што покушавамо да урадимо, у овом случају `ListToolsRequestSchema`.

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

Сјајно, сада смо решили део листања алата, хајде да погледамо како бисмо могли да позивамо алате.

### -4- Обрада позива алата

Да бисмо позвали алат, потребно је да поставимо још један хендлер захтева, овог пута фокусиран на обраду захтева који специфицира коју функцију позвати и са којим аргументима.

**Python**

Хајде да користимо декоратор `@server.call_tool` и имплементирамо га функцијом као што је `handle_call_tool`. Унутар те функције, потребно је да издвојимо име алата, његов аргумент и да осигурамо да су аргументи валидни за дати алат. Можемо валидирати аргументе у овој функцији или ниже у стварном алату.

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

Ево шта се дешава:

- Име нашег алата је већ присутно као улазни параметар `name`, што важи и за наше аргументе у облику речника `arguments`.

- Алат се позива са `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Валидација аргумената се дешава у својству `handler`, које показује на функцију, ако то не успе, подићи ће се изузетак.

Ето, сада имамо потпуно разумевање листања и позивања алата користећи сервер на ниском нивоу.

Погледајте [потпуни пример](./code/README.md) овде.

## Задатак

Проширите код који вам је дат са бројем алата, ресурса и упита и размислите о томе како примећујете да само треба да додате датотеке у директоријум алата и нигде другде.

*Решење није дато*

## Резиме

У овом поглављу, видели смо како функционише приступ серверу на ниском нивоу и како нам то може помоћи да креирамо лепу архитектуру на којој можемо наставити да градимо. Такође смо разговарали о валидацији и показано вам је како да радите са библиотекама за валидацију како бисте креирали шеме за валидацију уноса.

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.