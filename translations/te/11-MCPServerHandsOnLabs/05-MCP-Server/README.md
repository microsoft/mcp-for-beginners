<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "240e365cc324d23a0033e5615b5feb5e",
  "translation_date": "2025-12-11T14:33:00+00:00",
  "source_file": "11-MCPServerHandsOnLabs/05-MCP-Server/README.md",
  "language_code": "te"
}
-->
# MCP సర్వర్ అమలు

## 🎯 ఈ ప్రయోగశాలలో ఏమి నేర్చుకుంటారు

ఈ హ్యాండ్స్-ఆన్ ప్రయోగశాల FastMCP ఫ్రేమ్‌వర్క్ ఉపయోగించి ప్రొడక్షన్-రెడీ MCP సర్వర్‌ను అమలు చేయడంలో మీకు మార్గనిర్దేశం చేస్తుంది. మీరు కోర్ సర్వర్ నిర్మాణాన్ని నిర్మించి, డేటాబేస్ ఇంటిగ్రేషన్‌ను అమలు చేసి, డేటా యాక్సెస్ కోసం టూల్స్ సృష్టించి, AI ఆధారిత రిటైల్ విశ్లేషణల కోసం పునాది ఏర్పాటుచేస్తారు.

## అవలోకనం

MCP సర్వర్ మా రిటైల్ విశ్లేషణ పరిష్కారానికి హృదయం. ఇది AI అసిస్టెంట్లు మరియు PostgreSQL డేటాబేస్ మధ్య బ్రిడ్జ్‌గా పనిచేస్తుంది, వ్యాపార డేటాకు సురక్షిత, తెలివైన యాక్సెస్‌ను ఒక ప్రమాణీకృత ప్రోటోకాల్ ద్వారా అందిస్తుంది.

ఈ ప్రయోగశాల మీరు ఎంటర్‌ప్రైజ్ నమూనాలు మరియు ఉత్తమ ఆచారాలను అనుసరించి ఒక బలమైన, స్కేలబుల్ MCP సర్వర్‌ను నిర్మించడం నేర్పుతుంది.

## నేర్చుకునే లక్ష్యాలు

ఈ ప్రయోగశాల ముగింపు వరకు, మీరు చేయగలుగుతారు:

- **నిర్మించండి** సరైన ఆర్కిటెక్చర్ మరియు సంస్థతో FastMCP సర్వర్
- **అమలు చేయండి** కనెక్షన్ పూలింగ్ మరియు లోపాల నిర్వహణతో డేటాబేస్ ఇంటిగ్రేషన్
- **సృష్టించండి** డేటాబేస్ స్కీమా ఇంట్రోస్పెక్షన్ మరియు క్వెరీ అమలు కోసం MCP టూల్స్
- **కాన్ఫిగర్ చేయండి** రో లెవల్ సెక్యూరిటీ (RLS) కాంటెక్స్ట్ నిర్వహణ
- **చేర్చండి** ఆరోగ్య పర్యవేక్షణ మరియు పరిశీలన లక్షణాలు
- **పరీక్షించండి** మీ MCP సర్వర్ అమలును స్థానికంగా మరియు VS కోడ్‌తో

## 📁 ప్రాజెక్ట్ నిర్మాణం

MCP సర్వర్ సంస్థను పరిశీలిద్దాం:

```
mcp_server/
├── __init__.py                 # Package initialization
├── config.py                   # Configuration management
├── health_check.py             # Health monitoring endpoints
├── sales_analysis.py           # Main MCP server implementation
├── sales_analysis_postgres.py  # Database integration layer
└── sales_analysis_text_embeddings.py  # AI/semantic search integration
```

## 🔧 కాన్ఫిగరేషన్ నిర్వహణ

### ఎన్విరాన్‌మెంట్ కాన్ఫిగరేషన్ (`config.py`)

ముందుగా, బలమైన కాన్ఫిగరేషన్ సిస్టమ్‌ను సృష్టిద్దాం:

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

# .env ఫైల్ నుండి వాతావరణ చరాలు లోడ్ చేయండి
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
                'jit': 'off',  # స్థిరత్వం కోసం JIT ను నిలిపివేయండి
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
        
        # కాన్ఫిగరేషన్‌ను ధృవీకరించండి
        self._validate_config()
    
    def _validate_config(self):
        """Validate configuration and log warnings for missing values."""
        if not self.database.password:
            logger.warning("Database password is empty. This may cause connection issues.")
        
        if not self.azure.is_configured():
            logger.warning("Azure configuration is incomplete. AI features may not work.")
        
        logger.info(f"Configuration loaded - Database: {self.database.host}:{self.database.port}")
        logger.info(f"Server will run on {self.server.host}:{self.server.port}")

# గ్లోబల్ కాన్ఫిగరేషన్ ఉదాహరణ
config = MCPServerConfig()
```

### ముఖ్యమైన కాన్ఫిగరేషన్ లక్షణాలు

- **ఎన్విరాన్‌మెంట్ వేరియబుల్ లోడింగ్**: ఆటోమేటిక్ .env ఫైల్ మద్దతు
- **టైప్ సేఫ్టీ**: డేటాక్లాస్ ధృవీకరణ మరియు టైప్ సూచనలు
- **ఫ్లెక్సిబుల్ డిఫాల్ట్స్**: అభివృద్ధికి అనుకూలమైన డిఫాల్ట్స్
- **ధృవీకరణ**: సహాయక లోప సందేశాలతో కాన్ఫిగరేషన్ ధృవీకరణ
- **సెక్యూరిటీ**: సున్నితమైన విలువలు కేవలం ఎన్విరాన్‌మెంట్ వేరియబుల్స్ నుండి

## 🗄️ డేటాబేస్ ఇంటిగ్రేషన్ లేయర్

### PostgreSQL ప్రొవైడర్ (`sales_analysis_postgres.py`)

డేటాబేస్ ఇంటిగ్రేషన్ లేయర్‌ను అమలు చేద్దాం:

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
                    max_inactive_connection_lifetime=300  # 5 నిమిషాలు
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
            
            # స్కీమా మరియు పట్టిక పేరును పార్స్ చేయండి
            if '.' in table_name:
                schema_name, table_name = table_name.split('.', 1)
            else:
                schema_name = 'retail'  # డిఫాల్ట్ స్కీమా
            
            # కాలమ్ సమాచారం పొందండి
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
            
            # ఫారెన్ కీ సంబంధాలను పొందండి
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
            
            # సూచికలను పొందండి
            index_query = """
                SELECT 
                    indexname,
                    indexdef
                FROM pg_indexes 
                WHERE schemaname = $1 AND tablename = $2
            """
            
            indexes = await conn.fetch(index_query, schema_name, table_name)
            
            # స్కీమా సమాచారాన్ని ఫార్మాట్ చేయండి
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
        
        # కాలమ్ నిర్వచనాలను సృష్టించండి
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
        
        # ఫారెన్ కీ సమాచారాన్ని సృష్టించండి
        fk_lines = []
        for fk in foreign_keys:
            fk_lines.append(f"  {fk['column']} -> {fk['references']}")
        
        # చదవదగిన ఫార్మాట్‌లో కలపండి
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
                # ఒక క్వెరీ టైమౌట్ సెట్ చేయండి
                rows = await asyncio.wait_for(
                    conn.fetch(sql_query),
                    timeout=config.database.command_timeout
                )
                
                if not rows:
                    return "Query executed successfully. No rows returned."
                
                # ఫలితాల సెట్ పరిమితి
                limited_rows = rows[:max_rows]
                
                # ఫలితాలను ఫార్మాట్ చేయండి
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
        
        # కాలమ్ పేర్లను పొందండి
        columns = list(rows[0].keys())
        
        # హెడ్డర్ సృష్టించండి
        result_lines = [f"Results ({len(rows)} of {total_rows} rows):"]
        result_lines.append("=" * 50)
        
        # కాలమ్ హెడ్డర్లను జోడించండి
        header = " | ".join(columns)
        result_lines.append(header)
        result_lines.append("-" * len(header))
        
        # డేటా వరుసలను జోడించండి
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
        
        # అవసరమైతే ట్రంకేషన్ నోటీసును జోడించండి
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
                # సాదా కనెక్టివిటీ పరీక్ష
                result = await conn.fetchval("SELECT 1")
                
                # పూల్ స్థితిని తనిఖీ చేయండి
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

# గ్లోబల్ డేటాబేస్ ప్రొవైడర్ ఉదాహరణ
db_provider = PostgreSQLSchemaProvider()
```

### ముఖ్యమైన డేటాబేస్ లేయర్ లక్షణాలు

- **కనెక్షన్ పూలింగ్**: asyncpg తో సమర్థవంతమైన వనరుల నిర్వహణ
- **RLS ఇంటిగ్రేషన్**: ఆటోమేటిక్ రో లెవల్ సెక్యూరిటీ కాంటెక్స్ట్ సెట్టింగ్
- **స్కీమా ఇంట్రోస్పెక్షన్**: డైనమిక్ టేబుల్ స్కీమా కనుగొనడం
- **లోపాల నిర్వహణ**: సమగ్ర లోప నిర్వహణ మరియు లాగింగ్
- **క్వెరీ ఫార్మాటింగ్**: AI-స్నేహపూర్వక ఫలితాల ఫార్మాటింగ్
- **ఆరోగ్య పర్యవేక్షణ**: డేటాబేస్ కనెక్టివిటీ మరియు పూల్ స్థితి తనిఖీలు

## 🔧 ప్రధాన MCP సర్వర్ అమలు

### FastMCP సర్వర్ (`sales_analysis.py`)

ఇప్పుడు ప్రధాన MCP సర్వర్‌ను అమలు చేద్దాం:

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

# లాగింగ్‌ను కాన్ఫిగర్ చేయండి
logging.basicConfig(
    level=getattr(logging, config.server.log_level),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# FastMCP సర్వర్ ఇన్స్టాన్స్ సృష్టించండి
mcp = FastMCP("Zava Retail Sales Analysis")

# స్కీమా యాక్సెస్ కోసం చెల్లుబాటు అయ్యే పట్టికల జాబితా
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
    # HTTP మోడ్‌లో, హెడ్డర్ల నుండి పొందండి
    if hasattr(ctx, 'headers') and ctx.headers:
        rls_user_id = ctx.headers.get("x-rls-user-id")
        if rls_user_id:
            logger.debug(f"RLS User ID from headers: {rls_user_id}")
            return rls_user_id
    
    # అభివృద్ధి/పరీక్ష కోసం డిఫాల్ట్ ఫాల్బ్యాక్
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
    
    # పట్టిక పేర్లను ధృవీకరించండి
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

# అప్లికేషన్ జీవన చక్ర నిర్వహణ
@asynccontextmanager
async def lifespan(app):
    """Manage application startup and shutdown."""
    logger.info("Starting Zava Retail MCP Server...")
    
    try:
        # డేటాబేస్ కనెక్షన్ పూల్‌ను ప్రారంభించండి
        await db_provider.create_pool()
        logger.info("Database connection pool initialized")
        
        # డేటాబేస్ కనెక్టివిటీని పరీక్షించండి
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
        # శుభ్రపరచడం
        logger.info("Shutting down MCP Server...")
        await db_provider.close_pool()
        logger.info("MCP Server shutdown complete")

# సర్వర్ అప్లికేషన్‌ను కాన్ఫిగర్ చేయండి
def create_app():
    """Create and configure the MCP server application."""
    
    # FastMCP యాప్ ఇన్స్టాన్స్‌ను పొందండి
    app = mcp.sse_app()
    
    # జీవన చక్ర నిర్వహణను సెట్ చేయండి
    app.router.lifespan_context = lifespan
    
    # ఎనేబుల్ అయితే హెల్త్ చెక్ ఎండ్పాయింట్లను జోడించండి
    if config.server.enable_health_check:
        setup_health_endpoints(app, db_provider)
    
    # ఎనేబుల్ అయితే CORS ను కాన్ఫిగర్ చేయండి
    if config.server.enable_cors:
        from fastapi.middleware.cors import CORSMiddleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # ఉత్పత్తి కోసం తగిన విధంగా కాన్ఫిగర్ చేయండి
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    logger.info(f"MCP Server configured - CORS: {config.server.enable_cors}, Health: {config.server.enable_health_check}")
    
    return app

# అప్లికేషన్ ఇన్స్టాన్స్ సృష్టించండి
app = create_app()

# అభివృద్ధి కోసం ప్రధాన ప్రవేశ బిందువు
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

### ముఖ్యమైన MCP సర్వర్ లక్షణాలు

- **టూల్ రిజిస్ట్రేషన్**: టైప్ సేఫ్టీతో డిక్లరేటివ్ టూల్ నిర్వచనలు
- **RLS కాంటెక్స్ట్ నిర్వహణ**: ఆటోమేటిక్ యూజర్ ఐడెంటిటీ ఎక్స్‌ట్రాక్షన్ మరియు కాంటెక్స్ట్ సెట్టింగ్
- **లోపాల నిర్వహణ**: వినియోగదారులకు స్నేహపూర్వక సందేశాలతో సమగ్ర లోప నిర్వహణ
- **లైఫ్‌సైకిల్ నిర్వహణ**: సరైన స్టార్ట్‌అప్/షట్‌డౌన్ మరియు వనరు శుభ్రపరిచే ప్రక్రియ
- **ఆరోగ్య పర్యవేక్షణ**: బిల్ట్-ఇన్ ఆరోగ్య తనిఖీ ఎండ్పాయింట్లు
- **అభివృద్ధి మద్దతు**: హాట్ రీలోడ్ మరియు డీబగ్గింగ్ సామర్థ్యాలు

## 🏥 ఆరోగ్య పర్యవేక్షణ

### ఆరోగ్య తనిఖీ అమలు (`health_check.py`)

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
        
        # డేటాబేస్‌ను తనిఖీ చేయండి
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
        
        # మొత్తం స్థితిని నవీకరించండి
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
            # కీలక ఫంక్షనాలిటీని పరీక్షించండి
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

## 🧪 మీ MCP సర్వర్‌ను పరీక్షించడం

### స్థానిక పరీక్ష

1. **MCP సర్వర్ ప్రారంభించండి**:
   ```bash
   # వర్చువల్ ఎన్విరాన్‌మెంట్‌ను ప్రారంభించండి
   source mcp-env/bin/activate  # macOS/Linux
   # mcp-env\Scripts\activate   # Windows
   
   # సర్వర్‌ను ప్రారంభించండి
   cd mcp_server
   python sales_analysis.py
   ```

2. **ఆరోగ్య ఎండ్పాయింట్లను పరీక్షించండి**:
   ```bash
   # ప్రాథమిక ఆరోగ్య తనిఖీ
   curl http://localhost:8000/health
   
   # విపులమైన ఆరోగ్య తనిఖీ
   curl http://localhost:8000/health/detailed
   ```

3. **MCP టూల్స్‌ను పరీక్షించండి**:
   ```bash
   # అందుబాటులో ఉన్న సాధనాలను జాబితా చేయండి
   curl -X POST http://localhost:8000/mcp \
     -H "Content-Type: application/json" \
     -H "x-rls-user-id: 00000000-0000-0000-0000-000000000000" \
     -d '{"method": "tools/list", "params": {}}'
   
   # పట్టిక స్కీమాలను పొందండి
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

### VS కోడ్ ఇంటిగ్రేషన్ పరీక్ష

1. **VS కోడ్ MCP కాన్ఫిగర్ చేయండి**:
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

2. **AI చాట్‌లో పరీక్షించండి**:
   - VS కోడ్ AI చాట్ తెరవండి
   - `#zava` టైప్ చేసి మీ సర్వర్‌ను ఎంచుకోండి
   - అడగండి: "ఏ టేబుల్స్ అందుబాటులో ఉన్నాయి?"
   - అడగండి: "ఆర్డర్ల సంఖ్య ఆధారంగా టాప్ 5 స్టోర్లను చూపించండి"

### యూనిట్ పరీక్ష

సమగ్ర యూనిట్ పరీక్షలను సృష్టించండి:

```python
# పరీక్షలు/test_mcp_server.py
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

## 🎯 ముఖ్యమైన పాఠాలు

ఈ ప్రయోగశాల పూర్తి చేసిన తర్వాత, మీ వద్ద ఉండాలి:

✅ **పనిచేసే MCP సర్వర్**: డేటాబేస్ ఇంటిగ్రేషన్‌తో FastMCP సర్వర్  
✅ **కాన్ఫిగరేషన్ నిర్వహణ**: బలమైన ఎన్విరాన్‌మెంట్ ఆధారిత కాన్ఫిగరేషన్  
✅ **డేటాబేస్ లేయర్**: కనెక్షన్ పూలింగ్‌తో PostgreSQL ఇంటిగ్రేషన్  
✅ **MCP టూల్స్**: స్కీమా ఇంట్రోస్పెక్షన్ మరియు క్వెరీ అమలు టూల్స్  
✅ **RLS ఇంటిగ్రేషన్**: రో లెవల్ సెక్యూరిటీ కాంటెక్స్ట్ నిర్వహణ  
✅ **ఆరోగ్య పర్యవేక్షణ**: సమగ్ర ఆరోగ్య తనిఖీ ఎండ్పాయింట్లు  
✅ **పరీక్షా వ్యూహం**: స్థానిక పరీక్ష మరియు VS కోడ్ ఇంటిగ్రేషన్  

## 🚀 తదుపరి ఏమిటి

**[Lab 06: Tool Development](../06-Tools/README.md)** తో కొనసాగండి:

- మీ MCP టూల్ సేకరణను విస్తరించండి
- అధునాతన క్వెరీ నమూనాలను అమలు చేయండి
- డేటా ధృవీకరణ మరియు మార్పిడి చేర్చండి
- ప్రత్యేక విశ్లేషణ టూల్స్ సృష్టించండి

## 📚 అదనపు వనరులు

### FastMCP ఫ్రేమ్‌వర్క్
- [FastMCP డాక్యుమెంటేషన్](https://github.com/modelcontextprotocol/python-sdk) - అధికారిక FastMCP గైడ్
- [MCP స్పెసిఫికేషన్](https://modelcontextprotocol.io/docs/) - ప్రోటోకాల్ స్పెసిఫికేషన్
- [టూల్ డెవలప్‌మెంట్ గైడ్](https://modelcontextprotocol.io/docs/tools/) - MCP టూల్స్ సృష్టించడం

### డేటాబేస్ ఇంటిగ్రేషన్
- [asyncpg డాక్యుమెంటేషన్](https://magicstack.github.io/asyncpg/current/) - PostgreSQL async డ్రైవర్
- [కనెక్షన్ పూలింగ్ ఉత్తమ ఆచారాలు](https://www.postgresql.org/docs/current/runtime-config-connection.html) - PostgreSQL ట్యూనింగ్
- [రో లెవల్ సెక్యూరిటీ గైడ్](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - RLS అమలు

### FastAPI నమూనాలు
- [FastAPI డాక్యుమెంటేషన్](https://fastapi.tiangolo.com/) - వెబ్ ఫ్రేమ్‌వర్క్ సూచిక
- [డిపెండెన్సీ ఇంజెక్షన్](https://fastapi.tiangolo.com/tutorial/dependencies/) - FastAPI నమూనాలు
- [బ్యాక్‌గ్రౌండ్ టాస్క్స్](https://fastapi.tiangolo.com/tutorial/background-tasks/) - అసింక్ టాస్క్ నిర్వహణ

---

**తదుపరి**: మీ టూల్స్‌ను విస్తరించడానికి సిద్ధంగా ఉన్నారా? [Lab 06: Tool Development](../06-Tools/README.md) తో కొనసాగండి

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->