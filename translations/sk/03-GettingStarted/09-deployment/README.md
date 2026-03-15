# Nasadzovanie MCP serverov

Nasadenie vášho MCP servera umožňuje ostatným prístup k jeho nástrojom a zdrojom mimo vášho miestneho prostredia. Existuje niekoľko stratégií nasadenia, ktoré treba zvážiť v závislosti od vašich požiadaviek na škálovateľnosť, spoľahlivosť a jednoduché riadenie. Nižšie nájdete pokyny pre nasadenie MCP serverov lokálne, v kontajneroch a do cloudu.

## Prehľad

Táto lekcia pokrýva, ako nasadiť vašu aplikáciu MCP Server.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Zhodnotiť rôzne prístupy nasadenia.
- Nasadiť vašu aplikáciu.

## Lokálny vývoj a nasadenie

Ak je váš server určený na použitie spustením na stroji používateľa, môžete postupovať podľa nasledujúcich krokov:

1. **Stiahnite server**. Ak ste server nenapísali, najprv si ho stiahnite do svojho počítača.  
1. **Spustite proces servera**: Spustite vašu MCP server aplikáciu

Pre SSE (nie je potrebné pre stdio typ servera)

1. **Nastavte sieťovanie**: Zabezpečte, aby bol server prístupný na očakávanom porte  
1. **Pripojte klientov**: Použite lokálne pripojovacie URL ako `http://localhost:3000`

## Nasadenie do cloudu

MCP servery môžu byť nasadené na rôznych cloudových platformách:

- **Serverless funkcie**: Nasadzujte ľahké MCP servery ako serverless funkcie
- **Kontajnerové služby**: Používajte služby ako Azure Container Apps, AWS ECS alebo Google Cloud Run
- **Kubernetes**: Nasadzujte a spravujte MCP servery v Kubernetes klastroch pre vysokú dostupnosť

### Príklad: Azure Container Apps

Azure Container Apps podporuje nasadenie MCP Serverov. Je to stále vo vývoji a momentálne podporuje SSE servery.

Tu je postup, ako na to:

1. Klonujte repozitár:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Spustite to lokálne, aby ste si to otestovali:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Ak to chcete skúsiť lokálne, vytvorte súbor *mcp.json* v adresári *.vscode* a pridajte nasledujúci obsah:

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

  Keď je SSE server spustený, môžete kliknúť na ikonu spustenia v JSON súbore, teraz by ste mali vidieť, že nástroje na serveri sú zaregistrované GitHub Copilotom, pozrite sa na ikonu Nástroj.

1. Na nasadenie spustite nasledujúci príkaz:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Máte to, nasadíte to lokálne alebo do Azure podľa týchto krokov.

## Dodatočné zdroje

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Článok o Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repozitár](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Čo bude ďalej

- Ďalej: [Pokročilé témy serverov](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Výhrada zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->