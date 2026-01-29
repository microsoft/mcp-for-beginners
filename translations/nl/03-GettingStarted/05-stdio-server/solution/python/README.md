# MCP stdio Server - Python-oplossing

> **⚠️ Belangrijk**: Deze oplossing is bijgewerkt om gebruik te maken van de **stdio-transport** zoals aanbevolen door de MCP-specificatie 2025-06-18. Het oorspronkelijke SSE-transport is verouderd.

## Overzicht

Deze Python-oplossing laat zien hoe je een MCP-server bouwt met behulp van het huidige stdio-transport. Het stdio-transport is eenvoudiger, veiliger en biedt betere prestaties dan de verouderde SSE-aanpak.

## Vereisten

- Python 3.8 of hoger
- Het wordt aanbevolen om `uv` te installeren voor pakketbeheer, zie [instructies](https://docs.astral.sh/uv/#highlights)

## Installatie-instructies

### Stap 1: Maak een virtuele omgeving aan

```bash
python -m venv venv
```

### Stap 2: Activeer de virtuele omgeving

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Stap 3: Installeer de afhankelijkheden

```bash
pip install mcp
```

## De server starten

De stdio-server werkt anders dan de oude SSE-server. In plaats van een webserver te starten, communiceert deze via stdin/stdout:

```bash
python server.py
```

**Belangrijk**: Het lijkt alsof de server vastloopt - dit is normaal! De server wacht op JSON-RPC-berichten via stdin.

## De server testen

### Methode 1: Gebruik de MCP Inspector (Aanbevolen)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Dit zal:
1. Je server als subprocess starten
2. Een webinterface openen voor testen
3. Je in staat stellen om alle servertools interactief te testen

### Methode 2: Direct JSON-RPC testen

Je kunt ook testen door direct JSON-RPC-berichten te sturen:

1. Start de server: `python server.py`
2. Stuur een JSON-RPC-bericht (voorbeeld):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. De server zal reageren met beschikbare tools

### Beschikbare tools

De server biedt de volgende tools:

- **add(a, b)**: Twee getallen bij elkaar optellen
- **multiply(a, b)**: Twee getallen met elkaar vermenigvuldigen  
- **get_greeting(name)**: Een gepersonaliseerde begroeting genereren
- **get_server_info()**: Informatie over de server ophalen

### Testen met Claude Desktop

Om deze server te gebruiken met Claude Desktop, voeg je deze configuratie toe aan je `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Belangrijke verschillen met SSE

**stdio-transport (Huidig):**
- ✅ Eenvoudigere installatie - geen webserver nodig
- ✅ Betere beveiliging - geen HTTP-eindpunten
- ✅ Communicatie op basis van subprocessen
- ✅ JSON-RPC via stdin/stdout
- ✅ Betere prestaties

**SSE-transport (Verouderd):**
- ❌ Vereiste HTTP-serverconfiguratie
- ❌ Webframework nodig (Starlette/FastAPI)
- ❌ Complexere routing en sessiebeheer
- ❌ Extra beveiligingsoverwegingen
- ❌ Nu verouderd in MCP 2025-06-18

## Tips voor foutopsporing

- Gebruik `stderr` voor logging (nooit `stdout`)
- Test met de Inspector voor visuele foutopsporing
- Zorg ervoor dat alle JSON-berichten gescheiden zijn door nieuwe regels
- Controleer of de server zonder fouten start

Deze oplossing volgt de huidige MCP-specificatie en demonstreert best practices voor de implementatie van stdio-transport.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.