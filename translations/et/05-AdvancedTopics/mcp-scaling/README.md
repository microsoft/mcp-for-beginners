# Mastaapsus ja kõrge jõudlus MCP

Ettevõtte tasemel juurutustes peavad MCP rakendused sageli töötlema suurt hulka päringuid minimaalse viivitusega.

## Sissejuhatus

Selles õppetükis uurime strateegiaid MCP serverite mastaapsuse suurendamiseks, et tõhusalt hallata suuri töökoormusi. Käsitleme horisontaalset ja vertikaalset mastaapsust, ressursside optimeerimist ja hajutatud arhitektuure.

## Õppeeesmärgid

Selle õppetüki lõpuks oskate:

- Rakendada horisontaalset mastaapsust, kasutades koormuse tasakaalustamist ja hajutatud vahemällu salvestamist.
- Optimeerida MCP servereid vertikaalse mastaapsuse ja ressursside haldamise jaoks.
- Kavandada hajutatud MCP arhitektuure, mis tagavad kõrge saadavuse ja tõrketaluvuse.
- Kasutada täiustatud tööriistu ja tehnikaid jõudluse jälgimiseks ja optimeerimiseks.
- Rakendada parimaid tavasid MCP serverite mastaapsuse suurendamiseks tootmiskeskkonnas.

## Mastaapsuse strateegiad

MCP serverite tõhusaks mastaapsuse suurendamiseks on mitmeid strateegiaid:

- **Horisontaalne mastaapsus**: Paigaldage mitu MCP serveri eksemplari koormuse tasakaalustaja taha, et jaotada sissetulevad päringud ühtlaselt.
- **Vertikaalne mastaapsus**: Optimeerige üks MCP serveri eksemplar, et käsitleda rohkem päringuid, suurendades ressursse (CPU, mälu) ja seadistusi peenhäälestades.
- **Ressursside optimeerimine**: Kasutage tõhusaid algoritme, vahemällu salvestamist ja asünkroonset töötlemist, et vähendada ressursikasutust ja parandada vastuseaegu.
- **Hajutatud arhitektuur**: Rakendage hajutatud süsteem, kus mitu MCP sõlme töötavad koos, jagades koormust ja pakkudes varundust.

## Horisontaalne mastaapsus

Horisontaalne mastaapsus hõlmab mitme MCP serveri eksemplari paigaldamist ja koormuse tasakaalustaja kasutamist sissetulevate päringute jaotamiseks. See lähenemine võimaldab käsitleda rohkem päringuid samaaegselt ja tagab tõrketaluvuse.

Vaatame näidet, kuidas konfigureerida horisontaalset mastaapsust MCP jaoks.

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

Eelnevas koodis oleme:

- Konfigureerinud hajutatud vahemälu, kasutades Redis-t, et salvestada sessiooni olek ja tööriistade andmed.
- Lubanud hajutatud vahemällu salvestamise MCP serveri konfiguratsioonis.
- Registreerinud suure jõudlusega tööriista, mida saab kasutada mitme MCP eksemplari vahel.

---

## Vertikaalne mastaapsus ja ressursside optimeerimine

Vertikaalne mastaapsus keskendub ühe MCP serveri eksemplari optimeerimisele, et käsitleda rohkem päringuid tõhusalt. Seda saab saavutada seadistuste peenhäälestamise, tõhusate algoritmide kasutamise ja ressursside tõhusa haldamisega. Näiteks saate kohandada lõimepõlde, päringute ajalimiite ja mälupiiranguid, et parandada jõudlust.

Vaatame näidet, kuidas optimeerida MCP serverit vertikaalse mastaapsuse ja ressursside haldamise jaoks.

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

Eelnevas koodis oleme:

- Konfigureerinud lõimepõllu optimaalse arvu lõimedega, mis põhinevad saadaolevate protsessorite arvul.
- Määranud ressursipiirangud, nagu maksimaalne päringu suurus, maksimaalne samaaegsete päringute arv ja päringu ajalimiit.
- Kasutanud tagasurvestrateegiat, et käsitleda ülekoormuse olukordi sujuvalt.

---

## Hajutatud arhitektuur

Hajutatud arhitektuurid hõlmavad mitut MCP sõlme, mis töötavad koos päringute käsitlemiseks, ressursside jagamiseks ja varunduse pakkumiseks. See lähenemine suurendab mastaapsust ja tõrketaluvust, võimaldades sõlmedel suhelda ja koordineerida hajutatud süsteemi kaudu.

Vaatame näidet, kuidas rakendada hajutatud MCP serveri arhitektuuri, kasutades Redis-t koordineerimiseks.

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

Eelnevas koodis oleme:

- Loonud hajutatud MCP serveri, mis registreerib end Redis eksemplis koordineerimiseks.
- Rakendanud südame löögimehhanismi, et värskendada sõlme olekut ja koormust Redis-s.
- Registreerinud tööriistad, mida saab spetsialiseerida sõlme ID põhjal, võimaldades koormuse jaotamist sõlmede vahel.
- Pakkunud sulgemismeetodi ressursside puhastamiseks ja sõlme klastrist eemaldamiseks.
- Kasutanud asünkroonset programmeerimist, et käsitleda päringuid tõhusalt ja säilitada reageerimisvõime.
- Kasutanud Redis-t koordineerimiseks ja oleku haldamiseks hajutatud sõlmede vahel.

---

## Mis edasi

- [5.8 Turvalisus](../mcp-security/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.