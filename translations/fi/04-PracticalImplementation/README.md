# Käytännön toteutus

[![Miten rakentaa, testata ja ottaa MCP-sovelluksia käyttöön oikeilla työkaluilla ja työnkuluilla](../../../translated_images/fi/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Klikkaa yllä olevaa kuvaa katsellaksesi tämän oppitunnin videon)_

Käytännön toteutus on paikka, jossa Model Context Protocolin (MCP) voima tulee konkreettiseksi. Vaikka MCP:n teoria- ja arkkitehtuurin ymmärtäminen on tärkeää, todellinen arvo syntyy soveltamalla näitä konsepteja ratkaisujen rakentamiseen, testaamiseen ja käyttöönottoon, jotka ratkaisevat todellisia ongelmia. Tämä luku yhdistää käsitteellisen tiedon ja käytännön kehityksen, ohjaten sinua prosessin läpi MCP-pohjaisten sovellusten elävöittämiseksi.

Olitpa kehittämässä älykkäitä assistentteja, integroimassa tekoälyä liiketoimintatyönkulkuihin tai rakentamassa räätälöityjä työkaluja datankäsittelyyn, MCP tarjoaa joustavan perustan. Sen kielestä riippumaton rakenne ja viralliset SDK:t suosituilla ohjelmointikielillä tekevät siitä saavutettavan laajalle kehittäjäjoukolle. Hyödyntämällä näitä SDK:ita voit nopeasti luoda prototyyppejä, iteroida ja skaalata ratkaisujasi useilla alustoilla ja ympäristöissä.

Seuraavissa osioissa löydät käytännön esimerkkejä, näytekoodia ja käyttöönotto-strategioita, jotka osoittavat, miten MCP toteutetaan C#:ssa, Javassa Springin kanssa, TypeScriptissä, JavaScriptissä ja Pythonissa. Opit myös, miten MCP-palvelimia voi virheenkorjata ja testata, hallita API-rajapintoja ja ottaa ratkaisuja käyttöön pilvessä Azuren avulla. Nämä käytännön resurssit on suunniteltu nopeuttamaan oppimistasi ja auttamaan sinua rakentamaan luotettavia, tuotantovalmiita MCP-sovelluksia itsevarmasti.

## Yleiskatsaus

Tässä oppitunnissa keskitytään MCP:n käytännön toteutukseen useilla ohjelmointikielillä. Tutkimme, miten MCP SDK:ita käytetään C#:ssa, Javassa Springin kanssa, TypeScriptissä, JavaScriptissä ja Pythonissa vankkojen sovellusten rakentamiseen, MCP-palvelimien virheenkorjaukseen ja testaamiseen sekä uudelleenkäytettävien resurssien, kehotteiden ja työkalujen luomiseen.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Toteuttaa MCP-ratkaisuja virallisten SDK:iden avulla eri ohjelmointikielillä
- Virheenkorjata ja testata MCP-palvelimia järjestelmällisesti
- Luoda ja käyttää palvelimen ominaisuuksia (Resurssit, Kehotteet ja Työkalut)
- Suunnitella tehokkaita MCP-työnkulkuja monimutkaisiin tehtäviin
- Optimoida MCP-toteutuksia suorituskyvyn ja luotettavuuden näkökulmasta

## Viralliset SDK-resurssit

Model Context Protocol tarjoaa viralliset SDK:t useille kielille (yhteensopiva [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) kanssa):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Huom:** vaatii riippuvuuden [Project Reactor](https://projectreactor.io) -kirjastoon. (Katso [keskustelu 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Työskentely MCP SDK:den kanssa

Tässä osiossa esitellään käytännön esimerkkejä MCP:n toteutuksesta useilla ohjelmointikielillä. Näytekoodi löytyy `samples`-hakemistosta kielikohtaisesti järjestettynä.

### Saatavilla olevat näytteet

Arkistossa on [näytetoteutuksia](../../../04-PracticalImplementation/samples) seuraavilla kielillä:

- [C#](./samples/csharp/README.md)
- [Java Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Jokainen näyte havainnollistaa keskeisiä MCP-konsepteja ja toteutusmalleja kyseisen kielen ja ekosysteemin puitteissa.

### Käytännön oppaat

Lisäoppaita käytännön MCP-toteutuksiin:

- [Sivutus ja suuret tulosjoukot](./pagination/README.md) - Työkalujen, resurssien ja suurten datamäärien kursori-pohjainen sivutus

## Palvelimen keskeiset ominaisuudet

MCP-palvelimet voivat toteuttaa minkä tahansa näistä ominaisuuksien yhdistelmän:

### Resurssit

Resurssit tarjoavat kontekstia ja dataa käyttäjän tai tekoälymallin käyttöön:

- Asiakirjarekisterit
- Tietopohjat
- Rakenteelliset tietolähteet
- Tiedostojärjestelmät

### Kehotteet

Kehotteet ovat mallipohjaisia viestejä ja työnkulkuja käyttäjille:

- Ennalta määritellyt keskustelumallit
- Ohjatut vuorovaikutuskuviot
- Erikoistuneet dialogirakenteet

### Työkalut

Työkalut ovat toimintoja, joita tekoälymalli voi suorittaa:

- Datan käsittelytyökalut
- Ulkoiset API-integraatiot
- Laskentakyvyt
- Hakutoiminnot

## Näytetoteutukset: C#-toteutus

Virallisessa C# SDK -arkistossa on useita näytetoteutuksia, jotka demonstroivat eri MCP:n puolia:

- **Perus MCP-asiakas**: Yksinkertainen esimerkki MCP-asiakkaan luomisesta ja työkalujen kutsumisesta
- **Perus MCP-palvelin**: Minimipalvelin toteutus, jossa perus työkalurekisteröinti
- **Kehittynyt MCP-palvelin**: Täyden ominaisuuskirjon palvelin työkalurekisteröinnillä, autentikoinnilla ja virheenkäsittelyllä
- **ASP.NET-integraatio**: Esimerkkejä ASP.NET Core -integraatiosta
- **Työkalujen toteutusmallit**: Erilaisia malleja työkalujen toteuttamiseen eri monimutkaisuustasoilla

MCP C# SDK on esikatseluvaiheessa ja rajapinnat voivat muuttua. Päivitämme tätä blogia jatkuvasti SDK:n kehittyessä.

### Keskeiset ominaisuudet

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Ensimmäisen MCP-palvelimen rakentaminen: [Build a Model Context Protocol (MCP) server in C#](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)

Täydellisiä C#-toteutusnäytteitä löydät virallisen C# SDK:n näytearkistosta: [https://github.com/modelcontextprotocol/csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)

## Näytetoteutus: Java Spring -toteutus

Java Spring SDK tarjoaa vankkoja MCP-toteutusmahdollisuuksia yritystason ominaisuuksilla.

### Keskeiset ominaisuudet

- Spring Framework -integraatio
- Vahva tyyppiturva
- Reaktiivinen ohjelmointi
- Laaja virheenkäsittely

Täydellinen Java Spring -toteutusnäyte löytyy [Java Spring -näytteestä](samples/java/containerapp/README.md) näytekansiosta.

## Näytetoteutus: JavaScript-toteutus

JavaScript SDK tarjoaa kevyen ja joustavan tavan MCP:n toteuttamiseen.

### Keskeiset ominaisuudet

- Tuki Node.js:lle ja selaimelle
- Lupauspohjainen API
- Helppo integraatio Express:n ja muiden kehysten kanssa
- WebSocket-tuki virtausta varten

Täydellinen JavaScript-toteutusnäyte löytyy [JavaScript-näytteestä](samples/javascript/README.md) näytekansiosta.

## Näytetoteutus: Python-toteutus

Python SDK tarjoaa Python-tyyppisen lähestymistavan MCP:n toteutukseen erinomaisilla ML-kehysintegraatioilla.

### Keskeiset ominaisuudet

- Async/await -tuki asyncio:n kanssa
- FastAPI-integraatio
- Yksinkertainen työkalurekisteröinti
- Natiivi integraatio suosittuihin ML-kirjastoihin

Täydellinen Python-toteutusnäyte löytyy [Python-näytteestä](samples/python/README.md) näytekansiosta.

## API:n hallinta

Azure API Management on erinomainen ratkaisu, kun halutaan suojata MCP-palvelimet. Ajatuksena on laittaa Azure API Management -instanssi MCP-palvelimen eteen ja antaa sen hoitaa ominaisuuksia, joita todennäköisesti haluat, kuten:

- nopeusrajoitukset
- tunnusten hallinta
- valvonta
- kuormantasoitus
- turvallisuus

### Azure-näyte

Tässä on Azure-näyte, joka tekee juuri tämän, eli [luo MCP-palvelin ja suojaa se Azure API Managementilla](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Katso miten valtuutusprosessi etenee alla olevassa kuvassa:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Edellisessä kuvassa tapahtuu seuraavaa:

- Todentaminen/valtuutus tapahtuu Microsoft Entran avulla.
- Azure API Management toimii porttina ja käyttää sääntöjä liikenteen ohjaamiseen ja hallintaan.
- Azure Monitor kirjaa kaikki pyynnöt jatkoanalyysiä varten.

#### Valtuutusprosessi

Tarkastellaan valtuutusprosessia tarkemmin:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP:n valtuutusspesifikaatio

Lue lisää [MCP:n valtuutusspesifikaatiosta](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Etä-MCP-palvelimen käyttöönotto Azureen

Katsotaan, voimmeko ottaa aiemmin mainitun näytteen käyttöönottoon:

1. Kloonaa repositorio

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Rekisteröi `Microsoft.App` resurssitarjoaja.

   - Jos käytät Azure CLI:tä, suorita `az provider register --namespace Microsoft.App --wait`.
   - Jos käytät Azure PowerShelliä, suorita `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Tarkista rekisteröintitila ajamalla `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` jonkin ajan kuluttua.

1. Suorita tämä [azd](https://aka.ms/azd) -komento varmistamaan API Management -palvelu, Function App (koodeineen) ja kaikki muut tarvittavat Azure-resurssit

    ```shell
    azd up
    ```

    Tämä komento ottaa käyttöön kaikki pilvipalvelun resurssit Azureen

### Palvelimen testaaminen MCP Inspectorilla

1. **Uudessa komentorivipaneelissa**, asenna ja aja MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Näet käyttöliittymän, joka näyttää tältä:

    ![Yhdistä Node inspector](../../../translated_images/fi/connect.141db0b2bd05f096.webp)

1. CTRL-klikkaa ladataksesi MCP Inspector -web-sovelluksen sovelluksen näyttämästä URL-osoitteesta (esim. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Aseta kuljetustavaksi `SSE`
1. Syötä URL käynnissä olevalle API Management SSE -päätteellesi, joka näkyy `azd up` -komennon jälkeen ja **Yhdistä**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Listaa työkalut**. Klikkaa työkalua ja **Aja työkalu**.  

Jos kaikki vaiheet onnistuivat, olet nyt yhdistänyt MCP-palvelimeen ja pystynyt kutsumaan työkalua.

## MCP-palvelimet Azureen

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Nämä repositoriot ovat pika-aloitusmalleja räätälöityjen etä-MCP (Model Context Protocol) palvelinten rakentamiseen ja käyttöönottoon Azure Functions -ympäristössä Pythonin, C# .NETin tai Node/TypeScriptin avulla.

Näytteet tarjoavat täydellisen ratkaisun, jonka avulla kehittäjät voivat:

- Rakentaa ja ajaa paikallisesti: Kehittää ja virheenkorjata MCP-palvelinta paikallisella koneella
- Ota käyttöön Azureen: Helppo pilvikäyttöönotto yksinkertaisella azd up -komennolla
- Yhdistä asiakkailta: Yhdistä MCP-palvelimeen eri asiakasohjelmilla, mukaan lukien VS Code:n Copilot agent-moodi ja MCP Inspector -työkalu

### Keskeiset ominaisuudet

- Suojaus suunnittelusta lähtien: MCP-palvelin on suojattu avaimilla ja HTTPS:llä
- Autentikointivaihtoehdot: Tukee OAuth:ta sisäänrakennetulla autentikoinnilla ja/tai API Managementilla
- Verkkosegmentointi: Mahdollistaa verkkosegmentoinnin Azuren virtuaaliverkkojen (VNET) avulla
- Serverless-arkkitehtuuri: Hyödyntää Azure Functionseja skaalautuvaan, tapahtumapohjaiseen suoritukseen
- Paikallinen kehitys: Kattava tuki paikalliselle kehitykselle ja virheenkorjaukselle
- Yksinkertainen käyttöönotto: Sujuva käyttöönotto prosessi Azureen

Arkisto sisältää kaikki tarvittavat konfiguraatiotiedostot, lähdekoodin ja infrastruktuurin määrittelyt, joiden avulla pääset nopeasti alkuun tuotantovalmiin MCP-palvelimen toteutuksessa.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Näytetoteutus MCP:stä Azure Functionseilla Pythonilla

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Näytetoteutus MCP:stä Azure Functionseilla C# .NETillä

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Näytetoteutus MCP:stä Azure Functionseilla Node/TypeScriptillä

## Tärkeitä oppeja

- MCP SDK:t tarjoavat kielikohtaiset työkalut vahvojen MCP-ratkaisujen toteutukseen
- Virheenkorjaus- ja testausprosessit ovat kriittisiä luotettaville MCP-sovelluksille
- Uudelleenkäytettävät kehotemallit mahdollistavat johdonmukaiset tekoälyvuorovaikutukset
- Hyvin suunnitellut työnkulut voivat orkestroida monimutkaisia tehtäviä useilla työkaluilla
- MCP-ratkaisujen toteuttamisessa on huomioitava turvallisuus, suorituskyky ja virheenkäsittely

## Harjoitus

Suunnittele käytännön MCP-työnkulku, joka ratkaisee todellisen ongelman omalla alallasi:

1. Määrittele 3-4 työkalua, jotka olisivat hyödyllisiä tämän ongelman ratkaisemisessa
2. Luo työnkulun kaavio, joka näyttää, miten nämä työkalut vuorovaikuttavat
3. Toteuta yksinkertainen versio yhdestä työkaluista käyttämällä suosikkikieltäsi
4. Luo kehotemalli, joka auttaisi mallia käyttämään työkalua tehokkaasti

## Lisäresurssit

---

## Mitä seuraavaksi

Seuraavaksi: [Edistyneet aiheet](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ota huomioon, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen omalla kielellä on virallinen lähde. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa mahdollisista väärinymmärryksistä tai tulkinnoista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->