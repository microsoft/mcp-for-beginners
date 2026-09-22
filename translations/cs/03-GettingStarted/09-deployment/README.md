# Nasazení MCP serverů

> [!NOTE]
> Příklady konfigurace, které používají koncový bod `/sse`, cílí na starší transport HTTP+SSE. Vzdálení MCP servery verze `2026-07-28` používají Streamable HTTP, obvykle na koncovém bodě definovaném serverem, jako je `/mcp`.
> transport. MCP `2026-07-28` remote servers use Streamable HTTP, normally at a
> server-defined endpoint such as `/mcp`.

Nasazení vašeho MCP serveru umožňuje ostatním přístup k jeho nástrojům a zdrojům mimo vaše lokální prostředí. Existuje několik strategií nasazení v závislosti na vašich požadavcích na škálovatelnost, spolehlivost a jednoduchost správy. Níže najdete pokyny pro nasazení MCP serverů lokálně, v kontejnerech a do cloudu.

## Přehled

Tato lekce pokrývá, jak nasadit vaši MCP Server aplikaci.

## Výukové cíle

Na konci této lekce budete schopni:

- Vyhodnotit různé přístupy k nasazení.
- Nasadit vaši aplikaci.

## Lokální vývoj a nasazení

Pokud je váš server určen k použití na zařízeních uživatelů, můžete postupovat takto:

1. **Stáhnout server**. Pokud jste server nenapsali, stáhněte si ho nejprve do svého počítače.
1. **Spustit serverový proces**: Spusťte vaši MCP serverovou aplikaci

Pro SSE (není potřeba u serveru typu stdio)

1. **Nakonfigurovat síťování**: Ujistěte se, že je server přístupný na očekávaném portu
1. **Připojit klienty**: Použijte lokální připojovací URL jako `http://localhost:3000`

## Nasazení do cloudu

MCP servery lze nasadit na různých cloudových platformách:

- **Serverless funkce**: Nasadit lehké MCP servery jako serverless funkce
- **Kontejnerové služby**: Použít služby jako Azure Container Apps, AWS ECS nebo Google Cloud Run
- **Kubernetes**: Nasadit a spravovat MCP servery v Kubernetes klastrech pro vysokou dostupnost

### Příklad: Azure Container Apps

Azure Container Apps podporují nasazení MCP serverů. Jedná se stále o průběžnou práci a aktuálně podporují SSE servery.

Zde je, jak na to:

1. Naklonujte repozitář:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Spusťte to lokálně, abyste věci otestovali:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Pro pokus lokálně vytvořte soubor *mcp.json* v adresáři *.vscode* a přidejte následující obsah:

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

  Jakmile je SSE server spuštěn, můžete kliknout na ikonu přehrávání v JSON souboru, nyní byste měli vidět, že nástroje na serveru jsou rozpoznávány GitHub Copilotem, viz ikona nástroje.

1. Pro nasazení spusťte následující příkaz:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

A máte hotovo, nasaďte to lokálně nebo nasadit do Azure podle těchto kroků.

## Další zdroje

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Článek o Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repozitář Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Co dál

- Dále: [Pokročilá témata serveru](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->