# ការប្រើប្រាស់ម៉ាស៊ីនមួយពីផ្នែកបន្ថែម AI Toolkit សម្រាប់ Visual Studio Code

នៅពេលដែលអ្នកកំពុងបង្កើតភ្នាក់ងារបញ្ញាសិប្បនិម្មិត (AI agent) មួយ វាមិនត្រឹមតែការបង្កើតចម្លើយឆ្លាតវៃទេ; វាក៏ជាការផ្តល់សមត្ថភាពឲ្យភ្នាក់ងាររបស់អ្នកអាចធ្វើសកម្មភាពបានផងដែរ។ នេះជាកន្លែងដែល Model Context Protocol (MCP) មកលេង។ MCP ធ្វើឲ្យមានភាពងាយស្រួលសម្រាប់ភ្នាក់ងារដើម្បីចូលដំណើរការឧបករណ៍និងសេវាកម្មខាងក្រៅដោយមានរបៀបស្របគ្នា។ គិតថាវាត្រូវបានភ្ជាប់ភ្នាក់ងាររបស់អ្នកទៅក្នុងប្រអប់ឧបករណ៍ដែលវា *ពិតប្រាកដ* អាចប្រើបាន។

ឧទាហរណ៍ អ្នកភ្ជាប់ភ្នាក់ងារមួយទៅម៉ាស៊ីន MCP គណនាប្រាក់របស់អ្នក។ យ៉ាងឆាប់រហ័ស ភ្នាក់ងាររបស់អ្នកអាចបំពេញប្រតិបត្តិការគណិតវិទ្យាត្រឹមតែទទួលបានសេចក្តីថ្លែងថា "តើ ៤៧ គុណ ៨៩ បានប៉ុន្មាន?" — មិនចាំបាច់កូដភាសាដែលជាផ្លូវការ ឬកសាង API ផ្ទាល់ខ្លួនឡើយ។

## ទិដ្ឋភាពទូទៅ

មេរៀននេះដាក់បង្ហាញពីរបៀបភ្ជាប់ម៉ាស៊ីន MCP គណនាប្រាក់ទៅភ្នាក់ងារជាមួយនឹងផ្នែកបន្ថែម [AI Toolkit](https://aka.ms/AIToolkit) នៅក្នុង Visual Studio Code ដែលអនុញ្ញាតឲ្យភ្នាក់ងាររបស់អ្នកធ្វើប្រតិបត្តិការគណិតវិទ្យាដូចជា បូក កាត់ គុណ និង ចែក តាមរយៈភាសាធម្មជាតិ។

AI Toolkit គឺជាឧបករណ៍បន្ថែមមួយដែលមានសមត្ថភាពខ្ពស់សម្រាប់ Visual Studio Code ដែលជួយឲ្យការអភិវឌ្ឍភ្នាក់ងារអាយអាយ (AI) មានភាពរលូន។ វាសាមញ្ញសម្រាប់វិស្វករអាយអាយក្នុងការបង្កើតកម្មវិធី AI ដោយអភិវឌ្ឍនិងសាកល្បងម៉ូដែល AI ផ្សិតបង្កើត—ទាំងនៅលើម៉ាស៊ីនផ្ទាល់ និងក្នុងពពក។ ផ្នែកបន្ថែមនេះគាំទ្រម៉ូដែល AI ផ្សិតបច្ចុប្បន្នភាគច្រើន។

*សម្គាល់*: AI Toolkit បច្ចុប្បន្នគាំទ្រភាសា Python និង TypeScript។

## គោលបំណងនៃការសិក្សា

នៅចុងមេរៀននេះ អ្នកនឹងអាចធ្វើការបានៈ

- ប្រើម៉ាស៊ីន MCP ដោយប្រើ AI Toolkit។
- កំណត់រចនាសម្ព័ន្ធភ្នាក់ងារដើម្បីឲ្យវាអាចស្វែងរកនិងប្រើប្រាស់ឧបករណ៍ដែលមានពីម៉ាស៊ីន MCP។
- ប្រើប្រាស់ឧបករណ៍ MCP តាមរយៈភាសាធម្មជាតិ។

## វិធីសាស្ត្រ

នេះជាវិធីដែលយើងត្រូវអនុវត្តនៅកម្រិតខ្ពស់៖

- បង្កើតភ្នាក់ងារ និងកំណត់សារបង្កើតប្រព័ន្ធរបស់វា។
- បង្កើតម៉ាស៊ីន MCP ជាមួយឧបករណ៍គណនាប្រាក់។
- ភ្ជាប់ក្រុមបង្កើតភ្នាក់ងារទៅម៉ាស៊ីន MCP។
- សាកល្បងការអំពាវនាវឧបករណ៍របស់ភ្នាក់ងារតាមភាសាធម្មជាតិ។

ល្អណាស់ ឥលូវនេះដែលយើងយល់ដឹងពីលំហូរ មកកំណត់រចនាសម្ព័ន្ធភ្នាក់ងារអាយអាយហើយប្រើប្រាស់ឧបករណ៍ខាងក្រៅតាមរយៈ MCP ដើម្បីបង្កើតសមត្ថភាពបន្ថែម!

## មុនដែលចាប់ផ្តើម

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit សម្រាប់ Visual Studio Code](https://aka.ms/AIToolkit)

## លំហាត់៖ ប្រើម៉ាស៊ីនមួយ

> [!WARNING]
> សម្គាល់សម្រាប់អ្នកប្រើ macOS។ យើងកំពុងស៊ើបអង្កេតបញ្ហានៅលើក្បាលការដំឡើងអាស្រ័យភាពនៅលើ macOS។ ដូច្នេះ អ្នកប្រើ macOS នឹងមិនអាចបញ្ចប់មេរៀននេះបាននៅពេលនេះទេ។ យើងនឹងធ្វើការអាប់ដេតការណែនាំប៉ុន្តែមានដំណោះស្រាយ។ សូមអរគុណចំពោះការអត់ធ្មត់ និងការយល់ដឹងរបស់អ្នក!

ក្នុងលំហាត់នេះ អ្នកនឹងបង្កើត ប្រតិបត្តិ និងពង្រីកភ្នាក់ងារអាយអាយមួយដែលមានឧបករណ៍ពីម៉ាស៊ីន MCP នៅក្នុង Visual Studio Code ដោយប្រើ AI Toolkit។

### -0- ជំហានមុនគេចូរពាក្យ, បន្ថែមម៉ូដែល OpenAI GPT-4o ទៅ My Models

លំហាត់នេះប្រើម៉ូដែល **GPT-4o**។ ម៉ូដែលនេះគួរត្រូវបានបន្ថែមទៅក្នុង **My Models** មុនពេលបង្កើតភ្នាក់ងារ។

![Screenshot of a model selection interface in Visual Studio Code's AI Toolkit extension. The heading reads "Find the right model for your AI Solution" with a subtitle encouraging users to discover, test, and deploy AI models. Below, under “Popular Models,” six model cards are displayed: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), and DeepSeek-R1 (Ollama-hosted). Each card includes options to “Add” the model or “Try in Playground](../../../../translated_images/km/aitk-model-catalog.2acd38953bb9c119.webp)

1. បើកផ្នែកបន្ថែម **AI Toolkit** ពី **Activity Bar**។
1. នៅផ្នែក **Catalog** ជ្រើសរៀបចំ **Models** ដើម្បីបើក **Model Catalog**។ ជ្រើស **Models** នឹងបើក **Model Catalog** នៅក្នុងតាបនិចថ្មី។
1. នៅស្ពតបារស្វែងរក **Model Catalog** សូមបញ្ចូល **OpenAI GPT-4o**។
1. ចុច **+ Add** ដើម្បីបន្ថែមម៉ូដែលទៅក្នុងបញ្ជី **My Models**។ សូមប្រាកដថាអ្នកបានជ្រើសម៉ូដែលដែល **ផ្ទុកនៅលើ GitHub**។
1. នៅក្នុង **Activity Bar** សូមបញ្ជាក់ថាម៉ូដែល **OpenAI GPT-4o** បានបង្ហាញក្នុងបញ្ជី។

### -1- បង្កើតភ្នាក់ងារ

**Agent (Prompt) Builder** អនុញ្ញាតឲ្យអ្នកបង្កើតនិងប្ដូរតាមបំណងភ្នាក់ងារអាយអាយផ្ទាល់ខ្លួន។ នៅក្នុងផ្នែកនេះ អ្នកនឹងបង្កើតភ្នាក់ងារថ្មីមួយ ហើយផ្ដល់ម៉ូដែលសម្រាប់បើកបរ ការពិភាក្សា។

![Screenshot of the "Calculator Agent" builder interface in the AI Toolkit extension for Visual Studio Code. On the left panel, the model selected is "OpenAI GPT-4o (via GitHub)." A system prompt reads "You are a professor in university teaching math," and the user prompt says, "Explain to me the Fourier equation in simple terms." Additional options include buttons for adding tools, enabling MCP Server, and selecting structured output. A blue “Run” button is at the bottom. On the right panel, under "Get Started with Examples," three sample agents are listed: Web Developer (with MCP Server, Second-Grade Simplifier, and Dream Interpreter, each with brief descriptions of their functions.](../../../../translated_images/km/aitk-agent-builder.901e3a2960c3e477.webp)

1. បើកផ្នែកបន្ថែម **AI Toolkit** ពី **Activity Bar**។
1. នៅផ្នែក **Tools** ជ្រើស **Agent (Prompt) Builder**។ ជ្រើស **Agent (Prompt) Builder** នឹងបើក **Agent (Prompt) Builder** នៅក្នុងតាបនិចថ្មី។
1. ចុចប៊ូតុង **+ New Agent**។ ផ្នែកបន្ថែមនឹងបង្ហាញកម្មវិធីដឹកនាំតាមរយៈ **Command Palette**។
1. បញ្ចូលឈ្មោះ **Calculator Agent** ហើយចុច **Enter**។
1. នៅក្នុង **Agent (Prompt) Builder**, សម្រាប់ប្រអប់ **Model**, ជ្រើសម៉ូដែល **OpenAI GPT-4o (via GitHub)**។

### -2- បង្កើតសារប្រព័ន្ធសម្រាប់ភ្នាក់ងារ

បន្ទាប់ពីបានបង្កើតស៊ុមភ្នាក់ងារ ហើយបានកំណត់ឲ្យមានលក្ខណៈនិងគោលបំណងរបស់វា អ្នកនឹងប្រើមុខងារ **Generate system prompt** ដើម្បីពិពណ៌នាចំពោះការប្រព្រឹត្តិរបស់ភ្នាក់ងារ — ក្នុងករណីនេះគឺជាភ្នាក់ងារគណនាប្រាក់ — ហើយអោយម៉ូដែលសរសេរសារប្រព័ន្ធសម្រាប់អ្នក។

![Screenshot of the "Calculator Agent" interface in the AI Toolkit for Visual Studio Code with a modal window open titled "Generate a prompt." The modal explains that a prompt template can be generated by sharing basic details and includes a text box with the sample system prompt: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Below the text box are "Close" and "Generate" buttons. In the background, part of the agent configuration is visible, including the selected model "OpenAI GPT-4o (via GitHub)" and fields for system and user prompts.](../../../../translated_images/km/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. សម្រាប់ផ្នែក **Prompts**, ចុចប៊ូតុង **Generate system prompt**។ ប៊ូតុងនេះនឹងបើកអ្នកបង្កើត prompt ដែលប្រើ AI ដើម្បីបង្កើតសារប្រព័ន្ធសម្រាប់ភ្នាក់ងារ។
1. នៅក្នុងជញ្ជាំង **Generate a prompt**, បញ្ចូល៖ `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. ចុចប៊ូតុង **Generate**។ ជាមួយនឹងការជូនព័ត៌មាននៅខាងក្រោមខាងស្តាំបញ្ជាក់ថាសារប្រព័ន្ធកំពុងត្រូវបានបង្កើត។ បន្ទាប់ពីបង្កើតរួច សារនឹងបង្ហាញនៅក្នុងប្រអប់ **System prompt** របស់ **Agent (Prompt) Builder**។
1. ពិនិត្យមើល **System prompt** ហើយកែប្រែបើចាំបាច់។

### -3- បង្កើតម៉ាស៊ីន MCP

ឥលូវនេះដែលអ្នកបានកំណត់សារប្រព័ន្ធរបស់ភ្នាក់ងាររួចហើយ — ដែលគ្រប់គ្រងអាកប្បកិច្ចនិងចម្លើយ — វានៅកំឡុងពេលចំណែកកម្មវិធីដើម្បីអនុវត្តសមត្ថភាពជាក់លាក់។ នៅក្នុងផ្នែកនេះ អ្នកនឹងបង្កើតម៉ាស៊ីន MCP គណនាប្រាក់មួយជាមួយឧបករណ៍ដើម្បីបរិច្ឆេទបូក កាត់ គុណ និងចែក។ ម៉ាស៊ីននេះនឹងអនុញ្ញាតឲ្យភ្នាក់ងាររបស់អ្នកអាចធ្វើការគណនាប្រតិទិននៅពេលជា​ពិត បន្ទាន់តាមបញ្ហាភាសាធម្មជាតិ។

!["Screenshot of the lower section of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. It shows expandable menus for “Tools” and “Structure output,” along with a dropdown menu labeled “Choose output format” set to “text.” To the right, there is a button labeled “+ MCP Server” for adding a Model Context Protocol server. An image icon placeholder is shown above the Tools section.](../../../../translated_images/km/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit ត្រូវបានបំពាក់ដោយតំបន់ទម្រង់សម្រាប់ភាពងាយស្រួលក្នុងការបង្កើតម៉ាស៊ីន MCP របស់អ្នក។ យើងនឹងប្រើតំបន់ទម្រង់ Python សម្រាប់បង្កើតម៉ាស៊ីន MCP គណនាប្រាក់។

*សម្គាល់*: AI Toolkit បច្ចុប្បន្នគាំទ្រភាសា Python និង TypeScript។

1. នៅក្នុងផ្នែក **Tools** របស់ **Agent (Prompt) Builder**, ចុចប៊ូតុង **+ MCP Server**។ ផ្នែកបន្ថែមនឹងបង្ហាញកម្មវិធីដឹកនាំតាមរយៈ **Command Palette**។
1. ជ្រើស **+ Add Server**។
1. ជ្រើស **Create a New MCP Server**។
1. ជ្រើសតំបន់ទម្រង់ **python-weather**។
1. ជ្រើស **Default folder** ដើម្បីសន្សំតំបន់ទម្រង់ម៉ាស៊ីន MCP។
1. បញ្ចូលឈ្មោះសម្រាប់ម៉ាស៊ីន៖ **Calculator**
1. បង្អួចថ្មីនៃ Visual Studio Code នឹងបើកឡើង។ ជ្រើស **Yes, I trust the authors**។
1. ប្រើទឺរមិនល(terminal) (**Terminal** > **New Terminal**), បង្កើតបរិយាកាសវេនឆ័រ: `python -m venv .venv`
1. ប្រើទឺរមិនល ដើម្បីបើកបរិយាកាសវេនឆ័រ:
    1. វីនដូ - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. ប្រើទឺរមិនល ដើម្បីដំឡើងអាស្រ័យភាព: `pip install -e .[dev]`
1. នៅក្នុងទិដ្ឋភាព **Explorer** នៃ **Activity Bar**, ពង្រីកថត **src** ហើយជ្រើស **server.py** ដើម្បីបើកឯកសារនៅក្នុងកម្មវិធីកែសម្រួល។
1. ផ្លាស់ប្ដូរកូដក្នុងឯកសារ **server.py** ជាមួយខាងក្រោម ហើយរក្សាទុក៖

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

### -4- រត់ភ្នាក់ងារជាមួយម៉ាស៊ីន MCP គណនាប្រាក់

ឥលូវដែលភ្នាក់ងាររបស់អ្នកមានឧបករណ៍ហើយ វាពេលវេលា​ប្រើប្រាស់វា! នៅក្នុងផ្នែកនេះ អ្នកនឹងបញ្ចូនសំណើទៅភ្នាក់ងារ ដើម្បីសាកល្បងនិងផ្ទៀងផ្ទាត់ថា ភ្នាក់ងារប្រើប្រាស់ឧបករណ៍ត្រឹមត្រូវពីម៉ាស៊ីន MCP គណនាប្រាក់។

![Screenshot of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. On the left panel, under “Tools,” an MCP server named local-server-calculator_server is added, showing four available tools: add, subtract, multiply, and divide. A badge shows that four tools are active. Below is a collapsed “Structure output” section and a blue “Run” button. On the right panel, under “Model Response,” the agent invokes the multiply and subtract tools with inputs {"a": 3, "b": 25} and {"a": 75, "b": 20} respectively. The final “Tool Response” is shown as 75.0. A “View Code” button appears at the bottom.](../../../../translated_images/km/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

អ្នកនឹងរត់ម៉ាស៊ីន MCP គណនាប្រាក់នៅលើម៉ាស៊ីនអភិវឌ្ឍន៍តំបន់របស់អ្នក តាមរយៈ **Agent Builder** ដែលជាអតិថិជន MCP។

1. ចុច `F5` ដើម្បីចាប់ផ្តើមដេវរស្សិនកូដសម្រាប់ម៉ាស៊ីន MCP។ **Agent (Prompt) Builder** នឹងបើកក្នុងតាបថ្មី។ ស្ថានភាពម៉ាស៊ីនទាំងនេះអាចមើលឃើញនៅទីម៉ោងទឺរមិនល។
1. នៅក្នុងប្រអប់ **User prompt** របស់ **Agent (Prompt) Builder**, បញ្ចូលសំណួរដូចខាងក្រោម៖ `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. ចុចប៊ូតុង **Run** ដើម្បីបង្កើតចម្លើយពីភ្នាក់ងារ។
1. ពិនិត្យលទ្ធផលចេញពីភ្នាក់ងារ។ ម៉ូដែលគួរតែសន្និដ្ឋានថាអ្នកបានបង់ **$55**។
1. នេះជាការពិពណ៌នាថាត្រូវមានអ្វីកើតឡើង៖
    - ភ្នាក់ងារជ្រើសឧបករណ៍ **multiply** និង **subtract** ដើម្បីជួយគណនាប្រតិបត្តិការ។
    - តម្លៃ `a` និង `b` ត្រូវបានផ្ដល់សម្រាប់ឧបករណ៍ **multiply**។
    - តម្លៃ `a` និង `b` ត្រូវបានផ្ដល់សម្រាប់ឧបករណ៍ **subtract**។
    - ចម្លើយពីឧបករណ៍នីមួយៗត្រូវបានផ្តល់នៅក្នុង **Tool Response** ផ្ទាល់ខ្លួន។
    - លទ្ធផលចុងក្រោយពីម៉ូដែលត្រូវបានផ្តល់នៅក្នុង **Model Response** ចុងក្រោយ។
1. ផ្តល់សំណើបន្ថែមដើម្បីសាកល្បងភ្នាក់ងារបន្ថែមទៀត។ អ្នកអាចកែប្រែនៅក្នុងប្រអប់ **User prompt** ដោយចុចចូលហើយដាក់សំណើថ្មី។
1. បន្ទាប់ពីសាកល្បងរួច អ្នកអាចបញ្ឈប់ម៉ាស៊ីនដោយប្រើ **terminal** ដោយចុច **CTRL/CMD+C** ដើម្បីបញ្ឈប់។

## បេសកកម្ម

ព្យាយាមបន្ថែមឧបករណ៍ថ្មីមួយចូលក្នុងឯកសារ **server.py** របស់អ្នក (ឧទាហរណ៍៖ បង្វិលសរូបគុណរបស់ចំនួនមួយ)។ ផ្តល់សំណើបន្ថែមដើម្បីឲ្យភ្នាក់ងារប្រើឧបករណ៍ថ្មីរបស់អ្នក (ឬឧបករណ៍ដែលមានរួច)។ ចាំបាច់ផ្តើមម៉ាស៊ីនឡើងវិញដើម្បីផ្ទុកឧបករណ៍ថ្មី។

## ដំណោះស្រាយ

[Solution](./solution/README.md)

## ចំណុចសំខាន់ៗ

ចំណុចសំខាន់ៗពីជំពូកនេះមានដូចខាងក្រោម៖

- ផ្នែកបន្ថែម AI Toolkit គឺជាអតិថិជនល្អសម្រាប់ប្រើម៉ាស៊ីន MCP និងឧបករណ៍របស់វា។
- អ្នកអាចបន្ថែមឧបករណ៍ថ្មីទៅម៉ាស៊ីន MCP ដើម្បីពង្រីកសមត្ថភាពភ្នាក់ងារដើម្បីបំពេញតម្រូវការកំពុងរីកចម្រើន។
- AI Toolkit រួមបញ្ចូលតំបន់ទម្រង់ (ឧ. តំបន់ទម្រង់ម៉ាស៊ីន MCP Python) សម្រាប់ធ្វើឲ្យការបង្កើតឧបករណ៍ផ្ទាល់ខ្លួនមានភាពងាយស្រួល។

## ឯកសារបន្ថែម

- [ឯកសារ AI Toolkit](https://aka.ms/AIToolkit/doc)

## តើអ្វីទៅជាបន្ទាប់
- បន្ទាប់: [Testing & Debugging](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->