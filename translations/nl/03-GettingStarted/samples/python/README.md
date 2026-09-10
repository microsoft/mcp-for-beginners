# MCP Calculator Server (Python)



Een eenvoudige Model Context Protocol (MCP) serverimplementatie in Python die basis rekenmachinefunctionaliteit biedt.


## Installatie

Installeer de vereiste afhankelijkheden:

```bash
pip install -r requirements.txt
```

Of installeer de MCP Python SDK direct:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Gebruik

### De server draaien

De server is ontworpen om gebruikt te worden door MCP-clients (zoals Claude Desktop). Om de server te starten:

```bash
python mcp_calculator_server.py
```

**Opmerking**: Bij direct uitvoeren in een terminal zie je JSON-RPC validatiefouten. Dit is normaal gedrag - de server wacht op correct opgemaakte MCP clientberichten.

### De functies testen

Om te testen of de rekenmachinefuncties correct werken:

```bash
python test_calculator.py
```

## Problemen oplossen

### Importfouten

Als je `ModuleNotFoundError: No module named 'mcp'` ziet, installeer dan de MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### JSON-RPC fouten bij direct uitvoeren

Fouten zoals "Invalid JSON: EOF while parsing a value" bij het direct uitvoeren van de server zijn te verwachten. De server heeft MCP clientberichten nodig, geen directe terminalinvoer.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->