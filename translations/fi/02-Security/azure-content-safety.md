# Edistynyt MCP-turvallisuus Azure Content Safetyn avulla

Azure Content Safety tarjoaa useita tehokkaita työkaluja, jotka voivat parantaa MCP-ratkaisujesi turvallisuutta:

## Prompt Shields

Microsoftin AI Prompt Shields tarjoaa vahvan suojan sekä suoria että epäsuoria prompt-injektiohyökkäyksiä vastaan seuraavilla tavoilla:

1. **Edistynyt tunnistus**: Käyttää koneoppimista haitallisten ohjeiden tunnistamiseen sisällössä.
2. **Korostus**: Muokkaa syötetekstiä auttaakseen AI-järjestelmiä erottamaan pätevät ohjeet ulkoisista syötteistä.
3. **Erotinmerkit ja datamerkintä**: Merkitsee rajat luotettavan ja epäluotettavan datan välillä.
4. **Content Safety -integraatio**: Toimii yhdessä Azure AI Content Safetyn kanssa havaitakseen jailbreak-yritykset ja haitallisen sisällön.
5. **Jatkuvat päivitykset**: Microsoft päivittää säännöllisesti suojausmekanismeja uusia uhkia vastaan.

## Azure Content Safetyn käyttöönotto MCP:n kanssa

Tämä lähestymistapa tarjoaa monikerroksisen suojan:
- Syötteiden skannaus ennen käsittelyä
- Tulosten validointi ennen palauttamista
- Estolistojen käyttö tunnetuille haitallisille malleille
- Azure Content Safetyn jatkuvasti päivitettyjen mallien hyödyntäminen

## Azure Content Safety -resurssit

Lisätietoja Azure Content Safetyn käyttöönotosta MCP-palvelimillasi löydät näistä virallisista lähteistä:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Virallinen dokumentaatio Azure Content Safetystä.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Opas prompt-injektiohyökkäysten estämiseen.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Yksityiskohtainen API-viite Content Safetyn toteuttamiseen.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Nopean käyttöönoton opas C#:lla.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Asiakasohjelmistokirjastot eri ohjelmointikielille.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Tarkemmat ohjeet jailbreak-yritysten havaitsemiseen ja estämiseen.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Parhaat käytännöt Content Safetyn tehokkaaseen toteutukseen.

Syvällisempää toteutusta varten katso [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.