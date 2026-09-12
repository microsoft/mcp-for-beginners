# MCP-palvelimien käyttöönotto

> [!NOTE]
> Konfigurointiesimerkit, jotka käyttävät `/sse`-päätepistettä, kohdistuvat perinteiseen HTTP+SSE
> tiedonsiirtoon. MCP `2026-07-28` etäpalvelimet käyttävät Streamable HTTP:tä, yleensä palvelimen määrittelemässä
> päätepisteessä, kuten `/mcp`.

MCP-palvelimesi käyttöönotto mahdollistaa muiden pääsyn sen työkaluihin ja resursseihin paikallisen ympäristösi ulkopuolella. On olemassa useita käyttöönotto-strategioita, jotka kannattaa ottaa huomioon riippuen skaalautuvuuden, luotettavuuden ja hallinnan helppouden vaatimuksistasi. Seuraavassa löydät ohjeita MCP-palvelimien käyttöönottoon paikallisesti, konteissa ja pilvipalveluihin.

## Yleiskatsaus

Tässä oppitunnissa käydään läpi, miten MCP Server -sovelluksesi otetaan käyttöön.

## Oppimistavoitteet

Oppitunnin lopussa osaat:

- Arvioida erilaisia käyttöönotto-menetelmiä.
- Ottaa sovelluksesi käyttöön.

## Paikallinen kehitys ja käyttöönotto

Jos palvelimesi on tarkoitettu ajettavaksi käyttäjän koneella, voit seurata seuraavia vaiheita:

1. **Lataa palvelin**. Jos et ole kirjoittanut palvelinta, lataa se ensin koneellesi.
1. **Käynnistä palveluprosessi**: Aja MCP-palvelinsovelluksesi

SSE:tä varten (ei tarvita stdio-tyyppisille palvelimille)

1. **Määritä verkko**: Varmista, että palvelin on saavutettavissa odotetulla portilla
1. **Yhdistä asiakkaat**: Käytä paikallisia yhteys-URL-osoitteita kuten `http://localhost:3000`

## Pilvikäyttöönotto

MCP-palvelimia voidaan ottaa käyttöön eri pilvialustoilla:

- **Palvelimettomat funktiot**: Käyttöön kevyitä MCP-palvelimia palvelimettomina funktioina
- **Konttipalvelut**: Käytä palveluita kuten Azure Container Apps, AWS ECS tai Google Cloud Run
- **Kubernetes**: Ota MCP-palvelimet käyttöön ja hallinnoi niitä Kubernetes-klustereissa korkean käytettävyyden takaamiseksi

### Esimerkki: Azure Container Apps

Azure Container Apps tukee MCP-palvelimien käyttöönottoa. Se on vielä työn alla, ja tällä hetkellä tukee SSE-palvelimia.

Näin voit toimia:

1. Kopioi repository:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Aja se paikallisesti testataksesi:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Kokeillaksesi paikallisesti, luo *mcp.json* -tiedosto *.vscode*-kansioon ja lisää seuraava sisältö:

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

  Kun SSE-palvelin on käynnistetty, voit klikata play-kuvaketta JSON-tiedostossa, sinun pitäisi nyt nähdä palvelimen työkalut tulevan GitHub Copilotin käyttöön, katso Työkalu-kuvake.

1. Ota käyttöön ajamalla seuraava komento:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Siinä se, ota käyttöön paikallisesti tai Azureen näiden ohjeiden avulla.

## Lisäresurssit

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps -artikkeli](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Mitä seuraavaksi

- Seuraavaksi: [Kehittyneet palvelinaiheet](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->