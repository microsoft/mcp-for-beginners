# MCP സെർവർ നടപ്പാക്കൽ

## 🎯 ഈ ലാബ് ഉൾക്കൊള്ളുന്നത്

ഈ ഹാൻഡ്‌സ്-ഓൺ ലാബ് നിങ്ങൾക്ക് FastMCP ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച് പ്രൊഡക്ഷൻ-റെഡി MCP സെർവർ നടപ്പാക്കുന്നതിൽ മാർഗനിർദ്ദേശം നൽകുന്നു. നിങ്ങൾ കോർ സെർവർ ഘടന നിർമ്മിക്കും, ഡാറ്റാബേസ് ഇന്റഗ്രേഷൻ നടപ്പാക്കും, ഡാറ്റ ആക്സസ് ടൂളുകൾ സൃഷ്ടിക്കും, AI-ചാലിത റീട്ടെയിൽ അനലിറ്റിക്സിനുള്ള അടിസ്ഥാനമിടും.

## അവലോകനം

MCP സെർവർ നമ്മുടെ റീട്ടെയിൽ അനലിറ്റിക്സ് പരിഹാരത്തിന്റെ ഹൃദയമാണ്. ഇത് AI അസിസ്റ്റന്റുകളും PostgreSQL ഡാറ്റാബേസും തമ്മിലുള്ള പാലമായി പ്രവർത്തിച്ച്, ബിസിനസ് ഡാറ്റയ്ക്ക് സുരക്ഷിതവും ബുദ്ധിമുട്ടുള്ള ആക്സസ് ഒരു സ്റ്റാൻഡേർഡൈസ്ഡ് പ്രോട്ടോക്കോൾ വഴി നൽകുന്നു.

ഈ ലാബ് എന്റർപ്രൈസ് പാറ്റേണുകളും മികച്ച പ്രാക്ടീസുകളും പിന്തുടർന്ന് ഒരു ശക്തവും സ്കേലബിൾ ആയ MCP സെർവർ നിർമ്മിക്കാൻ നിങ്ങളെ പഠിപ്പിക്കുന്നു.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ ലാബ് അവസാനിക്കുന്നപ്പോൾ, നിങ്ങൾക്ക് കഴിയും:

- **നിർമ്മിക്കുക** ശരിയായ ആർക്കിടെക്ചറും സംഘടനയും ഉള്ള FastMCP സെർവർ  
- **നടപ്പാക്കുക** കണക്ഷൻ പൂലിംഗും പിശക് കൈകാര്യം ചെയ്യലും ഉള്ള ഡാറ്റാബേസ് ഇന്റഗ്രേഷൻ  
- **സൃഷ്ടിക്കുക** ഡാറ്റാബേസ് സ്കീമ ഇൻട്രോസ്പെക്ഷനും ക്വറി എക്സിക്യൂഷനും ഉള്ള MCP ടൂളുകൾ  
- **കോൺഫിഗർ ചെയ്യുക** റോ ലെവൽ സെക്യൂരിറ്റി കോൺടെക്സ്റ്റ് മാനേജ്മെന്റ്  
- **കൂടുക** ഹെൽത്ത് മോണിറ്ററിംഗ്, ഒബ്സർവബിലിറ്റി ഫീച്ചറുകൾ  
- **ടെസ്റ്റ് ചെയ്യുക** നിങ്ങളുടെ MCP സെർവർ നടപ്പാക്കൽ ലോക്കലിലും VS കോഡിലും

## 📁 പ്രോജക്ട് ഘടന

MCP സെർവർ സംഘടന പരിശോധിക്കാം:

```
mcp_server/
├── __init__.py                 # Package initialization
├── config.py                   # Configuration management
├── health_check.py             # Health monitoring endpoints
├── sales_analysis.py           # Main MCP server implementation
├── sales_analysis_postgres.py  # Database integration layer
└── sales_analysis_text_embeddings.py  # AI/semantic search integration
```

## 🔧 കോൺഫിഗറേഷൻ മാനേജ്മെന്റ്

### എൻവയോൺമെന്റ് കോൺഫിഗറേഷൻ (`config.py`)

ആദ്യം, ഒരു ശക്തമായ കോൺഫിഗറേഷൻ സിസ്റ്റം സൃഷ്ടിക്കാം:

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

# .env ഫയലിൽ നിന്ന് പരിസ്ഥിതി വ്യത്യാസങ്ങൾ ലോഡ് ചെയ്യുക
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
                'jit': 'off',  # സ്ഥിരതയ്ക്കായി JIT അപ്രാപ്തമാക്കുക
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
        
        # കോൺഫിഗറേഷൻ സാധുത പരിശോധിക്കുക
        self._validate_config()
    
    def _validate_config(self):
        """Validate configuration and log warnings for missing values."""
        if not self.database.password:
            logger.warning("Database password is empty. This may cause connection issues.")
        
        if not self.azure.is_configured():
            logger.warning("Azure configuration is incomplete. AI features may not work.")
        
        logger.info(f"Configuration loaded - Database: {self.database.host}:{self.database.port}")
        logger.info(f"Server will run on {self.server.host}:{self.server.port}")

# ആഗോള കോൺഫിഗറേഷൻ ഇൻസ്റ്റൻസ്
config = MCPServerConfig()
```

### പ്രധാന കോൺഫിഗറേഷൻ ഫീച്ചറുകൾ

- **എൻവയോൺമെന്റ് വേരിയബിൾ ലോഡിംഗ്**: ഓട്ടോമാറ്റിക് .env ഫയൽ പിന്തുണ  
- **ടൈപ്പ് സേഫ്റ്റി**: ഡാറ്റാക്ലാസ് വാലിഡേഷൻ, ടൈപ്പ് ഹിന്റുകൾ  
- **ഫ്ലെക്സിബിൾ ഡിഫോൾട്ടുകൾ**: ഡെവലപ്പ്മെന്റിനുള്ള സെൻസിബിൾ ഡിഫോൾട്ടുകൾ  
- **വാലിഡേഷൻ**: സഹായകരമായ പിശക് സന്ദേശങ്ങളോടെ കോൺഫിഗറേഷൻ വാലിഡേഷൻ  
- **സെക്യൂരിറ്റി**: സെൻസിറ്റീവ് മൂല്യങ്ങൾ എൻവയോൺമെന്റ് വേരിയബിൾമാർന്നിൽ നിന്നേ മാത്രം

## 🗄️ ഡാറ്റാബേസ് ഇന്റഗ്രേഷൻ ലെയർ

### PostgreSQL പ്രൊവൈഡർ (`sales_analysis_postgres.py`)

ഡാറ്റാബേസ് ഇന്റഗ്രേഷൻ ലെയർ നടപ്പാക്കാം:

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
                    max_inactive_connection_lifetime=300  # 5 മിനിറ്റ്
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
            
            # സ്കീമയും പട്ടികയുടെ പേരും പാഴ്‌സ് ചെയ്യുക
            if '.' in table_name:
                schema_name, table_name = table_name.split('.', 1)
            else:
                schema_name = 'retail'  # ഡിഫോൾട്ട് സ്കീമ
            
            # കോളം വിവരങ്ങൾ നേടുക
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
            
            # വിദേശ കീ ബന്ധങ്ങൾ നേടുക
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
            
            # ഇൻഡക്സുകൾ നേടുക
            index_query = """
                SELECT 
                    indexname,
                    indexdef
                FROM pg_indexes 
                WHERE schemaname = $1 AND tablename = $2
            """
            
            indexes = await conn.fetch(index_query, schema_name, table_name)
            
            # സ്കീമ വിവരങ്ങൾ ഫോർമാറ്റ് ചെയ്യുക
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
        
        # കോളം നിർവചനങ്ങൾ സൃഷ്ടിക്കുക
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
        
        # വിദേശ കീ വിവരങ്ങൾ സൃഷ്ടിക്കുക
        fk_lines = []
        for fk in foreign_keys:
            fk_lines.append(f"  {fk['column']} -> {fk['references']}")
        
        # വായിക്കാൻ കഴിയുന്ന ഫോർമാറ്റിലേക്ക് സംയോജിപ്പിക്കുക
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
                # ഒരു ക്വറി ടൈംഔട്ട് സജ്ജമാക്കുക
                rows = await asyncio.wait_for(
                    conn.fetch(sql_query),
                    timeout=config.database.command_timeout
                )
                
                if not rows:
                    return "Query executed successfully. No rows returned."
                
                # ഫലം സെറ്റ് വലുപ്പം പരിമിതപ്പെടുത്തുക
                limited_rows = rows[:max_rows]
                
                # ഫലങ്ങൾ ഫോർമാറ്റ് ചെയ്യുക
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
        
        # കോളം പേരുകൾ നേടുക
        columns = list(rows[0].keys())
        
        # ഹെഡർ സൃഷ്ടിക്കുക
        result_lines = [f"Results ({len(rows)} of {total_rows} rows):"]
        result_lines.append("=" * 50)
        
        # കോളം ഹെഡറുകൾ ചേർക്കുക
        header = " | ".join(columns)
        result_lines.append(header)
        result_lines.append("-" * len(header))
        
        # ഡാറ്റാ വരികൾ ചേർക്കുക
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
        
        # ആവശ്യമെങ്കിൽ ട്രങ്കേഷൻ അറിയിപ്പ് ചേർക്കുക
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
                # ലളിതമായ കണക്ടിവിറ്റി പരിശോധന
                result = await conn.fetchval("SELECT 1")
                
                # പൂൾ നില പരിശോധിക്കുക
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

# ആഗോള ഡാറ്റാബേസ് പ്രൊവൈഡർ ഇൻസ്റ്റൻസ്
db_provider = PostgreSQLSchemaProvider()
```

### പ്രധാന ഡാറ്റാബേസ് ലെയർ ഫീച്ചറുകൾ

- **കണക്ഷൻ പൂലിംഗ്**: asyncpg ഉപയോഗിച്ച് കാര്യക്ഷമമായ റിസോഴ്‌സ് മാനേജ്മെന്റ്  
- **RLS ഇന്റഗ്രേഷൻ**: ഓട്ടോമാറ്റിക് റോ ലെവൽ സെക്യൂരിറ്റി കോൺടെക്സ്റ്റ് സെറ്റിംഗ്  
- **സ്കീമ ഇൻട്രോസ്പെക്ഷൻ**: ഡൈനാമിക് ടേബിൾ സ്കീമ കണ്ടെത്തൽ  
- **പിശക് കൈകാര്യം ചെയ്യൽ**: സമഗ്രമായ പിശക് മാനേജ്മെന്റ്, ലോഗിംഗ്  
- **ക്വറി ഫോർമാറ്റിംഗ്**: AI-സൗഹൃദ ഫലം ഫോർമാറ്റിംഗ്  
- **ഹെൽത്ത് മോണിറ്ററിംഗ്**: ഡാറ്റാബേസ് കണക്ടിവിറ്റി, പൂൾ സ്റ്റാറ്റസ് പരിശോധനകൾ

## 🔧 പ്രധാന MCP സെർവർ നടപ്പാക്കൽ

### FastMCP സെർവർ (`sales_analysis.py`)

ഇപ്പോൾ പ്രധാന MCP സെർവർ നടപ്പാക്കാം:

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

# ലോഗിംഗ് ക്രമീകരിക്കുക
logging.basicConfig(
    level=getattr(logging, config.server.log_level),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# FastMCP സെർവർ ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുക
mcp = FastMCP("Zava Retail Sales Analysis")

# സ്കീമ ആക്സസിനുള്ള സാധുവായ പട്ടികകളുടെ പട്ടിക
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
    # HTTP മോഡിൽ, ഹെഡറുകളിൽ നിന്ന് നേടുക
    if hasattr(ctx, 'headers') and ctx.headers:
        rls_user_id = ctx.headers.get("x-rls-user-id")
        if rls_user_id:
            logger.debug(f"RLS User ID from headers: {rls_user_id}")
            return rls_user_id
    
    # വികസന/പരീക്ഷണത്തിനുള്ള ഡിഫോൾട്ട് ഫാൾബാക്ക്
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
    
    # പട്ടികയുടെ പേരുകൾ സാധുവാണെന്ന് പരിശോധിക്കുക
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

# ആപ്ലിക്കേഷൻ ലൈഫ്‌സൈക്കിൾ മാനേജ്മെന്റ്
@asynccontextmanager
async def lifespan(app):
    """Manage application startup and shutdown."""
    logger.info("Starting Zava Retail MCP Server...")
    
    try:
        # ഡാറ്റാബേസ് കണക്ഷൻ പൂൾ ആരംഭിക്കുക
        await db_provider.create_pool()
        logger.info("Database connection pool initialized")
        
        # ഡാറ്റാബേസ് കണക്ടിവിറ്റി പരിശോധിക്കുക
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
        # ക്ലീൻഅപ്പ്
        logger.info("Shutting down MCP Server...")
        await db_provider.close_pool()
        logger.info("MCP Server shutdown complete")

# സെർവർ ആപ്ലിക്കേഷൻ ക്രമീകരിക്കുക
def create_app():
    """Create and configure the MCP server application."""
    
    # FastMCP ആപ്പ് ഇൻസ്റ്റൻസ് നേടുക
    app = mcp.sse_app()
    
    # ലൈഫ്‌സൈക്കിൾ മാനേജ്മെന്റ് സജ്ജമാക്കുക
    app.router.lifespan_context = lifespan
    
    # സജീവമാക്കിയാൽ ഹെൽത്ത് ചെക്ക് എൻഡ്‌പോയിന്റുകൾ ചേർക്കുക
    if config.server.enable_health_check:
        setup_health_endpoints(app, db_provider)
    
    # സജീവമാക്കിയാൽ CORS ക്രമീകരിക്കുക
    if config.server.enable_cors:
        from fastapi.middleware.cors import CORSMiddleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # ഉത്പാദനത്തിനായി അനുയോജ്യമായി ക്രമീകരിക്കുക
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    logger.info(f"MCP Server configured - CORS: {config.server.enable_cors}, Health: {config.server.enable_health_check}")
    
    return app

# ആപ്ലിക്കേഷൻ ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുക
app = create_app()

# വികസനത്തിനുള്ള പ്രധാന പ്രവേശന പോയിന്റ്
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

### പ്രധാന MCP സെർവർ ഫീച്ചറുകൾ

- **ടൂൾ രജിസ്ട്രേഷൻ**: ടൈപ്പ് സേഫ്റ്റിയോടെയുള്ള ഡിക്ലറേറ്റീവ് ടൂൾ നിർവചനങ്ങൾ  
- **RLS കോൺടെക്സ്റ്റ് മാനേജ്മെന്റ്**: ഓട്ടോമാറ്റിക് യൂസർ ഐഡന്റിറ്റി എക്സ്ട്രാക്ഷനും കോൺടെക്സ്റ്റ് സെറ്റിംഗും  
- **പിശക് കൈകാര്യം ചെയ്യൽ**: ഉപയോക്തൃ സൗഹൃദ പിശക് സന്ദേശങ്ങളോടെ സമഗ്രമായ പിശക് മാനേജ്മെന്റ്  
- **ലൈഫ്‌സൈക്കിൾ മാനേജ്മെന്റ്**: ശരിയായ സ്റ്റാർട്ടപ്പ്/ഷട്ട്ഡൗൺ, റിസോഴ്‌സ് ക്ലീനപ്പ്  
- **ഹെൽത്ത് മോണിറ്ററിംഗ്**: ഇൻബിൽറ്റ് ഹെൽത്ത് ചെക്ക് എന്റ്പോയിന്റുകൾ  
- **ഡെവലപ്പ്മെന്റ് പിന്തുണ**: ഹോട്ട് റീലോഡ്, ഡീബഗ്ഗിംഗ് കഴിവുകൾ

## 🏥 ഹെൽത്ത് മോണിറ്ററിംഗ്

### ഹെൽത്ത് ചെക്ക് നടപ്പാക്കൽ (`health_check.py`)

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
        
        # ഡാറ്റാബേസ് പരിശോധിക്കുക
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
        
        # മൊത്തം നില അപ്ഡേറ്റ് ചെയ്യുക
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
            # പ്രധാന പ്രവർത്തനം പരീക്ഷിക്കുക
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

## 🧪 നിങ്ങളുടെ MCP സെർവർ ടെസ്റ്റിംഗ്

### ലോക്കൽ ടെസ്റ്റിംഗ്

1. **MCP സെർവർ ആരംഭിക്കുക**:  
   ```bash
   # വെർച്വൽ എൻവയോൺമെന്റ് സജീവമാക്കുക
   source mcp-env/bin/activate  # macOS/Linux
   # mcp-env\Scripts\activate   # Windows
   
   # സെർവർ ആരംഭിക്കുക
   cd mcp_server
   python sales_analysis.py
   ```

2. **ഹെൽത്ത് എന്റ്പോയിന്റുകൾ ടെസ്റ്റ് ചെയ്യുക**:  
   ```bash
   # അടിസ്ഥാന ആരോഗ്യ പരിശോധന
   curl http://localhost:8000/health
   
   # വിശദമായ ആരോഗ്യ പരിശോധന
   curl http://localhost:8000/health/detailed
   ```

3. **MCP ടൂളുകൾ ടെസ്റ്റ് ചെയ്യുക**:  
   ```bash
   # ലഭ്യമായ ഉപകരണങ്ങളുടെ പട്ടിക
   curl -X POST http://localhost:8000/mcp \
     -H "Content-Type: application/json" \
     -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
     -d '{"method": "tools/list", "params": {}}'
   
   # പട്ടികയുടെ സ്കീമകൾ നേടുക
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

### VS കോഡ് ഇന്റഗ്രേഷൻ ടെസ്റ്റിംഗ്

1. **VS കോഡ് MCP കോൺഫിഗർ ചെയ്യുക**:  
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

2. **AI ചാറ്റിൽ ടെസ്റ്റ് ചെയ്യുക**:  
   - VS കോഡ് AI ചാറ്റ് തുറക്കുക  
   - `#zava` ടൈപ്പ് ചെയ്ത് നിങ്ങളുടെ സെർവർ തിരഞ്ഞെടുക്കുക  
   - ചോദിക്കുക: "എന്തെല്ലാ ടേബിളുകൾ ലഭ്യമാണ്?"  
   - ചോദിക്കുക: "ഓർഡറുകളുടെ എണ്ണം അനുസരിച്ച് ടോപ്പ് 5 സ്റ്റോറുകൾ കാണിക്കുക"

### യൂണിറ്റ് ടെസ്റ്റിംഗ്

സമഗ്രമായ യൂണിറ്റ് ടെസ്റ്റുകൾ സൃഷ്ടിക്കുക:

```python
# ടെസ്റ്റുകൾ/test_mcp_server.py
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

## 🎯 പ്രധാന പഠനങ്ങൾ

ഈ ലാബ് പൂർത്തിയാക്കിയ ശേഷം, നിങ്ങൾക്ക് ഉണ്ടാകണം:

✅ **പ്രവർത്തനക്ഷമമായ MCP സെർവർ**: ഡാറ്റാബേസ് ഇന്റഗ്രേഷനോടുകൂടിയ FastMCP സെർവർ  
✅ **കോൺഫിഗറേഷൻ മാനേജ്മെന്റ്**: ശക്തമായ എൻവയോൺമെന്റ് അടിസ്ഥാനമാക്കിയ കോൺഫിഗറേഷൻ  
✅ **ഡാറ്റാബേസ് ലെയർ**: കണക്ഷൻ പൂലിംഗോടുകൂടിയ PostgreSQL ഇന്റഗ്രേഷൻ  
✅ **MCP ടൂളുകൾ**: സ്കീമ ഇൻട്രോസ്പെക്ഷനും ക്വറി എക്സിക്യൂഷനും ടൂളുകൾ  
✅ **RLS ഇന്റഗ്രേഷൻ**: റോ ലെവൽ സെക്യൂരിറ്റി കോൺടെക്സ്റ്റ് മാനേജ്മെന്റ്  
✅ **ഹെൽത്ത് മോണിറ്ററിംഗ്**: സമഗ്രമായ ഹെൽത്ത് ചെക്ക് എന്റ്പോയിന്റുകൾ  
✅ **ടെസ്റ്റിംഗ് തന്ത്രം**: ലോക്കൽ ടെസ്റ്റിംഗും VS കോഡ് ഇന്റഗ്രേഷനും

## 🚀 അടുത്തത് എന്താണ്

**[Lab 06: Tool Development](../06-Tools/README.md)** തുടർന്നു:

- നിങ്ങളുടെ MCP ടൂൾ ശേഖരം വിപുലീകരിക്കുക  
- ആഡ്വാൻസ്ഡ് ക്വറി പാറ്റേണുകൾ നടപ്പാക്കുക  
- ഡാറ്റ വാലിഡേഷൻ, ട്രാൻസ്ഫർമേഷൻ ചേർക്കുക  
- പ്രത്യേക അനലിറ്റിക്സ് ടൂളുകൾ സൃഷ്ടിക്കുക

## 📚 അധിക സ്രോതസുകൾ

### FastMCP ഫ്രെയിംവർക്ക്  
- [FastMCP ഡോക്യുമെന്റേഷൻ](https://github.com/modelcontextprotocol/python-sdk) - ഔദ്യോഗിക FastMCP ഗൈഡ്  
- [MCP സ്പെസിഫിക്കേഷൻ](https://modelcontextprotocol.io/docs/) - പ്രോട്ടോക്കോൾ സ്പെസിഫിക്കേഷൻ  
- [ടൂൾ ഡെവലപ്പ്മെന്റ് ഗൈഡ്](https://modelcontextprotocol.io/docs/tools/) - MCP ടൂളുകൾ സൃഷ്ടിക്കൽ

### ഡാറ്റാബേസ് ഇന്റഗ്രേഷൻ  
- [asyncpg ഡോക്യുമെന്റേഷൻ](https://magicstack.github.io/asyncpg/current/) - PostgreSQL അസിങ്ക് ഡ്രൈവർ  
- [കണക്ഷൻ പൂലിംഗ് മികച്ച പ്രാക്ടീസുകൾ](https://www.postgresql.org/docs/current/runtime-config-connection.html) - PostgreSQL ട്യൂണിംഗ്  
- [റോ ലെവൽ സെക്യൂരിറ്റി ഗൈഡ്](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - RLS നടപ്പാക്കൽ

### FastAPI പാറ്റേണുകൾ  
- [FastAPI ഡോക്യുമെന്റേഷൻ](https://fastapi.tiangolo.com/) - വെബ് ഫ്രെയിംവർക്ക് റഫറൻസ്  
- [ഡിപ്പെൻഡൻസി ഇൻജക്ഷൻ](https://fastapi.tiangolo.com/tutorial/dependencies/) - FastAPI പാറ്റേണുകൾ  
- [ബാക്ക്ഗ്രൗണ്ട് ടാസ്കുകൾ](https://fastapi.tiangolo.com/tutorial/background-tasks/) - അസിങ്ക് ടാസ്‌ക് മാനേജ്മെന്റ്

---

**അടുത്തത്**: നിങ്ങളുടെ ടൂളുകൾ വിപുലീകരിക്കാൻ തയ്യാറാണോ? **[Lab 06: Tool Development](../06-Tools/README.md)** തുടർന്നു.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->