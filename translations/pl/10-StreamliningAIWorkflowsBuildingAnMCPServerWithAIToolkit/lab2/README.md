# 🌐 Moduł 2: Podstawy MCP z AI Toolkit

[![Duration](https://img.shields.io/badge/Duration-20%20minutes-blue.svg)]()
[![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-yellow.svg)]()
[![Prerequisites](https://img.shields.io/badge/Prerequisites-Module%201%20Complete-orange.svg)]()

## 📋 Cele nauki

Po ukończeniu tego modułu będziesz potrafił:
- ✅ Zrozumieć architekturę i korzyści Model Context Protocol (MCP)
- ✅ Poznać ekosystem serwerów MCP Microsoftu
- ✅ Zintegrować serwery MCP z AI Toolkit Agent Builder
- ✅ Zbudować funkcjonalnego agenta automatyzacji przeglądarki z użyciem Playwright MCP
- ✅ Skonfigurować i przetestować narzędzia MCP w swoich agentach
- ✅ Eksportować i wdrażać agentów zasilanych MCP do użytku produkcyjnego

## 🎯 Kontynuacja z Modułu 1

W Moduł 1 opanowaliśmy podstawy AI Toolkit i stworzyliśmy naszego pierwszego agenta w Pythonie. Teraz **wzbogacimy** twoich agentów, łącząc ich z zewnętrznymi narzędziami i usługami dzięki rewolucyjnemu **Model Context Protocol (MCP)**.

Pomyśl o tym jak o przejściu z prostego kalkulatora do pełnoprawnego komputera – twoi agenci AI zyskają możliwość:
- 🌐 Przeglądania i interakcji ze stronami internetowymi
- 📁 Dostępu i manipulacji plikami
- 🔧 Integracji z systemami korporacyjnymi
- 📊 Przetwarzania danych w czasie rzeczywistym z API

## 🧠 Zrozumienie Model Context Protocol (MCP)

### 🔍 Czym jest MCP?

Model Context Protocol (MCP) to **„USB-C dla aplikacji AI”** – rewolucyjny, otwarty standard łączący duże modele językowe (LLM) z zewnętrznymi narzędziami, źródłami danych i usługami. Tak jak USB-C wyeliminowało chaos kabli, oferując jeden uniwersalny port, tak MCP upraszcza integrację AI, stosując jeden ustandaryzowany protokół.

### 🎯 Problem, który rozwiązuje MCP

**Przed MCP:**
- 🔧 Indywidualne integracje dla każdego narzędzia
- 🔄 Uzależnienie od dostawców i ich rozwiązań
- 🔒 Luki bezpieczeństwa wynikające z ad-hoc połączeń
- ⏱️ Miesiące pracy nad podstawowymi integracjami

**Z MCP:**
- ⚡ Integracja narzędzi typu plug-and-play
- 🔄 Architektura niezależna od dostawcy
- 🛡️ Wbudowane najlepsze praktyki bezpieczeństwa
- 🚀 Dodanie nowych funkcji w kilka minut

### 🏗️ Szczegóły architektury MCP

MCP opiera się na **architekturze klient-serwer**, tworząc bezpieczny i skalowalny ekosystem:

```mermaid
graph TB
    A[AI Application/Agent] --> B[MCP Client]
    B --> C[MCP Server 1: Files]
    B --> D[MCP Server 2: Web APIs]
    B --> E[MCP Server 3: Database]
    B --> F[MCP Server N: Custom Tools]
    
    C --> G[Local File System]
    D --> H[External APIs]
    E --> I[Database Systems]
    F --> J[Enterprise Systems]
```

**🔧 Kluczowe komponenty:**

| Komponent | Rola | Przykłady |
|-----------|------|-----------|
| **MCP Hosts** | Aplikacje korzystające z usług MCP | Claude Desktop, VS Code, AI Toolkit |
| **MCP Clients** | Obsługa protokołu (1:1 z serwerami) | Wbudowane w aplikacje hosta |
| **MCP Servers** | Udostępniają funkcje przez standardowy protokół | Playwright, Files, Azure, GitHub |
| **Warstwa transportowa** | Metody komunikacji | stdio, HTTP, WebSockets |

## 🏢 Ekosystem serwerów MCP Microsoftu

Microsoft przewodzi ekosystemowi MCP, oferując kompleksowy zestaw serwerów klasy korporacyjnej, które odpowiadają na rzeczywiste potrzeby biznesowe.

### 🌟 Najważniejsze serwery MCP Microsoftu

#### 1. ☁️ Azure MCP Server  
**🔗 Repozytorium**: [azure/azure-mcp](https://github.com/azure/azure-mcp)  
**🎯 Cel**: Kompleksowe zarządzanie zasobami Azure z integracją AI

**✨ Kluczowe funkcje:**  
- Deklaratywne provisionowanie infrastruktury  
- Monitorowanie zasobów w czasie rzeczywistym  
- Rekomendacje optymalizacji kosztów  
- Sprawdzanie zgodności z wymogami bezpieczeństwa

**🚀 Przykłady zastosowań:**  
- Infrastructure-as-Code z pomocą AI  
- Automatyczne skalowanie zasobów  
- Optymalizacja kosztów chmury  
- Automatyzacja procesów DevOps

#### 2. 📊 Microsoft Dataverse MCP  
**📚 Dokumentacja**: [Microsoft Dataverse Integration](https://go.microsoft.com/fwlink/?linkid=2320176)  
**🎯 Cel**: Interfejs w języku naturalnym do danych biznesowych

**✨ Kluczowe funkcje:**  
- Zapytania do bazy danych w języku naturalnym  
- Rozumienie kontekstu biznesowego  
- Własne szablony promptów  
- Zarządzanie danymi korporacyjnymi

**🚀 Przykłady zastosowań:**  
- Raportowanie BI  
- Analiza danych klientów  
- Wgląd w lejki sprzedażowe  
- Zapytania dotyczące zgodności

#### 3. 🌐 Playwright MCP Server  
**🔗 Repozytorium**: [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)  
**🎯 Cel**: Automatyzacja przeglądarki i interakcje webowe

**✨ Kluczowe funkcje:**  
- Automatyzacja międzyprzeglądarkowa (Chrome, Firefox, Safari)  
- Inteligentne wykrywanie elementów  
- Generowanie zrzutów ekranu i PDF  
- Monitorowanie ruchu sieciowego

**🚀 Przykłady zastosowań:**  
- Automatyczne testy  
- Web scraping i ekstrakcja danych  
- Monitorowanie UI/UX  
- Automatyzacja analiz konkurencji

#### 4. 📁 Files MCP Server  
**🔗 Repozytorium**: [microsoft/files-mcp-server](https://github.com/microsoft/files-mcp-server)  
**🎯 Cel**: Inteligentne operacje na systemie plików

**✨ Kluczowe funkcje:**  
- Deklaratywne zarządzanie plikami  
- Synchronizacja zawartości  
- Integracja z systemami kontroli wersji  
- Ekstrakcja metadanych

**🚀 Przykłady zastosowań:**  
- Zarządzanie dokumentacją  
- Organizacja repozytoriów kodu  
- Workflow publikacji treści  
- Obsługa plików w pipeline danych

#### 5. 📝 MarkItDown MCP Server  
**🔗 Repozytorium**: [microsoft/markitdown](https://github.com/microsoft/markitdown)  
**🎯 Cel**: Zaawansowane przetwarzanie i manipulacja Markdown

**✨ Kluczowe funkcje:**  
- Bogate parsowanie Markdown  
- Konwersja formatów (MD ↔ HTML ↔ PDF)  
- Analiza struktury treści  
- Przetwarzanie szablonów

**🚀 Przykłady zastosowań:**  
- Workflow dokumentacji technicznej  
- Systemy zarządzania treścią  
- Generowanie raportów  
- Automatyzacja baz wiedzy

#### 6. 📈 Clarity MCP Server  
**📦 Pakiet**: [@microsoft/clarity-mcp-server](https://www.npmjs.com/package/@microsoft/clarity-mcp-server)  
**🎯 Cel**: Analiza webowa i zachowania użytkowników

**✨ Kluczowe funkcje:**  
- Analiza danych heatmap  
- Nagrania sesji użytkowników  
- Metryki wydajności  
- Analiza lejków konwersji

**🚀 Przykłady zastosowań:**  
- Optymalizacja stron internetowych  
- Badania UX  
- Analiza testów A/B  
- Dashboardy BI

### 🌍 Ekosystem społecznościowy

Poza serwerami Microsoftu, ekosystem MCP obejmuje:  
- **🐙 GitHub MCP**: Zarządzanie repozytoriami i analiza kodu  
- **🗄️ MCP dla baz danych**: Integracje PostgreSQL, MySQL, MongoDB  
- **☁️ MCP dostawców chmury**: Narzędzia AWS, GCP, Digital Ocean  
- **📧 MCP komunikacji**: Integracje Slack, Teams, Email

## 🛠️ Laboratorium praktyczne: Budowa agenta automatyzacji przeglądarki

**🎯 Cel projektu**: Stwórz inteligentnego agenta automatyzacji przeglądarki z użyciem serwera Playwright MCP, który potrafi nawigować po stronach, wyciągać informacje i wykonywać złożone interakcje webowe.

### 🚀 Faza 1: Podstawy agenta

#### Krok 1: Inicjalizacja agenta  
1. **Otwórz AI Toolkit Agent Builder**  
2. **Utwórz nowego agenta** z następującą konfiguracją:  
   - **Nazwa**: `BrowserAgent`  
   - **Model**: Wybierz GPT-4o  

![BrowserAgent](../../../../translated_images/pl/BrowserAgent.09c1adde5e136573b64ab1baecd830049830e295eac66cb18bebb85fb386e00a.png)

### 🔧 Faza 2: Integracja MCP

#### Krok 3: Dodaj integrację z serwerem MCP  
1. **Przejdź do sekcji Narzędzia** w Agent Builder  
2. **Kliknij "Add Tool"**, aby otworzyć menu integracji  
3. **Wybierz "MCP Server"** z dostępnych opcji  

![AddMCP](../../../../translated_images/pl/AddMCP.afe3308ac20aa94469a5717b632d77b2197b9838a438b05d39aeb2db3ec47ef1.png)

**🔍 Rodzaje narzędzi:**  
- **Narzędzia wbudowane**: Prekonfigurowane funkcje AI Toolkit  
- **Serwery MCP**: Integracje z usługami zewnętrznymi  
- **Własne API**: Twoje własne punkty końcowe usług  
- **Wywołania funkcji**: Bezpośredni dostęp do funkcji modelu

#### Krok 4: Wybór serwera MCP  
1. **Wybierz opcję "MCP Server"**, aby kontynuować  
![AddMCPServer](../../../../translated_images/pl/AddMCPServer.69b911ccef872cbd0d0c0c2e6a00806916e1673e543b902a23dee23e6ff54b4c.png)

2. **Przeglądaj katalog MCP**, aby zobaczyć dostępne integracje  
![MCPCatalog](../../../../translated_images/pl/MCPCatalog.a817d053145699006264f5a475f2b48fbd744e43633f656b6453c15a09ba5130.png)

### 🎮 Faza 3: Konfiguracja Playwright MCP

#### Krok 5: Wybierz i skonfiguruj Playwright  
1. **Kliknij "Use Featured MCP Servers"**, aby uzyskać dostęp do zweryfikowanych serwerów Microsoftu  
2. **Wybierz "Playwright"** z listy  
3. **Zaakceptuj domyślne MCP ID** lub dostosuj do swojego środowiska  

![MCPID](../../../../translated_images/pl/MCPID.67d446052979e819c945ff7b6430196ef587f5217daadd3ca52fa9659c1245c9.png)

#### Krok 6: Włącz funkcje Playwright  
**🔑 Kluczowy krok**: Zaznacz **WSZYSTKIE** dostępne metody Playwright, aby uzyskać maksymalną funkcjonalność  

![Tools](../../../../translated_images/pl/Tools.3ea23c447b4d9feccbd7101e6dcf9e27cb0e5273f351995fde62c5abf9a78b4c.png)

**🛠️ Podstawowe narzędzia Playwright:**  
- **Nawigacja**: `goto`, `goBack`, `goForward`, `reload`  
- **Interakcja**: `click`, `fill`, `press`, `hover`, `drag`  
- **Ekstrakcja**: `textContent`, `innerHTML`, `getAttribute`  
- **Walidacja**: `isVisible`, `isEnabled`, `waitForSelector`  
- **Zrzuty**: `screenshot`, `pdf`, `video`  
- **Sieć**: `setExtraHTTPHeaders`, `route`, `waitForResponse`

#### Krok 7: Sprawdź poprawność integracji  
**✅ Wskaźniki sukcesu:**  
- Wszystkie narzędzia widoczne w interfejsie Agent Builder  
- Brak komunikatów o błędach w panelu integracji  
- Status serwera Playwright pokazuje „Connected”  

![AgentTools](../../../../translated_images/pl/AgentTools.053cfb96a17e02199dcc6563010d2b324d4fc3ebdd24889657a6950647a52f63.png)

**🔧 Rozwiązywanie typowych problemów:**  
- **Brak połączenia**: Sprawdź połączenie internetowe i ustawienia zapory  
- **Brak narzędzi**: Upewnij się, że wszystkie funkcje zostały wybrane podczas konfiguracji  
- **Błędy uprawnień**: Zweryfikuj, czy VS Code ma odpowiednie uprawnienia systemowe

### 🎯 Faza 4: Zaawansowane tworzenie promptów

#### Krok 8: Zaprojektuj inteligentne prompt systemowe  
Stwórz zaawansowane prompt’y wykorzystujące pełne możliwości Playwright:  

```markdown
# Web Automation Expert System Prompt

## Core Identity
You are an advanced web automation specialist with deep expertise in browser automation, web scraping, and user experience analysis. You have access to Playwright tools for comprehensive browser control.

## Capabilities & Approach
### Navigation Strategy
- Always start with screenshots to understand page layout
- Use semantic selectors (text content, labels) when possible
- Implement wait strategies for dynamic content
- Handle single-page applications (SPAs) effectively

### Error Handling
- Retry failed operations with exponential backoff
- Provide clear error descriptions and solutions
- Suggest alternative approaches when primary methods fail
- Always capture diagnostic screenshots on errors

### Data Extraction
- Extract structured data in JSON format when possible
- Provide confidence scores for extracted information
- Validate data completeness and accuracy
- Handle pagination and infinite scroll scenarios

### Reporting
- Include step-by-step execution logs
- Provide before/after screenshots for verification
- Suggest optimizations and alternative approaches
- Document any limitations or edge cases encountered

## Ethical Guidelines
- Respect robots.txt and rate limiting
- Avoid overloading target servers
- Only extract publicly available information
- Follow website terms of service
```

#### Krok 9: Stwórz dynamiczne prompt’y użytkownika  
Zaprojektuj prompt’y demonstrujące różne funkcje:  

**🌐 Przykład analizy stron:**  
```markdown
Navigate to github.com/kinfey and provide a comprehensive analysis including:
1. Repository structure and organization
2. Recent activity and contribution patterns  
3. Documentation quality assessment
4. Technology stack identification
5. Community engagement metrics
6. Notable projects and their purposes

Include screenshots at key steps and provide actionable insights.
```

![Prompt](../../../../translated_images/pl/Prompt.bfc846605db4999f4d9c1b09c710ef63cae7b3057444e68bf07240fb142d9f8f.png)

### 🚀 Faza 5: Wykonanie i testowanie

#### Krok 10: Uruchom pierwszą automatyzację  
1. **Kliknij "Run"**, aby rozpocząć sekwencję automatyzacji  
2. **Monitoruj wykonanie w czasie rzeczywistym**:  
   - Automatyczne uruchomienie przeglądarki Chrome  
   - Agent nawigujący do docelowej strony  
   - Zrzuty ekranu dokumentujące każdy ważny krok  
   - Wyniki analizy przesyłane na bieżąco  

![Browser](../../../../translated_images/pl/Browser.ec011d0bd64d0d112c8a29bd8cc44c76d0bbfd0b019cb2983ef679328435ce5d.png)

#### Krok 11: Analiza wyników i wniosków  
Przejrzyj szczegółową analizę w interfejsie Agent Builder:  

![Result](../../../../translated_images/pl/Result.8638f2b6703e9ea6d58d4e4475e39456b6a51d4c787f9bf481bae694d370a69a.png)

### 🌟 Faza 6: Zaawansowane funkcje i wdrożenie

#### Krok 12: Eksport i wdrożenie produkcyjne  
Agent Builder oferuje różne opcje wdrożenia:  

![Code](../../../../translated_images/pl/Code.d9eeeead0b96db0ca19c5b10ad64cfea8c1d0d1736584262970a4d43e1403d13.png)

## 🎓 Podsumowanie Modułu 2 i kolejne kroki

### 🏆 Osiągnięcie: Mistrz integracji MCP

**✅ Opanowane umiejętności:**  
- [ ] Zrozumienie architektury i korzyści MCP  
- [ ] Poruszanie się po ekosystemie serwerów MCP Microsoftu  
- [ ] Integracja Playwright MCP z AI Toolkit  
- [ ] Budowa zaawansowanych agentów automatyzacji przeglądarki  
- [ ] Zaawansowane tworzenie promptów do automatyzacji webowej

### 📚 Dodatkowe materiały

- **🔗 Specyfikacja MCP**: [Oficjalna dokumentacja protokołu](https://modelcontextprotocol.io/)  
- **🛠️ Playwright API**: [Pełna referencja metod](https://playwright.dev/docs/api/class-playwright)  
- **🏢 Serwery MCP Microsoftu**: [Przewodnik integracji korporacyjnej](https://github.com/microsoft/mcp-servers)  
- **🌍 Przykłady społeczności**: [Galeria serwerów MCP](https://github.com/modelcontextprotocol/servers)

**🎉 Gratulacje!** Opanowałeś integrację MCP i możesz teraz tworzyć produkcyjne agentów AI z funkcjami zewnętrznych narzędzi!

### 🔜 Przejdź do następnego modułu

Chcesz rozwinąć swoje umiejętności MCP? Przejdź do **[Moduł 3: Zaawansowany rozwój MCP z AI Toolkit](../lab3/README.md)**, gdzie nauczysz się:  
- Tworzyć własne niestandardowe serwery MCP  
- Konfigurować i korzystać z najnowszego MCP Python SDK  
- Ustawiać MCP Inspector do debugowania  
- Opanować zaawansowane workflowy rozwoju serwerów MCP
- Zbuduj serwer Weather MCP od podstaw

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.