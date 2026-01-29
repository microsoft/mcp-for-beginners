# Dziennik zmian: Program nauczania MCP dla początkujących

Ten dokument służy jako zapis wszystkich istotnych zmian wprowadzonych w programie nauczania Model Context Protocol (MCP) dla początkujących. Zmiany są dokumentowane w kolejności odwrotnej chronologicznie (najnowsze zmiany na początku).

## 18 grudnia 2025

### Aktualizacja dokumentacji bezpieczeństwa - Specyfikacja MCP 2025-11-25

#### Najlepsze praktyki bezpieczeństwa MCP (02-Security/mcp-best-practices.md) - Aktualizacja wersji specyfikacji
- **Aktualizacja wersji protokołu**: Zaktualizowano odniesienia do najnowszej Specyfikacji MCP 2025-11-25 (wydanej 25 listopada 2025)
  - Zaktualizowano wszystkie odniesienia do wersji specyfikacji z 2025-06-18 na 2025-11-25
  - Zaktualizowano daty dokumentów z 18 sierpnia 2025 na 18 grudnia 2025
  - Zweryfikowano, że wszystkie adresy URL specyfikacji wskazują na aktualną dokumentację
- **Weryfikacja treści**: Kompleksowa walidacja najlepszych praktyk bezpieczeństwa względem najnowszych standardów
  - **Rozwiązania Microsoft Security**: Zweryfikowano aktualną terminologię i linki dotyczące Prompt Shields (wcześniej "Wykrywanie ryzyka Jailbreak"), Azure Content Safety, Microsoft Entra ID oraz Azure Key Vault
  - **Bezpieczeństwo OAuth 2.1**: Potwierdzono zgodność z najnowszymi najlepszymi praktykami bezpieczeństwa OAuth
  - **Standardy OWASP**: Zweryfikowano aktualność odniesień do OWASP Top 10 dla LLM
  - **Usługi Azure**: Zweryfikowano wszystkie linki do dokumentacji Microsoft Azure oraz najlepsze praktyki
- **Zgodność ze standardami**: Wszystkie odwołane standardy bezpieczeństwa potwierdzone jako aktualne
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Najlepsze praktyki bezpieczeństwa OAuth 2.1
  - Ramy bezpieczeństwa i zgodności Azure
- **Zasoby implementacyjne**: Zweryfikowano wszystkie linki i zasoby przewodników implementacyjnych
  - Wzorce uwierzytelniania Azure API Management
  - Przewodniki integracji Microsoft Entra ID
  - Zarządzanie sekretami Azure Key Vault
  - Pipeline DevSecOps i rozwiązania monitorujące

### Zapewnienie jakości dokumentacji
- **Zgodność ze specyfikacją**: Zapewniono, że wszystkie obowiązkowe wymagania bezpieczeństwa MCP (MUST/MUST NOT) są zgodne z najnowszą specyfikacją
- **Aktualność zasobów**: Zweryfikowano wszystkie zewnętrzne linki do dokumentacji Microsoft, standardów bezpieczeństwa i przewodników implementacyjnych
- **Zakres najlepszych praktyk**: Potwierdzono kompleksowe omówienie uwierzytelniania, autoryzacji, zagrożeń specyficznych dla AI, bezpieczeństwa łańcucha dostaw oraz wzorców korporacyjnych

## 6 października 2025

### Rozszerzenie sekcji Wprowadzenie – Zaawansowane użycie serwera i prosta autoryzacja

#### Zaawansowane użycie serwera (03-GettingStarted/10-advanced)
- **Dodano nowy rozdział**: Wprowadzono kompleksowy przewodnik po zaawansowanym użyciu serwera MCP, obejmujący zarówno architekturę serwera regularnego, jak i niskopoziomowego.
  - **Serwer regularny vs. niskopoziomowy**: Szczegółowe porównanie i przykłady kodu w Python i TypeScript dla obu podejść.
  - **Projekt oparty na handlerach**: Wyjaśnienie zarządzania narzędziami/zasobami/promptami opartego na handlerach dla skalowalnych i elastycznych implementacji serwera.
  - **Praktyczne wzorce**: Scenariusze z życia, gdzie wzorce niskopoziomowego serwera są korzystne dla zaawansowanych funkcji i architektury.

#### Prosta autoryzacja (03-GettingStarted/11-simple-auth)
- **Dodano nowy rozdział**: Przewodnik krok po kroku dotyczący implementacji prostej autoryzacji w serwerach MCP.
  - **Koncepcje autoryzacji**: Jasne wyjaśnienie różnicy między uwierzytelnianiem a autoryzacją oraz obsługi poświadczeń.
  - **Implementacja Basic Auth**: Wzorce autoryzacji oparte na middleware w Python (Starlette) i TypeScript (Express) wraz z przykładami kodu.
  - **Przejście do zaawansowanego bezpieczeństwa**: Wskazówki dotyczące rozpoczęcia od prostej autoryzacji i przejścia do OAuth 2.1 oraz RBAC, z odniesieniami do modułów zaawansowanego bezpieczeństwa.

Te dodatki dostarczają praktycznych, praktycznych wskazówek do budowy bardziej solidnych, bezpiecznych i elastycznych implementacji serwerów MCP, łącząc podstawowe koncepcje z zaawansowanymi wzorcami produkcyjnymi.

## 29 września 2025

### Laboratoria integracji bazy danych serwera MCP - Kompleksowa ścieżka nauki praktycznej

#### 11-MCPServerHandsOnLabs - Nowy kompletny program nauczania integracji bazy danych
- **Kompletny 13-laboratoryjny program nauki**: Dodano kompleksowy program praktyczny do budowy produkcyjnych serwerów MCP z integracją bazy danych PostgreSQL
  - **Przykład z życia**: Przypadek użycia analityki Zava Retail demonstrujący wzorce klasy korporacyjnej
  - **Strukturalna progresja nauki**:
    - **Laboratoria 00-03: Podstawy** - Wprowadzenie, architektura rdzenia, bezpieczeństwo i multi-tenantowość, konfiguracja środowiska
    - **Laboratoria 04-06: Budowa serwera MCP** - Projektowanie bazy danych i schemat, implementacja serwera MCP, rozwój narzędzi  
    - **Laboratoria 07-09: Zaawansowane funkcje** - Integracja wyszukiwania semantycznego, testowanie i debugowanie, integracja z VS Code
    - **Laboratoria 10-12: Produkcja i najlepsze praktyki** - Strategie wdrożenia, monitorowanie i obserwowalność, najlepsze praktyki i optymalizacja
  - **Technologie korporacyjne**: Framework FastMCP, PostgreSQL z pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Zaawansowane funkcje**: Row Level Security (RLS), wyszukiwanie semantyczne, dostęp do danych multi-tenant, wektorowe osadzenia, monitorowanie w czasie rzeczywistym

#### Standaryzacja terminologii - konwersja modułów na laboratoria
- **Kompleksowa aktualizacja dokumentacji**: Systematycznie zaktualizowano wszystkie pliki README w 11-MCPServerHandsOnLabs, aby używać terminologii "Laboratorium" zamiast "Moduł"
  - **Nagłówki sekcji**: Zmieniono "Co obejmuje ten moduł" na "Co obejmuje to laboratorium" we wszystkich 13 laboratoriach
  - **Opis treści**: Zmieniono "Ten moduł zapewnia..." na "To laboratorium zapewnia..." w całej dokumentacji
  - **Cele nauki**: Zmieniono "Pod koniec tego modułu..." na "Pod koniec tego laboratorium..."
  - **Linki nawigacyjne**: Przekonwertowano wszystkie odniesienia "Moduł XX:" na "Laboratorium XX:" w odnośnikach i nawigacji
  - **Śledzenie ukończenia**: Zmieniono "Po ukończeniu tego modułu..." na "Po ukończeniu tego laboratorium..."
  - **Zachowano odniesienia techniczne**: Zachowano odniesienia do modułów Pythona w plikach konfiguracyjnych (np. `"module": "mcp_server.main"`)

#### Ulepszenie przewodnika nauki (study_guide.md)
- **Wizualna mapa programu nauczania**: Dodano nową sekcję "11. Laboratoria integracji bazy danych" z kompleksową wizualizacją struktury laboratoriów
- **Struktura repozytorium**: Zaktualizowano z dziesięciu do jedenastu głównych sekcji z szczegółowym opisem 11-MCPServerHandsOnLabs
- **Wskazówki dotyczące ścieżki nauki**: Ulepszono instrukcje nawigacji obejmujące sekcje 00-11
- **Zakres technologii**: Dodano szczegóły integracji FastMCP, PostgreSQL i usług Azure
- **Efekty nauki**: Podkreślono rozwój produkcyjnych serwerów, wzorce integracji baz danych i bezpieczeństwo korporacyjne

#### Ulepszenie struktury głównego README
- **Terminologia oparta na laboratoriach**: Zaktualizowano główny README.md w 11-MCPServerHandsOnLabs, aby konsekwentnie używać struktury "Laboratorium"
- **Organizacja ścieżki nauki**: Jasna progresja od podstawowych koncepcji przez zaawansowaną implementację do wdrożenia produkcyjnego
- **Skupienie na praktyce**: Nacisk na praktyczną naukę z wzorcami i technologiami klasy korporacyjnej

### Poprawki jakości i spójności dokumentacji
- **Nacisk na naukę praktyczną**: Wzmocniono podejście oparte na laboratoriach w całej dokumentacji
- **Skupienie na wzorcach korporacyjnych**: Podkreślono produkcyjne implementacje i kwestie bezpieczeństwa korporacyjnego
- **Integracja technologii**: Kompleksowe omówienie nowoczesnych usług Azure i wzorców integracji AI
- **Progresja nauki**: Jasna, strukturalna ścieżka od podstaw do wdrożenia produkcyjnego

## 26 września 2025

### Ulepszenie studiów przypadków - Integracja rejestru MCP GitHub

#### Studia przypadków (09-CaseStudy/) - Skupienie na rozwoju ekosystemu
- **README.md**: Znaczne rozszerzenie z kompleksowym studium przypadku rejestru MCP GitHub
  - **Studium przypadku rejestru MCP GitHub**: Nowe kompleksowe studium przypadku analizujące uruchomienie rejestru MCP GitHub we wrześniu 2025
    - **Analiza problemu**: Szczegółowa analiza fragmentacji odkrywania i wdrażania serwerów MCP
    - **Architektura rozwiązania**: Podejście scentralizowanego rejestru GitHub z instalacją VS Code jednym kliknięciem
    - **Wpływ biznesowy**: Mierzalne usprawnienia w onboardingu i produktywności deweloperów
    - **Wartość strategiczna**: Skupienie na modularnym wdrażaniu agentów i interoperacyjności między narzędziami
    - **Rozwój ekosystemu**: Pozycjonowanie jako platforma bazowa dla integracji agentowej
  - **Ulepszona struktura studiów przypadków**: Zaktualizowano wszystkie siedem studiów przypadków z jednolitą formą i kompleksowymi opisami
    - Azure AI Travel Agents: Nacisk na orkiestrację wielu agentów
    - Integracja Azure DevOps: Skupienie na automatyzacji workflow
    - Pobieranie dokumentacji w czasie rzeczywistym: Implementacja klienta konsolowego Python
    - Interaktywny generator planu nauki: Aplikacja webowa Chainlit konwersacyjna
    - Dokumentacja w edytorze: Integracja VS Code i GitHub Copilot
    - Azure API Management: Wzorce integracji API korporacyjnych
    - Rejestr MCP GitHub: Rozwój ekosystemu i platforma społecznościowa
  - **Kompleksowe podsumowanie**: Przepisana sekcja podsumowania podkreślająca siedem studiów przypadków obejmujących różne wymiary implementacji MCP
    - Integracja korporacyjna, orkiestracja multi-agentowa, produktywność deweloperów
    - Rozwój ekosystemu, zastosowania edukacyjne
    - Ulepszone wglądy w wzorce architektoniczne, strategie implementacji i najlepsze praktyki
    - Nacisk na MCP jako dojrzały, gotowy do produkcji protokół

#### Aktualizacje przewodnika nauki (study_guide.md)
- **Wizualna mapa programu nauczania**: Zaktualizowano mapę myśli o rejestr MCP GitHub w sekcji studiów przypadków
- **Opis studiów przypadków**: Rozszerzono z ogólnych opisów do szczegółowego podziału siedmiu kompleksowych studiów przypadków
- **Struktura repozytorium**: Zaktualizowano sekcję 10, aby odzwierciedlić kompleksowe pokrycie studiów przypadków ze szczegółami implementacji
- **Integracja dziennika zmian**: Dodano wpis z 26 września 2025 dokumentujący dodanie rejestru MCP GitHub i ulepszenia studiów przypadków
- **Aktualizacja daty**: Zaktualizowano znacznik czasowy stopki, aby odzwierciedlić najnowszą rewizję (26 września 2025)

### Poprawki jakości dokumentacji
- **Ujednolicenie**: Ustandaryzowano formatowanie i strukturę studiów przypadków we wszystkich siedmiu przykładach
- **Kompleksowe pokrycie**: Studia przypadków obejmują teraz scenariusze korporacyjne, produktywność deweloperów i rozwój ekosystemu
- **Pozycjonowanie strategiczne**: Wzmocniono nacisk na MCP jako platformę bazową dla wdrażania systemów agentowych
- **Integracja zasobów**: Zaktualizowano dodatkowe zasoby o link do rejestru MCP GitHub

## 15 września 2025

### Rozszerzenie tematów zaawansowanych - Własne transporty i inżynieria kontekstu

#### Własne transporty MCP (05-AdvancedTopics/mcp-transport/) - Nowy przewodnik implementacji zaawansowanej
- **README.md**: Kompletny przewodnik implementacji własnych mechanizmów transportu MCP
  - **Transport Azure Event Grid**: Kompleksowa implementacja bezserwerowego transportu zdarzeniowego
    - Przykłady w C#, TypeScript i Python z integracją Azure Functions
    - Wzorce architektury zdarzeniowej dla skalowalnych rozwiązań MCP
    - Odbiorniki webhook i obsługa wiadomości push
  - **Transport Azure Event Hubs**: Implementacja transportu strumieniowego o wysokiej przepustowości
    - Możliwości strumieniowania w czasie rzeczywistym dla scenariuszy niskich opóźnień
    - Strategie partycjonowania i zarządzanie checkpointami
    - Grupowanie wiadomości i optymalizacja wydajności
  - **Wzorce integracji korporacyjnej**: Przykłady architektury gotowej do produkcji
    - Rozproszona obróbka MCP na wielu Azure Functions
    - Hybrydowe architektury transportu łączące różne typy transportu
    - Trwałość wiadomości, niezawodność i strategie obsługi błędów
  - **Bezpieczeństwo i monitorowanie**: Integracja Azure Key Vault i wzorce obserwowalności
    - Uwierzytelnianie tożsamości zarządzanej i dostęp na zasadzie najmniejszych uprawnień
    - Telemetria Application Insights i monitorowanie wydajności
    - Obwody zabezpieczające i wzorce odporności na błędy
  - **Frameworki testowe**: Kompleksowe strategie testowania własnych transportów
    - Testy jednostkowe z użyciem podwójników testowych i frameworków do mockowania
    - Testy integracyjne z Azure Test Containers
    - Rozważania dotyczące testów wydajności i obciążeniowych

#### Inżynieria kontekstu (05-AdvancedTopics/mcp-contextengineering/) - Nowa dziedzina AI
- **README.md**: Kompleksowe omówienie inżynierii kontekstu jako rozwijającej się dziedziny
  - **Podstawowe zasady**: Pełne udostępnianie kontekstu, świadomość decyzji akcji i zarządzanie oknem kontekstu
  - **Zgodność z protokołem MCP**: Jak projekt MCP adresuje wyzwania inżynierii kontekstu
    - Ograniczenia okna kontekstu i strategie progresywnego ładowania
    - Określanie relewantności i dynamiczne pobieranie kontekstu
    - Obsługa kontekstu multimodalnego i kwestie bezpieczeństwa
  - **Podejścia implementacyjne**: Architektury jednoprocesowe vs. wieloagentowe
    - Techniki dzielenia i priorytetyzacji kontekstu
    - Progresywne ładowanie i strategie kompresji kontekstu
    - Warstwowe podejścia do kontekstu i optymalizacja pobierania
  - **Ramka pomiarowa**: Nowe metryki oceny efektywności kontekstu
    - Efektywność wejścia, wydajność, jakość i doświadczenie użytkownika
    - Eksperymentalne podejścia do optymalizacji kontekstu
    - Analiza błędów i metody poprawy

#### Aktualizacje nawigacji programu nauczania (README.md)
- **Ulepszona struktura modułów**: Zaktualizowano tabelę programu nauczania o nowe tematy zaawansowane
  - Dodano wpisy Inżynieria kontekstu (5.14) i Własny transport (5.15)
  - Spójne formatowanie i linki nawigacyjne we wszystkich modułach
  - Zaktualizowano opisy, aby odzwierciedlały aktualny zakres treści

### Ulepszenia struktury katalogów
- **Standaryzacja nazewnictwa**: Zmieniono nazwę "mcp transport" na "mcp-transport" dla spójności z innymi folderami tematów zaawansowanych
- **Organizacja treści**: Wszystkie foldery 05-AdvancedTopics teraz stosują spójny wzorzec nazewnictwa (mcp-[temat])

### Ulepszenia jakości dokumentacji
- **Zgodność ze specyfikacją MCP**: Wszystkie nowe treści odnoszą się do aktualnej Specyfikacji MCP 2025-06-18
- **Przykłady wielojęzyczne**: Kompleksowe przykłady kodu w C#, TypeScript i Python
- **Skupienie na korporacjach**: Wzorce gotowe do produkcji i integracja z chmurą Azure
- **Wizualizacja dokumentacji**: Diagramy Mermaid do wizualizacji architektury i przepływów

## 18 sierpnia 2025

### Kompleksowa aktualizacja dokumentacji - Standardy MCP 2025-06-18

#### Najlepsze praktyki bezpieczeństwa MCP (02-Security/) - Pełna modernizacja
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Całkowite przepisanie zgodne ze Specyfikacją MCP 2025-06-18
  - **Wymagania obowiązkowe**: Dodano wyraźne wymagania MUSI/NIE MUSI z oficjalnej specyfikacji z czytelnymi wskaźnikami wizualnymi
  - **12 podstawowych praktyk bezpieczeństwa**: Przekształcone z listy 15 elementów na kompleksowe domeny bezpieczeństwa
    - Bezpieczeństwo tokenów i uwierzytelnianie z integracją z zewnętrznym dostawcą tożsamości
    - Zarządzanie sesją i bezpieczeństwo transportu z wymaganiami kryptograficznymi
    - Ochrona przed zagrożeniami specyficznymi dla AI z integracją Microsoft Prompt Shields
    - Kontrola dostępu i uprawnienia z zasadą najmniejszych uprawnień
    - Bezpieczeństwo treści i monitorowanie z integracją Azure Content Safety
    - Bezpieczeństwo łańcucha dostaw z kompleksową weryfikacją komponentów
    - Bezpieczeństwo OAuth i zapobieganie atakom typu confused deputy z implementacją PKCE
    - Reagowanie na incydenty i odzyskiwanie z automatycznymi możliwościami
    - Zgodność i zarządzanie z dostosowaniem do regulacji
    - Zaawansowane kontrole bezpieczeństwa z architekturą zero trust
    - Integracja ekosystemu bezpieczeństwa Microsoft z kompleksowymi rozwiązaniami
    - Ciągła ewolucja bezpieczeństwa z adaptacyjnymi praktykami
  - **Rozwiązania bezpieczeństwa Microsoft**: Ulepszone wskazówki integracyjne dla Prompt Shields, Azure Content Safety, Entra ID i GitHub Advanced Security
  - **Zasoby wdrożeniowe**: Skategoryzowane kompleksowe linki do zasobów według Oficjalnej dokumentacji MCP, Rozwiązań bezpieczeństwa Microsoft, Standardów bezpieczeństwa i Przewodników wdrożeniowych

#### Zaawansowane kontrole bezpieczeństwa (02-Security/) - Wdrożenie korporacyjne
- **MCP-SECURITY-CONTROLS-2025.md**: Kompletny przegląd z ramami bezpieczeństwa klasy korporacyjnej
  - **9 kompleksowych domen bezpieczeństwa**: Rozszerzone z podstawowych kontroli do szczegółowych ram korporacyjnych
    - Zaawansowane uwierzytelnianie i autoryzacja z integracją Microsoft Entra ID
    - Bezpieczeństwo tokenów i kontrole anty-przekazywania z kompleksową walidacją
    - Kontrole bezpieczeństwa sesji z zapobieganiem przejęciu
    - Kontrole bezpieczeństwa specyficzne dla AI z zapobieganiem wstrzyknięciom promptów i zatruwaniu narzędzi
    - Zapobieganie atakom confused deputy z bezpieczeństwem proxy OAuth
    - Bezpieczeństwo wykonywania narzędzi z sandboxingiem i izolacją
    - Kontrole bezpieczeństwa łańcucha dostaw z weryfikacją zależności
    - Kontrole monitorowania i wykrywania z integracją SIEM
    - Reagowanie na incydenty i odzyskiwanie z automatycznymi możliwościami
  - **Przykłady wdrożeń**: Dodano szczegółowe bloki konfiguracji YAML i przykłady kodu
  - **Integracja rozwiązań Microsoft**: Kompleksowe omówienie usług bezpieczeństwa Azure, GitHub Advanced Security i zarządzania tożsamością korporacyjną

#### Zaawansowane tematy bezpieczeństwa (05-AdvancedTopics/mcp-security/) - Wdrożenie produkcyjne
- **README.md**: Kompletny przepis na wdrożenie bezpieczeństwa korporacyjnego
  - **Dostosowanie do aktualnej specyfikacji**: Zaktualizowano do specyfikacji MCP 2025-06-18 z obowiązkowymi wymaganiami bezpieczeństwa
  - **Ulepszone uwierzytelnianie**: Integracja Microsoft Entra ID z kompleksowymi przykładami .NET i Java Spring Security
  - **Integracja bezpieczeństwa AI**: Implementacja Microsoft Prompt Shields i Azure Content Safety ze szczegółowymi przykładami w Pythonie
  - **Zaawansowane łagodzenie zagrożeń**: Kompleksowe przykłady wdrożeń dla
    - Zapobiegania atakom confused deputy z PKCE i walidacją zgody użytkownika
    - Zapobiegania przekazywaniu tokenów z walidacją odbiorcy i bezpiecznym zarządzaniem tokenami
    - Zapobiegania przejęciu sesji z powiązaniem kryptograficznym i analizą zachowań
  - **Integracja bezpieczeństwa korporacyjnego**: Monitorowanie Azure Application Insights, potoki wykrywania zagrożeń i bezpieczeństwo łańcucha dostaw
  - **Lista kontrolna wdrożenia**: Jasne rozróżnienie obowiązkowych i zalecanych kontroli bezpieczeństwa z korzyściami ekosystemu bezpieczeństwa Microsoft

### Jakość dokumentacji i zgodność ze standardami
- **Odniesienia do specyfikacji**: Zaktualizowano wszystkie odniesienia do aktualnej specyfikacji MCP 2025-06-18
- **Ekosystem bezpieczeństwa Microsoft**: Ulepszone wskazówki integracyjne w całej dokumentacji bezpieczeństwa
- **Praktyczne wdrożenia**: Dodano szczegółowe przykłady kodu w .NET, Java i Python z wzorcami korporacyjnymi
- **Organizacja zasobów**: Kompleksowa kategoryzacja oficjalnej dokumentacji, standardów bezpieczeństwa i przewodników wdrożeniowych
- **Wskaźniki wizualne**: Wyraźne oznaczenia wymagań obowiązkowych i praktyk zalecanych


#### Podstawowe koncepcje (01-CoreConcepts/) - Kompleksowa modernizacja
- **Aktualizacja wersji protokołu**: Zaktualizowano do odniesienia aktualnej specyfikacji MCP 2025-06-18 z wersjonowaniem opartym na dacie (format RRRR-MM-DD)
- **Udoskonalenie architektury**: Ulepszone opisy hostów, klientów i serwerów odzwierciedlające aktualne wzorce architektury MCP
  - Hosty teraz jasno zdefiniowane jako aplikacje AI koordynujące wiele połączeń klientów MCP
  - Klienci opisani jako łączniki protokołu utrzymujące relacje jeden do jednego z serwerami
  - Serwery rozszerzone o scenariusze wdrożeń lokalnych i zdalnych
- **Przebudowa prymitywów**: Kompletny przegląd prymitywów serwera i klienta
  - Prymitywy serwera: Zasoby (źródła danych), Prompty (szablony), Narzędzia (funkcje wykonywalne) ze szczegółowymi wyjaśnieniami i przykładami
  - Prymitywy klienta: Próbkowanie (uzupełnienia LLM), Elicytacja (wejście użytkownika), Logowanie (debugowanie/monitorowanie)
  - Zaktualizowano do aktualnych wzorców metod odkrywania (`*/list`), pobierania (`*/get`) i wykonywania (`*/call`)
- **Architektura protokołu**: Wprowadzono model architektury dwuwarstwowej
  - Warstwa danych: Podstawa JSON-RPC 2.0 z zarządzaniem cyklem życia i prymitywami
  - Warstwa transportu: STDIO (lokalny) i Streamable HTTP z SSE (zdalny) mechanizmy transportu
- **Ramowy model bezpieczeństwa**: Kompleksowe zasady bezpieczeństwa obejmujące wyraźną zgodę użytkownika, ochronę prywatności danych, bezpieczeństwo wykonywania narzędzi i bezpieczeństwo warstwy transportu
- **Wzorce komunikacji**: Zaktualizowano komunikaty protokołu pokazujące inicjalizację, odkrywanie, wykonywanie i przepływy powiadomień
- **Przykłady kodu**: Odświeżone przykłady wielojęzyczne (.NET, Java, Python, JavaScript) odzwierciedlające aktualne wzorce SDK MCP

#### Bezpieczeństwo (02-Security/) - Kompleksowy przegląd bezpieczeństwa  
- **Zgodność ze standardami**: Pełna zgodność z wymaganiami bezpieczeństwa specyfikacji MCP 2025-06-18
- **Ewolucja uwierzytelniania**: Udokumentowana ewolucja od niestandardowych serwerów OAuth do delegacji zewnętrznego dostawcy tożsamości (Microsoft Entra ID)
- **Analiza zagrożeń specyficznych dla AI**: Ulepszone omówienie nowoczesnych wektorów ataków AI
  - Szczegółowe scenariusze ataków wstrzyknięcia promptów z przykładami z rzeczywistego świata
  - Mechanizmy zatruwania narzędzi i wzorce ataków "rug pull"
  - Zatruwanie okna kontekstowego i ataki na zamieszanie modelu
- **Rozwiązania bezpieczeństwa AI Microsoft**: Kompleksowe omówienie ekosystemu bezpieczeństwa Microsoft
  - AI Prompt Shields z zaawansowanym wykrywaniem, wyróżnianiem i technikami delimiterów
  - Wzorce integracji Azure Content Safety
  - GitHub Advanced Security dla ochrony łańcucha dostaw
- **Zaawansowane łagodzenie zagrożeń**: Szczegółowe kontrole bezpieczeństwa dla
  - Przejęcia sesji z scenariuszami ataków specyficznymi dla MCP i wymaganiami kryptograficznymi dla ID sesji
  - Problemów confused deputy w scenariuszach proxy MCP z wyraźnymi wymaganiami zgody
  - Luka w przekazywaniu tokenów z obowiązkowymi kontrolami walidacji
- **Bezpieczeństwo łańcucha dostaw**: Rozszerzone omówienie łańcucha dostaw AI obejmujące modele bazowe, usługi osadzania, dostawców kontekstu i API stron trzecich
- **Bezpieczeństwo fundamentów**: Ulepszona integracja z wzorcami bezpieczeństwa korporacyjnego, w tym architekturą zero trust i ekosystemem bezpieczeństwa Microsoft
- **Organizacja zasobów**: Skategoryzowane kompleksowe linki do zasobów według typu (Oficjalna dokumentacja, Standardy, Badania, Rozwiązania Microsoft, Przewodniki wdrożeniowe)

### Ulepszenia jakości dokumentacji
- **Strukturalne cele nauki**: Ulepszone cele nauki z konkretnymi, wykonalnymi rezultatami
- **Odnośniki krzyżowe**: Dodano linki między powiązanymi tematami bezpieczeństwa i podstawowych koncepcji
- **Aktualne informacje**: Zaktualizowano wszystkie odniesienia dat i linki do specyfikacji do aktualnych standardów
- **Wskazówki wdrożeniowe**: Dodano konkretne, wykonalne wytyczne wdrożeniowe w obu sekcjach

## 16 lipca 2025

### README i ulepszenia nawigacji
- Całkowicie przeprojektowano nawigację programu nauczania w README.md
- Zastąpiono tagi `<details>` bardziej dostępnym formatem tabelarycznym
- Stworzono alternatywne opcje układu w nowym folderze "alternative_layouts"
- Dodano przykłady nawigacji w stylu kart, zakładek i akordeonu
- Zaktualizowano sekcję struktury repozytorium, aby uwzględnić wszystkie najnowsze pliki
- Ulepszono sekcję "Jak korzystać z tego programu nauczania" z jasnymi zaleceniami
- Zaktualizowano linki do specyfikacji MCP, aby wskazywały poprawne adresy URL
- Dodano sekcję Inżynieria kontekstu (5.14) do struktury programu nauczania

### Aktualizacje przewodnika nauki
- Całkowicie zrewidowano przewodnik nauki, aby dostosować go do aktualnej struktury repozytorium
- Dodano nowe sekcje dla klientów MCP i narzędzi oraz popularnych serwerów MCP
- Zaktualizowano wizualną mapę programu nauczania, aby dokładnie odzwierciedlała wszystkie tematy
- Ulepszono opisy tematów zaawansowanych, aby objąć wszystkie specjalistyczne obszary
- Zaktualizowano sekcję studiów przypadków, aby odzwierciedlała rzeczywiste przykłady
- Dodano ten kompleksowy dziennik zmian

### Wkłady społeczności (06-CommunityContributions/)
- Dodano szczegółowe informacje o serwerach MCP do generowania obrazów
- Dodano kompleksową sekcję o używaniu Claude w VSCode
- Dodano instrukcje konfiguracji i użytkowania klienta terminalowego Cline
- Zaktualizowano sekcję klientów MCP, aby uwzględnić wszystkie popularne opcje klientów
- Ulepszono przykłady wkładów o dokładniejsze próbki kodu

### Tematy zaawansowane (05-AdvancedTopics/)
- Zorganizowano wszystkie foldery specjalistycznych tematów z jednolitym nazewnictwem
- Dodano materiały i przykłady inżynierii kontekstu
- Dodano dokumentację integracji agenta Foundry
- Ulepszono dokumentację integracji bezpieczeństwa Entra ID

## 11 czerwca 2025

### Pierwsze utworzenie
- Wydano pierwszą wersję programu nauczania MCP dla początkujących
- Stworzono podstawową strukturę dla wszystkich 10 głównych sekcji
- Wdrożono wizualną mapę programu nauczania do nawigacji
- Dodano początkowe projekty przykładowe w wielu językach programowania

### Rozpoczęcie pracy (03-GettingStarted/)
- Stworzono pierwsze przykłady implementacji serwera
- Dodano wskazówki dotyczące rozwoju klienta
- Uwzględniono instrukcje integracji klienta LLM
- Dodano dokumentację integracji VS Code
- Wdrożono przykłady serwera Server-Sent Events (SSE)

### Podstawowe koncepcje (01-CoreConcepts/)
- Dodano szczegółowe wyjaśnienie architektury klient-serwer
- Stworzono dokumentację kluczowych komponentów protokołu
- Udokumentowano wzorce komunikatów w MCP

## 23 maja 2025

### Struktura repozytorium
- Zainicjowano repozytorium z podstawową strukturą folderów
- Stworzono pliki README dla każdej głównej sekcji
- Skonfigurowano infrastrukturę tłumaczeń
- Dodano zasoby graficzne i diagramy

### Dokumentacja
- Stworzono początkowy README.md z przeglądem programu nauczania
- Dodano pliki CODE_OF_CONDUCT.md i SECURITY.md
- Skonfigurowano SUPPORT.md z wytycznymi dotyczącymi uzyskiwania pomocy
- Stworzono wstępną strukturę przewodnika nauki

## 15 kwietnia 2025

### Planowanie i ramy
- Wstępne planowanie programu nauczania MCP dla początkujących
- Zdefiniowano cele nauki i grupę docelową
- Nakreślono strukturę programu nauczania w 10 sekcjach
- Opracowano ramy koncepcyjne dla przykładów i studiów przypadków
- Stworzono wstępne prototypy przykładów dla kluczowych koncepcji

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->