# Kebolehsuaian dan MCP Berprestasi Tinggi

Untuk pengedaran perusahaan, pelaksanaan MCP sering kali perlu mengendalikan jumlah permintaan yang tinggi dengan kelewatan yang minimum.

## Pengenalan

Dalam pelajaran ini, kita akan meneroka strategi untuk mengembangkan pelayan MCP agar dapat mengendalikan beban kerja yang besar dengan cekap. Kita akan membincangkan penskalaan mendatar dan menegak, pengoptimuman sumber, dan seni bina teragih.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Melaksanakan penskalaan mendatar menggunakan pengimbangan beban dan caching teragih.
- Mengoptimumkan pelayan MCP untuk penskalaan menegak dan pengurusan sumber.
- Mereka bentuk seni bina MCP teragih untuk ketersediaan tinggi dan ketahanan terhadap kegagalan.
- Menggunakan alat dan teknik lanjutan untuk pemantauan prestasi dan pengoptimuman.
- Mengaplikasikan amalan terbaik untuk penskalaan pelayan MCP dalam persekitaran pengeluaran.

## Strategi Kebolehsuaian

Terdapat beberapa strategi untuk mengembangkan pelayan MCP dengan berkesan:

- **Penskalaan Mendatar**: Mengedarkan beberapa instans pelayan MCP di belakang pengimbang beban untuk mengagihkan permintaan masuk secara seimbang.
- **Penskalaan Menegak**: Mengoptimumkan satu instans pelayan MCP untuk mengendalikan lebih banyak permintaan dengan meningkatkan sumber (CPU, memori) dan melaraskan konfigurasi.
- **Pengoptimuman Sumber**: Menggunakan algoritma yang cekap, caching, dan pemprosesan tak segerak untuk mengurangkan penggunaan sumber dan memperbaiki masa tindak balas.
- **Seni Bina Teragih**: Melaksanakan sistem teragih di mana beberapa nod MCP bekerjasama, berkongsi beban dan menyediakan redundansi.

## Penskalaan Mendatar

Penskalaan mendatar melibatkan pengedaran beberapa instans pelayan MCP dan menggunakan pengimbang beban untuk mengagihkan permintaan masuk. Pendekatan ini membolehkan anda mengendalikan lebih banyak permintaan serentak dan menyediakan ketahanan terhadap kegagalan.

Mari kita lihat contoh cara mengkonfigurasi penskalaan mendatar dan MCP.

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

Dalam kod sebelum ini kami telah:

- Mengkonfigurasi cache teragih menggunakan Redis untuk menyimpan keadaan sesi dan data alat.
- Mengaktifkan caching teragih dalam konfigurasi pelayan MCP.
- Mendaftar alat berprestasi tinggi yang boleh digunakan merentasi beberapa instans MCP.

---

## Penskalaan Menegak dan Pengoptimuman Sumber

Penskalaan menegak memberi tumpuan kepada mengoptimumkan satu instans pelayan MCP untuk mengendalikan lebih banyak permintaan dengan cekap. Ini boleh dicapai dengan melaraskan konfigurasi, menggunakan algoritma yang cekap, dan mengurus sumber dengan berkesan. Contohnya, anda boleh melaraskan kolam benang, had masa permintaan, dan had memori untuk meningkatkan prestasi.

Mari kita lihat contoh cara mengoptimumkan pelayan MCP untuk penskalaan menegak dan pengurusan sumber.

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

Dalam kod sebelum ini, kami telah:

- Mengkonfigurasi kolam benang dengan bilangan benang yang optimum berdasarkan bilangan pemproses yang tersedia.
- Menetapkan had sumber seperti saiz maksimum permintaan, bilangan permintaan serentak maksimum, dan had masa permintaan.
- Menggunakan strategi tekanan balik untuk mengendalikan situasi beban berlebihan dengan lancar.

---

## Seni Bina Teragih

Seni bina teragih melibatkan beberapa nod MCP yang bekerjasama untuk mengendalikan permintaan, berkongsi sumber, dan menyediakan redundansi. Pendekatan ini meningkatkan kebolehsuaian dan ketahanan terhadap kegagalan dengan membenarkan nod berkomunikasi dan berkoordinasi melalui sistem teragih.

Mari kita lihat contoh cara melaksanakan seni bina pelayan MCP teragih menggunakan Redis untuk koordinasi.

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

Dalam kod sebelum ini, kami telah:

- Mewujudkan pelayan MCP teragih yang mendaftar dirinya dengan instans Redis untuk koordinasi.
- Melaksanakan mekanisme denyutan jantung untuk mengemas kini status dan beban nod dalam Redis.
- Mendaftar alat yang boleh disesuaikan berdasarkan ID nod, membolehkan pengagihan beban merentasi nod.
- Menyediakan kaedah penutupan untuk membersihkan sumber dan membatalkan pendaftaran nod dari kluster.
- Menggunakan pengaturcaraan tak segerak untuk mengendalikan permintaan dengan cekap dan mengekalkan responsif.
- Memanfaatkan Redis untuk koordinasi dan pengurusan keadaan merentasi nod teragih.

---

## Apa seterusnya

- [5.8 Keselamatan](../mcp-security/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.