# MCP skaičiuoklės serveris (Python)

Paprasta Model Context Protocol (MCP) serverio implementacija Python kalba, teikianti pagrindines skaičiuoklės funkcijas.

## Įdiegimas

Įdiekite reikalingas priklausomybes:

```bash
pip install -r requirements.txt
```

Arba tiesiogiai įdiekite MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

## Naudojimas

### Serverio paleidimas

Serveris skirtas naudoti MCP klientams (pvz., Claude Desktop). Norėdami paleisti serverį:

```bash
python mcp_calculator_server.py
```

**Pastaba**: Paleidus tiesiogiai terminale, matysite JSON-RPC validacijos klaidas. Tai normalus elgesys - serveris laukia tinkamai suformatuotų MCP klientų pranešimų.

### Funkcijų testavimas

Norėdami patikrinti, ar skaičiuoklės funkcijos veikia teisingai:

```bash
python test_calculator.py
```

## Trikčių šalinimas

### Importavimo klaidos

Jei matote `ModuleNotFoundError: No module named 'mcp'`, įdiekite MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC klaidos paleidžiant tiesiogiai

Tokios klaidos kaip "Invalid JSON: EOF while parsing a value" paleidžiant serverį tiesiogiai yra tikėtinos. Serveriui reikalingi MCP klientų pranešimai, o ne tiesioginis terminalo įvestis.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius naudojant šį vertimą.