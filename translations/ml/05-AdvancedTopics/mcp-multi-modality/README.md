# മൾട്ടി-മോഡൽ ഇന്റഗ്രേഷൻ

മൾട്ടി-മോഡൽ ആപ്ലിക്കേഷനുകൾ AI-യിൽ കൂടുതൽ പ്രധാനപ്പെട്ടതാകുന്നു, സമ്പന്നമായ ഇടപെടലുകൾക്കും കൂടുതൽ സങ്കീർണ്ണമായ ജോലികൾക്കും സഹായിക്കുന്നു. മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോക്കോൾ (MCP) വിവിധ തരത്തിലുള്ള ഡാറ്റകൾ, ഉദാഹരണത്തിന് ടെക്സ്റ്റ്, ചിത്രങ്ങൾ, ഓഡിയോ എന്നിവ കൈകാര്യം ചെയ്യാൻ കഴിയുന്ന മൾട്ടി-മോഡൽ ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കാൻ ഒരു ഫ്രെയിംവർക്ക് നൽകുന്നു.

MCP ടെക്സ്റ്റ് അടിസ്ഥാനമാക്കിയുള്ള ഇടപെടലുകൾ മാത്രമല്ല, ചിത്രങ്ങൾ, ഓഡിയോ, മറ്റ് ഡാറ്റാ തരം എന്നിവയുമായി പ്രവർത്തിക്കാൻ കഴിയുന്ന മൾട്ടി-മോഡൽ കഴിവുകളും പിന്തുണയ്ക്കുന്നു.

## പരിചയം

ഈ പാഠത്തിൽ, നിങ്ങൾ ഒരു മൾട്ടി-മോഡൽ ആപ്ലിക്കേഷൻ എങ്ങനെ നിർമ്മിക്കാമെന്ന് പഠിക്കും.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം അവസാനിക്കുമ്പോൾ, നിങ്ങൾക്ക് കഴിയും:

- മൾട്ടി-മോഡൽ തിരഞ്ഞെടുപ്പുകൾ മനസിലാക്കുക
- ഒരു മൾട്ടി-മോഡൽ ആപ്പ് നടപ്പിലാക്കുക.

## മൾട്ടി-മോഡൽ പിന്തുണയ്ക്കുള്ള ആർക്കിടെക്ചർ

മൾട്ടി-മോഡൽ MCP നടപ്പാക്കലുകൾ സാധാരണയായി ഉൾക്കൊള്ളുന്നു:

- **മോഡൽ-സ്പെസിഫിക് പാർസറുകൾ**: മോഡൽ പ്രോസസ്സ് ചെയ്യാൻ കഴിയുന്ന ഫോർമാറ്റുകളിലേക്ക് വ്യത്യസ്ത മീഡിയ തരം മാറ്റുന്ന ഘടകങ്ങൾ.
- **മോഡൽ-സ്പെസിഫിക് ടൂളുകൾ**: പ്രത്യേക മോഡാലിറ്റികൾ (ചിത്ര വിശകലനം, ഓഡിയോ പ്രോസസ്സിംഗ്) കൈകാര്യം ചെയ്യാൻ രൂപകൽപ്പന ചെയ്ത പ്രത്യേക ടൂളുകൾ.
- **ഏകീകൃത കോൺടെക്സ്റ്റ് മാനേജ്മെന്റ്**: വ്യത്യസ്ത മോഡാലിറ്റികളിലുടനീളം കോൺടെക്സ്റ്റ് നിലനിർത്താനുള്ള സിസ്റ്റം.
- **പ്രതികരണ സൃഷ്ടി**: പല മോഡാലിറ്റികളും ഉൾക്കൊള്ളുന്ന പ്രതികരണങ്ങൾ സൃഷ്ടിക്കാൻ കഴിയുന്ന കഴിവ്.

## മൾട്ടി-മോഡൽ ഉദാഹരണം: ചിത്രം വിശകലനം

താഴെ കൊടുത്ത ഉദാഹരണത്തിൽ, ഒരു ചിത്രം വിശകലനം ചെയ്ത് വിവരങ്ങൾ എടുക്കും.

### C# നടപ്പാക്കൽ

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

മുൻപത്തെ ഉദാഹരണത്തിൽ, ഞങ്ങൾ:

- ഒരു `ImageAnalysisTool` സൃഷ്ടിച്ചു, ഇത് ഒരു സങ്കൽപ്പിത `IImageAnalysisService` ഉപയോഗിച്ച് ചിത്രങ്ങൾ വിശകലനം ചെയ്യാൻ കഴിയും.
- MCP സർവർ വലിയ അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യാനും ചിത്രം ഉള്ളടക്ക തരം പിന്തുണയ്ക്കാനും ക്രമീകരിച്ചു.
- ചിത്രം വിശകലന ടൂൾ സർവറുമായി രജിസ്റ്റർ ചെയ്തു.
- URL-ൽ നിന്നുള്ള ചിത്രങ്ങൾ ഡൗൺലോഡ് ചെയ്ത് അഭ്യർത്ഥിച്ച തരം (വസ്തുക്കൾ, ടെക്സ്റ്റ്, മുഖങ്ങൾ, തുടങ്ങിയവ) അടിസ്ഥാനമാക്കി അവ വിശകലനം ചെയ്യാനുള്ള ഒരു മെത്തഡ് നടപ്പിലാക്കി.
- MCP സ്പെസിഫിക്കേഷനുമായി പൊരുത്തപ്പെടുന്ന ഫോർമാറ്റിൽ ഘടനാപരമായ ഫലങ്ങൾ തിരികെ നൽകി.

## മൾട്ടി-മോഡൽ ഉദാഹരണം: ഓഡിയോ പ്രോസസ്സിംഗ്

ഓഡിയോ പ്രോസസ്സിംഗ് മൾട്ടി-മോഡൽ ആപ്ലിക്കേഷനുകളിൽ മറ്റൊരു സാധാരണ മോഡാലിറ്റി ആണ്. താഴെ ഒരു ഓഡിയോ ട്രാൻസ്ക്രിപ്ഷൻ ടൂൾ എങ്ങനെ നടപ്പിലാക്കാമെന്ന് ഉദാഹരണം കൊടുത്തിരിക്കുന്നു, ഇത് ഓഡിയോ ഫയലുകൾ കൈകാര്യം ചെയ്ത് ട്രാൻസ്ക്രിപ്ഷനുകൾ തിരികെ നൽകും.

### ജാവാ നടപ്പാക്കൽ

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

// ഓഡിയോ ട്രാൻസ്ക്രിപ്ഷൻ ടൂൾ
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
                
            // URL അല്ലെങ്കിൽ നേരിട്ട് ഡാറ്റയിൽ നിന്ന് ഓഡിയോ നേടുക
            if (request.getParameters().has("audioUrl")) {
                String audioUrl = request.getParameters().get("audioUrl").asText();
                audioData = downloadAudio(audioUrl);
            } else if (request.getParameters().has("audioData")) {
                String base64Audio = request.getParameters().get("audioData").asText();
                audioData = Base64.getDecoder().decode(base64Audio);
            } else {
                throw new ToolExecutionException("Either audioUrl or audioData must be provided");
            }
            
            // ഓഡിയോ പ്രോസസ്സ് ചെയ്ത് ട്രാൻസ്ക്രൈബ് ചെയ്യുക
            Map<String, Object> transcriptionResult = audioProcessor.transcribe(audioData, language);
            
            // ട്രാൻസ്ക്രിപ്ഷൻ ഫലം തിരികെ നൽകുക
            return new ToolResponse.Builder()
                .setResult(transcriptionResult)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Audio transcription failed: " + ex.getMessage(), ex);
        }
    }
    
    private byte[] downloadAudio(String url) {
        // URL-ൽ നിന്ന് ഓഡിയോ ഡൗൺലോഡ് ചെയ്യാനുള്ള നടപ്പാക്കൽ
        // ...
        return new byte[0]; // പ്ലേസ്‌ഹോൾഡർ
    }
}

// ഓഡിയോയും മറ്റ് മോഡാലിറ്റികളും ഉള്ള പ്രധാന അപ്ലിക്കേഷൻ
public class MultiModalApplication {
    public static void main(String[] args) {
        // സേവനങ്ങൾ ക്രമീകരിക്കുക
        AudioProcessor audioProcessor = new AudioProcessor();
        ImageProcessor imageProcessor = new ImageProcessor();
        
        // സെർവർ സൃഷ്ടിച്ച് ക്രമീകരിക്കുക
        McpServer server = new McpServer.Builder()
            .setName("Multi-Modal MCP Server")
            .setVersion("1.0.0")
            .setPort(5000)
            .setMaxRequestSize(20 * 1024 * 1024) // ഓഡിയോ/വീഡിയോ ഉള്ളടക്കത്തിന് 20MB
            .build();
            
        // മൾട്ടി-മോഡൽ ടൂളുകൾ രജിസ്റ്റർ ചെയ്യുക
        server.registerTool(new AudioTranscriptionTool(audioProcessor));
        server.registerTool(new ImageAnalysisTool(imageProcessor));
        server.registerTool(new VideoProcessingTool());
        
        // സെർവർ ആരംഭിക്കുക
        server.start();
        System.out.println("Multi-Modal MCP Server started on port 5000");
    }
}
```

മുൻപത്തെ ഉദാഹരണത്തിൽ, ഞങ്ങൾ:

- ഓഡിയോ ഫയലുകൾ ട്രാൻസ്ക്രൈബ് ചെയ്യാൻ കഴിയുന്ന `AudioTranscriptionTool` സൃഷ്ടിച്ചു.
- ടൂളിന്റെ സ്കീമ നിർവചിച്ചു, ഇത് URL അല്ലെങ്കിൽ ബേസ്64 എൻകോഡുചെയ്ത ഓഡിയോ ഡാറ്റ സ്വീകരിക്കും.
- ഓഡിയോ പ്രോസസ്സിംഗ്, ട്രാൻസ്ക്രിപ്ഷൻ കൈകാര്യം ചെയ്യാൻ `execute` മെത്തഡ് നടപ്പിലാക്കി.
- ഓഡിയോ, ചിത്രം പ്രോസസ്സിംഗ് ഉൾപ്പെടെയുള്ള മൾട്ടി-മോഡൽ അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യാൻ MCP സർവർ ക്രമീകരിച്ചു.
- ഓഡിയോ ട്രാൻസ്ക്രിപ്ഷൻ ടൂൾ സർവറുമായി രജിസ്റ്റർ ചെയ്തു.
- URL-ൽ നിന്നോ ബേസ്64 ഓഡിയോ ഡാറ്റ ഡികോഡ് ചെയ്യാനോ ഒരു മെത്തഡ് നടപ്പിലാക്കി.
- യഥാർത്ഥ ട്രാൻസ്ക്രിപ്ഷൻ ലജിക് കൈകാര്യം ചെയ്യാൻ `AudioProcessor` സർവീസ് ഉപയോഗിച്ചു.
- അഭ്യർത്ഥനകൾ കേൾക്കാൻ MCP സർവർ ആരംഭിച്ചു.

### മൾട്ടി-മോഡൽ ഉദാഹരണം: മൾട്ടി-മോഡൽ പ്രതികരണ സൃഷ്ടി

### പൈതൺ നടപ്പാക്കൽ

```python
from mcp_server import McpServer
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
import base64
from PIL import Image
import io
import requests
import json
from typing import Dict, Any, List, Optional

# ചിത്രം സൃഷ്ടിക്കുന്ന ഉപകരണം
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
            # പാരാമീറ്ററുകൾ എടുക്കുക
            prompt = request.parameters.get("prompt")
            style = request.parameters.get("style", "realistic")
            width = request.parameters.get("width", 512)
            height = request.parameters.get("height", 512)
            
            # ബാഹ്യ സേവനം ഉപയോഗിച്ച് ചിത്രം സൃഷ്ടിക്കുക (ഉദാഹരണ നടപ്പാക്കൽ)
            image_data = await self._generate_image(prompt, style, width, height)
            
            # പ്രതികരണത്തിനായി ചിത്രം ബേസ്64 ആയി മാറ്റുക
            buffered = io.BytesIO()
            image_data.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            # ചിത്രം കൂടാതെ മെറ്റാഡാറ്റയും ഉൾപ്പെടെ ഫലം തിരികെ നൽകുക
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
        # പ്ലേസ്ഹോൾഡർ ചിത്രം തിരികെ നൽകുക അല്ലെങ്കിൽ യഥാർത്ഥ ചിത്രം സൃഷ്ടിക്കുന്ന API വിളിക്കുക
        # ഈ ഉദാഹരണത്തിന്, നാം ഒരു ലളിതമായ നിറമുള്ള ചിത്രം സൃഷ്ടിക്കും
        image = Image.new('RGB', (width, height), color=(73, 109, 137))
        return image

# മൾട്ടി-മോഡൽ പ്രതികരണ ഹാൻഡ്ലർ
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
        
        # അഭ്യർത്ഥിച്ചാൽ ചിത്രങ്ങൾ സൃഷ്ടിക്കുക
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

# പ്രധാന അപ്ലിക്കേഷൻ
async def main():
    # സെർവർ സൃഷ്ടിക്കുക
    server = McpServer(
        name="Multi-Modal MCP Server",
        version="1.0.0",
        port=5000
    )
    
    # മൾട്ടി-മോഡൽ ഉപകരണങ്ങൾ രജിസ്റ്റർ ചെയ്യുക
    server.register_tool(ImageGenerationTool())
    server.register_tool(AudioAnalysisTool())
    server.register_tool(VideoFrameExtractionTool())
    
    # സെർവർ ആരംഭിക്കുക
    await server.start()
    print("Multi-Modal MCP Server running on port 5000")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## അടുത്തത് എന്താണ്

- [5.3 Oauth 2](../mcp-oauth2-demo/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->