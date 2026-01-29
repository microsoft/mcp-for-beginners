# Udrulning af MCP-servere

At udrulle din MCP-server gør det muligt for andre at få adgang til dens værktøjer og ressourcer ud over dit lokale miljø. Der findes flere udrulningsstrategier, afhængigt af dine krav til skalerbarhed, pålidelighed og nem administration. Nedenfor finder du vejledning til at udrulle MCP-servere lokalt, i containere og i skyen.

## Oversigt

Denne lektion gennemgår, hvordan du udruller din MCP Server-app.

## Læringsmål

Når du er færdig med denne lektion, vil du kunne:

- Vurdere forskellige udrulningsmetoder.
- Udrulle din app.

## Lokal udvikling og udrulning

Hvis din server er beregnet til at blive brugt ved at køre på brugerens maskine, kan du følge disse trin:

1. **Download serveren**. Hvis du ikke selv har skrevet serveren, skal du først downloade den til din maskine.  
1. **Start serverprocessen**: Kør din MCP-serverapplikation.

For SSE (ikke nødvendigt for stdio-type server)

1. **Konfigurer netværk**: Sørg for, at serveren er tilgængelig på den forventede port.  
1. **Forbind klienter**: Brug lokale forbindelses-URL’er som `http://localhost:3000`.

## Udrulning i skyen

MCP-servere kan udrulles på forskellige cloud-platforme:

- **Serverless Functions**: Udrul letvægts MCP-servere som serverless functions.  
- **Container Services**: Brug tjenester som Azure Container Apps, AWS ECS eller Google Cloud Run.  
- **Kubernetes**: Udrul og administrer MCP-servere i Kubernetes-klynger for høj tilgængelighed.

### Eksempel: Azure Container Apps

Azure Container Apps understøtter udrulning af MCP-servere. Det er stadig under udvikling, og det understøtter i øjeblikket SSE-servere.

Sådan kan du gøre:

1. Klon et repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Kør det lokalt for at teste:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. For at prøve det lokalt, opret en *mcp.json*-fil i en *.vscode*-mappe og tilføj følgende indhold:

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

  Når SSE-serveren er startet, kan du klikke på afspilningsikonet i JSON-filen. Du skulle nu kunne se, at værktøjerne på serveren bliver opfanget af GitHub Copilot, se værktøjsikonet.

1. For at udrulle, kør følgende kommando:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Sådan! Udrul det lokalt, eller udrul det til Azure via disse trin.

## Yderligere ressourcer

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Azure Container Apps artikel](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)  


## Hvad er det næste

- Næste: [Praktisk implementering](../../04-PracticalImplementation/README.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.