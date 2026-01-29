# แนวคิดสถาปัตยกรรมหลัก

## 🎯 สิ่งที่ห้องปฏิบัติการนี้ครอบคลุม

ห้องปฏิบัติการนี้ให้การสำรวจเชิงลึกเกี่ยวกับรูปแบบสถาปัตยกรรมเซิร์ฟเวอร์ MCP หลักการออกแบบฐานข้อมูล และกลยุทธ์การดำเนินการทางเทคนิคที่ช่วยให้แอปพลิเคชัน AI ที่ผสานรวมฐานข้อมูลมีความแข็งแกร่งและสามารถขยายได้

## ภาพรวม

การสร้างเซิร์ฟเวอร์ MCP ที่พร้อมใช้งานในระดับการผลิตพร้อมการผสานรวมฐานข้อมูลต้องการการตัดสินใจด้านสถาปัตยกรรมอย่างรอบคอบ ห้องปฏิบัติการนี้จะแยกส่วนประกอบสำคัญ รูปแบบการออกแบบ และข้อพิจารณาทางเทคนิคที่ทำให้โซลูชันการวิเคราะห์ Zava Retail ของเรามีความแข็งแกร่ง ปลอดภัย และสามารถขยายได้

คุณจะเข้าใจว่าชั้นแต่ละชั้นทำงานร่วมกันอย่างไร เหตุผลที่เลือกใช้เทคโนโลยีเฉพาะ และวิธีการนำรูปแบบเหล่านี้ไปใช้กับการดำเนินการ MCP ของคุณเอง

## วัตถุประสงค์การเรียนรู้

เมื่อจบห้องปฏิบัติการนี้ คุณจะสามารถ:

- **วิเคราะห์** สถาปัตยกรรมแบบชั้นของเซิร์ฟเวอร์ MCP ที่ผสานรวมฐานข้อมูล  
- **เข้าใจ** บทบาทและความรับผิดชอบของแต่ละส่วนประกอบในสถาปัตยกรรม  
- **ออกแบบ** สคีมาฐานข้อมูลที่รองรับแอปพลิเคชัน MCP แบบหลายผู้เช่า  
- **ดำเนินการ** กลยุทธ์การจัดการทรัพยากรและการเชื่อมต่อ  
- **นำไปใช้** รูปแบบการจัดการข้อผิดพลาดและการบันทึกสำหรับระบบการผลิต  
- **ประเมิน** ข้อดีข้อเสียระหว่างแนวทางสถาปัตยกรรมต่าง ๆ  

## 🏗️ ชั้นสถาปัตยกรรมเซิร์ฟเวอร์ MCP

เซิร์ฟเวอร์ MCP ของเรานำเสนอ **สถาปัตยกรรมแบบชั้น** ที่แยกความกังวลและส่งเสริมการบำรุงรักษา:

### ชั้นที่ 1: ชั้นโปรโตคอล (FastMCP)  
**ความรับผิดชอบ**: จัดการการสื่อสารโปรโตคอล MCP และการกำหนดเส้นทางข้อความ  

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
  
**คุณสมบัติสำคัญ**:  
- **การปฏิบัติตามโปรโตคอล**: รองรับข้อกำหนด MCP อย่างเต็มรูปแบบ  
- **ความปลอดภัยของประเภท**: ใช้โมเดล Pydantic สำหรับการตรวจสอบคำขอ/การตอบกลับ  
- **รองรับ Async**: I/O แบบไม่บล็อกเพื่อรองรับการทำงานพร้อมกันสูง  
- **การจัดการข้อผิดพลาด**: การตอบกลับข้อผิดพลาดที่ได้มาตรฐาน  

### ชั้นที่ 2: ชั้นตรรกะทางธุรกิจ  
**ความรับผิดชอบ**: ดำเนินการกฎทางธุรกิจและประสานงานระหว่างชั้นโปรโตคอลและชั้นข้อมูล  

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
  
**คุณสมบัติสำคัญ**:  
- **การบังคับใช้กฎทางธุรกิจ**: การตรวจสอบการเข้าถึงร้านค้าและความสมบูรณ์ของข้อมูล  
- **การประสานงานบริการ**: การจัดการระหว่างฐานข้อมูลและบริการ AI  
- **การแปลงข้อมูล**: เปลี่ยนข้อมูลดิบให้เป็นข้อมูลเชิงลึกทางธุรกิจ  
- **กลยุทธ์การแคช**: การเพิ่มประสิทธิภาพสำหรับการสืบค้นที่เกิดขึ้นบ่อย  

### ชั้นที่ 3: ชั้นการเข้าถึงข้อมูล  
**ความรับผิดชอบ**: จัดการการเชื่อมต่อฐานข้อมูล การดำเนินการสืบค้น และการแมปข้อมูล  

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
  
**คุณสมบัติสำคัญ**:  
- **การจัดการพูลการเชื่อมต่อ**: การจัดการทรัพยากรอย่างมีประสิทธิภาพ  
- **การจัดการธุรกรรม**: การปฏิบัติตาม ACID และการจัดการการย้อนกลับ  
- **การเพิ่มประสิทธิภาพการสืบค้น**: การตรวจสอบและเพิ่มประสิทธิภาพ  
- **การผสานรวม RLS**: การจัดการบริบทความปลอดภัยระดับแถว  

### ชั้นที่ 4: ชั้นโครงสร้างพื้นฐาน  
**ความรับผิดชอบ**: จัดการข้อกังวลข้ามส่วน เช่น การบันทึก การตรวจสอบ และการกำหนดค่า  

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
  

## 🗄️ รูปแบบการออกแบบฐานข้อมูล

สคีมา PostgreSQL ของเรานำเสนอรูปแบบสำคัญหลายประการสำหรับแอปพลิเคชัน MCP แบบหลายผู้เช่า:

### 1. การออกแบบสคีมาแบบหลายผู้เช่า  

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
  
**หลักการออกแบบ**:  
- **ความสอดคล้องของคีย์ต่างประเทศ**: รับรองความสมบูรณ์ของข้อมูลระหว่างตาราง  
- **การส่งต่อ ID ร้านค้า**: ทุกตารางธุรกรรมรวมถึง store_id  
- **คีย์หลัก UUID**: ตัวระบุที่ไม่ซ้ำกันทั่วโลกสำหรับระบบแบบกระจาย  
- **การติดตามเวลา**: เส้นทางการตรวจสอบสำหรับการเปลี่ยนแปลงข้อมูลทั้งหมด  

### 2. การดำเนินการความปลอดภัยระดับแถว  

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
  
**ประโยชน์ของ RLS**:  
- **การกรองอัตโนมัติ**: ฐานข้อมูลบังคับใช้การแยกข้อมูล  
- **ความเรียบง่ายของแอปพลิเคชัน**: ไม่จำเป็นต้องใช้ WHERE clause ที่ซับซ้อน  
- **ความปลอดภัยโดยค่าเริ่มต้น**: ไม่สามารถเข้าถึงข้อมูลผิดพลาดได้โดยไม่ตั้งใจ  
- **การปฏิบัติตามการตรวจสอบ**: ขอบเขตการเข้าถึงข้อมูลที่ชัดเจน  

### 3. สคีมาสำหรับการค้นหาเวกเตอร์  

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
  

## 🔌 รูปแบบการจัดการการเชื่อมต่อ

การจัดการการเชื่อมต่อฐานข้อมูลอย่างมีประสิทธิภาพเป็นสิ่งสำคัญสำหรับประสิทธิภาพของเซิร์ฟเวอร์ MCP:

### การกำหนดค่าพูลการเชื่อมต่อ  

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
  

### การจัดการวงจรชีวิตทรัพยากร  

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
  

## 🛡️ รูปแบบการจัดการข้อผิดพลาดและความยืดหยุ่น

การจัดการข้อผิดพลาดที่แข็งแกร่งช่วยให้เซิร์ฟเวอร์ MCP ทำงานได้อย่างน่าเชื่อถือ:

### ประเภทข้อผิดพลาดแบบลำดับชั้น  

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
  

### มิดเดิลแวร์การจัดการข้อผิดพลาด  

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
  

## 📊 กลยุทธ์การเพิ่มประสิทธิภาพ

### การตรวจสอบประสิทธิภาพการสืบค้น  

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
  

### กลยุทธ์การแคช  

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
  

## 🎯 บทสรุปสำคัญ

หลังจากจบห้องปฏิบัติการนี้ คุณควรเข้าใจ:  

✅ **สถาปัตยกรรมแบบชั้น**: วิธีการแยกความกังวลในออกแบบเซิร์ฟเวอร์ MCP  
✅ **รูปแบบฐานข้อมูล**: การออกแบบสคีมาแบบหลายผู้เช่าและการดำเนินการ RLS  
✅ **การจัดการการเชื่อมต่อ**: การจัดการพูลอย่างมีประสิทธิภาพและวงจรชีวิตทรัพยากร  
✅ **การจัดการข้อผิดพลาด**: ประเภทข้อผิดพลาดแบบลำดับชั้นและรูปแบบความยืดหยุ่น  
✅ **การเพิ่มประสิทธิภาพ**: การตรวจสอบ การแคช และการเพิ่มประสิทธิภาพการสืบค้น  
✅ **ความพร้อมใช้งานในระดับการผลิต**: ข้อกังวลด้านโครงสร้างพื้นฐานและรูปแบบการดำเนินงาน  

## 🚀 สิ่งที่ต้องทำต่อไป

ดำเนินการต่อกับ **[Lab 02: Security and Multi-Tenancy](../02-Security/README.md)** เพื่อเจาะลึกใน:  

- รายละเอียดการดำเนินการความปลอดภัยระดับแถว  
- รูปแบบการตรวจสอบสิทธิ์และการอนุญาต  
- กลยุทธ์การแยกข้อมูลแบบหลายผู้เช่า  
- การตรวจสอบความปลอดภัยและข้อพิจารณาด้านการปฏิบัติตาม  

## 📚 แหล่งข้อมูลเพิ่มเติม

### รูปแบบสถาปัตยกรรม  
- [Clean Architecture in Python](https://github.com/cosmic-python/code) - รูปแบบสถาปัตยกรรมสำหรับแอปพลิเคชัน Python  
- [Database Design Patterns](https://en.wikipedia.org/wiki/Database_design) - หลักการออกแบบฐานข้อมูลเชิงสัมพันธ์  
- [Microservices Patterns](https://microservices.io/patterns/) - รูปแบบสถาปัตยกรรมบริการ  

### หัวข้อขั้นสูงของ PostgreSQL  
- [PostgreSQL Performance Tuning](https://wiki.postgresql.org/wiki/Performance_Optimization) - คู่มือการเพิ่มประสิทธิภาพฐานข้อมูล  
- [Connection Pooling Best Practices](https://www.postgresql.org/docs/current/runtime-config-connection.html) - การจัดการการเชื่อมต่อ  
- [Query Planning and Optimization](https://www.postgresql.org/docs/current/planner-optimizer.html) - ประสิทธิภาพการสืบค้น  

### รูปแบบ Async ใน Python  
- [AsyncIO Best Practices](https://docs.python.org/3/library/asyncio.html) - รูปแบบการเขียนโปรแกรม Async  
- [FastAPI Architecture](https://fastapi.tiangolo.com/advanced/) - สถาปัตยกรรมเว็บ Python สมัยใหม่  
- [Pydantic Models](https://pydantic-docs.helpmanual.io/) - การตรวจสอบและการจัดรูปแบบข้อมูล  

---

**ถัดไป**: พร้อมที่จะสำรวจรูปแบบความปลอดภัย? ดำเนินการต่อกับ [Lab 02: Security and Multi-Tenancy](../02-Security/README.md)  

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้