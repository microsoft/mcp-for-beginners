# Comunidade e Contribuições

[![Como Contribuir para o MCP: Ferramentas, Documentação, Código e Mais](../../../translated_images/pt-PT/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Clique na imagem acima para ver o vídeo desta lição)_

## Visão Geral

Esta lição foca-se em como interagir com a comunidade MCP, contribuir para o ecossistema MCP e seguir as melhores práticas para desenvolvimento colaborativo. Compreender como participar em projetos MCP open-source é essencial para quem pretende moldar o futuro desta tecnologia.

## Objetivos de Aprendizagem

No final desta lição, você será capaz de:

- Compreender a estrutura da comunidade e do ecossistema MCP
- Participar efetivamente nos fóruns e discussões da comunidade MCP
- Contribuir para repositórios open-source MCP
- Criar e partilhar ferramentas e servidores MCP personalizados
- Seguir as melhores práticas para desenvolvimento e colaboração MCP
- Descobrir recursos e frameworks comunitários para desenvolvimento MCP

## O Ecossistema da Comunidade MCP

O ecossistema MCP consiste em vários componentes e participantes que trabalham em conjunto para avançar o protocolo.

### Componentes Principais da Comunidade

1. **Mantenedores do Protocolo Core**: A oficial [organização Model Context Protocol GitHub](https://github.com/modelcontextprotocol) mantém as especificações core MCP e implementações de referência
2. **Desenvolvedores de Ferramentas**: Indivíduos e equipas que criam ferramentas e servidores MCP
3. **Fornecedores de Integração**: Empresas que integram MCP nos seus produtos e serviços
4. **Utilizadores Finais**: Desenvolvedores e organizações que usam MCP nas suas aplicações
5. **Contribuidores**: Membros da comunidade que contribuem com código, documentação ou outros recursos

### Recursos da Comunidade

#### Canais Oficiais

- [Organização MCP no GitHub](https://github.com/modelcontextprotocol)
- [Documentação MCP](https://modelcontextprotocol.io/)
- [Especificação MCP](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Discussões no GitHub](https://github.com/orgs/modelcontextprotocol/discussions)
- [Repositório de Exemplos & Servidores MCP](https://github.com/modelcontextprotocol/servers)

#### Recursos Comunitários

- [Clientes MCP](https://modelcontextprotocol.io/clients) - Lista de clientes que suportam integrações MCP
- [Servidores MCP Comunitários](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Lista crescente de servidores MCP desenvolvidos pela comunidade
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Lista selecionada de servidores MCP
- [PulseMCP](https://www.pulsemcp.com/) - Centro comunitário & newsletter para descobrir recursos MCP
- [Remote OpenClaw](https://www.remoteopenclaw.com/) - Diretório pesquisável gratuito de servidores MCP, skills de agentes e plugins
- [Servidor Discord](https://discord.gg/jHEGxQu2a5) - Conecte-se com desenvolvedores MCP
- Implementações SDK específicas de linguagem
- Publicações em blogs e tutoriais

## Contribuindo para o MCP

### Tipos de Contribuições

O ecossistema MCP acolhe vários tipos de contribuições:

1. **Contribuições de Código**:
   - Melhorias no protocolo core
   - Correções de bugs
   - Implementações de ferramentas e servidores
   - Bibliotecas cliente/servidor em diferentes linguagens

2. **Documentação**:
   - Melhorar documentação existente
   - Criar tutoriais e guias
   - Traduzir documentação
   - Criar exemplos e aplicações demonstrativas

3. **Suporte Comunitário**:
   - Responder perguntas em fóruns e discussões
   - Testar e reportar problemas
   - Organizar eventos comunitários
   - Orientar novos contribuidores

### Processo de Contribuição: Protocolo Core

Para contribuir com o protocolo core MCP ou implementações oficiais, siga estes princípios das [diretrizes oficiais de contribuição](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md):

1. **Simplicidade e Minimalismo**: A especificação MCP mantém um padrão elevado para adicionar novos conceitos. É mais fácil adicionar coisas a uma especificação do que removê-las.

2. **Abordagem Concreta**: Alterações na especificação devem basear-se em desafios de implementação específicos e não em ideias especulativas.

3. **Fases de uma Proposta**:
   - Definir: Explorar o problema, validar que outros utilizadores MCP enfrentam um problema semelhante
   - Prototipar: Construir uma solução de exemplo e demonstrar sua aplicação prática
   - Escrever: Com base no protótipo, redigir uma proposta de especificação

### Configuração do Ambiente de Desenvolvimento

```bash
# Criar um fork do repositório
git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
cd modelcontextprotocol

# Instalar dependências
npm install

# Para alterações no esquema, validar e gerar schema.json:
npm run check:schema:ts
npm run generate:schema

# Para alterações na documentação
npm run check:docs
npm run format

# Pré-visualizar a documentação localmente (opcional):
npm run serve:docs
```

### Exemplo: Contribuindo com uma Correção de Bug

```javascript
// Código original com erro no typescript-sdk
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Erro: Validação da propriedade em falta
  // Implementação atual:
  const hasName = 'name' in resource;
  const hasSchema = 'schema' in resource;
  
  return hasName && hasSchema;
}

// Implementação corrigida numa contribuição
export function validateResource(resource: unknown): resource is MCPResource {
  if (!resource || typeof resource !== 'object') {
    return false;
  }
  
  // Validação melhorada
  const hasName = 'name' in resource && typeof (resource as MCPResource).name === 'string';
  const hasSchema = 'schema' in resource && typeof (resource as MCPResource).schema === 'object';
  const hasDescription = !('description' in resource) || typeof (resource as MCPResource).description === 'string';
  
  return hasName && hasSchema && hasDescription;
}
```

### Exemplo: Contribuindo com uma Nova Ferramenta para a Biblioteca Padrão

```python
# Exemplo de contribuição: Uma ferramenta de processamento de dados CSV para a biblioteca padrão MCP

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
            # Extrair parâmetros
            operation = request.parameters.get("operation")
            output_format = request.parameters.get("outputFormat", "json")
            
            # Obter dados CSV a partir de dados diretos ou URL
            df = await self._get_dataframe(request)
            
            # Processar com base na operação solicitada
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
        # A implementação incluiria várias transformações
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

### Diretrizes de Contribuição

Para fazer uma contribuição bem-sucedida em projetos MCP:

1. **Comece Pequeno**: Inicie com documentação, correções de bugs ou pequenas melhorias
2. **Siga o Guia de Estilo**: Adira ao estilo de codificação e às convenções do projeto
3. **Escreva Testes**: Inclua testes unitários para as suas contribuições de código
4. **Documente o Seu Trabalho**: Adicione documentação clara para novas funcionalidades ou alterações
5. **Submeta Pull Requests Direcionados**: Mantenha os pull requests focados em uma única questão ou funcionalidade
6. **Interaja com o Feedback**: Seja responsivo ao feedback sobre as suas contribuições

### Exemplo de Fluxo de Trabalho de Contribuição

```bash
# Clonar o repositório
git clone https://github.com/modelcontextprotocol/typescript-sdk.git
cd typescript-sdk

# Criar um novo branch para a tua contribuição
git checkout -b feature/my-contribution

# Fazer as tuas alterações
# ...

# Executar testes para garantir que as tuas alterações não quebram a funcionalidade existente
npm test

# Cometer as tuas alterações com uma mensagem descritiva
git commit -am "Fix validation in resource handler"

# Enviar o teu branch para o teu fork
git push origin feature/my-contribution

# Criar um pull request do teu branch para o repositório principal
# Depois, interagir com o feedback e iterar o teu PR conforme necessário
```

## Criar e Partilhar Servidores MCP

Uma das formas mais valiosas de contribuir para o ecossistema MCP é criar e partilhar servidores MCP personalizados. A comunidade já desenvolveu centenas de servidores para vários serviços e casos de uso.

### Frameworks de Desenvolvimento de Servidores MCP

Existem vários frameworks disponíveis para simplificar o desenvolvimento de servidores MCP:

1. **SDKs Oficiais** (verifique a
    [documentação SDK](https://modelcontextprotocol.io/docs/sdk) para cada
    revisão de protocolo suportada pelo SDK):
   - [SDK TypeScript](https://github.com/modelcontextprotocol/typescript-sdk)
   - [SDK Python](https://github.com/modelcontextprotocol/python-sdk)
   - [SDK C#](https://github.com/modelcontextprotocol/csharp-sdk)
   - [SDK Go](https://github.com/modelcontextprotocol/go-sdk)
   - [SDK Java](https://github.com/modelcontextprotocol/java-sdk)
   - [SDK Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk)
   - [SDK Swift](https://github.com/modelcontextprotocol/swift-sdk)
   - [SDK Rust](https://github.com/modelcontextprotocol/rust-sdk)

2. **Frameworks Comunitários**:
   - [MCP-Framework](https://mcp-framework.com/) - Construa servidores MCP com elegância e rapidez em TypeScript
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Servidores MCP baseados em anotações com Java
   - [SDK Servidor Quarkus MCP](https://github.com/quarkiverse/quarkus-mcp-server) - Framework Java para servidores MCP
   - [Template Next.js para Servidor MCP](https://github.com/vercel-labs/mcp-for-next.js) - Projeto inicial Next.js para servidores MCP

### Desenvolvimento de Ferramentas Partilháveis

#### Exemplo .NET: Criar um pacote de ferramentas partilháveis

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

#### Exemplo Java: Criar um pacote Maven para Ferramentas

```java
// configuração pom.xml para um pacote de ferramentas MCP compartilhável
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
        // Definição do esquema...
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            String location = request.getParameters().get("location").asText();
            int days = request.getParameters().has("days") ? 
                request.getParameters().get("days").asInt() : 3;
            
            // Consultar API do tempo
            Map<String, Object> forecast = getForecast(location, days);
            
            // Construir resposta
            return new ToolResponse.Builder()
                .setResult(forecast)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Weather forecast failed: " + ex.getMessage(), ex);
        }
    }
    
    private Map<String, Object> getForecast(String location, int days) {
        // A implementação chamaria a API do tempo
        // Exemplo simplificado
        Map<String, Object> result = new HashMap<>();
        // Adicionar dados de previsão...
        return result;
    }
}

// Construir e publicar usando Maven
// mvn clean package
// mvn deploy
```

#### Exemplo Python: Publicar um pacote PyPI

```python
# Estrutura de diretórios para um pacote PyPI:
# mcp_nlp_tools/
# ├── LICENSE
# ├── README.md
# ├── setup.py
# ├── mcp_nlp_tools/
# │   ├── __init__.py
# │   ├── sentiment_tool.py
# │   └── translation_tool.py

# Exemplo de setup.py
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

# Exemplo de implementação de ferramenta NLP (sentiment_tool.py)
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
from transformers import pipeline
import torch

class SentimentAnalysisTool(Tool):
    """MCP tool for sentiment analysis of text"""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        # Carregar o modelo de análise de sentimento
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
            # Extrair parâmetros
            text = request.parameters.get("text")
            include_score = request.parameters.get("includeScore", True)
            
            # Analisar sentimento
            sentiment_result = self.sentiment_analyzer(text)[0]
            
            # Formatar resultado
            result = {
                "sentiment": sentiment_result["label"],
                "text": text
            }
            
            if include_score:
                result["score"] = sentiment_result["score"]
            
            # Retornar resultado
            return ToolResponse(result=result)
            
        except Exception as e:
            raise ToolExecutionException(f"Sentiment analysis failed: {str(e)}")

# Para publicar:
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
```

### Partilha das Melhores Práticas

Ao partilhar ferramentas MCP com a comunidade:

1. **Documentação Completa**:
   - Documentar propósito, uso e exemplos
   - Explicar parâmetros e valores de retorno
   - Documentar quaisquer dependências externas

2. **Tratamento de Erros**:
   - Implementar tratamento de erro robusto
   - Fornecer mensagens de erro úteis
   - Tratar casos limite de forma elegante

3. **Considerações de Desempenho**:
   - Otimizar para velocidade e uso de recursos
   - Implementar caching quando adequado
   - Considerar escalabilidade

4. **Segurança**:
   - Usar chaves API seguras e autenticação
   - Validar e sanitizar entradas
   - Implementar limitação de taxa para chamadas API externas

5. **Testes**:
   - Incluir cobertura de teste abrangente
   - Testar com diferentes tipos de entrada e casos limite
   - Documentar procedimentos de teste

## Colaboração Comunitária e Melhores Práticas

A colaboração eficaz é chave para um ecossistema MCP próspero.

### Canais de Comunicação

- Issues e Discussões no GitHub
- Microsoft Tech Community
- Canais Discord e Slack
- Stack Overflow (tag: `model-context-protocol` ou `mcp`)

### Revisões de Código

Ao rever contribuições MCP:

1. **Clareza**: O código está claro e bem documentado?
2. **Correção**: Funciona conforme esperado?
3. **Consistência**: Segue as convenções do projeto?
4. **Completude**: Inclui testes e documentação?
5. **Segurança**: Existem preocupações de segurança?

### Compatibilidade de Versão

Ao desenvolver para MCP:

1. **Versionamento do Protocolo**: Adira à versão do protocolo MCP que a sua ferramenta suporta
2. **Compatibilidade com Clientes**: Considere compatibilidade retroativa
3. **Compatibilidade com Servidores**: Siga as diretrizes de implementação de servidores
4. **Mudanças Quebradoras**: Documente claramente qualquer mudança incompatível

## Projeto Comunitário Exemplo: Registro de Ferramentas MCP

Uma contribuição comunitária importante pode ser desenvolver um registro público para ferramentas MCP.

```python
# Exemplo de esquema para uma API de registo de ferramentas comunitárias

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import datetime
import uuid

# Modelos para o registo de ferramentas
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

# Aplicação FastAPI para o registo
app = FastAPI(title="MCP Tool Registry")

# Base de dados em memória para este exemplo
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

## Conclusões Principais

- A comunidade MCP é diversa e acolhe vários tipos de contribuições
- Contribuir para MCP pode variar de melhorias no protocolo core a ferramentas personalizadas
- Seguir as diretrizes de contribuição aumenta as chances de aceitação do seu PR
- Criar e partilhar ferramentas MCP é uma forma valiosa de aprimorar o ecossistema
- A colaboração comunitária é essencial para o crescimento e melhoria do MCP

## Exercício

1. Identifique uma área no ecossistema MCP onde possa contribuir com base nas suas competências e interesses
2. Faça um fork do repositório MCP e configure um ambiente de desenvolvimento local
3. Crie uma pequena melhoria, correção de bug ou ferramenta que beneficie a comunidade
4. Documente a sua contribuição com testes e documentação apropriados
5. Submeta um pull request para o repositório apropriado

## Recursos Adicionais

- [Projetos da Comunidade MCP](https://github.com/topics/model-context-protocol)

---

## O Que Vem a Seguir

Seguinte: [Lições da Adoção Inicial](../07-LessonsfromEarlyAdoption/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->