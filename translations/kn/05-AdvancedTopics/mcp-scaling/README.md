<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4d8d17fc1f501468cce40c3651aed1",
  "translation_date": "2025-12-11T15:13:56+00:00",
  "source_file": "05-AdvancedTopics/mcp-scaling/README.md",
  "language_code": "kn"
}
-->
# ವಿಸ್ತರಣೆ ಮತ್ತು ಉನ್ನತ ಕಾರ್ಯಕ್ಷಮತೆ MCP

ಉದ್ಯಮ ನಿಯೋಜನೆಗಳಿಗೆ, MCP ಅನುಷ್ಠಾನಗಳು ಸಾಮಾನ್ಯವಾಗಿ ಕಡಿಮೆ ವಿಳಂಬದೊಂದಿಗೆ ಹೆಚ್ಚಿನ ಪ್ರಮಾಣದ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸಬೇಕಾಗುತ್ತದೆ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು MCP ಸರ್ವರ್‌ಗಳನ್ನು ದೊಡ್ಡ ಕೆಲಸದ ಭಾರವನ್ನು ಪರಿಣಾಮಕಾರಿಯಾಗಿ ನಿರ್ವಹಿಸಲು ವಿಸ್ತರಿಸುವ ತಂತ್ರಗಳನ್ನು ಅನ್ವೇಷಿಸುವೆವು. ನಾವು ಅಡ್ಡ ಮತ್ತು ಲಂಬ ವಿಸ್ತರಣೆ, ಸಂಪನ್ಮೂಲ ಆಪ್ಟಿಮೈಜೆಷನ್ ಮತ್ತು ವಿತರಿತ ವಾಸ್ತುಶಿಲ್ಪಗಳನ್ನು ಒಳಗೊಂಡಿರುತ್ತೇವೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪಾಠದ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಸಾಧ್ಯವಾಗುವುದು:

- ಲೋಡ್ ಬ್ಯಾಲೆನ್ಸಿಂಗ್ ಮತ್ತು ವಿತರಿತ ಕ್ಯಾಶಿಂಗ್ ಬಳಸಿ ಅಡ್ಡ ವಿಸ್ತರಣೆಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು.
- ಲಂಬ ವಿಸ್ತರಣೆ ಮತ್ತು ಸಂಪನ್ಮೂಲ ನಿರ್ವಹಣೆಗೆ MCP ಸರ್ವರ್‌ಗಳನ್ನು ಆಪ್ಟಿಮೈಸ್ ಮಾಡುವುದು.
- ಉನ್ನತ ಲಭ್ಯತೆ ಮತ್ತು ದೋಷ ಸಹಿಷ್ಣುತೆಗಾಗಿ ವಿತರಿತ MCP ವಾಸ್ತುಶಿಲ್ಪಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸುವುದು.
- ಕಾರ್ಯಕ್ಷಮತೆ ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ಆಪ್ಟಿಮೈಜೆಷನ್‌ಗಾಗಿ ಉನ್ನತ ಸಾಧನಗಳು ಮತ್ತು ತಂತ್ರಗಳನ್ನು ಬಳಸುವುದು.
- ಉತ್ಪಾದನಾ ಪರಿಸರಗಳಲ್ಲಿ MCP ಸರ್ವರ್‌ಗಳನ್ನು ವಿಸ್ತರಿಸುವ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳನ್ನು ಅನ್ವಯಿಸುವುದು.

## ವಿಸ್ತರಣೆ ತಂತ್ರಗಳು

MCP ಸರ್ವರ್‌ಗಳನ್ನು ಪರಿಣಾಮಕಾರಿಯಾಗಿ ವಿಸ್ತರಿಸಲು ಹಲವಾರು ತಂತ್ರಗಳಿವೆ:

- **ಅಡ್ಡ ವಿಸ್ತರಣೆ**: ಲೋಡ್ ಬ್ಯಾಲೆನ್ಸರ್ ಹಿಂದೆ ಹಲವಾರು MCP ಸರ್ವರ್ ಉದಾಹರಣೆಗಳನ್ನು ನಿಯೋಜಿಸಿ, ಬರುವ ವಿನಂತಿಗಳನ್ನು ಸಮಾನವಾಗಿ ಹಂಚಿಕೊಳ್ಳುವುದು.
- **ಲಂಬ ವಿಸ್ತರಣೆ**: ಸಂಪನ್ಮೂಲಗಳನ್ನು (CPU, ಮೆಮೊರಿ) ಹೆಚ್ಚಿಸುವ ಮೂಲಕ ಮತ್ತು ಸಂರಚನೆಗಳನ್ನು ಸೂಕ್ಷ್ಮಗೊಳಿಸುವ ಮೂಲಕ ಒಂದು MCP ಸರ್ವರ್ ಉದಾಹರಣೆಯನ್ನು ಹೆಚ್ಚು ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಆಪ್ಟಿಮೈಸ್ ಮಾಡುವುದು.
- **ಸಂಪನ್ಮೂಲ ಆಪ್ಟಿಮೈಜೆಷನ್**: ಪರಿಣಾಮಕಾರಿ ಅಲ್ಗಾರಿದಮ್‌ಗಳು, ಕ್ಯಾಶಿಂಗ್ ಮತ್ತು ಅಸಿಂಕ್ರೋನಸ್ ಪ್ರಕ್ರಿಯೆಗಳನ್ನು ಬಳಸಿ ಸಂಪನ್ಮೂಲ ಬಳಕೆಯನ್ನು ಕಡಿಮೆ ಮಾಡಿ ಪ್ರತಿಕ್ರಿಯೆ ಸಮಯಗಳನ್ನು ಸುಧಾರಿಸುವುದು.
- **ವಿತರಿತ ವಾಸ್ತುಶಿಲ್ಪ**: ಹಲವಾರು MCP ನೋಡ್‌ಗಳು ಒಟ್ಟಿಗೆ ಕೆಲಸ ಮಾಡುವ ವಿತರಿತ ವ್ಯವಸ್ಥೆಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ, ಲೋಡ್ ಹಂಚಿಕೊಳ್ಳುವುದು ಮತ್ತು ರೆಂಡಂಡನ್ಸಿ ಒದಗಿಸುವುದು.

## ಅಡ್ಡ ವಿಸ್ತರಣೆ

ಅಡ್ಡ ವಿಸ್ತರಣೆ MCP ಸರ್ವರ್‌ಗಳ ಹಲವಾರು ಉದಾಹರಣೆಗಳನ್ನು ನಿಯೋಜಿಸುವುದನ್ನು ಮತ್ತು ಬರುವ ವಿನಂತಿಗಳನ್ನು ಹಂಚಿಕೊಳ್ಳಲು ಲೋಡ್ ಬ್ಯಾಲೆನ್ಸರ್ ಅನ್ನು ಬಳಸುವುದನ್ನು ಒಳಗೊಂಡಿದೆ. ಈ ವಿಧಾನವು ನೀವು ಹೆಚ್ಚು ವಿನಂತಿಗಳನ್ನು ಒಂದೇ ಸಮಯದಲ್ಲಿ ನಿರ್ವಹಿಸಲು ಮತ್ತು ದೋಷ ಸಹಿಷ್ಣುತೆ ಒದಗಿಸಲು ಅನುಮತಿಸುತ್ತದೆ.

ಅಡ್ಡ ವಿಸ್ತರಣೆ ಮತ್ತು MCP ಅನ್ನು ಹೇಗೆ ಸಂರಚಿಸುವುದರ ಉದಾಹರಣೆಯನ್ನು ನೋಡೋಣ.

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

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸೆಷನ್ ಸ್ಥಿತಿ ಮತ್ತು ಸಾಧನ ಡೇಟಾವನ್ನು ಸಂಗ್ರಹಿಸಲು Redis ಬಳಸಿ ವಿತರಿತ ಕ್ಯಾಶ್ ಅನ್ನು ಸಂರಚಿಸಿದ್ದೇವೆ.
- MCP ಸರ್ವರ್ ಸಂರಚನೆಯಲ್ಲಿ ವಿತರಿತ ಕ್ಯಾಶಿಂಗ್ ಅನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿದ್ದೇವೆ.
- ಹಲವಾರು MCP ಉದಾಹರಣೆಗಳಲ್ಲಿ ಬಳಸಬಹುದಾದ ಉನ್ನತ ಕಾರ್ಯಕ್ಷಮತೆ ಸಾಧನವನ್ನು ನೋಂದಾಯಿಸಿದ್ದೇವೆ.

---

## ಲಂಬ ವಿಸ್ತರಣೆ ಮತ್ತು ಸಂಪನ್ಮೂಲ ಆಪ್ಟಿಮೈಜೆಷನ್

ಲಂಬ ವಿಸ್ತರಣೆ ಒಂದು MCP ಸರ್ವರ್ ಉದಾಹರಣೆಯನ್ನು ಹೆಚ್ಚು ವಿನಂತಿಗಳನ್ನು ಪರಿಣಾಮಕಾರಿಯಾಗಿ ನಿರ್ವಹಿಸಲು ಆಪ್ಟಿಮೈಸ್ ಮಾಡುವುದರ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸುತ್ತದೆ. ಇದನ್ನು ಸಂರಚನೆಗಳನ್ನು ಸೂಕ್ಷ್ಮಗೊಳಿಸುವುದು, ಪರಿಣಾಮಕಾರಿ ಅಲ್ಗಾರಿದಮ್‌ಗಳನ್ನು ಬಳಸುವುದು ಮತ್ತು ಸಂಪನ್ಮೂಲಗಳನ್ನು ಪರಿಣಾಮಕಾರಿಯಾಗಿ ನಿರ್ವಹಿಸುವ ಮೂಲಕ ಸಾಧಿಸಬಹುದು. ಉದಾಹರಣೆಗೆ, ಕಾರ್ಯಪಟುಗಳ ಗುಂಪುಗಳು, ವಿನಂತಿ ಸಮಯ ಮಿತಿ ಮತ್ತು ಮೆಮೊರಿ ಮಿತಿಗಳನ್ನು ಹೊಂದಿಸಿ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಸುಧಾರಿಸಬಹುದು.

ಲಂಬ ವಿಸ್ತರಣೆ ಮತ್ತು ಸಂಪನ್ಮೂಲ ನಿರ್ವಹಣೆಗೆ MCP ಸರ್ವರ್ ಅನ್ನು ಹೇಗೆ ಆಪ್ಟಿಮೈಸ್ ಮಾಡುವುದು ಎಂಬುದರ ಉದಾಹರಣೆಯನ್ನು ನೋಡೋಣ.

# [Java](../../../../05-AdvancedTopics/mcp-scaling)

```java
// ಸಂಪನ್ಮೂಲ ಆಪ್ಟಿಮೈಜೆಶನ್ ಹೊಂದಿರುವ ಜಾವಾ MCP ಸರ್ವರ್
public class OptimizedMcpServer {
    public static McpServer createOptimizedServer() {
        // ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆಗಾಗಿ ಥ್ರೆಡ್ ಪೂಲ್ ಅನ್ನು ಸಂರಚಿಸಿ
        int processors = Runtime.getRuntime().availableProcessors();
        int optimalThreads = processors * 2; // I/O-ಬಂಧಿತ ಕಾರ್ಯಗಳಿಗೆ ಸಾಮಾನ್ಯ ಹ್ಯೂರಿಸ್ಟಿಕ್
        
        ExecutorService executorService = new ThreadPoolExecutor(
            processors,       // ಕೋರ್ ಪೂಲ್ ಗಾತ್ರ
            optimalThreads,   // ಗರಿಷ್ಠ ಪೂಲ್ ಗಾತ್ರ
            60L,              // ಕೀಪ್-ಅಲೈವ್ ಸಮಯ
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(1000), // ವಿನಂತಿ ಕ್ಯೂ ಗಾತ್ರ
            new ThreadPoolExecutor.CallerRunsPolicy() // ಬ್ಯಾಕ್‌ಪ್ರೆಶರ್ ತಂತ್ರ
        );
        
        // ಸಂಪನ್ಮೂಲ ನಿರ್ಬಂಧಗಳೊಂದಿಗೆ MCP ಸರ್ವರ್ ಅನ್ನು ಸಂರಚಿಸಿ ಮತ್ತು ನಿರ್ಮಿಸಿ
        return new McpServer.Builder()
            .setName("High-Performance MCP Server")
            .setVersion("1.0.0")
            .setPort(5000)
            .setExecutor(executorService)
            .setMaxRequestSize(1024 * 1024) // 1MB
            .setMaxConcurrentRequests(100)
            .setRequestTimeoutMs(5000) // 5 ಸೆಕೆಂಡುಗಳು
            .build();
    }
}
```

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಲಭ್ಯವಿರುವ ಪ್ರೊಸೆಸರ್‌ಗಳ ಸಂಖ್ಯೆಯ ಆಧಾರದ ಮೇಲೆ ಸೂಕ್ತ ಸಂಖ್ಯೆಯ ಕಾರ್ಯಪಟುಗಳೊಂದಿಗೆ ಕಾರ್ಯಪಟು ಗುಂಪನ್ನು ಸಂರಚಿಸಿದ್ದೇವೆ.
- ಗರಿಷ್ಠ ವಿನಂತಿ ಗಾತ್ರ, ಗರಿಷ್ಠ ಸಮಕಾಲೀನ ವಿನಂತಿಗಳು ಮತ್ತು ವಿನಂತಿ ಸಮಯ ಮಿತಿಯಂತಹ ಸಂಪನ್ಮೂಲ ನಿರ್ಬಂಧಗಳನ್ನು ಹೊಂದಿಸಿದ್ದೇವೆ.
- ಓವರ್‌ಲೋಡ್ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಸೌಮ್ಯವಾಗಿ ನಿರ್ವಹಿಸಲು ಬ್ಯಾಕ್‌ಪ್ರೆಶರ್ ತಂತ್ರವನ್ನು ಬಳಸಿದ್ದೇವೆ.

---

## ವಿತರಿತ ವಾಸ್ತುಶಿಲ್ಪ

ವಿತರಿತ ವಾಸ್ತುಶಿಲ್ಪಗಳು ಹಲವಾರು MCP ನೋಡ್‌ಗಳು ಒಟ್ಟಿಗೆ ಕೆಲಸ ಮಾಡಿ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು, ಸಂಪನ್ಮೂಲಗಳನ್ನು ಹಂಚಿಕೊಳ್ಳುವುದು ಮತ್ತು ರೆಂಡಂಡನ್ಸಿ ಒದಗಿಸುವುದನ್ನು ಒಳಗೊಂಡಿವೆ. ಈ ವಿಧಾನವು ನೋಡ್‌ಗಳು ವಿತರಿತ ವ್ಯವಸ್ಥೆಯ ಮೂಲಕ ಸಂವಹನ ಮತ್ತು ಸಂಯೋಜನೆ ಮಾಡುವ ಮೂಲಕ ವಿಸ್ತರಣೆ ಮತ್ತು ದೋಷ ಸಹಿಷ್ಣುತೆ ಹೆಚ್ಚಿಸುತ್ತದೆ.

Redis ಅನ್ನು ಸಂಯೋಜನೆಗಾಗಿ ಬಳಸಿಕೊಂಡು ವಿತರಿತ MCP ಸರ್ವರ್ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಹೇಗೆ ಅನುಷ್ಠಾನಗೊಳಿಸುವುದರ ಉದಾಹರಣೆಯನ್ನು ನೋಡೋಣ.

# [Python](../../../../05-AdvancedTopics/mcp-scaling)

```python
# ವಿತರಿತ ವಾಸ್ತುಶಿಲ್ಪದಲ್ಲಿ ಪೈಥಾನ್ MCP ಸರ್ವರ್
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
        # ಸಂಯೋಜನೆಗಾಗಿ ರೆಡಿಸ್‌ಗೆ ಸಂಪರ್ಕಿಸಿ
        self.redis = await aioredis.create_redis_pool("redis://redis-master:6379")
        
        # ಕ್ಲಸ್ಟರ್‌ನೊಂದಿಗೆ ಈ ನೋಡ್ ಅನ್ನು ನೋಂದಾಯಿಸಿ
        await self.redis.sadd("mcp:nodes", self.node_id)
        await self.redis.hset(f"mcp:node:{self.node_id}", "status", "starting")
        
        # MCP ಸರ್ವರ್ ರಚಿಸಿ
        self.server = AsyncMcpServer(
            name=f"MCP Node {self.node_id[:8]}",
            version="1.0.0",
            port=5000,
            max_concurrent_requests=50
        )
        
        # ಸಾಧನಗಳನ್ನು ನೋಂದಾಯಿಸಿ - ಪ್ರತಿ ನೋಡ್ ಕೆಲವು ಸಾಧನಗಳಲ್ಲಿ ಪರಿಣತಿ ಹೊಂದಿರಬಹುದು
        self.register_tools()
        
        # ಹಾರ್ಟ್‌ಬೀಟ್ ಯಂತ್ರಣೆಯನ್ನು ಪ್ರಾರಂಭಿಸಿ
        asyncio.create_task(self._heartbeat())
        
        # ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸಿ
        await self.server.start()
        
        # ನೋಡ್ ಸ್ಥಿತಿಯನ್ನು ನವೀಕರಿಸಿ
        await self.redis.hset(f"mcp:node:{self.node_id}", "status", "running")
        print(f"MCP Node {self.node_id[:8]} running on port 5000")
    
    def register_tools(self):
        # ಎಲ್ಲಾ ನೋಡ್‌ಗಳಲ್ಲಿಯೂ ಸಾಮಾನ್ಯ ಸಾಧನಗಳನ್ನು ನೋಂದಾಯಿಸಿ
        self.server.register_tool(CommonTool1())
        self.server.register_tool(CommonTool2())
        
        # ಈ ನೋಡ್‌ಗೆ ವಿಶೇಷ ಸಾಧನಗಳನ್ನು ನೋಂದಾಯಿಸಿ (ನೋಡ್_ಐಡಿ ಅಥವಾ ಸಂರಚನೆಯ ಆಧಾರದ ಮೇಲೆ ಇರಬಹುದು)
        if int(self.node_id[-1], 16) % 3 == 0:  # ವಿಶೇಷ ಸಾಧನಗಳನ್ನು ವಿತರಿಸುವ ಸರಳ ವಿಧಾನ
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
                await asyncio.sleep(5)  # ಪ್ರತಿ 5 ಸೆಕೆಂಡಿಗೆ ಹಾರ್ಟ್‌ಬೀಟ್
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

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸಂಯೋಜನೆಗಾಗಿ Redis ಉದಾಹರಣೆಯೊಂದಿಗೆ ನೋಂದಾಯಿಸುವ ವಿತರಿತ MCP ಸರ್ವರ್ ಅನ್ನು ರಚಿಸಿದ್ದೇವೆ.
- ನೋಡ್ ಸ್ಥಿತಿ ಮತ್ತು ಲೋಡ್ ಅನ್ನು Redis ನಲ್ಲಿ ನವೀಕರಿಸಲು ಹಾರ್ಟ್‌ಬೀಟ್ ಯಂತ್ರಣೆಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿದ್ದೇವೆ.
- ನೋಡ್ ID ಆಧಾರಿತವಾಗಿ ವಿಶೇಷಗೊಳಿಸಬಹುದಾದ ಸಾಧನಗಳನ್ನು ನೋಂದಾಯಿಸಿದ್ದೇವೆ, ಇದು ನೋಡ್‌ಗಳ ನಡುವೆ ಲೋಡ್ ಹಂಚಿಕೆಯನ್ನು ಅನುಮತಿಸುತ್ತದೆ.
- ಸಂಪನ್ಮೂಲಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಲು ಮತ್ತು ಕ್ಲಸ್ಟರ್‌ನಿಂದ ನೋಡ್ ಅನ್ನು ಡೀರಿಜಿಸ್ಟರ್ ಮಾಡಲು ಶಟ್‌ಡೌನ್ ವಿಧಾನವನ್ನು ಒದಗಿಸಿದ್ದೇವೆ.
- ವಿನಂತಿಗಳನ್ನು ಪರಿಣಾಮಕಾರಿಯಾಗಿ ನಿರ್ವಹಿಸಲು ಮತ್ತು ಪ್ರತಿಕ್ರಿಯಾಶೀಲತೆಯನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಲು ಅಸಿಂಕ್ರೋನಸ್ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಅನ್ನು ಬಳಸಿದ್ದೇವೆ.
- ವಿತರಿತ ನೋಡ್‌ಗಳ ನಡುವೆ ಸಂಯೋಜನೆ ಮತ್ತು ಸ್ಥಿತಿ ನಿರ್ವಹಣೆಗೆ Redis ಅನ್ನು ಬಳಸಿದ್ದೇವೆ.

---


## ಮುಂದೇನು

- [5.8 ಭದ್ರತೆ](../mcp-security/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->