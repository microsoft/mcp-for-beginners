# Model Context Protocol (MCP) Python Implementation

Ang repositoryong ito ay naglalaman ng Python na implementasyon ng Model Context Protocol (MCP), na nagpapakita kung paano gumawa ng parehong server at client na aplikasyon na nag-uusap gamit ang MCP standard.

## Pangkalahatang-ideya

Ang implementasyon ng MCP ay binubuo ng dalawang pangunahing bahagi:

1. **MCP Server (`server.py`)** - Isang server na naglalabas ng:
   - **Tools**: Mga function na maaaring tawagin nang malayuan
   - **Resources**: Data na maaaring kunin
   - **Prompts**: Mga template para sa paggawa ng prompts para sa mga language model

2. **MCP Client (`client.py`)** - Isang client na aplikasyon na kumokonekta sa server at ginagamit ang mga tampok nito

## Mga Tampok

Ipinapakita ng implementasyong ito ang ilang mahahalagang tampok ng MCP:

### Tools
- `completion` - Gumagawa ng mga text completion mula sa AI models (pinagkunwari)
- `add` - Simpleng calculator na nagdadagdag ng dalawang numero

### Resources
- `models://` - Nagbabalik ng impormasyon tungkol sa mga available na AI models
- `greeting://{name}` - Nagbabalik ng personalisadong pagbati para sa isang pangalan

### Prompts
- `review_code` - Gumagawa ng prompt para sa pagre-review ng code

## Pag-install

Para magamit ang implementasyong MCP na ito, i-install ang mga kinakailangang package:

```powershell
pip install mcp-server mcp-client
```

## Pagpapatakbo ng Server at Client

### Pagsisimula ng Server

Patakbuhin ang server sa isang terminal window:

```powershell
python server.py
```

Maari ring patakbuhin ang server sa development mode gamit ang MCP CLI:

```powershell
mcp dev server.py
```

O i-install ito sa Claude Desktop (kung available):

```powershell
mcp install server.py
```

### Pagpapatakbo ng Client

Patakbuhin ang client sa isa pang terminal window:

```powershell
python client.py
```

Ito ay kokonekta sa server at ipapakita ang lahat ng mga available na tampok.

### Paggamit ng Client

Ipinapakita ng client (`client.py`) ang lahat ng kakayahan ng MCP:

```powershell
python client.py
```

Ito ay kokonekta sa server at gagamitin ang lahat ng tampok kabilang ang tools, resources, at prompts. Ang output ay magpapakita ng:

1. Resulta ng calculator tool (5 + 7 = 12)
2. Tugon ng completion tool sa "What is the meaning of life?"
3. Listahan ng mga available na AI models
4. Personal na pagbati para sa "MCP Explorer"
5. Template ng prompt para sa pagre-review ng code

## Mga Detalye ng Implementasyon

Ang server ay naipatupad gamit ang `FastMCP` API, na nagbibigay ng mataas na antas ng abstraction para sa pagdedeklara ng mga MCP service. Narito ang isang pinasimpleng halimbawa kung paano dine-define ang mga tools:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

Gumagamit ang client ng MCP client library para kumonekta at tumawag sa server:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Alamin Pa

Para sa karagdagang impormasyon tungkol sa MCP, bisitahin: https://modelcontextprotocol.io/

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.