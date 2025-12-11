<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62150e27d4b7b5797ee41146d176e6b",
  "translation_date": "2025-12-11T10:54:30+00:00",
  "source_file": "08-BestPractices/README.md",
  "language_code": "kn"
}
-->
# MCP ಅಭಿವೃದ್ಧಿ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು

[![MCP Development Best Practices](../../../translated_images/09.d0f6d86c9d72134ccf5a8d8c8650a0557e519936661fc894cad72d73522227cb.kn.png)](https://youtu.be/W56H9W7x-ao)

_(ಈ ಪಾಠದ ವೀಡಿಯೋವನ್ನು ವೀಕ್ಷಿಸಲು ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

## ಅವಲೋಕನ

ಈ ಪಾಠವು ಉತ್ಪಾದನಾ ಪರಿಸರಗಳಲ್ಲಿ MCP ಸರ್ವರ್‌ಗಳು ಮತ್ತು ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಅಭಿವೃದ್ಧಿಪಡಿಸುವುದು, ಪರೀಕ್ಷಿಸುವುದು ಮತ್ತು ನಿಯೋಜಿಸುವುದಕ್ಕಾಗಿ ಉನ್ನತ ಮಟ್ಟದ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸುತ್ತದೆ. MCP ಪರಿಸರಗಳು ಸಂಕೀರ್ಣತೆ ಮತ್ತು ಮಹತ್ವದಲ್ಲಿ ಬೆಳೆಯುತ್ತಿರುವಂತೆ, ಸ್ಥಾಪಿತ ಮಾದರಿಗಳನ್ನು ಅನುಸರಿಸುವುದು ವಿಶ್ವಾಸಾರ್ಹತೆ, ನಿರ್ವಹಣಾ ಸುಲಭತೆ ಮತ್ತು ಪರಸ್ಪರ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಖಚಿತಪಡಿಸುತ್ತದೆ. ಈ ಪಾಠವು ನೈಜ ಜಗತ್ತಿನ MCP ಅನುಷ್ಠಾನಗಳಿಂದ ಪಡೆದ ಪ್ರಾಯೋಗಿಕ ಜ್ಞಾನವನ್ನು ಸಂಗ್ರಹಿಸಿ, ಪರಿಣಾಮಕಾರಿ ಸಂಪನ್ಮೂಲಗಳು, ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಮತ್ತು ಸಾಧನಗಳೊಂದಿಗೆ ಬಲವಾದ, ಪರಿಣಾಮಕಾರಿ ಸರ್ವರ್‌ಗಳನ್ನು ರಚಿಸುವಲ್ಲಿ ನಿಮಗೆ ಮಾರ್ಗದರ್ಶನ ನೀಡುತ್ತದೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪಾಠದ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಈ ಕೆಳಗಿನವುಗಳನ್ನು ಮಾಡಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- MCP ಸರ್ವರ್ ಮತ್ತು ವೈಶಿಷ್ಟ್ಯ ವಿನ್ಯಾಸದಲ್ಲಿ ಕೈಗಾರಿಕಾ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳನ್ನು ಅನ್ವಯಿಸುವುದು
- MCP ಸರ್ವರ್‌ಗಳಿಗಾಗಿ ಸಮಗ್ರ ಪರೀಕ್ಷಾ ತಂತ್ರಗಳನ್ನು ರಚಿಸುವುದು
- ಸಂಕೀರ್ಣ MCP ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗಾಗಿ ಪರಿಣಾಮಕಾರಿ, ಮರುಬಳಕೆ ಮಾಡಬಹುದಾದ ವರ್ಕ್‌ಫ್ಲೋ ಮಾದರಿಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸುವುದು
- MCP ಸರ್ವರ್‌ಗಳಲ್ಲಿ ಸರಿಯಾದ ದೋಷ ನಿರ್ವಹಣೆ, ಲಾಗಿಂಗ್ ಮತ್ತು ಅವಲೋಕನವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು
- ಕಾರ್ಯಕ್ಷಮತೆ, ಭದ್ರತೆ ಮತ್ತು ನಿರ್ವಹಣಾ ಸುಲಭತೆಗಾಗಿ MCP ಅನುಷ್ಠಾನಗಳನ್ನು ಆಪ್ಟಿಮೈಸ್ ಮಾಡುವುದು

## MCP ಮೂಲ ತತ್ವಗಳು

ನಿರ್ದಿಷ್ಟ ಅನುಷ್ಠಾನ ಅಭ್ಯಾಸಗಳಿಗೆ ಮುನ್ನಡೆಸುವ ಮೊದಲು, ಪರಿಣಾಮಕಾರಿ MCP ಅಭಿವೃದ್ಧಿಗೆ ಮಾರ್ಗದರ್ಶನ ನೀಡುವ ಮೂಲ ತತ್ವಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು ಮುಖ್ಯ:

1. **ಪ್ರಮಾಣೀಕೃತ ಸಂವಹನ**: MCP ತನ್ನ ಆಧಾರವಾಗಿ JSON-RPC 2.0 ಅನ್ನು ಬಳಸುತ್ತದೆ, ಎಲ್ಲಾ ಅನುಷ್ಠಾನಗಳಲ್ಲಿ ವಿನಂತಿಗಳು, ಪ್ರತಿಕ್ರಿಯೆಗಳು ಮತ್ತು ದೋಷ ನಿರ್ವಹಣೆಗೆ ಸुसಂಗತ ಸ್ವರೂಪವನ್ನು ಒದಗಿಸುತ್ತದೆ.

2. **ಬಳಕೆದಾರ ಕೇಂದ್ರಿತ ವಿನ್ಯಾಸ**: ನಿಮ್ಮ MCP ಅನುಷ್ಠಾನಗಳಲ್ಲಿ ಸದಾ ಬಳಕೆದಾರರ ಅನುಮತಿ, ನಿಯಂತ್ರಣ ಮತ್ತು ಪಾರದರ್ಶಕತೆಯನ್ನು ಪ್ರಾಥಮ್ಯ ನೀಡಿ.

3. **ಭದ್ರತೆ ಮೊದಲಿಗೆ**: ದೃಢವಾದ ಭದ್ರತಾ ಕ್ರಮಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ, ಇದರಲ್ಲಿ ಪ್ರಾಮಾಣೀಕರಣ, ಪ್ರಾಧಿಕಾರ, ಮಾನ್ಯತೆ ಮತ್ತು ದರ ನಿಯಂತ್ರಣ ಸೇರಿವೆ.

4. **ಮಾಡ್ಯೂಲರ್ ವಾಸ್ತುಶಿಲ್ಪ**: ಪ್ರತಿ ಸಾಧನ ಮತ್ತು ಸಂಪನ್ಮೂಲಕ್ಕೆ ಸ್ಪಷ್ಟ, ಕೇಂದ್ರೀಕೃತ ಉದ್ದೇಶವಿರುವ ಮಾಡ್ಯೂಲರ್ ದೃಷ್ಟಿಕೋನದಿಂದ ನಿಮ್ಮ MCP ಸರ್ವರ್‌ಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ.

5. **ಸ್ಥಿತಿಸ್ಥಾಪಕ ಸಂಪರ್ಕಗಳು**: ಹೆಚ್ಚಿನ ಸुसಂಗತ ಮತ್ತು ಸಾಂದರ್ಭಿಕ ಜಾಗೃತಿ ಹೊಂದಿರುವ ಸಂವಹನಕ್ಕಾಗಿ ಬಹು ವಿನಂತಿಗಳಲ್ಲಿ ಸ್ಥಿತಿಯನ್ನು ಕಾಯ್ದುಕೊಳ್ಳುವ MCP ಸಾಮರ್ಥ್ಯವನ್ನು ಉಪಯೋಗಿಸಿ.

## ಅಧಿಕೃತ MCP ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು

ಕೆಳಗಿನ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು ಅಧಿಕೃತ ಮಾದರಿ ಸಾಂದರ್ಭಿಕ ಪ್ರೋಟೋಕಾಲ್ ಡಾಕ್ಯುಮೆಂಟೇಶನ್‌ನಿಂದ ಪಡೆದಿವೆ:

### ಭದ್ರತಾ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು

1. **ಬಳಕೆದಾರ ಅನುಮತಿ ಮತ್ತು ನಿಯಂತ್ರಣ**: ಡೇಟಾವನ್ನು ಪ್ರವೇಶಿಸುವ ಮೊದಲು ಅಥವಾ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಮೊದಲು ಸದಾ ಸ್ಪಷ್ಟ ಬಳಕೆದಾರ ಅನುಮತಿಯನ್ನು ಅಗತ್ಯವಿರಲಿ. ಯಾವ ಡೇಟಾ ಹಂಚಿಕೊಳ್ಳಲಾಗುತ್ತದೆ ಮತ್ತು ಯಾವ ಕ್ರಿಯೆಗಳು ಅನುಮತಿಸಲಾಗಿದೆ ಎಂಬುದರ ಮೇಲೆ ಸ್ಪಷ್ಟ ನಿಯಂತ್ರಣವನ್ನು ಒದಗಿಸಿ.

2. **ಡೇಟಾ ಗೌಪ್ಯತೆ**: ಸ್ಪಷ್ಟ ಅನುಮತಿಯೊಂದಿಗೆ ಮಾತ್ರ ಬಳಕೆದಾರ ಡೇಟಾವನ್ನು ಬಹಿರಂಗಪಡಿಸಿ ಮತ್ತು ಸೂಕ್ತ ಪ್ರವೇಶ ನಿಯಂತ್ರಣಗಳೊಂದಿಗೆ ಅದನ್ನು ರಕ್ಷಿಸಿ. ಅನಧಿಕೃತ ಡೇಟಾ ಪ್ರಸರಣದ ವಿರುದ್ಧ ರಕ್ಷಣೆ ಒದಗಿಸಿ.

3. **ಸಾಧನ ಭದ್ರತೆ**: ಯಾವುದೇ ಸಾಧನವನ್ನು ಕರೆಸುವ ಮೊದಲು ಸ್ಪಷ್ಟ ಬಳಕೆದಾರ ಅನುಮತಿಯನ್ನು ಅಗತ್ಯವಿರಲಿ. ಪ್ರತಿ ಸಾಧನದ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಬಳಕೆದಾರರು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಂತೆ ಮಾಡಿ ಮತ್ತು ದೃಢವಾದ ಭದ್ರತಾ ಗಡಿಗಳನ್ನು ಜಾರಿಗೆ ತರುವಿರಿ.

4. **ಸಾಧನ ಅನುಮತಿ ನಿಯಂತ್ರಣ**: ಸೆಷನ್ ಸಮಯದಲ್ಲಿ ಯಾವ ಸಾಧನಗಳನ್ನು ಮಾದರಿ ಬಳಸಲು ಅನುಮತಿಸಲಾಗಿದೆ ಎಂಬುದನ್ನು ಸಂರಚಿಸಿ, ಸ್ಪಷ್ಟವಾಗಿ ಅನುಮತಿಸಲ್ಪಟ್ಟ ಸಾಧನಗಳಿಗೆ ಮಾತ್ರ ಪ್ರವೇಶವನ್ನು ಖಚಿತಪಡಿಸಿ.

5. **ಪ್ರಾಮಾಣೀಕರಣ**: ಸಾಧನಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಅಥವಾ ಸಂವೇದನಾಶೀಲ ಕಾರ್ಯಗಳಿಗೆ ಪ್ರವೇಶ ನೀಡುವ ಮೊದಲು ಸರಿಯಾದ ಪ್ರಾಮಾಣೀಕರಣವನ್ನು ಅಗತ್ಯವಿರಲಿ, API ಕೀಗಳು, OAuth ಟೋಕನ್‌ಗಳು ಅಥವಾ ಇತರ ಭದ್ರ ಪ್ರಾಮಾಣೀಕರಣ ವಿಧಾನಗಳನ್ನು ಬಳಸಿ.

6. **ಪ್ಯಾರಾಮೀಟರ್ ಮಾನ್ಯತೆ**: ಎಲ್ಲಾ ಸಾಧನ ಕರೆಗಳಿಗೆ ಮಾನ್ಯತೆಯನ್ನು ಜಾರಿಗೆ ತರುವ ಮೂಲಕ ತಪ್ಪು ಅಥವಾ ದುಷ್ಟ ಇನ್‌ಪುಟ್‌ಗಳು ಸಾಧನ ಅನುಷ್ಠಾನಗಳಿಗೆ ತಲುಪದಂತೆ ತಡೆಯಿರಿ.

7. **ದರ ನಿಯಂತ್ರಣ**: ದುರುಪಯೋಗವನ್ನು ತಡೆಯಲು ಮತ್ತು ಸರ್ವರ್ ಸಂಪನ್ಮೂಲಗಳ ನ್ಯಾಯಸಮ್ಮತ ಬಳಕೆಯನ್ನು ಖಚಿತಪಡಿಸಲು ದರ ನಿಯಂತ್ರಣವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ.

### ಅನುಷ್ಠಾನ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು

1. **ಸಾಮರ್ಥ್ಯ ಸಂವಹನ**: ಸಂಪರ್ಕ ಸ್ಥಾಪನೆಯಾಗುವಾಗ, ಬೆಂಬಲಿತ ವೈಶಿಷ್ಟ್ಯಗಳು, ಪ್ರೋಟೋಕಾಲ್ ಆವೃತ್ತಿಗಳು, ಲಭ್ಯವಿರುವ ಸಾಧನಗಳು ಮತ್ತು ಸಂಪನ್ಮೂಲಗಳ ಬಗ್ಗೆ ಮಾಹಿತಿ ವಿನಿಮಯ ಮಾಡಿಕೊಳ್ಳಿ.

2. **ಸಾಧನ ವಿನ್ಯಾಸ**: ಬಹುಮುಖ ಸಮಸ್ಯೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಬದಲಿಗೆ ಒಳ್ಳೆಯ ಕಾರ್ಯಕ್ಷಮತೆಯೊಂದಿಗೆ ಒಂದೇ ಕಾರ್ಯವನ್ನು ಮಾಡುವ ಕೇಂದ್ರೀಕೃತ ಸಾಧನಗಳನ್ನು ರಚಿಸಿ.

3. **ದೋಷ ನಿರ್ವಹಣೆ**: ಸಮಸ್ಯೆಗಳನ್ನು ಗುರುತಿಸಲು, ವೈಫಲ್ಯಗಳನ್ನು ಸೌಮ್ಯವಾಗಿ ನಿರ್ವಹಿಸಲು ಮತ್ತು ಕಾರ್ಯನಿರ್ವಹಣೀಯ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಒದಗಿಸಲು ಪ್ರಮಾಣೀಕೃತ ದೋಷ ಸಂದೇಶಗಳು ಮತ್ತು ಕೋಡ್‌ಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ.

4. **ಲಾಗಿಂಗ್**: ಪ್ರೋಟೋಕಾಲ್ ಸಂವಹನಗಳ ಆಡಿಟಿಂಗ್, ಡಿಬಗಿಂಗ್ ಮತ್ತು ಮೇಲ್ವಿಚಾರಣೆಗೆ ರಚನಾತ್ಮಕ ಲಾಗ್‌ಗಳನ್ನು ಸಂರಚಿಸಿ.

5. **ಪ್ರಗತಿ ಟ್ರ್ಯಾಕಿಂಗ್**: ದೀರ್ಘಕಾಲದ ಕಾರ್ಯಾಚರಣೆಗಳಿಗೆ, ಪ್ರತಿಕ್ರಿಯಾಶೀಲ ಬಳಕೆದಾರ ಇಂಟರ್ಫೇಸ್‌ಗಳನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಲು ಪ್ರಗತಿ ನವೀಕರಣಗಳನ್ನು ವರದಿ ಮಾಡಿ.

6. **ವಿನಂತಿ ರದ್ದುಪಡಿಸುವಿಕೆ**: ಈಗ ಅಗತ್ಯವಿಲ್ಲದ ಅಥವಾ ಹೆಚ್ಚು ಸಮಯ ತೆಗೆದುಕೊಳ್ಳುತ್ತಿರುವ ವಿಮಾನದಲ್ಲಿರುವ ವಿನಂತಿಗಳನ್ನು ಗ್ರಾಹಕರು ರದ್ದುಪಡಿಸಲು ಅನುಮತಿಸಿ.

## ಹೆಚ್ಚುವರಿ ಉಲ್ಲೇಖಗಳು

MCP ಉತ್ತಮ ಅಭ್ಯಾಸಗಳ ಬಗ್ಗೆ ಅತ್ಯಂತ ನವೀಕರಿಸಿದ ಮಾಹಿತಿಗಾಗಿ, ಈ ಕೆಳಗಿನವುಗಳನ್ನು ನೋಡಿ:

- [MCP ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://modelcontextprotocol.io/)
- [MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್](https://spec.modelcontextprotocol.io/)
- [GitHub ರೆಪೊಸಿಟರಿ](https://github.com/modelcontextprotocol)
- [ಭದ್ರತಾ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## ಪ್ರಾಯೋಗಿಕ ಅನುಷ್ಠಾನ ಉದಾಹರಣೆಗಳು

### ಸಾಧನ ವಿನ್ಯಾಸ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು

#### 1. ಏಕ ಜವಾಬ್ದಾರಿ ತತ್ವ

ಪ್ರತಿ MCP ಸಾಧನಕ್ಕೆ ಸ್ಪಷ್ಟ, ಕೇಂದ್ರೀಕೃತ ಉದ್ದೇಶವಿರಬೇಕು. ಬಹುಮುಖ ಸಮಸ್ಯೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಬದಲಿಗೆ, ನಿರ್ದಿಷ್ಟ ಕಾರ್ಯಗಳಲ್ಲಿ ಪರಿಣತಿ ಹೊಂದಿರುವ ವಿಶೇಷ ಸಾಧನಗಳನ್ನು ಅಭಿವೃದ್ಧಿಪಡಿಸಿ.

```csharp
// A focused tool that does one thing well
public class WeatherForecastTool : ITool
{
    private readonly IWeatherService _weatherService;
    
    public WeatherForecastTool(IWeatherService weatherService)
    {
        _weatherService = weatherService;
    }
    
    public string Name => "weatherForecast";
    public string Description => "Gets weather forecast for a specific location";
    
    public ToolDefinition GetDefinition()
    {
        return new ToolDefinition
        {
            Name = Name,
            Description = Description,
            Parameters = new Dictionary<string, ParameterDefinition>
            {
                ["location"] = new ParameterDefinition
                {
                    Type = ParameterType.String,
                    Description = "City or location name"
                },
                ["days"] = new ParameterDefinition
                {
                    Type = ParameterType.Integer,
                    Description = "Number of forecast days",
                    Default = 3
                }
            },
            Required = new[] { "location" }
        };
    }
    
    public async Task<ToolResponse> ExecuteAsync(IDictionary<string, object> parameters)
    {
        var location = parameters["location"].ToString();
        var days = parameters.ContainsKey("days") 
            ? Convert.ToInt32(parameters["days"]) 
            : 3;
            
        var forecast = await _weatherService.GetForecastAsync(location, days);
        
        return new ToolResponse
        {
            Content = new List<ContentItem>
            {
                new TextContent(JsonSerializer.Serialize(forecast))
            }
        };
    }
}
```

#### 2. ಸुसಂಗತ ದೋಷ ನಿರ್ವಹಣೆ

ಸೂಚನಾತ್ಮಕ ದೋಷ ಸಂದೇಶಗಳು ಮತ್ತು ಸೂಕ್ತ ಪುನಃಪಡೆಯುವ ಯಂತ್ರಗಳನ್ನು ಹೊಂದಿರುವ ದೃಢವಾದ ದೋಷ ನಿರ್ವಹಣೆಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ.

```python
# ಸಮಗ್ರ ದೋಷ ನಿರ್ವಹಣೆಯೊಂದಿಗೆ ಪೈಥಾನ್ ಉದಾಹರಣೆ
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # ಪರಿಮಾಣ ಪರಿಶೀಲನೆ
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # ಭದ್ರತಾ ಪರಿಶೀಲನೆ
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # ಸಮಯ ಮಿತಿ ಹೊಂದಿರುವ ಡೇಟಾಬೇಸ್ ಕಾರ್ಯಾಚರಣೆ
                async with timeout(10):  # 10 ಸೆಕೆಂಡು ಸಮಯ ಮಿತಿ
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # ಸಂಪರ್ಕ ದೋಷಗಳು ತಾತ್ಕಾಲಿಕವಾಗಿರಬಹುದು
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # ಪ್ರಶ್ನೆ ದೋಷಗಳು ಸಾಧ್ಯತೆಯುಳ್ಳ ಗ್ರಾಹಕ ದೋಷಗಳು
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # ಸಾಧನ-ನಿರ್ದಿಷ್ಟ ದೋಷಗಳನ್ನು ಅನುಮತಿಸಿ
            raise
        except Exception as e:
            # ಅಪ್ರತೀಕ್ಷಿತ ದೋಷಗಳಿಗಾಗಿ ಹಿಡಿಯುವಿಕೆ
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # SQL ಇಂಜೆಕ್ಷನ್ ಪತ್ತೆಮಾಡುವಿಕೆಯ ಅನುಷ್ಠಾನ
        pass
        
    def _log_error(self, message, error):
        # ದೋಷ ಲಾಗಿಂಗ್ ಅನುಷ್ಠಾನ
        pass
```

#### 3. ಪ್ಯಾರಾಮೀಟರ್ ಮಾನ್ಯತೆ

ತಪ್ಪು ಅಥವಾ ದುಷ್ಟ ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ತಡೆಯಲು ಸದಾ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಮಾನ್ಯಗೊಳಿಸಿ.

```javascript
// JavaScript/TypeScript ಉದಾಹರಣೆ ವಿವರವಾದ ಪ್ಯಾರಾಮೀಟರ್ ಪರಿಶೀಲನೆಯೊಂದಿಗೆ
class FileOperationTool {
  getName() {
    return "fileOperation";
  }
  
  getDescription() {
    return "Performs file operations like read, write, and delete";
  }
  
  getDefinition() {
    return {
      name: this.getName(),
      description: this.getDescription(),
      parameters: {
        operation: {
          type: "string",
          description: "Operation to perform",
          enum: ["read", "write", "delete"]
        },
        path: {
          type: "string",
          description: "File path (must be within allowed directories)"
        },
        content: {
          type: "string",
          description: "Content to write (only for write operation)",
          optional: true
        }
      },
      required: ["operation", "path"]
    };
  }
  
  async execute(parameters) {
    // 1. ಪ್ಯಾರಾಮೀಟರ್ ಇರುವಿಕೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. ಪ್ಯಾರಾಮೀಟರ್ ಪ್ರಕಾರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. ಪ್ಯಾರಾಮೀಟರ್ ಮೌಲ್ಯಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. ಬರೆಯುವ ಕಾರ್ಯಕ್ಕಾಗಿ ವಿಷಯದ ಇರುವಿಕೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. ಮಾರ್ಗ ಸುರಕ್ಷತೆ ಪರಿಶೀಲನೆ
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // ಪರಿಶೀಲಿಸಲಾದ ಪ್ಯಾರಾಮೀಟರ್ ಆಧಾರಿತ ಅನುಷ್ಠಾನ
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // ಮಾರ್ಗ ಸುರಕ್ಷತೆ ಪರಿಶೀಲನೆಯ ಅನುಷ್ಠಾನ
    // ...
  }
}
```

### ಭದ್ರತಾ ಅನುಷ್ಠಾನ ಉದಾಹರಣೆಗಳು

#### 1. ಪ್ರಾಮಾಣೀಕರಣ ಮತ್ತು ಪ್ರಾಧಿಕಾರ

```java
// ದೃಢೀಕರಣ ಮತ್ತು ಪ್ರಾಧಿಕಾರಣೆಯೊಂದಿಗೆ ಜಾವಾ ಉದಾಹರಣೆ
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // ಅವಲಂಬನೆ ಇಂಜೆಕ್ಷನ್
    public SecureDataAccessTool(
            AuthenticationService authService,
            AuthorizationService authzService,
            DataService dataService) {
        this.authService = authService;
        this.authzService = authzService;
        this.dataService = dataService;
    }
    
    @Override
    public String getName() {
        return "secureDataAccess";
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        // 1. ದೃಢೀಕರಣ ಸನ್ನಿವೇಶವನ್ನು ಹೊರತೆಗೆಯಿರಿ
        String authToken = request.getContext().getAuthToken();
        
        // 2. ಬಳಕೆದಾರರನ್ನು ದೃಢೀಕರಿಸಿ
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. ನಿರ್ದಿಷ್ಟ ಕಾರ್ಯಾಚರಣೆಗೆ ಪ್ರಾಧಿಕಾರಣೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. ಅನುಮೋದಿತ ಕಾರ್ಯಾಚರಣೆಯೊಂದಿಗೆ ಮುಂದುವರಿಯಿರಿ
        try {
            switch (operation) {
                case "read":
                    Object data = dataService.getData(dataId, user.getId());
                    return ToolResponse.success(data);
                case "update":
                    JsonNode newData = request.getParameters().get("newData");
                    dataService.updateData(dataId, newData, user.getId());
                    return ToolResponse.success("Data updated successfully");
                default:
                    return ToolResponse.error("Unsupported operation: " + operation);
            }
        } catch (Exception e) {
            return ToolResponse.error("Operation failed: " + e.getMessage());
        }
    }
}
```

#### 2. ದರ ನಿಯಂತ್ರಣ

```csharp
// C# rate limiting implementation
public class RateLimitingMiddleware
{
    private readonly RequestDelegate _next;
    private readonly IMemoryCache _cache;
    private readonly ILogger<RateLimitingMiddleware> _logger;
    
    // Configuration options
    private readonly int _maxRequestsPerMinute;
    
    public RateLimitingMiddleware(
        RequestDelegate next,
        IMemoryCache cache,
        ILogger<RateLimitingMiddleware> logger,
        IConfiguration config)
    {
        _next = next;
        _cache = cache;
        _logger = logger;
        _maxRequestsPerMinute = config.GetValue<int>("RateLimit:MaxRequestsPerMinute", 60);
    }
    
    public async Task InvokeAsync(HttpContext context)
    {
        // 1. Get client identifier (API key or user ID)
        string clientId = GetClientIdentifier(context);
        
        // 2. Get rate limiting key for this minute
        string cacheKey = $"rate_limit:{clientId}:{DateTime.UtcNow:yyyyMMddHHmm}";
        
        // 3. Check current request count
        if (!_cache.TryGetValue(cacheKey, out int requestCount))
        {
            requestCount = 0;
        }
        
        // 4. Enforce rate limit
        if (requestCount >= _maxRequestsPerMinute)
        {
            _logger.LogWarning("Rate limit exceeded for client {ClientId}", clientId);
            
            context.Response.StatusCode = StatusCodes.Status429TooManyRequests;
            context.Response.Headers.Add("Retry-After", "60");
            
            await context.Response.WriteAsJsonAsync(new
            {
                error = "Rate limit exceeded",
                message = "Too many requests. Please try again later.",
                retryAfterSeconds = 60
            });
            
            return;
        }
        
        // 5. Increment request count
        _cache.Set(cacheKey, requestCount + 1, TimeSpan.FromMinutes(2));
        
        // 6. Add rate limit headers
        context.Response.Headers.Add("X-RateLimit-Limit", _maxRequestsPerMinute.ToString());
        context.Response.Headers.Add("X-RateLimit-Remaining", (_maxRequestsPerMinute - requestCount - 1).ToString());
        
        // 7. Continue with the request
        await _next(context);
    }
    
    private string GetClientIdentifier(HttpContext context)
    {
        // Implementation to extract API key or user ID
        // ...
    }
}
```

## ಪರೀಕ್ಷಾ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು

### 1. MCP ಸಾಧನಗಳ ಯುನಿಟ್ ಪರೀಕ್ಷೆ

ನಿಮ್ಮ ಸಾಧನಗಳನ್ನು ಪ್ರತ್ಯೇಕವಾಗಿ ಪರೀಕ್ಷಿಸಿ, ಬಾಹ್ಯ ಅವಲಂಬನೆಗಳನ್ನು ನಕಲಿಸಿ:

```typescript
// ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್ ಉದಾಹರಣೆ ಒಂದು ಉಪಕರಣ ಘಟಕ ಪರೀಕ್ಷೆ
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // ನಕಲಿ ಹವಾಮಾನ ಸೇವೆಯನ್ನು ರಚಿಸಿ
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // ನಕಲಿ ಅವಲಂಬನೆಯೊಂದಿಗೆ ಉಪಕರಣವನ್ನು ರಚಿಸಿ
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // ವ್ಯವಸ್ಥೆ ಮಾಡಿ
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // ಕಾರ್ಯನಿರ್ವಹಿಸಿ
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // ದೃಢೀಕರಿಸಿ
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // ವ್ಯವಸ್ಥೆ ಮಾಡಿ
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // ಕಾರ್ಯನಿರ್ವಹಿಸಿ ಮತ್ತು ದೃಢೀಕರಿಸಿ
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. ಇಂಟಿಗ್ರೇಶನ್ ಪರೀಕ್ಷೆ

ಗ್ರಾಹಕ ವಿನಂತಿಗಳಿಂದ ಸರ್ವರ್ ಪ್ರತಿಕ್ರಿಯೆಗಳವರೆಗೆ ಸಂಪೂರ್ಣ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ:

```python
# ಪೈಥಾನ್ ಇಂಟಿಗ್ರೇಶನ್ ಪರೀಕ್ಷಾ ಉದಾಹರಣೆ
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # ಪರೀಕ್ಷಾ ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸಿ
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # ಕ್ಲೈಂಟ್ ರಚಿಸಿ
        client = McpClient("http://localhost:5000")
        
        # ಸಾಧನ ಪತ್ತೆಮಾಡುವಿಕೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # ಸಾಧನ ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # ಸ್ವಚ್ಛಗೊಳಿಸಿ
        await server.stop()
```

## ಕಾರ್ಯಕ್ಷಮತೆ ಆಪ್ಟಿಮೈಜೆಷನ್

### 1. ಕ್ಯಾಶಿಂಗ್ ತಂತ್ರಗಳು

ವಿಲಂಬ ಮತ್ತು ಸಂಪನ್ಮೂಲ ಬಳಕೆಯನ್ನು ಕಡಿಮೆ ಮಾಡಲು ಸೂಕ್ತ ಕ್ಯಾಶಿಂಗ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ:

```csharp
// C# example with caching
public class CachedWeatherTool : ITool
{
    private readonly IWeatherService _weatherService;
    private readonly IDistributedCache _cache;
    private readonly ILogger<CachedWeatherTool> _logger;
    
    public CachedWeatherTool(
        IWeatherService weatherService,
        IDistributedCache cache,
        ILogger<CachedWeatherTool> logger)
    {
        _weatherService = weatherService;
        _cache = cache;
        _logger = logger;
    }
    
    public string Name => "weatherForecast";
    
    public async Task<ToolResponse> ExecuteAsync(IDictionary<string, object> parameters)
    {
        var location = parameters["location"].ToString();
        var days = Convert.ToInt32(parameters.GetValueOrDefault("days", 3));
        
        // Create cache key
        string cacheKey = $"weather:{location}:{days}";
        
        // Try to get from cache
        string cachedForecast = await _cache.GetStringAsync(cacheKey);
        if (!string.IsNullOrEmpty(cachedForecast))
        {
            _logger.LogInformation("Cache hit for weather forecast: {Location}", location);
            return new ToolResponse
            {
                Content = new List<ContentItem>
                {
                    new TextContent(cachedForecast)
                }
            };
        }
        
        // Cache miss - get from service
        _logger.LogInformation("Cache miss for weather forecast: {Location}", location);
        var forecast = await _weatherService.GetForecastAsync(location, days);
        string forecastJson = JsonSerializer.Serialize(forecast);
        
        // Store in cache (weather forecasts valid for 1 hour)
        await _cache.SetStringAsync(
            cacheKey,
            forecastJson,
            new DistributedCacheEntryOptions
            {
                AbsoluteExpirationRelativeToNow = TimeSpan.FromHours(1)
            });
        
        return new ToolResponse
        {
            Content = new List<ContentItem>
            {
                new TextContent(forecastJson)
            }
        };
    }
}
```

#### 2. ಅವಲಂಬನೆ ಇಂಜೆಕ್ಷನ್ ಮತ್ತು ಪರೀಕ್ಷಾ ಸಾಮರ್ಥ್ಯ

ನಿರ್ಮಾಪಕ ಇಂಜೆಕ್ಷನ್ ಮೂಲಕ ಅವಲಂಬನೆಗಳನ್ನು ಸ್ವೀಕರಿಸುವಂತೆ ಸಾಧನಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ, ಇದರಿಂದ ಅವುಗಳನ್ನು ಪರೀಕ್ಷಿಸಲು ಮತ್ತು ಸಂರಚಿಸಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

```java
// ಡಿಪೆಂಡೆನ್ಸಿ ಇಂಜೆಕ್ಷನ್‌ನೊಂದಿಗೆ ಜಾವಾ ಉದಾಹರಣೆ
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // ಕಾನ್ಸ್ಟ್ರಕ್ಟರ್ ಮೂಲಕ ಡಿಪೆಂಡೆನ್ಸಿಗಳನ್ನು ಇಂಜೆಕ್ಟ್ ಮಾಡಲಾಗಿದೆ
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // ಸಾಧನ ಅನುಷ್ಠಾನ
    // ...
}
```

#### 3. ಸಂಯೋಜನೀಯ ಸಾಧನಗಳು

ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ರಚಿಸಲು ಪರಸ್ಪರ ಸಂಯೋಜಿಸಬಹುದಾದ ಸಾಧನಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ:

```python
# ಸಂಯೋಜಿಸಬಹುದಾದ ಉಪಕರಣಗಳನ್ನು ತೋರಿಸುವ ಪೈಥಾನ್ ಉದಾಹರಣೆ
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # ಅನುಷ್ಠಾನ...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # ಈ ಉಪಕರಣವು dataFetch ಉಪಕರಣದಿಂದ ಫಲಿತಾಂಶಗಳನ್ನು ಬಳಸಬಹುದು
    async def execute_async(self, request):
        # ಅನುಷ್ಠಾನ...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # ಈ ಉಪಕರಣವು dataAnalysis ಉಪಕರಣದಿಂದ ಫಲಿತಾಂಶಗಳನ್ನು ಬಳಸಬಹುದು
    async def execute_async(self, request):
        # ಅನುಷ್ಠಾನ...
        pass

# ಈ ಉಪಕರಣಗಳನ್ನು ಸ್ವತಂತ್ರವಾಗಿ ಅಥವಾ ಕಾರ್ಯಪ್ರವಾಹದ ಭಾಗವಾಗಿ ಬಳಸಬಹುದು
```

### ಸ್ಕೀಮಾ ವಿನ್ಯಾಸ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು

ಸ್ಕೀಮಾ ಮಾದರಿ ಮತ್ತು ನಿಮ್ಮ ಸಾಧನದ ನಡುವೆ ಒಪ್ಪಂದವಾಗಿದೆ. ಚೆನ್ನಾಗಿ ವಿನ್ಯಾಸಗೊಳಿಸಿದ ಸ್ಕೀಮಾಗಳು ಉತ್ತಮ ಸಾಧನ ಬಳಕೆಯನ್ನು ಒದಗಿಸುತ್ತವೆ.

#### 1. ಸ್ಪಷ್ಟ ಪ್ಯಾರಾಮೀಟರ್ ವಿವರಣೆಗಳು

ಪ್ರತಿ ಪ್ಯಾರಾಮೀಟರ್‌ಗೆ ವಿವರಣಾತ್ಮಕ ಮಾಹಿತಿಯನ್ನು ಸದಾ ಸೇರಿಸಿ:

```csharp
public object GetSchema()
{
    return new {
        type = "object",
        properties = new {
            query = new { 
                type = "string", 
                description = "Search query text. Use precise keywords for better results." 
            },
            filters = new {
                type = "object",
                description = "Optional filters to narrow down search results",
                properties = new {
                    dateRange = new { 
                        type = "string", 
                        description = "Date range in format YYYY-MM-DD:YYYY-MM-DD" 
                    },
                    category = new { 
                        type = "string", 
                        description = "Category name to filter by" 
                    }
                }
            },
            limit = new { 
                type = "integer", 
                description = "Maximum number of results to return (1-50)",
                default = 10
            }
        },
        required = new[] { "query" }
    };
}
```

#### 2. ಮಾನ್ಯತೆ ನಿಯಮಗಳು

ಅಮಾನ್ಯ ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ತಡೆಯಲು ಮಾನ್ಯತೆ ನಿಯಮಗಳನ್ನು ಸೇರಿಸಿ:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // ಫಾರ್ಮ್ಯಾಟ್ ಮಾನ್ಯತೆ ಹೊಂದಿರುವ ಇಮೇಲ್ ಗುಣಲಕ್ಷಣ
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // ಸಂಖ್ಯಾತ್ಮಕ ನಿಯಮಗಳೊಂದಿಗೆ ವಯಸ್ಸಿನ ಗುಣಲಕ್ಷಣ
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // ಎನ್ಯೂಮರೇಟೆಡ್ ಗುಣಲಕ್ಷಣ
    Map<String, Object> subscription = new HashMap<>();
    subscription.put("type", "string");
    subscription.put("enum", Arrays.asList("free", "basic", "premium"));
    subscription.put("default", "free");
    subscription.put("description", "Subscription tier");
    
    properties.put("email", email);
    properties.put("age", age);
    properties.put("subscription", subscription);
    
    schema.put("properties", properties);
    schema.put("required", Arrays.asList("email"));
    
    return schema;
}
```

#### 3. ಸुसಂಗತ ಪ್ರತಿಕ್ರಿಯೆ ರಚನೆಗಳು

ಮಾದರಿಗಳು ಫಲಿತಾಂಶಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸುಲಭವಾಗುವಂತೆ ನಿಮ್ಮ ಪ್ರತಿಕ್ರಿಯೆ ರಚನೆಗಳಲ್ಲಿ ಸुसಂಗತತೆಯನ್ನು ಕಾಯ್ದುಕೊಳ್ಳಿ:

```python
async def execute_async(self, request):
    try:
        # ವಿನಂತಿಯನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ
        results = await self._search_database(request.parameters["query"])
        
        # ಯಾವಾಗಲೂ ಸತತವಾದ ರಚನೆಯನ್ನು ಹಿಂತಿರುಗಿಸಿ
        return ToolResponse(
            result={
                "matches": [self._format_item(item) for item in results],
                "totalCount": len(results),
                "queryTime": calculation_time_ms,
                "status": "success"
            }
        )
    except Exception as e:
        return ToolResponse(
            result={
                "matches": [],
                "totalCount": 0,
                "queryTime": 0,
                "status": "error",
                "error": str(e)
            }
        )
    
def _format_item(self, item):
    """Ensures each item has a consistent structure"""
    return {
        "id": item.id,
        "title": item.title,
        "summary": item.summary[:100] + "..." if len(item.summary) > 100 else item.summary,
        "url": item.url,
        "relevance": item.score
    }
```

### ದೋಷ ನಿರ್ವಹಣೆ

MCP ಸಾಧನಗಳ ವಿಶ್ವಾಸಾರ್ಹತೆಯನ್ನು ಕಾಯ್ದುಕೊಳ್ಳಲು ದೃಢವಾದ ದೋಷ ನಿರ್ವಹಣೆ ಅತ್ಯಾವಶ್ಯಕ.

#### 1. ಸೌಮ್ಯ ದೋಷ ನಿರ್ವಹಣೆ

ಸರಿಯಾದ ಮಟ್ಟಗಳಲ್ಲಿ ದೋಷಗಳನ್ನು ನಿರ್ವಹಿಸಿ ಮತ್ತು ಮಾಹಿತಿ ನೀಡುವ ಸಂದೇಶಗಳನ್ನು ಒದಗಿಸಿ:

```csharp
public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
{
    try
    {
        string fileId = request.Parameters.GetProperty("fileId").GetString();
        
        try
        {
            var fileData = await _fileService.GetFileAsync(fileId);
            return new ToolResponse { 
                Result = JsonSerializer.SerializeToElement(fileData) 
            };
        }
        catch (FileNotFoundException)
        {
            throw new ToolExecutionException($"File not found: {fileId}");
        }
        catch (UnauthorizedAccessException)
        {
            throw new ToolExecutionException("You don't have permission to access this file");
        }
        catch (Exception ex) when (ex is IOException || ex is TimeoutException)
        {
            _logger.LogError(ex, "Error accessing file {FileId}", fileId);
            throw new ToolExecutionException("Error accessing file: The service is temporarily unavailable");
        }
    }
    catch (JsonException)
    {
        throw new ToolExecutionException("Invalid file ID format");
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, "Unexpected error in FileAccessTool");
        throw new ToolExecutionException("An unexpected error occurred");
    }
}
```

#### 2. ರಚನಾತ್ಮಕ ದೋಷ ಪ್ರತಿಕ್ರಿಯೆಗಳು

ಸಾಧ್ಯವಾದರೆ ರಚನಾತ್ಮಕ ದೋಷ ಮಾಹಿತಿಯನ್ನು ಹಿಂತಿರುಗಿಸಿ:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // ಅನುಷ್ಠಾನ
    } catch (Exception ex) {
        Map<String, Object> errorResult = new HashMap<>();
        
        errorResult.put("success", false);
        
        if (ex instanceof ValidationException) {
            ValidationException validationEx = (ValidationException) ex;
            
            errorResult.put("errorType", "validation");
            errorResult.put("errorMessage", validationEx.getMessage());
            errorResult.put("validationErrors", validationEx.getErrors());
            
            return new ToolResponse.Builder()
                .setResult(errorResult)
                .build();
        }
        
        // ಇತರ ಹೊರತುಪಡಿಸುವಿಕೆಗಳನ್ನು ToolExecutionException ಆಗಿ ಮರುಸೂಸು
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. ಮರುಪ್ರಯತ್ನ ತಂತ್ರಜ್ಞಾನ

ತಾತ್ಕಾಲಿಕ ವೈಫಲ್ಯಗಳಿಗೆ ಸೂಕ್ತ ಮರುಪ್ರಯತ್ನ ತಂತ್ರಜ್ಞಾನವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # ಸೆಕೆಂಡುಗಳು
    
    while retry_count < max_retries:
        try:
            # ಬಾಹ್ಯ API ಅನ್ನು ಕರೆಮಾಡಿ
            return await self._call_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # ಘಾತಾಂಕ ಹಿಂಪಡೆಯುವಿಕೆ
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # ಅಸ್ಥಿರವಲ್ಲದ ದೋಷ, ಮರುಪ್ರಯತ್ನಿಸಬೇಡಿ
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### ಕಾರ್ಯಕ್ಷಮತೆ ಆಪ್ಟಿಮೈಜೆಷನ್

#### 1. ಕ್ಯಾಶಿಂಗ್

ಖರ್ಚುಬರಿದ ಕಾರ್ಯಾಚರಣೆಗಳಿಗೆ ಕ್ಯಾಶಿಂಗ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ:

```csharp
public class CachedDataTool : IMcpTool
{
    private readonly IDatabase _database;
    private readonly IMemoryCache _cache;
    
    public CachedDataTool(IDatabase database, IMemoryCache cache)
    {
        _database = database;
        _cache = cache;
    }
    
    public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
    {
        var query = request.Parameters.GetProperty("query").GetString();
        
        // Create cache key based on parameters
        var cacheKey = $"data_query_{ComputeHash(query)}";
        
        // Try to get from cache first
        if (_cache.TryGetValue(cacheKey, out var cachedResult))
        {
            return new ToolResponse { Result = cachedResult };
        }
        
        // Cache miss - perform actual query
        var result = await _database.QueryAsync(query);
        
        // Store in cache with expiration
        var cacheOptions = new MemoryCacheEntryOptions()
            .SetAbsoluteExpiration(TimeSpan.FromMinutes(15));
            
        _cache.Set(cacheKey, JsonSerializer.SerializeToElement(result), cacheOptions);
        
        return new ToolResponse { Result = JsonSerializer.SerializeToElement(result) };
    }
    
    private string ComputeHash(string input)
    {
        // Implementation to generate stable hash for cache key
    }
}
```

#### 2. ಅಸಿಂಕ್ರೋನಸ್ ಪ್ರೊಸೆಸಿಂಗ್

I/O-ಬಂಧಿತ ಕಾರ್ಯಗಳಿಗೆ ಅಸಿಂಕ್ರೋನಸ್ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಮಾದರಿಗಳನ್ನು ಬಳಸಿ:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // ದೀರ್ಘಕಾಲ ಚಲಿಸುವ ಕಾರ್ಯಗಳಿಗೆ, ತಕ್ಷಣ ಪ್ರಕ್ರಿಯೆ ID ಅನ್ನು ಹಿಂತಿರುಗಿಸಿ
        String processId = UUID.randomUUID().toString();
        
        // ಅಸಿಂಕ್ರೋನಸ್ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಪ್ರಾರಂಭಿಸಿ
        CompletableFuture.runAsync(() -> {
            try {
                // ದೀರ್ಘಕಾಲ ಚಲಿಸುವ ಕಾರ್ಯವನ್ನು ನಿರ್ವಹಿಸಿ
                documentService.processDocument(documentId);
                
                // ಸ್ಥಿತಿಯನ್ನು ನವೀಕರಿಸಿ (ಸಾಮಾನ್ಯವಾಗಿ ಡೇಟಾಬೇಸ್‌ನಲ್ಲಿ ಸಂಗ್ರಹಿಸಲಾಗುತ್ತದೆ)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // ಪ್ರಕ್ರಿಯೆ ID ಜೊತೆಗೆ ತಕ್ಷಣದ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಹಿಂತಿರುಗಿಸಿ
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // ಜೊತೆಯ ಸ್ಥಿತಿ ಪರಿಶೀಲನಾ ಸಾಧನ
    public class ProcessStatusTool implements Tool {
        @Override
        public ToolResponse execute(ToolRequest request) {
            String processId = request.getParameters().get("processId").asText();
            ProcessStatus status = processStatusRepository.getStatus(processId);
            
            return new ToolResponse.Builder().setResult(status).build();
        }
    }
}
```

#### 3. ಸಂಪನ್ಮೂಲ ನಿಯಂತ್ರಣ

ಏರಿಕೆಯನ್ನು ತಡೆಯಲು ಸಂಪನ್ಮೂಲ ನಿಯಂತ್ರಣವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # ಪ್ರತಿ ಸೆಕೆಂಡಿಗೆ 5 ವಿನಂತಿಗಳನ್ನು ಅನುಮತಿಸಿ
            bucket_size=10        # 10 ವಿನಂತಿಗಳವರೆಗೆ ಸ್ಫೋಟಗಳನ್ನು ಅನುಮತಿಸಿ
        )
    
    async def execute_async(self, request):
        # ನಾವು ಮುಂದುವರೆಯಬಹುದೇ ಅಥವಾ ಕಾಯಬೇಕೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # ಕಾಯುವ ಸಮಯ ತುಂಬಾ ಉದ್ದನೆಯಾಗಿದ್ದರೆ
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # ಸೂಕ್ತ ವಿಳಂಬ ಸಮಯಕ್ಕಾಗಿ ಕಾಯಿರಿ
                await asyncio.sleep(delay)
        
        # ಒಂದು ಟೋಕನ್ ಬಳಸಿ ವಿನಂತಿಯನ್ನು ಮುಂದುವರಿಸಿ
        self.rate_limiter.consume()
        
        # API ಅನ್ನು ಕರೆಮಾಡಿ
        result = await self._call_api(request.parameters)
        return ToolResponse(result=result)

class TokenBucketRateLimiter:
    def __init__(self, tokens_per_second, bucket_size):
        self.tokens_per_second = tokens_per_second
        self.bucket_size = bucket_size
        self.tokens = bucket_size
        self.last_refill = time.time()
        self.lock = asyncio.Lock()
    
    async def get_delay_time(self):
        async with self.lock:
            self._refill()
            if self.tokens >= 1:
                return 0
            
            # ಮುಂದಿನ ಟೋಕನ್ ಲಭ್ಯವಾಗುವವರೆಗೆ ಸಮಯವನ್ನು ಲೆಕ್ಕಹಾಕಿ
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # ಕಳೆದ ಸಮಯದ ಆಧಾರದ ಮೇಲೆ ಹೊಸ ಟೋಕನ್‌ಗಳನ್ನು ಸೇರಿಸಿ
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### ಭದ್ರತಾ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು

#### 1. ಇನ್‌ಪುಟ್ ಮಾನ್ಯತೆ

ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಮಾನ್ಯಗೊಳಿಸಿ:

```csharp
public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
{
    // Validate parameters exist
    if (!request.Parameters.TryGetProperty("query", out var queryProp))
    {
        throw new ToolExecutionException("Missing required parameter: query");
    }
    
    // Validate correct type
    if (queryProp.ValueKind != JsonValueKind.String)
    {
        throw new ToolExecutionException("Query parameter must be a string");
    }
    
    var query = queryProp.GetString();
    
    // Validate string content
    if (string.IsNullOrWhiteSpace(query))
    {
        throw new ToolExecutionException("Query parameter cannot be empty");
    }
    
    if (query.Length > 500)
    {
        throw new ToolExecutionException("Query parameter exceeds maximum length of 500 characters");
    }
    
    // Check for SQL injection attacks if applicable
    if (ContainsSqlInjection(query))
    {
        throw new ToolExecutionException("Invalid query: contains potentially unsafe SQL");
    }
    
    // Proceed with execution
    // ...
}
```

#### 2. ಪ್ರಾಧಿಕಾರ ಪರಿಶೀಲನೆಗಳು

ಸರಿಯಾದ ಪ್ರಾಧಿಕಾರ ಪರಿಶೀಲನೆಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // ವಿನಂತಿಯಿಂದ ಬಳಕೆದಾರರ ಸಂದರ್ಭವನ್ನು ಪಡೆಯಿರಿ
    UserContext user = request.getContext().getUserContext();
    
    // ಬಳಕೆದಾರರಿಗೆ ಅಗತ್ಯ ಅನುಮತಿಗಳು ಇದ್ದವೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // ನಿರ್ದಿಷ್ಟ ಸಂಪನ್ಮೂಲಗಳಿಗೆ, ಆ ಸಂಪನ್ಮೂಲದ ಪ್ರವೇಶವನ್ನು ಪರಿಶೀಲಿಸಿ
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // ಸಾಧನ ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆಯನ್ನು ಮುಂದುವರಿಸಿ
    // ...
}
```

#### 3. ಸಂವೇದನಾಶೀಲ ಡೇಟಾ ನಿರ್ವಹಣೆ

ಸಂವೇದನಾಶೀಲ ಡೇಟಾವನ್ನು ಜಾಗರೂಕತೆಯಿಂದ ನಿರ್ವಹಿಸಿ:

```python
class SecureDataTool(Tool):
    def get_schema(self):
        return {
            "type": "object",
            "properties": {
                "userId": {"type": "string"},
                "includeSensitiveData": {"type": "boolean", "default": False}
            },
            "required": ["userId"]
        }
    
    async def execute_async(self, request):
        user_id = request.parameters["userId"]
        include_sensitive = request.parameters.get("includeSensitiveData", False)
        
        # ಬಳಕೆದಾರ ಡೇಟಾವನ್ನು ಪಡೆಯಿರಿ
        user_data = await self.user_service.get_user_data(user_id)
        
        # ಸ್ಪಷ್ಟವಾಗಿ ವಿನಂತಿಸಲ್ಪಟ್ಟ ಮತ್ತು ಅನುಮತಿಸಲ್ಪಟ್ಟಿಲ್ಲದಿದ್ದರೆ ಸಂವೇದನಶೀಲ ಕ್ಷೇತ್ರಗಳನ್ನು ಫಿಲ್ಟರ್ ಮಾಡಿ
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # ವಿನಂತಿ ಸನ್ನಿವೇಶದಲ್ಲಿ ಅನುಮತಿ ಮಟ್ಟವನ್ನು ಪರಿಶೀಲಿಸಿ
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # ಮೂಲವನ್ನು ಬದಲಾಯಿಸುವುದನ್ನು ತಪ್ಪಿಸಲು ನಕಲನ್ನು ರಚಿಸಿ
        redacted = user_data.copy()
        
        # ನಿರ್ದಿಷ್ಟ ಸಂವೇದನಶೀಲ ಕ್ಷೇತ್ರಗಳನ್ನು ರೆಡ್ಯಾಕ್ಟ್ ಮಾಡಿ
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # ಒಳಗೊಂಡಿರುವ ಸಂವೇದನಶೀಲ ಡೇಟಾವನ್ನು ರೆಡ್ಯಾಕ್ಟ್ ಮಾಡಿ
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## MCP ಸಾಧನಗಳ ಪರೀಕ್ಷಾ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು

ಸಮಗ್ರ ಪರೀಕ್ಷೆ MCP ಸಾಧನಗಳು ಸರಿಯಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ, ಅಂಚು ಪ್ರಕರಣಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತವೆ ಮತ್ತು ವ್ಯವಸ್ಥೆಯ ಉಳಿದ ಭಾಗಗಳೊಂದಿಗೆ ಸರಿಯಾಗಿ ಸಂಯೋಜಿಸುತ್ತವೆ ಎಂಬುದನ್ನು ಖಚಿತಪಡಿಸುತ್ತದೆ.

### ಯುನಿಟ್ ಪರೀಕ್ಷೆ

#### 1. ಪ್ರತಿ ಸಾಧನವನ್ನು ಪ್ರತ್ಯೇಕವಾಗಿ ಪರೀಕ್ಷಿಸಿ

ಪ್ರತಿ ಸಾಧನದ ಕಾರ್ಯಕ್ಷಮತೆಯಿಗಾಗಿ ಕೇಂದ್ರೀಕೃತ ಪರೀಕ್ಷೆಗಳನ್ನು ರಚಿಸಿ:

```csharp
[Fact]
public async Task WeatherTool_ValidLocation_ReturnsCorrectForecast()
{
    // Arrange
    var mockWeatherService = new Mock<IWeatherService>();
    mockWeatherService
        .Setup(s => s.GetForecastAsync("Seattle", 3))
        .ReturnsAsync(new WeatherForecast(/* test data */));
    
    var tool = new WeatherForecastTool(mockWeatherService.Object);
    
    var request = new ToolRequest(
        toolName: "weatherForecast",
        parameters: JsonSerializer.SerializeToElement(new { 
            location = "Seattle", 
            days = 3 
        })
    );
    
    // Act
    var response = await tool.ExecuteAsync(request);
    
    // Assert
    Assert.NotNull(response);
    var result = JsonSerializer.Deserialize<WeatherForecast>(response.Result);
    Assert.Equal("Seattle", result.Location);
    Assert.Equal(3, result.DailyForecasts.Count);
}

[Fact]
public async Task WeatherTool_InvalidLocation_ThrowsToolExecutionException()
{
    // Arrange
    var mockWeatherService = new Mock<IWeatherService>();
    mockWeatherService
        .Setup(s => s.GetForecastAsync("InvalidLocation", It.IsAny<int>()))
        .ThrowsAsync(new LocationNotFoundException("Location not found"));
    
    var tool = new WeatherForecastTool(mockWeatherService.Object);
    
    var request = new ToolRequest(
        toolName: "weatherForecast",
        parameters: JsonSerializer.SerializeToElement(new { 
            location = "InvalidLocation", 
            days = 3 
        })
    );
    
    // Act & Assert
    var exception = await Assert.ThrowsAsync<ToolExecutionException>(
        () => tool.ExecuteAsync(request)
    );
    
    Assert.Contains("Location not found", exception.Message);
}
```

#### 2. ಸ್ಕೀಮಾ ಮಾನ್ಯತೆ ಪರೀಕ್ಷೆ

ಸ್ಕೀಮಾಗಳು ಮಾನ್ಯವಾಗಿವೆ ಮತ್ತು ನಿಯಮಗಳನ್ನು ಸರಿಯಾಗಿ ಜಾರಿಗೆ ತರುತ್ತವೆ ಎಂದು ಪರೀಕ್ಷಿಸಿ:

```java
@Test
public void testSchemaValidation() {
    // ಸಾಧನ ಉದಾಹರಣೆ ರಚಿಸಿ
    SearchTool searchTool = new SearchTool();
    
    // ಸ್ಕೀಮಾ ಪಡೆಯಿರಿ
    Object schema = searchTool.getSchema();
    
    // ಮಾನ್ಯತೆಗಾಗಿ ಸ್ಕೀಮಾವನ್ನು JSON ಗೆ ಪರಿವರ್ತಿಸಿ
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // ಸ್ಕೀಮಾ ಮಾನ್ಯ JSONSchema ಆಗಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // ಮಾನ್ಯವಾದ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // ಅಗತ್ಯವಿರುವ ಪ್ಯಾರಾಮೀಟರ್ ಇಲ್ಲದಿರುವುದನ್ನು ಪರೀಕ್ಷಿಸಿ
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // ಅಮಾನ್ಯ ಪ್ಯಾರಾಮೀಟರ್ ಪ್ರಕಾರವನ್ನು ಪರೀಕ್ಷಿಸಿ
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. ದೋಷ ನಿರ್ವಹಣೆ ಪರೀಕ್ಷೆಗಳು

ದೋಷ ಪರಿಸ್ಥಿತಿಗಳಿಗಾಗಿ ವಿಶೇಷ ಪರೀಕ್ಷೆಗಳನ್ನು ರಚಿಸಿ:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # ವ್ಯವಸ್ಥೆ ಮಾಡಿ
    tool = ApiTool(timeout=0.1)  # ತುಂಬಾ ಚಿಕ್ಕ ಸಮಯ ಮಿತಿ
    
    # ಸಮಯ ಮಿತಿ ಆಗುವ ವಿನಂತಿಯನ್ನು ನಕಲಿ ಮಾಡಿ
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # ಸಮಯ ಮಿತಿಗಿಂತ ಹೆಚ್ಚು
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # ಕಾರ್ಯನಿರ್ವಹಿಸಿ ಮತ್ತು ದೃಢೀಕರಿಸಿ
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # ಹೊರತುಪಡಿಸುವ ಸಂದೇಶವನ್ನು ಪರಿಶೀಲಿಸಿ
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # ವ್ಯವಸ್ಥೆ ಮಾಡಿ
    tool = ApiTool()
    
    # ದರ-ಮಿತಿಗೊಳಿಸಿದ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನಕಲಿ ಮಾಡಿ
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            status=429,
            headers={"Retry-After": "2"},
            body=json.dumps({"error": "Rate limit exceeded"})
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # ಕಾರ್ಯನಿರ್ವಹಿಸಿ ಮತ್ತು ದೃಢೀಕರಿಸಿ
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # ಹೊರತುಪಡಿಸುವಿಕೆ ದರ ಮಿತಿ ಮಾಹಿತಿಯನ್ನು ಹೊಂದಿದೆ ಎಂದು ಪರಿಶೀಲಿಸಿ
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### ಇಂಟಿಗ್ರೇಶನ್ ಪರೀಕ್ಷೆ

#### 1. ಸಾಧನ ಸರಪಳಿ ಪರೀಕ್ಷೆ

ನಿರೀಕ್ಷಿತ ಸಂಯೋಜನೆಗಳಲ್ಲಿ ಸಾಧನಗಳು ಒಟ್ಟಿಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ ಎಂದು ಪರೀಕ್ಷಿಸಿ:

```csharp
[Fact]
public async Task DataProcessingWorkflow_CompletesSuccessfully()
{
    // Arrange
    var dataFetchTool = new DataFetchTool(mockDataService.Object);
    var analysisTools = new DataAnalysisTool(mockAnalysisService.Object);
    var visualizationTool = new DataVisualizationTool(mockVisualizationService.Object);
    
    var toolRegistry = new ToolRegistry();
    toolRegistry.RegisterTool(dataFetchTool);
    toolRegistry.RegisterTool(analysisTools);
    toolRegistry.RegisterTool(visualizationTool);
    
    var workflowExecutor = new WorkflowExecutor(toolRegistry);
    
    // Act
    var result = await workflowExecutor.ExecuteWorkflowAsync(new[] {
        new ToolCall("dataFetch", new { source = "sales2023" }),
        new ToolCall("dataAnalysis", ctx => new { 
            data = ctx.GetResult("dataFetch"),
            analysis = "trend" 
        }),
        new ToolCall("dataVisualize", ctx => new {
            analysisResult = ctx.GetResult("dataAnalysis"),
            type = "line-chart"
        })
    });
    
    // Assert
    Assert.NotNull(result);
    Assert.True(result.Success);
    Assert.NotNull(result.GetResult("dataVisualize"));
    Assert.Contains("chartUrl", result.GetResult("dataVisualize").ToString());
}
```

#### 2. MCP ಸರ್ವರ್ ಪರೀಕ್ಷೆ

ಪೂರ್ಣ ಸಾಧನ ನೋಂದಣಿ ಮತ್ತು ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆಯಿಂದ MCP ಸರ್ವರ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಿ:

```java
@SpringBootTest
@AutoConfigureMockMvc
public class McpServerIntegrationTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @Autowired
    private ObjectMapper objectMapper;
    
    @Test
    public void testToolDiscovery() throws Exception {
        // ಡಿಸ್ಕವರಿ ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಿ
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // ಟೂಲ್ ವಿನಂತಿಯನ್ನು ರಚಿಸಿ
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // ವಿನಂತಿಯನ್ನು ಕಳುಹಿಸಿ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // ಅಮಾನ್ಯ ಟೂಲ್ ವಿನಂತಿಯನ್ನು ರಚಿಸಿ
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // "b" ಪರಿಮಾಣ ಕಾಣೆಯಾಗಿದೆ
        request.put("parameters", parameters);
        
        // ವಿನಂತಿಯನ್ನು ಕಳುಹಿಸಿ ಮತ್ತು ದೋಷ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. ಎಂಡ್-ಟು-ಎಂಡ್ ಪರೀಕ್ಷೆ

ಮಾದರಿ ಪ್ರಾಂಪ್ಟ್‌ನಿಂದ ಸಾಧನ ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆಗೆ ಸಂಪೂರ್ಣ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # ವ್ಯವಸ್ಥೆ - MCP ಕ್ಲೈಂಟ್ ಮತ್ತು ನಕಲಿ ಮಾದರಿಯನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # ನಕಲಿ ಮಾದರಿ ಪ್ರತಿಕ್ರಿಯೆಗಳು
    mock_model = MockLanguageModel([
        MockResponse(
            "What's the weather in Seattle?",
            tool_calls=[{
                "tool_name": "weatherForecast",
                "parameters": {"location": "Seattle", "days": 3}
            }]
        ),
        MockResponse(
            "Here's the weather forecast for Seattle:\n- Today: 65°F, Partly Cloudy\n- Tomorrow: 68°F, Sunny\n- Day after: 62°F, Rain",
            tool_calls=[]
        )
    ])
    
    # ನಕಲಿ ಹವಾಮಾನ ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆ
    with aioresponses() as mocked:
        mocked.post(
            "http://localhost:5000/mcp/execute",
            payload={
                "result": {
                    "location": "Seattle",
                    "forecast": [
                        {"date": "2023-06-01", "temperature": 65, "conditions": "Partly Cloudy"},
                        {"date": "2023-06-02", "temperature": 68, "conditions": "Sunny"},
                        {"date": "2023-06-03", "temperature": 62, "conditions": "Rain"}
                    ]
                }
            }
        )
        
        # ಕಾರ್ಯನಿರ್ವಹಿಸಿ
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # ದೃಢೀಕರಿಸಿ
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### ಕಾರ್ಯಕ್ಷಮತೆ ಪರೀಕ್ಷೆ

#### 1. ಲೋಡ್ ಪರೀಕ್ಷೆ

ನಿಮ್ಮ MCP ಸರ್ವರ್ ಎಷ್ಟು ಸಮಕಾಲೀನ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸಬಹುದು ಎಂದು ಪರೀಕ್ಷಿಸಿ:

```csharp
[Fact]
public async Task McpServer_HandlesHighConcurrency()
{
    // Arrange
    var server = new McpServer(
        name: "TestServer",
        version: "1.0",
        maxConcurrentRequests: 100
    );
    
    server.RegisterTool(new FastExecutingTool());
    await server.StartAsync();
    
    var client = new McpClient("http://localhost:5000");
    
    // Act
    var tasks = new List<Task<McpResponse>>();
    for (int i = 0; i < 1000; i++)
    {
        tasks.Add(client.ExecuteToolAsync("fastTool", new { iteration = i }));
    }
    
    var results = await Task.WhenAll(tasks);
    
    // Assert
    Assert.Equal(1000, results.Length);
    Assert.All(results, r => Assert.NotNull(r));
}
```

#### 2. ಸ್ಟ್ರೆಸ್ ಪರೀಕ್ಷೆ

ಅತ್ಯಂತ ಲೋಡ್ ಅಡಿಯಲ್ಲಿ ವ್ಯವಸ್ಥೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // ಒತ್ತಡ ಪರೀಕ್ಷೆಗಾಗಿ JMeter ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // JMeter ಪರೀಕ್ಷಾ ಯೋಜನೆಯನ್ನು ಸಂರಚಿಸಿ
    HashTree testPlanTree = new HashTree();
    
    // ಪರೀಕ್ಷಾ ಯೋಜನೆ, ಥ್ರೆಡ್ ಗುಂಪು, ಸ್ಯಾಂಪ್ಲರ್‌ಗಳು ಇತ್ಯಾದಿ ರಚಿಸಿ
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // ಸಾಧನ ಕಾರ್ಯಾಚರಣೆಗೆ HTTP ಸ್ಯಾಂಪ್ಲರ್ ಸೇರಿಸಿ
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // ಶ್ರೋತೃಗಳನ್ನು ಸೇರಿಸಿ
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // ಪರೀಕ್ಷೆಯನ್ನು ಚಾಲನೆ ಮಾಡಿ
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // ಫಲಿತಾಂಶಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // ಸರಾಸರಿ ಪ್ರತಿಕ್ರಿಯೆ ಸಮಯ < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90ನೇ ಶತಮಾನ < 500ms
}
```

#### 3. ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ಪ್ರೊಫೈಲಿಂಗ್

ದೀರ್ಘಕಾಲದ ಕಾರ್ಯಕ್ಷಮತೆ ವಿಶ್ಲೇಷಣೆಗೆ ಮೇಲ್ವಿಚಾರಣೆಯನ್ನು ಸ್ಥಾಪಿಸಿ:

```python
# MCP ಸರ್ವರ್‌ಗಾಗಿ ಮಾನಿಟರಿಂಗ್ ಅನ್ನು ಸಂರಚಿಸಿ
def configure_monitoring(server):
    # ಪ್ರೊಮಿಥಿಯಸ್ ಮೆಟ್ರಿಕ್ಸ್ ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ
    prometheus_metrics = {
        "request_count": Counter("mcp_requests_total", "Total MCP requests"),
        "request_latency": Histogram(
            "mcp_request_duration_seconds", 
            "Request duration in seconds",
            buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 2.5, 5.0, 10.0]
        ),
        "tool_execution_count": Counter(
            "mcp_tool_executions_total", 
            "Tool execution count",
            labelnames=["tool_name"]
        ),
        "tool_execution_latency": Histogram(
            "mcp_tool_duration_seconds", 
            "Tool execution duration in seconds",
            labelnames=["tool_name"],
            buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 2.5, 5.0, 10.0]
        ),
        "tool_errors": Counter(
            "mcp_tool_errors_total",
            "Tool execution errors",
            labelnames=["tool_name", "error_type"]
        )
    }
    
    # ಸಮಯ ಮತ್ತು ಮೆಟ್ರಿಕ್ಸ್ ದಾಖಲಿಸಲು ಮಧ್ಯವರ್ತಿ ಸೇರಿಸಿ
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # ಮೆಟ್ರಿಕ್ಸ್ ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಬಹಿರಂಗಪಡಿಸಿ
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## MCP ವರ್ಕ್‌ಫ್ಲೋ ವಿನ್ಯಾಸ ಮಾದರಿಗಳು

ಚೆನ್ನಾಗಿ ವಿನ್ಯಾಸಗೊಳಿಸಿದ MCP ವರ್ಕ್‌ಫ್ಲೋಗಳು ಕಾರ್ಯಕ್ಷಮತೆ, ವಿಶ್ವಾಸಾರ್ಹತೆ ಮತ್ತು ನಿರ್ವಹಣಾ ಸುಲಭತೆಯನ್ನು ಸುಧಾರಿಸುತ್ತವೆ. ಅನುಸರಿಸಬೇಕಾದ ಪ್ರಮುಖ ಮಾದರಿಗಳು ಇಲ್ಲಿವೆ:

### 1. ಸಾಧನ ಸರಪಳಿ ಮಾದರಿ

ಪ್ರತಿ ಸಾಧನದ ಔಟ್‌ಪುಟ್ ಮುಂದಿನ ಸಾಧನದ ಇನ್‌ಪುಟ್ ಆಗುವಂತೆ ಸರಣಿಯಲ್ಲಿ ಅನೇಕ ಸಾಧನಗಳನ್ನು ಸಂಪರ್ಕಿಸಿ:

```python
# ಪೈಥಾನ್ ಚೈನ್ ಆಫ್ ಟೂಲ್ಸ್ ಅನುಷ್ಠಾನ
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # ಕ್ರಮವಾಗಿ ಕಾರ್ಯಗತಗೊಳಿಸಲು ಟೂಲ್ ಹೆಸರುಗಳ ಪಟ್ಟಿ
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # ಸರಣಿಯಲ್ಲಿ ಪ್ರತಿ ಟೂಲ್ ಅನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ, ಹಿಂದಿನ ಫಲಿತಾಂಶವನ್ನು ಹಂಚಿಕೊಳ್ಳಿ
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # ಫಲಿತಾಂಶವನ್ನು ಸಂಗ್ರಹಿಸಿ ಮತ್ತು ಮುಂದಿನ ಟೂಲ್‌ಗೆ ಇನ್ಪುಟ್ ಆಗಿ ಬಳಸಿ
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# ಉದಾಹರಣೆಯ ಬಳಕೆ
data_processing_chain = ChainWorkflow([
    "dataFetch",
    "dataCleaner",
    "dataAnalyzer",
    "dataVisualizer"
])

result = await data_processing_chain.execute(
    mcp_client,
    {"source": "sales_database", "table": "transactions"}
)
```

### 2. ಡಿಸ್ಪ್ಯಾಚರ್ ಮಾದರಿ

ಇನ್‌ಪುಟ್ ಆಧಾರಿತವಾಗಿ ವಿಶೇಷ ಸಾಧನಗಳಿಗೆ ಡಿಸ್ಪ್ಯಾಚ್ ಮಾಡುವ ಕೇಂದ್ರಿತ ಸಾಧನವನ್ನು ಬಳಸಿ:

```csharp
public class ContentDispatcherTool : IMcpTool
{
    private readonly IMcpClient _mcpClient;
    
    public ContentDispatcherTool(IMcpClient mcpClient)
    {
        _mcpClient = mcpClient;
    }
    
    public string Name => "contentProcessor";
    public string Description => "Processes content of various types";
    
    public object GetSchema()
    {
        return new {
            type = "object",
            properties = new {
                content = new { type = "string" },
                contentType = new { 
                    type = "string",
                    enum = new[] { "text", "html", "markdown", "csv", "code" }
                },
                operation = new { 
                    type = "string",
                    enum = new[] { "summarize", "analyze", "extract", "convert" }
                }
            },
            required = new[] { "content", "contentType", "operation" }
        };
    }
    
    public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
    {
        var content = request.Parameters.GetProperty("content").GetString();
        var contentType = request.Parameters.GetProperty("contentType").GetString();
        var operation = request.Parameters.GetProperty("operation").GetString();
        
        // Determine which specialized tool to use
        string targetTool = DetermineTargetTool(contentType, operation);
        
        // Forward to the specialized tool
        var specializedResponse = await _mcpClient.ExecuteToolAsync(
            targetTool,
            new { content, options = GetOptionsForTool(targetTool, operation) }
        );
        
        return new ToolResponse { Result = specializedResponse.Result };
    }
    
    private string DetermineTargetTool(string contentType, string operation)
    {
        return (contentType, operation) switch
        {
            ("text", "summarize") => "textSummarizer",
            ("text", "analyze") => "textAnalyzer",
            ("html", _) => "htmlProcessor",
            ("markdown", _) => "markdownProcessor",
            ("csv", _) => "csvProcessor",
            ("code", _) => "codeAnalyzer",
            _ => throw new ToolExecutionException($"No tool available for {contentType}/{operation}")
        };
    }
    
    private object GetOptionsForTool(string toolName, string operation)
    {
        // Return appropriate options for each specialized tool
        return toolName switch
        {
            "textSummarizer" => new { length = "medium" },
            "htmlProcessor" => new { cleanUp = true, operation },
            // Options for other tools...
            _ => new { }
        };
    }
}
```

### 3. ಸಮಾಂತರ ಪ್ರೊಸೆಸಿಂಗ್ ಮಾದರಿ

ಕಾರ್ಯಕ್ಷಮತೆಯಿಗಾಗಿ ಅನೇಕ ಸಾಧನಗಳನ್ನು ಸಮಕಾಲೀನವಾಗಿ ಕಾರ್ಯಗತಗೊಳಿಸಿ:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // ಹಂತ 1: ಡೇಟಾಸೆಟ್ ಮೆಟಾಡೇಟಾ ಪಡೆಯಿರಿ (ಸಮಕಾಲೀನ)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // ಹಂತ 2: ಅನೇಕ ವಿಶ್ಲೇಷಣೆಗಳನ್ನು ಸಮಾಂತರವಾಗಿ ಪ್ರಾರಂಭಿಸಿ
        CompletableFuture<ToolResponse> statisticalAnalysis = CompletableFuture.supplyAsync(() ->
            mcpClient.executeTool("statisticalAnalysis", Map.of(
                "datasetId", datasetId,
                "type", "comprehensive"
            ))
        );
        
        CompletableFuture<ToolResponse> correlationAnalysis = CompletableFuture.supplyAsync(() ->
            mcpClient.executeTool("correlationAnalysis", Map.of(
                "datasetId", datasetId,
                "method", "pearson"
            ))
        );
        
        CompletableFuture<ToolResponse> outlierDetection = CompletableFuture.supplyAsync(() ->
            mcpClient.executeTool("outlierDetection", Map.of(
                "datasetId", datasetId,
                "sensitivity", "medium"
            ))
        );
        
        // ಎಲ್ಲಾ ಸಮಾಂತರ ಕಾರ್ಯಗಳು ಪೂರ್ಣಗೊಳ್ಳುವವರೆಗೆ ಕಾಯಿರಿ
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // ಪೂರ್ಣಗೊಳ್ಳುವವರೆಗೆ ಕಾಯಿರಿ
        
        // ಹಂತ 3: ಫಲಿತಾಂಶಗಳನ್ನು ಸಂಯೋಜಿಸಿ
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // ಹಂತ 4: ಸಾರಾಂಶ ವರದಿ ರಚಿಸಿ
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // ಸಂಪೂರ್ಣ ಕಾರ್ಯಪ್ರವಾಹ ಫಲಿತಾಂಶವನ್ನು ಹಿಂತಿರುಗಿಸಿ
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. ದೋಷ ಪುನಃಪಡೆಯುವಿಕೆ ಮಾದರಿ

ಸಾಧನ ವೈಫಲ್ಯಗಳಿಗೆ ಸೌಮ್ಯ ಬ್ಯಾಕ್ಅಪ್‌ಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # ಮೊದಲು ಪ್ರಾಥಮಿಕ ಸಾಧನವನ್ನು ಪ್ರಯತ್ನಿಸಿ
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # ವಿಫಲತೆಯನ್ನು ಲಾಗ್ ಮಾಡಿ
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # ದ್ವಿತೀಯ ಸಾಧನಕ್ಕೆ ಹಿಂತಿರುಗಿ
            try:
                # ಹಿಂತಿರುಗುವ ಸಾಧನಕ್ಕೆ ಪರಿಮಾಣಗಳನ್ನು ಪರಿವರ್ತಿಸಲು ಅಗತ್ಯವಿರಬಹುದು
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # ಎರಡೂ ಸಾಧನಗಳು ವಿಫಲವಾದವು
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # ಈ ಅನುಷ್ಠಾನವು ನಿರ್ದಿಷ್ಟ ಸಾಧನಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ
        # ಈ ಉದಾಹರಣೆಗೆ, ನಾವು ಮೂಲ ಪರಿಮಾಣಗಳನ್ನು ಮಾತ್ರ ಹಿಂತಿರುಗಿಸುವೆವು
        return params

# ಉದಾಹರಣೆಯ ಬಳಕೆ
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # ಪ್ರಾಥಮಿಕ (ಪಾವತಿಸಿದ) ಹವಾಮಾನ API
        "basicWeatherService",    # ಹಿಂತಿರುಗುವ (ಉಚಿತ) ಹವಾಮಾನ API
        {"location": location}
    )
```

### 5. ವರ್ಕ್‌ಫ್ಲೋ ಸಂಯೋಜನೆ ಮಾದರಿ

ಸರಳವಾದ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ಸಂಯೋಜಿಸಿ ಸಂಕೀರ್ಣ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ನಿರ್ಮಿಸಿ:

```csharp
public class CompositeWorkflow : IWorkflow
{
    private readonly List<IWorkflow> _workflows;
    
    public CompositeWorkflow(IEnumerable<IWorkflow> workflows)
    {
        _workflows = new List<IWorkflow>(workflows);
    }
    
    public async Task<WorkflowResult> ExecuteAsync(WorkflowContext context)
    {
        var results = new Dictionary<string, object>();
        
        foreach (var workflow in _workflows)
        {
            var workflowResult = await workflow.ExecuteAsync(context);
            
            // Store each workflow's result
            results[workflow.Name] = workflowResult;
            
            // Update context with the result for the next workflow
            context = context.WithResult(workflow.Name, workflowResult);
        }
        
        return new WorkflowResult(results);
    }
    
    public string Name => "CompositeWorkflow";
    public string Description => "Executes multiple workflows in sequence";
}

// Example usage
var documentWorkflow = new CompositeWorkflow(new IWorkflow[] {
    new DocumentFetchWorkflow(),
    new DocumentProcessingWorkflow(),
    new InsightGenerationWorkflow(),
    new ReportGenerationWorkflow()
});

var result = await documentWorkflow.ExecuteAsync(new WorkflowContext {
    Parameters = new { documentId = "12345" }
});
```

# MCP ಸರ್ವರ್‌ಗಳ ಪರೀಕ್ಷೆ: ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು ಮತ್ತು ಪ್ರಮುಖ ಸಲಹೆಗಳು

## ಅವಲೋಕನ

ಪರೀಕ್ಷೆ ವಿಶ್ವಾಸಾರ್ಹ, ಉನ್ನತ ಗುಣಮಟ್ಟದ MCP ಸರ್ವರ್‌ಗಳನ್ನು ಅಭಿವೃದ್ಧಿಪಡಿಸುವ ಪ್ರಮುಖ ಅಂಶವಾಗಿದೆ. ಈ ಮಾರ್ಗದರ್ಶಿ ನಿಮ್ಮ MCP ಸರ್ವರ್‌ಗಳನ್ನು ಅಭಿವೃದ್ಧಿ ಜೀವನಚರ್ಯೆಯಲ್ಲಿ ಯುನಿಟ್ ಪರೀಕ್ಷೆಗಳಿಂದ ಇಂಟಿಗ್ರೇಶನ್ ಪರೀಕ್ಷೆ ಮತ್ತು ಎಂಡ್-ಟು-ಎಂಡ್ ಮಾನ್ಯತೆವರೆಗೆ ಸಮಗ್ರ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು ಮತ್ತು ಸಲಹೆಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.

## MCP ಸರ್ವರ್‌ಗಳಿಗೆ ಪರೀಕ್ಷೆ ಏಕೆ ಮುಖ್ಯ

MCP ಸರ್ವರ್‌ಗಳು AI ಮಾದರಿಗಳು ಮತ್ತು ಗ್ರಾಹಕ ಅಪ್ಲಿಕೇಶನ್‌ಗಳ ನಡುವೆ ಪ್ರಮುಖ ಮಧ್ಯವರ್ತಿಗಳಾಗಿವೆ. ಸಂಪೂರ್ಣ ಪರೀಕ್ಷೆ ಖಚಿತಪಡಿಸುತ್ತದೆ:

- ಉತ್ಪಾದನಾ ಪರಿಸರಗಳಲ್ಲಿ ವಿಶ್ವಾಸಾರ್ಹತೆ
- ವಿನಂತಿಗಳು ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಗಳ ಸರಿಯಾದ ನಿರ್ವಹಣೆ
- MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್‌ಗಳ ಸರಿಯಾದ ಅನುಷ್ಠಾನ
- ವೈಫಲ್ಯಗಳು ಮತ್ತು ಅಂಚು ಪ್ರಕರಣಗಳ ವಿರುದ್ಧ ಸ್ಥೈರ್ಯ
- ವಿವಿಧ ಲೋಡ್‌ಗಳ ಅಡಿಯಲ್ಲಿ ಸತತ ಕಾರ್ಯಕ್ಷಮತೆ

## MCP ಸರ್ವರ್‌ಗಳಿಗಾಗಿ ಯುನಿಟ್ ಪರೀಕ್ಷೆ

### ಯುನಿಟ್ ಪರೀಕ್ಷೆ (ಮ
```yaml
name: MCP Server Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Runtime
      uses: actions/setup-dotnet@v1
      with:
        dotnet-version: '8.0.x'
    
    - name: Restore dependencies
      run: dotnet restore
    
    - name: Build
      run: dotnet build --no-restore
    
    - name: Unit Tests
      run: dotnet test --no-build --filter Category=Unit
    
    - name: Integration Tests
      run: dotnet test --no-build --filter Category=Integration
      
    - name: Performance Tests
      run: dotnet run --project tests/PerformanceTests/PerformanceTests.csproj
```

## MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್ ಅನುಕೂಲತೆಯ ಪರೀಕ್ಷೆ

ನಿಮ್ಮ ಸರ್ವರ್ ಸರಿಯಾಗಿ MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುತ್ತಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ.

### ಪ್ರಮುಖ ಅನುಕೂಲತಾ ಕ್ಷೇತ್ರಗಳು

1. **API ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳು**: ಅಗತ್ಯ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ (/resources, /tools, ಇತ್ಯಾದಿ)
2. **ವಿನಂತಿ/ಪ್ರತಿಕ್ರಿಯೆ ಫಾರ್ಮ್ಯಾಟ್**: ಸ್ಕೀಮಾ ಅನುಕೂಲತೆಯನ್ನು ಮಾನ್ಯಗೊಳಿಸಿ
3. **ದೋಷ ಕೋಡ್‌ಗಳು**: ವಿವಿಧ ಸಂದರ್ಭಗಳಿಗೆ ಸರಿಯಾದ ಸ್ಥಿತಿ ಕೋಡ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
4. **ವಿಷಯ ಪ್ರಕಾರಗಳು**: ವಿಭಿನ್ನ ವಿಷಯ ಪ್ರಕಾರಗಳ ನಿರ್ವಹಣೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ
5. **ಪ್ರಮಾಣೀಕರಣ ಪ್ರಕ್ರಿಯೆ**: ಸ್ಪೆಕ್ ಅನುಕೂಲತೆಯ ಪ್ರಾಮಾಣೀಕರಣ ಯಂತ್ರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ

### ಅನುಕೂಲತಾ ಪರೀಕ್ಷಾ ಸರಣಿ

```csharp
[Fact]
public async Task Server_ResourceEndpoint_ReturnsCorrectSchema()
{
    // Arrange
    var client = new HttpClient();
    client.DefaultRequestHeaders.Add("Authorization", "Bearer test-token");
    
    // Act
    var response = await client.GetAsync("http://localhost:5000/api/resources");
    var content = await response.Content.ReadAsStringAsync();
    var resources = JsonSerializer.Deserialize<ResourceList>(content);
    
    // Assert
    Assert.Equal(HttpStatusCode.OK, response.StatusCode);
    Assert.NotNull(resources);
    Assert.All(resources.Resources, resource => 
    {
        Assert.NotNull(resource.Id);
        Assert.NotNull(resource.Type);
        // Additional schema validation
    });
}
```

## ಪರಿಣಾಮಕಾರಿ MCP ಸರ್ವರ್ ಪರೀಕ್ಷೆಗೆ ಟಾಪ್ 10 ಸಲಹೆಗಳು

1. **ಟೂಲ್ ವ್ಯಾಖ್ಯಾನಗಳನ್ನು ಪ್ರತ್ಯೇಕವಾಗಿ ಪರೀಕ್ಷಿಸಿ**: ಟೂಲ್ ಲಾಜಿಕ್‌ನಿಂದ ಸ್ವತಂತ್ರವಾಗಿ ಸ್ಕೀಮಾ ವ್ಯಾಖ್ಯಾನಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
2. **ಪ್ಯಾರಾಮೀಟರ್‌ಗೊಳಿಸಿದ ಪರೀಕ್ಷೆಗಳನ್ನು ಬಳಸಿ**: ವಿವಿಧ ಇನ್ಪುಟ್‌ಗಳೊಂದಿಗೆ, ಅತಿ ಮಿತಿಯ ಪ್ರಕರಣಗಳನ್ನು ಸೇರಿಸಿ, ಟೂಲ್‌ಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ
3. **ದೋಷ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ**: ಎಲ್ಲಾ ಸಾಧ್ಯ ದೋಷ ಪರಿಸ್ಥಿತಿಗಳಿಗಾಗಿ ಸರಿಯಾದ ದೋಷ ನಿರ್ವಹಣೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
4. **ಅಧಿಕಾರ ಲಾಜಿಕ್ ಪರೀಕ್ಷಿಸಿ**: ವಿಭಿನ್ನ ಬಳಕೆದಾರ ಪಾತ್ರಗಳಿಗೆ ಸರಿಯಾದ ಪ್ರವೇಶ ನಿಯಂತ್ರಣವನ್ನು ಖಚಿತಪಡಿಸಿ
5. **ಪರೀಕ್ಷಾ ವ್ಯಾಪ್ತಿಯನ್ನು ಗಮನಿಸಿ**: ಪ್ರಮುಖ ಮಾರ್ಗದ ಕೋಡ್‌ನ ಹೆಚ್ಚಿನ ವ್ಯಾಪ್ತಿಯನ್ನು ಗುರಿಯಾಗಿಡಿ
6. **ಸ್ಟ್ರೀಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ**: ಸ್ಟ್ರೀಮಿಂಗ್ ವಿಷಯದ ಸರಿಯಾದ ನಿರ್ವಹಣೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
7. **ನೆಟ್‌ವರ್ಕ್ ಸಮಸ್ಯೆಗಳನ್ನು ಅನುಕರಿಸಿ**: ದುರ್ಬಲ ನೆಟ್‌ವರ್ಕ್ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ ವರ್ತನೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ
8. **ಸಂಪನ್ಮೂಲ ಮಿತಿಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ**: ಕೊಟಾ ಅಥವಾ ದರ ಮಿತಿಗಳನ್ನು ತಲುಪಿದಾಗ ವರ್ತನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
9. **ರಿಗ್ರೆಶನ್ ಪರೀಕ್ಷೆಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸಿ**: ಪ್ರತಿಯೊಂದು ಕೋಡ್ ಬದಲಾವಣೆಯಲ್ಲೂ ನಡೆಯುವ ಸರಣಿಯನ್ನು ನಿರ್ಮಿಸಿ
10. **ಪರೀಕ್ಷಾ ಪ್ರಕರಣಗಳನ್ನು ದಾಖಲೆ ಮಾಡಿ**: ಪರೀಕ್ಷಾ ಸಂದರ್ಭಗಳ ಸ್ಪಷ್ಟ ದಾಖಲೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ

## ಸಾಮಾನ್ಯ ಪರೀಕ್ಷಾ ತಪ್ಪುಗಳು

- **ಹ್ಯಾಪಿ ಪಾತ್ ಪರೀಕ್ಷೆಯ ಮೇಲೆ ಹೆಚ್ಚು ಅವಲಂಬನೆ**: ದೋಷ ಪ್ರಕರಣಗಳನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಪರೀಕ್ಷಿಸುವುದನ್ನು ಖಚಿತಪಡಿಸಿ
- **ಕಾರ್ಯಕ್ಷಮತೆ ಪರೀಕ್ಷೆಯನ್ನು ನಿರ್ಲಕ್ಷಿಸುವುದು**: ಉತ್ಪಾದನೆಗೆ ಪ್ರಭಾವ ಬೀರುವ ಮೊದಲು ಬಾಟಲ್‌ನೆಕ್‌ಗಳನ್ನು ಗುರುತಿಸಿ
- **ಒಂಟಿ ಪರೀಕ್ಷೆ ಮಾತ್ರ**: ಯೂನಿಟ್, ಇಂಟಿಗ್ರೇಶನ್ ಮತ್ತು E2E ಪರೀಕ್ಷೆಗಳನ್ನು ಸಂಯೋಜಿಸಿ
- **ಅಪೂರ್ಣ API ವ್ಯಾಪ್ತಿ**: ಎಲ್ಲಾ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳು ಮತ್ತು ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಪರೀಕ್ಷಿಸಲಾಗಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿ
- **ಅಸಮಾನ ಪರೀಕ್ಷಾ ಪರಿಸರಗಳು**: ಸತತ ಪರೀಕ್ಷಾ ಪರಿಸರಗಳನ್ನು ಖಚಿತಪಡಿಸಲು ಕಂಟೈನರ್‌ಗಳನ್ನು ಬಳಸಿ

## ಸಮಾರೋಪ

ನಂಬಿಕಯೋಗ್ಯ, ಉನ್ನತ ಗುಣಮಟ್ಟದ MCP ಸರ್ವರ್‌ಗಳನ್ನು ಅಭಿವೃದ್ಧಿಪಡಿಸಲು ಸಮಗ್ರ ಪರೀಕ್ಷಾ ತಂತ್ರವು ಅಗತ್ಯ. ಈ ಮಾರ್ಗದರ್ಶಿಯಲ್ಲಿ ವಿವರಿಸಿದ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು ಮತ್ತು ಸಲಹೆಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವ ಮೂಲಕ, ನಿಮ್ಮ MCP ಅನುಷ್ಠಾನಗಳು ಅತ್ಯುತ್ತಮ ಗುಣಮಟ್ಟ, ನಂಬಿಕೆ ಮತ್ತು ಕಾರ್ಯಕ್ಷಮತೆ ಮಾನದಂಡಗಳನ್ನು ಪೂರೈಸುತ್ತವೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಬಹುದು.

## ಪ್ರಮುಖ ಅಂಶಗಳು

1. **ಟೂಲ್ ವಿನ್ಯಾಸ**: ಏಕ ಜವಾಬ್ದಾರಿ ತತ್ವವನ್ನು ಅನುಸರಿಸಿ, ಡಿಪೆಂಡೆನ್ಸಿ ಇಂಜೆಕ್ಷನ್ ಬಳಸಿ, ಮತ್ತು ಸಂಯೋಜನೀಯತೆಯಿಗಾಗಿ ವಿನ್ಯಾಸ ಮಾಡಿ
2. **ಸ್ಕೀಮಾ ವಿನ್ಯಾಸ**: ಸ್ಪಷ್ಟ, ಚೆನ್ನಾಗಿ ದಾಖಲೆ ಮಾಡಲಾದ ಸ್ಕೀಮಾಗಳನ್ನು ಸರಿಯಾದ ಮಾನ್ಯತೆ ನಿಯಮಗಳೊಂದಿಗೆ ರಚಿಸಿ
3. **ದೋಷ ನಿರ್ವಹಣೆ**: ಸೌಮ್ಯ ದೋಷ ನಿರ್ವಹಣೆ, ರಚನಾತ್ಮಕ ದೋಷ ಪ್ರತಿಕ್ರಿಯೆಗಳು ಮತ್ತು ಮರುಪ್ರಯತ್ನ ಲಾಜಿಕ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ
4. **ಕಾರ್ಯಕ್ಷಮತೆ**: ಕ್ಯಾಶಿಂಗ್, ಅಸಿಂಕ್ರೋನಸ್ ಪ್ರಕ್ರಿಯೆ ಮತ್ತು ಸಂಪನ್ಮೂಲ ನಿಯಂತ್ರಣವನ್ನು ಬಳಸಿ
5. **ಭದ್ರತೆ**: ಸಂಪೂರ್ಣ ಇನ್ಪುಟ್ ಮಾನ್ಯತೆ, ಅಧಿಕಾರ ಪರಿಶೀಲನೆಗಳು ಮತ್ತು ಸಂವೇದನಾಶೀಲ ಡೇಟಾ ನಿರ್ವಹಣೆಯನ್ನು ಅನ್ವಯಿಸಿ
6. **ಪರೀಕ್ಷೆ**: ಸಮಗ್ರ ಯೂನಿಟ್, ಇಂಟಿಗ್ರೇಶನ್ ಮತ್ತು ಎಂಡ್-ಟು-ಎಂಡ್ ಪರೀಕ್ಷೆಗಳನ್ನು ರಚಿಸಿ
7. **ಕಾರ್ಯಪ್ರವಾಹ ಮಾದರಿಗಳು**: ಚೈನ್‌ಗಳು, ಡಿಸ್ಪ್ಯಾಚರ್‌ಗಳು ಮತ್ತು ಸಮಾಂತರ ಪ್ರಕ್ರಿಯೆಗಳನ್ನು ಹೋಲುವ ಸ್ಥಾಪಿತ ಮಾದರಿಗಳನ್ನು ಅನ್ವಯಿಸಿ

## ಅಭ್ಯಾಸ

ಡಾಕ್ಯುಮೆಂಟ್ ಪ್ರೊಸೆಸಿಂಗ್ ವ್ಯವಸ್ಥೆಯಿಗಾಗಿ MCP ಟೂಲ್ ಮತ್ತು ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ವಿನ್ಯಾಸಮಾಡಿ, ಅದು:

1. ಬಹು ಫಾರ್ಮ್ಯಾಟ್‌ಗಳಲ್ಲಿ (PDF, DOCX, TXT) ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಸ್ವೀಕರಿಸುತ್ತದೆ
2. ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳಿಂದ ಪಠ್ಯ ಮತ್ತು ಪ್ರಮುಖ ಮಾಹಿತಿಯನ್ನು ಹೊರತೆಗೆಯುತ್ತದೆ
3. ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಪ್ರಕಾರ ಮತ್ತು ವಿಷಯದ ಮೂಲಕ ವರ್ಗೀಕರಿಸುತ್ತದೆ
4. ಪ್ರತಿ ಡಾಕ್ಯುಮೆಂಟ್‌ನ ಸಾರಾಂಶವನ್ನು ರಚಿಸುತ್ತದೆ

ಈ ದೃಶ್ಯಾವಳಿಗೆ ಸೂಕ್ತವಾದ ಟೂಲ್ ಸ್ಕೀಮಾಗಳು, ದೋಷ ನಿರ್ವಹಣೆ ಮತ್ತು ಕಾರ್ಯಪ್ರವಾಹ ಮಾದರಿಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ. ಈ ಅನುಷ್ಠಾನವನ್ನು ನೀವು ಹೇಗೆ ಪರೀಕ್ಷಿಸುವಿರಿ ಎಂದು ಪರಿಗಣಿಸಿ.

## ಸಂಪನ್ಮೂಲಗಳು

1. [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs) ನಲ್ಲಿ MCP ಸಮುದಾಯಕ್ಕೆ ಸೇರಿ ಇತ್ತೀಚಿನ ಅಭಿವೃದ್ಧಿಗಳ ಬಗ್ಗೆ ಅಪ್‌ಡೇಟ್ ಆಗಿರಿ
2. ಓಪನ್-ಸೋರ್ಸ್ [MCP ಪ್ರಾಜೆಕ್ಟ್‌ಗಳಿಗೆ](https://github.com/modelcontextprotocol) ಕೊಡುಗೆ ನೀಡಿ
3. ನಿಮ್ಮ ಸಂಸ್ಥೆಯ AI ಉಪಕ್ರಮಗಳಲ್ಲಿ MCP ತತ್ವಗಳನ್ನು ಅನ್ವಯಿಸಿ
4. ನಿಮ್ಮ ಉದ್ಯಮಕ್ಕಾಗಿ ವಿಶೇಷ MCP ಅನುಷ್ಠಾನಗಳನ್ನು ಅನ್ವೇಷಿಸಿ
5. ಬಹು-ಮೋಡಲ್ ಇಂಟಿಗ್ರೇಶನ್ ಅಥವಾ ಎಂಟರ್‌ಪ್ರೈಸ್ ಅಪ್ಲಿಕೇಶನ್ ಇಂಟಿಗ್ರೇಶನ್ ಮುಂತಾದ ವಿಶೇಷ MCP ವಿಷಯಗಳ ಮೇಲೆ ಉನ್ನತ ಕೋರ್ಸ್‌ಗಳನ್ನು ಪರಿಗಣಿಸಿ
6. [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) ಮೂಲಕ ಕಲಿತ ತತ್ವಗಳನ್ನು ಬಳಸಿ ನಿಮ್ಮದೇ MCP ಟೂಲ್‌ಗಳು ಮತ್ತು ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ನಿರ್ಮಿಸಲು ಪ್ರಯೋಗ ಮಾಡಿ

ಮುಂದೆ: ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು [ಕೇಸ್ ಸ್ಟಡಿಗಳು](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->