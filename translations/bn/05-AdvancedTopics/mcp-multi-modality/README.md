# মাল্টি-মোডাল ইন্টিগ্রেশন

মাল্টি-মোডাল অ্যাপ্লিকেশনগুলি AI-তে ক্রমবর্ধমান গুরুত্বপূর্ণ হয়ে উঠছে, যা আরও সমৃদ্ধ ইন্টারঅ্যাকশন এবং জটিল কাজ সম্পাদনের সুযোগ দেয়। Model Context Protocol (MCP) একটি ফ্রেমওয়ার্ক প্রদান করে যা বিভিন্ন ধরনের ডেটা যেমন টেক্সট, ছবি, এবং অডিও পরিচালনা করতে পারে এমন মাল্টি-মোডাল অ্যাপ্লিকেশন তৈরি করতে সাহায্য করে।

MCP শুধুমাত্র টেক্সট-ভিত্তিক ইন্টারঅ্যাকশনের জন্য নয়, মাল্টি-মোডাল সক্ষমতাও সমর্থন করে, যা মডেলগুলোকে ছবি, অডিও এবং অন্যান্য ডেটা টাইপের সাথে কাজ করার সুযোগ দেয়।

## পরিচিতি

এই পাঠে, আপনি শিখবেন কিভাবে একটি মাল্টি-মোডাল অ্যাপ্লিকেশন তৈরি করতে হয়।

## শেখার উদ্দেশ্য

এই পাঠের শেষে, আপনি সক্ষম হবেন:

- মাল্টি-মোডাল বিকল্পগুলো বুঝতে
- একটি মাল্টি-মোডাল অ্যাপ্লিকেশন বাস্তবায়ন করতে।

## মাল্টি-মোডাল সাপোর্টের আর্কিটেকচার

মাল্টি-মোডাল MCP বাস্তবায়ন সাধারণত অন্তর্ভুক্ত করে:

- **মোডাল-নির্দিষ্ট পার্সার**: এমন উপাদান যা বিভিন্ন মিডিয়া টাইপকে এমন ফরম্যাটে রূপান্তর করে যা মডেল প্রক্রিয়া করতে পারে।
- **মোডাল-নির্দিষ্ট টুলস**: বিশেষ টুলস যা নির্দিষ্ট মোডালিটি (ছবি বিশ্লেষণ, অডিও প্রক্রিয়াকরণ) পরিচালনার জন্য ডিজাইন করা হয়েছে।
- **এককৃত কনটেক্সট ম্যানেজমেন্ট**: বিভিন্ন মোডালিটির মধ্যে কনটেক্সট বজায় রাখার জন্য সিস্টেম।
- **রেসপন্স জেনারেশন**: এমন ক্ষমতা যা একাধিক মোডালিটি অন্তর্ভুক্ত করে এমন উত্তর তৈরি করতে পারে।

## মাল্টি-মোডাল উদাহরণ: ছবি বিশ্লেষণ

নিচের উদাহরণে, আমরা একটি ছবি বিশ্লেষণ করব এবং তথ্য আহরণ করব।

### C# বাস্তবায়ন

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

উপরের উদাহরণে, আমরা:

- একটি `ImageAnalysisTool` তৈরি করেছি যা একটি কাল্পনিক `IImageAnalysisService` ব্যবহার করে ছবি বিশ্লেষণ করতে পারে।
- MCP সার্ভারকে বড় অনুরোধ গ্রহণ এবং ছবি কনটেন্ট টাইপ সমর্থন করার জন্য কনফিগার করেছি।
- সার্ভারে ছবি বিশ্লেষণ টুলটি নিবন্ধন করেছি।
- একটি পদ্ধতি বাস্তবায়ন করেছি যা URL থেকে ছবি ডাউনলোড করে এবং অনুরোধকৃত ধরণের (বস্তু, টেক্সট, মুখ ইত্যাদি) উপর ভিত্তি করে বিশ্লেষণ করে।
- MCP স্পেসিফিকেশনের সাথে সামঞ্জস্যপূর্ণ ফরম্যাটে কাঠামোবদ্ধ ফলাফল ফেরত দিয়েছি।

## মাল্টি-মোডাল উদাহরণ: অডিও প্রক্রিয়াকরণ

অডিও প্রক্রিয়াকরণ মাল্টি-মোডাল অ্যাপ্লিকেশনগুলোর আরেকটি সাধারণ মোডালিটি। নিচে একটি উদাহরণ দেওয়া হয়েছে কিভাবে একটি অডিও ট্রান্সক্রিপশন টুল তৈরি করা যায় যা অডিও ফাইল পরিচালনা করে এবং ট্রান্সক্রিপশন প্রদান করে।

### Java বাস্তবায়ন

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

উপরের উদাহরণে, আমরা:

- একটি `AudioTranscriptionTool` তৈরি করেছি যা অডিও ফাইল ট্রান্সক্রাইব করতে পারে।
- টুলের স্কিমা নির্ধারণ করেছি যা URL অথবা base64-এনকোডেড অডিও ডেটা গ্রহণ করতে পারে।
- `execute` মেথডটি বাস্তবায়ন করেছি যা অডিও প্রক্রিয়াকরণ এবং ট্রান্সক্রিপশন পরিচালনা করে।
- MCP সার্ভারকে মাল্টি-মোডাল অনুরোধ, যার মধ্যে অডিও এবং ছবি প্রক্রিয়াকরণ অন্তর্ভুক্ত, পরিচালনার জন্য কনফিগার করেছি।
- অডিও ট্রান্সক্রিপশন টুলটি সার্ভারে নিবন্ধন করেছি।
- একটি পদ্ধতি বাস্তবায়ন করেছি যা URL থেকে অডিও ফাইল ডাউনলোড করে অথবা base64 অডিও ডেটা ডিকোড করে।
- একটি `AudioProcessor` সার্ভিস ব্যবহার করেছি যা প্রকৃত ট্রান্সক্রিপশন লজিক পরিচালনা করে।
- MCP সার্ভার শুরু করেছি যাতে অনুরোধ শোনার জন্য প্রস্তুত থাকে।

### মাল্টি-মোডাল উদাহরণ: মাল্টি-মোডাল রেসপন্স জেনারেশন

### Python বাস্তবায়ন

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

## পরবর্তী ধাপ

- [5.3 Oauth 2](../mcp-oauth2-demo/README.md)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।