# బహుముఖ ఇంటిగ్రేషన్

బహుముఖ అనువర్తనాలు AIలో మరింత ప్రాముఖ్యత పొందుతున్నాయి, ఇవి సమృద్ధిగా పరస్పర చర్యలు మరియు మరింత సంక్లిష్టమైన పనులను సాధించడానికి సహాయపడతాయి. మోడల్ కాంటెక్స్ట్ ప్రోటోకాల్ (MCP) వివిధ రకాల డేటాను, ఉదాహరణకు టెక్స్ట్, చిత్రాలు, ఆడియో వంటి వాటిని నిర్వహించగల బహుముఖ అనువర్తనాలను నిర్మించడానికి ఒక ఫ్రేమ్‌వర్క్‌ను అందిస్తుంది.

MCP కేవలం టెక్స్ట్ ఆధారిత పరస్పర చర్యలను మాత్రమే కాకుండా బహుముఖ సామర్థ్యాలను కూడా మద్దతు ఇస్తుంది, మోడల్స్ చిత్రాలు, ఆడియో మరియు ఇతర డేటా రకాలతో పని చేయగలవు.

## పరిచయం

ఈ పాఠంలో, మీరు బహుముఖ అనువర్తనం ఎలా నిర్మించాలో నేర్చుకుంటారు.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం ముగిసిన తర్వాత, మీరు చేయగలుగుతారు:

- బహుముఖ ఎంపికలను అర్థం చేసుకోవడం
- బహుముఖ అనువర్తనాన్ని అమలు చేయడం.

## బహుముఖ మద్దతు కోసం ఆర్కిటెక్చర్

బహుముఖ MCP అమలు సాధారణంగా:

- **మోడల్-స్పెసిఫిక్ పార్సర్లు**: వివిధ మీడియా రకాలని మోడల్ ప్రాసెస్ చేయగల ఫార్మాట్లుగా మార్చే భాగాలు.
- **మోడల్-స్పెసిఫిక్ టూల్స్**: నిర్దిష్ట మోడాలిటీలను (చిత్ర విశ్లేషణ, ఆడియో ప్రాసెసింగ్) నిర్వహించడానికి ప్రత్యేకంగా రూపొందించిన టూల్స్.
- **ఐక్య కాంటెక్స్ట్ నిర్వహణ**: వివిధ మోడాలిటీల మధ్య కాంటెక్స్ట్‌ను నిర్వహించే వ్యవస్థ.
- **ప్రతిస్పందన ఉత్పత్తి**: బహుముఖ మోడాలిటీలను కలిగి ఉండగల ప్రతిస్పందనలను సృష్టించే సామర్థ్యం.

## బహుముఖ ఉదాహరణ: చిత్రం విశ్లేషణ

క్రింది ఉదాహరణలో, మనం ఒక చిత్రాన్ని విశ్లేషించి సమాచారం తీసుకుంటాము.

### C# అమలు

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

ముందటి ఉదాహరణలో, మనం:

- ఒక `ImageAnalysisTool` ను సృష్టించాము, ఇది ఒక ఊహాత్మక `IImageAnalysisService` ఉపయోగించి చిత్రాలను విశ్లేషించగలదు.
- MCP సర్వర్‌ను పెద్ద అభ్యర్థనలను మరియు చిత్రం కంటెంట్ రకాల మద్దతు కోసం కాన్ఫిగర్ చేసాము.
- చిత్రం విశ్లేషణ టూల్‌ను సర్వర్‌తో నమోదు చేసాము.
- URL నుండి చిత్రాలను డౌన్లోడ్ చేసి, అభ్యర్థించిన రకం (వస్తువులు, టెక్స్ట్, ముఖాలు మొదలైనవి) ఆధారంగా విశ్లేషించే విధానాన్ని అమలు చేసాము.
- MCP స్పెసిఫికేషన్‌కు అనుగుణంగా నిర్మిత ఫలితాలను తిరిగి ఇచ్చాము.

## బహుముఖ ఉదాహరణ: ఆడియో ప్రాసెసింగ్

ఆడియో ప్రాసెసింగ్ కూడా బహుముఖ అనువర్తనాలలో ఒక సాధారణ మోడాలిటీ. క్రింద ఆడియో ఫైళ్లను నిర్వహించి ట్రాన్స్క్రిప్షన్లను తిరిగి ఇచ్చే ఆడియో ట్రాన్స్క్రిప్షన్ టూల్‌ను ఎలా అమలు చేయాలో ఒక ఉదాహరణ ఉంది.

### Java అమలు

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

// ఆడియో ట్రాన్స్క్రిప్షన్ టూల్
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
                
            // URL లేదా ప్రత్యక్ష డేటా నుండి ఆడియో పొందండి
            if (request.getParameters().has("audioUrl")) {
                String audioUrl = request.getParameters().get("audioUrl").asText();
                audioData = downloadAudio(audioUrl);
            } else if (request.getParameters().has("audioData")) {
                String base64Audio = request.getParameters().get("audioData").asText();
                audioData = Base64.getDecoder().decode(base64Audio);
            } else {
                throw new ToolExecutionException("Either audioUrl or audioData must be provided");
            }
            
            // ఆడియోని ప్రాసెస్ చేసి ట్రాన్స్క్రైబ్ చేయండి
            Map<String, Object> transcriptionResult = audioProcessor.transcribe(audioData, language);
            
            // ట్రాన్స్క్రిప్షన్ ఫలితాన్ని తిరిగి ఇవ్వండి
            return new ToolResponse.Builder()
                .setResult(transcriptionResult)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Audio transcription failed: " + ex.getMessage(), ex);
        }
    }
    
    private byte[] downloadAudio(String url) {
        // URL నుండి ఆడియో డౌన్లోడ్ చేయడానికి అమలు
        // ...
        return new byte[0]; // ప్లేస్‌హోల్డర్
    }
}

// ఆడియో మరియు ఇతర మోడాలిటీలతో ప్రధాన అప్లికేషన్
public class MultiModalApplication {
    public static void main(String[] args) {
        // సేవలను కాన్ఫిగర్ చేయండి
        AudioProcessor audioProcessor = new AudioProcessor();
        ImageProcessor imageProcessor = new ImageProcessor();
        
        // సర్వర్ సృష్టించి కాన్ఫిగర్ చేయండి
        McpServer server = new McpServer.Builder()
            .setName("Multi-Modal MCP Server")
            .setVersion("1.0.0")
            .setPort(5000)
            .setMaxRequestSize(20 * 1024 * 1024) // ఆడియో/వీడియో కంటెంట్ కోసం 20MB
            .build();
            
        // బహుముఖ మోడల్ టూల్స్‌ను నమోదు చేయండి
        server.registerTool(new AudioTranscriptionTool(audioProcessor));
        server.registerTool(new ImageAnalysisTool(imageProcessor));
        server.registerTool(new VideoProcessingTool());
        
        // సర్వర్ ప్రారంభించండి
        server.start();
        System.out.println("Multi-Modal MCP Server started on port 5000");
    }
}
```

ముందటి ఉదాహరణలో, మనం:

- ఆడియో ఫైళ్లను ట్రాన్స్క్రైబ్ చేయగల `AudioTranscriptionTool` ను సృష్టించాము.
- టూల్ స్కీమాను URL లేదా base64-ఎన్‌కోడ్ చేసిన ఆడియో డేటాను స్వీకరించడానికి నిర్వచించాము.
- ఆడియో ప్రాసెసింగ్ మరియు ట్రాన్స్క్రిప్షన్ నిర్వహించడానికి `execute` పద్ధతిని అమలు చేసాము.
- ఆడియో మరియు చిత్రం ప్రాసెసింగ్ సహా బహుముఖ అభ్యర్థనలను నిర్వహించడానికి MCP సర్వర్‌ను కాన్ఫిగర్ చేసాము.
- ఆడియో ట్రాన్స్క్రిప్షన్ టూల్‌ను సర్వర్‌తో నమోదు చేసాము.
- URL నుండి ఆడియో ఫైళ్లను డౌన్లోడ్ చేయడం లేదా base64 ఆడియో డేటాను డీకోడ్ చేయడం కోసం పద్ధతిని అమలు చేసాము.
- వాస్తవ ట్రాన్స్క్రిప్షన్ లాజిక్ నిర్వహించడానికి `AudioProcessor` సేవను ఉపయోగించాము.
- అభ్యర్థనలను వినడానికి MCP సర్వర్‌ను ప్రారంభించాము.

### బహుముఖ ఉదాహరణ: బహుముఖ ప్రతిస్పందన ఉత్పత్తి

### Python అమలు

```python
from mcp_server import McpServer
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
import base64
from PIL import Image
import io
import requests
import json
from typing import Dict, Any, List, Optional

# చిత్రం సృష్టి సాధనం
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
            # పారామితులను తీసుకోండి
            prompt = request.parameters.get("prompt")
            style = request.parameters.get("style", "realistic")
            width = request.parameters.get("width", 512)
            height = request.parameters.get("height", 512)
            
            # బాహ్య సేవ ఉపయోగించి చిత్రం సృష్టించండి (ఉదాహరణ అమలు)
            image_data = await self._generate_image(prompt, style, width, height)
            
            # ప్రతిస్పందన కోసం చిత్రాన్ని base64 గా మార్చండి
            buffered = io.BytesIO()
            image_data.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            # చిత్రం మరియు మెటాడేటాతో ఫలితాన్ని తిరిగి ఇవ్వండి
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
        # ప్లేస్‌హోల్డర్ చిత్రం ఇవ్వండి లేదా వాస్తవ చిత్రం సృష్టి API ని పిలవండి
        # ఈ ఉదాహరణ కోసం, మనం ఒక సాదా రంగు చిత్రం సృష్టిస్తాము
        image = Image.new('RGB', (width, height), color=(73, 109, 137))
        return image

# బహుముఖ ప్రతిస్పందన హ్యాండ్లర్
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
        
        # అభ్యర్థన వచ్చినప్పుడు చిత్రాలు సృష్టించండి
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

# ప్రధాన అనువర్తనం
async def main():
    # సర్వర్ సృష్టించండి
    server = McpServer(
        name="Multi-Modal MCP Server",
        version="1.0.0",
        port=5000
    )
    
    # బహుముఖ సాధనాలను నమోదు చేయండి
    server.register_tool(ImageGenerationTool())
    server.register_tool(AudioAnalysisTool())
    server.register_tool(VideoFrameExtractionTool())
    
    # సర్వర్ ప్రారంభించండి
    await server.start()
    print("Multi-Modal MCP Server running on port 5000")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## తదుపరి ఏమిటి

- [5.3 Oauth 2](../mcp-oauth2-demo/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->