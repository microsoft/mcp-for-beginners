# ಪ್ರಕರಣ ಅಧ್ಯಯನ: API Management ನಲ್ಲಿ REST API ಅನ್ನು MCP ಸರ್ವರ್ ಆಗಿ ಬಹಿರಂಗಪಡಿಸಿ

Azure API Management ನಿಮ್ಮ API ಅಂತಿಮ ಬಿಂದುಗಳ ಮೇಲೆ ಗೇಟ್ವೇ ಅನ್ನು ಒದಗಿಸುವ ಸೇವೆ. ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಎಂದರೆ Azure API Management ನಿಮ್ಮ API ಗಳ ಮುಂದೆ ಪ್ರಾಕ್ಸಿ ಪ್ರಕಾರ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ ಮತ್ತು ಆಗಮಿಸುವ ವಿನಂತಿಗಳನ್ನು ಏನು ಮಾಡಬೇಕೆಂದು ನಿರ್ಧರಿಸುತ್ತದೆ.

ಇದನ್ನು ಬಳಸಿ, ನೀವು ಈ ಕೆಳಗಿನ ಅನೇಕ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಸೇರಿಸುತ್ತೀರಿ:

- **ಸುರಕ್ಷತೆ**, ನೀವು API ಕೀಗಳು, JWT ನಿಂದ ಮ್ಯಾನೇಜ್ಡ್ ಐಡೆಂಟಿಟಿಯವರೆಗೆ ಎಲ್ಲವನ್ನೂ ಬಳಸಬಹುದು.
- **ರೇಟು ಮಿತಿಗೊಳಿಸುವಿಕೆ**, ಪ್ರತಿಷ್ಟಿತ ಕಾಲ ಆಳ್ವಿಕೆಯಲ್ಲಿ ಎಷ್ಟು ಕರೆಗಳು ಸಾಗಬೇಕು ಎಂದು ನಿರ್ಧರಿಸುವುದು ಒಂದು ಉತ್ತಮ ವೈಶಿಷ್ಟ್ಯ. ಇದರಿಂದ ಎಲ್ಲಾ ಬಳಕೆದಾರರಿಗೆ ಉತ್ತಮ ಅನುಭವ ದೊರೆಯುತ್ತದೆ ಮತ್ತು ನಿಮ್ಮ ಸೇವೆ ವಿನಂತಿಗಳಿಂದ ತುಂಬಿಹೋಗುವುದಿಲ್ಲ.
- **ಸ್ಕೇಲಿಂಗ್ ಮತ್ತು ಲೋಡ್ ಬ್ಯಾಲೆನ್ಸಿಂಗ್**. ನೀವು ಲೋಡ್ ಬಗ್ಗಿಸಲು ಹಲವು ಅಂತಿಮ ಬಿಂದುಗಳನ್ನು ಹೊಂದಿಸಬಹುದು ಮತ್ತು "ಲೋಡ್ ಬ್ಯಾಲೆನ್ಮಾಡುವುದು" ಹೇಗೆ ಎಂದು ನಿರ್ಧರಿಸಬಹುದು.
- **ಸೆಮ್ಯಾಂಟಿಕ್ ಕ್ಯಾಶಿಂಗ್, ಟೋಕನ್ ಮಿತಿ ಮತ್ತು ಟೋಕನ್ ಮಾನಿಟರಿಂಗ್ ಸೇರಿದಂತೆ AI ವೈಶಿಷ್ಟ್ಯಗಳು**. ಈಂತಹ ವೈಶಿಷ್ಟ್ಯಗಳು ಪ್ರತಿಕ್ರಿಯಾಶೀಲತೆಯನ್ನು ಸುಧಾರಿಸುತ್ತವೆ ಮತ್ತು ನಿಮ್ಮ ಟೋಕನ್ ಖರ್ಚಿನ ಮೇಲೆಯೂ ಹೊಣೆ ಹೊತ್ತಿಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ. [ಇಲ್ಲಿ ಹೆಚ್ಚು ಓದಿರಿ](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## ಏಕೆ MCP + Azure API Management?

ಮಾದರಿ ಪ್ರಾತಿನಿಧ್ಯ ಪ್ರೋಟೋಕಾಲ್ (Model Context Protocol) ವೇಗವಾಗಿ ಏಜೆಂಟಿಕ್ AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ತಂತ್ರವಾಗಿದೆ ಮತ್ತು ಸಾಧನಗಳು ಮತ್ತು ಡೇಟಾವನ್ನು ಸुसಂಬಂಧಿತವಾಗಿ ಬಹಿರಂಗಪಡಿಸುವ ವಿಧಾನವಾಗಿದೆ. ನಿಮ್ಮ API ಗಳನ್ನು "ನಿರ್ವಹಿಸಲು" Azure API Management ಸ್ವಾಭಾವಿಕ ಆಯ್ಕೆಯಾಗಿದೆ. MCP ಸರ್ವರ್‌ಗಳು ಪ್ರায়ಶಃ ಬೇರೆ API ಗಳೊಂದಿಗೆ ಸಂಯೋಜನೆ ಮಾಡುತ್ತವೆ, ಉದಾಹರಣೆಗೆ, ಕೈಪಿಡಿ ಹುಡುಕಲು. ಆದ್ದರಿಂದ Azure API Management ಮತ್ತು MCP ಅನ್ನು ಸಂಯೋಜಿಸುವುದು ತರ್ಕಸಂಗತವಾಗಿದೆ.

## ಅವಲೋಕನ

ಈ ನಿರ್ದಿಷ್ಟ ಬಳಕೆಯಲ್ಲಿ ನಾವು API ಅಂತಿಮ ಬಿಂದುಗಳನ್ನು MCP ಸರ್ವರ್ ಆಗಿ ಬಹಿರಂಗಪಡಿಸುವುದನ್ನು ಕಲಿಯೋಣ. ಹಾಗಾಗಿ ನಾವು ಸುಲಭವಾಗಿ ಈ ಅಂತಿಮ ಬಿಂದುವುಗಳನ್ನು ಏಜೆಂಟಿಕ್ ಅಪ್ಲಿಕೇಶನ್ ಭಾಗವಾಗಿಸಲು ಹಾಗೂ Azure API Management ನ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಉಪಯೋಗಿಸಬಹುದು.

## ಮುಖ್ಯ ವೈಶಿಷ್ಟ್ಯಗಳು

- ನೀವು exposed ಮಾಡಬೇಕಾದ endpoint ವಿಧಾನಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡುತ್ತೀರಿ.
- ನಿಮ್ಮ ಗೊಳಿಸುವಿಕೆಯಲ್ಲಿ ನೀವು ಒದಗಿಸುವ ಹೆಚ್ಚಿನ ವೈಶಿಷ್ಟ್ಯಗಳು ನಿಮ್ಮ APIಗೆ ನೀತಿ ವಿಭಾಗದಲ್ಲಿ ಹೇಗೆ ಕಾನ್ಫಿಗರ್ ಮಾಡಿದ್ದೀರೋ ಅದರ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿವೆ. ಆದರೆ ಇಲ್ಲಿ ನಾವು ರೇಟು ಮಿತಿಗೊಳಿಸುವಿಕೆ ಹೇಗೆ ಸೇರಿಸುವುದು ಎಂಬುದನ್ನು ತೋರಿಸುತ್ತೇವೆ.

## ಮುಂಚಿತ ಹಂತ: API ಅನ್ನು ಆಮದುಮಾಡಿ

ನೀವು Azure API Management ನಲ್ಲಿ ಈಗಾಗಲೇ API ಹೊಂದಿದ್ದರೆ ಅದ್ಭುತ, ಈ ಹಂತವನ್ನು ಬಿಟ್ಟುಹೋಗಬಹುದು. ಇಲ್ಲದಿದ್ದರೆ, ಈ ಲಿಂಕ್ ನೋಡಿ, [Azure API Management ಗೆ API ಆಮದು ಮಾಡುವುದು](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API ಅನ್ನು MCP ಸರ್ವರ್ ಆಗಿ ಬಹಿರಂಗಪಡಿಸಿ

API ಅಂತಿಮ ಬಿಂದುಗಳನ್ನು ಬಹಿರಂಗಪಡಿಸಲು, ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸೋಣ:

1. Azure ಪೋರ್ಪಾಳ್‌ಗೆ ಭೇಟಿ ನೀಡಿ ಕೆಳಗಿನ ವಿಳಾಸಕ್ಕೆ <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
ನಿಮ್ಮ API Management ಉದಾಹರಣೆಗೆ ಹೋಗಿ.

1. ಎಡಮೆನುವಿನಲ್ಲಿ, APIs > MCP Servers > + Create new MCP Server ಆಯ್ಕೆಮಾಡಿ.

1. API ನಲ್ಲಿ, MCP ಸರ್ವರ್ ಆಗಿ ಬಹಿರಂಗಪಡಿಸಲು REST API ಆಯ್ಕೆಮಾಡಿ.

1. ಒಂದು ಅಥವಾ ಹೆಚ್ಚು API ಸೇವೆಗಳು ಟೂಲ್ ಗಳಂತೆ ಬಹಿರಂಗಪಡಿಸಲು ಆಯ್ಕೆಮಾಡಿ. ನೀವು ಎಲ್ಲಾ ಸೇವೆಗಳನ್ನು ಅಥವಾ ಕೆಲವು ನಿರ್ದಿಷ್ಟ ಸೇವೆಗಳನ್ನು ಆಯ್ಕೆಮಾಡಬಹುದು.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. **Create** ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ.

1. ಮೆನು ಆಯ್ಕೆಯಲ್ಲಿ **APIs** ಮತ್ತು **MCP Servers** ಗೆ ಹೋಗಿ, ನೀವು ಹೀಗೆ ಕಾಣಬಹುದು:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP ಸರ್ವರ್ ಸೃಷ್ಟಿಸಲಾಗಿದೆ ಮತ್ತು API ಕಾರ್ಯಗಳನ್ನು ಟೂಲ್ಸ್ ಆಗಿ ಬಹಿರಂಗಪಡಿಸಲಾಗಿದೆ. MCP ಸರ್ವರ್ MCP Servers ಪಿನ್ ನಲ್ಲಿ ಪಟ್ಟಿಯಾಗುತ್ತದೆ. URL ಕಾಲಮ್ MCP ಸರ್ವರ್ ಕರೆಗೆ ಪ್ರಯೋಗಿಸುವ ಅಂತಿಮ ಬಿಂದುವನ್ನು ತೋರಿಸುತ್ತದೆ.

## ಐಚ್ಛಿಕ: ನೀತಿಗಳನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ

Azure API Management ನಲ್ಲಿ ನೀತಿಗಳ ಮೂಲ ಭಾವನೆ ಇದೆ, ಅದು ನಿಮಗೆ ನಿಮ್ಮ ಅಂತಿಮ ಬಿಂದುವಿಗೆ ವಿಭಿನ್ನ ನಿಯಮಗಳನ್ನು ಹೊಂದಿಸಲು ಅನುಮತಿಸುತ್ತದೆ, ಉದಾಹರಣೆಗೆ ರೇಟು ಮಿತಿಗೊಳಿಸುವಿಕೆ ಅಥವಾ ಸೆಮ್ಯಾಂಟಿಕ್ ಕ್ಯಾಸಿಂಗ್. ಈ ನೀತಿಗಳನ್ನು XML ನಲ್ಲಿ ರಚಿಸಲಾಗುತ್ತದೆ.

MCP ಸರ್ವರ್ ಗೆ ರೇಟು ಮಿತಿಗೊಳಿಸುವ ನೀತಿ ಹೇಗೆ ಹೊಂದಿಸಲು ತಿಳಿಯೋಣ:

1. ಪೋರ್ಪಾಳ್ ನಲ್ಲಿ, APIs ಅಡಿಯಲ್ಲಿ, **MCP Servers** ಆಯ್ಕೆಮಾಡಿ.

1. ನೀವು ಸೃಷ್ಟಿಸಿದ MCP ಸರ್ವರ್ ಆಯ್ಕೆಮಾಡಿ.

1. ಎಡ ಮೆನುವಿನಲ್ಲಿ, MCP ಅಡಿಯಲ್ಲಿ **Policies** ಆಯ್ಕೆಮಾಡಿ.

1. ನೀತಿ ಸಂಪಾದಕದಲ್ಲಿ, MCP ಸರ್ವರ್ ಟೂಲ್ಸ್ ಗೆ ಅನ್ವಯಿಸುವ ನೀತಿಗಳನ್ನು ಉ接ಸಂಬಂಧಿತ XML ರೂಪದಲ್ಲಿ ಸೇರಿಸಿ ಅಥವಾ ಸಂಪಾದಿಸಿ. ಉದಾಹರಣೆಗೆ, MCP ಸರ್ವರ್ ಟೂಲ್ಸ್ ಗೆ ಕರೆಗಳನ್ನು ಮಿತಿಗೊಳಿಸುವ ನೀತಿ (ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ಒಂದು ಕ್ಲೈಂಟ್ IP ವಿಳಾಸಕ್ಕೆ ಪ್ರತಿ 30 ಸೆಕಂಡ್ಗೆ 5 ಕರೆಗಳು). ಈ ಕೆಳಗಿನ XML ಅದರಲ್ಲಿರುವುದು:

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

ನಮ್ಮ MCP ಸರ್ವರ್ ನಿರೀಕ್ಷೆಯಂತೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿದೆಯೇ ಎಂದು ಖಚಿತಪಡಿಸೋಣ.

> [!NOTE]
> Azure API Management ಪ್ರಸ್ತುತ ಈ ಸರ್ವರ್ ಅನ್ನು Streamable HTTP `/mcp` ಅಂತಿಮ ಬಿಂದುವಿನಿಂದ ಬಹಿರಂಗಪಡಿಸುತ್ತಿದೆ. ಹಳೆಯ HTTP+SSE `/sse` ಸಾರಿಗೆ ಅಪರಿಷ್ಕೃತವಾಗಿದೆ ಮತ್ತು ಹಳೆಯ ಕ್ಲೈಂಟ್ ಗಳಿಗೆ ಮಾತ್ರ ಬಳಸಬೇಕು.



ಇದಕ್ಕಾಗಿ ನಾವು Visual Studio Code ಮತ್ತು GitHub Copilot ಆಗಿವು ಮರೆತು ಅದರ Agent ಮೋಡ್ ಅನ್ನು ಬಳಸುತ್ತೇವೆ. *mcp.json* ಫೈಲ್‌ಗೆ MCP ಸರ್ವರ್ ಅನ್ನು ಸೇರಿಸುವುದರಿಂದ Visual Studio Code ಏಜೆಂಟಿಕ್ ಸಾಮರ್ಥ್ಯಗಳೊಂದಿಗೆ ಕ್ಲೈಂಟ್ ಆಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ ಮತ್ತು ಬಳಕೆದಾರರು ಪ್ರಾಂಪ್ಟ್/type ಮಾಡುವ ಮೂಲಕ ಸರ್ವರ್ ಜೊತೆ ಸಂವಾದ ನಡೆಸಬಹುದು.

Visual Studio Code ನಲ್ಲಿ MCP ಸರ್ವರ್ ಅನ್ನು ಸೇರಿಸುವ ವಿಧಾನ ನೋಡೋಣ:

1. Command Palette ನಿಂದ MCP: **Add Server command** ಅನ್ನು ಬಳಸಿ.

1. ಕೇಳಿದಾಗ ಸರ್ವರ್ ಪ್ರಕಾರ ಆಯ್ಕೆಮಾಡಿ: **HTTP (HTTP ಅಥವಾ Server Sent Events)**.

1. API Management ನಲ್ಲಿ MCP ಸರ್ವರ್ ಇತ್ತೀಚೆಗೆ ನೀಡಿರುವ Streamable HTTP URL ನಮೂದಿಸಿ.
    ಉದಾಹರಣೆಗೆ:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. ನಿಮ್ಮ ಇಚ್ಛೆಯ ಸರ್ವರ್ ID ನಮೂದಿಸಿ. ಇದು ಮುಖ್ಯ ಮೌಲ್ಯವಲ್ಲ ಆದರೆ ನೀವು ಈ ಸರ್ವರ್ ಉದಾಹರಣೆಯನ್ನು ಮರೆತದಂತೆ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.

1. ಕಾನ್ಫಿಗರೇಶನ್ ನಿಮ್ಮ ವರ್ಕ್‌ಸ್ಪೇಸ್ ಸೆಟ್ಟಿಂಗ್ಸ್ ಅಥವಾ ಯೂಸರ್ ಸೆಟ್ಟಿಂಗ್ಸ್ ಗೆ ಉಳಿಸಬೇಕೆಂದು ಆಯ್ಕೆಮಾಡಿ.

  - **ವರ್ಕ್‌ಸ್ಪೇಸ್ ಸೆಟ್ಟಿಂಗ್ಸ್** - ಸರ್ವರ್ ಕಾನ್ಫಿಗರೇಶನ್ ಪ್ರಸ್ತುತ ವರ್ಕ್‌ಸ್ಪೇಸ್ ನಲ್ಲಿ ಮಾತ್ರ ಲಭ್ಯವಿರುವ .vscode/mcp.json ಫೈಲ್ ಗೆ ಉಳಿಯುತ್ತದೆ.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **ಯೂಸರ್ ಸೆಟ್ಟಿಂಗ್ಸ್** - ಸರ್ವರ್ ಕಾನ್ಫಿಗರೇಶನ್ ನಿಮ್ಮ ಲೋಕಲ್ *settings.json* ಫೈಲ್ ಗೆ ಸೇರಿಸಲಾಗುತ್ತದೆ ಮತ್ತು ಎಲ್ಲಾ ವರ್ಕ್‌ಸ್ಪೇಸ್ ಗಳಲ್ಲಿ ಲಭ್ಯವಿರುತ್ತದೆ. ಕಾನ್ಫಿಗರೇಶನ್ ಈ ಕೆಳಗಿನಂತೆ ಕಾಣುತ್ತದೆ:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. ನೀವು ಸರ್ವರ್ ಅನ್ನು ಸರಿಯಾಗಿ ದೃಢೀಕರಿಸಲು ಒಂದು ಹೆಡರ್ (header) ಕಾನ್ಫಿಗರ್ ಮಾಡಬೇಕಾಗುತ್ತದೆ, ಅದನ್ನು **Ocp-Apim-Subscription-Key** ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ.

    - ಈ ರೀತಿಯಾಗಿ ನಾನು ಸೆಟ್ಟಿಂಗ್ಸ್ ಗೆ ಸೇರಿಸಬಹುದು:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ಇದು API ಕೀ ಮೌಲ್ಯವನ್ನು ಕೇಳಲು ಪ್ರಾಂಪ್ಟ್ ತೋರಿಸುವುದು, ನೀವು ಈ ಕೀ ಅನ್ನು Azure Portal ನಿಂದ ನಿಮ್ಮ Azure API Management ಉದಾಹರಣೆಯಲ್ಲಿ ಕಾಣಬಹುದು.

   - ಅದನ್ನು *mcp.json* ಗೆ ಸೇರಿಸಲು ನೀವು ಈ ರೀತಿಯಾಗಿ ಕೂಡ ಸೇರಿಸಬಹುದು:

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

### ಏಜೆಂಟ್ ಮೋಡ್ ಅನ್ನು ಬಳಸಿ

ಈಗ ನಾವು ಸೆಟ್ಟಿಂಗ್ಸ್ ಅಥವಾ *.vscode/mcp.json* ಎರಡರಲ್ಲಿ ಒಂದರಲ್ಲಿ ಸಿದ್ಧರಾಗಿ ಇದ್ದೇವೆ. ಪ್ರಯತ್ನಿಸಿ ನೋಡೋಣ.

ಕಡೆಯಲ್ಲಿ ಟೂಲ್ ಐಕಾನ್ ಇರುತ್ತದೆ, ಇಲ್ಲಿ ನಿಮ್ಮ ಸರ್ವರ್ ನಲ್ಲಿ ಬಹಿರಂಗಗೊಂಡ ಟೂಲ್ ಗಳ ಪಟ್ಟಿಯನ್ನು ಕಾಣಬಹುದು:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. ಟೂಲ್ ಐಕಾನ್ ಕ್ಲಿಕ್ ಮಾಡಿ, ಟೂಲ್ ಗಳ ಪಟ್ಟಿಯನ್ನು ಕಾಣಬಹುದು:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. ಚಾಟ್ ನಲ್ಲಿ ಪ್ರಾಂಪ್ಟ್ ನಮೂದಿಸಿ ಟೂಲ್ ಅನ್ನು invoke ಮಾಡಿ. ಉದಾಹರಣೆಗೆ, ನೀವು ಒರಡರ್ ಕುರಿತು ಮಾಹಿತಿಗಾಗಿ ಟೂಲ್ ಆಯ್ಕೆಮಾಡಿದ್ದರೆ, ಏಜೆಂಟ್ ಗೆ ಆ ಸಂಬಂಧಿಸಿದ ಒಂದು ಪ್ರಶ್ನೆಯನ್ನು ಕೇಳಬಹುದು. ಈ ಕೆಳಗಿನಂತೆ ಒಂದು ಉದಾಹರದ ಪ್ರಾಂಪ್ಟ್:

    ```text
    get information from order 2
    ```

    ಈಗ ನಿಮಗೆ ಟೂಲ್ ಅನ್ನು ಕರೆ ಮಾಡಲು ಮುಂದುವರಿಯಲು ಟೂಲ್ ಐಕಾನ್ ನೀಡುತ್ತದೆ. ಮುಂದುವರೆಸಲು ಆಯ್ಕೆಮಾಡಿ, ನಿಮಗೆ ಇದೇ ರೀತಿ ಔಟ್‌ಪುಟ್ ಕಾಣುತ್ತದೆ:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ಮುಂದಿನ ಚಿತ್ರದಲ್ಲಿ ನೀವು ನೋಡುತ್ತಿರುವುದು ನಿಮಗೆ ಯಾವ ಟೂಲ್‌ಗಳು ಸಿದ್ಧವಾಗಿವೆ ಅವಲಂಬಿತವಾಗುತ್ತದೆ, ಭಾವನೆ ಇದು ನೀವು ಮೇಲಿನಂತೆಯೇ ಪಠ್ಯಾತ್ಮಕ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪಡೆಯುತ್ತೀರಿ ಎಂಬುದಾಗಿದೆ**


## ಪರಿಚಯಗಳು

ನಿಮಗೆ ಇನ್ನಷ್ಟು ತಿಳಿದುಕೊಳ್ಳಲು ಈ ಕೆಳಗಿನವುಗಳು ಸಹಾಯಕ:

- [Azure API Management ಮತ್ತು MCP ಕುರಿತು ಟ್ಯುಟೋರಿಯಲ್](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python ಮಾದರಿ: Azure API Management ಬಳಸಿ ದೂರಸ್ಥ MCP ಸರ್ವರ್ ಗಳನ್ನು ಸುರಕ್ಷಿತಗೊಳಿಸುವುದು (ಪ್ರಾಯೋಗಿಕ)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP ಕ್ಲೈಂಟ್ ಅನುಮೋದನಾ ಪ್ರಯೋಗಾಲಯ](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code ಗೆ Azure API Management ವಿಸ್ತರಣೆ ಬಳಸಿ API ಗಳನ್ನು ಆಮದುಮಾಡಿ ಮತ್ತು ನಿರ್ವಹಿಸಿ](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center ನಲ್ಲಿ ದೂರಸ್ಥ MCP ಸರ್ವರ್ ಗಳನ್ನು ನೋಂದಾಯಿಸಿ ಮತ್ತು ಪತ್ತೆಮಾಡಿ](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI ಗೇಟ್ವೇ](https://github.com/Azure-Samples/AI-Gateway) Azure API Management ನೊಂದಿಗೆ ಅನೇಕ AI ಸಾಮರ್ಥ್ಯಗಳನ್ನು ತೋರಿಸುವ ಒಳ್ಳೆಯ ರೆಪೋ
- [AI ಗೇಟ್ವೇ ಕಾರ್ಯಾಗಾರಗಳು](https://azure-samples.github.io/AI-Gateway/)  Azure Portal ಉಪಯೋಗಿ ಕಾರ್ಯಾಗಾರಗಳನ್ನು ಹೊಂದಿದ್ದು, AI ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಆವಲೋಕಿಸುವ ಉತ್ತಮ ಮಾರ್ಗವಾಗಿದೆ.

## ಮುಂದೇವನು

- ಹಿಂತಿರುಗಿ: [ಕ್ರೇಸ್ ಅಧ್ಯಯನಗಳ ಅವಲೋಕನ](./README.md)
- ಮುಂದಿನದು: [Azure AI ಟ್ರಾವೆಲ್ ಏಜೆಂಟ್ಸ್](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->