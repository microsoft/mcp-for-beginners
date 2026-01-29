# MCP stdio Server - TypeScript Oplossing

> **⚠️ Belangrijk**: Deze oplossing is bijgewerkt om gebruik te maken van de **stdio transport** zoals aanbevolen in MCP Specificatie 2025-06-18. De oorspronkelijke SSE transport is verouderd.

## Overzicht

Deze TypeScript-oplossing laat zien hoe je een MCP-server bouwt met de huidige stdio transport. De stdio transport is eenvoudiger, veiliger en biedt betere prestaties dan de verouderde SSE-aanpak.

## Vereisten

- Node.js 18+ of later
- npm of yarn pakketbeheerder

## Installatie-instructies

### Stap 1: Installeer de afhankelijkheden

```bash
npm install
```

### Stap 2: Bouw het project

```bash
npm run build
```

## De Server Uitvoeren

De stdio-server werkt anders dan de oude SSE-server. In plaats van een webserver te starten, communiceert hij via stdin/stdout:

```bash
npm start
```

**Belangrijk**: Het lijkt alsof de server vastloopt - dit is normaal! Hij wacht op JSON-RPC-berichten via stdin.

## De Server Testen

### Methode 1: Gebruik de MCP Inspector (Aanbevolen)

```bash
npm run inspector
```

Dit zal:
1. Je server starten als een subprocess
2. Een webinterface openen voor testen
3. Je in staat stellen om alle servertools interactief te testen

### Methode 2: Direct testen via de commandoregel

Je kunt ook testen door de Inspector direct te starten:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Beschikbare Tools

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
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Projectstructuur

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Belangrijke Verschillen met SSE

**stdio transport (Huidig):**
- ✅ Eenvoudigere setup - geen HTTP-server nodig
- ✅ Betere beveiliging - geen HTTP-endpoints
- ✅ Communicatie op basis van subprocessen
- ✅ JSON-RPC via stdin/stdout
- ✅ Betere prestaties

**SSE transport (Verouderd):**
- ❌ Vereiste Express-server setup
- ❌ Complexe routing en sessiebeheer nodig
- ❌ Meer afhankelijkheden (Express, HTTP-afhandeling)
- ❌ Extra beveiligingsmaatregelen nodig
- ❌ Nu verouderd in MCP 2025-06-18

## Ontwikkeltips

- Gebruik `console.error()` voor loggen (nooit `console.log()` omdat dit naar stdout schrijft)
- Bouw met `npm run build` voordat je test
- Test met de Inspector voor visuele debugging
- Zorg ervoor dat alle JSON-berichten correct zijn geformatteerd
- De server handelt automatisch een nette afsluiting af bij SIGINT/SIGTERM

Deze oplossing volgt de huidige MCP-specificatie en demonstreert best practices voor stdio transport implementatie met TypeScript.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.