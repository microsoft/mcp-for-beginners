# Integración Multi-Modal

Las aplicaciones multi-modales están cobrando cada vez más importancia en la IA, permitiendo interacciones más ricas y tareas más complejas. El Protocolo de Contexto del Modelo (MCP) ofrece un marco para construir aplicaciones multi-modales que pueden manejar diversos tipos de datos, como texto, imágenes y audio.

MCP no solo soporta interacciones basadas en texto, sino también capacidades multi-modales, permitiendo que los modelos trabajen con imágenes, audio y otros tipos de datos.

## Introducción

En esta lección, aprenderás a construir una aplicación multi-modal.

## Objetivos de Aprendizaje

Al finalizar esta lección, serás capaz de:

- Entender las opciones multi-modales
- Implementar una aplicación multi-modal.

## Arquitectura para Soporte Multi-Modal

Las implementaciones multi-modales de MCP generalmente involucran:

- **Parseadores Específicos por Modalidad**: Componentes que convierten diferentes tipos de medios en formatos que el modelo puede procesar.
- **Herramientas Específicas por Modalidad**: Herramientas especiales diseñadas para manejar modalidades específicas (análisis de imágenes, procesamiento de audio)
- **Gestión Unificada del Contexto**: Sistema para mantener el contexto a través de diferentes modalidades
- **Generación de Respuestas**: Capacidad para generar respuestas que pueden incluir múltiples modalidades.

## Ejemplo Multi-Modal: Análisis de Imágenes

En el siguiente ejemplo, analizaremos una imagen y extraeremos información.

### Implementación en C#

```csharp
using ModelContextProtocol.SDK.Server;
using ModelContextProtocol.SDK.Server.Tools;
using ModelContextProtocol.SDK.Server.Content;
using System.Text.Json;
using System.IO;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace MultiModalMcpExample
{
    // Tool for image analysis
    public class ImageAnalysisTool : ITool
    {
        private readonly IImageAnalysisService _imageService;
        
        public ImageAnalysisTool(IImageAnalysisService imageService)
        {
            _imageService = imageService;
        }
        
        public string Name => "imageAnalysis";
        public string Description => "Analyzes image content and extracts information";
          public ToolDefinition GetDefinition()
        {
            return new ToolDefinition
            {
                Name = Name,
                Description = Description,
                Parameters = new Dictionary<string, ParameterDefinition>
                {
                    ["imageUrl"] = new ParameterDefinition
                    {
                        Type = ParameterType.String,
                        Description = "URL to the image to analyze" 
                    },
                    ["analysisType"] = new ParameterDefinition
                    {
                        Type = ParameterType.String,
                        Description = "Type of analysis to perform",
                        Enum = new[] { "general", "objects", "text", "faces" },
                        Default = "general"
                    }
                },
                Required = new[] { "imageUrl" }
            };
        }
        
        public async Task<ToolResponse> ExecuteAsync(IDictionary<string, object> parameters)
        {
            // Extract parameters
            string imageUrl = parameters["imageUrl"].ToString();
            string analysisType = parameters.ContainsKey("analysisType") 
                ? parameters["analysisType"].ToString() 
                : "general";
              // Download or access the image
            byte[] imageData = await DownloadImageAsync(imageUrl);
            
            // Analyze based on the requested analysis type
            var analysisResult = analysisType switch
            {
                "objects" => await _imageService.DetectObjectsAsync(imageData),                "text" => await _imageService.RecognizeTextAsync(imageData),
                "faces" => await _imageService.DetectFacesAsync(imageData),
                _ => await _imageService.AnalyzeGeneralAsync(imageData) // Default general analysis
            };
            
            // Return structured result as a ToolResponse
            // Format follows the MCP specification for content structure
            var content = new List<ContentItem>
            {
                new ContentItem
                {
                    Type = ContentType.Text,
                    Text = JsonSerializer.Serialize(analysisResult)
                }
            };
            
            return new ToolResponse
            {
                Content = content,
                IsError = false
            };
        }
        
        private async Task<byte[]> DownloadImageAsync(string url)
        {
            using var httpClient = new HttpClient();
            return await httpClient.GetByteArrayAsync(url);
        }
    }
    
    // Multi-modal MCP server with image and text processing
    public class MultiModalMcpServer
    {
        public static async Task Main(string[] args)
        {
            // Create an MCP server
            var server = new McpServer(
                name: "Multi-Modal MCP Server",
                version: "1.0.0"
            );
            
            // Configure server for multi-modal support
            var serverOptions = new McpServerOptions
            {
                MaxRequestSize = 10 * 1024 * 1024, // 10MB for larger payloads like images
                SupportedContentTypes = new[]
                {
                    "image/jpeg",
                    "image/png",
                    "text/plain",
                    "application/json"
                }
            };
            
            // Create image analysis service
            var imageService = new ComputerVisionService();
            
            // Register image analysis tools
            server.AddTool(new ImageAnalysisTool(imageService));
            
            // Register a text-to-image tool
            services.AddMcpTool<TextAnalysisTool>();
            services.AddMcpTool<ImageAnalysisTool>();
            services.AddMcpTool<DocumentGenerationTool>(); // Tool that can generate documents with text and images
        }
    }
}
```

En el ejemplo anterior, hemos:

- Creado un `ImageAnalysisTool` que puede analizar imágenes usando un hipotético `IImageAnalysisService`.
- Configurado el servidor MCP para manejar solicitudes más grandes y soportar tipos de contenido de imagen.
- Registrado la herramienta de análisis de imágenes con el servidor.
- Implementado un método para descargar imágenes desde una URL y analizarlas según el tipo solicitado (objetos, texto, rostros, etc.).
- Devuelto resultados estructurados en un formato compatible con la especificación MCP.

## Ejemplo Multi-Modal: Procesamiento de Audio

El procesamiento de audio es otra modalidad común en aplicaciones multi-modales. A continuación, un ejemplo de cómo implementar una herramienta de transcripción de audio que puede manejar archivos de audio y devolver transcripciones.

### Implementación en Java

```java
package com.example.mcp.multimodal;

import com.mcp.server.McpServer;
import com.mcp.tools.Tool;
import com.mcp.tools.ToolRequest;
import com.mcp.tools.ToolResponse;
import com.mcp.tools.ToolExecutionException;
import com.example.audio.AudioProcessor;

import java.util.Base64;
import java.util.HashMap;
import java.util.Map;

// Audio transcription tool
public class AudioTranscriptionTool implements Tool {
    private final AudioProcessor audioProcessor;
    
    public AudioTranscriptionTool(AudioProcessor audioProcessor) {
        this.audioProcessor = audioProcessor;
    }
    
    @Override
    public String getName() {
        return "audioTranscription";
    }
    
    @Override
    public String getDescription() {
        return "Transcribes speech from audio files to text";
    }
    
    @Override
    public Object getSchema() {
        Map<String, Object> schema = new HashMap<>();
        schema.put("type", "object");
        
        Map<String, Object> properties = new HashMap<>();
        
        Map<String, Object> audioUrl = new HashMap<>();
        audioUrl.put("type", "string");
        audioUrl.put("description", "URL to the audio file to transcribe");
        
        Map<String, Object> audioData = new HashMap<>();
        audioData.put("type", "string");
        audioData.put("description", "Base64-encoded audio data (alternative to URL)");
        
        Map<String, Object> language = new HashMap<>();
        language.put("type", "string");
        language.put("description", "Language code (e.g., 'en-US', 'es-ES')");
        language.put("default", "en-US");
        
        properties.put("audioUrl", audioUrl);
        properties.put("audioData", audioData);
        properties.put("language", language);
        
        schema.put("properties", properties);
        schema.put("required", Arrays.asList("audioUrl"));
        
        return schema;
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        try {
            byte[] audioData;
            String language = request.getParameters().has("language") ? 
                request.getParameters().get("language").asText() : "en-US";
                
            // Get audio either from URL or direct data
            if (request.getParameters().has("audioUrl")) {
                String audioUrl = request.getParameters().get("audioUrl").asText();
                audioData = downloadAudio(audioUrl);
            } else if (request.getParameters().has("audioData")) {
                String base64Audio = request.getParameters().get("audioData").asText();
                audioData = Base64.getDecoder().decode(base64Audio);
            } else {
                throw new ToolExecutionException("Either audioUrl or audioData must be provided");
            }
            
            // Process audio and transcribe
            Map<String, Object> transcriptionResult = audioProcessor.transcribe(audioData, language);
            
            // Return transcription result
            return new ToolResponse.Builder()
                .setResult(transcriptionResult)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Audio transcription failed: " + ex.getMessage(), ex);
        }
    }
    
    private byte[] downloadAudio(String url) {
        // Implementation for downloading audio from URL
        // ...
        return new byte[0]; // Placeholder
    }
}

// Main application with audio and other modalities
public class MultiModalApplication {
    public static void main(String[] args) {
        // Configure services
        AudioProcessor audioProcessor = new AudioProcessor();
        ImageProcessor imageProcessor = new ImageProcessor();
        
        // Create and configure server
        McpServer server = new McpServer.Builder()
            .setName("Multi-Modal MCP Server")
            .setVersion("1.0.0")
            .setPort(5000)
            .setMaxRequestSize(20 * 1024 * 1024) // 20MB for audio/video content
            .build();
            
        // Register multi-modal tools
        server.registerTool(new AudioTranscriptionTool(audioProcessor));
        server.registerTool(new ImageAnalysisTool(imageProcessor));
        server.registerTool(new VideoProcessingTool());
        
        // Start server
        server.start();
        System.out.println("Multi-Modal MCP Server started on port 5000");
    }
}
```

En el ejemplo anterior, hemos:

- Creado un `AudioTranscriptionTool` que puede transcribir archivos de audio.
- Definido el esquema de la herramienta para aceptar ya sea una URL o datos de audio codificados en base64.
- Implementado el método `execute` para manejar el procesamiento y la transcripción de audio.
- Configurado el servidor MCP para manejar solicitudes multi-modales, incluyendo procesamiento de audio e imágenes.
- Registrado la herramienta de transcripción de audio con el servidor.
- Implementado un método para descargar archivos de audio desde una URL o decodificar datos de audio en base64.
- Usado un servicio `AudioProcessor` para manejar la lógica real de transcripción.
- Iniciado el servidor MCP para escuchar solicitudes.

### Ejemplo Multi-Modal: Generación de Respuestas Multi-Modales

### Implementación en Python

```python
from mcp_server import McpServer
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
import base64
from PIL import Image
import io
import requests
import json
from typing import Dict, Any, List, Optional

# Image generation tool
class ImageGenerationTool(Tool):
    def get_name(self):
        return "imageGeneration"
        
    def get_description(self):
        return "Generates images based on text descriptions"
    
    def get_schema(self):
        return {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string", 
                    "description": "Text description of the image to generate"
                },
                "style": {
                    "type": "string",
                    "enum": ["realistic", "artistic", "cartoon", "sketch"],
                    "default": "realistic"
                },
                "width": {
                    "type": "integer",
                    "default": 512
                },
                "height": {
                    "type": "integer",
                    "default": 512
                }
            },
            "required": ["prompt"]
        }
    
    async def execute_async(self, request: ToolRequest) -> ToolResponse:
        try:
            # Extract parameters
            prompt = request.parameters.get("prompt")
            style = request.parameters.get("style", "realistic")
            width = request.parameters.get("width", 512)
            height = request.parameters.get("height", 512)
            
            # Generate image using external service (example implementation)
            image_data = await self._generate_image(prompt, style, width, height)
            
            # Convert image to base64 for response
            buffered = io.BytesIO()
            image_data.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            # Return result with both the image and metadata
            return ToolResponse(
                result={
                    "imageBase64": img_str,
                    "format": "image/png",
                    "width": width,
                    "height": height,
                    "generationPrompt": prompt,
                    "style": style
                }
            )
        except Exception as e:
            raise ToolExecutionException(f"Image generation failed: {str(e)}")
    
    async def _generate_image(self, prompt: str, style: str, width: int, height: int) -> Image.Image:
        """
        This would call an actual image generation API
        Simplified placeholder implementation
        """
        # Return a placeholder image or call actual image generation API
        # For this example, we'll create a simple colored image
        image = Image.new('RGB', (width, height), color=(73, 109, 137))
        return image

# Multi-modal response handler
class MultiModalResponseHandler:
    """Handler for creating responses that combine text, images, and other modalities"""
    
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def create_multi_modal_response(self, 
                                         text_content: str, 
                                         generate_images: bool = False,
                                         image_prompts: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Creates a response that may include generated images alongside text
        """
        response = {
            "text": text_content,
            "images": []
        }
        
        # Generate images if requested
        if generate_images and image_prompts:
            for prompt in image_prompts:
                image_result = await self.client.execute_tool(
                    "imageGeneration",
                    {
                        "prompt": prompt,
                        "style": "realistic",
                        "width": 512,
                        "height": 512
                    }
                )
                
                response["images"].append({
                    "imageData": image_result.result["imageBase64"],
                    "format": image_result.result["format"],
                    "prompt": prompt
                })
        
        return response

# Main application
async def main():
    # Create server
    server = McpServer(
        name="Multi-Modal MCP Server",
        version="1.0.0",
        port=5000
    )
    
    # Register multi-modal tools
    server.register_tool(ImageGenerationTool())
    server.register_tool(AudioAnalysisTool())
    server.register_tool(VideoFrameExtractionTool())
    
    # Start server
    await server.start()
    print("Multi-Modal MCP Server running on port 5000")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## Qué sigue

- [5.3 Oauth 2](../mcp-oauth2-demo/README.md)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.