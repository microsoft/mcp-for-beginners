# Nasazení MCP serverů

Nasazení vašeho MCP serveru umožňuje ostatním přístup k jeho nástrojům a zdrojům mimo vaše místní prostředí. Existuje několik strategií nasazení, které je třeba zvážit v závislosti na vašich požadavcích na škálovatelnost, spolehlivost a snadnost správy. Níže najdete pokyny pro nasazení MCP serverů lokálně, v kontejnerech a do cloudu.

## Přehled

Tato lekce pokrývá, jak nasadit vaši aplikaci MCP Server.

## Cíle učení

Na konci této lekce budete schopni:

- Zhodnotit různé přístupy k nasazení.
- Nasadit vaši aplikaci.

## Lokální vývoj a nasazení

Pokud je váš server určen k použití spuštěním na počítači uživatele, můžete postupovat podle těchto kroků:

1. **Stáhněte server**. Pokud jste server nenapsali, stáhněte si jej nejprve do svého počítače.  
1. **Spusťte proces serveru**: Spusťte vaši aplikaci MCP serveru.

Pro SSE (není potřeba pro server typu stdio)

1. **Nakonfigurujte síť**: Zajistěte, že server je přístupný na očekávaném portu.  
1. **Připojte klienty**: Použijte lokální připojovací URL jako `http://localhost:3000`.

## Nasazení do cloudu

MCP servery lze nasadit na různé cloudové platformy:

- **Serverless funkce**: Nasazení lehkých MCP serverů jako serverless funkcí.  
- **Služby kontejnerů**: Použijte služby jako Azure Container Apps, AWS ECS nebo Google Cloud Run.  
- **Kubernetes**: Nasazujte a spravujte MCP servery v Kubernetes clusterech pro vysokou dostupnost.

### Příklad: Azure Container Apps

Azure Container Apps podporují nasazení MCP serverů. Je to stále v procesu vývoje a v současnosti podporuje SSE servery.

Postupujte takto:

1. Naklonujte repozitář:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Spusťte ho lokálně, abyste to otestovali:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Pro lokální vyzkoušení vytvořte soubor *mcp.json* v adresáři *.vscode* a přidejte následující obsah:

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

  Jakmile je SSE server spuštěn, můžete kliknout na ikonu přehrávání v JSON souboru, měli byste nyní vidět nástroje na serveru, které GitHub Copilot rozpoznává, viz ikona nástroje.

1. Pro nasazení spusťte následující příkaz:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

A je to, nasadíte lokálně, nasadíte do Azure podle těchto kroků.

## Další zdroje

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Článek o Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repozitář Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Co bude dál

- Dále: [Pokročilá témata serverů](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o zřeknutí se odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Za jakékoli nedorozumění nebo chybné výklady plynoucí z použití tohoto překladu neneseme odpovědnost.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->