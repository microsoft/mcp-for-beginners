# Communauté et Contributions

[![Comment contribuer à MCP : outils, documentation, code et plus](../../../translated_images/fr/07.1179f6de46ff196e.webp)](https://youtu.be/v1pvCYAWpRE)

_(Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon)_

## Aperçu

Cette leçon explique comment s'engager avec la communauté MCP, contribuer à l'écosystème MCP et suivre les meilleures pratiques pour le développement collaboratif. Comprendre comment participer aux projets open-source MCP est essentiel pour ceux qui souhaitent façonner l'avenir de cette technologie.

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- Comprendre la structure de la communauté et de l'écosystème MCP
- Participer efficacement aux forums et discussions de la communauté MCP
- Contribuer aux dépôts open-source MCP
- Créer et partager des outils et serveurs MCP personnalisés
- Suivre les meilleures pratiques pour le développement et la collaboration MCP
- Découvrir les ressources et cadres communautaires pour le développement MCP

## L'écosystème de la communauté MCP

L'écosystème MCP est composé de divers éléments et participants qui collaborent pour faire avancer le protocole.

### Principaux éléments de la communauté

1. **Mainteneurs du protocole principal** : L'organisation officielle [Model Context Protocol GitHub](https://github.com/modelcontextprotocol) gère les spécifications principales MCP et les implémentations de référence.
2. **Développeurs d'outils** : Individus et équipes qui créent des outils et serveurs MCP.
3. **Fournisseurs d'intégration** : Entreprises qui intègrent MCP dans leurs produits et services.
4. **Utilisateurs finaux** : Développeurs et organisations qui utilisent MCP dans leurs applications.
5. **Contributeurs** : Membres de la communauté qui apportent du code, de la documentation ou d'autres ressources.

### Ressources communautaires

#### Canaux officiels

- [Organisation GitHub MCP](https://github.com/modelcontextprotocol)
- [Documentation MCP](https://modelcontextprotocol.io/)
- [Spécification MCP](https://modelcontextprotocol.io/docs/specification)
- [Discussions GitHub](https://github.com/orgs/modelcontextprotocol/discussions)
- [Dépôt d'exemples et serveurs MCP](https://github.com/modelcontextprotocol/servers)

#### Ressources communautaires

- [Clients MCP](https://modelcontextprotocol.io/clients) - Liste des clients prenant en charge les intégrations MCP.
- [Serveurs communautaires MCP](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) - Liste croissante de serveurs MCP développés par la communauté.
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers) - Liste sélectionnée de serveurs MCP.
- [PulseMCP](https://www.pulsemcp.com/) - Hub communautaire et newsletter pour découvrir les ressources MCP.
- [Serveur Discord](https://discord.gg/jHEGxQu2a5) - Connectez-vous avec les développeurs MCP.
- Implémentations SDK spécifiques aux langages.
- Articles de blog et tutoriels.

## Contribuer à MCP

### Types de contributions

L'écosystème MCP accueille divers types de contributions :

1. **Contributions de code** :
   - Améliorations du protocole principal.
   - Corrections de bugs.
   - Implémentations d'outils et de serveurs.
   - Bibliothèques client/serveur dans différents langages.

2. **Documentation** :
   - Amélioration de la documentation existante.
   - Création de tutoriels et guides.
   - Traduction de la documentation.
   - Création d'exemples et d'applications modèles.

3. **Support communautaire** :
   - Répondre aux questions sur les forums et discussions.
   - Tester et signaler les problèmes.
   - Organiser des événements communautaires.
   - Mentorer de nouveaux contributeurs.

### Processus de contribution : Protocole principal

Pour contribuer au protocole principal MCP ou aux implémentations officielles, suivez ces principes des [directives de contribution officielles](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md) :

1. **Simplicité et minimalisme** : La spécification MCP maintient un haut niveau d'exigence pour l'ajout de nouveaux concepts. Il est plus facile d'ajouter des éléments à une spécification que de les retirer.

2. **Approche concrète** : Les modifications de la spécification doivent être basées sur des défis d'implémentation spécifiques, et non sur des idées spéculatives.

3. **Étapes d'une proposition** :
   - Définir : Explorer l'espace problématique, valider que d'autres utilisateurs MCP rencontrent un problème similaire.
   - Prototyper : Construire une solution exemple et démontrer son application pratique.
   - Rédiger : Sur la base du prototype, rédiger une proposition de spécification.

### Configuration de l'environnement de développement

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

### Exemple : Contribuer à une correction de bug

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

### Exemple : Contribuer à un nouvel outil pour la bibliothèque standard

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

### Directives de contribution

Pour réussir une contribution aux projets MCP :

1. **Commencez petit** : Débutez par la documentation, les corrections de bugs ou de petites améliorations.
2. **Suivez le guide de style** : Respectez le style de codage et les conventions du projet.
3. **Écrivez des tests** : Incluez des tests unitaires pour vos contributions de code.
4. **Documentez votre travail** : Ajoutez une documentation claire pour les nouvelles fonctionnalités ou modifications.
5. **Soumettez des PR ciblées** : Gardez les pull requests concentrées sur un problème ou une fonctionnalité unique.
6. **Engagez-vous avec les retours** : Soyez réactif aux commentaires sur vos contributions.

### Exemple de workflow de contribution

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

## Créer et partager des serveurs MCP

L'une des façons les plus précieuses de contribuer à l'écosystème MCP est de créer et partager des serveurs MCP personnalisés. La communauté a déjà développé des centaines de serveurs pour divers services et cas d'utilisation.

### Cadres de développement de serveurs MCP

Plusieurs cadres sont disponibles pour simplifier le développement de serveurs MCP :

1. **SDK officiels** :
   - [SDK TypeScript](https://github.com/modelcontextprotocol/typescript-sdk)
   - [SDK Python](https://github.com/modelcontextprotocol/python-sdk)
   - [SDK C#](https://github.com/modelcontextprotocol/csharp-sdk)
   - [SDK Go](https://github.com/modelcontextprotocol/go-sdk)
   - [SDK Java](https://github.com/modelcontextprotocol/java-sdk)
   - [SDK Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk)

2. **Cadres communautaires** :
   - [MCP-Framework](https://mcp-framework.com/) - Construisez des serveurs MCP avec élégance et rapidité en TypeScript.
   - [MCP Declarative Java SDK](https://github.com/codeboyzhou/mcp-declarative-java-sdk) - Serveurs MCP basés sur des annotations en Java.
   - [Quarkus MCP Server SDK](https://github.com/quarkiverse/quarkus-mcp-server) - Cadre Java pour serveurs MCP.
   - [Template de serveur MCP Next.js](https://github.com/vercel-labs/mcp-for-next.js) - Projet de démarrage Next.js pour serveurs MCP.

### Développer des outils partageables

#### Exemple .NET : Créer un package d'outils partageable

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

#### Exemple Java : Créer un package Maven pour outils

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

#### Exemple Python : Publier un package PyPI

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

### Partager les meilleures pratiques

Lors du partage d'outils MCP avec la communauté :

1. **Documentation complète** :
   - Documentez l'objectif, l'utilisation et les exemples.
   - Expliquez les paramètres et les valeurs de retour.
   - Documentez les dépendances externes.

2. **Gestion des erreurs** :
   - Implémentez une gestion robuste des erreurs.
   - Fournissez des messages d'erreur utiles.
   - Gérez les cas limites avec soin.

3. **Considérations de performance** :
   - Optimisez à la fois pour la vitesse et l'utilisation des ressources.
   - Implémentez la mise en cache si nécessaire.
   - Prenez en compte l'évolutivité.

4. **Sécurité** :
   - Utilisez des clés API et une authentification sécurisées.
   - Validez et nettoyez les entrées.
   - Implémentez des limites de taux pour les appels API externes.

5. **Tests** :
   - Incluez une couverture de test complète.
   - Testez avec différents types d'entrées et cas limites.
   - Documentez les procédures de test.

## Collaboration communautaire et meilleures pratiques

Une collaboration efficace est essentielle pour un écosystème MCP florissant.

### Canaux de communication

- Issues et discussions GitHub.
- Microsoft Tech Community.
- Canaux Discord et Slack.
- Stack Overflow (tags : `model-context-protocol` ou `mcp`).

### Revues de code

Lors de la revue des contributions MCP :

1. **Clarté** : Le code est-il clair et bien documenté ?
2. **Exactitude** : Fonctionne-t-il comme prévu ?
3. **Cohérence** : Respecte-t-il les conventions du projet ?
4. **Complétude** : Les tests et la documentation sont-ils inclus ?
5. **Sécurité** : Y a-t-il des préoccupations de sécurité ?

### Compatibilité des versions

Lors du développement pour MCP :

1. **Versionnement du protocole** : Respectez la version du protocole MCP que votre outil prend en charge.
2. **Compatibilité client** : Prenez en compte la rétrocompatibilité.
3. **Compatibilité serveur** : Suivez les directives d'implémentation des serveurs.
4. **Modifications majeures** : Documentez clairement toute modification majeure.

## Exemple de projet communautaire : Registre d'outils MCP

Une contribution communautaire importante pourrait être le développement d'un registre public pour les outils MCP.

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

## Points clés

- La communauté MCP est diversifiée et accueille divers types de contributions.
- Contribuer à MCP peut aller des améliorations du protocole principal aux outils personnalisés.
- Suivre les directives de contribution augmente les chances d'acceptation de votre PR.
- Créer et partager des outils MCP est une manière précieuse d'améliorer l'écosystème.
- La collaboration communautaire est essentielle pour la croissance et l'amélioration de MCP.

## Exercice

1. Identifiez un domaine de l'écosystème MCP où vous pourriez contribuer en fonction de vos compétences et intérêts.
2. Forkez le dépôt MCP et configurez un environnement de développement local.
3. Créez une petite amélioration, correction de bug ou outil qui bénéficierait à la communauté.
4. Documentez votre contribution avec des tests et une documentation appropriés.
5. Soumettez une pull request au dépôt approprié.

## Ressources supplémentaires

- [Projets communautaires MCP](https://github.com/topics/model-context-protocol)

---

Suivant : [Leçons tirées de l'adoption précoce](../07-LessonsfromEarlyAdoption/README.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.