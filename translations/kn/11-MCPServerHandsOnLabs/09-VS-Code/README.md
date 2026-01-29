# VS Code ಏಕೀಕರಣ

## 🎯 ಈ ಪ್ರಯೋಗಶಾಲೆ ಏನು ಒಳಗೊಂಡಿದೆ

ಈ ಪ್ರಯೋಗಶಾಲೆ ನಿಮ್ಮ MCP ಸರ್ವರ್ ಅನ್ನು VS Code ಜೊತೆಗೆ ಏಕೀಕರಿಸುವ ಬಗ್ಗೆ ಸಮಗ್ರ ಮಾರ್ಗದರ್ಶನವನ್ನು ಒದಗಿಸುತ್ತದೆ, ಇದರಿಂದ AI ಚಾಟ್ ಮೂಲಕ ನೈಸರ್ಗಿಕ ಭಾಷಾ ಪ್ರಶ್ನೆಗಳನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಬಹುದು. ನೀವು MCP ಬಳಕೆಗೆ ಸೂಕ್ತವಾಗಿ VS Code ಅನ್ನು ಸಂರಚಿಸುವುದು, ಸರ್ವರ್ ಸಂಪರ್ಕಗಳನ್ನು ಡಿಬಗ್ ಮಾಡುವುದು ಮತ್ತು AI ಸಹಾಯಿತ ಡೇಟಾಬೇಸ್ ಸಂವಹನಗಳ ಸಂಪೂರ್ಣ ಶಕ್ತಿಯನ್ನು ಬಳಸಿಕೊಳ್ಳುವುದು ಕಲಿಯುತ್ತೀರಿ.

## ಅವಲೋಕನ

VS Code ನ MCP ಏಕೀಕರಣವು ಡೆವಲಪರ್‌ಗಳು ನೈಸರ್ಗಿಕ ಭಾಷೆಯ ಮೂಲಕ ಡೇಟಾಬೇಸ್‌ಗಳು ಮತ್ತು API ಗಳೊಂದಿಗೆ ಸಂವಹನ ಮಾಡುವ ರೀತಿಯನ್ನು ಪರಿವರ್ತಿಸುತ್ತದೆ. ನಿಮ್ಮ ರಿಟೇಲ್ MCP ಸರ್ವರ್ ಅನ್ನು VS Code ಚಾಟ್‌ಗೆ ಸಂಪರ್ಕಿಸುವ ಮೂಲಕ, ನೀವು ಸಂವಾದಾತ್ಮಕ AI ಬಳಸಿ ಮಾರಾಟದ ಡೇಟಾ, ಉತ್ಪನ್ನ ಕ್ಯಾಟಲಾಗ್‌ಗಳು ಮತ್ತು ವ್ಯವಹಾರ ವಿಶ್ಲೇಷಣೆಗಳ ಬುದ್ಧಿವಂತ ಪ್ರಶ್ನೆಗಳನ್ನು ಸಕ್ರಿಯಗೊಳಿಸುತ್ತೀರಿ.

ಈ ಏಕೀಕರಣವು ಡೆವಲಪರ್‌ಗಳಿಗೆ "ಈ ತಿಂಗಳು ಅತ್ಯಧಿಕ ಮಾರಾಟವಾದ ಉತ್ಪನ್ನಗಳನ್ನು ತೋರಿಸಿ" ಅಥವಾ "90 ದಿನಗಳಲ್ಲಿ ಖರೀದಿ ಮಾಡದ ಗ್ರಾಹಕರನ್ನು ಹುಡುಕಿ" ಎಂಬಂತಹ ಪ್ರಶ್ನೆಗಳನ್ನು ಕೇಳಲು ಮತ್ತು SQL ಪ್ರಶ್ನೆಗಳನ್ನು ಬರೆಯದೆ ರಚನಾತ್ಮಕ ಡೇಟಾ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ಪಡೆಯಲು ಅನುಮತಿಸುತ್ತದೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪ್ರಯೋಗಶಾಲೆಯ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಈ ಕೆಳಗಿನವುಗಳನ್ನು ಮಾಡಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- **ಸಂರಚಿಸುವುದು** ನಿಮ್ಮ ರಿಟೇಲ್ ಸರ್ವರ್‌ಗಾಗಿ VS Code MCP ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು  
- **ಏಕೀಕರಿಸುವುದು** MCP ಸರ್ವರ್‌ಗಳನ್ನು VS Code AI ಚಾಟ್ ಕಾರ್ಯಕ್ಷಮತೆಯೊಂದಿಗೆ  
- **ಡಿಬಗ್ ಮಾಡುವುದು** MCP ಸರ್ವರ್ ಸಂಪರ್ಕಗಳನ್ನು ಮತ್ತು ಸಮಸ್ಯೆಗಳನ್ನು ಪರಿಹರಿಸುವುದು  
- **ಆಪ್ಟಿಮೈಸ್ ಮಾಡುವುದು** ಉತ್ತಮ ಫಲಿತಾಂಶಗಳಿಗಾಗಿ ನೈಸರ್ಗಿಕ ಭಾಷಾ ಪ್ರಶ್ನೆ ಮಾದರಿಗಳನ್ನು  
- **ಕಸ್ಟಮೈಸ್ ಮಾಡುವುದು** MCP ಅಭಿವೃದ್ಧಿಗಾಗಿ VS Code ವರ್ಕ್‌ಸ್ಪೇಸ್ ಅನ್ನು  
- **ಡಿಪ್ಲಾಯ್ ಮಾಡುವುದು** ಸಂಕೀರ್ಣ ಸಂದರ್ಭಗಳಿಗೆ ಬಹು-ಸರ್ವರ್ ಸಂರಚನೆಗಳನ್ನು  

## 🔧 VS Code MCP ಸಂರಚನೆ

### ಪ್ರಾಥಮಿಕ ಸೆಟ್‌ಅಪ್ ಮತ್ತು ಸ್ಥಾಪನೆ

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

### ಪರಿಸರ ಸಂರಚನೆ

```bash
# ಅಭಿವೃದ್ಧಿಗಾಗಿ .env ಫೈಲ್
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=retail_db
POSTGRES_USER=mcp_user
POSTGRES_PASSWORD=your_secure_password

# ಅಜೂರ್ ಸಂರಚನೆ
PROJECT_ENDPOINT=https://your-project.openai.azure.com
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
AZURE_TENANT_ID=your-tenant-id

# ಐಚ್ಛಿಕ: ಅಜೂರ್ ಕೀ ವಾಲ್ಟ್
AZURE_KEY_VAULT_URL=https://your-keyvault.vault.azure.net/

# ಸರ್ವರ್ ಸಂರಚನೆ
MCP_SERVER_PORT=8000
MCP_SERVER_HOST=127.0.0.1
LOG_LEVEL=INFO
```

### ವರ್ಕ್‌ಸ್ಪೇಸ್ ಸಂರಚನೆ

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

### ಟಾಸ್ಕ್ ಸಂರಚನೆ

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

## 💬 AI ಚಾಟ್ ಏಕೀಕರಣ

### ನೈಸರ್ಗಿಕ ಭಾಷಾ ಪ್ರಶ್ನೆ ಮಾದರಿಗಳು

```typescript
// VS ಕೋಡ್ ಚಾಟ್‌ಗಾಗಿ ಉದಾಹರಣಾ ಪ್ರಶ್ನೆ ಮಾದರಿಗಳು
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

### ಚಾಟ್ ಏಕೀಕರಣ ಉದಾಹರಣೆಗಳು

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

### ಚಾಟ್ ಪ್ರತಿಕ್ರಿಯೆ ಸ್ವರೂಪೀಕರಣ

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
        
        # ಪ್ರಮುಖ ಅಂಶಗಳು
        response += "### Key Performance Indicators\n\n"
        response += f"- **Total Revenue**: ${float(data.get('total_revenue', 0)):,.2f}\n"
        response += f"- **Total Transactions**: {int(data.get('total_transactions', 0)):,}\n"
        response += f"- **Unique Customers**: {int(data.get('unique_customers', 0)):,}\n"
        response += f"- **Average Order Value**: ${float(data.get('avg_transaction_value', 0)):.2f}\n"
        response += f"- **Products Sold**: {int(data.get('products_sold', 0)):,} items\n\n"
        
        # ಕಾರ್ಯಕ್ಷಮತೆ ಸೂಚಕಗಳು
        if 'insights' in data and 'performance_indicators' in data['insights']:
            pi = data['insights']['performance_indicators']
            response += "### Performance Indicators\n\n"
            response += f"- **Transactions per Day**: {float(pi.get('transactions_per_day', 0)):.1f}\n"
            response += f"- **Revenue per Customer**: ${float(pi.get('revenue_per_customer', 0)):,.2f}\n"
            response += f"- **Items per Transaction**: {float(pi.get('items_per_transaction', 0)):.1f}\n\n"
        
        # ಶ್ರೇಷ್ಟ ವರ್ಗ
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

## 🔍 ಡಿಬಗ್ ಮತ್ತು ಸಮಸ್ಯೆ ಪರಿಹಾರ

### VS Code ಡಿಬಗ್ ಸಂರಚನೆ

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
        
        # VS ಕೋಡ್ ನಿರ್ದಿಷ್ಟ ಫಾರ್ಮ್ಯಾಟರ್ ರಚಿಸಿ
        formatter = logging.Formatter(
            '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'
        )
        
        # VS ಕೋಡ್ ಟರ್ಮಿನಲ್‌ಗಾಗಿ ಕಾನ್ಸೋಲ್ ಹ್ಯಾಂಡ್ಲರ್
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

# ಜಾಗತಿಕ ಡಿಬಗ್ ಲಾಗರ್
vscode_debug_logger = VSCodeDebugLogger()
```

### ಸಂಪರ್ಕ ಸಮಸ್ಯೆ ಪರಿಹಾರ

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
        # ಪರಿಸರದಿಂದ ಸಂಪರ್ಕ ಪರಿಮಾಣಗಳನ್ನು ಪಡೆಯಿರಿ
        connection_params = {
            'host': os.getenv('POSTGRES_HOST', 'localhost'),
            'port': int(os.getenv('POSTGRES_PORT', '5432')),
            'database': os.getenv('POSTGRES_DB', 'retail_db'),
            'user': os.getenv('POSTGRES_USER', 'mcp_user'),
            'password': os.getenv('POSTGRES_PASSWORD', '')
        }
        
        print(f"Testing connection to {connection_params['host']}:{connection_params['port']}")
        
        # ಸಂಪರ್ಕವನ್ನು ಪರೀಕ್ಷಿಸಿ
        conn = await asyncpg.connect(**connection_params)
        
        # ಮೂಲ ಪ್ರಶ್ನೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ
        result = await conn.fetchval("SELECT version()")
        
        # ಸ್ಕೀಮಾ ಪ್ರವೇಶವನ್ನು ಪರೀಕ್ಷಿಸಿ
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
        
        # ಎम्बೆಡ್ಡಿಂಗ್ ಉತ್ಪಾದನೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ
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
        # MCP ಸರ್ವರ್ ಘಟಕಗಳನ್ನು ಆಮದುಮಾಡಿ
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))
        
        from mcp_server.server import MCPServer
        from mcp_server.database import DatabaseProvider
        from mcp_server.config import Config
        
        # ಪರೀಕ್ಷಾ ಸಂರಚನೆಯನ್ನು ರಚಿಸಿ
        config = Config()
        db_provider = DatabaseProvider(config.database.connection_string)
        
        # ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ
        server = MCPServer(config, db_provider)
        await server.initialize()
        
        # ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು ಪಡೆಯಿರಿ
        tools = server.get_available_tools()
        
        # ಸರಳ ಸಾಧನವನ್ನು ಪರೀಕ್ಷಿಸಿ
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
    
    # ಡೇಟಾಬೇಸ್ ಸಂಪರ್ಕವನ್ನು ಪರೀಕ್ಷಿಸಿ
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
    
    # ಅಜೂರ್ ಓಪನ್‌ಎಐ ಸಂಪರ್ಕವನ್ನು ಪರೀಕ್ಷಿಸಿ
    print("\n🤖 Testing Azure OpenAI Connection...")
    azure_result = await test_azure_openai_connection()
    
    if azure_result['success']:
        print("✅ Azure OpenAI connection successful")
        print(f"   Endpoint: {azure_result['project_endpoint']}")
        print(f"   Embedding dimension: {azure_result['embedding_dimension']}")
    else:
        print("❌ Azure OpenAI connection failed")
        print(f"   Error: {azure_result['error']}")
    
    # MCP ಸಾಧನಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ
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
    
    # ಒಟ್ಟು ಸ್ಥಿತಿ
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

## 🚀 ಉನ್ನತ ಸಂರಚನೆ

### ಬಹು-ಸರ್ವರ್ ಸೆಟ್‌ಅಪ್

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

### ಕಸ್ಟಮ್ VS Code ವಿಸ್ತರಣೆ

```typescript
// src/extension.ts - ಕಸ್ಟಮ್ MCP ರೀಟೇಲ್ ವಿಸ್ತರಣೆ
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    
    // MCP ರೀಟೇಲ್ ಆಜ್ಞೆಗಳನ್ನು ನೋಂದಣಿ ಮಾಡು
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
    
    // ಸ್ಟೋರ್ ಸ್ವಿಚರ್ ಅನ್ನು ನೋಂದಣಿ ಮಾಡು
    const storeSwitcher = vscode.commands.registerCommand(
        'mcp-retail.switchStore',
        async () => {
            const stores = ['seattle', 'redmond', 'bellevue', 'online'];
            const selected = await vscode.window.showQuickPick(stores, {
                placeHolder: 'Select store for queries'
            });
            
            if (selected) {
                // ಸಂರಚನೆಯನ್ನು ನವೀಕರಿಸು
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
    // VS ಕೋಡ್ ಚಾಟ್‌ನಲ್ಲಿ ಪೂರ್ವನಿರ್ಧರಿತ ಪ್ರಶ್ನೆಗಳನ್ನು ನಿರ್ವಹಿಸು
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

### ವಿಸ್ತರಣೆ ಪ್ಯಾಕೇಜ್ ಸಂರಚನೆ

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

## 🎯 ಪ್ರಮುಖ ಪಾಠಗಳು

ಈ ಪ್ರಯೋಗಶಾಲೆಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಹೊಂದಿರಬೇಕು:

✅ **VS Code MCP ಸಂರಚನೆ**: MCP ಏಕೀಕರಣಕ್ಕಾಗಿ ಸಂಪೂರ್ಣ ಸೆಟ್‌ಅಪ್  
✅ **AI ಚಾಟ್ ಏಕೀಕರಣ**: VS Code ನಲ್ಲಿ ನೈಸರ್ಗಿಕ ಭಾಷಾ ಪ್ರಶ್ನೆ ಸಾಮರ್ಥ್ಯಗಳು  
✅ **ಡಿಬಗ್ ಸಾಧನಗಳು**: ಸಮಗ್ರ ಸಮಸ್ಯೆ ಪರಿಹಾರ ಮತ್ತು ಸಂಪರ್ಕ ವಿಶ್ಲೇಷಣೆ  
✅ **ಬಹು-ಸರ್ವರ್ ಸೆಟ್‌ಅಪ್**: ಬಹು MCP ಸರ್ವರ್ ಉದಾಹರಣೆಗಳ ಸಂರಚನೆ  
✅ **ಕಸ್ಟಮ್ ವಿಸ್ತರಣೆಗಳು**: ರಿಟೇಲ್-ನಿರ್ದಿಷ್ಟ ವೈಶಿಷ್ಟ್ಯಗಳೊಂದಿಗೆ ಸುಧಾರಿತ VS Code ಅನುಭವ  
✅ **ಉತ್ಪಾದನಾ ಸಿದ್ಧತೆ**: ಎಂಟರ್‌ಪ್ರೈಸ್-ಸಿದ್ಧ VS Code ಅಭಿವೃದ್ಧಿ ಪರಿಸರ  

## 🚀 ಮುಂದಿನದು ಏನು

**[ಪ್ರಯೋಗಶಾಲೆ 10: ನಿಯೋಜನೆ ತಂತ್ರಗಳು](../10-Deployment/README.md)** ಜೊತೆಗೆ ಮುಂದುವರಿಯಿರಿ:

- MCP ಸರ್ವರ್‌ಗಳನ್ನು ಉತ್ಪಾದನಾ ಪರಿಸರಗಳಿಗೆ ನಿಯೋಜಿಸುವುದು  
- ವಿಸ್ತರಣೆಗೆ ಕ್ಲೌಡ್ ಮೂಲಸೌಕರ್ಯವನ್ನು ಸಂರಚಿಸುವುದು  
- ಸ್ವಯಂಚಾಲಿತ ನಿಯೋಜನೆಗಾಗಿ CI/CD ಪೈಪ್ಲೈನ್ಗಳನ್ನು ಜಾರಿಗೆ ತರುವುದು  
- ಉತ್ಪಾದನಾ MCP ಸರ್ವರ್ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡುವುದು  

## 📚 ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

### VS Code ಅಭಿವೃದ್ಧಿ  
- [VS Code ವಿಸ್ತರಣೆ API](https://code.visualstudio.com/api) - ಅಧಿಕೃತ ವಿಸ್ತರಣೆ ಅಭಿವೃದ್ಧಿ ಮಾರ್ಗದರ್ಶಿ  
- [VS Code MCP ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://code.visualstudio.com/docs/copilot/copilot-extensibility-overview) - MCP ಏಕೀಕರಣ ಡಾಕ್ಯುಮೆಂಟೇಶನ್  
- [VS Code ಗೆ ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್](https://code.visualstudio.com/docs/languages/typescript) - VS Code ನಲ್ಲಿ ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್ ಅಭಿವೃದ್ಧಿ  

### MCP ಪ್ರೋಟೋಕಾಲ್  
- [ಮಾದರಿ ಸಂಧರ್ಭ ಪ್ರೋಟೋಕಾಲ್ ಸ್ಪೆಸಿಫಿಕೇಶನ್](https://modelcontextprotocol.io/specification) - ಅಧಿಕೃತ MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್  
- [MCP ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು](https://modelcontextprotocol.io/docs/best-practices) - ಜಾರಿಗೆ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು  
- [ಫಾಸ್ಟ್MCP ಫ್ರೇಮ್ವರ್ಕ್](https://github.com/jlowin/fastmcp) - ಪೈಥಾನ್ MCP ಜಾರಿಗೆ  

### ಅಭಿವೃದ್ಧಿ ಸಾಧನಗಳು  
- [VS Code ನಲ್ಲಿ ಪೈಥಾನ್](https://code.visualstudio.com/docs/python/python-tutorial) - ಪೈಥಾನ್ ಅಭಿವೃದ್ಧಿ ಸೆಟ್‌ಅಪ್  
- [VS Code ನಲ್ಲಿ ಡಿಬಗ್](https://code.visualstudio.com/docs/editor/debugging) - ಉನ್ನತ ಮಟ್ಟದ ಡಿಬಗ್ ತಂತ್ರಗಳು  
- [VS Code ಟಾಸ್ಕ್‌ಗಳು](https://code.visualstudio.com/docs/editor/tasks) - ಟಾಸ್ಕ್ ಸ್ವಯಂಚಾಲನೆ ಮತ್ತು ಸಂರಚನೆ  

---

**ಹಿಂದಿನದು**: [ಪ್ರಯೋಗಶಾಲೆ 08: ಪರೀಕ್ಷೆ ಮತ್ತು ಡಿಬಗ್](../08-Testing/README.md)  
**ಮುಂದಿನದು**: [ಪ್ರಯೋಗಶಾಲೆ 10: ನಿಯೋಜನೆ ತಂತ್ರಗಳು](../10-Deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->