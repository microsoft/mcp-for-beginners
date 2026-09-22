# Напредна употреба сервера

У MCP SDK изложена су два различита типа сервера: ваш стандардни сервер и ниско-нивo сервер. Обично бисте користили стандардни сервер да бисте му додали функције. Међутим, у неким случајевима желите се ослонити на ниско-нивo сервер као што је: 

- Боља архитектура. Mогуће је направити чисту архитектуру са оба, и стандардним и ниско-нивo сервером, али може се тврдити да је мало лакше са ниско-нивo сервером.
- Доступност функција. Неке напредне функције могу се користити само са
     ниско-нивo сервером. Накнадна поглавља покривају Елицитацију и задремалу Sampling
     функцију, која је застарела у MCP `2026-07-28`.

## Стандардни сервер против ниско-нивo сервера

Ево како изгледа креирање MCP сервера са стандардним сервером

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

// Додајте алатку за сабирање
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

Тачка је да експлицитно додате сваки алат, ресурс или упит који желите да сервер има. У томе нема ништа лоше.  

### Приступ низко-нивo серверу

Међутим, када користите ниско-нивo сервер, морате о томе размишљати другачије. Уместо регистрације сваког алата, креирате по два обрађивача за сваки тип функције (алати, ресурси или упити). На пример, алати онда имају само две функције овако:

- Листање свих алата. Једна функција би била одговорна за све покушаје листања алата.
- руковање позивима свих алата. Овде такође постоји само једна функција која руковође позивима алата.

Звучи као потенцијално мање посла, зар не? Уместо да региструјем алат, само морам да обезбедим да је алат на листи када листам све алате и да се позове кад постоји долазни захтев за позив алата. 

Погледајмо како сада изгледа код:

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

Сада имамо функцију која враћа листу функција. Свака ставка на листи алата сад има поља као што су `name`, `description` и `inputSchema` да би се уклопила у тип повратка. Ово нам омогућава да алате и дефиниције функција сместимо на друго место. Сада можемо све алате креирати у фолдеру tools, и исто тако за све ваше функције па ваш пројекат изненада може бити организован овако:

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

То је сјајно, архитектура нам може изгледати прилично чисто.

А шта је са позивањем алата, да ли је и ту иста идеја, један обрађивач за позив алата, било ког алата? Да, управо тако, ево кода за то:

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
    // TODO позвати алат,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Као што видите из горњег кода, потребно је раздвојити који алат треба позвати и са којим аргументима, а затим наставити са позивом алата.

## Побољшање приступа валидацијом

До сада сте видели како све регистрације за додавање алата, ресурса и упита могу бити замењене овим двојем обрађивача по типу функције. Шта још треба да урадимо? Па, требало би да додамо неки облик валидације да бисмо обезбедили да се алат позива са исправним аргументима. Свако окружење има своје решење за то, на пример Python користи Pydantic а TypeScript користи Zod. Идеја је да урадимо следеће:

- Пренесемо логику креирања функције (алат, ресурс или упит) у посебан фолдер.
- Додамо начин да валидирамо долазни захтев који, рецимо, тражи позив алата.

### Креирање функције

Да бисмо креирали функцију, морамо направити фајл за ту функцију и уверити се да има обавезна поља које та функција захтева. Која поља се разликују у зависности од алата, ресурса и упита.

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
        # Валидација улаза коришћењем Пидантик модела
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # ЗАДАТАК: додај Пидантик, како бисмо могли креирати AddInputModel и валидацију аргумената

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

овде видите како радимо следеће:

- Креирамо шему користећи Pydantic `AddInputModel` са пољима `a` и `b` у фајлу *schema.py*.
- Покушавамо да преведемо долазни захтев у тип `AddInputModel`, ако параметри не одговарају, ово ће изазвати грешку:

   ```python
   # add.py
    try:
        # Валидација уноса коришћењем Пидантиновог модела
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Можете изабрати да ли ћете ову логику превођења ставити у сам позив алата или у функцију обрађивача.

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

// скема.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// додај.ts
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

- У обрађивачу који се бави свим позивима алата сада покушавамо да преведемо долазни захтев у дефинисану шему алата:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ако то успе, онда настављамо са позивом стварног алата:

    ```typescript
    const result = await tool.callback(input);
    ```

Као што видите, овај приступ прави одличну архитектуру јер све има своје место, *server.ts* је веома мали фајл који само повезује обрађиваче захтева, а свака функција је у одговарајућем фолдеру, нпр. tools/, resources/ или /prompts.

Сјајно, хајде да покушамо да ово следеће изградимо. 

## Вежба: Креирање ниско-нивo сервера

У овој вежби урадимо следеће:

1. Креирај ниско-нивo сервер који обрађује листање алата и позив алата.
1. Имплементирај архитектуру коју можеш да проширујеш.
1. Додај валидацију да осигураш да су позиви алата испитивани.

### -1- Креирање архитектуре

Прво што морамо решити је архитектура која нам помаже да се скалирамо како додавамо више функција, ево како то изгледа:

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

Сада смо поставили архитектуру која нам омогућава лако додавање нових алата у фолдер tools. Слободно додате и поддиректоријуме за resources и prompts.

### -2- Креирање алата

Погледајмо како изгледа креирање алата. Прво, потребно га је направити у његовом поддиректоријуму *tool* овако:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Верификуј унос користећи Пидантик модел
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: додај Пидантик, да можемо креирати AddInputModel и верификовати аргументе

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Овде видимо како дефинишемо name, description и input schema користећи Pydantic и обрађивач који ће бити позван када се овај алат позове. На крају излажемо `tool_add` што је речник који држи сва ова својства.

Постоји и *schema.py* који се користи за дефинисање улазне шеме коју наш алат користи:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Такође морамо попунити *__init__.py* да бисмо осигурали да фолдер tools буде третирана као модули. Додатно, морамо изложити модуле унутар њега овако:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Овај фајл можемо наставити да проширујемо како додавамо више алата.

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

Овде правимо речник који се састоји од својстава:

- name, ово је име алата.
- rawSchema, ово је Zod шема која ће се користити за валидацију долазних захтева за позив овог алата.
- inputSchema, ову шему ће користити обрађивач.
- callback, ово се користи за позив алата.

Постоји и `Tool` који се користи да конвертује овај речник у тип који MCP серверски обрађивач може прихватити и изгледа овако:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

И ту је *schema.ts* где чува шеме улазних података за сваки алат, тренутно са само једном шемом али како додајемо алате можемо додати више ставки:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Одлично, сада пређимо на обраду листања наших алата.

### -3- Обрађивач листања алата

Следеће, за обраду листања алата, морамо поставити обрађивач захтева за то. Ево шта треба додати у фајл сервера:

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

Овде додамо декоратор `@server.list_tools` и имплементирајућу функцију `handle_list_tools`. У овој последњој морамо произвести листу алата. Запамтите да сваки алат мора имати name, description и inputSchema.   

**TypeScript**

Да бисмо поставили обрађивач захтева за листање алата, морамо позвати `setRequestHandler` на серверу са шемом која одговара нашем захтеву, у овом случају `ListToolsRequestSchema`. 

```typescript
// индекс.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// сервер.ts
// код изостављен ради краткоће
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Врати листу регистрованих алата
  return {
    tools: tools
  };
});
```

Одлично, сада смо решили део листања алата, погледајмо како да позивамо алате.

### -4- Обрађивач позива алата

Да бисмо позвали алат, треба поставити други обрађивач захтева, овај пут усредсређен на захтев да каже коју функцију да позове и са којим аргументима.

**Python**

Користимо декоратор `@server.call_tool` и имплементирамо га функцијом као што је `handle_call_tool`. Унутар те функције морамо издвојити име алата, његов аргумент и осигурати да су аргументи валидни за тај алат. Можемо или валидирати аргументе овде или касније у самом алату.

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

- Име алата је већ присутно као улазни параметар `name` што важи и за наше аргументе у облику речника `arguments`.

- Алат се позива са `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Валидација аргумената дешава се у својству `handler` које показује на функцију, ако то не успе избациће изузетак. 

Ето, сада имамо потпуно разумевање како листати и позивати алате користећи ниско-нивo сервер.

Погледајте [пуни пример](./code/README.md) овде

## Задатак

Прошири код који си добио са неколико алата, ресурса и упита и размисли како примећујеш да само мораш додавати фајлове у директоријум tools и нигде више.

*Нема понуђеног решења*

## Резиме

У овом поглављу видели смо како ради приступ ниско-нива сервисера и како нам то помаже да направимо лепу архитектуру на којој можемо наставити да градимо. Такође смо разговарали о валидацији и показано вам је како радити са библиотекама за верификацију да бисте направили шеме за проверу улаза.

## Шта следи

- Следеће: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->