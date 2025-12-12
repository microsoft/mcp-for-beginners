<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ad02c1223d7861292651ffce2f52bb28",
  "translation_date": "2025-12-11T14:31:15+00:00",
  "source_file": "11-MCPServerHandsOnLabs/08-Testing/README.md",
  "language_code": "kn"
}
-->
# ಪರೀಕ್ಷೆ ಮತ್ತು ಡಿಬಗಿಂಗ್

## 🎯 ಈ ಪ್ರಯೋಗಶಾಲೆ ಏನು ಒಳಗೊಂಡಿದೆ

ಈ ಪ್ರಯೋಗಶಾಲೆ ಉತ್ಪಾದನಾ ಪರಿಸರಗಳಲ್ಲಿ MCP ಸರ್ವರ್‌ಗಳ ಪರೀಕ್ಷೆ ಮತ್ತು ಡಿಬಗಿಂಗ್ ಕುರಿತು ಸಮಗ್ರ ಮಾರ್ಗದರ್ಶನವನ್ನು ಒದಗಿಸುತ್ತದೆ. ನೀವು ಬಲವಾದ ಪರೀಕ್ಷಾ ತಂತ್ರಗಳನ್ನು ಜಾರಿಗೆ ತರುವುದನ್ನು, ಸಂಕೀರ್ಣ ಸಮಸ್ಯೆಗಳನ್ನು ಡಿಬಗ್ ಮಾಡುವುದನ್ನು ಮತ್ತು ನಿಮ್ಮ MCP ಸರ್ವರ್ ವಿವಿಧ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ ವಿಶ್ವಾಸಾರ್ಹವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವುದನ್ನು ಕಲಿಯುತ್ತೀರಿ.

## ಅವಲೋಕನ

MCP ಸರ್ವರ್‌ಗಳ ಪರೀಕ್ಷೆಗೆ ಘಟಕ ಪರೀಕ್ಷೆಗಳು, ಸಂಯೋಜನೆ ಪರೀಕ್ಷೆಗಳು, ಕಾರ್ಯಕ್ಷಮತೆ ಮಾನ್ಯತೆ ಮತ್ತು ನೈಜ ಜಗತ್ತಿನ ದೃಶ್ಯಪಟ ಪರೀಕ್ಷೆಗಳನ್ನು ಒಳಗೊಂಡ ಬಹುಮಟ್ಟದ ವಿಧಾನ ಅಗತ್ಯವಿದೆ. ಈ ಪ್ರಯೋಗಶಾಲೆ ಅಭಿವೃದ್ಧಿಯಿಂದ ಉತ್ಪಾದನಾ ಮೇಲ್ವಿಚಾರಣೆಯವರೆಗೆ ಸಂಪೂರ್ಣ ಪರೀಕ್ಷಾ ಜೀವನಚಕ್ರವನ್ನು ಒಳಗೊಂಡಿದೆ.

ನಮ್ಮ ಪರೀಕ್ಷಾ ತಂತ್ರವು ವಿಶ್ವಾಸಾರ್ಹತೆ, ಭದ್ರತೆ ಮತ್ತು ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಒತ್ತಾಯಿಸುತ್ತದೆ, ನಿಮ್ಮ MCP ಸರ್ವರ್ ಉತ್ಪಾದನಾ ಕೆಲಸಭಾರಗಳನ್ನು ನಿರ್ವಹಿಸುವಾಗ ಡೇಟಾ ಅಖಂಡತೆ ಮತ್ತು ಬಳಕೆದಾರ ಅನುಭವ ಗುಣಮಟ್ಟವನ್ನು ಕಾಪಾಡುತ್ತದೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪ್ರಯೋಗಶಾಲೆಯ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- **ಸಂಪೂರ್ಣ ಘಟಕ ಮತ್ತು ಸಂಯೋಜನೆ ಪರೀಕ್ಷಾ ಸ್ಯೂಟ್‌ಗಳನ್ನು ಜಾರಿಗೆ ತರುವುದನ್ನು**  
- **MCP ಉಪಕರಣಗಳು ಮತ್ತು ಡೇಟಾಬೇಸ್ ಕಾರ್ಯಾಚರಣೆಗಳಿಗೆ ಪರಿಣಾಮಕಾರಿ ಪರೀಕ್ಷಾ ತಂತ್ರಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸುವುದನ್ನು**  
- **ಅತ್ಯಾಧುನಿಕ ಡಿಬಗಿಂಗ್ ತಂತ್ರಗಳನ್ನು ಬಳಸಿ ಸಂಕೀರ್ಣ ಸಮಸ್ಯೆಗಳನ್ನು ಡಿಬಗ್ ಮಾಡುವುದನ್ನು**  
- **ನೈಜ ಪರೀಕ್ಷಾ ದೃಶ್ಯಪಟಗಳೊಂದಿಗೆ ಲೋಡ್ ಅಡಿಯಲ್ಲಿ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಮಾನ್ಯಗೊಳಿಸುವುದನ್ನು**  
- **ಪ್ರಭಾವಶೀಲ ಎಚ್ಚರಿಕೆ ಮತ್ತು ಅವಲೋಕನದೊಂದಿಗೆ ಉತ್ಪಾದನಾ ವ್ಯವಸ್ಥೆಗಳನ್ನು ಮೇಲ್ವಿಚಾರಿಸುವುದನ್ನು**  
- **ನಿರಂತರ ಸಂಯೋಜನೆಗಾಗಿ ಪರೀಕ್ಷಾ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುವುದನ್ನು**

## 🧪 ಪರೀಕ್ಷಾ ವಾಸ್ತುಶಿಲ್ಪ

### ಪರೀಕ್ಷಾ ತಂತ್ರ ಅವಲೋಕನ

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

### ಪರೀಕ್ಷಾ ಪರಿಸರ ಸ್ಥಾಪನೆ

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

# ಪರೀಕ್ಷಾ ಸಂರಚನೆ
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
    
    # ಪರೀಕ್ಷಾ ಡೇಟಾಬೇಸ್ ಸಂಪರ್ಕವನ್ನು ರಚಿಸಿ
    sys_conn = await asyncpg.connect(
        "postgresql://postgres:password@localhost:5432/postgres"
    )
    
    try:
        # ಪರೀಕ್ಷಾ ಡೇಟಾಬೇಸ್ ರಚಿಸಿ
        await sys_conn.execute("DROP DATABASE IF EXISTS test_retail_db")
        await sys_conn.execute("CREATE DATABASE test_retail_db")
    finally:
        await sys_conn.close()
    
    # ಪರೀಕ್ಷಾ ಡೇಟಾಬೇಸ್‌ಗೆ ಸಂಪರ್ಕಿಸಿ ಮತ್ತು ಸ್ಕೀಮಾ ಸಿದ್ಧಪಡಿಸಿ
    test_conn = await asyncpg.connect(TEST_DATABASE_URL)
    
    try:
        # ಸ್ಕೀಮಾ ಲೋಡ್ ಮಾಡಿ
        schema_sql = await load_sql_file("../scripts/create_schema.sql")
        await test_conn.execute(schema_sql)
        
        # ಮಾದರಿ ಡೇಟಾ ಲೋಡ್ ಮಾಡಿ
        sample_data_sql = await load_sql_file("../scripts/sample_data.sql")
        await test_conn.execute(sample_data_sql)
        
        yield test_conn
        
    finally:
        await test_conn.close()
        
        # ಪರೀಕ್ಷಾ ಡೇಟಾಬೇಸ್ ಅನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ
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
    
    # ಪರೀಕ್ಷಾ ವಿಭಜನೆಗಾಗಿ ವ್ಯವಹಾರ ಪ್ರಾರಂಭಿಸಿ
    tx = conn.transaction()
    await tx.start()
    
    try:
        yield conn
    finally:
        # ಪರೀಕ್ಷಾ ವಿಭಜನೆ ಕಾಯ್ದುಕೊಳ್ಳಲು ವ್ಯವಹಾರವನ್ನು ರದ್ದುಗೊಳಿಸಿ
        await tx.rollback()
        await conn.close()

@pytest.fixture
async def mock_embedding_manager():
    """Mock embedding manager for testing without Azure OpenAI calls."""
    
    mock_manager = AsyncMock()
    
    # ಎम्बೆಡ್ಡಿಂಗ್ ಉತ್ಪಾದನೆಯನ್ನು ನಕಲಿ ಮಾಡಿ
    mock_manager.generate_embedding.return_value = [0.1] * 1536  # ಎम्बೆಡ್ಡಿಂಗ್ ನಕಲಿ ಮಾಡಿ
    mock_manager.generate_embeddings_batch.return_value = [[0.1] * 1536] * 10
    
    # ಪ್ರಾರಂಭಿಕರಣ ನಕಲಿ ಮಾಡಿ
    mock_manager.initialize.return_value = None
    mock_manager.cleanup.return_value = None
    
    return mock_manager

@pytest.fixture
async def test_mcp_server(db_connection, mock_embedding_manager):
    """Set up test MCP server instance."""
    
    from mcp_server.server import MCPServer
    from mcp_server.database import DatabaseProvider
    from mcp_server.config import Config
    
    # ಪರೀಕ್ಷಾ ಸಂರಚನೆ ರಚಿಸಿ
    config = Config()
    config.database.connection_string = TEST_DATABASE_URL
    config.server.enable_debug = True
    
    # ಡೇಟಾಬೇಸ್ ಪೂರೈಕೆದಾರ ರಚಿಸಿ
    db_provider = DatabaseProvider(config.database.connection_string)
    await db_provider.initialize()
    
    # MCP ಸರ್ವರ್ ರಚಿಸಿ
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

# ಪರೀಕ್ಷಾ ಡೇಟಾ ಸಹಾಯಕರು
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

## 🔧 ಘಟಕ ಪರೀಕ್ಷೆ

### ಉಪಕರಣ ಪರೀಕ್ಷಾ ಫ್ರೇಮ್ವರ್ಕ್

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
        
        # ಪರೀಕ್ಷಾ ಡೇಟಾವನ್ನು ಸಜ್ಜುಗೊಳಿಸಿ
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        customer_id = await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # ಪರೀಕ್ಷಾ ವ್ಯವಹಾರವನ್ನು ರಚಿಸಿ
        await db_connection.execute("""
            INSERT INTO retail.sales_transactions (
                store_id, customer_id, transaction_date, total_amount, transaction_type
            ) VALUES ($1, $2, $3, $4, $5)
        """, store_id, customer_id, datetime.now(), 150.00, 'sale')
        
        # ಸಾಧನವನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ
        result = await sales_tool.execute(
            query_type='daily_sales',
            store_id=store_id,
            start_date=(datetime.now() - timedelta(days=7)).date(),
            end_date=datetime.now().date()
        )
        
        # ಫಲಿತಾಂಶಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
        assert result.success is True
        assert len(result.data) > 0
        assert 'total_revenue' in result.data[0]
        assert result.metadata['query_type'] == 'daily_sales'
    
    async def test_custom_query_validation(self, sales_tool, db_connection):
        """Test custom query validation."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # ಮಾನ್ಯವಾದ ಪ್ರಶ್ನೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ
        valid_query = "SELECT COUNT(*) as customer_count FROM retail.customers"
        result = await sales_tool.execute(
            query_type='custom',
            store_id=store_id,
            query=valid_query
        )
        
        assert result.success is True
        
        # ಅಮಾನ್ಯವಾದ ಪ್ರಶ್ನೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ (ನಿರೋಧಿಸಬೇಕು)
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
        
        # ಎರಡು ವಿಭಿನ್ನ ಅಂಗಡಿಗಳನ್ನು ರಚಿಸಿ
        store1 = 'test_store1'
        store2 = 'test_store2'
        
        await TestDataHelper.create_test_store(db_connection, store1)
        await TestDataHelper.create_test_store(db_connection, store2)
        
        # ವಿಭಿನ್ನ ಅಂಗಡಿಗಳಲ್ಲಿ ಗ್ರಾಹಕರನ್ನು ರಚಿಸಿ
        customer1 = await TestDataHelper.create_test_customer(db_connection, store1)
        customer2 = await TestDataHelper.create_test_customer(db_connection, store2)
        
        # ಅಂಗಡಿ1 ನಿಂದ ಪ್ರಶ್ನೆ ಅಂಗಡಿ1 ಡೇಟಾವನ್ನು ಮಾತ್ರ ನೋಡಬೇಕು
        result1 = await sales_tool.execute(
            query_type='custom',
            store_id=store1,
            query="SELECT COUNT(*) as count FROM retail.customers"
        )
        
        # ಅಂಗಡಿ2 ನಿಂದ ಪ್ರಶ್ನೆ ಅಂಗಡಿ2 ಡೇಟಾವನ್ನು ಮಾತ್ರ ನೋಡಬೇಕು
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
        
        # ಪರೀಕ್ಷಾ ಉತ್ಪನ್ನಗಳನ್ನು ರಚಿಸಿ
        for product_data in sample_products:
            product_id = await TestDataHelper.create_test_product(
                db_connection, store_id, product_data
            )
            
            # ನಕಲಿ ಎम्बೆಡ್ಡಿಂಗ್ ರಚಿಸಿ
            await db_connection.execute("""
                INSERT INTO retail.product_embeddings (
                    product_id, store_id, embedding_text, embedding
                ) VALUES ($1, $2, $3, $4)
            """, 
                product_id, store_id, 
                f"{product_data['product_name']} {product_data['brand']}", 
                '[0.1,0.2,0.3]'  # ನಕಲಿ ಎम्बೆಡ್ಡಿಂಗ್
            )
        
        # ಹುಡುಕಾಟವನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ
        result = await search_tool.execute(
            query='running shoes',
            store_id=store_id,
            limit=10,
            similarity_threshold=0.0
        )
        
        # ಫಲಿತಾಂಶಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
        assert result.success is True
        assert len(result.data) > 0
        assert 'similarity_score' in result.data[0]
        assert result.metadata['search_type'] == 'semantic'
    
    async def test_search_parameter_validation(self, search_tool):
        """Test search parameter validation."""
        
        # ಕಳೆದುಹೋಗಿದ ಪ್ರಶ್ನೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ
        result = await search_tool.execute(store_id='test_store')
        assert result.success is False
        assert 'query is required' in result.error.lower()
        
        # ಕಳೆದುಹೋಗಿದ store_id ಅನ್ನು ಪರೀಕ್ಷಿಸಿ
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

### ಡೇಟಾಬೇಸ್ ಪರೀಕ್ಷೆ

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
        
        # ಸ್ಟೋರ್ ಸಂದರ್ಭವನ್ನು ಸೆಟ್ ಮಾಡಿ
        await db_connection.execute("SELECT retail.set_store_context($1)", store_id)
        
        # ಸಂದರ್ಭವು ಸೆಟ್ ಆಗಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
        current_store = await db_connection.fetchval(
            "SELECT current_setting('app.current_store_id', true)"
        )
        
        assert current_store == store_id
    
    async def test_customer_isolation(self, db_connection):
        """Test that customers are properly isolated by store."""
        
        # ಎರಡು ಸ್ಟೋರ್‌ಗಳನ್ನು ರಚಿಸಿ
        store1 = 'test_store1'
        store2 = 'test_store2'
        
        await TestDataHelper.create_test_store(db_connection, store1)
        await TestDataHelper.create_test_store(db_connection, store2)
        
        # ವಿಭಿನ್ನ ಸ್ಟೋರ್‌ಗಳಲ್ಲಿ ಗ್ರಾಹಕರನ್ನು ರಚಿಸಿ
        await TestDataHelper.create_test_customer(db_connection, store1)
        await TestDataHelper.create_test_customer(db_connection, store2)
        
        # ಸಂದರ್ಭವನ್ನು store1 ಗೆ ಸೆಟ್ ಮಾಡಿ ಮತ್ತು ಗ್ರಾಹಕರನ್ನು ಎಣಿಸಿ
        await db_connection.execute("SELECT retail.set_store_context($1)", store1)
        store1_count = await db_connection.fetchval("SELECT COUNT(*) FROM retail.customers")
        
        # ಸಂದರ್ಭವನ್ನು store2 ಗೆ ಸೆಟ್ ಮಾಡಿ ಮತ್ತು ಗ್ರಾಹಕರನ್ನು ಎಣಿಸಿ
        await db_connection.execute("SELECT retail.set_store_context($1)", store2)
        store2_count = await db_connection.fetchval("SELECT COUNT(*) FROM retail.customers")
        
        # ಪ್ರತಿ ಸ್ಟೋರ್ ತನ್ನದೇ ಗ್ರಾಹಕರನ್ನು ಮಾತ್ರ ನೋಡಬೇಕು
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
        
        # ಸ್ಟೋರ್ ಸಂದರ್ಭವನ್ನು ಸೆಟ್ ಮಾಡಿ
        await db_connection.execute("SELECT retail.set_store_context($1)", store_id)
        
        # ವಿಭಿನ್ನ ಸ್ಟೋರ್‌ಗೆ ಗ್ರಾಹಕರನ್ನು ಸೇರಿಸಲು ಪ್ರಯತ್ನಿಸಿ (ವಿಫಲವಾಗಬೇಕು)
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
        
        # ಬಹು ಸಂಪರ್ಕಗಳನ್ನು ಪಡೆಯಿರಿ
        conn1 = await db_provider.get_connection()
        conn2 = await db_provider.get_connection()
        
        assert conn1 is not None
        assert conn2 is not None
        assert conn1 != conn2  # ವಿಭಿನ್ನ ಸಂಪರ್ಕ ವಸ್ತುಗಳಾಗಿರಬೇಕು
        
        # ಸಂಪರ್ಕಗಳನ್ನು ಬಿಡುಗಡೆ ಮಾಡಿ
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
        
        # ಇದು ಸಂಪರ್ಕ ಪುನರುದ್ಧಾರ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಪರೀಕ್ಷಿಸುತ್ತದೆ
        # ನಿಜವಾದ ಪರೀಕ್ಷೆಯಲ್ಲಿ, ನೀವು ತಾತ್ಕಾಲಿಕವಾಗಿ ಸಂಪರ್ಕವನ್ನು ಮುರಿಯಬಹುದು
        # ಮತ್ತು ಪೂಲ್ ಪುನರುದ್ಧಾರವಾಗುವುದನ್ನು ಪರಿಶೀಲಿಸಿ
        
        # ಈಗಿಗೆ, ಆರೋಗ್ಯ ಪರಿಶೀಲನೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ ಎಂದು ಮಾತ್ರ ಪರಿಶೀಲಿಸಿ
        health_status = await db_provider.health_check()
        assert health_status['status'] == 'healthy'
```

## 🚀 ಸಂಯೋಜನೆ ಪರೀಕ್ಷೆ

### ಅಂತ್ಯದಿಂದ ಅಂತ್ಯವರೆಗೆ ಕಾರ್ಯಪ್ರವಾಹ ಪರೀಕ್ಷೆ

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
        
        # ಎम्बೆಡ್ಡಿಂಗ್‌ಗಳೊಂದಿಗೆ ಪರೀಕ್ಷಾ ಉತ್ಪನ್ನಗಳನ್ನು ರಚಿಸಿ
        for product_data in sample_products:
            product_id = await TestDataHelper.create_test_product(
                db_connection, store_id, product_data
            )
            
            # ಉತ್ಪನ್ನಕ್ಕೆ ಎम्बೆಡ್ಡಿಂಗ್ ರಚಿಸಿ
            await db_connection.execute("""
                INSERT INTO retail.product_embeddings (
                    product_id, store_id, embedding_text, embedding
                ) VALUES ($1, $2, $3, $4)
            """, 
                product_id, store_id, 
                f"{product_data['product_name']} {product_data['brand']}", 
                '[' + ','.join(['0.1'] * 1536) + ']'  # ನಕಲಿ ಎम्बೆಡ್ಡಿಂಗ್
            )
        
        # ಅರ್ಥಪೂರ್ಣ ಹುಡುಕಾಟವನ್ನು ಪರೀಕ್ಷಿಸಿ
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
        
        # ಸ್ಕೀಮಾ ಇಂಟ್ರೋಸ್ಪೆಕ್ಷನ್ ಪರೀಕ್ಷಿಸಿ
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
        
        # ಪರೀಕ್ಷಾ ಗ್ರಾಹಕ ಮತ್ತು ಉತ್ಪನ್ನವನ್ನು ರಚಿಸಿ
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
        
        # ಪರೀಕ್ಷಾ ವ್ಯವಹಾರವನ್ನು ರಚಿಸಿ
        transaction_id = await db_connection.fetchval("""
            INSERT INTO retail.sales_transactions (
                store_id, customer_id, transaction_date, total_amount, 
                subtotal, tax_amount, transaction_type
            ) VALUES ($1, $2, $3, $4, $5, $6, $7)
            RETURNING transaction_id
        """, store_id, customer_id, datetime.now(), 107.99, 99.99, 8.00, 'sale')
        
        # ವ್ಯವಹಾರ ಐಟಂ ರಚಿಸಿ
        await db_connection.execute("""
            INSERT INTO retail.sales_transaction_items (
                transaction_id, product_id, quantity, unit_price, total_price
            ) VALUES ($1, $2, $3, $4, $5)
        """, transaction_id, product_id, 1, 99.99, 99.99)
        
        # ದೈನಂದಿನ ಮಾರಾಟ ವಿಶ್ಲೇಷಣೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ
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
        
        # ಹಲವಾರು ಅಂಗಡಿಗಳನ್ನು ರಚಿಸಿ
        stores = ['test_seattle', 'test_redmond', 'test_bellevue']
        
        for store_id in stores:
            await TestDataHelper.create_test_store(db_connection, store_id)
            
            # ಪ್ರತಿ ಅಂಗಡಿಯಲ್ಲಿ ಗ್ರಾಹಕ ರಚಿಸಿ
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # ಪ್ರತಿ ಅಂಗಡಿ ತನ್ನದೇ ಡೇಟಾವನ್ನು ಮಾತ್ರ ನೋಡುತ್ತದೆ ಎಂದು ಪರೀಕ್ಷಿಸಿ
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
        
        # ಅಮಾನ್ಯ ಸಂಪರ್ಕವನ್ನು ಬಳಸಿ ಡೇಟಾಬೇಸ್ ವೈಫಲ್ಯವನ್ನು ಅನುಕರಿಸಿ
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
        
        # ಅಗತ್ಯವಾದ ಪರಿಮಾಣ ಕಳೆದುಹೋಗಿದೆ
        result = await test_mcp_server.execute_tool(
            'semantic_search_products',
            {'query': 'test query'}  # store_id ಕಳೆದುಹೋಗಿದೆ
        )
        
        assert result['success'] is False
        assert 'store_id is required' in result['error'].lower()
        
        # ಅಮಾನ್ಯ ಪರಿಮಾಣ ಪ್ರಕಾರ
        result = await test_mcp_server.execute_tool(
            'semantic_search_products',
            {
                'query': 'test query',
                'store_id': 'test_store',
                'limit': 'invalid'  # ಪೂರ್ಣಾಂಕವಾಗಿರಬೇಕು
            }
        )
        
        assert result['success'] is False
    
    async def test_sql_injection_prevention(self, test_mcp_server, db_connection):
        """Test that SQL injection attempts are blocked."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # SQL ಇಂಜೆಕ್ಷನ್ ಪ್ರಯತ್ನಿಸಿ
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

## 📊 ಕಾರ್ಯಕ್ಷಮತೆ ಪರೀಕ್ಷೆ

### ಲೋಡ್ ಪರೀಕ್ಷಾ ಫ್ರೇಮ್ವರ್ಕ್

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
        
        # ಪರೀಕ್ಷಾ ಡೇಟಾವನ್ನು ರಚಿಸಿ
        for i in range(100):
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # ಪರೀಕ್ಷಾ ದೃಶ್ಯಾವಳಿಗಳನ್ನು ನಿರ್ಧರಿಸಿ
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
        
        # ಸಮಕಾಲೀನ ಕಾರ್ಯಾಚರಣೆಗಳನ್ನು ನಡೆಸಿ
        concurrent_tasks = 20
        tasks = [execute_tool_scenario() for _ in range(concurrent_tasks)]
        
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        total_time = time.time() - start_time
        
        # ಫಲಿತಾಂಶಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ
        successful_executions = [r for r in results if r['success']]
        execution_times = [r['execution_time'] for r in successful_executions]
        
        assert len(successful_executions) == concurrent_tasks
        assert statistics.mean(execution_times) < 1.0  # ಸರಾಸರಿ 1 ಸೆಕೆಂಡಿನೊಳಗೆ
        assert max(execution_times) < 5.0  # 5 ಸೆಕೆಂಡುಗಳಿಗಿಂತ ಹೆಚ್ಚು ಕಾರ್ಯಾಚರಣೆ ಇಲ್ಲ
        assert total_time < 10.0  # ಎಲ್ಲಾ ಕಾರ್ಯಾಚರಣೆಗಳು 10 ಸೆಕೆಂಡುಗಳೊಳಗೆ
        
        print(f"Concurrent execution stats:")
        print(f"  Total time: {total_time:.2f}s")
        print(f"  Average execution time: {statistics.mean(execution_times):.3f}s")
        print(f"  Max execution time: {max(execution_times):.3f}s")
        print(f"  Min execution time: {min(execution_times):.3f}s")
    
    async def test_database_query_performance(self, test_mcp_server, db_connection):
        """Test database query performance with large datasets."""
        
        store_id = 'test_seattle'
        await TestDataHelper.create_test_store(db_connection, store_id)
        
        # ದೊಡ್ಡ ಡೇಟಾಸೆಟ್ ರಚಿಸಿ
        print("Creating test dataset...")
        for i in range(1000):
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # ವಿವಿಧ ಪ್ರಶ್ನಾ ಮಾದರಿಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ
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
        
        # ನಕಲಿ ಎम्बೆಡ್ಡಿಂಗ್ ಮ್ಯಾನೇಜರ್‌ನೊಂದಿಗೆ ಪರೀಕ್ಷಿಸಿ (ಯಥಾರ್ಥ API ಕರೆಗಳಿಲ್ಲ)
        embedder = ProductEmbedder(test_mcp_server.db_provider)
        embedder.embedding_manager = test_mcp_server.embedding_manager
        
        # ಬ್ಯಾಚ್ ಎम्बೆಡ್ಡಿಂಗ್ ಉತ್ಪಾದನೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ
        test_texts = [f"Test product {i} description" for i in range(100)]
        
        start_time = time.time()
        embeddings = await embedder.embedding_manager.generate_embeddings_batch(test_texts)
        batch_time = time.time() - start_time
        
        assert len(embeddings) == 100
        assert batch_time < 5.0  # ನಕಲಿಗಳೊಂದಿಗೆ 5 ಸೆಕೆಂಡುಗಳೊಳಗೆ ಪೂರ್ಣಗೊಳ್ಳಬೇಕು
        
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
        
        # ಸಾಕಷ್ಟು ಡೇಟಾಸೆಟ್ ರಚಿಸಿ
        for i in range(500):
            await TestDataHelper.create_test_customer(db_connection, store_id)
        
        # ಅನೇಕ ಕಾರ್ಯಾಚರಣೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ
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
        
        # ಮೆಮೊರಿ ವೃದ್ಧಿ ಯುಕ್ತವಾಗಿರಬೇಕು (ಈ ಪರೀಕ್ಷೆಗೆ 100MB ಕ್ಕಿಂತ ಕಡಿಮೆ)
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
        
        # ವಿಭಿನ್ನ ಡೇಟಾ ಗಾತ್ರಗಳೊಂದಿಗೆ ಪರೀಕ್ಷಿಸಿ
        data_sizes = [100, 500, 1000, 2000]
        response_times = []
        
        for size in data_sizes:
            # ಇತ್ತೀಚಿನ ಡೇಟಾವನ್ನು ತೆರವುಗೊಳಿಸಿ
            await db_connection.execute("DELETE FROM retail.customers WHERE store_id = $1", store_id)
            
            # ನಿರ್ದಿಷ್ಟ ಗಾತ್ರದ ಡೇಟಾಸೆಟ್ ರಚಿಸಿ
            for i in range(size):
                await TestDataHelper.create_test_customer(db_connection, store_id)
            
            # ಪ್ರಶ್ನೆ ಸಮಯವನ್ನು ಅಳೆಯಿರಿ
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
        
        # ಪ್ರತಿಕ್ರಿಯೆ ಸಮಯ ಯುಕ್ತವಾಗಿ ವೃದ್ಧಿಯಾಗಬೇಕು (ವ್ಯವಸ್ಥಿತವಾಗಿ ಅಲ್ಲ)
        # ಸರಳ ಎಣಿಕೆ ಪ್ರಶ್ನೆಗಳು ದೊಡ್ಡ ಡೇಟಾಸೆಟ್‌ಗಳೊಂದಿಗೆ ಕೂಡ ವೇಗವಾಗಿ ಇರಬೇಕು
        for time_val in response_times:
            assert time_val < 1.0  # ಎಲ್ಲಾ ಪ್ರಶ್ನೆಗಳು 1 ಸೆಕೆಂಡಿನೊಳಗೆ
```

## 🔍 ಡಿಬಗಿಂಗ್ ಉಪಕರಣಗಳು

### ಅತ್ಯಾಧುನಿಕ ಡಿಬಗಿಂಗ್ ಫ್ರೇಮ್ವರ್ಕ್

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
            
            # ಯಶಸ್ಸು
            execution_time = time.time() - start_time
            trace_info.update({
                'status': 'completed',
                'execution_time': execution_time
            })
            
            logger.debug(f"Completed trace: {trace_id} in {execution_time:.3f}s")
            
        except Exception as e:
            # ದೋಷ
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
            # ಪೂರ್ಣಗೊಂಡ ಟ್ರೇಸ್ ಸಂಗ್ರಹಿಸಿ
            self.debug_logs.append(trace_info.copy())
            del self.active_traces[trace_id]
            
            # ಡಿಬಗ್ ಲಾಗ್ ಗಾತ್ರವನ್ನು ಮಿತಿಗೊಳಿಸಿ
            if len(self.debug_logs) > 1000:
                self.debug_logs = self.debug_logs[-500:]
    
    async def debug_tool_execution(self, tool_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Debug tool execution with comprehensive logging."""
        
        async with self.trace_execution(f"tool_execution_{tool_name}", {'parameters': parameters}) as trace:
            
            # ಪೂರ್ವ-ಕಾರ್ಯನಿರ್ವಹಣಾ ಪರಿಶೀಲನೆ
            validation_result = await self._validate_tool_parameters(tool_name, parameters)
            trace['validation'] = validation_result
            
            if not validation_result['valid']:
                return {
                    'success': False,
                    'error': f"Parameter validation failed: {validation_result['errors']}",
                    'debug_info': trace
                }
            
            # ಡೇಟಾಬೇಸ್ ಸಂಪರ್ಕ ಪರಿಶೀಲನೆ
            db_health = await self._check_database_health()
            trace['database_health'] = db_health
            
            # ಮೇಲ್ವಿಚಾರಣೆಯೊಂದಿಗೆ ಸಾಧನವನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ
            try:
                tool_instance = self.server.get_tool(tool_name)
                if not tool_instance:
                    return {
                        'success': False,
                        'error': f"Tool '{tool_name}' not found",
                        'debug_info': trace
                    }
                
                # ಕಾರ್ಯನಿರ್ವಹಣೆಯ ಸಮಯದಲ್ಲಿ ಸಂಪನ್ಮೂಲ ಬಳಕೆಯನ್ನು ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ
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
        
        # ಕಾರ್ಯನಿರ್ವಹಣಾ ಸಮಯಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ
        execution_times = {}
        error_rates = {}
        memory_usage = {}
        
        for log_entry in self.debug_logs[-100:]:  # ಕೊನೆಯ 100 ದಾಖಲೆಗಳು
            operation = log_entry['operation']
            
            # ಕಾರ್ಯನಿರ್ವಹಣಾ ಸಮಯ ವಿಶ್ಲೇಷಣೆ
            if 'execution_time' in log_entry:
                if operation not in execution_times:
                    execution_times[operation] = []
                execution_times[operation].append(log_entry['execution_time'])
            
            # ದೋಷ ದರ ವಿಶ್ಲೇಷಣೆ
            if operation not in error_rates:
                error_rates[operation] = {'total': 0, 'errors': 0}
            
            error_rates[operation]['total'] += 1
            if log_entry['status'] == 'error':
                error_rates[operation]['errors'] += 1
            
            # ಮೆಮೊರಿ ಬಳಕೆ ವಿಶ್ಲೇಷಣೆ
            if 'memory_used_mb' in log_entry:
                if operation not in memory_usage:
                    memory_usage[operation] = []
                memory_usage[operation].append(log_entry['memory_used_mb'])
        
        # ಅಂಕಿಅಂಶಗಳನ್ನು ಲೆಕ್ಕಹಾಕಿ
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
        
        # ಅಡ್ಡಿ ಗುರುತಿಸಿ
        bottlenecks = []
        
        for operation, stats in performance_stats.items():
            if stats['avg_execution_time'] > 2.0:  # ನಿಧಾನ ಕಾರ್ಯಗಳು
                bottlenecks.append({
                    'type': 'slow_execution',
                    'operation': operation,
                    'avg_time': stats['avg_execution_time']
                })
            
            if stats['error_rate'] > 5.0:  # ಹೆಚ್ಚಿನ ದೋಷ ದರ
                bottlenecks.append({
                    'type': 'high_error_rate',
                    'operation': operation,
                    'error_rate': stats['error_rate']
                })
            
            if stats['avg_memory_usage'] > 100:  # ಹೆಚ್ಚಿನ ಮೆಮೊರಿ ಬಳಕೆ
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
            
            # ಮೂಲಭೂತ ಪರಿಶೀಲನೆ (ಉತ್ಪಾದನೆಯಲ್ಲಿ, jsonschema ಗ್ರಂಥಾಲಯವನ್ನು ಬಳಸಿ)
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

# ನೇರ ಬಳಕೆಗೆ ಡಿಬಗ್ ಸಾಧನ
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

## 🎯 ಪ್ರಮುಖ ಪಾಠಗಳು

ಈ ಪ್ರಯೋಗಶಾಲೆಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಹೊಂದಿರಬೇಕು:

✅ **ಸಂಪೂರ್ಣ ಪರೀಕ್ಷಾ ಫ್ರೇಮ್ವರ್ಕ್**: ಎಲ್ಲಾ ಘಟಕಗಳು, ಸಂಯೋಜನೆ ಮತ್ತು ಕಾರ್ಯಕ್ಷಮತೆ ಪರೀಕ್ಷೆಗಳು  
✅ **ಅತ್ಯಾಧುನಿಕ ಡಿಬಗಿಂಗ್ ಉಪಕರಣಗಳು**: ಕಾರ್ಯನಿರ್ವಹಣಾ ಟ್ರೇಸಿಂಗ್ ಹೊಂದಿರುವ ಸುಧಾರಿತ ಡಿಬಗಿಂಗ್ ಉಪಕರಣಗಳು  
✅ **ಕಾರ್ಯಕ್ಷಮತೆ ಮಾನ್ಯತೆ**: ಲೋಡ್ ಪರೀಕ್ಷೆ ಮತ್ತು ವಿಸ್ತರಣಾ ವಿಶ್ಲೇಷಣೆ ಸಾಮರ್ಥ್ಯಗಳು  
✅ **ಭದ್ರತಾ ಪರೀಕ್ಷೆ**: SQL ಇಂಜೆಕ್ಷನ್ ತಡೆ ಮತ್ತು RLS ಮಾನ್ಯತೆ  
✅ **ಮೇಲ್ವಿಚಾರಣೆಯ ಸಂಯೋಜನೆ**: ಕಾರ್ಯಕ್ಷಮತೆ ಅಂಶಗಳು ಮತ್ತು ಬಾಟಲ್‌ನೆಕ್ ವಿಶ್ಲೇಷಣೆ  
✅ **CI/CD ಸಿದ್ಧತೆ**: ನಿರಂತರ ಸಂಯೋಜನೆಗಾಗಿ ಸ್ವಯಂಚಾಲಿತ ಪರೀಕ್ಷಾ ಕಾರ್ಯಪ್ರವಾಹಗಳು  

## 🚀 ಮುಂದಿನದು ಏನು

**[ಪ್ರಯೋಗಶಾಲೆ 09: VS ಕೋಡ್ ಸಂಯೋಜನೆ](../09-VS-Code/README.md)** ಜೊತೆಗೆ ಮುಂದುವರಿಯಿರಿ:

- MCP ಸರ್ವರ್ ಅಭಿವೃದ್ಧಿಗಾಗಿ VS ಕೋಡ್ ಅನ್ನು ಸಂರಚಿಸುವುದು  
- VS ಕೋಡ್‌ನಲ್ಲಿ ಡಿಬಗಿಂಗ್ ಪರಿಸರಗಳನ್ನು ಸ್ಥಾಪಿಸುವುದು  
- MCP ಸರ್ವರ್ ಅನ್ನು VS ಕೋಡ್ ಚಾಟ್ ಜೊತೆಗೆ ಸಂಯೋಜಿಸುವುದು  
- ಸಂಪೂರ್ಣ VS ಕೋಡ್ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಪರೀಕ್ಷಿಸುವುದು  

## 📚 ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

### ಪರೀಕ್ಷಾ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು
- [pytest ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://docs.pytest.org/) - ಪೈಥಾನ್ ಪರೀಕ್ಷಾ ಫ್ರೇಮ್ವರ್ಕ್  
- [AsyncPG ಪರೀಕ್ಷೆ](https://magicstack.github.io/asyncpg/current/index.html) - ಅಸಿಂಕ್ ಪೋಸ್ಟ್‌ಗ್ರೆSQL ಪರೀಕ್ಷೆ  
- [FastAPI ಪರೀಕ್ಷೆ](https://fastapi.tiangolo.com/tutorial/testing/) - API ಪರೀಕ್ಷಾ ಮಾದರಿಗಳು  

### ಕಾರ್ಯಕ್ಷಮತೆ ಪರೀಕ್ಷೆ
- [ಲೋಡ್ ಪರೀಕ್ಷೆಯ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು](https://docs.python.org/3/library/asyncio.html) - ಅಸಿಂಕ್ ಕಾರ್ಯಕ್ಷಮತೆ ಪರೀಕ್ಷೆ  
- [ಡೇಟಾಬೇಸ್ ಕಾರ್ಯಕ್ಷಮತೆ ಪರೀಕ್ಷೆ](https://www.postgresql.org/docs/current/performance-tips.html) - ಪೋಸ್ಟ್‌ಗ್ರೆSQL ಆಪ್ಟಿಮೈಜೆಷನ್  
- [ಮೆಮೊರಿ ಪ್ರೊಫೈಲಿಂಗ್](https://docs.python.org/3/library/tracemalloc.html) - ಪೈಥಾನ್ ಮೆಮೊರಿ ವಿಶ್ಲೇಷಣೆ  

### ಡಿಬಗಿಂಗ್ ಉಪಕರಣಗಳು
- [ಪೈಥಾನ್ ಡಿಬಗಿಂಗ್](https://docs.python.org/3/library/pdb.html) - ಪೈಥಾನ್ ಡಿಬಗರ್  
- [ಅಸಿಂಕ್ ಡಿಬಗಿಂಗ್](https://docs.python.org/3/library/asyncio-dev.html) - ಅಸಿಂಕ್ ಡಿಬಗಿಂಗ್  
- [SQL ಡಿಬಗಿಂಗ್](https://www.postgresql.org/docs/current/runtime-config-logging.html) - ಪೋಸ್ಟ್‌ಗ್ರೆSQL ಲಾಗಿಂಗ್  

---

**ಹಿಂದಿನದು**: [ಪ್ರಯೋಗಶಾಲೆ 07: ಸೆಮ್ಯಾಂಟಿಕ್ ಸರ್ಚ್ ಸಂಯೋಜನೆ](../07-Semantic-Search/README.md)  
**ಮುಂದಿನದು**: [ಪ್ರಯೋಗಶಾಲೆ 09: VS ಕೋಡ್ ಸಂಯೋಜನೆ](../09-VS-Code/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->