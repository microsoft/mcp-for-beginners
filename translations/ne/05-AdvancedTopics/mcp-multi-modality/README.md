# बहु-मोडल एकीकरण

बहु-मोडल अनुप्रयोगहरू AI मा दिनप्रतिदिन महत्त्वपूर्ण हुँदैछन्, जसले समृद्ध अन्तरक्रियाहरू र जटिल कार्यहरू सम्भव बनाउँछ। Model Context Protocol (MCP) ले विभिन्न प्रकारका डाटा, जस्तै पाठ, छवि, र अडियो, सम्हाल्न सक्ने बहु-मोडल अनुप्रयोगहरू निर्माण गर्नका लागि एक रूपरेखा प्रदान गर्दछ।

MCP ले केवल पाठ-आधारित अन्तरक्रियाहरू मात्र होइन, बहु-मोडल क्षमताहरू पनि समर्थन गर्दछ, जसले मोडेलहरूलाई छवि, अडियो, र अन्य डाटा प्रकारहरूसँग काम गर्न सक्षम बनाउँछ।

## परिचय

यस पाठमा, तपाईंले बहु-मोडल अनुप्रयोग कसरी बनाउने सिक्नुहुनेछ।

## सिकाइ उद्देश्यहरू

यस पाठको अन्त्यसम्म, तपाईं सक्षम हुनुहुनेछ:

- बहु-मोडल विकल्पहरू बुझ्न
- बहु-मोडल अनुप्रयोग कार्यान्वयन गर्न।

## बहु-मोडल समर्थनको वास्तुकला

बहु-मोडल MCP कार्यान्वयनहरू सामान्यतया समावेश गर्छन्:

- **मोडल-विशिष्ट पार्सरहरू**: विभिन्न मिडिया प्रकारहरूलाई मोडेलले प्रक्रिया गर्न सक्ने ढाँचामा रूपान्तरण गर्ने कम्पोनेन्टहरू।
- **मोडल-विशिष्ट उपकरणहरू**: विशेष मोडलिटीहरू (जस्तै छवि विश्लेषण, अडियो प्रशोधन) सम्हाल्न डिजाइन गरिएका उपकरणहरू।
- **एकीकृत सन्दर्भ व्यवस्थापन**: विभिन्न मोडलिटीहरूमा सन्दर्भ कायम राख्ने प्रणाली।
- **प्रतिक्रिया उत्पादन**: बहु मोडलिटीहरू समावेश गर्न सक्ने प्रतिक्रियाहरू उत्पन्न गर्ने क्षमता।

## बहु-मोडल उदाहरण: छवि विश्लेषण

तलको उदाहरणमा, हामीले एउटा छवि विश्लेषण गर्नेछौं र जानकारी निकाल्नेछौं।

### C# कार्यान्वयन

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

अघिल्लो उदाहरणमा, हामीले:

- `ImageAnalysisTool` सिर्जना गरेका छौं जसले काल्पनिक `IImageAnalysisService` प्रयोग गरेर छविहरू विश्लेषण गर्न सक्छ।
- MCP सर्भरलाई ठूलो अनुरोधहरू र छवि सामग्री प्रकारहरू समर्थन गर्न कन्फिगर गरेका छौं।
- छवि विश्लेषण उपकरणलाई सर्भरसँग दर्ता गरेका छौं।
- URL बाट छविहरू डाउनलोड गर्ने र अनुरोध गरिएको प्रकार (वस्तुहरू, पाठ, अनुहारहरू, आदि) अनुसार विश्लेषण गर्ने विधि कार्यान्वयन गरेका छौं।
- MCP विनिर्देशन अनुरूप संरचित परिणामहरू फर्काएका छौं।

## बहु-मोडल उदाहरण: अडियो प्रशोधन

अडियो प्रशोधन बहु-मोडल अनुप्रयोगहरूमा अर्को सामान्य मोडलिटी हो। तल अडियो फाइलहरू सम्हाल्न र ट्रान्सक्रिप्शन फर्काउन सक्ने अडियो ट्रान्सक्रिप्शन उपकरण कसरी कार्यान्वयन गर्ने उदाहरण छ।

### Java कार्यान्वयन

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

अघिल्लो उदाहरणमा, हामीले:

- `AudioTranscriptionTool` सिर्जना गरेका छौं जसले अडियो फाइलहरू ट्रान्सक्राइब गर्न सक्छ।
- उपकरणको स्कीमा परिभाषित गरेका छौं जसले URL वा base64-एन्कोड गरिएको अडियो डाटा स्वीकार गर्न सक्छ।
- `execute` विधि कार्यान्वयन गरेका छौं जसले अडियो प्रशोधन र ट्रान्सक्रिप्शन सम्हाल्छ।
- MCP सर्भरलाई बहु-मोडल अनुरोधहरू, अडियो र छवि प्रशोधन सहित, समर्थन गर्न कन्फिगर गरेका छौं।
- अडियो ट्रान्सक्रिप्शन उपकरणलाई सर्भरसँग दर्ता गरेका छौं।
- URL बाट अडियो फाइलहरू डाउनलोड गर्ने वा base64 अडियो डाटा डिकोड गर्ने विधि कार्यान्वयन गरेका छौं।
- वास्तविक ट्रान्सक्रिप्शन तर्क सम्हाल्न `AudioProcessor` सेवा प्रयोग गरेका छौं।
- अनुरोधहरू सुन्न MCP सर्भर सुरु गरेका छौं।

### बहु-मोडल उदाहरण: बहु-मोडल प्रतिक्रिया उत्पादन

### Python कार्यान्वयन

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

## अब के गर्ने

- [5.3 Oauth 2](../mcp-oauth2-demo/README.md)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।