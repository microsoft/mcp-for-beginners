# Tapaustutkimus: REST-rajapinnan julkaiseminen API Managementissa MCP-palvelimena

Azure API Management on palvelu, joka tarjoaa yhdyskäytävän API-päätepisteidesi päälle. Se toimii siten, että Azure API Management toimii välityspalvelimena API:esi edessä ja voi päättää, mitä saapuville pyynnöille tehdään.

Sen avulla voit lisätä monia ominaisuuksia, kuten:

- **Turvallisuus**, voit käyttää kaikkea API-avaimista ja JWT:stä hallittuun identiteettiin.
- **Nopeusrajoitukset**, erinomainen ominaisuus on mahdollisuus päättää, kuinka monta kutsua sallitaan tietyn aikayksikön aikana. Tämä auttaa varmistamaan, että kaikilla käyttäjillä on hyvä kokemus ja että palvelusi ei ylikuormitu pyynnöistä.
- **Skaalautuvuus ja kuormantasapainotus**. Voit määrittää useita päätepisteitä tasapainottamaan kuormaa ja päättää, miten "kuormaa tasapainotetaan".
- **Tekoälyominaisuudet, kuten semanttinen välimuisti**, token-rajoitukset ja token-seuranta sekä paljon muuta. Nämä ovat erinomaisia ominaisuuksia, jotka parantavat reagointikykyä ja auttavat hallitsemaan token-kulutusta. [Lue lisää täältä](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Miksi MCP + Azure API Management?

Model Context Protocol (MCP) on nopeasti nousemassa standardiksi agenttipohjaisille tekoälysovelluksille ja työkalujen sekä datan yhdenmukaiselle esittämiselle. Azure API Management on luonnollinen valinta, kun tarvitset API:iden "hallintaa". MCP-palvelimet integroituvat usein muihin API:ihin ratkaistakseen esimerkiksi työkalupyyntöjä. Siksi Azure API Managementin ja MCP:n yhdistäminen on järkevää.

## Yleiskatsaus

Tässä erityisessä käyttötapauksessa opimme julkaisemaan API-päätepisteitä MCP-palvelimena. Näin voimme helposti tehdä näistä päätepisteistä osan agenttipohjaista sovellusta samalla hyödyntäen Azure API Managementin ominaisuuksia.

## Keskeiset ominaisuudet

- Voit valita, mitkä päätepisteiden metodit haluat julkaista työkaluina.
- Lisäominaisuudet riippuvat siitä, mitä määrität API:si käytäntöosiossa. Tässä näytämme, kuinka voit lisätä nopeusrajoituksia.

## Esivaihe: API:n tuonti

Jos sinulla on jo API Azure API Managementissa, voit ohittaa tämän vaiheen. Jos ei, tutustu tähän linkkiin: [API:n tuominen Azure API Managementiin](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API:n julkaiseminen MCP-palvelimena

Julkaistaksesi API-päätepisteet, seuraa näitä vaiheita:

1. Siirry Azure-portaaliin osoitteessa <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   Siirry API Management -instanssiisi.

1. Vasemmasta valikosta valitse **APIs > MCP Servers > + Create new MCP Server**.

1. Valitse API:sta REST API, jonka haluat julkaista MCP-palvelimena.

1. Valitse yksi tai useampi API-toiminto, jotka haluat julkaista työkaluina. Voit valita kaikki toiminnot tai vain tietyt toiminnot.

    ![Valitse julkaistavat metodit](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Valitse **Create**.

1. Siirry valikossa kohtaan **APIs** ja **MCP Servers**, ja sinun pitäisi nähdä seuraava näkymä:

    ![Näe MCP-palvelin pääikkunassa](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-palvelin on luotu, ja API-toiminnot on julkaistu työkaluina. MCP-palvelin näkyy MCP Servers -paneelissa. URL-sarake näyttää MCP-palvelimen päätepisteen, jota voit kutsua testaukseen tai asiakassovelluksessa.

## Valinnainen: Käytäntöjen määrittäminen

Azure API Managementin ydinajatus on käytännöt, joissa voit määrittää erilaisia sääntöjä päätepisteillesi, kuten nopeusrajoituksia tai semanttista välimuistia. Nämä käytännöt kirjoitetaan XML-muodossa.

Näin voit määrittää käytännön rajoittamaan MCP-palvelimen kutsuja:

1. Portaalissa, kohdassa **APIs**, valitse **MCP Servers**.

1. Valitse luomasi MCP-palvelin.

1. Vasemmasta valikosta, kohdasta **MCP**, valitse **Policies**.

1. Käytäntöeditorissa lisää tai muokkaa käytäntöjä, joita haluat soveltaa MCP-palvelimen työkaluihin. Käytännöt määritellään XML-muodossa. Esimerkiksi voit lisätä käytännön, joka rajoittaa kutsut MCP-palvelimen työkaluihin (tässä esimerkissä 5 kutsua 30 sekunnin aikana per asiakas-IP-osoite). Tässä on XML, joka asettaa nopeusrajoituksen:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Tässä on kuva käytäntöeditorista:

    ![Käytäntöeditori](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Kokeile

Varmistetaan, että MCP-palvelimemme toimii odotetusti.

Tätä varten käytämme Visual Studio Codea ja GitHub Copilotin Agent-tilaa. Lisäämme MCP-palvelimen *mcp.json*-tiedostoon. Näin Visual Studio Code toimii asiakkaana agenttikapasiteetilla, ja loppukäyttäjät voivat kirjoittaa kehotteita ja olla vuorovaikutuksessa palvelimen kanssa.

Näin lisäät MCP-palvelimen Visual Studio Codeen:

1. Käytä komentopalettia ja valitse **MCP: Add Server** -komento.

1. Kun sinulta kysytään, valitse palvelimen tyyppi: **HTTP (HTTP tai Server Sent Events)**.

1. Syötä MCP-palvelimen URL API Managementissa. Esimerkki: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE-päätepisteelle) tai **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP-päätepisteelle). Huomaa ero kuljetusmuotojen välillä: `/sse` tai `/mcp`.

1. Syötä palvelimen tunnus (ID) valintasi mukaan. Tämä arvo ei ole tärkeä, mutta auttaa muistamaan, mikä palvelininstanssi on kyseessä.

1. Valitse, tallennetaanko kokoonpano työtilan asetuksiin vai käyttäjäasetuksiin.

  - **Työtilan asetukset** - Palvelimen kokoonpano tallennetaan .vscode/mcp.json-tiedostoon, joka on käytettävissä vain nykyisessä työtilassa.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    tai jos valitset suoratoiston HTTP:n kuljetusmuodoksi, se olisi hieman erilainen:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Käyttäjäasetukset** - Palvelimen kokoonpano lisätään globaaliin *settings.json*-tiedostoon ja on käytettävissä kaikissa työtiloissa. Kokoonpano näyttää seuraavalta:

    ![Käyttäjäasetukset](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Sinun on myös lisättävä kokoonpanoon otsikko, joka varmistaa autentikoinnin Azure API Managementia vastaan. Se käyttää otsikkoa nimeltä **Ocp-Apim-Subscription-Key**.

    - Näin lisäät sen asetuksiin:

    ![Autentikointiotteen lisääminen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png). Tämä aiheuttaa kehotteen, jossa sinulta kysytään API-avaimen arvoa, jonka löydät Azure-portaalista Azure API Management -instanssillesi.

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

Nyt olemme valmiita joko asetuksissa tai *.vscode/mcp.json*-tiedostossa. Kokeillaan sitä.

Työkalukuvake pitäisi näkyä, ja siinä listataan palvelimeltasi julkaistut työkalut:

![Palvelimen työkalut](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klikkaa työkalukuvaketta, ja sinun pitäisi nähdä lista työkaluista, kuten tässä:

    ![Työkalut](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Kirjoita kehotus chattiin kutsuaksesi työkalua. Esimerkiksi, jos valitsit työkalun tilaustietojen hakemiseen, voit kysyä agentilta tilauksesta. Tässä esimerkki kehotuksesta:

    ```text
    get information from order 2
    ```

    Näet nyt työkalukuvakkeen, joka pyytää sinua jatkamaan työkalun kutsumista. Valitse jatkaaksesi työkalun suorittamista, ja sinun pitäisi nähdä tulos, kuten tässä:

    ![Kehotteen tulos](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Yllä näkyvä riippuu siitä, mitä työkaluja olet määrittänyt, mutta idea on, että saat tekstimuotoisen vastauksen, kuten yllä.**

## Viitteet

Tässä lisää oppimateriaalia:

- [Opas Azure API Managementista ja MCP:stä](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-esimerkki: Suojaa etä-MCP-palvelimet Azure API Managementilla (kokeellinen)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-asiakkaan valtuutuslaboratorio](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Käytä Azure API Management -laajennusta VS Codessa API:iden tuontiin ja hallintaan](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Rekisteröi ja löydä etä-MCP-palvelimet Azure API Centerissä](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Erinomainen repo, joka esittelee monia tekoälyominaisuuksia Azure API Managementilla
- [AI Gateway -työpajat](https://azure-samples.github.io/AI-Gateway/) Sisältää työpajoja Azure-portaalin avulla, mikä on loistava tapa aloittaa tekoälyominaisuuksien arviointi.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.