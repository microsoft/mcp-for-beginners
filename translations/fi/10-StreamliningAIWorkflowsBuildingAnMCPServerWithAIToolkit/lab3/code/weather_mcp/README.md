# Weather MCP Server

Tämä on esimerkkimallinen MCP-palvelin Pythonilla, joka toteuttaa säätyökaluja mock-vastauksilla. Sitä voi käyttää pohjana omalle MCP-palvelimellesi. Se sisältää seuraavat ominaisuudet:

- **Weather Tool**: Työkalu, joka tarjoaa simuloitua sääinformaatiota annetun sijainnin perusteella.
- **Yhdistä Agent Builderiin**: Ominaisuus, jonka avulla voit yhdistää MCP-palvelimen Agent Builderiin testauksen ja virheenkorjauksen ajaksi.
- **Virheenkorjaus [MCP Inspectorilla](https://github.com/modelcontextprotocol/inspector)**: Ominaisuus, jonka avulla voit virheenkorjata MCP-palvelinta MCP Inspectorin avulla.

## Aloita Weather MCP Server -mallipohjalla

> **Esivaatimukset**
>
> Jotta voit ajaa MCP-palvelinta paikallisella kehityskoneellasi, tarvitset:
>
> - [Python](https://www.python.org/)
> - (*Valinnainen - jos haluat käyttää uv:tä*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Ympäristön valmistelu

Tämän projektin ympäristön voi ottaa käyttöön kahdella eri tavalla. Voit valita mieleisesi tavan.

> Huomautus: Lataa VSCode tai terminaali uudelleen varmistaaksesi, että virtuaaliympäristön python on käytössä virtuaaliympäristön luomisen jälkeen.

| Tapa | Vaiheet |
| -------- | ----- |
| Käyttäen `uv` | 1. Luo virtuaaliympäristö: `uv venv` <br>2. Suorita VSCode-komento "***Python: Select Interpreter***" ja valitse luodun virtuaaliympäristön python <br>3. Asenna riippuvuudet (sisältäen kehitysriippuvuudet): `uv pip install -r pyproject.toml --extra dev` |
| Käyttäen `pip` | 1. Luo virtuaaliympäristö: `python -m venv .venv` <br>2. Suorita VSCode-komento "***Python: Select Interpreter***" ja valitse luodun virtuaaliympäristön python<br>3. Asenna riippuvuudet (sisältäen kehitysriippuvuudet): `pip install -e .[dev]` |

Ympäristön valmistelun jälkeen voit ajaa palvelimen paikallisella kehityskoneellasi Agent Builderin kautta MCP Clientina aloittaaksesi:
1. Avaa VS Code Debug-paneeli. Valitse `Debug in Agent Builder` tai paina `F5` aloittaaksesi MCP-palvelimen virheenkorjauksen.
2. Käytä AI Toolkit Agent Builderia testataksesi palvelinta [tällä kehotteella](../../../../../../../../../../open_prompt_builder). Palvelin yhdistyy automaattisesti Agent Builderiin.
3. Klikkaa `Run` testataksesi palvelinta kehotteella.

**Onnittelut**! Olet onnistuneesti ajanut Weather MCP Serverin paikallisella kehityskoneellasi Agent Builderin kautta MCP Clientina.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Mitä mallipohja sisältää

| Kansio / Tiedosto | Sisältö                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode-tiedostot virheenkorjausta varten    |
| `.aitk`      | Konfiguraatiot AI Toolkitille                |
| `src`        | Lähdekoodi weather mcp -palvelimelle         |

## Kuinka virheenkorjata Weather MCP Server

> Huomautuksia:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) on visuaalinen kehitystyökalu MCP-palvelinten testaamiseen ja virheenkorjaukseen.
> - Kaikki virheenkorjaustilat tukevat breakpointteja, joten voit lisätä breakpointteja työkalun toteutuskoodiin.

| Virheenkorjaustila | Kuvaus | Virheenkorjausvaiheet |
| ---------- | ----------- | --------------- |
| Agent Builder | Virheenkorjaa MCP-palvelinta Agent Builderissa AI Toolkitin kautta. | 1. Avaa VS Code Debug-paneeli. Valitse `Debug in Agent Builder` ja paina `F5` aloittaaksesi MCP-palvelimen virheenkorjauksen.<br>2. Käytä AI Toolkit Agent Builderia testataksesi palvelinta [tällä kehotteella](../../../../../../../../../../open_prompt_builder). Palvelin yhdistyy automaattisesti Agent Builderiin.<br>3. Klikkaa `Run` testataksesi palvelinta kehotteella. |
| MCP Inspector | Virheenkorjaa MCP-palvelinta MCP Inspectorin avulla. | 1. Asenna [Node.js](https://nodejs.org/)<br> 2. Valmistele Inspector: `cd inspector` && `npm install` <br> 3. Avaa VS Code Debug-paneeli. Valitse `Debug SSE in Inspector (Edge)` tai `Debug SSE in Inspector (Chrome)`. Paina F5 aloittaaksesi virheenkorjauksen.<br> 4. Kun MCP Inspector käynnistyy selaimessa, klikkaa `Connect` yhdistääksesi tämän MCP-palvelimen.<br> 5. Tämän jälkeen voit `List Tools`, valita työkalun, syöttää parametrit ja `Run Tool` virheenkorjataksesi palvelimesi koodia.<br> |

## Oletusportit ja mukautukset

| Virheenkorjaustila | Portit | Määritelmät | Mukautukset | Huomautus |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Muokkaa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) muuttaaksesi yllä olevia portteja. | Ei sovellettavissa |
| MCP Inspector | 3001 (Palvelin); 5173 ja 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Muokkaa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) muuttaaksesi yllä olevia portteja.| Ei sovellettavissa |

## Palaute

Jos sinulla on palautetta tai ehdotuksia tähän mallipohjaan liittyen, avaa issue [AI Toolkitin GitHub-repositoriossa](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.