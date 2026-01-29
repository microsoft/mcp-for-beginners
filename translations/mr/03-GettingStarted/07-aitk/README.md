# Visual Studio Code साठी AI Toolkit विस्तारातून सर्व्हर वापरणे

AI एजंट तयार करताना, फक्त हुशार प्रतिसाद निर्माण करणे महत्त्वाचे नसते; तर तुमच्या एजंटला कृती करण्याची क्षमता देणेही महत्त्वाचे असते. यासाठी Model Context Protocol (MCP) उपयोगी ठरतो. MCP एजंटसाठी बाह्य साधने आणि सेवा सुसंगत पद्धतीने वापरणे सोपे करते. हे तुमच्या एजंटला अशा टूलबॉक्समध्ये जोडण्यासारखे आहे ज्याचा तो *खरोखर* उपयोग करू शकतो.

उदाहरणार्थ, तुम्ही तुमच्या एजंटला कॅल्क्युलेटर MCP सर्व्हरशी जोडता. अचानक, तुमचा एजंट "47 गुणिले 89 किती?" अशा प्रॉम्प्टद्वारे गणितीय क्रिया करू शकतो—लॉजिक हार्डकोड करण्याची किंवा कस्टम API तयार करण्याची गरज नाही.

## आढावा

या धड्यात तुम्ही Visual Studio Code मधील [AI Toolkit](https://aka.ms/AIToolkit) विस्ताराचा वापर करून कॅल्क्युलेटर MCP सर्व्हर एजंटशी कसा जोडायचा हे शिकाल, ज्यामुळे तुमचा एजंट नैसर्गिक भाषेद्वारे बेरीज, वजाबाकी, गुणाकार आणि भागाकार यासारख्या गणितीय क्रिया करू शकेल.

AI Toolkit हे Visual Studio Code साठी एक शक्तिशाली विस्तार आहे जे एजंट विकास सुलभ करते. AI अभियंते स्थानिक किंवा क्लाउडमध्ये जनरेटिव्ह AI मॉडेल विकसित करून आणि चाचणी करून सहजपणे AI अनुप्रयोग तयार करू शकतात. हा विस्तार आज उपलब्ध असलेल्या प्रमुख जनरेटिव्ह मॉडेल्सना समर्थन देतो.

*टीप*: AI Toolkit सध्या Python आणि TypeScript ला समर्थन देते.

## शिकण्याची उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही खालील गोष्टी करू शकाल:

- AI Toolkit च्या माध्यमातून MCP सर्व्हर वापरणे.
- MCP सर्व्हरद्वारे प्रदान केलेल्या साधनांचा शोध घेण्यासाठी आणि वापरण्यासाठी एजंट कॉन्फिगरेशन सेट करणे.
- MCP साधनांचा नैसर्गिक भाषेद्वारे उपयोग करणे.

## दृष्टिकोन

आम्हाला उच्च स्तरावर खालीलप्रमाणे दृष्टिकोन ठेवायचा आहे:

- एजंट तयार करा आणि त्याचा सिस्टम प्रॉम्प्ट परिभाषित करा.
- कॅल्क्युलेटर साधनांसह MCP सर्व्हर तयार करा.
- Agent Builder MCP सर्व्हरशी जोडा.
- नैसर्गिक भाषेद्वारे एजंटच्या टूल वापराची चाचणी करा.

छान, आता प्रवाह समजला आहे, चला MCP च्या माध्यमातून बाह्य साधनांचा उपयोग करण्यासाठी AI एजंट कॉन्फिगर करूया, ज्यामुळे त्याच्या क्षमतांमध्ये वाढ होईल!

## पूर्वतयारी

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code साठी AI Toolkit](https://aka.ms/AIToolkit)

## सराव: सर्व्हर वापरणे

> [!WARNING]
> macOS वापरकर्त्यांसाठी टीप. सध्या dependency installation वर परिणाम करणाऱ्या समस्येचा तपास चालू आहे. त्यामुळे macOS वापरकर्ते सध्या हा ट्युटोरियल पूर्ण करू शकणार नाहीत. आम्ही लवकरच सूचना अद्यतनित करू. तुमच्या संयम आणि समजूतदारपणाबद्दल धन्यवाद!

या सरावामध्ये, तुम्ही Visual Studio Code च्या AI Toolkit च्या आत MCP सर्व्हरमधील साधनांसह AI एजंट तयार कराल, चालवाल आणि सुधारित कराल.

### -0- पूर्वतयारी, OpenAI GPT-4o मॉडेल My Models मध्ये जोडा

या सरावामध्ये **GPT-4o** मॉडेलचा उपयोग केला जातो. एजंट तयार करण्यापूर्वी मॉडेल **My Models** मध्ये जोडले पाहिजे.

![Visual Studio Code च्या AI Toolkit विस्तारातील मॉडेल निवड इंटरफेसचा स्क्रीनशॉट. शीर्षक "Find the right model for your AI Solution" असून उपशीर्षक वापरकर्त्यांना AI मॉडेल शोधण्यासाठी, चाचणी करण्यासाठी आणि तैनात करण्यासाठी प्रोत्साहित करते. खाली, “Popular Models” अंतर्गत सहा मॉडेल कार्ड्स दिसतात: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), आणि DeepSeek-R1 (Ollama-hosted). प्रत्येक कार्डमध्ये मॉडेल “Add” करण्याचा किंवा “Try in Playground” पर्याय आहे.](../../../../translated_images/mr/aitk-model-catalog.2acd38953bb9c119aa629fe74ef34cc56e4eed35e7f5acba7cd0a59e614ab335.png)

1. **Activity Bar** मधून **AI Toolkit** विस्तार उघडा.
1. **Catalog** विभागात, **Models** निवडा जेणेकरून **Model Catalog** उघडेल. **Models** निवडल्याने **Model Catalog** नवीन एडिटर टॅबमध्ये उघडेल.
1. **Model Catalog** च्या शोध बारमध्ये **OpenAI GPT-4o** प्रविष्ट करा.
1. **+ Add** क्लिक करा जेणेकरून मॉडेल तुमच्या **My Models** यादीत जोडले जाईल. GitHub द्वारे होस्ट केलेले मॉडेल निवडले असल्याची खात्री करा.
1. **Activity Bar** मध्ये, **OpenAI GPT-4o** मॉडेल यादीत दिसत असल्याची पुष्टी करा.

### -1- एजंट तयार करा

**Agent (Prompt) Builder** तुम्हाला तुमचे स्वतःचे AI-सक्षम एजंट तयार करण्यास आणि सानुकूलित करण्यास सक्षम करते. या विभागात, तुम्ही नवीन एजंट तयार कराल आणि संभाषणासाठी मॉडेल नियुक्त कराल.

![Visual Studio Code च्या AI Toolkit विस्तारातील "Calculator Agent" बिल्डर इंटरफेसचा स्क्रीनशॉट. डाव्या पॅनेलवर, निवडलेले मॉडेल "OpenAI GPT-4o (via GitHub)" आहे. सिस्टम प्रॉम्प्ट "You are a professor in university teaching math" असे आहे, आणि युजर प्रॉम्प्ट "Explain to me the Fourier equation in simple terms" असे आहे. अतिरिक्त पर्यायांमध्ये MCP Server सक्षम करण्यासाठी टूल्स जोडण्याचे बटण, आणि संरचित आउटपुट निवडण्याचे पर्याय आहेत. तळाशी निळा “Run” बटण आहे. उजव्या पॅनेलवर, "Get Started with Examples" अंतर्गत तीन नमुना एजंट सूचीबद्ध आहेत: Web Developer (MCP Server सह), Second-Grade Simplifier, आणि Dream Interpreter, प्रत्येकाच्या कार्याचे संक्षिप्त वर्णन आहे.](../../../../translated_images/mr/aitk-agent-builder.901e3a2960c3e4774b29a23024ff5bec2d4232f57fae2a418b2aaae80f81c05f.png)

1. **Activity Bar** मधून **AI Toolkit** विस्तार उघडा.
1. **Tools** विभागात, **Agent (Prompt) Builder** निवडा. **Agent (Prompt) Builder** निवडल्याने **Agent (Prompt) Builder** नवीन एडिटर टॅबमध्ये उघडेल.
1. **+ New Agent** बटण क्लिक करा. विस्तार **Command Palette** च्या माध्यमातून सेटअप विजार्ड सुरू करेल.
1. **Calculator Agent** नाव प्रविष्ट करा आणि **Enter** दाबा.
1. **Agent (Prompt) Builder** मध्ये, **Model** फील्डसाठी **OpenAI GPT-4o (via GitHub)** मॉडेल निवडा.

### -2- एजंटसाठी सिस्टम प्रॉम्प्ट तयार करा

एजंट तयार केल्यानंतर, त्याचे व्यक्तिमत्त्व आणि उद्देश परिभाषित करण्याची वेळ आली आहे. या विभागात, तुम्ही **Generate system prompt** वैशिष्ट्याचा उपयोग करून एजंटच्या इच्छित वर्तनाचे वर्णन कराल—या प्रकरणात, कॅल्क्युलेटर एजंट—आणि मॉडेलला तुमच्यासाठी सिस्टम प्रॉम्प्ट लिहिण्यास सांगाल.

![Visual Studio Code च्या AI Toolkit मधील "Calculator Agent" इंटरफेसचा स्क्रीनशॉट ज्यामध्ये "Generate a prompt" शीर्षक असलेली एक विंडो उघडलेली आहे. विंडो स्पष्ट करते की मूलभूत तपशील सामायिक करून प्रॉम्प्ट टेम्पलेट तयार केले जाऊ शकते आणि एक टेक्स्ट बॉक्स समाविष्ट आहे ज्यामध्ये नमुना सिस्टम प्रॉम्प्ट आहे: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." टेक्स्ट बॉक्सखाली "Close" आणि "Generate" बटणे आहेत. पार्श्वभूमीत, एजंट कॉन्फिगरेशनचा काही भाग दिसतो, ज्यामध्ये निवडलेले मॉडेल "OpenAI GPT-4o (via GitHub)" आणि सिस्टम आणि युजर प्रॉम्प्टसाठी फील्ड्स आहेत.](../../../../translated_images/mr/aitk-generate-prompt.ba9e69d3d2bbe2a26444d0c78775540b14196061eee32c2054e9ee68c4f51f3a.png)

1. **Prompts** विभागासाठी, **Generate system prompt** बटण क्लिक करा. हे बटण प्रॉम्प्ट बिल्डर उघडते जो AI चा उपयोग करून एजंटसाठी सिस्टम प्रॉम्प्ट तयार करतो.
1. **Generate a prompt** विंडोमध्ये, खालील प्रविष्ट करा: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. **Generate** बटण क्लिक करा. सिस्टम प्रॉम्प्ट तयार होत असल्याची पुष्टी करणारी सूचना तळाच्या उजव्या कोपऱ्यात दिसेल. प्रॉम्प्ट तयार झाल्यानंतर, ते **Agent (Prompt) Builder** च्या **System prompt** फील्डमध्ये दिसेल.
1. **System prompt** पुनरावलोकन करा आणि आवश्यक असल्यास सुधारित करा.

### -3- MCP सर्व्हर तयार करा

तुमच्या एजंटचा सिस्टम प्रॉम्प्ट परिभाषित केल्यानंतर—त्याचे वर्तन आणि प्रतिसाद मार्गदर्शित करण्यासाठी—त्याला व्यावहारिक क्षमता देण्याची वेळ आली आहे. या विभागात, तुम्ही कॅल्क्युलेटर MCP सर्व्हर तयार कराल ज्यामध्ये बेरीज, वजाबाकी, गुणाकार आणि भागाकार गणना करण्यासाठी साधने असतील. हा सर्व्हर तुमच्या एजंटला नैसर्गिक भाषेतील प्रॉम्प्टसाठी रिअल-टाइम गणितीय क्रिया करण्यास सक्षम करेल.

!["Visual Studio Code च्या AI Toolkit विस्तारातील Calculator Agent इंटरफेसचा खालचा विभागाचा स्क्रीनशॉट. यात “Tools” आणि “Structure output” साठी विस्तारण्यायोग्य मेनू दिसतात, तसेच “Choose output format” नावाचा ड्रॉपडाउन मेनू आहे जो “text” वर सेट आहे. उजवीकडे, Model Context Protocol सर्व्हर जोडण्यासाठी “+ MCP Server” नावाचे बटण आहे. Tools विभागाच्या वर एक placeholder image icon दिसते.](../../../../translated_images/mr/aitk-add-mcp-server.9742cfddfe808353c0caf9cc0a7ed3e80e13abf4d2ebde315c81c3cb02a2a449.png)

AI Toolkit मध्ये तुमचा स्वतःचा MCP सर्व्हर तयार करण्यासाठी टेम्पलेट्स उपलब्ध आहेत. कॅल्क्युलेटर MCP सर्व्हर तयार करण्यासाठी आपण Python टेम्पलेटचा उपयोग करू.

*टीप*: AI Toolkit सध्या Python आणि TypeScript ला समर्थन देते.

1. **Agent (Prompt) Builder** च्या **Tools** विभागात, **+ MCP Server** बटण क्लिक करा. विस्तार **Command Palette** च्या माध्यमातून सेटअप विजार्ड सुरू करेल.
1. **+ Add Server** निवडा.
1. **Create a New MCP Server** निवडा.
1. टेम्पलेट म्हणून **python-weather** निवडा.
1. MCP सर्व्हर टेम्पलेट सेव्ह करण्यासाठी **Default folder** निवडा.
1. सर्व्हरसाठी खालील नाव प्रविष्ट करा: **Calculator**
1. नवीन Visual Studio Code विंडो उघडेल. **Yes, I trust the authors** निवडा.
1. **Terminal** (**Terminal** > **New Terminal**) वापरून वर्चुअल एन्व्हायर्नमेंट तयार करा: `python -m venv .venv`
1. **Terminal** वापरून वर्चुअल एन्व्हायर्नमेंट सक्रिय करा:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. **Terminal** वापरून dependencies इंस्टॉल करा: `pip install -e .[dev]`
1. **Activity Bar** च्या **Explorer** दृश्यात, **src** डिरेक्टरी विस्तार करा आणि **server.py** निवडून फाइल एडिटरमध्ये उघडा.
1. **server.py** फाइलमधील कोड खालीलप्रमाणे बदला आणि सेव्ह करा:

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

### -4- कॅल्क्युलेटर MCP सर्व्हरसह एजंट चालवा

तुमच्या एजंटकडे साधने आहेत, आता त्यांचा उपयोग करण्याची वेळ आली आहे! या विभागात, तुम्ही एजंटला प्रॉम्प्ट सबमिट करून चाचणी कराल आणि पडताळणी कराल की एजंट कॅल्क्युलेटर MCP सर्व्हरमधील योग्य साधनांचा उपयोग करतो का.

![Visual Studio Code च्या AI Toolkit विस्तारातील Calculator Agent इंटरफेसचा स्क्रीनशॉट. डाव्या पॅनेलवर, “Tools” अंतर्गत MCP सर्व्हर local-server-calculator_server जोडलेले आहे, ज्यामध्ये चार उपलब्ध साधने आहेत: add, subtract, multiply, आणि divide. एक बॅज दर्शवतो की चार साधने सक्रिय आहेत. खाली एक संक्षिप्त “Structure output” विभाग आणि निळा “Run” बटण आहे. उजव्या पॅनेलवर, “Model Response” अंतर्गत, एजंट multiply आणि subtract साधनांचा उपयोग करून इनपुट्स {"a": 3, "b": 25} आणि {"a": 75, "b": 20} अनुक्रमे वापरतो. अंतिम “Tool Response” 75.0 म्हणून दर्शवले जाते. तळाशी “View Code” बटण आहे.](../../../../translated_images/mr/aitk-agent-response-with-tools.e7c781869dc8041a25f9903ed4f7e8e0c7e13d7d94f6786a6c51b1e172f56866.png)

तुम्ही तुमच्या स्थानिक डेव्ह मशीनवर MCP सर्व्हर **Agent Builder** च्या माध्यमातून MCP क्लायंट म्हणून चालवाल.

1. MCP सर्व्हर डिबग करण्यासाठी `F5` दाबा. **Agent (Prompt) Builder** नवीन एडिटर टॅबमध्ये उघडेल. सर्व्हरची स्थिती टर्मिनलमध्ये दिसेल.
1. **Agent (Prompt) Builder** च्या **User prompt** फील्डमध्ये खालील प्रॉम्प्ट प्रविष्ट करा: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. **Run** बटण क्लिक करा जेणेकरून एजंटचा प्रतिसाद तयार होईल.
1. एजंट आउटपुट पुनरावलोकन करा. मॉडेलने निष्कर्ष काढला पाहिजे की तुम्ही **$55** दिले.
1. काय घडले पाहिजे याचा तपशीलवार ब्रेकडाउन:
    - एजंट गणनेत मदत करण्यासाठी **multiply** आणि **subtract** साधने निवडतो.
    - **multiply** साधनासाठी अनुक्रमे `a` आणि `b` मूल्ये नियुक्त केली जातात.
    - **subtract** साधनासाठी अनुक्रमे `a` आणि `b` मूल्ये नियुक्त केली जातात.
    - प्रत्येक साधनाचा प्रतिसाद संबंधित **Tool Response** मध्ये प्रदान केला जातो.
    - मॉडेलकडून अंतिम आउटपुट **Model Response** मध्ये प्रदान केले जाते.
1. एजंटची पुढील चाचणी करण्यासाठी अतिरिक्त प्रॉम्प्ट सबमिट करा. **User prompt** फील्डमध्ये विद्यमान प्रॉम्प्ट बदलण्यासाठी फील्डमध्ये क्लिक करून विद्यमान प्रॉम्प्ट बदला.
1. एजंटची चाचणी पूर्ण झाल्यानंतर, **terminal** च्या माध्यमातून सर्व्हर थांबवण्यासाठी **CTRL/CMD+C** प्रविष्ट करा.

## असाइनमेंट

तुमच्या **server.py** फाइलमध्ये अतिरिक्त टूल एंट्री जोडा (उदा: एखाद्या संख्येचा वर्गमूळ परत करा). तुमच्या नवीन टूलचा (किंवा विद्यमान साधनांचा) उपयोग करण्यासाठी एजंटला आवश्यक असलेल्या अतिरिक्त प्रॉम्प्ट सबमिट करा. नवीन साधने लोड करण्यासाठी सर्व्हर पुन्हा सुरू करा.

## सोल्यूशन

[Solution](./solution/README.md)

## मुख्य मुद्दे

या अध्यायातील मुख्य मुद्दे खालीलप्रमाणे आहेत:

- AI Toolkit विस्तार MCP Servers आणि त्यांच्या साधनांचा उपयोग करण्यासाठी एक उत्कृष्ट क्लायंट आहे.
- MCP सर्व्हर्समध्ये नवीन साधने जोडून, एजंटच्या क्षमतांमध्ये वाढ करता येते जे बदलत्या गरजा पूर्ण करू शकतात.
- AI Toolkit मध्ये टेम्पलेट्स (उदा: Python MCP सर्व्हर टेम्पलेट्स) समाविष्ट आहेत जे कस्टम साधने तयार करणे सुलभ करतात.

## अतिरिक्त संसाधने

- [AI Toolkit docs](https://aka.ms/AIToolkit/doc)

## पुढे काय
- पुढील: [Testing & Debugging](../08-testing/README.md)

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून निर्माण होणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.