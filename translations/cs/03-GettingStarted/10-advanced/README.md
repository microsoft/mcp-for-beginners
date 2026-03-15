# Pokročilé použití serveru

V MCP SDK jsou k dispozici dva různé typy serverů, váš běžný server a nízkoúrovňový server. Obvykle byste používali běžný server k přidávání funkcí. V některých případech však chcete spoléhat na nízkoúrovňový server, například:

- Lepší architektura. Je možné vytvořit čistou architekturu jak s běžným serverem, tak s nízkoúrovňovým serverem, ale lze tvrdit, že je to o něco jednodušší s nízkoúrovňovým serverem.
- Dostupnost funkcí. Některé pokročilé funkce lze použít pouze s nízkoúrovňovým serverem. Uvidíte to v pozdějších kapitolách, když budeme přidávat vzorkování a vyvolávání.

## Běžný server vs nízkoúrovňový server

Takto vypadá vytvoření MCP serveru s běžným serverem

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

// Přidejte nástroj pro sčítání
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

Podstata je v tom, že explicitně přidáte každý nástroj, zdroj nebo výzvu, kterou chcete, aby server měl. Na tom není nic špatného.  

### Přístup nízkoúrovňového serveru

Pokud však používáte přístup nízkoúrovňového serveru, musíte o tom přemýšlet jinak. Místo registrace každého nástroje vytvoříte dvě funkce zpracovatelské pro každý typ funkce (nástroje, zdroje nebo výzvy). Například tedy nástroje mají pouze dvě funkce takto:

- Výpis všech nástrojů. Jedna funkce bude zodpovědná za všechny pokusy o vypsání nástrojů.
- Zpracování volání všech nástrojů. Zde je také pouze jedna funkce, která zpracovává volání nástroje.

To zní jako potenciálně méně práce, že? Místo registrace nástroje tedy stačí zajistit, že nástroj je uveden při výpisu nástrojů a že je volán, když přijde požadavek na volání nástroje.

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

Zde nyní máme funkci, která vrací seznam funkcí. Každá položka v seznamu nástrojů má nyní pole jako `name`, `description` a `inputSchema`, aby se dodržel návratový typ. To nám umožňuje umístit naše nástroje a definice funkcí jinam. Nyní můžeme vytvořit všechny naše nástroje ve složce tools a to samé platí pro všechny vaše funkce, takže váš projekt může najednou vypadat takto:

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

A co volání nástrojů, je pak stejný princip, jedna funkce zpracovatel, která volá nástroj, ať už kterýkoli? Ano, přesně tak, zde je kód pro to:

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

Jak vidíte z výše uvedeného kódu, musíme rozparsovat, který nástroj volat a s jakými argumenty, a pak pokračovat voláním nástroje.

## Vylepšení přístupu pomocí validace

Doposud jste viděli, jak všechny vaše registrace k přidání nástrojů, zdrojů a výzev mohou být nahrazeny těmito dvěma funkcemi zpracovatelskými na typ funkce. Co ještě musíme udělat? Měli bychom přidat nějakou formu validace, abychom zajistili, že nástroj je volán s pravými argumenty. Každé runtime má své řešení, například Python používá Pydantic a TypeScript používá Zod. Myšlenka je taková, že provedeme následující:

- Přesuneme logiku pro vytváření funkce (nástroj, zdroj nebo výzva) do jeho samostatné složky.
- Přidáme způsob, jak validovat příchozí požadavek například na volání nástroje.

### Vytvoření funkce

Pro vytvoření funkce budeme muset vytvořit soubor pro danou funkci a zajistit, že má povinná pole vyžadovaná pro danou funkci. Která pole se trochu liší mezi nástroji, zdroji a výzvami.

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

- Vytvoříme schéma pomocí Pydantic `AddInputModel` s poli `a` a `b` v souboru *schema.py*.
- Pokusíme se rozparsovat příchozí požadavek na typ `AddInputModel`, pokud dojde k nesouladu parametrů, dojde k chybě:

   ```python
   # add.py
    try:
        # Ověřte vstup pomocí Pydantic modelu
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Můžete si vybrat, zda dát logiku parsování přímo do volání nástroje nebo do funkce zpracovatele.

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

- Ve zpracovateli, který řeší všechna volání nástrojů, nyní zkusíme rozparsovat příchozí požadavek do schématu definovaného nástrojem:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    pokud to funguje, pokračujeme ve volání samotného nástroje:

    ```typescript
    const result = await tool.callback(input);
    ```

Jak vidíte, tento přístup vytváří skvělou architekturu, protože vše má své místo, *server.ts* je velmi malý soubor, který jen propojuje zpracovatele požadavků, a každá funkce je ve své vlastní složce, tedy tools/, resources/ nebo /prompts.

Skvělé, pojďme to dále postavit.

## Cvičení: Vytvoření nízkoúrovňového serveru

V tomto cvičení uděláme následující:

1. Vytvoříme nízkoúrovňový server, který bude zpracovávat výpis nástrojů a volání nástrojů.
1. Implementujeme architekturu, na kterou můžete stavět.
1. Přidáme validaci, abyste měli správně ověřené volání nástrojů.

### -1- Vytvoření architektury

První, co musíme řešit, je architektura, která nám pomůže škálovat při přidávání více funkcí, takto vypadá:

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

Nyní jsme nastavili architekturu, která zajišťuje, že můžeme snadno přidávat nové nástroje ve složce tools. Klidně pokračujte tímto způsobem a přidejte podadresáře pro resources a prompts.

### -2- Vytvoření nástroje

Podívejme se, jak vypadá vytvoření nástroje. Nejprve musí být vytvořen ve své podsložce *tool* takto:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validujte vstup pomocí Pydantic modelu
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: přidat Pydantic, abychom mohli vytvořit AddInputModel a validovat argumenty

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Vidíme zde, jak definujeme název, popis a vstupní schéma pomocí Pydantic a zpracovatele, který bude vyvolán, jakmile bude tento nástroj volán. Nakonec zpřístupňujeme `tool_add`, což je slovník obsahující všechny tyto vlastnosti.

Je zde také *schema.py*, který definuje vstupní schéma používané naším nástrojem:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Musíme také vyplnit *__init__.py*, aby byla složka tools považována za modul. Navíc musíme zpřístupnit moduly uvnitř takto:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Do tohoto souboru můžeme přidávat další položky, jak budeme přidávat více nástrojů.

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

- name, což je název nástroje.
- rawSchema, což je Zod schéma, které bude použito k validaci přicházejících požadavků na volání nástroje.
- inputSchema, toto schéma bude použito zpracovatelem.
- callback, to se používá k vyvolání nástroje.

Dále je tam `Tool`, který převádí tento slovník na typ, který může MCP server zpracovat, a vypadá takto:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

A je zde *schema.ts*, kde uchováváme vstupní schémata pro každý nástroj, které v současnosti obsahuje pouze jedno schéma, ale jak budeme přidávat nástroje, přidáme i další položky:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Skvělé, pojďme nyní pokračovat zpracováním výpisu našich nástrojů.

### -3- Zpracování výpisu nástrojů

Dále, pro zpracování výpisu našich nástrojů, musíme nastavit zpracovatele požadavku pro to. Toto je, co musíme přidat do našeho serverového souboru:

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

Zde přidáváme dekorátor `@server.list_tools` a implementující funkci `handle_list_tools`. V té musíme vytvořit seznam nástrojů. Všimněte si, že každý nástroj musí obsahovat název, popis a inputSchema.   

**TypeScript**

Pro nastavení zpracovatele požadavků pro výpis nástrojů musíme zavolat `setRequestHandler` na serveru se schématem, které odpovídá naší činnosti, v tomto případě `ListToolsRequestSchema`.

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

Skvělé, nyní máme vyřešený kus výpisu nástrojů, podívejme se jak pak můžeme volat nástroje.

### -4- Zpracování volání nástroje

Pro volání nástroje musíme nastavit další zpracovatele požadavků, tentokrát zaměřeného na řešení požadavku, který určuje, kterou funkci volat a s jakými argumenty.

**Python**

Použijme dekorátor `@server.call_tool` a implementujme ho s funkcí jako `handle_call_tool`. V rámci této funkce musíme rozparsovat název nástroje, jeho argumenty a zajistit, že argumenty jsou platné pro daný nástroj. Můžeme argumenty validovat buď tady, nebo později přímo v nástroji.

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
        # zavolat nástroj
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Takto to funguje:

- Název nástroje je přítomen jako vstupní parametr `name`, a argumenty máme ve formě slovníku `arguments`.

- Nástroj je volán pomocí `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validace argumentů se děje v `handler` vlastnosti, která ukazuje na funkci, pokud validace selže, vyvolá se výjimka.

Takže teď máme kompletní pochopení výpisu a volání nástrojů pomocí nízkoúrovňového serveru.

Vizuální [plný příklad](./code/README.md) zde

## Zadání

Rozšiřte kód, který jste dostali, o řadu nástrojů, zdrojů a výzev a zamyslete se nad tím, jak si všímáte, že je třeba přidávat soubory pouze ve složce tools a nikde jinde. 

*Žádné řešení není poskytnuto*

## Shrnutí

V této kapitole jsme viděli, jak funguje přístup nízkoúrovňového serveru a jak nám může pomoci vytvořit pěknou architekturu, na kterou můžeme dále stavět. Diskutovali jsme také o validaci a ukázalo se, jak pracovat s validačními knihovnami k vytváření schémat pro validaci vstupu.

## Co bude dál

- Dále: [Jednoduchá autentizace](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo mylné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->