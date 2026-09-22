# Społeczność i wkład

[![Jak wnosić wkład do MCP: narzędzia, dokumentacja, kod i więcej](../../../translated_images/pl/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

## Przegląd

Ta lekcja skupia się na tym, jak angażować się w społeczność MCP, wnosić wkład do ekosystemu MCP oraz stosować najlepsze praktyki w rozwoju współpracy. Zrozumienie, jak uczestniczyć w projektach open-source MCP, jest kluczowe dla tych, którzy chcą kształtować przyszłość tej technologii.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Zrozumieć strukturę społeczności i ekosystemu MCP
- Efektywnie uczestniczyć w forach i dyskusjach społeczności MCP
- Wnosić wkład do repozytoriów open-source MCP
- Tworzyć i udostępniać niestandardowe narzędzia i serwery MCP
- Stosować najlepsze praktyki rozwoju i współpracy MCP
- Odkrywać zasoby społeczności i frameworki do rozwoju MCP

## Ekosystem społeczności MCP

Ekosystem MCP składa się z różnych elementów i uczestników, którzy współpracują, aby rozwijać protokół.

### Kluczowe komponenty społeczności

1. **Główni opiekunowie protokołu**: Oficjalna [organizacja Model Context Protocol na GitHubie](https://github.com/modelcontextprotocol) zarządza głównymi specyfikacjami MCP oraz referencyjnymi implementacjami
2. **Twórcy narzędzi**: Osoby i zespoły tworzące narzędzia i serwery MCP
3. **Dostawcy integracji**: Firmy integrujące MCP w swoich produktach i usługach
4. **Użytkownicy końcowi**: Deweloperzy i organizacje korzystające z MCP w swoich aplikacjach
5. **Współtwórcy**: Członkowie społeczności wnoszący kod, dokumentację lub inne zasoby

### Zasoby społeczności

#### Oficjalne kanały

- [Organizacja MCP na GitHubie](https://github.com/modelcontextprotocol)
- [Dokumentacja MCP](https://modelcontextprotocol.io/)
- [Specyfikacja MCP](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Dyskusje na GitHubie](https://github.com/orgs/modelcontextprotocol/discussions)
- [Repozytorium przykładów i serwerów MCP](https://github.com/modelcontextprotocol/servers)

#### Zasoby tworzone przez społeczność

- [Klienci MCP](https://modelcontextprotocol.io/clients) - Lista klientów wspierających integracje MCP
- [Społecznościowe serwery MCP](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Rozwijająca się lista serwerów MCP tworzonych przez społeczność
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Kuratowana lista serwerów MCP
- [PulseMCP](https://www.pulsemcp.com/) - Centrum społeczności i newsletter do odkrywania zasobów MCP
- [Remote OpenClaw](https://www.remoteopenclaw.com/) - Bezpłatny katalog wyszukiwalny serwerów MCP, umiejętności agentów i pluginów
- [Serwer Discord](https://discord.gg/jHEGxQu2a5) - Połącz się z deweloperami MCP
- Implementacje SDK specyficzne dla różnych języków
- Posty na blogach i samouczki

## Wnoszenie wkładu do MCP

### Rodzaje wkładu

Ekosystem MCP przyjmuje różne typy wkładu:

1. **Wkład w kod**:
   - Ulepszenia głównego protokołu
   - Naprawa błędów
   - Implementacje narzędzi i serwerów
   - Biblioteki klient/serwer w różnych językach

2. **Dokumentacja**:
   - Ulepszanie istniejącej dokumentacji
   - Tworzenie samouczków i przewodników
   - Tłumaczenie dokumentacji
   - Tworzenie przykładów i przykładowych aplikacji

3. **Wsparcie społeczności**:
   - Odpowiadanie na pytania na forach i w dyskusjach
   - Testowanie i zgłaszanie problemów
   - Organizowanie wydarzeń społecznościowych
   - Mentoring nowych współtwórców

### Proces wnoszenia wkładu: główny protokół

Aby wnieść wkład do głównego protokołu MCP lub oficjalnych implementacji, postępuj zgodnie z zasadami opisanymi w [oficjalnych wytycznych dotyczących wkładu](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Prostota i minimalizm**: Specyfikacja MCP utrzymuje wysokie wymagania dla dodawania nowych koncepcji. Łatwiej jest dodać nowe elementy do specyfikacji niż je usuwać.

2. **Konkretne podejście**: Zmiany w specyfikacji powinny być oparte na konkretnych wyzwaniach implementacyjnych, a nie na spekulacjach.

3. **Etapy propozycji**:
   - Definiowanie: Zbadaj problem, potwierdź, że inni użytkownicy MCP mają podobny problem
   - Prototypowanie: Zbuduj przykładowe rozwiązanie i pokaż jego praktyczne zastosowanie
   - Pisanie: Na podstawie prototypu napisz propozycję specyfikacji

### Konfiguracja środowiska programistycznego

```bash
# Rozgałęź repozytorium
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# Zainstaluj zależności
npm install

# W przypadku zmian w schemacie, zweryfikuj i wygeneruj schema.json:
npm run check:schema:ts
npm run generate:schema

# W przypadku zmian w dokumentacji
npm run check:docs
npm run format

# Podgląd dokumentacji lokalnie (opcjonalnie):
npm run serve:docs
```

### Przykład: Wniesienie poprawek do błędu

```javascript
// Oryginalny kod z błędem w typescript-sdk
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Błąd: Brak weryfikacji właściwości
  // Obecna implementacja:
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// Naprawiona implementacja w wkładzie
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Ulepszona walidacja
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### Przykład: Dodanie nowego narzędzia do standardowej biblioteki

```python
# Przykładowy wkład: Narzędzie do przetwarzania danych CSV dla standardowej biblioteki MCP

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
            # Wyodrębnij parametry
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # Pobierz dane CSV z bezpośrednich danych lub URL
            df = await self._get_dataframe(request)
            
            # Przetwórz na podstawie żądanej operacji
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
        # Implementacja obejmowałaby różne transformacje
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

### Wytyczne dotyczące wkładu

Aby skutecznie wnosić wkład do projektów MCP:

1. **Zacznij od małych rzeczy**: Zacznij od dokumentacji, napraw błędów lub drobnych ulepszeń
2. **Przestrzegaj wytycznych stylu**: Trzymaj się stylu kodowania i konwencji projektu
3. **Pisz testy**: Dołącz testy jednostkowe dla swoich zmian w kodzie
4. **Dokumentuj swoją pracę**: Dodaj jasną dokumentację do nowych funkcji lub zmian
5. **Składaj celowane pull requesty**: Utrzymuj zgłoszenia zmian skupione na jednym problemie lub funkcji
6. **Reaguj na opinie**: Bądź otwarty na opinie dotyczące swoich wkładów

### Przykładowy proces wniesienia wkładu

```bash
# Sklonuj repozytorium
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# Utwórz nową gałąź dla swojego wkładu
git checkout -b feature/my-contribution

# Wprowadź swoje zmiany
# ...

# Uruchom testy, aby upewnić się, że twoje zmiany nie psują istniejącej funkcjonalności
npm test

# Zatwierdź zmiany z opisową wiadomością
git commit -am "Fix validation in resource handler"

# Wypchnij swoją gałąź do swojego forka
git push origin feature/my-contribution

# Stwórz pull request ze swojej gałęzi do głównego repozytorium
# Następnie zaangażuj się w otrzymane uwagi i iteruj swoje PR w razie potrzeby
```

## Tworzenie i udostępnianie serwerów MCP

Jednym z najbardziej wartościowych sposobów wniesienia wkładu do ekosystemu MCP jest tworzenie i udostępnianie niestandardowych serwerów MCP. Społeczność już opracowała setki serwerów dla różnych usług i zastosowań.

### Frameworki do tworzenia serwerów MCP

Dostępnych jest kilka frameworków ułatwiających tworzenie serwerów MCP:

1. **Oficjalne SDK** (sprawdź
    [dokumentację SDK](https://modelcontextprotocol.io/docs/sdk) dla każdej
    obsługiwanej rewizji protokołu):
   - [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
   - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
   - [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
   - [Go SDK](https://github.com/modelcontextprotocol/go-sdk)
   - [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
   - [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
   - [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
   - [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk)

2. **Frameworki społecznościowe**:
   - [MCP-Framework](https://mcp-framework.com/) - Twórz serwery MCP z elegancją i szybkością w TypeScript
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Serwery MCP sterowane adnotacjami w Javie
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Framework Javy do serwerów MCP
   - [Next.js MCP Server Template](https://github.com/vercel-labs/mcp-for-next.js) - Projekt startowy Next.js dla serwerów MCP

### Tworzenie narzędzi do udostępniania

#### Przykład .NET: Tworzenie pakietu narzędzi do udostępniania

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

#### Przykład Java: Tworzenie pakietu Maven dla narzędzi

```java
// konfiguracja pom.xml dla współdzielonego pakietu narzędzi MCP
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
        // Definicja schematu...
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            String location = request.getParameters().get("location").asText();
            int days = request.getParameters().has("days") ? 
                request.getParameters().get("days").asInt() : 3;
            
            // Wywołaj API pogodowe
            Map<String, Object> forecast = getForecast(location, days);
            
            // Zbuduj odpowiedź
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // Implementacja wywoła API pogodowe
        // Uproszczony przykład
        Map<String, Object> result = new HashMap<>();
        // Dodaj dane prognozy...
        return result;
    }
}

// Buduj i publikuj za pomocą Maven
// mvn clean package
// mvn deploy
```

#### Przykład Python: Publikowanie pakietu PyPI

```python
# Struktura katalogów dla pakietu PyPI:
# mcp_nlp_tools/
# ├── LICENSE
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# Przykładowy setup.py
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

# Przykładowa implementacja narzędzia NLP (sentiment_tool.py)
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # Załaduj model analizy sentymentu
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
            # Wyodrębnij parametry
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # Analizuj sentyment
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # Sformatuj wynik
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # Zwróć wynik
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# Aby opublikować:
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### Udostępnianie najlepszych praktyk

Udostępniając narzędzia MCP społeczności:

1. **Kompletna dokumentacja**:
   - Dokumentuj cel, użycie i przykłady
   - Wyjaśnij parametry i wartości zwracane
   - Dokumentuj wszelkie zewnętrzne zależności

2. **Obsługa błędów**:
   - Wdrażaj solidną obsługę błędów
   - Podawaj przydatne komunikaty błędów
   - Łagodnie obsługuj sytuacje brzegowe

3. **Wydajność**:
   - Optymalizuj zarówno pod kątem szybkości, jak i zużycia zasobów
   - Stosuj cache, gdy jest to właściwe
   - Weź pod uwagę skalowalność

4. **Bezpieczeństwo**:
   - Używaj bezpiecznych kluczy API i uwierzytelniania
   - Waliduj i oczyszczaj wejścia
   - Wdrażaj ograniczenia liczby wywołań do zewnętrznych API

5. **Testowanie**:
   - Zawieraj kompleksowe pokrycie testami
   - Testuj różne typy danych wejściowych i przypadki brzegowe
   - Dokumentuj procedury testowe

## Współpraca społeczności i najlepsze praktyki

Skuteczna współpraca jest kluczem do rozwijającego się ekosystemu MCP.

### Kanały komunikacji

- GitHub Issues i Dyskusje
- Microsoft Tech Community
- Kanały Discord i Slack
- Stack Overflow (tag: `model-context-protocol` lub `mcp`)

### Przeglądy kodu

Podczas przeglądu wkładów do MCP:

1. **Jasność**: Czy kod jest czytelny i dobrze udokumentowany?
2. **Poprawność**: Czy działa zgodnie z oczekiwaniami?
3. **Spójność**: Czy przestrzega konwencji projektu?
4. **Kompletność**: Czy zawiera testy i dokumentację?
5. **Bezpieczeństwo**: Czy nie ma potencjalnych zagrożeń bezpieczeństwa?

### Zgodność wersji

Przy tworzeniu dla MCP:

1. **Wersjonowanie protokołu**: Przestrzegaj wersji protokołu MCP obsługiwanej przez twoje narzędzie
2. **Zgodność klienta**: Uwzględnij kompatybilność wsteczną
3. **Zgodność serwera**: Przestrzegaj wytycznych implementacji serwera
4. **Zmiany łamiące kompatybilność**: Wyraźnie dokumentuj wszelkie zmiany łamiące kompatybilność

## Przykładowy projekt społecznościowy: rejestr narzędzi MCP

Istotnym wkładem społecznościowym może być stworzenie publicznego rejestru narzędzi MCP.

```python
# Przykładowy schemat dla API rejestru narzędzi społeczności

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# Modele dla rejestru narzędzi
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

# Aplikacja FastAPI dla rejestru
app = FastAPI(title="MCP Tool Registry")

# Baza danych w pamięci dla tego przykładu
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

## Najważniejsze wnioski

- Społeczność MCP jest różnorodna i przyjmuje różne rodzaje wkładu
- Wkład do MCP może obejmować ulepszenia protokołu głównego oraz niestandardowe narzędzia
- Przestrzeganie wytycznych dotyczących wkładu zwiększa szanse na akceptację twojego pull requesta
- Tworzenie i udostępnianie narzędzi MCP to wartościowy sposób na wzmocnienie ekosystemu
- Współpraca społecznościowa jest niezbędna dla rozwoju i ulepszania MCP

## Ćwiczenie

1. Zidentyfikuj obszar w ekosystemie MCP, w którym możesz wnieść wkład, bazując na swoich umiejętnościach i zainteresowaniach
2. Sklonuj repozytorium MCP i skonfiguruj lokalne środowisko programistyczne
3. Stwórz małe ulepszenie, poprawkę błędu lub narzędzie, które przyniesie korzyść społeczności
4. Udokumentuj swój wkład wraz z odpowiednimi testami i dokumentacją
5. Złóż pull request do odpowiedniego repozytorium

## Dodatkowe zasoby

- [Projekty społeczności MCP](https://github.com/topics/model-context-protocol)

---

## Co dalej

Następne: [Lekcje z wczesnej adopcji](../07-LessonsfromEarlyAdoption/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->