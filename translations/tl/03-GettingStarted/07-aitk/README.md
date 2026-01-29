# Paggamit ng server mula sa AI Toolkit extension para sa Visual Studio Code

Kapag gumagawa ka ng AI agent, hindi lang ito tungkol sa pagbibigay ng matatalinong sagot; mahalaga rin na mabigyan mo ang iyong agent ng kakayahang kumilos. Dito pumapasok ang Model Context Protocol (MCP). Ginagawang madali ng MCP para sa mga agent na ma-access ang mga panlabas na tool at serbisyo sa isang pare-parehong paraan. Isipin mo ito na parang binibigyan mo ang iyong agent ng toolbox na kaya nitong *gamitin*.

Halimbawa, ikinonekta mo ang isang agent sa iyong calculator MCP server. Bigla na lang, kaya na ng iyong agent na magsagawa ng mga operasyon sa matematika sa pamamagitan lamang ng pagtanggap ng prompt tulad ng “Ano ang 47 times 89?”—hindi na kailangang mag-hardcode ng logic o gumawa ng custom APIs.

## Pangkalahatang-ideya

Tatalakayin sa araling ito kung paano ikonekta ang isang calculator MCP server sa isang agent gamit ang [AI Toolkit](https://aka.ms/AIToolkit) extension sa Visual Studio Code, upang bigyang-kakayahan ang iyong agent na magsagawa ng mga operasyon sa matematika tulad ng pagdaragdag, pagbabawas, pagpaparami, at paghahati sa pamamagitan ng natural na wika.

Ang AI Toolkit ay isang makapangyarihang extension para sa Visual Studio Code na nagpapadali sa pagbuo ng mga agent. Madaling makakagawa ang mga AI Engineer ng mga AI application sa pamamagitan ng pagbuo at pagsubok ng mga generative AI model—lokal man o sa cloud. Sinusuportahan ng extension ang karamihan sa mga pangunahing generative model na magagamit ngayon.

*Paalala*: Sinusuportahan ng AI Toolkit ang Python at TypeScript sa kasalukuyan.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mo ang sumusunod:

- Gumamit ng MCP server gamit ang AI Toolkit.
- I-configure ang isang agent upang mahanap at magamit ang mga tool na ibinibigay ng MCP server.
- Gumamit ng mga MCP tool sa pamamagitan ng natural na wika.

## Paraan

Narito ang pangkalahatang hakbang na dapat sundin:

- Gumawa ng isang agent at tukuyin ang system prompt nito.
- Gumawa ng isang MCP server na may mga calculator tool.
- Ikonekta ang Agent Builder sa MCP server.
- Subukan ang paggamit ng tool ng agent sa pamamagitan ng natural na wika.

Magaling! Ngayon na nauunawaan na natin ang daloy, i-configure natin ang isang AI agent upang magamit ang mga panlabas na tool sa pamamagitan ng MCP, na magpapahusay sa kakayahan nito!

## Mga Kinakailangan

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit para sa Visual Studio Code](https://aka.ms/AIToolkit)

## Ehersisyo: Paggamit ng server

> [!WARNING]
> Paalala para sa mga gumagamit ng macOS. Sinisiyasat pa namin ang isang isyu na nakakaapekto sa pag-install ng dependency sa macOS. Dahil dito, hindi magagawang kumpletuhin ng mga gumagamit ng macOS ang tutorial na ito sa kasalukuyan. Ia-update namin ang mga tagubilin sa lalong madaling panahon kapag may solusyon na. Salamat sa inyong pasensya at pang-unawa!

Sa ehersisyong ito, gagawa, magpapatakbo, at magpapahusay ka ng isang AI agent gamit ang mga tool mula sa isang MCP server sa loob ng Visual Studio Code gamit ang AI Toolkit.

### -0- Paunang Hakbang: Idagdag ang OpenAI GPT-4o model sa My Models

Gagamitin sa ehersisyo ang **GPT-4o** model. Dapat itong idagdag sa **My Models** bago gumawa ng agent.

1. Buksan ang **AI Toolkit** extension mula sa **Activity Bar**.
1. Sa seksyong **Catalog**, piliin ang **Models** upang buksan ang **Model Catalog**. Ang pagpili sa **Models** ay magbubukas ng **Model Catalog** sa isang bagong editor tab.
1. Sa search bar ng **Model Catalog**, ilagay ang **OpenAI GPT-4o**.
1. I-click ang **+ Add** upang idagdag ang model sa iyong listahan ng **My Models**. Siguraduhing napili mo ang model na **Hosted by GitHub**.
1. Sa **Activity Bar**, tiyaking lumalabas ang **OpenAI GPT-4o** model sa listahan.

### -1- Gumawa ng agent

Ang **Agent (Prompt) Builder** ay nagbibigay-daan sa iyo na gumawa at i-customize ang sarili mong AI-powered agents. Sa seksyong ito, gagawa ka ng bagong agent at mag-a-assign ng model upang paganahin ang pag-uusap.

1. Buksan ang **AI Toolkit** extension mula sa **Activity Bar**.
1. Sa seksyong **Tools**, piliin ang **Agent (Prompt) Builder**. Ang pagpili sa **Agent (Prompt) Builder** ay magbubukas ng **Agent (Prompt) Builder** sa isang bagong editor tab.
1. I-click ang **+ New Agent** button. Maglulunsad ang extension ng setup wizard sa pamamagitan ng **Command Palette**.
1. Ilagay ang pangalan na **Calculator Agent** at pindutin ang **Enter**.
1. Sa **Agent (Prompt) Builder**, para sa field na **Model**, piliin ang **OpenAI GPT-4o (via GitHub)** model.

### -2- Gumawa ng system prompt para sa agent

Kapag na-set up na ang agent, oras na upang tukuyin ang personalidad at layunin nito. Sa seksyong ito, gagamitin mo ang **Generate system prompt** na tampok upang ilarawan ang layunin ng agent—sa kasong ito, isang calculator agent—at hahayaan ang model na magsulat ng system prompt para sa iyo.

1. Para sa seksyong **Prompts**, i-click ang **Generate system prompt** button. Bubuksan nito ang prompt builder na gumagamit ng AI upang makabuo ng system prompt para sa agent.
1. Sa **Generate a prompt** window, ilagay ang sumusunod: `Ikaw ay isang matulungin at mahusay na math assistant. Kapag binigyan ng problema na may kinalaman sa basic arithmetic, sumasagot ka gamit ang tamang resulta.`
1. I-click ang **Generate** button. Lalabas ang isang notification sa ibabang kanang bahagi na nagpapatunay na ang system prompt ay ginagawa. Kapag natapos na ang prompt generation, lalabas ito sa **System prompt** field ng **Agent (Prompt) Builder**.
1. Suriin ang **System prompt** at baguhin kung kinakailangan.

### -3- Gumawa ng MCP server

Ngayon na natukoy mo na ang system prompt ng iyong agent—na gumagabay sa pag-uugali at mga sagot nito—oras na upang bigyan ang agent ng mga praktikal na kakayahan. Sa seksyong ito, gagawa ka ng isang calculator MCP server na may mga tool para magsagawa ng mga kalkulasyon tulad ng pagdaragdag, pagbabawas, pagpaparami, at paghahati. Ang server na ito ang magpapahintulot sa iyong agent na magsagawa ng real-time na mga operasyon sa matematika bilang tugon sa mga natural na prompt.

Ang AI Toolkit ay may mga template para sa madaling paggawa ng sarili mong MCP server. Gagamitin natin ang Python template para sa paggawa ng calculator MCP server.

*Paalala*: Sinusuportahan ng AI Toolkit ang Python at TypeScript sa kasalukuyan.

1. Sa seksyong **Tools** ng **Agent (Prompt) Builder**, i-click ang **+ MCP Server** button. Maglulunsad ang extension ng setup wizard sa pamamagitan ng **Command Palette**.
1. Piliin ang **+ Add Server**.
1. Piliin ang **Create a New MCP Server**.
1. Piliin ang **python-weather** bilang template.
1. Piliin ang **Default folder** upang i-save ang MCP server template.
1. Ilagay ang sumusunod na pangalan para sa server: **Calculator**
1. Magbubukas ang isang bagong Visual Studio Code window. Piliin ang **Yes, I trust the authors**.
1. Gamit ang terminal (**Terminal** > **New Terminal**), gumawa ng virtual environment: `python -m venv .venv`
1. Gamit ang terminal, i-activate ang virtual environment:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Gamit ang terminal, i-install ang mga dependency: `pip install -e .[dev]`
1. Sa **Explorer** view ng **Activity Bar**, i-expand ang **src** directory at piliin ang **server.py** upang buksan ang file sa editor.
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

Ngayon na may mga tool na ang iyong agent, oras na upang gamitin ang mga ito! Sa seksyong ito, magpapadala ka ng mga prompt sa agent upang subukan at kumpirmahin kung ginagamit ng agent ang tamang tool mula sa calculator MCP server.

1. Pindutin ang `F5` upang simulan ang pag-debug ng MCP server. Magbubukas ang **Agent (Prompt) Builder** sa isang bagong editor tab. Ang status ng server ay makikita sa terminal.
1. Sa **User prompt** field ng **Agent (Prompt) Builder**, ilagay ang sumusunod na prompt: `Bumili ako ng 3 item na may presyo na $25 bawat isa, at pagkatapos ay gumamit ng $20 na diskwento. Magkano ang binayaran ko?`
1. I-click ang **Run** button upang makabuo ng sagot mula sa agent.
1. Suriin ang output ng agent. Dapat nitong tapusin na nagbayad ka ng **$55**.
1. Narito ang breakdown ng dapat mangyari:
    - Pinipili ng agent ang **multiply** at **subtract** tools upang makatulong sa kalkulasyon.
    - Ang mga kaukulang halaga ng `a` at `b` ay itinalaga para sa **multiply** tool.
    - Ang mga kaukulang halaga ng `a` at `b` ay itinalaga para sa **subtract** tool.
    - Ang sagot mula sa bawat tool ay ibinibigay sa kaukulang **Tool Response**.
    - Ang panghuling output mula sa model ay ibinibigay sa panghuling **Model Response**.
1. Magpadala ng karagdagang mga prompt upang higit pang subukan ang agent. Maaari mong baguhin ang kasalukuyang prompt sa **User prompt** field sa pamamagitan ng pag-click sa field at pagpapalit ng kasalukuyang prompt.
1. Kapag tapos ka nang subukan ang agent, maaari mong ihinto ang server sa pamamagitan ng **terminal** sa pamamagitan ng pagpasok ng **CTRL/CMD+C** upang tumigil.

## Takdang-Aralin

Subukang magdagdag ng karagdagang tool entry sa iyong **server.py** file (halimbawa: ibalik ang square root ng isang numero). Magpadala ng karagdagang mga prompt na mangangailangan ng agent na gamitin ang bago mong tool (o mga umiiral na tool). Siguraduhing i-restart ang server upang mai-load ang mga bagong idinagdag na tool.

## Solusyon

[Solusyon](./solution/README.md)

## Mahahalagang Punto

Ang mga mahahalagang punto mula sa kabanatang ito ay ang mga sumusunod:

- Ang AI Toolkit extension ay isang mahusay na client na nagbibigay-daan sa iyong gamitin ang MCP Servers at ang kanilang mga tool.
- Maaari kang magdagdag ng mga bagong tool sa MCP servers, na nagpapalawak sa kakayahan ng agent upang matugunan ang mga nagbabagong pangangailangan.
- Ang AI Toolkit ay may mga template (halimbawa: Python MCP server templates) upang gawing mas madali ang paggawa ng mga custom na tool.

## Karagdagang Mga Mapagkukunan

- [AI Toolkit docs](https://aka.ms/AIToolkit/doc)

## Ano ang Susunod
- Susunod: [Pagsubok at Pag-debug](../08-testing/README.md)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.