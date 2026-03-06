# Praktyczna implementacja

[![Jak budować, testować i wdrażać aplikacje MCP przy użyciu prawdziwych narzędzi i procesów](../../../translated_images/pl/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

Praktyczna implementacja to moment, w którym potęga Model Context Protocol (MCP) staje się namacalna. Choć zrozumienie teorii i architektury stojącej za MCP jest ważne, prawdziwa wartość pojawia się, gdy zastosujesz te koncepcje do budowy, testowania i wdrażania rozwiązań rozwiązujących rzeczywiste problemy. Ten rozdział wypełnia lukę między wiedzą koncepcyjną a praktycznym rozwojem, prowadząc Cię przez proces tworzenia aplikacji opartych na MCP.

Niezależnie od tego, czy tworzysz inteligentnych asystentów, integrujesz AI z procesami biznesowymi, czy budujesz niestandardowe narzędzia do przetwarzania danych, MCP zapewnia elastyczną podstawę. Jego językowo-neutralny projekt i oficjalne SDK dla popularnych języków programowania czynią go dostępnym dla szerokiego grona deweloperów. Wykorzystując te SDK, możesz szybko tworzyć prototypy, iterować i skalować swoje rozwiązania na różnych platformach i środowiskach.

W kolejnych sekcjach znajdziesz praktyczne przykłady, przykładowy kod oraz strategie wdrażania, które pokazują, jak zaimplementować MCP w C#, Java ze Springiem, TypeScript, JavaScript i Pythonie. Nauczysz się również, jak debugować i testować serwery MCP, zarządzać API oraz wdrażać rozwiązania w chmurze przy użyciu Azure. Te praktyczne zasoby pomogą Ci przyspieszyć naukę i zbudować pewnie solidne, produkcyjne aplikacje MCP.

## Przegląd

Lekcja koncentruje się na praktycznych aspektach implementacji MCP w różnych językach programowania. Zbadamy, jak korzystać z MCP SDK w C#, Java ze Springiem, TypeScript, JavaScript i Pythonie, aby budować solidne aplikacje, debugować i testować serwery MCP oraz tworzyć wielokrotnego użytku zasoby, prompty i narzędzia.

## Cele nauki

Po ukończeniu tej lekcji będziesz mógł:

- Implementować rozwiązania MCP za pomocą oficjalnych SDK w różnych językach programowania
- Systematycznie debugować i testować serwery MCP
- Tworzyć i używać funkcji serwera (Zasoby, Promptsy i Narzędzia)
- Projektować efektywne przepływy pracy MCP dla złożonych zadań
- Optymalizować implementacje MCP pod kątem wydajności i niezawodności

## Oficjalne zasoby SDK

Model Context Protocol oferuje oficjalne SDK dla wielu języków (zgodne ze [specyfikacją MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java ze Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Uwaga:** wymaga zależności od [Project Reactor](https://projectreactor.io). (Zobacz [dyskusję issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Praca z MCP SDK

Ta sekcja dostarcza praktycznych przykładów implementacji MCP w różnych językach programowania. Przykładowy kod znajduje się w katalogu `samples`, zorganizowanym według języka.

### Dostępne przykłady

Repozytorium zawiera [przykładowe implementacje](../../../04-PracticalImplementation/samples) w następujących językach:

- [C#](./samples/csharp/README.md)
- [Java ze Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Każdy przykład demonstruje kluczowe koncepcje i wzorce implementacji MCP dla danego języka i ekosystemu.

### Praktyczne przewodniki

Dodatkowe przewodniki dotyczące praktycznej implementacji MCP:

- [Paginacja i duże zestawy wyników](./pagination/README.md) - obsługa paginacji kursora dla narzędzi, zasobów i dużych zbiorów danych

## Podstawowe funkcje serwera

Serwery MCP mogą implementować dowolną kombinację następujących funkcji:

### Zasoby

Zasoby dostarczają kontekst i dane do wykorzystania przez użytkownika lub model AI:

- Repozytoria dokumentów
- Bazy wiedzy
- Strukturalne źródła danych
- Systemy plików

### Promptsy

Prompty to szablonowe wiadomości i przepływy dla użytkowników:

- Zdefiniowane szablony rozmów
- Prowadzone wzorce interakcji
- Specjalistyczne struktury dialogowe

### Narzędzia

Narzędzia to funkcje, które model AI może wykonywać:

- Narzędzia do przetwarzania danych
- Integracje z zewnętrznymi API
- Możliwości obliczeniowe
- Funkcjonalność wyszukiwania

## Przykładowe implementacje: Implementacja C#

Oficjalne repozytorium SDK C# zawiera kilka przykładowych implementacji pokazujących różne aspekty MCP:

- **Podstawowy klient MCP**: prosty przykład pokazujący, jak stworzyć klienta MCP i wywołać narzędzia
- **Podstawowy serwer MCP**: minimalna implementacja serwera z podstawową rejestracją narzędzi
- **Zaawansowany serwer MCP**: serwer z pełną funkcjonalnością, rejestracją narzędzi, uwierzytelnianiem i obsługą błędów
- **Integracja z ASP.NET**: przykłady demonstrujące integrację z ASP.NET Core
- **Wzorce implementacji narzędzi**: różne wzorce implementacji narzędzi o różnym poziomie złożoności

SDK MCP dla C# jest w wersji podglądowej i API mogą się zmieniać. Będziemy na bieżąco aktualizować ten blog wraz z ewolucją SDK.

### Kluczowe funkcje

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Budowa [pierwszego serwera MCP](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Dla kompletnych przykładów implementacji C# odwiedź [oficjalne repozytorium przykładów SDK C#](https://github.com/modelcontextprotocol/csharp-sdk)

## Przykładowa implementacja: Implementacja Java ze Spring

SDK Java ze Spring oferuje solidne opcje implementacji MCP z funkcjami na poziomie korporacyjnym.

### Kluczowe funkcje

- Integracja ze Spring Framework
- Silne typowanie
- Wsparcie programowania reaktywnego
- Obszerna obsługa błędów

Dla kompletnego przykładu implementacji Java ze Spring zobacz [przykład Java ze Spring](samples/java/containerapp/README.md) w katalogu z przykładami.

## Przykładowa implementacja: Implementacja JavaScript

SDK JavaScript oferuje lekkie i elastyczne podejście do implementacji MCP.

### Kluczowe funkcje

- Wsparcie Node.js i przeglądarki
- API oparte na Promise
- Łatwa integracja z Express i innymi frameworkami
- Wsparcie WebSocket do streamingu

Dla kompletnego przykładu implementacji JavaScript zobacz [przykład JavaScript](samples/javascript/README.md) w katalogu z przykładami.

## Przykładowa implementacja: Implementacja Python

SDK Python oferuje „pythoniczne” podejście do implementacji MCP z doskonałą integracją z frameworkami ML.

### Kluczowe funkcje

- Wsparcie async/await z asyncio
- Integracja FastAPI
- Prosta rejestracja narzędzi
- Natywna integracja z popularnymi bibliotekami ML

Dla kompletnego przykładu implementacji Python zobacz [przykład Python](samples/python/README.md) w katalogu z przykładami.

## Zarządzanie API

Azure API Management to doskonałe rozwiązanie, aby zabezpieczyć serwery MCP. Pomysł polega na umieszczeniu instancji Azure API Management przed Twoim serwerem MCP, która obsłuży funkcje, które mogą być potrzebne, takie jak:

- limitowanie liczby żądań
- zarządzanie tokenami
- monitorowanie
- równoważenie obciążenia
- bezpieczeństwo

### Przykład Azure

Oto przykład Azure wykonujący dokładnie to, czyli [tworzenie serwera MCP i zabezpieczanie go za pomocą Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Zobacz, jak przebiega przepływ autoryzacji na poniższym obrazku:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Na powyższym obrazku dzieje się następujące:

- Proces uwierzytelniania/autoryzacji odbywa się przy użyciu Microsoft Entra.
- Azure API Management działa jako brama i używa polityk do kierowania i zarządzania ruchem.
- Azure Monitor loguje wszystkie żądania do dalszej analizy.

#### Przepływ autoryzacji

Przyjrzyjmy się przepływowi autoryzacji bardziej szczegółowo:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Specyfikacja autoryzacji MCP

Dowiedz się więcej o [specyfikacji autoryzacji MCP](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Wdrażanie zdalnego serwera MCP na Azure

Zobaczmy, czy możemy wdrożyć przykład, o którym wspomnieliśmy wcześniej:

1. Sklonuj repozytorium

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Zarejestruj dostawcę zasobów `Microsoft.App`.

   - Jeśli używasz Azure CLI, uruchom `az provider register --namespace Microsoft.App --wait`.
   - Jeśli używasz Azure PowerShell, uruchom `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Następnie po czasie sprawdź `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`, aby potwierdzić, czy rejestracja jest zakończona.

1. Uruchom ten [azd](https://aka.ms/azd) polecenie, aby udostępnić usługę zarządzania API, funkcję aplikacji (z kodem) oraz wszystkie potrzebne zasoby Azure

    ```shell
    azd up
    ```

    To polecenie powinno wdrożyć wszystkie zasoby w chmurze na Azure

### Testowanie serwera za pomocą MCP Inspector

1. W **nowym oknie terminala** zainstaluj i uruchom MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Powinieneś zobaczyć interfejs podobny do:

    ![Connect to Node inspector](../../../translated_images/pl/connect.141db0b2bd05f096.webp)

1. Kliknij CTRL, aby załadować aplikację webową MCP Inspector z wyświetlonego URL (np. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Ustaw typ transportu na `SSE`
1. Ustaw URL na działający endpoint API Management SSE wyświetlony po `azd up` i **Połącz**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Lista narzędzi**. Kliknij narzędzie i **Uruchom narzędzie**.

Jeśli wszystkie kroki przebiegły pomyślnie, powinieneś być teraz połączony z serwerem MCP i móc wywołać narzędzie.

## Serwery MCP dla Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Ten zestaw repozytoriów stanowi szybki szablon do budowy i wdrażania niestandardowych zdalnych serwerów MCP (Model Context Protocol) z użyciem Azure Functions w Pythonie, C# .NET lub Node/TypeScript.

Przykłady te oferują kompletne rozwiązanie umożliwiające deweloperom:

- Budowanie i uruchamianie lokalnie: rozwój i debugowanie serwera MCP na lokalnej maszynie
- Wdrażanie do Azure: łatwe wdrażanie do chmury za pomocą prostego polecenia azd up
- Łączenie się z klientami: łączenie z serwerem MCP z różnych klientów, w tym z trybu agenta Copilot w VS Code oraz narzędzia MCP Inspector

### Kluczowe funkcje

- Bezpieczeństwo zaprojektowane od podstaw: serwer MCP jest zabezpieczony przy użyciu kluczy i HTTPS
- Opcje uwierzytelniania: obsługa OAuth przez wbudowane uwierzytelnianie i/lub API Management
- Izolacja sieciowa: umożliwia izolację sieciową przy użyciu Azure Virtual Networks (VNET)
- Architektura bezserwerowa: wykorzystuje Azure Functions do skalowalnego, zdarzeniowego wykonywania
- Lokalny rozwój: kompleksowe wsparcie lokalnego rozwoju i debugowania
- Proste wdrożenie: uproszczony proces wdrażania do Azure

Repozytorium zawiera wszystkie niezbędne pliki konfiguracyjne, kod źródłowy oraz definicje infrastruktury, aby szybko rozpocząć pracę z produkcyjną implementacją serwera MCP.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Przykładowa implementacja MCP z użyciem Azure Functions i Pythona

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Przykładowa implementacja MCP z użyciem Azure Functions i C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Przykładowa implementacja MCP z użyciem Azure Functions i Node/TypeScript.

## Najważniejsze wnioski

- SDK MCP dostarczają narzędzia specyficzne dla języka do implementacji solidnych rozwiązań MCP
- Proces debugowania i testowania jest kluczowy dla niezawodnych aplikacji MCP
- Szablony promptów wielokrotnego użytku umożliwiają spójne interakcje AI
- Dobrze zaprojektowane przepływy pracy mogą orkiestrację złożonych zadań z użyciem wielu narzędzi
- Implementacja rozwiązań MCP wymaga uwzględnienia bezpieczeństwa, wydajności i obsługi błędów

## Ćwiczenie

Zaprojektuj praktyczny przepływ pracy MCP, który rozwiązuje realny problem w twojej dziedzinie:

1. Zidentyfikuj 3-4 narzędzia, które byłyby użyteczne do rozwiązania tego problemu
2. Stwórz diagram przepływu pokazujący, jak te narzędzia wchodzą ze sobą w interakcję
3. Zaimplementuj podstawową wersję jednego z narzędzi w wybranym przez siebie języku
4. Stwórz szablon prompta, który pomoże modelowi efektywnie używać twojego narzędzia

## Dodatkowe zasoby

---

## Co dalej

Dalej: [Zaawansowane tematy](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usług tłumaczeniowych AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku krytycznych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->