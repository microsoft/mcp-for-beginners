# יכולת התרחבות וביצועים גבוהים ב-MCP

בפריסות ארגוניות, יישומי MCP נדרשים לעיתים לטפל בנפחי בקשות גבוהים עם השהייה מינימלית.

## מבוא

בשיעור זה נחקור אסטרטגיות להרחבת שרתי MCP לטיפול בעומסים גדולים בצורה יעילה. נסקור הרחבה אופקית ואנכית, אופטימיזציית משאבים וארכיטקטורות מבוזרות.

## מטרות הלמידה

בסיום השיעור תוכל/י:

- ליישם הרחבה אופקית באמצעות איזון עומסים ו-cache מבוזר.
- לאופטם שרתי MCP להרחבה אנכית וניהול משאבים.
- לתכנן ארכיטקטורות MCP מבוזרות לזמינות גבוהה ועמידות לתקלות.
- להשתמש בכלים וטכניקות מתקדמות למעקב ואופטימיזציית ביצועים.
- ליישם שיטות עבודה מומלצות להרחבת שרתי MCP בסביבות ייצור.

## אסטרטגיות להרחבה

קיימות מספר אסטרטגיות להרחבת שרתי MCP בצורה יעילה:

- **הרחבה אופקית**: פריסת מופעים מרובים של שרתי MCP מאחורי מאזן עומסים כדי לפזר את הבקשות הנכנסות באופן שווה.
- **הרחבה אנכית**: אופטימיזציה של מופע יחיד של שרת MCP לטיפול בכמות גדולה יותר של בקשות על ידי הגדלת משאבים (CPU, זיכרון) וכיוונון הגדרות.
- **אופטימיזציית משאבים**: שימוש באלגוריתמים יעילים, caching ועיבוד אסינכרוני להפחתת צריכת משאבים ושיפור זמני תגובה.
- **ארכיטקטורה מבוזרת**: יישום מערכת מבוזרת שבה מספר צמתים של MCP עובדים יחד, משתפים עומס ומספקים רדונדנציה.

## הרחבה אופקית

הרחבה אופקית כוללת פריסת מופעים מרובים של שרתי MCP ושימוש במאזן עומסים לפיזור הבקשות הנכנסות. גישה זו מאפשרת טיפול בכמות גדולה יותר של בקשות במקביל ומספקת עמידות לתקלות.

נבחן דוגמה להגדרת הרחבה אופקית ב-MCP.

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

בקוד שלמעלה:

- הגדרנו cache מבוזר באמצעות Redis לאחסון מצב סשן ונתוני כלים.
- אפשרנו caching מבוזר בהגדרות שרת ה-MCP.
- רשמנו כלי ביצועים גבוהים שניתן להשתמש בו במופעים מרובים של MCP.

---

## הרחבה אנכית ואופטימיזציית משאבים

הרחבה אנכית מתמקדת באופטימיזציה של מופע יחיד של שרת MCP לטיפול יעיל בכמות גדולה יותר של בקשות. ניתן להשיג זאת על ידי כיוונון הגדרות, שימוש באלגוריתמים יעילים וניהול משאבים נכון. לדוגמה, ניתן להתאים מאגרי תהליכים, זמני המתנה לבקשות ומגבלות זיכרון לשיפור הביצועים.

נבחן דוגמה לאופטימיזציה של שרת MCP להרחבה אנכית וניהול משאבים.

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

בקוד שלמעלה:

- הגדרנו מאגר תהליכים עם מספר אופטימלי של תהליכים בהתבסס על מספר המעבדים הזמינים.
- קבענו מגבלות משאבים כגון גודל מקסימלי לבקשה, מספר מקסימלי של בקשות במקביל וזמן המתנה לבקשה.
- השתמשנו באסטרטגיית backpressure לטיפול במצבי עומס יתר בצורה חלקה.

---

## ארכיטקטורה מבוזרת

ארכיטקטורות מבוזרות כוללות מספר צמתים של MCP העובדים יחד לטיפול בבקשות, שיתוף משאבים ומתן רדונדנציה. גישה זו משפרת את היכולת להתרחב ואת העמידות לתקלות על ידי תקשורת ותיאום בין הצמתים במערכת מבוזרת.

נבחן דוגמה ליישום ארכיטקטורת שרת MCP מבוזרת באמצעות Redis לתיאום.

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

בקוד שלמעלה:

- יצרנו שרת MCP מבוזר שנרשם ב-Redis לצורך תיאום.
- יישמנו מנגנון heartbeat לעדכון סטטוס ועומס הצומת ב-Redis.
- רשמנו כלים שיכולים להיות מותאמים לפי מזהה הצומת, מה שמאפשר פיזור עומס בין הצמתים.
- סיפקנו שיטת shutdown לניקוי משאבים והסרת רישום הצומת מהאשכול.
- השתמשנו בתכנות אסינכרוני לטיפול יעיל בבקשות ולשמירה על תגובתיות.
- ניצלנו את Redis לתיאום וניהול מצב בין הצמתים המבוזרים.

---

## מה הלאה

- [5.8 Security](../mcp-security/README.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.