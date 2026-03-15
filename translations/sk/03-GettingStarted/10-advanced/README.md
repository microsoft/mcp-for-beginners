# Pokročilé používanie servera

V MCP SDK sú vystavené dva rôzne typy serverov, váš bežný server a nízkoúrovňový server. Zvyčajne by ste použili bežný server na pridávanie funkcií. V niektorých prípadoch však chcete spoľahnúť sa na nízkoúrovňový server, napríklad:

- Lepšia architektúra. Je možné vytvoriť čistú architektúru s bežným serverom aj nízkoúrovňovým serverom, ale možno tvrdiť, že je to mierne jednoduchšie s nízkoúrovňovým serverom.
- Dostupnosť funkcií. Niektoré pokročilé funkcie je možné použiť iba s nízkoúrovňovým serverom. Uvidíte to v ďalších kapitolách, keď pridáme sampling a elicitation.

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

Podstata je v tom, že explicitne pridávate každý nástroj, zdroj alebo prompt, ktorý chcete, aby server mal. Na tom nie je nič zlé.

### Prístup nízkoúrovňového servera

Ak však používate prístup nízkoúrovňového servera, musíte o tom premýšľať inak. Namiesto registrácie každého nástroja vytvoríte dva handlery na každý typ funkcie (nástroje, zdroje alebo prompty). Napríklad nástroje majú iba dve funkcie takto:

- Výpis všetkých nástrojov. Jedna funkcia bude zodpovedná za všetky pokusy o výpis nástrojov.
- Spracovanie volania všetkých nástrojov. Tu je tiež len jedna funkcia, ktorá sa stará o volania nástrojov.

Znie to ako potenciálne menej práce, však? Takže namiesto registrácie nástroja stačí len zabezpečiť, aby bol nástroj uvedený pri výpise všetkých nástrojov a aby sa volal, keď je prichádzajúci požiadavok na volanie nástroja.

Pozrime sa na to, ako teraz vyzerá kód:

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

Tu máme funkciu, ktorá vracia zoznam funkcií. Každý záznam v zozname nástrojov má teraz polia ako `name`, `description` a `inputSchema`, aby zodpovedal návratovému typu. To nám umožňuje umiestniť definície nástrojov a funkcií inde. Môžeme teraz vytvoriť všetky nástroje v priečinku tools a to isté platí pre všetky vaše funkcie, takže váš projekt môže byť organizovaný takto:

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

To je skvelé, naša architektúra môže vyzerať veľmi čisto.

Čo volanie nástrojov, je to rovnaká myšlienka, jeden handler na volanie nástroja, bez ohľadu na to, ktorý nástroj? Áno, presne tak, tu je kód pre to:

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

Ako vidíte z vyššie uvedeného kódu, musíme rozparsovať, ktorý nástroj volať a s akými argumentmi, a potom pokračujeme volaním nástroja.

## Vylepšenie prístupu overovaním

Doteraz ste videli, ako všetky registrácie na pridávanie nástrojov, zdrojov a promptov môžu byť nahradené týmito dvoma handlerami na každý typ funkcie. Čo ešte potrebujeme? Mali by sme pridať nejakú formu overenia, aby sme zabezpečili, že nástroj sa volá so správnymi argumentmi. Každé runtime má svoje riešenie, napríklad Python používa Pydantic a TypeScript používa Zod. Myšlienka je nasledovná:

- Presunúť logiku na vytvorenie funkcie (nástroja, zdroja alebo promptu) do jej vyhradenej zložky.
- Pridať spôsob validácie prichádzajúceho požiadavku, ktorý napríklad žiada o volanie nástroja.

### Vytvorenie funkcie

Na vytvorenie funkcie potrebujeme vytvoriť súbor pre túto funkciu a zabezpečiť, aby obsahoval povinné polia požadované pre túto funkciu. Ktoré polia sa mierne líšia medzi nástrojmi, zdrojmi a promptmi.

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
- Pokúsime sa rozparsovať prichádzajúci požiadavok na typ `AddInputModel`, ak sú parametre nezhodné, dôjde k chybe:

   ```python
   # add.py
    try:
        # Overiť vstup pomocou modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Môžete sa rozhodnúť, či túto logiku parsovania umiestnite priamo do volania nástroja alebo do handler funkcie.

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

// pridaj.ts
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

- V handleji, ktorý spracováva všetky volania nástrojov, sa teraz snažíme rozparsovať prichádzajúci požiadavok podľa definovanej schémy nástroja:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ak to funguje, pokračujeme s volaním samotného nástroja:

    ```typescript
    const result = await tool.callback(input);
    ```

Ako vidíte, tento prístup vytvára skvelú architektúru, pretože všetko má svoje miesto, *server.ts* je veľmi malý súbor, ktorý len prepája handlery požiadaviek a každá funkcia je vo svojom príslušnom priečinku, t.j. tools/, resources/ alebo /prompts.

Skvelé, teraz sa pokúsime toto zostrojiť.

## Cvičenie: Vytvorenie nízkoúrovňového servera

V tomto cvičení urobíme nasledovné:

1. Vytvoríme nízkoúrovňový server, ktorý spracuje výpis nástrojov a volania nástrojov.
2. Implementujeme architektúru, na ktorú môžete stavať.
3. Pridáme validáciu, aby sa zabezpečilo, že volania nástrojov sú správne validované.

### -1- Vytvorenie architektúry

Prvou vecou, ktorú musíme riešiť, je architektúra, ktorá nám pomôže škálovať, keď pridáme viac funkcií, vyzerá takto:

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

Teraz sme nastavili architektúru, ktorá zabezpečuje, že môžeme ľahko pridávať nové nástroje do priečinka tools. Kľudne pokračujte a pridajte podadresáre pre zdroje a prompty.

### -2- Vytvorenie nástroja

Pozrime sa, ako vyzerá vytvorenie nástroja. Najprv musí byť vytvorený vo svojom podadresári *tool* takto:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Overte vstup pomocou modelu Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: pridajte Pydantic, aby sme mohli vytvoriť AddInputModel a overiť argumenty

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Vidíme tu definíciu názvu, popisu a vstupnej schémy pomocou Pydantic a handler, ktorý sa zavolá, keď je tento nástroj volaný. Nakoniec exponujeme `tool_add`, čo je slovník obsahujúci všetky tieto vlastnosti.

Máme aj *schema.py*, ktorý definuje vstupnú schému používanú naším nástrojom:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Tiež potrebujeme doplniť *__init__.py*, aby sa adresár nástrojov považoval za modul. Navyše musíme exponovať moduly v ňom takto:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Do tohto súboru môžeme pridávať ďalšie nástroje podľa potreby.

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

- name, názov nástroja.
- rawSchema, toto je Zod schéma, ktorá sa bude používať na validáciu prichádzajúcich požiadaviek na volanie tohto nástroja.
- inputSchema, táto schéma bude použitá handlerom.
- callback, používa sa na vyvolanie nástroja.

Existuje tiež `Tool`, ktorý konvertuje tento slovník na typ, ktorý môže prijať handler mcp servera, vyzerá takto:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

A máme *schema.ts*, kde uchovávame vstupné schémy pre každý nástroj, vyzerá to takto teraz iba s jednou schémou, ale s pridaním ďalších nástrojov môžeme pridávať ďalšie položky:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Skvelé, pokračujme teraz s handlerom na výpis nástrojov.

### -3- Handler na výpis nástrojov

Ďalej na spracovanie výpisu nástrojov potrebujeme nastaviť handler požiadavku na to. Tu je, čo potrebujeme pridať do nášho serverového súboru:

**Python**

```python
# kód vynechaný kvôli stručnosti
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

Tu pridávame dekorátor `@server.list_tools` a implementujeme funkciu `handle_list_tools`. V nej musíme vytvoriť zoznam nástrojov. Všímajte si, že každý nástroj musí mať meno, popis a inputSchema.

**TypeScript**

Na nastavenie handlera požiadavku na výpis nástrojov voláme `setRequestHandler` na serveri so schémou zodpovedajúcou tomu, čo chceme robiť, v tomto prípade `ListToolsRequestSchema`.

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
// kód vynechaný zo stručnosti
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Vrátiť zoznam registrovaných nástrojov
  return {
    tools: tools
  };
});
```

Skvelé, vyriešili sme časť výpisu nástrojov, pozrime sa, ako môžeme volať nástroje.

### -4- Handler na volanie nástroja

Na volanie nástroja potrebujeme nastaviť ďalší handler požiadavku, tentokrát zameraný na spracovanie požiadavku špecifikujúceho, ktorý feature volať a s akými argumentmi.

**Python**

Použijeme dekorátor `@server.call_tool` a implementujeme ho pomocou funkcie ako `handle_call_tool`. V tejto funkcii musíme rozparsovať názov nástroja, jeho argument a zabezpečiť, aby argumenty boli platné pre daný nástroj. Môžeme validovať argumenty buď tu alebo neskôr v samotnom nástroji.

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

- Názov nástroja je už prítomný ako vstupný parameter `name` a argumenty v podobe slovníka `arguments`.

- Nástroj sa volá pomocou `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validácia argumentov prebieha v `handler` vlastnosti, ktorá ukazuje na funkciu, ak zlyhá, vyvolá výnimku.

Takto máme kompletný prehľad o výpise a volaní nástrojov pomocou nízkoúrovňového servera.

Pozrite si [kompletný príklad](./code/README.md) tu

## Zadanie

Rozšírte kód, ktorý ste dostali, o niekoľko nástrojov, zdrojov a promptov a zamyslite sa nad tým, že potrebujete pridávať súbory iba do priečinka tools a nikde inde.

*Riešenie nie je poskytnuté*

## Zhrnutie

V tejto kapitole sme videli, ako funguje prístup nízkoúrovňového servera a ako nám môže pomôcť vytvoriť peknú architektúru, na ktorú môžeme ďalej stavať. Diskutovali sme tiež o validácii a ukázalo sa, ako pracovať s knižnicami na validáciu na tvorbu schém pre vstupné overovanie.

## Čo ďalej

- Ďalšie: [Jednoduchá autentifikácia](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, vezmite prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->