# Studium przypadku: Udostępnianie REST API w API Management jako serwer MCP

Azure API Management to usługa, która zapewnia bramę nad Twoimi punktami końcowymi API. Działa w ten sposób, że Azure API Management działa jak proxy przed Twoimi API i decyduje, co zrobić z przychodzącymi żądaniami.

Korzystając z niej, zyskujesz wiele funkcji, takich jak:

- **Bezpieczeństwo** – możesz używać wszystkiego, od kluczy API, JWT po zarządzaną tożsamość.
- **Ograniczanie liczby żądań** – świetna funkcja pozwalająca zdecydować, ile żądań może przejść w określonym czasie. Pomaga to zapewnić wszystkim użytkownikom dobrą jakość obsługi oraz chroni Twoją usługę przed przeciążeniem.
- **Skalowanie i równoważenie obciążenia** – możesz skonfigurować wiele punktów końcowych, aby równoważyć obciążenie, a także zdecydować, jak to równoważenie ma działać.
- **Funkcje AI, takie jak semantyczne buforowanie**, limit tokenów, monitorowanie tokenów i inne. Są to świetne funkcje, które poprawiają responsywność oraz pomagają kontrolować wydatki na tokeny. [Więcej informacji tutaj](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Dlaczego MCP + Azure API Management?

Model Context Protocol szybko staje się standardem dla aplikacji AI opartych na agentach oraz sposobem na udostępnianie narzędzi i danych w spójny sposób. Azure API Management jest naturalnym wyborem, gdy potrzebujesz "zarządzać" API. Serwery MCP często integrują się z innymi API, aby rozwiązywać żądania dotyczące narzędzi, na przykład. Dlatego połączenie Azure API Management i MCP ma dużo sensu.

## Przegląd

W tym konkretnym przypadku użycia nauczymy się, jak udostępniać punkty końcowe API jako serwer MCP. Dzięki temu możemy łatwo uczynić te punkty końcowe częścią aplikacji opartej na agentach, jednocześnie korzystając z funkcji Azure API Management.

## Kluczowe funkcje

- Wybierasz metody punktów końcowych, które chcesz udostępnić jako narzędzia.
- Dodatkowe funkcje zależą od tego, co skonfigurujesz w sekcji polityk dla swojego API. Tutaj pokażemy, jak dodać ograniczanie liczby żądań.

## Wstępny krok: importowanie API

Jeśli masz już API w Azure API Management, świetnie – możesz pominąć ten krok. Jeśli nie, sprawdź ten link: [importowanie API do Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Udostępnianie API jako serwer MCP

Aby udostępnić punkty końcowe API, wykonaj następujące kroki:

1. Przejdź do Azure Portal pod następujący adres: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. Przejdź do swojej instancji API Management.

1. W menu po lewej stronie wybierz **APIs > MCP Servers > + Create new MCP Server**.

1. W sekcji API wybierz REST API, które chcesz udostępnić jako serwer MCP.

1. Wybierz jedną lub więcej operacji API, które chcesz udostępnić jako narzędzia. Możesz wybrać wszystkie operacje lub tylko konkretne.

    ![Wybierz metody do udostępnienia](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Wybierz **Create**.

1. Przejdź do opcji menu **APIs** i **MCP Servers**, powinieneś zobaczyć następujące:

    ![Zobacz serwer MCP w głównym panelu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Serwer MCP został utworzony, a operacje API są udostępnione jako narzędzia. Serwer MCP jest widoczny w panelu MCP Servers. Kolumna URL pokazuje punkt końcowy serwera MCP, który możesz wywołać w celu testowania lub w aplikacji klienckiej.

## Opcjonalnie: Konfiguracja polityk

Azure API Management ma kluczową koncepcję polityk, w których konfigurujesz różne reguły dla swoich punktów końcowych, takie jak ograniczanie liczby żądań czy semantyczne buforowanie. Polityki te są tworzone w formacie XML.

Oto jak skonfigurować politykę ograniczania liczby żądań dla swojego serwera MCP:

1. W portalu, w sekcji **APIs**, wybierz **MCP Servers**.

1. Wybierz serwer MCP, który utworzyłeś.

1. W menu po lewej stronie, w sekcji MCP, wybierz **Policies**.

1. W edytorze polityk dodaj lub edytuj polityki, które chcesz zastosować do narzędzi serwera MCP. Polityki są definiowane w formacie XML. Na przykład możesz dodać politykę ograniczającą liczbę wywołań narzędzi serwera MCP (w tym przykładzie 5 wywołań na 30 sekund na adres IP klienta). Oto XML, który spowoduje ograniczenie liczby żądań:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Oto obraz edytora polityk:

    ![Edytor polityk](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Wypróbuj

Upewnijmy się, że nasz serwer MCP działa zgodnie z oczekiwaniami.

Do tego użyjemy Visual Studio Code oraz GitHub Copilot w trybie agenta. Dodamy serwer MCP do pliku *mcp.json*. Dzięki temu Visual Studio Code będzie działać jako klient z funkcjami agentowymi, a użytkownicy końcowi będą mogli wpisywać polecenia i wchodzić w interakcję z serwerem.

Zobaczmy, jak to zrobić, aby dodać serwer MCP w Visual Studio Code:

1. Użyj polecenia MCP: **Add Server** z palety poleceń.

1. Po wyświetleniu monitu wybierz typ serwera: **HTTP (HTTP lub Server Sent Events)**.

1. Wprowadź URL serwera MCP w API Management. Przykład: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (dla punktu końcowego SSE) lub **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (dla punktu końcowego MCP), zwróć uwagę na różnicę między transportami: `/sse` lub `/mcp`.

1. Wprowadź identyfikator serwera według własnego wyboru. Nie jest to wartość istotna, ale pomoże Ci zapamiętać, czym jest ta instancja serwera.

1. Wybierz, czy zapisać konfigurację w ustawieniach przestrzeni roboczej czy użytkownika.

  - **Ustawienia przestrzeni roboczej** – Konfiguracja serwera jest zapisywana w pliku .vscode/mcp.json dostępnym tylko w bieżącej przestrzeni roboczej.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    lub jeśli wybierzesz streaming HTTP jako transport, będzie to wyglądać nieco inaczej:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Ustawienia użytkownika** – Konfiguracja serwera jest dodawana do globalnego pliku *settings.json* i jest dostępna we wszystkich przestrzeniach roboczych. Konfiguracja wygląda podobnie do poniższego:

    ![Ustawienia użytkownika](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Musisz również dodać konfigurację nagłówka, aby upewnić się, że uwierzytelnianie działa poprawnie w Azure API Management. Używa nagłówka o nazwie **Ocp-Apim-Subscription-Key**.

    - Oto jak możesz dodać go do ustawień:

    ![Dodawanie nagłówka do uwierzytelniania](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), spowoduje to wyświetlenie monitu o podanie wartości klucza API, którą możesz znaleźć w Azure Portal dla swojej instancji Azure API Management.

   - Aby dodać go do *mcp.json*, możesz zrobić to w następujący sposób:

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

### Użyj trybu agenta

Teraz wszystko jest skonfigurowane w ustawieniach lub w *.vscode/mcp.json*. Wypróbujmy to.

Powinien pojawić się przycisk Narzędzia, gdzie widoczne są narzędzia udostępnione przez Twój serwer:

![Narzędzia z serwera](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kliknij ikonę narzędzi, a powinieneś zobaczyć listę narzędzi, jak poniżej:

    ![Narzędzia](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Wprowadź polecenie w czacie, aby wywołać narzędzie. Na przykład, jeśli wybrałeś narzędzie do uzyskiwania informacji o zamówieniu, możesz zapytać agenta o zamówienie. Oto przykład polecenia:

    ```text
    get information from order 2
    ```

    Zostanie wyświetlona ikona narzędzi z pytaniem, czy chcesz kontynuować wywoływanie narzędzia. Wybierz kontynuację, a powinieneś zobaczyć wynik, jak poniżej:

    ![Wynik z polecenia](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **To, co widzisz powyżej, zależy od narzędzi, które skonfigurowałeś, ale idea polega na tym, że otrzymujesz odpowiedź tekstową, jak powyżej.**

## Źródła

Oto, gdzie możesz dowiedzieć się więcej:

- [Samouczek dotyczący Azure API Management i MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Przykład w Pythonie: Zabezpiecz zdalne serwery MCP za pomocą Azure API Management (eksperymentalne)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorium autoryzacji klienta MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Użyj rozszerzenia Azure API Management dla VS Code, aby importować i zarządzać API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Rejestracja i odkrywanie zdalnych serwerów MCP w Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Świetne repozytorium pokazujące wiele możliwości AI z Azure API Management
- [Warsztaty AI Gateway](https://azure-samples.github.io/AI-Gateway/) Zawiera warsztaty z użyciem Azure Portal, co jest świetnym sposobem na rozpoczęcie oceny możliwości AI.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.