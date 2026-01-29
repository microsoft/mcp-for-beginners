# ਕੋਰ ਆਰਕੀਟੈਕਚਰ ਸੰਕਲਪ

## 🎯 ਇਹ ਲੈਬ ਕੀ ਕਵਰ ਕਰਦੀ ਹੈ

ਇਹ ਲੈਬ MCP ਸਰਵਰ ਆਰਕੀਟੈਕਚਰ ਪੈਟਰਨ, ਡਾਟਾਬੇਸ ਡਿਜ਼ਾਈਨ ਸਿਧਾਂਤਾਂ, ਅਤੇ ਤਕਨੀਕੀ ਅਮਲ ਰਣਨੀਤੀਆਂ ਦਾ ਵਿਸਤ੍ਰਿਤ ਅਧਿਐਨ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ ਜੋ ਮਜ਼ਬੂਤ, ਸਕੇਲ ਕਰਨ ਯੋਗ ਡਾਟਾਬੇਸ-ਇੰਟੀਗ੍ਰੇਟਡ AI ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਸ਼ਕਤੀ ਦਿੰਦੀ ਹੈ।

## ਓਵਰਵਿਊ

ਡਾਟਾਬੇਸ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦੇ ਨਾਲ ਇੱਕ ਪ੍ਰੋਡਕਸ਼ਨ-ਰੇਡੀ MCP ਸਰਵਰ ਬਣਾਉਣ ਲਈ ਧਿਆਨਪੂਰਵਕ ਆਰਕੀਟੈਕਚਰ ਫੈਸਲੇ ਲੈਣੇ ਪੈਂਦੇ ਹਨ। ਇਹ ਲੈਬ ਸਾਡੇ Zava Retail ਐਨਾਲਿਟਿਕਸ ਹੱਲ ਨੂੰ ਮਜ਼ਬੂਤ, ਸੁਰੱਖਿਅਤ, ਅਤੇ ਸਕੇਲ ਕਰਨ ਯੋਗ ਬਣਾਉਣ ਵਾਲੇ ਮੁੱਖ ਹਿੱਸਿਆਂ, ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ, ਅਤੇ ਤਕਨੀਕੀ ਵਿਚਾਰਾਂ ਨੂੰ ਤੋੜ ਕੇ ਸਮਝਾਉਂਦੀ ਹੈ।

ਤੁਹਾਨੂੰ ਸਮਝ ਆਵੇਗੀ ਕਿ ਹਰ ਲੇਅਰ ਕਿਵੇਂ ਇੰਟਰੈਕਟ ਕਰਦੀ ਹੈ, ਕਿਉਂ ਖਾਸ ਤਕਨਾਲੋਜੀਆਂ ਦੀ ਚੋਣ ਕੀਤੀ ਗਈ, ਅਤੇ ਕਿਵੇਂ ਤੁਸੀਂ ਆਪਣੇ MCP ਅਮਲਾਂ ਵਿੱਚ ਇਹ ਪੈਟਰਨ ਲਾਗੂ ਕਰ ਸਕਦੇ ਹੋ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਲੈਬ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਇਹ ਕਰਨ ਦੇ ਯੋਗ ਹੋਵੋਗੇ:

- **ਵਿਸ਼ਲੇਸ਼ਣ** ਕਰੋ: ਡਾਟਾਬੇਸ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦੇ ਨਾਲ MCP ਸਰਵਰ ਦੀ ਲੇਅਰਡ ਆਰਕੀਟੈਕਚਰ  
- **ਸਮਝੋ**: ਹਰ ਆਰਕੀਟੈਕਚਰ ਹਿੱਸੇ ਦੀ ਭੂਮਿਕਾ ਅਤੇ ਜ਼ਿੰਮੇਵਾਰੀਆਂ  
- **ਡਿਜ਼ਾਈਨ** ਕਰੋ: ਡਾਟਾਬੇਸ ਸਕੀਮਾ ਜੋ ਮਲਟੀ-ਟੈਨੈਂਟ MCP ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਸਹਾਰਾ ਦਿੰਦੇ ਹਨ  
- **ਅਮਲ ਕਰੋ**: ਕਨੈਕਸ਼ਨ ਪੂਲਿੰਗ ਅਤੇ ਰਿਸੋਰਸ ਮੈਨੇਜਮੈਂਟ ਰਣਨੀਤੀਆਂ  
- **ਲਾਗੂ ਕਰੋ**: ਪ੍ਰੋਡਕਸ਼ਨ ਸਿਸਟਮ ਲਈ ਐਰਰ ਹੈਂਡਲਿੰਗ ਅਤੇ ਲੌਗਿੰਗ ਪੈਟਰਨ  
- **ਮੁਲਾਂਕਣ ਕਰੋ**: ਵੱਖ-ਵੱਖ ਆਰਕੀਟੈਕਚਰ ਪਹੁੰਚਾਂ ਦੇ ਵਿਚਕਾਰ ਟਰੇਡ-ਆਫ਼

## 🏗️ MCP ਸਰਵਰ ਆਰਕੀਟੈਕਚਰ ਲੇਅਰ

ਸਾਡੇ MCP ਸਰਵਰ ਨੇ **ਲੇਅਰਡ ਆਰਕੀਟੈਕਚਰ** ਨੂੰ ਅਪਨਾਇਆ ਹੈ ਜੋ ਚਿੰਤਾਵਾਂ ਨੂੰ ਵੱਖ ਕਰਦਾ ਹੈ ਅਤੇ ਮਰੰਮਤਯੋਗਤਾ ਨੂੰ ਵਧਾਉਂਦਾ ਹੈ:

### ਲੇਅਰ 1: ਪ੍ਰੋਟੋਕੋਲ ਲੇਅਰ (FastMCP)
**ਜ਼ਿੰਮੇਵਾਰੀ**: MCP ਪ੍ਰੋਟੋਕੋਲ ਸੰਚਾਰ ਅਤੇ ਸੁਨੇਹਾ ਰੂਟਿੰਗ ਨੂੰ ਸੰਭਾਲਣਾ

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

**ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ**:
- **ਪ੍ਰੋਟੋਕੋਲ ਅਨੁਕੂਲਤਾ**: ਪੂਰੀ MCP ਵਿਸ਼ੇਸ਼ਤਾ ਸਹਾਇਤਾ  
- **ਟਾਈਪ ਸੇਫਟੀ**: ਰਿਕਵੈਸਟ/ਰਿਸਪਾਂਸ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਈ Pydantic ਮਾਡਲ  
- **ਐਸਿੰਕ ਸਹਾਇਤਾ**: ਉੱਚ ਸਮਕਾਲੀਤਾ ਲਈ ਨਾਨ-ਬਲਾਕਿੰਗ I/O  
- **ਐਰਰ ਹੈਂਡਲਿੰਗ**: ਮਿਆਰੀਕ੍ਰਿਤ ਐਰਰ ਜਵਾਬ

### ਲੇਅਰ 2: ਬਿਜ਼ਨਸ ਲਾਜ਼ਿਕ ਲੇਅਰ
**ਜ਼ਿੰਮੇਵਾਰੀ**: ਬਿਜ਼ਨਸ ਨਿਯਮ ਲਾਗੂ ਕਰਨਾ ਅਤੇ ਪ੍ਰੋਟੋਕੋਲ ਅਤੇ ਡਾਟਾ ਲੇਅਰ ਦੇ ਵਿਚਕਾਰ ਸਹਿਕਾਰ ਕਰਨਾ

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

**ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ**:
- **ਬਿਜ਼ਨਸ ਨਿਯਮ ਲਾਗੂ ਕਰਨਾ**: ਸਟੋਰ ਐਕਸੈਸ ਵੈਰੀਫਿਕੇਸ਼ਨ ਅਤੇ ਡਾਟਾ ਦੀ ਸੱਚਾਈ  
- **ਸੇਵਾ ਸਹਿਕਾਰ**: ਡਾਟਾਬੇਸ ਅਤੇ AI ਸੇਵਾਵਾਂ ਦੇ ਵਿਚਕਾਰ ਸੰਗਠਨ  
- **ਡਾਟਾ ਰੂਪਾਂਤਰਨ**: ਕੱਚੇ ਡਾਟਾ ਨੂੰ ਬਿਜ਼ਨਸ ਅੰਤਰਦ੍ਰਿਸ਼ਟੀ ਵਿੱਚ ਬਦਲਣਾ  
- **ਕੈਸ਼ਿੰਗ ਰਣਨੀਤੀ**: ਵਾਰੰ-ਵਾਰ ਪੁੱਛੇ ਜਾਣ ਵਾਲੇ ਪ੍ਰਸ਼ਨਾਂ ਲਈ ਪ੍ਰਦਰਸ਼ਨ ਦਾ ਅਧਿਕਤਮ

### ਲੇਅਰ 3: ਡਾਟਾ ਐਕਸੈਸ ਲੇਅਰ
**ਜ਼ਿੰਮੇਵਾਰੀ**: ਡਾਟਾਬੇਸ ਕਨੈਕਸ਼ਨ, ਪੁੱਛਗਿੱਛ ਅਮਲ, ਅਤੇ ਡਾਟਾ ਮੈਪਿੰਗ ਦਾ ਪ੍ਰਬੰਧਨ

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

**ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ**:
- **ਕਨੈਕਸ਼ਨ ਪੂਲਿੰਗ**: ਕੁਸ਼ਲ ਰਿਸੋਰਸ ਮੈਨੇਜਮੈਂਟ  
- **ਟ੍ਰਾਂਜ਼ੈਕਸ਼ਨ ਮੈਨੇਜਮੈਂਟ**: ACID ਅਨੁਕੂਲਤਾ ਅਤੇ ਰੋਲਬੈਕ ਹੈਂਡਲਿੰਗ  
- **ਪੁੱਛਗਿੱਛ ਅਧਿਕਤਮ**: ਪ੍ਰਦਰਸ਼ਨ ਮਾਨਟਰਿੰਗ ਅਤੇ ਅਧਿਕਤਮ  
- **RLS ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: ਰੋਅ-ਲੈਵਲ ਸੁਰੱਖਿਆ ਸੰਦਰਭ ਪ੍ਰਬੰਧਨ

### ਲੇਅਰ 4: ਇੰਫਰਾਸਟਰਕਚਰ ਲੇਅਰ
**ਜ਼ਿੰਮੇਵਾਰੀ**: ਲੌਗਿੰਗ, ਮਾਨਟਰਿੰਗ, ਅਤੇ ਕਨਫਿਗਰੇਸ਼ਨ ਵਰਗੇ ਕੱਟ-ਕਰਾਸ ਚਿੰਤਾਵਾਂ ਨੂੰ ਸੰਭਾਲਣਾ

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

## 🗄️ ਡਾਟਾਬੇਸ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ

ਸਾਡਾ PostgreSQL ਸਕੀਮਾ ਮਲਟੀ-ਟੈਨੈਂਟ MCP ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਕਈ ਮੁੱਖ ਪੈਟਰਨ ਲਾਗੂ ਕਰਦਾ ਹੈ:

### 1. ਮਲਟੀ-ਟੈਨੈਂਟ ਸਕੀਮਾ ਡਿਜ਼ਾਈਨ

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

**ਡਿਜ਼ਾਈਨ ਸਿਧਾਂਤ**:
- **ਵਿਦੇਸ਼ੀ ਕੁੰਜੀ ਸਥਿਰਤਾ**: ਟੇਬਲਾਂ ਦੇ ਵਿਚਕਾਰ ਡਾਟਾ ਦੀ ਸੱਚਾਈ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਣਾ  
- **ਸਟੋਰ ID ਪ੍ਰਸਾਰਣ**: ਹਰ ਲੈਣ-ਦੇਣ ਵਾਲੀ ਟੇਬਲ ਵਿੱਚ store_id ਸ਼ਾਮਲ ਹੈ  
- **UUID ਪ੍ਰਾਇਮਰੀ ਕੁੰਜੀਆਂ**: ਵੰਡੇ ਸਿਸਟਮਾਂ ਲਈ ਵਿਸ਼ਵ-ਵਿਆਪੀ ਵਿਲੱਖਣ ਪਹਿਚਾਨਕਰਤਾ  
- **ਟਾਈਮਸਟੈਂਪ ਟ੍ਰੈਕਿੰਗ**: ਸਾਰੇ ਡਾਟਾ ਬਦਲਾਅ ਲਈ ਆਡਿਟ ਟ੍ਰੇਲ

### 2. ਰੋਅ ਲੈਵਲ ਸੁਰੱਖਿਆ ਲਾਗੂ ਕਰਨਾ

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

**RLS ਫਾਇਦੇ**:
- **ਆਟੋਮੈਟਿਕ ਫਿਲਟਰਿੰਗ**: ਡਾਟਾਬੇਸ ਡਾਟਾ ਆਈਸੋਲੇਸ਼ਨ ਨੂੰ ਲਾਗੂ ਕਰਦਾ ਹੈ  
- **ਐਪਲੀਕੇਸ਼ਨ ਸਾਦਗੀ**: ਕੋਈ ਜਟਿਲ WHERE ਕਲੌਜ਼ ਦੀ ਲੋੜ ਨਹੀਂ  
- **ਡਿਫਾਲਟ ਦੁਆਰਾ ਸੁਰੱਖਿਆ**: ਗਲਤੀ ਨਾਲ ਗਲਤ ਡਾਟਾ ਤੱਕ ਪਹੁੰਚਣਾ ਅਸੰਭਵ  
- **ਆਡਿਟ ਅਨੁਕੂਲਤਾ**: ਸਪਸ਼ਟ ਡਾਟਾ ਪਹੁੰਚ ਸੀਮਾਵਾਂ

### 3. ਵੈਕਟਰ ਖੋਜ ਸਕੀਮਾ

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

## 🔌 ਕਨੈਕਸ਼ਨ ਮੈਨੇਜਮੈਂਟ ਪੈਟਰਨ

ਕੁਸ਼ਲ ਡਾਟਾਬੇਸ ਕਨੈਕਸ਼ਨ ਮੈਨੇਜਮੈਂਟ MCP ਸਰਵਰ ਦੇ ਪ੍ਰਦਰਸ਼ਨ ਲਈ ਮਹੱਤਵਪੂਰਨ ਹੈ:

### ਕਨੈਕਸ਼ਨ ਪੂਲ ਕਨਫਿਗਰੇਸ਼ਨ

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

### ਰਿਸੋਰਸ ਲਾਈਫਸਾਈਕਲ ਮੈਨੇਜਮੈਂਟ

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

## 🛡️ ਐਰਰ ਹੈਂਡਲਿੰਗ ਅਤੇ ਰੇਜ਼ੀਲੀਅੰਸ ਪੈਟਰਨ

ਮਜ਼ਬੂਤ ਐਰਰ ਹੈਂਡਲਿੰਗ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ MCP ਸਰਵਰ ਵਿਸ਼ਵਾਸਯੋਗ ਤਰੀਕੇ ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ:

### ਹਾਇਰਾਰਕੀਕਲ ਐਰਰ ਕਿਸਮਾਂ

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

### ਐਰਰ ਹੈਂਡਲਿੰਗ ਮਿਡਲਵੇਅਰ

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

## 📊 ਪ੍ਰਦਰਸ਼ਨ ਅਧਿਕਤਮ ਰਣਨੀਤੀਆਂ

### ਪੁੱਛਗਿੱਛ ਪ੍ਰਦਰਸ਼ਨ ਮਾਨਟਰਿੰਗ

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

### ਕੈਸ਼ਿੰਗ ਰਣਨੀਤੀ

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

## 🎯 ਮੁੱਖ ਨਿਸ਼ਚੇ

ਇਸ ਲੈਬ ਨੂੰ ਪੂਰਾ ਕਰਨ ਦੇ ਬਾਅਦ, ਤੁਸੀਂ ਸਮਝ ਸਕਦੇ ਹੋ:

✅ **ਲੇਅਰਡ ਆਰਕੀਟੈਕਚਰ**: MCP ਸਰਵਰ ਡਿਜ਼ਾਈਨ ਵਿੱਚ ਚਿੰਤਾਵਾਂ ਨੂੰ ਵੱਖ ਕਰਨ ਦਾ ਤਰੀਕਾ  
✅ **ਡਾਟਾਬੇਸ ਪੈਟਰਨ**: ਮਲਟੀ-ਟੈਨੈਂਟ ਸਕੀਮਾ ਡਿਜ਼ਾਈਨ ਅਤੇ RLS ਲਾਗੂ ਕਰਨਾ  
✅ **ਕਨੈਕਸ਼ਨ ਮੈਨੇਜਮੈਂਟ**: ਕੁਸ਼ਲ ਪੂਲਿੰਗ ਅਤੇ ਰਿਸੋਰਸ ਲਾਈਫਸਾਈਕਲ  
✅ **ਐਰਰ ਹੈਂਡਲਿੰਗ**: ਹਾਇਰਾਰਕੀਕਲ ਐਰਰ ਕਿਸਮਾਂ ਅਤੇ ਰੇਜ਼ੀਲੀਅੰਸ ਪੈਟਰਨ  
✅ **ਪ੍ਰਦਰਸ਼ਨ ਅਧਿਕਤਮ**: ਮਾਨਟਰਿੰਗ, ਕੈਸ਼ਿੰਗ, ਅਤੇ ਪੁੱਛਗਿੱਛ ਅਧਿਕਤਮ  
✅ **ਪ੍ਰੋਡਕਸ਼ਨ ਤਿਆਰੀ**: ਇੰਫਰਾਸਟਰਕਚਰ ਚਿੰਤਾਵਾਂ ਅਤੇ ਓਪਰੇਸ਼ਨਲ ਪੈਟਰਨ  

## 🚀 ਅਗਲਾ ਕੀ ਹੈ

**[ਲੈਬ 02: ਸੁਰੱਖਿਆ ਅਤੇ ਮਲਟੀ-ਟੈਨੈਂਸੀ](../02-Security/README.md)** ਨਾਲ ਜਾਰੀ ਰੱਖੋ:

- ਰੋਅ ਲੈਵਲ ਸੁਰੱਖਿਆ ਲਾਗੂ ਕਰਨ ਦੇ ਵੇਰਵੇ  
- ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਅਧਿਕਾਰ ਪੈਟਰਨ  
- ਮਲਟੀ-ਟੈਨੈਂਟ ਡਾਟਾ ਆਈਸੋਲੇਸ਼ਨ ਰਣਨੀਤੀਆਂ  
- ਸੁਰੱਖਿਆ ਆਡਿਟ ਅਤੇ ਅਨੁਕੂਲਤਾ ਵਿਚਾਰ

## 📚 ਵਾਧੂ ਸਰੋਤ

### ਆਰਕੀਟੈਕਚਰ ਪੈਟਰਨ
- [Python ਵਿੱਚ ਕਲੀਨ ਆਰਕੀਟੈਕਚਰ](https://github.com/cosmic-python/code) - Python ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਆਰਕੀਟੈਕਚਰ ਪੈਟਰਨ  
- [ਡਾਟਾਬੇਸ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ](https://en.wikipedia.org/wiki/Database_design) - ਰਿਲੇਸ਼ਨਲ ਡਾਟਾਬੇਸ ਡਿਜ਼ਾਈਨ ਸਿਧਾਂਤ  
- [ਮਾਈਕ੍ਰੋਸਰਵਿਸ ਪੈਟਰਨ](https://microservices.io/patterns/) - ਸੇਵਾ ਆਰਕੀਟੈਕਚਰ ਪੈਟਰਨ  

### PostgreSQL ਉੱਚ-ਸਤਹ ਵਿਸ਼ੇ
- [PostgreSQL ਪ੍ਰਦਰਸ਼ਨ ਟਿਊਨਿੰਗ](https://wiki.postgresql.org/wiki/Performance_Optimization) - ਡਾਟਾਬੇਸ ਅਧਿਕਤਮ ਗਾਈਡ  
- [ਕਨੈਕਸ਼ਨ ਪੂਲਿੰਗ ਬਿਹਤਰ ਅਭਿਆਸ](https://www.postgresql.org/docs/current/runtime-config-connection.html) - ਕਨੈਕਸ਼ਨ ਮੈਨੇਜਮੈਂਟ  
- [ਪੁੱਛਗਿੱਛ ਯੋਜਨਾ ਅਤੇ ਅਧਿਕਤਮ](https://www.postgresql.org/docs/current/planner-optimizer.html) - ਪੁੱਛਗਿੱਛ ਪ੍ਰਦਰਸ਼ਨ  

### Python Async ਪੈਟਰਨ
- [AsyncIO ਬਿਹਤਰ ਅਭਿਆਸ](https://docs.python.org/3/library/asyncio.html) - Async ਪ੍ਰੋਗਰਾਮਿੰਗ ਪੈਟਰਨ  
- [FastAPI ਆਰਕੀਟੈਕਚਰ](https://fastapi.tiangolo.com/advanced/) - ਆਧੁਨਿਕ Python ਵੈੱਬ ਆਰਕੀਟੈਕਚਰ  
- [Pydantic ਮਾਡਲ](https://pydantic-docs.helpmanual.io/) - ਡਾਟਾ ਵੈਰੀਫਿਕੇਸ਼ਨ ਅਤੇ ਸੀਰੀਅਲਾਈਜ਼ੇਸ਼ਨ  

---

**ਅਗਲਾ**: ਸੁਰੱਖਿਆ ਪੈਟਰਨ ਦੀ ਖੋਜ ਕਰਨ ਲਈ ਤਿਆਰ? [ਲੈਬ 02: ਸੁਰੱਖਿਆ ਅਤੇ ਮਲਟੀ-ਟੈਨੈਂਸੀ](../02-Security/README.md) ਨਾਲ ਜਾਰੀ ਰੱਖੋ

---

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਅਸਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।