# Kuweka Seva za MCP

Kuweka seva yako ya MCP kunaruhusu wengine kufikia zana na rasilimali zake zaidi ya mazingira yako ya eneo la kazi. Kuna mikakati mbalimbali ya kuweka huduma inayopaswa kuzingatiwa, kulingana na mahitaji yako ya upanuzi, uaminifu, na urahisi wa usimamizi. Hapa chini utapata mwongozo wa kuweka seva za MCP kwa karibu, katika vyombo, na kwenye wingu.

## Muhtasari

Somo hili linaelezea jinsi ya kuweka programu yako ya MCP Server.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kutathmini mbinu tofauti za kuweka huduma.
- Kuweka programu yako.

## Maendeleo ya Kieneo na Uwekaji Huduma

Ikiwa seva yako inakusudiwa kutumiwa kwa kuendeshwa kwenye kompyuta za watumiaji, unaweza kufuata hatua zifuatazo:

1. **Pakua seva**. Ikiwa hukutunga seva, basi pakua kwanza kwenye kompyuta yako.  
1. **Anzisha mchakato wa seva**: Endesha programu yako ya MCP Server 

Kwa SSE (haihitajiki kwa seva aina ya stdio)

1. **Panga mtandao**: Hakikisha seva inapatikana kwenye mlangoni uliotegemewa  
1. **Unganisha wateja**: Tumia URL za muunganisho wa eneo kama `http://localhost:3000`

## Uwekaji Huduma Wingu

Seva za MCP zinaweza kuwekwa kwenye majukwaa mbalimbali ya wingu:

- **Fungua Mifumo Isiyo na Seva (Serverless Functions)**: Weka seva za MCP nyepesi kama mifumo isiyo na seva
- **Huduma za Vyombo**: Tumia huduma kama Azure Container Apps, AWS ECS, au Google Cloud Run
- **Kubernetes**: Weka na simamia seva za MCP katika makundi ya Kubernetes kwa upatikanaji wa hali ya juu

### Mfano: Azure Container Apps

Azure Container Apps inaunga mkono kuweka Seva za MCP. Bado ni kazi inayoendelea na kwa sasa inaunga mkono seva za SSE.

Hapa ni jinsi ya kuifanya:

1. Nakili repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Ikiendeshe kwa karibu kujaribu mambo:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Ili kujaribu kwa karibu, tengeneza faili *mcp.json* katika saraka ya *.vscode* na ongeza maudhui yafuatayo:

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

  Mara seva ya SSE inapozinduliwa, unaweza kubofya ikoni ya kucheza kwenye faili ya JSON, sasa unapaswa kuona zana kwenye seva zikichukuliwa na GitHub Copilot, angalia ikoni ya Zana.

1. Kwa ajili ya kuweka huduma, endesha amri ifuatayo:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Hivyo ndivyo ulivyo, weka huduma kwa karibu, weka kwenye Azure kupitia hatua hizi.

## Rasilimali Zaidi

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Makala ya Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repo ya Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Nini Kinafuata

- Ifuatayo: [Mada za Seva za Juu Zaidi](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tangazo la Kutojulikana**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za otomatiki zinaweza kuwa na makosa au upotovu wa maana. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo halali. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inashauriwa. Hatuwajibiki kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->