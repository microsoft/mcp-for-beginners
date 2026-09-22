> [!WARNING]
> Próbkowanie jest przestarzałe w MCP `2026-07-28`. Ta lekcja jest zachowana dla
> implementacji dziedziczonych. Nowe serwery powinny integrować się bezpośrednio z API
> dostawcy LLM.

# Próbkowanie w Model Context Protocol

> Próbkowanie pozostaje w specyfikacji `2026-07-28` dla zachowania kompatybilności i jest
> kwalifikowane do usunięcia w pierwszej rewizji wydanej 28 lipca
> 2027 lub później. Przykłady w tej lekcji mogą korzystać z API SDK implementujących `2025-11-25`.
> Zobacz [Co się zmieniło w MCP: Specyfikacja 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

W dziedzicznych implementacjach MCP, Próbkowanie pozwala serwerom żądać uzupełnień LLM
przez klienta. Ta lekcja wyjaśnia ten przestarzały przepływ protokołu
w celach kompatybilności i migracji.

## Wprowadzenie

W tej lekcji omówimy, jak konfigurować parametry próbkowania w żądaniach MCP oraz zrozumieć mechanikę próbkowania w protokole.

## Cele nauki

Pod koniec tej lekcji będziesz potrafił:

- Zrozumieć kluczowe parametry próbkowania dostępne w MCP.
- Konfigurować parametry próbkowania dla różnych przypadków użycia.
- Implementować deterministyczne próbkowanie dla powtarzalnych wyników.
- Dynamicznie dostosowywać parametry próbkowania na podstawie kontekstu i preferencji użytkownika.
- Stosować strategie próbkowania w celu poprawy wydajności modelu w różnych scenariuszach.
- Zrozumieć, jak próbkowanie działa w przepływie klient-serwer MCP.

## Jak działa próbkowanie w MCP

Przepływ próbkowania w MCP obejmuje następujące kroki:

1. Serwer wysyła żądanie `sampling/createMessage` do klienta
2. Klient przegląda żądanie i może je modyfikować
3. Klient pobiera próbkę z LLM
4. Klient ocenia uzupełnienie
5. Klient zwraca wynik do serwera

Ta konstrukcja z udziałem człowieka w pętli zapewnia, że użytkownicy zachowują kontrolę nad tym, co LLM widzi i generuje.

## Przegląd parametrów próbkowania

MCP definiuje następujące parametry próbkowania, które można konfigurować w żądaniach klienta:

| Parameter | Opis | Typowy zakres |
|-----------|-------------|---------------|
| `temperature` | Kontroluje losowość w wyborze tokenów | 0.0 - 1.0 |
| `maxTokens` | Maksymalna liczba generowanych tokenów | Wartość całkowita |
| `stopSequences` | Niestandardowe sekwencje zatrzymujące generowanie po napotkaniu | Tablica łańcuchów znaków |
| `metadata` | Dodatkowe parametry specyficzne dla dostawcy | Obiekt JSON |

Wielu dostawców LLM obsługuje dodatkowe parametry poprzez pole `metadata`, które mogą zawierać:

| Powszechny parametr rozszerzenia | Opis | Typowy zakres |
|-----------|-------------|---------------|
| `top_p` | Próbkowanie jądrowe - ogranicza tokeny do największego skumulowanego prawdopodobieństwa | 0.0 - 1.0 |
| `top_k` | Ogranicza wybór tokenów do top K opcji | 1 - 100 |
| `presence_penalty` | Kara za obecność tokenów w dotychczasowym tekście | -2.0 - 2.0 |
| `frequency_penalty` | Kara za częstotliwość tokenów w dotychczasowym tekście | -2.0 - 2.0 |
| `seed` | Specyficzne ziarno losowości dla powtarzalnych wyników | Wartość całkowita |

## Przykładowy format żądania

Oto przykład żądania próbkowania od klienta w MCP:

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

## Kontrola człowieka w pętli

Próbkowanie MCP zaprojektowano z uwzględnieniem nadzoru człowieka:

- **Dla promptów**:
  - Klienci powinni pokazywać użytkownikom proponowany prompt
  - Użytkownicy powinni mieć możliwość modyfikacji lub odrzucenia promptów
  - Prompty systemowe mogą być filtrowane lub zmieniane
  - Włączanie kontekstu kontroluje klient

- **Dla uzupełnień**:
  - Klienci powinni pokazywać użytkownikom uzupełnienie
  - Użytkownicy powinni mieć możliwość modyfikacji lub odrzucenia uzupełnień
  - Klienci mogą filtrować lub modyfikować uzupełnienia
  - Użytkownicy kontrolują, który model jest używany

Z tymi zasadami na uwadze, przyjrzyjmy się, jak zaimplementować próbkowanie w różnych językach programowania, koncentrując się na parametrach powszechnie obsługiwanych przez dostawców LLM.

## Zagadnienia bezpieczeństwa

Implementując próbkowanie w MCP, rozważ następujące dobre praktyki bezpieczeństwa:

- **Weryfikuj całą zawartość wiadomości** przed wysłaniem do klienta
- **Oczyść poufne informacje** z promptów i uzupełnień
- **Wprowadź limity szybkości** aby zapobiegać nadużyciom
- **Monitoruj użycie próbkowania** pod kątem nietypowych wzorców
- **Szyfruj dane w tranzycie** używając bezpiecznych protokołów
- **Obsługuj prywatność danych użytkownika** zgodnie z obowiązującymi przepisami
- **Audytuj żądania próbkowania** pod kątem zgodności i bezpieczeństwa
- **Kontroluj narażenie na koszty** stosując odpowiednie limity
- **Wprowadzaj limit czasu** na żądania próbkowania
- **Obsługuj błędy modelu w sposób łagodny** z odpowiednimi rozwiązaniami zapasowymi

Parametry próbkowania pozwalają na precyzyjne dostrojenie zachowania modeli językowych, aby osiągnąć pożądaną równowagę pomiędzy wynikami deterministycznymi a kreatywnymi.

Przyjrzyjmy się, jak konfigurować te parametry w różnych językach programowania.

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

W powyższym kodzie:

- Utworzono klienta MCP z określonym URL serwera.
- Skonfigurowano żądanie z parametrami próbkowania takimi jak `temperature`, `top_p` oraz `top_k`.
- Wysłano żądanie i wydrukowano wygenerowany tekst.
- Użyto:
    - `allowedTools` by określić, które narzędzia model może używać podczas generowania. W tym przypadku zezwolono na narzędzia `ideaGenerator` i `marketAnalyzer` w celu wsparcia generowania kreatywnych pomysłów na aplikacje.
    - `frequencyPenalty` i `presencePenalty` do kontrolowania powtarzalności i różnorodności w wyniku.
    - `temperature` by kontrolować losowość wyniku, gdzie wyższe wartości prowadzą do bardziej kreatywnych odpowiedzi.
    - `top_p` by ograniczyć wybór tokenów do tych, które wnoszą największą skumulowaną masę prawdopodobieństwa, poprawiając jakość generowanego tekstu.
    - `top_k` by ograniczyć model do top K najbardziej prawdopodobnych tokenów, co pomaga generować spójniejsze odpowiedzi.
    - `frequencyPenalty` i `presencePenalty` by zmniejszyć powtarzalność i zachęcać do różnorodności w generowanym tekście.

# [JavaScript](#tab/javascript)

```javascript
// Przykład JavaScript: konfiguracja temperatury i próbkowania Top-P
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Inicjalizuj klienta MCP
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Skonfiguruj żądanie z różnymi parametrami próbkowania
  const creativeSampling = {
    temperature: 0.9,    // Wyższa temperatura = większa losowość/kreatywność
    topP: 0.92,          // Uwzględnij tokeny z masą prawdopodobieństwa top 92%
    frequencyPenalty: 0.6, // Zmniejsz powtarzalność sekwencji tokenów
    presencePenalty: 0.4   // Nakładaj karę na tokeny, które pojawiły się w tekście do tej pory
  };
  
  const factualSampling = {
    temperature: 0.2,    // Niższa temperatura = bardziej deterministyczne/faktyczne
    topP: 0.85,          // Nieco bardziej ukierunkowany wybór tokenów
    frequencyPenalty: 0.2, // Minimalna kara za powtarzanie
    presencePenalty: 0.1   // Minimalna kara za obecność
  };
  
  try {
    // Wyślij dwa żądania z różnymi konfiguracjami próbkowania
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

- Zainicjalizowano klienta MCP z URL serwera i kluczem API.
- Skonfigurowano dwa zestawy parametrów próbkowania: jeden dla zadań kreatywnych, drugi dla faktograficznych.
- Wysłano żądania z tymi konfiguracjami, pozwalając modelowi używać określonych narzędzi dla każdego zadania.
- Wydrukowano wygenerowane odpowiedzi, aby pokazać efekty różnych parametrów próbkowania.
- Użyto `allowedTools`, by określić, które narzędzia model może wykorzystywać podczas generowania. W tym przypadku zezwolono na `ideaGenerator` i `environmentalImpactTool` dla zadań kreatywnych oraz `factChecker` i `dataAnalysisTool` dla zadań faktograficznych.
- Użyto `temperature` do kontrolowania losowości wyniku, gdzie wyższe wartości prowadzą do bardziej kreatywnych odpowiedzi.

- Użyto `top_p`, aby ograniczyć wybór tokenów do tych, które wnoszą do najwyższej skumulowanej masy prawdopodobieństwa, co poprawia jakość generowanego tekstu.
- Użyto `frequencyPenalty` i `presencePenalty`, aby zmniejszyć powtórzenia i zachęcić do różnorodności w wyniku.
- Użyto `top_k`, aby ograniczyć model do top K najbardziej prawdopodobnych tokenów, co może pomóc w generowaniu spójniejszych odpowiedzi.

---

## Deterministyczne próbkowanie

Dla aplikacji wymagających spójnych wyników, deterministyczne próbkowanie zapewnia odtwarzalne rezultaty. Dzieje się tak poprzez użycie stałego ziarna losowości i ustawienie temperatury na zero.

Spójrzmy na poniższy przykład implementacji, aby zobaczyć deterministyczne próbkowanie w różnych językach programowania.

# [Java](#tab/java)

```java
// Przykład w Javie: Deterministyczne odpowiedzi z ustalonym ziarnem
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Użycie ustalonego ziarna dla deterministycznych wyników
        
        // Pierwsze zapytanie z ustalonym ziarnem
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Temperatura zero dla maksymalnego determinizmu
            .build();
            
        // Drugie zapytanie z tym samym ziarnem
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Wykonaj oba zapytania
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Odpowiedzi powinny być identyczne z powodu tego samego ziarna i temperatury=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

W poprzednim kodzie:

- Utworzono klienta MCP z podanym adresem URL serwera.
- Skonfigurowano dwa żądania z tym samym promptem, stałym ziarnem i zerową temperaturą.
- Wysłano oba żądania i wydrukowano wygenerowany tekst.
- Pokazano, że odpowiedzi są identyczne ze względu na deterministyczny charakter konfiguracji próbkowania (to samo ziarno i temperatura).
- Użyto `setSeed`, aby określić stałe ziarno losowości, zapewniając, że model generuje ten sam wynik dla tych samych danych wejściowych za każdym razem.
- Ustawiono `temperature` na zero, aby zapewnić maksymalną deterministykę, co oznacza, że model zawsze wybierze najbardziej prawdopodobny kolejny token bez losowości.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Przykład JavaScript: Deterministyczne odpowiedzi z kontrolą ziarna
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Pierwsze żądanie z ustalonym ziarnem
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Temperatura zero dla maksymalnego determinizmu
    });
    
    // Drugie żądanie z tym samym ziarnem i temperaturą
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Trzecie żądanie z innym ziarnem, ale tą samą temperaturą
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

W poprzednim kodzie:

- Zainicjowano klienta MCP z adresem URL serwera.
- Skonfigurowano dwa żądania z tym samym promptem, stałym ziarnem i zerową temperaturą.
- Wysłano oba żądania i wydrukowano wygenerowany tekst.
- Pokazano, że odpowiedzi są identyczne ze względu na deterministyczny charakter konfiguracji próbkowania (to samo ziarno i temperatura).
- Użyto `seed`, aby określić stałe ziarno losowości, zapewniając, że model generuje ten sam wynik dla tych samych danych wejściowych za każdym razem.
- Ustawiono `temperature` na zero, aby zapewnić maksymalną deterministykę, co oznacza, że model zawsze wybierze najbardziej prawdopodobny kolejny token bez losowości.
- Użyto innego ziarna dla trzeciego żądania, aby pokazać, że zmiana ziarna skutkuje różnymi wynikami, nawet przy tym samym promptcie i temperaturze.

---

## Dynamiczna konfiguracja próbkowania

Inteligentne próbkowanie dostosowuje parametry w oparciu o kontekst i wymagania każdego żądania. Oznacza to dynamiczne dostosowywanie parametrów takich jak temperatura, top_p oraz kary na podstawie typu zadania, preferencji użytkownika lub historycznej wydajności.

Spójrzmy, jak zaimplementować dynamiczne próbkowanie w różnych językach programowania.

# [Python](#tab/python)

```python
# Przykład Pythona: Dynamiczne próbkowanie oparte na kontekście zapytania
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Zdefiniuj presety próbkowania dla różnych typów zadań
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Wybierz podstawowy preset
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Dostosuj na podstawie preferencji użytkownika, jeśli są podane
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Skaluj temperaturę w oparciu o preferencje kreatywności (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Dostosuj top_p w zależności od pożądanej różnorodności odpowiedzi
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Utwórz i wyślij zapytanie z niestandardowymi parametrami próbkowania
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Zwróć odpowiedź z metadanymi próbkowania dla przejrzystości
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

W poprzednim kodzie:

- Utworzono klasę `DynamicSamplingService`, która zarządza adaptacyjnym próbkowaniem.
- Zdefiniowano wstępne ustawienia próbkowania dla różnych typów zadań (kreatywne, faktograficzne, kod, analityczne).
- Wybrano bazowe ustawienie próbkowania na podstawie typu zadania.
- Dostosowano parametry próbkowania na podstawie preferencji użytkownika, takich jak poziom kreatywności i różnorodności.
- Wysłano żądanie z dynamicznie skonfigurowanymi parametrami próbkowania.
- Zwrócono wygenerowany tekst wraz z zastosowanymi parametrami próbkowania i typem zadania dla przejrzystości.
- Użyto `temperature`, aby kontrolować losowość wyniku, gdzie wyższe wartości prowadzą do bardziej kreatywnych odpowiedzi.
- Użyto `top_p`, aby ograniczyć wybór tokenów do tych, które przyczyniają się do najwyższej skumulowanej masy prawdopodobieństwa, poprawiając jakość wygenerowanego tekstu.
- Użyto `frequency_penalty`, aby zmniejszyć powtórzenia i zachęcić do różnorodności w wyniku.
- Użyto `user_preferences`, aby umożliwić dostosowanie parametrów próbkowania w oparciu o zdefiniowane przez użytkownika poziomy kreatywności i różnorodności.
- Użyto `task_type`, aby określić odpowiednią strategię próbkowania dla żądania, pozwalając na bardziej dopasowane odpowiedzi w zależności od charakteru zadania.
- Użyto metody `send_request`, aby wysłać prompt z skonfigurowanymi parametrami próbkowania, zapewniając, że model generuje tekst zgodnie z określonymi wymaganiami.
- Użyto `generated_text`, aby pobrać odpowiedź modelu, która jest następnie zwracana wraz z parametrami próbkowania i typem zadania do dalszej analizy lub wyświetlenia.
- Użyto funkcji `min` i `max`, aby upewnić się, że preferencje użytkownika mieszczą się w prawidłowych zakresach, zapobiegając nieprawidłowym konfiguracjom próbkowania.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// Przykład JavaScript: Dynamiczna konfiguracja próbkowania oparta na kontekście użytkownika
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Definiuj podstawowe profile próbkowania
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Śledź historyczną wydajność
    this.performanceHistory = [];
  }
  
  // Wykryj typ zadania na podstawie prompta
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Proste wykrywanie heurystyczne - można ulepszyć za pomocą klasyfikacji ML
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
    
    // Domyślnie ustaw na konwersacyjne, jeśli nie wykryto wyraźnego typu
    return 'conversational';
  }
  
  // Oblicz parametry próbkowania na podstawie kontekstu i preferencji użytkownika
  getSamplingParameters(prompt, context = {}) {
    // Wykryj typ zadania
    const taskType = this.detectTaskType(prompt, context);
    
    // Pobierz podstawowy profil
    let params = {...this.samplingProfiles[taskType]};
    
    // Dostosuj na podstawie preferencji użytkownika
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Przeskaluj z 1-10 do odpowiedniego zakresu temperatury
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Wyższa precyzja oznacza niższe topP (bardziej skoncentrowany wybór)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Wyższa spójność oznacza niższe kary
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Zastosuj nauczone korekty z historii wydajności
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Prosta logika adaptacyjna - można ulepszyć bardziej zaawansowanymi algorytmami
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Uwzględniaj tylko niedawną historię
    
    if (relevantHistory.length > 0) {
      // Oblicz średnie wyniki wydajności
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Jeśli wydajność jest poniżej progu, dostosuj parametry
      if (avgScore < 0.7) {
        // Nieznaczna korekta w kierunku bezpieczniejszych wartości
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Zapisz wyniki wydajności do przyszłych korekt
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Ocena jakości odpowiedzi od 0 do 1
    });
    
    // Ogranicz rozmiar historii
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Pobierz zoptymalizowane parametry próbkowania
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Wyślij żądanie z zoptymalizowanymi parametrami
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Jeśli użytkownik udzieli opinii, zapisz ją do przyszłej optymalizacji
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

// Przykład użycia
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Kreatywne zadanie z niestandardowymi preferencjami użytkownika
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Wysoka kreatywność (1-10)
          consistency: 3  // Niska spójność (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Zadanie generowania kodu
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Niska kreatywność
          precision: 8,   // Wysoka precyzja
          consistency: 9  // Wysoka spójność
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

W poprzednim kodzie:

- Utworzono klasę `AdaptiveSamplingManager`, która zarządza dynamicznym próbkowaniem na podstawie typu zadania i preferencji użytkownika.
- Zdefiniowano profile próbkowania dla różnych typów zadań (kreatywne, faktograficzne, kod, konwersacyjne).
- Zaimplementowano metodę wykrywającą typ zadania na podstawie prompta używając prostych heurystyk.
- Obliczono parametry próbkowania w oparciu o wykryty typ zadania i preferencje użytkownika.
- Zastosowano wyuczone korekty na podstawie historycznej wydajności, aby zoptymalizować parametry próbkowania.
- Zarejestrowano wydajność do przyszłych korekt, pozwalając systemowi uczyć się na podstawie przeszłych interakcji.
- Wysłano żądania z dynamicznie skonfigurowanymi parametrami próbkowania i zwrócono wygenerowany tekst wraz z zastosowanymi parametrami i wykrytym typem zadania.
- Użyto:
    - `userPreferences`, aby umożliwić dostosowanie parametrów próbkowania w oparciu o zdefiniowane przez użytkownika poziomy kreatywności, precyzji i spójności.
    - `detectTaskType`, aby określić charakter zadania na podstawie prompta, pozwalając na bardziej dopasowane odpowiedzi.
    - `recordPerformance`, aby rejestrować wydajność wygenerowanych odpowiedzi, umożliwiając systemowi adaptację i poprawę w czasie.
    - `applyLearnedAdjustments`, aby modyfikować parametry próbkowania w oparciu o historyczną wydajność, zwiększając zdolność modelu do generowania wysokiej jakości odpowiedzi.
    - `generateResponse`, aby objąć cały proces generowania odpowiedzi z adaptacyjnym próbkowaniem, ułatwiając wywoływanie z różnymi promptami i kontekstami.
    - `allowedTools`, aby określić, które narzędzia model może wykorzystać podczas generowania, umożliwiając bardziej świadome kontekstowo odpowiedzi.
    - `feedbackScore`, aby umożliwić użytkownikom przekazywanie opinii na temat jakości wygenerowanej odpowiedzi, co może być wykorzystane do dalszej optymalizacji działania modelu.
    - `performanceHistory`, aby utrzymywać zapis przeszłych interakcji, umożliwiając systemowi naukę na podstawie wcześniejszych sukcesów i porażek.
    - `getSamplingParameters`, aby dynamicznie dostosowywać parametry próbkowania w zależności od kontekstu żądania, pozwalając na bardziej elastyczne i responsywne zachowanie modelu.
    - `detectTaskType`, aby klasyfikować zadanie na podstawie prompta, umożliwiając zastosowanie odpowiednich strategii próbkowania dla różnych rodzajów żądań.
    - `samplingProfiles`, aby definiować bazowe konfiguracje próbkowania dla różnych typów zadań, pozwalając na szybkie dostosowania w zależności od charakteru żądania.

---

## Co dalej

- [5.7 Skalowanie](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->