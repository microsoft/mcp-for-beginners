# Pokročilé použitie servera

V MCP SDK sú dostupné dva rôzne typy serverov, bežný server a nízkoúrovňový server. Obvykle by ste používali bežný server na pridávanie funkcií. V niektorých prípadoch však chcete spoľahnúť sa na nízkoúrovňový server, napríklad:

- Lepšia architektúra. Je možné vytvoriť čistú architektúru s bežným serverom aj nízkoúrovňovým serverom, ale dá sa argumentovať, že s nízkoúrovňovým serverom je to trochu jednoduchšie.
- Dostupnosť funkcií. Niektoré pokročilé funkcie je možné používať iba s nízkoúrovňovým serverom. Uvidíte to v ďalších kapitolách, keď pridáme sampling a elicitation.

## Bežný server vs nízkoúrovňový server

Takto vyzerá vytvorenie MCP servera s bežným serverom

**Python**

```python
mcp = FastMCP("Demo")

# Pridať nástroj na sčítanie
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

// Pridajte nástroj na sčítanie
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

Podstata je v tom, že explicitne pridáte každý nástroj, zdroj alebo prompt, ktorý chcete, aby server mal. Na tom nie je nič zlé.

### Prístup nízkoúrovňového servera

Keď používate prístup nízkoúrovňového servera, musíte na to myslieť inak. Namiesto registrácie každého nástroja jednoducho vytvoríte dva handlery na každý typ funkcie (nástroje, zdroje alebo prompty). Napríklad nástroje majú iba dve funkcie takto:

- Zoznam všetkých nástrojov. Jedna funkcia je zodpovedná za všetky pokusy o výpis nástrojov.
- Spracovanie volania všetkých nástrojov. Opäť je tu len jedna funkcia na spracovanie volaní nástroja.

To znie ako potenciálne menej práce, však? Namiesto registrácie nástroja len musím zabezpečiť, aby bol nástroj uvedený v zozname, keď vypisujem všetky nástroje, a aby sa vyvolal pri prichádzajúcej požiadavke na volanie nástroja.

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
  // Vrátiť zoznam zaregistrovaných nástrojov
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

Tu už máme funkciu, ktorá vracia zoznam funkcií. Každá položka v zozname nástrojov má polia ako `name`, `description` a `inputSchema`, aby zodpovedala návratovému typu. To nám umožňuje umiestniť naše nástroje a definíciu funkcií inde. Teraz môžeme vytvárať všetky naše nástroje v priečinku tools a to isté platí aj pre všetky vaše funkcie, takže váš projekt môže byť zrazu usporiadaný takto:

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

To je skvelé, naša architektúra môže vyzerať celkom čisto.

Čo volanie nástrojov? Platí ten istý princíp, jeden handler na volanie ľubovoľného nástroja? Áno, presne tak, tu je kód:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools je slovník s názvami nástrojov ako kľúčmi
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
    // TODO zavolať nástroj,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Ako vidíte z horeuvedeného kódu, musíme vyparsovať, ktorý nástroj volať a s akými argumentmi, a potom pokračovať v volaní nástroja.

## Vylepšenie prístupu s validáciou

Doteraz ste videli, ako všetky vaše registrácie na pridávanie nástrojov, zdrojov a promptov môžu byť nahradené týmito dvoma handlermi na každý typ funkcie. Čo ešte musíme urobiť? Mali by sme pridať nejakú formu validácie, aby sme zabezpečili, že nástroj sa volá s správnymi argumentmi. Každé runtime má svoje riešenie, napríklad Python používa Pydantic a TypeScript používa Zod. Myšlienka je nasledovná:

- Presunúť logiku vytvorenia funkcie (nástroj, zdroj alebo prompt) do jeho vyhradeného priečinka.
- Pridať spôsob, ako validovať prichádzajúcu požiadavku, ktorá napríklad požaduje volanie nástroja.

### Vytvorenie funkcie

Na vytvorenie funkcie budeme potrebovať vytvoriť súbor pre túto funkciu a zabezpečiť, aby mal povinné polia požadované pre danú funkciu. Polia sa mierne líšia medzi nástrojmi, zdrojmi a promptmi.

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
        # Validujte vstup pomocou modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: pridajte Pydantic, aby sme mohli vytvoriť AddInputModel a validovať argumenty

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Tu vidíte, ako robíme nasledovné:

- Vytvoríme schému pomocou Pydantic `AddInputModel` s poliami `a` a `b` v súbore *schema.py*.
- Pokúsime sa pomocou parse prijať prichádzajúcu požiadavku ako typ `AddInputModel`, ak nastane nezhoda v parametroch, program spadne:

   ```python
   # add.py
    try:
        # Overiť vstup pomocou modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Môžete si vybrať, či túto logiku parsovania dať priamo do samotného volania nástroja alebo do handler funkcie.

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

- V handleri, ktorý spracúva všetky volania nástrojov, teraz skúšame parse prichádzajúcu požiadavku do definovanej schémy nástroja:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Ak to funguje, pokračujeme vo volaní samotného nástroja:

    ```typescript
    const result = await tool.callback(input);
    ```

Ako vidíte, tento prístup vytvára skvelú architektúru, pretože všetko má svoje miesto, súbor *server.ts* je veľmi malý a len zapája request handlery a každá funkcia je vo svojom vlastnom priečinku, teda tools/, resources/ alebo /prompts.

Výborne, poďme to teraz skúsiť postaviť.

## Cvičenie: Vytvorenie nízkoúrovňového servera

V tomto cvičení urobíme nasledujúce:

1. Vytvoríme nízkoúrovňový server spracúvajúci výpis nástrojov a volania nástrojov.
1. Implementujeme architektúru, na ktorej môžete stavať.
1. Pridáme validáciu, aby sa zabezpečilo, že volania vašich nástrojov budú riadne validované.

### -1- Vytvorenie architektúry

Prvým problémom, ktorý musíme riešiť, je architektúra, ktorá nám pomôže škálovať, keď pridávame viac funkcií, vyzerá takto:

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

Teraz sme nastavili architektúru, ktorá nám umožňuje jednoducho pridávať nové nástroje v priečinku tools. Kľudne pridajte aj podpriečinky pre resources a prompts.

### -2- Vytvorenie nástroja

Pozrime sa, ako vyzerá vytvorenie nástroja. Najskôr ho treba vytvoriť v podpriečinku *tool* takto:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validovať vstup pomocou Pydantic modelu
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: pridať Pydantic, aby sme mohli vytvoriť AddInputModel a validovať argumenty

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Vidíme, že definujeme názov, popis a vstupnú schému pomocou Pydantic a handler, ktorý bude vyvolaný po zavolaní tohto nástroja. Nakoniec exponujeme `tool_add`, čo je slovník obsahujúci všetky tieto vlastnosti.

Je tu tiež *schema.py*, ktorý sa používa na definovanie vstupnej schémy používanej nástrojom:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Tiež musíme doplniť *__init__.py*, aby sa priečinok tools správal ako modul. Okrem toho musíme exponovať moduly v ňom takto:

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

Tu vytvárame slovník skladajúci sa z vlastností:

- name, to je názov nástroja.
- rawSchema, je to Zod schéma, ktorá sa použije na validáciu prichádzajúcich požiadaviek na volanie tohto nástroja.
- inputSchema, túto schému používa handler.
- callback, používa sa na vyvolanie nástroja.

Existuje tiež `Tool`, ktorý slúži na konverziu tohto slovníka na typ, ktorý MCP server handler dokáže prijať, vyzerá takto:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

A je tu *schema.ts*, kde uchovávame vstupné schémy pre každý nástroj, vyzerá to takto, momentálne je tam len jedna schéma, ale ako pridáme nástroje, môžeme pridávať viac položiek:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Skvelé, teraz pokračujeme v spracovaní výpisu našich nástrojov.

### -3- Spracovanie výpisu nástrojov

Na spracovanie výpisu nástrojov potrebujeme nastaviť request handler. Toto musíme pridať do nášho server súboru:

**Python**

```python
# kód vynechaný pre stručnosť
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

Tu pridáme dekorátor `@server.list_tools` a implementačnú funkciu `handle_list_tools`. V nej musíme vygenerovať zoznam nástrojov. Všimnite si, že každý nástroj musí mať názov, popis a inputSchema.

**TypeScript**

Na nastavenie request handlera na výpis nástrojov zavoláme `setRequestHandler` na serveri so schémou, ktorá zodpovedá tomu, čo chceme robiť, v tomto prípade `ListToolsRequestSchema`.

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
// kód skrátený pre stručnosť
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Vráti zoznam registrovaných nástrojov
  return {
    tools: tools
  };
});
```

Výborne, teraz sme vyriešili časť výpisu nástrojov, poďme sa pozrieť na volanie nástrojov.

### -4- Spracovanie volania nástroja

Na volanie nástroja potrebujeme nastaviť ďalší request handler, ktorý sa zameria na spracovanie požiadavky špecifikujúcej, ktorú funkciu volať a s akými argumentmi.

**Python**

Použijeme dekorátor `@server.call_tool` a implementujeme ho funkciou ako `handle_call_tool`. V tejto funkcii musíme vyparsovať názov nástroja, jeho argument a zabezpečiť, že argumenty sú platné pre daný nástroj. Validáciu argumentov môžeme urobiť buď tu alebo v samotnom nástroji.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools je slovník s názvami nástrojov ako kľúčmi
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # vyvolať nástroj
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Tu sa deje nasledovné:

- Názov nástroja je už zadaný ako vstupný parameter `name`, čo platí aj pre argumenty vo forme slovníka `arguments`.

- Nástroj sa volá pomocou `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validácia argumentov sa deje v property `handler`, ktorá ukazuje na funkciu, ak zlyhá, vyvolá výnimku.

Takže máme kompletné pochopenie výpisu a volania nástrojov pomocou nízkoúrovňového servera.

Pozrite si [plný príklad](./code/README.md) tu

## Zadanie

Rozšírte poskytnutý kód o niekoľko nástrojov, zdrojov a promptov a reflektujte, ako si všímate, že musíte pridávať súbory iba do priečinka tools a nikde inde.

*Riešenie nie je poskytnuté*

## Zhrnutie

V tejto kapitole sme videli, ako fungoval prístup nízkoúrovňového servera a ako nám môže pomôcť vytvoriť peknú architektúru, na ktorej môžeme stavať ďalej. Diskutovali sme aj o validácii a ukázali sme vám, ako pracovať s validačnými knižnicami na tvorbu schém pre validáciu vstupov.

## Čo ďalej

- Ďalej: [Jednoduchá autentifikácia](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->