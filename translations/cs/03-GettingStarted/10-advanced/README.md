# Pokročilé použití serveru

V MCP SDK jsou vystaveny dva různé typy serverů, váš běžný server a nízkoúrovňový server. Normálně byste používali běžný server k přidávání funkcí. V některých případech však chcete spoléhat na nízkoúrovňový server, například:

- Lepší architektura. Je možné vytvořit čistou architekturu jak s běžným serverem, tak s nízkoúrovňovým serverem, ale dá se tvrdit, že s nízkoúrovňovým serverem je to trochu jednodušší.
- Dostupnost funkcí. Některé pokročilé funkce lze používat pouze s
    nízkoúrovňovým serverem. Pozdější kapitoly se zabývají Elicitation a starší funkcí Sampling,
    která je v MCP `2026-07-28` označena jako zastaralá.

## Běžný server vs nízkoúrovňový server

Takto vypadá vytvoření MCP Serveru s běžným serverem

**Python**

```python
mcp = FastMCP("Demo")

# Přidejte nástroj pro sčítání
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

Pointa je, že explicitně přidáváte každý nástroj, zdroj nebo prompt, který chcete, aby server měl. Na tom není nic špatného.  

### Přístup nízkoúrovňového serveru

Při použití přístupu nízkoúrovňového serveru je potřeba na to myslet jinak. Místo registrace každého nástroje vytváříte dva handlery pro každý typ funkce (nástroje, zdroje nebo prompty). Například nástroje mají jen dvě funkce:

- Výpis všech nástrojů. Jedna funkce je zodpovědná za všechny pokusy o výpis nástrojů.
- Zpracování volání všech nástrojů. I zde je jen jedna funkce, která zpracovává volání nástroje.

To zní jako potenciálně méně práce, že? Takže místo registrace nástroje jen musím zajistit, že nástroj je vypsán, když vypisuji všechny nástroje, a že je vyvolán, když přijde požadavek na jeho zavolání.

Podívejme se, jak kód nyní vypadá:

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

Nyní máme funkci, která vrací seznam funkcí. Každá položka v seznamu nástrojů nyní obsahuje pole jako `name`, `description` a `inputSchema` pro dodržení návratového typu. To nám umožňuje umístit naše nástroje a definice funkcí jinam. Náš projekt může být nyní organizován například takto:

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

To je skvělé, naše architektura může být velmi čistá.

A co volání nástrojů? Je to stejný princip, jeden handler na volání nástroje, kterýkoliv nástroj? Ano, přesně tak, tady je kód pro to:

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

Jak vidíte z výše uvedeného kódu, musíme získat, který nástroj zavolat a s jakými argumenty, a pak přistoupit k volání nástroje.

## Vylepšení přístupu validací

Dosud jste viděli, jak všechny vaše registrace pro přidání nástrojů, zdrojů a promptů mohou být nahrazeny těmito dvěma handlery pro každý typ funkce. Co dál musíme udělat? Měli bychom přidat nějakou formu validace, abychom zajistili, že nástroj je volán se správnými argumenty. Každé runtime má svoje řešení, například Python používá Pydantic a TypeScript používá Zod. Myšlenka je následující:

- Přesunout logiku pro vytvoření funkce (nástroj, zdroj nebo prompt) do její vyhrazené složky.
- Přidat možnost validovat příchozí požadavky např. na volání nástroje.

### Vytvoření funkce

Pro vytvoření funkce budeme potřebovat vytvořit soubor pro tuto funkci a zajistit, aby obsahoval povinná pole požadovaná pro tuto funkci. Která pole se mírně liší mezi nástroji, zdroji a promptami.

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
        # Ověřte vstup pomocí modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: přidejte Pydantic, abychom mohli vytvořit AddInputModel a ověřit argumenty

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

- Vytvořit schéma pomocí Pydantic `AddInputModel` s poli `a` a `b` v souboru *schema.py*.
- Pokusit se analyzovat příchozí požadavek jako typ `AddInputModel`, pokud jsou parametry nesprávné, dojde k chybě:

   ```python
   # add.py
    try:
        # Ověřte vstup pomocí modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Můžete si vybrat, zda tuto logiku parsování dát přímo do volání nástroje nebo do handler funkce.

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

- V handleru, který obsluhuje všechna volání nástrojů, se nyní pokusíme analyzovat příchozí požadavek podle schématu definovaného nástrojem:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    pokud to funguje, pak pokračujeme ve volání skutečného nástroje:

    ```typescript
    const result = await tool.callback(input);
    ```

Jak vidíte, tento přístup umožňuje vytvořit skvělou architekturu, protože vše má své místo, soubor *server.ts* je velmi malý a jen propojuje handlery požadavků a každá funkce je ve své složce, tj. tools/, resources/ nebo /prompts.

Skvělé, zkuste toto nyní sestavit.

## Cvičení: Vytvoření nízkoúrovňového serveru

V tomto cvičení uděláme následující:

1. Vytvoříme nízkoúrovňový server, který bude spravovat výpis nástrojů a volání nástrojů.
1. Implementujeme architekturu, na které můžete stavět.
1. Přidáme validaci, která zajistí správné ověření volání nástrojů.

### -1- Vytvoření architektury

Nejprve se zaměříme na architekturu, která nám pomůže škálovat, jak přidáváme další funkce, takto to vypadá:

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

Nyní máme nastavenou architekturu, která zajistí, že můžeme snadno přidávat nové nástroje ve složce tools. Klidně přidejte další podsložky pro resources a prompts.

### -2- Vytvoření nástroje

Podívejme se nyní, jak vypadá vytvoření nástroje. Nejprve musí být vytvořen ve své podsložce *tool* takto:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Ověřte vstup pomocí Pydantic modelu
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

Co zde vidíme, je definice názvu, popisu a vstupního schématu pomocí Pydantic a handleru, který bude vyvolán, jakmile bude tento nástroj volán. Nakonec vystavujeme `tool_add`, což je slovník obsahující všechny tyto vlastnosti.

Je tu také *schema.py*, který definuje vstupní schéma používané naším nástrojem:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Také je potřeba vyplnit *__init__.py*, aby se adresář tools považoval za modul. Navíc musíme moduly v něm vystavit takto:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Do tohoto souboru můžeme nadále přidávat další nástroje.

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

Zde vytváříme slovník skládající se z vlastností:

- name, což je název nástroje.
- rawSchema, což je Zod schéma, které bude použito k validaci příchozích požadavků na volání tohoto nástroje.
- inputSchema, toto schéma bude použito v handleru.
- callback, které slouží k vyvolání nástroje.

Dále je tu `Tool`, které se používá k převodu tohoto slovníku na typ, který může přijmout mcp server handler, a vypadá takto:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

A tu je *schema.ts*, kde ukládáme vstupní schémata pro každý nástroj, zatím je tam jen jedno, ale můžeme přidávat další, jak budeme přidávat nástroje:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Skvělé, pokračujme nyní tím, jak zpracovat výpis našich nástrojů.

### -3- Zpracování výpisu nástrojů

Dále je potřeba nastavit request handler pro výpis našich nástrojů. Toto přidáme do našeho serverového souboru:

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

Zde přidáváme dekorátor `@server.list_tools` a implementační funkci `handle_list_tools`. V této funkci musíme vytvořit seznam nástrojů. Všimněte si, jak každý nástroj musí mít název, popis a inputSchema.   

**TypeScript**

Nastavení request handleru pro výpis nástrojů spočívá v zavolání `setRequestHandler` na serveru s odpovídajícím schématem, v tomto případě `ListToolsRequestSchema`. 

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

Skvělé, teď, když jsme vyřešili část výpisu nástrojů, podívejme se, jak by se mohlo volat nástroje.

### -4- Zpracování volání nástroje

Pro volání nástroje potřebujeme nastavit další request handler, který bude zpracovávat požadavek specifikující, kterou funkci volat a s jakými argumenty.

**Python**

Použijeme dekorátor `@server.call_tool` a implementujeme funkci jako `handle_call_tool`. V této funkci musíme rozparsovat název nástroje, jeho argumenty a zajistit, že argumenty jsou platné pro daný nástroj. Validaci můžeme provést buď zde, nebo později přímo v nástroji.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools je slovník s názvy nástrojů jako klíče
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # vyvolej nástroj
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Toto se zde děje:

- Název nástroje je již přítomen jako vstupní parametr `name`, což platí i pro naše argumenty ve formě slovníku `arguments`.

- Nástroj je volán pomocí `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validace argumentů probíhá v `handler` vlastnosti, která ukazuje na funkci, pokud validace selže, vyvolá výjimku.

Tím jsme nyní plně pochopili výpis a volání nástrojů pomocí nízkoúrovňového serveru.

Podívejte se na [kompletní příklad](./code/README.md) zde

## Zadání

Rozšiřte předaný kód o několik nástrojů, zdrojů a promptů a zamyslete se, jak si všímáte, že stačí přidávat pouze soubory v adresáři tools a nikde jinde. 

*Řešení není k dispozici*

## Shrnutí

V této kapitole jsme viděli, jak funguje přístup nízkoúrovňového serveru a jak nám může pomoci vytvořit čistou architekturu, na kterou můžeme pokračovat stavět. Také jsme diskutovali o validaci a ukázali jsme vám, jak pracovat s validačními knihovnami pro vytvoření schémat pro validaci vstupu.

## Co dál

- Dále: [Jednoduchá autentizace](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->