# Wprowadzenie do integracji bazy danych MCP

> [!NOTE]
> Diagramy lub kod w tej ścieżce nauki, które wykorzystują HTTP/SSE lub opcje inicjalizacji,
> odzwierciedlają zależności MCP `2025-11-25` w przykładowym rozwiązaniu. Dla nowych
> implementacji używaj bezstanowych żądań `2026-07-28` i strumieniowego HTTP.

## 🎯 Co obejmuje to laboratorium

To wprowadzenie zapewnia kompleksowy przegląd tworzenia serwerów Model Context Protocol (MCP) z integracją bazy danych. Zrozumiesz przypadek biznesowy, architekturę techniczną oraz rzeczywiste zastosowania poprzez studium przypadku analiz Zava Retail dostępne pod https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Przegląd

**Model Context Protocol (MCP)** umożliwia asystentom AI bezpieczny dostęp i interakcję z zewnętrznymi źródłami danych w czasie rzeczywistym. Połączony z integracją bazy danych, MCP otwiera potężne możliwości dla aplikacji AI opartych na danych.

Ta ścieżka nauki nauczy Cię tworzyć serwery MCP gotowe do produkcji, które łączą asystentów AI z danymi sprzedaży detalicznej za pomocą PostgreSQL, implementując wzorce korporacyjne takie jak zabezpieczenie na poziomie wiersza, wyszukiwanie semantyczne i dostęp do danych wielo-najemców.

## Cele nauki

Po zakończeniu tego laboratorium będziesz potrafił:

- **Zdefiniować** Model Context Protocol i jego kluczowe zalety dla integracji z bazą danych
- **Zidentyfikować** kluczowe komponenty architektury serwera MCP z bazami danych
- **Zrozumieć** studium przypadku Zava Retail i jego wymagania biznesowe
- **Rozpoznać** wzorce korporacyjne dla bezpiecznego i skalowalnego dostępu do bazy danych
- **Wypisać** narzędzia i technologie wykorzystywane w tej ścieżce nauki

## 🧭 Wyzwanie: AI spotyka dane ze świata rzeczywistego

### Tradycyjne ograniczenia AI

Nowoczesne asystenty AI są niesamowicie potężne, ale napotykają znaczące ograniczenia podczas pracy z rzeczywistymi danymi biznesowymi:

| **Wyzwanie** | **Opis** | **Wpływ na biznes** |
|---------------|-----------------|-------------------|
| **Statyczna wiedza** | Modele AI trenowane na stałych zestawach danych nie mają dostępu do aktualnych danych biznesowych | Przestarzałe wnioski, utracone okazje |
| **Silosy danych** | Informacje zamknięte w bazach danych, interfejsach API i systemach niedostępnych dla AI | Niekompletna analiza, fragmentaryczne procesy |
| **Ograniczenia bezpieczeństwa** | Bezpośredni dostęp do bazy danych rodzi problemy z bezpieczeństwem i zgodnością | Ograniczone wdrożenia, ręczne przygotowanie danych |
| **Złożone zapytania** | Użytkownicy biznesowi potrzebują wiedzy technicznej do wydobywania danych | Mniejsze wykorzystanie, nieefektywne procesy |

### Rozwiązanie MCP

Model Context Protocol rozwiązuje te wyzwania poprzez:

- **Dostęp w czasie rzeczywistym**: Asystenci AI zadają zapytania do żywych baz danych i API
- **Bezpieczną integrację**: Kontrolowany dostęp z uwierzytelnianiem i uprawnieniami
- **Interfejs w języku naturalnym**: Użytkownicy biznesowi zadają pytania w prostym angielskim
- **Standardowy protokół**: Działa na różnych platformach i narzędziach AI

## 🏪 Poznaj Zava Retail: Nasze studium przypadku https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

W trakcie tej ścieżki nauki zbudujemy serwer MCP dla **Zava Retail**, fikcyjnej sieci sklepów DIY z wieloma lokalizacjami. Ten realistyczny scenariusz demonstruje wdrożenie MCP na poziomie korporacyjnym.

### Kontekst biznesowy

**Zava Retail** prowadzi:
- **8 fizycznych sklepów** w stanie Waszyngton (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 sklep internetowy** dla sprzedaży e-commerce
- **Różnorodny katalog produktów** obejmujący narzędzia, sprzęt, artykuły ogrodowe i materiały budowlane
- **Wielopoziomowe zarządzanie** z kierownikami sklepów, menedżerami regionalnymi i kadrą kierowniczą

### Wymagania biznesowe

Kierownicy sklepów i kadra zarządzająca potrzebują analityki wspomaganej AI, aby:

1. **Analizować wyniki sprzedaży** w sklepach i okresach czasowych
2. **Monitorować stany magazynowe** i identyfikować potrzeby uzupełnienia
3. **Rozumieć zachowania klientów** i wzorce zakupowe
4. **Odkrywać informacje o produktach** za pomocą wyszukiwania semantycznego
5. **Generować raporty** za pomocą zapytań w języku naturalnym
6. **Utrzymywać bezpieczeństwo danych** z kontrolą dostępu opartą na rolach

### Wymagania techniczne

Serwer MCP musi zapewniać:

- **Dostęp do danych wielo-najemców**, gdzie kierownicy sklepów widzą tylko dane swojego sklepu
- **Elastyczne zapytania** obsługujące złożone operacje SQL
- **Wyszukiwanie semantyczne** dla odkrywania produktów i rekomendacji
- **Dane w czasie rzeczywistym** odzwierciedlające aktualny stan biznesu
- **Bezpieczne uwierzytelnianie** z zabezpieczeniem na poziomie wiersza
- **Skalowalna architektura** wspierająca wielu równoczesnych użytkowników

## 🏗️ Ogólny przegląd architektury serwera MCP

Nasz serwer MCP implementuje warstwową architekturę zoptymalizowaną pod integrację z bazą danych:

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### Kluczowe komponenty

#### **1. Warstwa serwera MCP**
- **FastMCP Framework**: Nowoczesna implementacja serwera MCP w Pythonie
- **Rejestracja narzędzi**: Deklaratywna definicja narzędzi z bezpieczeństwem typów
- **Kontekst żądania**: Tożsamość użytkownika i zarządzanie sesją
- **Obsługa błędów**: Solidne zarządzanie błędami i rejestrowanie

#### **2. Warstwa integracji z bazą danych**
- **Puli połączeń**: Efektywne zarządzanie połączeniami asyncpg
- **Dostawca schematów**: Dynamiczne odkrywanie schematów tabel
- **Wykonawca zapytań**: Bezpieczne wykonywanie SQL z kontekstem RLS
- **Zarządzanie transakcjami**: Zgodność ACID i obsługa rollback

#### **3. Warstwa bezpieczeństwa**
- **Zabezpieczenie na poziomie wiersza (RLS)**: PostgreSQL RLS do izolacji danych wielo-najemców
- **Tożsamość użytkownika**: Uwierzytelnianie i autoryzacja kierowników sklepów
- **Kontrola dostępu**: Szczegółowe uprawnienia i ścieżki audytu
- **Walidacja danych wejściowych**: Zapobieganie SQL injection i weryfikacja zapytań

#### **4. Warstwa ulepszeń AI**
- **Wyszukiwanie semantyczne**: Wektory osadzeń do odkrywania produktów
- **Integracja Azure OpenAI**: Generowanie osadzeń tekstowych
- **Algorytmy podobieństwa**: Wyszukiwanie podobieństwa kosinusowego pgvector
- **Optymalizacja wyszukiwania**: Indeksowanie i tuning wydajności

## 🔧 Stos technologiczny

### Podstawowe technologie

| **Komponent** | **Technologia** | **Cel** |
|---------------|----------------|-------------|
| **Framework MCP** | FastMCP (Python) | Nowoczesna implementacja serwera MCP |
| **Baza danych** | PostgreSQL 17 + pgvector | Dane relacyjne z wyszukiwaniem wektorowym |
| **Usługi AI** | Azure OpenAI | Osadzenia tekstowe i modele językowe |
| **Kontejnerizacja** | Docker + Docker Compose | Środowisko deweloperskie |
| **Platforma chmurowa** | Microsoft Azure | Wdrożenie produkcyjne |
| **Integracja IDE** | VS Code | Czaty AI i workflow deweloperski |

### Narzędzia deweloperskie

| **Narzędzie** | **Cel** |
|----------|-------------|
| **asyncpg** | Wysokowydajny sterownik PostgreSQL |
| **Pydantic** | Walidacja i serializacja danych |
| **Azure SDK** | Integracja usług chmurowych |
| **pytest** | Framework testowy |
| **Docker** | Kontejneryzacja i wdrożenia |

### Stos produkcyjny

| **Usługa** | **Zasób Azure** | **Cel** |
|-------------|-------------------|-------------|
| **Baza danych** | Azure Database for PostgreSQL | Zarządzana usługa bazy danych |
| **Kontejner** | Azure Container Apps | Hostowanie bezserwerowe kontenerów |
| **Usługi AI** | Microsoft Foundry | Modele i punkty końcowe OpenAI |
| **Monitoring** | Application Insights | Obserwowalność i diagnostyka |
| **Bezpieczeństwo** | Azure Key Vault | Zarządzanie sekretami i konfiguracją |

## 🎬 Scenariusze użycia w rzeczywistym świecie

Przyjrzyjmy się, jak różni użytkownicy współdziałają z naszym serwerem MCP:

### Scenariusz 1: Przegląd wyników kierownika sklepu

**Użytkownik**: Sarah, kierownik sklepu w Seattle  
**Cel**: Analiza wyników sprzedaży za ostatni kwartał

**Zapytanie w języku naturalnym**:
> „Pokaż mi 10 najlepszych produktów według przychodu dla mojego sklepu w IV kwartale 2024”

**Co się dzieje**:
1. VS Code AI Chat wysyła zapytanie do serwera MCP
2. Serwer MCP identyfikuje kontekst sklepu Sarah (Seattle)
3. Polityki RLS filtrują dane tylko do sklepu w Seattle
4. Generowane i wykonywane jest zapytanie SQL
5. Wyniki są formatowane i zwracane do AI Chat
6. AI dostarcza analizę i wnioski

### Scenariusz 2: Odkrywanie produktów za pomocą wyszukiwania semantycznego

**Użytkownik**: Mike, kierownik magazynu  
**Cel**: Znaleźć produkty podobne do zapytania klienta

**Zapytanie w języku naturalnym**:
> „Jakie produkty sprzedajemy, które są podobne do 'wodoszczelnych złączy elektrycznych do użytku na zewnątrz'?”

**Co się dzieje**:
1. Zapytanie przetwarzane przez narzędzie wyszukiwania semantycznego
2. Azure OpenAI generuje wektor osadzenia
3. pgvector wykonuje wyszukiwanie podobieństwa
4. Powiązane produkty są oceniane pod względem trafności
5. Wyniki zawierają szczegóły produktów i dostępność
6. AI sugeruje alternatywy i możliwości bundlingu

### Scenariusz 3: Analiza między sklepami

**Użytkownik**: Jennifer, menedżer regionalny  
**Cel**: Porównać wyniki we wszystkich sklepach

**Zapytanie w języku naturalnym**:
> „Porównaj sprzedaż według kategorii dla wszystkich sklepów w ciągu ostatnich 6 miesięcy”

**Co się dzieje**:
1. Ustawiony jest kontekst RLS dla dostępu menedżera regionalnego
2. Generowane jest złożone zapytanie wielosklepowe
3. Dane są agregowane ze wszystkich lokalizacji sklepów
4. Wyniki zawierają trendy i porównania
5. AI identyfikuje wnioski i rekomendacje

## 🔒 Szczegółowy przegląd bezpieczeństwa i wielonarodowości

Nasza implementacja priorytetowo traktuje bezpieczeństwo klasy korporacyjnej:

### Zabezpieczenie na poziomie wiersza (RLS)

PostgreSQL RLS zapewnia izolację danych:

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### Zarządzanie tożsamością użytkownika

Każde połączenie MCP zawiera:
- **ID kierownika sklepu**: Unikalny identyfikator kontekstu RLS
- **Przydział roli**: Uprawnienia i poziomy dostępu
- **Zarządzanie sesją**: Bezpieczne tokeny uwierzytelniania
- **Rejestrowanie audytu**: Pełna historia dostępu

### Ochrona danych

Wielowarstwowe bezpieczeństwo:
- **Szyfrowanie połączenia**: TLS dla wszystkich połączeń z bazą
- **Zapobieganie SQL injection**: Tylko parametryzowane zapytania
- **Walidacja danych wejściowych**: Kompleksowa weryfikacja żądań
- **Obsługa błędów**: Brak wrażliwych danych w komunikatach o błędach

## 🎯 Kluczowe wnioski

Po ukończeniu tego wprowadzenia powinieneś rozumieć:

✅ **Wartość MCP**: Jak MCP łączy asystentów AI ze światem rzeczywistych danych  
✅ **Kontekst biznesowy**: Wymagania i wyzwania Zava Retail  
✅ **Przegląd architektury**: Kluczowe komponenty i ich interakcje  
✅ **Stos technologiczny**: Narzędzia i frameworki używane w całej ścieżce  
✅ **Model bezpieczeństwa**: Wielonarodowy dostęp do danych i ich ochrona  
✅ **Wzorce użycia**: Scenariusze zapytań i workflow z życia  

## 🚀 Co dalej

Gotowy na dalszą naukę? Kontynuuj z:

**[Laboratorium 01: Podstawowe koncepcje architektury](../01-Architecture/README.md)**

Poznaj wzorce architektury serwera MCP, zasady projektowania baz danych oraz szczegółową implementację techniczną, która napędza nasze rozwiązanie analityki detalicznej.

## 📚 Dodatkowe zasoby

### Dokumentacja MCP
- [Specyfikacja MCP](https://modelcontextprotocol.io/docs/) - Oficjalna dokumentacja protokołu
- [MCP dla początkujących](https://aka.ms/mcp-for-beginners) - Kompleksowy przewodnik nauki MCP
- [Dokumentacja FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Dokumentacja SDK Pythona

### Integracja z bazą danych
- [Dokumentacja PostgreSQL](https://www.postgresql.org/docs/) - Kompletny podręcznik PostgreSQL
- [Przewodnik pgvector](https://github.com/pgvector/pgvector) - Dokumentacja rozszerzenia wektorowego
- [Zabezpieczenie na poziomie wiersza](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Przewodnik PostgreSQL RLS

### Usługi Azure
- [Dokumentacja Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integracja usług AI
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Zarządzana usługa bazy danych
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Kontenery bezserwerowe

---

**Zastrzeżenie**: To jest ćwiczenie edukacyjne wykorzystujące fikcyjne dane detaliczne. Zawsze przestrzegaj polityk bezpieczeństwa i zarządzania danymi w swojej organizacji podczas wdrażania podobnych rozwiązań w środowiskach produkcyjnych.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->