# Pokročilé použití serveru

V MCP SDK jsou k dispozici dva různé typy serverů: běžný server a nízkoúrovňový server. Obvykle používáte běžný server k přidávání funkcí. V některých případech však může být vhodné spolehnout se na nízkoúrovňový server, například:

- Lepší architektura. Je možné vytvořit čistou architekturu jak s běžným serverem, tak s nízkoúrovňovým serverem, ale lze argumentovat, že s nízkoúrovňovým serverem je to o něco jednodušší.
- Dostupnost funkcí. Některé pokročilé funkce lze použít pouze s nízkoúrovňovým serverem. Uvidíte to v dalších kapitolách, když budeme přidávat vzorkování a elicitační procesy.

## Běžný server vs nízkoúrovňový server

Takto vypadá vytvoření MCP serveru pomocí běžného serveru:

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

Pointa je, že explicitně přidáváte každý nástroj, zdroj nebo prompt, který chcete, aby server obsahoval. Na tom není nic špatného.  

### Přístup nízkoúrovňového serveru

Když však použijete přístup nízkoúrovňového serveru, musíte přemýšlet jinak, konkrétně místo registrace každého nástroje vytvoříte dva handlery pro každý typ funkce (nástroje, zdroje nebo prompty). Například u nástrojů budete mít pouze dvě funkce, jako například:

- Výpis všech nástrojů. Jedna funkce bude zodpovědná za všechny pokusy o výpis nástrojů.
- Zpracování volání všech nástrojů. Zde také existuje pouze jedna funkce, která zpracovává volání nástroje.

To zní jako potenciálně méně práce, že? Místo registrace nástroje stačí zajistit, aby byl nástroj uveden při výpisu všech nástrojů a aby byl volán při příchozím požadavku na volání nástroje. 

Podívejme se, jak nyní vypadá kód:

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

Zde máme funkci, která vrací seznam funkcí. Každý záznam v seznamu nástrojů nyní obsahuje pole jako `name`, `description` a `inputSchema`, aby odpovídal návratovému typu. To nám umožňuje umístit definice nástrojů a funkcí jinam. Nyní můžeme vytvořit všechny naše nástroje ve složce nástrojů a totéž platí pro všechny vaše funkce, takže váš projekt může být najednou organizován takto:

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

To je skvělé, naše architektura může být vytvořena tak, aby vypadala docela čistě.

A co volání nástrojů, je to stejný princip, tedy jeden handler pro volání nástroje, jakéhokoliv nástroje? Ano, přesně tak, zde je kód pro to:

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

Jak vidíte z výše uvedeného kódu, musíme rozparsovat nástroj, který má být volán, a s jakými argumenty, a poté musíme pokračovat v volání nástroje.

## Zlepšení přístupu pomocí validace

Doposud jste viděli, jak všechny vaše registrace pro přidání nástrojů, zdrojů a promptů mohou být nahrazeny těmito dvěma handlery pro každý typ funkce. Co dalšího musíme udělat? Měli bychom přidat nějakou formu validace, abychom zajistili, že nástroj je volán se správnými argumenty. Každé runtime má své vlastní řešení pro toto, například Python používá Pydantic a TypeScript používá Zod. Myšlenka je následující:

- Přesuňte logiku pro vytvoření funkce (nástroje, zdroje nebo promptu) do její dedikované složky.
- Přidejte způsob validace příchozího požadavku, například na volání nástroje.

### Vytvoření funkce

Pro vytvoření funkce budeme muset vytvořit soubor pro tuto funkci a zajistit, že obsahuje povinná pole požadovaná pro tuto funkci. Tato pole se mírně liší mezi nástroji, zdroji a prompty.

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

Zde můžete vidět, jak provádíme následující:

- Vytvoříme schéma pomocí Pydantic `AddInputModel` s poli `a` a `b` ve souboru *schema.py*.
- Pokusíme se rozparsovat příchozí požadavek, aby byl typu `AddInputModel`. Pokud dojde k nesouladu parametrů, dojde k chybě:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Můžete si vybrat, zda tuto logiku parsování umístíte přímo do volání nástroje nebo do funkce handleru.

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

- V handleru, který zpracovává všechna volání nástrojů, se nyní pokusíme rozparsovat příchozí požadavek do definovaného schématu nástroje:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Pokud to funguje, pokračujeme v volání skutečného nástroje:

    ```typescript
    const result = await tool.callback(input);
    ```

Jak vidíte, tento přístup vytváří skvělou architekturu, protože vše má své místo, soubor *server.ts* je velmi malý a pouze propojuje handlery požadavků, zatímco každá funkce je ve své příslušné složce, tj. tools/, resources/ nebo prompts/.

Skvělé, pojďme to zkusit postavit.

## Cvičení: Vytvoření nízkoúrovňového serveru

V tomto cvičení provedeme následující:

1. Vytvoříme nízkoúrovňový server, který zpracovává výpis nástrojů a volání nástrojů.
1. Implementujeme architekturu, na které můžete stavět.
1. Přidáme validaci, abychom zajistili, že volání nástrojů jsou správně validována.

### -1- Vytvoření architektury

První věc, kterou musíme řešit, je architektura, která nám pomůže škálovat, jak přidáváme více funkcí. Takto to vypadá:

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

Nyní máme nastavenou architekturu, která zajišťuje, že můžeme snadno přidávat nové nástroje do složky tools. Neváhejte podle toho přidat podadresáře pro resources a prompts.

### -2- Vytvoření nástroje

Podívejme se, jak vypadá vytvoření nástroje. Nejprve musí být vytvořen ve svém podadresáři *tool* takto:

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

Zde vidíme, jak definujeme název, popis, vstupní schéma pomocí Pydantic a handler, který bude vyvolán, jakmile bude tento nástroj volán. Nakonec vystavujeme `tool_add`, což je slovník obsahující všechny tyto vlastnosti.

Existuje také *schema.py*, který se používá k definování vstupního schématu používaného naším nástrojem:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Musíme také naplnit *__init__.py*, abychom zajistili, že složka tools bude považována za modul. Navíc musíme vystavit moduly uvnitř ní takto:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Tento soubor můžeme dále rozšiřovat, jak přidáváme více nástrojů.

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

Zde vytvoříme slovník sestávající z vlastností:

- name, což je název nástroje.
- rawSchema, což je Zod schéma, které bude použito k validaci příchozích požadavků na volání tohoto nástroje.
- inputSchema, toto schéma bude použito handlerem.
- callback, což se používá k vyvolání nástroje.

Existuje také `Tool`, který se používá k převodu tohoto slovníku na typ, který může přijmout handler MCP serveru, a vypadá takto:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

A existuje *schema.ts*, kde ukládáme vstupní schémata pro každý nástroj, který vypadá takto s pouze jedním schématem v současnosti, ale jak přidáváme nástroje, můžeme přidávat další položky:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Skvělé, pokračujme k zpracování výpisu našich nástrojů.

### -3- Zpracování výpisu nástrojů

Dále, abychom zpracovali výpis našich nástrojů, musíme nastavit handler požadavků pro to. Zde je to, co musíme přidat do našeho serverového souboru:

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

Zde přidáváme dekorátor `@server.list_tools` a implementační funkci `handle_list_tools`. V té druhé musíme vytvořit seznam nástrojů. Všimněte si, že každý nástroj musí mít název, popis a inputSchema.   

**TypeScript**

Pro nastavení handleru požadavků na výpis nástrojů musíme zavolat `setRequestHandler` na serveru se schématem odpovídajícím tomu, co se snažíme udělat, v tomto případě `ListToolsRequestSchema`. 

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

Skvělé, nyní jsme vyřešili část výpisu nástrojů, podívejme se, jak bychom mohli volat nástroje.

### -4- Zpracování volání nástroje

Pro volání nástroje musíme nastavit další handler požadavků, tentokrát zaměřený na zpracování požadavku specifikujícího, kterou funkci volat a s jakými argumenty.

**Python**

Použijme dekorátor `@server.call_tool` a implementujme ho funkcí jako `handle_call_tool`. V této funkci musíme rozparsovat název nástroje, jeho argumenty a zajistit, že argumenty jsou platné pro daný nástroj. Můžeme buď validovat argumenty v této funkci, nebo dále v samotném nástroji.

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

Zde se děje následující:

- Název našeho nástroje je již přítomen jako vstupní parametr `name`, což platí i pro naše argumenty ve formě slovníku `arguments`.

- Nástroj je volán pomocí `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validace argumentů probíhá v vlastnosti `handler`, která odkazuje na funkci. Pokud to selže, vyvolá se výjimka. 

A je to, nyní máme plné pochopení výpisu a volání nástrojů pomocí nízkoúrovňového serveru.

Podívejte se na [úplný příklad](./code/README.md) zde.

## Úkol

Rozšiřte kód, který jste dostali, o několik nástrojů, zdrojů a promptů a zamyslete se nad tím, jak si všimnete, že stačí přidávat soubory do složky tools a nikam jinam. 

*Řešení není uvedeno*

## Shrnutí

V této kapitole jsme viděli, jak funguje přístup nízkoúrovňového serveru a jak nám může pomoci vytvořit pěknou architekturu, na které můžeme dále stavět. Diskutovali jsme také o validaci a bylo vám ukázáno, jak pracovat s validačními knihovnami k vytvoření schémat pro validaci vstupů.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.