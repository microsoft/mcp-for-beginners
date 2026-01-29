# MCP Kalkulator Server (Python)

Jednostavna implementacija Model Context Protocol (MCP) servera u Pythonu koja pruža osnovnu funkcionalnost kalkulatora.

## Instalacija

Instalirajte potrebne ovisnosti:

```bash
pip install -r requirements.txt
```

Ili izravno instalirajte MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

## Upotreba

### Pokretanje Servera

Server je dizajniran za korištenje od strane MCP klijenata (poput Claude Desktopa). Za pokretanje servera:

```bash
python mcp_calculator_server.py
```

**Napomena**: Kada se pokrene izravno u terminalu, vidjet ćete JSON-RPC pogreške validacije. Ovo je normalno ponašanje - server čeka pravilno formatirane poruke MCP klijenta.

### Testiranje Funkcija

Za testiranje ispravnosti funkcija kalkulatora:

```bash
python test_calculator.py
```

## Rješavanje problema

### Pogreške pri uvozu

Ako vidite `ModuleNotFoundError: No module named 'mcp'`, instalirajte MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC pogreške pri izravnom pokretanju

Pogreške poput "Invalid JSON: EOF while parsing a value" pri izravnom pokretanju servera su očekivane. Server zahtijeva poruke MCP klijenta, a ne izravni unos u terminal.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.