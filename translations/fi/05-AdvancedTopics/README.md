# Edistyneet aiheet MCP:ssä

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/fi/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Klikkaa yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

Tässä luvussa käsitellään useita edistyneitä aiheita Model Context Protocolin (MCP) toteutuksessa, mukaan lukien monimuotoiset integraatiot, skaalautuvuus, tietoturvan parhaat käytännöt ja yritysintegrointi. Nämä aiheet ovat ratkaisevan tärkeitä kestävien ja tuotantovalmiiden MCP-sovellusten rakentamisessa, jotka voivat vastata nykyaikaisten tekoälyjärjestelmien vaatimuksiin.

## Yleiskuvaus

Tämä oppitunti tutkii edistyneitä käsitteitä Model Context Protocolin toteutuksessa, keskittyen monimuotoiseen integraatioon, skaalautuvuuteen, tietoturvan parhaisiin käytäntöihin ja yritysintegrointiin. Nämä aiheet ovat olennaisia tuotantotason MCP-sovellusten rakentamisessa, jotka pystyvät käsittelemään monimutkaisia vaatimuksia yritysympäristöissä.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Toteuttaa monimuotoisia ominaisuuksia MCP-kehyksissä
- Suunnitella skaalautuvia MCP-arkkitehtuureja vaativiin käyttötapauksiin
- Soveltaa MCP:n tietoturvaperiaatteiden mukaisia parhaimpia tietoturvakäytäntöjä
- Integroitu MCP yritysten tekoälyjärjestelmiin ja kehyksiin
- Optimoida suorituskykyä ja luotettavuutta tuotantoympäristöissä

## Oppitunnit ja esimerkkiprojektit

| Linkki | Otsikko | Kuvaus |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Integrointi Azureen | Opi integroimaan MCP-palvelimesi Azureen |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCP Monimuotoiset esimerkit | Näytteitä ääni-, kuva- ja monimuotoisista vasteista |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimalistinen Spring Boot -sovellus, joka näyttää OAuth2:n käytön MCP:n kanssa sekä valtuutus- että resurssipalvelimena. Esittelee turvallisen tunnistetokenin myöntämisen, suojatut päätepisteet, Azure Container Apps -käyttöönoton ja API Management -integraation. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Juurikontekstit | Lisätietoa juurikontekstista ja sen toteutuksesta |
| [5.5 Routing](./mcp-routing/README.md) | Reititys | Opettele erilaisia reititystyyppejä |
| [5.6 Sampling](./mcp-sampling/README.md) | Otanta | Opettele työskentelemään otannan kanssa |
| [5.7 Scaling](./mcp-scaling/README.md) | Skaalaus | Opettele skaalaamisesta |
| [5.8 Security](./mcp-security/README.md) | Tietoturva | Suojaa MCP-palvelimesi |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Verkkohaku MCP | Python MCP-palvelin ja asiakas integroituen SerpAPI:in reaaliaikaiseen verkko-, uutis-, tuotetietojen hakuun ja kysymyksiin. Esittelee monityökaluyhteensovittamista, ulkoisten API:en integraatiota ja vankkaa virheenkäsittelyä. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Suoratoisto | Reaaliaikainen tietovirta on nykypäivän dataohjautuvassa maailmassa välttämätöntä, sillä yritykset ja sovellukset tarvitsevat välitöntä pääsyä tietoihin oikea-aikaisten päätösten tueksi. |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Verkkohaku | Reaaliaikainen verkkohaku ja miten MCP muuttaa reaaliaikaista verkkohakua tarjoamalla standardoidun lähestymistavan kontekstinhallintaan tekoälymallien, hakukoneiden ja sovellusten välillä. | 
| [5.12 Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID -todennus | Microsoft Entra ID tarjoaa vankan pilvipohjaisen identiteetin ja pääsynhallinnan ratkaisun varmistaen, että vain valtuutetut käyttäjät ja sovellukset voivat olla vuorovaikutuksessa MCP-palvelimesi kanssa. |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry -integraatio | Opi integroimaan Model Context Protocol -palvelimet Azure AI Foundry -agenteihin, mahdollistaen tehokkaan työkalujen yhteensovittamisen ja yritysten tekoälyominaisuudet standardoitujen ulkoisten tietolähteiden liitäntöjen avulla. |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Konteksti-insinöörityö | Konteksti-insinöörityömenetelmien tulevaisuuden mahdollisuudet MCP-palvelimille, mukaan lukien kontekstin optimointi, dynaaminen kontekstinhallinta ja tehokkaan kehotetun suunnittelun strategiat MCP-kehyksissä. |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Räätälöity tiedonsiirto | Opi toteuttamaan räätälöityjä siirtomekanismeja erikoistuneisiin MCP-viestintätilanteisiin. |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Protokollan ominaisuudet | Hallitse kehittyneitä protokollan ominaisuuksia, mukaan lukien etenemisilmoitukset, pyyntöjen peruutus, resurssipohjat ja virheenkäsittelymallit. |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Vastakkaiset agentit | Käytä kahta vastakkaisilla kannoilla olevaa agenttia, jotka jakavat yhden MCP-työkalupaketin hallitakseen harhoja, paljastaakseen epätavalliset tapaukset ja tuottaakseen paremmin kalibroituja vastauksia rakenteellisen väittelyn kautta. |

> **Uutta MCP-määritelmässä 2025-11-25**: Määritelmä sisältää nyt kokeellisen tuen **tehtäville** (pitkäkestoiset operaatiot etenemisen seurannalla), **työkaluanotaatioille** (metadataa työkalujen käyttäytymisestä turvallisuutta varten), **URL-tilan indusoinnille** (asiakaspyyntöjä tietyn URL-sisällön hakemiseksi) ja parannetuille **juurille** (työtilakontekstinhallintaan). Katso [MCP-määritelmän muutokset](https://spec.modelcontextprotocol.io/) saadaksesi täydelliset yksityiskohdat.

## Lisäviitteet

Ajantasaisimman tiedon edistyneistä MCP-aiheista saat seuraavista lähteistä:
- [MCP-dokumentaatio](https://modelcontextprotocol.io/)
- [MCP-määritelmä (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub-repositorio](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Tietoturvariskit ja niiden lieventäminen
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Käytännön tietoturvakoulutus

## Keskeiset opit

- Monimuotoiset MCP-toteutukset laajentavat tekoälyn kyvykkyyksiä tekstinkäsittelyn ulkopuolelle
- Skaalautuvuus on välttämätöntä yritysympäristöissä ja sitä voidaan ratkaista horisontaalisella ja vertikaalisella skaalaamisella
- Laajat tietoturvatoimet suojaavat dataa ja varmistavat asianmukaisen pääsynvalvonnan
- Yritysintegrointi alustoilla kuten Azure OpenAI ja Microsoft AI Foundry parantaa MCP:n toiminnallisuutta
- Edistyneet MCP-toteutukset hyötyvät optimoiduista arkkitehtuureista ja huolellisesta resurssien hallinnasta

## Harjoitus

Suunnittele yritystason MCP-toteutus tietylle käyttötapaukselle:

1. Tunnista käyttötapauksen monimuotoiset vaatimukset
2. Laadi turvallisuusvalvontatoimet arkaluontoisen datan suojaamiseksi
3. Suunnittele skaalautuva arkkitehtuuri, joka kestää vaihtelevaa kuormitusta
4. Suunnittele integraatiopisteet yrityksen tekoälyjärjestelmiin
5. Dokumentoi mahdolliset suorituskykyä rajoittavat pullonkaulat ja lieventämisstrategiat

## Lisäresurssit

- [Azure OpenAI -dokumentaatio](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry -dokumentaatio](https://learn.microsoft.com/en-us/ai-services/)

---

## Mitä seuraavaksi

Tutustu tämän moduulin oppitunteihin aloittaen: [5.1 MCP Integration](./mcp-integration/README.md)

Kun olet suorittanut tämän moduulin, jatka: [Moduuli 6: Yhteisön panokset](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, on hyvä huomioida, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen omalla kielellä tulee pitää virallisena lähteenä. Keskeisissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai tulkintavirheistä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->