# AGENTS.md

## Przegląd projektu

**MCP dla początkujących** to otwarty program edukacyjny służący do nauki Model Context Protocol (MCP) – standaryzowanego frameworka dla interakcji pomiędzy modelami AI a aplikacjami klienckimi. To repozytorium zapewnia kompleksowe materiały edukacyjne z praktycznymi przykładami kodu w wielu językach programowania.

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
- **Dokumentacja**: Markdown z automatycznym tłumaczeniem na wiele języków (ponad 48)

### Architektura

- **11 modułów rdzeniowych (00-11)**: Sekwencyjna ścieżka nauki od podstaw do zaawansowanych tematów
- **Praktyczne laboratoria**: Ćwiczenia praktyczne z kompletnym kodem rozwiązań w wielu językach
- **Projekty przykładowe**: Działające implementacje serwera i klienta MCP
- **System tłumaczeń**: Zautomatyzowany workflow GitHub Actions wspierający wiele języków
- **Zasoby graficzne**: Centralne repozytorium obrazów z wersjami przetłumaczonymi

## Komendy konfiguracji

To repozytorium skupia się na dokumentacji. Większość konfiguracji odbywa się w poszczególnych projektach przykładowych i laboratoriach.

### Konfiguracja repozytorium

```bash
# Sklonuj repozytorium
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Praca z projektami przykładowymi

Projekty przykładowe znajdują się w:
- `03-GettingStarted/samples/` - Przykłady specyficzne dla języka
- `03-GettingStarted/01-first-server/solution/` - Implementacje pierwszego serwera
- `03-GettingStarted/02-client/solution/` - Implementacje klienta
- `11-MCPServerHandsOnLabs/` - Rozbudowane laboratoria integracji z bazą danych

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

## Przebieg pracy nad projektem

### Gotowość MCP 7-28

#### Lista kontrolna gotowości repozytorium

- [x] **Jasność dla nowych współtwórców**: Ten plik definiuje cel repozytorium,
  strukturę, zasady współpracy i przykładowe ścieżki konfiguracji.
- [x] **Dokładne komendy budowania/testowania/lintowania i flagi**:
  - Lintowanie dokumentacji w repozytorium:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audyt wzorców linków w dokumentacji:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Walidacja przykładu TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Walidacja przykładu Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Walidacja przykładu Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Jeden realistyczny przebieg pracy mogący stać się narzędziem MCP**:
  `validate_curriculum_change`
- [x] **Wejścia/wyjścia są jawne** (patrz specyfikacja poniżej).
- [x] **Uprawnienia i tryby awaryjne są udokumentowane** (patrz specyfikacja poniżej).
- [x] **Testowalność w CI jest jawna** (deterministyczne komendy, jawne
  kody wyjścia i dane wyjściowe czytelne maszynowo).

#### Proponowany przebieg pracy narzędzia MCP: `validate_curriculum_change`

##### Cel

Zweryfikować zmiany dokumentacji programu nauczania oraz reprezentatywnego kodu przykładowego
pod kątem poprawności przed scaleniem.

##### Wejścia

- `changed_paths: string[]` (wymagane) - zmienione ścieżki względne w PR.
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

- Odczyt plików roboczych i zapis artefaktów generowanych przez narzędzie (np. raporty lint,
  logi testów) tylko; brak zapisu do `translations/` lub
  `translated_images/`.
- Wykonywanie lokalnych poleceń shell.
- Opcjonalny dostęp do sieci tylko do przywracania pakietów (`npm ci`,
  `python -m pip install`, rozwiązywanie zależności `mvn`).
- Brak uprawnień do push, merge lub modyfikacji `translations/` lub
  `translated_images/`.

##### Tryby awaryjne

- `E_NO_INPUT_PATHS`: `changed_paths` puste.
- `E_INVALID_PATH`: ścieżka wejściowa wychodzi poza katalog repozytorium.
- `E_LINT_FAILED`: lintowanie markdown zakończyło się kodem różnym od zera.
- `E_LINK_AUDIT_FAILED`: audyt linków zakończył się błędem (kod różny od zera).
- `E_SAMPLE_TEST_FAILED`: test lub budowanie przykładu zakończyło się błędem.
- `E_TIMEOUT`: polecenie przekroczyło skonfigurowany limit czasu.

##### Zalecany kontrakt CI

Aby zautomatyzować walidację, skonfiguruj zadanie CI, które:

- Uruchamia się na pull requesty dotykające `*.md`, kodu przykładowego lub tego pliku.
- Wykonuje dokładnie powyższe komendy.
- Zapisuje logi jako artefakty.
- Kończy zadanie niepowodzeniem przy dowolnym kodzie wyjścia różnym od zera.

#### Jeśli udostępniasz serwer MCP z tego repo

- [ ] Przeczytaj finalny changelog MCP `2026-07-28`:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Zweryfikuj, że wybrana wersja SDK wspiera MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Usuń założenia dotyczące sesji i handshake; traktuj każde żądanie jako
  samodzielne:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Wysyłaj nagłówki `Mcp-Method` i `Mcp-Name` dla surowych żądań HTTP:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Audytuj na sztywno zakodowane kody błędów (`missing resource` przesunięto z `-32002` na `-32602`).
- [ ] Migruj z przestarzałych Roots, Sampling, Logging oraz Dynamic Client
  Registration:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Porzuć eksperymentalne API z `2025-11-25` Tasks:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Przejrzyj autoryzację pod kątem zabezpieczeń OAuth i OpenID Connect:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Struktura dokumentacji

- **Moduły 00-11**: Główne treści programu nauczania w kolejności sekwencyjnej
- **translations/**: Wersje językowe (generowane automatycznie, nie edytować bezpośrednio)
- **translated_images/**: Zlokalizowane wersje obrazów (generowane automatycznie)
- **images/**: Źródłowe obrazy i diagramy

### Wprowadzanie zmian w dokumentacji

1. Edytuj wyłącznie angielskie pliki markdown w katalogach modułów głównych (00-11)
2. Aktualizuj obrazy w katalogu `images/`, jeśli jest taka potrzeba
3. Akcja co-op-translator na GitHub automatycznie wygeneruje tłumaczenia
4. Tłumaczenia są odtwarzane przy pushu do gałęzi main

### Praca z tłumaczeniami

- **Automatyczne tłumaczenie**: Workflow GitHub Actions zajmuje się wszystkimi tłumaczeniami
- **Nie edytuj ręcznie** plików w katalogu `translations/`
- Metadane tłumaczenia są osadzone w każdym pliku tłumaczonym
- Obsługiwane języki: ponad 48, w tym arabski, chiński, francuski, niemiecki, hindi, japoński, koreański, portugalski, rosyjski, hiszpański i wiele innych

## Instrukcje testowania

### Walidacja dokumentacji

Ponieważ jest to w głównej mierze repozytorium dokumentacji, testowanie skupia się na:

1. **Audyt wzorców linków**: Wylistowanie linków Markdown do przeglądu

   ```bash
   # Wyświetl linki Markdown (wzorzec audytu)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Walidacja przykładów kodu**: Testowanie, czy przykłady kodu kompilują się i działają

   ```bash
   # Przejdź do konkretnego przykładu i uruchom jego testy
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Lintowanie Markdown**: Weryfikacja spójności formatowania

   ```bash
   # Użyj markdownlint, jeśli to konieczne
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testowanie projektów przykładowych

Każdy przykładowy projekt specyficzny dla języka ma własne podejście testowe:

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

## Zasady stylu kodu

### Styl dokumentacji

- Używaj jasnego, przyjaznego początkującym języka
- Zamieszczaj przykłady kodu w wielu językach, tam gdzie to stosowne
- Stosuj najlepsze praktyki w markdown:
  - Używaj nagłówków w stylu ATX (składnia `#`)
  - Używaj bloków kodu z oznaczeniem języka
  - Dodawaj opisowe teksty alternatywne do obrazów
  - Zachowuj rozsądne długości linii (brak ścisłego limitu, ale zachowaj umiar)

### Styl przykładowego kodu

#### TypeScript/JavaScript
- Używaj modułów ES (`import`/`export`)
- Stosuj konwencje ścisłego trybu TypeScript
- Dodawaj adnotacje typów
- Kieruj się do ES2022

#### Python
- Stosuj wytyczne stylu PEP 8
- Używaj wskazówek typów tam, gdzie to stosowne
- Dodawaj docstringi dla funkcji i klas
- Korzystaj z nowoczesnych funkcji wersji Pythona 3.8+

#### Java
- Stosuj konwencje Spring Boot
- Używaj funkcji Java 21
- Stosuj standardową strukturę projektów Maven
- Dodawaj komentarze Javadoc

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

## Budowanie i wdrożenie

### Wdrożenie dokumentacji

Repozytorium wykorzystuje GitHub Pages lub podobne rozwiązanie do hostingu dokumentacji (jeśli dotyczy). Zmiany w gałęzi main wywołują:

1. Workflow tłumaczeń (`.github/workflows/co-op-translator.yml`)
2. Automatyczne tłumaczenie wszystkich angielskich plików markdown
3. Lokalizację obrazów według potrzeby

### Brak procesu budowania

To repozytorium zawiera głównie dokumentację w markdown. Nie jest konieczna kompilacja ani krok budowania dla głównej treści programu nauczania.

### Wdrożenie projektów przykładowych

Poszczególne projekty przykładowe mogą mieć instrukcje wdrożenia:
- Zobacz `03-GettingStarted/09-deployment/` dla wskazówek wdrożenia serwera MCP
- Przykłady wdrożenia Azure Container Apps w `11-MCPServerHandsOnLabs/`

## Zasady współpracy

### Proces Pull Request

1. **Fork i klonowanie**: Utwórz fork repozytorium i sklonuj go lokalnie
2. **Utwórz gałąź**: Używaj opisowych nazw gałęzi (np. `fix/typo-module-3`, `add/python-example`)
3. **Wprowadź zmiany**: Edytuj tylko angielskie pliki markdown (nie tłumaczenia)
4. **Testuj lokalnie**: Zweryfikuj poprawność renderowania markdown
5. **Wyślij PR**: Używaj jasnych tytułów i opisów PR
6. **CLA**: Podpisz Microsoft Contributor License Agreement, gdy zostaniesz poproszony

### Format tytułu PR

Używaj jasnych, opisowych tytułów:
- `[Module XX] Krótki opis` dla zmian specyficznych dla modułu
- `[Samples] Opis` dla zmian w kodzie przykładowym
- `[Docs] Opis` dla ogólnych aktualizacji dokumentacji

### Co można wnosić

- Poprawki błędów w dokumentacji lub przykładach kodu
- Nowe przykłady kodu w dodatkowych językach
- Wyjaśnienia i ulepszenia istniejących treści
- Nowe studia przypadków lub przykłady praktyczne
- Zgłoszenia problemów dotyczących niejasnych lub błędnych treści

### Czego unikać

- Nie edytuj bezpośrednio plików w katalogu `translations/`
- Nie edytuj katalogu `translated_images/`
- Nie dodawaj dużych plików binarnych bez konsultacji
- Nie zmieniaj plików workflow tłumaczeń bez koordynacji

## Dodatkowe uwagi

### Utrzymanie repozytorium

- **Changelog**: Wszystkie znaczące zmiany są dokumentowane w `changelog.md`
- **Przewodnik nauki**: Używaj `study_guide.md` do ogólnego przeglądu programu nauczania
- **Szablony zgłoszeń**: Używaj szablonów GitHub do zgłoszeń błędów i próśb o funkcje
- **Kodeks postępowania**: Wszyscy współtwórcy muszą przestrzegać Microsoft Open Source Code of Conduct

### Ścieżka nauki

Przechodź przez moduły w kolejności sekwencyjnej (00-11) dla optymalnej nauki:
1. **00-02**: Podstawy (Wprowadzenie, podstawowe koncepcje, bezpieczeństwo)
2. **03**: Pierwsze kroki z praktyczną implementacją
3. **04-05**: Praktyczna implementacja i tematy zaawansowane
4. **06-10**: Społeczność, najlepsze praktyki i zastosowania w świecie rzeczywistym
5. **11**: Rozbudowane laboratoria integracji z bazą danych (13 laboratoriów sekwencyjnych)

### Zasoby wsparcia

- **Dokumentacja**: https://modelcontextprotocol.io/
- **Specyfikacja**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Społeczność**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Serwer Microsoft Foundry Discord
- **Powiązane kursy**: Zobacz README.md innych ścieżek edukacyjnych Microsoft

### Typowe rozwiązania problemów

**P: Mój PR nie przechodzi testu tłumaczenia**
O: Upewnij się, że edytowałeś tylko angielskie pliki markdown w katalogach modułów głównych, nie wersje tłumaczone.

**P: Jak dodać nowy język?**
O: Wsparcie językowe zarządzane jest przez workflow co-op-translator. Otwórz issue, aby omówić dodanie nowych języków.

**P: Przykłady kodu nie działają**
O: Upewnij się, że wykonałeś instrukcje konfiguracji w README konkretnego przykładu. Sprawdź, czy masz zainstalowane odpowiednie wersje zależności.

**P: Obrazy się nie wyświetlają**

A: Sprawdź, czy ścieżki do obrazów są względne i używają ukośników. Obrazy powinny znajdować się w katalogu `images/` lub `translated_images/` dla wersji lokalizowanych.

### Rozważania dotyczące wydajności

- Proces tłumaczenia może potrwać kilka minut
- Duże obrazy powinny być zoptymalizowane przed zatwierdzeniem
- Zachowaj pojedyncze pliki markdown skoncentrowane i o rozsądnym rozmiarze
- Używaj linków względnych dla lepszej przenośności

### Zarządzanie projektem

Ten projekt stosuje się do praktyk open source Microsoft:
- Licencja MIT dla kodu i dokumentacji
- Microsoft Open Source Code of Conduct
- Wymagana jest CLA dla wkładów
- Problemy z bezpieczeństwem: Postępuj zgodnie z wytycznymi SECURITY.md
- Wsparcie: Zobacz SUPPORT.md, aby uzyskać zasoby pomocy

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->