# Simple auth

MCP SDKs dey support to use OAuth 2.1 wey to be honest na one serious process wey get concepts like auth server, resource server, to post credentials, to collect code, to change the code for bearer token until you fit finally collect your resource data. If you never use OAuth before wey good make you try am, e good make you start with some simple auth level and build am up to beta security. Na why dis chapter dey so, to help you grow reach advanced auth.

## Auth, wetin we mean?

Auth na short for authentication and authorization. Di idea be say we need do two tins:

- **Authentication**, na di process of to sabi if we go gree make one person enter our house, if dem get right to dey "here" meaning access to our resource server where MCP Server features dey.
- **Authorization**, na di process of to sabi if user suppose get access to dis particular resources wey dem dey ask for, example these orders or products or if dem fit read the content but no fit delete am as example.

## Credentials: how we take tell system who we be

Well, most web developers dey think say make dem provide one credential to the server, normally one secret wey talk say if dem fit dey here "Authentication". Dis credential na usually base64 encoded username and password or API key wey uniquely identify one user. 

Dis one dey send am via header wey dem dey call "Authorization" like dis:

```json
{ "Authorization": "secret123" }
```

Dis na basic authentication dem dey call am. How di flow dey go be like dis:

```mermaid
sequenceDiagram
   participant User
   participant Client
   participant Server

   User->>Client: show me data
   Client->>Server: show me data, dis na my credential
   Server-->>Client: 1a, I sabi you, dis na your data
   Server-->>Client: 1b, I no sabi you, 401 
```

Now we sabi how e dey work as flow, how we take implement am? Most web servers get one thing wey dem dey call middleware, na piece of code wey dey run as part of the request wey fit check credentials, if credentials correct e go gree make the request pass. If request no get valid credential you go get auth error. Make we see how we fit implement am:

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
        # add any customer headers or change for di response for some way
        return response


starlette_app.add_middleware(CustomHeaderMiddleware)
```

Here we get:

- Create one middleware wey dem call `AuthMiddleware` where e get `dispatch` method wey web server dey call.
- Add di middleware come web server:

    ```python
    starlette_app.add_middleware(AuthMiddleware)
    ```

- Write validation logic wey dey check if Authorization header dey and if di secret wey dem send valid.

    ```python
    has_header = request.headers.get("Authorization")
    if not has_header:
        print("-> Missing Authorization header!")
        return Response(status_code=401, content="Unauthorized")

    if not valid_token(has_header):
        print("-> Invalid token!")
        return Response(status_code=403, content="Forbidden")
    ```

    if di secret dey and e valid, we go gree make request pass by to call `call_next` and return di response.

    ```python
    response = await call_next(request)
    # add any customer headers or change for di response for way small
    return response
    ```

How e dey work be say if web request come server middleware go run, based on how e implement, e go either gree make request pass or e go return error wey talk say client no get access.

**TypeScript**

Here we go create one middleware with popular framework Express and intercept request before e reach MCP Server. Dis na di code:

```typescript
function isValid(secret) {
    return secret === "secret123";
}

app.use((req, res, next) => {
    // 1. Authorization header dey?
    if(!req.headers["Authorization"]) {
        res.status(401).send('Unauthorized');
    }
    
    let token = req.headers["Authorization"];

    // 2. Check if e correct.
    if(!isValid(token)) {
        res.status(403).send('Forbidden');
    }

   
    console.log('Middleware executed');
    // 3. Pass di request go di next step for di request pipeline.
    next();
});
```

This code do:

1. Check if Authorization header dey at all, if no dey we send 401 error.
2. Check if credential/token valid, if no, we send 403 error.
3. Finally, we pass request forward in request pipeline, return resource wey dem ask for.

## Exercise: Implement authentication

Make we use our knowledge try implement dis plan:

Server

- Create web server and MCP instance.
- Implement middleware for server.

Client 

- Send web request wey get credential via header.

### -1- Create web server and MCP instance

> [!WARNING]
> Di TypeScript example wey dey below target MCP `2025-11-25`. E dey track transports
> by `mcp-session-id` and na no be current `2026-07-28` transport example. MCP
> `2026-07-28` remove `initialize` handshake and protocol session ID; new
> implementations use self-contained requests. See
> [What's Changed in MCP: The 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md).

For our first step, we suppose create web server instance and di MCP Server.

**Python**

Here we create MCP server instance, create starlette web app and host am with uvicorn.

```python
# di mɛki MCP Server

app = FastMCP(
    name="MCP Resource Server",
    instructions="Resource Server that validates tokens via Authorization Server introspection",
    host=settings["host"],
    port=settings["port"],
    debug=True
)

# di mɛki starlette web app
starlette_app = app.streamable_http_app()

# di serve di app through uvicorn
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

This code do:

- Create MCP Server.
- Construct starlette web app from MCP Server, `app.streamable_http_app()`.
- Host and server web app using uvicorn `server.serve()`.

**TypeScript**

Here we create MCP Server instance.

```typescript
const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    });

    // ... arrange server resources, tools, and prompts ...
```

Dis MCP Server creation go happen inside our POST /mcp route definition, so make we move top code like dis:

```typescript
import express from "express";
import { randomUUID } from "node:crypto";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { isInitializeRequest } from "@modelcontextprotocol/sdk/types.js"

const app = express();
app.use(express.json());

// Map wey dey store transports by session ID
const transports: { [sessionId: string]: StreamableHTTPServerTransport } = {};

// Handle POST requests for client-to-server communication
app.post('/mcp', async (req, res) => {
  // Check if session ID don dey
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  let transport: StreamableHTTPServerTransport;

  if (sessionId && transports[sessionId]) {
    // Use existing transport again
    transport = transports[sessionId];
  } else if (!sessionId && isInitializeRequest(req.body)) {
    // New initialization request
    transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: () => randomUUID(),
      onsessioninitialized: (sessionId) => {
        // Store di transport by session ID
        transports[sessionId] = transport;
      },
      // DNS rebinding protection no dey enabled by default for backwards compatibility. If you dey run dis server
      // locally, make sure say you set:
      // enableDnsRebindingProtection: true,
      // allowedHosts: ['127.0.0.1'],
    });

    // Clean transport when e close
    transport.onclose = () => {
      if (transport.sessionId) {
        delete transports[transport.sessionId];
      }
    };
    const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    });

    // ... set up server resources, tools, and prompts ...

    // Connect to di MCP server
    await server.connect(transport);
  } else {
    // Invalid request
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

  // Handle di request
  await transport.handleRequest(req, res, req.body);
});

// Reusable handler for GET and DELETE requests
const handleSessionRequest = async (req: express.Request, res: express.Response) => {
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  if (!sessionId || !transports[sessionId]) {
    res.status(400).send('Invalid or missing session ID');
    return;
  }
  
  const transport = transports[sessionId];
  await transport.handleRequest(req, res);
};

// Handle GET requests for server-to-client notifications via SSE
app.get('/mcp', handleSessionRequest);

// Handle DELETE requests for session termination
app.delete('/mcp', handleSessionRequest);

app.listen(3000);
```

Now you see how MCP Server creation move inside `app.post("/mcp")`.

Make we go next step create middleware wey fit validate credential wey dey come.

### -2- Implement middleware for server

Now make we do middleware part. Here we go create middleware wey go look for credential inside `Authorization` header and validate am. If e bam, request go do wetin e suppose do (like list tools, read resource or any MCP function client ask).

**Python**

To create middleware, we need create class wey inherit from `BaseHTTPMiddleware`. Two tins dey important:

- The request `request`, we go read header info from.
- `call_next` callback wey we go call if client bring credential we accept.

First, we go handle case if `Authorization` header no dey:

```python
has_header = request.headers.get("Authorization")

# no header dey, fail wit 401, if no, make you continue.
if not has_header:
    print("-> Missing Authorization header!")
    return Response(status_code=401, content="Unauthorized")
```

Here we send 401 unauthorized message because client fail authentication.

Next, if client send credential, we go check if e valid like dis:

```python
 if not valid_token(has_header):
    print("-> Invalid token!")
    return Response(status_code=403, content="Forbidden")
```

Notice say we send 403 forbidden message here. See full middleware code below wey do all we yarn:

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

Fine, but wetin be `valid_token` function? Here am below:

```python
# NO use am for production - make am beta !!
def valid_token(token: str) -> bool:
    # comot the "Bearer " prefix
    if token.startswith("Bearer "):
        token = token[7:]
        return token == "secret-token"
    return False
```

This one fit improve well well.

IMPORTANT: You no suppose store secret like dis for code. Beta be say you go take am from data source or IDP (identity service provider) or make IDP do di validation.

**TypeScript**

To do dis one with Express, we need to call `use` method wey take middleware functions.

We need:

- To interact with request object to check credential inside `Authorization` property.
- Validate credential, if bam, allow request continue so client request go run (list tools, read resource or any MCP related).

Here, we dey check if `Authorization` header dey, if no, we stop request:

```typescript
if(!req.headers["authorization"]) {
    res.status(401).send('Unauthorized');
    return;
}
```

If header no send, you go get 401.

Next, we check if credential valid, if no we stop request with different message:

```typescript
if(!isValid(token)) {
    res.status(403).send('Forbidden');
    return;
} 
```

See how now na 403 error you get.

Here na full code:

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

We set web server to accept middleware to check credential client fit send. How about the client?

### -3- Send web request with credential via header

We need make sure client dey pass credential inside header. Since we dey use MCP client, we need see how e dey done.

**Python**

For client, we go pass header with our credential like dis:

```python
# NO hardcode di value, make e dey for environment variable or beta secure place
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
      
            # TODO, wetin you want make client do, like list tools, call tools etc.
```

Note how we set `headers` property like `headers = {"Authorization": f"Bearer {token}"}`.

**TypeScript**

We fit do am for two steps:

1. Populate configuration object with credential.
2. Pass configuration to transport.

```typescript

// NO hardcode di value like dis for here. At least make am be env variable and use sometin like dotenv (for dev mode).
let token = "secret123"

// define client transport option object
let options: StreamableHTTPClientTransportOptions = {
  sessionId: sessionId,
  requestInit: {
    headers: {
      "Authorization": "secret123"
    }
  }
};

// pass di options object go di transport
async function main() {
   const transport = new StreamableHTTPClientTransport(
      new URL(serverUrl),
      options
   );
```

Here you see say we create `options` object and put our headers inside `requestInit`.

IMPORTANT: How we go make am beta? Right now e get wahala. First, to pass credential like dis na risk unless you get HTTPS. Even then e fit steal am, so you need system wey go fit revoke tokens and add checks like where e from, if request dey happen too much (bot behavior), and more. 

But e suppose talk say for very simple APIs, where you no want anybody dey call your API without auth, this one na good start.

With dat one, make we try make security strong small by to use standard format like JSON Web Token wey people sabi as JWT or "JOT" tokens.

## JSON Web Tokens, JWT

So, we dey try improve from to just dey send simple credentials, wetin na immediate betterment we get to if we use JWT?

- **Security improvement**. For basic auth, you go dey send username and password as base64 encoded token (or API key) again and again wey dey risky. With JWT, you go send your username and password and get token back wey dey expire after time. JWT fit give fine-grained control with roles, scopes, permissions.
- **Statelessness and scalability**. JWTs self-contained, dem carry all user info and no need server session storage. Token fit validate locally.
- **Interoperability and federation**. JWTs na center for Open ID Connect and dem dey use with big ID providers like Entra ID, Google Identity and Auth0. Dem fit do single sign on and plenti more beta beta enterprise features.
- **Modularity and flexibility**. JWTs fit also use with API Gateways like Azure API Management, NGINX and others. E support user auth and server-service communication like impersonation and delegation.
- **Performance and caching**. JWTs fit cache after decoding, wey reduce parsing need. E help beta for high-traffic apps as e improve throughput and reduce infrastructure load.
- **Advanced features**. E also support introspection (check validity for server) and revocation (make token invalid).

With all dis better tins, make we see as we fit take our implementation reach beta level.

## Turning basic auth into JWT

So, di changes we need make on top high level na:

- **Learn how to construct JWT token** and make am ready to send from client to server.
- **Validate JWT token**, if bam, allow client get our resources.
- **Secure token storage**. How we go store token.
- **Protect routes**. We go protect routes and specific MCP features.
- **Add refresh tokens**. Make tokens short-lived but add long-lived refresh tokens wey fit get new tokens if dem expire. Make sure refresh endpoint dey with rotation strategy.

### -1- Construct JWT token

First, JWT token get di following parts:

- **header**, algorithm wey e use and token type.
- **payload**, claims like sub (user or entity token represent, usually userid for auth), exp (when e expire), role (di role).
- **signature**, signed with secret or private key.

For dis one, we need construct header, payload, and encoded token.

**Python**

```python

import jwt
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import datetime

# Secret key wey dem use to sign di JWT
secret_key = 'your-secret-key'

header = {
    "alg": "HS256",
    "typ": "JWT"
}

# di user info and im claims and expiry time
payload = {
    "sub": "1234567890",               # Subject (user ID)
    "name": "User Userson",                # Custom claim
    "admin": True,                     # Custom claim
    "iat": datetime.datetime.utcnow(),# Issued at
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiry
}

# encode am
encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256", headers=header)
```

In dis code we:

- Define header using HS256 algorithm and type JWT.
- Construct payload wey get subject or user id, username, role, when e issued and when e go expire to do time bound like we talk before.

**TypeScript**

Here we need some dependencies wey go help us construct JWT token.

Dependencies

```sh

npm install jsonwebtoken
npm install --save-dev @types/jsonwebtoken
```

Now we get am, make we create header, payload and through that make encoded token.

```typescript
import jwt from 'jsonwebtoken';

const secretKey = 'your-secret-key'; // Use env vars for production

// Define di payload
const payload = {
  sub: '1234567890',
  name: 'User usersson',
  admin: true,
  iat: Math.floor(Date.now() / 1000), // Issued at
  exp: Math.floor(Date.now() / 1000) + 60 * 60 // Expires afta 1 hour
};

// Define di header (optional, jsonwebtoken dey set defaults)
const header = {
  alg: 'HS256',
  typ: 'JWT'
};

// Create di token
const token = jwt.sign(payload, secretKey, {
  algorithm: 'HS256',
  header: header
});

console.log('JWT:', token);
```

Dis token be:

Signed using HS256
Valid for 1 hour
Get claims like sub, name, admin, iat, exp.

### -2- Validate token

We go need validate token, dis na wetin server suppose do to confirm wetin client send na valid. Plenty checks dey to do from structure validation to validity. You fit even add checks if user dey your system and more.

To validate token, we need decode am to read and start check if e legit:

**Python**

```python

# Decode an check di JWT
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


For dis code, we dey call `jwt.decode` wit token, secret key and di algorithm wey we choose as input. See as we take use try-catch construct because if validation fail, e go raise error.

**TypeScript**

Here, we need to call `jwt.verify` to get decoded version of token wey we fit analyze more. If dis call fail, e mean say structure of token no correct or e no valid again.

```typescript

try {
  const decoded = jwt.verify(token, secretKey);
  console.log('Decoded Payload:', decoded);
} catch (err) {
  console.error('Token verification failed:', err);
}
```

NOTE: as we talk before, we suppose still do extra checks to make sure dis token dey represent user for our system and the user get di rights wey e dey claim.

Next, make we check role based access control, wey dem also dey call RBAC.

## Adding role based access control

Di idea be say we want express say different roles get different permissions. For example, we assume say admin fit do everything, normal user fit do read/write, and guest fit only read. So, dis na some possible permission levels:

- Admin.Write 
- User.Read
- Guest.Read

Make we see how we fit implement dis kind control with middleware. We fit add middleware per route or for all routes.

**Python**

```python
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import jwt

# NO gèt di secret inside di code like dis, dis na only for demonstration purposes. Make you read am from one safe place.
SECRET_KEY = "your-secret-key" # put dis for env variable
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

E get few ways to add middleware like dis one below:

```python

# Alt 1: put middleware wen you dey build starlette app
middleware = [
    Middleware(JWTPermissionMiddleware)
]

app = Starlette(routes=routes, middleware=middleware)

# Alt 2: put middleware afta starlette app don already build
starlette_app.add_middleware(JWTPermissionMiddleware)

# Alt 3: put middleware for each route
routes = [
    Route(
        "/mcp",
        endpoint=..., # handler
        middleware=[Middleware(JWTPermissionMiddleware)]
    )
]
```

**TypeScript**

We fit use `app.use` plus middleware wey go run for all requests. 

```typescript
app.use((req, res, next) => {
    console.log('Request received:', req.method, req.url, req.headers);
    console.log('Headers:', req.headers["authorization"]);

    // 1. Check if dem don send authorization header

    if(!req.headers["authorization"]) {
        res.status(401).send('Unauthorized');
        return;
    }
    
    let token = req.headers["authorization"];

    // 2. Check if token valid
    if(!isValid(token)) {
        res.status(403).send('Forbidden');
        return;
    }  

    // 3. Check if token user dey for our system
    if(!isExistingUser(token)) {
        res.status(403).send('Forbidden');
        console.log("User does not exist");
        return;
    }
    console.log("User exists");

    // 4. Confirm say token get correct permissions
    if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }

    console.log("User has required scopes");

    console.log('Middleware executed');
    next();
});

```

E get plenty things we fit allow middleware do and things we middleware suppose do, like:

1. Check if authorization header dey
2. Check if token valid, we call `isValid` wey na method we write to check integrity and validity of JWT token.
3. Verify say user dey for our system, na wetin we suppose check.

   ```typescript
    // users wey dey for DB
   const users = [
     "user1",
     "User usersson",
   ]

   function isExistingUser(token) {
     let decodedToken = verifyToken(token);

     // TODO, check if user dey for DB
     return users.includes(decodedToken?.name || "");
   }
   ```

   For top, we don create simple `users` list, we for put am for database obviously.

4. Besides dat, we suppose check say token get correct permissions.

   ```typescript
   if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
   }
   ```

   From dis middleware code above, we dey check say token get User.Read permission, if no get, we go send 403 error. Below na `hasScopes` helper method.

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

Now you don see how middleware fit work for both authentication and authorization, but how about MCP, e dey change how we do auth? Make we see for di next section.

### -3- Add RBAC to MCP

You don see so far how you fit add RBAC through middleware, but for MCP, no easy way to add RBAC per MCP feature, so wetin we go do? Simple, we go add code like dis wey go check if client get rights to call specific tool:

You get few choices how you fit do per feature RBAC, here dem be:

- Add check for each tool, resource, prompt where you need to check permission level.

   **python**

   ```python
   @tool()
   def delete_product(id: int):
      try:
          check_permissions(role="Admin.Write", request)
      catch:
        pass # client no fit get authorization, raise authorization error
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
        // todo, send id go productService and remote entry
      } catch(Exception e) {
        console.log("Authorization error, you're not allowed");  
      }

      return {
        content: [{ type: "text", text: `Deletected product with id ${id}` }]
      };
    }
   );
   ```


- Use advanced server approach plus request handlers to reduce how many places you need to do di check.

   **Python**

   ```python
   
   tool_permission = {
      "create_product": ["User.Write", "Admin.Write"],
      "delete_product": ["Admin.Write"]
   }

   def has_permission(user_permissions, required_permissions) -> bool:
      # user_permissions: list of permissions wey di user get
      # required_permissions: list of permissions wey di tool need
      return any(perm in user_permissions for perm in required_permissions)

   @server.call_tool()
   async def handle_call_tool(
     name: str, arguments: dict[str, str] | None
   ) -> list[types.TextContent]:
    # Assume say request.user.permissions na list of permissions wey di user get
     user_permissions = request.user.permissions
     required_permissions = tool_permission.get(name, [])
     if not has_permission(user_permissions, required_permissions):
        # Throw error "You no get permission to call tool {name}"
        raise Exception(f"You don't have permission to call tool {name}")
     # continue and call di tool
     # ...
   ```   
   

   **TypeScript**

   ```typescript
   function hasPermission(userPermissions: string[], requiredPermissions: string[]): boolean {
       if (!Array.isArray(userPermissions) || !Array.isArray(requiredPermissions)) return false;
       // Return true if user get at least one permission wey e need
       
       return requiredPermissions.some(perm => userPermissions.includes(perm));
   }
  
   server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { params: { name } } = request;
  
      let permissions = request.user.permissions;
  
      if (!hasPermission(permissions, toolPermissions[name])) {
         return new Error(`You don't have permission to call ${name}`);
      }
  
      // carry on..
   });
   ```

   Note, you go need make sure say your middleware assign decoded token to request's user property so the code above go simple.

### Summing up

Now we don talk how to add support for RBAC generally and for MCP in particular, na time to try build security yourself make sure you understand all di concepts wey dem talk.

## Assignment 1: Build mcp server and mcp client using basic authentication

Here, you go use wetin you learn on how to send credentials through headers.

## Solution 1

[Solution 1](./code/basic/README.md)

## Assignment 2: Upgrade solution from Assignment 1 to use JWT

Take first solution but this time, make we improve am.

Instead of using Basic Auth, make we use JWT.

## Solution 2

[Solution 2](./solution/jwt-solution/README.md)

## Challenge

Add RBAC per tool like we talk for "Add RBAC to MCP" section.

## Summary

You don hope say you learn plenty for dis chapter, from no security at all, to basic security, to JWT and how you fit add am to MCP.

We don build strong foundation with custom JWTs, but as we dey grow, we dey move to standards-based identity model. Using IdP like Entra or Keycloak go make us free from token issue, validate, and lifecycle management — so that we fit focus on app logic and how users dey experience am.

For dat, we get more [advanced chapter on Entra](../../05-AdvancedTopics/mcp-security-entra/README.md)

## What's Next

- Next: [Setting Up MCP Hosts](../12-mcp-hosts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->