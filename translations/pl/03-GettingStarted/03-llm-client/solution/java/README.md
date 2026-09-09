# Klient Kalkulatora LLM

Aplikacja Java, która demonstruje, jak używać LangChain4j do łączenia się z usługą kalkulatora MCP (Model Context Protocol) za pośrednictwem MiniMax OpenAI-kompatybilnego API.

## Wymagania wstępne

- Java 21 lub nowsza
- Maven 3.6+ (lub użyj dołączonego wrappera Maven)
- Klucz API MiniMax
- Usługa kalkulatora MCP działająca pod adresem `http://localhost:8080`

## Uzyskiwanie klucza API

Ta aplikacja korzysta z MiniMax OpenAI-kompatybilnego API. Wykonaj następujące kroki, aby uzyskać swój klucz i punkt końcowy:

### 1. Wybierz punkt końcowy
1. Użyj `https://api.minimax.io/v1` dla punktu końcowego globalnego
2. Użyj `https://api.minimaxi.com/v1` dla punktu końcowego Chin

### 2. Utwórz klucz API
1. Utwórz klucz API MiniMax na swoim koncie MiniMax
2. Przechowuj klucz w bezpiecznym miejscu

### 3. Ustaw zmienne środowiskowe

#### Na Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Na Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### Na macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Konfiguracja i instalacja

1. **Sklonuj lub przejdź do katalogu projektu**

2. **Zainstaluj zależności**:
   ```cmd
   mvnw clean install
   ```
   Lub jeśli masz zainstalowany Maven globalnie:
   ```cmd
   mvn clean install
   ```

3. **Skonfiguruj zmienne środowiskowe** (patrz sekcja "Uzyskiwanie klucza API" powyżej)

4. **Uruchom usługę kalkulatora MCP**:
   Upewnij się, że usługa kalkulatora MCP z rozdziału 1 działa pod adresem `http://localhost:8080/sse`. Powinna być uruchomiona przed startem klienta.

## Uruchamianie aplikacji

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Co robi aplikacja

Aplikacja demonstruje trzy główne interakcje z usługą kalkulatora:

1. **Dodawanie**: Oblicza sumę 24.5 i 17.3
2. **Pierwiastek kwadratowy**: Oblicza pierwiastek kwadratowy z 144
3. **Pomoc**: Pokazuje dostępne funkcje kalkulatora

## Oczekiwany wynik

Po pomyślnym uruchomieniu powinieneś zobaczyć wynik podobny do:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Rozwiązywanie problemów

### Typowe problemy

1. **"Zmienna środowiskowa OPENAI_API_KEY nie jest ustawiona"**
   - Upewnij się, że ustawiłeś zmienną środowiskową `OPENAI_API_KEY`
   - Po ustawieniu zmiennej, zrestartuj terminal/wiersz polecenia

2. **"Połączenie odrzucone na localhost:8080"**
   - Upewnij się, że usługa kalkulatora MCP działa na porcie 8080
   - Sprawdź, czy inna usługa nie używa portu 8080

3. **"Błąd uwierzytelniania"**
   - Zweryfikuj, czy Twój klucz API jest ważny
   - Sprawdź, czy `OPENAI_BASE_URL` odpowiada wybranemu punktowi końcowemu

4. **Błędy kompilacji Maven**
   - Upewnij się, że używasz Java 21 lub wyższej: `java -version`
   - Spróbuj wyczyścić build: `mvnw clean`

### Debugowanie

Aby włączyć logowanie debugowania, dodaj następujący argument JVM przy uruchamianiu:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguracja

Aplikacja jest skonfigurowana do:
- Domyślnego używania MiniMax-M3 lub MiniMax-M2.7, gdy ustawiona jest zmienna `MINIMAX_MODEL_ID`
- Łączenia z `OPENAI_BASE_URL` jeśli jest ustawiona; w przeciwnym razie używa `https://api.minimaxi.com/v1` gdy `MINIMAX_REGION=cn_zh`, albo domyślnie `https://api.minimax.io/v1`
- Łączenia się z usługą MCP pod adresem `http://localhost:8080/sse`
- Używa limitu czasu 60 sekund na żądania

## Zależności

Kluczowe zależności używane w tym projekcie:
- **LangChain4j**: Do integracji AI i zarządzania narzędziami
- **LangChain4j MCP**: Do wsparcia Model Context Protocol
- **LangChain4j OpenAI official**: Do integracji MiniMax OpenAI-kompatybilnego API
- **Spring Boot**: Do frameworka aplikacji i wstrzykiwania zależności

## Licencja

Ten projekt jest licencjonowany na podstawie Apache License 2.0 - szczegóły w pliku [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->