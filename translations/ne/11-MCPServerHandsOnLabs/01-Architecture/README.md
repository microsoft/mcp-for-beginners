# कोर आर्किटेक्चर अवधारणाहरू

## 🎯 यो प्रयोगशालाले के समेट्छ

यो प्रयोगशालाले MCP सर्भर आर्किटेक्चर ढाँचाहरू, डाटाबेस डिजाइन सिद्धान्तहरू, र बलियो, स्केलेबल डाटाबेस-एकीकृत AI अनुप्रयोगहरूलाई शक्ति प्रदान गर्ने प्राविधिक कार्यान्वयन रणनीतिहरूको गहन अन्वेषण प्रदान गर्दछ।

## अवलोकन

डाटाबेस एकीकरणसहित उत्पादन-तयार MCP सर्भर निर्माण गर्न सावधानीपूर्वक आर्किटेक्चरल निर्णयहरू आवश्यक हुन्छ। यो प्रयोगशालाले हाम्रो Zava Retail एनालिटिक्स समाधानलाई बलियो, सुरक्षित, र स्केलेबल बनाउने प्रमुख घटकहरू, डिजाइन ढाँचाहरू, र प्राविधिक विचारहरूलाई टुक्रा-टुक्रा पारेर व्याख्या गर्दछ।

तपाईं प्रत्येक तह कसरी अन्तरक्रिया गर्छ भन्ने बुझ्नुहुनेछ, किन विशिष्ट प्रविधिहरू चयन गरियो, र यी ढाँचाहरूलाई आफ्नै MCP कार्यान्वयनहरूमा कसरी लागू गर्ने।

## सिक्ने उद्देश्यहरू

यो प्रयोगशाला समाप्त गर्दा, तपाईं सक्षम हुनुहुनेछ:

- **विश्लेषण गर्नुहोस्**: डाटाबेस एकीकरणसहितको MCP सर्भरको तहबद्ध आर्किटेक्चर  
- **बुझ्नुहोस्**: प्रत्येक आर्किटेक्चरल घटकको भूमिका र जिम्मेवारी  
- **डिजाइन गर्नुहोस्**: बहु-भाडावाल MCP अनुप्रयोगहरूलाई समर्थन गर्ने डाटाबेस स्कीमाहरू  
- **कार्यान्वयन गर्नुहोस्**: कनेक्शन पूलिङ र स्रोत व्यवस्थापन रणनीतिहरू  
- **लागू गर्नुहोस्**: उत्पादन प्रणालीहरूको लागि त्रुटि ह्यान्डलिङ र लगिङ ढाँचाहरू  
- **मूल्याङ्कन गर्नुहोस्**: विभिन्न आर्किटेक्चरल दृष्टिकोणहरू बीचको व्यापार-सम्झौता  

## 🏗️ MCP सर्भर आर्किटेक्चर तहहरू

हाम्रो MCP सर्भरले **तहबद्ध आर्किटेक्चर** कार्यान्वयन गर्दछ जसले चिन्ताहरू अलग गर्दछ र मर्मतयोग्यता प्रवर्द्धन गर्दछ:

### तह १: प्रोटोकल तह (FastMCP)
**जिम्मेवारी**: MCP प्रोटोकल सञ्चार र सन्देश रुटिङ ह्यान्डल गर्नुहोस्

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

**मुख्य विशेषताहरू**:
- **प्रोटोकल अनुपालन**: पूर्ण MCP विशिष्टता समर्थन  
- **प्रकार सुरक्षा**: अनुरोध/प्रतिक्रिया मान्यताका लागि Pydantic मोडेलहरू  
- **Async समर्थन**: उच्च समवर्तीता लागि गैर-अवरोधक I/O  
- **त्रुटि ह्यान्डलिङ**: मानकीकृत त्रुटि प्रतिक्रियाहरू  

### तह २: व्यवसायिक तर्क तह
**जिम्मेवारी**: व्यवसायिक नियमहरू कार्यान्वयन गर्नुहोस् र प्रोटोकल र डाटा तहहरू बीच समन्वय गर्नुहोस्

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

**मुख्य विशेषताहरू**:
- **व्यवसायिक नियम प्रवर्तन**: स्टोर पहुँच मान्यता र डाटा अखण्डता  
- **सेवा समन्वय**: डाटाबेस र AI सेवाहरू बीचको समन्वय  
- **डाटा रूपान्तरण**: कच्चा डाटालाई व्यवसायिक अन्तर्दृष्टिमा रूपान्तरण गर्नुहोस्  
- **क्यासिङ रणनीति**: बारम्बार क्वेरीहरूको लागि प्रदर्शन अनुकूलन  

### तह ३: डाटा पहुँच तह
**जिम्मेवारी**: डाटाबेस कनेक्शनहरू, क्वेरी कार्यान्वयन, र डाटा म्यापिङ व्यवस्थापन गर्नुहोस्

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

**मुख्य विशेषताहरू**:
- **कनेक्शन पूलिङ**: स्रोत व्यवस्थापनको लागि प्रभावकारी  
- **लेनदेन व्यवस्थापन**: ACID अनुपालन र रोलब्याक ह्यान्डलिङ  
- **क्वेरी अनुकूलन**: प्रदर्शन अनुगमन र अनुकूलन  
- **RLS एकीकरण**: पङ्क्ति-स्तर सुरक्षा सन्दर्भ व्यवस्थापन  

### तह ४: पूर्वाधार तह
**जिम्मेवारी**: लगिङ, अनुगमन, र कन्फिगरेसन जस्ता क्रस-कटिङ चिन्ताहरू ह्यान्डल गर्नुहोस्

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

## 🗄️ डाटाबेस डिजाइन ढाँचाहरू

हाम्रो PostgreSQL स्कीमाले बहु-भाडावाल MCP अनुप्रयोगहरूको लागि केही प्रमुख ढाँचाहरू कार्यान्वयन गर्दछ:

### १. बहु-भाडावाल स्कीमा डिजाइन

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

**डिजाइन सिद्धान्तहरू**:
- **विदेशी कुञ्जी स्थिरता**: तालिकाहरू बीच डाटा अखण्डता सुनिश्चित गर्नुहोस्  
- **स्टोर ID प्रसार**: प्रत्येक लेनदेन तालिकाले store_id समावेश गर्दछ  
- **UUID प्राथमिक कुञ्जीहरू**: वितरित प्रणालीहरूको लागि विश्वव्यापी रूपमा अद्वितीय पहिचानकर्ता  
- **टाइमस्ट्याम्प ट्र्याकिङ**: सबै डाटा परिवर्तनहरूको अडिट ट्रेल  

### २. पङ्क्ति स्तर सुरक्षा कार्यान्वयन

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

**RLS लाभहरू**:
- **स्वचालित फिल्टरिङ**: डाटाबेसले डाटा अलगाव लागू गर्दछ  
- **अनुप्रयोग सरलता**: जटिल WHERE क्लजहरू आवश्यक छैन  
- **डिफल्टद्वारा सुरक्षा**: गलत डाटामा पहुँच गर्न असम्भव  
- **अडिट अनुपालन**: स्पष्ट डाटा पहुँच सीमाहरू  

### ३. भेक्टर खोज स्कीमा

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

## 🔌 कनेक्शन व्यवस्थापन ढाँचाहरू

प्रभावकारी डाटाबेस कनेक्शन व्यवस्थापन MCP सर्भर प्रदर्शनको लागि महत्त्वपूर्ण छ:

### कनेक्शन पूल कन्फिगरेसन

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

### स्रोत जीवनचक्र व्यवस्थापन

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

## 🛡️ त्रुटि ह्यान्डलिङ र लचिलोपन ढाँचाहरू

बलियो त्रुटि ह्यान्डलिङले MCP सर्भरको भरपर्दो सञ्चालन सुनिश्चित गर्दछ:

### पदानुक्रमित त्रुटि प्रकारहरू

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

### त्रुटि ह्यान्डलिङ मिडलवेयर

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

## 📊 प्रदर्शन अनुकूलन रणनीतिहरू

### क्वेरी प्रदर्शन अनुगमन

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

### क्यासिङ रणनीति

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

## 🎯 मुख्य निष्कर्षहरू

यो प्रयोगशाला पूरा गरेपछि, तपाईंले बुझ्नुपर्नेछ:

✅ **तहबद्ध आर्किटेक्चर**: MCP सर्भर डिजाइनमा चिन्ताहरू कसरी अलग गर्ने  
✅ **डाटाबेस ढाँचाहरू**: बहु-भाडावाल स्कीमा डिजाइन र RLS कार्यान्वयन  
✅ **कनेक्शन व्यवस्थापन**: प्रभावकारी पूलिङ र स्रोत जीवनचक्र  
✅ **त्रुटि ह्यान्डलिङ**: पदानुक्रमित त्रुटि प्रकारहरू र लचिलोपन ढाँचाहरू  
✅ **प्रदर्शन अनुकूलन**: अनुगमन, क्यासिङ, र क्वेरी अनुकूलन  
✅ **उत्पादन तयारी**: पूर्वाधार चिन्ताहरू र सञ्चालन ढाँचाहरू  

## 🚀 अब के गर्ने

**[Lab 02: Security and Multi-Tenancy](../02-Security/README.md)** जारी राख्नुहोस् र गहिरो रूपमा अन्वेषण गर्नुहोस्:

- पङ्क्ति स्तर सुरक्षा कार्यान्वयन विवरणहरू  
- प्रमाणीकरण र प्राधिकरण ढाँचाहरू  
- बहु-भाडावाल डाटा अलगाव रणनीतिहरू  
- सुरक्षा अडिट र अनुपालन विचारहरू  

## 📚 थप स्रोतहरू

### आर्किटेक्चर ढाँचाहरू
- [Clean Architecture in Python](https://github.com/cosmic-python/code) - Python अनुप्रयोगहरूको लागि आर्किटेक्चरल ढाँचाहरू  
- [Database Design Patterns](https://en.wikipedia.org/wiki/Database_design) - सम्बन्धपरक डाटाबेस डिजाइन सिद्धान्तहरू  
- [Microservices Patterns](https://microservices.io/patterns/) - सेवा आर्किटेक्चर ढाँचाहरू  

### PostgreSQL उन्नत विषयहरू
- [PostgreSQL Performance Tuning](https://wiki.postgresql.org/wiki/Performance_Optimization) - डाटाबेस अनुकूलन मार्गदर्शन  
- [Connection Pooling Best Practices](https://www.postgresql.org/docs/current/runtime-config-connection.html) - कनेक्शन व्यवस्थापन  
- [Query Planning and Optimization](https://www.postgresql.org/docs/current/planner-optimizer.html) - क्वेरी प्रदर्शन  

### Python Async ढाँचाहरू
- [AsyncIO Best Practices](https://docs.python.org/3/library/asyncio.html) - Async प्रोग्रामिङ ढाँचाहरू  
- [FastAPI Architecture](https://fastapi.tiangolo.com/advanced/) - आधुनिक Python वेब आर्किटेक्चर  
- [Pydantic Models](https://pydantic-docs.helpmanual.io/) - डाटा मान्यता र सिरियलाइजेसन  

---

**अर्को**: सुरक्षा ढाँचाहरू अन्वेषण गर्न तयार हुनुहुन्छ? [Lab 02: Security and Multi-Tenancy](../02-Security/README.md) जारी राख्नुहोस्

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथासम्भव शुद्धता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेज़ यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।