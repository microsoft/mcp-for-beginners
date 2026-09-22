# Pokročilé používanie servera

V MCP SDK sú vystavené dva rôzne typy serverov, váš bežný server a nízkoúrovňový server. Zvyčajne by ste použili bežný server na pridávanie funkcií. V niektorých prípadoch však chcete spoľahnúť na nízkoúrovňový server, napríklad:

- Lepšia architektúra. Je možné vytvoriť čistú architektúru s bežným serverom aj nízkoúrovňovým serverom, ale dá sa argumentovať, že je to o niečo jednoduchšie s nízkoúrovňovým serverom.
- Dostupnosť funkcií. Niektoré pokročilé funkcie je možné použiť iba s
    nízkoúrovňovým serverom. Neskoršie kapitoly pokrývajú Elicitation a starú funkciu Sampling,
    ktorá je v MCP `2026-07-28` zastaraná.

## Bežný server vs nízkoúrovňový server

Takto vyzerá vytvorenie MCP servera s bežným serverom

**Python**

```python
mcp = FastMCP("Demo")

# Pridajte nástroj na sčítanie
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

// Pridať nástroj na sčítanie
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

Pointa je, že explicitne pridávate každý nástroj, zdroj alebo prompt, ktorý chcete, aby server mal. Nie je na tom nič zlé.  

### Prístup nízkoúrovňového servera

Ak však použijete prístup nízkoúrovňového servera, musíte na to myslieť inak. Namiesto registrácie každého nástroja vytvoríte dva handlery pre každý typ funkcie (nástroje, zdroje alebo prompty). Napríklad nástroje potom majú iba dve funkcie takto:

- Výpis všetkých nástrojov. Jedna funkcia bude zodpovedná za všetky pokusy o výpis nástrojov.
- Spracovanie volania všetkých nástrojov. Taktiež tu je len jedna funkcia, ktorá spracováva volania nástroja.

Znie to ako potenciálne menej práce, však? Takže namiesto registrácie nástroja len musím zabezpečiť, aby bol nástroj uvedený pri výpise všetkých nástrojov a aby bol zavolaný, keď príde požiadavka na volanie nástroja.

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
  // Vrátiť zoznam registrovaných nástrojov
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

Tu máme funkciu, ktorá vracia zoznam funkcií. Každá položka v zozname nástrojov má teraz polia ako `name`, `description` a `inputSchema`, aby zodpovedala návratovému typu. To nám umožňuje umiestniť definíciu nástrojov a funkcií inde. Teraz môžeme vytvoriť všetky naše nástroje v priečinku tools a to isté platí pre všetky vaše funkcie, takže váš projekt môže byť náhle usporiadaný takto:

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

To je skvelé, naša architektúra môže byť pekne čistá.

A čo volanie nástrojov, je to potom rovnaký princíp, jeden handler na volanie nástroja, ktorýkoľvek nástroj? Áno, presne tak, tu je kód na to:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools je slovník s názvami nástrojov ako kľúče
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

Ako vidíte z vyššie uvedeného kódu, musíme vyparsovať, ktorý nástroj volať a s akými argumentmi, a potom pokračovať v volaní nástroja.

## Zlepšenie prístupu validáciou

Doteraz ste videli, ako je možné nahradiť všetky vaše registrácie na pridanie nástrojov, zdrojov a promptov týmito dvoma handlermi pre každý typ funkcie. Čo ešte musíme urobiť? No, mali by sme pridať nejakú formu validácie, aby sme zabezpečili, že nástroj je volaný so správnymi argumentmi. Každé runtime má na to vlastné riešenie, napríklad Python používa Pydantic a TypeScript používa Zod. Myšlienka je, že spravíme nasledovné:

- Presunúť logiku pre vytváranie funkcie (nástroja, zdroja alebo promptu) do jej vyhradenej zložky.
- Pridať spôsob validácie prichádzajúcej požiadavky žiadajúcej napríklad o volanie nástroja.

### Vytvorenie funkcie

Na vytvorenie funkcie budeme potrebovať vytvoriť pre ňu súbor a zabezpečiť, že obsahuje povinné polia potrebné pre túto funkciu. Ktoré polia sa trochu líšia medzi nástrojmi, zdrojmi a promptmi.

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
        # Overiť vstup pomocou modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: pridať Pydantic, aby sme mohli vytvoriť AddInputModel a overiť argumenty

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

- Vytvoríme schému pomocou Pydantic `AddInputModel` s poľami `a` a `b` v súbore *schema.py*.
- Pokúsime sa vyparsovať prichádzajúcu požiadavku na typ `AddInputModel`, ak sú parametre nezhodné, spôsobí to pád aplikácie:

   ```python
   # add.py
    try:
        # Overiť vstup pomocou Pydantic modelu
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Môžete si zvoliť, či túto logiku parsovania umiestnite priamo do volania nástroja alebo do handler funkcie.

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

- V handleri, ktorý spracováva všetky volania nástrojov, teraz skúšame vyparsovať prichádzajúcu požiadavku na schému definovanú nástrojom:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ak to prejde, pokračujeme vo volaní samotného nástroja:

    ```typescript
    const result = await tool.callback(input);
    ```

Ako vidíte, tento prístup vytvára skvelú architektúru, pretože všetko má svoje miesto, *server.ts* je veľmi malý súbor, ktorý iba spája tieto handlery požiadaviek a každý feature je vo svojej vlastnej zložke, teda tools/, resources/ alebo /prompts.

Skvelé, poďme sa teraz pokúsiť toto postaviť. 

## Cvičenie: Vytvorenie nízkoúrovňového servera

V tomto cvičení urobíme nasledovné:

1. Vytvoríme nízkoúrovňový server, ktorý spracuje výpis nástrojov a volanie nástrojov.
1. Implementujeme architektúru, na ktorej môžete stavať.
1. Pridáme validáciu, aby sme zabezpečili správnu validáciu vašich volaní nástrojov.

### -1- Vytvorenie architektúry

Najprv potrebujeme riešiť architektúru, ktorá nám pomôže škálovať sa s pridaním ďalších funkcií, vyzerá to takto:

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

Teraz sme nastavili architektúru, ktorá zabezpečuje jednoduché pridávanie nových nástrojov do priečinka tools. Kľudne pridajte podpriečinky pre resources a prompts.

### -2- Vytvorenie nástroja

Pozrime sa, ako vyzerá vytváranie nástroja. Najprv ho treba vytvoriť v jeho podadresári *tool* takto:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Overte vstup pomocou modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: pridať Pydantic, aby sme mohli vytvoriť AddInputModel a overiť argumenty

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Tu vidíme, ako definujeme meno, popis a input schema pomocou Pydantic a handler, ktorý bude vyvolaný, keď bude tento nástroj volaný. Nakoniec vystavíme `tool_add`, čo je slovník obsahujúci všetky tieto vlastnosti.

Je tu aj *schema.py*, ktorý sa používa na definovanie vstupnej schémy používanú naším nástrojom:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Tiež musíme vyplniť *__init__.py*, aby bol priečinok tools považovaný za modul. Navyše musíme moduly v ňom vystaviť takto:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Do tohto súboru môžeme pridávať viac nástrojov podľa potreby.

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

- name, to je meno nástroja.
- rawSchema, to je Zod schéma, používa sa na validáciu prichádzajúcich požiadaviek na volanie tohto nástroja.
- inputSchema, túto schému používa handler.
- callback, používa sa na vyvolanie nástroja.

Je tu aj `Tool`, ktorý slúži na konverziu tohto slovníka do typu, ktorý môže prijať mcp server handler, vyzerá takto:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

A je tu *schema.ts*, kde ukladáme vstupné schémy pre každý nástroj, vyzerá takto s aktuálne len jednou schémou, ale s pridaním ďalších nástrojov môžeme pridať ďalšie položky:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Skvelé, teraz pokračujme v spracovaní výpisu našich nástrojov.

### -3- Spracovanie výpisu nástrojov

Ďalej, na spracovanie výpisu nástrojov, potrebujeme nastaviť request handler na to. Tu je, čo potrebujeme pridať do nášho serverového súboru:

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

Tu pridáme dekorátor `@server.list_tools` a implementačnú funkciu `handle_list_tools`. V nej je potrebné vygenerovať zoznam nástrojov. Všimnite si, že každý nástroj musí mať meno, popis a inputSchema.   

**TypeScript**

Na nastavenie request handlera pre výpis nástrojov musíme zavolať `setRequestHandler` na serveri so schémou zodpovedajúcou našej požiadavke, v tomto prípade `ListToolsRequestSchema`. 

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
// kód vynechaný pre stručnosť
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Vrátiť zoznam registrovaných nástrojov
  return {
    tools: tools
  };
});
```

Skvelé, teraz sme vyriešili výpis nástrojov, pozrime sa, ako by sme mohli volať nástroje.

### -4- Spracovanie volania nástroja

Na volanie nástroja potrebujeme nastaviť ďalší request handler, tentoraz zameraný na požiadavku definujúcu, ktorú funkciu volať a s akými argumentmi.

**Python**

Použime dekorátor `@server.call_tool` a implementujme ho funkciou ako `handle_call_tool`. V tejto funkcii musíme vyparsovať meno nástroja, jeho argumenty a zabezpečiť, že argumenty sú platné pre daný nástroj. Validáciu argumentov môžeme urobiť buď tu, alebo neskôr priamo v nástroji.

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

Tu je, čo sa deje:

- Názov nástroja už máme ako vstupný parameter `name`, rovnako aj argumenty v slovníku `arguments`.

- Nástroj je volaný pomocou `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validácia argumentov prebieha vo vlastnosti `handler`, ktorá odkazuje na funkciu, ak zlyhá, vyhodí výnimku. 

Takto teraz plne rozumieme výpisu a volaniu nástrojov pomocou nízkoúrovňového servera.

Pozrite si [celý príklad](./code/README.md) tu

## Zadanie

Rozšírte daný kód o niekoľko nástrojov, zdrojov a promptov a zamyslite sa nad tým, ako si všímate, že stačí pridávať súbory iba do priečinka tools a nikde inde. 

*Riešenie nie je poskytnuté*

## Zhrnutie

V tejto kapitole sme videli, ako fungoval prístup nízkoúrovňového servera a ako nám môže pomôcť vytvoriť peknú architektúru, na ktorej môžeme ďalej stavať. Diskutovali sme aj o validácii a ukázalo sa vám, ako pracovať s knižnicami validácie na vytváranie schém pre validáciu vstupov.

## Čo ďalej

- Ďalej: [Jednoduchá autentifikácia](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->