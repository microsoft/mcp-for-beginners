# Sää MCP-palvelin

Tämä on esimerkkipalvelin Pythonilla, joka toteuttaa säätyökaluja mock-vastauksilla. Sitä voidaan käyttää pohjana omalle MCP-palvelimellesi. Se sisältää seuraavat ominaisuudet:

- **Säätyökalu**: Työkalu, joka tarjoaa mock-sääinformaatiota annetun sijainnin perusteella.
- **Git Clone -työkalu**: Työkalu, joka kloonaa git-repositorion määritettyyn kansioon.
- **VS Code Open -työkalu**: Työkalu, joka avaa kansion VS Codessa tai VS Code Insidersissa.
- **Yhdistä Agent Builderiin**: Ominaisuus, joka mahdollistaa MCP-palvelimen yhdistämisen Agent Builderiin testausta ja virheenkorjausta varten.
- **Debuggaus [MCP Inspectorilla](https://github.com/modelcontextprotocol/inspector)**: Ominaisuus, joka mahdollistaa MCP-palvelimen debuggaamisen MCP Inspectorilla.

## Aloita Sää MCP-palvelimen mallipohjalla

> **Edellytykset**
>
> Jotta voit ajaa MCP-palvelimen paikallisella kehityskoneellasi, tarvitset:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Vaaditaan git_clone_repo-työkalua varten)
> - [VS Code](https://code.visualstudio.com/) tai [VS Code Insiders](https://code.visualstudio.com/insiders/) (Vaaditaan open_in_vscode-työkalua varten)
> - (*Valinnainen - jos pidät uv:stä*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Valmistele ympäristö

Tämän projektin ympäristön voi asettaa kahdella eri tavalla. Voit valita kumman tahansa mieltymyksesi mukaan.

> Huom: Lataa VSCode tai terminaali uudelleen varmistaaksesi, että virtuaalisen ympäristön Python on käytössä ympäristön luomisen jälkeen.

| Lähestymistapa | Vaiheet |
| -------------- | ------- |
| Käyttäen `uv` | 1. Luo virtuaalinen ympäristö: `uv venv` <br>2. Suorita VSCode-komento "***Python: Select Interpreter***" ja valitse Python luodusta virtuaalisesta ympäristöstä <br>3. Asenna riippuvuudet (sisältäen kehitysriippuvuudet): `uv pip install -r pyproject.toml --extra dev` |
| Käyttäen `pip` | 1. Luo virtuaalinen ympäristö: `python -m venv .venv` <br>2. Suorita VSCode-komento "***Python: Select Interpreter***" ja valitse Python luodusta virtuaalisesta ympäristöstä <br>3. Asenna riippuvuudet (sisältäen kehitysriippuvuudet): `pip install -e .[dev]` |

Kun ympäristö on asetettu, voit ajaa palvelimen paikallisella kehityskoneellasi Agent Builderin kautta MCP Clientina aloittaaksesi:
1. Avaa VS Code Debug-paneeli. Valitse `Debug in Agent Builder` tai paina `F5` aloittaaksesi MCP-palvelimen debuggaamisen.
2. Käytä AI Toolkit Agent Builderia testataksesi palvelinta [tällä kehotteella](../../../../../../../../../../../open_prompt_builder). Palvelin yhdistetään automaattisesti Agent Builderiin.
3. Klikkaa `Run` testataksesi palvelinta kehotteella.

**Onnittelut**! Olet onnistuneesti ajanut Sää MCP-palvelimen paikallisella kehityskoneellasi Agent Builderin kautta MCP Clientina.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Mitä mallipohja sisältää

| Kansio / Tiedosto | Sisältö                                     |
| ------------------ | ------------------------------------------ |
| `.vscode`          | VSCode-tiedostot debuggausta varten        |
| `.aitk`            | AI Toolkit -konfiguraatiot                 |
| `src`              | Sää MCP-palvelimen lähdekoodi              |

## Kuinka debugata Sää MCP-palvelinta

> Huomioita:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) on visuaalinen kehitystyökalu MCP-palvelinten testaamiseen ja debuggaamiseen.
> - Kaikki debuggaustilat tukevat breakpointeja, joten voit lisätä breakpointeja työkalun toteutuskoodiin.

## Saatavilla olevat työkalut

### Säätyökalu
`get_weather`-työkalu tarjoaa mock-sääinformaatiota määritetylle sijainnille.

| Parametri | Tyyppi | Kuvaus |
| --------- | ------ | ------- |
| `location` | string | Sijainti, jolle sää halutaan (esim. kaupungin nimi, osavaltio tai koordinaatit) |

### Git Clone -työkalu
`git_clone_repo`-työkalu kloonaa git-repositorion määritettyyn kansioon.

| Parametri | Tyyppi | Kuvaus |
| --------- | ------ | ------- |
| `repo_url` | string | Kloonattavan git-repositorion URL |
| `target_folder` | string | Polku kansioon, johon repositorio kloonataan |

Työkalu palauttaa JSON-objektin, jossa on:
- `success`: Boolean, joka ilmaisee, onnistuiko operaatio
- `target_folder` tai `error`: Kloonatun repositorion polku tai virheilmoitus

### VS Code Open -työkalu
`open_in_vscode`-työkalu avaa kansion VS Codessa tai VS Code Insiders -sovelluksessa.

| Parametri | Tyyppi | Kuvaus |
| --------- | ------ | ------- |
| `folder_path` | string | Polku kansioon, joka avataan |
| `use_insiders` | boolean (valinnainen) | Käytetäänkö VS Code Insidersia tavallisen VS Coden sijaan |

Työkalu palauttaa JSON-objektin, jossa on:
- `success`: Boolean, joka ilmaisee, onnistuiko operaatio
- `message` tai `error`: Vahvistusviesti tai virheilmoitus

| Debuggaustila | Kuvaus | Debuggausvaiheet |
| ------------- | ------- | ---------------- |
| Agent Builder | Debuggaa MCP-palvelinta Agent Builderissa AI Toolkitin kautta. | 1. Avaa VS Code Debug-paneeli. Valitse `Debug in Agent Builder` ja paina `F5` aloittaaksesi MCP-palvelimen debuggaamisen.<br>2. Käytä AI Toolkit Agent Builderia testataksesi palvelinta [tällä kehotteella](../../../../../../../../../../../open_prompt_builder). Palvelin yhdistetään automaattisesti Agent Builderiin.<br>3. Klikkaa `Run` testataksesi palvelinta kehotteella. |
| MCP Inspector | Debuggaa MCP-palvelinta MCP Inspectorilla. | 1. Asenna [Node.js](https://nodejs.org/)<br> 2. Aseta Inspector: `cd inspector` && `npm install` <br> 3. Avaa VS Code Debug-paneeli. Valitse `Debug SSE in Inspector (Edge)` tai `Debug SSE in Inspector (Chrome)`. Paina F5 aloittaaksesi debuggaamisen.<br> 4. Kun MCP Inspector käynnistyy selaimessa, klikkaa `Connect`-painiketta yhdistääksesi tämän MCP-palvelimen.<br> 5. Voit sitten `List Tools`, valita työkalun, syöttää parametrit ja `Run Tool` debugataksesi palvelinkoodiasi.<br> |

## Oletusportit ja mukautukset

| Debuggaustila | Portit | Määritelmät | Mukautukset | Huomio |
| ------------- | ------ | ----------- | ----------- | ------ |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Muokkaa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) muuttaaksesi yllä olevia portteja. | Ei sovellettavissa |
| MCP Inspector | 3001 (Palvelin); 5173 ja 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Muokkaa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) muuttaaksesi yllä olevia portteja. | Ei sovellettavissa |

## Palaute

Jos sinulla on palautetta tai ehdotuksia tähän mallipohjaan liittyen, avaa issue [AI Toolkit GitHub-repositoriossa](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.