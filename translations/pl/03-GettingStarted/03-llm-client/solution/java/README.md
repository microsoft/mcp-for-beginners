# Calculator LLM Client

Aplikacja Java, która pokazuje, jak używać LangChain4j do połączenia z usługą kalkulatora MCP (Model Context Protocol) z integracją GitHub Models.

## Wymagania wstępne

- Java 21 lub nowsza
- Maven 3.6+ (lub użyj dołączonego wrappera Maven)
- Konto GitHub z dostępem do GitHub Models
- Usługa kalkulatora MCP działająca pod adresem `http://localhost:8080`

## Jak uzyskać token GitHub

Ta aplikacja korzysta z GitHub Models, co wymaga osobistego tokena dostępu GitHub. Wykonaj poniższe kroki, aby uzyskać swój token:

### 1. Wejdź na GitHub Models
1. Przejdź do [GitHub Models](https://github.com/marketplace/models)
2. Zaloguj się na swoje konto GitHub
3. Poproś o dostęp do GitHub Models, jeśli jeszcze go nie masz

### 2. Utwórz osobisty token dostępu
1. Przejdź do [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Kliknij "Generate new token" → "Generate new token (classic)"
3. Nadaj tokenowi opisową nazwę (np. "MCP Calculator Client")
4. Ustaw datę wygaśnięcia według potrzeb
5. Wybierz następujące zakresy:
   - `repo` (jeśli potrzebujesz dostępu do prywatnych repozytoriów)
   - `user:email`
6. Kliknij "Generate token"
7. **Ważne**: Skopiuj token od razu – nie będziesz mógł go zobaczyć ponownie!

### 3. Ustaw zmienną środowiskową

#### Na Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Na Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Na macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Konfiguracja i instalacja

1. **Sklonuj repozytorium lub przejdź do katalogu projektu**

2. **Zainstaluj zależności**:
   ```cmd
   mvnw clean install
   ```
   Lub jeśli masz globalnie zainstalowanego Mavena:
   ```cmd
   mvn clean install
   ```

3. **Ustaw zmienną środowiskową** (patrz sekcja "Jak uzyskać token GitHub" powyżej)

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
3. **Pomoc**: Wyświetla dostępne funkcje kalkulatora

## Oczekiwany wynik

Po poprawnym uruchomieniu powinieneś zobaczyć wynik podobny do:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Rozwiązywanie problemów

### Najczęstsze problemy

1. **"GITHUB_TOKEN environment variable not set"**
   - Upewnij się, że ustawiłeś zmienną środowiskową `GITHUB_TOKEN`
   - Zrestartuj terminal/wiersz poleceń po ustawieniu zmiennej

2. **"Connection refused to localhost:8080"**
   - Sprawdź, czy usługa kalkulatora MCP działa na porcie 8080
   - Upewnij się, że inna usługa nie zajmuje portu 8080

3. **"Authentication failed"**
   - Zweryfikuj, czy token GitHub jest ważny i ma odpowiednie uprawnienia
   - Sprawdź, czy masz dostęp do GitHub Models

4. **Błędy budowania Maven**
   - Upewnij się, że używasz Java 21 lub nowszej: `java -version`
   - Spróbuj wyczyścić build: `mvnw clean`

### Debugowanie

Aby włączyć logowanie debugowania, dodaj następujący argument JVM podczas uruchamiania:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguracja

Aplikacja jest skonfigurowana do:
- Korzystania z GitHub Models z modelem `gpt-4.1-nano`
- Łączenia się z usługą MCP pod adresem `http://localhost:8080/sse`
- Ustawienia limitu czasu na 60 sekund dla zapytań
- Włączenia logowania zapytań/odpowiedzi do celów debugowania

## Zależności

Kluczowe zależności użyte w tym projekcie:
- **LangChain4j**: do integracji AI i zarządzania narzędziami
- **LangChain4j MCP**: wsparcie dla Model Context Protocol
- **LangChain4j GitHub Models**: integracja z GitHub Models
- **Spring Boot**: framework aplikacji i wstrzykiwanie zależności

## Licencja

Projekt jest licencjonowany na podstawie Apache License 2.0 – szczegóły w pliku [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE).

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.