# मल्टी-मोडल इंटीग्रेशन

मल्टी-मोडल एप्लिकेशन AI में तेजी से महत्वपूर्ण होते जा रहे हैं, जो अधिक समृद्ध इंटरैक्शन और जटिल कार्यों को संभव बनाते हैं। Model Context Protocol (MCP) एक ऐसा फ्रेमवर्क प्रदान करता है जो विभिन्न प्रकार के डेटा जैसे टेक्स्ट, इमेज और ऑडियो को संभालने वाले मल्टी-मोडल एप्लिकेशन बनाने में मदद करता है।

MCP केवल टेक्स्ट-आधारित इंटरैक्शन तक सीमित नहीं है, बल्कि मल्टी-मोडल क्षमताओं का समर्थन करता है, जिससे मॉडल इमेज, ऑडियो और अन्य डेटा प्रकारों के साथ काम कर सकते हैं।

## परिचय

इस पाठ में, आप सीखेंगे कि कैसे एक मल्टी-मोडल एप्लिकेशन बनाया जाता है।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- मल्टी-मोडल विकल्पों को समझने के लिए
- एक मल्टी-मोडल ऐप को लागू करने के लिए।

## मल्टी-मोडल सपोर्ट के लिए आर्किटेक्चर

मल्टी-मोडल MCP इम्प्लीमेंटेशन आमतौर पर शामिल होते हैं:

- **मोडल-विशिष्ट पार्सर**: ऐसे घटक जो विभिन्न मीडिया प्रकारों को मॉडल द्वारा प्रोसेस किए जाने वाले फॉर्मेट में बदलते हैं।
- **मोडल-विशिष्ट टूल्स**: विशेष टूल जो विशिष्ट मोडालिटी (जैसे इमेज एनालिसिस, ऑडियो प्रोसेसिंग) को संभालने के लिए डिज़ाइन किए गए हैं।
- **यूनिफाइड कॉन्टेक्स्ट मैनेजमेंट**: विभिन्न मोडालिटी के बीच संदर्भ बनाए रखने की प्रणाली।
- **रिस्पॉन्स जनरेशन**: ऐसी क्षमता जो कई मोडालिटी को शामिल करने वाले उत्तर उत्पन्न कर सके।

## मल्टी-मोडल उदाहरण: इमेज एनालिसिस

नीचे दिए गए उदाहरण में, हम एक इमेज का विश्लेषण करेंगे और जानकारी निकालेंगे।

### C# इम्प्लीमेंटेशन

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

पिछले उदाहरण में, हमने:

- एक `ImageAnalysisTool` बनाया है जो एक काल्पनिक `IImageAnalysisService` का उपयोग करके इमेज का विश्लेषण कर सकता है।
- MCP सर्वर को बड़े अनुरोधों को संभालने और इमेज कंटेंट टाइप्स का समर्थन करने के लिए कॉन्फ़िगर किया।
- इमेज एनालिसिस टूल को सर्वर के साथ रजिस्टर किया।
- एक मेथड लागू किया जो URL से इमेज डाउनलोड करता है और अनुरोधित प्रकार (ऑब्जेक्ट्स, टेक्स्ट, चेहरे आदि) के आधार पर उनका विश्लेषण करता है।
- MCP स्पेसिफिकेशन के अनुरूप संरचित परिणाम लौटाए।

## मल्टी-मोडल उदाहरण: ऑडियो प्रोसेसिंग

ऑडियो प्रोसेसिंग मल्टी-मोडल एप्लिकेशन में एक और सामान्य मोडालिटी है। नीचे एक उदाहरण है कि कैसे एक ऑडियो ट्रांसक्रिप्शन टूल को लागू किया जाए जो ऑडियो फाइलों को संभाल सके और ट्रांसक्रिप्शन लौटाए।

### Java इम्प्लीमेंटेशन

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

पिछले उदाहरण में, हमने:

- एक `AudioTranscriptionTool` बनाया है जो ऑडियो फाइलों का ट्रांसक्रिप्शन कर सकता है।
- टूल के स्कीमा को परिभाषित किया ताकि वह या तो URL या बेस64-एन्कोडेड ऑडियो डेटा स्वीकार कर सके।
- `execute` मेथड को लागू किया जो ऑडियो प्रोसेसिंग और ट्रांसक्रिप्शन को संभालता है।
- MCP सर्वर को मल्टी-मोडल अनुरोधों को संभालने के लिए कॉन्फ़िगर किया, जिसमें ऑडियो और इमेज प्रोसेसिंग शामिल है।
- ऑडियो ट्रांसक्रिप्शन टूल को सर्वर के साथ रजिस्टर किया।
- एक मेथड लागू किया जो URL से ऑडियो फाइल डाउनलोड करता है या बेस64 ऑडियो डेटा को डिकोड करता है।
- एक `AudioProcessor` सेवा का उपयोग किया जो वास्तविक ट्रांसक्रिप्शन लॉजिक को संभालती है।
- MCP सर्वर को अनुरोधों के लिए सुनने के लिए शुरू किया।

### मल्टी-मोडल उदाहरण: मल्टी-मोडल रिस्पॉन्स जनरेशन

### Python इम्प्लीमेंटेशन

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

## आगे क्या

- [5.3 Oauth 2](../mcp-oauth2-demo/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।