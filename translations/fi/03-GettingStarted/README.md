## Aloittaminen  

[![Luo ensimmäinen MCP-palvelimesi](../../../translated_images/fi/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.png)](https://youtu.be/sNDZO9N4m9Y)

_(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Tämä osio sisältää useita oppitunteja:

- **1 Ensimmäinen palvelimesi**, tässä ensimmäisessä oppitunnissa opit luomaan ensimmäisen palvelimesi ja tarkastelemaan sitä tarkastustyökalulla, joka on arvokas tapa testata ja debugata palvelintasi, [siirry oppituntiin](01-first-server/README.md)

- **2 Asiakas**, tässä oppitunnissa opit kirjoittamaan asiakkaan, joka voi muodostaa yhteyden palvelimeesi, [siirry oppituntiin](02-client/README.md)

- **3 Asiakas LLM:n kanssa**, vielä parempi tapa kirjoittaa asiakas on lisätä siihen LLM, jotta se voi "neuvotella" palvelimesi kanssa siitä, mitä tehdä, [siirry oppituntiin](03-llm-client/README.md)

- **4 Palvelimen käyttö GitHub Copilot Agent -tilassa Visual Studio Codessa**. Tässä tarkastellaan MCP-palvelimen suorittamista Visual Studio Codessa, [siirry oppituntiin](04-vscode/README.md)

- **5 stdio Transport Server** stdio-kuljetus on nykyisen MCP-määrityksen suositeltu standardi palvelimen ja asiakkaan väliseen viestintään, tarjoten turvallisen aliprosessipohjaisen viestinnän [siirry oppituntiin](05-stdio-server/README.md)

- **6 HTTP-suoratoisto MCP:n kanssa (Streamable HTTP)**. Opit modernista HTTP-suoratoistosta, etenemisen ilmoituksista ja siitä, miten toteuttaa skaalautuvia, reaaliaikaisia MCP-palvelimia ja -asiakkaita Streamable HTTP:n avulla. [siirry oppituntiin](06-http-streaming/README.md)

- **7 AI Toolkitin hyödyntäminen VSCode:ssa** MCP-asiakkaiden ja -palvelimien kuluttamiseen ja testaamiseen [siirry oppituntiin](07-aitk/README.md)

- **8 Testaus**. Tässä keskitytään erityisesti siihen, miten palvelinta ja asiakasta voidaan testata eri tavoilla, [siirry oppituntiin](08-testing/README.md)

- **9 Käyttöönotto**. Tässä luvussa tarkastellaan erilaisia tapoja ottaa MCP-ratkaisut käyttöön, [siirry oppituntiin](09-deployment/README.md)

- **10 Edistynyt palvelimen käyttö**. Tämä luku kattaa edistyneen palvelimen käytön, [siirry oppituntiin](./10-advanced/README.md)

- **11 Tunnistus**. Tämä luku käsittelee, miten lisätä yksinkertainen tunnistus, Basic Authista JWT:n ja RBAC:n käyttöön. Suositellaan aloittamaan tästä ja sitten tarkastelemaan edistyneitä aiheita luvussa 5 sekä suorittamaan lisäturvatoimenpiteitä luvun 2 suositusten mukaisesti, [siirry oppituntiin](./11-simple-auth/README.md)

Model Context Protocol (MCP) on avoin protokolla, joka standardoi, miten sovellukset tarjoavat kontekstia LLM:ille. Ajattele MCP:tä kuin USB-C-porttia AI-sovelluksille - se tarjoaa standardoidun tavan yhdistää AI-malleja eri tietolähteisiin ja työkaluihin.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Määrittää MCP-kehitysympäristöt C#:lle, Javalle, Pythonille, TypeScriptille ja JavaScriptille
- Rakentaa ja ottaa käyttöön perus-MCP-palvelimia mukautetuilla ominaisuuksilla (resurssit, kehotteet ja työkalut)
- Luoda isäntäsovelluksia, jotka yhdistyvät MCP-palvelimiin
- Testata ja debugata MCP-toteutuksia
- Ymmärtää yleisiä asennushaasteita ja niiden ratkaisuja
- Yhdistää MCP-toteutuksesi suosittuihin LLM-palveluihin

## MCP-ympäristön asennus

Ennen kuin aloitat MCP:n parissa työskentelyn, on tärkeää valmistella kehitysympäristösi ja ymmärtää perusprosessit. Tämä osio opastaa sinut alkuasennuksen vaiheiden läpi varmistaen sujuvan aloituksen MCP:n kanssa.

### Esivaatimukset

Ennen MCP-kehitykseen sukeltamista varmista, että sinulla on:

- **Kehitysympäristö**: Valitsemallesi kielelle (C#, Java, Python, TypeScript tai JavaScript)
- **IDE/editori**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm tai mikä tahansa moderni koodieditori
- **Paketinhallintaohjelmat**: NuGet, Maven/Gradle, pip tai npm/yarn
- **API-avaimet**: AI-palveluille, joita aiot käyttää isäntäsovelluksissasi

### Viralliset SDK:t

Tulevissa luvuissa näet ratkaisuja, jotka on rakennettu Pythonilla, TypeScriptillä, Javalla ja .NET:llä. Tässä ovat kaikki virallisesti tuetut SDK:t.

MCP tarjoaa virallisia SDK:ita useille kielille:
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Ylläpidetään yhteistyössä Microsoftin kanssa
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Ylläpidetään yhteistyössä Spring AI:n kanssa
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Virallinen TypeScript-toteutus
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Virallinen Python-toteutus
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Virallinen Kotlin-toteutus
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Ylläpidetään yhteistyössä Loopwork AI:n kanssa
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Virallinen Rust-toteutus

## Keskeiset opit

- MCP-kehitysympäristön asennus on suoraviivaista kielikohtaisten SDK:iden avulla
- MCP-palvelimien rakentaminen sisältää työkalujen luomisen ja rekisteröinnin selkeillä kaavioilla
- MCP-asiakkaat yhdistyvät palvelimiin ja malleihin hyödyntääkseen laajennettuja ominaisuuksia
- Testaus ja debuggaus ovat olennaisia luotettaville MCP-toteutuksille
- Käyttöönotto voi tapahtua paikallisesta kehityksestä pilvipohjaisiin ratkaisuihin

## Harjoittelu

Meillä on joukko esimerkkejä, jotka täydentävät tämän osion kaikkien lukujen harjoituksia. Lisäksi jokaisessa luvussa on omat harjoituksensa ja tehtävänsä.

- [Java-laskin](./samples/java/calculator/README.md)
- [.Net-laskin](../../../03-GettingStarted/samples/csharp)
- [JavaScript-laskin](./samples/javascript/README.md)
- [TypeScript-laskin](./samples/typescript/README.md)
- [Python-laskin](../../../03-GettingStarted/samples/python)

## Lisäresurssit

- [Rakenna agentteja Model Context Protocolilla Azureen](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Etä-MCP Azure Container Appsilla (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Mitä seuraavaksi

Seuraavaksi: [Ensimmäisen MCP-palvelimen luominen](01-first-server/README.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.