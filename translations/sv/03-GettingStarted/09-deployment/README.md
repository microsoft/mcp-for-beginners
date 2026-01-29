# Distribuera MCP-servrar

Att distribuera din MCP-server gör det möjligt för andra att få tillgång till dess verktyg och resurser utanför din lokala miljö. Det finns flera distributionsstrategier att överväga, beroende på dina krav på skalbarhet, tillförlitlighet och enkel hantering. Nedan hittar du vägledning för att distribuera MCP-servrar lokalt, i containrar och i molnet.

## Översikt

Den här lektionen handlar om hur du distribuerar din MCP Server-app.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Utvärdera olika distributionsmetoder.
- Distribuera din app.

## Lokal utveckling och distribution

Om din server är avsedd att användas genom att köras på användarens dator kan du följa dessa steg:

1. **Ladda ner servern**. Om du inte har skrivit servern själv, ladda ner den först till din dator.  
1. **Starta serverprocessen**: Kör din MCP-serverapplikation.

För SSE (behövs inte för stdio-typ av server)

1. **Konfigurera nätverk**: Se till att servern är tillgänglig på den förväntade porten.  
1. **Anslut klienter**: Använd lokala anslutningsadresser som `http://localhost:3000`.

## Molndistribution

MCP-servrar kan distribueras till olika molnplattformar:

- **Serverless Functions**: Distribuera lätta MCP-servrar som serverlösa funktioner.  
- **Container Services**: Använd tjänster som Azure Container Apps, AWS ECS eller Google Cloud Run.  
- **Kubernetes**: Distribuera och hantera MCP-servrar i Kubernetes-kluster för hög tillgänglighet.

### Exempel: Azure Container Apps

Azure Container Apps stödjer distribution av MCP-servrar. Det är fortfarande under utveckling och stöder för närvarande SSE-servrar.

Så här kan du gå tillväga:

1. Klona ett repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Kör det lokalt för att testa:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. För att testa lokalt, skapa en *mcp.json*-fil i en *.vscode*-mapp och lägg till följande innehåll:

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

  När SSE-servern har startat kan du klicka på play-ikonen i JSON-filen, du bör nu se att verktygen på servern plockas upp av GitHub Copilot, se verktygsikonen.

1. För att distribuera, kör följande kommando:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Där har du det, distribuera lokalt eller till Azure med dessa steg.

## Ytterligare resurser

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Azure Container Apps artikel](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)  

## Vad händer härnäst

- Nästa: [Praktisk implementering](../../04-PracticalImplementation/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.