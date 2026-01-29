# Atvejo analizė: Azure AI kelionių agentai – pavyzdinė įgyvendinimo schema

## Apžvalga

[Azure AI kelionių agentai](https://github.com/Azure-Samples/azure-ai-travel-agents) yra išsamus „Microsoft“ sukurtas pavyzdinis sprendimas, kuris demonstruoja, kaip sukurti daugiaveiksnį, dirbtiniu intelektu paremtą kelionių planavimo programą, naudojant Model Context Protocol (MCP), Azure OpenAI ir Azure AI Search. Šis projektas pristato geriausią praktiką, kaip koordinuoti kelis dirbtinio intelekto agentus, integruoti įmonės duomenis ir sukurti saugią, pritaikomą platformą realioms situacijoms.

## Pagrindinės funkcijos
- **Daugiaveiksnė koordinacija:** Naudojamas MCP, kad būtų koordinuojami specializuoti agentai (pvz., skrydžių, viešbučių ir maršrutų agentai), kurie bendradarbiauja vykdydami sudėtingas kelionių planavimo užduotis.
- **Įmonės duomenų integracija:** Prisijungia prie Azure AI Search ir kitų įmonės duomenų šaltinių, kad pateiktų naujausią ir aktualią informaciją kelionių rekomendacijoms.
- **Saugus, pritaikomas architektūros sprendimas:** Naudojamos Azure paslaugos autentifikacijai, autorizacijai ir pritaikomam diegimui, laikantis įmonės saugumo geriausios praktikos.
- **Pritaikomi įrankiai:** Įgyvendinami MCP įrankiai ir šablonai, leidžiantys greitai prisitaikyti prie naujų sričių ar verslo poreikių.
- **Vartotojo patirtis:** Pateikiama pokalbių sąsaja, leidžianti vartotojams bendrauti su kelionių agentais, naudojant Azure OpenAI ir MCP.

## Architektūra
![Architektūra](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Architektūros diagramos aprašymas

Azure AI kelionių agentų sprendimas sukurtas taip, kad būtų modulinis, pritaikomas ir saugiai integruotų kelis dirbtinio intelekto agentus bei įmonės duomenų šaltinius. Pagrindiniai komponentai ir duomenų srautas yra tokie:

- **Vartotojo sąsaja:** Vartotojai bendrauja su sistema per pokalbių sąsają (pvz., internetinį pokalbį ar „Teams“ botą), kuri siunčia užklausas ir gauna kelionių rekomendacijas.
- **MCP serveris:** Veikia kaip centrinis koordinatorius, priimantis vartotojo įvestį, valdantis kontekstą ir koordinuojantis specializuotų agentų (pvz., FlightAgent, HotelAgent, ItineraryAgent) veiksmus per Model Context Protocol.
- **Dirbtinio intelekto agentai:** Kiekvienas agentas atsakingas už tam tikrą sritį (skrydžiai, viešbučiai, maršrutai) ir įgyvendinamas kaip MCP įrankis. Agentai naudoja šablonus ir logiką užklausoms apdoroti bei atsakymams generuoti.
- **Azure OpenAI paslauga:** Užtikrina pažangų natūralios kalbos supratimą ir generavimą, leidžiantį agentams interpretuoti vartotojo ketinimus ir generuoti pokalbių atsakymus.
- **Azure AI Search ir įmonės duomenys:** Agentai užklausia Azure AI Search ir kitus įmonės duomenų šaltinius, kad gautų naujausią informaciją apie skrydžius, viešbučius ir kelionių galimybes.
- **Autentifikacija ir saugumas:** Integruojama su Microsoft Entra ID saugiai autentifikacijai ir taikomi minimalios prieigos kontrolės principai visiems ištekliams.
- **Diegimas:** Sukurta diegimui Azure Container Apps, užtikrinant pritaikomumą, stebėjimą ir veikimo efektyvumą.

Ši architektūra leidžia sklandžiai koordinuoti kelis dirbtinio intelekto agentus, saugiai integruoti įmonės duomenis ir sukurti tvirtą, pritaikomą platformą, skirtą kurti specifinėms dirbtinio intelekto sprendimams.

## Architektūros diagramos paaiškinimas žingsnis po žingsnio
Įsivaizduokite, kad planuojate didelę kelionę ir turite komandą ekspertų, kurie padeda jums su kiekviena detale. Azure AI kelionių agentų sistema veikia panašiai, naudodama skirtingas dalis (kaip komandos narius), kurių kiekviena turi specialią užduotį. Štai kaip viskas susijungia:

### Vartotojo sąsaja (UI):
Tai tarsi kelionių agento registratūra. Čia jūs (vartotojas) užduodate klausimus ar pateikiate prašymus, pvz., „Suraskite man skrydį į Paryžių.“ Tai gali būti pokalbių langas svetainėje ar žinučių programėlėje.

### MCP serveris (Koordinatorius):
MCP serveris yra kaip vadybininkas, kuris išklauso jūsų prašymą registratūroje ir nusprendžia, kuris specialistas turėtų atlikti kiekvieną dalį. Jis seka jūsų pokalbį ir užtikrina, kad viskas vyktų sklandžiai.

### Dirbtinio intelekto agentai (Specialistai):
Kiekvienas agentas yra tam tikros srities ekspertas – vienas žino viską apie skrydžius, kitas apie viešbučius, o dar kitas apie jūsų maršruto planavimą. Kai paprašote kelionės, MCP serveris siunčia jūsų prašymą tinkamam agentui (-ams). Šie agentai naudoja savo žinias ir įrankius, kad surastų geriausius variantus jums.

### Azure OpenAI paslauga (Kalbos ekspertas):
Tai tarsi turėti kalbos ekspertą, kuris tiksliai supranta, ko jūs prašote, nesvarbu, kaip tai suformuluojate. Jis padeda agentams suprasti jūsų prašymus ir atsakyti natūralia, pokalbių kalba.

### Azure AI Search ir įmonės duomenys (Informacijos biblioteka):
Įsivaizduokite didžiulę, naujausią biblioteką su visa naujausia kelionių informacija – skrydžių tvarkaraščiais, viešbučių prieinamumu ir kt. Agentai ieško šioje bibliotekoje, kad pateiktų tiksliausius atsakymus jums.

### Autentifikacija ir saugumas (Apsaugos darbuotojas):
Kaip apsaugos darbuotojas tikrina, kas gali patekti į tam tikras zonas, ši dalis užtikrina, kad tik autorizuoti asmenys ir agentai galėtų pasiekti jautrią informaciją. Tai saugo jūsų duomenis.

### Diegimas Azure Container Apps (Pastatas):
Visi šie asistentai ir įrankiai dirba kartu saugiame, pritaikomame pastate (debesyje). Tai reiškia, kad sistema gali aptarnauti daug vartotojų vienu metu ir visada yra prieinama, kai jums jos reikia.

## Kaip viskas veikia kartu:

- Jūs pradedate užduodami klausimą registratūroje (UI).
- Vadybininkas (MCP serveris) nusprendžia, kuris specialistas (agentas) turėtų jums padėti.
- Specialistas naudoja kalbos ekspertą (OpenAI), kad suprastų jūsų prašymą, ir biblioteką (AI Search), kad surastų geriausią atsakymą.
- Apsaugos darbuotojas (Autentifikacija) užtikrina, kad viskas būtų saugu.
- Visa tai vyksta patikimame, pritaikomame pastate (Azure Container Apps), todėl jūsų patirtis yra sklandi ir saugi.

Šis komandinis darbas leidžia sistemai greitai ir saugiai padėti jums planuoti kelionę, kaip ekspertų kelionių agentų komanda, dirbanti moderniame biure!

## Techninis įgyvendinimas
- **MCP serveris:** Talpina pagrindinę koordinavimo logiką, pateikia agentų įrankius ir valdo kontekstą daugiapakopėms kelionių planavimo užduotims.
- **Agentai:** Kiekvienas agentas (pvz., FlightAgent, HotelAgent) įgyvendinamas kaip MCP įrankis su savo šablonais ir logika.
- **Azure integracija:** Naudojama Azure OpenAI natūralios kalbos supratimui ir Azure AI Search duomenų paieškai.
- **Saugumas:** Integruojama su Microsoft Entra ID autentifikacijai ir taikomi minimalios prieigos kontrolės principai visiems ištekliams.
- **Diegimas:** Palaikomas diegimas Azure Container Apps, užtikrinant pritaikomumą ir veikimo efektyvumą.

## Rezultatai ir poveikis
- Demonstruoja, kaip MCP gali būti naudojamas koordinuoti kelis dirbtinio intelekto agentus realiame, gamybos lygio scenarijuje.
- Paspartina sprendimų kūrimą, pateikdamas pritaikomas schemas agentų koordinavimui, duomenų integracijai ir saugiam diegimui.
- Tarnauja kaip pavyzdys, kaip kurti specifines, dirbtiniu intelektu paremtas programas, naudojant MCP ir Azure paslaugas.

## Nuorodos
- [Azure AI kelionių agentų GitHub saugykla](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI paslauga](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.