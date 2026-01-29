# Fællesskab og Bidrag

[![Sådan bidrager du til MCP: Værktøjer, Dokumentation, Kode og Mere](../../../translated_images/da/07.1179f6de46ff196eb3cc13c3510e01c37807a13f3bb9be3c779105ce26737c67.png)](https://youtu.be/v1pvCYAWpRE)

_(Klik på billedet ovenfor for at se videoen til denne lektion)_

## Oversigt

Denne lektion fokuserer på, hvordan man engagerer sig i MCP-fællesskabet, bidrager til MCP-økosystemet og følger bedste praksis for samarbejdsudvikling. At forstå, hvordan man deltager i open source MCP-projekter, er afgørende for dem, der ønsker at forme fremtiden for denne teknologi.

## Læringsmål

Ved afslutningen af denne lektion vil du kunne:

- Forstå strukturen af MCP-fællesskabet og økosystemet
- Deltage effektivt i MCP-fællesskabets fora og diskussioner
- Bidrage til MCP open source-repositorier
- Oprette og dele skræddersyede MCP-værktøjer og servere
- Følge bedste praksis for MCP-udvikling og samarbejde
- Opdage fællesskabsressourcer og rammer for MCP-udvikling

## MCP-fællesskabets økosystem

MCP-økosystemet består af forskellige komponenter og deltagere, der arbejder sammen for at fremme protokollen.

### Centrale fællesskabskomponenter

1. **Kerneprotokolvedligeholdere**: Den officielle [Model Context Protocol GitHub-organisation](https://github.com/modelcontextprotocol) vedligeholder de centrale MCP-specifikationer og referenceimplementeringer.
2. **Værktøjsudviklere**: Personer og teams, der skaber MCP-værktøjer og servere.
3. **Integrationsleverandører**: Virksomheder, der integrerer MCP i deres produkter og tjenester.
4. **Slutbrugere**: Udviklere og organisationer, der bruger MCP i deres applikationer.
5. **Bidragydere**: Fællesskabsmedlemmer, der bidrager med kode, dokumentation eller andre ressourcer.

### Fællesskabsressourcer

#### Officielle kanaler

- [MCP GitHub-organisation](https://github.com/modelcontextprotocol)
- [MCP-dokumentation](https://modelcontextprotocol.io/)
- [MCP-specifikation](https://modelcontextprotocol.io/docs/specification)
- [GitHub-diskussioner](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP Eksempler & Servere Repository](https://github.com/modelcontextprotocol/servers)

#### Fællesskabsdrevne ressourcer

- [MCP-klienter](https://modelcontextprotocol.io/clients) - Liste over klienter, der understøtter MCP-integrationer.
- [Fællesskabets MCP-servere](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Voksende liste over MCP-servere udviklet af fællesskabet.
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Kurateret liste over MCP-servere.
- [PulseMCP](https://www.pulsemcp.com/) - Fællesskabshub og nyhedsbrev til opdagelse af MCP-ressourcer.
- [Discord-server](https://discord.gg/jHEGxQu2a5) - Forbind med MCP-udviklere.
- Sprog-specifikke SDK-implementeringer.
- Blogindlæg og tutorials.

## Bidrag til MCP

### Typer af bidrag

MCP-økosystemet byder velkommen til forskellige typer bidrag:

1. **Kodebidrag**:
   - Forbedringer af kerneprotokollen.
   - Fejlrettelser.
   - Implementeringer af værktøjer og servere.
   - Klient-/serverbiblioteker på forskellige sprog.

2. **Dokumentation**:
   - Forbedring af eksisterende dokumentation.
   - Oprettelse af tutorials og vejledninger.
   - Oversættelse af dokumentation.
   - Oprettelse af eksempler og prøveapplikationer.

3. **Fællesskabsstøtte**:
   - Besvare spørgsmål på fora og diskussioner.
   - Testning og rapportering af problemer.
   - Organisering af fællesskabsbegivenheder.
   - Mentoring af nye bidragydere.

### Bidragsproces: Kerneprotokol

For at bidrage til MCP's kerneprotokol eller officielle implementeringer skal du følge disse principper fra de [officielle retningslinjer for bidrag](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Enkelhed og minimalisme**: MCP-specifikationen opretholder en høj standard for at tilføje nye begreber. Det er lettere at tilføje ting til en specifikation end at fjerne dem.

2. **Konkret tilgang**: Ændringer i specifikationen bør baseres på specifikke implementeringsudfordringer, ikke spekulative ideer.

3. **Faser af et forslag**:
   - Definer: Udforsk problemområdet, valider at andre MCP-brugere står over for et lignende problem.
   - Prototype: Byg en eksempel-løsning og demonstrer dens praktiske anvendelse.
   - Skriv: Baseret på prototypen, skriv et specifikationsforslag.

### Opsætning af udviklingsmiljø

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

### Eksempel: Bidrage med en fejlrettelse

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

### Eksempel: Bidrage med et nyt værktøj til standardbiblioteket

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

### Retningslinjer for bidrag

For at gøre et vellykket bidrag til MCP-projekter:

1. **Start småt**: Begynd med dokumentation, fejlrettelser eller små forbedringer.
2. **Følg stilguiden**: Overhold projektets kodestil og konventioner.
3. **Skriv tests**: Inkluder enhedstests for dine kodebidrag.
4. **Dokumentér dit arbejde**: Tilføj klar dokumentation for nye funktioner eller ændringer.
5. **Indsend målrettede PR'er**: Hold pull requests fokuseret på et enkelt problem eller funktion.
6. **Engager dig med feedback**: Vær lydhør over for feedback på dine bidrag.

### Eksempel på bidragsworkflow

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

## Oprettelse og deling af MCP-servere

En af de mest værdifulde måder at bidrage til MCP-økosystemet er ved at oprette og dele skræddersyede MCP-servere. Fællesskabet har allerede udviklet hundredevis af servere til forskellige tjenester og anvendelser.

### MCP-serverudviklingsrammer

Flere rammer er tilgængelige for at forenkle udviklingen af MCP-servere:

1. **Officielle SDK'er**:
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Fællesskabsrammer**:
   - [MCP-Framework](https://mcp-framework.com/) - Byg MCP-servere med elegance og hastighed i TypeScript.
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Annotation-drevne MCP-servere med Java.
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java-ramme for MCP-servere.
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Starterprojekt for MCP-servere med Next.js.

### Udvikling af delbare værktøjer

#### .NET Eksempel: Oprettelse af en delbar værktøjspakke

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

#### Java Eksempel: Oprettelse af en Maven-pakke til værktøjer

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

#### Python Eksempel: Udgivelse af en PyPI-pakke

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

### Deling af bedste praksis

Når du deler MCP-værktøjer med fællesskabet:

1. **Komplet dokumentation**:
   - Dokumentér formål, brug og eksempler.
   - Forklar parametre og returværdier.
   - Dokumentér eventuelle eksterne afhængigheder.

2. **Fejlhåndtering**:
   - Implementér robust fejlhåndtering.
   - Giv nyttige fejlmeddelelser.
   - Håndtér kanttilfælde elegant.

3. **Ydeevneovervejelser**:
   - Optimer for både hastighed og ressourceforbrug.
   - Implementér caching, hvor det er passende.
   - Overvej skalerbarhed.

4. **Sikkerhed**:
   - Brug sikre API-nøgler og autentifikation.
   - Valider og rens input.
   - Implementér hastighedsbegrænsning for eksterne API-kald.

5. **Testning**:
   - Inkluder omfattende testdækning.
   - Test med forskellige inputtyper og kanttilfælde.
   - Dokumentér testprocedurer.

## Fællesskabssamarbejde og bedste praksis

Effektivt samarbejde er nøglen til et blomstrende MCP-økosystem.

### Kommunikationskanaler

- GitHub Issues og Diskussioner.
- Microsoft Tech Community.
- Discord- og Slack-kanaler.
- Stack Overflow (tag: `model-context-protocol` eller `mcp`).

### Kodegennemgange

Når du gennemgår MCP-bidrag:

1. **Klarhed**: Er koden klar og veldokumenteret?
2. **Korrekthed**: Fungerer den som forventet?
3. **Konsistens**: Følger den projektets konventioner?
4. **Komplethed**: Er tests og dokumentation inkluderet?
5. **Sikkerhed**: Er der nogen sikkerhedsproblemer?

### Versionskompatibilitet

Når du udvikler til MCP:

1. **Protokolversionering**: Overhold MCP-protokolversionen, som dit værktøj understøtter.
2. **Klientkompatibilitet**: Overvej bagudkompatibilitet.
3. **Serverkompatibilitet**: Følg retningslinjerne for serverimplementering.
4. **Breaking Changes**: Dokumentér tydeligt eventuelle breaking changes.

## Eksempel på fællesskabsprojekt: MCP-værktøjsregister

En vigtig fællesskabsbidrag kunne være udviklingen af et offentligt register for MCP-værktøjer.

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

## Vigtige pointer

- MCP-fællesskabet er mangfoldigt og byder velkommen til forskellige typer bidrag.
- Bidrag til MCP kan spænde fra forbedringer af kerneprotokollen til skræddersyede værktøjer.
- At følge retningslinjer for bidrag øger chancerne for, at din PR bliver accepteret.
- Oprettelse og deling af MCP-værktøjer er en værdifuld måde at forbedre økosystemet på.
- Fællesskabssamarbejde er afgørende for væksten og forbedringen af MCP.

## Øvelse

1. Identificér et område i MCP-økosystemet, hvor du kunne bidrage baseret på dine færdigheder og interesser.
2. Fork MCP-repositoriet og opsæt et lokalt udviklingsmiljø.
3. Opret en lille forbedring, fejlrettelse eller et værktøj, der vil gavne fællesskabet.
4. Dokumentér dit bidrag med passende tests og dokumentation.
5. Indsend en pull request til det relevante repository.

## Yderligere ressourcer

- [MCP-fællesskabsprojekter](https://github.com/topics/model-context-protocol)

---

Næste: [Lektioner fra tidlig adoption](../07-LessonsfromEarlyAdoption/README.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.