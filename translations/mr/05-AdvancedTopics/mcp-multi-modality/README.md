# मल्टी-मोडल इंटिग्रेशन

मल्टी-मोडल अॅप्लिकेशन्स AI मध्ये दिवसेंदिवस महत्त्वाचे होत आहेत, जे अधिक समृद्ध संवाद आणि जटिल कार्ये शक्य करतात. Model Context Protocol (MCP) एक असा फ्रेमवर्क प्रदान करतो जो विविध प्रकारच्या डेटासह, जसे की मजकूर, प्रतिमा आणि ऑडिओ, हाताळू शकणाऱ्या मल्टी-मोडल अॅप्लिकेशन्स तयार करण्यास मदत करतो.

MCP फक्त मजकूर-आधारित संवादांपुरता मर्यादित नाही तर मल्टी-मोडल क्षमता देखील पुरवतो, ज्यामुळे मॉडेल प्रतिमा, ऑडिओ आणि इतर डेटा प्रकारांसह काम करू शकतात.

## परिचय

या धड्यात, तुम्ही मल्टी-मोडल अॅप्लिकेशन कसे तयार करायचे ते शिकाल.

## शिकण्याचे उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही सक्षम असाल:

- मल्टी-मोडल पर्याय समजून घेणे
- मल्टी-मोडल अॅप तयार करणे

## मल्टी-मोडल समर्थनासाठी आर्किटेक्चर

मल्टी-मोडल MCP अंमलबजावण्या सहसा यांचा समावेश करतात:

- **मोडल-विशिष्ट पार्सर्स**: असे घटक जे वेगवेगळ्या माध्यम प्रकारांना मॉडेल प्रक्रियेसाठी योग्य स्वरूपात रूपांतरित करतात.
- **मोडल-विशिष्ट साधने**: विशिष्ट माध्यमांसाठी डिझाइन केलेली साधने (प्रतिमा विश्लेषण, ऑडिओ प्रक्रिया)
- **एकत्रित संदर्भ व्यवस्थापन**: वेगवेगळ्या माध्यमांमध्ये संदर्भ राखण्यासाठी प्रणाली
- **प्रतिक्रिया निर्मिती**: अशी क्षमता जी अनेक माध्यमांचा समावेश असलेल्या प्रतिसादांची निर्मिती करू शकते.

## मल्टी-मोडल उदाहरण: प्रतिमा विश्लेषण

खालील उदाहरणात, आपण एका प्रतिमेचे विश्लेषण करून माहिती काढणार आहोत.

### C# अंमलबजावणी

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

वरील उदाहरणात, आपण:

- `ImageAnalysisTool` तयार केले आहे जे काल्पनिक `IImageAnalysisService` वापरून प्रतिमा विश्लेषित करू शकते.
- MCP सर्व्हरला मोठ्या विनंत्या हाताळण्यासाठी आणि प्रतिमा सामग्री प्रकारांना समर्थन देण्यासाठी कॉन्फिगर केले आहे.
- प्रतिमा विश्लेषण साधन सर्व्हरमध्ये नोंदवले आहे.
- URL वरून प्रतिमा डाउनलोड करण्यासाठी आणि विनंती केलेल्या प्रकारानुसार (ऑब्जेक्ट्स, मजकूर, चेहरे इ.) त्यांचे विश्लेषण करण्यासाठी पद्धत अंमलात आणली आहे.
- MCP स्पेसिफिकेशनशी सुसंगत स्वरूपात संरचित निकाल परत केले आहेत.

## मल्टी-मोडल उदाहरण: ऑडिओ प्रक्रिया

ऑडिओ प्रक्रिया ही मल्टी-मोडल अॅप्लिकेशन्समधील आणखी एक सामान्य माध्यम आहे. खाली ऑडिओ फाइल्स हाताळणारे आणि ट्रान्सक्रिप्शन परत करणारे ऑडिओ ट्रान्सक्रिप्शन टूल कसे तयार करायचे याचे उदाहरण दिले आहे.

### Java अंमलबजावणी

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

वरील उदाहरणात, आपण:

- `AudioTranscriptionTool` तयार केले आहे जे ऑडिओ फाइल्सचे ट्रान्सक्रिप्शन करू शकते.
- टूलच्या स्कीमामध्ये URL किंवा बेस64-एन्कोडेड ऑडिओ डेटा स्वीकारण्याची व्याख्या केली आहे.
- `execute` पद्धत अंमलात आणली आहे जी ऑडिओ प्रक्रिया आणि ट्रान्सक्रिप्शन हाताळते.
- MCP सर्व्हरला मल्टी-मोडल विनंत्या, ज्यात ऑडिओ आणि प्रतिमा प्रक्रिया यांचा समावेश आहे, हाताळण्यासाठी कॉन्फिगर केले आहे.
- ऑडिओ ट्रान्सक्रिप्शन टूल सर्व्हरमध्ये नोंदवले आहे.
- URL वरून ऑडिओ फाइल्स डाउनलोड करण्यासाठी किंवा बेस64 ऑडिओ डेटा डीकोड करण्यासाठी पद्धत अंमलात आणली आहे.
- प्रत्यक्ष ट्रान्सक्रिप्शन लॉजिकसाठी `AudioProcessor` सेवा वापरली आहे.
- विनंत्यांसाठी ऐकण्यासाठी MCP सर्व्हर सुरू केला आहे.

### मल्टी-मोडल उदाहरण: मल्टी-मोडल प्रतिक्रिया निर्मिती

### Python अंमलबजावणी

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

## पुढे काय

- [5.3 Oauth 2](../mcp-oauth2-demo/README.md)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.