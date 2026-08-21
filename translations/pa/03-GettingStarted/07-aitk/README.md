# Visual Studio Code ਲਈ AI Toolkit ਵਾਧਾ ਤੋਂ ਇੱਕ ਸਰਵਰ ਦੀ ਵਰਤੋਂ ਕਰਨਾ

ਜਦੋਂ ਤੁਸੀਂ ਇੱਕ AI ਏਜੰਟ ਬਣਾ ਰਹੇ ਹੋ, ਤਾਂ ਸਿਰਫ ਸਮਾਰਟ ਜਵਾਬ ਬਣਾਉਣ ਦੀ ਗੱਲ ਨਹੀਂ ਹੈ; ਇਹ ਤੁਹਾਡੇ ਏਜੰਟ ਨੂੰ ਕਾਰਵਾਈ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਦੇਣ ਬਾਰੇ ਵੀ ਹੈ। ਇਹੇ ਜਗ੍ਹਾ ਹੈ ਜਿੱਥੇ Model Context Protocol (MCP) ਮਦਦ ਕਰਦਾ ਹੈ। MCP ਏਜੰਟਾਂ ਲਈ ਬਾਹਰੀ ਉਪਕਾਰਣ ਅਤੇ ਸੇਵਾਵਾਂ ਤੱਕ ਇੱਕ ਸਥਿਰ ਤਰੀਕੇ ਨਾਲ ਪਹੁੰਚ ਨੂੰ ਆਸਾਨ ਬਣਾਉਂਦਾ ਹੈ। ਇਸਨੂੰ ਐਸਾ ਸੋਚੋ ਜਿਵੇਂ ਤੁਹਾਡੇ ਏਜੰਟ ਨੂੰ ਇੱਕ ਟੂਲਬਾਕਸ ਨਾਲ ਜੋੜਨਾ ਜੋ ਉਹ *ਅਸਲੀ* ਤੌਰ 'ਤੇ ਵਰਤ ਸਕਦਾ ਹੈ।

ਮਾਨੋ ਤੁਸੀਂ ਆਪਣੇ ਏਜੰਟ ਨੂੰ ਕੈਲਕੂਲੇਟਰ MCP ਸਰਵਰ ਨਾਲ ਜੋੜਦੇ ਹੋ। ਅਚਾਨਕ, ਤੁਹਾਡਾ ਏਜੰਟ ਸਿਰਫ "47 ਗੁਣਾ 89 ਕਿੰਨਾ ਹੁੰਦਾ ਹੈ?" ਵਰਗਾ ਪ੍ਰਾਂਪਟ ਮਿਲਣ 'ਤੇ ਗਣਿਤੀਕ ਕਾਰਵਾਈਆਂ ਕਰ ਸਕਦਾ ਹੈ—ਬਿਨਾਂ ਕਿਸੇ ਲੋਜਿਕ ਨੂੰ ਸਖਤੀ ਨਾਲ ਲਿਖਣ ਜਾਂ ਕਸਟਮ API ਬਣਾਉਣ ਦੀ ਲੋੜ।

## ਓਵਰਵਿਊ

ਇਹ ਪਾਠ Visual Studio Code ਵਿੱਚ [AI Toolkit](https://aka.ms/AIToolkit) ਵਾਧਾ ਨਾਲ ਕੈਲਕੂਲੇਟਰ MCP ਸਰਵਰ ਨੂੰ ਏਜੰਟ ਨਾਲ ਜੋੜਨ ਬਾਰੇ ਸਿੱਖਾਉਂਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਤੁਹਾਡੇ ਏਜੰਟ ਨੂੰ ਪ੍ਰਭਾਸ਼ਾ ਦੁਆਰਾ ਜੋੜ ਭਾਗ, ਘਟਾਓ, ਗੁਣਾ ਅਤੇ ਭਾਗ ਕਰਨ ਵਰਗੀਆਂ ਗਣਿਤ ਕਾਰਵਾਈਆਂ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਮਿਲਦੀ ਹੈ।

AI Toolkit Visual Studio Code ਲਈ ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ ਵਾਧਾ ਹੈ ਜੋ ਏਜੰਟ ਵਿਕਾਸ ਨੂੰ ਸਰਲ ਬਣਾਉਂਦਾ ਹੈ। AI ਇੰਜੀਨੀਅਰਜ਼ ਆਸਾਨੀ ਨਾਲ ਲੋਕਲੀ ਜਾਂ ਕਲਾਉਡ ਵਿੱਚ ਜਨਰੇਟਿਵ AI ਮਾਡਲ ਬਣਾਉਣ ਅਤੇ ਟੈਸਟ ਕਰਨ ਨਾਲ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹਨ। ਇਹ ਵਾਧਾ ਅੱਜ ਹਰ ਵੱਡੇ ਜਨਰੇਟਿਵ ਮਾਡਲ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ।

*ਨੋਟ*: AI Toolkit ਇਸ ਵੇਲੇ Python ਅਤੇ TypeScript ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਲਕੜੀ

ਇਸ ਪਾਠ ਦੇ ਅਖੀਰ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- AI Toolkit ਰਾਹੀਂ MCP ਸਰਵਰ ਦੀ ਵਰਤੋਂ ਕਰਨਾ।
- ਏਜੰਟ Конфਿਗਰੇਸ਼ਨ ਸੈੱਟ ਕਰਨਾ ਜੋ MCP ਸਰਵਰ ਦੁਆਰਾ ਦਿੱਤੇ ਗਏ ਟੂਲ ਖੋਜਣ ਅਤੇ ਵਰਤਣ ਦੀ ਆਗਿਆ ਦੇਵੇ।
- ਕਾਰਮਿਕ ਭਾਸ਼ਾ ਰਾਹੀਂ MCP ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਨਾ।

## ਤਰੀਕਾ

ਇੱਥੇ ਉੱਚੀ ਸਤਰ 'ਤੇ ਅਸੀਂ ਇਸ ਦਾ ਤਰੀਕਾ ਵੇਖਦੇ ਹਾਂ:

- ਇੱਕ ਏਜੰਟ ਬਣਾਓ ਅਤੇ ਉਸਦਾ ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਨਿਰਧਾਰਿਤ ਕਰੋ।
- ਕੈਲਕੂਲੇਟਰ ਟੂਲਜ਼ ਨਾਲ MCP ਸਰਵਰ ਬਣਾਓ।
- ਏਜੰਟ ਬਿਲਡਰ ਨੂੰ MCP ਸਰਵਰ ਨਾਲ ਜੋੜੋ।
- ਕਾਰਮਿਕ ਭਾਸ਼ਾ ਰਾਹੀਂ ਏਜੰਟ ਦੀ ਟੂਲ ਇਨਵੋਕੇਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ।

ਬਹੁਤ ਵਧੀਆ, ਹੁਣ ਜਦੋਂ ਅਸੀਂ ਫਲੋ ਸਮਝ ਚੁੱਕੇ ਹਾਂ, ਆਓ ਇੱਕ AI ਏਜੰਟ ਨੂੰ MCP ਰਾਹੀਂ ਬਾਹਰੀ ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਕਨਫ਼ਿਗਰ ਕਰੀਏ, ਇਸਦੀ ਸਮਰੱਥਾ ਵਧਾਈਏ!

## ਲੋੜੀਂਦੇ ਸੰਦਰਭ

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code ਲਈ AI Toolkit](https://aka.ms/AIToolkit)

## ਐਕਸਰਸਾਈਜ਼: ਇੱਕ ਸਰਵਰ ਦੀ ਵਰਤੋਂ ਕਰਨਾ

> [!WARNING]
> macOS ਉਪਭੋਗਤਿਆਂ ਲਈ ਨੋਟ: ਅਸੀਂ ਇਸ ਸਮੇਂ macOS 'ਤੇ ਡਿਪੈਂਡੈਸੀ ਇੰਸਟਾਲੇਸ਼ਨ ਨਾਲ ਜੁੜੀ ਸਮੱਸਿਆ ਦੀ ਜਾਂਚ ਕਰ ਰਹੇ ਹਾਂ। ਇਸ ਕਰਕੇ, macOS ਉਪਭੋਗਤਾ ਇਸ ਟਿਊਟੋਰਿਯਲ ਨੂੰ ਇਸ ਵੇਲੇ ਸਮਾਪਤ ਨਹੀਂ ਕਰ ਸਕਣਗੇ। ਜਿਵੇਂ ਹੀ ਮੁਰੰਮਤ ਮਿਲਦੀ ਹੈ, ਸਾਨੂੰ ਹਦਾਇਤਾਂ ਅੱਪਡੇਟ ਕਰਾਂਗੇ। ਤੁਹਾਡੇ ਸਹਿਣਸ਼ੀਲਤਾ ਅਤੇ ਸਮਝਦਾਰੀ ਲਈ ਧੰਨਵਾਦ!

ਇਸ ਕਸਰਤ ਵਿੱਚ, ਤੁਸੀਂ Visual Studio Code ਵਿੱਚ AI Toolkit ਦੀ ਵਰਤੋਂ ਕਰਦਿਆਂ MCP ਸਰਵਰ ਤੋਂ ਟੂਲਜ਼ ਨਾਲ ਏਜੰਟ ਬਣਾਓਗੇ, ਚਲਾਉਗੇ ਅਤੇ ਉਸਦੀ ਸਮਰੱਥਾ ਵਧਾਓਗੇ।

### -0- ਪਹਿਲਾਂ ਕਦਮ: ਆਪਣੀਆਂ ਮਾਡਲਾਂ ਵਿੱਚ OpenAI GPT-4o ਮਾਡਲ ਸ਼ਾਮਲ ਕਰੋ

ਇਸ ਕਸਰਤ ਵਿੱਚ **GPT-4o** ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਗਈ ਹੈ। ਮਾਡਲ ਨੂੰ ਪਹਿਲਾਂ ਹੀ **My Models** ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ ਅਗਰ ਤੁਸੀਂ ਏਜੰਟ ਬਣਾਉਣੇ ਹੋ।

![Visual Studio Code ਦੇ AI Toolkit ਵਾਧਾ ਦਾ ਮਾਡਲ ਚੋਣ ਇੰਟਰਫੇਸ ਸਕਰੀਨਸ਼ਾਟ। ਸਿਰਲੇਖ ਵਿੱਚ लिखा ਹੈ "Find the right model for your AI Solution" ਅਤੇ ਇੱਕ ਸਬਟਾਈਟਲ ਹੈ ਜੋ ਉਪਭੋਗਤਿਆਂ ਨੂੰ AI ਮਾਡਲ ਖੋਜਣ, ਟੈਸਟ ਕਰਨ ਅਤੇ ਤੈਨਾਤ ਕਰਨ ਲਈ ਉਤਸ਼ਾਹਤ ਕਰਦਾ ਹੈ। ਹੇਠਾਂ, "Popular Models" ਹੇਠਾਂ ਛੇ ਮਾਡਲ ਕਾਰਡ ਦਿਖਾਏ ਗਏ ਹਨ: DeepSeek-R1 (GitHub ਤੋਂ ਹੋਸਟ ਕੀਤਾ), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - ਛੋਟਾ, ਤੇਜ਼), ਅਤੇ DeepSeek-R1 (Ollama ਤੋਂ ਹੋਸਟ ਕੀਤਾ)। ਹਰ ਕਾਰਡ ਵਿੱਚ "Add" ਕਰਨ ਜਾਂ "Try in Playground" ਦੇ ਵਿਕਲਪ ਹਨ।](../../../../translated_images/pa/aitk-model-catalog.2acd38953bb9c119.webp)

1. **Activity Bar** ਤੋਂ **AI Toolkit** ਵਾਧਾ ਖੋਲ੍ਹੋ।
1. **Catalog** ਸੈਕਸ਼ਨ ਵਿੱਚ, **Models** ਨੂੰ ਚੁਣੋ ਤਾਂ ਜੋ **Model Catalog** ਖੁਲ ਜਾਵੇ। **Models** ਚੁਣਨ ਨਾਲ **Model Catalog** ਨਵੀਂ ਐਡੀਟਰ ਟੈਬ ਵਿੱਚ ਖੁਲਦਾ ਹੈ।
1. **Model Catalog** ਦੇ ਖੋਜ ਬਾਰ ਵਿੱਚ **OpenAI GPT-4o** ਲਿਖੋ।
1. ਮਾਡਲ ਨੂੰ ਆਪਣੀ **My Models** ਸੂਚੀ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਨ ਲਈ **+ Add** 'ਤੇ ਕਲਿੱਕ ਕਰੋ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਉਹ ਮਾਡਲ ਚੁਣਿਆ ਹੈ ਜੋ **GitHub ਦੁਆਰਾ ਹੋਸਟ ਕੀਤਾ ਗਿਆ** ਹੈ।
1. **Activity Bar** ਵਿੱਚ ਪੱਕਾ ਕਰੋ ਕਿ **OpenAI GPT-4o** ਮਾਡਲ ਸੂਚੀ ਵਿੱਚ ਦਿਖਾਈ ਦੇ ਰਿਹਾ ਹੈ।

### -1- ਏਜੰਟ ਬਣਾਓ

**Agent (Prompt) Builder** ਤੁਹਾਨੂੰ ਆਪਣਾ ਖ਼ੁਦ ਦਾ ਏਜੰਟ ਬਣਾਉਣ ਅਤੇ ਕਸਟਮਾਈਜ਼ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਇਸ ਭਾਗ ਵਿੱਚ, ਤੁਸੀਂ ਇੱਕ ਨਵਾਂ ਏਜੰਟ ਬਣਾਵੋਗੇ ਅਤੇ ਗੱਲਬਾਤ ਲਈ ਮਾਡਲ ਨਿਯੁਕਤ ਕਰਾਂਗੇ।

![Visual Studio Code ਦੇ AI Toolkit ਵਾਧਾ ਵਿੱਚ "Calculator Agent" ਬਿਲਡਰ ਇੰਟਰਫੇਸ ਦਾ ਸਕਰੀਨਸ਼ਾਟ। ਖੱਬੇ ਪੈਨਲ 'ਤੇ ਮਾਡਲ ਚੁਣਿਆ ਗਿਆ ਹੈ "OpenAI GPT-4o (via GitHub)"। ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ "ਤੁਸੀਂ ਯੂਨੀਵਰਸਿਟੀ ਵਿੱਚ ਗਣਿਤ ਸਿਖਾਉਣ ਵਾਲੇ ਪ੍ਰੋਫੈਸਰ ਹੋ," ਅਤੇ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ "ਮੈਨੂੰ ਫੁਰਿਏਰ ਸਮੀਕਰਨ ਸਧਾਰਨ ਸ਼ਬਦਾਂ ਵਿੱਚ ਸਮਝਾਓ" ਹੈ। ਵਧੇਰੇ ਵਿਕਲਪਾਂ ਵਿੱਚ ਟੂਲਜ ਸ਼ਾਮਲ ਕਰਨ, MCP ਸਰਵਰ ਸਮਰਥਿਤ ਕਰਨ ਅਤੇ ਸਟ੍ਰਕਚਰਡ ਆਉਟਪੁੱਟ ਚੁਣਨ ਲਈ ਬਟਨ ਹਨ। ਹੇਠਾਂ ਇਕ ਨੀਲਾ “Run” ਬਟਨ ਹੈ। ਸੱਜੇ ਪੈਨਲ 'ਤੇ "Get Started with Examples" ਹੇਠਾਂ ਤਿੰਨ ਸੈਂਪਲ ਏਜੰਟ ਸੂਚੀਬੱਧ ਹਨ: Web Developer (MCP Server, Second-Grade Simplifier, ਅਤੇ Dream Interpreter ਨਾਲ, ਜਿਨ੍ਹਾਂ ਦੀਆਂ ਸੰਖੇਪ ਜਾਣਕਾਰੀਆਂ ਦਿੱਤੀਆਂ ਗਈਆਂ ਹਨ)।](../../../../translated_images/pa/aitk-agent-builder.901e3a2960c3e477.webp)

1. **Activity Bar** ਤੋਂ **AI Toolkit** ਵਾਧਾ ਖੋਲ੍ਹੋ।
1. **Tools** ਸੈਕਸ਼ਨ ਵਿੱਚ, **Agent (Prompt) Builder** ਚੁਣੋ। ਇਹ ਨਵੀਂ ਐਡੀਟਰ ਟੈਬ ਵਿੱਚ ਖੁਲ ਜਾਵੇਗਾ।
1. **+ New Agent** ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ। ਵਾਧਾ **Command Palette** ਰਾਹੀਂ ਸੈਟਅਪ ਵਿਜ਼ਾਰਡ ਖੋਲ੍ਹੇਗਾ।
1. ਨਾਮ ਦਰਜ ਕਰੋ **Calculator Agent** ਅਤੇ **Enter** ਦਬਾਓ।
1. **Agent (Prompt) Builder** ਵਿੱਚ **Model** ਖੇਤਰ ਲਈ, **OpenAI GPT-4o (via GitHub)** ਮਾਡਲ ਚੁਣੋ।

### -2- ਏਜੰਟ ਲਈ ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਬਣਾਓ

ਜਦੋਂ ਏਜੰਟ ਬਣ ਕੇ ਤਿਆਰ ਹੋਇਆ, ਇਸਦਾ ਵਿਅਕਤਿਤਵ ਅਤੇ ਮਕਸਦ ਨਿਰਧਾਰਿਤ ਕਰਨਾ ਬਕਾਇਆ ਹੈ। ਇਸ ਹਿੱਸੇ ਵਿੱਚ, ਤੁਸੀਂ **Generate system prompt** ਵਿਸ਼ੇਸ਼ਤਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਏਜੰਟ ਦੀ ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਕਾਰਵਾਈ ਦੀ ਵਰਣਨਾ ਕਰੋਗੇ—ਇਸ ਮਾਮਲੇ ਵਿੱਚ ਕੈਲਕੂਲੇਟਰ ਏਜੰਟ—ਅਤੇ ਮਾਡਲ ਤੁਹਾਡੇ ਲਈ ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਲਿਖੇਗਾ।

![Visual Studio Code ਵਿੱਚ AI Toolkit ਲਈ "Calculator Agent" ਇੰਟਰਫੇਸ ਦਾ ਸਕਰੀਨਸ਼ਾਟ ਜਿਸ ਵਿੱਚ "Generate a prompt" ਨਾਮਕ ਮੋਡਲ ਵਿਂਡੋ ਖੁਲ੍ਹੀ ਹੋਈ ਹੈ। ਮੋਡਲ ਵਿੱਚ ਸਮਝਾਇਆ ਗਿਆ ਹੈ ਕਿ ਬੁਨਿਆਦੀ ਵੇਰਵੇ ਸਾਂਝੇ ਕਰਕੇ ਪ੍ਰਾਂਪਟ ਟੈਮਪਲੇਟ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ ਅਤੇ ਇੱਕ ਟੈਕਸਟ ਬਾਕਸ ਵਿੱਚ ਨਮੂਨਾ ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਦਿੱਤਾ ਹੈ: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." ਟੈਕਸਟ ਬਾਕਸ ਹੇਠਾਂ "Close" ਅਤੇ "Generate" ਬਟਨ ਹਨ। ਪਿੱਛੋਕੜ ਵਿੱਚ ਏਜੰਟ Конфਿਗਰੇਸ਼ਨ ਦਾ ਹਿੱਸਾ ਦਿੱਸ ਰਿਹਾ ਹੈ ਜਿਥੇ ਮਾਡਲ "OpenAI GPT-4o (via GitHub)" ਚੁਣਿਆ ਗਿਆ ਹੈ ਅਤੇ ਸਿਸਟਮ ਅਤੇ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਖੇਤਰ ਹਨ।](../../../../translated_images/pa/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. **Prompts** ਭਾਗ ਲਈ, **Generate system prompt** ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ। ਇਹ ਬਟਨ ਪ੍ਰਾਂਪਟ ਬਿਲਡਰ ਖੋਲ੍ਹਦਾ ਹੈ ਜੋ ਏਜੰਟ ਲਈ ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਬਣਾਉਂਦਾ ਹੈ।
1. **Generate a prompt** ਵਿੰਡੋ ਵਿੱਚ, ਇਹ ਲਿਖੋ: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. **Generate** ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ। ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਬਣਾਉਣ ਦੀ पुषਟੀ ਦੇਣ ਵਾਲਾ ਸੂਚਨਾਸੂਚਕ ਨੂੰਹੇਠਲਾ-ਸੱਜਾ ਕੋਨਾ ਵਿੱਚ ਆਵੇਗੀ। ਜਦੋਂ ਪ੍ਰਾਂਪਟ ਬਣਾਉਣ ਮੁਕੰਮਲ ਹੋ ਜਾਵੇ, ਇਹ **Agent (Prompt) Builder** ਦੇ **System prompt** ਖੇਤਰ ਵਿੱਚ ਦਿਖਾਈ ਦੇਵੇਗਾ।
1. **System prompt** ਦੀ ਸਮੀਖਿਆ ਕਰੋ ਅਤੇ ਜੇ ਜ਼ਰੂਰੀ ਹੋਵੇ ਤਾਂ ਤਬਦੀਲ ਕਰੋ।

### -3- MCP ਸਰਵਰ ਬਣਾਓ

ਹੁਣ ਜਦੋਂ ਤੁਸੀਂ ਆਪਣੇ ਏਜੰਟ ਦਾ ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਨਿਰਧਾਰਿਤ ਕਰ ਲਿਆ ਹੈ, ਜੋ ਇਸਦੀ ਕਾਰਵਾਈ ਅਤੇ ਜਵਾਬਾਂ ਦਾ ਰਹਿਨੁਮਾ ਹੈ, ਸਮਾਂ ਆ ਗਿਆ ਹੈ ਕਿ ਏਜੰਟ ਨੂੰ ਵਿਹਾਰਕ ਸਮਰੱਥਾਵਾਂ ਨਾਲ ਯੁਕਤ ਕੀਤਾ ਜਾਵੇ। ਇਸ ਭਾਗ ਵਿੱਚ, ਤੁਸੀਂ ਜੋੜ, ਘਟਾਓ, ਗੁਣਾ ਅਤੇ ਭਾਗ ਕਰਨ ਵਾਲੇ ਕੈਲਕੂਲੇਟਰ MCP ਸਰਵਰ ਨੂੰ ਬਣਾਵੋਗੇ। ਇਹ ਸਰਵਰ ਤੁਹਾਡੇ ਏਜੰਟ ਨੂੰ ਪ੍ਰਭਾਸ਼ਾ ਪ੍ਰਾਂਪਟਾਂ 'ਤੇ ਤੁਰੰਤ ਗਣਿਤ ਕਾਰਵਾਈ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਦੇਵੇਗਾ।

![Visual Studio Code ਦੇ AI Toolkit ਵਾਧਾ ਵਿੱਚ Calculator Agent ਇੰਟਰਫੇਸ ਦੇ ਹੇਠਲੇ ਹਿੱਸੇ ਦਾ ਸਕਰੀਨਸ਼ਾਟ। ਇਸ ਵਿੱਚ "Tools" ਅਤੇ "Structure output" ਲਈ ਵੇਖਣ ਯੋਗ ਮੀਨੂੰ ਹਨ, ਨਾਲ ਹੀ "Choose output format" ਡ੍ਰਾਪਡਾਊਨ ਮੀਨੂੰ "text" ਤੇ ਸੈੱਟ ਹੈ। ਸੱਜੇ ਪਾਸੇ "+ MCP Server" ਬਟਨ ਹੈ ਜੋ Model Context Protocol ਸਰਵਰ ਜੋੜਦਾ ਹੈ। Tools ਹਿੱਸੇ ਉੱਪਰ ਚਿੱਤਰ ਆਈਕਨ ਪਲੇਸਹੋਲਡਰ ਹੈ।](../../../../translated_images/pa/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit ਆਪਣੇ MCP ਸਰਵਰ ਬਣਾਉਣ ਲਈ ਟੈਮਪਲੇਟ ਹੇਠਾਂ ਮੁਹੱਈਆ ਕਰਵਾਉਂਦਾ ਹੈ। ਅਸੀਂ ਕੈਲਕੂਲੇਟਰ MCP ਸਰਵਰ ਬਣਾਉਣ ਲਈ Python ਟੈਮਪਲੇਟ ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ।

*ਨੋਟ*: AI Toolkit ਇਸ ਵੇਲੇ Python ਅਤੇ TypeScript ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ।

1. **Agent (Prompt) Builder** ਦੇ **Tools** ਸੈਕਸ਼ਨ ਵਿੱਚ, **+ MCP Server** ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ। ਵਾਧਾ ਇੱਕ ਸੈਟਅਪ ਵਿਜ਼ਾਰਡ **Command Palette** ਰਾਹੀਂ ਚਲਾਏਗਾ।
1. **+ Add Server** ਚੁਣੋ।
1. **Create a New MCP Server** ਚੁਣੋ।
1. ਟੈਮਪਲੇਟ ਵਜੋਂ **python-weather** ਚੁਣੋ।
1. MCP ਸਰਵਰ ਟੈਮਪਲੇਟ ਸੇਵ ਕਰਨ ਲਈ **Default folder** ਚੁਣੋ।
1. ਸਰਵਰ ਲਈ ਨਾਮ ਦਿਓ: **Calculator**
1. ਇੱਕ ਨਵੀਂ Visual Studio Code ਵਿੰਡੋ ਖੁੱਲੇਗੀ। **Yes, I trust the authors** ਚੁਣੋ।
1. ਟਰਮੀਨਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ: `python -m venv .venv`
1. ਟਰਮੀਨਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਚਾਲੂ ਕਰੋ:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. ਟਰਮੀਨਲ ਵਿੱਚ ਡਿਪੈਂਡੇਂਸੀ ਇੰਸਟਾਲ ਕਰੋ: `pip install -e .[dev]`
1. **Activity Bar** ਦੇ **Explorer** ਵਿੱਚ **src** ਫੋਲਡਰ ਖੋਲ੍ਹੋ ਅਤੇ ਐਡੀਟਰ ਵਿੱਚ ਫਾਈਲ ਖੋਲ੍ਹਣ ਲਈ **server.py** ਚੁਣੋ।
1. **server.py** ਫਾਈਲ ਵਿਚ ਕੋਡ ਨੂੰ ਇਹ ਨਾਲ ਬਦਲੋ ਅਤੇ ਸੇਵ ਕਰੋ:

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

### -4- ਕੈਲਕੂਲੇਟਰ MCP ਸਰਵਰ ਨਾਲ ਏਜੰਟ ਚਲਾਓ

ਹੁਣ ਜਦੋਂ ਤੁਹਾਡੇ ਏਜੰਟ ਕੋਲ ਟੂਲਜ਼ ਹਨ, ਸਮਾਂ ਹੈ ਉਹਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦਾ! ਇਸ ਹਿੱਸੇ ਵਿੱਚ, ਤੁਸੀਂ ਏਜੰਟ ਨੂੰ ਪ੍ਰਾਂਪਟ ਭੇਜੋਗੇ ਤਾਂ ਕਿ ਉਹ ਦੇਖ ਸਕੇ ਕਿ ਕੀ ਏਜੰਟ ਕੈਲਕੂਲੇਟਰ MCP ਸਰਵਰ ਤੋਂ ਸਹੀ ਟੂਲ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ।

![Visual Studio Code ਵਿੱਚ AI Toolkit ਵਾਧਾ ਲਈ Calculator Agent ਇੰਟਰਫੇਸ ਦਾ ਸਕਰੀਨਸ਼ਾਟ। ਖੱਬੇ ਪੈਨਲ 'ਚ "Tools" ਹੇਠਾਂ MCP ਸਰਵਰ ਨਾਮ local-server-calculator_server ਜੋੜਿਆ ਗਿਆ ਹੈ, ਜਿਸ ਵਿੱਚ ਚਾਰ ਉਪਲਬਧ ਟੂਲ ਹਨ: add, subtract, multiply, ਅਤੇ divide। ਇੱਕ ਬੈਜ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਚਾਰ ਟੂਲ ਸਰਗਰਮ ਹਨ। ਹੇਠਾਂ ਇੱਕ ਕਾਲਪਨੀਕ "Structure output" ਸੈਕਸ਼ਨ ਅਤੇ ਨੀਲਾ "Run" ਬਟਨ ਹੈ। ਸੱਜੇ ਪੈਨਲ 'ਤੇ "Model Response" ਹੇਠਾਂ, ਏਜੰਟ multiply ਅਤੇ subtract ਟੂਲ ਚਲਾ ਰਿਹਾ ਹੈ ਇੰਪੁਟ {"a": 3, "b": 25} ਅਤੇ {"a": 75, "b": 20} ਨਾਲ। ਅੰਤਿਮ "Tool Response" 75.0 ਹੈ। ਹੇਠਾਂ "View Code" ਬਟਨ ਹੈ।](../../../../translated_images/pa/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

ਤੁਸੀਂ ਆਪਣੇ ਲੋਕਲ ਡਿਵੈਲਪਮੈਂਟ ਮਸ਼ੀਨ 'ਤੇ MCP ਸਰਵਰ Agent Builder ਰਾਹੀਂ MCP ਕਲੀਐਂਟ ਵਜੋਂ ਚਲਾਓਗੇ।

1. MCP ਸਰਵਰ ਨੂੰ ਡੀਬੱਗ ਕਰਨ ਲਈ `F5` ਦਬਾਓ। **Agent (Prompt) Builder** ਨਵੀਂ ਐਡੀਟਰ ਟੈਬ ਵਿੱਚ ਖੁਲੇਗਾ। ਸਰਵਰ ਦੀ ਸਥਿਤੀ ਟਰਮੀਨਲ ਵਿੱਚ ਦਿਸੇਗੀ।
1. **Agent (Prompt) Builder** ਦੇ **User prompt** ਖੇਤਰ ਵਿੱਚ ਇਹ ਪ੍ਰਾਂਪਟ ਦਿਓ: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. ਏਜੰਟ ਦਾ ਜਵਾਬ ਤਿਆਰ ਕਰਨ ਲਈ **Run** ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
1. ਏਜੰਟ ਦੇ ਆਉਟਪੁੱਟ ਦੀ ਸਮੀਖਿਆ ਕਰੋ। ਮਾਡਲ ਨੂੰ ਨਤੀਜਾ ਕੱਢਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਤੁਸੀਂ **$55** ਦਾ ਭੁਗਤਾਨ ਕੀਤਾ।
1. ਇਸ ਦਾ ਵਿਸਥਾਰ ਇਹ ਹੈ ਕਿ:
    - ਏਜੰਟ ਗਣਿਤ ਵਿੱਚ ਸਹਾਇਤਾ ਲਈ **multiply** ਅਤੇ **subtract** ਟੂਲ ਚੁਣਦਾ ਹੈ।
    - multiply ਟੂਲ ਲਈ ਸੰਬੰਧਤ `a` ਅਤੇ `b` ਮੁੱਲ ਦਿੱਤੇ ਜਾਂਦੇ ਹਨ।
    - subtract ਟੂਲ ਲਈ ਸੰਬੰਧਤ `a` ਅਤੇ `b` ਮੁੱਲ ਦਿੱਤੇ ਜਾਂਦੇ ਹਨ।
    - ਹਰ ਟੂਲ ਦਾ ਜਵਾਬ ਵਿਭਿੰਨ **Tool Response** ਵਿੱਚ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ।
    - ਮਾਡਲ ਦਾ ਅੰਤਿਮ ਜਵਾਬ ਅਖੀਰ ਦੇ **Model Response** ਵਿੱਚ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ।
1. ਏਜੰਟ ਦੀ ਹੋਰ ਟੈਸਟਿੰਗ ਲਈ ਵਾਧੂ ਪ੍ਰਾਂਪਟ ਜਮ੍ਹਾਂ ਕਰੋ। ਤੁਸੀਂ ਮੌਜੂਦਾ ਪ੍ਰਾਂਪਟ ਨੂੰ ਸੋਧ ਕੇ ਨਵਾਂ ਪ੍ਰਾਂਪਟ ਦੇ ਸਕਦੇ ਹੋ।
1. ਇਸ ਤੋਂ ਬਾਅਦ, ਟੈਸਟਿੰਗ ਮੁਕੰਮਲ ਕਰਨ 'ਤੇ, ਸਰਵਰ ਰੋਕਣ ਲਈ ਟਰਮੀਨਲ ਵਿੱਚ **CTRL/CMD+C** ਦਬਾਓ।

## ਅਸਾਈਨਮੈਂਟ

ਆਪਣੇ **server.py** ਫਾਈਲ ਵਿੱਚ ਇੱਕ ਹੋਰ ਟੂਲ ਐਂਟਰੀ ਜੋੜ ਕੇ ਦੇਖੋ (ਜਿਵੇਂ ਕਿ ਕਿਸੇ ਨੰਬਰ ਦਾ ਵਰਗਮੂਲ ਦੇਣਾ)। ਵਾਧੂ ਪ੍ਰਾਂਪਟ ਜਮ੍ਹਾਂ ਕਰੋ ਜਿਹੜੇ ਤੁਹਾਡੇ ਨਵੇਂ (ਜਾਂ ਮੌਜੂਦਾ) ਟੂਲ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਣ। ਨਵੀਂ ਟੂਲਾਂ ਨੂੰ ਲੋਡ ਕਰਨ ਲਈ ਸਰਵਰ ਨੂੰ ਮੁੜ ਚਾਲੂ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਓ।

## ਹੱਲ

[Solution](./solution/README.md)

## ਮੁੱਖ ਸਿੱਖਿਆ

ਇਸ ਅਧਿਆਇ ਤੋਂ ਪਰਾਪਤ ਸਿੱਖਿਆਵਾਂ ਇਹ ਹਨ:

- AI Toolkit ਵਾਧਾ ਇੱਕ ਸ਼ਾਨਦਾਰ ਕਲੀਐਂਟ ਹੈ ਜੋ ਤੁਹਾਨੂੰ MCP ਸਰਵਰ ਅਤੇ ਇਸਦੇ ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦਿੰਦਾ ਹੈ।
- ਤੁਸੀਂ MCP ਸਰਵਰਾਂ ਵਿੱਚ ਨਵੇਂ ਟੂਲ ਜੋੜ ਕੇ ਏਜੰਟ ਦੀ ਯੋਗਤਾਵਾਂ ਵਧਾ ਸਕਦੇ ਹੋ ਜੋ ਵਿਕਾਸਸ਼ੀਲ ਮੰਗਾਂ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਹੈ।
- AI Toolkit ਵਿੱਚ ਟੈਮਪਲੇਟ ਸ਼ਾਮਲ ਹਨ (ਜਿਵੇਂ Python MCP ਸਰਵਰ ਟੈਮਪਲੇਟ) ਜੋ ਕਸਟਮ ਟੂਲ ਬਣਾਉਣ ਨੂੰ ਆਸਾਨ ਬਣਾਉਂਦੇ ਹਨ।

## ਹੋਰ ਸਰੋਤ

- [AI Toolkit ਦਸਤਾਵੇਜ਼](https://aka.ms/AIToolkit/doc)

## ਅਗਲਾ ਕਦਮ
- ਅਗਲਾ: [ਟੈਸਟਿੰਗ ਅਤੇ ਡੀਬੱਗਿੰਗ](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->