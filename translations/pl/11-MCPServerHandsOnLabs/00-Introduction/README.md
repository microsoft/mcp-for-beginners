# Wprowadzenie do integracji bazy danych MCP

## 🎯 Co obejmuje ten lab

Ten wprowadzający lab oferuje kompleksowy przegląd budowy serwerów Model Context Protocol (MCP) z integracją bazy danych. Zrozumiesz przypadek biznesowy, architekturę techniczną oraz zastosowania w rzeczywistych scenariuszach na przykładzie analityki Zava Retail dostępnej pod adresem https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Przegląd

**Model Context Protocol (MCP)** umożliwia asystentom AI bezpieczny dostęp do zewnętrznych źródeł danych i interakcję z nimi w czasie rzeczywistym. W połączeniu z integracją bazy danych MCP odblokowuje potężne możliwości dla aplikacji AI opartych na danych.

Ten ścieżka nauki nauczy Cię budować gotowe do produkcji serwery MCP, które łączą asystentów AI z danymi sprzedaży detalicznej za pomocą PostgreSQL, implementując wzorce korporacyjne, takie jak bezpieczeństwo na poziomie wiersza (Row Level Security), wyszukiwanie semantyczne i dostęp do danych dla wielu najemców.

## Cele nauki

Po ukończeniu tego labu będziesz w stanie:

- **Zdefiniować** Model Context Protocol i jego kluczowe korzyści dla integracji bazy danych
- **Zidentyfikować** kluczowe komponenty architektury serwera MCP z bazami danych
- **Zrozumieć** przypadek użycia Zava Retail i jego wymagania biznesowe
- **Rozpoznać** wzorce korporacyjne dla bezpiecznego i skalowalnego dostępu do bazy danych
- **Wymienić** narzędzia i technologie używane w tej ścieżce nauki

## 🧭 Wyzwanie: AI spotyka dane z rzeczywistego świata

### Ograniczenia tradycyjnej AI

Nowoczesne asystenty AI są niezwykle potężne, ale napotykają istotne ograniczenia podczas pracy z rzeczywistymi danymi biznesowymi:

| **Wyzwanie**         | **Opis**                                   | **Wpływ na biznes**               |
|-----------------------|-------------------------------------------|------------------------------------|
| **Statyczna wiedza**  | Modele AI trenowane na stałych zbiorach danych nie mają dostępu do aktualnych danych biznesowych | Nieaktualne wnioski, stracone szanse |
| **Silosy danych**     | Informacje zamknięte w bazach danych, API i systemach, do których AI nie ma dostępu | Niekompletna analiza, rozdrobnione procesy |
| **Ograniczenia bezpieczeństwa** | Bezpośredni dostęp do bazy danych rodzi obawy dotyczące bezpieczeństwa i zgodności | Ograniczone wdrożenie, ręczne przygotowanie danych |
| **Złożone zapytania** | Użytkownicy biznesowi potrzebują wiedzy technicznej, aby uzyskać wgląd w dane | Zmniejszona adopcja, nieefektywne procesy |

### Rozwiązanie MCP

Model Context Protocol rozwiązuje te wyzwania, oferując:

- **Dostęp do danych w czasie rzeczywistym**: Asystenty AI mogą zapytaniać na żywo bazy danych i API
- **Bezpieczną integrację**: Kontrolowany dostęp z uwierzytelnianiem i uprawnieniami
- **Interfejs w języku naturalnym**: Użytkownicy biznesowi zadają pytania w prostym języku
- **Standaryzowany protokół**: Działa na różnych platformach i narzędziach AI

## 🏪 Poznaj Zava Retail: Nasze studium przypadku https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

W trakcie tej ścieżki nauki zbudujemy serwer MCP dla **Zava Retail**, fikcyjnej sieci sklepów DIY z wieloma lokalizacjami. Ten realistyczny scenariusz pokazuje implementację MCP na poziomie korporacyjnym.

### Kontekst biznesowy

**Zava Retail** prowadzi:
- **8 sklepów stacjonarnych** w stanie Waszyngton (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 sklep internetowy** dla sprzedaży e-commerce
- **Zróżnicowany katalog produktów** obejmujący narzędzia, sprzęt, artykuły ogrodowe i materiały budowlane
- **Wielopoziomowe zarządzanie** z kierownikami sklepów, menedżerami regionalnymi i kadrą zarządzającą

### Wymagania biznesowe

Kierownicy sklepów i kadra zarządzająca potrzebują analityki wspieranej przez AI, aby:

1. **Analizować wyniki sprzedaży** w różnych sklepach i okresach
2. **Śledzić poziomy zapasów** i identyfikować potrzeby w zakresie uzupełniania
3. **Zrozumieć zachowania klientów** i wzorce zakupowe
4. **Odkrywać informacje o produktach** za pomocą wyszukiwania semantycznego
5. **Generować raporty** za pomocą zapytań w języku naturalnym
6. **Zachować bezpieczeństwo danych** dzięki kontroli dostępu opartej na rolach

### Wymagania techniczne

Serwer MCP musi zapewniać:

- **Dostęp do danych dla wielu najemców**, gdzie kierownicy sklepów widzą tylko dane swojego sklepu
- **Elastyczne zapytania** wspierające złożone operacje SQL
- **Wyszukiwanie semantyczne** dla odkrywania produktów i rekomendacji
- **Dane w czasie rzeczywistym** odzwierciedlające aktualny stan biznesu
- **Bezpieczne uwierzytelnianie** z bezpieczeństwem na poziomie wiersza
- **Skalowalną architekturę** obsługującą wielu użytkowników jednocześnie

## 🏗️ Przegląd architektury serwera MCP

Nasz serwer MCP implementuje warstwową architekturę zoptymalizowaną pod kątem integracji bazy danych:

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
- **Rejestracja narzędzi**: Deklaratywne definicje narzędzi z bezpieczeństwem typów
- **Kontekst zapytań**: Zarządzanie tożsamością użytkownika i sesją
- **Obsługa błędów**: Solidne zarządzanie błędami i logowanie

#### **2. Warstwa integracji bazy danych**
- **Pula połączeń**: Efektywne zarządzanie połączeniami asyncpg
- **Dostawca schematów**: Dynamiczne odkrywanie schematów tabel
- **Wykonawca zapytań**: Bezpieczne wykonywanie SQL z kontekstem RLS
- **Zarządzanie transakcjami**: Zgodność z ACID i obsługa wycofań

#### **3. Warstwa bezpieczeństwa**
- **Bezpieczeństwo na poziomie wiersza**: PostgreSQL RLS dla izolacji danych wielu najemców
- **Tożsamość użytkownika**: Uwierzytelnianie i autoryzacja kierowników sklepów
- **Kontrola dostępu**: Drobnoziarniste uprawnienia i ślady audytowe
- **Walidacja danych wejściowych**: Zapobieganie SQL injection i walidacja zapytań

#### **4. Warstwa ulepszeń AI**
- **Wyszukiwanie semantyczne**: Wektory osadzeń dla odkrywania produktów
- **Integracja Azure OpenAI**: Generowanie osadzeń tekstowych
- **Algorytmy podobieństwa**: Wyszukiwanie podobieństwa kosinusowego pgvector
- **Optymalizacja wyszukiwania**: Indeksowanie i dostrajanie wydajności

## 🔧 Stos technologiczny

### Kluczowe technologie

| **Komponent**         | **Technologia**            | **Cel**                          |
|------------------------|----------------------------|-----------------------------------|
| **Framework MCP**      | FastMCP (Python)          | Nowoczesna implementacja serwera MCP |
| **Baza danych**        | PostgreSQL 17 + pgvector  | Relacyjne dane z wyszukiwaniem wektorowym |
| **Usługi AI**          | Azure OpenAI              | Osadzenia tekstowe i modele językowe |
| **Konteneryzacja**     | Docker + Docker Compose   | Środowisko deweloperskie         |
| **Platforma chmurowa** | Microsoft Azure           | Wdrożenie produkcyjne            |
| **Integracja IDE**     | VS Code                   | Chat AI i przepływ pracy deweloperskiej |

### Narzędzia deweloperskie

| **Narzędzie**          | **Cel**                   |
|------------------------|---------------------------|
| **asyncpg**            | Wydajny sterownik PostgreSQL |
| **Pydantic**           | Walidacja danych i serializacja |
| **Azure SDK**          | Integracja usług chmurowych |
| **pytest**             | Framework testowy         |
| **Docker**             | Konteneryzacja i wdrożenie |

### Stos produkcyjny

| **Usługa**             | **Zasób Azure**           | **Cel**                          |
|------------------------|---------------------------|-----------------------------------|
| **Baza danych**        | Azure Database for PostgreSQL | Zarządzana usługa bazy danych   |
| **Kontener**           | Azure Container Apps      | Hosting kontenerów bezserwerowych |
| **Usługi AI**          | Azure AI Foundry          | Modele OpenAI i punkty końcowe   |
| **Monitorowanie**      | Application Insights      | Obserwowalność i diagnostyka     |
| **Bezpieczeństwo**     | Azure Key Vault           | Zarządzanie sekretami i konfiguracją |

## 🎬 Scenariusze użycia w rzeczywistości

Przyjrzyjmy się, jak różni użytkownicy korzystają z naszego serwera MCP:

### Scenariusz 1: Przegląd wyników kierownika sklepu

**Użytkownik**: Sarah, kierownik sklepu w Seattle  
**Cel**: Analiza wyników sprzedaży za ostatni kwartał

**Zapytanie w języku naturalnym**:
> "Pokaż mi 10 najlepszych produktów pod względem przychodów dla mojego sklepu w Q4 2024"

**Co się dzieje**:
1. Chat AI w VS Code wysyła zapytanie do serwera MCP
2. Serwer MCP identyfikuje kontekst sklepu Sarah (Seattle)
3. Polityki RLS filtrują dane tylko dla sklepu w Seattle
4. Generowane i wykonywane jest zapytanie SQL
5. Wyniki są formatowane i zwracane do Chat AI
6. AI dostarcza analizę i wnioski

### Scenariusz 2: Odkrywanie produktów za pomocą wyszukiwania semantycznego

**Użytkownik**: Mike, kierownik ds. zapasów  
**Cel**: Znalezienie produktów podobnych do zapytania klienta

**Zapytanie w języku naturalnym**:
> "Jakie produkty sprzedajemy, które są podobne do 'wodoodpornych złączy elektrycznych do użytku na zewnątrz'?"

**Co się dzieje**:
1. Zapytanie jest przetwarzane przez narzędzie wyszukiwania semantycznego
2. Azure OpenAI generuje wektor osadzenia
3. pgvector wykonuje wyszukiwanie podobieństwa
4. Powiązane produkty są klasyfikowane według trafności
5. Wyniki zawierają szczegóły produktów i dostępność
6. AI sugeruje alternatywy i możliwości pakowania

### Scenariusz 3: Analiza między sklepami

**Użytkownik**: Jennifer, menedżer regionalny  
**Cel**: Porównanie wyników w różnych sklepach

**Zapytanie w języku naturalnym**:
> "Porównaj sprzedaż według kategorii dla wszystkich sklepów w ciągu ostatnich 6 miesięcy"

**Co się dzieje**:
1. Kontekst RLS ustawiony dla dostępu menedżera regionalnego
2. Generowane jest złożone zapytanie dla wielu sklepów
3. Dane są agregowane w różnych lokalizacjach sklepów
4. Wyniki zawierają trendy i porównania
5. AI identyfikuje wnioski i rekomendacje

## 🔒 Szczegółowe omówienie bezpieczeństwa i wielonajemności

Nasza implementacja priorytetowo traktuje bezpieczeństwo na poziomie korporacyjnym:

### Bezpieczeństwo na poziomie wiersza (RLS)

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
- **ID kierownika sklepu**: Unikalny identyfikator dla kontekstu RLS
- **Przypisanie roli**: Uprawnienia i poziomy dostępu
- **Zarządzanie sesją**: Bezpieczne tokeny uwierzytelniające
- **Logowanie audytowe**: Pełna historia dostępu

### Ochrona danych

Wiele warstw bezpieczeństwa:
- **Szyfrowanie połączeń**: TLS dla wszystkich połączeń z bazą danych
- **Zapobieganie SQL injection**: Tylko zapytania z parametrami
- **Walidacja danych wejściowych**: Kompleksowa walidacja zapytań
- **Obsługa błędów**: Brak wrażliwych danych w komunikatach o błędach

## 🎯 Kluczowe wnioski

Po ukończeniu tego wprowadzenia powinieneś zrozumieć:

✅ **Wartość MCP**: Jak MCP łączy asystenty AI z danymi rzeczywistymi  
✅ **Kontekst biznesowy**: Wymagania i wyzwania Zava Retail  
✅ **Przegląd architektury**: Kluczowe komponenty i ich interakcje  
✅ **Stos technologiczny**: Narzędzia i frameworki używane w całym procesie  
✅ **Model bezpieczeństwa**: Dostęp do danych dla wielu najemców i ich ochrona  
✅ **Wzorce użycia**: Scenariusze zapytań i przepływy pracy w rzeczywistości  

## 🚀 Co dalej

Gotowy na głębsze zanurzenie? Kontynuuj z:

**[Lab 01: Podstawowe koncepcje architektury](../01-Architecture/README.md)**

Dowiedz się o wzorcach architektury serwera MCP, zasadach projektowania baz danych i szczegółowej implementacji technicznej, która napędza nasze rozwiązanie analityki detalicznej.

## 📚 Dodatkowe zasoby

### Dokumentacja MCP
- [Specyfikacja MCP](https://modelcontextprotocol.io/docs/) - Oficjalna dokumentacja protokołu
- [MCP dla początkujących](https://aka.ms/mcp-for-beginners) - Kompleksowy przewodnik po MCP
- [Dokumentacja FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Dokumentacja SDK dla Pythona

### Integracja bazy danych
- [Dokumentacja PostgreSQL](https://www.postgresql.org/docs/) - Kompletny przewodnik po PostgreSQL
- [Przewodnik pgvector](https://github.com/pgvector/pgvector) - Dokumentacja rozszerzenia wektorowego
- [Bezpieczeństwo na poziomie wiersza](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Przewodnik po RLS w PostgreSQL

### Usługi Azure
- [Dokumentacja Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integracja usług AI
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Zarządzana usługa bazy danych
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Kontenery bezserwerowe

---

**Zastrzeżenie**: To ćwiczenie edukacyjne wykorzystujące fikcyjne dane detaliczne. Zawsze przestrzegaj polityk zarządzania danymi i bezpieczeństwa swojej organizacji podczas wdrażania podobnych rozwiązań w środowiskach produkcyjnych.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.