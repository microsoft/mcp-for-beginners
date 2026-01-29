# Deployen van MCP-servers

Het deployen van je MCP-server maakt het mogelijk dat anderen toegang krijgen tot de tools en resources buiten je lokale omgeving. Er zijn verschillende strategieën om te deployen, afhankelijk van je wensen op het gebied van schaalbaarheid, betrouwbaarheid en beheer. Hieronder vind je richtlijnen voor het deployen van MCP-servers lokaal, in containers en in de cloud.

## Overzicht

Deze les behandelt hoe je je MCP Server-app kunt deployen.

## Leerdoelen

Aan het einde van deze les kun je:

- Verschillende deploymethodes beoordelen.
- Je app deployen.

## Lokale ontwikkeling en deployment

Als je server bedoeld is om te draaien op de machine van de gebruiker, kun je de volgende stappen volgen:

1. **Download de server**. Als je de server niet zelf hebt geschreven, download deze dan eerst naar je machine.  
1. **Start het serverproces**: Start je MCP-serverapplicatie.

Voor SSE (niet nodig voor stdio-type server)

1. **Configureer netwerk**: Zorg dat de server bereikbaar is op de verwachte poort.  
1. **Verbind clients**: Gebruik lokale verbindings-URL’s zoals `http://localhost:3000`.

## Cloud Deployment

MCP-servers kunnen worden gedeployed naar verschillende cloudplatformen:

- **Serverless Functions**: Deploy lichte MCP-servers als serverless functies.  
- **Container Services**: Gebruik diensten zoals Azure Container Apps, AWS ECS of Google Cloud Run.  
- **Kubernetes**: Deploy en beheer MCP-servers in Kubernetes-clusters voor hoge beschikbaarheid.

### Voorbeeld: Azure Container Apps

Azure Container Apps ondersteunen het deployen van MCP-servers. Dit is nog in ontwikkeling en ondersteunt momenteel SSE-servers.

Zo pak je het aan:

1. Clone een repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Run het lokaal om te testen:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Om het lokaal te proberen, maak een *mcp.json* bestand aan in een *.vscode* map en voeg de volgende inhoud toe:

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

  Zodra de SSE-server gestart is, kun je op het afspeel-icoon in het JSON-bestand klikken. Je zou nu de tools op de server moeten zien verschijnen in GitHub Copilot, herkenbaar aan het Tool-icoon.

1. Om te deployen, voer het volgende commando uit:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Dat is alles, deploy lokaal of deploy naar Azure via deze stappen.

## Aanvullende bronnen

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Azure Container Apps artikel](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)  

## Wat volgt

- Volgende: [Praktische Implementatie](../../04-PracticalImplementation/README.md)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.