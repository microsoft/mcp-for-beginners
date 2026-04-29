# ការធ្វើតេស្ត និងកែបញ្ហា

## 🎯 អ្វីដែលមន្ទីរពហុកម្មវិធីនេះគ្របដណ្តប់

មន្ទីរនេះផ្តល់នូវការណែនាំពេញលេញអំពីការធ្វើតេស្ត និងកែបញ្ហា MCP servers ក្នុងបរិយាកាសផលិតកម្ម។ អ្នកនឹងរៀនច្បាប់ស្ត្រាតেজីតេស្តរឹងមាំ កែបញ្ហាបញ្ហាស្មុគស្មាញ ហើយធានាថា MCP server របស់អ្នកដំណើរការយ៉ាងទៀងទាត់ក្រោមលក្ខខណ្ឌផ្សេងៗ។

## សង្ខេប

ការធ្វើតេស្ត MCP servers ត្រូវបានទាមទារឱ្យមានវិធានការប្រមូលផ្តុំជាច្រើនដែលគ្របដណ្តប់ការធ្វើតេស្តឯកត្តា ធ្វើតេស្តបញ្ចូលគ្នា វាយតម្លៃសមត្ថភាព និងការធ្វើតេស្តលើសេណារីយោជាក់ស្តែង។ មន្ទីរនេះគ្របដណ្តប់ក្បួនជីវិតភាពសរុបនៃការធ្វើតេស្តចាប់ពីការអភិវឌ្ឍដល់ការត្រួតពិនិត្យផលិតកម្ម។

ស្ត្រាតេជីរបស់យើងលើការធ្វើតេស្តផ្តោតលើភាពទុកចិត្ត សុវត្ថិភាព និងសមត្ថភាព ដើម្បីធានាថា MCP server របស់អ្នកអាចដោះស្រាយបញ្ហានៅក្នុងបរិវេណផលិតកម្មខណៈដែលរក្សារភាពត្រឹមត្រូវនៃទិន្នន័យ និងគុណភាពបទពិសោធន៍អ្នកប្រើ។

## គោលបំណងរៀន

នៅចុងបញ្ចប់នៃមន្ទីរនេះ អ្នកនឹងអាច:

- **អនុវត្ត** សំណុំតេស្តឯកត្តា និងបញ្ចូលគ្នាត្រឹមត្រូវ  
- **រចនា** ស្ត្រាតេជីរាជតេស្តមានប្រសិទ្ធភាពសម្រាប់ឧបករណ៍ MCP និងប្រតិបត្តិការទិន្នន័យ  
- **កែបញ្ហា** បញ្ហាស្មុគស្មាញដោយប្រើបច្ចេកទេសកែបញ្ហាចុងក្រោយ  
- **វាយតម្លៃ** សមត្ថភាពក្រោមបន្ទុកជាមួយសេណារីយោការធ្វើតេស្តរួមចំណែកជាក់ស្តែង  
- **តាមដាន** ប្រព័ន្ធផលិតកម្មជាមួយការជូនដំណឹង និងការមើលឃើញមានប្រសិទ្ធភាព  
- **ស្វ័យប្រវត្តិ** សកម្មភាពធ្វើតេស្តសម្រាប់បញ្ចូលបន្ត

## 🧪 រចនាសម្ព័ន្ធការធ្វើតេស្ត

### សង្ខេបស្ត្រាតេជីឡើការធ្វើតេស្ត

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

### ការតំឡើងបរិយាកាសធ្វើតេស្ត

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

# ការកំណត់តេស្ត
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
    
    # បង្កើតការតភ្ជាប់មូលដ្ឋានទិន្នន័យសម្រាប់តេស្ត
    sys_conn = await asyncpg.connect(
        "postgresql://postgres:password@localhost:5432/postgres"
    )
    
    try:
        # បង្កើតមូលដ្ឋានទិន្នន័យសម្រាប់តេស្ត
        await sys_conn.execute("DROP DATABASE IF EXISTS test_retail_db")
        await sys_conn.execute("CREATE DATABASE test_retail_db")
    finally:
        await sys_conn.close()
    
    # តភ្ជាប់ទៅមូលដ្ឋានទិន្នន័យសម្រាប់តេស្ត និងរៀបចំស្គីម៉ា
    test_conn = await asyncpg.connect(TEST_DATABASE_URL)
    
    try:
        # ផ្ទុកស្គីម៉ា
        schema_sql = await load_sql_file("../scripts/create_schema.sql")
        await test_conn.execute(schema_sql)
        
        # ផ្ទុកទិន្នន័យគំរូ
        sample_data_sql = await load_sql_file("../scripts/sample_data.sql")
        await test_conn.execute(sample_data_sql)
        
        yield test_conn
        
    finally:
        await test_conn.close()
        
        # សម្អាតមូលដ្ឋានទិន្នន័យសម្រាប់តេស្ត
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
    
    # ចាប់ផ្តើមប្រតិបត្ដិការសម្រាប់ការផ្ដាច់ផ្ដោយតេស្ត
    tx = conn.transaction()
    await tx.start()
    
    try:
        yield conn
    finally:
        # ត្រឡប់ការប្រតិបត្ដិការឡើងវិញដើម្បីរក្សាការផ្ដាច់ផ្ដោយតេស្ត
        await tx.rollback()
        await conn.close()

@pytest.fixture
async def mock_embedding_manager():
    """Mock embedding manager for testing without Azure OpenAI calls."""
    
    mock_manager = AsyncMock()
    
    # សំរមោលការផលិត embedding
    mock_manager.generate_embedding.return_value = [0.1] * 1536  # សំរមោល embedding
    mock_manager.generate_embeddings_batch.return_value = [[0.1] * 1536] * 10
    
    # សំរមោលការចាប់ផ្ដើម
    mock_manager.initialize.return_value = None
    mock_manager.cleanup.return_value = None
    
    return mock_manager

@pytest.fixture
async def test_mcp_server(db_connection, mock_embedding_manager):
    """Set up test MCP server instance."""
    
    from mcp_server.server import MCPServer
    from mcp_server.database import DatabaseProvider
    from mcp_server.config import Config
    
    # បង្កើតការកំណត់តេស្ត
    config = Config()
    config.database.connection_string = TEST_DATABASE_URL
    config.server.enable_debug = True
    
    # បង្កើតអ្នកផ្តល់មូលដ្ឋានទិន្នន័យ
    db_provider = DatabaseProvider(config.database.connection_string)
    await db_provider.initialize()
    
    # បង្កើតម៉ាស៊ីនមេ MCP
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

# ជំនួយការទិន្នន័យសម្រាប់តេស្ត
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

## 🔧 ការធ្វើតេស្តឯកត្តា

### ស៊ុមធ្វើតេស្តឧបករណ៍

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
        
        # រៀបចំទិន្នន័យសម្រាប់ការធ្វើតេស្ត
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        customer_id = await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # បង្កើតប្រតិបត្តិការធ្វើតេស្ត
        await db_connection.execute("""
            INSERT INTO retail.sales_transactions (
                store_id, customer_id, transaction_date, total_amount, transaction_type
            ) VALUES ($1, $2, $3, $4, $5)
        """, store_id, customer_id, datetime.now(), 150.00, 'sale')
        
        # ប្រតិបត្ដិឧបករណ៍
        result = await sales_tool.execute(
            query_type='daily_sales',
            store_id=store_id,
            start_date=(datetime.now() - timedelta(days=7)).date(),
            end_date=datetime.now().date()
        )
        
        # បញ្ចាក់លទ្ធផល
        assert result.success is True
        assert len(result.data) > 0
        assert 'total_revenue' in result.data[0]
        assert result.metadata['query_type'] == 'daily_sales'
    
    async def test_custom_query_validation(self, sales_tool, db_connection):
        """Test custom query validation."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # សាកល្បងសំណួរដែលត្រឹមត្រូវ
        valid_query = "SELECT COUNT(*) as customer_count FROM retail.customers"
        result = await sales_tool.execute(
            query_type='custom',
            store_id=store_id,
            query=valid_query
        )
        
        assert result.success is True
        
        # សាកល្បងសំណួរមិនត្រឹមត្រូវ (គួរតែកាត់ទាំងអស់)
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
        
        # បង្កើតហាងពីរផ្សេងគ្នា
        store1 = 'test_store1'
        store2 = 'test_store2'
        
        await TestDataHelper.create_test_store(db_connection, store1)
        await TestDataHelper.create_test_store(db_connection, store2)
        
        # បង្កើតអតិថិជននៅក្នុងហាងភាគីផ្សេងៗ
        customer1 = await TestDataHelper.create_test_customer(db_connection, store1)
        customer2 = await TestDataHelper.create_test_customer(db_connection, store2)
        
        # សំណួរពីហាង១គួរតែឃើញទិន្នន័យគ្រាន់តែហាង១ប៉ុណ្ណោះ
        result1 = await sales_tool.execute(
            query_type='custom',
            store_id=store1,
            query="SELECT COUNT(*) as count FROM retail.customers"
        )
        
        # សំណួរពីហាង២គួរតែឃើញទិន្នន័យគ្រាន់តែហាង២ប៉ុណ្ណោះ
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
        
        # បង្កើតផលិតផលសម្រាប់ធ្វើតេស្ត
        for product_data in sample_products:
            product_id = await TestDataHelper.create_test_product(
                db_connection, store_id, product_data
            )
            
            # បង្កើតតំណាង embedding ក្លែងក្លាយ
            await db_connection.execute("""
                INSERT INTO retail.product_embeddings (
                    product_id, store_id, embedding_text, embedding
                ) VALUES ($1, $2, $3, $4)
            """, 
                product_id, store_id, 
                f"{product_data['product_name']} {product_data['brand']}", 
                '[0.1,0.2,0.3]'  # embedding ក្លែងក្លាយ
            )
        
        # ប្រតិបត្ដិការស្វែងរក
        result = await search_tool.execute(
            query='running shoes',
            store_id=store_id,
            limit=10,
            similarity_threshold=0.0
        )
        
        # បញ្ចាក់លទ្ធផល
        assert result.success is True
        assert len(result.data) > 0
        assert 'similarity_score' in result.data[0]
        assert result.metadata['search_type'] == 'semantic'
    
    async def test_search_parameter_validation(self, search_tool):
        """Test search parameter validation."""
        
        # សាកល្បងសំណួរមិនមាន
        result = await search_tool.execute(store_id='test_store')
        assert result.success is False
        assert 'query is required' in result.error.lower()
        
        # សាកល្បង store_id មិនមាន
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

### ការធ្វើតេស្តមូលដ្ឋានទិន្នន័យ

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
        
        # កំណត់បរិបទហាង
        await db_connection.execute("SELECT retail.set_store_context($1)", store_id)
        
        # បញ្ជាក់ថាបរិបទត្រូវបានកំណត់
        current_store = await db_connection.fetchval(
            "SELECT current_setting('app.current_store_id', true)"
        )
        
        assert current_store == store_id
    
    async def test_customer_isolation(self, db_connection):
        """Test that customers are properly isolated by store."""
        
        # បង្កើតហាងពីរពីរប្រភេទ
        store1 = 'test_store1'
        store2 = 'test_store2'
        
        await TestDataHelper.create_test_store(db_connection, store1)
        await TestDataHelper.create_test_store(db_connection, store2)
        
        # បង្កើតអតិថិជននៅក្នុងហាងផ្សេងៗ
        await TestDataHelper.create_test_customer(db_connection, store1)
        await TestDataHelper.create_test_customer(db_connection, store2)
        
        # កំណត់បរិបទទៅហាង១ និងរាប់ចំនួនអតិថិជន
        await db_connection.execute("SELECT retail.set_store_context($1)", store1)
        store1_count = await db_connection.fetchval("SELECT COUNT(*) FROM retail.customers")
        
        # កំណត់បរិបទទៅហាង២ និងរាប់ចំនួនអតិថិជន
        await db_connection.execute("SELECT retail.set_store_context($1)", store2)
        store2_count = await db_connection.fetchval("SELECT COUNT(*) FROM retail.customers")
        
        # ហាងនីមួយៗគួរតែឃើញតែអតិថិជនរបស់ខ្លួនតែប៉ុណ្ណោះ
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
        
        # កំណត់បរិបទហាង
        await db_connection.execute("SELECT retail.set_store_context($1)", store_id)
        
        # ព្យាយាមបញ្ចូលអតិថិជនទៅហាងផ្សេង (គួរតែបរាជ័យ)
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
        
        # ទទួលបានការតភ្ជាប់ច្រើន
        conn1 = await db_provider.get_connection()
        conn2 = await db_provider.get_connection()
        
        assert conn1 is not None
        assert conn2 is not None
        assert conn1 != conn2  # គួរតែជាវត្ថុការតភ្ជាប់ខុសគ្នា
        
        # សម្លឹងការតភ្ជាប់វិញ
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
        
        # នេះនឹងសាកល្បងសណ្ឋានការស្ដារឡើងវិញនៃការតភ្ជាប់
        # ក្នុងការសាកល្បងពិត អ្នកអាចបំបែកការតភ្ជាប់បណ្ដោះអាសន្ន
        # ហើយបញ្ជាក់ថាប្រមូលការតភ្ជាប់បានស្ដារឡើងវិញ
        
        # សម្រាប់ឥឡូវនេះ គ្រាន់តែបញ្ជាក់ថាការត្រួតពិនិត្យសុខភាពដំណើរការ
        health_status = await db_provider.health_check()
        assert health_status['status'] == 'healthy'
```

## 🚀 ការធ្វើតេស្តបញ្ចូលគ្នា

### ការធ្វើតេស្តវេទិកាការងារចុងពីលើដល់ចុងក្រោម

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
        
        # បង្កើតផលិតផលសាកល្បងជាមួយនឹង embeddings
        for product_data in sample_products:
            product_id = await TestDataHelper.create_test_product(
                db_connection, store_id, product_data
            )
            
            # បង្កើត embedding សម្រាប់ផលិតផល
            await db_connection.execute("""
                INSERT INTO retail.product_embeddings (
                    product_id, store_id, embedding_text, embedding
                ) VALUES ($1, $2, $3, $4)
            """, 
                product_id, store_id, 
                f"{product_data['product_name']} {product_data['brand']}", 
                '[' + ','.join(['0.1'] * 1536) + ']'  # យក embedding មកគំរូ
            )
        
        # សាកល្បងស្វែងរកពាក្យអត្ថន័យ
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
        
        # សាកល្បងការពិនិត្យ schema
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
        
        # បង្កើតអតិថិជន និងផលិតផលសាកល្បង
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
        
        # បង្កើតប្រតិបត្តិការសាកល្បង
        transaction_id = await db_connection.fetchval("""
            INSERT INTO retail.sales_transactions (
                store_id, customer_id, transaction_date, total_amount, 
                subtotal, tax_amount, transaction_type
            ) VALUES ($1, $2, $3, $4, $5, $6, $7)
            RETURNING transaction_id
        """, store_id, customer_id, datetime.now(), 107.99, 99.99, 8.00, 'sale')
        
        # បង្កើតធាតុប្រតិបត្តិការ
        await db_connection.execute("""
            INSERT INTO retail.sales_transaction_items (
                transaction_id, product_id, quantity, unit_price, total_price
            ) VALUES ($1, $2, $3, $4, $5)
        """, transaction_id, product_id, 1, 99.99, 99.99)
        
        # សាកល្បងវិភាគការលក់ប្រចាំថ្ងៃ
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
        
        # បង្កើតហាងជាច្រើន
        stores = ['test_seattle', 'test_redmond', 'test_bellevue']
        
        for store_id in stores:
            await TestDataHelper.create_test_store(db_connection, store_id)
            
            # បង្កើតអតិថិជននៅក្នុងហាងនីមួយៗ
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # សាកល្បងថា ហាងនីមួយៗមើលឃើញទិន្នន័យរបស់ខ្លួនប៉ុណ្ណោះ
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
        
        # simulation ការបរាជ័យរបស់មូលដ្ឋានទិន្នន័យដោយប្រើការតភ្ជាប់មិនត្រឹមត្រូវ
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
        
        # ខ្វះប៉ារ៉ាម៉ែត្រដែលត្រូវការ
        result = await test_mcp_server.execute_tool(
            'semantic_search_products',
            {'query': 'test query'}  # ខ្វះ store_id
        )
        
        assert result['success'] is False
        assert 'store_id is required' in result['error'].lower()
        
        # ប្រភេទប៉ារ៉ាម៉ែត្រមិនត្រឹមត្រូវ
        result = await test_mcp_server.execute_tool(
            'semantic_search_products',
            {
                'query': 'test query',
                'store_id': 'test_store',
                'limit': 'invalid'  # គួរតែជាចំនួនគត់
            }
        )
        
        assert result['success'] is False
    
    async def test_sql_injection_prevention(self, test_mcp_server, db_connection):
        """Test that SQL injection attempts are blocked."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # ព្យាយាម SQL injection
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

## 📊 ការធ្វើតេស្តសមត្ថភាព

### ស៊ុមការធ្វើតេស្តបន្ទុក

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
        
        # បង្កើតទិន្នន័យសាកល្បង
        for i in range(100):
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # កំណត់សកម្មភាពសាកល្បង
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
        
        # ប្រតិបត្តិការដំណើរការចូលរួម
        concurrent_tasks = 20
        tasks = [execute_tool_scenario() for _ in range(concurrent_tasks)]
        
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        total_time = time.time() - start_time
        
        # វិភាគលទ្ធផល
        successful_executions = [r for r in results if r['success']]
        execution_times = [r['execution_time'] for r in successful_executions]
        
        assert len(successful_executions) == concurrent_tasks
        assert statistics.mean(execution_times) < 1.0  # មធ្យមក្រោម 1 វិនាទី
        assert max(execution_times) < 5.0  # មិនមានការប្រតិបត្តិលើស 5 វិនាទី
        assert total_time < 10.0  # ការប្រតិបត្តិទាំងអស់ក្រោម 10 វិនាទី
        
        print(f"Concurrent execution stats:")
        print(f"  Total time: {total_time:.2f}s")
        print(f"  Average execution time: {statistics.mean(execution_times):.3f}s")
        print(f"  Max execution time: {max(execution_times):.3f}s")
        print(f"  Min execution time: {min(execution_times):.3f}s")
    
    async def test_database_query_performance(self, test_mcp_server, db_connection):
        """Test database query performance with large datasets."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # បង្កើតមូលដ្ឋានទិន្នន័យធំ
        print("Creating test dataset...")
        for i in range(1000):
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # សាកល្បងលំនាំសំណួរផ្សេងៗ
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
        
        # សាកល្បងជាមួយអ្នកគ្រប់គ្រងបញ្ចូលមុខងារ (គ្មានការហៅ API ពិតជាដំណើរការ)
        embedder = ProductEmbedder(test_mcp_server.db_provider)
        embedder.embedding_manager = test_mcp_server.embedding_manager
        
        # សាកល្បងការបង្កើតបញ្ចូលមុខងារជាកញ្ចប់
        test_texts = [f"Test product {i} description" for i in range(100)]
        
        start_time = time.time()
        embeddings = await embedder.embedding_manager.generate_embeddings_batch(test_texts)
        batch_time = time.time() - start_time
        
        assert len(embeddings) == 100
        assert batch_time < 5.0  # គួរតែបញ្ចប់ក្នុងរយៈពេលក្រោម 5 វិនាទីជាមួយមុខងារ mock
        
        print(f"Batch embedding generation (100 items): {batch_time:.3f}s")
        print(f"Average per embedding: {batch_time/100:.4f}s")
    
    @pytest.mark.slow
    async def test_memory_usage(self, test_mcp_server, db_connection):
        """Test memory usage under load."""
        
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024 / 1024  # មេកាបៃ
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # បង្កើតមូលដ្ឋានទិន្នន័យសំខាន់
        for i in range(500):
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # អនុវត្តន៍ប្រតិបត្តិការច្រើន
        for i in range(50):
            await test_mcp_server.execute_tool(
                'execute_sales_query',
                {
                    'query_type': 'custom',
                    'store_id': store_id,
                    'query': 'SELECT * FROM retail.customers LIMIT 100'
                }
            )
        
        final_memory = process.memory_info().rss / 1024 / 1024  # មេកាបៃ
        memory_increase = final_memory - initial_memory
        
        # ការកើនឡើងនៃចងចាំគួរតែសមរម្យ (ក្រោម 100MB សម្រាប់ការសាកល្បងនេះ)
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
        
        # សាកល្បងជាមួយទំហំទិន្នន័យផ្សេងៗ
        data_sizes = [100, 500, 1000, 2000]
        response_times = []
        
        for size in data_sizes:
            # លាងសំអាតទិន្នន័យដែលមានរួច
            await db_connection.execute("DELETE FROM retail.customers WHERE store_id = $1", store_id)
            
            # បង្កើតមូលដ្ឋានទិន្នន័យមានទំហំបានកំណត់
            for i in range(size):
                await TestDataHelper.create_test_customer(db_connection, store_id)
            
            # វាស់ពេលវេលាសំណួរ
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
        
        # ពេលវេលារឆ្លើយតបគួរតែបង្រួមតាមប្រការ (មិនលូតលាស់ប្រសើរ)
        # សំណួរដើម្បីរាប់មូលដ្ឋានសាមញ្ញគួរតែរហ័សក្នុងករណីទិន្នន័យធំ
        for time_val in response_times:
            assert time_val < 1.0  # សំណួរទាំងអស់ក្រោម 1 វិនាទី
```

## 🔍 ឧបករណ៍កែបញ្ហា

### ស៊ុមកែបញ្ហាចុងក្រោយ

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
            
            # ជោគជ័យ
            execution_time = time.time() - start_time
            trace_info.update({
                'status': 'completed',
                'execution_time': execution_time
            })
            
            logger.debug(f"Completed trace: {trace_id} in {execution_time:.3f}s")
            
        except Exception as e:
            # កំហុស
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
            # រក្សាទុកការតាមដានបានបញ្ចប់
            self.debug_logs.append(trace_info.copy())
            del self.active_traces[trace_id]
            
            # កំណត់ទំហំកំណត់ហេតុបញ្ជោល
            if len(self.debug_logs) > 1000:
                self.debug_logs = self.debug_logs[-500:]
    
    async def debug_tool_execution(self, tool_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Debug tool execution with comprehensive logging."""
        
        async with self.trace_execution(f"tool_execution_{tool_name}", {'parameters': parameters}) as trace:
            
            # សុពលភាពមុនការអនុវត្ត
            validation_result = await self._validate_tool_parameters(tool_name, parameters)
            trace['validation'] = validation_result
            
            if not validation_result['valid']:
                return {
                    'success': False,
                    'error': f"Parameter validation failed: {validation_result['errors']}",
                    'debug_info': trace
                }
            
            # ពិនិត្យការតភ្ជាប់មូលដ្ឋានទិន្នន័យ
            db_health = await self._check_database_health()
            trace['database_health'] = db_health
            
            # អនុវត្តឧបករណ៍ជាមួយការត្រួតពិនិត្យ
            try:
                tool_instance = self.server.get_tool(tool_name)
                if not tool_instance:
                    return {
                        'success': False,
                        'error': f"Tool '{tool_name}' not found",
                        'debug_info': trace
                    }
                
                # ត្រួតពិនិត្យការប្រើប្រាស់ធនធានក្នុងអំឡុងការអនុវត្ត
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
        
        # វិភាគពេលវេលាអនុវត្ត
        execution_times = {}
        error_rates = {}
        memory_usage = {}
        
        for log_entry in self.debug_logs[-100:]:  # បញ្ចូលចុងក្រោយ ១០០
            operation = log_entry['operation']
            
            # វិភាគពេលវេលាអនុវត្ត
            if 'execution_time' in log_entry:
                if operation not in execution_times:
                    execution_times[operation] = []
                execution_times[operation].append(log_entry['execution_time'])
            
            # វិភាគអត្រាកំហុស
            if operation not in error_rates:
                error_rates[operation] = {'total': 0, 'errors': 0}
            
            error_rates[operation]['total'] += 1
            if log_entry['status'] == 'error':
                error_rates[operation]['errors'] += 1
            
            # វិភាគការប្រើប្រាស់ផ្នែកម៉emory
            if 'memory_used_mb' in log_entry:
                if operation not in memory_usage:
                    memory_usage[operation] = []
                memory_usage[operation].append(log_entry['memory_used_mb'])
        
        # គណនាស្ថិតិ
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
        
        # សម្គាល់ចំណុចរាំងស្ទះ
        bottlenecks = []
        
        for operation, stats in performance_stats.items():
            if stats['avg_execution_time'] > 2.0:  # ប្រតិបត្តិការពេលយឺត
                bottlenecks.append({
                    'type': 'slow_execution',
                    'operation': operation,
                    'avg_time': stats['avg_execution_time']
                })
            
            if stats['error_rate'] > 5.0:  # អត្រាកំហុសខ្ពស់
                bottlenecks.append({
                    'type': 'high_error_rate',
                    'operation': operation,
                    'error_rate': stats['error_rate']
                })
            
            if stats['avg_memory_usage'] > 100:  # ការប្រើប្រាស់ផ្នែកម៉memoryខ្ពស់
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
            
            # សុពលភាពមូលដ្ឋាន (នៅក្នុងផលិតកម្ម ប្រើបណ្ណាល័យ jsonschema)
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

# ឧបករណ៍បញ្ជោលសម្រាប់ប្រើប្រាស់ផ្ទាល់
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

## 🎯 ចំណុចចម្បងដែលគួរចង្អុល

បន្ទាប់ពីបញ្ចប់មន្ទីរនេះ អ្នកគួរតែមាន:

✅ **ស៊ុមធ្វើតេស្តពេញលេញ**: ការធ្វើតេស្តឯកត្តា បញ្ចូលគ្នា និងសមត្ថភាពសម្រាប់គ្រប់ធាតុ  
✅ **ឧបករណ៍កែបញ្ហាចុងក្រោយ**: ឧបករណ៍កែបញ្ហារឹងមាំជាមួយការតាមដានការប្រតិបត្តិ  
✅ **ការវាយតម្លៃសមត្ថភាព**: សមត្ថភាពធ្វើតេស្តបន្ទុក និងវិភាគអាចតំលៃលើបណ្តោយ  
✅ **ការធ្វើតេស្តសុវត្ថិភាព**: ការការពារ SQL injection និងការវាយតម្លៃ RLS  
✅ **ការតាមដានបញ្ចូលគ្នា**: មេត្រីកសមត្ថភាព និងវិភាគបញ្ហាការលំបាក  
✅ **ត្រៀមសម្រាប់ CI/CD**: សកម្មភាពធ្វើតេស្តស្វ័យប្រវត្តិសម្រាប់បញ្ចូលបន្ត  

## 🚀 អ្វីខាងក្រោម

សូមបន្តជាមួយ **[Lab 09: VS Code Integration](../09-VS-Code/README.md)** ដើម្បី:

- កំណត់តម្រូវ VS Code សម្រាប់អភិវឌ្ឍ MCP server  
- តំឡើងបរិយាកាសកែបញ្ហានៅក្នុង VS Code  
- ធ្វើបញ្ចូល MCP server ជាមួយ VS Code Chat  
- ធ្វើតេស្តវេទិកាពេញលេញនៅក្នុង VS Code  

## 📚 ឯកសារពាក់ព័ន្ធបន្ថែម

### ស៊ុមធ្វើតេស្ត
- [pytest Documentation](https://docs.pytest.org/) - ស៊ុមធ្វើតេស្ត Python  
- [AsyncPG Testing](https://magicstack.github.io/asyncpg/current/index.html) - ការធ្វើតេស្ត Async PostgreSQL  
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/) - រចនាសម្ព័ន្ធការធ្វើតេស្ត API  

### ការធ្វើតេស្តសមត្ថភាព
- [Load Testing Best Practices](https://docs.python.org/3/library/asyncio.html) - ការធ្វើតេស្តសមត្ថភាព Async  
- [Database Performance Testing](https://www.postgresql.org/docs/current/performance-tips.html) - ការបង្កើនប្រសិទ្ធភាព PostgreSQL  
- [Memory Profiling](https://docs.python.org/3/library/tracemalloc.html) - វិភាគអង្គចងចាំ Python  

### ឧបករណ៍កែបញ្ហា
- [Python Debugging](https://docs.python.org/3/library/pdb.html) - កម្មវិធីកែបញ្ហា Python  
- [Async Debugging](https://docs.python.org/3/library/asyncio-dev.html) - កែបញ្ហា Asyncio  
- [SQL Debugging](https://www.postgresql.org/docs/current/runtime-config-logging.html) - ការចុះបញ្ជី PostgreSQL  

---

**មុននេះ**: [Lab 07: Semantic Search Integration](../07-Semantic-Search/README.md)  
**បន្ទាប់**: [Lab 09: VS Code Integration](../09-VS-Code/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**លក្ខណៈព័ត៌មានបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំរកភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាម្ចាស់ដើមគួរត្រូវបានចាត់ទុកជាមូលដ្ឋានដ៏មានសុពលភាព។ សម្រាប់ព័ត៌មានដ៏សំខាន់ ខ្ញុំស្នើឱ្យប្រើការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំនៅឬការបកស្រាយខុសនៅពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->