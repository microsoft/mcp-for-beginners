# Skupnost in prispevki

[![Kako prispevati k MCP: orodja, dokumentacija, koda in več](../../../translated_images/sl/07.1179f6de46ff196eb3cc13c3510e01c37807a13f3bb9be3c779105ce26737c67.png)](https://youtu.be/v1pvCYAWpRE)

_(Kliknite zgornjo sliko za ogled videa te lekcije)_

## Pregled

Ta lekcija se osredotoča na to, kako sodelovati s skupnostjo MCP, prispevati k ekosistemu MCP in slediti najboljšim praksam za sodelovalni razvoj. Razumevanje, kako sodelovati v odprtokodnih projektih MCP, je ključno za tiste, ki želijo oblikovati prihodnost te tehnologije.

## Cilji učenja

Do konca te lekcije boste lahko:

- Razumeli strukturo skupnosti in ekosistema MCP
- Učinkovito sodelovali na forumih in v razpravah skupnosti MCP
- Prispevali k odprtokodnim repozitorijem MCP
- Ustvarjali in delili prilagojena orodja in strežnike MCP
- Sledili najboljšim praksam za razvoj in sodelovanje MCP
- Odkrijte vire in ogrodja skupnosti za razvoj MCP

## Ekosistem skupnosti MCP

Ekosistem MCP sestavljajo različne komponente in udeleženci, ki skupaj delujejo za napredek protokola.

### Ključne komponente skupnosti

1. **Vzdrževalci osnovnega protokola**: Uradna [Model Context Protocol GitHub organizacija](https://github.com/modelcontextprotocol) vzdržuje osnovne specifikacije MCP in referenčne implementacije.
2. **Razvijalci orodij**: Posamezniki in ekipe, ki ustvarjajo orodja in strežnike MCP.
3. **Ponudniki integracij**: Podjetja, ki integrirajo MCP v svoje izdelke in storitve.
4. **Končni uporabniki**: Razvijalci in organizacije, ki uporabljajo MCP v svojih aplikacijah.
5. **Prispevalci**: Člani skupnosti, ki prispevajo kodo, dokumentacijo ali druge vire.

### Viri skupnosti

#### Uradni kanali

- [MCP GitHub organizacija](https://github.com/modelcontextprotocol)
- [MCP dokumentacija](https://modelcontextprotocol.io/)
- [MCP specifikacija](https://modelcontextprotocol.io/docs/specification)
- [GitHub razprave](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP primeri in repozitorij strežnikov](https://github.com/modelcontextprotocol/servers)

#### Viri, ki jih vodi skupnost

- [MCP odjemalci](https://modelcontextprotocol.io/clients) - Seznam odjemalcev, ki podpirajo integracije MCP.
- [Skupnostni strežniki MCP](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Rastoči seznam strežnikov MCP, ki jih razvija skupnost.
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Kuriran seznam strežnikov MCP.
- [PulseMCP](https://www.pulsemcp.com/) - Središče skupnosti in glasilo za odkrivanje virov MCP.
- [Discord strežnik](https://discord.gg/jHEGxQu2a5) - Povežite se z razvijalci MCP.
- SDK implementacije za specifične jezike.
- Blog objave in vadnice.

## Prispevanje k MCP

### Vrste prispevkov

Ekosistem MCP pozdravlja različne vrste prispevkov:

1. **Prispevki kode**:
   - Izboljšave osnovnega protokola
   - Popravki napak
   - Implementacije orodij in strežnikov
   - Knjižnice odjemalcev/strežnikov v različnih jezikih

2. **Dokumentacija**:
   - Izboljšanje obstoječe dokumentacije
   - Ustvarjanje vadnic in vodnikov
   - Prevajanje dokumentacije
   - Ustvarjanje primerov in vzorčnih aplikacij

3. **Podpora skupnosti**:
   - Odgovarjanje na vprašanja na forumih in v razpravah
   - Testiranje in poročanje o težavah
   - Organizacija dogodkov skupnosti
   - Mentorstvo novih prispevalcev

### Postopek prispevanja: Osnovni protokol

Za prispevanje k osnovnemu protokolu MCP ali uradnim implementacijam sledite tem načelom iz [uradnih smernic za prispevanje](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Preprostost in minimalizem**: Specifikacija MCP ohranja visoke standarde za dodajanje novih konceptov. Lažje je dodati stvari v specifikacijo kot jih odstraniti.

2. **Konkretni pristop**: Spremembe specifikacije naj temeljijo na specifičnih izzivih implementacije, ne na špekulativnih idejah.

3. **Faze predloga**:
   - Definiraj: Raziščite problematično področje in preverite, ali se drugi uporabniki MCP soočajo s podobno težavo.
   - Prototip: Zgradite primer rešitve in pokažite njeno praktično uporabo.
   - Napiši: Na podlagi prototipa napišite predlog specifikacije.

### Nastavitev razvojnega okolja

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

### Primer: Prispevanje popravka napake

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

### Primer: Prispevanje novega orodja v standardno knjižnico

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

### Smernice za prispevanje

Za uspešen prispevek k projektom MCP:

1. **Začnite z majhnim**: Začnite z dokumentacijo, popravki napak ali manjšimi izboljšavami.
2. **Sledite slogovnim smernicam**: Upoštevajte slog in konvencije kodiranja projekta.
3. **Pišite teste**: Vključite enotne teste za svoje prispevke kode.
4. **Dokumentirajte svoje delo**: Dodajte jasno dokumentacijo za nove funkcije ali spremembe.
5. **Pošljite ciljno usmerjene PR-je**: Naj bodo pull requesti osredotočeni na eno težavo ali funkcijo.
6. **Sodelujte pri povratnih informacijah**: Bodite odzivni na povratne informacije o svojih prispevkih.

### Primer delovnega toka prispevka

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

## Ustvarjanje in deljenje strežnikov MCP

Eden najbolj dragocenih načinov prispevanja k ekosistemu MCP je ustvarjanje in deljenje prilagojenih strežnikov MCP. Skupnost je že razvila na stotine strežnikov za različne storitve in primere uporabe.

### Ogrodja za razvoj strežnikov MCP

Na voljo je več ogrodij za poenostavitev razvoja strežnikov MCP:

1. **Uradni SDK-ji**:
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Ogrodja skupnosti**:
   - [MCP-Framework](https://mcp-framework.com/) - Gradite strežnike MCP elegantno in hitro v TypeScriptu.
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Strežniki MCP, ki temeljijo na anotacijah v Javi.
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java ogrodje za strežnike MCP.
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Začetni projekt Next.js za strežnike MCP.

### Razvijanje deljivih orodij

#### .NET Primer: Ustvarjanje deljivega paketa orodij

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

#### Java Primer: Ustvarjanje Maven paketa za orodja

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

#### Python Primer: Objavljanje paketa na PyPI

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

### Deljenje najboljših praks

Pri deljenju orodij MCP s skupnostjo:

1. **Popolna dokumentacija**:
   - Dokumentirajte namen, uporabo in primere.
   - Pojasnite parametre in vrnjene vrednosti.
   - Dokumentirajte vse zunanje odvisnosti.

2. **Obravnava napak**:
   - Implementirajte robustno obravnavo napak.
   - Zagotovite uporabna sporočila o napakah.
   - Eleganten pristop k robnim primerom.

3. **Učinkovitost**:
   - Optimizirajte za hitrost in uporabo virov.
   - Implementirajte predpomnjenje, kjer je primerno.
   - Upoštevajte razširljivost.

4. **Varnost**:
   - Uporabljajte varne API ključe in avtentikacijo.
   - Validirajte in sanirajte vnose.
   - Implementirajte omejevanje hitrosti za zunanje klice API.

5. **Testiranje**:
   - Vključite obsežno pokritost testov.
   - Testirajte z različnimi tipi vhodov in robnimi primeri.
   - Dokumentirajte postopke testiranja.

## Sodelovanje v skupnosti in najboljše prakse

Učinkovito sodelovanje je ključno za uspešen ekosistem MCP.

### Komunikacijski kanali

- GitHub težave in razprave
- Microsoft Tech Community
- Discord in Slack kanali
- Stack Overflow (oznaka: `model-context-protocol` ali `mcp`)

### Pregledi kode

Pri pregledu prispevkov MCP:

1. **Jasnost**: Ali je koda jasna in dobro dokumentirana?
2. **Pravilnost**: Ali deluje, kot je pričakovano?
3. **Doslednost**: Ali sledi konvencijam projekta?
4. **Popolnost**: Ali so vključeni testi in dokumentacija?
5. **Varnost**: Ali obstajajo varnostni pomisleki?

### Združljivost različic

Pri razvoju za MCP:

1. **Različice protokola**: Upoštevajte različico protokola MCP, ki jo podpira vaše orodje.
2. **Združljivost odjemalcev**: Upoštevajte združljivost za nazaj.
3. **Združljivost strežnikov**: Sledite smernicam za implementacijo strežnikov.
4. **Prelomne spremembe**: Jasno dokumentirajte vse prelomne spremembe.

## Primer projekta skupnosti: Register orodij MCP

Pomemben prispevek skupnosti bi lahko bil razvoj javnega registra za orodja MCP.

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

## Ključne točke

- Skupnost MCP je raznolika in pozdravlja različne vrste prispevkov.
- Prispevanje k MCP lahko vključuje izboljšave osnovnega protokola ali prilagojena orodja.
- Sledenje smernicam za prispevanje poveča možnosti za sprejetje vašega PR.
- Ustvarjanje in deljenje orodij MCP je dragocen način za izboljšanje ekosistema.
- Sodelovanje v skupnosti je bistveno za rast in izboljšanje MCP.

## Vaja

1. Prepoznajte področje v ekosistemu MCP, kjer bi lahko prispevali glede na svoje veščine in interese.
2. Forkajte repozitorij MCP in nastavite lokalno razvojno okolje.
3. Ustvarite majhno izboljšavo, popravek napake ali orodje, ki bi koristilo skupnosti.
4. Dokumentirajte svoj prispevek z ustreznimi testi in dokumentacijo.
5. Pošljite pull request v ustrezen repozitorij.

## Dodatni viri

- [Projekti skupnosti MCP](https://github.com/topics/model-context-protocol)

---

Naprej: [Lekcije iz zgodnje uporabe](../07-LessonsfromEarlyAdoption/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.