# 🚀 Modul 1: Grunnleggende om AI Toolkit

[![Varighet](https://img.shields.io/badge/Duration-15%20minutes-blue.svg)]()
[![Vanskelighetsgrad](https://img.shields.io/badge/Difficulty-Beginner-green.svg)]()
[![Forutsetninger](https://img.shields.io/badge/Prerequisites-VS%20Code-orange.svg)]()

## 📋 Læringsmål

Etter denne modulen vil du kunne:
- ✅ Installere og konfigurere AI Toolkit for Visual Studio Code
- ✅ Navigere i Model Catalog og forstå ulike modellkilder
- ✅ Bruke Playground for modelltesting og eksperimentering
- ✅ Lage tilpassede AI-agenter med Agent Builder
- ✅ Sammenligne modellprestasjoner på tvers av leverandører
- ✅ Anvende beste praksis for prompt engineering

## 🧠 Introduksjon til AI Toolkit (AITK)

**AI Toolkit for Visual Studio Code** er Microsofts flaggskip-utvidelse som forvandler VS Code til et komplett AI-utviklingsmiljø. Den bygger bro mellom AI-forskning og praktisk applikasjonsutvikling, og gjør generativ AI tilgjengelig for utviklere på alle ferdighetsnivåer.

### 🌟 Nøkkelfunksjoner

| Funksjon | Beskrivelse | Bruksområde |
|---------|-------------|-------------|
| **🗂️ Model Catalog** | Tilgang til 100+ modeller fra GitHub, ONNX, OpenAI, Anthropic, Google | Modellutforskning og valg |
| **🔌 BYOM Support** | Integrer dine egne modeller (lokalt/fjernt) | Tilpasset modellutrulling |
| **🎮 Interaktiv Playground** | Sanntidstesting av modeller med chat-grensesnitt | Rask prototyping og testing |
| **📎 Multi-modalt støtte** | Håndter tekst, bilder og vedlegg | Komplekse AI-applikasjoner |
| **⚡ Batchbehandling** | Kjør flere prompts samtidig | Effektive testarbeidsflyter |
| **📊 Modellevaluering** | Innebygde måleparametere (F1, relevans, likhet, sammenheng) | Vurdering av ytelse |

### 🎯 Hvorfor AI Toolkit er viktig

- **🚀 Raskere utvikling**: Fra idé til prototype på minutter
- **🔄 Enhetlig arbeidsflyt**: Én plattform for flere AI-leverandører
- **🧪 Enkel eksperimentering**: Sammenlign modeller uten komplisert oppsett
- **📈 Klar for produksjon**: Sømløs overgang fra prototype til utrulling

## 🛠️ Forutsetninger og oppsett

### 📦 Installer AI Toolkit-utvidelsen

**Steg 1: Åpne Extensions Marketplace**
1. Åpne Visual Studio Code
2. Gå til Extensions-visningen (`Ctrl+Shift+X` eller `Cmd+Shift+X`)
3. Søk etter "AI Toolkit"

**Steg 2: Velg versjon**
- **🟢 Release**: Anbefalt for produksjonsbruk
- **🔶 Pre-release**: Tidlig tilgang til nye funksjoner

**Steg 3: Installer og aktiver**

![AI Toolkit Extension](../../../../translated_images/no/aitkext.d28945a03eed003c39fc39bc96ae655af9b64b9b922e78e88b07214420ed7985.png)

### ✅ Sjekkliste for verifisering
- [ ] AI Toolkit-ikon vises i VS Code-sidepanelet
- [ ] Utvidelsen er aktivert og i bruk
- [ ] Ingen installasjonsfeil i output-panelet

## 🧪 Praktisk øvelse 1: Utforske GitHub-modeller

**🎯 Mål**: Bli kjent med Model Catalog og test din første AI-modell

### 📊 Steg 1: Naviger i Model Catalog

Model Catalog er inngangsporten til AI-økosystemet. Den samler modeller fra flere leverandører, noe som gjør det enkelt å oppdage og sammenligne alternativer.

**🔍 Navigasjonsveiledning:**

Klikk på **MODELS - Catalog** i AI Toolkit-sidepanelet

![Model Catalog](../../../../translated_images/no/aimodel.263ed2be013d8fb0e2265c4f742cfe490f6f00eca5e132ec50438c8e826e34ed.png)

**💡 Profftips**: Se etter modeller med spesifikke egenskaper som passer ditt brukstilfelle (f.eks. kodegenerering, kreativ skriving, analyse).

**⚠️ Merk**: GitHub-hostede modeller (dvs. GitHub Models) er gratis å bruke, men har begrensninger på antall forespørsler og tokens. For å få tilgang til ikke-GitHub-modeller (eksterne modeller via Azure AI eller andre endepunkter) må du oppgi riktig API-nøkkel eller autentisering.

### 🚀 Steg 2: Legg til og konfigurer din første modell

**Modellvalgstrategi:**
- **GPT-4.1**: Best for komplekse resonnementer og analyser
- **Phi-4-mini**: Lettvekter, raske svar for enkle oppgaver

**🔧 Konfigurasjonsprosess:**
1. Velg **OpenAI GPT-4.1** fra katalogen
2. Klikk **Add to My Models** – dette registrerer modellen for bruk
3. Velg **Try in Playground** for å åpne testmiljøet
4. Vent på at modellen initialiseres (første oppstart kan ta litt tid)

![Playground Setup](../../../../translated_images/no/playground.dd6f5141344878ca4d4f3de819775da7b113518941accf37c291117c602f85db.png)

**⚙️ Forstå modellparametere:**
- **Temperature**: Styrer kreativitet (0 = deterministisk, 1 = kreativ)
- **Max Tokens**: Maksimal lengde på svar
- **Top-p**: Nucleus sampling for variasjon i svar

### 🎯 Steg 3: Mestre Playground-grensesnittet

Playground er ditt AI-eksperimentlaboratorium. Slik får du mest ut av det:

**🎨 Beste praksis for prompt engineering:**
1. **Vær spesifikk**: Klare, detaljerte instruksjoner gir bedre resultater
2. **Gi kontekst**: Inkluder relevant bakgrunnsinformasjon
3. **Bruk eksempler**: Vis modellen hva du ønsker med eksempler
4. **Iterer**: Forbedre prompts basert på tidlige resultater

**🧪 Testscenarier:**
```markdown
# Example 1: Code Generation
"Write a Python function that calculates the factorial of a number using recursion. Include error handling and docstrings."

# Example 2: Creative Writing
"Write a professional email to a client explaining a project delay, maintaining a positive tone while being transparent about challenges."

# Example 3: Data Analysis
"Analyze this sales data and provide insights: [paste your data]. Focus on trends, anomalies, and actionable recommendations."
```

![Testing Results](../../../../translated_images/no/result.1dfcf211fb359cf65902b09db191d3bfc65713ca15e279c1a30be213bb526949.png)

### 🏆 Utfordringsøvelse: Sammenligning av modellprestasjoner

**🎯 Mål**: Sammenlign ulike modeller med identiske prompts for å forstå styrkene deres

**📋 Instruksjoner:**
1. Legg til **Phi-4-mini** i arbeidsområdet ditt
2. Bruk samme prompt for både GPT-4.1 og Phi-4-mini

![set](../../../../translated_images/no/set.88132df189ecde2cbbda256c1841db5aac8e9bdeba1a4e343dfa031b9545d6c9.png)

3. Sammenlign svarenes kvalitet, hastighet og nøyaktighet
4. Dokumenter funnene dine i resultatdelen

![Model Comparison](../../../../translated_images/no/compare.97746cd0f907495503c1fc217739f3890dc76ea5f6fd92379a6db0cc331feb58.png)

**💡 Viktige innsikter å oppdage:**
- Når bør man bruke LLM vs SLM
- Kostnad vs ytelse
- Spesialiserte egenskaper ved ulike modeller

## 🤖 Praktisk øvelse 2: Bygge tilpassede agenter med Agent Builder

**🎯 Mål**: Lag spesialiserte AI-agenter tilpasset bestemte oppgaver og arbeidsflyter

### 🏗️ Steg 1: Forstå Agent Builder

Agent Builder er der AI Toolkit virkelig skinner. Her kan du lage skreddersydde AI-assistenter som kombinerer kraften i store språkmodeller med tilpassede instruksjoner, spesifikke parametere og spesialisert kunnskap.

**🧠 Komponenter i agentarkitekturen:**
- **Kjernemodell**: Grunnleggende LLM (GPT-4, Groks, Phi, osv.)
- **Systemprompt**: Definerer agentens personlighet og oppførsel
- **Parametere**: Fininnstilte innstillinger for optimal ytelse
- **Verktøyintegrasjon**: Koble til eksterne API-er og MCP-tjenester
- **Minne**: Samtalekontekst og sesjonspersistens

![Agent Builder Interface](../../../../translated_images/no/agentbuilder.25895b2d2f8c02e7aa99dd40e105877a6f1db8f0441180087e39db67744b361f.png)

### ⚙️ Steg 2: Dypdykk i agentkonfigurasjon

**🎨 Lage effektive systemprompter:**
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

*Selvfølgelig kan du også bruke Generate System Prompt for å la AI hjelpe deg med å lage og optimalisere prompter*

**🔧 Parameteroptimalisering:**
| Parameter | Anbefalt område | Bruksområde |
|-----------|-----------------|-------------|
| **Temperature** | 0.1-0.3 | Tekniske/faktabaserte svar |
| **Temperature** | 0.7-0.9 | Kreative/idémyldringsoppgaver |
| **Max Tokens** | 500-1000 | Konsise svar |
| **Max Tokens** | 2000-4000 | Detaljerte forklaringer |

### 🐍 Steg 3: Praktisk øvelse – Python-programmeringsagent

**🎯 Oppdrag**: Lag en spesialisert assistent for Python-koding

**📋 Konfigurasjonstrinn:**

1. **Modellvalg**: Velg **Claude 3.5 Sonnet** (utmerket for kode)

2. **Systempromptdesign**:
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

3. **Parameterkonfigurasjon**:
   - Temperature: 0.2 (for konsistent, pålitelig kode)
   - Max Tokens: 2000 (detaljerte forklaringer)
   - Top-p: 0.9 (balansert kreativitet)

![Python Agent Configuration](../../../../translated_images/no/pythonagent.5e51b406401c165fcabfd66f2d943c27f46b5fed0f9fb73abefc9e91ca3489d4.png)

### 🧪 Steg 4: Test din Python-agent

**Testscenarier:**
1. **Grunnleggende funksjon**: "Lag en funksjon for å finne primtall"
2. **Kompleks algoritme**: "Implementer et binært søketre med innsetting, sletting og søk"
3. **Virkelighetsproblem**: "Lag en webskraper som håndterer rate limiting og retry"
4. **Feilsøking**: "Fiks denne koden [lim inn buggy kode]"

**🏆 Suksesskriterier:**
- ✅ Koden kjører uten feil
- ✅ Inkluderer god dokumentasjon
- ✅ Følger beste praksis for Python
- ✅ Gir klare forklaringer
- ✅ Foreslår forbedringer

## 🎓 Modul 1 Oppsummering og neste steg

### 📊 Kunnskapssjekk

Test din forståelse:
- [ ] Kan du forklare forskjellen mellom modellene i katalogen?
- [ ] Har du laget og testet en tilpasset agent?
- [ ] Forstår du hvordan du optimaliserer parametere for ulike bruksområder?
- [ ] Kan du lage effektive systemprompter?

### 📚 Ekstra ressurser

- **AI Toolkit Dokumentasjon**: [Official Microsoft Docs](https://github.com/microsoft/vscode-ai-toolkit)
- **Guide til prompt engineering**: [Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- **Modeller i AI Toolkit**: [Models in Development](https://github.com/microsoft/vscode-ai-toolkit/blob/main/doc/models.md)

**🎉 Gratulerer!** Du har mestret det grunnleggende i AI Toolkit og er klar for å bygge mer avanserte AI-applikasjoner!

### 🔜 Fortsett til neste modul

Klar for mer avanserte funksjoner? Fortsett til **[Modul 2: MCP med AI Toolkit Fundamentals](../lab2/README.md)** hvor du vil lære å:
- Koble agentene dine til eksterne verktøy med Model Context Protocol (MCP)
- Bygge nettleserautomatiseringsagenter med Playwright
- Integrere MCP-servere med AI Toolkit-agentene dine
- Gi agentene dine ekstra kraft med ekstern data og funksjonalitet

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.