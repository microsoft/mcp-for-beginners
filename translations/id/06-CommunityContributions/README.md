# Komunitas dan Kontribusi

[![Cara Berkontribusi pada MCP: Alat, Dokumentasi, Kode, dan Lainnya](../../../translated_images/id/07.1179f6de46ff196eb3cc13c3510e01c37807a13f3bb9be3c779105ce26737c67.png)](https://youtu.be/v1pvCYAWpRE)

_(Klik gambar di atas untuk menonton video pelajaran ini)_

## Gambaran Umum

Pelajaran ini berfokus pada cara berinteraksi dengan komunitas MCP, berkontribusi pada ekosistem MCP, dan mengikuti praktik terbaik dalam pengembangan kolaboratif. Memahami cara berpartisipasi dalam proyek MCP open-source sangat penting bagi mereka yang ingin membentuk masa depan teknologi ini.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Memahami struktur komunitas dan ekosistem MCP
- Berpartisipasi secara efektif dalam forum dan diskusi komunitas MCP
- Berkontribusi pada repositori open-source MCP
- Membuat dan membagikan alat serta server MCP kustom
- Mengikuti praktik terbaik untuk pengembangan dan kolaborasi MCP
- Menemukan sumber daya dan kerangka kerja komunitas untuk pengembangan MCP

## Ekosistem Komunitas MCP

Ekosistem MCP terdiri dari berbagai komponen dan peserta yang bekerja sama untuk memajukan protokol ini.

### Komponen Utama Komunitas

1. **Pemelihara Protokol Inti**: [Organisasi GitHub Model Context Protocol](https://github.com/modelcontextprotocol) secara resmi memelihara spesifikasi inti MCP dan implementasi referensi.
2. **Pengembang Alat**: Individu dan tim yang membuat alat dan server MCP.
3. **Penyedia Integrasi**: Perusahaan yang mengintegrasikan MCP ke dalam produk dan layanan mereka.
4. **Pengguna Akhir**: Pengembang dan organisasi yang menggunakan MCP dalam aplikasi mereka.
5. **Kontributor**: Anggota komunitas yang menyumbangkan kode, dokumentasi, atau sumber daya lainnya.

### Sumber Daya Komunitas

#### Saluran Resmi

- [Organisasi GitHub MCP](https://github.com/modelcontextprotocol)
- [Dokumentasi MCP](https://modelcontextprotocol.io/)
- [Spesifikasi MCP](https://modelcontextprotocol.io/docs/specification)
- [Diskusi GitHub](https://github.com/orgs/modelcontextprotocol/discussions)
- [Repositori Contoh & Server MCP](https://github.com/modelcontextprotocol/servers)

#### Sumber Daya yang Dikelola Komunitas

- [Klien MCP](https://modelcontextprotocol.io/clients) - Daftar klien yang mendukung integrasi MCP
- [Server MCP Komunitas](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Daftar server MCP yang dikembangkan komunitas
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Daftar server MCP yang dikurasi
- [PulseMCP](https://www.pulsemcp.com/) - Pusat komunitas & buletin untuk menemukan sumber daya MCP
- [Server Discord](https://discord.gg/jHEGxQu2a5) - Terhubung dengan pengembang MCP
- Implementasi SDK khusus bahasa
- Artikel blog dan tutorial

## Berkontribusi pada MCP

### Jenis Kontribusi

Ekosistem MCP menyambut berbagai jenis kontribusi:

1. **Kontribusi Kode**:
   - Peningkatan protokol inti
   - Perbaikan bug
   - Implementasi alat dan server
   - Perpustakaan klien/server dalam berbagai bahasa

2. **Dokumentasi**:
   - Meningkatkan dokumentasi yang ada
   - Membuat tutorial dan panduan
   - Menerjemahkan dokumentasi
   - Membuat contoh dan aplikasi sampel

3. **Dukungan Komunitas**:
   - Menjawab pertanyaan di forum dan diskusi
   - Menguji dan melaporkan masalah
   - Mengorganisir acara komunitas
   - Membimbing kontributor baru

### Proses Kontribusi: Protokol Inti

Untuk berkontribusi pada protokol inti MCP atau implementasi resmi, ikuti prinsip-prinsip dari [panduan kontribusi resmi](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Kesederhanaan dan Minimalisme**: Spesifikasi MCP mempertahankan standar tinggi untuk menambahkan konsep baru. Lebih mudah menambahkan sesuatu ke spesifikasi daripada menghapusnya.

2. **Pendekatan Konkret**: Perubahan spesifikasi harus didasarkan pada tantangan implementasi spesifik, bukan ide spekulatif.

3. **Tahapan Proposal**:
   - Definisikan: Jelajahi ruang masalah, validasi bahwa pengguna MCP lain menghadapi masalah serupa.
   - Prototipe: Bangun solusi contoh dan tunjukkan aplikasi praktisnya.
   - Tulis: Berdasarkan prototipe, tulis proposal spesifikasi.

### Pengaturan Lingkungan Pengembangan

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

### Contoh: Berkontribusi Perbaikan Bug

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

### Contoh: Berkontribusi Alat Baru ke Perpustakaan Standar

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

### Panduan Kontribusi

Untuk membuat kontribusi yang sukses pada proyek MCP:

1. **Mulai dari yang Kecil**: Mulailah dengan dokumentasi, perbaikan bug, atau peningkatan kecil.
2. **Ikuti Panduan Gaya**: Patuhi gaya penulisan kode dan konvensi proyek.
3. **Tulis Tes**: Sertakan tes unit untuk kontribusi kode Anda.
4. **Dokumentasikan Pekerjaan Anda**: Tambahkan dokumentasi yang jelas untuk fitur atau perubahan baru.
5. **Kirim PR yang Terfokus**: Pastikan pull request Anda hanya mencakup satu masalah atau fitur.
6. **Tanggapi Umpan Balik**: Bersikap responsif terhadap umpan balik pada kontribusi Anda.

### Alur Kerja Kontribusi Contoh

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

## Membuat dan Membagikan Server MCP

Salah satu cara paling berharga untuk berkontribusi pada ekosistem MCP adalah dengan membuat dan membagikan server MCP kustom. Komunitas telah mengembangkan ratusan server untuk berbagai layanan dan kasus penggunaan.

### Kerangka Kerja Pengembangan Server MCP

Beberapa kerangka kerja tersedia untuk menyederhanakan pengembangan server MCP:

1. **SDK Resmi**:
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Kerangka Kerja Komunitas**:
   - [MCP-Framework](https://mcp-framework.com/) - Bangun server MCP dengan elegan dan cepat menggunakan TypeScript.
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Server MCP berbasis anotasi dengan Java.
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Kerangka kerja Java untuk server MCP.
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Proyek awal Next.js untuk server MCP.

### Mengembangkan Alat yang Dapat Dibagikan

#### Contoh .NET: Membuat Paket Alat yang Dapat Dibagikan

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

#### Contoh Java: Membuat Paket Maven untuk Alat

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

#### Contoh Python: Menerbitkan Paket PyPI

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

### Berbagi Praktik Terbaik

Saat membagikan alat MCP dengan komunitas:

1. **Dokumentasi Lengkap**:
   - Dokumentasikan tujuan, penggunaan, dan contoh.
   - Jelaskan parameter dan nilai pengembalian.
   - Dokumentasikan ketergantungan eksternal.

2. **Penanganan Kesalahan**:
   - Terapkan penanganan kesalahan yang kuat.
   - Berikan pesan kesalahan yang berguna.
   - Tangani kasus tepi dengan baik.

3. **Pertimbangan Kinerja**:
   - Optimalkan untuk kecepatan dan penggunaan sumber daya.
   - Terapkan caching jika diperlukan.
   - Pertimbangkan skalabilitas.

4. **Keamanan**:
   - Gunakan kunci API dan autentikasi yang aman.
   - Validasi dan sanitasi input.
   - Terapkan pembatasan laju untuk panggilan API eksternal.

5. **Pengujian**:
   - Sertakan cakupan pengujian yang komprehensif.
   - Uji dengan berbagai jenis input dan kasus tepi.
   - Dokumentasikan prosedur pengujian.

## Kolaborasi Komunitas dan Praktik Terbaik

Kolaborasi yang efektif adalah kunci untuk ekosistem MCP yang berkembang.

### Saluran Komunikasi

- Isu dan Diskusi GitHub
- Microsoft Tech Community
- Saluran Discord dan Slack
- Stack Overflow (tag: `model-context-protocol` atau `mcp`)

### Tinjauan Kode

Saat meninjau kontribusi MCP:

1. **Kejelasan**: Apakah kode jelas dan terdokumentasi dengan baik?
2. **Kebenaran**: Apakah kode berfungsi seperti yang diharapkan?
3. **Konsistensi**: Apakah kode mengikuti konvensi proyek?
4. **Kelengkapan**: Apakah tes dan dokumentasi disertakan?
5. **Keamanan**: Apakah ada masalah keamanan?

### Kompatibilitas Versi

Saat mengembangkan untuk MCP:

1. **Versi Protokol**: Patuhi versi protokol MCP yang didukung alat Anda.
2. **Kompatibilitas Klien**: Pertimbangkan kompatibilitas ke belakang.
3. **Kompatibilitas Server**: Ikuti panduan implementasi server.
4. **Perubahan yang Merusak**: Dokumentasikan dengan jelas perubahan yang merusak.

## Proyek Komunitas Contoh: Registri Alat MCP

Kontribusi komunitas yang penting bisa berupa pengembangan registri publik untuk alat MCP.

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

- Komunitas MCP beragam dan menyambut berbagai jenis kontribusi.
- Berkontribusi pada MCP dapat mencakup peningkatan protokol inti hingga alat kustom.
- Mengikuti panduan kontribusi meningkatkan peluang PR Anda diterima.
- Membuat dan membagikan alat MCP adalah cara berharga untuk meningkatkan ekosistem.
- Kolaborasi komunitas sangat penting untuk pertumbuhan dan peningkatan MCP.

## Latihan

1. Identifikasi area dalam ekosistem MCP di mana Anda dapat memberikan kontribusi berdasarkan keterampilan dan minat Anda.
2. Fork repositori MCP dan atur lingkungan pengembangan lokal.
3. Buat peningkatan kecil, perbaikan bug, atau alat yang akan bermanfaat bagi komunitas.
4. Dokumentasikan kontribusi Anda dengan tes dan dokumentasi yang sesuai.
5. Kirim pull request ke repositori yang sesuai.

## Sumber Daya Tambahan

- [Proyek Komunitas MCP](https://github.com/topics/model-context-protocol)

---

Selanjutnya: [Pelajaran dari Adopsi Awal](../07-LessonsfromEarlyAdoption/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.