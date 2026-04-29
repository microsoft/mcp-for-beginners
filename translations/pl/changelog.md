# Dziennik zmian: MCP dla kursu dla początkujących

Ten dokument służy jako rejestr wszystkich istotnych zmian wprowadzonych w programie nauczania Model Context Protocol (MCP) dla początkujących. Zmiany są dokumentowane w kolejności od najnowszych do najstarszych.

## 11 kwietnia 2026

### Nowa lekcja, poprawki dokumentacji i aktualizacje zależności

#### Dodano nową zawartość programu nauczania

**Moduł 05 - Tematy zaawansowane**
- **Lekcja 5.17: Adversarial Multi-Agent Reasoning z MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nowy kompleksowy przewodnik obejmujący wzorzec debaty adversarialnej dla systemów wieloagentowych
  - Diagram architektury Mermaid: dwóch agentów → współdzielony serwer MCP → zapis debaty → sędzia → werdykt
  - Wspólny serwer narzędzi MCP (`web_search` + `run_python`) zaimplementowany w Pythonie i TypeScript
  - Przeciwdziałające sobie systemowe podpowiedzi (ZA / PRZECIW / Sędzia) z wyraźnymi wymaganiami dotyczącymi użycia narzędzi
  - Koordynator debaty w Python, TypeScript i C#, zarządzający rundami i trasowaniem argumentów
  - Okablowanie MCP `ClientSession` dla koordynatora do wywołań prawdziwych narzędzi
  - Tabela przypadków użycia (wykrywanie halucynacji, modelowanie zagrożeń, przegląd projektowania API, weryfikacja faktów, wybór technologii)
  - Aspekty bezpieczeństwa: odizolowane wykonanie, walidacja wywołań narzędzi, limitowanie częstości, logowanie audytu
  - Strukturyzowane ćwiczenie z trzema praktycznymi scenariuszami (przegląd kodu, decyzja architektoniczna, moderacja treści)

#### Poprawki dokumentacji

**Moduł 03 - Pierwsze kroki**
- **05-stdio-server/README.md**: Naprawiono niepełny przykład serwera stdio w TypeScript — dodano brakującą instancję transportu (`new StdioServerTransport()`) oraz wywołanie `server.connect(transport)`, aby pasowało do przykładów w Python i .NET w tym samym rozdziale
- **14-sampling/README.md**: Poprawiono literówkę — poprawiono `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Aktualizacje programu nauczania

**Główny README.md**
- Dodano wpis 5.17 (Adversarial Multi-Agent Reasoning z MCP) do tabeli programów z bezpośrednim linkiem do nowej lekcji

**05-AdvancedTopics/README.md**
- Dodano wiersz Lekcji 5.17 do tabeli lekcji

**study_guide.md**
- Dodano temat Adversarial Multi-Agent Reasoning do mapy myśli i opisu tekstowego Tematów zaawansowanych

#### Poprawki kodu i bezpieczeństwa

**Moduł 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Poprawka bezpieczeństwa — wstrzykiwanie poleceń**: Zastąpiono interpolację powłoki `execSync` za pomocą `execFile` + `promisify` w narzędziu `run_python` napisanym w TypeScript, eliminując możliwość wstrzyknięcia poleceń (kod kontrolowany przez LLM jest teraz przekazywany jako literalny element argv bez udziału powłoki)
- **Okablowanie pętli narzędzi MCP**: Zaktualizowano koordynatora debaty w Python, aby używał klienta `AsyncAnthropic` (zamiast blokującego, synchronicznego `Anthropic`), przekazywał aktywną `ClientSession` bezpośrednio do każdej tury agenta, pobierał definicje narzędzi przez `session.list_tools()` w każdej turze oraz wysyłał bloki `tool_use` przez `session.call_tool()` w pętli aż model zwróci ostateczną odpowiedź tekstową

#### Aktualizacje zależności

- Podniesiono wersję `hono` do 4.12.12 w wielu pakietach (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Podniesiono wersję `@hono/node-server` z 1.19.11 do 1.19.13 w pakietach TypeScript
- Podniesiono wersję `cryptography` z 46.0.5 do 46.0.7 w pakietach Python (10-StreamliningAIWorkflows laboratoria 3 i 4)
- Podniesiono wersję `lodash` z 4.17.23 do 4.18.1 w inspektorze 10-StreamliningAIWorkflows

#### Tłumaczenia

- Zsynchronizowano tłumaczenia na ponad 48 języków z najnowszymi zmianami źródła (aktualizacja i18n)

---

## 5 lutego 2026

### Walidacja całego repozytorium i usprawnienia nawigacji

#### Dodano nową zawartość programu nauczania

**Moduł 03 - Pierwsze kroki**
- **12-mcp-hosts/README.md**: Nowy kompleksowy przewodnik uruchamiania hostów MCP
  - Przykłady konfiguracji dla Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Szablony konfiguracji JSON dla wszystkich głównych hostów
  - Tabela porównawcza typów transportu (stdio, SSE/HTTP, WebSocket)
  - Rozwiązywanie najczęstszych problemów z połączeniem
  - Najlepsze praktyki bezpieczeństwa konfiguracji hostów

- **13-mcp-inspector/README.md**: Nowy przewodnik debugowania MCP Inspector
  - Metody instalacji (npx, globalny npm, ze źródła)
  - Łączenie z serwerami przez stdio i HTTP/SSE
  - Narzędzia testujące, zasoby i przepływy poleceń
  - Integracja z VS Code dla MCP Inspector
  - Typowe scenariusze debugowania z rozwiązaniami

**Moduł 04 - Wdrożenie praktyczne**
- **pagination/README.md**: Nowy przewodnik implementacji paginacji
  - Wzorce paginacji oparte na kursorach w Python, TypeScript, Java
  - Obsługa paginacji po stronie klienta
  - Strategie projektowania kursorów (nieprzejrzyste vs. strukturalne)
  - Zalecenia optymalizacji wydajności

**Moduł 05 - Tematy zaawansowane**
- **mcp-protocol-features/README.md**: Nowy dogłębny opis funkcji protokołu
  - Implementacja powiadomień o postępie
  - Wzorce anulowania zapytań
  - Szablony zasobów z wzorcami URI
  - Zarządzanie cyklem życia serwera
  - Kontrola poziomu logowania
  - Wzorce obsługi błędów z kodami JSON-RPC

#### Poprawki nawigacji (zaktualizowano 24+ plików)

**Główne README modułów**  
 Obecnie linkują do pierwszej lekcji ORAZ kolejnego modułu

**Podpliki 02-Security**  
 Wszystkie 5 dodatkowych dokumentów bezpieczeństwa mają nawigację "Co dalej"

**Pliki 09-CaseStudy**  
 Wszystkie pliki studiów przypadków mają teraz sekwencyjną nawigację

**Laboratoria 10-StreamliningAI**  
 Dodano sekcję Co dalej do przeglądu Modułu 10 i Modułu 11

#### Poprawki kodu i zawartości

**Aktualizacje SDK i zależności**  
 Naprawiono pustą wersję openai na `^4.95.0`  
 Zaktualizowano SDK z `^1.8.0` do `>=1.26.0`  
 Zaktualizowano piny wersji mcp do `>=1.26.0`

**Poprawki kodu**  
 Naprawiono nieprawidłowy model `gpt-4o-mini` na `gpt-4.1-mini`

**Poprawki zawartości**  
 Naprawiono uszkodzony link `READMEmd` → `README.md`, poprawiono nagłówek w programie `Module 1-3` → `Module 0-3`, poprawiono ścieżkę uwzględniającą wielkość liter  
 Usunięto uszkodzoną zduplikowaną zawartość Case Study 5

**Ulepszenia dla początkujących**  
 Dodano właściwe wprowadzenie, cele nauki i wymagania wstępne dla początkujących

#### Aktualizacje programu nauczania

**Główny README.md**  
- Dodano wpisy 3.12 (Hosty MCP), 3.13 (MCP Inspector), 4.1 (Paginacja), 5.16 (Funkcje protokołu) do tabeli programu

**README modułów**  
 Dodano lekcje 12 i 13 do listy lekcji  
 Dodano sekcję Przewodniki praktyczne z linkiem do paginacji  
 Dodano lekcje 5.15 (Custom Transport) i 5.16 (Funkcje protokołu)

**study_guide.md**  
- Zaktualizowano mapę myśli o wszystkie nowe tematy: konfiguracja hostów MCP, MCP Inspector, strategie paginacji, dogłębne funkcje protokołu

## 28 stycznia 2026

### Przegląd zgodności ze specyfikacją MCP 2025-11-25

#### Ulepszenia kluczowych koncepcji (01-CoreConcepts/)
- **Nowa prymitywa klienta - Roots**: Dodano obszerną dokumentację prymitywy klienta Roots, umożliwiającej serwerom rozumienie granic systemu plików oraz uprawnień dostępu
- **Adnotacje narzędzi**: Dodano dokumentację adnotacji zachowań narzędzi (`readOnlyHint`, `destructiveHint`) dla lepszych decyzji wykonawczych narzędzi
- **Wywoływanie narzędzi w próbkowaniu**: Zaktualizowano dokumentację Sampling o parametry `tools` i `toolChoice` dla modelowego wywoływania narzędzi podczas próbkowania
- **Elicytacja w trybie URL**: Dodano dokumentację wywoływania inicjowanego z serwera przez zewnętrzne interakcje WWW oparte na URL
- **Zadania (eksperymentalne)**: Dodano nową sekcję dokumentującą eksperymentalną funkcję Zadania dla trwałych opakowań wykonawczych i odroczonego pobierania wyników
- **Wsparcie ikon**: Zauważono, że teraz narzędzia, zasoby, szablony zasobów i podpowiedzi mogą zawierać ikony jako dodatkowe metadane

#### Aktualizacje dokumentacji
- **README.md**: Dodano odniesienie do wersji MCP Specification 2025-11-25 oraz wyjaśnienie wersjonowania opartego na dacie
- **study_guide.md**: Zaktualizowano mapę programu o Zadania i Adnotacje narzędzi w sekcji Kluczowe koncepcje; zaktualizowano znacznik czasowy dokumentu

#### Weryfikacja zgodności specyfikacji
- **Wersja protokołu**: Zweryfikowano, że cała dokumentacja odnosi się do aktualnej MCP Specification 2025-11-25
- **Zgodność architektury**: Potwierdzono poprawność dokumentacji dwuwarstwowej architektury (warstwa danych + warstwa transportu)
- **Dokumentacja prymitywów**: Potwierdzono opis prymitywów serwera (Zasoby, Podpowiedzi, Narzędzia) oraz klienta (Sampling, Elicytacja, Logowanie, Roots)
- **Mechanizmy transportu**: Zweryfikowano poprawność dokumentacji transportu STDIO i strumieniowego HTTP
- **Wytyczne bezpieczeństwa**: Potwierdzono zgodność z aktualnymi najlepszymi praktykami bezpieczeństwa MCP

#### Kluczowe funkcje MCP 2025-11-25 udokumentowane
- **OpenID Connect Discovery**: Odkrywanie serwera uwierzytelniania przez OIDC
- **Dokumenty metadanych OAuth Client ID**: Zalecany mechanizm rejestracji klientów
- **JSON Schema 2020-12**: Domyślny dialekt definicji schematów MCP
- **System poziomów SDK**: Formalne wymagania dla wsparcia i utrzymania funkcji SDK
- **Struktura zarządzania**: Formalizacja grup roboczych i grup zainteresowań w zarządzaniu MCP

### Główna aktualizacja dokumentacji bezpieczeństwa (02-Security/)

#### Integracja warsztatów MCP Security Summit (Sherpa)
- **Nowe zasoby szkoleniowe praktyczne**: Dodano kompletną integrację z [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) w całej dokumentacji bezpieczeństwa
- **Trasa wyprawy**: Udokumentowano pełny przebieg od Bazy do Szczytu
- **Zgodność z OWASP**: Wszystkie wytyczne bezpieczeństwa mapują się teraz do ryzyk OWASP MCP Azure Security Guide

#### Integracja OWASP MCP Top 10
- **Nowa sekcja**: Dodano tabelę ryzyk OWASP MCP Top 10 z ochronami Azure do głównego README bezpieczeństwa
- **Dokumentacja oparta na ryzyku**: Zaktualizowano mcp-security-controls-2025.md o odniesienia do ryzyk OWASP MCP dla wszystkich domen bezpieczeństwa
- **Architektura referencyjna**: Połączono z OWASP MCP Azure Security Guide i wzorcami implementacji

#### Zaktualizowane pliki bezpieczeństwa
- **README.md**: Dodano przegląd warsztatów Sherpa, tabelę trasy wyprawy, podsumowanie ryzyk OWASP MCP Top 10 oraz sekcję praktycznego szkolenia
- **mcp-security-controls-2025.md**: Zaktualizowano nagłówek na luty 2026, dodano odniesienia do ryzyk OWASP (MCP01-MCP08), naprawiono niespójność wersji specyfikacji
- **mcp-security-best-practices-2025.md**: Dodano sekcję zasobów Sherpa i OWASP, zaktualizowano znacznik czasowy
- **mcp-best-practices.md**: Dodano sekcję treningu praktycznego z linkami do Sherpa i OWASP
- **azure-content-safety-implementation.md**: Dodano odniesienie OWASP MCP06, dopasowanie do obozu 3 Sherpa oraz dodatkową sekcję zasobów

#### Dodano nowe linki do zasobów
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Strony poszczególnych ryzyk OWASP MCP (MCP01-MCP10)

### Zgodność całego programu nauczania ze specyfikacją MCP 2025-11-25

#### Moduł 03 - Pierwsze kroki
- **Dokumentacja SDK**: Dodano Go SDK do oficjalnej listy SDK; zaktualizowano wszystkie odniesienia SDK do zgodności ze specyfikacją MCP 2025-11-25
- **Wyjaśnienie transportu**: Zaktualizowano opisy transportów STDIO i HTTP Streaming z wyraźnymi odniesieniami do specyfikacji

#### Moduł 04 - Wdrożenie praktyczne
- **Aktualizacje SDK**: Dodano Go SDK; zaktualizowano listę SDK z odniesieniem do wersji specyfikacji
- **Specyfikacja autoryzacji**: Zaktualizowano link do specyfikacji MCP Authorization na aktualną wersję 2025-11-25

#### Moduł 05 - Tematy zaawansowane
- **Nowe funkcje**: Dodano notkę o nowych funkcjach MCP Specification 2025-11-25 (Zadania, Adnotacje narzędzi, Elicytacja w trybie URL, Roots)
- **Zasoby bezpieczeństwa**: Dodano linki do OWASP MCP Top 10 i warsztatów Sherpa w dodatkowych odniesieniach

#### Moduł 06 - Wkład społeczności
- **Lista SDK**: Dodano SDK Swift i Rust; zaktualizowano link do specyfikacji na 2025-11-25
- **Odniesienie do specyfikacji**: Zaktualizowano link specyfikacji MCP na bezpośredni URL specyfikacji

#### Moduł 07 - Lekcje z wczesnej adopcji
- **Aktualizacje zasobów**: Dodano link MCP Specification 2025-11-25 i OWASP MCP Top 10 do dodatkowych zasobów

#### Moduł 08 - Najlepsze praktyki
- **Wersja specyfikacji**: Zaktualizowano odniesienie do MCP Specification 2025-11-25
- **Zasoby bezpieczeństwa**: Dodano OWASP MCP Top 10 i warsztaty Sherpa do dodatkowych odniesień

#### Moduł 10 - Usprawnianie przepływów pracy AI
- **Aktualizacja odznaki**: Zmieniono odznakę wersji MCP z wersji SDK (1.9.3) na wersję specyfikacji (2025-11-25)
- **Linki do zasobów**: Zaktualizowano link do MCP Specification; dodano OWASP MCP Top 10

#### Moduł 11 - Laboratoria praktyczne serwera MCP
- **Odniesienie do specyfikacji**: Zaktualizowano link MCP Specification do wersji 2025-11-25
- **Zasoby bezpieczeństwa**: Dodano OWASP MCP Top 10 do oficjalnych zasobów

## 18 grudnia 2025
### Aktualizacja Dokumentacji Bezpieczeństwa - Specyfikacja MCP 2025-11-25

#### Najlepsze praktyki bezpieczeństwa MCP (02-Security/mcp-best-practices.md) - Aktualizacja wersji specyfikacji
- **Aktualizacja wersji protokołu**: Zaktualizowano odniesienia do najnowszej Specyfikacji MCP 2025-11-25 (wydanej 25 listopada 2025)
  - Zmieniono wszystkie odniesienia wersji specyfikacji z 2025-06-18 na 2025-11-25
  - Zaktualizowano daty dokumentu z 18 sierpnia 2025 na 18 grudnia 2025
  - Zweryfikowano, że wszystkie linki specyfikacji wskazują na aktualną dokumentację
- **Weryfikacja treści**: Kompleksowa walidacja najlepszych praktyk bezpieczeństwa zgodnie z najnowszymi standardami
  - **Rozwiązania Microsoft Security**: Zweryfikowano aktualne terminy i linki do Prompt Shields (wcześniej „Wykrywanie ryzyka jailbreak”), Azure Content Safety, Microsoft Entra ID oraz Azure Key Vault
  - **Bezpieczeństwo OAuth 2.1**: Potwierdzono zgodność z najnowszymi najlepszymi praktykami bezpieczeństwa OAuth
  - **Standardy OWASP**: Sprawdzono aktualność odniesień OWASP Top 10 dla LLM-ów
  - **Usługi Azure**: Zweryfikowano wszystkie linki do dokumentacji Microsoft Azure i najlepsze praktyki
- **Zgodność ze standardami**: Wszystkie odniesione standardy bezpieczeństwa potwierdzone jako aktualne
  - Ramy zarządzania ryzykiem AI NIST
  - ISO 27001:2022
  - Najlepsze praktyki bezpieczeństwa OAuth 2.1
  - Ramy bezpieczeństwa i zgodności Azure
- **Zasoby wdrożeniowe**: Zweryfikowano wszystkie linki do przewodników wdrożenia i zasobów
  - Wzorce uwierzytelniania Azure API Management
  - Przewodniki integracji Microsoft Entra ID
  - Zarządzanie sekretami Azure Key Vault
  - Pipeline’y DevSecOps i rozwiązania monitorujące

### Zapewnienie jakości dokumentacji
- **Zgodność ze specyfikacją**: Upewniono się, że wszystkie obowiązkowe wymagania bezpieczeństwa MCP (MUST/MUST NOT) są zgodne z najnowszą specyfikacją
- **Aktualność zasobów**: Zweryfikowano wszystkie zewnętrzne linki do dokumentacji Microsoft, standardów bezpieczeństwa i przewodników wdrożeniowych
- **Zakres najlepszych praktyk**: Potwierdzono pełne pokrycie uwierzytelniania, autoryzacji, zagrożeń specyficznych AI, bezpieczeństwa łańcucha dostaw oraz wzorców korporacyjnych

## 6 października 2025

### Rozszerzenie sekcji Wprowadzenie – Zaawansowane użycie serwera i prosta autentykacja

#### Zaawansowane użycie serwera (03-GettingStarted/10-advanced)
- **Nowy rozdział dodany**: Wprowadzono obszerny przewodnik po zaawansowanym użyciu serwera MCP, obejmujący zarówno architekturę serwera standardowego, jak i niskopoziomowego
  - **Serwer standardowy vs. niskopoziomowy**: Szczegółowe porównanie i przykłady kodu w Pythonie i TypeScript dla obu podejść
  - **Projekt oparty na handlerach**: Wyjaśnienie zarządzania narzędziami/zasobami/promptami oparte na handlerach dla skalowalnych i elastycznych implementacji serwera
  - **Praktyczne wzorce**: Realne scenariusze, w których wzorce niskopoziomowego serwera są korzystne dla zaawansowanych funkcji i architektury

#### Prosta autentykacja (03-GettingStarted/11-simple-auth)
- **Nowy rozdział dodany**: Przewodnik krok po kroku wdrażania prostej autentykacji w serwerach MCP
  - **Koncepcje uwierzytelniania**: Jasne wyjaśnienie różnicy między uwierzytelnianiem a autoryzacją oraz zarządzania poświadczeniami
  - **Implementacja Basic Auth**: Wzorce uwierzytelniania oparte na middleware w Pythonie (Starlette) i TypeScript (Express) wraz z przykładami kodu
  - **Przejście do zaawansowanego bezpieczeństwa**: Wskazówki dotyczące rozpoczęcia od prostej autentykacji i dalszego przechodzenia do OAuth 2.1 oraz RBAC, z odniesieniami do modułów zaawansowanego bezpieczeństwa

Te dodatki dostarczają praktyczne wskazówki do budowania bardziej niezawodnych, bezpiecznych i elastycznych implementacji serwerów MCP, łącząc podstawowe koncepcje z zaawansowanymi wzorcami produkcyjnymi.

## 29 września 2025

### Laboratoria integracji bazy danych w serwerze MCP – kompleksowa ścieżka nauki praktycznej

#### 11-MCPServerHandsOnLabs – nowy kompletny kurs integracji baz danych
- **Kompletny 13-laboratoryjny kurs**: Dodano kompleksowy, praktyczny kurs budowania produkcyjnych serwerów MCP z integracją bazy PostgreSQL
  - **Implementacja w świecie rzeczywistym**: Przypadek użycia analityki Zava Retail demonstrujący wzorce klasy korporacyjnej
  - **Strukturalna progresja nauki**:
    - **Laboratoria 00-03: Podstawy** – Wprowadzenie, architektura podstawowa, bezpieczeństwo i multi-tenancy, konfiguracja środowiska
    - **Laboratoria 04-06: Budowa serwera MCP** – Projektowanie bazy danych i schematu, implementacja serwera MCP, rozwój narzędzi  
    - **Laboratoria 07-09: Funkcje zaawansowane** – Integracja wyszukiwania semantycznego, testowanie i debugowanie, integracja z VS Code
    - **Laboratoria 10-12: Produkcja i najlepsze praktyki** – Strategie wdrożenia, monitorowanie i obserwowalność, najlepsze praktyki i optymalizacja
  - **Technologie korporacyjne**: Framework FastMCP, PostgreSQL z pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Funkcje zaawansowane**: RLS (Row Level Security), wyszukiwanie semantyczne, dostęp do danych multi-tenant, osadzenia wektorowe, monitorowanie w czasie rzeczywistym

#### Standaryzacja terminologii – konwersja modułu na laboratorium
- **Kompleksowa aktualizacja dokumentacji**: Systematyczna zmiana wszystkich plików README w 11-MCPServerHandsOnLabs na terminologię „Laboratorium” zamiast „Moduł”
  - **Nagłówki sekcji**: Zmieniono „Co ten moduł obejmuje” na „Co to laboratorium obejmuje” we wszystkich 13 laboratoriach
  - **Opis treści**: Zmieniono „Ten moduł dostarcza...” na „To laboratorium dostarcza...” w całej dokumentacji
  - **Cele nauki**: Aktualizacja „Pod koniec tego modułu...” na „Pod koniec tego laboratorium...”
  - **Linki nawigacyjne**: Konwersja wszystkich odniesień „Moduł XX:” na „Laboratorium XX:” w odnośnikach i nawigacji
  - **Śledzenie ukończenia**: Aktualizacja „Po ukończeniu tego modułu...” na „Po ukończeniu tego laboratorium...”
  - **Zachowanie odniesień technicznych**: Zachowano odniesienia do modułów Pythona w plikach konfiguracyjnych (np. `"module": "mcp_server.main"`)

#### Ulepszenie przewodnika nauki (study_guide.md)
- **Wizualna mapa programu nauczania**: Dodano nową sekcję „11. Laboratoria integracji baz danych” z obszerną wizualizacją struktury laboratorium
- **Struktura repozytorium**: Zaktualizowano z dziesięciu do jedenaście głównych sekcji wraz z opisem 11-MCPServerHandsOnLabs
- **Wskazówki dotyczące ścieżki nauki**: Ulepszono instrukcje nawigacji obejmujące sekcje 00-11
- **Zasięg technologii**: Dodano szczegóły dotyczące integracji FastMCP, PostgreSQL i usług Azure
- **Wyniki nauki**: Podkreślono rozwój produkcyjnych serwerów, wzorce integracji baz danych i bezpieczeństwo korporacyjne

#### Ulepszenie struktury głównego README
- **Terminologia oparta na laboratoriach**: Zaktualizowano główny README.md w 11-MCPServerHandsOnLabs do spójnego użycia struktury „Laboratorium”
- **Organizacja ścieżki nauki**: Jasna progresja od podstaw do zaawansowanej implementacji i wdrożenia produkcyjnego
- **Skupienie na praktyce**: Nacisk na praktyczne, manualne uczenie z wzorcami i technologiami klasy korporacyjnej

### Poprawa jakości i spójności dokumentacji
- **Nacisk na praktyczną naukę**: Wzmocnione podejście oparte na laboratoriach w całej dokumentacji
- **Fokus na wzorce korporacyjne**: Podkreślono produkcyjne implementacje i aspekty bezpieczeństwa klasy enterprise
- **Integracja technologii**: Kompleksowe omówienie nowoczesnych usług Azure i wzorców integracji AI
- **Progresja nauki**: Jasna, strukturalna ścieżka od podstaw po wdrożenie produkcyjne

## 26 września 2025

### Ulepszenie studiów przypadków – integracja rejestru MCP GitHub

#### Studia przypadków (09-CaseStudy/) – Fokus na rozwój ekosystemu
- **README.md**: Znaczące rozszerzenie o kompleksowe studium przypadku rejestru MCP GitHub
  - **Studium przypadku rejestru MCP GitHub**: Nowe obszerne studium analizujące uruchomienie rejestru MCP GitHub we wrześniu 2025
    - **Analiza problemu**: Szczegółowa analiza fragmentacji wykrywania i wdrażania serwerów MCP
    - **Architektura rozwiązania**: Centralne podejście rejestru GitHub z instalacją VS Code jednym kliknięciem
    - **Wpływ biznesowy**: Mierzalne usprawnienia w onboarding deweloperów i produktywności
    - **Wartość strategiczna**: Skupienie na modułowym wdrażaniu agentów oraz interoperacyjności narzędzi
    - **Rozwój ekosystemu**: Pozycjonowanie jako platforma bazowa do integracji agentów
  - **Ulepszona struktura studiów przypadków**: Zaktualizowano wszystkie siedem studiów z konsekwentnym formatowaniem i opisami
    - Azure AI Travel Agents: Nacisk na orkiestrację wieloagentową
    - Integracja Azure DevOps: Fokus na automatyzację workflow
    - Pobieranie dokumentacji w czasie rzeczywistym: Implementacja klienta konsoli Python
    - Generator planu nauki interaktywnej: Aplikacja łańcuchowa Chainlit
    - Dokumentacja w edytorze: Integracje VS Code i GitHub Copilot
    - Azure API Management: Wzorce integracji API klasy enterprise
    - GitHub MCP Registry: Rozwój ekosystemu i platforma społecznościowa
  - **Kompleksowe zakończenie**: Przepisany rozdział podsumowujący siedem studiów przypadków obejmujących różne wymiary implementacji MCP
    - Integracja enterprise, orkiestracja multi-agentowa, produktywność developerów
    - Rozwój ekosystemu, aplikacje edukacyjne
    - Pogłębione spostrzeżenia dotyczące wzorców architektonicznych, strategii implementacji i najlepszych praktyk
    - Podkreślenie MCP jako dojrzałego, produkcyjnego protokołu

#### Aktualizacje przewodnika nauki (study_guide.md)
- **Wizualna mapa programu**: Zaktualizowano mindmapę o rejestr MCP GitHub w sekcji studiów przypadków
- **Opis studiów przypadków**: Rozszerzono opis z ogólnych na szczegółowy podział siedmiu kompleksowych studiów
- **Struktura repozytorium**: Zaktualizowano sekcję 10 odpowiadającą szczegółowemu pokryciu studiów przypadków i implementacji
- **Integracja changelogu**: Dodano wpis z 26 września 2025 dokumentujący dodanie rejestru MCP GitHub i ulepszenia studiów przypadków
- **Aktualizacja daty**: Zmieniono datę stopki na najnowszą rewizję (26 września 2025)

### Ulepszenia jakości dokumentacji
- **Poprawa spójności**: Ujednolicono formatowanie i strukturę studiów przypadków we wszystkich siedmiu przykładach
- **Kompleksowe pokrycie**: Studia przypadków obejmują scenariusze enterprise, produktywności deweloperów i rozwoju ekosystemu
- **Pozycjonowanie strategiczne**: Wzmocniony fokus na MCP jako platformę bazową do wdrażania agentów
- **Integracja zasobów**: Zaktualizowano dodatkowe zasoby o link do rejestru MCP GitHub

## 15 września 2025

### Rozszerzenie tematów zaawansowanych – dedykowane transporty i inżynieria kontekstu

#### Dedykowane transporty MCP (05-AdvancedTopics/mcp-transport/) – nowy przewodnik zaawansowanej implementacji
- **README.md**: Kompletny przewodnik implementacji niestandardowych mechanizmów transportu MCP
  - **Transport Azure Event Grid**: Kompleksowa implementacja serwerless transportu zdarzeniowego
    - Przykłady w C#, TypeScript i Python z integracją Azure Functions
    - Wzorce architektury zdarzeniowej dla skalowalnych rozwiązań MCP
    - Odbiorniki webhooków i obsługa wiadomości push
  - **Transport Azure Event Hubs**: Implementacja transportu strumieniowego o wysokiej przepustowości
    - Możliwości strumieniowania w czasie rzeczywistym dla scenariuszy o niskich opóźnieniach
    - Strategie partycjonowania i zarządzanie checkpointami
    - Grupowanie wiadomości i optymalizacja wydajności
  - **Wzorce integracji korporacyjnej**: Przykłady architektury produkcyjnej
    - Rozproszony przetwarzanie MCP na wielu Azure Functions
    - Hybrydowe architektury transportu łączące różne typy
    - Trwałość wiadomości, niezawodność i strategie obsługi błędów
  - **Bezpieczeństwo i monitoring**: Integracja Azure Key Vault i wzorce obserwowalności
    - Uwierzytelnianie Managed Identity i dostęp na zasadzie najmniejszych uprawnień
    - Telemetria Application Insights i monitorowanie wydajności
    - Obwody ochronne i wzorce odporności na błędy
  - **Frameworki testowe**: Kompleksowe strategie testowania niestandardowych transportów
    - Testy jednostkowe z podwójnikami i frameworkami do mockowania
    - Testy integracyjne z Azure Test Containers
    - Rozważania dotyczące testów wydajności i obciążeniowych

#### Inżynieria kontekstu (05-AdvancedTopics/mcp-contextengineering/) – rozwijająca się dziedzina AI
- **README.md**: Kompleksowe omówienie inżynierii kontekstu jako rosnącej dyscypliny
  - **Podstawowe zasady**: Kompletny sharing kontekstu, świadomość działań decyzyjnych i zarządzanie oknem kontekstu
  - **Zgodność z protokołem MCP**: Jak projekt MCP odpowiada na wyzwania inżynierii kontekstu
    - Ograniczenia okna kontekstu i strategie progresywnego ładowania
    - Określanie relewancji i dynamiczne pobieranie kontekstu
    - Obsługa kontekstu multimodalnego oraz kwestie bezpieczeństwa
  - **Podejścia implementacyjne**: Architektury jedno- i wieloagentowe
    - Segmentacja i priorytetyzacja kontekstu
    - Progresywne ładowanie i strategie kompresji kontekstu
    - Warstwowe podejścia do kontekstu i optymalizacja pobierania
  - **Ramy pomiarowe**: Nowe metryki oceny efektywności kontekstu
    - Wydajność wejścia, działanie, jakość i doświadczenie użytkownika
    - Eksperymentalne metody optymalizacji kontekstu
    - Analiza awarii i metody ulepszania

#### Aktualizacje nawigacji po kursie (README.md)
- **Ulepszona struktura modułów**: Zaktualizowano tabelę kursu o nowe tematy zaawansowane
  - Dodano wpisy Inżynieria kontekstu (5.14) i Dedykowany transport (5.15)
  - Spójne formatowanie i linki nawigacyjne we wszystkich modułach
  - Zaktualizowane opisy odzwierciedlające obecny zakres treści

### Ulepszenia struktury katalogów
- **Standaryzacja nazewnictwa**: Zmieniono nazwę „mcp transport” na „mcp-transport” dla spójności z innymi folderami tematów zaawansowanych
- **Organizacja zawartości**: Wszystkie foldery 05-AdvancedTopics stosują teraz spójny wzorzec nazewnictwa (mcp-[temat])

### Ulepszenia jakości dokumentacji
- **Zgodność z specyfikacją MCP**: Cała nowa zawartość odnosi się do aktualnej Specyfikacji MCP 2025-06-18
- **Przykłady wielojęzyczne**: Kompleksowe przykłady kodu w C#, TypeScript i Python
- **Fokus korporacyjny**: Wzorce produkcyjne i integracja z chmurą Azure na całym obszarze
- **Dokumentacja wizualna**: Diagramy Mermaid do wizualizacji architektury i przepływów

## 18 sierpnia 2025

### Kompleksowa aktualizacja dokumentacji – standardy MCP 2025-06-18

#### Najlepsze praktyki bezpieczeństwa MCP (02-Security/) – pełna modernizacja
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Kompletny przepis zgodny ze Specyfikacją MCP 2025-06-18  
  - **Wymagania Obowiązkowe**: Dodano wyraźne wymagania MUSI/NIE MUSI z oficjalnej specyfikacji z jasnymi wskaźnikami wizualnymi  
  - **12 Kluczowych Praktyk Bezpieczeństwa**: Przekształcone z listy 15-punktowej na kompleksowe domeny bezpieczeństwa  
    - Bezpieczeństwo Tokenów i Uwierzytelnianie z integracją z zewnętrznym dostawcą tożsamości  
    - Zarządzanie Sesjami i Bezpieczeństwo Transportu z wymaganiami kryptograficznymi  
    - Ochrona Przed Zagrożeniami Specyficznymi dla AI z integracją Microsoft Prompt Shields  
    - Kontrola Dostępu i Uprawnienia z zasadą najmniejszego uprzywilejowania  
    - Bezpieczeństwo Zawartości i Monitorowanie z integracją Azure Content Safety  
    - Bezpieczeństwo Łańcucha Dostaw z kompleksową weryfikacją komponentów  
    - Bezpieczeństwo OAuth i Zapobieganie Atakom Confused Deputy z implementacją PKCE  
    - Reakcja na Incydenty i Odzyskiwanie z możliwościami automatyzacji  
    - Zgodność i Zarządzanie z dostosowaniem do regulacji  
    - Zaawansowane Kontrole Bezpieczeństwa z architekturą zero trust  
    - Integracja z Ekosystemem Bezpieczeństwa Microsoft z kompleksowymi rozwiązaniami  
    - Ciągła Ewolucja Bezpieczeństwa z praktykami adaptacyjnymi  
  - **Rozwiązania Bezpieczeństwa Microsoft**: Ulepszone wytyczne integracyjne dla Prompt Shields, Azure Content Safety, Entra ID i GitHub Advanced Security  
  - **Zasoby Implementacyjne**: Sklasyfikowane kompleksowe linki do zasobów według Oficjalnej Dokumentacji MCP, Rozwiązań Bezpieczeństwa Microsoft, Standardów Bezpieczeństwa oraz Przewodników Implementacyjnych  

#### Zaawansowane Kontrole Bezpieczeństwa (02-Security/) - Implementacja Enterprise  
- **MCP-SECURITY-CONTROLS-2025.md**: Kompletny przegląd frameworka bezpieczeństwa klasy enterprise  
  - **9 Kompleksowych Domen Bezpieczeństwa**: Rozszerzone z podstawowych kontroli do szczegółowego frameworka enterprise  
    - Zaawansowane Uwierzytelnianie i Autoryzacja z integracją Microsoft Entra ID  
    - Bezpieczeństwo Tokenów i Kontrole Anti-Passthrough z kompleksową walidacją  
    - Kontrole Bezpieczeństwa Sesji z zapobieganiem przejęciom  
    - Kontrole Bezpieczeństwa Specyficzne dla AI z zapobieganiem wstrzyknięciom promptów i zatruciu narzędzi  
    - Zapobieganie Atakom Confused Deputy z bezpieczeństwem proxy OAuth  
    - Bezpieczeństwo Wykonywania Narzędzi z piaskownicą i izolacją  
    - Kontrole Bezpieczeństwa Łańcucha Dostaw z weryfikacją zależności  
    - Kontrole Monitorowania i Wykrywania z integracją SIEM  
    - Reakcja na Incydenty i Odzyskiwanie z automatycznymi funkcjami  
  - **Przykłady Implementacji**: Dodane szczegółowe bloki konfiguracyjne YAML i przykłady kodu  
  - **Integracja Rozwiązań Microsoft**: Kompleksowe omówienie usług bezpieczeństwa Azure, GitHub Advanced Security i zarządzania tożsamością enterprise  

#### Zaawansowane Tematy Bezpieczeństwa (05-AdvancedTopics/mcp-security/) - Gotowa do Produkcji Implementacja  
- **README.md**: Kompletny przepis dla implementacji bezpieczeństwa enterprise  
  - **Zgodność ze Specyfikacją**: Zaktualizowane do MCP Specification 2025-06-18 z obowiązkowymi wymaganiami bezpieczeństwa  
  - **Wzmocnione Uwierzytelnianie**: Integracja Microsoft Entra ID z pełnymi przykładami w .NET i Java Spring Security  
  - **Integracja Bezpieczeństwa AI**: Implementacja Microsoft Prompt Shields i Azure Content Safety z szczegółowymi przykładami w Python  
  - **Zaawansowane Łagodzenie Zagrożeń**: Kompleksowe przykłady implementacji dla  
    - Zapobiegania Atakom Confused Deputy z PKCE i walidacją zgody użytkownika  
    - Zapobiegania Token Passthrough z walidacją odbiorcy i bezpiecznym zarządzaniem tokenami  
    - Zapobiegania Przejęciu Sesji z powiązaniem kryptograficznym i analizą zachowań  
  - **Integracja Bezpieczeństwa Enterprise**: Monitorowanie Azure Application Insights, potoki wykrywania zagrożeń i bezpieczeństwo łańcucha dostaw  
  - **Lista Kontrolna Implementacji**: Jasne rozróżnienie wymagań obowiązkowych i zalecanych kontroli bezpieczeństwa z korzyściami ekosystemu Microsoft  

### Jakość Dokumentacji i Zgodność ze Standardami  
- **Odniesienia do Specyfikacji**: Zaktualizowano wszystkie odniesienia do aktualnej Specyfikacji MCP 2025-06-18  
- **Ekosystem Bezpieczeństwa Microsoft**: Ulepszona integracja w całej dokumentacji bezpieczeństwa  
- **Praktyczna Implementacja**: Dodano szczegółowe przykłady kodu w .NET, Java i Python z wzorcami enterprise  
- **Organizacja Zasobów**: Kompleksowa kategoryzacja oficjalnej dokumentacji, standardów bezpieczeństwa i przewodników implementacyjnych  
- **Wskaźniki Wizualne**: Wyraźne oznaczenia wymagań obowiązkowych versus praktyk zalecanych  

#### Podstawowe Koncepcje (01-CoreConcepts/) - Kompletny Modernizacja  
- **Aktualizacja Wersji Protokółu**: Zaktualizowano do aktualnej Specyfikacji MCP 2025-06-18 z wersjonowaniem opartym na dacie (format RRRR-MM-DD)  
- **Udoskonalenie Architektury**: Ulepszone opisy Hostów, Klientów i Serwerów odzwierciedlające aktualne wzorce architektoniczne MCP  
  - Hosty jasno zdefiniowane jako aplikacje AI koordynujące wiele połączeń klientów MCP  
  - Klienci opisani jako konektory protokółu utrzymujące relacje jeden-do-jednego z serwerami  
  - Serwery rozszerzone o scenariusze wdrożeń lokalnych i zdalnych  
- **Restrukturyzacja Prymitywów**: Kompletny przegląd prymitywów serwerowych i klienckich  
  - Prymitywy Serwera: Zasoby (źródła danych), Prompt'y (szablony), Narzędzia (funkcje wykonywalne) ze szczegółowymi objaśnieniami i przykładami  
  - Prymitywy Klienta: Próbkowanie (uzupełnienia LLM), Elicytacja (wejście użytkownika), Logowanie (debugowanie/monitoring)  
  - Zaktualizowane do aktualnych wzorców metod odkrywania (`*/list`), pobierania (`*/get`) i wykonywania (`*/call`)  
- **Architektura Protokółu**: Wprowadzono model dwuwarstwowy  
  - Warstwa Danych: Fundament JSON-RPC 2.0 z zarządzaniem cyklem życia i prymitywami  
  - Warstwa Transportu: STDIO (lokalny) i strumieniowy HTTP z SSE (zdalny) mechanizmy transportowe  
- **Framework Bezpieczeństwa**: Kompleksowe zasady bezpieczeństwa obejmujące wyraźną zgodę użytkownika, ochronę prywatności danych, bezpieczeństwo wykonywania narzędzi i zabezpieczenia warstwy transportowej  
- **Wzorce Komunikacji**: Zaktualizowane komunikaty protokołu pokazujące inicjalizację, odkrywanie, wykonanie i powiadomienia  
- **Przykłady Kodów**: Odświeżone wielojęzyczne przykłady (.NET, Java, Python, JavaScript) odzwierciedlające aktualne wzorce SDK MCP  

#### Bezpieczeństwo (02-Security/) - Kompleksowy Przegląd  
- **Zgodność ze Standardami**: Pełna zgodność z wymaganiami bezpieczeństwa Specyfikacji MCP 2025-06-18  
- **Ewolucja Uwierzytelniania**: Udokumentowana ewolucja od własnych serwerów OAuth do delegacji do zewnętrznych dostawców tożsamości (Microsoft Entra ID)  
- **Analiza Zagrożeń Specyficznych dla AI**: Ulepszony opis nowoczesnych wektorów ataków na AI  
  - Szczegółowe scenariusze ataków typu prompt injection z przykładami z życia  
  - Mechanizmy zatrucia narzędzi i wzorce ataków „rug pull”  
  - Zatrucie kontekstu i ataki na dezorientację modelu  
- **Rozwiązania Bezpieczeństwa AI Microsoft**: Kompleksowy przegląd ekosystemu bezpieczeństwa Microsoft  
  - AI Prompt Shields z zaawansowanym wykrywaniem, wyróżnianiem i technikami rozdzielaczy  
  - Wzorce integracji Azure Content Safety  
  - GitHub Advanced Security dla ochrony łańcucha dostaw  
- **Zaawansowane Łagodzenie Zagrożeń**: Szczegółowe kontrole bezpieczeństwa dla  
  - Przejęć sesji z przykładami ataków specyficznych dla MCP i wymaganiami kryptograficznymi dla identyfikatorów sesji  
  - Problemów Confused Deputy w scenariuszach proxy MCP z wyraźnymi wymaganiami zgody  
  - Luka Token Passthrough z obowiązkowymi kontrolami walidacji  
- **Bezpieczeństwo Łańcucha Dostaw**: Rozszerzone omówienie łańcucha dostaw AI, w tym modeli bazowych, usług embeddings, dostawców kontekstu i API firm trzecich  
- **Podstawy Bezpieczeństwa**: Ulepszona integracja z wzorcami bezpieczeństwa enterprise, w tym architekturą zero trust i ekosystemem bezpieczeństwa Microsoft  
- **Organizacja Zasobów**: Sklasyfikowane kompleksowe linki do zasobów według typu (Oficjalna Dokumentacja, Standardy, Badania, Rozwiązania Microsoft, Przewodniki Implementacyjne)  

### Ulepszenia Jakości Dokumentacji  
- **Strukturyzowane Cele Nauczania**: Ulepszone cele nauczania z konkretnymi, wykonalnymi rezultatami  
- **Odnośniki Krzyżowe**: Dodano linki między powiązanymi tematami bezpieczeństwa i podstawowych koncepcji  
- **Aktualne Informacje**: Zaktualizowano wszystkie odniesienia do dat i linków do specyfikacji zgodnie z aktualnymi standardami  
- **Wytyczne Implementacyjne**: Dodano konkretne, wykonalne wytyczne implementacyjne w obu sekcjach  

## 16 lipca 2025  

### Ulepszenia README i Nawigacji  
- Całkowicie przeprojektowano nawigację programu nauczania w README.md  
- Zastąpiono tagi `<details>` bardziej dostępnym formatem opartym na tabelach  
- Stworzono alternatywne opcje układu w nowym folderze "alternative_layouts"  
- Dodano przykłady nawigacji w stylu kart, zakładek i akordeonu  
- Zaktualizowano sekcję struktury repozytorium o wszystkie najnowsze pliki  
- Ulepszono sekcję "Jak korzystać z tego programu nauczania" z jasnymi rekomendacjami  
- Zaktualizowano linki do specyfikacji MCP, aby wskazywały poprawne URL-e  
- Dodano sekcję Inżynierii Kontekstowej (5.14) do struktury programu  

### Aktualizacje Przewodnika Nauki  
- Całkowicie zrewidowano przewodnik nauki, aby dostosować go do aktualnej struktury repozytorium  
- Dodano nowe sekcje dotyczące Klientów i Narzędzi MCP oraz Popularnych Serwerów MCP  
- Zaktualizowano Wizualną Mapę Programu, aby dokładnie odzwierciedlała wszystkie tematy  
- Ulepszono opisy Zaawansowanych Tematów, aby objąć wszystkie obszary specjalistyczne  
- Zaktualizowano sekcję Studium Przypadków zgodnie z rzeczywistymi przykładami  
- Dodano ten kompleksowy changelog  

### Wkład Społeczności (06-CommunityContributions/)  
- Dodano szczegółowe informacje o serwerach MCP do generowania obrazów  
- Dodano obszerną sekcję dotyczącą używania Claude w VSCode  
- Dodano instrukcje konfiguracji i użytkowania terminala Cline  
- Zaktualizowano sekcję klientów MCP, aby uwzględnić wszystkie popularne opcje  
- Ulepszono przykłady wkładu z bardziej precyzyjnymi przykładami kodu  

### Zaawansowane Tematy (05-AdvancedTopics/)  
- Zorganizowano wszystkie specjalistyczne foldery tematów z konsekwentnym nazewnictwem  
- Dodano materiały i przykłady inżynierii kontekstu  
- Dodano dokumentację integracji agenta Foundry  
- Ulepszono dokumentację integracji bezpieczeństwa Entra ID  

## 11 czerwca 2025  

### Utworzenie Początkowe  
- Wydano pierwszą wersję programu nauczania MCP dla początkujących  
- Stworzono podstawową strukturę dla wszystkich 10 głównych sekcji  
- Wdrożono Wizualną Mapę Programu do nawigacji  
- Dodano początkowe projekty przykładowe w różnych językach programowania  

### Rozpoczęcie Pracy (03-GettingStarted/)  
- Utworzono pierwsze przykłady implementacji serwerów  
- Dodano wytyczne do rozwoju klientów  
- Uwzględniono instrukcje integracji klientów LLM  
- Dodano dokumentację integracji z VS Code  
- Wdrożono przykłady serwerów Server-Sent Events (SSE)  

### Podstawowe Koncepcje (01-CoreConcepts/)  
- Dodano szczegółowe wyjaśnienie architektury klient-serwer  
- Stworzono dokumentację kluczowych komponentów protokołu  
- Udokumentowano wzorce komunikatów w MCP  

## 23 maja 2025  

### Struktura Repozytorium  
- Zainicjowano repozytorium z podstawową strukturą folderów  
- Utworzono pliki README dla każdej głównej sekcji  
- Skonfigurowano infrastrukturę do tłumaczeń  
- Dodano zasoby graficzne i diagramy  

### Dokumentacja  
- Utworzono wstępny README.md z przeglądem programu nauczania  
- Dodano pliki CODE_OF_CONDUCT.md i SECURITY.md  
- Skonfigurowano SUPPORT.md z wytycznymi dotyczącymi uzyskania pomocy  
- Utworzono wstępną strukturę przewodnika nauki  

## 15 kwietnia 2025  

### Planowanie i Podstawa  
- Wstępne planowanie programu nauczania MCP dla początkujących  
- Zdefiniowano cele nauczania i grupę docelową  
- Nakreślono 10-sekcyjną strukturę programu  
- Opracowano koncepcyjne ramy dla przykładów i studiów przypadków  
- Stworzono wstępne prototypowe przykłady kluczowych koncepcji  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uważany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie wykonane przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikłe z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->