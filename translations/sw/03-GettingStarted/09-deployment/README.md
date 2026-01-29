# Kuweka seva za MCP

Kuweka seva yako ya MCP kunawawezesha wengine kufikia zana na rasilimali zake zaidi ya mazingira yako ya ndani. Kuna mikakati kadhaa ya kuweka seva unayoweza kuzingatia, kulingana na mahitaji yako ya upanuzi, uaminifu, na urahisi wa usimamizi. Hapa chini utapata mwongozo wa kuweka seva za MCP kwa njia ya ndani, kwenye kontena, na kwenye wingu.

## Muhtasari

Somo hili linashughulikia jinsi ya kuweka programu yako ya MCP Server.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kutathmini mbinu tofauti za kuweka seva.
- Kuweka programu yako.

## Maendeleo na kuweka kwa ndani

Kama seva yako inakusudiwa kutumika kwa kuendeshwa kwenye mashine za watumiaji, unaweza kufuata hatua zifuatazo:

1. **Pakua seva**. Kama hujaandika seva hiyo, pakua kwanza kwenye mashine yako.  
1. **Anzisha mchakato wa seva**: Endesha programu yako ya MCP server

Kwa SSE (si lazima kwa seva ya aina ya stdio)

1. **Sanidi mtandao**: Hakikisha seva inapatikana kwenye bandari inayotarajiwa  
1. **Unganisha wateja**: Tumia URL za muunganisho wa ndani kama `http://localhost:3000`

## Kuweka kwenye Wingu

Seva za MCP zinaweza kuwekwa kwenye majukwaa mbalimbali ya wingu:

- **Serverless Functions**: Weka seva nyepesi za MCP kama serverless functions  
- **Huduma za Kontena**: Tumia huduma kama Azure Container Apps, AWS ECS, au Google Cloud Run  
- **Kubernetes**: Weka na simamia seva za MCP kwenye makundi ya Kubernetes kwa upatikanaji wa hali ya juu

### Mfano: Azure Container Apps

Azure Container Apps inaunga mkono kuweka seva za MCP. Hii bado ni kazi inayoendelea na kwa sasa inaunga mkono seva za SSE.

Hivi ndivyo unavyoweza kuifanya:

1. Nakili repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Iendeshe kwa ndani kujaribu mambo:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Ili kujaribu kwa ndani, tengeneza faili *mcp.json* katika saraka ya *.vscode* na ongeza maudhui yafuatayo:

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

  Mara seva ya SSE itakapozinduliwa, unaweza kubofya ikoni ya kucheza kwenye faili la JSON, sasa utaona zana kwenye seva zikichukuliwa na GitHub Copilot, angalia ikoni ya Zana.

1. Ili kuweka, endesha amri ifuatayo:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Hapo unao, weka kwa ndani, weka kwenye Azure kupitia hatua hizi.

## Rasilimali Zaidi

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Makala ya Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repo ya Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Nini Kifuatacho

- Ifuatayo: [Utekelezaji wa Kivitendo](../../04-PracticalImplementation/README.md)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.