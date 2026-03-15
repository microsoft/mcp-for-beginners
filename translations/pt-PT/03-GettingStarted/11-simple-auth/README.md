# Autenticação simples

Os SDKs MCP suportam o uso de OAuth 2.1 que, para ser justo, é um processo bastante complexo envolvendo conceitos como servidor de autenticação, servidor de recursos, envio de credenciais, obtenção de um código, troca do código por um token bearer até finalmente conseguir aceder aos dados do recurso. Se não estiver habituado ao OAuth, que é algo ótimo para implementar, é uma boa ideia começar com algum nível básico de autenticação e evoluir para uma segurança cada vez melhor. É por isso que este capítulo existe, para o levar a uma autenticação mais avançada.

## Autenticação, o que queremos dizer?

Auth é a abreviação de autenticação e autorização. A ideia é que precisamos de fazer duas coisas:

- **Autenticação**, que é o processo de descobrir se deixamos uma pessoa entrar na nossa casa, se ela tem o direito de estar "aqui", ou seja, ter acesso ao nosso servidor de recursos onde vivem as funcionalidades do nosso servidor MCP.
- **Autorização**, é o processo de descobrir se um utilizador deve ter acesso a esses recursos específicos que está a pedir, por exemplo, estas encomendas ou estes produtos, ou se está autorizado a ler o conteúdo mas não a apagar, como outro exemplo.

## Credenciais: como dizemos ao sistema quem somos

Bem, a maioria dos programadores web começa a pensar em fornecer uma credencial ao servidor, geralmente um segredo que indica se podem estar aqui "Autenticação". Esta credencial é normalmente uma versão codificada em base64 do nome de utilizador e palavra-passe ou uma chave API que identifica de forma única um utilizador específico.

Isto envolve enviá-la através de um cabeçalho chamado "Authorization" assim:

```json
{ "Authorization": "secret123" }
```

Isto é normalmente referido como autenticação básica. O fluxo geral funciona da seguinte maneira:

```mermaid
sequenceDiagram
   participant User
   participant Client
   participant Server

   User->>Client: mostra-me os dados
   Client->>Server: mostra-me os dados, aqui estão as minhas credenciais
   Server-->>Client: 1a, conheço-te, aqui estão os teus dados
   Server-->>Client: 1b, não te conheço, 401 
```
Agora que compreendemos como funciona do ponto de vista do fluxo, como é que o implementamos? Bem, a maioria dos servidores web tem um conceito chamado middleware, um pedaço de código que corre como parte da requisição e que pode verificar credenciais, e se as credenciais forem válidas pode deixar a requisição passar. Se a requisição não tiver credenciais válidas, então recebe um erro de autenticação. Vamos ver como isto pode ser implementado:

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
        # adicionar quaisquer cabeçalhos do cliente ou alterar a resposta de alguma forma
        return response


starlette_app.add_middleware(CustomHeaderMiddleware)
```

Aqui temos:

- Criado um middleware chamado `AuthMiddleware` em que o seu método `dispatch` é invocado pelo servidor web.
- Adicionado o middleware ao servidor web:

    ```python
    starlette_app.add_middleware(AuthMiddleware)
    ```

- Escrito a lógica de validação que verifica se o cabeçalho Authorization está presente e se o segredo enviado é válido:

    ```python
    has_header = request.headers.get("Authorization")
    if not has_header:
        print("-> Missing Authorization header!")
        return Response(status_code=401, content="Unauthorized")

    if not valid_token(has_header):
        print("-> Invalid token!")
        return Response(status_code=403, content="Forbidden")
    ```

    se o segredo estiver presente e válido, deixamos a requisição passar chamando `call_next` e retornamos a resposta.

    ```python
    response = await call_next(request)
    # adicionar quaisquer cabeçalhos de cliente ou alterar a resposta de alguma forma
    return response
    ```

Como funciona é que se for feita uma requisição web ao servidor, o middleware será invocado e, dada a sua implementação, vai permitir que a requisição passe ou acaba por devolver um erro que indica que o cliente não tem autorização para continuar.

**TypeScript**

Aqui criamos um middleware com o popular framework Express e interceptamos a requisição antes de chegar ao servidor MCP. Aqui está o código:

```typescript
function isValid(secret) {
    return secret === "secret123";
}

app.use((req, res, next) => {
    // 1. Cabeçalho de autorização presente?
    if(!req.headers["Authorization"]) {
        res.status(401).send('Unauthorized');
    }
    
    let token = req.headers["Authorization"];

    // 2. Verificar validade.
    if(!isValid(token)) {
        res.status(403).send('Forbidden');
    }

   
    console.log('Middleware executed');
    // 3. Passa a requisição para o próximo passo no pipeline da requisição.
    next();
});
```

Neste código nós:

1. Verificamos se o cabeçalho Authorization está presente, se não estiver, enviamos um erro 401.
2. Garantimos que a credencial/token é válido, se não for, enviamos um erro 403.
3. Finalmente passa a requisição na pipeline e retorna o recurso solicitado.

## Exercício: Implementar autenticação

Vamos aplicar os nossos conhecimentos e tentar implementar. Aqui está o plano:

Servidor

- Criar um servidor web e instância MCP.
- Implementar um middleware para o servidor.

Cliente

- Enviar uma requisição web com credencial via cabeçalho.

### -1- Criar um servidor web e instância MCP

No primeiro passo, precisamos criar a instância do servidor web e do servidor MCP.

**Python**

Aqui criamos uma instância do servidor MCP, criamos uma aplicação web starlette e hospedamo-la com uvicorn.

```python
# a criar servidor MCP

app = FastMCP(
    name="MCP Resource Server",
    instructions="Resource Server that validates tokens via Authorization Server introspection",
    host=settings["host"],
    port=settings["port"],
    debug=True
)

# a criar aplicação web starlette
starlette_app = app.streamable_http_app()

# a servir aplicação via uvicorn
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

Neste código nós:

- Criamos o servidor MCP.
- Construímos a aplicação web starlette a partir do servidor MCP, `app.streamable_http_app()`.
- Hospedamos e servimos a aplicação web usando uvicorn `server.serve()`.

**TypeScript**

Aqui criamos uma instância do servidor MCP.

```typescript
const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    });

    // ... configurar recursos do servidor, ferramentas e sugestões ...
```

A criação do servidor MCP vai precisar acontecer dentro da definição da rota POST /mcp, por isso vamos pegar no código acima e movê-lo assim:

```typescript
import express from "express";
import { randomUUID } from "node:crypto";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { isInitializeRequest } from "@modelcontextprotocol/sdk/types.js"

const app = express();
app.use(express.json());

// Mapa para armazenar transportes por ID de sessão
const transports: { [sessionId: string]: StreamableHTTPServerTransport } = {};

// Tratar pedidos POST para comunicação cliente-servidor
app.post('/mcp', async (req, res) => {
  // Verificar se existe ID de sessão
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  let transport: StreamableHTTPServerTransport;

  if (sessionId && transports[sessionId]) {
    // Reutilizar transporte existente
    transport = transports[sessionId];
  } else if (!sessionId && isInitializeRequest(req.body)) {
    // Novo pedido de inicialização
    transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: () => randomUUID(),
      onsessioninitialized: (sessionId) => {
        // Armazenar o transporte pelo ID de sessão
        transports[sessionId] = transport;
      },
      // A proteção contra DNS rebinding está desativada por defeito para compatibilidade retroativa. Se estiver a executar este servidor
      // localmente, certifique-se de definir:
      // enableDnsRebindingProtection: true,
      // allowedHosts: ['127.0.0.1'],
    });

    // Limpar transporte quando fechado
    transport.onclose = () => {
      if (transport.sessionId) {
        delete transports[transport.sessionId];
      }
    };
    const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    });

    // ... configurar recursos do servidor, ferramentas e prompts ...

    // Ligar ao servidor MCP
    await server.connect(transport);
  } else {
    // Pedido inválido
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

  // Tratar o pedido
  await transport.handleRequest(req, res, req.body);
});

// Manipulador reutilizável para pedidos GET e DELETE
const handleSessionRequest = async (req: express.Request, res: express.Response) => {
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  if (!sessionId || !transports[sessionId]) {
    res.status(400).send('Invalid or missing session ID');
    return;
  }
  
  const transport = transports[sessionId];
  await transport.handleRequest(req, res);
};

// Tratar pedidos GET para notificações do servidor para o cliente via SSE
app.get('/mcp', handleSessionRequest);

// Tratar pedidos DELETE para terminação de sessão
app.delete('/mcp', handleSessionRequest);

app.listen(3000);
```

Agora vê como a criação do servidor MCP foi movida para dentro de `app.post("/mcp")`.

Vamos avançar para o próximo passo de criar o middleware para podermos validar a credencial recebida.

### -2- Implementar um middleware para o servidor

Vamos agora à parte do middleware. Aqui vamos criar um middleware que procura uma credencial no cabeçalho `Authorization` e a valida. Se for aceitável, a requisição continuará e fará o que for necessário (ex: listar ferramentas, ler um recurso ou qualquer funcionalidade MCP que o cliente pediu).

**Python**

Para criar o middleware, precisamos de criar uma classe que herde de `BaseHTTPMiddleware`. Há duas partes interessantes:

- A requisição `request`, da qual lemos a informação do cabeçalho.
- `call_next`, o callback que precisamos invocar se o cliente trouxer uma credencial que aceitamos.

Primeiro, precisamos tratar o caso em que o cabeçalho `Authorization` está em falta:

```python
has_header = request.headers.get("Authorization")

# nenhum cabeçalho presente, falhar com 401, caso contrário continuar.
if not has_header:
    print("-> Missing Authorization header!")
    return Response(status_code=401, content="Unauthorized")
```

Aqui enviamos uma mensagem 401 unauthorized pois o cliente está a falhar na autenticação.

De seguida, se uma credencial foi submetida, precisamos de verificar a sua validade assim:

```python
 if not valid_token(has_header):
    print("-> Invalid token!")
    return Response(status_code=403, content="Forbidden")
```

Repare como enviamos uma mensagem 403 forbidden acima. Vamos ver o middleware completo abaixo implementando tudo o que mencionámos:

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

Ótimo, mas o que é a função `valid_token`? Aqui está ela abaixo:

```python
# NÃO usar para produção - melhorar !!
def valid_token(token: str) -> bool:
    # remover o prefixo "Bearer "
    if token.startswith("Bearer "):
        token = token[7:]
        return token == "secret-token"
    return False
```

Obviamente, isto deve melhorar.

IMPORTANTE: Nunca deve ter segredos assim diretamente no código. Idealmente, deve obter o valor a comparar de uma fonte de dados ou de um IDP (fornecedor de serviço de identidade) ou melhor ainda, deixar que o IDP faça a validação.

**TypeScript**

Para implementar isto com Express, precisamos de chamar o método `use` que recebe funções middleware.

Precisamos de:

- Interagir com a variável da requisição para verificar a credencial passada na propriedade `Authorization`.
- Validar a credencial, e se for válida deixar a requisição continuar e permitir que o pedido MCP do cliente faça o que deva (ex: listar ferramentas, ler recurso ou outro relacionado a MCP).

Aqui estamos a verificar se o cabeçalho `Authorization` está presente e se não estiver, interrompemos a requisição:

```typescript
if(!req.headers["authorization"]) {
    res.status(401).send('Unauthorized');
    return;
}
```

Se o cabeçalho não for enviado, recebe um erro 401.

De seguida, verificamos se a credencial é válida, se não for voltamos a interromper a requisição com uma mensagem diferente:

```typescript
if(!isValid(token)) {
    res.status(403).send('Forbidden');
    return;
} 
```

Repare que agora recebe um erro 403.

Aqui está o código completo:

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

Configurámos o servidor web para aceitar um middleware que verifica a credencial que o cliente, esperançosamente, está a enviar. E o cliente em si?

### -3- Enviar requisição web com credencial via cabeçalho

Precisamos garantir que o cliente está a passar a credencial através do cabeçalho. Como vamos usar um cliente MCP para isso, precisamos de descobrir como se faz.

**Python**

Para o cliente, precisamos passar um cabeçalho com a nossa credencial assim:

```python
# NÃO codifique o valor diretamente, tenha-o pelo menos numa variável de ambiente ou num armazenamento mais seguro
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
      
            # POR FAZER, o que quer que seja feito no cliente, por exemplo listar ferramentas, chamar ferramentas, etc.
```

Repare como preenchermos a propriedade `headers` assim ` headers = {"Authorization": f"Bearer {token}"}`.

**TypeScript**

Podemos fazer isto em dois passos:

1. Preencher um objeto de configuração com a nossa credencial.
2. Passar o objeto de configuração para o transporte.

```typescript

// NÃO codifique o valor diretamente como mostrado aqui. No mínimo, tenha-o como uma variável de ambiente e use algo como dotenv (em modo de desenvolvimento).
let token = "secret123"

// defina um objeto de opções de transporte do cliente
let options: StreamableHTTPClientTransportOptions = {
  sessionId: sessionId,
  requestInit: {
    headers: {
      "Authorization": "secret123"
    }
  }
};

// passe o objeto de opções para o transporte
async function main() {
   const transport = new StreamableHTTPClientTransport(
      new URL(serverUrl),
      options
   );
```

Aqui vê como tivemos de criar um objeto `options` e colocar os nossos headers na propriedade `requestInit`.

IMPORTANTE: Como melhorar isto a partir daqui? Bem, a implementação atual tem algumas falhas. Em primeiro lugar, passar uma credencial assim é bastante arriscado a menos que tenha HTTPS. Mesmo assim, a credencial pode ser roubada, por isso precisa de um sistema onde possa revogar facilmente o token e adicionar verificações adicionais como: de onde no mundo vem, se a requisição acontece demasiado frequentemente (comportamento tipo bot), resumindo, há muitas preocupações.

Dito isto, para APIs muito simples em que não quer que ninguém chame a sua API sem autenticação, o que temos aqui é um bom começo.

Com isso, vamos tentar reforçar a segurança um pouco mais usando um formato padronizado como o JSON Web Token, também conhecido como JWT ou tokens "JOT".

## JSON Web Tokens, JWT

Então, estamos a tentar melhorar as coisas em relação ao envio de credenciais muito simples. Quais as melhorias imediatas que obtemos adotando JWT?

- **Melhorias de segurança**. Na autenticação básica, envia-se o nome de utilizador e palavra-passe como um token codificado em base64 (ou uma chave API) repetidamente, o que aumenta o risco. Com JWT, envia-se o nome de utilizador e palavra-passe e recebe-se um token em troca que também tem validade temporal, ou seja, expira. O JWT permite facilmente usar controlo de acesso granular através de roles, scopes e permissões.
- **Ausência de estado e escalabilidade**. Os JWT são auto-contidos, transportam toda a informação do utilizador e eliminam a necessidade de armazenamento de sessão do lado do servidor. O token também pode ser validado localmente.
- **Interoperabilidade e federação**. Os JWT são centrais no Open ID Connect e usados com fornecedores de identidade conhecidos como Entra ID, Google Identity e Auth0. Também possibilitam o uso de single sign on e muito mais, tornando-se aptos para empresas.
- **Modularidade e flexibilidade**. Os JWT também podem ser usados com API Gateways como Azure API Management, NGINX e outros. Suportam cenários de autenticação de utilizador e comunicação servidor-a-servidor incluindo impersonações e delegações.
- **Performance e caching**. Os JWT podem ser cacheados após decodificação, o que reduz a necessidade de o analisar múltiplas vezes. Ajuda especialmente em apps com tráfego elevado, pois melhora a capacidade e reduz a carga na infraestrutura escolhida.
- **Funcionalidades avançadas**. Suportam introspeção (verificação da validade no servidor) e revogação (tornar um token inválido).

Com todos estes benefícios, vamos ver como podemos levar a nossa implementação para o próximo nível.

## Transformar autenticação básica em JWT

Então, as alterações a alto nível que precisamos de fazer são:

- **Aprender a construir um token JWT** e deixá-lo pronto para ser enviado do cliente para o servidor.
- **Validar um token JWT** e, se válido, permitir que o cliente aceda aos nossos recursos.
- **Armazenamento seguro do token**. Como armazenamos este token.
- **Proteger as rotas**. Precisamos proteger as rotas, no nosso caso, proteger rotas específicas e funcionalidades MCP específicas.
- **Adicionar tokens de atualização**. Garantir que criamos tokens de curta duração mas tokens de atualização de longa duração que podem ser usados para adquirir novos tokens quando estes expirarem. Também garantir que existe um endpoint de refresh e uma estratégia de rotação.

### -1- Construir um token JWT

Para começar, um token JWT tem as seguintes partes:

- **header**, algoritmo usado e tipo do token.
- **payload**, claims, como sub (o utilizador ou entidade que o token representa. Numa autenticação, normalmente o userid), exp (quando expira) role (a role).
- **signature**, assinada com um segredo ou chave privada.

Para isso, vamos precisar construir o header, o payload e o token codificado.

**Python**

```python

import jwt
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import datetime

# Chave secreta usada para assinar o JWT
secret_key = 'your-secret-key'

header = {
    "alg": "HS256",
    "typ": "JWT"
}

# a informação do utilizador, as suas declarações e o tempo de expiração
payload = {
    "sub": "1234567890",               # Sujeito (ID do utilizador)
    "name": "User Userson",                # Declaração personalizada
    "admin": True,                     # Declaração personalizada
    "iat": datetime.datetime.utcnow(),# Emitido em
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiração
}

# codificá-lo
encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256", headers=header)
```

No código acima nós:

- Definimos um header usando HS256 como algoritmo e tipo JWT.
- Construímos um payload que contém um subject ou user id, um nome de utilizador, uma role, quando foi emitido e quando vai expirar, implementando assim o aspeto temporal que mencionámos antes.

**TypeScript**

Aqui vamos precisar de algumas dependências que vão ajudar-nos a construir o token JWT.

Dependências

```sh

npm install jsonwebtoken
npm install --save-dev @types/jsonwebtoken
```

Agora que temos isso em funcionamento, vamos criar o header, payload e, através destes, criar o token codificado.

```typescript
import jwt from 'jsonwebtoken';

const secretKey = 'your-secret-key'; // Usar variáveis de ambiente em produção

// Definir a carga útil
const payload = {
  sub: '1234567890',
  name: 'User usersson',
  admin: true,
  iat: Math.floor(Date.now() / 1000), // Emitido em
  exp: Math.floor(Date.now() / 1000) + 60 * 60 // Expira em 1 hora
};

// Definir o cabeçalho (opcional, jsonwebtoken define padrões)
const header = {
  alg: 'HS256',
  typ: 'JWT'
};

// Criar o token
const token = jwt.sign(payload, secretKey, {
  algorithm: 'HS256',
  header: header
});

console.log('JWT:', token);
```

Este token é:

Assinado usando HS256
Válido por 1 hora
Inclui claims como sub, name, admin, iat e exp.

### -2- Validar um token

Também precisaremos de validar um token, isto é algo que devemos fazer no servidor para garantir que o que o cliente está a enviar é de facto válido. Existem vários testes que deveríamos fazer, desde validar a sua estrutura até à validade. Também é recomendado fazer outras verificações para garantir que o utilizador está no nosso sistema e mais.

Para validar um token, precisamos decodificá-lo para podermos lê-lo e depois começar a verificar a sua validade:

**Python**

```python

# Decodificar e verificar o JWT
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

Neste código, chamamos `jwt.decode` usando o token, a chave secreta e o algoritmo escolhido como entrada. Repare que usamos um bloco try-catch pois uma validação falhada leva ao lançamento de um erro.

**TypeScript**

Aqui precisamos chamar `jwt.verify` para obter uma versão decodificada do token que podemos analisar mais profundamente. Se esta chamada falhar, significa que a estrutura do token está incorreta ou que já não é válido.

```typescript

try {
  const decoded = jwt.verify(token, secretKey);
  console.log('Decoded Payload:', decoded);
} catch (err) {
  console.error('Token verification failed:', err);
}
```

NOTA: como mencionado anteriormente, devemos realizar verificações adicionais para garantir que este token corresponde a um utilizador no nosso sistema e garantir que o utilizador tem os direitos que alega ter.

De seguida, vamos olhar para controlo de acesso baseado em funções, também conhecido como RBAC.
## Adicionar controlo de acesso baseado em funções

A ideia é que queremos expressar que diferentes funções têm permissões diferentes. Por exemplo, assumimos que um administrador pode fazer tudo, que um utilizador normal pode ler/escrever e que um convidado só pode ler. Portanto, aqui estão alguns possíveis níveis de permissão:

- Admin.Write 
- User.Read
- Guest.Read

Vamos ver como podemos implementar esse controlo com middleware. Middlewares podem ser adicionados por rota assim como para todas as rotas.

**Python**

```python
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import jwt

# NÃO tenha o segredo no código, isto é apenas para fins de demonstração. Leia-o de um local seguro.
SECRET_KEY = "your-secret-key" # coloque isto numa variável de ambiente
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

Existem algumas formas diferentes de adicionar o middleware como abaixo:

```python

# Alt 1: adicionar middleware durante a construção da aplicação starlette
middleware = [
    Middleware(JWTPermissionMiddleware)
]

app = Starlette(routes=routes, middleware=middleware)

# Alt 2: adicionar middleware depois de a aplicação starlette já estar construída
starlette_app.add_middleware(JWTPermissionMiddleware)

# Alt 3: adicionar middleware por rota
routes = [
    Route(
        "/mcp",
        endpoint=..., # manipulador
        middleware=[Middleware(JWTPermissionMiddleware)]
    )
]
```

**TypeScript**

Podemos usar `app.use` e um middleware que será executado para todas as requisições.

```typescript
app.use((req, res, next) => {
    console.log('Request received:', req.method, req.url, req.headers);
    console.log('Headers:', req.headers["authorization"]);

    // 1. Verifique se o cabeçalho de autorização foi enviado

    if(!req.headers["authorization"]) {
        res.status(401).send('Unauthorized');
        return;
    }
    
    let token = req.headers["authorization"];

    // 2. Verifique se o token é válido
    if(!isValid(token)) {
        res.status(403).send('Forbidden');
        return;
    }  

    // 3. Verifique se o utilizador do token existe no nosso sistema
    if(!isExistingUser(token)) {
        res.status(403).send('Forbidden');
        console.log("User does not exist");
        return;
    }
    console.log("User exists");

    // 4. Verifique se o token tem as permissões corretas
    if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }

    console.log("User has required scopes");

    console.log('Middleware executed');
    next();
});

```

Há várias coisas que podemos deixar o nosso middleware fazer e que o middleware DEVE fazer, nomeadamente:

1. Verificar se o cabeçalho de autorização está presente
2. Verificar se o token é válido, chamamos `isValid` que é um método que escrevemos para verificar a integridade e validade do token JWT.
3. Verificar se o utilizador existe no nosso sistema, devemos fazer esta verificação.

   ```typescript
    // utilizadores na BD
   const users = [
     "user1",
     "User usersson",
   ]

   function isExistingUser(token) {
     let decodedToken = verifyToken(token);

     // TODO, verificar se o utilizador existe na BD
     return users.includes(decodedToken?.name || "");
   }
   ```

   Acima, criámos uma lista muito simples de `users`, que obviamente deveria estar numa base de dados.

4. Além disso, também devemos verificar se o token tem as permissões corretas.

   ```typescript
   if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
   }
   ```

   No código acima do middleware, verificamos que o token contém a permissão User.Read, caso contrário enviamos um erro 403. Abaixo está o método auxiliar `hasScopes`.

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

Agora que viu como o middleware pode ser usado tanto para autenticação como para autorização, e quanto ao MCP, será que muda a forma como fazemos a autenticação? Vamos descobrir na próxima secção.

### -3- Adicionar RBAC ao MCP

Até agora viu como pode adicionar RBAC via middleware, no entanto, para MCP não há uma forma fácil de adicionar RBAC por funcionalidade MCP, então o que fazemos? Bem, temos apenas de adicionar código como este que verifica, neste caso, se o cliente tem os direitos para chamar uma ferramenta específica:

Tem algumas escolhas diferentes sobre como conseguir RBAC por funcionalidade, aqui estão algumas:

- Adicionar uma verificação para cada ferramenta, recurso, prompt onde precisa de verificar o nível de permissão.

   **python**

   ```python
   @tool()
   def delete_product(id: int):
      try:
          check_permissions(role="Admin.Write", request)
      catch:
        pass # o cliente falhou na autorização, gerar erro de autorização
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
        // todo, enviar id para productService e entrada remota
      } catch(Exception e) {
        console.log("Authorization error, you're not allowed");  
      }

      return {
        content: [{ type: "text", text: `Deletected product with id ${id}` }]
      };
    }
   );
   ```


- Usar abordagem avançada de servidor e os handlers de requisição para minimizar quantos locais é preciso fazer a verificação.

   **Python**

   ```python
   
   tool_permission = {
      "create_product": ["User.Write", "Admin.Write"],
      "delete_product": ["Admin.Write"]
   }

   def has_permission(user_permissions, required_permissions) -> bool:
      # user_permissions: lista de permissões que o utilizador tem
      # required_permissions: lista de permissões necessárias para a ferramenta
      return any(perm in user_permissions for perm in required_permissions)

   @server.call_tool()
   async def handle_call_tool(
     name: str, arguments: dict[str, str] | None
   ) -> list[types.TextContent]:
    # Assuma que request.user.permissions é uma lista de permissões para o utilizador
     user_permissions = request.user.permissions
     required_permissions = tool_permission.get(name, [])
     if not has_permission(user_permissions, required_permissions):
        # Levantar erro "Não tem permissão para usar a ferramenta {name}"
        raise Exception(f"You don't have permission to call tool {name}")
     # continuar e chamar a ferramenta
     # ...
   ```   
   

   **TypeScript**

   ```typescript
   function hasPermission(userPermissions: string[], requiredPermissions: string[]): boolean {
       if (!Array.isArray(userPermissions) || !Array.isArray(requiredPermissions)) return false;
       // Retorna verdadeiro se o utilizador tiver pelo menos uma permissão necessária
       
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

   Note que terá de garantir que o seu middleware atribui um token decodificado à propriedade user da requisição para que o código acima seja simples.

### Resumo

Agora que discutimos como adicionar suporte para RBAC em geral e para MCP em particular, é altura de tentar implementar a segurança por si próprio para garantir que compreendeu os conceitos apresentados.

## Exercício 1: Construir um servidor mcp e cliente mcp usando autenticação básica

Aqui vai aplicar o que aprendeu em termos de enviar credenciais através dos cabeçalhos.

## Solução 1

[Solução 1](./code/basic/README.md)

## Exercício 2: Atualizar a solução do Exercício 1 para usar JWT

Pegue na primeira solução, mas desta vez vamos melhorar.

Em vez de usar Autenticação Básica, vamos usar JWT.

## Solução 2

[Solução 2](./solution/jwt-solution/README.md)

## Desafio

Adicionar o RBAC por ferramenta que descrevemos na secção "Adicionar RBAC ao MCP".

## Sumário

Esperamos que tenha aprendido bastante neste capítulo, desde ausência total de segurança, à segurança básica, até JWT e como pode ser adicionada ao MCP.

Construímos uma base sólida com JWTs personalizados, mas à medida que escalamos, estamos a migrar para um modelo de identidade baseado em standards. Adotar um IdP como Entra ou Keycloak permite transferir a emissão, validação e gestão do ciclo de vida dos tokens para uma plataforma confiável — libertando-nos para focar na lógica da aplicação e experiência do utilizador.

Para isso, temos um [capítulo mais avançado sobre Entra](../../05-AdvancedTopics/mcp-security-entra/README.md).

## O que vem a seguir

- Seguinte: [Configurar Hosts MCP](../12-mcp-hosts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->