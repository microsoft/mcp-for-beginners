# ការរួមបញ្ចូលមួយចំនួន

កម្មវិធីម៉ូឌែលច្រើនកំពុងក្លាយទៅជារឿងសំខាន់កាន់តែច្រើននៅក្នុង AI ដោយអាចបង្កើតការប៉ះពាល់មានភាពសំបូរបែប និងភារកិច្ចស្មុគស្មាញជាងមុន។ ពិធីសាស្រ្ត Model Context Protocol (MCP) ផ្តល់ស៊ុមស៊ីមសម្រាប់ស្ថាបនាកម្មវិធីម៉ូឌែលច្រើនដែលអាចដោះស្រាយទិន្នន័យវេទ្រសម្បូរបែប ដូចជាអក្សរ រូបភាព និងសម្លេង។

MCP គាំទ្រមិនត្រឹមតែការប៉ះពាល់ជាអក្សរនោះទេ តែថែមទាំងមានសមត្ថភាពម៉ូលទីម៉ូឌែល ដែលអនុញ្ញាតឲ្យម៉ូឌែលអាចដំណើរការជាមួយរូបភាព សម្លេង និងប្រភេទទិន្នន័យផ្សេងទៀត។

## ការណែនាំ

នៅក្នុងមេរៀននេះ អ្នកនឹងរៀនពីរបៀបបង្កើតកម្មវិធីម៉ូលទីម៉ូឌែល។

## គោលបំណងសិក្សា

នៅចុងបញ្ចប់មេរៀននេះ អ្នកនឹងអាច៖

- យល់ដឹងអំពីជម្រើសម៉ូឌែលច្រើន
- អនុវត្តកម្មវិធីម៉ូឌែលច្រើន។

## វត្ថុធាតុសម្រាប់គាំទ្រម៉ូលទីម៉ូឌែល

ការអនុវត្ត MCP ម៉ូលទីម៉ូឌែលភាគច្រើនរួមមាន៖

- **អ្នកបំលែងពីម៉ូឌែលជាក់លាក់**៖ ឧបករណ៍ដែលបម្លែងប្រភេទមិឌាយូនៗទៅទ្រង់ទ្រាយដែលម៉ូឌែលអាចដំណើរការ។
- **ឧបករណ៍សម្រាប់ម៉ូឌែលជាក់លាក់**៖ ឧបករណ៍ពិសេសដែលរចនាឡើងសម្រាប់ដោះស្រាយម៉ូឌែលជាក់លាក់ (វិភាគរូបភាព ការដំណើរការសម្លេង)
- **ការគ្រប់គ្រងបរិបទឯកសាររួម**៖ ប្រព័ន្ធដើម្បីរក្សាបរិបទក្នុងម៉ូឌែលផ្សេងៗគ្នា
- **ការបង្កើតចម្លើយ**៖ សមត្ថភាពបង្កើតចម្លើយដែលអាចរួមបញ្ចូលម៉ូឌែលច្រើន។

## ឧទាហរណ៍ម៉ូឌែលច្រើន៖ វិភាគរូបភាព

នៅឧទាហរណ៍ខាងក្រោម យើងនឹងវិភាគរូបភាពមួយ និងដកព័ត៌មានចេញមក។

### ការអនុវត្ត C#

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
  
នៅក្នុងឧទាហរណ៍មុននេះ យើងបាន៖

- បង្កើត `ImageAnalysisTool` ដែលអាចវិភាគរូបភាពដោយប្រើសេវាកម្មស្មានតែមួយ `IImageAnalysisService`។
- កំណត់រចនាសម្ព័ន្ធម៉ាស៊ីនមេ MCP ដើម្បីគាំទ្រការស្នើសុំធំៗ និងគាំទ្រប្រភេទមាតិការូបភាព។
- ចុះបញ្ជីឧបករណ៍វិភាគរូបភាពជាមួយម៉ាស៊ីនមេ។
- អនុវត្តវិធីសាស្រ្តទាញយករូបភាពពី URL និងវិភាគវាតាមប្រភេទដែលបានស្នើសុំ (វត្ថុ អក្សរ មនុស្សលក្ខណៈ បញ្ចូលជាដើម)។
- បញ្ចូនលទ្ធផលដែលមានរចនាប័ទ្មយ៉ាងត្រឹមត្រូវទៅតាមលក្ខ័ណ MCP។

## ឧទាហរណ៍ម៉ូឌែលច្រើន៖ ការបំលែងសម្លេង

ការបំលែងសម្លេងគឺជាម៉ូឌែលទៀងទាត់មួយទៀតនៅក្នុងកម្មវិធីម៉ូលទីម៉ូឌែល។ ខាងក្រោមជាឧទាហរណ៍ពីរបៀបអនុវត្តឧបករណ៍បំលែងសម្លេងដែលអាចដោះស្រាយឯកសារសម្លេង និងតបដោយអត្ថបទបំលែង។

### ការអនុវត្ត Java

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

// ឧបករណ៍បកប្រែសំឡេង
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
                
            // ទទួលសំឡេងពី URL ឬទិន្នន័យផ្ទាល់
            if (request.getParameters().has("audioUrl")) {
                String audioUrl = request.getParameters().get("audioUrl").asText();
                audioData = downloadAudio(audioUrl);
            } else if (request.getParameters().has("audioData")) {
                String base64Audio = request.getParameters().get("audioData").asText();
                audioData = Base64.getDecoder().decode(base64Audio);
            } else {
                throw new ToolExecutionException("Either audioUrl or audioData must be provided");
            }
            
            // ដំណើរការ​សំឡេង និង​បកប្រែ
            Map<String, Object> transcriptionResult = audioProcessor.transcribe(audioData, language);
            
            // ត្រឡប់លទ្ធផលការបកប្រែ
            return new ToolResponse.Builder()
                .setResult(transcriptionResult)
                .build();
        } catch (Exception ex) {
            throw new ToolExecutionException("Audio transcription failed: " + ex.getMessage(), ex);
        }
    }
    
    private byte[] downloadAudio(String url) {
        // អនុវត្តសម្រាប់ទាញយកសំឡេងពី URL
        // ...
        return new byte[0]; // កន្លែងដាក់ជំនួស
    }
}

// កម្មវិធីមុខងារសំឡេង និងរូបភាពផ្សេងៗ
public class MultiModalApplication {
    public static void main(String[] args) {
        // កំណត់តម្លៃសេវាកម្ម
        AudioProcessor audioProcessor = new AudioProcessor();
        ImageProcessor imageProcessor = new ImageProcessor();
        
        // បង្កើត និងកំណត់ម៉ាស៊ីនបម្រើ
        McpServer server = new McpServer.Builder()
            .setName("Multi-Modal MCP Server")
            .setVersion("1.0.0")
            .setPort(5000)
            .setMaxRequestSize(20 * 1024 * 1024) // 20MB សម្រាប់មាតិកាសំឡេង/វីដេអូ
            .build();
            
        // ចុះបញ្ជីឧបករណ៍ចម្រុះមុខងារ
        server.registerTool(new AudioTranscriptionTool(audioProcessor));
        server.registerTool(new ImageAnalysisTool(imageProcessor));
        server.registerTool(new VideoProcessingTool());
        
        // ចាប់ផ្តើមម៉ាស៊ីនបម្រើ
        server.start();
        System.out.println("Multi-Modal MCP Server started on port 5000");
    }
}
```
  
នៅក្នុងឧទាហរណ៍មុននេះ យើងបាន៖

- បង្កើត `AudioTranscriptionTool` ដែលអាចបំលែងឯកសារសំឡេង។
- កំណត់រចនាប័ទ្មឧបករណ៍ដើម្បីទទួល URL ឬទិន្នន័យសម្លេងកូដដូច base64។
- អនុវត្តវិធីសាស្រ្ត `execute` ដើម្បីដោះស្រាយការបំលែងសម្លេង។
- កំណត់រចនាសម្ព័ន្ធម៉ាស៊ីនមេ MCP ដើម្បីគាំទ្រការស្នើសុំម៉ូលទីម៉ូឌែល រួមទាំងការដំណើរការសម្លេង និងរូបភាព។
- ចុះបញ្ជីឧបករណ៍បំលែងសម្លេងជាមួយម៉ាស៊ីនមេ។
- អនុវត្តវិធីសាស្រ្តទាញយកឯកសារសម្លេងពី URL ឬលីយកូដ base64។
- ប្រើសេវាកម្ម `AudioProcessor` ដើម្បីដោះស្រាយមេគុណបំលែងសម្លេងពិត។
- ចាប់ផ្តើមម៉ាស៊ីនមេ MCP ដើម្បីស្ដាប់ស្នើសុំ។

### ឧទាហរណ៍ម៉ូឌែលច្រើន៖ ការបង្កើតចម្លើយម៉ូលទីម៉ូឌែល

### ការអនុវត្ត Python

```python
from mcp_server import McpServer
from mcp_tools import Tool, ToolRequest, ToolResponse, ToolExecutionException
import base64
from PIL import Image
import io
import requests
import json
from typing import Dict, Any, List, Optional

# ឧបករណ៍បង្កើតរូបភាព
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
            # ដោះស្រាយប៉ារ៉ាម៉ែត្រ
            prompt = request.parameters.get("prompt")
            style = request.parameters.get("style", "realistic")
            width = request.parameters.get("width", 512)
            height = request.parameters.get("height", 512)
            
            # បង្កើតរូបភាពដោយប្រើសេវាកម្មខាងក្រៅ (ការអនុវត្តឧទាហរណ៍)
            image_data = await self._generate_image(prompt, style, width, height)
            
            # ផ្ទេររូបភាពទៅជា base64 សម្រាប់ការឆ្លើយតប
            buffered = io.BytesIO()
            image_data.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            # ត្រឡប់លទ្ធផលជាមួយរូបភាព និងមេតាដាតា
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
        # ត្រឡប់រូបភាពជំនួសឬហៅ API បង្កើតរូបភាពពិត
        # សម្រាប់ឧទាហរណ៍នេះ យើងនឹងបង្កើតរូបភាពពណ៌សាមញ្ញមួយ
        image = Image.new('RGB', (width, height), color=(73, 109, 137))
        return image

# អ្នកដឹកនាំការឆ្លើយតបមួយចំនួន
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
        
        # បង្កើតរូបភាព ប្រសិនបើបានស្នើសុំ
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

# កម្មវិធីមេ
async def main():
    # បង្កើតម៉ាស៊ីនបម្រើ
    server = McpServer(
        name="Multi-Modal MCP Server",
        version="1.0.0",
        port=5000
    )
    
    # ចុះបញ្ជីឧបករណ៍ចម្រុះ
    server.register_tool(ImageGenerationTool())
    server.register_tool(AudioAnalysisTool())
    server.register_tool(VideoFrameExtractionTool())
    
    # ចាប់ផ្តើមម៉ាស៊ីនបម្រើ
    await server.start()
    print("Multi-Modal MCP Server running on port 5000")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```
  
## បន្ទាប់មកនៅតើអ្វី

- [5.3 Oauth 2](../mcp-oauth2-demo/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការព្រមាន**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំសំរាប់ភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវជាង។ ឯកសារដើមក្នុងភាសាដើមគួរត្រូវបានទទួលស្គាល់ថាជាមូលដ្ឋានផ្លូវការជាចម្បង។ សម្រាប់ព័ត៌មានសំខាន់ៗ គ្រាន់តែមានការបកប្រែដោយមនុស្សជំនាញផងដែរ។ យើងមិនទទួលខុសត្រូវចំពោះការជ្រុះចោល ឬការពន្យល់ខុសពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->