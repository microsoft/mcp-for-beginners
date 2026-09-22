# Exploration Approfondie des Fonctionnalités du Protocole MCP

Ce guide explore les fonctionnalités avancées du protocole MCP qui vont au-delà de la gestion basique des outils et des ressources. Comprendre ces fonctionnalités vous aide à construire des serveurs MCP plus robustes, conviviaux et prêts pour la production.

> **Portée de MCP `2026-07-28` :** le démarrage et l'arrêt du processus serveur restent
> des préoccupations applicatives, mais la poignée de main `initialize` MCP et les sessions au niveau du protocole
> sont supprimées. La section Journalisation ci-dessous est conservée pour les implémentations héritées ;
> les nouveaux serveurs doivent utiliser `stderr` ou OpenTelemetry. Tasks est
> désormais une extension versionnée séparément. Voir
> [Quoi de Neuf dans MCP : La Spécification 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

## Fonctionnalités Couvertes

1. **Notifications de Progression** - Rapporter la progression des opérations longues
2. **Annulation de Requête** - Permettre aux clients d'annuler des requêtes en cours
3. **Templates de Ressources** - URI de ressources dynamiques avec paramètres
4. **Cycle de Vie de l'Application** - Démarrage et arrêt du processus serveur
5. **Contrôle de la Journalisation (Hérité)** - Configuration de journalisation MCP dépréciée
6. **Modèles de Gestion des Erreurs** - Réponses d'erreur cohérentes

---

## 1. Notifications de Progression

Pour les opérations qui prennent du temps (traitement de données, téléchargements de fichiers, appels API), les notifications de progression maintiennent les utilisateurs informés.

### Comment ça Marche

```mermaid
sequenceDiagram
    participant Client
    participant Server
    
    Client->>Server: outils/appel (opération longue)
    Server-->>Client: notification : progression 10 %
    Server-->>Client: notification : progression 50 %
    Server-->>Client: notification : progression 90 %
    Server->>Client: résultat (terminé)
```

### Implémentation Python

```python
from mcp.server import Server, NotificationOptions
from mcp.types import ProgressNotification
import asyncio

app = Server("progress-server")

@app.tool()
async def process_large_file(file_path: str, ctx) -> str:
    """Process a large file with progress updates."""
    
    # Obtenir la taille du fichier pour le calcul de la progression
    file_size = os.path.getsize(file_path)
    processed = 0
    
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            # Traiter le segment
            await process_chunk(chunk)
            processed += len(chunk)
            
            # Envoyer une notification de progression
            progress = (processed / file_size) * 100
            await ctx.send_notification(
                ProgressNotification(
                    progressToken=ctx.request_id,
                    progress=progress,
                    total=100,
                    message=f"Processing: {progress:.1f}%"
                )
            )
    
    return f"Processed {file_size} bytes"

@app.tool()
async def batch_operation(items: list[str], ctx) -> str:
    """Process multiple items with progress."""
    
    results = []
    total = len(items)
    
    for i, item in enumerate(items):
        result = await process_item(item)
        results.append(result)
        
        # Rapporter la progression après chaque élément
        await ctx.send_notification(
            ProgressNotification(
                progressToken=ctx.request_id,
                progress=i + 1,
                total=total,
                message=f"Processed {i + 1}/{total}: {item}"
            )
        )
    
    return f"Completed {total} items"
```

### Implémentation TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";

server.setRequestHandler(CallToolSchema, async (request, extra) => {
  const { name, arguments: args } = request.params;
  
  if (name === "process_data") {
    const items = args.items as string[];
    const results = [];
    
    for (let i = 0; i < items.length; i++) {
      const result = await processItem(items[i]);
      results.push(result);
      
      // Envoyer une notification de progression
      await extra.sendNotification({
        method: "notifications/progress",
        params: {
          progressToken: request.id,
          progress: i + 1,
          total: items.length,
          message: `Processing item ${i + 1}/${items.length}`
        }
      });
    }
    
    return { content: [{ type: "text", text: JSON.stringify(results) }] };
  }
});
```

### Gestion Client (Python)

```python
async def handle_progress(notification):
    """Handle progress notifications from server."""
    params = notification.params
    print(f"Progress: {params.progress}/{params.total} - {params.message}")

# Enregistrer le gestionnaire
session.on_notification("notifications/progress", handle_progress)

# Appeler l'outil (les mises à jour de progression arriveront via le gestionnaire)
result = await session.call_tool("process_large_file", {"file_path": "/data/large.csv"})
```

---

## 2. Annulation de Requête

Permettre aux clients d'annuler des requêtes qui ne sont plus nécessaires ou qui prennent trop de temps.

### Implémentation Python

```python
from mcp.server import Server
from mcp.types import CancelledError
import asyncio

app = Server("cancellable-server")

@app.tool()
async def long_running_search(query: str, ctx) -> str:
    """Search that can be cancelled."""
    
    results = []
    
    try:
        for page in range(100):  # Rechercher à travers plusieurs pages
            # Vérifier si une annulation a été demandée
            if ctx.is_cancelled:
                raise CancelledError("Search cancelled by user")
            
            # Simuler la recherche de page
            page_results = await search_page(query, page)
            results.extend(page_results)
            
            # Un court délai permet les vérifications d'annulation
            await asyncio.sleep(0.1)
            
    except CancelledError:
        # Retourner des résultats partiels
        return f"Cancelled. Found {len(results)} results before cancellation."
    
    return f"Found {len(results)} total results"

@app.tool()
async def download_file(url: str, ctx) -> str:
    """Download with cancellation support."""
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            chunks = []
            
            async for chunk in response.content.iter_chunked(8192):
                if ctx.is_cancelled:
                    return f"Download cancelled at {downloaded}/{total_size} bytes"
                
                chunks.append(chunk)
                downloaded += len(chunk)
            
            return f"Downloaded {downloaded} bytes"
```

### Mise en œuvre du Contexte d'Annulation

```python
class CancellableContext:
    """Context object that tracks cancellation state."""
    
    def __init__(self, request_id: str):
        self.request_id = request_id
        self._cancelled = asyncio.Event()
        self._cancel_reason = None
    
    @property
    def is_cancelled(self) -> bool:
        return self._cancelled.is_set()
    
    def cancel(self, reason: str = "Cancelled"):
        self._cancel_reason = reason
        self._cancelled.set()
    
    async def check_cancelled(self):
        """Raise if cancelled, otherwise continue."""
        if self.is_cancelled:
            raise CancelledError(self._cancel_reason)
    
    async def sleep_or_cancel(self, seconds: float):
        """Sleep that can be interrupted by cancellation."""
        try:
            await asyncio.wait_for(
                self._cancelled.wait(),
                timeout=seconds
            )
            raise CancelledError(self._cancel_reason)
        except asyncio.TimeoutError:
            pass  # Délai d'attente normal, continuer
```

### Annulation côté Client

```python
import asyncio

async def search_with_timeout(session, query, timeout=30):
    """Search with automatic cancellation on timeout."""
    
    task = asyncio.create_task(
        session.call_tool("long_running_search", {"query": query})
    )
    
    try:
        result = await asyncio.wait_for(task, timeout=timeout)
        return result
    except asyncio.TimeoutError:
        # Annulation de la demande
        await session.send_notification({
            "method": "notifications/cancelled",
            "params": {"requestId": task.request_id, "reason": "Timeout"}
        })
        return "Search timed out"
```

---

## 3. Templates de Ressources

Les templates de ressources permettent la construction dynamique d'URI avec paramètres, utile pour les APIs et bases de données.

### Définition des Templates

```python
from mcp.server import Server
from mcp.types import ResourceTemplate

app = Server("template-server")

@app.list_resource_templates()
async def list_templates() -> list[ResourceTemplate]:
    """Return available resource templates."""
    return [
        ResourceTemplate(
            uriTemplate="db://users/{user_id}",
            name="User Profile",
            description="Fetch user profile by ID",
            mimeType="application/json"
        ),
        ResourceTemplate(
            uriTemplate="api://weather/{city}/{date}",
            name="Weather Data",
            description="Historical weather for city and date",
            mimeType="application/json"
        ),
        ResourceTemplate(
            uriTemplate="file://{path}",
            name="File Content",
            description="Read file at given path",
            mimeType="text/plain"
        )
    ]

@app.read_resource()
async def read_resource(uri: str) -> str:
    """Read resource, expanding template parameters."""
    
    # Analyser l'URI pour extraire les paramètres
    if uri.startswith("db://users/"):
        user_id = uri.split("/")[-1]
        return await fetch_user(user_id)
    
    elif uri.startswith("api://weather/"):
        parts = uri.replace("api://weather/", "").split("/")
        city, date = parts[0], parts[1]
        return await fetch_weather(city, date)
    
    elif uri.startswith("file://"):
        path = uri.replace("file://", "")
        return await read_file(path)
    
    raise ValueError(f"Unknown resource URI: {uri}")
```

### Implémentation TypeScript

```typescript
server.setRequestHandler(ListResourceTemplatesSchema, async () => {
  return {
    resourceTemplates: [
      {
        uriTemplate: "github://repos/{owner}/{repo}/issues/{issue_number}",
        name: "GitHub Issue",
        description: "Fetch a specific GitHub issue",
        mimeType: "application/json"
      },
      {
        uriTemplate: "db://tables/{table}/rows/{id}",
        name: "Database Row",
        description: "Fetch a row from a database table",
        mimeType: "application/json"
      }
    ]
  };
});

server.setRequestHandler(ReadResourceSchema, async (request) => {
  const uri = request.params.uri;
  
  // Analyser l'URI du problème GitHub
  const githubMatch = uri.match(/^github:\/\/repos\/([^/]+)\/([^/]+)\/issues\/(\d+)$/);
  if (githubMatch) {
    const [_, owner, repo, issueNumber] = githubMatch;
    const issue = await fetchGitHubIssue(owner, repo, parseInt(issueNumber));
    return {
      contents: [{
        uri,
        mimeType: "application/json",
        text: JSON.stringify(issue, null, 2)
      }]
    };
  }
  
  throw new Error(`Unknown resource URI: ${uri}`);
});
```

---

## 4. Cycle de Vie de l'Application

Cette section couvre le démarrage et l'arrêt du processus applicatif, pas la poignée de main `initialize`
MCP supprimée. Une gestion appropriée du cycle de vie garantit une gestion propre des ressources.


### Gestion du Cycle de Vie en Python

```python
from mcp.server import Server
from contextlib import asynccontextmanager

app = Server("lifecycle-server")

# État partagé
db_connection = None
cache = None

@asynccontextmanager
async def lifespan(server: Server):
    """Manage server lifecycle."""
    global db_connection, cache
    
    # Démarrage
    print("🚀 Server starting...")
    db_connection = await create_database_connection()
    cache = await create_cache_client()
    print("✅ Resources initialized")
    
    yield  # Le serveur s'exécute ici
    
    # Arrêt
    print("🛑 Server shutting down...")
    await db_connection.close()
    await cache.close()
    print("✅ Resources cleaned up")

app = Server("lifecycle-server", lifespan=lifespan)

@app.tool()
async def query_database(sql: str) -> str:
    """Use the shared database connection."""
    result = await db_connection.execute(sql)
    return str(result)
```

### Cycle de Vie TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";

class ManagedServer {
  private server: Server;
  private dbConnection: DatabaseConnection | null = null;
  
  constructor() {
    this.server = new Server({
      name: "lifecycle-server",
      version: "1.0.0"
    });
    
    this.setupHandlers();
  }
  
  async start() {
    // Initialiser les ressources
    console.log("🚀 Server starting...");
    this.dbConnection = await createDatabaseConnection();
    console.log("✅ Database connected");
    
    // Démarrer le serveur
    await this.server.connect(transport);
  }
  
  async stop() {
    // Nettoyer les ressources
    console.log("🛑 Server shutting down...");
    if (this.dbConnection) {
      await this.dbConnection.close();
    }
    await this.server.close();
    console.log("✅ Cleanup complete");
  }
  
  private setupHandlers() {
    this.server.setRequestHandler(CallToolSchema, async (request) => {
      // Utiliser this.dbConnection en toute sécurité
      // ...
    });
  }
}

// Utilisation avec arrêt progressif
const server = new ManagedServer();

process.on('SIGINT', async () => {
  await server.stop();
  process.exit(0);
});

await server.start();
```

---

## 5. Contrôle de la Journalisation (Hérité)

> [!WARNING]
> La journalisation MCP est dépréciée dans `2026-07-28` et est susceptible d'être supprimée dans
> la première révision de la spécification publiée à partir du 28 juillet 2027. Les exemples
> ci-dessous sont pour compatibilité avec les anciennes implémentations. Utilisez `stderr` avec
> stdio et OpenTelemetry pour une observabilité structurée dans les nouveaux serveurs.

Les versions héritées de MCP prennent en charge des niveaux de journalisation côté serveur que les clients peuvent contrôler.

### Mise en œuvre des Niveaux de Journalisation

```python
from mcp.server import Server
from mcp.types import LoggingLevel
import logging

app = Server("logging-server")

# Mapper les niveaux MCP aux niveaux de journalisation Python
LEVEL_MAP = {
    LoggingLevel.DEBUG: logging.DEBUG,
    LoggingLevel.INFO: logging.INFO,
    LoggingLevel.WARNING: logging.WARNING,
    LoggingLevel.ERROR: logging.ERROR,
}

logger = logging.getLogger("mcp-server")

@app.set_logging_level()
async def set_logging_level(level: LoggingLevel) -> None:
    """Handle client request to change logging level."""
    python_level = LEVEL_MAP.get(level, logging.INFO)
    logger.setLevel(python_level)
    logger.info(f"Logging level set to {level}")

@app.tool()
async def debug_operation(data: str) -> str:
    """Tool with various logging levels."""
    logger.debug(f"Processing data: {data}")
    
    try:
        result = process(data)
        logger.info(f"Successfully processed: {result}")
        return result
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        raise
```

### Envoi des Messages de Journal au Client

```python
@app.tool()
async def complex_operation(input: str, ctx) -> str:
    """Operation that logs to client."""
    
    # Envoyer une notification de journal au client
    await ctx.send_log(
        level="info",
        message=f"Starting complex operation with input: {input}"
    )
    
    # Faire le travail...
    result = await do_work(input)
    
    await ctx.send_log(
        level="debug",
        message=f"Operation complete, result size: {len(result)}"
    )
    
    return result
```

---

## 6. Modèles de Gestion des Erreurs

Une gestion cohérente des erreurs améliore le débogage et l'expérience utilisateur.

### Codes d'Erreur MCP

```python
from mcp.types import McpError, ErrorCode

class ToolError(McpError):
    """Base class for tool errors."""
    pass

class ValidationError(ToolError):
    """Invalid input parameters."""
    def __init__(self, message: str):
        super().__init__(ErrorCode.INVALID_PARAMS, message)

class NotFoundError(ToolError):
    """Requested resource not found."""
    def __init__(self, resource: str):
        super().__init__(ErrorCode.INVALID_REQUEST, f"Not found: {resource}")

class PermissionError(ToolError):
    """Access denied."""
    def __init__(self, action: str):
        super().__init__(ErrorCode.INVALID_REQUEST, f"Permission denied: {action}")

class InternalError(ToolError):
    """Internal server error."""
    def __init__(self, message: str):
        super().__init__(ErrorCode.INTERNAL_ERROR, message)
```

### Réponses d'Erreur Structurées

```python
@app.tool()
async def safe_operation(input: str) -> str:
    """Tool with comprehensive error handling."""
    
    # Valider l'entrée
    if not input:
        raise ValidationError("Input cannot be empty")
    
    if len(input) > 10000:
        raise ValidationError(f"Input too large: {len(input)} chars (max 10000)")
    
    try:
        # Vérifier les permissions
        if not await check_permission(input):
            raise PermissionError(f"read {input}")
        
        # Effectuer l'opération
        result = await perform_operation(input)
        
        if result is None:
            raise NotFoundError(input)
        
        return result
        
    except ConnectionError as e:
        raise InternalError(f"Database connection failed: {e}")
    except TimeoutError as e:
        raise InternalError(f"Operation timed out: {e}")
    except Exception as e:
        # Enregistrer les erreurs inattendues
        logger.exception(f"Unexpected error in safe_operation")
        raise InternalError(f"Unexpected error: {type(e).__name__}")
```

### Gestion des Erreurs en TypeScript

```typescript
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";

function validateInput(data: unknown): asserts data is ValidInput {
  if (typeof data !== "object" || data === null) {
    throw new McpError(
      ErrorCode.InvalidParams,
      "Input must be an object"
    );
  }
  // Plus de validation...
}

server.setRequestHandler(CallToolSchema, async (request) => {
  try {
    validateInput(request.params.arguments);
    
    const result = await performOperation(request.params.arguments);
    
    return {
      content: [{ type: "text", text: JSON.stringify(result) }]
    };
    
  } catch (error) {
    if (error instanceof McpError) {
      throw error;  // Erreur MCP déjà existante
    }
    
    // Convertir d'autres erreurs
    if (error instanceof NotFoundError) {
      throw new McpError(ErrorCode.InvalidRequest, error.message);
    }
    
    // Erreur inconnue
    console.error("Unexpected error:", error);
    throw new McpError(
      ErrorCode.InternalError,
      "An unexpected error occurred"
    );
  }
});
```

---

## Fonctionnalités Sensibles à la Version

### Extension Tasks

Tasks est une extension officielle, versionnée séparément dans MCP `2026-07-28`. Un
serveur peut retourner une poignée de tâche à partir d'un appel d'outil, et le client pilote la tâche
avec `tasks/get`, `tasks/update` et `tasks/cancel`. L'API expérimentale
`2025-11-25` Tasks n'est pas rétrocompatible, et `tasks/list` n'existe
plus.

### Annotations d'Outil

Les annotations d'outil décrivent des comportements tels que lecture seule, destructif, idempotent,
ou opération en monde ouvert. Ce sont des indices et ne doivent pas être considérés comme des garanties
d'autorisation ou de sécurité de confiance à moins qu'ils ne proviennent d'un serveur de confiance.

---

## Prochaines Étapes

- [Module 8 - Bonnes Pratiques](../../08-BestPractices/README.md)
- [5.14 - Ingénierie du Contexte](../mcp-contextengineering/README.md)
- [Journal des Changements de la Spécification MCP](https://modelcontextprotocol.io/specification/2026-07-28/changelog)

---

## Ressources Supplémentaires

- [Spécification MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Codes d'Erreur JSON-RPC 2.0](https://www.jsonrpc.org/specification#error_object)
- [Exemples SDK Python](https://github.com/modelcontextprotocol/python-sdk/tree/main/examples)
- [Exemples SDK TypeScript](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->