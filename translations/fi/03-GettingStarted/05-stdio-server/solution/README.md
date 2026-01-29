# MCP stdio-palvelinratkaisut

> **⚠️ Tärkeää**: Nämä ratkaisut on päivitetty käyttämään **stdio-kuljetusta** MCP-määrittelyn 2025-06-18 suositusten mukaisesti. Alkuperäinen SSE (Server-Sent Events) -kuljetus on poistettu käytöstä.

Tässä ovat täydelliset ratkaisut MCP-palvelimien rakentamiseen stdio-kuljetusta käyttäen eri ajoympäristöissä:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Täydellinen stdio-palvelimen toteutus
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Python-stdio-palvelin asyncio-kirjastolla
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - .NET-stdio-palvelin riippuvuuksien injektoinnilla

Jokainen ratkaisu esittelee:
- Stdio-kuljetuksen käyttöönoton
- Palvelintyökalujen määrittelyn
- Oikeaoppisen JSON-RPC-viestien käsittelyn
- Integraation MCP-asiakkaiden, kuten Clauden, kanssa

Kaikki ratkaisut noudattavat nykyistä MCP-määrittelyä ja käyttävät suositeltua stdio-kuljetusta parhaan suorituskyvyn ja turvallisuuden takaamiseksi.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.