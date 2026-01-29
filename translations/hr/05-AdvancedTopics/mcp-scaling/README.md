# Skalabilnost i visokoučinkoviti MCP

Za implementacije u poduzećima, MCP često mora obrađivati velike količine zahtjeva s minimalnim kašnjenjem.

## Uvod

U ovoj lekciji istražit ćemo strategije za skaliranje MCP servera kako bismo učinkovito upravljali velikim opterećenjima. Pokrit ćemo horizontalno i vertikalno skaliranje, optimizaciju resursa i distribuirane arhitekture.

## Ciljevi učenja

Na kraju ove lekcije moći ćete:

- Implementirati horizontalno skaliranje koristeći balansiranje opterećenja i distribuirano keširanje.
- Optimizirati MCP servere za vertikalno skaliranje i upravljanje resursima.
- Dizajnirati distribuirane MCP arhitekture za visoku dostupnost i otpornost na greške.
- Koristiti napredne alate i tehnike za praćenje performansi i optimizaciju.
- Primijeniti najbolje prakse za skaliranje MCP servera u produkcijskim okruženjima.

## Strategije skalabilnosti

Postoji nekoliko strategija za učinkovito skaliranje MCP servera:

- **Horizontalno skaliranje**: Postavljanje više instanci MCP servera iza load balancera za ravnomjernu raspodjelu dolaznih zahtjeva.
- **Vertikalno skaliranje**: Optimizacija jedne instance MCP servera za obradu većeg broja zahtjeva povećanjem resursa (CPU, memorija) i podešavanjem konfiguracija.
- **Optimizacija resursa**: Korištenje učinkovitih algoritama, keširanja i asinkronog procesiranja za smanjenje potrošnje resursa i poboljšanje vremena odziva.
- **Distribuirana arhitektura**: Implementacija distribuiranog sustava u kojem više MCP čvorova surađuje, dijeleći opterećenje i osiguravajući redundanciju.

## Horizontalno skaliranje

Horizontalno skaliranje podrazumijeva postavljanje više instanci MCP servera i korištenje load balancera za raspodjelu dolaznih zahtjeva. Ovaj pristup omogućuje istovremenu obradu većeg broja zahtjeva i pruža otpornost na greške.

Pogledajmo primjer kako konfigurirati horizontalno skaliranje i MCP.

### [.NET](../../../../05-AdvancedTopics/mcp-scaling)

```csharp
// ASP.NET Core MCP load balancing configuration
public class McpLoadBalancedStartup
{
    public void ConfigureServices(IServiceCollection services)
    {
        // Configure distributed cache for session state
        services.AddStackExchangeRedisCache(options =>
        {
            options.Configuration = Configuration.GetConnectionString("RedisConnection");
            options.InstanceName = "MCP_";
        });
        
        // Configure MCP with distributed caching
        services.AddMcpServer(options =>
        {
            options.ServerName = "Scalable MCP Server";
            options.ServerVersion = "1.0.0";
            options.EnableDistributedCaching = true;
            options.CacheExpirationMinutes = 60;
        });
        
        // Register tools
        services.AddMcpTool<HighPerformanceTool>();
    }
}
```

U prethodnom kodu smo:

- Konfigurirali distribuirani keš koristeći Redis za pohranu stanja sesije i podataka alata.
- Omogućili distribuirano keširanje u konfiguraciji MCP servera.
- Registrirali visokoučinkoviti alat koji se može koristiti na više MCP instanci.

---

## Vertikalno skaliranje i optimizacija resursa

Vertikalno skaliranje fokusira se na optimizaciju jedne instance MCP servera za učinkovitiju obradu većeg broja zahtjeva. To se postiže podešavanjem konfiguracija, korištenjem učinkovitih algoritama i učinkovitim upravljanjem resursima. Na primjer, možete prilagoditi thread poolove, timeoutove zahtjeva i memorijske limite za poboljšanje performansi.

Pogledajmo primjer kako optimizirati MCP server za vertikalno skaliranje i upravljanje resursima.

# [Java](../../../../05-AdvancedTopics/mcp-scaling)

```java
// Java MCP server with resource optimization
public class OptimizedMcpServer {
    public static McpServer createOptimizedServer() {
        // Configure thread pool for optimal performance
        int processors = Runtime.getRuntime().availableProcessors();
        int optimalThreads = processors * 2; // Common heuristic for I/O-bound tasks
        
        ExecutorService executorService = new ThreadPoolExecutor(
            processors,       // Core pool size
            optimalThreads,   // Maximum pool size 
            60L,              // Keep-alive time
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(1000), // Request queue size
            new ThreadPoolExecutor.CallerRunsPolicy() // Backpressure strategy
        );
        
        // Configure and build MCP server with resource constraints
        return new McpServer.Builder()
            .setName("High-Performance MCP Server")
            .setVersion("1.0.0")
            .setPort(5000)
            .setExecutor(executorService)
            .setMaxRequestSize(1024 * 1024) // 1MB
            .setMaxConcurrentRequests(100)
            .setRequestTimeoutMs(5000) // 5 seconds
            .build();
    }
}
```

U prethodnom kodu smo:

- Konfigurirali thread pool s optimalnim brojem niti temeljenim na broju dostupnih procesora.
- Postavili ograničenja resursa poput maksimalne veličine zahtjeva, maksimalnog broja istovremenih zahtjeva i timeouta zahtjeva.
- Koristili strategiju backpressure za elegantno upravljanje preopterećenjem.

---

## Distribuirana arhitektura

Distribuirane arhitekture uključuju više MCP čvorova koji zajedno obrađuju zahtjeve, dijele resurse i osiguravaju redundanciju. Ovaj pristup poboljšava skalabilnost i otpornost na greške omogućujući čvorovima međusobnu komunikaciju i koordinaciju kroz distribuirani sustav.

Pogledajmo primjer kako implementirati distribuiranu MCP arhitekturu koristeći Redis za koordinaciju.

# [Python](../../../../05-AdvancedTopics/mcp-scaling)

```python
# Python MCP server in distributed architecture
from mcp_server import AsyncMcpServer
import asyncio
import aioredis
import uuid

class DistributedMcpServer:
    def __init__(self, node_id=None):
        self.node_id = node_id or str(uuid.uuid4())
        self.redis = None
        self.server = None
    
    async def initialize(self):
        # Connect to Redis for coordination
        self.redis = await aioredis.create_redis_pool("redis://redis-master:6379")
        
        # Register this node with the cluster
        await self.redis.sadd("mcp:nodes", self.node_id)
        await self.redis.hset(f"mcp:node:{self.node_id}", "status", "starting")
        
        # Create the MCP server
        self.server = AsyncMcpServer(
            name=f"MCP Node {self.node_id[:8]}",
            version="1.0.0",
            port=5000,
            max_concurrent_requests=50
        )
        
        # Register tools - each node might specialize in certain tools
        self.register_tools()
        
        # Start heartbeat mechanism
        asyncio.create_task(self._heartbeat())
        
        # Start server
        await self.server.start()
        
        # Update node status
        await self.redis.hset(f"mcp:node:{self.node_id}", "status", "running")
        print(f"MCP Node {self.node_id[:8]} running on port 5000")
    
    def register_tools(self):
        # Register common tools across all nodes
        self.server.register_tool(CommonTool1())
        self.server.register_tool(CommonTool2())
        
        # Register specialized tools for this node (could be based on node_id or config)
        if int(self.node_id[-1], 16) % 3 == 0:  # Simple way to distribute specialized tools
            self.server.register_tool(SpecializedTool1())
        elif int(self.node_id[-1], 16) % 3 == 1:
            self.server.register_tool(SpecializedTool2())
        else:
            self.server.register_tool(SpecializedTool3())
    
    async def _heartbeat(self):
        """Periodic heartbeat to indicate node health"""
        while True:
            try:
                await self.redis.hset(
                    f"mcp:node:{self.node_id}", 
                    mapping={
                        "lastHeartbeat": int(time.time()),
                        "load": len(self.server.active_requests),
                        "maxLoad": self.server.max_concurrent_requests
                    }
                )
                await asyncio.sleep(5)  # Heartbeat every 5 seconds
            except Exception as e:
                print(f"Heartbeat error: {e}")
                await asyncio.sleep(1)
    
    async def shutdown(self):
        await self.redis.hset(f"mcp:node:{self.node_id}", "status", "stopping")
        await self.server.stop()
        await self.redis.srem("mcp:nodes", self.node_id)
        await self.redis.delete(f"mcp:node:{self.node_id}")
        self.redis.close()
        await self.redis.wait_closed()
```

U prethodnom kodu smo:

- Kreirali distribuirani MCP server koji se registrira kod Redis instance radi koordinacije.
- Implementirali heartbeat mehanizam za ažuriranje statusa i opterećenja čvora u Redisu.
- Registrirali alate koji se mogu specijalizirati prema ID-u čvora, omogućujući raspodjelu opterećenja između čvorova.
- Osigurali metodu za gašenje koja čisti resurse i deregistrira čvor iz klastera.
- Koristili asinkrono programiranje za učinkovitu obradu zahtjeva i održavanje responzivnosti.
- Iskoristili Redis za koordinaciju i upravljanje stanjem među distribuiranim čvorovima.

---

## Što slijedi

- [5.8 Security](../mcp-security/README.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.