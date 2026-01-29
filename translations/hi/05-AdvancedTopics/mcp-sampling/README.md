# मॉडल कॉन्टेक्स्ट प्रोटोकॉल में सैंपलिंग

सैंपलिंग एक शक्तिशाली MCP फीचर है जो सर्वरों को क्लाइंट के माध्यम से LLM पूर्णताएँ अनुरोध करने की अनुमति देता है, जिससे जटिल एजेंटिक व्यवहार संभव होते हैं जबकि सुरक्षा और गोपनीयता बनी रहती है। सही सैंपलिंग कॉन्फ़िगरेशन प्रतिक्रिया की गुणवत्ता और प्रदर्शन में नाटकीय सुधार कर सकता है। MCP एक मानकीकृत तरीका प्रदान करता है जिससे मॉडल विशिष्ट पैरामीटर के साथ टेक्स्ट उत्पन्न करते हैं, जो यादृच्छिकता, रचनात्मकता और सुसंगतता को प्रभावित करते हैं।

## परिचय

इस पाठ में, हम MCP अनुरोधों में सैंपलिंग पैरामीटर को कॉन्फ़िगर करना सीखेंगे और सैंपलिंग के अंतर्निहित प्रोटोकॉल मैकेनिक्स को समझेंगे।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- MCP में उपलब्ध मुख्य सैंपलिंग पैरामीटर को समझना।
- विभिन्न उपयोग मामलों के लिए सैंपलिंग पैरामीटर को कॉन्फ़िगर करना।
- पुनरुत्पादनीय परिणामों के लिए निर्धारक सैंपलिंग लागू करना।
- संदर्भ और उपयोगकर्ता प्राथमिकताओं के आधार पर सैंपलिंग पैरामीटर को गतिशील रूप से समायोजित करना।
- विभिन्न परिदृश्यों में मॉडल प्रदर्शन बढ़ाने के लिए सैंपलिंग रणनीतियों को लागू करना।
- MCP के क्लाइंट-सर्वर प्रवाह में सैंपलिंग कैसे काम करती है, इसे समझना।

## MCP में सैंपलिंग कैसे काम करती है

MCP में सैंपलिंग प्रवाह निम्नलिखित चरणों का पालन करता है:

1. सर्वर क्लाइंट को `sampling/createMessage` अनुरोध भेजता है
2. क्लाइंट अनुरोध की समीक्षा करता है और इसे संशोधित कर सकता है
3. क्लाइंट LLM से सैंपल करता है
4. क्लाइंट पूर्णता की समीक्षा करता है
5. क्लाइंट परिणाम सर्वर को लौटाता है

यह मानव-इन-द-लूप डिज़ाइन सुनिश्चित करता है कि उपयोगकर्ता नियंत्रित करें कि LLM क्या देखता है और उत्पन्न करता है।

## सैंपलिंग पैरामीटर का अवलोकन

MCP निम्नलिखित सैंपलिंग पैरामीटर को परिभाषित करता है जिन्हें क्लाइंट अनुरोधों में कॉन्फ़िगर किया जा सकता है:

| पैरामीटर | विवरण | सामान्य सीमा |
|-----------|-------------|---------------|
| `temperature` | टोकन चयन में यादृच्छिकता को नियंत्रित करता है | 0.0 - 1.0 |
| `maxTokens` | उत्पन्न किए जाने वाले अधिकतम टोकन की संख्या | पूर्णांक मान |
| `stopSequences` | कस्टम अनुक्रम जो मिलने पर जनरेशन रोकते हैं | स्ट्रिंग्स की सूची |
| `metadata` | अतिरिक्त प्रदाता-विशिष्ट पैरामीटर | JSON ऑब्जेक्ट |

कई LLM प्रदाता `metadata` फ़ील्ड के माध्यम से अतिरिक्त पैरामीटर का समर्थन करते हैं, जिनमें शामिल हो सकते हैं:

| सामान्य एक्सटेंशन पैरामीटर | विवरण | सामान्य सीमा |
|-----------|-------------|---------------|
| `top_p` | न्यूक्लियस सैंपलिंग - टोकन को शीर्ष संचयी संभावना तक सीमित करता है | 0.0 - 1.0 |
| `top_k` | टोकन चयन को शीर्ष K विकल्पों तक सीमित करता है | 1 - 100 |
| `presence_penalty` | अब तक के टेक्स्ट में टोकन की उपस्थिति के आधार पर दंडित करता है | -2.0 - 2.0 |
| `frequency_penalty` | अब तक के टेक्स्ट में टोकन की आवृत्ति के आधार पर दंडित करता है | -2.0 - 2.0 |
| `seed` | पुनरुत्पादनीय परिणामों के लिए विशिष्ट यादृच्छिक बीज | पूर्णांक मान |

## उदाहरण अनुरोध प्रारूप

यहाँ MCP में क्लाइंट से सैंपलिंग अनुरोध करने का एक उदाहरण है:

```json
{
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "What files are in the current directory?"
        }
      }
    ],
    "systemPrompt": "You are a helpful file system assistant.",
    "includeContext": "thisServer",
    "maxTokens": 100,
    "temperature": 0.7
  }
}
```

## प्रतिक्रिया प्रारूप

क्लाइंट एक पूर्णता परिणाम लौटाता है:

```json
{
  "model": "string",  // Name of the model used
  "stopReason": "endTurn" | "stopSequence" | "maxTokens" | "string",
  "role": "assistant",
  "content": {
    "type": "text",
    "text": "string"
  }
}
```

## मानव-इन-द-लूप नियंत्रण

MCP सैंपलिंग मानव निगरानी को ध्यान में रखकर डिज़ाइन किया गया है:

- **प्रॉम्प्ट के लिए**:
  - क्लाइंट उपयोगकर्ताओं को प्रस्तावित प्रॉम्प्ट दिखाएं
  - उपयोगकर्ता प्रॉम्प्ट को संशोधित या अस्वीकार कर सकें
  - सिस्टम प्रॉम्प्ट को फ़िल्टर या संशोधित किया जा सकता है
  - संदर्भ समावेशन क्लाइंट द्वारा नियंत्रित होता है

- **पूर्णताओं के लिए**:
  - क्लाइंट उपयोगकर्ताओं को पूर्णता दिखाएं
  - उपयोगकर्ता पूर्णताओं को संशोधित या अस्वीकार कर सकें
  - क्लाइंट पूर्णताओं को फ़िल्टर या संशोधित कर सकता है
  - उपयोगकर्ता नियंत्रित करते हैं कि कौन सा मॉडल उपयोग किया जाए

इन सिद्धांतों को ध्यान में रखते हुए, आइए देखें कि विभिन्न प्रोग्रामिंग भाषाओं में सैंपलिंग कैसे लागू करें, खासकर उन पैरामीटरों पर जो आमतौर पर LLM प्रदाताओं द्वारा समर्थित हैं।

## सुरक्षा विचार

MCP में सैंपलिंग लागू करते समय इन सुरक्षा सर्वोत्तम प्रथाओं पर विचार करें:

- **सभी संदेश सामग्री को मान्य करें** इससे पहले कि इसे क्लाइंट को भेजा जाए
- **प्रॉम्प्ट और पूर्णताओं से संवेदनशील जानकारी को साफ़ करें**
- **दुरुपयोग रोकने के लिए दर सीमाएँ लागू करें**
- **असामान्य पैटर्न के लिए सैंपलिंग उपयोग की निगरानी करें**
- **सुरक्षित प्रोटोकॉल का उपयोग करके डेटा को ट्रांजिट में एन्क्रिप्ट करें**
- **प्रासंगिक नियमों के अनुसार उपयोगकर्ता डेटा गोपनीयता को संभालें**
- **अनुपालन और सुरक्षा के लिए सैंपलिंग अनुरोधों का ऑडिट करें**
- **उचित सीमाओं के साथ लागत जोखिम को नियंत्रित करें**
- **सैंपलिंग अनुरोधों के लिए टाइमआउट लागू करें**
- **मॉडल त्रुटियों को उपयुक्त बैकअप के साथ सहजता से संभालें**

सैंपलिंग पैरामीटर भाषा मॉडलों के व्यवहार को सूक्ष्म रूप से समायोजित करने की अनुमति देते हैं ताकि निर्धारक और रचनात्मक आउटपुट के बीच वांछित संतुलन प्राप्त किया जा सके।

आइए देखें कि इन पैरामीटरों को विभिन्न प्रोग्रामिंग भाषाओं में कैसे कॉन्फ़िगर किया जाए।

# [.NET](../../../../05-AdvancedTopics/mcp-sampling)

```csharp
// .NET Example: Configuring sampling parameters in MCP
public class SamplingExample
{
    public async Task RunWithSamplingAsync()
    {
        // Create MCP client with sampling configuration
        var client = new McpClient("https://mcp-server-url.com");
        
        // Create request with specific sampling parameters
        var request = new McpRequest
        {
            Prompt = "Generate creative ideas for a mobile app",
            SamplingParameters = new SamplingParameters
            {
                Temperature = 0.8f,     // Higher temperature for more creative outputs
                TopP = 0.95f,           // Nucleus sampling parameter
                TopK = 40,              // Limit token selection to top K options
                FrequencyPenalty = 0.5f, // Reduce repetition
                PresencePenalty = 0.2f   // Encourage diversity
            },
            AllowedTools = new[] { "ideaGenerator", "marketAnalyzer" }
        };
        
        // Send request using specific sampling configuration
        var response = await client.SendRequestAsync(request);
        
        // Output results
        Console.WriteLine($"Generated with Temperature={request.SamplingParameters.Temperature}:");
        Console.WriteLine(response.GeneratedText);
    }
}
```

पिछले कोड में हमने:

- एक विशिष्ट सर्वर URL के साथ MCP क्लाइंट बनाया।
- `temperature`, `top_p`, और `top_k` जैसे सैंपलिंग पैरामीटर के साथ एक अनुरोध कॉन्फ़िगर किया।
- अनुरोध भेजा और उत्पन्न टेक्स्ट को प्रिंट किया।
- उपयोग किया:
    - `allowedTools` यह निर्दिष्ट करने के लिए कि मॉडल जनरेशन के दौरान किन टूल्स का उपयोग कर सकता है। इस मामले में, हमने रचनात्मक ऐप विचारों को उत्पन्न करने में मदद के लिए `ideaGenerator` और `marketAnalyzer` टूल्स की अनुमति दी।
    - `frequencyPenalty` और `presencePenalty` आउटपुट में पुनरावृत्ति और विविधता को नियंत्रित करने के लिए।
    - `temperature` आउटपुट की यादृच्छिकता को नियंत्रित करने के लिए, जहां उच्च मान अधिक रचनात्मक प्रतिक्रियाओं की ओर ले जाते हैं।
    - `top_p` टोकन चयन को शीर्ष संचयी संभावना वाले टोकन तक सीमित करने के लिए, जिससे उत्पन्न टेक्स्ट की गुणवत्ता बढ़ती है।
    - `top_k` मॉडल को शीर्ष K सबसे संभावित टोकन तक सीमित करने के लिए, जो अधिक सुसंगत प्रतिक्रियाओं में मदद करता है।
    - `frequencyPenalty` और `presencePenalty` पुनरावृत्ति को कम करने और उत्पन्न टेक्स्ट में विविधता को प्रोत्साहित करने के लिए।

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Temperature and Top-P sampling configuration
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Initialize the MCP client
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Configure request with different sampling parameters
  const creativeSampling = {
    temperature: 0.9,    // Higher temperature = more randomness/creativity
    topP: 0.92,          // Consider tokens with top 92% probability mass
    frequencyPenalty: 0.6, // Reduce repetition of token sequences
    presencePenalty: 0.4   // Penalize tokens that have appeared in the text so far
  };
  
  const factualSampling = {
    temperature: 0.2,    // Lower temperature = more deterministic/factual
    topP: 0.85,          // Slightly more focused token selection
    frequencyPenalty: 0.2, // Minimal repetition penalty
    presencePenalty: 0.1   // Minimal presence penalty
  };
  
  try {
    // Send two requests with different sampling configurations
    const creativeResponse = await client.sendPrompt(
      "Generate innovative ideas for sustainable urban transportation",
      {
        allowedTools: ['ideaGenerator', 'environmentalImpactTool'],
        ...creativeSampling
      }
    );
    
    const factualResponse = await client.sendPrompt(
      "Explain how electric vehicles impact carbon emissions",
      {
        allowedTools: ['factChecker', 'dataAnalysisTool'],
        ...factualSampling
      }
    );
    
    console.log('Creative Response (temperature=0.9):');
    console.log(creativeResponse.generatedText);
    
    console.log('\nFactual Response (temperature=0.2):');
    console.log(factualResponse.generatedText);
    
  } catch (error) {
    console.error('Error demonstrating sampling:', error);
  }
}

demonstrateSampling();
```

पिछले कोड में हमने:

- एक सर्वर URL और API कुंजी के साथ MCP क्लाइंट इनिशियलाइज़ किया।
- दो सेट सैंपलिंग पैरामीटर कॉन्फ़िगर किए: एक रचनात्मक कार्यों के लिए और दूसरा तथ्यात्मक कार्यों के लिए।
- इन कॉन्फ़िगरेशन के साथ अनुरोध भेजे, जिससे मॉडल को प्रत्येक कार्य के लिए विशिष्ट टूल्स का उपयोग करने की अनुमति मिली।
- उत्पन्न प्रतिक्रियाओं को प्रिंट किया ताकि विभिन्न सैंपलिंग पैरामीटर के प्रभाव दिखाए जा सकें।
- उपयोग किया `allowedTools` यह निर्दिष्ट करने के लिए कि मॉडल जनरेशन के दौरान किन टूल्स का उपयोग कर सकता है। इस मामले में, रचनात्मक कार्यों के लिए `ideaGenerator` और `environmentalImpactTool` की अनुमति दी गई, और तथ्यात्मक कार्यों के लिए `factChecker` और `dataAnalysisTool` की।
- उपयोग किया `temperature` आउटपुट की यादृच्छिकता को नियंत्रित करने के लिए, जहां उच्च मान अधिक रचनात्मक प्रतिक्रियाओं की ओर ले जाते हैं।
- उपयोग किया `top_p` टोकन चयन को शीर्ष संचयी संभावना वाले टोकन तक सीमित करने के लिए, जिससे उत्पन्न टेक्स्ट की गुणवत्ता बढ़ती है।
- उपयोग किया `frequencyPenalty` और `presencePenalty` आउटपुट में पुनरावृत्ति को कम करने और विविधता को प्रोत्साहित करने के लिए।
- उपयोग किया `top_k` मॉडल को शीर्ष K सबसे संभावित टोकन तक सीमित करने के लिए, जो अधिक सुसंगत प्रतिक्रियाओं में मदद करता है।

---

## निर्धारक सैंपलिंग

ऐसे अनुप्रयोगों के लिए जिन्हें सुसंगत आउटपुट की आवश्यकता होती है, निर्धारक सैंपलिंग पुनरुत्पादनीय परिणाम सुनिश्चित करता है। यह एक निश्चित यादृच्छिक बीज का उपयोग करके और तापमान को शून्य पर सेट करके किया जाता है।

आइए नीचे दिए गए उदाहरण को देखें जो विभिन्न प्रोग्रामिंग भाषाओं में निर्धारक सैंपलिंग को प्रदर्शित करता है।

# [Java](../../../../05-AdvancedTopics/mcp-sampling)

```java
// Java Example: Deterministic responses with fixed seed
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Using a fixed seed for deterministic results
        
        // First request with fixed seed
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Zero temperature for maximum determinism
            .build();
            
        // Second request with the same seed
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Execute both requests
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Responses should be identical due to same seed and temperature=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

पिछले कोड में हमने:

- एक निर्दिष्ट सर्वर URL के साथ MCP क्लाइंट बनाया।
- एक ही प्रॉम्प्ट, निश्चित बीज, और शून्य तापमान के साथ दो अनुरोध कॉन्फ़िगर किए।
- दोनों अनुरोध भेजे और उत्पन्न टेक्स्ट को प्रिंट किया।
- दिखाया कि प्रतिक्रियाएँ समान हैं क्योंकि सैंपलिंग कॉन्फ़िगरेशन (एक ही बीज और तापमान) निर्धारक है।
- `setSeed` का उपयोग किया ताकि एक निश्चित यादृच्छिक बीज निर्दिष्ट किया जा सके, जिससे मॉडल हर बार एक ही इनपुट के लिए समान आउटपुट उत्पन्न करे।
- `temperature` को शून्य पर सेट किया ताकि अधिकतम निर्धारकता सुनिश्चित हो, यानी मॉडल हमेशा सबसे संभावित अगला टोकन यादृच्छिकता के बिना चुने।

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Deterministic responses with seed control
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // First request with fixed seed
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Zero temperature for maximum determinism
    });
    
    // Second request with same seed and temperature
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Third request with different seed but same temperature
    const response3 = await client.sendPrompt(prompt, {
      seed: 67890,
      temperature: 0.0
    });
    
    console.log('Response 1:', response1.generatedText);
    console.log('Response 2:', response2.generatedText);
    console.log('Response 3:', response3.generatedText);
    console.log('Responses 1 and 2 match:', response1.generatedText === response2.generatedText);
    console.log('Responses 1 and 3 match:', response1.generatedText === response3.generatedText);
    
  } catch (error) {
    console.error('Error in deterministic sampling demo:', error);
  }
}

deterministicSampling();
```

पिछले कोड में हमने:

- एक सर्वर URL के साथ MCP क्लाइंट इनिशियलाइज़ किया।
- एक ही प्रॉम्प्ट, निश्चित बीज, और शून्य तापमान के साथ दो अनुरोध कॉन्फ़िगर किए।
- दोनों अनुरोध भेजे और उत्पन्न टेक्स्ट को प्रिंट किया।
- दिखाया कि प्रतिक्रियाएँ समान हैं क्योंकि सैंपलिंग कॉन्फ़िगरेशन (एक ही बीज और तापमान) निर्धारक है।
- `seed` का उपयोग किया ताकि एक निश्चित यादृच्छिक बीज निर्दिष्ट किया जा सके, जिससे मॉडल हर बार एक ही इनपुट के लिए समान आउटपुट उत्पन्न करे।
- `temperature` को शून्य पर सेट किया ताकि अधिकतम निर्धारकता सुनिश्चित हो, यानी मॉडल हमेशा सबसे संभावित अगला टोकन यादृच्छिकता के बिना चुने।
- तीसरे अनुरोध के लिए अलग बीज का उपयोग किया ताकि दिखाया जा सके कि बीज बदलने पर, भले ही प्रॉम्प्ट और तापमान समान हों, आउटपुट अलग होंगे।

---

## गतिशील सैंपलिंग कॉन्फ़िगरेशन

स्मार्ट सैंपलिंग प्रत्येक अनुरोध के संदर्भ और आवश्यकताओं के आधार पर पैरामीटर को अनुकूलित करता है। इसका मतलब है कि तापमान, top_p, और दंड जैसे पैरामीटर को कार्य के प्रकार, उपयोगकर्ता प्राथमिकताओं, या ऐतिहासिक प्रदर्शन के आधार पर गतिशील रूप से समायोजित करना।

आइए देखें कि विभिन्न प्रोग्रामिंग भाषाओं में गतिशील सैंपलिंग कैसे लागू करें।

# [Python](../../../../05-AdvancedTopics/mcp-sampling)

```python
# Python Example: Dynamic sampling based on request context
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Define sampling presets for different task types
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Select base preset
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Adjust based on user preferences if provided
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Scale temperature based on creativity preference (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Adjust top_p based on desired response diversity
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Create and send request with custom sampling parameters
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Return response with sampling metadata for transparency
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

पिछले कोड में हमने:

- एक `DynamicSamplingService` क्लास बनाया जो अनुकूली सैंपलिंग का प्रबंधन करता है।
- विभिन्न कार्य प्रकारों (रचनात्मक, तथ्यात्मक, कोड, विश्लेषणात्मक) के लिए सैंपलिंग प्रीसेट परिभाषित किए।
- कार्य प्रकार के आधार पर एक बेस सैंपलिंग प्रीसेट चुना।
- उपयोगकर्ता प्राथमिकताओं जैसे रचनात्मकता स्तर और विविधता के आधार पर सैंपलिंग पैरामीटर समायोजित किए।
- गतिशील रूप से कॉन्फ़िगर किए गए सैंपलिंग पैरामीटर के साथ अनुरोध भेजा।
- उत्पन्न टेक्स्ट के साथ लागू सैंपलिंग पैरामीटर और कार्य प्रकार भी लौटाए ताकि पारदर्शिता बनी रहे।
- उपयोग किया:
    - `temperature` आउटपुट की यादृच्छिकता को नियंत्रित करने के लिए, जहां उच्च मान अधिक रचनात्मक प्रतिक्रियाओं की ओर ले जाते हैं।
    - `top_p` टोकन चयन को शीर्ष संचयी संभावना वाले टोकन तक सीमित करने के लिए, जिससे उत्पन्न टेक्स्ट की गुणवत्ता बढ़ती है।
    - `frequency_penalty` पुनरावृत्ति को कम करने और विविधता को प्रोत्साहित करने के लिए।
    - `user_preferences` उपयोगकर्ता-परिभाषित रचनात्मकता और विविधता स्तर के आधार पर सैंपलिंग पैरामीटर को अनुकूलित करने के लिए।
    - `task_type` अनुरोध के लिए उपयुक्त सैंपलिंग रणनीति निर्धारित करने के लिए, जिससे कार्य की प्रकृति के आधार पर अधिक अनुकूलित प्रतिक्रियाएं मिलती हैं।
    - `send_request` विधि का उपयोग प्रॉम्प्ट के साथ कॉन्फ़िगर किए गए सैंपलिंग पैरामीटर भेजने के लिए, यह सुनिश्चित करते हुए कि मॉडल निर्दिष्ट आवश्यकताओं के अनुसार टेक्स्ट उत्पन्न करे।
    - `generated_text` मॉडल की प्रतिक्रिया प्राप्त करने के लिए, जिसे फिर सैंपलिंग पैरामीटर और कार्य प्रकार के साथ लौटाया जाता है।
    - `min` और `max` फ़ंक्शन का उपयोग यह सुनिश्चित करने के लिए किया गया कि उपयोगकर्ता प्राथमिकताएँ मान्य सीमाओं के भीतर हों, जिससे अमान्य सैंपलिंग कॉन्फ़िगरेशन से बचा जा सके।

# [JavaScript Dynamic](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Dynamic sampling configuration based on user context
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Define base sampling profiles
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Track historical performance
    this.performanceHistory = [];
  }
  
  // Detect task type from prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Simple heuristic detection - could be enhanced with ML classification
    if (context.taskType) return context.taskType;
    
    if (promptLower.includes('code') || 
        promptLower.includes('function') || 
        promptLower.includes('program')) {
      return 'code';
    }
    
    if (promptLower.includes('explain') || 
        promptLower.includes('what is') || 
        promptLower.includes('how does')) {
      return 'factual';
    }
    
    if (promptLower.includes('creative') || 
        promptLower.includes('imagine') || 
        promptLower.includes('story')) {
      return 'creative';
    }
    
    // Default to conversational if no clear type is detected
    return 'conversational';
  }
  
  // Calculate sampling parameters based on context and user preferences
  getSamplingParameters(prompt, context = {}) {
    // Detect the type of task
    const taskType = this.detectTaskType(prompt, context);
    
    // Get base profile
    let params = {...this.samplingProfiles[taskType]};
    
    // Adjust based on user preferences
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Scale from 1-10 to appropriate temperature range
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Higher precision means lower topP (more focused selection)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Higher consistency means lower penalties
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Apply learned adjustments from performance history
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Simple adaptive logic - could be enhanced with more sophisticated algorithms
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Only consider recent history
    
    if (relevantHistory.length > 0) {
      // Calculate average performance scores
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // If performance is below threshold, adjust parameters
      if (avgScore < 0.7) {
        // Slight adjustment toward safer values
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Record performance for future adjustments
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 rating of response quality
    });
    
    // Limit history size
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Get optimized sampling parameters
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Send request with optimized parameters
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // If user provides feedback, record it for future optimization
    if (context.recordPerformance) {
      this.recordPerformance(prompt, samplingParams, response, context.feedbackScore || 0.5);
    }
    
    return {
      response,
      appliedSamplingParams: samplingParams,
      detectedTaskType: this.detectTaskType(prompt, context)
    };
  }
}

// Example usage
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Creative task with custom user preferences
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // High creativity (1-10)
          consistency: 3  // Low consistency (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Code generation task
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Low creativity
          precision: 8,   // High precision
          consistency: 9  // High consistency
        }
      }
    );
    
    console.log('\nCode Task:');
    console.log(`Detected type: ${codeResult.detectedTaskType}`);
    console.log('Applied sampling:', codeResult.appliedSamplingParams);
    console.log(codeResult.response.generatedText);
    
  } catch (error) {
    console.error('Error in adaptive sampling demo:', error);
  }
}

demonstrateAdaptiveSampling();
```

पिछले कोड में हमने:

- एक `AdaptiveSamplingManager` क्लास बनाया जो कार्य प्रकार और उपयोगकर्ता प्राथमिकताओं के आधार पर गतिशील सैंपलिंग का प्रबंधन करता है।
- विभिन्न कार्य प्रकारों (रचनात्मक, तथ्यात्मक, कोड, संवादात्मक) के लिए सैंपलिंग प्रोफाइल परिभाषित किए।
- सरल हीयूरिस्टिक्स का उपयोग करके प्रॉम्प्ट से कार्य प्रकार का पता लगाने के लिए एक विधि लागू की।
- पता लगाए गए कार्य प्रकार और उपयोगकर्ता प्राथमिकताओं के आधार पर सैंपलिंग पैरामीटर की गणना की।
- ऐतिहासिक प्रदर्शन के आधार पर सीखे गए समायोजन लागू किए ताकि सैंपलिंग पैरामीटर का अनुकूलन हो सके।
- भविष्य के समायोजनों के लिए प्रदर्शन रिकॉर्ड किया, जिससे सिस्टम पिछले इंटरैक्शन से सीख सके।
- गतिशील रूप से कॉन्फ़िगर किए गए सैंपलिंग पैरामीटर के साथ अनुरोध भेजे और उत्पन्न टेक्स्ट को लागू पैरामीटर और पता लगाए गए कार्य प्रकार के साथ लौटाया।
- उपयोग किया:
    - `userPreferences` उपयोगकर्ता-परिभाषित रचनात्मकता, सटीकता, और स्थिरता स्तर के आधार पर सैंपलिंग पैरामीटर को अनुकूलित करने के लिए।
    - `detectTaskType` प्रॉम्प्ट के आधार पर कार्य की प्रकृति निर्धारित करने के लिए, जिससे अधिक अनुकूलित प्रतिक्रियाएं मिलती हैं।
    - `recordPerformance` उत्पन्न प्रतिक्रियाओं के प्रदर्शन को लॉग करने के लिए, जिससे सिस्टम समय के साथ अनुकूलित हो सके।
    - `applyLearnedAdjustments` ऐतिहासिक प्रदर्शन के आधार पर सैंपलिंग पैरामीटर को संशोधित करने के लिए, जिससे उच्च गुणवत्ता वाली प्रतिक्रियाएं उत्पन्न करने की क्षमता बढ़ती है।
    - `generateResponse` पूरी प्रक्रिया को समाहित करने के लिए, जिससे विभिन्न प्रॉम्प्ट और संदर्भों के साथ कॉल करना आसान हो।
    - `allowedTools` यह निर्दिष्ट करने के लिए कि मॉडल जनरेशन के दौरान किन टूल्स का उपयोग कर सकता है, जिससे अधिक संदर्भ-संवेदनशील प्रतिक्रियाएं मिलती हैं।
    - `feedbackScore` उपयोगकर्ताओं को उत्पन्न प्रतिक्रिया की गुणवत्ता पर प्रतिक्रिया देने की अनुमति देने के लिए, जिसका उपयोग मॉडल के प्रदर्शन को समय के साथ बेहतर बनाने के लिए किया जा सकता है।
    - `performanceHistory` पिछले इंटरैक्शन का रिकॉर्ड बनाए रखने के लिए, जिससे सिस्टम पिछली सफलताओं और असफलताओं से सीख सके।
    - `getSamplingParameters` अनुरोध के संदर्भ के आधार पर सैंपलिंग पैरामीटर को गतिशील रूप से समायोजित करने के लिए, जिससे मॉडल व्यवहार अधिक लचीला और प्रतिक्रियाशील हो।
    - `detectTaskType` प्रॉम्प्ट के आधार

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।