# Nasazení MCP serverů

Nasazení vašeho MCP serveru umožňuje ostatním přístup k jeho nástrojům a zdrojům i mimo vaše lokální prostředí. Existuje několik strategií nasazení, které je třeba zvážit podle vašich požadavků na škálovatelnost, spolehlivost a snadnost správy. Níže najdete pokyny pro nasazení MCP serverů lokálně, v kontejnerech a do cloudu.

## Přehled

Tato lekce pokrývá, jak nasadit vaši aplikaci MCP Server.

## Cíle učení

Na konci této lekce budete schopni:

- Zhodnotit různé přístupy k nasazení.
- Nasadit vaši aplikaci.

## Lokální vývoj a nasazení

Pokud je váš server určen k použití na počítači uživatele, můžete postupovat podle těchto kroků:

1. **Stáhněte server**. Pokud jste server nenapsali, nejprve si ho stáhněte do svého počítače.  
1. **Spusťte serverový proces**: Spusťte vaši MCP serverovou aplikaci.

Pro SSE (není potřeba u serveru typu stdio)

1. **Nakonfigurujte síť**: Ujistěte se, že je server přístupný na očekávaném portu.  
1. **Připojte klienty**: Použijte lokální připojovací URL jako `http://localhost:3000`.

## Nasazení do cloudu

MCP servery lze nasadit na různé cloudové platformy:

- **Serverless Functions**: Nasazení lehkých MCP serverů jako serverless funkcí  
- **Container Services**: Použití služeb jako Azure Container Apps, AWS ECS nebo Google Cloud Run  
- **Kubernetes**: Nasazení a správa MCP serverů v Kubernetes clusterech pro vysokou dostupnost

### Příklad: Azure Container Apps

Azure Container Apps podporují nasazení MCP serverů. Je to stále ve vývoji a aktuálně podporuje SSE servery.

Zde je postup, jak na to:

1. Naklonujte repozitář:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Spusťte ho lokálně pro otestování:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Pro lokální test vytvořte soubor *mcp.json* ve složce *.vscode* a přidejte následující obsah:

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

  Jakmile je SSE server spuštěn, můžete kliknout na ikonu přehrávání v JSON souboru, nyní by měly být nástroje na serveru rozpoznány GitHub Copilotem, viz ikona nástroje.

1. Pro nasazení spusťte následující příkaz:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

A je to, nasadíte ho lokálně i do Azure podle těchto kroků.

## Další zdroje

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Článek o Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repo Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Co dál

- Další: [Praktická implementace](../../04-PracticalImplementation/README.md)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.