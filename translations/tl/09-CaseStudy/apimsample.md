# Case Study: I-expose ang REST API sa API Management bilang isang MCP server

Ang Azure API Management ay isang serbisyo na nagbibigay ng Gateway sa ibabaw ng iyong mga API Endpoints. Gumagana ito bilang isang proxy sa harap ng iyong mga API at maaaring magdesisyon kung ano ang gagawin sa mga papasok na request.

Sa paggamit nito, makakakuha ka ng maraming benepisyo tulad ng:

- **Seguridad**, maaari mong gamitin ang lahat mula sa API keys, JWT, hanggang sa managed identity.
- **Rate limiting**, isang mahusay na tampok na nagbibigay-daan sa iyo na magtakda kung ilang tawag ang papayagan sa loob ng isang tiyak na oras. Nakakatulong ito upang masiguro na lahat ng gumagamit ay may magandang karanasan at hindi rin ma-overwhelm ang iyong serbisyo sa dami ng request.
- **Scaling at Load balancing**. Maaari kang mag-set up ng maraming endpoints upang maibalanse ang load at maaari mo ring piliin kung paano mag-"load balance".
- **AI features tulad ng semantic caching**, token limit, at token monitoring, at iba pa. Ang mga ito ay mahusay na tampok na nagpapabuti sa responsiveness at tumutulong sa iyo na masubaybayan ang iyong token spending. [Magbasa pa dito](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Bakit MCP + Azure API Management?

Ang Model Context Protocol ay mabilis na nagiging pamantayan para sa mga agentic AI apps at kung paano i-expose ang mga tools at data sa isang pare-parehong paraan. Ang Azure API Management ay natural na pagpipilian kapag kailangan mong "i-manage" ang mga API. Ang MCP Servers ay madalas na nag-iintegrate sa iba pang mga API upang mag-resolve ng mga request sa isang tool, halimbawa. Kaya't ang pagsasama ng Azure API Management at MCP ay may malaking kabuluhan.

## Pangkalahatang-ideya

Sa partikular na use case na ito, matututo tayong i-expose ang mga API endpoints bilang isang MCP Server. Sa paggawa nito, madali nating maisasama ang mga endpoints na ito sa isang agentic app habang ginagamit din ang mga tampok ng Azure API Management.

## Pangunahing Tampok

- Maaari mong piliin ang mga endpoint methods na nais mong i-expose bilang mga tools.
- Ang mga karagdagang tampok na makukuha mo ay nakadepende sa kung ano ang iko-configure mo sa policy section ng iyong API. Ngunit dito, ipapakita namin kung paano magdagdag ng rate limiting.

## Pre-step: mag-import ng API

Kung mayroon ka nang API sa Azure API Management, mahusay, maaari mong laktawan ang hakbang na ito. Kung wala pa, tingnan ang link na ito, [pag-import ng API sa Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## I-expose ang API bilang MCP Server

Upang i-expose ang mga API endpoints, sundin ang mga hakbang na ito:

1. Pumunta sa Azure Portal sa sumusunod na address <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   Pumunta sa iyong API Management instance.

1. Sa kaliwang menu, piliin ang **APIs > MCP Servers > + Create new MCP Server**.

1. Sa API, piliin ang isang REST API na i-expose bilang isang MCP server.

1. Piliin ang isa o higit pang API Operations na i-expose bilang mga tools. Maaari mong piliin ang lahat ng operations o mga partikular lamang.

    ![Piliin ang mga methods na i-expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Piliin ang **Create**.

1. Pumunta sa menu option na **APIs** at **MCP Servers**, dapat mong makita ang sumusunod:

    ![Makita ang MCP Server sa pangunahing pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Ang MCP server ay nalikha at ang mga API operations ay na-expose bilang mga tools. Ang MCP server ay nakalista sa MCP Servers pane. Ang URL column ay nagpapakita ng endpoint ng MCP server na maaari mong tawagan para sa testing o sa loob ng isang client application.

## Opsyonal: I-configure ang mga polisiya

Ang Azure API Management ay may pangunahing konsepto ng mga polisiya kung saan maaari kang mag-set up ng iba't ibang mga patakaran para sa iyong mga endpoints tulad ng rate limiting o semantic caching. Ang mga polisiya na ito ay isinusulat sa XML.

Narito kung paano mag-set up ng polisiya upang mag-rate limit sa iyong MCP Server:

1. Sa portal, sa ilalim ng **APIs**, piliin ang **MCP Servers**.

1. Piliin ang MCP server na iyong nalikha.

1. Sa kaliwang menu, sa ilalim ng MCP, piliin ang **Policies**.

1. Sa policy editor, magdagdag o mag-edit ng mga polisiya na nais mong i-apply sa mga tools ng MCP server. Ang mga polisiya ay tinutukoy sa XML format. Halimbawa, maaari kang magdagdag ng polisiya upang limitahan ang mga tawag sa mga tools ng MCP server (sa halimbawang ito, 5 tawag kada 30 segundo bawat client IP address). Narito ang XML na magpapagana ng rate limit:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Narito ang imahe ng policy editor:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Subukan ito

Tiyakin nating gumagana ang ating MCP Server ayon sa inaasahan.

Para dito, gagamit tayo ng Visual Studio Code at GitHub Copilot at ang Agent mode nito. Idadagdag natin ang MCP server sa isang *mcp.json* file. Sa paggawa nito, ang Visual Studio Code ay kikilos bilang isang client na may agentic capabilities at ang mga end user ay maaaring mag-type ng prompt at makipag-ugnayan sa nasabing server.

Narito kung paano idagdag ang MCP server sa Visual Studio Code:

1. Gamitin ang MCP: **Add Server command mula sa Command Palette**.

1. Kapag tinanong, piliin ang uri ng server: **HTTP (HTTP o Server Sent Events)**.

1. Ipasok ang URL ng MCP server sa API Management. Halimbawa: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (para sa SSE endpoint) o **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (para sa MCP endpoint), tandaan ang pagkakaiba sa pagitan ng mga transport ay `/sse` o `/mcp`.

1. Ipasok ang isang server ID ng iyong pinili. Hindi ito mahalagang halaga ngunit makakatulong ito upang maalala mo kung ano ang server instance na ito.

1. Piliin kung ise-save ang configuration sa iyong workspace settings o user settings.

  - **Workspace settings** - Ang server configuration ay mase-save sa isang .vscode/mcp.json file na makikita lamang sa kasalukuyang workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    o kung pipiliin mo ang streaming HTTP bilang transport, bahagyang mag-iiba ito:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - Ang server configuration ay idadagdag sa iyong global *settings.json* file at makikita sa lahat ng workspace. Ang configuration ay magiging ganito:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Kailangan mo ring magdagdag ng configuration, isang header upang masigurong maayos ang authentication sa Azure API Management. Gumagamit ito ng header na tinatawag na **Ocp-Apim-Subscription-Key**.

    - Narito kung paano mo ito maidaragdag sa settings:

    ![Pagdaragdag ng header para sa authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), magpapakita ito ng prompt upang hilingin ang API key value na makikita mo sa Azure Portal para sa iyong Azure API Management instance.

   - Upang idagdag ito sa *mcp.json*, maaari mo itong idagdag tulad nito:

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

### Gamitin ang Agent mode

Ngayon ay naka-set up na tayo sa alinman sa settings o sa *.vscode/mcp.json*. Subukan natin ito.

Dapat mayroong Tools icon tulad nito, kung saan nakalista ang mga tools na na-expose mula sa iyong server:

![Mga Tools mula sa server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. I-click ang tools icon at dapat mong makita ang listahan ng mga tools tulad nito:

    ![Mga Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Maglagay ng prompt sa chat upang tawagin ang tool. Halimbawa, kung pumili ka ng tool upang makakuha ng impormasyon tungkol sa isang order, maaari mong tanungin ang agent tungkol sa isang order. Narito ang halimbawa ng prompt:

    ```text
    get information from order 2
    ```

    Makikita mo ngayon ang isang tools icon na nagtatanong kung nais mong magpatuloy sa pagtawag ng tool. Piliin ang magpatuloy sa pagpapatakbo ng tool, dapat mong makita ang output tulad nito:

    ![Resulta mula sa prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Ang makikita mo sa itaas ay nakadepende sa kung anong mga tools ang na-setup mo, ngunit ang ideya ay makakakuha ka ng isang textual na tugon tulad ng nasa itaas.**

## Mga Sanggunian

Narito kung paano ka makakapag-aral pa:

- [Tutorial sa Azure API Management at MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python sample: Secure remote MCP servers gamit ang Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client authorization lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gamitin ang Azure API Management extension para sa VS Code upang mag-import at mag-manage ng mga API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Magrehistro at mag-discover ng remote MCP servers sa Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Mahusay na repo na nagpapakita ng maraming AI capabilities gamit ang Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Naglalaman ng mga workshop gamit ang Azure Portal, na isang mahusay na paraan upang simulan ang pag-evaluate ng AI capabilities.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.