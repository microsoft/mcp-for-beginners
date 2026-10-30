# Weather MCP Server

Ovo je primjer MCP poslužitelja u Pythonu koji implementira vremenske alate s lažnim odgovorima. Može se koristiti kao osnova za vaš vlastiti MCP poslužitelj. Uključuje sljedeće značajke:

- **Vremenski alat**: Alat koji pruža lažne vremenske informacije na temelju zadane lokacije.
- **Povezivanje s Agent Builderom**: Značajka koja vam omogućuje povezivanje MCP poslužitelja s Agent Builderom za testiranje i ispravljanje pogrešaka.
- **Ispravljanje pogrešaka u [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Značajka koja vam omogućuje ispravljanje pogrešaka MCP poslužitelja koristeći MCP Inspector.

## Početak s predloškom Weather MCP Server

> **Preduvjeti**
>
> Za pokretanje MCP poslužitelja na vašem lokalnom razvojnom računalu potrebni su vam:
>
> - [Python](https://www.python.org/)
> - (*Opcionalno - ako preferirate uv*) [uv](https://github.com/astral-sh/uv)
> - [Proširenje za Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Priprema okruženja

Postoje dva pristupa za postavljanje okruženja za ovaj projekt. Možete odabrati jedan ovisno o vašim željama.

> Napomena: Ponovo učitajte VSCode ili terminal kako biste osigurali da se koristi Python iz virtualnog okruženja nakon stvaranja virtualnog okruženja.

| Pristup | Koraci |
| -------- | ----- |
| Koristeći `uv` | 1. Napravite virtualno okruženje: `uv venv` <br>2. Pokrenite VSCode naredbu "***Python: Select Interpreter***" i odaberite Python iz stvorenog virtualnog okruženja <br>3. Instalirajte ovisnosti (uključujući razvojne ovisnosti): `uv pip install -r pyproject.toml --extra dev` |
| Koristeći `pip` | 1. Napravite virtualno okruženje: `python -m venv .venv` <br>2. Pokrenite VSCode naredbu "***Python: Select Interpreter***" i odaberite Python iz stvorenog virtualnog okruženja<br>3. Instalirajte ovisnosti (uključujući razvojne ovisnosti): `pip install -e .[dev]` | 

Nakon postavljanja okruženja, možete pokrenuti poslužitelj na vašem lokalnom razvojnom računalu putem Agent Buildera kao MCP klijenta da biste započeli:
1. Otvorite VS Code Debug panel. Odaberite `Debug in Agent Builder` ili pritisnite `F5` za početak ispravljanja pogrešaka MCP poslužitelja.
2. U Microsoft Foundry Toolkit Agent Builderu odaberite aktivnu Foundry implementaciju kao što je `gpt-5.1`, zatim unesite: `What is the weather in Shanghai?`. Poslužitelj će se automatski povezati.
3. Kliknite `Run` za testiranje poslužitelja s promptom.

**Čestitamo**! Uspješno ste pokrenuli Weather MCP Server na vašem lokalnom razvoju računala putem Agent Buildera kao MCP klijenta.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Što predložak uključuje

| Mapa / Datoteka| Sadržaj                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode datoteke za ispravljanje pogrešaka                   |
| `.aitk`      | Konfiguracije za Microsoft Foundry Toolkit                |
| `src`        | Izvorni kod za weather MCP poslužitelj   |

## Kako ispravljati pogreške Weather MCP Servera

> Napomene:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) je vizualni razvojni alat za testiranje i ispravljanje pogrešaka MCP poslužitelja.
> - Svi načini ispravljanja pogrešaka podržavaju prekide, tako da možete dodati prekide u kod implementacije alata.

| Način ispravljanja | Opis | Koraci za ispravljanje pogrešaka |
| ---------- | ----------- | --------------- |
| Agent Builder | Ispravljajte pogreške MCP poslužitelja u Agent Builderu putem Microsoft Foundry Toolkit. | 1. Otvorite VS Code Debug panel. Odaberite `Debug in Agent Builder` i pritisnite `F5` za početak ispravljanja pogrešaka MCP poslužitelja.<br>2. Odaberite aktivnu Foundry implementaciju kao što je `gpt-5.1`, zatim unesite `What is the weather in Shanghai?`. Poslužitelj će se automatski povezati.<br>3. Kliknite `Run` za testiranje poslužitelja s promptom. |
| MCP Inspector | Ispravljajte pogreške MCP poslužitelja koristeći MCP Inspector. | 1. Instalirajte [Node.js](https://nodejs.org/)<br> 2. Postavite Inspector: `cd inspector` && `npm install` <br> 3. Otvorite VS Code Debug panel. Odaberite `Debug SSE in Inspector (Edge)` ili `Debug SSE in Inspector (Chrome)`. Pritisnite F5 za početak ispravljanja.<br> 4. Kad se MCP Inspector pokrene u pregledniku, kliknite gumb `Connect` za povezivanje s ovim MCP poslužiteljem.<br> 5. Tada možete `List Tools`, odabrati alat, unijeti parametre i `Run Tool` za ispravljanje koda poslužitelja.<br> |

## Zadani portovi i prilagodbe

| Način ispravljanja | Portovi | Definicije | Prilagodbe | Napomena |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Uredite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) za promjenu navedenih portova. | N/A |
| MCP Inspector | 3001 (Poslužitelj); 5173 i 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Uredite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) za promjenu navedenih portova. | N/A |

## Povratne informacije

Ako imate bilo kakve povratne informacije ili prijedloge za ovaj predložak, molimo otvorite problem na [Microsoft Foundry Toolkit GitHub spremištu](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->