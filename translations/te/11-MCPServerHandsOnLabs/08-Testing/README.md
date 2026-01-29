# పరీక్ష మరియు డీబగ్గింగ్

## 🎯 ఈ ప్రయోగశాలలో ఏమి ఉంటుంది

ఈ ప్రయోగశాల ఉత్పత్తి వాతావరణాలలో MCP సర్వర్లను పరీక్షించడం మరియు డీబగ్గింగ్ చేయడం గురించి సమగ్ర మార్గదర్శకాన్ని అందిస్తుంది. మీరు బలమైన పరీక్షా వ్యూహాలను అమలు చేయడం, సంక్లిష్ట సమస్యలను డీబగ్గింగ్ చేయడం, మరియు వివిధ పరిస్థితులలో మీ MCP సర్వర్ విశ్వసనీయంగా పనిచేయడం ఎలా చేయాలో నేర్చుకుంటారు.

## అవలోకనం

MCP సర్వర్లను పరీక్షించడం అనేది యూనిట్ టెస్టులు, ఇంటిగ్రేషన్ టెస్టులు, పనితీరు ధృవీకరణ, మరియు వాస్తవ ప్రపంచ పరిస్థితుల పరీక్షలను కవర్ చేసే బహుళ-స్థాయి దృష్టికోణాన్ని అవసరం చేస్తుంది. ఈ ప్రయోగశాల అభివృద్ధి నుండి ఉత్పత్తి మానిటరింగ్ వరకు పూర్తి పరీక్షా జీవనచక్రాన్ని కవర్ చేస్తుంది.

మా పరీక్షా వ్యూహం విశ్వసనీయత, భద్రత, మరియు పనితీరు పై దృష్టి సారిస్తుంది, మీ MCP సర్వర్ ఉత్పత్తి లోడ్లను నిర్వహించగలుగుతూ డేటా సమగ్రత మరియు వినియోగదారు అనుభవ నాణ్యతను కాపాడుతుంది.

## నేర్చుకునే లక్ష్యాలు

ఈ ప్రయోగశాల ముగిసిన తర్వాత, మీరు చేయగలుగుతారు:

- **సంపూర్ణ యూనిట్ మరియు ఇంటిగ్రేషన్ టెస్ట్ సూట్లను అమలు చేయడం**  
- **MCP టూల్స్ మరియు డేటాబేస్ ఆపరేషన్ల కోసం సమర్థవంతమైన పరీక్షా వ్యూహాలను రూపకల్పన చేయడం**  
- **అధునాతన డీబగ్గింగ్ సాంకేతికతలను ఉపయోగించి సంక్లిష్ట సమస్యలను డీబగ్గింగ్ చేయడం**  
- **నిజమైన పరీక్షా పరిస్థితులతో లోడ్ క్రింద పనితీరును ధృవీకరించడం**  
- **ప్రొడక్షన్ సిస్టమ్స్‌ను సమర్థవంతమైన అలర్టింగ్ మరియు పరిశీలనతో మానిటర్ చేయడం**  
- **సతత ఇంటిగ్రేషన్ కోసం పరీక్షా వర్క్‌ఫ్లోలను ఆటోమేట్ చేయడం**

## 🧪 పరీక్షా నిర్మాణం

### పరీక్షా వ్యూహం అవలోకనం

```
┌─────────────────────────────────────────────────┐
│                Unit Tests                       │
│   • Tool execution logic                       │
│   • Database query validation                  │
│   • Authentication/authorization               │
│   • Embedding generation                       │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│             Integration Tests                   │
│   • End-to-end MCP workflows                  │
│   • Database schema validation                 │
│   • API endpoint testing                       │
│   • Multi-tool interactions                    │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│            Performance Tests                    │
│   • Load testing under realistic conditions    │
│   • Database performance validation            │
│   • Memory and resource usage                  │
│   • Embedding generation performance           │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│              E2E Tests                         │
│   • Complete user workflows                    │
│   • VS Code integration testing               │
│   • Real-world scenario validation            │
│   • Cross-browser compatibility               │
└─────────────────────────────────────────────────┘
```

### పరీక్షా వాతావరణం సెటప్

```python
# tests/conftest.py
"""
Pytest configuration and shared fixtures for MCP server testing.
"""
import pytest
import asyncio
import asyncpg
import os
from typing import AsyncGenerator, Dict, Any
from unittest.mock import AsyncMock, Mock
import tempfile
import shutil
from datetime import datetime

# పరీక్షా కాన్ఫిగరేషన్
TEST_DATABASE_URL = "postgresql://test_user:test_pass@localhost:5432/test_retail_db"
TEST_STORE_IDS = ['test_seattle', 'test_redmond', 'test_bellevue']

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def test_database():
    """Set up test database with schema and sample data."""
    
    # పరీక్షా డేటాబేస్ కనెక్షన్ సృష్టించండి
    sys_conn = await asyncpg.connect(
        "postgresql://postgres:password@localhost:5432/postgres"
    )
    
    try:
        # పరీక్షా డేటాబేస్ సృష్టించండి
        await sys_conn.execute("DROP DATABASE IF EXISTS test_retail_db")
        await sys_conn.execute("CREATE DATABASE test_retail_db")
    finally:
        await sys_conn.close()
    
    # పరీక్షా డేటాబేస్‌కు కనెక్ట్ అయి స్కీమాను సెట్ చేయండి
    test_conn = await asyncpg.connect(TEST_DATABASE_URL)
    
    try:
        # స్కీమాను లోడ్ చేయండి
        schema_sql = await load_sql_file("../scripts/create_schema.sql")
        await test_conn.execute(schema_sql)
        
        # నమూనా డేటాను లోడ్ చేయండి
        sample_data_sql = await load_sql_file("../scripts/sample_data.sql")
        await test_conn.execute(sample_data_sql)
        
        yield test_conn
        
    finally:
        await test_conn.close()
        
        # పరీక్షా డేటాబేస్‌ను శుభ్రపరచండి
        sys_conn = await asyncpg.connect(
            "postgresql://postgres:password@localhost:5432/postgres"
        )
        try:
            await sys_conn.execute("DROP DATABASE IF EXISTS test_retail_db")
        finally:
            await sys_conn.close()

@pytest.fixture
async def db_connection(test_database):
    """Provide a clean database connection for each test."""
    
    conn = await asyncpg.connect(TEST_DATABASE_URL)
    
    # పరీక్షా వేరుపడుట కోసం లావాదేవీ ప్రారంభించండి
    tx = conn.transaction()
    await tx.start()
    
    try:
        yield conn
    finally:
        # పరీక్షా వేరుపడుటను నిలుపుకోవడానికి లావాదేవీని రోల్‌బ్యాక్ చేయండి
        await tx.rollback()
        await conn.close()

@pytest.fixture
async def mock_embedding_manager():
    """Mock embedding manager for testing without Azure OpenAI calls."""
    
    mock_manager = AsyncMock()
    
    # ఎంబెడ్డింగ్ ఉత్పత్తిని మాక్ చేయండి
    mock_manager.generate_embedding.return_value = [0.1] * 1536  # ఎంబెడ్డింగ్‌ను మాక్ చేయండి
    mock_manager.generate_embeddings_batch.return_value = [[0.1] * 1536] * 10
    
    # ప్రారంభీకరణను మాక్ చేయండి
    mock_manager.initialize.return_value = None
    mock_manager.cleanup.return_value = None
    
    return mock_manager

@pytest.fixture
async def test_mcp_server(db_connection, mock_embedding_manager):
    """Set up test MCP server instance."""
    
    from mcp_server.server import MCPServer
    from mcp_server.database import DatabaseProvider
    from mcp_server.config import Config
    
    # పరీక్షా కాన్ఫిగరేషన్ సృష్టించండి
    config = Config()
    config.database.connection_string = TEST_DATABASE_URL
    config.server.enable_debug = True
    
    # డేటాబేస్ ప్రొవైడర్ సృష్టించండి
    db_provider = DatabaseProvider(config.database.connection_string)
    await db_provider.initialize()
    
    # MCP సర్వర్ సృష్టించండి
    server = MCPServer(config, db_provider)
    server.embedding_manager = mock_embedding_manager
    
    await server.initialize()
    
    yield server
    
    await server.cleanup()

@pytest.fixture
def sample_products():
    """Sample product data for testing."""
    
    return [
        {
            'product_id': 'test-product-1',
            'product_name': 'Test Running Shoes',
            'brand': 'TestBrand',
            'price': 99.99,
            'product_description': 'Comfortable running shoes for daily training',
            'category_name': 'Electronics',
            'current_stock': 50
        },
        {
            'product_id': 'test-product-2',
            'product_name': 'Test Laptop',
            'brand': 'TestTech',
            'price': 1299.99,
            'product_description': 'High-performance laptop for professional use',
            'category_name': 'Electronics',
            'current_stock': 25
        }
    ]

async def load_sql_file(file_path: str) -> str:
    """Load SQL file content."""
    
    with open(file_path, 'r') as file:
        return file.read()

# పరీక్షా డేటా సహాయకులు
class TestDataHelper:
    """Helper class for managing test data."""
    
    @staticmethod
    async def create_test_store(conn: asyncpg.Connection, store_id: str) -> Dict[str, Any]:
        """Create a test store."""
        
        store_data = {
            'store_id': store_id,
            'store_name': f'Test Store {store_id}',
            'store_location': 'Test Location',
            'store_type': 'test',
            'region': 'test'
        }
        
        await conn.execute("""
            INSERT INTO retail.stores (store_id, store_name, store_location, store_type, region)
            VALUES ($1, $2, $3, $4, $5)
            ON CONFLICT (store_id) DO NOTHING
        """, *store_data.values())
        
        return store_data
    
    @staticmethod
    async def create_test_customer(conn: asyncpg.Connection, store_id: str) -> str:
        """Create a test customer."""
        
        customer_id = await conn.fetchval("""
            INSERT INTO retail.customers (
                store_id, first_name, last_name, email, loyalty_tier
            ) VALUES ($1, $2, $3, $4, $5)
            RETURNING customer_id
        """, store_id, 'Test', 'Customer', 'test@example.com', 'bronze')
        
        return customer_id
    
    @staticmethod
    async def create_test_product(
        conn: asyncpg.Connection, 
        store_id: str, 
        product_data: Dict[str, Any]
    ) -> str:
        """Create a test product."""
        
        product_id = await conn.fetchval("""
            INSERT INTO retail.products (
                store_id, sku, product_name, brand, price, product_description, current_stock
            ) VALUES ($1, $2, $3, $4, $5, $6, $7)
            RETURNING product_id
        """, 
            store_id, 
            f"TEST-{product_data['product_name'][:10]}",
            product_data['product_name'],
            product_data['brand'],
            product_data['price'],
            product_data['product_description'],
            product_data['current_stock']
        )
        
        return product_id
```

## 🔧 యూనిట్ పరీక్ష

### టూల్ పరీక్షా ఫ్రేమ్‌వర్క్

```python
# tests/test_tools.py
"""
Comprehensive unit tests for MCP tools.
"""
import pytest
import asyncio
from unittest.mock import AsyncMock, patch
from datetime import datetime, timedelta

from mcp_server.tools.sales_analysis import SalesAnalysisTool
from mcp_server.tools.semantic_search import SemanticProductSearchTool
from mcp_server.tools.schema_introspection import SchemaIntrospectionTool
from tests.conftest import TestDataHelper

class TestSalesAnalysisTool:
    """Test sales analysis tool functionality."""
    
    @pytest.fixture
    async def sales_tool(self, test_mcp_server):
        """Create sales analysis tool for testing."""
        return SalesAnalysisTool(test_mcp_server.db_provider)
    
    async def test_daily_sales_query(self, sales_tool, db_connection):
        """Test daily sales analysis query."""
        
        # పరీక్షా డేటాను సెట్ చేయండి
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        customer_id = await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # పరీక్షా లావాదేవీని సృష్టించండి
        await db_connection.execute("""
            INSERT INTO retail.sales_transactions (
                store_id, customer_id, transaction_date, total_amount, transaction_type
            ) VALUES ($1, $2, $3, $4, $5)
        """, store_id, customer_id, datetime.now(), 150.00, 'sale')
        
        # టూల్‌ను అమలు చేయండి
        result = await sales_tool.execute(
            query_type='daily_sales',
            store_id=store_id,
            start_date=(datetime.now() - timedelta(days=7)).date(),
            end_date=datetime.now().date()
        )
        
        # ఫలితాలను ధృవీకరించండి
        assert result.success is True
        assert len(result.data) > 0
        assert 'total_revenue' in result.data[0]
        assert result.metadata['query_type'] == 'daily_sales'
    
    async def test_custom_query_validation(self, sales_tool, db_connection):
        """Test custom query validation."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # చెల్లుబాటు అయ్యే క్వెరీని పరీక్షించండి
        valid_query = "SELECT COUNT(*) as customer_count FROM retail.customers"
        result = await sales_tool.execute(
            query_type='custom',
            store_id=store_id,
            query=valid_query
        )
        
        assert result.success is True
        
        # చెల్లుబాటు కాని క్వెరీని పరీక్షించండి (నిరోధించబడాలి)
        invalid_query = "DROP TABLE retail.customers"
        result = await sales_tool.execute(
            query_type='custom',
            store_id=store_id,
            query=invalid_query
        )
        
        assert result.success is False
        assert 'validation failed' in result.error.lower()
    
    async def test_store_isolation(self, sales_tool, db_connection):
        """Test that store isolation works correctly."""
        
        # రెండు వేర్వేరు స్టోర్లను సృష్టించండి
        store1 = 'test_store1'
        store2 = 'test_store2'
        
        await TestDataHelper.create_test_store(db_connection, store1)
        await TestDataHelper.create_test_store(db_connection, store2)
        
        # వేర్వేరు స్టోర్లలో కస్టమర్లను సృష్టించండి
        customer1 = await TestDataHelper.create_test_customer(db_connection, store1)
        customer2 = await TestDataHelper.create_test_customer(db_connection, store2)
        
        # store1 నుండి క్వెరీ చేయడం store1 డేటాను మాత్రమే చూడాలి
        result1 = await sales_tool.execute(
            query_type='custom',
            store_id=store1,
            query="SELECT COUNT(*) as count FROM retail.customers"
        )
        
        # store2 నుండి క్వెరీ చేయడం store2 డేటాను మాత్రమే చూడాలి
        result2 = await sales_tool.execute(
            query_type='custom',
            store_id=store2,
            query="SELECT COUNT(*) as count FROM retail.customers"
        )
        
        assert result1.success is True
        assert result2.success is True
        assert result1.data[0]['count'] == 1
        assert result2.data[0]['count'] == 1

class TestSemanticSearchTool:
    """Test semantic search tool functionality."""
    
    @pytest.fixture
    async def search_tool(self, test_mcp_server):
        """Create semantic search tool for testing."""
        return SemanticProductSearchTool(test_mcp_server.db_provider)
    
    async def test_semantic_search_execution(self, search_tool, db_connection, sample_products):
        """Test semantic search with mock embeddings."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # పరీక్షా ఉత్పత్తులను సృష్టించండి
        for product_data in sample_products:
            product_id = await TestDataHelper.create_test_product(
                db_connection, store_id, product_data
            )
            
            # మాక్ ఎంబెడ్డింగ్ సృష్టించండి
            await db_connection.execute("""
                INSERT INTO retail.product_embeddings (
                    product_id, store_id, embedding_text, embedding
                ) VALUES ($1, $2, $3, $4)
            """, 
                product_id, store_id, 
                f"{product_data['product_name']} {product_data['brand']}", 
                '[0.1,0.2,0.3]'  # మాక్ ఎంబెడ్డింగ్
            )
        
        # శోధనను అమలు చేయండి
        result = await search_tool.execute(
            query='running shoes',
            store_id=store_id,
            limit=10,
            similarity_threshold=0.0
        )
        
        # ఫలితాలను ధృవీకరించండి
        assert result.success is True
        assert len(result.data) > 0
        assert 'similarity_score' in result.data[0]
        assert result.metadata['search_type'] == 'semantic'
    
    async def test_search_parameter_validation(self, search_tool):
        """Test search parameter validation."""
        
        # మిస్సింగ్ క్వెరీని పరీక్షించండి
        result = await search_tool.execute(store_id='test_store')
        assert result.success is False
        assert 'query is required' in result.error.lower()
        
        # మిస్సింగ్ store_idని పరీక్షించండి
        result = await search_tool.execute(query='test query')
        assert result.success is False
        assert 'store_id is required' in result.error.lower()

class TestSchemaIntrospectionTool:
    """Test schema introspection tool."""
    
    @pytest.fixture
    async def schema_tool(self, test_mcp_server):
        """Create schema introspection tool for testing."""
        return SchemaIntrospectionTool(test_mcp_server.db_provider)
    
    async def test_single_table_schema(self, schema_tool, db_connection):
        """Test getting schema for a single table."""
        
        result = await schema_tool.execute(
            table_name='customers',
            include_constraints=True,
            include_indexes=True
        )
        
        assert result.success is True
        assert result.data['table_name'] == 'customers'
        assert len(result.data['columns']) > 0
        assert 'customer_id' in [col['column_name'] for col in result.data['columns']]
    
    async def test_all_tables_schema(self, schema_tool, db_connection):
        """Test getting schema for all tables."""
        
        result = await schema_tool.execute()
        
        assert result.success is True
        assert result.data['schema_name'] == 'retail'
        assert len(result.data['tables']) > 0
        
        table_names = [table['table_name'] for table in result.data['tables']]
        expected_tables = ['customers', 'products', 'sales_transactions']
        
        for expected_table in expected_tables:
            assert expected_table in table_names
```

### డేటాబేస్ పరీక్ష

```python
# tests/test_database.py
"""
Database layer testing including RLS and security.
"""
import pytest
import asyncpg
from datetime import datetime

from mcp_server.database import DatabaseProvider
from tests.conftest import TestDataHelper

class TestRowLevelSecurity:
    """Test Row Level Security implementation."""
    
    async def test_store_context_setting(self, db_connection):
        """Test that store context is set correctly."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # స్టోర్ సందర్భాన్ని సెట్ చేయండి
        await db_connection.execute("SELECT retail.set_store_context($1)", store_id)
        
        # సందర్భం సెట్ అయినదని నిర్ధారించండి
        current_store = await db_connection.fetchval(
            "SELECT current_setting('app.current_store_id', true)"
        )
        
        assert current_store == store_id
    
    async def test_customer_isolation(self, db_connection):
        """Test that customers are properly isolated by store."""
        
        # రెండు స్టోర్లను సృష్టించండి
        store1 = 'test_store1'
        store2 = 'test_store2'
        
        await TestDataHelper.create_test_store(db_connection, store1)
        await TestDataHelper.create_test_store(db_connection, store2)
        
        # వేర్వేరు స్టోర్లలో కస్టమర్లను సృష్టించండి
        await TestDataHelper.create_test_customer(db_connection, store1)
        await TestDataHelper.create_test_customer(db_connection, store2)
        
        # సందర్భాన్ని store1 గా సెట్ చేసి కస్టమర్లను లెక్కించండి
        await db_connection.execute("SELECT retail.set_store_context($1)", store1)
        store1_count = await db_connection.fetchval("SELECT COUNT(*) FROM retail.customers")
        
        # సందర్భాన్ని store2 గా సెట్ చేసి కస్టమర్లను లెక్కించండి
        await db_connection.execute("SELECT retail.set_store_context($1)", store2)
        store2_count = await db_connection.fetchval("SELECT COUNT(*) FROM retail.customers")
        
        # ప్రతి స్టోర్ తన స్వంత కస్టమర్లను మాత్రమే చూడాలి
        assert store1_count == 1
        assert store2_count == 1
    
    async def test_invalid_store_context(self, db_connection):
        """Test that invalid store context raises error."""
        
        with pytest.raises(Exception) as exc_info:
            await db_connection.execute("SELECT retail.set_store_context($1)", 'invalid_store')
        
        assert "Store not found" in str(exc_info.value)
    
    async def test_cross_store_data_insertion_blocked(self, db_connection):
        """Test that users cannot insert data for other stores."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # స్టోర్ సందర్భాన్ని సెట్ చేయండి
        await db_connection.execute("SELECT retail.set_store_context($1)", store_id)
        
        # వేరే స్టోర్ కోసం కస్టమర్‌ను చేర్చడానికి ప్రయత్నించండి (విఫలమవుతుంది)
        with pytest.raises(Exception):
            await db_connection.execute("""
                INSERT INTO retail.customers (store_id, first_name, last_name, email)
                VALUES ($1, $2, $3, $4)
            """, 'different_store', 'Test', 'Customer', 'test@example.com')

class TestDatabaseProvider:
    """Test database provider functionality."""
    
    @pytest.fixture
    async def db_provider(self):
        """Create database provider for testing."""
        
        provider = DatabaseProvider(TEST_DATABASE_URL)
        await provider.initialize()
        yield provider
        await provider.cleanup()
    
    async def test_connection_pooling(self, db_provider):
        """Test connection pool functionality."""
        
        # బహుళ కనెక్షన్లను పొందండి
        conn1 = await db_provider.get_connection()
        conn2 = await db_provider.get_connection()
        
        assert conn1 is not None
        assert conn2 is not None
        assert conn1 != conn2  # అవి వేర్వేరు కనెక్షన్ ఆబ్జెక్టులు కావాలి
        
        # కనెక్షన్లను విడుదల చేయండి
        await db_provider.release_connection(conn1)
        await db_provider.release_connection(conn2)
    
    async def test_health_check(self, db_provider):
        """Test database health check."""
        
        health_status = await db_provider.health_check()
        
        assert health_status['status'] == 'healthy'
        assert 'connection_pool_size' in health_status
        assert 'database_version' in health_status
    
    async def test_connection_recovery(self, db_provider):
        """Test connection recovery after database issues."""
        
        # ఇది కనెక్షన్ పునరుద్ధరణ పరిస్థితులను పరీక్షిస్తుంది
        # నిజమైన పరీక్షలో, మీరు తాత్కాలికంగా కనెక్షన్‌ను విరగడచేయవచ్చు
        # మరియు పూల్ పునరుద్ధరించబడిందని నిర్ధారించండి
        
        # ఇప్పటికీ, హెల్త్ చెక్ పనిచేస్తుందో లేదో మాత్రమే నిర్ధారించండి
        health_status = await db_provider.health_check()
        assert health_status['status'] == 'healthy'
```

## 🚀 ఇంటిగ్రేషన్ పరీక్ష

### ఎండ్-టు-ఎండ్ వర్క్‌ఫ్లో పరీక్ష

```python
# tests/test_integration.py
"""
Integration tests for complete MCP workflows.
"""
import pytest
import json
from datetime import datetime, timedelta

from mcp_server.server import MCPServer
from tests.conftest import TestDataHelper

class TestMCPWorkflows:
    """Test complete MCP server workflows."""
    
    async def test_product_search_workflow(self, test_mcp_server, db_connection, sample_products):
        """Test complete product search workflow."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # ఎంబెడ్డింగ్స్‌తో టెస్ట్ ఉత్పత్తులను సృష్టించండి
        for product_data in sample_products:
            product_id = await TestDataHelper.create_test_product(
                db_connection, store_id, product_data
            )
            
            # ఉత్పత్తికి ఎంబెడ్డింగ్ సృష్టించండి
            await db_connection.execute("""
                INSERT INTO retail.product_embeddings (
                    product_id, store_id, embedding_text, embedding
                ) VALUES ($1, $2, $3, $4)
            """, 
                product_id, store_id, 
                f"{product_data['product_name']} {product_data['brand']}", 
                '[' + ','.join(['0.1'] * 1536) + ']'  # మాక్ ఎంబెడ్డింగ్
            )
        
        # సెమాంటిక్ శోధనను పరీక్షించండి
        search_result = await test_mcp_server.execute_tool(
            'semantic_search_products',
            {
                'query': 'running shoes',
                'store_id': store_id,
                'limit': 10
            }
        )
        
        assert search_result['success'] is True
        assert len(search_result['data']) > 0
        
        # స్కీమా ఇంట్రోస్పెక్షన్‌ను పరీక్షించండి
        schema_result = await test_mcp_server.execute_tool(
            'get_table_schema',
            {'table_name': 'products'}
        )
        
        assert schema_result['success'] is True
        assert schema_result['data']['table_name'] == 'products'
    
    async def test_sales_analysis_workflow(self, test_mcp_server, db_connection):
        """Test sales analysis workflow."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # టెస్ట్ కస్టమర్ మరియు ఉత్పత్తిని సృష్టించండి
        customer_id = await TestDataHelper.create_test_customer(db_connection, store_id)
        product_id = await TestDataHelper.create_test_product(
            db_connection, store_id, {
                'product_name': 'Test Product',
                'brand': 'TestBrand',
                'price': 99.99,
                'product_description': 'Test product description',
                'current_stock': 50
            }
        )
        
        # టెస్ట్ లావాదేవీని సృష్టించండి
        transaction_id = await db_connection.fetchval("""
            INSERT INTO retail.sales_transactions (
                store_id, customer_id, transaction_date, total_amount, 
                subtotal, tax_amount, transaction_type
            ) VALUES ($1, $2, $3, $4, $5, $6, $7)
            RETURNING transaction_id
        """, store_id, customer_id, datetime.now(), 107.99, 99.99, 8.00, 'sale')
        
        # లావాదేవీ అంశాన్ని సృష్టించండి
        await db_connection.execute("""
            INSERT INTO retail.sales_transaction_items (
                transaction_id, product_id, quantity, unit_price, total_price
            ) VALUES ($1, $2, $3, $4, $5)
        """, transaction_id, product_id, 1, 99.99, 99.99)
        
        # రోజువారీ అమ్మకాల విశ్లేషణను పరీక్షించండి
        sales_result = await test_mcp_server.execute_tool(
            'execute_sales_query',
            {
                'query_type': 'daily_sales',
                'store_id': store_id,
                'start_date': (datetime.now() - timedelta(days=1)).date().isoformat(),
                'end_date': datetime.now().date().isoformat()
            }
        )
        
        assert sales_result['success'] is True
        assert len(sales_result['data']) > 0
        assert sales_result['data'][0]['total_revenue'] == 107.99
    
    async def test_multi_store_workflow(self, test_mcp_server, db_connection):
        """Test workflows across multiple stores."""
        
        # బహుళ స్టోర్లను సృష్టించండి
        stores = ['test_seattle', 'test_redmond', 'test_bellevue']
        
        for store_id in stores:
            await TestDataHelper.create_test_store(db_connection, store_id)
            
            # ప్రతి స్టోర్‌లో కస్టమర్‌ను సృష్టించండి
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # ప్రతి స్టోర్ తన స్వంత డేటాను మాత్రమే చూడగలదని పరీక్షించండి
        for store_id in stores:
            schema_result = await test_mcp_server.execute_tool(
                'execute_sales_query',
                {
                    'query_type': 'custom',
                    'store_id': store_id,
                    'query': 'SELECT COUNT(*) as customer_count FROM retail.customers'
                }
            )
            
            assert schema_result['success'] is True
            assert schema_result['data'][0]['customer_count'] == 1

class TestErrorHandling:
    """Test error handling and edge cases."""
    
    async def test_database_connection_failure(self, test_mcp_server):
        """Test behavior when database connection fails."""
        
        # చెలామణీ కాని కనెక్షన్ ఉపయోగించి డేటాబేస్ వైఫల్యాన్ని అనుకరించండి
        with patch.object(test_mcp_server.db_provider, 'get_connection') as mock_conn:
            mock_conn.side_effect = Exception("Database connection failed")
            
            result = await test_mcp_server.execute_tool(
                'get_table_schema',
                {'table_name': 'customers'}
            )
            
            assert result['success'] is False
            assert 'connection failed' in result['error'].lower()
    
    async def test_invalid_tool_parameters(self, test_mcp_server):
        """Test handling of invalid tool parameters."""
        
        # అవసరమైన పారామీటర్ లేదు
        result = await test_mcp_server.execute_tool(
            'semantic_search_products',
            {'query': 'test query'}  # store_id లేదు
        )
        
        assert result['success'] is False
        assert 'store_id is required' in result['error'].lower()
        
        # చెలామణీ కాని పారామీటర్ రకం
        result = await test_mcp_server.execute_tool(
            'semantic_search_products',
            {
                'query': 'test query',
                'store_id': 'test_store',
                'limit': 'invalid'  # ఇది పూర్తి సంఖ్య కావాలి
            }
        )
        
        assert result['success'] is False
    
    async def test_sql_injection_prevention(self, test_mcp_server, db_connection):
        """Test that SQL injection attempts are blocked."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # SQL ఇంజెక్షన్ ప్రయత్నం
        malicious_query = "SELECT * FROM retail.customers; DROP TABLE retail.customers; --"
        
        result = await test_mcp_server.execute_tool(
            'execute_sales_query',
            {
                'query_type': 'custom',
                'store_id': store_id,
                'query': malicious_query
            }
        )
        
        assert result['success'] is False
        assert 'validation failed' in result['error'].lower()
```

## 📊 పనితీరు పరీక్ష

### లోడ్ పరీక్షా ఫ్రేమ్‌వర్క్

```python
# tests/test_performance.py
"""
Performance and load testing for MCP server.
"""
import pytest
import asyncio
import time
import statistics
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any

class TestPerformance:
    """Performance testing for MCP server operations."""
    
    async def test_concurrent_tool_execution(self, test_mcp_server, db_connection):
        """Test performance under concurrent tool execution."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # పరీక్షా డేటాను సృష్టించండి
        for i in range(100):
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # పరీక్షా పరిస్థితులను నిర్వచించండి
        async def execute_tool_scenario():
            """Execute a tool and measure performance."""
            start_time = time.time()
            
            result = await test_mcp_server.execute_tool(
                'execute_sales_query',
                {
                    'query_type': 'custom',
                    'store_id': store_id,
                    'query': 'SELECT COUNT(*) as count FROM retail.customers'
                }
            )
            
            execution_time = time.time() - start_time
            return {
                'success': result['success'],
                'execution_time': execution_time
            }
        
        # సమకాలీన అమలులను నడపండి
        concurrent_tasks = 20
        tasks = [execute_tool_scenario() for _ in range(concurrent_tasks)]
        
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        total_time = time.time() - start_time
        
        # ఫలితాలను విశ్లేషించండి
        successful_executions = [r for r in results if r['success']]
        execution_times = [r['execution_time'] for r in successful_executions]
        
        assert len(successful_executions) == concurrent_tasks
        assert statistics.mean(execution_times) < 1.0  # సగటు 1 సెకన్ల కింద
        assert max(execution_times) < 5.0  # 5 సెకన్లకు పైగా అమలు లేదు
        assert total_time < 10.0  # అన్ని అమలులు 10 సెకన్ల కింద ఉన్నాయి
        
        print(f"Concurrent execution stats:")
        print(f"  Total time: {total_time:.2f}s")
        print(f"  Average execution time: {statistics.mean(execution_times):.3f}s")
        print(f"  Max execution time: {max(execution_times):.3f}s")
        print(f"  Min execution time: {min(execution_times):.3f}s")
    
    async def test_database_query_performance(self, test_mcp_server, db_connection):
        """Test database query performance with large datasets."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # పెద్ద డేటాసెట్ సృష్టించండి
        print("Creating test dataset...")
        for i in range(1000):
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # వివిధ క్వెరీ నమూనాలను పరీక్షించండి
        query_tests = [
            {
                'name': 'Simple COUNT',
                'query': 'SELECT COUNT(*) FROM retail.customers',
                'expected_max_time': 0.1
            },
            {
                'name': 'Filtered SELECT',
                'query': "SELECT * FROM retail.customers WHERE loyalty_tier = 'bronze' LIMIT 100",
                'expected_max_time': 0.5
            },
            {
                'name': 'Aggregation',
                'query': 'SELECT loyalty_tier, COUNT(*) FROM retail.customers GROUP BY loyalty_tier',
                'expected_max_time': 0.5
            }
        ]
        
        for test_case in query_tests:
            start_time = time.time()
            
            result = await test_mcp_server.execute_tool(
                'execute_sales_query',
                {
                    'query_type': 'custom',
                    'store_id': store_id,
                    'query': test_case['query']
                }
            )
            
            execution_time = time.time() - start_time
            
            assert result['success'] is True
            assert execution_time < test_case['expected_max_time']
            
            print(f"Query '{test_case['name']}': {execution_time:.3f}s")
    
    async def test_embedding_generation_performance(self, test_mcp_server):
        """Test embedding generation performance."""
        
        from mcp_server.embeddings.product_embedder import ProductEmbedder
        
        # మాక్ ఎంబెడ్డింగ్ మేనేజర్‌తో పరీక్షించండి (వాస్తవ API కాల్స్ లేవు)
        embedder = ProductEmbedder(test_mcp_server.db_provider)
        embedder.embedding_manager = test_mcp_server.embedding_manager
        
        # బ్యాచ్ ఎంబెడ్డింగ్ ఉత్పత్తిని పరీక్షించండి
        test_texts = [f"Test product {i} description" for i in range(100)]
        
        start_time = time.time()
        embeddings = await embedder.embedding_manager.generate_embeddings_batch(test_texts)
        batch_time = time.time() - start_time
        
        assert len(embeddings) == 100
        assert batch_time < 5.0  # మాక్స్‌తో 5 సెకన్ల కింద పూర్తి కావాలి
        
        print(f"Batch embedding generation (100 items): {batch_time:.3f}s")
        print(f"Average per embedding: {batch_time/100:.4f}s")
    
    @pytest.mark.slow
    async def test_memory_usage(self, test_mcp_server, db_connection):
        """Test memory usage under load."""
        
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # పెద్ద డేటాసెట్ సృష్టించండి
        for i in range(500):
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # బహుళ ఆపరేషన్లను అమలు చేయండి
        for i in range(50):
            await test_mcp_server.execute_tool(
                'execute_sales_query',
                {
                    'query_type': 'custom',
                    'store_id': store_id,
                    'query': 'SELECT * FROM retail.customers LIMIT 100'
                }
            )
        
        final_memory = process.memory_info().rss / 1024 / 1024  # MB
        memory_increase = final_memory - initial_memory
        
        # మెమరీ పెరుగుదల తగినంత ఉండాలి (ఈ పరీక్షకు 100MB కింద)
        assert memory_increase < 100
        
        print(f"Memory usage:")
        print(f"  Initial: {initial_memory:.1f} MB")
        print(f"  Final: {final_memory:.1f} MB")
        print(f"  Increase: {memory_increase:.1f} MB")

class TestScalability:
    """Test scalability characteristics."""
    
    async def test_response_time_scaling(self, test_mcp_server, db_connection):
        """Test how response time scales with data size."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # వేర్వేరు డేటా పరిమాణాలతో పరీక్షించండి
        data_sizes = [100, 500, 1000, 2000]
        response_times = []
        
        for size in data_sizes:
            # ఉన్న డేటాను క్లియర్ చేయండి
            await db_connection.execute("DELETE FROM retail.customers WHERE store_id = $1", store_id)
            
            # నిర్దిష్ట పరిమాణం గల డేటాసెట్ సృష్టించండి
            for i in range(size):
                await TestDataHelper.create_test_customer(db_connection, store_id)
            
            # క్వెరీ సమయాన్ని కొలవండి
            start_time = time.time()
            result = await test_mcp_server.execute_tool(
                'execute_sales_query',
                {
                    'query_type': 'custom',
                    'store_id': store_id,
                    'query': 'SELECT COUNT(*) FROM retail.customers'
                }
            )
            execution_time = time.time() - start_time
            
            assert result['success'] is True
            response_times.append(execution_time)
            
            print(f"Data size {size}: {execution_time:.3f}s")
        
        # స్పందన సమయం తగినంతగా పెరగాలి (ఎక్స్‌పోనెన్షియల్ కాదు)
        # సులభమైన కౌంట్ క్వెరీలు పెద్ద డేటాసెట్‌లతో కూడా వేగంగా ఉండాలి
        for time_val in response_times:
            assert time_val < 1.0  # అన్ని క్వెరీలు 1 సెకన్ల కింద ఉండాలి
```

## 🔍 డీబగ్గింగ్ టూల్స్

### అధునాతన డీబగ్గింగ్ ఫ్రేమ్‌వర్క్

```python
# mcp_server/debugging/debug_tools.py
"""
Advanced debugging tools for MCP server troubleshooting.
"""
import asyncio
import json
import time
import traceback
from typing import Dict, Any, List, Optional
from datetime import datetime
import logging
from contextlib import asynccontextmanager

logger = logging.getLogger(__name__)

class MCPDebugger:
    """Comprehensive debugging utilities for MCP server."""
    
    def __init__(self, server_instance):
        self.server = server_instance
        self.debug_logs = []
        self.performance_metrics = {}
        self.active_traces = {}
        
    @asynccontextmanager
    async def trace_execution(self, operation_name: str, context: Dict[str, Any] = None):
        """Trace operation execution with detailed logging."""
        
        trace_id = f"{operation_name}_{int(time.time() * 1000)}"
        start_time = time.time()
        
        trace_info = {
            'trace_id': trace_id,
            'operation': operation_name,
            'start_time': start_time,
            'context': context or {},
            'status': 'running'
        }
        
        self.active_traces[trace_id] = trace_info
        
        logger.debug(f"Starting trace: {trace_id} - {operation_name}")
        
        try:
            yield trace_info
            
            # విజయం
            execution_time = time.time() - start_time
            trace_info.update({
                'status': 'completed',
                'execution_time': execution_time
            })
            
            logger.debug(f"Completed trace: {trace_id} in {execution_time:.3f}s")
            
        except Exception as e:
            # లోపం
            execution_time = time.time() - start_time
            trace_info.update({
                'status': 'error',
                'execution_time': execution_time,
                'error': str(e),
                'traceback': traceback.format_exc()
            })
            
            logger.error(f"Error in trace: {trace_id} - {str(e)}")
            raise
            
        finally:
            # పూర్తయిన ట్రేస్ నిల్వ చేయండి
            self.debug_logs.append(trace_info.copy())
            del self.active_traces[trace_id]
            
            # డీబగ్ లాగ్ పరిమాణాన్ని పరిమితం చేయండి
            if len(self.debug_logs) > 1000:
                self.debug_logs = self.debug_logs[-500:]
    
    async def debug_tool_execution(self, tool_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Debug tool execution with comprehensive logging."""
        
        async with self.trace_execution(f"tool_execution_{tool_name}", {'parameters': parameters}) as trace:
            
            # ముందస్తు అమలు ధృవీకరణ
            validation_result = await self._validate_tool_parameters(tool_name, parameters)
            trace['validation'] = validation_result
            
            if not validation_result['valid']:
                return {
                    'success': False,
                    'error': f"Parameter validation failed: {validation_result['errors']}",
                    'debug_info': trace
                }
            
            # డేటాబేస్ కనెక్షన్ తనిఖీ
            db_health = await self._check_database_health()
            trace['database_health'] = db_health
            
            # పరికరాన్ని పర్యవేక్షణతో అమలు చేయండి
            try:
                tool_instance = self.server.get_tool(tool_name)
                if not tool_instance:
                    return {
                        'success': False,
                        'error': f"Tool '{tool_name}' not found",
                        'debug_info': trace
                    }
                
                # అమలు సమయంలో వనరుల వినియోగాన్ని పర్యవేక్షించండి
                start_memory = await self._get_memory_usage()
                
                result = await tool_instance.call(**parameters)
                
                end_memory = await self._get_memory_usage()
                
                trace.update({
                    'memory_start_mb': start_memory,
                    'memory_end_mb': end_memory,
                    'memory_used_mb': end_memory - start_memory,
                    'result_success': result.success,
                    'result_row_count': result.row_count
                })
                
                return {
                    'success': result.success,
                    'data': result.data,
                    'error': result.error,
                    'metadata': result.metadata,
                    'debug_info': trace
                }
                
            except Exception as e:
                trace['exception'] = {
                    'type': type(e).__name__,
                    'message': str(e),
                    'traceback': traceback.format_exc()
                }
                
                return {
                    'success': False,
                    'error': f"Tool execution failed: {str(e)}",
                    'debug_info': trace
                }
    
    async def analyze_performance_bottlenecks(self) -> Dict[str, Any]:
        """Analyze performance bottlenecks from debug logs."""
        
        if not self.debug_logs:
            return {'message': 'No debug data available'}
        
        # అమలు సమయాలను విశ్లేషించండి
        execution_times = {}
        error_rates = {}
        memory_usage = {}
        
        for log_entry in self.debug_logs[-100:]:  # చివరి 100 ఎంట్రీలు
            operation = log_entry['operation']
            
            # అమలు సమయ విశ్లేషణ
            if 'execution_time' in log_entry:
                if operation not in execution_times:
                    execution_times[operation] = []
                execution_times[operation].append(log_entry['execution_time'])
            
            # లోపాల రేటు విశ్లేషణ
            if operation not in error_rates:
                error_rates[operation] = {'total': 0, 'errors': 0}
            
            error_rates[operation]['total'] += 1
            if log_entry['status'] == 'error':
                error_rates[operation]['errors'] += 1
            
            # మెమరీ వినియోగ విశ్లేషణ
            if 'memory_used_mb' in log_entry:
                if operation not in memory_usage:
                    memory_usage[operation] = []
                memory_usage[operation].append(log_entry['memory_used_mb'])
        
        # గణాంకాలను లెక్కించండి
        performance_stats = {}
        
        for operation, times in execution_times.items():
            if times:
                performance_stats[operation] = {
                    'avg_execution_time': sum(times) / len(times),
                    'max_execution_time': max(times),
                    'min_execution_time': min(times),
                    'execution_count': len(times),
                    'error_rate': (error_rates[operation]['errors'] / 
                                 error_rates[operation]['total'] * 100),
                    'avg_memory_usage': (sum(memory_usage.get(operation, [0])) / 
                                       len(memory_usage.get(operation, [1])))
                }
        
        # అడ్డంకులను గుర్తించండి
        bottlenecks = []
        
        for operation, stats in performance_stats.items():
            if stats['avg_execution_time'] > 2.0:  # మెల్లగా జరిగే ఆపరేషన్లు
                bottlenecks.append({
                    'type': 'slow_execution',
                    'operation': operation,
                    'avg_time': stats['avg_execution_time']
                })
            
            if stats['error_rate'] > 5.0:  # అధిక లోపాల రేటు
                bottlenecks.append({
                    'type': 'high_error_rate',
                    'operation': operation,
                    'error_rate': stats['error_rate']
                })
            
            if stats['avg_memory_usage'] > 100:  # అధిక మెమరీ వినియోగం
                bottlenecks.append({
                    'type': 'high_memory_usage',
                    'operation': operation,
                    'memory_mb': stats['avg_memory_usage']
                })
        
        return {
            'performance_stats': performance_stats,
            'bottlenecks': bottlenecks,
            'total_operations': len(self.debug_logs),
            'analysis_timestamp': datetime.now().isoformat()
        }
    
    async def _validate_tool_parameters(self, tool_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Validate tool parameters against schema."""
        
        try:
            tool_instance = self.server.get_tool(tool_name)
            if not tool_instance:
                return {
                    'valid': False,
                    'errors': [f"Tool '{tool_name}' not found"]
                }
            
            schema = tool_instance.get_input_schema()
            
            # ప్రాథమిక ధృవీకరణ (ఉత్పత్తిలో jsonschema లైబ్రరీ ఉపయోగించండి)
            errors = []
            required_props = schema.get('required', [])
            
            for prop in required_props:
                if prop not in parameters:
                    errors.append(f"Missing required parameter: {prop}")
            
            return {
                'valid': len(errors) == 0,
                'errors': errors,
                'schema': schema
            }
            
        except Exception as e:
            return {
                'valid': False,
                'errors': [f"Validation error: {str(e)}"]
            }
    
    async def _check_database_health(self) -> Dict[str, Any]:
        """Check database health and connectivity."""
        
        try:
            health_status = await self.server.db_provider.health_check()
            return {
                'healthy': health_status.get('status') == 'healthy',
                'details': health_status
            }
        except Exception as e:
            return {
                'healthy': False,
                'error': str(e)
            }
    
    async def _get_memory_usage(self) -> float:
        """Get current memory usage in MB."""
        
        try:
            import psutil
            import os
            process = psutil.Process(os.getpid())
            return process.memory_info().rss / 1024 / 1024
        except:
            return 0.0
    
    def get_debug_summary(self) -> Dict[str, Any]:
        """Get summary of debug information."""
        
        recent_logs = self.debug_logs[-50:] if self.debug_logs else []
        
        return {
            'total_operations': len(self.debug_logs),
            'active_traces': len(self.active_traces),
            'recent_operations': [
                {
                    'operation': log['operation'],
                    'status': log['status'],
                    'execution_time': log.get('execution_time', 0),
                    'timestamp': log.get('start_time', 0)
                }
                for log in recent_logs
            ],
            'current_traces': list(self.active_traces.keys())
        }

# నేరుగా ఉపయోగించడానికి డీబగ్ పరికరం
class DebugTool:
    """Interactive debugging tool for MCP server."""
    
    def __init__(self, server_instance):
        self.debugger = MCPDebugger(server_instance)
    
    async def debug_query(self, query: str, store_id: str) -> Dict[str, Any]:
        """Debug a specific database query."""
        
        return await self.debugger.debug_tool_execution(
            'execute_sales_query',
            {
                'query_type': 'custom',
                'store_id': store_id,
                'query': query
            }
        )
    
    async def debug_search(self, query: str, store_id: str) -> Dict[str, Any]:
        """Debug a semantic search query."""
        
        return await self.debugger.debug_tool_execution(
            'semantic_search_products',
            {
                'query': query,
                'store_id': store_id,
                'limit': 10
            }
        )
    
    async def get_performance_report(self) -> Dict[str, Any]:
        """Get comprehensive performance report."""
        
        return await self.debugger.analyze_performance_bottlenecks()
```

## 🎯 ముఖ్యమైన పాఠాలు

ఈ ప్రయోగశాల పూర్తి చేసిన తర్వాత, మీ వద్ద ఉండాలి:

✅ **సంపూర్ణ పరీక్షా ఫ్రేమ్‌వర్క్**: అన్ని భాగాల కోసం యూనిట్, ఇంటిగ్రేషన్, మరియు పనితీరు పరీక్షలు  
✅ **అధునాతన డీబగ్గింగ్ టూల్స్**: అమలు ట్రేసింగ్‌తో కూడిన సున్నితమైన డీబగ్గింగ్ ఉపకరణాలు  
✅ **పనితీరు ధృవీకరణ**: లోడ్ పరీక్ష మరియు స్కేలబిలిటీ విశ్లేషణ సామర్థ్యాలు  
✅ **భద్రతా పరీక్ష**: SQL ఇంజెక్షన్ నివారణ మరియు RLS ధృవీకరణ  
✅ **మానిటరింగ్ ఇంటిగ్రేషన్**: పనితీరు మెట్రిక్స్ మరియు బాటిల్‌నెక్ విశ్లేషణ  
✅ **CI/CD సిద్ధం**: సతత ఇంటిగ్రేషన్ కోసం ఆటోమేటెడ్ పరీక్షా వర్క్‌ఫ్లోలు  

## 🚀 తదుపరి ఏమిటి

**[Lab 09: VS Code Integration](../09-VS-Code/README.md)** తో కొనసాగండి:

- MCP సర్వర్ అభివృద్ధి కోసం VS Code ను కాన్ఫిగర్ చేయడం  
- VS Code లో డీబగ్గింగ్ వాతావరణాలను సెటప్ చేయడం  
- MCP సర్వర్‌ను VS Code చాట్‌తో ఇంటిగ్రేట్ చేయడం  
- పూర్తి VS Code వర్క్‌ఫ్లోను పరీక్షించడం  

## 📚 అదనపు వనరులు

### పరీక్షా ఫ్రేమ్‌వర్క్లు
- [pytest Documentation](https://docs.pytest.org/) - పైథాన్ పరీక్షా ఫ్రేమ్‌వర్క్  
- [AsyncPG Testing](https://magicstack.github.io/asyncpg/current/index.html) - Async PostgreSQL పరీక్ష  
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/) - API పరీక్షా నమూనాలు  

### పనితీరు పరీక్ష
- [Load Testing Best Practices](https://docs.python.org/3/library/asyncio.html) - Async పనితీరు పరీక్ష  
- [Database Performance Testing](https://www.postgresql.org/docs/current/performance-tips.html) - PostgreSQL ఆప్టిమైజేషన్  
- [Memory Profiling](https://docs.python.org/3/library/tracemalloc.html) - పైథాన్ మెమరీ విశ్లేషణ  

### డీబగ్గింగ్ టూల్స్
- [Python Debugging](https://docs.python.org/3/library/pdb.html) - పైథాన్ డీబగ్గర్  
- [Async Debugging](https://docs.python.org/3/library/asyncio-dev.html) - Asyncio డీబగ్గింగ్  
- [SQL Debugging](https://www.postgresql.org/docs/current/runtime-config-logging.html) - PostgreSQL లాగింగ్  

---

**మునుపటి**: [Lab 07: Semantic Search Integration](../07-Semantic-Search/README.md)  
**తదుపరి**: [Lab 09: VS Code Integration](../09-VS-Code/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. అసలు పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం చేయించుకోవడం మంచిది. ఈ అనువాదం వలన కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారుల బాధ్యత మేము తీసుకోము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->