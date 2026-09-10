# MCP strežnik za kalkulator (Python)



Preprosta implementacija strežnika Model Context Protocol (MCP) v Pythonu, ki zagotavlja osnovno funkcionalnost kalkulatorja.


## Namestitev

Namestite potrebne odvisnosti:

```bash
pip install -r requirements.txt
```

Ali pa namestite MCP Python SDK neposredno:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Uporaba

### Zagon strežnika

Strežnik je zasnovan za uporabo s strani MCP klientov (kot je Claude Desktop). Za zagon strežnika:

```bash
python mcp_calculator_server.py
```

**Opomba**: Ko ga zaženete neposredno v terminalu, boste videli napake validacije JSON-RPC. To je normalen pojav - strežnik čaka na pravilno oblikovana sporočila MCP klienta.

### Testiranje funkcij

Za preverjanje pravilnega delovanja funkcij kalkulatorja:

```bash
python test_calculator.py
```

## Odpravljanje težav

### Napake pri uvozu

Če vidite `ModuleNotFoundError: No module named 'mcp'`, namestite MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Napake JSON-RPC pri neposrednem zagonu

Pri neposrednem zagonu strežnika so pričakovane napake, kot je "Invalid JSON: EOF while parsing a value". Strežnik potrebuje sporočila MCP klienta, ne pa neposredne vnose iz terminala.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->