# Visual Studio Code साठी AI Toolkit विस्तारातून सर्व्हर वापरणे

जेव्हा आपण AI एजंट तयार करत असता, तेव्हा फक्त स्मार्ट प्रतिसाद तयार करणे महत्त्वाचे नसते; आपल्या एजंटला कृती घेण्याची क्षमता देणेही महत्त्वाचे असते. Model Context Protocol (MCP) यामध्ये हाच हेतू आहे. MCP एजंट्सना बाह्य उपकरणे आणि सेवा सुसंगत रीतीने वापरणे सुलभ करते. आपल्या एजंटला अशा प्रकारे एका टूलबॉक्समध्ये प्लगइन करण्यासारखे ठरते जी ते *खरंच* वापरू शकते.

समजा आपण आपल्या एजंटला कॅल्क्युलेटर MCP सर्व्हरशी जोडता. अचानक, आपला एजंट फक्त “47 गुणिले 89 काय?” असे एक प्रॉम्प्ट देऊन गणितीय क्रिया करू शकतो—कोणतीही हार्डकोड केलेली लॉजिक किंवा कस्टम API तयार करण्याची गरज नाही.

## आढावा

हा धडा Visual Studio Code मध्ये [AI Toolkit](https://aka.ms/AIToolkit) विस्तार वापरून कॅल्क्युलेटर MCP सर्व्हर एजंटशी कसा जोडायचा यावर प्रकाश टाकतो, ज्यामुळे आपला एजंट नैसर्गिक भाषेतून बेरीज, वजाबाकी, गुणाकार, आणि भागाकार यांसारख्या गणितीय क्रिया करु शकतो.

AI Toolkit हे Visual Studio Code साठी एक शक्तिशाली विस्तार आहे जे एजंट विकास सुलभ करतो. AI इंजिनियर्स सहजपणे AI अॅप्लिकेशन्स तयार आणि चाचणी करू शकतात—स्थानिकरित्या किंवा क्लाउडमध्ये. हा विस्तार आज उपलब्ध असलेल्या बहुतेक प्रमुख जनरेटिव्ह मॉडेल्सना समर्थन देतो.

*टीप*: AI Toolkit सध्या फक्त Python आणि TypeScript ला समर्थन देतो.

## शिकण्याची उद्दिष्टे

या धड्याच्या शेवटी, आपण पुढील गोष्टी करू शकाल:

- AI Toolkit वापरून MCP सर्व्हर वापरणे.
- एजंट कॉन्फिगरेशन कसे तयार करायचे जेणेकरून तो MCP सर्व्हरकडून उपकरणे शोधू आणि वापरू शकेल.
- नैसर्गिक भाषेतून MCP उपकरणे वापरणे.

## पद्धत

येथे उच्च स्तरावर आपल्याला कसे पुढे जायचे आहे:

- एजंट तयार करा आणि त्याचा सिस्टम प्रॉम्प्ट परिभाषित करा.
- कॅल्क्युलेटर साधनांसह MCP सर्व्हर तयार करा.
- एजंट बिल्डरला MCP सर्व्हरशी जोडा.
- नैसर्गिक भाषेतून एजंटच्या उपकरण कॉलची चाचणी करा.

छान, आता आपल्याला प्रवाह समजला आहे, चला MCP च्या माध्यमातून बाह्य उपकरणे वापरण्यासाठी AI एजंट कसे कॉन्फिगर करायचे ते पाहूया, ज्यामुळे त्याच्या क्षमता वाढतील!

## पूर्वअटी

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code साठी AI Toolkit](https://aka.ms/AIToolkit)

## व्यायाम: सर्व्हर वापरणे

> [!WARNING]
> macOS वापरकर्त्यांसाठी सूचना. सध्या macOS मध्ये अवलंबन स्थापित करण्यासंबंधी एक समस्या तपासण्यात येत आहे. यामुळे, macOS वापरकर्त्यांना सध्या हा ट्यूटोरियल पूर्ण करता येणार नाही. समस्या दुरुस्त होताच सूचना अद्यतनित केल्या जातील. आपल्या संयम आणि समजुतीसाठी धन्यवाद!

या व्यायामात, आपण Visual Studio Code मध्ये AI Toolkit वापरून MCP सर्व्हरमधील साधने वापरून AI एजंट तयार, चालवणार आणि सुधारित करणार आहात.

### -0- पूर्वतयारी, OpenAI GPT-4o मॉडेल My Models मध्ये जोडा

व्यायामात **GPT-4o** मॉडेलचा वापर केला आहे. एजंट तयार करण्यापूर्वी हे मॉडेल **My Models** मध्ये जोडलेले असले पाहिजे.

![Visual Studio Code च्या AI Toolkit विस्तारातील मॉडेल निवड इंटरफेसचे स्क्रीनशॉट. शीर्षक आहे "Find the right model for your AI Solution" आणि उपशीर्षक आहे AI मॉडेल्स शोधा, चाचणी करा आणि डिप्लॉय करा. "Popular Models" खाली सहा मॉडेल कार्ड्स आहेत: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), आणि DeepSeek-R1 (Ollama-hosted). प्रत्येकीमध्ये "Add" किंवा "Try in Playground" पर्याय आहेत.](../../../../translated_images/mr/aitk-model-catalog.2acd38953bb9c119.webp)

1. **Activity Bar** मधून **AI Toolkit** विस्तार उघडा.
1. **Catalog** विभागात **Models** निवडा जेणेकरून **Model Catalog** उघडेल. Models निवडल्याने नवीन एडिटर टॅबमध्ये **Model Catalog** उघडतो.
1. **Model Catalog** च्या शोध पट्टीत **OpenAI GPT-4o** टाइप करा.
1. **+ Add** वर क्लिक करा जेणेकरून मॉडेल **My Models** यादीत जाईल. नक्की करा की आपण हा मॉडेल GitHub वर होस्ट केलेला निवडलेला आहे.
1. **Activity Bar** मध्ये तपासा की **OpenAI GPT-4o** मॉडेल यादीत दिसत आहे का.

### -1- एजंट तयार करा

**Agent (Prompt) Builder** आपल्याला स्वतःचे AI-शक्तीचे एजंट तयार आणि कस्टमाइझ करण्यास अनुमती देतो. या विभागात, आपण नवीन एजंट तयार कराल आणि संभाषणासाठी मॉडेल वापराल.

![Visual Studio Code साठी AI Toolkit विस्तारातील "Calculator Agent" बिल्डर इंटरफेस स्क्रीनशॉट. डाव्या पॅनेलवर "OpenAI GPT-4o (via GitHub)" मॉडेल निवडलेले आहे. सिस्टम प्रॉम्प्ट लिहिलेले आहे "तुम्ही विद्यापीठात गणित शिकवणारा प्राध्यापक आहात," आणि युजर प्रॉम्प्टमध्ये "फूरियर समीकरण साध्या शब्दांत समजवा." अतिरिक्त पर्यायांमध्ये उपकरणे जोडणे, MCP सर्व्हर सक्षम करणे, आणि संरचित आउटपुट निवडणे याचा समावेश आहे. खाली निळा "Run" बटण आहे. उजव्या पॅनेलमध्ये "Get Started with Examples" अंतर्गत तीन नमुना एजंट्सची यादी आहे: Web Developer (MCP Server, Second-Grade Simplifier, आणि Dream Interpreter सह, प्रत्येकाचे कार्य लहान वर्णनांसह.](../../../../translated_images/mr/aitk-agent-builder.901e3a2960c3e477.webp)

1. **Activity Bar** मधून **AI Toolkit** विस्तार उघडा.
1. **Tools** विभागात **Agent (Prompt) Builder** निवडा. Agent (Prompt) Builder निवडल्यावर तो नवीन एडिटर टॅबमध्ये उघडतो.
1. **+ New Agent** बटण क्लिक करा. विस्तार **Command Palette** मधून सेटअप विजार्ड सुरु करेल.
1. **Calculator Agent** नाव टाका आणि **Enter** दाबा.
1. **Agent (Prompt) Builder** मध्ये, **Model** फील्डसाठी **OpenAI GPT-4o (via GitHub)** मॉडेल निवडा.

### -2- एजंटसाठी सिस्टम प्रॉम्प्ट तयार करा

एजंट तयार झाल्यावर, त्याची व्यक्तिमत्त्व आणि उद्दिष्ट ठरवण्याची वेळ आली आहे. या विभागात, आपण **Generate system prompt** वैशिष्ट्य वापरून एजंटच्या हेतूविषयी (उदाहरणार्थ, कॅल्क्युलेटर एजंट) वर्णन कराल आणि मॉडेलकडून सिस्टम प्रॉम्प्ट तयार करून घ्याल.

![Visual Studio Code च्या AI Toolkit मधील "Calculator Agent" इंटरफेसचा स्क्रीनशॉट ज्यामध्ये "Generate a prompt" नावाचा एक मोडॅल विंडो उघडलेला आहे. मोडॅलमध्ये प्रॉम्प्ट टेम्प्लेट तयार करण्यासाठी मूलभूत माहिती पुरवण्याची सूचना आहे. एका टेक्स्ट बॉक्समध्ये नमुना सिस्टम प्रॉम्प्ट दाखवला आहे: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." खाली "Close" आणि "Generate" बटणे आहेत. पार्श्वभूमीत, एजंट कॉन्फिगरेशनचा भाग, निवडलेला मॉडेल "OpenAI GPT-4o (via GitHub)" आणि सिस्टम व युजर प्रॉम्प्ट फील्ड दिसत आहेत.](../../../../translated_images/mr/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. **Prompts** विभागात, **Generate system prompt** बटण क्लिक करा. या बटणावर क्लिक केल्यावर प्रॉम्प्ट बिल्डर उघडेल जो AI चा वापर करून सिस्टम प्रॉम्प्ट तयार करतो.
1. **Generate a prompt** विंडोमध्ये हे टाका: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. **Generate** बटण क्लिक करा. एक सूचना खाली-उजव्या कोपर्‍यात दिसेल की सिस्टम प्रॉम्प्ट तयार केला जात आहे. प्रॉम्प्ट तयार झाल्यानंतर तो **Agent (Prompt) Builder** च्या **System prompt** फील्डमध्ये दिसेल.
1. **System prompt** तपासा आणि आवश्यक असल्यास बदल करा.

### -3- MCP सर्व्हर तयार करा

आता आपला एजंटचा सिस्टम प्रॉम्प्ट परिभाषित झाल्यामुळे—जो त्याचे वर्तन आणि प्रतिसाद मार्गदर्शित करतो—एजंटला व्यवहार्य क्षमता देण्याची वेळ आली आहे. या विभागात, आपण बेरीज, वजाबाकी, गुणाकार, व भागाकार करता येतील असे कॅल्क्युलेटर MCP सर्व्हर तयार करणार आहोत. हा सर्व्हर आपला एजंट नैसर्गिक भाषेतील प्रॉम्प्ट्सला प्रतिसाद देताना रिअल-टाइम गणितीय क्रिया करण्यास सक्षम करेल.

![Visual Studio Code साठी AI Toolkit विस्तारातील Calculator Agent इंटरफेसच्या खालच्या भागाचा स्क्रीनशॉट. यामध्ये “Tools” आणि “Structure output” या विस्तृत होणाऱ्या मेनूसह, “Choose output format” ड्रॉपडाऊन मेनू “text” निवडलेले आहे. उजवीकडे, “+ MCP Server” बटण दिसत आहे ज्याद्वारे Model Context Protocol सर्व्हर जोडा. टूल्स विभागावर एक प्रतिमा चिन्ह प्लेसहोल्डर आहे.](../../../../translated_images/mr/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit मध्ये आपले MCP सर्व्हर तयार करण्यासाठी साचा (templates) उपलब्ध आहेत. आपण कॅल्क्युलेटर MCP सर्व्हर तयार करण्यासाठी Python साचा वापरणार आहोत.

*टीप*: AI Toolkit सध्या Python आणि TypeScript ला समर्थन देतो.

1. **Agent (Prompt) Builder** च्या **Tools** विभागात, **+ MCP Server** बटण क्लिक करा. विस्तार **Command Palette** मधून सेटअप विजार्ड सुरु करेल.
1. **+ Add Server** निवडा.
1. **Create a New MCP Server** निवडा.
1. साचा म्हणून **python-weather** निवडा.
1. MCP सर्व्हर साचा जतन करण्यासाठी **Default folder** निवडा.
1. सर्व्हरचे नाव म्हणून **Calculator** टाका.
1. नवीन Visual Studio Code विंडो उघडेल. **Yes, I trust the authors** निवडा.
1. टर्मिनल वापरून (Terminal > New Terminal), व्हर्च्युअल वातावरण तयार करा: `python -m venv .venv`
1. टर्मिनलमध्ये व्हर्च्युअल वातावरण सक्रिय करा:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. टर्मिनलमध्ये अवलंबन इंस्टॉल करा: `pip install -e .[dev]`
1. **Activity Bar** मधील **Explorer** दृश्यात, **src** फोल्डर विस्तृत करा आणि **server.py** फाईल निवडा.
1. **server.py** फाईलमधील कोड खालीलप्रमाणे बदला आणि जतन करा:

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

आता आपल्याकडे एजंटसाठी उपकरणे उपलब्ध आहेत, त्यांचा वापर करण्याची वेळ आली आहे! या विभागात, आपण एजंटला प्रॉम्प्ट्स सादर करून चाचणी कराल आणि तपासाल की एजंट कॅल्क्युलेटर MCP सर्व्हरमधील योग्य उपकरणे वापरत आहे का.

![Visual Studio Code च्या AI Toolkit विस्तारातील Calculator Agent इंटरफेसचा स्क्रीनशॉट. डाव्या पॅनेलवर "Tools" अंतर्गत स्थानिक MCP सर्व्हर local-server-calculator_server जोडले गेले आहे, ज्यात चार उपकरणे आहेत: add, subtract, multiply, आणि divide. चार उपकरणे सक्रिय असल्याचे बॅज दर्शवितो. खाली "Structure output" विभाग संकुचित आहे आणि निळा "Run" बटण आहे. उजव्या पॅनेलवर "Model Response" अंतर्गत एजंटने multiply आणि subtract उपकरणांना अनुक्रमे इनपुट {"a": 3, "b": 25} आणि {"a": 75, "b": 20} दिले आहेत. अंतिम "Tool Response" 75.0 दर्शवित आहे. खाली "View Code" बटण आहे.](../../../../translated_images/mr/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

आपण आपल्या स्थानिक विकास मशीनवरील कॅल्क्युलेटर MCP सर्व्हर **Agent Builder** च्या माध्यमातून MCP क्लायंट म्हणून चालवणार आहात.

1. `F5` दाबून MCP सर्व्हर डिबगिंग सुरू करा. **Agent (Prompt) Builder** नवीन एडिटर टॅबमध्ये उघडेल. सर्व्हरची स्थिती टर्मिनलमध्ये दिसेल.
1. **Agent (Prompt) Builder** मधील **User prompt** फील्डमध्ये खालीलप्रमाणे टाका: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. एजंटच्या प्रतिसादासाठी **Run** बटण क्लिक करा.
1. एजंटचे आउटपुट तपासा. मॉडेलने ठरवले पाहिजे की आपण **$55** पेमेंट केले आहे.
1. येथे काय होणार आहे याचे विघटन:
    - एजंटने गणनेसाठी **multiply** आणि **subtract** उपकरणे निवडली.
    - **multiply** उपकरणासाठी `a` आणि `b` मूल्ये दिली जातील.
    - **subtract** उपकरणासाठी `a` आणि `b` मूल्ये दिली जातील.
    - प्रत्येक उपकरणाचा प्रतिसाद **Tool Response** मध्ये दिला जाईल.
    - अंतिम आउटपुट **Model Response** मध्ये दिला जाईल.
1. एजंटची आणखी चाचणी करण्यासाठी अतिरिक्त प्रॉम्प्ट्स सादर करा. आपण **User prompt** फील्डमधील विद्यमान प्रॉम्प्ट संपादित करू शकता.
1. चाचणी पूर्ण झाल्यावर, **terminal** मध्ये **CTRL/CMD+C** दाबून सर्व्हर थांबवा.

## असाइनमेंट

आपल्या **server.py** फाईलमध्ये एक अतिरिक्त टूल एन्ट्री जोडा (उदा.: संख्येचा वर्गमूळ परत करा). एजंटने नवीन किंवा विद्यमान उपकरणे वापरून प्रॉम्प्ट्स सादर करा. नवीन उपकरणे लोड करण्यासाठी सर्व्हर पुनःप्रारंभ करणे सुनिश्चित करा.

## उपाय

[उपाय](./solution/README.md)

## मुख्य मुद्दे

या अध्यायातील मुख्य मुद्दे पुढीलप्रमाणे आहेत:

- AI Toolkit विस्तार एक उत्कृष्ट क्लायंट आहे जो MCP सर्व्हर आणि त्यांच्या उपकरणांचा वापर करण्याची परवानगी देतो.
- आपण MCP सर्व्हरमध्ये नवीन उपकरणे जोडू शकता, ज्यामुळे एजंटच्या क्षमतामध्ये वाढ होते.
- AI Toolkit मध्ये साचे (उदा. Python MCP सर्व्हर साच्यांसह) समाविष्ट आहेत जे कस्टम उपकरणे तयार करणे सुलभ करतात.

## अतिरिक्त संसाधने

- [AI Toolkit दस्तऐवज](https://aka.ms/AIToolkit/doc)

## पुढे काय
- पुढे: [चाचणी व डिबगिंग](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->