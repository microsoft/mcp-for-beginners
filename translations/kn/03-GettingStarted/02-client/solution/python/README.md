# ಈ ಮಾದರಿಯನ್ನು ಚಾಲನೆಯಲ್ಲಿರಿಸಲಾಗುತ್ತಿದೆ

ನೀವು `uv` ಅನ್ನು ಸ್ಥಾಪಿಸಲು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ ಆದರೆ ಇದು ಅವಶ್ಯಕವಲ್ಲ, [ಸೂಚನೆಗಳು](https://docs.astral.sh/uv/#highlights) ನೋಡಿ

## -0- ವರ್ಚುವಲ್ ವಾತಾವರಣವನ್ನು ರಚಿಸಿ

```bash
python -m venv venv
```

## -1- ವರ್ಚುವಲ್ ವಾತಾವರಣವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ

```bash
venv\Scripts\activate
```

## -2- ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```bash
pip install "mcp[cli]"
```

## -3- ಮಾದರಿಯನ್ನು ಚಾಲನೆ ಮಾಡಿ

```bash
python client.py
```

ನೀವು ಕೆಳಗಿನಂತಹ ಔಟ್‌ಪುಟ್ ಅನ್ನು ನೋಡಬೇಕು:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
INFO Processing request of type ListToolsRequest server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
INFO Processing request of type ReadResourceRequest server.py:534
CALL TOOL
INFO Processing request of type CallToolRequest server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->