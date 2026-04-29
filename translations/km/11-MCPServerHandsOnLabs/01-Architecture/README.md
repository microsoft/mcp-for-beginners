# គំនិតស្ថាបត្យកម្មមូលដ្ឋាន

## 🎯 មាតិកាដែលមន្ទីរពិសោធន៍នេះគ្របដណ្តប់

មន្ទីរពិសោធន៍នេះផ្តល់នូវការស្រាវជ្រាវជ្រៅអំពីលំនាំស្ថាបត្យកម្មម៉ាស៊ីនមេ MCP ការរចនាមូលដ្ឋានទិន្នន័យ និងយុទ្ធសាស្រ្តអនុវត្តបច្ចេកទេសដែលឱ្យសមត្ថភាពដំណើរការកម្មវិធី AI ដែលមានមូលដ្ឋានទិន្នន័យរឹងមាំ និងអាចពង្រីកបាន។

## ទិដ្ឋភាពទូទៅ

ការបង្កើតម៉ាស៊ីនមេ MCP ដែលមានភាពរឹងមាំរួមបញ្ចូលនឹងមូលដ្ឋានទិន្នន័យត្រូវការសេចក្ដីស្រៀវសម្រាំងយ៉ាងហ្មត់ចត់ក្នុងការជ្រើសរើសស្ថាបត្យកម្ម។ មន្ទីរពិសោធន៍នេះបំបែកគ្រឿងផ្សំនៃគំរូស្ថាបត្យកម្ម លំនាំរចនា និងវិចារណកថាទាក់ទងបច្ចេកទេសដើម្បីធ្វើឱ្យដំណោះស្រាយវិភាគ Zava Retail របស់យើងរឹងមាំ សុវត្ថិភាព និងអាចពង្រីកបាន។

អ្នកនឹងយល់ដឹងពីរបៀបស្រទាប់នីមួយៗមានប្រតិកម្មយ៉ាងដូចម្តេច មូលហេតុដែលជ្រើសរើសបច្ចេកវិទ្យា ជាក់លាក់ និងរបៀបអនុវត្តលំនាំเหล่านៅលើការអនុវត្ត MCP របស់អ្នកផ្ទាល់។

## គោលបំណងសិក្សា

ចុងបញ្ចប់នៃមន្ទីរពិសោធន៍នេះ អ្នកនឹងអាច៖

- **វិភាគ** ស្ថាបត្យកម្មស្រទាប់នៃម៉ាស៊ីនមេ MCP រួមបញ្ចូលមូលដ្ឋានទិន្នន័យ
- **យល់ដឹង** ពិភពនៃតួនាទី និងកាតព្វកិច្ចនៃគ្រឿងស្ថាបត្យកម្មនីមួយៗ
- **រចនា** ស្កីម៉ាមូលដ្ឋានទិន្នន័យដែលគាំទ្រកម្មវិធី MCP ជាអ្នកប្រើជាច្រើនជាន់
- **អនុវត្ត** ការប្រមូលតភ្ជាប់ និងយុទ្ធសាស្រ្តគ្រប់គ្រងធនធាន
- **អនុវត្ត** លំនាំដោះស្រាយកំហុស និងកំណត់ហេតុនៅក្នុងប្រព័ន្ធផលិតកម្ម
- **វាយតម្លៃ** ការបង្វិលតម្លៃរវាងវិធីសាស្រ្តស្ថាបត្យកម្មផ្សេងៗ

## 🏗️ ស្រទាប់ស្ថាបត្យកម្មម៉ាស៊ីនមេ MCP

ម៉ាស៊ីនមេ MCP របស់យើងអនុវត្ត **ស្ថាបត្យកម្មស្រទាប់** ដែលបំបែកការថែរក្សាអភិរក្សនិងលើកទឹកចិត្តការរក្សាតុល្យភាព៖

### ស្រទាប់ ១៖ ស្រទាប់ប្រព័ន្ធប្រតិបត្តិការ (FastMCP)
**កាតព្វកិច្ច**៖ រៀបចំការទំនាក់ទំនងតាមប្រព័ន្ធ MCP និងការបញ្ជូនសារ

```python
# ការតំឡើងម៉ាស៊ីនមេ FastMCP
from fastmcp import FastMCP

mcp = FastMCP("Zava Retail Analytics")

# ការចុះបញ្ជីឧបករណ៍ជាមួយភាពសុវត្ថិភាពប្រភេទ
@mcp.tool()
async def execute_sales_query(
    ctx: Context,
    postgresql_query: Annotated[str, Field(description="Well-formed PostgreSQL query")]
) -> str:
    """Execute PostgreSQL queries with Row Level Security."""
    return await query_executor.execute(postgresql_query, ctx)
```
  
**លក្ខណៈសំខាន់**៖  
- **គោរពតាមប្រព័ន្ធ**៖ គាំទ្រពេញលេញលក្ខខណ្ឌ MCP  
- **សុវត្ថិភាពប្រភេទ**៖ ម៉ូឌែល Pydantic សម្រាប់បញ្ជាក់សំណើ/ការឆ្លើយ  
- **គាំទ្រ Async**៖ I/O មិនរាំងខ្ទប់សម្រាប់ការជួរថ្មីខ្ពស់  
- **ដោះស្រាយកំហុស**៖ ការឆ្លើយតបកំហុសតាមស្តង់ដារ  

### ស្រទាប់ ២៖ ស្រទាប់តុល្យភាពអាជីវកម្ម
**កាតព្វកិច្ច**៖ អនុវត្តច្បាប់អាជីវកម្ម និងសម្របសម្រួលរវាងស្រទាប់ប្រព័ន្ធ និងស្រទាប់ទិន្នន័យ

```python
class SalesAnalyticsService:
    """Business logic for retail analytics operations."""
    
    async def get_store_performance(
        self, 
        store_id: str, 
        time_period: str
    ) -> Dict[str, Any]:
        """Calculate store performance metrics."""
        
        # បញ្ជាក់ច្បាប់អាជីវកម្ម
        if not self._validate_store_access(store_id):
            raise UnauthorizedError("Access denied for store")
        
        # សម្របសម្រួលការទាញយកទិន្នន័យ
        sales_data = await self.db_provider.get_sales_data(store_id, time_period)
        metrics = self._calculate_metrics(sales_data)
        
        return {
            "store_id": store_id,
            "period": time_period,
            "metrics": metrics,
            "insights": self._generate_insights(metrics)
        }
```
  
**លក្ខណៈសំខាន់**៖  
- **ការអនុវត្តច្បាប់អាជីវកម្ម**៖ ការផ្ទៀងផ្ទាត់ការចូលប្រើហាង និងសុពលភាពទិន្នន័យ  
- **សម្របសម្រួលសេវាកម្ម**៖ សម្របសម្រួលរវាងមូលដ្ឋានទិន្នន័យ និងសេវាកម្ម AI  
- **បំលែងទិន្នន័យ**៖ បម្លែងទិន្នន័យដើមទៅជាឃ្លែងចិត្តអាជីវកម្ម  
- **យុទ្ធសាស្រ្តកំណត់បំលែង**៖ បង្កើនប្រសិទ្ធភាពសម្រាប់សំណួរញឹកញាប់  

### ស្រទាប់ ៣៖ ស្រទាប់ចូលដំណើរការទិន្នន័យ
**កាតព្វកិច្ច**៖ គ្រប់គ្រងការតភ្ជាប់មូលដ្ឋានទិន្នន័យ រៀបចំការសំណួរ និងការប្រែផែនទិន្នន័យ

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
            # កំណត់បរិបទ RLS
            await conn.execute(
                "SELECT set_config('app.current_rls_user_id', $1, false)",
                rls_user_id
            )
            
            # រត់ការសួរជាមួយពេលកំណត់
            try:
                rows = await asyncio.wait_for(
                    conn.fetch(query),
                    timeout=30.0
                )
                return [dict(row) for row in rows]
            except asyncio.TimeoutError:
                raise QueryTimeoutError("Query execution exceeded timeout")
```
  
**លក្ខណៈសំខាន់**៖  
- **ប្រមូលតភ្ជាប់**៖ គ្រប់គ្រងធនធានលើកំណត់  
- **គ្រប់គ្រងប្រតិបត្តិការណ៍**៖ គោរព ACID និងដោះស្រាយការវាយត្រឡប់  
- **បង្កើនប្រសិទ្ធភាពសំណួរ**៖ ត្រួតពិនិត្យនិងបង្កើនប្រសើរឡើង  
- **ការបញ្ចូល RLS**៖ ការគ្រប់គ្រងបរិបទសុវត្ថិភាពកម្រិតជួរ  

### ស្រទាប់ ៤៖ ស្រទាប់ហេដ្ឋារចនាសម្ព័ន្ធ
**កាតព្វកិច្ច**៖ គ្រប់គ្រងបញ្ហាទូទៅដូចជា ការចុះកំណត់ហេតុ ការត្រួតពិនិត្យ និងការកំណត់រចនា

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
  
## 🗄️ លំនាំរចនាដែកទិន្នន័យ

ស្កីមា PostgreSQL របស់យើងអនុវត្តលំនាំសំខាន់ប៉ុន្មានសម្រាប់កម្មវិធី MCP ដែលមានអ្នកប្រើជាច្រើនជាន់៖

### ១. រចនាស្កីម៉ា Multi-Tenant

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
  
**គោលការណ៍រចនា**៖  
- **ភាពសម្បូរបែបកូនផ្សេងគ្នា**៖ ធានាសុពលភាពទិន្នន័យឆ្លងកាត់តារាង  
- **ការបញ្ជូនលេខសម្គាល់ហាង**៖ រាល់តារាងប្រតិបត្តិការណ៍មាន store_id  
- **សោ UUID ជាចម្បង**៖ អត្តសញ្ញាណវិស្ដារពិភពលោកសម្រាប់ប្រព័ន្ធចែកចាយ  
- **ការតាមដានពេលវេលា**៖ សម្ងាត់ធ្វើហើយសិនសម្រាប់ការផ្លាស់ប្តូរទិន្នន័យទាំងអស់  

### ២. ការអនុវត្ត Row Level Security

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
  
**អត្ថប្រយោជន៍របស់ RLS**៖  
- **ចម្រាញ់ដោយស្វ័យប្រវត្តិ**៖ មូលដ្ឋានទិន្នន័យបង្កើតការចាក់ចេញនូវទិន្នន័យបញ្ជី  
- **ភាពងាយស្រួលនៅក្នុងកម្មវិធី**៖ មិនចាំបាច់មាន WHERE ការរវល់សាមញ្ញ  
- **សុវត្ថិភាពដោយដើម**៖ មិនអាចចូលដំណើរការទិន្នន័យខុសបានដោយចៃដន្យ  
- **គោរពការត្រួតពិនិត្យ**៖ ព្រំដែនច្បាស់លាស់នៃការចូលប្រើទិន្នន័យ  

### ៣. ស្កីម៉ាស្វែងរកវិចទ័រ

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
  
## 🔌 លំនាំគ្រប់គ្រងតភ្ជាប់

ការគ្រប់គ្រងតភ្ជាប់មូលដ្ឋានទិន្នន័យបានយ៉ាងមានប្រសិទ្ធភាពគឺសំខាន់សម្រាប់សមត្ថភាពម៉ាស៊ីនមេ MCP៖

### កំណត់តម្លៃប្រមូលតភ្ជាប់

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
            
            # ការកំណត់ការប្រើប្រាស់ស្តុក
            min_size=2,          # ចំណុចខ្សែស្រឡាយអប្បបរមា
            max_size=10,         # ចំណុចខ្សែស្រឡាយអតិបរមា
            max_inactive_connection_lifetime=300,  # ៥ នាទី
            
            # ការកំណត់ការស្វែងរក
            command_timeout=30,   # ការដំណើរការស្វែងរកពេលវេលាចុងក្រោយ
            server_settings={
                "application_name": "zava-mcp-server",
                "jit": "off",          # បិទ JIT សម្រាប់ស្ថិរភាព
                "work_mem": "4MB",     # កំណត់អង្គចងចាំការងារ
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
                
                # ការបង់យឺតបន្ថែមតាមលំដាប់ផ្លូវចំនួន
                await asyncio.sleep(2 ** attempt)
                logger.warning(f"Database connection failed, retrying ({attempt + 1}/{max_retries})")
```
  
### គ្រប់គ្រងជីវិតធនធាន

```python
class MCPServerManager:
    """Manages MCP server lifecycle and resources."""
    
    async def startup(self):
        """Initialize server resources."""
        # បង្កើតរឹងភ្ជាប់មូលដ្ឋានទិន្នន័យ
        self.db_pool = await self.pool_manager.create_pool()
        
        # ចាប់ផ្តើមសេវាកម្ម AI
        self.ai_client = await self.create_ai_client()
        
        # កំណត់ការត្រួតពិនិត្យ
        self.metrics_collector = MetricsCollector()
        
        logger.info("MCP server startup complete")
    
    async def shutdown(self):
        """Cleanup server resources."""
        try:
            # បិទរឹងភ្ជាប់មូលដ្ឋានទិន្នន័យ
            if self.db_pool:
                await self.db_pool.close()
            
            # វះលាងអតិថិជន AI
            if self.ai_client:
                await self.ai_client.close()
            
            # ច្រោះមេត្រិច
            await self.metrics_collector.flush()
            
            logger.info("MCP server shutdown complete")
            
        except Exception as e:
            logger.error(f"Error during shutdown: {e}")
    
    async def health_check(self) -> Dict[str, str]:
        """Verify server health status."""
        status = {}
        
        # ពិនិត្យរឹងភ្ជាប់មូលដ្ឋានទិន្នន័យ
        try:
            async with self.db_pool.acquire() as conn:
                await conn.fetchval("SELECT 1")
            status["database"] = "healthy"
        except Exception as e:
            status["database"] = f"unhealthy: {e}"
        
        # ពិនិត្យសេវាកម្ម AI
        try:
            await self.ai_client.health_check()
            status["ai_service"] = "healthy"
        except Exception as e:
            status["ai_service"] = f"unhealthy: {e}"
        
        return status
```
  
## 🛡️ លំនាំដោះស្រាយកំហុស និងភាពរឹងមាំ

ការដោះស្រាយកំហុសរឹងមាំធានាស្ថិតិដោយម៉ាស៊ីនមេ MCP មានភាពទុកចិត្ត៖

### ប្រភេទកំហុសហេរីអាគី

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
  
### មធ្យោបាយដោះស្រាយកំហុស

```python
@contextmanager
async def error_handling_context(operation_name: str, user_id: str = None):
    """Centralized error handling for operations."""
    start_time = time.time()
    
    try:
        yield
        
        # មេត្រដ្ឋានជោគជ័យ
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
  
## 📊 យុទ្ធសាស្រ្តបង្កើនសមត្ថភាព

### ត្រួតពិនិត្យប្រសិទ្ធភាពសំណួរ

```python
class QueryPerformanceMonitor:
    """Monitor and optimize query performance."""
    
    def __init__(self):
        self.slow_query_threshold = 1.0  # វិនាទី
        self.query_stats = defaultdict(list)
    
    @contextmanager
    async def monitor_query(self, query: str, operation_type: str = "unknown"):
        """Monitor query execution time and performance."""
        start_time = time.time()
        query_hash = hashlib.md5(query.encode()).hexdigest()[:8]
        
        try:
            yield
            
            duration = time.time() - start_time
            
            # កត់ត្រាមេត្រិចការសម្តែង
            self.query_stats[operation_type].append(duration)
            
            # កំណត់ហេតុសំណួរដែលយឺត
            if duration > self.slow_query_threshold:
                logger.warning(f"Slow query detected", extra={
                    "query_hash": query_hash,
                    "duration": duration,
                    "operation_type": operation_type,
                    "query": query[:200]
                })
            
            # បន្ទាន់សម័យមេត្រិច
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
  
### យុទ្ធសាស្រ្តកំណត់បំលែង

```python
class QueryCache:
    """Intelligent query result caching."""
    
    def __init__(self, redis_url: str = None):
        self.cache = {}  # ចុះក្រោមអនុស្សរណៈចិត្ត
        self.redis_client = redis.Redis.from_url(redis_url) if redis_url else None
        self.cache_ttl = 300  # 5 នាទីជា​រយៈពេលលំនាំដើម
    
    async def get_cached_result(
        self, 
        cache_key: str, 
        query_func: Callable,
        ttl: int = None
    ) -> Any:
        """Get result from cache or execute query."""
        ttl = ttl or self.cache_ttl
        
        # ព្យាយាមជាមួយខ្សែផ្ទុកជាមុន
        cached_result = await self._get_from_cache(cache_key)
        if cached_result is not None:
            metrics.cache_hit.labels(type="query").inc()
            return cached_result
        
        # ប្រតិបត្តិការស៊ើបអង្កេត
        metrics.cache_miss.labels(type="query").inc()
        result = await query_func()
        
        # ផ្ទុកលទ្ធផលក្នុងខ្សែផ្ទុក
        await self._set_in_cache(cache_key, result, ttl)
        
        return result
    
    def _generate_cache_key(self, query: str, user_context: str) -> str:
        """Generate consistent cache key."""
        key_data = f"{query}:{user_context}"
        return hashlib.sha256(key_data.encode()).hexdigest()
```
  
## 🎯 ចំណុចសំខាន់

បន្ទាប់ពីបញ្ចប់មន្ទីរពិសោធន៍នេះ អ្នកគួរតែយល់ដឹង៖

✅ **ស្ថាបត្យកម្មស្រទាប់**៖ របៀបបំបែកការថែរក្សាក្នុងការរចនាម៉ាស៊ីនមេ MCP  
✅ **លំនាំមូលដ្ឋានទិន្នន័យ**៖ រចនាស្កីម៉ាពហុជាន់ និងការអនុវត្ត RLS  
✅ **គ្រប់គ្រងតភ្ជាប់**៖ ការប្រមូលតភ្ជាប់មានប្រសិទ្ធភាព និងជីវិតធនធាន  
✅ **ដោះស្រាយកំហុស**៖ ប្រភេទកំហុសហេរីអាគី និងលំនាំភាពរឹងមាំ  
✅ **បង្កើនសមត្ថភាព**៖ ត្រួតពិនិត្យ កំណត់បំលែង និងបង្កើនប្រសិទ្ធភាពសំណួរ  
✅ **ភាពត្រៀមរួចសម្រាប់ផលិតកម្ម**៖ បញ្ហាហេដ្ឋារចនាសម្ព័ន្ធ និងលំនាំប្រតិបត្តិការ  

## 🚀 តើអ្វីទៅជា ជំហានបន្ទាប់

បន្តជាមួយ **[Lab 02: សុវត្ថិភាព និងមហានីយកម្មច្រើនជាន់](../02-Security/README.md)** ដើម្បីបង្កើនជ្រៅក្នុង៖

- យល់ដឹងអំពីការអនុវត្ត Row Level Security
- លំនាំផ្ទៀងផ្ទាត់អត្តសញ្ញាណ និងការអនុញ្ញាត
- យុទ្ធសាស្រ្តបំបែកទិន្នន័យរបស់មហានីយកម្មច្រើនជាន់
- ការត្រួតពិនិត្យសុវត្ថិភាព និងគោលការណ៍គោរព

## 📚 ឯកសារបន្ថែម

### លំនាំស្ថាបត្យកម្ម
- [Clean Architecture ក្នុង Python](https://github.com/cosmic-python/code) - លំនាំស្ថាបត្យកម្មសម្រាប់កម្មវិធី Python  
- [លំនាំរចនាមូលដ្ឋានទិន្នន័យ](https://en.wikipedia.org/wiki/Database_design) - គោលការណ៍រចនាមូលដ្ឋានទិន្នន័យរួម  
- [លំនាំ Microservices](https://microservices.io/patterns/) - លំនាំស្ថាបត្យកម្មសេវាកម្ម  

### ប្រធានបទកម្រិតខ្ពស់ PostgreSQL  
- [ការកែលម្អសមត្ថភាព PostgreSQL](https://wiki.postgresql.org/wiki/Performance_Optimization) - សៀវភៅណែនាំបង្កើនសមត្ថភាព  
- [វិធីការប្រមូលតភ្ជាប់ដ៏ល្អបំផុត](https://www.postgresql.org/docs/current/runtime-config-connection.html) - គ្រប់គ្រងតភ្ជាប់  
- [ផែនការនិងបង្កើនសមត្ថភាពសំណួរ](https://www.postgresql.org/docs/current/planner-optimizer.html) - សមត្ថភាពសំណួរ  

### លំនាំ Python Async  
- [AsyncIO វិធីល្អបំផុត](https://docs.python.org/3/library/asyncio.html) - លំនាំកម្មវិធីAsync  
- [ស្ថាបត្យកម្ម FastAPI](https://fastapi.tiangolo.com/advanced/) - ស្ថាបត្យកម្មបណ្ដាញ Python សម័យទំនើប  
- [ម៉ូឌែល Pydantic](https://pydantic-docs.helpmanual.io/) - ការបញ្ជាក់ទិន្នន័យ និងការបំលែងទ្រង់ទ្រាយ  

---

**បន្ទាប់**៖ រួចរាល់ដែលចូលទៅសិក្សាលំនាំសុវត្ថិភាព? បន្តជាមួយ [Lab 02: សុវត្ថិភាព និងមហានីយកម្មច្រើនជាន់](../02-Security/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖
ឯកសារនេះត្រូវបានបកប្រែក្នុងការប្រើប្រាស់សេវាកម្មបកប្រែដោយ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងដើម្បីភាពត្រឹមត្រូវ សូមយល់អំពីថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនច្បាស់លាស់។ ឯកសារដើមដែលមានភាសាតំណាងគួរត្រូវបានទុកចិត្តជាប្រភពសម្គាល់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឲ្យប្រើការបកប្រែដោយអ្នកជំនាញមនុស្សជាផ្លូវការ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់វៃឬការបកប្រែក្នុងរបៀបខុសណាមួយដែលបង្កឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->