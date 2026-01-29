# Community en Bijdragen

[![Hoe bij te dragen aan MCP: Tools, Documentatie, Code en Meer](../../../translated_images/nl/07.1179f6de46ff196eb3cc13c3510e01c37807a13f3bb9be3c779105ce26737c67.png)](https://youtu.be/v1pvCYAWpRE)

_(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

## Overzicht

Deze les richt zich op hoe je kunt deelnemen aan de MCP-community, bijdragen aan het MCP-ecosysteem en de beste praktijken voor samenwerking kunt volgen. Begrijpen hoe je kunt deelnemen aan open-source MCP-projecten is essentieel voor iedereen die de toekomst van deze technologie wil vormgeven.

## Leerdoelen

Aan het einde van deze les kun je:

- De structuur van de MCP-community en het ecosysteem begrijpen
- Effectief deelnemen aan MCP-communityforums en discussies
- Bijdragen aan open-source MCP-repositories
- Eigen MCP-tools en servers maken en delen
- Beste praktijken voor MCP-ontwikkeling en samenwerking volgen
- Communitybronnen en frameworks voor MCP-ontwikkeling ontdekken

## Het MCP Community Ecosysteem

Het MCP-ecosysteem bestaat uit verschillende componenten en deelnemers die samenwerken om het protocol te verbeteren.

### Belangrijke Communitycomponenten

1. **Core Protocol Beheerders**: De officiële [Model Context Protocol GitHub-organisatie](https://github.com/modelcontextprotocol) onderhoudt de kernspecificaties en referentie-implementaties van MCP.
2. **Toolontwikkelaars**: Individuen en teams die MCP-tools en servers maken.
3. **Integratieaanbieders**: Bedrijven die MCP integreren in hun producten en diensten.
4. **Eindgebruikers**: Ontwikkelaars en organisaties die MCP in hun applicaties gebruiken.
5. **Bijdragers**: Communityleden die code, documentatie of andere middelen bijdragen.

### Communitybronnen

#### Officiële Kanalen

- [MCP GitHub-organisatie](https://github.com/modelcontextprotocol)
- [MCP Documentatie](https://modelcontextprotocol.io/)
- [MCP Specificatie](https://modelcontextprotocol.io/docs/specification)
- [GitHub Discussies](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP Voorbeelden & Servers Repository](https://github.com/modelcontextprotocol/servers)

#### Door de Community Gedreven Bronnen

- [MCP Clients](https://modelcontextprotocol.io/clients) - Lijst van clients die MCP-integraties ondersteunen
- [Community MCP Servers](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Groeiende lijst van door de community ontwikkelde MCP-servers
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Geselecteerde lijst van MCP-servers
- [PulseMCP](https://www.pulsemcp.com/) - Communityhub & nieuwsbrief voor het ontdekken van MCP-bronnen
- [Discord Server](https://discord.gg/jHEGxQu2a5) - Verbinden met MCP-ontwikkelaars
- Taal-specifieke SDK-implementaties
- Blogposts en tutorials

## Bijdragen aan MCP

### Soorten Bijdragen

Het MCP-ecosysteem verwelkomt verschillende soorten bijdragen:

1. **Codebijdragen**:
   - Verbeteringen aan het kernprotocol
   - Bugfixes
   - Implementaties van tools en servers
   - Client/serverbibliotheken in verschillende talen

2. **Documentatie**:
   - Verbeteren van bestaande documentatie
   - Maken van tutorials en handleidingen
   - Vertalen van documentatie
   - Voorbeelden en voorbeeldapplicaties maken

3. **Communityondersteuning**:
   - Vragen beantwoorden op forums en in discussies
   - Testen en rapporteren van problemen
   - Organiseren van community-evenementen
   - Nieuwe bijdragers begeleiden

### Bijdrageproces: Kernprotocol

Om bij te dragen aan het kernprotocol van MCP of officiële implementaties, volg je deze principes uit de [officiële richtlijnen voor bijdragen](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Eenvoud en Minimalisme**: De MCP-specificatie hanteert een hoge standaard voor het toevoegen van nieuwe concepten. Het is makkelijker om iets toe te voegen aan een specificatie dan om het te verwijderen.

2. **Concrete Aanpak**: Wijzigingen in de specificatie moeten gebaseerd zijn op specifieke implementatie-uitdagingen, niet op speculatieve ideeën.

3. **Fasen van een Voorstel**:
   - Definiëren: Onderzoek het probleemgebied en valideer dat andere MCP-gebruikers met een soortgelijk probleem te maken hebben.
   - Prototypen: Bouw een voorbeeldoplossing en demonstreer de praktische toepassing ervan.
   - Schrijven: Op basis van het prototype schrijf je een specificatievoorstel.

### Ontwikkelomgeving Instellen

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

### Voorbeeld: Een Bugfix Bijdragen

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

### Voorbeeld: Een Nieuwe Tool Bijdragen aan de Standaardbibliotheek

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

### Richtlijnen voor Bijdragen

Om succesvol bij te dragen aan MCP-projecten:

1. **Begin Klein**: Start met documentatie, bugfixes of kleine verbeteringen.
2. **Volg de Stijlgids**: Houd je aan de codeerstijl en conventies van het project.
3. **Schrijf Tests**: Voeg unittests toe voor je codebijdragen.
4. **Documenteer Je Werk**: Voeg duidelijke documentatie toe voor nieuwe functies of wijzigingen.
5. **Dien Gerichte PR's In**: Houd pull requests gericht op één enkel probleem of functie.
6. **Ga in op Feedback**: Reageer op feedback over je bijdragen.

### Voorbeeld Bijdrageworkflow

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

## MCP-Servers Maken en Delen

Een van de meest waardevolle manieren om bij te dragen aan het MCP-ecosysteem is door het maken en delen van aangepaste MCP-servers. De community heeft al honderden servers ontwikkeld voor verschillende diensten en toepassingen.

### Frameworks voor MCP-Serverontwikkeling

Er zijn verschillende frameworks beschikbaar om de ontwikkeling van MCP-servers te vereenvoudigen:

1. **Officiële SDK's**:
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Community Frameworks**:
   - [MCP-Framework](https://mcp-framework.com/) - Bouw MCP-servers met elegantie en snelheid in TypeScript
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Annotatiegestuurde MCP-servers met Java
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java-framework voor MCP-servers
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Starterproject voor MCP-servers in Next.js

### Ontwikkelen van Deelbare Tools

#### .NET Voorbeeld: Een Deelbaar Toolpakket Maken

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

#### Java Voorbeeld: Een Mavenpakket voor Tools Maken

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

#### Python Voorbeeld: Een PyPI-pakket Publiceren

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

### Beste Praktijken Delen

Bij het delen van MCP-tools met de community:

1. **Volledige Documentatie**:
   - Documenteer doel, gebruik en voorbeelden
   - Leg parameters en retourwaarden uit
   - Documenteer eventuele externe afhankelijkheden

2. **Foutafhandeling**:
   - Implementeer robuuste foutafhandeling
   - Geef nuttige foutmeldingen
   - Behandel randgevallen zorgvuldig

3. **Prestatieoverwegingen**:
   - Optimaliseer voor zowel snelheid als hulpbrongebruik
   - Implementeer caching waar nodig
   - Houd rekening met schaalbaarheid

4. **Beveiliging**:
   - Gebruik veilige API-sleutels en authenticatie
   - Valideer en filter invoer
   - Implementeer snelheidslimieten voor externe API-aanroepen

5. **Testen**:
   - Zorg voor uitgebreide testdekking
   - Test met verschillende invoertypen en randgevallen
   - Documenteer testprocedures

## Samenwerking en Beste Praktijken in de Community

Effectieve samenwerking is essentieel voor een bloeiend MCP-ecosysteem.

### Communicatiekanalen

- GitHub Issues en Discussies
- Microsoft Tech Community
- Discord- en Slack-kanalen
- Stack Overflow (tag: `model-context-protocol` of `mcp`)

### Code Reviews

Bij het beoordelen van MCP-bijdragen:

1. **Duidelijkheid**: Is de code duidelijk en goed gedocumenteerd?
2. **Correctheid**: Werkt het zoals verwacht?
3. **Consistentie**: Volgt het de conventies van het project?
4. **Volledigheid**: Zijn tests en documentatie inbegrepen?
5. **Beveiliging**: Zijn er beveiligingsproblemen?

### Versiecompatibiliteit

Bij het ontwikkelen voor MCP:

1. **Protocolversies**: Houd je aan de MCP-protocolversie die je tool ondersteunt.
2. **Clientcompatibiliteit**: Houd rekening met achterwaartse compatibiliteit.
3. **Servercompatibiliteit**: Volg de richtlijnen voor serverimplementatie.
4. **Breaking Changes**: Documenteer duidelijk eventuele breaking changes.

## Voorbeeld Communityproject: MCP Tool Registry

Een belangrijke bijdrage van de community kan het ontwikkelen van een openbare registry voor MCP-tools zijn.

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

## Belangrijkste Inzichten

- De MCP-community is divers en verwelkomt verschillende soorten bijdragen.
- Bijdragen aan MCP kan variëren van verbeteringen aan het kernprotocol tot aangepaste tools.
- Het volgen van richtlijnen voor bijdragen vergroot de kans dat je PR wordt geaccepteerd.
- Het maken en delen van MCP-tools is een waardevolle manier om het ecosysteem te verbeteren.
- Samenwerking binnen de community is essentieel voor de groei en verbetering van MCP.

## Oefening

1. Identificeer een gebied in het MCP-ecosysteem waar je een bijdrage kunt leveren op basis van je vaardigheden en interesses.
2. Fork de MCP-repository en stel een lokale ontwikkelomgeving in.
3. Maak een kleine verbetering, bugfix of tool die de community ten goede komt.
4. Documenteer je bijdrage met de juiste tests en documentatie.
5. Dien een pull request in naar de juiste repository.

## Aanvullende Bronnen

- [MCP Communityprojecten](https://github.com/topics/model-context-protocol)

---

Volgende: [Lessen uit Vroege Adoptie](../07-LessonsfromEarlyAdoption/README.md)

**Disclaimer (Vrijwaring)**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.