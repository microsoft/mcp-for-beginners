# Pag-aaral ng Kaso: I-expose ang REST API sa API Management bilang isang MCP server

Ang Azure API Management, ay isang serbisyo na nagbibigay ng Gateway sa ibabaw ng iyong mga API Endpoints. Ang pamamaraan nito ay ang Azure API Management ay kumikilos na parang proxy sa harap ng iyong mga API at maaaring magpasya kung ano ang gagawin sa mga papasok na kahilingan.

Sa pamamagitan ng paggamit nito, nagdadagdag ka ng maraming mga tampok tulad ng:

- **Seguridad**, maaari mong gamitin ang lahat mula sa API keys, JWT hanggang sa managed identity.
- **Paghihigpit ng rate**, isang mahusay na tampok ay ang kakayahang magdesisyon kung ilang tawag ang makakapasa sa loob ng isang takdang yunit ng oras. Nakakatulong ito upang matiyak na lahat ng gumagamit ay may mahusay na karanasan at pati na rin na ang iyong serbisyo ay hindi napuno ng mga kahilingan.
- **Pagsusukat at Load balancing**. Maaari kang mag-set up ng bilang ng mga endpoints para i-balanse ang load at maaari mo ring piliin kung paano "load balance".
- **Mga tampok ng AI tulad ng semantic caching**, limitasyon ng token at pagmamanman ng token at marami pa. Ito ay mga mahusay na tampok na nagpapabuti ng pagiging mabilis ng tugon pati na rin tumutulong upang masubaybayan ang iyong paggastos sa token. [Basahin pa dito](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Bakit MCP + Azure API Management?

Ang Model Context Protocol ay mabilis na nagiging pamantayan para sa mga agentic AI apps at kung paano i-expose ang mga tools at data sa isang pare-parehong paraan. Ang Azure API Management ay isang natural na pagpipilian kapag kailangan mong "pamamahalaan" ang mga API. Ang mga MCP Servers ay madalas na nagsasama-sama sa ibang mga API upang lutasin ang mga kahilingan sa isang tool halimbawa. Kaya't ang pagsasama ng Azure API Management at MCP ay may malaking katuturan.

## Pangkalahatang Pagsusuri

Sa partikular na kaso na ito, matututuhan natin kung paano i-expose ang mga API endpoints bilang isang MCP Server. Sa pamamagitan nito, madali nating magagawa ang mga endpoints na ito bilang bahagi ng isang agentic app habang ginagamit din ang mga tampok mula sa Azure API Management.

## Mga Pangunahing Tampok

- Pinipili mo ang mga endpoint methods na nais mong i-expose bilang mga tools.
- Ang karagdagang mga tampok na makukuha mo ay depende sa kung ano ang i-configure mo sa seksyong patakaran para sa iyong API. Ngunit dito ipapakita namin paano magdagdag ng paghihigpit ng rate.

## Paunang hakbang: mag-import ng API

Kung mayroon ka nang API sa Azure API Management, mahusay, maaari mo nang laktawan ang hakbang na ito. Kung wala pa, tingnan ang link na ito, [pag-import ng API sa Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## I-expose ang API bilang MCP Server

Upang i-expose ang mga API endpoints, sundin natin ang mga hakbang na ito:

1. Pumunta sa Azure Portal at sa sumusunod na address <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Pumunta sa iyong API Management instance.

1. Sa kaliwang menu, piliin ang APIs > MCP Servers > + Lumikha ng bagong MCP Server.

1. Sa API, piliin ang REST API na ia-expose bilang MCP server.

1. Piliin ang isa o higit pang mga API Operations na ia-expose bilang mga tools. Maaari mong piliin lahat ng operasyon o mga partikular lamang.

    ![Piliin ang mga methods na ia-expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Piliin ang **Create**.

1. Pumunta sa opsyong menu na **APIs** at **MCP Servers**, makikita mo ang mga sumusunod:

    ![Makita ang MCP Server sa pangunahing pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Nabuo na ang MCP server at na-expose ang API operations bilang mga tools. Nakalista ang MCP server sa pane ng MCP Servers. Ang URL column ay nagpapakita ng endpoint ng MCP server na maaari mong tawagan para sa pagsubok o sa loob ng isang client application.

## Opsyonal: I-configure ang mga patakaran

Ang Azure API Management ay may pangunahing konsepto ng mga patakaran kung saan nagse-set up ka ng iba't ibang rules para sa iyong mga endpoints tulad ng halimbawa paghihigpit ng rate o semantic caching. Ang mga patakarang ito ay nililikha sa XML.

Ganito mo mae-set up ang patakaran upang paghigpitan ang rate ng iyong MCP Server:

1. Sa portal, sa ilalim ng APIs, piliin ang **MCP Servers**.

1. Piliin ang MCP server na nilikha mo.

1. Sa kaliwang menu, sa ilalim ng MCP, piliin ang **Policies**.

1. Sa policy editor, idagdag o i-edit ang mga patakaran na gusto mong i-apply sa mga tool ng MCP server. Ang mga patakaran ay nakasaad sa XML na format. Halimbawa, maaari kang magdagdag ng patakaran upang limitahan ang tawag sa mga tool ng MCP server (sa halimbawa na ito, 5 tawag bawat 30 segundo para sa bawat client IP address). Narito ang XML na magsasaad ng paghihigpit ng rate:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Narito ang isang larawan ng policy editor:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Subukan ito

Tiyakin nating gumagana ang ating MCP Server nang ayon sa inaasahan.

> [!NOTE]
> Ang Azure API Management ay kasalukuyang nag-eexpose ng server na ito sa pamamagitan ng Streamable
> HTTP `/mcp` endpoint. Ang dating HTTP+SSE `/sse` na transport ay hindi na ginagamit at
> dapat gamitin lamang sa mga legacy clients.

Para dito, gagamitin natin ang Visual Studio Code at GitHub Copilot kasama ang Agent mode nito. Idadagdag natin ang MCP server sa isang *mcp.json*. Sa paggawa nito, gagawin ng Visual Studio Code bilang client na may agentic capabilities at magagawa ng end users na mag-type ng prompt at makipag-ugnayan sa nasabing server.

Tingnan natin kung paano idagdag ang MCP server sa Visual Studio Code:

1. Gamitin ang MCP: **Add Server command mula sa Command Palette**.

1. Kapag na-prompt, piliin ang uri ng server: **HTTP (HTTP o Server Sent Events)**.

1. Ipasok ang Streamable HTTP URL na ipinakita para sa MCP server sa API Management.
    Halimbawa:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Magpasok ng server ID na iyong pipiliin. Hindi ito isang mahalagang halaga ngunit makakatulong ito upang maalala kung ano ang instance ng server na ito.

1. Piliin kung i-se-save ang configuration sa iyong workspace settings o user settings.

  - **Workspace settings** - Ang configuration ng server ay ise-save sa isang .vscode/mcp.json file na available lamang sa kasalukuyang workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - Ang configuration ng server ay idaragdag sa iyong global *settings.json* file at available sa lahat ng workspaces. Ang configuration ay katulad ng sumusunod:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Kailangan mo ring magdagdag ng configuration, isang header upang matiyak na ito ay ma-authenticate nang maayos patungo sa Azure API Management. Gumagamit ito ng header na tinatawag na **Ocp-Apim-Subscription-Key*.

    - Ganito mo ito madadagdag sa settings:

    ![Nagdaragdag ng header para sa authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ito ay magpapakita ng prompt para hilingin ang API key value na makikita mo sa Azure Portal para sa iyong Azure API Management instance.

   - Upang idagdag ito sa *mcp.json* sa halip, maaari mo itong idagdag ganito:

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

Ngayon ay handa na tayo, sa alin mang settings o sa *.vscode/mcp.json*. Subukan natin ito.

Dapat mayroong icon na Tools na ganito, kung saan nakalista ang mga exposed tools mula sa iyong server:

![Mga tool mula sa server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. I-click ang tools icon at makikita mo ang listahan ng mga tools na ganito:

    ![Mga tool](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Maglagay ng prompt sa chat upang tawagin ang tool. Halimbawa, kung pumili ka ng tool para kumuha ng impormasyon tungkol sa isang order, maaari mong tanungin ang ahente tungkol sa isang order. Narito ang isang halimbawa ng prompt:

    ```text
    get information from order 2
    ```

    Ngayon ipapakita sa iyo ang tools icon na nagtatanong kung gusto mong ipagpatuloy ang pagtawag sa tool. Piliin upang ipagpatuloy ang pagpapatakbo ng tool, makikita mo ngayon ang output na ganito:

    ![Resulta mula sa prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ang nakikita mo sa itaas ay depende sa mga tools na na-setup mo, ngunit ang ideya ay makakakuha ka ng text-based na tugon na tulad ng nasa itaas**


## Mga Sanggunian

Ganito mo matututuhan pa nang higit:

- [Tutorial sa Azure API Management at MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python sample: Secure remote MCP servers using Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client authorization lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gamitin ang Azure API Management extension para sa VS Code upang mag-import at pamahalaan ang mga API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Magrehistro at mag-discover ng mga remote MCP servers sa Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Napakagandang repo na nagpapakita ng maraming AI capabilities gamit ang Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Naglalaman ng mga workshop gamit ang Azure Portal, na isang mahusay na paraan upang simulan ang pagsusuri ng mga kakayahan ng AI.

## Ano ang Susunod

- Bumalik sa: [Pangkalahatang Pagsusuri ng Mga Pag-aaral ng Kaso](./README.md)
- Susunod: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->