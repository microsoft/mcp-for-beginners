# Спільнота та внески

[![Як робити внески в MCP: Інструменти, Документація, Код та інше](../../../translated_images/uk/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

## Огляд

Цей урок зосереджений на тому, як взаємодіяти зі спільнотою MCP, вносити свій внесок в екосистему MCP та дотримуватися найкращих практик спільної розробки. Розуміння того, як брати участь у відкритих проектах MCP, є важливим для тих, хто хоче формувати майбутнє цієї технології.

## Цілі навчання

До кінця цього уроку ви зможете:

- Розуміти структуру спільноти та екосистеми MCP
- Ефективно брати участь у форумах та обговореннях спільноти MCP
- Вносити внесок у відкриті репозиторії MCP
- Створювати та ділитися користувацькими інструментами й серверами MCP
- Дотримуватися найкращих практик розробки та співпраці MCP
- Знаходити ресурси спільноти та фреймворки для розробки MCP

## Екосистема спільноти MCP

Екосистема MCP складається з різних компонентів і учасників, які спільно працюють над розвитком протоколу.

### Ключові компоненти спільноти

1. **Основні підтримувачі протоколу**: офіційна [організація Model Context Protocol на GitHub](https://github.com/modelcontextprotocol) підтримує основні специфікації MCP та референтні реалізації
2. **Розробники інструментів**: окремі особи та команди, які створюють інструменти та сервери MCP
3. **Постачальники інтеграції**: компанії, які інтегрують MCP у свої продукти та послуги
4. **Кінцеві користувачі**: розробники та організації, які використовують MCP у своїх додатках
5. **Внесники**: учасники спільноти, які вносять код, документацію чи інші ресурси

### Ресурси спільноти

#### Офіційні канали

- [Організація MCP на GitHub](https://github.com/modelcontextprotocol)
- [Документація MCP](https://modelcontextprotocol.io/)
- [Специфікація MCP](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Обговорення на GitHub](https://github.com/orgs/modelcontextprotocol/discussions)
- [Репозиторій прикладів і серверів MCP](https://github.com/modelcontextprotocol/servers)

#### Ресурси, створені спільнотою

- [Клієнти MCP](https://modelcontextprotocol.io/clients) - список клієнтів, які підтримують інтеграції MCP
- [Сервери MCP від спільноти](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - зростаючий список серверів MCP, розроблених спільнотою
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - кураторський список MCP серверів
- [PulseMCP](https://www.pulsemcp.com/) - спільнотне хаб та розсилка для відкриття ресурсів MCP
- [Remote OpenClaw](https://www.remoteopenclaw.com/) - безкоштовний пошуковий каталог серверів MCP, навичок агентів та плагінів
- [Discord сервер](https://discord.gg/jHEGxQu2a5) - зв’язок із розробниками MCP
- SDK імплементації для різних мов
- Блоги та навчальні матеріали

## Внесок у MCP

### Види внесків

Екосистема MCP вітає різні типи внесків:

1. **Код**:
   - Покращення основного протоколу
   - Виправлення помилок
   - Реалізації інструментів і серверів
   - Бібліотеки клієнтів/серверів для різних мов

2. **Документація**:
   - Покращення існуючої документації
   - Створення посібників і керівництв
   - Переклади документації
   - Створення прикладів та демонстраційних додатків

3. **Підтримка спільноти**:
   - Відповіді на запитання на форумах і в обговореннях
   - Тестування та звітування про проблеми
   - Організація подій спільноти
   - Наставництво новим внесникам

### Процес внеску: Основний протокол

Щоб внести свій внесок у основний протокол MCP або офіційні реалізації, дотримуйтеся принципів з [офіційних вказівок для внесків](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Простота та мінімалізм**: Специфікація MCP ставить високі вимоги до додавання нових концепцій. Додати щось у специфікацію легше, ніж видалити.

2. **Конкретний підхід**: Зміни у специфікації мають базуватися на конкретних проблемах реалізації, а не на спекулятивних ідеях.

3. **Етапи пропозиції**:
   - Визначення: дослідити проблему, перевірити, що інші користувачі MCP мають схожу проблему
   - Прототипування: створити приклад рішення та продемонструвати його практичне застосування
   - Написання: на основі прототипу написати пропозицію до специфікації

### Налаштування середовища розробки

```bash
# Форкнути репозиторій
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# Встановити залежності
npm install

# Для змін у схемі, перевірте та згенеруйте schema.json:
npm run check:schema:ts
npm run generate:schema

# Для змін у документації
npm run check:docs
npm run format

# Попередній перегляд документації локально (за бажанням):
npm run serve:docs
```

### Приклад: внесок виправлення помилки

```javascript
// Початковий код із помилкою в typescript-sdk
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Помилка: відсутня перевірка властивостей
  // Поточна реалізація:
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// Виправлена реалізація в сприянні
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Покращена перевірка
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### Приклад: внесок нового інструменту до стандартної бібліотеки

```python
# Приклад внеску: Інструмент обробки CSV даних для стандартної бібліотеки MCP

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
            # Витяг параметрів
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # Отримати CSV дані або з безпосередніх даних, або з URL
            df = await self._get_dataframe(request)
            
            # Обробка на основі запитаної операції
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
        # Реалізація включатиме різні трансформації
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

### Керівництво для внесків

Щоб зробити успішний внесок у MCP проекти:

1. **Починайте з малого**: почніть з документації, виправлення помилок або невеликих покращень
2. **Дотримуйтеся стилю коду**: слідуйте стилю коду та конвенціям проекту
3. **Пишіть тести**: додавайте юніт-тести для своїх внесків коду
4. **Документуйте вашу роботу**: додавайте чітку документацію для нових функцій або змін
5. **Подавайте цільові pull-запити**: тримайте запити на злиття сфокусованими на одній проблемі чи функції
6. **Взаємодійте з відгуками**: будьте відкритими до фідбеку щодо своїх внесків

### Приклад робочого процесу внеску

```bash
# Клонувати репозиторій
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# Створити нову гілку для вашого внеску
git checkout -b feature/my-contribution

# Внести свої зміни
# ...

# Запустити тести, щоб переконатися, що ваші зміни не порушують існуючу функціональність
npm test

# Зафіксувати зміни з описовим повідомленням
git commit -am "Fix validation in resource handler"

# Відправити вашу гілку до форку
git push origin feature/my-contribution

# Створити пулл-реквест з вашої гілки до основного репозиторію
# Потім врахувати відгуки і за потреби повторно працювати над вашим PR
```

## Створення та поширення серверів MCP

Один із найцінніших способів зробити внесок у екосистему MCP — створювати та ділитися користувацькими серверами MCP. Спільнота вже розробила сотні серверів для різних сервісів та випадків використання.

### Фреймворки для розробки серверів MCP

Існує кілька фреймворків, які спрощують розробку серверів MCP:

1. **Офіційні SDK** (див. 
    [документацію SDK](https://modelcontextprotocol.io/docs/sdk) для кожної
    підтримуваної версії протоколу):
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
   - [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
   - [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk)

2. **Фреймворки спільноти**:
   - [MCP-Framework](https://mcp-framework.com/) - створення серверів MCP з елегантністю та швидкістю на TypeScript
   - [Декларативний Java SDK MCP](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - сервери MCP з анотаціями на Java
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java фреймворк для серверів MCP
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - стартовий проект Next.js для серверів MCP

### Розробка і поширення інструментів

#### Приклад .NET: створення пакету для спільного використання інструменту

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

#### Приклад Java: створення пакету Maven для інструментів

```java
// конфігурація pom.xml для пакету MCP інструментів, що можна спільно використовувати
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
        // Визначення схеми...
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            String location = request.getParameters().get("location").asText();
            int days = request.getParameters().has("days") ? 
                request.getParameters().get("days").asInt() : 3;
            
            // Виклик API погоди
            Map<String, Object> forecast = getForecast(location, days);
            
            // Формування відповіді
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // Реалізація викличе API погоди
        // Спрощений приклад
        Map<String, Object> result = new HashMap<>();
        // Додати дані прогнозу...
        return result;
    }
}

// Збірка та публікація за допомогою Maven
// mvn clean package
// mvn deploy
```

#### Приклад Python: публікація пакету PyPI

```python
# Структура каталогу для пакету PyPI:
# mcp_nlp_tools/
# ├── LICENSE
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# Приклад setup.py
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

# Приклад реалізації NLP інструменту (sentiment_tool.py)
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # Завантажити модель аналізу настроїв
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
            # Витягнути параметри
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # Проаналізувати настрій
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # Відформатувати результат
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # Повернути результат
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# Для публікації:
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### Поширення найкращих практик

Коли ви ділитеся інструментами MCP зі спільнотою:

1. **Повна документація**:
   - Документуйте призначення, використання та приклади
   - Пояснюйте параметри та значення, що повертаються
   - Документуйте зовнішні залежності

2. **Обробка помилок**:
   - Реалізуйте надійну обробку помилок
   - Надавайте корисні повідомлення про помилки
   - Коректно обробляйте крайні випадки

3. **Врахування продуктивності**:
   - Оптимізуйте як швидкість, так і використання ресурсів
   - Використовуйте кешування там, де це доцільно
   - Розглядайте масштабованість

4. **Безпека**:
   - Використовуйте безпечні ключі API та автентифікацію
   - Перевіряйте та очищайте вхідні дані
   - Реалізуйте обмеження частоти запитів до зовнішніх API

5. **Тестування**:
   - Забезпечуйте комплексне покриття тестами
   - Тестуйте з різними типами вхідних даних і крайніми випадками
   - Документуйте процедури тестування

## Співпраця в спільноті та найкращі практики

Ефективна співпраця є ключем до процвітання екосистеми MCP.

### Канали комунікації

- Питання та обговорення на GitHub
- Microsoft Tech Community
- Канали Discord та Slack
- Stack Overflow (теги: `model-context-protocol` або `mcp`)

### Перевірка коду

Під час перевірки внесків у MCP:

1. **Зрозумілість**: Чи є код зрозумілим і добре документованим?
2. **Коректність**: Чи працює він відповідно до очікувань?
3. **Послідовність**: Чи дотримується він конвенцій проекту?
4. **Повнота**: Чи включено тести та документацію?
5. **Безпека**: Чи не містить він проблем безпеки?

### Сумісність версій

Під час розробки для MCP:

1. **Версіонування протоколу**: дотримуйтесь версії протоколу MCP, яку підтримує ваш інструмент
2. **Сумісність з клієнтами**: враховуйте сумісність назад
3. **Сумісність з серверами**: дотримуйтесь вказівок щодо реалізації серверів
4. **Руйнівні зміни**: чітко документуйте всі зміни, що порушують сумісність

## Приклад спільнотного проекту: Реєстр інструментів MCP

Важливим внеском спільноти може бути розробка публічного реєстру для інструментів MCP.

```python
# Приклад схеми для API реєстру інструментів спільноти

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# Моделі для реєстру інструментів
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

# Додаток FastAPI для реєстру
app = FastAPI(title="MCP Tool Registry")

# База даних у пам’яті для цього прикладу
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

## Основні висновки

- Спільнота MCP є різноманітною і вітає різні типи внесків
- Внесок у MCP може охоплювати від покращень основного протоколу до користувацьких інструментів
- Дотримання керівництва для внесків підвищує шанси на прийняття вашого PR
- Створення та поширення інструментів MCP є цінним способом розширення екосистеми
- Співпраця в спільноті є суттєвою для зростання та вдосконалення MCP

## Вправа

1. Визначте область в екосистемі MCP, у якій ви могли б зробити внесок, базуючись на своїх навичках і інтересах
2. Форкніть репозиторій MCP і налаштуйте локальне середовище розробки
3. Створіть невелике покращення, виправлення помилки або інструмент, що принесе користь спільноті
4. Задокументуйте ваш внесок із відповідними тестами та документацією
5. Подайте pull-запит у відповідний репозиторій

## Додаткові ресурси

- [Проекти спільноти MCP](https://github.com/topics/model-context-protocol)

---

## Що далі

Далі: [Уроки з раннього впровадження](../07-LessonsfromEarlyAdoption/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->