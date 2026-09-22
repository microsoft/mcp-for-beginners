# Topluluk ve Katkılar

[![MCP'ye Nasıl Katkıda Bulunulur: Araçlar, Dokümantasyon, Kod ve Daha Fazlası](../../../translated_images/tr/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Bu dersin videosunu izlemek için yukarıdaki resme tıklayın)_

## Genel Bakış

Bu ders, MCP topluluğuyla nasıl etkileşim kuracağınızı, MCP ekosistemine nasıl katkıda bulunacağınızı ve işbirlikçi geliştirme için en iyi uygulamaları nasıl takip edeceğinizi öğretiyor. Açık kaynaklı MCP projelerine nasıl katılacağınızı anlamak, bu teknolojinin geleceğini şekillendirmek isteyenler için çok önemlidir.

## Öğrenme Hedefleri

Bu ders sonunda şunları yapabileceksiniz:

- MCP topluluğunun ve ekosisteminin yapısını anlamak
- MCP topluluk forumları ve tartışmalarına etkili şekilde katılmak
- MCP açık kaynak depolarına katkıda bulunmak
- Özel MCP araçları ve sunucuları oluşturup paylaşmak
- MCP geliştirme ve iş birliği için en iyi uygulamaları takip etmek
- MCP geliştirme için topluluk kaynakları ve çerçevelerini keşfetmek

## MCP Topluluk Ekosistemi

MCP ekosistemi, protokolü ilerletmek için birlikte çalışan çeşitli bileşenler ve katılımcılardan oluşur.

### Ana Topluluk Bileşenleri

1. **Çekirdek Protokol Bakımcıları**: Resmi [Model Context Protocol GitHub organizasyonu](https://github.com/modelcontextprotocol), çekirdek MCP spesifikasyonlarını ve referans uygulamalarını yönetir
2. **Araç Geliştiricileri**: MCP araçları ve sunucuları yaratan bireyler ve ekipler
3. **Entegrasyon Sağlayıcıları**: MCP’yi ürün ve hizmetlerine entegre eden şirketler
4. **Son Kullanıcılar**: MCP’yi uygulamalarında kullanan geliştiriciler ve organizasyonlar
5. **Katkıda Bulunanlar**: Kod, dokümantasyon veya diğer kaynaklarla katkı sağlayan topluluk üyeleri

### Topluluk Kaynakları

#### Resmi Kanallar

- [MCP GitHub Organizasyonu](https://github.com/modelcontextprotocol)
- [MCP Dokümantasyonu](https://modelcontextprotocol.io/)
- [MCP Spesifikasyonu](https://modelcontextprotocol.io/specification/2026-07-28/)
- [GitHub Tartışmaları](https://github.com/orgs/modelcontextprotocol/discussions)
- [MCP Örnekleri ve Sunucular Deposu](https://github.com/modelcontextprotocol/servers)

#### Topluluk Odaklı Kaynaklar

- [MCP İstemcileri](https://modelcontextprotocol.io/clients) - MCP entegrasyonlarını destekleyen istemcilerin listesi
- [Topluluk MCP Sunucuları](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Topluluk tarafından geliştirilen MCP sunucularının büyüyen listesi
- [Harika MCP Sunucuları](https://github.com/wong2/awesome-mcp-servers) - Düzenlenmiş MCP sunucuları listesi
- [PulseMCP](https://www.pulsemcp.com/) - MCP kaynaklarını keşfetmek için topluluk merkezi & haber bülteni
- [Remote OpenClaw](https://www.remoteopenclaw.com/) - MCP sunucuları, ajan becerileri ve eklentiler için ücretsiz aranabilir dizin
- [Discord Sunucusu](https://discord.gg/jHEGxQu2a5) - MCP geliştiricileri ile bağlantı kurun
- Dil bazlı SDK uygulamaları
- Blog yazıları ve öğreticiler

## MCP'ye Katkıda Bulunma

### Katkı Türleri

MCP ekosistemi çeşitli katkı türlerini memnuniyetle karşılar:

1. **Kod Katkıları**:
   - Çekirdek protokol geliştirmeleri
   - Hata düzeltmeleri
   - Araç ve sunucu uygulamaları
   - Farklı dillerde istemci/sunucu kütüphaneleri

2. **Dokümantasyon**:
   - Mevcut dokümantasyonu geliştirme
   - Öğreticiler ve rehberler oluşturma
   - Dokümantasyon çevirisi yapma
   - Örnekler ve örnek uygulamalar oluşturma

3. **Topluluk Desteği**:

   - Forumlarda ve tartışmalarda soruları cevaplamak
   - Test yapmak ve sorunları bildirmek
   - Topluluk etkinlikleri düzenlemek
   - Yeni katkıda bulunanlara mentorluk yapmak

### Katkı Süreci: Temel Protokol

Temel MCP protokolüne veya resmi uygulamalara katkıda bulunmak için, [resmi katkı yönergeleri](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md) başlangıç noktası olarak şu ilkeleri takip edin:

1. **Sadelik ve Minimalizm**: MCP spesifikasyonu yeni kavramlar eklemek için yüksek bir standart korur. Bir spesifikasyona ekleme yapmak, ondan çıkarma yapmaktan daha kolaydır.

2. **Somut Yaklaşım**: Spesifikasyon değişiklikleri, spekülatif fikirler değil, belirli uygulama zorluklarına dayanmalıdır.

3. **Bir Teklifin Aşamaları**:
   - Tanımla: Problem alanını keşfet, diğer MCP kullanıcılarının benzer bir sorunla karşılaşıp karşılaşmadığını doğrula
   - Prototip: Bir örnek çözüm oluştur ve pratik uygulamasını göster
   - Yaz: Prototipe dayanarak bir spesifikasyon teklifi yaz

### Geliştirme Ortamı Kurulumu

```bash
# Depoyu çatalla
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# Bağımlılıkları yükle
npm install

# Şema değişiklikleri için, schema.json dosyasını doğrula ve oluştur:
npm run check:schema:ts
npm run generate:schema

# Dokümantasyon değişiklikleri için
npm run check:docs
npm run format

# Dokümantasyonu yerel olarak önizle (isteğe bağlı):
npm run serve:docs
```

### Örnek: Bir Hata Düzeltmesine Katkıda Bulunma

```javascript
// typescript-sdk'de hatalı orijinal kod
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Hata: Eksik özellik doğrulaması
  // Mevcut uygulama:
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// Bir katkıda düzeltilmiş uygulama
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Geliştirilmiş doğrulama
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### Örnek: Standart Kütüphaneye Yeni Bir Araç Katkısı

```python
# Örnek katkı: MCP standart kütüphanesi için bir CSV veri işleme aracı

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
            # Parametreleri çıkar
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # CSV verisini doğrudan veri veya URL'den al
            df = await self._get_dataframe(request)
            
            # İstenen işleme göre işle
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
        # Uygulama, çeşitli dönüşümleri içerecektir
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

### Katkı Yönergeleri

MCP projelerine başarılı bir katkı yapmak için:

1. **Küçük Başlayın**: Dokümantasyon, hata düzeltmeleri veya küçük geliştirmelerle başlayın
2. **Stil Rehberine Uyma**: Projenin kodlama stil ve kurallarına uyun
3. **Test Yazın**: Kod katkılarınız için birim testler ekleyin
4. **Çalışmanızı Belgelendirin**: Yeni özellikler veya değişiklikler için açık dokümantasyon ekleyin
5. **Hedefe Yönelik PR Gönderin**: Çekme isteklerini tek bir sorun veya özellikle sınırlı tutun
6. **Geri Bildirimlerle Etkileşim**: Katkılarınıza gelen geri bildirimlere yanıt verin

### Örnek Katkı İş Akışı

```bash
# Depoyu klonlayın
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# Katkınız için yeni bir dal oluşturun
git checkout -b feature/my-contribution

# Değişikliklerinizi yapın
# ...

# Değişikliklerinizin mevcut işlevselliği bozmadığından emin olmak için testleri çalıştırın
npm test

# Değişikliklerinizi açıklayıcı bir mesajla commit yapın
git commit -am "Fix validation in resource handler"

# Dalınızı forkunuza push edin
git push origin feature/my-contribution

# Dalınızdan ana depoya bir pull request oluşturun
# Ardından geri bildirimlerle etkileşime geçin ve PR'nizi gerektiği gibi yineleyin
```

## MCP Sunucuları Oluşturma ve Paylaşma

MCP ekosistemine katkıda bulunmanın en değerli yollarından biri özel MCP sunucuları oluşturmak ve paylaşmaktır. Topluluk, çeşitli hizmetler ve kullanım durumları için yüzlerce sunucu geliştirmiştir.

### MCP Sunucu Geliştirme Çerçeveleri

MCP sunucu geliştirmeyi kolaylaştıran birkaç çerçeve mevcuttur:

1. **Resmi SDK'lar** (her
    SDK'nın desteklediği protokol revizyonları için
    [SDK dokümantasyonuna](https://modelcontextprotocol.io/docs/sdk) bakın):
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
   - [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
   - [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk)

2. **Topluluk Çerçeveleri**:
   - [MCP-Framework](https://mcp-framework.com/) - TypeScript ile zarif ve hızlı MCP sunucuları oluşturun
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Java ile anotasyon tabanlı MCP sunucuları
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - MCP sunucuları için Java çerçevesi

   - [Next.js MCP Sunucu Şablonu](https://github.com/vercel-labs/mcp-for-next.js) - MCP sunucuları için başlangıç Next.js projesi

### Paylaşılabilir Araçlar Geliştirme

#### .NET Örneği: Paylaşılabilir Bir Araç Paketi Oluşturma

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

#### Java Örneği: Araçlar için Maven Paketi Oluşturma

```java
// paylaşılabilir bir MCP araç paketinin pom.xml yapılandırması
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
            <url>https://maven.pkg.github.com/kullanıcıadı/mcp-hava-durumu-araçları</url>
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
        // Şema tanımı...
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            String location = request.getParameters().get("location").asText();
            int days = request.getParameters().has("days") ? 
                request.getParameters().get("days").asInt() : 3;
            
            // Hava durumu API'sini çağır
            Map<String, Object> forecast = getForecast(location, days);
            
            // Yanıtı oluştur
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // Uygulama hava durumu API'sini çağıracak
        // Basitleştirilmiş örnek
        Map<String, Object> result = new HashMap<>();
        // Tahmin verisini ekle...
        return result;
    }
}

// Maven kullanarak derle ve yayınla
// mvn clean package
// mvn deploy
```

#### Python Örneği: PyPI Paketi Yayınlama

```python
# Bir PyPI paketi için dizin yapısı:
# mcp_nlp_tools/
# ├── LICENSE
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# Örnek setup.py
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

# Örnek NLP aracı uygulaması (sentiment_tool.py)
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # Duygu analizi modelini yükle
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
            # Parametreleri çıkar
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # Duyguyu analiz et
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # Sonucu formatla
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # Sonucu döndür
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# Yayınlamak için:
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### En İyi Uygulamaların Paylaşımı

MCP araçlarını toplumla paylaşırken:

1. **Tam Dokümantasyon**:
   - Amacı, kullanımı ve örnekleri belgeleyin
   - Parametreleri ve dönüş değerlerini açıklayın
   - Herhangi bir dış bağımlılığı belgeleyin

2. **Hata Yönetimi**:
   - Sağlam hata yönetimi uygulayın
   - Yararlı hata mesajları sağlayın
   - Kenar durumları nazikçe ele alın

3. **Performans Düşünceleri**:
   - Hem hız hem kaynak kullanımı için optimize edin
   - Uygunsa önbellekleme uygulayın
   - Ölçeklenebilirliği göz önünde bulundurun

4. **Güvenlik**:
   - Güvenli API anahtarları ve kimlik doğrulama kullanın
   - Girdileri doğrulayın ve temizleyin
   - Harici API çağrıları için hız sınırlaması uygulayın

5. **Test**:
   - Kapsamlı test kapsamı ekleyin
   - Farklı giriş türleri ve kenar durumları ile test edin
   - Test prosedürlerini belgeleyin

## Topluluk İşbirliği ve En İyi Uygulamalar

Etkili işbirliği, gelişen bir MCP ekosisteminin anahtarıdır.

### İletişim Kanalları

- GitHub Sorunları ve Tartışmaları
- Microsoft Tech Community
- Discord ve Slack kanalları
- Stack Overflow (etiket: `model-context-protocol` veya `mcp`)

### Kod İncelemeleri

MCP katkıları incelenirken:

1. **Anlaşılırlık**: Kod açık ve iyi belgelenmiş mi?
2. **Doğruluk**: Beklendiği gibi çalışıyor mu?
3. **Tutarlılık**: Proje kurallarına uyuyor mu?
4. **Tamlık**: Testler ve dokümantasyon dahil mi?
5. **Güvenlik**: Herhangi bir güvenlik endişesi var mı?

### Sürüm Uyumluluğu

MCP için geliştirirken:

1. **Protokol Sürümü**: Aracınızın desteklediği MCP protokol sürümüne uyun
2. **İstemci Uyumluluğu**: Gerçekten geriye dönük uyumluluğu göz önüne alın
3. **Sunucu Uyumluluğu**: Sunucu uygulama yönergelerini izleyin
4. **Kırıcı Değişiklikler**: Herhangi bir kırıcı değişikliği açıkça belgeleyin

## Örnek Topluluk Projesi: MCP Araç Kayıt Defteri

Önemli bir topluluk katkısı, MCP araçları için genel bir kayıt defteri geliştirmek olabilir.

```python
# Bir topluluk araç kaydı API'si için örnek şema

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# Araç kaydı için modeller
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

# Kayıt için FastAPI uygulaması
app = FastAPI(title="MCP Tool Registry")

# Bu örnek için bellek içi veritabanı
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

## Temel Çıkarımlar

- MCP topluluğu çeşitli ve çeşitli katkı türlerini hoş karşılar
- MCP'ye katkı, temel protokol iyileştirmelerinden özel araçlara kadar değişebilir
- Katkı yönergelerine uymak, PR'nizin kabul edilme şansını artırır
- MCP araçları oluşturmak ve paylaşmak, ekosistemi geliştirmek için değerli bir yoldur
- Topluluk işbirliği, MCP'nin büyümesi ve gelişimi için esastır

## Alıştırma

1. Becerilerinize ve ilgi alanlarınıza göre katkı sağlayabileceğiniz MCP ekosisteminde bir alan belirleyin
2. MCP deposunu çatallayın ve yerel geliştirme ortamı kurun
3. Topluluğa fayda sağlayacak küçük bir geliştirme, hata düzeltmesi veya araç oluşturun
4. Katkınızı doğru testler ve dokümantasyonla belgeleyin
5. Uygun depoya bir çekme isteği gönderin

## Ek Kaynaklar

- [MCP Topluluk Projeleri](https://github.com/topics/model-context-protocol)

---

## Sırada Ne Var

Sonraki: [Erken Kabulden Dersler](../07-LessonsfromEarlyAdoption/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->