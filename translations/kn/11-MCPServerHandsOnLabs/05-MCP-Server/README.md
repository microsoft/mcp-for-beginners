<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "240e365cc324d23a0033e5615b5feb5e",
  "translation_date": "2025-12-11T14:36:55+00:00",
  "source_file": "11-MCPServerHandsOnLabs/05-MCP-Server/README.md",
  "language_code": "kn"
}
-->
# MCP ಸರ್ವರ್ ಅನುಷ್ಠಾನ

## 🎯 ಈ ಪ್ರಯೋಗಶಾಲೆ ಏನು ಒಳಗೊಂಡಿದೆ

ಈ ಕೈಯಿಂದ ಮಾಡುವ ಪ್ರಯೋಗಶಾಲೆ ನಿಮಗೆ FastMCP ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ ಉತ್ಪಾದನೆಗೆ ಸಿದ್ಧವಾದ MCP ಸರ್ವರ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವುದನ್ನು ಮಾರ್ಗದರ್ಶನ ಮಾಡುತ್ತದೆ. ನೀವು ಮೂಲ ಸರ್ವರ್ ರಚನೆಯನ್ನು ನಿರ್ಮಿಸುವಿರಿ, ಡೇಟಾಬೇಸ್ ಸಂಯೋಜನೆಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವಿರಿ, ಡೇಟಾ ಪ್ರವೇಶಕ್ಕಾಗಿ ಉಪಕರಣಗಳನ್ನು ಸೃಷ್ಟಿಸುವಿರಿ ಮತ್ತು AI ಚಾಲಿತ ರಿಟೇಲ್ ವಿಶ್ಲೇಷಣೆಯ ಆಧಾರವನ್ನು ಸ್ಥಾಪಿಸುವಿರಿ.

## ಅವಲೋಕನ

MCP ಸರ್ವರ್ ನಮ್ಮ ರಿಟೇಲ್ ವಿಶ್ಲೇಷಣೆ ಪರಿಹಾರದ ಹೃದಯವಾಗಿದೆ. ಇದು AI ಸಹಾಯಕರು ಮತ್ತು PostgreSQL ಡೇಟಾಬೇಸ್ ನಡುವೆ ಸೇತುವೆಯಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ, ವ್ಯವಹಾರ ಡೇಟಾಗೆ ಸುರಕ್ಷಿತ, ಬುದ್ಧಿವಂತ ಪ್ರವೇಶವನ್ನು ಮಾನಕೃತ ಪ್ರೋಟೋಕಾಲ್ ಮೂಲಕ ಒದಗಿಸುತ್ತದೆ.

ಈ ಪ್ರಯೋಗಶಾಲೆ ನಿಮಗೆ ಎಂಟರ್‌ಪ್ರೈಸ್ ಮಾದರಿಗಳು ಮತ್ತು ಉತ್ತಮ ಅಭ್ಯಾಸಗಳನ್ನು ಅನುಸರಿಸಿ ಬಲವಾದ, ವಿಸ್ತರಿಸಬಹುದಾದ MCP ಸರ್ವರ್ ಅನ್ನು ನಿರ್ಮಿಸುವುದನ್ನು ಕಲಿಸುತ್ತದೆ.

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪ್ರಯೋಗಶಾಲೆಯ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಸಾಧ್ಯವಾಗುವುದು:

- **ನಿರ್ಮಿಸಲು** ಸರಿಯಾದ ವಾಸ್ತುಶಿಲ್ಪ ಮತ್ತು ಸಂಘಟನೆಯೊಂದಿಗೆ FastMCP ಸರ್ವರ್
- **ಅನುಷ್ಠಾನಗೊಳಿಸಲು** ಸಂಪರ್ಕ ಪೂಲಿಂಗ್ ಮತ್ತು ದೋಷ ನಿರ್ವಹಣೆಯೊಂದಿಗೆ ಡೇಟಾಬೇಸ್ ಸಂಯೋಜನೆ
- **ಸೃಷ್ಟಿಸಲು** ಡೇಟಾಬೇಸ್ ಸ್ಕೀಮಾ ಪರಿಶೀಲನೆ ಮತ್ತು ಪ್ರಶ್ನೆ ನಿರ್ವಹಣೆಗೆ MCP ಉಪಕರಣಗಳು
- **ಕಾನ್ಫಿಗರ್ ಮಾಡಲು** ಸಾಲಿನ ಮಟ್ಟದ ಭದ್ರತಾ (Row Level Security) ಸನ್ನಿವೇಶ ನಿರ್ವಹಣೆ
- **ಸೇರಿಸಲು** ಆರೋಗ್ಯ ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ಗಮನಾರ್ಹತೆ ವೈಶಿಷ್ಟ್ಯಗಳು
- **ಪರೀಕ್ಷಿಸಲು** ನಿಮ್ಮ MCP ಸರ್ವರ್ ಅನುಷ್ಠಾನವನ್ನು ಸ್ಥಳೀಯವಾಗಿ ಮತ್ತು VS ಕೋಡ್ ಮೂಲಕ

## 📁 ಪ್ರಾಜೆಕ್ಟ್ ರಚನೆ

MCP ಸರ್ವರ್ ಸಂಘಟನೆಯನ್ನು ಪರಿಶೀಲಿಸೋಣ:

```
mcp_server/
├── __init__.py                 # Package initialization
├── config.py                   # Configuration management
├── health_check.py             # Health monitoring endpoints
├── sales_analysis.py           # Main MCP server implementation
├── sales_analysis_postgres.py  # Database integration layer
└── sales_analysis_text_embeddings.py  # AI/semantic search integration
```

## 🔧 ಸಂರಚನಾ ನಿರ್ವಹಣೆ

### ಪರಿಸರ ಸಂರಚನೆ (`config.py`)

ಮೊದಲು, ಬಲವಾದ ಸಂರಚನಾ ವ್ಯವಸ್ಥೆಯನ್ನು ಸೃಷ್ಟಿಸೋಣ:

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

# .env ಫೈಲ್‌ನಿಂದ ಪರಿಸರ ಚರಗಳನ್ನು ಲೋಡ್ ಮಾಡಿ
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
                'jit': 'off',  # ಸ್ಥಿರತೆಯಿಗಾಗಿ JIT ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಿ
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
        
        # ಸಂರಚನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
        self._validate_config()
    
    def _validate_config(self):
        """Validate configuration and log warnings for missing values."""
        if not self.database.password:
            logger.warning("Database password is empty. This may cause connection issues.")
        
        if not self.azure.is_configured():
            logger.warning("Azure configuration is incomplete. AI features may not work.")
        
        logger.info(f"Configuration loaded - Database: {self.database.host}:{self.database.port}")
        logger.info(f"Server will run on {self.server.host}:{self.server.port}")

# ಜಾಗತಿಕ ಸಂರಚನಾ ಉದಾಹರಣೆ
config = MCPServerConfig()
```

### ಪ್ರಮುಖ ಸಂರಚನಾ ವೈಶಿಷ್ಟ್ಯಗಳು

- **ಪರಿಸರ ಚರ ಸಂಗ್ರಹಣೆ**: ಸ್ವಯಂಚಾಲಿತ .env ಫೈಲ್ ಬೆಂಬಲ
- **ಪ್ರಕಾರ ಭದ್ರತೆ**: ಡೇಟಾಕ್ಲಾಸ್ ಮಾನ್ಯತೆ ಮತ್ತು ಪ್ರಕಾರ ಸೂಚನೆಗಳು
- **ಲವಚಿಕ ಡೀಫಾಲ್ಟ್‌ಗಳು**: ಅಭಿವೃದ್ಧಿಗಾಗಿ ಸೂಕ್ತ ಡೀಫಾಲ್ಟ್‌ಗಳು
- **ಮಾನ್ಯತೆ**: ಸಹಾಯಕ ದೋಷ ಸಂದೇಶಗಳೊಂದಿಗೆ ಸಂರಚನಾ ಮಾನ್ಯತೆ
- **ಭದ್ರತೆ**: ಸಂವೇದನಾಶೀಲ ಮೌಲ್ಯಗಳು ಕೇವಲ ಪರಿಸರ ಚರಗಳಿಂದ

## 🗄️ ಡೇಟಾಬೇಸ್ ಸಂಯೋಜನೆ ಪದರ

### PostgreSQL ಪೂರೈಕೆದಾರ (`sales_analysis_postgres.py`)

ಡೇಟಾಬೇಸ್ ಸಂಯೋಜನೆ ಪದರವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸೋಣ:

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
                    max_inactive_connection_lifetime=300  # 5 ನಿಮಿಷಗಳು
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
            
            # ಸ್ಕೀಮಾ ಮತ್ತು ಟೇಬಲ್ ಹೆಸರನ್ನು ವಿಶ್ಲೇಷಿಸಿ
            if '.' in table_name:
                schema_name, table_name = table_name.split('.', 1)
            else:
                schema_name = 'retail'  # ಡೀಫಾಲ್ಟ್ ಸ್ಕೀಮಾ
            
            # ಕಾಲಮ್ ಮಾಹಿತಿಯನ್ನು ಪಡೆಯಿರಿ
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
            
            # ವಿದೇಶಿ ಕೀ ಸಂಬಂಧಗಳನ್ನು ಪಡೆಯಿರಿ
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
            
            # ಸೂಚ್ಯಂಕಗಳನ್ನು ಪಡೆಯಿರಿ
            index_query = """
                SELECT 
                    indexname,
                    indexdef
                FROM pg_indexes 
                WHERE schemaname = $1 AND tablename = $2
            """
            
            indexes = await conn.fetch(index_query, schema_name, table_name)
            
            # ಸ್ಕೀಮಾ ಮಾಹಿತಿಯನ್ನು ಸ್ವರೂಪಗೊಳಿಸಿ
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
        
        # ಕಾಲಮ್ ವ್ಯಾಖ್ಯಾನಗಳನ್ನು ರಚಿಸಿ
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
        
        # ವಿದೇಶಿ ಕೀ ಮಾಹಿತಿಯನ್ನು ರಚಿಸಿ
        fk_lines = []
        for fk in foreign_keys:
            fk_lines.append(f"  {fk['column']} -> {fk['references']}")
        
        # ಓದಲು ಸುಲಭವಾದ ಸ್ವರೂಪದಲ್ಲಿ ಸಂಯೋಜಿಸಿ
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
                # ಪ್ರಶ್ನೆ ಸಮಯ ಮಿತಿ ನಿಗದಿಪಡಿಸಿ
                rows = await asyncio.wait_for(
                    conn.fetch(sql_query),
                    timeout=config.database.command_timeout
                )
                
                if not rows:
                    return "Query executed successfully. No rows returned."
                
                # ಫಲಿತಾಂಶ ಸೆಟ್ ಗಾತ್ರವನ್ನು ಮಿತಿಗೊಳಿಸಿ
                limited_rows = rows[:max_rows]
                
                # ಫಲಿತಾಂಶಗಳನ್ನು ಸ್ವರೂಪಗೊಳಿಸಿ
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
        
        # ಕಾಲಮ್ ಹೆಸರನ್ನು ಪಡೆಯಿರಿ
        columns = list(rows[0].keys())
        
        # ಶೀರ್ಷಿಕೆ ರಚಿಸಿ
        result_lines = [f"Results ({len(rows)} of {total_rows} rows):"]
        result_lines.append("=" * 50)
        
        # ಕಾಲಮ್ ಶೀರ್ಷಿಕೆಗಳನ್ನು ಸೇರಿಸಿ
        header = " | ".join(columns)
        result_lines.append(header)
        result_lines.append("-" * len(header))
        
        # ಡೇಟಾ ಸಾಲುಗಳನ್ನು ಸೇರಿಸಿ
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
        
        # ಅಗತ್ಯವಿದ್ದರೆ ಕಡಿತ ಸೂಚನೆಯನ್ನು ಸೇರಿಸಿ
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
                # ಸರಳ ಸಂಪರ್ಕ ಪರೀಕ್ಷೆ
                result = await conn.fetchval("SELECT 1")
                
                # ಪೂಲ್ ಸ್ಥಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
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

# ಜಾಗತಿಕ ಡೇಟಾಬೇಸ್ ಪೂರೈಕೆದಾರ ಉದಾಹರಣೆ
db_provider = PostgreSQLSchemaProvider()
```

### ಪ್ರಮುಖ ಡೇಟಾಬೇಸ್ ಪದರ ವೈಶಿಷ್ಟ್ಯಗಳು

- **ಸಂಪರ್ಕ ಪೂಲಿಂಗ್**: asyncpg ಮೂಲಕ ಪರಿಣಾಮಕಾರಿ ಸಂಪನ್ಮೂಲ ನಿರ್ವಹಣೆ
- **RLS ಸಂಯೋಜನೆ**: ಸ್ವಯಂಚಾಲಿತ ಸಾಲಿನ ಮಟ್ಟದ ಭದ್ರತಾ ಸನ್ನಿವೇಶ ಸೆಟ್ಟಿಂಗ್
- **ಸ್ಕೀಮಾ ಪರಿಶೀಲನೆ**: ಡೈನಾಮಿಕ್ ಟೇಬಲ್ ಸ್ಕೀಮಾ ಅನ್ವೇಷಣೆ
- **ದೋಷ ನಿರ್ವಹಣೆ**: ಸಮಗ್ರ ದೋಷ ನಿರ್ವಹಣೆ ಮತ್ತು ಲಾಗಿಂಗ್
- **ಪ್ರಶ್ನೆ ಸ್ವರೂಪಣ**: AI-ಸ್ನೇಹಿ ಫಲಿತಾಂಶ ಸ್ವರೂಪಣ
- **ಆರೋಗ್ಯ ಮೇಲ್ವಿಚಾರಣೆ**: ಡೇಟಾಬೇಸ್ ಸಂಪರ್ಕ ಮತ್ತು ಪೂಲ್ ಸ್ಥಿತಿ ಪರಿಶೀಲನೆ

## 🔧 ಮುಖ್ಯ MCP ಸರ್ವರ್ ಅನುಷ್ಠಾನ

### FastMCP ಸರ್ವರ್ (`sales_analysis.py`)

ಈಗ ಮುಖ್ಯ MCP ಸರ್ವರ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸೋಣ:

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

# ಲಾಗಿಂಗ್ ಅನ್ನು ಸಂರಚಿಸಿ
logging.basicConfig(
    level=getattr(logging, config.server.log_level),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ಫಾಸ್ಟ್‌ಎಂಸಿಪಿ ಸರ್ವರ್ ಉದಾಹರಣೆಯನ್ನು ರಚಿಸಿ
mcp = FastMCP("Zava Retail Sales Analysis")

# ಸ್ಕೀಮಾ ಪ್ರವೇಶಕ್ಕಾಗಿ ಮಾನ್ಯವಾದ ಟೇಬಲ್‌ಗಳ ಪಟ್ಟಿ
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
    # HTTP ಮೋಡ್‌ನಲ್ಲಿ, ಹೆಡರ್‌ಗಳಿಂದ ಪಡೆಯಿರಿ
    if hasattr(ctx, 'headers') and ctx.headers:
        rls_user_id = ctx.headers.get("x-rls-user-id")
        if rls_user_id:
            logger.debug(f"RLS User ID from headers: {rls_user_id}")
            return rls_user_id
    
    # ಅಭಿವೃದ್ಧಿ/ಪರೀಕ್ಷೆಗಾಗಿ ಡೀಫಾಲ್ಟ್ ಬ್ಯಾಕ್ಅಪ್
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
    
    # ಟೇಬಲ್ ಹೆಸರುಗಳನ್ನು ಮಾನ್ಯಗೊಳಿಸಿ
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

# ಅಪ್ಲಿಕೇಶನ್ ಜೀವನಚಕ್ರ ನಿರ್ವಹಣೆ
@asynccontextmanager
async def lifespan(app):
    """Manage application startup and shutdown."""
    logger.info("Starting Zava Retail MCP Server...")
    
    try:
        # ಡೇಟಾಬೇಸ್ ಸಂಪರ್ಕ ಪೂಲ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ
        await db_provider.create_pool()
        logger.info("Database connection pool initialized")
        
        # ಡೇಟಾಬೇಸ್ ಸಂಪರ್ಕತೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ
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
        # ಸ್ವಚ್ಛತೆ
        logger.info("Shutting down MCP Server...")
        await db_provider.close_pool()
        logger.info("MCP Server shutdown complete")

# ಸರ್ವರ್ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಸಂರಚಿಸಿ
def create_app():
    """Create and configure the MCP server application."""
    
    # ಫಾಸ್ಟ್‌ಎಂಸಿಪಿ ಅಪ್ಲಿಕೇಶನ್ ಉದಾಹರಣೆಯನ್ನು ಪಡೆಯಿರಿ
    app = mcp.sse_app()
    
    # ಜೀವನಚಕ್ರ ನಿರ್ವಹಣೆಯನ್ನು ಸ್ಥಾಪಿಸಿ
    app.router.lifespan_context = lifespan
    
    # ಸಕ್ರಿಯಗೊಂಡಿದ್ದರೆ ಆರೋಗ್ಯ ಪರಿಶೀಲನೆ ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಸೇರಿಸಿ
    if config.server.enable_health_check:
        setup_health_endpoints(app, db_provider)
    
    # ಸಕ್ರಿಯಗೊಂಡಿದ್ದರೆ CORS ಅನ್ನು ಸಂರಚಿಸಿ
    if config.server.enable_cors:
        from fastapi.middleware.cors import CORSMiddleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # ಉತ್ಪಾದನೆಗಾಗಿ ಸೂಕ್ತವಾಗಿ ಸಂರಚಿಸಿ
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    logger.info(f"MCP Server configured - CORS: {config.server.enable_cors}, Health: {config.server.enable_health_check}")
    
    return app

# ಅಪ್ಲಿಕೇಶನ್ ಉದಾಹರಣೆಯನ್ನು ರಚಿಸಿ
app = create_app()

# ಅಭಿವೃದ್ಧಿಗಾಗಿ ಮುಖ್ಯ ಪ್ರವೇಶ ಬಿಂದುವು
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

### ಪ್ರಮುಖ MCP ಸರ್ವರ್ ವೈಶಿಷ್ಟ್ಯಗಳು

- **ಉಪಕರಣ ನೋಂದಣಿ**: ಪ್ರಕಾರ ಭದ್ರತೆಯೊಂದಿಗೆ ಘೋಷಣಾತ್ಮಕ ಉಪಕರಣ ವ್ಯಾಖ್ಯಾನಗಳು
- **RLS ಸನ್ನಿವೇಶ ನಿರ್ವಹಣೆ**: ಸ್ವಯಂಚಾಲಿತ ಬಳಕೆದಾರ ಗುರುತಿನ ಹೊರತೆಗೆಯುವಿಕೆ ಮತ್ತು ಸನ್ನಿವೇಶ ಸೆಟ್ಟಿಂಗ್
- **ದೋಷ ನಿರ್ವಹಣೆ**: ಬಳಕೆದಾರ ಸ್ನೇಹಿ ಸಂದೇಶಗಳೊಂದಿಗೆ ಸಮಗ್ರ ದೋಷ ನಿರ್ವಹಣೆ
- **ಜೀವನಚಕ್ರ ನಿರ್ವಹಣೆ**: ಸಂಪನ್ಮೂಲ ಶುದ್ಧೀಕರಣದೊಂದಿಗೆ ಸರಿಯಾದ ಪ್ರಾರಂಭ/ನಿರ್ಗಮನ
- **ಆರೋಗ್ಯ ಮೇಲ್ವಿಚಾರಣೆ**: ಒಳಗೊಂಡ ಆರೋಗ್ಯ ಪರಿಶೀಲನೆ ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳು
- **ಅಭಿವೃದ್ಧಿ ಬೆಂಬಲ**: ಹಾಟ್ ರಿಲೋಡ್ ಮತ್ತು ಡಿಬಗಿಂಗ್ ಸಾಮರ್ಥ್ಯಗಳು

## 🏥 ಆರೋಗ್ಯ ಮೇಲ್ವಿಚಾರಣೆ

### ಆರೋಗ್ಯ ಪರಿಶೀಲನೆ ಅನುಷ್ಠಾನ (`health_check.py`)

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
        
        # ಡೇಟಾಬೇಸ್ ಪರಿಶೀಲಿಸಿ
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
        
        # ಒಟ್ಟು ಸ್ಥಿತಿಯನ್ನು ನವೀಕರಿಸಿ
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
            # ಪ್ರಮುಖ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ
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

## 🧪 ನಿಮ್ಮ MCP ಸರ್ವರ್ ಪರೀಕ್ಷೆ

### ಸ್ಥಳೀಯ ಪರೀಕ್ಷೆ

1. **MCP ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸಿ**:
   ```bash
   # ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ
   source mcp-env/bin/activate  # macOS/Linux
   # mcp-env\Scripts\activate   # ವಿಂಡೋಸ್
   
   # ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸಿ
   cd mcp_server
   python sales_analysis.py
   ```

2. **ಆರೋಗ್ಯ ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ**:
   ```bash
   # ಮೂಲ ಆರೋಗ್ಯ ಪರಿಶೀಲನೆ
   curl http://localhost:8000/health
   
   # ವಿವರವಾದ ಆರೋಗ್ಯ ಪರಿಶೀಲನೆ
   curl http://localhost:8000/health/detailed
   ```

3. **MCP ಉಪಕರಣಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ**:
   ```bash
   # ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
   curl -X POST http://localhost:8000/mcp \
     -H "Content-Type: application/json" \
     -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
     -d '{"method": "tools/list", "params": {}}'
   
   # ಟೇಬಲ್ ಸ್ಕೀಮಾಗಳನ್ನು ಪಡೆಯಿರಿ
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

### VS ಕೋಡ್ ಸಂಯೋಜನೆ ಪರೀಕ್ಷೆ

1. **VS ಕೋಡ್ MCP ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ**:
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

2. **AI ಚಾಟ್‌ನಲ್ಲಿ ಪರೀಕ್ಷಿಸಿ**:
   - VS ಕೋಡ್ AI ಚಾಟ್ ತೆರೆಯಿರಿ
   - `#zava` ಟೈಪ್ ಮಾಡಿ ಮತ್ತು ನಿಮ್ಮ ಸರ್ವರ್ ಆಯ್ಕೆಮಾಡಿ
   - ಕೇಳಿ: "ಯಾವ ಟೇಬಲ್‌ಗಳು ಲಭ್ಯವಿವೆ?"
   - ಕೇಳಿ: "ಆರ್ಡರ್‌ಗಳ ಸಂಖ್ಯೆಯ ಆಧಾರದ ಮೇಲೆ ಟಾಪ್ 5 ಅಂಗಡಿಗಳನ್ನು ತೋರಿಸಿ"

### ಘಟಕ ಪರೀಕ್ಷೆ

ವಿಸ್ತೃತ ಘಟಕ ಪರೀಕ್ಷೆಗಳನ್ನು ಸೃಷ್ಟಿಸಿ:

```python
# ಪರೀಕ್ಷೆಗಳು/test_mcp_server.py
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

## 🎯 ಪ್ರಮುಖ ಪಾಠಗಳು

ಈ ಪ್ರಯೋಗಶಾಲೆ ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಹೊಂದಿರಬೇಕು:

✅ **ಕಾರ್ಯನಿರ್ವಹಿಸುವ MCP ಸರ್ವರ್**: ಡೇಟಾಬೇಸ್ ಸಂಯೋಜನೆಯೊಂದಿಗೆ FastMCP ಸರ್ವರ್  
✅ **ಸಂರಚನಾ ನಿರ್ವಹಣೆ**: ಬಲವಾದ ಪರಿಸರ ಆಧಾರಿತ ಸಂರಚನೆ  
✅ **ಡೇಟಾಬೇಸ್ ಪದರ**: ಸಂಪರ್ಕ ಪೂಲಿಂಗ್ ಹೊಂದಿರುವ PostgreSQL ಸಂಯೋಜನೆ  
✅ **MCP ಉಪಕರಣಗಳು**: ಸ್ಕೀಮಾ ಪರಿಶೀಲನೆ ಮತ್ತು ಪ್ರಶ್ನೆ ನಿರ್ವಹಣಾ ಉಪಕರಣಗಳು  
✅ **RLS ಸಂಯೋಜನೆ**: ಸಾಲಿನ ಮಟ್ಟದ ಭದ್ರತಾ ಸನ್ನಿವೇಶ ನಿರ್ವಹಣೆ  
✅ **ಆರೋಗ್ಯ ಮೇಲ್ವಿಚಾರಣೆ**: ಸಮಗ್ರ ಆರೋಗ್ಯ ಪರಿಶೀಲನೆ ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳು  
✅ **ಪರೀಕ್ಷಾ ತಂತ್ರ**: ಸ್ಥಳೀಯ ಪರೀಕ್ಷೆ ಮತ್ತು VS ಕೋಡ್ ಸಂಯೋಜನೆ  

## 🚀 ಮುಂದಿನ ಹಂತ

**[Lab 06: Tool Development](../06-Tools/README.md)** ಜೊತೆಗೆ ಮುಂದುವರಿಯಿರಿ:

- ನಿಮ್ಮ MCP ಉಪಕರಣ ಸಂಗ್ರಹವನ್ನು ವಿಸ್ತರಿಸಿ
- ಸುಧಾರಿತ ಪ್ರಶ್ನೆ ಮಾದರಿಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ
- ಡೇಟಾ ಮಾನ್ಯತೆ ಮತ್ತು ಪರಿವರ್ತನೆಯನ್ನು ಸೇರಿಸಿ
- ವಿಶೇಷ ವಿಶ್ಲೇಷಣಾ ಉಪಕರಣಗಳನ್ನು ಸೃಷ್ಟಿಸಿ

## 📚 ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

### FastMCP ಫ್ರೇಮ್ವರ್ಕ್
- [FastMCP ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://github.com/modelcontextprotocol/python-sdk) - ಅಧಿಕೃತ FastMCP ಮಾರ್ಗದರ್ಶಿ
- [MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್](https://modelcontextprotocol.io/docs/) - ಪ್ರೋಟೋಕಾಲ್ ಸ್ಪೆಸಿಫಿಕೇಶನ್
- [ಉಪಕರಣ ಅಭಿವೃದ್ಧಿ ಮಾರ್ಗದರ್ಶಿ](https://modelcontextprotocol.io/docs/tools/) - MCP ಉಪಕರಣಗಳ ಸೃಷ್ಟಿ

### ಡೇಟಾಬೇಸ್ ಸಂಯೋಜನೆ
- [asyncpg ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://magicstack.github.io/asyncpg/current/) - PostgreSQL async ಚಾಲಕ
- [ಸಂಪರ್ಕ ಪೂಲಿಂಗ್ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು](https://www.postgresql.org/docs/current/runtime-config-connection.html) - PostgreSQL ಟ್ಯೂನಿಂಗ್
- [ಸಾಲಿನ ಮಟ್ಟದ ಭದ್ರತಾ ಮಾರ್ಗದರ್ಶಿ](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - RLS ಅನುಷ್ಠಾನ

### FastAPI ಮಾದರಿಗಳು
- [FastAPI ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://fastapi.tiangolo.com/) - ವೆಬ್ ಫ್ರೇಮ್ವರ್ಕ್ ಉಲ್ಲೇಖ
- [ಆಧಾರ ನಿರ್ವಹಣೆ](https://fastapi.tiangolo.com/tutorial/dependencies/) - FastAPI ಮಾದರಿಗಳು
- [ಹಿನ್ನೆಲೆ ಕಾರ್ಯಗಳು](https://fastapi.tiangolo.com/tutorial/background-tasks/) - ಅಸಿಂಕ್ರೋನಸ್ ಕಾರ್ಯ ನಿರ್ವಹಣೆ

---

**ಮುಂದೆ**: ನಿಮ್ಮ ಉಪಕರಣಗಳನ್ನು ವಿಸ್ತರಿಸಲು ಸಿದ್ಧರಾ? [Lab 06: Tool Development](../06-Tools/README.md) ಜೊತೆಗೆ ಮುಂದುವರಿಯಿರಿ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->