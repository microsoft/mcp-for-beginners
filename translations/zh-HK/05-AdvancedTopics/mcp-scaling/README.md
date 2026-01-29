# 可擴展性與高效能 MCP

對於企業部署而言，MCP 實作通常需要處理大量請求，同時保持最低延遲。

## 介紹

在本課程中，我們將探討擴展 MCP 伺服器以有效處理大量工作負載的策略。我們會涵蓋水平與垂直擴展、資源優化以及分散式架構。

## 學習目標

完成本課程後，您將能夠：

- 使用負載平衡與分散式快取實作水平擴展。
- 優化 MCP 伺服器以支援垂直擴展與資源管理。
- 設計具高可用性與容錯能力的分散式 MCP 架構。
- 利用進階工具與技術進行效能監控與優化。
- 應用最佳實務於生產環境中的 MCP 伺服器擴展。

## 擴展策略

有效擴展 MCP 伺服器有幾種策略：

- **水平擴展**：在負載平衡器後部署多個 MCP 伺服器實例，均勻分配進來的請求。
- **垂直擴展**：透過增加資源（CPU、記憶體）及微調設定，優化單一 MCP 伺服器實例以處理更多請求。
- **資源優化**：使用高效演算法、快取與非同步處理，降低資源消耗並提升回應速度。
- **分散式架構**：實作多個 MCP 節點協同工作，共享負載並提供冗餘備援。

## 水平擴展

水平擴展指部署多個 MCP 伺服器實例，並利用負載平衡器分配進來的請求。此方法能同時處理更多請求，並提供容錯能力。

以下示範如何設定水平擴展與 MCP。

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

在上述程式碼中，我們：

- 使用 Redis 配置分散式快取以儲存會話狀態與工具資料。
- 在 MCP 伺服器設定中啟用分散式快取。
- 註冊一個可跨多個 MCP 實例使用的高效能工具。

---

## 垂直擴展與資源優化

垂直擴展著重於優化單一 MCP 伺服器實例，以更有效率地處理更多請求。這可透過微調設定、使用高效演算法及有效管理資源來達成。例如，您可以調整執行緒池、請求逾時與記憶體限制以提升效能。

以下示範如何優化 MCP 伺服器以支援垂直擴展與資源管理。

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

在上述程式碼中，我們：

- 根據可用處理器數量配置了最佳執行緒池大小。
- 設定資源限制，如最大請求大小、最大同時請求數與請求逾時。
- 使用背壓策略優雅地處理過載情況。

---

## 分散式架構

分散式架構涉及多個 MCP 節點協同處理請求、共享資源並提供冗餘備援。此方法透過節點間的通訊與協調，提升擴展性與容錯能力。

以下示範如何使用 Redis 來實作分散式 MCP 伺服器架構。

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

在上述程式碼中，我們：

- 建立一個分散式 MCP 伺服器，並向 Redis 實例註冊以進行協調。
- 實作心跳機制，定期更新節點狀態與負載至 Redis。
- 註冊可依節點 ID 專門化的工具，實現節點間負載分配。
- 提供關閉方法以清理資源並從叢集取消註冊節點。
- 使用非同步程式設計有效處理請求並維持回應能力。
- 利用 Redis 進行分散節點間的協調與狀態管理。

---

## 接下來的內容

- [5.8 Security](../mcp-security/README.md)

**免責聲明**：  
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。