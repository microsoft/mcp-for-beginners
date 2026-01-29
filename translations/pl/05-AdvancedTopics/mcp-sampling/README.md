# Sampling w protokole Model Context Protocol

Sampling to potężna funkcja MCP, która pozwala serwerom na żądanie uzupełnień LLM za pośrednictwem klienta, umożliwiając zaawansowane zachowania agentowe przy jednoczesnym zachowaniu bezpieczeństwa i prywatności. Odpowiednia konfiguracja sampling może znacząco poprawić jakość odpowiedzi i wydajność. MCP zapewnia ustandaryzowany sposób kontrolowania, jak modele generują tekst, z wykorzystaniem konkretnych parametrów wpływających na losowość, kreatywność i spójność.

## Wprowadzenie

W tej lekcji omówimy, jak konfigurować parametry sampling w żądaniach MCP oraz zrozumiemy mechanikę protokołu sampling.

## Cele nauki

Po zakończeniu tej lekcji będziesz potrafił:

- Zrozumieć kluczowe parametry sampling dostępne w MCP.
- Konfigurować parametry sampling dla różnych zastosowań.
- Wdrażać deterministyczny sampling dla powtarzalnych wyników.
- Dynamicznie dostosowywać parametry sampling w zależności od kontekstu i preferencji użytkownika.
- Stosować strategie sampling w celu poprawy wydajności modelu w różnych scenariuszach.
- Zrozumieć, jak sampling działa w przepływie klient-serwer MCP.

## Jak działa sampling w MCP

Przepływ sampling w MCP przebiega według następujących kroków:

1. Serwer wysyła żądanie `sampling/createMessage` do klienta
2. Klient przegląda żądanie i może je zmodyfikować
3. Klient wykonuje sampling z LLM
4. Klient przegląda wygenerowaną odpowiedź
5. Klient zwraca wynik do serwera

Ten projekt z udziałem człowieka w pętli zapewnia, że użytkownicy zachowują kontrolę nad tym, co LLM widzi i generuje.

## Przegląd parametrów sampling

MCP definiuje następujące parametry sampling, które można konfigurować w żądaniach klienta:

| Parametr | Opis | Typowy zakres |
|-----------|-------------|---------------|
| `temperature` | Kontroluje losowość wyboru tokenów | 0.0 - 1.0 |
| `maxTokens` | Maksymalna liczba tokenów do wygenerowania | Wartość całkowita |
| `stopSequences` | Niestandardowe sekwencje zatrzymujące generowanie po ich napotkaniu | Tablica stringów |
| `metadata` | Dodatkowe parametry specyficzne dla dostawcy | Obiekt JSON |

Wielu dostawców LLM obsługuje dodatkowe parametry przez pole `metadata`, które mogą zawierać:

| Popularny parametr rozszerzenia | Opis | Typowy zakres |
|-----------|-------------|---------------|
| `top_p` | Sampling jądrowy - ogranicza tokeny do tych o najwyższym skumulowanym prawdopodobieństwie | 0.0 - 1.0 |
| `top_k` | Ogranicza wybór tokenów do top K opcji | 1 - 100 |
| `presence_penalty` | Nakłada karę na tokeny na podstawie ich obecności w dotychczasowym tekście | -2.0 - 2.0 |
| `frequency_penalty` | Nakłada karę na tokeny na podstawie ich częstotliwości w dotychczasowym tekście | -2.0 - 2.0 |
| `seed` | Konkretne ziarno losowe dla powtarzalnych wyników | Wartość całkowita |

## Przykładowy format żądania

Oto przykład żądania sampling od klienta w MCP:

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

## Format odpowiedzi

Klient zwraca wynik uzupełnienia:

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

## Kontrola z udziałem człowieka

Sampling w MCP został zaprojektowany z myślą o nadzorze człowieka:

- **Dla promptów**:
  - Klienci powinni pokazywać użytkownikom proponowany prompt
  - Użytkownicy powinni mieć możliwość modyfikacji lub odrzucenia promptów
  - Prompty systemowe mogą być filtrowane lub modyfikowane
  - Włączanie kontekstu jest kontrolowane przez klienta

- **Dla uzupełnień**:
  - Klienci powinni pokazywać użytkownikom wygenerowaną odpowiedź
  - Użytkownicy powinni mieć możliwość modyfikacji lub odrzucenia uzupełnień
  - Klienci mogą filtrować lub modyfikować uzupełnienia
  - Użytkownicy kontrolują, który model jest używany

Mając na uwadze te zasady, przyjrzyjmy się, jak zaimplementować sampling w różnych językach programowania, skupiając się na parametrach powszechnie obsługiwanych przez dostawców LLM.

## Aspekty bezpieczeństwa

Podczas implementacji sampling w MCP należy uwzględnić następujące najlepsze praktyki bezpieczeństwa:

- **Weryfikuj całą zawartość wiadomości** przed wysłaniem do klienta
- **Oczyść wrażliwe informacje** z promptów i uzupełnień
- **Wprowadź limity szybkości** aby zapobiec nadużyciom
- **Monitoruj użycie sampling** pod kątem nietypowych wzorców
- **Szyfruj dane w tranzycie** za pomocą bezpiecznych protokołów
- **Zadbaj o prywatność danych użytkowników** zgodnie z obowiązującymi przepisami
- **Audytuj żądania sampling** pod kątem zgodności i bezpieczeństwa
- **Kontroluj koszty** stosując odpowiednie limity
- **Wprowadź timeouty** dla żądań sampling
- **Obsługuj błędy modelu** w sposób łagodny, stosując odpowiednie mechanizmy zapasowe

Parametry sampling pozwalają precyzyjnie dostroić zachowanie modeli językowych, aby osiągnąć pożądany balans między deterministycznymi a kreatywnymi wynikami.

Przyjrzyjmy się, jak konfigurować te parametry w różnych językach programowania.

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

W powyższym kodzie:

- Utworzono klienta MCP z określonym URL serwera.
- Skonfigurowano żądanie z parametrami sampling takimi jak `temperature`, `top_p` i `top_k`.
- Wysłano żądanie i wydrukowano wygenerowany tekst.
- Użyto:
    - `allowedTools` do określenia, które narzędzia model może używać podczas generowania. W tym przypadku pozwolono na użycie narzędzi `ideaGenerator` i `marketAnalyzer`, aby pomóc w tworzeniu kreatywnych pomysłów na aplikacje.
    - `frequencyPenalty` i `presencePenalty` do kontrolowania powtarzalności i różnorodności w wyjściu.
    - `temperature` do kontrolowania losowości odpowiedzi, gdzie wyższe wartości prowadzą do bardziej kreatywnych wyników.
    - `top_p` do ograniczenia wyboru tokenów do tych, które wnoszą największy wkład w skumulowaną masę prawdopodobieństwa, co poprawia jakość generowanego tekstu.
    - `top_k` do ograniczenia modelu do top K najbardziej prawdopodobnych tokenów, co może pomóc w generowaniu bardziej spójnych odpowiedzi.
    - `frequencyPenalty` i `presencePenalty` do zmniejszenia powtórzeń i zachęcania do różnorodności w generowanym tekście.

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

W powyższym kodzie:

- Zainicjowano klienta MCP z URL serwera i kluczem API.
- Skonfigurowano dwa zestawy parametrów sampling: jeden dla zadań kreatywnych, drugi dla zadań faktograficznych.
- Wysłano żądania z tymi konfiguracjami, pozwalając modelowi używać określonych narzędzi dla każdego zadania.
- Wydrukowano wygenerowane odpowiedzi, aby pokazać efekty różnych parametrów sampling.
- Użyto `allowedTools` do określenia, które narzędzia model może używać podczas generowania. W tym przypadku pozwolono na `ideaGenerator` i `environmentalImpactTool` dla zadań kreatywnych oraz `factChecker` i `dataAnalysisTool` dla zadań faktograficznych.
- Użyto `temperature` do kontrolowania losowości odpowiedzi, gdzie wyższe wartości prowadzą do bardziej kreatywnych wyników.
- Użyto `top_p` do ograniczenia wyboru tokenów do tych, które wnoszą największy wkład w skumulowaną masę prawdopodobieństwa, co poprawia jakość generowanego tekstu.
- Użyto `frequencyPenalty` i `presencePenalty` do zmniejszenia powtórzeń i zachęcania do różnorodności w wyjściu.
- Użyto `top_k` do ograniczenia modelu do top K najbardziej prawdopodobnych tokenów, co może pomóc w generowaniu bardziej spójnych odpowiedzi.

---

## Deterministyczny sampling

Dla aplikacji wymagających spójnych wyników, deterministyczny sampling zapewnia powtarzalne rezultaty. Osiąga się to przez użycie stałego ziarna losowego i ustawienie temperatury na zero.

Poniżej znajduje się przykładowa implementacja demonstrująca deterministyczny sampling w różnych językach programowania.

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

W powyższym kodzie:

- Utworzono klienta MCP z określonym URL serwera.
- Skonfigurowano dwa żądania z tym samym promptem, stałym ziarnem i zerową temperaturą.
- Wysłano oba żądania i wydrukowano wygenerowany tekst.
- Pokazano, że odpowiedzi są identyczne ze względu na deterministyczny charakter konfiguracji sampling (to samo ziarno i temperatura).
- Użyto `setSeed` do określenia stałego ziarna losowego, co zapewnia, że model generuje ten sam wynik dla tego samego wejścia za każdym razem.
- Ustawiono `temperature` na zero, aby zapewnić maksymalną deterministyczność, co oznacza, że model zawsze wybierze najbardziej prawdopodobny kolejny token bez losowości.

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

W powyższym kodzie:

- Zainicjowano klienta MCP z URL serwera.
- Skonfigurowano dwa żądania z tym samym promptem, stałym ziarnem i zerową temperaturą.
- Wysłano oba żądania i wydrukowano wygenerowany tekst.
- Pokazano, że odpowiedzi są identyczne ze względu na deterministyczny charakter konfiguracji sampling (to samo ziarno i temperatura).
- Użyto `seed` do określenia stałego ziarna losowego, co zapewnia, że model generuje ten sam wynik dla tego samego wejścia za każdym razem.
- Ustawiono `temperature` na zero, aby zapewnić maksymalną deterministyczność, co oznacza, że model zawsze wybierze najbardziej prawdopodobny kolejny token bez losowości.
- Użyto innego ziarna dla trzeciego żądania, aby pokazać, że zmiana ziarna skutkuje różnymi wynikami, nawet przy tym samym prompt i temperaturze.

---

## Dynamiczna konfiguracja sampling

Inteligentny sampling dostosowuje parametry na podstawie kontekstu i wymagań każdego żądania. Oznacza to dynamiczne dostosowywanie parametrów takich jak temperature, top_p i kary na podstawie typu zadania, preferencji użytkownika lub historycznej wydajności.

Poniżej pokazujemy, jak zaimplementować dynamiczny sampling w różnych językach programowania.

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

W powyższym kodzie:

- Utworzono klasę `DynamicSamplingService`, która zarządza adaptacyjnym samplingiem.
- Zdefiniowano presety sampling dla różnych typów zadań (kreatywne, faktograficzne, kod, analityczne).
- Wybrano bazowy preset sampling na podstawie typu zadania.
- Dostosowano parametry sampling na podstawie preferencji użytkownika, takich jak poziom kreatywności i różnorodności.
- Wysłano żądanie z dynamicznie skonfigurowanymi parametrami sampling.
- Zwrócono wygenerowany tekst wraz z zastosowanymi parametrami sampling i typem zadania dla przejrzystości.
- Użyto `temperature` do kontrolowania losowości odpowiedzi, gdzie wyższe wartości prowadzą do bardziej kreatywnych wyników.
- Użyto `top_p` do ograniczenia wyboru tokenów do tych, które wnoszą największy wkład w skumulowaną masę prawdopodobieństwa, co poprawia jakość generowanego tekstu.
- Użyto `frequency_penalty` do zmniejszenia powtórzeń i zachęcania do różnorodności w wyjściu.
- Użyto `user_preferences` do umożliwienia dostosowania parametrów sampling na podstawie zdefiniowanego przez użytkownika poziomu kreatywności i różnorodności.
- Użyto `task_type` do określenia odpowiedniej strategii sampling dla żądania, co pozwala na bardziej dopasowane odpowiedzi w zależności od charakteru zadania.
- Użyto metody `send_request` do wysłania promptu z skonfigurowanymi parametrami sampling, zapewniając, że model generuje tekst zgodnie z określonymi wymaganiami.
- Użyto `generated_text` do pobrania odpowiedzi modelu, która jest następnie zwracana wraz z parametrami sampling i typem zadania do dalszej analizy lub wyświetlenia.
- Użyto funkcji `min` i `max` do zapewnienia, że preferencje użytkownika mieszczą się w prawidłowych zakresach, zapobiegając nieprawidłowym konfiguracjom sampling.

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

W powyższym kodzie:

- Utworzono klasę `AdaptiveSamplingManager`, która zarządza dynamicznym samplingiem na podstawie typu zadania i preferencji użytkownika.
- Zdefiniowano profile sampling dla różnych typów zadań (kreatywne, faktograficzne, kod, konwersacyjne).
- Zaimplementowano metodę wykrywającą typ zadania na podstawie promptu, używając prostych heurystyk.
- Obliczono parametry sampling na podstawie wykrytego typu zadania i preferencji użytkownika.
- Zastosowano wyuczone korekty na podstawie historycznej wydajności, aby zoptymalizować parametry sampling.
- Zarejestrowano wydajność dla przyszłych korekt, pozwalając systemowi uczyć się na podstawie wcześniejszych interakcji.
- Wysłano żądania z dynamicznie skonfigurowanymi parametrami sampling i zwrócono wygenerowany tekst wraz z zastosowanymi parametrami i wykrytym typem zadania.
- Użyto:
    - `userPreferences` do umożliwienia dostosowania parametrów sampling na podstawie zdefiniowanego przez użytkownika poziomu kreatywności, precyzji i spójności.
    - `detectTaskType` do określenia charakteru zadania na podstawie promptu, co pozwala na bardziej dopasowane odpowiedzi.
    - `recordPerformance` do rejestrowania wydajności wygenerowanych odpowiedzi, umożliwiając systemowi adaptację i poprawę z czasem.
    - `applyLearnedAdjustments` do modyfikowania parametrów sampling na podstawie historycznej wydajności, zwiększając zdolność modelu do generowania wysokiej jakości odpowiedzi.
    - `generateResponse` do enkapsulacji całego procesu generowania odpowiedzi z adaptacyjnym samplingiem, ułatwiając wywołanie z różnymi promptami i kontekstami.
    - `allowedTools` do określenia, które narzędzia model może używać podczas generowania, co pozwala na bardziej kontekstowe odpowiedzi.
    - `feedbackScore` do umożliwienia użytkownikom przekazywania opinii na temat jakości wygenerowanej odpowiedzi, co może być wykorzystane do dalszego doskonalenia modelu.
    - `performanceHistory` do utrzymywania zapisu wcześniejszych interakcji, umożliwiając systemowi uczenie się na podstawie sukcesów i porażek.
    - `getSamplingParameters` do dynamicznego dostosowywania parametrów sampling na podstawie kontekstu żądania, co pozwala na bardziej elastyczne i responsywne zachowanie modelu.
    - `detectTaskType` do klasyfikacji zadania na podstawie promptu, umożliwiając stosowanie odpowiednich strategii sampling dla różnych typów żądań.
    - `samplingProfiles` do definiowania bazowych konfiguracji sampling dla różnych typów zadań, co pozwala na szybkie dostosowania w zależności od charakteru żądania.

---

## Co dalej

- [5.7 Skalowanie](../mcp-scaling/README.md)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.