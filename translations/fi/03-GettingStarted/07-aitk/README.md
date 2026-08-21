# Palvelimen käyttäminen AI Toolkit -laajennuksesta Visual Studio Codeen

Rakentaessasi tekoälyagenttia kyse ei ole pelkästään älykkäiden vastausten luomisesta; kyse on myös agentillesi annettavasta kyvystä toimia. Tässä astuu kuvaan Model Context Protocol (MCP). MCP helpottaa agenttien pääsyä ulkoisiin työkaluihin ja palveluihin johdonmukaisella tavalla. Voit ajatella sitä ikään kuin agenttisi liittämisenä työkalupakkiin, jota se *tosiasiassa* voi käyttää.

Sanotaanpa, että yhdistät agentin laskin-MCP-palvelimeesi. Yhtäkkiä agenttisi voi suorittaa matemaattisia laskutoimituksia vastaanottamalla vain kehotteen, kuten "Paljonko on 47 kertaa 89?" — logiikkaa ei tarvitse kovakoodata tai rakentaa mukautettuja API-rajapintoja.

## Yleiskatsaus

Tässä oppitunnissa käsitellään, miten yhdistää laskin-MCP-palvelin agenttiin [AI Toolkit](https://aka.ms/AIToolkit) -laajennuksen avulla Visual Studio Codessa, jolloin agentti voi suorittaa matematiikan operaatioita, kuten yhteen- ja vähennyslaskuja, kertolaskua ja jakolaskua luonnollisen kielen avulla.

AI Toolkit on tehokas Visual Studio Code -laajennus, joka virtaviivaistaa agenttien kehitystä. AI-suunnittelijat voivat helposti rakentaa tekoälysovelluksia kehittämällä ja testaamalla generatiivisia tekoälymalleja — paikallisesti tai pilvessä. Laajennus tukee useimpia nykyisin saatavilla olevia generatiivisia malleja.

*Huomautus*: AI Toolkit tukee tällä hetkellä Pythonia ja TypeScriptiä.

## Oppimistavoitteet

Oppitunnin lopussa osaat:

- Käyttää MCP-palvelinta AI Toolkitin kautta.
- Konfiguroida agentti löytämään ja käyttämään MCP-palvelimen tarjoamia työkaluja.
- Hyödyntää MCP-työkaluja luonnollisen kielen avulla.

## Lähestymistapa

Tässä on korkean tason lähestymistapamme:

- Luo agentti ja määritä sen järjestelmäkehotus.
- Luo MCP-palvelin laskimen työkaluilla.
- Yhdistä Agent Builder MCP-palvelimeen.
- Testaa agentin työkalukutsut luonnollisen kielen avulla.

Hienoa, kun ymmärrämme työnkulun, konfiguroidaan tekoälyagentti hyödyntämään ulkoisia työkaluja MCP:n kautta, parantaen sen kykyjä!

## Vaatimukset

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Harjoitus: Palvelimen käyttäminen

> [!WARNING]
> Huomio macOS-käyttäjille. Tutkimme tällä hetkellä riippuvuuksien asennukseen liittyvää ongelmaa macOS:llä. Tämän seurauksena macOS-käyttäjät eivät tällä hetkellä pysty suorittamaan tätä opasta loppuun. Päivitämme ohjeet heti, kun korjaus on saatavilla. Kiitos kärsivällisyydestä ja ymmärryksestä!

Tässä harjoituksessa rakennat, suoritat ja laajennat tekoälyagenttia MCP-palvelimen työkalujen avulla Visual Studio Codessa AI Toolkit -laajennusta käyttäen.

### -0- Esivaihe, lisää OpenAI GPT-4o malli Omiin malleihin

Harjoitus hyödyntää **GPT-4o** mallia. Malli tulee lisätä **Omiin malleihin** ennen agentin luontia.

![Näyttökuva mallin valintaliittymästä Visual Studio Coden AI Toolkit -laajennuksessa. Otsikkona "Löydä oikea malli AI-ratkaisuusi" ja alaotsikkona kehotus löytää, testata ja ottaa käyttöön AI-malleja. Alla "Suositut mallit" -kohdassa kuusi mallikorttia: DeepSeek-R1 (GitHubilla ylläpidetty), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Pieni, Nope), ja DeepSeek-R1 (Ollama-ylläpidetty). Jokaisessa kortissa vaihtoehdot "Lisää" ja "Kokeile leikkikentällä"](../../../../translated_images/fi/aitk-model-catalog.2acd38953bb9c119.webp)

1. Avaa **AI Toolkit** -laajennus **Activity Bar**:sta.
1. Valitse **Luettelo**-osiosta **Mallit** avataksesi **Malliluettelon**. Mallien valinta avaa uuden editorin välilehden Malliluettelolle.
1. Kirjoita Malliluettelon hakupalkkiin **OpenAI GPT-4o**.
1. Klikkaa **+ Lisää** lisätäksesi mallin Omiin malleihin. Varmista, että valittu malli on **GitHubilla ylläpidetty**.
1. Tarkista Activity Barista, että **OpenAI GPT-4o** malli näkyy listalla.

### -1- Luo agentti

**Agent (Prompt) Builder** mahdollistaa oman tekoälyavusteisen agentin luomisen ja muokkaamisen. Tässä osassa luot uuden agentin ja valitset mallin, joka tehostaa keskustelua.

![Näyttökuva "Calculator Agent" -rakentajan käyttöliittymästä AI Toolkit -laajennuksessa Visual Studio Codessa. Vasemmassa paneelissa valittu malli on "OpenAI GPT-4o (GitHubin kautta)." Järjestelmäkehotus on "Olet matematiikan professori yliopistossa," ja käyttäjän kehotus "Selitä Fourier'n yhtälö yksinkertaisesti." Lisävaihtoehtoina painikkeet työkalujen lisäämiseen, MCP-palvelimen käyttöön ottamiseen ja rakenteellisen tulosteen valintaan. Alhaalla sininen "Suorita" -painike. Oikeassa paneelissa "Aloita esimerkeillä" -osiosta löytyvät kolme näytteenomaista agenttia: Web Developer (MCP-palvelimella, Toisen luokan yksinkertaistaja ja Unien tulkitsija, jokaisella lyhyt kuvaus toiminnastaan.)](../../../../translated_images/fi/aitk-agent-builder.901e3a2960c3e477.webp)

1. Avaa **AI Toolkit** -laajennus **Activity Bar**:sta.
1. Valitse **Työkalut**-osiosta **Agent (Prompt) Builder**. Tämä avaa uuden editorin välilehden.
1. Klikkaa **+ Uusi agentti** -painiketta. Laajennus käynnistää asetustyökalun **Komento-palettin** kautta.
1. Anna agentille nimi **Calculator Agent** ja paina **Enter**.
1. Agent (Prompt) Builderissa valitse **Malliksi** **OpenAI GPT-4o (GitHubin kautta)**.

### -2- Luo agentille järjestelmäkehotus

Kun agentin runko on luotu, määritä sen persoonallisuus ja tarkoitus. Tässä osassa käytät **Luo järjestelmäkehotus** -ominaisuutta kuvaamaan agentin tavoitteet — tässä tapauksessa laskinagentti — ja annat mallin kirjoittaa sinulle järjestelmäkehotuksen.

![Näyttökuva "Calculator Agent" -liittymästä AI Toolkitissa Visual Studio Codessa, jossa avoinna modaalinen ikkuna nimeltä "Luo kehotus". Ikkuna selittää, että kehotuspohja voidaan luoda jakamalla perus tietoa. Tekstikentässä esimerkkijärjestelmäkehotus: "Olet avulias ja tehokas matematiikka-avustaja. Saattaessasi peruslaskutehtävän, vastaat oikealla tuloksella." Ikkunan alareunassa ovat "Sulje" ja "Luo" -painikkeet. Taustalla näkyy osittain agentin konfiguraatio, jossa valittu malli "OpenAI GPT-4o (GitHubin kautta)" ja kentät järjestelmä- ja käyttäjäkehotuksille.](../../../../translated_images/fi/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Kehotukset-osiosta valitse **Luo järjestelmäkehotus** -painike. Se avaa kehotusrakentajan, joka käyttää tekoälyä luodakseen järjestelmäkehotuksen agentille.
1. Kirjoita **Luo kehotus** -ikkunaan seuraava teksti: `Olet avulias ja tehokas matematiikka-avustaja. Saattaessasi peruslaskutehtävän, vastaat oikealla tuloksella.`
1. Klikkaa **Luo** -painiketta. Ilmoitus näkyy oikeassa alakulmassa vahvistaen, että järjestelmäkehotus luodaan. Kun luonti on valmis, kehotus ilmestyy **Agent (Prompt) Builderin** Järjestelmäkehotus-kenttään.
1. Tarkista järjestelmäkehotus ja muokkaa tarvittaessa.

### -3- Luo MCP-palvelin

Nyt kun olet määrittänyt agenttisi järjestelmäkehotuksen — joka ohjaa sen käyttäytymistä ja vastauksia — on aika varustaa agentti käytännöllisillä ominaisuuksilla. Tässä osassa luot laskin-MCP-palvelimen, joka sisältää työkalut yhteen-, vähennys-, kerto- ja jakolaskujen suorittamiseen. Tämä palvelin antaa agentille mahdollisuuden suorittaa reaaliaikaisia matemaattisia operaatioita luonnollisen kielen kehotusten perusteella.

![Näyttökuva Calculator Agent -liittymän alaosasta AI Toolkit -laajennuksessa Visual Studio Codessa. Näkyvissä ovat laajennettavat valikot "Tools" ja "Structure output", sekä alasvetovalikko "Choose output format" asetettuna "text." Oikealla on "+ MCP Server" -painike Model Context Protocol -palvelimen lisäämiseen. Yläpuolella näkyy paikkakuva kuvakkeelle.](../../../../translated_images/fi/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit sisältää malleja, jotka helpottavat oman MCP-palvelimen luomista. Käytämme Python-mallipohjaa laskin-MCP-palvelimen luomiseen.

*Huomautus*: AI Toolkit tukee tällä hetkellä Pythonia ja TypeScriptiä.

1. Agent (Prompt) Builderin **Työkalut**-osiosta klikkaa **+ MCP Server** -painiketta. Laajennus käynnistää asetustyökalun **Komento-palettin** kautta.
1. Valitse **+ Lisää palvelin**.
1. Valitse **Luo uusi MCP-palvelin**.
1. Valitse mallipohjaksi **python-weather**.
1. Valitse **Oletuskansio** tallennuspaikaksi MCP-palvelimen mallipohjalle.
1. Anna palvelimelle nimi: **Calculator**
1. Uusi Visual Studio Code -ikkuna avautuu. Valitse **Kyllä, luotan tekijöihin**.
1. Käyttäen terminaalia (**Terminal** > **New Terminal**), luo virtuaaliympäristö: `python -m venv .venv`
1. Aktivoi virtuaaliympäristö terminaalissa:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Asenna riippuvuudet terminaalissa: `pip install -e .[dev]`
1. **Explorer**-näkymässä avaa **src**-hakemisto ja valitse **server.py** tiedosto editorissa.
1. Korvaa **server.py** -tiedoston sisältö seuraavalla ja tallenna:

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- Suorita agentti laskin-MCP-palvelimella

Nyt kun agentilla on työkalut, on aika käyttää niitä! Tässä osassa lähetät kehotteita agentille testataksesi ja vahvistaaksesi, käyttääkö agentti oikeaa työkalua laskin-MCP-palvelimelta.

![Näyttökuva Calculator Agentin käyttöliittymästä AI Toolkit -laajennuksessa Visual Studio Codessa. Vasemmalla "Tools" -osiossa on lisätty MCP-palvelin nimeltä local-server-calculator_server, jossa on neljä käytettävissä olevaa työkalua: add, subtract, multiply ja divide. Neljä työkalua on aktiivisia. Alempana on kytketty "Structure output" -osio ja sininen "Run" -painike. Oikealla "Model Response" -osiossa agentti kutsuu multiply- ja subtract-työkaluja syötteillä {"a": 3, "b": 25} ja {"a": 75, "b": 20}. Lopullinen "Tool Response" on 75.0. Alhaalla on "View Code" -painike.](../../../../translated_images/fi/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Suoritat laskin-MCP-palvelimen paikallisella kehityskoneellasi **Agent Builder**in kautta MCP-asiakkaana.

1. Paina `F5` aloittaaksesi MCP-palvelimen virheenkorjauksen. **Agent (Prompt) Builder** avautuu uuteen editorin välilehteen. Palvelimen tila näkyy terminaalissa.
1. Kirjoita **Käyttäjän kehotus** -kenttään **Agent (Prompt) Builderissa** seuraava kehotus: `Ostin 3 kappaletta, joiden hinta oli 25 $ kappaleelta, ja käytin sitten 20 $ alennuksen. Paljonko maksoin?`
1. Klikkaa **Suorita** tuottaaksesi agentin vastauksen.
1. Tarkista agentin tuloste. Mallin tulisi päätyä siihen, että maksoit **55 dollaria**.
1. Tässä mitä tapahtuu:
    - Agentti valitsee **multiply** ja **subtract** -työkalut laskutoimitusten avuksi.
    - Työkalulle **multiply** annetaan arvot `a` ja `b`.
    - Työkalulle **subtract** annetaan arvot `a` ja `b`.
    - Kunkin työkalun vastaus annetaan **Tool Response** -kentässä.
    - Mallin lopullinen vastaus näkyy **Model Response** -kentässä.
1. Lähetä lisää kehotteita testataksesi agenttia. Voit muuttaa nykyistä kehotetta **Käyttäjän kehotus** -kentässä muokkaamalla tekstiä.
1. Kun olet valmis testaamaan agenttia, voit lopettaa palvelimen terminaalissa painamalla **CTRL/CMD+C**.

## Tehtävä

Yritä lisätä uusi työkalu **server.py** -tiedostoosi (esim. laskea luvun neliöjuuri). Lähetä uusia kehotteita, jotka vaativat agenttia käyttämään uutta työkalua (tai olemassa olevia työkaluja). Muista käynnistää palvelin uudelleen, jotta juuri lisäämäsi työkalut latautuvat.

## Ratkaisu

[Ratkaisu](./solution/README.md)

## Tärkeimmät opit

Tässä luvussa opittua:

- AI Toolkit -laajennus on erinomainen asiakas, jonka avulla voit käyttää MCP-palvelimia ja niiden työkaluja.
- Voit lisätä uusia työkaluja MCP-palvelimiin, laajentaen agentin kyvykkyyttä vastaamaan kehittyviä vaatimuksia.
- AI Toolkit sisältää mallipohjia (esim. Python MCP-palvelinmallit) helpottamaan mukautettujen työkalujen luomista.

## Lisäresurssit

- [AI Toolkit dokumentaatio](https://aka.ms/AIToolkit/doc)

## Mitä seuraavaksi
- Seuraava: [Testaus & virheenkorjaus](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->