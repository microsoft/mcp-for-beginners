<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c3c28b090a54f59374677200e23a809e",
  "translation_date": "2025-11-18T19:18:28+00:00",
  "source_file": "03-GettingStarted/10-advanced/code/python/README.md",
  "language_code": "pcm"
}
-->
# Run sample

## Set up virtual environment

```sh
python -m venv venv
source ./venv/bin/activate
```

## Install dependencies

```sh
pip install "mcp[cli]"
```

## Run code

```sh
python client.py
```

You go see dis text:

```text
Available tools: ['add']
Result of add tool: meta=None content=[TextContent(type='text', text='8.0', annotations=None, meta=None)] structuredContent=None isError=False
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make e accurate, abeg sabi say automated translations fit get mistake or no correct well. Di original document for di native language na di main correct source. For important information, e good make una use professional human translation. We no go fit take responsibility for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->