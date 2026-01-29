# MCP strežnik kalkulatorja (Python)

Preprosta implementacija strežnika Model Context Protocol (MCP) v Pythonu, ki omogoča osnovno funkcionalnost kalkulatorja.

## Namestitev

Namestite potrebne odvisnosti:

```bash
pip install -r requirements.txt
```

Ali pa neposredno namestite MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

## Uporaba

### Zagon strežnika

Strežnik je zasnovan za uporabo s MCP odjemalci (kot je Claude Desktop). Za zagon strežnika:

```bash
python mcp_calculator_server.py
```

**Opomba**: Ko strežnik zaženete neposredno v terminalu, boste videli napake pri preverjanju JSON-RPC. To je normalno vedenje - strežnik čaka na pravilno oblikovana sporočila MCP odjemalca.

### Testiranje funkcij

Za testiranje, ali funkcije kalkulatorja delujejo pravilno:

```bash
python test_calculator.py
```

## Odpravljanje težav

### Napake pri uvozu

Če vidite `ModuleNotFoundError: No module named 'mcp'`, namestite MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### Napake JSON-RPC pri neposrednem zagonu

Napake, kot je "Invalid JSON: EOF while parsing a value", pri neposrednem zagonu strežnika so pričakovane. Strežnik potrebuje sporočila MCP odjemalca, ne neposrednega vnosa v terminal.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.