# Zajednica i doprinosi

[![Kako doprinijeti MCP-u: Alati, dokumentacija, kod i još mnogo toga](../../../translated_images/hr/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Kliknite na gornju sliku za pregled videozapisa ovog sata)_

## Pregled

Ova lekcija se fokusira na to kako se uključiti u MCP zajednicu, doprinositi MCP ekosustavu i pratiti najbolje prakse za suradnički razvoj. Razumijevanje načina sudjelovanja u otvorenim MCP projektima ključno je za one koji žele oblikovati budućnost ove tehnologije.

## Ciljevi učenja

Na kraju ove lekcije, moći ćete:

- Razumjeti strukturu MCP zajednice i ekosustava
- Učinkovito sudjelovati u MCP forumima i raspravama
- Doprinositi MCP open-source repozitorijima
- Stvarati i dijeliti prilagođene MCP alate i servere
- Pridržavati se najboljih praksi za MCP razvoj i suradnju
- Otkriti resurse i okvire zajednice za MCP razvoj

## MCP ekosustav zajednice

MCP ekosustav se sastoji od različitih komponenti i sudionika koji surađuju na napretku protokola.

### Ključne komponente zajednice

1. **Održavatelji osnovnog protokola**: Službena [Model Context Protocol GitHub organizacija](https://github.com/modelcontextprotocol) održava osnovne MCP specifikacije i referentne implementacije
2. **Razvijači alata**: Pojedinci i timovi koji stvaraju MCP alate i servere
3. **Pružatelji integracija**: Tvrtke koje integriraju MCP u svoje proizvode i usluge
4. **Krajnji korisnici**: Programeri i organizacije koji koriste MCP u svojim aplikacijama
5. **Suradnici**: Članovi zajednice koji doprinose kodom, dokumentacijom ili drugim resursima

### Resursi zajednice

#### Službeni kanali

- [MCP GitHub organizacija](https://github.com/modelcontextprotocol)
- [MCP dokumentacija](https://modelcontextprotocol.io/)
- [MCP specifikacija](https://modelcontextprotocol.io/specification/2026-07-28/)
- [GitHub rasprave](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP primjeri i repozitorij servera](https://github.com/modelcontextprotocol/servers)

#### Resursi zajednice

- [MCP klijenti](https://modelcontextprotocol.io/clients) - Popis klijenata koji podržavaju MCP integracije
- [Zajednički MCP serveri](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Rastući popis MCP servera koje je razvila zajednica
- [Awesome MCP serveri](https://github.com/wong2/awesome-mcp-servers) - Kurirani popis MCP servera
- [PulseMCP](https://www.pulsemcp.com/) - Čvorište zajednice i newsletter za otkrivanje MCP resursa
- [Remote OpenClaw](https://www.remoteopenclaw.com/) - Besplatni pretraživi imenik MCP servera, vještina agenata i dodataka
- [Discord server](https://discord.gg/jHEGxQu2a5) - Povežite se s MCP programerima
- SDK implementacije specifične za jezik
- Blog postovi i tutorijali

## Doprinos MCP-u

### Vrste doprinosa

MCP ekosustav pozdravlja razne vrste doprinosa:

1. **Doprinosi kodom**:
   - Poboljšanja osnovnog protokola
   - Popravci bugova
   - Implementacije alata i servera
   - Klijentske/server biblioteke na različitim jezicima

2. **Dokumentacija**:
   - Poboljšanje postojeće dokumentacije
   - Izrada tutorijala i vodiča
   - Prevođenje dokumentacije
   - Izrada primjera i uzoraka aplikacija

3. **Podrška zajednici**:
   - Odgovaranje na pitanja na forumima i raspravama
   - Testiranje i prijavljivanje problema
   - Organizacija zajedničkih događaja
   - Mentorstvo za nove suradnike

### Proces doprinosa: Osnovni protokol

Za doprinos osnovnom MCP protokolu ili službenim implementacijama, slijedite ove principe iz [službenih smjernica za doprinos](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Jednostavnost i minimalizam**: MCP specifikacija postavlja visoke standarde za dodavanje novih koncepata. Lakše je dodati stvari u specifikaciju nego ih ukloniti.

2. **Konkretan pristup**: Promjene u specifikaciji trebaju se temeljiti na specifičnim problemima implementacije, a ne na spekulativnim idejama.

3. **Faze prijedloga**:
   - Definiraj: Istražiti problem, potvrditi da drugi MCP korisnici imaju sličan problem
   - Prototip: Izraditi primjer rješenja i demonstrirati njegovu praktičnu primjenu
   - Napiši: Na temelju prototipa napisati prijedlog specifikacije

### Postavljanje razvojne okoline

```bash
# Napravi fork repozitorija
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# Instaliraj ovisnosti
npm install

# Za promjene u shemi, validiraj i generiraj schema.json:
npm run check:schema:ts
npm run generate:schema

# Za promjene u dokumentaciji
npm run check:docs
npm run format

# Pregledaj dokumentaciju lokalno (opcionalno):
npm run serve:docs
```

### Primjer: Doprinos popravku buga

```javascript
// Izvorni kod s greškom u typescript-sdk
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Greška: Nedostaje provjera svojstava
  // Trenutna implementacija:
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// Ispravljena implementacija u doprinose
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Poboljšana provjera
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### Primjer: Doprinos novom alatu u standardnu biblioteku

```python
# Primjer doprinosa: Alat za obradu CSV podataka za MCP standardnu biblioteku

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
            # Izvuci parametre
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # Dohvati CSV podatke bilo iz izravnih podataka ili URL-a
            df = await self._get_dataframe(request)
            
            # Obradi na temelju tražene operacije
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
        # Implementacija bi uključivala različite transformacije
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

### Smjernice za doprinos

Za uspješan doprinos MCP projektima:

1. **Počni s malim stvarima**: Počni s dokumentacijom, popravcima bugova ili malim poboljšanjima
2. **Slijedi vodič za stil**: Poštuj stil kodiranja i konvencije projekta
3. **Piši testove**: Uključi jedinicne testove za svoje kodne doprinose
4. **Dokumentiraj svoj rad**: Dodaj jasnu dokumentaciju za nove značajke ili promjene
5. **Podnesi ciljane PR-ove**: Drži pull requestove fokusiranim na jedan problem ili značajku
6. **Uključi se u povratne informacije**: Budi odzivan na povratne informacije o svojim doprinosima

### Primjer tijeka rada za doprinos

```bash
# Klonirajte spremište
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# Kreirajte novu granu za svoj doprinos
git checkout -b feature/my-contribution

# Napravite svoje promjene
# ...

# Pokrenite testove kako biste provjerili da vaše promjene ne narušavaju postojeću funkcionalnost
npm test

# Pošaljite svoje promjene s opisnom porukom
git commit -am "Fix validation in resource handler"

# Gurnite svoju granu na svoj fork
git push origin feature/my-contribution

# Kreirajte pull request sa svoje grane prema glavnom spremištu
# Zatim se uključite u povratne informacije i iterirajte na svom PR-u po potrebi
```

## Stvaranje i dijeljenje MCP servera

Jedan od najvrijednijih načina za doprinos MCP ekosustavu je stvaranje i dijeljenje prilagođenih MCP servera. Zajednica je već razvila stotine servera za različite usluge i slučajeve upotrebe.

### Okviri za razvoj MCP servera

Dostupno je nekoliko okvira koji pojednostavljuju razvoj MCP servera:

1. **Službeni SDK-ovi** (provjerite
    [dokumentaciju SDK-a](https://modelcontextprotocol.io/docs/sdk) za svaku
    verziju protokola koju SDK podržava):
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
   - [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
   - [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk)

2. **Okviri zajednice**:
   - [MCP-Framework](https://mcp-framework.com/) - Izgradite MCP servere s elegancijom i brzinom u TypeScriptu
   - [MCP deklarativni Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - MCP serveri vođeni anotacijama u Javi
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java okvir za MCP servere
   - [Next.js MCP Server predložak](https://github.com/vercel-labs/mcp-for-next.js) - Početni Next.js projekt za MCP servere

### Razvoj alata za dijeljenje

#### .NET primjer: Izrada paketa alata za dijeljenje

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

#### Java primjer: Izrada Maven paketa za alate

```java
// konfiguracija pom.xml za dijeljivi MCP alat paket
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
        // Definicija sheme...
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            String location = request.getParameters().get("location").asText();
            int days = request.getParameters().has("days") ? 
                request.getParameters().get("days").asInt() : 3;
            
            // Pozovi vremenski API
            Map<String, Object> forecast = getForecast(location, days);
            
            // Izgradi odgovor
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // Implementacija bi pozvala vremenski API
        // Pojednostavljeni primjer
        Map<String, Object> result = new HashMap<>();
        // Dodaj podatke o prognozi...
        return result;
    }
}

// Izgradi i objavi koristeći Maven
// mvn clean package
// mvn deploy
```

#### Python primjer: Objavljivanje PyPI paketa

```python
# Struktura direktorija za PyPI paket:
# mcp_nlp_tools/
# ├── LICENSE
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# Primjer setup.py
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

# Primjer implementacije NLP alata (sentiment_tool.py)
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # Učitaj model za analizu sentimenta
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
            # Izvuci parametre
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # Analiziraj sentiment
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # Formatiraj rezultat
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # Vrati rezultat
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# Za objavu:
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### Dijeljenje najboljih praksi

Kada dijelite MCP alate sa zajednicom:

1. **Potpuna dokumentacija**:
   - Dokumentirajte svrhu, uporabu i primjere
   - Objasnite parametre i povratne vrijednosti
   - Dokumentirajte sve vanjske ovisnosti

2. **Rukovanje greškama**:
   - Implementirajte robusno upravljanje greškama
   - Prikazujte korisne poruke o greškama
   - Pristupite rubnim slučajevima pažljivo

3. **Razmatranja performansi**:
   - Optimizirajte za brzinu i korištenje resursa
   - Implementirajte keširanje gdje je primjenjivo
   - Razmotrite skalabilnost

4. **Sigurnost**:
   - Koristite sigurne API ključeve i autentikaciju
   - Validirajte i sanitizirajte ulaze
   - Implementirajte ograničenje brzine za vanjske API pozive

5. **Testiranje**:
   - Uključite sveobuhvatno testiranje
   - Testirajte s različitim vrstama ulaza i rubnim slučajevima
   - Dokumentirajte testne procedure

## Suradnja u zajednici i najbolje prakse

Učinkovita suradnja ključ je za uspješan MCP ekosustav.

### Komunikacijski kanali

- GitHub Issues i Rasprave
- Microsoft Tech Community
- Discord i Slack kanali
- Stack Overflow (oznaka: `model-context-protocol` ili `mcp`)

### Pregledi koda

Kod pregleda MCP doprinosa:

1. **Jasnoća**: Je li kod jasan i dobro dokumentiran?
2. **Ispravnost**: Radi li očekivano?
3. **Dosljednost**: Pridržava li se konvencija projekta?
4. **Potpunost**: Jesu li uključeni testovi i dokumentacija?
5. **Sigurnost**: Postoje li sigurnosni problemi?

### Kompatibilnost verzija

Prilikom razvoja za MCP:

1. **Verzioniranje protokola**: Pridržavajte se verzije MCP protokola koju vaš alat podržava
2. **Kompatibilnost klijenta**: Uzmite u obzir povratnu kompatibilnost
3. **Kompatibilnost servera**: Slijedite smjernice za implementaciju servera
4. **Prekidajuće promjene**: Jasno dokumentirajte sve prekidajuće promjene

## Primjer zajedničkog projekta: Registar MCP alata

Važan doprinos zajednice mogao bi biti razvoj javnog registra za MCP alate.

```python
# Primjer sheme za API registar alata za zajednicu

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# Modeli za registar alata
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

# FastAPI aplikacija za registar
app = FastAPI(title="MCP Tool Registry")

# Memorijska baza podataka za ovaj primjer
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

## Ključne spoznaje

- MCP zajednica je raznolika i pozdravlja različite vrste doprinosa
- Doprinos MCP-u može biti od poboljšanja osnovnog protokola do prilagođenih alata
- Pridržavanje smjernica za doprinos povećava šanse da vaš PR bude prihvaćen
- Stvaranje i dijeljenje MCP alata vrijedan je način za unapređenje ekosustava
- Suradnja u zajednici ključna je za rast i poboljšanje MCP-a

## Vježba

1. Identificirajte područje u MCP ekosustavu gdje biste mogli doprinijeti svojim vještinama i interesima
2. Forkajte MCP repozitorij i postavite lokalno razvojno okruženje
3. Napravite malo poboljšanje, popravak buga ili alat koji bi koristio zajednici
4. Dokumentirajte svoj doprinos s odgovarajućim testovima i dokumentacijom
5. Podnesite pull request u odgovarajući repozitorij

## Dodatni resursi

- [Zajednički MCP projekti](https://github.com/topics/model-context-protocol)

---

## Što slijedi

Sljedeće: [Pouke iz ranog usvajanja](../07-LessonsfromEarlyAdoption/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->