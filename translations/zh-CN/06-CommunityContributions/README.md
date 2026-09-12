# 社区与贡献

[![如何为 MCP 贡献：工具、文档、代码及更多](../../../translated_images/zh-CN/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(点击上方图片可观看本课视频)_

## 总览

本课重点讲解如何融入 MCP 社区、为 MCP 生态系统贡献力量，以及协作开发的最佳实践。了解如何参与开源 MCP 项目对希望塑造该技术未来的人来说至关重要。

## 学习目标

本课结束后，您将能够：

- 理解 MCP 社区和生态系统的结构
- 有效参与 MCP 社区论坛和讨论
- 向 MCP 开源代码库贡献力量
- 创建并分享自定义 MCP 工具和服务器
- 遵循 MCP 开发和协作的最佳实践
- 发现 MCP 开发的社区资源和框架

## MCP 社区生态系统

MCP 生态系统由多个组件和参与方组成，共同推动协议的发展。

### 主要社区组件

1. <strong>核心协议维护者</strong>：官方的 [Model Context Protocol GitHub 组织](https://github.com/modelcontextprotocol) 维护 MCP 核心规范和参考实现
2. <strong>工具开发者</strong>：创建 MCP 工具和服务器的个人和团队
3. <strong>集成提供商</strong>：将 MCP 集成到其产品和服务中的公司
4. <strong>最终用户</strong>：在其应用中使用 MCP 的开发者和组织
5. <strong>贡献者</strong>：为社区贡献代码、文档或其他资源的成员

### 社区资源

#### 官方渠道

- [MCP GitHub 组织](https://github.com/modelcontextprotocol)
- [MCP 文档](https://modelcontextprotocol.io/)
- [MCP 规范](https://modelcontextprotocol.io/specification/2026-07-28/)
- [GitHub 讨论](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP 示例与服务器代码库](https://github.com/modelcontextprotocol/servers)

#### 社区驱动资源

- [MCP 客户端](https://modelcontextprotocol.io/clients) - 支持 MCP 集成的客户端列表
- [社区 MCP 服务器](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - 不断增长的社区开发 MCP 服务器列表
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - 精选 MCP 服务器列表
- [PulseMCP](https://www.pulsemcp.com/) - 用于发现 MCP 资源的社区中心与通讯
- [Remote OpenClaw](https://www.remoteopenclaw.com/) - 免费可搜索的 MCP 服务器、代理技能及插件目录
- [Discord 服务器](https://discord.gg/jHEGxQu2a5) - 连接 MCP 开发者
- 语言特定的 SDK 实现
- 博客文章和教程

## 为 MCP 贡献

### 贡献类型

MCP 生态系统欢迎多种类型的贡献：

1. <strong>代码贡献</strong>：
   - 核心协议增强
   - Bug 修复
   - 工具和服务器实现
   - 不同语言的客户端/服务器库

2. <strong>文档</strong>：
   - 改进现有文档
   - 创建教程和指南
   - 翻译文档
   - 创建示例和样例应用

3. <strong>社区支持</strong>：
   - 在论坛和讨论中回答问题
   - 测试与报告问题
   - 组织社区活动
   - 指导新贡献者

### 贡献流程：核心协议

想为核心 MCP 协议或官方实现贡献，请遵循[官方贡献指南](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md)中的原则：

1. <strong>简洁与极简主义</strong>：MCP 规范对新增概念保持高标准。向规范添加内容比移除更容易。

2. <strong>具体方案</strong>：规范变更应基于具体实现难题，而非推测性想法。

3. <strong>提案阶段</strong>：
   - 定义：探讨问题领域，验证其他 MCP 用户是否面临类似问题
   - 原型：构建示例解决方案并展示其实用效果
   - 撰写：基于原型，编写规范提案

### 开发环境设置

```bash
# 派生仓库
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# 安装依赖
npm install

# 对于架构更改，验证并生成 schema.json：
npm run check:schema:ts
npm run generate:schema

# 对于文档更改
npm run check:docs
npm run format

# 本地预览文档（可选）：
npm run serve:docs
```

### 示例：贡献 Bug 修复

```javascript
// typescript-sdk中的原始带错误代码
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // 错误：缺少属性验证
  // 当前实现：
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// 贡献中的修复实现
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // 改进的验证
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### 示例：为标准库贡献新工具

```python
# 示例贡献：MCP标准库的CSV数据处理工具

from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
import pandas as pd
import io
import json
from typing import Dict, Any, List, Optional

class CsvProcessingTool(Tool):
    """
    Tool for processing and analyzing CSV data.
    
    This tool allows models to extract information from CSV files,
    run basic analysis, and convert data between formats.
    """
    
    def get_name(self):
        return "csvProcessor"
        
    def get_description(self):
        return "Processes and analyzes CSV data"
    
    def get_schema(self):
        return {
            "type": "object",
            "properties": {
                "csvData": {
                    "type": "string", 
                    "description": "CSV data as a string"
                },
                "csvUrl": {
                    "type": "string",
                    "description": "URL to a CSV file (alternative to csvData)"
                },
                "operation": {
                    "type": "string",
                    "enum": ["summary", "filter", "transform", "convert"],
                    "description": "Operation to perform on the CSV data"
                },
                "filterColumn": {
                    "type": "string",
                    "description": "Column to filter by (for filter operation)"
                },
                "filterValue": {
                    "type": "string",
                    "description": "Value to filter for (for filter operation)"
                },
                "outputFormat": {
                    "type": "string",
                    "enum": ["json", "csv", "markdown"],
                    "default": "json",
                    "description": "Output format for the processed data"
                }
            },
            "oneOf": [
                {"required": ["csvData", "operation"]},
                {"required": ["csvUrl", "operation"]}
            ]
        }
    
    async def execute_async(self, request: ToolRequest) -> ToolResponse:
        try:
            # 提取参数
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # 从直接数据或URL获取CSV数据
            df = await self._get_dataframe(request)
            
            # 根据请求的操作进行处理
            result = {}
            
            if operation == "summary":
                result = self._generate_summary(df)
            elif operation == "filter":
                column = request.parameters.get("filterColumn")
                value = request.parameters.get("filterValue")
                if not column:
                    raise ToolExecutionException("filterColumn is required for filter operation")
                result = self._filter_data(df, column, value)
            elif operation == "transform":
                result = self._transform_data(df, request.parameters)
            elif operation == "convert":
                result = self._convert_format(df, output_format)
            else:
                raise ToolExecutionException(f"Unknown operation: {operation}")
            
            return ToolResponse(result=result)
        
        except Exception as e:
            raise ToolExecutionException(f"CSV processing failed: {str(e)}")
    
    async def _get_dataframe(self, request: ToolRequest) -> pd.DataFrame:
        """Gets a pandas DataFrame from either CSV data or URL"""
        if "csvData" in request.parameters:
            csv_data = request.parameters.get("csvData")
            return pd.read_csv(io.StringIO(csv_data))
        elif "csvUrl" in request.parameters:
            csv_url = request.parameters.get("csvUrl")
            return pd.read_csv(csv_url)
        else:
            raise ToolExecutionException("Either csvData or csvUrl must be provided")
    
    def _generate_summary(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Generates a summary of the CSV data"""
        return {
            "columns": df.columns.tolist(),
            "rowCount": len(df),
            "columnCount": len(df.columns),
            "numericColumns": df.select_dtypes(include=['number']).columns.tolist(),
            "categoricalColumns": df.select_dtypes(include=['object']).columns.tolist(),
            "sampleRows": json.loads(df.head(5).to_json(orient="records")),
            "statistics": json.loads(df.describe().to_json())
        }
    
    def _filter_data(self, df: pd.DataFrame, column: str, value: str) -> Dict[str, Any]:
        """Filters the DataFrame by a column value"""
        if column not in df.columns:
            raise ToolExecutionException(f"Column '{column}' not found")
            
        filtered_df = df[df[column].astype(str).str.contains(value)]
        
        return {
            "originalRowCount": len(df),
            "filteredRowCount": len(filtered_df),
            "data": json.loads(filtered_df.to_json(orient="records"))
        }
    
    def _transform_data(self, df: pd.DataFrame, params: Dict[str, Any]) -> Dict[str, Any]:
        """Transforms the data based on parameters"""
        # 实现将包括各种转换
        return {
            "status": "success",
            "message": "Transformation applied"
        }
    
    def _convert_format(self, df: pd.DataFrame, format: str) -> Dict[str, Any]:
        """Converts the DataFrame to different formats"""
        if format == "json":
            return {
                "data": json.loads(df.to_json(orient="records")),
                "format": "json"
            }
        elif format == "csv":
            return {
                "data": df.to_csv(index=False),
                "format": "csv"
            }
        elif format == "markdown":
            return {
                "data": df.to_markdown(),
                "format": "markdown"
            }
        else:
            raise ToolExecutionException(f"Unsupported output format: {format}")
```

### 贡献指南

成功为 MCP 项目贡献：

1. <strong>从小处做起</strong>：从文档、Bug 修复或小改进开始
2. <strong>遵循风格指南</strong>：遵守项目的编码风格和规范
3. <strong>编写测试</strong>：为您的代码贡献包含单元测试
4. <strong>文档说明</strong>：为新功能或更改添加清晰文档
5. **提交专注的 PR**：拉取请求集中于单一问题或功能
6. <strong>积极反馈互动</strong>：及时回应对贡献的反馈

### 贡献工作流程示例

```bash
# 克隆仓库
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# 为你的贡献创建一个新分支
git checkout -b feature/my-contribution

# 进行你的更改
# ...

# 运行测试以确保你的更改不会破坏现有功能
npm test

# 使用描述性信息提交你的更改
git commit -am "Fix validation in resource handler"

# 将你的分支推送到你的分叉仓库
git push origin feature/my-contribution

# 从你的分支创建一个拉取请求到主仓库
# 然后根据反馈进行交流并根据需要迭代你的拉取请求
```

## 创建与分享 MCP 服务器

向 MCP 生态系统贡献的最有价值方式之一是创建并分享自定义 MCP 服务器。社区已开发数百个用于各种服务和用例的服务器。

### MCP 服务器开发框架

有若干框架可简化 MCP 服务器开发：

1. **官方 SDK**（请查阅
    [SDK 文档](https://modelcontextprotocol.io/docs/sdk)了解每个
    SDK 支持的协议版本）：
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
   - [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
   - [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk)

2. <strong>社区框架</strong>：
   - [MCP-Framework](https://mcp-framework.com/) - 以优雅和高效方式用 TypeScript 构建 MCP 服务器
   - [MCP 声明式 Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - 基于注解的 Java MCP 服务器
   - [Quarkus MCP 服务器 SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java MCP 服务器框架
   - [Next.js MCP 服务器模板](https://github.com/vercel-labs/mcp-for-next.js) - MCP 服务器的 Next.js 入门项目

### 开发可共享工具

#### .NET 示例：创建可共享的工具包

```csharp
// Create a new .NET library project
// dotnet new classlib -n McpFinanceTools

using Microsoft.Mcp.Tools;
using System.Threading.Tasks;
using System.Net.Http;
using System.Text.Json;

namespace McpFinanceTools
{
    // Stock quote tool
    public class StockQuoteTool : IMcpTool
    {
        private readonly HttpClient _httpClient;
        
        public StockQuoteTool(HttpClient httpClient = null)
        {
            _httpClient = httpClient ?? new HttpClient();
        }
        
        public string Name => "stockQuote";
        public string Description => "Gets current stock quotes for specified symbols";
        
        public object GetSchema()
        {
            return new {
                type = "object",
                properties = new {
                    symbol = new { 
                        type = "string",
                        description = "Stock symbol (e.g., MSFT, AAPL)" 
                    },
                    includeHistory = new { 
                        type = "boolean",
                        description = "Whether to include historical data",
                        default = false
                    }
                },
                required = new[] { "symbol" }
            };
        }
        
        public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
        {
            // Extract parameters
            string symbol = request.Parameters.GetProperty("symbol").GetString();
            bool includeHistory = false;
            
            if (request.Parameters.TryGetProperty("includeHistory", out var historyProp))
            {
                includeHistory = historyProp.GetBoolean();
            }
            
            // Call external API (example)
            var quoteResult = await GetStockQuoteAsync(symbol);
            
            // Add historical data if requested
            if (includeHistory)
            {
                var historyData = await GetStockHistoryAsync(symbol);
                quoteResult.Add("history", historyData);
            }
            
            // Return formatted result
            return new ToolResponse {
                Result = JsonSerializer.SerializeToElement(quoteResult)
            };
        }
        
        private async Task<Dictionary<string, object>> GetStockQuoteAsync(string symbol)
        {
            // Implementation would call a real stock API
            // This is a simplified example
            return new Dictionary<string, object>
            {
                ["symbol"] = symbol,
                ["price"] = 123.45,
                ["change"] = 2.5,
                ["percentChange"] = 1.2,
                ["lastUpdated"] = DateTime.UtcNow
            };
        }
        
        private async Task<object> GetStockHistoryAsync(string symbol)
        {
            // Implementation would get historical data
            // Simplified example
            return new[]
            {
                new { date = DateTime.Now.AddDays(-7).Date, price = 120.25 },
                new { date = DateTime.Now.AddDays(-6).Date, price = 122.50 },
                new { date = DateTime.Now.AddDays(-5).Date, price = 121.75 }
                // More historical data...
            };
        }
    }
}

// Create package and publish to NuGet
// dotnet pack -c Release
// dotnet nuget push bin/Release/McpFinanceTools.1.0.0.nupkg -s https://api.nuget.org/v3/index.json -k YOUR_API_KEY
```

#### Java 示例：为工具创建 Maven 包

```java
// 用于可共享MCP工具包的pom.xml配置
<!-- 
<project>
    <groupId>com.example</groupId>
    <artifactId>mcp-weather-tools</artifactId>
    <version>1.0.0</version>
    
    <dependencies>
        <dependency>
            <groupId>com.mcp</groupId>
            <artifactId>mcp-server</artifactId>
            <version>1.0.0</version>
        </dependency>
    </dependencies>
    
    <distributionManagement>
        <repository>
            <id>github</id>
            <name>GitHub Packages</name>
            <url>https://maven.pkg.github.com/username/mcp-weather-tools</url>
        </repository>
    </distributionManagement>
</project>
-->

package com.example.mcp.weather;

import com.mcp.tools.Tool;
import com.mcp.tools.ToolRequest;
import com.mcp.tools.ToolResponse;
import com.mcp.tools.ToolExecutionException;

import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;
import java.util.HashMap;
import java.util.Map;

public class WeatherForecastTool implements Tool {
    private final HttpClient httpClient;
    private final String apiKey;
    
    public WeatherForecastTool(String apiKey) {
        this.httpClient = HttpClient.newHttpClient();
        this.apiKey = apiKey;
    }
    
    @Override
    public String getName() {
        return "weatherForecast";
    }
    
    @Override
    public String getDescription() {
        return "Gets weather forecast for a specified location";
    }
    
    @Override
    public Object getSchema() {
        Map<String, Object> schema = new HashMap<>();
        // 模式定义...
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            String location = request.getParameters().get("location").asText();
            int days = request.getParameters().has("days") ? 
                request.getParameters().get("days").asInt() : 3;
            
            // 调用天气API
            Map<String, Object> forecast = getForecast(location, days);
            
            // 构建响应
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // 实现将调用天气API
        // 简化示例
        Map<String, Object> result = new HashMap<>();
        // 添加预测数据...
        return result;
    }
}

// 使用Maven构建并发布
// mvn clean package
// mvn deploy
```

#### Python 示例：发布 PyPI 包

```python
# PyPI包的目录结构：
# mcp_nlp_tools/
# ├── LICENSE
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# 示例setup.py
"""
from setuptools import setup, find_packages

setup(
    name="mcp_nlp_tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "mcp_server>=1.0.0",
        "transformers>=4.0.0",
        "torch>=1.8.0"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="MCP tools for natural language processing tasks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/mcp_nlp_tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
"""

# 示例NLP工具实现（sentiment_tool.py）
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # 加载情感分析模型
        self.sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)
    
    def get_name(self):
        return "sentimentAnalysis"
        
    def get_description(self):
        return "Analyzes the sentiment of text, classifying it as positive or negative"
    
    def get_schema(self):
        return {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string", 
                    "description": "The text to analyze for sentiment"
                },
                "includeScore": {
                    "type": "boolean",
                    "description": "Whether to include confidence scores",
                    "default": True
                }
            },
            "required": ["text"]
        }
    
    async def execute_async(self, request: ToolRequest) -> ToolResponse:
        try:
            # 提取参数
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # 分析情感
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # 格式化结果
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # 返回结果
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# 发布步骤：
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### 分享最佳实践

分享 MCP 工具给社区时：

1. <strong>完善文档</strong>：
   - 记录目的、用法和示例
   - 解释参数和返回值
   - 记录任何外部依赖

2. <strong>错误处理</strong>：
   - 实现稳健的错误处理
   - 提供有用的错误信息
   - 优雅处理边缘情况

3. <strong>性能考虑</strong>：
   - 优化速度和资源使用
   - 适时实现缓存
   - 考虑可扩展性

4. <strong>安全性</strong>：
   - 使用安全的 API 密钥和认证
   - 验证和消毒输入
   - 实现外部 API 调用的速率限制

5. <strong>测试</strong>：
   - 包含全面测试覆盖
   - 测试不同输入类型和边缘情况
   - 记录测试流程

## 社区协作和最佳实践

有效协作是 MCP 繁荣生态系统的关键。

### 通信渠道

- GitHub Issues 和讨论
- Microsoft 技术社区
- Discord 和 Slack 频道
- Stack Overflow（标签：`model-context-protocol` 或 `mcp`）

### 代码审查

评审 MCP 贡献时：

1. <strong>清晰性</strong>：代码是否清晰且有良好文档？
2. <strong>正确性</strong>：是否按预期工作？
3. <strong>一致性</strong>：是否遵循项目规范？
4. <strong>完整性</strong>：包含测试和文档了吗？
5. <strong>安全性</strong>：是否存在安全隐患？

### 版本兼容性

开发 MCP 时：

1. <strong>协议版本控制</strong>：遵循工具支持的 MCP 协议版本
2. <strong>客户端兼容性</strong>：考虑向后兼容
3. <strong>服务器兼容性</strong>：遵循服务器实现指南
4. <strong>破坏性变更</strong>：清楚文档说明任何重大变更

## 社区示例项目：MCP 工具注册中心

重要的社区贡献之一是开发公用的 MCP 工具注册中心。

```python
# 社区工具注册表API的示例架构

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# 工具注册表的模型
class ToolSchema(BaseModel):
    """JSON Schema for a tool"""
    type: str
    properties: dict
    required: List[str] = []

class ToolRegistration(BaseModel):
    """Information for registering a tool"""
    name: str = Field(..., description="Unique name for the tool")
    description: str = Field(..., description="Description of what the tool does")
    version: str = Field(..., description="Semantic version of the tool")
    schema: ToolSchema = Field(..., description="JSON Schema for tool parameters")
    author: str = Field(..., description="Author of the tool")
    repository: Optional[HttpUrl] = Field(None, description="Repository URL")
    documentation: Optional[HttpUrl] = Field(None, description="Documentation URL")
    package: Optional[HttpUrl] = Field(None, description="Package URL")
    tags: List[str] = Field(default_factory=list, description="Tags for categorization")
    examples: List[dict] = Field(default_factory=list, description="Example usage")

class Tool(ToolRegistration):
    """Tool with registry metadata"""
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    downloads: int = Field(default=0)
    rating: float = Field(default=0.0)
    ratings_count: int = Field(default=0)

# 注册表的FastAPI应用
app = FastAPI(title="MCP Tool Registry")

# 此示例的内存数据库
tools_db = {}

@app.post("/tools", response_model=Tool)
async def register_tool(tool: ToolRegistration):
    """Register a new tool in the registry"""
    if tool.name in tools_db:
        raise HTTPException(status_code=400, detail=f"Tool '{tool.name}' already exists")
    
    new_tool = Tool(**tool.dict())
    tools_db[tool.name] = new_tool
    return new_tool

@app.get("/tools", response_model=List[Tool])
async def list_tools(tag: Optional[str] = None):
    """List all registered tools, optionally filtered by tag"""
    if tag:
        return [tool for tool in tools_db.values() if tag in tool.tags]
    return list(tools_db.values())

@app.get("/tools/{tool_name}", response_model=Tool)
async def get_tool(tool_name: str):
    """Get information about a specific tool"""
    if tool_name not in tools_db:
        raise HTTPException(status_code=404, detail=f"Tool '{tool_name}' not found")
    return tools_db[tool_name]

@app.delete("/tools/{tool_name}")
async def delete_tool(tool_name: str):
    """Delete a tool from the registry"""
    if tool_name not in tools_db:
        raise HTTPException(status_code=404, detail=f"Tool '{tool_name}' not found")
    del tools_db[tool_name]
    return {"message": f"Tool '{tool_name}' deleted"}
```

## 主要收获

- MCP 社区多元化，欢迎多种贡献形式
- 贡献内容涵盖核心协议增强到自定义工具开发
- 遵守贡献指南能提高拉取请求被接受的可能性
- 创建并分享 MCP 工具是提升生态系统的宝贵途径
- 社区协作是 MCP 成长与改进的关键

## 练习

1. 根据技能和兴趣，确定您能为 MCP 生态系统贡献的领域
2. Fork MCP 代码库并设置本地开发环境
3. 创建小型改进、Bug 修复或有益社区的工具
4. 使用适当的测试和文档记录您的贡献
5. 向相应代码库提交拉取请求

## 额外资源

- [MCP 社区项目](https://github.com/topics/model-context-protocol)

---

## 接下来

接下来：[早期采纳的经验教训](../07-LessonsfromEarlyAdoption/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->