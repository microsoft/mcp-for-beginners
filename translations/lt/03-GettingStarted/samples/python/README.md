# MCP skaičiuoklės serveris (Python)



Paprasta Modelio konteksto protokolo (MCP) serverio implementacija Python, kuri teikia pagrindines skaičiuoklės funkcijas.


## Įdiegimas

Įdiekite reikalingas priklausomybes:

```bash
pip install -r requirements.txt
```

Arba įdiekite MCP Python SDK tiesiogiai:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Naudojimas

### Serverio paleidimas

Serveris skirtas naudoti MCP klientų (pvz., Claude Desktop). Norėdami paleisti serverį:

```bash
python mcp_calculator_server.py
```

**Pastaba**: kai paleidžiate tiesiogiai terminale, matysite JSON-RPC tikrinimo klaidas. Tai įprasta elgsena – serveris laukia teisingai suformatuotų MCP kliento žinučių.

### Funkcijų testavimas

Norėdami patikrinti, ar skaičiuoklės funkcijos veikia tinkamai:

```bash
python test_calculator.py
```

## Trikčių šalinimas

### Importavimo klaidos

Jei matote `ModuleNotFoundError: No module named 'mcp'`, įdiekite MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### JSON-RPC klaidos paleidžiant tiesiogiai

Klaidos, tokios kaip „Invalid JSON: EOF while parsing a value“ paleidžiant serverį tiesiai, yra numatytos. Serveriui reikalingos MCP kliento žinutės, o ne tiesioginė terminalo įvestis.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->