## Rozpoczęcie  

[![Zbuduj swój pierwszy serwer MCP](../../../translated_images/pl/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.png)](https://youtu.be/sNDZO9N4m9Y)

_(Kliknij obrazek powyżej, aby obejrzeć wideo z tej lekcji)_

Ta sekcja składa się z kilku lekcji:

- **1 Twój pierwszy serwer**. W tej pierwszej lekcji nauczysz się, jak stworzyć swój pierwszy serwer i sprawdzić go za pomocą narzędzia inspektora, które jest cennym sposobem testowania i debugowania serwera, [do lekcji](01-first-server/README.md)

- **2 Klient**. W tej lekcji nauczysz się, jak napisać klienta, który może połączyć się z Twoim serwerem, [do lekcji](02-client/README.md)

- **3 Klient z LLM**. Jeszcze lepszym sposobem pisania klienta jest dodanie do niego LLM, dzięki czemu może "negocjować" z serwerem, co ma zrobić, [do lekcji](03-llm-client/README.md)

- **4 Konsumowanie serwera w trybie GitHub Copilot Agent w Visual Studio Code**. Tutaj omawiamy uruchamianie serwera MCP z poziomu Visual Studio Code, [do lekcji](04-vscode/README.md)

- **5 Serwer transportowy stdio**. Transport stdio jest zalecanym standardem komunikacji między serwerem a klientem MCP w obecnej specyfikacji, zapewniającym bezpieczną komunikację opartą na podprocesach, [do lekcji](05-stdio-server/README.md)

- **6 HTTP Streaming z MCP (Streamable HTTP)**. Dowiedz się o nowoczesnym strumieniowaniu HTTP, powiadomieniach o postępie oraz jak wdrożyć skalowalne, w czasie rzeczywistym serwery i klientów MCP za pomocą Streamable HTTP, [do lekcji](06-http-streaming/README.md)

- **7 Wykorzystanie AI Toolkit dla VSCode** do konsumpcji i testowania klientów oraz serwerów MCP, [do lekcji](07-aitk/README.md)

- **8 Testowanie**. Skupimy się tutaj szczególnie na tym, jak testować serwer i klienta na różne sposoby, [do lekcji](08-testing/README.md)

- **9 Wdrożenie**. Ten rozdział omawia różne sposoby wdrażania rozwiązań MCP, [do lekcji](09-deployment/README.md)

- **10 Zaawansowane użycie serwera**. Ten rozdział obejmuje zaawansowane użycie serwera, [do lekcji](./10-advanced/README.md)

- **11 Autoryzacja**. Ten rozdział omawia, jak dodać prostą autoryzację, od Basic Auth po użycie JWT i RBAC. Zaleca się rozpoczęcie tutaj, a następnie zapoznanie się z zaawansowanymi tematami w rozdziale 5 oraz przeprowadzenie dodatkowego zabezpieczenia zgodnie z zaleceniami w rozdziale 2, [do lekcji](./11-simple-auth/README.md)

Model Context Protocol (MCP) to otwarty protokół, który standaryzuje sposób, w jaki aplikacje dostarczają kontekst do LLM. Można myśleć o MCP jak o porcie USB-C dla aplikacji AI - zapewnia ustandaryzowany sposób łączenia modeli AI z różnymi źródłami danych i narzędziami.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Skonfigurować środowiska programistyczne dla MCP w C#, Java, Python, TypeScript i JavaScript
- Zbudować i wdrożyć podstawowe serwery MCP z niestandardowymi funkcjami (zasoby, podpowiedzi, narzędzia)
- Tworzyć aplikacje hostujące, które łączą się z serwerami MCP
- Testować i debugować implementacje MCP
- Zrozumieć typowe wyzwania związane z konfiguracją i ich rozwiązania
- Połączyć swoje implementacje MCP z popularnymi usługami LLM

## Konfiguracja środowiska MCP

Zanim zaczniesz pracę z MCP, ważne jest, aby przygotować środowisko programistyczne i zrozumieć podstawowy przepływ pracy. Ta sekcja poprowadzi Cię przez początkowe kroki konfiguracji, aby zapewnić płynny start z MCP.

### Wymagania wstępne

Przed rozpoczęciem pracy z MCP upewnij się, że masz:

- **Środowisko programistyczne**: Dla wybranego języka (C#, Java, Python, TypeScript lub JavaScript)
- **IDE/Edytor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm lub dowolny nowoczesny edytor kodu
- **Menadżery pakietów**: NuGet, Maven/Gradle, pip lub npm/yarn
- **Klucze API**: Dla dowolnych usług AI, które planujesz używać w swoich aplikacjach hostujących

### Oficjalne SDK

W nadchodzących rozdziałach zobaczysz rozwiązania zbudowane w Python, TypeScript, Java i .NET. Oto wszystkie oficjalnie wspierane SDK.

MCP oferuje oficjalne SDK dla wielu języków:
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Utrzymywane we współpracy z Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Utrzymywane we współpracy z Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Oficjalna implementacja TypeScript
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Oficjalna implementacja Python
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Oficjalna implementacja Kotlin
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Utrzymywane we współpracy z Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Oficjalna implementacja Rust

## Kluczowe informacje

- Konfiguracja środowiska programistycznego MCP jest prosta dzięki SDK specyficznym dla języka
- Budowanie serwerów MCP polega na tworzeniu i rejestrowaniu narzędzi z jasnymi schematami
- Klienci MCP łączą się z serwerami i modelami, aby korzystać z rozszerzonych możliwości
- Testowanie i debugowanie są kluczowe dla niezawodnych implementacji MCP
- Opcje wdrożenia obejmują lokalny rozwój oraz rozwiązania w chmurze

## Ćwiczenia praktyczne

Posiadamy zestaw przykładów, które uzupełniają ćwiczenia, które zobaczysz we wszystkich rozdziałach tej sekcji. Dodatkowo każdy rozdział zawiera własne ćwiczenia i zadania.

- [Kalkulator w Javie](./samples/java/calculator/README.md)
- [Kalkulator w .Net](../../../03-GettingStarted/samples/csharp)
- [Kalkulator w JavaScript](./samples/javascript/README.md)
- [Kalkulator w TypeScript](./samples/typescript/README.md)
- [Kalkulator w Python](../../../03-GettingStarted/samples/python)

## Dodatkowe zasoby

- [Budowanie agentów za pomocą Model Context Protocol na Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Zdalny MCP z Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Co dalej

Następne: [Tworzenie pierwszego serwera MCP](01-first-server/README.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.