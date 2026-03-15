# Autenticazione semplice

Gli SDK MCP supportano l'uso di OAuth 2.1 che, a dire il vero, è un processo piuttosto complesso che coinvolge concetti come server di autenticazione, server di risorse, invio delle credenziali, ottenimento di un codice, scambio del codice per un token bearer fino a quando finalmente si possono ottenere i dati della risorsa. Se non sei abituato a OAuth, che è una cosa ottima da implementare, è una buona idea iniziare con un livello base di autenticazione e aumentare progressivamente la sicurezza. Ecco perché esiste questo capitolo, per portarti a un'autenticazione più avanzata.

## Autenticazione, cosa intendiamo?

Auth è l'abbreviazione di autenticazione e autorizzazione. L'idea è che dobbiamo fare due cose:

- **Autenticazione**, che è il processo di capire se lasciamo entrare una persona nella nostra casa, che ha il diritto di essere "qui", cioè di avere accesso al nostro server di risorse dove risiedono le funzionalità del nostro MCP Server.
- **Autorizzazione**, è il processo di scoprire se un utente dovrebbe avere accesso a queste risorse specifiche che sta richiedendo, ad esempio questi ordini o questi prodotti, o se è autorizzato a leggere il contenuto ma non a cancellarlo, come altro esempio.

## Credenziali: come diciamo al sistema chi siamo

Beh, la maggior parte degli sviluppatori web pensa in termini di fornire una credenziale al server, di solito un segreto che dice se gli è permesso di essere qui, l'"Autenticazione". Questa credenziale è solitamente una versione codificata base64 di username e password o una chiave API che identifica un utente specifico.

Questo implica inviarla tramite un header chiamato "Authorization" in questo modo:

```json
{ "Authorization": "secret123" }
```

Questo è solitamente definito autenticazione base. Poi il flusso complessivo funziona nel modo seguente:

```mermaid
sequenceDiagram
   participant User
   participant Client
   participant Server

   User->>Client: mostrami i dati
   Client->>Server: mostrami i dati, ecco le mie credenziali
   Server-->>Client: 1a, ti conosco, ecco i tuoi dati
   Server-->>Client: 1b, non ti conosco, 401 
```
Ora che abbiamo capito come funziona dal punto di vista del flusso, come lo implementiamo? Beh, la maggior parte dei web server ha un concetto chiamato middleware, un pezzo di codice che viene eseguito come parte della richiesta e può verificare le credenziali, e se sono valide può far passare la richiesta. Se la richiesta non ha credenziali valide, ottieni un errore di autenticazione. Vediamo come può essere implementato:

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
        # aggiungi eventuali intestazioni cliente o modifica in qualche modo la risposta
        return response


starlette_app.add_middleware(CustomHeaderMiddleware)
```

Qui abbiamo:

- Creato un middleware chiamato `AuthMiddleware` dove il suo metodo `dispatch` viene invocato dal web server.
- Aggiunto il middleware al web server:

    ```python
    starlette_app.add_middleware(AuthMiddleware)
    ```

- Scritto la logica di convalida che verifica se l'header Authorization è presente e se il segreto inviato è valido:

    ```python
    has_header = request.headers.get("Authorization")
    if not has_header:
        print("-> Missing Authorization header!")
        return Response(status_code=401, content="Unauthorized")

    if not valid_token(has_header):
        print("-> Invalid token!")
        return Response(status_code=403, content="Forbidden")
    ```

    se il segreto è presente e valido allora lasciamo passare la richiesta chiamando `call_next` e restituiamo la risposta.

    ```python
    response = await call_next(request)
    # aggiungere eventuali intestazioni cliente o modificare in qualche modo la risposta
    return response
    ```

Come funziona è che se viene effettuata una richiesta web verso il server, il middleware verrà invocato e, dato il suo comportamento, o farà passare la richiesta oppure restituirà un errore che indica che il client non è autorizzato a procedere.

**TypeScript**

Qui creiamo un middleware con il popolare framework Express e intercettiamo la richiesta prima che raggiunga il MCP Server. Ecco il codice:

```typescript
function isValid(secret) {
    return secret === "secret123";
}

app.use((req, res, next) => {
    // 1. Header di autorizzazione presente?
    if(!req.headers["Authorization"]) {
        res.status(401).send('Unauthorized');
    }
    
    let token = req.headers["Authorization"];

    // 2. Verifica validità.
    if(!isValid(token)) {
        res.status(403).send('Forbidden');
    }

   
    console.log('Middleware executed');
    // 3. Passa la richiesta al passaggio successivo nella pipeline di richiesta.
    next();
});
```

In questo codice:

1. Controlliamo se l'header Authorization è presente, se no, inviamo un errore 401.
2. Assicuriamo che la credenziale/token sia valida, se no inviamo un errore 403.
3. Infine lasciamo passare la richiesta nella pipeline e restituiamo la risorsa richiesta.

## Esercizio: Implementare l'autenticazione

Mettiamo alla prova la nostra conoscenza implementandola. Ecco il piano:

Server

- Creare un web server e un'istanza MCP.
- Implementare un middleware per il server.

Client

- Inviare una richiesta web, con credenziale, tramite header.

### -1- Creare un web server e un'istanza MCP

Nel primo passo, dobbiamo creare l'istanza del web server e l'MCP Server.

**Python**

Qui creiamo un'istanza di MCP server, creiamo un'app starlette web e la ospitiamo con uvicorn.

```python
# creazione del server MCP

app = FastMCP(
    name="MCP Resource Server",
    instructions="Resource Server that validates tokens via Authorization Server introspection",
    host=settings["host"],
    port=settings["port"],
    debug=True
)

# creazione dell'app web starlette
starlette_app = app.streamable_http_app()

# servizio dell'app tramite uvicorn
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

In questo codice:

- Creiamo il MCP Server.
- Costruiamo l'app web starlette dall'MCP Server, `app.streamable_http_app()`.
- Ospitiamo e serviamo l'app web usando uvicorn `server.serve()`.

**TypeScript**

Qui creiamo un'istanza di MCP Server.

```typescript
const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    });

    // ... configurare risorse server, strumenti e prompt ...
```

Questa creazione del MCP Server dovrà avvenire all'interno della definizione del route POST /mcp, quindi prendiamo il codice sopra e lo spostiamo così:

```typescript
import express from "express";
import { randomUUID } from "node:crypto";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { isInitializeRequest } from "@modelcontextprotocol/sdk/types.js"

const app = express();
app.use(express.json());

// Mappa per memorizzare i trasporti per ID sessione
const transports: { [sessionId: string]: StreamableHTTPServerTransport } = {};

// Gestisci le richieste POST per la comunicazione da client a server
app.post('/mcp', async (req, res) => {
  // Controlla l'ID sessione esistente
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  let transport: StreamableHTTPServerTransport;

  if (sessionId && transports[sessionId]) {
    // Riutilizza il trasporto esistente
    transport = transports[sessionId];
  } else if (!sessionId && isInitializeRequest(req.body)) {
    // Nuova richiesta di inizializzazione
    transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: () => randomUUID(),
      onsessioninitialized: (sessionId) => {
        // Memorizza il trasporto per ID sessione
        transports[sessionId] = transport;
      },
      // La protezione dal rebinding DNS è disattivata di default per compatibilità con versioni precedenti. Se stai eseguendo questo server
      // localmente, assicurati di impostare:
      // enableDnsRebindingProtection: true,
      // allowedHosts: ['127.0.0.1'],
    });

    // Pulisci il trasporto quando viene chiuso
    transport.onclose = () => {
      if (transport.sessionId) {
        delete transports[transport.sessionId];
      }
    };
    const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    });

    // ... configura risorse, strumenti e prompt del server ...

    // Connetti al server MCP
    await server.connect(transport);
  } else {
    // Richiesta non valida
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

  // Gestisci la richiesta
  await transport.handleRequest(req, res, req.body);
});

// Gestore riutilizzabile per richieste GET e DELETE
const handleSessionRequest = async (req: express.Request, res: express.Response) => {
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  if (!sessionId || !transports[sessionId]) {
    res.status(400).send('Invalid or missing session ID');
    return;
  }
  
  const transport = transports[sessionId];
  await transport.handleRequest(req, res);
};

// Gestisci le richieste GET per notifiche server-to-client tramite SSE
app.get('/mcp', handleSessionRequest);

// Gestisci le richieste DELETE per la terminazione della sessione
app.delete('/mcp', handleSessionRequest);

app.listen(3000);
```

Ora vedi come la creazione del MCP Server sia stata spostata all'interno di `app.post("/mcp")`.

Procediamo al passo successivo di creare il middleware in modo da poter validare la credenziale in arrivo.

### -2- Implementare un middleware per il server

Passiamo ora alla parte del middleware. Qui creeremo un middleware che cerca una credenziale nell'header `Authorization` e la valida. Se è accettabile, la richiesta procederà per fare ciò che deve (es. elencare strumenti, leggere una risorsa o qualunque funzionalità MCP il client stesse richiedendo).

**Python**

Per creare il middleware, dobbiamo creare una classe che eredita da `BaseHTTPMiddleware`. Ci sono due pezzi interessanti:

- La richiesta `request`, da cui leggiamo le info degli header.
- `call_next`, la callback che dobbiamo invocare se il client ha fornito una credenziale che accettiamo.

Prima, dobbiamo gestire il caso in cui l'header `Authorization` è mancante:

```python
has_header = request.headers.get("Authorization")

# nessun header presente, fallire con 401, altrimenti procedere.
if not has_header:
    print("-> Missing Authorization header!")
    return Response(status_code=401, content="Unauthorized")
```

Qui inviamo un messaggio 401 non autorizzato perché il client fallisce l'autenticazione.

Poi, se è stata fornita una credenziale, dobbiamo verificarne la validità così:

```python
 if not valid_token(has_header):
    print("-> Invalid token!")
    return Response(status_code=403, content="Forbidden")
```

Nota come qui inviamo un messaggio 403 proibito. Vediamo il middleware completo sotto che implementa tutto quanto sopra:

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

Ottimo, ma che fine fa la funzione `valid_token`? Eccola qui sotto:
:

```python
# NON usare in produzione - miglioralo !!
def valid_token(token: str) -> bool:
    # rimuovi il prefisso "Bearer "
    if token.startswith("Bearer "):
        token = token[7:]
        return token == "secret-token"
    return False
```

Ovviamente dovrebbe essere migliorata.

IMPORTANTE: Non dovresti MAI avere segreti come questo nel codice. Idealmente dovresti recuperare il valore da confrontare da una fonte dati o da un IDP (provider di identità) o meglio ancora, lasciare che l'IDP faccia la validazione.

**TypeScript**

Per implementare questo con Express, dobbiamo chiamare il metodo `use` che accetta funzioni middleware.

Dobbiamo:

- Interagire con la variabile request per controllare la credenziale passata nella proprietà `Authorization`.
- Validare la credenziale e, in caso affermativo, lasciare che la richiesta continui e permetta alla richiesta MCP del client di fare ciò che deve (esempio: listare strumenti, leggere risorsa o altro MCP correlato).

Qui controlliamo se l'header `Authorization` è presente e in caso contrario blocchiamo la richiesta:

```typescript
if(!req.headers["authorization"]) {
    res.status(401).send('Unauthorized');
    return;
}
```

Se l'header non è inviato, ricevi un 401.

Poi verifichiamo se la credenziale è valida, se no blocchiamo di nuovo con un messaggio diverso:

```typescript
if(!isValid(token)) {
    res.status(403).send('Forbidden');
    return;
} 
```

Nota come ora ricevi un errore 403.

Ecco il codice completo:

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

Abbiamo configurato il web server per accettare un middleware che controlla la credenziale che il client ci invia. E il client?

### -3- Inviare richiesta web con credenziale tramite header

Dobbiamo assicurarci che il client stia passando la credenziale nell'header. Poiché useremo un client MCP per farlo, dobbiamo capire come si fa.

**Python**

Per il client, dobbiamo passare un header con la credenziale così:

```python
# NON inserire il valore in modo fisso, tienilo almeno in una variabile d'ambiente o in una memoria più sicura
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
      
            # DA FARE, cosa vuoi che venga fatto nel client, per esempio elencare strumenti, chiamare strumenti ecc.
```

Nota come qui impostiamo la proprietà `headers` così: ` headers = {"Authorization": f"Bearer {token}"}`.

**TypeScript**

Possiamo risolvere in due passi:

1. Popolare un oggetto di configurazione con la nostra credenziale.
2. Passare l'oggetto di configurazione al trasporto.

```typescript

// NON inserire direttamente il valore come mostrato qui. Al minimo, usalo come variabile d'ambiente e utilizza qualcosa come dotenv (in modalità sviluppo).
let token = "secret123"

// definire un oggetto opzioni di trasporto client
let options: StreamableHTTPClientTransportOptions = {
  sessionId: sessionId,
  requestInit: {
    headers: {
      "Authorization": "secret123"
    }
  }
};

// passare l'oggetto opzioni al trasporto
async function main() {
   const transport = new StreamableHTTPClientTransport(
      new URL(serverUrl),
      options
   );
```

Qui vedi come abbiamo creato un oggetto `options` e abbiamo inserito gli header nella proprietà `requestInit`.

IMPORTANTE: Come migliorarlo da qui? Beh, l'implementazione attuale ha alcuni problemi. In primo luogo, passare una credenziale così è piuttosto rischioso a meno che non si usi almeno HTTPS. Anche così, la credenziale può essere rubata quindi serve un sistema dove sia facile revocare il token e aggiungere controlli come da dove nel mondo proviene, se le richieste avvengono troppo spesso (comportamento da bot), insomma, ci sono tante preoccupazioni.

Detto questo, per API molto semplici dove non vuoi che chiunque chiami la tua API senza essere autenticato, ciò che abbiamo qui è un buon inizio.

Detto ciò, cerchiamo di rafforzare un po' la sicurezza usando un formato standardizzato come JSON Web Token, noto anche come JWT o "JOT" token.

## JSON Web Token, JWT

Quindi, stiamo cercando di migliorare rispetto all'invio di credenziali molto semplici. Quali sono gli immediati miglioramenti ottenibili con l'adozione di JWT?

- **Miglioramenti di sicurezza**. Nell'autenticazione base, invii username e password come token codificato base64 (o una chiave API) continuamente, aumentando il rischio. Con JWT, invii username e password e ricevi in cambio un token, inoltre è legato al tempo quindi scade. JWT ti permette di usare facilmente un controllo accessi granulare con ruoli, scope e permessi.
- **Statelessness e scalabilità**. I JWT sono self-contained, trasportano tutte le info utente ed eliminano la necessità di memorizzazione server-side di sessioni. Il token può anche essere validato localmente.
- **Interoperabilità e federazione**. I JWT sono centrali in Open ID Connect e sono usati con provider di identità noti come Entra ID, Google Identity e Auth0. Rendono possibile single sign-on e molto altro rendendoli enterprise-grade.
- **Modularità e flessibilità**. I JWT possono essere usati con API Gateway come Azure API Management, NGINX e altri. Supportano scenari di autenticazione e comunicazione server-to-service inclusi scenari di impersonificazione e delega.
- **Prestazioni e caching**. I JWT possono essere memorizzati in cache dopo la decodifica riducendo la necessità di parsing, utile per app ad alto traffico migliorando il throughput e riducendo il carico sull'infrastruttura scelta.
- **Funzionalità avanzate**. Supportano anche introspezione (verifica di validità sul server) e revoca (rendere un token invalido).

Con tutti questi benefici, vediamo come portare la nostra implementazione al livello successivo.

## Trasformare l'autenticazione base in JWT

Quindi, i cambiamenti a livello molto alto sono:

- **Imparare a costruire un token JWT** e prepararlo per essere inviato da client a server.
- **Validare un token JWT**, e se valido, permettere al client di accedere alle nostre risorse.
- **Conservazione sicura del token**. Come conserviamo questo token.
- **Proteggere le rotte**. Dobbiamo proteggere le rotte e specifiche funzionalità MCP.
- **Aggiungere refresh token**. Assicurarci di creare token a breve durata ma refresh token a lunga durata da usare per acquisire nuovi token se scadono. Assicurarsi che ci sia un endpoint di refresh e una strategia di rotazione.

### -1- Costruire un token JWT

Prima di tutto, un token JWT ha queste parti:

- **header**, algoritmo usato e tipo token.
- **payload**, claims, come sub (l’utente o entità che il token rappresenta, tipicamente userid in uno scenario auth), exp (scadenza), role (ruolo)
- **signature**, firmata con un segreto o chiave privata.

Per questo, dobbiamo costruire header, payload e token codificato.

**Python**

```python

import jwt
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import datetime

# Chiave segreta usata per firmare il JWT
secret_key = 'your-secret-key'

header = {
    "alg": "HS256",
    "typ": "JWT"
}

# le informazioni dell'utente, le sue rivendicazioni e il tempo di scadenza
payload = {
    "sub": "1234567890",               # Soggetto (ID utente)
    "name": "User Userson",                # Rivendicazione personalizzata
    "admin": True,                     # Rivendicazione personalizzata
    "iat": datetime.datetime.utcnow(),# Emesso il
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Scadenza
}

# codificalo
encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256", headers=header)
```

Nel codice sopra abbiamo:

- Definito un header usando HS256 come algoritmo e il tipo JWT.
- Costruito un payload contenente un soggetto o user id, username, ruolo, quando è stato emesso e quando scade, implementando l'aspetto legato al tempo di cui abbiamo parlato prima.

**TypeScript**

Qui avremo bisogno di alcune dipendenze che ci aiutano a costruire il token JWT.

Dipendenze

```sh

npm install jsonwebtoken
npm install --save-dev @types/jsonwebtoken
```

Ora che abbiamo questo, creiamo header, payload e attraverso questi creiamo il token codificato.

```typescript
import jwt from 'jsonwebtoken';

const secretKey = 'your-secret-key'; // Usa le variabili d'ambiente in produzione

// Definisci il payload
const payload = {
  sub: '1234567890',
  name: 'User usersson',
  admin: true,
  iat: Math.floor(Date.now() / 1000), // Emesso a
  exp: Math.floor(Date.now() / 1000) + 60 * 60 // Scade tra 1 ora
};

// Definisci l'intestazione (opzionale, jsonwebtoken imposta i valori predefiniti)
const header = {
  alg: 'HS256',
  typ: 'JWT'
};

// Crea il token
const token = jwt.sign(payload, secretKey, {
  algorithm: 'HS256',
  header: header
});

console.log('JWT:', token);
```

Questo token è:

Firmato usando HS256
Valido per 1 ora
Include claims come sub, name, admin, iat, ed exp.

### -2- Validare un token

Dobbiamo anche validare un token; questo è qualcosa da fare sul server per assicurarci che ciò che il client ci sta inviando sia effettivamente valido. Ci sono molti controlli da fare, dalla validazione della struttura alla validità. Sei anche incoraggiato ad aggiungere altri controlli per verificare se l'utente è nel tuo sistema e altro.

Per validare un token, dobbiamo decodificarlo così da poterlo leggere e poi iniziare a controllarne la validità:

**Python**

```python

# Decodifica e verifica il JWT
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

In questo codice chiamiamo `jwt.decode` usando il token, la chiave segreta e l'algoritmo scelto come input. Nota come usiamo un blocco try-catch perché una validazione fallita porta a un'eccezione.

**TypeScript**

Qui dobbiamo chiamare `jwt.verify` per ottenere una versione decodificata del token che possiamo analizzare. Se questa chiamata fallisce, significa che la struttura del token è errata o non è più valido.

```typescript

try {
  const decoded = jwt.verify(token, secretKey);
  console.log('Decoded Payload:', decoded);
} catch (err) {
  console.error('Token verification failed:', err);
}
```

NOTA: come detto prima, dobbiamo fare controlli aggiuntivi per accertarci che questo token rappresenti un utente nel nostro sistema e che l'utente abbia i diritti che dichiara di avere.

Passiamo ora a guardare il controllo accessi basato sui ruoli, conosciuto anche come RBAC.
## Aggiunta del controllo degli accessi basato sui ruoli

L'idea è che vogliamo esprimere che ruoli diversi hanno permessi diversi. Per esempio, assumiamo che un amministratore possa fare tutto, che un utente normale possa leggere/scrivere e che un ospite possa solo leggere. Pertanto, ecco alcuni possibili livelli di permessi:

- Admin.Write 
- User.Read
- Guest.Read

Vediamo come possiamo implementare tale controllo con il middleware. I middleware possono essere aggiunti per percorso specifico così come per tutti i percorsi.

**Python**

```python
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import jwt

# NON mettere il segreto nel codice come questo, è solo a scopo dimostrativo. Leggilo da un posto sicuro.
SECRET_KEY = "your-secret-key" # metti questo in una variabile d'ambiente
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

Ci sono diversi modi per aggiungere il middleware come sotto:

```python

# Alt 1: aggiungi middleware durante la costruzione dell'app starlette
middleware = [
    Middleware(JWTPermissionMiddleware)
]

app = Starlette(routes=routes, middleware=middleware)

# Alt 2: aggiungi middleware dopo che l'app starlette è già stata costruita
starlette_app.add_middleware(JWTPermissionMiddleware)

# Alt 3: aggiungi middleware per rotta
routes = [
    Route(
        "/mcp",
        endpoint=..., # gestore
        middleware=[Middleware(JWTPermissionMiddleware)]
    )
]
```

**TypeScript**

Possiamo usare `app.use` e un middleware che verrà eseguito per tutte le richieste.

```typescript
app.use((req, res, next) => {
    console.log('Request received:', req.method, req.url, req.headers);
    console.log('Headers:', req.headers["authorization"]);

    // 1. Verifica se l'intestazione di autorizzazione è stata inviata

    if(!req.headers["authorization"]) {
        res.status(401).send('Unauthorized');
        return;
    }
    
    let token = req.headers["authorization"];

    // 2. Verifica se il token è valido
    if(!isValid(token)) {
        res.status(403).send('Forbidden');
        return;
    }  

    // 3. Verifica se l'utente del token esiste nel nostro sistema
    if(!isExistingUser(token)) {
        res.status(403).send('Forbidden');
        console.log("User does not exist");
        return;
    }
    console.log("User exists");

    // 4. Verifica che il token abbia le autorizzazioni corrette
    if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }

    console.log("User has required scopes");

    console.log('Middleware executed');
    next();
});

```

Ci sono parecchie cose che possiamo lasciare al nostro middleware e che il nostro middleware DOVREBBE fare, ovvero:

1. Controllare se l'intestazione di autorizzazione è presente
2. Controllare se il token è valido, chiamiamo `isValid` che è un metodo che abbiamo scritto per verificare l'integrità e la validità del token JWT.
3. Verificare che l'utente esista nel nostro sistema, dovremmo controllare questo.

   ```typescript
    // utenti nel DB
   const users = [
     "user1",
     "User usersson",
   ]

   function isExistingUser(token) {
     let decodedToken = verifyToken(token);

     // DA FARE, controlla se l'utente esiste nel DB
     return users.includes(decodedToken?.name || "");
   }
   ```

   Sopra, abbiamo creato una lista molto semplice `users`, che ovviamente dovrebbe essere in un database.

4. Inoltre, dovremmo anche controllare che il token abbia i permessi corretti.

   ```typescript
   if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
   }
   ```

   In questo codice sopra dal middleware, controlliamo che il token contenga il permesso User.Read, altrimenti inviamo un errore 403. Di seguito c'è il metodo helper `hasScopes`.

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

Ora hai visto come il middleware può essere usato sia per l'autenticazione che per l'autorizzazione, ma per quanto riguarda MCP, cambia il modo in cui facciamo l’autenticazione? Scopriamolo nella prossima sezione.

### -3- Aggiungere RBAC a MCP

Finora hai visto come è possibile aggiungere RBAC tramite middleware, tuttavia, per MCP non c’è un modo semplice per aggiungere RBAC per singola funzionalità MCP, quindi cosa facciamo? Beh, dobbiamo semplicemente aggiungere codice come questo che verifica in questo caso se il client ha i diritti per chiamare uno specifico strumento:

Hai alcune diverse opzioni su come realizzare RBAC per singola funzionalità, eccone alcune:

- Aggiungere un controllo per ogni strumento, risorsa, prompt dove è necessario verificare il livello di permesso.

   **python**

   ```python
   @tool()
   def delete_product(id: int):
      try:
          check_permissions(role="Admin.Write", request)
      catch:
        pass # il client non è riuscito all'autorizzazione, genera errore di autorizzazione
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
        // da fare, inviare l'id a productService e remote entry
      } catch(Exception e) {
        console.log("Authorization error, you're not allowed");  
      }

      return {
        content: [{ type: "text", text: `Deletected product with id ${id}` }]
      };
    }
   );
   ```


- Usare un approccio server avanzato e i gestori delle richieste in modo da minimizzare i posti in cui devi effettuare il controllo.

   **Python**

   ```python
   
   tool_permission = {
      "create_product": ["User.Write", "Admin.Write"],
      "delete_product": ["Admin.Write"]
   }

   def has_permission(user_permissions, required_permissions) -> bool:
      # user_permissions: elenco delle autorizzazioni che l'utente ha
      # required_permissions: elenco delle autorizzazioni richieste per lo strumento
      return any(perm in user_permissions for perm in required_permissions)

   @server.call_tool()
   async def handle_call_tool(
     name: str, arguments: dict[str, str] | None
   ) -> list[types.TextContent]:
    # Assumere che request.user.permissions sia un elenco di autorizzazioni per l'utente
     user_permissions = request.user.permissions
     required_permissions = tool_permission.get(name, [])
     if not has_permission(user_permissions, required_permissions):
        # Solleva errore "Non hai il permesso di chiamare lo strumento {name}"
        raise Exception(f"You don't have permission to call tool {name}")
     # continua e chiama lo strumento
     # ...
   ```   
   

   **TypeScript**

   ```typescript
   function hasPermission(userPermissions: string[], requiredPermissions: string[]): boolean {
       if (!Array.isArray(userPermissions) || !Array.isArray(requiredPermissions)) return false;
       // Restituisce true se l'utente ha almeno un permesso richiesto
       
       return requiredPermissions.some(perm => userPermissions.includes(perm));
   }
  
   server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { params: { name } } = request;
  
      let permissions = request.user.permissions;
  
      if (!hasPermission(permissions, toolPermissions[name])) {
         return new Error(`You don't have permission to call ${name}`);
      }
  
      // continua..
   });
   ```

   Nota, dovrai assicurarti che il tuo middleware assegni un token decodificato alla proprietà user della richiesta in modo che il codice sopra sia semplice.

### Riepilogo

Ora che abbiamo discusso come aggiungere il supporto per RBAC in generale e per MCP in particolare, è tempo di provare a implementare la sicurezza da solo per assicurarti di aver compreso i concetti presentati.

## Compito 1: Costruire un server MCP e un client MCP usando l'autenticazione base

Qui metterai in pratica ciò che hai imparato riguardo all’invio delle credenziali tramite intestazioni.

## Soluzione 1

[Solution 1](./code/basic/README.md)

## Compito 2: Migliorare la soluzione del Compito 1 usando JWT

Prendi la prima soluzione, ma questa volta miglioriamola.

Invece di usare Basic Auth, usiamo JWT.

## Soluzione 2

[Solution 2](./solution/jwt-solution/README.md)

## Sfida

Aggiungi RBAC per ogni strumento come descritto nella sezione "Aggiungere RBAC a MCP".

## Sommario

Spero tu abbia imparato molto in questo capitolo, dalla totale assenza di sicurezza, alla sicurezza di base, fino a JWT e a come può essere aggiunta a MCP.

Abbiamo costruito una solida base con JWT personalizzati, ma man mano che cresciamo ci stiamo muovendo verso un modello di identità basato su standard. Adottare un IdP come Entra o Keycloak ci permette di delegare l’emissione, la validazione e la gestione del ciclo di vita dei token a una piattaforma affidabile, liberandoci per concentrarci sulla logica dell’app e sull’esperienza utente.

Per questo, abbiamo un capitolo più [avanzato su Entra](../../05-AdvancedTopics/mcp-security-entra/README.md)

## Cosa c’è dopo

- Prossimo: [Configurazione degli host MCP](../12-mcp-hosts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->