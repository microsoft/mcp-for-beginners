<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2aa9dbc165e104764fa57e8a0d3f1c73",
  "translation_date": "2025-08-26T17:02:17+00:00",
  "source_file": "10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md",
  "language_code": "lt"
}
-->
# 🚀 Modulis 1: AI Toolkit Pagrindai

[![Trukmė](https://img.shields.io/badge/Duration-15%20minutes-blue.svg)]()
[![Sudėtingumas](https://img.shields.io/badge/Difficulty-Beginner-green.svg)]()
[![Reikalavimai](https://img.shields.io/badge/Prerequisites-VS%20Code-orange.svg)]()

## 📋 Mokymosi tikslai

Baigę šį modulį, galėsite:
- ✅ Įdiegti ir sukonfigūruoti AI Toolkit Visual Studio Code aplinkoje
- ✅ Naršyti Modelių katalogą ir suprasti skirtingus modelių šaltinius
- ✅ Naudoti Playground modelių testavimui ir eksperimentavimui
- ✅ Kurti individualius AI agentus naudojant Agent Builder
- ✅ Palyginti modelių našumą tarp skirtingų tiekėjų
- ✅ Taikyti geriausias praktikas kuriant užklausas (prompt engineering)

## 🧠 Įvadas į AI Toolkit (AITK)

**AI Toolkit for Visual Studio Code** yra pagrindinis „Microsoft“ plėtinys, kuris paverčia VS Code visapusiška AI kūrimo aplinka. Jis sujungia AI tyrimus su praktiniu programų kūrimu, padarydamas generatyvinį AI prieinamą visų lygių kūrėjams.

### 🌟 Pagrindinės galimybės

| Funkcija | Aprašymas | Pritaikymas |
|----------|-----------|-------------|
| **🗂️ Modelių katalogas** | Prieiga prie daugiau nei 100 modelių iš GitHub, ONNX, OpenAI, Anthropic, Google | Modelių atranka ir pasirinkimas |
| **🔌 BYOM palaikymas** | Integruokite savo modelius (vietinius/nuotolinius) | Individualių modelių diegimas |
| **🎮 Interaktyvus Playground** | Realaus laiko modelių testavimas su pokalbių sąsaja | Greitas prototipų kūrimas ir testavimas |
| **📎 Multi-modalinis palaikymas** | Darbas su tekstu, vaizdais ir priedais | Sudėtingos AI programos |
| **⚡ Grupinis apdorojimas** | Vienu metu vykdykite kelias užklausas | Efektyvūs testavimo procesai |
| **📊 Modelių vertinimas** | Integruoti metrikos rodikliai (F1, aktualumas, panašumas, nuoseklumas) | Našumo vertinimas |

### 🎯 Kodėl AI Toolkit yra svarbus

- **🚀 Spartesnis kūrimas**: Nuo idėjos iki prototipo per kelias minutes
- **🔄 Vieninga darbo eiga**: Viena sąsaja keliems AI tiekėjams
- **🧪 Lengvas eksperimentavimas**: Modelių palyginimas be sudėtingų nustatymų
- **📈 Paruošta gamybai**: Sklandus perėjimas nuo prototipo prie diegimo

## 🛠️ Reikalavimai ir nustatymas

### 📦 AI Toolkit plėtinio diegimas

**1 žingsnis: Prieiga prie Extensions Marketplace**
1. Atidarykite Visual Studio Code
2. Eikite į Extensions peržiūrą (`Ctrl+Shift+X` arba `Cmd+Shift+X`)
3. Ieškokite „AI Toolkit“

**2 žingsnis: Pasirinkite versiją**
- **🟢 Stabilus leidimas**: Rekomenduojama naudoti gamyboje
- **🔶 Išankstinis leidimas**: Ankstyva prieiga prie naujausių funkcijų

**3 žingsnis: Įdiekite ir aktyvuokite**

![AI Toolkit Extension](../../../../translated_images/aitkext.d28945a03eed003c39fc39bc96ae655af9b64b9b922e78e88b07214420ed7985.lt.png)

### ✅ Patikrinimo sąrašas
- [ ] AI Toolkit piktograma matoma VS Code šoninėje juostoje
- [ ] Plėtinys įjungtas ir aktyvuotas
- [ ] Nėra diegimo klaidų išvesties skydelyje

## 🧪 Praktinė užduotis 1: GitHub modelių tyrinėjimas

**🎯 Tikslas**: Įvaldyti Modelių katalogą ir išbandyti pirmąjį AI modelį

### 📊 1 žingsnis: Naršykite Modelių katalogą

Modelių katalogas yra jūsų vartai į AI ekosistemą. Jis apjungia modelius iš kelių tiekėjų, todėl lengva atrasti ir palyginti galimybes.

**🔍 Naršymo vadovas:**

Spustelėkite **MODELS - Catalog** AI Toolkit šoninėje juostoje

![Model Catalog](../../../../translated_images/aimodel.263ed2be013d8fb0e2265c4f742cfe490f6f00eca5e132ec50438c8e826e34ed.lt.png)

**💡 Patarimas**: Ieškokite modelių su specifinėmis galimybėmis, atitinkančiomis jūsų poreikius (pvz., kodo generavimas, kūrybinis rašymas, analizė).

**⚠️ Pastaba**: GitHub talpinami modeliai (pvz., GitHub Models) yra nemokami, tačiau jiems taikomi užklausų ir žetonų apribojimai. Jei norite pasiekti ne GitHub modelius (pvz., išorinius modelius, talpinamus per Azure AI ar kitus galinius taškus), turėsite pateikti atitinkamą API raktą arba autentifikaciją.

### 🚀 2 žingsnis: Pridėkite ir sukonfigūruokite pirmąjį modelį

**Modelio pasirinkimo strategija:**
- **GPT-4.1**: Geriausias sudėtingam mąstymui ir analizei
- **Phi-4-mini**: Lengvas, greitas atsakas paprastoms užduotims

**🔧 Konfigūravimo procesas:**
1. Pasirinkite **OpenAI GPT-4.1** iš katalogo
2. Spustelėkite **Add to My Models** - tai užregistruos modelį naudojimui
3. Pasirinkite **Try in Playground**, kad paleistumėte testavimo aplinką
4. Palaukite, kol modelis bus inicializuotas (pirmasis nustatymas gali užtrukti)

![Playground Setup](../../../../translated_images/playground.dd6f5141344878ca4d4f3de819775da7b113518941accf37c291117c602f85db.lt.png)

**⚙️ Modelio parametrų supratimas:**
- **Temperature**: Valdo kūrybiškumą (0 = deterministinis, 1 = kūrybiškas)
- **Max Tokens**: Maksimalus atsakymo ilgis
- **Top-p**: Nucleus sampling atsakymo įvairovei

### 🎯 3 žingsnis: Įvaldykite Playground sąsają

Playground yra jūsų AI eksperimentavimo laboratorija. Štai kaip maksimaliai išnaudoti jos galimybes:

**🎨 Geriausios praktikos kuriant užklausas:**
1. **Būkite konkretūs**: Aiškios, detalios instrukcijos duoda geresnius rezultatus
2. **Pateikite kontekstą**: Įtraukite svarbią foninę informaciją
3. **Naudokite pavyzdžius**: Parodykite modeliui, ko norite, naudodami pavyzdžius
4. **Iteruokite**: Tobulinkite užklausas pagal pradinius rezultatus

**🧪 Testavimo scenarijai:**
```markdown
# Example 1: Code Generation
"Write a Python function that calculates the factorial of a number using recursion. Include error handling and docstrings."

# Example 2: Creative Writing
"Write a professional email to a client explaining a project delay, maintaining a positive tone while being transparent about challenges."

# Example 3: Data Analysis
"Analyze this sales data and provide insights: [paste your data]. Focus on trends, anomalies, and actionable recommendations."
```

![Testing Results](../../../../translated_images/result.1dfcf211fb359cf65902b09db191d3bfc65713ca15e279c1a30be213bb526949.lt.png)

### 🏆 Iššūkio užduotis: Modelių našumo palyginimas

**🎯 Tikslas**: Palyginti skirtingus modelius naudojant identiškas užklausas, kad suprastumėte jų stipriąsias puses

**📋 Instrukcijos:**
1. Pridėkite **Phi-4-mini** į savo darbo aplinką
2. Naudokite tą pačią užklausą tiek GPT-4.1, tiek Phi-4-mini

![set](../../../../translated_images/set.88132df189ecde2cbbda256c1841db5aac8e9bdeba1a4e343dfa031b9545d6c9.lt.png)

3. Palyginkite atsakymų kokybę, greitį ir tikslumą
4. Dokumentuokite savo pastebėjimus rezultatų skyriuje

![Model Comparison](../../../../translated_images/compare.97746cd0f907495503c1fc217739f3890dc76ea5f6fd92379a6db0cc331feb58.lt.png)

**💡 Pagrindinės įžvalgos:**
- Kada naudoti LLM prieš SLM
- Kainos ir našumo kompromisai
- Skirtingų modelių specializuotos galimybės

## 🤖 Praktinė užduotis 2: Individualių agentų kūrimas su Agent Builder

**🎯 Tikslas**: Kurti specializuotus AI agentus, pritaikytus specifinėms užduotims ir darbo eigoms

### 🏗️ 1 žingsnis: Suprasti Agent Builder

Agent Builder yra vieta, kur AI Toolkit tikrai išsiskiria. Jis leidžia kurti tikslinius AI asistentus, kurie sujungia didelių kalbos modelių galią su individualiomis instrukcijomis, specifiniais parametrais ir specializuotomis žiniomis.

**🧠 Agentų architektūros komponentai:**
- **Pagrindinis modelis**: LLM pagrindas (GPT-4, Groks, Phi ir kt.)
- **Sistemos užklausa**: Apibrėžia agento asmenybę ir elgesį
- **Parametrai**: Optimizuoti nustatymai geriausiam našumui
- **Įrankių integracija**: Prisijungimas prie išorinių API ir MCP paslaugų
- **Atmintis**: Pokalbio kontekstas ir sesijos išsaugojimas

![Agent Builder Interface](../../../../translated_images/agentbuilder.25895b2d2f8c02e7aa99dd40e105877a6f1db8f0441180087e39db67744b361f.lt.png)

### ⚙️ 2 žingsnis: Agentų konfigūravimo gilinimasis

**🎨 Efektyvių sisteminių užklausų kūrimas:**
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

*Žinoma, galite naudoti Generate System Prompt, kad AI padėtų jums generuoti ir optimizuoti užklausas*

**🔧 Parametrų optimizavimas:**
| Parametras | Rekomenduojamas diapazonas | Pritaikymas |
|------------|----------------------------|-------------|
| **Temperature** | 0.1-0.3 | Techniniai/faktiniai atsakymai |
| **Temperature** | 0.7-0.9 | Kūrybinės/smegenų šturmo užduotys |
| **Max Tokens** | 500-1000 | Trumpi atsakymai |
| **Max Tokens** | 2000-4000 | Išsamūs paaiškinimai |

### 🐍 3 žingsnis: Praktinė užduotis - Python programavimo agentas

**🎯 Misija**: Sukurti specializuotą Python kodavimo asistentą

**📋 Konfigūravimo žingsniai:**

1. **Modelio pasirinkimas**: Pasirinkite **Claude 3.5 Sonnet** (puikiai tinka kodui)

2. **Sistemos užklausos dizainas**:
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

3. **Parametrų konfigūravimas**:
   - Temperature: 0.2 (nuosekliam, patikimam kodui)
   - Max Tokens: 2000 (išsamūs paaiškinimai)
   - Top-p: 0.9 (subalansuotas kūrybiškumas)

![Python Agent Configuration](../../../../translated_images/pythonagent.5e51b406401c165fcabfd66f2d943c27f46b5fed0f9fb73abefc9e91ca3489d4.lt.png)

### 🧪 4 žingsnis: Testuokite savo Python agentą

**Testavimo scenarijai:**
1. **Paprasta funkcija**: „Sukurkite funkciją pirminių skaičių radimui“
2. **Sudėtingas algoritmas**: „Įgyvendinkite dvejetainį paieškos medį su įterpimo, ištrynimo ir paieškos metodais“
3. **Reali problema**: „Sukurkite tinklalapio duomenų rinkiklį, kuris tvarkytų užklausų limitus ir pakartotinius bandymus“
4. **Derinimas**: „Pataisykite šį kodą [įklijuokite klaidingą kodą]“

**🏆 Sėkmės kriterijai:**
- ✅ Kodas veikia be klaidų
- ✅ Yra tinkama dokumentacija
- ✅ Laikosi Python geriausių praktikų
- ✅ Pateikia aiškius paaiškinimus
- ✅ Siūlo patobulinimus

## 🎓 Modulio 1 apibendrinimas ir tolesni žingsniai

### 📊 Žinių patikrinimas

Patikrinkite savo supratimą:
- [ ] Ar galite paaiškinti skirtumą tarp modelių kataloge?
- [ ] Ar sėkmingai sukūrėte ir išbandėte individualų agentą?
- [ ] Ar suprantate, kaip optimizuoti parametrus skirtingiems atvejams?
- [ ] Ar galite sukurti efektyvias sistemines užklausas?

### 📚 Papildomi ištekliai

- **AI Toolkit dokumentacija**: [Oficialūs Microsoft dokumentai](https://github.com/microsoft/vscode-ai-toolkit)
- **Užklausų kūrimo vadovas**: [Geriausios praktikos](https://platform.openai.com/docs/guides/prompt-engineering)
- **Modeliai AI Toolkit**: [Modeliai kūrime](https://github.com/microsoft/vscode-ai-toolkit/blob/main/doc/models.md)

**🎉 Sveikiname!** Jūs įvaldėte AI Toolkit pagrindus ir esate pasiruošę kurti sudėtingesnes AI programas!

### 🔜 Tęskite kitą modulį

Pasiruošę pažengusioms galimybėms? Tęskite **[Modulis 2: MCP su AI Toolkit pagrindai](../lab2/README.md)**, kur išmoksite:
- Prijungti savo agentus prie išorinių įrankių naudojant Model Context Protocol (MCP)
- Kurti naršyklės automatizavimo agentus su Playwright
- Integruoti MCP serverius su savo AI Toolkit agentais
- Sustiprinti savo agentus išoriniais duomenimis ir galimybėmis

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.