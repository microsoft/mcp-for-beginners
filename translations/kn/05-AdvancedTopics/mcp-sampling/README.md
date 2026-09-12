> [!WARNING]
> MCP `2026-07-28` ನಲ್ಲಿ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಅನ್ನು ನಿಷೇಧಿಸಲಾಗಿದೆ. ಈ ಪಾಠವು
> ಹಳೆಯ ಕಾರ್ಯಗತಿಯಿಗಾಗಿ ಉಳಿಸಲಾಗಿದೆ. ಹೊಸ ಸರ್ವರ್‌ಗಳು ನೇರವಾಗಿ LLM
> ಒದಗಿಸುವ API ಜೊತೆಗೆ ಇಂಟಿಗ್ರೇಟ್ ಮಾಡಬೇಕು.

# ಮಾದರಿ ಕಾಂಟೆಕ್ಸ್ಟ್ ಪ್ರೋಟೋಕಾಲ್ ನಲ್ಲಿ ಸ್ಯಾಂಪ್ಲಿಂಗ್

> ಹೊಂದಾಣಿಕೆಗೆ `2026-07-28` ವಿವರಣೆದಲ್ಲಿ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಉಳಿದಿದೆ ಮತ್ತು
> ಜುಲೈ 28, 2027 ನಂತರ ಬಿಡುಗಡೆ ಆಗುವ ಮೊದಲ ಮರುಪರಿಶೀಲನೆಯಲ್ಲಿ ತೆಗೆದುಹಾಕಬಹುದು.
> ಈ ಪಾಠದ ಉದಾಹರಣೆಗಳು `2025-11-25` ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವ SDK API ಗಳನ್ನು ಬಳಸಬಹುದು.
> [MCPನಲ್ಲಿ ಏನು ಬದಲಾಗಿದೆ: 2026-07-28 ಸ್ಪೆಸಿಫಿಕೇಶನ್](../../01-CoreConcepts/mcp-2026-07-28.md) ನೋಡಿ.

ಹಳೆಯ MCP ಕಾರ್ಯಗತಿಗಳಲ್ಲಿ, ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಮೂಲಕ ಸರ್ವರ್‌ಗಳು ಕ್ಲೈಂಟ್ ಮೂಲಕ LLM ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಯನ್ನು ವಿನಂತಿಸಬಹುದು.
ಈ ಪಾಠವು ಹೊಂದಾಣಿಕೆಯ ಮತ್ತು seldom-ಆವರ್ತನೆ ಕೆಲಸಕ್ಕಾಗಿ ಆ ನಿಷೇಧಿತ ಪ್ರೋಟೋಕಾಲ್
ಪ್ರಸ್ಥಾವನೆಯನ್ನು ವಿವರಿಸುತ್ತದೆ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ ನಾವು MCP ವಿನಂತಿಗಳಲ್ಲಿ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳನ್ನು ಹೇಗೆ ಸಂರಚಿಸುವುದು ಮತ್ತು ಸ್ಯಾಂಪ್ಲಿಂಗ್ ನೆಲೆಯಲ್ಲಿ ಪ್ರೋಟೋಕಾಲ್ ಯಂತ್ರಗಳನ್ನು ಹೇಗೆ ಅರ್ಥಮಾಡಿರುವುದು ಸ್ಥಾನಗೊಳ್ಳುತ್ತದೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪಾಠದ ಕೊನಿಗೆ, ನೀವು:

- MCP ಯಲ್ಲಿ ಲಭ್ಯವಿರುವ ಮುಖ್ಯ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಬೇಕು.
- ವಿಭಿನ್ನ ಬಳಕೆಗಳಿಗಾಗಿ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳನ್ನು ಸಂರಚಿಸಬೇಕು.
- ಪುನರಾವರ್ತಿಸಲ್ಪಡಬಹುದಾದ ಫಲಿತಾಂಶಗಳಿಗಾಗಿ ನಿರ್ಧಾರಾತ್ಮಕ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಬೇಕು.
- ಸಂಧರ್ಭ ಮತ್ತು ಬಳಕೆದಾರ ಆಯ್ಕೆಗಳ ಆಧಾರದ ಮೇಲೆ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳನ್ನು ಗತಿಯಲ್ಲಿಡಬೇಕು.
- ವಿವಿಧ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ ಮಾದರಿಯ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಸುಧಾರಿಸಲು ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಕಾರ್ಯನೀತಿಗಳನ್ನು ಜಾರಿಗೊಳಿಸು.
- MCP ಯ ಕ್ಲೈಂಟ್-ಸರ್ವರ್ ಪ್ರವಾಹದಲ್ಲಿ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ.

## MCP ನಲ್ಲಿ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ

MCP ನಲ್ಲಿ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪ್ರವಾಹವು ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸುತ್ತದೆ:

1. ಸರ್ವರ್ `sampling/createMessage` ವಿನಂತಿಯನ್ನು ಕ್ಲೈಂಟ್ ಗೆ ಕಳುಹಿಸುತ್ತದೆ
2. ಕ್ಲೈಂಟ್ ವಿನಂತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ ಅದನ್ನು ಬದಲಾಯಿಸಬಹುದು
3. ಕ್ಲೈಂಟ್ LLM ಇಂದ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಮಾಡುತ್ತದೆ
4. ಕ್ಲೈಂಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಯನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ
5. ಕ್ಲೈಂಟ್ ಫಲಿತಾಂಶವನ್ನು ಸರ್ವರ್ ಗೆ ಹಿಂತಿರುಗಿಸುತ್ತದೆ

ಈ ಮಾನವ-ನಡೆತೋಡೆ ವಿನ್ಯಾಸವು ಬಳಕೆದಾರರಿಗೆ LLM ನೋಡಿರುವುದು ಮತ್ತು ತಯಾರಿಸುವುದರ ಮೇಲೆ ನಿಯಂತ್ರಣವನ್ನು ನೀಡುತ್ತದೆ.

## ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳ ಅವಲೋಕನ

MCP ಗುರಿಪಡಿಸಿರುವ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳು ಕಡತ ವಿನಂತಿಗಳಿಗೆ ಸಂರಚಿಸಲ್ಪಡಬಹುದು:

| ಪರಿಮಾಣ | ವಿವರಣೆ | ಸಾಮಾನ್ಯ ಮಿತಿಗಳು |
|-----------|-------------|---------------|
| `temperature` | ಟೋಕನ್ ಆಯ್ಕೆಯಲ್ಲಿ ಅತಿಲೋದ್ಯಮ ನಿಯಂತ್ರಣ | 0.0 - 1.0 |
| `maxTokens` | ජනನಕ್ಕೆ ಗರಿಷ್ಠ ಟೋಕನಗಳ ಸಂಖ್ಯೆ | ಪೂರ್ಣಾಂಕ ಮೌಲ್ಯ |
| `stopSequences` | ವಿಶೇಷ ಸರಣಿಗಳು ಜನನ ನಿಲ್ಲಿಸಲು | ಅಕ್ಷರ ಸರಣಿಗಳ ಗುರೂಪ |
| `metadata` | ಹೆಚ್ಚುವರಿ ಒದಗಿಸುವವರ ವಿಶಿಷ್ಟ ಪರಿಮಾಣಗಳು | JSON ವಸ್ತು |

ಅನೇಕ LLM ಒದಗಿಸುವವರು `metadata` ಕ್ಷೇತ್ರದಿಂದ ಹೆಚ್ಚುವರಿ ಪರಿಮಾಣಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತಾರೆ, ಉದಾಹರಣೆಗೆ:

| ಸಾಮಾನ್ಯ ವಿಸ್ತರಣೆ ಪರಿಮಾಣ | ವಿವರಣೆ | ಸಾಮಾನ್ಯ ಮಿತಿಗಳು |
|-----------|-------------|---------------|
| `top_p` | ನ್ಯೂಕ್ಲಿಯಸ್ ಸ್ಯಾಂಪ್ಲಿಂಗ್ - ಟೋಕನ್ಗಳನ್ನು ಮೇಲ್ಮಟ್ಟದ ಸಾಂದರ್ಭಿಕ ಸಾಧ್ಯತೆಗಳಿಗೆ ಮಿತಿಮಾಡುತ್ತದೆ | 0.0 - 1.0 |
| `top_k` | ಟೋಕನ್ಗಳ ಆಯ್ಕೆಯನ್ನು ಟಾಪ್ K ಆಯ್ಕೆಗೆ ಮಿತಿಗೊಳಿಸುತ್ತದೆ | 1 - 100 |
| `presence_penalty` | ಈಗಾಗಲೇ ಬದಿಯಲ್ಲಿ ಇರುವುದು ಆಧರಿಸಿ ಪೆನಲ್ಟಿ ನೀಡುತ್ತದೆ | -2.0 - 2.0 |
| `frequency_penalty` | ಟೋಕನಗಳ ಬಹುಮಾರ್ಗವನ್ನು ಆಧರಿಸಿ ಪೆನಲ್ಟಿ ನೀಡುತ್ತದೆ | -2.0 - 2.0 |
| `seed` | ಪುನರಾವರ್ತಿಸಬಹುದಾದ ಫಲಿತಾಂಶಕ್ಕೆ ವಿಶಿಷ್ಟ ಯಾದೃಚ್ಛಿಕ ಬೀಜ | ಪೂರ್ಣಾಂಕ ಮೌಲ್ಯ |

## ಉದಾಹರಣೆ ವಿನಂತಿ ಸ್ವರೂಪ

ಇಲ್ಲಿದೆ MCP ನಲ್ಲಿ ಕ್ಲೈಂಟ್ ಇಂದ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ವಿನಂತಿಯ ಉದಾಹರಣೆ:

```json
{
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "What files are in the current directory?"
        }
      }
    ],
    "systemPrompt": "You are a helpful file system assistant.",
    "includeContext": "thisServer",
    "maxTokens": 100,
    "temperature": 0.7
  }
}
```

## ಪ್ರತಿಕ್ರಿಯೆ ಸ್ವರೂಪ

ಕ್ಲೈಂಟ್ ಪೂರ್ಣಗೊಳಿಸಿದ ಫಲಿತಾಂಶವನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ:

```json
{
  "model": "string",  // Name of the model used
  "stopReason": "endTurn" | "stopSequence" | "maxTokens" | "string",
  "role": "assistant",
  "content": {
    "type": "text",
    "text": "string"
  }
}
```

## ಮಾನವನ ನಿಯಂತ್ರಣಗಳು

MCP ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಮಾನವ ತನ್ನಾಗುವಿಕೆಯೊಂದಿಗೆ ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ:

- **ಪ್ರಾಂಪ್ಟ್‌ಗಳಿಗಾಗಿ**:
  - ಕ್ಲೈಂಟ್ ಬಳಕೆದಾರರಿಗೆ ಸಲಹೆಯ ಪ್ರಾಂಪ್ಟ್ ತೋರಿಸಬೇಕು
  - ಬಳಕೆದಾರರು ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಬದಲಾಯಿಸಲು ಅಥವಾ ನಿರಾಕರಿಸಲು ಸಾಧ್ಯವಾಗಬೇಕು
  - ವ್ಯವಸ್ಥೆ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಅಡಚಣೆಯಲ್ಲಿಡಬಹುದು ಅಥವಾ ಬದಲಾಯಿಸಬಹುದು
  - ಸಂಧರ್ಭವನ್ನು ಕ್ಲೈಂಟ್ ನಿಯಂತ್ರಿಸುತ್ತದೆ

- **ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಾಗಿ**:
  - ಕ್ಲೈಂಟ್ ಬಳಕೆದಾರರಿಗೆ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಯನ್ನು ತೋರಿಸಬೇಕು
  - ಬಳಕೆದಾರರು ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಯನ್ನು ಬದಲಾಯಿಸಲು ಅಥವಾ ನಿರಾಕರಿಸಲು ಸಾಧ್ಯವಾಗಬೇಕು
  - ಕ್ಲೈಂಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗೆ ಫಿಲ್ಟರ್ ಅಥವಾ ಬದಲಾವಣೆ ಮಾಡಬಹುದು
  - ಬಳಕೆದಾರರು ಬಳಸುವ ಮಾದರಿಯನ್ನು ನಿಯಂತ್ರಿಸುತ್ತಾರೆ

ಈ ತತ್ವಗಳನ್ನು ಗಮನದಲ್ಲಿಟ್ಟುಕೊಂಡು, ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಅನ್ನು ವಿವಿಧ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಭಾಷೆಗಳಲ್ಲಿ ಹೇಗೆ ಅನುಷ್ಠಾನಗೊಳಿಸುವುದನ್ನು ನೋಡಿ, ಪ್ರಧಾನವಾಗಿ LLM ಒದಗಿಸುವವರ ಮೂಲಕ ಸಾಮಾನ್ಯವಾಗಿ ಬೆಂಬಲಿಸಲ್ಪಡುವ ಪರಿಮಾಣಗಳಿಗೆ ಕೇಂದ್ರೀಕರಿಸಿ.

## ಭದ್ರತಾ ಪರಿಗಣನೆಗಳು

MCP ನಲ್ಲಿ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಅನುಷ್ಠಾನಗೊಳಿಸುವಾಗ, ಈ ಭದ್ರತಾ ಅತ್ಯುತ್ತಮ ಅಭ್ಯಾಸಗಳನ್ನು ಪರಿಗಣಿಸಿ:

- **ಎಲ್ಲಾ ಸಂದೇಶ ವಿಷಯವನ್ನು ಪರಿಶೀಲಿಸಿ** ಮತ್ತು ನಂತರ ಕ್ಲೈಂಟ್ ಗೆ ಕಳುಹಿಸಿ
- **ಸೂಕ್ಷ್ಮ ಮಾಹಿತಿಯನ್ನು ಶುದ್ಧಗೊಳಿಸಿ** ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಮತ್ತು ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳಿಂದ
- **ಪ್ರಮಾಣಿತ ಹಂತಗಳಲ್ಲಿ ನಿರೋಧವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ** ದುರುಪಯೋಗವನ್ನು ತಡೆಯಲು
- **ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಬಳಕೆಯನ್ನು ಕಣ್ಣು ಹಾಕಿ** ಅಸಾಮಾನ್ಯ ಮಾದರಿಗಳಿಗೆ
- **ಮಾರ್ಗದಲ್ಲಿ ಡೇಟಾಗೆ ಎನ್‌ಕ್ರಿಪ್ಷನ್ ಮಾಡಿ** ಭದ್ರ ಪ್ರೋಟೋಕಾಲ್ ಬಳಸಿ
- **ಬಳಕೆದಾರ ಡೇಟಾ ಗೌಪ್ಯತೆಯನ್ನು ನಿಯಮಾವಳಿಗಳ ಪ್ರಕಾರ ನಿರ್ವಹಿಸಿ**
- **ಸ pieza ಉತ್ತರವಿನಂತಿಲ್ಲsampling ವಿನಂತಿಗಳಿಗೆ ಪರಿಶೀಲನೆ ಮಾಡಿ** ಪಾಲನೆ ಮತ್ತು ಭದ್ರತೆಗಾಗಿ
- **ಖರ್ಚಿನ ಬಾಹ್ಯತೆ ನಿಯಂತ್ರಿಸಿ** ಸೂಕ್ತ ಮಿತಿಗಳೊಂದಿಗೆ
- **ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪ್ರಶ್ನೆಗಳಿಗೆ ಕಾಲಹರಣಗಳನ್ನೂ ಹೇರಿಕೊಳ್ಳಿ**
- **ಮಾದರಿ ದೋಷಗಳನ್ನು ಮೃದುವಾಗಿ ನಿರ್ವಹಿಸಿ** ಸೂಕ್ತ ಮುಕ್ತಾಯಗಳೊಂದಿಗೆ

ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳು ಭಾಷಾ ಮಾದರಿಗಳ ವರ್ತನೆಯನ್ನು ಸೂಕ್ಷ್ಮವಾಗಿ ಬದಲಿಸಿ ನಿರ್ಧಾರಾತ್ಮಕ ಮತ್ತು ಸೃಜನಶೀಲ ಉತ್ಪನ್ನಗಳ ನಡುವೆ ಇಚ್ಛಿತ ಸಮತೋಲನವನ್ನು ತಲುಪಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ.

ಈ ಪರಿಮಾಣಗಳನ್ನು ವಿಭಿನ್ನ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಭಾಷೆಗಳಲ್ಲಿ ಹೇಗೆ ಸಂರಚಿಸಬೇಕೆಂಬುದನ್ನು ನೋಡೋಣ.

# [.NET](#tab-dotnet)

```csharp
// .NET Example: Configuring sampling parameters in MCP
public class SamplingExample
{
    public async Task RunWithSamplingAsync()
    {
        // Create MCP client with sampling configuration
        var client = new McpClient("https://mcp-server-url.com");
        
        // Create request with specific sampling parameters
        var request = new McpRequest
        {
            Prompt = "Generate creative ideas for a mobile app",
            SamplingParameters = new SamplingParameters
            {
                Temperature = 0.8f,     // Higher temperature for more creative outputs
                TopP = 0.95f,           // Nucleus sampling parameter
                TopK = 40,              // Limit token selection to top K options
                FrequencyPenalty = 0.5f, // Reduce repetition
                PresencePenalty = 0.2f   // Encourage diversity
            },
            AllowedTools = new[] { "ideaGenerator", "marketAnalyzer" }
        };
        
        // Send request using specific sampling configuration
        var response = await client.SendRequestAsync(request);
        
        // Output results
        Console.WriteLine($"Generated with Temperature={request.SamplingParameters.Temperature}:");
        Console.WriteLine(response.GeneratedText);
    }
}
```

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ನಿರ್ದಿಷ್ಟ ಸರ್ವರ್ URL ಯೊಂದಿಗೆ MCP ಕ್ಲೈಂಟ್ ರಚಿಸಲಾಗಿದೆ.
- `temperature`, `top_p`, ಮತ್ತು `top_k` ಮುಂತಾದ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳೊಂದಿಗೆ ವಿನಂತಿಯನ್ನು ಸಂರಚಿಸಲಾಗಿದೆ.
- ವಿನಂತಿಯನ್ನು ಕಳುಹಿಸಿ ಉತ್ಪನ್ನ ಪಠ್ಯವನ್ನು ಔಟ್ ಪುಟ್ ಮಾಡಲಾಗಿದೆ.
- ಬಳಸದಾಗಿದೆ:
    - `allowedTools` ಮೂಲಕ ಉತ್ಪಾದನೆಗೆ ಸಹಾಯವಾಗುವ `ideaGenerator` ಮತ್ತು `marketAnalyzer` ಸಾಧನಗಳನ್ನು ಆಧರಿಸಲಾಗಿದೆ.
    - `frequencyPenalty` ಮತ್ತು `presencePenalty` ಅನ್ನು ಪುನರಾವರ್ತನೆ ಮತ್ತು ವೈವಿಧ್ಯತೆ ನಿಯಂತ್ರಣಕ್ಕೆ.
    - ಹೆಚ್ಚು ಸೃಜನಶೀಲ ಪ್ರತಿಕ್ರಿಯೆಗಳಿಗೆ randomness ನಿಯಂತ್ರಣಕ್ಕೆ `temperature`.
    - ಉನ್ನತ ಸಾಂದರ್ಭಿಕ ಸಾಧ್ಯತೆಗಳಿಗೆ ಟೋಕನ್ಗಳ ಆಯ್ಕೆಯನ್ನು ಮಿತಿಗೊಳಿಸಲು `top_p`.
    - ಸಾಂಕೇತಿಕ ಉತ್ತರಗಳ ನಿರ್ಮಾಣಕ್ಕೆ ಟಾಪ್ K ಟೋಕನ್ಗಳನ್ನು ನಿಯಂತ್ರಿಸುವ `top_k`.
    - ಪುನರಾವರ್ತನ ಮತ್ತು ವೈವಿಧ್ಯತೆ ಕನಿಷ್ಠಗೊಳಿಸಲು `frequencyPenalty` ಮತ್ತು `presencePenalty`.

# [JavaScript](#tab/javascript)

```javascript
// ಜಾವಾಸ್ಕ್ರಿಪ್ಟ್ ಉದಾಹರಣೆ: ತಾಪಮಾನ ಮತ್ತು ಟಾಪ್-পি ಶ್ಯಾಂಪ್ಲಿಂಗ್ ಸಂರಚನೆ
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // MCP ಕ್ಲೈಂಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // ವಿಭಿನ್ನ ಶ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳೊಂದಿಗೆ ವಿನಂತಿಯನ್ನು ಸಂರಚಿಸಿ
  const creativeSampling = {
    temperature: 0.9,    // ಹೆಚ್ಚು ತಾಪಮಾನ = ಹೆಚ್ಚು ಯಾದೃಚ್ಛಿಕತೆ/ಸೃಜನಶೀಲತೆ
    topP: 0.92,          // ಟಾಪ್ 92% ಸಂಭವನೀಯತೆ ಮಾಸ್ ಹೊಂದಿರುವ ಟೋಕನ್‌ಗಳನ್ನು ಪರಿಗಣಿಸಿ
    frequencyPenalty: 0.6, // ಟೋಕನ್ ಸರಣಿಗಳ ಆಹರಿಕೆ ಕಡಿಮೆ ಮಾಡಿ
    presencePenalty: 0.4   // ಇದುವರೆಗೆ ಪಠ್ಯದಲ್ಲಿ ಕಂಡುಬಂದ ಟೋಕನ್‌ಗಳಿಗೆ ದಂಡ ವಿಧಿಸಿ
  };
  
  const factualSampling = {
    temperature: 0.2,    // ಕಡಿಮೆ ತಾಪಮಾನ = ಹೆಚ್ಚು ನಿರ್ದಿಷ್ಟ/ತಥ್ಯಾತ್ಮಕ
    topP: 0.85,          // ಸ್ವಲ್ಪ ಹೆಚ್ಚು ಕೇಂದ್ರೀಕೃತ ಟೋಕನ್ ಆಯ್ಕೆ
    frequencyPenalty: 0.2, // ಕನಿಷ್ಠ ಆಹರಿಕೆ ದಂಡ
    presencePenalty: 0.1   // ಕನಿಷ್ಠ ಉಪಸ್ಥಿತಿಯ ದಂಡ
  };
  
  try {
    // ವಿಭಿನ್ನ ಶ್ಯಾಂಪ್ಲಿಂಗ್ ಸಂರಚನೆಗಳೊಂದಿಗೆ ಎರಡು ವಿನಂತಿಗಳನ್ನು ಕಳುಹಿಸಿ
    const creativeResponse = await client.sendPrompt(
      "Generate innovative ideas for sustainable urban transportation",
      {
        allowedTools: ['ideaGenerator', 'environmentalImpactTool'],
        ...creativeSampling
      }
    );
    
    const factualResponse = await client.sendPrompt(
      "Explain how electric vehicles impact carbon emissions",
      {
        allowedTools: ['factChecker', 'dataAnalysisTool'],
        ...factualSampling
      }
    );
    
    console.log('Creative Response (temperature=0.9):');
    console.log(creativeResponse.generatedText);
    
    console.log('\nFactual Response (temperature=0.2):');
    console.log(factualResponse.generatedText);
    
  } catch (error) {
    console.error('Error demonstrating sampling:', error);
  }
}

demonstrateSampling();
```

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸರ್ವರ್ URL ಮತ್ತು API ಕೀ ಅಳವಡಿಸಿದ MCP ಕ್ಲೈಂಟ್ ಪ್ರಾರಂಭಿಸಲಾಗಿದೆ.
- ಸೃಜನಾತ್ಮಕ ಕಾರ್ಯಗಳಿಗೆ ಮತ್ತು ವಾಸ್ತವಿಕ ಕಾರ್ಯಗಳಿಗೆ ಎರಡು ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳನ್ನು ಸಂರಚಿಸಲಾಗಿದೆ.
- ಈ ಸಂರಚನೆಗಳೊಂದಿಗೆ ವಿನಂತಿಗಳನ್ನು ಕಳುಹಿಸಿ ಮಾದರಿಯು ನಿಗದಿತ ಸಾಧನಗಳನ್ನು ಬಳಸಲು ಅವಕಾಶ ನೀಡಲಾಗಿದೆ.
- ವಿವಿಧ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳ ಪರಿಣಾಮವನ್ನು ತೋರಿಸಲು ಉತ್ಪಾದಿತ ಉತ್ತರಗಳನ್ನು ಮುದ್ರಿಸಲಾಗಿದೆ.
- `allowedTools` ಮೂಲಕ, ಸೃಜನಾತ್ಮಕ ಕಾರ್ಯಗಳಿಗೆ `ideaGenerator` ಮತ್ತು `environmentalImpactTool`, ವಾಸ್ತವಿಕ ಕಾರ್ಯಗಳಿಗೆ `factChecker` ಮತ್ತು `dataAnalysisTool` ಸಾಧನಗಳನ್ನು ಬಳಕೆ ಮಾಡಲು ಅವಕಾಶ ನೀಡಲಾಗಿದೆ.
- randomness ನಿಯಂತ್ರಣಕ್ಕೆ `temperature`.
- ಉನ್ನತ ಸಾಂದರ್ಭಿಕ ಸಾಧ್ಯತೆಗಳಿಗೆ ಟೋಕನ್ಗಳ ಆಯ್ಕೆಯನ್ನು ಮಿತಿಗೊಳಿಸಲು `top_p`.
- ಪುನರಾವರ್ತನೆ ಕಡಿಮೆ ಮಾಡಲು ಮತ್ತು ವೈವಿಧ್ಯತೆ ಹೆಚ್ಚಿಸಲು `frequencyPenalty` ಮತ್ತು `presencePenalty`.
- ಸಾಂದರ್ಭಿಕ ತಾಲೀಮು ಸಹಿತ ಟಾಪ್ K ಟೋಕನ್ಗಳನ್ನು ನಿಯಂತ್ರಿಸಲು `top_k`.

---

## ನಿರ್ಧಾರಾತ್ಮಕ ಸ್ಯಾಂಪ್ಲಿಂಗ್

ನಿರಂತರ ಉತ್ಪನ್ನಗಳನ್ನು ಬೇಕಾಗಿರುವ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ, ನಿರ್ಧಾರಾತ್ಮಕ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪುನರಾವರ್ತಿಸಲ್ಪಡಬಹುದಾದ ಫಲಿತಾಂಶವನ್ನು ಒದಗಿಸುತ್ತದೆ. ಇದು ವಿಶೇಷ ಯಾದೃಚ್ಛಿಕ ಬೀಜ ಮತ್ತು ಶೂನ್ಯ ತಾಪಮಾನವನ್ನು ಬಳಸಿ ಮಾಡುತ್ತದೆ.

ವಿವಿಧ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಭಾಷೆಗಳಲ್ಲಿ ನಿರ್ಧಾರಾತ್ಮಕ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಯಾವುದೇ ವಿವರಿಸಲು ಕೆಳಗಿನ ಉದಾಹರಣೆ ಅನುಷ್ಠಾನ ನೀಡಲಾಗಿದೆ.

# [Java](#tab/java)

```java
// ಜಾವಾ ಉದಾಹರಣೆ: ಸ್ಥಿರ ಬೀಜದೊಂದಿಗೆ ನಿರ್ಧಾರಾತ್ಮಕ ಪ್ರತಿಕ್ರಿಯೆಗಳು
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // ನಿರ್ಧಾರಾತ್ಮಕ ಫಲಿತಾಂಶಗಳಿಗಾಗಿ ಸ್ಥಿರ ಬೀಜವನ್ನು ಬಳಸುವುದು
        
        // ಸ್ಥಿರ ಬೀಜದೊಂದಿಗೆ ಮೊದಲ ವಿನಂತಿ
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // ಗರಿಷ್ಠ ನಿರ್ಧಾರಾತ್ಮಕತೆಗೆ ಶೂನ್ಯ ತಾಪಮಾನ
            .build();
            
        // ಒಂದೇ ಬೀಜದೊಂದಿಗೆ ಎರಡನೇ ವಿನಂತಿ
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // ಇಬ್ಬರು ವಿನಂತಿಗಳನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // ಪ್ರತಿಕ್ರಿಯೆಗಳು ಒಂದೇ ಬೀಜ ಮತ್ತು ತಾಪಮಾನ=0 ಕಾರಣಕ್ಕೆ ಸಮಾನವಾಗಿರಬೇಕು
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ನಿರ್ದಿಷ್ಟ ಸರ್ವರ್ URL ಹೊಂದಿದ MCP ಕ್ಲೈಂಟ್ ರಚಿಸಲಾಗಿದೆ.
- ಒಂದೇ ಪ್ರಾಂಪ್ಟ್, ನಿಗದಿತ ಬೀಜ ಮತ್ತು ಶೂನ್ಯ ತಾಪಮಾನದ ಎರಡು ವಿನಂತಿಗಳನ್ನು ಸಂರಚಿಸಲಾಗಿದೆ.
- ಇಬ್ಬರೂ ವಿನಂತಿಗಳನ್ನು ಕಳುಹಿಸಿ ಉತ್ಪಾದಿತ ಪಠ್ಯವನ್ನು ಔಟ್ ಪುಟ್ ಮಾಡಲಾಗಿದೆ.
- ಮೊದಲ ವಿನಂತಿಯ ಉತ್ತರಗಳು ನಿರ್ಧಾರಾತ್ಮಕ ಸ್ವಭಾವದಿಂದ ಒಂದು ಹಾಗೆಯೇ ಇದ್ದವು (ಒಂದೇ ಬೀಜ ಮತ್ತು ತಾಪಮಾನ).
- `setSeed` ಬಳಸಿ ನಿಗದಿತ ಯಾದೃಚ್ಛಿಕ ಬೀಜವನ್ನು ನಿರ್ಧರಿಸಲಾಗಿದೆ, ಇದರಿಂದ ಮಾದರಿ ಪ್ರತೀ ಬಾರಿ ಒಂದೇ ಇನ್‌ಪುಟ್‌ಗೆ ಒಂದೇ ಫಲಿತಾಂಶ ನೀಡುತ್ತದೆ.
- `temperature` ಅನ್ನು ಶೂನ್ಯಕ್ಕೆ ಸೆಟ್ ಮಾಡಿ ಹೆಚ್ಚು ನಿರ್ಧಾರಾತ್ಮಕತೆಗಾಗಿ; అంటే randomness ಇಲ್ಲದೆ ಜಾಸ್ತಿ ಸಾಧ್ಯತೆ ಇರುವ ಟೋಕನ್ ಅನ್ನು ಮಾತ್ರ ಆಯ್ಕೆಮಾಡುತ್ತದೆ.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// ಜಾವಾಸ್ಕ್ರಿಪ್ಟ್ ಉದಾಹರಣೆ: ಬೀಜ ನಿಯಂತ್ರಣದೊಂದಿಗೆ ನಿರ್ಧಾರಕಾರಿ ಪ್ರತಿಕ್ರಿಯೆಗಳು
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // ಸ್ಥಿರ ಬೀಜದೊಂದಿಗೆ ಮೊದಲ ವಿನಂತಿ
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // ಗರಿ ತಾಪಮಾನ ಅತ್ಯಧಿಕ ನಿರ್ಧಾರಕತೆಗೆ ಶೂನ್ಯ
    });
    
    // ಎರಡನೇ ವಿನಂತಿ ಅದೇ ಬೀಜ ಮತ್ತು ತಾಪಮಾನದಲ್ಲಿ
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // ಮೂರನೇ ವಿನಂತಿ ವಿಭಿನ್ನ ಬೀಜದೊಂದಿಗೆ ಆದರೆ ಅದೇ ತಾಪಮಾನ
    const response3 = await client.sendPrompt(prompt, {
      seed: 67890,
      temperature: 0.0
    });
    
    console.log('Response 1:', response1.generatedText);
    console.log('Response 2:', response2.generatedText);
    console.log('Response 3:', response3.generatedText);
    console.log('Responses 1 and 2 match:', response1.generatedText === response2.generatedText);
    console.log('Responses 1 and 3 match:', response1.generatedText === response3.generatedText);
    
  } catch (error) {
    console.error('Error in deterministic sampling demo:', error);
  }
}

deterministicSampling();
```

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸರ್ವರ್ URL ಹೊಂದಿದ MCP ಕ್ಲೈಂಟ್ ಪ್ರಾರಂಭಿಸಲಾಗಿದೆ.
- ಒಂದೇ ಪ್ರಾಂಪ್ಟ್, ನಿಗದಿತ ಬೀಜ ಮತ್ತು ಶೂನ್ಯ ತಾಪಮಾನದ ಎರಡು ವಿನಂತಿಗಳನ್ನು ಸಂರಚಿಸಲಾಗಿದೆ.
- ಇಬ್ಬರೂ ವಿನಂತಿಗಳನ್ನು ಕಳುಹಿಸಿ ಉತ್ಪಾದಿತ ಪಠ್ಯವನ್ನು ಔಟ್ ಪುಟ್ ಮಾಡಲಾಗಿದೆ.
- ಮೊದಲ ವಿನಂತಿಯ ಉತ್ತರಗಳು ನಿರ್ಧಾರಾತ್ಮಕ ಸ್ವಭಾವದಿಂದ ಒಂದೇ ಇದ್ದವು (ಒಂದೇ ಬೀಜ ಮತ್ತು ತಾಪಮಾನ).
- `seed` ಬಳಸಿ ನಿಗದಿತ ಯಾದೃಚ್ಛಿಕ ಬೀಜವನ್ನು ಸಿಗ್ರಿಸ್ ಮಾಡಲಾಗಿದೆ, ಇದರಿಂದ ಮಾದರಿ ಪ್ರತೀ ಬಾರಿ ಒಂದೇ ಇನ್‌ಪುಟ್‌ಗೆ ಒಂದೇ ಉತ್ತರ ನೀಡುತ್ತದೆ.
- `temperature` ಅನ್ನು ಶೂನ್ಯಕ್ಕೆ ಸೆಟ್ ಮಾಡಿ ಹೆಚ್ಚು ನಿರ್ಧಾರಾತ್ಮಕತೆಗಾಗಿ.
- ಮೂರನೇ ವಿನಂತಿಗೆ ಬೇರೆ ಬೀಜ ಬಳಸಿದ್ದು, ನಾಯಾ ಬೀಜ ಬದಲಾವಣೆ ಜೊತೆ ವಿಭಿನ್ನ ಉತ್ತರ ದೊರಕುತ್ತದೆ.

---

## ಸುಗಮ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಸಂರಚನೆ

ಬುದ್ಧಿವಂತಿಕೆಯ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪ್ರತಿಯೊಂದು ವಿನಂತಿಯ ಸಂಧರ್ಭ ಮತ್ತು ಅವಶ್ಯಕತೆಗಳನ್ನು ಆಧರಿಸಿ ಪರಿಮಾಣಗಳನ್ನು ಬದಲಿಸುತ್ತದೆ. ಇದಕ್ಕೆ ಅವಶ್ಯಕತೆ ಪ್ರಕಾರ ತಾಪಮಾನ, top_p ಮತ್ತು ಪೆನಲ್ಟಿಗಳನ್ನು ಗತಿಯಲ್ಲಿಡುವುದು ಸೇರಿದೆ.

ವಿವಿಧ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಭಾಷೆಗಳಲ್ಲಿ ಸುಗಮ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಅನ್ನು ಹೇಗೆ ಅನುಷ್ಠಾನಗೊಳಿಸುವುದನ್ನು ನೋಡೋಣ.

# [Python](#tab/python)

```python
# Python ಉದಾಹರಣೆ: ವಿನಂತಿ ಸੰਦਰಭದ ಆಧಾರದ ಮೇಲೆ ಡೈನಾಮಿಕ್ ಸ್ಯಾಂಪ್ಲಿಂಗ್
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # ವಿಭಿನ್ನ ಟಾಸ್ಕ್ ಪ್ರಕಾರಗಳಿಗೆ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪೂರ್ವನಿಯೋಜನೆಗಳನ್ನು นิ\ಾನಗೊಳಿಸಿ
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # ಮೂಲ ಪೂರ್ವನಿಯೋಜನೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # ಬಳಕೆದಾರ ಪ್ರಿಯತೆಗಳ ಆಧಾರದ ಮೇಲೆ ಹೊಂದಿಸಿ, ನೀಡಿದ್ದರೆ
        if user_preferences:
            if "creativity_level" in user_preferences:
                # ಸೃಜನಾತ್ಮಕತೆ ಪ್ರಿಯತೆ (1-10) ಆಧಾರದ ಮೇಲೆ ತಾಪಮಾನವನ್ನು ತಗ_ENTER೦ಗಿಸಿ
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # ಇಚ್ಛಿತ ಪ್ರತಿಕ್ರಿಯೆ ವೈವಿಧ್ಯತೆಯ ಆಧಾರದ ಮೇಲೆ top_p ಅನ್ನು ಸಮಂಜಸಗೊಳಿಸಿ
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # ಕ_CUSTOM ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳೊಂದಿಗೆ ವಿನಂತಿಯನ್ನು ಸೃಷ್ಟಿಸಿ ಮತ್ತು ಕಳುಹಿಸಿ
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # ಪಾರದರ್ಶಕತೆಗಾಗಿ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಮೆಟಾ‌ಡೇಟಾ ಜೊತೆಗೆ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಹಿಂತಿರುಗಿಸಿ
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸರಿಹೊಂದುವ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಅನ್ನು ನಿರ್ವಹಿಸುವ `DynamicSamplingService` ವರ್ಗವನ್ನು ರಚಿಸಿದೆವು.
- ವಿವಿಧ ಕಾರ್ಯ ಪ್ರಕಾರಗಳಿಗೆ (ಸೃಜನಾತ್ಮಕ, ವಾಸ್ತವಿಕ, ಕೋಡ್, ವಿಶ್ಲೇಷಣಾತ್ಮಕ) ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪೂರ್ವನಿಯೋಜನೆಗಳನ್ನು ನಿರ್ಧರಿಸಲಾಗಿದೆ.
- ಕಾರ್ಯ ಪ್ರಕಾರ ಆಧಾರಿತ ಮೂಲ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪೂರ್ವನಿಯೋಜನೆಯನ್ನು ಆಯ್ಕೆ ಮಾಡಲಾಗಿದೆ.
- ಬಳಕೆದಾರ ಆಯ್ಕೆ (ಸೃಜನಶೀಲತೆ, ವೈವಿಧ್ಯತೆ) ಆಧಾರದ ಮೇಲೆ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳನ್ನು ಹೊಂದಿಸಲಾಗಿದೆ.
- ಈ ಸಂರಚಿಸಿದ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳೊಂದಿಗೆ ವಿನಂತಿಯನ್ನು ಕಳುಹಿಸಲಾಗಿದೆ.
- ಉತ್ಪಾದಿತ ಪಠ್ಯವನ್ನು ಮತ್ತು ಅನ್ವಯಿಸಿದ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳು ಮತ್ತು ಕಾರ್ಯ ಪ್ರಕಾರವನ್ನು ಗ್ರಾಹಕರಿಗೆ ಮರಳಿಸಲಾಗಿದೆ.
- randomness ನಿಯಂತ್ರಣಕ್ಕೆ `temperature`.
- ಉತ್ತಮ ಗುಣಮಟ್ಟದ ಪಠ್ಯಕ್ಕಾಗಿ top cumulative probability mass ಗೆ ಟೋಕನ್ಗಳ ಆಯ್ಕೆಯನ್ನು ಮಿತಿಗೊಳಿಸಲು `top_p`.
- ಪುನರಾವರ್ತನೆ ಕಡಿಮೆ ಮಾಡಲು ಮತ್ತು ವೈವಿಧ್ಯತೆ ಹೆಚ್ಚಿಸಲು `frequency_penalty`.
- ಬಳಕೆದಾರ ನಿರ್ದಿಷ್ಟ ಕಸ್ಟಮೈಝೇಶನ್ ಗಾಗಿ `user_preferences`.
- ಕಾರ್ಯ ಪ್ರಕಾರ ಆಧಾರದ ಮೇಲೆ ಸೂಕ್ತ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಕಾರ್ಯನೀತಿಯನ್ನು ನಿರ್ಧರಿಸಲು `task_type`.
- ಸಂರಚಿತ ಪರಿಮಾಣಗಳೊಂದಿಗೆ ಪ್ರಾಂಪ್ಟ್ ಕಳುಹಿಸಲು `send_request` ವಿಧಾನ.
- ಮತ್ತಷ್ಟು ವಿಶ್ಲೇಷಣೆ ಅಥವಾ ಪ್ರದರ್ಶನಕ್ಕಾಗಿ ಉತ್ಪಾದಿತ ಉತ್ತರವನ್ನು ಮತ್ತು ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳನ್ನು `generated_text` ಮೂಲಕ ಪಡೆಯಲಾಗಿದೆ.
- `min` ಮತ್ತು `max` ಫಂಕ್ಷನ್ ಗಳ ಮೂಲಕ ವಿಶ್ವಾಸಾರ್ಹ ಮಿತಿಯನ್ನು ಖಚಿತಪಡಿಸಲಾಗಿದೆ, ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಸಂರಚನೆಗಳಿಗೆ ಅನ್ವಯ.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// ಜಾವಾಸ್ಕ್ರಿಪ್ಟ್ ಉದಾಹರಣೆ: ಬಳಕೆದಾರ ಸಂಧರ್ಭದ ಆಧಾರದ ಮೇಲೆ ಡೈನಾಮಿಕ್ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಕಾನ್ಫಿಗರೇಶನ್
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // ಬೇಸ್ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪ್ರೊಫೈಲ್‌ಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // ಐತಿಹಾಸಿಕ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ
    this.performanceHistory = [];
  }
  
  // ಪ್ರಾಂಪ್ಟ್‌ನಿಂದ ಕಾರ್ಯದ ಪ್ರಕಾರವನ್ನು ಪತ್ತೆಮಾಡಿ
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // ಸರಳ heuristic ಪತ್ತೆಮಾಡುವಿಕೆ - ML ವರ್ಗೀಕರಣದಿಂದ ಹೆಚ್ಚಿಸಬಹುದಾಗಿದೆ
    if (context.taskType) return context.taskType;
    
    if (promptLower.includes('code') || 
        promptLower.includes('function') || 
        promptLower.includes('program')) {
      return 'code';
    }
    
    if (promptLower.includes('explain') || 
        promptLower.includes('what is') || 
        promptLower.includes('how does')) {
      return 'factual';
    }
    
    if (promptLower.includes('creative') || 
        promptLower.includes('imagine') || 
        promptLower.includes('story')) {
      return 'creative';
    }
    
    // ಸ್ಪಷ್ಟ ಪ್ರಕಾರ ಪತ್ತೆಯಾಗದಿದ್ದಲ್ಲಿ ಸಂವಾದಾತ್ಮಕಕ್ಕೆ ಡಿಫಾಲ್ಟ್ ಮಾಡಿ
    return 'conversational';
  }
  
  // ಸಂಧರ್ಭ ಮತ್ತು ಬಳಕೆದಾರಆಸಕ್ತಿಗಳ ಆಧಾರದ ಮೇಲೆ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಲೆಕ್ಕಿಸಿ
  getSamplingParameters(prompt, context = {}) {
    // ಕಾರ್ಯದ ಪ್ರಕಾರವನ್ನು ಪತ್ತೆಮಾಡಿ
    const taskType = this.detectTaskType(prompt, context);
    
    // ಬೇಸ್ ಪ್ರೊಫೈಲ್ ಅನ್ನು ಪಡೆಯಿರಿ
    let params = {...this.samplingProfiles[taskType]};
    
    // ಬಳಕೆದಾರ ಆಸಕ್ತಿಗಳ ಆಧಾರದ ಮೇಲೆ调整ಮಾಡಿ
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // 1-10 ಮಟ್ಟದ θερಮಾಪಮಾನ ವ್ಯಾಪ್ತಿಗೆ ಪ್ರಮಾಣಮಾಡಿ
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // ಹೆಚ್ಚಿನ ನಿಖರತೆ ಅಂದರೆ ಕಡಿಮೆ topP (ಹೆಚ್ಚು ಕೇಂದ್ರೀಕೃತ ಆಯ್ಕೆ)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // ಹೆಚ್ಚಿನ ಸ್ಥಿರತೆ ಅಂದರೆ ಕಡಿಮೆ ದಂಡನೆಗಳು
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // ಕಾರ್ಯಕ್ಷಮತಾ ಇತಿಹಾಸದಿಂದ ಕಲಿತ调整ಗಳನ್ನು ಅನ್ವಯಿಸಿ
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // ಸರಳ অভিযೋಜಿತ ತರ್ಕ - ಹೆಚ್ಚು ಪರಿಷ್ಕೃತ ಆಲ್ಗಾರಿಥಮ್‌ಗಳೊಂದಿಗೆ ಹೆಚ್ಚಿಸಬಹುದು
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // ಇತ್ತೀಚಿನ ಇತಿಹಾಸವನ್ನು ಮಾತ್ರ ಪರಿಗಣಿಸಿ
    
    if (relevantHistory.length > 0) {
      // ಸರಾಸರಿ ಕಾರ್ಯಕ್ಷಮತಾ ಅಂಕಗಳನ್ನು ಲೆಕ್ಕಿಸಿ
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // ಕಾರ್ಯಕ್ಷಮತೆ ಮಾತ್ರೆಗಿಂತ ಕೆಳಗಿನಿದ್ದರೆ, ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು调整ಮಾಡಿ
      if (avgScore < 0.7) {
        // ಹೆಚ್ಚು ಸುರಕ್ಷಿತ ಮೌಲ್ಯಗಳ ಕಡೆಗೆ ಸಣ್ಣ调整
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // ಭವಿಷ್ಯದ调整ಗಳಿಗೆ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ದಾಖಲಿಸಿ
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // ಪ್ರತಿಕ್ರಿಯೆಯ ಗುಣಮಟ್ಟದ 0-1 ರೇಟಿಂಗ್
    });
    
    // ಇತಿಹಾಸದ ಗಾತ್ರವನ್ನು ನಿಯಂತ್ರಿಸಿ
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // ಅನ್ವಯಿಸಲಾದ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಪಡೆಯಿರಿ
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // ಅನ್ವಯಿಸಲಾದ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳೊಂದಿಗೆ ವಿನಂತಿ ಕಳುಹಿಸಿ
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // ಬಳಕೆದಾರ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನೀಡುತ್ತಿದೆಯಾದರೆ, ಭವಿಷ್ಯದ ಉತ್ತಮೀಕರಣಕ್ಕಾಗಿ ಅದನ್ನು ದಾಖಲಿಸಿ
    if (context.recordPerformance) {
      this.recordPerformance(prompt, samplingParams, response, context.feedbackScore || 0.5);
    }
    
    return {
      response,
      appliedSamplingParams: samplingParams,
      detectedTaskType: this.detectTaskType(prompt, context)
    };
  }
}

// ಉದಾಹರಣೆಯ ಬಳಕೆ
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // ವಿನ್ಯಾಸ చేసింది ಕಾರ್ಯವು ಕಸ್ಟಮ್ ಬಳಕೆದಾರ ಆಸಕ್ತಿಗಳೊಂದಿಗೆ
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // ಹೆಚ್ಚು ಸೃಜನಶೀಲತೆ (1-10)
          consistency: 3  // ಕಡಿಮೆ ಸ್ಥಿರತೆ (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // ಕೋಡ್ ಉತ್ಪಾದನೆ ಕಾರ್ಯ
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // ಕಡಿಮೆ ಸೃಜನಶೀಲತೆ
          precision: 8,   // ಹೆಚ್ಚು ನಿಖರತೆ
          consistency: 9  // ಹೆಚ್ಚು ಸ್ಥಿರತೆ
        }
      }
    );
    
    console.log('\nCode Task:');
    console.log(`Detected type: ${codeResult.detectedTaskType}`);
    console.log('Applied sampling:', codeResult.appliedSamplingParams);
    console.log(codeResult.response.generatedText);
    
  } catch (error) {
    console.error('Error in adaptive sampling demo:', error);
  }
}

demonstrateAdaptiveSampling();
```

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಕಾರ್ಯ ಪ್ರಕಾರ ಮತ್ತು ಬಳಕೆದಾರ ಆಯ್ಕೆ ಆಧಾರದ ಮೇಲೆ ಗತಿಶೀಲ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ನಿರ್ವಹಿಸುವ `AdaptiveSamplingManager` ವರ್ಗ.
- ವಿವಿಧ ಕಾರ್ಯ ಪ್ರಕಾರಗಳಿಗಾಗಿ (ಸೃಜನಾತ್ಮಕ, ವಾಸ್ತವಿಕ, ಕೋಡ್, ಸಂವಹನಾತ್ಮಕ) ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪ್ರೊಫೈಲ್‌ಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿದೆವು.
- ಸರಳ ನಿಯಮಾಲುಗಳ ಮೂಲಕ ಪ್ರಾಂಪ್ಟ್ ಇಂದ ಕಾರ್ಯ ಪ್ರಕಾರವನ್ನು ಪತ್ತೆಹಚ್ಚುವ ವಿಧಾನವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಲಾಗಿದೆ.
- ಪತ್ತೆಹಚ್ಚಿದ ಕಾರ್ಯ ಪ್ರಕಾರ ಮತ್ತು ಬಳಕೆದಾರ ಆಯ್ಕೆಯ ಆಧಾರದ ಮೇಲೆ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳನ್ನು ಲೆಕ್ಕ ಹಾಕಲಾಗಿದೆ.
- ಇತಿಹಾಸದ ಕಾರ್ಯಕ್ಷಮತೆಯ ಆಧಾರದ ಮೇಲೆ ಅಧ್ಯಯನ ಮಾಡಲಾದ ಬದಲಾವಣೆಗಳನ್ನು ಅನ್ವಯಿಸಿದೆವು.
- ಭವಿಷ್ಯದ ಬದಲಾವಣೆಗಾಗಿ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ದಾಖಲಿಸಲಾಗಿದೆ, ಇದರಿಂದ ವ್ಯವಸ್ಥೆ ಹಿಂದಿನ ಅನುಭವಗಳಿಂದ ಕಲಿಯಬಹುದು.
- ಗತಿಶೀಲ ಸಂರಚಿತ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳೊಂದಿಗೆ ವಿನಂತಿಗಳನ್ನು ಕಳುಹಿಸಿ, ಅನ್ವಯಿಸಿದ ಪರಿಮಾಣಗಳು ಮತ್ತು ಪತ್ತೆ ಹಚ್ಚಿದ ಕಾರ್ಯ ಪ್ರಕಾರದ ಜೊತೆಗೆ ಉತ್ಪಾದಿತ ಉತ್ತರವನ್ನು ಮರಳಿಸಲಾಗಿದೆ.
- ಬಳಸದಾಗಿದೆ:
    - `userPreferences` ಮೂಲಕ ಬಳಕೆದಾರ-ವ್ಯಾಖ್ಯಾನಿತ ಸೃಜನಶೀಲತೆ, ನಿಖರತೆ, ಮತ್ತು ಸತತತೆ ಮಟ್ಟಗಳಿಗೆ ಅನುಗುಣವಾಗಿ ಪರಿಮಾಣಗಳನ್ನು ಕಸ್ಟಮೈಸ್ ಮಾಡುವುದು.
    - `detectTaskType` ಮೂಲಕ ಪ್ರಾಂಪ್ಟ್ ಆಧಾರಿತ ಕಾರ್ಯ ಪ್ರಕಾರ ಪತ್ತೆ ಹಚ್ಚುವುದು.
    - `recordPerformance` ಮೂಲಕ ಉತ್ತರಗಳ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ದಾಖಲಿಸುವುದು, ಪೂರ್ವ ಸಂವಹನದಿಂದ ಕಲಿಯಲು ಸಹಾಯ.
    - `applyLearnedAdjustments` ಮೂಲಕ ಇತಿಹಾಸ ಕಾರ್ಯಕ್ಷಮತೆ ಆಧಾರದ ಮೇಲೆ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣ ಬದಲಾವಣೆಗಳು.
    - `generateResponse` ಸಂಪೂರ್ಣ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಅಡಾಪ್ಟಿವ್ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಮೂಲಕ ಹೆಸರಿಸುವುದು, ವಿಭಿನ್ನ ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಮತ್ತು ಪ್ರಕಾರಗಳಿಗಾಗಿ ಸರಳ ಕರೆ.
    - `allowedTools` ಮೂಲಕ ಉತ್ಪಾದನೆಗೆ ಬಳಸಬಹುದಾದ ಸಾಧನಗಳ ಆಯ್ಕೆ, ಹೆಚ್ಚು ಸಂಧರ್ಭಜ್ಞ ಉತ್ತರಗಳಿಗಾಗಿ.
    - `feedbackScore` ಮೂಲಕ ಬಳಕೆದಾರರಿಂದ ಉತ್ತರ ಗುಣಮಟ್ಟದ ಮೇಲೆ ಪ್ರತಿಕ್ರಿಯೆ ಪಡೆಯುವುದು, ಇದರ ಮೂಲಕ ಮುಂದಿನ ಸುಧಾರಣೆಗೆ ನೆರವು.
    - `performanceHistory` ಮೂಲಕ ಹಿಂದಿನ ಸಂವಹನಗಳ ದಾಖಲೆಯನ್ನು ಕಾಯ್ದು ಬಿಡುವುದು, ವ್ಯವಸ್ಥೆಗೆ ಕಲಿಕೆ ಮತ್ತು ಸುಧಾರಣೆ ಮಾಡಲು.
    - `getSamplingParameters` ಮೂಲಕ ವಿನಂತಿಯ ಸಂಧರ್ಭದಲ್ಲಿ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಪರಿಮಾಣಗಳನ್ನು ಬದಲಾಯಿಸುವುದು, ಹೆಚ್ಚು ವೈಶಿಷ್ಟ್ಯಮಯ ಹಾಗೂ ಪ್ರತಿಕ್ರಿಯಾಶೀಲ ಮಾದರಿ ವರ್ತನೆಗಾಗಿ.
    - `detectTaskType` ಮೂಲಕ ಪ್ರಾಂಪ್ಟ್ ಆಧಾರಿತ ಕಾರ್ಯ ಪ್ರಕಾರ ವರ್ಗಾಯಿಸುವುದು, ವಿಭಿನ್ನ ವಿನಂತಿಗಳಿಗೆ ಸೂಕ್ತ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ತಂತ್ರಗಳನ್ನು ಅನ್ವಯಿಸಲು.
    - `samplingProfiles` ಮೂಲಕ ವಿವಿಧ ಕಾರ್ಯ ಪ್ರಕಾರಗಳಿಗೆ ಆಧಾರ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಸಂರಚನೆಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವುದು, ವಿನಂತಿಯ ಸ್ವಭಾವ ಆಧಾರದ ಮೇಲೆ ವೇಗದ ಬದಲಾವಣೆಗಾಗಿ.

---

## ಮುಂದಿನದೇನು

- [5.7 ವಿಸ್ತರಣೆ](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->