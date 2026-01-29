# Jamii na Michango

[![Jinsi ya Kuchangia MCP: Zana, Nyaraka, Msimbo na Zaidi](../../../translated_images/sw/07.1179f6de46ff196eb3cc13c3510e01c37807a13f3bb9be3c779105ce26737c67.png)](https://youtu.be/v1pvCYAWpRE)

_(Bofya picha hapo juu kutazama video ya somo hili)_

## Muhtasari

Somo hili linazingatia jinsi ya kushirikiana na jamii ya MCP, kuchangia katika mfumo wa MCP, na kufuata mbinu bora za maendeleo ya pamoja. Kuelewa jinsi ya kushiriki katika miradi ya MCP ya chanzo huria ni muhimu kwa wale wanaotaka kuunda mustakabali wa teknolojia hii.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuelewa muundo wa jamii na mfumo wa MCP
- Kushiriki kwa ufanisi katika majukwaa na mijadala ya jamii ya MCP
- Kuchangia katika hifadhi za MCP za chanzo huria
- Kuunda na kushiriki zana na seva za MCP zilizobinafsishwa
- Kufuata mbinu bora za maendeleo na ushirikiano wa MCP
- Kugundua rasilimali za jamii na mifumo ya maendeleo ya MCP

## Mfumo wa Jamii ya MCP

Mfumo wa MCP unajumuisha vipengele mbalimbali na washiriki wanaofanya kazi pamoja kuendeleza itifaki.

### Vipengele Muhimu vya Jamii

1. **Wadumishaji wa Itifaki ya Msingi**: Shirika rasmi la [Model Context Protocol GitHub](https://github.com/modelcontextprotocol) linadumisha maelezo ya msingi ya MCP na utekelezaji wa marejeo.
2. **Watengenezaji wa Zana**: Watu binafsi na timu zinazounda zana na seva za MCP.
3. **Watoa Huduma za Ujumuishaji**: Kampuni zinazojumuisha MCP katika bidhaa na huduma zao.
4. **Watumiaji wa Mwisho**: Waendelezaji na mashirika yanayotumia MCP katika programu zao.
5. **Wachangiaji**: Wanachama wa jamii wanaochangia msimbo, nyaraka, au rasilimali nyingine.

### Rasilimali za Jamii

#### Mifumo Rasmi

- [Shirika la MCP GitHub](https://github.com/modelcontextprotocol)
- [Nyaraka za MCP](https://modelcontextprotocol.io/)
- [Maelezo ya MCP](https://modelcontextprotocol.io/docs/specification)
- [Mijadala ya GitHub](https://github.com/orgs/modelcontextprotocol/discussions)
- [Hifadhi ya Mifano na Seva za MCP](https://github.com/modelcontextprotocol/servers)

#### Rasilimali Zinazoendeshwa na Jamii

- [Wateja wa MCP](https://modelcontextprotocol.io/clients) - Orodha ya wateja wanaounga mkono ujumuishaji wa MCP.
- [Seva za Jamii za MCP](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Orodha inayokua ya seva za MCP zilizotengenezwa na jamii.
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Orodha iliyochaguliwa ya seva za MCP.
- [PulseMCP](https://www.pulsemcp.com/) - Kituo cha jamii na jarida la kugundua rasilimali za MCP.
- [Kituo cha Discord](https://discord.gg/jHEGxQu2a5) - Ungana na waendelezaji wa MCP.
- Utekelezaji wa SDK maalum kwa lugha.
- Machapisho ya blogu na mafunzo.

## Kuchangia katika MCP

### Aina za Michango

Mfumo wa MCP unakaribisha aina mbalimbali za michango:

1. **Michango ya Msimbo**:
   - Uboreshaji wa itifaki ya msingi
   - Marekebisho ya hitilafu
   - Utekelezaji wa zana na seva
   - Maktaba za wateja/seva katika lugha tofauti

2. **Nyaraka**:
   - Kuboresha nyaraka zilizopo
   - Kuunda mafunzo na miongozo
   - Kutafsiri nyaraka
   - Kuunda mifano na programu za mfano

3. **Msaada wa Jamii**:
   - Kujibu maswali kwenye majukwaa na mijadala
   - Kupima na kuripoti masuala
   - Kuandaa matukio ya jamii
   - Kutoa mafunzo kwa wachangiaji wapya

### Mchakato wa Michango: Itifaki ya Msingi

Ili kuchangia katika itifaki ya msingi ya MCP au utekelezaji rasmi, fuata kanuni hizi kutoka kwa [miongozo rasmi ya kuchangia](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Unyenyekevu na Urahisi**: Maelezo ya MCP yanadumisha viwango vya juu vya kuongeza dhana mpya. Ni rahisi kuongeza vitu kwenye maelezo kuliko kuondoa.
2. **Njia ya Kivitendo**: Mabadiliko ya maelezo yanapaswa kutegemea changamoto maalum za utekelezaji, si mawazo ya kubahatisha.
3. **Hatua za Pendekezo**:
   - Kufafanua: Chunguza tatizo, thibitisha kuwa watumiaji wengine wa MCP wanakutana na tatizo sawa.
   - Kujaribu: Tengeneza suluhisho la mfano na onyesha matumizi yake ya vitendo.
   - Kuandika: Kulingana na mfano, andika pendekezo la maelezo.

### Mazingira ya Maendeleo

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

### Mfano: Kuchangia Marekebisho ya Hitilafu

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

### Mfano: Kuchangia Zana Mpya kwenye Maktaba ya Kawaida

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

### Miongozo ya Michango

Ili kufanya mchango wenye mafanikio katika miradi ya MCP:

1. **Anza Kidogo**: Anza na nyaraka, marekebisho ya hitilafu, au maboresho madogo.
2. **Fuata Mwongozo wa Mtindo**: Zingatia mtindo wa uandishi wa msimbo na kanuni za mradi.
3. **Andika Majaribio**: Jumuisha majaribio ya kitengo kwa michango yako ya msimbo.
4. **Andika Nyaraka**: Ongeza nyaraka wazi kwa vipengele au mabadiliko mapya.
5. **Tuma PR Zilizoelekezwa**: Weka maombi ya kuvuta yakiwa yamelenga suala moja au kipengele.
6. **Shirikiana na Maoni**: Kuwa tayari kujibu maoni kuhusu michango yako.

### Mfano wa Mtiririko wa Michango

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

## Kuunda na Kushiriki Seva za MCP

Njia mojawapo ya kuchangia kwa thamani katika mfumo wa MCP ni kuunda na kushiriki seva za MCP zilizobinafsishwa. Jamii tayari imeunda mamia ya seva kwa huduma na matumizi mbalimbali.

### Mifumo ya Maendeleo ya Seva za MCP

Mifumo kadhaa inapatikana ili kurahisisha maendeleo ya seva za MCP:

1. **SDK Rasmi**:
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Mifumo ya Jamii**:
   - [MCP-Framework](https://mcp-framework.com/) - Jenga seva za MCP kwa urahisi na kasi katika TypeScript.
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Seva za MCP zinazoendeshwa na maelezo katika Java.
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Mfumo wa Java kwa seva za MCP.
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Mradi wa kuanzia wa Next.js kwa seva za MCP.

### Kuunda Zana Zinazoweza Kushirikika

#### Mfano wa .NET: Kuunda Kifurushi cha Zana Kinachoweza Kushirikika

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

#### Mfano wa Java: Kuunda Kifurushi cha Maven kwa Zana

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

#### Mfano wa Python: Kuchapisha Kifurushi cha PyPI

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

### Kushiriki Mbinu Bora

Unaposhiriki zana za MCP na jamii:

1. **Nyaraka Kamili**:
   - Andika madhumuni, matumizi, na mifano.
   - Eleza vigezo na thamani za kurudi.
   - Andika utegemezi wowote wa nje.

2. **Ushughulikiaji wa Hitilafu**:
   - Tekeleza usimamizi wa hitilafu thabiti.
   - Toa ujumbe wa hitilafu unaofaa.
   - Shughulikia hali za kipekee kwa uangalifu.

3. **Masuala ya Utendaji**:
   - Boresha kasi na matumizi ya rasilimali.
   - Tekeleza uhifadhi wa muda inapofaa.
   - Fikiria kuhusu uwezo wa kupanuka.

4. **Usalama**:
   - Tumia funguo za API salama na uthibitishaji.
   - Thibitisha na kusafisha pembejeo.
   - Tekeleza mipaka ya kiwango kwa miito ya API ya nje.

5. **Upimaji**:
   - Jumuisha chanjo kamili ya majaribio.
   - Jaribu na aina tofauti za pembejeo na hali za kipekee.
   - Andika taratibu za majaribio.

## Ushirikiano wa Jamii na Mbinu Bora

Ushirikiano wa ufanisi ni muhimu kwa ukuaji wa mfumo wa MCP.

### Mifumo ya Mawasiliano

- Masuala na Mijadala ya GitHub
- Microsoft Tech Community
- Vituo vya Discord na Slack
- Stack Overflow (tagi: `model-context-protocol` au `mcp`)

### Mapitio ya Msimbo

Unapopitia michango ya MCP:

1. **Uwazi**: Je, msimbo ni wazi na umeandikwa vizuri?
2. **Usahihi**: Je, unafanya kazi kama inavyotarajiwa?
3. **Ulinganifu**: Je, unafuata kanuni za mradi?
4. **Ukamilifu**: Je, majaribio na nyaraka zimejumuishwa?
5. **Usalama**: Je, kuna masuala yoyote ya usalama?

### Utangamano wa Toleo

Unapounda kwa MCP:

1. **Utoaji wa Itifaki**: Zingatia toleo la itifaki ya MCP ambalo zana yako inaunga mkono.
2. **Utangamano wa Wateja**: Fikiria kuhusu utangamano wa nyuma.
3. **Utangamano wa Seva**: Fuata miongozo ya utekelezaji wa seva.
4. **Mabadiliko Makubwa**: Andika wazi mabadiliko yoyote makubwa.

## Mfano wa Mradi wa Jamii: Usajili wa Zana za MCP

Michango muhimu ya jamii inaweza kuwa kuunda usajili wa umma wa zana za MCP.

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

## Mambo Muhimu ya Kukumbuka

- Jamii ya MCP ni tofauti na inakaribisha aina mbalimbali za michango.
- Kuchangia katika MCP kunaweza kuanzia uboreshaji wa itifaki ya msingi hadi zana za kibinafsi.
- Kufuatilia miongozo ya michango kunaboresha nafasi ya PR yako kukubaliwa.
- Kuunda na kushiriki zana za MCP ni njia muhimu ya kuimarisha mfumo.
- Ushirikiano wa jamii ni muhimu kwa ukuaji na uboreshaji wa MCP.

## Zoezi

1. Tambua eneo katika mfumo wa MCP ambapo unaweza kuchangia kulingana na ujuzi na maslahi yako.
2. Fork hifadhi ya MCP na weka mazingira ya maendeleo ya ndani.
3. Unda uboreshaji mdogo, marekebisho ya hitilafu, au zana ambayo itafaidi jamii.
4. Andika nyaraka za mchango wako na majaribio sahihi.
5. Tuma ombi la kuvuta kwenye hifadhi inayofaa.

## Rasilimali za Ziada

- [Miradi ya Jamii ya MCP](https://github.com/topics/model-context-protocol)

---

Ifuatayo: [Masomo kutoka kwa Kupitishwa Mapema](../07-LessonsfromEarlyAdoption/README.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.