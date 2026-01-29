# MCP Calculator Server (Python)

En simpel Model Context Protocol (MCP) serverimplementering i Python, der tilbyder grundlæggende regnefunktionalitet.

## Installation

Installer de nødvendige afhængigheder:

```bash
pip install -r requirements.txt
```

Eller installer MCP Python SDK direkte:

```bash
pip install mcp>=1.18.0
```

## Brug

### Start serveren

Serveren er designet til at blive brugt af MCP-klienter (som Claude Desktop). For at starte serveren:

```bash
python mcp_calculator_server.py
```

**Bemærk**: Når serveren køres direkte i en terminal, vil du se JSON-RPC valideringsfejl. Dette er normal opførsel - serveren venter på korrekt formaterede MCP-klientmeddelelser.

### Test funktionerne

For at teste, at regnefunktionerne fungerer korrekt:

```bash
python test_calculator.py
```

## Fejlfinding

### Importfejl

Hvis du ser `ModuleNotFoundError: No module named 'mcp'`, skal du installere MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC fejl ved direkte kørsel

Fejl som "Invalid JSON: EOF while parsing a value" ved direkte kørsel af serveren er forventet. Serveren kræver MCP-klientmeddelelser og ikke direkte terminalinput.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.