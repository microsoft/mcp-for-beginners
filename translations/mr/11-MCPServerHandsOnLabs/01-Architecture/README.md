# मुख्य आर्किटेक्चर संकल्पना

## 🎯 हे प्रयोगशाळा काय कव्हर करते

ही प्रयोगशाळा MCP सर्व्हर आर्किटेक्चर पॅटर्न्स, डेटाबेस डिझाइन तत्त्वे आणि मजबूत, स्केलेबल डेटाबेस-एकत्रित AI अनुप्रयोगांना चालना देणाऱ्या तांत्रिक अंमलबजावणी धोरणांचा सखोल अभ्यास प्रदान करते.

## आढावा

डेटाबेस एकत्रीकरणासह उत्पादन-तयार MCP सर्व्हर तयार करणे काळजीपूर्वक आर्किटेक्चरल निर्णयांची आवश्यकता आहे. ही प्रयोगशाळा आमच्या Zava Retail विश्लेषण समाधानाला मजबूत, सुरक्षित आणि स्केलेबल बनवणाऱ्या प्रमुख घटक, डिझाइन पॅटर्न्स आणि तांत्रिक विचारांचे विश्लेषण करते.

तुम्हाला प्रत्येक स्तर कसा संवाद साधतो, विशिष्ट तंत्रज्ञान का निवडले गेले आणि MCP अंमलबजावणीसाठी हे नमुने कसे लागू करायचे हे समजेल.

## शिकण्याची उद्दिष्टे

या प्रयोगशाळेच्या शेवटी, तुम्ही सक्षम असाल:

- **विश्लेषण** MCP सर्व्हरची स्तरित आर्किटेक्चर डेटाबेस एकत्रीकरणासह
- **समजून घेणे** प्रत्येक आर्किटेक्चरल घटकाची भूमिका आणि जबाबदाऱ्या
- **डिझाइन** डेटाबेस स्कीमा जे मल्टी-टेनंट MCP अनुप्रयोगांना समर्थन देतात
- **अंमलबजावणी** कनेक्शन पूलिंग आणि संसाधन व्यवस्थापन धोरणे
- **लागू करणे** उत्पादन प्रणालीसाठी त्रुटी हाताळणी आणि लॉगिंग नमुने
- **मूल्यांकन** विविध आर्किटेक्चरल दृष्टिकोनांमधील व्यापार-offs

## 🏗️ MCP सर्व्हर आर्किटेक्चर स्तर

आमचा MCP सर्व्हर **स्तरित आर्किटेक्चर** अंमलात आणतो जो चिंता वेगळा करतो आणि देखभालक्षमतेला प्रोत्साहन देतो:

### स्तर 1: प्रोटोकॉल स्तर (FastMCP)
**जबाबदारी**: MCP प्रोटोकॉल संवाद आणि संदेश रूटिंग हाताळणे

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

**महत्वाच्या वैशिष्ट्ये**:
- **प्रोटोकॉल अनुपालन**: MCP स्पेसिफिकेशनचे पूर्ण समर्थन
- **टाइप सेफ्टी**: विनंती/प्रतिसाद पडताळणीसाठी Pydantic मॉडेल्स
- **Async समर्थन**: उच्च एकत्रिततेसाठी नॉन-ब्लॉकिंग I/O
- **त्रुटी हाताळणी**: प्रमाणित त्रुटी प्रतिसाद

### स्तर 2: व्यवसाय लॉजिक स्तर
**जबाबदारी**: व्यवसाय नियम अंमलात आणणे आणि प्रोटोकॉल आणि डेटा स्तरांमध्ये समन्वय साधणे

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

**महत्वाच्या वैशिष्ट्ये**:
- **व्यवसाय नियम अंमलबजावणी**: स्टोअर प्रवेश पडताळणी आणि डेटा अखंडता
- **सेवा समन्वय**: डेटाबेस आणि AI सेवांमधील समन्वय
- **डेटा रूपांतरण**: कच्च्या डेटाचे व्यवसाय अंतर्दृष्टीमध्ये रूपांतर
- **कॅशिंग धोरण**: वारंवार क्वेरीसाठी कार्यक्षमता अनुकूलन

### स्तर 3: डेटा प्रवेश स्तर
**जबाबदारी**: डेटाबेस कनेक्शन व्यवस्थापित करणे, क्वेरी अंमलबजावणी आणि डेटा मॅपिंग

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

**महत्वाच्या वैशिष्ट्ये**:
- **कनेक्शन पूलिंग**: कार्यक्षम संसाधन व्यवस्थापन
- **लेनदेन व्यवस्थापन**: ACID अनुपालन आणि रोलबॅक हाताळणी
- **क्वेरी ऑप्टिमायझेशन**: कार्यक्षमता निरीक्षण आणि ऑप्टिमायझेशन
- **RLS एकत्रीकरण**: रो-लेव्हल सुरक्षा संदर्भ व्यवस्थापन

### स्तर 4: पायाभूत सुविधा स्तर
**जबाबदारी**: लॉगिंग, मॉनिटरिंग आणि कॉन्फिगरेशन यासारख्या क्रॉस-कटिंग चिंता हाताळणे

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

## 🗄️ डेटाबेस डिझाइन नमुने

आमचा PostgreSQL स्कीमा मल्टी-टेनंट MCP अनुप्रयोगांसाठी अनेक प्रमुख नमुने अंमलात आणतो:

### 1. मल्टी-टेनंट स्कीमा डिझाइन

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

**डिझाइन तत्त्वे**:
- **फॉरेन की सुसंगतता**: टेबल्समध्ये डेटा अखंडता सुनिश्चित करा
- **स्टोअर आयडी प्रसार**: प्रत्येक व्यवहारात्मक टेबलमध्ये store_id समाविष्ट आहे
- **UUID प्राथमिक की**: वितरित प्रणालींसाठी जागतिकदृष्ट्या अद्वितीय ओळखपत्रे
- **टाइमस्टॅम्प ट्रॅकिंग**: सर्व डेटा बदलांसाठी ऑडिट ट्रेल

### 2. रो लेव्हल सुरक्षा अंमलबजावणी

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

**RLS फायदे**:
- **स्वयंचलित फिल्टरिंग**: डेटाबेस डेटा वेगळेपणा लागू करतो
- **अनुप्रयोग साधेपणा**: जटिल WHERE क्लॉजची गरज नाही
- **डिफॉल्टनुसार सुरक्षा**: चुकीचा डेटा अपघाताने प्रवेश करणे अशक्य
- **ऑडिट अनुपालन**: स्पष्ट डेटा प्रवेश सीमा

### 3. व्हेक्टर शोध स्कीमा

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

## 🔌 कनेक्शन व्यवस्थापन नमुने

MCP सर्व्हर कार्यक्षमतेसाठी कार्यक्षम डेटाबेस कनेक्शन व्यवस्थापन महत्त्वाचे आहे:

### कनेक्शन पूल कॉन्फिगरेशन

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

### संसाधन जीवनचक्र व्यवस्थापन

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

## 🛡️ त्रुटी हाताळणी आणि लवचिकता नमुने

मजबूत त्रुटी हाताळणी MCP सर्व्हरची विश्वासार्ह ऑपरेशन सुनिश्चित करते:

### श्रेणीबद्ध त्रुटी प्रकार

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

### त्रुटी हाताळणी मिडलवेअर

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

## 📊 कार्यक्षमता ऑप्टिमायझेशन धोरणे

### क्वेरी कार्यक्षमता निरीक्षण

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

### कॅशिंग धोरण

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

## 🎯 मुख्य मुद्दे

ही प्रयोगशाळा पूर्ण केल्यानंतर, तुम्हाला समजले पाहिजे:

✅ **स्तरित आर्किटेक्चर**: MCP सर्व्हर डिझाइनमध्ये चिंता वेगळे कसे करायचे  
✅ **डेटाबेस नमुने**: मल्टी-टेनंट स्कीमा डिझाइन आणि RLS अंमलबजावणी  
✅ **कनेक्शन व्यवस्थापन**: कार्यक्षम पूलिंग आणि संसाधन जीवनचक्र  
✅ **त्रुटी हाताळणी**: श्रेणीबद्ध त्रुटी प्रकार आणि लवचिकता नमुने  
✅ **कार्यक्षमता ऑप्टिमायझेशन**: निरीक्षण, कॅशिंग आणि क्वेरी ऑप्टिमायझेशन  
✅ **उत्पादन तयारी**: पायाभूत सुविधा चिंता आणि ऑपरेशनल नमुने  

## 🚀 पुढे काय

**[Lab 02: Security and Multi-Tenancy](../02-Security/README.md)** सह सुरू ठेवा जे सखोलपणे कव्हर करते:

- रो लेव्हल सुरक्षा अंमलबजावणी तपशील
- प्रमाणीकरण आणि अधिकृतता नमुने
- मल्टी-टेनंट डेटा वेगळेपणा धोरणे
- सुरक्षा ऑडिट आणि अनुपालन विचार

## 📚 अतिरिक्त संसाधने

### आर्किटेक्चर नमुने
- [Clean Architecture in Python](https://github.com/cosmic-python/code) - Python अनुप्रयोगांसाठी आर्किटेक्चरल नमुने
- [Database Design Patterns](https://en.wikipedia.org/wiki/Database_design) - रिलेशनल डेटाबेस डिझाइन तत्त्वे
- [Microservices Patterns](https://microservices.io/patterns/) - सेवा आर्किटेक्चर नमुने

### PostgreSQL प्रगत विषय
- [PostgreSQL Performance Tuning](https://wiki.postgresql.org/wiki/Performance_Optimization) - डेटाबेस ऑप्टिमायझेशन मार्गदर्शक
- [Connection Pooling Best Practices](https://www.postgresql.org/docs/current/runtime-config-connection.html) - कनेक्शन व्यवस्थापन
- [Query Planning and Optimization](https://www.postgresql.org/docs/current/planner-optimizer.html) - क्वेरी कार्यक्षमता

### Python Async नमुने
- [AsyncIO Best Practices](https://docs.python.org/3/library/asyncio.html) - Async प्रोग्रामिंग नमुने
- [FastAPI Architecture](https://fastapi.tiangolo.com/advanced/) - आधुनिक Python वेब आर्किटेक्चर
- [Pydantic Models](https://pydantic-docs.helpmanual.io/) - डेटा पडताळणी आणि सिरीयलायझेशन

---

**पुढे**: सुरक्षा नमुने एक्सप्लोर करण्यासाठी तयार? [Lab 02: Security and Multi-Tenancy](../02-Security/README.md) सह सुरू ठेवा

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.