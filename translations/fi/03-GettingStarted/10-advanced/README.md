# Edistynyt palvelimen käyttö

MCP SDK:ssa on kaksi erilaista palvelintyyppiä, tavallinen palvelimesi ja matalan tason palvelin. Yleensä käytät tavallista palvelinta lisätäksesi siihen ominaisuuksia. Joissain tapauksissa haluat kuitenkin turvautua matalan tason palvelimeen, kuten:

- Parempi arkkitehtuuri. On mahdollista luoda puhdas arkkitehtuuri sekä tavallisella että matalan tason palvelimella, mutta voidaan väittää, että se on hieman helpompaa matalan tason palvelimella.
- Ominaisuuksien saatavuus. Jotkut edistyneet ominaisuudet ovat käytettävissä vain matalan tason palvelimen kanssa. Näet tämän myöhemmissä luvuissa, kun lisäämme näytteenoton ja houkuttelun.

## Tavallinen palvelin vs matalan tason palvelin

Näin MCP-palvelimen luominen näyttää tavallisella palvelimella

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

// Lisää yhdistämistyökalu
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

Ajatus on, että lisäät eksplisiittisesti jokaisen työkalun, resurssin tai kehotteen, jonka haluat palvelimen sisältävän. Tässä ei ole mitään väärää.

### Matalan tason palvelin -lähestymistapa

Kuitenkin, kun käytät matalan tason palvelimen lähestymistapaa, sinun täytyy ajatella asiat toisin. Sen sijaan, että rekisteröit jokaisen työkalun erikseen, luot kullekin ominaisuustyypille (työkalut, resurssit tai kehote) kaksi käsittelijää. Esimerkiksi työkaluilla on vain kaksi funktiota:

- Kaikkien työkalujen listaaminen. Yksi funktio vastaa kaikista yrityksistä listata työkaluja.
- Kaikkien työkalujen kutsujen käsittely. Tässäkin on vain yksi funktio, joka käsittelee työkalun kutsut.

Se kuulostaa mahdollisesti vähemmän työtä vaativalta, eikö? Joten sen sijaan, että rekisteröisin työkalun, minun tarvitsee vain varmistaa, että työkalu listataan, kun listaan kaikki työkalut, ja että sitä kutsutaan, kun saapuu pyyntö kutsua työkalua.

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
  // Palauta rekisteröityjen työkalujen luettelo
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

Tässä meillä on nyt funktio, joka palauttaa ominaisuuksien listan. Jokaisessa työkalujen listan kohdassa on kenttiä kuten `name`, `description` ja `inputSchema` vastaamaan palautustyyppiä. Tämä mahdollistaa työkalujen ja ominaisuusmääritelmien sijoittamisen muualle. Voimme nyt luoda kaikki työkalut tools-hakemistoon ja sama pätee kaikkiin ominaisuuksiin, joten projektisi voidaan yhtäkkiä järjestää näin:

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

Hienoa, arkkitehtuurimme voi näyttää erittäin siistiltä.

Miten sitten työkalujen kutsuminen, onko se sama idea, yksi käsittelijä kutsumaan työkalua, mikä tahansa työkalu? Kyllä, juuri niin, tässä on koodi siihen:

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

Kuten yllä olevasta koodista näkyy, meidän täytyy purkaa, mikä työkalu kutsutaan ja millä argumenteilla, ja sen jälkeen meidän täytyy jatkaa työkalun kutsumista.

## Lähestymistavan parantaminen validoinnilla

Tähän mennessä olet nähnyt, kuinka kaikki rekisteröintisi työkalujen, resurssien ja kehotteiden lisäämiseksi voidaan korvata näillä kahdella käsittelijällä per ominaisuustyyppi. Mitä muuta meidän täytyy tehdä? No, meidän pitäisi lisätä jonkinlainen validointi varmistaaksemme, että työkalu kutsutaan oikeilla argumenteilla. Jokaisella ajonaikaisella ympäristöllä on oma ratkaisunsa tähän, esimerkiksi Python käyttää Pydanticia ja TypeScript käyttää Zodia. Ajatus on, että teemme seuraavaa:

- Siirrämme logiikan ominaisuuden (työkalu, resurssi tai kehote) luomiseksi siihen omistautuneeseen kansioon.
- Lisätään tapa validoida saapuva pyyntö, joka esimerkiksi pyytää työkalun kutsua.

### Ominaisuuden luominen

Ominaisuuden luomiseksi meidän täytyy luoda tiedosto kyseiselle ominaisuudelle ja varmistaa, että sillä on pakolliset kentät, joita ominaisuus vaatii. Kentät eroavat hieman työkaluissa, resursseissa ja kehotteissa.

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

tässä näet kuinka teemme seuraavaa:

- Luomme skeeman käyttäen Pydanticin `AddInputModel`-luokkaa kentillä `a` ja `b` tiedostossa *schema.py*.
- Yritämme jäsentää saapuvan pyynnön tyypiksi `AddInputModel`. Jos parametrit eivät täsmää, tämä aiheuttaa virheen:

   ```python
   # add.py
    try:
        # Vahvista syöte käyttämällä Pydantic-mallia
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Voit valita, laitatko tämän jäsentämislogiikan työkalukutsuun itsessään vai käsittelijäfunktioon.

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

// lisää.ts
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

- Käsittelijässä, joka käsittelee kaikkia työkalukutsuja, yritämme nyt jäsentää saapuvan pyynnön työkalun määrittelemään skeemaan:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jos se onnistuu, jatkamme työkalun varsinaista kutsua:

    ```typescript
    const result = await tool.callback(input);
    ```

Kuten näet, tämä lähestymistapa luo hienon arkkitehtuurin, sillä kaikella on paikkansa. *server.ts* on hyvin pieni tiedosto, joka vain kytkee pyyntökäsittelijät paikoilleen, ja kukin ominaisuus on omassa kansiossaan, eli tools/, resources/ tai /prompts.

Hienoa, kokeillaan seuraavaksi tämän rakentamista.

## Harjoitus: Matala tason palvelimen luominen

Tässä harjoituksessa teemme seuraavaa:

1. Luomme matalan tason palvelimen, joka käsittelee työkalujen listauksen ja kutsumisen.
1. Toteutamme arkkitehtuurin, jonka päälle voit rakentaa.
1. Lisäämme validoinnin varmistaaksemme, että työkalukutsusi validoidaan oikein.

### -1- Luo arkkitehtuuri

Ensimmäinen asia, johon meidän täytyy keskittyä, on arkkitehtuuri, joka auttaa meitä skaalaamaan, kun lisäämme ominaisuuksia. Näin se näyttää:

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

Nyt olemme luoneet arkkitehtuurin, joka varmistaa, että voimme helposti lisätä uusia työkaluja tools-kansioon. Voit vapaasti lisätä alihakemistoja resursseille ja kehotteille.

### -2- Työkalun luominen

Katsotaan seuraavaksi, miltä työkalun luominen näyttää. Ensin sen pitää olla luotuna omassa *tool*-alikansiossaan näin:

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

Näet tässä, miten määrittelemme nimen, kuvauksen ja syötteen skeeman käyttäen Pydanticia sekä käsittelijän, jota kutsutaan, kun tätä työkalua käytetään. Lopuksi julkaisemme `tool_add`-sanakirjan, joka sisältää kaikki nämä ominaisuudet.

Mukana on myös *schema.py*, jota käytämme määrittelemään työkalun syötteen skeeman:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Meidän täytyy myös täyttää *__init__.py* varmistaaksemme, että tools-kansio käsitellään moduulina. Lisäksi meidän pitää julkaista sen moduulit näin:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Voimme lisätä tähän tiedostoon lisää työkaluja, kun niitä tulee.

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

Täällä luomme sanakirjan, joka sisältää ominaisuudet:

- name, työkalun nimi.
- rawSchema, Zod-skeema, jota käytetään validointiin saapuvissa syötteissä tätä työkalua kutsuttaessa.
- inputSchema, tätä skeemaa käyttää käsittelijä.
- callback, tätä käytetään työkalun kutsumiseen.

Mukana on myös `Tool`, jolla tämä sanakirja muunnetaan tyypiksi, jonka mcp-palvelimen käsittelijä voi hyväksyä, ja se näyttää tältä:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Ja siellä on *schema.ts*, jossa säilytämme syöteskeemat jokaiselle työkaluin, joka näyttää tältä, tällä hetkellä vain yhdellä skeemalla, mutta kun lisäämme työkaluja, lisäämme rivejä:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Hienoa, siirrytään seuraavaksi työkalujen listauksen käsittelyyn.

### -3- Käsittele työkalujen listausta

Seuraavaksi, työkalujen listaamisen käsittelemiseksi meidän täytyy määrittää pyyntökäsittelijä. Tässä mitä meidän tulee lisätä palvelintiedostoomme:

**Python**

```python
# koodi jätetty lyhyyden vuoksi
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

Lisäämme koristeen `@server.list_tools` ja toteuttavan funktion `handle_list_tools`. Tässä meidän täytyy tuottaa lista työkaluista. Huomaa kuinka jokaisella työkalulla on nimi, kuvaus ja inputSchema.

**TypeScript**

Työkalujen listauksen pyyntökäsittelijän asettamiseksi kutsumme `setRequestHandler`-funktiota palvelimessa skeemalla, joka sopii tehtävään, tässä tapauksessa `ListToolsRequestSchema`.

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
// Koodi jätetty pois lyhyyden vuoksi
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Palauta rekisteröityjen työkalujen lista
  return {
    tools: tools
  };
});
```

Hienoa, nyt olemme ratkaisseet työkalujen listauksen osan. Katsotaan seuraavaksi, miten voisimme kutsua työkaluja.

### -4- Käsittele työkalun kutsua

Työkalun kutsumiseksi meidän täytyy asettaa toinen pyyntökäsittelijä, joka keskittyy käsittelemään pyyntöjä, joissa määritellään, mitä ominaisuutta kutsutaan ja millä argumenteilla.

**Python**

Käytetään koristetta `@server.call_tool` ja toteutetaan se funktiolla, kuten `handle_call_tool`. Funktion sisällä meidän täytyy purkaa työkalun nimi, sen argumentti ja varmistaa, että argumentit ovat päteviä kyseiselle työkalulle. Voimme validoida argumentit tässä funktiossa tai myöhemmin varsinaisessa työkalussa.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools on sanakirja, jossa avaimina ovat työkalujen nimet
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

- Työkalun nimi on jo syöteparametrina `name`, ja argumentit ovat `arguments`-sanakirjassa.

- Työkalu kutsutaan `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Argumenttien validointi tapahtuu `handler`-ominaisuudessa, joka on funktioon osoittava osoitin; jos validointi epäonnistuu, se nostaa poikkeuksen.

Nyt meillä on täydellinen ymmärrys työkalujen listaamisesta ja kutsumisesta matalan tason palvelimella.

Katso [täysi esimerkki](./code/README.md) täältä

## Tehtävä

Laajenna sinulle annettua koodia lisäämällä useita työkaluja, resursseja ja kehotteita ja pohdi, kuinka huomaat, että sinun tarvitsee lisätä tiedostoja vain tools-kansioon, etkä minnekään muualle.

*Ratkaisua ei anneta*

## Yhteenveto

Tässä luvussa näimme, miten matalan tason palvelin toimii ja miten se voi auttaa meitä luomaan siistin arkkitehtuurin, jonka päälle voi rakentaa. Keskustelimme myös validoinnista, ja sinulle näytettiin, miten käytetään validointikirjastoja luomaan skeemoja syötteen validointiin.

## Mitä seuraavaksi

- Seuraavaksi: [Yksinkertainen todennus](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja omalla kielellään tulee pitää ensisijaisena lähteenä. Tärkeissä asioissa suositellaan ammattilaisen tekemää ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä mahdollisesti aiheutuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->