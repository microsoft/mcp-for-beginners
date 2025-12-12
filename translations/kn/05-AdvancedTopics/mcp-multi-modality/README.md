<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e1d142978227a4bfc468bb0accab62e2",
  "translation_date": "2025-12-11T15:27:28+00:00",
  "source_file": "05-AdvancedTopics/mcp-multi-modality/README.md",
  "language_code": "kn"
}
-->
# ಬಹು-ಮೋಡಲ್ ಏಕೀಕರಣ

ಬಹು-ಮೋಡಲ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು AI ಯಲ್ಲಿ ಹೆಚ್ಚುತ್ತಿರುವ ಮಹತ್ವವನ್ನು ಹೊಂದಿವೆ, ಸಮೃದ್ಧ ಸಂವಹನಗಳು ಮತ್ತು ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಕಾರ್ಯಗಳನ್ನು ಸಾಧ್ಯಮಾಡುತ್ತವೆ. ಮಾದರಿ ಸಾಂದರ್ಭಿಕ ಪ್ರೋಟೋಕಾಲ್ (MCP) ವಿವಿಧ ರೀತಿಯ ಡೇಟಾ, ಉದಾಹರಣೆಗೆ ಪಠ್ಯ, ಚಿತ್ರಗಳು ಮತ್ತು ಧ್ವನಿಯನ್ನು ನಿರ್ವಹಿಸಲು ಬಹು-ಮೋಡಲ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಒಂದು ಚಟುವಟಿಕೆ ನೀಡುತ್ತದೆ.

MCP ಕೇವಲ ಪಠ್ಯ ಆಧಾರಿತ ಸಂವಹನಗಳನ್ನು ಮಾತ್ರ ಅಲ್ಲದೆ, ಚಿತ್ರಗಳು, ಧ್ವನಿ ಮತ್ತು ಇತರ ಡೇಟಾ ಪ್ರಕಾರಗಳೊಂದಿಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸಲು ಬಹು-ಮೋಡಲ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಸಹ ಬೆಂಬಲಿಸುತ್ತದೆ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ, ನೀವು ಬಹು-ಮೋಡಲ್ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಹೇಗೆ ನಿರ್ಮಿಸುವುದೆಂದು ಕಲಿಯುತ್ತೀರಿ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪಾಠದ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಸಾಧ್ಯವಾಗುವುದು:

- ಬಹು-ಮೋಡಲ್ ಆಯ್ಕೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು
- ಬಹು-ಮೋಡಲ್ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು.

## ಬಹು-ಮೋಡಲ್ ಬೆಂಬಲಕ್ಕಾಗಿ ವಾಸ್ತುಶಿಲ್ಪ

ಬಹು-ಮೋಡಲ್ MCP ಅನುಷ್ಠಾನಗಳು ಸಾಮಾನ್ಯವಾಗಿ ಒಳಗೊಂಡಿರುತ್ತವೆ:

- **ಮೋಡಲ್-ನಿರ್ದಿಷ್ಟ ಪಾರ್ಸರ್‌ಗಳು**: ಮಾದರಿ ಪ್ರಕ್ರಿಯೆ ಮಾಡಬಹುದಾದ ಸ್ವರೂಪಗಳಿಗೆ ವಿಭಿನ್ನ ಮಾಧ್ಯಮ ಪ್ರಕಾರಗಳನ್ನು ಪರಿವರ್ತಿಸುವ ಘಟಕಗಳು.
- **ಮೋಡಲ್-ನಿರ್ದಿಷ್ಟ ಸಾಧನಗಳು**: ನಿರ್ದಿಷ್ಟ ಮೋಡಾಲಿಟಿಗಳನ್ನು (ಚಿತ್ರ ವಿಶ್ಲೇಷಣೆ, ಧ್ವನಿ ಪ್ರಕ್ರಿಯೆ) ನಿರ್ವಹಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಿದ ವಿಶೇಷ ಸಾಧನಗಳು.
- **ಒಕ್ಕೂಟ ಸಾಂದರ್ಭಿಕ ನಿರ್ವಹಣೆ**: ವಿಭಿನ್ನ ಮೋಡಾಲಿಟಿಗಳ ನಡುವೆ ಸಾಂದರ್ಭಿಕತೆಯನ್ನು ಕಾಪಾಡುವ ವ್ಯವಸ್ಥೆ.
- **ಪ್ರತಿಕ್ರಿಯೆ ಉತ್ಪಾದನೆ**: ಬಹು ಮೋಡಾಲಿಟಿಗಳನ್ನು ಒಳಗೊಂಡಿರಬಹುದಾದ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ಉತ್ಪಾದಿಸುವ ಸಾಮರ್ಥ್ಯ.

## ಬಹು-ಮೋಡಲ್ ಉದಾಹರಣೆ: ಚಿತ್ರ ವಿಶ್ಲೇಷಣೆ

ಕೆಳಗಿನ ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು ಒಂದು ಚಿತ್ರವನ್ನು ವಿಶ್ಲೇಷಿಸಿ ಮಾಹಿತಿಯನ್ನು ಹೊರತೆಗೆಯುತ್ತೇವೆ.

### C# ಅನುಷ್ಠಾನ

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

ಮುಂಬರುವ ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು:

- ಕಲ್ಪಿತ `IImageAnalysisService` ಬಳಸಿ ಚಿತ್ರಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಲು ಸಾಧ್ಯವಿರುವ `ImageAnalysisTool` ಅನ್ನು ರಚಿಸಿದ್ದೇವೆ.
- MCP ಸರ್ವರ್ ಅನ್ನು ದೊಡ್ಡ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಮತ್ತು ಚಿತ್ರ ವಿಷಯ ಪ್ರಕಾರಗಳನ್ನು ಬೆಂಬಲಿಸಲು ಸಂರಚಿಸಿದ್ದೇವೆ.
- ಚಿತ್ರ ವಿಶ್ಲೇಷಣಾ ಸಾಧನವನ್ನು ಸರ್ವರ್‌ಗೆ ನೋಂದಾಯಿಸಿದ್ದೇವೆ.
- URL ನಿಂದ ಚಿತ್ರಗಳನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ವಿನಂತಿಸಿದ ಪ್ರಕಾರ (ವಸ್ತುಗಳು, ಪಠ್ಯ, ಮುಖಗಳು ಇತ್ಯಾದಿ) ಆಧರಿಸಿ ಅವುಗಳನ್ನು ವಿಶ್ಲೇಷಿಸುವ ವಿಧಾನವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿದ್ದೇವೆ.
- MCP ನಿರ್ದಿಷ್ಟತೆಯ ಅನುಕೂಲವಾಗಿರುವ ಸ್ವರೂಪದಲ್ಲಿ ರಚನಾತ್ಮಕ ಫಲಿತಾಂಶಗಳನ್ನು ಹಿಂತಿರುಗಿಸಿದ್ದೇವೆ.

## ಬಹು-ಮೋಡಲ್ ಉದಾಹರಣೆ: ಧ್ವನಿ ಪ್ರಕ್ರಿಯೆ

ಧ್ವನಿ ಪ್ರಕ್ರಿಯೆ ಬಹು-ಮೋಡಲ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ ಮತ್ತೊಂದು ಸಾಮಾನ್ಯ ಮೋಡಾಲಿಟಿ. ಕೆಳಗಿನ ಉದಾಹರಣೆಯಲ್ಲಿ, ಧ್ವನಿ ಫೈಲ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸಿ ಲಿಪ್ಯಂತರಣಗಳನ್ನು ಹಿಂತಿರುಗಿಸುವ ಧ್ವನಿ ಲಿಪ್ಯಂತರಣ ಸಾಧನವನ್ನು ಹೇಗೆ ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು ಎಂಬುದನ್ನು ತೋರಿಸಲಾಗಿದೆ.

### ಜಾವಾ ಅನುಷ್ಠಾನ

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

// ಧ್ವನಿ ಲಿಪ್ಯಂತರಣ ಸಾಧನ
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
                
            // URL ಅಥವಾ ನೇರ ಡೇಟಾದಿಂದ ಧ್ವನಿಯನ್ನು ಪಡೆಯಿರಿ
            if (request.getParameters().has("audioUrl")) {
                String audioUrl = request.getParameters().get("audioUrl").asText();
                audioData = downloadAudio(audioUrl);
            } else if (request.getParameters().has("audioData")) {
                String base64Audio = request.getParameters().get("audioData").asText();
                audioData = Base64.getDecoder().decode(base64Audio);
            } else {
                throw new ToolExecutionException("Either audioUrl or audioData must be provided");
            }
            
            // ಧ್ವನಿಯನ್ನು ಪ್ರಕ್ರಿಯೆ ಮಾಡಿ ಮತ್ತು ಲಿಪ್ಯಂತರಣ ಮಾಡಿ
            Map<String, Object> transcriptionResult = audioProcessor.transcribe(audioData, language);
            
            // ಲಿಪ್ಯಂತರಣ ಫಲಿತಾಂಶವನ್ನು ಹಿಂತಿರುಗಿಸಿ
            return new ToolResponse.Builder()
                .setResult(transcriptionResult)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Audio transcription failed: " + ex.getMessage(), ex);
        }
    }
    
    private byte[] downloadAudio(String url) {
        // URL ನಿಂದ ಧ್ವನಿಯನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡುವ ಅನುಷ್ಠಾನ
        // ...
        return new byte[0]; // ಸ್ಥಳಾಪಕ
    }
}

// ಧ್ವನಿ ಮತ್ತು ಇತರ ಮಾದರಿಗಳೊಂದಿಗೆ ಮುಖ್ಯ ಅಪ್ಲಿಕೇಶನ್
public class MultiModalApplication {
    public static void main(String[] args) {
        // ಸೇವೆಗಳನ್ನು ಸಂರಚಿಸಿ
        AudioProcessor audioProcessor = new AudioProcessor();
        ImageProcessor imageProcessor = new ImageProcessor();
        
        // ಸರ್ವರ್ ರಚಿಸಿ ಮತ್ತು ಸಂರಚಿಸಿ
        McpServer server = new McpServer.Builder()
            .setName("Multi-Modal MCP Server")
            .setVersion("1.0.0")
            .setPort(5000)
            .setMaxRequestSize(20 * 1024 * 1024) // ಧ್ವನಿ/ವೀಡಿಯೊ ವಿಷಯಕ್ಕಾಗಿ 20MB
            .build();
            
        // ಬಹು-ಮಾದರಿ ಸಾಧನಗಳನ್ನು ನೋಂದಣಿ ಮಾಡಿ
        server.registerTool(new AudioTranscriptionTool(audioProcessor));
        server.registerTool(new ImageAnalysisTool(imageProcessor));
        server.registerTool(new VideoProcessingTool());
        
        // ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸಿ
        server.start();
        System.out.println("Multi-Modal MCP Server started on port 5000");
    }
}
```

ಮುಂಬರುವ ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು:

- ಧ್ವನಿ ಫೈಲ್‌ಗಳನ್ನು ಲಿಪ್ಯಂತರಣ ಮಾಡಲು ಸಾಧ್ಯವಿರುವ `AudioTranscriptionTool` ಅನ್ನು ರಚಿಸಿದ್ದೇವೆ.
- ಸಾಧನದ ಸ್ಕೀಮಾವನ್ನು URL ಅಥವಾ ಬೇಸ್64-ಕೋಡ್ ಮಾಡಿದ ಧ್ವನಿ ಡೇಟಾವನ್ನು ಸ್ವೀಕರಿಸಲು ನಿರ್ಧರಿಸಿದ್ದೇವೆ.
- ಧ್ವನಿ ಪ್ರಕ್ರಿಯೆ ಮತ್ತು ಲಿಪ್ಯಂತರಣವನ್ನು ನಿರ್ವಹಿಸಲು `execute` ವಿಧಾನವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿದ್ದೇವೆ.
- ಧ್ವನಿ ಮತ್ತು ಚಿತ್ರ ಪ್ರಕ್ರಿಯೆ ಸೇರಿದಂತೆ ಬಹು-ಮೋಡಲ್ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸಲು MCP ಸರ್ವರ್ ಅನ್ನು ಸಂರಚಿಸಿದ್ದೇವೆ.
- ಧ್ವನಿ ಲಿಪ್ಯಂತರಣ ಸಾಧನವನ್ನು ಸರ್ವರ್‌ಗೆ ನೋಂದಾಯಿಸಿದ್ದೇವೆ.
- URL ನಿಂದ ಧ್ವನಿ ಫೈಲ್‌ಗಳನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡುವುದು ಅಥವಾ ಬೇಸ್64 ಧ್ವನಿ ಡೇಟಾವನ್ನು ಡಿಕೋಡ್ ಮಾಡುವ ವಿಧಾನವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿದ್ದೇವೆ.
- ನಿಜವಾದ ಲಿಪ್ಯಂತರಣ ತರ್ಕವನ್ನು ನಿರ್ವಹಿಸಲು `AudioProcessor` ಸೇವೆಯನ್ನು ಬಳಸಿದ್ದೇವೆ.
- ವಿನಂತಿಗಳನ್ನು ಕೇಳಲು MCP ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿದ್ದೇವೆ.

### ಬಹು-ಮೋಡಲ್ ಉದಾಹರಣೆ: ಬಹು-ಮೋಡಲ್ ಪ್ರತಿಕ್ರಿಯೆ ಉತ್ಪಾದನೆ

### ಪೈಥಾನ್ ಅನುಷ್ಠಾನ

```python
from mcp_server import McpServer
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
import base64
from PIL import Image
import io
import requests
import json
from typing import Dict, Any, List, Optional

# ಚಿತ್ರ ರಚನೆ ಸಾಧನ
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
            # ಪರಿಮಾಣಗಳನ್ನು ಹೊರತೆಗೆಯಿರಿ
            prompt = request.parameters.get("prompt")
            style = request.parameters.get("style", "realistic")
            width = request.parameters.get("width", 512)
            height = request.parameters.get("height", 512)
            
            # ಬಾಹ್ಯ ಸೇವೆಯನ್ನು ಬಳಸಿ ಚಿತ್ರ ರಚಿಸಿ (ಉದಾಹರಣೆಯ ಅನುಷ್ಠಾನ)
            image_data = await self._generate_image(prompt, style, width, height)
            
            # ಪ್ರತಿಕ್ರಿಯೆಗೆ ಚಿತ್ರವನ್ನು ಬೇಸ್64 ಗೆ ಪರಿವರ್ತಿಸಿ
            buffered = io.BytesIO()
            image_data.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            # ಚಿತ್ರ ಮತ್ತು ಮೆಟಾಡೇಟಾ ಎರಡನ್ನೂ ಹೊಂದಿರುವ ಫಲಿತಾಂಶವನ್ನು ಹಿಂತಿರುಗಿಸಿ
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
        # ಪ್ಲೇಸ್‌ಹೋಲ್ಡರ್ ಚಿತ್ರವನ್ನು ಹಿಂತಿರುಗಿಸಿ ಅಥವಾ ನಿಜವಾದ ಚಿತ್ರ ರಚನೆ API ಅನ್ನು ಕರೆಮಾಡಿ
        # ಈ ಉದಾಹರಣೆಗೆ, ನಾವು ಸರಳ ಬಣ್ಣದ ಚಿತ್ರವನ್ನು ರಚಿಸುವೆವು
        image = Image.new('RGB', (width, height), color=(73, 109, 137))
        return image

# ಬಹು-ಮೋಡ್ ಪ್ರತಿಕ್ರಿಯೆ ನಿರ್ವಹಣೆ
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
        
        # ವಿನಂತಿಸಿದರೆ ಚಿತ್ರಗಳನ್ನು ರಚಿಸಿ
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

# ಮುಖ್ಯ ಅಪ್ಲಿಕೇಶನ್
async def main():
    # ಸರ್ವರ್ ರಚಿಸಿ
    server = McpServer(
        name="Multi-Modal MCP Server",
        version="1.0.0",
        port=5000
    )
    
    # ಬಹು-ಮೋಡ್ ಸಾಧನಗಳನ್ನು ನೋಂದಣಿ ಮಾಡಿ
    server.register_tool(ImageGenerationTool())
    server.register_tool(AudioAnalysisTool())
    server.register_tool(VideoFrameExtractionTool())
    
    # ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸಿ
    await server.start()
    print("Multi-Modal MCP Server running on port 5000")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## ಮುಂದೇನು

- [5.3 Oauth 2](../mcp-oauth2-demo/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->