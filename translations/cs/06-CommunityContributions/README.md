# Komunita a příspěvky

[![Jak přispět do MCP: nástroje, dokumentace, kód a další](../../../translated_images/cs/07.1179f6de46ff196eb3cc13c3510e01c37807a13f3bb9be3c779105ce26737c67.png)](https://youtu.be/v1pvCYAWpRE)

_(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

## Přehled

Tato lekce se zaměřuje na to, jak se zapojit do komunity MCP, přispívat do ekosystému MCP a dodržovat osvědčené postupy pro spolupráci při vývoji. Porozumění tomu, jak se zapojit do open-source projektů MCP, je klíčové pro ty, kteří chtějí formovat budoucnost této technologie.

## Cíle učení

Na konci této lekce budete schopni:

- Porozumět struktuře komunity a ekosystému MCP
- Efektivně se zapojit do fór a diskusí komunity MCP
- Přispívat do open-source repozitářů MCP
- Vytvářet a sdílet vlastní nástroje a servery MCP
- Dodržovat osvědčené postupy pro vývoj a spolupráci v MCP
- Objevovat komunitní zdroje a rámce pro vývoj MCP

## Ekosystém komunity MCP

Ekosystém MCP se skládá z různých komponent a účastníků, kteří společně pracují na rozvoji protokolu.

### Klíčové komponenty komunity

1. **Správci jádra protokolu**: Oficiální [GitHub organizace Model Context Protocol](https://github.com/modelcontextprotocol) spravuje hlavní specifikace MCP a referenční implementace.
2. **Vývojáři nástrojů**: Jednotlivci a týmy, které vytvářejí nástroje a servery MCP.
3. **Poskytovatelé integrací**: Společnosti, které integrují MCP do svých produktů a služeb.
4. **Koncoví uživatelé**: Vývojáři a organizace, které používají MCP ve svých aplikacích.
5. **Přispěvatelé**: Členové komunity, kteří přispívají kódem, dokumentací nebo jinými zdroji.

### Zdroje komunity

#### Oficiální kanály

- [GitHub organizace MCP](https://github.com/modelcontextprotocol)
- [Dokumentace MCP](https://modelcontextprotocol.io/)
- [Specifikace MCP](https://modelcontextprotocol.io/docs/specification)
- [Diskuse na GitHubu](https://github.com/orgs/modelcontextprotocol/discussions)
- [Repozitář příkladů a serverů MCP](https://github.com/modelcontextprotocol/servers)

#### Zdroje řízené komunitou

- [Klienti MCP](https://modelcontextprotocol.io/clients) - Seznam klientů podporujících integrace MCP
- [Komunitní servery MCP](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Rostoucí seznam serverů vyvinutých komunitou
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Kurátorovaný seznam serverů MCP
- [PulseMCP](https://www.pulsemcp.com/) - Komunitní centrum a newsletter pro objevování zdrojů MCP
- [Discord server](https://discord.gg/jHEGxQu2a5) - Spojte se s vývojáři MCP
- SDK implementace pro konkrétní jazyky
- Blogové příspěvky a návody

## Přispívání do MCP

### Typy příspěvků

Ekosystém MCP vítá různé typy příspěvků:

1. **Příspěvky ke kódu**:
   - Vylepšení jádra protokolu
   - Opravy chyb
   - Implementace nástrojů a serverů
   - Knihovny klient/server v různých jazycích

2. **Dokumentace**:
   - Zlepšování stávající dokumentace
   - Vytváření návodů a průvodců
   - Překlady dokumentace
   - Vytváření příkladů a ukázkových aplikací

3. **Podpora komunity**:
   - Odpovídání na otázky na fórech a v diskusích
   - Testování a hlášení problémů
   - Organizace komunitních akcí
   - Mentorování nových přispěvatelů

### Proces přispívání: Jádro protokolu

Chcete-li přispět do jádra protokolu MCP nebo oficiálních implementací, postupujte podle těchto zásad z [oficiálních pokynů pro přispívání](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Jednoduchost a minimalismus**: Specifikace MCP udržuje vysokou laťku pro přidávání nových konceptů. Je snazší něco do specifikace přidat než odstranit.
2. **Konkrétní přístup**: Změny ve specifikaci by měly vycházet z konkrétních implementačních výzev, nikoli ze spekulativních nápadů.
3. **Fáze návrhu**:
   - Definice: Prozkoumejte problémovou oblast, ověřte, že ostatní uživatelé MCP čelí podobnému problému.
   - Prototyp: Vytvořte ukázkové řešení a demonstrujte jeho praktické použití.
   - Návrh: Na základě prototypu napište návrh specifikace.

### Nastavení vývojového prostředí

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

### Příklad: Přispění opravy chyby

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

### Příklad: Přidání nového nástroje do standardní knihovny

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

### Pokyny pro přispívání

Chcete-li úspěšně přispět do projektů MCP:

1. **Začněte v malém**: Začněte s dokumentací, opravami chyb nebo malými vylepšeními.
2. **Dodržujte stylový průvodce**: Držte se stylu a konvencí projektu.
3. **Pište testy**: Přidejte jednotkové testy ke svým příspěvkům.
4. **Dokumentujte svou práci**: Přidejte jasnou dokumentaci k novým funkcím nebo změnám.
5. **Odesílejte cílené PR**: Udržujte pull requesty zaměřené na jeden problém nebo funkci.
6. **Reagujte na zpětnou vazbu**: Buďte otevření zpětné vazbě na své příspěvky.

### Ukázkový pracovní postup přispívání

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

## Vytváření a sdílení serverů MCP

Jedním z nejcennějších způsobů, jak přispět do ekosystému MCP, je vytváření a sdílení vlastních serverů MCP. Komunita již vyvinula stovky serverů pro různé služby a případy použití.

### Rámce pro vývoj serverů MCP

K dispozici je několik rámců, které usnadňují vývoj serverů MCP:

1. **Oficiální SDK**:
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Komunitní rámce**:
   - [MCP-Framework](https://mcp-framework.com/) - Rychlý a elegantní vývoj serverů MCP v TypeScriptu.
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - MCP servery řízené anotacemi v Javě.
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java rámec pro servery MCP.
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Startovací projekt Next.js pro servery MCP.

### Vývoj sdílených nástrojů

#### Příklad v .NET: Vytvoření sdíleného balíčku nástrojů

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

#### Příklad v Javě: Vytvoření Maven balíčku pro nástroje

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

#### Příklad v Pythonu: Publikace balíčku na PyPI

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

### Sdílení osvědčených postupů

Při sdílení nástrojů MCP s komunitou:

1. **Kompletní dokumentace**:
   - Dokumentujte účel, použití a příklady.
   - Vysvětlete parametry a návratové hodnoty.
   - Dokumentujte externí závislosti.

2. **Zpracování chyb**:
   - Implementujte robustní zpracování chyb.
   - Poskytujte užitečné chybové zprávy.
   - Elegantně řešte okrajové případy.

3. **Výkonnostní úvahy**:
   - Optimalizujte pro rychlost i využití zdrojů.
   - Implementujte caching, pokud je to vhodné.
   - Zvažte škálovatelnost.

4. **Bezpečnost**:
   - Používejte bezpečné API klíče a autentizaci.
   - Validujte a čistěte vstupy.
   - Implementujte omezení rychlosti pro externí API volání.

5. **Testování**:
   - Zahrňte komplexní pokrytí testy.
   - Testujte s různými typy vstupů a okrajovými případy.
   - Dokumentujte postupy testování.

## Spolupráce v komunitě a osvědčené postupy

Efektivní spolupráce je klíčem k prosperujícímu ekosystému MCP.

### Komunikační kanály

- GitHub Issues a Diskuse
- Microsoft Tech Community
- Discord a Slack kanály
- Stack Overflow (tagy: `model-context-protocol` nebo `mcp`)

### Recenze kódu

Při recenzování příspěvků MCP:

1. **Srozumitelnost**: Je kód jasný a dobře zdokumentovaný?
2. **Správnost**: Funguje podle očekávání?
3. **Konzistence**: Dodržuje konvence projektu?
4. **Kompletnost**: Jsou zahrnuty testy a dokumentace?
5. **Bezpečnost**: Existují nějaké bezpečnostní obavy?

### Kompatibilita verzí

Při vývoji pro MCP:

1. **Verzování protokolu**: Dodržujte verzi protokolu MCP, kterou váš nástroj podporuje.
2. **Kompatibilita klienta**: Zvažte zpětnou kompatibilitu.
3. **Kompatibilita serveru**: Dodržujte pokyny pro implementaci serveru.
4. **Změny narušující kompatibilitu**: Jasně dokumentujte jakékoli změny narušující kompatibilitu.

## Ukázkový komunitní projekt: Registr nástrojů MCP

Důležitým komunitním příspěvkem by mohlo být vytvoření veřejného registru nástrojů MCP.

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

## Klíčové poznatky

- Komunita MCP je rozmanitá a vítá různé typy příspěvků.
- Přispívání do MCP může zahrnovat vylepšení jádra protokolu i vlastní nástroje.
- Dodržování pokynů pro přispívání zvyšuje šanci na přijetí vašeho PR.
- Vytváření a sdílení nástrojů MCP je cenný způsob, jak rozšířit ekosystém.
- Spolupráce v komunitě je zásadní pro růst a zlepšování MCP.

## Cvičení

1. Identifikujte oblast v ekosystému MCP, kde byste mohli přispět na základě svých dovedností a zájmů.
2. Forkněte repozitář MCP a nastavte si lokální vývojové prostředí.
3. Vytvořte malé vylepšení, opravu chyby nebo nástroj, který by komunitě prospěl.
4. Zdokumentujte svůj příspěvek s odpovídajícími testy a dokumentací.
5. Odesílejte pull request do příslušného repozitáře.

## Další zdroje

- [Komunitní projekty MCP](https://github.com/topics/model-context-protocol)

---

Další: [Lekce z raného přijetí](../07-LessonsfromEarlyAdoption/README.md)

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.