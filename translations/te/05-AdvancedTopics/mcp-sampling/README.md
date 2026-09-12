> [!WARNING]
> MCP `2026-07-28` నందు శాంప్లింగ్‍ పర్యూటమైంది. ఈ పాఠం
> పాత అమలు విధానాల కోసం ఉంచబడింది. కొత్త సర్వర్లు నేరుగా LLM
> ప్రొవైడర్ API తో ఐకీకృతం కావాలి.

# మోడల్ కాన్టెక్స్ట్ ప్రోటోకాల్ లో శాంప్లింగ్

> శాంప్లింగ్ `2026-07-28` ప్రత్యేకణలో అనుకూలత కోసం ఉంచబడినది మరియు
> జులై 28, 2027 తర్వాత విడుదలవేసే మొదటి సవరణలో తొలగింపు కి అర్హత కల్గుంది.
> ఈ పాఠంలోని ఉదాహరణలు `2025-11-25` అమలు చేసే SDK API లను ఉపయోగించవచ్చు.
> [MCP లో ఏమి మారిపోయింది: 2026-07-28 ప్రత్యేకణ](../../01-CoreConcepts/mcp-2026-07-28.md) చూడండి.

పాత MCP అమలులో, శాంప్లింగ్ సర్వర్లు క్లయింట్ ద్వారా LLM పూర్తి
అభ్యర్థించడానికి అనుమతిస్తుంది. ఈ పాఠం ఆ పాత ప్రోటోకాల్
ఫ్లోను అనుకూలత మరియు మార్పిడి పనులకు వివరిస్తుంది.

## పరిచయం

ఈ పాఠంలో, మేము MCP అభ్యర్థనలలో శాంప్లింగ్ పరామితులు ఎలా






- MCP లో అందుబాటులో ఉన్న ముఖ్యమైన శాంప్లింగ్ పరామితులను అవగాహన చేసుకోండి.
- వేర్వేరు ఉపయోగాల కోసం శాంప్లింగ్ పరామితులను సెటప్ చేయండి.
- పునఃఉత్పాదక ఫలితాల కోసం నిర్దిస్ట శాంప్లింగ్ ను అమలు చేయండి.
- సందర్భం మరియు వినియోగదారు ఇష్టాల ఆధారంగా శాంప్లింగ్ పరామితులను డైనమిక్ గా సర్దుబాటు చేయండి.
- వివిధ సందర్భాల్లో మోడల్ పనితీరును మెరుగు పరచడానికి శాంప్లింగ్ వ్యూహాలను వర్తపరచండి.






1. సర్వర్ నుండి క్లయింట్ కి `sampling/createMessage` అభ్యర్థన పంపబడుతుంది
2. క్లయింట్ ఆ అభ్యర్థనను సమీక్షించి మార్చవచ్చు
3. క్లయింట్ LLM నుండి శాంపుల్ చేస్తుంది
4. క్లయింట్ పూర్తయిన పరిశీలన చేస్తుంది








| Parameter | వివరణ | సాదారణ పరిధి |
|-----------|-------------|---------------|
| `temperature` | టోకెన్ ఎంపికలో యాదృచ్ఛికతను నియంత్రిస్తుంది | 0.0 - 1.0 |
| `maxTokens` | ఉత్పత్తి చేయవలసిన గరిష్ట టోకెన్ల సంఖ్య | పూర్తిసంఖ్య విలువ |
| `stopSequences` | ఎదురైతే ఉత్పత్తి ఆగే ప్రత్యేక సీక్వెన్సులు | స్ట్రింగ్ ల యర్రే |




| సాధారణ పొడగింపు పరామితి | వివరణ | సాదారణ పరిధి |
|-----------|-------------|---------------|
| `top_p` | న్యూక్లియస్ శాంప్లింగ్ - టోకెన్లను టాప్ సమ్మిళితProbability కి పరిమితం చేస్తుంది | 0.0 - 1.0 |
| `top_k` | టోకెన్ ఎంపికను టాప్ K ఎంపికలకి పరిమితం చేస్తుంది | 1 - 100 |
| `presence_penalty` | ఇప్పటి వరకు టెక్స్ట్ లో టోకెన్ల ఉనికికి ఆధారంగా జరిమానా విధిస్తుంది | -2.0 - 2.0 |
| `frequency_penalty` | ఇప్పటి వరకు టెక్స్ట్ లో టోకెన్ల తరచుకాలపై జరిమానా విధిస్తుంది | -2.0 - 2.0 |





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

## ప్రతిస్పందన ఫార్మాట్

క్లయింట్ పూర్తి ఫలితాన్ని ఇస్తుంది:

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

## మానవ నియంత్రణలు

MCP శాంప్లింగ్ మానవ పర్యవేక్షణతో రూపొందించబడింది:


- **ప్రాంప్ట్‌ల కోసం**:
  - క్లయింట్లు ఉపయోగదారులకు ప్రతిపాదిత ప్రాంప్ట్‌ను చూపించాలి
  - ఉపయోగదారులు ప్రాంప్ట్‌లను మార్చడానికి లేదా తిరస్కరించడానికి వీలుగా ఉండాలి
  - సిస్టమ్ ప్రాంప్ట్‌లను ఫిల్టర్ చేయవచ్చు లేదా మార్చవచ్చు
  - కాంటెక్ట్ చేర్పింపు క్లయింట్ చేత నియంత్రించబడుతుంది

- **పూర్తి కోసం**:
  - క్లయింట్లు ఉపయోగదారులకు పూర్తి వివరాన్ని చూపించాలి
  - ఉపయోగదారులు పూర్తి వివరాలను మార్చడానికి లేదా తిరస్కరించడానికి వీలుగా ఉండాలి
  - క్లయింట్లు పూర్తి వివరాలను ఫిల్టర్ చేయవచ్చు లేదా మార్చవచ్చు
  - ఉపయోగదారులు ఏ మోడల్ వాడాలని నిర్ణయిస్తారు

ఈ సూత్రాలకు అనుగుణంగా, వివిధ ప్రోగ్రామింగ్ భాషల్లో ఎలా శాంప్లింగ్‌ను అమలు చేయాలో చూద్దాం, ముఖ్యంగా LLM ప్రొవైడర్లలో సాధారణంగా మద్దతు ఉన్న పరామితులపై ఫోకస్ చేస్తూ.

## భద్రతా పరిగణనలు

MCP లో శాంప్లింగ్‌ను అమలు చేస్తున్నప్పుడు ఈ భద్రతా ఉత్తమ విధానాలను పరిగణించాలి:

- **సందేశపు అన్ని కంటెంట్‌ను ధృవీకరించండి** క్లయింట్‌కు పంపించే ముందు
- **ప్రాంప్ట్‌లు మరియు పూర్తి వివరాలలోని సున్నితమైన సమాచారాన్ని శుభ్రపరచండి**
- **దడియాన్ని నియంత్రించేందుకు రేట్ పరిమితులను అమలు చేయండి**
- **అసాధారణ నమూనాల కోసం శాంప్లింగ్ వినియోగాన్ని గమనించండి**
- **సురక్షిత ప్రోటోకాల్స్ ఉపయోగించి డేటాను ట్రాన్సిట్‌లో ఎన్‌క్రిప్ట్ చేయండి**
- **సంబంధిత నియమావళి ప్రకారం ఉపయోగదారి డేటా గోప్యతను నిర్వహించండి**
- **అనుగుణత మరియు భద్రత కోసం శాంప్లింగ్ అభ్యర్థనలను ఆడిట్ చేయండి**
- **సరైన పరిమితులతో ఖర్చు ప్రదర్శనను నియంత్రించండి**
- **శాంప్లింగ్ అభ్యర్థనలకు టైమ్‌అవుట్‌లను అమలు చేయండి**
- **మోడల్ లోపాలను శ్రద్ధగా నిర్వహించి సరైన ప్రత్యామ్నాయాలను అమలు చేయండి**

శాంప్లింగ్ పరామితులు భాషా మోడళ్ల ప్రవర్తనను నిశ్చితమైన మరియు సృజనాత్మక అవుట్‌పుట్‌ల మధ్య అవసరమయిన సమతుల్యతను సాధించడానికి సంతులనం చేస్తాయి.

వివిధ ప్రోగ్రామింగ్ భాషల్లో ఈ పరామితులను ఎలా కాన్ఫిగర్ చేయాలో చూద్దాం.

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

పై కోడ్లో మేము:

- నిర్దిష్ట సర్వర్ URL తో MCP క్లయింట్‌ను సృష్టించాము.
- `temperature`, `top_p`, మరియు `top_k` వంటి శాంప్లింగ్ పరామితులతో అభ్యర్థనను కాన్ఫిగర్ చేయాము.
- అభ్యర్థనను పంపించి సృష్టించిన టెక్స్ట్‌ను ప్రింట్ చేశాము.
- ఉపయోగించాము:
    - `allowedTools` ద్వారా జనరేషన్ సమయంలో మోడల్ వాడగల టూల్స్‌ను నిర్దేశించాము. ఈ కేసులో, సృజనాత్మక యాప్ ఆలోచనలను సృష్టించడానికి `ideaGenerator` మరియు `marketAnalyzer` టూల్స్‌కి అనుమతి ఇచ్చాము.
    - అవుట్‌పుట్‌లో పునరావృతం మరియు వైవిధ్యాన్ని నియంత్రించడానికి `frequencyPenalty` మరియు `presencePenalty`.
    - అవుట్‌పుట్ రాండమ్నెస్‌ను నియంత్రించడానికి `temperature`, దీనిలో ఎక్కువ విలువలు మరింత సృజనాత్మక సమాధానాలకు దారి తీస్తాయి.
    -.Generated text నాణ్యతను మెరుగుపరచడానికి ఎంచుకున్న టోకెన్లను టాప్ సమీకృత probability mass వరకు పరిమితం చేయడానికి `top_p`.
    - మరింత సుస్ఫూర్తి సమాధానాలను రాబట్టడానికి టాప్ K అత్యంత సంభావ్య టోకెన్లకు మోడల్‌ను పరిమితం చేయడానికి `top_k`.
    - పునరావృతం తగ్గించడానికి మరియు వైవిధ్యం ప్రేరేపించడానికి `frequencyPenalty` మరియు `presencePenalty`.

# [JavaScript](#tab/javascript)

```javascript
// జావాస్క్రిప్ట్ ఉదాహరణ: ఉష్ణోగ్రత మరియు టాప్-పి శాంప్లింగ్ కాన్ఫిగరేషన్
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // MCP క్లయింట్‌ను 초기ి చేయండి
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // విభిన్న 샘్ప్లింగ్ పరామితులతో అభ్యర్థనను కాన్ఫిగర్ చేయండి
  const creativeSampling = {
    temperature: 0.9,    // అధిక ఉష్ణోగ్రత = మరింత యాదృచ్ఛికత/సృజనాత్మకత
    topP: 0.92,          // టోకెన్లను టాప్ 92% ప్రాబబిలిటీ మాస్‌తో పరిగణనలోకి తీసుకోండి
    frequencyPenalty: 0.6, // టోకెన్ వరుసల పునరావృతిని తగ్గించండి
    presencePenalty: 0.4   // ఇప్పటి వరకు పాఠ్యത്തിൽ వచ్చిన టోకెన్లను శిక్షించండి
  };
  
  const factualSampling = {
    temperature: 0.2,    // తక్కువ ఉష్ణోగ్రత = మరింత నిర్ణయాత్మక/వాస్తవిక
    topP: 0.85,          // కొంచెం ఎక్కువ కేంద్రీకృత టోకెన్ ఎంపిక
    frequencyPenalty: 0.2, // కనీస పునరావృతి శిక్ష
    presencePenalty: 0.1   // కనీస ప్రస్తుతత్వ శిక్ష
  };
  
  try {
    // విభిన్న శాంప్లింగ్ కాన్ఫిగరేషన్లతో రెండు అభ్యర్థనలు పంపండి
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

పై కోడ్లో మేము:

- సర్వర్ URL మరియు API కీతో MCP క్లయింట్‌ను ప్రారంభించాము.
- సృజనాత్మక పనులకు ఒకటి మరియు వాస్తవ పనులకు మరొకటి గా రెండు శాంప్లింగ్ పరామితుల సమితులను కాన్ఫిగర్ చేశాము.
- ఈ కాన్ఫిగర్‌లతో అభ్యర్థనలను పంపించాము, ప్రతి పనికి ప్రత్యేక టూల్స్ వాడేందుకు మోడల్‌కు అనుమతిస్తూ.
- వివిధ శాంప్లింగ్ పరామితుల ప్రభావాలను చూపించడానికి సృష్టించిన స్పందనలను ప్రింట్ చేయడం జరిగింది.
- జనరేషన్ సమయంలో మోడల్ వాడగల టూల్స్‌ను `allowedTools` ద్వారా నిర్దేశించాము. ఈ కేసులో, సృజనాత్మక పనులకు `ideaGenerator` మరియు `environmentalImpactTool` ను, వాస్తవ పనులకు `factChecker` మరియు `dataAnalysisTool` ను అనుమతించాము.
- అవుట్‌పుట్ రాండమ్నెస్‌ను నియంత్రించడానికి `temperature` ను ఉపయోగించాము, దీనిలో ఎక్కువ విలువలు మరింత సృజనాత్మక సమాధానాలకు దారి తీస్తాయి.

- `top_p` ను టోకెన్ల ఎంపికను టాప్ సహస్రజన్యత సామ్యం ద్రవ్యాన్ని అందించే వాటిపై పరిమితం చెయ్యడానికి ఉపయోగించి, సృష్టించిన టెక్స్టు గుణాత్మకతను పెంపొందించి.
- `frequencyPenalty` మరియు `presencePenalty` ను పునరావృతాన్ని తగ్గించడానికి మరియు అవుట్‌పుట్‌లో విభిన్నతను ప్రేరేపించడానికి ఉపయోగించారు.
- `top_k` ఉపయోగించి నమూనాను టాప్ K అత్యంత సంభావ్య టోకెన్ల వరకు పరిమితం చేసి, సమగ్రమైన ప్రతిస్పందనలు సృష్టించడంలో సహాయం చేయవచ్చు.

---

## నిర్ణీత శాంప్లింగ్

స్థిరమైన అవుట్పుట్లను కావాలనుకునే అనువర్తనాల కోసం, నిర్ణీత శాంప్లింగ్ తిరిగి ఉత్పాదక ఫలితాలను నిర్ధారిస్తుంది. ఇది ఎలా చేస్తుంది అంటే, ఒక స్థిర రాండమ్సీడ్ ఉపయోగించి మరియు nhiệtశక్తిని (temperature) సున్నా గా సెట్ చేయడం ద్వారా.

వివిధ ప్రోగ్రామింగ్ భాషలలో నిర్ణీత శాంప్లింగ్‌ను చూపించడానికి క్రింది నమూనా అమలును చూద్దాం.

# [Java](#tab/java)

```java
// జావా ఉదాహరణ: స్థిరమైన సీడ్ తో నిర్ధారిత ప్రతిస్పందనలు
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // నిర్ధారిత ఫలితాల కోసం స్థిరమైన సీడ్ ఉపయోగించడం
        
        // స్థిరమైన సీడ్ తో మొదటి అభ్యర్థన
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // అత్యధిక నిర్ధారితత్వం కోసం శూన్య ఉష్ణోగ్రత
            .build();
            
        // అదే సీడ్ తో రెండవ అభ్యర్థన
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // రెండు అభ్యర్థనలను నడపండి
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // అదే సీడ్ మరియు ఉష్ణోగ్రత=0 కారణంగా ప్రతిస్పందనలు ఒకటే ఉండాలి
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

పూర్వపు కోడ్‌లో మేము:

- ఒక MCP క్లీంట్ ను నిర్దేశిత సర్వర్ URL తో సృష్టించాము.
- ఒకే ప్రాంప్ట్, స్థిరమైన సీడ్, మరియు సున్నా nhiệtశక్తితో రెండు అభ్యర్థనలను రక్తించింది.
- ఇరువురు అభ్యర్థనలను పంపించి సృష్టించబడిన టెక్స్టును ముద్రించారు.
- సమాధానాలు ఒకే విధంగా ఉన్నాయని ప్రదర్శించాము, దానిని నిర్ణీత శాంప్లింగ్ కాన్ఫిగరేషన్ యొక్క ప్రకృతిని (అనే ఒకే సీడ్ మరియు nhiệtశక్తి) కారణంగా.
- `setSeed` ఉపయోగించి ఒక స్థిర రాండమ్ సీడ్‌ను పేర్కొన్నాము, తద్వారా నమూనా ఒక్కోసారి అదే ఇన్పుట్ కోసం ఒకే అవుట్‌పుట్‌ను సృష్టిస్తుంది.
- nhiệtశక్తి (temperature) ని సున్నాగా సెట్ చేసి, గరిష్ట నిర్ణీతత్వం కలిగించేలా చేశాము, అంటే నమూనా ఎప్పుడూ అత్యంత సంభావ్యమైన తదుపరి టోకెన్‌ను ఏ విపరీతత్వం లేకుండా ఎంచుకుంటుంది.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// జావాస్క్రిప్ట్ ఉదాహరణ: సీడ్ నియంత్రణతో నిర్ణీత స్పందనలు
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // స్థిర సీడ్‌తో మొదటి అభ్యర్థన
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // గరిష్ఠ నిర్ణీతత్వానికి సున్నా ఉష్ణోగ్రత
    });
    
    // అదే సీడ్ మరియు ఉష్ణోగ్రతతో రెండవ అభ్యర్థన
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // ప్రముఖ సీడ్ కానాంటి కాని అదే ఉష్ణోగ్రతతో మూడవ అభ్యర్థన
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

పూర్వపు కోడ్‌లో మేము:

- ఒక MCP క్లీంట్ ను సర్వర్ URL తో ప్రారంభించాము.
- ఒకే ప్రాంప్ట్, స్థిరమైన సీడ్ మరియు సున్నా nhiệtశక్తితో రెండు అభ్యర్థనలను సెట్ చేశాము.
- ఇరువురు అభ్యర్థనలను పంపించి సృష్టించిన టెక్స్టును ముద్రించాము.
- సమాధానాలు ఒకే విధంగా ఉన్నాయని ప్రదర్శించాము, నిర్ణీత శాంప్లింగ్ కాన్ఫిగరేషన్ (ఒకే సీడ్ మరియు nhiệtశక్తి) కారణంగా.
- `seed` ఉపయోగించి స్థిర రాండమ్ సీడ్‌ను పేర్కొన్నాము, దాంతో నమూనా ఒకే ఇన్పుట్ కోసం ఎప్పుడూ ఒకే అవుట్‌పుట్ సృష్టిస్తుంది.
- nhiệtశక్తిని సున్నాగా సెట్ చేసి గరిష్ట నిర్ణీతత్వాన్ని నిర్ధారించాము, దాంతో నమూనా ఎప్పుడూ అత్యంత సంభావ్యమైన తదుపరి టోకెన్‌ను ఎంచుకుంటుంది.
- మూడవ అభ్యర్థన కోసం వేరే సీడ్ ఉపయోగించి చూపించాము, సీడ్ మార్చడం వల్ల కూడా ఒకే ప్రాంప్ట్ మరియు nhiệtశక్తి ఉన్నప్పటికీ భిన్నమైన అవుట్పుట్లను తెస్తుంది.

---

## డైనమిక్ శాంప్లింగ్ కాన్ఫిగరేషన్

తెలివైన శాంప్లింగ్ ప్రతి అభ్యర్థన యొక్క సందర్భం మరియు అవసరాల ఆధారంగా పారామితులను అనుకూలంగా మార్చుకుంటుంది. అంటే పనితీరు విధానం, వినియోగదారు అభిరుచులు లేదా చరిత్రాత్మక పనితీరు ఆధారంగా nhiệtశక్తి, top_p మరియు శిక్షణలను డైనమిక్‌గా సర్దుబాటు చేయడం.

వివిధ ప్రోగ్రామింగ్ భాషల్లో డైనమిక్ శాంప్లింగ్‌ను ఎలా అమలు చేయాలో చూద్దాం.

# [Python](#tab/python)

```python
# పైథాన్ ఉదాహరణ: అభ్యర్థన సందర్భం ఆధారంగా డైనమిక్ సాంప్లింగ్
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # వివిధ పనితీరుల కోసం సాంప్లింగ్ ప్రీసెట్స్ నిర్వచించండి
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # బేస్ ప్రీసెట్ ఎంచుకోండి
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # ఇచ్చినట్లయితే వాడుకరి ప్రాధాన్యతల ఆధారంగా సర్దుబాటు చేయండి
        if user_preferences:
            if "creativity_level" in user_preferences:
                # సృజనాత్మకత ప్రాధాన్యత (1-10) ఆధారంగా ఉష్ణోగ్రతను స్కేలు చేయండి
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # కావలసిన ప్రతిస్పందన వైవిధ్యం ఆధారంగా top_pను సర్దుబాటు చేయండి
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # కస్టమ్ సాంప్లింగ్ పారామితులతో అభ్యర్థనను సృష్టించి పంపండి
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # పారదర్శకత కోసం సాంప్లింగ్ మెటాడేటాతో సమాధానాన్ని తిరిగి ఇవ్వండి
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

పూర్వపు కోడ్‌లో మేము:

- అనుకూల శాంప్లింగ్‌ను నిర్వహించే `DynamicSamplingService` క్లాస్‌ను రూపొందించాము.
- వివిధ పనితీరు విధానాలకు (సృజనాత్మక, వాస్తవం, కోడ్, విశ్లేషణాత్మక) శాంప్లింగ్ ప్రీసెట్లను నిర్వచించాము.
- పనితీరు విధానం ఆధారంగా ప్రాథమిక శాంప్లింగ్ ప్రీసెట్‌ను ఎంచుకున్నాము.
- వినియోగదారు అభిరుచులు, ఉదాహరణకు సృజనాత్మక స్థాయి మరియు విభిన్నత ఆధారంగా శాంప్లింగ్ పారామితులను సర్దుబాటు చేసాము.
- డైనమిక్ గా కాన్ఫిగర్ చేయబడిన శాంప్లింగ్ పారామితులతో అభ్యర్థనను పంపించాము.
- సృష్టించబడిన టెక్స్టును, వర్తించిన శాంప్లింగ్ పారామితులు మరియు పనితీరు విధానంతో పాటు పారదర్శకత కోసం తిరిగి ఇచ్చాము.
- అవుట్‌పుట్ యొక్క విపరీతతను నియంత్రించడానికి nhiệtశక్తి ఉపయోగించాము, అధిక విలువలు మరింత సృజనాత్మక ప్రతిస్పందనలకు దారితీయగలవు.
- `top_p` ను టోకెన్ల ఎంపికను టాప్ సహస్రజన్యత సామ్యం ద్రవ్యాన్ని అందించే వాటిపై పరిమితం చేయడానికి ఉపయోగించి, సృష్టించిన టెక్స్టు గుణాత్మకతను పెంపొందించి.
- పునరావృతాన్ని తగ్గించడానికి మరియు అవుట్‌పుట్‌లో విభిన్నతను ప్రేరేపించడానికి `frequency_penalty` ఉపయోగించాము.
- వినియోగదారు నిర్వచించిన సృజనాత్మకత మరియు విభిన్నత స్థాయిల ఆధారంగా శాంప్లింగ్ పారామితుల అనుకూలీకరణకు `user_preferences` ఉపయోగించాము.
- అభ్యర్థనకు సరైన శాంప్లింగ్ వ్యూహాన్ని నిర్ధారించడానికి `task_type` ఉపయోగించాము, పనితీరు స్వభావం ఆధారంగా మరింత అనుకూల ప్రత్యుత్తరాలను ఇస్తుంది.
- కాన్ఫిగర్ చేసిన శాంప్లింగ్ పారామితులతో ప్రాంప్ట్ పంపడానికి `send_request` పద్ధతిని ఉపయోగించాము, నమూనా నిర్దిష్ట అవసరాల ప్రకారం టెక్స్టు సృష్టించేందుకు ఇది నిర్ధారిస్తుంది.
- నమూనా ప్రత్యుత్తరాన్ని పొందడానికి `generated_text` ఉపయోగించి, తరువాత విశ్లేషణ లేదా ప్రదర్శన కోసం శాంప్లింగ్ పారామితులు మరియు పనితీరు విధానంతో పాటు తిరిగి ఇచ్చాము.
- వినియోగదారు అభిరుచులు చెల్లుబాటు అయ్యే పరిధుల్లోనే ఉండేలా నిర్దారించడానికి `min` మరియు `max` ఫంక్షన్లను ఉపయోగించి, చెల్లని శాంప్లింగ్ కాన్ఫిగరేషన్లను నిరోధించాము.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// జావాస్క్రిప్ట్ ఉదాహరణ: వినియోగదారు సందర్భాన్ని ఆధారపడి డైనమిక్ శాంప్లింగ్ కాన్ఫిగరేషన్
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // ప్రాథమిక శాంప్లింగ్ ప్రొఫైல்கள் నిర్వచించండి
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // చారిత్రక పనితీరు ట్రాక్ చేయండి
    this.performanceHistory = [];
  }
  
  // ప్రాంప్ట్ నుండి టాస్క్ రకం గుర్తించండి
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // సులభమైన అంచనా గుర్తింపు - ఎం ఎల్ వర్గీకరణతో మెరుగుపరచవచ్చు
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
    
    // స్పష్టమైన రకం గుర్తించకపోతే డిఫాల్ట్ గా సంభాషణాత్మకంగా ఉంచండి
    return 'conversational';
  }
  
  // సందర్భం మరియు వినియోగదారు ఇష్టాలను ఆధారపడి శాంప్లింగ్ పారామితులను గణించండి
  getSamplingParameters(prompt, context = {}) {
    // టాస్క్ రకాన్ని గుర్తించండి
    const taskType = this.detectTaskType(prompt, context);
    
    // ప్రాథమిక ప్రొఫైల్ పొందండి
    let params = {...this.samplingProfiles[taskType]};
    
    // వినియోగదారు ఇష్టాల ఆధారంగా సర్దుబాటు చేయండి
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // 1-10 నుండి సరైన ఉష్ణోగ్రత పరిధికి స్కేలింగ్ చేయండి
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // ఎక్కువ ఖచ్చితత్వం అంటే తక్కువ టాప్‌పి (మరియు ఎక్కువ దృష్టి పెట్టడం)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // ఎక్కువ స్థిరత్వం అంటే తక్కువ శిక్షలు
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // పనితీరు చరిత్ర నుండి నేర్చుకున్న సర్దుబాట్లను వర్తింపజేయండి
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // సులభమైన అనుకూల తార్కికత - మరింత శ్రేస్టమైన అల్గోరిథములతో మెరుగుపర్చవచ్చు
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // ఇటీవల చరిత్ర మాత్రమే పరిగణించండి
    
    if (relevantHistory.length > 0) {
      // సగటు పనితీరు స్కోర్లు గణించండి
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // పనితీరు పరిమితికి క్రింద ఉంటే, పారామితులను సర్దుబాటు చేయండి
      if (avgScore < 0.7) {
        // సురక్షిత విలువల వైపు స్వల్ప సర్దుబాటు
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // భవిష్యత్ సర్దుబాట్ల కోసం పనితీరు రికార్డు చేయండి
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // ప్రతిస్పందన నాణ్యత యొక్క 0-1 రేటింగ్
    });
    
    // చరిత్ర పరిమాణాన్ని పరిమితం చేయండి
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // ఆప్టిమైజ్ చేయబడిన శాంప్లింగ్ పారామితులు పొందండి
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // ఆప్టిమైజ్ చేయబడిన పారామితులతో అభ్యర్థన పంపండి
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // వినియోగదారు ఫీడ్బాక్ ఇచ్చితే, భవిష్యత్ ఆప్టిమైజేషన్ కోసం రికార్డు చేయండి
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

// ఉదాహరణ వినియోగం
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // కస్టమ్ వినియోగదారు ఇష్టాలతో సృజనాత్మక పని
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // అధిక సృజనాత్మకత (1-10)
          consistency: 3  // తక్కువ స్థిరత్వం (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // కోడ్ జనరేషన్ పని
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // తక్కువ సృజనాత్మకత
          precision: 8,   // అధిక ఖచ్చితత్వం
          consistency: 9  // అధిక స్థిరత్వం
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

పూర్వపు కోడ్‌లో మేము:

- పనితీరు విధానం మరియు వినియోగదారు అభిరుచుల ఆధారంగా డైనమిక్ శాంప్లింగ్‌ను నిర్వహించే `AdaptiveSamplingManager` క్లాస్‌ను సృష్టించాము.
- వివిధ పనితీరు విధానాలకు (సృజనాత్మక, వాస్తవం, కోడ్, సంభాషణాత్మక) శాంప్లింగ్ ప్రొఫైళ్లను నిర్వచించాము.
- సాదా నియమాలకు పనితీరు విధానాన్ని ప్రాంప్ట్ నుండి గుర్తించడానికి ఒక పద్ధతిని అమలు చేశాము.
- గుర్తించిన పనితీరు విధానం మరియు వినియోగదారు అభిరుచుల ఆధారంగా శాంప్లింగ్ పారామితులను లెక్కించాము.
- శిక్షణాత్మక పనితీరు ఆధారంగా నేర్చుకున్న సర్దుబాటులను వర్తింపజేసి శాంప్లింగ్ పారామితులను మెరుగు పరచేందుకు ప్రయత్నించాము.
- భవిష్యత్తు సర్దుబాట్ల కోసం పనితీరు రికార్డ్ చేసాము, పూర్వ అనుభవాలనుండి సిస్టమ్ నేర్చుకునేందుకు అనుమతిస్తూ.
- డైనమిక్ గా కాన్ఫిగర్ చేసిన శాంప్లింగ్ పారామితులతో అభ్యర్థనలు పంపించి, వర్తించిన పారామితులు మరియు గుర్తించిన పనితీరు విధానం తో పాటు సృష్టించబడిన టెక్స్ట్‌ను తిరిగి ఇచ్చాము.
- క్రింది వాటిని ఉపయోగించాము:
    - `userPreferences` వినియోగదారు నిర్వచించిన సృజనాత్మకత, ఖచ్చితత్వం, మరియు స్థిరత్వ స్థాయిల ఆధారంగా శాంప్లింగ్ పారామితులను అనుకూలీకరించడానికి.
    - `detectTaskType` ప్రాంప్ట్ ఆధారంగా పనితీరు స్వభావాన్ని నిర్ణయించడానికి, మరింత అనుకూల ప్రత్యుత్తరాలను ఇవ్వడానికి.
    - `recordPerformance` సృష్టించబడిన ప్రతిస్పందనల పనితీరును నమోదు చేయడానికి, సిస్టమ్ పరిణామం మరియు మెరుగుదల కొరకు.
    - `applyLearnedAdjustments` చరిత్రాత్మక పనితీరు ఆధారంగా శాంప్లింగ్ పారామితులను మార్చడానికి, నమూనా అధిక-గుణాత్మక ప్రతిస్పందనలు సృష్టించడంలో దోహదం.
    - `generateResponse` అనుకూల శాంప్లింగ్‌తో ప్రతిస్పందన సృష్టించే మొత్తం ప్రక్రియను సంకలనంచేయడానికి, వేరే ప్రాంప్ట్‌లు మరియు సందర్భాలతో సులభంగా పిలవడానికి.
    - `allowedTools` నమూనా సృష్టించడం సమయంలో ఉపయోగించగల సాధనాలను నిర్దేశించడానికి, మరింత సందర్భ-అవగాహన కలిగిన ప్రతిస్పందనలకు అనుమతిస్తూ.
    - `feedbackScore` వినియోగదారులు సృష్టించబడిన ప్రతిస్పందన గుణం పై అభిప్రాయం చెప్పడానికి అనుమతించేలా, దీని ద్వారా నమూనా పనితీరులో మెరుగుదల సాధించవచ్చు.
    - `performanceHistory` గత పరస్పర చర్యల రికార్డును నిలుపుకోవడానికి, పూర్వ విజయాలు మరియు విఫలాలను చూసి సిస్టమ్ నేర్చుకునేందుకు.
    - `getSamplingParameters` అభ్యర్థన సందర్భం ఆధారంగా శాంప్లింగ్ పారామితులను డైనమిక్‌గా సర్దుబాటు చేయడానికి, నమూనా వర్చస్వనీయత మరియు స్పందనాత్మకత పెంచేందుకు.
    - `detectTaskType` ప్రాంప్ట్ ఆధారంగా పనితీరు విధానాన్ని వర్గీకరించడానికి, వివిధ రకాల అభ్యర్థనలకు సరిపోయే శాంప్లింగ్ వ్యూహాలను వర్తింపజేయడానికి.
    - `samplingProfiles` వివిధ పనితీరు విధానాలకి ప్రాథమిక శాంప్లింగ్ కాన్ఫిగరేషన్లను నిర్వచించడానికి, అభ్యర్థన స్వభావం ఆధారంగా వేగవంతమైన సర్దుబాటు కోసం.

---

## తర్వాత ఏమి ఉంటుంది

- [5.7 స్కేలింగ్](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->