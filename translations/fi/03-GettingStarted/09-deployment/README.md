# MCP-palvelimien käyttöönotto

MCP-palvelimen käyttöönotto mahdollistaa sen työkalujen ja resurssien käytön paikallisen ympäristösi ulkopuolella. Käyttöönottoon on useita strategioita, riippuen vaatimuksistasi skaalautuvuuden, luotettavuuden ja hallinnan helppouden suhteen. Alla löydät ohjeita MCP-palvelimien käyttöönottoon paikallisesti, konteissa ja pilveen.

## Yleiskatsaus

Tässä oppitunnissa käsitellään, miten MCP Server -sovelluksesi otetaan käyttöön.

## Oppimistavoitteet

Oppitunnin lopuksi osaat:

- Arvioida erilaisia käyttöönotto lähestymistapoja.
- Ottaa sovelluksesi käyttöön.

## Paikallinen kehitys ja käyttöönotto

Jos palvelimesi on tarkoitettu käytettäväksi käyttäjän koneella, voit seurata seuraavia vaiheita:

1. **Lataa palvelin**. Jos et itse kirjoittanut palvelinta, lataa se ensin koneellesi.  
1. **Käynnistä palvelinprosessi**: Käynnistä MCP-palvelinsovelluksesi 

SSE:lle (ei tarvita stdio-tyyppiselle palvelimelle)

1. **Konfiguroi verkko**: Varmista, että palvelimeen pääsee odotetulla portilla  
1. **Yhdistä asiakkaat**: Käytä paikallisia URL-osoitteita kuten `http://localhost:3000`

## Pilvikäyttöönotto

MCP-palvelimia voidaan ottaa käyttöön erilaisilla pilvialustoilla:

- **Serverless Functions**: Ota käyttöön kevyitä MCP-palvelimia serverless-toimintoina
- **Konttipalvelut**: Käytä palveluita kuten Azure Container Apps, AWS ECS tai Google Cloud Run
- **Kubernetes**: Ota käyttöön ja hallitse MCP-palvelimia Kubernetes-klustereissa korkean käytettävyyden varmistamiseksi

### Esimerkki: Azure Container Apps

Azure Container Apps tukee MCP-palvelimien käyttöönottoa. Se on vielä työn alla, ja tällä hetkellä se tukee SSE-palvelimia.

Näin voit toimia:

1. Kloonaa repositorio:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Käynnistä se paikallisesti testataksesi:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Jotta voit kokeilla paikallisesti, luo *mcp.json* tiedosto *.vscode* hakemistoon ja lisää seuraava sisältö:

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

  Kun SSE-palvelin on käynnistetty, voit klikata JSON-tiedostossa play-kuvaketta, ja nyt GitHub Copilot tunnistaa palvelimella olevat työkalut, katso työkalukuvaketta.

1. Ota käyttöön suorittamalla seuraava komento:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Siinä se, käytä nämä vaiheet ottaaksesi palvelimen käyttöön paikallisesti tai Azureen.

## Lisäresurssit

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps artikkeli](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Seuraavaksi

- Seuraava: [Advanced Server Topics](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälykäännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoriteettisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä johtuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->