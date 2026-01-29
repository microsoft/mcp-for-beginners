# Edistynyt palvelimen käyttö

MCP SDK:ssä on kaksi erilaista palvelintyyppiä: tavallinen palvelin ja matalan tason palvelin. Yleensä käytät tavallista palvelinta lisätäksesi siihen ominaisuuksia. Joissain tapauksissa kuitenkin haluat käyttää matalan tason palvelinta, esimerkiksi:

- Parempi arkkitehtuuri. On mahdollista luoda selkeä arkkitehtuuri sekä tavallisella että matalan tason palvelimella, mutta voidaan väittää, että matalan tason palvelimella se on hieman helpompaa.
- Ominaisuuksien saatavuus. Jotkut edistyneet ominaisuudet ovat käytettävissä vain matalan tason palvelimella. Näet tämän myöhemmissä luvuissa, kun lisäämme näytteenottoa ja tiedonkeruuta.

## Tavallinen palvelin vs matalan tason palvelin

Näin MCP-palvelimen luominen näyttää tavallisella palvelimella:

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

Tässä ideana on, että lisäät eksplisiittisesti jokaisen työkalun, resurssin tai kehotteen, jonka haluat palvelimella olevan. Tässä ei sinänsä ole mitään vikaa.

### Matalan tason palvelimen lähestymistapa

Kun käytät matalan tason palvelimen lähestymistapaa, sinun täytyy ajatella asiaa eri tavalla. Sen sijaan, että rekisteröisit jokaisen työkalun, luot kaksi käsittelijää per ominaisuustyyppi (työkalut, resurssit tai kehotteet). Esimerkiksi työkalujen kohdalla on vain kaksi funktiota, kuten seuraavasti:

- Kaikkien työkalujen listaus. Yksi funktio vastaa kaikista yrityksistä listata työkaluja.
- Kaikkien työkalujen kutsuminen. Tässäkin on vain yksi funktio, joka käsittelee työkalun kutsumista.

Kuulostaa siltä, että työmäärä voisi vähentyä, eikö? Sen sijaan, että rekisteröisit työkalun, sinun tarvitsee vain varmistaa, että työkalu listataan, kun listataan kaikki työkalut, ja että se kutsutaan, kun saapuu pyyntö työkalun kutsumiseksi.

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

Tässä meillä on funktio, joka palauttaa ominaisuuksien listan. Jokaisella merkinnällä työkalujen listassa on kentät, kuten `name`, `description` ja `inputSchema`, jotka vastaavat palautustyyppiä. Tämä mahdollistaa työkalujen ja ominaisuuksien määrittelyn sijoittamisen muualle. Voimme nyt luoda kaikki työkalumme työkalukansioon, ja sama pätee kaikkiin ominaisuuksiin, joten projektimme voi yhtäkkiä olla järjestetty seuraavasti:

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

Hienoa, arkkitehtuurimme voi näyttää melko siistiltä.

Entä työkalujen kutsuminen, onko se sama idea, yksi käsittelijä kutsumaan työkalua, mikä tahansa työkalu? Kyllä, juuri niin, tässä on koodi siihen:

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

Kuten yllä olevasta koodista näkyy, meidän täytyy purkaa kutsuttava työkalu ja sen argumentit, ja sitten jatkaa työkalun kutsumista.

## Lähestymistavan parantaminen validoinnilla

Tähän mennessä olet nähnyt, kuinka kaikki rekisteröinnit työkalujen, resurssien ja kehotteiden lisäämiseksi voidaan korvata näillä kahdella käsittelijällä per ominaisuustyyppi. Mitä muuta meidän täytyy tehdä? Meidän pitäisi lisätä jonkinlainen validointi varmistaaksemme, että työkalu kutsutaan oikeilla argumenteilla. Jokaisella ajonaikaisella ympäristöllä on oma ratkaisunsa tähän, esimerkiksi Python käyttää Pydanticia ja TypeScript käyttää Zodia. Idea on seuraava:

- Siirrä logiikka ominaisuuden (työkalu, resurssi tai kehotus) luomiseksi sen omaan kansioon.
- Lisää tapa validoida saapuva pyyntö, joka esimerkiksi pyytää työkalun kutsumista.

### Ominaisuuden luominen

Ominaisuuden luomiseksi meidän täytyy luoda tiedosto kyseiselle ominaisuudelle ja varmistaa, että siinä on kyseisen ominaisuuden vaatimat pakolliset kentät. Kentät vaihtelevat hieman työkalujen, resurssien ja kehotteiden välillä.

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

Tässä näet, kuinka teemme seuraavat asiat:

- Luomme skeeman käyttämällä Pydanticin `AddInputModel`-mallia, jossa on kentät `a` ja `b` tiedostossa *schema.py*.
- Yritämme jäsentää saapuvan pyynnön tyyppiin `AddInputModel`. Jos parametreissa on ristiriita, tämä kaatuu:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Voit valita, sijoitatko tämän jäsennyslogiikan itse työkalun kutsuun vai käsittelijäfunktioon.

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

- Käsittelijässä, joka käsittelee kaikkia työkalukutsuja, yritämme jäsentää saapuvan pyynnön työkalun määriteltyyn skeemaan:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Jos tämä onnistuu, jatkamme varsinaisen työkalun kutsumista:

    ```typescript
    const result = await tool.callback(input);
    ```

Kuten näet, tämä lähestymistapa luo hienon arkkitehtuurin, jossa kaikella on oma paikkansa. *server.ts* on hyvin pieni tiedosto, joka vain yhdistää pyyntökäsittelijät, ja jokainen ominaisuus on omassa kansiossaan, kuten tools/, resources/ tai prompts/.

Hienoa, kokeillaan rakentaa tämä seuraavaksi.

## Harjoitus: Matalan tason palvelimen luominen

Tässä harjoituksessa teemme seuraavat asiat:

1. Luomme matalan tason palvelimen, joka käsittelee työkalujen listaamista ja kutsumista.
1. Toteutamme arkkitehtuurin, jota voit laajentaa.
1. Lisäämme validoinnin varmistaaksemme, että työkalukutsut validoidaan asianmukaisesti.

### -1- Arkkitehtuurin luominen

Ensimmäinen asia, joka meidän täytyy ratkaista, on arkkitehtuuri, joka auttaa meitä laajentamaan ominaisuuksia. Tässä on, miltä se näyttää:

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

Nyt olemme luoneet arkkitehtuurin, joka varmistaa, että voimme helposti lisätä uusia työkaluja työkalukansioon. Voit halutessasi lisätä alikansioita resursseille ja kehotteille.

### -2- Työkalun luominen

Katsotaanpa, miltä työkalun luominen näyttää. Ensiksi se täytyy luoda sen *tool*-alikansioon, kuten seuraavasti:

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

Tässä näemme, kuinka määrittelemme nimen, kuvauksen, syöttöskeeman Pydanticin avulla ja käsittelijän, joka kutsutaan, kun tätä työkalua käytetään. Lopuksi paljastamme `tool_add`-sanakirjan, joka sisältää kaikki nämä ominaisuudet.

Lisäksi on *schema.py*, jota käytetään määrittämään työkalun käyttämä syöttöskeema:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Meidän täytyy myös täyttää *__init__.py* varmistaaksemme, että työkalukansio käsitellään moduulina. Lisäksi meidän täytyy paljastaa moduulit sen sisällä, kuten seuraavasti:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Voimme jatkaa tämän tiedoston päivittämistä, kun lisäämme uusia työkaluja.

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

Tässä luomme sanakirjan, joka koostuu seuraavista ominaisuuksista:

- name, työkalun nimi.
- rawSchema, Zod-skeema, jota käytetään validoimaan saapuvat pyynnöt työkalun kutsumiseksi.
- inputSchema, skeema, jota käsittelijä käyttää.
- callback, käytetään työkalun kutsumiseen.

Lisäksi on `Tool`, jota käytetään muuntamaan tämä sanakirja tyypiksi, jonka MCP-palvelimen käsittelijä voi hyväksyä, ja se näyttää tältä:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Ja on *schema.ts*, jossa säilytämme kunkin työkalun syöttöskeemat. Se näyttää tältä, ja siinä on tällä hetkellä vain yksi skeema, mutta kun lisäämme työkaluja, voimme lisätä enemmän merkintöjä:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Hienoa, jatketaan seuraavaksi työkalujen listaamisen käsittelyyn.

### -3- Työkalujen listaamisen käsittely

Seuraavaksi, jotta voimme käsitellä työkalujen listaamista, meidän täytyy asettaa pyyntökäsittelijä sitä varten. Tässä on, mitä meidän täytyy lisätä palvelintiedostoomme:

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

Tässä lisäämme koristeen `@server.list_tools` ja toteutamme funktion `handle_list_tools`. Jälkimmäisessä meidän täytyy tuottaa lista työkaluista. Huomaa, että jokaisella työkalulla täytyy olla nimi, kuvaus ja syöttöskeema.

**TypeScript**

Työkalujen listaamisen pyyntökäsittelijän asettamiseksi meidän täytyy kutsua `setRequestHandler` palvelimessa skeemalla, joka sopii siihen, mitä yritämme tehdä, tässä tapauksessa `ListToolsRequestSchema`.

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

Hienoa, nyt olemme ratkaisseet työkalujen listaamisen osan. Katsotaanpa seuraavaksi, kuinka voisimme kutsua työkaluja.

### -4- Työkalun kutsumisen käsittely

Työkalun kutsumiseksi meidän täytyy asettaa toinen pyyntökäsittelijä, tällä kertaa keskittyen käsittelemään pyyntöä, joka määrittää, mikä ominaisuus kutsutaan ja millä argumenteilla.

**Python**

Käytetään koristetta `@server.call_tool` ja toteutetaan se funktiolla, kuten `handle_call_tool`. Tämän funktion sisällä meidän täytyy purkaa työkalun nimi, sen argumentit ja varmistaa, että argumentit ovat validit kyseiselle työkalulle. Voimme joko validoida argumentit tässä funktiossa tai myöhemmin varsinaisessa työkalussa.

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

Tässä tapahtuu seuraavaa:

- Työkalun nimi on jo olemassa syöttöparametrina `name`, mikä pätee myös argumentteihin `arguments`-sanakirjan muodossa.

- Työkalu kutsutaan `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`-koodilla. Argumenttien validointi tapahtuu `handler`-ominaisuudessa, joka osoittaa funktioon. Jos validointi epäonnistuu, se nostaa poikkeuksen.

Siinä kaikki, nyt meillä on täydellinen ymmärrys työkalujen listaamisesta ja kutsumisesta matalan tason palvelimella.

Katso [täydellinen esimerkki](./code/README.md) täältä.

## Tehtävä

Laajenna sinulle annettua koodia useilla työkaluilla, resursseilla ja kehotteilla, ja pohdi, kuinka huomaat, että sinun tarvitsee lisätä tiedostoja vain työkalukansioon eikä mihinkään muualle.

*Ratkaisua ei anneta*

## Yhteenveto

Tässä luvussa näimme, kuinka matalan tason palvelimen lähestymistapa toimii ja kuinka se voi auttaa meitä luomaan mukavan arkkitehtuurin, jota voimme jatkaa rakentamaan. Keskustelimme myös validoinnista, ja sinulle näytettiin, kuinka työskennellä validointikirjastojen kanssa syöttöskeemojen luomiseksi.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.