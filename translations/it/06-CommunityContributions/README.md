# Comunità e Contributi

[![Come Contribuire a MCP: Strumenti, Documentazione, Codice e Altro](../../../translated_images/it/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Clicca sull'immagine sopra per vedere il video di questa lezione)_

## Panoramica

Questa lezione si concentra su come interagire con la comunità MCP, contribuire all'ecosistema MCP e seguire le migliori pratiche per lo sviluppo collaborativo. Comprendere come partecipare ai progetti open-source MCP è essenziale per chi desidera plasmare il futuro di questa tecnologia.

## Obiettivi di Apprendimento

Al termine di questa lezione, sarai in grado di:

- Comprendere la struttura della comunità e dell'ecosistema MCP
- Partecipare efficacemente ai forum e alle discussioni della comunità MCP
- Contribuire ai repository open-source MCP
- Creare e condividere strumenti e server MCP personalizzati
- Seguire le migliori pratiche per lo sviluppo e la collaborazione MCP
- Scoprire risorse e framework della comunità per lo sviluppo MCP

## L'Ecosistema della Comunità MCP

L'ecosistema MCP è composto da vari componenti e partecipanti che lavorano insieme per far progredire il protocollo.

### Componenti Chiave della Comunità

1. **Manutentori del Protocollo Core**: L'[organizzazione GitHub ufficiale Model Context Protocol](https://github.com/modelcontextprotocol) mantiene le specifiche core MCP e le implementazioni di riferimento
2. **Sviluppatori di Strumenti**: Individui e team che creano strumenti e server MCP
3. **Fornitori di Integrazione**: Aziende che integrano MCP nei loro prodotti e servizi
4. **Utenti Finali**: Sviluppatori e organizzazioni che usano MCP nelle loro applicazioni
5. **Contributori**: Membri della comunità che contribuiscono con codice, documentazione o altre risorse

### Risorse della Comunità

#### Canali Ufficiali

- [Organizzazione MCP su GitHub](https://github.com/modelcontextprotocol)
- [Documentazione MCP](https://modelcontextprotocol.io/)
- [Specifiche MCP](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Discussioni su GitHub](https://github.com/orgs/modelcontextprotocol/discussions)
- [Repository Esempi & Server MCP](https://github.com/modelcontextprotocol/servers)

#### Risorse Guidate dalla Comunità

- [Client MCP](https://modelcontextprotocol.io/clients) - Elenco di client che supportano integrazioni MCP
- [Server MCP della Comunità](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Elenco in crescita di server MCP sviluppati dalla comunità
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Elenco curato di server MCP
- [PulseMCP](https://www.pulsemcp.com/) - Hub della comunità e newsletter per scoprire risorse MCP
- [Remote OpenClaw](https://www.remoteopenclaw.com/) - Directory ricercabile gratuita di server MCP, skill agent e plugin
- [Server Discord](https://discord.gg/jHEGxQu2a5) - Collegati con sviluppatori MCP
- Implementazioni SDK specifiche per linguaggio
- Post di blog e tutorial

## Contribuire a MCP

### Tipi di Contributi

L'ecosistema MCP accoglie vari tipi di contributi:

1. **Contributi di Codice**:
   - Miglioramenti al protocollo core
   - Correzione di bug
   - Implementazioni di strumenti e server
   - Librerie client/server in diversi linguaggi

2. **Documentazione**:
   - Miglioramento della documentazione esistente
   - Creazione di tutorial e guide
   - Traduzione della documentazione
   - Creazione di esempi e applicazioni di esempio

3. **Supporto alla Comunità**:
   - Rispondere a domande su forum e discussioni
   - Testare e segnalare problemi
   - Organizzare eventi comunitari
   - Fare da mentore ai nuovi contribuenti

### Processo di Contributo: Protocollo Core

Per contribuire al protocollo core MCP o alle implementazioni ufficiali, segui questi principi delle [linee guida ufficiali per i contributi](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Semplicità e Minimalismo**: La specifica MCP mantiene un alto standard per l'aggiunta di nuovi concetti. È più facile aggiungere cose a una specifica che rimuoverle.

2. **Approccio Concreto**: Le modifiche alla specifica devono basarsi su sfide di implementazione specifiche, non su idee speculative.

3. **Fasi di una Proposta**:
   - Definire: Esplorare il problema, validare che altri utenti MCP affrontino un problema simile
   - Prototipare: Costruire una soluzione di esempio e dimostrare l'applicazione pratica
   - Scrivere: Basandosi sul prototipo, scrivere una proposta di specifica

### Configurazione dell'Ambiente di Sviluppo

```bash
# Crea un fork del repository
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# Installa le dipendenze
npm install

# Per modifiche allo schema, valida e genera schema.json:
npm run check:schema:ts
npm run generate:schema

# Per modifiche alla documentazione
npm run check:docs
npm run format

# Anteprima della documentazione in locale (opzionale):
npm run serve:docs
```

### Esempio: Contribuire con una Correzione di Bug

```javascript
// Codice originale con bug nel typescript-sdk
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Bug: Mancata validazione delle proprietà
  // Implementazione attuale:
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// Implementazione corretta in un contributo
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Validazione migliorata
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### Esempio: Contribuire con un Nuovo Strumento alla Libreria Standard

```python
# Esempio di contributo: Uno strumento di elaborazione dati CSV per la libreria standard MCP

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
            # Estrai parametri
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # Ottieni dati CSV da dati diretti o URL
            df = await self._get_dataframe(request)
            
            # Elabora in base all'operazione richiesta
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
        # L'implementazione includerebbe varie trasformazioni
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

### Linee Guida per il Contributo

Per fare un contributo di successo ai progetti MCP:

1. **Iniziare in piccolo**: Comincia con documentazione, correzioni di bug o piccoli miglioramenti
2. **Segui la Guida di Stile**: Rispetta lo stile di codifica e le convenzioni del progetto
3. **Scrivi Test**: Includi test unitari per i tuoi contributi di codice
4. **Documenta il tuo lavoro**: Aggiungi documentazione chiara per nuove funzionalità o modifiche
5. **Invia PR mirate**: Mantieni le pull request focalizzate su un singolo problema o funzionalità
6. **Interagisci con il Feedback**: Rispondi al feedback sui tuoi contributi

### Flusso di lavoro di contributo esempio

```bash
# Clona il repository
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# Crea un nuovo ramo per il tuo contributo
git checkout -b feature/my-contribution

# Apporta le tue modifiche
# ...

# Esegui i test per assicurarti che le modifiche non compromettano le funzionalità esistenti
npm test

# Fai il commit delle modifiche con un messaggio descrittivo
git commit -am "Fix validation in resource handler"

# Invia il tuo ramo al tuo fork
git push origin feature/my-contribution

# Crea una pull request dal tuo ramo al repository principale
# Poi interagisci con il feedback e itera sulla tua PR secondo necessità
```

## Creare e Condividere Server MCP

Uno dei modi più preziosi per contribuire all'ecosistema MCP è creare e condividere server MCP personalizzati. La comunità ha già sviluppato centinaia di server per vari servizi e casi d'uso.

### Framework per lo Sviluppo di Server MCP

Diversi framework sono disponibili per semplificare lo sviluppo di server MCP:

1. **SDK Ufficiali** (consulta la
    [documentazione SDK](https://modelcontextprotocol.io/docs/sdk) per ogni
    revisione del protocollo supportata dall'SDK):
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
   - [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
   - [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk)

2. **Framework della Comunità**:
   - [MCP-Framework](https://mcp-framework.com/) - Costruisci server MCP con eleganza e velocità in TypeScript
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Server MCP con annotazioni in Java
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Framework Java per server MCP
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Progetto starter Next.js per server MCP

### Sviluppare Strumenti Condivisibili

#### Esempio .NET: Creare un Pacchetto Strumento Condivisibile

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

#### Esempio Java: Creare un Pacchetto Maven per Strumenti

```java
// configurazione pom.xml per un pacchetto di strumenti MCP condivisibile
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
        // Definizione dello schema...
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            String location = request.getParameters().get("location").asText();
            int days = request.getParameters().has("days") ? 
                request.getParameters().get("days").asInt() : 3;
            
            // Chiamare l'API del meteo
            Map<String, Object> forecast = getForecast(location, days);
            
            // Costruire la risposta
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // L'implementazione chiamerebbe l'API del meteo
        // Esempio semplificato
        Map<String, Object> result = new HashMap<>();
        // Aggiungere dati meteo...
        return result;
    }
}

// Costruire e pubblicare usando Maven
// mvn clean package
// mvn deploy
```

#### Esempio Python: Pubblicare un Pacchetto PyPI

```python
# Struttura della directory per un pacchetto PyPI:
# mcp_nlp_tools/
# ├── LICENSE
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# Esempio di setup.py
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

# Esempio di implementazione di uno strumento NLP (sentiment_tool.py)
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # Carica il modello di analisi del sentiment
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
            # Estrai i parametri
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # Analizza il sentiment
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # Formattta il risultato
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # Restituisci il risultato
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# Per pubblicare:
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### Condivisione delle Migliori Pratiche

Quando condividi strumenti MCP con la comunità:

1. **Documentazione Completa**:
   - Documenta scopo, uso ed esempi
   - Spiega parametri e valori di ritorno
   - Documenta eventuali dipendenze esterne

2. **Gestione degli Errori**:
   - Implementa una robusta gestione degli errori
   - Fornisci messaggi di errore utili
   - Gestisci elegantemente i casi limite

3. **Considerazioni sulle Prestazioni**:
   - Ottimizza per velocità e uso delle risorse
   - Implementa caching quando appropriato
   - Considera la scalabilità

4. **Sicurezza**:
   - Usa chiavi API sicure e autenticazione
   - Valida e sanitizza input
   - Implementa limitazioni di velocità per chiamate API esterne

5. **Test**:
   - Includi una copertura di test completa
   - Testa con diversi tipi di input e casi limite
   - Documenta le procedure di test

## Collaborazione Comunitaria e Migliori Pratiche

La collaborazione efficace è la chiave per un ecosistema MCP prospero.

### Canali di Comunicazione

- Issue e Discussioni su GitHub
- Microsoft Tech Community
- Canali Discord e Slack
- Stack Overflow (tag: `model-context-protocol` o `mcp`)

### Revisioni del Codice

Quando revisioni contributi MCP:

1. **Chiarezza**: Il codice è chiaro e ben documentato?
2. **Correttezza**: Funziona come previsto?
3. **Coerenza**: Segue le convenzioni del progetto?
4. **Completezza**: Include test e documentazione?
5. **Sicurezza**: Ci sono preoccupazioni di sicurezza?

### Compatibilità delle Versioni

Quando sviluppi per MCP:

1. **Versionamento del Protocollo**: Attieniti alla versione del protocollo MCP supportata dal tuo strumento
2. **Compatibilità Client**: Considera la retrocompatibilità
3. **Compatibilità Server**: Segui le linee guida di implementazione server
4. **Modifiche Incompatibili**: Documenta chiaramente eventuali modifiche incompatibili

## Progetto Comunitario Esempio: Registro Strumenti MCP

Un contributo importante della comunità potrebbe essere lo sviluppo di un registro pubblico per strumenti MCP.

```python
# Esempio di schema per un'API di registro degli strumenti della comunità

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# Modelli per il registro degli strumenti
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

# Applicazione FastAPI per il registro
app = FastAPI(title="MCP Tool Registry")

# Database in memoria per questo esempio
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

## Punti Chiave

- La comunità MCP è diversificata e accoglie vari tipi di contributi
- Contribuire a MCP può spaziare da miglioramenti del protocollo core a strumenti personalizzati
- Seguire le linee guida per i contributi migliora le possibilità che la tua PR venga accettata
- Creare e condividere strumenti MCP è un modo prezioso per migliorare l'ecosistema
- La collaborazione comunitaria è essenziale per la crescita e il miglioramento di MCP

## Esercizio

1. Identifica un'area nell'ecosistema MCP dove potresti fare un contributo basato sulle tue competenze e interessi
2. Effettua il fork del repository MCP e configura un ambiente di sviluppo locale
3. Crea un piccolo miglioramento, correzione di bug o strumento che possa beneficiare la comunità
4. Documenta il tuo contributo con test e documentazione adeguati
5. Invia una pull request al repository appropriato

## Risorse Aggiuntive

- [Progetti della Comunità MCP](https://github.com/topics/model-context-protocol)

---

## Cosa Fare Dopo

Successivo: [Lezioni dall'Adozione Precoce](../07-LessonsfromEarlyAdoption/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->