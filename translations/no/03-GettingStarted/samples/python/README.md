# MCP Kalkulator Server (Python)

En enkel implementering av Model Context Protocol (MCP) server i Python som tilbyr grunnleggende kalkulatorfunksjonalitet.

## Installasjon

Installer de nødvendige avhengighetene:

```bash
pip install -r requirements.txt
```

Eller installer MCP Python SDK direkte:

```bash
pip install mcp>=1.18.0
```

## Bruk

### Kjøre serveren

Serveren er designet for å brukes av MCP-klienter (som Claude Desktop). For å starte serveren:

```bash
python mcp_calculator_server.py
```

**Merk**: Når du kjører direkte i en terminal, vil du se JSON-RPC-valideringsfeil. Dette er normal oppførsel - serveren venter på riktig formaterte MCP-klientmeldinger.

### Teste funksjonene

For å teste at kalkulatorfunksjonene fungerer korrekt:

```bash
python test_calculator.py
```

## Feilsøking

### Importfeil

Hvis du ser `ModuleNotFoundError: No module named 'mcp'`, installer MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC-feil ved direkte kjøring

Feil som "Invalid JSON: EOF while parsing a value" når du kjører serveren direkte er forventet. Serveren trenger MCP-klientmeldinger, ikke direkte terminalinput.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.