# Kogukond ja panused

[![Kuidas panustada MCP-sse: tööriistad, dokumentatsioon, kood ja muud](../../../translated_images/et/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Klõpsake ülaloleval pildil, et vaadata selle õppetunni videot)_

## Ülevaade

See õppetund keskendub sellele, kuidas suhelda MCP kogukonnaga, panustada MCP ökosüsteemi ja järgida koostööl põhineva arenduse parimaid tavasid. Arusaamine sellest, kuidas osaleda avatud lähtekoodiga MCP projektides, on oluline neile, kes soovivad selle tehnoloogia tulevikku kujundada.

## Õpieesmärgid

Selle õppetunni lõpuks suudate:

- mõista MCP kogukonna ja ökosüsteemi struktuuri
- osaleda tõhusalt MCP kogukonna foorumites ja aruteludes
- panustada MCP avatud lähtekoodiga hoidlastesse
- luua ja jagada kohandatud MCP tööriistu ja servereid
- järgida MCP arenduse ja koostöö parimaid tavasid
- avastada kogukonna ressursse ja raamistikke MCP arenduseks

## MCP kogukonna ökosüsteem

MCP ökosüsteem koosneb erinevatest komponentidest ja osalejatest, kes töötavad koos protokolli arendamiseks.

### Olulised kogukonna komponendid

1. **Tuumikprotokolli hoidjad**: ametlik [Model Context Protocol GitHub organisatsioon](https://github.com/modelcontextprotocol) haldab MCP tuumikspetsifikatsioone ja viite rakendusi
2. **Tööriistaarendajad**: üksikisikud ja meeskonnad, kes loovad MCP tööriistu ja servereid
3. **Integratsioonipakkujad**: ettevõtted, kes integreerivad MCP oma toodetesse ja teenustesse
4. **Lõppkasutajad**: arendajad ja organisatsioonid, kes kasutavad MCP-d oma rakendustes
5. **Panustajad**: kogukonna liikmed, kes panustavad koodi, dokumentatsiooni või muid ressursse

### Kogukonna ressursid

#### Ametlikud kanalid

- [MCP GitHub organizzatsioon](https://github.com/modelcontextprotocol)
- [MCP dokumentatsioon](https://modelcontextprotocol.io/)
- [MCP spetsifikatsioon](https://modelcontextprotocol.io/specification/2026-07-28/)
- [GitHub arutelud](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP näidete ja serverite hoidla](https://github.com/modelcontextprotocol/servers)

#### Kogukonna juhitud ressursid

- [MCP kliendid](https://modelcontextprotocol.io/clients) - nimekiri klientidest, kes toetavad MCP integratsioone
- [Kogukonna MCP serverid](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - kasvav nimekiri kogukonna loodud MCP serveritest
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - kureeritud nimekiri MCP serveritest
- [PulseMCP](https://www.pulsemcp.com/) - kogukonnakeskus ja uudiskiri MCP ressursside avastamiseks
- [Remote OpenClaw](https://www.remoteopenclaw.com/) - tasuta otsitav kataloog MCP serveritest, agendioskustest ja pistikprogrammidest
- [Discord server](https://discord.gg/jHEGxQu2a5) - ühendus MCP arendajatega
- Keelespetsiifilised SDK rakendused
- Blogipostitused ja juhendid

## Panustamine MCP-sse

### Panuse tüübid

MCP ökosüsteem ootab erinevaid panuseid:

1. **Koodipanused**:
   - Tuumikprotokolli täiustused
   - Veaparandused
   - Tööriistade ja serverite rakendused
   - Kliendi/serveri teegid erinevates keeltes

2. **Dokumentatsioon**:
   - Olemasoleva dokumentatsiooni parandamine
   - Juhendite ja õpetuste loomine
   - Dokumentatsiooni tõlkimine
   - Näidete ja proovirakenduste loomine

3. **Kogukonna tugi**:
   - Küsitlustele vastamine foorumites ja aruteludes
   - Testimine ja probleemide raporteerimine
   - Kogukonnaürituste korraldamine
   - Uute panustajate juhendamine

### Panuse protsess: Tuumikprotokoll

Tuumik-MCP protokolli või ametlike rakenduste panustamiseks järgige neid põhimõtteid [ametlikest panustamisjuhistest](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Lihtsus ja minimalism**: MCP spetsifikatsioon seab kõrged nõuded uute kontseptsioonide lisamisel. On lihtsam spetsifikatsioonile asju lisada kui neid eemaldada.

2. **Konkreetne lähenemine**: Spetsifikatsiooni muudatused peaksid põhinema konkreetsetel rakendusprobleemidel, mitte spekulatiivsetel ideedel.

3. **Pakkumise etapid**:
   - Määratle: Uurige probleemivaldkonda, kinnitage, et teistel MCP kasutajatel on sarnane probleem
   - Prototüüp: Looge näidislahendus ja demonstreerige selle praktilist kasutust
   - Kirjutamine: Kirjutage spetsifikatsiooni ettepanek prototüübi põhjal

### Arenduskeskkonna seadistamine

```bash
# Tee selle hoidla kloon
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# Paigalda sõltuvused
npm install

# Skeemi muudatuste puhul valideeri ja genereeri schema.json:
npm run check:schema:ts
npm run generate:schema

# Dokumentatsiooni muudatuste jaoks
npm run check:docs
npm run format

# Eelvaata dokumentatsiooni lokaalselt (valikuline):
npm run serve:docs
```

### Näide: Veaparandusega panustamine

```javascript
// Originaalkood, milles on viga typescript-sdk-s
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Viga: Puudub omaduse valideerimine
  // Praegune teostus:
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// Parandatud teostus panustuses
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Täiustatud valideerimine
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### Näide: Uue tööriista panustamine standardteeki

```python
# Näide panusest: CSV andmetöötlustööriist MCP standardraamatukogule

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
            # Parameetrite väljavõtmine
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # Hangi CSV andmed kas otse andmetest või URL-ilt
            df = await self._get_dataframe(request)
            
            # Töötle taotletud toimingu alusel
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
        # Rakendus hõlmaks erinevaid teisendusi
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

### Panustamisjuhised

Eduka panuse tegemiseks MCP projektides:

1. **Alusta väikesest**: alusta dokumentatsioonist, veaparandustest või väikestest täiustustest
2. **Järgi stiilijuhist**: järgi projekti kodeerimisstiili ja konventsioone
3. **Kirjuta testid**: lisa oma koodipanustele ühiktestid
4. **Dokumenteeri oma töö**: lisa uusfunktsioonide või muudatuste selge dokumentatsioon
5. **Esita sihitud PR-e**: hoia tõmbepäringud keskendunud ühele probleemile või funktsioonile
6. **Ole valmis tagasisideks**: reageeri oma panustele tulevale tagasisidele

### Näidis panustamise töövoog

```bash
# Kopeeri hoidla
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# Loo uus haru oma panuse jaoks
git checkout -b feature/my-contribution

# Tee oma muudatused
# ...

# Käivita testid, et veenduda, et sinu muudatused ei katkesta olemasolevat funktsionaalsust
npm test

# Tee oma muudatustest commit kirjeldava sõnumiga
git commit -am "Fix validation in resource handler"

# Lükka oma haru oma fork'i
git push origin feature/my-contribution

# Loo pull request oma harust põhihoidlasse
# Seejärel suhtle tagasisidega ja täiusta oma PR-i vastavalt vajadusele
```

## MCP serverite loomine ja jagamine

Üks väärtuslikumaid viise panustada MCP ökosüsteemi on luua ja jagada kohandatud MCP servereid. Kogukond on juba arendanud sadu servereid erinevate teenuste ja kasutusjuhtude jaoks.

### MCP serveriarenduse raamistike valik

MCP serveri arenduse lihtsustamiseks on saadaval mitu raamistikke:

1. **Ametlikud SDK-d** (kontrolli
    [SDK dokumentatsiooni](https://modelcontextprotocol.io/docs/sdk) iga
    SDK toetatud protokollide versioonide kohta):
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
   - [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
   - [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk)

2. **Kogukonna raamistikud**:
   - [MCP-Framework](https://mcp-framework.com/) - ehitage MCP servereid elegantselt ja kiiresti TypeScriptis
   - [MCP deklaratiivne Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - annotatsioonidel põhinevad MCP serverid Java abil
   - [Quarkus MCP serveri SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java raamistik MCP serveritele
   - [Next.js MCP serveri mall](https://github.com/vercel-labs/mcp-for-next.js) - alustav Next.js projekt MCP serveritele

### Jagatavate tööriistade arendamine

#### .NET näide: jagatava tööriistapaketi loomine

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

#### Java näide: Maven paketi loomine tööriistadele

```java
// pom.xml konfiguratsioon jagatava MCP tööriistapaketi jaoks
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
            <url>https://maven.pkg.github.com/kasutajanimi/mcp-ilmatööriistad</url>
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
        // Skeemi definitsioon...
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            String location = request.getParameters().get("location").asText();
            int days = request.getParameters().has("days") ? 
                request.getParameters().get("days").asInt() : 3;
            
            // Kõneta ilma API-d
            Map<String, Object> forecast = getForecast(location, days);
            
            // Koosta vastus
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // Rakendus kutsuks ilma API-d
        // Lihtsustatud näide
        Map<String, Object> result = new HashMap<>();
        // Lisa prognoosi andmed...
        return result;
    }
}

// Koosta ja avalda kasutades Maveni
// mvn clean package
// mvn deploy
```

#### Python näide: PyPI paketi avaldamine

```python
# Kaustastruktuur PyPI paketile:
# mcp_nlp_tools/
# ├── LICENSE
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# Näide setup.py-st
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

# Näide NLP tööriista rakendusest (sentiment_tool.py)
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # Laadi sentimentide analüüsi mudel
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
            # Erista parameetrid
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # Analüüsi sentimenti
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # Vorminda tulemus
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # Tagasta tulemus
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# Avaldamiseks:
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### Parimate tavade jagamine

MCP tööriistade kogukonnaga jagamisel:

1. **Täielik dokumentatsioon**:
   - Kirjelda eesmärki, kasutust ja näiteid
   - Selgita parameetreid ja tagastatavaid väärtusi
   - Dokumenteeri kõik välised sõltuvused

2. **Vea käsitlemine**:
   - Rakenda korralik vea käsitlemine
   - Paku kasulikke veateateid
   - Käsitle äärejuhtumeid sujuvalt

3. **Jõudluse kaalutlused**:
   - Optimeeri nii kiiruse kui ressursikasutuse osas
   - Rakenda vajadusel vahemälu kasutust
   - Mõtle skaleeritavusele

4. **Turvalisus**:
   - Kasuta turvalisi API võtmeid ja autentimist
   - Kontrolli ja puhasta sisendeid
   - Rakenda väliste API kõnede kiirusepiirangut

5. **Testimine**:
   - Kaasa põhjalik testide katvus
   - Testi erinevate sisenditüüpide ja äärejuhtumitega
   - Dokumenteeri testimise protseduurid

## Kogukonna koostöö ja parimad tavad

Tõhus koostöö on eluliselt oluline eduka MCP ökosüsteemi jaoks.

### Suhtluskanalid

- GitHub probleemid ja arutelud
- Microsoft Tech Community
- Discord ja Slack kanalid
- Stack Overflow (silt: `model-context-protocol` või `mcp`)

### Koodi ülevaated

MCP panuseid üle vaadates:

1. **Selgus**: Kas kood on selge ja hästi dokumenteeritud?
2. **Õigsus**: Kas see töötab ootuspäraselt?
3. **Järjepidevus**: Kas see järgib projekti konventsioone?
4. **Täielikkus**: Kas kaasatud on testid ja dokumentatsioon?
5. **Turvalisus**: Kas on turvariske?

### Versioonide ühilduvus

MCP jaoks arendades:

1. **Protokolli versioonimine**: järgi MCP protokolli versiooni, mida sinu tööriist toetab
2. **Kliendi ühilduvus**: arvestada tagurpidi ühilduvusega
3. **Serveri ühilduvus**: järgi serveri rakenduse juhiseid
4. **Katkestavad muudatused**: dokumenteeri selgelt kõik katkestavad muudatused

## Näidis kogukonnaprojekt: MCP tööriistade register

Oluline kogukonna panus võib olla avaliku MCP tööriistaregistri väljatöötamine.

```python
# Ühiskonna tööriistade registri API näidisskeem

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# Tööriistaregistri mudelid
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

# Registri FastAPI rakendus
app = FastAPI(title="MCP Tool Registry")

# Selle näite jaoks mälus olev andmebaas
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

## Peamised võtmed

- MCP kogukond on mitmekesine ja ootab erinevat tüüpi panuseid
- Panustamine MCP-sse võib ulatuda tuumikprotokolli täiustustest kohandatud tööriistadeni
- Panustamisjuhiste järgimine parandab tõenäosust, et sinu tõmbepäring aktsepteeritakse
- MCP tööriistade loomine ja jagamine on ökosüsteemi rikastamise oluline viis
- Kogukonna koostöö on MCP kasvu ja arengut toetav oluline tegur

## Harjutus

1. Määrake MCP ökosüsteemis valdkond, kus saaksite oma oskuste ja huvide järgi panustada
2. Forkige MCP hoidla ja seadistage kohalik arenduskeskkond
3. Looge väike täiustus, veaparandus või tööriist, mis oleks kogukonnale kasulik
4. Dokumenteerige oma panus vastavate testide ja dokumentatsiooniga
5. Esitage tõmbepäring sobivasse hoidlasu

## Lisavressursid

- [MCP kogukonnaprojektid](https://github.com/topics/model-context-protocol)

---

## Mis järgmiseks

Järgmine: [Õppetunnid varajasest kasutuselevõtust](../07-LessonsfromEarlyAdoption/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->