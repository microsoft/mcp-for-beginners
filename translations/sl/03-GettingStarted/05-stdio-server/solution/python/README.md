# MCP stdio strežnik - Python rešitev

> **⚠️ Pomembno**: Ta rešitev je bila posodobljena za uporabo **stdio transporta**, kot je priporočeno v MCP specifikaciji 2025-06-18. Prvotni SSE transport je bil ukinjen.

## Pregled

Ta Python rešitev prikazuje, kako zgraditi MCP strežnik z uporabo trenutnega stdio transporta. Stdio transport je enostavnejši, varnejši in zagotavlja boljšo zmogljivost kot ukinjeni pristop SSE.

## Predpogoji

- Python 3.8 ali novejši
- Priporočamo namestitev `uv` za upravljanje paketov, glejte [navodila](https://docs.astral.sh/uv/#highlights)

## Navodila za nastavitev

### Korak 1: Ustvarite virtualno okolje

```bash
python -m venv venv
```

### Korak 2: Aktivirajte virtualno okolje

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Korak 3: Namestite odvisnosti

```bash
pip install mcp
```

## Zagon strežnika

Stdio strežnik deluje drugače kot stari SSE strežnik. Namesto zagona spletnega strežnika komunicira prek stdin/stdout:

```bash
python server.py
```

**Pomembno**: Strežnik se bo zdel, kot da je "zamrznil" - to je normalno! Čaka na JSON-RPC sporočila prek stdin.

## Testiranje strežnika

### Metoda 1: Uporaba MCP Inspectorja (Priporočeno)

```bash
npx @modelcontextprotocol/inspector python server.py
```

To bo:
1. Zagnalo vaš strežnik kot podproces
2. Odprlo spletni vmesnik za testiranje
3. Omogočilo interaktivno testiranje vseh orodij strežnika

### Metoda 2: Neposredno testiranje JSON-RPC

Strežnik lahko testirate tudi z neposrednim pošiljanjem JSON-RPC sporočil:

1. Zaženite strežnik: `python server.py`
2. Pošljite JSON-RPC sporočilo (primer):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Strežnik bo odgovoril z razpoložljivimi orodji

### Razpoložljiva orodja

Strežnik ponuja naslednja orodja:

- **add(a, b)**: Sešteje dve števili
- **multiply(a, b)**: Pomnoži dve števili  
- **get_greeting(name)**: Ustvari personalizirano pozdravno sporočilo
- **get_server_info()**: Pridobi informacije o strežniku

### Testiranje s Claude Desktop

Če želite ta strežnik uporabljati s Claude Desktop, dodajte to konfiguracijo v datoteko `claude_desktop_config.json`:

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

## Ključne razlike od SSE

**stdio transport (trenutni):**
- ✅ Enostavnejša nastavitev - ni potreben spletni strežnik
- ✅ Boljša varnost - ni HTTP končnih točk
- ✅ Komunikacija na osnovi podprocesov
- ✅ JSON-RPC prek stdin/stdout
- ✅ Boljša zmogljivost

**SSE transport (ukinjen):**
- ❌ Zahteval nastavitev HTTP strežnika
- ❌ Potreboval spletni okvir (Starlette/FastAPI)
- ❌ Bolj zapleteno usmerjanje in upravljanje sej
- ❌ Dodatni varnostni vidiki
- ❌ Zdaj ukinjen v MCP 2025-06-18

## Nasveti za odpravljanje napak

- Uporabljajte `stderr` za beleženje (nikoli `stdout`)
- Testirajte z Inspectorjem za vizualno odpravljanje napak
- Prepričajte se, da so vsa JSON sporočila ločena z novimi vrsticami
- Preverite, da se strežnik zažene brez napak

Ta rešitev sledi trenutni MCP specifikaciji in prikazuje najboljše prakse za implementacijo stdio transporta.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.