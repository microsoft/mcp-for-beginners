# HTTPS Streaming z protokołem Model Context Protocol (MCP)

Ten rozdział oferuje kompleksowy przewodnik po implementacji bezpiecznego, skalowalnego i w czasie rzeczywistym przesyłania strumieniowego z użyciem protokołu Model Context Protocol (MCP) za pomocą HTTPS. Omawia motywację do przesyłania strumieniowego, dostępne mechanizmy transportowe, sposób implementacji przesyłania strumieniowego HTTP w MCP, najlepsze praktyki dotyczące bezpieczeństwa, migrację z SSE oraz praktyczne wskazówki dotyczące budowy własnych aplikacji MCP do przesyłania strumieniowego.

## Mechanizmy transportowe i przesyłanie strumieniowe w MCP

Ta sekcja bada różne mechanizmy transportowe dostępne w MCP oraz ich rolę w umożliwianiu przesyłania strumieniowego dla komunikacji w czasie rzeczywistym między klientami a serwerami.

### Co to jest mechanizm transportowy?

Mechanizm transportowy definiuje sposób wymiany danych między klientem a serwerem. MCP obsługuje wiele typów transportu, aby dostosować się do różnych środowisk i wymagań:

- **stdio**: Standardowe wejście/wyjście, odpowiednie dla lokalnych narzędzi CLI. Proste, ale nieodpowiednie dla aplikacji webowych czy chmurowych.
- **SSE (Server-Sent Events)**: Pozwala serwerom na przesyłanie aktualizacji w czasie rzeczywistym do klientów za pomocą HTTP. Dobre dla interfejsów webowych, ale ograniczone pod względem skalowalności i elastyczności.
- **Streamable HTTP**: Nowoczesny transport oparty na HTTP, obsługujący powiadomienia i lepszą skalowalność. Zalecany dla większości scenariuszy produkcyjnych i chmurowych.

### Tabela porównawcza

Zapoznaj się z poniższą tabelą porównawczą, aby zrozumieć różnice między tymi mechanizmami transportowymi:

| Transport         | Aktualizacje w czasie rzeczywistym | Przesyłanie strumieniowe | Skalowalność | Zastosowanie               |
|-------------------|------------------------------------|--------------------------|-------------|---------------------------|
| stdio             | Nie                               | Nie                      | Niska       | Lokalnie, narzędzia CLI   |
| SSE               | Tak                               | Tak                      | Średnia     | Web, aktualizacje w czasie rzeczywistym |
| Streamable HTTP   | Tak                               | Tak                      | Wysoka      | Chmura, wieloklientowe    |

> **Tip:** Wybór odpowiedniego transportu wpływa na wydajność, skalowalność i doświadczenie użytkownika. **Streamable HTTP** jest zalecany dla nowoczesnych, skalowalnych aplikacji gotowych na chmurę.

Zwróć uwagę na transporty stdio i SSE, które zostały omówione w poprzednich rozdziałach, oraz na to, że streamable HTTP jest transportem omawianym w tym rozdziale.

## Przesyłanie strumieniowe: Koncepcje i motywacja

Zrozumienie podstawowych koncepcji i motywacji stojących za przesyłaniem strumieniowym jest kluczowe dla implementacji skutecznych systemów komunikacji w czasie rzeczywistym.

**Przesyłanie strumieniowe** to technika w programowaniu sieciowym, która pozwala na przesyłanie i odbieranie danych w małych, łatwych do zarządzania fragmentach lub jako sekwencja zdarzeń, zamiast czekać na pełną odpowiedź. Jest to szczególnie przydatne w przypadku:

- Dużych plików lub zestawów danych.
- Aktualizacji w czasie rzeczywistym (np. czat, paski postępu).
- Długotrwałych obliczeń, gdzie chcesz informować użytkownika na bieżąco.

Oto, co warto wiedzieć o przesyłaniu strumieniowym na wysokim poziomie:

- Dane są dostarczane stopniowo, a nie wszystkie naraz.
- Klient może przetwarzać dane w miarę ich przybywania.
- Zmniejsza postrzeganą latencję i poprawia doświadczenie użytkownika.

### Dlaczego warto korzystać z przesyłania strumieniowego?

Powody, dla których warto korzystać z przesyłania strumieniowego, są następujące:

- Użytkownicy otrzymują informacje zwrotne natychmiast, a nie dopiero na końcu.
- Umożliwia aplikacje w czasie rzeczywistym i responsywne interfejsy użytkownika.
- Bardziej efektywne wykorzystanie zasobów sieciowych i obliczeniowych.

### Prosty przykład: Serwer i klient HTTP przesyłający strumieniowo

Oto prosty przykład, jak można zaimplementować przesyłanie strumieniowe:

#### Python

**Serwer (Python, używając FastAPI i StreamingResponse):**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**Klient (Python, używając requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Ten przykład pokazuje serwer wysyłający serię wiadomości do klienta w miarę ich dostępności, zamiast czekać na gotowość wszystkich wiadomości.

**Jak to działa:**

- Serwer generuje każdą wiadomość w miarę jej gotowości.
- Klient odbiera i drukuje każdy fragment w miarę jego przybywania.

**Wymagania:**

- Serwer musi używać odpowiedzi strumieniowej (np. `StreamingResponse` w FastAPI).
- Klient musi przetwarzać odpowiedź jako strumień (`stream=True` w requests).
- Content-Type zazwyczaj to `text/event-stream` lub `application/octet-stream`.

#### Java

**Serwer (Java, używając Spring Boot i Server-Sent Events):**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**Klient (Java, używając Spring WebFlux WebClient):**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**Uwagi dotyczące implementacji w Javie:**

- Używa reaktywnego stosu Spring Boot z `Flux` do przesyłania strumieniowego.
- `ServerSentEvent` zapewnia strukturalne przesyłanie zdarzeń z typami zdarzeń.
- `WebClient` z `bodyToFlux()` umożliwia reaktywne odbieranie strumieniowe.
- `delayElements()` symuluje czas przetwarzania między zdarzeniami.
- Zdarzenia mogą mieć typy (`info`, `result`) dla lepszej obsługi po stronie klienta.

### Porównanie: Klasyczne przesyłanie strumieniowe vs MCP Streaming

Różnice między klasycznym przesyłaniem strumieniowym a przesyłaniem strumieniowym w MCP można przedstawić w następujący sposób:

| Funkcja                | Klasyczne przesyłanie HTTP     | MCP Streaming (Powiadomienia)      |
|------------------------|-------------------------------|-------------------------------------|
| Główna odpowiedź       | Fragmentowana                 | Jedna, na końcu                    |
| Aktualizacje postępu   | Wysyłane jako fragmenty danych | Wysyłane jako powiadomienia        |
| Wymagania klienta      | Musi przetwarzać strumień      | Musi implementować obsługę wiadomości |
| Zastosowanie           | Duże pliki, strumienie tokenów AI | Postęp, logi, informacje zwrotne w czasie rzeczywistym |

### Zaobserwowane kluczowe różnice

Dodatkowo, oto kilka kluczowych różnic:

- **Wzorzec komunikacji:**
  - Klasyczne przesyłanie HTTP: Używa prostego kodowania transferu fragmentowanego do wysyłania danych w fragmentach.
  - MCP Streaming: Używa strukturalnego systemu powiadomień z protokołem JSON-RPC.

- **Format wiadomości:**
  - Klasyczne HTTP: Fragmenty tekstu z nowymi liniami.
  - MCP: Strukturalne obiekty LoggingMessageNotification z metadanymi.

- **Implementacja klienta:**
  - Klasyczne HTTP: Prosty klient przetwarzający odpowiedzi strumieniowe.
  - MCP: Bardziej zaawansowany klient z obsługą wiadomości do przetwarzania różnych typów wiadomości.

- **Aktualizacje postępu:**
  - Klasyczne HTTP: Postęp jest częścią głównego strumienia odpowiedzi.
  - MCP: Postęp jest wysyłany za pomocą oddzielnych wiadomości powiadomień, podczas gdy główna odpowiedź przychodzi na końcu.

### Rekomendacje

Oto kilka zaleceń dotyczących wyboru między implementacją klasycznego przesyłania strumieniowego (jako punkt końcowy pokazany powyżej używający `/stream`) a wyborem przesyłania strumieniowego za pomocą MCP.

- **Dla prostych potrzeb przesyłania strumieniowego:** Klasyczne przesyłanie HTTP jest prostsze w implementacji i wystarczające dla podstawowych potrzeb przesyłania strumieniowego.

- **Dla złożonych, interaktywnych aplikacji:** MCP Streaming oferuje bardziej strukturalne podejście z bogatszymi metadanymi i rozdzieleniem między powiadomieniami a wynikami końcowymi.

- **Dla aplikacji AI:** System powiadomień MCP jest szczególnie przydatny w przypadku długotrwałych zadań AI, gdzie chcesz informować użytkowników o postępie.

## Przesyłanie strumieniowe w MCP

Ok, widziałeś już kilka zaleceń i porównań dotyczących różnic między klasycznym przesyłaniem strumieniowym a przesyłaniem strumieniowym w MCP. Przejdźmy do szczegółów, jak dokładnie możesz wykorzystać przesyłanie strumieniowe w MCP.

Zrozumienie, jak działa przesyłanie strumieniowe w ramach MCP, jest kluczowe dla budowy responsywnych aplikacji, które zapewniają użytkownikom informacje zwrotne w czasie rzeczywistym podczas długotrwałych operacji.

W MCP przesyłanie strumieniowe nie polega na wysyłaniu głównej odpowiedzi w fragmentach, ale na wysyłaniu **powiadomień** do klienta podczas przetwarzania żądania przez narzędzie. Te powiadomienia mogą zawierać aktualizacje postępu, logi lub inne zdarzenia.

### Jak to działa

Główny wynik nadal jest wysyłany jako pojedyncza odpowiedź. Jednak powiadomienia mogą być wysyłane jako oddzielne wiadomości podczas przetwarzania, aktualizując klienta w czasie rzeczywistym. Klient musi być w stanie obsługiwać i wyświetlać te powiadomienia.

## Co to jest powiadomienie?

Powiedzieliśmy "Powiadomienie", co to oznacza w kontekście MCP?

Powiadomienie to wiadomość wysyłana z serwera do klienta, informująca o postępie, statusie lub innych zdarzeniach podczas długotrwałej operacji. Powiadomienia poprawiają przejrzystość i doświadczenie użytkownika.

Na przykład klient powinien wysłać powiadomienie po nawiązaniu początkowego połączenia z serwerem.

Powiadomienie wygląda tak jako wiadomość JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Powiadomienia należą do tematu w MCP określanego jako ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Aby logowanie działało, serwer musi włączyć je jako funkcję/możliwość w następujący sposób:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> W zależności od używanego SDK logowanie może być domyślnie włączone lub może być konieczne jego wyraźne włączenie w konfiguracji serwera.

Istnieją różne typy powiadomień:

| Poziom     | Opis                          | Przykład zastosowania          |
|------------|-------------------------------|---------------------------------|
| debug      | Szczegółowe informacje debugowania | Punkty wejścia/wyjścia funkcji |
| info       | Ogólne wiadomości informacyjne | Aktualizacje postępu operacji  |
| notice     | Zwykłe, ale istotne zdarzenia | Zmiany konfiguracji            |
| warning    | Warunki ostrzegawcze          | Użycie przestarzałej funkcji   |
| error      | Warunki błędów                | Niepowodzenia operacji         |
| critical   | Krytyczne warunki             | Awaria komponentu systemu      |
| alert      | Natychmiastowa akcja wymagana | Wykrycie uszkodzenia danych    |
| emergency  | System nie działa             | Całkowita awaria systemu       |

## Implementacja powiadomień w MCP

Aby zaimplementować powiadomienia w MCP, musisz skonfigurować zarówno stronę serwera, jak i klienta, aby obsługiwały aktualizacje w czasie rzeczywistym. Dzięki temu Twoja aplikacja będzie mogła zapewniać użytkownikom natychmiastowe informacje zwrotne podczas długotrwałych operacji.

### Po stronie serwera: Wysyłanie powiadomień

Zacznijmy od strony serwera. W MCP definiujesz narzędzia, które mogą wysyłać powiadomienia podczas przetwarzania żądań. Serwer używa obiektu kontekstu (zwykle `ctx`) do wysyłania wiadomości do klienta.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

W powyższym przykładzie narzędzie `process_files` wysyła trzy powiadomienia do klienta podczas przetwarzania każdego pliku. Metoda `ctx.info()` jest używana do wysyłania wiadomości informacyjnych.

Dodatkowo, aby włączyć powiadomienia, upewnij się, że Twój serwer używa transportu strumieniowego (takiego jak `streamable-http`), a Twój klient implementuje obsługę wiadomości do przetwarzania powiadomień. Oto jak możesz skonfigurować serwer do używania transportu `streamable-http`:

```python
mcp.run(transport="streamable-http")
```

#### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

W tym przykładzie .NET narzędzie `ProcessFiles` jest oznaczone atrybutem `Tool` i wysyła trzy powiadomienia do klienta podczas przetwarzania każdego pliku. Metoda `ctx.Info()` jest używana do wysyłania wiadomości informacyjnych.

Aby włączyć powiadomienia w serwerze MCP .NET, upewnij się, że używasz transportu strumieniowego:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Po stronie klienta: Odbieranie powiadomień

Klient musi zaimplementować obsługę wiadomości, aby przetwarzać i wyświetlać powiadomienia w miarę ich przybywania.

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```

W powyższym kodzie funkcja `message_handler` sprawdza, czy przychodząca wiadomość jest powiadomieniem. Jeśli tak, drukuje powiadomienie; w przeciwnym razie przetwarza je jako zwykłą wiadomość serwera. Zwróć uwagę, jak `ClientSession` jest inicjalizowany z `message_handler`, aby obsługiwać przychodzące powiadomienia.

#### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```

W tym przykładzie .NET funkcja `MessageHandler` sprawdza, czy przychodząca wiadomość jest powiadomieniem. Jeśli tak, drukuje powiadomienie; w przeciwnym razie przetwarza je jako zwykłą wiadomość serwera. `ClientSession` jest inicjalizowany z obsługą wiadomości za pomocą `ClientSessionOptions`.

Aby włączyć powiadomienia, upewnij się, że Twój serwer używa transportu strumieniowego (takiego jak `streamable-http`), a Twój klient implementuje obsługę wiadomości do przetwarzania powiadomień.

## Powiadomienia o postępie i scenariusze

Ta sekcja wyjaśnia koncepcję powiadomień o postępie w MCP, dlaczego są ważne i jak je zaimplementować za pomocą Streamable HTTP. Znajdziesz tu również praktyczne zadanie, które pomoże Ci utrwalić wiedzę.

Powiadomienia o postępie to wiadomości w czasie rzeczywistym wysyłane z serwera do klienta podczas długotrwałych operacji. Zamiast czekać na zakończenie całego procesu, serwer informuje klienta o bieżącym statusie. Poprawia to przejrzystość, doświadczenie użytkownika i ułatwia debugowanie.

**Przykład:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Dlaczego warto używać powiadomień o postępie?

Powiadomienia o postępie są niezbędne z kilku powodów:

- **Lepsze doświadczenie użytkownika:** Użytkownicy widzą aktualizacje w miarę postępu pracy, a nie dopiero na końcu.
- **Informacje zwrotne w czasie rzeczywistym:** Klienci mogą wyświetlać paski postępu lub logi, co sprawia, że aplikacja wydaje się responsywna.
- **Łatwiejsze debugowanie i monitorowanie:** Programiści i użytkownicy mogą zobaczyć, gdzie proces może być wolny lub zablokowany.

### Jak zaimplementować powiadomienia o postępie

Oto jak możesz zaimplementować powiadomienia o postępie w MCP:

- **Po stronie serwera:** Użyj `ctx.info()` lub `ctx.log()`, aby wysyłać powiadomienia w miarę przetwarzania każdego elementu. To wysyła wiadomość do klienta przed przygotowaniem głównego wyniku.
- **Po stronie klienta:** Zaimplementuj obsługę wiadomo
Istnieją dwa przekonujące powody, aby przejść z SSE na Streamable HTTP:

- Streamable HTTP oferuje lepszą skalowalność, kompatybilność i bogatsze wsparcie dla powiadomień niż SSE.
- Jest to zalecany transport dla nowych aplikacji MCP.

### Kroki migracji

Oto jak można przejść z SSE na Streamable HTTP w swoich aplikacjach MCP:

- **Zaktualizuj kod serwera**, aby używać `transport="streamable-http"` w `mcp.run()`.
- **Zaktualizuj kod klienta**, aby korzystać z `streamablehttp_client` zamiast klienta SSE.
- **Zaimplementuj obsługę wiadomości** w kliencie, aby przetwarzać powiadomienia.
- **Przetestuj kompatybilność** z istniejącymi narzędziami i przepływami pracy.

### Utrzymanie kompatybilności

Zaleca się utrzymanie kompatybilności z istniejącymi klientami SSE podczas procesu migracji. Oto kilka strategii:

- Możesz obsługiwać zarówno SSE, jak i Streamable HTTP, uruchamiając oba transporty na różnych punktach końcowych.
- Stopniowo migruj klientów na nowy transport.

### Wyzwania

Upewnij się, że rozwiązujesz następujące wyzwania podczas migracji:

- Aktualizacja wszystkich klientów
- Radzenie sobie z różnicami w dostarczaniu powiadomień

## Rozważania dotyczące bezpieczeństwa

Bezpieczeństwo powinno być najwyższym priorytetem podczas implementacji dowolnego serwera, szczególnie przy użyciu transportów opartych na HTTP, takich jak Streamable HTTP w MCP.

Podczas implementacji serwerów MCP z transportami opartymi na HTTP, bezpieczeństwo staje się kluczowym zagadnieniem, które wymaga starannego uwzględnienia wielu wektorów ataku i mechanizmów ochrony.

### Przegląd

Bezpieczeństwo jest kluczowe podczas udostępniania serwerów MCP przez HTTP. Streamable HTTP wprowadza nowe powierzchnie ataku i wymaga starannej konfiguracji.

Oto kluczowe kwestie dotyczące bezpieczeństwa:

- **Walidacja nagłówka Origin**: Zawsze weryfikuj nagłówek `Origin`, aby zapobiec atakom typu DNS rebinding.
- **Powiązanie z localhost**: Na potrzeby lokalnego rozwoju, powiąż serwery z `localhost`, aby uniknąć ich wystawienia na publiczny internet.
- **Uwierzytelnianie**: Wdroż uwierzytelnianie (np. klucze API, OAuth) w środowiskach produkcyjnych.
- **CORS**: Skonfiguruj zasady Cross-Origin Resource Sharing (CORS), aby ograniczyć dostęp.
- **HTTPS**: Używaj HTTPS w środowiskach produkcyjnych, aby szyfrować ruch.

### Najlepsze praktyki

Dodatkowo, oto kilka najlepszych praktyk dotyczących bezpieczeństwa w serwerach strumieniowych MCP:

- Nigdy nie ufaj przychodzącym żądaniom bez ich weryfikacji.
- Loguj i monitoruj wszystkie dostępy i błędy.
- Regularnie aktualizuj zależności, aby załatać luki w zabezpieczeniach.

### Wyzwania

Podczas wdrażania zabezpieczeń w serwerach strumieniowych MCP możesz napotkać następujące wyzwania:

- Równoważenie bezpieczeństwa z łatwością rozwoju
- Zapewnienie kompatybilności z różnymi środowiskami klientów

### Zadanie: Zbuduj własną aplikację strumieniową MCP

**Scenariusz:**
Zbuduj serwer i klienta MCP, gdzie serwer przetwarza listę elementów (np. plików lub dokumentów) i wysyła powiadomienie dla każdego przetworzonego elementu. Klient powinien wyświetlać każde powiadomienie w czasie rzeczywistym.

**Kroki:**

1. Zaimplementuj narzędzie serwera, które przetwarza listę i wysyła powiadomienia dla każdego elementu.
2. Zaimplementuj klienta z obsługą wiadomości, aby wyświetlać powiadomienia w czasie rzeczywistym.
3. Przetestuj swoją implementację, uruchamiając zarówno serwer, jak i klienta, i obserwuj powiadomienia.

[Solution](./solution/README.md)

## Dalsza lektura i co dalej?

Aby kontynuować swoją przygodę z MCP streamingiem i poszerzyć wiedzę, ta sekcja zawiera dodatkowe zasoby i sugerowane kolejne kroki w budowaniu bardziej zaawansowanych aplikacji.

### Dalsza lektura

- [Microsoft: Wprowadzenie do HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS w ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Co dalej?

- Spróbuj zbudować bardziej zaawansowane narzędzia MCP, które wykorzystują streaming do analityki w czasie rzeczywistym, czatu lub wspólnej edycji.
- Zbadaj integrację MCP streaming z frameworkami frontendowymi (React, Vue itp.) dla aktualizacji interfejsu użytkownika na żywo.
- Następny krok: [Wykorzystanie AI Toolkit dla VSCode](../07-aitk/README.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.