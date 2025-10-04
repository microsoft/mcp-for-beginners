# Simple auth

MCP SDKs support the use of OAuth 2.1 which to be fair is a pretty involved process involving concepts like auth server, resource server, posting credentials, getting a code, exhanging the code for a bearer token until you can finally get your resource data. If you're unused to OAuth which is a great thing to implement, it's a good idea to start with some basic level of auth and build up to better and better security. 

## Auth, what do we mean?

Auth is short for authentication and authorization. The idea is that we need to do two things:

- **Authentication**, which is the process of figuring out whether we let a person enter our house, that they have the right to be "here" that is have access to our resource server where our MCP Server features live.
- **Authorization**, is the process of finding out if a user should have access to these specific resources they're asking for for example these orders or these products or whether they're allowed to read the content but not delete as another example.

## Token: how we tell the system who we are

Well, most web developers out there start thinking in terms of providing a credential to the server, usually a secret that says if they're allowed to be here "Authentication". 

This involves sending it via a header called "Authorization" like so:

```json
{ "Authorization": "secret123" }
```

This is usually referred to as basic authentication. How the overall flow then works is in the following way:

```mermaid
sequenceDiagram
   participant User
   participant Client
   participant Server

   User->>Client: show me data
   Client->>Server: show me data, here's my secret
   Server-->>Client: 1a, I know you, here's your data
   Server-->>Client: 1b, I don't know you, 401 
```

Now that we understand how it works from a flow standpoint, how do we implement it? Well, most web servers have a concept called middleware, a piece of code that runs as part of the request that can verify credentials, and if credentials are valid can let the request pass through. If the request doesn't have valid credentials then you get an auth error. Let's see how this can be implemented:

**Python**

```python
class CustomHeaderMiddleware(BaseHTTPMiddleware):
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
        # add any customer headers or change in the response in some way
        return response


starlette_app.add_middleware(CustomHeaderMiddleware)
```

Here we have: 

- Created a middleware called `CustomHeaderMiddleware` where its `dispatch` method is being invoked by the web server. 
- Added the middleware to the web server:

    ```python
    starlette_app.add_middleware(CustomHeaderMiddleware)
    ```

- Written validation logic that checks if Authorization header is present and if the secret being sent is valid:

    ```python
    has_header = request.headers.get("Authorization")
    if not has_header:
        print("-> Missing Authorization header!")
        return Response(status_code=401, content="Unauthorized")

    if not valid_token(has_header):
        print("-> Invalid token!")
        return Response(status_code=403, content="Forbidden")
    ```

    if the secret is present and valid then we let the request pass through by calling `call_next` and return the response.

    ```python
    response = await call_next(request)
    # add any customer headers or change in the response in some way
    return response
    ```

How it works is that if a web request are made towards the server the middleware will be invoked and given its implementation it will either let the request pass through or end up returning an error that indicates the client isn't allowed to proceed.

**TypeScript**

It's a similar idea in TypeScript, here we use a middleware with the popular framework Express and intercept the request before it reaches the MCP Server. Here's the code for that:

```typescript
function isValid(secret) {
    return secret === "secret123";
}

app.use((req, res, next) => {
    if(!req.headers["Authorization"]) {
        res.status(401).send('Unauthorized');
    }
    
    let token = req.headers["Authorization"];

    if(!isValid(token)) {
        res.status(403).send('Forbidden');
    }

    console.log('Middleware executed');
    next();
});
```

## Exercise: Implement authentication

- Server: Create a web server and MCP instance.
- Server: Implement a middleware for the server.
- Client: Send web request with credential via header.

### -1- Create a web server and MCP instance

**Python**

Here we create an MCP server instance, create a starlette web app and host it with uvicorn.

```python
# creating MCP Server

app = FastMCP(
    name="MCP Resource Server",
    instructions="Resource Server that validates tokens via Authorization Server introspection",
    host=settings["host"],
    port=settings["port"],
    debug=True
)

# creating starlette web app
starlette_app = app.streamable_http_app()

# serving app via uvicorn
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

**TypeScript**

Here we create an MCP Server instance.

```typescript
const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    });

    // ... set up server resources, tools, and prompts ...
```

In the below code, we create a web server using Express, an MCP Server instance that we showed above. This is the standard way of defining a streamable MCP app.

```typescript
import express from "express";
import { randomUUID } from "node:crypto";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { isInitializeRequest } from "@modelcontextprotocol/sdk/types.js"

const app = express();
app.use(express.json());

// Map to store transports by session ID
const transports: { [sessionId: string]: StreamableHTTPServerTransport } = {};

// Handle POST requests for client-to-server communication
app.post('/mcp', async (req, res) => {
  // Check for existing session ID
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  let transport: StreamableHTTPServerTransport;

  if (sessionId && transports[sessionId]) {
    // Reuse existing transport
    transport = transports[sessionId];
  } else if (!sessionId && isInitializeRequest(req.body)) {
    // New initialization request
    transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: () => randomUUID(),
      onsessioninitialized: (sessionId) => {
        // Store the transport by session ID
        transports[sessionId] = transport;
      },
      // DNS rebinding protection is disabled by default for backwards compatibility. If you are running this server
      // locally, make sure to set:
      // enableDnsRebindingProtection: true,
      // allowedHosts: ['127.0.0.1'],
    });

    // Clean up transport when closed
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

    // Connect to the MCP server
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

  // Handle the request
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

### -2- Implement a middleware for the server

Let's get to the middleware portion next. Here we will create a middleware that looks for a credential in the `Authorization` header and validate it. If it's acceptable then the request will move on to do what it needs (e.g list tools, read a resource or whatever MCP functionality the client was asking for).

**Python**

To create the middleware, we need to create a class that inherits from `BaseHTTPMiddleware`. There's two interesting pieces:

- The request `request` , that we read the header info from.
- `call_next` the callback we need to invoke if the client have brought a credential we accept.

First, we need to handle the case if the `Authorization` header is missing:

```python
 has_header = request.headers.get("Authorization")
if not has_header:
    print("-> Missing Authorization header!")
    return Response(status_code=401, content="Unauthorized")
```

Here we send a 401 unauthorized message as the client is failing authentication.

Next, if a credential was submitted, we need to check its validity like so:

```python
 if not valid_token(has_header):
    print("-> Invalid token!")
    return Response(status_code=403, content="Forbidden")
```

Note how we send a 403 forbidden message.

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

Here's our validation method, that has a very simple validation that you should obviously improve:

```python
# DON'T use for production - improve it !!
def valid_token(token: str) -> bool:
    # remove the "Bearer " prefix
    if token.startswith("Bearer "):
        token = token[7:]
        return token == "secret-token"
    return False
```

**TypeScript**

To implement this with Express, we need to call the `use` method that takes middleware functions.

We need to:

- Interact with the request `req` to check the passed credential in the `Authorization` property.
- Validate the credential, and if so let the request continue and have the client's MCP request do what it should (e.g list tools, read resource or anything other MCP related).

Here, we're checking if the `Authorization` header is present and if not, we stop the request from going through:

```typescript
if(!req.headers["authorization"]) {
    res.status(401).send('Unauthorized');
    return;
}
```

Next, we check if the credential is valid, if not we again stop the request but with a slightly different message:

```typescript
if(!isValid(token)) {
    res.status(403).send('Forbidden');
    return;
} 
```

Here's the full code:

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

Now, we have set up the web server to accept a middleware to check the credential the client is hopefully sending us. What about the client itself?

### -3- Send web request with credential via header

**Python**

For the client, we need to pass a header with our credential like so:

```python
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
      
            # TODO, what you want done in the client, e.g list tools, call tools etc.
```

Note how we populate the `headers` property like so ` headers = {"Authorization": f"Bearer {token}"}`.

**TypeScript**

We can solve this in two steps:

1. Populate a configuration object with our credential.
2. Pass the configuration object to the transport.

```typescript
// define a client transport option object
let options: StreamableHTTPClientTransportOptions = {
  sessionId: sessionId,
  requestInit: {
    headers: {
      "Authorization": "secret123"
    }
  }
};

// pass the options object to the transport
async function main() {
   const transport = new StreamableHTTPClientTransport(
      new URL(serverUrl),
      options
   );
```

How do we improve it from here though? Well, the current implementation has some issues. First off, passing a credential like this is pretty risky unless you at minimum have HTTPS. Even then, the credential can be stolen so you need a system where you can easily revoke the token and add additional checks like where in the world is it coming from, does the request happen way too often (bot-like behavior), in short, there's a whole host of concerns. It should be said though, for very simple APIs where you don't want anyone calling your API without being authenticated this is a good start. 

With that said, let's try to harden the security a little bit by using a standardized format like JSON Web Token, also known as JWT or "JOT" tokens.

## JSON Web Tokens, JWT

So, we're trying to improve things from sending very simple credentials. What's the immediate improvements we get adopting JWT?

- **Security improvements**. In basic auth, you send the username and password as a base64 encoded token over and over which increase the risk. With JWT, you send your username and password and gets a token in return and it's also time bound meaning it will expire. JWT lets you easily use fine-grained access control using roles, scopes and permissions. 
- **Statelessness and scalability**. JWTs are self-contained, they carry all user info and eliminates the need to store server-side session storage. Token can also be validated locally.
- **Interoperability and federation**. JWTs is central of Open ID Connect and is used with known identity providers like Entra ID, Google Identity and Auth0. They also make it possible to use single sign on and much more making it enterprise-grade.
- **Modularity and flexibility**. JWTs can also be used with API Gateways like Azure API Management, NGINX and more. It also supports use authentication scenarios and server-to-service communication including impersonation and delegation scenarios.
- **Performance and caching**. JWTs can be cavhed after decoding which reduces the need for parsing. This helps specifically with high-traffic apps as it improves throughput and reduced load on your chosen infrastructure.
- **Advanced features**. It also supports introspection (checking validity on server) and revocation (making a token invalid).

With all of these benefits, let's see how we can take our implementation to the next level.

## Turning basic auth into JWT

So, the changes we need to at mile-high level is to:

- **Learn to construct a JWT token** and make it ready for being sent from client to server.
- **Validate a JWT token**, and if so, let the client have our resources.
- **Secure token storage**. How we store this token.
- **Protect the routes**. We need to protect the routes, in our case, we need to protect routes and specific MCP features.
- **Add refresh tokens**. Ensure we create tokens that are short-lived but refresh tokens that are long-lived that can be used to acquire new tokens if they expire. Also ensure there's a refresh endpoint and a rotation strategy.

### -1- Construct a JWT token

First off, a JWT token has the following parts:

- **header**, algorithm used and token type.
- **payload**, claimes, like sub (the user or entity the token represents. In an auth scenario this typically the userid), exp (when it expires) role (the role)
- **signature**, signed with a secret or private key.

**Python**

```python

import jwt
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import datetime

# Secret key used to sign the JWT
secret_key = 'your-secret-key'

header = {
    "alg": "HS256",
    "typ": "JWT"
}

# the user info andits claims and expiry time
payload = {
    "sub": "1234567890",               # Subject (user ID)
    "name": "User Userson",                # Custom claim
    "admin": True,                     # Custom claim
    "iat": datetime.datetime.utcnow(),# Issued at
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiry
}

# encode it
encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256", headers=header)
```

**TypeScript**

Dependencies

```sh

npm install jsonwebtoken
npm install --save-dev @types/jsonwebtoken
```

```typescript
import jwt from 'jsonwebtoken';

const secretKey = 'your-secret-key'; // Use env vars in production

// Define the payload
const payload = {
  sub: '1234567890',
  name: 'User usersson',
  admin: true,
  iat: Math.floor(Date.now() / 1000), // Issued at
  exp: Math.floor(Date.now() / 1000) + 60 * 60 // Expires in 1 hour
};

// Define the header (optional, jsonwebtoken sets defaults)
const header = {
  alg: 'HS256',
  typ: 'JWT'
};

// Create the token
const token = jwt.sign(payload, secretKey, {
  algorithm: 'HS256',
  header: header
});

console.log('JWT:', token);
```

This token is:

Signed using HS256
Valid for 1 hour
Includes claims like sub, name, admin, iat, and exp

### -2- Validate a token

To validate a token, we need to decode it so we can read it and then start checking its validity

**Python**

```python

# Decode and verify the JWT
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

**TypeScript**

```typescript

try {
  const decoded = jwt.verify(token, secretKey);
  console.log('Decoded Payload:', decoded);
} catch (err) {
  console.error('Token verification failed:', err);
}
```

## Adding role based access control

The idea is that we want to express that different roles have different permissions. For example, we assume an admin can do everything and that a normal users can do read/write and that a guest can only read. Therefore, here are some possible permission levels:

- Admin.Write 
- User.Read
- Guest.Read

Let's look at how we can implement such a control with middleware. Middlewares can be added per route as well as for all routes.

**Python**

```python
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import jwt

SECRET_KEY = "your-secret-key" # put this in env variable
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


# add middleware
# todo, add to one specific route

```

**TypeScript**

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

// todo, add to one specific route
```

### -3- Add RBAC to MCP

You've seen so far how you can add RBAC via middleware, however, for MCP there's no easy way to add a per MCP feature RBAC, so what do we do? Well, we just have to add code like this that checks in this case whether the client has the rights to call a specific tool:

**python**

```python
@tool()
def delete_product(id: int):
    try:
        check_permissions(role="Admin.Write", request)
    catch:
      pass # client failed authorization, raise authorization error
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
       // todo, send id to productService and remote entry
    } catch(Exception e) {
      console.log("Authorization error, you're not allowed");  
    }

    return {
      content: [{ type: "text", text: `Deletected product with id ${id}` }]
    };
  }
);
```

## Assignment 1: Build an mcp server and mcp client using basic authentication

Here you will take what you've learnt in terms of sending credentials through headers.

## Solution 1

[Solution 1](./solution/basic/README.md)

## Assignment 2: Upgrade the solution from Assignment 1 to use JWT

Take the first solution but this time, let's improve upon it. 

Here's how it should work, you should have a /login route and a /resource route.

```mermaid
sequenceDiagram
   participant Client
   participant Server

   Client->>Server: logging in, /login
   Server-->>Client: here's your token
   Client->>Server: get me my resources /resource, here's my token
   Server-->>Client: here's your resources
```

Below is roughly what gets sent between client and server and what output to expect.

```

POST /login
{
  "username": "jane.doe",
  "password": "secure123"
}
→ Server responds with:
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refreshToken": "..."
}

GET /resource
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
→ Server validates token and returns protected data

```

## Solution 2

[Solution 2](./solution/jwt-solution/README.md)

## Summary

You've hopefully learned a lot in this chapter, from no security at all, to basic security, to JWT and how it can be added to MCP.

We’ve built a solid foundation with custom JWTs, but as we scale, we’re moving toward a standards-based identity model. Adopting an IdP like Entra or Keycloak lets us offload token issuance, validation, and lifecycle management to a trusted platform — freeing us to focus on app logic and user experience.

For that, we have a more [advanced chapter on Entra](../../05-AdvancedTopics/mcp-security-entra/README.md)
