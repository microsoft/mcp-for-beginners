# Wdrażanie serwerów MCP

Wdrażanie serwera MCP pozwala innym na dostęp do jego narzędzi i zasobów poza Twoim lokalnym środowiskiem. Istnieje kilka strategii wdrażania do rozważenia, w zależności od Twoich wymagań dotyczących skalowalności, niezawodności i łatwości zarządzania. Poniżej znajdziesz wskazówki dotyczące wdrażania serwerów MCP lokalnie, w kontenerach oraz w chmurze.

## Przegląd

Ta lekcja obejmuje sposób wdrażania aplikacji serwera MCP.

## Cele nauki

Pod koniec tej lekcji będziesz umiał:

- Ocenić różne podejścia do wdrożenia.
- Wdrożyć swoją aplikację.

## Lokalny rozwój i wdrożenie

Jeśli serwer ma być używany na komputerach użytkowników, możesz postępować według poniższych kroków:

1. **Pobierz serwer**. Jeśli nie napisałeś serwera, najpierw pobierz go na swój komputer.  
1. **Uruchom proces serwera**: Uruchom aplikację serwera MCP.

Dla SSE (niepotrzebne dla serwera typu stdio)

1. **Skonfiguruj sieć**: Upewnij się, że serwer jest dostępny na oczekiwanym porcie  
1. **Połącz klientów**: Używaj lokalnych adresów URL, takich jak `http://localhost:3000`

## Wdrażanie w chmurze

Serwery MCP można wdrażać na różnych platformach chmurowych:

- **Funkcje serverless**: Wdrażaj lekkie serwery MCP jako funkcje serverless  
- **Usługi kontenerowe**: Używaj usług takich jak Azure Container Apps, AWS ECS lub Google Cloud Run  
- **Kubernetes**: Wdrażaj i zarządzaj serwerami MCP w klastrach Kubernetes dla wysokiej dostępności

### Przykład: Azure Container Apps

Azure Container Apps obsługuje wdrażanie serwerów MCP. To nadal praca w toku i obecnie obsługuje serwery SSE.

Oto jak możesz to zrobić:

1. Sklonuj repozytorium:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Uruchom go lokalnie, aby przetestować działanie:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Aby uruchomić lokalnie, stwórz plik *mcp.json* w katalogu *.vscode* i dodaj następującą zawartość:

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

  Po uruchomieniu serwera SSE możesz kliknąć ikonę odtwarzania w pliku JSON, powinieneś teraz zobaczyć, że narzędzia na serwerze są wykrywane przez GitHub Copilot, zobacz ikonę Narzędzia. 

1. Aby wdrożyć, uruchom następujące polecenie:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Oto masz, wdroż go lokalnie lub wdroż do Azure według tych kroków.

## Dodatkowe zasoby

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Artykuł o Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repozytorium MCP Azure Container Apps](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Co dalej

- Dalej: [Zaawansowane tematy serwera](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Źródłem ostatecznym i wiążącym jest oryginalny dokument w języku źródłowym. W przypadku informacji o krytycznym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->