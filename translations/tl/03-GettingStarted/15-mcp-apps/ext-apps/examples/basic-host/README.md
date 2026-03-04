# Example: Basic Host

Isang sanggunian ng implementasyon na nagpapakita kung paano bumuo ng isang MCP host application na kumokonekta sa MCP servers at nagre-render ng tool UIs sa isang secure na sandbox.

Ang basic host na ito ay maaari ring gamitin para subukan ang MCP Apps sa panahon ng lokal na pag-develop.

## Key Files

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI host na may pagpili ng tool, pag-input ng parametro, at pamamahala ng iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Panlabas na iframe proxy na may seguridad na pag-validate at bidirectional na pagpasa ng mensahe
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Pangunahing lohika: koneksyon sa server, pagtawag ng tool, at setup ng AppBridge

## Getting Started

```bash
npm install
npm run start
# Buksan ang http://localhost:8080
```

Bilang default, susubukan ng host application na kumonekta sa isang MCP server sa `http://localhost:3001/mcp`. Maaari mong i-configure ang pag-uugaling ito sa pamamagitan ng pagtatakda ng `SERVERS` environment variable gamit ang isang JSON array ng mga URL ng server:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architecture

Gumagamit ang halimbawa na ito ng double-iframe sandbox pattern para sa secure na UI isolation:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Bakit dalawang iframe?**

- Ang panlabas na iframe ay tumatakbo sa isang hiwalay na origin (port 8081) na pumipigil sa direktang pag-access sa host
- Ang panloob na iframe ay tumatanggap ng HTML gamit ang `srcdoc` at nililimitahan ng mga sandbox attribute
- Dumadaloy ang mga mensahe sa panlabas na iframe na nagva-validate at nagpapasa ng mga ito nang bidirectionally

Tinitiyak ng arhitekturang ito na kahit na ang code ng tool UI ay malisyoso, hindi nito maa-access ang DOM, cookies, o JavaScript context ng host application.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pahayag ng Pagsisi**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kaming maging tumpak, pakatandaang ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->