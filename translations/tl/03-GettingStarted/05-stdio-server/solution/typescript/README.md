# MCP stdio Server - Solusyon sa TypeScript

> **⚠️ Mahalagang Paalala**: Ang solusyong ito ay na-update upang gumamit ng **stdio transport** ayon sa rekomendasyon ng MCP Specification 2025-06-18. Ang orihinal na SSE transport ay hindi na ginagamit.

## Pangkalahatang-ideya

Ipinapakita ng solusyong ito sa TypeScript kung paano bumuo ng isang MCP server gamit ang kasalukuyang stdio transport. Ang stdio transport ay mas simple, mas ligtas, at nagbibigay ng mas mahusay na performance kumpara sa hindi na ginagamit na SSE approach.

## Mga Kinakailangan

- Node.js 18+ o mas bago
- npm o yarn package manager

## Mga Hakbang sa Setup

### Hakbang 1: I-install ang mga dependencies

```bash
npm install
```

### Hakbang 2: I-build ang proyekto

```bash
npm run build
```

## Pagpapatakbo ng Server

Ang stdio server ay gumagana nang iba kumpara sa lumang SSE server. Sa halip na magpatakbo ng web server, ito ay nakikipag-ugnayan sa pamamagitan ng stdin/stdout:

```bash
npm start
```

**Mahalaga**: Ang server ay magmumukhang nakabitin - normal ito! Naghihintay ito ng mga JSON-RPC na mensahe mula sa stdin.

## Pagsusuri ng Server

### Paraan 1: Gamit ang MCP Inspector (Inirerekomenda)

```bash
npm run inspector
```

Ito ay:
1. Maglulunsad ng iyong server bilang subprocess
2. Magbubukas ng web interface para sa pagsusuri
3. Magbibigay-daan sa iyo na subukan ang lahat ng tools ng server nang interactive

### Paraan 2: Direktang pagsusuri gamit ang command line

Maaari mo ring subukan sa pamamagitan ng direktang paglulunsad ng Inspector:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Mga Available na Tools

Ang server ay nagbibigay ng mga sumusunod na tools:

- **add(a, b)**: Pinagsasama ang dalawang numero
- **multiply(a, b)**: Minumultiply ang dalawang numero  
- **get_greeting(name)**: Gumagawa ng personalized na pagbati
- **get_server_info()**: Nagbibigay ng impormasyon tungkol sa server

### Pagsusuri gamit ang Claude Desktop

Upang magamit ang server na ito sa Claude Desktop, idagdag ang configuration na ito sa iyong `claude_desktop_config.json`:

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

## Estruktura ng Proyekto

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Mga Pangunahing Pagkakaiba mula sa SSE

**stdio transport (Kasalukuyan):**
- ✅ Mas simpleng setup - hindi kailangan ng HTTP server
- ✅ Mas ligtas - walang HTTP endpoints
- ✅ Komunikasyon batay sa subprocess
- ✅ JSON-RPC sa stdin/stdout
- ✅ Mas mahusay na performance

**SSE transport (Hindi na ginagamit):**
- ❌ Kinakailangan ang setup ng Express server
- ❌ Kailangan ng mas komplikadong routing at session management
- ❌ Mas maraming dependencies (Express, HTTP handling)
- ❌ Dagdag na konsiderasyon sa seguridad
- ❌ Hindi na ginagamit simula MCP 2025-06-18

## Mga Tip sa Pag-develop

- Gumamit ng `console.error()` para sa pag-log (huwag gumamit ng `console.log()` dahil ito ay nagsusulat sa stdout)
- I-build gamit ang `npm run build` bago mag-test
- Subukan gamit ang Inspector para sa visual debugging
- Siguraduhing maayos ang format ng lahat ng JSON na mensahe
- Ang server ay awtomatikong humahawak ng maayos na shutdown sa SIGINT/SIGTERM

Ang solusyong ito ay sumusunod sa kasalukuyang MCP specification at nagpapakita ng pinakamahusay na mga kasanayan para sa stdio transport implementation gamit ang TypeScript.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.