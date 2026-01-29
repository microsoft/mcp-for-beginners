# 🚀 Module 1: Mga Pangunahing Kaalaman sa AI Toolkit

[![Duration](https://img.shields.io/badge/Duration-15%20minutes-blue.svg)]()
[![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-green.svg)]()
[![Prerequisites](https://img.shields.io/badge/Prerequisites-VS%20Code-orange.svg)]()

## 📋 Mga Layunin sa Pagkatuto

Sa pagtatapos ng module na ito, magagawa mong:
- ✅ I-install at i-configure ang AI Toolkit para sa Visual Studio Code
- ✅ Mag-navigate sa Model Catalog at maunawaan ang iba't ibang pinagmulan ng mga modelo
- ✅ Gamitin ang Playground para sa pagsubok at eksperimento ng mga modelo
- ✅ Gumawa ng mga custom na AI agent gamit ang Agent Builder
- ✅ Ihambing ang performance ng mga modelo mula sa iba't ibang provider
- ✅ Ipatupad ang mga pinakamahusay na kasanayan sa prompt engineering

## 🧠 Panimula sa AI Toolkit (AITK)

Ang **AI Toolkit para sa Visual Studio Code** ay pangunahing extension ng Microsoft na nagbabago sa VS Code bilang isang kumpletong kapaligiran para sa pag-develop ng AI. Pinag-uugnay nito ang pagitan ng pananaliksik sa AI at praktikal na pagbuo ng aplikasyon, kaya't nagiging accessible ang generative AI para sa mga developer sa lahat ng antas ng kasanayan.

### 🌟 Pangunahing Kakayahan

| Tampok | Paglalarawan | Gamit |
|---------|-------------|----------|
| **🗂️ Model Catalog** | Access sa mahigit 100 modelo mula sa GitHub, ONNX, OpenAI, Anthropic, Google | Paghahanap at pagpili ng modelo |
| **🔌 BYOM Support** | Isama ang sarili mong mga modelo (lokal/manwal) | Custom na deployment ng modelo |
| **🎮 Interactive Playground** | Real-time na pagsubok ng modelo gamit ang chat interface | Mabilisang prototyping at testing |
| **📎 Multi-Modal Support** | Paghawak ng teksto, larawan, at mga attachment | Mga komplikadong AI application |
| **⚡ Batch Processing** | Patakbuhin ang maraming prompt nang sabay-sabay | Epektibong workflow sa pagsubok |
| **📊 Model Evaluation** | May kasamang metrics (F1, relevance, similarity, coherence) | Pagsusuri ng performance |

### 🎯 Bakit Mahalaga ang AI Toolkit

- **🚀 Pinabilis na Pag-develop**: Mula ideya hanggang prototype sa loob ng ilang minuto
- **🔄 Pinagsamang Workflow**: Isang interface para sa maraming AI provider
- **🧪 Madaling Eksperimento**: Ihambing ang mga modelo nang walang komplikadong setup
- **📈 Handa para sa Produksyon**: Mabilis na paglipat mula prototype hanggang deployment

## 🛠️ Mga Kinakailangan at Setup

### 📦 Pag-install ng AI Toolkit Extension

**Hakbang 1: Buksan ang Extensions Marketplace**
1. Buksan ang Visual Studio Code
2. Pumunta sa Extensions view (`Ctrl+Shift+X` o `Cmd+Shift+X`)
3. Hanapin ang "AI Toolkit"

**Hakbang 2: Piliin ang Bersyon**
- **🟢 Release**: Inirerekomenda para sa production use
- **🔶 Pre-release**: Maagang access sa mga bagong tampok

**Hakbang 3: I-install at I-activate**

![AI Toolkit Extension](../../../../translated_images/tl/aitkext.d28945a03eed003c39fc39bc96ae655af9b64b9b922e78e88b07214420ed7985.png)

### ✅ Checklist sa Pag-verify
- [ ] Lumabas ang AI Toolkit icon sa sidebar ng VS Code
- [ ] Na-enable at na-activate ang extension
- [ ] Walang error sa pag-install sa output panel

## 🧪 Hands-on Exercise 1: Pagsusuri sa mga Modelo ng GitHub

**🎯 Layunin**: Maging bihasa sa Model Catalog at subukan ang iyong unang AI model

### 📊 Hakbang 1: Mag-navigate sa Model Catalog

Ang Model Catalog ang iyong daan sa AI ecosystem. Pinagsasama-sama nito ang mga modelo mula sa iba't ibang provider, kaya madali kang makakahanap at makakapagkumpara ng mga opsyon.

**🔍 Gabay sa Pag-navigate:**

I-click ang **MODELS - Catalog** sa AI Toolkit sidebar

![Model Catalog](../../../../translated_images/tl/aimodel.263ed2be013d8fb0e2265c4f742cfe490f6f00eca5e132ec50438c8e826e34ed.png)

**💡 Tip**: Hanapin ang mga modelo na may partikular na kakayahan na tugma sa iyong pangangailangan (hal., code generation, malikhaing pagsulat, pagsusuri).

**⚠️ Note**: Ang mga modelong naka-host sa GitHub (GitHub Models) ay libre gamitin ngunit may limitasyon sa dami ng request at token. Kung nais mong gamitin ang mga non-GitHub models (mga external na modelo na naka-host sa Azure AI o iba pang endpoints), kailangan mong magbigay ng tamang API key o authentication.

### 🚀 Hakbang 2: Idagdag at I-configure ang Iyong Unang Modelo

**Strategiya sa Pagpili ng Modelo:**
- **GPT-4.1**: Pinakamainam para sa komplikadong pag-iisip at pagsusuri
- **Phi-4-mini**: Magaan at mabilis na tugon para sa simpleng gawain

**🔧 Proseso ng Pag-configure:**
1. Piliin ang **OpenAI GPT-4.1** mula sa catalog
2. I-click ang **Add to My Models** - ito ay magrerehistro ng modelo para magamit
3. Piliin ang **Try in Playground** para ilunsad ang testing environment
4. Maghintay para sa initialization ng modelo (maaaring tumagal ng kaunti sa unang setup)

![Playground Setup](../../../../translated_images/tl/playground.dd6f5141344878ca4d4f3de819775da7b113518941accf37c291117c602f85db.png)

**⚙️ Pag-unawa sa Mga Parameter ng Modelo:**
- **Temperature**: Kontrol sa pagiging malikhain (0 = deterministic, 1 = malikhain)
- **Max Tokens**: Pinakamahabang sagot na maaaring ibigay
- **Top-p**: Nucleus sampling para sa pagkakaiba-iba ng sagot

### 🎯 Hakbang 3: Maging Eksperto sa Playground Interface

Ang Playground ang iyong laboratoryo para sa eksperimento sa AI. Narito kung paano mo mapapakinabangan ito nang husto:

**🎨 Pinakamahusay na Kasanayan sa Prompt Engineering:**
1. **Maging Tiyak**: Malinaw at detalyadong mga tagubilin ang mas maganda ang resulta
2. **Magbigay ng Konteksto**: Isama ang mahalagang background na impormasyon
3. **Gumamit ng Halimbawa**: Ipakita sa modelo ang gusto mo gamit ang mga halimbawa
4. **Ulitin**: I-refine ang mga prompt base sa unang resulta

**🧪 Mga Senaryo sa Pagsubok:**
```markdown
# Example 1: Code Generation
"Write a Python function that calculates the factorial of a number using recursion. Include error handling and docstrings."

# Example 2: Creative Writing
"Write a professional email to a client explaining a project delay, maintaining a positive tone while being transparent about challenges."

# Example 3: Data Analysis
"Analyze this sales data and provide insights: [paste your data]. Focus on trends, anomalies, and actionable recommendations."
```

![Testing Results](../../../../translated_images/tl/result.1dfcf211fb359cf65902b09db191d3bfc65713ca15e279c1a30be213bb526949.png)

### 🏆 Hamon: Paghahambing ng Performance ng Modelo

**🎯 Layunin**: Ihambing ang iba't ibang modelo gamit ang parehong prompt upang maunawaan ang kanilang kalakasan

**📋 Mga Tagubilin:**
1. Idagdag ang **Phi-4-mini** sa iyong workspace
2. Gamitin ang parehong prompt para sa GPT-4.1 at Phi-4-mini

![set](../../../../translated_images/tl/set.88132df189ecde2cbbda256c1841db5aac8e9bdeba1a4e343dfa031b9545d6c9.png)

3. Ihambing ang kalidad ng sagot, bilis, at katumpakan
4. I-dokumento ang iyong mga natuklasan sa seksyon ng resulta

![Model Comparison](../../../../translated_images/tl/compare.97746cd0f907495503c1fc217739f3890dc76ea5f6fd92379a6db0cc331feb58.png)

**💡 Mahahalagang Punto na Dapat Matuklasan:**
- Kailan gagamit ng LLM kumpara sa SLM
- Pagsusuri ng gastos laban sa performance
- Espesyal na kakayahan ng iba't ibang modelo

## 🤖 Hands-on Exercise 2: Paggawa ng Custom Agents gamit ang Agent Builder

**🎯 Layunin**: Gumawa ng mga espesyal na AI agent na angkop para sa partikular na gawain at workflow

### 🏗️ Hakbang 1: Pag-unawa sa Agent Builder

Dito tunay na namumukod-tangi ang AI Toolkit. Pinapayagan ka nitong gumawa ng mga AI assistant na may tiyak na layunin na pinagsasama ang lakas ng malalaking language model sa custom na mga tagubilin, partikular na mga parameter, at espesyal na kaalaman.

**🧠 Mga Bahagi ng Arkitektura ng Agent:**
- **Core Model**: Pangunahing LLM (GPT-4, Groks, Phi, atbp.)
- **System Prompt**: Nagpapakilala sa personalidad at kilos ng agent
- **Parameters**: Mga pinong setting para sa pinakamainam na performance
- **Tools Integration**: Koneksyon sa external APIs at MCP services
- **Memory**: Konteksto ng pag-uusap at pagpapanatili ng session

![Agent Builder Interface](../../../../translated_images/tl/agentbuilder.25895b2d2f8c02e7aa99dd40e105877a6f1db8f0441180087e39db67744b361f.png)

### ⚙️ Hakbang 2: Malalimang Pag-configure ng Agent

**🎨 Paggawa ng Epektibong System Prompts:**
```markdown
# Template Structure:
## Role Definition
You are a [specific role] with expertise in [domain].

## Capabilities
- List specific abilities
- Define scope of knowledge
- Clarify limitations

## Behavior Guidelines
- Response style (formal, casual, technical)
- Output format preferences
- Error handling approach

## Examples
Provide 2-3 examples of ideal interactions
```

*Syempre, maaari mo ring gamitin ang Generate System Prompt para tulungan ka ng AI na gumawa at i-optimize ang mga prompt*

**🔧 Pag-optimize ng Parameter:**
| Parameter | Inirerekomendang Saklaw | Gamit |
|-----------|-------------------------|----------|
| **Temperature** | 0.1-0.3 | Mga teknikal o factual na sagot |
| **Temperature** | 0.7-0.9 | Malikhaing gawain o brainstorming |
| **Max Tokens** | 500-1000 | Maikling sagot |
| **Max Tokens** | 2000-4000 | Detalyadong paliwanag |

### 🐍 Hakbang 3: Praktikal na Pagsasanay - Python Programming Agent

**🎯 Misyon**: Gumawa ng espesyal na assistant para sa Python coding

**📋 Mga Hakbang sa Pag-configure:**

1. **Pagpili ng Modelo**: Piliin ang **Claude 3.5 Sonnet** (magaling sa code)

2. **Disenyo ng System Prompt**:
```markdown
# Python Programming Expert Agent

## Role
You are a senior Python developer with 10+ years of experience. You excel at writing clean, efficient, and well-documented Python code.

## Capabilities
- Write production-ready Python code
- Debug complex issues
- Explain code concepts clearly
- Suggest best practices and optimizations
- Provide complete working examples

## Response Format
- Always include docstrings
- Add inline comments for complex logic
- Suggest testing approaches
- Mention relevant libraries when applicable

## Code Quality Standards
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Handle exceptions gracefully
- Write readable, maintainable code
```

3. **Pag-configure ng Parameter**:
   - Temperature: 0.2 (para sa consistent at maaasahang code)
   - Max Tokens: 2000 (detalyadong paliwanag)
   - Top-p: 0.9 (balanseng pagiging malikhain)

![Python Agent Configuration](../../../../translated_images/tl/pythonagent.5e51b406401c165fcabfd66f2d943c27f46b5fed0f9fb73abefc9e91ca3489d4.png)

### 🧪 Hakbang 4: Pagsubok sa Iyong Python Agent

**Mga Senaryo sa Pagsubok:**
1. **Pangunahing Function**: "Gumawa ng function para maghanap ng prime numbers"
2. **Komplikadong Algorithm**: "I-implement ang binary search tree na may insert, delete, at search methods"
3. **Problema sa Totoong Mundo**: "Gumawa ng web scraper na kayang humawak ng rate limiting at retries"
4. **Pag-debug**: "Ayusin ang code na ito [ipaste ang buggy code]"

**🏆 Mga Pamantayan sa Tagumpay:**
- ✅ Tumakbo ang code nang walang error
- ✅ May tamang dokumentasyon
- ✅ Sumusunod sa pinakamahusay na kasanayan sa Python
- ✅ Nagbibigay ng malinaw na paliwanag
- ✅ Nagmumungkahi ng mga pagpapabuti

## 🎓 Pagtatapos ng Module 1 at Mga Susunod na Hakbang

### 📊 Pagsusulit sa Kaalaman

Subukan ang iyong pagkaunawa:
- [ ] Naiipaliwanag mo ba ang pagkakaiba ng mga modelo sa catalog?
- [ ] Nagawa mo na bang gumawa at subukan ang isang custom agent?
- [ ] Naiintindihan mo ba kung paano i-optimize ang mga parameter para sa iba't ibang gamit?
- [ ] Kaya mo bang magdisenyo ng epektibong system prompts?

### 📚 Karagdagang Mga Sanggunian

- **AI Toolkit Documentation**: [Official Microsoft Docs](https://github.com/microsoft/vscode-ai-toolkit)
- **Prompt Engineering Guide**: [Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- **Models in AI Toolkit**: [Models in Develpment](https://github.com/microsoft/vscode-ai-toolkit/blob/main/doc/models.md)

**🎉 Congratulations!** Naitaguyod mo na ang mga pangunahing kaalaman sa AI Toolkit at handa ka nang gumawa ng mas advanced na AI applications!

### 🔜 Magpatuloy sa Susunod na Module

Handa ka na ba sa mas advanced na kakayahan? Magpatuloy sa **[Module 2: MCP with AI Toolkit Fundamentals](../lab2/README.md)** kung saan matututuhan mo kung paano:
- Ikonekta ang iyong mga agent sa external tools gamit ang Model Context Protocol (MCP)
- Gumawa ng browser automation agents gamit ang Playwright
- Isama ang MCP servers sa iyong AI Toolkit agents
- Palakasin ang iyong mga agent gamit ang external na data at kakayahan

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.