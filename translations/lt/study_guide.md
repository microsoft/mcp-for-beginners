<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2c6ed897fa98fa08e0146101776c7ff",
  "translation_date": "2025-08-26T16:03:42+00:00",
  "source_file": "study_guide.md",
  "language_code": "lt"
}
-->
# Modelio Konteksto Protokolas (MCP) pradedantiesiems – Mokymosi vadovas

Šis mokymosi vadovas pateikia apžvalgą apie saugyklos struktūrą ir turinį, skirtą „Modelio Konteksto Protokolas (MCP) pradedantiesiems“ mokymo programai. Naudokite šį vadovą, kad efektyviai naršytumėte saugyklą ir maksimaliai išnaudotumėte turimus išteklius.

## Saugyklos apžvalga

Modelio Konteksto Protokolas (MCP) yra standartizuota sistema, skirta sąveikai tarp dirbtinio intelekto modelių ir klientų programų. Iš pradžių sukurtas „Anthropic“, MCP dabar prižiūri platesnė MCP bendruomenė per oficialią „GitHub“ organizaciją. Ši saugykla siūlo išsamią mokymo programą su praktiniais kodo pavyzdžiais C#, Java, JavaScript, Python ir TypeScript kalbomis, skirtą DI kūrėjams, sistemų architektams ir programinės įrangos inžinieriams.

## Vizualus mokymo programos žemėlapis

```mermaid
mindmap
  root((MCP for Beginners))
    00. Introduction
      ::icon(fa fa-book)
      (Protocol Overview)
      (Standardization Benefits)
      (Real-world Use Cases)
      (AI Integration Fundamentals)
    01. Core Concepts
      ::icon(fa fa-puzzle-piece)
      (Client-Server Architecture)
      (Protocol Components)
      (Messaging Patterns)
      (Transport Mechanisms)
    02. Security
      ::icon(fa fa-shield)
      (AI-Specific Threats)
      (Best Practices 2025)
      (Azure Content Safety)
      (Auth & Authorization)
      (Microsoft Prompt Shields)
    03. Getting Started
      ::icon(fa fa-rocket)
      (First Server Implementation)
      (Client Development)
      (LLM Client Integration)
      (VS Code Extensions)
      (SSE Server Setup)
      (HTTP Streaming)
      (AI Toolkit Integration)
      (Testing Frameworks)
      (Deployment Strategies)
    04. Practical Implementation
      ::icon(fa fa-code)
      (Multi-Language SDKs)
      (Testing & Debugging)
      (Prompt Templates)
      (Sample Projects)
      (Production Patterns)
    05. Advanced Topics
      ::icon(fa fa-graduation-cap)
      (Context Engineering)
      (Foundry Agent Integration)
      (Multi-modal AI Workflows)
      (OAuth2 Authentication)
      (Real-time Search)
      (Streaming Protocols)
      (Root Contexts)
      (Routing Strategies)
      (Sampling Techniques)
      (Scaling Solutions)
      (Security Hardening)
      (Entra ID Integration)
      (Web Search MCP)
      
    06. Community
      ::icon(fa fa-users)
      (Code Contributions)
      (Documentation)
      (MCP Client Ecosystem)
      (MCP Server Registry)
      (Image Generation Tools)
      (GitHub Collaboration)
    07. Early Adoption
      ::icon(fa fa-lightbulb)
      (Production Deployments)
      (Microsoft MCP Servers)
      (Azure MCP Service)
      (Enterprise Case Studies)
      (Future Roadmap)
    08. Best Practices
      ::icon(fa fa-check)
      (Performance Optimization)
      (Fault Tolerance)
      (System Resilience)
      (Monitoring & Observability)
    09. Case Studies
      ::icon(fa fa-file-text)
      (Azure API Management)
      (AI Travel Agent)
      (Azure DevOps Integration)
      (Documentation MCP)
      (Real-world Implementations)
    10. Hands-on Workshop
      ::icon(fa fa-laptop)
      (MCP Server Fundamentals)
      (Advanced Development)
      (AI Toolkit Integration)
      (Production Deployment)
      (4-Lab Structure)
```

## Saugyklos struktūra

Saugykla suskirstyta į dešimt pagrindinių skyrių, kurių kiekvienas orientuotas į skirtingus MCP aspektus:

1. **Įvadas (00-Introduction/)**
   - Modelio Konteksto Protokolo apžvalga
   - Kodėl standartizacija svarbi DI procesuose
   - Praktiniai naudojimo atvejai ir nauda

2. **Pagrindinės sąvokos (01-CoreConcepts/)**
   - Kliento-serverio architektūra
   - Pagrindiniai protokolo komponentai
   - Žinučių perdavimo modeliai MCP

3. **Saugumas (02-Security/)**
   - Saugumo grėsmės MCP pagrįstose sistemose
   - Geriausios praktikos saugiam įgyvendinimui
   - Autentifikavimo ir autorizacijos strategijos
   - **Išsamūs saugumo dokumentai**:
     - MCP saugumo geriausios praktikos 2025
     - Azure turinio saugumo įgyvendinimo vadovas
     - MCP saugumo kontrolės ir technikos
     - MCP greitosios nuorodos geriausios praktikos
   - **Pagrindinės saugumo temos**:
     - Užklausų injekcijos ir įrankių užnuodijimo atakos
     - Sesijos užgrobimas ir „suklaidinto pavaduotojo“ problemos
     - Žetonų perdavimo pažeidžiamumai
     - Perteklinės teisės ir prieigos kontrolė
     - Tiekimo grandinės saugumas DI komponentams
     - Microsoft Prompt Shields integracija

4. **Pradžia (03-GettingStarted/)**
   - Aplinkos nustatymas ir konfigūravimas
   - Pagrindinių MCP serverių ir klientų kūrimas
   - Integracija su esamomis programomis
   - Apima skyrius apie:
     - Pirmojo serverio įgyvendinimą
     - Kliento kūrimą
     - LLM kliento integraciją
     - VS Code integraciją
     - Serverio siunčiamų įvykių (SSE) serverį
     - HTTP srautą
     - DI įrankių rinkinio integraciją
     - Testavimo strategijas
     - Diegimo gaires

5. **Praktinis įgyvendinimas (04-PracticalImplementation/)**
   - SDK naudojimas skirtingomis programavimo kalbomis
   - Derinimo, testavimo ir patvirtinimo technikos
   - Pakartotinai naudojamų užklausų šablonų ir darbo eigų kūrimas
   - Pavyzdiniai projektai su įgyvendinimo pavyzdžiais

6. **Pažangios temos (05-AdvancedTopics/)**
   - Konteksto inžinerijos technikos
   - Foundry agento integracija
   - Daugiarūšiai DI darbo srautai
   - OAuth2 autentifikavimo demonstracijos
   - Realaus laiko paieškos galimybės
   - Realaus laiko srautas
   - Pagrindinių kontekstų įgyvendinimas
   - Maršruto strategijos
   - Mėginių ėmimo technikos
   - Skalavimo metodai
   - Saugumo aspektai
   - Entra ID saugumo integracija
   - Interneto paieškos integracija

7. **Bendruomenės indėlis (06-CommunityContributions/)**
   - Kaip prisidėti prie kodo ir dokumentacijos
   - Bendradarbiavimas per „GitHub“
   - Bendruomenės siūlomi patobulinimai ir atsiliepimai
   - Naudojimasis įvairiais MCP klientais (Claude Desktop, Cline, VSCode)
   - Darbas su populiariais MCP serveriais, įskaitant vaizdų generavimą

8. **Pamokos iš ankstyvojo pritaikymo (07-LessonsfromEarlyAdoption/)**
   - Realūs įgyvendinimai ir sėkmės istorijos
   - MCP pagrįstų sprendimų kūrimas ir diegimas
   - Tendencijos ir ateities planai
   - **Microsoft MCP serverių vadovas**: Išsamus vadovas apie 10 gamybai paruoštų Microsoft MCP serverių, įskaitant:
     - Microsoft Learn Docs MCP serverį
     - Azure MCP serverį (15+ specializuotų jungčių)
     - GitHub MCP serverį
     - Azure DevOps MCP serverį
     - MarkItDown MCP serverį
     - SQL Server MCP serverį
     - Playwright MCP serverį
     - Dev Box MCP serverį
     - Azure AI Foundry MCP serverį
     - Microsoft 365 Agents Toolkit MCP serverį

9. **Geriausios praktikos (08-BestPractices/)**
   - Našumo optimizavimas
   - Atsparių MCP sistemų kūrimas
   - Testavimo ir atsparumo strategijos

10. **Atvejų analizės (09-CaseStudy/)**
    - Azure API valdymo integracijos pavyzdys
    - Kelionių agento įgyvendinimo pavyzdys
    - Azure DevOps integracija su „YouTube“ atnaujinimais
    - Dokumentacijos MCP įgyvendinimo pavyzdžiai
    - Įgyvendinimo pavyzdžiai su išsamia dokumentacija

11. **Praktinis seminaras (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - Išsamus praktinis seminaras, jungiantis MCP su DI įrankių rinkiniu
    - Intelektualių programų kūrimas, jungiant DI modelius su realaus pasaulio įrankiais
    - Praktiniai moduliai, apimantys pagrindus, individualų serverio kūrimą ir diegimo strategijas
    - **Laboratorijos struktūra**:
      - Laboratorija 1: MCP serverio pagrindai
      - Laboratorija 2: Pažangus MCP serverio kūrimas
      - Laboratorija 3: DI įrankių rinkinio integracija
      - Laboratorija 4: Diegimas ir skalavimas
    - Mokymasis laboratorijose su žingsnis po žingsnio instrukcijomis

## Papildomi ištekliai

Saugykla apima papildomus išteklius:

- **Vaizdų aplankas**: Diagramos ir iliustracijos, naudojamos visoje mokymo programoje
- **Vertimai**: Daugiakalbė parama su automatizuotais dokumentacijos vertimais
- **Oficialūs MCP ištekliai**:
  - [MCP dokumentacija](https://modelcontextprotocol.io/)
  - [MCP specifikacija](https://spec.modelcontextprotocol.io/)
  - [MCP GitHub saugykla](https://github.com/modelcontextprotocol)

## Kaip naudotis šia saugykla

1. **Nuoseklus mokymasis**: Sekite skyrius iš eilės (00–10), kad gautumėte struktūruotą mokymosi patirtį.
2. **Kalbai specifinis dėmesys**: Jei jus domina tam tikra programavimo kalba, tyrinėkite pavyzdžių aplankus, skirtus jūsų pageidaujamai kalbai.
3. **Praktinis įgyvendinimas**: Pradėkite nuo „Pradžia“ skyriaus, kad nustatytumėte aplinką ir sukurtumėte pirmąjį MCP serverį bei klientą.
4. **Pažangus tyrinėjimas**: Kai įsisavinsite pagrindus, gilinkitės į pažangias temas, kad praplėstumėte žinias.
5. **Bendruomenės įsitraukimas**: Prisijunkite prie MCP bendruomenės per „GitHub“ diskusijas ir „Discord“ kanalus, kad susisiektumėte su ekspertais ir kitais kūrėjais.

## MCP klientai ir įrankiai

Mokymo programa apima įvairius MCP klientus ir įrankius:

1. **Oficialūs klientai**:
   - Visual Studio Code 
   - MCP Visual Studio Code aplinkoje
   - Claude Desktop
   - Claude VSCode aplinkoje
   - Claude API

2. **Bendruomenės klientai**:
   - Cline (terminalo pagrindu)
   - Cursor (kodo redaktorius)
   - ChatMCP
   - Windsurf

3. **MCP valdymo įrankiai**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## Populiarūs MCP serveriai

Saugykla pristato įvairius MCP serverius, įskaitant:

1. **Oficialūs Microsoft MCP serveriai**:
   - Microsoft Learn Docs MCP serveris
   - Azure MCP serveris (15+ specializuotų jungčių)
   - GitHub MCP serveris
   - Azure DevOps MCP serveris
   - MarkItDown MCP serveris
   - SQL Server MCP serveris
   - Playwright MCP serveris
   - Dev Box MCP serveris
   - Azure AI Foundry MCP serveris
   - Microsoft 365 Agents Toolkit MCP serveris

2. **Oficialūs pavyzdiniai serveriai**:
   - Failų sistema
   - Fetch
   - Atmintis
   - Sekvencinis mąstymas

3. **Vaizdų generavimas**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **Kūrimo įrankiai**:
   - Git MCP
   - Terminalo valdymas
   - Kodo asistentas

5. **Specializuoti serveriai**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## Prisidėjimas

Ši saugykla laukia bendruomenės indėlio. Žr. skyrių „Bendruomenės indėlis“, kad sužinotumėte, kaip efektyviai prisidėti prie MCP ekosistemos.

## Pakeitimų žurnalas

| Data | Pakeitimai |
|------|-----------|
| 2025 m. liepos 18 d. | - Atnaujinta saugyklos struktūra, įtraukiant Microsoft MCP serverių vadovą<br>- Pridėtas išsamus 10 gamybai paruoštų Microsoft MCP serverių sąrašas<br>- Patobulintas Populiarių MCP serverių skyrius su oficialiais Microsoft MCP serveriais<br>- Atnaujintas Atvejų analizės skyrius su faktiniais failų pavyzdžiais<br>- Pridėta Laboratorijos struktūros detalės praktiniam seminarui |
| 2025 m. liepos 16 d. | - Atnaujinta saugyklos struktūra, atspindinti dabartinį turinį<br>- Pridėtas MCP klientų ir įrankių skyrius<br>- Pridėtas Populiarių MCP serverių skyrius<br>- Atnaujintas Vizualus mokymo programos žemėlapis su visomis dabartinėmis temomis<br>- Patobulintas Pažangių temų skyrius su visomis specializuotomis sritimis<br>- Atnaujintos Atvejų analizės su faktiniais pavyzdžiais<br>- Paaiškinta MCP kilmė kaip sukurta „Anthropic“ |
| 2025 m. birželio 11 d. | - Sukurtas pradinis mokymosi vadovas<br>- Pridėtas Vizualus mokymo programos žemėlapis<br>- Apibrėžta saugyklos struktūra<br>- Įtraukti pavyzdiniai projektai ir papildomi ištekliai |

---

*Šis mokymosi vadovas buvo atnaujintas 2025 m. liepos 18 d. ir pateikia saugyklos apžvalgą pagal tą datą. Saugyklos turinys gali būti atnaujintas po šios datos.*

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.