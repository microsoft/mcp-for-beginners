# MCP Kalkulátor Szerver (Python)

Egy egyszerű Model Context Protocol (MCP) szerver implementáció Pythonban, amely alapvető kalkulátor funkciókat biztosít.

## Telepítés

Telepítse a szükséges függőségeket:

```bash
pip install -r requirements.txt
```

Vagy telepítse közvetlenül az MCP Python SDK-t:

```bash
pip install mcp>=1.18.0
```

## Használat

### A szerver futtatása

A szerver MCP kliensek (például Claude Desktop) által történő használatra lett tervezve. A szerver indításához:

```bash
python mcp_calculator_server.py
```

**Megjegyzés**: Ha közvetlenül terminálban futtatja, JSON-RPC validációs hibákat fog látni. Ez normális viselkedés - a szerver megfelelően formázott MCP kliens üzenetekre vár.

### A funkciók tesztelése

Annak teszteléséhez, hogy a kalkulátor funkciók helyesen működnek-e:

```bash
python test_calculator.py
```

## Hibakeresés

### Importálási hibák

Ha a következő hibaüzenetet látja: `ModuleNotFoundError: No module named 'mcp'`, telepítse az MCP Python SDK-t:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC hibák közvetlen futtatáskor

Az olyan hibák, mint például "Invalid JSON: EOF while parsing a value", amikor közvetlenül futtatja a szervert, várhatóak. A szerver MCP kliens üzeneteket igényel, nem közvetlen terminál bemenetet.

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.