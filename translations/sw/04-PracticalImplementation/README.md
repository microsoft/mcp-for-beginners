# Utekelezaji wa Kivitendo

[![Jinsi ya Kujenga, Kupima, na Kutoa Programu za MCP kwa Vifaa na Mifumo halisi ya Kazi](../../../translated_images/sw/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Bonyeza picha juu ili kutazama video ya somo hili)_

Utekelezaji wa kivitendo ndiko nguvu ya Itifaki ya Muktadha wa Mfano (MCP) inapoonekana wazi. Wakati kuelewa nadharia na usanifu nyuma ya MCP ni muhimu, thamani halisi huibuka unapoweka dhana hizi katika matumizi kujenga, kupima, na kutoa suluhisho zinazotatua matatizo halisi ya dunia. Sura hii inaziba pengo kati ya maarifa ya dhana na maendeleo ya vitendo, ikiongoza kupitia mchakato wa kuleta programu za msingi wa MCP kuishi.

Iwe unafanya maendeleo ya wasaidizi wa akili, kuunganisha AI katika mifumo ya biashara, au kujenga zana maalum za usindikaji wa data, MCP hutoa msingi wenye kubadilika. Muundo wake usio tegemea lugha na SDK rasmi kwa lugha maarufu za programu hufanya iwe rahisi kufikiwa na watengenezaji wengi. Kwa kutumia SDK hizi, unaweza haraka kuunda mifano, kurudia, na kupanua suluhisho zako katika majukwaa na mazingira tofauti.

Katika sehemu zilizo fuata, utapata mifano ya vitendo, nambari za sampuli, na mikakati ya utoaji inayobainisha jinsi ya kutekeleza MCP kwa C#, Java na Spring, TypeScript, JavaScript, na Python. Pia utajifunza jinsi ya kutatua matatizo na kupima seva zako za MCP, kusimamia API, na kutoa suluhisho kwenye wingu kwa kutumia Azure. Vifaa hivi vya vitendo vimeundwa kuharakisha kujifunza kwako na kukusaidia kujenga kwa kujiamini programu thabiti za MCP zinazotumika uzalishaji.

## Muhtasari

Somo hili linazingatia nyanja za vitendo za utekelezaji wa MCP katika lugha mbalimbali za programu. Tutachunguza jinsi ya kutumia SDK za MCP katika C#, Java na Spring, TypeScript, JavaScript, na Python kujenga programu thabiti, kutatua matatizo na kupima seva za MCP, na kuunda rasilimali, maelekezo, na zana zinazoweza kutumika tena.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kutekeleza suluhisho za MCP kwa kutumia SDK rasmi katika lugha mbalimbali za programu
- Kutatua matatizo na kupima seva za MCP kwa mfumo
- Kuunda na kutumia vipengele vya seva (Rasilimali, Maelekezo, na Zana)
- Kubuni mifumo ya kazi ya MCP yenye ufanisi kwa kazi ngumu
- Kuboresha utekelezaji wa MCP kwa utendaji na uaminifu

## Rasilimali Rasmi za SDK

Itifaki ya Muktadha wa Mfano hutoa SDK rasmi kwa lugha nyingi (zingine zikifuata [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java na Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Kumbuka:** inahitaji tegemezi ya [Project Reactor](https://projectreactor.io). (Tazama [mjadala nambari 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Kazi na SDK za MCP

Sehemu hii hutoa mifano ya vitendo ya utekelezaji wa MCP katika lugha mbalimbali za programu. Unaweza kupata nambari za sampuli kwenye saraka ya `samples` iliyopangwa kwa lugha.

### Sampuli Zinazopatikana

Hifadhi ina [utekelezaji wa sampuli](../../../04-PracticalImplementation/samples) katika lugha zifuatazo:

- [C#](./samples/csharp/README.md)
- [Java na Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Kila sampuli inaonyesha dhana kuu za MCP na mifumo ya utekelezaji kwa lugha na mfumo maalum.

### Mwongozo wa Vitendo

Mwongozo zaidi wa utekelezaji wa vitendo wa MCP:

- [Paginations na Seti Kubwa za Matokeo](./pagination/README.md) - Shughulikia paginations inayotegemea cursor kwa zana, rasilimali, na data kubwa

## Vipengele Muhimu vya Seva

Seva za MCP zinaweza kutekeleza mchanganyiko wowote wa vipengele hivi:

### Rasilimali

Rasilimali hutoa muktadha na data kwa mtumiaji au mfano wa AI kutumia:

- Makusanyo ya hati
- Misingi ya maarifa
- Vyanzo vya data vilivyopangwa
- Mifumo ya faili

### Maelekezo

Maelekezo ni ujumbe wa kiolezo na michakato kwa watumiaji:

- Violezo vya mazungumzo yaliyowekwa awali
- Mifumo ya mawasiliano inayotegemewa
- Miundo maalum ya mazungumzo

### Zana

Zana ni kazi kwa mfano wa AI kutekeleza:

- Zana za usindikaji data
- Uingiaji wa API wa nje
- Uwezo wa kompyuta
- Utafutaji

## Utekelezaji wa Sampuli: Utekelezaji wa C#

Hifadhi rasmi ya SDK ya C# ina utekelezaji kadhaa wa sampuli unaoonyesha nyanja tofauti za MCP:

- **Mteja wa MCP wa Msingi**: Mfano rahisi unaoonyesha jinsi ya kuunda mteja wa MCP na kuita zana
- **Seva ya MCP ya Msingi**: Utekelezaji mdogo wa seva yenye usajili wa zana za msingi
- **Seva ya MCP ya Juu**: Seva yenye vipengele kamili na usajili wa zana, uthibitishaji, na utambuzi wa makosa
- **Uingiliaji wa ASP.NET**: Mifano inayothibitisha uingizaji na ASP.NET Core
- **Mifumo ya Utekelezaji wa Zana**: Mifano mbalimbali ya kutekeleza zana kwa ngazi tofauti za ugumu

SDK ya MCP ya C# bado iko kwenye awamu ya majaribio na API zinaweza kubadilika. Tutaendelea kusasisha blogu hii kadri SDK inavyoendelea.

### Vipengele Muhimu

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Kuunda [Seva yako ya MCP ya kwanza](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Kwa sampuli kamili za utekelezaji wa C#, tembelea [hifadhi rasmi ya sampuli za SDK ya C#](https://github.com/modelcontextprotocol/csharp-sdk)

## Utekelezaji wa Sampuli: Utekelezaji wa Java na Spring

SDK ya Java na Spring hutoa chaguzi madhubuti za utekelezaji wa MCP zenye vipengele vya daraja la biashara.

### Vipengele Muhimu

- Uingiliaji wa Spring Framework
- Usalama wa aina thabiti
- Msaada wa programu za kuingiliana zinazotegemea matukio
- Uendeshaji wa makosa kwa kina

Kwa sampuli kamili ya utekelezaji wa Java na Spring, ona [sampuli ya Java na Spring](samples/java/containerapp/README.md) katika saraka ya sampuli.

## Utekelezaji wa Sampuli: Utekelezaji wa JavaScript

SDK ya JavaScript hutoa njia nyepesi na inayobadilika kwa utekelezaji wa MCP.

### Vipengele Muhimu

- Msaada wa Node.js na kivinjari
- API inayotegemea ahadi (Promise)
- Uingiliaji rahisi na Express na mifumo mingine
- Msaada wa WebSocket kwa utiririshaji

Kwa sampuli kamili ya utekelezaji wa JavaScript, ona [sampuli ya JavaScript](samples/javascript/README.md) katika saraka ya sampuli.

## Utekelezaji wa Sampuli: Utekelezaji wa Python

SDK ya Python hutoa njia ya pythonic ya utekelezaji wa MCP pamoja na uunganisho bora wa mifumo ya ML.

### Vipengele Muhimu

- Msaada wa async/await kupitia asyncio
- Uingiliaji na FastAPI
- Usajili wa zana rahisi
- Uingiliaji wa asili na maktaba maarufu za ML

Kwa sampuli kamili ya utekelezaji wa Python, ona [sampuli ya Python](samples/python/README.md) katika saraka ya sampuli.

## Usimamizi wa API

Usimamizi wa API wa Azure ni jibu bora kwa jinsi tunavyoweza kuimarisha seva za MCP. Dhana ni kuweka mfano wa Usimamizi wa API wa Azure mbele ya seva yako ya MCP na kuruhusu iendeshe vipengele unavyotaka kama:

- ukomo wa kiwango cha maombi
- usimamizi wa tokeni
- ufuatiliaji
- usawazishaji mzigo
- usalama

### Sampuli ya Azure

Hii ni Sampuli ya Azure inayofanya hasa hivyo, yaani [kuunda Seva ya MCP na kuilinda kwa Usimamizi wa API wa Azure](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Tazama jinsi mchakato wa idhini unavyotokea katika picha ifuatayo:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Katika picha hapo juu, yafuatayo hutokea:

- Uthibitishaji/Idhini hufanyika kutumia Microsoft Entra.
- Usimamizi wa API wa Azure hufanya kazi kama lango na hutumia sera kuongoza na kusimamia trafiki.
- Azure Monitor hurekodi maombi yote kwa uchambuzi zaidi.

#### Mtiririko wa idhini

Tuchunguze mtiririko wa idhini kwa kina zaidi:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Maelezo ya idhini ya MCP

Jifunza zaidi kuhusu [maelezo ya idhini ya MCP](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Toa Seva ya MCP ya Mbali kwenye Azure

Tutaona kama tunaweza kutoa sampuli tuliyoitaja awali:

1. Nakili hifadhi ya mradi

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Sajili mtoa huduma wa rasilimali `Microsoft.App`.

   - Ikiwa unatumia Azure CLI, endesha `az provider register --namespace Microsoft.App --wait`.
   - Ikiwa unatumia Azure PowerShell, endesha `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Kisha endesha `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` baada ya muda kuchunguza kama usajili umekamilika.

1. Endesha amri hii ya [azd](https://aka.ms/azd) kuandaa huduma ya usimamizi wa api, app ya kazi (ikiwa na nambari) na rasilimali zote zinazohitajika za Azure

    ```shell
    azd up
    ```

    Amri hii inapaswa kutoa rasilimali zote za wingu kwenye Azure

### Kupima seva yako kwa MCP Inspector

1. Katika **dirisha jipya la terminal**, sanidi na endesha MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Unapaswa kuona kiolesura kinachofanana na hiki:

    ![Unganisha na Node inspector](../../../translated_images/sw/connect.141db0b2bd05f096.webp)

1. Bonyeza CTRL upakue app ya wavuti ya MCP Inspector kutoka kwenye URL inayoonyeshwa na app (mfano [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Weka aina ya usafirishaji kuwa `SSE`
1. Weka URL ya kitakasa SSE cha Usimamizi wa API kinachoendesha baada ya `azd up` na **Unganisha**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Orodha ya Zana**. Bonyeza zana na **Endesha Zana**.

Kama hatua zote zimefanikiwa, sasa unapaswa kuunganishwa na seva ya MCP na umeweza kuita zana.

## Seva za MCP kwa Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Seti hii ya hifadhi ni kiolezo cha kuanza haraka kwa kujenga na kutoa seva za MCP za mbali (Model Context Protocol) kwa kutumia Azure Functions kwa Python, C# .NET au Node/TypeScript.

Sampuli hutoa suluhisho kamili zinazomruhusu mtaalamu wa maendeleo:

- Kujenga na kuendesha kwa eneo la karibu: Tengeneza na tatua matatizo ya seva ya MCP kwenye mashine yako
- Kutoa kwa Azure: Toa kwa urahisi kwenye wingu kwa amri rahisi ya azd up
- Kuungana na wateja: Unganisha na seva ya MCP kutoka kwa wateja mbalimbali ikiwa ni pamoja na hali ya wakala wa Copilot wa VS Code na zana ya MCP Inspector

### Vipengele Muhimu

- Usalama kwa muundo: Seva ya MCP inalindwa kwa kutumia funguo na HTTPS
- Chaguzi za uthibitishaji: Inasaidia OAuth kwa kutumia uthibitishaji wa ndani na/au Usimamizi wa API
- Kutenganisha mtandao: Kuruhusu kutenganishwa mtandao kwa kutumia Azure Virtual Networks (VNET)
- Usaidizi wa usanifu usio na seva: Inatumia Azure Functions kwa utekelezaji unaoendeka na matukio
- Maendeleo ya eneo la karibu: Usaidizi kamili wa maendeleo na tatizo la eneo la karibu
- Utoaji rahisi: Mchakato ulio rahisishwa wa utoaji kwenye Azure

Hifadhi ina faili zote muhimu za usanidi, nambari za chanzo, na maelezo ya miundombinu ili kuanza haraka na utekelezaji wa seva ya MCP inayotumika uzalishaji.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Utekelezaji wa sampuli wa MCP kwa kutumia Azure Functions na Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Utekelezaji wa sampuli wa MCP kwa kutumia Azure Functions na C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Utekelezaji wa sampuli wa MCP kwa kutumia Azure Functions na Node/TypeScript.

## Muhimu Kusoma

- SDK za MCP hutoa zana maalum za lugha kutekeleza suluhisho thabiti za MCP
- Mchakato wa kutatua matatizo na kupima ni muhimu kwa programu za MCP zenye kuaminika
- Violezo vya maelekezo vinavyoweza kutumiwa tena huruhusu mwingiliano mzuri wa AI
- Mifumo mizuri ya kazi inaweza kuendesha kazi ngumu kwa kutumia zana nyingi
- Kutekeleza suluhisho za MCP kunahitaji kuzingatia usalama, utendaji, na utambuzi wa makosa

## Zoee

Buni mfumo wa kazi wa MCP unaoshughulikia tatizo halisi katika eneo lako:

1. Tambua zana 3-4 ambazo zingekuwa na msaada katika kutatua tatizo hili
2. Tengeneza mchoro wa mfumo wa kazi unaoonyesha jinsi zana hizi zinavyoshirikiana
3. Tekeleza toleo la msingi la mojawapo ya zana ukitumia lugha unayopendelea
4. Tengeneza kiolezo cha maelekezo kitakachomsaidia mfano kutumia zana yako kwa ufanisi

## Rasilimali Zaidi

---

## Ifuatayo

Ifuatayo: [Mada Zaidi](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tangazo la Kutolewa Lawama**:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya utafsiri wa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Wakati tunajitahidi kufanikisha usahihi, tafadhali fahamu kwamba tafsiri za otomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Nyaraka ya awali kwa lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubeba dhima kwa uelewa mbaya au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->