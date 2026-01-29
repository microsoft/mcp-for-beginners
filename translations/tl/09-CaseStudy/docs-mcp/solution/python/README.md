# Tagabuo ng Plano sa Pag-aaral gamit ang Chainlit at Microsoft Learn Docs MCP

## Mga Kinakailangan

- Python 3.8 o mas mataas
- pip (Python package manager)
- Internet access para kumonekta sa Microsoft Learn Docs MCP server

## Pag-install

1. I-clone ang repositoryong ito o i-download ang mga file ng proyekto.
2. I-install ang mga kinakailangang dependency:

   ```bash
   pip install -r requirements.txt
   ```

## Paggamit

### Scenario 1: Simpleng Query sa Docs MCP
Isang command-line client na kumokonekta sa Docs MCP server, nagpapadala ng query, at ipinapakita ang resulta.

1. Patakbuhin ang script:
   ```bash
   python scenario1.py
   ```
2. Ipasok ang iyong tanong tungkol sa dokumentasyon sa prompt.

### Scenario 2: Tagabuo ng Plano sa Pag-aaral (Chainlit Web App)
Isang web-based na interface (gamit ang Chainlit) na nagbibigay-daan sa mga user na lumikha ng personalized na plano sa pag-aaral kada linggo para sa anumang teknikal na paksa.

1. Simulan ang Chainlit app:
   ```bash
   chainlit run scenario2.py
   ```
2. Buksan ang lokal na URL na ibinigay sa iyong terminal (hal., http://localhost:8000) sa iyong browser.
3. Sa chat window, ipasok ang iyong paksa sa pag-aaral at ang bilang ng linggo na nais mong mag-aral (hal., "AI-900 certification, 8 weeks").
4. Ang app ay magbibigay ng plano sa pag-aaral kada linggo, kabilang ang mga link sa kaugnay na Microsoft Learn na dokumentasyon.

**Mga Kinakailangang Environment Variable:**

Upang magamit ang Scenario 2 (ang Chainlit web app na may Azure OpenAI), kailangan mong itakda ang sumusunod na mga environment variable sa isang `.env` file sa direktoryong `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Punan ang mga halagang ito gamit ang iyong detalye ng Azure OpenAI resource bago patakbuhin ang app.

> [!TIP]
> Madali mong ma-deploy ang sarili mong mga modelo gamit ang [Azure AI Foundry](https://ai.azure.com/).

### Scenario 3: In-Editor Docs gamit ang MCP Server sa VS Code

Sa halip na magpalipat-lipat ng browser tabs para maghanap ng dokumentasyon, maaari mong dalhin ang Microsoft Learn Docs direkta sa iyong VS Code gamit ang MCP server. Pinapayagan ka nitong:
- Maghanap at magbasa ng dokumentasyon sa loob ng VS Code nang hindi umaalis sa coding environment.
- Mag-refer ng dokumentasyon at magpasok ng mga link direkta sa iyong README o mga file ng kurso.
- Gamitin ang GitHub Copilot at MCP nang magkasama para sa seamless, AI-powered na workflow sa dokumentasyon.

**Mga Halimbawa ng Paggamit:**
- Mabilis na magdagdag ng mga reference link sa isang README habang nagsusulat ng kurso o dokumentasyon ng proyekto.
- Gamitin ang Copilot para bumuo ng code at MCP para agad na makahanap at mag-cite ng kaugnay na dokumentasyon.
- Manatiling nakatutok sa iyong editor at pataasin ang produktibidad.

> [!IMPORTANT]
> Siguraduhing mayroon kang wastong [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) na configuration sa iyong workspace (lokasyon ay `.vscode/mcp.json`).

## Bakit Chainlit para sa Scenario 2?

Ang Chainlit ay isang modernong open-source na framework para sa paggawa ng conversational web applications. Pinapadali nito ang paggawa ng chat-based na user interfaces na kumokonekta sa mga backend service tulad ng Microsoft Learn Docs MCP server. Ang proyektong ito ay gumagamit ng Chainlit upang magbigay ng simple at interactive na paraan para makabuo ng personalized na plano sa pag-aaral sa real time. Sa pamamagitan ng Chainlit, mabilis kang makakagawa at makakapag-deploy ng chat-based na mga tool na nagpapahusay sa produktibidad at pagkatuto.

## Ano ang Ginagawa Nito

Ang app na ito ay nagbibigay-daan sa mga user na lumikha ng personalized na plano sa pag-aaral sa pamamagitan lamang ng pagpasok ng paksa at tagal ng panahon. Ang app ay nag-a-analyze ng iyong input, nagku-query sa Microsoft Learn Docs MCP server para sa kaugnay na nilalaman, at inaayos ang mga resulta sa isang naka-istrukturang plano kada linggo. Ang mga rekomendasyon kada linggo ay ipinapakita sa chat, na ginagawang madali ang pagsunod at pagsubaybay sa iyong progreso. Ang integrasyon ay tinitiyak na palagi kang nakakakuha ng pinakabago at pinaka-kaugnay na mga learning resource.

## Mga Halimbawa ng Query

Subukan ang mga query na ito sa chat window upang makita kung paano tumutugon ang app:

- `AI-900 certification, 8 weeks`
- `Learn Azure Functions, 4 weeks`
- `Azure DevOps, 6 weeks`
- `Data engineering on Azure, 10 weeks`
- `Microsoft security fundamentals, 5 weeks`
- `Power Platform, 7 weeks`
- `Azure AI services, 12 weeks`
- `Cloud architecture, 9 weeks`

Ipinapakita ng mga halimbawang ito ang flexibility ng app para sa iba't ibang layunin sa pag-aaral at tagal ng panahon.

## Mga Sanggunian

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.