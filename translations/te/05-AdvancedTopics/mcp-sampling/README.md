# మోడల్ కాంటెక్స్ట్ ప్రోటోకాల్‌లో శాంప్లింగ్

శాంప్లింగ్ అనేది శక్తివంతమైన MCP ఫీచర్, ఇది సర్వర్లు క్లయింట్ ద్వారా LLM పూర్తి చేయడాన్ని అభ్యర్థించడానికి అనుమతిస్తుంది, సురక్షత మరియు గోప్యతను కాపాడుతూ సున్నితమైన ఏజెంటిక్ ప్రవర్తనలను సాధించడానికి. సరైన శాంప్లింగ్ కాన్ఫిగరేషన్ ప్రతిస్పందన నాణ్యత మరియు పనితీరును గణనీయంగా మెరుగుపరుస్తుంది. MCP ఒక ప్రమాణీకృత మార్గాన్ని అందిస్తుంది, ఇది నమూనాలు నిర్దిష్ట పారామితులతో టెక్స్ట్‌ను ఎలా ఉత్పత్తి చేస్తాయో నియంత్రిస్తుంది, ఇవి యాదృచ్ఛికత, సృజనాత్మకత మరియు సారూప్యతను ప్రభావితం చేస్తాయి.

## పరిచయం

ఈ పాఠంలో, మేము MCP అభ్యర్థనలలో శాంప్లింగ్ పారామితులను ఎలా కాన్ఫిగర్ చేయాలో మరియు శాంప్లింగ్ యొక్క ప్రోటోకాల్ యాంత్రికతలను అర్థం చేసుకోబోతున్నాము.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం ముగిసిన తర్వాత, మీరు చేయగలుగుతారు:

- MCPలో అందుబాటులో ఉన్న ముఖ్యమైన శాంప్లింగ్ పారామితులను అర్థం చేసుకోవడం.
- వివిధ ఉపయోగాల కోసం శాంప్లింగ్ పారామితులను కాన్ఫిగర్ చేయడం.
- పునరుత్పాదక ఫలితాల కోసం నిర్దిష్ట శాంప్లింగ్‌ను అమలు చేయడం.
- సందర్భం మరియు వినియోగదారు ప్రాధాన్యతల ఆధారంగా శాంప్లింగ్ పారామితులను డైనమిక్‌గా సర్దుబాటు చేయడం.
- వివిధ సందర్భాలలో మోడల్ పనితీరును మెరుగుపరచడానికి శాంప్లింగ్ వ్యూహాలను వర్తింపజేయడం.
- MCP యొక్క క్లయింట్-సర్వర్ ప్రవాహంలో శాంప్లింగ్ ఎలా పనిచేస్తుందో అర్థం చేసుకోవడం.

## MCPలో శాంప్లింగ్ ఎలా పనిచేస్తుంది

MCPలో శాంప్లింగ్ ప్రవాహం ఈ దశలను అనుసరిస్తుంది:

1. సర్వర్ `sampling/createMessage` అభ్యర్థనను క్లయింట్‌కు పంపుతుంది
2. క్లయింట్ అభ్యర్థనను సమీక్షించి దాన్ని మార్చవచ్చు
3. క్లయింట్ LLM నుండి శాంపుల్ చేస్తుంది
4. క్లయింట్ పూర్తి చేయడాన్ని సమీక్షిస్తుంది
5. క్లయింట్ ఫలితాన్ని సర్వర్‌కు తిరిగి పంపుతుంది

ఈ మానవ-ఇన్-ది-లూప్ డిజైన్ వినియోగదారులు LLM చూసే మరియు ఉత్పత్తి చేసే విషయంపై నియంత్రణను కలిగి ఉండటానికి హామీ ఇస్తుంది.

## శాంప్లింగ్ పారామితుల అవలోకనం

MCP క్లయింట్ అభ్యర్థనలలో కాన్ఫిగర్ చేయగల శాంప్లింగ్ పారామితులను నిర్వచిస్తుంది:

| పారామితి | వివరణ | సాధారణ పరిధి |
|-----------|-------------|---------------|
| `temperature` | టోకెన్ ఎంపికలో యాదృచ్ఛికతను నియంత్రిస్తుంది | 0.0 - 1.0 |
| `maxTokens` | ఉత్పత్తి చేయవలసిన గరిష్ట టోకెన్ల సంఖ్య | పూర్తి సంఖ్య విలువ |
| `stopSequences` | ఎదురైనప్పుడు ఉత్పత్తిని ఆపే కస్టమ్ సీక్వెన్సులు | స్ట్రింగ్‌ల శ్రేణి |
| `metadata` | అదనపు ప్రొవైడర్-స్పెసిఫిక్ పారామితులు | JSON ఆబ్జెక్ట్ |

చాలా LLM ప్రొవైడర్లు `metadata` ఫీల్డ్ ద్వారా అదనపు పారామితులను మద్దతు ఇస్తారు, వీటిలో ఉండవచ్చు:

| సాధారణ విస్తరణ పారామితి | వివరణ | సాధారణ పరిధి |
|-----------|-------------|---------------|
| `top_p` | న్యూక్లియస్ శాంప్లింగ్ - టోకెన్లను టాప్ సమ్మిళిత సంభావ్యతకు పరిమితం చేస్తుంది | 0.0 - 1.0 |
| `top_k` | టోకెన్ ఎంపికను టాప్ K ఎంపికలకు పరిమితం చేస్తుంది | 1 - 100 |
| `presence_penalty` | ఇప్పటి వరకు టెక్స్ట్‌లో టోకెన్ల ఉనికిని ఆధారంగా శిక్షిస్తుంది | -2.0 - 2.0 |
| `frequency_penalty` | ఇప్పటి వరకు టెక్స్ట్‌లో టోకెన్ల తరచుదల ఆధారంగా శిక్షిస్తుంది | -2.0 - 2.0 |
| `seed` | పునరుత్పాదక ఫలితాల కోసం నిర్దిష్ట యాదృచ్ఛిక సీడ్ | పూర్తి సంఖ్య విలువ |

## ఉదాహరణ అభ్యర్థన ఫార్మాట్

ఇది MCPలో క్లయింట్ నుండి శాంప్లింగ్ అభ్యర్థించడానికి ఒక ఉదాహరణ:

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

క్లయింట్ పూర్తి ఫలితాన్ని తిరిగి ఇస్తుంది:

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
  - క్లయింట్లు వినియోగదారులకు ప్రతిపాదిత ప్రాంప్ట్ చూపించాలి
  - వినియోగదారులు ప్రాంప్ట్‌లను మార్చగలగాలి లేదా తిరస్కరించగలగాలి
  - సిస్టమ్ ప్రాంప్ట్‌లను ఫిల్టర్ చేయవచ్చు లేదా మార్చవచ్చు
  - సందర్భం చేర్చడం క్లయింట్ ద్వారా నియంత్రించబడుతుంది

- **పూర్తి చేయడాల కోసం**:
  - క్లయింట్లు వినియోగదారులకు పూర్తి చేయడాన్ని చూపించాలి
  - వినియోగదారులు పూర్తి చేయడాలను మార్చగలగాలి లేదా తిరస్కరించగలగాలి
  - క్లయింట్లు పూర్తి చేయడాలను ఫిల్టర్ చేయవచ్చు లేదా మార్చవచ్చు
  - వినియోగదారులు ఏ మోడల్ ఉపయోగించాలో నియంత్రిస్తారు

ఈ సూత్రాలతో, LLM ప్రొవైడర్లలో సాధారణంగా మద్దతు పొందే పారామితులపై దృష్టి సారించి వివిధ ప్రోగ్రామింగ్ భాషలలో శాంప్లింగ్‌ను ఎలా అమలు చేయాలో చూద్దాం.

## భద్రతా పరిగణనలు

MCPలో శాంప్లింగ్‌ను అమలు చేసే సమయంలో ఈ భద్రతా ఉత్తమ ఆచారాలను పరిగణించండి:

- **అన్ని సందేశ విషయాన్ని ధృవీకరించండి** క్లయింట్‌కు పంపించే ముందు
- **సున్నితమైన సమాచారాన్ని శుభ్రపరచండి** ప్రాంప్ట్‌లు మరియు పూర్తి చేయడాల నుండి
- **దుర్వినియోగం నివారించడానికి రేట్ పరిమితులను అమలు చేయండి**
- **అసాధారణ నమూనాల కోసం శాంప్లింగ్ వినియోగాన్ని పర్యవేక్షించండి**
- **సురక్షిత ప్రోటోకాల్స్ ఉపయోగించి డేటాను ట్రాన్సిట్‌లో ఎన్‌క్రిప్ట్ చేయండి**
- **సంబంధిత నియమావళుల ప్రకారం వినియోగదారు డేటా గోప్యతను నిర్వహించండి**
- **అనుగుణత మరియు భద్రత కోసం శాంప్లింగ్ అభ్యర్థనలను ఆడిట్ చేయండి**
- **సరైన పరిమితులతో ఖర్చు ప్రదర్శనను నియంత్రించండి**
- **శాంప్లింగ్ అభ్యర్థనలకు టైమౌట్‌లను అమలు చేయండి**
- **మోడల్ లోపాలను సరైన ప్రత్యామ్నాయాలతో సున్నితంగా నిర్వహించండి**

శాంప్లింగ్ పారామితులు భాషా నమూనాల ప్రవర్తనను సున్నితంగా సర్దుబాటు చేయడానికి అనుమతిస్తాయి, నిర్దిష్ట మరియు సృజనాత్మక అవుట్పుట్ల మధ్య కావలసిన సమతుల్యతను సాధించడానికి.

వివిధ ప్రోగ్రామింగ్ భాషలలో ఈ పారామితులను ఎలా కాన్ఫిగర్ చేయాలో చూద్దాం.

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

ముందటి కోడ్‌లో మేము:

- నిర్దిష్ట సర్వర్ URLతో MCP క్లయింట్‌ను సృష్టించాము.
- `temperature`, `top_p`, మరియు `top_k` వంటి శాంప్లింగ్ పారామితులతో అభ్యర్థనను కాన్ఫిగర్ చేసాము.
- అభ్యర్థనను పంపించి ఉత్పత్తి చేసిన టెక్స్ట్‌ను ప్రింట్ చేసాము.
- ఉపయోగించాము:
    - `allowedTools` మోడల్ ఉత్పత్తి సమయంలో ఉపయోగించగల టూల్స్‌ను నిర్దేశించడానికి. ఈ సందర్భంలో, సృజనాత్మక యాప్ ఆలోచనలను సృష్టించడంలో సహాయపడటానికి `ideaGenerator` మరియు `marketAnalyzer` టూల్స్‌ను అనుమతించాము.
    - `frequencyPenalty` మరియు `presencePenalty` అవుట్పుట్‌లో పునరావృతం మరియు వైవిధ్యాన్ని నియంత్రించడానికి.
    - `temperature` అవుట్పుట్ యాదృచ్ఛికతను నియంత్రించడానికి, ఎక్కువ విలువలు మరింత సృజనాత్మక ప్రతిస్పందనలకు దారితీస్తాయి.
    - `top_p` టోకెన్ల ఎంపికను టాప్ సమ్మిళిత సంభావ్యత మాస్కు వరకు పరిమితం చేయడానికి, ఉత్పత్తి టెక్స్ట్ నాణ్యతను మెరుగుపరచడానికి.
    - `top_k` మోడల్‌ను టాప్ K అత్యంత సంభావ్య టోకెన్లకు పరిమితం చేయడానికి, ఇది మరింత సారూప్యమైన ప్రతిస్పందనలను సృష్టించడంలో సహాయపడుతుంది.
    - `frequencyPenalty` మరియు `presencePenalty` ఉత్పత్తి టెక్స్ట్‌లో పునరావృతం తగ్గించడానికి మరియు వైవిధ్యాన్ని ప్రోత్సహించడానికి.

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// జావాస్క్రిప్ట్ ఉదాహరణ: ఉష్ణోగ్రత మరియు టాప్-పీ శాంప్లింగ్ కాన్ఫిగరేషన్
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // MCP క్లయింట్‌ను ప్రారంభించండి
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // వేర్వేరు శాంప్లింగ్ పారామితులతో అభ్యర్థనను కాన్ఫిగర్ చేయండి
  const creativeSampling = {
    temperature: 0.9,    // ఎక్కువ ఉష్ణోగ్రత = ఎక్కువ యాదృచ్ఛికత/సృజనాత్మకత
    topP: 0.92,          // టోకెన్లను టాప్ 92% సంభావ్యత మాస్‌తో పరిగణించండి
    frequencyPenalty: 0.6, // టోకెన్ సీక్వెన్స్ పునరావృతిని తగ్గించండి
    presencePenalty: 0.4   // ఇప్పటివరకు టెక్స్ట్‌లో కనిపించిన టోకెన్లను శిక్షించండి
  };
  
  const factualSampling = {
    temperature: 0.2,    // తక్కువ ఉష్ణోగ్రత = ఎక్కువ నిర్ణయాత్మక/వాస్తవిక
    topP: 0.85,          // కొంచెం ఎక్కువ కేంద్రీకృత టోకెన్ ఎంపిక
    frequencyPenalty: 0.2, // కనిష్ట పునరావృత శిక్ష
    presencePenalty: 0.1   // కనిష్ట ఉనికి శిక్ష
  };
  
  try {
    // వేర్వేరు శాంప్లింగ్ కాన్ఫిగరేషన్లతో రెండు అభ్యర్థనలను పంపండి
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

ముందటి కోడ్‌లో మేము:

- సర్వర్ URL మరియు API కీతో MCP క్లయింట్‌ను ప్రారంభించాము.
- సృజనాత్మక పనుల కోసం ఒకటి, వాస్తవిక పనుల కోసం మరొకటి అనే రెండు శాంప్లింగ్ పారామితుల సెట్‌లను కాన్ఫిగర్ చేసాము.
- ఈ కాన్ఫిగరేషన్లతో అభ్యర్థనలను పంపించి, ప్రతి పనికి మోడల్ నిర్దిష్ట టూల్స్ ఉపయోగించడానికి అనుమతించాము.
- వివిధ శాంప్లింగ్ పారామితుల ప్రభావాలను చూపించడానికి ఉత్పత్తి చేసిన ప్రతిస్పందనలను ప్రింట్ చేసాము.
- ఉపయోగించాము `allowedTools` మోడల్ ఉత్పత్తి సమయంలో ఉపయోగించగల టూల్స్‌ను నిర్దేశించడానికి. ఈ సందర్భంలో, సృజనాత్మక పనుల కోసం `ideaGenerator` మరియు `environmentalImpactTool`, వాస్తవిక పనుల కోసం `factChecker` మరియు `dataAnalysisTool` అనుమతించాము.
- `temperature` అవుట్పుట్ యాదృచ్ఛికతను నియంత్రించడానికి, ఎక్కువ విలువలు మరింత సృజనాత్మక ప్రతిస్పందనలకు దారితీస్తాయి.
- `top_p` టోకెన్ల ఎంపికను టాప్ సమ్మిళిత సంభావ్యత మాస్కు వరకు పరిమితం చేయడానికి, ఉత్పత్తి టెక్స్ట్ నాణ్యతను మెరుగుపరచడానికి.
- `frequencyPenalty` మరియు `presencePenalty` అవుట్పుట్‌లో పునరావృతం తగ్గించడానికి మరియు వైవిధ్యాన్ని ప్రోత్సహించడానికి.
- `top_k` మోడల్‌ను టాప్ K అత్యంత సంభావ్య టోకెన్లకు పరిమితం చేయడానికి, ఇది మరింత సారూప్యమైన ప్రతిస్పందనలను సృష్టించడంలో సహాయపడుతుంది.

---

## నిర్దిష్ట శాంప్లింగ్

సమానమైన అవుట్పుట్లను అవసరం చేసే అనువర్తనాల కోసం, నిర్దిష్ట శాంప్లింగ్ పునరుత్పాదక ఫలితాలను హామీ ఇస్తుంది. ఇది ఒక స్థిర యాదృచ్ఛిక సీడ్ ఉపయోగించి మరియు టెంపరేచర్‌ను సున్నాకు సెట్ చేయడం ద్వారా సాధించబడుతుంది.

వివిధ ప్రోగ్రామింగ్ భాషలలో నిర్దిష్ట శాంప్లింగ్‌ను ప్రదర్శించడానికి క్రింది నమూనా అమలును చూద్దాం.

# [Java](../../../../05-AdvancedTopics/mcp-sampling)

```java
// జావా ఉదాహరణ: స్థిరమైన సీడ్‌తో నిర్దిష్ట ప్రతిస్పందనలు
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // నిర్దిష్ట ఫలితాల కోసం స్థిరమైన సీడ్ ఉపయోగించడం
        
        // స్థిరమైన సీడ్‌తో మొదటి అభ్యర్థన
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // గరిష్ట నిర్దిష్టత కోసం శూన్య ఉష్ణోగ్రత
            .build();
            
        // అదే సీడ్‌తో రెండవ అభ్యర్థన
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // రెండు అభ్యర్థనలను అమలు చేయండి
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // అదే సీడ్ మరియు ఉష్ణోగ్రత=0 కారణంగా ప్రతిస్పందనలు సమానంగా ఉండాలి
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

ముందటి కోడ్‌లో మేము:

- నిర్దిష్ట సర్వర్ URLతో MCP క్లయింట్‌ను సృష్టించాము.
- ఒకే ప్రాంప్ట్, స్థిర సీడ్ మరియు సున్నా టెంపరేచర్‌తో రెండు అభ్యర్థనలను కాన్ఫిగర్ చేసాము.
- రెండు అభ్యర్థనలను పంపించి ఉత్పత్తి చేసిన టెక్స్ట్‌ను ప్రింట్ చేసాము.
- సమాధానాలు నిర్దిష్ట శాంప్లింగ్ కాన్ఫిగరేషన్ (ఒకే సీడ్ మరియు టెంపరేచర్) కారణంగా ఒకే విధంగా ఉన్నాయని ప్రదర్శించాము.
- `setSeed` ఉపయోగించి స్థిర యాదృచ్ఛిక సీడ్‌ను నిర్దేశించాము, ఇది మోడల్ ప్రతి సారి ఒకే ఇన్‌పుట్‌కు ఒకే అవుట్పుట్‌ను ఉత్పత్తి చేయడానికి హామీ ఇస్తుంది.
- గరిష్ట నిర్దిష్టత కోసం `temperature` ను సున్నాకు సెట్ చేసాము, అంటే మోడల్ ఎప్పుడూ యాదృచ్ఛికత లేకుండా అత్యంత సంభావ్యమైన తదుపరి టోకెన్‌ను ఎంచుకుంటుంది.

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// జావాస్క్రిప్ట్ ఉదాహరణ: సీడ్ నియంత్రణతో నిర్ణీత ప్రతిస్పందనలు
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
      temperature: 0.0  // గరిష్ట నిర్ణీతత్వం కోసం శూన్య ఉష్ణోగ్రత
    });
    
    // అదే సీడ్ మరియు ఉష్ణోగ్రతతో రెండవ అభ్యర్థన
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // వేరే సీడ్ కానీ అదే ఉష్ణోగ్రతతో మూడవ అభ్యర్థన
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

ముందటి కోడ్‌లో మేము:

- సర్వర్ URLతో MCP క్లయింట్‌ను ప్రారంభించాము.
- ఒకే ప్రాంప్ట్, స్థిర సీడ్ మరియు సున్నా టెంపరేచర్‌తో రెండు అభ్యర్థనలను కాన్ఫిగర్ చేసాము.
- రెండు అభ్యర్థనలను పంపించి ఉత్పత్తి చేసిన టెక్స్ట్‌ను ప్రింట్ చేసాము.
- సమాధానాలు నిర్దిష్ట శాంప్లింగ్ కాన్ఫిగరేషన్ (ఒకే సీడ్ మరియు టెంపరేచర్) కారణంగా ఒకే విధంగా ఉన్నాయని ప్రదర్శించాము.
- `seed` ఉపయోగించి స్థిర యాదృచ్ఛిక సీడ్‌ను నిర్దేశించాము, ఇది మోడల్ ప్రతి సారి ఒకే ఇన్‌పుట్‌కు ఒకే అవుట్పుట్‌ను ఉత్పత్తి చేయడానికి హామీ ఇస్తుంది.
- గరిష్ట నిర్దిష్టత కోసం `temperature` ను సున్నాకు సెట్ చేసాము, అంటే మోడల్ ఎప్పుడూ యాదృచ్ఛికత లేకుండా అత్యంత సంభావ్యమైన తదుపరి టోకెన్‌ను ఎంచుకుంటుంది.
- మూడవ అభ్యర్థన కోసం వేరే సీడ్ ఉపయోగించి, ఒకే ప్రాంప్ట్ మరియు టెంపరేచర్ ఉన్నప్పటికీ సీడ్ మార్చడం వలన వేరే అవుట్పుట్లు వస్తాయని చూపించాము.

---

## డైనమిక్ శాంప్లింగ్ కాన్ఫిగరేషన్

బుద్ధిమంతమైన శాంప్లింగ్ ప్రతి అభ్యర్థన యొక్క సందర్భం మరియు అవసరాల ఆధారంగా పారామితులను అనుకూలంగా మార్చుతుంది. అంటే, టాస్క్ రకం, వినియోగదారు ప్రాధాన్యతలు లేదా చారిత్రక పనితీరు ఆధారంగా `temperature`, `top_p`, మరియు శిక్షలను డైనమిక్‌గా సర్దుబాటు చేయడం.

వివిధ ప్రోగ్రామింగ్ భాషలలో డైనమిక్ శాంప్లింగ్‌ను ఎలా అమలు చేయాలో చూద్దాం.

# [Python](../../../../05-AdvancedTopics/mcp-sampling)

```python
# పైథాన్ ఉదాహరణ: అభ్యర్థన సందర్భం ఆధారంగా డైనమిక్ శాంప్లింగ్
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # వివిధ పనుల రకాల కోసం శాంప్లింగ్ ప్రీసెట్స్ నిర్వచించండి
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # బేస్ ప్రీసెట్ ఎంచుకోండి
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # అందించినట్లయితే వినియోగదారు ప్రాధాన్యతల ఆధారంగా సర్దుబాటు చేయండి
        if user_preferences:
            if "creativity_level" in user_preferences:
                # సృజనాత్మకత ప్రాధాన్యత (1-10) ఆధారంగా ఉష్ణోగ్రతను స్కేలు చేయండి
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # కావలసిన ప్రతిస్పందన వైవిధ్యాన్ని ఆధారంగా top_p సర్దుబాటు చేయండి
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # కస్టమ్ శాంప్లింగ్ పారామితులతో అభ్యర్థనను సృష్టించి పంపండి
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # పారదర్శకత కోసం శాంప్లింగ్ మెటాడేటాతో ప్రతిస్పందనను తిరిగి ఇవ్వండి
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

ముందటి కోడ్‌లో మేము:

- అనుకూల శాంప్లింగ్‌ను నిర్వహించే `DynamicSamplingService` క్లాస్‌ను సృష్టించాము.
- వివిధ టాస్క్ రకాల కోసం శాంప్లింగ్ ప్రీసెట్స్‌ను నిర్వచించాము (సృజనాత్మక, వాస్తవిక, కోడ్, విశ్లేషణాత్మక).
- టాస్క్ రకం ఆధారంగా ప్రాథమిక శాంప్లింగ్ ప్రీసెట్‌ను ఎంచుకున్నాము.
- వినియోగదారు ప్రాధాన్యతల ఆధారంగా శాంప్లింగ్ పారామితులను సర్దుబాటు చేసాము, ఉదాహరణకు సృజనాత్మకత స్థాయి మరియు వైవిధ్యం.
- డైనమిక్‌గా కాన్ఫిగర్ చేసిన శాంప్లింగ్ పారామితులతో అభ్యర్థనను పంపాము.
- పారదర్శకత కోసం ఉత్పత్తి చేసిన టెక్స్ట్‌ను, వర్తించిన శాంప్లింగ్ పారామితులను మరియు టాస్క్ రకాన్ని తిరిగి ఇచ్చాము.
- `temperature` ఉపయోగించి అవుట్పుట్ యాదృచ్ఛికతను నియంత్రించాము, ఎక్కువ విలువలు మరింత సృజనాత్మక ప్రతిస్పందనలకు దారితీస్తాయి.
- `top_p` టోకెన్ల ఎంపికను టాప్ సమ్మిళిత సంభావ్యత మాస్కు వరకు పరిమితం చేయడానికి ఉపయోగించాము, ఉత్పత్తి టెక్స్ట్ నాణ్యతను మెరుగుపరచడానికి.
- `frequency_penalty` పునరావృతం తగ్గించడానికి మరియు వైవిధ్యాన్ని ప్రోత్సహించడానికి ఉపయోగించాము.
- `user_preferences` వినియ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->