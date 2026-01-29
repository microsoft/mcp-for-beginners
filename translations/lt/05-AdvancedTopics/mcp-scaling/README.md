# Skalė ir aukštas MCP našumas

Įmonių diegimuose MCP dažnai turi apdoroti didelius užklausų kiekius su minimalia delsos trukme.

## Įvadas

Šioje pamokoje nagrinėsime strategijas, kaip efektyviai išplėsti MCP serverius, kad jie galėtų apdoroti didelius darbo krūvius. Aptarsime horizontalų ir vertikalų mastelio keitimą, resursų optimizavimą ir paskirstytas architektūras.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Įgyvendinti horizontalų mastelio keitimą naudojant apkrovos balansavimą ir paskirstytą talpyklą.
- Optimizuoti MCP serverius vertikaliam mastelio keitimui ir resursų valdymui.
- Kurti paskirstytas MCP architektūras, užtikrinančias aukštą prieinamumą ir gedimų toleranciją.
- Naudoti pažangius įrankius ir technikas našumo stebėjimui bei optimizavimui.
- Taikyti geriausias praktikas MCP serverių mastelio keitimui gamybos aplinkoje.

## Mastelio keitimo strategijos

Yra keletas veiksmingų MCP serverių mastelio keitimo strategijų:

- **Horizontalus mastelio keitimas**: Diegti kelias MCP serverių instancijas už apkrovos balansavimo įrenginio, kad užklausos būtų tolygiai paskirstytos.
- **Vertikalus mastelio keitimas**: Optimizuoti vieną MCP serverio instanciją, kad ji galėtų apdoroti daugiau užklausų, didinant resursus (CPU, atmintį) ir koreguojant konfigūracijas.
- **Resursų optimizavimas**: Naudoti efektyvius algoritmus, talpyklą ir asinchroninį apdorojimą, kad sumažintumėte resursų sunaudojimą ir pagerintumėte atsako laiką.
- **Paskirstyta architektūra**: Įgyvendinti paskirstytą sistemą, kurioje keli MCP mazgai dirba kartu, dalijasi apkrova ir užtikrina atsargumą.

## Horizontalus mastelio keitimas

Horizontalus mastelio keitimas apima kelių MCP serverių instancijų diegimą ir apkrovos balansavimo įrenginio naudojimą užklausoms paskirstyti. Šis metodas leidžia vienu metu apdoroti daugiau užklausų ir užtikrina gedimų toleranciją.

Pažvelkime į horizontaliojo mastelio keitimo ir MCP konfigūravimo pavyzdį.

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

Šiame kode mes:

- Konfigūravome paskirstytą talpyklą, naudodami Redis, kad saugotume sesijos būseną ir įrankių duomenis.
- Įgalinome paskirstytą talpyklą MCP serverio konfigūracijoje.
- Registravome aukštos našumo įrankį, kurį galima naudoti keliose MCP instancijose.

---

## Vertikalus mastelio keitimas ir resursų optimizavimas

Vertikalus mastelio keitimas orientuojasi į vienos MCP serverio instancijos optimizavimą, kad ji galėtų efektyviau apdoroti daugiau užklausų. Tai galima pasiekti koreguojant konfigūracijas, naudojant efektyvius algoritmus ir veiksmingai valdant resursus. Pavyzdžiui, galite koreguoti gijų baseinus, užklausų laiko limitus ir atminties ribas, kad pagerintumėte našumą.

Pažvelkime į MCP serverio optimizavimo vertikaliam mastelio keitimui ir resursų valdymui pavyzdį.

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

Šiame kode mes:

- Konfigūravome gijų baseiną su optimaliu gijų skaičiumi, atsižvelgiant į turimų procesorių skaičių.
- Nustatėme resursų apribojimus, tokius kaip maksimalus užklausos dydis, maksimalus vienu metu vykdomų užklausų skaičius ir užklausos laiko limitas.
- Naudojome atgalinio spaudimo strategiją, kad elegantiškai tvarkytume perkrovos situacijas.

---

## Paskirstyta architektūra

Paskirstytos architektūros apima kelis MCP mazgus, kurie dirba kartu, apdoroja užklausas, dalijasi resursais ir užtikrina atsargumą. Šis metodas pagerina mastelio keitimą ir gedimų toleranciją, leidžiant mazgams bendrauti ir koordinuotis per paskirstytą sistemą.

Pažvelkime į paskirstytos MCP serverio architektūros įgyvendinimo pavyzdį, naudojant Redis koordinavimui.

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

Šiame kode mes:

- Sukūrėme paskirstytą MCP serverį, kuris registruojasi Redis instancijoje koordinavimui.
- Įgyvendinome širdies ritmo mechanizmą, kad atnaujintume mazgo būseną ir apkrovą Redis.
- Registravome įrankius, kurie gali būti specializuoti pagal mazgo ID, leidžiant apkrovą paskirstyti tarp mazgų.
- Pateikėme uždarymo metodą, kad išvalytume resursus ir išregistruotume mazgą iš klasterio.
- Naudojome asinchroninį programavimą, kad efektyviai apdorotume užklausas ir išlaikytume atsaką.
- Naudojome Redis koordinavimui ir būsenos valdymui tarp paskirstytų mazgų.

---

## Kas toliau

- [5.8 Saugumas](../mcp-security/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.