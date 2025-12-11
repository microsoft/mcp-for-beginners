<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2228721599c0c8673de83496b4d7d7a9",
  "translation_date": "2025-12-11T10:34:05+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "ml"
}
-->
# കേസ് സ്റ്റഡി: API മാനേജ്മെന്റിൽ REST API MCP സെർവറായി എക്സ്പോസ് ചെയ്യുക

Azure API Management, നിങ്ങളുടെ API എന്റ്പോയിന്റുകളുടെ മുകളിൽ ഗേറ്റ്വേ നൽകുന്ന ഒരു സേവനമാണ്. ഇത് എങ്ങനെ പ്രവർത്തിക്കുന്നു എന്നത് Azure API Management നിങ്ങളുടെ API-കളുടെ മുന്നിൽ ഒരു പ്രോക്സി പോലെ പ്രവർത്തിച്ച് വരുന്ന അഭ്യർത്ഥനകളെ എങ്ങനെ കൈകാര്യം ചെയ്യണമെന്ന് തീരുമാനിക്കുന്നു.

ഇത് ഉപയോഗിച്ച്, നിങ്ങൾക്ക് നിരവധി ഫീച്ചറുകൾ ലഭിക്കുന്നു:

- **സുരക്ഷ**, API കീകൾ, JWT മുതൽ മാനേജ്ഡ് ഐഡന്റിറ്റി വരെ എല്ലാം ഉപയോഗിക്കാം.
- **റേറ്റ് ലിമിറ്റിംഗ്**, ഒരു നിശ്ചിത സമയഘട്ടത്തിൽ എത്ര കോളുകൾ കടക്കാമെന്ന് തീരുമാനിക്കാൻ കഴിയുന്ന മികച്ച ഫീച്ചർ. ഇത് എല്ലാ ഉപയോക്താക്കൾക്കും മികച്ച അനുഭവം ഉറപ്പാക്കുകയും നിങ്ങളുടെ സേവനം അഭ്യർത്ഥനകളാൽ ഭരിക്കപ്പെടാതിരിക്കാനും സഹായിക്കുന്നു.
- **സ്കെയിലിംഗ് & ലോഡ് ബാലൻസിംഗ്**. ലോഡ് ബാലൻസ് ചെയ്യാൻ നിരവധി എന്റ്പോയിന്റുകൾ സജ്ജമാക്കാം, കൂടാതെ "ലോഡ് ബാലൻസ്" എങ്ങനെ ചെയ്യാമെന്ന് തീരുമാനിക്കാം.
- **സെമാന്റിക് കാഷിംഗ് പോലുള്ള AI ഫീച്ചറുകൾ**, ടോക്കൺ പരിധി, ടോക്കൺ നിരീക്ഷണം എന്നിവ. ഇവ പ്രതികരണക്ഷമത മെച്ചപ്പെടുത്തുകയും ടോക്കൺ ചെലവുകൾ നിയന്ത്രിക്കാനും സഹായിക്കുന്നു. [ഇവിടെ കൂടുതൽ വായിക്കുക](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## MCP + Azure API Management എന്തുകൊണ്ട്?

Model Context Protocol (MCP) ഏജന്റിക് AI ആപ്പുകൾക്കും ടൂളുകളും ഡാറ്റയും സ്ഥിരതയുള്ള രീതിയിൽ എങ്ങനെ എക്സ്പോസ് ചെയ്യാമെന്ന് ഒരു സ്റ്റാൻഡേർഡായി മാറുകയാണ്. API-കൾ "മാനേജ്" ചെയ്യേണ്ടപ്പോൾ Azure API Management സ്വാഭാവികമായ തിരഞ്ഞെടുപ്പാണ്. MCP സെർവറുകൾ സാധാരണയായി മറ്റൊരു API-കളുമായി ഇന്റഗ്രേറ്റ് ചെയ്ത് ടൂളുകൾക്ക് അഭ്യർത്ഥനകൾ പരിഹരിക്കുന്നു. അതിനാൽ Azure API Management-ഉം MCP-ഉം ചേർത്ത് ഉപയോഗിക്കുന്നത് വളരെ ബുദ്ധിമുട്ടില്ലാത്തതാണ്.

## അവലോകനം

ഈ പ്രത്യേക ഉപയോഗ കേസിൽ, API എന്റ്പോയിന്റുകൾ MCP സെർവറായി എക്സ്പോസ് ചെയ്യുന്നത് പഠിക്കാം. ഇതിലൂടെ, ഈ എന്റ്പോയിന്റുകൾ ഏജന്റിക് ആപ്പിന്റെ ഭാഗമാക്കാനും Azure API Management-ന്റെ ഫീച്ചറുകൾ പ്രയോജനപ്പെടുത്താനും കഴിയും.

## പ്രധാന ഫീച്ചറുകൾ

- നിങ്ങൾ എക്സ്പോസ് ചെയ്യാൻ ആഗ്രഹിക്കുന്ന എന്റ്പോയിന്റ് മെത്തഡുകൾ ടൂളുകളായി തിരഞ്ഞെടുക്കാം.
- നിങ്ങൾക്ക് ലഭിക്കുന്ന അധിക ഫീച്ചറുകൾ നിങ്ങളുടെ API ന്റെ പോളിസി സെക്ഷനിൽ കോൺഫിഗർ ചെയ്തതിനെ ആശ്രയിച്ചിരിക്കും. ഇവിടെ റേറ്റ് ലിമിറ്റിംഗ് എങ്ങനെ ചേർക്കാമെന്ന് കാണിക്കും.

## മുൻപടി: API ഇമ്പോർട്ട് ചെയ്യുക

നിങ്ങൾക്ക് Azure API Management-ൽ API ഇതിനകം ഉണ്ടെങ്കിൽ, ഈ ഘട്ടം ഒഴിവാക്കാം. ഇല്ലെങ്കിൽ, ഈ ലിങ്ക് പരിശോധിക്കുക, [Azure API Management-ലേക്ക് API ഇമ്പോർട്ട് ചെയ്യൽ](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API MCP സെർവറായി എക്സ്പോസ് ചെയ്യുക

API എന്റ്പോയിന്റുകൾ എക്സ്പോസ് ചെയ്യാൻ, താഴെ പറയുന്ന ഘട്ടങ്ങൾ പിന്തുടരുക:

1. Azure പോർട്ടലിലേക്ക് പോവുക, ഈ വിലാസം <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> സന്ദർശിക്കുക  
നിങ്ങളുടെ API Management ഇൻസ്റ്റൻസ് തിരഞ്ഞെടുക്കുക.

1. ഇടത് മെനുവിൽ, APIs > MCP Servers > + Create new MCP Server തിരഞ്ഞെടുക്കുക.

1. API-യിൽ, MCP സെർവറായി എക്സ്പോസ് ചെയ്യാൻ ഒരു REST API തിരഞ്ഞെടുക്കുക.

1. ടൂളുകളായി എക്സ്പോസ് ചെയ്യാൻ ഒരു അല്ലെങ്കിൽ കൂടുതൽ API ഓപ്പറേഷനുകൾ തിരഞ്ഞെടുക്കുക. എല്ലാ ഓപ്പറേഷനുകളും അല്ലെങ്കിൽ ചില പ്രത്യേക ഓപ്പറേഷനുകളും തിരഞ്ഞെടുക്കാം.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** തിരഞ്ഞെടുക്കുക.

1. **APIs** > **MCP Servers** മെനു ഓപ്ഷനിലേക്ക് പോവുക, താഴെ കാണുന്നവ കാണാം:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP സെർവർ സൃഷ്ടിക്കപ്പെട്ടിട്ടുണ്ട്, API ഓപ്പറേഷനുകൾ ടൂളുകളായി എക്സ്പോസ് ചെയ്തിട്ടുണ്ട്. MCP സെർവർ MCP Servers പെയിനിൽ ലിസ്റ്റ് ചെയ്തിരിക്കുന്നു. URL കോളത്തിൽ MCP സെർവറിന്റെ എന്റ്പോയിന്റ് കാണാം, ഇത് ടെസ്റ്റിംഗിനോ ക്ലയന്റ് ആപ്ലിക്കേഷനിൽ ഉപയോഗിക്കാനോ കഴിയും.

## ഐച്ഛികം: പോളിസികൾ കോൺഫിഗർ ചെയ്യുക

Azure API Management-ൽ പോളിസികൾ എന്ന കോർ ആശയം ഉണ്ട്, ഇതിലൂടെ നിങ്ങൾക്ക് റേറ്റ് ലിമിറ്റിംഗ്, സെമാന്റിക് കാഷിംഗ് പോലുള്ള വ്യത്യസ്ത നിയമങ്ങൾ എന്റ്പോയിന്റുകൾക്ക് സജ്ജമാക്കാം. ഈ പോളിസികൾ XML-ൽ എഴുതപ്പെടുന്നു.

MCP സെർവറിന്റെ റേറ്റ് ലിമിറ്റിംഗ് പോളിസി എങ്ങനെ സജ്ജമാക്കാമെന്ന് കാണാം:

1. പോർട്ടലിൽ, APIs-ൽ **MCP Servers** തിരഞ്ഞെടുക്കുക.

1. നിങ്ങൾ സൃഷ്ടിച്ച MCP സെർവർ തിരഞ്ഞെടുക്കുക.

1. ഇടത് മെനുവിൽ MCP-യിൽ **Policies** തിരഞ്ഞെടുക്കുക.

1. പോളിസി എഡിറ്ററിൽ MCP സെർവറിന്റെ ടൂളുകൾക്ക് ബാധകമായ പോളിസികൾ ചേർക്കുക അല്ലെങ്കിൽ തിരുത്തുക. പോളിസികൾ XML ഫോർമാറ്റിലാണ്. ഉദാഹരണത്തിന്, MCP സെർവറിന്റെ ടൂളുകൾക്ക് (ഈ ഉദാഹരണത്തിൽ, ഓരോ ക്ലയന്റ് IP വിലാസത്തിനും 30 സെക്കൻഡിൽ 5 കോളുകൾ) കോളുകൾ പരിധി നിശ്ചയിക്കുന്ന പോളിസി ചേർക്കാം. റേറ്റ് ലിമിറ്റിംഗ് സൃഷ്ടിക്കുന്ന XML ഇതാണ്:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```
  
    പോളിസി എഡിറ്ററിന്റെ ചിത്രം:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## പരീക്ഷിച്ച് നോക്കുക

നമ്മുടെ MCP സെർവർ ഉദ്ദേശിച്ച പോലെ പ്രവർത്തിക്കുന്നുണ്ടെന്ന് ഉറപ്പാക്കാം.

ഇതിന്, Visual Studio Code, GitHub Copilot, അതിന്റെ Agent മോഡ് ഉപയോഗിക്കും. MCP സെർവർ *mcp.json*-ലേക്ക് ചേർക്കും. ഇതിലൂടെ Visual Studio Code ഏജന്റിക് കഴിവുകളുള്ള ക്ലയന്റായി പ്രവർത്തിക്കുകയും, ഉപയോക്താക്കൾ പ്രോംപ്റ്റ് ടൈപ്പ് ചെയ്ത് സെർവറുമായി ഇടപഴകാൻ കഴിയും.

Visual Studio Code-ൽ MCP സെർവർ ചേർക്കുന്നത് ഇങ്ങനെ:

1. Command Palette-ൽ MCP: **Add Server command** ഉപയോഗിക്കുക.

1. പ്രോംപ്റ്റ് വന്നാൽ സെർവർ തരം തിരഞ്ഞെടുക്കുക: **HTTP (HTTP or Server Sent Events)**.

1. API Management-ലെ MCP സെർവറിന്റെ URL നൽകുക. ഉദാഹരണം: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE എന്റ്പോയിന്റ്) അല്ലെങ്കിൽ **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP എന്റ്പോയിന്റ്), ട്രാൻസ്പോർട്ടുകൾ തമ്മിലുള്ള വ്യത്യാസം `/sse` അല്ലെങ്കിൽ `/mcp` ആണ്.

1. നിങ്ങളുടെ ഇഷ്ടാനുസൃത സെർവർ ഐഡി നൽകുക. ഇത് പ്രധാനപ്പെട്ട മൂല്യം അല്ല, പക്ഷേ ഈ സെർവർ ഇൻസ്റ്റൻസ് എന്താണെന്ന് ഓർക്കാൻ സഹായിക്കും.

1. കോൺഫിഗറേഷൻ നിങ്ങളുടെ വർക്ക്‌സ്പേസ് സെറ്റിംഗ്സിലോ യൂസർ സെറ്റിംഗ്സിലോ സേവ് ചെയ്യാമെന്ന് തിരഞ്ഞെടുക്കുക.

  - **വർക്ക്‌സ്പേസ് സെറ്റിംഗ്സ്** - സെർവർ കോൺഫിഗറേഷൻ .vscode/mcp.json ഫയലിൽ സേവ് ചെയ്യപ്പെടും, ഇത് നിലവിലെ വർക്ക്‌സ്പേസിൽ മാത്രമേ ലഭ്യമാകൂ.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```
  
    അല്ലെങ്കിൽ ട്രാൻസ്പോർട്ട് ആയി സ്റ്റ്രീമിംഗ് HTTP തിരഞ്ഞെടുക്കുകയാണെങ്കിൽ ഇത് അല്പം വ്യത്യസ്തമായിരിക്കും:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```
  
  - **യൂസർ സെറ്റിംഗ്സ്** - സെർവർ കോൺഫിഗറേഷൻ നിങ്ങളുടെ ഗ്ലോബൽ *settings.json* ഫയലിൽ ചേർക്കപ്പെടും, എല്ലാ വർക്ക്‌സ്പേസുകളിലും ലഭ്യമാകും. കോൺഫിഗറേഷൻ ഇങ്ങനെ കാണപ്പെടും:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Azure API Management-നോട് ശരിയായി ഓതന്റിക്കേറ്റ് ചെയ്യാൻ ഒരു ഹെഡർ കോൺഫിഗർ ചെയ്യേണ്ടതുണ്ട്. ഇത് **Ocp-Apim-Subscription-Key** എന്ന ഹെഡർ ഉപയോഗിക്കുന്നു.

    - സെറ്റിംഗ്സിൽ ഇത് ചേർക്കുന്നത് ഇങ്ങനെ:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ഇത് API കീ മൂല്യം ചോദിക്കുന്ന പ്രോംപ്റ്റ് കാണിക്കും, ഇത് Azure പോർട്ടലിൽ നിങ്ങളുടെ Azure API Management ഇൻസ്റ്റൻസിനായി കണ്ടെത്താം.

   - *mcp.json*-ലേക്ക് ചേർക്കാൻ, ഇങ്ങനെ ചേർക്കാം:

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
  
### ഏജന്റ് മോഡ് ഉപയോഗിക്കുക

ഇപ്പോൾ സെറ്റിംഗ്സിലോ *.vscode/mcp.json*-ലോ എല്ലാം സജ്ജമാണ്. പരീക്ഷിച്ച് നോക്കാം.

ടൂളുകൾ ഐക്കൺ ഇങ്ങനെ കാണണം, നിങ്ങളുടെ സെർവറിൽ നിന്നുള്ള എക്സ്പോസ് ചെയ്ത ടൂളുകൾ ലിസ്റ്റ് ചെയ്തിരിക്കും:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. ടൂളുകൾ ഐക്കൺ ക്ലിക്ക് ചെയ്യുക, ടൂളുകളുടെ ലിസ്റ്റ് കാണാം:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. ടൂൾ പ്രവർത്തിപ്പിക്കാൻ ചാറ്റിൽ പ്രോംപ്റ്റ് നൽകുക. ഉദാഹരണത്തിന്, ഒരു ഓർഡറിനെക്കുറിച്ച് വിവരങ്ങൾ ലഭിക്കാൻ ടൂൾ തിരഞ്ഞെടുക്കുകയാണെങ്കിൽ, ഏജന്റിനോട് ഓർഡറിനെക്കുറിച്ച് ചോദിക്കാം. ഉദാഹരണ പ്രോംപ്റ്റ്:

    ```text
    get information from order 2
    ```
  
    ഇപ്പോൾ ടൂളുകൾ ഐക്കൺ കാണിച്ച് ടൂൾ വിളിക്കാൻ തുടരണം എന്ന് ചോദിക്കും. തുടരണം തിരഞ്ഞെടുക്കുക, താഴെപോലെ ഔട്ട്പുട്ട് കാണാം:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **മുകളിൽ കാണുന്നത് നിങ്ങൾ സജ്ജമാക്കിയ ടൂളുകളെ ആശ്രയിച്ചിരിക്കും, പക്ഷേ ആശയം നിങ്ങൾക്ക് ടെക്സ്റ്റ് അടിസ്ഥാനത്തിലുള്ള പ്രതികരണം ലഭിക്കുകയാണ്**


## റഫറൻസുകൾ

കൂടുതൽ പഠിക്കാൻ:

- [Azure API Management & MCP ട്യൂട്ടോറിയൽ](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python സാമ്പിൾ: Azure API Management ഉപയോഗിച്ച് സുരക്ഷിത റിമോട്ട് MCP സെർവറുകൾ (പരീക്ഷണ ഘട്ടം)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP ക്ലയന്റ് ഓതറൈസേഷൻ ലാബ്](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code-ൽ Azure API Management എക്സ്റ്റൻഷൻ ഉപയോഗിച്ച് API-കൾ ഇമ്പോർട്ട് ചെയ്യാനും മാനേജ് ചെയ്യാനും](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center-ൽ റിമോട്ട് MCP സെർവറുകൾ രജിസ്റ്റർ ചെയ്യാനും കണ്ടെത്താനും](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Management-ഉം AI കഴിവുകളും കാണിക്കുന്ന മികച്ച റിപോസിറ്ററി
- [AI Gateway വർക്ക്‌ഷോപ്പുകൾ](https://azure-samples.github.io/AI-Gateway/) Azure പോർട്ടൽ ഉപയോഗിച്ച് AI കഴിവുകൾ വിലയിരുത്താൻ മികച്ച മാർഗ്ഗം നൽകുന്ന വർക്ക്‌ഷോപ്പുകൾ ഉൾക്കൊള്ളുന്നു.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->