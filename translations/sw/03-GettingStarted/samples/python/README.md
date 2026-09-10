# MCP Calculator Server (Python)



Utekelezaji rahisi wa seva ya Model Context Protocol (MCP) katika Python inayotoa utendaji wa sarafu ya msingi.


## Usanidi

Sakinisha tegemezi zinazohitajika:

```bash
pip install -r requirements.txt
```

Au sakinisha MCP Python SDK moja kwa moja:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Matumizi

### Kukimbia Seva

Seva imeundwa kutumika na wateja wa MCP (kama Claude Desktop). Ili kuanzisha seva:

```bash
python mcp_calculator_server.py
```

**Kumbuka**: Ukikimbia moja kwa moja kwenye terminal, utaona makosa ya uthibitishaji ya JSON-RPC. Hii ni tabia ya kawaida - seva inasubiri ujumbe wa mteja wa MCP ulioandaliwa vizuri.

### Kujaribu Vikovu

Ili kujaribu kwamba vikovu vya sarafu vinafanya kazi vizuri:

```bash
python test_calculator.py
```

## Utatuzi wa Matatizo

### Makosa ya Kuagiza

Ukiona `ModuleNotFoundError: No module named 'mcp'`, sakinisha MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Makosa ya JSON-RPC Wakati wa Kukimbia Moja kwa Moja

Makosa kama "Invalid JSON: EOF while parsing a value" wakati unakimbia seva moja kwa moja yanatarajiwa. Seva inahitaji ujumbe wa mteja MCP, si ingizo la moja kwa moja la terminal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->