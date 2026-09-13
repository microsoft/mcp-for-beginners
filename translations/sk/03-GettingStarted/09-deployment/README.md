# Nasadenie MCP serverov

> [!NOTE]
> Konfiguračné príklady používajúce `/sse` endpoint cielia na staršiu HTTP+SSE
> transportnú vrstvu. Vzdialené MCP servery `2026-07-28` používajú Streamable HTTP, bežne na
> serverom definovanom endpoint-e, napríklad `/mcp`.

Nasadenie vášho MCP servera umožní ostatným pristupovať k jeho nástrojom a zdrojom mimo vášho lokálneho prostredia. Existuje niekoľko stratégií nasadenia, ktoré treba zvážiť v závislosti od vašich požiadaviek na škálovateľnosť, spoľahlivosť a jednoduchosť správy. Nižšie nájdete usmernenia pre nasadenie MCP serverov lokálne, v kontajneroch a do cloudu.

## Prehľad

Táto lekcia pokrýva, ako nasadiť vašu MCP Server aplikáciu.

## Ciele učenia

Na konci tejto lekcie budete vedieť:

- Zhodnotiť rôzne prístupy k nasadeniu.
- Nasadiť vašu aplikáciu.

## Lokálny vývoj a nasadenie

Ak má váš server bežať na používateľovom počítači, môžete nasledovať tieto kroky:

1. **Stiahnite server**. Ak ste server nenapísali vy, najprv si ho stiahnite do vášho počítača.
1. **Spustite serverový proces**: Spustite vašu MCP serverovú aplikáciu.

Pre SSE (nie je potrebné pre stdio typ servera)

1. **Nakonfigurujte sieťovanie**: Uistite sa, že server je prístupný na očakávanom porte.
1. **Pripojte klientov**: Použite lokálne pripojovacie URL ako `http://localhost:3000`.

## Nasadenie do cloudu

MCP servery môžu byť nasadené na rôzne cloudové platformy:

- **Serverless funkcie**: Nasadzujte ľahké MCP servery ako serverless funkcie.
- **Kontajnerové služby**: Používajte služby ako Azure Container Apps, AWS ECS alebo Google Cloud Run.
- **Kubernetes**: Nasadzujte a spravujte MCP servery v Kubernetes klastroch pre vysokú dostupnosť.

### Príklad: Azure Container Apps

Azure Container Apps podporujú nasadenie MCP serverov. Je to stále vo vývoji a momentálne podporuje SSE servery.

Takto na to môžete ísť:

1. Naklonujte repozitár:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Spustite ho lokálne, aby ste si veci otestovali:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Ak chcete vyskúšať lokálne, vytvorte súbor *mcp.json* v priečinku *.vscode* a pridajte nasledujúci obsah:

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

  Po spustení SSE servera môžete kliknúť na ikonu prehrávania v JSON súbore, teraz by ste mali vidieť, že nástroje na serveri sú detekované GitHub Copilotom, pozrite ikonu nástroja.

1. Pre nasadenie spustite nasledujúci príkaz:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Máte hotovo, nasadte to lokálne alebo do Azure podľa týchto krokov.

## Ďalšie zdroje

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Článok o Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repozitár](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Čo bude ďalej

- Ďalej: [Pokročilé témy servera](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->