# Sää MCP -palvelin

Tämä on esimerkkimäinen MCP-palvelin Pythonilla, joka toteuttaa säätyökaluja mallivastauksineen. Sitä voi käyttää perustana omalle MCP-palvelimellesi. Se sisältää seuraavat ominaisuudet:

- **Säätyökalu**: Työkalu, joka tarjoaa mallinnettua sääinformaatiota annettuun sijaintiin perustuen.
- **Yhdistä Agent Builderiin**: Ominaisuus, joka mahdollistaa MCP-palvelimen yhdistämisen Agent Builderiin testausta ja virheenkorjausta varten.
- **Virheenkorjaus [MCP Inspectorilla](https://github.com/modelcontextprotocol/inspector)**: Ominaisuus, joka mahdollistaa MCP-palvelimen virheenkorjauksen MCP Inspectorin avulla.

## Aloita Weather MCP Server -mallilla

> **Esivaatimukset**
>
> Jotta voit suorittaa MCP-palvelimen omalla kehityskoneellasi, tarvitset:
>
> - [Python](https://www.python.org/)
> - (*Valinnainen - jos haluat käyttää uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Valmistele ympäristö

Tämän projektin ympäristön voi valmistella kahdella tavalla. Voit valita mieltymyksesi mukaan jommankumman.

> Huomautus: Lataa VSCode tai terminaali uudelleen varmistuaksesi, että luotu virtuaaliympäristö python on käytössä.

| Menetelmä | Vaiheet |
| -------- | ----- |
| Käyttämällä `uv` | 1. Luo virtuaaliympäristö: `uv venv` <br>2. Suorita VSCode-komento "***Python: Valitse tulkki***" ja valitse virtuaaliympäristön python <br>3. Asenna riippuvuudet (sisältäen kehitysriippuvuudet): `uv pip install -r pyproject.toml --extra dev` |
| Käyttämällä `pip` | 1. Luo virtuaaliympäristö: `python -m venv .venv` <br>2. Suorita VSCode-komento "***Python: Valitse tulkki***" ja valitse virtuaaliympäristön python<br>3. Asenna riippuvuudet (sisältäen kehitysriippuvuudet): `pip install -e .[dev]` | 

Ympäristön valmistelun jälkeen voit ajaa palvelimen omalla kehityskoneellasi Agent Builderin kautta MCP Client -asiakkaana aloittaaksesi:
1. Avaa VS Code Debug-paneeli. Valitse `Debug in Agent Builder` tai paina `F5` aloittaaksesi MCP-palvelimen virheenkorjauksen.
2. Microsoft Foundry Toolkit Agent Builderissa valitse aktiivinen Foundry-järjestelmä, kuten `gpt-5.1`, ja kirjoita: `What is the weather in Shanghai?` Palvelin yhdistetään automaattisesti.
3. Klikkaa `Run` testataksesi palvelinta kehotteella.

**Onnittelut**! Olet onnistuneesti suorittanut Weather MCP Serverin omalla kehityskoneellasi Agent Builderin kautta MCP Client -asiakkaana.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Mitä mallipohjaan sisältyy

| Kansio / Tiedosto | Sisältö                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode-tiedostot virheenkorjaukseen              |
| `.aitk`      | Microsoft Foundry Toolkitin määritykset         |
| `src`        | Weather MCP -palvelimen lähdekoodi               |

## Kuinka virheenkorjata Weather MCP Serveriä

> Huomautuksia:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) on visuaalinen kehitystyökalu MCP-palvelimien testaamiseen ja virheenkorjaukseen.
> - Kaikki virheenkorjaustilat tukevat katkospisteitä, joten voit lisätä katkospisteitä työkalun toteutuskoodiin.

| Virheenkorjaustila | Kuvaus | Vaiheet virheenkorjaukseen |
| ---------- | ----------- | --------------- |
| Agent Builder | Virheenkorjaa MCP-palvelinta Agent Builderissa Microsoft Foundry Toolkitin kautta. | 1. Avaa VS Code Debug-paneeli. Valitse `Debug in Agent Builder` ja paina `F5` aloittaaksesi MCP-palvelimen virheenkorjauksen.<br>2. Valitse aktiivinen Foundry-järjestelmä, kuten `gpt-5.1`, ja syötä `What is the weather in Shanghai?`. Palvelin yhdistetään automaattisesti.<br>3. Klikkaa `Run` testataksesi palvelinta kehotteella. |
| MCP Inspector | Virheenkorjaa MCP-palvelinta MCP Inspectorilla. | 1. Asenna [Node.js](https://nodejs.org/)<br> 2. Valmistele Inspector: `cd inspector` && `npm install` <br> 3. Avaa VS Code Debug-paneeli. Valitse `Debug SSE in Inspector (Edge)` tai `Debug SSE in Inspector (Chrome)`. Paina F5 aloittaaksesi virheenkorjauksen.<br> 4. Kun MCP Inspector käynnistyy selaimessa, paina `Connect`-painiketta yhdistääksesi tämän MCP-palvelimen.<br> 5. Tämän jälkeen voit `List Tools`, valita työkalun, syöttää parametrit ja `Run Tool` virheenkorjataksesi palvelimen koodia.<br> |

## Oletusportit ja mukautukset

| Virheenkorjaustila | Portit | Määritelmät | Mukautukset | Huomautus |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Muokkaa tiedostoja [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) vaihtaaksesi yllä olevia portteja. | Ei sovellu |
| MCP Inspector | 3001 (palvelin); 5173 ja 3000 (Inspektori) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Muokkaa tiedostoja [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) vaihtaaksesi yllä olevia portteja.| Ei sovellu |

## Palaute

Jos sinulla on palautetta tai ehdotuksia tähän malliin liittyen, avaa ongelma [Microsoft Foundry Toolkit GitHub -varastossa](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->