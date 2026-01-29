# Общност и приноси

[![Как да допринесете за MCP: инструменти, документация, код и други](../../../translated_images/bg/07.1179f6de46ff196eb3cc13c3510e01c37807a13f3bb9be3c779105ce26737c67.png)](https://youtu.be/v1pvCYAWpRE)

_(Кликнете върху изображението по-горе, за да гледате видеото на този урок)_

## Преглед

Този урок се фокусира върху това как да се ангажирате с общността на MCP, да допринасяте за екосистемата на MCP и да следвате най-добрите практики за съвместна разработка. Разбирането как да участвате в проекти с отворен код на MCP е от съществено значение за тези, които искат да оформят бъдещето на тази технология.

## Цели на обучението

До края на този урок ще можете:

- Да разбирате структурата на общността и екосистемата на MCP
- Да участвате ефективно във форуми и дискусии на общността на MCP
- Да допринасяте за хранилищата с отворен код на MCP
- Да създавате и споделяте персонализирани инструменти и сървъри за MCP
- Да следвате най-добрите практики за разработка и сътрудничество в MCP
- Да откривате ресурси и рамки на общността за разработка на MCP

## Екосистемата на общността на MCP

Екосистемата на MCP се състои от различни компоненти и участници, които работят заедно за напредъка на протокола.

### Основни компоненти на общността

1. **Поддържащи основния протокол**: Официалната [Model Context Protocol GitHub организация](https://github.com/modelcontextprotocol) поддържа основните спецификации и референтни реализации на MCP.
2. **Разработчици на инструменти**: Индивиди и екипи, които създават инструменти и сървъри за MCP.
3. **Доставчици на интеграции**: Компании, които интегрират MCP в своите продукти и услуги.
4. **Крайни потребители**: Разработчици и организации, които използват MCP в своите приложения.
5. **Приносители**: Членове на общността, които допринасят с код, документация или други ресурси.

### Ресурси на общността

#### Официални канали

- [MCP GitHub организация](https://github.com/modelcontextprotocol)
- [MCP документация](https://modelcontextprotocol.io/)
- [MCP спецификация](https://modelcontextprotocol.io/docs/specification)
- [GitHub дискусии](https://github.com/orgs/modelcontextprotocol/discussions)
- [Хранилище за примери и сървъри на MCP](https://github.com/modelcontextprotocol/servers)

#### Ресурси, управлявани от общността

- [MCP клиенти](https://modelcontextprotocol.io/clients) - Списък с клиенти, които поддържат интеграции с MCP.
- [Сървъри на общността за MCP](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Нарастващ списък с разработени от общността сървъри за MCP.
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Курирани списъци със сървъри за MCP.
- [PulseMCP](https://www.pulsemcp.com/) - Център и бюлетин на общността за откриване на ресурси за MCP.
- [Discord сървър](https://discord.gg/jHEGxQu2a5) - Свържете се с разработчици на MCP.
- SDK реализации за специфични езици.
- Блог публикации и уроци.

## Принос към MCP

### Видове приноси

Екосистемата на MCP приветства различни видове приноси:

1. **Приноси в кода**:
   - Подобрения на основния протокол
   - Поправки на грешки
   - Реализации на инструменти и сървъри
   - Библиотеки за клиенти/сървъри на различни езици

2. **Документация**:
   - Подобряване на съществуващата документация
   - Създаване на уроци и ръководства
   - Превод на документация
   - Създаване на примери и примерни приложения

3. **Подкрепа на общността**:
   - Отговаряне на въпроси във форуми и дискусии
   - Тестване и докладване на проблеми
   - Организиране на събития на общността
   - Менторство на нови приносители

### Процес на принос: Основен протокол

За да допринесете към основния MCP протокол или официалните реализации, следвайте тези принципи от [официалните насоки за принос](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Простота и минимализъм**: Спецификацията на MCP поддържа високи стандарти за добавяне на нови концепции. По-лесно е да се добавят неща към спецификацията, отколкото да се премахнат.
2. **Конкретен подход**: Промените в спецификацията трябва да се основават на конкретни предизвикателства при реализация, а не на спекулативни идеи.
3. **Етапи на предложение**:
   - Дефиниране: Изследвайте пространството на проблема, валидирайте, че други потребители на MCP срещат подобен проблем.
   - Прототип: Създайте примерно решение и демонстрирайте неговото практическо приложение.
   - Написване: Въз основа на прототипа, напишете предложение за спецификация.

### Настройка на среда за разработка

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

### Пример: Принос за поправка на грешка

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

### Пример: Принос за нов инструмент към стандартната библиотека

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

### Насоки за принос

За да направите успешен принос към проекти на MCP:

1. **Започнете с малко**: Започнете с документация, поправки на грешки или малки подобрения.
2. **Следвайте ръководството за стил**: Придържайте се към стила и конвенциите на проекта.
3. **Напишете тестове**: Включете модулни тестове за вашите приноси в кода.
4. **Документирайте работата си**: Добавете ясна документация за нови функции или промени.
5. **Изпращайте целенасочени PRs**: Дръжте pull request-ите фокусирани върху един проблем или функция.
6. **Ангажирайте се с обратна връзка**: Бъдете отзивчиви към обратната връзка за вашите приноси.

### Примерен работен процес за принос

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

## Създаване и споделяне на сървъри за MCP

Един от най-ценните начини за принос към екосистемата на MCP е чрез създаване и споделяне на персонализирани сървъри за MCP. Общността вече е разработила стотици сървъри за различни услуги и случаи на употреба.

### Рамки за разработка на сървъри за MCP

Няколко рамки са налични за опростяване на разработката на сървъри за MCP:

1. **Официални SDKs**:
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Рамки на общността**:
   - [MCP-Framework](https://mcp-framework.com/) - Създавайте сървъри за MCP с елегантност и бързина в TypeScript.
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - MCP сървъри, управлявани чрез анотации в Java.
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java рамка за сървъри за MCP.
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Стартов проект за Next.js за сървъри за MCP.

### Разработване на споделяеми инструменти

#### Пример за .NET: Създаване на пакет с инструменти за споделяне

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

#### Пример за Java: Създаване на Maven пакет за инструменти

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

#### Пример за Python: Публикуване на пакет в PyPI

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

### Споделяне на най-добри практики

Когато споделяте инструменти за MCP с общността:

1. **Пълна документация**:
   - Документирайте целта, употребата и примерите.
   - Обяснете параметрите и стойностите на връщане.
   - Документирайте всички външни зависимости.

2. **Обработка на грешки**:
   - Реализирайте надеждна обработка на грешки.
   - Осигурете полезни съобщения за грешки.
   - Обработвайте гранични случаи внимателно.

3. **Съображения за производителност**:
   - Оптимизирайте както за скорост, така и за използване на ресурси.
   - Реализирайте кеширане, когато е подходящо.
   - Вземете предвид мащабируемостта.

4. **Сигурност**:
   - Използвайте сигурни API ключове и автентикация.
   - Валидирайте и пречиствайте входните данни.
   - Реализирайте ограничаване на скоростта за външни API повиквания.

5. **Тестване**:
   - Включете обширно покритие на тестовете.
   - Тествайте с различни типове входни данни и гранични случаи.
   - Документирайте процедурите за тестване.

## Сътрудничество в общността и най-добри практики

Ефективното сътрудничество е ключът към процъфтяваща екосистема на MCP.

### Канали за комуникация

- GitHub Issues и дискусии
- Microsoft Tech Community
- Discord и Slack канали
- Stack Overflow (таг: `model-context-protocol` или `mcp`)

### Прегледи на код

Когато преглеждате приноси към MCP:

1. **Яснота**: Дали кодът е ясен и добре документиран?
2. **Коректност**: Работи ли както се очаква?
3. **Последователност**: Следва ли конвенциите на проекта?
4. **Пълнота**: Включени ли са тестове и документация?
5. **Сигурност**: Има ли някакви проблеми със сигурността?

### Съвместимост на версиите

Когато разработвате за MCP:

1. **Версиониране на протокола**: Придържайте се към версията на MCP протокола, която вашият инструмент поддържа.
2. **Съвместимост с клиенти**: Вземете предвид обратната съвместимост.
3. **Съвместимост със сървъри**: Следвайте насоките за реализация на сървъри.
4. **Промени, нарушаващи съвместимостта**: Ясно документирайте всякакви промени, които нарушават съвместимостта.

## Примерен проект на общността: Регистър на инструменти за MCP

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

## Основни изводи

- Общността на MCP е разнообразна и приветства различни видове приноси.
- Приносът към MCP може да варира от подобрения на основния протокол до персонализирани инструменти.
- Следването на насоките за принос увеличава шансовете вашият PR да бъде приет.
- Създаването и споделянето на инструменти за MCP е ценен начин за подобряване на екосистемата.
- Сътрудничеството в общността е от съществено значение за растежа и подобрението на MCP.

## Упражнение

1. Идентифицирайте област в екосистемата на MCP, където можете да направите принос въз основа на вашите умения и интереси.
2. Форкнете хранилището на MCP и настройте локална среда за разработка.
3. Създайте малко подобрение, поправка на грешка или инструмент, който би бил полезен за общността.
4. Документирайте вашия принос с подходящи тестове и документация.
5. Изпратете pull request към съответното хранилище.

## Допълнителни ресурси

- [Проекти на общността за MCP](https://github.com/topics/model-context-protocol)

---

Следва: [Уроци от ранното приемане](../07-LessonsfromEarlyAdoption/README.md)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.