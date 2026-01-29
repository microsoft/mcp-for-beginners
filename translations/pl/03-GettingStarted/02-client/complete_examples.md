# Kompletny Przykład Klientów MCP

Ten katalog zawiera kompletne, działające przykłady klientów MCP w różnych językach programowania. Każdy klient demonstruje pełną funkcjonalność opisaną w głównym samouczku README.md.

## Dostępni Klienci

### 1. Klient Java (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) przez HTTP
- **Serwer docelowy**: `http://localhost:8080`
- **Funkcje**:
  - Nawiązywanie połączenia i ping
  - Wyświetlanie listy narzędzi
  - Operacje kalkulatora (dodawanie, odejmowanie, mnożenie, dzielenie, pomoc)
  - Obsługa błędów i ekstrakcja wyników

**Aby uruchomić:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. Klient C# (`client_example_csharp.cs`)

- **Transport**: Stdio (Standardowe Wejście/Wyjście)
- **Serwer docelowy**: Lokalny serwer MCP .NET uruchamiany za pomocą dotnet run
- **Funkcje**:
  - Automatyczne uruchamianie serwera przez transport stdio
  - Wyświetlanie listy narzędzi i zasobów
  - Operacje kalkulatora
  - Parsowanie wyników w formacie JSON
  - Kompleksowa obsługa błędów

**Aby uruchomić:**

```bash
dotnet run
```

### 3. Klient TypeScript (`client_example_typescript.ts`)

- **Transport**: Stdio (Standardowe Wejście/Wyjście)
- **Serwer docelowy**: Lokalny serwer MCP Node.js
- **Funkcje**:
  - Pełne wsparcie dla protokołu MCP
  - Operacje na narzędziach, zasobach i promptach
  - Operacje kalkulatora
  - Odczyt zasobów i wykonywanie promptów
  - Solidna obsługa błędów

**Aby uruchomić:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Klient Python (`client_example_python.py`)

- **Transport**: Stdio (Standardowe Wejście/Wyjście)  
- **Serwer docelowy**: Lokalny serwer MCP w Pythonie
- **Funkcje**:
  - Wzorzec async/await dla operacji
  - Odkrywanie narzędzi i zasobów
  - Testowanie operacji kalkulatora
  - Odczyt treści zasobów
  - Organizacja oparta na klasach

**Aby uruchomić:**

```bash
python client_example_python.py
```

## Wspólne Funkcje Wszystkich Klientów

Każda implementacja klienta demonstruje:

1. **Zarządzanie Połączeniem**
   - Nawiązywanie połączenia z serwerem MCP
   - Obsługa błędów połączenia
   - Odpowiednie czyszczenie i zarządzanie zasobami

2. **Odkrywanie Serwera**
   - Wyświetlanie dostępnych narzędzi
   - Wyświetlanie dostępnych zasobów (jeśli obsługiwane)
   - Wyświetlanie dostępnych promptów (jeśli obsługiwane)

3. **Wywoływanie Narzędzi**
   - Podstawowe operacje kalkulatora (dodawanie, odejmowanie, mnożenie, dzielenie)
   - Komenda pomocy dla informacji o serwerze
   - Prawidłowe przekazywanie argumentów i obsługa wyników

4. **Obsługa Błędów**
   - Błędy połączenia
   - Błędy podczas wykonywania narzędzi
   - Łagodne awarie i informowanie użytkownika

5. **Przetwarzanie Wyników**
   - Ekstrakcja treści tekstowej z odpowiedzi
   - Formatowanie wyników dla czytelności
   - Obsługa różnych formatów odpowiedzi

## Wymagania Wstępne

Przed uruchomieniem tych klientów upewnij się, że:

1. **Odpowiedni serwer MCP działa** (z katalogu `../01-first-server/`)
2. **Zainstalowano wymagane zależności** dla wybranego języka
3. **Masz odpowiednią łączność sieciową** (dla transportów opartych na HTTP)

## Kluczowe Różnice Między Implementacjami

| Język      | Transport | Uruchamianie Serwera | Model Async | Kluczowe Biblioteki |
|------------|-----------|----------------------|-------------|---------------------|
| Java       | SSE/HTTP  | Zewnętrzne          | Sync        | WebFlux, MCP SDK    |
| C#         | Stdio     | Automatyczne        | Async/Await | .NET MCP SDK        |
| TypeScript | Stdio     | Automatyczne        | Async/Await | Node MCP SDK        |
| Python     | Stdio     | Automatyczne        | AsyncIO     | Python MCP SDK      |
| Rust       | Stdio     | Automatyczne        | Async/Await | Rust MCP SDK, Tokio |

## Kolejne Kroki

Po zapoznaniu się z tymi przykładami klientów:

1. **Zmodyfikuj klientów**, aby dodać nowe funkcje lub operacje
2. **Stwórz własny serwer** i przetestuj go z tymi klientami
3. **Eksperymentuj z różnymi transportami** (SSE vs. Stdio)
4. **Zbuduj bardziej złożoną aplikację**, która integruje funkcjonalność MCP

## Rozwiązywanie Problemów

### Typowe Problemy

1. **Odmowa połączenia**: Upewnij się, że serwer MCP działa na oczekiwanym porcie/ścieżce
2. **Nie znaleziono modułu**: Zainstaluj wymagane MCP SDK dla swojego języka
3. **Odmowa dostępu**: Sprawdź uprawnienia do plików dla transportu stdio
4. **Nie znaleziono narzędzia**: Zweryfikuj, czy serwer implementuje oczekiwane narzędzia

### Wskazówki Debugowania

1. **Włącz szczegółowe logowanie** w swoim MCP SDK
2. **Sprawdź logi serwera** w poszukiwaniu komunikatów o błędach
3. **Zweryfikuj nazwy i sygnatury narzędzi**, aby pasowały między klientem a serwerem
4. **Przetestuj za pomocą MCP Inspector**, aby zweryfikować funkcjonalność serwera

## Powiązana Dokumentacja

- [Główny Samouczek Klienta](./README.md)
- [Przykłady Serwera MCP](../../../../03-GettingStarted/01-first-server)
- [MCP z Integracją LLM](../../../../03-GettingStarted/03-llm-client)
- [Oficjalna Dokumentacja MCP](https://modelcontextprotocol.io/)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.