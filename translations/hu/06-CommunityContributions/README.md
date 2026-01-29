# Közösség és hozzájárulások

[![Hogyan járulhatsz hozzá az MCP-hez: eszközök, dokumentáció, kód és egyebek](../../../translated_images/hu/07.1179f6de46ff196eb3cc13c3510e01c37807a13f3bb9be3c779105ce26737c67.png)](https://youtu.be/v1pvCYAWpRE)

_(Kattints a fenti képre a videó megtekintéséhez)_

## Áttekintés

Ez a lecke arra összpontosít, hogyan kapcsolódhatsz be az MCP közösségébe, hogyan járulhatsz hozzá az MCP ökoszisztémához, és hogyan követheted a legjobb gyakorlatokat a közös fejlesztés során. Az MCP nyílt forráskódú projektjeiben való részvétel megértése elengedhetetlen azok számára, akik formálni szeretnék ennek a technológiának a jövőjét.

## Tanulási célok

A lecke végére képes leszel:

- Megérteni az MCP közösség és ökoszisztéma felépítését
- Hatékonyan részt venni az MCP közösségi fórumokon és vitákban
- Hozzájárulni az MCP nyílt forráskódú tárolóihoz
- Egyedi MCP eszközöket és szervereket létrehozni és megosztani
- Követni az MCP fejlesztés és együttműködés legjobb gyakorlatait
- Felfedezni közösségi erőforrásokat és keretrendszereket az MCP fejlesztéshez

## Az MCP közösségi ökoszisztéma

Az MCP ökoszisztéma különböző összetevőkből és résztvevőkből áll, amelyek együtt dolgoznak a protokoll fejlesztésén.

### Kulcsfontosságú közösségi összetevők

1. **Alapvető protokoll karbantartók**: Az [Model Context Protocol GitHub szervezet](https://github.com/modelcontextprotocol) tartja karban az MCP specifikációkat és referenciaimplementációkat.
2. **Eszközfejlesztők**: Egyének és csapatok, akik MCP eszközöket és szervereket hoznak létre.
3. **Integrációs szolgáltatók**: Vállalatok, amelyek MCP-t integrálnak termékeikbe és szolgáltatásaikba.
4. **Végfelhasználók**: Fejlesztők és szervezetek, akik MCP-t használnak alkalmazásaikban.
5. **Hozzájárulók**: Közösségi tagok, akik kódot, dokumentációt vagy egyéb erőforrásokat adnak hozzá.

### Közösségi erőforrások

#### Hivatalos csatornák

- [MCP GitHub szervezet](https://github.com/modelcontextprotocol)
- [MCP dokumentáció](https://modelcontextprotocol.io/)
- [MCP specifikáció](https://modelcontextprotocol.io/docs/specification)
- [GitHub viták](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP példák és szerverek tárolója](https://github.com/modelcontextprotocol/servers)

#### Közösség által létrehozott erőforrások

- [MCP kliensek](https://modelcontextprotocol.io/clients) - MCP integrációkat támogató kliensek listája
- [Közösségi MCP szerverek](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Közösség által fejlesztett MCP szerverek növekvő listája
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Válogatott MCP szerverek listája
- [PulseMCP](https://www.pulsemcp.com/) - Közösségi központ és hírlevél MCP erőforrások felfedezéséhez
- [Discord szerver](https://discord.gg/jHEGxQu2a5) - Kapcsolódj MCP fejlesztőkhöz
- Nyelvspecifikus SDK implementációk
- Blogbejegyzések és oktatóanyagok

## Hozzájárulás az MCP-hez

### Hozzájárulások típusai

Az MCP ökoszisztéma különböző típusú hozzájárulásokat fogad:

1. **Kódhozzájárulások**:
   - Alapvető protokoll fejlesztések
   - Hibajavítások
   - Eszköz- és szerverimplementációk
   - Kliens/szerver könyvtárak különböző nyelveken

2. **Dokumentáció**:
   - Meglévő dokumentáció javítása
   - Oktatóanyagok és útmutatók készítése
   - Dokumentáció fordítása
   - Példák és mintaprogramok létrehozása

3. **Közösségi támogatás**:
   - Kérdések megválaszolása fórumokon és vitákban
   - Hibák tesztelése és jelentése
   - Közösségi események szervezése
   - Új hozzájárulók mentorálása

### Hozzájárulási folyamat: Alapvető protokoll

Az MCP alapvető protokolljához vagy hivatalos implementációihoz való hozzájáruláshoz kövesd az [hivatalos hozzájárulási irányelvek](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md) alapelveit:

1. **Egyszerűség és minimalizmus**: Az MCP specifikáció magas szintet tart fenn az új fogalmak hozzáadásához. Könnyebb dolgokat hozzáadni egy specifikációhoz, mint eltávolítani őket.

2. **Konkrét megközelítés**: A specifikáció változtatásainak konkrét implementációs kihívásokon kell alapulniuk, nem spekulatív ötleteken.

3. **Javaslat szakaszai**:
   - Meghatározás: Fedezd fel a probléma területét, és igazold, hogy más MCP felhasználók is hasonló problémával szembesülnek.
   - Prototípus: Építs egy példamegoldást, és mutasd be annak gyakorlati alkalmazását.
   - Írás: A prototípus alapján írj egy specifikációs javaslatot.

### Fejlesztési környezet beállítása

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

### Példa: Hibajavítás hozzájárulása

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

### Példa: Új eszköz hozzáadása a standard könyvtárhoz

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

### Hozzájárulási irányelvek

Az MCP projektekhez való sikeres hozzájáruláshoz:

1. **Kezdj kicsiben**: Kezdd dokumentációval, hibajavításokkal vagy kisebb fejlesztésekkel.
2. **Kövesd a stílusirányelveket**: Tartsd be a projekt kódolási stílusát és konvencióit.
3. **Írj teszteket**: Adj hozzá egységteszteket a kódhozzájárulásaidhoz.
4. **Dokumentáld a munkádat**: Adj hozzá egyértelmű dokumentációt az új funkciókhoz vagy változtatásokhoz.
5. **Célzott PR-eket küldj**: Tartsd a pull requesteket egyetlen problémára vagy funkcióra fókuszálva.
6. **Reagálj a visszajelzésekre**: Légy nyitott a hozzájárulásaidra érkező visszajelzésekre.

### Példa hozzájárulási munkafolyamat

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

## MCP szerverek létrehozása és megosztása

Az MCP ökoszisztéma egyik legértékesebb hozzájárulási módja egyedi MCP szerverek létrehozása és megosztása. A közösség már több száz szervert fejlesztett különböző szolgáltatásokhoz és felhasználási esetekhez.

### MCP szerverfejlesztési keretrendszerek

Számos keretrendszer áll rendelkezésre az MCP szerverfejlesztés egyszerűsítésére:

1. **Hivatalos SDK-k**:
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Közösségi keretrendszerek**:
   - [MCP-Framework](https://mcp-framework.com/) - MCP szerverek gyors és elegáns fejlesztése TypeScriptben
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Annotáció-alapú MCP szerverek Java nyelven
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java keretrendszer MCP szerverekhez
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Indító Next.js projekt MCP szerverekhez

### Megosztható eszközök fejlesztése

#### .NET példa: Megosztható eszközcsomag létrehozása

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

#### Java példa: Maven csomag létrehozása eszközökhöz

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

#### Python példa: PyPI csomag közzététele

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

### Legjobb gyakorlatok megosztása

Amikor MCP eszközöket osztasz meg a közösséggel:

1. **Teljes dokumentáció**:
   - Dokumentáld a célt, használatot és példákat.
   - Magyarázd el a paramétereket és visszatérési értékeket.
   - Dokumentáld az esetleges külső függőségeket.

2. **Hibakezelés**:
   - Valósíts meg robusztus hibakezelést.
   - Adj hasznos hibaüzeneteket.
   - Kezeld az edge case-eket megfelelően.

3. **Teljesítmény szempontok**:
   - Optimalizáld a sebességet és az erőforrás-használatot.
   - Valósíts meg gyorsítótárazást, ha szükséges.
   - Gondolj a skálázhatóságra.

4. **Biztonság**:
   - Használj biztonságos API kulcsokat és hitelesítést.
   - Validáld és tisztítsd meg a bemeneteket.
   - Valósíts meg sebességkorlátozást külső API hívásokhoz.

5. **Tesztelés**:
   - Adj hozzá átfogó tesztlefedettséget.
   - Tesztelj különböző bemenettípusokkal és edge case-ekkel.
   - Dokumentáld a tesztelési eljárásokat.

## Közösségi együttműködés és legjobb gyakorlatok

A hatékony együttműködés kulcsfontosságú az MCP ökoszisztéma virágzásához.

### Kommunikációs csatornák

- GitHub hibajegyek és viták
- Microsoft Tech Community
- Discord és Slack csatornák
- Stack Overflow (címkék: `model-context-protocol` vagy `mcp`)

### Kódellenőrzések

MCP hozzájárulások ellenőrzésekor:

1. **Érthetőség**: Világos és jól dokumentált a kód?
2. **Helyesség**: Úgy működik, ahogy elvárható?
3. **Konzisztencia**: Követi a projekt konvencióit?
4. **Teljesség**: Tartalmaz teszteket és dokumentációt?
5. **Biztonság**: Van-e bármilyen biztonsági aggály?

### Verziókompatibilitás

MCP fejlesztésekor:

1. **Protokoll verziózás**: Tartsd be az MCP protokoll verzióját, amelyet az eszközöd támogat.
2. **Kliens kompatibilitás**: Gondolj a visszafelé kompatibilitásra.
3. **Szerver kompatibilitás**: Kövesd a szerver implementációs irányelveket.
4. **Breaking változások**: Dokumentáld egyértelműen a breaking változásokat.

## Példa közösségi projekt: MCP eszközregiszter

Egy fontos közösségi hozzájárulás lehet egy nyilvános MCP eszközregiszter fejlesztése.

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

## Kulcsfontosságú tanulságok

- Az MCP közösség sokszínű, és különböző típusú hozzájárulásokat fogad.
- Az MCP-hez való hozzájárulás kiterjedhet az alapvető protokoll fejlesztésektől az egyedi eszközökig.
- A hozzájárulási irányelvek követése növeli az esélyét annak, hogy a PR-t elfogadják.
- MCP eszközök létrehozása és megosztása értékes módja az ökoszisztéma fejlesztésének.
- A közösségi együttműködés elengedhetetlen az MCP növekedéséhez és fejlesztéséhez.

## Gyakorlat

1. Azonosíts egy területet az MCP ökoszisztémában, ahol a képességeid és érdeklődési köröd alapján hozzájárulhatsz.
2. Forkold az MCP tárolót, és állítsd be a helyi fejlesztési környezetet.
3. Hozz létre egy kisebb fejlesztést, hibajavítást vagy eszközt, amely hasznos lehet a közösség számára.
4. Dokumentáld a hozzájárulásodat megfelelő tesztekkel és dokumentációval.
5. Küldj be egy pull requestet a megfelelő tárolóba.

## További erőforrások

- [MCP közösségi projektek](https://github.com/topics/model-context-protocol)

---

Következő: [Korai alkalmazás tanulságai](../07-LessonsfromEarlyAdoption/README.md)

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.