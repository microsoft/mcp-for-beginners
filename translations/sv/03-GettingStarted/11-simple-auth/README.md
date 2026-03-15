# Enkel autentisering

MCP SDK:er stödjer användning av OAuth 2.1 som för att vara ärlig är en ganska omfattande process som involverar begrepp som autentiseringsserver, resursserver, postning av uppgifter, att få en kod, byta koden mot en access-token tills du slutligen kan få dina resursdata. Om du är ovan vid OAuth, vilket är en bra sak att implementera, är det en god idé att börja med en grundläggande nivå av autentisering och bygga upp till bättre och bättre säkerhet. Det är därför detta kapitel finns, för att bygga upp dig till mer avancerad autentisering.

## Autentisering, vad menar vi?

Auth är kort för autentisering och auktorisering. Idén är att vi behöver göra två saker:

- **Autentisering**, vilket är processen att ta reda på om vi släpper in en person i vårt hem, att de har rätt att vara "här", det vill säga ha åtkomst till vår resursserver där våra MCP Server-funktioner finns.
- **Auktorisering**, är processen att ta reda på om en användare ska ha åtkomst till just dessa specifika resurser de efterfrågar, till exempel dessa order eller dessa produkter, eller om de tillåts läsa innehållet men inte ta bort det som ett annat exempel.

## Uppgifter: hur vi berättar för systemet vem vi är

De flesta webbtrafikutvecklare tänker i termer av att tillhandahålla en uppgift till servern, vanligtvis en hemlighet som säger om de har tillåtelse att vara här "Autentisering". Denna uppgift är vanligtvis en base64-kodad version av användarnamn och lösenord eller en API-nyckel som unikt identifierar en specifik användare.

Det innebär att den skickas via en header som kallas "Authorization" på följande sätt:

```json
{ "Authorization": "secret123" }
```

Detta kallas vanligtvis för grundläggande autentisering. Hur det övergripande flödet sedan fungerar är på följande sätt:

```mermaid
sequenceDiagram
   participant User
   participant Client
   participant Server

   User->>Client: visa mig data
   Client->>Server: visa mig data, här är mina uppgifter
   Server-->>Client: 1a, jag känner dig, här är din data
   Server-->>Client: 1b, jag känner inte dig, 401 
```
Nu när vi förstår hur det fungerar från ett flödesperspektiv, hur implementerar vi det? De flesta webbservrar har ett koncept som kallas middleware, en kodbit som körs som en del av förfrågan och kan verifiera uppgifter, och om uppgifterna är giltiga kan låta förfrågan passera. Om förfrågan inte har giltiga uppgifter får du ett autentiseringsfel. Låt oss se hur detta kan implementeras:

**Python**

```python
class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):

        has_header = request.headers.get("Authorization")
        if not has_header:
            print("-> Missing Authorization header!")
            return Response(status_code=401, content="Unauthorized")

        if not valid_token(has_header):
            print("-> Invalid token!")
            return Response(status_code=403, content="Forbidden")

        print("Valid token, proceeding...")
       
        response = await call_next(request)
        # lägg till eventuella kundhuvuden eller ändra svaret på något sätt
        return response


starlette_app.add_middleware(CustomHeaderMiddleware)
```

Här har vi:

- Skapat en middleware som heter `AuthMiddleware` där dess `dispatch`-metod anropas av webbservern.
- Lagt till middleware i webbservern:

    ```python
    starlette_app.add_middleware(AuthMiddleware)
    ```

- Skrivit valideringslogik som kontrollerar om Authorization-headern finns och om den hemlighet som skickas är giltig:

    ```python
    has_header = request.headers.get("Authorization")
    if not has_header:
        print("-> Missing Authorization header!")
        return Response(status_code=401, content="Unauthorized")

    if not valid_token(has_header):
        print("-> Invalid token!")
        return Response(status_code=403, content="Forbidden")
    ```

    Om hemligheten finns och är giltig låter vi förfrågan passera genom att anropa `call_next` och returnera svaret.

    ```python
    response = await call_next(request)
    # lägg till eventuella kundhuvuden eller ändra svaret på något sätt
    return response
    ```

Så här fungerar det: om en webbfråga görs mot servern kommer middleware att anropas och givet dess implementation kommer det antingen låta förfrågan passera eller returnera ett fel som indikerar att klienten inte har rätt att fortsätta.

**TypeScript**

Här skapar vi en middleware med det populära ramverket Express och stoppar förfrågan innan den når MCP Server. Här är koden för det:

```typescript
function isValid(secret) {
    return secret === "secret123";
}

app.use((req, res, next) => {
    // 1. Har auktoriseringshuvud?
    if(!req.headers["Authorization"]) {
        res.status(401).send('Unauthorized');
    }
    
    let token = req.headers["Authorization"];

    // 2. Kontrollera giltighet.
    if(!isValid(token)) {
        res.status(403).send('Forbidden');
    }

   
    console.log('Middleware executed');
    // 3. Skicka vidare förfrågan till nästa steg i förfrågningskedjan.
    next();
});
```

I denna kod:

1. Kontrollerar vi om Authorization-headern finns överhuvudtaget, om inte skickar vi ett 401-fel.
2. Säkerställer vi att uppgiften/token är giltig, om inte skickar vi ett 403-fel.
3. Slutligen skickar vi vidare förfrågan i förfrågningspipen och returnerar den efterfrågade resursen.

## Övning: Implementera autentisering

Låt oss ta vår kunskap och försöka implementera det. Så här är planen:

Server

- Skapa en webbserver och MCP-instans.
- Implementera middleware för servern.

Klient 

- Skicka webbfråga, med uppgift, via header.

### -1- Skapa en webbserver och MCP-instans

I vårt första steg behöver vi skapa webbserverinstansen och MCP Server.

**Python**

Här skapar vi en MCP-serverinstans, skapar en starlette-webbapp och hostar den med uvicorn.

```python
# skapar MCP-server

app = FastMCP(
    name="MCP Resource Server",
    instructions="Resource Server that validates tokens via Authorization Server introspection",
    host=settings["host"],
    port=settings["port"],
    debug=True
)

# skapar starlette webbapp
starlette_app = app.streamable_http_app()

# serverar app via uvicorn
async def run(starlette_app):
    import uvicorn
    config = uvicorn.Config(
            starlette_app,
            host=app.settings.host,
            port=app.settings.port,
            log_level=app.settings.log_level.lower(),
        )
    server = uvicorn.Server(config)
    await server.serve()

run(starlette_app)
```

I denna kod:

- Skapar vi MCP Server.
- Konstruerar starlette-webbappen från MCP Server, `app.streamable_http_app()`.
- Hostar och serverar webbappen med uvicorn `server.serve()`.

**TypeScript**

Här skapar vi en MCP Server-instans.

```typescript
const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    });

    // ... konfigurera serverresurser, verktyg och uppmaningar ...
```

Denna skapande av MCP Server måste hända inom vår POST /mcp-routdefinition, så låt oss ta ovanstående kod och flytta den så här:

```typescript
import express from "express";
import { randomUUID } from "node:crypto";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { isInitializeRequest } from "@modelcontextprotocol/sdk/types.js"

const app = express();
app.use(express.json());

// Karta för att lagra transporter efter sessions-ID
const transports: { [sessionId: string]: StreamableHTTPServerTransport } = {};

// Hantera POST-förfrågningar för klient-till-server-kommunikation
app.post('/mcp', async (req, res) => {
  // Kontrollera om sessions-ID redan finns
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  let transport: StreamableHTTPServerTransport;

  if (sessionId && transports[sessionId]) {
    // Återanvänd befintlig transport
    transport = transports[sessionId];
  } else if (!sessionId && isInitializeRequest(req.body)) {
    // Ny initieringsförfrågan
    transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: () => randomUUID(),
      onsessioninitialized: (sessionId) => {
        // Lagra transporten efter sessions-ID
        transports[sessionId] = transport;
      },
      // DNS-rebindningsskydd är som standard avaktiverat för bakåtkompatibilitet. Om du kör denna server
      // lokalt, se till att ställa in:
      // enableDnsRebindingProtection: true,
      // allowedHosts: ['127.0.0.1'],
    });

    // Rensa upp transport när den stängs
    transport.onclose = () => {
      if (transport.sessionId) {
        delete transports[transport.sessionId];
      }
    };
    const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    });

    // ... sätt upp serverresurser, verktyg och prompts ...

    // Anslut till MCP-servern
    await server.connect(transport);
  } else {
    // Ogiltig förfrågan
    res.status(400).json({
      jsonrpc: '2.0',
      error: {
        code: -32000,
        message: 'Bad Request: No valid session ID provided',
      },
      id: null,
    });
    return;
  }

  // Hantera förfrågan
  await transport.handleRequest(req, res, req.body);
});

// Återanvändbar hanterare för GET- och DELETE-förfrågningar
const handleSessionRequest = async (req: express.Request, res: express.Response) => {
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  if (!sessionId || !transports[sessionId]) {
    res.status(400).send('Invalid or missing session ID');
    return;
  }
  
  const transport = transports[sessionId];
  await transport.handleRequest(req, res);
};

// Hantera GET-förfrågningar för server-till-klient-notifikationer via SSE
app.get('/mcp', handleSessionRequest);

// Hantera DELETE-förfrågningar för att avsluta sessionen
app.delete('/mcp', handleSessionRequest);

app.listen(3000);
```

Nu ser du hur MCP Server-skapandet flyttades inuti `app.post("/mcp")`.

Låt oss gå vidare till nästa steg att skapa middleware så vi kan validera den inkommande uppgiften.

### -2- Implementera middleware för servern

Låt oss gå till middleware-delen nästa. Här skapar vi en middleware som letar efter en uppgift i `Authorization`-headern och validerar den. Om den accepteras går förfrågan vidare för att göra det som behövs (t.ex. lista verktyg, läsa en resurs eller vad än MCP-funktionalitet klienten bad om).

**Python**

För att skapa middleware måste vi skapa en klass som ärver från `BaseHTTPMiddleware`. Det finns två intressanta delar:

- Förfrågan `request` som vi läser header-informationen från.
- `call_next`, callback som vi måste anropa om klienten har medfört en uppgift vi accepterar.

Först måste vi hantera fallet om `Authorization`-headern saknas:

```python
has_header = request.headers.get("Authorization")

# ingen header närvarande, misslyckas med 401, annars fortsätt.
if not has_header:
    print("-> Missing Authorization header!")
    return Response(status_code=401, content="Unauthorized")
```

Här skickar vi ett 401 unauthorized-meddelande eftersom klienten misslyckas med autentiseringen.

Om en uppgift skickats med måste vi sedan kontrollera dess giltighet så här:

```python
 if not valid_token(has_header):
    print("-> Invalid token!")
    return Response(status_code=403, content="Forbidden")
```

Notera hur vi skickar ett 403 forbidden-meddelande ovan. Låt oss se hela middleware nedan som implementerar allt vi nämnt:

```python
class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):

        has_header = request.headers.get("Authorization")
        if not has_header:
            print("-> Missing Authorization header!")
            return Response(status_code=401, content="Unauthorized")

        if not valid_token(has_header):
            print("-> Invalid token!")
            return Response(status_code=403, content="Forbidden")

        print("Valid token, proceeding...")
        print(f"-> Received {request.method} {request.url}")
        response = await call_next(request)
        response.headers['Custom'] = 'Example'
        return response

```

Bra, men vad är `valid_token`-funktionen? Här är den nedan:

```python
# ANVÄND INTE för produktion - förbättra det !!
def valid_token(token: str) -> bool:
    # ta bort prefixet "Bearer "
    if token.startswith("Bearer "):
        token = token[7:]
        return token == "secret-token"
    return False
```

Detta bör naturligtvis förbättras.

VIKTIGT: Du bör ALDRIG ha hemligheter som denna i kod. Du bör helst hämta värdet att jämföra med från en datakälla eller från en IDP (identity service provider) eller ännu bättre, låta IDP göra valideringen.

**TypeScript**

För att implementera detta med Express måste vi anropa `use`-metoden som tar middlewarefunktioner.

Vi behöver:

- Interagera med request-variabeln för att kontrollera den skickade uppgiften i `Authorization`-egenskapen.
- Validera uppgiften, och om så är fallet låta förfrågan fortsätta så att klientens MCP-förfrågan kan göra vad den ska (t.ex. lista verktyg, läsa resurs eller något annat MCP-relaterat).

Här kontrollerar vi om `Authorization`-headern finns och stoppar annars förfrågan från att gå igenom:

```typescript
if(!req.headers["authorization"]) {
    res.status(401).send('Unauthorized');
    return;
}
```

Om headern inte skickas från början får du ett 401.

Nästa, vi kontrollerar om uppgiften är giltig, om inte stoppar vi förfrågan igen men med ett något annorlunda meddelande:

```typescript
if(!isValid(token)) {
    res.status(403).send('Forbidden');
    return;
} 
```

Notera hur du nu får ett 403-fel.

Här är hela koden:

```typescript
app.use((req, res, next) => {
    console.log('Request received:', req.method, req.url, req.headers);
    console.log('Headers:', req.headers["authorization"]);
    if(!req.headers["authorization"]) {
        res.status(401).send('Unauthorized');
        return;
    }
    
    let token = req.headers["authorization"];

    if(!isValid(token)) {
        res.status(403).send('Forbidden');
        return;
    }  

    console.log('Middleware executed');
    next();
});
```

Vi har ställt in webbservern för att acceptera en middleware som kontrollerar uppgiften som klienten förhoppningsvis skickar till oss. Hur är det med själva klienten?

### -3- Skicka webbfråga med uppgift via header

Vi måste säkerställa att klienten skickar uppgiften genom headern. Eftersom vi ska använda en MCP-klient för detta måste vi ta reda på hur det görs.

**Python**

För klienten behöver vi skicka med en header med vår uppgift så här:

```python
# KODA INTE värdet direkt, ha det som minst i en miljövariabel eller ett säkrare lagringsställe
token = "secret-token"

async with streamablehttp_client(
        url = f"http://localhost:{port}/mcp",
        headers = {"Authorization": f"Bearer {token}"}
    ) as (
        read_stream,
        write_stream,
        session_callback,
    ):
        async with ClientSession(
            read_stream,
            write_stream
        ) as session:
            await session.initialize()
      
            # TODO, vad du vill göra i klienten, t.ex. lista verktyg, anropa verktyg osv.
```

Notera hur vi fyller i `headers`-egenskapen så här ` headers = {"Authorization": f"Bearer {token}"}`.

**TypeScript**

Vi kan lösa detta i två steg:

1. Fyll i ett konfigurationsobjekt med vår uppgift.
2. Skicka konfigurationsobjektet till transporten.

```typescript

// SKRIV INTE värdet som hårdkodat som visas här. Ha det åtminstone som en miljövariabel och använd något som dotenv (i utvecklingsläge).
let token = "secret123"

// definiera ett klienttransportalternativsobjekt
let options: StreamableHTTPClientTransportOptions = {
  sessionId: sessionId,
  requestInit: {
    headers: {
      "Authorization": "secret123"
    }
  }
};

// skicka optionsobjektet till transporten
async function main() {
   const transport = new StreamableHTTPClientTransport(
      new URL(serverUrl),
      options
   );
```

Här ser du ovan hur vi var tvungna att skapa ett `options`-objekt och placera våra headers under `requestInit`-egenskapen.

VIKTIGT: Hur förbättrar vi det härifrån? Den nuvarande implementeringen har vissa problem. För det första är det ganska riskabelt att skicka uppgifter så här om du inte åtminstone har HTTPS. Även då kan uppgifterna stjälas, så du behöver ett system där du enkelt kan återkalla token och lägga till ytterligare kontroller som var i världen den kommer ifrån, händer förfrågan för ofta (botliknande beteende), kort sagt, det finns en hel rad bekymmer.

Det bör dock sägas att för väldigt enkla API:er där du inte vill att någon ska anropa ditt API utan att vara autentiserad är det vi har här en bra start.

Med det sagt, låt oss försöka stärka säkerheten lite genom att använda ett standardiserat format som JSON Web Token, även känt som JWT eller "JOT"-tokens.

## JSON Web Tokens, JWT

Så, vi försöker förbättra saker från att skicka mycket enkla uppgifter. Vilka är de direkta förbättringarna vi får genom att använda JWT?

- **Säkerhetsförbättringar**. Vid grundläggande auth skickar du användarnamn och lösenord som en base64-kodat token (eller skickar en API-nyckel) om och om igen vilket ökar risken. Med JWT skickar du ditt användarnamn och lösenord och får en token tillbaka och den är också tidsbegränsad vilket innebär att den kommer att gå ut. JWT låter dig enkelt använda finmaskig åtkomstkontroll med roller, scopes och behörigheter.
- **Statelessness och skalbarhet**. JWT är självständiga, de bär all användarinformation och eliminerar behovet av server-sidig sessionslagring. Token kan också valideras lokalt.
- **Interoperabilitet och federation**. JWT är central för Open ID Connect och används med kända identitetsleverantörer som Entra ID, Google Identity och Auth0. De gör det också möjligt att använda single sign-on och mycket mer vilket gör det företagsklassat.
- **Modularitet och flexibilitet**. JWT kan också användas med API-gateways som Azure API Management, NGINX med mer. Det stöder också användarautentiseringsscenarier och server-till-server-kommunikation inklusive impersonering och delegation.
- **Prestanda och caching**. JWT kan cachas efter avkodning vilket minskar behovet av parsing. Detta hjälper särskilt med appar med hög trafik då det förbättrar genomströmningen och minskar belastningen på din valda infrastruktur.
- **Avancerade funktioner**. Det stöder också introspektion (kontrollera giltighet på server) och återkallelse (göra en token ogiltig).

Med alla dessa fördelar, låt oss se hur vi kan ta vår implementation till nästa nivå.

## Göra om basic auth till JWT

Så, förändringarna vi behöver på hög nivå är att:

- **Lära oss att konstruera en JWT-token** och göra den redo att skickas från klient till server.
- **Validera en JWT-token**, och om giltig, låta klienten få tillgång till våra resurser.
- **Säker lagring av token**. Hur vi lagrar denna token.
- **Skydda routar**. Vi behöver skydda routarna, i vårt fall behöver vi skydda routar och specifika MCP-funktioner.
- **Lägg till refresh tokens**. Säkerställ att vi skapar tokens som är kortlivade men refresh tokens som är långlivade som kan användas för att införskaffa nya tokens om de går ut. Säkerställ också att det finns en refresh endpoint och en rotationsstrategi.

### -1- Konstruera en JWT-token

Först har en JWT-token följande delar:

- **header**, vilken algoritm som används och token-typ.
- **payload**, claims, som sub (den användare eller entitet token representerar. I ett auth-scenario är detta typiskt userid), exp (när den går ut) roll (rollen).
- **signature**, signerad med en hemlighet eller privat nyckel.

För detta behöver vi konstruera headern, payload och den kodade tokenen.

**Python**

```python

import jwt
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import datetime

# Hemligt nyckel som används för att signera JWT
secret_key = 'your-secret-key'

header = {
    "alg": "HS256",
    "typ": "JWT"
}

# användarinformationen och dess påståenden och utgångstid
payload = {
    "sub": "1234567890",               # Ämne (användar-ID)
    "name": "User Userson",                # Egen anmärkning
    "admin": True,                     # Egen anmärkning
    "iat": datetime.datetime.utcnow(),# Utfärdat vid
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Utgång
}

# koda den
encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256", headers=header)
```

I ovanstående kod har vi:

- Definierat en header med HS256 som algoritm och typ JWT.
- Konstruerat en payload som innehåller ett subject eller user id, användarnamn, roll, när den utfärdades och när den ska gå ut och därmed implementerar den tidsbegränsade aspekten vi nämnde tidigare.

**TypeScript**

Här kommer vi behöva några beroenden som hjälper oss konstruera JWT-tokenen.

Beroenden

```sh

npm install jsonwebtoken
npm install --save-dev @types/jsonwebtoken
```

Nu när vi har det på plats, låt oss skapa header, payload och därigenom den kodade tokenen.

```typescript
import jwt from 'jsonwebtoken';

const secretKey = 'your-secret-key'; // Använd miljövariabler i produktion

// Definiera nyttolasten
const payload = {
  sub: '1234567890',
  name: 'User usersson',
  admin: true,
  iat: Math.floor(Date.now() / 1000), // Utfärdat vid
  exp: Math.floor(Date.now() / 1000) + 60 * 60 // Går ut om 1 timme
};

// Definiera headern (valfritt, jsonwebtoken sätter standardvärden)
const header = {
  alg: 'HS256',
  typ: 'JWT'
};

// Skapa token
const token = jwt.sign(payload, secretKey, {
  algorithm: 'HS256',
  header: header
});

console.log('JWT:', token);
```

Denna token är:

Signerad med HS256
Giltig i 1 timme
Inkluderar claims som sub, name, admin, iat och exp.

### -2- Validera en token

Vi kommer också behöva validera en token, detta är något vi bör göra på servern för att säkerställa att det klienten skickar faktiskt är giltigt. Det finns många kontroller vi bör göra här från att validera dess struktur till giltighet. Du uppmuntras också att lägga till andra kontroller för att se om användaren finns i ditt system med mera.

För att validera en token måste vi avkoda den så vi kan läsa den och sedan börja kontrollera dess giltighet:

**Python**

```python

# Avkoda och verifiera JWT
try:
    decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
    print("✅ Token is valid.")
    print("Decoded claims:")
    for key, value in decoded.items():
        print(f"  {key}: {value}")
except ExpiredSignatureError:
    print("❌ Token has expired.")
except InvalidTokenError as e:
    print(f"❌ Invalid token: {e}")

```

I denna kod anropar vi `jwt.decode` med token, hemlig nyckel och vald algoritm som indata. Notera hur vi använder try-catch eftersom en misslyckad validering leder till ett fel.

**TypeScript**

Här behöver vi anropa `jwt.verify` för att få en avkodad version av token som vi kan analysera vidare. Om detta anrop misslyckas betyder det att tokenens struktur är felaktig eller inte längre giltig.

```typescript

try {
  const decoded = jwt.verify(token, secretKey);
  console.log('Decoded Payload:', decoded);
} catch (err) {
  console.error('Token verification failed:', err);
}
```

OBS: som nämnt tidigare bör vi utföra ytterligare kontroller för att säkerställa att denna token pekar ut en användare i vårt system och säkerställa att användaren har de rättigheter som den hävdar.

Nästa, låt oss titta på rollbaserad åtkomstkontroll, även känt som RBAC.
## Lägga till rollbaserad åtkomstkontroll

Idén är att vi vill uttrycka att olika roller har olika behörigheter. Till exempel antar vi att en admin kan göra allt, en vanlig användare kan läsa/skriva och att en gäst bara kan läsa. Därför finns här några möjliga behörighetsnivåer:

- Admin.Write 
- User.Read
- Guest.Read

Låt oss titta på hur vi kan implementera en sådan kontroll med middleware. Middleware kan läggas till per rutt samt för alla rutter.

**Python**

```python
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import jwt

# HA INTE hemligheten i koden som detta, det är endast för demonstrationsändamål. Läs den från en säker plats.
SECRET_KEY = "your-secret-key" # lägg detta i en miljövariabel
REQUIRED_PERMISSION = "User.Read"

class JWTPermissionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse({"error": "Missing or invalid Authorization header"}, status_code=401)

        token = auth_header.split(" ")[1]
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return JSONResponse({"error": "Token expired"}, status_code=401)
        except jwt.InvalidTokenError:
            return JSONResponse({"error": "Invalid token"}, status_code=401)

        permissions = decoded.get("permissions", [])
        if REQUIRED_PERMISSION not in permissions:
            return JSONResponse({"error": "Permission denied"}, status_code=403)

        request.state.user = decoded
        return await call_next(request)


```

Det finns några olika sätt att lägga till middleware på som nedan:

```python

# Alt 1: lägg till middleware medan starlette-appen byggs
middleware = [
    Middleware(JWTPermissionMiddleware)
]

app = Starlette(routes=routes, middleware=middleware)

# Alt 2: lägg till middleware efter att starlette-appen redan är byggd
starlette_app.add_middleware(JWTPermissionMiddleware)

# Alt 3: lägg till middleware per rutt
routes = [
    Route(
        "/mcp",
        endpoint=..., # hanterare
        middleware=[Middleware(JWTPermissionMiddleware)]
    )
]
```

**TypeScript**

Vi kan använda `app.use` och en middleware som körs för alla förfrågningar. 

```typescript
app.use((req, res, next) => {
    console.log('Request received:', req.method, req.url, req.headers);
    console.log('Headers:', req.headers["authorization"]);

    // 1. Kontrollera om auktoriseringshuvudet har skickats

    if(!req.headers["authorization"]) {
        res.status(401).send('Unauthorized');
        return;
    }
    
    let token = req.headers["authorization"];

    // 2. Kontrollera om token är giltig
    if(!isValid(token)) {
        res.status(403).send('Forbidden');
        return;
    }  

    // 3. Kontrollera om tokenanvändaren finns i vårt system
    if(!isExistingUser(token)) {
        res.status(403).send('Forbidden');
        console.log("User does not exist");
        return;
    }
    console.log("User exists");

    // 4. Verifiera att token har rätt behörigheter
    if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }

    console.log("User has required scopes");

    console.log('Middleware executed');
    next();
});

```

Det är ganska många saker vi kan låta vår middleware göra och som vår middleware BÖR göra, nämligen:

1. Kontrollera om auktoriserings-header finns
2. Kontrollera om token är giltig, vi kallar `isValid` som är en metod vi skrivit som kontrollerar integriteten och giltigheten av JWT-token.
3. Verifiera att användaren finns i vårt system, detta bör vi kontrollera.

   ```typescript
    // användare i databasen
   const users = [
     "user1",
     "User usersson",
   ]

   function isExistingUser(token) {
     let decodedToken = verifyToken(token);

     // TODO, kontrollera om användaren finns i databasen
     return users.includes(decodedToken?.name || "");
   }
   ```

   Ovan har vi skapat en väldigt enkel lista `users`, som förstås borde finnas i en databas.

4. Dessutom bör vi också kontrollera att token har rätt behörigheter.

   ```typescript
   if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
   }
   ```

   I koden ovan från middleware kontrollerar vi att token innehåller User.Read behörighet, annars skickar vi en 403-felkod. Nedan är hjälpfunktionen `hasScopes`.

   ```typescript
   function hasScopes(scope: string, requiredScopes: string[]) {
     let decodedToken = verifyToken(scope);
    return requiredScopes.every(scope => decodedToken?.scopes.includes(scope));
  }
   ```

Have a think which additional checks you should be doing, but these are the absolute minimum of checks you should be doing.

Using Express as a web framework is a common choice. There are helpers library when you use JWT so you can write less code.

- `express-jwt`, helper library that provides a middleware that helps decode your token.
- `express-jwt-permissions`, this provides a middleware `guard` that helps check if a certain permission is on the token.

Here's what these libraries can look like when used:

```typescript
const express = require('express');
const jwt = require('express-jwt');
const guard = require('express-jwt-permissions')();

const app = express();
const secretKey = 'your-secret-key'; // put this in env variable

// Decode JWT and attach to req.user
app.use(jwt({ secret: secretKey, algorithms: ['HS256'] }));

// Check for User.Read permission
app.use(guard.check('User.Read'));

// multiple permissions
// app.use(guard.check(['User.Read', 'Admin.Access']));

app.get('/protected', (req, res) => {
  res.json({ message: `Welcome ${req.user.name}` });
});

// Error handler
app.use((err, req, res, next) => {
  if (err.code === 'permission_denied') {
    return res.status(403).send('Forbidden');
  }
  next(err);
});

```

Nu har du sett hur middleware kan användas både för autentisering och auktorisering, men hur är det med MCP? Ändrar det hur vi gör auth? Låt oss ta reda på det i nästa avsnitt.

### -3- Lägg till RBAC till MCP

Du har hittills sett hur du kan lägga till RBAC via middleware, men för MCP finns det inget enkelt sätt att lägga till per MCP-funktion RBAC, så vad gör vi? Jo, vi måste bara lägga till kod som i detta fall kontrollerar om klienten har rättigheter att anropa ett specifikt verktyg:

Du har några olika val på hur du kan åstadkomma per funktion RBAC, här är några:

- Lägg till en kontroll för varje verktyg, resurs, prompt där du behöver kontrollera behörighetsnivå.

   **python**

   ```python
   @tool()
   def delete_product(id: int):
      try:
          check_permissions(role="Admin.Write", request)
      catch:
        pass # klienten misslyckades med auktorisering, utlös auktoriseringsfel
   ```

   **typescript**

   ```typescript
   server.registerTool(
    "delete-product",
    {
      title: Delete a product",
      description: "Deletes a product",
      inputSchema: { id: z.number() }
    },
    async ({ id }) => {
      
      try {
        checkPermissions("Admin.Write", request);
        // todo, skicka id till productService och fjärrposten
      } catch(Exception e) {
        console.log("Authorization error, you're not allowed");  
      }

      return {
        content: [{ type: "text", text: `Deletected product with id ${id}` }]
      };
    }
   );
   ```


- Använd avancerad servermetod och request handlers så att du minimerar hur många ställen kontrollen behöver göras på.

   **Python**

   ```python
   
   tool_permission = {
      "create_product": ["User.Write", "Admin.Write"],
      "delete_product": ["Admin.Write"]
   }

   def has_permission(user_permissions, required_permissions) -> bool:
      # user_permissions: lista över behörigheter som användaren har
      # required_permissions: lista över behörigheter som krävs för verktyget
      return any(perm in user_permissions for perm in required_permissions)

   @server.call_tool()
   async def handle_call_tool(
     name: str, arguments: dict[str, str] | None
   ) -> list[types.TextContent]:
    # Anta att request.user.permissions är en lista över behörigheter för användaren
     user_permissions = request.user.permissions
     required_permissions = tool_permission.get(name, [])
     if not has_permission(user_permissions, required_permissions):
        # Kasta fel "Du har inte behörighet att kalla på verktyget {name}"
        raise Exception(f"You don't have permission to call tool {name}")
     # fortsätt och kalla på verktyget
     # ...
   ```   
   

   **TypeScript**

   ```typescript
   function hasPermission(userPermissions: string[], requiredPermissions: string[]): boolean {
       if (!Array.isArray(userPermissions) || !Array.isArray(requiredPermissions)) return false;
       // Returnera sant om användaren har minst en av de nödvändiga behörigheterna
       
       return requiredPermissions.some(perm => userPermissions.includes(perm));
   }
  
   server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { params: { name } } = request;
  
      let permissions = request.user.permissions;
  
      if (!hasPermission(permissions, toolPermissions[name])) {
         return new Error(`You don't have permission to call ${name}`);
      }
  
      // fortsätt..
   });
   ```

   Observera att du behöver säkerställa att din middleware tilldelar en avkodad token till request.user egenskapen så att koden ovan blir enkel.

### Sammanfattning

Nu när vi har diskuterat hur man lägger till stöd för RBAC i allmänhet och för MCP i synnerhet, är det dags att försöka implementera säkerhet på egen hand för att säkerställa att du förstår de koncept som presenterats.

## Uppgift 1: Bygg en MCP-server och MCP-klient med grundläggande autentisering

Här ska du tillämpa det du lärt dig när det gäller att skicka inloggningsuppgifter via headers.

## Lösning 1

[Lösning 1](./code/basic/README.md)

## Uppgift 2: Uppgradera lösningen från Uppgift 1 för att använda JWT

Ta den första lösningen men förbättra den denna gång. 

Istället för att använda Basic Auth, låt oss använda JWT.

## Lösning 2

[Lösning 2](./solution/jwt-solution/README.md)

## Utmaning

Lägg till RBAC per verktyg som vi beskrev i avsnittet "Lägg till RBAC till MCP".

## Sammanfattning

Du har förhoppningsvis lärt dig mycket i detta kapitel, från ingen säkerhet alls, till grundläggande säkerhet, till JWT och hur det kan läggas till MCP.

Vi har byggt en solid grund med anpassade JWT, men när vi växer skiftar vi mot en standardbaserad identitetsmodell. Att adoptera en IdP som Entra eller Keycloak låter oss överlåta utfärdande, validering och livscykelhantering av tokens till en betrodd plattform — vilket frigör oss att fokusera på applikationslogik och användarupplevelse.

För det har vi ett mer [avancerat kapitel om Entra](../../05-AdvancedTopics/mcp-security-entra/README.md)

## Vad händer härnäst

- Nästa: [Ställa in MCP Hosts](../12-mcp-hosts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör anses vara den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->