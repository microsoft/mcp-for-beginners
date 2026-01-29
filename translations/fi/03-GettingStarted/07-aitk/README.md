# AI Toolkit -palvelimen käyttäminen Visual Studio Code -laajennuksessa

Kun rakennat tekoälyagenttia, kyse ei ole pelkästään älykkäiden vastausten tuottamisesta; kyse on myös agentin kyvystä toimia. Tässä kohtaa Model Context Protocol (MCP) astuu kuvaan. MCP mahdollistaa agenttien pääsyn ulkoisiin työkaluihin ja palveluihin yhtenäisellä tavalla. Voit ajatella sen kuin liittäisit agenttisi työkalupakkiin, jota se *oikeasti* voi käyttää.

Oletetaan, että yhdistät agentin laskin-MCP-palvelimeen. Yhtäkkiä agenttisi voi suorittaa matemaattisia operaatioita pelkän kehotteen, kuten "Mikä on 47 kertaa 89?", avulla—ilman, että sinun tarvitsee kovakoodata logiikkaa tai rakentaa mukautettuja API:ita.

## Yleiskatsaus

Tässä osiossa käsitellään, kuinka yhdistää laskin-MCP-palvelin agenttiin [AI Toolkit](https://aka.ms/AIToolkit) -laajennuksen avulla Visual Studio Codessa, jolloin agentti voi suorittaa matemaattisia operaatioita, kuten yhteen-, vähennys-, kerto- ja jakolaskuja luonnollisen kielen avulla.

AI Toolkit on tehokas laajennus Visual Studio Codeen, joka tehostaa agenttien kehitystä. Tekoälyinsinöörit voivat helposti rakentaa tekoälysovelluksia kehittämällä ja testaamalla generatiivisia tekoälymalleja—paikallisesti tai pilvessä. Laajennus tukee useimpia nykyään saatavilla olevia generatiivisia malleja.

*Huomio*: AI Toolkit tukee tällä hetkellä Pythonia ja TypeScriptiä.

## Oppimistavoitteet

Tämän osion lopussa osaat:

- Käyttää MCP-palvelinta AI Toolkitin kautta.
- Määrittää agentin konfiguraation, jotta se voi löytää ja hyödyntää MCP-palvelimen tarjoamia työkaluja.
- Käyttää MCP-työkaluja luonnollisen kielen avulla.

## Lähestymistapa

Näin etenemme yleisellä tasolla:

- Luo agentti ja määritä sen järjestelmäkehotus.
- Luo MCP-palvelin laskintyökaluilla.
- Yhdistä Agent Builder MCP-palvelimeen.
- Testaa agentin työkalujen käyttöä luonnollisen kielen avulla.

Hienoa, nyt kun ymmärrämme prosessin, konfiguroidaan tekoälyagentti hyödyntämään ulkoisia työkaluja MCP:n avulla ja parannetaan sen kyvykkyyksiä!

## Esivaatimukset

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Harjoitus: Palvelimen käyttäminen

> [!WARNING]
> Huomio macOS-käyttäjille. Tutkimme parhaillaan ongelmaa, joka vaikuttaa riippuvuuksien asennukseen macOS:ssä. Tämän vuoksi macOS-käyttäjät eivät tällä hetkellä voi suorittaa tätä opetusohjelmaa loppuun. Päivitämme ohjeet heti, kun korjaus on saatavilla. Kiitos kärsivällisyydestä ja ymmärryksestä!

Tässä harjoituksessa rakennat, suoritat ja parannat tekoälyagenttia MCP-palvelimen työkalujen avulla Visual Studio Codessa AI Toolkitin kautta.

### -0- Esivaihe: Lisää OpenAI GPT-4o -malli My Models -osioon

Harjoituksessa käytetään **GPT-4o**-mallia. Malli tulee lisätä **My Models** -osioon ennen agentin luomista.

![Kuvakaappaus Visual Studio Coden AI Toolkit -laajennuksen mallivalintaliittymästä. Otsikko kuuluu "Find the right model for your AI Solution" ja alaotsikko kehottaa käyttäjiä löytämään, testaamaan ja ottamaan käyttöön tekoälymalleja. Alla "Popular Models" -osiossa näkyy kuusi mallikorttia: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast) ja DeepSeek-R1 (Ollama-hosted). Jokaisessa kortissa on vaihtoehdot "Add" mallin lisäämiseksi tai "Try in Playground"](../../../../translated_images/fi/aitk-model-catalog.2acd38953bb9c119aa629fe74ef34cc56e4eed35e7f5acba7cd0a59e614ab335.png)

1. Avaa **AI Toolkit** -laajennus **Activity Bar** -valikosta.
1. Valitse **Catalog**-osiossa **Models**, jolloin **Model Catalog** avautuu uuteen editorivälilehteen.
1. Kirjoita **Model Catalog** -hakupalkkiin **OpenAI GPT-4o**.
1. Klikkaa **+ Add** lisätäksesi mallin **My Models** -osioon. Varmista, että olet valinnut mallin, joka on **Hosted by GitHub**.
1. Vahvista **Activity Bar** -valikossa, että **OpenAI GPT-4o**-malli näkyy listassa.

### -1- Luo agentti

**Agent (Prompt) Builder** mahdollistaa oman tekoälyagentin luomisen ja muokkaamisen. Tässä osiossa luot uuden agentin ja määrität mallin keskustelun voimanlähteeksi.

![Kuvakaappaus "Calculator Agent" -rakennusliittymästä Visual Studio Coden AI Toolkit -laajennuksessa. Vasemmassa paneelissa valittu malli on "OpenAI GPT-4o (via GitHub)." Järjestelmäkehotus kuuluu "You are a professor in university teaching math," ja käyttäjäkehotus sanoo "Explain to me the Fourier equation in simple terms." Lisäasetuksiin kuuluu painikkeet työkalujen lisäämiseksi, MCP-palvelimen aktivoimiseksi ja rakenteellisen tulostuksen valitsemiseksi. Alhaalla on sininen "Run"-painike. Oikeassa paneelissa "Get Started with Examples" -osiossa on kolme esimerkkiaagenttia: Web Developer (MCP Serverin kanssa), Second-Grade Simplifier ja Dream Interpreter, joista jokaisella on lyhyt kuvaus niiden toiminnoista.](../../../../translated_images/fi/aitk-agent-builder.901e3a2960c3e4774b29a23024ff5bec2d4232f57fae2a418b2aaae80f81c05f.png)

1. Avaa **AI Toolkit** -laajennus **Activity Bar** -valikosta.
1. Valitse **Tools**-osiossa **Agent (Prompt) Builder**, jolloin **Agent (Prompt) Builder** avautuu uuteen editorivälilehteen.
1. Klikkaa **+ New Agent** -painiketta. Laajennus käynnistää asennusvelhon **Command Palette** -valikon kautta.
1. Kirjoita nimeksi **Calculator Agent** ja paina **Enter**.
1. Valitse **Agent (Prompt) Builder** -osiossa **Model**-kenttään **OpenAI GPT-4o (via GitHub)** -malli.

### -2- Luo agentille järjestelmäkehotus

Kun agentti on alustettu, on aika määrittää sen persoonallisuus ja tarkoitus. Tässä osiossa käytät **Generate system prompt** -ominaisuutta kuvaamaan agentin aiottua käyttäytymistä—tässä tapauksessa laskinagentti—ja annat mallin kirjoittaa järjestelmäkehotuksen puolestasi.

![Kuvakaappaus "Calculator Agent" -liittymästä Visual Studio Coden AI Toolkit -laajennuksessa, jossa avoinna oleva modaalinen ikkuna on otsikoitu "Generate a prompt." Modaalinen ikkuna selittää, että kehotemalli voidaan luoda jakamalla perustiedot, ja sisältää tekstikentän, jossa on esimerkkijärjestelmäkehotus: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Tekstikentän alla on "Close" ja "Generate" -painikkeet. Taustalla näkyy osa agentin konfiguraatiosta, mukaan lukien valittu malli "OpenAI GPT-4o (via GitHub)" ja kentät järjestelmä- ja käyttäjäkehotuksille.](../../../../translated_images/fi/aitk-generate-prompt.ba9e69d3d2bbe2a26444d0c78775540b14196061eee32c2054e9ee68c4f51f3a.png)

1. **Prompts**-osiossa klikkaa **Generate system prompt** -painiketta. Tämä avaa kehotuksen luontityökalun, joka hyödyntää tekoälyä järjestelmäkehotuksen luomiseen agentille.
1. **Generate a prompt** -ikkunassa kirjoita seuraava: `Olet avulias ja tehokas matematiikka-avustaja. Kun sinulle annetaan tehtävä, joka sisältää peruslaskutoimituksia, vastaat oikealla tuloksella.`
1. Klikkaa **Generate**-painiketta. Ilmoitus ilmestyy oikeaan alakulmaan vahvistaen, että järjestelmäkehotusta luodaan. Kun kehotuksen luonti on valmis, kehotus ilmestyy **System prompt** -kenttään **Agent (Prompt) Builder** -osiossa.
1. Tarkista **System prompt** ja muokkaa tarvittaessa.

### -3- Luo MCP-palvelin

Nyt kun olet määrittänyt agentin järjestelmäkehotuksen—ohjaten sen käyttäytymistä ja vastauksia—on aika varustaa agentti käytännön kyvyillä. Tässä osiossa luot laskin-MCP-palvelimen, jossa on työkaluja yhteen-, vähennys-, kerto- ja jakolaskujen suorittamiseen. Tämä palvelin mahdollistaa agentin suorittaa reaaliaikaisia matemaattisia operaatioita luonnollisen kielen kehotusten perusteella.

!["Kuvakaappaus Calculator Agent -liittymän alaosasta Visual Studio Coden AI Toolkit -laajennuksessa. Näytetään laajennettavat valikot “Tools” ja “Structure output,” sekä pudotusvalikko “Choose output format,” joka on asetettu “text.” Oikealla on painike “+ MCP Server” Model Context Protocol -palvelimen lisäämiseksi. Kuvakepaikkamerkki näkyy Tools-osan yläpuolella.](../../../../translated_images/fi/aitk-add-mcp-server.9742cfddfe808353c0caf9cc0a7ed3e80e13abf4d2ebde315c81c3cb02a2a449.png)

AI Toolkit sisältää mallipohjia MCP-palvelimen luomisen helpottamiseksi. Käytämme Python-mallipohjaa laskin-MCP-palvelimen luomiseen.

*Huomio*: AI Toolkit tukee tällä hetkellä Pythonia ja TypeScriptiä.

1. **Tools**-osiossa **Agent (Prompt) Builder** -liittymässä klikkaa **+ MCP Server** -painiketta. Laajennus käynnistää asennusvelhon **Command Palette** -valikon kautta.
1. Valitse **+ Add Server**.
1. Valitse **Create a New MCP Server**.
1. Valitse mallipohjaksi **python-weather**.
1. Valitse **Default folder** tallentaaksesi MCP-palvelimen mallipohjan.
1. Kirjoita palvelimen nimeksi: **Calculator**
1. Uusi Visual Studio Code -ikkuna avautuu. Valitse **Yes, I trust the authors**.
1. Käytä terminaalia (**Terminal** > **New Terminal**) ja luo virtuaaliympäristö: `python -m venv .venv`
1. Aktivoi virtuaaliympäristö terminaalin kautta:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Asenna riippuvuudet terminaalin kautta: `pip install -e .[dev]`
1. **Activity Bar** -valikon **Explorer**-näkymässä laajenna **src**-hakemisto ja valitse **server.py** avataksesi tiedoston editorissa.
1. Korvaa **server.py**-tiedoston sisältö seuraavalla ja tallenna:

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

### -4- Suorita agentti laskin-MCP-palvelimen kanssa

Nyt kun agentillasi on työkaluja, on aika käyttää niitä! Tässä osiossa lähetät kehotuksia agentille testataksesi ja validoidaksesi, käyttääkö agentti laskin-MCP-palvelimen asianmukaista työkalua.

![Kuvakaappaus Calculator Agent -liittymästä Visual Studio Coden AI Toolkit -laajennuksessa. Vasemmassa paneelissa “Tools”-osiossa on lisätty MCP-palvelin nimeltä local-server-calculator_server, jossa on neljä käytettävissä olevaa työkalua: add, subtract, multiply ja divide. Merkintä näyttää, että neljä työkalua on aktiivisia. Alla on supistettu “Structure output” -osio ja sininen “Run”-painike. Oikeassa paneelissa “Model Response” -osiossa agentti käyttää multiply- ja subtract-työkaluja syötteillä {"a": 3, "b": 25} ja {"a": 75, "b": 20}. Lopullinen “Tool Response” näytetään arvona 75.0. Alhaalla näkyy “View Code” -painike.](../../../../translated_images/fi/aitk-agent-response-with-tools.e7c781869dc8041a25f9903ed4f7e8e0c7e13d7d94f6786a6c51b1e172f56866.png)

Suoritat laskin-MCP-palvelimen paikallisella kehityskoneellasi **Agent Builder** -liittymän kautta MCP-asiakkaana.

1. Paina `F5` käynnistääksesi MCP-palvelimen virheenkorjauksen. **Agent (Prompt) Builder** avautuu uuteen editorivälilehteen. Palvelimen tila näkyy terminaalissa.
1. **Agent (Prompt) Builder** -liittymän **User prompt** -kenttään kirjoita seuraava kehotus: `Ostin 3 tuotetta, joiden hinta oli $25 kappaleelta, ja käytin $20 alennuksen. Kuinka paljon maksoin?`
1. Klikkaa **Run**-painiketta luodaksesi agentin vastauksen.
1. Tarkista agentin tuotos. Mallin pitäisi päätellä, että maksoit **$55**.
1. Tässä on yhteenveto siitä, mitä pitäisi tapahtua:
    - Agentti valitsee **multiply**- ja **subtract**-työkalut laskennan avuksi.
    - Vastaavat `a`- ja `b`-arvot määritetään **multiply**-työkalulle.
    - Vastaavat `a`- ja `b`-arvot määritetään **subtract**-työkalulle.
    - Jokaisen työkalun vastaus annetaan vastaavassa **Tool Response** -osiossa.
    - Lopullinen tuotos mallilta annetaan lopullisessa **Model Response** -osiossa.
1. Lähetä lisää kehotuksia testataksesi agenttia edelleen. Voit muokata olemassa olevaa kehotusta **User prompt** -kentässä klikkaamalla kenttää ja korvaamalla nykyisen kehotuksen.
1. Kun olet valmis testaamaan agenttia, voit pysäyttää palvelimen terminaalin kautta painamalla **CTRL/CMD+C** lopettaaksesi.

## Tehtävä

Kokeile lisätä uusi työkalu **server.py**-tiedostoon (esim. palauttaa luvun neliöjuuri). Lähetä lisäkehotuksia, jotka vaativat agenttia käyttämään uutta työkalua (tai olemassa olevia työkaluja). Muista käynnistää palvelin uudelleen ladataksesi uudet työkalut.

## Ratkaisu

[Ratkaisu](./solution/README.md)

## Keskeiset opit

Tämän osion keskeiset opit ovat seuraavat:

- AI Toolkit -laajennus on erinomainen asiakas, joka mahdollistaa MCP-palvelimien ja niiden työkalujen käytön.
- Voit lisätä uusia työkaluja MCP-palvelimiin, laajentaen agentin kyvykkyyksiä vastaamaan kehittyviä tarpeita.
- AI Toolkit sisältää mallipohjia (esim. Python MCP-palvelinmallipohjat), jotka yksinkertaistavat mukautettujen työkalujen luomista.

## Lisäresurssit

- [AI Toolkit -dokumentaatio](https://aka.ms/AIToolkit/doc)

## Mitä seuraavaksi
- Seuraava: [Testaus ja virheenkorjaus](../08-testing/README.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.