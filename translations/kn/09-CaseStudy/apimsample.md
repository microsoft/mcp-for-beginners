<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2228721599c0c8673de83496b4d7d7a9",
  "translation_date": "2025-12-11T10:34:49+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "kn"
}
-->
# ಪ್ರಕರಣ ಅಧ್ಯಯನ: API ನಿರ್ವಹಣೆಯಲ್ಲಿ REST API ಅನ್ನು MCP ಸರ್ವರ್ ಆಗಿ ಬಹಿರಂಗಪಡಿಸುವುದು

Azure API ನಿರ್ವಹಣೆ, ನಿಮ್ಮ API ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳ ಮೇಲೆ ಗೇಟ್ವೇ ಅನ್ನು ಒದಗಿಸುವ ಸೇವೆಯಾಗಿದೆ. ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಎಂದರೆ Azure API ನಿರ್ವಹಣೆ ನಿಮ್ಮ API ಗಳ ಮುಂದೆ ಪ್ರಾಕ್ಸಿ ಆಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ ಮತ್ತು ಬರುವ ವಿನಂತಿಗಳೊಂದಿಗೆ ಏನು ಮಾಡಬೇಕೆಂದು ನಿರ್ಧರಿಸಬಹುದು.

ಇದನ್ನು ಬಳಸುವುದರಿಂದ, ನೀವು ಕೆಳಗಿನ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಸೇರಿಸಬಹುದು:

- **ಭದ್ರತೆ**, ನೀವು API ಕೀಗಳು, JWT ನಿಂದ ನಿರ್ವಹಿತ ಗುರುತಿನವರೆಗೆ ಎಲ್ಲವನ್ನೂ ಬಳಸಬಹುದು.
- **ರೇಟ್ ಲಿಮಿಟಿಂಗ್**, ಒಂದು ಸಮಯ ಘಟಕಕ್ಕೆ ಎಷ್ಟು ಕರೆಗಳು ಹೋಗಬೇಕು ಎಂದು ನಿರ್ಧರಿಸುವ ಅದ್ಭುತ ವೈಶಿಷ್ಟ್ಯ. ಇದು ಎಲ್ಲಾ ಬಳಕೆದಾರರಿಗೆ ಉತ್ತಮ ಅನುಭವವನ್ನು ಖಚಿತಪಡಿಸುತ್ತದೆ ಮತ್ತು ನಿಮ್ಮ ಸೇವೆ ವಿನಂತಿಗಳಿಂದ ಅತಿಭಾರಿತವಾಗದಂತೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ.
- **ಸ್ಕೇಲಿಂಗ್ ಮತ್ತು ಲೋಡ್ ಬ್ಯಾಲೆನ್ಸಿಂಗ್**. ನೀವು ಲೋಡ್ ಅನ್ನು ಸಮತೋಲಗೊಳಿಸಲು ಹಲವಾರು ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಹೊಂದಿಸಬಹುದು ಮತ್ತು "ಲೋಡ್ ಬ್ಯಾಲೆನ್ಸ್" ಹೇಗೆ ಮಾಡಬೇಕೆಂದು ನಿರ್ಧರಿಸಬಹುದು.
- **ಸಾಮಾನ್ಯ ಕ್ಯಾಶಿಂಗ್, ಟೋಕನ್ ಮಿತಿ ಮತ್ತು ಟೋಕನ್ ಮಾನಿಟರಿಂಗ್** ಮುಂತಾದ AI ವೈಶಿಷ್ಟ್ಯಗಳು. ಇವು ಪ್ರತಿಕ್ರಿಯಾಶೀಲತೆಯನ್ನು ಸುಧಾರಿಸುತ್ತವೆ ಮತ್ತು ನಿಮ್ಮ ಟೋಕನ್ ಖರ್ಚಿನ ಮೇಲ್ವಿಚಾರಣೆಯಲ್ಲಿಯೂ ಸಹಾಯ ಮಾಡುತ್ತವೆ. [ಇಲ್ಲಿ ಇನ್ನಷ್ಟು ಓದಿ](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## ಏಕೆ MCP + Azure API ನಿರ್ವಹಣೆ?

ಮಾದರಿ ಸಾಂದರ್ಭಿಕ ಪ್ರೋಟೋಕಾಲ್ (Model Context Protocol) ವೇಗವಾಗಿ ಏಜೆಂಟಿಕ್ AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗಾಗಿ ಮಾನದಂಡವಾಗುತ್ತಿದೆ ಮತ್ತು ಸಾಧನಗಳು ಮತ್ತು ಡೇಟಾವನ್ನು ಸुसಂಗತ ರೀತಿಯಲ್ಲಿ ಬಹಿರಂಗಪಡಿಸುವ ವಿಧಾನವಾಗಿದೆ. API ಗಳನ್ನು "ನಿರ್ವಹಿಸಲು" ನೀವು ಬೇಕಾದಾಗ Azure API ನಿರ್ವಹಣೆ ಸಹಜ ಆಯ್ಕೆಯಾಗುತ್ತದೆ. MCP ಸರ್ವರ್‌ಗಳು ಸಾಮಾನ್ಯವಾಗಿ ಬೇರೆ API ಗಳೊಂದಿಗೆ ಸಂಯೋಜನೆ ಮಾಡುತ್ತವೆ ಉದಾಹರಣೆಗೆ ಸಾಧನಕ್ಕೆ ವಿನಂತಿಗಳನ್ನು ಪರಿಹರಿಸಲು. ಆದ್ದರಿಂದ Azure API ನಿರ್ವಹಣೆ ಮತ್ತು MCP ಅನ್ನು ಸಂಯೋಜಿಸುವುದು ಬಹಳ ಅರ್ಥಪೂರ್ಣ.

## ಅವಲೋಕನ

ಈ ವಿಶೇಷ ಬಳಕೆಯ ಪ್ರಕರಣದಲ್ಲಿ ನಾವು API ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು MCP ಸರ್ವರ್ ಆಗಿ ಬಹಿರಂಗಪಡಿಸುವುದನ್ನು ಕಲಿಯುತ್ತೇವೆ. ಇದರಿಂದ, ನಾವು ಈ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಏಜೆಂಟಿಕ್ ಅಪ್ಲಿಕೇಶನ್ ಭಾಗವನ್ನಾಗಿ ಸುಲಭವಾಗಿ ಮಾಡಬಹುದು ಮತ್ತು Azure API ನಿರ್ವಹಣೆಯ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಸಹ ಉಪಯೋಗಿಸಬಹುದು.

## ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯಗಳು

- ನೀವು ಸಾಧನಗಳಾಗಿ ಬಹಿರಂಗಪಡಿಸಲು ಬಯಸುವ ಎಂಡ್‌ಪಾಯಿಂಟ್ ವಿಧಾನಗಳನ್ನು ಆಯ್ಕೆಮಾಡುತ್ತೀರಿ.
- ನೀವು ಪಡೆಯುವ ಹೆಚ್ಚುವರಿ ವೈಶಿಷ್ಟ್ಯಗಳು ನಿಮ್ಮ API ಗಾಗಿ ನೀತಿ ವಿಭಾಗದಲ್ಲಿ ನೀವು ಸಂರಚಿಸುವುದರ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿವೆ. ಆದರೆ ಇಲ್ಲಿ ನಾವು ರೇಟ್ ಲಿಮಿಟಿಂಗ್ ಅನ್ನು ಹೇಗೆ ಸೇರಿಸುವುದೆಂದು ತೋರಿಸುತ್ತೇವೆ.

## ಪೂರ್ವ ಹಂತ: API ಅನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳಿ

ನೀವು ಈಗಾಗಲೇ Azure API ನಿರ್ವಹಣೆಯಲ್ಲಿ API ಹೊಂದಿದ್ದರೆ ಅದ್ಭುತ, ಈ ಹಂತವನ್ನು ಬಿಟ್ಟುಹೋಗಬಹುದು. ಇಲ್ಲದಿದ್ದರೆ, ಈ ಲಿಂಕ್ ನೋಡಿ, [Azure API ನಿರ್ವಹಣೆಗೆ API ಅನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳುವುದು](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API ಅನ್ನು MCP ಸರ್ವರ್ ಆಗಿ ಬಹಿರಂಗಪಡಿಸುವುದು

API ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಬಹಿರಂಗಪಡಿಸಲು, ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸೋಣ:

1. Azure ಪೋರ್ಟಲ್‌ಗೆ ಹೋಗಿ ಮತ್ತು ಈ ವಿಳಾಸಕ್ಕೆ <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
ನಿಮ್ಮ API ನಿರ್ವಹಣಾ ಘಟಕಕ್ಕೆ ನವಿಗೇಟ್ ಮಾಡಿ.

1. ಎಡ ಮೆನುದಲ್ಲಿ, APIs > MCP Servers > + Create new MCP Server ಆಯ್ಕೆಮಾಡಿ.

1. API ನಲ್ಲಿ, MCP ಸರ್ವರ್ ಆಗಿ ಬಹಿರಂಗಪಡಿಸಲು REST API ಆಯ್ಕೆಮಾಡಿ.

1. ಸಾಧನಗಳಾಗಿ ಬಹಿರಂಗಪಡಿಸಲು ಒಂದು ಅಥವಾ ಹೆಚ್ಚು API ಕಾರ್ಯಾಚರಣೆಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ. ನೀವು ಎಲ್ಲಾ ಕಾರ್ಯಾಚರಣೆಗಳನ್ನು ಅಥವಾ ನಿರ್ದಿಷ್ಟ ಕಾರ್ಯಾಚರಣೆಗಳನ್ನು ಆಯ್ಕೆಮಾಡಬಹುದು.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** ಆಯ್ಕೆಮಾಡಿ.

1. ಮೆನು ಆಯ್ಕೆಗೆ **APIs** ಮತ್ತು **MCP Servers** ಗೆ ನವಿಗೇಟ್ ಮಾಡಿ, ನೀವು ಕೆಳಗಿನಂತೆ ಕಾಣಬೇಕು:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP ಸರ್ವರ್ ರಚಿಸಲಾಗಿದೆ ಮತ್ತು API ಕಾರ್ಯಾಚರಣೆಗಳು ಸಾಧನಗಳಾಗಿ ಬಹಿರಂಗಪಡಿಸಲಾಗಿದೆ. MCP ಸರ್ವರ್ MCP Servers ಪೇನ್‌ನಲ್ಲಿ ಪಟ್ಟಿ ಮಾಡಲಾಗಿದೆ. URL ಕಾಲಮ್ MCP ಸರ್ವರ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ತೋರಿಸುತ್ತದೆ, ನೀವು ಪರೀಕ್ಷೆ ಅಥವಾ ಕ್ಲೈಂಟ್ ಅಪ್ಲಿಕೇಶನ್ ಒಳಗೆ ಕರೆ ಮಾಡಬಹುದು.

## ಐಚ್ಛಿಕ: ನೀತಿಗಳನ್ನು ಸಂರಚಿಸುವುದು

Azure API ನಿರ್ವಹಣೆಗೆ ನೀತಿಗಳ ಮೂಲ ಸಂಪ್ರದಾಯವಿದೆ, ಇಲ್ಲಿ ನೀವು ನಿಮ್ಮ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳಿಗೆ ವಿವಿಧ ನಿಯಮಗಳನ್ನು ಹೊಂದಿಸಬಹುದು ಉದಾಹರಣೆಗೆ ರೇಟ್ ಲಿಮಿಟಿಂಗ್ ಅಥವಾ ಸಾಮಾನ್ಯ ಕ್ಯಾಶಿಂಗ್. ಈ ನೀತಿಗಳು XML ನಲ್ಲಿ ರಚಿಸಲಾಗುತ್ತವೆ.

ನಿಮ್ಮ MCP ಸರ್ವರ್‌ಗೆ ರೇಟ್ ಲಿಮಿಟ್ ಹಾಕಲು ನೀತಿ ಹೇಗೆ ಹೊಂದಿಸುವುದು ಇಲ್ಲಿದೆ:

1. ಪೋರ್ಟಲ್‌ನಲ್ಲಿ, APIs ಅಡಿಯಲ್ಲಿ, **MCP Servers** ಆಯ್ಕೆಮಾಡಿ.

1. ನೀವು ರಚಿಸಿದ MCP ಸರ್ವರ್ ಆಯ್ಕೆಮಾಡಿ.

1. ಎಡ ಮೆನುದಲ್ಲಿ, MCP ಅಡಿಯಲ್ಲಿ, **Policies** ಆಯ್ಕೆಮಾಡಿ.

1. ನೀತಿ ಸಂಪಾದಕದಲ್ಲಿ, MCP ಸರ್ವರ್ ಸಾಧನಗಳಿಗೆ ಅನ್ವಯಿಸುವ ನೀತಿಗಳನ್ನು ಸೇರಿಸಿ ಅಥವಾ ಸಂಪಾದಿಸಿ. ನೀತಿಗಳು XML ಸ್ವರೂಪದಲ್ಲಿ ವ್ಯಾಖ್ಯಾನಿಸಲಾಗಿದೆ. ಉದಾಹರಣೆಗೆ, MCP ಸರ್ವರ್ ಸಾಧನಗಳಿಗೆ ಕರೆಗಳನ್ನು (ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ಪ್ರತಿ 30 ಸೆಕೆಂಡಿಗೆ 5 ಕರೆಗಳು ಪ್ರತಿ ಕ್ಲೈಂಟ್ IP ವಿಳಾಸಕ್ಕೆ) ಮಿತಿಗೊಳಿಸುವ ನೀತಿ ಸೇರಿಸಬಹುದು. ಇದಕ್ಕೆ ಕಾರಣವಾಗುವ XML ಇಲ್ಲಿದೆ:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    ನೀತಿ ಸಂಪಾದಕದ ಚಿತ್ರ ಇಲ್ಲಿದೆ:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## ಪ್ರಯತ್ನಿಸಿ

ನಮ್ಮ MCP ಸರ್ವರ್ ನಿರೀಕ್ಷಿತವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿದೆಯೇ ಎಂದು ಖಚಿತಪಡಿಸೋಣ.

ಇದಕ್ಕಾಗಿ, ನಾವು Visual Studio Code ಮತ್ತು GitHub Copilot ಮತ್ತು ಅದರ ಏಜೆಂಟ್ ಮೋಡ್ ಅನ್ನು ಬಳಸುತ್ತೇವೆ. ನಾವು MCP ಸರ್ವರ್ ಅನ್ನು *mcp.json* ಗೆ ಸೇರಿಸುವೆವು. ಇದರಿಂದ Visual Studio Code ಏಜೆಂಟಿಕ್ ಸಾಮರ್ಥ್ಯಗಳೊಂದಿಗೆ ಕ್ಲೈಂಟ್ ಆಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ ಮತ್ತು ಅಂತಿಮ ಬಳಕೆದಾರರು ಪ್ರಾಂಪ್ಟ್ ಟೈಪ್ ಮಾಡಿ ಆ ಸರ್ವರ್ ಜೊತೆ ಸಂವಹನ ಮಾಡಬಹುದು.

Visual Studio Code ನಲ್ಲಿ MCP ಸರ್ವರ್ ಅನ್ನು ಸೇರಿಸುವ ವಿಧಾನ ಇಲ್ಲಿದೆ:

1. Command Palette ನಿಂದ MCP: **Add Server command** ಬಳಸಿ.

1. ಪ್ರಾಂಪ್ಟ್ ಬಂದಾಗ, ಸರ್ವರ್ ಪ್ರಕಾರ ಆಯ್ಕೆಮಾಡಿ: **HTTP (HTTP ಅಥವಾ Server Sent Events)**.

1. API ನಿರ್ವಹಣೆಯ MCP ಸರ್ವರ್ URL ನಮೂದಿಸಿ. ಉದಾಹರಣೆ: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಾಗಿ) ಅಥವಾ **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಾಗಿ), ಸಾರಿಗೆಗಳ ನಡುವಿನ ವ್ಯತ್ಯಾಸ `/sse` ಅಥವಾ `/mcp` ಆಗಿದೆ ಎಂದು ಗಮನಿಸಿ.

1. ನಿಮ್ಮ ಆಯ್ಕೆಯ ಸರ್ವರ್ ID ನಮೂದಿಸಿ. ಇದು ಪ್ರಮುಖ ಮೌಲ್ಯವಲ್ಲ ಆದರೆ ಈ ಸರ್ವರ್ ಉದಾಹರಣೆಯೇನು ಎಂದು ನೆನಪಿಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.

1. ಸಂರಚನೆಯನ್ನು ನಿಮ್ಮ ವರ್ಕ್‌ಸ್ಪೇಸ್ ಸೆಟ್ಟಿಂಗ್ಸ್ ಅಥವಾ ಬಳಕೆದಾರ ಸೆಟ್ಟಿಂಗ್ಸ್‌ಗೆ ಉಳಿಸುವುದನ್ನು ಆಯ್ಕೆಮಾಡಿ.

  - **ವರ್ಕ್‌ಸ್ಪೇಸ್ ಸೆಟ್ಟಿಂಗ್ಸ್** - ಸರ್ವರ್ ಸಂರಚನೆ .vscode/mcp.json ಫೈಲ್‌ಗೆ ಮಾತ್ರ ಉಳಿಯುತ್ತದೆ, ಇದು ಪ್ರಸ್ತುತ ವರ್ಕ್‌ಸ್ಪೇಸ್‌ನಲ್ಲಿ ಲಭ್ಯವಿರುತ್ತದೆ.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    ಅಥವಾ ನೀವು ಸ್ಟ್ರೀಮಿಂಗ್ HTTP ಅನ್ನು ಸಾರಿಗೆ ಎಂದು ಆಯ್ಕೆಮಾಡಿದರೆ ಸ್ವಲ್ಪ ವಿಭಿನ್ನವಾಗಿರುತ್ತದೆ:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **ಬಳಕೆದಾರ ಸೆಟ್ಟಿಂಗ್ಸ್** - ಸರ್ವರ್ ಸಂರಚನೆ ನಿಮ್ಮ ಜಾಗತಿಕ *settings.json* ಫೈಲ್‌ಗೆ ಸೇರಿಸಲಾಗುತ್ತದೆ ಮತ್ತು ಎಲ್ಲಾ ವರ್ಕ್‌ಸ್ಪೇಸ್‌ಗಳಲ್ಲಿ ಲಭ್ಯವಿರುತ್ತದೆ. ಸಂರಚನೆ ಕೆಳಗಿನಂತಿದೆ:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. ನೀವು Azure API ನಿರ್ವಹಣೆಯತ್ತ ಸರಿಯಾಗಿ ಪ್ರಮಾಣೀಕರಿಸಲು ಶೀರ್ಷಿಕೆ ಸೇರಿಸಬೇಕಾಗುತ್ತದೆ. ಇದು **Ocp-Apim-Subscription-Key** ಎಂಬ ಶೀರ್ಷಿಕೆಯನ್ನು ಬಳಸುತ್ತದೆ.

    - ಇದನ್ನು ಸೆಟ್ಟಿಂಗ್ಸ್‌ಗೆ ಹೇಗೆ ಸೇರಿಸುವುದು ಇಲ್ಲಿದೆ:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ಇದು ನಿಮ್ಮ API ಕೀ ಮೌಲ್ಯವನ್ನು ಕೇಳುವ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ತೋರಿಸುತ್ತದೆ, ನೀವು ಅದನ್ನು Azure ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಮ್ಮ Azure API ನಿರ್ವಹಣಾ ಘಟಕದಿಂದ ಕಂಡುಹಿಡಿಯಬಹುದು.

   - ಬದಲಾಗಿ *mcp.json* ಗೆ ಸೇರಿಸಲು, ನೀವು ಹೀಗೆ ಸೇರಿಸಬಹುದು:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### ಏಜೆಂಟ್ ಮೋಡ್ ಬಳಸಿ

ಈಗ ನಾವು ಸೆಟ್ಟಿಂಗ್ಸ್ ಅಥವಾ *.vscode/mcp.json* ನಲ್ಲಿ ಎಲ್ಲವನ್ನೂ ಸಿದ್ಧಪಡಿಸಿದ್ದೇವೆ. ಪ್ರಯತ್ನಿಸೋಣ.

ನಿಮ್ಮ ಸರ್ವರ್‌ನಿಂದ ಬಹಿರಂಗಪಡಿಸಲಾದ ಸಾಧನಗಳು ಪಟ್ಟಿ ಮಾಡಲ್ಪಟ್ಟಿರುವ ಸಾಧನಗಳ ಐಕಾನ್ ಇರುತ್ತದೆ:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. ಸಾಧನಗಳ ಐಕಾನ್ ಕ್ಲಿಕ್ ಮಾಡಿ, ನೀವು ಕೆಳಗಿನಂತೆಯಾದ ಸಾಧನಗಳ ಪಟ್ಟಿಯನ್ನು ಕಾಣಬೇಕು:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. ಸಾಧನವನ್ನು ಕರೆ ಮಾಡಲು ಚಾಟ್‌ನಲ್ಲಿ ಪ್ರಾಂಪ್ಟ್ ನಮೂದಿಸಿ. ಉದಾಹರಣೆಗೆ, ನೀವು ಆರ್ಡರ್ ಬಗ್ಗೆ ಮಾಹಿತಿ ಪಡೆಯಲು ಸಾಧನವನ್ನು ಆಯ್ಕೆಮಾಡಿದ್ದರೆ, ಏಜೆಂಟ್‌ಗೆ ಆರ್ಡರ್ ಬಗ್ಗೆ ಕೇಳಬಹುದು. ಉದಾಹರಣೆಯ ಪ್ರಾಂಪ್ಟ್ ಇಲ್ಲಿದೆ:

    ```text
    get information from order 2
    ```

    ಈಗ ನಿಮಗೆ ಸಾಧನಗಳ ಐಕಾನ್ ತೋರಿಸಲಾಗುತ್ತದೆ, ಸಾಧನವನ್ನು ಕರೆ ಮಾಡಲು ಮುಂದುವರಿಯಿರಿ ಆಯ್ಕೆಮಾಡಿ, ನೀವು ಕೆಳಗಿನಂತೆಯಾದ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಕಾಣಬೇಕು:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ನೀವು ಮೇಲಿನಂತೆ ಏನು ನೋಡುತ್ತೀರೋ ಅದು ನೀವು ಹೊಂದಿಸಿರುವ ಸಾಧನಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿದೆ, ಆದರೆ ಆಲೋಚನೆ ಎಂದರೆ ನೀವು ಮೇಲಿನಂತೆ ಪಠ್ಯಾತ್ಮಕ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪಡೆಯುತ್ತೀರಿ**


## ಉಲ್ಲೇಖಗಳು

ಇನ್ನಷ್ಟು ತಿಳಿಯಲು ಇಲ್ಲಿದೆ:

- [Azure API ನಿರ್ವಹಣೆ ಮತ್ತು MCP ಕುರಿತು ಟ್ಯುಟೋರಿಯಲ್](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python ಮಾದರಿ: Azure API ನಿರ್ವಹಣೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಸುರಕ್ಷಿತ ದೂರ MCP ಸರ್ವರ್‌ಗಳು (ಪ್ರಾಯೋಗಿಕ)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP ಕ್ಲೈಂಟ್ ಪ್ರಾಧಿಕಾರ ಲ್ಯಾಬ್](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code ಗೆ Azure API ನಿರ್ವಹಣೆ ವಿಸ್ತರಣೆ ಬಳಸಿ API ಗಳನ್ನು ಆಮದುಮಾಡಿ ಮತ್ತು ನಿರ್ವಹಿಸಿ](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API ಸೆಂಟರ್‌ನಲ್ಲಿ ದೂರ MCP ಸರ್ವರ್‌ಗಳನ್ನು ನೋಂದಣಿ ಮಾಡಿ ಮತ್ತು ಕಂಡುಹಿಡಿಯಿರಿ](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI ಗೇಟ್ವೇ](https://github.com/Azure-Samples/AI-Gateway) Azure API ನಿರ್ವಹಣೆಯೊಂದಿಗೆ ಅನೇಕ AI ಸಾಮರ್ಥ್ಯಗಳನ್ನು ತೋರಿಸುವ ಅದ್ಭುತ ರೆಪೊ
- [AI ಗೇಟ್ವೇ ಕಾರ್ಯಾಗಾರಗಳು](https://azure-samples.github.io/AI-Gateway/)  Azure ಪೋರ್ಟಲ್ ಬಳಸಿ ಕಾರ್ಯಾಗಾರಗಳನ್ನು ಒಳಗೊಂಡಿದೆ, ಇದು AI ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡಲು ಉತ್ತಮ ವಿಧಾನ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->