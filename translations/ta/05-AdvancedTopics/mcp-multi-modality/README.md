# பல்வேறு முறை ஒருங்கிணைப்பு

பல்வேறு முறை பயன்பாடுகள் AI-யில் முக்கியத்துவம் பெறுகின்றன, மேலும் செறிவான தொடர்புகள் மற்றும் சிக்கலான பணிகளை செயல்படுத்த உதவுகின்றன. மாடல் சூழல் நெறிமுறை (MCP) பல்வேறு தரவுகளை (உதாரணமாக, உரை, படங்கள், ஒலி) கையாளக்கூடிய பல்வேறு முறை பயன்பாடுகளை உருவாக்க ஒரு கட்டமைப்பை வழங்குகிறது.

MCP உரை அடிப்படையிலான தொடர்புகளை மட்டுமல்லாமல், படங்கள், ஒலி மற்றும் பிற தரவுகளுடன் வேலை செய்ய பல்வேறு முறை திறன்களையும் ஆதரிக்கிறது.

## அறிமுகம்

இந்த பாடத்தில், பல்வேறு முறை பயன்பாட்டை உருவாக்குவது எப்படி என்பதை நீங்கள் கற்றுக்கொள்வீர்கள்.

## கற்றல் நோக்கங்கள்

இந்த பாடத்தின் முடிவில், நீங்கள்:

- பல்வேறு முறை தேர்வுகளை புரிந்துகொள்வீர்கள்
- ஒரு பல்வேறு முறை பயன்பாட்டை செயல்படுத்துவீர்கள்.

## பல்வேறு முறை ஆதரவு கட்டமைப்பு

பல்வேறு முறை MCP செயல்பாடுகள் பொதுவாக அடங்கும்:

- **முறை-குறிப்பிட்ட பார்சர்கள்**: மாடல் செயல்படுத்தக்கூடிய வடிவங்களாக பல்வேறு ஊடக வகைகளை மாற்றும் கூறுகள்.
- **முறை-குறிப்பிட்ட கருவிகள்**: குறிப்பிட்ட முறைகளைக் கையாள வடிவமைக்கப்பட்ட சிறப்பு கருவிகள் (பட பகுப்பாய்வு, ஒலி செயலாக்கம்).
- **ஒற்றுமையான சூழல் மேலாண்மை**: பல்வேறு முறைகளில் சூழலை பராமரிக்க அமைப்பு.
- **பதில் உருவாக்கம்**: பல்வேறு முறைகளை உள்ளடக்கிய பதில்களை உருவாக்கும் திறன்.

## பல்வேறு முறை உதாரணம்: பட பகுப்பாய்வு

கீழே உள்ள உதாரணத்தில், ஒரு படத்தை பகுப்பாய்வு செய்து தகவலை எடுப்போம்.

### C# செயல்பாடு

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

மேலே உள்ள உதாரணத்தில், நாம்:

- `ImageAnalysisTool` உருவாக்கி, ஒரு கற்பனை `IImageAnalysisService` பயன்படுத்தி படங்களை பகுப்பாய்வு செய்துள்ளோம்.
- MCP சர்வரை பெரிய கோரிக்கைகளை கையாளவும், பட உள்ளடக்க வகைகளை ஆதரிக்கவும் அமைத்துள்ளோம்.
- சர்வருடன் பட பகுப்பாய்வு கருவியை பதிவு செய்துள்ளோம்.
- URL-இல் இருந்து படங்களை பதிவிறக்கம் செய்து, கோரிய வகை (பொருட்கள், உரை, முகங்கள், போன்றவை) அடிப்படையில் அவற்றை பகுப்பாய்வு செய்யும் முறைமையை செயல்படுத்தியுள்ளோம்.
- MCP விவரக்குறிப்புடன் இணக்கமான வடிவத்தில் அமைக்கப்பட்ட முடிவுகளை திருப்பியுள்ளோம்.

## பல்வேறு முறை உதாரணம்: ஒலி செயலாக்கம்

ஒலி செயலாக்கம் பல்வேறு முறை பயன்பாடுகளில் மற்றொரு பொதுவான முறை. கீழே ஒலி கோப்புகளை கையாளவும், உரை மாற்றங்களை திருப்பவும் உதவும் ஒரு ஒலி உரை மாற்ற கருவியை செயல்படுத்துவது எப்படி என்பதைப் பார்க்கலாம்.

### Java செயல்பாடு

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

மேலே உள்ள உதாரணத்தில், நாம்:

- `AudioTranscriptionTool` உருவாக்கி, ஒலி கோப்புகளை உரை மாற்றம் செய்யும் திறனை கொண்டுள்ளோம்.
- கருவியின் திட்டத்தை URL அல்லது base64-கோடிட்ட ஒலி தரவுகளை ஏற்கும் வகையில் வரையறுத்துள்ளோம்.
- ஒலி செயலாக்கம் மற்றும் உரை மாற்றத்தை கையாள `execute` முறைமையை செயல்படுத்தியுள்ளோம்.
- MCP சர்வரை பல்வேறு முறை கோரிக்கைகளை (ஒலி மற்றும் பட செயலாக்கம்) கையாள அமைத்துள்ளோம்.
- சர்வருடன் ஒலி உரை மாற்ற கருவியை பதிவு செய்துள்ளோம்.
- URL-இல் இருந்து ஒலி கோப்புகளை பதிவிறக்கம் செய்ய அல்லது base64 ஒலி தரவுகளை டிகோட் செய்ய முறைமையை செயல்படுத்தியுள்ளோம்.
- `AudioProcessor` சேவையை உண்மையான உரை மாற்ற தற்காலிகத்தை கையாள பயன்படுத்தியுள்ளோம்.
- MCP சர்வரை கோரிக்கைகளை கேட்க தொடங்கியுள்ளோம்.

### பல்வேறு முறை உதாரணம்: பல்வேறு முறை பதில் உருவாக்கம்

### Python செயல்பாடு

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

## அடுத்தது என்ன?

- [5.3 Oauth 2](../mcp-oauth2-demo/README.md)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் தரத்தை உறுதிப்படுத்த முயற்சி செய்தாலும், தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.