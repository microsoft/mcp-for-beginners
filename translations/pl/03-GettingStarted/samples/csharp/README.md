# Basic Calculator MCP Service

Ta usługa udostępnia podstawowe operacje kalkulatora za pomocą Model Context Protocol (MCP). Została zaprojektowana jako prosty przykład dla początkujących uczących się implementacji MCP.

Więcej informacji znajdziesz w [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funkcje

Ta usługa kalkulatora oferuje następujące możliwości:

1. **Podstawowe operacje arytmetyczne**:
   - Dodawanie dwóch liczb
   - Odejmowanie jednej liczby od drugiej
   - Mnożenie dwóch liczb
   - Dzielenie jednej liczby przez drugą (z kontrolą dzielenia przez zero)

## Korzystanie z typu `stdio`
  
## Konfiguracja

1. **Konfiguracja serwerów MCP**:
   - Otwórz swoje środowisko pracy w VS Code.
   - Utwórz plik `.vscode/mcp.json` w folderze swojego workspace, aby skonfigurować serwery MCP. Przykładowa konfiguracja:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - Zostaniesz poproszony o podanie katalogu głównego repozytorium GitHub, który można uzyskać za pomocą polecenia `git rev-parse --show-toplevel`.

## Korzystanie z usługi

Usługa udostępnia następujące endpointy API przez protokół MCP:

- `add(a, b)`: Dodaj dwie liczby
- `subtract(a, b)`: Odejmij drugą liczbę od pierwszej
- `multiply(a, b)`: Pomnóż dwie liczby
- `divide(a, b)`: Podziel pierwszą liczbę przez drugą (z kontrolą dzielenia przez zero)
- isPrime(n): Sprawdź, czy liczba jest pierwsza

## Testowanie z Github Copilot Chat w VS Code

1. Spróbuj wykonać zapytanie do usługi za pomocą protokołu MCP. Na przykład możesz zapytać:
   - "Dodaj 5 i 3"
   - "Odejmij 10 od 4"
   - "Pomnóż 6 i 7"
   - "Podziel 8 przez 2"
   - "Czy 37854 jest liczbą pierwszą?"
   - "Jakie są 3 liczby pierwsze przed i po 4242?"
2. Aby upewnić się, że używane są odpowiednie narzędzia, dodaj #MyCalculator do zapytania. Na przykład:
   - "Dodaj 5 i 3 #MyCalculator"
   - "Odejmij 10 od 4 #MyCalculator"

## Wersja konteneryzowana

Poprzednie rozwiązanie jest świetne, gdy masz zainstalowane .NET SDK i wszystkie zależności są na miejscu. Jednak jeśli chcesz udostępnić rozwiązanie lub uruchomić je w innym środowisku, możesz skorzystać z wersji konteneryzowanej.

1. Uruchom Dockera i upewnij się, że działa.
1. W terminalu przejdź do folderu `03-GettingStarted\samples\csharp\src`
1. Aby zbudować obraz Dockera dla usługi kalkulatora, wykonaj następujące polecenie (zamień `<YOUR-DOCKER-USERNAME>` na swoją nazwę użytkownika Docker Hub):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Po zbudowaniu obrazu, prześlij go do Docker Hub. Wykonaj następujące polecenie:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Korzystanie z wersji Dockerowej

1. W pliku `.vscode/mcp.json` zastąp konfigurację serwera następującą:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Patrząc na konfigurację, widzisz, że polecenie to `docker`, a argumenty to `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Flaga `--rm` zapewnia usunięcie kontenera po jego zatrzymaniu, a flaga `-i` pozwala na interakcję z wejściem standardowym kontenera. Ostatni argument to nazwa obrazu, który właśnie zbudowaliśmy i przesłaliśmy do Docker Hub.

## Testowanie wersji Dockerowej

Uruchom serwer MCP, klikając mały przycisk Start nad `"mcp-calc": {`, i tak jak wcześniej możesz poprosić usługę kalkulatora o wykonanie obliczeń.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.