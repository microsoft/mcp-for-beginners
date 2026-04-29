# Autenticazione semplice

Gli SDK MCP supportano l'uso di OAuth 2.1 che, a dire il vero, è un processo abbastanza complesso che coinvolge concetti come server di autenticazione, server delle risorse, invio delle credenziali, ottenimento di un codice, scambio del codice per un token bearer fino a quando finalmente si possono ottenere i dati della risorsa. Se non sei abituato a OAuth, cosa ottima da implementare, è una buona idea iniziare con un livello base di autenticazione e costruire una sicurezza sempre migliore. Ecco perché esiste questo capitolo, per farti crescere fino ad autenticazioni più avanzate.

## Autenticazione, cosa intendiamo?

Auth è l'abbreviazione di autenticazione e autorizzazione. L'idea è che dobbiamo fare due cose:

- **Autenticazione**, che è il processo di capire se lasciamo entrare una persona in casa nostra, se ha il diritto di essere "qui", cioè avere accesso al nostro server delle risorse dove vivono le funzionalità del nostro MCP Server.
- **Autorizzazione**, è il processo di verificare se un utente dovrebbe avere accesso a queste specifiche risorse che sta chiedendo, per esempio questi ordini o questi prodotti o se è consentito leggere il contenuto ma non cancellarlo, come altro esempio.

## Credenziali: come diciamo al sistema chi siamo

Beh, la maggior parte degli sviluppatori web inizia pensando in termini di fornire un'identità al server, solitamente un segreto che dice se sono autorizzati ad essere qui "Autenticazione". Questa credenziale è di solito una versione codificata in base64 di nome utente e password oppure una API key che identifica un utente specifico.

Questo comporta l'invio tramite un header chiamato "Authorization" così:

```json
{ "Authorization": "secret123" }
```

Questo è solitamente chiamato autenticazione basic. Come funziona il flusso nel complesso è nel modo seguente:

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
Ora che abbiamo capito il funzionamento dal punto di vista del flusso, come lo implementiamo? Beh, la maggior parte dei server web ha un concetto chiamato middleware, un pezzo di codice che gira come parte della richiesta che può verificare le credenziali e, se valide, lascia passare la richiesta. Se la richiesta non ha credenziali valide si ottiene un errore di autenticazione. Vediamo come si può implementare:

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
        # aggiungi eventuali intestazioni personalizzate o modifica la risposta in qualche modo
        return response


starlette_app.add_middleware(CustomHeaderMiddleware)
```

Qui abbiamo:

- Creato un middleware chiamato `AuthMiddleware` in cui il metodo `dispatch` viene invocato dal server web.
- Aggiunto il middleware al server web:

    ```python
    starlette_app.add_middleware(AuthMiddleware)
    ```

- Scritto una logica di validazione che controlla se l'header Authorization è presente e se il segreto inviato è valido:

    ```python
    has_header = request.headers.get("Authorization")
    if not has_header:
        print("-> Missing Authorization header!")
        return Response(status_code=401, content="Unauthorized")

    if not valid_token(has_header):
        print("-> Invalid token!")
        return Response(status_code=403, content="Forbidden")
    ```

    se il segreto è presente e valido, allora lasciamo passare la richiesta chiamando `call_next` e restituiamo la risposta.

    ```python
    response = await call_next(request)
    # aggiungi eventuali intestazioni personalizzate o modifica la risposta in qualche modo
    return response
    ```

Come funziona è che se una richiesta web viene fatta verso il server, il middleware viene invocato e, data la sua implementazione, lascerà passare la richiesta oppure restituirà un errore che indica che il client non è autorizzato a procedere.

**TypeScript**

Qui creiamo un middleware con il popolare framework Express e intercettiamo la richiesta prima che raggiunga l'MCP Server. Ecco il codice per questo:

```typescript
function isValid(secret) {
    return secret === "secret123";
}

app.use((req, res, next) => {
    // 1. Intestazione di autorizzazione presente?
    if(!req.headers["Authorization"]) {
        res.status(401).send('Unauthorized');
    }
    
    let token = req.headers["Authorization"];

    // 2. Controlla la validità.
    if(!isValid(token)) {
        res.status(403).send('Forbidden');
    }

   
    console.log('Middleware executed');
    // 3. Passa la richiesta al passaggio successivo nella pipeline della richiesta.
    next();
});
```

In questo codice:

1. Controlliamo se l'header Authorization è presente, altrimenti inviamo un errore 401.
2. Ci assicuriamo che la credenziale/token sia valido, altrimenti inviamo errore 403.
3. Infine, passa la richiesta nella pipeline e restituisce la risorsa richiesta.

## Esercizio: Implementa l'autenticazione

Prendiamo la nostra conoscenza e proviamo a implementarla. Ecco il piano:

Server

- Crea un server web e un'istanza MCP.
- Implementa un middleware per il server.

Client

- Invia una richiesta web, con credenziali, tramite header.

### -1- Crea un server web e un'istanza MCP

Nel primo passo, dobbiamo creare l'istanza del server web e l'MCP Server.

**Python**

Qui creiamo un'istanza MCP Server, creiamo una app web starlette e la ospitiamo con uvicorn.

```python
# creando server MCP

app = FastMCP(
    name="MCP Resource Server",
    instructions="Resource Server that validates tokens via Authorization Server introspection",
    host=settings["host"],
    port=settings["port"],
    debug=True
)

# creando applicazione web starlette
starlette_app = app.streamable_http_app()

# servendo l'app tramite uvicorn
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

- Creiamo l'MCP Server.
- Costruiamo la app starlette dal MCP Server, `app.streamable_http_app()`.
- Ospitiamo e serviamo la app web usando uvicorn `server.serve()`.

**TypeScript**

Qui creiamo un'istanza MCP Server.

```typescript
const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    });

    // ... configura risorse del server, strumenti e prompt ...
```

La creazione dell'MCP Server dovrà avvenire all'interno della definizione della rotta POST /mcp, quindi prendiamo il codice sopra e spostiamolo così:

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

// Gestire richieste POST per la comunicazione client-server
app.post('/mcp', async (req, res) => {
  // Controlla l'esistenza dell'ID sessione
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
      // La protezione contro il DNS rebinding è disabilitata di default per compatibilità con versioni precedenti. Se stai eseguendo questo server
      // localmente, assicurati di impostare:
      // enableDnsRebindingProtection: true,
      // allowedHosts: ['127.0.0.1'],
    });

    // Pulisce il trasporto quando chiuso
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

    // Connessione al server MCP
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

// Gestisci richieste GET per notifiche server-client tramite SSE
app.get('/mcp', handleSessionRequest);

// Gestisci richieste DELETE per terminazione sessione
app.delete('/mcp', handleSessionRequest);

app.listen(3000);
```

Ora vedi come la creazione dell'MCP Server è stata spostata dentro `app.post("/mcp")`.

Procediamo con il prossimo passo di creare il middleware per poter validare la credenziale in arrivo.

### -2- Implementa un middleware per il server

Passiamo alla parte middleware. Qui creeremo un middleware che cerca una credenziale nell'header `Authorization` e la valida. Se è accettabile, la richiesta proseguirà per fare quello che deve (es. elencare strumenti, leggere una risorsa o qualsiasi funzionalità MCP richiesta dal client).

**Python**

Per creare il middleware, dobbiamo creare una classe che eredita da `BaseHTTPMiddleware`. Ci sono due parti interessanti:

- La request `request`, da cui leggiamo le informazioni dell'header.
- `call_next` il callback da invocare se il client ha portato una credenziale che accettiamo.

Prima dobbiamo gestire il caso se manca l'header `Authorization`:

```python
has_header = request.headers.get("Authorization")

# nessuna intestazione presente, fallire con 401, altrimenti procedere.
if not has_header:
    print("-> Missing Authorization header!")
    return Response(status_code=401, content="Unauthorized")
```

Qui inviamo un messaggio 401 unauthorized dato che il client non supera l'autenticazione.

Successivamente, se una credenziale è stata inviata, dobbiamo verificarne la validità così:

```python
 if not valid_token(has_header):
    print("-> Invalid token!")
    return Response(status_code=403, content="Forbidden")
```

Nota come sopra inviamo un messaggio 403 forbidden. Vediamo il middleware completo che implementa tutto quanto detto sopra:

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

```python
# NON usare per la produzione - migliora !!
def valid_token(token: str) -> bool:
    # rimuovi il prefisso "Bearer "
    if token.startswith("Bearer "):
        token = token[7:]
        return token == "secret-token"
    return False
```

Ovviamente dovrebbe essere migliorata.

IMPORTANTE: Non dovresti MAI avere segreti così nel codice. Dovresti idealmente recuperare il valore da confrontare da una fonte dati o da un IDP (identity provider) o, meglio ancora, lasciare all'IDP la validazione.

**TypeScript**

Per implementare questo con Express, dobbiamo chiamare il metodo `use` che accetta funzioni middleware.

Dobbiamo:

- Interagire con la variabile request per controllare la credenziale passata nella proprietà `Authorization`.
- Validare la credenziale e, se valida, lasciare proseguire la richiesta e far svolgere la richiesta MCP del client (es. elencare strumenti, leggere risorsa o altro MCP correlato).

Qui controlliamo se l'header `Authorization` è presente, se no fermiamo la richiesta:

```typescript
if(!req.headers["authorization"]) {
    res.status(401).send('Unauthorized');
    return;
}
```

Se l'header non è inviato, ricevi un 401.

Poi verifichiamo se la credenziale è valida, altrimenti fermiamo di nuovo la richiesta ma con un messaggio diverso:

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

Abbiamo impostato il server web per accettare un middleware che verifica le credenziali che il client speriamo ci stia inviando. E il client stesso?

### -3- Invia la richiesta web con credenziale tramite header

Dobbiamo assicurarci che il client passi la credenziale attraverso l'header. Poiché useremo un client MCP per farlo, dobbiamo capire come fare.

**Python**

Per il client, dobbiamo passare un header con la nostra credenziale così:

```python
# NON inserire il valore in modo statico, conservalo almeno in una variabile d'ambiente o in un archivio più sicuro
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
      
            # TODO, cosa vuoi fare nel client, ad esempio elencare strumenti, chiamare strumenti ecc.
```

Nota come popoliamo la proprietà `headers` così ` headers = {"Authorization": f"Bearer {token}"}`.

**TypeScript**

Possiamo risolvere in due passi:

1. Popolare un oggetto di configurazione con la nostra credenziale.
2. Passare l'oggetto di configurazione al transport.

```typescript

// NON codificare a valore fisso come mostrato qui. Al minimo, impostalo come variabile d'ambiente e usa qualcosa come dotenv (in modalità sviluppo).
let token = "secret123"

// definire un oggetto opzioni di trasporto per il client
let options: StreamableHTTPClientTransportOptions = {
  sessionId: sessionId,
  requestInit: {
    headers: {
      "Authorization": "secret123"
    }
  }
};

// passa l'oggetto opzioni al trasporto
async function main() {
   const transport = new StreamableHTTPClientTransport(
      new URL(serverUrl),
      options
   );
```

Qui vedi come abbiamo dovuto creare un oggetto `options` e mettere gli header sotto la proprietà `requestInit`.

IMPORTANTE: Come migliorarlo da qui? Beh, l'implementazione attuale ha problemi. Innanzitutto, passare una credenziale così è rischioso a meno che non si usi HTTPS almeno. Anche così, la credenziale può essere rubata quindi serve un sistema dove puoi facilmente revocare il token e aggiungere controlli come da dove nel mondo arriva, se la richiesta avviene troppo spesso (comportamento bot), insomma, ci sono diverse preoccupazioni.

Detto questo, per API molto semplici dove non vuoi nessuno che chiami la tua API senza essere autenticato ciò che abbiamo qui è un buon inizio.

Detto ciò, proviamo a irrobustire la sicurezza un po’ usando un formato standardizzato come JSON Web Token, noto anche come JWT o token "JOT".

## JSON Web Tokens, JWT

Stiamo cercando di migliorare l'invio di credenziali molto semplici. Quali sono i miglioramenti immediati adottando JWT?

- **Miglioramenti di sicurezza**. Nella basic auth, invii nome utente e password codificati in base64 (o un API key) più volte aumentando il rischio. Con JWT, invii nome utente e password e ottieni un token in cambio che ha anche una scadenza temporale. JWT permette facilmente il controllo accessi fine-grained usando ruoli, scope e permessi.
- **Statelessness e scalabilità**. I JWT sono self-contained, contengono tutte le info utente ed eliminano la necessità di memorizzazione lato server. Il token può anche essere validato localmente.
- **Interoperabilità e federazione**. I JWT sono centrali in Open ID Connect e sono usati con provider di identità noti come Entra ID, Google Identity e Auth0. Rendono possibile usare il single sign on e molto altro, rendendoli adatti enterprise.
- **Modularità e flessibilità**. I JWT possono essere usati con API Gateway come Azure API Management, NGINX e altri. Supportano scenari di autenticazione e comunicazione server-to-service inclusi impersonificazione e delega.
- **Performance e caching**. I JWT possono essere memorizzati in cache dopo la decodifica riducendo la necessità di parsing. Aiuta specialmente app ad alto traffico migliorando la throughput e riducendo carico sull'infrastruttura.
- **Funzionalità avanzate**. Supporta anche introspezione (verifica di validità sul server) e revoca (rendere un token invalido).

Con tutti questi vantaggi, vediamo come portare la nostra implementazione al livello successivo.

## Trasformare la basic auth in JWT

Quindi, i cambiamenti da fare a livello generale sono:

- **Imparare a costruire un token JWT** e renderlo pronto per essere inviato da client a server.
- **Validare un token JWT** e, se valido, permettere al client di accedere alle risorse.
- **Archiviazione sicura del token**. Come memorizziamo questo token.
- **Proteggere le rotte**. Dobbiamo proteggere le rotte, cioè proteggere rotte e funzionalità specifiche MCP.
- **Aggiungere refresh token**. Assicurarci di creare token a vita breve ma refresh token a vita lunga che possono essere usati per ottenere nuovi token se scadono. Assicurarsi anche di avere un endpoint di refresh e una strategia di rotazione.

### -1- Costruire un token JWT

Per cominciare, un token JWT ha le seguenti parti:

- **header**, algoritmo usato e tipo del token.
- **payload**, claims, come sub (l’utente o entità che il token rappresenta, tipicamente userid in uno scenario auth), exp (quando scade), role (ruolo)
- **signature**, firmata con un segreto o chiave privata.

Per questo, dobbiamo costruire header, payload e il token codificato.

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

Nel codice sopra:

- Abbiamo definito un header usando HS256 come algoritmo e tipo JWT.
- Costruito un payload che contiene un soggetto o id utente, un username, un ruolo, quando è stato emesso e quando scade implementando così l’aspetto temporale descritto prima.

**TypeScript**

Qui avremo bisogno di dipendenze che aiutano a costruire il token JWT.

Dipendenze

```sh

npm install jsonwebtoken
npm install --save-dev @types/jsonwebtoken
```

Ora che abbiamo questo, creiamo header, payload e tramite questo creiamo il token codificato.

```typescript
import jwt from 'jsonwebtoken';

const secretKey = 'your-secret-key'; // Usa variabili d'ambiente in produzione

// Definisci il payload
const payload = {
  sub: '1234567890',
  name: 'User usersson',
  admin: true,
  iat: Math.floor(Date.now() / 1000), // Emesso il
  exp: Math.floor(Date.now() / 1000) + 60 * 60 // Scade in 1 ora
};

// Definisci l'intestazione (opzionale, jsonwebtoken imposta valori predefiniti)
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

Dobbiamo anche validare un token, cosa che dovremmo fare sul server per assicurarci che quello che il client ci manda sia valido. Ci sono molti controlli da fare, dalla struttura alla validità. Sei anche incoraggiato ad aggiungere altri controlli per verificare che l’utente sia nel tuo sistema e altro.

Per validare un token, dobbiamo decodificarlo per leggerlo e iniziare a controllare la validità:

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

In questo codice chiamiamo `jwt.decode` con token, segreto e algoritmo scelto come input. Nota come usiamo un costrutto try-catch dato che una validazione fallita genera un errore.

**TypeScript**

Qui chiamiamo `jwt.verify` per ottenere una versione decodificata del token da analizzare ulteriormente. Se la chiamata fallisce significa che la struttura del token è incorretta o non è più valido.

```typescript

try {
  const decoded = jwt.verify(token, secretKey);
  console.log('Decoded Payload:', decoded);
} catch (err) {
  console.error('Token verification failed:', err);
}
```

NOTA: come detto prima, dovremmo fare controlli aggiuntivi per assicurarci che il token indichi un utente nel nostro sistema e che l’utente abbia i diritti dichiarati.

Passiamo ora a vedere l'accesso basato sui ruoli, noto anche come RBAC.
## Aggiunta del controllo degli accessi basato sui ruoli

L'idea è che vogliamo esprimere che ruoli diversi hanno permessi diversi. Ad esempio, presumiamo che un amministratore possa fare tutto, che un utente normale possa leggere/scrivere e che un ospite possa solo leggere. Pertanto, ecco alcuni possibili livelli di permesso:

- Admin.Write 
- User.Read
- Guest.Read

Vediamo come possiamo implementare un tale controllo con middleware. I middleware possono essere aggiunti per rotta così come per tutte le rotte.

**Python**

```python
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import jwt

# NON mettere il segreto nel codice, questo è solo a scopo dimostrativo. Légilo da un luogo sicuro.
SECRET_KEY = "your-secret-key" # mettilo in una variabile d'ambiente
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

# Alt 1: aggiungere middleware durante la costruzione dell'app starlette
middleware = [
    Middleware(JWTPermissionMiddleware)
]

app = Starlette(routes=routes, middleware=middleware)

# Alt 2: aggiungere middleware dopo che l'app starlette è già stata costruita
starlette_app.add_middleware(JWTPermissionMiddleware)

# Alt 3: aggiungere middleware per ogni route
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

Ci sono molte cose che possiamo lasciare al nostro middleware e che il nostro middleware DEVE fare, cioè:

1. Controllare se l'header di autorizzazione è presente
2. Controllare se il token è valido, chiamiamo `isValid` che è un metodo che abbiamo scritto che verifica l'integrità e la validità del token JWT.
3. Verificare che l'utente esista nel nostro sistema, dovremmo controllare questo.

   ```typescript
    // utenti nel DB
   const users = [
     "user1",
     "User usersson",
   ]

   function isExistingUser(token) {
     let decodedToken = verifyToken(token);

     // DA FARE, controllare se l'utente esiste nel DB
     return users.includes(decodedToken?.name || "");
   }
   ```

   Sopra, abbiamo creato una lista molto semplice di `users`, che ovviamente dovrebbe essere in un database.

4. Inoltre, dovremmo anche verificare che il token abbia i permessi corretti.

   ```typescript
   if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
   }
   ```

   Nel codice sopra dal middleware, verifichiamo che il token contenga il permesso User.Read, altrimenti inviamo un errore 403. Qui sotto c'è il metodo helper `hasScopes`.

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

Ora avete visto come il middleware può essere usato sia per l'autenticazione che per l'autorizzazione, ma per MCP invece, cambia il modo in cui facciamo l'autenticazione? Scopriamolo nella prossima sezione.

### -3- Aggiungere RBAC a MCP

Finora hai visto come aggiungere RBAC tramite middleware, tuttavia, per MCP non c'è un modo semplice per aggiungere RBAC per ogni funzionalità MCP, quindi cosa facciamo? Beh, dobbiamo semplicemente aggiungere un codice come questo che verifica in questo caso se il client ha i diritti per chiamare uno strumento specifico:

Hai diverse scelte su come realizzare il RBAC per ogni funzionalità, eccone alcune:

- Aggiungi un controllo per ogni strumento, risorsa, prompt dove devi verificare il livello di permesso.

   **python**

   ```python
   @tool()
   def delete_product(id: int):
      try:
          check_permissions(role="Admin.Write", request)
      catch:
        pass # il cliente non è riuscito all'autorizzazione, genera errore di autorizzazione
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
        // da fare, inviare l'id a productService e all'entry remota
      } catch(Exception e) {
        console.log("Authorization error, you're not allowed");  
      }

      return {
        content: [{ type: "text", text: `Deletected product with id ${id}` }]
      };
    }
   );
   ```


- Utilizza un approccio avanzato server e i gestori delle richieste così da minimizzare il numero di posizioni dove devi fare il controllo.

   **Python**

   ```python
   
   tool_permission = {
      "create_product": ["User.Write", "Admin.Write"],
      "delete_product": ["Admin.Write"]
   }

   def has_permission(user_permissions, required_permissions) -> bool:
      # permessi_utente: lista dei permessi che l'utente ha
      # permessi_richiesti: lista dei permessi richiesti per lo strumento
      return any(perm in user_permissions for perm in required_permissions)

   @server.call_tool()
   async def handle_call_tool(
     name: str, arguments: dict[str, str] | None
   ) -> list[types.TextContent]:
    # Si assume che request.user.permissions sia una lista di permessi per l'utente
     user_permissions = request.user.permissions
     required_permissions = tool_permission.get(name, [])
     if not has_permission(user_permissions, required_permissions):
        # Genera errore "Non hai il permesso di chiamare lo strumento {name}"
        raise Exception(f"You don't have permission to call tool {name}")
     # continua ed esegui lo strumento
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

   Nota, dovrai assicurarti che il tuo middleware assegni un token decodificato alla proprietà user della richiesta così che il codice sopra sia semplice.

### Riassumendo

Ora che abbiamo discusso come aggiungere il supporto per RBAC in generale e per MCP in particolare, è il momento di provare a implementare la sicurezza da soli per assicurarti di aver compreso i concetti presentati.

## Compito 1: Costruire un server MCP e un client MCP usando l'autenticazione base

Qui prenderai ciò che hai imparato in termini di invio delle credenziali tramite header.

## Soluzione 1

[Soluzione 1](./code/basic/README.md)

## Compito 2: Aggiornare la soluzione del Compito 1 per usare JWT

Prendi la prima soluzione ma questa volta, miglioriamola.

Invece di usare l'autenticazione Basic, usiamo JWT.

## Soluzione 2

[Soluzione 2](./solution/jwt-solution/README.md)

## Sfida

Aggiungi il RBAC per ogni strumento come descritto nella sezione "Aggiungere RBAC a MCP".

## Riepilogo

Si spera che tu abbia imparato molto in questo capitolo, da nessuna sicurezza, a una sicurezza base, a JWT e come può essere aggiunto a MCP.

Abbiamo costruito una solida base con JWT personalizzati, ma man mano che cresciamo, stiamo andando verso un modello di identità basato su standard. Adottare un IdP come Entra o Keycloak ci permette di scaricare il rilascio, la validazione e la gestione del ciclo di vita dei token su una piattaforma fidata — liberandoci per concentrarci sulla logica dell'app e sull'esperienza utente.

Per questo, abbiamo un capitolo più [avanzato su Entra](../../05-AdvancedTopics/mcp-security-entra/README.md)

## Cosa c’è dopo

- Successivo: [Impostare gli host MCP](../12-mcp-hosts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si consiglia la traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->