# மாடல் சூழல் நெறிமுறை (MCP) இல் மாதிரியாக்கல்

மாதிரியாக்கல் என்பது MCP இன் ஒரு சக்திவாய்ந்த அம்சமாகும், இது சேவையகங்களுக்கு LLM முடிவுகளை வாடிக்கையாளர்களின் மூலம் கோர அனுமதிக்கிறது. இது பாதுகாப்பு மற்றும் தனியுரிமையை பராமரிக்கும்போது நுண்ணிய செயற்கை நுண்ணறிவு செயல்பாடுகளை செயல்படுத்த உதவுகிறது. சரியான மாதிரியாக்கல் அமைப்புகள் பதில்களின் தரத்தையும் செயல்திறனையும் கணிசமாக மேம்படுத்த முடியும். MCP, குறிப்பிட்ட அளவீடுகளின் மூலம் உரை உருவாக்கத்தை கட்டுப்படுத்த ஒரு நிலையான வழியை வழங்குகிறது, இது சீரற்ற தன்மை, படைப்பாற்றல் மற்றும் ஒழுங்கை பாதிக்கிறது.

## அறிமுகம்

இந்த பாடத்தில், MCP கோரிக்கைகளில் மாதிரியாக்கல் அளவீடுகளை எப்படி அமைப்பது மற்றும் மாதிரியாக்கலின் அடிப்படை நெறிமுறை இயங்குதளங்களை புரிந்து கொள்வது என்பதை ஆராய்வோம்.

## கற்றல் இலக்குகள்

இந்த பாடத்தின் முடிவில், நீங்கள்:

- MCP இல் உள்ள முக்கியமான மாதிரியாக்கல் அளவீடுகளை புரிந்து கொள்ளலாம்.
- வெவ்வேறு பயன்பாடுகளுக்காக மாதிரியாக்கல் அளவீடுகளை அமைக்கலாம்.
- மீண்டும் உருவாக்கக்கூடிய முடிவுகளுக்காக நிர்ணயமான மாதிரியாக்கலை செயல்படுத்தலாம்.
- சூழல் மற்றும் பயனர் விருப்பங்களின் அடிப்படையில் மாதிரியாக்கல் அளவீடுகளை மாறுபடச் செய்யலாம்.
- மாடல் செயல்திறனை மேம்படுத்த மாதிரியாக்கல் உத்திகளை பயன்படுத்தலாம்.
- MCP இன் வாடிக்கையாளர்-சேவையக ஓட்டத்தில் மாதிரியாக்கல் எப்படி செயல்படுகிறது என்பதை புரிந்து கொள்ளலாம்.

## MCP இல் மாதிரியாக்கல் எப்படி செயல்படுகிறது

MCP இல் மாதிரியாக்கல் ஓட்டம் பின்வரும் படிகளை பின்பற்றுகிறது:

1. சேவையகம் `sampling/createMessage` கோரிக்கையை வாடிக்கையாளருக்கு அனுப்புகிறது.
2. வாடிக்கையாளர் கோரிக்கையை மதிப்பீடு செய்து மாற்றலாம்.
3. வாடிக்கையாளர் LLM இல் இருந்து மாதிரியாக்குகிறது.
4. வாடிக்கையாளர் முடிவுகளை மதிப்பீடு செய்கிறது.
5. வாடிக்கையாளர் முடிவுகளை சேவையகத்திற்கு திருப்பி அனுப்புகிறது.

இந்த மனிதன்-உள்ளே-சுழற்சி வடிவமைப்பு, LLM என்ன பார்க்கிறது மற்றும் உருவாக்குகிறது என்பதைப் பற்றிய கட்டுப்பாட்டை பயனர்களுக்கு வழங்குகிறது.

## மாதிரியாக்கல் அளவீடுகளின் மேற்பார்வை

MCP, வாடிக்கையாளர் கோரிக்கைகளில் அமைக்கக்கூடிய பின்வரும் மாதிரியாக்கல் அளவீடுகளை வரையறுக்கிறது:

| அளவீடு | விளக்கம் | வழக்கமான வரம்பு |
|-----------|-------------|---------------|
| `temperature` | டோக்கன் தேர்வில் சீரற்ற தன்மையை கட்டுப்படுத்துகிறது | 0.0 - 1.0 |
| `maxTokens` | உருவாக்கக்கூடிய அதிகபட்ச டோக்கன்களின் எண்ணிக்கை | முழு எண் |
| `stopSequences` | சந்திக்கும் போது உருவாக்கத்தை நிறுத்தும் தனிப்பயன் வரிசைகள் | சரங்கள் வரிசை |
| `metadata` | கூடுதல் வழங்குநர்-குறிப்பிட்ட அளவீடுகள் | JSON பொருள் |

பல LLM வழங்குநர்கள் `metadata` புலத்தின் மூலம் கூடுதல் அளவீடுகளை ஆதரிக்கின்றனர், இதில் அடங்கும்:

| பொதுவான நீட்டிப்பு அளவீடு | விளக்கம் | வழக்கமான வரம்பு |
|-----------|-------------|---------------|
| `top_p` | நியூக்ளியஸ் மாதிரியாக்கல் - டோக்கன்களை மேல் மொத்த சாத்தியமான அளவுக்கு வரையறுக்கிறது | 0.0 - 1.0 |
| `top_k` | டோக்கன் தேர்வை மேல் K விருப்பங்களுக்கு வரையறுக்கிறது | 1 - 100 |
| `presence_penalty` | உரையில் இதுவரை உள்ள டோக்கன்களின் அடிப்படையில் தண்டனை அளிக்கிறது | -2.0 - 2.0 |
| `frequency_penalty` | இதுவரை உள்ள டோக்கன்களின் அடிப்படையில் தண்டனை அளிக்கிறது | -2.0 - 2.0 |
| `seed` | மீண்டும் உருவாக்கக்கூடிய முடிவுகளுக்கான குறிப்பிட்ட சீரற்ற விதை | முழு எண் |

## கோரிக்கை வடிவமைப்பு எடுத்துக்காட்டு

MCP இல் வாடிக்கையாளரிடமிருந்து மாதிரியாக்கலை கோருவதற்கான எடுத்துக்காட்டு:

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


## பதில் வடிவமைப்பு

வாடிக்கையாளர் முடிவுகளை திருப்பி அனுப்புகிறது:

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


## மனிதன்-உள்ளே-சுழற்சி கட்டுப்பாடுகள்

MCP மாதிரியாக்கல் மனித மேற்பார்வையுடன் வடிவமைக்கப்பட்டுள்ளது:

- **தூண்டுதல்களுக்கு**:
  - வாடிக்கையாளர்கள் பயனர்களுக்கு முன்மொழியப்பட்ட தூண்டுதலைக் காட்ட வேண்டும்.
  - பயனர்கள் தூண்டுதல்களை மாற்றவோ நிராகரிக்கவோ முடியும்.
  - அமைப்பு தூண்டுதல்களை வடிகட்டவோ மாற்றவோ முடியும்.
  - சூழல் சேர்க்கை வாடிக்கையாளர் மூலம் கட்டுப்படுத்தப்படுகிறது.

- **முடிவுகளுக்கு**:
  - வாடிக்கையாளர்கள் பயனர்களுக்கு முடிவுகளை காட்ட வேண்டும்.
  - பயனர்கள் முடிவுகளை மாற்றவோ நிராகரிக்கவோ முடியும்.
  - வாடிக்கையாளர்கள் முடிவுகளை வடிகட்டவோ மாற்றவோ முடியும்.
  - எந்த மாடல் பயன்படுத்தப்பட வேண்டும் என்பதை பயனர்கள் கட்டுப்படுத்துகிறார்கள்.

இந்தக் கொள்கைகளை மனதில் கொண்டு, வெவ்வேறு நிரலாக்க மொழிகளில் மாதிரியாக்கலை எப்படி செயல்படுத்துவது என்பதைப் பார்ப்போம், LLM வழங்குநர்களுக்கு பொதுவாக ஆதரிக்கப்படும் அளவீடுகளின் மீது கவனம் செலுத்தி.

## பாதுகாப்பு கருத்துக்கள்

MCP இல் மாதிரியாக்கலை செயல்படுத்தும்போது, பின்வரும் பாதுகாப்பு சிறந்த நடைமுறைகளை கருத்தில் கொள்ளுங்கள்:

- **அனைத்து செய்தி உள்ளடக்கத்தையும் சரிபார்க்கவும்** அதை வாடிக்கையாளருக்கு அனுப்புவதற்கு முன்.
- **தனியுரிமை தகவல்களை தூண்டுதல்களிலிருந்து மற்றும் முடிவுகளிலிருந்து சுத்திகரிக்கவும்.**
- **தவறாக பயன்படுத்துவதைத் தடுக்க** வீத வரம்புகளை செயல்படுத்தவும்.
- **மாதிரியாக்கல் பயன்பாட்டை கண்காணிக்கவும்** சந்தேகத்திற்கிடமான முறைமைகளுக்கு.
- **பாதுகாப்பான நெறிமுறைகளைப் பயன்படுத்தி** தரவுகளை பரிமாற்றத்தில் குறியாக்கவும்.
- **பயனர் தரவுகளின் தனியுரிமையை** தொடர்புடைய விதிமுறைகளுக்கு ஏற்ப கையாளவும்.
- **மாதிரியாக்கல் கோரிக்கைகளை தணிக்கவும்** இணக்கம் மற்றும் பாதுகாப்புக்காக.
- **செலவுக் கட்டுப்பாட்டை** சரியான வரம்புகளுடன் நிர்வகிக்கவும்.
- **மாதிரியாக்கல் கோரிக்கைகளுக்கு நேர வரம்புகளை** செயல்படுத்தவும்.
- **மாடல் பிழைகளை நன்கு கையாளவும்** சரியான மாற்று வழிகளுடன்.

மாதிரியாக்கல் அளவீடுகள், நிர்ணயமான மற்றும் படைப்பாற்றல் விளைவுகளுக்கு இடையில் தேவையான சமநிலையை அடைய மொழி மாடல்களின் நடத்தை fine-tune செய்ய அனுமதிக்கின்றன.

இப்போது இந்த அளவீடுகளை வெவ்வேறு நிரலாக்க மொழிகளில் எப்படி அமைப்பது என்பதைப் பார்ப்போம்.

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


மேலே உள்ள குறியீட்டில், நாங்கள்:

- குறிப்பிட்ட சேவையக URL உடன் MCP வாடிக்கையாளரை உருவாக்கியுள்ளோம்.
- `temperature`, `top_p`, மற்றும் `top_k` போன்ற மாதிரியாக்கல் அளவீடுகளுடன் கோரிக்கையை அமைத்துள்ளோம்.
- கோரிக்கையை அனுப்பி உருவாக்கப்பட்ட உரையை அச்சிட்டுள்ளோம்.
- பயன்படுத்தியுள்ளோம்:
    - `allowedTools` உருவாக்கத்தின் போது மாடல் பயன்படுத்தக்கூடிய கருவிகளை குறிப்பிட. இங்கு, படைப்பாற்றலான செயல்பாடுகளுக்கு உதவ `ideaGenerator` மற்றும் `marketAnalyzer` கருவிகளை அனுமதித்துள்ளோம்.
    - `frequencyPenalty` மற்றும் `presencePenalty` மூலம் மீண்டும் மீண்டும் தோன்றுவதை கட்டுப்படுத்தவும், பல்வகைமையை ஊக்குவிக்கவும்.
    - `temperature` மூலம் சீரற்ற தன்மையை கட்டுப்படுத்தவும், அதிக மதிப்புகள் படைப்பாற்றலான பதில்களுக்கு வழிவகுக்கும்.
    - `top_p` மூலம் மேல் மொத்த சாத்தியமான அளவுக்கு டோக்கன்களை வரையறுக்கவும், உருவாக்கப்பட்ட உரையின் தரத்தை மேம்படுத்தவும்.
    - `top_k` மூலம் மேல் K மிகவும் சாத்தியமான டோக்கன்களுக்கு மாடலை வரையறுக்கவும், மேலும் ஒழுங்கான பதில்களை உருவாக்க உதவும்.

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


மேலே உள்ள குறியீட்டில், நாங்கள்:

- சேவையக URL மற்றும் API விசையுடன் MCP வாடிக்கையாளரை தொடங்கியுள்ளோம்.
- படைப்பாற்றல் பணிகளுக்கும் உண்மையான பணிகளுக்கும் இரண்டு மாதிரியாக்கல் அளவீடுகளை அமைத்துள்ளோம்.
- இந்த அமைப்புகளுடன் கோரிக்கைகளை அனுப்பி, ஒவ்வொரு பணிக்கும் குறிப்பிட்ட கருவிகளை மாடல் பயன்படுத்த அனுமதித்துள்ளோம்.
- உருவாக்கப்பட்ட பதில்களை அச்சிட்டு, வெவ்வேறு மாதிரியாக்கல் அளவீடுகளின் விளைவுகளை விளக்கியுள்ளோம்.
- பயன்படுத்தியுள்ளோம்:
    - `allowedTools` உருவாக்கத்தின் போது மாடல் பயன்படுத்தக்கூடிய கருவிகளை குறிப்பிட. இங்கு, படைப்பாற்றல் பணிகளுக்கு `ideaGenerator` மற்றும் `environmentalImpactTool` கருவிகளை அனுமதித்துள்ளோம், உண்மையான பணிகளுக்கு `factChecker` மற்றும் `dataAnalysisTool` கருவிகளை அனுமதித்துள்ளோம்.
    - `temperature` மூலம் சீரற்ற தன்மையை கட்டுப்படுத்தவும், அதிக மதிப்புகள் படைப்பாற்றலான பதில்களுக்கு வழிவகுக்கும்.
    - `top_p` மூலம் மேல் மொத்த சாத்தியமான அளவுக்கு டோக்கன்களை வரையறுக்கவும், உருவாக்கப்பட்ட உரையின் தரத்தை மேம்படுத்தவும்.
    - `frequencyPenalty` மற்றும் `presencePenalty` மூலம் மீண்டும் மீண்டும் தோன்றுவதை கட்டுப்படுத்தவும், பல்வகைமையை ஊக்குவிக்கவும்.
    - `top_k` மூலம் மேல் K மிகவும் சாத்தியமான டோக்கன்களுக்கு மாடலை வரையறுக்கவும், மேலும் ஒழுங்கான பதில்களை உருவாக்க உதவும்.

---

## நிர்ணயமான மாதிரியாக்கல்

சீரான விளைவுகளை தேவைப்படும் பயன்பாடுகளுக்கு, நிர்ணயமான மாதிரியாக்கல் மீண்டும் உருவாக்கக்கூடிய முடிவுகளை உறுதிசெய்கிறது. இது ஒரு நிலையான சீரற்ற விதையைப் பயன்படுத்தி, `temperature` ஐ பூஜ்யமாக அமைப்பதன் மூலம் செய்யப்படுகிறது.

வெவ்வேறு நிரலாக்க மொழிகளில் நிர்ணயமான மாதிரியாக்கலை விளக்குவதற்கான எடுத்துக்காட்டு:

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


மேலே உள்ள குறியீட்டில், நாங்கள்:

- குறிப்பிட்ட சேவையக URL உடன் MCP வாடிக்கையாளரை உருவாக்கியுள்ளோம்.
- ஒரே தூண்டுதலுடன், நிலையான விதை மற்றும் பூஜ்ய `temperature` உடன் இரண்டு கோரிக்கைகளை அமைத்துள்ளோம்.
- இரு கோரிக்கைகளையும் அனுப்பி உருவாக்கப்பட்ட உரையை அச்சிட்டுள்ளோம்.
- ஒரே விதை மற்றும் `temperature` காரணமாக பதில்கள் ஒரே மாதிரியானவை என்பதை நிர்ணயமான மாதிரியாக்கல் அமைப்பின் மூலம் விளக்கியுள்ளோம்.
- `setSeed` மூலம் ஒரு நிலையான சீரற்ற விதையை குறிப்பிடியுள்ளோம், இதனால் ஒரே உள்ளீட்டுக்கு மாடல் ஒரே விளைவுகளை உருவாக்கும்.
- `temperature` ஐ பூஜ்யமாக அமைத்துள்ளோம், இது அதிகபட்ச நிர்ணயத்தை உறுதிசெய்கிறது, அதாவது மாடல் எந்த சீரற்ற தன்மையுமின்றி மிகவும் சாத்தியமான அடுத்த டோக்கனை எப்போதும் தேர்ந்தெடுக்கிறது.

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


மேலே உள்ள குறியீட்டில், நாங்கள்:

- சேவையக URL உடன் MCP வாடிக்கையாளரை தொடங்கியுள்ளோம்.
- ஒரே தூண்டுதலுடன், நிலையான விதை மற்றும் பூஜ்ய `temperature` உடன் இரண்டு கோரிக்கைகளை அமைத்துள்ளோம்.
- இரு கோரிக்கைகளையும் அனுப்பி உருவாக்கப்பட்ட உரையை அச்சிட்டுள்ளோம்.
- ஒரே விதை மற்றும் `temperature` காரணமாக பதில்கள் ஒரே மாதிரியானவை என்பதை நிர்ணயமான மாதிரியாக்கல் அமைப்பின் மூலம் விளக்கியுள்ளோம்.
- `seed` மூலம் ஒரு நிலையான சீரற்ற விதையை குறிப்பிடியுள்ளோம், இதனால் ஒரே உள்ளீட்டுக்கு மாடல் ஒரே விளைவுகளை உருவாக்கும்.
- `temperature` ஐ பூஜ்யமாக அமைத்துள்ளோம், இது அதிகபட்ச நிர்ணயத்தை உறுதிசெய்கிறது, அதாவது மாடல் எந்த சீரற்ற தன்மையுமின்றி மிகவும் சாத்தியமான அடுத்த டோக்கனை எப்போதும் தேர்ந்தெடுக்கிறது.
- மூன்றாவது கோரிக்கைக்காக வேறொரு விதையைப் பயன்படுத்தியுள்ளோம், இதனால் ஒரே தூண்டுதலுடன் மற்றும் `temperature` உடன் விதை மாறும்போது விளைவுகள் மாறுபடுவதை காட்டுகிறது.

---

## மாறுபடும் மாதிரியாக்கல் அமைப்பு

புத்திசாலித்தனமான மாதிரியாக்கல் ஒவ்வொரு கோரிக்கையின் சூழல் மற்றும் தேவைகளின் அடிப்படையில் அளவீடுகளை மாறுபடுத்துகிறது. அதாவது, பணியின் வகை, பயனர் விருப்பங்கள் அல்லது வரலாற்று செயல்திறன் அடிப்படையில் `temperature`, `top_p`, மற்றும் தண்டனைகளை மாறுபடுத்துகிறது.

வெவ்வேறு நிரலாக்க மொழிகளில் மாறுபடும் மாதிரியாக்கலை எப்படி செயல்படுத்துவது என்பதைப் பார்ப்போம்.

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


மேலே உள்ள குறியீட்டில், நாங்கள்:

- மாறுபடும் மாதிரியாக்கலை நிர்வகிக்கும் `DynamicSamplingService` வகுப்பை உருவாக்கியுள்ளோம்.
- வெவ்வேறு பணிகளுக்கான மாதிரியாக்கல் முன்மாதிரிகளை வரையறுத்துள்ளோம் (படைப்பாற்றல், உண்மையான, குறியீடு, பகுப்பாய்வு).
- பணியின் வகையின் அடிப்படையில் அடிப்படை மாதிரியாக்கல் முன்மாதிரியைத் தேர்ந்தெடுத்துள்ளோம்.
- பயனர் விருப்பங்கள் போன்றவை அடிப்படையில் மாதிரியாக்கல் அளவீடுகளை சரிசெய்துள்ளோம்.
- மாறுபடும் மாதிரியாக்கல் அளவீடுகளுடன் கோரிக்கையை அனுப்பியுள்ளோம்.
- உருவாக்கப்பட்ட உரையை, பயன்படுத்தப்பட்ட மாதிரியாக்கல் அளவீடுகள் மற்றும் பணியின் வகையுடன் திருப்பியுள்ளோம்.
- பயன்படுத்தியுள்ளோம்:
    - `temperature` மூலம் சீரற்ற தன்மையை கட்டுப்படுத்தவும், அதிக மதிப்புகள் படைப்பாற்றலான பதில்களுக்கு வழிவகுக்கும்.
    - `top_p` மூலம் மேல் மொத்த சாத்தியமான அளவுக்கு டோக்கன்களை வரையறுக்கவும், உருவாக்கப்பட்ட உரையின் தரத்தை மேம்படுத்தவும்.
    - `frequency_penalty` மூலம் மீண்டும் மீண்டும் தோன்றுவதை கட்டுப்படுத்தவும், பல்வகைமையை ஊக்குவிக்கவும்.
    - `user_preferences` மூலம் பயனர் வரையறுத்த படைப்பாற்றல் மற்றும் பல்வகைமையுடன் மாதிரியாக்கல் அளவீடுகளை தனிப்பயனாக்கவும்.
    - `task_type` மூலம் கோரிக்கைக்கான சரியான மாதிரியாக்கல் உத்தியைத் தேர்ந்தெடுக்கவும், பணியின் தன்மையின் அடிப்படையில் மேலும் தனிப்பயனாக்கப்பட்ட பதில்களை அனுமதிக்கவும்.
    - `send_request` முறை மூலம், குறிப்பிட்ட தேவைகளுக்கு ஏற்ப மாதிரியாக்கல் அளவீடுகளுடன் தூண்டுதலை அனுப்பவும்.
    - `generated_text` மூலம் மாடலின் பதிலைப் பெறவும், இது பின்னர் மாதிரியாக்கல் அளவீடுகள் மற்றும் பணியின் வகையுடன் திருப்பப்படுகிறது.
    - `min` மற்றும் `max` செயல்பாடுகளைப் பயன்படுத்தி பயனர் விருப்பங்களை செல்லுபடியாகும் வரம்புகளுக்குள் கட்டுப்படுத்தவும், தவறான மாதிரியாக்கல் அமைப்புகளைத் தடுக்கவும்.

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


மேலே உள்ள குறியீட்டில், நாங்கள்:

- பணியின் வகை மற்றும் பயனர் விருப்பங்களின் அடிப்படையில் மாறுபடும் மாதிரியாக்கலை நிர்வகிக்கும் `AdaptiveSamplingManager` வகுப்பை உருவாக்கியுள்ளோம்.
- வெவ்வேறு பணிகளுக்கான மாதிரியாக்கல் சுயவிவரங்களை வரையறுத்துள்ளோம் (படைப்பாற்றல், உண்மையான, குறியீடு, உரையாடல்).
- எளிய யூகங்களின் மூலம் தூண்டுதலிலிருந்து பணியின் வகையை கண்டறியும் முறையை செயல்படுத்தியுள்ளோம்.
- கண்டறியப்பட்ட பணியின் வகை மற்றும் பயனர் விருப்பங்களின் அடிப்படையில் மாதிரியாக்கல் அளவீடுகளை கணக்கிட்டுள்ளோம்.
- வரலாற்று செயல்திறன் அடிப்படையில் கற்றுக்கொண்ட சரிசெய்தல்களைப் பயன்படுத்தி மாதிரியாக்கல் அளவீடுகளை சரிசெய்துள்ளோம்.
- எதிர்கால சரிசெய்தல

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாகக் கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.