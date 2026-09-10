# Klient Kalkulatora LLM

Aplikacja Java, która demonstruje, jak używać LangChain4j do połączenia z usługą kalkulatora MCP (Model Context Protocol) poprzez zgodne z OpenAI API MiniMax.

## Wymagania wstępne

- Java 21 lub nowsza
- Maven 3.6+ (lub użyj dołączonego wrappera Maven)
- Klucz API MiniMax
- Usługa kalkulatora MCP działająca na `http://localhost:8080`

## Jak uzyskać klucz API

Ta aplikacja korzysta z kompatybilnego z OpenAI API MiniMax. Wykonaj poniższe kroki, aby otrzymać swój klucz i punkt końcowy:

### 1. Wybierz punkt końcowy
1. Użyj `https://api.minimax.io/v1` dla globalnego punktu końcowego
2. Użyj `https://api.minimaxi.com/v1` dla punktu końcowego w Chinach

### 2. Utwórz klucz API
1. Utwórz klucz API MiniMax ze swojego konta MiniMax
2. Przechowuj klucz w bezpiecznym miejscu

### 3. Ustaw zmienne środowiskowe

#### W systemie Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### W systemie Windows (PowerShell):
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
   Lub jeśli masz Maven zainstalowany globalnie:
   ```cmd
   mvn clean install
   ```

3. **Ustaw zmienne środowiskowe** (patrz sekcja "Jak uzyskać klucz API" powyżej)

4. **Uruchom usługę kalkulatora MCP**:
   Upewnij się, że masz uruchomioną usługę kalkulatora MCP z rozdziału 1 pod adresem `http://localhost:8080/sse`. Powinna być uruchomiona przed startem klienta.

## Uruchomienie aplikacji

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

Po poprawnym uruchomieniu powinieneś zobaczyć wynik podobny do:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Rozwiązywanie problemów

### Najczęstsze problemy

1. **"Zmienna środowiskowa OPENAI_API_KEY nie jest ustawiona"**
   - Upewnij się, że ustawiłeś zmienną środowiskową `OPENAI_API_KEY`
   - Uruchom ponownie terminal/wiersz poleceń po ustawieniu zmiennej

2. **"Odmowa połączenia z localhost:8080"**
   - Sprawdź, czy usługa kalkulatora MCP działa na porcie 8080
   - Upewnij się, że inna usługa nie używa portu 8080

3. **"Błąd uwierzytelniania"**
   - Zweryfikuj, czy Twój klucz API jest poprawny
   - Sprawdź, czy `OPENAI_BASE_URL` odpowiada zamierzonemu punktowi końcowemu

4. **Błędy kompilacji Maven**
   - Upewnij się, że używasz Java 21 lub nowszej: `java -version`
   - Spróbuj wyczyścić kompilację: `mvnw clean`

### Debugowanie

Aby włączyć logowanie debugowania, dodaj następujący argument JVM podczas uruchamiania:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguracja

Aplikacja jest skonfigurowana do:
- Domyślnego użycia MiniMax-M3; ustaw `MINIMAX_MODEL_ID` by wybrać `MiniMax-M3` lub `MiniMax-M2.7`
- Łączenia się z `OPENAI_BASE_URL` jeśli jest ustawiony; w przeciwnym razie używa `https://api.minimaxi.com/v1` gdy `MINIMAX_REGION=cn_zh`, lub domyślnie `https://api.minimax.io/v1`
- Łączenia się z usługą MCP pod `http://localhost:8080/sse`
- Używania timeoutu 60 sekund dla zapytań

## Zależności

Kluczowe zależności użyte w tym projekcie:
- **LangChain4j**: Do integracji AI i zarządzania narzędziami
- **LangChain4j MCP**: Do wsparcia Model Context Protocol
- **LangChain4j OpenAI official**: Do integracji MiniMax kompatybilnego API OpenAI
- **Spring Boot**: Do frameworka aplikacji i wstrzykiwania zależności

## Licencja

Ten projekt jest licencjonowany na warunkach Apache License 2.0 - zobacz plik [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) po szczegóły.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->