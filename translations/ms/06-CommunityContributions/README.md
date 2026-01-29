# Komuniti dan Sumbangan

[![Cara Menyumbang kepada MCP: Alat, Dokumentasi, Kod dan Lain-lain](../../../translated_images/ms/07.1179f6de46ff196eb3cc13c3510e01c37807a13f3bb9be3c779105ce26737c67.png)](https://youtu.be/v1pvCYAWpRE)

_(Klik imej di atas untuk menonton video pelajaran ini)_

## Gambaran Keseluruhan

Pelajaran ini memberi tumpuan kepada cara melibatkan diri dengan komuniti MCP, menyumbang kepada ekosistem MCP, dan mengikuti amalan terbaik untuk pembangunan kolaboratif. Memahami cara untuk mengambil bahagian dalam projek MCP sumber terbuka adalah penting bagi mereka yang ingin membentuk masa depan teknologi ini.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Memahami struktur komuniti dan ekosistem MCP
- Mengambil bahagian secara berkesan dalam forum dan perbincangan komuniti MCP
- Menyumbang kepada repositori sumber terbuka MCP
- Mencipta dan berkongsi alat dan pelayan MCP tersuai
- Mengikuti amalan terbaik untuk pembangunan dan kolaborasi MCP
- Meneroka sumber dan rangka kerja komuniti untuk pembangunan MCP

## Ekosistem Komuniti MCP

Ekosistem MCP terdiri daripada pelbagai komponen dan peserta yang bekerjasama untuk memajukan protokol ini.

### Komponen Utama Komuniti

1. **Penyelenggara Protokol Teras**: [Organisasi GitHub Model Context Protocol](https://github.com/modelcontextprotocol) rasmi menyelenggara spesifikasi MCP teras dan implementasi rujukan
2. **Pembangun Alat**: Individu dan pasukan yang mencipta alat dan pelayan MCP
3. **Penyedia Integrasi**: Syarikat yang mengintegrasikan MCP ke dalam produk dan perkhidmatan mereka
4. **Pengguna Akhir**: Pembangun dan organisasi yang menggunakan MCP dalam aplikasi mereka
5. **Penyumbang**: Ahli komuniti yang menyumbang kod, dokumentasi, atau sumber lain

### Sumber Komuniti

#### Saluran Rasmi

- [Organisasi GitHub MCP](https://github.com/modelcontextprotocol)
- [Dokumentasi MCP](https://modelcontextprotocol.io/)
- [Spesifikasi MCP](https://modelcontextprotocol.io/docs/specification)
- [Perbincangan GitHub](https://github.com/orgs/modelcontextprotocol/discussions)
- [Repositori Contoh & Pelayan MCP](https://github.com/modelcontextprotocol/servers)

#### Sumber Didorong Komuniti

- [Klien MCP](https://modelcontextprotocol.io/clients) - Senarai klien yang menyokong integrasi MCP
- [Pelayan MCP Komuniti](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Senarai pelayan MCP yang dibangunkan komuniti
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Senarai pelayan MCP yang dikurasi
- [PulseMCP](https://www.pulsemcp.com/) - Hab komuniti & surat berita untuk meneroka sumber MCP
- [Pelayan Discord](https://discord.gg/jHEGxQu2a5) - Berhubung dengan pembangun MCP
- Implementasi SDK khusus bahasa
- Catatan blog dan tutorial

## Menyumbang kepada MCP

### Jenis Sumbangan

Ekosistem MCP mengalu-alukan pelbagai jenis sumbangan:

1. **Sumbangan Kod**:
   - Penambahbaikan protokol teras
   - Pembetulan pepijat
   - Implementasi alat dan pelayan
   - Perpustakaan klien/pelayan dalam pelbagai bahasa

2. **Dokumentasi**:
   - Menambah baik dokumentasi sedia ada
   - Mencipta tutorial dan panduan
   - Menterjemah dokumentasi
   - Mencipta contoh dan aplikasi sampel

3. **Sokongan Komuniti**:
   - Menjawab soalan di forum dan perbincangan
   - Menguji dan melaporkan isu
   - Menganjurkan acara komuniti
   - Membimbing penyumbang baru

### Proses Sumbangan: Protokol Teras

Untuk menyumbang kepada protokol MCP teras atau implementasi rasmi, ikuti prinsip ini daripada [garis panduan sumbangan rasmi](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Kesederhanaan dan Minimalisme**: Spesifikasi MCP mengekalkan standard tinggi untuk menambah konsep baru. Lebih mudah untuk menambah sesuatu kepada spesifikasi daripada mengeluarkannya.

2. **Pendekatan Konkret**: Perubahan spesifikasi harus berdasarkan cabaran implementasi tertentu, bukan idea spekulatif.

3. **Tahap Cadangan**:
   - Definisi: Terokai ruang masalah, sahkan bahawa pengguna MCP lain menghadapi isu serupa
   - Prototip: Bina penyelesaian contoh dan tunjukkan aplikasi praktikalnya
   - Penulisan: Berdasarkan prototip, tulis cadangan spesifikasi

### Persediaan Persekitaran Pembangunan

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

### Contoh: Menyumbang Pembetulan Pepijat

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

### Contoh: Menyumbang Alat Baru kepada Perpustakaan Standard

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

### Garis Panduan Sumbangan

Untuk membuat sumbangan yang berjaya kepada projek MCP:

1. **Mulakan Kecil**: Bermula dengan dokumentasi, pembetulan pepijat, atau penambahbaikan kecil
2. **Ikuti Panduan Gaya**: Patuhi gaya pengekodan dan konvensi projek
3. **Tulis Ujian**: Sertakan ujian unit untuk sumbangan kod anda
4. **Dokumentasikan Kerja Anda**: Tambahkan dokumentasi yang jelas untuk ciri atau perubahan baru
5. **Hantar PR yang Disasarkan**: Kekalkan permintaan tarik (PR) yang fokus pada satu isu atau ciri
6. **Terlibat dengan Maklum Balas**: Responsif terhadap maklum balas pada sumbangan anda

### Aliran Kerja Sumbangan Contoh

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

## Mencipta dan Berkongsi Pelayan MCP

Salah satu cara paling bernilai untuk menyumbang kepada ekosistem MCP adalah dengan mencipta dan berkongsi pelayan MCP tersuai. Komuniti telah membangunkan ratusan pelayan untuk pelbagai perkhidmatan dan kegunaan.

### Rangka Kerja Pembangunan Pelayan MCP

Beberapa rangka kerja tersedia untuk mempermudah pembangunan pelayan MCP:

1. **SDK Rasmi**:
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Rangka Kerja Komuniti**:
   - [MCP-Framework](https://mcp-framework.com/) - Bina pelayan MCP dengan elegan dan pantas dalam TypeScript
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Pelayan MCP berasaskan anotasi dengan Java
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Rangka kerja Java untuk pelayan MCP
   - [Templat Pelayan MCP Next.js](https://github.com/vercel-labs/mcp-for-next.js) - Projek permulaan Next.js untuk pelayan MCP

### Membangunkan Alat yang Boleh Dikongsi

#### Contoh .NET: Mencipta Pakej Alat yang Boleh Dikongsi

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

#### Contoh Java: Mencipta Pakej Maven untuk Alat

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

#### Contoh Python: Menerbitkan Pakej PyPI

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

### Amalan Terbaik untuk Berkongsi

Apabila berkongsi alat MCP dengan komuniti:

1. **Dokumentasi Lengkap**:
   - Dokumentasikan tujuan, penggunaan, dan contoh
   - Terangkan parameter dan nilai pemulangan
   - Dokumentasikan sebarang kebergantungan luaran

2. **Pengendalian Ralat**:
   - Laksanakan pengendalian ralat yang kukuh
   - Sediakan mesej ralat yang berguna
   - Tangani kes tepi dengan baik

3. **Pertimbangan Prestasi**:
   - Optimumkan untuk kelajuan dan penggunaan sumber
   - Laksanakan caching apabila sesuai
   - Pertimbangkan skalabiliti

4. **Keselamatan**:
   - Gunakan kunci API dan pengesahan yang selamat
   - Sahkan dan sanitasi input
   - Laksanakan had kadar untuk panggilan API luaran

5. **Ujian**:
   - Sertakan liputan ujian yang komprehensif
   - Uji dengan pelbagai jenis input dan kes tepi
   - Dokumentasikan prosedur ujian

## Kolaborasi Komuniti dan Amalan Terbaik

Kolaborasi yang berkesan adalah kunci kepada ekosistem MCP yang berkembang maju.

### Saluran Komunikasi

- Isu dan Perbincangan GitHub
- Microsoft Tech Community
- Saluran Discord dan Slack
- Stack Overflow (tag: `model-context-protocol` atau `mcp`)

### Semakan Kod

Apabila menyemak sumbangan MCP:

1. **Kejelasan**: Adakah kod jelas dan didokumentasikan dengan baik?
2. **Ketepatan**: Adakah ia berfungsi seperti yang diharapkan?
3. **Konsistensi**: Adakah ia mengikuti konvensi projek?
4. **Kelengkapan**: Adakah ujian dan dokumentasi disertakan?
5. **Keselamatan**: Adakah terdapat kebimbangan keselamatan?

### Keserasian Versi

Apabila membangunkan untuk MCP:

1. **Versi Protokol**: Patuhi versi protokol MCP yang disokong oleh alat anda
2. **Keserasian Klien**: Pertimbangkan keserasian ke belakang
3. **Keserasian Pelayan**: Ikuti garis panduan implementasi pelayan
4. **Perubahan Besar**: Dokumentasikan dengan jelas sebarang perubahan besar

## Projek Komuniti Contoh: Daftar Alat MCP

Sumbangan komuniti yang penting boleh menjadi pembangunan daftar awam untuk alat MCP.

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

## Poin Penting

- Komuniti MCP adalah pelbagai dan mengalu-alukan pelbagai jenis sumbangan
- Sumbangan kepada MCP boleh merangkumi penambahbaikan protokol teras hingga alat tersuai
- Mengikuti garis panduan sumbangan meningkatkan peluang PR anda diterima
- Mencipta dan berkongsi alat MCP adalah cara yang bernilai untuk meningkatkan ekosistem
- Kolaborasi komuniti adalah penting untuk pertumbuhan dan penambahbaikan MCP

## Latihan

1. Kenal pasti kawasan dalam ekosistem MCP di mana anda boleh membuat sumbangan berdasarkan kemahiran dan minat anda
2. Fork repositori MCP dan sediakan persekitaran pembangunan tempatan
3. Cipta penambahbaikan kecil, pembetulan pepijat, atau alat yang akan memberi manfaat kepada komuniti
4. Dokumentasikan sumbangan anda dengan ujian dan dokumentasi yang sesuai
5. Hantar permintaan tarik ke repositori yang sesuai

## Sumber Tambahan

- [Projek Komuniti MCP](https://github.com/topics/model-context-protocol)

---

Seterusnya: [Pelajaran daripada Penggunaan Awal](../07-LessonsfromEarlyAdoption/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.