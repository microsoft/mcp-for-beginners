# Community und Beiträge

[![Wie man zu MCP beiträgt: Tools, Dokumentation, Code und mehr](../../../translated_images/de/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Klicken Sie auf das Bild oben, um das Video zu dieser Lektion anzusehen)_

## Überblick

Diese Lektion konzentriert sich darauf, wie man sich in der MCP-Community engagiert, zum MCP-Ökosystem beiträgt und bewährte Praktiken für kollaborative Entwicklung befolgt. Zu verstehen, wie man an Open-Source-MCP-Projekten teilnimmt, ist entscheidend für diejenigen, die die Zukunft dieser Technologie mitgestalten möchten.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Die Struktur der MCP-Community und des Ökosystems zu verstehen
- Effektiv an Foren und Diskussionen der MCP-Community teilzunehmen
- Zu Open-Source-Repositories von MCP beizutragen
- Eigene MCP-Tools und -Server zu erstellen und zu teilen
- Bewährte Praktiken für MCP-Entwicklung und Zusammenarbeit zu befolgen
- Community-Ressourcen und Frameworks für die MCP-Entwicklung zu entdecken

## Das MCP-Community-Ökosystem

Das MCP-Ökosystem besteht aus verschiedenen Komponenten und Teilnehmern, die zusammenarbeiten, um das Protokoll voranzubringen.

### Wichtige Community-Komponenten

1. **Kernprotokoll-Wartungsteam**: Die offizielle [Model Context Protocol GitHub-Organisation](https://github.com/modelcontextprotocol) pflegt die MCP-Spezifikationen und Referenzimplementierungen.
2. **Tool-Entwickler**: Einzelpersonen und Teams, die MCP-Tools und -Server erstellen.
3. **Integrationsanbieter**: Unternehmen, die MCP in ihre Produkte und Dienstleistungen integrieren.
4. **Endbenutzer**: Entwickler und Organisationen, die MCP in ihren Anwendungen nutzen.
5. **Beitragende**: Community-Mitglieder, die Code, Dokumentation oder andere Ressourcen beisteuern.

### Community-Ressourcen

#### Offizielle Kanäle

- [MCP GitHub-Organisation](https://github.com/modelcontextprotocol)
- [MCP-Dokumentation](https://modelcontextprotocol.io/)
- [MCP-Spezifikation](https://modelcontextprotocol.io/docs/specification)
- [GitHub-Diskussionen](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP-Beispiele & Server-Repository](https://github.com/modelcontextprotocol/servers)

#### Community-gesteuerte Ressourcen

- [MCP-Clients](https://modelcontextprotocol.io/clients) - Liste von Clients, die MCP-Integrationen unterstützen
- [Community-MCP-Server](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Wachsende Liste von Community-entwickelten MCP-Servern
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Kuratierte Liste von MCP-Servern
- [PulseMCP](https://www.pulsemcp.com/) - Community-Hub & Newsletter für MCP-Ressourcen
- [Discord-Server](https://discord.gg/jHEGxQu2a5) - Vernetzen Sie sich mit MCP-Entwicklern
- Sprachspezifische SDK-Implementierungen
- Blogbeiträge und Tutorials

## Beiträge zu MCP

### Arten von Beiträgen

Das MCP-Ökosystem begrüßt verschiedene Arten von Beiträgen:

1. **Code-Beiträge**:
   - Verbesserungen des Kernprotokolls
   - Fehlerbehebungen
   - Implementierungen von Tools und Servern
   - Client-/Server-Bibliotheken in verschiedenen Programmiersprachen

2. **Dokumentation**:
   - Verbesserung bestehender Dokumentation
   - Erstellung von Tutorials und Anleitungen
   - Übersetzung von Dokumentation
   - Erstellung von Beispielen und Musteranwendungen

3. **Community-Unterstützung**:
   - Beantwortung von Fragen in Foren und Diskussionen
   - Testen und Melden von Problemen
   - Organisation von Community-Events
   - Mentoring neuer Beitragender

### Beitragsprozess: Kernprotokoll

Um zum Kernprotokoll oder zu offiziellen Implementierungen von MCP beizutragen, folgen Sie diesen Prinzipien aus den [offiziellen Beitragsrichtlinien](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Einfachheit und Minimalismus**: Die MCP-Spezifikation setzt hohe Maßstäbe für das Hinzufügen neuer Konzepte. Es ist einfacher, etwas zu einer Spezifikation hinzuzufügen, als es zu entfernen.

2. **Konkreter Ansatz**: Änderungen an der Spezifikation sollten auf spezifischen Implementierungsherausforderungen basieren, nicht auf spekulativen Ideen.

3. **Phasen eines Vorschlags**:
   - Definieren: Den Problemraum erkunden und validieren, dass andere MCP-Nutzer ein ähnliches Problem haben.
   - Prototyp: Eine Beispiel-Lösung entwickeln und deren praktische Anwendung demonstrieren.
   - Schreiben: Basierend auf dem Prototyp einen Spezifikationsvorschlag erstellen.

### Entwicklungsumgebung einrichten

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

### Beispiel: Einen Fehler beheben

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

### Beispiel: Ein neues Tool zur Standardbibliothek hinzufügen

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

### Beitragsrichtlinien

Um erfolgreich zu MCP-Projekten beizutragen:

1. **Klein anfangen**: Beginnen Sie mit Dokumentation, Fehlerbehebungen oder kleinen Verbesserungen.
2. **Styleguide befolgen**: Halten Sie sich an den Coding-Stil und die Konventionen des Projekts.
3. **Tests schreiben**: Fügen Sie Unit-Tests für Ihre Code-Beiträge hinzu.
4. **Arbeit dokumentieren**: Fügen Sie klare Dokumentation für neue Funktionen oder Änderungen hinzu.
5. **Gezielte PRs einreichen**: Halten Sie Pull Requests auf ein einzelnes Problem oder eine Funktion fokussiert.
6. **Feedback annehmen**: Reagieren Sie auf Feedback zu Ihren Beiträgen.

### Beispiel-Workflow für Beiträge

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

## MCP-Server erstellen und teilen

Eine der wertvollsten Möglichkeiten, zum MCP-Ökosystem beizutragen, ist die Erstellung und das Teilen von benutzerdefinierten MCP-Servern. Die Community hat bereits Hunderte von Servern für verschiedene Dienste und Anwendungsfälle entwickelt.

### MCP-Server-Entwicklungsframeworks

Mehrere Frameworks stehen zur Verfügung, um die Entwicklung von MCP-Servern zu vereinfachen:

1. **Offizielle SDKs**:
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Community-Frameworks**:
   - [MCP-Framework](https://mcp-framework.com/) - MCP-Server mit Eleganz und Geschwindigkeit in TypeScript erstellen
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Annotation-gesteuerte MCP-Server mit Java
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java-Framework für MCP-Server
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Starterprojekt für MCP-Server mit Next.js

### Entwickeln von teilbaren Tools

#### .NET-Beispiel: Ein teilbares Tool-Paket erstellen

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

#### Java-Beispiel: Ein Maven-Paket für Tools erstellen

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

#### Python-Beispiel: Ein PyPI-Paket veröffentlichen

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

### Best Practices beim Teilen

Beim Teilen von MCP-Tools mit der Community:

1. **Vollständige Dokumentation**:
   - Zweck, Nutzung und Beispiele dokumentieren
   - Parameter und Rückgabewerte erklären
   - Externe Abhängigkeiten dokumentieren

2. **Fehlerbehandlung**:
   - Robuste Fehlerbehandlung implementieren
   - Nützliche Fehlermeldungen bereitstellen
   - Randfälle elegant behandeln

3. **Leistungsüberlegungen**:
   - Sowohl Geschwindigkeit als auch Ressourcennutzung optimieren
   - Caching implementieren, wenn angebracht
   - Skalierbarkeit berücksichtigen

4. **Sicherheit**:
   - Sichere API-Schlüssel und Authentifizierung verwenden
   - Eingaben validieren und bereinigen
   - Ratenbegrenzung für externe API-Aufrufe implementieren

5. **Tests**:
   - Umfassende Testabdeckung sicherstellen
   - Mit verschiedenen Eingabetypen und Randfällen testen
   - Testverfahren dokumentieren

## Community-Zusammenarbeit und Best Practices

Effektive Zusammenarbeit ist der Schlüssel zu einem florierenden MCP-Ökosystem.

### Kommunikationskanäle

- GitHub-Issues und -Diskussionen
- Microsoft Tech Community
- Discord- und Slack-Kanäle
- Stack Overflow (Tag: `model-context-protocol` oder `mcp`)

### Code-Reviews

Beim Überprüfen von MCP-Beiträgen:

1. **Klarheit**: Ist der Code klar und gut dokumentiert?
2. **Korrektheit**: Funktioniert er wie erwartet?
3. **Konsistenz**: Folgt er den Projektkonventionen?
4. **Vollständigkeit**: Sind Tests und Dokumentation enthalten?
5. **Sicherheit**: Gibt es Sicherheitsbedenken?

### Versionskompatibilität

Bei der Entwicklung für MCP:

1. **Protokollversionierung**: Halten Sie sich an die MCP-Protokollversion, die Ihr Tool unterstützt.
2. **Client-Kompatibilität**: Berücksichtigen Sie Abwärtskompatibilität.
3. **Server-Kompatibilität**: Befolgen Sie die Richtlinien für Serverimplementierungen.
4. **Breaking Changes**: Dokumentieren Sie alle Breaking Changes klar.

## Beispiel-Community-Projekt: MCP-Tool-Registry

Ein wichtiges Community-Projekt könnte die Entwicklung eines öffentlichen Registers für MCP-Tools sein.

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

## Wichtige Erkenntnisse

- Die MCP-Community ist vielfältig und begrüßt verschiedene Arten von Beiträgen.
- Beiträge zu MCP können von Verbesserungen des Kernprotokolls bis hin zu benutzerdefinierten Tools reichen.
- Das Befolgen von Beitragsrichtlinien erhöht die Wahrscheinlichkeit, dass Ihr PR akzeptiert wird.
- Die Erstellung und das Teilen von MCP-Tools ist eine wertvolle Möglichkeit, das Ökosystem zu verbessern.
- Community-Zusammenarbeit ist entscheidend für das Wachstum und die Verbesserung von MCP.

## Übung

1. Identifizieren Sie einen Bereich im MCP-Ökosystem, in dem Sie basierend auf Ihren Fähigkeiten und Interessen einen Beitrag leisten könnten.
2. Forken Sie das MCP-Repository und richten Sie eine lokale Entwicklungsumgebung ein.
3. Erstellen Sie eine kleine Verbesserung, Fehlerbehebung oder ein Tool, das der Community zugutekommt.
4. Dokumentieren Sie Ihren Beitrag mit entsprechenden Tests und Dokumentation.
5. Reichen Sie einen Pull Request im entsprechenden Repository ein.

## Zusätzliche Ressourcen

- [MCP-Community-Projekte](https://github.com/topics/model-context-protocol)

---

Weiter: [Lektionen aus der frühen Einführung](../07-LessonsfromEarlyAdoption/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.