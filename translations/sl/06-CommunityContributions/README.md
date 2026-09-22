# Skupnost in prispevki

[![Kako prispevati k MCP: orodja, dokumentacija, koda in več](../../../translated_images/sl/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Kliknite zgornjo sliko za ogled posnetka tega predavanja)_

## Pregled

To predavanje se osredotoča na to, kako se vključiti v MCP skupnost, prispevati k MCP ekosistemu in slediti najboljšim praksam za sodelovalni razvoj. Razumevanje, kako sodelovati v odprtokodnih MCP projektih, je ključnega pomena za tiste, ki želijo oblikovati prihodnost te tehnologije.

## Cilji učenja

Do konca tega predavanja boste lahko:

- Razumeli strukturo MCP skupnosti in ekosistema
- Učinkovito sodelovali v MCP forumih in razpravah v skupnosti
- Prispevali k odprtokodnim MCP repozitorijem
- Ustvarjali in delili prilagojena MCP orodja in strežnike
- Sledili najboljšim praksam za razvoj in sodelovanje pri MCP
- Odkrijete vire in okvire skupnosti za razvoj MCP

## MCP Skupnostni ekosistem

MCP ekosistem sestavljajo različne komponente in udeleženci, ki skupaj delajo na napredovanju protokola.

### Ključne sestavine skupnosti

1. **Vzdrževalci jedra protokola**: uradna [Model Context Protocol GitHub organizacija](https://github.com/modelcontextprotocol) vzdržuje jedrne MCP specifikacije in referenčne implementacije
2. **Razvijalci orodij**: posamezniki in ekipe, ki ustvarjajo MCP orodja in strežnike
3. **Ponudniki integracij**: podjetja, ki integrirajo MCP v svoje izdelke in storitve
4. **Končni uporabniki**: razvijalci in organizacije, ki uporabljajo MCP v svojih aplikacijah
5. **Prispevkarji**: člani skupnosti, ki prispevajo kodo, dokumentacijo ali druge vire

### Viri skupnosti

#### Uradni kanali

- [MCP GitHub organizacija](https://github.com/modelcontextprotocol)
- [MCP dokumentacija](https://modelcontextprotocol.io/)
- [MCP specifikacija](https://modelcontextprotocol.io/specification/2026-07-28/)
- [GitHub razprave](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP primeri in repozitorij strežnikov](https://github.com/modelcontextprotocol/servers)

#### Viri, ki jih vodi skupnost

- [MCP odjemalci](https://modelcontextprotocol.io/clients) - seznam odjemalcev, ki podpirajo MCP integracije
- [Skupnostni MCP strežniki](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - rastoči seznam skupnostno razvijanih MCP strežnikov
- [Odlični MCP strežniki](https://github.com/wong2/awesome-mcp-servers) - kuriran seznam MCP strežnikov
- [PulseMCP](https://www.pulsemcp.com/) - skupnostni center in bilten za odkrivanje MCP virov
- [Remote OpenClaw](https://www.remoteopenclaw.com/) - brezplačen iskalni imenik MCP strežnikov, agentnih spretnosti in vtičnikov
- [Discord strežnik](https://discord.gg/jHEGxQu2a5) - povezava z MCP razvijalci
- SDK implementacije po jezikih
- Blog objave in vodiči

## Prispevanje k MCP

### Vrste prispevkov

MCP ekosistem sprejema različne vrste prispevkov:

1. **Prispevki kode**:
   - Izboljšave jedrnega protokola
   - Popravki napak
   - Implementacije orodij in strežnikov
   - Knjižnice za odjemalce/strežnike v različnih jezikih

2. **Dokumentacija**:
   - Izboljševanje obstoječe dokumentacije
   - Ustvarjanje vodičev in navodil
   - Prevajanje dokumentacije
   - Ustvarjanje primerov in vzorčnih aplikacij

3. **Podpora skupnosti**:
   - Odgovarjanje na vprašanja na forumih in razpravah
   - Testiranje in poročanje o težavah
   - Organizacija dogodkov skupnosti
   - Mentorstvo novim prispevkarjem

### Proces prispevka: jedrni protokol

Za prispevanje k jedrnemu MCP protokolu ali uradnim implementacijam sledite načelom iz [uradnih smernic za prispevanje](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Preprostost in minimalizem**: MCP specifikacija zahteva visok standard za dodajanje novih konceptov. Lažje je nekaj dodati kot odstraniti.

2. **Konkretni pristop**: Spremembe specifikacije naj temeljijo na konkretnih implementacijskih izzivih, ne na teoretičnih idejah.

3. **Faze predloga**:
   - Določitev: Raziskovanje problema, preverjanje, da imajo tudi drugi uporabniki MCP podoben izziv
   - Prototip: Izdelava primerne rešitve in prikaz njene praktične uporabe
   - Pisanje: Na podlagi prototipa napisati predlog specifikacije

### Nastavitev razvojnega okolja

```bash
# Razveji repozitorij
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# Namesti odvisnosti
npm install

# Za spremembe sheme, preveri in generiraj schema.json:
npm run check:schema:ts
npm run generate:schema

# Za spremembe dokumentacije
npm run check:docs
npm run format

# Lokalni predogled dokumentacije (izbirno):
npm run serve:docs
```

### Primer: prispevek z odpravo napake

```javascript
// Izvorna koda z napako v typescript-sdk
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Napaka: Manjkajoča validacija lastnosti
  // Trenutna izvedba:
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// Popravljena izvedba v prispevku
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Izboljšana validacija
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### Primer: prispevek novega orodja v standardno knjižnico

```python
# Primer prispevka: Orodje za obdelavo CSV podatkov za knjižnico MCP standarda

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
            # Izvleci parametre
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # Pridobi CSV podatke bodisi iz neposrednih podatkov ali URL
            df = await self._get_dataframe(request)
            
            # Obdelaj na podlagi zahtevane operacije
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
        # Implementacija bi vključevala različne transformacije
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

Za uspešno prispevanje k MCP projektom:

1. **Začnite z majhnim**: Začnite z dokumentacijo, popravki napak ali manjšimi izboljšavami
2. **Sledite slogovnemu vodniku**: Upoštevajte stil in konvencije kode projekta
3. **Pišite teste**: Vključite enotne teste za svoje prispevke kode
4. **Dokumentirajte svoje delo**: Dodajte jasno dokumentacijo za nove funkcije ali spremembe
5. **Oddajte ciljno usmerjene Pull Request-e**: Ohranite Pull Request osredotočen na eno težavo ali funkcijo
6. **Sodelujte pri povratnih informacijah**: Bodite odzivni na povratne informacije o vaših prispevkih

### Primer delovnega procesa prispevka

```bash
# Klonirajte repozitorij
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# Ustvarite novo vejo za svoj prispevek
git checkout -b feature/my-contribution

# Naredite svoje spremembe
# ...

# Zaženite teste, da zagotovite, da vaše spremembe ne pokvarijo obstoječe funkcionalnosti
npm test

# Potrdite svoje spremembe z opisnim sporočilom
git commit -am "Fix validation in resource handler"

# Potisnite svojo vejo v svoj fork
git push origin feature/my-contribution

# Ustvarite pull request iz svoje veje v glavni repozitorij
# Nato se odzovite na povratne informacije in po potrebi iterirajte svoj PR
```

## Ustvarjanje in deljenje MCP strežnikov

Eden najbolj dragocenih načinov prispevka k MCP ekosistemu je ustvarjanje in deljenje prilagojenih MCP strežnikov. Skupnost je že razvila na stotine strežnikov za različne storitve in primere uporabe.

### Okviri za razvoj MCP strežnikov

Na voljo je več ogrodij za poenostavitev razvoja MCP strežnikov:

1. **Uradni SDK-ji** (preverite
    [dokumentacijo SDK](https://modelcontextprotocol.io/docs/sdk) za vsak
    SDK glede podprtih revizij protokola):
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
   - [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
   - [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk)

2. **Okviri skupnosti**:
   - [MCP-Framework](https://mcp-framework.com/) - gradnja MCP strežnikov s prefinjenostjo in hitrostjo v TypeScriptu
   - [MCP deklarativni Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - anotacijsko vodeni MCP strežniki v Javi
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java okvir za MCP strežnike
   - [Next.js MCP strežnik predloga](https://github.com/vercel-labs/mcp-for-next.js) - začetni Next.js projekt za MCP strežnike

### Razvijanje orodij za deljenje

#### .NET primer: ustvarjanje paketa za deljenje orodij

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

#### Java primer: ustvarjanje Maven paketa za orodja

```java
// pom.xml konfiguracija za deljiv paket orodij MCP
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
            <url>https://maven.pkg.github.com/uporabniško_ime/mcp-weather-tools</url>
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
            
            // Pokliči vremenski API
            Map<String, Object> forecast = getForecast(location, days);
            
            // Ustvari odziv
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // Implementacija bi poklicala vremenski API
        // Poenostavljen primer
        Map<String, Object> result = new HashMap<>();
        // Dodaj podatke o napovedi...
        return result;
    }
}

// Gradnja in objava z Mavenom
// mvn clean package
// mvn deploy
```

#### Python primer: objava paketa na PyPI

```python
# Struktura imenikov za paket PyPI:
# mcp_nlp_tools/
# ├── LICENSE
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# Primer setup.py
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

# Primer implementacije orodja NLP (sentiment_tool.py)
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # Naloži model za analizo sentimenta
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
            # Izvleci parametre
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # Analiziraj sentiment
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # Oblikuj rezultat
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # Vrni rezultat
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# Za objavo:
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### Deljenje najboljših praks

Pri deljenju MCP orodij s skupnostjo:

1. **Popolna dokumentacija**:
   - Dokumentirajte namen, uporabo in primere
   - Razložite parametre in vrnjene vrednosti
   - Dokumentirajte vse zunanje odvisnosti

2. **Ravnanje z napakami**:
   - Implementirajte robustno upravljanje napak
   - Zagotovite uporabna sporočila o napakah
   - Ustrezno obravnavajte robne primere

3. **Izvedbena razmišljanja**:
   - Optimizirajte za hitrost in uporabo virov
   - Po potrebi implementirajte predpomnjenje
   - Upoštevajte razširljivost

4. **Varnost**:
   - Uporabljajte varne API ključe in avtentikacijo
   - Validirajte in očistite vnose
   - Implementirajte omejevanje hitrosti za zunanje API klice

5. **Testiranje**:
   - Vključite obsežno testno pokritost
   - Testirajte z različnimi vrstami vhodov in robnimi primeri
   - Dokumentirajte testne postopke

## Sodelovanje skupnosti in najboljše prakse

Učinkovito sodelovanje je ključ do uspevajočega MCP ekosistema.

### Kanali komunikacije

- GitHub Issues in razprave
- Microsoft Tech Community
- Discord in Slack kanali
- Stack Overflow (oznaka: `model-context-protocol` ali `mcp`)

### Pregledi kode

Pri pregledu MCP prispevkov:

1. **Jasnost**: Je koda jasna in dobro dokumentirana?
2. **Pravilnost**: Ali deluje tako, kot je pričakovano?
3. **Doslednost**: Ali sledi konvencijam projekta?
4. **Popolnost**: Ali so vključeni testi in dokumentacija?
5. **Varnost**: Ali obstajajo kakšne varnostne skrbi?

### Združljivost različic

Pri razvoju za MCP:

1. **Verzija protokola**: Upoštevajte verzijo MCP protokola, ki jo vaše orodje podpira
2. **Združljivost z odjemalci**: Upoštevajte združljivost nazaj
3. **Združljivost s strežniki**: Sledite smernicam za implementacijo strežnikov
4. **Prelomne spremembe**: Jasno dokumentirajte vse prelomne spremembe

## Primer skupnostnega projekta: MCP register orodij

Pomemben prispevek skupnosti bi lahko bil razvoj javnega registra za MCP orodja.

```python
# Primer sheme za API registra orodij skupnosti

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# Modeli za register orodij
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

# FastAPI aplikacija za register
app = FastAPI(title="MCP Tool Registry")

# Baza podatkov v pomnilniku za ta primer
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

## Ključna spoznanja

- MCP skupnost je raznolika in sprejema različne vrste prispevkov
- Prispevanje k MCP lahko sega od izboljšav jedrnega protokola do prilagojenih orodij
- Sledenje smernicam prispevkov poveča možnosti za sprejem vašega PR
- Ustvarjanje in deljenje MCP orodij je dragocen način za izboljšanje ekosistema
- Sodelovanje skupnosti je bistveno za rast in izboljšave MCP

## Vaja

1. Identificirajte področje v MCP ekosistemu, kjer lahko prispevate glede na svoje veščine in interese
2. Naredite fork MCP repozitorija in nastavite lokalno razvojno okolje
3. Ustvarite majhno izboljšavo, odpravo napake ali orodje, ki bi koristilo skupnosti
4. Dokumentirajte svoj prispevek s primernimi testi in dokumentacijo
5. Oddajte pull request v ustrezni repozitorij

## Dodatni viri

- [MCP skupnostni projekti](https://github.com/topics/model-context-protocol)

---

## Kaj sledi

Naslednje: [Lekcije iz zgodnje uporabe](../07-LessonsfromEarlyAdoption/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->