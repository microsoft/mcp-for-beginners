# Praktikal na Implementasyon

[![Paano Magtayo, Mag-test, at Mag-deploy ng MCP Apps gamit ang Totoong Mga Tool at Workflow](../../../translated_images/tl/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

Ang praktikal na implementasyon ang nagiging konkreto ng kapangyarihan ng Model Context Protocol (MCP). Habang mahalagang maunawaan ang teorya at arkitektura sa likod ng MCP, ang tunay na halaga ay lumilitaw kapag inilapat mo ang mga konseptong ito upang bumuo, mag-test, at mag-deploy ng mga solusyon na lumulutas sa mga tunay na problema sa mundo. Binubuo ng kabanatang ito ang pagitan ng konseptwal na kaalaman at praktikal na pag-unlad, na ginagabayan ka sa proseso ng pagbuhay ng mga aplikasyon na nakabase sa MCP.

Kung ikaw man ay nagde-develop ng mga intelligent assistant, nag-iintegrate ng AI sa mga business workflow, o bumubuo ng mga custom na tool para sa pagproseso ng data, nagbibigay ang MCP ng isang flexible na pundasyon. Ang language-agnostic na disenyo nito at opisyal na mga SDK para sa mga popular na programming language ay ginagawang accessible sa malawak na saklaw ng mga developer. Sa pamamagitan ng paggamit ng mga SDK na ito, maaari kang mabilis na mag-prototype, mag-iterate, at mag-scale ng iyong mga solusyon sa iba't ibang platform at mga kapaligiran.

Sa mga sumusunod na seksyon, makakakita ka ng mga praktikal na halimbawa, sample code, at mga estratehiya sa pag-deploy na nagpapakita kung paano i-implement ang MCP sa C#, Java gamit ang Spring, TypeScript, JavaScript, at Python. Malalaman mo rin kung paano i-debug at i-test ang iyong mga MCP server, pamahalaan ang mga API, at mag-deploy ng mga solusyon sa cloud gamit ang Azure. Ang mga praktikal na resources na ito ay nilikha upang pabilisin ang iyong pag-aaral at tulungan kang tiwalang bumuo ng matatag at handang gamitin sa produksiyon na mga aplikasyon ng MCP.

## Pangkalahatang Ideya

Nakatuon ang araling ito sa praktikal na mga aspeto ng implementasyon ng MCP sa iba't ibang programming language. Susuriin natin kung paano gamitin ang MCP SDK sa C#, Java gamit ang Spring, TypeScript, JavaScript, at Python upang bumuo ng matitibay na aplikasyon, mag-debug at mag-test ng MCP server, at gumawa ng mga reusable na resources, prompt, at mga tool.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- I-implement ang mga solusyon ng MCP gamit ang opisyal na SDK sa iba't ibang programming language
- Sistematikong mag-debug at mag-test ng mga MCP server
- Gumawa at gumamit ng mga feature ng server (Mga Resources, Prompts, at Mga Tool)
- Magdisenyo ng epektibong mga workflow ng MCP para sa mga kumplikadong gawain
- I-optimize ang mga implementasyon ng MCP para sa performance at pagiging maaasahan

## Opisyal na SDK na Mga Resource

Nag-aalok ang Model Context Protocol ng opisyal na mga SDK para sa maraming wika (ayon sa [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java gamit ang Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Tandaan:** nangangailangan ng dependency sa [Project Reactor](https://projectreactor.io). (Tingnan ang [discussion issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Paggamit ng MCP SDK

Nagbibigay ang seksyong ito ng mga praktikal na halimbawa ng implementasyon ng MCP sa iba't ibang programming language. Makikita mo ang sample code sa `samples` direktoryo na nakaayos ayon sa wika.

### Magagamit na Mga Sample

Ang repositoryo ay naglalaman ng [mga sample na implementasyon](../../../04-PracticalImplementation/samples) sa mga sumusunod na wika:

- [C#](./samples/csharp/README.md)
- [Java gamit ang Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Bawat sample ay nagpapakita ng mga susi na konsepto at pattern ng implementasyon ng MCP para sa partikular na wika at ecosystem.

### Praktikal na Mga Gabay

Mga karagdagang gabay para sa praktikal na implementasyon ng MCP:

- [Pagination at Malalaking Result Set](./pagination/README.md) - Pamahalaan ang cursor-based na pagination para sa mga tool, resources, at malalaking dataset

## Pangunahing Mga Feature ng Server

Maaaring mag-implement ang mga MCP server ng anumang kumbinasyon ng mga feature na ito:

### Mga Resources

Nagbibigay ang mga resource ng konteksto at data para magamit ng user o AI model:

- Dokumentong repositoryo
- Mga knowledge base
- Mga naka-istrukturang data sources
- File system

### Mga Prompt

Ang mga prompt ay mga templated na mensahe at workflow para sa mga user:

- Paunang itinakdang mga template ng usapan
- Pinapatnubayang pattern ng interaksyon
- Espesyal na istruktura ng diyalogo

### Mga Tool

Ang mga tool ay mga function na ipapatupad ng AI model:

- Mga utility para sa pagproseso ng data
- Mga integrasyon sa external na API
- Mga kakayahang pang-computational
- Pagsasagawa ng paghahanap

## Mga Sample na Implementasyon: C# Implementasyon

Naglalaman ang opisyal na C# SDK repository ng ilang sample na implementasyon na nagpapakita ng iba't ibang aspekto ng MCP:

- **Basic MCP Client**: Simpleng halimbawa kung paano gumawa ng MCP client at tumawag ng mga tool
- **Basic MCP Server**: Minimal na implementasyon ng server na may pangunahing pagrehistro ng tool
- **Advanced MCP Server**: Kompletong server na may pagrehistro ng tool, authentication, at error handling
- **ASP.NET Integration**: Mga halimbawa ng integrasyon sa ASP.NET Core
- **Mga Pattern ng Implementasyon ng Tool**: Iba’t ibang pattern para sa pagpapatupad ng mga tool na may iba't ibang antas ng komplikasyon

Ang MCP C# SDK ay nasa preview pa at maaaring magbago ang mga API. Patuloy naming ia-update ang blog na ito habang umuunlad ang SDK.

### Mga Pangunahing Feature

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Pagtatayo ng iyong [unang MCP Server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Para sa kompletong mga sample ng C# implementasyon, bisitahin ang [opisyal na C# SDK samples repository](https://github.com/modelcontextprotocol/csharp-sdk)

## Sample na implementasyon: Java gamit ang Spring Implementasyon

Nag-aalok ang Java gamit ang Spring SDK ng matibay na mga pagpipilian sa implementasyon ng MCP na may enterprise-grade na mga feature.

### Mga Pangunahing Feature

- Integrasyon sa Spring Framework
- Malakas na type safety
- Suporta sa reactive programming
- Kompletong error handling

Para sa kompletong halimbawa ng implementasyon ng Java gamit ang Spring, tingnan ang [Java na may Spring sample](samples/java/containerapp/README.md) sa samples na direktoryo.

## Sample na Implementasyon: JavaScript Implementasyon

Nagbibigay ang JavaScript SDK ng isang magaan at flexible na paraan sa implementasyon ng MCP.

### Mga Pangunahing Feature

- Suporta para sa Node.js at browser
- API na nakabatay sa mga Promise
- Madaling integrasyon sa Express at iba pang framework
- Suporta sa WebSocket para sa streaming

Para sa kompletong halimbawa ng implementasyon sa JavaScript, tingnan ang [JavaScript sample](samples/javascript/README.md) sa samples na direktoryo.

## Sample na Implementasyon: Python Implementasyon

Nag-aalok ang Python SDK ng isang Pythonic na paraan sa implementasyon ng MCP na may napakagandang integrasyon para sa mga ML framework.

### Mga Pangunahing Feature

- Async/await na suporta gamit ang asyncio
- Integrasyon sa FastAPI``
- Simpleng pagrehistro ng tool
- Native na integrasyon sa mga popular na ML library

Para sa kompletong halimbawa ng implementasyon sa Python, tingnan ang [Python sample](samples/python/README.md) sa samples na direktoryo.

## Pamamahala ng API

Ang Azure API Management ay isang mahusay na sagot kung paano natin masisiguro ang mga MCP Server. Ang ideya ay ilagay ang isang Azure API Management instance sa harap ng iyong MCP Server at hayaan itong pamahalaan ang mga feature na malamang mong kailangan tulad ng:

- rate limiting
- pamamahala ng token
- monitoring
- load balancing
- seguridad

### Azure Sample

Narito ang isang Azure Sample na ginagawa mismo iyon, i.e [gumagawa ng MCP Server at sinisiguro ito gamit ang Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Tingnan kung paano nangyayari ang authorization flow sa larawan sa ibaba:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Sa nakaraang larawan, nangyayari ang mga sumusunod:

- Isinasagawa ang Authentication/Authorization gamit ang Microsoft Entra.
- Gumaganap ang Azure API Management bilang gateway at gumagamit ng mga polisiya upang idirekta at pamahalaan ang trapiko.
- Nilolog ang lahat ng request ng Azure Monitor para sa karagdagang pagsusuri.

#### Daloy ng Authorization

Tingnan natin ng mas detalyado ang daloy ng authorization:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP na espesipikasyon ng authorization

Alamin pa tungkol sa [MCP Authorization specification](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Mag-deploy ng Remote MCP Server sa Azure

Tingnan natin kung maide-deploy natin ang sample na nabanggit natin kanina:

1. I-clone ang repo

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Irehistro ang `Microsoft.App` resource provider.

   - Kung gumagamit ka ng Azure CLI, patakbuhin ang `az provider register --namespace Microsoft.App --wait`.
   - Kung gumagamit ka ng Azure PowerShell, patakbuhin ang `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Pagkatapos, patakbuhin ang `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` pagkatapos ng ilang sandali upang tingnan kung kumpleto na ang pagrehistro.

1. Patakbuhin ang utos na ito ng [azd](https://aka.ms/azd) para i-provision ang api management service, function app (kasama ang code), at lahat ng iba pang kinakailangang Azure resources

    ```shell
    azd up
    ```

    Ang mga utos na ito ay dapat mag-deploy ng lahat ng cloud resources sa Azure

### Pagsubok ng iyong server gamit ang MCP Inspector

1. Sa isang **bagong terminal window**, i-install at patakbuhin ang MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Makikita mo ang isang interface na katulad nito:

    ![Connect to Node inspector](../../../translated_images/tl/connect.141db0b2bd05f096.webp)

1. CTRL click upang i-load ang MCP Inspector web app mula sa URL na ipinapakita ng app (hal. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Itakda ang transport type sa `SSE`
1. Itakda ang URL sa iyong tumatakbong API Management SSE endpoint na ipinapakita pagkatapos ng `azd up` at **Connect**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Listahan ng Mga Tool**. I-click ang isang tool at **Patakbuhin ang Tool**.

Kung lahat ng mga hakbang ay gumana, konektado ka na ngayon sa MCP server at nagawang tumawag ng isang tool.

## Mga MCP server para sa Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Ang grupo ng mga repositoryo na ito ay mga quickstart template para sa paggawa at pag-deploy ng mga custom na remote MCP (Model Context Protocol) server gamit ang Azure Functions na may Python, C# .NET, o Node/TypeScript.

Nagbibigay ang mga sample ng kumpletong solusyon na nagpapahintulot sa mga developer na:

- Bumuo at patakbuhin nang lokal: Mag-develop at mag-debug ng MCP server sa lokal na makina
- Mag-deploy sa Azure: Madaling mag-deploy sa cloud gamit ang simpleng utos na azd up
- Kumonekta mula sa mga client: Kumonekta sa MCP server mula sa iba't ibang client kabilang ang VS Code's Copilot agent mode at ang MCP Inspector tool

### Mga Pangunahing Feature

- Seguridad sa disenyo: Ang MCP server ay sinisiguro gamit ang mga key at HTTPS
- Mga opsyon sa authentication: Sinusuportahan ang OAuth gamit ang built-in na auth at/o API Management
- Network isolation: Pinapayagan ang network isolation gamit ang Azure Virtual Networks (VNET)
- Serverless na arkitektura: Ginagamit ang Azure Functions para sa scalable, event-driven na pagpapatupad
- Lokal na pag-unlad: Komprehensibong suporta sa lokal na pag-unlad at pag-debug
- Simpleng deployment: Pinadaling proseso ng pag-deploy sa Azure

Kasama sa repositoryo ang lahat ng kinakailangang configuration files, source code, at mga depinisyon ng infrastructure upang mabilis ka makapagsimula gamit ang isang production-ready na implementasyon ng MCP server.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Sample na implementasyon ng MCP gamit ang Azure Functions na may Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Sample na implementasyon ng MCP gamit ang Azure Functions na may C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Sample na implementasyon ng MCP gamit ang Azure Functions na may Node/TypeScript.

## Mga Pangunahing Alam

- Nagbibigay ang MCP SDK ng mga tool na partikular sa wika para sa paggawa ng matitibay na solusyon ng MCP
- Kritikal ang proseso ng debugging at testing para sa maaasahan na mga aplikasyon ng MCP
- Pinapayagan ng mga reusable prompt template ang magkakatulad na pakikipag-ugnayan sa AI
- Maaaring i-orchestrate ng mga maayos na disenyo ng workflow ang mga kumplikadong gawain gamit ang maraming tool
- Nangangailangan ang implementasyon ng mga solusyon ng MCP ng pagsasaalang-alang sa seguridad, performance, at error handling

## Ehersisyo

Magdisenyo ng isang praktikal na workflow ng MCP na tumutugon sa isang tunay na problema sa iyong larangan:

1. Tukuyin ang 3-4 na tool na magiging kapaki-pakinabang sa paglutas ng problemang ito
2. Gumawa ng diagram ng workflow na nagpapakita kung paano nag-iinteract ang mga tool na ito
3. I-implement ang isang basic na bersyon ng isa sa mga tool gamit ang iyong paboritong wika
4. Gumawa ng prompt template na makakatulong sa modelong epektibong magamit ang iyong tool

## Karagdagang Mga Resource

---

## Ano ang Susunod

Susunod: [Mga Advanced na Paksa](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kaming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi eksaktong mga impormasyon. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pangunahing sanggunian. Para sa mga mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na maaaring maidulot ng paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->