# Kutumia seva kutoka kwa nyongeza ya AI Toolkit kwa Visual Studio Code

Unapojenga wakala wa AI, siyo tu kuhusu kuunda majibu makini; pia ni kuhusu kumpa wakala wako uwezo wa kuchukua hatua. Hapa ndipo Model Context Protocol (MCP) huingia. MCP hufanya iwe rahisi kwa wakala kufikia zana na huduma za nje kwa njia thabiti. Fikiria kama unamuunganisha wakala wako kwenye sanduku la zana ambalo anaweza *kweli* kutumia.

Sema unaunganisha wakala kwenye seva ya kalkuleta ya MCP. Ghafla, wakala wako anaweza kufanya operesheni za hesabu kwa kupokea tu agizo kama "Je, ni ngapi 47 mara 89?"—hakuna haja ya kuandika mantiki ngumu au kujenga API maalum.

## Muhtasari

Somo hili linaelezea jinsi ya kuunganisha seva ya kalkuleta ya MCP kwa wakala kwa kutumia nyongeza ya [AI Toolkit](https://aka.ms/AIToolkit) katika Visual Studio Code, kuwezesha wakala wako kufanya operesheni za hesabu kama kuongeza, kutoa, kuzidisha, na kugawa kupitia lugha ya asili.

AI Toolkit ni nyongeza yenye nguvu kwa Visual Studio Code inayorahisisha maendeleo ya wakala. Wahandisi wa AI wanaweza kwa urahisi kujenga programu za AI kwa kuendeleza na kujaribu mifano ya AI ya kizazi—ndani au wingu. Nyongeza inaunga mkono mifano mikubwa ya kizazi inayopatikana leo.

*Kumbuka*: AI Toolkit kwa sasa inaunga mkono Python na TypeScript.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kutumia seva ya MCP kupitia AI Toolkit.
- Kusanidi usanidi wa wakala kuwezesha kugundua na kutumia zana zinazotolewa na seva ya MCP.
- Kutumia zana za MCP kupitia lugha ya asili.

## Njia

Hapa ni jinsi tunavyohitaji kuishughulikia kwa ujumla:

- Tengeneza wakala na ueleze agizo la mfumo wake.
- Unda seva ya MCP yenye zana za kalkuleta.
- Unganisha Agent Builder kwa seva ya MCP.
- Jaribu kuitwa kwa zana ya wakala kupitia lugha ya asili.

Vizuri, sasa tunapoelewa mtiririko, tuchangamkie kusanidi wakala wa AI kutumia zana za nje kupitia MCP, kuongeza uwezo wake!

## Mahitaji ya Awali

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit kwa Visual Studio Code](https://aka.ms/AIToolkit)

## Zoef Mkuu: Kutumia seva

> [!WARNING]
> Kumbuka kwa watumiaji wa macOS. Hivi sasa tunachunguza tatizo linaloathiri usakinishaji wa utegemezi katika macOS. Kwa hiyo, watumiaji wa macOS hawawezi kumaliza mafunzo haya kwa sasa. Tutasasisha maelekezo mara tu suluhisho litakapopatikana. Asante kwa uvumilivu na uelewa wako!

Katika zoezi hili, utajenga, kuendesha, na kuboresha wakala wa AI kwa kutumia zana kutoka kwa seva ya MCP ndani ya Visual Studio Code kwa kutumia AI Toolkit.

### -0- Hatua ya Awali, ongeza mfano wa OpenAI GPT-4o kwenye My Models

Zoezi hili linatumia mfano wa **GPT-4o**. Mfano unapaswa kuongezwa kwenye **My Models** kabla ya kuunda wakala.

![Picha ya kiolesura cha uteuzi wa mfano kwenye nyongeza ya AI Toolkit ya Visual Studio Code. Kichwa cha habari kinasoma "Tafuta mfano sahihi kwa Suluhisho lako la AI" na maneno ndogo yanayowaonyesha watumiaji kugundua, kujaribu, na kupeleka mifano ya AI. Chini, chini ya "Popular Models," kuna kadi sita za mifano: DeepSeek-R1 (inayohudumiwa na GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Ndogo, Haraka), na DeepSeek-R1 (inayohudumiwa na Ollama). Kila kadi ina chaguzi za "Ongeza" mfano au "Jaribu katika Playground](../../../../translated_images/sw/aitk-model-catalog.2acd38953bb9c119.webp)

1. Fungua nyongeza ya **AI Toolkit** kutoka kwenye **Activity Bar**.
1. Katika sehemu ya **Catalog**, chagua **Models** kufungua **Model Catalog**. Kuchagua **Models** hufungua **Model Catalog** kwa kichupo kipya cha mhariri.
1. Katika uwanja wa utafutaji wa **Model Catalog**, andika **OpenAI GPT-4o**.
1. Bonyeza **+ Ongeza** kuongeza mfano kwenye orodha yako ya **My Models**. Hakikisha umechagua mfano unaoendeshwa na **GitHub**.
1. Katika **Activity Bar**, thibitisha kwamba mfano wa **OpenAI GPT-4o** unaonekana kwenye orodha.

### -1- Unda wakala

**Agent (Prompt) Builder** hukuwezesha kuunda na kubinafsisha wakala wako mwenye nguvu za AI. Katika sehemu hii, utaunda wakala mpya na kumuongezea mfano kuendesha mazungumzo.

![Picha ya kiolesura cha "Calculator Agent" katika nyongeza ya AI Toolkit kwa Visual Studio Code. Paneli ya kushoto inaonyesha mfano ulioteuliwa ni "OpenAI GPT-4o (kupitia GitHub)." Agizo la mfumo linasema "Wewe ni profesa katika chuo kikuu ukifundisha hesabu," na agizo la mtumiaji linasema, "Nielezee mlinganyo wa Fourier kwa maneno rahisi." Chaguzi nyingine ni pamoja na vifungo vya kuongeza zana, kuwezesha MCP Server, na kuchagua matokeo yaliyo na muundo. Kuna kitufe cha buluu cha “Run” chini kabisa. Paneli ya kulia inaonyesha waanzilishi wa mfano wa mawakala wa majaribio): Mjenzi wa wavuti (Web Developer) (akiwa na MCP Server, Mraibu wa darasa la pili, na Mfasiri wa ndoto, kila mmoja na maelezo mafupi ya kazi zao.](../../../../translated_images/sw/aitk-agent-builder.901e3a2960c3e477.webp)

1. Fungua nyongeza ya **AI Toolkit** kutoka kwenye **Activity Bar**.
1. Katika sehemu ya **Tools**, chagua **Agent (Prompt) Builder**. Kuchagua **Agent (Prompt) Builder** hufungua **Agent (Prompt) Builder** katika kichupo kipya cha mhariri.
1. Bonyeza kitufe cha **+ New Agent**. Nyongeza itafungua wizard ya usanidi kupitia **Command Palette**.
1. Andika jina **Calculator Agent** kisha bonyeza **Enter**.
1. Katika **Agent (Prompt) Builder**, kwa sehemu ya **Model**, chagua mfano wa **OpenAI GPT-4o (via GitHub)**.

### -2- Unda agizo la mfumo kwa wakala

Baada ya kuanzisha wakala, ni wakati wa kufafanua tabia na kusudi lake. Katika sehemu hii, utatumia kipengele cha **Generate system prompt** kuelezea tabia inayotarajiwa ya wakala—katika kesi hii, wakala wa kalkuleta—na kumruhusu mfano kuandika agizo la mfumo kwako.

![Picha ya kiolesura cha "Calculator Agent" katika AI Toolkit kwa Visual Studio Code yenye dirisha la modal lililoitwa "Generate a prompt." Dirisha linasema kwamba kiolezo cha agizo kinaweza kuundwa kwa kushiriki maelezo ya msingi na lina kisanduku cha maandishi chenye mfano wa agizo la mfumo: "Wewe ni msaidizi wa hesabu mwenye msaada na mzuri. Unapopewa tatizo linalohusiana na hesabu za msingi, unatuma jibu sahihi." Chini ya kisanduku kuna vifungo vya "Funga" na "Generate." Hapo nyuma, sehemu ya usanidi wa wakala inaonekana, ikijumuisha mfano ulioteuliwa "OpenAI GPT-4o (via GitHub)" na maeneo ya maagizo ya mfumo na mtumiaji.](../../../../translated_images/sw/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Kwa sehemu ya **Prompts**, bonyeza kitufe cha **Generate system prompt**. Kitufe hiki kitafungua kivinjari cha agizo kinachotumia AI kuunda agizo la mfumo kwa wakala.
1. Katika dirisha la **Generate a prompt**, andika ifuatayo: `Wewe ni msaidizi wa hesabu mwenye msaada na mzuri. Unapopewa tatizo linalohusiana na hesabu za msingi, unatuma jibu sahihi.`
1. Bonyeza kitufe cha **Generate**. Taarifa itatokea kona ya chini kulia kuthibitisha kwamba agizo la mfumo linaundwa. Mara baada ya utengenezaji wa agizo kukamilika, agizo litaonekana katika sehemu ya **System prompt** ya **Agent (Prompt) Builder**.
1. Pitia agizo la **System prompt** na ubadilishe ikiwa inahitajika.

### -3- Unda seva ya MCP

Sasa baada ya kufafanua agizo la mfumo wa wakala wako—kutia moyo tabia na majibu—ni wakati wa kumpatia wakala uwezo wa vitendo. Katika sehemu hii, utaunda seva ya MCP ya kalkuleta yenye zana za kufanya operesheni za kuongeza, kutoa, kuzidisha, na kugawa. Seva hii itamruhusu wakala kufanya hesabu za wakati halisi kwa majibu ya lugha ya asili.

!["Picha ya sehemu ya chini ya kiolesura cha Calculator Agent katika nyongeza ya AI Toolkit kwa Visual Studio Code. Inaonyesha menyu zinazoweza kupanuliwa za “Tools” na “Structure output,” pamoja na menyu ya kushuka chini iliyo na lebo “Choose output format” iliyowekwa kuwa “text.” Kushoto kuna kitufe kilichoandikwa “+ MCP Server” cha kuongeza seva ya Model Context Protocol. Picha ya ikoni ipo juu ya sehemu ya Tools.](../../../../translated_images/sw/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit imeandaliwa na violezo vinavyorahisisha kuunda seva yako mwenyewe ya MCP. Tutatumia kiambatisho cha Python kuunda seva ya MCP ya kalkuleta.

*Kumbuka*: AI Toolkit kwa sasa inaunga mkono Python na TypeScript.

1. Katika sehemu ya **Tools** ya **Agent (Prompt) Builder**, bonyeza kitufe cha **+ MCP Server**. Nyongeza itafungua wizard ya usanidi kupitia **Command Palette**.
1. Chagua **+ Add Server**.
1. Chagua **Create a New MCP Server**.
1. Chagua **python-weather** kama kiolezo.
1. Chagua **Default folder** kuhifadhi kiolezo cha seva ya MCP.
1. Andika jina lifuatalo kwa seva: **Calculator**
1. Dirisha jipya la Visual Studio Code litaonekana. Chagua **Yes, I trust the authors**.
1. Kwa kutumia terminal (**Terminal** > **New Terminal**), tengeneza mazingira ya virtual: `python -m venv .venv`
1. Kwa kutumia terminal, washawishi mazingira ya virtual:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Kwa kutumia terminal, sakinisha utegemezi: `pip install -e .[dev]`
1. Katika mtazamo wa **Explorer** wa **Activity Bar**, panua saraka ya **src** na chagua **server.py** kufungua faili mhariri.
1. Badilisha msimbo kwenye faili ya **server.py** kwa ifuatayo na uhifadhi:

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- Endesha wakala kwa seva ya kalkuleta ya MCP

Sasa wakala wako ana zana, ni wakati wa kuzitumia! Katika sehemu hii, utatuma maagizo kwa wakala kujaribu na kuthibitisha kama wakala anatumia zana inayofaa kutoka kwa seva ya MCP ya kalkuleta.

![Picha ya kiolesura cha Calculator Agent katika nyongeza ya AI Toolkit kwa Visual Studio Code. Paneli ya kushoto, chini ya "Tools," seva ya MCP iitwayo local-server-calculator_server imeongezwa, ikionyesha zana nne zinazopatikana: add, subtract, multiply, na divide. Kadi inasema zana nne zinafanya kazi. Chini kuna sehemu ya "Structure output" iliyofichwa na kitufe cha buluu cha “Run.” Paneli ya kulia, chini ya “Model Response,” wakala anaitisha zana za multiply na subtract akiwa na maingizo {"a": 3, "b": 25} na {"a": 75, "b": 20} mtawalia. Jibu la mwisho la "Tool Response" linaoneshwa kuwa 75.0. Kuna kitufe cha "View Code" chini.](../../../../translated_images/sw/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Utaendesha seva ya MCP ya kalkuleta kwenye mashine yako ya maendeleo kwa kutumia **Agent Builder** kama mteja wa MCP.

1. Bonyeza `F5` kuanza kufuatilia kosa la seva ya MCP. **Agent (Prompt) Builder** itafunguka katika kichupo kipya cha mhariri. Hali ya seva itaonekana kwenye terminal.
1. Katika uwanja wa **User prompt** wa **Agent (Prompt) Builder**, andika agizo lifuatalo: `Nimenunua vitu 3 kila kimoja kikigharimu $25, kisha nikatumia punguzo la $20. Nililipa kiasi gani?`
1. Bonyeza kitufe cha **Run** kuunda jibu la wakala.
1. Pitia mazao ya wakala. Mfano unapaswa kuhitimisha kwamba ulilipa **$55**.
1. Hapa ni muhtasari wa kinachopaswa kutokea:
    - Wakala huchagua zana za **multiply** na **subtract** kusaidia katika hesabu.
    - Thamani za `a` na `b` zinateuliwa kwa zana ya **multiply**.
    - Thamani za `a` na `b` zinateuliwa kwa zana ya **subtract**.
    - Majibu kutoka kwa kila zana yanatolewa katika **Tool Response** husika.
    - Matokeo ya mwisho kutoka kwa mfano yanatolewa katika **Model Response** ya mwisho.
1. Tuma maagizo zaidi kujaribu zaidi wakala. Unaweza kubadilisha agizo lililopo katika uwanja wa **User prompt** kwa kubofya ndani na kubadilisha agizo lililopo.
1. Ukimaliza kujaribu wakala, unaweza kuacha seva kupitia **terminal** kwa kubofya **CTRL/CMD+C** kuondoka.

## Kazi

Jaribu kuongeza zana nyingine kwenye faili yako ya **server.py** (mfano: rudisha mzizi wa mraba wa nambari). Tuma maagizo zaidi ambayo yatamlazimisha wakala kutumia zana yako mpya (au zana zilizopo). Hakikisha unasimamisha tena seva kuingiza zana mpya.

## Suluhisho

[Suluhisho](./solution/README.md)

## Muhimu Kumbukumbu

Kumbukumbu muhimu kutoka sura hii ni kama ifuatavyo:

- Nyongeza ya AI Toolkit ni mteja mzuri anayekuwezesha kutumia Seva za MCP na zana zao.
- Unaweza kuongeza zana mpya kwa seva za MCP, ukipanua uwezo wa wakala ili kukidhi mahitaji yanayobadilika.
- AI Toolkit ina violezo (mfano, violezo vya seva za Python MCP) vilivyo rahisisha kuunda zana maalum.

## Rasilimali Zaidi

- [AI Toolkit docs](https://aka.ms/AIToolkit/doc)

## Nini Kifuatacho
- Ifuatayo: [UJARIBU & UREKELEZA KOSA](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->