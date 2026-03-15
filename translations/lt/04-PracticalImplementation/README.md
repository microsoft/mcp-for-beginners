# Praktinė įgyvendinimo dalis

[![Kaip sukurti, išbandyti ir diegti MCP programas naudojant realius įrankius ir darbo eigas](../../../translated_images/lt/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Paspauskite ant paveikslėlio aukščiau, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

Praktinė įgyvendinimo dalis yra ta vieta, kur Model Context Protocol (MCP) galia tampa apčiuopiama. Nors svarbu suprasti teoriją ir MCP architektūrą, tikroji vertė atsiskleidžia tada, kai taikote šias sąvokas kuriant, išbandant ir diegiant sprendimus, sprendžiančius realius pasaulio iššūkius. Šis skyrius jungia koncepcines žinias su praktiniu kūrimu, vedantis jus per MCP pagrindu veikiančių programų kūrimo procesą.

Nesvarbu, ar kuriate išmaniuosius asistentus, integruojate DI į verslo darbo eigas, ar kuriate individualius duomenų apdorojimo įrankius, MCP suteikia lanksčią pagrindą. Jo kalbai nepriklausomas dizainas ir oficialūs SDK populiarioms programavimo kalboms leidžia platų kūrėjų spektrą pasiekti. Naudodamiesi šiais SDK galite greitai prototipuoti, iteruoti ir pritaikyti savo sprendimus įvairioms platformoms ir aplinkoms.

Toliau esančiuose skyriuose rasite praktinius pavyzdžius, pavyzdinį kodą ir diegimo strategijas, kurios demonstruoja, kaip įgyvendinti MCP C#, Java su Spring, TypeScript, JavaScript ir Python kalbomis. Taip pat sužinosite, kaip derinti ir testuoti MCP serverius, valdyti API ir diegti sprendimus debesyje naudojant Azure. Šios praktinės priemonės skirtos spartinti jūsų mokymąsi ir padėti užtikrintai kurti patikimas, gamybai paruoštas MCP programas.

## Apžvalga

Ši pamoka skirta praktiškiems MCP įgyvendinimo aspektams įvairiomis programavimo kalbomis. Išnagrinėsime, kaip naudoti MCP SDK C#, Java su Spring, TypeScript, JavaScript ir Python, siekiant kurti patikimas programas, derinti ir testuoti MCP serverius bei kurti pakartotinai naudojamus išteklius, užklausimus ir įrankius.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Įgyvendinti MCP sprendimus naudodamiesi oficialiais SDK įvairiomis programavimo kalbomis
- Sistemingai derinti ir testuoti MCP serverius
- Kurti ir naudoti serverio funkcijas (Ištekliai, Užklausimai ir Įrankiai)
- Kurti veiksmingas MCP darbo eigas sudėtingoms užduotims
- Optimizuoti MCP įgyvendinimus dėl našumo ir patikimumo

## Oficialūs SDK ištekliai

Model Context Protocol siūlo oficialius SDK kelioms kalboms (atitinka [MCP specifikaciją 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java su Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Pastaba:** reikalauja priklausomybės nuo [Project Reactor](https://projectreactor.io). (Žr. [diskusijos klausimą 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Darbas su MCP SDK

Šiame skyriuje pateikiami praktiniai MCP įgyvendinimo pavyzdžiai keliomis programavimo kalbomis. Galite rasti pavyzdinį kodą `samples` kataloge, suskirstytą pagal kalbas.

### Turimi pavyzdžiai

Saugykloje yra [pavyzdiniai įgyvendinimai](../../../04-PracticalImplementation/samples) šiose kalbose:

- [C#](./samples/csharp/README.md)
- [Java su Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Kiekvienas pavyzdys demonstruoja pagrindines MCP sąvokas ir įgyvendinimo modelius konkrečioje kalboje ir ekosistemoje.

### Praktiniai vadovai

Papildomi praktiniai MCP įgyvendinimo vadovai:

- [Puslapiavimas ir dideli rezultatų rinkiniai](./pagination/README.md) – kaip tvarkyti kursoriaus pagrindu veikiančią puslapiavimo funkciją įrankiams, ištekliams ir dideliems duomenų kiekiams

## Pagrindinės serverio funkcijos

MCP serveriai gali įgyvendinti bet kokią šių funkcijų kombinaciją:

### Ištekliai

Ištekliai suteikia kontekstą ir duomenis vartotojui arba DI modeliui naudoti:

- Dokumentų saugyklos
- Žinių bazės
- Struktūrizuoti duomenų šaltiniai
- Failų sistemos

### Užklausimai

Užklausimai yra šabloniniai pranešimai ir darbo eigų šablonai vartotojams:

- Iš anksto apibrėžti pokalbių šablonai
- Vadovaujami interakcijos modeliai
- Specializuotos dialogų struktūros

### Įrankiai

Įrankiai yra funkcijos, kurias DI modelis gali vykdyti:

- Duomenų apdorojimo įrankiai
- Išorinės API integracijos
- Skaičiavimo galimybės
- Paieškos funkcionalumas

## Pavyzdiniai įgyvendinimai: C# įgyvendinimas

Oficialiame C# SDK saugykloje yra keli pavyzdiniai įgyvendinimai, demonstruojantys skirtingus MCP aspektus:

- **Paprastas MCP klientas**: paprastas pavyzdys, kaip sukurti MCP klientą ir kviesti įrankius
- **Paprastas MCP serveris**: minimalus serverio įgyvendinimas su pagrindiniu įrankių registravimu
- **Pažangus MCP serveris**: pilnavertis serveris su įrankių registracija, autentifikacija ir klaidų valdymu
- **ASP.NET integracija**: pavyzdžiai, demonstruojantys integraciją su ASP.NET Core
- **Įrankių įgyvendinimo modeliai**: įvairūs įrankių įgyvendinimo modeliai skirtingo sudėtingumo lygiams

MCP C# SDK yra peržiūros stadijoje ir API gali keistis. Šį tinklaraštį nuolat atnaujinsime pagal SDK vystymąsi.

### Pagrindinės savybės

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Kaip sukurti savo [pirmą MCP serverį](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Visiems C# įgyvendinimo pavyzdžiams žiūrėkite [oficialią C# SDK pavyzdžių saugyklą](https://github.com/modelcontextprotocol/csharp-sdk)

## Pavyzdinis įgyvendinimas: Java su Spring

Java su Spring SDK siūlo tvirtas MCP įgyvendinimo galimybes su įmonių lygio funkcijomis.

### Pagrindinės savybės

- Spring Framework integracija
- Stipri tipų sauga
- Reaktyvios programavimo galimybės
- Išsamus klaidų valdymas

Pilnam Java su Spring įgyvendinimo pavyzdžiui žr. [Java su Spring pavyzdį](samples/java/containerapp/README.md) pavyzdžių kataloge.

## Pavyzdinis įgyvendinimas: JavaScript

JavaScript SDK suteikia lengvą ir lanksčią MCP įgyvendinimo prieigą.

### Pagrindinės savybės

- Node.js ir naršyklės palaikymas
- Promise pagrindu veikiantis API
- Lengva integracija su Express ir kitais karkasais
- WebSocket palaikymas srautiniam režimui

Pilnam JavaScript įgyvendinimo pavyzdžiui žr. [JavaScript pavyzdį](samples/javascript/README.md) pavyzdžių kataloge.

## Pavyzdinis įgyvendinimas: Python

Python SDK suteikia python-type MCP įgyvendinimą su puikiais ML karkasų integravimo sprendimais.

### Pagrindinės savybės

- Async/await palaikymas su asyncio
- FastAPI integracija``
- Paprastas įrankių registravimas
- Natūrali integracija su populiariomis ML bibliotekomis

Pilnam Python įgyvendinimo pavyzdžiui žr. [Python pavyzdį](samples/python/README.md) pavyzdžių kataloge.

## API valdymas

Azure API Management yra puikus sprendimas, kaip užtikrinti MCP serverių saugumą. Idėja yra įdėti Azure API Management instanciją prieš jūsų MCP serverį ir leisti jai valdyti tokias funkcijas, kaip:

- pralaidumo ribojimas
- žetonų valdymas
- stebėjimas
- apkrovos balansavimas
- saugumas

### Azure pavyzdys

Čia yra Azure pavyzdys, kuris tiksliai taip ir daro, t.y., [kuria MCP serverį ir jį saugo Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Pažiūrėkite, kaip vyksta autorizacijos srautas žemiau esančiame paveikslėlyje:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Paveikslėlyje vyksta šie veiksmai:

- Autentifikacija/Autorizacija vykdoma naudojant Microsoft Entra.
- Azure API Management veikia kaip vartai ir naudoja politiką srautui nukreipti ir valdyti.
- Azure Monitor fiksuoja visus užklausimus tolesnei analizei.

#### Autorizacijos srautas

Pažvelkime į autorizacijos srautą detaliau:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP autorizacijos specifikacija

Daugiau informacijos apie [MCP autorizacijos specifikaciją](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Nuotolinio MCP serverio diegimas į Azure

Pažiūrėkime, ar galime diegti anksčiau minėtą pavyzdį:

1. Klonuokite saugyklą

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Užregistruokite `Microsoft.App` resursų teikėją.

   - Jei naudojate Azure CLI, vykdykite `az provider register --namespace Microsoft.App --wait`.
   - Jei naudojate Azure PowerShell, vykdykite `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Po kurio laiko patikrinkite `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`, ar registracija baigta.

1. Paleiskite šią [azd](https://aka.ms/azd) komandą, kad sukurtumėte API valdymo paslaugą, funkcijų programėlę (su kodu) ir visas kitas reikiamas Azure paslaugas

    ```shell
    azd up
    ```

    Ši komanda turėtų įdiegti visus debesies išteklius Azure aplinkoje

### Serverio testavimas su MCP Inspector

1. Atidarykite **naują terminalo langą**, įdiekite ir paleiskite MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Turėtumėte pamatyti sąsają, panašią į:

    ![Connect to Node inspector](../../../translated_images/lt/connect.141db0b2bd05f096.webp)

1. Paspauskite CTRL ir spustelėkite, kad įkrautumėte MCP Inspector žiniatinklio programėlę pagal URL, kurį pateikia programa (pvz. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Nustatykite transporto tipą į `SSE`
1. Nustatykite savo veikiančio API Management SSE galinį tašką, kuris rodomas po `azd up`, ir **Prisijunkite**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Įrankių sąrašas**. Paspauskite ant įrankio ir **Paleiskite įrankį**.

Jeigu visi žingsniai pavyko, dabar turėtumėte būti prisijungę prie MCP serverio ir sugebėjote iškviesti įrankį.

## MCP serveriai Azure aplinkai

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Šių saugyklų rinkinys yra greito starto šablonas kuriant ir diegiant nuotolinius MCP (Model Context Protocol) serverius naudojant Azure Functions su Python, C# .NET arba Node/TypeScript.

Pavyzdžiai suteikia pilną sprendimą, leidžiantį kūrėjams:

- Kurti ir paleisti lokaliai: kurti ir derinti MCP serverį lokaliame kompiuteryje
- Diegti į Azure: lengvai diegti debesyje su paprasta azd up komanda
- Prisijungti iš klientų: jungtis prie MCP serverio iš įvairių klientų, įskaitant VS Code Copilot agento režimą bei MCP Inspector įrankį

### Pagrindinės savybės

- Saugumas pagal dizainą: MCP serveris yra apsaugotas raktų ir HTTPS mechanizmais
- Autentifikacijos parinktys: palaiko OAuth naudojant įmontuotą autentifikaciją ir/arba API valdymą
- Tinklo izoliacija: leidžia naudoti Azure virtualius tinklus (VNET) tinklo izoliacijai
- Serverless architektūra: naudoja Azure Functions skalabiliam, įvykiams valdyti skirtam vykdymui
- Vietinis vystymas: išsamus vietinio vystymo ir derinimo palaikymas
- Paprastas diegimas: supaprastintas Azure diegimo procesas

Saugykla apima visus reikalingus konfigūracijos failus, šaltinio kodą ir infrastruktūros apibrėžimus, kad greitai pradėtumėte kurti gamybai paruoštą MCP serverio įgyvendinimą.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) – MCP pavyzdys naudojant Azure Functions su Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) – MCP pavyzdys naudojant Azure Functions su C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) – MCP pavyzdys naudojant Azure Functions su Node/TypeScript.

## Pagrindinės pamokos

- MCP SDK suteikia kalbai pritaikytus įrankius patikimoms MCP sprendimų realizacijoms
- Derinimo ir testavimo procesas yra kritiškai svarbus patikimoms MCP programoms
- Pakartotinai naudojami užklausų šablonai užtikrina nuoseklias DI sąveikas
- Gerai sukurti darbo eiga gali koordinuoti sudėtingas užduotis, naudojant kelis įrankius
- MCP sprendimų įgyvendinimui reikia atsižvelgti į saugumą, našumą ir klaidų valdymą

## Užduotis

Sukurkite praktinę MCP darbo eigą, skirtą spręsti realų problemą jūsų srityje:

1. Nustatykite 3–4 įrankius, kurie būtų naudingi sprendžiant šią problemą
2. Sukurkite darbo eigos diagramą, kurioje būtų parodyta, kaip šie įrankiai tarpusavyje sąveikauja
3. Įgyvendinkite paprastą vieno iš įrankių versiją savo pasirinkta kalba
4. Sukurkite užklausos šabloną, kuris padėtų modeliui efektyviai naudoti jūsų įrankį

## Papildomi ištekliai

---

## Kas toliau

Toliau: [Pažangios temos](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus humanitarinis vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->