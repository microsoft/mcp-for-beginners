# MCP serverių diegimas

Diegdami savo MCP serverį leidžiate kitiems naudotis jo įrankiais ir ištekliais ne tik jūsų vietinėje aplinkoje. Yra keli diegimo strategijų variantai, priklausomai nuo jūsų reikalavimų skalabilumui, patikimumui ir valdymo paprastumui. Žemiau rasite rekomendacijas MCP serverių diegimui vietoje, konteineriuose ir debesyje.

## Apžvalga

Ši pamoka apima, kaip diegti jūsų MCP Server programėlę.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Įvertinti skirtingus diegimo metodus.
- Diegti savo programėlę.

## Vietinis kūrimas ir diegimas

Jei jūsų serveris skirtas naudoti vartotojo mašinoje, galite vadovautis šiomis instrukcijomis:

1. **Atsisiųskite serverį**. Jei serverio nerašėte patys, pirmiausia atsisiųskite jį į savo kompiuterį.  
1. **Paleiskite serverio procesą**: Paleiskite jūsų MCP serverio programą

SSE atveju (nereikalinga stdio tipo serveriui)

1. **Konfigūruokite tinklą**: Užtikrinkite, kad serveris būtų pasiekiamas per numatytą prievadą  
1. **Prijunkite klientus**: Naudokite vietinius prisijungimo URL, pvz., `http://localhost:3000`

## Debesų diegimas

MCP serverius galima diegti įvairiose debesų platformose:

- **Serverless funkcijos**: Diegti lengvus MCP serverius kaip serverless funkcijas  
- **Konteinerių paslaugos**: Naudokite paslaugas kaip Azure Container Apps, AWS ECS arba Google Cloud Run  
- **Kubernetes**: Diegti ir valdyti MCP serverius Kubernetes klasteriuose, siekiant aukšto prieinamumo

### Pavyzdys: Azure Container Apps

Azure Container Apps palaiko MCP serverių diegimą. Tai dar yra kuriama funkcija ir šiuo metu palaikomi SSE serveriai.

Štai kaip galite tai padaryti:

1. Atsiųskite repozitoriją:

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

  Kai SSE serveris bus paleistas, spustelėkite grojimo piktogramą JSON faile, ir turėtumėte matyti, kad GitHub Copilot aptinka serverio įrankius, žr. įrankio piktogramą.

1. Norėdami diegti, vykdykite šią komandą:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Štai ir viskas – diegiate vietoje arba diegiate į Azure atlikdami šiuos veiksmus.

## Papildomi ištekliai

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps straipsnis](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repozitorija](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Kas toliau

- Toliau: [Pažangios serverio temos](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingus interpretavimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->