# Scalability and High-Performance MCP

एंटरप्राइज डिप्लॉयमेंट्स के लिए, MCP इम्प्लीमेंटेशन को अक्सर उच्च मात्रा में रिक्वेस्ट्स को न्यूनतम विलंबता के साथ संभालना पड़ता है।

## परिचय

इस पाठ में, हम MCP सर्वर्स को बड़े वर्कलोड को कुशलतापूर्वक संभालने के लिए स्केल करने की रणनीतियों का अध्ययन करेंगे। हम हॉरिजॉन्टल और वर्टिकल स्केलिंग, संसाधन अनुकूलन, और वितरित आर्किटेक्चर को कवर करेंगे।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- लोड बैलेंसिंग और वितरित कैशिंग का उपयोग करके हॉरिजॉन्टल स्केलिंग को लागू करना।
- वर्टिकल स्केलिंग और संसाधन प्रबंधन के लिए MCP सर्वर्स का अनुकूलन करना।
- उच्च उपलब्धता और फॉल्ट टॉलरेंस के लिए वितरित MCP आर्किटेक्चर डिजाइन करना।
- प्रदर्शन मॉनिटरिंग और अनुकूलन के लिए उन्नत उपकरणों और तकनीकों का उपयोग करना।
- प्रोडक्शन वातावरण में MCP सर्वर्स को स्केल करने के लिए सर्वोत्तम प्रथाओं को लागू करना।

## स्केलेबिलिटी रणनीतियाँ

MCP सर्वर्स को प्रभावी ढंग से स्केल करने के लिए कई रणनीतियाँ हैं:

- **हॉरिजॉन्टल स्केलिंग**: लोड बैलेंसर के पीछे कई MCP सर्वर इंस्टेंस तैनात करें ताकि आने वाले रिक्वेस्ट्स को समान रूप से वितरित किया जा सके।
- **वर्टिकल स्केलिंग**: एकल MCP सर्वर इंस्टेंस को अधिक रिक्वेस्ट्स संभालने के लिए संसाधनों (CPU, मेमोरी) को बढ़ाकर और कॉन्फ़िगरेशन को फाइन-ट्यून करके अनुकूलित करें।
- **संसाधन अनुकूलन**: कुशल एल्गोरिदम, कैशिंग, और असिंक्रोनस प्रोसेसिंग का उपयोग करके संसाधन खपत को कम करें और प्रतिक्रिया समय में सुधार करें।
- **वितरित आर्किटेक्चर**: एक वितरित सिस्टम लागू करें जहां कई MCP नोड्स मिलकर काम करते हैं, लोड साझा करते हैं और रेडंडेंसी प्रदान करते हैं।

## हॉरिजॉन्टल स्केलिंग

हॉरिजॉन्टल स्केलिंग में कई MCP सर्वर इंस्टेंस तैनात करना और लोड बैलेंसर का उपयोग करके आने वाले रिक्वेस्ट्स को वितरित करना शामिल है। यह तरीका आपको एक साथ अधिक रिक्वेस्ट्स को संभालने और फॉल्ट टॉलरेंस प्रदान करने की अनुमति देता है।

आइए देखें कि हॉरिजॉन्टल स्केलिंग और MCP को कैसे कॉन्फ़िगर किया जाए।

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

पिछले कोड में हमने:

- Redis का उपयोग करके एक वितरित कैश कॉन्फ़िगर किया है ताकि सेशन स्टेट और टूल डेटा स्टोर किया जा सके।
- MCP सर्वर कॉन्फ़िगरेशन में वितरित कैशिंग सक्षम की है।
- एक उच्च-प्रदर्शन टूल पंजीकृत किया है जिसे कई MCP इंस्टेंस में उपयोग किया जा सकता है।

---

## वर्टिकल स्केलिंग और संसाधन अनुकूलन

वर्टिकल स्केलिंग एकल MCP सर्वर इंस्टेंस को अधिक रिक्वेस्ट्स कुशलतापूर्वक संभालने के लिए अनुकूलित करने पर केंद्रित है। इसे कॉन्फ़िगरेशन को फाइन-ट्यून करके, कुशल एल्गोरिदम का उपयोग करके, और संसाधनों का प्रभावी प्रबंधन करके प्राप्त किया जा सकता है। उदाहरण के लिए, आप थ्रेड पूल, रिक्वेस्ट टाइमआउट, और मेमोरी लिमिट्स को समायोजित करके प्रदर्शन सुधार सकते हैं।

आइए देखें कि MCP सर्वर को वर्टिकल स्केलिंग और संसाधन प्रबंधन के लिए कैसे अनुकूलित किया जाए।

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

पिछले कोड में हमने:

- उपलब्ध प्रोसेसर की संख्या के आधार पर थ्रेड पूल को अनुकूलित किया है।
- अधिकतम रिक्वेस्ट साइज, अधिकतम समवर्ती रिक्वेस्ट्स, और रिक्वेस्ट टाइमआउट जैसे संसाधन प्रतिबंध सेट किए हैं।
- ओवरलोड की स्थिति को सहजता से संभालने के लिए बैकप्रेशर रणनीति का उपयोग किया है।

---

## वितरित आर्किटेक्चर

वितरित आर्किटेक्चर में कई MCP नोड्स मिलकर रिक्वेस्ट्स को संभालते हैं, संसाधनों को साझा करते हैं, और रेडंडेंसी प्रदान करते हैं। यह तरीका स्केलेबिलिटी और फॉल्ट टॉलरेंस को बढ़ाता है क्योंकि नोड्स एक वितरित सिस्टम के माध्यम से संवाद और समन्वय करते हैं।

आइए देखें कि Redis का उपयोग करके वितरित MCP सर्वर आर्किटेक्चर को कैसे लागू किया जाए।

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

पिछले कोड में हमने:

- एक वितरित MCP सर्वर बनाया है जो समन्वय के लिए Redis इंस्टेंस के साथ खुद को पंजीकृत करता है।
- नोड की स्थिति और लोड को Redis में अपडेट करने के लिए हार्टबीट मैकेनिज्म लागू किया है।
- ऐसे टूल पंजीकृत किए हैं जो नोड के ID के आधार पर विशेषीकृत हो सकते हैं, जिससे नोड्स के बीच लोड वितरण संभव होता है।
- क्लस्टर से नोड को डीरजिस्टर करने और संसाधनों की सफाई के लिए शटडाउन मेथड प्रदान किया है।
- रिक्वेस्ट्स को कुशलतापूर्वक संभालने और प्रतिक्रिया बनाए रखने के लिए असिंक्रोनस प्रोग्रामिंग का उपयोग किया है।
- वितरित नोड्स के बीच समन्वय और स्टेट प्रबंधन के लिए Redis का उपयोग किया है।

---

## आगे क्या है

- [5.8 Security](../mcp-security/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।