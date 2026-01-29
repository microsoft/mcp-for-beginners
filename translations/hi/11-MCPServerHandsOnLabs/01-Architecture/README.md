# कोर आर्किटेक्चर अवधारणाएँ

## 🎯 यह लैब क्या कवर करता है

यह लैब MCP सर्वर आर्किटेक्चर पैटर्न, डेटाबेस डिज़ाइन सिद्धांतों, और तकनीकी कार्यान्वयन रणनीतियों का गहन अन्वेषण प्रदान करता है, जो मजबूत, स्केलेबल और डेटाबेस-इंटीग्रेटेड AI अनुप्रयोगों को शक्ति प्रदान करते हैं।

## अवलोकन

डेटाबेस इंटीग्रेशन के साथ एक प्रोडक्शन-रेडी MCP सर्वर बनाना सावधानीपूर्वक आर्किटेक्चरल निर्णयों की मांग करता है। यह लैब हमारे ज़ावा रिटेल एनालिटिक्स समाधान को मजबूत, सुरक्षित और स्केलेबल बनाने वाले प्रमुख घटकों, डिज़ाइन पैटर्न और तकनीकी विचारों को तोड़कर समझाता है।

आप समझेंगे कि प्रत्येक लेयर कैसे इंटरैक्ट करती है, क्यों विशिष्ट तकनीकों को चुना गया, और इन पैटर्न्स को अपने MCP कार्यान्वयन में कैसे लागू करें।

## सीखने के उद्देश्य

इस लैब के अंत तक, आप सक्षम होंगे:

- **विश्लेषण करें**: डेटाबेस इंटीग्रेशन के साथ MCP सर्वर की लेयर्ड आर्किटेक्चर का  
- **समझें**: प्रत्येक आर्किटेक्चरल घटक की भूमिका और जिम्मेदारियाँ  
- **डिज़ाइन करें**: मल्टी-टेनेंट MCP अनुप्रयोगों का समर्थन करने वाली डेटाबेस स्कीमाएँ  
- **कार्यान्वित करें**: कनेक्शन पूलिंग और संसाधन प्रबंधन रणनीतियाँ  
- **लागू करें**: प्रोडक्शन सिस्टम्स के लिए एरर हैंडलिंग और लॉगिंग पैटर्न  
- **मूल्यांकन करें**: विभिन्न आर्किटेक्चरल दृष्टिकोणों के बीच ट्रेड-ऑफ  

## 🏗️ MCP सर्वर आर्किटेक्चर लेयर्स

हमारा MCP सर्वर **लेयर्ड आर्किटेक्चर** को लागू करता है, जो चिंताओं को अलग करता है और रखरखाव को बढ़ावा देता है:

### लेयर 1: प्रोटोकॉल लेयर (FastMCP)
**जिम्मेदारी**: MCP प्रोटोकॉल संचार और संदेश रूटिंग को संभालना

```python
# FastMCP server setup
from fastmcp import FastMCP

mcp = FastMCP("Zava Retail Analytics")

# Tool registration with type safety
@mcp.tool()
async def execute_sales_query(
    ctx: Context,
    postgresql_query: Annotated[str, Field(description="Well-formed PostgreSQL query")]
) -> str:
    """Execute PostgreSQL queries with Row Level Security."""
    return await query_executor.execute(postgresql_query, ctx)
```

**मुख्य विशेषताएँ**:
- **प्रोटोकॉल अनुपालन**: MCP विनिर्देश का पूर्ण समर्थन  
- **टाइप सेफ्टी**: अनुरोध/प्रतिक्रिया सत्यापन के लिए Pydantic मॉडल  
- **ऐसिंक समर्थन**: उच्च समवर्तीता के लिए नॉन-ब्लॉकिंग I/O  
- **एरर हैंडलिंग**: मानकीकृत त्रुटि प्रतिक्रियाएँ  

### लेयर 2: बिजनेस लॉजिक लेयर
**जिम्मेदारी**: बिजनेस नियमों को लागू करना और प्रोटोकॉल और डेटा लेयर्स के बीच समन्वय करना

```python
class SalesAnalyticsService:
    """Business logic for retail analytics operations."""
    
    async def get_store_performance(
        self, 
        store_id: str, 
        time_period: str
    ) -> Dict[str, Any]:
        """Calculate store performance metrics."""
        
        # Validate business rules
        if not self._validate_store_access(store_id):
            raise UnauthorizedError("Access denied for store")
        
        # Coordinate data retrieval
        sales_data = await self.db_provider.get_sales_data(store_id, time_period)
        metrics = self._calculate_metrics(sales_data)
        
        return {
            "store_id": store_id,
            "period": time_period,
            "metrics": metrics,
            "insights": self._generate_insights(metrics)
        }
```

**मुख्य विशेषताएँ**:
- **बिजनेस नियम प्रवर्तन**: स्टोर एक्सेस सत्यापन और डेटा अखंडता  
- **सेवा समन्वय**: डेटाबेस और AI सेवाओं के बीच ऑर्केस्ट्रेशन  
- **डेटा ट्रांसफॉर्मेशन**: कच्चे डेटा को व्यावसायिक अंतर्दृष्टि में बदलना  
- **कैशिंग रणनीति**: बार-बार पूछे जाने वाले प्रश्नों के लिए प्रदर्शन अनुकूलन  

### लेयर 3: डेटा एक्सेस लेयर
**जिम्मेदारी**: डेटाबेस कनेक्शन, क्वेरी निष्पादन, और डेटा मैपिंग का प्रबंधन

```python
class PostgreSQLProvider:
    """Data access layer for PostgreSQL operations."""
    
    def __init__(self, connection_config: Dict[str, Any]):
        self.connection_pool: Optional[Pool] = None
        self.config = connection_config
    
    async def execute_query(
        self, 
        query: str, 
        rls_user_id: str
    ) -> List[Dict[str, Any]]:
        """Execute query with RLS context."""
        
        async with self.connection_pool.acquire() as conn:
            # Set RLS context
            await conn.execute(
                "SELECT set_config('app.current_rls_user_id', $1, false)",
                rls_user_id
            )
            
            # Execute query with timeout
            try:
                rows = await asyncio.wait_for(
                    conn.fetch(query),
                    timeout=30.0
                )
                return [dict(row) for row in rows]
            except asyncio.TimeoutError:
                raise QueryTimeoutError("Query execution exceeded timeout")
```

**मुख्य विशेषताएँ**:
- **कनेक्शन पूलिंग**: कुशल संसाधन प्रबंधन  
- **लेन-देन प्रबंधन**: ACID अनुपालन और रोलबैक हैंडलिंग  
- **क्वेरी अनुकूलन**: प्रदर्शन निगरानी और अनुकूलन  
- **RLS इंटीग्रेशन**: रो-लेवल सुरक्षा संदर्भ प्रबंधन  

### लेयर 4: इंफ्रास्ट्रक्चर लेयर
**जिम्मेदारी**: लॉगिंग, मॉनिटरिंग, और कॉन्फ़िगरेशन जैसी क्रॉस-कटिंग चिंताओं को संभालना

```python
class InfrastructureManager:
    """Infrastructure concerns management."""
    
    def __init__(self):
        self.logger = self._setup_logging()
        self.metrics = self._setup_metrics()
        self.config = self._load_configuration()
    
    def _setup_logging(self) -> Logger:
        """Configure structured logging."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler('mcp_server.log')
            ]
        )
        return logging.getLogger(__name__)
    
    async def track_query_execution(
        self, 
        query_type: str, 
        duration: float, 
        success: bool
    ):
        """Track query performance metrics."""
        self.metrics.counter('query_total').labels(
            type=query_type,
            status='success' if success else 'error'
        ).inc()
        
        self.metrics.histogram('query_duration').labels(
            type=query_type
        ).observe(duration)
```

## 🗄️ डेटाबेस डिज़ाइन पैटर्न

हमारी PostgreSQL स्कीमा मल्टी-टेनेंट MCP अनुप्रयोगों के लिए कई प्रमुख पैटर्न लागू करती है:

### 1. मल्टी-टेनेंट स्कीमा डिज़ाइन

```sql
-- Core retail entities with store-based partitioning
CREATE TABLE retail.stores (
    store_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    location VARCHAR(200) NOT NULL,
    manager_id UUID NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE retail.customers (
    customer_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    store_id UUID REFERENCES retail.stores(store_id),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE retail.orders (
    order_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID REFERENCES retail.customers(customer_id),
    store_id UUID REFERENCES retail.stores(store_id),
    order_date TIMESTAMP DEFAULT NOW(),
    total_amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending'
);
```

**डिज़ाइन सिद्धांत**:
- **फॉरेन की संगति**: तालिकाओं के बीच डेटा अखंडता सुनिश्चित करना  
- **स्टोर ID प्रचार**: प्रत्येक लेन-देन तालिका में store_id शामिल करना  
- **UUID प्राथमिक कुंजियाँ**: वितरित प्रणालियों के लिए वैश्विक रूप से अद्वितीय पहचानकर्ता  
- **टाइमस्टैम्प ट्रैकिंग**: सभी डेटा परिवर्तनों के लिए ऑडिट ट्रेल  

### 2. रो लेवल सुरक्षा कार्यान्वयन

```sql
-- Enable RLS on multi-tenant tables
ALTER TABLE retail.customers ENABLE ROW LEVEL SECURITY;
ALTER TABLE retail.orders ENABLE ROW LEVEL SECURITY;
ALTER TABLE retail.order_items ENABLE ROW LEVEL SECURITY;

-- Store manager can only see their store's data
CREATE POLICY store_manager_customers ON retail.customers
    FOR ALL TO store_managers
    USING (store_id = get_current_user_store());

CREATE POLICY store_manager_orders ON retail.orders
    FOR ALL TO store_managers
    USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_orders ON retail.orders
    FOR ALL TO regional_managers
    USING (store_id = ANY(get_user_store_list()));

-- Support function for RLS context
CREATE OR REPLACE FUNCTION get_current_user_store()
RETURNS UUID AS $$
BEGIN
    RETURN current_setting('app.current_rls_user_id')::UUID;
EXCEPTION WHEN OTHERS THEN
    RETURN '00000000-0000-0000-0000-000000000000'::UUID;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
```

**RLS लाभ**:
- **स्वचालित फ़िल्टरिंग**: डेटाबेस डेटा अलगाव को लागू करता है  
- **एप्लिकेशन सादगी**: जटिल WHERE क्लॉज़ की आवश्यकता नहीं  
- **डिफ़ॉल्ट रूप से सुरक्षा**: गलत डेटा तक आकस्मिक पहुंच असंभव  
- **ऑडिट अनुपालन**: स्पष्ट डेटा एक्सेस सीमाएँ  

### 3. वेक्टर सर्च स्कीमा

```sql
-- Product embeddings for semantic search
CREATE TABLE retail.product_description_embeddings (
    product_id UUID PRIMARY KEY REFERENCES retail.products(product_id),
    description_embedding vector(1536),
    last_updated TIMESTAMP DEFAULT NOW()
);

-- Optimize vector similarity search
CREATE INDEX idx_product_embeddings_vector 
ON retail.product_description_embeddings 
USING ivfflat (description_embedding vector_cosine_ops);

-- Semantic search function
CREATE OR REPLACE FUNCTION search_products_by_description(
    query_embedding vector(1536),
    similarity_threshold FLOAT DEFAULT 0.7,
    max_results INTEGER DEFAULT 20
)
RETURNS TABLE(
    product_id UUID,
    name VARCHAR,
    description TEXT,
    similarity_score FLOAT
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        p.product_id,
        p.name,
        p.description,
        (1 - (pde.description_embedding <=> query_embedding)) AS similarity_score
    FROM retail.products p
    JOIN retail.product_description_embeddings pde ON p.product_id = pde.product_id
    WHERE (pde.description_embedding <=> query_embedding) <= (1 - similarity_threshold)
    ORDER BY similarity_score DESC
    LIMIT max_results;
END;
$$ LANGUAGE plpgsql;
```

## 🔌 कनेक्शन प्रबंधन पैटर्न

MCP सर्वर प्रदर्शन के लिए कुशल डेटाबेस कनेक्शन प्रबंधन महत्वपूर्ण है:

### कनेक्शन पूल कॉन्फ़िगरेशन

```python
class ConnectionPoolManager:
    """Manages PostgreSQL connection pools."""
    
    async def create_pool(self) -> Pool:
        """Create optimized connection pool."""
        return await asyncpg.create_pool(
            host=self.config.db_host,
            port=self.config.db_port,
            database=self.config.db_name,
            user=self.config.db_user,
            password=self.config.db_password,
            
            # Pool configuration
            min_size=2,          # Minimum connections
            max_size=10,         # Maximum connections
            max_inactive_connection_lifetime=300,  # 5 minutes
            
            # Query configuration
            command_timeout=30,   # Query timeout
            server_settings={
                "application_name": "zava-mcp-server",
                "jit": "off",          # Disable JIT for stability
                "work_mem": "4MB",     # Limit work memory
                "statement_timeout": "30s"
            }
        )
    
    async def execute_with_retry(
        self, 
        query: str, 
        params: Tuple = None,
        max_retries: int = 3
    ) -> List[Dict[str, Any]]:
        """Execute query with automatic retry logic."""
        
        for attempt in range(max_retries):
            try:
                async with self.pool.acquire() as conn:
                    if params:
                        rows = await conn.fetch(query, *params)
                    else:
                        rows = await conn.fetch(query)
                    return [dict(row) for row in rows]
                    
            except (ConnectionError, InterfaceError) as e:
                if attempt == max_retries - 1:
                    raise
                
                # Exponential backoff
                await asyncio.sleep(2 ** attempt)
                logger.warning(f"Database connection failed, retrying ({attempt + 1}/{max_retries})")
```

### संसाधन जीवनचक्र प्रबंधन

```python
class MCPServerManager:
    """Manages MCP server lifecycle and resources."""
    
    async def startup(self):
        """Initialize server resources."""
        # Create database connection pool
        self.db_pool = await self.pool_manager.create_pool()
        
        # Initialize AI services
        self.ai_client = await self.create_ai_client()
        
        # Setup monitoring
        self.metrics_collector = MetricsCollector()
        
        logger.info("MCP server startup complete")
    
    async def shutdown(self):
        """Cleanup server resources."""
        try:
            # Close database connections
            if self.db_pool:
                await self.db_pool.close()
            
            # Cleanup AI client
            if self.ai_client:
                await self.ai_client.close()
            
            # Flush metrics
            await self.metrics_collector.flush()
            
            logger.info("MCP server shutdown complete")
            
        except Exception as e:
            logger.error(f"Error during shutdown: {e}")
    
    async def health_check(self) -> Dict[str, str]:
        """Verify server health status."""
        status = {}
        
        # Check database connection
        try:
            async with self.db_pool.acquire() as conn:
                await conn.fetchval("SELECT 1")
            status["database"] = "healthy"
        except Exception as e:
            status["database"] = f"unhealthy: {e}"
        
        # Check AI service
        try:
            await self.ai_client.health_check()
            status["ai_service"] = "healthy"
        except Exception as e:
            status["ai_service"] = f"unhealthy: {e}"
        
        return status
```

## 🛡️ एरर हैंडलिंग और लचीलापन पैटर्न

मजबूत एरर हैंडलिंग MCP सर्वर के विश्वसनीय संचालन को सुनिश्चित करती है:

### पदानुक्रमित त्रुटि प्रकार

```python
class MCPError(Exception):
    """Base MCP server error."""
    def __init__(self, message: str, error_code: str = "MCP_ERROR"):
        self.message = message
        self.error_code = error_code
        super().__init__(message)

class DatabaseError(MCPError):
    """Database operation errors."""
    def __init__(self, message: str, query: str = None):
        super().__init__(message, "DATABASE_ERROR")
        self.query = query

class AuthorizationError(MCPError):
    """Access control errors."""
    def __init__(self, message: str, user_id: str = None):
        super().__init__(message, "AUTHORIZATION_ERROR")
        self.user_id = user_id

class QueryTimeoutError(DatabaseError):
    """Query execution timeout."""
    def __init__(self, query: str):
        super().__init__(f"Query timeout: {query[:100]}...", query)
        self.error_code = "QUERY_TIMEOUT"

class ValidationError(MCPError):
    """Input validation errors."""
    def __init__(self, field: str, value: Any, constraint: str):
        message = f"Validation failed for {field}: {constraint}"
        super().__init__(message, "VALIDATION_ERROR")
        self.field = field
        self.value = value
```

### एरर हैंडलिंग मिडलवेयर

```python
@contextmanager
async def error_handling_context(operation_name: str, user_id: str = None):
    """Centralized error handling for operations."""
    start_time = time.time()
    
    try:
        yield
        
        # Success metrics
        duration = time.time() - start_time
        metrics.operation_success.labels(operation=operation_name).inc()
        metrics.operation_duration.labels(operation=operation_name).observe(duration)
        
    except ValidationError as e:
        logger.warning(f"Validation error in {operation_name}: {e.message}", extra={
            "operation": operation_name,
            "user_id": user_id,
            "error_type": "validation",
            "field": e.field
        })
        metrics.operation_error.labels(operation=operation_name, type="validation").inc()
        raise
        
    except AuthorizationError as e:
        logger.warning(f"Authorization error in {operation_name}: {e.message}", extra={
            "operation": operation_name,
            "user_id": user_id,
            "error_type": "authorization"
        })
        metrics.operation_error.labels(operation=operation_name, type="authorization").inc()
        raise
        
    except DatabaseError as e:
        logger.error(f"Database error in {operation_name}: {e.message}", extra={
            "operation": operation_name,
            "user_id": user_id,
            "error_type": "database",
            "query": e.query[:100] if e.query else None
        })
        metrics.operation_error.labels(operation=operation_name, type="database").inc()
        raise
        
    except Exception as e:
        logger.error(f"Unexpected error in {operation_name}: {str(e)}", extra={
            "operation": operation_name,
            "user_id": user_id,
            "error_type": "unexpected"
        }, exc_info=True)
        metrics.operation_error.labels(operation=operation_name, type="unexpected").inc()
        raise MCPError(f"Internal server error in {operation_name}")
```

## 📊 प्रदर्शन अनुकूलन रणनीतियाँ

### क्वेरी प्रदर्शन निगरानी

```python
class QueryPerformanceMonitor:
    """Monitor and optimize query performance."""
    
    def __init__(self):
        self.slow_query_threshold = 1.0  # seconds
        self.query_stats = defaultdict(list)
    
    @contextmanager
    async def monitor_query(self, query: str, operation_type: str = "unknown"):
        """Monitor query execution time and performance."""
        start_time = time.time()
        query_hash = hashlib.md5(query.encode()).hexdigest()[:8]
        
        try:
            yield
            
            duration = time.time() - start_time
            
            # Record performance metrics
            self.query_stats[operation_type].append(duration)
            
            # Log slow queries
            if duration > self.slow_query_threshold:
                logger.warning(f"Slow query detected", extra={
                    "query_hash": query_hash,
                    "duration": duration,
                    "operation_type": operation_type,
                    "query": query[:200]
                })
            
            # Update metrics
            metrics.query_duration.labels(type=operation_type).observe(duration)
            
        except Exception as e:
            duration = time.time() - start_time
            logger.error(f"Query failed", extra={
                "query_hash": query_hash,
                "duration": duration,
                "operation_type": operation_type,
                "error": str(e)
            })
            raise
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """Generate performance summary report."""
        summary = {}
        
        for operation_type, durations in self.query_stats.items():
            if durations:
                summary[operation_type] = {
                    "count": len(durations),
                    "avg_duration": sum(durations) / len(durations),
                    "max_duration": max(durations),
                    "min_duration": min(durations),
                    "slow_queries": len([d for d in durations if d > self.slow_query_threshold])
                }
        
        return summary
```

### कैशिंग रणनीति

```python
class QueryCache:
    """Intelligent query result caching."""
    
    def __init__(self, redis_url: str = None):
        self.cache = {}  # In-memory fallback
        self.redis_client = redis.Redis.from_url(redis_url) if redis_url else None
        self.cache_ttl = 300  # 5 minutes default
    
    async def get_cached_result(
        self, 
        cache_key: str, 
        query_func: Callable,
        ttl: int = None
    ) -> Any:
        """Get result from cache or execute query."""
        ttl = ttl or self.cache_ttl
        
        # Try cache first
        cached_result = await self._get_from_cache(cache_key)
        if cached_result is not None:
            metrics.cache_hit.labels(type="query").inc()
            return cached_result
        
        # Execute query
        metrics.cache_miss.labels(type="query").inc()
        result = await query_func()
        
        # Cache result
        await self._set_in_cache(cache_key, result, ttl)
        
        return result
    
    def _generate_cache_key(self, query: str, user_context: str) -> str:
        """Generate consistent cache key."""
        key_data = f"{query}:{user_context}"
        return hashlib.sha256(key_data.encode()).hexdigest()
```

## 🎯 मुख्य निष्कर्ष

इस लैब को पूरा करने के बाद, आपको समझ में आना चाहिए:

✅ **लेयर्ड आर्किटेक्चर**: MCP सर्वर डिज़ाइन में चिंताओं को अलग कैसे करें  
✅ **डेटाबेस पैटर्न**: मल्टी-टेनेंट स्कीमा डिज़ाइन और RLS कार्यान्वयन  
✅ **कनेक्शन प्रबंधन**: कुशल पूलिंग और संसाधन जीवनचक्र  
✅ **एरर हैंडलिंग**: पदानुक्रमित त्रुटि प्रकार और लचीलापन पैटर्न  
✅ **प्रदर्शन अनुकूलन**: निगरानी, कैशिंग, और क्वेरी अनुकूलन  
✅ **प्रोडक्शन रेडीनेस**: इंफ्रास्ट्रक्चर चिंताएँ और परिचालन पैटर्न  

## 🚀 आगे क्या करें

**[लैब 02: सुरक्षा और मल्टी-टेनेंसी](../02-Security/README.md)** के साथ जारी रखें, जिसमें गहराई से शामिल हैं:

- रो लेवल सुरक्षा कार्यान्वयन विवरण  
- प्रमाणीकरण और प्राधिकरण पैटर्न  
- मल्टी-टेनेंट डेटा अलगाव रणनीतियाँ  
- सुरक्षा ऑडिट और अनुपालन विचार  

## 📚 अतिरिक्त संसाधन

### आर्किटेक्चर पैटर्न
- [Python में क्लीन आर्किटेक्चर](https://github.com/cosmic-python/code) - Python अनुप्रयोगों के लिए आर्किटेक्चरल पैटर्न  
- [डेटाबेस डिज़ाइन पैटर्न](https://en.wikipedia.org/wiki/Database_design) - रिलेशनल डेटाबेस डिज़ाइन सिद्धांत  
- [माइक्रोसर्विसेज पैटर्न](https://microservices.io/patterns/) - सेवा आर्किटेक्चर पैटर्न  

### PostgreSQL उन्नत विषय
- [PostgreSQL प्रदर्शन ट्यूनिंग](https://wiki.postgresql.org/wiki/Performance_Optimization) - डेटाबेस अनुकूलन गाइड  
- [कनेक्शन पूलिंग सर्वोत्तम प्रथाएँ](https://www.postgresql.org/docs/current/runtime-config-connection.html) - कनेक्शन प्रबंधन  
- [क्वेरी प्लानिंग और अनुकूलन](https://www.postgresql.org/docs/current/planner-optimizer.html) - क्वेरी प्रदर्शन  

### Python ऐसिंक पैटर्न
- [AsyncIO सर्वोत्तम प्रथाएँ](https://docs.python.org/3/library/asyncio.html) - ऐसिंक प्रोग्रामिंग पैटर्न  
- [FastAPI आर्किटेक्चर](https://fastapi.tiangolo.com/advanced/) - आधुनिक Python वेब आर्किटेक्चर  
- [Pydantic मॉडल](https://pydantic-docs.helpmanual.io/) - डेटा सत्यापन और सीरियलाइज़ेशन  

---

**अगला**: सुरक्षा पैटर्न का अन्वेषण करने के लिए तैयार हैं? [लैब 02: सुरक्षा और मल्टी-टेनेंसी](../02-Security/README.md) के साथ जारी रखें।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।