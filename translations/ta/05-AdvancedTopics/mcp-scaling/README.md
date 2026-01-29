# அளவீட்டு திறன் மற்றும் உயர் செயல்திறன் MCP

நிறுவன பயன்பாடுகளுக்காக, MCP செயல்பாடுகள் குறைந்த தாமதத்துடன் அதிக அளவிலான கோரிக்கைகளை கையாள வேண்டும்.

## அறிமுகம்

இந்த பாடத்தில், MCP சர்வர்களை பெரிய பணிகளை திறமையாக கையாளுவதற்கான அளவீட்டு உத்திகளை ஆராய்வோம். நாங்கள் ஹாரிசொன்டல் மற்றும் வெர்டிகல் அளவீடு, வளங்களை மேம்படுத்தல், மற்றும் பகிர்ந்தமைக்கப்பட்ட கட்டமைப்புகளை கையாளுவோம்.

## கற்றல் நோக்கங்கள்

இந்த பாடத்தின் முடிவில், நீங்கள்:

- லோட் பாலன்சிங் மற்றும் பகிர்ந்தமைக்கப்பட்ட கேஷிங் மூலம் ஹாரிசொன்டல் அளவீட்டை செயல்படுத்த முடியும்.
- MCP சர்வர்களை வெர்டிகல் அளவீடு மற்றும் வள மேலாண்மைக்காக மேம்படுத்த முடியும்.
- MCP சர்வர்களுக்கான உயர் கிடைக்கும் மற்றும் பிழை சகிப்புத்தன்மைக்கான பகிர்ந்தமைக்கப்பட்ட கட்டமைப்புகளை வடிவமைக்க முடியும்.
- செயல்திறன் கண்காணிப்பு மற்றும் மேம்படுத்தலுக்கான மேம்பட்ட கருவிகள் மற்றும் உத்திகளை பயன்படுத்த முடியும்.
- MCP சர்வர்களை உற்பத்தி சூழல்களில் அளவீட்டுக்கான சிறந்த நடைமுறைகளை பயன்படுத்த முடியும்.

## அளவீட்டு உத்திகள்

MCP சர்வர்களை திறமையாக அளவீடு செய்ய பல உத்திகள் உள்ளன:

- **ஹாரிசொன்டல் அளவீடு**: MCP சர்வர்களின் பல இன்ஸ்டன்ஸ்களை லோட் பாலன்சரின் பின்னால் அமைத்து, வரும் கோரிக்கைகளை சமமாக பகிரவும்.
- **வெர்டிகல் அளவீடு**: ஒரு MCP சர்வர் இன்ஸ்டன்ஸை அதிக கோரிக்கைகளை கையாளுவதற்காக வளங்களை (CPU, மெமரி) அதிகரித்து மற்றும் கட்டமைப்புகளை நன்றாக அமைத்து மேம்படுத்தவும்.
- **வள மேம்படுத்தல்**: திறமையான ஆல்காரிதங்கள், கேஷிங், மற்றும் அசிங்க செயலாக்கத்தை பயன்படுத்தி வள நுகர்வை குறைத்து பதிலளிக்கும் நேரத்தை மேம்படுத்தவும்.
- **பகிர்ந்தமைக்கப்பட்ட கட்டமைப்பு**: பல MCP நொடுகள் ஒன்றாக வேலை செய்யும் பகிர்ந்தமைக்கப்பட்ட அமைப்பை செயல்படுத்தவும், சுமையை பகிர்ந்து, மீள்நிரப்பத்தை வழங்கவும்.

## ஹாரிசொன்டல் அளவீடு

ஹாரிசொன்டல் அளவீடு என்பது MCP சர்வர்களின் பல இன்ஸ்டன்ஸ்களை அமைத்து, வரும் கோரிக்கைகளை லோட் பாலன்சர் மூலம் பகிர்வதை குறிக்கிறது. இந்த அணுகுமுறை ஒரே நேரத்தில் அதிக கோரிக்கைகளை கையாள அனுமதிக்கிறது மற்றும் பிழை சகிப்புத்தன்மையை வழங்குகிறது.

இப்போது ஹாரிசொன்டல் அளவீடு மற்றும் MCP அமைப்பை எப்படி கட்டமைப்பது என்பதை ஒரு உதாரணமாக பார்க்கலாம்.

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

மேலே உள்ள குறியீட்டில், நாங்கள்:

- Redis பயன்படுத்தி செஷன் நிலை மற்றும் கருவி தரவுகளை சேமிக்க பகிர்ந்தமைக்கப்பட்ட கேஷை அமைத்துள்ளோம்.
- MCP சர்வர் கட்டமைப்பில் பகிர்ந்தமைக்கப்பட்ட கேஷிங்கை இயக்கியுள்ளோம்.
- பல MCP இன்ஸ்டன்ஸ்களில் பயன்படுத்தக்கூடிய உயர் செயல்திறன் கருவியை பதிவு செய்துள்ளோம்.

---

## வெர்டிகல் அளவீடு மற்றும் வள மேம்படுத்தல்

வெர்டிகல் அளவீடு என்பது ஒரு MCP சர்வர் இன்ஸ்டன்ஸை அதிக கோரிக்கைகளை திறமையாக கையாளுவதற்காக மேம்படுத்துவதை குறிக்கிறது. இது கட்டமைப்புகளை நன்றாக அமைத்தல், திறமையான ஆல்காரிதங்களை பயன்படுத்துதல், மற்றும் வளங்களை திறமையாக நிர்வகித்தல் மூலம் அடைய முடியும். உதாரணமாக, திரட் பூல்களை, கோரிக்கை நேரத்தை, மற்றும் மெமரி வரம்புகளை சரிசெய்து செயல்திறனை மேம்படுத்தலாம்.

இப்போது வெர்டிகல் அளவீடு மற்றும் வள மேலாண்மைக்காக MCP சர்வரை எப்படி மேம்படுத்துவது என்பதை ஒரு உதாரணமாக பார்க்கலாம்.

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

மேலே உள்ள குறியீட்டில், நாங்கள்:

- கிடைக்கும் செயலி எண்ணிக்கையை அடிப்படையாகக் கொண்டு திரட் பூல்களை சரியான எண்ணிக்கையுடன் அமைத்துள்ளோம்.
- அதிகபட்ச கோரிக்கை அளவு, அதிகபட்ச ஒரே நேர கோரிக்கைகள், மற்றும் கோரிக்கை நேரத்தை போன்ற வள கட்டுப்பாடுகளை அமைத்துள்ளோம்.
- அதிக சுமை நிலைகளை நன்றாக கையாள ஒரு பின்சுமை உத்தியை பயன்படுத்தியுள்ளோம்.

---

## பகிர்ந்தமைக்கப்பட்ட கட்டமைப்பு

பகிர்ந்தமைக்கப்பட்ட கட்டமைப்புகள் பல MCP நொடுகள் ஒன்றாக வேலை செய்து கோரிக்கைகளை கையாள, வளங்களை பகிர, மற்றும் மீள்நிரப்பத்தை வழங்க உதவுகின்றன. இந்த அணுகுமுறை அளவீட்டு திறனை மற்றும் பிழை சகிப்புத்தன்மையை மேம்படுத்துகிறது, மேலும் நொடுகள் ஒரு பகிர்ந்தமைக்கப்பட்ட அமைப்பின் மூலம் தொடர்பு கொண்டு ஒருங்கிணைக்க அனுமதிக்கிறது.

Redis பயன்படுத்தி ஒருங்கிணைப்புக்கான பகிர்ந்தமைக்கப்பட்ட MCP சர்வர் கட்டமைப்பை எப்படி செயல்படுத்துவது என்பதை ஒரு உதாரணமாக பார்க்கலாம்.

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

மேலே உள்ள குறியீட்டில், நாங்கள்:

- Redis உடன் ஒருங்கிணைப்புக்கான MCP சர்வரை பதிவு செய்துள்ளோம்.
- Redis இல் நொடி நிலை மற்றும் சுமையை புதுப்பிக்க ஒரு ஹார்ட்பீட் முறைமை செயல்படுத்தியுள்ளோம்.
- நொடி ஐடியை அடிப்படையாகக் கொண்டு சிறப்பு செய்யக்கூடிய கருவிகளை பதிவு செய்துள்ளோம், இது நொடுகளுக்கு இடையே சுமையை பகிர அனுமதிக்கிறது.
- கிளஸ்டரில் இருந்து நொடியை நீக்க மற்றும் வளங்களை சுத்தம் செய்ய ஒரு ஷட்ட்டவுன் முறைமையை வழங்கியுள்ளோம்.
- கோரிக்கைகளை திறமையாக கையாள மற்றும் பதிலளிக்கும் திறனை பராமரிக்க அசிங்க நிரலாக்கத்தை பயன்படுத்தியுள்ளோம்.
- Redis ஐ பகிர்ந்தமைக்கப்பட்ட நொடுகளுக்கு இடையே ஒருங்கிணைப்பு மற்றும் நிலை மேலாண்மைக்காக பயன்படுத்தியுள்ளோம்.

---

## அடுத்தது என்ன

- [5.8 பாதுகாப்பு](../mcp-security/README.md)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.