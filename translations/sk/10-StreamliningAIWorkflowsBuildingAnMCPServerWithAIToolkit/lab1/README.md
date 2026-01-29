# 🚀 Modul 1: Základy AI Toolkit

[![Duration](https://img.shields.io/badge/Duration-15%20minutes-blue.svg)]()
[![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-green.svg)]()
[![Prerequisites](https://img.shields.io/badge/Prerequisites-VS%20Code-orange.svg)]()

## 📋 Ciele učenia

Na konci tohto modulu budete vedieť:
- ✅ Nainštalovať a nakonfigurovať AI Toolkit pre Visual Studio Code
- ✅ Pohybovať sa v Katalógu modelov a porozumieť rôznym zdrojom modelov
- ✅ Používať Playground na testovanie a experimentovanie s modelmi
- ✅ Vytvárať vlastných AI agentov pomocou Agent Builder
- ✅ Porovnávať výkonnosť modelov od rôznych poskytovateľov
- ✅ Aplikovať osvedčené postupy pre prompt engineering

## 🧠 Úvod do AI Toolkit (AITK)

**AI Toolkit pre Visual Studio Code** je vlajkovým rozšírením Microsoftu, ktoré premení VS Code na komplexné vývojové prostredie pre AI. Prepojuje výskum AI s praktickým vývojom aplikácií a sprístupňuje generatívnu AI vývojárom na všetkých úrovniach.

### 🌟 Kľúčové funkcie

| Funkcia | Popis | Použitie |
|---------|-------------|----------|
| **🗂️ Katalóg modelov** | Prístup k viac ako 100 modelom z GitHub, ONNX, OpenAI, Anthropic, Google | Objavovanie a výber modelov |
| **🔌 Podpora BYOM** | Integrácia vlastných modelov (lokálnych alebo vzdialených) | Nasadenie vlastných modelov |
| **🎮 Interaktívny Playground** | Testovanie modelov v reálnom čase s chatovým rozhraním | Rýchle prototypovanie a testovanie |
| **📎 Podpora multimodálnych vstupov** | Práca s textom, obrázkami a prílohami | Zložité AI aplikácie |
| **⚡ Hromadné spracovanie** | Spustenie viacerých promptov naraz | Efektívne testovacie procesy |
| **📊 Hodnotenie modelov** | Vstavané metriky (F1, relevantnosť, podobnosť, koherencia) | Posúdenie výkonnosti |

### 🎯 Prečo je AI Toolkit dôležitý

- **🚀 Rýchlejší vývoj**: Od nápadu k prototypu za pár minút
- **🔄 Jednotný pracovný tok**: Jedno rozhranie pre viacerých AI poskytovateľov
- **🧪 Jednoduché experimentovanie**: Porovnávajte modely bez zložitého nastavenia
- **📈 Pripravený na produkciu**: Plynulý prechod z prototypu do nasadenia

## 🛠️ Požiadavky a nastavenie

### 📦 Inštalácia rozšírenia AI Toolkit

**Krok 1: Otvorte Marketplace rozšírení**
1. Spustite Visual Studio Code
2. Prejdite do zobrazenia rozšírení (`Ctrl+Shift+X` alebo `Cmd+Shift+X`)
3. Vyhľadajte "AI Toolkit"

**Krok 2: Vyberte verziu**
- **🟢 Release**: Odporúčané pre produkčné použitie
- **🔶 Pre-release**: Predbežný prístup k najnovším funkciám

**Krok 3: Inštalujte a aktivujte**

![AI Toolkit Extension](../../../../translated_images/sk/aitkext.d28945a03eed003c39fc39bc96ae655af9b64b9b922e78e88b07214420ed7985.png)

### ✅ Kontrolný zoznam overenia
- [ ] Ikona AI Toolkit sa zobrazuje v bočnom paneli VS Code
- [ ] Rozšírenie je povolené a aktívne
- [ ] V paneli výstupu nie sú žiadne chyby inštalácie

## 🧪 Praktické cvičenie 1: Preskúmanie modelov na GitHub

**🎯 Cieľ**: Ovládnuť Katalóg modelov a otestovať svoj prvý AI model

### 📊 Krok 1: Preskúmajte Katalóg modelov

Katalóg modelov je vašou bránou do AI ekosystému. Zhromažďuje modely od viacerých poskytovateľov, čo uľahčuje ich objavovanie a porovnávanie.

**🔍 Navigačný návod:**

Kliknite na **MODELS - Catalog** v bočnom paneli AI Toolkit

![Model Catalog](../../../../translated_images/sk/aimodel.263ed2be013d8fb0e2265c4f742cfe490f6f00eca5e132ec50438c8e826e34ed.png)

**💡 Tip**: Hľadajte modely s konkrétnymi schopnosťami, ktoré zodpovedajú vášmu prípadu použitia (napr. generovanie kódu, kreatívne písanie, analýza).

**⚠️ Poznámka**: Modely hostované na GitHub (GitHub Models) sú zadarmo, ale podliehajú limitom na počet požiadaviek a tokenov. Ak chcete pristupovať k modelom mimo GitHub (napr. externé modely cez Azure AI alebo iné endpointy), budete potrebovať príslušný API kľúč alebo autentifikáciu.

### 🚀 Krok 2: Pridajte a nakonfigurujte svoj prvý model

**Stratégia výberu modelu:**
- **GPT-4.1**: Najlepší pre zložité uvažovanie a analýzu
- **Phi-4-mini**: Ľahký, rýchly na jednoduché úlohy

**🔧 Proces konfigurácie:**
1. Vyberte **OpenAI GPT-4.1** z katalógu
2. Kliknite na **Add to My Models** – tým sa model zaregistruje na použitie
3. Zvoľte **Try in Playground** pre spustenie testovacieho prostredia
4. Počkajte na inicializáciu modelu (prvé spustenie môže chvíľu trvať)

![Playground Setup](../../../../translated_images/sk/playground.dd6f5141344878ca4d4f3de819775da7b113518941accf37c291117c602f85db.png)

**⚙️ Pochopenie parametrov modelu:**
- **Temperature**: Ovláda kreativitu (0 = deterministické, 1 = kreatívne)
- **Max Tokens**: Maximálna dĺžka odpovede
- **Top-p**: Nucleus sampling pre rozmanitosť odpovedí

### 🎯 Krok 3: Ovládnite rozhranie Playground

Playground je vaše laboratórium na experimentovanie s AI. Tu je, ako vyťažiť z neho maximum:

**🎨 Najlepšie postupy pre prompt engineering:**
1. **Buďte konkrétni**: Jasné a detailné inštrukcie prinášajú lepšie výsledky
2. **Poskytnite kontext**: Pridajte relevantné pozadie
3. **Používajte príklady**: Ukážte modelu, čo chcete, na príkladoch
4. **Iterujte**: Vylepšujte prompt podľa prvých výsledkov

**🧪 Testovacie scenáre:**
```markdown
# Example 1: Code Generation
"Write a Python function that calculates the factorial of a number using recursion. Include error handling and docstrings."

# Example 2: Creative Writing
"Write a professional email to a client explaining a project delay, maintaining a positive tone while being transparent about challenges."

# Example 3: Data Analysis
"Analyze this sales data and provide insights: [paste your data]. Focus on trends, anomalies, and actionable recommendations."
```

![Testing Results](../../../../translated_images/sk/result.1dfcf211fb359cf65902b09db191d3bfc65713ca15e279c1a30be213bb526949.png)

### 🏆 Výzva: Porovnanie výkonnosti modelov

**🎯 Cieľ**: Porovnať rôzne modely pomocou rovnakých promptov a pochopiť ich silné stránky

**📋 Inštrukcie:**
1. Pridajte **Phi-4-mini** do svojho pracovného priestoru
2. Použite rovnaký prompt pre GPT-4.1 aj Phi-4-mini

![set](../../../../translated_images/sk/set.88132df189ecde2cbbda256c1841db5aac8e9bdeba1a4e343dfa031b9545d6c9.png)

3. Porovnajte kvalitu odpovedí, rýchlosť a presnosť
4. Zaznamenajte svoje zistenia v sekcii výsledkov

![Model Comparison](../../../../translated_images/sk/compare.97746cd0f907495503c1fc217739f3890dc76ea5f6fd92379a6db0cc331feb58.png)

**💡 Kľúčové poznatky:**
- Kedy použiť LLM vs SLM
- Pomery nákladov a výkonu
- Špecializované schopnosti rôznych modelov

## 🤖 Praktické cvičenie 2: Vytváranie vlastných agentov pomocou Agent Builder

**🎯 Cieľ**: Vytvoriť špecializovaných AI agentov prispôsobených konkrétnym úlohám a pracovným tokom

### 🏗️ Krok 1: Pochopenie Agent Builder

Agent Builder je miesto, kde AI Toolkit naozaj vyniká. Umožňuje vytvárať účelovo zameraných AI asistentov, ktorí kombinujú silu veľkých jazykových modelov s vlastnými inštrukciami, špecifickými parametrami a odbornými znalosťami.

**🧠 Komponenty architektúry agenta:**
- **Jadrový model**: Základný LLM (GPT-4, Groks, Phi, atď.)
- **Systémový prompt**: Definuje osobnosť a správanie agenta
- **Parametre**: Jemné doladenie pre optimálny výkon
- **Integrácia nástrojov**: Prepojenie na externé API a MCP služby
- **Pamäť**: Kontext konverzácie a ukladanie relácií

![Agent Builder Interface](../../../../translated_images/sk/agentbuilder.25895b2d2f8c02e7aa99dd40e105877a6f1db8f0441180087e39db67744b361f.png)

### ⚙️ Krok 2: Hlbší pohľad na konfiguráciu agenta

**🎨 Vytváranie efektívnych systémových promptov:**
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

*Samozrejme, môžete použiť aj Generate System Prompt, aby vám AI pomohla s tvorbou a optimalizáciou promptov*

**🔧 Optimalizácia parametrov:**
| Parameter | Odporúčaný rozsah | Použitie |
|-----------|------------------|----------|
| **Temperature** | 0.1-0.3 | Technické/faktické odpovede |
| **Temperature** | 0.7-0.9 | Kreatívne/brainstormingové úlohy |
| **Max Tokens** | 500-1000 | Stručné odpovede |
| **Max Tokens** | 2000-4000 | Podrobné vysvetlenia |

### 🐍 Krok 3: Praktické cvičenie – Python programovací agent

**🎯 Misia**: Vytvoriť špecializovaného asistenta pre Python kódovanie

**📋 Kroky konfigurácie:**

1. **Výber modelu**: Zvoľte **Claude 3.5 Sonnet** (vynikajúci pre kódovanie)

2. **Návrh systémového promptu**:
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

3. **Nastavenie parametrov**:
   - Temperature: 0.2 (pre konzistentný a spoľahlivý kód)
   - Max Tokens: 2000 (podrobné vysvetlenia)
   - Top-p: 0.9 (vyvážená kreativita)

![Python Agent Configuration](../../../../translated_images/sk/pythonagent.5e51b406401c165fcabfd66f2d943c27f46b5fed0f9fb73abefc9e91ca3489d4.png)

### 🧪 Krok 4: Testovanie vášho Python agenta

**Testovacie scenáre:**
1. **Základná funkcia**: "Vytvor funkciu na hľadanie prvočísel"
2. **Zložitý algoritmus**: "Implementuj binárny vyhľadávací strom s metódami insert, delete a search"
3. **Reálny problém**: "Vytvor web scraper, ktorý zvláda limitovanie požiadaviek a opakovania"
4. **Ladenie chýb**: "Oprav tento kód [vložiť chybný kód]"

**🏆 Kritériá úspechu:**
- ✅ Kód beží bez chýb
- ✅ Obsahuje správnu dokumentáciu
- ✅ Dodržiava najlepšie praktiky Pythonu
- ✅ Poskytuje jasné vysvetlenia
- ✅ Navrhuje vylepšenia

## 🎓 Zhrnutie modulu 1 a ďalšie kroky

### 📊 Overenie vedomostí

Otestujte svoje znalosti:
- [ ] Viete vysvetliť rozdiely medzi modelmi v katalógu?
- [ ] Podarilo sa vám vytvoriť a otestovať vlastného agenta?
- [ ] Rozumiete, ako optimalizovať parametre pre rôzne prípady použitia?
- [ ] Viete navrhnúť efektívne systémové prompty?

### 📚 Dodatočné zdroje

- **Dokumentácia AI Toolkit**: [Oficiálne Microsoft Docs](https://github.com/microsoft/vscode-ai-toolkit)
- **Sprievodca prompt engineeringom**: [Najlepšie postupy](https://platform.openai.com/docs/guides/prompt-engineering)
- **Modely v AI Toolkit**: [Modely vo vývoji](https://github.com/microsoft/vscode-ai-toolkit/blob/main/doc/models.md)

**🎉 Gratulujeme!** Ovládli ste základy AI Toolkit a ste pripravení vytvárať pokročilejšie AI aplikácie!

### 🔜 Pokračujte do ďalšieho modulu

Ste pripravení na pokročilejšie funkcie? Pokračujte do **[Modul 2: MCP s AI Toolkit – základy](../lab2/README.md)**, kde sa naučíte:
- Pripojiť agentov k externým nástrojom pomocou Model Context Protocol (MCP)
- Vytvárať agentov pre automatizáciu prehliadača s Playwright
- Integrovať MCP servery s vašimi AI Toolkit agentmi
- Vylepšiť agentov externými dátami a schopnosťami

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.