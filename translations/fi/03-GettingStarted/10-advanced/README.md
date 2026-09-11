# Edistynyt palvelimen käyttö

MCP SDK:ssa on kaksi erilaista palvelintyyppiä, tavallinen palvelin ja matalan tason palvelin. Tavallisesti käytät tavallista palvelinta ominaisuuksien lisäämiseen. Joissakin tapauksissa haluat kuitenkin luottaa matalan tason palvelimeen, kuten:

- Parempi arkkitehtuuri. On mahdollista luoda puhdas arkkitehtuuri sekä tavallisella että matalan tason palvelimella, mutta voidaan väittää, että se on hieman helpompaa matalan tason palvelimella.
- Ominaisuuksien saatavuus. Jotkin edistyneet ominaisuudet ovat käytettävissä vain
    matalan tason palvelimen kanssa. Myöhemmissä luvuissa käsitellään Elicitationia ja vanhentunutta Sampling-ominaisuutta,
    joka on poistettu käytöstä MCP `2026-07-28` jälkeen.

## Tavallinen palvelin vs matalan tason palvelin

Näin MCP-palvelimen luominen tavallisella palvelimella näyttää:

**Python**

```python
mcp = FastMCP("Demo")

# Lisää lisäystyökalu
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

// Lisää lisäystyökalu
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

Ajatus on, että lisäät selkeästi jokaisen työkalun, resurssin tai kehotteen, jonka haluat palvelimen sisältävän. Siinä ei ole mitään vikaa.  

### Matalan tason palvelimen tapa

Käytettäessä matalan tason palvelimen lähestymistapaa sinun on ajateltava asia eri tavalla. Sen sijaan, että rekisteröisit jokaisen työkalun erikseen, luot vain kaksi käsittelijää per ominaisuustyyppi (työkalut, resurssit tai kehotteet). Esimerkiksi työkaluilla on vain kaksi funktiota seuraavasti:

- Luettelo kaikkien työkalujen listaamiseen. Yksi funktio vastaa kaikkien työkalujen listaamisen yrityksistä.
- Työkalujen kutsujen käsittely. Tässäkin on vain yksi funktio, joka käsittelee kutsut työkaluun.

Kuulostaa potentiaalisesti vähemmän työtä vaativalta, eikö? Joten rekisteröinnin sijaan minun tarvitsee vain varmistaa, että työkalu listataan, kun listaan kaikki työkalut, ja että sitä kutsutaan, kun tulee pyyntö kutsua työkalua.

Katsotaanpa, miltä koodi nyt näyttää:

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
  // Palauta rekisteröityjen työkalujen lista
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

Täällä meillä on funktio, joka palauttaa ominaisuuksien listan. Jokaisella työkalun listan kohdalla on nyt kentät kuten `name`, `description` ja `inputSchema` vastaamaan paluuarvotyypin vaatimuksia. Tämä mahdollistaa työkalujen ja ominaisuusmääritelmien sijoittamisen muualle. Voimme nyt luoda kaikki työkalut työkalukansioon, ja sama pätee kaikkiin ominaisuuksiin, jolloin projektisi voi olla järjestetty näin:

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

Se on hienoa, arkkitehtuurimme voi näyttää melko siistiltä.

Entä työkalujen kutsuminen, onko se siis sama idea, yksi käsittelijä kutsuu mitä tahansa työkalua? Kyllä, juuri niin, tässä on koodi siihen:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools on sanakirja, jonka avaimina ovat työkalujen nimet
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
    // TODO kutsu työkalua,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Kuten yllä olevasta koodista näkyy, meidän täytyy purkaa kutsuttava työkalu ja sen argumentit ja sitten jatkaa työkalun kutsumista.

## Lähestymistavan parantaminen validaatiolla

Tähän asti olet nähnyt, miten kaikkien työkalujen, resurssien ja kehotteiden rekisteröintisi voidaan korvata näillä kahdella käsittelijällä per ominaisuustyyppi. Mitä muuta meidän pitää tehdä? No, meidän pitäisi lisätä jonkinlainen validointi varmistaaksemme, että työkalu kutsutaan oikeilla argumenteilla. Jokaisella ajon aikana käytettävällä ympäristöllä on oma ratkaisunsa tähän, esimerkiksi Python käyttää Pydanticia ja TypeScript käyttää Zodia. Idea on, että teemme seuraavaa:

- Siirrämme ominaisuuden (työkalu, resurssi tai kehotteen) luontilogiikan omaan kansioonsa.
- Lisätään tapa validoida saapuva pyyntö, joka esimerkiksi pyytää kutsumaan työkalua.

### Ominaisuuden luominen

Luoaksesi ominaisuuden sinun täytyy luoda kyseiselle ominaisuudelle tiedosto ja varmistaa, että siinä on pakolliset kentät, joita ominaisuus vaatii. Kentät poikkeavat hieman työkalujen, resurssien ja kehotteiden välillä.

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
        # Vahvista syöte Pydantic-mallin avulla
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: lisää Pydantic, jotta voimme luoda AddInputModelin ja vahvistaa argumentit

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Tässä näet, miten teemme seuraavaa:

- Luomme skeeman käyttäen Pydanticin `AddInputModel`-mallia, jossa on kentät `a` ja `b` tiedostossa *schema.py*.
- Yritämme purkaa saapuvan pyynnön tyypiksi `AddInputModel`, jos parametrit eivät täsmää, tämä aiheuttaa virheen:

   ```python
   # add.py
    try:
        # Vahvista syöte Pydantic-mallin avulla
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Voit valita, laitatko tämän purkamislogiikan itse työkalun kutsuun vai käsittelijäfunktioon.

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

- Työkaluja käsittelevässä kutsuissa käytettävässä käsittelijässä yritämme nyt purkaa saapuvan pyynnön työkalun määrittelemän skeeman mukaiseksi:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Jos se onnistuu, jatkamme varsinaista työkalun kutsua:

    ```typescript
    const result = await tool.callback(input);
    ```

Kuten näet, tämä lähestymistapa luo hyvän arkkitehtuurin, koska kaikella on paikkansa. *server.ts* on hyvin pieni tiedosto, joka yhdistää vain pyyntökäsittelijät, ja jokainen ominaisuus on omassa kansiossaan, kuten tools/, resources/ tai /prompts.

Hienoa, kokeillaanpa seuraavaksi rakentaa tätä.

## Harjoitus: Matalan tason palvelimen luominen

Tässä harjoituksessa teemme seuraavaa:

1. Luo matalan tason palvelin, joka käsittelee työkalujen listauksen ja kutsun.
1. Toteuta arkkitehtuuri, johon voit rakentaa.
1. Lisää validointi varmistaaksesi, että työkalukutsut validoidaan oikein.

### -1- Arkkitehtuurin luominen

Ensimmäinen asia, joka meidän täytyy hoitaa, on arkkitehtuuri, joka auttaa meitä laajentamaan ominaisuuksia lisäämällä. Näin se näyttää:

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

Nyt olemme perustaneet arkkitehtuurin, joka mahdollistaa uusien työkalujen helpon lisäämisen tools-kansiossa. Voit myös halutessasi lisätä alikansioita resources- ja prompts-kansioille.

### -2- Työkalun luominen

Katsotaan, miltä työkalun luominen näyttää. Ensin sen täytyy luoda *tool*-alikansioon näin:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Vahvista syöte Pydantic-mallin avulla
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: lisää Pydantic, jotta voimme luoda AddInputModelin ja vahvistaa argumentit

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Tässä näemme, miten määrittelemme nimen, kuvauksen ja syötteen skeeman käyttäen Pydanticia sekä käsittelijän, joka kutsutaan, kun tätä työkalua käytetään. Lopuksi paljastamme `tool_add`, joka on sanakirja, joka pitää sisällään nämä ominaisuudet.

On myös *schema.py*, jota käytetään määrittelemään työkalun käyttämä syötteen skeema:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Meidän täytyy myös täyttää *__init__.py* varmistaaksemme, että työkalukansio käsitellään moduulina. Lisäksi meidän täytyy paljastaa sen moduulit näin:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Voimme jatkaa tämän tiedoston laajentamista, kun lisäämme työkaluja.

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

Tässä luomme sanakirjan, joka sisältää ominaisuuksia:

- name, tämä on työkalun nimi.
- rawSchema, tämä on Zod-skeema, jota käytetään validoimaan sisään tulevat työkalukutsut.
- inputSchema, tätä skeemaa käyttää käsittelijä.
- callback, tätä käytetään kutsumaan työkalua.

On myös `Tool`, jota käytetään muuttamaan tämä sanakirja tyyppiin, jonka mcp-palvelimen käsittelijä hyväksyy, ja se näyttää tältä:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Lisäksi on *schema.ts*, jossa säilytämme syötteen skeemoja jokaiselle työkalulle, ja se näyttää tältä tällä hetkellä yhdellä skeemalla, mutta kun lisäämme työkaluja, voimme lisätä lisää:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Hienoa, jatketaan työkalujen listauksen käsittelyllä seuraavaksi.

### -3- Työkalulistan käsittely

Seuraavaksi työkalujen listauksen käsittelemiseksi meidän täytyy määrittää siihen pyyntökäsittelijä. Tässä mitä meidän täytyy lisätä palvelintiedostoon:

**Python**

```python
# koodi jätetty pois lyhyyden vuoksi
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

Tässä lisäämme koristeen `@server.list_tools` ja toteuttavan funktion `handle_list_tools`. Tässä funktion sisällä meidän täytyy tuottaa työkalulista. Huomaa, että jokaisella työkalulla täytyy olla nimi, kuvaus ja inputSchema.   

**TypeScript**

Pyyntökäsittelijän asettamiseksi työkalujen listaukseen meidän täytyy kutsua `setRequestHandler` palvelimella käyttäen skeemaa, joka sopii siihen, mitä yritämme tehdä, tässä tapauksessa `ListToolsRequestSchema`. 

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
// koodi jätetty pois tiiviyden vuoksi
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Palauta rekisteröityjen työkalujen lista
  return {
    tools: tools
  };
});
```

Hienoa, nyt kun olemme ratkaisseet työkalujen listauksen osan, katsotaan miten voisimme kutsua työkaluja seuraavaksi.

### -4- Työkalun kutsun käsittely

Työkalun kutsumiseksi meidän täytyy määritellä toinen pyyntökäsittelijä, joka keskittyy pyynnön käsittelyyn, joka määrittää, mitä ominaisuutta kutsutaan ja millä argumenteilla.

**Python**

Käytetään koristetta `@server.call_tool` ja toteutetaan se funktiolla kuten `handle_call_tool`. Tämän funktion sisällä meidän täytyy purkaa työkalun nimi, sen argumentti ja varmistaa, että argumentit ovat valideja kyseiselle työkalulle. Voimme validoida argumentit tässä funktiossa tai myöhemmin varsinaisessa työkalussa.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools on sanakirja, jossa työkalujen nimet ovat avaimina
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # kutsu työkalua
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Tässä tapahtuu seuraavaa:

- Työkalun nimi on jo läsnä syötteenä parametrina `name` ja argumentit sanakirjana `arguments`.

- Työkalu kutsutaan lausekkeella `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Argumenttien validointi tapahtuu `handler`-ominaisuudessa, joka viittaa funktioon; jos se epäonnistuu, se nostaa poikkeuksen.

Nyt meillä on täysi käsitys työkalujen listaamisesta ja kutsumisesta matalan tason palvelinta käyttäen.

Katso [täydellinen esimerkki](./code/README.md) täältä

## Tehtävä

Laajenna saamasi koodi useilla työkaluilla, resursseilla ja kehotteilla ja pohdi, miten huomaat, että sinun tarvitsee lisätä tiedostoja vain tools-kansioon etkä minnekään muualle.

*Ratkaisua ei anneta*

## Yhteenveto

Tässä luvussa näimme, miten matalan tason palvelimen lähestymistapa toimi ja miten se auttaa meitä luomaan siistin arkkitehtuurin, jonka päälle voimme rakentaa. Keskustelimme myös validoinnista ja sinulle näytettiin, miten validointikirjastoilla luodaan skeemoja syötteen validointiin.

## Mitä seuraavaksi

- Seuraavaksi: [Yksinkertainen todennus](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->