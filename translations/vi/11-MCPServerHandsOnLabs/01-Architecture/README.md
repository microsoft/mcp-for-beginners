# Các Khái Niệm Cốt Lõi Về Kiến Trúc

## 🎯 Nội Dung Của Bài Thực Hành Này

Bài thực hành này cung cấp một cái nhìn sâu sắc về các mẫu kiến trúc máy chủ MCP, nguyên tắc thiết kế cơ sở dữ liệu, và các chiến lược triển khai kỹ thuật để xây dựng các ứng dụng AI tích hợp cơ sở dữ liệu mạnh mẽ và có khả năng mở rộng.

## Tổng Quan

Xây dựng một máy chủ MCP sẵn sàng cho sản xuất với tích hợp cơ sở dữ liệu đòi hỏi các quyết định kiến trúc cẩn thận. Bài thực hành này phân tích các thành phần chính, mẫu thiết kế, và các yếu tố kỹ thuật giúp giải pháp phân tích Zava Retail của chúng tôi trở nên mạnh mẽ, an toàn, và có khả năng mở rộng.

Bạn sẽ hiểu cách từng lớp tương tác, lý do chọn các công nghệ cụ thể, và cách áp dụng các mẫu này vào các triển khai MCP của riêng bạn.

## Mục Tiêu Học Tập

Kết thúc bài thực hành này, bạn sẽ có thể:

- **Phân tích** kiến trúc phân lớp của máy chủ MCP với tích hợp cơ sở dữ liệu  
- **Hiểu** vai trò và trách nhiệm của từng thành phần kiến trúc  
- **Thiết kế** các sơ đồ cơ sở dữ liệu hỗ trợ ứng dụng MCP đa khách hàng  
- **Triển khai** các chiến lược quản lý kết nối và tài nguyên  
- **Áp dụng** các mẫu xử lý lỗi và ghi nhật ký cho hệ thống sản xuất  
- **Đánh giá** các đánh đổi giữa các cách tiếp cận kiến trúc khác nhau  

## 🏗️ Các Lớp Kiến Trúc Máy Chủ MCP

Máy chủ MCP của chúng tôi triển khai một **kiến trúc phân lớp** để tách biệt các mối quan tâm và thúc đẩy khả năng bảo trì:

### Lớp 1: Lớp Giao Thức (FastMCP)
**Trách nhiệm**: Xử lý giao tiếp giao thức MCP và định tuyến thông điệp

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

**Các Tính Năng Chính**:
- **Tuân Thủ Giao Thức**: Hỗ trợ đầy đủ đặc tả MCP  
- **An Toàn Kiểu Dữ Liệu**: Các mô hình Pydantic để xác thực yêu cầu/phản hồi  
- **Hỗ Trợ Async**: I/O không chặn để đạt độ đồng thời cao  
- **Xử Lý Lỗi**: Phản hồi lỗi được chuẩn hóa  

### Lớp 2: Lớp Logic Kinh Doanh
**Trách nhiệm**: Triển khai các quy tắc kinh doanh và phối hợp giữa lớp giao thức và lớp dữ liệu

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

**Các Tính Năng Chính**:
- **Thực Thi Quy Tắc Kinh Doanh**: Xác thực truy cập cửa hàng và tính toàn vẹn dữ liệu  
- **Phối Hợp Dịch Vụ**: Điều phối giữa cơ sở dữ liệu và các dịch vụ AI  
- **Chuyển Đổi Dữ Liệu**: Chuyển đổi dữ liệu thô thành thông tin kinh doanh  
- **Chiến Lược Bộ Nhớ Đệm**: Tối ưu hóa hiệu suất cho các truy vấn thường xuyên  

### Lớp 3: Lớp Truy Cập Dữ Liệu
**Trách nhiệm**: Quản lý kết nối cơ sở dữ liệu, thực thi truy vấn, và ánh xạ dữ liệu

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

**Các Tính Năng Chính**:
- **Quản Lý Kết Nối**: Quản lý tài nguyên hiệu quả  
- **Quản Lý Giao Dịch**: Tuân thủ ACID và xử lý hoàn tác  
- **Tối Ưu Hóa Truy Vấn**: Giám sát và tối ưu hóa hiệu suất  
- **Tích Hợp RLS**: Quản lý ngữ cảnh bảo mật cấp hàng  

### Lớp 4: Lớp Hạ Tầng
**Trách nhiệm**: Xử lý các mối quan tâm chung như ghi nhật ký, giám sát, và cấu hình

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

## 🗄️ Các Mẫu Thiết Kế Cơ Sở Dữ Liệu

Sơ đồ PostgreSQL của chúng tôi triển khai một số mẫu chính cho các ứng dụng MCP đa khách hàng:

### 1. Thiết Kế Sơ Đồ Đa Khách Hàng

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

**Nguyên Tắc Thiết Kế**:
- **Tính Nhất Quán Khóa Ngoại**: Đảm bảo tính toàn vẹn dữ liệu giữa các bảng  
- **Truyền ID Cửa Hàng**: Mỗi bảng giao dịch đều bao gồm store_id  
- **Khóa Chính UUID**: Các định danh duy nhất toàn cầu cho hệ thống phân tán  
- **Theo Dõi Dấu Thời Gian**: Lưu vết kiểm tra cho tất cả các thay đổi dữ liệu  

### 2. Triển Khai Bảo Mật Cấp Hàng

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

**Lợi Ích Của RLS**:
- **Lọc Tự Động**: Cơ sở dữ liệu thực thi cách ly dữ liệu  
- **Đơn Giản Hóa Ứng Dụng**: Không cần các câu lệnh WHERE phức tạp  
- **Bảo Mật Mặc Định**: Không thể vô tình truy cập dữ liệu sai  
- **Tuân Thủ Kiểm Toán**: Ranh giới truy cập dữ liệu rõ ràng  

### 3. Sơ Đồ Tìm Kiếm Vector

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

## 🔌 Các Mẫu Quản Lý Kết Nối

Quản lý kết nối cơ sở dữ liệu hiệu quả là yếu tố quan trọng đối với hiệu suất máy chủ MCP:

### Cấu Hình Bộ Kết Nối

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

### Quản Lý Vòng Đời Tài Nguyên

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

## 🛡️ Các Mẫu Xử Lý Lỗi và Tăng Cường Độ Tin Cậy

Xử lý lỗi mạnh mẽ đảm bảo hoạt động đáng tin cậy của máy chủ MCP:

### Các Loại Lỗi Phân Cấp

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

### Middleware Xử Lý Lỗi

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

## 📊 Chiến Lược Tối Ưu Hóa Hiệu Suất

### Giám Sát Hiệu Suất Truy Vấn

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

### Chiến Lược Bộ Nhớ Đệm

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

## 🎯 Những Điểm Chính

Sau khi hoàn thành bài thực hành này, bạn sẽ hiểu:

✅ **Kiến Trúc Phân Lớp**: Cách tách biệt các mối quan tâm trong thiết kế máy chủ MCP  
✅ **Mẫu Cơ Sở Dữ Liệu**: Thiết kế sơ đồ đa khách hàng và triển khai RLS  
✅ **Quản Lý Kết Nối**: Bộ kết nối hiệu quả và vòng đời tài nguyên  
✅ **Xử Lý Lỗi**: Các loại lỗi phân cấp và mẫu tăng cường độ tin cậy  
✅ **Tối Ưu Hóa Hiệu Suất**: Giám sát, bộ nhớ đệm, và tối ưu hóa truy vấn  
✅ **Sẵn Sàng Sản Xuất**: Các mối quan tâm về hạ tầng và mẫu vận hành  

## 🚀 Tiếp Theo

Tiếp tục với **[Lab 02: Bảo Mật và Đa Khách Hàng](../02-Security/README.md)** để tìm hiểu sâu hơn về:

- Chi tiết triển khai Bảo Mật Cấp Hàng  
- Các mẫu xác thực và ủy quyền  
- Chiến lược cách ly dữ liệu đa khách hàng  
- Kiểm toán bảo mật và các yếu tố tuân thủ  

## 📚 Tài Nguyên Bổ Sung

### Các Mẫu Kiến Trúc
- [Clean Architecture in Python](https://github.com/cosmic-python/code) - Các mẫu kiến trúc cho ứng dụng Python  
- [Database Design Patterns](https://en.wikipedia.org/wiki/Database_design) - Nguyên tắc thiết kế cơ sở dữ liệu quan hệ  
- [Microservices Patterns](https://microservices.io/patterns/) - Các mẫu kiến trúc dịch vụ  

### Các Chủ Đề Nâng Cao Về PostgreSQL
- [PostgreSQL Performance Tuning](https://wiki.postgresql.org/wiki/Performance_Optimization) - Hướng dẫn tối ưu hóa cơ sở dữ liệu  
- [Connection Pooling Best Practices](https://www.postgresql.org/docs/current/runtime-config-connection.html) - Quản lý kết nối  
- [Query Planning and Optimization](https://www.postgresql.org/docs/current/planner-optimizer.html) - Hiệu suất truy vấn  

### Các Mẫu Async Python
- [AsyncIO Best Practices](https://docs.python.org/3/library/asyncio.html) - Các mẫu lập trình async  
- [FastAPI Architecture](https://fastapi.tiangolo.com/advanced/) - Kiến trúc web Python hiện đại  
- [Pydantic Models](https://pydantic-docs.helpmanual.io/) - Xác thực và tuần tự hóa dữ liệu  

---

**Tiếp Theo**: Sẵn sàng khám phá các mẫu bảo mật? Tiếp tục với [Lab 02: Bảo Mật và Đa Khách Hàng](../02-Security/README.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.