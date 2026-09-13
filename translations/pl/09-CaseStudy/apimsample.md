# Studium przypadku: Udostępnianie REST API w Azure API Management jako serwer MCP

Azure API Management to usługa, która zapewnia Braminę (Gateway) nad punktami końcowymi Twojego API. Działa ona jako proxy przed Twoimi API i może decydować, co zrobić z nadchodzącymi żądaniami.

Korzystając z niej, dodajesz cały zestaw funkcji, takich jak:

- **Bezpieczeństwo**, możesz korzystać z wszystkiego, od kluczy API, JWT po zarządzaną tożsamość.
- **Ograniczanie liczby zapytań (rate limiting)**, świetna funkcja pozwalająca zdecydować, ile wywołań jest dozwolonych na określoną jednostkę czasu. Pomaga to zapewnić wszystkim użytkownikom świetne doświadczenia oraz zapobiega przeładowaniu usługi.
- **Skalowanie i równoważenie obciążenia**. Możesz skonfigurować wiele punktów końcowych, aby rozłożyć obciążenie oraz zdecydować, jak ma działać „równoważenie obciążenia”.
- **Funkcje AI, takie jak semantyczne buforowanie (semantic caching)**, limit tokenów, monitorowanie tokenów i inne. To świetne funkcje, które poprawiają szybkość reakcji oraz pomagają kontrolować zużycie tokenów. [Czytaj więcej tutaj](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Dlaczego MCP + Azure API Management?

Model Context Protocol szybko staje się standardem dla agentowych aplikacji AI oraz sposobów nadawania narzędziom i danym spójnej formy udostępniania. Azure API Management jest naturalnym wyborem, gdy trzeba „zarządzać” API. Serwery MCP często integrują się z innymi API, aby na przykład rozwiązywać żądania do narzędzi. Dlatego połączenie Azure API Management i MCP ma wiele sensu.

## Przegląd

W tym konkretnym przypadku użycia nauczymy się, jak udostępnić punkty końcowe API jako serwer MCP. Dzięki temu możemy łatwo uczynić te punkty końcowe częścią agentowej aplikacji, jednocześnie korzystając z funkcji Azure API Management.

## Kluczowe funkcje

- Wybierasz metody punktu końcowego, które chcesz udostępnić jako narzędzia.
- Dodatkowe funkcje, które uzyskasz, zależą od tego, co skonfigurujesz w sekcji polityk dla Twojego API. Tutaj pokażemy, jak możesz dodać ograniczenie liczby zapytań (rate limiting).

## Krok wstępny: importowanie API

Jeśli masz już API w Azure API Management, świetnie, możesz pominąć ten krok. Jeśli nie, sprawdź ten link, [importowanie API do Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Udostępnianie API jako serwera MCP

Aby udostępnić punkty końcowe API, wykonaj następujące kroki:

1. Wejdź do Azure Portal pod następujący adres <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Przejdź do swojej instancji Azure API Management.

1. W lewym menu wybierz APIs > MCP Servers > + Utwórz nowy serwer MCP.

1. W API wybierz REST API, które chcesz udostępnić jako serwer MCP.

1. Wybierz jedną lub więcej operacji API do udostępnienia jako narzędzia. Możesz wybrać wszystkie operacje lub tylko konkretne.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Wybierz **Utwórz**.

1. Przejdź do menu **APIs** i **MCP Servers**, powinieneś zobaczyć następujące:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Serwer MCP został utworzony, a operacje API są udostępnione jako narzędzia. Serwer MCP jest widoczny na liście w panelu MCP Servers. Kolumna URL pokazuje punkt końcowy serwera MCP, który możesz wywołać do testów lub z poziomu aplikacji klienckiej.

## Opcjonalnie: Konfiguracja polityk

Azure API Management opiera się na koncepcji polityk, gdzie definiujesz różne reguły dla swoich punktów końcowych, na przykład ograniczenie liczby zapytań lub semantyczne buforowanie. Polityki te są zdefiniowane w XML.

Oto jak możesz ustawić politykę ograniczenia liczby zapytań dla serwera MCP:

1. W portalu, w sekcji APIs, wybierz **MCP Servers**.

1. Wybierz utworzony serwer MCP.

1. W lewym menu, pod MCP, wybierz **Policies**.

1. W edytorze polityk dodaj lub edytuj polityki, które chcesz zastosować do narzędzi serwera MCP. Polityki są definiowane w formacie XML. Na przykład możesz dodać politykę ograniczającą wywołania narzędzi serwera MCP (w tym przykładzie 5 wywołań na 30 sekund na adres IP klienta). Oto XML, który spowoduje takie ograniczenie:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Oto zrzut ekranu edytora polityk:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Wypróbuj to

Sprawdźmy, czy nasz serwer MCP działa zgodnie z oczekiwaniami.

> [!NOTE]
> Azure API Management obecnie udostępnia ten serwer przez transmisję HTTP Streamable
> pod endpointem `/mcp`. Starszy transport HTTP+SSE `/sse` jest przestarzały i
> powinien być używany wyłącznie z klientami legacy.

Do tego użyjemy Visual Studio Code oraz GitHub Copilot w trybie Agenta. Dodamy serwer MCP do pliku *mcp.json*. Dzięki temu Visual Studio Code będzie działać jako klient z funkcjonalnościami agentowymi, a użytkownicy końcowi będą mogli wpisać zapytanie i wchodzić w interakcję z tym serwerem.

Zobaczmy, jak dodać serwer MCP w Visual Studio Code:

1. Użyj polecenia MCP: **Dodaj serwer z palety poleceń**.

1. Po wyświetleniu monitów wybierz typ serwera: **HTTP (HTTP lub Server Sent Events)**.

1. Wprowadź adres Streamable HTTP URL wyświetlony dla serwera MCP w API Management.
    Na przykład:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Wprowadź identyfikator serwera według własnego wyboru. Nie jest to istotna wartość, ale pomoże Ci zapamiętać, czym jest ta instancja serwera.

1. Wybierz, czy zapisać konfigurację w ustawieniach workspace czy użytkownika.

  - **Ustawienia workspace** - Konfiguracja serwera zostanie zapisana w pliku .vscode/mcp.json, dostępnym tylko w bieżącym workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Ustawienia użytkownika** - Konfiguracja serwera zostanie dodana do globalnego pliku *settings.json* i będzie dostępna we wszystkich workspace'ach. Konfiguracja wygląda mniej więcej tak:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Musisz także dodać konfigurację nagłówka, aby poprawnie autoryzować się w Azure API Management. Używa on nagłówka o nazwie **Ocp-Apim-Subscription-Key**.

    - Oto jak możesz dodać go do ustawień:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), spowoduje to wyświetlenie monitu o podanie wartości klucza API, który możesz znaleźć w Azure Portal dla swojej instancji Azure API Management.

   - Aby dodać go do *mcp.json*, możesz to zrobić w ten sposób:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Użycie trybu Agenta

Teraz wszystko mamy skonfigurowane, zarówno w ustawieniach, jak i w *.vscode/mcp.json*. Spróbujmy to przetestować.

Powinien pojawić się ikonka Narzędzi, gdzie widoczne są udostępnione narzędzia z Twojego serwera:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kliknij ikonę narzędzi, zobaczysz listę dostępnych narzędzi, na przykład:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Wpisz zapytanie w czacie, aby wywołać narzędzie. Przykładowo, jeśli wybrałeś narzędzie do pobierania informacji o zamówieniu, możesz zapytać agenta o zamówienie. Oto przykładowe zapytanie:

    ```text
    get information from order 2
    ```

    Zostanie wyświetlona ikona narzędzi z pytaniem, czy chcesz kontynuować wywołanie narzędzia. Wybierz kontynuuj, a powinieneś zobaczyć wynik podobny do poniższego:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **to, co zobaczysz powyżej, zależy od narzędzi, które skonfigurowałeś, ale idea jest taka, że otrzymujesz tekstową odpowiedź jak powyżej**


## Odnośniki

Oto, jak możesz dowiedzieć się więcej:

- [Samouczek dotyczący Azure API Management i MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Przykład w Python: Zabezpieczanie zdalnych serwerów MCP za pomocą Azure API Management (eksperymentalne)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorium autoryzacji klienta MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Użycie rozszerzenia Azure API Management dla VS Code do importu i zarządzania API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Rejestracja i odkrywanie zdalnych serwerów MCP w Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Świetne repozytorium prezentujące wiele możliwości AI z Azure API Management
- [Warsztaty AI Gateway](https://azure-samples.github.io/AI-Gateway/) Zawierają warsztaty korzystające z Azure Portal, co jest świetnym sposobem na rozpoczęcie oceny możliwości AI.

## Co dalej

- Powrót do: [Przegląd studiów przypadków](./README.md)
- Następne: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->