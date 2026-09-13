# MCP serverių diegimas

> [!NOTE]
> Konfigūracijos pavyzdžiai, naudojantys `/sse` pabaigos tašką, taikomi tradiciniam HTTP+SSE
> perdavimui. MCP `2026-07-28` nuotoliniai serveriai naudoja Streamable HTTP, paprastai serveryje
> apibrėžtą pabaigos tašką, pvz., `/mcp`.

Jūsų MCP serverio diegimas leidžia kitiems prieiti prie jo įrankių ir išteklių už jūsų vietinio aplinkos ribų. Yra keletas diegimo strategijų, kurias reikėtų apsvarstyti, atsižvelgiant į jūsų mastelio didinimo, patikimumo ir valdymo paprastumo reikalavimus. Žemiau rasite gaires, kaip diegti MCP serverius vietoje, konteineriuose ir debesyje.

## Apžvalga

Ši pamoka apima, kaip įdiegti savo MCP Server programą.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Įvertinti skirtingus diegimo būdus.
- Įdiegti savo programą.

## Vietinis vystymas ir diegimas

Jei jūsų serveris skirtas naudoti vartotojo kompiuteryje, galite vadovautis šiais žingsniais:

1. **Atsisiųskite serverį**. Jei pats nesukūrėte serverio, pirmiausia atsisiųskite jį į savo kompiuterį.
1. **Paleiskite serverio procesą**: paleiskite MCP serverio programą

SSE atveju (nereikalinga stdio tipo serveriui)

1. **Konfigūruokite tinklą**: įsitikinkite, kad serveris pasiekiamas per numatytą prievadą
1. **Prisijunkite klientus**: naudokite vietinius prisijungimo URL, pvz., `http://localhost:3000`

## Debesų diegimas

MCP serverius galima diegti įvairiose debesų platformose:

- **Serverless funkcijos**: diegti lengvus MCP serverius kaip serverless funkcijas
- **Konteinerių paslaugos**: naudoti paslaugas, tokias kaip Azure Container Apps, AWS ECS arba Google Cloud Run
- **Kubernetes**: diegti ir valdyti MCP serverius Kubernetes klasteriuose dėl didelio prieinamumo

### Pavyzdys: Azure Container Apps

Azure Container Apps palaiko MCP serverių diegimą. Tai vis dar kuriama, ir šiuo metu palaikomi SSE serveriai.

Štai kaip galite tai atlikti:

1. Klonuokite repozitoriją:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Paleiskite vietoje, kad išbandytumėte:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # langai
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Norėdami išbandyti vietoje, sukurkite *mcp.json* failą *.vscode* kataloge ir pridėkite šį turinį:

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

  Kai SSE serveris bus paleistas, galėsite spustelėti grojimo piktogramą JSON faile, dabar turėtumėte matyti įrankius serveryje, kuriuos aptinka GitHub Copilot, žr. įrankio piktogramą.

1. Norėdami įdiegti, vykdykite šią komandą:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Štai ir viskas, įdiekite vietoje arba Azure pagal šiuos žingsnius.

## Papildomi ištekliai

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps straipsnis](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repozitorija](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Kas toliau

- Toliau: [Pažangūs serverio klausimai](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->