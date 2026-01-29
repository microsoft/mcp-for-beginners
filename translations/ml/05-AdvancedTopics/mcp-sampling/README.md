# മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോക്കോളിൽ സാമ്പ്ലിംഗ്

സാമ്പ്ലിംഗ് ഒരു ശക്തമായ MCP ഫീച്ചറാണ്, ഇത് സെർവറുകൾക്ക് ക്ലയന്റിലൂടെ LLM പൂർത്തീകരണങ്ങൾ അഭ്യർത്ഥിക്കാൻ അനുവദിക്കുന്നു, സുരക്ഷയും സ്വകാര്യതയും നിലനിർത്തിക്കൊണ്ട് സങ്കീർണ്ണമായ ഏജന്റിക് പെരുമാറ്റങ്ങൾ സജ്ജമാക്കുന്നു. ശരിയായ സാമ്പ്ലിംഗ് കോൺഫിഗറേഷൻ പ്രതികരണ ഗുണമേന്മയും പ്രകടനവും നിഗമനാത്മകമായി മെച്ചപ്പെടുത്താൻ കഴിയും. MCP മോഡലുകൾ ടെക്സ്റ്റ് സൃഷ്ടിക്കുന്ന വിധം നിയന്ത്രിക്കാൻ ഒരു സ്റ്റാൻഡേർഡൈസ്ഡ് മാർഗം നൽകുന്നു, ഇത് റാൻഡംനസ്, സൃഷ്ടിപരത്വം, ഏകോപനം എന്നിവയെ ബാധിക്കുന്ന പ്രത്യേക പാരാമീറ്ററുകളാണ്.

## പരിചയം

ഈ പാഠത്തിൽ, MCP അഭ്യർത്ഥനകളിൽ സാമ്പ്ലിംഗ് പാരാമീറ്ററുകൾ എങ്ങനെ കോൺഫിഗർ ചെയ്യാമെന്ന് പരിശോധിക്കുകയും സാമ്പ്ലിംഗിന്റെ അടിസ്ഥാന പ്രോട്ടോക്കോൾ മെക്കാനിസങ്ങൾ മനസ്സിലാക്കുകയും ചെയ്യും.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം അവസാനിക്കുമ്പോൾ, നിങ്ങൾക്ക് കഴിയും:

- MCP-യിൽ ലഭ്യമായ പ്രധാന സാമ്പ്ലിംഗ് പാരാമീറ്ററുകൾ മനസ്സിലാക്കുക.
- വ്യത്യസ്ത ഉപയോഗകേസുകൾക്കായി സാമ്പ്ലിംഗ് പാരാമീറ്ററുകൾ കോൺഫിഗർ ചെയ്യുക.
- പുനരുത്പാദനയോഗ്യമായ ഫലങ്ങൾക്കായി നിർണ്ണായക സാമ്പ്ലിംഗ് നടപ്പിലാക്കുക.
- കോൺടെക്സ്റ്റ്, ഉപയോക്തൃ ഇഷ്ടാനുസരണം സാമ്പ്ലിംഗ് പാരാമീറ്ററുകൾ ഡൈനാമിക് ആയി ക്രമീകരിക്കുക.
- വിവിധ സാഹചര്യങ്ങളിൽ മോഡൽ പ്രകടനം മെച്ചപ്പെടുത്താൻ സാമ്പ്ലിംഗ് തന്ത്രങ്ങൾ പ്രയോഗിക്കുക.
- MCP-യുടെ ക്ലയന്റ്-സെർവർ ഫ്ലോയിൽ സാമ്പ്ലിംഗ് എങ്ങനെ പ്രവർത്തിക്കുന്നു എന്ന് മനസ്സിലാക്കുക.

## MCP-യിൽ സാമ്പ്ലിംഗ് എങ്ങനെ പ്രവർത്തിക്കുന്നു

MCP-യിലെ സാമ്പ്ലിംഗ് പ്രവാഹം ഈ ഘട്ടങ്ങൾ പിന്തുടരുന്നു:

1. സെർവർ `sampling/createMessage` അഭ്യർത്ഥന ക്ലയന്റിലേക്ക് അയയ്ക്കുന്നു
2. ക്ലയന്റ് അഭ്യർത്ഥന പരിശോധിച്ച് അതിൽ മാറ്റങ്ങൾ വരുത്താം
3. ക്ലയന്റ് LLM-യിൽ നിന്ന് സാമ്പിൾ എടുക്കുന്നു
4. ക്ലയന്റ് പൂർത്തീകരണം പരിശോധിക്കുന്നു
5. ക്ലയന്റ് ഫലം സെർവറിലേക്ക് തിരികെ നൽകുന്നു

ഈ മനുഷ്യൻ-ഇൻ-ദി-ലൂപ്പ് ഡിസൈൻ ഉപയോക്താക്കൾക്ക് LLM കാണുന്നതും സൃഷ്ടിക്കുന്നതും നിയന്ത്രിക്കാൻ സഹായിക്കുന്നു.

## സാമ്പ്ലിംഗ് പാരാമീറ്ററുകളുടെ അവലോകനം

MCP ക്ലയന്റ് അഭ്യർത്ഥനകളിൽ കോൺഫിഗർ ചെയ്യാവുന്ന താഴെപ്പറയുന്ന സാമ്പ്ലിംഗ് പാരാമീറ്ററുകൾ നിർവചിക്കുന്നു:

| പാരാമീറ്റർ | വിവരണം | സാധാരണ പരിധി |
|-----------|-------------|---------------|
| `temperature` | ടോക്കൺ തിരഞ്ഞെടുപ്പിൽ റാൻഡംനസ് നിയന്ത്രിക്കുന്നു | 0.0 - 1.0 |
| `maxTokens` | സൃഷ്ടിക്കാവുന്ന പരമാവധി ടോക്കണുകളുടെ എണ്ണം | പൂർണ്ണസംഖ്യ മൂല്യം |
| `stopSequences` | കണ്ടാൽ സൃഷ്ടി നിർത്തുന്ന കസ്റ്റം സീക്വൻസുകൾ | സ്ട്രിംഗ് ലിസ്റ്റ് |
| `metadata` | അധിക പ്രൊവൈഡർ-സ്പെസിഫിക് പാരാമീറ്ററുകൾ | JSON ഒബ്ജക്റ്റ് |

അധിക LLM പ്രൊവൈഡർമാർ `metadata` ഫീൽഡിലൂടെ താഴെപ്പറയുന്ന അധിക പാരാമീറ്ററുകൾ പിന്തുണയ്ക്കാം:

| സാധാരണ വിപുലീകരണ പാരാമീറ്റർ | വിവരണം | സാധാരണ പരിധി |
|-----------|-------------|---------------|
| `top_p` | ന്യൂക്ലിയസ് സാമ്പ്ലിംഗ് - ടോക്കണുകൾ ടോപ്പ് ക്യൂമുലേറ്റീവ് പ്രൊബബിലിറ്റിക്ക് പരിധി വയ്ക്കുന്നു | 0.0 - 1.0 |
| `top_k` | ടോക്കൺ തിരഞ്ഞെടുപ്പ് ടോപ്പ് K ഓപ്ഷനുകളിലേക്കു പരിമിതപ്പെടുത്തുന്നു | 1 - 100 |
| `presence_penalty` | ഇതുവരെ ടെക്സ്റ്റിൽ ഉള്ള ടോക്കണുകളുടെ സാന്നിധ്യത്തെ അടിസ്ഥാനമാക്കി പിഴവ് നൽകുന്നു | -2.0 - 2.0 |
| `frequency_penalty` | ഇതുവരെ ടെക്സ്റ്റിൽ ടോക്കണുകളുടെ ആവൃത്തി അടിസ്ഥാനമാക്കി പിഴവ് നൽകുന്നു | -2.0 - 2.0 |
| `seed` | പുനരുത്പാദനയോഗ്യമായ ഫലങ്ങൾക്ക് പ്രത്യേക റാൻഡം സീഡ് | പൂർണ്ണസംഖ്യ മൂല്യം |

## ഉദാഹരണ അഭ്യർത്ഥന ഫോർമാറ്റ്

MCP-യിൽ ക്ലയന്റിൽ നിന്ന് സാമ്പ്ലിംഗ് അഭ്യർത്ഥിക്കുന്ന ഉദാഹരണം:

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

## പ്രതികരണ ഫോർമാറ്റ്

ക്ലയന്റ് പൂർത്തീകരണ ഫലം തിരികെ നൽകുന്നു:

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

## മനുഷ്യൻ-ഇൻ-ദി-ലൂപ്പ് നിയന്ത്രണങ്ങൾ

MCP സാമ്പ്ലിംഗ് മനുഷ്യൻ മേൽനോട്ടത്തോടെ രൂപകൽപ്പന ചെയ്തിരിക്കുന്നു:

- **പ്രോംപ്റ്റുകൾക്കായി**:
  - ക്ലയന്റുകൾ ഉപയോക്താക്കൾക്ക് നിർദ്ദേശിച്ച പ്രോംപ്റ്റ് കാണിക്കണം
  - ഉപയോക്താക്കൾക്ക് പ്രോംപ്റ്റുകൾ മാറ്റാനും നിരസിക്കാനും കഴിയണം
  - സിസ്റ്റം പ്രോംപ്റ്റുകൾ ഫിൽട്ടർ ചെയ്യുകയോ മാറ്റുകയോ ചെയ്യാം
  - കോൺടെക്സ്റ്റ് ഉൾപ്പെടുത്തൽ ക്ലയന്റ് നിയന്ത്രിക്കുന്നു

- **പൂർത്തീകരണങ്ങൾക്കായി**:
  - ക്ലയന്റുകൾ ഉപയോക്താക്കൾക്ക് പൂർത്തീകരണം കാണിക്കണം
  - ഉപയോക്താക്കൾക്ക് പൂർത്തീകരണം മാറ്റാനും നിരസിക്കാനും കഴിയണം
  - ക്ലയന്റുകൾ പൂർത്തീകരണങ്ങൾ ഫിൽട്ടർ ചെയ്യുകയോ മാറ്റുകയോ ചെയ്യാം
  - ഉപയോക്താക്കൾ ഉപയോഗിക്കുന്ന മോഡൽ നിയന്ത്രിക്കുന്നു

ഈ സിദ്ധാന്തങ്ങൾ മനസ്സിലാക്കി, LLM പ്രൊവൈഡർമാർ സാധാരണ പിന്തുണയ്ക്കുന്ന പാരാമീറ്ററുകളെ കേന്ദ്രീകരിച്ച് വ്യത്യസ്ത പ്രോഗ്രാമിംഗ് ഭാഷകളിൽ സാമ്പ്ലിംഗ് എങ്ങനെ നടപ്പിലാക്കാമെന്ന് നോക്കാം.

## സുരക്ഷാ പരിഗണനകൾ

MCP-യിൽ സാമ്പ്ലിംഗ് നടപ്പിലാക്കുമ്പോൾ ഈ സുരക്ഷാ മികച്ച പ്രാക്ടീസുകൾ പരിഗണിക്കുക:

- **എല്ലാ സന്ദേശ ഉള്ളടക്കവും സാധുത പരിശോധിക്കുക** ക്ലയന്റിലേക്ക് അയയ്ക്കുന്നതിന് മുമ്പ്
- **പ്രോംപ്റ്റുകളും പൂർത്തീകരണങ്ങളും നിന്നുള്ള സങ്കീർണ്ണ വിവരങ്ങൾ ശുദ്ധീകരിക്കുക**
- **ദുരുപയോഗം തടയാൻ നിരക്ക് പരിധികൾ നടപ്പിലാക്കുക**
- **അസാധാരണ മാതൃകകൾക്കായി സാമ്പ്ലിംഗ് ഉപയോഗം നിരീക്ഷിക്കുക**
- **സുരക്ഷിത പ്രോട്ടോക്കോളുകൾ ഉപയോഗിച്ച് ഡാറ്റ ട്രാൻസിറ്റിൽ എൻക്രിപ്റ്റ് ചെയ്യുക**
- **പ്രസക്തമായ നിയമങ്ങൾ അനുസരിച്ച് ഉപയോക്തൃ ഡാറ്റ സ്വകാര്യത കൈകാര്യം ചെയ്യുക**
- **അനുസരണവും സുരക്ഷയും ഉറപ്പാക്കാൻ സാമ്പ്ലിംഗ് അഭ്യർത്ഥനകൾ ഓഡിറ്റ് ചെയ്യുക**
- **ചെലവ് നിയന്ത്രണത്തിന് അനുയോജ്യമായ പരിധികൾ നിയന്ത്രിക്കുക**
- **സാമ്പ്ലിംഗ് അഭ്യർത്ഥനകൾക്ക് ടൈംഔട്ടുകൾ നടപ്പിലാക്കുക**
- **മോഡൽ പിശകുകൾ സുഖപ്രദമായി കൈകാര്യം ചെയ്യുക, അനുയോജ്യമായ ഫാൾബാക്കുകൾ ഉപയോഗിച്ച്**

സാമ്പ്ലിംഗ് പാരാമീറ്ററുകൾ ഭാഷാ മോഡലുകളുടെ പെരുമാറ്റം സൂക്ഷ്മമായി ക്രമീകരിക്കാൻ അനുവദിക്കുന്നു, നിർണ്ണായകവും സൃഷ്ടിപരവുമായ ഔട്ട്പുട്ടുകൾക്കിടയിൽ ആവശ്യമായ ബാലൻസ് നേടാൻ.

വ്യത്യസ്ത പ്രോഗ്രാമിംഗ് ഭാഷകളിൽ ഈ പാരാമീറ്ററുകൾ എങ്ങനെ കോൺഫിഗർ ചെയ്യാമെന്ന് നോക്കാം.

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

മുൻകൂട്ടി നൽകിയ കോഡിൽ ഞങ്ങൾ:

- ഒരു പ്രത്യേക സെർവർ URL ഉപയോഗിച്ച് MCP ക്ലയന്റ് സൃഷ്ടിച്ചു.
- `temperature`, `top_p`, `top_k` പോലുള്ള സാമ്പ്ലിംഗ് പാരാമീറ്ററുകൾ ഉപയോഗിച്ച് അഭ്യർത്ഥന കോൺഫിഗർ ചെയ്തു.
- അഭ്യർത്ഥന അയച്ച് സൃഷ്ടിച്ച ടെക്സ്റ്റ് പ്രിന്റ് ചെയ്തു.
- ഉപയോഗിച്ചത്:
    - `allowedTools` മോഡൽ സൃഷ്ടിക്കുമ്പോൾ ഉപയോഗിക്കാവുന്ന ടൂളുകൾ വ്യക്തമാക്കാൻ. ഈ കേസിൽ, സൃഷ്ടിപരമായ ആപ്പ് ആശയങ്ങൾ സൃഷ്ടിക്കാൻ `ideaGenerator`യും `marketAnalyzer`യും അനുവദിച്ചു.
    - `frequencyPenalty`യും `presencePenalty`യും ആവർത്തനവും വൈവിധ്യവും നിയന്ത്രിക്കാൻ.
    - `temperature` ഔട്ട്പുട്ടിന്റെ റാൻഡംനസ് നിയന്ത്രിക്കാൻ, ഉയർന്ന മൂല്യങ്ങൾ കൂടുതൽ സൃഷ്ടിപരമായ പ്രതികരണങ്ങൾക്കായി.
    - `top_p` ടോക്കണുകൾ ടോപ്പ് ക്യൂമുലേറ്റീവ് പ്രൊബബിലിറ്റി മാസ്സിൽ ഉൾപ്പെടുന്നവയാക്കി പരിധി വയ്ക്കാൻ, സൃഷ്ടിച്ച ടെക്സ്റ്റിന്റെ ഗുണമേന്മ മെച്ചപ്പെടുത്താൻ.
    - `top_k` മോഡലിനെ ടോപ്പ് K ഏറ്റവും സാധ്യതയുള്ള ടോക്കണുകളിലേക്കു പരിമിതപ്പെടുത്താൻ, കൂടുതൽ ഏകോപിത പ്രതികരണങ്ങൾക്കായി.
    - `frequencyPenalty`യും `presencePenalty`യും ആവർത്തന കുറയ്ക്കാനും വൈവിധ്യം പ്രോത്സാഹിപ്പിക്കാനും.

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// ജാവാസ്ക്രിപ്റ്റ് ഉദാഹരണം: താപനിലയും ടോപ്പ്-പി സാമ്പിളിംഗ് കോൺഫിഗറേഷൻ
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // MCP ക്ലയന്റ് ആരംഭിക്കുക
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // വ്യത്യസ്ത സാമ്പിളിംഗ് പാരാമീറ്ററുകളോടെ അഭ്യർത്ഥന കോൺഫിഗർ ചെയ്യുക
  const creativeSampling = {
    temperature: 0.9,    // ഉയർന്ന താപനില = കൂടുതൽ യാദൃച്ഛികത/സൃഷ്ടിപരത്വം
    topP: 0.92,          // ടോക്കണുകൾ ടോപ്പ് 92% സാധ്യതാ ഭാരം പരിഗണിക്കുക
    frequencyPenalty: 0.6, // ടോക്കൺ ക്രമങ്ങളുടെ ആവർത്തനം കുറയ്ക്കുക
    presencePenalty: 0.4   // ഇതുവരെ ടെക്സ്റ്റിൽ പ്രത്യക്ഷപ്പെട്ട ടോക്കണുകൾക്ക് ശിക്ഷ നൽകുക
  };
  
  const factualSampling = {
    temperature: 0.2,    // താഴ്ന്ന താപനില = കൂടുതൽ നിർണ്ണായകമായ/വാസ്തവപരമായ
    topP: 0.85,          // അല്പം കൂടുതൽ കേന്ദ്രീകൃത ടോക്കൺ തിരഞ്ഞെടുപ്പ്
    frequencyPenalty: 0.2, // കുറഞ്ഞ ആവർത്തന ശിക്ഷ
    presencePenalty: 0.1   // കുറഞ്ഞ സാന്നിധ്യ ശിക്ഷ
  };
  
  try {
    // വ്യത്യസ്ത സാമ്പിളിംഗ് കോൺഫിഗറേഷനുകളോടെ രണ്ട് അഭ്യർത്ഥനകൾ അയയ്ക്കുക
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

മുൻകൂട്ടി നൽകിയ കോഡിൽ ഞങ്ങൾ:

- സെർവർ URL, API കീ ഉപയോഗിച്ച് MCP ക്ലയന്റ് ആരംഭിച്ചു.
- സൃഷ്ടിപരമായ ജോലികൾക്കും വാസ്തവപരമായ ജോലികൾക്കും രണ്ട് സെറ്റ് സാമ്പ്ലിംഗ് പാരാമീറ്ററുകൾ കോൺഫിഗർ ചെയ്തു.
- ഈ കോൺഫിഗറേഷനുകളോടെ അഭ്യർത്ഥനകൾ അയച്ചു, ഓരോ ജോലിക്കും മോഡൽ പ്രത്യേക ടൂളുകൾ ഉപയോഗിക്കാൻ അനുവദിച്ചു.
- വ്യത്യസ്ത സാമ്പ്ലിംഗ് പാരാമീറ്ററുകളുടെ ഫലങ്ങൾ കാണിക്കാൻ സൃഷ്ടിച്ച പ്രതികരണങ്ങൾ പ്രിന്റ് ചെയ്തു.
- ഉപയോഗിച്ചത് `allowedTools` മോഡൽ സൃഷ്ടിക്കുമ്പോൾ ഉപയോഗിക്കാവുന്ന ടൂളുകൾ വ്യക്തമാക്കാൻ. ഈ കേസിൽ, സൃഷ്ടിപര ജോലികൾക്കായി `ideaGenerator`യും `environmentalImpactTool`യും, വാസ്തവപര ജോലികൾക്കായി `factChecker`യും `dataAnalysisTool`ഉം അനുവദിച്ചു.
- `temperature` ഔട്ട്പുട്ടിന്റെ റാൻഡംനസ് നിയന്ത്രിക്കാൻ, ഉയർന്ന മൂല്യങ്ങൾ കൂടുതൽ സൃഷ്ടിപരമായ പ്രതികരണങ്ങൾക്കായി.
- `top_p` ടോക്കണുകൾ ടോപ്പ് ക്യൂമുലേറ്റീവ് പ്രൊബബിലിറ്റി മാസ്സിൽ ഉൾപ്പെടുന്നവയാക്കി പരിധി വയ്ക്കാൻ, സൃഷ്ടിച്ച ടെക്സ്റ്റിന്റെ ഗുണമേന്മ മെച്ചപ്പെടുത്താൻ.
- `frequencyPenalty`യും `presencePenalty`യും ആവർത്തന കുറയ്ക്കാനും വൈവിധ്യം പ്രോത്സാഹിപ്പിക്കാനും.
- `top_k` മോഡലിനെ ടോപ്പ് K ഏറ്റവും സാധ്യതയുള്ള ടോക്കണുകളിലേക്കു പരിമിതപ്പെടുത്താൻ, കൂടുതൽ ഏകോപിത പ്രതികരണങ്ങൾക്കായി.

---

## നിർണ്ണായക സാമ്പ്ലിംഗ്

സ്ഥിരമായ ഔട്ട്പുട്ടുകൾ ആവശ്യമായ ആപ്ലിക്കേഷനുകൾക്കായി, നിർണ്ണായക സാമ്പ്ലിംഗ് പുനരുത്പാദനയോഗ്യമായ ഫലങ്ങൾ ഉറപ്പാക്കുന്നു. ഇത് ഒരു നിശ്ചിത റാൻഡം സീഡ് ഉപയോഗിച്ച്, `temperature` നുള്ള മൂല്യം പൂജ്യം ആക്കിയാണ് സാധ്യമാക്കുന്നത്.

വ്യത്യസ്ത പ്രോഗ്രാമിംഗ് ഭാഷകളിൽ നിർണ്ണായക സാമ്പ്ലിംഗ് കാണിക്കുന്ന ഉദാഹരണ നടപ്പാക്കൽ താഴെ കാണാം.

# [Java](../../../../05-AdvancedTopics/mcp-sampling)

```java
// ജാവ ഉദാഹരണം: നിശ്ചിത വിത്തുമായി നിർണ്ണായക പ്രതികരണങ്ങൾ
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // നിർണ്ണായക ഫലങ്ങൾക്ക് നിശ്ചിത വിത്ത് ഉപയോഗിക്കുന്നു
        
        // നിശ്ചിത വിത്തോടെ ആദ്യ അഭ്യർത്ഥന
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // പരമാവധി നിർണ്ണായകതയ്ക്കായി ശൂന്യ താപനില
            .build();
            
        // അതേ വിത്തോടെ രണ്ടാം അഭ്യർത്ഥന
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // ഇരുവരുടെയും അഭ്യർത്ഥനകൾ നടപ്പിലാക്കുക
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // ഒരേ വിത്തും താപനില=0 ഉം കാരണം പ്രതികരണങ്ങൾ സമാനമായിരിക്കണം
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

മുൻകൂട്ടി നൽകിയ കോഡിൽ ഞങ്ങൾ:

- ഒരു നിർദ്ദിഷ്ട സെർവർ URL ഉപയോഗിച്ച് MCP ക്ലയന്റ് സൃഷ്ടിച്ചു.
- ഒരേ പ്രോംപ്റ്റ്, നിശ്ചിത സീഡ്, പൂജ്യം `temperature` ഉപയോഗിച്ച് രണ്ട് അഭ്യർത്ഥനകൾ കോൺഫിഗർ ചെയ്തു.
- രണ്ട് അഭ്യർത്ഥനകളും അയച്ച് സൃഷ്ടിച്ച ടെക്സ്റ്റ് പ്രിന്റ് ചെയ്തു.
- സാമ്പ്ലിംഗ് കോൺഫിഗറേഷന്റെ നിർണ്ണായക സ്വഭാവം (ഒരേ സീഡ്, ഒരേ `temperature`) കാരണം പ്രതികരണങ്ങൾ ഒരുപോലെയാണ് എന്ന് തെളിയിച്ചു.
- `setSeed` ഉപയോഗിച്ച് നിശ്ചിത റാൻഡം സീഡ് വ്യക്തമാക്കി, ഒരേ ഇൻപുട്ടിനായി ഒരേ ഔട്ട്പുട്ട് സൃഷ്ടിക്കാനായി.
- `temperature` പൂജ്യം ആക്കി, പരമാവധി നിർണ്ണായകത ഉറപ്പാക്കാൻ, മോഡൽ എപ്പോഴും ഏറ്റവും സാധ്യതയുള്ള അടുത്ത ടോക്കൺ തിരഞ്ഞെടുക്കും.

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// ജാവാസ്ക്രിപ്റ്റ് ഉദാഹരണം: സീഡ് നിയന്ത്രണത്തോടെ നിർണായക പ്രതികരണങ്ങൾ
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // സ്ഥിരമായ സീഡോടെ ആദ്യ അഭ്യർത്ഥന
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // പരമാവധി നിർണായകതയ്ക്കായി പൂജ്യം താപനില
    });
    
    // ഒരേ സീഡും താപനിലയും ഉപയോഗിച്ച് രണ്ടാം അഭ്യർത്ഥന
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // വ്യത്യസ്ത സീഡും ഒരേ താപനിലയും ഉപയോഗിച്ച് മൂന്നാം അഭ്യർത്ഥന
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

മുൻകൂട്ടി നൽകിയ കോഡിൽ ഞങ്ങൾ:

- സെർവർ URL ഉപയോഗിച്ച് MCP ക്ലയന്റ് ആരംഭിച്ചു.
- ഒരേ പ്രോംപ്റ്റ്, നിശ്ചിത സീഡ്, പൂജ്യം `temperature` ഉപയോഗിച്ച് രണ്ട് അഭ്യർത്ഥനകൾ കോൺഫിഗർ ചെയ്തു.
- രണ്ട് അഭ്യർത്ഥനകളും അയച്ച് സൃഷ്ടിച്ച ടെക്സ്റ്റ് പ്രിന്റ് ചെയ്തു.
- സാമ്പ്ലിംഗ് കോൺഫിഗറേഷന്റെ നിർണ്ണായക സ്വഭാവം (ഒരേ സീഡ്, ഒരേ `temperature`) കാരണം പ്രതികരണങ്ങൾ ഒരുപോലെയാണ് എന്ന് തെളിയിച്ചു.
- `seed` ഉപയോഗിച്ച് നിശ്ചിത റാൻഡം സീഡ് വ്യക്തമാക്കി, ഒരേ ഇൻപുട്ടിനായി ഒരേ ഔട്ട്പുട്ട് സൃഷ്ടിക്കാനായി.
- `temperature` പൂജ്യം ആക്കി, പരമാവധി നിർണ്ണായകത ഉറപ്പാക്കാൻ, മോഡൽ എപ്പോഴും ഏറ്റവും സാധ്യതയുള്ള അടുത്ത ടോക്കൺ തിരഞ്ഞെടുക്കും.
- മൂന്നാം അഭ്യർത്ഥനയ്ക്ക് വ്യത്യസ്ത സീഡ് ഉപയോഗിച്ച്, ഒരേ പ്രോംപ്റ്റും `temperature`യും ഉള്ളപ്പോൾ സീഡ് മാറ്റിയാൽ വ്യത്യസ്ത ഔട്ട്പുട്ടുകൾ ഉണ്ടാകുമെന്ന് കാണിച്ചു.

---

## ഡൈനാമിക് സാമ്പ്ലിംഗ് കോൺഫിഗറേഷൻ

ബുദ്ധിമുട്ടുള്ള സാമ്പ്ലിംഗ് ഓരോ അഭ്യർത്ഥനയുടെ കോൺടെക്സ്റ്റ്, ആവശ്യകതകൾ അനുസരിച്ച് പാരാമീറ്ററുകൾ ക്രമീകരിക്കുന്നു. അതായത്, ജോലിയുടെ തരം, ഉപയോക്തൃ ഇഷ്ടങ്ങൾ, ചരിത്ര പ്രകടനം എന്നിവയുടെ അടിസ്ഥാനത്തിൽ `temperature`, `top_p`, പിഴവുകൾ എന്നിവ ഡൈനാമിക് ആയി ക്രമീകരിക്കുന്നു.

വ്യത്യസ്ത പ്രോഗ്രാമിംഗ് ഭാഷകളിൽ ഡൈനാമിക് സാമ്പ്ലിംഗ് എങ്ങനെ നടപ്പിലാക്കാമെന്ന് നോക്കാം.

# [Python](../../../../05-AdvancedTopics/mcp-sampling)

```python
# പൈതൺ ഉദാഹരണം: അഭ്യർത്ഥനാ സാഹചര്യത്തിന്റെ അടിസ്ഥാനത്തിൽ ഡൈനാമിക് സാമ്പ്ലിംഗ്
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # വ്യത്യസ്ത ടാസ്‌ക് തരംകൾക്കായി സാമ്പ്ലിംഗ് പ്രീസെറ്റുകൾ നിർവചിക്കുക
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # അടിസ്ഥാന പ്രീസെറ്റ് തിരഞ്ഞെടുക്കുക
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # ഉപയോക്തൃ ഇഷ്ടാനുസരണം ക്രമീകരിക്കുക, നൽകിയിട്ടുണ്ടെങ്കിൽ
        if user_preferences:
            if "creativity_level" in user_preferences:
                # സൃഷ്ടിപരത്വ ഇഷ്ടാനുസരണം (1-10) താപനില സ്കെയിൽ ചെയ്യുക
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # ആവശ്യമായ പ്രതികരണ വൈവിധ്യം അടിസ്ഥാനമാക്കി top_p ക്രമീകരിക്കുക
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # കസ്റ്റം സാമ്പ്ലിംഗ് പാരാമീറ്ററുകളോടെ അഭ്യർത്ഥന സൃഷ്ടിച്ച് അയയ്ക്കുക
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # പാരദർശിത്വത്തിനായി സാമ്പ്ലിംഗ് മെറ്റാഡേറ്റയോടുകൂടിയ പ്രതികരണം തിരികെ നൽകുക
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

മുൻകൂട്ടി നൽകിയ കോഡിൽ ഞങ്ങൾ:

- അഡാപ്റ്റീവ് സാമ്പ്ലിംഗ് കൈകാര്യം ചെയ്യുന്ന `DynamicSamplingService` ക്ലാസ് സൃഷ്ടിച്ചു.
- വ്യത്യസ്ത ജോലിതരം (സൃഷ്ടിപര, വാസ്തവപര, കോഡ്, വിശകലന) എന്നിവയ്ക്ക് സാമ്പ്ലിംഗ് പ്രീസെറ്റുകൾ നിർവചിച്ചു.
- ജോലിതരം അടിസ്ഥാനമാക്കി അടിസ്ഥാന സാമ്പ്ലിംഗ് പ്രീസെറ്റ് തിരഞ്ഞെടുക്കുന്നു.
- ഉപയോക്തൃ ഇഷ്ടാനുസരണം സൃഷ്ടിപരത്വം, വൈവിധ്യം എന്നിവയുടെ അടിസ്ഥാനത്തിൽ സാമ്പ്ലിംഗ് പാരാമീറ്ററുകൾ ക്രമീകരിച്ചു.
- ഡൈനാമിക് കോൺഫിഗർ ചെയ്ത സാമ്പ്ലിംഗ് പാരാമീറ്ററുകളോടെ അഭ്യർത്ഥന അയച്ചു.
- സൃഷ്ടിച്ച ടെക്സ്റ്റും പ്രയോഗിച്ച സാമ്പ്ലിംഗ് പാരാമീറ്ററുകളും ജോലിതരവും തിരിച്ചുവിട്ടു, വ്യക്തതക്കായി.
- `temperature` ഔട്ട്പുട്ടിന്റെ റാൻഡംനസ് നിയന്ത്രിക്കാൻ, ഉയർന്ന മൂല്യങ്ങൾ കൂടുതൽ സൃഷ്ടിപരമായ പ്രതികരണങ്ങൾക്കായി.
- `top_p` ടോക്കണുകൾ ടോപ്പ് ക്യൂമുലേറ്റീവ് പ്രൊബബിലിറ്റി മാസ്സിൽ ഉൾപ്പെടുന്നവയാക്കി പരിധി വയ്ക്കാൻ, സൃഷ്ടിച്ച ടെക്സ്റ്റിന്റെ ഗുണമേന്മ മെച്ചപ്പെടുത്താൻ.
- `frequency_penalty` ആവർത്തന കുറയ്ക്കാനും വൈവിധ്യം പ്രോത്സാഹിപ്പിക്കാനും.
- `user_preferences` ഉപയോക്തൃ നിർവചിച്ച സൃഷ്ടിപരത്വം, വൈവിധ്യം തലങ്ങൾ അടിസ്ഥാനമാക്കി സാമ്പ്ലിംഗ് പാരാമീറ്ററുകൾ ഇഷ്ടാനുസരിച്ച് ക്രമീകരിക്കാൻ.
- `task_type` അഭ്യർത്ഥനയ്ക്ക് അനുയോജ്യമായ സാമ്പ്ലിംഗ് തന്ത്രം തിരഞ്ഞെടുക്കാൻ.
- `send_request` മെത്തഡ് പ്രോംപ്റ്റും കോൺഫിഗർ ചെയ്ത സാമ്പ്ലിംഗ് പാരാമീറ്ററുകളും ഉപയോഗിച്ച് അഭ്യർത്ഥന അയയ്ക്കാൻ.
- `generated_text` മോഡലിന്റെ പ്രതികരണം ലഭിക്കാൻ, പിന്നീട് സാമ്പ്ലിംഗ് പാരാമീറ്ററുകളും ജോലിതരവും കൂടെ തിരിച്ചുവിടാൻ.
- `min` , `max` ഫങ്ഷനുകൾ ഉപയോക്തൃ ഇഷ്ടങ്ങൾ സാധുവായ പരിധികളിൽ ഉറപ്പാക്കാൻ, അസാധുവായ കോൺഫിഗറേഷനുകൾ തടയാൻ.

# [JavaScript Dynamic](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// ജാവാസ്ക്രിപ്റ്റ് ഉദാഹരണം: ഉപയോക്തൃ സാഹചര്യത്തിന്റെ അടിസ്ഥാനത്തിൽ ഡൈനാമിക് സാമ്പ്ലിംഗ് കോൺഫിഗറേഷൻ
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // അടിസ്ഥാന സാമ്പ്ലിംഗ് പ്രൊഫൈലുകൾ നിർവചിക്കുക
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // ചരിത്രപരമായ പ്രകടനം ട്രാക്ക് ചെയ്യുക
    this.performanceHistory = [];
  }
  
  // പ്രോംപ്റ്റിൽ നിന്നുള്ള ടാസ്‌ക് തരം കണ്ടെത്തുക
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // ലളിതമായ ഹ്യൂറിസ്റ്റിക് കണ്ടെത്തൽ - എംഎൽ ക്ലാസിഫിക്കേഷനോടെ മെച്ചപ്പെടുത്താവുന്നതാണ്
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
    
    // വ്യക്തമായ തരം കണ്ടെത്താനാകാതെപോയാൽ ഡിഫോൾട്ട് ആയി സംഭാഷണാത്മകമായി നിശ്ചയിക്കുക
    return 'conversational';
  }
  
  // സാഹചര്യവും ഉപയോക്തൃ ഇഷ്ടാനുസൃതികളും അടിസ്ഥാനമാക്കി സാമ്പ്ലിംഗ് പാരാമീറ്ററുകൾ കണക്കാക്കുക
  getSamplingParameters(prompt, context = {}) {
    // ടാസ്‌കിന്റെ തരം കണ്ടെത്തുക
    const taskType = this.detectTaskType(prompt, context);
    
    // അടിസ്ഥാന പ്രൊഫൈൽ നേടുക
    let params = {...this.samplingProfiles[taskType]};
    
    // ഉപയോക്തൃ ഇഷ്ടാനുസൃതികൾ അടിസ്ഥാനമാക്കി ക്രമീകരിക്കുക
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // 1-10 മുതൽ അനുയോജ്യമായ താപനില പരിധിയിലേക്ക് സ്കെയിൽ ചെയ്യുക
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // ഉയർന്ന കൃത്യത കുറഞ്ഞ topP (കൂടുതൽ കേന്ദ്രീകൃതമായ തിരഞ്ഞെടുപ്പ്) അർത്ഥമാക്കുന്നു
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // ഉയർന്ന സ്ഥിരത കുറഞ്ഞ ശിക്ഷകൾ അർത്ഥമാക്കുന്നു
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // പ്രകടന ചരിത്രത്തിൽ നിന്നുള്ള പഠിച്ച ക്രമീകരണങ്ങൾ പ്രയോഗിക്കുക
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // ലളിതമായ അനുയോജ്യമായ ലജിക് - കൂടുതൽ സങ്കീർണ്ണ ആൽഗോരിതങ്ങൾ ഉപയോഗിച്ച് മെച്ചപ്പെടുത്താവുന്നതാണ്
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // അടുത്തകാലത്തെ ചരിത്രം മാത്രം പരിഗണിക്കുക
    
    if (relevantHistory.length > 0) {
      // ശരാശരി പ്രകടന സ്കോറുകൾ കണക്കാക്കുക
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // പ്രകടനം പരിധിക്കു താഴെ ആണെങ്കിൽ, പാരാമീറ്ററുകൾ ക്രമീകരിക്കുക
      if (avgScore < 0.7) {
        // സുരക്ഷിത മൂല്യങ്ങളിലേക്കുള്ള ചെറിയ ക്രമീകരണം
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // ഭാവിയിലെ ക്രമീകരണങ്ങൾക്ക് പ്രകടനം രേഖപ്പെടുത്തുക
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // പ്രതികരണ ഗുണനിലവാരത്തിന്റെ 0-1 റേറ്റിംഗ്
    });
    
    // ചരിത്ര വലുപ്പം പരിമിതപ്പെടുത്തുക
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // മെച്ചപ്പെടുത്തിയ സാമ്പ്ലിംഗ് പാരാമീറ്ററുകൾ നേടുക
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // മെച്ചപ്പെടുത്തിയ പാരാമീറ്ററുകളോടെ അഭ്യർത്ഥന അയയ്ക്കുക
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // ഉപയോക്താവ് പ്രതികരണം നൽകുന്നുവെങ്കിൽ, ഭാവിയിലെ മെച്ചപ്പെടുത്തലിനായി അത് രേഖപ്പെടുത്തുക
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

// ഉദാഹരണ ഉപയോഗം
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // കസ്റ്റം ഉപയോക്തൃ ഇഷ്ടാനുസൃതികളോടുള്ള സൃഷ്ടിപരമായ ടാസ്‌ക്
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // ഉയർന്ന സൃഷ്ടിപരത (1-10)
          consistency: 3  // കുറഞ്ഞ സ്ഥിരത (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // കോഡ് ജനറേഷൻ ടാസ്‌ക്
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // കുറഞ്ഞ സൃഷ്ടിപരത
          precision: 8,   // ഉയർന്ന കൃത്യത
          consistency: 9  // ഉയർന്ന സ്ഥിരത
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

മുൻകൂട്ടി നൽകിയ കോഡിൽ ഞങ്ങൾ:

- ജോലിതരം, ഉപയോക്തൃ ഇഷ്ടാനുസരണം ഡൈനാമിക് സാമ്പ്ലിംഗ് കൈകാര്യം ചെയ്യുന്ന `AdaptiveSamplingManager` ക്ലാസ് സൃഷ്ടിച്ചു.
- വ്യത്യസ്ത ജോലിതരം (സൃഷ്ടിപര, വാസ്തവപര, കോഡ്, സംഭാഷണ) എന്നിവയ്ക്ക് സാമ്പ്ലിംഗ് പ്രൊഫൈലുകൾ നിർവചിച്ചു.
- പ്രോംപ്റ്റിൽ നിന്നുള്ള ലളിതമായ ഹ്യൂറിസ്റ്റിക്സ് ഉപയോഗിച്ച് ജോലിതരം കണ്ടെത്താനുള്ള മെത്തഡ് നടപ്പിലാക്കി.
- കണ്ടെത്തിയ ജോലിതരം, ഉപയോക്തൃ ഇഷ്ടാനുസരണം സാമ്പ്ലിംഗ് പാര

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->