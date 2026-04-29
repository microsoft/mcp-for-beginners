# ការអនុវត្ត MCP Server

## 🎯 ការព្រាបអ្វីដែលកម្មវិធីពិសេសនេះគ្របដណ្តប់

កម្មវិធីនេះផ្តល់ការបណ្តុះបណ្តាលជាក់ស្តែងសម្រាប់អនុវត្តម៉ាសុីន MCP សក្តានុពលប្រើប្រាស់បានក្នុងការផលិតដោយប្រើ FastMCP framework។ អ្នកនឹងសាងសង់រចនាសម្ព័ន្ធម៉ាសុីន MCP មូលដ្ឋាន អនុវត្តការតភ្ជាប់​ទិន្នន័យ បង្កើតឧបករណ៍សម្រាប់ចូលដំណើរការ​ទិន្នន័យ និងបង្កើតមូលដ្ឋានសម្រាប់វិភាគលក់រាយដែលថែមទាំងគ្រប់គ្រងដោយ AI។

## ទិដ្ឋភាពទូទៅ

ម៉ាសុីន MCP គឺជាបេះដូងនៃដំណោះស្រាយវិភាគលក់រាយរបស់យើង។ វាធ្វើជា​ស្ពាន់ភ្ជាប់រវាងជំនួយក AI និងមូលដ្ឋានទិន្នន័យ PostgreSQL ផ្តល់នូវការចូលដំណើរការដោយសុវត្ថិភាព និងមានភាពឆ្លាតវៃទៅលើទិន្នន័យអាជីវកម្មតាមរយៈប្រព័ន្ធស្តង់ដារ។

កម្មវិធីនេះបង្រៀនអ្នកបង្កើតម៉ាសុីន MCP ដែលរឹងមាំ និងអាចរីកលូតលាស់បានដោយអនុវត្តគំរូស្ថាបត្យកម្ម និងអនុវិទ្យាល្អបំផុតរបស់ក្រុមហ៊ុន។

## គោលបំណងសិក្សា

នៅចុងកម្មវិធីនេះ អ្នកនឹងអាច៖

- **សាងសង់** ម៉ាសុីន FastMCP ជាមួយរចនាសម្ព័ន្ធនិងដំណើរការដែលត្រឹមត្រូវ
- **អនុវត្ត** ការតភ្ជាប់​ទិន្នន័យជាមួយ​ការ​គ្រប់គ្រង​ការតភ្ជាប់ និងការដោះស្រាយកំហុស
- **បង្កើត** ឧបករណ៍ MCP សម្រាប់ការស៊ើបអង្កេត​ស្កីម៉ា​មូលដ្ឋាន​ទិន្នន័យ និងការប្រតិបត្តិការសំណួរ
- **កំណត់​រចនាសម្ព័ន្ធ** គ្រប់គ្រងបរិបទសុវត្ថិភាពជួរដេក (Row Level Security)
- **បន្ថែម** លក្ខណៈមើលឃើញសុខភាព និងការត្រួតពិនិត្យ
- **សាកល្បង** ការអនុវត្ត MCP Server ដោយផ្ទាល់ និងជាមួយ VS Code

## 📁 រចនាសម្ព័ន្ធគម្រោង

គួរតែពិនិត្យមើលអង្គភាពម៉ាសុីន MCP៖

```
mcp_server/
├── __init__.py                 # Package initialization
├── config.py                   # Configuration management
├── health_check.py             # Health monitoring endpoints
├── sales_analysis.py           # Main MCP server implementation
├── sales_analysis_postgres.py  # Database integration layer
└── sales_analysis_text_embeddings.py  # AI/semantic search integration
```

## 🔧 ការគ្រប់គ្រងការកំណត់

### ការកំណត់បរិស្ថាន (`config.py`)

ជំហានដំបូង បង្កើតប្រព័ន្ធកំណត់ដែលរឹងមាំ៖

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

# ដំណើរការបង្កលអចលនាពីឯកសារ .env
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
                'jit': 'off',  # បង្កប់ JIT សម្រាប់ស្ថិរភាព
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
        
        # ផ្ទៀងផ្ទាត់ការកំណត់រចនាសម្ព័ន្ធ
        self._validate_config()
    
    def _validate_config(self):
        """Validate configuration and log warnings for missing values."""
        if not self.database.password:
            logger.warning("Database password is empty. This may cause connection issues.")
        
        if not self.azure.is_configured():
            logger.warning("Azure configuration is incomplete. AI features may not work.")
        
        logger.info(f"Configuration loaded - Database: {self.database.host}:{self.database.port}")
        logger.info(f"Server will run on {self.server.host}:{self.server.port}")

# ជាឧទាហរណ៍កំណត់រចនាសម្ព័ន្ធសកល
config = MCPServerConfig()
```

### លក្ខណៈសំខាន់នៃការកំណត់

- **ការតភ្ជាប់អថេរបរិស្ថាន**៖ គាំទ្រឯកសារ .env ដោយស្វ័យប្រវត្តិ
- **សុវត្ថិភាពប្រភេទ**៖ ការផ្ទៀងផ្ទាត់ dataclass និងកំណត់ប្រភេទ
- **លំនាំដើមបត់បែនបាន**៖ លំនាំដើមបន្ថែមសម្រាប់ការអភិវឌ្ឍន៍
- **ការផ្ទៀងផ្ទាត់**៖ ការផ្ទៀងផ្ទាត់ការកំណត់ជាមួយសារ​កំហុសមានប្រយោជន៍
- **សុវត្ថិភាព**៖ តម្លៃសំខាន់ៗទទួលបានតែពីអថេរបរិស្ថាន

## 🗄️ ស្រទាប់​បញ្ចូល​មូលដ្ឋាន​ទិន្នន័យ

### អ្នកផ្ដល់សេវា PostgreSQL (`sales_analysis_postgres.py`)

ចាប់ផ្ដើមអនុវត្តស្រទាប់បញ្ចូលមូលដ្ឋានទិន្នន័យ៖

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
                    max_inactive_connection_lifetime=300  # ៥ នាទី
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
            
            # វាយបញ្ចូល schema និងឈ្មោះតារាង
            if '.' in table_name:
                schema_name, table_name = table_name.split('.', 1)
            else:
                schema_name = 'retail'  # Schema មូលដ្ឋាន
            
            # ទទួលព័ត៌មានជួរឈរ
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
            
            # ទទួលទំនាក់ទំនងកូនសោ
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
            
            # ទទួល indexes
            index_query = """
                SELECT 
                    indexname,
                    indexdef
                FROM pg_indexes 
                WHERE schemaname = $1 AND tablename = $2
            """
            
            indexes = await conn.fetch(index_query, schema_name, table_name)
            
            # រៀបចំព័ត៌មាន schema
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
        
        # បង្កើតការបរិយាយជួរឈរ
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
        
        # បង្កើតព័ត៌មានកូនសោ
        fk_lines = []
        for fk in foreign_keys:
            fk_lines.append(f"  {fk['column']} -> {fk['references']}")
        
        # បញ្ចូលជា ទ្រង់ទ្រាយអានបាន
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
                # កំណត់ពេលវេលាខ្សែសំណួរ
                rows = await asyncio.wait_for(
                    conn.fetch(sql_query),
                    timeout=config.database.command_timeout
                )
                
                if not rows:
                    return "Query executed successfully. No rows returned."
                
                # ដាក់កំណត់ទំហំលទ្ធផល
                limited_rows = rows[:max_rows]
                
                # រៀបចំលទ្ធផល
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
        
        # ទទួលឈ្មោះជួរឈរ
        columns = list(rows[0].keys())
        
        # បង្កើត header
        result_lines = [f"Results ({len(rows)} of {total_rows} rows):"]
        result_lines.append("=" * 50)
        
        # បន្ថែម header ជួរឈរ
        header = " | ".join(columns)
        result_lines.append(header)
        result_lines.append("-" * len(header))
        
        # បន្ថែមមួកទិន្នន័យ
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
        
        # បន្ថែមការជូនដំណឹងកាត់បន្ថយ ប្រសិនបើត្រូវការ
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
                # សាកល្បងភ្ជាប់សាមញ្ញ
                result = await conn.fetchval("SELECT 1")
                
                # ត្រួតពិនិត្យស្ថានភាព pool
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

# តំណាងអ្នកផ្ដល់ទិន្នន័យមូលដ្ឋានទូទៅ
db_provider = PostgreSQLSchemaProvider()
```

### លក្ខណៈសំខាន់នៃស្រទាប់មូលដ្ឋានទិន្នន័យ

- **ការគ្រប់គ្រង​កម្រិត​ការតភ្ជាប់**៖ ប្រើ asyncpg ដើម្បីគ្រប់គ្រងធនធានយ៉ាងមានប្រសិទ្ធភាព
- **ការតភ្ជាប់ RLS**៖ ការកំណត់បរិបទសុវត្ថិភាពជួរដេកដោយស្វ័យប្រវត្តិ
- **ស៊ើបអង្កេតស្កីម៉ាផ្ទៃតារាង**៖ ការរកឃើញស្កីម៉ាតារាងឌីណាមិច
- **ការដោះស្រាយកំហុស**៖ ការគ្រប់គ្រងកំហុស និងកំណត់ហេតុយ៉ាងទូលំទូលាយ
- **ទ្រង់ទ្រាយសំណួរ**៖ ទ្រង់ទ្រាយលទ្ធផលឲ្យម៉ាស៊ីន AI ងាយយល់
- **ការត្រួតពិនិត្យសុខភាព**៖ ការត្រួតពិនិត្យស្តាតសេវាសមាហរណ៏និងស្ថានភាព​កម្មវិធី​ចាប់​ផ្តើម

## 🔧 ការអនុវត្ត MCP Server ដ៏សំខាន់

### ម៉ាសុីន FastMCP (`sales_analysis.py`)

ឥឡូវនេះចាប់ផ្ដើមអនុវត្តម៉ាសុីន MCP សំខាន់៖

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

# កំណត់ការចុះបញ្ជីត្រឹមត្រូវ
logging.basicConfig(
    level=getattr(logging, config.server.log_level),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# បង្កើតអ实例 FastMCP server
mcp = FastMCP("Zava Retail Sales Analysis")

# បញ្ជីតារាងដែលត្រឹមត្រូវសម្រាប់ចូលប្រើ schema
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
    # ក្នុងរបៀប HTTP ស្រាវ​យក​ពីក្បាល​សំណើ
    if hasattr(ctx, 'headers') and ctx.headers:
        rls_user_id = ctx.headers.get("x-rls-user-id")
        if rls_user_id:
            logger.debug(f"RLS User ID from headers: {rls_user_id}")
            return rls_user_id
    
    # ជម្រើសលំនាំដើម​សម្រាប់ការអភិវឌ្ឍន៍/សាកល្បង
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
    
    # ត្រួតពិនិត្យឈ្មោះតារាង
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

# គ្រប់គ្រងជីវចលកម្មកម្មវិធី
@asynccontextmanager
async def lifespan(app):
    """Manage application startup and shutdown."""
    logger.info("Starting Zava Retail MCP Server...")
    
    try:
        # ចាប់ផ្ដើមភ្ជាប់ប្រព័ន្ធឃ្លាំងទិន្នន័យ
        await db_provider.create_pool()
        logger.info("Database connection pool initialized")
        
        # សាកល្បងការតភ្ជាប់ប្រព័ន្ធឃ្លាំងទិន្នន័យ
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
        # សម្អាត
        logger.info("Shutting down MCP Server...")
        await db_provider.close_pool()
        logger.info("MCP Server shutdown complete")

# កំណត់កម្មវិធីម៉ាស៊ីនបម្រើ
def create_app():
    """Create and configure the MCP server application."""
    
    # បញ្ជីកម្មវិធី FastMCP ចូល
    app = mcp.sse_app()
    
    # រៀបចំគ្រប់គ្រងជីវចលកម្ម
    app.router.lifespan_context = lifespan
    
    # បន្ថែមចំណុចពិនិត្យសុខភាពបើបានដំណើរការ
    if config.server.enable_health_check:
        setup_health_endpoints(app, db_provider)
    
    # កំណត់ CORS ប្រសិនបើបានដំណើរការ
    if config.server.enable_cors:
        from fastapi.middleware.cors import CORSMiddleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # កំណត់ត្រឹមត្រូវចំពោះសម្រាប់ផលិតកម្ម
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    logger.info(f"MCP Server configured - CORS: {config.server.enable_cors}, Health: {config.server.enable_health_check}")
    
    return app

# បង្កើត实例កម្មវិធី
app = create_app()

# ច្រកចូលសំខាន់សម្រាប់ការអភិវឌ្ឍន៍
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

### លក្ខណៈសំខាន់នៃម៉ាសុីន MCP Server

- **ការចុះបញ្ជីឧបករណ៍**៖ ការបញ្ជាក់ឧបករណ៍ដោយប្រើការទូលប្រភេទ
- **ការគ្រប់គ្រងបរិបទ RLS**៖ ការដកស្រាយអត្តសញ្ញាណអ្នកប្រើនិងកំណត់បរិបទដោយស្វ័យប្រវត្តិ
- **ការដោះស្រាយកំហុស**៖ ការគ្រប់គ្រងកំហុសពេញលេញជាមួយសារដិតដល់អ្នកប្រើ
- **ការគ្រប់គ្រងរយៈពេលប្រតិបត្តិការ**៖ ការចាប់ផ្ដើម/បិទប្រតិបត្តិការដោយមានកាកបាទធនធានត្រឹមត្រូវ
- **ការត្រួតពិនិត្យសុខភាព**៖ ចំណុចពិនិត្យ​សុខភាព​ត្រូវបានបង្ហាប់
- **គាំទ្រការអភិវឌ្ឍន៍**៖ ការផ្ទុកឡើងវិញឆាប់រហ័ស និងមុខងារបង្កើតកំហុស

## 🏥 ការត្រួតពិនិត្យសុខភាព

### ការអនុវត្តការត្រួតពិនិត្យ​សុខភាព (`health_check.py`)

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
        
        # ពិនិត្យមូលដ្ឋានទិន្នន័យ
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
        
        # បន្ទាន់ប្រសិនដល់ស្ថានភាពទូទៅ
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
            # សាកល្បងមុខងារសំខាន់ៗ
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

## 🧪 ការសាកល្បងម៉ាសុីន MCP របស់អ្នក

### ការសាកល្បងក្នុងស្រុក

1. **ចាប់ផ្ដើមម៉ាសុីន MCP**៖
   ```bash
   # បើកបរប្រព័ន្ធវីរុត្យែល
   source mcp-env/bin/activate  # macOS/Linux
   # mcp-env\Scripts\activate   # Windows
   
   # ចាប់ផ្ដើមម៉ាស៊ីនបម្រើ
   cd mcp_server
   python sales_analysis.py
   ```

2. **សាកល្បងចំណុចពិនិត្យសុខភាព**៖
   ```bash
   # ការត្រួតពិនិត្យសុខភាពមូលដ្ឋាន
   curl http://localhost:8000/health
   
   # ការត្រួតពិនិត្យសុខភាពលម្អិត
   curl http://localhost:8000/health/detailed
   ```

3. **សាកល្បងឧបករណ៍ MCP**៖
   ```bash
   # បញ្ជីឧបករណ៍ដែលមានស្រាប់
   curl -X POST http://localhost:8000/mcp \
     -H "Content-Type: application/json" \
     -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
     -d '{"method": "tools/list", "params": {}}'
   
   # ទទួលបានសេម៉ង់តារាង
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

### ការសាកល្បងជាមួយ VS Code

1. **កំណត់រចនាសម្ព័ន្ធ VS Code MCP**៖
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

2. **សាកល្បងនៅក្នុង AI Chat**៖
   - បើក VS Code AI Chat
   - វាយ `#zava` និងជ្រើសម៉ាសុីន	server របស់អ្នក
   - សួរ៖ "តារាងណាខ្លះដែលមាន?"
   - សួរ៖ "បង្ហាញហាងលើកំពូល 5 យោងតាមចំនួនការបញ្ជាទិញ"

### ការសាកល្បងឯកតា

បង្កើតការសាកល្បងឯកតាដ៏ទូលំទូលាយ៖

```python
# សាកល្បង/test_mcp_server.py
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

## 🎯 សេចក្ដីចំណាំសំខាន់

បន្ទាប់ពីបញ្ចប់កម្មវិធីនេះ អ្នកគួរតែមាន៖

✅ **ម៉ាសុីន MCP Server ធ្វើការ​បាន**៖ ម៉ាសុីន FastMCP ដំណើរការជាមួយការតភ្ជាប់មូលដ្ឋានទិន្នន័យ  
✅ **ការគ្រប់គ្រងការកំណត់**៖ ការកំណត់បរិយាកាសរឹងមាំ  
✅ **ស្រទាប់មូលដ្ឋានទិន្នន័យ**៖ ការតភ្ជាប់ PostgreSQL ជាមួយការគ្រប់គ្រងការតភ្ជាប់  
✅ **ឧបករណ៍ MCP**៖ ឧបករណ៍ស៊ើបអង្កេតស្កីម៉ារតារាង និងដំណើរការសំណួរ  
✅ **ការតភ្ជាប់ RLS**៖ គ្រប់គ្រងបរិបទសុវត្ថិភាពជួរដេក  
✅ **ការត្រួតពិនិត្យសុខភាព**៖ ចំណុចពិនិត្យសុខភាពពេញលេញ  
✅ **យុទ្ធសាស្ត្រសាកល្បង**៖ ការសាកល្បងក្នុងស្រុក និងការរួមបញ្ចូលជាមួយ VS Code  

## 🚀 អ្វីទៅខាងមុខ

បន្តជាមួយ **[Lab 06: Tool Development](../06-Tools/README.md)** ដើម្បី៖

- ពង្រីកប្រមុខឧបករណ៍ MCP របស់អ្នក
- អនុវត្តគំរូសំណួរលំដាប់ខ្ពស់
- បន្ថែមការផ្ទៀងផ្ទាត់ និងបម្លែងទិន្នន័យ
- បង្កើតឧបករណ៍វិភាគពិសេស

## 📚 ឯកសារបន្ថែម

### FastMCP Framework
- [FastMCP Documentation](https://github.com/modelcontextprotocol/python-sdk) - មគ្គុទេសក៍ផ្លូវការរបស់ FastMCP
- [MCP Specification](https://modelcontextprotocol.io/docs/) - ការបញ្ជាក់ពិសេសនៃពិធីការ
- [Tool Development Guide](https://modelcontextprotocol.io/docs/tools/) - ការបង្កើតឧបករណ៍ MCP

### ការបញ្ចូលមូលដ្ឋានទិន្នន័យ
- [asyncpg Documentation](https://magicstack.github.io/asyncpg/current/) - ដ្រាយវើ PostgreSQL async
- [Connection Pooling Best Practices](https://www.postgresql.org/docs/current/runtime-config-connection.html) - ការតំរូវ PostgreSQL
- [Row Level Security Guide](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - ការអនុវត្ត RLS

### លំនាំ FastAPI
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - មនុស្សផ្នែក​ភាពគេហទំព័រ
- [Dependency Injection](https://fastapi.tiangolo.com/tutorial/dependencies/) - លំនាំ FastAPI
- [Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) - ការគ្រប់គ្រងភារកិច្ច async

---

**បន្ទាប់**៖ ត្រៀមច្រើនឧបករណ៍របស់អ្នកទៀត? បន្តជាមួយ [Lab 06: Tool Development](../06-Tools/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការ​បដិសេធ**៖  
ឡើង​ដើម​ឯកសារ​នេះ​ត្រូវ​បាន​បកប្រែ​ដោយ​ប្រព័ន្ធ​បកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះ​បី​ជា​យើង​ព្យាយាម​បញ្ចេញភាព​ត្រឹមត្រូវក៏​ដោយ សូម​អ្នក​ជ្រាប​ថា​ការ​បកប្រែ​ដោយ​ស្វ័យប្រវត្តិ​អាច​មាន​កំហុស ឬ​ភាព​មិន​ត្រឹមត្រូវ​បាន។ ឯកសារ​ដើម​ក្នុង​ភាសា​ទ្រង់​ទ្រាយ​ដើម​គួរត្រូវ​បាន​គេ​ជា​ទិន្នន័យ​សំខាន់។ សម្រាប់​ព័ត៌មាន​សំខាន់ៗ ការ​បកប្រែ​ដោយ​មនុស្ស​វិជ្ជាជីវៈ​គឺ​ត្រូវ​បានណែនាំ។ យើង​មិន​ទទួល​ខុស​ត្រូវ​ចំពោះ​ការ​យល់​ត្រង់​ខុស ឬ​ការ​ពន្យល់​ខុស​ដែល​កើត​ជា​ពេល​ប្រើប្រាស់​ការ​បកប្រែ​នេះ​ទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->