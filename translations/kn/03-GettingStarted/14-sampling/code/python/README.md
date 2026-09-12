# ಮಾದರಿಯನ್ನು ಚಲಾಯಿಸಿ

> [!WARNING]
> ಈ ಮಾದರಿ ಹಳೆಯ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಮತ್ತು ಪರಂಪರাগত HTTP+SSE ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ಬಳಸುತ್ತದೆ. ಇದು
> MCP `2025-11-25` ಹೊಂದಾಣಿಕೆಗೆ ಸಂರಕ್ಷಿಸಲಾಗಿದೆ. ಹೊಸ ಜಾರಿಗೆ
> LLM ಪೂರೈಕೆದಾರರನ್ನು ನೇರವಾಗಿ ಕರೆ ಮಾಡಿ ಮತ್ತು ದೂರಸ್ಥ MCP ಟ್ರಾಫಿಕ್‌ಗೆ ಸ್ಟ್ರೀಮಬಲ್ HTTP ಬಳಸಿ.

## ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಸೃಷ್ಟಿಸಿ

```sh
python -m venv venv
source ./venv/bin/activate
```

## ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```sh
pip install "mcp[cli]"
```

## ಸರ್ವರ್ ಅನ್ನು ಚಲಾಯಿಸಿ

```sh
uvicorn server:app --port 8000
```

## GitHub Copilot ಮತ್ತು VS Code ಸಹಿತ ಸರ್ವರ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಿ

mcp.json ನಲ್ಲಿ ಈ ರೀತಿಯಾಗಿ ದಾಖಲೆಯನ್ನು ಸೇರಿಸಿ:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

ಸರ್ವರ್‌ನಲ್ಲಿ "start" ಕ್ಲಿಕ್ ಮಾಡುವುದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

GitHub Copilot ನಲ್ಲಿ ಕೆಳಗಿನ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಪೇಸ್ಟ್ ಮಾಡಿ:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

ಮೊದಲು ನೀವು ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಕ್ರಿಯೆಯನ್ನು ಒಪ್ಪಿಕೊಳ್ಳಬೇಕೆಂದು ಕೇಳಲ್ಪಡುತ್ತೀರಿ, ನಂತರ "create_blog" ಅನ್ನು ಚಲಾಯಿಸಲು ಉಪಕರಣವನ್ನು ಒಪ್ಪಿಕೊಳ್ಳಬೇಕೆಂದು ಕೇಳಲಾದರೆ, ನೀವು ನಂತರದಂತಹ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನೋಡಬಹುದು:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->