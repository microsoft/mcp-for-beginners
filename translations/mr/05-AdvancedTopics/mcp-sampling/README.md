# Sampling in Model Context Protocol

Sampling हा एक शक्तिशाली MCP वैशिष्ट्य आहे जो सर्व्हर्सना क्लायंटद्वारे LLM पूर्णता विनंत्या करण्याची परवानगी देतो, ज्यामुळे सुरक्षितता आणि गोपनीयता राखून प्रगत एजंटिक वर्तन शक्य होते. योग्य sampling कॉन्फिगरेशन प्रतिसादाची गुणवत्ता आणि कार्यक्षमता लक्षणीयरीत्या सुधारू शकते. MCP मॉडेल्सना विशिष्ट पॅरामीटर्ससह मजकूर निर्माण करण्यासाठी नियंत्रित करण्याचा एक मानकीकृत मार्ग प्रदान करतो, जे यादृच्छिकता, सर्जनशीलता आणि सुसंगततेवर परिणाम करतात.

## परिचय

या धड्यात आपण MCP विनंत्यांमध्ये sampling पॅरामीटर्स कसे कॉन्फिगर करायचे आणि sampling च्या अंतर्निहित प्रोटोकॉल यांत्रिकी कशी कार्य करते हे पाहणार आहोत.

## शिकण्याचे उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही सक्षम असाल:

- MCP मध्ये उपलब्ध मुख्य sampling पॅरामीटर्स समजून घेणे.
- वेगवेगळ्या वापरासाठी sampling पॅरामीटर्स कॉन्फिगर करणे.
- पुनरुत्पादनीय निकालांसाठी deterministic sampling अंमलात आणणे.
- संदर्भ आणि वापरकर्त्याच्या पसंतीनुसार sampling पॅरामीटर्स गतिशीलपणे समायोजित करणे.
- विविध परिस्थितींमध्ये मॉडेल कार्यक्षमता सुधारण्यासाठी sampling धोरणे लागू करणे.
- MCP च्या क्लायंट-सर्व्हर प्रवाहात sampling कसे कार्य करते हे समजून घेणे.

## MCP मध्ये Sampling कसे कार्य करते

MCP मधील sampling प्रवाह खालील टप्प्यांनुसार चालतो:

1. सर्व्हर `sampling/createMessage` विनंती क्लायंटकडे पाठवतो
2. क्लायंट विनंती तपासतो आणि आवश्यक असल्यास बदल करू शकतो
3. क्लायंट LLM मधून sampling करतो
4. क्लायंट पूर्णता तपासतो
5. क्लायंट निकाल सर्व्हरकडे परत पाठवतो

हा मानव-इन-द-लूप डिझाइन वापरकर्त्यांना LLM काय पाहते आणि तयार करते यावर नियंत्रण ठेवण्याची खात्री देतो.

## Sampling पॅरामीटर्सचे आढावा

MCP खालील sampling पॅरामीटर्स परिभाषित करतो जे क्लायंट विनंत्यांमध्ये कॉन्फिगर करता येतात:

| Parameter | वर्णन | सामान्य श्रेणी |
|-----------|-------------|---------------|
| `temperature` | टोकन निवडीत randomness नियंत्रित करते | 0.0 - 1.0 |
| `maxTokens` | तयार करावयाच्या टोकन्सची कमाल संख्या | पूर्णांक मूल्य |
| `stopSequences` | सानुकूल अनुक्रम जे आढळल्यावर निर्मिती थांबवतात | स्ट्रिंग्जची यादी |
| `metadata` | अतिरिक्त प्रदाता-विशिष्ट पॅरामीटर्स | JSON ऑब्जेक्ट |

अनेक LLM प्रदाते `metadata` फील्डद्वारे अतिरिक्त पॅरामीटर्स समर्थन करतात, ज्यात समाविष्ट असू शकतात:

| सामान्य विस्तार पॅरामीटर | वर्णन | सामान्य श्रेणी |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - टोकन्सना टॉप संचित संभाव्यता पर्यंत मर्यादित करते | 0.0 - 1.0 |
| `top_k` | टोकन निवड टॉप K पर्यंत मर्यादित करते | 1 - 100 |
| `presence_penalty` | आतापर्यंत मजकूरात असलेल्या टोकन्सवर दंड लावतो | -2.0 - 2.0 |
| `frequency_penalty` | आतापर्यंत मजकूरात टोकन्सच्या वारंवारतेवर दंड लावतो | -2.0 - 2.0 |
| `seed` | पुनरुत्पादनीय निकालांसाठी विशिष्ट यादृच्छिक बीज | पूर्णांक मूल्य |

## उदाहरण विनंती स्वरूप

खाली MCP मध्ये क्लायंटकडून sampling विनंती करण्याचे उदाहरण आहे:

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

## प्रतिसाद स्वरूप

क्लायंट पूर्णता निकाल परत करतो:

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

MCP sampling मानवी देखरेखीच्या दृष्टीने डिझाइन केलेले आहे:

- **प्रॉम्प्टसाठी**:
  - क्लायंटने वापरकर्त्यांना प्रस्तावित प्रॉम्प्ट दाखवावा
  - वापरकर्ते प्रॉम्प्ट बदलू किंवा नाकारू शकतात
  - सिस्टम प्रॉम्प्ट्स फिल्टर किंवा बदलले जाऊ शकतात
  - संदर्भ समावेश क्लायंटद्वारे नियंत्रित केला जातो

- **पूर्णतांसाठी**:
  - क्लायंटने वापरकर्त्यांना पूर्णता दाखवावी
  - वापरकर्ते पूर्णता बदलू किंवा नाकारू शकतात
  - क्लायंट पूर्णता फिल्टर किंवा बदलू शकतो
  - वापरकर्ते कोणता मॉडेल वापरायचा ते नियंत्रित करतात

या तत्त्वांनुसार, चला वेगवेगळ्या प्रोग्रामिंग भाषांमध्ये sampling कसे अंमलात आणायचे ते पाहू, विशेषतः जे पॅरामीटर्स बहुतेक LLM प्रदात्यांकडून समर्थित आहेत.

## सुरक्षा विचार

MCP मध्ये sampling अंमलात आणताना खालील सुरक्षा सर्वोत्तम पद्धती लक्षात घ्या:

- सर्व संदेश सामग्री क्लायंटकडे पाठवण्यापूर्वी सत्यापित करा
- प्रॉम्प्ट्स आणि पूर्णतांमधून संवेदनशील माहिती स्वच्छ करा
- गैरवापर टाळण्यासाठी दर मर्यादा लागू करा
- sampling वापरातील असामान्य नमुने निरीक्षण करा
- सुरक्षित प्रोटोकॉल वापरून डेटा प्रवासात एन्क्रिप्ट करा
- संबंधित नियमांनुसार वापरकर्त्याचा डेटा गोपनीयता सांभाळा
- अनुपालन आणि सुरक्षा साठी sampling विनंत्यांचे ऑडिट करा
- योग्य मर्यादांसह खर्च नियंत्रण करा
- sampling विनंत्यांसाठी टाइमआउट्स लागू करा
- मॉडेल त्रुटी योग्य प्रकारे हाताळा आणि पर्यायी उपाय वापरा

Sampling पॅरामीटर्स भाषिक मॉडेल्सच्या वर्तनाचे सूक्ष्म समायोजन करण्यास परवानगी देतात, ज्यामुळे निश्चित आणि सर्जनशील आउटपुट यामध्ये संतुलन साधता येते.

चला पाहूया वेगवेगळ्या प्रोग्रामिंग भाषांमध्ये हे पॅरामीटर्स कसे कॉन्फिगर करायचे.

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

वरील कोडमध्ये आपण:

- विशिष्ट सर्व्हर URL सह MCP क्लायंट तयार केला आहे.
- `temperature`, `top_p`, आणि `top_k` सारख्या sampling पॅरामीटर्ससह विनंती कॉन्फिगर केली आहे.
- विनंती पाठवली आणि तयार केलेला मजकूर प्रिंट केला.
- वापरले:
    - `allowedTools` ज्याद्वारे मॉडेलला निर्मिती दरम्यान कोणती साधने वापरायची आहेत ते निर्दिष्ट केले. या प्रकरणात, `ideaGenerator` आणि `marketAnalyzer` साधने वापरून सर्जनशील अॅप कल्पना तयार करण्यात मदत केली.
    - `frequencyPenalty` आणि `presencePenalty` जे आउटपुटमधील पुनरावृत्ती आणि वैविध्य नियंत्रित करतात.
    - `temperature` जे आउटपुटमधील randomness नियंत्रित करते, जिथे जास्त मूल्ये अधिक सर्जनशील प्रतिसादांना प्रोत्साहन देतात.
    - `top_p` जे टोकन निवड टॉप संचित संभाव्यता पर्यंत मर्यादित करते, ज्यामुळे तयार केलेल्या मजकूराची गुणवत्ता वाढते.
    - `top_k` जे मॉडेलला टॉप K सर्वाधिक संभाव्य टोकन्सपर्यंत मर्यादित करते, ज्यामुळे अधिक सुसंगत प्रतिसाद तयार होतात.
    - `frequencyPenalty` आणि `presencePenalty` जे पुनरावृत्ती कमी करतात आणि तयार केलेल्या मजकूरात वैविध्य वाढवतात.

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

वरील कोडमध्ये आपण:

- सर्व्हर URL आणि API कीसह MCP क्लायंट प्रारंभ केला आहे.
- दोन वेगवेगळ्या sampling पॅरामीटर्स सेट कॉन्फिगर केले: एक सर्जनशील कार्यांसाठी आणि दुसरा तथ्यात्मक कार्यांसाठी.
- या कॉन्फिगरेशनसह विनंत्या पाठवल्या, ज्यामुळे मॉडेलला प्रत्येक कार्यासाठी विशिष्ट साधने वापरण्याची परवानगी मिळाली.
- तयार केलेले प्रतिसाद प्रिंट केले जे वेगवेगळ्या sampling पॅरामीटर्सच्या परिणामांचे प्रदर्शन करतात.
- वापरले `allowedTools` ज्याद्वारे मॉडेलला निर्मिती दरम्यान कोणती साधने वापरायची आहेत ते निर्दिष्ट केले. या प्रकरणात, सर्जनशील कार्यांसाठी `ideaGenerator` आणि `environmentalImpactTool`, आणि तथ्यात्मक कार्यांसाठी `factChecker` आणि `dataAnalysisTool` वापरले.
- वापरले `temperature` जे आउटपुटमधील randomness नियंत्रित करते, जिथे जास्त मूल्ये अधिक सर्जनशील प्रतिसादांना प्रोत्साहन देतात.
- वापरले `top_p` जे टोकन निवड टॉप संचित संभाव्यता पर्यंत मर्यादित करते, ज्यामुळे तयार केलेल्या मजकूराची गुणवत्ता वाढते.
- वापरले `frequencyPenalty` आणि `presencePenalty` जे पुनरावृत्ती कमी करतात आणि आउटपुटमध्ये वैविध्य वाढवतात.
- वापरले `top_k` जे मॉडेलला टॉप K सर्वाधिक संभाव्य टोकन्सपर्यंत मर्यादित करते, ज्यामुळे अधिक सुसंगत प्रतिसाद तयार होतात.

---

## Deterministic Sampling

सुसंगत आउटपुट आवश्यक असलेल्या अनुप्रयोगांसाठी, deterministic sampling पुनरुत्पादनीय निकाल सुनिश्चित करते. हे निश्चित यादृच्छिक बीज वापरून आणि temperature शून्यावर सेट करून साध्य होते.

खाली वेगवेगळ्या प्रोग्रामिंग भाषांमध्ये deterministic sampling कसे अंमलात आणायचे याचे उदाहरण दिले आहे.

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

वरील कोडमध्ये आपण:

- निर्दिष्ट सर्व्हर URL सह MCP क्लायंट तयार केला आहे.
- एकाच प्रॉम्प्टसह दोन विनंत्या कॉन्फिगर केल्या, निश्चित बीज आणि शून्य temperature सह.
- दोन्ही विनंत्या पाठवल्या आणि तयार केलेला मजकूर प्रिंट केला.
- दाखवले की प्रतिसाद deterministic sampling कॉन्फिगरेशनमुळे (समान बीज आणि temperature) एकसारखे आहेत.
- `setSeed` वापरून निश्चित यादृच्छिक बीज निर्दिष्ट केले, ज्यामुळे मॉडेल प्रत्येक वेळी समान इनपुटसाठी समान आउटपुट तयार करते.
- `temperature` शून्यावर सेट केले, ज्यामुळे जास्तीत जास्त निश्चितता मिळते, म्हणजे मॉडेल नेहमी सर्वाधिक संभाव्य पुढील टोकन निवडेल.

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

वरील कोडमध्ये आपण:

- सर्व्हर URL सह MCP क्लायंट प्रारंभ केला आहे.
- एकाच प्रॉम्प्टसह दोन विनंत्या कॉन्फिगर केल्या, निश्चित बीज आणि शून्य temperature सह.
- दोन्ही विनंत्या पाठवल्या आणि तयार केलेला मजकूर प्रिंट केला.
- दाखवले की प्रतिसाद deterministic sampling कॉन्फिगरेशनमुळे (समान बीज आणि temperature) एकसारखे आहेत.
- `seed` वापरून निश्चित यादृच्छिक बीज निर्दिष्ट केले, ज्यामुळे मॉडेल प्रत्येक वेळी समान इनपुटसाठी समान आउटपुट तयार करते.
- `temperature` शून्यावर सेट केले, ज्यामुळे जास्तीत जास्त निश्चितता मिळते.
- तिसऱ्या विनंतीसाठी वेगळे बीज वापरले, ज्यामुळे समान प्रॉम्प्ट आणि temperature असूनही वेगळे आउटपुट मिळाले.

---

## Dynamic Sampling Configuration

बुद्धिमान sampling प्रत्येक विनंतीच्या संदर्भ आणि गरजांनुसार पॅरामीटर्स समायोजित करते. याचा अर्थ temperature, top_p, आणि दंड यांसारख्या पॅरामीटर्स कार्यप्रकार, वापरकर्त्याच्या पसंती किंवा ऐतिहासिक कार्यक्षमतेनुसार गतिशीलपणे बदलणे.

खाली वेगवेगळ्या प्रोग्रामिंग भाषांमध्ये dynamic sampling कसे अंमलात आणायचे ते पाहूया.

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

वरील कोडमध्ये आपण:

- `DynamicSamplingService` वर्ग तयार केला जो अनुकूली sampling व्यवस्थापित करतो.
- वेगवेगळ्या कार्यप्रकारांसाठी (सर्जनशील, तथ्यात्मक, कोड, विश्लेषणात्मक) sampling प्रीसेट्स परिभाषित केले.
- कार्यप्रकारानुसार बेस sampling प्रीसेट निवडला.
- वापरकर्त्याच्या पसंतीनुसार, जसे की सर्जनशीलता आणि वैविध्य, sampling पॅरामीटर्स समायोजित केले.
- गतिशीलपणे कॉन्फिगर केलेल्या sampling पॅरामीटर्ससह विनंती पाठवली.
- तयार केलेला मजकूर, sampling पॅरामीटर्स आणि कार्यप्रकार परत केला, ज्यामुळे पारदर्शकता राखली गेली.
- वापरले `temperature` जे आउटपुटमधील randomness नियंत्रित करते, जिथे जास्त मूल्ये अधिक सर्जनशील प्रतिसादांना प्रोत्साहन देतात.
- वापरले `top_p` जे टोकन निवड टॉप संचित संभाव्यता पर्यंत मर्यादित करते, ज्यामुळे तयार केलेल्या मजकूराची गुणवत्ता वाढते.
- वापरले `frequency_penalty` जे पुनरावृत्ती कमी करते आणि वैविध्य वाढवते.
- वापरले `user_preferences` जे वापरकर्त्याद्वारे परिभाषित सर्जनशीलता आणि वैविध्य स्तरांनुसार sampling पॅरामीटर्स सानुकूलित करण्यास परवानगी देते.
- वापरले `task_type` जे विनंतीसाठी योग्य sampling धोरण ठरवते, ज्यामुळे कार्याच्या स्वरूपानुसार अधिक सानुकूल प्रतिसाद मिळतात.
- वापरले `send_request` पद्धत जी कॉन्फिगर केलेल्या sampling पॅरामीटर्ससह प्रॉम्प्ट पाठवते, ज्यामुळे मॉडेल निर्दिष्ट गरजांनुसार मजकूर तयार करते.
- वापरले `generated_text` जे मॉडेलचा प्रतिसाद प्राप्त करते आणि नंतर sampling पॅरामीटर्स आणि कार्यप्रकारासह परत करते.
- वापरले `min` आणि `max` फंक्शन्स जे वापरकर्त्याच्या पसंती वैध श्रेणीत राहतील याची खात्री करतात.

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

वरील कोडमध्ये आपण:

- `AdaptiveSamplingManager` वर्ग तयार केला जो कार्यप्रकार आणि वापरकर्त्याच्या पसंतीनुसार dynamic sampling व्यवस्थापित करतो.
- वेगवेगळ्या कार्यप्रकारांसाठी (सर्जनशील, तथ्यात्मक, कोड, संभाषणात्मक) sampling प्रोफाइल्स परिभाषित केल्या.
- प्रॉम्प्टमधून साध्या heuristic वापरून कार्यप्रकार ओळखण्याची पद्धत अंमलात आणली.
- ओळखलेल्या कार्यप्रकार आणि वापरकर्त्याच्या पसंतीनुसार sampling पॅरामीटर्सची गणना केली.
- ऐतिहासिक कार्यक्षमतेवर आधारित शिकलेल्या समायोजने लागू केली, ज्यामुळे sampling पॅरामीटर्स ऑप्टिमाइझ होतात.
- भविष्यातील समायोजनांसाठी कार्यक्षमता नोंदवली, ज्यामुळे प्रणाली पूर्वीच्या संवादांमधून शिकू शकते.
- गतिशीलपणे कॉन्फिगर केलेल्या sampling पॅरामीटर्ससह विनंत्या पाठवल्या आणि तयार केलेला मजकूर, लागू केलेले पॅरामीटर्स आणि ओळखलेला कार्यप्रकार परत केला.
- वापरले:
    - `userPreferences` जे वापरकर्त्याद्वारे परिभाषित सर्जनशीलता, अचूकता आणि सातत्य स्तरांनुसार sampling पॅरामीटर्स सानुकूलित करण्यास परवानगी देते.
    - `detectTaskType` जे प्रॉम्प्टवरून कार्यप्रकार ठरवते, ज्यामुळे अधिक सानुकूल प्रतिसाद मिळतात.
    - `recordPerformance` जे तयार केलेल्या प्रतिसादांची कार्यक्षमता नोंदवते, ज्यामुळे प्रणाली वेळोवेळी सुधारू शकते.
    - `applyLearnedAdjustments` जे ऐतिहासिक कार्यक्षमतेवर आधारित sampling पॅरामीटर्स बदलते, ज्यामुळे उच्च-गुणवत्तेचे प्रतिसाद तयार होतात.
    - `generateResponse` जे adaptive samplingसह प्रतिसाद तयार करण्याची संपूर्ण प्रक्रिया सुलभ करते, ज्यामुळे वेगवेगळ्या प्रॉम्प्ट्स आणि संदर्भांसाठी सहज कॉल करता येते.
    - `allowedTools` ज्याद्वारे मॉडेलला निर्मिती दरम्यान कोणती साधने वापरायची आहेत ते निर्दिष्ट केले, ज्यामुळे अधिक संदर्भ-जाणकार प्रतिसाद मिळतात.
    - `feedbackScore` जे वापरकर्त्यांना तयार केलेल्या प्रतिसादावर अभिप्राय देण्याची परवानगी देते, ज्याचा वापर मॉडेलच्या कार्यक्षमतेत सुधारणा करण्यासाठी होतो.
    - `performanceHistory` जे मागील संवादांची नोंद ठेवते, ज्यामुळे प्रणाली पूर्वीच्या यशस्वी आणि अपयशी अनुभवांमधून शिकू शकते.
    - `getSamplingParameters

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.