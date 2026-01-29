# MCP stdio Server - Python rješenje

> **⚠️ Važno**: Ovo rješenje je ažurirano kako bi koristilo **stdio transport** prema preporuci MCP specifikacije 2025-06-18. Izvorni SSE transport je ukinut.

## Pregled

Ovo Python rješenje pokazuje kako izraditi MCP server koristeći trenutni stdio transport. Stdio transport je jednostavniji, sigurniji i pruža bolje performanse od zastarjelog SSE pristupa.

## Preduvjeti

- Python 3.8 ili noviji
- Preporučuje se instalacija `uv` za upravljanje paketima, pogledajte [upute](https://docs.astral.sh/uv/#highlights)

## Upute za postavljanje

### Korak 1: Kreirajte virtualno okruženje

```bash
python -m venv venv
```

### Korak 2: Aktivirajte virtualno okruženje

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Korak 3: Instalirajte ovisnosti

```bash
pip install mcp
```

## Pokretanje servera

Stdio server radi drugačije od starog SSE servera. Umjesto pokretanja web servera, komunicira putem stdin/stdout:

```bash
python server.py
```

**Važno**: Server će izgledati kao da se "zamrznuo" - to je normalno! Čeka JSON-RPC poruke putem stdin.

## Testiranje servera

### Metoda 1: Korištenje MCP Inspectora (Preporučeno)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Ovo će:
1. Pokrenuti vaš server kao podproces
2. Otvoriti web sučelje za testiranje
3. Omogućiti interaktivno testiranje svih alata servera

### Metoda 2: Direktno JSON-RPC testiranje

Možete testirati i slanjem JSON-RPC poruka direktno:

1. Pokrenite server: `python server.py`
2. Pošaljite JSON-RPC poruku (primjer):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Server će odgovoriti s dostupnim alatima

### Dostupni alati

Server pruža sljedeće alate:

- **add(a, b)**: Zbraja dva broja
- **multiply(a, b)**: Množi dva broja  
- **get_greeting(name)**: Generira personalizirani pozdrav
- **get_server_info()**: Dohvaća informacije o serveru

### Testiranje s Claude Desktopom

Za korištenje ovog servera s Claude Desktopom, dodajte ovu konfiguraciju u vaš `claude_desktop_config.json`:

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

## Ključne razlike u odnosu na SSE

**stdio transport (Trenutni):**
- ✅ Jednostavnije postavljanje - nije potreban web server
- ✅ Bolja sigurnost - nema HTTP krajnjih točaka
- ✅ Komunikacija temeljena na podprocesima
- ✅ JSON-RPC putem stdin/stdout
- ✅ Bolje performanse

**SSE transport (Zastarjelo):**
- ❌ Zahtijevao postavljanje HTTP servera
- ❌ Potrebni web framework (Starlette/FastAPI)
- ❌ Složenije upravljanje rutama i sesijama
- ❌ Dodatni sigurnosni izazovi
- ❌ Sada ukinut u MCP 2025-06-18

## Savjeti za otklanjanje pogrešaka

- Koristite `stderr` za logiranje (nikada `stdout`)
- Testirajte s Inspectorom za vizualno otklanjanje pogrešaka
- Provjerite da su sve JSON poruke odvojene novim redom
- Provjerite da server započinje bez grešaka

Ovo rješenje slijedi trenutnu MCP specifikaciju i demonstrira najbolje prakse za implementaciju stdio transporta.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.