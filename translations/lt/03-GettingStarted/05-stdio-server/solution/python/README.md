# MCP stdio Server - Python sprendimas

> **⚠️ Svarbu**: Šis sprendimas buvo atnaujintas, kad naudotų **stdio transportą**, kaip rekomenduojama MCP specifikacijoje 2025-06-18. Originalus SSE transportas yra nebenaudojamas.

## Apžvalga

Šis Python sprendimas parodo, kaip sukurti MCP serverį naudojant dabartinį stdio transportą. Stdio transportas yra paprastesnis, saugesnis ir užtikrina geresnį našumą nei nebenaudojamas SSE metodas.

## Reikalavimai

- Python 3.8 ar naujesnė versija
- Rekomenduojama įdiegti `uv` paketų valdymui, žr. [instrukcijas](https://docs.astral.sh/uv/#highlights)

## Nustatymo instrukcijos

### 1 žingsnis: Sukurkite virtualią aplinką

```bash
python -m venv venv
```

### 2 žingsnis: Aktyvuokite virtualią aplinką

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3 žingsnis: Įdiekite priklausomybes

```bash
pip install mcp
```

## Serverio paleidimas

Stdio serveris veikia kitaip nei senasis SSE serveris. Vietoj internetinio serverio paleidimo jis komunikuoja per stdin/stdout:

```bash
python server.py
```

**Svarbu**: Serveris gali atrodyti kaip užstrigęs - tai normalu! Jis laukia JSON-RPC pranešimų iš stdin.

## Serverio testavimas

### 1 metodas: Naudojant MCP Inspector (Rekomenduojama)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Tai atliks:
1. Paleis jūsų serverį kaip subprocesą
2. Atidarys internetinę sąsają testavimui
3. Leis interaktyviai testuoti visus serverio įrankius

### 2 metodas: Tiesioginis JSON-RPC testavimas

Taip pat galite testuoti siųsdami JSON-RPC pranešimus tiesiogiai:

1. Paleiskite serverį: `python server.py`
2. Siųskite JSON-RPC pranešimą (pavyzdys):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Serveris atsakys su galimais įrankiais

### Galimi įrankiai

Serveris siūlo šiuos įrankius:

- **add(a, b)**: Sudėti du skaičius
- **multiply(a, b)**: Padauginti du skaičius  
- **get_greeting(name)**: Sukurti asmeninį pasveikinimą
- **get_server_info()**: Gauti informaciją apie serverį

### Testavimas su Claude Desktop

Norėdami naudoti šį serverį su Claude Desktop, pridėkite šią konfigūraciją į savo `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Pagrindiniai skirtumai nuo SSE

**stdio transportas (Dabartinis):**
- ✅ Paprastesnis nustatymas - nereikia internetinio serverio
- ✅ Geresnis saugumas - nėra HTTP galinių taškų
- ✅ Komunikacija per subprocesus
- ✅ JSON-RPC per stdin/stdout
- ✅ Geresnis našumas

**SSE transportas (Nebenaudojamas):**
- ❌ Reikėjo HTTP serverio nustatymo
- ❌ Reikėjo internetinio karkaso (Starlette/FastAPI)
- ❌ Sudėtingesnis maršrutizavimas ir sesijų valdymas
- ❌ Papildomi saugumo aspektai
- ❌ Nebenaudojamas MCP 2025-06-18 specifikacijoje

## Derinimo patarimai

- Naudokite `stderr` logavimui (niekada `stdout`)
- Testuokite su Inspector vizualiam derinimui
- Įsitikinkite, kad visi JSON pranešimai yra atskirti naujos eilutės simboliu
- Patikrinkite, ar serveris paleidžiamas be klaidų

Šis sprendimas atitinka dabartinę MCP specifikaciją ir demonstruoja geriausią praktiką stdio transporto įgyvendinimui.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.