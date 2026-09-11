# MCP-servers implementeren

> [!NOTE]
> Configuratievoorbeelden die een `/sse` endpoint gebruiken richten zich op het legacy HTTP+SSE
> transport. MCP `2026-07-28` externe servers gebruiken Streamable HTTP, normaal gesproken op een
> door de server gedefinieerd endpoint zoals `/mcp`.

Het implementeren van je MCP-server stelt anderen in staat om toegang te krijgen tot de tools en bronnen ervan buiten je lokale omgeving. Er zijn verschillende implementatiestrategieën om te overwegen, afhankelijk van je vereisten voor schaalbaarheid, betrouwbaarheid en beheerbaarheid. Hieronder vind je richtlijnen voor het lokaal, in containers en in de cloud implementeren van MCP-servers.

## Overzicht

Deze les behandelt hoe je je MCP Server-app implementeert.

## Leerdoelen

Aan het einde van deze les kun je:

- Verschillende implementatie-aanpakken evalueren.
- Je app implementeren.

## Lokale ontwikkeling en implementatie

Als je server bedoeld is om op de machines van gebruikers te draaien, kun je de volgende stappen volgen:

1. **Download de server**. Als jij de server niet hebt geschreven, download deze dan eerst naar je machine.
1. **Start het serverproces**: Start je MCP serverapplicatie

Voor SSE (niet nodig voor stdio-type server)

1. **Configureer networking**: Zorg dat de server bereikbaar is op de verwachte poort
1. **Verbind clients**: Gebruik lokale verbindings-URL's zoals `http://localhost:3000`

## Cloud-implementatie

MCP-servers kunnen worden geïmplementeerd op verschillende cloudplatformen:

- **Serverless Functions**: Implementeer lichtgewicht MCP-servers als serverloze functies
- **Container Services**: Gebruik services zoals Azure Container Apps, AWS ECS of Google Cloud Run
- **Kubernetes**: Implementeer en beheer MCP-servers in Kubernetes-clusters voor hoge beschikbaarheid

### Voorbeeld: Azure Container Apps

Azure Container Apps ondersteunen het implementeren van MCP-servers. Het is nog in ontwikkeling en ondersteunt momenteel SSE-servers.

Zo ga je te werk:

1. Clone een repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Test het lokaal:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Maak om het lokaal te proberen een *mcp.json*-bestand aan in een *.vscode*-map en voeg de volgende inhoud toe:

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

  Zodra de SSE-server is gestart, kun je op het afspeel-icoon in het JSON-bestand klikken; je zou nu tools op de server moeten zien worden opgepikt door GitHub Copilot, kijk naar het Tool-icoon.

1. Om te implementeren, voer je het volgende commando uit:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Dat is het, implementeer het lokaal, implementeer het op Azure via deze stappen.

## Aanvullende bronnen

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Artikel over Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Wat Nu

- Volgende: [Geavanceerde Serveronderwerpen](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->