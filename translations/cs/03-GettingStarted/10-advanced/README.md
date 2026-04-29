# Pokročilé použití serveru

V MCP SDK existují dva různé typy serverů, váš běžný server a nízkoúrovňový server. Obvykle byste používali běžný server pro přidávání funkcí. V některých případech však chcete spoléhat na nízkoúrovňový server, například:

- Lepší architektura. Je možné vytvořit čistou architekturu jak s běžným serverem, tak s nízkoúrovňovým serverem, ale lze tvrdit, že s nízkoúrovňovým serverem je to o něco jednodušší.
- Dostupnost funkcí. Některé pokročilé funkce lze použít pouze s nízkoúrovňovým serverem. To uvidíte v následujících kapitolách, jak přidáváme sampling a elicitation.

## Běžný server vs nízkoúrovňový server

Takto vypadá vytvoření MCP Serveru s běžným serverem

**Python**

```python
mcp = FastMCP("Demo")

# Přidat nástroj pro sčítání
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

// Přidat nástroj pro sčítání
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

Podstatou je, že explicitně přidáváte každý nástroj, zdroj nebo prompt, který chcete, aby server měl. Na tom není nic špatného.

### Přístup nízkoúrovňového serveru

Při použití nízkoúrovňového serveru je ovšem potřeba myslet na to jinak. Místo registrace každého nástroje vytvoříte dva handlery pro každý typ funkce (nástroje, zdroje nebo prompty). Například nástroje pak mají pouze dvě funkce:

- Vyjmenování všech nástrojů. Jedna funkce má na starost všechny pokusy o vypsání nástrojů.
- Zpracování volání všech nástrojů. I zde je pouze jedna funkce, která zpracovává volání nástroje.

To zní jako potenciálně méně práce, že? Místo registrace nástroje tedy stačí zajistit, aby byl nástroj uveden při vypsání všech nástrojů a aby byl zavolán, když přijde požadavek na volání nástroje.

Pojďme se podívat, jak nyní vypadá kód:

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
  // Vrátit seznam registrovaných nástrojů
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

Zde nyní máme funkci, která vrací seznam funkcí. Každá položka v seznamu nástrojů má pole jako `name`, `description` a `inputSchema`, aby odpovídala návratovému typu. To nám umožňuje umístit definice nástrojů a funkcí jinde. Nyní můžeme vytvořit všechny nástroje ve složce tools a totéž platí pro všechny vaše funkce, takže váš projekt může být náhle uspořádán takto:

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

To je skvělé, naši architekturu lze udělat poměrně čistou.

A co volání nástrojů, je to ta samá myšlenka, jeden handler na volání nástroje, kterýkoliv nástroj? Ano, přesně tak, tady je kód pro to:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools je slovník s názvy nástrojů jako klíči
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
    // TODO zavolat nástroj,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Jak vidíte z výše uvedeného kódu, musíme parsovat nástroj k volání a s jakými argumenty, a pak musíme pokračovat voláním nástroje.

## Vylepšení přístupu s validací

Zatím jste viděli, jak lze všechny vaše registrace pro přidávání nástrojů, zdrojů a promptů nahradit těmito dvěma handlery na typ funkce. Co dalšího musíme udělat? Měli bychom přidat nějakou formu validace, abychom zajistili, že se nástroj volá s správnými argumenty. Každé runtime má své vlastní řešení, například Python používá Pydantic a TypeScript používá Zod. Myšlenka je, že uděláme následující:

- Přesuneme logiku vytváření funkce (nástroj, zdroj nebo prompt) do její vlastní složky.
- Přidáme způsob validace příchozího požadavku, například pro volání nástroje.

### Vytvoření funkce

K vytvoření funkce budeme potřebovat vytvořit soubor pro tuto funkci a zajistit, aby měl povinná pole požadovaná funkci. Která pole se trochu liší mezi nástroji, zdroji a promptami.

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
        # Ověřte vstup pomocí Pydantic modelu
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: přidat Pydantic, aby bylo možné vytvořit AddInputModel a ověřit argumenty

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

zde vidíte, jak děláme následující:

- Vytvoříme schéma pomocí Pydantic `AddInputModel` s poli `a` a `b` v souboru *schema.py*.
- Pokusíme se parsovat příchozí požadavek na typ `AddInputModel`, pokud se parametry neshodují, dojde k chybě:

   ```python
   # add.py
    try:
        # Ověřte vstup pomocí modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Můžete si zvolit, zda tuto logiku parsování umístíte přímo do volání nástroje nebo do handleru.

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

- V handleru zpracovávajícím všechna volání nástrojů se nyní pokoušíme parsovat příchozí požadavek podle definovaného schématu nástroje:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    pokud to projde, pokračujeme voláním skutečného nástroje:

    ```typescript
    const result = await tool.callback(input);
    ```

Jak vidíte, tento přístup vytváří skvělou architekturu, protože vše má své místo, soubor *server.ts* je velmi malý a pouze propojuje request handlery a každá funkce je ve své složce, tj. tools/, resources/ nebo /prompts.

Skvěle, pojďme to zkusit postavit dále.

## Cvičení: Vytvoření nízkoúrovňového serveru

V tomto cvičení uděláme následující:

1. Vytvoříme nízkoúrovňový server, který bude zpracovávat vypsání nástrojů a jejich volání.
1. Implementujeme architekturu, na které můžete stavět.
1. Přidáme validaci, aby se volání nástrojů správně ověřovala.

### -1- Vytvoření architektury

První věc, kterou musíme řešit, je architektura, která nám pomůže škálovat, jak přidáváme další funkce, takto to vypadá:

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

Nyní jsme nastavili architekturu, která zajistí, že můžeme snadno přidávat nové nástroje ve složce tools. Klidně přidejte podadresáře pro resources a prompts.

### -2- Vytvoření nástroje

Podívejme se, jak vypadá vytvoření nástroje. Nejprve musí být vytvořen ve své podsložce *tool* takto:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Ověřte vstup pomocí modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: přidat Pydantic, abychom mohli vytvořit AddInputModel a ověřit argumenty

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Tady vidíme, jak definujeme název, popis a vstupní schéma pomocí Pydantic a handler, který bude volán při volání nástroje. Nakonec vystavujeme `tool_add`, což je slovník obsahující všechny tyto vlastnosti.

Je zde také *schema.py*, který se používá k definici vstupního schématu našeho nástroje:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Musíme také naplnit *__init__.py*, aby byla složka tools považována za modul. Navíc musíme vystavit moduly v něm takto:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Do tohoto souboru můžeme přidávat další, jak přidáváme nástroje.

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

Zde vytváříme slovník obsahující vlastnosti:

- name, to je název nástroje.
- rawSchema, to je Zod schéma, které se použije pro validaci příchozích požadavků na volání nástroje.
- inputSchema, toto schéma používá handler.
- callback, tímto se nástroj vyvolává.

Je zde také `Tool`, který slouží k převodu tohoto slovníku na typ, který může handler mcp serveru přijmout, a vypadá takto:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

A je zde *schema.ts*, kde uchováváme vstupní schémata pro každý nástroj, v současnosti s jedním schématem, ale jak přidáváme další nástroje, můžeme přidávat další položky:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Výborně, pojďme pokračovat ve zpracování vypsání našich nástrojů.

### -3- Zpracování vypsání nástrojů

K vypsání nástrojů potřebujeme nastavit request handler. Tady je, co si přidáme do našeho serverového souboru:

**Python**

```python
# kód vynechán pro stručnost
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

Zde přidáváme dekorátor `@server.list_tools` a implementační funkci `handle_list_tools`. V ní musíme vytvořit seznam nástrojů. Všimněte si, že každý nástroj musí mít název, popis a inputSchema.

**TypeScript**

Pro nastavení request handleru na vypsání nástrojů je potřeba zavolat `setRequestHandler` na serveru se schématem odpovídajícím našemu požadavku, v tomto případě `ListToolsRequestSchema`.

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
// kód vynechán pro stručnost
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Vrátit seznam registrovaných nástrojů
  return {
    tools: tools
  };
});
```

Výborně, nyní máme vyřešeno vypsání nástrojů, podívejme se na to, jak bychom mohli volat nástroje.

### -4- Zpracování volání nástroje

Pro volání nástroje je potřeba nastavit další request handler, tentokrát zaměřený na požadavek specifikující, kterou funkci volat a s jakými argumenty.

**Python**

Použijeme dekorátor `@server.call_tool` a implementujeme funkci `handle_call_tool`. V ní musíme parsovat název nástroje, jeho argumenty a zajistit, že argumenty jsou platné pro daný nástroj. Validaci argumentů můžeme dělat buď zde, nebo přímo v nástroji.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools je slovník s názvy nástrojů jako klíči
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # zavolejte nástroj
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Tady se děje:

- Název našeho nástroje je již přítomen jako vstupní parametr `name` a argumenty jsou ve slovníku `arguments`.

- Nástroj je volán pomocí `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validace argumentů probíhá v exportovaném `handleru`, pokud selže, vyvolá výjimku.

Tak tedy máme kompletní pochopení vypsání a volání nástrojů pomocí nízkoúrovňového serveru.

Podívejte se na [plný příklad](./code/README.md)

## Zadání úkolu

Rozšiřte poskytnutý kód o několik nástrojů, zdrojů a promptů a všimněte si, že je potřeba přidávat soubory pouze ve složce tools a nikde jinde.

*Řešení není k dispozici*

## Shrnutí

V této kapitole jsme viděli, jak funguje přístup nízkoúrovňového serveru a jak nám může pomoci vytvořit pěknou architekturu, na které můžeme dále stavět. Také jsme probírali validaci a ukázali jsme, jak pracovat s validačními knihovnami pro tvorbu schémat pro ověřování vstupů.

## Co bude dál

- Dále: [Jednoduchá autentifikace](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->