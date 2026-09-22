# Wdrażanie serwerów MCP

> [!NOTE]
> Przykłady konfiguracji korzystające z punktu końcowego `/sse` dotyczą starszego transportu HTTP+SSE.
> Zdalne serwery MCP `2026-07-28` korzystają ze Streamable HTTP, zwykle na
> serwerowo zdefiniowanym punkcie końcowym, takim jak `/mcp`.

Wdrążenie Twojego serwera MCP umożliwia innym dostęp do jego narzędzi i zasobów poza Twoim lokalnym środowiskiem. Istnieje kilka strategii wdrażania, które warto rozważyć, w zależności od wymagań dotyczących skalowalności, niezawodności i łatwości zarządzania. Poniżej znajdziesz wskazówki dotyczące wdrażania serwerów MCP lokalnie, w kontenerach oraz w chmurze.

## Przegląd

Ta lekcja obejmuje informacje, jak wdrożyć aplikację MCP Server.

## Cele nauki

Do końca tej lekcji będziesz potrafił:

- Ocenić różne podejścia do wdrażania.
- Wdrożyć swoją aplikację.

## Lokalny rozwój i wdrożenie

Jeśli Twój serwer ma być używany na maszynie użytkownika, możesz wykonać następujące kroki:

1. **Pobierz serwer**. Jeśli nie napisałeś serwera, najpierw pobierz go na swoją maszynę.
1. **Uruchom proces serwera**: Uruchom swoją aplikację serwera MCP

Dla SSE (nie dotyczy serwera typu stdio)

1. **Skonfiguruj sieć**: Upewnij się, że serwer jest dostępny na oczekiwanym porcie
1. **Połącz klientów**: Użyj lokalnych adresów URL połączenia, takich jak `http://localhost:3000`

## Wdrażanie w chmurze

Serwery MCP można wdrażać na różnych platformach chmurowych:

- **Funkcje bezserwerowe (Serverless Functions)**: Wdróż lekkie serwery MCP jako funkcje bezserwerowe
- **Usługi kontenerowe**: Użyj usług takich jak Azure Container Apps, AWS ECS lub Google Cloud Run
- **Kubernetes**: Wdróż i zarządzaj serwerami MCP w klastrach Kubernetes dla wysokiej dostępności

### Przykład: Azure Container Apps

Azure Container Apps obsługuje wdrażanie serwerów MCP. To wciąż praca w toku i obecnie obsługuje serwery SSE.

Oto, jak możesz to zrobić:

1. Sklonuj repozytorium:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Uruchom lokalnie, aby przetestować:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Aby spróbować lokalnie, utwórz plik *mcp.json* w katalogu *.vscode* i dodaj następującą zawartość:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  Po uruchomieniu serwera SSE, możesz kliknąć ikonę odtwarzania w pliku JSON, powinieneś teraz zobaczyć, że narzędzia serwera są wykrywane przez GitHub Copilot, zobacz ikonę narzędzi.

1. Aby wdrożyć, uruchom następujące polecenie:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

I już, wdroż to lokalnie lub do Azure krok po kroku.

## Dodatkowe zasoby

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Artykuł o Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repozytorium Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Co dalej

- Dalej: [Zaawansowane tematy serwera](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->