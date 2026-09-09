# MCP Calculator Server (Python)



Jednostavna implementacija Model Context Protocol (MCP) servera u Pythonu koja pruža osnovnu funkcionalnost kalkulatora.


## Instalacija

Instalirajte potrebne ovisnosti:

```bash
pip install -r requirements.txt
```

Ili instalirajte MCP Python SDK izravno:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Upotreba

### Pokretanje servera

Server je namijenjen za korištenje od strane MCP klijenata (kao što je Claude Desktop). Za pokretanje servera:

```bash
python mcp_calculator_server.py
```

**Napomena**: Kada se pokreće izravno u terminalu, vidjet ćete JSON-RPC pogreške provjere valjanosti. To je normalno ponašanje – server čeka ispravno formatirane poruke MCP klijenta.

### Testiranje funkcija

Za testiranje da kalkulator funkcije rade ispravno:

```bash
python test_calculator.py
```

## Rješavanje problema

### Pogreške u uvozu

Ako vidite `ModuleNotFoundError: No module named 'mcp'`, instalirajte MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### JSON-RPC pogreške kod izravnog pokretanja

Pogreške poput "Invalid JSON: EOF while parsing a value" kod izravnog pokretanja servera su očekivane. Server treba poruke MCP klijenta, ne izravni unos u terminal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->