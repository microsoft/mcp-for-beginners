# مفاهیم اصلی معماری

## 🎯 این آزمایشگاه چه چیزی را پوشش می‌دهد؟

این آزمایشگاه به بررسی عمیق الگوهای معماری سرور MCP، اصول طراحی پایگاه داده، و استراتژی‌های پیاده‌سازی فنی که برنامه‌های هوش مصنوعی یکپارچه با پایگاه داده را قدرتمند و مقیاس‌پذیر می‌سازند، می‌پردازد.

## نمای کلی

ساخت یک سرور MCP آماده تولید با یکپارچگی پایگاه داده نیازمند تصمیمات معماری دقیق است. این آزمایشگاه اجزای کلیدی، الگوهای طراحی، و ملاحظات فنی را که راه‌حل تحلیل Zava Retail ما را قدرتمند، امن و مقیاس‌پذیر می‌سازد، تجزیه و تحلیل می‌کند.

شما خواهید فهمید که چگونه هر لایه تعامل دارد، چرا فناوری‌های خاص انتخاب شده‌اند، و چگونه این الگوها را در پیاده‌سازی‌های MCP خود اعمال کنید.

## اهداف یادگیری

تا پایان این آزمایشگاه، شما قادر خواهید بود:

- **تحلیل کنید** معماری لایه‌ای یک سرور MCP با یکپارچگی پایگاه داده  
- **درک کنید** نقش و مسئولیت‌های هر جزء معماری  
- **طراحی کنید** طرح‌های پایگاه داده که از برنامه‌های MCP چند مستاجری پشتیبانی می‌کنند  
- **پیاده‌سازی کنید** استراتژی‌های مدیریت منابع و اتصال  
- **اعمال کنید** الگوهای مدیریت خطا و ثبت وقایع برای سیستم‌های تولیدی  
- **ارزیابی کنید** مزایا و معایب رویکردهای مختلف معماری  

## 🏗️ لایه‌های معماری سرور MCP

سرور MCP ما از یک **معماری لایه‌ای** استفاده می‌کند که نگرانی‌ها را جدا کرده و قابلیت نگهداری را ارتقا می‌دهد:

### لایه ۱: لایه پروتکل (FastMCP)
**مسئولیت**: مدیریت ارتباطات پروتکل MCP و مسیریابی پیام‌ها

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

**ویژگی‌های کلیدی**:
- **رعایت پروتکل**: پشتیبانی کامل از مشخصات MCP  
- **ایمنی نوع**: مدل‌های Pydantic برای اعتبارسنجی درخواست/پاسخ  
- **پشتیبانی از Async**: I/O غیرمسدودکننده برای همزمانی بالا  
- **مدیریت خطا**: پاسخ‌های خطای استاندارد  

### لایه ۲: لایه منطق کسب‌وکار
**مسئولیت**: اجرای قوانین کسب‌وکار و هماهنگی بین لایه پروتکل و داده‌ها

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

**ویژگی‌های کلیدی**:
- **اجرای قوانین کسب‌وکار**: اعتبارسنجی دسترسی به فروشگاه و یکپارچگی داده‌ها  
- **هماهنگی خدمات**: ارکستراسیون بین پایگاه داده و خدمات هوش مصنوعی  
- **تبدیل داده‌ها**: تبدیل داده‌های خام به بینش‌های کسب‌وکار  
- **استراتژی کش**: بهینه‌سازی عملکرد برای پرس‌وجوهای مکرر  

### لایه ۳: لایه دسترسی به داده‌ها
**مسئولیت**: مدیریت اتصالات پایگاه داده، اجرای پرس‌وجوها، و نگاشت داده‌ها

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

**ویژگی‌های کلیدی**:
- **مدیریت اتصال**: مدیریت منابع کارآمد  
- **مدیریت تراکنش**: رعایت ACID و مدیریت بازگشت  
- **بهینه‌سازی پرس‌وجو**: نظارت و بهینه‌سازی عملکرد  
- **یکپارچگی RLS**: مدیریت زمینه امنیت سطح ردیف  

### لایه ۴: لایه زیرساخت
**مسئولیت**: مدیریت نگرانی‌های متقاطع مانند ثبت وقایع، نظارت، و پیکربندی

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

## 🗄️ الگوهای طراحی پایگاه داده

طرح PostgreSQL ما چندین الگوی کلیدی برای برنامه‌های MCP چند مستاجری پیاده‌سازی می‌کند:

### ۱. طراحی طرح چند مستاجری

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

**اصول طراحی**:
- **سازگاری کلید خارجی**: اطمینان از یکپارچگی داده‌ها در جداول  
- **انتشار شناسه فروشگاه**: هر جدول تراکنشی شامل store_id است  
- **کلیدهای اصلی UUID**: شناسه‌های منحصر به فرد جهانی برای سیستم‌های توزیع‌شده  
- **ردیابی زمان**: مسیر حسابرسی برای تمام تغییرات داده  

### ۲. پیاده‌سازی امنیت سطح ردیف (RLS)

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

**مزایای RLS**:
- **فیلتر خودکار**: پایگاه داده جداسازی داده‌ها را اجرا می‌کند  
- **سادگی برنامه**: نیازی به WHERE پیچیده نیست  
- **امنیت پیش‌فرض**: دسترسی تصادفی به داده‌های اشتباه غیرممکن است  
- **رعایت حسابرسی**: مرزهای دسترسی به داده‌ها واضح است  

### ۳. طرح جستجوی برداری

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

## 🔌 الگوهای مدیریت اتصال

مدیریت کارآمد اتصال پایگاه داده برای عملکرد سرور MCP حیاتی است:

### پیکربندی استخر اتصال

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

### مدیریت چرخه عمر منابع

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

## 🛡️ الگوهای مدیریت خطا و مقاومت

مدیریت خطای قوی عملکرد قابل اعتماد سرور MCP را تضمین می‌کند:

### انواع خطاهای سلسله‌مراتبی

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

### میان‌افزار مدیریت خطا

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

## 📊 استراتژی‌های بهینه‌سازی عملکرد

### نظارت بر عملکرد پرس‌وجو

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

### استراتژی کش

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

## 🎯 نکات کلیدی

پس از تکمیل این آزمایشگاه، شما باید درک کنید:

✅ **معماری لایه‌ای**: چگونه نگرانی‌ها را در طراحی سرور MCP جدا کنیم  
✅ **الگوهای پایگاه داده**: طراحی طرح چند مستاجری و پیاده‌سازی RLS  
✅ **مدیریت اتصال**: استخر کارآمد و چرخه عمر منابع  
✅ **مدیریت خطا**: انواع خطاهای سلسله‌مراتبی و الگوهای مقاومت  
✅ **بهینه‌سازی عملکرد**: نظارت، کش، و بهینه‌سازی پرس‌وجو  
✅ **آمادگی تولید**: نگرانی‌های زیرساختی و الگوهای عملیاتی  

## 🚀 مرحله بعدی

ادامه دهید با **[آزمایشگاه ۰۲: امنیت و چند مستاجری](../02-Security/README.md)** برای بررسی عمیق:

- جزئیات پیاده‌سازی امنیت سطح ردیف  
- الگوهای احراز هویت و مجوز  
- استراتژی‌های جداسازی داده‌های چند مستاجری  
- حسابرسی امنیتی و ملاحظات رعایت  

## 📚 منابع اضافی

### الگوهای معماری
- [معماری پاک در پایتون](https://github.com/cosmic-python/code) - الگوهای معماری برای برنامه‌های پایتون  
- [الگوهای طراحی پایگاه داده](https://en.wikipedia.org/wiki/Database_design) - اصول طراحی پایگاه داده رابطه‌ای  
- [الگوهای میکروسرویس](https://microservices.io/patterns/) - الگوهای معماری خدمات  

### موضوعات پیشرفته PostgreSQL
- [تنظیم عملکرد PostgreSQL](https://wiki.postgresql.org/wiki/Performance_Optimization) - راهنمای بهینه‌سازی پایگاه داده  
- [بهترین شیوه‌های استخر اتصال](https://www.postgresql.org/docs/current/runtime-config-connection.html) - مدیریت اتصال  
- [برنامه‌ریزی و بهینه‌سازی پرس‌وجو](https://www.postgresql.org/docs/current/planner-optimizer.html) - عملکرد پرس‌وجو  

### الگوهای Async در پایتون
- [بهترین شیوه‌های AsyncIO](https://docs.python.org/3/library/asyncio.html) - الگوهای برنامه‌نویسی Async  
- [معماری FastAPI](https://fastapi.tiangolo.com/advanced/) - معماری وب مدرن پایتون  
- [مدل‌های Pydantic](https://pydantic-docs.helpmanual.io/) - اعتبارسنجی و سریال‌سازی داده‌ها  

---

**مرحله بعدی**: آماده برای بررسی الگوهای امنیتی؟ ادامه دهید با [آزمایشگاه ۰۲: امنیت و چند مستاجری](../02-Security/README.md)

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.