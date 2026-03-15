# Deployen van MCP-servers

Het deployen van je MCP-server stelt anderen in staat toegang te krijgen tot de tools en bronnen buiten je lokale omgeving. Er zijn verschillende deploystrategieën om te overwegen, afhankelijk van je eisen voor schaalbaarheid, betrouwbaarheid en beheergemak. Hieronder vind je richtlijnen voor het deployen van MCP-servers lokaal, in containers en in de cloud.

## Overzicht

Deze les behandelt hoe je je MCP Server-app kunt deployen.

## Leerdoelen

Aan het einde van deze les kun je:

- Verschillende deploybenaderingen evalueren.
- Je app deployen.

## Lokale ontwikkeling en deployment

Als je server bedoeld is om te draaien op de machine van de gebruiker, kun je de volgende stappen volgen:

1. **Download de server**. Als je de server niet hebt geschreven, download deze dan eerst naar je machine.  
1. **Start het serverproces**: Start je MCP serverapplicatie.

Voor SSE (niet nodig voor stdio-type server)

1. **Configureer netwerken**: Zorg ervoor dat de server bereikbaar is op de verwachte poort.  
1. **Verbind clients**: Gebruik lokale connectie-URL's zoals `http://localhost:3000`.

## Cloud Deployment

MCP-servers kunnen worden gedeployed naar verschillende cloudplatforms:

- **Serverless Functions**: Deploy lichte MCP-servers als serverless functies.  
- **Containerservices**: Gebruik services zoals Azure Container Apps, AWS ECS of Google Cloud Run.  
- **Kubernetes**: Deploy en beheer MCP-servers in Kubernetes-clusters voor hoge beschikbaarheid.

### Voorbeeld: Azure Container Apps

Azure Container Apps ondersteunt het deployen van MCP-servers. Dit is nog in ontwikkeling en ondersteunt momenteel SSE-servers.

Zo kun je te werk gaan:

1. Clone een repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Draai het lokaal om het uit te proberen:

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

  Zodra de SSE-server is gestart, kun je op het afspeelicoon in het JSON-bestand klikken. Je zou nu de tools op de server moeten zien die door GitHub Copilot worden opgepikt, zie het Tool-icoon.

1. Om te deployen, voer je het volgende commando uit:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Daar heb je het, deploy lokaal, deploy naar Azure via deze stappen.

## Extra bronnen

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Azure Container Apps artikel](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)  


## Wat is de volgende stap

- Volgende: [Geavanceerde serveronderwerpen](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal geldt als de gezaghebbende bron. Voor kritieke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->