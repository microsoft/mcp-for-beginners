# VS Code ပေါင်းစည်းမှု

> [!NOTE]
> ဒီလက်တွေ့လေ့လာမှုမှာ `initializationOptions` သတ်မှတ်ချက်တွေက နမူနာ MCP
> `2025-11-25` ဆက်သွယ်မှုကို ဦးတည်ထားတယ်။ MCP `2026-07-28` မှာ initialization ဆက်သွယ်မှုကို ဖယ်ရှား
> ထားတဲ့အတွက် ဒီနမူနာကိုပြောင်းရွှေ့တဲ့အခါ per-request metadata နဲ့ `server/discover`
> ကိုပံ့ပိုးတဲ့ host နဲ့ SDK ကို အသုံးပြုပါ။

## 🎯 ဒီလက်တွေ့လေ့လာမှုကဘာတွေ ပါဝင်သလဲ

ဒီလက်တွေ့လေ့လာမှုက MCP ဆာဗာနဲ့ VS Code ကိုပေါင်းစည်းခြင်းအခြေခံနဲ့ ကျယ်ပြန့်စွာ လမ်းညွှန်ချက်တွေနဲ့ သင်ယူပေးပါမယ်။ VS Code ကို MCP အတွက် အကောင်းဆုံး သုံးနိုင်ရန် ပြင်ဆင်ခြင်း၊ ဆာဗာ ဆက်သွယ်မှုများကို ဖြေရှင်းခြင်းနှင့် AI အကူအညီဖြင့် ဒေတာဘေ့စ်ဆိုင်ရာ ဆက်သွယ်မှုများကို ပြုလုပ်နည်းတွေကို သင်ယူနိုင်မှာ ဖြစ်ပါတယ်။

## အကျဉ်းချုပ်

VS Code ရဲ့ MCP ပေါင်းစည်းမှုက developer တွေအတွက် database နဲ့ API တွေကို သဘာဝဘာသာစကားဖြင့် လွယ်ကူစွာ ဆက်သွယ်ခွင့် ပေးပါတယ်။ သင့် retail MCP ဆာဗာကို VS Code Chat နဲ့ချိတ်ဆက်ခြင်းဖြင့် အရောင်းဒေတာ၊ ကုန်ပစ္စည်းစာရင်း၊ စီးပွားရေးဗွီဇနယ်များကို AI စကားပြောမှတဆင့် ရှာဖွေမေးမြန်းနိုင်ပါတယ်။

ဒီပေါင်းစည်းမှုက developer တွေကို "ဒီလအတွင်း ထိပ်တန်းရောင်းအားများပြပါ" သို့မဟုတ် "90 ရက်အတွင်း အဝယ်မလုပ်သော ဖောက်သည်များကို ရှာပါ" လို့မေးနိုင်ပြီး SQL စာသား မရေးပါဘဲ တိကျသော ဒေတာများကို ရရှိစေပါတယ်။

## သင်ယူရမည့် အချက်များ

ဒီလက်တွေ့လေ့လာမှုပြီးဆုံးချိန်မှာ သင်တက်ရောက်နိုင်မှာများကတော့ -

- သင့် retail ဆာဗာအတွက် VS Code MCP သတ်မှတ်ချက်များ **ပြင်ဆင်**နိုင်ခြင်း
- MCP ဆာဗာများကို VS Code AI Chat လုပ်ဆောင်ချက်များနှင့် **ပေါင်းစည်း**နိုင်ခြင်း
- MCP ဆာဗာ ဆက်သွယ်မှုများကို **ဖြေရှင်း**၍ ပြဿနာများကို စူးစမ်းရှာဖွေနိုင်ခြင်း
- သဘာဝဘာသာစကား မေးခွန်းမပုံများကို **အကောင်းဆုံးဖြစ်အောင် မြှင့်တင်**ခြင်း
- MCP ဖွံ့ဖြိုးရေးအတွက် VS Code workspace ကို **စိတ်ကြိုက်ပြင်ဆင်**နိုင်ခြင်း
- ရှုပ်ထွေးသောအခြေအနေများအတွက် multi-server ကွန်ဖစ်ဂျူရေးရှင်းများကို **တပ်ဆင်**နိုင်ခြင်း

## 🔧 VS Code MCP ပြင်ဆင်ခြင်း

### ပထမဆုံး ပြင်ဆင်မှုနှင့် ထည့်သွင်းခြင်း

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

### ပတ်ဝန်းကျင် ပြင်ဆင်ခြင်း

```bash
# ဖွံ့ဖြိုးတိုးတက်မှုအတွက် .env ဖိုင်
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=retail_db
POSTGRES_USER=mcp_user
POSTGRES_PASSWORD=your_secure_password

# Azure ဆက်တင်များ
PROJECT_ENDPOINT=https://your-project.openai.azure.com
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
AZURE_TENANT_ID=your-tenant-id

# ရွေးချယ်စရာ: Azure Key Vault
AZURE_KEY_VAULT_URL=https://your-keyvault.vault.azure.net/

# ဆာဗာ ဆက်တင်များ
MCP_SERVER_PORT=8000
MCP_SERVER_HOST=127.0.0.1
LOG_LEVEL=INFO
```

### အလုပ်နေရာ ပြင်ဆင်ခြင်း

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

### တာဝန် ပြင်ဆင်ခြင်း

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

## 💬 AI စကားပြော ပေါင်းစည်းမှု

### သဘာဝဘာသာစကား မေးခွန်းပုံစံများ

```typescript
// VS Code Chat အတွက် နမူနာ မေးခွန်းပုံစံများ
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

### စကားပြောပေါင်းစည်းမှု ဥပမာများ

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

### စကားပြန် ပြန်လည်ဖော်ပြမှု အစီအစဉ်

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
        
        # အဓိကတိုင်းတာခန့်မှန်းချက်များ
        response += "### Key Performance Indicators\n\n"
        response += f"- **Total Revenue**: ${float(data.get('total_revenue', 0)):,.2f}\n"
        response += f"- **Total Transactions**: {int(data.get('total_transactions', 0)):,}\n"
        response += f"- **Unique Customers**: {int(data.get('unique_customers', 0)):,}\n"
        response += f"- **Average Order Value**: ${float(data.get('avg_transaction_value', 0)):.2f}\n"
        response += f"- **Products Sold**: {int(data.get('products_sold', 0)):,} items\n\n"
        
        # ဖျော်ဖြေတာ ဆုံးဖြတ်ချက်များ
        if 'insights' in data and 'performance_indicators' in data['insights']:
            pi = data['insights']['performance_indicators']
            response += "### Performance Indicators\n\n"
            response += f"- **Transactions per Day**: {float(pi.get('transactions_per_day', 0)):.1f}\n"
            response += f"- **Revenue per Customer**: ${float(pi.get('revenue_per_customer', 0)):,.2f}\n"
            response += f"- **Items per Transaction**: {float(pi.get('items_per_transaction', 0)):.1f}\n\n"
        
        # ထိပ်တန်းအမျိုးအစား
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

## 🔍 ပြဿနာရှာဖွေအကူအညီနှင့် ဖြေရှင်းမှု

### VS Code ဖြေရှင်းမှု ပြင်ဆင်ခြင်း

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
        
        # VS Code အတွက် အထူးဖော်မြူလာ တစ်ခု ဖန်တီးပါ
        formatter = logging.Formatter(
            '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'
        )
        
        # VS Code terminal အတွက် Console handler
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

# ကမ္ဘာလုံးဆိုင်ရာ debug logger
vscode_debug_logger = VSCodeDebugLogger()
```

### ဆက်သွယ်မှု ပြဿနာရှာဖွေရေး

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
        # ပတ်ဝန်းကျင်မှ ချိတ်ဆက်ချက် ပါရာမီတာများ ရယူသည်
        connection_params = {
            'host': os.getenv('POSTGRES_HOST', 'localhost'),
            'port': int(os.getenv('POSTGRES_PORT', '5432')),
            'database': os.getenv('POSTGRES_DB', 'retail_db'),
            'user': os.getenv('POSTGRES_USER', 'mcp_user'),
            'password': os.getenv('POSTGRES_PASSWORD', '')
        }
        
        print(f"Testing connection to {connection_params['host']}:{connection_params['port']}")
        
        # ချိတ်ဆက်မှု စမ်းသပ်သည်
        conn = await asyncpg.connect(**connection_params)
        
        # အခြေခံ စုံစမ်းမေးမြန်းမှု စမ်းသပ်သည်
        result = await conn.fetchval("SELECT version()")
        
        # ပုံစံအသုံးပြုခွင့် စမ်းသပ်သည်
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
        
        # အင်ဘက်ဒ်ထောက် ထုတ်လုပ်မှု စမ်းသပ်သည်
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
        # MCP ဆာဗာ အစိတ်အပိုင်းများ ထည့်သွင်းသည်
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))
        
        from mcp_server.server import MCPServer
        from mcp_server.database import DatabaseProvider
        from mcp_server.config import Config
        
        # စမ်းသပ်ရန် ပုံစံဖွဲ့စည်းမှု ပြုလုပ်သည်
        config = Config()
        db_provider = DatabaseProvider(config.database.connection_string)
        
        # ဆာဗာ သတ်မှတ်ပေးသည်
        server = MCPServer(config, db_provider)
        await server.initialize()
        
        # အသုံးပြုနိုင်သော တူလ်များ ရယူသည်
        tools = server.get_available_tools()
        
        # ရိုးရှင်းသော တူလ်တစ်ခု စမ်းသပ်သည်
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
    
    # ဒေတာဘေ့စ် ချိတ်ဆက်မှု စမ်းသပ်သည်
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
    
    # Azure OpenAI ချိတ်ဆက်မှု စမ်းသပ်သည်
    print("\n🤖 Testing Azure OpenAI Connection...")
    azure_result = await test_azure_openai_connection()
    
    if azure_result['success']:
        print("✅ Azure OpenAI connection successful")
        print(f"   Endpoint: {azure_result['project_endpoint']}")
        print(f"   Embedding dimension: {azure_result['embedding_dimension']}")
    else:
        print("❌ Azure OpenAI connection failed")
        print(f"   Error: {azure_result['error']}")
    
    # MCP တူလ်များ စမ်းသပ်သည်
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
    
    # စုစုပေါင်း အခြေအနေ
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

## 🚀 အဆင့်မြင့် ပြင်ဆင်မှု

### Multi-Server တပ်ဆင်ခြင်း

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

### စိတ်ကြိုက် VS Code တိုးချဲ့မှု

```typescript
// src/extension.ts - စိတ်ကြိုက် MCP လက်လီချဲ့ထွင်မှု
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    
    // MCP လက်လီအမိန့်များမှတ်ပုံတင်ပါ
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
    
    // ဆိုင်ပြောင်းလဲမှု အစက်များမှတ်ပုံတင်ပါ
    const storeSwitcher = vscode.commands.registerCommand(
        'mcp-retail.switchStore',
        async () => {
            const stores = ['seattle', 'redmond', 'bellevue', 'online'];
            const selected = await vscode.window.showQuickPick(stores, {
                placeHolder: 'Select store for queries'
            });
            
            if (selected) {
                // ဖော်ပြချက်အား အပ်ဒိတ်လုပ်ပါ
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
    // VS Code Chat တွင် ကြိုတင်သတ်မှတ်ထားသော စုံစမ်းမေးမြန်းမှုများ ကို အကောင်အထည်ဖော်ပါ
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

### တိုးချဲ့မှု ပက်ကေ့ဂျ် ပြင်ဆင်မှု

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

## 🎯 အဓိက သိရှိသင့်သောအချက်များ

ဒီလေ့လာမှုပြီးဆုံးလျှင် သင်မှာရှိနေမယ့်အရာတွေကတော့ -

✅ **VS Code MCP ပြင်ဆင်မှု**: MCP ပေါင်းစည်းမှုအတွက် ပြည့်စုံစွာ ပြင်ဆင်ထားခြင်း  
✅ **AI စကားပြော ပေါင်းစည်းမှု**: VS Code မှ သဘာဝဘာသာစကားဖြင့် မေးခွန်းမပုံစံအသုံးပြုနိုင်ခြင်း  
✅ **ပြဿနာရှာဖွေရေး စနစ်များ**: ပြဿနာများ ဖြေရှင်းခြင်းနှင့် ဆက်သွယ်မှု စစ်ဆေးခြင်း  
✅ **Multi-Server တပ်ဆင်မှု**: MCP ဆာဗာ များစွာအတွက် ကွန်ဖစ်ဂျူရေးရှင်းများ  
✅ **စိတ်ကြိုက် တိုးချဲ့မှုများ**: retail အထူး လုပ်ဆောင်ချက်များနဲ့ VS Code အတွေ့အကြုံ တိုးတက်ခြင်း  
✅ **ထုတ်လုပ်မှု အသင့်အဆင့်**: စီးပွားရေးအဆင့် VS Code ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်  

## 🚀 နောက်တစ်ဆင့် ဘာတွေရှိလဲ

**[Lab 10: Deployment Strategies](../10-Deployment/README.md)** ကို ဆက်လက် လေ့လာပြီး -

- MCP ဆာဗာများကို ထုတ်လုပ်မှု ပတ်ဝန်းကျင်သို့ တပ်ဆင်ခြင်း
- တိုးချဲ့နိုင်စေရန် မိုဃ်းကွယ် အခြေခံအဆောက်အအုံ ပြင်ဆင်ခြင်း
- CI/CD လုပ်ထုံးလုပ်နည်းများ လက်တွေ့ အသုံးပြုခြင်း
- ထုတ်လုပ်မှု MCP ဆာဗာ လုပ်ဆောင်ချက်များကို စောင့်ကြပ်ခြင်း

## 📚 အပိုဆောင်း အရင်းအမြစ်များ

### VS Code ဖွံ့ဖြိုးရေး
- [VS Code Extension API](https://code.visualstudio.com/api) - တရားဝင် တိုးချဲ့မှု ဖွံ့ဖြိုးရေး လမ်းညွှန်
- [VS Code MCP ပြကြားချက်](https://code.visualstudio.com/docs/copilot/copilot-extensibility-overview) - MCP ပေါင်းစည်းမှု စာတမ်း
- [VS Code အတွက် TypeScript](https://code.visualstudio.com/docs/languages/typescript) - VS Code တွင် TypeScript ဖွံ့ဖြိုးရေး

### MCP နည်းပညာအဆောက်အအုံ
- [Model Context Protocol ဖော်ပြချက်](https://modelcontextprotocol.io/specification) - တရားဝင် MCP ဖော်ပြချက်
- [MCP အကောင်းဆုံး အတွေ့အကြုံများ](https://modelcontextprotocol.io/docs/best-practices) - လုပ်ငန်းစဉ် အကောင်းမြန်
- [FastMCP Framework](https://github.com/jlowin/fastmcp) - Python MCP အကောင်အထည်ဖော်မှု

### ဖွံ့ဖြိုးရေး ကိရိယာများ
- [Python နှင့် VS Code](https://code.visualstudio.com/docs/python/python-tutorial) - Python ဖွံ့ဖြိုးရေး ပြင်ဆင်မှု
- [VS Code တွင် ဖြေရှင်းခြင်း](https://code.visualstudio.com/docs/editor/debugging) - အဆင့်မြင့် ဖြေရှင်းနည်းများ
- [VS Code တာဝန်များ](https://code.visualstudio.com/docs/editor/tasks) - တာဝန် အလိုအလျောက်ပြုလုပ်မှုနှင့် ပြင်ဆင်မှု

---

**ယခင်**: [Lab 08: Testing and Debugging](../08-Testing/README.md)  
**နောက်တစ်ခု**: [Lab 10: Deployment Strategies](../10-Deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->