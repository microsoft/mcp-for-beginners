# MCP Calculator Server (Python)



Isang simpleng Model Context Protocol (MCP) server na ipinatupad sa Python na nagbibigay ng pangunahing functionality ng calculator.


## Pag-install

I-install ang mga kinakailangang dependencies:

```bash
pip install -r requirements.txt
```

O kaya'y i-install nang direkta ang MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Paggamit

### Pagpapatakbo ng Server

Ang server ay dinisenyo upang gamitin ng mga MCP client (tulad ng Claude Desktop). Upang simulan ang server:

```bash
python mcp_calculator_server.py
```

**Tandaan**: Kapag pinatakbo nang direkta sa terminal, makakakita ka ng JSON-RPC validation errors. Ito ay normal na pag-uugali – naghihintay ang server ng wastong format na mga mensahe mula sa MCP client.

### Pagsusuri ng mga Function

Para subukan kung gumagana nang tama ang mga function ng calculator:

```bash
python test_calculator.py
```

## Pag-ayos ng Problema

### Mga Import Error

Kung nakakita ka ng `ModuleNotFoundError: No module named 'mcp'`, i-install ang MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Mga JSON-RPC Error Kapag Pinatakbo Nang Direkta

Ang mga error tulad ng "Invalid JSON: EOF while parsing a value" kapag pinatakbo nang direkta ang server ay inaasahan. Kailangan ng server ang mga mensahe mula sa MCP client, hindi direktang input mula sa terminal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->