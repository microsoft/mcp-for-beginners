<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1d9dc83260576b76f272d330ed93c51f",
  "translation_date": "2025-08-26T16:50:50+00:00",
  "source_file": "03-GettingStarted/09-deployment/README.md",
  "language_code": "lt"
}
-->
# MCP serverių diegimas

MCP serverio diegimas leidžia kitiems naudotis jo įrankiais ir ištekliais už jūsų vietinės aplinkos ribų. Yra keletas diegimo strategijų, kurias galite apsvarstyti, priklausomai nuo jūsų poreikių dėl mastelio, patikimumo ir valdymo paprastumo. Žemiau rasite rekomendacijas, kaip diegti MCP serverius vietoje, konteineriuose ir debesyje.

## Apžvalga

Ši pamoka apima MCP serverio programos diegimą.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Įvertinti skirtingus diegimo metodus.
- Įdiegti savo programą.

## Vietinis kūrimas ir diegimas

Jei jūsų serveris skirtas naudoti vartotojų kompiuteriuose, galite atlikti šiuos veiksmus:

1. **Atsisiųskite serverį**. Jei serverio nesukūrėte patys, pirmiausia atsisiųskite jį į savo kompiuterį.
1. **Paleiskite serverio procesą**: Paleiskite savo MCP serverio programą.

SSE atveju (nereikia stdio tipo serveriui):

1. **Konfigūruokite tinklą**: Įsitikinkite, kad serveris pasiekiamas numatytu prievadu.
1. **Prisijunkite klientus**: Naudokite vietinius prisijungimo URL, pvz., `http://localhost:3000`.

## Diegimas debesyje

MCP serveriai gali būti diegiami įvairiose debesų platformose:

- **Serverless funkcijos**: Diekite lengvus MCP serverius kaip serverless funkcijas.
- **Konteinerių paslaugos**: Naudokite tokias paslaugas kaip Azure Container Apps, AWS ECS ar Google Cloud Run.
- **Kubernetes**: Diekite ir valdykite MCP serverius Kubernetes klasteriuose, siekiant užtikrinti aukštą prieinamumą.

### Pavyzdys: Azure Container Apps

Azure Container Apps palaiko MCP serverių diegimą. Šiuo metu tai dar vystoma ir palaiko SSE serverius.

Štai kaip tai padaryti:

1. Nukopijuokite saugyklą:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Paleiskite ją vietoje, kad patikrintumėte:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
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

  Kai SSE serveris bus paleistas, galite spustelėti paleidimo piktogramą JSON faile. Dabar turėtumėte matyti, kaip įrankiai serveryje yra aptinkami GitHub Copilot, matysite Įrankio piktogramą.

1. Norėdami diegti, paleiskite šią komandą:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Štai ir viskas – diekite vietoje, diekite į Azure naudodamiesi šiais žingsniais.

## Papildomi ištekliai

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps straipsnis](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP saugykla](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Kas toliau

- Toliau: [Praktinis įgyvendinimas](../../04-PracticalImplementation/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipiame dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudotis profesionalių vertėjų paslaugomis. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.