# 핵심 아키텍처 개념

## 🎯 이 실습에서 다루는 내용

이 실습은 MCP 서버 아키텍처 패턴, 데이터베이스 설계 원칙, 그리고 견고하고 확장 가능한 데이터베이스 통합 AI 애플리케이션을 구현하는 기술적 전략에 대한 심층적인 탐구를 제공합니다.

## 개요

데이터베이스 통합을 포함한 프로덕션 준비 MCP 서버를 구축하려면 신중한 아키텍처 결정이 필요합니다. 이 실습에서는 Zava Retail 분석 솔루션을 견고하고 안전하며 확장 가능하게 만드는 핵심 구성 요소, 설계 패턴, 기술적 고려 사항을 분해하여 설명합니다.

각 계층이 어떻게 상호작용하는지, 특정 기술이 왜 선택되었는지, 그리고 이러한 패턴을 자신의 MCP 구현에 어떻게 적용할 수 있는지를 이해하게 될 것입니다.

## 학습 목표

이 실습을 완료하면 다음을 수행할 수 있습니다:

- **분석**: 데이터베이스 통합 MCP 서버의 계층화된 아키텍처 분석
- **이해**: 각 아키텍처 구성 요소의 역할과 책임
- **설계**: 다중 테넌트 MCP 애플리케이션을 지원하는 데이터베이스 스키마 설계
- **구현**: 연결 풀링 및 리소스 관리 전략
- **적용**: 프로덕션 시스템을 위한 오류 처리 및 로깅 패턴
- **평가**: 다양한 아키텍처 접근 방식 간의 트레이드오프 평가

## 🏗️ MCP 서버 아키텍처 계층

우리의 MCP 서버는 **계층화된 아키텍처**를 구현하여 관심사를 분리하고 유지보수를 촉진합니다:

### 계층 1: 프로토콜 계층 (FastMCP)
**책임**: MCP 프로토콜 통신 및 메시지 라우팅 처리

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

**주요 기능**:
- **프로토콜 준수**: MCP 사양 완벽 지원
- **타입 안전성**: 요청/응답 유효성 검사를 위한 Pydantic 모델
- **비동기 지원**: 높은 동시성을 위한 비차단 I/O
- **오류 처리**: 표준화된 오류 응답

### 계층 2: 비즈니스 로직 계층
**책임**: 비즈니스 규칙 구현 및 프로토콜과 데이터 계층 간 조정

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

**주요 기능**:
- **비즈니스 규칙 준수**: 저장소 접근 검증 및 데이터 무결성
- **서비스 조정**: 데이터베이스와 AI 서비스 간 오케스트레이션
- **데이터 변환**: 원시 데이터를 비즈니스 인사이트로 변환
- **캐싱 전략**: 빈번한 쿼리에 대한 성능 최적화

### 계층 3: 데이터 접근 계층
**책임**: 데이터베이스 연결 관리, 쿼리 실행 및 데이터 매핑

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

**주요 기능**:
- **연결 풀링**: 효율적인 리소스 관리
- **트랜잭션 관리**: ACID 준수 및 롤백 처리
- **쿼리 최적화**: 성능 모니터링 및 최적화
- **RLS 통합**: 행 수준 보안 컨텍스트 관리

### 계층 4: 인프라 계층
**책임**: 로깅, 모니터링, 구성과 같은 횡단 관심사 처리

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

## 🗄️ 데이터베이스 설계 패턴

우리의 PostgreSQL 스키마는 다중 테넌트 MCP 애플리케이션을 위한 몇 가지 주요 패턴을 구현합니다:

### 1. 다중 테넌트 스키마 설계

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

**설계 원칙**:
- **외래 키 일관성**: 테이블 간 데이터 무결성 보장
- **저장소 ID 전파**: 모든 트랜잭션 테이블에 store_id 포함
- **UUID 기본 키**: 분산 시스템을 위한 전역적으로 고유한 식별자
- **타임스탬프 추적**: 모든 데이터 변경에 대한 감사 기록

### 2. 행 수준 보안 구현

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

**RLS의 이점**:
- **자동 필터링**: 데이터베이스가 데이터 격리를 강제
- **애플리케이션 단순화**: 복잡한 WHERE 절 불필요
- **기본 보안**: 잘못된 데이터 접근이 불가능
- **감사 준수**: 명확한 데이터 접근 경계

### 3. 벡터 검색 스키마

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

## 🔌 연결 관리 패턴

효율적인 데이터베이스 연결 관리는 MCP 서버 성능에 중요합니다:

### 연결 풀 구성

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

### 리소스 라이프사이클 관리

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

## 🛡️ 오류 처리 및 복원력 패턴

견고한 오류 처리는 MCP 서버의 안정적인 운영을 보장합니다:

### 계층적 오류 유형

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

### 오류 처리 미들웨어

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

## 📊 성능 최적화 전략

### 쿼리 성능 모니터링

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

### 캐싱 전략

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

## 🎯 주요 요점

이 실습을 완료한 후, 다음을 이해할 수 있어야 합니다:

✅ **계층화된 아키텍처**: MCP 서버 설계에서 관심사를 분리하는 방법  
✅ **데이터베이스 패턴**: 다중 테넌트 스키마 설계 및 RLS 구현  
✅ **연결 관리**: 효율적인 풀링 및 리소스 라이프사이클  
✅ **오류 처리**: 계층적 오류 유형 및 복원력 패턴  
✅ **성능 최적화**: 모니터링, 캐싱 및 쿼리 최적화  
✅ **프로덕션 준비**: 인프라 관심사 및 운영 패턴  

## 🚀 다음 단계

**[Lab 02: 보안 및 다중 테넌트](../02-Security/README.md)**로 계속 진행하여 다음을 심층적으로 탐구하세요:

- 행 수준 보안 구현 세부사항
- 인증 및 권한 부여 패턴
- 다중 테넌트 데이터 격리 전략
- 보안 감사 및 준수 고려 사항

## 📚 추가 자료

### 아키텍처 패턴
- [Python에서의 클린 아키텍처](https://github.com/cosmic-python/code) - Python 애플리케이션을 위한 아키텍처 패턴
- [데이터베이스 설계 패턴](https://en.wikipedia.org/wiki/Database_design) - 관계형 데이터베이스 설계 원칙
- [마이크로서비스 패턴](https://microservices.io/patterns/) - 서비스 아키텍처 패턴

### PostgreSQL 고급 주제
- [PostgreSQL 성능 튜닝](https://wiki.postgresql.org/wiki/Performance_Optimization) - 데이터베이스 최적화 가이드
- [연결 풀링 모범 사례](https://www.postgresql.org/docs/current/runtime-config-connection.html) - 연결 관리
- [쿼리 계획 및 최적화](https://www.postgresql.org/docs/current/planner-optimizer.html) - 쿼리 성능

### Python 비동기 패턴
- [AsyncIO 모범 사례](https://docs.python.org/3/library/asyncio.html) - 비동기 프로그래밍 패턴
- [FastAPI 아키텍처](https://fastapi.tiangolo.com/advanced/) - 현대적인 Python 웹 아키텍처
- [Pydantic 모델](https://pydantic-docs.helpmanual.io/) - 데이터 유효성 검사 및 직렬화

---

**다음**: 보안 패턴을 탐구할 준비가 되셨나요? [Lab 02: 보안 및 다중 테넌트](../02-Security/README.md)로 계속 진행하세요.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.