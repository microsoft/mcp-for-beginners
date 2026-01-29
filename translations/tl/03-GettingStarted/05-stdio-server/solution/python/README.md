# MCP stdio Server - Solusyon sa Python

> **⚠️ Mahalagang Paalala**: Ang solusyong ito ay na-update upang gumamit ng **stdio transport** ayon sa rekomendasyon ng MCP Specification 2025-06-18. Ang orihinal na SSE transport ay hindi na ginagamit.

## Pangkalahatang-ideya

Ipinapakita ng solusyong ito sa Python kung paano bumuo ng isang MCP server gamit ang kasalukuyang stdio transport. Ang stdio transport ay mas simple, mas ligtas, at nagbibigay ng mas mahusay na performance kumpara sa lumang SSE approach.

## Mga Kinakailangan

- Python 3.8 o mas bago
- Inirerekomenda na i-install ang `uv` para sa package management, tingnan ang [mga tagubilin](https://docs.astral.sh/uv/#highlights)

## Mga Hakbang sa Setup

### Hakbang 1: Gumawa ng virtual environment

```bash
python -m venv venv
```

### Hakbang 2: I-activate ang virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Hakbang 3: I-install ang mga kinakailangang package

```bash
pip install mcp
```

## Pagpapatakbo ng Server

Ang stdio server ay gumagana nang iba kumpara sa lumang SSE server. Sa halip na magsimula ng web server, ito ay nakikipag-ugnayan sa pamamagitan ng stdin/stdout:

```bash
python server.py
```

**Mahalaga**: Ang server ay magmumukhang nakabitin - normal ito! Naghihintay ito ng mga JSON-RPC na mensahe mula sa stdin.

## Pagsubok ng Server

### Paraan 1: Gamit ang MCP Inspector (Inirerekomenda)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Ito ay gagawin ang sumusunod:
1. Ilulunsad ang iyong server bilang subprocess
2. Magbubukas ng web interface para sa pagsubok
3. Papayagan kang subukan ang lahat ng tools ng server nang interactive

### Paraan 2: Direktang JSON-RPC na pagsubok

Maaari mo ring subukan sa pamamagitan ng pagpapadala ng mga JSON-RPC na mensahe nang direkta:

1. Simulan ang server: `python server.py`
2. Magpadala ng JSON-RPC na mensahe (halimbawa):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Sasagot ang server gamit ang mga available na tools

### Mga Available na Tools

Ang server ay nagbibigay ng mga sumusunod na tools:

- **add(a, b)**: Pinagsasama ang dalawang numero
- **multiply(a, b)**: Minumultiply ang dalawang numero  
- **get_greeting(name)**: Gumagawa ng personalized na pagbati
- **get_server_info()**: Nagbibigay ng impormasyon tungkol sa server

### Pagsubok gamit ang Claude Desktop

Upang magamit ang server na ito sa Claude Desktop, idagdag ang configuration na ito sa iyong `claude_desktop_config.json`:

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

## Pangunahing Pagkakaiba sa SSE

**stdio transport (Kasalukuyan):**
- ✅ Mas simpleng setup - walang kinakailangang web server
- ✅ Mas ligtas - walang HTTP endpoints
- ✅ Komunikasyon batay sa subprocess
- ✅ JSON-RPC sa stdin/stdout
- ✅ Mas mahusay na performance

**SSE transport (Hindi na ginagamit):**
- ❌ Kinakailangan ang HTTP server setup
- ❌ Nangangailangan ng web framework (Starlette/FastAPI)
- ❌ Mas komplikadong routing at session management
- ❌ Karagdagang mga konsiderasyon sa seguridad
- ❌ Hindi na ginagamit simula MCP 2025-06-18

## Mga Tip sa Pag-debug

- Gumamit ng `stderr` para sa pag-log (huwag gumamit ng `stdout`)
- Subukan gamit ang Inspector para sa visual debugging
- Siguraduhing ang lahat ng JSON na mensahe ay newline-delimited
- Tiyaking ang server ay nagsisimula nang walang mga error

Ang solusyong ito ay sumusunod sa kasalukuyang MCP specification at nagpapakita ng pinakamahusay na mga kasanayan para sa stdio transport implementation.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.