# Komunita a príspevky

[![Ako prispieť do MCP: Nástroje, dokumentácia, kód a viac](../../../translated_images/sk/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

## Prehľad

Táto lekcia sa zameriava na to, ako sa zapojiť do komunity MCP, prispieť do ekosystému MCP a dodržiavať osvedčené postupy pre spoluprácu pri vývoji. Pochopenie spôsobu účasti na open-source MCP projektoch je nevyhnutné pre tých, ktorí chcú formovať budúcnosť tejto technológie.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Pochopiť štruktúru komunity a ekosystému MCP
- Efektívne sa zapájať do fór a diskusií komunity MCP
- Prispievať do open-source repozitárov MCP
- Vytvárať a zdieľať vlastné nástroje a servery MCP
- Dodržiavať najlepšie praktiky pre vývoj a spoluprácu v MCP
- Objavovať zdroje a rámce komunity pre vývoj MCP

## Ekosystém komunity MCP

Ekosystém MCP pozostáva z rôznych komponentov a účastníkov, ktorí spolupracujú na rozvoji protokolu.

### Kľúčové komponenty komunity

1. **Hlavní správcovia protokolu**: Oficiálna [GitHub organizácia Model Context Protocol](https://github.com/modelcontextprotocol) spravuje základné špecifikácie a referenčné implementácie MCP
2. **Vývojári nástrojov**: Jednotlivci a tímy vytvárajúce nástroje a servery MCP
3. **Poskytovatelia integrácií**: Spoločnosti, ktoré integrujú MCP do svojich produktov a služieb
4. **Koncoví používatelia**: Vývojári a organizácie používajúce MCP vo svojich aplikáciách
5. **Prispievatelia**: Členovia komunity, ktorí prispievajú kódom, dokumentáciou alebo inými zdrojmi

### Zdroje komunity

#### Oficiálne kanály

- [GitHub organizácia MCP](https://github.com/modelcontextprotocol)
- [Dokumentácia MCP](https://modelcontextprotocol.io/)
- [Špecifikácia MCP](https://modelcontextprotocol.io/specification/2026-07-28/)
- [GitHub diskusie](https://github.com/orgs/modelcontextprotocol/discussions)
- [Repozitár príkladov a serverov MCP](https://github.com/modelcontextprotocol/servers)

#### Zdroje poháňané komunitou

- [Klienti MCP](https://modelcontextprotocol.io/clients) - Zoznam klientov podporujúcich integrácie MCP
- [Servery MCP komunity](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Rastúci zoznam serverov MCP vyvinutých komunitou
- [Awesome MCP servery](https://github.com/wong2/awesome-mcp-servers) - Kurátorský zoznam MCP serverov
- [PulseMCP](https://www.pulsemcp.com/) - Komunitné centrum a newsletter na objavovanie zdrojov MCP
- [Remote OpenClaw](https://www.remoteopenclaw.com/) - Bezplatný vyhľadávateľný adresár MCP serverov, schopností agentov a pluginov
- [Discord server](https://discord.gg/jHEGxQu2a5) - Spojte sa s vývojármi MCP
- SDK implementácie špecifické pre jazyky
- Blogové príspevky a návody

## Prispievanie do MCP

### Typy príspevkov

Ekosystém MCP víta rôzne typy príspevkov:

1. **Príspevky kódu**:
   - Vylepšenia základného protokolu
   - Opravy chýb
   - Implementácie nástrojov a serverov
   - Knižnice klient/server v rôznych jazykoch

2. **Dokumentácia**:
   - Zlepšovanie existujúcej dokumentácie
   - Vytváranie návodov a sprievodcov
   - Preklad dokumentácie
   - Vytváranie príkladov a vzorových aplikácií

3. **Podpora komunity**:
   - Odpovedanie na otázky vo fórach a diskusiách
   - Testovanie a hlásenie problémov
   - Organizovanie komunitných podujatí
   - Mentorovanie nových prispievateľov

### Proces príspevku: Základný protokol

Na prispievanie do základného MCP protokolu alebo oficiálnych implementácií dodržiavajte princípy z [oficiálnych pokynov na prispievanie](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Jednoduchosť a minimalizmus**: Špecifikácia MCP udržiava vysoký štandard pre pridávanie nových konceptov. Je jednoduchšie pridávať veci do špecifikácie než ich odstraňovať.

2. **Konkretizovaný prístup**: Zmeny v špecifikácii by mali vychádzať zo špecifických implementačných problémov, nie zo špekulatívnych myšlienok.

3. **Fázy návrhu**:
   - Definovať: Preskúmať problematiku, overiť, či aj iní používatelia MCP majú podobný problém
   - Prototíp: Vytvoriť príkladné riešenie a demonštrovať jeho praktickú použiteľnosť
   - Napísať: Na základe prototypu napísať návrh špecifikácie

### Nastavenie vývojového prostredia

```bash
# Vytvorte fork úložiska
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# Nainštalujte závislosti
npm install

# Pre zmeny schémy overte a vygenerujte schema.json:
npm run check:schema:ts
npm run generate:schema

# Pre zmeny dokumentácie
npm run check:docs
npm run format

# Náhľad dokumentácie lokálne (voliteľné):
npm run serve:docs
```

### Príklad: Príspevok opravou chyby

```javascript
// Pôvodný kód s chybou v typescript-sdk
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Chyba: Chýbajúca validácia vlastností
  // Súčasná implementácia:
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// Opravená implementácia v príspevku
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Vylepšená validácia
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### Príklad: Príspevok novým nástrojom do štandardnej knižnice

```python
# Príklad príspevku: Nástroj na spracovanie CSV dát pre štandardnú knižnicu MCP

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
            # Extrahovať parametre
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # Získať CSV dáta buď z priamych dát alebo URL
            df = await self._get_dataframe(request)
            
            # Spracovať na základe požadovanej operácie
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
        # Implementácia by zahŕňala rôzne transformácie
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

### Pokyny pre prispievanie

Aby ste úspešne prispeli do projektov MCP:

1. **Začnite malé**: Začnite dokumentáciou, opravami chýb alebo malými vylepšeniami
2. **Dodržiavajte štýl**: Dodržiavajte kódovacie štandardy projektu
3. **Píšte testy**: Zahrňte jednotkové testy pre vaše kódové príspevky
4. **Dokumentujte svoju prácu**: Pridajte jasnú dokumentáciu k novým funkciám alebo zmenám
5. **Predkladajte cielené pull requesty**: Držte pull requesty zamerané na jedno konkrétne riešenie alebo funkciu
6. **Reagujte na spätnú väzbu**: Buďte otvorení a promptní k spätnej väzbe k vašim príspevkom

### Príklad pracovného postupu príspevku

```bash
# Naklonujte repozitár
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# Vytvorte novú vetvu pre váš príspevok
git checkout -b feature/my-contribution

# Urobte svoje zmeny
# ...

# Spustite testy, aby ste zabezpečili, že vaše zmeny nepoškodia existujúcu funkcionalitu
npm test

# Commitnite svoje zmeny s popisnou správou
git commit -am "Fix validation in resource handler"

# Pushnite svoju vetvu do svojho fork
git push origin feature/my-contribution

# Vytvorte pull request zo svojej vetvy do hlavného repozitára
# Potom reagujte na spätnú väzbu a podľa potreby upravujte svoj PR
```

## Vytváranie a zdieľanie serverov MCP

Jedným z najcennejších spôsobov, ako prispieť do ekosystému MCP, je vytváranie a zdieľanie vlastných MCP serverov. Komunita už vyvinula stovky serverov pre rôzne služby a použitia.

### Rámce pre vývoj serverov MCP

K dispozícii je niekoľko rámcov, ktoré uľahčujú vývoj serverov MCP:

1. **Oficiálne SDK** (skontrolujte
    [dokumentáciu SDK](https://modelcontextprotocol.io/docs/sdk) pre každú
    podporovanú revíziu protokolu SDK):
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
   - [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
   - [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk)

2. **Rámce komunity**:
   - [MCP-Framework](https://mcp-framework.com/) - Budujte MCP servery s eleganciou a rýchlosťou v TypeScripte
   - [Dekoratívne MCP Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - MCP servery riadené anotáciami v Jave
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java rámec pre MCP servery
   - [Šablóna MCP servera pre Next.js](https://github.com/vercel-labs/mcp-for-next.js) - Štartovací projekt Next.js pre MCP servery

### Vývoj zdieľateľných nástrojov

#### Príklad .NET: Vytvorenie balíka zdieľateľných nástrojov

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

#### Príklad Java: Vytvorenie Maven balíka pre nástroje

```java
// konfiguračný súbor pom.xml pre zdieľateľný balík nástrojov MCP
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
        // Definícia schémy...
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            String location = request.getParameters().get("location").asText();
            int days = request.getParameters().has("days") ? 
                request.getParameters().get("days").asInt() : 3;
            
            // Volanie API počasia
            Map<String, Object> forecast = getForecast(location, days);
            
            // Vytvoriť odpoveď
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // Implementácia by volala API počasia
        // Zjednodušený príklad
        Map<String, Object> result = new HashMap<>();
        // Pridať dáta predpovede...
        return result;
    }
}

// Sestaviť a publikovať pomocou Maven
// mvn clean package
// mvn deploy
```

#### Príklad Python: Publikovanie balíka na PyPI

```python
# Adresárová štruktúra pre balík PyPI:
# mcp_nlp_tools/
# ├── LICENSE
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# Príklad setup.py
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

# Príklad implementácie NLP nástroja (sentiment_tool.py)
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # Načítať model analýzy sentimentu
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
            # Extrahovať parametre
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # Analyzovať sentiment
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # Naformátovať výsledok
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # Vrátiť výsledok
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# Na publikovanie:
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### Zdieľanie osvedčených postupov

Pri zdieľaní MCP nástrojov s komunitou:

1. **Kompletná dokumentácia**:
   - Dokumentujte účel, použitie a príklady
   - Vysvetlite parametre a návratové hodnoty
   - Dokumentujte všetky externé závislosti

2. **Spracovanie chýb**:
   - Implementujte robustné spracovanie chýb
   - Poskytujte užitočné chybové hlásenia
   - Správne riešte hraničné prípady

3. **Výkonové hľadiská**:
   - Optimalizujte rýchlosť aj využitie zdrojov
   - Implementujte caching, keď je to vhodné
   - Zvažujte škálovateľnosť

4. **Bezpečnosť**:
   - Používajte bezpečné API kľúče a overovanie
   - Validujte a sanitizujte vstupy
   - Implementujte obmedzenia frekvencie volaní externých API

5. **Testovanie**:
   - Zahrňte komplexné testovacie pokrytie
   - Testujte s rôznymi typmi vstupov a hraničnými prípadmi
   - Dokumentujte testovacie postupy

## Spolupráca komunity a najlepšie praktiky

Efektívna spolupráca je kľúčom k prosperujúcemu ekosystému MCP.

### Komunikačné kanály

- GitHub Issues a diskusie
- Microsoft Tech Community
- Discord a Slack kanály
- Stack Overflow (tag: `model-context-protocol` alebo `mcp`)

### Revízie kódu

Pri kontrole príspevkov do MCP:

1. **Jasnosť**: Je kód jasný a dobre zdokumentovaný?
2. **Správnosť**: Funguje podľa očakávaní?
3. **Konzistentnosť**: Dodržiava konvencie projektu?
4. **Kompletnosť**: Sú zahrnuté testy a dokumentácia?
5. **Bezpečnosť**: Existujú nejaké bezpečnostné obavy?

### Kompatibilita verzií

Pri vývoji pre MCP:

1. **Verzionovanie protokolu**: Dodržiavajte verzovanie MCP protokolu, ktorý váš nástroj podporuje
2. **Kompatibilita klientov**: Zvážte spätnú kompatibilitu
3. **Kompatibilita serverov**: Dodržiavajte pokyny pre implementáciu serverov
4. **Lámavé zmeny**: Jasne dokumentujte všetky lámavé zmeny

## Príklad komunitného projektu: MCP registrácia nástrojov

Významným príspevkom komunity by mohol byť vývoj verejnej registrácie nástrojov MCP.

```python
# Príklad schémy pre API registra nástrojov komunity

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# Modely pre register nástrojov
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

# FastAPI aplikácia pre register
app = FastAPI(title="MCP Tool Registry")

# Pamäťová databáza pre tento príklad
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

## Kľúčové zistenia

- Komunita MCP je rôznorodá a víta rôzne typy príspevkov
- Príspevky do MCP môžu byť od vylepšení základného protokolu po vlastné nástroje
- Dodržiavanie pokynov na prispievanie zvyšuje pravdepodobnosť akceptácie vášho PR
- Vytváranie a zdieľanie nástrojov MCP je cenný spôsob, ako zlepšiť ekosystém
- Spolupráca komunity je nevyhnutná pre rast a zlepšovanie MCP

## Cvičenie

1. Identifikujte oblasť v ekosystéme MCP, kde by ste mohli prispieť na základe svojich zručností a záujmov
2. Vytvorte fork repozitára MCP a nastavte si lokálne vývojové prostredie
3. Vytvorte malé vylepšenie, opravu chyby alebo nástroj, ktorý by prospel komunite
4. Dokumentujte svoj príspevok so správnymi testami a dokumentáciou
5. Predložte pull request do príslušného repozitára

## Ďalšie zdroje

- [Projekty komunity MCP](https://github.com/topics/model-context-protocol)

---

## Čo nasleduje

Ďalej: [Lekcie z rannej adopcie](../07-LessonsfromEarlyAdoption/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->