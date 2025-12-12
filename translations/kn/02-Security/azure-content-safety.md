<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5300fd1b5e84520d500b2a8f568a1d8",
  "translation_date": "2025-12-11T11:29:11+00:00",
  "source_file": "02-Security/azure-content-safety.md",
  "language_code": "kn"
}
-->
# ಅಡ್ವಾನ್ಸ್ಡ್ MCP ಭದ್ರತೆ ಜೊತೆಗೆ ಅಜೂರ್ ವಿಷಯ ಭದ್ರತೆ

ಅಜೂರ್ ವಿಷಯ ಭದ್ರತೆ ನಿಮ್ಮ MCP ಅನುಷ್ಠಾನಗಳ ಭದ್ರತೆಯನ್ನು ಹೆಚ್ಚಿಸಬಹುದಾದ ಹಲವು ಶಕ್ತಿಶಾಲಿ ಸಾಧನಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ:

## ಪ್ರಾಂಪ್ಟ್ ಶೀಲ್ಡ್‌ಗಳು

ಮೈಕ್ರೋಸಾಫ್ಟ್‌ನ AI ಪ್ರಾಂಪ್ಟ್ ಶೀಲ್ಡ್‌ಗಳು ನೇರ ಮತ್ತು ಪರೋಕ್ಷ ಪ್ರಾಂಪ್ಟ್ ಇಂಜೆಕ್ಷನ್ ದಾಳಿಗಳ ವಿರುದ್ಧ ಬಲವಾದ ರಕ್ಷಣೆ ಒದಗಿಸುತ್ತವೆ:

1. **ಅಡ್ವಾನ್ಸ್ಡ್ ಡಿಟೆಕ್ಷನ್**: ವಿಷಯದಲ್ಲಿ ನುಡಿದಿರುವ ದುಷ್ಟ ಸೂಚನೆಗಳನ್ನು ಗುರುತಿಸಲು ಯಂತ್ರ ಅಧ್ಯಯನವನ್ನು ಬಳಸುತ್ತದೆ.
2. **ಸ್ಪಾಟ್‌ಲೈಟಿಂಗ್**: AI ವ್ಯವಸ್ಥೆಗಳು ಮಾನ್ಯ ಸೂಚನೆಗಳು ಮತ್ತು ಬಾಹ್ಯ ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ವಿಭಿನ್ನಗೊಳಿಸಲು ಇನ್‌ಪುಟ್ ಪಠ್ಯವನ್ನು ಪರಿವರ್ತಿಸುತ್ತದೆ.
3. **ಡೆಲಿಮಿಟರ್ಸ್ ಮತ್ತು ಡೇಟಾಮಾರ್ಕಿಂಗ್**: ನಂಬಿಗಸ್ತ ಮತ್ತು ನಂಬಲಾಗದ ಡೇಟಾ ನಡುವಿನ ಗಡಿಗಳನ್ನು ಗುರುತಿಸುತ್ತದೆ.
4. **ವಿಷಯ ಭದ್ರತೆ ಏಕೀಕರಣ**: ಜೈಲ್ಬ್ರೇಕ್ ಪ್ರಯತ್ನಗಳು ಮತ್ತು ಹಾನಿಕಾರಕ ವಿಷಯಗಳನ್ನು ಪತ್ತೆಹಚ್ಚಲು ಅಜೂರ್ AI ವಿಷಯ ಭದ್ರತೆ ಜೊತೆಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ.
5. **ನಿರಂತರ ನವೀಕರಣಗಳು**: ಮೈಕ್ರೋಸಾಫ್ಟ್ ಉದಯೋನ್ಮುಖ ಬೆದರಿಕೆಗಳ ವಿರುದ್ಧ ರಕ್ಷಣಾ ಯಂತ್ರಗಳನ್ನು ನಿಯಮಿತವಾಗಿ ನವೀಕರಿಸುತ್ತದೆ.

## MCP ಜೊತೆಗೆ ಅಜೂರ್ ವಿಷಯ ಭದ್ರತೆ ಅನುಷ್ಠಾನ

ಈ ವಿಧಾನವು ಬಹು-ಮಟ್ಟದ ರಕ್ಷಣೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ:
- ಪ್ರಕ್ರಿಯೆಗೆ ಒಳಪಡಿಸುವ ಮೊದಲು ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ಸ್ಕ್ಯಾನ್ ಮಾಡುವುದು
- ಹಿಂತಿರುಗಿಸುವ ಮೊದಲು ಔಟ್‌ಪುಟ್‌ಗಳನ್ನು ಮಾನ್ಯಗೊಳಿಸುವುದು
- ತಿಳಿದಿರುವ ಹಾನಿಕಾರಕ ಮಾದರಿಗಳಿಗಾಗಿ ಬ್ಲಾಕ್‌ಲಿಸ್ಟ್‌ಗಳನ್ನು ಬಳಸುವುದು
- ಅಜೂರ್‌ನ ನಿರಂತರ ನವೀಕರಿಸಲಾದ ವಿಷಯ ಭದ್ರತೆ ಮಾದರಿಗಳನ್ನು ಉಪಯೋಗಿಸುವುದು

## ಅಜೂರ್ ವಿಷಯ ಭದ್ರತೆ ಸಂಪನ್ಮೂಲಗಳು

ನಿಮ್ಮ MCP ಸರ್ವರ್‌ಗಳೊಂದಿಗೆ ಅಜೂರ್ ವಿಷಯ ಭದ್ರತೆಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವ ಬಗ್ಗೆ ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ ಈ ಅಧಿಕೃತ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಪರಿಶೀಲಿಸಿ:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - ಅಜೂರ್ ವಿಷಯ ಭದ್ರತೆಗಾಗಿ ಅಧಿಕೃತ ಡಾಕ್ಯುಮೆಂಟೇಶನ್.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - ಪ್ರಾಂಪ್ಟ್ ಇಂಜೆಕ್ಷನ್ ದಾಳಿಗಳನ್ನು ತಡೆಯುವ ವಿಧಾನವನ್ನು ತಿಳಿಯಿರಿ.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - ವಿಷಯ ಭದ್ರತೆ ಅನುಷ್ಠಾನಗೊಳಿಸಲು ವಿವರವಾದ API ರೆಫರೆನ್ಸ್.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C# ಬಳಸಿ ತ್ವರಿತ ಅನುಷ್ಠಾನ ಮಾರ್ಗದರ್ಶಿ.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - ವಿವಿಧ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಭಾಷೆಗಳಿಗಾಗಿ ಕ್ಲೈಂಟ್ ಲೈಬ್ರರಿಗಳು.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - ಜೈಲ್ಬ್ರೇಕ್ ಪ್ರಯತ್ನಗಳನ್ನು ಪತ್ತೆಹಚ್ಚುವ ಮತ್ತು ತಡೆಯುವ ವಿಶೇಷ ಮಾರ್ಗದರ್ಶನ.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - ವಿಷಯ ಭದ್ರತೆಯನ್ನು ಪರಿಣಾಮಕಾರಿಯಾಗಿ ಅನುಷ್ಠಾನಗೊಳಿಸುವ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು.

ಹೆಚ್ಚು ಆಳವಾದ ಅನುಷ್ಠಾನಕ್ಕಾಗಿ, ನಮ್ಮ [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md) ಅನ್ನು ನೋಡಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->