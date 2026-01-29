# Jenereta ya Mpango wa Kujifunza na Chainlit & Microsoft Learn Docs MCP

## Mahitaji ya Awali

- Python 3.8 au zaidi
- pip (msimamizi wa pakiti ya Python)
- Ufikiaji wa mtandao kuunganishwa na seva ya Microsoft Learn Docs MCP

## Usakinishaji

1. Clone hifadhi hii au pakua faili za mradi.
2. Sakinisha utegemezi unaohitajika:

   ```bash
   pip install -r requirements.txt
   ```

## Matumizi

### Hali ya 1: Swali Rahisi kwa Docs MCP
Mteja wa mstari wa amri unaounganishwa na seva ya Docs MCP, kutuma swali, na kuchapisha matokeo.

1. Endesha script:
   ```bash
   python scenario1.py
   ```
2. Ingiza swali lako kuhusu nyaraka kwenye kidokezo.

### Hali ya 2: Jenereta ya Mpango wa Kujifunza (Chainlit Web App)
Kiolesura cha mtandao (kinachotumia Chainlit) kinachoruhusu watumiaji kuunda mpango wa kujifunza wa kibinafsi, wiki kwa wiki, kwa mada yoyote ya kiufundi.

1. Anzisha programu ya Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Fungua URL ya ndani iliyotolewa kwenye terminal yako (mfano, http://localhost:8000) kwenye kivinjari chako.
3. Katika dirisha la mazungumzo, ingiza mada yako ya kujifunza na idadi ya wiki unazotaka kujifunza (mfano, "Cheti cha AI-900, wiki 8").
4. Programu itajibu na mpango wa kujifunza wiki kwa wiki, ikiwa ni pamoja na viungo vya nyaraka husika za Microsoft Learn.

**Vigezo vya Mazingira Vinavyohitajika:**

Ili kutumia Hali ya 2 (programu ya mtandao ya Chainlit na Azure OpenAI), lazima uweke vigezo vifuatavyo vya mazingira kwenye faili `.env` ndani ya saraka ya `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Jaza maelezo haya na maelezo ya rasilimali yako ya Azure OpenAI kabla ya kuendesha programu.

> [!TIP]
> Unaweza kupeleka kwa urahisi mifano yako mwenyewe ukitumia [Azure AI Foundry](https://ai.azure.com/).

### Hali ya 3: Nyaraka Ndani ya Mhariri na Seva ya MCP katika VS Code

Badala ya kubadilisha tabo za kivinjari kutafuta nyaraka, unaweza kuleta Microsoft Learn Docs moja kwa moja ndani ya VS Code ukitumia seva ya MCP. Hii inakuwezesha:
- Kutafuta na kusoma nyaraka ndani ya VS Code bila kuacha mazingira yako ya kuandika.
- Kurejelea nyaraka na kuingiza viungo moja kwa moja kwenye README au faili za kozi.
- Kutumia GitHub Copilot na MCP pamoja kwa mtiririko wa kazi wa nyaraka unaotumia AI bila usumbufu.

**Mifano ya Matumizi:**
- Kuongeza viungo vya rejea haraka kwenye README wakati wa kuandika nyaraka za kozi au mradi.
- Kutumia Copilot kuunda msimbo na MCP kupata na kunukuu nyaraka husika papo hapo.
- Kubaki umakini katika mhariri wako na kuongeza tija.

> [!IMPORTANT]
> Hakikisha una [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) halali katika mazingira yako ya kazi (eneo ni `.vscode/mcp.json`).

## Kwa Nini Chainlit kwa Hali ya 2?

Chainlit ni mfumo wa kisasa wa chanzo huria kwa ajili ya kujenga programu za mazungumzo za mtandao. Inafanya iwe rahisi kuunda kiolesura cha mtumiaji cha mazungumzo kinachounganishwa na huduma za nyuma kama seva ya Microsoft Learn Docs MCP. Mradi huu unatumia Chainlit kutoa njia rahisi, ya maingiliano ya kuunda mipango ya kujifunza ya kibinafsi papo hapo. Kwa kutumia Chainlit, unaweza haraka kujenga na kupeleka zana za mazungumzo zinazoongeza tija na kujifunza.

## Kile Hii Inafanya

Programu hii inaruhusu watumiaji kuunda mpango wa kujifunza wa kibinafsi kwa kuingiza tu mada na muda. Programu inachambua maingizo yako, inatafuta seva ya Microsoft Learn Docs MCP kwa maudhui husika, na kupanga matokeo katika mpango uliopangwa, wiki kwa wiki. Mapendekezo ya kila wiki yanaonyeshwa kwenye mazungumzo, na kufanya iwe rahisi kufuata na kufuatilia maendeleo yako. Muunganisho unahakikisha unapata rasilimali za kujifunza za hivi karibuni na zinazofaa.

## Maswali ya Mfano

Jaribu maswali haya kwenye dirisha la mazungumzo ili kuona jinsi programu inavyojibu:

- `Cheti cha AI-900, wiki 8`
- `Jifunze Azure Functions, wiki 4`
- `Azure DevOps, wiki 6`
- `Uhandisi wa data kwenye Azure, wiki 10`
- `Misingi ya usalama wa Microsoft, wiki 5`
- `Power Platform, wiki 7`
- `Huduma za AI za Azure, wiki 12`
- `Usanifu wa wingu, wiki 9`

Mifano hii inaonyesha kubadilika kwa programu kwa malengo tofauti ya kujifunza na muda.

## Marejeleo

- [Nyaraka za Chainlit](https://docs.chainlit.io/)
- [Nyaraka za MCP](https://github.com/MicrosoftDocs/mcp)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.