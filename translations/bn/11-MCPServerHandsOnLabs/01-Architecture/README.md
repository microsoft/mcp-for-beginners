# মূল স্থাপত্য ধারণা

## 🎯 এই ল্যাবে কী শেখানো হবে

এই ল্যাবটি MCP সার্ভারের স্থাপত্য প্যাটার্ন, ডাটাবেস ডিজাইনের নীতিমালা এবং শক্তিশালী, স্কেলযোগ্য ডাটাবেস-ইন্টিগ্রেটেড AI অ্যাপ্লিকেশন তৈরির প্রযুক্তিগত বাস্তবায়ন কৌশলগুলোর গভীর বিশ্লেষণ প্রদান করে।

## সংক্ষিপ্ত বিবরণ

ডাটাবেস ইন্টিগ্রেশনের সাথে একটি প্রোডাকশন-রেডি MCP সার্ভার তৈরি করতে সঠিক স্থাপত্য সিদ্ধান্ত নেওয়া অত্যন্ত গুরুত্বপূর্ণ। এই ল্যাবটি আমাদের Zava Retail অ্যানালিটিক্স সমাধানকে শক্তিশালী, নিরাপদ এবং স্কেলযোগ্য করার জন্য প্রয়োজনীয় মূল উপাদান, ডিজাইন প্যাটার্ন এবং প্রযুক্তিগত বিবেচনাগুলো বিশ্লেষণ করে।

আপনি শিখবেন কীভাবে প্রতিটি স্তর একে অপরের সাথে যোগাযোগ করে, কেন নির্দিষ্ট প্রযুক্তিগুলো বেছে নেওয়া হয়েছে এবং কীভাবে এই প্যাটার্নগুলো আপনার নিজস্ব MCP বাস্তবায়নে প্রয়োগ করবেন।

## শেখার লক্ষ্য

এই ল্যাব শেষে আপনি:

- **বিশ্লেষণ** করতে পারবেন MCP সার্ভারের স্তরযুক্ত স্থাপত্য এবং ডাটাবেস ইন্টিগ্রেশন
- **বোঝতে** পারবেন প্রতিটি স্থাপত্য উপাদানের ভূমিকা এবং দায়িত্ব
- **ডিজাইন** করতে পারবেন মাল্টি-টেন্যান্ট MCP অ্যাপ্লিকেশন সমর্থনকারী ডাটাবেস স্কিমা
- **বাস্তবায়ন** করতে পারবেন কানেকশন পুলিং এবং রিসোর্স ম্যানেজমেন্ট কৌশল
- **প্রয়োগ** করতে পারবেন প্রোডাকশন সিস্টেমের জন্য ত্রুটি পরিচালনা এবং লগিং প্যাটার্ন
- **মূল্যায়ন** করতে পারবেন বিভিন্ন স্থাপত্য পদ্ধতির মধ্যে ট্রেড-অফ

## 🏗️ MCP সার্ভারের স্থাপত্য স্তর

আমাদের MCP সার্ভার একটি **স্তরযুক্ত স্থাপত্য** ব্যবহার করে যা রক্ষণাবেক্ষণযোগ্যতা বাড়ায় এবং দায়িত্ব পৃথক করে:

### স্তর ১: প্রোটোকল স্তর (FastMCP)
**দায়িত্ব**: MCP প্রোটোকল যোগাযোগ এবং বার্তা রাউটিং পরিচালনা করা

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

**মূল বৈশিষ্ট্য**:
- **প্রোটোকল সামঞ্জস্য**: MCP স্পেসিফিকেশনের পূর্ণ সমর্থন
- **টাইপ সুরক্ষা**: অনুরোধ/প্রতিক্রিয়া যাচাইয়ের জন্য Pydantic মডেল
- **অ্যাসিঙ্ক সাপোর্ট**: উচ্চ কনকারেন্সির জন্য নন-ব্লকিং I/O
- **ত্রুটি পরিচালনা**: মানক ত্রুটি প্রতিক্রিয়া

### স্তর ২: বিজনেস লজিক স্তর
**দায়িত্ব**: বিজনেস নিয়ম বাস্তবায়ন এবং প্রোটোকল ও ডাটা স্তরের মধ্যে সমন্বয় করা

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

**মূল বৈশিষ্ট্য**:
- **বিজনেস নিয়ম প্রয়োগ**: স্টোর অ্যাক্সেস যাচাই এবং ডাটা অখণ্ডতা
- **সার্ভিস সমন্বয়**: ডাটাবেস এবং AI সার্ভিসের মধ্যে অর্কেস্ট্রেশন
- **ডাটা রূপান্তর**: কাঁচা ডাটাকে বিজনেস ইনসাইটে রূপান্তর করা
- **ক্যাশিং কৌশল**: ঘন ঘন প্রশ্নের জন্য পারফরম্যান্স অপ্টিমাইজেশন

### স্তর ৩: ডাটা অ্যাক্সেস স্তর
**দায়িত্ব**: ডাটাবেস সংযোগ পরিচালনা, প্রশ্ন কার্যকর করা এবং ডাটা ম্যাপিং

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

**মূল বৈশিষ্ট্য**:
- **কানেকশন পুলিং**: দক্ষ রিসোর্স ম্যানেজমেন্ট
- **লেনদেন পরিচালনা**: ACID সামঞ্জস্য এবং রোলব্যাক হ্যান্ডলিং
- **প্রশ্ন অপ্টিমাইজেশন**: পারফরম্যান্স মনিটরিং এবং অপ্টিমাইজেশন
- **RLS ইন্টিগ্রেশন**: রো-লেভেল সিকিউরিটি কনটেক্সট ম্যানেজমেন্ট

### স্তর ৪: ইনফ্রাস্ট্রাকচার স্তর
**দায়িত্ব**: লগিং, মনিটরিং এবং কনফিগারেশনের মতো ক্রস-কাটিং বিষয়গুলো পরিচালনা করা

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

## 🗄️ ডাটাবেস ডিজাইন প্যাটার্ন

আমাদের PostgreSQL স্কিমা মাল্টি-টেন্যান্ট MCP অ্যাপ্লিকেশনের জন্য কয়েকটি গুরুত্বপূর্ণ প্যাটার্ন বাস্তবায়ন করে:

### ১. মাল্টি-টেন্যান্ট স্কিমা ডিজাইন

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

**ডিজাইন নীতিমালা**:
- **ফরেন কী সামঞ্জস্য**: টেবিলগুলোর মধ্যে ডাটা অখণ্ডতা নিশ্চিত করা
- **স্টোর আইডি প্রচার**: প্রতিটি লেনদেন টেবিলে store_id অন্তর্ভুক্ত করা
- **UUID প্রাইমারি কী**: বিতরণকৃত সিস্টেমের জন্য বিশ্বব্যাপী অনন্য শনাক্তকারী
- **টাইমস্ট্যাম্প ট্র্যাকিং**: সমস্ত ডাটা পরিবর্তনের জন্য অডিট ট্রেইল

### ২. রো লেভেল সিকিউরিটি বাস্তবায়ন

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

**RLS সুবিধা**:
- **স্বয়ংক্রিয় ফিল্টারিং**: ডাটাবেস ডাটা আইসোলেশন নিশ্চিত করে
- **অ্যাপ্লিকেশন সরলতা**: জটিল WHERE ক্লজের প্রয়োজন নেই
- **ডিফল্ট নিরাপত্তা**: ভুল ডাটা অ্যাক্সেস করা অসম্ভব
- **অডিট সামঞ্জস্য**: ডাটা অ্যাক্সেসের স্পষ্ট সীমা

### ৩. ভেক্টর সার্চ স্কিমা

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

## 🔌 কানেকশন ম্যানেজমেন্ট প্যাটার্ন

দক্ষ ডাটাবেস কানেকশন ম্যানেজমেন্ট MCP সার্ভারের পারফরম্যান্সের জন্য অত্যন্ত গুরুত্বপূর্ণ:

### কানেকশন পুল কনফিগারেশন

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

### রিসোর্স লাইফসাইকেল ম্যানেজমেন্ট

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

## 🛡️ ত্রুটি পরিচালনা এবং স্থিতিশীলতার প্যাটার্ন

শক্তিশালী ত্রুটি পরিচালনা MCP সার্ভারের নির্ভরযোগ্য অপারেশন নিশ্চিত করে:

### স্তরভিত্তিক ত্রুটি প্রকার

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

### ত্রুটি পরিচালনা মিডলওয়্যার

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

## 📊 পারফরম্যান্স অপ্টিমাইজেশন কৌশল

### প্রশ্ন পারফরম্যান্স মনিটরিং

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

### ক্যাশিং কৌশল

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

## 🎯 মূল বিষয়গুলো

এই ল্যাব সম্পন্ন করার পর আপনি বুঝতে পারবেন:

✅ **স্তরযুক্ত স্থাপত্য**: MCP সার্ভার ডিজাইনে দায়িত্ব পৃথক করার পদ্ধতি  
✅ **ডাটাবেস প্যাটার্ন**: মাল্টি-টেন্যান্ট স্কিমা ডিজাইন এবং RLS বাস্তবায়ন  
✅ **কানেকশন ম্যানেজমেন্ট**: দক্ষ পুলিং এবং রিসোর্স লাইফসাইকেল  
✅ **ত্রুটি পরিচালনা**: স্তরভিত্তিক ত্রুটি প্রকার এবং স্থিতিশীলতার প্যাটার্ন  
✅ **পারফরম্যান্স অপ্টিমাইজেশন**: মনিটরিং, ক্যাশিং এবং প্রশ্ন অপ্টিমাইজেশন  
✅ **প্রোডাকশন প্রস্তুতি**: ইনফ্রাস্ট্রাকচার বিষয় এবং অপারেশনাল প্যাটার্ন  

## 🚀 পরবর্তী ধাপ

**[ল্যাব ০২: নিরাপত্তা এবং মাল্টি-টেন্যান্সি](../02-Security/README.md)** এর সাথে চালিয়ে যান যেখানে বিস্তারিত আলোচনা করা হবে:

- রো লেভেল সিকিউরিটি বাস্তবায়নের বিবরণ
- প্রমাণীকরণ এবং অনুমোদন প্যাটার্ন
- মাল্টি-টেন্যান্ট ডাটা আইসোলেশন কৌশল
- নিরাপত্তা অডিট এবং সামঞ্জস্য বিবেচনা

## 📚 অতিরিক্ত সম্পদ

### স্থাপত্য প্যাটার্ন
- [Python-এ ক্লিন আর্কিটেকচার](https://github.com/cosmic-python/code) - Python অ্যাপ্লিকেশনের জন্য স্থাপত্য প্যাটার্ন
- [ডাটাবেস ডিজাইন প্যাটার্ন](https://en.wikipedia.org/wiki/Database_design) - রিলেশনাল ডাটাবেস ডিজাইনের নীতিমালা
- [মাইক্রোসার্ভিস প্যাটার্ন](https://microservices.io/patterns/) - সার্ভিস স্থাপত্য প্যাটার্ন

### PostgreSQL উন্নত বিষয়
- [PostgreSQL পারফরম্যান্স টিউনিং](https://wiki.postgresql.org/wiki/Performance_Optimization) - ডাটাবেস অপ্টিমাইজেশন গাইড
- [কানেকশন পুলিং সেরা অনুশীলন](https://www.postgresql.org/docs/current/runtime-config-connection.html) - কানেকশন ম্যানেজমেন্ট
- [প্রশ্ন পরিকল্পনা এবং অপ্টিমাইজেশন](https://www.postgresql.org/docs/current/planner-optimizer.html) - প্রশ্ন পারফরম্যান্স

### Python অ্যাসিঙ্ক প্যাটার্ন
- [AsyncIO সেরা অনুশীলন](https://docs.python.org/3/library/asyncio.html) - অ্যাসিঙ্ক প্রোগ্রামিং প্যাটার্ন
- [FastAPI স্থাপত্য](https://fastapi.tiangolo.com/advanced/) - আধুনিক Python ওয়েব স্থাপত্য
- [Pydantic মডেল](https://pydantic-docs.helpmanual.io/) - ডাটা যাচাই এবং সিরিয়ালাইজেশন

---

**পরবর্তী**: নিরাপত্তা প্যাটার্ন অন্বেষণ করতে প্রস্তুত? চালিয়ে যান [ল্যাব ০২: নিরাপত্তা এবং মাল্টি-টেন্যান্সি](../02-Security/README.md)

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।