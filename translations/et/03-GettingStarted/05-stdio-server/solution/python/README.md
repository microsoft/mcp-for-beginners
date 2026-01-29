# MCP stdio Server - Python Lahendus

> **⚠️ Tähtis**: See lahendus on uuendatud, et kasutada **stdio transporti**, nagu soovitatud MCP spetsifikatsioonis 2025-06-18. Algne SSE transport on aegunud.

## Ülevaade

See Python lahendus näitab, kuidas ehitada MCP serverit, kasutades praegust stdio transporti. Stdio transport on lihtsam, turvalisem ja pakub paremat jõudlust võrreldes aegunud SSE meetodiga.

## Eeltingimused

- Python 3.8 või uuem
- Soovitatav on paigaldada `uv` pakettide haldamiseks, vaata [juhiseid](https://docs.astral.sh/uv/#highlights)

## Paigaldusjuhised

### Samm 1: Loo virtuaalne keskkond

```bash
python -m venv venv
```

### Samm 2: Aktiveeri virtuaalne keskkond

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Samm 3: Paigalda sõltuvused

```bash
pip install mcp
```

## Serveri Käivitamine

Stdio server töötab erinevalt vanast SSE serverist. Selle asemel, et käivitada veebiserver, suhtleb see stdin/stdout kaudu:

```bash
python server.py
```

**Tähtis**: Server näib justkui "hangunud" - see on normaalne! See ootab JSON-RPC sõnumeid stdin kaudu.

## Serveri Testimine

### Meetod 1: MCP Inspector'i kasutamine (Soovitatav)

```bash
npx @modelcontextprotocol/inspector python server.py
```

See teeb järgmist:
1. Käivitab serveri alamprotsessina
2. Avab veebiliidese testimiseks
3. Võimaldab interaktiivselt testida kõiki serveri tööriistu

### Meetod 2: Otsene JSON-RPC testimine

Võid testida ka JSON-RPC sõnumeid otse saates:

1. Käivita server: `python server.py`
2. Saada JSON-RPC sõnum (näide):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Server vastab saadaolevate tööriistadega

### Saadaolevad Tööriistad

Server pakub järgmisi tööriistu:

- **add(a, b)**: Liidab kaks arvu
- **multiply(a, b)**: Korrutab kaks arvu  
- **get_greeting(name)**: Loob isikupärastatud tervituse
- **get_server_info()**: Annab teavet serveri kohta

### Testimine Claude Desktopiga

Claude Desktopi kasutamiseks lisa see konfiguratsioon oma `claude_desktop_config.json` faili:

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

## Peamised Erinevused SSE-st

**stdio transport (Praegune):**
- ✅ Lihtsam seadistamine - veebiserverit pole vaja
- ✅ Parem turvalisus - HTTP lõpp-punkte pole
- ✅ Suhtlus alamprotsesside kaudu
- ✅ JSON-RPC stdin/stdout kaudu
- ✅ Parem jõudlus

**SSE transport (Aegunud):**
- ❌ Vajalik HTTP serveri seadistamine
- ❌ Vajalik veebiraamistik (Starlette/FastAPI)
- ❌ Keerukam marsruutimine ja sessioonihaldus
- ❌ Täiendavad turvalisuse kaalutlused
- ❌ Nüüd aegunud MCP 2025-06-18 spetsifikatsioonis

## Veaotsingu Näpunäited

- Kasuta logimiseks `stderr` (mitte kunagi `stdout`)
- Testi Inspector'iga visuaalseks veaotsinguks
- Veendu, et kõik JSON sõnumid oleksid reavahetusega eraldatud
- Kontrolli, et server käivituks vigadeta

See lahendus järgib praegust MCP spetsifikatsiooni ja näitab parimaid tavasid stdio transpordi rakendamiseks.

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.