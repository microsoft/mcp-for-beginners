# การสร้างเซิร์ฟเวอร์ MCP

## 🎯 สิ่งที่คุณจะได้เรียนรู้ในห้องปฏิบัติการนี้

ห้องปฏิบัติการนี้จะช่วยให้คุณสร้างเซิร์ฟเวอร์ MCP ที่พร้อมใช้งานในระดับการผลิตโดยใช้เฟรมเวิร์ก FastMCP คุณจะได้สร้างโครงสร้างเซิร์ฟเวอร์หลัก, เชื่อมต่อฐานข้อมูล, สร้างเครื่องมือสำหรับการเข้าถึงข้อมูล และวางรากฐานสำหรับการวิเคราะห์ข้อมูลค้าปลีกที่ขับเคลื่อนด้วย AI

## ภาพรวม

เซิร์ฟเวอร์ MCP เป็นหัวใจสำคัญของโซลูชันการวิเคราะห์ข้อมูลค้าปลีกของเรา มันทำหน้าที่เป็นสะพานเชื่อมระหว่างผู้ช่วย AI และฐานข้อมูล PostgreSQL โดยให้การเข้าถึงข้อมูลธุรกิจที่ปลอดภัยและชาญฉลาดผ่านโปรโตคอลมาตรฐาน

ห้องปฏิบัติการนี้จะสอนคุณสร้างเซิร์ฟเวอร์ MCP ที่มีความแข็งแกร่งและสามารถขยายได้ตามรูปแบบและแนวปฏิบัติที่ดีที่สุดในระดับองค์กร

## วัตถุประสงค์การเรียนรู้

เมื่อจบห้องปฏิบัติการนี้ คุณจะสามารถ:

- **สร้าง** เซิร์ฟเวอร์ FastMCP ด้วยสถาปัตยกรรมและการจัดระเบียบที่เหมาะสม  
- **เชื่อมต่อ** ฐานข้อมูลด้วยการจัดการการเชื่อมต่อและการจัดการข้อผิดพลาด  
- **สร้าง** เครื่องมือ MCP สำหรับการตรวจสอบโครงสร้างฐานข้อมูลและการดำเนินการคำสั่ง  
- **ตั้งค่า** การจัดการบริบท Row Level Security  
- **เพิ่ม** ฟีเจอร์การตรวจสอบสุขภาพและการสังเกตการณ์  
- **ทดสอบ** การใช้งานเซิร์ฟเวอร์ MCP ของคุณในเครื่องและใน VS Code  

## 📁 โครงสร้างโปรเจกต์

มาดูการจัดระเบียบเซิร์ฟเวอร์ MCP กัน:

```
mcp_server/
├── __init__.py                 # Package initialization
├── config.py                   # Configuration management
├── health_check.py             # Health monitoring endpoints
├── sales_analysis.py           # Main MCP server implementation
├── sales_analysis_postgres.py  # Database integration layer
└── sales_analysis_text_embeddings.py  # AI/semantic search integration
```

## 🔧 การจัดการการตั้งค่า

### การตั้งค่าสภาพแวดล้อม (`config.py`)

เริ่มต้นด้วยการสร้างระบบการตั้งค่าที่แข็งแกร่ง:

```python
# mcp_server/config.py
"""
Configuration management for the MCP server.
Handles environment variables, validation, and defaults.
"""
import os
import logging
from typing import Optional, Dict, Any
from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)

@dataclass
class DatabaseConfig:
    """Database connection configuration."""
    host: str
    port: int
    database: str
    user: str
    password: str
    min_connections: int = 2
    max_connections: int = 10
    command_timeout: int = 30
    
    @classmethod
    def from_env(cls) -> 'DatabaseConfig':
        """Create configuration from environment variables."""
        return cls(
            host=os.getenv('POSTGRES_HOST', 'localhost'),
            port=int(os.getenv('POSTGRES_PORT', '5432')),
            database=os.getenv('POSTGRES_DB', 'zava'),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD', ''),
            min_connections=int(os.getenv('POSTGRES_MIN_CONNECTIONS', '2')),
            max_connections=int(os.getenv('POSTGRES_MAX_CONNECTIONS', '10')),
            command_timeout=int(os.getenv('POSTGRES_COMMAND_TIMEOUT', '30'))
        )
    
    def to_asyncpg_params(self) -> Dict[str, Any]:
        """Convert to asyncpg connection parameters."""
        return {
            'host': self.host,
            'port': self.port,
            'database': self.database,
            'user': self.user,
            'password': self.password,
            'command_timeout': self.command_timeout,
            'server_settings': {
                'application_name': 'zava-mcp-server',
                'jit': 'off',  # Disable JIT for stability
                'work_mem': '4MB',
                'statement_timeout': f'{self.command_timeout}s'
            }
        }

@dataclass
class AzureConfig:
    """Azure AI services configuration."""
    project_endpoint: str
    openai_endpoint: str
    embedding_model_deployment: str
    client_id: str
    client_secret: str
    tenant_id: str
    
    @classmethod
    def from_env(cls) -> 'AzureConfig':
        """Create configuration from environment variables."""
        return cls(
            project_endpoint=os.getenv('PROJECT_ENDPOINT', ''),
            openai_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
            embedding_model_deployment=os.getenv('EMBEDDING_MODEL_DEPLOYMENT_NAME', 'text-embedding-3-small'),
            client_id=os.getenv('AZURE_CLIENT_ID', ''),
            client_secret=os.getenv('AZURE_CLIENT_SECRET', ''),
            tenant_id=os.getenv('AZURE_TENANT_ID', '')
        )
    
    def is_configured(self) -> bool:
        """Check if all required Azure configuration is present."""
        return all([
            self.project_endpoint,
            self.openai_endpoint,
            self.client_id,
            self.client_secret,
            self.tenant_id
        ])

@dataclass
class ServerConfig:
    """MCP server configuration."""
    host: str = '0.0.0.0'
    port: int = 8000
    log_level: str = 'INFO'
    enable_cors: bool = True
    enable_health_check: bool = True
    applicationinsights_connection_string: Optional[str] = None
    
    @classmethod
    def from_env(cls) -> 'ServerConfig':
        """Create configuration from environment variables."""
        return cls(
            host=os.getenv('MCP_SERVER_HOST', '0.0.0.0'),
            port=int(os.getenv('MCP_SERVER_PORT', '8000')),
            log_level=os.getenv('LOG_LEVEL', 'INFO').upper(),
            enable_cors=os.getenv('ENABLE_CORS', 'true').lower() == 'true',
            enable_health_check=os.getenv('ENABLE_HEALTH_CHECK', 'true').lower() == 'true',
            applicationinsights_connection_string=os.getenv('APPLICATIONINSIGHTS_CONNECTION_STRING')
        )

class MCPServerConfig:
    """Main configuration class for the MCP server."""
    
    def __init__(self):
        self.database = DatabaseConfig.from_env()
        self.azure = AzureConfig.from_env()
        self.server = ServerConfig.from_env()
        
        # Validate configuration
        self._validate_config()
    
    def _validate_config(self):
        """Validate configuration and log warnings for missing values."""
        if not self.database.password:
            logger.warning("Database password is empty. This may cause connection issues.")
        
        if not self.azure.is_configured():
            logger.warning("Azure configuration is incomplete. AI features may not work.")
        
        logger.info(f"Configuration loaded - Database: {self.database.host}:{self.database.port}")
        logger.info(f"Server will run on {self.server.host}:{self.server.port}")

# Global configuration instance
config = MCPServerConfig()
```

### ฟีเจอร์สำคัญของการตั้งค่า

- **การโหลดตัวแปรสภาพแวดล้อม**: รองรับไฟล์ .env โดยอัตโนมัติ  
- **ความปลอดภัยของประเภทข้อมูล**: การตรวจสอบ Dataclass และคำใบ้ประเภท  
- **ค่าเริ่มต้นที่ยืดหยุ่น**: ค่าเริ่มต้นที่เหมาะสมสำหรับการพัฒนา  
- **การตรวจสอบ**: การตรวจสอบการตั้งค่าพร้อมข้อความแสดงข้อผิดพลาดที่เป็นประโยชน์  
- **ความปลอดภัย**: ค่าที่สำคัญจะมาจากตัวแปรสภาพแวดล้อมเท่านั้น  

## 🗄️ ชั้นการเชื่อมต่อฐานข้อมูล

### ผู้ให้บริการ PostgreSQL (`sales_analysis_postgres.py`)

มาสร้างชั้นการเชื่อมต่อฐานข้อมูลกัน:

```python
# mcp_server/sales_analysis_postgres.py
"""
PostgreSQL database integration for MCP server.
Handles connections, queries, and schema introspection.
"""
import asyncio
import asyncpg
import logging
from typing import Dict, Any, List, Optional, Tuple
from contextlib import asynccontextmanager
from datetime import datetime
import json

from .config import config

logger = logging.getLogger(__name__)

class PostgreSQLSchemaProvider:
    """Provides PostgreSQL database access and schema information."""
    
    def __init__(self):
        self.connection_pool: Optional[asyncpg.Pool] = None
        self.postgres_config = config.database.to_asyncpg_params()
        
    async def create_pool(self) -> None:
        """Create connection pool for database operations."""
        if self.connection_pool is None:
            try:
                self.connection_pool = await asyncpg.create_pool(
                    **self.postgres_config,
                    min_size=config.database.min_connections,
                    max_size=config.database.max_connections,
                    max_inactive_connection_lifetime=300  # 5 minutes
                )
                logger.info("Database connection pool created successfully")
            except Exception as e:
                logger.error(f"Failed to create database connection pool: {e}")
                raise
    
    async def close_pool(self) -> None:
        """Close the connection pool."""
        if self.connection_pool:
            await self.connection_pool.close()
            self.connection_pool = None
            logger.info("Database connection pool closed")
    
    @asynccontextmanager
    async def get_connection(self):
        """Get a database connection from the pool."""
        if not self.connection_pool:
            await self.create_pool()
        
        async with self.connection_pool.acquire() as connection:
            yield connection
    
    async def set_rls_context(self, connection: asyncpg.Connection, rls_user_id: str) -> None:
        """Set Row Level Security context for the connection."""
        try:
            await connection.execute(
                "SELECT set_config('app.current_rls_user_id', $1, false)",
                rls_user_id
            )
            logger.debug(f"RLS context set for user: {rls_user_id}")
        except Exception as e:
            logger.error(f"Failed to set RLS context: {e}")
            raise
    
    async def get_table_schema(self, table_name: str, rls_user_id: str) -> Dict[str, Any]:
        """Get detailed schema information for a specific table."""
        async with self.get_connection() as conn:
            await self.set_rls_context(conn, rls_user_id)
            
            # Parse schema and table name
            if '.' in table_name:
                schema_name, table_name = table_name.split('.', 1)
            else:
                schema_name = 'retail'  # Default schema
            
            # Get column information
            columns_query = """
                SELECT 
                    column_name,
                    data_type,
                    is_nullable,
                    column_default,
                    character_maximum_length,
                    numeric_precision,
                    numeric_scale,
                    ordinal_position
                FROM information_schema.columns 
                WHERE table_schema = $1 AND table_name = $2
                ORDER BY ordinal_position
            """
            
            columns = await conn.fetch(columns_query, schema_name, table_name)
            
            if not columns:
                raise ValueError(f"Table {schema_name}.{table_name} not found or not accessible")
            
            # Get foreign key relationships
            fk_query = """
                SELECT 
                    kcu.column_name,
                    ccu.table_schema AS foreign_table_schema,
                    ccu.table_name AS foreign_table_name,
                    ccu.column_name AS foreign_column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu 
                    ON tc.constraint_name = kcu.constraint_name
                JOIN information_schema.constraint_column_usage ccu 
                    ON ccu.constraint_name = tc.constraint_name
                WHERE tc.constraint_type = 'FOREIGN KEY' 
                    AND tc.table_schema = $1 
                    AND tc.table_name = $2
            """
            
            foreign_keys = await conn.fetch(fk_query, schema_name, table_name)
            
            # Get indexes
            index_query = """
                SELECT 
                    indexname,
                    indexdef
                FROM pg_indexes 
                WHERE schemaname = $1 AND tablename = $2
            """
            
            indexes = await conn.fetch(index_query, schema_name, table_name)
            
            # Format schema information
            schema_info = {
                "table_name": f"{schema_name}.{table_name}",
                "columns": [
                    {
                        "name": col["column_name"],
                        "type": col["data_type"],
                        "nullable": col["is_nullable"] == "YES",
                        "default": col["column_default"],
                        "max_length": col["character_maximum_length"],
                        "precision": col["numeric_precision"],
                        "scale": col["numeric_scale"],
                        "position": col["ordinal_position"]
                    }
                    for col in columns
                ],
                "foreign_keys": [
                    {
                        "column": fk["column_name"],
                        "references": f"{fk['foreign_table_schema']}.{fk['foreign_table_name']}.{fk['foreign_column_name']}"
                    }
                    for fk in foreign_keys
                ],
                "indexes": [
                    {
                        "name": idx["indexname"],
                        "definition": idx["indexdef"]
                    }
                    for idx in indexes
                ]
            }
            
            return schema_info
    
    async def get_multiple_table_schemas(
        self, 
        table_names: List[str], 
        rls_user_id: str
    ) -> str:
        """Get schema information for multiple tables."""
        schemas = []
        
        for table_name in table_names:
            try:
                schema = await self.get_table_schema(table_name, rls_user_id)
                schemas.append(self._format_schema_for_ai(schema))
            except Exception as e:
                logger.warning(f"Failed to get schema for {table_name}: {e}")
                schemas.append(f"Error retrieving schema for {table_name}: {str(e)}")
        
        return "\n\n".join(schemas)
    
    def _format_schema_for_ai(self, schema: Dict[str, Any]) -> str:
        """Format schema information for AI consumption."""
        table_name = schema["table_name"]
        columns = schema["columns"]
        foreign_keys = schema["foreign_keys"]
        
        # Create column definitions
        column_lines = []
        for col in columns:
            nullable = "NULL" if col["nullable"] else "NOT NULL"
            type_info = col["type"]
            
            if col["max_length"]:
                type_info += f"({col['max_length']})"
            elif col["precision"] and col["scale"]:
                type_info += f"({col['precision']},{col['scale']})"
            
            default_info = f" DEFAULT {col['default']}" if col["default"] else ""
            
            column_lines.append(f"  {col['name']} {type_info} {nullable}{default_info}")
        
        # Create foreign key information
        fk_lines = []
        for fk in foreign_keys:
            fk_lines.append(f"  {fk['column']} -> {fk['references']}")
        
        # Combine into readable format
        schema_text = f"Table: {table_name}\n"
        schema_text += "Columns:\n" + "\n".join(column_lines)
        
        if fk_lines:
            schema_text += "\n\nForeign Keys:\n" + "\n".join(fk_lines)
        
        return schema_text
    
    async def execute_query(
        self, 
        sql_query: str, 
        rls_user_id: str,
        max_rows: int = 20
    ) -> str:
        """Execute a SQL query with Row Level Security context."""
        async with self.get_connection() as conn:
            await self.set_rls_context(conn, rls_user_id)
            
            try:
                # Set a query timeout
                rows = await asyncio.wait_for(
                    conn.fetch(sql_query),
                    timeout=config.database.command_timeout
                )
                
                if not rows:
                    return "Query executed successfully. No rows returned."
                
                # Limit result set size
                limited_rows = rows[:max_rows]
                
                # Format results
                result = self._format_query_results(limited_rows, len(rows), max_rows)
                
                logger.info(f"Query executed successfully. Returned {len(limited_rows)} rows.")
                return result
                
            except asyncio.TimeoutError:
                error_msg = f"Query timeout after {config.database.command_timeout} seconds"
                logger.error(error_msg)
                raise Exception(error_msg)
            except Exception as e:
                logger.error(f"Query execution failed: {e}")
                raise
    
    def _format_query_results(
        self, 
        rows: List[asyncpg.Record], 
        total_rows: int,
        max_rows: int
    ) -> str:
        """Format query results for AI consumption."""
        if not rows:
            return "No results found."
        
        # Get column names
        columns = list(rows[0].keys())
        
        # Create header
        result_lines = [f"Results ({len(rows)} of {total_rows} rows):"]
        result_lines.append("=" * 50)
        
        # Add column headers
        header = " | ".join(columns)
        result_lines.append(header)
        result_lines.append("-" * len(header))
        
        # Add data rows
        for row in rows:
            formatted_values = []
            for col in columns:
                value = row[col]
                if value is None:
                    formatted_values.append("NULL")
                elif isinstance(value, datetime):
                    formatted_values.append(value.strftime("%Y-%m-%d %H:%M:%S"))
                elif isinstance(value, (dict, list)):
                    formatted_values.append(json.dumps(value))
                else:
                    formatted_values.append(str(value))
            
            result_lines.append(" | ".join(formatted_values))
        
        # Add truncation notice if needed
        if total_rows > max_rows:
            result_lines.append(f"\n... and {total_rows - max_rows} more rows (truncated for display)")
        
        return "\n".join(result_lines)
    
    async def get_current_utc_date(self) -> str:
        """Get current UTC date/time."""
        async with self.get_connection() as conn:
            result = await conn.fetchval("SELECT NOW() AT TIME ZONE 'UTC'")
            return result.isoformat() + "Z"
    
    async def health_check(self) -> Dict[str, Any]:
        """Perform database health check."""
        try:
            async with self.get_connection() as conn:
                # Simple connectivity test
                result = await conn.fetchval("SELECT 1")
                
                # Check pool status
                pool_info = {
                    "min_size": self.connection_pool._minsize if self.connection_pool else 0,
                    "max_size": self.connection_pool._maxsize if self.connection_pool else 0,
                    "current_size": self.connection_pool.get_size() if self.connection_pool else 0,
                    "idle_size": self.connection_pool.get_idle_size() if self.connection_pool else 0
                }
                
                return {
                    "status": "healthy",
                    "database_responsive": result == 1,
                    "pool_info": pool_info
                }
                
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e)
            }

# Global database provider instance
db_provider = PostgreSQLSchemaProvider()
```

### ฟีเจอร์สำคัญของชั้นฐานข้อมูล

- **การจัดการการเชื่อมต่อ**: การจัดการทรัพยากรอย่างมีประสิทธิภาพด้วย asyncpg  
- **การรวม RLS**: การตั้งค่าบริบท Row Level Security โดยอัตโนมัติ  
- **การตรวจสอบโครงสร้างฐานข้อมูล**: การค้นพบโครงสร้างตารางแบบไดนามิก  
- **การจัดการข้อผิดพลาด**: การจัดการข้อผิดพลาดและการบันทึกอย่างครอบคลุม  
- **การจัดรูปแบบคำสั่ง**: การจัดรูปแบบผลลัพธ์ที่เหมาะกับ AI  
- **การตรวจสอบสุขภาพ**: การตรวจสอบการเชื่อมต่อฐานข้อมูลและสถานะของพูล  

## 🔧 การสร้างเซิร์ฟเวอร์ MCP หลัก

### เซิร์ฟเวอร์ FastMCP (`sales_analysis.py`)

ตอนนี้มาสร้างเซิร์ฟเวอร์ MCP หลักกัน:

```python
# mcp_server/sales_analysis.py
"""
Main MCP server implementation for Zava Retail Sales Analysis.
Provides AI assistants with secure access to retail database.
"""
import logging
import asyncio
from typing import Dict, Any, List, Annotated
from contextlib import asynccontextmanager

from fastmcp import FastMCP, Context
from pydantic import Field

from .config import config
from .sales_analysis_postgres import db_provider
from .health_check import setup_health_endpoints

# Configure logging
logging.basicConfig(
    level=getattr(logging, config.server.log_level),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastMCP server instance
mcp = FastMCP("Zava Retail Sales Analysis")

# List of valid tables for schema access
VALID_TABLES = [
    "retail.stores",
    "retail.customers", 
    "retail.categories",
    "retail.product_types",
    "retail.products",
    "retail.orders",
    "retail.order_items",
    "retail.inventory"
]

def get_rls_user_id(ctx: Context) -> str:
    """Extract Row Level Security User ID from request context."""
    # In HTTP mode, get from headers
    if hasattr(ctx, 'headers') and ctx.headers:
        rls_user_id = ctx.headers.get("x-rls-user-id")
        if rls_user_id:
            logger.debug(f"RLS User ID from headers: {rls_user_id}")
            return rls_user_id
    
    # Default fallback for development/testing
    default_id = "00000000-0000-0000-0000-000000000000"
    logger.warning(f"No RLS User ID found, using default: {default_id}")
    return default_id

@mcp.tool()
async def get_multiple_table_schemas(
    ctx: Context,
    table_names: Annotated[List[str], Field(description="List of table names to retrieve schemas for. Valid tables: " + ", ".join(VALID_TABLES))]
) -> str:
    """
    Retrieve database schemas for multiple tables in a single request.
    
    This tool provides comprehensive schema information including:
    - Column names, types, and constraints
    - Foreign key relationships
    - Index information
    - Table structure for AI query planning
    
    Args:
        table_names: List of valid table names from the retail schema
        
    Returns:
        Formatted schema information for all requested tables
    """
    rls_user_id = get_rls_user_id(ctx)
    
    # Validate table names
    invalid_tables = [table for table in table_names if table not in VALID_TABLES]
    if invalid_tables:
        logger.warning(f"Invalid table names requested: {invalid_tables}")
        return f"Error: Invalid table names: {', '.join(invalid_tables)}. Valid tables are: {', '.join(VALID_TABLES)}"
    
    try:
        logger.info(f"Retrieving schemas for tables: {table_names} (User: {rls_user_id})")
        result = await db_provider.get_multiple_table_schemas(table_names, rls_user_id)
        return result
    except Exception as e:
        logger.error(f"Error retrieving table schemas: {e}")
        return f"Error retrieving table schemas: {e!s}"

@mcp.tool()
async def execute_sales_query(
    ctx: Context,
    postgresql_query: Annotated[str, Field(description="A well-formed PostgreSQL query to execute against the retail database. Always get table schemas first before writing queries.")]
) -> str:
    """
    Execute PostgreSQL queries against the retail sales database with Row Level Security.
    
    This tool allows AI assistants to run analytical queries on retail data including:
    - Sales performance analysis
    - Customer behavior insights  
    - Inventory management queries
    - Product performance metrics
    - Store-specific reporting
    
    Important: Row Level Security ensures users only see data they're authorized to access.
    
    Args:
        postgresql_query: SQL query to execute (automatically filtered by RLS)
        
    Returns:
        Query results formatted for AI analysis (limited to 20 rows for readability)
    """
    rls_user_id = get_rls_user_id(ctx)
    
    try:
        logger.info(f"Executing query for user: {rls_user_id}")
        logger.debug(f"Query: {postgresql_query[:100]}...")
        
        result = await db_provider.execute_query(postgresql_query, rls_user_id)
        return result
    except Exception as e:
        logger.error(f"Error executing database query: {e}")
        return f"Error executing database query: {e!s}"

@mcp.tool()
async def get_current_utc_date(ctx: Context) -> str:
    """
    Get the current UTC date and time in ISO format.
    
    Useful for time-sensitive queries and date-based analysis.
    
    Returns:
        Current UTC date/time in ISO format (YYYY-MM-DDTHH:MM:SS.fffffZ)
    """
    try:
        result = await db_provider.get_current_utc_date()
        logger.debug(f"Current UTC date retrieved: {result}")
        return result
    except Exception as e:
        logger.error(f"Error getting current UTC date: {e}")
        return f"Error getting current UTC date: {e!s}"

# Application lifecycle management
@asynccontextmanager
async def lifespan(app):
    """Manage application startup and shutdown."""
    logger.info("Starting Zava Retail MCP Server...")
    
    try:
        # Initialize database connection pool
        await db_provider.create_pool()
        logger.info("Database connection pool initialized")
        
        # Test database connectivity
        health_status = await db_provider.health_check()
        if health_status["status"] != "healthy":
            logger.error(f"Database health check failed: {health_status}")
            raise Exception("Database not healthy")
        
        logger.info("MCP Server startup complete")
        yield
        
    except Exception as e:
        logger.error(f"Startup failed: {e}")
        raise
    finally:
        # Cleanup
        logger.info("Shutting down MCP Server...")
        await db_provider.close_pool()
        logger.info("MCP Server shutdown complete")

# Configure server application
def create_app():
    """Create and configure the MCP server application."""
    
    # Get the FastMCP app instance
    app = mcp.sse_app()
    
    # Set up lifecycle management
    app.router.lifespan_context = lifespan
    
    # Add health check endpoints if enabled
    if config.server.enable_health_check:
        setup_health_endpoints(app, db_provider)
    
    # Configure CORS if enabled
    if config.server.enable_cors:
        from fastapi.middleware.cors import CORSMiddleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Configure appropriately for production
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    logger.info(f"MCP Server configured - CORS: {config.server.enable_cors}, Health: {config.server.enable_health_check}")
    
    return app

# Create the application instance
app = create_app()

# Main entry point for development
if __name__ == "__main__":
    import uvicorn
    
    logger.info(f"Starting development server on {config.server.host}:{config.server.port}")
    
    uvicorn.run(
        "sales_analysis:app",
        host=config.server.host,
        port=config.server.port,
        reload=True,
        log_level=config.server.log_level.lower()
    )
```

### ฟีเจอร์สำคัญของเซิร์ฟเวอร์ MCP

- **การลงทะเบียนเครื่องมือ**: การกำหนดเครื่องมือแบบประกาศด้วยความปลอดภัยของประเภท  
- **การจัดการบริบท RLS**: การดึงข้อมูลตัวตนผู้ใช้และการตั้งค่าบริบทโดยอัตโนมัติ  
- **การจัดการข้อผิดพลาด**: การจัดการข้อผิดพลาดอย่างครอบคลุมพร้อมข้อความที่เป็นมิตรต่อผู้ใช้  
- **การจัดการวงจรชีวิต**: การเริ่มต้น/ปิดระบบอย่างเหมาะสมพร้อมการทำความสะอาดทรัพยากร  
- **การตรวจสอบสุขภาพ**: จุดตรวจสอบสุขภาพในตัว  
- **การสนับสนุนการพัฒนา**: การโหลดซ้ำและความสามารถในการดีบัก  

## 🏥 การตรวจสอบสุขภาพ

### การใช้งานการตรวจสอบสุขภาพ (`health_check.py`)

```python
# mcp_server/health_check.py
"""
Health check endpoints for monitoring MCP server status.
"""
import logging
from typing import Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

def setup_health_endpoints(app: FastAPI, db_provider) -> None:
    """Add health check endpoints to the FastAPI application."""
    
    @app.get("/health")
    async def health_check() -> JSONResponse:
        """Basic health check endpoint."""
        return JSONResponse(
            status_code=200,
            content={
                "status": "healthy",
                "service": "zava-retail-mcp-server",
                "timestamp": await db_provider.get_current_utc_date()
            }
        )
    
    @app.get("/health/detailed")
    async def detailed_health_check() -> JSONResponse:
        """Detailed health check including database connectivity."""
        health_status = {
            "service": "zava-retail-mcp-server",
            "status": "healthy",
            "components": {}
        }
        
        overall_healthy = True
        
        # Check database
        try:
            db_health = await db_provider.health_check()
            health_status["components"]["database"] = db_health
            
            if db_health["status"] != "healthy":
                overall_healthy = False
                
        except Exception as e:
            health_status["components"]["database"] = {
                "status": "unhealthy",
                "error": str(e)
            }
            overall_healthy = False
        
        # Update overall status
        if not overall_healthy:
            health_status["status"] = "unhealthy"
        
        status_code = 200 if overall_healthy else 503
        
        return JSONResponse(
            status_code=status_code,
            content=health_status
        )
    
    @app.get("/health/ready")
    async def readiness_check() -> JSONResponse:
        """Kubernetes readiness probe endpoint."""
        try:
            # Test critical functionality
            db_health = await db_provider.health_check()
            
            if db_health["status"] != "healthy":
                raise HTTPException(status_code=503, detail="Database not ready")
            
            return JSONResponse(
                status_code=200,
                content={"status": "ready"}
            )
            
        except Exception as e:
            logger.error(f"Readiness check failed: {e}")
            raise HTTPException(status_code=503, detail="Service not ready")
    
    @app.get("/health/live")
    async def liveness_check() -> JSONResponse:
        """Kubernetes liveness probe endpoint."""
        return JSONResponse(
            status_code=200,
            content={"status": "alive"}
        )
    
    logger.info("Health check endpoints configured")
```

## 🧪 การทดสอบเซิร์ฟเวอร์ MCP ของคุณ

### การทดสอบในเครื่อง

1. **เริ่มเซิร์ฟเวอร์ MCP**:
   ```bash
   # Activate virtual environment
   source mcp-env/bin/activate  # macOS/Linux
   # mcp-env\Scripts\activate   # Windows
   
   # Start server
   cd mcp_server
   python sales_analysis.py
   ```

2. **ทดสอบจุดตรวจสอบสุขภาพ**:
   ```bash
   # Basic health check
   curl http://localhost:8000/health
   
   # Detailed health check
   curl http://localhost:8000/health/detailed
   ```

3. **ทดสอบเครื่องมือ MCP**:
   ```bash
   # List available tools
   curl -X POST http://localhost:8000/mcp \
     -H "Content-Type: application/json" \
     -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
     -d '{"method": "tools/list", "params": {}}'
   
   # Get table schemas
   curl -X POST http://localhost:8000/mcp \
     -H "Content-Type: application/json" \
     -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
     -d '{
       "method": "tools/call",
       "params": {
         "name": "get_multiple_table_schemas",
         "arguments": {
           "table_names": ["retail.stores", "retail.products"]
         }
       }
     }'
   ```

### การทดสอบการรวมใน VS Code

1. **ตั้งค่า VS Code MCP**:
   ```json
   // .vscode/mcp.json
   {
       "servers": {
           "zava-retail-test": {
               "url": "http://127.0.0.1:8000/mcp",
               "type": "http",
               "headers": {"x-rls-user-id": "00000000-0000-0000-0000-000000000000"}
           }
       }
   }
   ```

2. **ทดสอบใน AI Chat**:
   - เปิด VS Code AI Chat  
   - พิมพ์ `#zava` และเลือกเซิร์ฟเวอร์ของคุณ  
   - ถาม: "มีตารางอะไรบ้าง?"  
   - ถาม: "แสดงร้านค้า 5 อันดับแรกตามจำนวนคำสั่งซื้อ"  

### การทดสอบหน่วย

สร้างการทดสอบหน่วยที่ครอบคลุม:

```python
# tests/test_mcp_server.py
import pytest
import asyncio
from mcp_server.sales_analysis_postgres import PostgreSQLSchemaProvider
from mcp_server.config import config

@pytest.mark.asyncio
async def test_database_connection():
    """Test database connectivity."""
    db = PostgreSQLSchemaProvider()
    
    try:
        await db.create_pool()
        health = await db.health_check()
        assert health["status"] == "healthy"
    finally:
        await db.close_pool()

@pytest.mark.asyncio
async def test_table_schema_retrieval():
    """Test table schema retrieval."""
    db = PostgreSQLSchemaProvider()
    
    try:
        await db.create_pool()
        schema = await db.get_table_schema("retail.stores", "00000000-0000-0000-0000-000000000000")
        
        assert schema["table_name"] == "retail.stores"
        assert len(schema["columns"]) > 0
        
    finally:
        await db.close_pool()

@pytest.mark.asyncio
async def test_query_execution():
    """Test query execution with RLS."""
    db = PostgreSQLSchemaProvider()
    
    try:
        await db.create_pool()
        result = await db.execute_query(
            "SELECT COUNT(*) as store_count FROM retail.stores",
            "00000000-0000-0000-0000-000000000000"
        )
        
        assert "store_count" in result
        
    finally:
        await db.close_pool()
```

## 🎯 สิ่งที่คุณควรได้รับ

หลังจากจบห้องปฏิบัติการนี้ คุณควรมี:

✅ **เซิร์ฟเวอร์ MCP ที่ใช้งานได้**: เซิร์ฟเวอร์ FastMCP พร้อมการเชื่อมต่อฐานข้อมูล  
✅ **การจัดการการตั้งค่า**: การตั้งค่าที่แข็งแกร่งตามสภาพแวดล้อม  
✅ **ชั้นฐานข้อมูล**: การเชื่อมต่อ PostgreSQL พร้อมการจัดการการเชื่อมต่อ  
✅ **เครื่องมือ MCP**: เครื่องมือสำหรับการตรวจสอบโครงสร้างและการดำเนินการคำสั่ง  
✅ **การรวม RLS**: การจัดการบริบท Row Level Security  
✅ **การตรวจสอบสุขภาพ**: จุดตรวจสอบสุขภาพที่ครอบคลุม  
✅ **กลยุทธ์การทดสอบ**: การทดสอบในเครื่องและการรวมใน VS Code  

## 🚀 สิ่งที่ต้องทำต่อไป

ดำเนินการต่อกับ **[Lab 06: การพัฒนาเครื่องมือ](../06-Tools/README.md)** เพื่อ:

- ขยายชุดเครื่องมือ MCP ของคุณ  
- ใช้รูปแบบคำสั่งขั้นสูง  
- เพิ่มการตรวจสอบและการแปลงข้อมูล  
- สร้างเครื่องมือวิเคราะห์เฉพาะทาง  

## 📚 แหล่งข้อมูลเพิ่มเติม

### เฟรมเวิร์ก FastMCP
- [เอกสาร FastMCP](https://github.com/modelcontextprotocol/python-sdk) - คู่มือ FastMCP อย่างเป็นทางการ  
- [สเปค MCP](https://modelcontextprotocol.io/docs/) - สเปคโปรโตคอล  
- [คู่มือการพัฒนาเครื่องมือ](https://modelcontextprotocol.io/docs/tools/) - การสร้างเครื่องมือ MCP  

### การเชื่อมต่อฐานข้อมูล
- [เอกสาร asyncpg](https://magicstack.github.io/asyncpg/current/) - ไดรเวอร์ PostgreSQL แบบ async  
- [แนวปฏิบัติที่ดีที่สุดสำหรับการจัดการการเชื่อมต่อ](https://www.postgresql.org/docs/current/runtime-config-connection.html) - การปรับแต่ง PostgreSQL  
- [คู่มือ Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - การใช้งาน RLS  

### รูปแบบ FastAPI
- [เอกสาร FastAPI](https://fastapi.tiangolo.com/) - อ้างอิงเฟรมเวิร์กเว็บ  
- [การฉีดพึ่งพา](https://fastapi.tiangolo.com/tutorial/dependencies/) - รูปแบบ FastAPI  
- [งานเบื้องหลัง](https://fastapi.tiangolo.com/tutorial/background-tasks/) - การจัดการงานแบบ async  

---

**ถัดไป**: พร้อมที่จะขยายเครื่องมือของคุณ? ดำเนินการต่อกับ [Lab 06: การพัฒนาเครื่องมือ](../06-Tools/README.md)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้