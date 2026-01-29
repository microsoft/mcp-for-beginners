# AGENTS.md

## Przegląd projektu

**MCP dla początkujących** to otwarty program edukacyjny, który umożliwia naukę Model Context Protocol (MCP) - standardowego frameworka do interakcji między modelami AI a aplikacjami klienckimi. Repozytorium zawiera kompleksowe materiały edukacyjne z praktycznymi przykładami kodu w różnych językach programowania.

### Kluczowe technologie

- **Języki programowania**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworki i SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Bazy danych**: PostgreSQL z rozszerzeniem pgvector
- **Platformy chmurowe**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Narzędzia budowania**: npm, Maven, pip, Cargo
- **Dokumentacja**: Markdown z automatycznym tłumaczeniem na wiele języków (ponad 48 języków)

### Architektura

- **11 modułów podstawowych (00-11)**: Sekwencyjna ścieżka nauki od podstaw do zaawansowanych tematów
- **Laboratoria praktyczne**: Ćwiczenia praktyczne z kompletnymi rozwiązaniami w różnych językach
- **Projekty przykładowe**: Działające implementacje serwera i klienta MCP
- **System tłumaczeń**: Automatyczny workflow GitHub Actions wspierający tłumaczenia na wiele języków
- **Zasoby graficzne**: Centralny katalog obrazów z wersjami przetłumaczonymi

## Polecenia konfiguracji

To repozytorium skupia się na dokumentacji. Większość konfiguracji odbywa się w poszczególnych projektach przykładowych i laboratoriach.

### Konfiguracja repozytorium

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Praca z projektami przykładowymi

Projekty przykładowe znajdują się w:
- `03-GettingStarted/samples/` - Przykłady specyficzne dla języków
- `03-GettingStarted/01-first-server/solution/` - Implementacje pierwszego serwera
- `03-GettingStarted/02-client/solution/` - Implementacje klienta
- `11-MCPServerHandsOnLabs/` - Kompleksowe laboratoria integracji z bazą danych

Każdy projekt przykładowy zawiera własne instrukcje konfiguracji:

#### Projekty TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Projekty Python
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Projekty Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Workflow rozwoju

### Struktura dokumentacji

- **Moduły 00-11**: Treści podstawowego programu nauczania w kolejności sekwencyjnej
- **translations/**: Wersje językowe (generowane automatycznie, nie edytować ręcznie)
- **translated_images/**: Zlokalizowane wersje obrazów (generowane automatycznie)
- **images/**: Źródłowe obrazy i diagramy

### Wprowadzanie zmian w dokumentacji

1. Edytuj tylko angielskie pliki markdown w głównych katalogach modułów (00-11)
2. Zaktualizuj obrazy w katalogu `images/`, jeśli to konieczne
3. GitHub Action co-op-translator automatycznie wygeneruje tłumaczenia
4. Tłumaczenia są regenerowane po przesłaniu zmian do głównej gałęzi

### Praca z tłumaczeniami

- **Automatyczne tłumaczenie**: Workflow GitHub Actions obsługuje wszystkie tłumaczenia
- **Nie edytuj ręcznie** plików w katalogu `translations/`
- Metadane tłumaczeń są osadzone w każdym przetłumaczonym pliku
- Obsługiwane języki: Ponad 48 języków, w tym arabski, chiński, francuski, niemiecki, hindi, japoński, koreański, portugalski, rosyjski, hiszpański i wiele innych

## Instrukcje testowania

### Walidacja dokumentacji

Ponieważ repozytorium skupia się głównie na dokumentacji, testowanie obejmuje:

1. **Walidacja linków**: Upewnij się, że wszystkie wewnętrzne linki działają
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Walidacja przykładów kodu**: Sprawdź, czy przykłady kodu się kompilują/uruchamiają
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Linting Markdown**: Sprawdź spójność formatowania
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Testowanie projektów przykładowych

Każdy projekt specyficzny dla języka zawiera własne podejście do testowania:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Wytyczne dotyczące stylu kodu

### Styl dokumentacji

- Używaj jasnego, przyjaznego dla początkujących języka
- Dołącz przykłady kodu w różnych językach, jeśli to możliwe
- Przestrzegaj najlepszych praktyk markdown:
  - Używaj nagłówków w stylu ATX (`#` syntax)
  - Używaj bloków kodu z identyfikatorami języka
  - Dołącz opisowy tekst alternatywny dla obrazów
  - Zachowaj rozsądną długość linii (bez sztywnego limitu, ale bądź rozsądny)

### Styl przykładów kodu

#### TypeScript/JavaScript
- Używaj modułów ES (`import`/`export`)
- Przestrzegaj konwencji trybu ścisłego TypeScript
- Dołącz adnotacje typów
- Celuj w ES2022

#### Python
- Przestrzegaj wytycznych stylu PEP 8
- Używaj wskazówek typów, gdzie to możliwe
- Dołącz docstringi dla funkcji i klas
- Używaj nowoczesnych funkcji Pythona (3.8+)

#### Java
- Przestrzegaj konwencji Spring Boot
- Używaj funkcji Java 21
- Przestrzegaj standardowej struktury projektu Maven
- Dołącz komentarze Javadoc

### Organizacja plików

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Budowanie i wdrażanie

### Wdrażanie dokumentacji

Repozytorium używa GitHub Pages lub podobnych do hostowania dokumentacji (jeśli dotyczy). Zmiany w głównej gałęzi uruchamiają:

1. Workflow tłumaczeń (`.github/workflows/co-op-translator.yml`)
2. Automatyczne tłumaczenie wszystkich angielskich plików markdown
3. Lokalizację obrazów, jeśli to konieczne

### Brak wymaganego procesu budowania

Repozytorium zawiera głównie dokumentację markdown. Nie jest wymagany proces kompilacji ani budowania dla treści programu nauczania.

### Wdrażanie projektów przykładowych

Poszczególne projekty przykładowe mogą mieć instrukcje wdrażania:
- Zobacz `03-GettingStarted/09-deployment/` dla wskazówek dotyczących wdrażania serwera MCP
- Przykłady wdrażania Azure Container Apps w `11-MCPServerHandsOnLabs/`

## Wytyczne dotyczące współpracy

### Proces Pull Request

1. **Fork i klonowanie**: Zrób fork repozytorium i sklonuj swój fork lokalnie
2. **Utwórz gałąź**: Używaj opisowych nazw gałęzi (np. `fix/typo-module-3`, `add/python-example`)
3. **Wprowadź zmiany**: Edytuj tylko angielskie pliki markdown (nie tłumaczenia)
4. **Testuj lokalnie**: Sprawdź, czy markdown renderuje się poprawnie
5. **Prześlij PR**: Używaj jasnych tytułów i opisów PR
6. **CLA**: Podpisz Microsoft Contributor License Agreement, gdy zostaniesz o to poproszony

### Format tytułu PR

Używaj jasnych, opisowych tytułów:
- `[Module XX] Krótki opis` dla zmian specyficznych dla modułu
- `[Samples] Opis` dla zmian w kodzie przykładowym
- `[Docs] Opis` dla ogólnych aktualizacji dokumentacji

### Co można wnieść

- Poprawki błędów w dokumentacji lub przykładach kodu
- Nowe przykłady kodu w dodatkowych językach
- Wyjaśnienia i ulepszenia istniejących treści
- Nowe studia przypadków lub praktyczne przykłady
- Zgłaszanie problemów dotyczących niejasnych lub niepoprawnych treści

### Czego NIE robić

- Nie edytuj bezpośrednio plików w katalogu `translations/`
- Nie edytuj katalogu `translated_images/`
- Nie dodawaj dużych plików binarnych bez wcześniejszej dyskusji
- Nie zmieniaj plików workflow tłumaczeń bez koordynacji

## Dodatkowe uwagi

### Utrzymanie repozytorium

- **Changelog**: Wszystkie istotne zmiany są dokumentowane w `changelog.md`
- **Przewodnik nauki**: Użyj `study_guide.md` do nawigacji po programie nauczania
- **Szablony zgłoszeń**: Używaj szablonów zgłoszeń GitHub do raportowania błędów i zgłaszania funkcji
- **Kodeks postępowania**: Wszyscy współtwórcy muszą przestrzegać Microsoft Open Source Code of Conduct

### Ścieżka nauki

Podążaj za modułami w kolejności sekwencyjnej (00-11) dla optymalnej nauki:
1. **00-02**: Podstawy (Wprowadzenie, Kluczowe koncepcje, Bezpieczeństwo)
2. **03**: Pierwsze kroki z praktyczną implementacją
3. **04-05**: Praktyczna implementacja i zaawansowane tematy
4. **06-10**: Społeczność, najlepsze praktyki i zastosowania w rzeczywistości
5. **11**: Kompleksowe laboratoria integracji z bazą danych (13 sekwencyjnych laboratoriów)

### Zasoby wsparcia

- **Dokumentacja**: https://modelcontextprotocol.io/
- **Specyfikacja**: https://spec.modelcontextprotocol.io/
- **Społeczność**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Serwer Discord Microsoft Azure AI Foundry
- **Powiązane kursy**: Zobacz README.md dla innych ścieżek nauki Microsoft

### Częste problemy

**P: Mój PR nie przechodzi testu tłumaczenia**
O: Upewnij się, że edytowałeś tylko angielskie pliki markdown w głównych katalogach modułów, a nie wersje przetłumaczone.

**P: Jak dodać nowy język?**
O: Obsługa języków jest zarządzana przez workflow co-op-translator. Otwórz zgłoszenie, aby omówić dodanie nowych języków.

**P: Przykłady kodu nie działają**
O: Upewnij się, że postępowałeś zgodnie z instrukcjami konfiguracji w README konkretnego przykładu. Sprawdź, czy masz zainstalowane odpowiednie wersje zależności.

**P: Obrazy się nie wyświetlają**
O: Sprawdź, czy ścieżki obrazów są względne i używają ukośników. Obrazy powinny znajdować się w katalogu `images/` lub `translated_images/` dla wersji zlokalizowanych.

### Uwagi dotyczące wydajności

- Workflow tłumaczeń może zająć kilka minut
- Duże obrazy powinny być zoptymalizowane przed przesłaniem
- Utrzymuj pojedyncze pliki markdown skoncentrowane i o rozsądnej wielkości
- Używaj linków względnych dla lepszej przenośności

### Zarządzanie projektem

Ten projekt przestrzega praktyk open source Microsoft:
- Licencja MIT dla kodu i dokumentacji
- Microsoft Open Source Code of Conduct
- Wymagana CLA dla współtwórców
- Problemy związane z bezpieczeństwem: Przestrzegaj wytycznych w SECURITY.md
- Wsparcie: Zobacz SUPPORT.md dla zasobów pomocy

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.