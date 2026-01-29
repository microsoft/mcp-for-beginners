# मोडेल कन्टेक्स्ट प्रोटोकलमा स्याम्पलिङ

स्याम्पलिङ एउटा शक्तिशाली MCP सुविधा हो जसले सर्भरहरूलाई क्लाइन्टमार्फत LLM कम्प्लीसनहरू अनुरोध गर्न अनुमति दिन्छ, जसले जटिल एजेन्टिक व्यवहारहरू सक्षम पार्छ र सुरक्षा तथा गोपनीयता कायम राख्छ। सही स्याम्पलिङ कन्फिगरेसनले प्रतिक्रिया गुणस्तर र प्रदर्शनमा उल्लेखनीय सुधार ल्याउन सक्छ। MCP ले मोडेलहरूले कसरी टेक्स्ट उत्पादन गर्ने भन्ने कुरामा नियन्त्रण गर्न मानकीकृत तरिका प्रदान गर्छ, जसले र्यान्डमनेस, सिर्जनात्मकता, र सुसंगततामा प्रभाव पार्ने विशेष प्यारामिटरहरू समावेश गर्छ।

## परिचय

यस पाठमा, हामी MCP अनुरोधहरूमा स्याम्पलिङ प्यारामिटरहरू कसरी कन्फिगर गर्ने र स्याम्पलिङको आधारभूत प्रोटोकल म्याकानिक्स बुझ्नेछौं।

## सिकाइका उद्देश्यहरू

यस पाठको अन्त्यसम्म, तपाईं सक्षम हुनुहुनेछ:

- MCP मा उपलब्ध मुख्य स्याम्पलिङ प्यारामिटरहरू बुझ्न।
- विभिन्न प्रयोगका लागि स्याम्पलिङ प्यारामिटरहरू कन्फिगर गर्न।
- पुनरुत्पादनयोग्य नतिजाका लागि निर्धारक स्याम्पलिङ लागू गर्न।
- सन्दर्भ र प्रयोगकर्ता प्राथमिकताहरूको आधारमा स्याम्पलिङ प्यारामिटरहरू गतिशील रूपमा समायोजन गर्न।
- विभिन्न परिदृश्यहरूमा मोडेल प्रदर्शन सुधार गर्न स्याम्पलिङ रणनीतिहरू लागू गर्न।
- MCP को क्लाइन्ट-सर्भर प्रवाहमा स्याम्पलिङ कसरी काम गर्छ बुझ्न।

## MCP मा स्याम्पलिङ कसरी काम गर्छ

MCP मा स्याम्पलिङ प्रवाह यी चरणहरू पालना गर्छ:

1. सर्भरले क्लाइन्टलाई `sampling/createMessage` अनुरोध पठाउँछ
2. क्लाइन्टले अनुरोध समीक्षा गर्छ र आवश्यक परिमार्जन गर्न सक्छ
3. क्लाइन्टले LLM बाट स्याम्पल गर्छ
4. क्लाइन्टले कम्प्लीसन समीक्षा गर्छ
5. क्लाइन्टले नतिजा सर्भरलाई फर्काउँछ

यो मानव-इन-द-लूप डिजाइनले प्रयोगकर्ताहरूलाई LLM ले के देख्छ र उत्पादन गर्छ भन्नेमा नियन्त्रण कायम राख्न सुनिश्चित गर्छ।

## स्याम्पलिङ प्यारामिटरहरूको अवलोकन

MCP ले क्लाइन्ट अनुरोधहरूमा कन्फिगर गर्न सकिने निम्न स्याम्पलिङ प्यारामिटरहरू परिभाषित गर्छ:

| प्यारामिटर | विवरण | सामान्य दायरा |
|------------|---------|---------------|
| `temperature` | टोकन चयनमा र्यान्डमनेस नियन्त्रण गर्छ | 0.0 - 1.0 |
| `maxTokens` | उत्पादन गर्न सकिने अधिकतम टोकन संख्या | पूर्णांक मान |
| `stopSequences` | उत्पादन रोक्ने कस्टम अनुक्रमहरू | स्ट्रिङहरूको एरे |
| `metadata` | थप प्रदायक-विशिष्ट प्यारामिटरहरू | JSON वस्तु |

धेरै LLM प्रदायकहरूले `metadata` फिल्डमार्फत थप प्यारामिटरहरू समर्थन गर्छन्, जसमा समावेश हुन सक्छ:

| सामान्य विस्तार प्यारामिटर | विवरण | सामान्य दायरा |
|--------------------------|---------|---------------|
| `top_p` | न्युक्लियस स्याम्पलिङ - टोकनहरूलाई शीर्ष संचयी सम्भावनामा सीमित गर्छ | 0.0 - 1.0 |
| `top_k` | टोकन चयनलाई शीर्ष K विकल्पहरूमा सीमित गर्छ | 1 - 100 |
| `presence_penalty` | हालसम्मको टेक्स्टमा टोकनको उपस्थितिको आधारमा दण्ड लगाउँछ | -2.0 - 2.0 |
| `frequency_penalty` | हालसम्मको टेक्स्टमा टोकनको आवृत्तिको आधारमा दण्ड लगाउँछ | -2.0 - 2.0 |
| `seed` | पुनरुत्पादनयोग्य नतिजाका लागि निश्चित र्यान्डम सिड | पूर्णांक मान |

## अनुरोध ढाँचा उदाहरण

यहाँ MCP मा क्लाइन्टबाट स्याम्पलिङ अनुरोध गर्ने उदाहरण छ:

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

## प्रतिक्रिया ढाँचा

क्लाइन्टले कम्प्लीसन नतिजा फर्काउँछ:

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

## मानव-इन-द-लूप नियन्त्रणहरू

MCP स्याम्पलिङ मानव निरीक्षणलाई ध्यानमा राखेर डिजाइन गरिएको छ:

- **प्रम्प्टहरूको लागि**:
  - क्लाइन्टहरूले प्रयोगकर्तालाई प्रस्तावित प्रम्प्ट देखाउनुपर्छ
  - प्रयोगकर्ताले प्रम्प्टहरू परिमार्जन वा अस्वीकृत गर्न सक्नुपर्छ
  - सिस्टम प्रम्प्टहरू फिल्टर वा परिमार्जन गर्न सकिन्छ
  - सन्दर्भ समावेशीकरण क्लाइन्टले नियन्त्रण गर्छ

- **कम्प्लीसनहरूको लागि**:
  - क्लाइन्टहरूले प्रयोगकर्तालाई कम्प्लीसन देखाउनुपर्छ
  - प्रयोगकर्ताले कम्प्लीसनहरू परिमार्जन वा अस्वीकृत गर्न सक्नुपर्छ
  - क्लाइन्टहरूले कम्प्लीसनहरू फिल्टर वा परिमार्जन गर्न सक्छन्
  - प्रयोगकर्ताले कुन मोडेल प्रयोग गर्ने नियन्त्रण गर्छन्

यी सिद्धान्तहरूलाई ध्यानमा राख्दै, विभिन्न प्रोग्रामिङ भाषाहरूमा स्याम्पलिङ कसरी लागू गर्ने र LLM प्रदायकहरूमा सामान्य रूपमा समर्थित प्यारामिटरहरूमा केन्द्रित भएर हेरौं।

## सुरक्षा सम्बन्धी विचारहरू

MCP मा स्याम्पलिङ लागू गर्दा यी सुरक्षा उत्तम अभ्यासहरू विचार गर्नुहोस्:

- **सबै सन्देश सामग्री प्रमाणीकरण गर्नुहोस्** क्लाइन्टलाई पठाउनु अघि
- **प्रम्प्ट र कम्प्लीसनबाट संवेदनशील जानकारी सफा गर्नुहोस्**
- **दुरुपयोग रोक्न दर सीमा लागू गर्नुहोस्**
- **असामान्य ढाँचाहरूको लागि स्याम्पलिङ प्रयोग निगरानी गर्नुहोस्**
- **सुरक्षित प्रोटोकल प्रयोग गरी डाटा ट्रान्जिटमा इन्क्रिप्ट गर्नुहोस्**
- **प्रयोगकर्ता डाटा गोपनीयता सम्बन्धी नियमहरू पालना गर्नुहोस्**
- **अनुपालन र सुरक्षा लागि स्याम्पलिङ अनुरोधहरूको अडिट गर्नुहोस्**
- **लागत नियन्त्रणका लागि उपयुक्त सीमा राख्नुहोस्**
- **स्याम्पलिङ अनुरोधहरूको लागि टाइमआउट लागू गर्नुहोस्**
- **मोडेल त्रुटिहरूलाई उपयुक्त फलब्याकसहित सहज रूपमा व्यवस्थापन गर्नुहोस्**

स्याम्पलिङ प्यारामिटरहरूले भाषा मोडेलहरूको व्यवहारलाई सूक्ष्म रूपमा समायोजन गर्न अनुमति दिन्छ, जसले निर्धारक र सिर्जनात्मक आउटपुटबीचको सन्तुलन प्राप्त गर्न मद्दत गर्छ।

अब विभिन्न प्रोग्रामिङ भाषाहरूमा यी प्यारामिटरहरू कसरी कन्फिगर गर्ने हेरौं।

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

अघिल्लो कोडमा हामीले:

- विशिष्ट सर्भर URL सहित MCP क्लाइन्ट सिर्जना गर्यौं।
- `temperature`, `top_p`, र `top_k` जस्ता स्याम्पलिङ प्यारामिटरहरूसहित अनुरोध कन्फिगर गर्यौं।
- अनुरोध पठायौं र उत्पन्न टेक्स्ट प्रिन्ट गर्यौं।
- प्रयोग गर्यौं:
    - `allowedTools` जसले मोडेललाई उत्पादनको क्रममा कुन उपकरणहरू प्रयोग गर्न सकिन्छ भनेर निर्दिष्ट गर्छ। यस अवस्थामा, हामीले `ideaGenerator` र `marketAnalyzer` उपकरणहरूलाई सिर्जनात्मक एप आइडिया उत्पादनमा सहयोग गर्न अनुमति दियौं।
    - `frequencyPenalty` र `presencePenalty` जसले आउटपुटमा दोहोरिने र विविधता नियन्त्रण गर्छ।
    - `temperature` जसले आउटपुटको र्यान्डमनेस नियन्त्रण गर्छ, उच्च मानले बढी सिर्जनात्मक प्रतिक्रिया ल्याउँछ।
    - `top_p` जसले टोकन चयनलाई शीर्ष संचयी सम्भावनामा सीमित गरेर उत्पन्न टेक्स्टको गुणस्तर सुधार्छ।
    - `top_k` जसले मोडेललाई शीर्ष K सम्भावित टोकनहरूमा सीमित गर्छ, जसले बढी सुसंगत प्रतिक्रिया उत्पादनमा मद्दत गर्छ।
    - `frequencyPenalty` र `presencePenalty` लाई दोहोरिने कम गर्न र विविधता बढाउन प्रयोग गरियो।

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

अघिल्लो कोडमा हामीले:

- सर्भर URL र API कुञ्जीसहित MCP क्लाइन्ट सुरु गर्यौं।
- दुई सेट स्याम्पलिङ प्यारामिटरहरू कन्फिगर गर्यौं: एउटा सिर्जनात्मक कार्यका लागि र अर्को तथ्यात्मक कार्यका लागि।
- यी कन्फिगरेसनहरूसहित अनुरोधहरू पठायौं, मोडेललाई प्रत्येक कार्यका लागि विशिष्ट उपकरणहरू प्रयोग गर्न अनुमति दिँदै।
- उत्पन्न प्रतिक्रियाहरू प्रिन्ट गर्यौं जसले विभिन्न स्याम्पलिङ प्यारामिटरहरूको प्रभाव देखाउँछ।
- प्रयोग गर्यौं `allowedTools` जसले मोडेललाई उत्पादनको क्रममा कुन उपकरणहरू प्रयोग गर्न सकिन्छ भनेर निर्दिष्ट गर्छ। यस अवस्थामा, सिर्जनात्मक कार्यका लागि `ideaGenerator` र `environmentalImpactTool`, र तथ्यात्मक कार्यका लागि `factChecker` र `dataAnalysisTool` लाई अनुमति दियौं।
- प्रयोग गर्यौं `temperature` जसले आउटपुटको र्यान्डमनेस नियन्त्रण गर्छ, उच्च मानले बढी सिर्जनात्मक प्रतिक्रिया ल्याउँछ।
- प्रयोग गर्यौं `top_p` जसले टोकन चयनलाई शीर्ष संचयी सम्भावनामा सीमित गरेर उत्पन्न टेक्स्टको गुणस्तर सुधार्छ।
- प्रयोग गर्यौं `frequencyPenalty` र `presencePenalty` जसले दोहोरिने कम गर्न र विविधता बढाउन मद्दत गर्छ।
- प्रयोग गर्यौं `top_k` जसले मोडेललाई शीर्ष K सम्भावित टोकनहरूमा सीमित गर्छ, जसले बढी सुसंगत प्रतिक्रिया उत्पादनमा मद्दत गर्छ।

---

## निर्धारक स्याम्पलिङ

लगातार नतिजा आवश्यक पर्ने अनुप्रयोगहरूको लागि, निर्धारक स्याम्पलिङले पुनरुत्पादनयोग्य नतिजा सुनिश्चित गर्छ। यसले निश्चित र्यान्डम सिड प्रयोग गरेर र तापक्रमलाई शून्यमा सेट गरेर यो गर्छ।

विभिन्न प्रोग्रामिङ भाषाहरूमा निर्धारक स्याम्पलिङ प्रदर्शन गर्न तलको नमूना कार्यान्वयन हेरौं।

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

अघिल्लो कोडमा हामीले:

- निर्दिष्ट सर्भर URL सहित MCP क्लाइन्ट सिर्जना गर्यौं।
- एउटै प्रम्प्ट, निश्चित सिड, र शून्य तापक्रम सहित दुई अनुरोधहरू कन्फिगर गर्यौं।
- दुवै अनुरोधहरू पठायौं र उत्पन्न टेक्स्ट प्रिन्ट गर्यौं।
- देखायौं कि प्रतिक्रिया निर्धारक स्याम्पलिङ कन्फिगरेसन (उही सिड र तापक्रम) को कारण समान छन्।
- `setSeed` प्रयोग गर्यौं जसले निश्चित र्यान्डम सिड निर्दिष्ट गर्छ, जसले मोडेललाई हरेक पटक एउटै इनपुटका लागि एउटै आउटपुट उत्पादन गर्न सुनिश्चित गर्छ।
- `temperature` लाई शून्यमा सेट गर्यौं जसले अधिकतम निर्धारकता सुनिश्चित गर्छ, अर्थात् मोडेलले सधैं सबैभन्दा सम्भावित अर्को टोकन चयन गर्छ र र्यान्डमनेस हुँदैन।

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

अघिल्लो कोडमा हामीले:

- सर्भर URL सहित MCP क्लाइन्ट सुरु गर्यौं।
- एउटै प्रम्प्ट, निश्चित सिड, र शून्य तापक्रम सहित दुई अनुरोधहरू कन्फिगर गर्यौं।
- दुवै अनुरोधहरू पठायौं र उत्पन्न टेक्स्ट प्रिन्ट गर्यौं।
- देखायौं कि प्रतिक्रिया निर्धारक स्याम्पलिङ कन्फिगरेसन (उही सिड र तापक्रम) को कारण समान छन्।
- `seed` प्रयोग गर्यौं जसले निश्चित र्यान्डम सिड निर्दिष्ट गर्छ, जसले मोडेललाई हरेक पटक एउटै इनपुटका लागि एउटै आउटपुट उत्पादन गर्न सुनिश्चित गर्छ।
- `temperature` लाई शून्यमा सेट गर्यौं जसले अधिकतम निर्धारकता सुनिश्चित गर्छ, अर्थात् मोडेलले सधैं सबैभन्दा सम्भावित अर्को टोकन चयन गर्छ र र्यान्डमनेस हुँदैन।
- तेस्रो अनुरोधका लागि फरक सिड प्रयोग गर्यौं जसले देखाउँछ कि सिड परिवर्तन गर्दा एउटै प्रम्प्ट र तापक्रम भए पनि फरक आउटपुट आउँछ।

---

## गतिशील स्याम्पलिङ कन्फिगरेसन

बुद्धिमानी स्याम्पलिङले प्रत्येक अनुरोधको सन्दर्भ र आवश्यकताका आधारमा प्यारामिटरहरू अनुकूलन गर्छ। यसको अर्थ तापक्रम, top_p, र दण्डहरू जस्ता प्यारामिटरहरू कार्यको प्रकार, प्रयोगकर्ता प्राथमिकता, वा ऐतिहासिक प्रदर्शनको आधारमा गतिशील रूपमा समायोजन गर्नु हो।

विभिन्न प्रोग्रामिङ भाषाहरूमा गतिशील स्याम्पलिङ कसरी लागू गर्ने हेरौं।

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

अघिल्लो कोडमा हामीले:

- `DynamicSamplingService` क्लास सिर्जना गर्यौं जसले अनुकूली स्याम्पलिङ व्यवस्थापन गर्छ।
- विभिन्न कार्य प्रकारहरू (सिर्जनात्मक, तथ्यात्मक, कोड, विश्लेषणात्मक) का लागि स्याम्पलिङ प्रिसेटहरू परिभाषित गर्यौं।
- कार्य प्रकारको आधारमा आधारभूत स्याम्पलिङ प्रिसेट चयन गर्यौं।
- प्रयोगकर्ता प्राथमिकताहरू जस्तै सिर्जनात्मकता स्तर र विविधताको आधारमा स्याम्पलिङ प्यारामिटरहरू समायोजन गर्यौं।
- कन्फिगर गरिएका स्याम्पलिङ प्यारामिटरहरूसहित अनुरोध पठायौं।
- उत्पन्न टेक्स्ट स्याम्पलिङ प्यारामिटरहरू र कार्य प्रकारसँगै पारदर्शिताका लागि फर्कायौं।
- प्रयोग गर्यौं `temperature` जसले आउटपुटको र्यान्डमनेस नियन्त्रण गर्छ, उच्च मानले बढी सिर्जनात्मक प्रतिक्रिया ल्याउँछ।
- प्रयोग गर्यौं `top_p` जसले टोकन चयनलाई शीर्ष संचयी सम्भावनामा सीमित गरेर उत्पन्न टेक्स्टको गुणस्तर सुधार्छ।
- प्रयोग गर्यौं `frequency_penalty` जसले दोहोरिने कम गर्न र विविधता बढाउन मद्दत गर्छ।
- प्रयोग गर्यौं `user_preferences` जसले प्रयोगकर्ताद्वारा परिभाषित सिर्जनात्मकता र विविधता स्तरका आधारमा स्याम्पलिङ प्यारामिटरहरू अनुकूलन गर्न अनुमति दिन्छ।
- प्रयोग गर्यौं `task_type` जसले अनुरोधको प्रकृतिको आधारमा उपयुक्त स्याम्पलिङ रणनीति निर्धारण गर्छ, जसले बढी लक्षित प्रतिक्रिया दिन्छ।
- प्रयोग गर्यौं `send_request` विधि जसले कन्फिगर गरिएका स्याम्पलिङ प्यारामिटरहरूसहित प्रम्प्ट पठाउँछ, सुनिश्चित गर्दै मोडेलले निर्दिष्ट आवश्यकताअनुसार टेक्स्ट उत्पादन गर्छ।
- प्रयोग गर्यौं `generated_text` जसले मोडेलको प्रतिक्रिया प्राप्त गर्छ, जुन पछि स्याम्पलिङ प्यारामिटरहरू र कार्य प्रकारसँगै विश्लेषण वा प्रदर्शनका लागि फर्काइन्छ।
- प्रयोग गर्यौं `min` र `max` कार्यहरू जसले प्रयोगकर्ता प्राथमिकताहरूलाई मान्य दायरामा सीमित गर्छ, अवैध स्याम्पलिङ कन्फिगरेसन रोक्न।

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

अघिल्लो कोडमा हामीले:

- `AdaptiveSamplingManager` क्लास सिर्जना गर्यौं जसले कार्य प्रकार र प्रयोगकर्ता प्राथमिकताका आधारमा गतिशील स्याम्पलिङ व्यवस्थापन गर्छ।
- विभिन्न कार्य प्रकारहरू (सिर्जनात्मक, तथ्यात्मक, कोड, संवादात्मक) का लागि स्याम्पलिङ प्रोफाइलहरू परिभाषित गर्यौं।
- सरल ह्युरिस्टिक्स प्रयोग गरी प्रम्प्टबाट कार्य प्रकार पत्ता लगाउने विधि लागू गर्यौं।
- पत्ता लगाइएको कार्य प्रकार र प्रयोगकर्ता प्राथमिकताका आधारमा स्याम्पलिङ प्यारामिटरहरू गणना गर्यौं।
- ऐतिहासिक प्रदर्शनमा आधारित सिकाइएका समायोजनहरू लागू गरेर स्याम्पलिङ प्यारामिटरहरू अनुकूलन गर्यौं।
- भविष्यका समायोजनहरूको लागि प्रदर्शन रेकर्ड गर्यौं, जसले प्रणालीलाई विगतका अन्तरक्रियाबाट सिक्न अनुमति दिन्छ।
- गतिशील रूपमा कन्फिगर गरिएका स्याम्पलिङ प्यारामिटरहरूसहित अनुरोधहरू पठायौं र लागू प्यारामिटरहरू र पत्ता लगाइएको कार्य प्रकारसँगै उत्पन्न टेक्स्ट फर्कायौं।
- प्रयोग गर्यौं:
    - `userPreferences` जसले प्रयोगकर्ताद्वारा परिभाषित सिर्जनात्मकता, सटीकता, र स्थिरता स्तरका आधारमा स्याम्पलिङ प्यारामिटरहरू अनुकूलन गर्न अनुमति दिन्छ।
    - `detectTaskType` जसले प्रम्प्टको आधारमा कार्यको प्रकृति निर्धारण गर्छ, जसले विभिन्न प्रकारका अनुरोधहरूका लागि उपयुक्त स्याम्पलिङ रणनीतिहरू लागू गर्न सक्षम बनाउँछ।
    - `recordPerformance` जसले उत्पन्न प्रतिक्रियाको प्रदर्शन लग गर्छ, जसले प्रणालीलाई समयसँगै अनुकूलन र सुधार गर्न मद्दत गर्छ।
    - `applyLearnedAdjustments` जसले ऐतिहासिक प्रदर्शनको आधारमा स्याम्पलिङ प्यारामिटरहरू परिमार्जन गर्छ, जसले मोडेललाई उच्च गुणस्तरको प्रतिक्रिया उत्पादन गर्न सक्षम बनाउँछ।
    - `generateResponse` जसले अनुकूली स्याम्पलिङसहित प्रतिक्रिया उत्पादन गर्ने सम्पूर्ण प्रक्रियालाई समेट्छ, जसले विभिन्न प्रम्प्ट र सन्दर्भहरूसँग सजिलै कल गर्न सकिन्छ।
    - `allowedTools` जसले मोडेललाई उत्पादनको क्रममा कुन

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।