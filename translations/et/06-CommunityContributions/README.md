# Kogukond ja panustamine

[![Kuidas panustada MCP-sse: tööriistad, dokumendid, kood ja palju muud](../../../translated_images/et/07.1179f6de46ff196eb3cc13c3510e01c37807a13f3bb9be3c779105ce26737c67.png)](https://youtu.be/v1pvCYAWpRE)

_(Klõpsa ülaloleval pildil, et vaadata selle õppetunni videot)_

## Ülevaade

See õppetund keskendub sellele, kuidas osaleda MCP kogukonnas, panustada MCP ökosüsteemi ja järgida parimaid tavasid koostööl põhinevas arenduses. Avatud lähtekoodiga MCP projektides osalemise mõistmine on oluline neile, kes soovivad kujundada selle tehnoloogia tulevikku.

## Õppeeesmärgid

Selle õppetunni lõpuks oskad:

- Mõista MCP kogukonna ja ökosüsteemi struktuuri
- Tõhusalt osaleda MCP kogukonna foorumites ja aruteludes
- Panustada MCP avatud lähtekoodiga repositooriumidesse
- Luua ja jagada kohandatud MCP tööriistu ja servereid
- Järgida MCP arenduse ja koostöö parimaid tavasid
- Avastada kogukonna ressursse ja raamistikke MCP arenduseks

## MCP kogukonna ökosüsteem

MCP ökosüsteem koosneb erinevatest komponentidest ja osalejatest, kes töötavad koos protokolli arendamise nimel.

### Kogukonna põhikomponendid

1. **Põhiprotokolli hooldajad**: Ametlik [Model Context Protocol GitHubi organisatsioon](https://github.com/modelcontextprotocol) haldab MCP põhispetsifikatsioone ja viiteimplementatsioone.
2. **Tööriistade arendajad**: Isikud ja meeskonnad, kes loovad MCP tööriistu ja servereid.
3. **Integratsioonipakkujad**: Ettevõtted, kes integreerivad MCP oma toodetesse ja teenustesse.
4. **Lõppkasutajad**: Arendajad ja organisatsioonid, kes kasutavad MCP-d oma rakendustes.
5. **Panustajad**: Kogukonna liikmed, kes panustavad koodi, dokumentatsiooni või muude ressurssidega.

### Kogukonna ressursid

#### Ametlikud kanalid

- [MCP GitHubi organisatsioon](https://github.com/modelcontextprotocol)
- [MCP dokumentatsioon](https://modelcontextprotocol.io/)
- [MCP spetsifikatsioon](https://modelcontextprotocol.io/docs/specification)
- [GitHubi arutelud](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP näited ja serverite repositoorium](https://github.com/modelcontextprotocol/servers)

#### Kogukonna juhitud ressursid

- [MCP kliendid](https://modelcontextprotocol.io/clients) - Nimekiri klientidest, mis toetavad MCP integratsioone.
- [Kogukonna MCP serverid](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Kasvav nimekiri kogukonna arendatud MCP serveritest.
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Kuraatorite nimekiri MCP serveritest.
- [PulseMCP](https://www.pulsemcp.com/) - Kogukonna keskus ja uudiskiri MCP ressursside avastamiseks.
- [Discordi server](https://discord.gg/jHEGxQu2a5) - Ühenda MCP arendajatega.
- Keelepõhised SDK implementatsioonid.
- Blogipostitused ja juhendid.

## Panustamine MCP-sse

### Panustamise tüübid

MCP ökosüsteem tervitab erinevaid panustamisviise:

1. **Koodipanused**:
   - Põhiprotokolli täiustused
   - Vigade parandused
   - Tööriistade ja serverite implementatsioonid
   - Klient/serveri teegid erinevates keeltes

2. **Dokumentatsioon**:
   - Olemasoleva dokumentatsiooni täiustamine
   - Juhendite ja õpetuste loomine
   - Dokumentatsiooni tõlkimine
   - Näidete ja näidisrakenduste loomine

3. **Kogukonna tugi**:
   - Küsimustele vastamine foorumites ja aruteludes
   - Testimine ja probleemide raporteerimine
   - Kogukonna ürituste korraldamine
   - Uute panustajate juhendamine

### Panustamise protsess: Põhiprotokoll

Põhiprotokolli või ametlike implementatsioonide panustamiseks järgi [ametlikke panustamise juhiseid](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Lihtsus ja minimalism**: MCP spetsifikatsioon seab kõrge lati uute kontseptsioonide lisamiseks. Spetsifikatsiooni on lihtsam asju lisada kui eemaldada.

2. **Konkreetne lähenemine**: Spetsifikatsiooni muudatused peaksid põhinema konkreetsetel implementatsiooniprobleemidel, mitte spekulatiivsetel ideedel.

3. **Ettepaneku etapid**:
   - Defineeri: Uuri probleemiruumi, kinnita, et teised MCP kasutajad seisavad silmitsi sarnase probleemiga.
   - Prototüüp: Loo näidislahendus ja demonstreeri selle praktilist rakendust.
   - Kirjuta: Prototüübi põhjal kirjuta spetsifikatsiooni ettepanek.

### Arenduskeskkonna seadistamine

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

### Näide: Vigade paranduse panustamine

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

### Näide: Uue tööriista lisamine standardteeki

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

### Panustamise juhised

Eduka panuse tegemiseks MCP projektidesse:

1. **Alusta väikselt**: Alusta dokumentatsioonist, vigade parandustest või väikestest täiustustest.
2. **Järgi stiilijuhendit**: Järgi projekti koodistiili ja konventsioone.
3. **Kirjuta teste**: Lisa oma koodipanustele ühiktestid.
4. **Dokumenteeri oma töö**: Lisa selge dokumentatsioon uute funktsioonide või muudatuste kohta.
5. **Esita sihitud PR-id**: Hoia pull requestid keskendunud ühele probleemile või funktsioonile.
6. **Vasta tagasisidele**: Ole vastuvõtlik tagasisidele oma panuste kohta.

### Näide panustamise töövoost

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

## MCP serverite loomine ja jagamine

Üks väärtuslikumaid viise MCP ökosüsteemi panustamiseks on kohandatud MCP serverite loomine ja jagamine. Kogukond on juba arendanud sadu servereid erinevate teenuste ja kasutusjuhtude jaoks.

### MCP serverite arendamise raamistikud

MCP serverite arendamise lihtsustamiseks on saadaval mitmeid raamistikke:

1. **Ametlikud SDK-d**:
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Kogukonna raamistikud**:
   - [MCP-Framework](https://mcp-framework.com/) - Ehita MCP servereid elegantselt ja kiiresti TypeScriptis.
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Annotatsioonipõhised MCP serverid Java keeles.
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java raamistik MCP serverite jaoks.
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Starter Next.js projekt MCP serverite jaoks.

### Jagatavate tööriistade arendamine

#### .NET näide: Jagatava tööriistapaketi loomine

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

#### Java näide: Maven paketi loomine tööriistade jaoks

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

#### Python näide: PyPI paketi avaldamine

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

### Parimate tavade jagamine

MCP tööriistade jagamisel kogukonnaga:

1. **Täielik dokumentatsioon**:
   - Dokumenteeri eesmärk, kasutus ja näited.
   - Selgita parameetreid ja tagastusväärtusi.
   - Dokumenteeri kõik välised sõltuvused.

2. **Vigade käsitlemine**:
   - Rakenda tugev vigade käsitlemine.
   - Paku kasulikke veateateid.
   - Käsitle äärejuhtumeid elegantselt.

3. **Jõudluse kaalutlused**:
   - Optimeeri nii kiiruse kui ka ressursikasutuse jaoks.
   - Rakenda vahemällu salvestamist, kui see on asjakohane.
   - Mõtle skaleeritavusele.

4. **Turvalisus**:
   - Kasuta turvalisi API võtmeid ja autentimist.
   - Kontrolli ja puhasta sisendeid.
   - Rakenda väliste API-kõnede jaoks kiirusepiiranguid.

5. **Testimine**:
   - Lisa ulatuslik testkatvus.
   - Testi erinevate sisenditüüpide ja äärejuhtumitega.
   - Dokumenteeri testimisprotseduurid.

## Kogukonna koostöö ja parimad tavad

Tõhus koostöö on MCP ökosüsteemi elujõulisuse võti.

### Kommunikatsioonikanalid

- GitHubi probleemid ja arutelud
- Microsoft Tech Community
- Discordi ja Slacki kanalid
- Stack Overflow (märksõna: `model-context-protocol` või `mcp`)

### Koodikontrollid

MCP panuste ülevaatamisel:

1. **Selgus**: Kas kood on selge ja hästi dokumenteeritud?
2. **Õigsus**: Kas see töötab ootuspäraselt?
3. **Järjepidevus**: Kas see järgib projekti konventsioone?
4. **Täielikkus**: Kas testid ja dokumentatsioon on lisatud?
5. **Turvalisus**: Kas on mingeid turvalisuse probleeme?

### Versioonide ühilduvus

MCP jaoks arendamisel:

1. **Protokolli versioonimine**: Järgi MCP protokolli versiooni, mida sinu tööriist toetab.
2. **Kliendi ühilduvus**: Mõtle tagasiühilduvusele.
3. **Serveri ühilduvus**: Järgi serveri implementatsiooni juhiseid.
4. **Murdvad muudatused**: Dokumenteeri selgelt kõik murdvad muudatused.

## Näide kogukonna projektist: MCP tööriistade register

Oluline kogukonna panus võiks olla avaliku registri arendamine MCP tööriistade jaoks.

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

## Peamised punktid

- MCP kogukond on mitmekesine ja tervitab erinevaid panustamisviise.
- MCP-sse panustamine võib ulatuda põhiprotokolli täiustustest kohandatud tööriistadeni.
- Panustamise juhiste järgimine suurendab PR-i vastuvõtmise tõenäosust.
- MCP tööriistade loomine ja jagamine on väärtuslik viis ökosüsteemi täiustamiseks.
- Kogukonna koostöö on MCP kasvu ja täiustamise jaoks hädavajalik.

## Harjutus

1. Määra MCP ökosüsteemis valdkond, kuhu saaksid oma oskuste ja huvide põhjal panustada.
2. Forki MCP repositoorium ja seadista kohalik arenduskeskkond.
3. Loo väike täiustus, vigade parandus või tööriist, mis kogukonnale kasuks tuleks.
4. Dokumenteeri oma panus koos sobivate testide ja dokumentatsiooniga.
5. Esita pull request sobivasse repositooriumisse.

## Lisamaterjalid

- [MCP kogukonna projektid](https://github.com/topics/model-context-protocol)

---

Järgmine: [Õppetunnid varajasest kasutuselevõtust](../07-LessonsfromEarlyAdoption/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.