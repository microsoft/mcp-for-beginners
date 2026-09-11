# Tapaustutkimus: Altista REST-rajapinta API Managementissa MCP-palvelimena

Azure API Management on palvelu, joka tarjoaa portin API-päätteidesi päälle. Sen toimintaperiaate on, että Azure API Management toimii proxyna API:esi edessä ja voi päättää, mitä saapuville pyynnöille tehdään.

Käyttämällä sitä lisäät kokonaisen joukon ominaisuuksia, kuten:

- **Turvallisuus**, voit käyttää kaikkea API-avaimista, JWT:hen ja hallittuun identiteettiin.
- **Kutsujen rajoittaminen**, hieno ominaisuus on pystyä päättämään, kuinka monta kutsua menee läpi tiettyä aikayksikköä kohden. Tämä auttaa varmistamaan, että kaikilla käyttäjillä on erinomainen kokemus ja että palvelusi ei kuormitu liikaa pyynnöistä.
- **Skaalaus ja kuormantasapainotus**. Voit määrittää useita päätepisteitä kuorman tasaamiseksi ja voit myös päättää, miten "kuormantasaat".
- **AI-ominaisuudet kuten semanttinen välimuisti**, token-raja ja tokenin seuranta sekä muuta. Nämä ovat hienoja ominaisuuksia, jotka parantavat reagointikykyä ja auttavat seuraamaan token-menojasi. [Lue lisää tästä](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Miksi MCP + Azure API Management?

Model Context Protocol on nopeasti muodostumassa standardiksi agenttisille AI-sovelluksille ja tavaksi altistaa työkaluja ja dataa yhdenmukaisella tavalla. Azure API Management on luonteva valinta, kun sinun tarvitsee "hallita" API:ita. MCP-palvelimet integroituvat usein muihin API:ihin ratkaistakseen pyyntöjä esimerkiksi työkaluille. Siksi Azure API Managementin ja MCP:n yhdistäminen on hyvin järkevää.

## Yleiskatsaus

Tässä käyttötapauksessa opimme altistamaan API-päätteet MCP-palvelimena. Näin voimme helposti tehdä näistä päätteistä osan agenttista sovellusta samalla hyödyntäen Azure API Managementin ominaisuuksia.

## Keskeiset ominaisuudet

- Valitset pääte-metodit, jotka haluat altistaa työkaluina.
- Lisäominaisuudet riippuvat siitä, mitä konfiguroit API:n politiikkaosiossa. Tässä näytämme, kuinka voit lisätä kutsujen rajoituksen.

## Esivaihe: Tuo API

Jos sinulla on jo API Azure API Managementissa, hienoa, voit ohittaa tämän vaiheen. Jos ei, katso tämä linkki, [API:n tuominen Azure API Managementiin](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Altista API MCP-palvelimena

Jotta altistat API-päätteet, seuraa näitä ohjeita:

1. Siirry Azure-portaaliin ja osoitteeseen <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Siirry API Management -instanssiisi.

1. Vasemman valikon kautta valitse APIs > MCP Servers > + Luo uusi MCP Server.

1. API:ssa valitse REST API, jonka haluat altistaa MCP-palvelimena.

1. Valitse yksi tai useampi API-toiminto altistettavaksi työkaluina. Voit valita kaikki toiminnot tai vain tietyt.

    ![Valitse metodit altistettavaksi](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Valitse **Luo**.

1. Siirry valikkokohtaan **APIs** ja **MCP Servers**, sinun pitäisi nähdä seuraava:

    ![Näe MCP-palvelin pääikkunassa](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-palvelin on luotu ja API-toiminnot on altistettu työkaluina. MCP-palvelin näkyy MCP Servers -paneelissa. URL-sarake näyttää MCP-palvelimen päätepisteen, jota voit kutsua testauksessa tai asiakassovelluksessa.

## Valinnainen: Määritä politiikat

Azure API Managementissa on ydinkonsepti nimeltä politiikat, joissa määrittelet erilaisia sääntöjä päätepisteille, kuten kutsujen rajoitus tai semanttinen välimuisti. Näitä politiikkoja kirjoitetaan XML-muodossa.

Näin voit määrittää politiikan rajoittamaan MCP-palvelimesi kuormitusta:

1. Portaalissa, APIs-kohdan alta, valitse **MCP Servers**.

1. Valitse luomasi MCP-palvelin.

1. Vasemmasta valikosta MCP:n alta valitse **Politiikat**.

1. Politiikkaeditorissa lisää tai muokkaa politiikkoja, joita haluat soveltaa MCP-palvelimen työkaluihin. Politiikat määritellään XML-muodossa. Esimerkiksi voit lisätä politiikan rajoittamaan kutsuja MCP-palvelimen työkaluihin (tässä esimerkissä 5 kutsua 30 sekunnissa per asiakas-IP-osoite). Tässä on XML, joka aiheuttaa kutsujen rajoituksen:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Tässä on kuva politiikkaeditorista:

    ![Politiikkaeditori](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Kokeile

Varmistetaan, että MCP-palvelimemme toimii suunnitellulla tavalla.

> [!NOTE]
> Azure API Management altistaa tällä hetkellä tämän palvelimen Streamable
> HTTP `/mcp` -päätepisteen kautta. Vanhempi HTTP+SSE `/sse` -kuljetus on vanhentunut ja
> sitä tulisi käyttää vain vanhempien asiakkaiden kanssa.

Tätä varten käytämme Visual Studio Codea ja GitHub Copilotia sen Agent-tilassa. Lisäämme MCP-palvelimen *mcp.json*-tiedostoon. Näin Visual Studio Code toimii asiakkaana, jolla on agenttikyvyt, ja loppukäyttäjät voivat kirjoittaa kehotteen ja olla vuorovaikutuksessa kyseisen palvelimen kanssa.

Katsotaan, miten lisäät MCP-palvelimen Visual Studio Codeen:

1. Käytä MCP: **Add Server -komentoa Komentopalettista**.

1. Kun sinulta kysytään, valitse palvelintyyppi: **HTTP (HTTP tai Server Sent Events)**.

1. Syötä MCP-palvelimen Streamable HTTP -URL, joka näkyy API Managementissa.
    Esimerkiksi:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Syötä palvelimen tunniste (server ID) oman valintasi mukaan. Tämä ei ole tärkeä arvo, mutta se auttaa muistamaan, mikä palvelininstanssi on kyseessä.

1. Valitse, tallennetaanko konfiguraatio työtilan asetuksiin vai käyttäjän asetuksiin.

  - **Työtilan asetukset** - Palvelinconfig tallennetaan .vscode/mcp.json -tiedostoon, joka on käytettävissä vain nykyisessä työtilassa.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Käyttäjän asetukset** - Palvelinconfig lisätään globaaliin *settings.json* -tiedostoon ja on käytettävissä kaikissa työtiloissa. Konfiguraatio näyttää seuraavalta:

    ![Käyttäjän asetus](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Sinun tulee myös lisätä konfiguraatioon otsikko varmistaaksesi, että se autentikoi oikein Azure API Managementia vastaan. Se käyttää otsikkoa nimeltä **Ocp-Apim-Subscription-Key**.


    - Näin voit lisätä sen asetuksiin:

    ![Todennuksen otsikon lisääminen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), tämä saa aikaan kehotteen, jossa pyydetään API-avaimen arvoa, jonka löydät Azure-portaalista Azure API Management -instanssillesi.

   - Jos haluat lisätä sen *mcp.json*-tiedostoon, voit tehdä sen näin:

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

### Käytä Agent-tilaa

Nyt olemme valmiina asetuksissa tai *.vscode/mcp.json*-tiedostossa. Kokeillaanpa.

Työkalukuvake pitäisi näkyä tältä, jossa serveriltäsi paljastetut työkalut on listattu:

![Työkalut palvelimelta](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klikkaa työkalukuvaketta, niin näet työkaluluettelon tältä:

    ![Työkalut](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Anna kehotteeseen viesti käynnistääksesi työkalun. Esimerkiksi, jos valitsit työkalun saadaksesi tietoa tilauksesta, voit kysyä agentilta tilauksesta. Tässä esimerkki kehotteesta:

    ```text
    get information from order 2
    ```

    Sinulle näytetään nyt työkalukuvake, joka pyytää jatkamaan työkalun kutsumista. Valitse jatkaaksesi työkalun suorittamista, ja sinun tulisi nyt nähdä tulos tältä:

    ![Tulos kehotteesta](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **näkemäsi yllä riippuu asetetuista työkaluista, mutta idea on, että saat tekstipohjaisen vastauksen kuten yllä**


## Viitteet

Näin voit oppia lisää:

- [Opas Azure API Managementistä ja MCP:stä](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-esimerkki: Suojaa etä-MCP-palvelimet Azure API Managementilla (kokeellinen)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-asiakkaan auktorisoinnin laboratorio](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Käytä Azure API Management -laajennusta VS Codeen API:en tuontiin ja hallintaan](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Rekisteröi ja löydä etä-MCP-palvelimet Azure API Centerissä](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Hieno repositorio, joka esittelee monia tekoälyominaisuuksia Azure API Managementilla
- [AI Gateway -työpajat](https://azure-samples.github.io/AI-Gateway/) Sisältää työpajoja Azure-portaalin avulla, mikä on loistava tapa aloittaa tekoälyominaisuuksien arviointi.

## Mitä seuraavaksi

- Takaisin: [Tapaustutkimusten yleiskatsaus](./README.md)
- Seuraava: [Azure AI matkatoimistot](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->