# القابلية للتوسع وأداء MCP العالي

في بيئات المؤسسات، غالبًا ما تحتاج تطبيقات MCP إلى التعامل مع حجم كبير من الطلبات مع تقليل زمن الاستجابة إلى أدنى حد.

## المقدمة

في هذا الدرس، سنستعرض استراتيجيات توسيع خوادم MCP للتعامل مع أحمال عمل كبيرة بكفاءة. سنغطي التوسع الأفقي والعمودي، تحسين الموارد، والهياكل الموزعة.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:

- تنفيذ التوسع الأفقي باستخدام موازنة التحميل والتخزين المؤقت الموزع.
- تحسين خوادم MCP للتوسع العمودي وإدارة الموارد.
- تصميم هياكل MCP موزعة لتحقيق توافر عالي وتحمل الأخطاء.
- استخدام أدوات وتقنيات متقدمة لمراقبة الأداء وتحسينه.
- تطبيق أفضل الممارسات لتوسيع خوادم MCP في بيئات الإنتاج.

## استراتيجيات القابلية للتوسع

هناك عدة استراتيجيات لتوسيع خوادم MCP بفعالية:

- **التوسع الأفقي**: نشر عدة نسخ من خوادم MCP خلف موازن تحميل لتوزيع الطلبات الواردة بشكل متساوٍ.
- **التوسع العمودي**: تحسين نسخة واحدة من خادم MCP للتعامل مع المزيد من الطلبات عن طريق زيادة الموارد (المعالج، الذاكرة) وضبط الإعدادات بدقة.
- **تحسين الموارد**: استخدام خوارزميات فعالة، التخزين المؤقت، والمعالجة غير المتزامنة لتقليل استهلاك الموارد وتحسين أوقات الاستجابة.
- **الهياكل الموزعة**: تنفيذ نظام موزع حيث تعمل عدة عقد MCP معًا، تشارك الحمل وتوفر التكرار.

## التوسع الأفقي

التوسع الأفقي يتضمن نشر عدة نسخ من خوادم MCP واستخدام موازن تحميل لتوزيع الطلبات الواردة. تتيح هذه الطريقة التعامل مع المزيد من الطلبات في نفس الوقت وتوفر تحملًا للأخطاء.

لننظر في مثال لكيفية تكوين التوسع الأفقي وMCP.

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

في الكود السابق قمنا بـ:

- تكوين تخزين مؤقت موزع باستخدام Redis لتخزين حالة الجلسة وبيانات الأدوات.
- تفعيل التخزين المؤقت الموزع في إعدادات خادم MCP.
- تسجيل أداة عالية الأداء يمكن استخدامها عبر عدة نسخ من MCP.

---

## التوسع العمودي وتحسين الموارد

يركز التوسع العمودي على تحسين نسخة واحدة من خادم MCP للتعامل مع المزيد من الطلبات بكفاءة. يمكن تحقيق ذلك من خلال ضبط الإعدادات بدقة، استخدام خوارزميات فعالة، وإدارة الموارد بشكل جيد. على سبيل المثال، يمكن تعديل مجموعات الخيوط، مهلات الطلبات، وحدود الذاكرة لتحسين الأداء.

لننظر في مثال لكيفية تحسين خادم MCP للتوسع العمودي وإدارة الموارد.

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

في الكود السابق قمنا بـ:

- تكوين مجموعة خيوط بعدد أمثل من الخيوط بناءً على عدد المعالجات المتاحة.
- تعيين قيود على الموارد مثل الحد الأقصى لحجم الطلب، الحد الأقصى للطلبات المتزامنة، ومدة مهلة الطلب.
- استخدام استراتيجية ضغط عكسي للتعامل مع حالات التحميل الزائد بسلاسة.

---

## الهيكل الموزع

تشمل الهياكل الموزعة عدة عقد MCP تعمل معًا للتعامل مع الطلبات، مشاركة الموارد، وتوفير التكرار. تعزز هذه الطريقة القابلية للتوسع وتحمل الأخطاء من خلال السماح للعقد بالتواصل والتنسيق عبر نظام موزع.

لننظر في مثال لكيفية تنفيذ هيكل خادم MCP موزع باستخدام Redis للتنسيق.

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

في الكود السابق قمنا بـ:

- إنشاء خادم MCP موزع يقوم بتسجيل نفسه في مثيل Redis للتنسيق.
- تنفيذ آلية نبضات القلب لتحديث حالة العقدة وحملها في Redis.
- تسجيل أدوات يمكن تخصيصها بناءً على معرف العقدة، مما يسمح بتوزيع الحمل عبر العقد.
- توفير طريقة إيقاف لتنظيف الموارد وإلغاء تسجيل العقدة من العنقود.
- استخدام البرمجة غير المتزامنة للتعامل مع الطلبات بكفاءة والحفاظ على الاستجابة.
- استخدام Redis للتنسيق وإدارة الحالة عبر العقد الموزعة.

---

## ما التالي

- [5.8 الأمان](../mcp-security/README.md)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.