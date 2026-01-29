# Case Study: Azure AI Travel Agents – Referenssitoteutus

## Yleiskatsaus

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) on Microsoftin kehittämä kattava referenssiratkaisu, joka havainnollistaa, miten rakentaa monen agentin AI-pohjainen matkasuunnittelu-sovellus käyttäen Model Context Protocolia (MCP), Azure OpenAI:ta ja Azure AI Searchia. Tämä projekti esittelee parhaita käytäntöjä useiden AI-agenttien orkestroinnissa, yritystiedon integroinnissa sekä turvallisen ja laajennettavan alustan tarjoamisessa todellisiin käyttötapauksiin.

## Keskeiset ominaisuudet
- **Moni-agenttien orkestrointi:** Käyttää MCP:tä koordinoimaan erikoistuneita agentteja (esim. lento-, hotelli- ja matkareittiagentit), jotka tekevät yhteistyötä monimutkaisten matkasuunnittelutehtävien toteuttamiseksi.
- **Yritystiedon integrointi:** Yhdistää Azure AI Searchiin ja muihin yritystietolähteisiin tarjoten ajantasaista ja relevanttia tietoa matkasuosituksia varten.
- **Turvallinen ja skaalautuva arkkitehtuuri:** Hyödyntää Azure-palveluita todennukseen, valtuutukseen ja skaalautuvaan käyttöönottoon noudattaen yritysturvallisuuden parhaita käytäntöjä.
- **Laajennettavat työkalut:** Toteuttaa uudelleenkäytettäviä MCP-työkaluja ja kehotemalleja, jotka mahdollistavat nopean sopeutumisen uusiin toimialoihin tai liiketoimintavaatimuksiin.
- **Käyttäjäkokemus:** Tarjoaa keskustelupohjaisen käyttöliittymän, jonka kautta käyttäjät voivat olla vuorovaikutuksessa matkatoimistojen agenttien kanssa, hyödyntäen Azure OpenAI:ta ja MCP:tä.

## Arkkitehtuuri
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Arkkitehtuurikaavion kuvaus

Azure AI Travel Agents -ratkaisu on suunniteltu modulaariseksi, skaalautuvaksi ja turvalliseksi useiden AI-agenttien ja yritystietolähteiden integroinnille. Pääkomponentit ja tiedonkulku ovat seuraavat:

- **Käyttöliittymä:** Käyttäjät ovat vuorovaikutuksessa järjestelmän kanssa keskustelupohjaisen käyttöliittymän kautta (esim. verkkokeskustelu tai Teams-botti), joka lähettää käyttäjän kyselyt ja vastaanottaa matkasuositukset.
- **MCP Server:** Toimii keskeisenä orkestroijana, vastaanottaa käyttäjän syötteen, hallinnoi kontekstia ja koordinoi erikoistuneiden agenttien (esim. FlightAgent, HotelAgent, ItineraryAgent) toimintaa Model Context Protocolin avulla.
- **AI-agentit:** Jokainen agentti vastaa omasta toimialueestaan (lennot, hotellit, matkareitit) ja on toteutettu MCP-työkaluna. Agentit käyttävät kehotemalleja ja logiikkaa käsitelläkseen pyyntöjä ja tuottaakseen vastauksia.
- **Azure OpenAI Service:** Tarjoaa kehittynyttä luonnollisen kielen ymmärrystä ja generointia, mahdollistaen agenttien tulkita käyttäjän aikomuksia ja tuottaa keskustelullisia vastauksia.
- **Azure AI Search & Yritystieto:** Agentit hakevat Azure AI Searchista ja muista yritystietolähteistä ajantasaista tietoa lennoista, hotelleista ja matkavaihtoehdoista.
- **Todennus ja turvallisuus:** Integroituu Microsoft Entra ID:n kanssa turvallista todennusta varten ja soveltaa vähimmän oikeuden periaatetta kaikkiin resursseihin.
- **Käyttöönotto:** Suunniteltu käytettäväksi Azure Container Apps -ympäristössä, mikä takaa skaalautuvuuden, valvonnan ja operatiivisen tehokkuuden.

Tämä arkkitehtuuri mahdollistaa saumattoman moni-agenttien orkestroinnin, turvallisen yritystiedon integroinnin sekä vankan ja laajennettavan alustan toimialakohtaisten AI-ratkaisujen rakentamiseen.

## Arkkitehtuurikaavion vaiheittainen selitys
Kuvittele, että suunnittelet isoa matkaa ja sinulla on tiimi asiantuntija-avustajia auttamassa joka yksityiskohdassa. Azure AI Travel Agents -järjestelmä toimii samalla tavalla, käyttäen eri osia (kuin tiimin jäseniä), joilla jokaisella on oma erityistehtävänsä. Näin kaikki toimii yhdessä:

### Käyttöliittymä (UI):
Ajattele tätä kuin matkatoimistosi vastaanottoa. Siellä sinä (käyttäjä) esität kysymyksiä tai teet pyyntöjä, kuten ”Etsi lento Pariisiin.” Tämä voi olla verkkosivun chat-ikkuna tai viestisovellus.

### MCP Server (Koordinaattori):
MCP Server on kuin johtaja, joka kuuntelee pyyntöäsi vastaanotossa ja päättää, mikä asiantuntija hoitaa minkäkin osan. Se seuraa keskustelua ja varmistaa, että kaikki sujuu jouhevasti.

### AI-agentit (Asiantuntija-avustajat):
Jokainen agentti on oman alansa asiantuntija—yksi tuntee lennot, toinen hotellit ja kolmas matkareittien suunnittelun. Kun pyydät matkaa, MCP Server lähettää pyyntösi oikealle agentille tai agenteille. Nämä agentit käyttävät tietämystään ja työkalujaan löytääkseen sinulle parhaat vaihtoehdot.

### Azure OpenAI Service (Kieliasiantuntija):
Tämä on kuin kieliasiantuntija, joka ymmärtää tarkalleen, mitä pyydät, riippumatta siitä, miten sen ilmaiset. Se auttaa agentteja ymmärtämään pyyntösi ja vastaamaan luonnollisella, keskustelullisella kielellä.

### Azure AI Search & Yritystieto (Tietokirjasto):
Kuvittele valtava, ajantasainen kirjasto, jossa on kaikki viimeisimmät matkustustiedot—lentoaikataulut, hotellien saatavuus ja muuta. Agentit etsivät tästä kirjastosta tarkimmat vastaukset sinulle.

### Todennus ja turvallisuus (Turvamies):
Aivan kuten turvamies tarkistaa, kuka pääsee tiettyihin tiloihin, tämä osa varmistaa, että vain valtuutetut henkilöt ja agentit pääsevät käsiksi arkaluontoiseen tietoon. Se pitää tietosi turvassa ja yksityisinä.

### Käyttöönotto Azure Container Appsissa (Rakennus):
Kaikki nämä avustajat ja työkalut toimivat yhdessä turvallisessa, skaalautuvassa rakennuksessa (pilvessä). Tämä tarkoittaa, että järjestelmä pystyy palvelemaan monia käyttäjiä samanaikaisesti ja on aina käytettävissä, kun tarvitset sitä.

## Miten kaikki toimii yhdessä:

Aloitat esittämällä kysymyksen vastaanotossa (UI).
Johtaja (MCP Server) päättää, mikä asiantuntija (agentti) auttaa sinua.
Asiantuntija käyttää kieliasiantuntijaa (OpenAI) ymmärtääkseen pyyntösi ja kirjastoa (AI Search) löytääkseen parhaan vastauksen.
Turvamies (todennus) varmistaa, että kaikki on turvallista.
Kaikki tapahtuu luotettavassa, skaalautuvassa rakennuksessa (Azure Container Apps), joten käyttökokemuksesi on sujuva ja turvallinen.
Tämä tiimityö mahdollistaa järjestelmän nopean ja turvallisen avun matkasuunnittelussa, aivan kuin joukko asiantuntevia matkatoimistoagentteja työskentelisi yhdessä modernissa toimistossa!

## Tekninen toteutus
- **MCP Server:** Isännöi keskeistä orkestrointilogiikkaa, tarjoaa agenttityökaluja ja hallinnoi kontekstia monivaiheisissa matkasuunnitteluprosesseissa.
- **Agentit:** Jokainen agentti (esim. FlightAgent, HotelAgent) on toteutettu MCP-työkaluna omine kehotemalleineen ja logiikkoineen.
- **Azure-integraatio:** Käyttää Azure OpenAI:ta luonnollisen kielen ymmärtämiseen ja Azure AI Searchia tiedonhakuun.
- **Turvallisuus:** Integroituu Microsoft Entra ID:n kanssa todennusta varten ja soveltaa vähimmän oikeuden periaatetta kaikkiin resursseihin.
- **Käyttöönotto:** Tukee käyttöönottoa Azure Container Appsissa skaalautuvuuden ja operatiivisen tehokkuuden takaamiseksi.

## Tulokset ja vaikutus
- Havainnollistaa, miten MCP:tä voidaan käyttää useiden AI-agenttien orkestrointiin todellisessa, tuotantotason ympäristössä.
- Nopeuttaa ratkaisun kehitystä tarjoamalla uudelleenkäytettäviä malleja agenttien koordinointiin, tiedon integrointiin ja turvalliseen käyttöönottoon.
- Toimii pohjana toimialakohtaisten, AI-pohjaisten sovellusten rakentamiselle MCP:n ja Azure-palveluiden avulla.

## Viitteet
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.