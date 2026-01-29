# MCP stdio Server - Suluhisho la Python

> **⚠️ Muhimu**: Suluhisho hili limeboreshwa kutumia **stdio transport** kama ilivyopendekezwa na MCP Specification 2025-06-18. Njia ya awali ya SSE imeachwa.

## Muhtasari

Suluhisho hili la Python linaonyesha jinsi ya kujenga seva ya MCP kwa kutumia njia ya sasa ya stdio transport. Stdio transport ni rahisi, salama zaidi, na inatoa utendaji bora kuliko njia ya zamani ya SSE.

## Mahitaji

- Python 3.8 au toleo jipya zaidi
- Inapendekezwa usakinishe `uv` kwa usimamizi wa vifurushi, angalia [maelekezo](https://docs.astral.sh/uv/#highlights)

## Maelekezo ya Usanidi

### Hatua ya 1: Unda mazingira ya kawaida (virtual environment)

```bash
python -m venv venv
```

### Hatua ya 2: Washa mazingira ya kawaida

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Hatua ya 3: Sakinisha utegemezi

```bash
pip install mcp
```

## Kuendesha Seva

Seva ya stdio inaendeshwa tofauti na seva ya zamani ya SSE. Badala ya kuanzisha seva ya wavuti, inawasiliana kupitia stdin/stdout:

```bash
python server.py
```

**Muhimu**: Seva itaonekana kama imekwama - hili ni la kawaida! Inasubiri ujumbe wa JSON-RPC kutoka stdin.

## Kupima Seva

### Njia ya 1: Kutumia MCP Inspector (Inapendekezwa)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Hii itafanya:
1. Kuzindua seva yako kama subprocess
2. Kufungua kiolesura cha wavuti kwa ajili ya kupima
3. Kukuruhusu kupima zana zote za seva kwa njia ya maingiliano

### Njia ya 2: Kupima moja kwa moja kwa JSON-RPC

Unaweza pia kupima kwa kutuma ujumbe wa JSON-RPC moja kwa moja:

1. Anzisha seva: `python server.py`
2. Tuma ujumbe wa JSON-RPC (mfano):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Seva itajibu na zana zinazopatikana

### Zana Zinazopatikana

Seva inatoa zana hizi:

- **add(a, b)**: Jumlisha namba mbili
- **multiply(a, b)**: Zidisha namba mbili  
- **get_greeting(name)**: Tengeneza salamu ya kibinafsi
- **get_server_info()**: Pata taarifa kuhusu seva

### Kupima na Claude Desktop

Ili kutumia seva hii na Claude Desktop, ongeza usanidi huu kwenye `claude_desktop_config.json` yako:

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

## Tofauti Muhimu kutoka SSE

**stdio transport (Ya sasa):**
- ✅ Usanidi rahisi - hakuna seva ya wavuti inayohitajika
- ✅ Usalama bora - hakuna endpoints za HTTP
- ✅ Mawasiliano yanayotegemea subprocess
- ✅ JSON-RPC kupitia stdin/stdout
- ✅ Utendaji bora

**SSE transport (Imeachwa):**
- ❌ Ilihitaji usanidi wa seva ya HTTP
- ❌ Ilihitaji mfumo wa wavuti (Starlette/FastAPI)
- ❌ Usimamizi wa routing na session ulikuwa mgumu zaidi
- ❌ Masuala ya ziada ya usalama
- ❌ Sasa imeachwa katika MCP 2025-06-18

## Vidokezo vya Kutatua Hitilafu

- Tumia `stderr` kwa logging (kamwe usitumie `stdout`)
- Pima na Inspector kwa debugging ya kuona
- Hakikisha ujumbe wote wa JSON umegawanywa kwa newline
- Hakikisha seva inaanza bila hitilafu

Suluhisho hili linafuata maelezo ya sasa ya MCP na linaonyesha mbinu bora za utekelezaji wa stdio transport.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.