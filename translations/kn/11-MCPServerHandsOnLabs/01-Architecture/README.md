<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d72a1d9e9ad1a7cc8d40d05d546b5ca0",
  "translation_date": "2025-12-11T14:00:35+00:00",
  "source_file": "11-MCPServerHandsOnLabs/01-Architecture/README.md",
  "language_code": "kn"
}
-->
# ಕೋರ್ ವಾಸ್ತುಶಿಲ್ಪ ಸಂಪ್ರದಾಯಗಳು

## 🎯 ಈ ಪ್ರಯೋಗಶಾಲೆ ಏನು ಒಳಗೊಂಡಿದೆ

ಈ ಪ್ರಯೋಗಶಾಲೆ MCP ಸರ್ವರ್ ವಾಸ್ತುಶಿಲ್ಪ ಮಾದರಿಗಳು, ಡೇಟಾಬೇಸ್ ವಿನ್ಯಾಸ ತತ್ವಗಳು ಮತ್ತು ಬಲವಾದ, ವಿಸ್ತಾರಗೊಳ್ಳುವ ಡೇಟಾಬೇಸ್-ಸಂಯೋಜಿತ AI ಅನ್ವಯಿಕೆಗಳನ್ನು ಚಾಲನೆ ಮಾಡುವ ತಾಂತ್ರಿಕ ಅನುಷ್ಠಾನ ತಂತ್ರಗಳನ್ನು ಆಳವಾಗಿ ಅನ್ವೇಷಿಸುತ್ತದೆ.

## ಅವಲೋಕನ

ಡೇಟಾಬೇಸ್ ಸಂಯೋಜನೆಯೊಂದಿಗೆ ಉತ್ಪಾದನೆಗೆ ಸಿದ್ಧ MCP ಸರ್ವರ್ ನಿರ್ಮಾಣವು ಜಾಗರೂಕ ವಾಸ್ತುಶಿಲ್ಪ ನಿರ್ಧಾರಗಳನ್ನು ಅಗತ್ಯವಿರುತ್ತದೆ. ಈ ಪ್ರಯೋಗಶಾಲೆ ನಮ್ಮ Zava Retail ವಿಶ್ಲೇಷಣಾ ಪರಿಹಾರವನ್ನು ಬಲವಾದ, ಸುರಕ್ಷಿತ ಮತ್ತು ವಿಸ್ತಾರಗೊಳ್ಳುವಂತೆ ಮಾಡುವ ಪ್ರಮುಖ ಘಟಕಗಳು, ವಿನ್ಯಾಸ ಮಾದರಿಗಳು ಮತ್ತು ತಾಂತ್ರಿಕ ಪರಿಗಣನೆಗಳನ್ನು ವಿಭಜಿಸುತ್ತದೆ.

ನೀವು ಪ್ರತಿ ಪದರವು ಹೇಗೆ ಸಂವಹನ ಮಾಡುತ್ತದೆ, ಯಾವ ತಂತ್ರಜ್ಞಾನಗಳನ್ನು ಆಯ್ಕೆಮಾಡಲಾಗಿದೆ ಮತ್ತು ಈ ಮಾದರಿಗಳನ್ನು ನಿಮ್ಮ ಸ್ವಂತ MCP ಅನುಷ್ಠಾನಗಳಿಗೆ ಹೇಗೆ ಅನ್ವಯಿಸಬಹುದು ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುತ್ತೀರಿ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪ್ರಯೋಗಶಾಲೆಯ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- **ವಿಶ್ಲೇಷಣೆ** ಮಾಡುವುದು ಡೇಟಾಬೇಸ್ ಸಂಯೋಜನೆಯೊಂದಿಗೆ MCP ಸರ್ವರ್‌ನ ಪದರಿತ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು  
- **ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು** ಪ್ರತಿ ವಾಸ್ತುಶಿಲ್ಪ ಘಟಕದ ಪಾತ್ರ ಮತ್ತು ಜವಾಬ್ದಾರಿಗಳನ್ನು  
- **ವಿನ್ಯಾಸ** ಮಾಡುವುದು ಬಹು-ಭಾಡಿಗೆ MCP ಅನ್ವಯಿಕೆಗಳನ್ನು ಬೆಂಬಲಿಸುವ ಡೇಟಾಬೇಸ್ ಸ್ಕೀಮಾಗಳನ್ನು  
- **ಅನುಷ್ಠಾನ** ಮಾಡುವುದು ಸಂಪರ್ಕ ಪೂಲಿಂಗ್ ಮತ್ತು ಸಂಪನ್ಮೂಲ ನಿರ್ವಹಣಾ ತಂತ್ರಗಳನ್ನು  
- **ಅನ್ವಯಿಸು** ದೋಷ ನಿರ್ವಹಣೆ ಮತ್ತು ಲಾಗಿಂಗ್ ಮಾದರಿಗಳನ್ನು ಉತ್ಪಾದನಾ ವ್ಯವಸ್ಥೆಗಳಿಗೆ  
- **ಮೌಲ್ಯಮಾಪನ** ಮಾಡುವುದು ವಿಭಿನ್ನ ವಾಸ್ತುಶಿಲ್ಪ ವಿಧಾನಗಳ ನಡುವಿನ ವ್ಯವಹಾರಗಳನ್ನು  

## 🏗️ MCP ಸರ್ವರ್ ವಾಸ್ತುಶಿಲ್ಪ ಪದರಗಳು

ನಮ್ಮ MCP ಸರ್ವರ್ **ಪದರಿತ ವಾಸ್ತುಶಿಲ್ಪ** ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುತ್ತದೆ, ಇದು ಚಿಂತನೆಗಳನ್ನು ವಿಭಜಿಸಿ ನಿರ್ವಹಣೀಯತೆಯನ್ನು ಉತ್ತೇಜಿಸುತ್ತದೆ:

### ಪದರ 1: ಪ್ರೋಟೋಕಾಲ್ ಪದರ (FastMCP)
**ಜವಾಬ್ದಾರಿ**: MCP ಪ್ರೋಟೋಕಾಲ್ ಸಂವಹನ ಮತ್ತು ಸಂದೇಶ ಮಾರ್ಗದರ್ಶನವನ್ನು ನಿರ್ವಹಿಸುವುದು

```python
# ಫಾಸ್ಟ್‌ಎಂಸಿಪಿ ಸರ್ವರ್ ಸೆಟ್‌ಅಪ್
from fastmcp import FastMCP

mcp = FastMCP("Zava Retail Analytics")

# ಪ್ರಕಾರ ಸುರಕ್ಷತೆ ಜೊತೆಗೆ ಸಾಧನ ನೋಂದಣಿ
@mcp.tool()
async def execute_sales_query(
    ctx: Context,
    postgresql_query: Annotated[str, Field(description="Well-formed PostgreSQL query")]
) -> str:
    """Execute PostgreSQL queries with Row Level Security."""
    return await query_executor.execute(postgresql_query, ctx)
```

**ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯಗಳು**:
- **ಪ್ರೋಟೋಕಾಲ್ ಅನುಕೂಲತೆ**: ಸಂಪೂರ್ಣ MCP ನಿರ್ದಿಷ್ಟತೆ ಬೆಂಬಲ
- **ಪ್ರಕಾರ ಸುರಕ್ಷತೆ**: ವಿನಂತಿ/ಪ್ರತಿಕ್ರಿಯೆ ಮಾನ್ಯತೆಗಾಗಿ Pydantic ಮಾದರಿಗಳು
- **ಅಸಿಂಕ್ರೋನಸ್ ಬೆಂಬಲ**: ಹೆಚ್ಚಿನ ಸಮಕಾಲೀನತೆಗೆ ಅಡ್ಡಿಪಡಿಸದ I/O
- **ದೋಷ ನಿರ್ವಹಣೆ**: ಮಾನಕೃತ ದೋಷ ಪ್ರತಿಕ್ರಿಯೆಗಳು

### ಪದರ 2: ವ್ಯವಹಾರ ತರ್ಕ ಪದರ
**ಜವಾಬ್ದಾರಿ**: ವ್ಯವಹಾರ ನಿಯಮಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು ಮತ್ತು ಪ್ರೋಟೋಕಾಲ್ ಮತ್ತು ಡೇಟಾ ಪದರಗಳ ನಡುವೆ ಸಂಯೋಜನೆ

```python
class SalesAnalyticsService:
    """Business logic for retail analytics operations."""
    
    async def get_store_performance(
        self, 
        store_id: str, 
        time_period: str
    ) -> Dict[str, Any]:
        """Calculate store performance metrics."""
        
        # ವ್ಯವಹಾರ ನಿಯಮಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
        if not self._validate_store_access(store_id):
            raise UnauthorizedError("Access denied for store")
        
        # ಡೇಟಾ ಪಡೆಯುವಿಕೆಯನ್ನು ಸಂಯೋಜಿಸಿ
        sales_data = await self.db_provider.get_sales_data(store_id, time_period)
        metrics = self._calculate_metrics(sales_data)
        
        return {
            "store_id": store_id,
            "period": time_period,
            "metrics": metrics,
            "insights": self._generate_insights(metrics)
        }
```

**ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯಗಳು**:
- **ವ್ಯವಹಾರ ನಿಯಮ ಜಾರಿಗೆ**: ಅಂಗಡಿ ಪ್ರವೇಶ ಮಾನ್ಯತೆ ಮತ್ತು ಡೇಟಾ ಅಖಂಡತೆ
- **ಸೇವಾ ಸಂಯೋಜನೆ**: ಡೇಟಾಬೇಸ್ ಮತ್ತು AI ಸೇವೆಗಳ ನಡುವೆ ಸಂಯೋಜನೆ
- **ಡೇಟಾ ಪರಿವರ್ತನೆ**: ಕಚ್ಚಾ ಡೇಟಾವನ್ನು ವ್ಯವಹಾರ ಒಳನೋಟಗಳಿಗೆ ಪರಿವರ್ತಿಸುವುದು
- **ಕ್ಯಾಶಿಂಗ್ ತಂತ್ರ**: ನಿಯಮಿತ ಪ್ರಶ್ನೆಗಳಿಗೆ ಕಾರ್ಯಕ್ಷಮತೆ ಸುಧಾರಣೆ

### ಪದರ 3: ಡೇಟಾ ಪ್ರವೇಶ ಪದರ
**ಜವಾಬ್ದಾರಿ**: ಡೇಟಾಬೇಸ್ ಸಂಪರ್ಕಗಳು, ಪ್ರಶ್ನೆ ನಿರ್ವಹಣೆ ಮತ್ತು ಡೇಟಾ ನಕ್ಷೆಗೊಳಿಸುವಿಕೆ

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
            # RLS ಸಂದರ್ಭವನ್ನು ಹೊಂದಿಸಿ
            await conn.execute(
                "SELECT set_config('app.current_rls_user_id', $1, false)",
                rls_user_id
            )
            
            # ಸಮಯ ಮಿತಿ ಸಹಿತ ಪ್ರಶ್ನೆಯನ್ನು ನಿರ್ವಹಿಸಿ
            try:
                rows = await asyncio.wait_for(
                    conn.fetch(query),
                    timeout=30.0
                )
                return [dict(row) for row in rows]
            except asyncio.TimeoutError:
                raise QueryTimeoutError("Query execution exceeded timeout")
```

**ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯಗಳು**:
- **ಸಂಪರ್ಕ ಪೂಲಿಂಗ್**: ಪರಿಣಾಮಕಾರಿ ಸಂಪನ್ಮೂಲ ನಿರ್ವಹಣೆ
- **ವಹಿವಾಟು ನಿರ್ವಹಣೆ**: ACID ಅನುಕೂಲತೆ ಮತ್ತು ರೋಲ್‌ಬ್ಯಾಕ್ ನಿರ್ವಹಣೆ
- **ಪ್ರಶ್ನೆ ಸುಧಾರಣೆ**: ಕಾರ್ಯಕ್ಷಮತೆ ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ಸುಧಾರಣೆ
- **RLS ಸಂಯೋಜನೆ**: ಸಾಲಿನ ಮಟ್ಟದ ಭದ್ರತಾ ಸನ್ನಿವೇಶ ನಿರ್ವಹಣೆ

### ಪದರ 4: ಮೂಲಸೌಕರ್ಯ ಪದರ
**ಜವಾಬ್ದಾರಿ**: ಲಾಗಿಂಗ್, ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ಸಂರಚನೆ ಮುಂತಾದ ಅಡ್ಡಕಟು ಚಿಂತನೆಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು

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

## 🗄️ ಡೇಟಾಬೇಸ್ ವಿನ್ಯಾಸ ಮಾದರಿಗಳು

ನಮ್ಮ PostgreSQL ಸ್ಕೀಮಾ ಬಹು-ಭಾಡಿಗೆ MCP ಅನ್ವಯಿಕೆಗಳಿಗೆ ಹಲವಾರು ಪ್ರಮುಖ ಮಾದರಿಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುತ್ತದೆ:

### 1. ಬಹು-ಭಾಡಿಗೆ ಸ್ಕೀಮಾ ವಿನ್ಯಾಸ

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

**ವಿನ್ಯಾಸ ತತ್ವಗಳು**:
- **ವಿದೇಶಿ ಕೀ ಸಮ್ಮತತೆ**: ಟೇಬಲ್‌ಗಳ ನಡುವೆ ಡೇಟಾ ಅಖಂಡತೆ ಖಚಿತಪಡಿಸುವುದು
- **ಅಂಗಡಿ ID ಪ್ರಸರಣ**: ಪ್ರತಿ ವಹಿವಾಟು ಟೇಬಲ್‌ನಲ್ಲಿ store_id ಸೇರಿಸುವುದು
- **UUID ಪ್ರಾಥಮಿಕ ಕೀಗಳು**: ವಿತರಣಾ ವ್ಯವಸ್ಥೆಗಳಿಗೆ ಜಾಗತಿಕವಾಗಿ ವಿಶಿಷ್ಟ ಗುರುತಿನ ಸಂಖ್ಯೆ
- **ಟೈಮ್‌ಸ್ಟ್ಯಾಂಪ್ ಟ್ರ್ಯಾಕಿಂಗ್**: ಎಲ್ಲಾ ಡೇಟಾ ಬದಲಾವಣೆಗಳಿಗಾಗಿ ಆಡಿಟ್ ಟ್ರೇಲ್

### 2. ಸಾಲಿನ ಮಟ್ಟದ ಭದ್ರತಾ ಅನುಷ್ಠಾನ

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

**RLS ಪ್ರಯೋಜನಗಳು**:
- **ಸ್ವಯಂಚಾಲಿತ ಫಿಲ್ಟರಿಂಗ್**: ಡೇಟಾಬೇಸ್ ಡೇಟಾ ವಿಭಜನೆ ಜಾರಿಗೆ
- **ಅನ್ವಯಿಕೆ ಸರಳತೆ**: ಸಂಕೀರ್ಣ WHERE ವಾಕ್ಯರಚನೆಗಳ ಅಗತ್ಯವಿಲ್ಲ
- **ಡೀಫಾಲ್ಟ್ ಭದ್ರತೆ**: ತಪ್ಪಾಗಿ ತಪ್ಪು ಡೇಟಾ ಪ್ರವೇಶಿಸುವುದು ಅಸಾಧ್ಯ
- **ಆಡಿಟ್ ಅನುಕೂಲತೆ**: ಸ್ಪಷ್ಟ ಡೇಟಾ ಪ್ರವೇಶ ಗಡಿಗಳು

### 3. ವೆಕ್ಟರ್ ಹುಡುಕಾಟ ಸ್ಕೀಮಾ

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

## 🔌 ಸಂಪರ್ಕ ನಿರ್ವಹಣಾ ಮಾದರಿಗಳು

ಕಾರ್ಯಕ್ಷಮ MCP ಸರ್ವರ್ ಕಾರ್ಯಕ್ಷಮತೆಗೆ ಪರಿಣಾಮಕಾರಿ ಡೇಟಾಬೇಸ್ ಸಂಪರ್ಕ ನಿರ್ವಹಣೆ ಅತ್ಯಂತ ಮುಖ್ಯ:

### ಸಂಪರ್ಕ ಪೂಲ್ ಸಂರಚನೆ

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
            
            # ಪೂಲ್ ಸಂರಚನೆ
            min_size=2,          # ಕನಿಷ್ಠ ಸಂಪರ್ಕಗಳು
            max_size=10,         # ಗರಿಷ್ಠ ಸಂಪರ್ಕಗಳು
            max_inactive_connection_lifetime=300,  # 5 ನಿಮಿಷಗಳು
            
            # ಪ್ರಶ್ನೆ ಸಂರಚನೆ
            command_timeout=30,   # ಪ್ರಶ್ನೆ ಸಮಯ ಮಿತಿ
            server_settings={
                "application_name": "zava-mcp-server",
                "jit": "off",          # ಸ್ಥಿರತೆಯಿಗಾಗಿ JIT ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಿ
                "work_mem": "4MB",     # ಕೆಲಸದ ಮೆಮೊರಿಯನ್ನು ಮಿತಿಗೊಳಿಸಿ
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
                
                # ಘಾತಾಂಕ ಹಿಂಪಡೆಯುವಿಕೆ
                await asyncio.sleep(2 ** attempt)
                logger.warning(f"Database connection failed, retrying ({attempt + 1}/{max_retries})")
```

### ಸಂಪನ್ಮೂಲ ಜೀವನಚಕ್ರ ನಿರ್ವಹಣೆ

```python
class MCPServerManager:
    """Manages MCP server lifecycle and resources."""
    
    async def startup(self):
        """Initialize server resources."""
        # ಡೇಟಾಬೇಸ್ ಸಂಪರ್ಕ ಪೂಲ್ ರಚಿಸಿ
        self.db_pool = await self.pool_manager.create_pool()
        
        # AI ಸೇವೆಗಳನ್ನು ಪ್ರಾರಂಭಿಸಿ
        self.ai_client = await self.create_ai_client()
        
        # ಮಾನಿಟರಿಂಗ್ ಸೆಟ್ ಅಪ್ ಮಾಡಿ
        self.metrics_collector = MetricsCollector()
        
        logger.info("MCP server startup complete")
    
    async def shutdown(self):
        """Cleanup server resources."""
        try:
            # ಡೇಟಾಬೇಸ್ ಸಂಪರ್ಕಗಳನ್ನು ಮುಚ್ಚಿ
            if self.db_pool:
                await self.db_pool.close()
            
            # AI ಕ್ಲೈಂಟ್ ಅನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ
            if self.ai_client:
                await self.ai_client.close()
            
            # ಮೆಟ್ರಿಕ್ಸ್ ಅನ್ನು ಫ್ಲಷ್ ಮಾಡಿ
            await self.metrics_collector.flush()
            
            logger.info("MCP server shutdown complete")
            
        except Exception as e:
            logger.error(f"Error during shutdown: {e}")
    
    async def health_check(self) -> Dict[str, str]:
        """Verify server health status."""
        status = {}
        
        # ಡೇಟಾಬೇಸ್ ಸಂಪರ್ಕವನ್ನು ಪರಿಶೀಲಿಸಿ
        try:
            async with self.db_pool.acquire() as conn:
                await conn.fetchval("SELECT 1")
            status["database"] = "healthy"
        except Exception as e:
            status["database"] = f"unhealthy: {e}"
        
        # AI ಸೇವೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
        try:
            await self.ai_client.health_check()
            status["ai_service"] = "healthy"
        except Exception as e:
            status["ai_service"] = f"unhealthy: {e}"
        
        return status
```

## 🛡️ ದೋಷ ನಿರ್ವಹಣೆ ಮತ್ತು ಸ್ಥೈರ್ಯತೆ ಮಾದರಿಗಳು

ಬಲವಾದ ದೋಷ ನಿರ್ವಹಣೆ ವಿಶ್ವಾಸಾರ್ಹ MCP ಸರ್ವರ್ ಕಾರ್ಯಾಚರಣೆಯನ್ನು ಖಚಿತಪಡಿಸುತ್ತದೆ:

### ಹಿರಾರ್ಕಿಕಲ್ ದೋಷ ಪ್ರಕಾರಗಳು

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

### ದೋಷ ನಿರ್ವಹಣೆ ಮಧ್ಯವರ್ತಿ

```python
@contextmanager
async def error_handling_context(operation_name: str, user_id: str = None):
    """Centralized error handling for operations."""
    start_time = time.time()
    
    try:
        yield
        
        # ಯಶಸ್ಸಿನ ಅಳತೆಗಳು
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

## 📊 ಕಾರ್ಯಕ್ಷಮತೆ ಸುಧಾರಣಾ ತಂತ್ರಗಳು

### ಪ್ರಶ್ನೆ ಕಾರ್ಯಕ್ಷಮತೆ ಮೇಲ್ವಿಚಾರಣೆ

```python
class QueryPerformanceMonitor:
    """Monitor and optimize query performance."""
    
    def __init__(self):
        self.slow_query_threshold = 1.0  # ಸೆಕೆಂಡುಗಳು
        self.query_stats = defaultdict(list)
    
    @contextmanager
    async def monitor_query(self, query: str, operation_type: str = "unknown"):
        """Monitor query execution time and performance."""
        start_time = time.time()
        query_hash = hashlib.md5(query.encode()).hexdigest()[:8]
        
        try:
            yield
            
            duration = time.time() - start_time
            
            # ಕಾರ್ಯಕ್ಷಮತೆ ಅಳತೆಗಳನ್ನು ದಾಖಲಿಸಿ
            self.query_stats[operation_type].append(duration)
            
            # ನಿಧಾನವಾದ ಪ್ರಶ್ನೆಗಳನ್ನು ಲಾಗ್ ಮಾಡಿ
            if duration > self.slow_query_threshold:
                logger.warning(f"Slow query detected", extra={
                    "query_hash": query_hash,
                    "duration": duration,
                    "operation_type": operation_type,
                    "query": query[:200]
                })
            
            # ಅಳತೆಗಳನ್ನು ನವೀಕರಿಸಿ
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

### ಕ್ಯಾಶಿಂಗ್ ತಂತ್ರ

```python
class QueryCache:
    """Intelligent query result caching."""
    
    def __init__(self, redis_url: str = None):
        self.cache = {}  # ಮೆಮೊರಿಯಲ್ಲಿ ಬ್ಯಾಕ್ಅಪ್
        self.redis_client = redis.Redis.from_url(redis_url) if redis_url else None
        self.cache_ttl = 300  # 5 ನಿಮಿಷಗಳು ಡೀಫಾಲ್ಟ್
    
    async def get_cached_result(
        self, 
        cache_key: str, 
        query_func: Callable,
        ttl: int = None
    ) -> Any:
        """Get result from cache or execute query."""
        ttl = ttl or self.cache_ttl
        
        # ಮೊದಲು ಕ್ಯಾಶೆ ಪ್ರಯತ್ನಿಸಿ
        cached_result = await self._get_from_cache(cache_key)
        if cached_result is not None:
            metrics.cache_hit.labels(type="query").inc()
            return cached_result
        
        # ಪ್ರಶ್ನೆಯನ್ನು ನಿರ್ವಹಿಸಿ
        metrics.cache_miss.labels(type="query").inc()
        result = await query_func()
        
        # ಫಲಿತಾಂಶವನ್ನು ಕ್ಯಾಶೆ ಮಾಡಿ
        await self._set_in_cache(cache_key, result, ttl)
        
        return result
    
    def _generate_cache_key(self, query: str, user_context: str) -> str:
        """Generate consistent cache key."""
        key_data = f"{query}:{user_context}"
        return hashlib.sha256(key_data.encode()).hexdigest()
```

## 🎯 ಪ್ರಮುಖ ಪಾಠಗಳು

ಈ ಪ್ರಯೋಗಶಾಲೆಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಬೇಕು:

✅ **ಪದರಿತ ವಾಸ್ತುಶಿಲ್ಪ**: MCP ಸರ್ವರ್ ವಿನ್ಯಾಸದಲ್ಲಿ ಚಿಂತನೆಗಳನ್ನು ವಿಭಜಿಸುವುದು  
✅ **ಡೇಟಾಬೇಸ್ ಮಾದರಿಗಳು**: ಬಹು-ಭಾಡಿಗೆ ಸ್ಕೀಮಾ ವಿನ್ಯಾಸ ಮತ್ತು RLS ಅನುಷ್ಠಾನ  
✅ **ಸಂಪರ್ಕ ನಿರ್ವಹಣೆ**: ಪರಿಣಾಮಕಾರಿ ಪೂಲಿಂಗ್ ಮತ್ತು ಸಂಪನ್ಮೂಲ ಜೀವನಚಕ್ರ  
✅ **ದೋಷ ನಿರ್ವಹಣೆ**: ಹಿರಾರ್ಕಿಕಲ್ ದೋಷ ಪ್ರಕಾರಗಳು ಮತ್ತು ಸ್ಥೈರ್ಯತೆ ಮಾದರಿಗಳು  
✅ **ಕಾರ್ಯಕ್ಷಮತೆ ಸುಧಾರಣೆ**: ಮೇಲ್ವಿಚಾರಣೆ, ಕ್ಯಾಶಿಂಗ್ ಮತ್ತು ಪ್ರಶ್ನೆ ಸುಧಾರಣೆ  
✅ **ಉತ್ಪಾದನಾ ಸಿದ್ಧತೆ**: ಮೂಲಸೌಕರ್ಯ ಚಿಂತನೆಗಳು ಮತ್ತು ಕಾರ್ಯಾಚರಣೆ ಮಾದರಿಗಳು  

## 🚀 ಮುಂದೇನು

**[Lab 02: Security and Multi-Tenancy](../02-Security/README.md)** ಜೊತೆಗೆ ಮುಂದುವರಿದು ಆಳವಾಗಿ ತಿಳಿದುಕೊಳ್ಳಿ:

- ಸಾಲಿನ ಮಟ್ಟದ ಭದ್ರತಾ ಅನುಷ್ಠಾನ ವಿವರಗಳು  
- ಪ್ರಮಾಣೀಕರಣ ಮತ್ತು ಪ್ರಾಧಿಕಾರ ಮಾದರಿಗಳು  
- ಬಹು-ಭಾಡಿಗೆ ಡೇಟಾ ವಿಭಜನೆ ತಂತ್ರಗಳು  
- ಭದ್ರತಾ ಆಡಿಟ್ ಮತ್ತು ಅನುಕೂಲತೆ ಪರಿಗಣನೆಗಳು  

## 📚 ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

### ವಾಸ್ತುಶಿಲ್ಪ ಮಾದರಿಗಳು
- [Python ನಲ್ಲಿ ಕ್ಲೀನ್ ವಾಸ್ತುಶಿಲ್ಪ](https://github.com/cosmic-python/code) - Python ಅನ್ವಯಿಕೆಗಳ ವಾಸ್ತುಶಿಲ್ಪ ಮಾದರಿಗಳು  
- [ಡೇಟಾಬೇಸ್ ವಿನ್ಯಾಸ ಮಾದರಿಗಳು](https://en.wikipedia.org/wiki/Database_design) - ಸಂಬಂಧಿತ ಡೇಟಾಬೇಸ್ ವಿನ್ಯಾಸ ತತ್ವಗಳು  
- [ಮೈಕ್ರೋಸರ್ವಿಸಸ್ ಮಾದರಿಗಳು](https://microservices.io/patterns/) - ಸೇವಾ ವಾಸ್ತುಶಿಲ್ಪ ಮಾದರಿಗಳು  

### PostgreSQL ಉನ್ನತ ವಿಷಯಗಳು
- [PostgreSQL ಕಾರ್ಯಕ್ಷಮತೆ ಟ್ಯೂನಿಂಗ್](https://wiki.postgresql.org/wiki/Performance_Optimization) - ಡೇಟಾಬೇಸ್ ಸುಧಾರಣಾ ಮಾರ್ಗದರ್ಶಿ  
- [ಸಂಪರ್ಕ ಪೂಲಿಂಗ್ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು](https://www.postgresql.org/docs/current/runtime-config-connection.html) - ಸಂಪರ್ಕ ನಿರ್ವಹಣೆ  
- [ಪ್ರಶ್ನೆ ಯೋಜನೆ ಮತ್ತು ಸುಧಾರಣೆ](https://www.postgresql.org/docs/current/planner-optimizer.html) - ಪ್ರಶ್ನೆ ಕಾರ್ಯಕ್ಷಮತೆ  

### Python ಅಸಿಂಕ್ರೋನಸ್ ಮಾದರಿಗಳು
- [AsyncIO ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು](https://docs.python.org/3/library/asyncio.html) - ಅಸಿಂಕ್ರೋನಸ್ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಮಾದರಿಗಳು  
- [FastAPI ವಾಸ್ತುಶಿಲ್ಪ](https://fastapi.tiangolo.com/advanced/) - ಆಧುನಿಕ Python ವೆಬ್ ವಾಸ್ತುಶಿಲ್ಪ  
- [Pydantic ಮಾದರಿಗಳು](https://pydantic-docs.helpmanual.io/) - ಡೇಟಾ ಮಾನ್ಯತೆ ಮತ್ತು ಸರಣೀಕರಣ  

---

**ಮುಂದೆ**: ಭದ್ರತಾ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸಲು ಸಿದ್ಧರಾ? **[Lab 02: Security and Multi-Tenancy](../02-Security/README.md)** ಜೊತೆಗೆ ಮುಂದುವರಿಯಿರಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->