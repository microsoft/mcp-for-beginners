# توسعه ابزار

## 🎯 این آزمایش چه چیزی را پوشش می‌دهد

این آزمایش به طور عمیق به ایجاد ابزارهای پیشرفته MCP می‌پردازد که به دستیاران هوش مصنوعی قابلیت‌های قدرتمند برای پرس‌وجوی پایگاه داده، بررسی ساختار (schema introspection) و عملکردهای تحلیلی ارائه می‌دهند. شما یاد خواهید گرفت که ابزارهایی بسازید که هم قدرتمند و هم ایمن باشند، با مدیریت جامع خطا و بهینه‌سازی عملکرد.

## مرور کلی

ابزارهای MCP رابط بین دستیاران هوش مصنوعی و سیستم‌های داده شما هستند. ابزارهای خوب طراحی‌شده دسترسی ساختاریافته و معتبر به عملیات پیچیده را فراهم می‌کنند و در عین حال امنیت و عملکرد را حفظ می‌کنند. این آزمایش چرخه کامل توسعه ابزار از طراحی تا استقرار را پوشش می‌دهد.

سرور MCP خرده‌فروشی ما مجموعه کاملی از ابزارها را پیاده‌سازی می‌کند که امکان پرس‌وجوی طبیعی داده‌های فروش، کاتالوگ محصولات و تحلیل‌های کسب‌وکار را فراهم می‌کند، در حالی که مرزهای امنیتی سختگیرانه و عملکرد بهینه را حفظ می‌کند.

## اهداف یادگیری

تا پایان این آزمایش، شما قادر خواهید بود:

- **طراحی** ابزارهای پیشرفته MCP با اعتبارسنجی پارامترهای پیچیده  
- **پیاده‌سازی** ابزارهای پرس‌وجوی پایگاه داده ایمن با حفاظت در برابر تزریق SQL  
- **ایجاد** قابلیت‌های بررسی ساختار برای پرس‌وجوهای پویا  
- **ساخت** ابزارهای تحلیلی سفارشی برای هوش تجاری  
- **اعمال** مدیریت جامع خطا و کاهش تدریجی مشکلات  
- **بهینه‌سازی** عملکرد ابزار برای بارهای کاری تولیدی  

## 🛠️ معماری اصلی ابزار

### اصول طراحی ابزار

```python
# mcp_server/tools/base.py
"""
Base classes and patterns for MCP tool development.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from enum import Enum
import asyncio
import time
import logging
from contextlib import asynccontextmanager

logger = logging.getLogger(__name__)

class ToolCategory(Enum):
    """Tool categorization for organization and discovery."""
    DATABASE_QUERY = "database_query"
    SCHEMA_INTROSPECTION = "schema_introspection"
    ANALYTICS = "analytics"
    UTILITY = "utility"
    ADMINISTRATIVE = "administrative"

@dataclass
class ToolResult:
    """Standardized tool result structure."""
    success: bool
    data: Any = None
    error: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    execution_time_ms: Optional[float] = None
    row_count: Optional[int] = None

class BaseTool(ABC):
    """Abstract base class for all MCP tools."""
    
    def __init__(self, name: str, description: str, category: ToolCategory):
        self.name = name
        self.description = description
        self.category = category
        self.call_count = 0
        self.total_execution_time = 0.0
        
    @abstractmethod
    async def execute(self, **kwargs) -> ToolResult:
        """Execute the tool with given parameters."""
        pass
    
    @abstractmethod
    def get_input_schema(self) -> Dict[str, Any]:
        """Get JSON schema for tool input validation."""
        pass
    
    async def call(self, **kwargs) -> ToolResult:
        """Wrapper for tool execution with metrics and error handling."""
        
        start_time = time.time()
        self.call_count += 1
        
        try:
            # Validate input parameters
            self._validate_input(kwargs)
            
            # Log tool execution
            logger.info(
                f"Executing tool: {self.name}",
                extra={
                    'tool_name': self.name,
                    'tool_category': self.category.value,
                    'parameters': self._sanitize_parameters(kwargs)
                }
            )
            
            # Execute the tool
            result = await self.execute(**kwargs)
            
            # Record execution time
            execution_time = (time.time() - start_time) * 1000
            result.execution_time_ms = execution_time
            self.total_execution_time += execution_time
            
            # Log success
            logger.info(
                f"Tool execution completed: {self.name}",
                extra={
                    'tool_name': self.name,
                    'execution_time_ms': execution_time,
                    'success': result.success,
                    'row_count': result.row_count
                }
            )
            
            return result
            
        except Exception as e:
            execution_time = (time.time() - start_time) * 1000
            
            logger.error(
                f"Tool execution failed: {self.name}",
                extra={
                    'tool_name': self.name,
                    'execution_time_ms': execution_time,
                    'error': str(e)
                },
                exc_info=True
            )
            
            return ToolResult(
                success=False,
                error=f"Tool execution failed: {str(e)}",
                execution_time_ms=execution_time
            )
    
    def _validate_input(self, kwargs: Dict[str, Any]):
        """Validate input parameters against schema."""
        
        schema = self.get_input_schema()
        required_props = schema.get('required', [])
        properties = schema.get('properties', {})
        
        # Check required parameters
        missing_required = [prop for prop in required_props if prop not in kwargs]
        if missing_required:
            raise ValueError(f"Missing required parameters: {missing_required}")
        
        # Type validation would go here
        # For production, use jsonschema library for comprehensive validation
    
    def _sanitize_parameters(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """Sanitize parameters for logging (remove sensitive data)."""
        
        # Remove or mask sensitive parameters
        sanitized = kwargs.copy()
        sensitive_keys = ['password', 'token', 'secret', 'key']
        
        for key in sanitized:
            if any(sensitive in key.lower() for sensitive in sensitive_keys):
                sanitized[key] = "***MASKED***"
        
        return sanitized
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get tool usage statistics."""
        
        return {
            'name': self.name,
            'category': self.category.value,
            'call_count': self.call_count,
            'total_execution_time_ms': self.total_execution_time,
            'average_execution_time_ms': (
                self.total_execution_time / self.call_count 
                if self.call_count > 0 else 0
            )
        }

class DatabaseTool(BaseTool):
    """Base class for database-related tools."""
    
    def __init__(self, name: str, description: str, db_provider):
        super().__init__(name, description, ToolCategory.DATABASE_QUERY)
        self.db_provider = db_provider
    
    @asynccontextmanager
    async def get_connection(self):
        """Get database connection with proper context management."""
        
        conn = None
        try:
            conn = await self.db_provider.get_connection()
            yield conn
        finally:
            if conn:
                await self.db_provider.release_connection(conn)
    
    async def execute_query(
        self, 
        query: str, 
        params: tuple = None,
        store_id: str = None
    ) -> ToolResult:
        """Execute database query with security and performance monitoring."""
        
        async with self.get_connection() as conn:
            try:
                # Set store context if provided
                if store_id:
                    await conn.execute("SELECT retail.set_store_context($1)", store_id)
                
                # Execute query
                start_time = time.time()
                
                if params:
                    rows = await conn.fetch(query, *params)
                else:
                    rows = await conn.fetch(query)
                
                execution_time = (time.time() - start_time) * 1000
                
                # Convert rows to dictionaries
                data = [dict(row) for row in rows]
                
                return ToolResult(
                    success=True,
                    data=data,
                    row_count=len(data),
                    execution_time_ms=execution_time
                )
                
            except Exception as e:
                logger.error(f"Database query failed: {str(e)}")
                return ToolResult(
                    success=False,
                    error=f"Query execution failed: {str(e)}"
                )
```
  
### اعتبارسنجی پرس‌وجو و امنیت

```python
# mcp_server/tools/query_validator.py
"""
SQL query validation and security for MCP tools.
"""
import re
import sqlparse
from typing import List, Dict, Any, Set
from enum import Enum

class QueryRisk(Enum):
    """Query risk levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class QueryValidator:
    """Validate and analyze SQL queries for security risks."""
    
    # Dangerous SQL keywords and patterns
    DANGEROUS_KEYWORDS = {
        'DROP', 'DELETE', 'TRUNCATE', 'ALTER', 'CREATE', 'INSERT',
        'UPDATE', 'GRANT', 'REVOKE', 'EXEC', 'EXECUTE', 'sp_',
        'xp_', 'BULK', 'OPENROWSET', 'OPENDATASOURCE'
    }
    
    # Allowed read-only operations
    SAFE_KEYWORDS = {
        'SELECT', 'WITH', 'UNION', 'ORDER', 'GROUP', 'HAVING',
        'WHERE', 'FROM', 'JOIN', 'AS', 'ON', 'IN', 'EXISTS',
        'CASE', 'WHEN', 'THEN', 'ELSE', 'END', 'AND', 'OR', 'NOT'
    }
    
    # Allowed schemas and tables
    ALLOWED_SCHEMAS = {'retail', 'information_schema', 'pg_catalog'}
    ALLOWED_TABLES = {
        'customers', 'products', 'sales_transactions', 
        'sales_transaction_items', 'product_categories',
        'product_embeddings', 'stores'
    }
    
    def __init__(self):
        self.injection_patterns = [
            # SQL injection patterns
            r"(\b(UNION|union)\s+(ALL\s+)?(SELECT|select))",
            r"(\b(DROP|drop)\s+(TABLE|table|DATABASE|database))",
            r"(\b(DELETE|delete)\s+(FROM|from))",
            r"(\b(INSERT|insert)\s+(INTO|into))",
            r"(\b(UPDATE|update)\s+\w+\s+(SET|set))",
            r"(\b(EXEC|exec|EXECUTE|execute)\s*\()",
            r"(\b(sp_|xp_)\w+)",
            r"(--\s*$)",  # SQL comments
            r"(/\*.*?\*/)",  # Block comments
            r"(;\s*(DROP|DELETE|INSERT|UPDATE|CREATE|ALTER))",
            r"(\bOR\b\s+['\"]?\w+['\"]?\s*=\s*['\"]?\w+['\"]?)",  # OR injection
            r"(\bAND\b\s+['\"]?\w+['\"]?\s*=\s*['\"]?\w+['\"]?)",  # AND injection
        ]
        
        self.compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in self.injection_patterns]
    
    def validate_query(self, query: str) -> Dict[str, Any]:
        """Comprehensive query validation."""
        
        validation_result = {
            'is_safe': True,
            'risk_level': QueryRisk.LOW,
            'issues': [],
            'warnings': [],
            'allowed_operations': [],
            'metadata': {}
        }
        
        try:
            # Parse the query
            parsed = sqlparse.parse(query)
            
            if not parsed:
                validation_result['is_safe'] = False
                validation_result['issues'].append("Unable to parse query")
                validation_result['risk_level'] = QueryRisk.HIGH
                return validation_result
            
            # Analyze each statement
            for statement in parsed:
                self._analyze_statement(statement, validation_result)
            
            # Check for injection patterns
            self._check_injection_patterns(query, validation_result)
            
            # Validate table/schema access
            self._validate_table_access(query, validation_result)
            
            # Determine final risk level
            self._determine_risk_level(validation_result)
            
        except Exception as e:
            validation_result['is_safe'] = False
            validation_result['issues'].append(f"Query analysis failed: {str(e)}")
            validation_result['risk_level'] = QueryRisk.CRITICAL
        
        return validation_result
    
    def _analyze_statement(self, statement, validation_result):
        """Analyze individual SQL statement."""
        
        # Get statement type
        stmt_type = statement.get_type()
        
        # Check if statement type is allowed
        if stmt_type and stmt_type.upper() not in ['SELECT', 'WITH']:
            validation_result['issues'].append(f"Disallowed statement type: {stmt_type}")
            validation_result['is_safe'] = False
            return
        
        # Extract tokens and analyze
        for token in statement.flatten():
            if token.ttype is sqlparse.tokens.Keyword:
                keyword = token.value.upper()
                
                if keyword in self.DANGEROUS_KEYWORDS:
                    validation_result['issues'].append(f"Dangerous keyword detected: {keyword}")
                    validation_result['is_safe'] = False
                elif keyword in self.SAFE_KEYWORDS:
                    if keyword not in validation_result['allowed_operations']:
                        validation_result['allowed_operations'].append(keyword)
    
    def _check_injection_patterns(self, query: str, validation_result):
        """Check for SQL injection patterns."""
        
        for pattern in self.compiled_patterns:
            matches = pattern.findall(query)
            if matches:
                validation_result['issues'].append(f"Potential injection pattern detected")
                validation_result['is_safe'] = False
    
    def _validate_table_access(self, query: str, validation_result):
        """Validate that only allowed tables/schemas are accessed."""
        
        # Extract table names (simplified approach)
        # In production, use proper SQL parsing
        from_match = re.findall(r'FROM\s+(\w+\.?\w*)', query, re.IGNORECASE)
        join_match = re.findall(r'JOIN\s+(\w+\.?\w*)', query, re.IGNORECASE)
        
        all_tables = from_match + join_match
        
        for table_ref in all_tables:
            if '.' in table_ref:
                schema, table = table_ref.split('.', 1)
                if schema.lower() not in self.ALLOWED_SCHEMAS:
                    validation_result['issues'].append(f"Access to unauthorized schema: {schema}")
                    validation_result['is_safe'] = False
                if table.lower() not in self.ALLOWED_TABLES:
                    validation_result['warnings'].append(f"Access to table: {table}")
            else:
                # Assume retail schema if not specified
                if table_ref.lower() not in self.ALLOWED_TABLES:
                    validation_result['warnings'].append(f"Access to table: {table_ref}")
    
    def _determine_risk_level(self, validation_result):
        """Determine overall risk level."""
        
        if not validation_result['is_safe']:
            if any('injection' in issue.lower() for issue in validation_result['issues']):
                validation_result['risk_level'] = QueryRisk.CRITICAL
            elif any('DROP' in issue or 'DELETE' in issue for issue in validation_result['issues']):
                validation_result['risk_level'] = QueryRisk.HIGH
            else:
                validation_result['risk_level'] = QueryRisk.MEDIUM
        elif validation_result['warnings']:
            validation_result['risk_level'] = QueryRisk.LOW
        else:
            validation_result['risk_level'] = QueryRisk.LOW

# Global validator instance
query_validator = QueryValidator()
```
  

## 🗃️ ابزارهای پرس‌وجوی پایگاه داده

### ابزار تحلیل فروش

```python
# mcp_server/tools/sales_analysis.py
"""
Comprehensive sales analysis tool for retail data querying.
"""
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from .base import DatabaseTool, ToolResult
from .query_validator import query_validator

class SalesAnalysisTool(DatabaseTool):
    """Advanced sales analysis and reporting tool."""
    
    def __init__(self, db_provider):
        super().__init__(
            name="execute_sales_query",
            description="Execute sophisticated sales analysis queries with natural language support",
            db_provider=db_provider
        )
        
        # Pre-built query templates for common analysis
        self.query_templates = {
            'daily_sales': """
                SELECT 
                    DATE(transaction_date) as sales_date,
                    COUNT(*) as transaction_count,
                    SUM(total_amount) as total_revenue,
                    AVG(total_amount) as avg_transaction_value,
                    COUNT(DISTINCT customer_id) as unique_customers
                FROM retail.sales_transactions 
                WHERE transaction_date >= $1 AND transaction_date <= $2
                  AND transaction_type = 'sale'
                GROUP BY DATE(transaction_date)
                ORDER BY sales_date DESC
            """,
            
            'top_products': """
                SELECT 
                    p.product_name,
                    p.brand,
                    SUM(sti.quantity) as total_quantity_sold,
                    SUM(sti.total_price) as total_revenue,
                    COUNT(DISTINCT st.transaction_id) as transaction_count,
                    AVG(sti.unit_price) as avg_price
                FROM retail.sales_transaction_items sti
                JOIN retail.sales_transactions st ON sti.transaction_id = st.transaction_id
                JOIN retail.products p ON sti.product_id = p.product_id
                WHERE st.transaction_date >= $1 AND st.transaction_date <= $2
                  AND st.transaction_type = 'sale'
                GROUP BY p.product_id, p.product_name, p.brand
                ORDER BY total_revenue DESC
                LIMIT $3
            """,
            
            'customer_analysis': """
                SELECT 
                    c.customer_id,
                    c.first_name || ' ' || c.last_name as customer_name,
                    c.loyalty_tier,
                    COUNT(st.transaction_id) as transaction_count,
                    SUM(st.total_amount) as total_spent,
                    AVG(st.total_amount) as avg_transaction_value,
                    MAX(st.transaction_date) as last_purchase_date,
                    DATE_PART('day', CURRENT_DATE - MAX(st.transaction_date)) as days_since_last_purchase
                FROM retail.customers c
                LEFT JOIN retail.sales_transactions st ON c.customer_id = st.customer_id
                WHERE st.transaction_date >= $1 AND st.transaction_date <= $2
                  AND st.transaction_type = 'sale'
                GROUP BY c.customer_id, c.first_name, c.last_name, c.loyalty_tier
                HAVING COUNT(st.transaction_id) > 0
                ORDER BY total_spent DESC
                LIMIT $3
            """,
            
            'category_performance': """
                SELECT 
                    pc.category_name,
                    COUNT(DISTINCT p.product_id) as unique_products,
                    SUM(sti.quantity) as total_quantity_sold,
                    SUM(sti.total_price) as total_revenue,
                    AVG(sti.unit_price) as avg_price,
                    COUNT(DISTINCT st.transaction_id) as transaction_count
                FROM retail.product_categories pc
                JOIN retail.products p ON pc.category_id = p.category_id
                JOIN retail.sales_transaction_items sti ON p.product_id = sti.product_id
                JOIN retail.sales_transactions st ON sti.transaction_id = st.transaction_id
                WHERE st.transaction_date >= $1 AND st.transaction_date <= $2
                  AND st.transaction_type = 'sale'
                GROUP BY pc.category_id, pc.category_name
                ORDER BY total_revenue DESC
            """,
            
            'sales_trends': """
                WITH daily_sales AS (
                    SELECT 
                        DATE(transaction_date) as sales_date,
                        SUM(total_amount) as daily_revenue,
                        COUNT(*) as daily_transactions
                    FROM retail.sales_transactions 
                    WHERE transaction_date >= $1 AND transaction_date <= $2
                      AND transaction_type = 'sale'
                    GROUP BY DATE(transaction_date)
                ),
                trend_analysis AS (
                    SELECT 
                        sales_date,
                        daily_revenue,
                        daily_transactions,
                        LAG(daily_revenue, 1) OVER (ORDER BY sales_date) as prev_day_revenue,
                        LAG(daily_revenue, 7) OVER (ORDER BY sales_date) as prev_week_revenue,
                        AVG(daily_revenue) OVER (
                            ORDER BY sales_date 
                            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
                        ) as rolling_7day_avg
                    FROM daily_sales
                )
                SELECT 
                    sales_date,
                    daily_revenue,
                    daily_transactions,
                    rolling_7day_avg,
                    CASE 
                        WHEN prev_day_revenue IS NOT NULL THEN
                            ROUND(((daily_revenue - prev_day_revenue) / prev_day_revenue * 100)::numeric, 2)
                        ELSE NULL
                    END as day_over_day_growth_pct,
                    CASE 
                        WHEN prev_week_revenue IS NOT NULL THEN
                            ROUND(((daily_revenue - prev_week_revenue) / prev_week_revenue * 100)::numeric, 2)
                        ELSE NULL
                    END as week_over_week_growth_pct
                FROM trend_analysis
                ORDER BY sales_date DESC
            """
        }
    
    async def execute(self, **kwargs) -> ToolResult:
        """Execute sales analysis query."""
        
        query_type = kwargs.get('query_type', 'custom')
        store_id = kwargs.get('store_id')
        
        if not store_id:
            return ToolResult(
                success=False,
                error="store_id is required for sales analysis"
            )
        
        try:
            if query_type in self.query_templates:
                return await self._execute_template_query(query_type, kwargs)
            elif query_type == 'custom':
                return await self._execute_custom_query(kwargs)
            else:
                return ToolResult(
                    success=False,
                    error=f"Unknown query type: {query_type}"
                )
        
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"Sales analysis failed: {str(e)}"
            )
    
    async def _execute_template_query(self, query_type: str, kwargs: Dict[str, Any]) -> ToolResult:
        """Execute pre-built template query."""
        
        query = self.query_templates[query_type]
        store_id = kwargs['store_id']
        
        # Default parameters for template queries
        start_date = kwargs.get('start_date', (datetime.now() - timedelta(days=30)).date())
        end_date = kwargs.get('end_date', datetime.now().date())
        limit = kwargs.get('limit', 20)
        
        # Convert string dates if needed
        if isinstance(start_date, str):
            start_date = datetime.fromisoformat(start_date).date()
        if isinstance(end_date, str):
            end_date = datetime.fromisoformat(end_date).date()
        
        # Execute query with parameters
        params = (start_date, end_date, limit) if '$3' in query else (start_date, end_date)
        
        result = await self.execute_query(query, params, store_id)
        
        if result.success:
            result.metadata = {
                'query_type': query_type,
                'date_range': f"{start_date} to {end_date}",
                'store_id': store_id,
                'analysis_type': 'template'
            }
        
        return result
    
    async def _execute_custom_query(self, kwargs: Dict[str, Any]) -> ToolResult:
        """Execute custom SQL query with validation."""
        
        custom_query = kwargs.get('query')
        store_id = kwargs['store_id']
        
        if not custom_query:
            return ToolResult(
                success=False,
                error="Custom query is required when query_type is 'custom'"
            )
        
        # Validate the query for security
        validation = query_validator.validate_query(custom_query)
        
        if not validation['is_safe']:
            return ToolResult(
                success=False,
                error=f"Query validation failed: {', '.join(validation['issues'])}",
                metadata={
                    'validation_result': validation,
                    'risk_level': validation['risk_level'].value
                }
            )
        
        # Execute validated query
        result = await self.execute_query(custom_query, None, store_id)
        
        if result.success:
            result.metadata = {
                'query_type': 'custom',
                'store_id': store_id,
                'validation_warnings': validation.get('warnings', []),
                'analysis_type': 'custom'
            }
        
        return result
    
    def get_input_schema(self) -> Dict[str, Any]:
        """Get input schema for the sales analysis tool."""
        
        return {
            "type": "object",
            "properties": {
                "query_type": {
                    "type": "string",
                    "enum": list(self.query_templates.keys()) + ["custom"],
                    "description": "Type of sales analysis to perform",
                    "default": "daily_sales"
                },
                "store_id": {
                    "type": "string",
                    "description": "Store ID for data isolation",
                    "pattern": "^[a-zA-Z0-9_-]+$"
                },
                "start_date": {
                    "type": "string",
                    "format": "date",
                    "description": "Start date for analysis (YYYY-MM-DD)"
                },
                "end_date": {
                    "type": "string",
                    "format": "date",
                    "description": "End date for analysis (YYYY-MM-DD)"
                },
                "limit": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 1000,
                    "description": "Maximum number of results to return",
                    "default": 20
                },
                "query": {
                    "type": "string",
                    "description": "Custom SQL query (required when query_type is 'custom')"
                }
            },
            "required": ["store_id"],
            "additionalProperties": False
        }
```
  
### ابزار بررسی ساختار

```python
# mcp_server/tools/schema_introspection.py
"""
Database schema introspection and metadata tools.
"""
from typing import Dict, Any, List
from .base import DatabaseTool, ToolResult, ToolCategory

class SchemaIntrospectionTool(DatabaseTool):
    """Tool for exploring database schema and metadata."""
    
    def __init__(self, db_provider):
        super().__init__(
            name="get_table_schema",
            description="Get detailed schema information for database tables",
            db_provider=db_provider
        )
        self.category = ToolCategory.SCHEMA_INTROSPECTION
    
    async def execute(self, **kwargs) -> ToolResult:
        """Execute schema introspection."""
        
        table_name = kwargs.get('table_name')
        include_constraints = kwargs.get('include_constraints', True)
        include_indexes = kwargs.get('include_indexes', True)
        include_statistics = kwargs.get('include_statistics', False)
        
        try:
            if table_name:
                return await self._get_single_table_schema(
                    table_name, include_constraints, include_indexes, include_statistics
                )
            else:
                return await self._get_all_tables_schema(include_constraints, include_indexes)
        
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"Schema introspection failed: {str(e)}"
            )
    
    async def _get_single_table_schema(
        self, 
        table_name: str, 
        include_constraints: bool,
        include_indexes: bool,
        include_statistics: bool
    ) -> ToolResult:
        """Get detailed schema for a single table."""
        
        schema_info = {
            'table_name': table_name,
            'columns': [],
            'constraints': [],
            'indexes': [],
            'statistics': {}
        }
        
        async with self.get_connection() as conn:
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
                    ordinal_position,
                    udt_name
                FROM information_schema.columns
                WHERE table_schema = 'retail' AND table_name = $1
                ORDER BY ordinal_position
            """
            
            columns = await conn.fetch(columns_query, table_name)
            schema_info['columns'] = [dict(col) for col in columns]
            
            # Get constraints if requested
            if include_constraints:
                constraints_query = """
                    SELECT 
                        constraint_name,
                        constraint_type,
                        column_name,
                        foreign_table_name,
                        foreign_column_name
                    FROM information_schema.table_constraints tc
                    LEFT JOIN information_schema.key_column_usage kcu 
                        ON tc.constraint_name = kcu.constraint_name
                    LEFT JOIN information_schema.referential_constraints rc
                        ON tc.constraint_name = rc.constraint_name
                    LEFT JOIN information_schema.key_column_usage fkcu
                        ON rc.unique_constraint_name = fkcu.constraint_name
                    WHERE tc.table_schema = 'retail' AND tc.table_name = $1
                """
                
                constraints = await conn.fetch(constraints_query, table_name)
                schema_info['constraints'] = [dict(const) for const in constraints]
            
            # Get indexes if requested
            if include_indexes:
                indexes_query = """
                    SELECT 
                        indexname as index_name,
                        indexdef as index_definition,
                        tablespace
                    FROM pg_indexes
                    WHERE schemaname = 'retail' AND tablename = $1
                """
                
                indexes = await conn.fetch(indexes_query, table_name)
                schema_info['indexes'] = [dict(idx) for idx in indexes]
            
            # Get table statistics if requested
            if include_statistics:
                stats_query = """
                    SELECT 
                        n_tup_ins as inserts,
                        n_tup_upd as updates,
                        n_tup_del as deletes,
                        n_live_tup as live_tuples,
                        n_dead_tup as dead_tuples,
                        last_vacuum,
                        last_autovacuum,
                        last_analyze,
                        last_autoanalyze
                    FROM pg_stat_user_tables
                    WHERE schemaname = 'retail' AND relname = $1
                """
                
                stats = await conn.fetchrow(stats_query, table_name)
                if stats:
                    schema_info['statistics'] = dict(stats)
        
        return ToolResult(
            success=True,
            data=schema_info,
            metadata={
                'table_name': table_name,
                'schema': 'retail',
                'introspection_type': 'single_table'
            }
        )
    
    async def _get_all_tables_schema(
        self, 
        include_constraints: bool,
        include_indexes: bool
    ) -> ToolResult:
        """Get schema information for all tables."""
        
        async with self.get_connection() as conn:
            # Get all tables in retail schema
            tables_query = """
                SELECT 
                    table_name,
                    table_type
                FROM information_schema.tables
                WHERE table_schema = 'retail'
                ORDER BY table_name
            """
            
            tables = await conn.fetch(tables_query)
            schema_info = {
                'schema_name': 'retail',
                'tables': []
            }
            
            for table in tables:
                table_info = {
                    'table_name': table['table_name'],
                    'table_type': table['table_type'],
                    'columns': []
                }
                
                # Get columns for each table
                columns_query = """
                    SELECT 
                        column_name,
                        data_type,
                        is_nullable,
                        column_default
                    FROM information_schema.columns
                    WHERE table_schema = 'retail' AND table_name = $1
                    ORDER BY ordinal_position
                """
                
                columns = await conn.fetch(columns_query, table['table_name'])
                table_info['columns'] = [dict(col) for col in columns]
                
                schema_info['tables'].append(table_info)
        
        return ToolResult(
            success=True,
            data=schema_info,
            metadata={
                'schema': 'retail',
                'table_count': len(schema_info['tables']),
                'introspection_type': 'all_tables'
            }
        )
    
    def get_input_schema(self) -> Dict[str, Any]:
        """Get input schema for schema introspection tool."""
        
        return {
            "type": "object",
            "properties": {
                "table_name": {
                    "type": "string",
                    "description": "Specific table name to introspect (optional - if not provided, all tables are returned)",
                    "pattern": "^[a-zA-Z_][a-zA-Z0-9_]*$"
                },
                "include_constraints": {
                    "type": "boolean",
                    "description": "Include constraint information",
                    "default": True
                },
                "include_indexes": {
                    "type": "boolean",
                    "description": "Include index information",
                    "default": True
                },
                "include_statistics": {
                    "type": "boolean",
                    "description": "Include table statistics",
                    "default": False
                }
            },
            "additionalProperties": False
        }

class MultiTableSchemaTool(DatabaseTool):
    """Tool for getting schema information for multiple tables at once."""
    
    def __init__(self, db_provider):
        super().__init__(
            name="get_multiple_table_schemas",
            description="Get schema information for multiple tables efficiently",
            db_provider=db_provider
        )
        self.category = ToolCategory.SCHEMA_INTROSPECTION
    
    async def execute(self, **kwargs) -> ToolResult:
        """Execute multi-table schema introspection."""
        
        table_names = kwargs.get('table_names', [])
        
        if not table_names:
            return ToolResult(
                success=False,
                error="At least one table name is required"
            )
        
        try:
            schemas = {}
            
            async with self.get_connection() as conn:
                for table_name in table_names:
                    # Get table schema
                    schema_query = """
                        SELECT 
                            c.column_name,
                            c.data_type,
                            c.is_nullable,
                            c.column_default,
                            c.character_maximum_length,
                            tc.constraint_type,
                            kcu.constraint_name
                        FROM information_schema.columns c
                        LEFT JOIN information_schema.key_column_usage kcu
                            ON c.table_name = kcu.table_name 
                            AND c.column_name = kcu.column_name
                            AND c.table_schema = kcu.table_schema
                        LEFT JOIN information_schema.table_constraints tc
                            ON kcu.constraint_name = tc.constraint_name
                            AND kcu.table_schema = tc.table_schema
                        WHERE c.table_schema = 'retail' AND c.table_name = $1
                        ORDER BY c.ordinal_position
                    """
                    
                    columns = await conn.fetch(schema_query, table_name)
                    
                    if columns:
                        schemas[table_name] = {
                            'table_name': table_name,
                            'columns': [dict(col) for col in columns]
                        }
                    else:
                        schemas[table_name] = {
                            'table_name': table_name,
                            'error': 'Table not found or not accessible'
                        }
            
            return ToolResult(
                success=True,
                data=schemas,
                metadata={
                    'requested_tables': table_names,
                    'found_tables': [name for name, info in schemas.items() if 'error' not in info],
                    'missing_tables': [name for name, info in schemas.items() if 'error' in info]
                }
            )
        
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"Multi-table schema introspection failed: {str(e)}"
            )
    
    def get_input_schema(self) -> Dict[str, Any]:
        """Get input schema for multi-table schema tool."""
        
        return {
            "type": "object",
            "properties": {
                "table_names": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "pattern": "^[a-zA-Z_][a-zA-Z0-9_]*$"
                    },
                    "description": "List of table names to get schema information for",
                    "minItems": 1,
                    "maxItems": 20
                }
            },
            "required": ["table_names"],
            "additionalProperties": False
        }
```
  

## 📊 ابزارهای تحلیلی و کاربردی

### ابزار هوش تجاری

```python
# mcp_server/tools/business_intelligence.py
"""
Advanced business intelligence and analytics tools.
"""
from typing import Dict, Any, List
from datetime import datetime, timedelta
from .base import DatabaseTool, ToolResult, ToolCategory

class BusinessIntelligenceTool(DatabaseTool):
    """Advanced analytics tool for business intelligence queries."""
    
    def __init__(self, db_provider):
        super().__init__(
            name="generate_business_insights",
            description="Generate comprehensive business intelligence reports and insights",
            db_provider=db_provider
        )
        self.category = ToolCategory.ANALYTICS
    
    async def execute(self, **kwargs) -> ToolResult:
        """Execute business intelligence analysis."""
        
        analysis_type = kwargs.get('analysis_type', 'summary')
        store_id = kwargs.get('store_id')
        
        if not store_id:
            return ToolResult(
                success=False,
                error="store_id is required for business intelligence analysis"
            )
        
        try:
            if analysis_type == 'summary':
                return await self._generate_business_summary(kwargs)
            elif analysis_type == 'customer_segmentation':
                return await self._analyze_customer_segmentation(kwargs)
            elif analysis_type == 'product_performance':
                return await self._analyze_product_performance(kwargs)
            elif analysis_type == 'seasonal_trends':
                return await self._analyze_seasonal_trends(kwargs)
            else:
                return ToolResult(
                    success=False,
                    error=f"Unknown analysis type: {analysis_type}"
                )
        
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"Business intelligence analysis failed: {str(e)}"
            )
    
    async def _generate_business_summary(self, kwargs: Dict[str, Any]) -> ToolResult:
        """Generate comprehensive business summary."""
        
        store_id = kwargs['store_id']
        days = kwargs.get('days', 30)
        
        summary_query = """
            WITH date_range AS (
                SELECT CURRENT_DATE - INTERVAL '%s days' as start_date,
                       CURRENT_DATE as end_date
            ),
            sales_summary AS (
                SELECT 
                    COUNT(*) as total_transactions,
                    COUNT(DISTINCT customer_id) as unique_customers,
                    SUM(total_amount) as total_revenue,
                    AVG(total_amount) as avg_transaction_value,
                    COUNT(DISTINCT DATE(transaction_date)) as active_days
                FROM retail.sales_transactions st, date_range dr
                WHERE st.transaction_date >= dr.start_date 
                  AND st.transaction_date <= dr.end_date
                  AND st.transaction_type = 'sale'
            ),
            product_summary AS (
                SELECT 
                    COUNT(DISTINCT p.product_id) as products_sold,
                    SUM(sti.quantity) as total_items_sold
                FROM retail.sales_transaction_items sti
                JOIN retail.sales_transactions st ON sti.transaction_id = st.transaction_id
                JOIN retail.products p ON sti.product_id = p.product_id
                CROSS JOIN date_range dr
                WHERE st.transaction_date >= dr.start_date 
                  AND st.transaction_date <= dr.end_date
                  AND st.transaction_type = 'sale'
            ),
            top_category AS (
                SELECT 
                    pc.category_name,
                    SUM(sti.total_price) as category_revenue
                FROM retail.product_categories pc
                JOIN retail.products p ON pc.category_id = p.category_id
                JOIN retail.sales_transaction_items sti ON p.product_id = sti.product_id
                JOIN retail.sales_transactions st ON sti.transaction_id = st.transaction_id
                CROSS JOIN date_range dr
                WHERE st.transaction_date >= dr.start_date 
                  AND st.transaction_date <= dr.end_date
                  AND st.transaction_type = 'sale'
                GROUP BY pc.category_name
                ORDER BY category_revenue DESC
                LIMIT 1
            )
            SELECT 
                ss.*,
                ps.products_sold,
                ps.total_items_sold,
                tc.category_name as top_category,
                tc.category_revenue as top_category_revenue,
                CASE 
                    WHEN ss.active_days > 0 THEN ss.total_revenue / ss.active_days
                    ELSE 0
                END as avg_daily_revenue
            FROM sales_summary ss
            CROSS JOIN product_summary ps
            CROSS JOIN top_category tc
        """ % days
        
        result = await self.execute_query(summary_query, None, store_id)
        
        if result.success and result.data:
            summary = result.data[0]
            
            # Add derived insights
            insights = {
                'revenue_trend': 'stable',  # Would calculate based on historical data
                'customer_retention': f"{summary.get('unique_customers', 0)} active customers",
                'performance_indicators': {
                    'transactions_per_day': round(summary.get('total_transactions', 0) / max(summary.get('active_days', 1), 1), 2),
                    'revenue_per_customer': round(summary.get('total_revenue', 0) / max(summary.get('unique_customers', 1), 1), 2),
                    'items_per_transaction': round(summary.get('total_items_sold', 0) / max(summary.get('total_transactions', 1), 1), 2)
                }
            }
            
            summary['insights'] = insights
            
            result.data = [summary]
            result.metadata = {
                'analysis_type': 'business_summary',
                'period_days': days,
                'store_id': store_id
            }
        
        return result
    
    def get_input_schema(self) -> Dict[str, Any]:
        """Get input schema for business intelligence tool."""
        
        return {
            "type": "object",
            "properties": {
                "analysis_type": {
                    "type": "string",
                    "enum": ["summary", "customer_segmentation", "product_performance", "seasonal_trends"],
                    "description": "Type of business intelligence analysis to perform",
                    "default": "summary"
                },
                "store_id": {
                    "type": "string",
                    "description": "Store ID for analysis",
                    "pattern": "^[a-zA-Z0-9_-]+$"
                },
                "days": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 365,
                    "description": "Number of days to analyze",
                    "default": 30
                }
            },
            "required": ["store_id"],
            "additionalProperties": False
        }

class UtilityTool(DatabaseTool):
    """Utility tool for common operations."""
    
    def __init__(self, db_provider):
        super().__init__(
            name="get_current_utc_date",
            description="Get current UTC date and time for reference",
            db_provider=db_provider
        )
        self.category = ToolCategory.UTILITY
    
    async def execute(self, **kwargs) -> ToolResult:
        """Execute utility operation."""
        
        format_type = kwargs.get('format', 'iso')
        
        try:
            async with self.get_connection() as conn:
                if format_type == 'iso':
                    query = "SELECT CURRENT_TIMESTAMP AT TIME ZONE 'UTC' as current_utc_datetime"
                elif format_type == 'epoch':
                    query = "SELECT EXTRACT(EPOCH FROM CURRENT_TIMESTAMP AT TIME ZONE 'UTC') as current_utc_epoch"
                elif format_type == 'date_only':
                    query = "SELECT CURRENT_DATE as current_date"
                else:
                    return ToolResult(
                        success=False,
                        error=f"Unknown format type: {format_type}"
                    )
                
                result = await conn.fetchrow(query)
                
                return ToolResult(
                    success=True,
                    data=dict(result),
                    metadata={
                        'format_type': format_type,
                        'timezone': 'UTC'
                    }
                )
        
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"Utility operation failed: {str(e)}"
            )
    
    def get_input_schema(self) -> Dict[str, Any]:
        """Get input schema for utility tool."""
        
        return {
            "type": "object",
            "properties": {
                "format": {
                    "type": "string",
                    "enum": ["iso", "epoch", "date_only"],
                    "description": "Format for the returned date/time",
                    "default": "iso"
                }
            },
            "additionalProperties": False
        }
```
  

## 🎯 نکات کلیدی

پس از تکمیل این آزمایش، شما باید:

✅ **معماری پیشرفته ابزار**: ابزارهای پیشرفته MCP با مدیریت جامع خطا پیاده‌سازی کرده باشید  
✅ **اعتبارسنجی پرس‌وجو**: اعتبارسنجی SQL ایمن برای جلوگیری از حملات تزریق ایجاد کرده باشید  
✅ **ابزارهای پایگاه داده**: قابلیت‌های قدرتمند تحلیل فروش و بررسی ساختار ایجاد کرده باشید  
✅ **هوش تجاری**: ابزارهای تحلیلی برای بینش جامع کسب‌وکار توسعه داده باشید  
✅ **بهینه‌سازی عملکرد**: کشینگ، مدیریت اتصال و بهینه‌سازی پرس‌وجو را اعمال کرده باشید  
✅ **یکپارچه‌سازی امنیت**: کنترل دسترسی مبتنی بر نقش و ثبت وقایع (audit logging) پیاده‌سازی کرده باشید  

## 🚀 مرحله بعدی

ادامه دهید با **[آزمایش 07: یکپارچه‌سازی جستجوی معنایی](../07-Semantic-Search/README.md)** برای:

- یکپارچه‌سازی قابلیت‌های جستجوی برداری با ابزارهای MCP  
- ساخت قابلیت جستجوی معنایی محصولات  
- پیاده‌سازی درک پرس‌وجو توسط هوش مصنوعی  
- ایجاد جستجوی ترکیبی که پرس‌وجوهای سنتی و برداری را ترکیب می‌کند  

## 📚 منابع اضافی

### توسعه ابزار MCP  
- [مستندات پروتکل زمینه مدل](https://modelcontextprotocol.io/docs) - مشخصات رسمی MCP  
- [چارچوب FastMCP](https://github.com/jlowin/fastmcp) - پیاده‌سازی MCP با پایتون  
- [الگوهای ابزار MCP](https://github.com/modelcontextprotocol/servers) - پیاده‌سازی نمونه ابزارها  

### امنیت پایگاه داده  
- [پیشگیری از تزریق SQL](https://owasp.org/www-community/attacks/SQL_Injection) - راهنمای امنیت OWASP  
- [امنیت PostgreSQL](https://www.postgresql.org/docs/current/security.html) - بهترین روش‌های امنیت پایگاه داده  
- [تکنیک‌های اعتبارسنجی پرس‌وجو](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html) - الگوهای پرس‌وجوی ایمن  

### بهینه‌سازی عملکرد  
- [بهینه‌سازی پرس‌وجوی پایگاه داده](https://www.postgresql.org/docs/current/performance-tips.html) - راهنمای عملکرد PostgreSQL  
- [بهترین روش‌های مدیریت اتصال](https://www.postgresql.org/docs/current/runtime-config-connection.html) - مدیریت اتصال  
- [الگوهای پایتون غیرهمزمان](https://docs.python.org/3/library/asyncio.html) - راهنمای برنامه‌نویسی غیرهمزمان  

---

**قبلی**: [آزمایش 05: پیاده‌سازی سرور MCP](../05-MCP-Server/README.md)  
**بعدی**: [آزمایش 07: یکپارچه‌سازی جستجوی معنایی](../07-Semantic-Search/README.md)  

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.