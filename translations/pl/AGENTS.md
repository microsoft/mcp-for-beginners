# AGENTS.md

## Przegląd Projektu

**MCP dla początkujących** to otwarty program nauczania do nauki Model Context Protocol (MCP) - ustandaryzowanego frameworka do interakcji między modelami AI a aplikacjami klienckimi. To repozytorium dostarcza obszerne materiały do nauki z praktycznymi przykładami kodu w różnych językach programowania.

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
- **Dokumentacja**: Markdown z automatycznym tłumaczeniem na wiele języków (48+ języków)

### Architektura

- **11 modułów rdzeniowych (00-11)**: Sekwencyjna ścieżka nauki od podstaw do zaawansowanych tematów
- **Ćwiczenia praktyczne**: Ćwiczenia z kompletnymi rozwiązaniami w wielu językach
- **Przykładowe projekty**: Działające implementacje serwera i klienta MCP
- **System tłumaczeń**: Zautomatyzowany workflow GitHub Actions do wsparcia wielu języków
- **Zasoby graficzne**: Centralny katalog obrazów z wersjami przetłumaczonymi

## Komendy konfiguracyjne

To jest repozytorium skoncentrowane na dokumentacji. Większość konfiguracji odbywa się w poszczególnych przykładowych projektach i laboratoriach.

### Konfiguracja repozytorium

```bash
# Sklonuj repozytorium
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Praca z przykładowymi projektami

Przykładowe projekty znajdują się w:
- `03-GettingStarted/samples/` - przykłady specyficzne dla języków
- `03-GettingStarted/01-first-server/solution/` - pierwsze implementacje serwera
- `03-GettingStarted/02-client/solution/` - implementacje klienta
- `11-MCPServerHandsOnLabs/` - pełne laboratoria integracji z bazą danych

Każdy przykładowy projekt zawiera własne instrukcje konfiguracji:

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
# lub
pip install -e .
python main.py
```

#### Projekty Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Proces rozwoju

### Gotowość MCP 7-28

#### Lista kontrolna gotowości repozytorium

- [x] **Jasność dla nowych współtwórców**: Ten plik definiuje cel repozytorium,
  strukturę, zasady współpracy oraz ścieżki konfiguracji przykładów.
- [x] **Polecenia build/test/lint z dokładnymi flagami**:
  - Lint dokumentacji repozytorium:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audyt wzorców linków w dokumentacji:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Walidacja przykładów TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Walidacja przykładów Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Walidacja przykładów Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Jeden realistyczny workflow, który może stać się narzędziem MCP**:
  `validate_curriculum_change`
- [x] **Wejścia/wyjścia są jawne** (patrz specyfikacja poniżej).
- [x] **Uprawnienia i tryby błędów są udokumentowane** (patrz specyfikacja poniżej).
- [x] **Testowalność w CI jest jawna** (deterministyczne polecenia, jawne
  kody wyjścia oraz dane wyjściowe możliwe do odczytu maszynowego).

#### Proponowany workflow narzędzia MCP: `validate_curriculum_change`

##### Cel

Zweryfikować zmiany w dokumentacji programu nauczania oraz stan przykładowego reprezentatywnego kodu
przed zatwierdzeniem.

##### Wejścia

- `changed_paths: string[]` (wymagane) - zmienione ścieżki w PR.
- `run_docs_lint: boolean` (domyślnie `true`)
- `run_links_audit: boolean` (domyślnie `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (domyślnie wszystkie `false`)

##### Wyjścia

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Uprawnienia

- Odczyt plików przestrzeni roboczej oraz zapis artefaktów generowanych przez narzędzia (np. raporty lint,
  logi testów); brak zapisu do `translations/` lub
  `translated_images/`.
- Wykonywanie poleceń lokalnej powłoki.
- Opcjonalny dostęp do sieci tylko do przywracania pakietów (`npm ci`,
  `python -m pip install`, rozwiązywanie zależności `mvn`).
- Brak uprawnień do push, merge ani modyfikacji `translations/` oraz
  `translated_images/`.

##### Tryby błędów

- `E_NO_INPUT_PATHS`: `changed_paths` jest puste.
- `E_INVALID_PATH`: ścieżka wejściowa wychodzi poza katalog główny repozytorium.
- `E_LINT_FAILED`: polecenie lint markdown zakończyło się błędem.
- `E_LINK_AUDIT_FAILED`: polecenie audytu linków zakończyło się błędem.
- `E_SAMPLE_TEST_FAILED`: test lub budowa przykładu zakończyła się błędem.
- `E_TIMEOUT`: polecenie przekroczyło ustawiony limit czasu.

##### Zalecany kontrakt CI

Aby zautomatyzować walidację, skonfiguruj zadanie CI, które:

- Uruchamia się na żądania pull request dotykające `*.md`, kodu przykładowego lub tego pliku.
- Uruchamia dokładne wyżej wymienione polecenia.
- Zachowuje logi jako artefakty.
- Kończy zadanie błędem przy dowolnym niezerowym kodzie wyjścia.

#### Jeśli wdrażasz serwer MCP z tego repozytorium

- [ ] Przeczytaj roboczy changelog dla MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Uruchom swój serwer z betami SDK:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Usuń założenia dotyczące sesji i handshake; traktuj każde żądanie jako
  niezależne:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Przesyłaj nagłówki `Mcp-Method` i `Mcp-Name` przy surowych żądaniach HTTP:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Zaudytuj na sztywno zakodowane kody błędów (`missing resource` przesunięty z `-32002` do `-32602`).

- [ ] Oznacz i zaplanuj migrację przestarzałych korzeni, próbkowania i
  logowania:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Przejdź z eksperymentalnego API zadań `2025-11-25`:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Przejrzyj autoryzację pod kątem wzmocnienia OAuth i OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Struktura dokumentacji

- **Moduły 00-11**: Podstawowa treść kursu w kolejności sekwencyjnej
- **translations/**: Wersje specyficzne dla języków (generowane automatycznie, nie edytuj bezpośrednio)
- **translated_images/**: Zlokalizowane wersje obrazów (generowane automatycznie)
- **images/**: Pliki źródłowe obrazów i diagramów

### Dokonywanie zmian w dokumentacji

1. Edytuj tylko angielskie pliki markdown w głównych katalogach modułów (00-11)
2. W razie potrzeby aktualizuj obrazy w katalogu `images/`
3. GitHub Action co-op-translator automatycznie wygeneruje tłumaczenia
4. Tłumaczenia są ponownie generowane przy pushu do gałęzi main

### Praca z tłumaczeniami

- **Automatyczne tłumaczenie**: Workflow GitHub Actions obsługuje wszystkie tłumaczenia
- **Nie edytuj ręcznie** plików w katalogu `translations/`
- Metadane tłumaczenia są osadzone w każdym przetłumaczonym pliku
- Obsługiwane języki: ponad 48 języków, w tym arabski, chiński, francuski, niemiecki, hindi, japoński, koreański, portugalski, rosyjski, hiszpański i wiele innych

## Instrukcje testowania

### Walidacja dokumentacji

Ponieważ jest to głównie repozytorium dokumentacji, testy koncentrują się na:

1. **Audyt wzorców linków**: Lista linków Markdown do przeglądu

   ```bash
   # Wyświetl linki Markdown (audyt wzorców)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Weryfikacja przykładów kodu**: Testowanie kompilacji/uruchomienia przykładów kodu

   ```bash
   # Przejdź do określonego przykładu i uruchom jego testy
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Lintowanie Markdown**: Sprawdzanie spójności formatowania

   ```bash
   # Użyj markdownlint, jeśli to konieczne
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testowanie przykładowych projektów

Każdy przykładowy projekt specyficzny dla języka ma własne podejście do testowania:

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
- Uwzględniaj przykłady kodu w kilku językach, tam gdzie to stosowne
- Stosuj najlepsze praktyki markdown:
  - Używaj nagłówków w stylu ATX (składnia `#`)
  - Używaj ogrodzonych bloków kodu z identyfikatorami języka
  - Dołączaj opisowy tekst alt do obrazów
  - Utrzymuj rozsądne długości linii (bez sztywnego limitu, ale rozsądnie)

### Styl przykładów kodu

#### TypeScript/JavaScript
- Używaj modułów ES (`import`/`export`)
- Przestrzegaj konwencji ścisłego trybu TypeScript
- Uwzględniaj adnotacje typów
- Targetuj ES2022

#### Python
- Przestrzegaj wytycznych stylu PEP 8
- Używaj podpowiedzi typów tam, gdzie to stosowne
- Dodaj docstringi do funkcji i klas
- Korzystaj z nowoczesnych cech Pythona (3.8+)

#### Java
- Przestrzegaj konwencji Spring Boot
- Używaj funkcji Java 21
- Stosuj standardową strukturę projektu Maven
- Dołączaj komentarze Javadoc

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

## Kompilacja i wdrażanie

### Wdrażanie dokumentacji

Repozytorium korzysta z GitHub Pages lub podobnego do hostowania dokumentacji (jeśli dotyczy). Zmiany w gałęzi main wyzwalają:

1. Workflow tłumaczeń (`.github/workflows/co-op-translator.yml`)
2. Automatyczne tłumaczenie wszystkich angielskich plików markdown
3. Lokalizację obrazów w razie potrzeby

### Brak wymaganego procesu budowy

To repozytorium zawiera głównie dokumentację markdown. Nie jest potrzebny krok kompilacji lub budowy dla podstawowej zawartości kursu.

### Wdrażanie przykładowych projektów

Pojedyncze przykładowe projekty mogą mieć instrukcje wdrożenia:
- Zobacz `03-GettingStarted/09-deployment/` dla wskazówek dotyczących wdrażania serwera MCP
- Przykłady wdrożeń Azure Container Apps w `11-MCPServerHandsOnLabs/`

## Zasady współtworzenia

### Proces Pull Request

1. **Fork i klonowanie**: Stwórz fork repozytorium i sklonuj go lokalnie
2. **Stwórz gałąź**: Używaj opisowych nazw gałęzi (np. `fix/typo-module-3`, `add/python-example`)
3. **Wprowadź zmiany**: Edytuj tylko angielskie pliki markdown (nie tłumaczenia)
4. **Testuj lokalnie**: Sprawdź, czy markdown renderuje się poprawnie
5. **Prześlij PR**: Używaj jasnych tytułów i opisów PR
6. **CLA**: Podpisz Microsoft Contributor License Agreement, gdy zostaniesz o to poproszony

### Format tytułu PR

Używaj jasnych, opisowych tytułów:
- `[Module XX] Krótki opis` dla zmian specyficznych dla modułu
- `[Samples] Opis` dla zmian w przykładowym kodzie
- `[Docs] Opis` dla ogólnych aktualizacji dokumentacji

### Co wnosić

- Poprawki błędów w dokumentacji lub przykładach kodu
- Nowe przykłady kodu w dodatkowych językach
- Wyjaśnienia i ulepszenia istniejącej treści
- Nowe studia przypadków lub praktyczne przykłady
- Zgłoszenia problemów z niejasną lub niepoprawną treścią

### Czego NIE robić

- Nie edytuj bezpośrednio plików w katalogu `translations/`
- Nie edytuj katalogu `translated_images/`
- Nie dodawaj dużych plików binarnych bez uzgodnienia
- Nie zmieniaj workflow tłumaczeń bez koordynacji

## Dodatkowe uwagi

### Utrzymanie repozytorium

- **Changelog**: Wszystkie znaczące zmiany są dokumentowane w `changelog.md`
- **Przewodnik nauki**: Używaj `study_guide.md` do przeglądu nawigacji kursu
- **Szablony problemów**: Używaj szablonów GitHub do zgłoszeń błędów i żądań funkcji
- **Kodeks postępowania**: Wszyscy współtwórcy muszą przestrzegać Microsoft Open Source Code of Conduct

### Ścieżka nauki

Postępuj według modułów w kolejności sekwencyjnej (00-11) dla optymalnej nauki:
1. **00-02**: Podstawy (Wprowadzenie, Podstawowe koncepcje, Bezpieczeństwo)
2. **03**: Rozpoczęcie z praktyczną implementacją
3. **04-05**: Praktyczna implementacja i tematy zaawansowane
4. **06-10**: Społeczność, najlepsze praktyki i zastosowania w rzeczywistych projektach
5. **11**: Kompleksowe laboratoria integracji baz danych (13 kolejnych laboratoriów)

### Zasoby wsparcia

- **Dokumentacja**: https://modelcontextprotocol.io/
- **Specyfikacja**: https://spec.modelcontextprotocol.io/
- **Społeczność**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Serwer Microsoft Foundry Discord
- **Powiązane kursy**: Zobacz README.md dla innych ścieżek nauki Microsoft

### Typowe problemy z rozwiązywaniem

**P: Mój PR nie przeszedł sprawdzenia tłumaczeń**
O: Upewnij się, że edytowałeś tylko angielskie pliki markdown w głównych katalogach modułów, a nie wersje tłumaczone.

**P: Jak dodać nowy język?**
O: Obsługa języków jest zarządzana przez workflow co-op-translator. Otwórz problem, aby omówić dodanie nowych języków.

**P: Przykłady kodu nie działają**

A: Upewnij się, że postępowałeś zgodnie z instrukcjami instalacji w pliku README konkretnego przykładu. Sprawdź, czy masz zainstalowane odpowiednie wersje zależności.

**P: Obrazy się nie wyświetlają**
A: Sprawdź, czy ścieżki do obrazów są względne i używają ukośników. Obrazy powinny znajdować się w katalogu `images/` lub `translated_images/` dla wersji przetłumaczonych.

### Uwagi dotyczące wydajności

- Proces tłumaczenia może potrwać kilka minut
- Duże obrazy powinny być zoptymalizowane przed zatwierdzeniem
- Zachowuj pojedyncze pliki markdown skupione i o rozsądnych rozmiarach
- Używaj względnych linków dla lepszej przenośności

### Zarządzanie projektem

Ten projekt stosuje zasady open source Microsoft:
- Licencja MIT dla kodu i dokumentacji
- Microsoft Open Source Code of Conduct
- Wymagana CLA dla wkładów
- Problemy z bezpieczeństwem: Postępuj zgodnie z wytycznymi SECURITY.md
- Wsparcie: Zobacz SUPPORT.md po zasoby pomocy

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->