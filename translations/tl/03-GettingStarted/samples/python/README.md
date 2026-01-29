# MCP Calculator Server (Python)

Isang simpleng implementasyon ng Model Context Protocol (MCP) server sa Python na nagbibigay ng pangunahing functionality ng calculator.

## Pag-install

I-install ang mga kinakailangang dependencies:

```bash
pip install -r requirements.txt
```

O direktang i-install ang MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

## Paggamit

### Pagpapatakbo ng Server

Ang server ay idinisenyo para magamit ng mga MCP client (tulad ng Claude Desktop). Para simulan ang server:

```bash
python mcp_calculator_server.py
```

**Tandaan**: Kapag pinatakbo nang direkta sa terminal, makakakita ka ng mga JSON-RPC validation error. Normal ito - ang server ay naghihintay ng maayos na formatted na mga mensahe mula sa MCP client.

### Pagsubok sa mga Function

Para masubukan kung gumagana nang tama ang mga calculator function:

```bash
python test_calculator.py
```

## Pag-aayos ng Problema

### Mga Error sa Import

Kung makakita ka ng `ModuleNotFoundError: No module named 'mcp'`, i-install ang MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### Mga JSON-RPC Error Kapag Pinatakbo nang Direkta

Ang mga error tulad ng "Invalid JSON: EOF while parsing a value" kapag pinatakbo ang server nang direkta ay inaasahan. Ang server ay nangangailangan ng mga mensahe mula sa MCP client, hindi direktang input mula sa terminal.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.