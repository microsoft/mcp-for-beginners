# VS Code ఇంటిగ్రేషన్

## 🎯 ఈ ల్యాబ్ కవర్ చేసే అంశాలు

ఈ ల్యాబ్ మీ MCP సర్వర్‌ను VS Code తో ఇంటిగ్రేట్ చేయడం గురించి సమగ్ర మార్గదర్శకాన్ని అందిస్తుంది, తద్వారా AI చాట్ ద్వారా సహజ భాషా ప్రశ్నలను సులభంగా అడగవచ్చు. మీరు MCP ఉపయోగానికి అనుకూలంగా VS Code ను కాన్ఫిగర్ చేయడం, సర్వర్ కనెక్షన్లను డీబగ్ చేయడం, మరియు AI సహాయంతో డేటాబేస్ ఇంటరాక్షన్ల పూర్తి శక్తిని వినియోగించడం నేర్చుకుంటారు.

## అవలోకనం

VS Code యొక్క MCP ఇంటిగ్రేషన్ డెవలపర్లకు సహజ భాష ద్వారా డేటాబేస్‌లు మరియు APIలతో ఎలా ఇంటరాక్ట్ చేయాలో మార్చేస్తుంది. మీ రిటైల్ MCP సర్వర్‌ను VS Code చాట్‌కు కనెక్ట్ చేయడం ద్వారా, మీరు సేల్స్ డేటా, ఉత్పత్తి క్యాటలాగ్లు, మరియు వ్యాపార విశ్లేషణలను సంభాషణాత్మక AI ఉపయోగించి తెలివిగా ప్రశ్నించవచ్చు.

ఈ ఇంటిగ్రేషన్ డెవలపర్లకు "ఈ నెలలో టాప్ సేలింగ్ ఉత్పత్తులు చూపించు" లేదా "90 రోజులుగా కొనుగోలు చేయని కస్టమర్లను కనుగొను" వంటి ప్రశ్నలు అడగడానికి మరియు SQL ప్రశ్నలు రాయకుండా నిర్మిత డేటా ప్రతిస్పందనలు పొందడానికి అనుమతిస్తుంది.

## నేర్చుకునే లక్ష్యాలు

ఈ ల్యాబ్ ముగిసిన తర్వాత, మీరు చేయగలుగుతారు:

- **కాన్ఫిగర్ చేయడం** మీ రిటైల్ సర్వర్ కోసం VS Code MCP సెట్టింగ్స్  
- **ఇంటిగ్రేట్ చేయడం** MCP సర్వర్లను VS Code AI చాట్ ఫంక్షనాలిటీతో  
- **డీబగ్ చేయడం** MCP సర్వర్ కనెక్షన్లను మరియు సమస్యలను పరిష్కరించడం  
- **ఆప్టిమైజ్ చేయడం** సహజ భాషా ప్రశ్న నమూనాలను మెరుగైన ఫలితాల కోసం  
- **కస్టమైజ్ చేయడం** MCP డెవలప్‌మెంట్ కోసం VS Code వర్క్‌స్పేస్  
- **డిప్లాయ్ చేయడం** సంక్లిష్ట పరిస్థితుల కోసం బహుళ సర్వర్ కాన్ఫిగరేషన్లు  

## 🔧 VS Code MCP కాన్ఫిగరేషన్

### ప్రారంభ సెటప్ మరియు ఇన్‌స్టాలేషన్

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

### పరిసరాల కాన్ఫిగరేషన్

```bash
# అభివృద్ధి కోసం .env ఫైల్
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=retail_db
POSTGRES_USER=mcp_user
POSTGRES_PASSWORD=your_secure_password

# అజ్యూర్ కాన్ఫిగరేషన్
PROJECT_ENDPOINT=https://your-project.openai.azure.com
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
AZURE_TENANT_ID=your-tenant-id

# ఐచ్ఛికం: అజ్యూర్ కీ వాల్ట్
AZURE_KEY_VAULT_URL=https://your-keyvault.vault.azure.net/

# సర్వర్ కాన్ఫిగరేషన్
MCP_SERVER_PORT=8000
MCP_SERVER_HOST=127.0.0.1
LOG_LEVEL=INFO
```

### వర్క్‌స్పేస్ కాన్ఫిగరేషన్

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

### టాస్క్ కాన్ఫిగరేషన్

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

## 💬 AI చాట్ ఇంటిగ్రేషన్

### సహజ భాషా ప్రశ్న నమూనాలు

```typescript
// VS కోడ్ చాట్ కోసం ఉదాహరణ ప్రశ్న నమూనాలు
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

### చాట్ ఇంటిగ్రేషన్ ఉదాహరణలు

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

### చాట్ ప్రతిస్పందన ఫార్మాటింగ్

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
        
        # ముఖ్యమైన ప్రమాణాలు
        response += "### Key Performance Indicators\n\n"
        response += f"- **Total Revenue**: ${float(data.get('total_revenue', 0)):,.2f}\n"
        response += f"- **Total Transactions**: {int(data.get('total_transactions', 0)):,}\n"
        response += f"- **Unique Customers**: {int(data.get('unique_customers', 0)):,}\n"
        response += f"- **Average Order Value**: ${float(data.get('avg_transaction_value', 0)):.2f}\n"
        response += f"- **Products Sold**: {int(data.get('products_sold', 0)):,} items\n\n"
        
        # పనితీరు సూచికలు
        if 'insights' in data and 'performance_indicators' in data['insights']:
            pi = data['insights']['performance_indicators']
            response += "### Performance Indicators\n\n"
            response += f"- **Transactions per Day**: {float(pi.get('transactions_per_day', 0)):.1f}\n"
            response += f"- **Revenue per Customer**: ${float(pi.get('revenue_per_customer', 0)):,.2f}\n"
            response += f"- **Items per Transaction**: {float(pi.get('items_per_transaction', 0)):.1f}\n\n"
        
        # టాప్ వర్గం
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

## 🔍 డీబగింగ్ మరియు సమస్య పరిష్కారం

### VS Code డీబగ్ కాన్ఫిగరేషన్

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
        
        # VS కోడ్ ప్రత్యేక ఫార్మాటర్ సృష్టించండి
        formatter = logging.Formatter(
            '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'
        )
        
        # VS కోడ్ టెర్మినల్ కోసం కన్సోల్ హ్యాండ్లర్
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

# గ్లోబల్ డీబగ్ లాగర్
vscode_debug_logger = VSCodeDebugLogger()
```

### కనెక్షన్ సమస్య పరిష్కారం

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
        # పరిసరాల నుండి కనెక్షన్ పరామితులను పొందండి
        connection_params = {
            'host': os.getenv('POSTGRES_HOST', 'localhost'),
            'port': int(os.getenv('POSTGRES_PORT', '5432')),
            'database': os.getenv('POSTGRES_DB', 'retail_db'),
            'user': os.getenv('POSTGRES_USER', 'mcp_user'),
            'password': os.getenv('POSTGRES_PASSWORD', '')
        }
        
        print(f"Testing connection to {connection_params['host']}:{connection_params['port']}")
        
        # కనెక్షన్‌ను పరీక్షించండి
        conn = await asyncpg.connect(**connection_params)
        
        # ప్రాథమిక క్వెరీని పరీక్షించండి
        result = await conn.fetchval("SELECT version()")
        
        # స్కీమా యాక్సెస్‌ను పరీక్షించండి
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
        
        # ఎంబెడ్డింగ్ ఉత్పత్తిని పరీక్షించండి
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
        # MCP సర్వర్ భాగాలను దిగుమతి చేసుకోండి
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))
        
        from mcp_server.server import MCPServer
        from mcp_server.database import DatabaseProvider
        from mcp_server.config import Config
        
        # పరీక్షా కాన్ఫిగరేషన్ సృష్టించండి
        config = Config()
        db_provider = DatabaseProvider(config.database.connection_string)
        
        # సర్వర్‌ను ప్రారంభించండి
        server = MCPServer(config, db_provider)
        await server.initialize()
        
        # అందుబాటులో ఉన్న టూల్స్‌ను పొందండి
        tools = server.get_available_tools()
        
        # ఒక సాదా టూల్‌ను పరీక్షించండి
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
    
    # డేటాబేస్ కనెక్షన్‌ను పరీక్షించండి
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
    
    # Azure OpenAI కనెక్షన్‌ను పరీక్షించండి
    print("\n🤖 Testing Azure OpenAI Connection...")
    azure_result = await test_azure_openai_connection()
    
    if azure_result['success']:
        print("✅ Azure OpenAI connection successful")
        print(f"   Endpoint: {azure_result['project_endpoint']}")
        print(f"   Embedding dimension: {azure_result['embedding_dimension']}")
    else:
        print("❌ Azure OpenAI connection failed")
        print(f"   Error: {azure_result['error']}")
    
    # MCP టూల్స్‌ను పరీక్షించండి
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
    
    # మొత్తం స్థితి
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

## 🚀 అధునాతన కాన్ఫిగరేషన్

### బహుళ సర్వర్ సెటప్

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

### కస్టమ్ VS Code ఎక్స్‌టెన్షన్

```typescript
// src/extension.ts - కస్టమ్ MCP రిటైల్ ఎక్స్‌టెన్షన్
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    
    // MCP రిటైల్ కమాండ్లను నమోదు చేయండి
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
    
    // స్టోర్ స్విచ్చర్‌ను నమోదు చేయండి
    const storeSwitcher = vscode.commands.registerCommand(
        'mcp-retail.switchStore',
        async () => {
            const stores = ['seattle', 'redmond', 'bellevue', 'online'];
            const selected = await vscode.window.showQuickPick(stores, {
                placeHolder: 'Select store for queries'
            });
            
            if (selected) {
                // కాన్ఫిగరేషన్‌ను నవీకరించండి
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
    // VS కోడ్ చాట్‌లో ముందుగా నిర్వచించిన ప్రశ్నలను అమలు చేయండి
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

### ఎక్స్‌టెన్షన్ ప్యాకేజ్ కాన్ఫిగరేషన్

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

## 🎯 ముఖ్యమైన పాఠాలు

ఈ ల్యాబ్ పూర్తి చేసిన తర్వాత, మీ వద్ద ఉండాలి:

✅ **VS Code MCP కాన్ఫిగరేషన్**: MCP ఇంటిగ్రేషన్ కోసం పూర్తి సెటప్  
✅ **AI చాట్ ఇంటిగ్రేషన్**: VS Code లో సహజ భాషా ప్రశ్నల సామర్థ్యాలు  
✅ **డీబగింగ్ టూల్స్**: సమగ్ర సమస్య పరిష్కారం మరియు కనెక్షన్ డయాగ్నోస్టిక్స్  
✅ **బహుళ సర్వర్ సెటప్**: బహుళ MCP సర్వర్ ఇన్స్టాన్సుల కోసం కాన్ఫిగరేషన్  
✅ **కస్టమ్ ఎక్స్‌టెన్షన్లు**: రిటైల్-స్పెసిఫిక్ ఫీచర్లతో మెరుగైన VS Code అనుభవం  
✅ **ప్రొడక్షన్ రెడినెస్**: ఎంటర్ప్రైజ్-సిద్ధ VS Code డెవలప్‌మెంట్ వాతావరణం  

## 🚀 తదుపరి ఏమిటి

**[ల్యాబ్ 10: డిప్లాయ్‌మెంట్ వ్యూహాలు](../10-Deployment/README.md)** తో కొనసాగండి:

- MCP సర్వర్లను ప్రొడక్షన్ వాతావరణాలకు డిప్లాయ్ చేయడం  
- స్కేలబిలిటీ కోసం క్లౌడ్ ఇన్‌ఫ్రాస్ట్రక్చర్ కాన్ఫిగర్ చేయడం  
- ఆటోమేటెడ్ డిప్లాయ్‌మెంట్ కోసం CI/CD పైప్లైన్లను అమలు చేయడం  
- ప్రొడక్షన్ MCP సర్వర్ పనితీరును మానిటర్ చేయడం  

## 📚 అదనపు వనరులు

### VS Code డెవలప్‌మెంట్  
- [VS Code ఎక్స్‌టెన్షన్ API](https://code.visualstudio.com/api) - అధికారిక ఎక్స్‌టెన్షన్ డెవలప్‌మెంట్ గైడ్  
- [VS Code MCP డాక్యుమెంటేషన్](https://code.visualstudio.com/docs/copilot/copilot-extensibility-overview) - MCP ఇంటిగ్రేషన్ డాక్యుమెంటేషన్  
- [VS Code కోసం TypeScript](https://code.visualstudio.com/docs/languages/typescript) - VS Code లో TypeScript డెవలప్‌మెంట్  

### MCP ప్రోటోకాల్  
- [మోడల్ కాంటెక్స్ట్ ప్రోటోకాల్ స్పెసిఫికేషన్](https://modelcontextprotocol.io/specification) - అధికారిక MCP స్పెసిఫికేషన్  
- [MCP ఉత్తమ పద్ధతులు](https://modelcontextprotocol.io/docs/best-practices) - అమలు ఉత్తమ పద్ధతులు  
- [FastMCP ఫ్రేమ్‌వర్క్](https://github.com/jlowin/fastmcp) - Python MCP అమలు  

### డెవలప్‌మెంట్ టూల్స్  
- [VS Code లో Python](https://code.visualstudio.com/docs/python/python-tutorial) - Python డెవలప్‌మెంట్ సెటప్  
- [VS Code లో డీబగింగ్](https://code.visualstudio.com/docs/editor/debugging) - అధునాతన డీబగింగ్ సాంకేతికతలు  
- [VS Code టాస్క్స్](https://code.visualstudio.com/docs/editor/tasks) - టాస్క్ ఆటోమేషన్ మరియు కాన్ఫిగరేషన్  

---

**మునుపటి**: [ల్యాబ్ 08: టెస్టింగ్ మరియు డీబగింగ్](../08-Testing/README.md)  
**తదుపరి**: [ల్యాబ్ 10: డిప్లాయ్‌మెంట్ వ్యూహాలు](../10-Deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->