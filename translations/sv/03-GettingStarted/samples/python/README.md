# MCP Calculator Server (Python)

En enkel serverimplementation av Model Context Protocol (MCP) i Python som erbjuder grundläggande kalkylatorfunktionalitet.

## Installation

Installera de nödvändiga beroendena:

```bash
pip install -r requirements.txt
```

Eller installera MCP Python SDK direkt:

```bash
pip install mcp>=1.18.0
```

## Användning

### Starta servern

Servern är designad för att användas av MCP-klienter (som Claude Desktop). För att starta servern:

```bash
python mcp_calculator_server.py
```

**Obs**: När du kör servern direkt i en terminal kommer du att se JSON-RPC valideringsfel. Detta är normalt beteende - servern väntar på korrekt formaterade MCP-klientmeddelanden.

### Testa funktionerna

För att testa att kalkylatorfunktionerna fungerar korrekt:

```bash
python test_calculator.py
```

## Felsökning

### Importfel

Om du ser `ModuleNotFoundError: No module named 'mcp'`, installera MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC-fel vid direkt körning

Fel som "Invalid JSON: EOF while parsing a value" när du kör servern direkt är förväntade. Servern behöver MCP-klientmeddelanden, inte direkt terminalinmatning.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.