# Weather MCP -palvelin

Tämä on esimerkkipalvelin Pythonissa, joka toteuttaa säätyökaluja mallivastauksilla. Sitä voidaan käyttää viritelmänä omalle MCP-palvelimellesi. Se sisältää seuraavat ominaisuudet:

- **Weather Tool**: Työkalu, joka tarjoaa mallinnettua sääinformaatiota annetun sijainnin perusteella.
- **Git Clone Tool**: Työkalu, joka kloonaa git-repositorion määritettyyn kansioon.
- **VS Code Open Tool**: Työkalu, joka avaa kansion VS Codessa tai VS Code Insidersissa.
- **Yhdistä Agent Builderiin**: Ominaisuus, joka mahdollistaa MCP-palvelimen yhdistämisen Agent Builderiin testaukseen ja vianetsintään.
- **Vianetsintä [MCP Inspectorilla](https://github.com/modelcontextprotocol/inspector)**: Ominaisuus, joka mahdollistaa MCP-palvelimen vianetsinnän MCP Inspector -työkalulla.

## Aloita Weather MCP -palvelimen mallipohjalla

> **Esivaatimukset**
>
> Jotta voit ajaa MCP-palvelinta paikallisessa kehitysympäristössäsi, tarvitset:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (vaaditaan git_clone_repo-työkaluun)
> - [VS Code](https://code.visualstudio.com/) tai [VS Code Insiders](https://code.visualstudio.com/insiders/) (vaaditaan open_in_vscode-työkaluun)
> - (*Valinnainen - jos haluat käyttää uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Ympäristön valmistelu

Tämän projektin ympäristön pystyttämiseen on kaksi lähestymistapaa. Voit valita jommankumman mieltymyksesi mukaan.

> Huom: Lataa VSCode tai terminaali uudelleen varmistaaksesi, että virtuaaliympäristön python otetaan käyttöön luomisen jälkeen.

| Lähestymistapa | Vaiheet |
| -------- | ----- |
| Käyttämällä `uv` | 1. Luo virtuaaliympäristö: `uv venv` <br>2. Suorita VSCode-komento "***Python: Select Interpreter***" ja valitse luodun virtuaaliympäristön python <br>3. Asenna riippuvuudet (sisältää kehitysriippuvuudet): `uv pip install -r pyproject.toml --extra dev` |
| Käyttämällä `pip` | 1. Luo virtuaaliympäristö: `python -m venv .venv` <br>2. Suorita VSCode-komento "***Python: Select Interpreter***" ja valitse luodun virtuaaliympäristön python<br>3. Asenna riippuvuudet (sisältää kehitysriippuvuudet): `pip install -e .[dev]` |

Ympäristön pystyttämisen jälkeen voit ajaa palvelimen paikallisessa kehitysympäristössäsi Agent Builderin kautta MCP-asiakkaana aloittaaksesi:
1. Avaa VS Code Debug -paneeli. Valitse `Debug in Agent Builder` tai paina `F5` aloittaaksesi MCP-palvelimen vianetsinnän.
2. Microsoft Foundry Toolkit for Visual Studio Code Agent Builderissa valitse aktiivinen Foundry-julkaisu, kuten `gpt-5.1`, ja syötä: `What is the weather in Shanghai?` Palvelin yhdistetään automaattisesti.
3. Klikkaa `Run` testataksesi palvelinta kehotteen avulla.

**Onnittelut**! Olet onnistuneesti ajanut Weather MCP -palvelimen paikallisessa kehitysympäristössäsi Agent Builderin kautta MCP-asiakkaana.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Mallipohjan sisältö

| Kansiot / Tiedostot | Sisältö                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode-tiedostot vianetsintään                    |
| `.aitk`      | Microsoft Foundry Toolkit -asetukset               |
| `src`        | Weather MCP -palvelimen lähdekoodi                 |

## Kuinka vianetsit Weather MCP -palvelinta

> Huomioita:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) on visuaalinen kehittäjätyökalu MCP-palvelinten testaamiseen ja vianetsintään.
> - Kaikki vianetsintätilat tukevat taukopisteitä, joten voit lisätä taukopisteitä työkalun toteutuskoodiin.

## Saatavilla olevat työkalut

### Weather Tool
`get_weather`-työkalu tarjoaa mallinnettua sääinformaatiota määritetystä sijainnista.

| Parametri | Tyyppi | Kuvaus |
| --------- | ---- | ----------- |
| `location` | string | Sijainti, jolle sää pyydetään (esim. kaupungin nimi, osavaltio tai koordinaatit) |

### Git Clone Tool
`git_clone_repo`-työkalu kloonaa git-repositorion määritettyyn kansioon.

| Parametri | Tyyppi | Kuvaus |
| --------- | ---- | ----------- |
| `repo_url` | string | Git-repositorion URL-osoite, joka kloonataan |
| `target_folder` | string | Polku kansioon, johon repositorio kloonataan |

Työkalu palauttaa JSON-objektin, joka sisältää:
- `success`: Totuusarvon, joka indikoi, onnistuiko operaatio
- `target_folder` tai `error`: Kloonatun repositorion polku tai virheilmoitus

### VS Code Open Tool
`open_in_vscode`-työkalu avaa kansion VS Codessa tai VS Code Insiders -sovelluksessa.

| Parametri | Tyyppi | Kuvaus |
| --------- | ---- | ----------- |
| `folder_path` | string | Polku avattavaan kansioon |
| `use_insiders` | boolean (valinnainen) | Käytetäänkö VS Code Insidersia tavallisen VS Coden sijaan |

Työkalu palauttaa JSON-objektin, joka sisältää:
- `success`: Totuusarvon, joka indikoi, onnistuiko operaatio
- `message` tai `error`: Vahvistusviesti tai virheilmoitus

| Vianetsintätila | Kuvaus | Vianetsinnän vaiheet |
| ---------- | ----------- | --------------- |
| Agent Builder | Vianetsii MCP-palvelinta Agent Builderissa Microsoft Foundry Toolkit for Visual Studio Code kautta. | 1. Avaa VS Code Debug -paneeli. Valitse `Debug in Agent Builder` ja paina `F5` aloittaaksesi MCP-palvelimen vianetsinnän.<br>2. Valitse aktiivinen Foundry-julkaisu, kuten `gpt-5.1`, ja syötä `What is the weather in Shanghai?`. Palvelin yhdistetään automaattisesti.<br>3. Klikkaa `Run` testataksesi palvelinta kehotteen avulla. |
| MCP Inspector | Vianetsii MCP-palvelinta MCP Inspector -työkalulla. | 1. Asenna [Node.js](https://nodejs.org/)<br> 2. Valmistele Inspector: `cd inspector` && `npm install` <br> 3. Avaa VS Code Debug -paneeli. Valitse `Debug SSE in Inspector (Edge)` tai `Debug SSE in Inspector (Chrome)`. Paina F5 aloittaaksesi vianetsinnän.<br> 4. Kun MCP Inspector käynnistyy selaimessa, klikkaa `Connect`-painiketta yhdistääksesi tämän MCP-palvelimen.<br> 5. Sen jälkeen voit `List Tools`, valita työkalun, syöttää parametrit ja `Run Tool` vianetsintään palvelinkoodissasi.<br> |

## Oletusportit ja mukautukset

| Vianetsintätila | Portit | Määritelmät | Mukautukset | Huomautus |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Muokkaa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) vaihtaaksesi yllä olevia portteja. | Ei sovellettavissa |
| MCP Inspector | 3001 (palvelin); 5173 ja 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Muokkaa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) vaihtaaksesi yllä olevia portteja.| Ei sovellettavissa |

## Palaute

Jos sinulla on palautetta tai ehdotuksia tähän mallipohjaan, avaa issue [Microsoft Foundry Toolkit for Visual Studio Code GitHub -varastoon](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->