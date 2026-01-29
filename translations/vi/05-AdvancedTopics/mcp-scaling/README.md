# Khả năng mở rộng và MCP hiệu suất cao

Đối với các triển khai doanh nghiệp, các cài đặt MCP thường cần xử lý khối lượng lớn yêu cầu với độ trễ tối thiểu.

## Giới thiệu

Trong bài học này, chúng ta sẽ khám phá các chiến lược để mở rộng các máy chủ MCP nhằm xử lý khối lượng công việc lớn một cách hiệu quả. Chúng ta sẽ đề cập đến mở rộng theo chiều ngang và chiều dọc, tối ưu hóa tài nguyên, và kiến trúc phân tán.

## Mục tiêu học tập

Kết thúc bài học này, bạn sẽ có thể:

- Triển khai mở rộng theo chiều ngang bằng cách sử dụng cân bằng tải và bộ nhớ đệm phân tán.
- Tối ưu hóa máy chủ MCP cho mở rộng theo chiều dọc và quản lý tài nguyên.
- Thiết kế kiến trúc MCP phân tán để đảm bảo tính sẵn sàng cao và khả năng chịu lỗi.
- Sử dụng các công cụ và kỹ thuật nâng cao để giám sát và tối ưu hiệu suất.
- Áp dụng các thực hành tốt nhất để mở rộng máy chủ MCP trong môi trường sản xuất.

## Các chiến lược mở rộng

Có một số chiến lược để mở rộng máy chủ MCP một cách hiệu quả:

- **Mở rộng theo chiều ngang**: Triển khai nhiều phiên bản máy chủ MCP phía sau bộ cân bằng tải để phân phối đều các yêu cầu đến.
- **Mở rộng theo chiều dọc**: Tối ưu hóa một phiên bản máy chủ MCP để xử lý nhiều yêu cầu hơn bằng cách tăng tài nguyên (CPU, bộ nhớ) và tinh chỉnh cấu hình.
- **Tối ưu hóa tài nguyên**: Sử dụng các thuật toán hiệu quả, bộ nhớ đệm và xử lý bất đồng bộ để giảm tiêu thụ tài nguyên và cải thiện thời gian phản hồi.
- **Kiến trúc phân tán**: Triển khai hệ thống phân tán với nhiều nút MCP làm việc cùng nhau, chia sẻ tải và cung cấp khả năng dự phòng.

## Mở rộng theo chiều ngang

Mở rộng theo chiều ngang bao gồm việc triển khai nhiều phiên bản máy chủ MCP và sử dụng bộ cân bằng tải để phân phối các yêu cầu đến. Cách tiếp cận này cho phép bạn xử lý nhiều yêu cầu đồng thời và cung cấp khả năng chịu lỗi.

Hãy xem ví dụ về cách cấu hình mở rộng theo chiều ngang và MCP.

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

Trong đoạn mã trên, chúng ta đã:

- Cấu hình bộ nhớ đệm phân tán sử dụng Redis để lưu trạng thái phiên và dữ liệu công cụ.
- Kích hoạt bộ nhớ đệm phân tán trong cấu hình máy chủ MCP.
- Đăng ký một công cụ hiệu suất cao có thể sử dụng trên nhiều phiên bản MCP.

---

## Mở rộng theo chiều dọc và tối ưu hóa tài nguyên

Mở rộng theo chiều dọc tập trung vào việc tối ưu hóa một phiên bản máy chủ MCP để xử lý nhiều yêu cầu hiệu quả hơn. Điều này có thể đạt được bằng cách tinh chỉnh cấu hình, sử dụng các thuật toán hiệu quả và quản lý tài nguyên một cách hợp lý. Ví dụ, bạn có thể điều chỉnh pool luồng, thời gian chờ yêu cầu và giới hạn bộ nhớ để cải thiện hiệu suất.

Hãy xem ví dụ về cách tối ưu hóa máy chủ MCP cho mở rộng theo chiều dọc và quản lý tài nguyên.

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

Trong đoạn mã trên, chúng ta đã:

- Cấu hình pool luồng với số lượng luồng tối ưu dựa trên số lượng bộ xử lý có sẵn.
- Đặt các giới hạn tài nguyên như kích thước yêu cầu tối đa, số lượng yêu cầu đồng thời tối đa và thời gian chờ yêu cầu.
- Sử dụng chiến lược backpressure để xử lý tình trạng quá tải một cách nhẹ nhàng.

---

## Kiến trúc phân tán

Kiến trúc phân tán bao gồm nhiều nút MCP làm việc cùng nhau để xử lý yêu cầu, chia sẻ tài nguyên và cung cấp khả năng dự phòng. Cách tiếp cận này nâng cao khả năng mở rộng và chịu lỗi bằng cách cho phép các nút giao tiếp và phối hợp thông qua hệ thống phân tán.

Hãy xem ví dụ về cách triển khai kiến trúc máy chủ MCP phân tán sử dụng Redis để điều phối.

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

Trong đoạn mã trên, chúng ta đã:

- Tạo một máy chủ MCP phân tán đăng ký với một phiên bản Redis để điều phối.
- Triển khai cơ chế heartbeat để cập nhật trạng thái và tải của nút trong Redis.
- Đăng ký các công cụ có thể được chuyên biệt hóa dựa trên ID của nút, cho phép phân phối tải giữa các nút.
- Cung cấp phương thức tắt máy để dọn dẹp tài nguyên và hủy đăng ký nút khỏi cụm.
- Sử dụng lập trình bất đồng bộ để xử lý yêu cầu hiệu quả và duy trì khả năng phản hồi.
- Tận dụng Redis để điều phối và quản lý trạng thái giữa các nút phân tán.

---

## Tiếp theo

- [5.8 Bảo mật](../mcp-security/README.md)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.