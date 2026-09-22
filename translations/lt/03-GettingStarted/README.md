## Pradžia  

[![Sukurkite savo pirmąjį MCP serverį](../../../translated_images/lt/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(Spustelėkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

Šiame skyriuje yra kelios pamokos:

- **1 Jūsų pirmasis serveris**, šioje pirmojoje pamokoje sužinosite, kaip sukurti savo pirmąjį serverį ir apžvelgti jį su inspektoriumi, vertingu įrankiu serverio testavimui ir derinimui, [į pamoką](01-first-server/README.md)

- **2 Klientas**, šioje pamokoje išmoksite sukurti klientą, kuris gali prisijungti prie jūsų serverio, [į pamoką](02-client/README.md)

- **3 Klientas su LLM**, dar geresnis klientų rašymo būdas yra pridėti LLM, kad jis galėtų "derėtis" su serveriu dėl veiksmų, [į pamoką](03-llm-client/README.md)

- **4 Serverio GitHub Copilot Agent režimo naudojimas Visual Studio Code**. Čia apžvelgsime, kaip vykdyti MCP serverį tiesiai iš Visual Studio Code, [į pamoką](04-vscode/README.md)

- **5 stdio Transport Server** stdio transportas yra rekomenduojama standartinė vietinė MCP serverio-kliento komunikacija, užtikrinanti saugų pagalbinių procesų pagrindu veikiančią komunikaciją su integruota procesų izoliacija [į pamoką](05-stdio-server/README.md)

- **6 MCP HTTP srautinė perdavimo funkcija (Streamable HTTP)**. Sužinokite apie standartinį
	nuotolinį transportą pagal [MCP specifikaciją 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http),
	taip pat apie senesnį sesijomis pagrįstą įgyvendinimą, išlaikytą pamokoje.
	[į pamoką](06-http-streaming/README.md)

- **7 AI įrankių rinkinio naudojimas VSCode** MCP klientų ir serverių vartojimui ir testavimui [į pamoką](07-aitk/README.md)

- **8 Testavimas**. Čia ypatingai sutelksime dėmesį, kaip įvairiais būdais galima testuoti serverį ir klientą, [į pamoką](08-testing/README.md)

- **9 Diegimas**. Šiame skyriuje apžvelgsime skirtingus jūsų MCP sprendimų diegimo būdus, [į pamoką](09-deployment/README.md)

- **10 Pažangus serverio naudojimas**. Šis skyrius aprėpia pažangų serverio naudojimą, [į pamoką](./10-advanced/README.md)

- **11 Autentifikacija**. Šiame skyriuje apžvelgsime, kaip pridėti paprastą autentifikaciją, nuo paprastos Basic Auth iki JWT ir RBAC. Rekomenduojama pradėti čia, o vėliau pažvelgti į pažangias temas 5 skyriuje ir papildomai stiprinti saugumą, vadovaujantis rekomendacijomis 2 skyriuje, [į pamoką](./11-simple-auth/README.md)

- **12 MCP šeimininkai**. Konfigūruokite ir naudokite populiarius MCP šeimininko klientus, įskaitant Claude Desktop, Cursor, Cline ir Windsurf. Sužinokite apie transporto tipus ir trikčių šalinimą, [į pamoką](./12-mcp-hosts/README.md)

- **13 MCP inspektorius**. Interaktyviai derinkite ir testuokite MCP serverius naudodami MCP inspektoriaus įrankį. Sužinokite, kaip spręsti problemas, naudoti įrankius, resursus ir protokolo žinutes, [į pamoką](./13-mcp-inspector/README.md)

- **14 Pavyzdžio ėmimas (Sampling)**. Sužinokite senąjį Sampling primityvą `2025-11-25` ir
	kaip pereiti prie naujų dizainų su tiesiogine LLM paslaugų teikėjo integracija. Sampling yra
	nenaudojamas MCP `2026-07-28`. [į pamoką](./14-sampling/README.md)

- **15 MCP programėlės**. Kurkite MCP serverius, kurie taip pat atsako su vartotojo sąsajos instrukcijomis, [į pamoką](./15-mcp-apps/README.md)

Model Context Protocol (MCP) yra atviras protokolas, standartizuojantis, kaip programos teikia kontekstą LLM. Galvokite apie MCP kaip apie USB-C prievadą AI programėlėms – tai standartizuotas būdas prijungti AI modelius prie skirtingų duomenų šaltinių ir įrankių.

## Mokymosi tikslai

Baigę šią pamoką, mokėsite:

- Paruošti MCP kūrimo aplinkas C#, Java, Python, TypeScript ir JavaScript kalboms
- Kurti ir diegti bazinius MCP serverius su pasirinktinais bruožais (ištekliais, užklausomis ir įrankiais)
- Kurti šeimininko programėles, kurios jungiasi prie MCP serverių
- Testuoti ir derinti MCP įgyvendinimus
- Suprasti dažnas diegimo problemas ir jų sprendimus
- Jungti savo MCP įgyvendinimus prie populiarių LLM paslaugų

## MCP aplinkos paruošimas

Prieš pradėdami dirbti su MCP, svarbu paruošti kūrimo aplinką ir suprasti pagrindinį darbo eigą. Šiame skyriuje jus supažindinsime su pradiniais nustatymo žingsniais, kad MCP pradžia būtų sklandi.

### Reikalavimai

Prieš pradedant MCP kūrimą, įsitikinkite, kad turite:

- **Kūrimo aplinka**: Jūsų pasirinktoje kalboje (C#, Java, Python, TypeScript arba JavaScript)
- **IDE/Redaktorius**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm arba bet kuris šiuolaikinis kodo redaktorius
- **Paketo tvarkyklės**: NuGet, Maven/Gradle, pip arba npm/yarn
- **API raktai**: Bet kurioms AI paslaugoms, kurias planuojate naudoti savo šeimininko programėlėse


### Oficiali SDK

Ateinančiuose skyriuose matysite sprendimus, sukurti naudojant Python, TypeScript,
Java ir .NET. Čia yra oficialios SDK.

SDK palaikymas MCP `2026-07-28` versijai diegiamas nepriklausomai pagal kalbas.
Prieš paleisdami pavyzdį, patikrinkite jo paketo versiją ir SDK išleidimo pastabas
dėl palaikomų protokolo versijų. Žr.
[oficialių SDK sąrašą](https://modelcontextprotocol.io/docs/sdk):
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Palaikoma bendradarbiaujant su Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Palaikoma bendradarbiaujant su Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Oficiali TypeScript įgyvendinimas
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Oficiali Python įgyvendinimas (FastMCP)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Oficiali Kotlin įgyvendinimas
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Palaikoma bendradarbiaujant su Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Oficiali Rust įgyvendinimas
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk) - Oficiali Go įgyvendinimas

## Svarbiausios išvados

- MCP kūrimo aplinkos paruošimas yra paprastas naudojant kalbai skirtas SDK
- MCP serverių kūrimas apima įrankių kūrimą ir registravimą su aiškiomis schemomis
- MCP klientai jungiasi prie serverių ir modelių, kad panaudotų išplėstą funkcionalumą
- Testavimas ir derinimas yra būtini patikimiems MCP įgyvendinimams
- Diegimo galimybės svyruoja nuo vietinio kūrimo iki debesų sprendimų

## Praktika

Turime rinkinį pavyzdžių, kurie papildo pratimus, kuriuos rasite visuose šio skyriaus skyriuose. Be to, kiekvienas skyrius turi savo pratimus ir užduotis.

- [Java skaičiuoklė](./samples/java/calculator/README.md)
- [.NET skaičiuoklė](../../../03-GettingStarted/samples/csharp)
- [JavaScript skaičiuoklė](./samples/javascript/README.md)
- [TypeScript skaičiuoklė](./samples/typescript/README.md)
- [Python skaičiuoklė](../../../03-GettingStarted/samples/python)

## Papildomi ištekliai

- [Agentų kūrimas naudojant Model Context Protocol Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Nuotolinis MCP su Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP agentas](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Kas toliau

Pradėkite nuo pirmos pamokos: [Sukurti savo pirmą MCP serverį](01-first-server/README.md)

Užbaigus šį modulį, tęskite: [4 modulis: Praktinė įgyvendinimo dalis](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->