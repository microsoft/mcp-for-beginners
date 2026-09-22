# Uchunguzi wa Kesi: Kufichua REST API katika Usimamizi wa API kama seva ya MCP

Azure API Management, ni huduma inayotoa Mlango wa kuingia juu ya Vituo vyako vya API. Inavyofanya kazi ni kwamba Azure API Management hufanya kazi kama wakala mbele ya API zako na inaweza kuamua nini cha kufanya na maombi yanayoingia.

Kwa kuitumia, unaongeza vipengele vingi kama:

- **Usalama**, unaweza kutumia kila kitu kutoka kwa funguo za API, JWT mpaka kitambulisho kinachosimamiwa.
- **Kuzuia kiwango cha maombi**, kipengele kizuri ni uwezo wa kuamua ni maombi mangapi yanayopitishwa kwa kipindi fulani cha wakati. Hii husaidia kuhakikisha watumiaji wote wanapata uzoefu mzuri na pia huduma yako haibidiwi na maombi mengi mno.
- **Kupanda kwa kiwango & Usawazishaji mzigo**. Unaweza kuweka idadi ya vituo kusawazisha mzigo na pia unaweza kuamua jinsi ya "kusawazisha mzigo".
- **Vipengele vya AI kama kuhifadhi kumbukumbu ya maana**, kikomo cha tokeni na ufuatiliaji wa tokeni na zaidi. Hizi ni vipengele bora vinavyoongeza mwitikio pamoja na kusaidia kufuatilia matumizi yako ya tokeni. [Soma zaidi hapa](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Kwa Nini MCP + Azure API Management?

Model Context Protocol inaendelea kuwa kiwango kwa haraka kwa programu za AI zenye mawakala na jinsi ya kufichua zana na data kwa njia thabiti. Azure API Management ni chaguo la asili unapotaka "kusimamia" APIs. Seva za MCP mara nyingi huunganishwa na APIs zingine kutatua maombi kwa zana kwa mfano. Kwa hiyo kuunganisha Azure API Management na MCP kuna maana kubwa.

## Muhtasari

Katika mfano huu maalum tutaelewa kufichua vituo vya API kama Seva ya MCP. Kwa kufanya hivi, tunaweza kwa urahisi kufanya vituo hivi sehemu ya programu yenye mawakala huku tukitumia pia vipengele kutoka Azure API Management.

## Vipengele Muhimu

- Unachagua njia za kituo unazotaka kufichua kama zana.
- Vipengele vya ziada unavyopata vinategemea kile unachoweka katika sehemu ya sera kwa API yako. Lakini hapa tutakuonyesha jinsi ya kuongeza kuzuia kiwango cha maombi.

## Hatua ya awali: ingiza API

Ikiwa tayari una API katika Azure API Management nzuri, basi unaweza kuruka hatua hii. Ikiwa huna, angalia kiungo hiki, [kuingiza API katika Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Fichua API kama Seva ya MCP

Kufichua vituo vya API, tufuate hatua hizi:

1. Nenda kwenye Azure Portal na anwani ifuatayo <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Nenda kwenye mfano wa Usimamizi wa API wako.

1. Katika menyu ya kushoto, chagua APIs > Seva za MCP > + Unda seva mpya ya MCP.

1. Katika API, chagua REST API kufichua kama seva ya MCP.

1. Chagua moja au zaidi ya Operesheni za API kufichua kama zana. Unaweza kuchagua operesheni zote au operesheni maalum tu.

    ![Teua njia za kufichua](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Chagua **Unda**.

1. Nenda kwenye chaguo la menyu **APIs** na **Seva za MCP**, unapaswa kuona yafuatayo:

    ![Ona seva ya MCP kwenye dirisha kuu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Seva ya MCP imetengenezwa na operesheni za API zimefichuliwa kama zana. Seva ya MCP inaorodheshwa kwenye dirisha la Seva za MCP. Safu ya URL inaonyesha kituo cha seva ya MCP ambacho unaweza kuita kwa ajili ya majaribio au ndani ya programu ya mteja.

## Hiari: Sanidi sera

Azure API Management ina dhana kuu ya sera ambapo unaweka sheria tofauti kwa vituo vyako kama vile kuzuia kiwango cha maombi au kuhifadhi kumbukumbu ya maana. Sera hizi zinaandikwa kwa XML.

Hapa ni jinsi unavyoweza kuweka sera ya kuzuia kiwango cha maombi kwenye seva yako ya MCP:

1. Katika portal, chini ya APIs, chagua **Seva za MCP**.

1. Chagua seva ya MCP uliyotengeneza.

1. Katika menyu ya kushoto, chini ya MCP, chagua **Sera**.

1. Katika mhariri wa sera, ongeza au hariri sera unazotaka kutumia kwa zana za seva ya MCP. Sera zinafafanuliwa kwa mtindo wa XML. Kwa mfano, unaweza kuongeza sera ya kuzuia simu kwenda kwa zana za seva ya MCP (katika mfano huu, simu 5 kwa sekunde 30 kwa kila anwani ya IP ya mteja). Hii ni XML itakayofanya kuzuia kiwango cha maombi:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Hii ni picha ya mhariri wa sera:

    ![Mhariri wa sera](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Jaribu

Tukihakikishe seva yetu ya MCP inafanya kazi kama inavyotarajiwa.

> [!NOTE]
> Azure API Management kwa sasa inafichua seva hii kupitia
> kiungo cha HTTP cha Streamable `/mcp`. Usafirishaji wa zamani wa HTTP+SSE `/sse`
> umekwisha na unapaswa kutumiwa tu na wateja wa kale.

Kwa hili, tutatumia Visual Studio Code na GitHub Copilot na mode yake ya Wakala. Tutatoa seva ya MCP katika *mcp.json* wakati huu. Kwa kufanya hivyo, Visual Studio Code itafanya kazi kama mteja mwenye uwezo wa wakala na watumiaji wa mwisho wataweza kuandika ombi na kuingiliana na seva hiyo.

Tazama jinsi ya kuongeza seva ya MCP katika Visual Studio Code:

1. Tumia amri ya MCP: **Ongeza Seva kutoka kwenye Menu ya Amri**.

1. Inapoulizwa, chagua aina ya seva: **HTTP (HTTP au Server Sent Events)**.

1. Ingiza URL ya Streamable HTTP iliyoonyeshwa kwa seva ya MCP katika Usimamizi wa API.
    Kwa mfano:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Ingiza kitambulisho cha seva unachochagua. Hii si thamani muhimu lakini itakusaidia kukumbuka seva hii ni ya nini.

1. Chagua kama utahifadhi usanidi kwenye mipangilio ya eneo la kazi au mipangilio ya mtumiaji.

  - **Mipangilio ya eneo la kazi** - Usanidi wa seva unahifadhiwa kwenye faili la .vscode/mcp.json linalopatikana tu kwenye eneo lako la kazi.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Mipangilio ya mtumiaji** - Usanidi wa seva unaongezwa kwenye faili yako ya jumla *settings.json* na unapatikana katika maeneo yote ya kazi. Usanidi unaonekana kama ifuatavyo:

    ![Mipangilio ya mtumiaji](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Pia unahitaji kuongeza usanidi, kichwa cha maombi ili kuhakikisha kinathibitishwa ipasavyo kuelekea Azure API Management. Kinatumia kichwa kinachoitwa **Ocp-Apim-Subscription-Key**.

    - Hapa ni jinsi unavyoweza kuiongeza kwenye mipangilio:

    ![Kuongeza kichwa cha kuthibitisha](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), hii itasababisha onyesho la maombi la kuweka thamani ya funguo ya API ambayo unaweza kupata Azure Portal kwa mfano wako wa Azure API Management.

   - Ili kuiweka katika *mcp.json* badala yake, unaweza kuiongeza kama ifuatavyo:

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

### Tumia mode ya Wakala

Sasa tumeshaanza usanidi katika mipangilio au katika *.vscode/mcp.json*. Hebu itumie.

Kwenye dirisha la zana kuna ikoni ya zana kama hii, ambapo zana zilizofichuliwa kutoka kwenye seva yako zinaorodheshwa:

![Zana kutoka kwenye seva](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Bonyeza ikoni ya zana na utapokea orodha ya zana kama hii:

    ![Zana](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Ingiza ombi kwenye mazungumzo kuomba zana ifanyike. Kwa mfano, kama umechagua zana ya kupata taarifa kuhusu agizo, unaweza kumuuliza wakala kuhusu agizo. Huu ni mfano wa ombi:

    ```text
    get information from order 2
    ```

    Sasa utaonyeshwa ikoni ya zana ikikuomba uendelee kutumia zana. Chagua kuendelea kuitumia zana, sasa utapokea matokeo kama haya:

    ![Matokeo kutoka kwenye ombi](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **kile unachoona hapo juu kinategemea zana ulizoweka, lakini wazo ni kwamba unapata jibu la maandishi kama lile hapo juu**


## Marejeleo

Hapa ni jinsi unavyoweza kujifunza zaidi:

- [Mafunzo kuhusu Azure API Management na MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Mfano wa Python: Kuhakikisha seva za MCP za mbali kwa kutumia Azure API Management (jaribio)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Maabara ya idhini ya mteja wa MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Tumia nyongeza ya Azure API Management kwa VS Code kuingiza na kusimamia APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Jisajili na gundua seva za MCP za mbali katika Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Reposi nzuri inayonyesha uwezo mwingi wa AI kwa Azure API Management
- [Warsha za AI Gateway](https://azure-samples.github.io/AI-Gateway/) Zinajumuisha warsha kwa kutumia Azure Portal, ambayo ni njia nzuri ya kuanza kutathmini uwezo wa AI.

## Nini Kifuatayo

- Rudi kwa: [Muhtasari wa Uchunguzi wa Kesi](./README.md)
- Ifuatayo: [Wakala wa Safari wa Azure AI](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->