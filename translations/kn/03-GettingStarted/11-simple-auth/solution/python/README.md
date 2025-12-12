<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fd28e690667b8ad84bb153cb025cfd73",
  "translation_date": "2025-12-11T13:22:47+00:00",
  "source_file": "03-GettingStarted/11-simple-auth/solution/python/README.md",
  "language_code": "kn"
}
-->
# ಮಾದರಿ ಚಾಲನೆ

## ಪರಿಸರವನ್ನು ರಚಿಸಿ

```sh
python -m venv venv
source ./venv/bin/activate
```

## ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## ಟೋಕನ್ ರಚಿಸಿ

ಗ್ರಾಹಕ ಸರ್ವರ್ ಜೊತೆ ಮಾತನಾಡಲು ಬಳಸುವ ಟೋಕನ್ ಅನ್ನು ನೀವು ರಚಿಸಬೇಕಾಗುತ್ತದೆ.

ಕರೆ ಮಾಡಿ:

```sh
python util.py
```

## ಕೋಡ್ ಚಾಲನೆ

ಕೋಡ್ ಅನ್ನು ಈ ಕೆಳಗಿನಂತೆ ಚಾಲನೆ ಮಾಡಿ:

```sh
python server.py
```

ಬೇರೆ ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ, ಟೈಪ್ ಮಾಡಿ:

```sh
python client.py
```

ಸರ್ವರ್ ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ, ನೀವು ಹೀಗೆ ಏನಾದರೂ ಕಾಣಬಹುದು:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

ಗ್ರಾಹಕ ವಿಂಡೋದಲ್ಲಿ, ನೀವು ಹೀಗೆ ಪಠ್ಯವನ್ನು ಕಾಣಬೇಕು:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

ಇದು ಎಲ್ಲವೂ ಸರಿಯಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತಿದೆ ಎಂದು ಅರ್ಥ.

### ಮಾಹಿತಿಯನ್ನು ಬದಲಿಸಿ, ವಿಫಲವಾಗುವುದನ್ನು ನೋಡಿ

*server.py* ನಲ್ಲಿ ಈ ಕೋಡ್ ಅನ್ನು ಹುಡುಕಿ:

```python
 if not has_scope(has_header, "Admin.Write"):
```

ಇದನ್ನು "User.Write" ಎಂದು ಬದಲಿಸಿ. ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಟೋಕನ್‌ಗೆ ಆ ಅನುಮತಿ ಮಟ್ಟವಿಲ್ಲ, ಆದ್ದರಿಂದ ನೀವು ಸರ್ವರ್ ಅನ್ನು ಮರುಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಗ್ರಾಹಕವನ್ನು ಮತ್ತೆ ಚಾಲನೆ ಮಾಡಿದರೆ, ಸರ್ವರ್ ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಕೆಳಗಿನಂತೆಯೇ ದೋಷವನ್ನು ನೀವು ಕಾಣಬಹುದು:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

ನೀವು ನಿಮ್ಮ ಸರ್ವರ್ ಕೋಡ್ ಅನ್ನು ಹಿಂದಕ್ಕೆ ಬದಲಾಯಿಸಬಹುದು ಅಥವಾ ಈ ಹೆಚ್ಚುವರಿ ವ್ಯಾಪ್ತಿಯನ್ನು ಹೊಂದಿರುವ ಹೊಸ ಟೋಕನ್ ಅನ್ನು ರಚಿಸಬಹುದು, ನಿಮ್ಮ ಆಯ್ಕೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->