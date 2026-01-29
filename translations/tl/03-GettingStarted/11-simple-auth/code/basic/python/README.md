# Patakbuhin ang halimbawa

Ang halimbawang ito ay nagsisimula ng isang MCP Server na may middleware na nagche-check para sa valid na Authorization header.

## I-install ang mga dependency

```bash
pip install "mcp[cli]" 
```

## Simulan ang server

```bash
python server.py
```

patakbuhin ang client sa ibang terminal

```bash
python client.py
```

Makikita mo ang resulta na katulad nito:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

Ibig sabihin nito ay pinapayagan ang credential na ipinapadala.

Subukang baguhin ang credential sa `client.py` sa "secret-token2", pagkatapos ay makikita mo ang text na ito bilang bahagi ng response:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

Ibig sabihin nito ay na-authenticate ka (may credential ka), ngunit ito ay hindi wasto.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.