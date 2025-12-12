<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "24531f2b6b0f7fa3839accf4dc10088a",
  "translation_date": "2025-12-11T12:56:51+00:00",
  "source_file": "03-GettingStarted/03-llm-client/solution/python/README.md",
  "language_code": "kn"
}
-->
# ಈ ಮಾದರಿಯನ್ನು ಚಾಲನೆ ಮಾಡುವುದು

ನೀವು `uv` ಅನ್ನು ಸ್ಥಾಪಿಸಲು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ ಆದರೆ ಅದು ಅಗತ್ಯವಿಲ್ಲ, [ಸೂಚನೆಗಳು](https://docs.astral.sh/uv/#highlights) ನೋಡಿ

## -0- ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿ

```bash
python -m venv venv
```

## -1- ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ

```bash
venv\Scrips\activate
```

## -2- ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```bash
pip install "mcp[cli]"
pip install openai
pip install azure-ai-inference
```

## -3- ಮಾದರಿಯನ್ನು ಚಾಲನೆ ಮಾಡಿ


```bash
python client.py
```

ನೀವು ಹೀಗೊಂದು ಔಟ್‌ಪುಟ್ ನೋಡಬೇಕು:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
Tool {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
CALLING LLM
TOOL:  {'function': {'arguments': '{"a":2,"b":20}', 'name': 'add'}, 'id': 'call_BCbyoCcMgq0jDwR8AuAF9QY3', 'type': 'function'}
[05/08/25 21:04:55] INFO     Processing request of type CallToolRequest                                                                                server.py:534
TOOLS result:  [TextContent(type='text', text='22', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->