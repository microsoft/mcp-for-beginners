# Edistynyt palvelimen käyttö

MCP SDK:ssa on kaksi erilaista palvelintyyppiä, tavallinen palvelin ja matalan tason palvelin. Tavallisesti käytät tavallista palvelinta lisätäksesi siihen ominaisuuksia. Joissain tapauksissa kuitenkin haluat käyttää matalan tason palvelinta, esimerkiksi:

- Parempi arkkitehtuuri. On mahdollista luoda siisti arkkitehtuuri sekä tavallisella palvelimella että matalan tason palvelimella, mutta voidaan väittää, että se on hieman helpompaa matalan tason palvelimella.
- Ominaisuuksien saatavuus. Jotkin edistyneet ominaisuudet ovat käytettävissä vain matalan tason palvelimen kanssa. Näet tämän myöhemmissä luvuissa, kun lisäämme näytteistämistä ja villintämistä.

## Tavallinen palvelin vs matalan tason palvelin

Tältä MCP-palvelimen luominen näyttää tavallisella palvelimella

**Python**

```python
mcp = FastMCP("Demo")

# Lisää yhteenlaskutyökalu
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

// Lisää yhteenlaskutyökalu
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

Ajatuksena on, että lisäät nimenomaan jokaisen työkalun, resurssin tai kehotteen, jonka haluat palvelimessa olevan. Tässä ei ole mitään vikaa.

### Matalan tason palvelimen lähestymistapa

Kuitenkin, kun käytät matalan tason palvelimen lähestymistapaa, sinun täytyy ajatella sitä eri tavalla. Sen sijaan, että rekisteröisit jokaisen työkalun, luot kaksi käsittelijää kutakin ominaisuustyyppiä (työkalut, resurssit tai kehote) varten. Esimerkiksi työkaluilla on vain kaksi toimintoa:

- Kaikkien työkalujen listaaminen. Yksi funktio huolehtii kaikista yrityksistä listata työkaluja.
- Työkalujen kutsumisen käsittely. Täälläkin on vain yksi funktio käsittelemässä työkalun kutsuja.

Kuulostaa ehkä vähemmän työtä vaativalta? Joten rekisteröinnin sijaan minun tarvitsee vain varmistaa, että työkalu listataan, kun listaan kaikki työkalut ja että sitä kutsutaan, kun tulee pyyntö kutsua työkalua.

Katsotaanpa, miltä koodi näyttää nyt:

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

Tässä meillä on nyt funktio, joka palauttaa ominaisuuksien listan. Jokaisella työkalun listan merkinnällä on nyt kenttiä, kuten `name`, `description` ja `inputSchema` vastaamaan paluuarvotyyppiä. Tämä mahdollistaa sen, että voimme sijoittaa työkalumme ja ominaisuusmäärittelymme muualle. Voimme luoda kaikki työkalumme *tools* -kansioon ja vastaavasti kaikki ominaisuutesi niin, että projektisi voi yhtäkkiä olla organisoitu näin:

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

Hienoa, arkkitehtuurimme voidaan tehdä varsin siistiksi.

Entä työkalujen kutsuminen, onko sama idea, yksi käsittelijä kutsua työkalua, mikä tahansa työkalu? Kyllä, juuri niin, tässä on koodi siihen:

**Python**

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

Kuten yllä olevasta koodista näet, meidän täytyy purkaa kutsuttava työkalu ja millä argumenteilla, ja sitten meidän täytyy jatkaa työkalun kutsumista.

## Lähestymistavan parantaminen validoinnilla

Tähän asti olet nähnyt, miten kaikki rekisteröintisi lisätäksesi työkaluja, resursseja ja kehotteita voidaan korvata näillä kahdella käsittelijällä kutakin ominaisuustyyppiä kohden. Mitä muuta meidän täytyy tehdä? No, meidän pitäisi lisätä jonkinlainen validointi varmistaaksemme, että työkalua kutsutaan oikeilla argumenteilla. Jokaisella suoritusympäristöllä on oma ratkaisunsa tähän, esimerkiksi Python käyttää Pydanticia ja TypeScript Zodia. Ajatus on, että teemme seuraavaa:

- Siirrämme logiikan ominaisuuden (työkalun, resurssin tai kehotteen) luomiseen omalle kansiolleen.
- Lisäämme tavan validoida sisään tuleva pyyntö, joka esimerkiksi pyytää työkalun kutsumista.

### Luo ominaisuus

Luodaksemme ominaisuuden, meidän täytyy luoda tiedosto kyseiselle ominaisuudelle ja varmistaa, että sillä on ominaisuudelle pakolliset kentät. Kentät eroavat hieman työkalujen, resurssien ja kehotteiden välillä.

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
        # Vahvista syöte käyttäen Pydantic-mallia
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

tässä näet, miten teemme seuraavaa:

- Luodaan skeema Pydanticilla `AddInputModel`, jossa on kentät `a` ja `b` tiedostossa *schema.py*.
- Yritetään jäsentää sisään tuleva pyyntö tyypiksi `AddInputModel`; jos parametrit eivät täsmää, tämä kaatuu:

   ```python
   # add.py
    try:
        # Vahvista syöte Pydantic-mallin avulla
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Voit valita, sijoitatko tämän jäsennyslogiikan itse työkalukutsuun vai käsittelijäfunktioon.

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

- Työkaluja käsittelevässä käsittelijässä yritämme nyt jäsentää tulevan pyynnön työkalun määritellyksi skeemaksi:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jos se onnistuu, jatkamme työkalun kutsua:

    ```typescript
    const result = await tool.callback(input);
    ```

Kuten näet, tämä lähestymistapa luo hyvän arkkitehtuurin, koska kaikella on oma paikkansa; *server.ts* on hyvin pieni tiedosto, joka vain yhdistää pyyntöjen käsittelijät, ja jokainen ominaisuus on omassa kansiossaan eli tools/, resources/ tai prompts/.

Hienoa, kokeillaan tätä seuraavaksi rakentaa.

## Harjoitus: Matalan tason palvelimen luominen

Tässä harjoituksessa teemme seuraavaa:

1. Luomme matalan tason palvelimen, joka käsittelee työkalujen listaamista ja työkalujen kutsumista.
1. Toteutamme arkkitehtuurin, jonka päälle voit rakentaa.
1. Lisäämme validoinnin varmistaaksemme, että työkalukutsusi validoidaan oikein.

### -1- Luo arkkitehtuuri

Ensimmäinen asia, johon meidän pitää puuttua, on arkkitehtuuri, joka auttaa meitä skaalaamaan sitä, kun lisäämme ominaisuuksia; tältä se näyttää:

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

Nyt olemme luoneet arkkitehtuurin, joka takaa, että voimme helposti lisätä uusia työkaluja *tools* -kansioon. Voit vapaasti seurata tätä alihakemistoja varten resursseille ja kehotteille.

### -2- Luo työkalu

Katsotaanpa, miltä työkalun luominen näyttää seuraavaksi. Ensin sen täytyy luoda *tool* alihakemistoon näin:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Vahvista syöte Pydantic-mallin avulla
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: lisää Pydantic, jotta voimme luoda AddInputModelin ja validoida argumentit

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Tässä näemme, miten määrittelemme nimen, kuvauksen ja syötteiden skeeman Pydanticilla sekä käsittelijän, joka kutsutaan, kun tätä työkalua kutsutaan. Lopuksi altistamme `tool_add`, joka on sanakirja, joka pitää sisällään nämä ominaisuudet.

On myös *schema.py*, jota käytetään määrittelemään työkalun käyttämä syöteskeema:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Meidän myös täytyy täyttää *__init__.py* varmistaaksemme, että tools-hakemisto käsitellään moduulina. Lisäksi meidän on altistettava sen moduulit näin:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Voimme lisätä tähän tiedostoon aina vain tiedostoja, kun lisäämme työkaluja.

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

Täällä luomme sanakirjan, joka koostuu seuraavista ominaisuuksista:

- name, työkaluun nimi.
- rawSchema, Zod-skeema, jota käytetään syötteen validointiin työkalun kutsun yhteydessä.
- inputSchema, tätä skeemaa käyttää käsittelijä.
- callback, tätä käytetään työkalun kutsumiseen.

On myös `Tool`, jota käytetään muuttamaan tämä sanakirja tyypiksi, jonka mcp-palvelimen käsittelijä voi hyväksyä; se näyttää tältä:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Ja on *schema.ts*, jossa säilytämme kunkin työkalun syöteskeemat tällä hetkellä vain yhdellä skeemalla, mutta kun lisäämme työkaluja, voimme lisätä lisää merkintöjä:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Hienoa, siirrytään seuraavaksi työkalujen listaamisen käsittelyyn.

### -3- Käsittele työkalujen listaaminen

Seuraavaksi, käsitelläksemme työkalujen listaamista, meidän täytyy asettaa pyyntöjen käsittelijä sitä varten. Tässä mitä meidän täytyy lisätä palvelintiedostoomme:

**Python**

```python
# koodi jätetty lyhykäiseksi
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

Tässä lisäämme dekorointiin `@server.list_tools` ja toteuttavaan funktioon `handle_list_tools`. Jälkimmäisessä meidän täytyy tuottaa lista työkaluista. Huomaa, että jokaisella työkalulla täytyy olla nimi, kuvaus ja inputSchema.

**TypeScript**

Työkalujen listaamisen pyyntöjen käsittelijän määrittämiseen meidän täytyy kutsua `setRequestHandler` palvelimella skeeman kanssa, joka sopii siihen, mitä yritämme tehdä, tässä tapauksessa `ListToolsRequestSchema`.

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
// koodi jätetty pois lyhyyden vuoksi
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Palauta rekisteröityjen työkalujen lista
  return {
    tools: tools
  };
});
```

Hienoa, nyt olemme ratkaisseet työkalujen listaamisen osan, katsotaan seuraavaksi, miten voimme kutsua työkaluja.

### -4- Käsittele työkalun kutsu

Työkalun kutsumiseksi meidän täytyy määrittää toinen pyyntöjen käsittelijä, joka keskittyy käsittelemään pyyntöjä, joissa määritellään, mitä ominaisuutta kutsutaan ja millä argumenteilla.

**Python**

Käytetään dekorointia `@server.call_tool` ja toteutetaan se funktiolla, kuten `handle_call_tool`. Funktiossa meidän täytyy purkaa työkalun nimi, sen argumentti ja varmistaa, että argumentit ovat kelvollisia kyseiselle työkalulle. Voimme validoida argumentit tässä funktiossa tai varsinaisessa työkalussa.

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

Tässä mitä tapahtuu:

- Työkalun nimi on jo läsnä syötteenä parametrina `name`, mikä on totta argumenteille `arguments`-sanakirjassa.

- Työkalu kutsutaan `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Argumenttien validointi tapahtuu `handler`-ominaisuudessa, joka osoittaa funktioon; jos se epäonnistuu, se heittää poikkeuksen.

Siinäpä se, nyt meillä on täysi ymmärrys työkalujen listaamisesta ja kutsumisesta matalan tason palvelimella.

Katso [kokonaisesimerkki](./code/README.md) täältä

## Tehtävä

Laajenna saamaasi koodia useilla työkaluilla, resursseilla ja kehotteilla ja pohdi, kuinka huomaat, että sinun tarvitsee lisätä tiedostoja vain *tools*-hakemistoon etkä muualle.

*Ratkaisua ei anneta*

## Yhteenveto

Tässä luvussa näimme, miten matalan tason palvelimen lähestymistapa toimii ja miten se voi auttaa meitä luomaan hyvän arkkitehtuurin, jonka päälle voimme jatkaa rakentamista. Keskustelimme myös validoinnista, ja sinut näytettiin työskentelemään validointikirjastojen kanssa luodaksesi skeemoja syötteen validointiin.

## Seuraavaksi

- Seuraavaksi: [Yksinkertainen todennus](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimmekin tarkkuuteen, on hyvä huomioida, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää auktoritatiivisena lähteenä. Kriittisten tietojen osalta suosittelemme ammattilaisten tekemää ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->