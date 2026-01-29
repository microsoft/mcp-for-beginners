# Weather MCP Server

Tai yra pavyzdinis MCP serveris, parašytas Python kalba, kuris įgyvendina orų įrankius su imituotais atsakymais. Jis gali būti naudojamas kaip pagrindas kuriant savo MCP serverį. Šiame serveryje yra šios funkcijos:

- **Orų įrankis**: Įrankis, kuris pateikia imituotą orų informaciją pagal nurodytą vietą.
- **Prisijungimas prie Agent Builder**: Funkcija, leidžianti prijungti MCP serverį prie Agent Builder testavimui ir derinimui.
- **Derinimas naudojant [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Funkcija, leidžianti derinti MCP serverį naudojant MCP Inspector.

## Pradėkite naudotis Weather MCP Server šablonu

> **Reikalavimai**
>
> Norint paleisti MCP serverį savo vietinėje kūrimo mašinoje, jums reikės:
>
> - [Python](https://www.python.org/)
> - (*Pasirinktinai - jei naudojate uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Aplinkos paruošimas

Yra du būdai, kaip nustatyti šio projekto aplinką. Galite pasirinkti bet kurį iš jų pagal savo pageidavimus.

> Pastaba: Perkraukite VSCode arba terminalą, kad įsitikintumėte, jog po virtualios aplinkos sukūrimo naudojama tinkama Python versija.

| Metodas | Veiksmai |
| -------- | -------- |
| Naudojant `uv` | 1. Sukurkite virtualią aplinką: `uv venv` <br>2. Paleiskite VSCode komandą "***Python: Select Interpreter***" ir pasirinkite Python iš sukurtos virtualios aplinkos <br>3. Įdiekite priklausomybes (įskaitant kūrimo priklausomybes): `uv pip install -r pyproject.toml --extra dev` |
| Naudojant `pip` | 1. Sukurkite virtualią aplinką: `python -m venv .venv` <br>2. Paleiskite VSCode komandą "***Python: Select Interpreter***" ir pasirinkite Python iš sukurtos virtualios aplinkos <br>3. Įdiekite priklausomybes (įskaitant kūrimo priklausomybes): `pip install -e .[dev]` |

Po aplinkos nustatymo galite paleisti serverį savo vietinėje kūrimo mašinoje naudodami Agent Builder kaip MCP klientą, kad pradėtumėte:
1. Atidarykite VS Code derinimo skydelį. Pasirinkite `Debug in Agent Builder` arba paspauskite `F5`, kad pradėtumėte derinti MCP serverį.
2. Naudokite AI Toolkit Agent Builder, kad išbandytumėte serverį su [šiuo raginimu](../../../../../../../../../../../open_prompt_builder). Serveris bus automatiškai prijungtas prie Agent Builder.
3. Spustelėkite `Run`, kad išbandytumėte serverį su raginimu.

**Sveikiname**! Jūs sėkmingai paleidote Weather MCP Server savo vietinėje kūrimo mašinoje naudodami Agent Builder kaip MCP klientą.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Kas įtraukta į šabloną

| Aplankas / Failas | Turinys                                     |
| ----------------- | ------------------------------------------- |
| `.vscode`         | VSCode failai derinimui                    |
| `.aitk`           | AI Toolkit konfigūracijos                  |
| `src`             | Weather MCP serverio šaltinio kodas        |

## Kaip derinti Weather MCP Server

> Pastabos:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) yra vizualus kūrėjų įrankis MCP serverių testavimui ir derinimui.
> - Visos derinimo parinktys palaiko lūžio taškus, todėl galite pridėti lūžio taškus įrankio įgyvendinimo kode.

| Derinimo režimas | Aprašymas | Derinimo veiksmai |
| ---------------- | --------- | ----------------- |
| Agent Builder    | Derinkite MCP serverį Agent Builder naudodami AI Toolkit. | 1. Atidarykite VS Code derinimo skydelį. Pasirinkite `Debug in Agent Builder` ir paspauskite `F5`, kad pradėtumėte derinti MCP serverį.<br>2. Naudokite AI Toolkit Agent Builder, kad išbandytumėte serverį su [šiuo raginimu](../../../../../../../../../../../open_prompt_builder). Serveris bus automatiškai prijungtas prie Agent Builder.<br>3. Spustelėkite `Run`, kad išbandytumėte serverį su raginimu. |
| MCP Inspector    | Derinkite MCP serverį naudodami MCP Inspector. | 1. Įdiekite [Node.js](https://nodejs.org/)<br> 2. Nustatykite Inspector: `cd inspector` && `npm install` <br> 3. Atidarykite VS Code derinimo skydelį. Pasirinkite `Debug SSE in Inspector (Edge)` arba `Debug SSE in Inspector (Chrome)`. Paspauskite F5, kad pradėtumėte derinti.<br> 4. Kai MCP Inspector paleidžiamas naršyklėje, spustelėkite mygtuką `Connect`, kad prijungtumėte šį MCP serverį.<br> 5. Tada galite `List Tools`, pasirinkti įrankį, įvesti parametrus ir `Run Tool`, kad derintumėte savo serverio kodą.<br> |

## Numatytieji prievadai ir pritaikymai

| Derinimo režimas | Prievadai | Apibrėžimai | Pritaikymai | Pastaba |
| ---------------- | --------- | ----------- | ----------- | ------- |
| Agent Builder    | 3001      | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Redaguokite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json), kad pakeistumėte aukščiau nurodytus prievadus. | N/A |
| MCP Inspector    | 3001 (Serveris); 5173 ir 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Redaguokite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json), kad pakeistumėte aukščiau nurodytus prievadus. | N/A |

## Atsiliepimai

Jei turite atsiliepimų ar pasiūlymų dėl šio šablono, prašome atidaryti problemą [AI Toolkit GitHub saugykloje](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.