<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3f68294760a11dd3fdd175bd7f904a92",
  "translation_date": "2025-12-11T13:21:08+00:00",
  "source_file": "03-GettingStarted/11-simple-auth/code/basic/python/README.md",
  "language_code": "kn"
}
-->
# ಮಾದರಿ ಚಾಲನೆ

ಈ ಮಾದರಿ ಮಾನ್ಯ Authorization ಹೆಡರ್‌ಗಾಗಿ ಪರಿಶೀಲಿಸುವ ಮಧ್ಯವರ್ತಿಯನ್ನು ಹೊಂದಿರುವ MCP ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸುತ್ತದೆ.

## ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```bash
pip install "mcp[cli]" 
```

## ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸಿ

```bash
python server.py
```

ಮತ್ತೊಂದು ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಕ್ಲೈಂಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ

```bash
python client.py
```

ನೀವು ಈ ರೀತಿಯ ಫಲಿತಾಂಶವನ್ನು ನೋಡಬೇಕು:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

ಇದು ಕಳುಹಿಸಲಾಗುತ್ತಿರುವ ಪ್ರಮಾಣಪತ್ರವನ್ನು ಅನುಮತಿಸಲಾಗುತ್ತಿದೆ ಎಂದು ಅರ್ಥ.

`client.py` ನಲ್ಲಿ ಪ್ರಮಾಣಪತ್ರವನ್ನು "secret-token2" ಗೆ ಬದಲಾಯಿಸಿ, ನಂತರ ನೀವು ಪ್ರತಿಕ್ರಿಯೆಯ ಭಾಗವಾಗಿ ಈ ಪಠ್ಯವನ್ನು ನೋಡಬೇಕು:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

ಇದು ನೀವು ಪ್ರಮಾಣೀಕೃತರಾಗಿದ್ದೀರಿ (ನಿಮ್ಮ ಬಳಿ ಪ್ರಮಾಣಪತ್ರವಿತ್ತು), ಆದರೆ ಅದು ಅಮಾನ್ಯವಾಗಿತ್ತು ಎಂದು ಅರ್ಥ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->