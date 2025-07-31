<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6fb74f952ab79ed4b4a33fda5fa04ecb",
  "translation_date": "2025-07-31T01:19:45+00:00",
  "source_file": "03-GettingStarted/07-aitk/README.md",
  "language_code": "hi"
}
-->
# Visual Studio Code के AI Toolkit एक्सटेंशन से सर्वर का उपयोग करना

जब आप एक AI एजेंट बना रहे हैं, तो यह केवल स्मार्ट जवाब देने के बारे में नहीं है; यह आपके एजेंट को कार्रवाई करने की क्षमता देने के बारे में भी है। यहीं पर Model Context Protocol (MCP) काम आता है। MCP एजेंट्स को बाहरी टूल्स और सेवाओं तक एक समान तरीके से पहुंचने में मदद करता है। इसे ऐसे समझें जैसे आप अपने एजेंट को एक टूलबॉक्स से जोड़ रहे हैं जिसे वह *वास्तव में* उपयोग कर सकता है।

मान लीजिए आपने अपने एजेंट को एक कैलकुलेटर MCP सर्वर से जोड़ा। अचानक, आपका एजेंट गणितीय ऑपरेशन्स कर सकता है, बस एक प्रॉम्प्ट जैसे "47 को 89 से गुणा करें" प्राप्त करके—कोई हार्डकोडिंग लॉजिक या कस्टम API बनाने की आवश्यकता नहीं।

## परिचय

इस पाठ में आप सीखेंगे कि कैसे Visual Studio Code के [AI Toolkit](https://aka.ms/AIToolkit) एक्सटेंशन का उपयोग करके एक कैलकुलेटर MCP सर्वर को एजेंट से जोड़ना है, जिससे आपका एजेंट प्राकृतिक भाषा के माध्यम से जोड़, घटाव, गुणा और भाग जैसे गणितीय ऑपरेशन्स कर सके।

AI Toolkit एक शक्तिशाली एक्सटेंशन है जो Visual Studio Code में एजेंट डेवलपमेंट को आसान बनाता है। AI इंजीनियर आसानी से जनरेटिव AI मॉडल्स को लोकल या क्लाउड में विकसित और टेस्ट कर सकते हैं। यह एक्सटेंशन आज उपलब्ध अधिकांश प्रमुख जनरेटिव मॉडल्स को सपोर्ट करता है।

*नोट*: AI Toolkit वर्तमान में Python और TypeScript को सपोर्ट करता है।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप:

- AI Toolkit के माध्यम से MCP सर्वर का उपयोग कर सकेंगे।
- एजेंट कॉन्फ़िगरेशन को सेटअप कर सकेंगे ताकि वह MCP सर्वर द्वारा प्रदान किए गए टूल्स को खोज और उपयोग कर सके।
- MCP टूल्स को प्राकृतिक भाषा के माध्यम से उपयोग कर सकेंगे।

## दृष्टिकोण

हमें इसे उच्च स्तर पर इस तरह से अपनाना होगा:

- एक एजेंट बनाएं और उसका सिस्टम प्रॉम्प्ट परिभाषित करें।
- कैलकुलेटर टूल्स के साथ एक MCP सर्वर बनाएं।
- Agent Builder को MCP सर्वर से कनेक्ट करें।
- प्राकृतिक भाषा के माध्यम से एजेंट के टूल्स को टेस्ट करें।

बहुत बढ़िया, अब जब हमें प्रक्रिया समझ में आ गई है, तो चलिए MCP के माध्यम से बाहरी टूल्स का उपयोग करने के लिए एक AI एजेंट को कॉन्फ़िगर करते हैं, जिससे उसकी क्षमताओं में सुधार हो!

## आवश्यकताएँ

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code के लिए AI Toolkit](https://aka.ms/AIToolkit)

## अभ्यास: सर्वर का उपयोग करना

> [!WARNING]
> macOS उपयोगकर्ताओं के लिए नोट। हम वर्तमान में macOS पर डिपेंडेंसी इंस्टॉलेशन को प्रभावित करने वाले एक मुद्दे की जांच कर रहे हैं। परिणामस्वरूप, macOS उपयोगकर्ता इस ट्यूटोरियल को इस समय पूरा नहीं कर पाएंगे। जैसे ही कोई समाधान उपलब्ध होगा, हम निर्देशों को अपडेट करेंगे। आपके धैर्य और समझ के लिए धन्यवाद!

इस अभ्यास में, आप Visual Studio Code के AI Toolkit का उपयोग करके MCP सर्वर के टूल्स के साथ एक AI एजेंट बनाएंगे, चलाएंगे और सुधारेंगे।

### -0- प्रारंभिक चरण, OpenAI GPT-4o मॉडल को My Models में जोड़ें

इस अभ्यास में **GPT-4o** मॉडल का उपयोग किया गया है। एजेंट बनाने से पहले इस मॉडल को **My Models** में जोड़ना चाहिए।

![Visual Studio Code के AI Toolkit एक्सटेंशन के मॉडल चयन इंटरफ़ेस का स्क्रीनशॉट। हेडिंग "Find the right model for your AI Solution" है और सबटाइटल उपयोगकर्ताओं को AI मॉडल्स को खोजने, टेस्ट करने और डिप्लॉय करने के लिए प्रोत्साहित करता है। नीचे, “Popular Models” के तहत छह मॉडल कार्ड दिखाए गए हैं: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), और DeepSeek-R1 (Ollama-hosted)। प्रत्येक कार्ड में “Add” या “Try in Playground” विकल्प हैं।](../../../../translated_images/aitk-model-catalog.2acd38953bb9c119aa629fe74ef34cc56e4eed35e7f5acba7cd0a59e614ab335.hi.png)

1. **Activity Bar** से **AI Toolkit** एक्सटेंशन खोलें।
1. **Catalog** सेक्शन में **Models** चुनें ताकि **Model Catalog** खुल जाए। **Models** चुनने पर **Model Catalog** एक नए एडिटर टैब में खुलता है।
1. **Model Catalog** सर्च बार में **OpenAI GPT-4o** दर्ज करें।
1. **+ Add** पर क्लिक करें ताकि मॉडल को आपके **My Models** सूची में जोड़ा जा सके। सुनिश्चित करें कि आपने वह मॉडल चुना है जो **GitHub द्वारा होस्ट किया गया है**।
1. **Activity Bar** में पुष्टि करें कि **OpenAI GPT-4o** मॉडल सूची में दिखाई दे रहा है।

### -1- एक एजेंट बनाएं

**Agent (Prompt) Builder** आपको अपने AI-पावर्ड एजेंट्स को बनाने और कस्टमाइज़ करने में सक्षम बनाता है। इस सेक्शन में, आप एक नया एजेंट बनाएंगे और बातचीत को पावर देने के लिए एक मॉडल असाइन करेंगे।

![Visual Studio Code के AI Toolkit एक्सटेंशन में "Calculator Agent" बिल्डर इंटरफ़ेस का स्क्रीनशॉट। बाएं पैनल में, चयनित मॉडल "OpenAI GPT-4o (via GitHub)" है। सिस्टम प्रॉम्प्ट "You are a professor in university teaching math" है और उपयोगकर्ता प्रॉम्प्ट "Explain to me the Fourier equation in simple terms" है। अतिरिक्त विकल्पों में टूल्स जोड़ने, MCP सर्वर सक्षम करने और संरचित आउटपुट चुनने के बटन शामिल हैं। नीचे एक नीला “Run” बटन है। दाएं पैनल में, "Get Started with Examples" के तहत तीन सैंपल एजेंट्स सूचीबद्ध हैं: Web Developer (with MCP Server, Second-Grade Simplifier, और Dream Interpreter, प्रत्येक के कार्यों के संक्षिप्त विवरण के साथ।](../../../../translated_images/aitk-agent-builder.901e3a2960c3e4774b29a23024ff5bec2d4232f57fae2a418b2aaae80f81c05f.hi.png)

1. **Activity Bar** से **AI Toolkit** एक्सटेंशन खोलें।
1. **Tools** सेक्शन में **Agent (Prompt) Builder** चुनें। **Agent (Prompt) Builder** चुनने पर **Agent (Prompt) Builder** एक नए एडिटर टैब में खुलता है।
1. **+ New Agent** बटन पर क्लिक करें। एक्सटेंशन **Command Palette** के माध्यम से एक सेटअप विज़ार्ड लॉन्च करेगा।
1. **Calculator Agent** नाम दर्ज करें और **Enter** दबाएं।
1. **Agent (Prompt) Builder** में, **Model** फ़ील्ड के लिए **OpenAI GPT-4o (via GitHub)** मॉडल चुनें।

### -2- एजेंट के लिए सिस्टम प्रॉम्प्ट बनाएं

एजेंट को स्कैफोल्ड करने के बाद, अब उसके व्यक्तित्व और उद्देश्य को परिभाषित करने का समय है। इस सेक्शन में, आप **Generate system prompt** फीचर का उपयोग करके एजेंट के इरादे और व्यवहार का वर्णन करेंगे—इस मामले में, एक कैलकुलेटर एजेंट—और मॉडल को आपके लिए सिस्टम प्रॉम्प्ट लिखने देंगे।

![Visual Studio Code के AI Toolkit में "Calculator Agent" इंटरफ़ेस का स्क्रीनशॉट जिसमें "Generate a prompt" शीर्षक वाली एक मोडल विंडो खुली है। मोडल बताता है कि एक प्रॉम्प्ट टेम्पलेट को बुनियादी विवरण साझा करके जनरेट किया जा सकता है और इसमें एक टेक्स्ट बॉक्स है जिसमें सैंपल सिस्टम प्रॉम्प्ट है: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." टेक्स्ट बॉक्स के नीचे "Close" और "Generate" बटन हैं। बैकग्राउंड में, एजेंट कॉन्फ़िगरेशन का हिस्सा दिखाई दे रहा है, जिसमें चयनित मॉडल "OpenAI GPT-4o (via GitHub)" और सिस्टम और उपयोगकर्ता प्रॉम्प्ट्स के लिए फ़ील्ड शामिल हैं।](../../../../translated_images/aitk-generate-prompt.ba9e69d3d2bbe2a26444d0c78775540b14196061eee32c2054e9ee68c4f51f3a.hi.png)

1. **Prompts** सेक्शन के लिए, **Generate system prompt** बटन पर क्लिक करें। यह बटन प्रॉम्प्ट बिल्डर में खुलता है जो एजेंट के लिए सिस्टम प्रॉम्प्ट जनरेट करने के लिए AI का उपयोग करता है।
1. **Generate a prompt** विंडो में निम्नलिखित दर्ज करें: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. **Generate** बटन पर क्लिक करें। नीचे-दाएं कोने में एक नोटिफिकेशन दिखाई देगा जो पुष्टि करेगा कि सिस्टम प्रॉम्प्ट जनरेट किया जा रहा है। प्रॉम्प्ट जनरेशन पूरा होने के बाद, प्रॉम्प्ट **Agent (Prompt) Builder** के **System prompt** फ़ील्ड में दिखाई देगा।
1. **System prompt** की समीक्षा करें और यदि आवश्यक हो तो संशोधित करें।

### -3- MCP सर्वर बनाएं

अब जब आपने अपने एजेंट के सिस्टम प्रॉम्प्ट को परिभाषित कर लिया है—जो उसके व्यवहार और प्रतिक्रियाओं को निर्देशित करता है—अब उसे व्यावहारिक क्षमताओं से लैस करने का समय है। इस सेक्शन में, आप जोड़, घटाव, गुणा और भाग गणनाओं को निष्पादित करने के लिए टूल्स के साथ एक कैलकुलेटर MCP सर्वर बनाएंगे। यह सर्वर आपके एजेंट को प्राकृतिक भाषा प्रॉम्प्ट्स के जवाब में रीयल-टाइम गणितीय ऑपरेशन्स करने में सक्षम बनाएगा।

![Visual Studio Code के AI Toolkit एक्सटेंशन में Calculator Agent इंटरफ़ेस के निचले हिस्से का स्क्रीनशॉट। इसमें “Tools” और “Structure output” के लिए विस्तार योग्य मेनू दिखाए गए हैं, साथ ही “Choose output format” लेबल वाला एक ड्रॉपडाउन मेनू है जो “text” पर सेट है। दाईं ओर, एक बटन लेबल “+ MCP Server” है जो Model Context Protocol सर्वर जोड़ने के लिए है। Tools सेक्शन के ऊपर एक इमेज आइकन प्लेसहोल्डर दिखाया गया है।](../../../../translated_images/aitk-add-mcp-server.9742cfddfe808353c0caf9cc0a7ed3e80e13abf4d2ebde315c81c3cb02a2a449.hi.png)

AI Toolkit टेम्पलेट्स से लैस है जो अपना MCP सर्वर बनाने को आसान बनाता है। हम कैलकुलेटर MCP सर्वर बनाने के लिए Python टेम्पलेट का उपयोग करेंगे।

*नोट*: AI Toolkit वर्तमान में Python और TypeScript को सपोर्ट करता है।

1. **Agent (Prompt) Builder** के **Tools** सेक्शन में, **+ MCP Server** बटन पर क्लिक करें। एक्सटेंशन **Command Palette** के माध्यम से एक सेटअप विज़ार्ड लॉन्च करेगा।
1. **+ Add Server** चुनें।
1. **Create a New MCP Server** चुनें।
1. **python-weather** को टेम्पलेट के रूप में चुनें।
1. MCP सर्वर टेम्पलेट को सेव करने के लिए **Default folder** चुनें।
1. सर्वर के लिए निम्नलिखित नाम दर्ज करें: **Calculator**
1. एक नया Visual Studio Code विंडो खुलेगा। **Yes, I trust the authors** चुनें।
1. **Terminal** (**Terminal** > **New Terminal**) का उपयोग करके एक वर्चुअल एनवायरनमेंट बनाएं: `python -m venv .venv`
1. **Terminal** का उपयोग करके वर्चुअल एनवायरनमेंट को सक्रिय करें:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source venv/bin/activate`
1. **Terminal** का उपयोग करके डिपेंडेंसी इंस्टॉल करें: `pip install -e .[dev]`
1. **Activity Bar** के **Explorer** व्यू में **src** डायरेक्टरी को विस्तार करें और **server.py** को एडिटर में खोलें।
1. **server.py** फाइल में कोड को निम्नलिखित से बदलें और सेव करें:

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

### -4- कैलकुलेटर MCP सर्वर के साथ एजेंट चलाएं

अब जब आपके एजेंट के पास टूल्स हैं, तो उन्हें उपयोग करने का समय है! इस सेक्शन में, आप एजेंट को प्रॉम्प्ट सबमिट करेंगे ताकि यह टेस्ट और वैलिडेट किया जा सके कि एजेंट कैलकुलेटर MCP सर्वर से उपयुक्त टूल्स का उपयोग करता है।

![Visual Studio Code के AI Toolkit एक्सटेंशन में Calculator Agent इंटरफ़ेस का स्क्रीनशॉट। बाएं पैनल में, “Tools” के तहत एक MCP सर्वर local-server-calculator_server जोड़ा गया है, जिसमें चार उपलब्ध टूल्स दिखाए गए हैं: add, subtract, multiply, और divide। एक बैज दिखाता है कि चार टूल्स सक्रिय हैं। नीचे एक संक्षिप्त “Structure output” सेक्शन और एक नीला “Run” बटन है। दाएं पैनल में, “Model Response” के तहत, एजेंट multiply और subtract टूल्स को इनपुट्स {"a": 3, "b": 25} और {"a": 75, "b": 20} के साथ इनवोक करता है। अंतिम “Tool Response” 75.0 के रूप में दिखाया गया है। नीचे एक “View Code” बटन है।](../../../../translated_images/aitk-agent-response-with-tools.e7c781869dc8041a25f9903ed4f7e8e0c7e13d7d94f6786a6c51b1e172f56866.hi.png)

आप अपने लोकल डेव मशीन पर **Agent Builder** के माध्यम से कैलकुलेटर MCP सर्वर को MCP क्लाइंट के रूप में चलाएंगे।

1. MCP सर्वर को डिबग करने के लिए `F5` दबाएं। **Agent (Prompt) Builder** एक नए एडिटर टैब में खुलेगा। सर्वर की स्थिति टर्मिनल में दिखाई देगी।
1. **Agent (Prompt) Builder** के **User prompt** फ़ील्ड में निम्नलिखित प्रॉम्प्ट दर्ज करें: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. एजेंट का जवाब जनरेट करने के लिए **Run** बटन पर क्लिक करें।
1. एजेंट आउटपुट की समीक्षा करें। मॉडल को निष्कर्ष निकालना चाहिए कि आपने **$55** का भुगतान किया।
1. यहां क्या होना चाहिए इसका विवरण:
    - एजेंट गणना में मदद के लिए **multiply** और **subtract** टूल्स का चयन करता है।
    - **multiply** टूल के लिए संबंधित `a` और `b` मान असाइन किए जाते हैं।
    - **subtract** टूल के लिए संबंधित `a` और `b` मान असाइन किए जाते हैं।
    - प्रत्येक टूल से प्रतिक्रिया संबंधित **Tool Response** में प्रदान की जाती है।
    - मॉडल से अंतिम आउटपुट **Model Response** में प्रदान किया जाता है।
1. एजेंट को और टेस्ट करने के लिए अतिरिक्त प्रॉम्प्ट सबमिट करें। आप **User prompt** फ़ील्ड में मौजूदा प्रॉम्प्ट को क्लिक करके और बदलकर संशोधित कर सकते हैं।
1. जब आप एजेंट का टेस्टिंग समाप्त कर लें, तो **terminal** के माध्यम से सर्वर को **CTRL/CMD+C** दबाकर बंद कर सकते हैं।

## असाइनमेंट

अपने **server.py** फाइल में एक अतिरिक्त टूल एंट्री जोड़ने का प्रयास करें (जैसे: किसी संख्या का वर्गमूल लौटाएं)। ऐसे अतिरिक्त प्रॉम्प्ट सबमिट करें जो आपके नए टूल (या मौजूदा टूल्स) का उपयोग करने की आवश्यकता हो। नए टूल्स को लोड करने के लिए सर्वर को पुनः शुरू करना सुनिश्चित करें।

## समाधान

[Solution](./solution/README.md)

## मुख्य बातें

इस अध्याय से मुख्य बातें निम्नलिखित हैं:

- AI Toolkit एक्सटेंशन एक शानदार क्लाइंट है जो MCP सर्वर्स और उनके टूल्स का उपयोग करने देता है।
- आप MCP सर्वर्स में नए टूल्स जोड़ सकते हैं, एजेंट की क्षमताओं को बदलती आवश्यकताओं को पूरा करने के लिए विस्तारित कर सकते हैं।
- AI Toolkit में टेम्पलेट्स (जैसे, Python MCP सर्वर टेम्पलेट्स) शामिल हैं जो कस्टम टूल्स बनाने को सरल बनाते हैं।

## अतिरिक्त संसाधन

- [AI Toolkit डॉक्यूमेंटेशन](https://aka.ms/AIToolkit/doc)

## आगे क्या है
- अगला: [Testing & Debugging](../08-testing/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।