# MCP Calculator Server (Python)

Een eenvoudige implementatie van een Model Context Protocol (MCP) server in Python die basisfunctionaliteit voor een rekenmachine biedt.

## Installatie

Installeer de benodigde afhankelijkheden:

```bash
pip install -r requirements.txt
```

Of installeer de MCP Python SDK direct:

```bash
pip install mcp>=1.18.0
```

## Gebruik

### De server starten

De server is ontworpen om gebruikt te worden door MCP-clients (zoals Claude Desktop). Om de server te starten:

```bash
python mcp_calculator_server.py
```

**Let op**: Wanneer je de server direct in een terminal uitvoert, zie je JSON-RPC validatiefouten. Dit is normaal gedrag - de server wacht op correct geformatteerde MCP-clientberichten.

### De functies testen

Om te testen of de rekenmachinefuncties correct werken:

```bash
python test_calculator.py
```

## Problemen oplossen

### Importfouten

Als je de foutmelding `ModuleNotFoundError: No module named 'mcp'` ziet, installeer dan de MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC fouten bij direct uitvoeren

Fouten zoals "Invalid JSON: EOF while parsing a value" bij het direct uitvoeren van de server zijn te verwachten. De server heeft MCP-clientberichten nodig, geen directe invoer via de terminal.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.