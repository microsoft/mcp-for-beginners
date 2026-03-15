# Напредна употреба сервера

Постоје две различите врсте сервера изложене у MCP SDK, ваш нормални сервер и ниско-ниво сервер. Обично бисте користили регуларни сервер да бисте додали функције. Међутим, у неким случајевима желите да се ослоните на ниско-ниво сервер као што су:

- Боља архитектура. Могуће је створити чисту архитектуру са обема, и регуларним сервером и ниско-ниво сервером, али може се тврдити да је мало лакше са ниско-ниво сервером.
- Доступност функција. Неке напредне функције могу се користити само са ниско-ниво сервером. Видете то у каснијим поглављима док додајемо узорковање и изазивање.

## Регуларни сервер у односу на ниско-ниво сервер

Ево како изгледа креирање MCP сервера са регуларним сервером

**Python**

```python
mcp = FastMCP("Demo")

# Додај алат за сабирање
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

// Додај алат за сабирање
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

Поента је да јасно додате сваки алат, ресурс или упит који желите да сервер има. Нема ништа лоше у томе.

### Приступ ниско-ниво сервера

Међутим, када користите приступ ниско-ниво сервера, морате размишљати другачије. Уместо регистрације сваког алата, умјесто тога креирате два обработача по типу функције (алати, ресурси или упити). На пример, алати имају само две функције овако:

- Листање свих алата. Једна функција ће бити одговорна за све покушаје листања алата.
- Обрада позива свих алата. Ту такође постоји само једна функција која обрађује позиве алата.

То звучи као потенцијално мање посла, зар не? Дакле, уместо регистрације алата, само морам да се уверим да је алат на листи када листам све алате и да се позива када стигне захтев за позив алата.

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

Овде сада имамо функцију која враћа списак функција. Сваки унос у листи алата сада има поља као што су `name`, `description` и `inputSchema` да задовољи тип повратне вредности. Ово нам омогућава да наше алате и дефиницију функција ставимо негде друго. Сада можемо креирати све наше алате у фасцикли tools и једнако важи за све ваше функције тако да ваш пројекат изненада може бити организацки овако:

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

То је сјајно, наша архитектура може бити прилично чиста.

Шта је са позивом алата, је ли и даље иста идеја, један обработач за позив алата, било ког алата? Да, тачно, ево кода за то:

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

Као што видите из горњег кода, треба да издвојимо који алат позвати и са којим аргументима, а затим наставити са позивањем алата.

## Побољшање приступа са валидацијом

Досад сте видели како све ваше регистрације за додавање алата, ресурса и упита могу бити замењене са овим двема обрадјивачима по типу функције. Шта још треба да урадимо? Па, требало би да додамо неку врсту валидације како бисмо осигурали да се алат позива са исправним аргументима. Сваки runtime има своје решење за ово, на пример Python користи Pydantic а TypeScript користи Zod. Идеја је да урадимо следеће:

- Померимо логику за креирање функције (алат, ресурс или упит) у њен посебни фолдер.
- Додамо начин да валидирамо долазни захтев који тражи, на пример, позив алата.

### Креирање функције

Да бисмо креирали функцију, мораћемо да креирамо фајл за ту функцију и уверимо се да има обавезна поља која функција захтева. Која поља се разликују између алата, ресурса и упита.

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
        # Валидација уноса користећи Пидантик модел
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # ЗАДАТАК: додај Пидантик, тако да можемо направити AddInputModel и валидирати аргументе

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Овде можете видети како урадимо следеће:

- Креирамо шему коришћењем Pydantic `AddInputModel` са пољима `a` и `b` у фајлу *schema.py*.
- Пokušавамо да парсирамо долазни захтев као тип `AddInputModel`, ако постоји неслагање у параметрима, то ће изазвати сртав:

   ```python
   # add.py
    try:
        # Валидација уноса коришћењем Пидантик модела
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Можете изабрати да ли ћете ставити ову логику парсирања у сам позив алата или у обработач функцију.

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

// шема.ts
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

- У обработачу који рукује свим позивима алата покушавамо да парсирамо долазни захтев у дефинисану шему алата:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ако то успе, онда настављамо да позивамо стварни алат:

    ```typescript
    const result = await tool.callback(input);
    ```

Као што видите, овај приступ ствара добру архитектуру јер све има своје место, *server.ts* је веома мали фајл који само повезује обрадјиваче захтева, а свака функција је у својој фасцикли, нпр. tools/, resources/ или /prompts/.

Сјајно, хајде да то направимо следеће.

## Вежба: Креирање ниско-ниво сервера

У овој вежби урадићемо следеће:

1. Креирати ниско-ниво сервер који рукује листањем алата и позивом алата.
1. Имплементирати архитектуру на коју се можете надоградити.
1. Додати валидацију како бисмо осигурали да су ваши позиви алата исправно валидирани.

### -1- Креирање архитектуре

Прва ствар коју треба решити је архитектура која нам помаже да се ширимо док додајемо више функција, ево како изгледа:

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

Сада смо поставили архитектуру која осигурава да лако можемо додавати нове алате у фолдер tools. Слободно пратите ово да бисте додали поддиректоријуме за ресурсе и упите.

### -2- Креирање алата

Погледајмо како изгледа креирање алата. Прво, мора бити креиран у његовом потфолдеру *tool* овако:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Валидација улаза користећи Пидантик модел
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: додати Пидантик, тако да можемо креирати AddInputModel и валидирати аргументе

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Овде видимо како дефинишемо име, опис и улазну шему коришћењем Pydantic-а и обработач који ће бити позван када се овај алат позове. На крају, излажемо `tool_add` који је речник са свим овим својствима.

Постоји и *schema.py* који се користи за дефинисање улазне шеме коју користи наш алат:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Такође морамо попунити *__init__.py* да би фолдер tools био третира као модул. Поред тога, морамо излагати модуле унутар њега овако:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Можемо наставити да додамо у овај фајл како будемо додавали више алата.

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

Овде креирамо речник састављен од својстава:

- name, ово је име алата.
- rawSchema, ово је Zod шема, користи се за валидацију долазних захтева за позив овог алата.
- inputSchema, ову шему користи обработач.
- callback, користи се за позив алата.

Постоји и `Tool` који се користи да претвори овај речник у тип који mcp server обрадјивач може прихватити и изгледа овако:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Постоји и *schema.ts* где чувамо улазне шеме за сваки алат који изгледа овако са само једном шемом тренутно, али како додајемо алате можемо додати више уноса:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Сјајно, хајде да прелазимо на обраду листања алата следеће.

### -3- Обрада листања алата

Да бисмо обрадили листање алата потребно је да подесимо обработач захтева за то. Ево шта треба да додамо у наш сервер фајл:

**Python**

```python
# код изостављен због краткоће
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

Овде додамо декоратор `@server.list_tools` и имплементациону функцију `handle_list_tools`. У овој последњој треба да направимо списак алата. Обратите пажњу да сваки алат треба да има name, description и inputSchema.

**TypeScript**

Да бисмо подесили обработач захтева за листање алата, позивамо `setRequestHandler` на серверу са шемом која одговара ономе шта желимо да радимо, у овом случају `ListToolsRequestSchema`.

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
// код изостављен због краткоће
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Врати листу регистрованих алата
  return {
    tools: tools
  };
});
```

Одлично, сада смо решили део листања алата, погледајмо како бисмо могли да обрађујемо позиве алата следеће.

### -4- Обрада позива алата

Да бисмо позвали алат, треба да подесимо други обработач захтева, ове пута фокусиран на обраду захтева који одређује коју функцију позвати и са којим аргументима.

**Python**

Користимо декоратор `@server.call_tool` и имплементирамо га функцијом као што је `handle_call_tool`. Унутар те функције морамо издвојити име алата, његове аргументе и осигурати да су аргументи валидни за тај алат. Можемо валидирати аргументе у овој функцији или касније у самом алату.

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
        # позвати алат
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Ево шта се дешава:

- Име алата је већ присутно као улазни параметар `name` и аргументи су у форми речника `arguments`.
- Алат се позива са `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Валидација аргумената се дешава у `handler` својству које показује на функцију. Ако то не успе, биће покренута изузетак.

Тиме сада имамо пуно разумевање како листати и позивати алате користећи ниско-ниво сервер.

Погледајте [пуни пример](./code/README.md) овде

## Задатак

Проширите код који сте добили са неколико алата, ресурса и упита и размислите како примећујете да је потребно само додавати фајлове у директоријум tools и нигде више.

*Нема решења дата*

## Резиме

У овом поглављу смо видели како ради приступ ниско-ниво сервера и како нам то помаже да креирамо лепу архитектуру на којој можемо наставити да градимо. Такође смо разговарали о валидацији и показано вам је како радити са библиотекама за валидирање да бисте креирали шеме за валидацију улазних података.

## Шта следи

- Следеће: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде прецизан, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Нисмо одговорни за било каква неспоразума или погрешна тумачења која могу проистећи из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->