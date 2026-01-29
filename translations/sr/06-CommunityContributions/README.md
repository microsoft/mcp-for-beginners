# Заједница и доприноси

[![Како допринети MCP-у: Алатке, документација, код и више](../../../translated_images/sr/07.1179f6de46ff196eb3cc13c3510e01c37807a13f3bb9be3c779105ce26737c67.png)](https://youtu.be/v1pvCYAWpRE)

_(Кликните на слику изнад да бисте погледали видео овог часа)_

## Преглед

Овај час се фокусира на то како се укључити у MCP заједницу, допринети MCP екосистему и пратити најбоље праксе за колаборативни развој. Разумевање како учествовати у отвореним MCP пројектима је кључно за оне који желе да обликују будућност ове технологије.

## Циљеви учења

До краја овог часа, моћи ћете да:

- Разумете структуру MCP заједнице и екосистема
- Ефективно учествујете у MCP форумима и дискусијама
- Допринесете MCP отвореним репозиторијумима
- Креирате и делите прилагођене MCP алатке и сервере
- Пратите најбоље праксе за MCP развој и сарадњу
- Откријете ресурсе и оквире за MCP развој

## MCP екосистем заједнице

MCP екосистем се састоји од различитих компоненти и учесника који заједно раде на унапређењу протокола.

### Кључне компоненте заједнице

1. **Одржаваоци основног протокола**: Званична [Model Context Protocol GitHub организација](https://github.com/modelcontextprotocol) одржава основне MCP спецификације и референтне имплементације
2. **Развијачи алатки**: Појединци и тимови који креирају MCP алатке и сервере
3. **Пружаоци интеграција**: Компаније које интегришу MCP у своје производе и услуге
4. **Крајњи корисници**: Развијачи и организације које користе MCP у својим апликацијама
5. **Сарадници**: Чланови заједнице који доприносе кодом, документацијом или другим ресурсима

### Ресурси заједнице

#### Званични канали

- [MCP GitHub организација](https://github.com/modelcontextprotocol)
- [MCP документација](https://modelcontextprotocol.io/)
- [MCP спецификација](https://modelcontextprotocol.io/docs/specification)
- [GitHub дискусије](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP примери и репозиторијум сервера](https://github.com/modelcontextprotocol/servers)

#### Ресурси које води заједница

- [MCP клијенти](https://modelcontextprotocol.io/clients) - Листа клијената који подржавају MCP интеграције
- [Заједнички MCP сервери](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Растућа листа MCP сервера које је развила заједница
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Курирана листа MCP сервера
- [PulseMCP](https://www.pulsemcp.com/) - Центар заједнице и билтен за откривање MCP ресурса
- [Discord сервер](https://discord.gg/jHEGxQu2a5) - Повежите се са MCP развијачима
- SDK имплементације за специфичне језике
- Блогови и туторијали

## Допринос MCP-у

### Типови доприноса

MCP екосистем поздравља различите типове доприноса:

1. **Код доприноси**:
   - Унапређења основног протокола
   - Исправке грешака
   - Имплементације алатки и сервера
   - Клијентске/серверске библиотеке на различитим језицима

2. **Документација**:
   - Унапређење постојеће документације
   - Креирање туторијала и водича
   - Превођење документације
   - Креирање примера и узорних апликација

3. **Подршка заједници**:
   - Одговарање на питања на форумима и дискусијама
   - Тестирање и пријављивање проблема
   - Организовање догађаја заједнице
   - Менторисање нових сарадника

### Процес доприноса: Основни протокол

Да бисте допринели основном MCP протоколу или званичним имплементацијама, пратите ове принципе из [званичних смерница за допринос](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Једноставност и минимализам**: MCP спецификација одржава висок стандард за додавање нових концепата. Лакше је додати ствари у спецификацију него их уклонити.

2. **Конкретан приступ**: Промене у спецификацији треба да се заснивају на специфичним изазовима имплементације, а не на спекулативним идејама.

3. **Фазе предлога**:
   - Дефинисање: Истражите проблем, потврдите да и други MCP корисници имају сличан изазов
   - Прототип: Изградите пример решења и демонстрирајте његову практичну примену
   - Писање: На основу прототипа, напишите предлог спецификације

### Подешавање развојног окружења

```bash
# Fork the repository
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# Install dependencies
npm install

# For schema changes, validate and generate schema.json:
npm run check:schema:ts
npm run generate:schema

# For documentation changes
npm run check:docs
npm run format

# Preview documentation locally (optional):
npm run serve:docs
```

### Пример: Допринос исправци грешке

```javascript
// Original code with bug in the typescript-sdk
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Bug: Missing property validation
  // Current implementation:
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// Fixed implementation in a contribution
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Improved validation
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### Пример: Допринос нове алатке у стандардну библиотеку

```python
# Example contribution: A CSV data processing tool for the MCP standard library

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
            # Extract parameters
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # Get CSV data from either direct data or URL
            df = await self._get_dataframe(request)
            
            # Process based on requested operation
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
        # Implementation would include various transformations
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

### Смернице за допринос

Да бисте успешно допринели MCP пројектима:

1. **Почните са малим**: Почните са документацијом, исправкама грешака или малим унапређењима
2. **Пратите стилске смернице**: Придржавајте се стилских и кодних конвенција пројекта
3. **Пишите тестове**: Укључите јединичне тестове за своје кодне доприносе
4. **Документујте свој рад**: Додајте јасну документацију за нове функције или промене
5. **Поднесите циљане PR-ове**: Држите pull request-ове фокусиране на један проблем или функцију
6. **Одговорите на повратне информације**: Будите одзивни на повратне информације о својим доприносима

### Пример радног тока доприноса

```bash
# Clone the repository
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# Create a new branch for your contribution
git checkout -b feature/my-contribution

# Make your changes
# ...

# Run tests to ensure your changes don't break existing functionality
npm test

# Commit your changes with a descriptive message
git commit -am "Fix validation in resource handler"

# Push your branch to your fork
git push origin feature/my-contribution

# Create a pull request from your branch to the main repository
# Then engage with feedback and iterate on your PR as needed
```

## Креирање и дељење MCP сервера

Један од највреднијих начина да допринесете MCP екосистему је креирање и дељење прилагођених MCP сервера. Заједница је већ развила стотине сервера за различите услуге и случајеве употребе.

### MCP оквири за развој сервера

Неколико оквира је доступно за поједностављење развоја MCP сервера:

1. **Званични SDK-ови**:
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Оквири које води заједница**:
   - [MCP-Framework](https://mcp-framework.com/) - Изградите MCP сервере са елеганцијом и брзином у TypeScript-у
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - MCP сервери засновани на анотацијама у Java-и
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java оквир за MCP сервере
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Почетни Next.js пројекат за MCP сервере

### Развој алатки за дељење

#### .NET пример: Креирање пакета алатки за дељење

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

#### Java пример: Креирање Maven пакета за алатке

```java
// pom.xml configuration for a shareable MCP tool package
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
        // Schema definition...
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            String location = request.getParameters().get("location").asText();
            int days = request.getParameters().has("days") ? 
                request.getParameters().get("days").asInt() : 3;
            
            // Call weather API
            Map<String, Object> forecast = getForecast(location, days);
            
            // Build response
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // Implementation would call weather API
        // Simplified example
        Map<String, Object> result = new HashMap<>();
        // Add forecast data...
        return result;
    }
}

// Build and publish using Maven
// mvn clean package
// mvn deploy
```

#### Python пример: Објављивање PyPI пакета

```python
# Directory structure for a PyPI package:
# mcp_nlp_tools/
# ├── LICENSE
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# Example setup.py
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

# Example NLP tool implementation (sentiment_tool.py)
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # Load the sentiment analysis model
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
            # Extract parameters
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # Analyze sentiment
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # Format result
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # Return result
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# To publish:
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### Најбоље праксе за дељење

Када делите MCP алатке са заједницом:

1. **Комплетна документација**:
   - Документујте сврху, употребу и примере
   - Објасните параметре и повратне вредности
   - Документујте све спољне зависности

2. **Руковање грешкама**:
   - Имплементирајте робусно руковање грешкама
   - Обезбедите корисне поруке о грешкама
   - Грациозно обрадите граничне случајеве

3. **Перформансе**:
   - Оптимизујте за брзину и коришћење ресурса
   - Имплементирајте кеширање када је прикладно
   - Размотрите скалабилност

4. **Безбедност**:
   - Користите безбедне API кључеве и аутентификацију
   - Валидација и чишћење уноса
   - Имплементирајте ограничење брзине за спољне API позиве

5. **Тестирање**:
   - Укључите свеобухватно покривање тестовима
   - Тестирајте са различитим типовима уноса и граничним случајевима
   - Документујте процедуре тестирања

## Сарадња у заједници и најбоље праксе

Ефективна сарадња је кључна за напредак MCP екосистема.

### Канали комуникације

- GitHub Issues и дискусије
- Microsoft Tech Community
- Discord и Slack канали
- Stack Overflow (ознаке: `model-context-protocol` или `mcp`)

### Прегледи кода

Када прегледате MCP доприносе:

1. **Јасноћа**: Да ли је код јасан и добро документован?
2. **Тачност**: Да ли ради како је очекивано?
3. **Конзистентност**: Да ли прати конвенције пројекта?
4. **Комплетност**: Да ли су укључени тестови и документација?
5. **Безбедност**: Да ли постоје безбедносни проблеми?

### Верзиона компатибилност

Када развијате за MCP:

1. **Верзионисање протокола**: Придржавајте се верзије MCP протокола коју ваш алат подржава
2. **Клијентска компатибилност**: Размотрите уназад компатибилност
3. **Серверска компатибилност**: Пратите смернице за имплементацију сервера
4. **Промене које прекидају рад**: Јасно документујте све промене које прекидају рад

## Пример пројекта заједнице: MCP регистар алатки

```python
# Example schema for a community tool registry API

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# Models for the tool registry
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

# FastAPI application for the registry
app = FastAPI(title="MCP Tool Registry")

# In-memory database for this example
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

## Кључне поруке

- MCP заједница је разнолика и поздравља различите типове доприноса
- Доприношење MCP-у може обухватати унапређења основног протокола до прилагођених алатки
- Поштовање смерница за допринос повећава шансе да ваш PR буде прихваћен
- Креирање и дељење MCP алатки је вредан начин за унапређење екосистема
- Сарадња у заједници је суштинска за раст и унапређење MCP-а

## Вежба

1. Идентификујте област у MCP екосистему где можете допринети на основу својих вештина и интересовања
2. Fork-ујте MCP репозиторијум и подесите локално развојно окружење
3. Креирајте мало унапређење, исправку грешке или алатку која би користила заједници
4. Документујте свој допринос са одговарајућим тестовима и документацијом
5. Поднесите pull request у одговарајући репозиторијум

## Додатни ресурси

- [MCP пројекти заједнице](https://github.com/topics/model-context-protocol)

---

Следеће: [Лекције из раног усвајања](../07-LessonsfromEarlyAdoption/README.md)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на свом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква неспоразумевања или погрешна тумачења која могу произаћи из коришћења овог превода.