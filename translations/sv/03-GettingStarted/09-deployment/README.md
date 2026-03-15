# Distribuera MCP-servrar

Att distribuera din MCP-server gör det möjligt för andra att komma åt dess verktyg och resurser utanför din lokala miljö. Det finns flera distributionsstrategier att överväga beroende på dina krav på skalbarhet, tillförlitlighet och enkel hantering. Nedan hittar du vägledning för att distribuera MCP-servrar lokalt, i containrar och i molnet.

## Översikt

Den här lektionen täcker hur du distribuerar din MCP Server-app.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Utvärdera olika distributionsmetoder.
- Distribuera din app.

## Lokal utveckling och distribution

Om din server är avsedd att användas på användarnas egen dator kan du följa dessa steg:

1. **Ladda ner servern**. Om du inte skrev servern själv, ladda ner den först till din dator.  
1. **Starta serverprocessen**: Kör din MCP-serverapplikation

För SSE (behövs inte för stdio-typ server)

1. **Konfigurera nätverk**: Säkerställ att servern är åtkomlig på förväntad port  
1. **Anslut klienter**: Använd lokala anslutningsadresser som `http://localhost:3000`

## Molndistribution

MCP-servrar kan distribueras till olika molnplattformar:

- **Serverlösa funktioner**: Distribuera lätta MCP-servrar som serverlösa funktioner  
- **Container-tjänster**: Använd tjänster som Azure Container Apps, AWS ECS eller Google Cloud Run  
- **Kubernetes**: Distribuera och hantera MCP-servrar i Kubernetes-kluster för hög tillgänglighet

### Exempel: Azure Container Apps

Azure Container Apps stödjer distribution av MCP-servrar. Det är fortfarande under utveckling och stödjer för närvarande SSE-servrar.

Så här kan du gå tillväga:

1. Klona ett repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Kör det lokalt för att prova:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. För att testa lokalt, skapa en *mcp.json*-fil i en *.vscode*-katalog och lägg till följande innehåll:

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

  När SSE-servern har startat kan du klicka på spela-ikonen i JSON-filen, du bör nu se verktyg på servern som plockas upp av GitHub Copilot, se Verktygsikonen.

1. För att distribuera kör följande kommando:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Där har du det, distribuera lokalt eller distribuera till Azure via dessa steg.

## Ytterligare resurser

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Artikel om Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Vad händer härnäst

- Nästa: [Avancerade serverämnen](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->