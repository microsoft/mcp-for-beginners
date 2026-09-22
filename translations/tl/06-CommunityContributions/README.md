# Komunidad at mga Ambag

[![Paano Mag-ambag sa MCP: Mga Kasangkapan, Dokumento, Code at Higit Pa](../../../translated_images/tl/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

## Pangkalahatang-Ideya

Ang araling ito ay nakatuon sa kung paano makisali sa komunidad ng MCP, mag-ambag sa ekosistema ng MCP, at sundin ang mga pinakamahusay na kasanayan para sa kolaboratibong pag-unlad. Mahalaga ang pag-unawa kung paano makilahok sa mga proyekto ng open-source MCP para sa mga nais hubugin ang hinaharap ng teknolohiyang ito.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Maunawaan ang estruktura ng komunidad at ekosistema ng MCP
- Mabisang makilahok sa mga forum at talakayan ng komunidad ng MCP
- Mag-ambag sa mga open-source na repositoryo ng MCP
- Lumikha at magbahagi ng mga custom na kasangkapan at server ng MCP
- Sundin ang mga pinakamahusay na kasanayan para sa pag-unlad at kolaborasyon ng MCP
- Tuklasin ang mga mapagkukunan at mga framework ng komunidad para sa pag-unlad ng MCP

## Ang Ekosistema ng Komunidad ng MCP

Binubuo ang ekosistema ng MCP ng iba't ibang mga bahagi at kalahok na nagtutulungan upang isulong ang protocol.

### Mga Pangunahing Sangkap ng Komunidad

1. **Mga Tagapangasiwa ng Core Protocol**: Ang opisyal na [Model Context Protocol GitHub organization](https://github.com/modelcontextprotocol) ang nangangasiwa ng mga pangunahing espesipikasyon ng MCP at mga reference implementation
2. **Mga Developer ng Kasangkapan**: Mga indibidwal at koponan na lumilikha ng mga kasangkapan at server ng MCP
3. **Mga Tagapagbigay ng Integrasyon**: Mga kumpanya na nag-iintegrate ng MCP sa kanilang mga produkto at serbisyo
4. **Mga End User**: Mga developer at organisasyon na gumagamit ng MCP sa kanilang mga aplikasyon
5. **Mga Nag-aambag**: Mga kasapi ng komunidad na nag-aambag ng code, dokumentasyon, o iba pang mga mapagkukunan

### Mga Mapagkukunan ng Komunidad

#### Mga Opisyal na Channel

- [MCP GitHub Organization](https://github.com/modelcontextprotocol)
- [MCP Dokumentasyon](https://modelcontextprotocol.io/)
- [Espesipikasyon ng MCP](https://modelcontextprotocol.io/specification/2026-07-28/)
- [GitHub Mga Talakayan](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP Mga Halimbawa at Repositoryo ng mga Server](https://github.com/modelcontextprotocol/servers)

#### Mga Mapagkukunang Pinangungunahan ng Komunidad

- [MCP Clients](https://modelcontextprotocol.io/clients) - Listahan ng mga kliyenteng sumusuporta sa mga integrasyon ng MCP
- [Community MCP Servers](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Lumalaking listahan ng mga MCP server na binuo ng komunidad
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Napiling listahan ng mga MCP server
- [PulseMCP](https://www.pulsemcp.com/) - Hub at newsletter ng komunidad para sa pagtuklas ng mga mapagkukunan ng MCP
- [Remote OpenClaw](https://www.remoteopenclaw.com/) - Libreng direktoryo na maaaring hanapin ng mga MCP server, kakayahan ng ahente, at plugins
- [Discord Server](https://discord.gg/jHEGxQu2a5) - Makipag-ugnayan sa mga developer ng MCP
- Mga implementasyon ng SDK na partikular sa wika
- Mga blog post at tutorial

## Pag-aambag sa MCP

### Mga Uri ng Ambag

Tinatanggap ng ekosistema ng MCP ang iba't ibang uri ng ambag:

1. **Mga Ambag sa Code**:
   - Mga pagpapahusay sa core protocol
   - Pagwawasto ng bug
   - Implementasyon ng mga kasangkapan at server
   - Mga client/server na library sa iba't ibang mga wika

2. **Dokumentasyon**:
   - Pagpapabuti ng umiiral na dokumentasyon
   - Paggawa ng mga tutorial at gabay
   - Pagsasalin ng dokumentasyon
   - Paggawa ng mga halimbawa at sample na aplikasyon

3. **Suporta sa Komunidad**:
   - Pagsagot sa mga tanong sa mga forum at talakayan
   - Pagtitiyak at pag-uulat ng mga isyu
   - Pag-oorganisa ng mga kaganapan sa komunidad
   - Paggabay sa mga bagong nag-aambag

### Proseso ng Pag-aambag: Core Protocol

Upang mag-ambag sa core MCP protocol o opisyal na mga implementasyon, sundin ang mga prinsipyo mula sa [opisyal na gabay sa pag-aambag](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Kasimplehan at Minimalismo**: Pinapanatili ng espesipikasyon ng MCP ang mataas na pamantayan para sa pagdagdag ng mga bagong konsepto. Mas madali ang magdagdag kaysa mag-alis sa isang espesipikasyon.

2. **Konkretong Lapit**: Ang mga pagbabago sa espesipikasyon ay dapat nakabase sa mga partikular na hamon sa implementasyon, hindi sa haka-haka.

3. **Mga Yugto ng Proposal**:
   - Tukuyin: Tuklasin ang problema, tiyakin na nakakaranas rin ng parehong isyu ang ibang mga user ng MCP
   - Gumawa ng Prototype: Bumuo ng isang halimbawa ng solusyon at ipakita ang praktikal na aplikasyon nito
   - Isulat: Batay sa prototype, isulat ang isang proposal para sa espesipikasyon

### Pag-setup ng Kapaligiran sa Pag-unlad

```bash
# I-fork ang repositoryo
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# I-install ang mga dependency
npm install

# Para sa mga pagbabago sa schema, i-validate at gumawa ng schema.json:
npm run check:schema:ts
npm run generate:schema

# Para sa mga pagbabago sa dokumentasyon
npm run check:docs
npm run format

# I-preview ang dokumentasyon nang lokal (opsyonal):
npm run serve:docs
```

### Halimbawa: Pag-aambag ng Pagwawasto ng Bug

```javascript
// Orihinal na code na may bug sa typescript-sdk
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Bug: Nawawalang pag-validate ng property
  // Kasalukuyang implementasyon:
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// Naayos na implementasyon sa isang kontribusyon
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Pinahusay na pag-validate
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### Halimbawa: Pag-aambag ng Bagong Kasangkapan sa Standard Library

```python
# Halimbawang kontribusyon: Isang kasangkapang nagpoproseso ng datos na CSV para sa MCP standard library

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
            # Kunin ang mga parametro
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # Kuhanin ang datos ng CSV mula sa direktang datos o URL
            df = await self._get_dataframe(request)
            
            # Iproseso base sa hinihinging operasyon
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
        # Kasama sa implementasyon ang iba't ibang pagbabago
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

### Mga Panuntunan sa Pag-aambag

Upang magkaroon ng matagumpay na pag-aambag sa mga proyekto ng MCP:

1. **Magsimula Maliit**: Simulan sa dokumentasyon, pag-aayos ng bug, o maliliit na pagpapabuti
2. **Sundin ang Style Guide**: Sundin ang estilo ng coding at mga konbensiyon ng proyekto
3. **Sumulat ng mga Test**: Isama ang unit tests para sa iyong mga ambag sa code
4. **Idokumento ang Iyong Trabaho**: Magdagdag ng malinaw na dokumentasyon para sa mga bagong tampok o pagbabago
5. **Mag-submit ng Targeted PRs**: Panatilihing nakatuon ang mga pull request sa isang isyu o tampok lamang
6. **Makipag-ugnayan sa Feedback**: Maging bukas at tumugon sa mga puna tungkol sa iyong mga ambag

### Halimbawa ng Daloy ng Pag-aambag

```bash
# Kopyahin ang repositoryo
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# Gumawa ng bagong sangay para sa iyong kontribusyon
git checkout -b feature/my-contribution

# Gawin ang iyong mga pagbabago
# ...

# Patakbuhin ang mga pagsusulit upang matiyak na ang iyong mga pagbabago ay hindi sisira sa kasalukuyang functionality
npm test

# I-commit ang iyong mga pagbabago na may malinaw na mensahe
git commit -am "Fix validation in resource handler"

# I-push ang iyong sangay sa iyong fork
git push origin feature/my-contribution

# Gumawa ng pull request mula sa iyong sangay papunta sa pangunahing repositoryo
# Pagkatapos ay makipag-ugnayan sa feedback at ulitin ang iyong PR kung kinakailangan
```

## Paglikha at Pagbabahagi ng mga MCP Server

Isa sa mga pinakamahalagang paraan upang mag-ambag sa ekosistema ng MCP ay sa pamamagitan ng paglikha at pagbabahagi ng mga custom na MCP server. Nakabuo na ang komunidad ng daan-daang server para sa iba't ibang serbisyo at gamit.

### Mga Framework sa Pag-develop ng MCP Server

May ilang mga framework na magpapadali sa pag-develop ng MCP server:

1. **Opisyal na SDK** (tingnan ang
    [dokumentasyon ng SDK](https://modelcontextprotocol.io/docs/sdk) para sa bawat
    protocol revisions na sinusuportahan ng SDK):
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
   - [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
   - [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk)

2. **Mga Framework ng Komunidad**:
   - [MCP-Framework](https://mcp-framework.com/) - Gumawa ng MCP server nang elegante at mabilis gamit ang TypeScript
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Annotation-driven MCP server gamit ang Java
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Java framework para sa MCP server
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Starter Next.js project para sa MCP server

### Pag-develop ng Mga Kasangkapang Maaaring Ibahagi

#### Halimbawa sa .NET: Paglikha ng Package ng Kasangka pang-Ibahagi

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

#### Halimbawa sa Java: Paglikha ng Maven Package para sa Mga Kasangkapan

```java
// pom.xml na konfigurasyon para sa isang maibabahaging MCP tool package
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
        // Kahulugan ng schema...
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            String location = request.getParameters().get("location").asText();
            int days = request.getParameters().has("days") ? 
                request.getParameters().get("days").asInt() : 3;
            
            // Tawagan ang weather API
            Map<String, Object> forecast = getForecast(location, days);
            
            // Buuin ang tugon
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // Ang implementasyon ay tatawag sa weather API
        // Pinadaling halimbawa
        Map<String, Object> result = new HashMap<>();
        // Magdagdag ng forecast data...
        return result;
    }
}

// Buuin at i-publish gamit ang Maven
// mvn clean package
// mvn deploy
```

#### Halimbawa sa Python: Paglalathala ng PyPI Package

```python
# Istruktura ng direktoryo para sa isang PyPI package:
# mcp_nlp_tools/
# ├── LICENSE
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# Halimbawa ng setup.py
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

# Halimbawa ng implementasyon ng NLP tool (sentiment_tool.py)
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # I-load ang modelo ng sentiment analysis
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
            # Kunin ang mga parameter
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # Suriin ang sentiment
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # I-format ang resulta
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # Ibalik ang resulta
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# Para mag-publish:
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### Pagbabahagi ng Mga Pinakamahusay na Kasanayan

Kapag nagbabahagi ng mga kasangkapan ng MCP sa komunidad:

1. **Kompletong Dokumentasyon**:
   - Idokumento ang layunin, paggamit, at mga halimbawa
   - Ipaliwanag ang mga parametro at mga return value
   - I-dokumento ang anumang panlabas na dependency

2. **Pag-handle ng Error**:
   - Magpatupad ng matibay na pag-handle ng error
   - Magbigay ng kapaki-pakinabang na mga mensahe ng error
   - Maayos na hawakan ang mga edge case

3. **Mga Pagsasaalang-alang sa Performance**:
   - I-optimize ang bilis at paggamit ng mga resources
   - Magpatupad ng caching kung kailangan
   - Isaalang-alang ang scalability

4. **Seguridad**:
   - Gamitin ang mga secure na API keys at authentication
   - I-validate at i-sanitize ang mga input
   - Magpatupad ng rate limiting para sa mga external na API call

5. **Pagsusuri**:
   - Isama ang komprehensibong test coverage
   - Subukan gamit ang iba't ibang uri ng input at mga edge case
   - Idokumento ang mga pamamaraan ng pagsusuri

## Kolaborasyon ng Komunidad at Pinakamahusay na Kasanayan

Ang epektibong kolaborasyon ang susi sa isang umuunlad na ekosistema ng MCP.

### Mga Channel sa Komunikasyon

- Mga Isyu at Talakayan sa GitHub
- Microsoft Tech Community
- Mga Discord at Slack channel
- Stack Overflow (tag: `model-context-protocol` o `mcp`)

### Mga Review ng Code

Kapag nirereview ang mga ambag sa MCP:

1. **Kalilinawan**: Malinaw at mahusay na nadokumento ba ang code?
2. **Katatagan**: Gumagana ba ito ayon sa inaasahan?
3. **Konsistensi**: Sinusunod ba nito ang mga konbensiyon ng proyekto?
4. **Kabuuan**: Kasama ba ang mga pagsubok at dokumentasyon?
5. **Seguridad**: Mayroon bang mga isyu sa seguridad?

### Pagkakatugma ng Bersyon

Kapag nagde-develop para sa MCP:

1. **Pagbabersyon ng Protocol**: Sundin ang bersyon ng MCP protocol na sinusuportahan ng iyong kasangkapan
2. **Pagkakatugma ng Kliyente**: Isaalang-alang ang backward compatibility
3. **Pagkakatugma ng Server**: Sundin ang mga alituntunin sa implementasyon ng server
4. **Mga Pagbabago na Nakakabasag**: Klarong idokumento ang anumang mga pagbabago na maaaring makasira

## Halimbawa ng Proyektong Pangkomunidad: MCP Tool Registry

Isang mahalagang ambag ng komunidad ang pagbuo ng isang pampublikong registry para sa mga kasangkapan ng MCP.

```python
# Halimbawang iskema para sa isang API ng talaan ng mga kagamitan ng komunidad

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# Mga modelo para sa talaan ng kagamitan
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

# FastAPI na aplikasyon para sa talaan
app = FastAPI(title="MCP Tool Registry")

# In-memory na database para sa halimbawang ito
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

## Mga Pangunahing Aral

- Ang komunidad ng MCP ay iba-iba at tumatanggap ng iba't ibang uri ng ambag
- Maaaring mag-ambag sa MCP mula sa mga pagpapahusay sa core protocol hanggang sa mga sariling kasangkapan
- Ang pagsunod sa mga gabay sa pag-aambag ay nagpapabuti ng tsansa na tanggapin ang iyong PR
- Ang paglikha at pagbabahagi ng mga kasangkapan ng MCP ay isang mahalagang paraan upang mapalago ang ekosistema
- Mahalaga ang kolaborasyon ng komunidad para sa paglago at pagpapabuti ng MCP

## Pagsasanay

1. Tukuyin ang isang bahagi ng ekosistema ng MCP kung saan maaari kang mag-ambag batay sa iyong mga kasanayan at interes
2. I-fork ang repositoryo ng MCP at mag-setup ng lokal na kapaligiran sa pag-unlad
3. Lumikha ng maliit na pagpapabuti, pag-aayos ng bug, o kasangkapan na makakatulong sa komunidad
4. Idokumento ang iyong ambag kasama ang angkop na mga pagsusuri at dokumentasyon
5. Mag-submit ng pull request sa angkop na repositoryo

## Karagdagang Mapagkukunan

- [MCP Community Projects](https://github.com/topics/model-context-protocol)

---

## Ano ang Susunod

Susunod: [Mga Aral mula sa Maagang Pagtanggap](../07-LessonsfromEarlyAdoption/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->