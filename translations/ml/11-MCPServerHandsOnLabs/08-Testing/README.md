<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ad02c1223d7861292651ffce2f52bb28",
  "translation_date": "2025-12-11T14:29:21+00:00",
  "source_file": "11-MCPServerHandsOnLabs/08-Testing/README.md",
  "language_code": "ml"
}
-->
# ടെസ്റ്റിംഗ് ആൻഡ് ഡീബഗ്ഗിംഗ്

## 🎯 ഈ ലാബ് ഉൾക്കൊള്ളുന്നത്

ഈ ലാബ് പ്രൊഡക്ഷൻ പരിസ്ഥിതികളിൽ MCP സർവറുകളുടെ ടെസ്റ്റിംഗും ഡീബഗ്ഗിംഗും സംബന്ധിച്ച സമഗ്ര മാർഗ്ഗനിർദ്ദേശം നൽകുന്നു. നിങ്ങൾ ശക്തമായ ടെസ്റ്റിംഗ് തന്ത്രങ്ങൾ നടപ്പിലാക്കാനും, സങ്കീർണ്ണ പ്രശ്നങ്ങൾ ഡീബഗ് ചെയ്യാനും, വിവിധ സാഹചര്യങ്ങളിൽ നിങ്ങളുടെ MCP സർവർ വിശ്വസനീയമായി പ്രവർത്തിക്കുന്നുണ്ടെന്ന് ഉറപ്പാക്കാനും പഠിക്കും.

## അവലോകനം

MCP സർവറുകളുടെ ടെസ്റ്റിംഗ് യൂണിറ്റ് ടെസ്റ്റുകൾ, ഇന്റഗ്രേഷൻ ടെസ്റ്റുകൾ, പ്രകടന പരിശോധന, യഥാർത്ഥ ലോക സീനാരിയോ ടെസ്റ്റിംഗ് എന്നിവ ഉൾക്കൊള്ളുന്ന ബഹുസ്ഥര സമീപനം ആവശ്യമാണ്. ഈ ലാബ് വികസനത്തിൽ നിന്ന് പ്രൊഡക്ഷൻ നിരീക്ഷണത്തിലേക്ക് ടെസ്റ്റിംഗ് ജീവിതചക്രം പൂർണ്ണമായി ഉൾക്കൊള്ളുന്നു.

നമ്മുടെ ടെസ്റ്റിംഗ് തന്ത്രം വിശ്വസനീയത, സുരക്ഷ, പ്രകടനം എന്നിവയെ മുൻനിർത്തിയാണ്, പ്രൊഡക്ഷൻ വർക്ക്‌ലോഡുകൾ കൈകാര്യം ചെയ്യുമ്പോൾ ഡാറ്റാ ഇന്റഗ്രിറ്റി, ഉപയോക്തൃ അനുഭവ ഗുണമേന്മ എന്നിവ നിലനിർത്താൻ നിങ്ങളുടെ MCP സർവർക്ക് കഴിവുണ്ടാകുമെന്ന് ഉറപ്പാക്കുന്നു.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ ലാബ് പൂർത്തിയാക്കിയാൽ, നിങ്ങൾക്ക് കഴിയും:

- **സമഗ്ര യൂണിറ്റ്** ആൻഡ് **ഇന്റഗ്രേഷൻ ടെസ്റ്റ് സ്യൂട്ടുകൾ** നടപ്പിലാക്കുക  
- MCP ടൂളുകളും ഡാറ്റാബേസ് പ്രവർത്തനങ്ങളും വേണ്ടി **ഫലപ്രദമായ ടെസ്റ്റിംഗ് തന്ത്രങ്ങൾ** രൂപകൽപ്പന ചെയ്യുക  
- **സങ്കീർണ്ണ പ്രശ്നങ്ങൾ** ആധുനിക ഡീബഗ്ഗിംഗ് സാങ്കേതികവിദ്യകൾ ഉപയോഗിച്ച് ഡീബഗ് ചെയ്യുക  
- യാഥാർത്ഥ്യപരമായ ടെസ്റ്റിംഗ് സീനാരിയോകളിൽ **ലോഡ് കീഴിൽ പ്രകടനം** സ്ഥിരീകരിക്കുക  
- ഫലപ്രദമായ അലർട്ടിംഗ്, നിരീക്ഷണ സംവിധാനങ്ങളോടെ **പ്രൊഡക്ഷൻ സിസ്റ്റങ്ങൾ നിരീക്ഷിക്കുക**  
- തുടർച്ചയായ ഇന്റഗ്രേഷനായി **ടെസ്റ്റിംഗ് വർക്ക്‌ഫ്ലോകൾ ഓട്ടോമേറ്റ് ചെയ്യുക**  

## 🧪 ടെസ്റ്റിംഗ് ആർക്കിടെക്ചർ

### ടെസ്റ്റിംഗ് തന്ത്രം അവലോകനം

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

### ടെസ്റ്റ് പരിസ്ഥിതി ക്രമീകരണം

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

# ടെസ്റ്റ് കോൺഫിഗറേഷൻ
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
    
    # ടെസ്റ്റ് ഡാറ്റാബേസ് കണക്ഷൻ സൃഷ്ടിക്കുക
    sys_conn = await asyncpg.connect(
        "postgresql://postgres:password@localhost:5432/postgres"
    )
    
    try:
        # ടെസ്റ്റ് ഡാറ്റാബേസ് സൃഷ്ടിക്കുക
        await sys_conn.execute("DROP DATABASE IF EXISTS test_retail_db")
        await sys_conn.execute("CREATE DATABASE test_retail_db")
    finally:
        await sys_conn.close()
    
    # ടെസ്റ്റ് ഡാറ്റാബേസുമായി കണക്ട് ചെയ്ത് സ്കീമ സജ്ജമാക്കുക
    test_conn = await asyncpg.connect(TEST_DATABASE_URL)
    
    try:
        # സ്കീമ ലോഡ് ചെയ്യുക
        schema_sql = await load_sql_file("../scripts/create_schema.sql")
        await test_conn.execute(schema_sql)
        
        # സാമ്പിൾ ഡാറ്റ ലോഡ് ചെയ്യുക
        sample_data_sql = await load_sql_file("../scripts/sample_data.sql")
        await test_conn.execute(sample_data_sql)
        
        yield test_conn
        
    finally:
        await test_conn.close()
        
        # ടെസ്റ്റ് ഡാറ്റാബേസ് ക്ലീൻഅപ്പ് ചെയ്യുക
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
    
    # ടെസ്റ്റ് ഐസൊലേഷനായി ട്രാൻസാക്ഷൻ ആരംഭിക്കുക
    tx = conn.transaction()
    await tx.start()
    
    try:
        yield conn
    finally:
        # ടെസ്റ്റ് ഐസൊലേഷൻ നിലനിർത്താൻ ട്രാൻസാക്ഷൻ റോള്ബാക്ക് ചെയ്യുക
        await tx.rollback()
        await conn.close()

@pytest.fixture
async def mock_embedding_manager():
    """Mock embedding manager for testing without Azure OpenAI calls."""
    
    mock_manager = AsyncMock()
    
    # എംബെഡ്ഡിംഗ് ജനറേഷൻ മോക് ചെയ്യുക
    mock_manager.generate_embedding.return_value = [0.1] * 1536  # എംബെഡ്ഡിംഗ് മോക് ചെയ്യുക
    mock_manager.generate_embeddings_batch.return_value = [[0.1] * 1536] * 10
    
    # ഇൻഷിയലൈസേഷൻ മോക് ചെയ്യുക
    mock_manager.initialize.return_value = None
    mock_manager.cleanup.return_value = None
    
    return mock_manager

@pytest.fixture
async def test_mcp_server(db_connection, mock_embedding_manager):
    """Set up test MCP server instance."""
    
    from mcp_server.server import MCPServer
    from mcp_server.database import DatabaseProvider
    from mcp_server.config import Config
    
    # ടെസ്റ്റ് കോൺഫിഗറേഷൻ സൃഷ്ടിക്കുക
    config = Config()
    config.database.connection_string = TEST_DATABASE_URL
    config.server.enable_debug = True
    
    # ഡാറ്റാബേസ് പ്രൊവൈഡർ സൃഷ്ടിക്കുക
    db_provider = DatabaseProvider(config.database.connection_string)
    await db_provider.initialize()
    
    # MCP സർവർ സൃഷ്ടിക്കുക
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

# ടെസ്റ്റ് ഡാറ്റാ ഹെൽപ്പേഴ്സ്
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

## 🔧 യൂണിറ്റ് ടെസ്റ്റിംഗ്

### ടൂൾ ടെസ്റ്റിംഗ് ഫ്രെയിംവർക്ക്

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
        
        # ടെസ്റ്റ് ഡാറ്റ സജ്ജമാക്കുക
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        customer_id = await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # ടെസ്റ്റ് ട്രാൻസാക്ഷൻ സൃഷ്ടിക്കുക
        await db_connection.execute("""
            INSERT INTO retail.sales_transactions (
                store_id, customer_id, transaction_date, total_amount, transaction_type
            ) VALUES ($1, $2, $3, $4, $5)
        """, store_id, customer_id, datetime.now(), 150.00, 'sale')
        
        # ടൂൾ പ്രവർത്തിപ്പിക്കുക
        result = await sales_tool.execute(
            query_type='daily_sales',
            store_id=store_id,
            start_date=(datetime.now() - timedelta(days=7)).date(),
            end_date=datetime.now().date()
        )
        
        # ഫലങ്ങൾ സാധൂകരിക്കുക
        assert result.success is True
        assert len(result.data) > 0
        assert 'total_revenue' in result.data[0]
        assert result.metadata['query_type'] == 'daily_sales'
    
    async def test_custom_query_validation(self, sales_tool, db_connection):
        """Test custom query validation."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # സാധുവായ ക്വറി പരിശോധിക്കുക
        valid_query = "SELECT COUNT(*) as customer_count FROM retail.customers"
        result = await sales_tool.execute(
            query_type='custom',
            store_id=store_id,
            query=valid_query
        )
        
        assert result.success is True
        
        # അസാധുവായ ക്വറി പരിശോധിക്കുക (തടയപ്പെടണം)
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
        
        # രണ്ട് വ്യത്യസ്ത സ്റ്റോറുകൾ സൃഷ്ടിക്കുക
        store1 = 'test_store1'
        store2 = 'test_store2'
        
        await TestDataHelper.create_test_store(db_connection, store1)
        await TestDataHelper.create_test_store(db_connection, store2)
        
        # വ്യത്യസ്ത സ്റ്റോറുകളിൽ ഉപഭോക്താക്കളെ സൃഷ്ടിക്കുക
        customer1 = await TestDataHelper.create_test_customer(db_connection, store1)
        customer2 = await TestDataHelper.create_test_customer(db_connection, store2)
        
        # സ്റ്റോർ1-ൽ നിന്നുള്ള ക്വറി സ്റ്റോർ1 ഡാറ്റ മാത്രം കാണണം
        result1 = await sales_tool.execute(
            query_type='custom',
            store_id=store1,
            query="SELECT COUNT(*) as count FROM retail.customers"
        )
        
        # സ്റ്റോർ2-ൽ നിന്നുള്ള ക്വറി സ്റ്റോർ2 ഡാറ്റ മാത്രം കാണണം
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
        
        # ടെസ്റ്റ് ഉൽപ്പന്നങ്ങൾ സൃഷ്ടിക്കുക
        for product_data in sample_products:
            product_id = await TestDataHelper.create_test_product(
                db_connection, store_id, product_data
            )
            
            # മോക് എംബെഡിംഗ് സൃഷ്ടിക്കുക
            await db_connection.execute("""
                INSERT INTO retail.product_embeddings (
                    product_id, store_id, embedding_text, embedding
                ) VALUES ($1, $2, $3, $4)
            """, 
                product_id, store_id, 
                f"{product_data['product_name']} {product_data['brand']}", 
                '[0.1,0.2,0.3]'  # മോക് എംബെഡിംഗ്
            )
        
        # തിരയൽ പ്രവർത്തിപ്പിക്കുക
        result = await search_tool.execute(
            query='running shoes',
            store_id=store_id,
            limit=10,
            similarity_threshold=0.0
        )
        
        # ഫലങ്ങൾ സാധൂകരിക്കുക
        assert result.success is True
        assert len(result.data) > 0
        assert 'similarity_score' in result.data[0]
        assert result.metadata['search_type'] == 'semantic'
    
    async def test_search_parameter_validation(self, search_tool):
        """Test search parameter validation."""
        
        # കാണാനില്ലാത്ത ക്വറി പരിശോധിക്കുക
        result = await search_tool.execute(store_id='test_store')
        assert result.success is False
        assert 'query is required' in result.error.lower()
        
        # കാണാനില്ലാത്ത സ്റ്റോർ_ഐഡി പരിശോധിക്കുക
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

### ഡാറ്റാബേസ് ടെസ്റ്റിംഗ്

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
        
        # സ്റ്റോർ കോൺടെക്സ്റ്റ് സജ്ജമാക്കുക
        await db_connection.execute("SELECT retail.set_store_context($1)", store_id)
        
        # കോൺടെക്സ്റ്റ് സജ്ജമാക്കിയിട്ടുണ്ടെന്ന് സ്ഥിരീകരിക്കുക
        current_store = await db_connection.fetchval(
            "SELECT current_setting('app.current_store_id', true)"
        )
        
        assert current_store == store_id
    
    async def test_customer_isolation(self, db_connection):
        """Test that customers are properly isolated by store."""
        
        # രണ്ട് സ്റ്റോറുകൾ സൃഷ്ടിക്കുക
        store1 = 'test_store1'
        store2 = 'test_store2'
        
        await TestDataHelper.create_test_store(db_connection, store1)
        await TestDataHelper.create_test_store(db_connection, store2)
        
        # വ്യത്യസ്ത സ്റ്റോറുകളിൽ ഉപഭോക്താക്കളെ സൃഷ്ടിക്കുക
        await TestDataHelper.create_test_customer(db_connection, store1)
        await TestDataHelper.create_test_customer(db_connection, store2)
        
        # കോൺടെക്സ്റ്റ് store1 ആയി സജ്ജമാക്കി ഉപഭോക്താക്കളുടെ എണ്ണം എണ്ണുക
        await db_connection.execute("SELECT retail.set_store_context($1)", store1)
        store1_count = await db_connection.fetchval("SELECT COUNT(*) FROM retail.customers")
        
        # കോൺടെക്സ്റ്റ് store2 ആയി സജ്ജമാക്കി ഉപഭോക്താക്കളുടെ എണ്ണം എണ്ണുക
        await db_connection.execute("SELECT retail.set_store_context($1)", store2)
        store2_count = await db_connection.fetchval("SELECT COUNT(*) FROM retail.customers")
        
        # ഓരോ സ്റ്റോറും അതിന്റെ സ്വന്തം ഉപഭോക്താക്കളെ മാത്രമേ കാണൂ
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
        
        # സ്റ്റോർ കോൺടെക്സ്റ്റ് സജ്ജമാക്കുക
        await db_connection.execute("SELECT retail.set_store_context($1)", store_id)
        
        # വ്യത്യസ്ത സ്റ്റോറിനായി ഉപഭോക്താവ് ചേർക്കാൻ ശ്രമിക്കുക (പരാജയപ്പെടണം)
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
        
        # പല കണക്ഷനുകളും നേടുക
        conn1 = await db_provider.get_connection()
        conn2 = await db_provider.get_connection()
        
        assert conn1 is not None
        assert conn2 is not None
        assert conn1 != conn2  # വ്യത്യസ്ത കണക്ഷൻ ഒബ്ജക്റ്റുകൾ ആയിരിക്കണം
        
        # കണക്ഷനുകൾ റിലീസ് ചെയ്യുക
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
        
        # ഇത് കണക്ഷൻ പുനരുദ്ധാരണ സാഹചര്യങ്ങൾ പരിശോധിക്കും
        # യഥാർത്ഥ ടെസ്റ്റിൽ, നിങ്ങൾ താൽക്കാലികമായി കണക്ഷൻ തകരാറിലാക്കാം
        # പിന്നെ പൂളിന്റെ പുനരുദ്ധാരണം സ്ഥിരീകരിക്കുക
        
        # ഇപ്പോൾ, ഹെൽത്ത് ചെക്ക് പ്രവർത്തിക്കുന്നുണ്ടെന്ന് മാത്രം സ്ഥിരീകരിക്കുക
        health_status = await db_provider.health_check()
        assert health_status['status'] == 'healthy'
```

## 🚀 ഇന്റഗ്രേഷൻ ടെസ്റ്റിംഗ്

### എന്റ്-ടു-എന്റ് വർക്ക്‌ഫ്ലോ ടെസ്റ്റിംഗ്

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
        
        # എംബെഡിംഗുകളുള്ള ടെസ്റ്റ് ഉൽപ്പന്നങ്ങൾ സൃഷ്ടിക്കുക
        for product_data in sample_products:
            product_id = await TestDataHelper.create_test_product(
                db_connection, store_id, product_data
            )
            
            # ഉൽപ്പന്നത്തിനായി എംബെഡിംഗ് സൃഷ്ടിക്കുക
            await db_connection.execute("""
                INSERT INTO retail.product_embeddings (
                    product_id, store_id, embedding_text, embedding
                ) VALUES ($1, $2, $3, $4)
            """, 
                product_id, store_id, 
                f"{product_data['product_name']} {product_data['brand']}", 
                '[' + ','.join(['0.1'] * 1536) + ']'  # മോക് എംബെഡിംഗ്
            )
        
        # സെമാന്റിക് സെർച്ച് ടെസ്റ്റ് ചെയ്യുക
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
        
        # സ്കീമ ഇൻട്രോസ്പെക്ഷൻ ടെസ്റ്റ് ചെയ്യുക
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
        
        # ടെസ്റ്റ് കസ്റ്റമറും ഉൽപ്പന്നവും സൃഷ്ടിക്കുക
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
        
        # ടെസ്റ്റ് ട്രാൻസാക്ഷൻ സൃഷ്ടിക്കുക
        transaction_id = await db_connection.fetchval("""
            INSERT INTO retail.sales_transactions (
                store_id, customer_id, transaction_date, total_amount, 
                subtotal, tax_amount, transaction_type
            ) VALUES ($1, $2, $3, $4, $5, $6, $7)
            RETURNING transaction_id
        """, store_id, customer_id, datetime.now(), 107.99, 99.99, 8.00, 'sale')
        
        # ട്രാൻസാക്ഷൻ ഐറ്റം സൃഷ്ടിക്കുക
        await db_connection.execute("""
            INSERT INTO retail.sales_transaction_items (
                transaction_id, product_id, quantity, unit_price, total_price
            ) VALUES ($1, $2, $3, $4, $5)
        """, transaction_id, product_id, 1, 99.99, 99.99)
        
        # ദൈനംദിന വിൽപ്പന വിശകലനം ടെസ്റ്റ് ചെയ്യുക
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
        
        # പല സ്റ്റോറുകളും സൃഷ്ടിക്കുക
        stores = ['test_seattle', 'test_redmond', 'test_bellevue']
        
        for store_id in stores:
            await TestDataHelper.create_test_store(db_connection, store_id)
            
            # ഓരോ സ്റ്റോറിലും കസ്റ്റമർ സൃഷ്ടിക്കുക
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # ഓരോ സ്റ്റോറും തങ്ങളുടെ സ്വന്തം ഡാറ്റ മാത്രമേ കാണൂ എന്നത് ടെസ്റ്റ് ചെയ്യുക
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
        
        # അസാധുവായ കണക്ഷൻ ഉപയോഗിച്ച് ഡാറ്റാബേസ് പരാജയം അനുകരിക്കുക
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
        
        # ആവശ്യമായ പാരാമീറ്റർ കാണുന്നില്ല
        result = await test_mcp_server.execute_tool(
            'semantic_search_products',
            {'query': 'test query'}  # സ്റ്റോർ_ഐഡി കാണുന്നില്ല
        )
        
        assert result['success'] is False
        assert 'store_id is required' in result['error'].lower()
        
        # പാരാമീറ്റർ തരം അസാധുവാണ്
        result = await test_mcp_server.execute_tool(
            'semantic_search_products',
            {
                'query': 'test query',
                'store_id': 'test_store',
                'limit': 'invalid'  # ഇത് പൂർണ്ണസംഖ്യയായിരിക്കണം
            }
        )
        
        assert result['success'] is False
    
    async def test_sql_injection_prevention(self, test_mcp_server, db_connection):
        """Test that SQL injection attempts are blocked."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # SQL ഇൻജക്ഷൻ ശ്രമം
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

## 📊 പ്രകടന ടെസ്റ്റിംഗ്

### ലോഡ് ടെസ്റ്റിംഗ് ഫ്രെയിംവർക്ക്

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
        
        # ടെസ്റ്റ് ഡാറ്റ സൃഷ്ടിക്കുക
        for i in range(100):
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # ടെസ്റ്റ് സീനാരിയോകൾ നിർവചിക്കുക
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
        
        # സമകാലിക എക്സിക്യൂഷനുകൾ നടത്തുക
        concurrent_tasks = 20
        tasks = [execute_tool_scenario() for _ in range(concurrent_tasks)]
        
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        total_time = time.time() - start_time
        
        # ഫലങ്ങൾ വിശകലനം ചെയ്യുക
        successful_executions = [r for r in results if r['success']]
        execution_times = [r['execution_time'] for r in successful_executions]
        
        assert len(successful_executions) == concurrent_tasks
        assert statistics.mean(execution_times) < 1.0  # ശരാശരി 1 സെക്കൻഡിന് താഴെ
        assert max(execution_times) < 5.0  # 5 സെക്കൻഡിന് മുകളിൽ എക്സിക്യൂഷൻ ഇല്ല
        assert total_time < 10.0  # എല്ലാ എക്സിക്യൂഷനുകളും 10 സെക്കൻഡിന് താഴെ
        
        print(f"Concurrent execution stats:")
        print(f"  Total time: {total_time:.2f}s")
        print(f"  Average execution time: {statistics.mean(execution_times):.3f}s")
        print(f"  Max execution time: {max(execution_times):.3f}s")
        print(f"  Min execution time: {min(execution_times):.3f}s")
    
    async def test_database_query_performance(self, test_mcp_server, db_connection):
        """Test database query performance with large datasets."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # വലിയ ഡാറ്റാസെറ്റ് സൃഷ്ടിക്കുക
        print("Creating test dataset...")
        for i in range(1000):
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # വിവിധ ക്വറി പാറ്റേണുകൾ പരീക്ഷിക്കുക
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
        
        # മോക് എംബെഡിംഗ് മാനേജറുമായി പരീക്ഷിക്കുക (യഥാർത്ഥ API കോൾസ് ഇല്ല)
        embedder = ProductEmbedder(test_mcp_server.db_provider)
        embedder.embedding_manager = test_mcp_server.embedding_manager
        
        # ബാച്ച് എംബെഡിംഗ് ജനറേഷൻ പരീക്ഷിക്കുക
        test_texts = [f"Test product {i} description" for i in range(100)]
        
        start_time = time.time()
        embeddings = await embedder.embedding_manager.generate_embeddings_batch(test_texts)
        batch_time = time.time() - start_time
        
        assert len(embeddings) == 100
        assert batch_time < 5.0  # മോക്സുകളോടെ 5 സെക്കൻഡിനുള്ളിൽ പൂർത്തിയാകണം
        
        print(f"Batch embedding generation (100 items): {batch_time:.3f}s")
        print(f"Average per embedding: {batch_time/100:.4f}s")
    
    @pytest.mark.slow
    async def test_memory_usage(self, test_mcp_server, db_connection):
        """Test memory usage under load."""
        
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024 / 1024  # എംബി
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # വലിയ ഡാറ്റാസെറ്റ് സൃഷ്ടിക്കുക
        for i in range(500):
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # പല ഓപ്പറേഷനുകളും നടത്തുക
        for i in range(50):
            await test_mcp_server.execute_tool(
                'execute_sales_query',
                {
                    'query_type': 'custom',
                    'store_id': store_id,
                    'query': 'SELECT * FROM retail.customers LIMIT 100'
                }
            )
        
        final_memory = process.memory_info().rss / 1024 / 1024  # എംബി
        memory_increase = final_memory - initial_memory
        
        # മെമ്മറി വർധനവ് യുക്തിസഹമായിരിക്കണം (ഈ ടെസ്റ്റിനായി 100MB ന് താഴെ)
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
        
        # വ്യത്യസ്ത ഡാറ്റാ വലുപ്പങ്ങളുമായി പരീക്ഷിക്കുക
        data_sizes = [100, 500, 1000, 2000]
        response_times = []
        
        for size in data_sizes:
            # നിലവിലുള്ള ഡാറ്റ ക്ലിയർ ചെയ്യുക
            await db_connection.execute("DELETE FROM retail.customers WHERE store_id = $1", store_id)
            
            # നിർദ്ദിഷ്ട വലുപ്പത്തിലുള്ള ഡാറ്റാസെറ്റ് സൃഷ്ടിക്കുക
            for i in range(size):
                await TestDataHelper.create_test_customer(db_connection, store_id)
            
            # ക്വറി സമയം അളക്കുക
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
        
        # പ്രതികരണ സമയം യുക്തിസഹമായി വർധിക്കണം (എക്സ്പൊണൻഷ്യൽ അല്ല)
        # ലളിതമായ ക്വറി കണക്കുകൾ വലിയ ഡാറ്റാസെറ്റുകളിലും വേഗത്തിൽ തുടരണം
        for time_val in response_times:
            assert time_val < 1.0  # എല്ലാ ക്വറികളും 1 സെക്കൻഡിന് താഴെ
```

## 🔍 ഡീബഗ്ഗിംഗ് ടൂളുകൾ

### ആധുനിക ഡീബഗ്ഗിംഗ് ഫ്രെയിംവർക്ക്

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
            
            # വിജയം
            execution_time = time.time() - start_time
            trace_info.update({
                'status': 'completed',
                'execution_time': execution_time
            })
            
            logger.debug(f"Completed trace: {trace_id} in {execution_time:.3f}s")
            
        except Exception as e:
            # പിശക്
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
            # പൂർത്തിയായ ട്രേസ് സംഭരിക്കുക
            self.debug_logs.append(trace_info.copy())
            del self.active_traces[trace_id]
            
            # ഡീബഗ് ലോഗ് വലുപ്പം പരിധിയിടുക
            if len(self.debug_logs) > 1000:
                self.debug_logs = self.debug_logs[-500:]
    
    async def debug_tool_execution(self, tool_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Debug tool execution with comprehensive logging."""
        
        async with self.trace_execution(f"tool_execution_{tool_name}", {'parameters': parameters}) as trace:
            
            # മുൻകൂർ നിർവഹണ പരിശോധന
            validation_result = await self._validate_tool_parameters(tool_name, parameters)
            trace['validation'] = validation_result
            
            if not validation_result['valid']:
                return {
                    'success': False,
                    'error': f"Parameter validation failed: {validation_result['errors']}",
                    'debug_info': trace
                }
            
            # ഡാറ്റാബേസ് കണക്ഷൻ പരിശോധന
            db_health = await self._check_database_health()
            trace['database_health'] = db_health
            
            # നിരീക്ഷണത്തോടെ ടൂൾ പ്രവർത്തിപ്പിക്കുക
            try:
                tool_instance = self.server.get_tool(tool_name)
                if not tool_instance:
                    return {
                        'success': False,
                        'error': f"Tool '{tool_name}' not found",
                        'debug_info': trace
                    }
                
                # പ്രവർത്തന സമയത്ത് വിഭവ ഉപയോഗം നിരീക്ഷിക്കുക
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
        
        # പ്രവർത്തന സമയങ്ങൾ വിശകലനം ചെയ്യുക
        execution_times = {}
        error_rates = {}
        memory_usage = {}
        
        for log_entry in self.debug_logs[-100:]:  # അവസാന 100 എൻട്രികൾ
            operation = log_entry['operation']
            
            # പ്രവർത്തന സമയം വിശകലനം
            if 'execution_time' in log_entry:
                if operation not in execution_times:
                    execution_times[operation] = []
                execution_times[operation].append(log_entry['execution_time'])
            
            # പിശക് നിരക്ക് വിശകലനം
            if operation not in error_rates:
                error_rates[operation] = {'total': 0, 'errors': 0}
            
            error_rates[operation]['total'] += 1
            if log_entry['status'] == 'error':
                error_rates[operation]['errors'] += 1
            
            # മെമ്മറി ഉപയോഗം വിശകലനം
            if 'memory_used_mb' in log_entry:
                if operation not in memory_usage:
                    memory_usage[operation] = []
                memory_usage[operation].append(log_entry['memory_used_mb'])
        
        # സ്ഥിതിവിവരക്കണക്കുകൾ കണക്കാക്കുക
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
        
        # തടസ്സങ്ങൾ തിരിച്ചറിയുക
        bottlenecks = []
        
        for operation, stats in performance_stats.items():
            if stats['avg_execution_time'] > 2.0:  # മന്ദഗതിയിലുള്ള പ്രവർത്തനങ്ങൾ
                bottlenecks.append({
                    'type': 'slow_execution',
                    'operation': operation,
                    'avg_time': stats['avg_execution_time']
                })
            
            if stats['error_rate'] > 5.0:  # ഉയർന്ന പിശക് നിരക്ക്
                bottlenecks.append({
                    'type': 'high_error_rate',
                    'operation': operation,
                    'error_rate': stats['error_rate']
                })
            
            if stats['avg_memory_usage'] > 100:  # ഉയർന്ന മെമ്മറി ഉപയോഗം
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
            
            # അടിസ്ഥാന പരിശോധന (ഉത്പാദനത്തിൽ jsonschema ലൈബ്രറി ഉപയോഗിക്കുക)
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

# നേരിട്ട് ഉപയോഗിക്കാൻ ഡീബഗ് ടൂൾ
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

## 🎯 പ്രധാന പഠനങ്ങൾ

ഈ ലാബ് പൂർത്തിയാക്കിയ ശേഷം, നിങ്ങൾക്കുണ്ടാകേണ്ടത്:

✅ **സമഗ്ര ടെസ്റ്റിംഗ് ഫ്രെയിംവർക്ക്**: എല്ലാ ഘടകങ്ങൾക്കും യൂണിറ്റ്, ഇന്റഗ്രേഷൻ, പ്രകടന ടെസ്റ്റുകൾ  
✅ **ആധുനിക ഡീബഗ്ഗിംഗ് ടൂളുകൾ**: എക്സിക്യൂഷൻ ട്രേസിംഗ് ഉള്ള സങ്കീർണ്ണ ഡീബഗ്ഗിംഗ് ഉപകരണങ്ങൾ  
✅ **പ്രകടന സ്ഥിരീകരണം**: ലോഡ് ടെസ്റ്റിംഗ്, സ്കെയിലബിലിറ്റി വിശകലന ശേഷി  
✅ **സുരക്ഷാ ടെസ്റ്റിംഗ്**: SQL ഇൻജക്ഷൻ തടയൽ, RLS സ്ഥിരീകരണം  
✅ **നിരീക്ഷണ ഇന്റഗ്രേഷൻ**: പ്രകടന മെട്രിക്‌സ്, ബോട്ടിൽനെക്ക് വിശകലനം  
✅ **CI/CD റെഡി**: തുടർച്ചയായ ഇന്റഗ്രേഷനായി ഓട്ടോമേറ്റഡ് ടെസ്റ്റിംഗ് വർക്ക്‌ഫ്ലോകൾ  

## 🚀 അടുത്തത് എന്താണ്

**[Lab 09: VS Code Integration](../09-VS-Code/README.md)** തുടരണം:

- MCP സർവർ വികസനത്തിന് VS Code ക്രമീകരിക്കുക  
- VS Code-ൽ ഡീബഗ്ഗിംഗ് പരിസ്ഥിതികൾ സജ്ജമാക്കുക  
- MCP സർവർ VS Code ചാറ്റുമായി ഇന്റഗ്രേറ്റ് ചെയ്യുക  
- പൂർണ്ണ VS Code വർക്ക്‌ഫ്ലോ ടെസ്റ്റ് ചെയ്യുക  

## 📚 അധിക സ്രോതസുകൾ

### ടെസ്റ്റിംഗ് ഫ്രെയിംവർക്ക്‌സ്
- [pytest ഡോക്യുമെന്റേഷൻ](https://docs.pytest.org/) - പൈതൺ ടെസ്റ്റിംഗ് ഫ്രെയിംവർക്ക്  
- [AsyncPG Testing](https://magicstack.github.io/asyncpg/current/index.html) - അസിങ്ക്രൺ പോസ്റ്റ്‌ഗ്രെഎസ്‌ക്യുവൽ ടെസ്റ്റിംഗ്  
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/) - API ടെസ്റ്റിംഗ് മാതൃകകൾ  

### പ്രകടന ടെസ്റ്റിംഗ്
- [Load Testing Best Practices](https://docs.python.org/3/library/asyncio.html) - അസിങ്ക്രൺ പ്രകടന ടെസ്റ്റിംഗ്  
- [Database Performance Testing](https://www.postgresql.org/docs/current/performance-tips.html) - പോസ്റ്റ്‌ഗ്രെഎസ്‌ക്യുവൽ ഓപ്റ്റിമൈസേഷൻ  
- [Memory Profiling](https://docs.python.org/3/library/tracemalloc.html) - പൈതൺ മെമ്മറി വിശകലനം  

### ഡീബഗ്ഗിംഗ് ടൂളുകൾ
- [Python Debugging](https://docs.python.org/3/library/pdb.html) - പൈതൺ ഡീബഗ്ഗർ  
- [Async Debugging](https://docs.python.org/3/library/asyncio-dev.html) - അസിങ്ക്രൺ ഡീബഗ്ഗിംഗ്  
- [SQL Debugging](https://www.postgresql.org/docs/current/runtime-config-logging.html) - പോസ്റ്റ്‌ഗ്രെഎസ്‌ക്യുവൽ ലോഗിംഗ്  

---

**മുൻപ്**: [Lab 07: Semantic Search Integration](../07-Semantic-Search/README.md)  
**അടുത്തത്**: [Lab 09: VS Code Integration](../09-VS-Code/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->