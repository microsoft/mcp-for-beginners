# Közösség és Hozzájárulások

[![Hogyan járulj hozzá az MCP-hez: Eszközök, Dokumentáció, Kód és még sok más](../../../translated_images/hu/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Kattints a fenti képre a lecke videójának megtekintéséhez)_

## Áttekintés

Ez a lecke arra fókuszál, hogyan lehet bekapcsolódni az MCP közösségébe, hozzájárulni az MCP ökoszisztémához, és követni a legjobb gyakorlatokat az együttműködő fejlesztésben. Az MCP nyílt forráskódú projektjeiben való részvétel megértése alapvető azok számára, akik alakítani szeretnék ennek a technológiának a jövőjét.

## Tanulási Célok

A lecke végére képes leszel:

- Megérteni az MCP közösség és ökoszisztéma felépítését
- Hatékonyan részt venni az MCP közösségi fórumokon és vitákban
- Hozzájárulni az MCP nyílt forráskódú adattáraihoz
- Egyedi MCP eszközök és szerverek létrehozása és megosztása
- Követni az MCP fejlesztésére és együttműködésére vonatkozó legjobb gyakorlatokat
- Felfedezni közösségi forrásokat és keretrendszereket az MCP fejlesztéshez

## Az MCP Közösségi Ökoszisztéma

Az MCP ökoszisztéma különböző összetevőkből és résztvevőkből áll, akik együtt dolgoznak a protokoll előmozdításán.

### Fő Közösségi Összetevők

1. **Alapprotokoll Karbantartók**: Az hivatalos [Model Context Protocol GitHub szervezet](https://github.com/modelcontextprotocol) tartja karban az MCP alapvető specifikációit és referenciamegvalósításait
2. **Eszközfejlesztők**: Egyének és csapatok, akik MCP eszközöket és szervereket hoznak létre
3. **Integrációs Szolgáltatók**: Cégek, amelyek az MCP-t integrálják termékeikbe és szolgáltatásaikba
4. **Végfelhasználók**: Fejlesztők és szervezetek, akik MCP-t használnak alkalmazásaikban
5. **Hozzájárulók**: Közösségi tagok, akik kódot, dokumentációt vagy egyéb erőforrásokat biztosítanak

### Közösségi Források

#### Hivatalos Csatornák

- [MCP GitHub szervezet](https://github.com/modelcontextprotocol)
- [MCP Dokumentáció](https://modelcontextprotocol.io/)
- [MCP Specifikáció](https://modelcontextprotocol.io/specification/2026-07-28/)
- [GitHub Fórumok](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP Példák és Szerverek adattár](https://github.com/modelcontextprotocol/servers)

#### Közösségi Kezdeményezések

- [MCP Kliensek](https://modelcontextprotocol.io/clients) - MCP integrációkat támogató kliensek listája
- [Közösségi MCP szerverek](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Növekvő lista közösség által fejlesztett MCP szerverekről
- [Awesome MCP szerverek](https://github.com/wong2/awesome-mcp-servers) - Kurátori MCP szerverlista
- [PulseMCP](https://www.pulsemcp.com/) - Közösségi központ és hírlevél MCP források felfedezéséhez
- [Remote OpenClaw](https://www.remoteopenclaw.com/) - Ingyenes kereshető MCP szerverek, ügynöki képességek és pluginok könyvtára
- [Discord szerver](https://discord.gg/jHEGxQu2a5) - Kapcsolódj MCP fejlesztőkkel
- Nyelvspecifikus SDK implementációk
- Blogbejegyzések és oktatóanyagok

## Hozzájárulás az MCP-hez

### Hozzájárulás Típusai

Az MCP ökoszisztéma különféle hozzájárulásokat fogad:

1. **Kódhozzájárulások**:
   - Alapprotokoll fejlesztések
   - Hibajavítások
   - Eszköz- és szerverimplementációk
   - Kliens/szerver könyvtárak különféle nyelveken

2. **Dokumentáció**:
   - Meglévő dokumentáció javítása
   - Oktatóanyagok és útmutatók készítése
   - Dokumentációk fordítása
   - Példák és mintapéldák készítése

3. **Közösségi Támogatás**:
   - Kérdések megválaszolása fórumokon és vitákban
   - Tesztelés és hibajelentés
   - Közösségi események szervezése
   - Új hozzájárulók mentorálása

### Hozzájárulási Folyamat: Alapprotokoll

Az MCP alapprotokoll vagy hivatalos megvalósításokhoz való hozzájáruláshoz kövesd a [hivatalos hozzájárulási irányelveket](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Egyszerűség és Minimalizmus**: Az MCP specifikáció magas szintű követelményeket támaszt az új fogalmak hozzáadásakor. Könnyebb dolgokat hozzáadni egy specifikációhoz, mint eltávolítani őket.

2. **Konkretizált Megközelítés**: A specifikáció változtatásai konkrét megvalósítási kihívásokon kell alapuljanak, nem spekulatív elképzeléseken.

3. **Egy Javaslat Szakaszai**:
   - Meghatározás: Vizsgáld meg a problématerületet, ellenőrizd, hogy más MCP felhasználók hasonló problémával küzdenek
   - Prototípus: Készíts egy példamegoldást és mutasd be gyakorlati alkalmazását
   - Írás: A prototípus alapján írj specifikációs javaslatot

### Fejlesztői Környezet Beállítása

```bash
# Használd fel a tárhelyet
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# Telepítsd a függőségeket
npm install

# Sémaváltozások esetén ellenőrizd és generáld a schema.json fájlt:
npm run check:schema:ts
npm run generate:schema

# Dokumentációváltozások esetén
npm run check:docs
npm run format

# Dokumentáció helyi előnézete (opcionális):
npm run serve:docs
```

### Példa: Hibajavítás Hozzájárulása

```javascript
// Eredeti kód hibával a typescript-sdk-ben
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Hiba: Hiányzó tulajdonság ellenőrzés
  // Jelenlegi megvalósítás:
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// Javított megvalósítás egy hozzájárulásban
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Javított érvényesítés
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### Példa: Új Eszköz Hozzájárulása az Alapkönyvtárhoz

```python
# Példa hozzájárulás: Egy CSV adatfeldolgozó eszköz az MCP szabványkönyvtárhoz

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
            # Paraméterek kinyerése
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # CSV adat lekérése közvetlen adatból vagy URL-ből
            df = await self._get_dataframe(request)
            
            # Feldolgozás a kért művelet alapján
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
        # A megvalósítás különféle átalakításokat tartalmazna
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

### Hozzájárulási Irányelvek

Sikert hozó hozzájárulás az MCP projektekhez:

1. **Kis lépésekben**: Kezdd dokumentációval, hibajavításokkal vagy kisebb fejlesztésekkel
2. **Stílus útmutató követése**: Tartsd be a projekt kódolási stílusát és konvencióit
3. **Tesztírás**: Mellékelj egységteszteket a kódhozzájárulásaidhoz
4. **Munkád dokumentálása**: Adj világos dokumentációt az új funkciókról vagy változásokról
5. **Célzott PR-ek benyújtása**: Tartózkodj attól, hogy a pull request-ek több problémát vagy funkciót fedjenek le egyszerre
6. **Visszajelzésre reagálás**: Légy nyitott és válaszolj a hozzájárulásodra érkező visszajelzésekre

### Példa Hozzájárulási Munkafolyamat

```bash
# Klónozd a tárat
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# Hozz létre egy új ágat a hozzájárulásodhoz
git checkout -b feature/my-contribution

# Végezze el a módosításaidat
# ...

# Futtasd a teszteket, hogy biztosítsd, módosításaid nem törik meg a meglévő funkcionalitást
npm test

# Kövesd el a módosításaidat egy leíró üzenettel
git commit -am "Fix validation in resource handler"

# Toldd fel az ágadat a saját forkodra
git push origin feature/my-contribution

# Hozz létre egy pull requestet az ágadból a fő tárba
# Ezután foglalkozz a visszajelzésekkel és szükség szerint ismételd meg a PR-t
```

## MCP Szerverek Létrehozása és Megosztása

Az egyik legértékesebb módja az MCP ökoszisztémához való hozzájárulásnak az egyedi MCP szerverek létrehozása és megosztása. A közösség már több száz szervert fejlesztett különböző szolgáltatások és felhasználási esetek számára.

### MCP Szerver Fejlesztői Keretrendszerek

Több keretrendszer is elérhető az MCP szerver fejlesztés egyszerűsítésére:

1. **Hivatalos SDK-k** (ellenőrizd a
    [SDK dokumentációt](https://modelcontextprotocol.io/docs/sdk) az egyes
    SDK-k támogatott protokoll verzióiról):
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
   - [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
   - [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk)

2. **Közösségi Keretrendszerek**:
   - [MCP-Framework](https://mcp-framework.com/) - MCP szerverek fejlesztése elegánsan és gyorsan TypeScript-ben
   - [MCP Deklaratív Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Annotáció-alapú MCP szerverek Java nyelven
   - [Quarkus MCP Szerver SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java keretrendszer MCP szerverekhez
   - [Next.js MCP Szerver sablon](https://github.com/vercel-labs/mcp-for-next.js) - Kezdő Next.js projekt MCP szerverekhez

### Megosztható Eszközök Fejlesztése

#### .NET példa: megosztható eszközcsomag készítése

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

#### Java példa: Maven csomag létrehozása eszközökhez

```java
// pom.xml konfiguráció egy megosztható MCP eszközcsomaghoz
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
            <url>https://maven.pkg.github.com/felhasználónév/mcp-weather-tools</url>
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
        // Sémadefiníció...
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            String location = request.getParameters().get("location").asText();
            int days = request.getParameters().has("days") ? 
                request.getParameters().get("days").asInt() : 3;
            
            // Időjárás API meghívása
            Map<String, Object> forecast = getForecast(location, days);
            
            // Válasz összeállítása
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // A megvalósítás meghívná az időjárás API-t
        // Egyszerűsített példa
        Map<String, Object> result = new HashMap<>();
        // Előrejelzési adat hozzáadása...
        return result;
    }
}

// Fordítás és publikálás Maven használatával
// mvn clean package
// mvn deploy
```

#### Python példa: PyPI csomag közzététele

```python
# PyPI csomag könyvtárszerkezete:
# mcp_nlp_tools/
# ├── LICENSE
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# Példa setup.py
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

# Példa NLP eszköz implementáció (sentiment_tool.py)
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # Töltse be az érzelemelemző modellt
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
            # Paraméterek kinyerése
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # Érzelmek elemzése
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # Eredmény formázása
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # Eredmény visszaadása
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# Kiadáshoz:
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### Legjobb Gyakorlatok Megosztása

Amikor MCP eszközöket osztasz meg a közösséggel:

1. **Teljes Dokumentáció**:
   - Dokumentáld a célt, használatot és példákat
   - Magyarázd el a paramétereket és visszatérési értékeket
   - Dokumentáld az esetleges külső függőségeket

2. **Hibakezelés**:
   - Valósíts meg robosztus hibakezelést
   - Adj hasznos hibaüzeneteket
   - Kezeld szépen a szélsőséges eseteket

3. **Teljesítmény szempontok**:
   - Optimalizáld a sebességet és az erőforrás használatot
   - Valósíts meg gyorsítótárazást, ahol megfelelő
   - Gondolj a skálázhatóságra

4. **Biztonság**:
   - Használj biztonságos API kulcsokat és hitelesítést
   - Érvényesítsd és tisztítsd az inputokat
   - Valósíts meg sebességkorlátozást külső API hívásokhoz

5. **Tesztelés**:
   - Tartalmazzon átfogó tesztlefedettséget
   - Tesztelj különböző bemenetekkel és szélsőséges esetekkel
   - Dokumentáld a tesztelési eljárásokat

## Közösségi Együttműködés és Legjobb Gyakorlatok

A hatékony együttműködés kulcsfontosságú egy virágzó MCP ökoszisztéma számára.

### Kommunikációs Csatornák

- GitHub Issues és Fórumok
- Microsoft Tech Community
- Discord és Slack csatornák
- Stack Overflow (címke: `model-context-protocol` vagy `mcp`)

### Kódellenőrzések

MCP hozzájárulások ellenőrzésekor:

1. **Világosság**: Világos és jól dokumentált a kód?
2. **Helyesség**: A működése megfelel az elvártnak?
3. **Konzisztencia**: Követi a projekt konvencióit?
4. **Teljesség**: Tartalmaz teszteket és dokumentációt?
5. **Biztonság**: Vannak biztonsági aggályok?

### Verzió Kompatibilitás

MCP fejlesztés során:

1. **Protokoll verziózás**: Tartsd be az MCP protokoll verzióját, amit az eszközöd támogat
2. **Kliens kompatibilitás**: Fontold meg a visszafelé kompatibilitást
3. **Szerver kompatibilitás**: Kövesd a szerver implementációs irányelveket
4. **Törő változások**: Egyértelműen dokumentáld az esetleges visszavonó változtatásokat

## Példa Közösségi Projekt: MCP Eszközregiszter

Egy fontos közösségi hozzájárulás lehet egy nyilvános regiszter fejlesztése az MCP eszközökhöz.

```python
# Példa séma egy közösségi eszközregiszter API-hoz

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# Modellek az eszközregiszterhez
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

# FastAPI alkalmazás a regiszterhez
app = FastAPI(title="MCP Tool Registry")

# Memóriában tárolt adatbázis ehhez a példához
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

## Főbb Tanulságok

- Az MCP közösség sokszínű és számos hozzájárulás típust fogad el
- Az MCP-hez való hozzájárulás az alapprotokoll fejlesztéseitől az egyedi eszközökig terjedhet
- A hozzájárulási irányelvek követése növeli a PR elfogadásának esélyét
- MCP eszközök létrehozása és megosztása értékes módja az ökoszisztéma fejlesztésének
- A közösségi együttműködés elengedhetetlen az MCP növekedéséhez és fejlődéséhez

## Gyakorlat

1. Azonosíts egy területet az MCP ökoszisztémában, ahol a képességeid és érdeklődésed alapján hozzájárulhatsz
2. Forkold az MCP adattárat, és állíts be egy helyi fejlesztői környezetet
3. Készíts egy kisebb fejlesztést, hibajavítást vagy eszközt, ami hasznos a közösség számára
4. Dokumentáld a hozzájárulásodat megfelelő tesztekkel és dokumentációval
5. Nyújts be pull request-et a megfelelő adattárba

## További Források

- [MCP Közösségi Projektek](https://github.com/topics/model-context-protocol)

---

## Mi következik

Következő: [Tanulságok a korai elfogadásból](../07-LessonsfromEarlyAdoption/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->