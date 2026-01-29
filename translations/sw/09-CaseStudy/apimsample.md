# Uchunguzi wa Kesi: Kufichua REST API katika API Management kama seva ya MCP

Azure API Management ni huduma inayotoa lango juu ya sehemu za mwisho za API yako. Inavyofanya kazi ni kwamba Azure API Management hufanya kama wakala mbele ya API zako na inaweza kuamua nini cha kufanya na maombi yanayoingia.

Kwa kuitumia, unaongeza vipengele vingi kama:

- **Usalama**, unaweza kutumia kila kitu kutoka kwa funguo za API, JWT hadi utambulisho unaosimamiwa.
- **Kuweka kikomo cha kiwango**, kipengele kizuri ni uwezo wa kuamua ni simu ngapi zinapita kwa muda fulani. Hii husaidia kuhakikisha watumiaji wote wanapata uzoefu mzuri na pia huduma yako haizidiwi na maombi.
- **Kuweka mizani na usawa wa mzigo**. Unaweza kusanidi idadi ya sehemu za mwisho ili kusawazisha mzigo na pia unaweza kuamua jinsi ya "kusawazisha mzigo".
- **Vipengele vya AI kama akiba ya semantiki**, kikomo cha tokeni na ufuatiliaji wa tokeni na zaidi. Hivi ni vipengele bora vinavyoboresha mwitikio na pia vinakusaidia kufuatilia matumizi ya tokeni zako. [Soma zaidi hapa](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Kwa nini MCP + Azure API Management?

Model Context Protocol inakuwa haraka kiwango cha programu za AI zenye mawakala na jinsi ya kufichua zana na data kwa njia thabiti. Azure API Management ni chaguo la asili unapohitaji "kusimamia" API. Seva za MCP mara nyingi huunganishwa na API nyingine kutatua maombi kwa zana kwa mfano. Kwa hivyo, kuchanganya Azure API Management na MCP kuna mantiki sana.

## Muhtasari

Katika kesi hii maalum, tutajifunza jinsi ya kufichua sehemu za mwisho za API kama seva ya MCP. Kwa kufanya hivyo, tunaweza kwa urahisi kufanya sehemu hizi za mwisho kuwa sehemu ya programu yenye mawakala huku tukitumia vipengele vya Azure API Management.

## Vipengele Muhimu

- Unachagua mbinu za sehemu za mwisho unazotaka kufichua kama zana.
- Vipengele vya ziada unavyopata vinategemea kile unachosanidi katika sehemu ya sera kwa API yako. Lakini hapa tutaonyesha jinsi unavyoweza kuongeza kikomo cha kiwango.

## Hatua ya awali: kuingiza API

Ikiwa tayari una API katika Azure API Management ni vizuri, basi unaweza kuruka hatua hii. Ikiwa sivyo, angalia kiungo hiki, [kuingiza API katika Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Kufichua API kama Seva ya MCP

Ili kufichua sehemu za mwisho za API, fuata hatua hizi:

1. Tembelea Azure Portal kwa anwani ifuatayo <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Tembelea mfano wako wa API Management.

1. Katika menyu ya kushoto, chagua APIs > MCP Servers > + Unda seva mpya ya MCP.

1. Katika API, chagua REST API kufichua kama seva ya MCP.

1. Chagua moja au zaidi ya Operesheni za API kufichua kama zana. Unaweza kuchagua operesheni zote au operesheni maalum tu.

    ![Chagua mbinu za kufichua](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Chagua **Unda**.

1. Tembelea chaguo la menyu **APIs** na **MCP Servers**, unapaswa kuona yafuatayo:

    ![Tazama seva ya MCP katika paneli kuu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Seva ya MCP imeundwa na operesheni za API zimefichuliwa kama zana. Seva ya MCP imeorodheshwa katika paneli ya MCP Servers. Safu ya URL inaonyesha sehemu ya mwisho ya seva ya MCP ambayo unaweza kupiga kwa majaribio au ndani ya programu ya mteja.

## Hiari: Sanidi sera

Azure API Management ina dhana kuu ya sera ambapo unaseti sheria tofauti kwa sehemu zako za mwisho kama kwa mfano kuweka kikomo cha kiwango au akiba ya semantiki. Sera hizi zinaandikwa kwa XML.

Hivi ndivyo unavyoweza kusanidi sera ya kuweka kikomo cha kiwango kwa seva yako ya MCP:

1. Katika portal, chini ya APIs, chagua **MCP Servers**.

1. Chagua seva ya MCP uliyounda.

1. Katika menyu ya kushoto, chini ya MCP, chagua **Policies**.

1. Katika mhariri wa sera, ongeza au hariri sera unazotaka kutumia kwa zana za seva ya MCP. Sera zinafafanuliwa kwa muundo wa XML. Kwa mfano, unaweza kuongeza sera ya kuweka kikomo cha simu kwa zana za seva ya MCP (katika mfano huu, simu 5 kwa sekunde 30 kwa kila anwani ya IP ya mteja). Hapa kuna XML itakayosababisha kuweka kikomo cha kiwango:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Hapa kuna picha ya mhariri wa sera:

    ![Mhariri wa sera](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Jaribu

Tuhakikishe seva yetu ya MCP inafanya kazi kama ilivyokusudiwa.

Kwa hili, tutatumia Visual Studio Code na GitHub Copilot na hali yake ya Mawakala. Tutaongeza seva ya MCP kwenye faili ya *mcp.json*. Kwa kufanya hivyo, Visual Studio Code itafanya kazi kama mteja mwenye uwezo wa mawakala na watumiaji wa mwisho wataweza kuandika maelekezo na kuingiliana na seva hiyo.

Hivi ndivyo, kuongeza seva ya MCP katika Visual Studio Code:

1. Tumia MCP: **Amri ya Ongeza Seva kutoka kwa Command Palette**.

1. Unapoulizwa, chagua aina ya seva: **HTTP (HTTP au Server Sent Events)**.

1. Ingiza URL ya seva ya MCP katika API Management. Mfano: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (kwa sehemu ya mwisho ya SSE) au **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (kwa sehemu ya mwisho ya MCP), angalia jinsi tofauti kati ya usafirishaji ni `/sse` au `/mcp`.

1. Ingiza ID ya seva ya chaguo lako. Hii si thamani muhimu lakini itakusaidia kukumbuka seva hii ni nini.

1. Chagua ikiwa kuhifadhi usanidi kwenye mipangilio ya workspace yako au mipangilio ya mtumiaji.

  - **Mipangilio ya workspace** - Usanidi wa seva umehifadhiwa kwenye faili ya .vscode/mcp.json inayopatikana tu katika workspace ya sasa.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    au ikiwa unachagua HTTP ya kusambaza kama usafirishaji itakuwa tofauti kidogo:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Mipangilio ya mtumiaji** - Usanidi wa seva umeongezwa kwenye faili yako ya *settings.json* ya kimataifa na inapatikana katika workspace zote. Usanidi unaonekana kama ifuatavyo:

    ![Mipangilio ya mtumiaji](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Unahitaji pia kuongeza usanidi, kichwa ili kuhakikisha inathibitisha vizuri kuelekea Azure API Management. Inatumia kichwa kinachoitwa **Ocp-Apim-Subscription-Key**.

    - Hivi ndivyo unavyoweza kuongeza kwenye mipangilio:

    ![Kuongeza kichwa kwa uthibitisho](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), hii itasababisha maelekezo kuonyeshwa kukuuliza thamani ya funguo ya API ambayo unaweza kupata katika Azure Portal kwa mfano wako wa Azure API Management.

   - Ili kuongeza kwenye *mcp.json* badala yake, unaweza kuongeza kama ifuatavyo:

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

### Tumia hali ya Mawakala

Sasa tumesanidi katika mipangilio au katika *.vscode/mcp.json*. Hebu tujaribu.

Kunapaswa kuwa na ikoni ya Zana kama ifuatavyo, ambapo zana zilizofichuliwa kutoka kwa seva yako zimeorodheshwa:

![Zana kutoka kwa seva](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Bonyeza ikoni ya zana na unapaswa kuona orodha ya zana kama ifuatavyo:

    ![Zana](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Ingiza maelekezo katika mazungumzo ili kuamsha zana. Kwa mfano, ikiwa umechagua zana ya kupata taarifa kuhusu agizo, unaweza kuuliza wakala kuhusu agizo. Hapa kuna mfano wa maelekezo:

    ```text
    get information from order 2
    ```

    Sasa utaonyeshwa na ikoni ya zana inayokuuliza kuendelea kuita zana. Chagua kuendelea kuendesha zana, unapaswa sasa kuona matokeo kama ifuatavyo:

    ![Matokeo kutoka kwa maelekezo](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **kile unachokiona hapo juu kinategemea zana ulizosanidi, lakini wazo ni kwamba unapata majibu ya maandishi kama hapo juu**

## Marejeleo

Hivi ndivyo unavyoweza kujifunza zaidi:

- [Mafunzo kuhusu Azure API Management na MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Mfano wa Python: Linda seva za MCP za mbali kwa kutumia Azure API Management (majaribio)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Maabara ya idhini ya mteja wa MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Tumia kiendelezi cha Azure API Management kwa VS Code kuingiza na kusimamia API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Sajili na gundua seva za MCP za mbali katika Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Hifadhi nzuri inayoonyesha uwezo mwingi wa AI na Azure API Management
- [Warsha za AI Gateway](https://azure-samples.github.io/AI-Gateway/) Inayo warsha zinazotumia Azure Portal, ambayo ni njia nzuri ya kuanza kutathmini uwezo wa AI.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.