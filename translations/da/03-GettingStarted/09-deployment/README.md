# Udrulning af MCP-servere

Udrulning af din MCP-server giver andre adgang til dens værktøjer og ressourcer ud over dit lokale miljø. Der er flere udrulningsstrategier at overveje, afhængigt af dine krav til skalerbarhed, pålidelighed og nem administration. Nedenfor finder du vejledning til at udrulle MCP-servere lokalt, i containere og til skyen.

## Oversigt

Denne lektion gennemgår, hvordan du udruller din MCP Server-app.

## Læringsmål

Ved slutningen af denne lektion vil du kunne:

- Vurdere forskellige udrulningstilgange.
- Udrulle din app.

## Lokal udvikling og udrulning

Hvis din server er beregnet til at blive brugt ved at køre på brugernes maskine, kan du følge følgende trin:

1. **Download serveren**. Hvis du ikke har skrevet serveren, skal du først downloade den til din maskine.
1. **Start serverprocessen**: Kør din MCP serverapplikation.

For SSE (ikke nødvendigt for stdio-type server)

1. **Konfigurer netværk**: Sørg for, at serveren er tilgængelig på den forventede port.
1. **Forbind klienter**: Brug lokale forbindelses-URL'er som `http://localhost:3000`.

## Cloud-udrulning

MCP-servere kan udrulles til forskellige cloud-platforme:

- **Serverløse funktioner**: Udrul letvægts MCP-servere som serverløse funktioner.
- **Containertjenester**: Brug tjenester som Azure Container Apps, AWS ECS eller Google Cloud Run.
- **Kubernetes**: Udrul og administrer MCP-servere i Kubernetes-klynger for høj tilgængelighed.

### Eksempel: Azure Container Apps

Azure Container Apps understøtter udrulning af MCP-servere. Det er stadig et igangværende arbejde, og det understøtter i øjeblikket SSE-servere.

Sådan kan du gøre:

1. Klon et repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Kør det lokalt for at teste tingene:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. For at prøve det lokalt skal du oprette en *mcp.json*-fil i en *.vscode*-mappe og tilføje følgende indhold:

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

  Når SSE-serveren er startet, kan du klikke på afspilningsikonet i JSON-filen, og du burde nu kunne se værktøjer på serveren, der bliver fanget af GitHub Copilot, se værktøjsikonet.

1. For at udrulle, kør følgende kommando:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Så har du det, udrul det lokalt, udrul det til Azure gennem disse trin.

## Yderligere ressourcer

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps artikel](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Hvad er det næste

- Næste: [Avancerede Serveremner](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets originale sprog bør betragtes som den autoritative kilde. For vigtig information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår ved brug af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->