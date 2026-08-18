# Dziennik zmian: Program nauczania MCP dla początkujących

Ten dokument służy jako zapis wszystkich znaczących zmian wprowadzonych w programie nauczania Model Context Protocol (MCP) dla początkujących. Zmiany są dokumentowane w porządku odwrotnym chronologicznie (najnowsze zmiany na początku).

## 29 lipca 2026

### Nowy towarzyszący moduł 08: Sidecary niezawodności i bezpieczne ponawianie prób

Dodano neutralną wobec dostawcy lekcję towarzyszącą dla narzędzi MCP, które tworzą rzeczywiste
efekty, zgodnie z ostateczną specyfikacją `2026-07-28`.

- **Nowość**: [lekcja towarzysząca sidecar niezawodności][reliability-sidecar]
  wykorzystuje jedną historię zgłoszenia wsparcia, dwa diagramy Mermaid oraz proces decyzyjny ponawiania prób,
  aby wyjaśnić klucze stabilnej pracy, atomową dopuszczalność duplikatów,
  pojednanie, dowody oraz granicę rozszerzenia Zadań.
- **Nowość**: Ćwiczenie wstrzykiwania awarii w Pythonie i SQLite z biblioteki standardowej
  korzysta z oddzielnego magazynu operacji i zgłoszeń, aby zilustrować utratę odpowiedzi
  po zatwierdzeniu efektu zewnętrznego. Sześć deterministycznych testów obejmuje naiwną
  duplikację, chronioną rekonwalescencję restartu, konflikty ładunku,
  buforowane wyniki, aktywne roszczenia oraz równoczesną dopuszczalność duplikatów.
- **Zaktualizowano**: Moduł 08 teraz linkuje lekcję towarzyszącą, identyfikuje
  ostateczny model żądania bezstanowego `2026-07-28`, rozróżnia obserwowalność OpenTelemetry
  od przestarzałej funkcji logowania MCP i ogranicza swój
  ogólny przykład ponawiania prób do operacji tylko do odczytu.
- **Opcjonalne**: Lekcja mapuje swoje przenośne koncepcje na jedno oznaczone implementację społecznościową,
  nie czyniąc usługi hostowanej ani wywołania sieciowego częścią
  ćwiczenia.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 lipca 2026

### Nowa lekcja: Kandydat do wydania specyfikacji MCP 2026-07-28

Dodano omówienie nadchodzącego kandydata do wydania specyfikacji MCP `2026-07-28` (ogłoszonego 21 maja 2026; ostateczne wydanie zaplanowane na 28 lipca 2026), podsumowane z [oficjalnego wpisu na blogu](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Podstawą programu pozostaje **Specyfikacja MCP 2025-11-25** do momentu wypuszczenia nowej wersji, więc jest to przedstawione jako wskazówki na przyszłość, a nie przepisywanie istniejących lekcji.

- **Nowość**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — pełna lekcja obejmująca bezstanowe jądro protokołu (usunięcie negocjacji `initialize` i `Mcp-Session-Id`), nowe nagłówki trasowania `Mcp-Method`/`Mcp-Name`, metadane buforowania `ttlMs`/`cacheScope`, W3C Trace Context w `_meta`, formalny framework rozszerzeń (aplikacje MCP i nowe rozszerzenie Zadań), sześć SEP wzmacniających autoryzację, wycofanie Roots/Sampling/Logging oraz przejście na pełne schematy JSON Schema 2020-12 dla schematów narzędzi.
- **Zaktualizowano** z perspektywicznymi odwołaniami do nowej lekcji:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): notatka o wersji protokołu, sekcje Sampling/Roots/Logging/Tasks oraz „Co dalej”
  - [02-Security/README.md](./02-Security/README.md): odwołanie do wzmacniania autoryzacji
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): odwołanie do bezstanowego transportu
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): odwołanie do wycofania Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): odwołanie do wycofania logowania i rozszerzenia Zadań
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): odwołanie do bezstanowego/trasowania sesji
  - [README.md](./README.md): notatka „Patrząc w przyszłość” w sekcji specyfikacji i nowy wpis `1.1` w tabeli modułów programu nauczania
  - [study_guide.md](./study_guide.md): punkty perspektywiczne w przeglądzie podstawek i datowana nota uzupełniająca
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): odwołanie do mapy transportu `mcp-session-id` przed modelem żądania bezstanowego
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): odwołanie do przeglądu modułu o wycofaniu Root Contexts/Sampling i rozszerzeniu Zadań
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): odwołanie do wzmacniania autoryzacji

## 24 czerwca 2026

### Nowa lekcja: Wykorzystanie MCP w aplikacji Copilot

- Dodano [sekcję narzędziową](./12-tooling/README.md).
- [MCP w aplikacji Copilot](./12-tooling/01-copilot-app/README.md)

## 16 czerwca 2026

### Zgodność specyfikacji MCP i walidacja przykładowa

Zweryfikowano program nauczania pod kątem obecnej **Specyfikacji MCP 2025-11-25** oraz najnowszych oficjalnych SDK, następnie skorygowano pozostałe przestarzałe odniesienia do specyfikacji i potwierdzono, że próbki nadal się kompilują i działają.

#### Korekty wersji specyfikacji (2025-06-18 / 2025-03-26 → 2025-11-25)

Zaktualizowano angielskie treści tam, gdzie dalej twierdzono, że starsza rewizja specyfikacji była *obowiązującym/najnowszym* standardem, i przekierowano linki do kanonicznych ścieżek specyfikacji w `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Zaktualizowano baner „Aktualny standard”, wprowadzenie, nagłówek zasad bezpieczeństwa rdzenia, nagłówek wymagań obowiązkowych, sekcję Microsoft Entra ID, linki do Odniesień i Zasobów oraz końcową notę bezpieczeństwa (8 odniesień) do 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Zaktualizowano link do Dodatkowych zasobów specyfikacji i baner „Aktualny standard” do 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Zastąpiono przestarzały link bezpieczeństwa i zaufania `2025-03-26` aktualną stroną najlepszych praktyk bezpieczeństwa 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Zaktualizowano oficjalny link do dokumentacji Sampling do 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Zaktualizowano odniesienie do bieżącej specyfikacji MCP oraz link do specyfikacji Dodatkowych zasobów do 2025-11-25 (historyczne notatki wycofania SSE zostawiono dla dokładności)

#### Walidacja próbek względem obecnych SDK

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` zainstalował `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` przeszedł bez błędów typów — istniejące API `McpServer`/`StdioServerTransport` są poprawne
- **Python (03-GettingStarted/01-first-server/solution/python)**: Zweryfikowano w izolowanym `.venv` z `mcp[cli]` (1.27.2); `py_compile` przeszedł, a `FastMCP.list_tools()` poprawnie zwrócił narzędzia `add` i `subtract`
- Potwierdzono, że wszystkie zakresy wersji `@modelcontextprotocol/sdk` próbek (`>=1.26.0` / `^1.26.0` / `^1.27.0`) rozwiązują się czysto do obecnej `1.29.0` bez łamiących zmian API

#### Wyrównanie wersji zależności (zamykanie luk wersji)

Podniesiono przestarzałe wersje SDK, aby każda próbka śledziła aktualne wydanie MCP, zgodnie z konwencją całego repozytorium:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Podniesiono `@modelcontextprotocol/sdk` z `^1.8.0` → `>=1.26.0` i zaktualizowano przestarzały opis pakietu `"updated for MCP 2025-06-18"` do `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** oraz **lab4/code/github_mcp_server/pyproject.toml**: Podniesiono dokładne ustalenie `mcp==1.23.0` → `mcp>=1.26.0`; wygenerowano ponownie oba pliki `uv.lock` (`uv lock`), aby pliki blokad rozwiązywały się do obecnej wersji `mcp 1.27.2` i były zsynchronizowane z manifestami

#### Analiza luki w programie nauczania — pokrycie najnowszych funkcji specyfikacji

Zweryfikowano, że program nauczania już obejmuje wszystkie prymitywy wprowadzone/rozszerzone w MCP 2025-11-25, więc nie pozostają luki w treści:
- **Sampling**: Lekcja 03-GettingStarted/14-sampling oraz 05-AdvancedTopics/mcp-sampling
- **Elicitation (w tym tryb URL)**: Udokumentowano w 01-CoreConcepts oraz 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Udokumentowano w 00-Introduction, 01-CoreConcepts oraz 05-AdvancedTopics/mcp-root-contexts
- **Tasks (eksperymentalne, długotrwałe operacje)**: Udokumentowano w 01-CoreConcepts oraz 05-AdvancedTopics/mcp-protocol-features
- **Adnotacje narzędzi** (`readOnlyHint` / `destructiveHint`): Udokumentowano w 01-CoreConcepts oraz 05-AdvancedTopics/mcp-protocol-features

### Wzmocnienie bezpieczeństwa i usuwanie luk w zależnościach

Przeprowadzono pełną kontrolę bezpieczeństwa każdego manifestu zależności i kodu źródłowego próbek, następnie usunięto wszystkie zgłoszone ostrzeżenia npm oraz jedno znalezisko na poziomie kodu. Po usunięciu raport `npm audit` wskazuje **0 luk** w każdym audytowanym katalogu.

#### Luki bezpieczeństwa w zależnościach npm (przechodnie) — naprawione

Przeaudytowano wszystkie 15 zaangażowanych plików `package-lock.json`. Luki ograniczały się do zależności przechodnich ściąganych przez narzędzie developerskie MCP Inspector, klienta OpenAI oraz MCP SDK; wszystkie zostały teraz rozwiązane bez łamania próbek:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** oraz **lab3/code/weather_mcp/inspector**: Podniesiono `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), co usunęło powiązane ostrzeżenia dla `ajv`, `brace-expansion`, `diff`, `path-to-regexp` i `ws`. Dodano wpis npm `overrides` wymuszający załataną wersję `shell-quote@1.8.4` by wyeliminować pozostałe krytyczne ostrzeżenie z `concurrently`; wygenerowano ponownie oba pliki locka (obecnie 0 luk)
- **03-GettingStarted/samples/typescript**: `npm audit fix` zaktualizował zależność przechodnią `qs` (umiarkowana) do załatanej wersji
- **03-GettingStarted/samples/javascript**: `npm audit fix` zaktualizował zależność przechodnią `hono` (umiarkowana) do załatanej wersji
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` zaktualizował zależność przechodnią `form-data` (wysoka) do załatanej wersji
- **03-GettingStarted/11-simple-auth/solution/typescript**: Wygenerowano brakujący `package-lock.json`, aby projekt był powtarzalny i poddany audytowi (0 luk)

#### Naprawa bezpieczeństwa na poziomie kodu (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Usunięto `shell=True` z narzędzia `open_in_vscode`. Poprzednie `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` pozwalało na interpretację znaków metaznaków powłoki w ścieżce folderu przez `cmd.exe` (wektor ataku wstrzyknięcia polecenia). Teraz uruchamia bezpośrednio rozwiązaną ścieżkę `Code.exe` z folderem jako argumentem — bez powłoki — co jest funkcjonalnie równoważne i bezpieczne

#### Audyt zależności Pythona

- Przeaudytowano wszystkie zestawy wymagań Pythona za pomocą `pip-audit`. `05-AdvancedTopics` i `03-GettingStarted/samples/python` nie zgłosiły **żadnych znanych luk** (ich zakresy `mcp` / `httpx` / `pydantic` / `python-dotenv` rozwiązują się do obecnych załatanych wydań)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` oznaczył przechodnią zależność **`werkzeug` 3.1.1** z trzema ostrzeżeniami DoS `safe_join` dotyczących nazwy urządzenia Windows — `CVE-2025-66221`, `CVE-2026-21860` oraz `CVE-2026-27199` (wszystkie naprawione w 3.1.6). Dodano explicite zabezpieczające przypięcie wersji `werkzeug>=3.1.6` aby rozwiązać załataną wersję; zweryfikowano, że ograniczenie resolwuje się czysto z pakietem `chainlit` / `mcp` / `semantic-kernel`

### Rebranding nazwy produktu

Zaktualizowano całą zawartość programu nauczania, aby odzwierciedlić rebranding produktów Microsoft:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Zaktualizowano link do społeczności Discord

- **AGENTS.md**: Zaktualizowano odniesienie do serwera Discord
- **README.md**: Zaktualizowano odniesienia do ekosystemu technologicznego
- **study_guide.md**: Zaktualizowano odniesienia do studiów przypadków
- **05-AdvancedTopics/README.md**: Zaktualizowano tytuł i opis Modułu 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Zaktualizowano nagłówek sekcji i opis
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Pełna aktualizacja tytułu i treści modułu
- **05-AdvancedTopics/mcp-security-entra/README.md**: Zaktualizowano link do referencji krzyżowej
- **07-LessonsfromEarlyAdoption/README.md**: Zaktualizowano odniesienia do studiów przypadków
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Zaktualizowano nagłówek Sekcji 9, odznaki i możliwości
- **08-BestPractices/README.md**: Zaktualizowano link do społeczności Discord
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Zaktualizowano odniesienie do kanału Discord
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Zaktualizowano odniesienie do wdrożenia modelu
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Zaktualizowano tabelę usług AI
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Zaktualizowano odniesienia do zasobów

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Zaktualizowano główne odniesienia w programie nauczania
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Zaktualizowano tytuł modułu, przegląd oraz wszystkie nagłówki modułów
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Zaktualizowano tytuł, cele nauki, instrukcje konfiguracji i zasoby
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Zaktualizowano tytuł, cele nauki, tabelę hostów MCP oraz odniesienia krzyżowe
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Zaktualizowano tytuł, odznaki, wymagania wstępne i zasoby
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Zaktualizowano odniesienia do Agent Builder i link do opinii
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Zaktualizowano wymagania wstępne i odniesienia do rozszerzeń

---

## 11 kwietnia 2026

### Nowa lekcja, poprawki dokumentacji i aktualizacje zależności

#### Dodano nową zawartość programu nauczania

**Moduł 05 - Tematy zaawansowane**
- **Lekcja 5.17: Adwersarialne rozumowanie wieloagentowe z MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nowy kompleksowy przewodnik omawiający wzorzec debaty adwersarialnej dla systemów wieloagentowych
  - Diagram architektury Mermaid: dwóch agentów → współdzielony serwer MCP → transkrypt debaty → sędzia → werdykt
  - Wspólny serwer narzędzi MCP (`web_search` + `run_python`) zaimplementowany w Pythonie i TypeScript
  - Przeciwdziałające sobie systemowe prompt’y (FOR / AGAINST / Sędzia) z wyraźnymi wymaganiami użycia narzędzi
  - Orkiestrator debaty w Pythonie, TypeScript i C# zarządzający rundami i trasowaniem argumentów
  - Okablowanie MCP `ClientSession` dla orkiestratora do rzeczywistych wywołań narzędzi
  - Tabela zastosowań (wykrywanie halucynacji, modelowanie zagrożeń, przegląd projektowania API, weryfikacja faktów, wybór technologii)
  - Rozważania bezpieczeństwa: wykonywanie w piaskownicy, walidacja wywołań narzędzi, ograniczanie tempa, logowanie audytu
  - Ustrukturyzowane ćwiczenie z trzema praktycznymi scenariuszami (przegląd kodu, decyzja architektoniczna, moderacja treści)

#### Poprawki dokumentacji

**Moduł 03 - Rozpoczęcie pracy**
- **05-stdio-server/README.md**: Naprawiono niekompletny przykład serwera stdio w TypeScript — dodano brakującą instancję transportu (`new StdioServerTransport()`) oraz wywołanie `server.connect(transport)` zgodnie z przykładami Pythona i .NET w tej samej sekcji
- **14-sampling/README.md**: Poprawiono literówkę — poprawiono `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Aktualizacje programu nauczania

**Główny README.md**
- Dodano wpis 5.17 (Adwersarialne rozumowanie wieloagentowe z MCP) do tabeli programu nauczania z bezpośrednim linkiem do nowej lekcji

**05-AdvancedTopics/README.md**
- Dodano wiersz lekcji 5.17 do tabeli lekcji

**study_guide.md**
- Dodano temat Adwersarialnego rozumowania wieloagentowego do mapy myśli i opisu prozatorskiego Tematów Zaawansowanych

#### Poprawki kodu i bezpieczeństwa

**Moduł 05 - Adwersarialni agenci (`mcp-adversarial-agents`)**
- **Poprawka bezpieczeństwa — wstrzyknięcie polecenia**: Zastąpiono interpolację shell `execSync` przez `execFile` + `promisify` w narzędziu `run_python` TypeScript, eliminując powierzchnię wstrzyknięcia poleceń (kod kontrolowany przez LLM jest teraz przekazywany jako dosłowny element argv bez udziału shella)
- **Okablowanie pętli narzędzi MCP**: Zaktualizowano orkiestrator debaty Python do używania klienta `AsyncAnthropic` (zastępując blokujący synchronizujący `Anthropic`), przekazywania na żywo `ClientSession` bezpośrednio do każdej tury agenta, pobierania definicji narzędzi przez `session.list_tools()` w każdej turze oraz wysyłania bloków `tool_use` przez `session.call_tool()` w pętli, aż model wyemituje końcową tekstową odpowiedź

#### Aktualizacje zależności

- Podniesiono `hono` do wersji 4.12.12 w wielu pakietach (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Podniesiono `@hono/node-server` z 1.19.11 do 1.19.13 w pakietach TypeScript
- Podniesiono `cryptography` z 46.0.5 do 46.0.7 w pakietach Python (labs 3 i 4 w 10-StreamliningAIWorkflows)
- Podniesiono `lodash` z 4.17.23 do 4.18.1 w inspektorze 10-StreamliningAIWorkflows

#### Tłumaczenia

- Zsynchronizowano tłumaczenia dla 48+ języków z najnowszymi zmianami źródłowymi (aktualizacja i18n)

---

## 5 lutego 2026

### Ulepszenia walidacji i nawigacji w całym repozytorium

#### Dodano nową zawartość programu nauczania

**Moduł 03 - Rozpoczęcie pracy**
- **12-mcp-hosts/README.md**: Nowy kompleksowy przewodnik po konfiguracji hostów MCP
  - Przykłady konfiguracji Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Szablony konfiguracji JSON dla wszystkich głównych hostów
  - Tabela porównawcza typów transportu (stdio, SSE/HTTP, WebSocket)
  - Rozwiązywanie typowych problemów z połączeniem
  - Najlepsze praktyki bezpieczeństwa konfiguracji hostów

- **13-mcp-inspector/README.md**: Nowy przewodnik debugowania dla MCP Inspector
  - Metody instalacji (npx, npm global, ze źródła)
  - Łączenie się z serwerami przez stdio i HTTP/SSE
  - Testowanie narzędzi, zasobów i przepływów pracy promptów
  - Integracja MCP Inspector z VS Code
  - Typowe scenariusze debugowania z rozwiązaniami

**Moduł 04 - Implementacja praktyczna**
- **pagination/README.md**: Nowy przewodnik implementacji paginacji
  - Wzorce paginacji opartej na kursorze w Pythonie, TypeScript i Javie
  - Obsługa paginacji po stronie klienta
  - Strategie projektowania kursorów (nieprzezroczysty vs. ustrukturyzowany)
  - Zalecenia optymalizacji wydajności

**Moduł 05 - Tematy zaawansowane**
- **mcp-protocol-features/README.md**: Dogłębna analiza nowych funkcji protokołu
  - Implementacja powiadomień o postępie
  - Wzorce anulowania żądań
  - Szablony zasobów z wzorcami URI
  - Zarządzanie cyklem życia serwera
  - Kontrola poziomu logowania
  - Wzorce obsługi błędów z kodami JSON-RPC

#### Poprawki nawigacji (zaktualizowano 24+ plików)

**Główne pliki README modułów**
 Obecnie zawierają linki zarówno do pierwszej lekcji, JAK I następnego modułu

**Podkatalogi 02-Security**
- Wszystkie 5 dodatkowych dokumentów bezpieczeństwa ma teraz nawigację "Co dalej"

**Pliki 09-CaseStudy**
- Wszystkie pliki ze studiów przypadków mają teraz nawigację sekwencyjną

**Laboratoria 10-StreamliningAI**
Dodano sekcję Co dalej do przeglądu Modułu 10 i Modułu 11

#### Poprawki kodu i treści

**Aktualizacje SDK i zależności**
Naprawiono pustą wersję openai na `^4.95.0`
Zaktualizowano SDK z `^1.8.0` do `>=1.26.0`
Zaktualizowano szpilki wersji mcp na `>=1.26.0`

**Poprawki kodu**
Naprawiono nieprawidłowy model `gpt-4o-mini` na `gpt-4.1-mini`

**Poprawki treści**
Naprawiono uszkodzony link `READMEmd` → `README.md`, poprawiono nagłówek programu nauczania `Module 1-3` → `Module 0-3`, poprawiono ścieżkę z uwzględnieniem wielkości liter
Usunięto uszkodzoną zduplikowaną treść studium przypadku 5

**Ulepszenia dla początkujących**
Dodano właściwe wprowadzenie, cele nauki i wymagania wstępne dla początkujących

#### Aktualizacje programu nauczania

**Główny README.md**
- Dodano wpisy 3.12 (Hosty MCP), 3.13 (Inspektor MCP), 4.1 (Paginacja), 5.16 (Funkcje protokołu) do tabeli programu nauczania

**README modułów**
Dodano lekcje 12 i 13 do listy lekcji
Dodano sekcję Przewodniki praktyczne z linkiem do paginacji
Dodano lekcje 5.15 (Własny transport) i 5.16 (Funkcje protokołu)

**study_guide.md**
- Zaktualizowano mapę myśli o wszystkie nowe tematy: konfiguracja hostów MCP, Inspektor MCP, strategie paginacji, dogłębna analiza funkcji protokołu

## 28 stycznia 2026

### Przegląd zgodności specyfikacji MCP 2025-11-25

#### Ulepszenia koncepcji podstawowych (01-CoreConcepts/)
- **Nowy prymityw klienta - Roots**: Dodano kompleksową dokumentację dotyczącą prymitywu klienta Roots, umożliwiającą serwerom zrozumienie granic systemu plików i uprawnień dostępu
- **Adnotacje narzędzi**: Dodano dokumentację dotyczącą zachowań narzędzi (`readOnlyHint`, `destructiveHint`) dla lepszych decyzji wykonania narzędzi
- **Wywoływanie narzędzi w Sampling**: Zaktualizowano dokumentację Sampling o parametry `tools` i `toolChoice` do wywołań narzędzi sterowanych modelem podczas żądań próbkowania
- **Tryb elicytacji URL**: Dodano dokumentację dotyczącą elicytacji opartej na URL dla zewnętrznych interakcji z inicjacją przez serwer
- **Zadania (eksperymentalne)**: Dodano nową sekcję dokumentującą eksperymentalną funkcję Zadania do trwałych opakowań wykonawczych i odroczonego pobierania wyników
- **Wsparcie ikon**: Zauważono, że narzędzia, zasoby, szablony zasobów i prompt’y mogą teraz zawierać ikony jako dodatkowe metadane

#### Aktualizacje dokumentacji
- **README.md**: Dodano odniesienie do wersji specyfikacji MCP 2025-11-25 oraz wyjaśnienie wersjonowania wg daty
- **study_guide.md**: Zaktualizowano mapę programu nauczania o Zadania i adnotacje narzędzi w sekcji Koncepcje podstawowe; zaktualizowano znacznik czasowy dokumentu

#### Weryfikacja zgodności specyfikacji
- **Wersja protokołu**: Zweryfikowano, że cała dokumentacja odnosi się do aktualnej specyfikacji MCP 2025-11-25
- **Dopasowanie architektury**: Potwierdzono dokładność dokumentacji dwóch warstw architektury (Warstwa danych + Warstwa transportu)
- **Dokumentacja prymitywów**: Zweryfikowano prymitywy serwera (Zasoby, Prompty, Narzędzia) oraz prymitywy klienta (Sampling, Elicitation, Logging, Roots)
- **Mechanizmy transportu**: Zweryfikowano dokładność dokumentacji transportu STDIO i HTTP strumieniowalnego
- **Wytyczne bezpieczeństwa**: Potwierdzono zgodność z aktualnymi najlepszymi praktykami bezpieczeństwa MCP

#### Kluczowe cechy MCP 2025-11-25 udokumentowane
- **Odkrywanie OpenID Connect**: Odkrywanie serwera uwierzytelniającego przez OIDC
- **Metadane klienta OAuth Client ID**: Zalecany mechanizm rejestracji klienta
- **JSON Schema 2020-12**: Domyślny dialekt dla definicji schematu MCP
- **System poziomów SDK**: Sformalizowane wymagania wsparcia i utrzymania funkcji SDK
- **Struktura zarządzania**: Sformalizowane Grupy Robocze i Grupy Zainteresowania w zarządzaniu MCP

### Główna aktualizacja dokumentacji bezpieczeństwa (02-Security/)

#### Integracja z warsztatem MCP Security Summit (Sherpa)
- **Nowy zasób treningowy praktyczny**: Dodano kompleksową integrację z [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) we wszystkich dokumentach dotyczących bezpieczeństwa
- **Pokrycie trasy ekspedycji**: Udokumentowano pełny przebieg od Base Camp do Summit
- **Dopasowanie do OWASP**: Wszystkie wytyczne bezpieczeństwa teraz odpowiadają ryzykom z OWASP MCP Azure Security Guide

#### Integracja OWASP MCP Top 10
- **Nowa sekcja**: Dodano tabelę ryzyk bezpieczeństwa OWASP MCP Top 10 z mitigacjami Azure do głównego README bezpieczeństwa
- **Dokumentacja oparta na ryzyku**: Zaktualizowano `mcp-security-controls-2025.md` o odniesienia do ryzyk OWASP MCP dla każdego obszaru bezpieczeństwa
- **Architektura referencyjna**: Dodano link do referencyjnej architektury OWASP MCP Azure Security Guide i wzorców implementacyjnych

#### Zaktualizowane pliki bezpieczeństwa
- **README.md**: Dodano przegląd warsztatu Sherpa, tabelę trasy ekspedycji, podsumowanie ryzyk OWASP MCP Top 10 oraz sekcję treningu praktycznego
- **mcp-security-controls-2025.md**: Zaktualizowano nagłówek na luty 2026, dodano odniesienia do ryzyk OWASP (MCP01-MCP08), naprawiono niespójności wersji specyfikacji
- **mcp-security-best-practices-2025.md**: Dodano sekcję zasobów Sherpa i OWASP, zaktualizowano znacznik czasowy
- **mcp-best-practices.md**: Dodano sekcję treningu praktycznego z linkami do Sherpa i OWASP
- **azure-content-safety-implementation.md**: Dodano odniesienie do OWASP MCP06, dopasowanie do obozu Sherpa Camp 3 oraz dodatkową sekcję zasobów

#### Dodano nowe linki do zasobów
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Indywidualne strony ryzyka OWASP MCP (MCP01-MCP10)

### Wyrównanie do Specyfikacji MCP w całym programie nauczania 2025-11-25

#### Moduł 03 - Pierwsze kroki
- **Dokumentacja SDK**: Dodano Go SDK do oficjalnej listy SDK; zaktualizowano wszystkie odniesienia do SDK zgodnie ze Specyfikacją MCP 2025-11-25
- **Doprecyzowanie transportu**: Zaktualizowano opisy transportu STDIO i HTTP Streaming z wyraźnymi odniesieniami do specyfikacji

#### Moduł 04 - Praktyczna implementacja
- **Aktualizacje SDK**: Dodano Go SDK; zaktualizowano listę SDK z odniesieniem do wersji specyfikacji
- **Specyfikacja autoryzacji**: Zaktualizowano link do specyfikacji MCP Autoryzacji do bieżącej wersji 2025-11-25

#### Moduł 05 - Tematy zaawansowane
- **Nowe funkcje**: Dodano notatkę o nowych funkcjach Specyfikacji MCP 2025-11-25 (Zadania, Adnotacje narzędzi, Elikytacja trybu URL, Korzenie)
- **Zasoby bezpieczeństwa**: Dodano odnośniki do OWASP MCP Top 10 i warsztatów Sherpa jako dodatkowe materiały

#### Moduł 06 - Wkład społeczności
- **Lista SDK**: Dodano SDK Swift i Rust; zaktualizowano link do specyfikacji do wersji 2025-11-25
- **Odniesienie do specyfikacji**: Zaktualizowano link do Specyfikacji MCP na bezpośredni adres URL specyfikacji

#### Moduł 07 - Lekcje z wczesnej adopcji
- **Aktualizacje zasobów**: Dodano link do Specyfikacji MCP 2025-11-25 oraz OWASP MCP Top 10 do dodatkowych zasobów

#### Moduł 08 - Najlepsze praktyki
- **Wersja specyfikacji**: Zaktualizowano odniesienie do Specyfikacji MCP do 2025-11-25
- **Zasoby bezpieczeństwa**: Dodano OWASP MCP Top 10 i warsztat Sherpa do dodatkowych materiałów

#### Moduł 10 - Usprawnianie przepływów pracy AI
- **Aktualizacja odznaki**: Zmieniono odznakę wersji MCP z wersji SDK (1.9.3) na wersję specyfikacji (2025-11-25)
- **Linki do zasobów**: Zaktualizowano link do Specyfikacji MCP; dodano OWASP MCP Top 10

#### Moduł 11 - Laboratoria praktyczne MCP Server
- **Odniesienie do specyfikacji**: Zaktualizowano link do Specyfikacji MCP do wersji 2025-11-25
- **Zasoby bezpieczeństwa**: Dodano OWASP MCP Top 10 do oficjalnych zasobów

## 18 grudnia 2025

### Aktualizacja dokumentacji bezpieczeństwa - Specyfikacja MCP 2025-11-25

#### Najlepsze praktyki bezpieczeństwa MCP (02-Security/mcp-best-practices.md) - Aktualizacja wersji specyfikacji
- **Aktualizacja wersji protokołu**: Zaktualizowano odniesienia do najnowszej Specyfikacji MCP 2025-11-25 (wydanej 25 listopada 2025)
  - Zaktualizowano wszystkie odniesienia wersji specyfikacji z 2025-06-18 do 2025-11-25
  - Zaktualizowano daty w dokumentach z 18 sierpnia 2025 do 18 grudnia 2025
  - Zweryfikowano, że wszystkie URL-e do specyfikacji wskazują na aktualną dokumentację
- **Weryfikacja zawartości**: Kompleksowa weryfikacja najlepszych praktyk bezpieczeństwa zgodnie z najnowszymi standardami
  - **Microsoft Security Solutions**: Zweryfikowano aktualną terminologię i linki dla Prompt Shields (dawniej "wykrywanie ryzyka Jailbreak"), Azure Content Safety, Microsoft Entra ID oraz Azure Key Vault
  - **Bezpieczeństwo OAuth 2.1**: Potwierdzono zgodność z najnowszymi najlepszymi praktykami bezpieczeństwa OAuth
  - **Standardy OWASP**: Zweryfikowano, że odniesienia do OWASP Top 10 dla LLM pozostają aktualne
  - **Usługi Azure**: Zweryfikowano wszystkie linki do dokumentacji Microsoft Azure oraz najlepsze praktyki
- **Zgodność ze standardami**: Potwierdzono aktualność wszystkich odniesionych standardów bezpieczeństwa
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Najlepsze praktyki bezpieczeństwa OAuth 2.1
  - Azure security and compliance frameworks
- **Zasoby implementacji**: Zweryfikowano wszystkie linki do przewodników implementacji i zasobów
  - Wzorce uwierzytelniania Azure API Management
  - Przewodniki integracji Microsoft Entra ID
  - Zarządzanie sekretami Azure Key Vault
  - Pipeline DevSecOps i rozwiązania monitorujące

### Zapewnienie jakości dokumentacji
- **Zgodność ze specyfikacją**: Zapewniono, że wszystkie obowiązkowe wymagania bezpieczeństwa MCP (MUST/MUST NOT) są zgodne z najnowszą specyfikacją
- **Aktualność zasobów**: Sprawdzono wszystkie zewnętrzne linki do dokumentacji Microsoft, standardów bezpieczeństwa i przewodników wdrożeniowych
- **Pokrycie najlepszych praktyk**: Potwierdzono kompleksowe pokrycie uwierzytelniania, autoryzacji, zagrożeń specyficznych dla AI, bezpieczeństwa łańcucha dostaw oraz wzorców korporacyjnych

## 6 października 2025

### Rozszerzenie sekcji Pierwsze kroki – Zaawansowane użycie serwera i prosta autoryzacja

#### Zaawansowane użycie serwera (03-GettingStarted/10-advanced)
- **Dodany nowy rozdział**: Wprowadzono kompleksowy przewodnik po zaawansowanym użyciu serwera MCP, obejmujący zarówno zwykłe, jak i niskopoziomowe architektury serwera.
  - **Zwykły kontra niskopoziomowy serwer**: Szczegółowe porównanie i przykłady kodu w Python i TypeScript dla obu podejść.
  - **Projekt oparty na handlerach**: Wyjaśnienie zarządzania narzędziami/zasobami/promptami opartego na handlerach dla skalowalnych i elastycznych implementacji serwera.
  - **Praktyczne wzorce**: Scenariusze z rzeczywistego świata, gdzie wzorce serwera niskopoziomowego są korzystne dla zaawansowanych funkcji i architektury.

#### Prosta autoryzacja (03-GettingStarted/11-simple-auth)
- **Dodany nowy rozdział**: Przewodnik krok po kroku dotyczący implementacji prostej autoryzacji w serwerach MCP.
  - **Koncepcje autoryzacji**: Jasne wyjaśnienie różnicy między uwierzytelnianiem a autoryzacją oraz zarządzanie poświadczeniami.
  - **Podstawowa implementacja autoryzacji**: Wzorce uwierzytelniania oparte na middleware w Python (Starlette) i TypeScript (Express), z przykładami kodu.
  - **Postęp do zaawansowanego bezpieczeństwa**: Wskazówki dotyczące rozpoczęcia od prostej autoryzacji i rozwoju do OAuth 2.1 i RBAC, z odniesieniami do zaawansowanych modułów bezpieczeństwa.

Te dodatki zapewniają praktyczne, interaktywne wskazówki do budowania bardziej solidnych, bezpiecznych i elastycznych implementacji serwerów MCP, łącząc podstawowe koncepcje z zaawansowanymi wzorcami produkcyjnymi.

## 29 września 2025

### Laboratoria integracji bazy danych MCP Server – Kompleksowa ścieżka nauki praktycznej

#### 11-MCPServerHandsOnLabs - Nowy kompletny program ćwiczeń integracji bazy danych
- **Kompletna ścieżka nauki 13 laboratoriów**: Dodano kompleksowy praktyczny program nauczania tworzenia produkcyjnych serwerów MCP z integracją bazy PostgreSQL
  - **Realny przypadek użycia**: Przykład analizy Zava Retail demonstrujący wzorce klasy enterprise
  - **Strukturalna progresja nauki**:
    - **Laboratoria 00-03: Fundamenty** – Wprowadzenie, Architektura rdzeniowa, Bezpieczeństwo i multi-tenantowość, Konfiguracja środowiska
    - **Laboratoria 04-06: Budowa serwera MCP** – Projektowanie bazy danych i schematu, Implementacja serwera MCP, Tworzenie narzędzi  
    - **Laboratoria 07-09: Funkcje zaawansowane** – Integracja wyszukiwania semantycznego, Testowanie i debugowanie, Integracja z VS Code
    - **Laboratoria 10-12: Produkcja i najlepsze praktyki** – Strategie wdrożenia, Monitoring i obserwowalność, Najlepsze praktyki i optymalizacja
  - **Technologie klasy enterprise**: Framework FastMCP, PostgreSQL z pgvector, osadzenia Azure OpenAI, Azure Container Apps, Application Insights
  - **Funkcje zaawansowane**: Bezpieczeństwo na poziomie wiersza (RLS), wyszukiwanie semantyczne, wielonajemcowy dostęp do danych, osadzenia wektorowe, monitorowanie w czasie rzeczywistym

#### Standaryzacja terminologii – konwersja modułów na laboratoria
- **Kompleksowa aktualizacja dokumentacji**: Systematyczna aktualizacja wszystkich plików README w 11-MCPServerHandsOnLabs w celu używania terminologii "laboratorium" zamiast "moduł"
  - **Nagłówki sekcji**: Aktualizacja "Co obejmuje ten moduł" na "Co obejmuje to laboratorium" we wszystkich 13 laboratoriach
  - **Opis zawartości**: Zmiana "Ten moduł zapewnia..." na "To laboratorium zapewnia..." we wszystkich dokumentach
  - **Cele nauki**: Aktualizacja "Na koniec tego modułu..." na "Na koniec tego laboratorium..." 
  - **Linki nawigacyjne**: Konwersja wszystkich odniesień "Moduł XX:" na "Laboratorium XX:" w przekrojach i nawigacji
  - **Śledzenie ukończenia**: Zaktualizowano "Po ukończeniu tego modułu..." na "Po ukończeniu tego laboratorium..."
  - **Zachowano odniesienia techniczne**: Zachowano odniesienia modułów Python w plikach konfiguracyjnych (np. `"module": "mcp_server.main"`)

#### Ulepszenie przewodnika nauki (study_guide.md)
- **Wizualna mapa programu nauczania**: Dodano nową sekcję "11. Laboratoria integracji bazy danych" z kompleksową wizualizacją struktury laboratoriów
- **Struktura repozytorium**: Zaktualizowano z dziesięciu do jedenastu głównych sekcji z szczegółowym opisem 11-MCPServerHandsOnLabs
- **Wskazówki dotyczące ścieżki nauki**: Ulepszone instrukcje nawigacji obejmujące sekcje 00-11
- **Pokrycie technologii**: Dodano detale integracji FastMCP, PostgreSQL i usług Azure
- **Wyniki nauki**: Podkreślono rozwój produkcyjnych serwerów, wzorce integracji baz danych oraz bezpieczeństwo korporacyjne

#### Ulepszenie struktury głównego README
- **Terminologia oparta na laboratoriach**: Zaktualizowano główny README.md w 11-MCPServerHandsOnLabs do konsekwentnego używania struktury "laboratorium"
- **Organizacja ścieżki nauki**: Jasna progresja od podstawowych koncepcji przez zaawansowaną implementację do wdrożenia produkcyjnego
- **Fokus na realne zastosowania**: Nacisk na praktyczną, interaktywną naukę z wzorcami i technologiami klasy enterprise

### Poprawki jakości i spójności dokumentacji
- **Nacisk na naukę praktyczną**: Wzmocniono podejście oparte na laboratoriach w całej dokumentacji
- **Fokus na wzorce korporacyjne**: Podkreślono produkcyjne implementacje i aspekty bezpieczeństwa korporacyjnego
- **Integracja technologii**: Kompleksowe pokrycie nowoczesnych usług Azure i wzorców integracji AI
- **Progresja nauki**: Jasna, strukturalna ścieżka od podstaw do wdrożenia produkcyjnego

## 26 września 2025

### Rozszerzenie studiów przypadków – Integracja z rejestrem MCP GitHub

#### Studia przypadków (09-CaseStudy/) - Fokus na rozwój ekosystemu
- **README.md**: Duże rozszerzenie o kompleksowe studium przypadku rejestru MCP GitHub
  - **Studium przypadku rejestru MCP GitHub**: Nowe kompleksowe studium analityczne dotyczące uruchomienia rejestru MCP przez GitHub we wrześniu 2025
    - **Analiza problemu**: Szczegółowa analiza fragmentacji odkrywania i wdrażania serwerów MCP
    - **Architektura rozwiązania**: Podejście rejestru scentralizowanego GitHub z instalacją VS Code jednym kliknięciem
    - **Wpływ biznesowy**: Mierzalna poprawa onboardingu i produktywności deweloperów
    - **Wartość strategiczna**: Fokus na modułowe wdrażanie agentów i interoperacyjność między narzędziami
    - **Rozwój ekosystemu**: Pozycjonowanie jako platforma podstawowa dla integracji agentowej
  - **Ulepszona struktura studium przypadku**: Zaktualizowano wszystkie siedem studiów przypadków z jednolitym formatowaniem i kompleksowymi opisami
    - Azure AI Travel Agents: Nacisk na orkiestrację multi-agenta
    - Integracja Azure DevOps: Fokus na automatyzację przepływów pracy
    - Pobieranie dokumentacji w czasie rzeczywistym: Implementacja klienta konsolowego Python
    - Interaktywny generator planu nauki: Konwersacyjna aplikacja webowa Chainlit
    - Dokumentacja w edytorze: Integracja VS Code i GitHub Copilot
    - Azure API Management: Wzorce integracji API klasy enterprise
    - Rejestr MCP GitHub: Rozwój ekosystemu i platforma społecznościowa
  - **Kompleksowe zakończenie**: Przepisany rozdział końcowy podkreślający siedem studiów przypadków obejmujących wiele wymiarów implementacji MCP
    - Integracja korporacyjna, orkiestracja multi-agenta, produktywność deweloperów
    - Rozwój ekosystemu, kategoryzacja zastosowań edukacyjnych
    - Ulepszone wglądy w wzorce architektoniczne, strategie wdrożeniowe i najlepsze praktyki
    - Nacisk na MCP jako dojrzały, gotowy do produkcji protokół

#### Aktualizacje przewodnika nauki (study_guide.md)
- **Wizualna mapa programu nauczania**: Zaktualizowano mapę mentalną o rejestr MCP GitHub w sekcji studiów przypadków
- **Opis studiów przypadków**: Rozbudowano z opisów ogólnych do szczegółowego podziału siedmiu kompleksowych studiów przypadków
- **Struktura repozytorium**: Zaktualizowano sekcję 10 zgodnie z kompleksowym pokryciem studiów przypadków i specyficznymi szczegółami implementacji
- **Integracja changeloga**: Dodano wpis z 26 września 2025 dokumentujący dodanie rejestru MCP GitHub oraz ulepszenia studiów przypadków
- **Aktualizacja daty**: Zmieniono datę stopki na najnowszą rewizję (26 września 2025)

### Poprawki jakości dokumentacji
- **Wzmocnienie spójności**: Ustandaryzowano formatowanie i strukturę studiów przypadków we wszystkich siedmiu przykładach
- **Kompleksowe pokrycie**: Studia przypadków obejmują teraz scenariusze korporacyjne, produktywność deweloperów i rozwój ekosystemu
- **Pozycjonowanie strategiczne**: Zwiększony nacisk na MCP jako platformę bazową do wdrożeń systemów agentowych
- **Integracja zasobów**: Zaktualizowano dodatkowe zasoby o link do rejestru MCP GitHub

## 15 września 2025

### Rozszerzenie tematów zaawansowanych – Własne transporty i inżynieria kontekstu

#### Własne transporty MCP (05-AdvancedTopics/mcp-transport/) - Nowy przewodnik zaawansowanej implementacji
- **README.md**: Kompletny przewodnik implementacji własnych mechanizmów transportu MCP
  - **Transport Azure Event Grid**: Kompleksowa implementacja transportu zdarzeniowego serverless
    - Przykłady w C#, TypeScript i Python z integracją Azure Functions
    - Wzorce architektury zdarzeniowo-sterowanej dla skalowalnych rozwiązań MCP
    - Odbieranie webhooków i obsługa wiadomości typu push
  - **Transport Azure Event Hubs**: Implementacja transportu strumieniowego o wysokiej przepustowości
    - Możliwości streamingu w czasie rzeczywistym dla scenariuszy o niskiej latencji
    - Strategie partycjonowania i zarządzanie checkpointami
    - Grupowanie wiadomości i optymalizacja wydajności
  - **Wzorce integracji korporacyjnej**: Przykłady architektury gotowej do produkcji
    - Rozproszone przetwarzanie MCP za pomocą wielu Azure Functions
    - Hybrydowe architektury transportowe łączące różne typy transportów
    - Strategie trwałości wiadomości, niezawodności i obsługi błędów
  - **Bezpieczeństwo i monitoring**: Integracja Azure Key Vault oraz wzorce obserwowalności
    - Uwierzytelnianie za pomocą zarządzanej tożsamości i dostęp z najmniejszymi uprawnieniami
    - Telemetria Application Insights i monitorowanie wydajności
    - Obwody zabezpieczające i wzorce odporności na błędy
  - **Frameworki testowe**: Kompleksowe strategie testowania własnych transportów
    - Testy jednostkowe z użyciem test double i frameworków do mockowania
    - Testy integracyjne z Azure Test Containers
    - Uwagi dotyczące testów wydajności i obciążeniowych

#### Inżynieria kontekstu (05-AdvancedTopics/mcp-contextengineering/) - Nowa dziedzina AI
- **README.md**: Kompleksowe omówienie inżynierii kontekstu jako rozwijającej się dziedziny
  - **Podstawowe zasady**: Kompleksowe udostępnianie kontekstu, świadomość podejmowania decyzji dotyczących akcji oraz zarządzanie oknem kontekstowym

  - **Dopasowanie protokołu MCP**: Jak projekt MCP rozwiązuje wyzwania inżynierii kontekstu
    - Ograniczenia okna kontekstowego i strategie ładowania progresywnego
    - Określanie trafności i dynamiczne pobieranie kontekstu
    - Obsługa kontekstu multimodalnego i kwestie bezpieczeństwa
  - **Podejścia do implementacji**: Architektury jednoprocesowe vs. wieloagentowe
    - Techniki dzielenia i priorytetyzacji kontekstu
    - Strategie progresywnego ładowania i kompresji kontekstu
    - Warstwowe podejścia do kontekstu i optymalizacja pobierania
  - **Ramka pomiarowa**: Wschodzące metryki oceny skuteczności kontekstu
    - Wydajność wejścia, wydajność, jakość i aspekty doświadczenia użytkownika
    - Eksperymentalne podejścia do optymalizacji kontekstu
    - Analiza błędów i metodologie poprawy

#### Aktualizacje nawigacji w programie nauczania (README.md)
- **Ulepszona struktura modułów**: Zaktualizowano tabelę programu nauczania o nowe zaawansowane tematy
  - Dodano wpisy Inżynieria Kontekstu (5.14) i Niestandardowy Transport (5.15)
  - Spójne formatowanie i linki nawigacyjne we wszystkich modułach
  - Zaktualizowano opisy, aby odzwierciedlały aktualny zakres treści

### Ulepszenia struktury katalogów
- **Standaryzacja nazewnictwa**: Zmieniono nazwę "mcp transport" na "mcp-transport" dla spójności z innymi folderami zaawansowanych tematów
- **Organizacja treści**: Wszystkie foldery 05-AdvancedTopics teraz mają spójny wzorzec nazewnictwa (mcp-[temat])

### Poprawa jakości dokumentacji
- **Dopasowanie specyfikacji MCP**: Wszystkie nowe treści odwołują się do aktualnej Specyfikacji MCP z 2025-06-18
- **Przykłady wielojęzyczne**: Kompleksowe przykłady kodu w C#, TypeScript i Python
- **Skupienie korporacyjne**: Wzorce gotowe do produkcji i integracja z chmurą Azure we wszystkich materiałach
- **Wizualna dokumentacja**: Diagramy Mermaid do wizualizacji architektury i przepływów

## 18 sierpnia 2025

### Kompleksowa aktualizacja dokumentacji - standardy MCP 2025-06-18

#### Najlepsze praktyki bezpieczeństwa MCP (02-Security/) - Całkowita modernizacja
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Całkowite przepisanie dostosowane do Specyfikacji MCP 2025-06-18
  - **Wymagania obowiązkowe**: Dodano wyraźne wymagania MUSI/NIE MUSI z oficjalnej specyfikacji z czytelnymi wskaźnikami wizualnymi
  - **12 kluczowych praktyk bezpieczeństwa**: Przekształcone z listy 15 pozycji na kompleksowe domeny bezpieczeństwa
    - Bezpieczeństwo tokenów i uwierzytelnianie z integracją z zewnętrznym dostawcą tożsamości
    - Zarządzanie sesjami i bezpieczeństwo transportu z wymogami kryptograficznymi
    - Ochrona przed zagrożeniami specyficznymi dla AI z integracją Microsoft Prompt Shields
    - Kontrola dostępu i uprawnienia według zasady najmniejszych uprawnień
    - Bezpieczeństwo treści i monitorowanie z integracją Azure Content Safety
    - Bezpieczeństwo łańcucha dostaw z kompleksową weryfikacją komponentów
    - Bezpieczeństwo OAuth i zapobieganie atakom confused deputy z implementacją PKCE
    - Reagowanie na incydenty i odzyskiwanie z automatycznymi możliwościami
    - Zgodność i nadzór z dostosowaniem do regulacji
    - Zaawansowane kontrole bezpieczeństwa z architekturą zero trust
    - Integracja ekosystemu bezpieczeństwa Microsoft z kompleksowymi rozwiązaniami
    - Ciągła ewolucja bezpieczeństwa z adaptacyjnymi praktykami
  - **Rozwiązania bezpieczeństwa Microsoft**: Ulepszone wskazówki dotyczące integracji Prompt Shields, Azure Content Safety, Entra ID i GitHub Advanced Security
  - **Zasoby wdrożeniowe**: Skategoryzowane kompleksowe linki do zasobów według Oficjalnej dokumentacji MCP, rozwiązań bezpieczeństwa Microsoft, standardów oraz przewodników wdrożeniowych

#### Zaawansowane kontrole bezpieczeństwa (02-Security/) - Wdrożenie korporacyjne
- **MCP-SECURITY-CONTROLS-2025.md**: Kompletny przegląd ram bezpieczeństwa klasy enterprise
  - **9 kompleksowych domen bezpieczeństwa**: Rozszerzone z podstawowych kontroli do szczegółowego korporacyjnego frameworku
    - Zaawansowane uwierzytelnianie i autoryzacja z integracją Microsoft Entra ID
    - Bezpieczeństwo tokenów i kontrola anti-passthrough z kompleksową walidacją
    - Kontrole bezpieczeństwa sesji z zapobieganiem przejęciom
    - Specyficzne dla AI kontrole bezpieczeństwa z zapobieganiem wstrzyknięciom promptów i zatruwaniu narzędzi
    - Zapobieganie atakom confused deputy w scenariuszach proxy MCP z ochroną OAuth
    - Bezpieczeństwo wykonania narzędzi z użyciem sandboxingu i izolacji
    - Kontrole bezpieczeństwa łańcucha dostaw z weryfikacją zależności
    - Kontrole monitoringu i wykrywania z integracją SIEM
    - Reagowanie na incydenty i odzyskiwanie z automatycznymi możliwościami
  - **Przykłady wdrożeniowe**: Dodano szczegółowe bloki konfiguracji YAML i przykłady kodu
  - **Integracja rozwiązań Microsoft**: Kompleksowe omówienie usług bezpieczeństwa Azure, GitHub Advanced Security oraz korporacyjnego zarządzania tożsamością

#### Zaawansowane tematy dotyczące bezpieczeństwa (05-AdvancedTopics/mcp-security/) - Wdrożenie gotowe do produkcji
- **README.md**: Całkowite przepisanie pod korporacyjne wdrożenie bezpieczeństwa
  - **Dopasowanie do aktualnej specyfikacji**: Zaktualizowano do Specyfikacji MCP 2025-06-18 z obowiązkowymi wymaganiami bezpieczeństwa
  - **Ulepszone uwierzytelnianie**: Integracja Microsoft Entra ID z zaawansowanymi przykładami w .NET i Java Spring Security
  - **Integracja zabezpieczeń AI**: Implementacja Microsoft Prompt Shields i Azure Content Safety ze szczegółowymi przykładami w Pythonie
  - **Zaawansowana łagodzenie zagrożeń**: Kompleksowe przykłady implementacji dla
    - Zapobieganie atakom confused deputy z PKCE i walidacją zgody użytkownika
    - Zapobieganie passthrough tokenów z walidacją odbiorcy i bezpiecznym zarządzaniem tokenami
    - Zapobieganie przejęciom sesji z wiązaniem kryptograficznym i analizą zachowań
  - **Integracja zabezpieczeń korporacyjnych**: Monitorowanie Azure Application Insights, potoki wykrywania zagrożeń oraz bezpieczeństwo łańcucha dostaw
  - **Lista kontrolna wdrożenia**: Jasne rozróżnienie między obowiązkowymi a zalecanymi kontrolami bezpieczeństwa z korzyściami ekosystemu Microsoft

### Jakość dokumentacji i zgodność ze standardami
- **Odniesienia do specyfikacji**: Zaktualizowano wszystkie referencje do aktualnej Specyfikacji MCP 2025-06-18
- **Ekosystem bezpieczeństwa Microsoft**: Ulepszone wskazówki dotyczące integracji we wszystkich dokumentach dotyczących bezpieczeństwa
- **Praktyczna implementacja**: Dodano szczegółowe przykłady kodu w .NET, Java i Python oraz wzorce korporacyjne
- **Organizacja zasobów**: Kompleksowa kategoryzacja oficjalnej dokumentacji, standardów bezpieczeństwa i przewodników wdrożeniowych
- **Wskaźniki wizualne**: Wyraźne oznaczenie wymagań obowiązkowych i praktyk zalecanych


#### Podstawowe koncepcje (01-CoreConcepts/) - Kompletny remont
- **Aktualizacja wersji protokołu**: Zaktualizowano odniesienia do aktualnej Specyfikacji MCP 2025-06-18 z wersjonowaniem datowym (format RRRR-MM-DD)
- **Udoskonalenie architektury**: Ulepszone opisy hostów, klientów i serwerów odzwierciedlające aktualne wzorce architektury MCP
  - Hosty jasno zdefiniowane jako aplikacje AI koordynujące wiele połączeń klientów MCP
  - Klienci opisani jako łączniki protokołu utrzymujące relacje jeden do jednego z serwerami
  - Serwery rozszerzone o scenariusze wdrożeń lokalnych i zdalnych
- **Restrukturyzacja prymitywów**: Kompletny przegląd prymitywów serwera i klienta
  - Prymitywy serwera: zasoby (źródła danych), prompty (szablony), narzędzia (funkcje wykonywalne) z detalicznymi wyjaśnieniami i przykładami
  - Prymitywy klienta: próbkowanie (uzyskiwanie wyników LLM), wywołanie (wejście użytkownika), logowanie (debugowanie/monitoring)
  - Zaktualizowane wzorce metod odkrywania (`*/list`), pobierania (`*/get`) i wykonania (`*/call`)
- **Architektura protokołu**: Wprowadzono model architektury dwuwarstwowej
  - Warstwa danych: podstawa JSON-RPC 2.0 z zarządzaniem cyklem życia i prymitywami
  - Warstwa transportowa: STDIO (lokalny) i HTTP strumieniowy z SSE (transport zdalny)
- **Ramka bezpieczeństwa**: Kompletne zasady bezpieczeństwa, w tym wyraźna zgoda użytkownika, ochrona prywatności danych, bezpieczeństwo wykonania narzędzi i zabezpieczenia warstwy transportowej
- **Wzorce komunikacji**: Zaktualizowano wiadomości protokołu pokazujące inicjalizację, odkrywanie, wykonanie i przepływy powiadomień
- **Przykłady kodu**: Odświeżone przykłady wielojęzyczne (.NET, Java, Python, JavaScript) odzwierciedlające aktualne wzorce SDK MCP

#### Bezpieczeństwo (02-Security/) - Kompleksowa przebudowa bezpieczeństwa  
- **Zgodność ze standardami**: Pełna zgodność z wymaganiami bezpieczeństwa Specyfikacji MCP 2025-06-18
- **Ewolucja uwierzytelniania**: Udokumentowana ewolucja od niestandardowych serwerów OAuth do delegacji z zewnętrznym dostawcą tożsamości (Microsoft Entra ID)
- **Analiza zagrożeń specyficznych dla AI**: Ulepszony zakres nowoczesnych wektorów ataków AI
  - Szczegółowe scenariusze ataków wstrzyknięcia promptów z przykładami z rzeczywistego świata
  - Mechanizmy zatruwania narzędzi i schematy ataków „rug pull”
  - Zatruwanie okna kontekstu i ataki polegające na dezorientacji modelu
- **Rozwiązania bezpieczeństwa Microsoft AI**: Kompleksowe omówienie ekosystemu bezpieczeństwa Microsoft
  - AI Prompt Shields z zaawansowanym wykrywaniem, podświetlaniem i technikami delimiterów
  - Wzorce integracji Azure Content Safety
  - GitHub Advanced Security do ochrony łańcucha dostaw
- **Zaawansowane łagodzenie zagrożeń**: Szczegółowe kontrole bezpieczeństwa dla
  - Przejęcia sesji z uwzględnieniem scenariuszy ataków specyficznych dla MCP i wymagań kryptograficznych ID sesji
  - Problemy confused deputy w scenariuszach proxy MCP z wyraźnymi wymaganiami zgody
  - Luki passthrough tokenów z obowiązkowymi kontrolami walidacji
- **Bezpieczeństwo łańcucha dostaw**: Rozszerzony zakres łańcucha dostaw AI obejmujący modele bazowe, usługi osadzeń, dostawców kontekstu i API firm trzecich
- **Bezpieczeństwo fundamentów**: Ulepszona integracja z korporacyjnymi wzorcami bezpieczeństwa, w tym architekturą zero trust i ekosystemem bezpieczeństwa Microsoft
- **Organizacja zasobów**: Skategoryzowane obszerne linki do zasobów według typu (Oficjalna dokumentacja, Standardy, Badania, Rozwiązania Microsoft, Przewodniki wdrożeniowe)

### Poprawa jakości dokumentacji
- **Strukturalne cele nauki**: Ulepszone cele nauki z konkretnymi rezultatami do osiągnięcia
- **Przekierowania krzyżowe**: Dodano linki między powiązanymi tematami bezpieczeństwa i podstawowych koncepcji
- **Aktualne informacje**: Zaktualizowano wszystkie daty i linki specyfikacji do aktualnych standardów
- **Wskazówki wdrożeniowe**: Dodano konkretne, praktyczne wytyczne wdrożeniowe w obu sekcjach

## 16 lipca 2025

### Ulepszenia README i nawigacji
- Całkowicie przeprojektowano nawigację programu nauczania w README.md
- Zastąpiono tagi `<details>` bardziej dostępnym formatem opartym na tabeli
- Utworzono alternatywne opcje układu w nowym folderze "alternative_layouts"
- Dodano przykłady nawigacji w stylu kart, zakładek i akordeonu
- Zaktualizowano sekcję struktury repozytorium, aby uwzględnić najnowsze pliki
- Ulepszono sekcję „Jak korzystać z tego programu nauczania” jasnymi zaleceniami
- Zaktualizowano linki do specyfikacji MCP, aby wskazywały poprawne URL-e
- Dodano sekcję Inżynierii Kontekstu (5.14) do struktury programu nauczania

### Aktualizacje przewodnika do nauki
- Całkowicie przeprojektowano przewodnik do nauki, aby był zgodny z aktualną strukturą repozytorium
- Dodano nowe sekcje dla klientów MCP i narzędzi oraz popularnych serwerów MCP
- Zaktualizowano wizualną mapę programu nauczania, aby dokładnie odzwierciedlała wszystkie tematy
- Ulepszono opisy zaawansowanych tematów, aby objąć wszystkie obszary specjalistyczne
- Zaktualizowano sekcję studiów przypadków, aby odzwierciedlała rzeczywiste przykłady
- Dodano ten obszerny changelog

### Wkłady społeczności (06-CommunityContributions/)
- Dodano szczegółowe informacje o serwerach MCP do generowania obrazów
- Dodano obszerną sekcję dotyczącą używania Claude w VSCode
- Dodano instrukcje instalacji i użytkowania terminalowego klienta Cline
- Zaktualizowano sekcję klienta MCP, aby uwzględnić wszystkie popularne opcje klientów
- Ulepszono przykłady wkładów o dokładniejsze próbki kodu

### Zaawansowane tematy (05-AdvancedTopics/)
- Zorganizowano wszystkie foldery ze specjalistycznymi tematami z użyciem spójnego nazewnictwa
- Dodano materiały i przykłady dotyczące inżynierii kontekstu
- Dodano dokumentację integracji agenta Foundry
- Ulepszono dokumentację integracji zabezpieczeń Entra ID

## 11 czerwca 2025

### Utworzenie początkowe
- Wydano pierwszą wersję programu nauczania MCP dla początkujących
- Utworzono podstawową strukturę dla wszystkich 10 głównych sekcji
- Wdrożono wizualną mapę programu nauczania do nawigacji
- Dodano początkowe projekty przykładowe w wielu językach programowania

### Pierwsze kroki (03-GettingStarted/)
- Utworzono pierwsze przykłady implementacji serwera
- Dodano wskazówki dotyczące tworzenia klientów
- Uwzględniono instrukcje integracji klienta LLM
- Dodano dokumentację integracji z VS Code
- Wdrożono przykłady serwera Server-Sent Events (SSE)

### Podstawowe koncepcje (01-CoreConcepts/)
- Dodano szczegółowe wyjaśnienie architektury klient-serwer
- Utworzono dokumentację kluczowych komponentów protokołu
- Udokumentowano wzorce wiadomości w MCP

## 23 maja 2025

### Struktura repozytorium
- Zainicjowano repozytorium z podstawową strukturą folderów
- Utworzono pliki README dla każdego głównego działu
- Skonfigurowano infrastrukturę tłumaczeń
- Dodano zasoby obrazów i diagramy

### Dokumentacja
- Utworzono początkowy README.md z przeglądem programu nauczania
- Dodano pliki CODE_OF_CONDUCT.md i SECURITY.md
- Skonfigurowano SUPPORT.md z wytycznymi dotyczącymi uzyskiwania pomocy
- Utworzono wstępną strukturę przewodnika do nauki

## 15 kwietnia 2025

### Planowanie i ramy
- Wstępne planowanie programu nauczania MCP dla początkujących
- Zdefiniowano cele nauki i docelową grupę odbiorców
- Nakreślono strukturę programu w 10 sekcjach
- Opracowano ramy koncepcyjne dla przykładów i studiów przypadku
- Utworzono wstępne prototypowe przykłady kluczowych koncepcji

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->