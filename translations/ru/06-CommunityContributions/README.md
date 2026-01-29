# Сообщество и вклад

[![Как внести вклад в MCP: инструменты, документация, код и многое другое](../../../translated_images/ru/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

## Обзор

Этот урок посвящен тому, как взаимодействовать с сообществом MCP, вносить вклад в экосистему MCP и следовать лучшим практикам совместной разработки. Понимание того, как участвовать в проектах с открытым исходным кодом MCP, важно для тех, кто хочет формировать будущее этой технологии.

## Цели обучения

К концу этого урока вы сможете:

- Понять структуру сообщества и экосистемы MCP
- Эффективно участвовать в форумах и обсуждениях сообщества MCP
- Вносить вклад в репозитории с открытым исходным кодом MCP
- Создавать и делиться пользовательскими инструментами и серверами MCP
- Следовать лучшим практикам разработки и сотрудничества MCP
- Открывать ресурсы и фреймворки сообщества для разработки MCP

## Экосистема сообщества MCP

Экосистема MCP состоит из различных компонентов и участников, которые работают вместе для развития протокола.

### Основные компоненты сообщества

1. **Поддерживающие основной протокол**: Официальная [Model Context Protocol GitHub организация](https://github.com/modelcontextprotocol) поддерживает основные спецификации MCP и эталонные реализации.
2. **Разработчики инструментов**: Индивидуальные разработчики и команды, создающие инструменты и серверы MCP.
3. **Поставщики интеграций**: Компании, которые интегрируют MCP в свои продукты и услуги.
4. **Конечные пользователи**: Разработчики и организации, использующие MCP в своих приложениях.
5. **Участники**: Члены сообщества, которые вносят код, документацию или другие ресурсы.

### Ресурсы сообщества

#### Официальные каналы

- [MCP GitHub организация](https://github.com/modelcontextprotocol)
- [Документация MCP](https://modelcontextprotocol.io/)
- [Спецификация MCP](https://modelcontextprotocol.io/docs/specification)
- [Обсуждения на GitHub](https://github.com/orgs/modelcontextprotocol/discussions)
- [Репозиторий примеров и серверов MCP](https://github.com/modelcontextprotocol/servers)

#### Ресурсы, созданные сообществом

- [Клиенты MCP](https://modelcontextprotocol.io/clients) - Список клиентов, поддерживающих интеграции MCP.
- [Серверы MCP сообщества](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Растущий список серверов MCP, разработанных сообществом.
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Кураторский список серверов MCP.
- [PulseMCP](https://www.pulsemcp.com/) - Центр сообщества и рассылка для поиска ресурсов MCP.
- [Discord сервер](https://discord.gg/jHEGxQu2a5) - Связь с разработчиками MCP.
- Реализации SDK для различных языков.
- Блог-посты и учебные материалы.

## Внесение вклада в MCP

### Типы вкладов

Экосистема MCP приветствует различные типы вкладов:

1. **Код**:
   - Улучшения основного протокола
   - Исправление ошибок
   - Реализация инструментов и серверов
   - Библиотеки клиентов/серверов на разных языках

2. **Документация**:
   - Улучшение существующей документации
   - Создание учебных материалов и руководств
   - Перевод документации
   - Создание примеров и демонстрационных приложений

3. **Поддержка сообщества**:
   - Ответы на вопросы на форумах и в обсуждениях
   - Тестирование и сообщение об ошибках
   - Организация мероприятий сообщества
   - Наставничество для новых участников

### Процесс внесения вклада: основной протокол

Чтобы внести вклад в основной протокол MCP или официальные реализации, следуйте этим принципам из [официальных рекомендаций по внесению вклада](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Простота и минимализм**: Спецификация MCP придерживается высокого стандарта для добавления новых концепций. Добавить что-то в спецификацию проще, чем удалить.
2. **Конкретный подход**: Изменения в спецификации должны основываться на конкретных проблемах реализации, а не на гипотетических идеях.
3. **Этапы предложения**:
   - Определение: Исследуйте проблему, убедитесь, что другие пользователи MCP сталкиваются с аналогичной проблемой.
   - Прототип: Создайте пример решения и продемонстрируйте его практическое применение.
   - Написание: На основе прототипа напишите предложение по спецификации.

### Настройка среды разработки

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

### Пример: внесение исправления ошибки

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

### Пример: добавление нового инструмента в стандартную библиотеку

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

### Рекомендации по внесению вклада

Чтобы ваш вклад в проекты MCP был успешным:

1. **Начинайте с малого**: Начните с документации, исправления ошибок или небольших улучшений.
2. **Следуйте стилю проекта**: Соблюдайте стиль кодирования и соглашения проекта.
3. **Пишите тесты**: Включайте модульные тесты для ваших вкладов в код.
4. **Документируйте вашу работу**: Добавляйте четкую документацию для новых функций или изменений.
5. **Отправляйте целевые PR**: Сосредоточьтесь на одной проблеме или функции в каждом pull request.
6. **Реагируйте на обратную связь**: Будьте готовы к отзывам о ваших вкладах.

### Пример рабочего процесса внесения вклада

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

## Создание и распространение серверов MCP

Одним из самых ценных способов внести вклад в экосистему MCP является создание и распространение пользовательских серверов MCP. Сообщество уже разработало сотни серверов для различных сервисов и случаев использования.

### Фреймворки для разработки серверов MCP

Существует несколько фреймворков, упрощающих разработку серверов MCP:

1. **Официальные SDK**:
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Фреймворки сообщества**:
   - [MCP-Framework](https://mcp-framework.com/) - Создание серверов MCP с элегантностью и скоростью на TypeScript.
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Серверы MCP на основе аннотаций в Java.
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java-фреймворк для серверов MCP.
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Стартовый проект Next.js для серверов MCP.

### Разработка инструментов для общего использования

#### Пример .NET: создание пакета инструментов для общего использования

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

#### Пример Java: создание Maven-пакета для инструментов

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

#### Пример Python: публикация пакета на PyPI

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

### Рекомендации по распространению

При распространении инструментов MCP в сообществе:

1. **Полная документация**:
   - Опишите цель, использование и примеры.
   - Объясните параметры и возвращаемые значения.
   - Документируйте внешние зависимости.

2. **Обработка ошибок**:
   - Реализуйте надежную обработку ошибок.
   - Предоставляйте полезные сообщения об ошибках.
   - Аккуратно обрабатывайте крайние случаи.

3. **Производительность**:
   - Оптимизируйте скорость и использование ресурсов.
   - Реализуйте кэширование, если это уместно.
   - Учитывайте масштабируемость.

4. **Безопасность**:
   - Используйте безопасные ключи API и аутентификацию.
   - Проверяйте и очищайте входные данные.
   - Реализуйте ограничение скорости для внешних API-запросов.

5. **Тестирование**:
   - Включайте полное покрытие тестами.
   - Тестируйте с различными типами входных данных и крайними случаями.
   - Документируйте процедуры тестирования.

## Сотрудничество в сообществе и лучшие практики

Эффективное сотрудничество — ключ к процветанию экосистемы MCP.

### Каналы связи

- Проблемы и обсуждения на GitHub
- Microsoft Tech Community
- Каналы Discord и Slack
- Stack Overflow (теги: `model-context-protocol` или `mcp`)

### Рецензирование кода

При рецензировании вкладов в MCP:

1. **Ясность**: Является ли код понятным и хорошо документированным?
2. **Корректность**: Работает ли он так, как ожидается?
3. **Последовательность**: Соответствует ли он соглашениям проекта?
4. **Полнота**: Включены ли тесты и документация?
5. **Безопасность**: Есть ли какие-либо проблемы с безопасностью?

### Совместимость версий

При разработке для MCP:

1. **Версионирование протокола**: Соблюдайте версию MCP, которую поддерживает ваш инструмент.
2. **Совместимость клиентов**: Учитывайте обратную совместимость.
3. **Совместимость серверов**: Следуйте рекомендациям по реализации серверов.
4. **Критические изменения**: Четко документируйте любые критические изменения.

## Пример проекта сообщества: реестр инструментов MCP

Важным вкладом сообщества может стать разработка публичного реестра инструментов MCP.

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

## Основные выводы

- Сообщество MCP разнообразно и приветствует различные типы вкладов.
- Внесение вклада в MCP может включать улучшения основного протокола и создание пользовательских инструментов.
- Следование рекомендациям по внесению вклада увеличивает шансы на принятие вашего PR.
- Создание и распространение инструментов MCP — ценный способ улучшить экосистему.
- Сотрудничество в сообществе важно для роста и улучшения MCP.

## Упражнение

1. Определите область в экосистеме MCP, где вы могли бы внести вклад, исходя из ваших навыков и интересов.
2. Форкните репозиторий MCP и настройте локальную среду разработки.
3. Создайте небольшое улучшение, исправление ошибки или инструмент, который будет полезен сообществу.
4. Задокументируйте ваш вклад, добавив тесты и документацию.
5. Отправьте pull request в соответствующий репозиторий.

## Дополнительные ресурсы

- [Проекты сообщества MCP](https://github.com/topics/model-context-protocol)

---

Далее: [Уроки раннего внедрения](../07-LessonsfromEarlyAdoption/README.md)

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.