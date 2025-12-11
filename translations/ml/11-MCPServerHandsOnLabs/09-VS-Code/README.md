<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "769c9794759f416450dce77286e98f00",
  "translation_date": "2025-12-11T14:15:04+00:00",
  "source_file": "11-MCPServerHandsOnLabs/09-VS-Code/README.md",
  "language_code": "ml"
}
-->
# VS Code ഇന്റഗ്രേഷൻ

## 🎯 ഈ ലാബ് ഉൾക്കൊള്ളുന്നത്

ഈ ലാബ് നിങ്ങളുടെ MCP സെർവറെ VS Code-യുമായി ഇന്റഗ്രേറ്റ് ചെയ്ത് AI ചാറ്റ് വഴി സ്വാഭാവിക ഭാഷാ ക്വെറിയുകൾ സാധ്യമാക്കുന്നതിന് സമഗ്ര മാർഗ്ഗനിർദ്ദേശം നൽകുന്നു. MCP ഉപയോഗത്തിന് അനുയോജ്യമായ രീതിയിൽ VS Code ക്രമീകരിക്കുന്നതും, സെർവർ കണക്ഷനുകൾ ഡീബഗ് ചെയ്യുന്നതും, AI സഹായത്തോടെ ഡാറ്റാബേസ് ഇടപാടുകളുടെ പൂർണ്ണശക്തി പ്രയോജനപ്പെടുത്തുന്നതും നിങ്ങൾക്ക് പഠിക്കാം.

## അവലോകനം

VS Code-യുടെ MCP ഇന്റഗ്രേഷൻ ഡെവലപ്പർമാർ ഡാറ്റാബേസുകളുമായി, API-കളുമായി സ്വാഭാവിക ഭാഷയിലൂടെ ഇടപഴകുന്ന രീതിയിൽ വിപ്ലവം സൃഷ്ടിക്കുന്നു. നിങ്ങളുടെ റീട്ടെയിൽ MCP സെർവറെ VS Code ചാറ്റുമായി ബന്ധിപ്പിച്ച്, conversational AI ഉപയോഗിച്ച് വിൽപ്പന ഡാറ്റ, ഉൽപ്പന്ന കാറ്റലോഗുകൾ, ബിസിനസ് അനലിറ്റിക്സ് എന്നിവയുടെ ബുദ്ധിമുട്ടില്ലാത്ത ക്വെറിയിംഗ് സാധ്യമാക്കുന്നു.

ഈ ഇന്റഗ്രേഷൻ ഡെവലപ്പർമാർക്ക് "ഈ മാസം ഏറ്റവും കൂടുതൽ വിൽപ്പനയുള്ള ഉൽപ്പന്നങ്ങൾ കാണിക്കൂ" അല്ലെങ്കിൽ "90 ദിവസമായി വാങ്ങാത്ത ഉപഭോക്താക്കളെ കണ്ടെത്തൂ" പോലുള്ള ചോദ്യങ്ങൾ ചോദിച്ച് SQL ക്വെറികൾ എഴുതാതെ ഘടനാപരമായ ഡാറ്റാ പ്രതികരണങ്ങൾ ലഭിക്കാനാകും.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ ലാബ് പൂർത്തിയാക്കിയാൽ, നിങ്ങൾക്ക് കഴിയും:

- **കൺഫിഗർ ചെയ്യുക** നിങ്ങളുടെ റീട്ടെയിൽ സെർവറിനായി VS Code MCP ക്രമീകരണങ്ങൾ
- **ഇന്റഗ്രേറ്റ് ചെയ്യുക** MCP സെർവറുകൾ VS Code AI ചാറ്റ് ഫംഗ്ഷണാലിറ്റിയുമായി
- **ഡീബഗ് ചെയ്യുക** MCP സെർവർ കണക്ഷനുകൾ, പ്രശ്നങ്ങൾ പരിഹരിക്കുക
- **ഓപ്റ്റിമൈസ് ചെയ്യുക** സ്വാഭാവിക ഭാഷാ ക്വെറി പാറ്റേണുകൾ മികച്ച ഫലങ്ങൾക്ക്
- **കസ്റ്റമൈസ് ചെയ്യുക** MCP ഡെവലപ്പ്മെന്റിനായി VS Code വർക്ക്സ്പേസ്
- **ഡിപ്ലോയ് ചെയ്യുക** സങ്കീർണ്ണ സാഹചര്യങ്ങൾക്ക് മൾട്ടി-സെർവർ കോൺഫിഗറേഷനുകൾ

## 🔧 VS Code MCP ക്രമീകരണം

### പ്രാഥമിക സെറ്റപ്പ് & ഇൻസ്റ്റലേഷൻ

```json
// .vscode/settings.json
{
    "mcp.servers": {
        "retail-mcp-server": {
            "command": "python",
            "args": [
                "-m", "mcp_server.main"
            ],
            "env": {
                "POSTGRES_HOST": "localhost",
                "POSTGRES_PORT": "5432",
                "POSTGRES_DB": "retail_db",
                "POSTGRES_USER": "mcp_user",
                "POSTGRES_PASSWORD": "${env:POSTGRES_PASSWORD}",
                "PROJECT_ENDPOINT": "${env:PROJECT_ENDPOINT}",
                "AZURE_CLIENT_ID": "${env:AZURE_CLIENT_ID}",
                "AZURE_CLIENT_SECRET": "${env:AZURE_CLIENT_SECRET}",
                "AZURE_TENANT_ID": "${env:AZURE_TENANT_ID}",
                "LOG_LEVEL": "INFO",
                "MCP_SERVER_DEBUG": "false"
            },
            "cwd": "${workspaceFolder}",
            "initializationOptions": {
                "store_id": "seattle",
                "enable_semantic_search": true,
                "enable_analytics": true,
                "cache_embeddings": true
            }
        }
    },
    "mcp.serverTimeout": 30000,
    "mcp.enableLogging": true,
    "mcp.logLevel": "info"
}
```

### പരിസ്ഥിതി ക്രമീകരണം

```bash
# വികസനത്തിനുള്ള .env ഫയൽ
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=retail_db
POSTGRES_USER=mcp_user
POSTGRES_PASSWORD=your_secure_password

# അസ്യൂർ കോൺഫിഗറേഷൻ
PROJECT_ENDPOINT=https://your-project.openai.azure.com
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
AZURE_TENANT_ID=your-tenant-id

# ഐച്ഛികം: അസ്യൂർ കീ വാൾട്ട്
AZURE_KEY_VAULT_URL=https://your-keyvault.vault.azure.net/

# സെർവർ കോൺഫിഗറേഷൻ
MCP_SERVER_PORT=8000
MCP_SERVER_HOST=127.0.0.1
LOG_LEVEL=INFO
```

### വർക്ക്സ്പേസ് ക്രമീകരണം

```json
// .vscode/launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug MCP Server",
            "type": "python",
            "request": "launch",
            "module": "mcp_server.main",
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env",
            "env": {
                "MCP_SERVER_DEBUG": "true",
                "LOG_LEVEL": "DEBUG"
            },
            "args": [],
            "justMyCode": false,
            "stopOnEntry": false
        },
        {
            "name": "Test MCP Server",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env.test",
            "args": [
                "tests/",
                "-v",
                "--tb=short"
            ]
        }
    ]
}
```

### ടാസ്‌ക് ക്രമീകരണം

```json
// .vscode/tasks.json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Start MCP Server",
            "type": "shell",
            "command": "python",
            "args": [
                "-m", "mcp_server.main"
            ],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "new"
            },
            "options": {
                "env": {
                    "PYTHONPATH": "${workspaceFolder}"
                }
            },
            "isBackground": true,
            "problemMatcher": {
                "pattern": {
                    "regexp": "^(.*):(\\d+):(\\d+):\\s+(warning|error):\\s+(.*)$",
                    "file": 1,
                    "line": 2,
                    "column": 3,
                    "severity": 4,
                    "message": 5
                },
                "background": {
                    "activeOnStart": true,
                    "beginsPattern": "^.*Starting MCP server.*$",
                    "endsPattern": "^.*MCP server ready.*$"
                }
            }
        },
        {
            "label": "Run Tests",
            "type": "shell",
            "command": "python",
            "args": [
                "-m", "pytest",
                "tests/",
                "-v"
            ],
            "group": "test",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            }
        },
        {
            "label": "Generate Sample Data",
            "type": "shell",
            "command": "python",
            "args": [
                "scripts/generate_sample_data.py"
            ],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            }
        },
        {
            "label": "Create Database Schema",
            "type": "shell",
            "command": "psql",
            "args": [
                "-h", "${env:POSTGRES_HOST}",
                "-p", "${env:POSTGRES_PORT}",
                "-U", "${env:POSTGRES_USER}",
                "-d", "${env:POSTGRES_DB}",
                "-f", "scripts/create_schema.sql"
            ],
            "group": "build"
        }
    ]
}
```

## 💬 AI ചാറ്റ് ഇന്റഗ്രേഷൻ

### സ്വാഭാവിക ഭാഷാ ക്വെറി പാറ്റേണുകൾ

```typescript
// VS കോഡ് ചാറ്റിനുള്ള ഉദാഹരണ ക്വറി പാറ്റേണുകൾ
interface QueryPattern {
    intent: string;
    examples: string[];
    expectedTools: string[];
}

const retailQueryPatterns: QueryPattern[] = [
    {
        intent: "sales_analysis",
        examples: [
            "Show me daily sales for the last 30 days",
            "What are our top selling products this month?",
            "Which customers have spent the most this quarter?",
            "Compare sales performance between stores"
        ],
        expectedTools: ["execute_sales_query"]
    },
    {
        intent: "product_search",
        examples: [
            "Find running shoes for women",
            "Show me electronics under $500",
            "What laptops do we have in stock?",
            "Search for wireless headphones"
        ],
        expectedTools: ["semantic_search_products", "hybrid_product_search"]
    },
    {
        intent: "inventory_management",
        examples: [
            "Which products are low on stock?",
            "Show me products that need reordering",
            "What's our current inventory value?",
            "Find products with zero stock"
        ],
        expectedTools: ["execute_sales_query"]
    },
    {
        intent: "customer_analysis",
        examples: [
            "Show me customers who haven't purchased in 90 days",
            "What's the average customer lifetime value?",
            "Which customers are in the gold tier?",
            "Find customers with returns"
        ],
        expectedTools: ["execute_sales_query"]
    },
    {
        intent: "business_intelligence",
        examples: [
            "Generate a business summary for this month",
            "Show me seasonal trends",
            "What are our best performing categories?",
            "Create a sales forecast"
        ],
        expectedTools: ["generate_business_insights"]
    },
    {
        intent: "recommendations",
        examples: [
            "Recommend products similar to product X",
            "What should we recommend to customer Y?",
            "Show me trending products",
            "Find cross-sell opportunities"
        ],
        expectedTools: ["get_product_recommendations"]
    }
];
```

### ചാറ്റ് ഇന്റഗ്രേഷൻ ഉദാഹരണങ്ങൾ

```markdown
<!-- Examples of VS Code Chat interactions -->

## Sales Analysis Queries

**User**: Show me the top 10 selling products in the Seattle store for the last month

**Expected Response**: 
- Tool: execute_sales_query
- Parameters: query_type="top_products", store_id="seattle", start_date="2025-08-29", end_date="2025-09-29", limit=10
- Result: Formatted table with product names, quantities sold, revenue, and performance metrics

**User**: What was our daily revenue trend last week?

**Expected Response**:
- Tool: execute_sales_query  
- Parameters: query_type="daily_sales", store_id="seattle", start_date="2025-09-22", end_date="2025-09-29"
- Result: Chart-ready data with daily revenue figures and growth percentages

## Product Search Queries

**User**: Find comfortable running shoes for outdoor activities

**Expected Response**:
- Tool: semantic_search_products
- Parameters: query="comfortable running shoes outdoor activities", store_id="seattle", similarity_threshold=0.7
- Result: Ranked list of relevant products with similarity scores and detailed information

**User**: Search for laptops under $1500 with good reviews

**Expected Response**:
- Tool: hybrid_product_search
- Parameters: query="laptops under $1500 good reviews", store_id="seattle", semantic_weight=0.6, keyword_weight=0.4
- Result: Combined keyword and semantic search results with price and rating filters

## Business Intelligence Queries

**User**: Generate a comprehensive business summary for September

**Expected Response**:
- Tool: generate_business_insights
- Parameters: analysis_type="summary", store_id="seattle", days=30
- Result: KPI dashboard with revenue, customer metrics, top categories, and growth trends
```

### ചാറ്റ് പ്രതികരണ ഫോർമാറ്റിംഗ്

```python
# mcp_server/chat/response_formatter.py
"""
Format MCP tool responses for optimal VS Code Chat display.
"""
from typing import Dict, Any, List
import json
from datetime import datetime

class ChatResponseFormatter:
    """Format tool responses for VS Code Chat consumption."""
    
    @staticmethod
    def format_sales_data(data: List[Dict[str, Any]], query_type: str) -> str:
        """Format sales data for chat display."""
        
        if not data:
            return "No sales data found for the specified criteria."
        
        if query_type == "daily_sales":
            return ChatResponseFormatter._format_daily_sales(data)
        elif query_type == "top_products":
            return ChatResponseFormatter._format_top_products(data)
        elif query_type == "customer_analysis":
            return ChatResponseFormatter._format_customer_analysis(data)
        else:
            return ChatResponseFormatter._format_generic_table(data)
    
    @staticmethod
    def _format_daily_sales(data: List[Dict[str, Any]]) -> str:
        """Format daily sales data."""
        
        response = "## Daily Sales Summary\n\n"
        response += "| Date | Revenue | Transactions | Avg Order Value | Customers |\n"
        response += "|------|---------|-------------|----------------|----------|\n"
        
        total_revenue = 0
        total_transactions = 0
        
        for day in data:
            revenue = float(day.get('total_revenue', 0))
            transactions = int(day.get('transaction_count', 0))
            avg_value = float(day.get('avg_transaction_value', 0))
            customers = int(day.get('unique_customers', 0))
            
            total_revenue += revenue
            total_transactions += transactions
            
            response += f"| {day.get('sales_date', 'N/A')} | "
            response += f"${revenue:,.2f} | "
            response += f"{transactions:,} | "
            response += f"${avg_value:.2f} | "
            response += f"{customers:,} |\n"
        
        response += f"\n**Totals**: ${total_revenue:,.2f} revenue, {total_transactions:,} transactions"
        
        return response
    
    @staticmethod
    def _format_top_products(data: List[Dict[str, Any]]) -> str:
        """Format top products data."""
        
        response = "## Top Selling Products\n\n"
        response += "| Rank | Product | Brand | Revenue | Qty Sold | Avg Price |\n"
        response += "|------|---------|-------|---------|----------|----------|\n"
        
        for i, product in enumerate(data, 1):
            response += f"| {i} | "
            response += f"{product.get('product_name', 'N/A')} | "
            response += f"{product.get('brand', 'N/A')} | "
            response += f"${float(product.get('total_revenue', 0)):,.2f} | "
            response += f"{int(product.get('total_quantity_sold', 0)):,} | "
            response += f"${float(product.get('avg_price', 0)):.2f} |\n"
        
        return response
    
    @staticmethod
    def format_search_results(data: List[Dict[str, Any]], search_type: str) -> str:
        """Format product search results."""
        
        if not data:
            return "No products found matching your search criteria."
        
        response = f"## Product Search Results ({search_type})\n\n"
        
        for i, product in enumerate(data, 1):
            response += f"### {i}. {product.get('product_name', 'Unknown Product')}\n"
            response += f"**Brand**: {product.get('brand', 'N/A')}\n"
            response += f"**Price**: ${float(product.get('price', 0)):.2f}\n"
            response += f"**Stock**: {int(product.get('current_stock', 0))} units\n"
            
            if 'similarity_score' in product:
                score = float(product['similarity_score'])
                response += f"**Relevance**: {score:.1%}\n"
            
            if 'rating_average' in product and product['rating_average']:
                rating = float(product['rating_average'])
                count = int(product.get('rating_count', 0))
                response += f"**Rating**: {rating:.1f}/5.0 ({count:,} reviews)\n"
            
            if product.get('product_description'):
                desc = product['product_description']
                if len(desc) > 150:
                    desc = desc[:150] + "..."
                response += f"**Description**: {desc}\n"
            
            response += "\n---\n\n"
        
        return response
    
    @staticmethod
    def format_business_insights(data: Dict[str, Any]) -> str:
        """Format business intelligence data."""
        
        response = "## Business Intelligence Summary\n\n"
        
        # പ്രധാന മാനദണ്ഡങ്ങൾ
        response += "### Key Performance Indicators\n\n"
        response += f"- **Total Revenue**: ${float(data.get('total_revenue', 0)):,.2f}\n"
        response += f"- **Total Transactions**: {int(data.get('total_transactions', 0)):,}\n"
        response += f"- **Unique Customers**: {int(data.get('unique_customers', 0)):,}\n"
        response += f"- **Average Order Value**: ${float(data.get('avg_transaction_value', 0)):.2f}\n"
        response += f"- **Products Sold**: {int(data.get('products_sold', 0)):,} items\n\n"
        
        # പ്രകടന സൂചകങ്ങൾ
        if 'insights' in data and 'performance_indicators' in data['insights']:
            pi = data['insights']['performance_indicators']
            response += "### Performance Indicators\n\n"
            response += f"- **Transactions per Day**: {float(pi.get('transactions_per_day', 0)):.1f}\n"
            response += f"- **Revenue per Customer**: ${float(pi.get('revenue_per_customer', 0)):,.2f}\n"
            response += f"- **Items per Transaction**: {float(pi.get('items_per_transaction', 0)):.1f}\n\n"
        
        # മുകളിൽ വരുന്ന വിഭാഗം
        if data.get('top_category'):
            response += f"### Top Performing Category\n\n"
            response += f"**{data['top_category']}** - ${float(data.get('top_category_revenue', 0)):,.2f} revenue\n\n"
        
        return response
    
    @staticmethod
    def format_error_response(error: str, tool_name: str) -> str:
        """Format error responses for chat."""
        
        response = f"## ❌ Error in {tool_name}\n\n"
        response += f"I encountered an issue while processing your request:\n\n"
        response += f"**Error**: {error}\n\n"
        response += "Please try:\n"
        response += "- Checking your query parameters\n"
        response += "- Verifying store access permissions\n"
        response += "- Simplifying your request\n"
        response += "- Contacting support if the issue persists\n"
        
        return response
```

## 🔍 ഡീബഗ്ഗിംഗ് & പ്രശ്നപരിഹാരം

### VS Code ഡീബഗ് ക്രമീകരണം

```python
# mcp_server/debug/vscode_debug.py
"""
VS Code specific debugging utilities for MCP server.
"""
import logging
import json
from typing import Dict, Any
from datetime import datetime

class VSCodeDebugLogger:
    """Enhanced logging for VS Code debugging."""
    
    def __init__(self):
        self.logger = logging.getLogger("mcp_vscode_debug")
        self.setup_vscode_logging()
    
    def setup_vscode_logging(self):
        """Configure logging for VS Code debugging."""
        
        # VS കോഡ് പ്രത്യേക ഫോർമാറ്റർ സൃഷ്ടിക്കുക
        formatter = logging.Formatter(
            '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'
        )
        
        # VS കോഡ് ടെർമിനലിനുള്ള കൺസോൾ ഹാൻഡ്ലർ
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.DEBUG)
        
        self.logger.addHandler(console_handler)
        self.logger.setLevel(logging.DEBUG)
    
    def log_mcp_request(self, method: str, params: Dict[str, Any]):
        """Log MCP requests for debugging."""
        
        self.logger.info(f"MCP Request: {method}")
        self.logger.debug(f"Parameters: {json.dumps(params, indent=2)}")
    
    def log_tool_execution(self, tool_name: str, result: Dict[str, Any]):
        """Log tool execution results."""
        
        success = result.get('success', False)
        level = logging.INFO if success else logging.ERROR
        
        self.logger.log(level, f"Tool '{tool_name}' - {'Success' if success else 'Failed'}")
        
        if not success and result.get('error'):
            self.logger.error(f"Error: {result['error']}")
        
        if result.get('data'):
            data_summary = self._summarize_data(result['data'])
            self.logger.debug(f"Result summary: {data_summary}")
    
    def _summarize_data(self, data: Any) -> str:
        """Create a summary of result data."""
        
        if isinstance(data, list):
            return f"List with {len(data)} items"
        elif isinstance(data, dict):
            return f"Dict with keys: {list(data.keys())}"
        else:
            return f"Data type: {type(data).__name__}"

# ആഗോള ഡീബഗ് ലോഗർ
vscode_debug_logger = VSCodeDebugLogger()
```

### കണക്ഷൻ പ്രശ്നപരിഹാരം

```python
# scripts/debug_mcp_connection.py
"""
Debug script for troubleshooting MCP server connections in VS Code.
"""
import asyncio
import asyncpg
import os
import sys
from typing import Dict, Any

async def test_database_connection() -> Dict[str, Any]:
    """Test database connectivity."""
    
    try:
        # പരിസ്ഥിതിയിൽ നിന്ന് കണക്ഷൻ പാരാമീറ്ററുകൾ നേടുക
        connection_params = {
            'host': os.getenv('POSTGRES_HOST', 'localhost'),
            'port': int(os.getenv('POSTGRES_PORT', '5432')),
            'database': os.getenv('POSTGRES_DB', 'retail_db'),
            'user': os.getenv('POSTGRES_USER', 'mcp_user'),
            'password': os.getenv('POSTGRES_PASSWORD', '')
        }
        
        print(f"Testing connection to {connection_params['host']}:{connection_params['port']}")
        
        # കണക്ഷൻ പരിശോധിക്കുക
        conn = await asyncpg.connect(**connection_params)
        
        # അടിസ്ഥാന ക്വറി പരിശോധിക്കുക
        result = await conn.fetchval("SELECT version()")
        
        # സ്കീമ ആക്‌സസ് പരിശോധിക്കുക
        tables = await conn.fetch("""
            SELECT table_name FROM information_schema.tables 
            WHERE table_schema = 'retail'
        """)
        
        await conn.close()
        
        return {
            'success': True,
            'database_version': result,
            'retail_tables': len(tables),
            'table_names': [table['table_name'] for table in tables]
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'connection_params': {k: v for k, v in connection_params.items() if k != 'password'}
        }

async def test_azure_openai_connection() -> Dict[str, Any]:
    """Test Azure OpenAI connectivity."""
    
    try:
        from azure.identity import DefaultAzureCredential
        from azure.ai.projects import AIProjectClient
        
        project_endpoint = os.getenv('PROJECT_ENDPOINT')
        if not project_endpoint:
            return {
                'success': False,
                'error': 'PROJECT_ENDPOINT not configured'
            }
        
        print(f"Testing Azure OpenAI connection to {project_endpoint}")
        
        credential = DefaultAzureCredential()
        client = AIProjectClient(
            endpoint=project_endpoint,
            credential=credential
        )
        
        # എംബെഡിംഗ് ജനറേഷൻ പരിശോധിക്കുക
        response = await client.embeddings.create(
            model="text-embedding-3-small",
            input="test connection"
        )
        
        embedding = response.data[0].embedding
        
        return {
            'success': True,
            'project_endpoint': project_endpoint,
            'embedding_dimension': len(embedding),
            'model': 'text-embedding-3-small'
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'project_endpoint': os.getenv('PROJECT_ENDPOINT', 'Not configured')
        }

async def test_mcp_tools() -> Dict[str, Any]:
    """Test MCP tool availability."""
    
    try:
        # MCP സെർവർ ഘടകങ്ങൾ ഇറക്കുമതി ചെയ്യുക
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))
        
        from mcp_server.server import MCPServer
        from mcp_server.database import DatabaseProvider
        from mcp_server.config import Config
        
        # ടെസ്റ്റ് കോൺഫിഗറേഷൻ സൃഷ്ടിക്കുക
        config = Config()
        db_provider = DatabaseProvider(config.database.connection_string)
        
        # സെർവർ ആരംഭിക്കുക
        server = MCPServer(config, db_provider)
        await server.initialize()
        
        # ലഭ്യമായ ഉപകരണങ്ങൾ നേടുക
        tools = server.get_available_tools()
        
        # ഒരു ലളിതമായ ഉപകരണം പരിശോധിക്കുക
        test_result = await server.execute_tool(
            'get_current_utc_date',
            {'format': 'iso'}
        )
        
        await server.cleanup()
        
        return {
            'success': True,
            'available_tools': [tool.name for tool in tools],
            'tool_count': len(tools),
            'test_tool_result': test_result.get('success', False)
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

async def main():
    """Run comprehensive connection tests."""
    
    print("🔍 MCP Server Connection Diagnostics")
    print("=" * 50)
    
    # ഡാറ്റാബേസ് കണക്ഷൻ പരിശോധിക്കുക
    print("\n📊 Testing Database Connection...")
    db_result = await test_database_connection()
    
    if db_result['success']:
        print("✅ Database connection successful")
        print(f"   Database version: {db_result['database_version']}")
        print(f"   Retail tables found: {db_result['retail_tables']}")
        print(f"   Table names: {', '.join(db_result['table_names'])}")
    else:
        print("❌ Database connection failed")
        print(f"   Error: {db_result['error']}")
    
    # ആസ്യൂർ ഓപ്പൺഎഐ കണക്ഷൻ പരിശോധിക്കുക
    print("\n🤖 Testing Azure OpenAI Connection...")
    azure_result = await test_azure_openai_connection()
    
    if azure_result['success']:
        print("✅ Azure OpenAI connection successful")
        print(f"   Endpoint: {azure_result['project_endpoint']}")
        print(f"   Embedding dimension: {azure_result['embedding_dimension']}")
    else:
        print("❌ Azure OpenAI connection failed")
        print(f"   Error: {azure_result['error']}")
    
    # MCP ഉപകരണങ്ങൾ പരിശോധിക്കുക
    print("\n🛠️  Testing MCP Tools...")
    tools_result = await test_mcp_tools()
    
    if tools_result['success']:
        print("✅ MCP tools loaded successfully")
        print(f"   Available tools: {tools_result['tool_count']}")
        print(f"   Tool names: {', '.join(tools_result['available_tools'])}")
        print(f"   Test execution: {'✅' if tools_result['test_tool_result'] else '❌'}")
    else:
        print("❌ MCP tools loading failed")
        print(f"   Error: {tools_result['error']}")
    
    # മൊത്തം നില
    print("\n📋 Overall Status")
    print("=" * 50)
    
    all_success = all([
        db_result['success'],
        azure_result['success'],
        tools_result['success']
    ])
    
    if all_success:
        print("🎉 All systems ready! MCP server should work correctly in VS Code.")
    else:
        print("⚠️  Some issues detected. Please resolve the errors above.")
        print("\n💡 Troubleshooting tips:")
        print("   - Check environment variables in .env file")
        print("   - Verify database is running and accessible")
        print("   - Confirm Azure credentials are configured")
        print("   - Review VS Code MCP server configuration")

if __name__ == "__main__":
    asyncio.run(main())
```

## 🚀 ആഡ്വാൻസ്ഡ് ക്രമീകരണം

### മൾട്ടി-സെർവർ സെറ്റപ്പ്

```json
// .vscode/settings.json - Multiple MCP servers
{
    "mcp.servers": {
        "retail-seattle": {
            "command": "python",
            "args": ["-m", "mcp_server.main"],
            "env": {
                "POSTGRES_HOST": "localhost",
                "POSTGRES_DB": "retail_db",
                "POSTGRES_USER": "mcp_user",
                "POSTGRES_PASSWORD": "${env:POSTGRES_PASSWORD}",
                "PROJECT_ENDPOINT": "${env:PROJECT_ENDPOINT}",
                "DEFAULT_STORE_ID": "seattle"
            },
            "initializationOptions": {
                "store_id": "seattle",
                "server_name": "Seattle Store"
            }
        },
        "retail-redmond": {
            "command": "python",
            "args": ["-m", "mcp_server.main"],
            "env": {
                "POSTGRES_HOST": "localhost",
                "POSTGRES_DB": "retail_db",
                "POSTGRES_USER": "mcp_user",
                "POSTGRES_PASSWORD": "${env:POSTGRES_PASSWORD}",
                "PROJECT_ENDPOINT": "${env:PROJECT_ENDPOINT}",
                "DEFAULT_STORE_ID": "redmond"
            },
            "initializationOptions": {
                "store_id": "redmond",
                "server_name": "Redmond Store"
            }
        },
        "retail-analytics": {
            "command": "python",
            "args": ["-m", "mcp_server.analytics_main"],
            "env": {
                "POSTGRES_HOST": "localhost",
                "POSTGRES_DB": "retail_db",
                "POSTGRES_USER": "analytics_user",
                "POSTGRES_PASSWORD": "${env:ANALYTICS_PASSWORD}",
                "PROJECT_ENDPOINT": "${env:PROJECT_ENDPOINT}"
            },
            "initializationOptions": {
                "mode": "analytics",
                "cross_store_access": true
            }
        }
    }
}
```

### കസ്റ്റം VS Code എക്സ്റ്റൻഷൻ

```typescript
// src/extension.ts - കസ്റ്റം MCP റീട്ടെയിൽ എക്സ്റ്റൻഷൻ
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    
    // MCP റീട്ടെയിൽ കമാൻഡുകൾ രജിസ്റ്റർ ചെയ്യുക
    const disposable = vscode.commands.registerCommand(
        'mcp-retail.quickQuery', 
        async () => {
            const quickPick = vscode.window.createQuickPick();
            quickPick.items = [
                {
                    label: '📊 Daily Sales',
                    description: 'Show daily sales for the last 30 days'
                },
                {
                    label: '🏆 Top Products',
                    description: 'Show top selling products this month'
                },
                {
                    label: '👥 Customer Analysis',
                    description: 'Analyze customer behavior and trends'
                },
                {
                    label: '🔍 Product Search',
                    description: 'Search for products using natural language'
                },
                {
                    label: '📈 Business Insights',
                    description: 'Generate comprehensive business summary'
                }
            ];
            
            quickPick.onDidChangeSelection(selection => {
                if (selection[0]) {
                    executeQuickQuery(selection[0].label);
                }
            });
            
            quickPick.onDidHide(() => quickPick.dispose());
            quickPick.show();
        }
    );
    
    context.subscriptions.push(disposable);
    
    // സ്റ്റോർ സ്വിച്ച് രജിസ്റ്റർ ചെയ്യുക
    const storeSwitcher = vscode.commands.registerCommand(
        'mcp-retail.switchStore',
        async () => {
            const stores = ['seattle', 'redmond', 'bellevue', 'online'];
            const selected = await vscode.window.showQuickPick(stores, {
                placeHolder: 'Select store for queries'
            });
            
            if (selected) {
                // കോൺഫിഗറേഷൻ അപ്ഡേറ്റ് ചെയ്യുക
                const config = vscode.workspace.getConfiguration('mcp');
                await config.update('defaultStore', selected, true);
                
                vscode.window.showInformationMessage(
                    `Switched to ${selected.charAt(0).toUpperCase() + selected.slice(1)} store`
                );
            }
        }
    );
    
    context.subscriptions.push(storeSwitcher);
}

async function executeQuickQuery(queryType: string) {
    // VS കോഡ് ചാറ്റിൽ മുൻകൂട്ടി നിർവചിച്ച ക്വെറികൾ പ്രവർത്തിപ്പിക്കുക
    const chatCommands = {
        '📊 Daily Sales': '@retail Show me daily sales for the last 30 days',
        '🏆 Top Products': '@retail What are the top 10 selling products this month?',
        '👥 Customer Analysis': '@retail Show me customer analysis for active customers',
        '🔍 Product Search': '@retail Find products matching "laptop computer"',
        '📈 Business Insights': '@retail Generate a business summary for this month'
    };
    
    const command = chatCommands[queryType];
    if (command) {
        await vscode.commands.executeCommand('workbench.action.chat.open');
        await vscode.commands.executeCommand('workbench.action.chat.insert', command);
    }
}

export function deactivate() {}
```

### എക്സ്റ്റൻഷൻ പാക്കേജ് ക്രമീകരണം

```json
// package.json for VS Code extension
{
    "name": "mcp-retail-assistant",
    "displayName": "MCP Retail Assistant",
    "description": "AI-powered retail data analysis through MCP",
    "version": "1.0.0",
    "engines": {
        "vscode": "^1.74.0"
    },
    "categories": [
        "Other",
        "Data Science",
        "Machine Learning"
    ],
    "activationEvents": [
        "onCommand:mcp-retail.quickQuery",
        "onCommand:mcp-retail.switchStore"
    ],
    "main": "./out/extension.js",
    "contributes": {
        "commands": [
            {
                "command": "mcp-retail.quickQuery",
                "title": "Quick Retail Query",
                "category": "MCP Retail"
            },
            {
                "command": "mcp-retail.switchStore",
                "title": "Switch Store",
                "category": "MCP Retail"
            }
        ],
        "keybindings": [
            {
                "command": "mcp-retail.quickQuery",
                "key": "ctrl+shift+r",
                "mac": "cmd+shift+r"
            }
        ],
        "configuration": {
            "title": "MCP Retail",
            "properties": {
                "mcp-retail.defaultStore": {
                    "type": "string",
                    "default": "seattle",
                    "enum": ["seattle", "redmond", "bellevue", "online"],
                    "description": "Default store for retail queries"
                },
                "mcp-retail.enableAnalytics": {
                    "type": "boolean",
                    "default": true,
                    "description": "Enable advanced analytics features"
                }
            }
        }
    },
    "scripts": {
        "vscode:prepublish": "npm run compile",
        "compile": "tsc -p ./",
        "watch": "tsc -watch -p ./"
    },
    "devDependencies": {
        "@types/vscode": "^1.74.0",
        "@types/node": "16.x",
        "typescript": "^4.9.4"
    }
}
```

## 🎯 പ്രധാന പഠനങ്ങൾ

ഈ ലാബ് പൂർത്തിയാക്കിയ ശേഷം, നിങ്ങൾക്ക് ഉണ്ടാകണം:

✅ **VS Code MCP ക്രമീകരണം**: MCP ഇന്റഗ്രേഷനിനായി പൂർണ്ണ സെറ്റപ്പ്  
✅ **AI ചാറ്റ് ഇന്റഗ്രേഷൻ**: VS Code-യിൽ സ്വാഭാവിക ഭാഷാ ക്വെറിയിംഗ് കഴിവുകൾ  
✅ **ഡീബഗ്ഗിംഗ് ടൂളുകൾ**: സമഗ്രമായ പ്രശ്നപരിഹാരവും കണക്ഷൻ ഡയഗ്നോസ്റ്റിക്സും  
✅ **മൾട്ടി-സെർവർ സെറ്റപ്പ്**: നിരവധി MCP സെർവർ ഇൻസ്റ്റൻസുകൾക്കുള്ള ക്രമീകരണം  
✅ **കസ്റ്റം എക്സ്റ്റൻഷനുകൾ**: റീട്ടെയിൽ-സ്പെസിഫിക് ഫീച്ചറുകളോടെ മെച്ചപ്പെട്ട VS Code അനുഭവം  
✅ **പ്രൊഡക്ഷൻ റെഡിനസ്**: എന്റർപ്രൈസ്-തയ്യാറായ VS Code ഡെവലപ്പ്മെന്റ് പരിസ്ഥിതി  

## 🚀 അടുത്തത് എന്താണ്

**[Lab 10: Deployment Strategies](../10-Deployment/README.md)**-നൊപ്പം തുടരണം:

- MCP സെർവറുകൾ പ്രൊഡക്ഷൻ പരിസ്ഥിതികളിലേക്ക് ഡിപ്ലോയ് ചെയ്യുക  
- സ്കെയിലബിലിറ്റിക്ക് ക്ലൗഡ് ഇൻഫ്രാസ്ട്രക്ചർ ക്രമീകരിക്കുക  
- ഓട്ടോമേറ്റഡ് ഡിപ്ലോയ്മെന്റിനായി CI/CD പൈപ്പ്ലൈനുകൾ നടപ്പിലാക്കുക  
- പ്രൊഡക്ഷൻ MCP സെർവർ പ്രകടനം നിരീക്ഷിക്കുക  

## 📚 അധിക സ്രോതസുകൾ

### VS Code ഡെവലപ്പ്മെന്റ്
- [VS Code Extension API](https://code.visualstudio.com/api) - ഔദ്യോഗിക എക്സ്റ്റൻഷൻ ഡെവലപ്പ്മെന്റ് ഗൈഡ്  
- [VS Code MCP Documentation](https://code.visualstudio.com/docs/copilot/copilot-extensibility-overview) - MCP ഇന്റഗ്രേഷൻ ഡോക്യുമെന്റേഷൻ  
- [TypeScript for VS Code](https://code.visualstudio.com/docs/languages/typescript) - VS Code-യിൽ TypeScript ഡെവലപ്പ്മെന്റ്  

### MCP പ്രോട്ടോക്കോൾ
- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification) - ഔദ്യോഗിക MCP സ്പെസിഫിക്കേഷൻ  
- [MCP Best Practices](https://modelcontextprotocol.io/docs/best-practices) - നടപ്പാക്കൽ മികച്ച രീതികൾ  
- [FastMCP Framework](https://github.com/jlowin/fastmcp) - Python MCP നടപ്പാക്കൽ  

### ഡെവലപ്പ്മെന്റ് ടൂളുകൾ
- [Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial) - Python ഡെവലപ്പ്മെന്റ് സെറ്റപ്പ്  
- [Debugging in VS Code](https://code.visualstudio.com/docs/editor/debugging) - ആഡ്വാൻസ്ഡ് ഡീബഗ്ഗിംഗ് സാങ്കേതികവിദ്യകൾ  
- [VS Code Tasks](https://code.visualstudio.com/docs/editor/tasks) - ടാസ്‌ക് ഓട്ടോമേഷൻ & ക്രമീകരണം  

---

**മുൻപ്**: [Lab 08: Testing and Debugging](../08-Testing/README.md)  
**അടുത്തത്**: [Lab 10: Deployment Strategies](../10-Deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->