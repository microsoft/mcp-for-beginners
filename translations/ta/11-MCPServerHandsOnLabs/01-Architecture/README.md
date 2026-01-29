# முக்கிய கட்டமைப்பு கருத்துக்கள்

## 🎯 இந்த ஆய்வகத்தில் என்ன கற்றுக்கொள்வீர்கள்

இந்த ஆய்வகம் MCP சர்வர் கட்டமைப்பு முறை, தரவுத்தொகுப்பு வடிவமைப்பு கோட்பாடுகள் மற்றும் AI பயன்பாடுகளுக்கான வலுவான, அளவீட்டுக்குரிய தரவுத்தொகுப்பு ஒருங்கிணைந்த தொழில்நுட்ப செயல்படுத்தல் உத்திகளை ஆழமாக ஆராய்கிறது.

## கண்ணோட்டம்

தரவுத்தொகுப்பு ஒருங்கிணைப்புடன் ஒரு MCP சர்வரை தயாரிப்பு நிலைக்கு கொண்டு வருவதற்கு கவனமாக கட்டமைப்பு முடிவுகள் தேவை. இந்த ஆய்வகம் முக்கிய கூறுகள், வடிவமைப்பு முறைகள் மற்றும் Zava Retail பகுப்பாய்வு தீர்வை வலுவான, பாதுகாப்பான மற்றும் அளவீட்டுக்குரியதாக்கும் தொழில்நுட்ப கருத்துக்களை விளக்குகிறது.

ஒவ்வொரு அடுக்கு எப்படி தொடர்பு கொள்கிறது, குறிப்பிட்ட தொழில்நுட்பங்கள் ஏன் தேர்ந்தெடுக்கப்பட்டன, மற்றும் இந்த முறைகளை உங்கள் MCP செயல்பாடுகளில் எப்படி பயன்படுத்துவது என்பதை நீங்கள் புரிந்துகொள்வீர்கள்.

## கற்றல் நோக்கங்கள்

இந்த ஆய்வகத்தின் முடிவில், நீங்கள்:

- **ஆய்வு செய்ய** MCP சர்வரின் அடுக்கமைப்பு மற்றும் தரவுத்தொகுப்பு ஒருங்கிணைப்பை
- **புரிந்து கொள்ள** ஒவ்வொரு கட்டமைப்பு கூறின் பங்கு மற்றும் பொறுப்புகளை
- **வடிவமைக்க** பல வாடிக்கையாளர் MCP பயன்பாடுகளுக்கு ஆதரவு தரவுத்தொகுப்பு ஸ்கீமாக்களை
- **செயல்படுத்த** இணைப்பு தொகுப்பு மற்றும் வள மேலாண்மை உத்திகளை
- **பயன்படுத்த** உற்பத்தி அமைப்புகளுக்கான பிழை கையாளல் மற்றும் பதிவு முறைகளை
- **மதிப்பீடு செய்ய** பல்வேறு கட்டமைப்பு அணுகுமுறைகளின் வர்த்தக-offs

## 🏗️ MCP சர்வர் கட்டமைப்பு அடுக்குகள்

எங்கள் MCP சர்வர் **அடுக்கமைப்பு** முறையை செயல்படுத்துகிறது, இது கவலைகளை பிரிக்கவும் பராமரிக்கத்தக்கதாக்கவும் உதவுகிறது:

### அடுக்கு 1: நெறிமுறை அடுக்கு (FastMCP)
**பொறுப்பு**: MCP நெறிமுறை தொடர்பு மற்றும் செய்தி வழிமாற்றத்தை கையாளுதல்

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

**முக்கிய அம்சங்கள்**:
- **நெறிமுறை இணக்கம்**: MCP விவரக்குறிப்பு முழுமையான ஆதரவு
- **வகை பாதுகாப்பு**: கோரிக்கை/பதில் சரிபார்ப்புக்கான Pydantic மாடல்கள்
- **அசிங்க ஆதரவு**: அதிக ஒருங்கிணைப்புக்கான non-blocking I/O
- **பிழை கையாளல்**: நிலையான பிழை பதில்கள்

### அடுக்கு 2: வணிக தர்க்க அடுக்கு
**பொறுப்பு**: வணிக விதிகளை செயல்படுத்துதல் மற்றும் நெறிமுறை மற்றும் தரவுத்தொகுப்பு அடுக்குகளுக்கு இடையே ஒருங்கிணைத்தல்

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

**முக்கிய அம்சங்கள்**:
- **வணிக விதி அமலாக்கம்**: கடை அணுகல் சரிபார்ப்பு மற்றும் தரவின் முழுமை
- **சேவை ஒருங்கிணைப்பு**: தரவுத்தொகுப்பு மற்றும் AI சேவைகளுக்கு இடையே ஒருங்கிணைப்பு
- **தரவு மாற்றம்**: மூல தரவை வணிக அறிவாக மாற்றுதல்
- **கேஷிங் உத்தி**: அடிக்கடி கேள்விகளுக்கான செயல்திறன் மேம்பாடு

### அடுக்கு 3: தரவுத்தொகுப்பு அணுகல் அடுக்கு
**பொறுப்பு**: தரவுத்தொகுப்பு இணைப்புகள், கேள்வி செயல்படுத்தல் மற்றும் தரவின் வரைபடத்தை நிர்வகித்தல்

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

**முக்கிய அம்சங்கள்**:
- **இணைப்பு தொகுப்பு**: திறமையான வள மேலாண்மை
- **பரிவர்த்தனை மேலாண்மை**: ACID இணக்கம் மற்றும் ரோல்பேக் கையாளல்
- **கேள்வி மேம்பாடு**: செயல்திறன் கண்காணிப்பு மற்றும் மேம்பாடு
- **RLS ஒருங்கிணைப்பு**: வரிசை நிலை பாதுகாப்பு சூழல் மேலாண்மை

### அடுக்கு 4: உள்கட்டமைப்பு அடுக்கு
**பொறுப்பு**: பதிவு, கண்காணிப்பு மற்றும் கட்டமைப்பு போன்ற குறுக்குவெட்டு கவலைகளை கையாளுதல்

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

## 🗄️ தரவுத்தொகுப்பு வடிவமைப்பு முறைகள்

எங்கள் PostgreSQL ஸ்கீமா பல வாடிக்கையாளர் MCP பயன்பாடுகளுக்கான முக்கிய முறைகளை செயல்படுத்துகிறது:

### 1. பல வாடிக்கையாளர் ஸ்கீமா வடிவமைப்பு

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

**வடிவமைப்பு கோட்பாடுகள்**:
- **வெளியுறு விசை நிலைத்தன்மை**: அட்டவணைகளுக்கு இடையே தரவின் முழுமையை உறுதிசெய்ய
- **கடை ID பரவல்**: ஒவ்வொரு பரிவர்த்தனை அட்டவணையும் store_id ஐ உள்ளடக்கியது
- **UUID முதன்மை விசைகள்**: பகிர்ந்தளிக்கப்பட்ட அமைப்புகளுக்கான உலகளாவிய தனித்துவமான அடையாளங்கள்
- **நேரம்சம் கண்காணிப்பு**: அனைத்து தரவுமாற்றங்களுக்கான ஆடிட் பாதை

### 2. வரிசை நிலை பாதுகாப்பு செயல்படுத்தல்

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

**RLS நன்மைகள்**:
- **தானியங்கி வடிகட்டி**: தரவுத்தொகுப்பு தரவின் தனிமையை அமல்படுத்துகிறது
- **விண்ணப்ப எளிமை**: சிக்கலான WHERE கிளாஸ்கள் தேவையில்லை
- **இயல்பாக பாதுகாப்பு**: தவறாக தரவினை அணுகுவது இயலாது
- **ஆடிட் இணக்கம்**: தெளிவான தரவின் அணுகல் எல்லைகள்

### 3. வெக்டர் தேடல் ஸ்கீமா

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

## 🔌 இணைப்பு மேலாண்மை முறைகள்

MCP சர்வர் செயல்திறனுக்கு திறமையான தரவுத்தொகுப்பு இணைப்பு மேலாண்மை முக்கியமானது:

### இணைப்பு தொகுப்பு கட்டமைப்பு

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

### வள வாழ்க்கைச்சுழி மேலாண்மை

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

## 🛡️ பிழை கையாளல் மற்றும் நிலைத்தன்மை முறைகள்

MCP சர்வர் நம்பகத்தன்மையை உறுதிசெய்ய வலுவான பிழை கையாளல் முக்கியமானது:

### அடுக்கமைப்பு பிழை வகைகள்

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

### பிழை கையாளல் மிடில்வேர்

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

## 📊 செயல்திறன் மேம்பாட்டு உத்திகள்

### கேள்வி செயல்திறன் கண்காணிப்பு

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

### கேஷிங் உத்தி

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

## 🎯 முக்கியக் குறிப்புகள்

இந்த ஆய்வகத்தை முடித்த பிறகு, நீங்கள் புரிந்துகொள்வீர்கள்:

✅ **அடுக்கமைப்பு**: MCP சர்வர் வடிவமைப்பில் கவலைகளை பிரிக்க எப்படி  
✅ **தரவுத்தொகுப்பு முறைகள்**: பல வாடிக்கையாளர் ஸ்கீமா வடிவமைப்பு மற்றும் RLS செயல்படுத்தல்  
✅ **இணைப்பு மேலாண்மை**: திறமையான தொகுப்பு மற்றும் வள வாழ்க்கைச்சுழி  
✅ **பிழை கையாளல்**: அடுக்கமைப்பு பிழை வகைகள் மற்றும் நிலைத்தன்மை முறைகள்  
✅ **செயல்திறன் மேம்பாடு**: கண்காணிப்பு, கேஷிங் மற்றும் கேள்வி மேம்பாடு  
✅ **தயாரிப்பு தயார்மை**: உள்கட்டமைப்பு கவலைகள் மற்றும் செயல்பாட்டு முறைகள்  

## 🚀 அடுத்தது என்ன

**[Lab 02: Security and Multi-Tenancy](../02-Security/README.md)** உடன் தொடரவும்:

- வரிசை நிலை பாதுகாப்பு செயல்படுத்தல் விவரங்கள்
- அங்கீகாரம் மற்றும் அனுமதி முறைகள்
- பல வாடிக்கையாளர் தரவின் தனிமை உத்திகள்
- பாதுகாப்பு ஆடிட் மற்றும் இணக்கம் கருத்துக்கள்

## 📚 கூடுதல் வளங்கள்

### கட்டமைப்பு முறைகள்
- [Python இல் சுத்தமான கட்டமைப்பு](https://github.com/cosmic-python/code) - Python பயன்பாடுகளுக்கான கட்டமைப்பு முறைகள்
- [தரவுத்தொகுப்பு வடிவமைப்பு முறைகள்](https://en.wikipedia.org/wiki/Database_design) - தொடர்புடைய தரவுத்தொகுப்பு வடிவமைப்பு கோட்பாடுகள்
- [மைக்ரோசேவை முறைகள்](https://microservices.io/patterns/) - சேவை கட்டமைப்பு முறைகள்

### PostgreSQL மேம்பட்ட தலைப்புகள்
- [PostgreSQL செயல்திறன் மேம்பாடு](https://wiki.postgresql.org/wiki/Performance_Optimization) - தரவுத்தொகுப்பு மேம்பாட்டு வழிகாட்டி
- [இணைப்பு தொகுப்பு சிறந்த நடைமுறைகள்](https://www.postgresql.org/docs/current/runtime-config-connection.html) - இணைப்பு மேலாண்மை
- [கேள்வி திட்டமிடல் மற்றும் மேம்பாடு](https://www.postgresql.org/docs/current/planner-optimizer.html) - கேள்வி செயல்திறன்

### Python அசிங்க முறைகள்
- [AsyncIO சிறந்த நடைமுறைகள்](https://docs.python.org/3/library/asyncio.html) - அசிங்க நிரலாக்க முறைகள்
- [FastAPI கட்டமைப்பு](https://fastapi.tiangolo.com/advanced/) - நவீன Python வலை கட்டமைப்பு
- [Pydantic மாடல்கள்](https://pydantic-docs.helpmanual.io/) - தரவின் சரிபார்ப்பு மற்றும் சீரமைப்பு

---

**அடுத்தது**: பாதுகாப்பு முறைகளை ஆராய தயாரா? [Lab 02: Security and Multi-Tenancy](../02-Security/README.md) உடன் தொடரவும்

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.