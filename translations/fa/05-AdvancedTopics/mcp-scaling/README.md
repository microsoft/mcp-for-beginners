# مقیاس‌پذیری و عملکرد بالا در MCP

برای استقرارهای سازمانی، پیاده‌سازی‌های MCP اغلب باید حجم بالایی از درخواست‌ها را با کمترین تأخیر مدیریت کنند.

## مقدمه

در این درس، استراتژی‌هایی برای مقیاس‌پذیری سرورهای MCP به منظور مدیریت بارهای کاری بزرگ به‌صورت بهینه بررسی خواهیم کرد. موضوعاتی مانند مقیاس‌پذیری افقی و عمودی، بهینه‌سازی منابع و معماری‌های توزیع‌شده را پوشش می‌دهیم.

## اهداف یادگیری

در پایان این درس، شما قادر خواهید بود:

- مقیاس‌پذیری افقی را با استفاده از بارگذاری متعادل و کش توزیع‌شده پیاده‌سازی کنید.
- سرورهای MCP را برای مقیاس‌پذیری عمودی و مدیریت منابع بهینه کنید.
- معماری‌های توزیع‌شده MCP را برای دسترسی بالا و تحمل خطا طراحی کنید.
- از ابزارها و تکنیک‌های پیشرفته برای نظارت و بهینه‌سازی عملکرد استفاده کنید.
- بهترین شیوه‌ها برای مقیاس‌پذیری سرورهای MCP در محیط‌های تولید را به‌کار ببرید.

## استراتژی‌های مقیاس‌پذیری

چندین استراتژی برای مقیاس‌پذیری مؤثر سرورهای MCP وجود دارد:

- **مقیاس‌پذیری افقی**: چندین نمونه از سرورهای MCP را پشت یک بارگذار متعادل‌کننده مستقر کنید تا درخواست‌های ورودی به‌طور مساوی توزیع شوند.
- **مقیاس‌پذیری عمودی**: یک نمونه سرور MCP را با افزایش منابع (CPU، حافظه) و تنظیم دقیق پیکربندی‌ها بهینه کنید تا بتواند درخواست‌های بیشتری را مدیریت کند.
- **بهینه‌سازی منابع**: از الگوریتم‌های کارآمد، کش و پردازش ناهمزمان استفاده کنید تا مصرف منابع کاهش یافته و زمان پاسخ بهبود یابد.
- **معماری توزیع‌شده**: سیستمی توزیع‌شده پیاده‌سازی کنید که در آن چندین گره MCP با هم کار کنند، بار را تقسیم کرده و افزونگی فراهم کنند.

## مقیاس‌پذیری افقی

مقیاس‌پذیری افقی شامل استقرار چندین نمونه از سرورهای MCP و استفاده از بارگذار متعادل‌کننده برای توزیع درخواست‌های ورودی است. این روش امکان مدیریت همزمان درخواست‌های بیشتر و فراهم کردن تحمل خطا را می‌دهد.

بیایید نگاهی به نمونه‌ای از نحوه پیکربندی مقیاس‌پذیری افقی و MCP بیندازیم.

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

در کد بالا:

- کش توزیع‌شده با استفاده از Redis برای ذخیره وضعیت نشست و داده‌های ابزار پیکربندی شده است.
- کش توزیع‌شده در پیکربندی سرور MCP فعال شده است.
- ابزاری با عملکرد بالا ثبت شده که می‌تواند در چندین نمونه MCP استفاده شود.

---

## مقیاس‌پذیری عمودی و بهینه‌سازی منابع

مقیاس‌پذیری عمودی بر بهینه‌سازی یک نمونه سرور MCP برای مدیریت مؤثرتر درخواست‌ها تمرکز دارد. این کار با تنظیم دقیق پیکربندی‌ها، استفاده از الگوریتم‌های کارآمد و مدیریت منابع به‌خوبی انجام می‌شود. به‌عنوان مثال، می‌توانید استخرهای نخ، زمان‌تایم‌اوت درخواست‌ها و محدودیت‌های حافظه را تنظیم کنید تا عملکرد بهبود یابد.

بیایید نگاهی به نمونه‌ای از نحوه بهینه‌سازی سرور MCP برای مقیاس‌پذیری عمودی و مدیریت منابع بیندازیم.

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

در کد بالا:

- استخر نخ با تعداد بهینه نخ‌ها بر اساس تعداد پردازنده‌های موجود پیکربندی شده است.
- محدودیت‌های منابع مانند حداکثر اندازه درخواست، حداکثر درخواست‌های همزمان و زمان‌تایم‌اوت درخواست تنظیم شده‌اند.
- استراتژی backpressure برای مدیریت شرایط بار اضافی به‌صورت نرم به‌کار رفته است.

---

## معماری توزیع‌شده

معماری‌های توزیع‌شده شامل چندین گره MCP است که با هم کار می‌کنند تا درخواست‌ها را مدیریت کنند، منابع را به اشتراک بگذارند و افزونگی فراهم کنند. این روش با اجازه دادن به گره‌ها برای ارتباط و هماهنگی از طریق یک سیستم توزیع‌شده، مقیاس‌پذیری و تحمل خطا را افزایش می‌دهد.

بیایید نگاهی به نمونه‌ای از نحوه پیاده‌سازی معماری سرور MCP توزیع‌شده با استفاده از Redis برای هماهنگی بیندازیم.

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

در کد بالا:

- سرور MCP توزیع‌شده‌ای ایجاد شده که خود را برای هماهنگی با یک نمونه Redis ثبت می‌کند.
- مکانیزم heartbeat برای به‌روزرسانی وضعیت و بار گره در Redis پیاده‌سازی شده است.
- ابزارهایی ثبت شده‌اند که می‌توانند بر اساس شناسه گره تخصصی شوند و توزیع بار بین گره‌ها را ممکن سازند.
- متدی برای خاموش کردن فراهم شده تا منابع پاک‌سازی شده و گره از خوشه خارج شود.
- برنامه‌نویسی ناهمزمان برای مدیریت مؤثر درخواست‌ها و حفظ پاسخگویی استفاده شده است.
- از Redis برای هماهنگی و مدیریت وضعیت در بین گره‌های توزیع‌شده بهره گرفته شده است.

---

## مرحله بعد

- [5.8 امنیت](../mcp-security/README.md)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.