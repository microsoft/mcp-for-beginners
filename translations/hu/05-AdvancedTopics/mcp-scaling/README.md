# Skálázhatóság és nagy teljesítményű MCP

Vállalati telepítések esetén az MCP megvalósításoknak gyakran kell nagy mennyiségű kérést minimális késleltetéssel kezelniük.

## Bevezetés

Ebben a leckében megvizsgáljuk az MCP szerverek skálázásának stratégiáit, hogy hatékonyan kezeljék a nagy terhelést. Tárgyaljuk a horizontális és vertikális skálázást, az erőforrás-optimalizálást és az elosztott architektúrákat.

## Tanulási célok

A lecke végére képes leszel:

- Horizontális skálázást megvalósítani terheléselosztás és elosztott gyorsítótárazás segítségével.
- Optimalizálni az MCP szervereket vertikális skálázásra és erőforrás-kezelésre.
- Elosztott MCP architektúrákat tervezni magas rendelkezésre állás és hibabiztosság érdekében.
- Haladó eszközöket és technikákat alkalmazni a teljesítményfigyeléshez és optimalizáláshoz.
- A legjobb gyakorlatokat követni az MCP szerverek skálázásában éles környezetben.

## Skálázási stratégiák

Többféle módszer létezik az MCP szerverek hatékony skálázására:

- **Horizontális skálázás**: Több MCP szerver példány telepítése terheléselosztó mögé, hogy egyenletesen ossza el a bejövő kéréseket.
- **Vertikális skálázás**: Egyetlen MCP szerver példány optimalizálása több kérés kezelésére erőforrások (CPU, memória) növelésével és konfigurációk finomhangolásával.
- **Erőforrás-optimalizálás**: Hatékony algoritmusok, gyorsítótárazás és aszinkron feldolgozás alkalmazása az erőforrás-felhasználás csökkentésére és a válaszidők javítására.
- **Elosztott architektúra**: Olyan elosztott rendszer megvalósítása, ahol több MCP csomópont együtt dolgozik, megosztva a terhelést és biztosítva a redundanciát.

## Horizontális skálázás

A horizontális skálázás több MCP szerver példány telepítését jelenti, és terheléselosztó használatát a bejövő kérések elosztására. Ez a megközelítés lehetővé teszi, hogy egyszerre több kérést kezeljünk, és hibabiztosságot biztosít.

Nézzünk egy példát arra, hogyan konfigurálhatjuk a horizontális skálázást és az MCP-t.

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

A fenti kódban:

- Redis segítségével konfiguráltunk elosztott gyorsítótárat a munkamenet állapotának és az eszközadatok tárolására.
- Engedélyeztük az elosztott gyorsítótárazást az MCP szerver konfigurációjában.
- Regisztráltunk egy nagy teljesítményű eszközt, amely több MCP példány között is használható.

---

## Vertikális skálázás és erőforrás-optimalizálás

A vertikális skálázás egyetlen MCP szerver példány optimalizálására fókuszál, hogy hatékonyabban kezelje a megnövekedett kérésszámot. Ezt konfigurációk finomhangolásával, hatékony algoritmusok alkalmazásával és az erőforrások megfelelő kezelésével érhetjük el. Például beállíthatjuk a szálkészleteket, a kérésidőkorlátokat és a memóriahatárokat a teljesítmény javítása érdekében.

Nézzünk egy példát arra, hogyan optimalizálhatunk egy MCP szervert vertikális skálázásra és erőforrás-kezelésre.

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

A fenti kódban:

- Olyan szálkészletet konfiguráltunk, amely optimális számú szálat használ az elérhető processzorok alapján.
- Beállítottunk erőforrás-korlátozásokat, mint a maximális kérésméret, a párhuzamos kérések maximális száma és a kérésidőkorlát.
- Háttérnyomás-kezelési stratégiát alkalmaztunk a túlterheltségi helyzetek finom kezelésére.

---

## Elosztott architektúra

Az elosztott architektúrák több MCP csomópont együttműködését jelentik a kérések kezelésére, az erőforrások megosztására és a redundancia biztosítására. Ez a megközelítés növeli a skálázhatóságot és a hibabiztosságot azáltal, hogy a csomópontok egy elosztott rendszeren keresztül kommunikálnak és koordinálódnak.

Nézzünk egy példát arra, hogyan valósíthatunk meg elosztott MCP szerver architektúrát Redis használatával a koordinációhoz.

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

A fenti kódban:

- Létrehoztunk egy elosztott MCP szervert, amely regisztrálja magát egy Redis példánynál a koordináció érdekében.
- Megvalósítottunk egy heartbeat mechanizmust, amely frissíti a csomópont állapotát és terhelését Redis-ben.
- Regisztráltunk olyan eszközöket, amelyek a csomópont azonosítója alapján specializálhatók, lehetővé téve a terhelés elosztását a csomópontok között.
- Biztosítottunk egy leállítási metódust az erőforrások felszabadítására és a csomópont klaszterből való leiratkozására.
- Aszinkron programozást alkalmaztunk a kérések hatékony kezelésére és a válaszkészség fenntartására.
- Redis-t használtunk a koordinációhoz és az állapotkezeléshez az elosztott csomópontok között.

---

## Mi következik

- [5.8 Biztonság](../mcp-security/README.md)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.