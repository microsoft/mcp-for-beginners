# Ölçeklenebilirlik ve Yüksek Performanslı MCP

Kurumsal dağıtımlarda, MCP uygulamalarının genellikle yüksek hacimli istekleri düşük gecikmeyle karşılaması gerekir.

## Giriş

Bu derste, MCP sunucularını büyük iş yüklerini verimli şekilde karşılayacak şekilde ölçeklendirme stratejilerini inceleyeceğiz. Yatay ve dikey ölçeklendirme, kaynak optimizasyonu ve dağıtık mimariler konularını ele alacağız.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Yük dengeleme ve dağıtık önbellekleme kullanarak yatay ölçeklendirme uygulamak.
- MCP sunucularını dikey ölçeklendirme ve kaynak yönetimi için optimize etmek.
- Yüksek erişilebilirlik ve hata toleransı için dağıtık MCP mimarileri tasarlamak.
- Performans izleme ve optimizasyon için gelişmiş araçlar ve teknikler kullanmak.
- Üretim ortamlarında MCP sunucularını ölçeklendirmek için en iyi uygulamaları uygulamak.

## Ölçeklendirme Stratejileri

MCP sunucularını etkili şekilde ölçeklendirmek için birkaç strateji vardır:

- **Yatay Ölçeklendirme**: Gelen istekleri eşit şekilde dağıtmak için bir yük dengeleyicinin arkasında birden fazla MCP sunucusu örneği dağıtmak.
- **Dikey Ölçeklendirme**: Kaynakları (CPU, bellek) artırarak ve yapılandırmaları ince ayar yaparak tek bir MCP sunucusu örneğini daha fazla isteği karşılayacak şekilde optimize etmek.
- **Kaynak Optimizasyonu**: Kaynak tüketimini azaltmak ve yanıt sürelerini iyileştirmek için verimli algoritmalar, önbellekleme ve asenkron işlem kullanmak.
- **Dağıtık Mimari**: Birden fazla MCP düğümünün birlikte çalıştığı, yükü paylaştığı ve yedeklilik sağladığı dağıtık bir sistem uygulamak.

## Yatay Ölçeklendirme

Yatay ölçeklendirme, birden fazla MCP sunucusu örneği dağıtmayı ve gelen istekleri dağıtmak için bir yük dengeleyici kullanmayı içerir. Bu yöntem, aynı anda daha fazla isteği karşılamanızı sağlar ve hata toleransı sunar.

Yatay ölçeklendirme ve MCP yapılandırmasına dair bir örneğe bakalım.

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

Yukarıdaki kodda:

- Oturum durumu ve araç verilerini depolamak için Redis kullanarak dağıtık önbellek yapılandırdık.
- MCP sunucu yapılandırmasında dağıtık önbelleği etkinleştirdik.
- Birden fazla MCP örneği arasında kullanılabilen yüksek performanslı bir aracı kaydettik.

---

## Dikey Ölçeklendirme ve Kaynak Optimizasyonu

Dikey ölçeklendirme, tek bir MCP sunucusu örneğini daha fazla isteği verimli şekilde karşılayacak şekilde optimize etmeye odaklanır. Bu, yapılandırmaları ince ayar yapmak, verimli algoritmalar kullanmak ve kaynakları etkili yönetmekle sağlanabilir. Örneğin, performansı artırmak için iş parçacığı havuzlarını, istek zaman aşımını ve bellek sınırlarını ayarlayabilirsiniz.

Dikey ölçeklendirme ve kaynak yönetimi için MCP sunucusunu nasıl optimize edeceğimize dair bir örneğe bakalım.

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

Yukarıdaki kodda:

- Mevcut işlemci sayısına göre optimal sayıda iş parçacığı içeren bir iş parçacığı havuzu yapılandırdık.
- Maksimum istek boyutu, eşzamanlı maksimum istek sayısı ve istek zaman aşımı gibi kaynak kısıtlamalarını belirledik.
- Aşırı yük durumlarını zarifçe yönetmek için bir geri basınç stratejisi kullandık.

---

## Dağıtık Mimari

Dağıtık mimariler, birden fazla MCP düğümünün birlikte çalışarak istekleri karşılaması, kaynakları paylaşması ve yedeklilik sağlamasıdır. Bu yaklaşım, düğümlerin dağıtık bir sistem aracılığıyla iletişim kurup koordinasyon sağlamasına olanak tanıyarak ölçeklenebilirliği ve hata toleransını artırır.

Redis kullanarak koordinasyon için dağıtık bir MCP sunucu mimarisi uygulama örneğine bakalım.

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

Yukarıdaki kodda:

- Koordinasyon için kendini bir Redis örneğine kaydeden dağıtık bir MCP sunucusu oluşturduk.
- Düğümün durumunu ve yükünü Redis'te güncellemek için bir heartbeat mekanizması uyguladık.
- Düğümün ID'sine göre özelleştirilebilen araçları kaydettik, böylece yük düğümler arasında dağıtılabilir.
- Kaynakları temizlemek ve düğümü kümeden kayıttan kaldırmak için bir kapatma yöntemi sağladık.
- İstekleri verimli şekilde işlemek ve yanıt verebilirliği korumak için asenkron programlama kullandık.
- Dağıtık düğümler arasında koordinasyon ve durum yönetimi için Redis'ten yararlandık.

---

## Sonraki Adımlar

- [5.8 Güvenlik](../mcp-security/README.md)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.