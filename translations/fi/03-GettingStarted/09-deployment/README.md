# MCP-palvelimien käyttöönotto

MCP-palvelimen käyttöönotto mahdollistaa sen työkalujen ja resurssien käytön myös paikallisen ympäristösi ulkopuolella. Käyttöönottoon on useita strategioita, jotka kannattaa valita tarpeidesi mukaan skaalautuvuuden, luotettavuuden ja hallinnan helppouden perusteella. Alta löydät ohjeet MCP-palvelimien käyttöönottoon paikallisesti, konteissa ja pilvessä.

## Yleiskatsaus

Tässä oppitunnissa käydään läpi, miten MCP Server -sovellus otetaan käyttöön.

## Oppimistavoitteet

Oppitunnin lopuksi osaat:

- Arvioida erilaisia käyttöönoton tapoja.
- Ottaa sovelluksesi käyttöön.

## Paikallinen kehitys ja käyttöönotto

Jos palvelimesi on tarkoitettu käytettäväksi käyttäjän koneella, voit noudattaa seuraavia vaiheita:

1. **Lataa palvelin**. Jos et ole itse kirjoittanut palvelinta, lataa se ensin koneellesi.  
1. **Käynnistä palvelinprosessi**: Suorita MCP Server -sovelluksesi.

SSE:tä varten (ei tarvita stdio-tyyppiselle palvelimelle)

1. **Määritä verkkoasetukset**: Varmista, että palvelin on saavutettavissa odotetulla portilla.  
1. **Yhdistä asiakkaat**: Käytä paikallisia yhteysosoitteita, kuten `http://localhost:3000`.

## Pilvikäyttöönotto

MCP-palvelimia voi ottaa käyttöön useilla pilvialustoilla:

- **Serverless Functions**: Ota käyttöön kevyitä MCP-palvelimia serverless-funktioina.  
- **Container Services**: Käytä palveluita kuten Azure Container Apps, AWS ECS tai Google Cloud Run.  
- **Kubernetes**: Ota MCP-palvelimet käyttöön ja hallitse niitä Kubernetes-klustereissa korkean käytettävyyden takaamiseksi.

### Esimerkki: Azure Container Apps

Azure Container Apps tukee MCP-palvelimien käyttöönottoa. Se on vielä kehitysvaiheessa ja tukee tällä hetkellä SSE-palvelimia.

Näin voit toimia:

1. Kloonaa repositorio:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Suorita se paikallisesti testataksesi:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Kokeillaksesi paikallisesti, luo *mcp.json* -tiedosto *.vscode* -hakemistoon ja lisää seuraava sisältö:

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

  Kun SSE-palvelin on käynnistetty, voit klikata JSON-tiedoston toistopainiketta. Nyt GitHub Copilot tunnistaa palvelimen työkalut, katso työkalukuvaketta.

1. Käyttöönottoa varten suorita seuraava komento:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Siinä se, ota palvelin käyttöön paikallisesti tai Azureen näiden vaiheiden avulla.

## Lisäresurssit

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps -artikkeli](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP -repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Mitä seuraavaksi

- Seuraava: [Käytännön toteutus](../../04-PracticalImplementation/README.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.