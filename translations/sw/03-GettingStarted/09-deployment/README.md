# Kuweka seva za MCP

> [!NOTE]
> Mifano ya usanidi inayotumia kiungo cha `/sse` inalenga usafirishaji wa zamani wa HTTP+SSE. Seva za mbali za MCP `2026-07-28` hutumia Streamable HTTP, kawaida kwenye kiungo kilichobainishwa na seva kama `/mcp`.
> 


Kuweka seva yako ya MCP kunaruhusu wengine kufikia zana na rasilimali zake zaidi ya mazingira yako ya ndani. Kuna mikakati kadhaa ya uenezaji ya kuzingatia, kutegemea mahitaji yako ya upanuzi, kuaminika, na urahisi wa usimamizi. Hapa chini utapata mwongozo wa kuweka seva za MCP kwa ndani, kwenye kontena, na kwenye wingu.

## Muhtasari

Somo hili linahusu jinsi ya kuweka programu yako ya Seva ya MCP.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kutathmini mbinu tofauti za uenezaji.
- Kuweka programu yako.

## Maendeleo na uenezaji wa ndani

Ikiwa seva yako inapaswa kutumiwa kwa kuendeshwa kwenye kompyuta ya mtumiaji, unaweza kufuata hatua zifuatazo:

1. **Pakua seva**. Ikiwa hujaunda seva hiyo, basi ipakue kwanza kwenye kompyuta yako.
1. **Anza mchakato wa seva**: Endesha programu yako ya seva ya MCP

Kwa SSE (haina haja kwa seva ya aina ya stdio)

1. **Sanidi mtandao**: Hakikisha seva inapatikana kwenye mlango uliootarajiwa
1. **Unganisha wateja**: Tumia URL za uunganisho za ndani kama `http://localhost:3000`

## Uenezaji Wingu

Seva za MCP zinaweza kuwekwa katika majukwaa mbalimbali ya wingu:

- **Serverless Functions**: Weka seva nyepesi za MCP kama huduma zisizo na seva
- **Container Services**: Tumia huduma kama Azure Container Apps, AWS ECS, au Google Cloud Run
- **Kubernetes**: Weka na simamia seva za MCP kwenye magenge ya Kubernetes kwa upatikanaji wa hali ya juu

### Mfano: Azure Container Apps

Azure Container Apps inaunga mkono uenezaji wa seva za MCP. Bado ni kazi inayoendelea na kwa sasa inaunga mkono seva za SSE.

Hapa ni jinsi unavyoweza kuifanya:

1. Nakili repozitori:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Iendeshe kwa ndani kupima mambo:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Ili kuijaribu kwa ndani, tengeneza faili *mcp.json* katika saraka ya *.vscode* na ongeza maudhui yafuatayo:

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

  Mara seva ya SSE itakapozinduliwa, unaweza kubofya ikoni ya kucheza kwenye faili ya JSON, sasa unapaswa kuona zana kwenye seva zikichukuliwa na GitHub Copilot, angalia ikoni ya Zana.

1. Ili kueneza, endesha amri ifuatayo:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Hiyo ndiyo, enezesha kwa ndani, enezesha kwa Azure kupitia hatua hizi.

## Rasilimali Zaidi

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps article](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Nini Kifuatayo

- Kifuatayo: [Advanced Server Topics](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->