<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0df1ee78a6dd8300f3a040ca5b411c2e",
  "translation_date": "2025-08-26T16:59:07+00:00",
  "source_file": "00-Introduction/README.md",
  "language_code": "lt"
}
-->
# Įvadas į Model Context Protocol (MCP): Kodėl tai svarbu kuriant mastelio AI programas

[![Įvadas į Model Context Protocol](../../../translated_images/01.a467036d886b5fb5b9cf7b39bac0e743b6ca0a4a18a492de90061daaf0cc55f0.lt.png)](https://youtu.be/agBbdiOPLQA)

_(Spustelėkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

Generatyviosios AI programos yra didelis žingsnis į priekį, nes jos dažnai leidžia vartotojui bendrauti su programa naudojant natūralios kalbos užklausas. Tačiau, kai į tokias programas investuojama daugiau laiko ir išteklių, norisi užtikrinti, kad funkcionalumai ir ištekliai būtų lengvai integruojami, kad būtų paprasta plėsti programą, ji galėtų dirbti su daugiau nei vienu modeliu ir tvarkytų įvairias modelių subtilybes. Trumpai tariant, generatyviosios AI programos kūrimas yra lengvas pradžioje, tačiau, kai jos auga ir tampa sudėtingesnės, reikia pradėti apibrėžti architektūrą ir greičiausiai remtis standartu, kad programos būtų kuriamos nuosekliai. Čia į pagalbą ateina MCP, kuris padeda organizuoti procesus ir suteikia standartą.

---

## **🔍 Kas yra Model Context Protocol (MCP)?**

**Model Context Protocol (MCP)** yra **atviras, standartizuotas sąsajos protokolas**, leidžiantis dideliems kalbos modeliams (LLM) sklandžiai sąveikauti su išoriniais įrankiais, API ir duomenų šaltiniais. Jis suteikia nuoseklią architektūrą, kuri pagerina AI modelių funkcionalumą už jų mokymo duomenų ribų, leidžiant kurti išmanesnes, mastelio ir jautresnes AI sistemas.

---

## **🎯 Kodėl AI standartizacija yra svarbi**

Kai generatyviosios AI programos tampa sudėtingesnės, būtina priimti standartus, kurie užtikrintų **mastelį, plėtrumą, palaikomumą** ir **išvengtų priklausomybės nuo vieno tiekėjo**. MCP sprendžia šiuos poreikius:

- Suvienodindamas modelių ir įrankių integracijas
- Sumažindamas trapias, vienkartines pritaikytas sprendimų sistemas
- Leidžiant vienoje ekosistemoje egzistuoti keliems modeliams iš skirtingų tiekėjų

**Pastaba:** Nors MCP save pristato kaip atvirą standartą, nėra planų MCP standartizuoti per esamas standartų organizacijas, tokias kaip IEEE, IETF, W3C, ISO ar kitas.

---

## **📚 Mokymosi tikslai**

Šio straipsnio pabaigoje galėsite:

- Apibrėžti **Model Context Protocol (MCP)** ir jo naudojimo atvejus
- Suprasti, kaip MCP standartizuoja modelio ir įrankių komunikaciją
- Atpažinti pagrindinius MCP architektūros komponentus
- Išnagrinėti realaus pasaulio MCP taikymo pavyzdžius įmonių ir kūrimo kontekstuose

---

## **💡 Kodėl Model Context Protocol (MCP) yra proveržis**

### **🔗 MCP sprendžia AI sąveikų fragmentaciją**

Prieš MCP, modelių integravimas su įrankiais reikalavo:

- Individualaus kodo kiekvienai įrankio ir modelio porai
- Nestandartinių API kiekvienam tiekėjui
- Dažnų gedimų dėl atnaujinimų
- Prasto mastelio didėjant įrankių skaičiui

### **✅ MCP standartizacijos privalumai**

| **Privalumas**             | **Aprašymas**                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Sąveikumas                | LLM sklandžiai dirba su įrankiais iš skirtingų tiekėjų                      |
| Nuoseklumas               | Vienodas elgesys visose platformose ir įrankiuose                           |
| Pakartotinis naudojimas   | Vieną kartą sukurti įrankiai gali būti naudojami įvairiuose projektuose      |
| Spartesnis kūrimas        | Sutrumpėja kūrimo laikas naudojant standartizuotas, lengvai pritaikomas sąsajas |

---

## **🧱 Aukšto lygio MCP architektūros apžvalga**

MCP naudoja **kliento-serverio modelį**, kuriame:

- **MCP Hostai** vykdo AI modelius
- **MCP Klientai** inicijuoja užklausas
- **MCP Serveriai** teikia kontekstą, įrankius ir galimybes

### **Pagrindiniai komponentai:**

- **Ištekliai** – Statiniai arba dinaminiai duomenys modeliams  
- **Užklausos** – Iš anksto apibrėžti darbo srautai generavimui nukreipti  
- **Įrankiai** – Vykdomos funkcijos, tokios kaip paieška, skaičiavimai  
- **Mėginių ėmimas** – Agentinis elgesys per rekursines sąveikas  

---

## Kaip veikia MCP serveriai

MCP serveriai veikia taip:

- **Užklausų srautas**:
    1. Užklausą inicijuoja galutinis vartotojas arba programinė įranga, veikianti jo vardu.
    2. **MCP Klientas** siunčia užklausą **MCP Hostui**, kuris valdo AI modelio vykdymo aplinką.
    3. **AI Modelis** gauna vartotojo užklausą ir gali prašyti prieigos prie išorinių įrankių ar duomenų per vieną ar kelis įrankių iškvietimus.
    4. **MCP Hostas**, o ne pats modelis, bendrauja su atitinkamais **MCP Serveriais** naudodamas standartizuotą protokolą.
- **MCP Hosto funkcionalumas**:
    - **Įrankių registras**: Tvarko galimų įrankių ir jų galimybių katalogą.
    - **Autentifikacija**: Tikrina leidimus naudotis įrankiais.
    - **Užklausų tvarkytojas**: Apdoroja gaunamas modelio įrankių užklausas.
    - **Atsakymų formuotojas**: Struktūrizuoja įrankių išvestį formatu, kurį modelis gali suprasti.
- **MCP Serverio vykdymas**:
    - **MCP Hostas** nukreipia įrankių užklausas į vieną ar kelis **MCP Serverius**, kurie teikia specializuotas funkcijas (pvz., paieška, skaičiavimai, duomenų bazės užklausos).
    - **MCP Serveriai** atlieka savo operacijas ir grąžina rezultatus **MCP Hostui** nuosekliu formatu.
    - **MCP Hostas** formatuoja ir perduoda šiuos rezultatus **AI Modeliui**.
- **Atsakymo užbaigimas**:
    - **AI Modelis** įtraukia įrankių išvestį į galutinį atsakymą.
    - **MCP Hostas** siunčia šį atsakymą atgal **MCP Klientui**, kuris jį pateikia galutiniam vartotojui arba kviečiančiai programinei įrangai.

```mermaid
---
title: MCP Architecture and Component Interactions
description: A diagram showing the flows of the components in MCP.
---
graph TD
    Client[MCP Client/Application] -->|Sends Request| H[MCP Host]
    H -->|Invokes| A[AI Model]
    A -->|Tool Call Request| H
    H -->|MCP Protocol| T1[MCP Server Tool 01: Web Search]
    H -->|MCP Protocol| T2[MCP Server Tool 02: Calculator tool]
    H -->|MCP Protocol| T3[MCP Server Tool 03: Database Access tool]
    H -->|MCP Protocol| T4[MCP Server Tool 04: File System tool]
    H -->|Sends Response| Client

    subgraph "MCP Host Components"
        H
        G[Tool Registry]
        I[Authentication]
        J[Request Handler]
        K[Response Formatter]
    end

    H <--> G
    H <--> I
    H <--> J
    H <--> K

    style A fill:#f9d5e5,stroke:#333,stroke-width:2px
    style H fill:#eeeeee,stroke:#333,stroke-width:2px
    style Client fill:#d5e8f9,stroke:#333,stroke-width:2px
    style G fill:#fffbe6,stroke:#333,stroke-width:1px
    style I fill:#fffbe6,stroke:#333,stroke-width:1px
    style J fill:#fffbe6,stroke:#333,stroke-width:1px
    style K fill:#fffbe6,stroke:#333,stroke-width:1px
    style T1 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T2 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T3 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T4 fill:#c2f0c2,stroke:#333,stroke-width:1px
```

## 👨‍💻 Kaip sukurti MCP serverį (su pavyzdžiais)

MCP serveriai leidžia išplėsti LLM galimybes, teikiant duomenis ir funkcionalumą.

Pasiruošę išbandyti? Štai kalbų ir/arba technologijų rinkiniai su pavyzdžiais, kaip sukurti paprastus MCP serverius skirtingomis kalbomis/technologijomis:

- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk

- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk

- **Java SDK**: https://github.com/modelcontextprotocol/java-sdk

- **C#/.NET SDK**: https://github.com/modelcontextprotocol/csharp-sdk

---

## 🌍 Realūs MCP naudojimo atvejai

MCP leidžia platų programų spektrą, išplečiant AI galimybes:

| **Programa**                | **Aprašymas**                                                                 |
|-----------------------------|------------------------------------------------------------------------------|
| Įmonių duomenų integracija  | Sujunkite LLM su duomenų bazėmis, CRM ar vidiniais įrankiais                 |
| Agentinės AI sistemos       | Leiskite autonominiams agentams naudotis įrankiais ir sprendimų priėmimo srautais |
| Daugiarūšės programos       | Sujunkite tekstą, vaizdus ir garsą vienoje AI programoje                     |
| Realaus laiko duomenų integracija | Įtraukite tiesioginius duomenis į AI sąveikas, kad gautumėte tikslesnius rezultatus |

### 🧠 MCP = Universalus AI sąveikų standartas

Model Context Protocol (MCP) veikia kaip universalus AI sąveikų standartas, panašiai kaip USB-C standartizavo fizinius įrenginių jungimus. AI pasaulyje MCP suteikia nuoseklią sąsają, leidžiančią modeliams (klientams) sklandžiai integruotis su išoriniais įrankiais ir duomenų teikėjais (serveriais). Tai pašalina poreikį kurti įvairius, pritaikytus protokolus kiekvienai API ar duomenų šaltiniui.

Pagal MCP, MCP suderinamas įrankis (vadinamas MCP serveriu) laikosi vieningo standarto. Šie serveriai gali pateikti sąrašą įrankių ar veiksmų, kuriuos jie siūlo, ir vykdyti tuos veiksmus, kai jų prašo AI agentas. AI agentų platformos, palaikančios MCP, gali aptikti galimus įrankius iš serverių ir juos iškviesti per šį standartizuotą protokolą.

### 💡 Palengvina prieigą prie žinių

Be įrankių teikimo, MCP taip pat palengvina prieigą prie žinių. Tai leidžia programoms suteikti kontekstą dideliems kalbos modeliams (LLM), susiejant juos su įvairiais duomenų šaltiniais. Pavyzdžiui, MCP serveris gali atstovauti įmonės dokumentų saugyklą, leidžiant agentams pagal poreikį gauti aktualią informaciją. Kitas serveris galėtų atlikti specifinius veiksmus, pvz., siųsti el. laiškus ar atnaujinti įrašus. Agentui šie veiksmai tiesiog atrodo kaip įrankiai – kai kurie įrankiai grąžina duomenis (žinių kontekstą), o kiti atlieka veiksmus. MCP efektyviai valdo abu.

Agentas, prisijungęs prie MCP serverio, automatiškai sužino apie serverio galimybes ir prieinamus duomenis per standartinį formatą. Ši standartizacija leidžia dinamiškai naudoti įrankius. Pavyzdžiui, pridėjus naują MCP serverį į agento sistemą, jo funkcijos tampa iš karto prieinamos be papildomo agento instrukcijų pritaikymo.

---

## 🔐 Praktinė MCP nauda

Štai praktinė MCP naudojimo nauda:

- **Naujumas**: Modeliai gali pasiekti naujausią informaciją už jų mokymo duomenų ribų  
- **Galimybių išplėtimas**: Modeliai gali naudotis specializuotais įrankiais užduotims, kurioms jie nebuvo apmokyti  
- **Sumažintos haliucinacijos**: Išoriniai duomenų šaltiniai suteikia faktinį pagrindą  
- **Privatumas**: Jautrūs duomenys gali likti saugioje aplinkoje, o ne būti įtraukti į užklausas  

---

## 📌 Pagrindinės išvados

Štai pagrindinės išvados apie MCP naudojimą:

- **MCP** standartizuoja, kaip AI modeliai sąveikauja su įrankiais ir duomenimis  
- Skatina **plėtrumą, nuoseklumą ir sąveikumą**  
- MCP padeda **sutrumpinti kūrimo laiką, pagerinti patikimumą ir išplėsti modelio galimybes**  
- Kliento-serverio architektūra **leidžia kurti lanksčias, plėtrias AI programas**  

---

## 🧠 Pratimas

Pagalvokite apie AI programą, kurią norėtumėte sukurti.

- Kokie **išoriniai įrankiai ar duomenys** galėtų pagerinti jos galimybes?  
- Kaip MCP galėtų padaryti integraciją **paprastesnę ir patikimesnę**?  

---

## Papildomi ištekliai

- [MCP GitHub saugykla](https://github.com/modelcontextprotocol)

---

## Kas toliau

Toliau: [1 skyrius: Pagrindinės sąvokos](../01-CoreConcepts/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.