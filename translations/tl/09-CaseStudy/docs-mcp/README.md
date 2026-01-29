# Case Study: Pagkonekta sa Microsoft Learn Docs MCP Server mula sa isang Client

Naranasan mo na bang magpalipat-lipat sa pagitan ng mga dokumentasyon, Stack Overflow, at walang katapusang mga tab sa search engine habang sinusubukang lutasin ang isang problema sa iyong code? Baka may pangalawang monitor ka para lang sa docs, o palaging nag-a-alt-tab sa pagitan ng iyong IDE at browser. Hindi ba mas maganda kung maipapasok mo ang dokumentasyon mismo sa iyong workflow—naka-integrate sa iyong mga app, IDE, o kahit sa sarili mong mga custom na tools? Sa case study na ito, tatalakayin natin kung paano gawin ito sa pamamagitan ng direktang pagkonekta sa Microsoft Learn Docs MCP server mula sa iyong sariling client application.

## Pangkalahatang-ideya

Ang modernong pag-develop ay hindi lang basta pagsusulat ng code—ito ay tungkol sa paghahanap ng tamang impormasyon sa tamang oras. Maraming dokumentasyon, pero bihira itong nandiyan kung saan mo ito pinaka-kailangan: sa loob mismo ng iyong mga tools at workflow. Sa pamamagitan ng pag-integrate ng pagkuha ng dokumentasyon direkta sa iyong mga aplikasyon, makakatipid ka ng oras, mababawasan ang paglipat-lipat ng konteksto, at mapapataas ang produktibidad. Sa bahaging ito, ipapakita namin kung paano kumonekta ang isang client sa Microsoft Learn Docs MCP server, para ma-access mo ang real-time, context-aware na dokumentasyon nang hindi umaalis sa iyong app.

Dadalhin ka namin sa proseso ng pagtatatag ng koneksyon, pagpapadala ng request, at maayos na paghawak ng streaming responses. Ang paraang ito ay hindi lang nagpapadali ng iyong workflow kundi nagbubukas din ng pinto para makabuo ng mas matatalinong developer tools.

## Mga Layunin sa Pagkatuto

Bakit natin ito ginagawa? Dahil ang pinakamahusay na karanasan ng developer ay yung nag-aalis ng sagabal. Isipin ang isang mundo kung saan ang iyong code editor, chatbot, o web app ay kayang sagutin ang iyong mga tanong sa dokumentasyon agad-agad, gamit ang pinakabagong nilalaman mula sa Microsoft Learn. Sa pagtatapos ng kabanatang ito, malalaman mo kung paano:

- Maunawaan ang mga batayan ng komunikasyon sa pagitan ng MCP server at client para sa dokumentasyon
- Mag-implementa ng console o web application na kumokonekta sa Microsoft Learn Docs MCP server
- Gumamit ng streaming HTTP clients para sa real-time na pagkuha ng dokumentasyon
- Mag-log at mag-interpret ng mga sagot mula sa dokumentasyon sa iyong aplikasyon

Makikita mo kung paano makakatulong ang mga kasanayang ito sa paggawa ng mga tools na hindi lang reactive, kundi tunay na interactive at context-aware.

## Scenario 1 - Real-Time na Pagkuha ng Dokumentasyon gamit ang MCP

Sa scenario na ito, ipapakita namin kung paano kumonekta ang isang client sa Microsoft Learn Docs MCP server, para ma-access mo ang real-time, context-aware na dokumentasyon nang hindi umaalis sa iyong app.

Isabuhay natin ito. Ang iyong gawain ay gumawa ng app na kumokonekta sa Microsoft Learn Docs MCP server, tatawagin ang `microsoft_docs_search` tool, at ilalagay ang streaming response sa console.

### Bakit ganitong paraan?
Dahil ito ang pundasyon para sa paggawa ng mas advanced na mga integrasyon—kung gusto mong magpatakbo ng chatbot, IDE extension, o web dashboard.

Makikita mo ang code at mga tagubilin para sa scenario na ito sa folder na [`solution`](./solution/README.md) sa loob ng case study na ito. Ang mga hakbang ay gagabay sa iyo sa pagsasaayos ng koneksyon:
- Gamitin ang opisyal na MCP SDK at streamable HTTP client para sa koneksyon
- Tawagin ang `microsoft_docs_search` tool gamit ang query parameter para makuha ang dokumentasyon
- Mag-implementa ng tamang pag-log at paghawak ng error
- Gumawa ng interactive console interface para payagan ang mga user na magpasok ng maraming search queries

Ipinapakita ng scenario na ito kung paano:
- Kumonekta sa Docs MCP server
- Magpadala ng query
- I-parse at i-print ang mga resulta

Ganito ang maaaring hitsura ng pagpapatakbo ng solusyon:

```
Prompt> What is Azure Key Vault?
Answer> Azure Key Vault is a cloud service for securely storing and accessing secrets. ...
```

Narito ang isang minimal na sample solution. Ang buong code at detalye ay makikita sa solution folder.

<details>
<summary>Python</summary>

```python
import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async def main():
    async with streamablehttp_client("https://learn.microsoft.com/api/mcp") as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool("microsoft_docs_search", {"query": "Azure Functions best practices"})
            print(result.content)

if __name__ == "__main__":
    asyncio.run(main())
```

- Para sa kumpletong implementasyon at pag-log, tingnan ang [`scenario1.py`](../../../../09-CaseStudy/docs-mcp/solution/python/scenario1.py).
- Para sa mga tagubilin sa pag-install at paggamit, tingnan ang [`README.md`](./solution/python/README.md) na file sa parehong folder.
</details>

## Scenario 2 - Interactive Study Plan Generator Web App gamit ang MCP

Sa scenario na ito, matututuhan mo kung paano i-integrate ang Docs MCP sa isang web development project. Layunin nito na payagan ang mga user na maghanap ng Microsoft Learn documentation direkta mula sa web interface, kaya agad na maa-access ang dokumentasyon sa loob ng iyong app o site.

Makikita mo kung paano:
- Mag-set up ng web app
- Kumonekta sa Docs MCP server
- Hawakan ang input ng user at ipakita ang mga resulta

Ganito ang maaaring hitsura ng pagpapatakbo ng solusyon:

```
User> I want to learn about AI102 - so suggest the roadmap to get it started from learn for 6 weeks

Assistant> Here’s a detailed 6-week roadmap to start your preparation for the AI-102: Designing and Implementing a Microsoft Azure AI Solution certification, using official Microsoft resources and focusing on exam skills areas:

---
## Week 1: Introduction & Fundamentals
- **Understand the Exam**: Review the [AI-102 exam skills outline](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-102/).
- **Set up Azure**: Sign up for a free Azure account if you don't have one.
- **Learning Path**: [Introduction to Azure AI services](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-ai/)
- **Focus**: Get familiar with Azure portal, AI capabilities, and necessary tools.

....more weeks of the roadmap...

Let me know if you want module-specific recommendations or need more customized weekly tasks!
```

Narito ang isang minimal na sample solution. Ang buong code at detalye ay makikita sa solution folder.

![Scenario 2 Overview](../../../../translated_images/tl/scenario2.0c92726d5cd81f68238e5ba65f839a0b300d5b74b8ca7db28bc8f900c3e7d037.png)

<details>
<summary>Python (Chainlit)</summary>

Ang Chainlit ay isang framework para sa paggawa ng conversational AI web apps. Pinapadali nito ang paggawa ng interactive chatbots at assistants na kayang tumawag ng MCP tools at magpakita ng resulta nang real time. Mainam ito para sa mabilisang prototyping at user-friendly na mga interface.

```python
import chainlit as cl
import requests

MCP_URL = "https://learn.microsoft.com/api/mcp"

@cl.on_message
def handle_message(message):
    query = {"question": message}
    response = requests.post(MCP_URL, json=query)
    if response.ok:
        result = response.json()
        cl.Message(content=result.get("answer", "No answer found.")).send()
    else:
        cl.Message(content="Error: " + response.text).send()
```

- Para sa kumpletong implementasyon, tingnan ang [`scenario2.py`](../../../../09-CaseStudy/docs-mcp/solution/python/scenario2.py).
- Para sa mga tagubilin sa setup at pagpapatakbo, tingnan ang [`README.md`](./solution/python/README.md).
</details>

## Scenario 3: In-Editor Docs gamit ang MCP Server sa VS Code

Kung gusto mong makuha ang Microsoft Learn Docs direkta sa loob ng VS Code (sa halip na magpalipat-lipat sa mga browser tab), maaari mong gamitin ang MCP server sa iyong editor. Pinapayagan ka nitong:
- Maghanap at magbasa ng docs sa VS Code nang hindi umaalis sa iyong coding environment.
- Mag-refer ng dokumentasyon at maglagay ng mga link direkta sa iyong README o course files.
- Pagsamahin ang GitHub Copilot at MCP para sa seamless, AI-powered na workflow sa dokumentasyon.

**Makikita mo kung paano:**
- Magdagdag ng valid na `.vscode/mcp.json` file sa root ng iyong workspace (tingnan ang halimbawa sa ibaba).
- Buksan ang MCP panel o gamitin ang command palette sa VS Code para maghanap at maglagay ng docs.
- Mag-refer ng dokumentasyon direkta sa iyong markdown files habang nagtatrabaho.
- Pagsamahin ang workflow na ito sa GitHub Copilot para sa mas mataas na produktibidad.

Narito ang isang halimbawa kung paano i-set up ang MCP server sa VS Code:

```json
{
  "servers": {
    "LearnDocsMCP": {
      "url": "https://learn.microsoft.com/api/mcp"
    }
  }
}
```

</details>

> Para sa detalyadong walkthrough na may mga screenshot at step-by-step na gabay, tingnan ang [`README.md`](./solution/scenario3/README.md).

![Scenario 3 Overview](../../../../translated_images/tl/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.png)

Ang paraang ito ay mainam para sa sinumang gumagawa ng mga technical courses, nagsusulat ng dokumentasyon, o nagde-develop ng code na madalas nangangailangan ng reference.

## Mga Pangunahing Aral

Ang pag-integrate ng dokumentasyon direkta sa iyong mga tools ay hindi lang kaginhawaan—ito ay isang malaking tulong sa produktibidad. Sa pagkonekta sa Microsoft Learn Docs MCP server mula sa iyong client, maaari mong:

- Alisin ang paglipat-lipat ng konteksto sa pagitan ng iyong code at dokumentasyon
- Kunin ang pinakabagong, context-aware na dokumentasyon nang real time
- Gumawa ng mas matatalino, mas interactive na developer tools

Makakatulong ang mga kasanayang ito na makagawa ka ng mga solusyon na hindi lang epektibo, kundi masaya ring gamitin.

## Karagdagang Mga Mapagkukunan

Para palalimin ang iyong kaalaman, tuklasin ang mga opisyal na mapagkukunan na ito:

- [Microsoft Learn Docs MCP Server (GitHub)](https://github.com/MicrosoftDocs/mcp)
- [Get started with Azure MCP Server (mcp-python)](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/get-started#create-the-python-app)
- [What is the Azure MCP Server?](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/)
- [Model Context Protocol (MCP) Introduction](https://modelcontextprotocol.io/introduction)
- [Add plugins from a MCP Server (Python)](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-mcp-plugins)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.