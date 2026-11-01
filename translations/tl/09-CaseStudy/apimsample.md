# Pag-aaral ng Kaso: I-expose ang REST API sa API Management bilang MCP server

Ang Azure API Management, ay isang serbisyo na nagbibigay ng Gateway sa ibabaw ng iyong mga API Endpoints. Ang pag-andar nito ay ang Azure API Management ay kumikilos bilang proxy sa harap ng iyong mga API at maaaring magpasya kung ano ang gagawin sa mga papasok na kahilingan.

Sa pamamagitan ng paggamit nito, makakakuha ka ng maraming mga tampok tulad ng:

- **Seguridad**, maaari mong gamitin ang lahat mula sa API keys, JWT hanggang sa managed identity.
- **Paglilimita sa rate**, isang magaling na tampok ay ang kakayahang magpasya kung ilang tawag ang papasok bawat tiyak na yunit ng oras. Ito ay tumutulong upang matiyak na lahat ng mga gumagamit ay may magandang karanasan at na hindi mapuno ang iyong serbisyo ng mga kahilingan.
- **Pag-scale & Load balancing**. Maaari kang mag-set up ng ilang mga endpoints upang pantayin ang load at maaari mo ring piliin kung paano mag-"load balance". 
- **Mga tampok ng AI tulad ng semantic caching**, token limit at token monitoring at marami pa. Ito ay mga magagandang tampok na nagpapabuti ng responsiveness pati na rin tumutulong upang masubaybayan ang iyong paggasta sa token. [Basahin pa dito](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities). 

## Bakit MCP + Azure API Management?

Ang Model Context Protocol ay mabilis na nagiging pamantayan para sa agentic AI apps at kung paano i-expose ang mga tools at data sa isang pare-parehong paraan. Ang Azure API Management ay isang natural na pagpipilian kapag kailangan mong "pamahalaan" ang mga API. Ang MCP Servers ay madalas na nag-iintegrate sa iba pang mga API upang malutas ang mga kahilingan sa isang tool halimbawa. Kaya ang pagsasama ng Azure API Management at MCP ay may malaking kahulugan.

## Pangkalahatang-ideya

Sa partikular na kaso ng paggamit na ito, matututuhan natin kung paano i-expose ang API endpoints bilang isang MCP Server. Sa paggawa nito, madali nating magagawang maging bahagi ng isang agentic app ang mga endpoints habang ginagamit din ang mga tampok mula sa Azure API Management.

## Mga Pangunahing Tampok

- Pinipili mo ang mga endpoint methods na gusto mong i-expose bilang mga tools.
- Ang mga karagdagang tampok na makukuha mo ay nakasalalay sa kung ano ang iyong ikokonekta sa policy section para sa iyong API. Ngunit dito ipapakita namin kung paano magdagdag ng rate limiting.

## Pre-step: mag-import ng API

Kung mayroon ka nang API sa Azure API Management, maganda, maaari mong laktawan ang hakbang na ito. Kung wala pa, tingnan ang link na ito, [pag-import ng API sa Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## I-expose ang API bilang MCP Server

Upang i-expose ang mga API endpoints, sundin natin ang mga hakbang na ito:

1. Pumunta sa Azure Portal sa sumusunod na adres <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Mag-navigate sa iyong API Management instance.

1. Sa kaliwang menu, piliin ang APIs > MCP Servers > + Lumikha ng bagong MCP Server.

1. Sa API, piliin ang isang REST API na i-eexpose bilang MCP server.

1. Piliin ang isa o higit pang API Operations na i-expose bilang mga tools. Maaari mong piliin lahat ng operasyon o ilang tiyak na operasyon lamang.

    ![Piliin ang mga paraan na i-eexpose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Piliin ang **Create**.

1. Pumunta sa menu option na **APIs** at **MCP Servers**, makikita mo ang sumusunod:

    ![Makita ang MCP Server sa pangunahing pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Ang MCP server ay nalikha at ang API operations ay na-eexpose bilang mga tools. Ang MCP server ay nakalista sa MCP Servers pane. Ang URL column ay nagpapakita ng endpoint ng MCP server na maaari mong tawagan para sa testing o sa loob ng isang client application.

## Opsyonal: I-configure ang mga patakaran

Mayroong core concept ng mga patakaran ang Azure API Management kung saan nagse-set up ka ng iba't ibang mga panuntunan para sa iyong mga endpoint tulad ng halimbawa rate limiting o semantic caching. Ang mga patakarang ito ay nilikha sa XML.

Ganito kung paano mo maaaring i-set up ang isang patakaran upang i-rate limit ang iyong MCP Server:

1. Sa portal, sa ilalim ng APIs, piliin ang **MCP Servers**.

1. Piliin ang MCP server na nilikha mo.

1. Sa kaliwang menu, sa ilalim ng MCP, piliin ang **Policies**.

1. Sa policy editor, idagdag o i-edit ang mga patakaran na gusto mong ilapat sa mga tools ng MCP server. Ang mga patakaran ay tinutukoy sa format ng XML. Halimbawa, maaari kang magdagdag ng patakaran upang limitahan ang mga tawag sa mga tools ng MCP server (sa halimbawa na ito, 5 tawag bawat 30 segundo bawat IP address ng kliyente). Narito ang XML na magreresulta ng rate limit:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Narito ang isang imahe ng policy editor:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Subukan ito 

Siguraduhin nating gumagana ang ating MCP Server ayon sa nilalayon.

> [!NOTE]
> Ang Azure API Management ay kasalukuyang nag-eexpose ng server na ito sa pamamagitan ng Streamable
> HTTP `/mcp` endpoint. Ang mas lumang HTTP+SSE `/sse` transport ay tinatanggal na at
> dapat gamitin lamang sa mga legacy na kliyente.

Para dito, gagamit tayo ng Visual Studio Code at GitHub Copilot at ang Agent mode nito. Idadagdag natin ang MCP server sa isang *mcp.json* file. Sa paggawa nito, ang Visual Studio Code ay kikilos bilang isang kliyente na may agentic capabilities at ang mga end user ay makakapag-type ng prompt at makikipag-ugnayan sa nasabing server.

Tingnan natin kung paano idagdag ang MCP server sa Visual Studio Code:

1. Gamitin ang MCP: **Add Server command mula sa Command Palette**.

1. Kapag na-prompt, piliin ang uri ng server: **HTTP (HTTP o Server Sent Events)**.

1. Ipasok ang Streamable HTTP URL na ipinakita para sa MCP server sa API Management.
    Halimbawa:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Maglagay ng server ID na iyong pipiliin. Hindi ito mahalagang halaga ngunit makakatulong ito upang maalala mo kung ano ang instance ng server na ito.

1. Piliin kung i-save ang configuration sa iyong workspace settings o user settings.

    - **Workspace settings** - Ang server configuration ay ini-save sa isang `.vscode/mcp.json` file, na available lamang sa kasalukuyang workspace.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **User settings** - Ang server configuration ay idinadagdag sa iyong global na *settings.json* file at available ito sa lahat ng mga workspace. Ganito ang hitsura ng configuration:

      ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Kailangan mo ring magdagdag ng configuration header upang siguraduhin na ma-authenticate ito nang maayos patungo sa Azure API Management. Gumagamit ito ng header na tinatawag na **Ocp-Apim-Subscription-Key**.

    - Ganito mo ito maidagdag sa settings:


    ![Pagdagdag ng header para sa authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), magpapakita ito ng prompt na hihingi sa iyo ng API key value na maaari mong makita sa Azure Portal para sa iyong Azure API Management instance.

   - Para idagdag ito sa *mcp.json* sa halip, maaari mo itong idagdag ganito:

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

### Gumamit ng Agent mode

Naka-set up na tayo sa alinman sa settings o sa *.vscode/mcp.json*. Subukan na natin ito.

Dapat mayroong Tools icon tulad nito, kung saan nakalista ang mga exposed tools mula sa iyong server:

![Mga Tools mula sa server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. I-click ang tools icon at makikita mo ang listahan ng mga tools tulad nito:

    ![Mga Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Maglagay ng prompt sa chat upang tawagin ang tool. Halimbawa, kung pumili ka ng tool upang kumuha ng impormasyon tungkol sa isang order, maaari mong tanungin ang agent tungkol sa isang order. Narito ang isang halimbawa ng prompt:

    ```text
    get information from order 2
    ```

    Ngayon ay ipapakita ang tools icon na nagtatanong kung gusto mong magpatuloy sa pagtawag ng tool. Piliin na ituloy ang pagpapatakbo ng tool, makikita mo na ang output tulad nito:

    ![Resulta mula sa prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ang nakikita mo sa itaas ay depende sa mga tool na na-set up mo, ngunit ang ideya ay makakakuha ka ng tekstuwal na tugon tulad ng nasa itaas**


## Mga Sanggunian

Ganito mo matututuhan nang higit pa:

- [Tutorial sa Azure API Management at MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Halimbawa sa Python: Secure remote MCP servers gamit ang Azure API Management (eksperimento)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client authorization lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gamitin ang Azure API Management extension para sa VS Code upang mag-import at mag-manage ng mga API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Magrehistro at tuklasin ang mga remote MCP servers sa Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Mahusay na repository na nagpapakita ng maraming kakayahan ng AI gamit ang Azure API Management
- [Mga workshop ng AI Gateway](https://azure-samples.github.io/AI-Gateway/) Naglalaman ng mga workshop gamit ang Azure Portal, na isang mahusay na paraan upang simulan ang pagsusuri sa mga kakayahan ng AI.

## Ano ang Susunod

- Bumalik sa: [Pangkalahatang-ideya ng Mga Pag-aaral ng Kaso](./README.md)
- Susunod: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->