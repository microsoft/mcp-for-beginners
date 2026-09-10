# MCP Calculator Server (Python)



En enkel Model Context Protocol (MCP) serverimplementation i Python som erbjuder grundläggande kalkylatorfunktionalitet.


## Installation

Installera de nödvändiga beroenden:

```bash
pip install -r requirements.txt
```

Eller installera MCP Python SDK direkt:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Användning

### Starta Servern

Servern är avsedd att användas av MCP-klienter (som Claude Desktop). För att starta servern:

```bash
python mcp_calculator_server.py
```

**Notera**: När den körs direkt i en terminal, kommer du se JSON-RPC valideringsfel. Detta är normalt – servern väntar på korrekt formaterade MCP-klientmeddelanden.

### Testa Funktionerna

För att testa att kalkylatorfunktionerna fungerar korrekt:

```bash
python test_calculator.py
```

## Felsökning

### Importfel

Om du ser `ModuleNotFoundError: No module named 'mcp'`, installera MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### JSON-RPC fel vid direkt körning

Fel som "Invalid JSON: EOF while parsing a value" vid direkt körning av servern förväntas. Servern behöver MCP-klientmeddelanden, inte direkt terminalinput.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->