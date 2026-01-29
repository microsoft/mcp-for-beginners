# Model Context Protocol (MCP) Utekelezaji wa Python

Hifadhi hii ina utekelezaji wa Python wa Model Context Protocol (MCP), unaoonyesha jinsi ya kuunda programu ya seva na mteja zinazozungumza kwa kutumia kiwango cha MCP.

## Muhtasari

Utekelezaji wa MCP unajumuisha vipengele viwili vikuu:

1. **MCP Server (`server.py`)** - Seva inayotoa:
   - **Zana**: Kazi zinazoweza kuitwa kwa mbali
   - **Rasilimali**: Data zinazoweza kupatikana
   - **Prompts**: Violezo vya kuunda maelekezo kwa mifano ya lugha

2. **MCP Client (`client.py`)** - Programu ya mteja inayounganisha na seva na kutumia vipengele vyake

## Vipengele

Utekelezaji huu unaonyesha vipengele muhimu vya MCP:

### Zana
- `completion` - Inazalisha maandishi ya kukamilisha kutoka kwa mifano ya AI (imeigizwa)
- `add` - Kihesabu rahisi kinachoongeza nambari mbili

### Rasilimali
- `models://` - Inarudisha taarifa kuhusu mifano ya AI inayopatikana
- `greeting://{name}` - Inarudisha salamu ya kibinafsi kwa jina fulani

### Prompts
- `review_code` - Inazalisha maelekezo ya kupitia msimbo

## Usanidi

Ili kutumia utekelezaji huu wa MCP, sakinisha vifurushi vinavyohitajika:

```powershell
pip install mcp-server mcp-client
```

## Kuendesha Seva na Mteja

### Kuanzisha Seva

Endesha seva kwenye dirisha moja la terminali:

```powershell
python server.py
```

Seva pia inaweza kuendeshwa katika hali ya maendeleo kwa kutumia MCP CLI:

```powershell
mcp dev server.py
```

Au kusakinishwa kwenye Claude Desktop (ikiwa inapatikana):

```powershell
mcp install server.py
```

### Kuendesha Mteja

Endesha mteja kwenye dirisha lingine la terminali:

```powershell
python client.py
```

Hii itaunganisha na seva na kuonyesha vipengele vyote vinavyopatikana.

### Matumizi ya Mteja

Mteja (`client.py`) unaonyesha uwezo wote wa MCP:

```powershell
python client.py
```

Hii itaunganisha na seva na kutumia vipengele vyote ikijumuisha zana, rasilimali, na maelekezo. Matokeo yataonyesha:

1. Matokeo ya zana ya kihesabu (5 + 7 = 12)
2. Jibu la zana ya kukamilisha kwa "What is the meaning of life?"
3. Orodha ya mifano ya AI inayopatikana
4. Salamu ya kibinafsi kwa "MCP Explorer"
5. Kiolezo cha maelekezo ya kupitia msimbo

## Maelezo ya Utekelezaji

Seva imetekelezwa kwa kutumia API ya `FastMCP`, inayotoa viwango vya juu vya kufafanua huduma za MCP. Hapa kuna mfano rahisi wa jinsi zana zinavyofafanuliwa:

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

Mteja anatumia maktaba ya mteja ya MCP kuungana na kuitisha seva:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Jifunze Zaidi

Kwa taarifa zaidi kuhusu MCP, tembelea: https://modelcontextprotocol.io/

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.