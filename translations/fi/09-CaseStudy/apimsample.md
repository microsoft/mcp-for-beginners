# Tapaustutkimus: Julkaise REST API API Managementissä MCP-palvelimena

Azure API Management on palvelu, joka tarjoaa portin API-päätepisteidesi päälle. Se toimii niin, että Azure API Management toimii välityspalvelimena API:esi edessä ja voi päättää, mitä saapuville pyynnöille tehdään.

Käyttämällä sitä, lisäät koko joukon ominaisuuksia, kuten:

- **Turvallisuus**, voit käyttää kaikkea API-avaimista, JWT:stä ja hallittuun identiteettiin.
- **Kutsujen rajoittaminen**, erinomainen ominaisuus, jolla voit päättää kuinka monta kutsua pääsee läpi tietyn aikayksikön aikana. Tämä auttaa varmistamaan, että kaikilla käyttäjillä on hyvä käyttökokemus ja myös sen, ettei palvelusi kuormitu liikaa pyynnöistä.
- **Skaalaus & Kuormantasapaino**. Voit määrittää useita päätepisteitä kuorman tasaamiseksi ja voit myös päättää, miten "kuormantasapaino" toimii.
- **AI-ominaisuudet kuten semanttinen välimuisti**, token-rajoitus ja token-valvonta sekä paljon muuta. Nämä ovat erinomaisia ominaisuuksia, jotka parantavat reagoivuutta ja auttavat pitämään tokenien käytön hallinnassa. [Lue lisää täältä](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Miksi MCP + Azure API Management?

Model Context Protocolista on nopeasti tulossa standardi agenttipohjaisille tekoälysovelluksille ja työkalujen sekä datan yhdenmukaiselle julkaisulle. Azure API Management on luonnollinen valinta kun tarvitset API:iden "hallintaa". MCP-palvelimet usein integroituvat muihin API:hin ratkaistakseen esimerkiksi työkaluun kohdistuvia pyyntöjä. Siksi Azure API Managementin ja MCP:n yhdistäminen on järkevää.

## Yleiskuva

Tässä erityisessä käyttötapauksessa opimme julkistamaan API-päätepisteet MCP-palvelimena. Näin voimme helposti ottaa nämä päätepisteet agenttipohjaisen sovelluksen osaksi samalla kun hyödynnämme Azure API Managementin ominaisuuksia.

## Keskeiset ominaisuudet

- Valitset päätepisteiden menetelmät, jotka haluat julkaista työkaluina.
- Lisäominaisuudet riippuvat siitä, mitä määrittelet politiikkaosiossa API:llesi. Tässä näytämme, miten voit lisätä kutsujen rajoituksen.

## Esivaihe: tuo API

Jos sinulla on jo API Azure API Managementissä, hienoa, voit ohittaa tämän vaiheen. Muussa tapauksessa tutustu tähän linkkiin, [API:n tuonti Azure API Managementiin](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Julkaise API MCP-palvelimena

Julkaistaksesi API-päätepisteet, seuraa näitä ohjeita:

1. Siirry Azure-portaaliin osoitteeseen <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Siirry API Management -instanssiisi.

1. Vasemmasta valikosta valitse APIs > MCP Servers > + Luo uusi MCP Server.

1. Valitse API-kohdassa REST API, jonka haluat julkaista MCP-palvelimena.

1. Valitse yksi tai useampi API-operaatio julkaistavaksi työkaluina. Voit valita kaikki operaatiot tai vain tietyt.

    ![Valitse julkaistavat menetelmät](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Valitse **Luo**.

1. Siirry valikosta kohtaan **APIs** ja **MCP Servers**, sinun pitäisi nähdä seuraava:

    ![Näytä MCP-palvelin pääikkunassa](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-palvelin on luotu ja API-operaatiot on julkaistu työkaluina. MCP-palvelin näkyy MCP Servers -paneelissa. URL-sarake näyttää MCP-palvelimen päätepisteen, jolle voit tehdä testikutsuja tai käyttää sitä asiakassovelluksessa.

## Valinnainen: Määritä politiikat

Azure API Managementissä keskeinen käsite ovat politiikat, joilla määritellään eri säännöt päätepisteillesi, kuten kutsujen rajoittaminen tai semanttinen välimuisti. Nämä politiikat kirjoitetaan XML-muodossa.

Näin voit määrittää politiikan MCP-palvelimesi kutsujen rajoittamiseksi:

1. Portaalissa, API:issa, valitse **MCP Servers**.

1. Valitse luomasi MCP-palvelin.

1. Vasemmassa valikossa, MCP:ssä, valitse **Policies**.

1. Politiikkamuokkaimessa lisää tai muokkaa MCP-palvelimen työkaluihin sovellettavia politiikkoja. Politiikat määritellään XML-muodossa. Esimerkiksi voit lisätä politiikan, joka rajoittaa kutsujen määrää MCP-palvelimen työkaluihin (tässä esimerkissä 5 kutsua 30 sekunnissa per asiakas-IP-osoite). Tässä XML, joka aiheuttaa rajoituksen:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Tässä kuva politiikkamuokkaimesta:

    ![Politiikkamuokkaimen kuva] (https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Kokeile

Varmistetaan, että MCP-palvelimemme toimii oikein.

> [!NOTE]
> Azure API Management julkaisee tällä hetkellä palvelinta Streamable
> HTTP `/mcp` -päätepisteen kautta. Vanhempi HTTP+SSE `/sse` -kuljetus on vanhentunut ja
> sitä tulisi käyttää vain vanhojen asiakkaiden kanssa.

Tätä varten käytämme Visual Studio Codea ja GitHub Copilotia agenttitilassa. Lisäämme MCP-palvelimen *mcp.json*-tiedostoon. Näin Visual Studio Code toimii agenttikykyisenä asiakkaana ja loppukäyttäjät voivat kirjoittaa kehotteen ja olla vuorovaikutuksessa palvelimen kanssa.

Katsotaan, miten MCP-palvelin lisätään Visual Studio Codeen:

1. Käytä MCP:n **Add Server** -komentoa Komentopalettista.

1. Kun sinulta kysytään, valitse palvelintyyppi: **HTTP (HTTP tai Server Sent Events)**.

1. Syötä Streamable HTTP URL, joka näkyy MCP-palvelimella API Managementissä.
    Esimerkiksi:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Anna haluamasi palvelimen tunniste. Tämä ei ole tärkeä arvo, mutta auttaa muistamaan, mikä palvelin on kyseessä.

1. Valitse, tallennetaanko määritys työtilan vai käyttäjäasetuksiin.

    - **Työtila-asetukset** - Palvelimen määritys tallennetaan `.vscode/mcp.json` -tiedostoon, joka on käytettävissä vain nykyisessä työtilassa.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **Käyttäjäasetukset** - Palvelinasetukset lisätään globaaliin *settings.json* -tiedostoon ja ne ovat käytettävissä kaikissa työtiloissa. Määritys näyttää suunnilleen tältä:

      ![Käyttäjäasetuksen kuva] (https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Sinun tulee myös lisätä määrityksen otsikko varmistaaksesi autentikoinnin Azure API Managementia kohtaan. Se käyttää otsikkoa nimeltä **Ocp-Apim-Subscription-Key**.

    - Tässä, miten voit lisätä sen asetuksiin:


    ![Otsikon lisääminen autentikointiin](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), tämä aiheuttaa kehotteen, joka pyytää API-avaimen, jonka löydät Azure-portaalista Azure API Management -instanssillesi.

   - Jos haluat lisätä sen *mcp.json*:iin, voit tehdä sen näin:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Käytä agenttitilaa

Nyt olemme valmiit asetuksista riippumatta, olipa se asetuksissa tai *.vscode/mcp.json*. Kokeillaan.

Sinulla pitäisi olla Työkalut-kuvake, jossa näkyvät palvelimen julkistetut työkalut:

![Palvelimen työkalut](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klikkaa työkalukuvaketta, jolloin näet työkaluluettelon:

    ![Työkalut](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Kirjoita keskustelukenttään pyyntö työkalun kutsumiseksi. Esimerkiksi, jos valitsit työkalun tilaustietojen hakemiseen, voit kysyä agentilta tilauksesta. Tässä esimerkkipyyntö:

    ```text
    get information from order 2
    ```

    Nyt sinulle näytetään työkalukuvake, joka pyytää vahvistusta työkalun kutsumiseen. Valitse jatkaaksesi työkalun käyttöä, ja näet tuloksen tältä näyttävänä:

    ![Tulos kehotteesta](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **mitä näet yllä riippuu siitä, mitä työkaluja olet määrittänyt, mutta ajatuksena on saada tekstipohjainen vastaus kuten yllä**


## Viitteet

Näin voit oppia lisää:

- [Opas Azure API Managementiin ja MCP:hen](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-esimerkki: Suojaa etä-MCP-palvelimet Azure API Managementilla (kokeellinen)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-asiakkaan valtuutusharjoitus](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Käytä Azure API Management -laajennusta VS Codeen API:den tuontiin ja hallintaan](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Rekisteröi ja etsi etä MCP-palvelimia Azure API Centerissä](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Erinomainen repositorio, joka esittelee monia tekoälyominaisuuksia Azure API Managementilla
- [AI Gateway -työpajat](https://azure-samples.github.io/AI-Gateway/) Sisältää työpajoja Azure-portaalin avulla, erinomainen tapa aloittaa tekoälyominaisuuksien arviointi.

## Mitä seuraavaksi

- Palaa kohtaan: [Tapaustutkimusten yleiskuva](./README.md)
- Seuraavaksi: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->