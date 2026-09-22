# Общност и Приноси

[![Как да допринесете за MCP: Инструменти, Документация, Код и Още](../../../translated_images/bg/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Кликнете на горната снимка, за да гледате видеото на този урок)_

## Преглед

Този урок се фокусира върху това как да се включите в общността на MCP, да допринасяте за екосистемата на MCP и да следвате най-добрите практики за съвместна разработка. Разбирането как да участвате в проекти с отворен код на MCP е от съществено значение за тези, които искат да формират бъдещето на тази технология.

## Учебни цели

В края на този урок ще можете да:

- Разберете структурата на общността и екосистемата на MCP
- Участвате ефективно в MCP форуми и дискусии на общността
- Допринесете в отворени хранилища на MCP
- Създавате и споделяте персонализирани инструменти и сървъри за MCP
- Следвате най-добрите практики за разработка и сътрудничество в MCP
- Откривате ресурси и рамки на общността за разработка на MCP

## Екосистемата на общността на MCP

Екосистемата на MCP се състои от различни компоненти и участници, които работят заедно да развиват протокола.

### Ключови компоненти на общността

1. **Основни поддръжници на протокола**: Официалната [GitHub организация Model Context Protocol](https://github.com/modelcontextprotocol) поддържа основните спецификации на MCP и референтните реализации
2. **Разработчици на инструменти**: Индивиди и екипи, които създават инструменти и сървъри за MCP
3. **Доставчици на интеграция**: Компании, които интегрират MCP в своите продукти и услуги
4. **Крайни потребители**: Разработчици и организации, които използват MCP в своите приложения
5. **Приносители**: Членове на общността, които допринасят с код, документация или други ресурси

### Ресурси на общността

#### Официални канали

- [MCP GitHub организация](https://github.com/modelcontextprotocol)
- [Документация на MCP](https://modelcontextprotocol.io/)
- [Спецификация на MCP](https://modelcontextprotocol.io/specification/2026-07-28/)
- [GitHub дискусии](https://github.com/orgs/modelcontextprotocol/discussions)
- [Хранилище с примери и сървъри на MCP](https://github.com/modelcontextprotocol/servers)

#### Ресурси, водени от общността

- [MCP клиенти](https://modelcontextprotocol.io/clients) - Списък с клиенти, които поддържат интеграции на MCP
- [Общностни MCP сървъри](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Разрастващ се списък с MCP сървъри, разработени от общността
- [Уау MCP сървъри](https://github.com/wong2/awesome-mcp-servers) - Курираният списък на MCP сървъри
- [PulseMCP](https://www.pulsemcp.com/) - Хъб и бюлетин на общността за откриване на MCP ресурси
- [Remote OpenClaw](https://www.remoteopenclaw.com/) - Безплатен търсещ се указател на MCP сървъри, умения на агенти и приставки
- [Discord сървър](https://discord.gg/jHEGxQu2a5) - Свържете се с разработчици на MCP
- SDK реализации за конкретни езици
- Постове в блогове и уроци

## Допринасяне за MCP

### Видове приноси

Екосистемата на MCP приветства различни видове приноси:

1. **Приноси с код**:
   - Подобрения основния протокол
   - Поправки на грешки
   - Имплементации на инструменти и сървъри
   - Клиентски/сървърни библиотеки на различни езици

2. **Документация**:
   - Подобряване на съществуващата документация
   - Създаване на уроци и наръчници
   - Превод на документация
   - Създаване на примери и демонстрационни приложения

3. **Подкрепа на общността**:
   - Отговаряне на въпроси в форуми и дискусии
   - Тестване и докладване на проблеми
   - Организиране на събития на общността
   - Наставничество на нови приноси

### Процес на принос: Основен протокол

За да допринесете за основния MCP протокол или официалните реализации, следвайте тези принципи от [официалните насоки за принос](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Оптималност и минимализъм**: Спецификацията на MCP поддържа висок стандарт при добавяне на нови концепции. По-лесно е да добавите неща, отколкото да ги премахнете.

2. **Конкретен подход**: Промените в спецификацията трябва да се основават на конкретни предизвикателства в реални реализации, а не на спекулативни идеи.

3. **Етапи на предложение**:
   - Дефиниране: Изследване на проблемното пространство, потвърждаване, че други MCP потребители имат подобен проблем
   - Прототипиране: Създаване на примерна реализация и демонстриране на практическа полза
   - Писане: На база на прототипа, написване на предложение за спецификация

### Настройка на средата за разработка

```bash
# Форкнете хранилището
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# Инсталирайте зависимостите
npm install

# За промени в схемата, валидирайте и генерирайте schema.json:
npm run check:schema:ts
npm run generate:schema

# За промени в документацията
npm run check:docs
npm run format

# Прегледайте документацията локално (по желание):
npm run serve:docs
```

### Пример: Допринесане на поправка на грешка

```javascript
// Оригинален код с грешка в typescript-sdk
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Грешка: Липсваща проверка на свойство
  // Текуща имплементация:
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// Поправена имплементация в приноса
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Подобрена проверка
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### Пример: Допринесане на нов инструмент към стандартната библиотека

```python
# Примерен принос: Инструмент за обработка на CSV данни за стандартната библиотека MCP

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
            # Извличане на параметри
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # Вземете CSV данни от директни данни или URL
            df = await self._get_dataframe(request)
            
            # Обработка въз основа на заявената операция
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
        # Имплементацията ще включва различни трансформации
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

За успешен принос към MCP проекти:

1. **Започнете малко**: Започнете с документация, поправки на грешки или малки подобрения
2. **Следвайте стиловия наръчник**: Спазвайте стиловете и конвенциите на проекта
3. **Пишете тестове**: Включете юнит тестове към кода си
4. **Документирайте работата си**: Добавяйте ясна документация за нови функции или промени
5. **Подавайте целенасочени pull заявки**: Поддържайте pull заявките фокусирани върху един проблем или функция
6. **Приемете обратна връзка**: Бъдете отзивчиви към мненията за приносите ви

### Примерен работен процес на принос

```bash
# Клонирайте хранилището
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# Създайте нов клон за вашия принос
git checkout -b feature/my-contribution

# Направете вашите промени
# ...

# Стартирайте тестове, за да сте сигурни, че промените ви не нарушават съществуващата функционалност
npm test

# Запишете промените си с описателно съобщение
git commit -am "Fix validation in resource handler"

# Издърпайте клона си към вашето форкване
git push origin feature/my-contribution

# Създайте заявка за изтегляне от вашия клон към основното хранилище
# След това се ангажирайте с обратна връзка и итерации по вашата заявка за изтегляне според нуждите
```

## Създаване и споделяне на MCP сървъри

Един от най-ценните начини да допринесете за екосистемата на MCP е чрез създаването и споделянето на персонализирани MCP сървъри. Общността вече е развила стотици сървъри за различни услуги и случаи на използване.

### Рамки за разработка на MCP сървъри

Няколко рамки са налични, за да улеснят разработката на MCP сървъри:

1. **Официални SDK-та** (проверете
    [документацията на SDK](https://modelcontextprotocol.io/docs/sdk) за поддържаните версии на протокола за всеки
    SDK):
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
   - [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
   - [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk)

2. **Рамки, водени от общността**:
   - [MCP-Framework](https://mcp-framework.com/) - Създавайте MCP сървъри с елегантност и бързина в TypeScript
   - [MCP Декларативен Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Антоационно ориентирани MCP сървъри с Java
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java рамка за MCP сървъри
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Стартов проект за MCP сървъри с Next.js

### Разработка на споделени инструменти

#### Пример на .NET: Създаване на споделяна пакетирана библиотека

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

#### Пример на Java: Създаване на Maven пакет за инструменти

```java
// конфигурация pom.xml за споделяем пакет с MCP инструменти
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
        // Дефиниция на схема...
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            String location = request.getParameters().get("location").asText();
            int days = request.getParameters().has("days") ? 
                request.getParameters().get("days").asInt() : 3;
            
            // Обадете се на API за времето
            Map<String, Object> forecast = getForecast(location, days);
            
            // Създаване на отговор
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // Имплементацията би извикала API за времето
        // Оптимизиран пример
        Map<String, Object> result = new HashMap<>();
        // Добавете прогнозни данни...
        return result;
    }
}

// Създаване и публикуване с Maven
// mvn clean package
// mvn deploy
```

#### Пример на Python: Публикуване на PyPI пакет

```python
# Структура на директорията за PyPI пакет:
# mcp_nlp_tools/
# ├── ЛИЦЕНЗ
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# Пример setup.py
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

# Примерна реализация на NLP инструмент (sentiment_tool.py)
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # Зареждане на модела за анализ на настроения
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
            # Извличане на параметри
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # Анализиране на настроението
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # Форматиране на резултата
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # Връщане на резултата
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# За публикуване:
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### Споделяне на най-добрите практики

При споделяне на MCP инструменти с общността:

1. **Пълна документация**:
   - Документирайте целта, употребата и примери
   - Обяснете параметрите и връщаните стойности
   - Документирайте всички външни зависимости

2. **Обработка на грешки**:
   - Реализирайте стабилна обработка на грешки
   - Предоставяйте полезни съобщения за грешки
   - Обработвайте гранични случаи елегантно

3. **Представяне на производителността**:
   - Оптимизирайте за бързина и използване на ресурси
   - Реализирайте кеширане при подходящи случаи
   - Обмислете мащабируемостта

4. **Сигурност**:
   - Използвайте сигурни API ключове и автентикация
   - Валидация и дезинфекция на входните данни
   - Ограничаване на скоростта при външни API повиквания

5. **Тестване**:
   - Включвайте изчерпателно тестово покритие
   - Тествайте с различни типове входни данни и гранични случаи
   - Документирайте тестовите процедури

## Сътрудничество в общността и най-добри практики

Ефективното сътрудничество е ключът към процъфтяваща екосистема на MCP.

### Канали за комуникация

- GitHub проблеми и дискусии
- Microsoft Tech Community
- Discord и Slack канали
- Stack Overflow (тег: `model-context-protocol` или `mcp`)

### Преглед на код

При преглед на приноси към MCP:

1. **Яснота**: Ясен и добре документиран ли е кодът?
2. **Правилност**: Работи ли кодът както се очаква?
3. **Последователност**: Спазва ли проектните конвенции?
4. **Пълнота**: Включени ли са тестове и документация?
5. **Сигурност**: Има ли някакви проблеми със сигурността?

### Съвместимост на версии

При разработка за MCP:

1. **Версиониране на протокола**: Спазвайте версията на MCP протокола, която вашият инструмент поддържа
2. **Съвместимост на клиента**: Обмислете обратно съвместимост
3. **Съвместимост на сървъра**: Следвайте насоките за имплементация на сървъра
4. **Промени, които нарушават съвместимостта**: Ясно документирайте такива промени

## Примерен проект на общността: Регистър на MCP инструменти

Важен принос в общността може да бъде разработването на публичен регистър за MCP инструменти.

```python
# Примерна схема за API на регистър за инструменти на общността

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# Модели за регистър на инструменти
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

# FastAPI приложение за регистъра
app = FastAPI(title="MCP Tool Registry")

# В паметта база данни за този пример
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

## Ключови изводи

- Общността на MCP е разнообразна и приветства различни видове приноси
- Приносите за MCP могат да варират от подобрения в основния протокол до персонализирани инструменти
- Следването на насоките за принос увеличава шанса PR заявките ви да бъдат приети
- Създаването и споделянето на MCP инструменти е ценен начин за подобряване на екосистемата
- Сътрудничеството в общността е необходимо за растежа и усъвършенстването на MCP

## Упражнение

1. Идентифицирайте област в екосистемата на MCP, в която можете да допринесете според уменията и интересите си
2. Форкнете MCP репозиторито и настройте локална среда за разработка
3. Създайте малко подобрение, поправка на грешка или инструмент, който би бил полезен за общността
4. Документирайте вашия принос с подходящи тестове и документация
5. Подайте pull заявка към съответното хранилище

## Допълнителни ресурси

- [Проекти на MCP общността](https://github.com/topics/model-context-protocol)

---

## Какво следва

Следва: [Уроци от ранното приемане](../07-LessonsfromEarlyAdoption/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->