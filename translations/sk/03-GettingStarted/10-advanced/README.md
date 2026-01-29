# Pokročilé používanie servera

V MCP SDK sú dostupné dva typy serverov: bežný server a nízkoúrovňový server. Zvyčajne používate bežný server na pridávanie funkcií. V niektorých prípadoch však môžete chcieť použiť nízkoúrovňový server, napríklad:

- Lepšia architektúra. Je možné vytvoriť čistú architektúru s bežným aj nízkoúrovňovým serverom, ale dá sa argumentovať, že s nízkoúrovňovým serverom je to o niečo jednoduchšie.
- Dostupnosť funkcií. Niektoré pokročilé funkcie je možné použiť iba s nízkoúrovňovým serverom. Uvidíte to v neskorších kapitolách, keď pridáme sampling a elicitation.

## Bežný server vs nízkoúrovňový server

Takto vyzerá vytvorenie MCP servera pomocou bežného servera:

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

Pointa je, že explicitne pridávate každý nástroj, zdroj alebo prompt, ktorý chcete, aby server obsahoval. Na tom nie je nič zlé.  

### Prístup nízkoúrovňového servera

Keď však použijete prístup nízkoúrovňového servera, musíte premýšľať inak, konkrétne namiesto registrácie každého nástroja vytvoríte dva handlery pre každý typ funkcie (nástroje, zdroje alebo prompty). Napríklad pre nástroje existujú iba dve funkcie, ako je uvedené nižšie:

- Zoznam všetkých nástrojov. Jedna funkcia bude zodpovedná za všetky pokusy o zoznam nástrojov.
- Spracovanie volania všetkých nástrojov. Aj tu existuje iba jedna funkcia, ktorá spracováva volania nástroja.

To znie ako potenciálne menej práce, však? Namiesto registrácie nástroja stačí zabezpečiť, aby bol nástroj uvedený v zozname všetkých nástrojov a aby bol zavolaný, keď príde požiadavka na jeho použitie.

Pozrime sa, ako teraz vyzerá kód:

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

Tu máme funkciu, ktorá vracia zoznam funkcií. Každý záznam v zozname nástrojov má teraz polia ako `name`, `description` a `inputSchema`, aby vyhovoval návratovému typu. To nám umožňuje umiestniť definíciu nástrojov a funkcií inde. Teraz môžeme vytvoriť všetky naše nástroje v priečinku tools a to isté platí pre všetky vaše funkcie, takže váš projekt môže byť zrazu organizovaný takto:

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

To je skvelé, naša architektúra môže byť veľmi čistá.

A čo volanie nástrojov, je to rovnaký princíp, jeden handler na volanie nástroja, nech je to akýkoľvek nástroj? Áno, presne tak, tu je kód na to:

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

Ako vidíte z vyššie uvedeného kódu, musíme analyzovať, ktorý nástroj zavolať, s akými argumentmi, a potom pokračovať v jeho volaní.

## Zlepšenie prístupu pomocou validácie

Doteraz ste videli, ako všetky vaše registrácie na pridanie nástrojov, zdrojov a promptov môžu byť nahradené týmito dvoma handlermi pre každý typ funkcie. Čo ešte musíme urobiť? Mali by sme pridať nejakú formu validácie, aby sme zabezpečili, že nástroj je volaný so správnymi argumentmi. Každé runtime má svoje vlastné riešenie na toto, napríklad Python používa Pydantic a TypeScript používa Zod. Myšlienka je nasledovná:

- Presunúť logiku vytvárania funkcie (nástroja, zdroja alebo promptu) do jej dedikovaného priečinka.
- Pridať spôsob validácie prichádzajúcej požiadavky, napríklad na volanie nástroja.

### Vytvorenie funkcie

Na vytvorenie funkcie budeme potrebovať vytvoriť súbor pre túto funkciu a zabezpečiť, aby obsahoval povinné polia požadované pre túto funkciu. Tieto polia sa líšia medzi nástrojmi, zdrojmi a promptmi.

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

Tu môžete vidieť, ako robíme nasledovné:

- Vytvoríme schému pomocou Pydantic `AddInputModel` s poliami `a` a `b` v súbore *schema.py*.
- Pokúsime sa analyzovať prichádzajúcu požiadavku, aby bola typu `AddInputModel`. Ak sa parametre nezhodujú, dôjde k chybe:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Môžete si vybrať, či túto logiku analýzy umiestnite priamo do volania nástroja alebo do funkcie handlera.

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

- V handleri, ktorý spracováva všetky volania nástrojov, sa teraz pokúšame analyzovať prichádzajúcu požiadavku do definovanej schémy nástroja:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Ak to funguje, pokračujeme v volaní samotného nástroja:

    ```typescript
    const result = await tool.callback(input);
    ```

Ako vidíte, tento prístup vytvára skvelú architektúru, kde má všetko svoje miesto. Súbor *server.ts* je veľmi malý a slúži len na prepojenie handlerov požiadaviek, pričom každá funkcia je v príslušnom priečinku, napríklad tools/, resources/ alebo prompts/.

Skvelé, poďme to skúsiť postaviť ďalej.

## Cvičenie: Vytvorenie nízkoúrovňového servera

V tomto cvičení urobíme nasledovné:

1. Vytvoríme nízkoúrovňový server, ktorý spracováva zoznam nástrojov a ich volanie.
1. Implementujeme architektúru, na ktorej môžete stavať.
1. Pridáme validáciu, aby sme zabezpečili správnu validáciu volaní nástrojov.

### -1- Vytvorenie architektúry

Prvá vec, ktorú musíme riešiť, je architektúra, ktorá nám pomôže škálovať, keď pridáme viac funkcií. Takto to vyzerá:

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

Teraz máme nastavenú architektúru, ktorá zabezpečuje, že môžeme ľahko pridávať nové nástroje do priečinka tools. Môžete podľa toho pridať podpriečinky pre resources a prompts.

### -2- Vytvorenie nástroja

Pozrime sa, ako vyzerá vytvorenie nástroja. Najprv ho musíme vytvoriť v jeho podpriečinku *tool*, ako je uvedené nižšie:

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

Tu vidíme, ako definujeme názov, popis, vstupnú schému pomocou Pydantic a handler, ktorý bude vyvolaný, keď bude tento nástroj volaný. Nakoniec vystavujeme `tool_add`, čo je slovník obsahujúci všetky tieto vlastnosti.

Existuje tiež *schema.py*, ktorý sa používa na definovanie vstupnej schémy použitej naším nástrojom:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Musíme tiež naplniť *__init__.py*, aby sa priečinok tools považoval za modul. Okrem toho musíme vystaviť moduly v rámci neho, ako je uvedené nižšie:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Tento súbor môžeme ďalej rozširovať, keď pridáme viac nástrojov.

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

Tu vytvárame slovník pozostávajúci z vlastností:

- name, čo je názov nástroja.
- rawSchema, čo je Zod schéma, ktorá bude použitá na validáciu prichádzajúcich požiadaviek na volanie tohto nástroja.
- inputSchema, táto schéma bude použitá handlerom.
- callback, ktorý sa používa na vyvolanie nástroja.

Existuje tiež `Tool`, ktorý sa používa na konverziu tohto slovníka na typ, ktorý môže handler MCP servera akceptovať, a vyzerá takto:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

A existuje *schema.ts*, kde uchovávame vstupné schémy pre každý nástroj. Vyzerá to takto, pričom momentálne obsahuje iba jednu schému, ale ako pridáme nástroje, môžeme pridať viac záznamov:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Skvelé, poďme ďalej spracovať zoznam našich nástrojov.

### -3- Spracovanie zoznamu nástrojov

Ďalej, na spracovanie zoznamu nástrojov, musíme nastaviť handler požiadaviek na to. Tu je, čo musíme pridať do nášho serverového súboru:

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

Tu pridávame dekorátor `@server.list_tools` a implementačnú funkciu `handle_list_tools`. V tejto funkcii musíme vytvoriť zoznam nástrojov. Všimnite si, že každý nástroj musí mať názov, popis a inputSchema.   

**TypeScript**

Na nastavenie handlera požiadaviek na zoznam nástrojov musíme zavolať `setRequestHandler` na serveri so schémou, ktorá zodpovedá tomu, čo sa snažíme urobiť, v tomto prípade `ListToolsRequestSchema`. 

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

Skvelé, teraz sme vyriešili časť zoznamu nástrojov, pozrime sa, ako by sme mohli volať nástroje ďalej.

### -4- Spracovanie volania nástroja

Na volanie nástroja musíme nastaviť ďalší handler požiadaviek, tentokrát zameraný na spracovanie požiadavky špecifikujúcej, ktorú funkciu zavolať a s akými argumentmi.

**Python**

Použime dekorátor `@server.call_tool` a implementujme ho funkciou ako `handle_call_tool`. V rámci tejto funkcie musíme analyzovať názov nástroja, jeho argumenty a zabezpečiť, aby argumenty boli platné pre daný nástroj. Argumenty môžeme validovať buď v tejto funkcii, alebo downstream v samotnom nástroji.

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

Tu sa deje nasledovné:

- Názov nástroja je už prítomný ako vstupný parameter `name`, čo platí aj pre argumenty vo forme slovníka `arguments`.

- Nástroj je volaný pomocou `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validácia argumentov sa deje vo vlastnosti `handler`, ktorá odkazuje na funkciu. Ak zlyhá, vyvolá výnimku. 

Tak, teraz máme úplné pochopenie zoznamu a volania nástrojov pomocou nízkoúrovňového servera.

Pozrite si [úplný príklad](./code/README.md) tu.

## Zadanie

Rozšírte kód, ktorý ste dostali, o množstvo nástrojov, zdrojov a promptov a zamyslite sa nad tým, ako si všimnete, že stačí pridávať súbory do priečinka tools a nikam inam. 

*Riešenie nie je uvedené*

## Zhrnutie

V tejto kapitole sme videli, ako funguje prístup nízkoúrovňového servera a ako nám môže pomôcť vytvoriť peknú architektúru, na ktorej môžeme ďalej stavať. Diskutovali sme tiež o validácii a ukázali sme vám, ako pracovať s validačnými knižnicami na vytváranie schém pre validáciu vstupov.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.