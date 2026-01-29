# Seva ya MCP Calculator (Python)

Utekelezaji rahisi wa seva ya Model Context Protocol (MCP) kwa Python inayotoa uwezo wa msingi wa kikokotoo.

## Usakinishaji

Sakinisha utegemezi unaohitajika:

```bash
pip install -r requirements.txt
```

Au sakinisha MCP Python SDK moja kwa moja:

```bash
pip install mcp>=1.18.0
```

## Matumizi

### Kuendesha Seva

Seva imeundwa kutumiwa na wateja wa MCP (kama Claude Desktop). Ili kuanzisha seva:

```bash
python mcp_calculator_server.py
```

**Kumbuka**: Unapoendesha moja kwa moja kwenye terminal, utaona makosa ya uthibitishaji wa JSON-RPC. Hii ni tabia ya kawaida - seva inasubiri ujumbe wa mteja wa MCP ulio na muundo sahihi.

### Kupima Kazi za Kikokotoo

Ili kupima kwamba kazi za kikokotoo zinafanya kazi vizuri:

```bash
python test_calculator.py
```

## Utatuzi wa Shida

### Makosa ya Uagizaji

Ukiona `ModuleNotFoundError: No module named 'mcp'`, sakinisha MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### Makosa ya JSON-RPC Unapoendesha Moja kwa Moja

Makosa kama "Invalid JSON: EOF while parsing a value" unapoendesha seva moja kwa moja yanatarajiwa. Seva inahitaji ujumbe wa mteja wa MCP, si pembejeo ya moja kwa moja ya terminal.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.