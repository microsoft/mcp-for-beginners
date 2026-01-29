# ਮਲਟੀ-ਮੋਡਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ

ਮਲਟੀ-ਮੋਡਲ ਐਪਲੀਕੇਸ਼ਨ AI ਵਿੱਚ ਦਿਨੋ-ਦਿਨ ਮਹੱਤਵਪੂਰਨ ਹੁੰਦੀਆਂ ਜਾ ਰਹੀਆਂ ਹਨ, ਜੋ ਵਧੇਰੇ ਗਹਿਰਾਈ ਵਾਲੀਆਂ ਗੱਲਬਾਤਾਂ ਅਤੇ ਜਟਿਲ ਕੰਮ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਦਿੰਦੀਆਂ ਹਨ। Model Context Protocol (MCP) ਇੱਕ ਐਸਾ ਫਰੇਮਵਰਕ ਹੈ ਜੋ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਡੇਟਾ, ਜਿਵੇਂ ਕਿ ਟੈਕਸਟ, ਚਿੱਤਰ ਅਤੇ ਆਡੀਓ ਨੂੰ ਸੰਭਾਲ ਸਕਣ ਵਾਲੀਆਂ ਮਲਟੀ-ਮੋਡਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਬਣਾਉਣ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ।

MCP ਸਿਰਫ ਟੈਕਸਟ-ਆਧਾਰਿਤ ਗੱਲਬਾਤਾਂ ਹੀ ਨਹੀਂ, ਸਗੋਂ ਮਲਟੀ-ਮੋਡਲ ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਵੀ ਸਹਿਯੋਗ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਮਾਡਲ ਚਿੱਤਰਾਂ, ਆਡੀਓ ਅਤੇ ਹੋਰ ਡੇਟਾ ਕਿਸਮਾਂ ਨਾਲ ਕੰਮ ਕਰ ਸਕਦੇ ਹਨ।

## ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ, ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ ਮਲਟੀ-ਮੋਡਲ ਐਪਲੀਕੇਸ਼ਨ ਕਿਵੇਂ ਬਣਾਈ ਜਾਂਦੀ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਮਲਟੀ-ਮੋਡਲ ਚੋਣਾਂ ਨੂੰ ਸਮਝਣ ਲਈ
- ਇੱਕ ਮਲਟੀ-ਮੋਡਲ ਐਪ ਬਣਾਉਣ ਲਈ।

## ਮਲਟੀ-ਮੋਡਲ ਸਹਿਯੋਗ ਲਈ ਆਰਕੀਟੈਕਚਰ

ਮਲਟੀ-ਮੋਡਲ MCP ਇੰਪਲੀਮੈਂਟੇਸ਼ਨਾਂ ਵਿੱਚ ਆਮ ਤੌਰ 'ਤੇ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ:

- **ਮੋਡਲ-ਵਿਸ਼ੇਸ਼ ਪਾਰਸਰ**: ਉਹ ਹਿੱਸੇ ਜੋ ਵੱਖ-ਵੱਖ ਮੀਡੀਆ ਕਿਸਮਾਂ ਨੂੰ ਮਾਡਲ ਲਈ ਸਮਝਣ ਯੋਗ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਦੇ ਹਨ।
- **ਮੋਡਲ-ਵਿਸ਼ੇਸ਼ ਟੂਲ**: ਖਾਸ ਮੋਡਾਲਿਟੀਜ਼ (ਚਿੱਤਰ ਵਿਸ਼ਲੇਸ਼ਣ, ਆਡੀਓ ਪ੍ਰੋਸੈਸਿੰਗ) ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਬਣਾਏ ਗਏ ਟੂਲ।
- **ਇਕਜੁੱਟ ਸੰਦਰਭ ਪ੍ਰਬੰਧਨ**: ਵੱਖ-ਵੱਖ ਮੋਡਾਲਿਟੀਜ਼ ਵਿੱਚ ਸੰਦਰਭ ਨੂੰ ਬਣਾਈ ਰੱਖਣ ਵਾਲਾ ਸਿਸਟਮ।
- **ਜਵਾਬ ਤਿਆਰ ਕਰਨਾ**: ਅਜਿਹੀ ਸਮਰੱਥਾ ਜੋ ਕਈ ਮੋਡਾਲਿਟੀਜ਼ ਵਾਲੇ ਜਵਾਬ ਤਿਆਰ ਕਰ ਸਕੇ।

## ਮਲਟੀ-ਮੋਡਲ ਉਦਾਹਰਨ: ਚਿੱਤਰ ਵਿਸ਼ਲੇਸ਼ਣ

ਹੇਠਾਂ ਦਿੱਤੇ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ ਇੱਕ ਚਿੱਤਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਾਂਗੇ ਅਤੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਾਂਗੇ।

### C# ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ

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

ਉਪਰੋਕਤ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ:

- ਇੱਕ `ImageAnalysisTool` ਬਣਾਇਆ ਹੈ ਜੋ ਇੱਕ ਕਲਪਨਾਤਮਕ `IImageAnalysisService` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰ ਸਕਦਾ ਹੈ।
- MCP ਸਰਵਰ ਨੂੰ ਵੱਡੀਆਂ ਬੇਨਤੀਆਂ ਸੰਭਾਲਣ ਅਤੇ ਚਿੱਤਰ ਸਮੱਗਰੀ ਕਿਸਮਾਂ ਦਾ ਸਹਿਯੋਗ ਦੇਣ ਲਈ ਸੰਰਚਿਤ ਕੀਤਾ।
- ਚਿੱਤਰ ਵਿਸ਼ਲੇਸ਼ਣ ਟੂਲ ਨੂੰ ਸਰਵਰ ਨਾਲ ਰਜਿਸਟਰ ਕੀਤਾ।
- ਇੱਕ ਵਿਧੀ ਲਾਗੂ ਕੀਤੀ ਜੋ URL ਤੋਂ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰਦੀ ਹੈ ਅਤੇ ਮੰਗੀ ਗਈ ਕਿਸਮ (ਵਸਤੂਆਂ, ਟੈਕਸਟ, ਚਿਹਰੇ ਆਦਿ) ਦੇ ਅਧਾਰ 'ਤੇ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦੀ ਹੈ।
- MCP ਵਿਸ਼ੇਸ਼ਤਾ ਦੇ ਅਨੁਕੂਲ ਸਟਰੱਕਚਰਡ ਨਤੀਜੇ ਵਾਪਸ ਕੀਤੇ।

## ਮਲਟੀ-ਮੋਡਲ ਉਦਾਹਰਨ: ਆਡੀਓ ਪ੍ਰੋਸੈਸਿੰਗ

ਆਡੀਓ ਪ੍ਰੋਸੈਸਿੰਗ ਮਲਟੀ-ਮੋਡਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਇੱਕ ਹੋਰ ਆਮ ਮੋਡਾਲਿਟੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤਾ ਉਦਾਹਰਨ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਕਿਵੇਂ ਇੱਕ ਆਡੀਓ ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਟੂਲ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ ਜੋ ਆਡੀਓ ਫਾਈਲਾਂ ਨੂੰ ਸੰਭਾਲ ਸਕਦਾ ਹੈ ਅਤੇ ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਵਾਪਸ ਕਰ ਸਕਦਾ ਹੈ।

### ਜਾਵਾ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ

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

ਉਪਰੋਕਤ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ:

- ਇੱਕ `AudioTranscriptionTool` ਬਣਾਇਆ ਹੈ ਜੋ ਆਡੀਓ ਫਾਈਲਾਂ ਦੀ ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਕਰ ਸਕਦਾ ਹੈ।
- ਟੂਲ ਦਾ ਸਕੀਮਾ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ ਹੈ ਜੋ URL ਜਾਂ base64-ਕੋਡਿਡ ਆਡੀਓ ਡੇਟਾ ਦੋਹਾਂ ਨੂੰ ਸਵੀਕਾਰ ਕਰਦਾ ਹੈ।
- `execute` ਵਿਧੀ ਲਾਗੂ ਕੀਤੀ ਜੋ ਆਡੀਓ ਪ੍ਰੋਸੈਸਿੰਗ ਅਤੇ ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਨੂੰ ਸੰਭਾਲਦੀ ਹੈ।
- MCP ਸਰਵਰ ਨੂੰ ਮਲਟੀ-ਮੋਡਲ ਬੇਨਤੀਆਂ, ਜਿਸ ਵਿੱਚ ਆਡੀਓ ਅਤੇ ਚਿੱਤਰ ਪ੍ਰੋਸੈਸਿੰਗ ਸ਼ਾਮਲ ਹੈ, ਸੰਭਾਲਣ ਲਈ ਸੰਰਚਿਤ ਕੀਤਾ।
- ਆਡੀਓ ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਟੂਲ ਨੂੰ ਸਰਵਰ ਨਾਲ ਰਜਿਸਟਰ ਕੀਤਾ।
- ਇੱਕ ਵਿਧੀ ਲਾਗੂ ਕੀਤੀ ਜੋ URL ਤੋਂ ਆਡੀਓ ਫਾਈਲਾਂ ਡਾਊਨਲੋਡ ਕਰਦੀ ਹੈ ਜਾਂ base64 ਆਡੀਓ ਡੇਟਾ ਡੀਕੋਡ ਕਰਦੀ ਹੈ।
- ਅਸਲ ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਲਾਜਿਕ ਨੂੰ ਸੰਭਾਲਣ ਲਈ `AudioProcessor` ਸੇਵਾ ਦੀ ਵਰਤੋਂ ਕੀਤੀ।
- MCP ਸਰਵਰ ਨੂੰ ਬੇਨਤੀਆਂ ਸੁਣਨ ਲਈ ਸ਼ੁਰੂ ਕੀਤਾ।

### ਮਲਟੀ-ਮੋਡਲ ਉਦਾਹਰਨ: ਮਲਟੀ-ਮੋਡਲ ਜਵਾਬ ਤਿਆਰ ਕਰਨਾ

### ਪਾਇਥਨ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ

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

## ਅਗਲਾ ਕੀ ਹੈ

- [5.3 Oauth 2](../mcp-oauth2-demo/README.md)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।