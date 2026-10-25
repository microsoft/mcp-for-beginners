> [!WARNING]
> MCP `2026-07-28`ல் சாம்பிளிங் மார்க்கப்படுகிறது. இந்த பாடம் 
> பழைய அமல்படுத்தல்களுக்கு சேமிக்கப்பட்டுள்ளது. புதிய சேவையகங்கள் நேரடியாக ஒரு LLM
> வழங்குநர் API உடன் ஒருங்கிணைக்க வேண்டும்.

# மாடல் கன்டெக்ஸ்ட் ப்ரோட்டோகால் (MCP) இல் சாம்பிளிங்

> ஒத்திசைவு நோக்கத்திற்காக சாம்பிளிங் இன்னும் `2026-07-28` குறித்து உள்ளது மற்றும்
> 2027 ஜூலை 28 அடுத்தது அல்லது அதற்கு பிறகு வெளியிடப்படும் முதல் திருத்தத்தில் நீக்க மிகச் சாத்தியமாகும்.
> இந்த பாடத்தில் உள்ள எடுத்துக்காட்டுகள் `2025-11-25` செயல்படுத்தும் SDK APIகளைப் பயன்படுத்தலாம்.
> MCP இல் என்ன மாற்றம் நடந்தது என்பதை பார்க்க [What's Changed in MCP: The 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md).

பழைய MCP அமல்களில், சாம்பிளிங் சேவையகங்களுக்கு க்ளையண்ட் வாயிலாக LLM நிறைவேற்றல்களை கோர உதவுகிறது.
இந்த பாடம் உடன்பாட்டு மற்றும் இடமாற்ற பணிக்கான அந்த மார்க்கங்களை விளக்குகிறது.




சாம்பிளிங் அடிப்படையிலான ப்ரோட்டோகால் இயந்திரவியல் என்பதைப் புரிந்துகொள்வோம்.

## கற்றல் நோக்கங்கள்

இந்தப் பாடத்தை முடித்தவுடன், நீங்கள் செய்யக்கூடியவைகள்:

- MCP இல் கிடைக்கும் முக்கிய சாம்பிளிங் அளவுருக்களை புரிந்து கொள்வது.
- வெவ்வேறு பயன்பாடுகளுக்கான சாம்பிளிங் அளவுருக்களை அமைத்தல்.
- மீண்டும் பெறக்கூடிய முடிவுகளுக்கு நிச்சயமான சாம்பிளிங் செயல்படுத்தல்.
- பரிசரிப்புகள் மற்றும் பயனர் விருப்பங்களை கருத்தில் கொண்டு சாம்பிளிங் அளவுருக்களை இயல்புநிலை மாற்றல்.
- பல்வேறு சூழலில் மாடல் செயல்திறனை மேம்படுத்த சாம்பிளிங் நெறிமுறைகளை பயன்படுத்தல்.
- MCP க்ளையண்ட்-சேவையக ப்ரோட்டோகால் ஓட்டத்தில் சாம்பிளிங் எவ்வாறு வேலை செய்கிறது என்பதைக் கற்றுக்கொள்ளல்.

## MCP இல் சாம்பிளிங் வேலைசெய்கிறது எப்படி

MCPல் உள்ள சாம்பிளிங் ஓட்டை பின்வரும் படி நடக்கும்:

1. சேவையகம் ஒரு `sampling/createMessage` கோரிக்கையை க்ளையண்டுக்கு அனுப்புகிறது
2. க்ளையண்ட் கோரிக்கையை மதிப்பாய்வு செய்து மாற்றலாம்
3. க்ளையண்ட் LLM இலிருந்து சாம்பிள் எடுக்கிறது
4. க்ளையண்ட் நிறைவு பொருத்தாமையைப் பரிசீலிக்கிறது
5. க்ளையண்ட் முடிவை சேவையகத்திற்கு திருப்பி வழங்குகிறது

இந்த மனிதன்-இன்-தி-லூப் வடிவமைப்பு பயனர்களுக்கு LLM பார்க்கும் மற்றும் உருவாக்கும் விஷயத்தில் கட்டுப்பாடு தருகிறது.

## சாம்பிளிங் அளவுருக்கள் சுருக்கம்

MCP க்ளையண்ட் கோரிக்கைகளில் கட்டமைக்கக்கூடிய பின்வரும் சாம்பிளிங் அளவுருக்கள் உள்ளன:

| அளவுரு | விளக்கம் | சாதாரண வரம்பு |
|-----------|-------------|---------------|
| `temperature` | டோக்கன் தேர்வில் சீரற்ற தன்மையை கட்டுப்படுத்துகிறது | 0.0 - 1.0 |
| `maxTokens` | உருவாக்கப்பட வேண்டிய அதிகபட்ச டோக்கன் எண்ணிக்கை | முழு எண் மதிப்பு |
| `stopSequences` | உருவாக்கத்தை நிறுத்தும் தனிப்பயன் தொடர்கள் | சரங்களின் வரிசை |
| `metadata` | கூடுதல் வழங்குநர்-சிவிலான அளவுருக்கள் | JSON பொருள் |

பல LLM வழங்குநர்கள் `metadata` என்ற புலம் மூலம் கூடுதல் அளவுருக்களை ஆதரிக்கின்றனர், அதில் உள்ளன:

| பொதுவான நீட்டிப்பு அளவுரு | விளக்கம் | சாதாரண வரம்பு |
|-----------|-------------|---------------|
| `top_p` | நியூகிளியஸ் சாம்பிளிங் - டோக்கன்களை மேல்நிலை சீர்திருத்தப் வாய்ப்புடன் வரம்பிடுகிறது | 0.0 - 1.0 |
| `top_k` | டோக்கன் தேர்வை மேல் K விருப்பங்களுக்கு மட்டுப்படுத்துகிறது | 1 - 100 |
| `presence_penalty` | இதுவரை உள்ள உரையில் அடிப்படையிலான டோக்கன்களுக்கு தண்டனை அளிக்கிறது | -2.0 - 2.0 |
| `frequency_penalty` | இதுவரை உள்ள உரையில் அடிப்படையிலான டோக்கன்களுக்கு அடவணை தண்டனை அளிக்கிறது | -2.0 - 2.0 |
| `seed` | மீண்டும் பெறக்கூடிய முடிவுகளுக்கு குறிப்பிட்ட சீரற்ற விதை | முழு எண் மதிப்பு |

## எடுத்துக்காட்டு கோரிக்கை வடிவம்

இதோ MCP இல் இருந்து க்ளையண்டிடம் சாம்பிளிங் கோரிய எடுத்துக்காட்டு:

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

## பதில் வடிவம்

க்ளையண்ட் ஒரு நிறைவு முடிவை திருப்பி அனுப்புகிறது:

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

## மனிதன்-இன்-தி-லூப் கட்டுப்பாடுகள்

மனிதக் கண்காணிப்புடன் MCP சாம்பிளிங் வடிவமைக்கப்பட்டுள்ளது:

- **ப்ராம்ப்ட்களுக்கு**:
  - க்ளையண்டுகள் பயனர்களுக்கு பரிந்துரைக்கப்பட்ட ப்ராம்ப்ட்டை காட்ட வேண்டும்
  - பயனர்கள் ப்ராம்ப்ட்டை மாற்ற அல்லது நிராகரிக்க முடியும்
  - முறைமை ப்ராம்ப்டுகள் வடிகட்ட அல்லது மாற்றப்படலாம்
  - சூழலின் சேர்க்கை க்ளையண்டால் கட்டுப்படுத்தப்படுகிறது

- **நிறைவுகளுக்கு**:
  - க்ளையண்டுகள் பயனர்களுக்கு நிறைவை காட்ட வேண்டும்
  - பயனர்கள் நிறைவுகளை மாற்ற அல்லது நிராகரிக்க முடியும்
  - க்ளையண்டுகள் நிறைவுகளை வடிகட்ட அல்லது மாற்றலாம்
  - பயனர்கள் பயன்படுத்தப்படும் மாடலை கட்டுப்படுத்துகிறார்கள்

இத்தகைய தத்துவங்களோடு, வெவ்வேறு தொகுதிகள் ஆண்டிருக்கும் LLM வழங்குநர்களுக்கு பொதுவான அளவுருக்களில் கவனம் செலுத்தி சாம்பிளிங் செயல்படுத்துவது எப்படி என்று பார்ப்போம்.

## பாதுகாப்பு பரிசீலனைகள்

MCPவில் சாம்பிளிங் செய்வதில், பின்வரும் பாதுகாப்பு சிறந்த நடைமுறைகளை கருத்தில் கொள்ளுங்கள்:

- **அனைத்து செய்தி உள்ளடக்கங்களையும் சரிபார்க்கவும்** க்ளையண்டுக்கு அனுப்புவதற்கு முன்பு
- **பரிந்துரைகள் மற்றும் நிறைவேற்றல்களில் இருந்து sensibles தகவலை சுத்திகரிக்கவும்**
- **தவிர்க்குமாறு வரம்புகளை அமல்படுத்தவும்**
- **சாம்பிளிங் பயன்பாட்டை அசாதாரண விதிகளுக்கு கண்காணிக்கவும்**
- **பாதுகாப்பான ப்ரோட்டோகால்களை பயன்படுத்தி தரவை குறியாக்கவும்**
- **பயனர் தரவு தனியுரிமையை சம்பந்தப்பட்ட விதிகளின் படி கையாளவும்**
- **உறுப்புப் பின்வாங்குதல்களுக்கு சாம்பிளிங் கோரிக்கைகளை ஆய்வு செய்யவும்**
- **செலவுகளை கட்டுப்படுத்த சரியான வரம்புகளை அமைக்கவும்**
- **சாம்பிளிங் கோரிக்கைகளுக்கு காலாவதிச்செலுத்தல்களை நிறைவேற்றவும்**
- **மாடல் பிழைகளை நுணுக்கமாக கையாளவும், சரியான மாற்றுரைகளை விடுவிக்கவும்**

சாம்பிளிங் அளவுருக்கள் மொழி மாடல்களின் நடத்தையை நுட்பமாக கட்டுப்படுத்த உதவுகின்றன, குறிப்பாக நிச்சயமான மற்றும் சிண்மானமான முடிவுகளுக்கு இடையே சரியான சமநிலை கொண்டு உருவாக்கும்.

இப்போது அவற்றைக் வெவ்வேறு புரோகிராமிங் மொழிகளில் எவ்வாறு அமைப்பது என்பதைப் பார்ப்போம்.

# [.NET](#tab-dotnet)

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

முன்னைய குறியீட்டில் நாம்:

- குறிப்பிட்ட சேவையக URL உடன் MCP க்ளையண்ட் உருவாக்கினோம்.
- `temperature`, `top_p` மற்றும் `top_k` போன்ற சாம்பிளிங் அளவுருக்களை கோரிக்கையில் அமைத்தோம்.
- கோரிக்கையை அனுப்பி உருவாக்கப்பட்ட உரையை அச்சிடவும் செய்தோம்.
- பயன்படுத்தியது:
    - உருவாக்க நேரத்தில் எந்த கருவிகள் பயன்படும் என்பதை குறிப்பிட `allowedTools`. இந்த வழக்கில், `ideaGenerator` மற்றும் `marketAnalyzer` கருவிகள் படைப்பாற்றல் அப்பிளிக்கேஷன் யோசனைகளை உதவ அனுமதிக்கப்பட்டன.
    - வெளிப்பாட்டில் மீண்டும் வருகையை மற்றும் பன்முகத்துவத்தை கட்டுப்படுத்த `frequencyPenalty` மற்றும் `presencePenalty` பயன்படுத்தப்பட்டன.
    - வெளியீட்டின் சீரற்ற தன்மையை கட்டுப்படுத்த `temperature` பயன்படுத்தப்பட்டது, அதிக மதிப்புகள் அதிக சாம்பிளிங் சுதந்திரத்தைக் கொண்டுவிடும்.
    - உருவாக்கப்பட்ட உரையின் தரம் மேம்படும் வகையில் மேல்நிலை சேர்க்கை வாய்ப்பை பதிப்புக்கு மட்டுப்படுத்த `top_p` பயன்படுத்தப்பட்டது.
    - மாடலை மேல்நிலை K அதிக வாய்ப்புடைய டோக்கன்களுக்கு மட்டுமே கட்டுப்படுத்த `top_k` பயன்படுத்தப்பட்டது, இது பதில்கள் பிணைப்பை மேம்படுத்த உதவும்.
    - மீண்டும் வருகையை குறைக்கும் மற்றும் பன்முகத்துவத்தை ஊக்குவிக்கும் வகையில் `frequencyPenalty` மற்றும் `presencePenalty` பயன்படுத்தப்பட்டது.

# [JavaScript](#tab/javascript)

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

முன்னைய குறியீட்டில் நாம்:

- சேவையக URL மற்றும் API கீயுடன் MCP க்ளையண்ட் தொடங்கினோம்.
- இரு வகையான சாம்பிளிங் அளவுருக்களை அமைத்தோம்: படைப்பாற்றல் பணிகளுக்கு மற்றும் உண்மையான பணிகளுக்கு.
- இந்த அமைப்புகளுடன் கோரிக்கைகளை அனுப்பி, மாடல் ஒவ்வொரு பணிக்கும் குறிப்பிட்ட கருவிகளைப் பயன்படுத்த அனுமதித்தோம்.
- வெவ்வேறு சாம்பிளிங் அளவுருக்கள் விளைவுகளை தெளிவுபடுத்தி பதில்களை அச்சிடினோம்.
- உருவாக்கத்தில் எந்த கருவிகள் பயன்படும் என்பதை குறிப்பிட `allowedTools` பயன்படுத்தப்பட்டது. இதில் படைப்பாற்றல் பணிகளுக்கான `ideaGenerator` மற்றும் `environmentalImpactTool` மற்றும் உண்மையான பணிகளுக்கான `factChecker` மற்றும் `dataAnalysisTool` அனுமதிக்கப்பட்டன.
- வெளியீட்டின் சீரற்ற தன்மையை கட்டுப்படுத்த `temperature` பயன்படுத்தப்பட்டது, அதிக மதிப்புகள் அதிக படைப்பாற்றலை வழிநடத்தும்.
- உருவாக்க உரையின் தரத்தை மேம்படுத்த மேல்நிலை சேர்க்கை வாய்ப்புக்கு மட்டும் டோக்கன்களை கட்டுப்படுத்த `top_p` பயன்படுத்தப்பட்டது.
- மீண்டும் வருகையை குறைத்து பன்முகத்துவத்தை ஊக்குவிக்க `frequencyPenalty` மற்றும் `presencePenalty` பயன்படுத்தப்பட்டன.
- மாடலை மேல் K அதிக வாய்ப்புடைய டோக்கன்களுக்கு மட்டுப்படுத்த `top_k` பயன்படுத்தப்படுகிறது, இது பதில்களை தெளிவான முறையில் உருவாக்க உதவும்.

---

## நிச்சயமான சாம்பிளிங்

எப்போதும் ஒரே மாதிரி முடிவுகளை தேவைப்படும் பயன்பாடுகளுக்கு, நிச்சயமான சாம்பிளிங் மீண்டும் பெறக்கூடிய முடிவுகளை உறுதி செய்கிறது. இது ஒரு நிரந்தர ரேண்டம் விதையை பயன்படுத்தி மற்றும் வெப்பநிலை அமைப்பை பூஜ்ஜியமாக்கி செயல் படுகிறது.

கீழே வெவ்வேறு புரோகிராமிங் மொழிகளில் நிச்சயமான சாம்பிளிங்கைப் பாவித்த பராமரிப்பின் எடுத்துக்காட்டு உள்ளது.

# [Java](#tab/java)

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

முன்னைய குறியீட்டில் நாம்:

- குறிப்பிட்ட சேவையக URL உடன் MCP க்ளையண்ட் உருவாக்கினோம்.
- ஒரே ப்ராம்ப்டுடன், நிரந்தர விதையுடன் மற்றும் பூஜ்ஜிய வெப்பநிலையுடன் இரண்டு கோரிக்கைகளை அமைத்தோம்.
- இரண்டும் அனுப்பி உருவாக்கப்பட்ட உரையை அச்சிடினோம்.
- நிச்சயமான சாம்பிளிங் அமைப்பைக் காரணமாகவும் பதில்கள் ஒரே மாதிரியாக இருப்பதை காட்டினோம்.
- பதில்கள் ஒருபோதும் மாறாததை உறுதி செய்ய `setSeed` கொண்டு நிரந்தர ரேண்டம் விதையை குறிப்பிட்டோம்.
- அதிகபட்ச நிச்சயத்தை உறுதியானது செய்ய `temperature` பூஜ்ஜியமாக அமைத்தது, இதனால் மாடல் எப்போதும் அடுத்த பெறுமானம் மிக அதிக வாய்ப்புள்ள டோக்கனை தேர்ந்தெடுக்கிறது.

# [JavaScript](#tab/javascript-deterministic)

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

முன்னைய குறியீட்டில் நாம்:

- சேவையக URL உடன் MCP க்ளையண்ட் தொடங்கினோம்.
- ஒரே ப்ராம்ப்டுடன், நிரந்தர விதையுடன் மற்றும் பூஜ்ஜிய வெப்பநிலையுடன் இரண்டு கோரிக்கைகளை அமைத்தோம்.
- இரண்டும் அனுப்பி உருவாக்கப்பட்ட உரையை அச்சிடினோம்.
- பதில்கள் நிச்சயமான சாம்பிளிங் காரணமாக ஒரே மாதிரியாக இருப்பதை விளக்கினோம்.
- நிரந்தர விதையை குறிப்பிட `seed` பயன்படுத்தியது, அதனால் மாடல் ஒரே உள்ளீட்டுக்கு எப்போதும் ஒரே வெளியீட்டைத் தரும்.
- அதிக நிச்சயத்தை உறுதி செய்ய `temperature` பூஜ்ஜியமாக அமைத்தோம், இதனால் சீரற்ற தன்மை இல்லாமல் மட்டுமே தேர்வு செய்யப்படும்.
- முப்பத்தாண்டாவது கோரிக்கைக்கான விதையை வேறுபடுத்தியது பற்ற்மாறுபடுபவை வெளிப்படும் என்பதை காட்டியது.

---

## தானாக மாறும் சாம்பிளிங் அமைப்பு

புத்திசாலித்தனம் கொண்ட சாம்பிளிங் ஒவ்வொரு கோரிக்கையின் சூழல் மற்றும் தேவைகளின் படி அளவுருக்களை தானாக மாறச் செய்கிறது. இது வெப்பநிலை, top_p மற்றும் தண்டனைகள் போன்றவற்றை பணியின் வகை, பயனர் விருப்பங்கள் அல்லது கடந்த கால செயல்திறன் அடிப்படையில் மாற்றுதல் ஆகும்.

தானாக மாறும் சாம்பிளிங்கை வெவ்வேறு புரோகிராமிங் மொழிகளில் எவ்வாறு செய்யலாம் என்பதை பார்க்கலாம்.

# [Python](#tab/python)

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

முன்னைய குறியீட்டில் நாம்:

- அதிரடியாக சாம்பிளிங்கை நயவழி நிர்வகிக்கும் `DynamicSamplingService` வகுப்பை உருவாக்கினோம்.
- வெவ்வேறு பணிகளுக்கு சாம்பிளிங் முன்கூட்டிய அமைப்புகளை வரையறுத்தோம் (படைப்பாற்றல், உண்மை, குறியீடு, பகுப்பாய்வு).
- பணியின் வகை அடிப்படையில் அடிப்படை சாம்பிளிங் திட்டத்தைக் தேர்ந்தெடுத்தோம்.
- படைப்பாற்றல் மற்றும் பன்முகத்துவம் போன்ற பயனர் விருப்பங்களின் படி சாம்பிளிங் அளவுருக்களை மாற்றினோம்.
- கண்காணிக்க கூடிய சாம்பிளிங் அளவுருக்களுடன் கோரிக்கையை அனுப்பினோம்.
- உருவாக்கப்பட்ட உரையை, பயன்படுத்திய அளவுருக்கள் மற்றும் பணியினை வெளிப்படுத்தித் திருப்பி வழங்கினோம்.
- வெளியீட்டின் சீரற்ற தன்மையை கட்டுப்படுத்த `temperature` பயன்படுத்தி, உயர்ந்த மதிப்புகள் கூட அதிக படைப்பாற்றலை வழிநடத்தும்.
- உரையின் தரத்தை மேம்படுத்த மேல்நிலை சேர்க்கையை கட்டுப்படுத்த `top_p` பயன்படுத்தினோம்.
- மீண்டும் வருகையை குறைக்க மற்றும் பன்முகத்துவம் ஊக்குவிக்க `frequency_penalty` பயன்படுத்தினோம்.
- பயனர் வரையறுத்த படைப்பாற்றல் மற்றும் பன்முகத்துவத்தின் அடிப்படையில் சாம்பிளிங் அளவுருக்களை தனிப்பயனாக்க `user_preferences` பயன்படுத்தினோம்.
- கோரிக்கைக்கான ஏற்புடைய சாம்பிளிங் திட்டத்தை தீர்மானிக்க `task_type` பயன்படுத்தினோம்.
- விவரிக்கப்பட்ட அளவுருக்களுடன் ப்ராம்ப்ட்டைக் அனுப்ப `send_request` विधியை பயன்படுத்தினோம்.
- மாடல் பதிலை பெற `generated_text` பயன்படுத்தி, அது திருப்பியும் அளவுருக்களும் மற்றும் பணிவகை பகிர்ந்தன.
- பயனர் விருப்பங்களை சரியான வரம்புக்குள் உறுதிப்படுத்த `min` மற்றும் `max` செயல்பாடுகளை இந்தபடி இயக்கினோம்.

# [JavaScript Dynamic](#tab/javascript-dynamic)

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

முன்னைய குறியீட்டில் நாம்:

- பணியின் வகை மற்றும் பயனர் விருப்பங்கள் அடிப்படையிலான தானாக மாறும் சாம்பிளிங் நிர்வகிக்கும் `AdaptiveSamplingManager` வகுப்பை உருவாக்கினோம்.
- வெவ்வேறு பணிகளுக்கான சாம்பிளிங் நோக்குகளைக் கண்டறிந்தோம் (படைப்பாற்றல், உண்மை, குறியீடு, உரையாடல்).
- எளிமையான வழிகள் மூலம் ப்ராம்ப்டிலிருந்து பணி வகையை கண்டுபிடிக்கும் முறையை செயல்படுத்தினோம்.
- பணி வகை மற்றும் பயனர் விருப்பத்தின் படி சாம்பிளிங் அளவுருக்களை கணக்கிட்டோம்.
- கடந்த கால செயல்திறன் அடிப்படையில் படிப்படியான மாற்றங்களைச் செய்கிறோம்.
- இனிய விருப்பங்களுக்கு கற்றலை பதிவு செய்தோம்.
- கண்காணிக்கப்பட்ட சாம்பிளிங் அளவுருக்கள் மற்றும் கண்டறியும் பணி வகையுடன் கோரிக்கைகளை அனுப்பி உருவாக்கப்பட்ட உரையை திருப்பியும் வழங்கினோம்.
- பயன்படுத்தியது:
    - பயனர் வரையறுக்கப்பட்ட படைப்பாற்றல், துல்லியம் மற்றும் ஒத்திசைவு நிலைகளின் படி சாம்பிளிங் அளவுருக்களை தனிப்பயனாக்க `userPreferences`.
    - ப்ராம்ப்டின் அடிப்படையில் பணி இயல்பை தீர்மானிக்க `detectTaskType`.
    - உருவாக்கப்பட்ட பதில்களின் செயல்திறன் பதிவு செய்து அமைப்புக்கு மாற்றங்களை ஏற்றுக்கொள்ளும் வகையில் `recordPerformance`.
    - கடந்த கால செயல்திறன் அடிப்படையில் சாம்பிளிங் அளவுருக்களை மாற்ற `applyLearnedAdjustments`.
    - அதிரடிப் சாம்பிளிங்குடன் பதில்கள் உருவாக்குவதற்கான முழு செயல்முறையை இந்தப் பொருளாக்கி அழைக்கக் கூடியவாறு `generateResponse`.
    - உருவாக்கத்தின் போது எந்த கருவிகள் பயன்படும் என்பதைக் குறிப்பிட `allowedTools`.
    - பயன்படுத்திய பதில்களின் தரத்தை ஆராய பயனர்களின் கருத்துக்களை பெற `feedbackScore`.
    - கடந்த வினவுகளில் இருந்து கற்றுக்கொள்ள முன் செயல்திறன் பதிவு `performanceHistory`.
    - கோரிக்கையின் சூழல் அடிப்படையில் சாம்பிளிங் அளவுருக்களை தானாக மாற்ற `getSamplingParameters`.
    - ப்ராம்ப்டின் அடிப்படையில் பணி வகையை வகைப்படுத்தி சரியான சாம்பிளிங் திட்டத்தை அமல்படுத்த `detectTaskType`.
    - வேகமாகவே வேண்டிய அளவுரு மாற்றங்களைச் செய்யும் தனிப்பட்ட அமைப்புகள் `samplingProfiles`.

---

## அடுத்து என்ன

- [5.7 பரிமாண முறை](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->