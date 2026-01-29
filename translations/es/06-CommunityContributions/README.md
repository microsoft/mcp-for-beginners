# Comunidad y Contribuciones

[![Cómo Contribuir a MCP: Herramientas, Documentación, Código y Más](../../../translated_images/es/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Haz clic en la imagen de arriba para ver el video de esta lección)_

## Descripción General

Esta lección se centra en cómo involucrarse con la comunidad de MCP, contribuir al ecosistema de MCP y seguir las mejores prácticas para el desarrollo colaborativo. Comprender cómo participar en proyectos de MCP de código abierto es esencial para quienes desean dar forma al futuro de esta tecnología.

## Objetivos de Aprendizaje

Al final de esta lección, serás capaz de:

- Comprender la estructura de la comunidad y el ecosistema de MCP
- Participar de manera efectiva en foros y discusiones de la comunidad MCP
- Contribuir a los repositorios de código abierto de MCP
- Crear y compartir herramientas y servidores personalizados de MCP
- Seguir las mejores prácticas para el desarrollo y la colaboración en MCP
- Descubrir recursos y marcos comunitarios para el desarrollo de MCP

## El Ecosistema de la Comunidad MCP

El ecosistema de MCP está compuesto por varios componentes y participantes que trabajan juntos para avanzar en el protocolo.

### Componentes Clave de la Comunidad

1. **Mantenedores del Protocolo Principal**: La organización oficial de [Model Context Protocol en GitHub](https://github.com/modelcontextprotocol) mantiene las especificaciones principales de MCP y las implementaciones de referencia.
2. **Desarrolladores de Herramientas**: Individuos y equipos que crean herramientas y servidores MCP.
3. **Proveedores de Integración**: Empresas que integran MCP en sus productos y servicios.
4. **Usuarios Finales**: Desarrolladores y organizaciones que utilizan MCP en sus aplicaciones.
5. **Contribuyentes**: Miembros de la comunidad que aportan código, documentación u otros recursos.

### Recursos de la Comunidad

#### Canales Oficiales

- [Organización de MCP en GitHub](https://github.com/modelcontextprotocol)
- [Documentación de MCP](https://modelcontextprotocol.io/)
- [Especificación de MCP](https://modelcontextprotocol.io/docs/specification)
- [Discusiones en GitHub](https://github.com/orgs/modelcontextprotocol/discussions)
- [Repositorio de Ejemplos y Servidores de MCP](https://github.com/modelcontextprotocol/servers)

#### Recursos Generados por la Comunidad

- [Clientes MCP](https://modelcontextprotocol.io/clients) - Lista de clientes que soportan integraciones MCP.
- [Servidores MCP de la Comunidad](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Lista creciente de servidores MCP desarrollados por la comunidad.
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Lista curada de servidores MCP.
- [PulseMCP](https://www.pulsemcp.com/) - Centro comunitario y boletín para descubrir recursos de MCP.
- [Servidor de Discord](https://discord.gg/jHEGxQu2a5) - Conéctate con desarrolladores de MCP.
- Implementaciones de SDK específicas por lenguaje.
- Publicaciones en blogs y tutoriales.

## Contribuir a MCP

### Tipos de Contribuciones

El ecosistema de MCP da la bienvenida a varios tipos de contribuciones:

1. **Contribuciones de Código**:
   - Mejoras al protocolo principal.
   - Corrección de errores.
   - Implementaciones de herramientas y servidores.
   - Bibliotecas cliente/servidor en diferentes lenguajes.

2. **Documentación**:
   - Mejorar la documentación existente.
   - Crear tutoriales y guías.
   - Traducir documentación.
   - Crear ejemplos y aplicaciones de muestra.

3. **Soporte Comunitario**:
   - Responder preguntas en foros y discusiones.
   - Probar y reportar problemas.
   - Organizar eventos comunitarios.
   - Mentorear a nuevos contribuyentes.

### Proceso de Contribución: Protocolo Principal

Para contribuir al protocolo principal de MCP o a las implementaciones oficiales, sigue estos principios de las [directrices oficiales de contribución](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Simplicidad y Minimalismo**: La especificación de MCP mantiene un estándar alto para agregar nuevos conceptos. Es más fácil agregar cosas a una especificación que eliminarlas.

2. **Enfoque Concreto**: Los cambios en la especificación deben basarse en desafíos específicos de implementación, no en ideas especulativas.

3. **Etapas de una Propuesta**:
   - Definir: Explorar el problema, validar que otros usuarios de MCP enfrentan un problema similar.
   - Prototipar: Construir una solución de ejemplo y demostrar su aplicación práctica.
   - Escribir: Basado en el prototipo, redactar una propuesta de especificación.

### Configuración del Entorno de Desarrollo

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

### Ejemplo: Contribuir con una Corrección de Error

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

### Ejemplo: Contribuir con una Nueva Herramienta a la Biblioteca Estándar

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

### Directrices para Contribuir

Para realizar una contribución exitosa a los proyectos de MCP:

1. **Comienza Pequeño**: Empieza con documentación, correcciones de errores o pequeñas mejoras.
2. **Sigue la Guía de Estilo**: Adhiérete al estilo de codificación y convenciones del proyecto.
3. **Escribe Pruebas**: Incluye pruebas unitarias para tus contribuciones de código.
4. **Documenta tu Trabajo**: Agrega documentación clara para nuevas características o cambios.
5. **Envía PRs Enfocados**: Mantén las solicitudes de extracción enfocadas en un solo problema o característica.
6. **Responde a los Comentarios**: Sé receptivo a los comentarios sobre tus contribuciones.

### Flujo de Trabajo de Ejemplo para Contribuciones

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

## Crear y Compartir Servidores MCP

Una de las formas más valiosas de contribuir al ecosistema de MCP es creando y compartiendo servidores MCP personalizados. La comunidad ya ha desarrollado cientos de servidores para diversos servicios y casos de uso.

### Marcos de Desarrollo de Servidores MCP

Existen varios marcos para simplificar el desarrollo de servidores MCP:

1. **SDKs Oficiales**:
   - [SDK de TypeScript](https://github.com/modelcontextprotocol/typescript-sdk)
   - [SDK de Python](https://github.com/modelcontextprotocol/python-sdk)
   - [SDK de C#](https://github.com/modelcontextprotocol/csharp-sdk)
   - [SDK de Go](https://github.com/modelcontextprotocol/go-sdk)
   - [SDK de Java](https://github.com/modelcontextprotocol/java-sdk)
   - [SDK de Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Marcos Comunitarios**:
   - [MCP-Framework](https://mcp-framework.com/) - Construye servidores MCP con elegancia y rapidez en TypeScript.
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Servidores MCP impulsados por anotaciones en Java.
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Marco de Java para servidores MCP.
   - [Plantilla de Servidor MCP para Next.js](https://github.com/vercel-labs/mcp-for-next.js) - Proyecto inicial de Next.js para servidores MCP.

### Desarrollar Herramientas Compartibles

#### Ejemplo en .NET: Crear un Paquete de Herramientas Compartible

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

#### Ejemplo en Java: Crear un Paquete Maven para Herramientas

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

#### Ejemplo en Python: Publicar un Paquete en PyPI

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

### Compartir Mejores Prácticas

Al compartir herramientas MCP con la comunidad:

1. **Documentación Completa**:
   - Documenta el propósito, uso y ejemplos.
   - Explica parámetros y valores de retorno.
   - Documenta cualquier dependencia externa.

2. **Manejo de Errores**:
   - Implementa un manejo de errores robusto.
   - Proporciona mensajes de error útiles.
   - Maneja casos extremos de manera adecuada.

3. **Consideraciones de Rendimiento**:
   - Optimiza tanto para velocidad como para uso de recursos.
   - Implementa caché cuando sea apropiado.
   - Considera la escalabilidad.

4. **Seguridad**:
   - Usa claves API y autenticación seguras.
   - Valida y sanitiza entradas.
   - Implementa limitación de tasa para llamadas a APIs externas.

5. **Pruebas**:
   - Incluye una cobertura de pruebas completa.
   - Prueba con diferentes tipos de entrada y casos extremos.
   - Documenta los procedimientos de prueba.

## Colaboración Comunitaria y Mejores Prácticas

La colaboración efectiva es clave para un ecosistema MCP próspero.

### Canales de Comunicación

- Issues y Discusiones en GitHub.
- Microsoft Tech Community.
- Canales de Discord y Slack.
- Stack Overflow (etiqueta: `model-context-protocol` o `mcp`).

### Revisiones de Código

Al revisar contribuciones a MCP:

1. **Claridad**: ¿El código es claro y está bien documentado?
2. **Corrección**: ¿Funciona como se espera?
3. **Consistencia**: ¿Sigue las convenciones del proyecto?
4. **Completitud**: ¿Incluye pruebas y documentación?
5. **Seguridad**: ¿Existen preocupaciones de seguridad?

### Compatibilidad de Versiones

Al desarrollar para MCP:

1. **Versionado del Protocolo**: Adhiérete a la versión del protocolo MCP que soporta tu herramienta.
2. **Compatibilidad con Clientes**: Considera la compatibilidad hacia atrás.
3. **Compatibilidad con Servidores**: Sigue las directrices de implementación de servidores.
4. **Cambios Rompedores**: Documenta claramente cualquier cambio rompedor.

## Proyecto Comunitario de Ejemplo: Registro de Herramientas MCP

Una contribución comunitaria importante podría ser desarrollar un registro público para herramientas MCP.

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

## Puntos Clave

- La comunidad MCP es diversa y da la bienvenida a varios tipos de contribuciones.
- Contribuir a MCP puede abarcar desde mejoras al protocolo principal hasta herramientas personalizadas.
- Seguir las directrices de contribución mejora las posibilidades de que tu PR sea aceptado.
- Crear y compartir herramientas MCP es una forma valiosa de mejorar el ecosistema.
- La colaboración comunitaria es esencial para el crecimiento y mejora de MCP.

## Ejercicio

1. Identifica un área en el ecosistema MCP donde puedas hacer una contribución basada en tus habilidades e intereses.
2. Haz un fork del repositorio de MCP y configura un entorno de desarrollo local.
3. Crea una pequeña mejora, corrección de error o herramienta que beneficie a la comunidad.
4. Documenta tu contribución con pruebas y documentación adecuadas.
5. Envía una solicitud de extracción al repositorio correspondiente.

## Recursos Adicionales

- [Proyectos Comunitarios de MCP](https://github.com/topics/model-context-protocol)

---

Siguiente: [Lecciones de la Adopción Temprana](../07-LessonsfromEarlyAdoption/README.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.