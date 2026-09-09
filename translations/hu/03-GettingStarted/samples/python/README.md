# MCP számológép szerver (Python)



Egy egyszerű Model Context Protocol (MCP) szerver megvalósítás Pythonban, amely alapvető számológép funkcionalitást biztosít.


## Telepítés

Telepítse a szükséges függőségeket:

```bash
pip install -r requirements.txt
```

Vagy telepítse közvetlenül az MCP Python SDK-t:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Használat

### A szerver indítása

A szervert MCP kliensek (például Claude Desktop) használatára tervezték. A szerver indításához:

```bash
python mcp_calculator_server.py
```

**Megjegyzés**: Ha közvetlenül a terminálban futtatja, JSON-RPC érvényesítési hibákat fog látni. Ez normális viselkedés – a szerver megfelelően formázott MCP kliens üzenetekre vár.

### A funkciók tesztelése

A számológép funkciók helyes működésének teszteléséhez:

```bash
python test_calculator.py
```

## Hibakeresés

### Importálási hibák

Ha ezt látja: `ModuleNotFoundError: No module named 'mcp'`, telepítse az MCP Python SDK-t:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### JSON-RPC hibák közvetlen futtatáskor

Olyan hibák, mint például "Invalid JSON: EOF while parsing a value", amikor közvetlenül futtatja a szervert, várhatóak. A szerver MCP kliens üzeneteket vár, nem közvetlen terminál bevitelét.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->