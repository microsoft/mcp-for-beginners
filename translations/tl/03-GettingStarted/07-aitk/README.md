# Paggamit ng server mula sa AI Toolkit extension para sa Visual Studio Code

Kapag gumagawa ka ng isang AI agent, hindi lang ito tungkol sa pagbuo ng matatalinong tugon; tungkol din ito sa pagbibigay ng kakayahan sa iyong agent na kumilos. Dito pumapasok ang Model Context Protocol (MCP). Pinapadali ng MCP para sa mga agent na ma-access ang mga panlabas na tool at serbisyo sa isang pare-parehong paraan. Isiping parang tinutuklaw mo ang iyong agent sa isang toolbox na *talagang* magagamit nito.

Halimbawa, ikinakabit mo ang isang agent sa iyong calculator MCP server. Bigla, kayang magsagawa ng mga operasyon sa matematika ng iyong agent sa pamamagitan lang ng pagtanggap ng prompt tulad ng “Ano ang 47 times 89?”—hindi na kailangang i-hardcode ang logic o gumawa ng custom na mga API.

## Pangkalahatang-ideya

Tinutukoy ng araling ito kung paano ikonekta ang isang calculator MCP server sa isang agent gamit ang [AI Toolkit](https://aka.ms/AIToolkit) extension sa Visual Studio Code, na nagpapahintulot sa iyong agent na magsagawa ng mga operasyon sa matematika gaya ng addition, subtraction, multiplication, at division gamit ang natural na wika.

Ang AI Toolkit ay isang makapangyarihang extension para sa Visual Studio Code na nagpapasimple ng pagbuo ng agent. Madaling makabuo ang mga AI Engineer ng mga AI na aplikasyon sa pamamagitan ng pag-develop at pagsubok ng mga generative AI model—lokal man o sa cloud. Sinusuportahan ng extension ang karamihan sa mga pangunahing generative model na available ngayon.

*Tandaan*: Sinusuportahan ng AI Toolkit sa kasalukuyan ang Python at TypeScript.

## Mga Layuning Pangkatuto

Sa pagtatapos ng araling ito, magagawa mo na:

- Gumamit ng MCP server sa pamamagitan ng AI Toolkit.
- I-configure ang isang agent configuration upang paganahin itong matuklasan at magamit ang mga tool na ibinibigay ng MCP server.
- Gamitin ang mga MCP tool gamit ang natural na wika.

## Pamamaraan

Ganito natin kailangang lapitan ito sa mataas na antas:

- Gumawa ng isang agent at tukuyin ang system prompt nito.
- Gumawa ng MCP server na may calculator tools.
- Ikonekta ang Agent Builder sa MCP server.
- Subukan ang pag-invoke ng tool ng agent gamit ang natural na wika.

Mahusay, ngayon na nauunawaan natin ang daloy, i-configure natin ang isang AI agent upang magamit ang mga panlabas na tool sa pamamagitan ng MCP, pinapalakas ang mga kakayahan nito!

## Mga Kinakailangan

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit para sa Visual Studio Code](https://aka.ms/AIToolkit)

## Ehersisyo: Paggamit ng server

> [!WARNING]
> Paalala para sa mga gumagamit ng macOS. Kasalukuyan naming iniimbestigahan ang isang isyu na nakaapekto sa pag-install ng dependency sa macOS. Dahil dito, hindi muna makukumpleto ng mga gumagamit ng macOS ang tutorial na ito sa ngayon. Ia-update namin ang mga tagubilin kapag may maibigay na solusyon. Salamat sa inyong pasensya at pag-unawa!

Sa ehersisyong ito, bubuuin, patatakbuhin, at pagyayamanin mo ang isang AI agent gamit ang mga tool mula sa isang MCP server sa loob ng Visual Studio Code gamit ang AI Toolkit.

### -0- Paunang hakbang, idagdag ang OpenAI GPT-4o model sa My Models

Ginagamit sa ehersisyong ito ang **GPT-4o** model. Dapat itong idagdag sa **My Models** bago gumawa ng agent.

![Screenshot ng model selection interface sa AI Toolkit extension ng Visual Studio Code. Nakalagay sa heading ang "Find the right model for your AI Solution" na may subtitle na naghihikayat sa mga user na tuklasin, subukan, at i-deploy ang AI models. Sa ibaba, sa ilalim ng “Popular Models,” may anim na card ng modelo na ipinapakita: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), at DeepSeek-R1 (Ollama-hosted). Bawat card ay may opsyon na “Add” o “Try in Playground.”](../../../../translated_images/tl/aitk-model-catalog.2acd38953bb9c119.webp)

1. Buksan ang **AI Toolkit** extension mula sa **Activity Bar**.
1. Sa seksyon na **Catalog**, piliin ang **Models** upang buksan ang **Model Catalog**. Ang pagpili ng **Models** ay magbubukas ng **Model Catalog** sa bagong editor tab.
1. Sa search bar ng **Model Catalog**, i-type ang **OpenAI GPT-4o**.
1. I-click ang **+ Add** upang idagdag ang modelo sa iyong listahan ng **My Models**. Siguraduhing napili mo ang modelong **Hosted by GitHub**.
1. Sa **Activity Bar**, tiyaking lumalabas ang **OpenAI GPT-4o** na modelo sa listahan.

### -1- Gumawa ng agent

Pinapayagan ka ng **Agent (Prompt) Builder** na gumawa at i-customize ang sarili mong AI-powered na mga agent. Sa seksyong ito, gagawa ka ng bagong agent at magtatakda ng model upang magpatakbo ng pag-uusap.

![Screenshot ng "Calculator Agent" builder interface sa AI Toolkit extension para sa Visual Studio Code. Sa kaliwang panel, ang napiling modelo ay "OpenAI GPT-4o (via GitHub)." Ang system prompt ay "You are a professor in university teaching math," at ang user prompt ay "Explain to me the Fourier equation in simple terms." May mga karagdagang opsyon tulad ng mga button para sa pagdagdag ng mga tool, pag-enable ng MCP Server, at pagpili ng structured output. May asul na “Run” button sa ibaba. Sa kanang panel, sa ilalim ng "Get Started with Examples," may tatlong sample agents na nakalista: Web Developer (may MCP Server, Second-Grade Simplifier, at Dream Interpreter, bawat isa ay may maikling paglalarawan ng kanilang mga function).](../../../../translated_images/tl/aitk-agent-builder.901e3a2960c3e477.webp)

1. Buksan ang **AI Toolkit** extension mula sa **Activity Bar**.
1. Sa seksyon na **Tools**, piliin ang **Agent (Prompt) Builder**. Ang pagpili ng **Agent (Prompt) Builder** ay magbubukas ng **Agent (Prompt) Builder** sa bagong editor tab.
1. I-click ang button na **+ New Agent**. Magbubukas ang extension ng setup wizard sa pamamagitan ng **Command Palette**.
1. I-type ang pangalang **Calculator Agent** at pindutin ang **Enter**.
1. Sa **Agent (Prompt) Builder**, para sa field na **Model**, piliin ang **OpenAI GPT-4o (via GitHub)** na modelo.

### -2- Gumawa ng system prompt para sa agent

Ngayong na-set mo na ang agent, panahon na upang tukuyin ang personalidad at layunin nito. Sa seksyong ito, gagamitin mo ang **Generate system prompt** na tampok upang ilarawan ang inaasahang ugali ng agent—sa pagkakataong ito, isang calculator agent—at hayaang isulat ng modelo ang system prompt para sa iyo.

![Screenshot ng "Calculator Agent" interface sa AI Toolkit para sa Visual Studio Code na may bukas na modal window na pinamagatang "Generate a prompt." Ipinaliwanag sa modal na maaaring makabuo ng prompt template sa pamamagitan ng pagbibigay ng mga pangunahing detalye at may kasamang text box na may halimbawang system prompt: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Sa ilalim ng text box ay may mga button na "Close" at "Generate." Sa background, makikita ang bahagi ng agent configuration, kabilang ang napiling modelo na "OpenAI GPT-4o (via GitHub)" at mga field para sa system at user prompts.](../../../../translated_images/tl/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Sa seksyong **Prompts**, i-click ang button na **Generate system prompt**. Bubukas ang prompt builder na gumagamit ng AI upang gumawa ng system prompt para sa agent.
1. Sa window na **Generate a prompt**, ilagay ang sumusunod: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. I-click ang button na **Generate**. Magpapakita ng notification sa ibabang-kanang bahagi bilang kumpirmasyon na ginagawa ang system prompt. Kapag natapos, lalabas ang prompt sa field na **System prompt** ng **Agent (Prompt) Builder**.
1. Suriin ang **System prompt** at baguhin kung kinakailangan.

### -3- Gumawa ng MCP server

Ngayong naitakda mo na ang system prompt ng iyong agent—na gumagabay sa kanyang ugali at mga tugon—panahon na upang bigyan ang agent ng praktikal na kakayahan. Sa seksyong ito, gagawa ka ng calculator MCP server na may mga tool para sa addition, subtraction, multiplication, at division na kalkulasyon. Papayagan nito ang iyong agent na magsagawa ng mga operasyon sa matematika sa real-time bilang tugon sa mga natural na wika na prompt.

!["Screenshot ng ibabang bahagi ng Calculator Agent interface sa AI Toolkit extension para sa Visual Studio Code. Mayroong mga expandable menu para sa “Tools” at “Structure output,” pati na rin ang dropdown menu na may label na “Choose output format” na naka-set sa “text.” Sa kanan, may button na may label na “+ MCP Server” para magdagdag ng Model Context Protocol server. May placeholder na image icon sa itaas ng seksiyong Tools.](../../../../translated_images/tl/aitk-add-mcp-server.9742cfddfe808353.webp)

Ang AI Toolkit ay may mga template upang mas madaling makagawa ka ng sarili mong MCP server. Gagamitin natin ang Python template para gumawa ng calculator MCP server.

*Tandaan*: Sinusuportahan ng AI Toolkit sa kasalukuyan ang Python at TypeScript.

1. Sa seksyon na **Tools** ng **Agent (Prompt) Builder**, i-click ang button na **+ MCP Server**. Magbubukas ang setup wizard sa pamamagitan ng **Command Palette**.
1. Piliin ang **+ Add Server**.
1. Piliin ang **Create a New MCP Server**.
1. Piliin ang **python-weather** bilang template.
1. Piliin ang **Default folder** para i-save ang MCP server template.
1. Ilagay ang sumusunod na pangalan para sa server: **Calculator**
1. Magbubukas ang bagong Visual Studio Code window. Piliin ang **Yes, I trust the authors**.
1. Gamit ang terminal (**Terminal** > **New Terminal**), gumawa ng virtual environment: `python -m venv .venv`
1. Gamit ang terminal, i-activate ang virtual environment:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Gamit ang terminal, i-install ang mga dependencies: `pip install -e .[dev]`
1. Sa **Explorer** view ng **Activity Bar**, i-expand ang direktoryong **src** at piliin ang **server.py** upang buksan ang file sa editor.
1. Palitan ang code sa **server.py** file ng sumusunod at i-save:

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

### -4- Patakbuhin ang agent gamit ang calculator MCP server

Ngayong may mga tool na ang iyong agent, panahon na upang gamitin ang mga ito! Sa seksyong ito, magsusumite ka ng mga prompt sa agent upang subukan at tiyakin kung ginagamit ng agent ang tamang tool mula sa calculator MCP server.

![Screenshot ng Calculator Agent interface sa AI Toolkit extension para sa Visual Studio Code. Sa kaliwang panel, sa ilalim ng “Tools,” mayroong MCP server na pinangalanang local-server-calculator_server, na may apat na tool: add, subtract, multiply, at divide. May badge na nagpapakita na apat na tool ang aktif. Sa ibaba ay isang nakatagong “Structure output” section at isang asul na “Run” button. Sa kanang panel, sa ilalim ng “Model Response,” ini-invoke ng agent ang multiply at subtract tools na may inputs na {"a": 3, "b": 25} at {"a": 75, "b": 20} ayon Sa pagkakabanggit. Ang panghuling “Tool Response” ay ipinapakita bilang 75.0. May “View Code” button sa ibaba.](../../../../translated_images/tl/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Patakbuhin mo ang calculator MCP server sa iyong lokal na makina gamit ang **Agent Builder** bilang MCP client.

1. Pindutin ang `F5` upang simulan ang pag-debug ng MCP server. Magbubukas ang **Agent (Prompt) Builder** sa bagong editor tab. Ang status ng server ay makikita sa terminal.
1. Sa field na **User prompt** ng **Agent (Prompt) Builder**, ilagay ang sumusunod na prompt: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. I-click ang **Run** button upang makabuo ng tugon ng agent.
1. Suriin ang output ng agent. Dapat tapusin ng modelo na ikaw ay nagbayad ng **$55**.
1. Narito ang paliwanag kung ano ang mangyayari:
    - Pinili ng agent ang mga tool na **multiply** at **subtract** upang tumulong sa kalkulasyon.
    - Inilaan ang mga halaga ng `a` at `b` para sa tool na **multiply**.
    - Inilaan ang mga halaga ng `a` at `b` para sa tool na **subtract**.
    - Ang tugon mula sa bawat tool ay ibinibigay sa kani-kanilang **Tool Response**.
    - Ang panghuling output mula sa modelo ay ibinibigay sa panghuling **Model Response**.
1. Mag-submit ng mga dagdag na prompt upang karagdagang subukan ang agent. Maaari mong baguhin ang kasalukuyang prompt sa field na **User prompt** sa pamamagitan ng pag-click dito at pagpapalit ng kasalukuyang prompt.
1. Kapag tapos ka na sa pagsubok sa agent, maaaring itigil ang server via terminal sa pamamagitan ng pagpindot ng **CTRL/CMD+C** upang lumabas.

## Takdang-Aralin

Subukang magdagdag ng isa pang tool entry sa iyong **server.py** file (halimbawa: magbalik ng square root ng isang numero). Mag-submit ng mga dagdag na prompt na maaaring mangailangan ng agent na gamitin ang iyong bagong tool (o mga umiiral na tool). Huwag kalimutang i-restart ang server upang ma-load ang mga bagong idinagdag na tool.

## Solusyon

[Solusyon](./solution/README.md)

## Mga Pangunahing Punto

Ang mga mahahalagang matutunan mula sa kabanatang ito ay ang mga sumusunod:

- Ang AI Toolkit extension ay isang mahusay na client na nagpapahintulot sa iyo na gamitin ang MCP Servers at kanilang mga tool.
- Maaari kang magdagdag ng mga bagong tool sa MCP servers, pinalalawak ang kakayahan ng agent upang matugunan ang nagbabagong pangangailangan.
- Kasama sa AI Toolkit ang mga template (hal., mga Python MCP server template) upang pasimplehin ang paggawa ng mga custom na tool.

## Karagdagang Mga Sanggunian

- [AI Toolkit docs](https://aka.ms/AIToolkit/doc)

## Ano ang Susunod
- Susunod: [Testing & Debugging](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->