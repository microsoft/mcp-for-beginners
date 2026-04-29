# Sampling - delegera funktioner till klienten

Ibland behöver du att MCP-klienten och MCP-servern samarbetar för att uppnå ett gemensamt mål. Du kan ha ett fall där servern behöver hjälp av en LLM som finns på klienten. För denna situation är sampling det du bör använda.

Låt oss utforska några användningsfall och hur man bygger en lösning som involverar sampling.

## Översikt

I denna lektion fokuserar vi på att förklara när och var man ska använda Sampling och hur man konfigurerar det.

## Lärandemål

I detta kapitel kommer vi att:

- Förklara vad Sampling är och när man ska använda det.
- Visa hur man konfigurerar Sampling i MCP.
- Ge exempel på Sampling i praktiken.

## Vad är Sampling och varför använda det?

Sampling är en avancerad funktion som fungerar på följande sätt:

```mermaid
sequenceDiagram
    participant User
    participant MCP Client
    participant LLM
    participant MCP Server

    User->>MCP Client: Skapa bloggpost
    MCP Client->>MCP Server: Verktygsanrop (utkast till bloggpost)
    MCP Server->>MCP Client: Begäran om sampling (skapa sammanfattning)
    MCP Client->>LLM: Generera sammanfattning av bloggpost
    LLM->>MCP Client: Sammanfattningsresultat
    MCP Client->>MCP Server: Svar på sampling (sammanfattning)
    MCP Server->>MCP Client: Komplett bloggpost (utkast + sammanfattning)
    MCP Client->>User: Bloggpost klar
```
### Sampling-förfrågan

Okej, nu har vi en översiktlig bild av ett trovärdigt scenario, låt oss prata om den sampling-förfrågan som servern skickar tillbaka till klienten. Så här kan en sådan förfrågan se ut i JSON-RPC-format:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "Create a blog post summary of the following blog post: <BLOG POST>"
        }
      }
    ],
    "modelPreferences": {
      "hints": [
        {
          "name": "claude-3-sonnet"
        }
      ],
      "intelligencePriority": 0.8,
      "speedPriority": 0.5
    },
    "systemPrompt": "You are a helpful assistant.",
    "maxTokens": 100
  }
}
```

Det finns några saker här som är värda att lyfta fram:

- Prompt, under content -> text, är vår prompt som är en instruktion till LLM att sammanfatta innehållet i ett blogginlägg.

- **modelPreferences**. Den här sektionen är just det, en preferens, en rekommendation av vilken konfiguration som ska användas med LLM:en. Användaren kan välja om de vill följa dessa rekommendationer eller ändra dem. I det här fallet finns rekommendationer om vilken modell som ska användas samt prioritering mellan hastighet och intelligens.
- **systemPrompt**, detta är din vanliga systemprompt som ger din LLM en personlighet och innehåller vägledande instruktioner.
- **maxTokens**, detta är en annan egenskap som används för att ange hur många tokens som rekommenderas att använda för denna uppgift.

### Sampling-svar

Detta svar är vad MCP-klienten till slut skickar tillbaka till MCP-servern och är resultatet av att klienten anropar LLM, väntar på svaret och sedan konstruerar detta meddelande. Så här kan det se ut i JSON-RPC:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "role": "assistant",
    "content": {
      "type": "text",
      "text": "Here's your abstract <ABSTRACT>"
    },
    "model": "gpt-5",
    "stopReason": "endTurn"
  }
}
```

Notera hur svaret är ett abstrakt av blogginlägget precis som vi bad om. Notera också hur den använda `model` inte är vad vi bad om utan "gpt-5" istället för "claude-3-sonnet". Detta för att illustrera att användaren kan ändra sig om vad som ska användas och att din sampling-förfrågan är en rekommendation.

Okej, nu när vi förstår huvudflödet, och en användbar uppgift att använda det till "skapa blogginlägg + abstrakt", låt oss se vad vi behöver göra för att få det att fungera.

### Meddelandetyper

Sampling-meddelanden är inte begränsade till bara text, utan du kan även skicka bilder och ljud. Så här ser JSON-RPC annorlunda ut:

**Text**

```json
{
  "type": "text",
  "text": "The message content"
}
```

**Bildinnehåll**

```json
{
  "type": "image",
  "data": "base64-encoded-image-data",
  "mimeType": "image/jpeg"
}
```

**Ljudinnehåll**

```json
{
  "type": "audio",
  "data": "base64-encoded-audio-data",
  "mimeType": "audio/wav"
}
```

> NOTE: för mer detaljerad information om Sampling, kolla [officiell dokumentation](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling)

## Hur man konfigurerar Sampling i klienten

> Obs: om du bara bygger en server behöver du inte göra mycket här.

I en klient behöver du specificera följande funktion så här:

```json
{
  "capabilities": {
    "sampling": {}
  }
}
```

Detta kommer sedan att plockas upp när din valda klient initieras med servern.

## Exempel på Sampling i praktiken - Skapa ett blogginlägg

Låt oss koda en sampling-server tillsammans, vi behöver göra följande:

1. Skapa ett verktyg på servern.
1. Detta verktyg ska skapa en sampling-förfrågan.
1. Verktyget ska vänta tills klientens sampling-förfrågan har besvarats.
1. Sedan ska verktygets resultat produceras.

Låt oss titta på koden steg för steg:

### -1- Skapa verktyget

**python**

```python
@mcp.tool()
async def create_blog(title: str, content: str, ctx: Context[ServerSession, None]) -> str:
    """Create a blog post and generate a summary"""

```

### -2- Skapa en sampling-förfrågan

Utöka ditt verktyg med följande kod:

**python**

```python
post = BlogPost(
        id=len(posts) + 1,
        title=title,
        content=content,
        abstract=""
    )

prompt = f"Create an abstract of the following blog post: title: {title} and draft: {content} "

result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(type="text", text=prompt),
            )
        ],
        max_tokens=100,
)

```

### -3- Vänta på svaret och returnera svaret

**python**

```python
post.abstract = result.content.text

posts.append(post)

# returnera den kompletta produkten
return json.dumps({
    "id": post.title,
    "abstract": post.abstract
})
```

### -4- Fullständig kod

**python**

```python
from starlette.applications import Starlette
from starlette.routing import Mount, Host

from mcp.server.fastmcp import Context, FastMCP

from mcp.server.session import ServerSession
from mcp.types import SamplingMessage, TextContent

import json


from uuid import uuid4
from typing import List
from pydantic import BaseModel


mcp = FastMCP("Blog post generator")

# app = FastAPI()

posts = []

class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    abstract: str

posts: List[BlogPost] = []

@mcp.tool()
async def create_blog(title: str, content: str, ctx: Context[ServerSession, None]) -> str:
    """Create a blog post and generate a summary"""

    post = BlogPost(
        id=len(posts) + 1,
        title=title,
        content=content,
        abstract=""
    )

    prompt = f"Create an abstract of the following blog post: title: {title} and draft: {content} "

    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(type="text", text=prompt),
            )
        ],
        max_tokens=100,
    )

    post.abstract = result.content.text

    posts.append(post)

    # returnera det kompletta blogginlägget
    return json.dumps({
        "id": post.title,
        "abstract": post.abstract
    })

if __name__ == "__main__":
    print("Starting server...")
    # mcp.run()
    mcp.run(transport="streamable-http")

# kör appen med: python server.py
```

### -5- Testa det i Visual Studio Code

För att testa detta i Visual Studio Code, gör följande:

1. Starta servern i terminalen
1. Lägg till den i *mcp.json* (och se till att den är startad), något i stil med detta:

   ```json
   "servers": {
      "blog-server": {
        "type": "http",
        "url": "http://localhost:8000/mcp"
      }
   }
   ```

1. Skriv en prompt:

   ```text
   create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
   ```

1. Tillåt sampling att ske. Första gången du testar detta kommer du att presenteras med en extra dialog som du måste acceptera, sedan ser du den vanliga dialogen för att bli tillfrågad att köra ett verktyg.

1. Inspektera resultat. Du kommer att se resultaten både snyggt presenterade i GitHub Copilot Chat men du kan även inspektera det råa JSON-svaret.

**Bonus**. Visual Studio Codes verktyg har bra stöd för sampling. Du kan konfigurera Sampling-åtkomst på din installerade server genom att navigera så här:

1. Gå till avsnittet för extension.
1. Välj kugghjulsikonen för din installerade server i avsnittet "MCP SERVERS - INSTALLED".
1. Välj "Configure Model Access", här kan du välja vilka modeller GitHub Copilot får använda vid sampling. Du kan också se alla sampling-förfrågningar som gjorts nyligen genom att välja "Show Sampling requests".

## Uppgift

I denna uppgift ska du bygga en något annorlunda Sampling, nämligen en sampling-integration som stödjer att generera en produktbeskrivning. Här är ditt scenario:

**Scenario**: Backoffice-medarbetaren på en e-handel behöver hjälp, det tar alldeles för lång tid att generera produktbeskrivningar. Därför ska du bygga en lösning där du kan kalla ett verktyg "create_product" med "title" och "keywords" som argument och det ska producera en komplett produkt inklusive ett fält "description" som ska fyllas i av en LLM på klienten.

TIP: använd det du lärt dig tidigare för att konstruera denna server och dess verktyg med en sampling-förfrågan.

## Lösning

[Lösning](./solution/README.md)

## Viktiga lärdomar

Sampling är en kraftfull funktion som låter servern delegera uppgifter till klienten när den behöver hjälp av en LLM.

## Vad händer härnäst

- [Kapitel 4 - Praktisk implementation](../../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->