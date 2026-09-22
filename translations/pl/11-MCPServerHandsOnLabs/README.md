# 🚀 Serwer MCP z PostgreSQL - Kompletny przewodnik po nauce

## 🧠 Przegląd ścieżki nauki integracji bazy danych MCP

Ten kompleksowy przewodnik po nauce nauczy Cię, jak zbudować produkcyjnie gotowe **serwery Model Context Protocol (MCP)** integrujące się z bazami danych poprzez praktyczną implementację analityki detalicznej. Poznasz wzorce na poziomie przedsiębiorstwa, w tym **Row Level Security (RLS)**, **semantyczne wyszukiwanie**, **integrację Azure AI** oraz **wielowarstwowy dostęp do danych**.

Niezależnie od tego, czy jesteś programistą backendu, inżynierem AI czy architektem danych, ten przewodnik zapewnia uporządkowaną naukę z przykładami z życia i praktycznymi ćwiczeniami, które przeprowadzą Cię przez następujący serwer MCP https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Oficjalne zasoby MCP

- 📘 [Dokumentacja MCP](https://modelcontextprotocol.io/) – Szczegółowe samouczki i przewodniki użytkownika
- 📜 [Specyfikacja MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Architektura protokołu i odniesienia techniczne
- 🧑‍💻 [Repozytorium MCP na GitHub](https://github.com/modelcontextprotocol) – Open-source SDK, narzędzia i przykłady kodu
- 🌐 [Społeczność MCP](https://github.com/orgs/modelcontextprotocol/discussions) – Dołącz do dyskusji i dołóż się do społeczności
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Najlepsze praktyki bezpieczeństwa i minimalizacja ryzyka


## 🧭 Ścieżka nauki integracji bazy danych MCP

### 📚 Pełna struktura nauki dla https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Lab | Temat | Opis | Link |
|--------|-------|-------------|------|
| **Lab 1-3: Podstawy** | | | |
| 00 | [Wprowadzenie do integracji bazy danych MCP](./00-Introduction/README.md) | Przegląd MCP z integracją baz danych i zastosowaniem analityki detalicznej | [Rozpocznij tutaj](./00-Introduction/README.md) |
| 01 | [Podstawowe koncepcje architektury](./01-Architecture/README.md) | Zrozumienie architektury serwera MCP, warstw bazy danych i wzorców bezpieczeństwa | [Ucz się](./01-Architecture/README.md) |
| 02 | [Bezpieczeństwo i wielowarstwowość](./02-Security/README.md) | Row Level Security, uwierzytelnianie i dostęp do danych wielowarstwowych | [Ucz się](./02-Security/README.md) |
| 03 | [Konfiguracja środowiska](./03-Setup/README.md) | Konfiguracja środowiska deweloperskiego, Docker, zasoby Azure | [Konfiguruj](./03-Setup/README.md) |
| **Lab 4-6: Budowanie serwera MCP** | | | |
| 04 | [Projekt i schemat bazy danych](./04-Database/README.md) | Konfiguracja PostgreSQL, projekt schematu detalicznego i przykładowe dane | [Buduj](./04-Database/README.md) |
| 05 | [Implementacja serwera MCP](./05-MCP-Server/README.md) | Tworzenie serwera FastMCP z integracją bazy danych | [Buduj](./05-MCP-Server/README.md) |
| 06 | [Tworzenie narzędzi](./06-Tools/README.md) | Tworzenie narzędzi do zapytań i introspekcji schematu bazy danych | [Buduj](./06-Tools/README.md) |
| **Lab 7-9: Zaawansowane funkcje** | | | |
| 07 | [Integracja wyszukiwania semantycznego](./07-Semantic-Search/README.md) | Implementacja wektorowych osadzeń z Azure OpenAI i pgvector | [Zaawansowane](./07-Semantic-Search/README.md) |
| 08 | [Testowanie i debugowanie](./08-Testing/README.md) | Strategie testowania, narzędzia debugowania i podejścia do walidacji | [Testuj](./08-Testing/README.md) |
| 09 | [Integracja VS Code](./09-VS-Code/README.md) | Konfiguracja integracji MCP w VS Code i używanie czatu AI | [Integruj](./09-VS-Code/README.md) |
| **Lab 10-12: Produkcja i najlepsze praktyki** | | | |
| 10 | [Strategie wdrażania](./10-Deployment/README.md) | Wdrażanie z Dockerem, Azure Container Apps i skalowanie | [Wdrażaj](./10-Deployment/README.md) |
| 11 | [Monitorowanie i obserwowalność](./11-Monitoring/README.md) | Application Insights, logowanie, monitorowanie wydajności | [Monitoruj](./11-Monitoring/README.md) |
| 12 | [Najlepsze praktyki i optymalizacja](./12-Best-Practices/README.md) | Optymalizacja wydajności, wzmacnianie bezpieczeństwa i wskazówki produkcyjne | [Optymalizuj](./12-Best-Practices/README.md) |

### 💻 Co zbudujesz

Pod koniec tej ścieżki nauki zbudujesz kompletny **Zava Retail Analytics MCP Server** z następującymi funkcjami:

- **Wielotabelowa baza detaliczna** z zamówieniami klientów, produktami i zapasami
- **Row Level Security** dla izolacji danych na poziomie sklepu
- **Semantyczne wyszukiwanie produktów** wykorzystujące osadzenia Azure OpenAI
- **Integracja czatu AI w VS Code** dla zapytań w języku naturalnym
- **Gotowe do produkcji wdrożenie** z Dockerem i Azure
- **Kompleksowe monitorowanie** za pomocą Application Insights

## 🎯 Wymagania wstępne do nauki

Aby maksymalnie wykorzystać tę ścieżkę nauki, powinieneś mieć:

- **Doświadczenie programistyczne**: Znajomość Pythona (preferowana) lub podobnych języków
- **Znajomość baz danych**: Podstawową wiedzę o SQL i bazach relacyjnych
- **Koncepcje API**: Zrozumienie REST API i protokołów HTTP
- **Narzędzia developerskie**: Doświadczenie z linią poleceń, Gitem i edytorami kodu
- **Podstawy chmury**: (opcjonalnie) Podstawowa wiedza o Azure lub podobnych platformach chmurowych
- **Znajomość Dockera**: (opcjonalnie) Zrozumienie koncepcji konteneryzacji

### Wymagane narzędzia

- **Docker Desktop** - Do uruchomienia PostgreSQL i serwera MCP
- **Azure CLI** - Do wdrażania zasobów w chmurze
- **VS Code** - Do rozwoju i integracji MCP
- **Git** - Do kontroli wersji
- **Python 3.8+** - Do tworzenia serwera MCP

## 📚 Przewodnik i zasoby do nauki

Ta ścieżka nauki zawiera kompleksowe zasoby, które pomogą Ci efektywnie się uczyć:

### Przewodnik nauki

Każde laboratorium zawiera:
- **Jasne cele nauki** - Co osiągniesz
- **Instrukcje krok po kroku** - Szczegółowe przewodniki implementacji
- **Przykłady kodu** - Działające przykłady z wyjaśnieniami
- **Ćwiczenia** - Możliwości praktycznego zastosowania
- **Poradniki rozwiązywania problemów** - Typowe problemy i rozwiązania
- **Dodatkowe zasoby** - Dalsza lektura i eksploracja

### Sprawdzenie wymagań wstępnych

Przed rozpoczęciem każdego laboratorium znajdziesz:
- **Wymaganą wiedzę** - Co powinieneś znać wcześniej
- **Weryfikację konfiguracji** - Jak sprawdzić środowisko
- **Szacowany czas** - Oczekiwany czas ukończenia
- **Efekty nauki** - Czego się nauczysz po ukończeniu

### Zalecane ścieżki nauki

Wybierz ścieżkę w zależności od swojego poziomu doświadczenia:

#### 🟢 **Ścieżka początkującego** (Nowy w MCP)
1. Upewnij się, że ukończyłeś 0-10 [MCP dla początkujących](https://aka.ms/mcp-for-beginners)
2. Przerób laboratoria 00-03, aby utrwalić podstawy
3. Postępuj z laboratoriami 04-06 dla praktycznego budowania
4. Wypróbuj laboratoria 07-09 dla praktycznego zastosowania

#### 🟡 **Ścieżka średniozaawansowana** (Z pewnym doświadczeniem MCP)
1. Przejrzyj laboratoria 00-01 pod kątem koncepcji bazodanowych
2. Skoncentruj się na laboratoriach 02-06 dla implementacji
3. Zagłęb się w laboratoria 07-12 dla zaawansowanych funkcji

#### 🔴 **Ścieżka zaawansowana** (Doświadczony w MCP)
1. Przejrzyj laboratoria 00-03 dla kontekstu
2. Skup się na laboratoriach 04-09 dla integracji bazy danych
3. Skoncentruj się na laboratoriach 10-12 dla produkcyjnego wdrożenia

## 🛠️ Jak efektywnie korzystać z tej ścieżki nauki

### Nauka sekwencyjna (zalecane)

Pracuj przez laboratoria w kolejności, aby uzyskać kompleksowe zrozumienie:

1. **Przeczytaj przegląd** - Zrozum, czego się nauczysz
2. **Sprawdź wymagania wstępne** - Upewnij się, że masz wymaganą wiedzę
3. **Kroki implementacji** - Wdrażaj zgodnie z przewodnikami
4. **Wykonaj ćwiczenia** - Utrwal swą wiedzę
5. **Przejrzyj kluczowe wnioski** - Utrwal wyniki nauki

### Nauka ukierunkowana

Jeśli potrzebujesz konkretnych umiejętności:

- **Integracja bazy danych**: Skup się na laboratoriach 04-06
- **Implementacja bezpieczeństwa**: Skoncentruj się na laboratoriach 02, 08, 12
- **AI/Semantyczne wyszukiwanie**: Zagłęb się w laboratorium 07
- **Wdrożenie produkcyjne**: Studiuj laboratoria 10-12

### Praktyka „hands-on”

Każde laboratorium zawiera:
- **Działające przykłady kodu** - Kopiuj, modyfikuj i eksperymentuj
- **Scenariusze rzeczywiste** - Praktyczne zastosowania analityki detalicznej
- **Stopniowa złożoność** - Budowanie od prostych do zaawansowanych
- **Kroki walidacji** - Sprawdź, czy implementacja działa

## 🌟 Społeczność i wsparcie

### Uzyskaj pomoc

- **Discord Azure AI**: [Dołącz, by uzyskać eksperckie wsparcie](https://discord.com/invite/ByRwuEEgH4)
- **Repozytorium GitHub i przykładowa implementacja**: [Przykład wdrożenia i zasoby](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **Społeczność MCP**: [Dołącz do szerszych dyskusji MCP](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Gotowy, by zacząć?

Rozpocznij swoją podróż od **[Lab 00: Wprowadzenie do integracji bazy danych MCP](./00-Introduction/README.md)**

---

*Opanuj tworzenie produkcyjnie gotowych serwerów MCP z integracją baz danych dzięki temu kompleksowemu, praktycznemu doświadczeniu edukacyjnemu.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->