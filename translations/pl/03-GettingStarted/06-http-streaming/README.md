# HTTPS Streaming z protokołem Model Context Protocol (MCP)

Ten rozdział oferuje kompleksowy przewodnik po implementacji bezpiecznego, skalowalnego i strumieniowego przesyłu danych w czasie rzeczywistym za pomocą Model Context Protocol (MCP) przez HTTPS. Omawia motywację do strumieniowania, dostępne mechanizmy transportowe, jak zaimplementować strumieniowy HTTP w MCP, najlepsze praktyki bezpieczeństwa, migrację z SSE i praktyczne wskazówki dotyczące tworzenia własnych aplikacji strumieniowych MCP.

> **Patrząc w przyszłość:** ta lekcja opisuje Strumieniowy HTTP w ramach **Specyfikacji MCP 2025-11-25**, gdzie sesja jest ustanowiona podczas `initialize` i przypisana za pomocą nagłówka `Mcp-Session-Id`. W kandydacie do wydania `2026-07-28` usunięto całkowicie proces uzgadniania i identyfikator sesji, czyniąc każde żądanie samodzielnym i kierowalnym do dowolnej instancji serwera bez potrzeby stałych sesji. Szczegóły znajdziesz w [Co się zmienia w MCP: kandydat do wydania 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

## Mechanizmy transportowe i strumieniowanie w MCP

W tej sekcji poznasz różne mechanizmy transportowe dostępne w MCP oraz ich rolę w umożliwianiu funkcji strumieniowania dla komunikacji w czasie rzeczywistym między klientami a serwerami.

### Co to jest mechanizm transportowy?

Mechanizm transportowy definiuje sposób wymiany danych między klientem a serwerem. MCP obsługuje różne typy transportu, aby dopasować się do różnych środowisk i wymagań:

- **stdio**: Standardowe wejście/wyjście, odpowiednie dla narzędzi lokalnych i opartych na CLI. Prosty, ale niezbyt nadaje się do wykorzystania w webie czy chmurze.
- **SSE (Server-Sent Events)**: Pozwala serwerom wysyłać aktualizacje w czasie rzeczywistym do klientów przez HTTP. Dobre dla interfejsów webowych, lecz ograniczone pod względem skalowalności i elastyczności. Od Specyfikacji MCP 2025-06-18 samodzielny transport SSE został wycofany i zastąpiony przez "Streamable HTTP".
- **Streamable HTTP**: Nowoczesny transport strumieniowy oparty na HTTP, obsługujący powiadomienia i lepszą skalowalność. Zalecany dla większości produkcyjnych i chmurowych zastosowań.

### Tabela porównawcza

Spójrz na poniższą tabelę porównawczą, aby zrozumieć różnice między tymi mechanizmami transportu:

| Transport         | Aktualizacje w czasie rzeczywistym | Strumieniowanie | Skalowalność | Przypadek użycia           |
|-------------------|------------------------------------|-----------------|--------------|----------------------------|
| stdio             | Nie                                | Nie             | Niska        | Narzędzia lokalne CLI      |
| SSE               | Tak                                | Tak             | Średnia      | Web, aktualizacje czasu rzeczywistego |
| Streamable HTTP   | Tak                                | Tak             | Wysoka       | Chmura, wieloklientowe     |

> **Wskazówka:** Wybór odpowiedniego transportu wpływa na wydajność, skalowalność i doświadczenie użytkownika. **Streamable HTTP** jest zalecany dla nowoczesnych, skalowalnych i gotowych do chmury aplikacji.

Zwróć uwagę na transporty stdio i SSE przedstawione w poprzednich rozdziałach oraz na to, że transportem omawianym w tym rozdziale jest strumieniowy HTTP.

## Strumieniowanie: Koncepcje i motywacje

Zrozumienie podstawowych koncepcji i motywacji stojących za strumieniowaniem jest niezbędne do implementacji skutecznych systemów komunikacji w czasie rzeczywistym.

**Strumieniowanie** to technika w programowaniu sieciowym pozwalająca na wysyłanie i odbieranie danych w małych, zarządzalnych fragmentach lub jako sekwencja zdarzeń, zamiast oczekiwania na pełną odpowiedź. Jest to szczególnie przydatne przy:

- Dużych plikach lub zestawach danych.
- Aktualizacjach w czasie rzeczywistym (np. czat, paski postępu).
- Długotrwałych obliczeniach, gdzie chce się informować użytkownika na bieżąco.

Oto, co warto wiedzieć o strumieniowaniu na wysokim poziomie:

- Dane są dostarczane stopniowo, nie wszystkie na raz.
- Klient może przetwarzać dane jak tylko nadejdą.
- Redukuje odczuwalną latencję i poprawia doświadczenie użytkownika.

### Dlaczego warto stosować strumieniowanie?

Powody korzystania ze strumieniowania to:

- Użytkownicy otrzymują natychmiastową informację zwrotną, nie tylko na końcu.
- Umożliwia aplikacjom w czasie rzeczywistym i responsywnym interfejsom.
- Bardziej efektywne wykorzystanie zasobów sieci i obliczeń.

### Prosty przykład: Serwer i klient HTTP streamingowy

Oto prosty przykład implementacji strumieniowania:

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

Ten przykład pokazuje serwer wysyłający serię wiadomości do klienta, gdy tylko są dostępne, zamiast czekać na wszystkie wiadomości naraz.

**Jak to działa:**

- Serwer generuje każdą wiadomość, gdy jest gotowa.
- Klient odbiera i wypisuje każdy fragment po otrzymaniu.

**Wymagania:**

- Serwer musi używać odpowiedzi strumieniowanej (np. `StreamingResponse` w FastAPI).
- Klient musi przetwarzać odpowiedź jako strumień (`stream=True` w requests).
- Content-Type to zwykle `text/event-stream` lub `application/octet-stream`.

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

**Notatki dotyczące implementacji w Javie:**

- Używa reaktywnego stosu Spring Boot z `Flux` do strumieniowania
- `ServerSentEvent` oferuje strukturalne strumieniowanie zdarzeń z typami zdarzeń
- `WebClient` z `bodyToFlux()` umożliwia konsumowanie strumieni reaktywnych
- `delayElements()` symuluje czas przetwarzania między zdarzeniami
- Zdarzenia mogą mieć typy (`info`, `result`) dla lepszej obsługi klienta

### Porównanie: klasyczne strumieniowanie vs strumieniowanie MCP

Różnice między tym, jak działa klasyczne strumieniowanie, a jak działa strumieniowanie w MCP można przedstawić w ten sposób:

| Cecha                  | Klasyczne strumieniowanie HTTP    | Strumieniowanie MCP (Powiadomienia) |
|------------------------|----------------------------------|-------------------------------------|
| Główna odpowiedź       | Porcjowana (chunked)              | Jedna, na końcu                      |
| Aktualizacje postępu   | Wysyłane jako porcje danych       | Wysyłane jako powiadomienia         |
| Wymagania klienta      | Musi przetwarzać strumień         | Musi implementować obsługę wiadomości |
| Przypadek użycia       | Duże pliki, strumienie tokenów AI | Postęp, logi, informacja zwrotna na żywo |

### Zaobserwowane kluczowe różnice

Dodatkowo, oto kilka kluczowych różnic:

- **Wzorzec komunikacji:**
  - Klasyczne strumieniowanie HTTP: Używa prostego kodowania transferu porcjowanego do wysyłania danych w częściach
  - Strumieniowanie MCP: Używa strukturalnego systemu powiadomień z protokołem JSON-RPC

- **Format wiadomości:**
  - Klasyczne HTTP: Czysty tekst z podziałem na porcje i nowe linie
  - MCP: Strukturalne obiekty LoggingMessageNotification z metadanymi

- **Implementacja klienta:**
  - Klasyczne HTTP: Prosty klient przetwarzający odpowiedzi strumieniowe
  - MCP: Bardziej zaawansowany klient z obsługą wiadomości przetwarzającą różne typy wiadomości

- **Aktualizacje postępu:**
  - Klasyczne HTTP: Postęp jest częścią głównego strumienia odpowiedzi
  - MCP: Postęp jest wysyłany przez oddzielne wiadomości powiadomień, podczas gdy główny wynik jest przesyłany na końcu

### Zalecenia

Zalecamy kilka rzeczy przy wyborze między klasyczną implementacją strumieniowania (jak pokazaliśmy powyżej z endpointem `/stream`) a strumieniowaniem przez MCP.

- **Dla prostych potrzeb strumieniowych:** Klasyczne HTTP streaming jest prostszy do implementacji i wystarcza do podstawowych wymagań.

- **Dla złożonych, interaktywnych aplikacji:** Strumieniowanie MCP zapewnia bardziej strukturalne podejście z bogatszymi metadanymi oraz rozdzieleniem powiadomień i wyników końcowych.

- **Dla aplikacji AI:** System powiadomień MCP jest szczególnie przydatny w długotrwałych zadaniach AI, gdzie chcesz na bieżąco informować użytkowników o postępach.

## Strumieniowanie w MCP

Więc widziałeś już zalecenia i porównania dotyczące różnic między klasycznym strumieniowaniem a strumieniowaniem w MCP. Przejdźmy do szczegółów, jak dokładnie możesz wykorzystać strumieniowanie w MCP.

Zrozumienie, jak działa strumieniowanie w ramach MCP, jest kluczowe do budowania responsywnych aplikacji oferujących użytkownikom informacje zwrotne w czasie rzeczywistym podczas długotrwałych operacji.

W MCP strumieniowanie nie polega na wysyłaniu głównej odpowiedzi w porcjach, lecz na wysyłaniu **powiadomień** do klienta podczas przetwarzania żądania przez narzędzie. Powiadomienia te mogą zawierać aktualizacje postępu, logi lub inne zdarzenia.

### Jak to działa

Główny wynik jest nadal przesyłany jako pojedyncza odpowiedź. Jednakże powiadomienia mogą być wysyłane jako oddzielne wiadomości w trakcie przetwarzania i w ten sposób aktualizują klienta na bieżąco. Klient musi potrafić obsługiwać i wyświetlać te powiadomienia.

## Co to jest powiadomienie?

Powiedzieliśmy „powiadomienie”, co to znaczy w kontekście MCP?

Powiadomienie to wiadomość wysyłana z serwera do klienta, informująca o postępie, statusie lub innych zdarzeniach podczas długotrwałej operacji. Powiadomienia zwiększają przejrzystość i poprawiają doświadczenie użytkownika.

Na przykład klient powinien wysłać powiadomienie zaraz po nawiązaniu początkowego połączenia z serwerem.

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

> **Informacja o wycofaniu:** kandydat do wersji specyfikacji MCP `2026-07-28` oznacza prymityw Logging jako przestarzały na korzyść `stderr` dla transportów stdio oraz OpenTelemetry dla ustrukturyzowanej obserwowalności. Logging będzie działać w `2025-11-25` i co najmniej rok po formalnym wycofaniu. Szczegóły znajdziesz w [Co się zmienia w MCP: kandydat do wydania 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Aby umożliwić logowanie, serwer musi je aktywować jako funkcję/możliwość w ten sposób:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> W zależności od używanego SDK, logowanie może być domyślnie włączone lub trzeba je będzie explicitnie włączyć w konfiguracji serwera.

Istnieją różne typy powiadomień:

| Poziom     | Opis                             | Przykład użycia               |
|-----------|---------------------------------|------------------------------|
| debug     | Szczegółowe informacje debugowania | Punkty wejścia/wyjścia funkcji |
| info      | Ogólne wiadomości informacyjne  | Aktualizacje postępu operacji  |
| notice    | Normalne, ale istotne zdarzenia | Zmiany konfiguracji            |
| warning   | Warunki ostrzegawcze            | Użycie przestarzałej funkcji  |
| error     | Warunki błędów                 | Niepowodzenia operacji         |
| critical  | Warunki krytyczne              | Awaria komponentów systemu     |
| alert     | Natychmiastowe działania wymagane | Wykryto uszkodzenie danych   |
| emergency | System jest nieużywalny         | Całkowita awaria systemu      |

## Implementacja powiadomień w MCP

Aby zaimplementować powiadomienia w MCP, musisz skonfigurować zarówno stronę serwera, jak i klienta do obsługi aktualizacji w czasie rzeczywistym. Pozwala to aplikacji na dostarczanie natychmiastowej informacji zwrotnej użytkownikom podczas długotrwałych operacji.

### Strona serwera: wysyłanie powiadomień

Zacznijmy od strony serwera. W MCP definiujesz narzędzia, które mogą wysyłać powiadomienia podczas przetwarzania żądań. Serwer używa obiektu kontekstu (zwykle `ctx`), aby wysłać wiadomości do klienta.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

W powyższym przykładzie narzędzie `process_files` wysyła trzy powiadomienia do klienta podczas przetwarzania każdego pliku. Metoda `ctx.info()` służy do wysyłania wiadomości informacyjnych.

Dodatkowo, aby włączyć powiadomienia, upewnij się, że serwer używa transportu strumieniowego (np. `streamable-http`), a klient implementuje obsługę wiadomości do przetwarzania powiadomień. Oto jak skonfigurować serwer do użycia transportu `streamable-http`:

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

Aby włączyć powiadomienia w swoim serwerze MCP .NET, upewnij się, że używasz transportu strumieniowego:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Strona klienta: odbieranie powiadomień

Klient musi zaimplementować obsługę wiadomości, aby przetwarzać i wyświetlać powiadomienia w miarę ich nadejścia.

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

W powyższym kodzie funkcja `message_handler` sprawdza, czy przychodząca wiadomość jest powiadomieniem. Jeśli tak, wypisuje powiadomienie; w przeciwnym razie przetwarza je jako zwykłą wiadomość serwera. Zwróć uwagę, że `ClientSession` jest inicjalizowana z `message_handler` do obsługi przychodzących powiadomień.

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

W tym przykładzie .NET funkcja `MessageHandler` sprawdza, czy przychodząca wiadomość jest powiadomieniem. Jeśli tak, wypisuje powiadomienie; w przeciwnym razie przetwarza jako zwykłą wiadomość serwera. `ClientSession` jest inicjalizowana z handlerem wiadomości przez `ClientSessionOptions`.

Aby włączyć powiadomienia, upewnij się, że serwer używa transportu strumieniowego (np. `streamable-http`), a klient implementuje obsługę wiadomości do przetwarzania powiadomień.

## Powiadomienia o postępie i scenariusze

Ta sekcja wyjaśnia koncept powiadomień o postępie w MCP, dlaczego są ważne i jak je zaimplementować za pomocą Streamable HTTP. Znajdziesz tu też praktyczne zadanie, które utrwali Twoją wiedzę.

Powiadomienia o postępie to wiadomości w czasie rzeczywistym wysyłane z serwera do klienta podczas długotrwałych operacji. Zamiast czekać na ukończenie całego procesu, serwer na bieżąco informuje klienta o aktualnym stanie. To zwiększa przejrzystość, poprawia doświadczenie użytkownika i ułatwia debugowanie.

**Przykład:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Dlaczego stosować powiadomienia o postępie?

Powiadomienia o postępie są niezbędne z kilku powodów:

- **Lepsze doświadczenie użytkownika:** Użytkownicy widzą aktualizacje w trakcie pracy, a nie tylko na końcu.
- **Informacja zwrotna w czasie rzeczywistym:** Klienci mogą pokazywać paski postępu lub logi, co sprawia, że aplikacja jest bardziej responsywna.
- **Łatwiejsze debugowanie i monitorowanie:** Programiści i użytkownicy widzą, gdzie proces może się opóźniać lub utknąć.

### Jak zaimplementować powiadomienia o postępie

Oto sposób, w jaki możesz zaimplementować powiadomienia o postępie w MCP:

- **Po stronie serwera:** Używaj `ctx.info()` lub `ctx.log()` do wysyłania powiadomień w trakcie przetwarzania każdego elementu. Wysyła to wiadomość do klienta zanim gotowy będzie główny wynik.
- **Po stronie klienta:** Implementuj handler wiadomości, który nasłuchuje i wyświetla powiadomienia w miarę nadejścia. Handler rozróżnia powiadomienia od finalnego wyniku.

**Przykład po stronie serwera:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Przykład klienta:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Rozważania dotyczące bezpieczeństwa

Bezpieczeństwo powinno być najwyższym priorytetem podczas implementacji każdego serwera, szczególnie przy użyciu transportów opartych na HTTP, takich jak Streamable HTTP w MCP.

Wdrażając serwery MCP z transportami opartymi na HTTP, bezpieczeństwo staje się sprawą nadrzędną, która wymaga szczególnej uwagi w kontekście wielu wektorów ataku i mechanizmów ochronnych.

### Przegląd

Bezpieczeństwo ma kluczowe znaczenie przy udostępnianiu serwerów MCP przez HTTP. Streamable HTTP wprowadza nowe powierzchnie ataku i wymaga starannej konfiguracji.

Oto kilka kluczowych zagadnień związanych z bezpieczeństwem:

- **Weryfikacja nagłówka Origin**: Zawsze weryfikuj nagłówek `Origin`, aby zapobiec atakom DNS rebinding.
- **Bindowanie do localhost**: Dla lokalnego rozwoju binduj serwery do `localhost`, aby nie udostępniać ich publicznie w internecie.
- **Uwierzytelnianie**: Wdrażaj uwierzytelnianie (np. klucze API, OAuth) w środowisku produkcyjnym.
- **CORS**: Konfiguruj polityki Cross-Origin Resource Sharing (CORS), aby ograniczyć dostęp.
- **HTTPS**: Używaj HTTPS w produkcji, aby szyfrować ruch.

### Najlepsze praktyki

Dodatkowo, oto kilka najlepszych praktyk, których należy przestrzegać podczas implementacji zabezpieczeń w Twoim strumieniowym serwerze MCP:

- Nigdy nie ufaj przychodzącym żądaniom bez weryfikacji.
- Loguj i monitoruj wszystkie dostęp i błędy.
- Regularnie aktualizuj zależności, aby załatać luki bezpieczeństwa.

### Wyzwania

Spotkasz się z pewnymi wyzwaniami podczas implementacji zabezpieczeń w strumieniowych serwerach MCP:

- Równoważenie bezpieczeństwa z łatwością rozwoju
- Zapewnienie kompatybilności z różnymi środowiskami klientów


## Aktualizacja z SSE do Streamable HTTP

Dla aplikacji obecnie korzystających z Server-Sent Events (SSE), migracja do Streamable HTTP zapewnia rozszerzone możliwości i lepszą długoterminową stabilność dla Twoich implementacji MCP.

### Dlaczego uaktualniać?

Istnieją dwa przekonujące powody, aby przejść z SSE na Streamable HTTP:

- Streamable HTTP oferuje lepszą skalowalność, kompatybilność i bogatsze wsparcie powiadomień niż SSE.
- Jest zalecanym transportem dla nowych aplikacji MCP.

### Kroki migracji

Oto jak możesz przeprowadzić migrację z SSE na Streamable HTTP w swoich aplikacjach MCP:

- **Zaktualizuj kod serwera**, aby używał `transport="streamable-http"` w `mcp.run()`.
- **Zaktualizuj kod klienta**, aby używał `streamablehttp_client` zamiast klienta SSE.
- **Zaimplementuj obsługę wiadomości** po stronie klienta do przetwarzania powiadomień.
- **Przetestuj kompatybilność** z istniejącymi narzędziami i procesami.

### Utrzymywanie kompatybilności

Zaleca się utrzymanie kompatybilności z istniejącymi klientami SSE podczas procesu migracji. Oto kilka strategii:

- Możesz wspierać zarówno SSE, jak i Streamable HTTP, obsługując oba transporty na różnych punktach końcowych.
- Stopniowo migruj klientów do nowego transportu.

### Wyzwania

Upewnij się, że podczas migracji rozwiązujesz następujące wyzwania:

- Zapewnienie, że wszyscy klienci zostaną zaktualizowani
- Radzenie sobie z różnicami w dostarczaniu powiadomień

### Zadanie: Zbuduj własną aplikację strumieniową MCP

**Scenariusz:**
Zbuduj serwer i klienta MCP, gdzie serwer przetwarza listę elementów (np. pliki lub dokumenty) i wysyła powiadomienie dla każdego przetworzonego elementu. Klient powinien wyświetlać każde powiadomienie natychmiast po jego nadejściu.

**Kroki:**

1. Zaimplementuj narzędzie serwerowe, które przetwarza listę i wysyła powiadomienia dla każdego elementu.
2. Zaimplementuj klienta z obsługą wiadomości, aby na bieżąco wyświetlać powiadomienia.
3. Przetestuj swoje rozwiązanie, uruchamiając zarówno serwer, jak i klienta, i obserwuj powiadomienia.

[Rozwiązanie](./solution/README.md)

## Dalsza lektura i co dalej?

Aby kontynuować swoją przygodę ze strumieniowaniem MCP i poszerzyć wiedzę, ta sekcja zawiera dodatkowe źródła i sugestie kolejnych kroków do budowania bardziej zaawansowanych aplikacji.

### Dalsza lektura

- [Microsoft: Wprowadzenie do HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS w ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Co dalej?

- Spróbuj zbudować bardziej zaawansowane narzędzia MCP wykorzystujące streaming do analiz w czasie rzeczywistym, czatu lub współpracy w edycji.
- Zbadaj integrację strumieniowania MCP z frameworkami frontendowymi (React, Vue itp.) dla na żywo aktualizacji UI.
- Następny temat: [Wykorzystanie AI Toolkit dla VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->