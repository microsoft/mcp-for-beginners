# Напредна употреба сервера

Постоје две различите врсте сервера изложене у MCP SDK-у, ваш нормални сервер и ниско-нивo сервер. Обично бисте користили редовни сервер да додате функционалности. Међутим, за неке случајеве желите да се ослоните на ниско-ниво сервер као што су:

- Боља архитектура. Могуће је креирати чисту архитектуру са и редовним сервером и ниско-нивo сервером, али може се тврдити да је нешто лакше са ниско-нивo сервером.
- Доступност функција. Неке напредне функције могу се користити само са ниско-нивo сервером. Ово ћете видети у каснијим поглављима када додамо узорковање и издвајање.

## Редовни сервер у односу на ниско-ниво сервер

Ево како изгледа креирање MCP сервера са редовним сервером

**Python**

```python
mcp = FastMCP("Demo")

# Додајте алат за сабирање
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

// Додај додатак алат
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

Поента је да експлицитно додате сваки алат, ресурс или упит који желите да сервер има. Нема ништа лоше у томе.

### Приступ ниско-нивo сервера

Међутим, када користите приступ ниско-нивo сервера, морате о томе размишљати другачије. Уместо да региструјете сваки алат, уместо тога креирате два обрађивача по типу функције (алати, ресурси или упити). Тако, на пример, алати имају само две функције овако:

- Листање свих алата. Једна функција би била одговорна за све покушаје да се наброје алати.
- Обрада позивања свих алата. Овде се такође налази само једна функција која обрађује позиве алата.

То звучи као потенцијално мање посла, зар не? Дакле, уместо регистровања алата, само морам да обезбедим да је алат наведен када набрајам све алате и да се позове када дође захтев за позив алата.

Погледајмо како сада код изгледа:

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
  // Врати листу регистрованих алата
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

Овде сада имамо функцију која враћа листу функција. Свако уношење у листу алата сада има поља као `name`, `description` и `inputSchema` која одговарају типу повратка. Ово нам омогућава да алате и дефиницију функције ставимо на друго место. Сада можемо креирати све алате у фасцикли tools и исто важи за све ваше функције тако да ваш пројекат може изненадно бити организован овако:

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

Одлично, наша архитектура може бити прилично чиста.

А шта је са позивом алата, да ли је и даље иста идеја, један обрађивач који позива алат, било који алат? Да, управо тако, ево кода за то:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools је речник са именима алата као кључевима
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
    // TODO позвати алатку,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Као што видите из горњег кода, потребно је издвојити алат који се позива и с којим аргументима, а затим наставити са позивом алата.

## Побољшање приступа са валидацијом

Досад сте видели како сва ваша регистрација за додавање алата, ресурса и упита може бити замењена са ова два обрађивача по типу функције. Шта још треба да урадимо? Па, требало би да додамо неки облик валидације да бисмо осигурали да се алат позива са исправним аргументима. Сваки извршни окружење има своје решење за ово, на пример Python користи Pydantic а TypeScript користи Zod. Идеја је да урадимо следеће:

- Преселимо логику за креирање функције (алат, ресурс или упит) у њен посебан фолдер.
- Додамо начин да се валидира долазни захтев који нпр. тражи да се позове алат.

### Креирање функције

Да бисмо креирали функцију, морамо креирати датотеку за ту функцију и осигурати да има обавезна поља која су потребна тој функцији. Која поља се разликују мало између алата, ресурса и упита.

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
        # Верификуј унос користећи Пидантик модел
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: додај Пидантик, како бисмо могли да креирамо AddInputModel и верификујемо аргументе

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

овде можете видети како радимо следеће:

- Креирамо шему користећи Pydantic `AddInputModel` са пољима `a` и `b` у датотеци *schema.py*.
- Покушавамо да парсирамо долазни захтев да буде типа `AddInputModel`, ако има неслагања у параметрима, ово ће се срушити:

   ```python
   # add.py
    try:
        # Верификовати улаз користећи Пидантик модел
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Можете изабрати да ову логику парсирања ставите у сам позив алата или у функцију обрађивача.

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

- У обрађивачу који рукује свим позивима алата, сада покушавамо да парсирамо добијени захтев у дефинисану шему алата:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ако то успе, онда настављамо са позивом стварног алата:

    ```typescript
    const result = await tool.callback(input);
    ```

Као што видите, овај приступ креира одличну архитектуру јер све има своје место, *server.ts* је врло мала датотека која само повезује обрађиваче захтева, а свака функција је у свом одговарајућем фолдеру нпр. tools/, resources/ или /prompts.

Одлично, покушајмо да следеће направимо ово.

## Вежба: Креирање ниско-нивo сервера

У овој вежби урадићемо следеће:

1. Креирати ниско-ниво сервер који рукује набрајањем алата и позивом алата.
1. Имплементирати архитектуру на којој можете градити.
1. Додати валидацију да бисте осигурали да су ваши позиви алата правилно валидирани.

### -1- Креирај архитектуру

Прва ствар коју морамо решити је архитектура која нам помаже да се скалирамо како додамо више функција, ево како то изгледа:

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

Сада смо успоставили архитектуру која осигурава да лако можемо додати нове алате у папци tools. Слободно пратите ову шему да додате поддиректоријуме за ресурсе и упите.

### -2- Креирање алата

Погледајмо како изгледа креирање алата следеће. Прво, алат треба бити креиран у свом поддиректоријуму *tool* овако:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Валидација уноса коришћењем Пидантик модела
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: додај Пидантик, како бисмо могли направити AddInputModel и валидацију аргумената

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Оно што видимо овде је како дефинишемо име, опис и улазну шему користећи Pydantic и обрађивач који ће се позивати када се овај алат позове. На крају, излажемо `tool_add` који је речник који садржи сва ова својства.

Постоји и *schema.py* која се користи за дефинисање улазне шеме коју наш алат користи:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Такође морамо попунити *__init__.py* да бисмо осигурали да се директоријум алата третира као модул. Поред тога, морамо изложити модуле који се у њему налазе овако:

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
- rawSchema, ово је Zod шема, користиће се за валидацију долазних захтева да се овај алат позове.
- inputSchema, ова шема се користи у обрађивачу.
- callback, ово се користи за позивање алата.

Постоји и `Tool` који се користи да конвертује овај речник у тип који mcp сервер обрађивач може прихватити и изгледа овако:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Постоји и *schema.ts* где чувамо улазне шеме за сваки алат који изледа овако са само једном шемом за сада, али како додајемо алате можемо додати још уноса:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Одлично, наставимо даље да руковањемо набрајањем наших алата.

### -3- Руковање набрајањем алата

Да бисмо руковали набрајањем наших алата, потребно је да подесимо обрађивач захтева за то. Ево шта треба да додамо у нашу серверску датотеку:

**Python**

```python
# код изостављен ради краткоће
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

Овде додајемо декоратор `@server.list_tools` и имплементирајућу функцију `handle_list_tools`. У последњем, треба да направимо листу алата. Обратите пажњу да сваки алат мора имати име, опис и inputSchema.

**TypeScript**

Да бисмо подесили обрађивач захтева за набрајање алата, потребно је позвати `setRequestHandler` на серверу са шемом која одговара томе што покушавамо да урадимо, у овом случају `ListToolsRequestSchema`.

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
// код изостављен ради краткоће
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Вратите листу регистрованих алата
  return {
    tools: tools
  };
});
```

Одлично, сада смо решили део са набрајањем алата, погледајмо како можемо позивати алате.

### -4- Руковање позивом алата

Да бисмо позвали алат, морамо подесити још један обрађивач захтева, овог пута фокусиран на обраду захтева који наводи коју функцију позвати и са којим аргументима.

**Python**

Хајде да користимо декоратор `@server.call_tool` и имплементирамо га функцијом као `handle_call_tool`. Унутар те функције, потребно је издвојити име алата, његове аргументе и осигурати да су аргументи важећи за тај алат. Можемо валидирати аргументе или овде у овој функцији или касније у самом алату.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools је речник са именима алата као кључевима
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # позови алат
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Ево шта се дешава:

- Име нашег алата је већ присутно као улазни параметар `name`, што је истина и за наше аргументе у облику речника `arguments`.

- Алат се позива са `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Валидација аргумената се дешава у својству `handler` које указује на функцију, ако то не успе избациће изузетак.

Ето, сада имамо потпуно разумевање набрајања и позива алата коришћењем ниско-ниво сервера.

Погледајте [пуни пример](./code/README.md) овде

## Задатак

Проширите датујћи код са бројем алата, ресурса и упита и размислите како примећујете да треба да додате само датотеке у директоријум tools и нигде више.

*Решење није дато*

## Резиме

У овом поглављу смо видели како приступ ниско-нивo сервера функционише и како нам може помоћи да направимо лепу архитектуру на коју можемо наставити да градимо. Такође смо говорили о валидацији и показано вам је како радити са библиотекама за валидацију да бисте креирали шеме за проверу улаза.

## Шта следи

- Следеће: [Једноставна аутентикација](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да будемо прецизни, имајте на уму да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетом. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразуме или погрешна тумачења која произилазе из употребе овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->