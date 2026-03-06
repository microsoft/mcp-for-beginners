# Praktiline rakendamine

[![Kuidas ehitada, testida ja juurutada MCP rakendusi tõeliste tööriistade ja töövoogudega](../../../translated_images/et/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Klõpsake ülaloleval pildil, et vaadata selle õppetunni videot)_

Praktiline rakendamine on koht, kus Model Context Protocol'i (MCP) võimsus muutub käegakatsutavaks. Kuigi MCP taga oleva teooria ja arhitektuuri mõistmine on oluline, on tõeline väärtus siis, kui rakendate neid kontseptsioone lahenduste ehitamiseks, testimiseks ja juurutamiseks, mis lahendavad reaalmaailma probleeme. See peatükk sillutab lõhet kontseptuaalse teadmise ja praktilise arenduse vahel, juhatades teid MCP-põhiste rakenduste elluviimise protsessis.

Olenemata sellest, kas arendate intelligentseid assistente, integreerite tehisintellekti äriprotsessidesse või ehitate kohandatud tööriistu andmetöötluseks, pakub MCP paindlikku alust. Selle keeleagnostiline disain ja ametlikud SDK-d populaarsetele programmeerimiskeeltele teevad selle ligipääsetavaks laiendile arendajatele. Nende SDK-de kasutamise abil saate kiiresti prototüüpida, iteratiivselt arendada ja skaleerida oma lahendusi erinevatel platvormidel ja keskkondades.

Järgmistes lõikudes leiate praktilisi näiteid, näidiskoodi ja juurutamisstrateegiaid, mis demonstreerivad, kuidas MCP-d rakendada C#, Java Spring'i, TypeScripti, JavaScripti ja Pythoniga. Õppite ka, kuidas MCP servereid siluda ja testida, hallata API-sid ning juurutada lahendusi pilves Azure'i abil. Need praktilised ressursid on mõeldud teie õppimise kiirendamiseks ja enesekindlaks ning töökindlate tootmisvalmis MCP rakenduste ehitamiseks.

## Ülevaade

See õppetund keskendub MCP praktilisele rakendamisele mitmes programmeerimiskeeles. Uurime, kuidas kasutada MCP SDK-sid C#, Java Spring'i, TypeScripti, JavaScripti ja Pythoniga, et ehitada töökindlaid rakendusi, siluda ja testida MCP servereid ning luua taaskasutatavaid ressursse, prompt'e ja tööriistu.

## Õpieesmärgid

Selle õppetunni lõpuks suudate:

- Rakendada MCP lahendusi, kasutades ametlikke SDK-sid erinevates programmeerimiskeeltes
- Süstemaatiliselt siluda ja testida MCP servereid
- Luua ja kasutada serveri funktsioone (ressursid, prompt'id ja tööriistad)
- Kujundada tõhusaid MCP töövooge keerukate ülesannete jaoks
- Optimeerida MCP rakendusi jõudluse ja usaldusväärsuse tagamiseks

## Ametlikud SDK ressursid

Model Context Protocol pakub ametlikke SDK-sid mitmele keelele (kooskõlas [MCP Spetsifikatsiooniga 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Märkus:** nõuab sõltuvust [Project Reactor](https://projectreactor.io). (Vt [arutelu teemal 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Töötamine MCP SDK-dega

See sektsioon annab praktilisi näiteid MCP rakendamisest mitmes programmeerimiskeeles. Näidiskood asub `samples` kaustas, korraldatuna keelte järgi.

### Saadaval näited

Repositoorium sisaldab [näidisrakendusi](../../../04-PracticalImplementation/samples) järgmistes keeltes:

- [C#](./samples/csharp/README.md)
- [Java Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Iga näide demonstreerib peamisi MCP kontseptsioone ja rakendusmustreid konkreetse keele ja ökosüsteemi jaoks.

### Praktilised juhendid

Täiendavad juhendid praktiliseks MCP rakendamiseks:

- [Lehitsemine ja suured tulemuste komplektid](./pagination/README.md) – Kursoripõhise lehitsemise käsitlemine tööriistade, ressursside ja suurte andmekogumite jaoks

## Põhiserveri funktsioonid

MCP serverid võivad rakendada mis tahes kombinatsiooni järgmistest funktsioonidest:

### Ressursid

Ressursid pakuvad kasutajale või tehisintellektimudelile konteksti ja andmeid:

- Dokumentide hoidlad
- Teadmistebaasid
- Struktureeritud andmeallikad
- Failisüsteemid

### Prompt'id

Prompt'id on malli tüüpi sõnumid ja töövood kasutajatele:

- Eelmääratletud vestlusmallid
- Juhitud interaktsioonimustrid
- Spetsialiseeritud dialoogistruktuurid

### Tööriistad

Tööriistad on funktsioonid, mida AI mudel saab käivitada:

- Andmetöötluse tööriistad
- Väliste API-de integratsioonid
- Arvutusvõimekus
- Otsingufunktsionaalsus

## Näidisrakendused: C# rakendus

Ametlik C# SDK hoidla sisaldab mitmeid näidisrakendusi, mis demonstreerivad MCP erinevaid aspekte:

- **Lihtne MCP klient**: Lihtne näide, kuidas luua MCP klient ja kutsuda tööriistu
- **Lihtne MCP server**: Minimaalne serveri rakendus koos põhilise tööriistade registreerimisega
- **Täpsem MCP server**: Täisfunktsionaalne server tööriistade registreerimise, autentimise ja veahaldusega
- **ASP.NET integratsioon**: Näited ASP.NET Core integratsiooni kohta
- **Tööriistade rakendusmustrid**: Erinevad mustrid tööriistade rakendamiseks erineva keerukuse tasemega

MCP C# SDK on eelvaates ja API-d võivad muutuda. Jätkame selle blogi uuendamist vastavalt SDK arengule.

### Peamised funktsioonid

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Oma [esimese MCP serveri ehitamine](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Täielike C# rakenduste näidete jaoks külastage [ametliku C# SDK näidiste hoidlat](https://github.com/modelcontextprotocol/csharp-sdk)

## Näidisrakendus: Java Spring rakendus

Java Spring SDK pakub tugevaid MCP rakendusvõimalusi ettevõtte tasemel funktsioonidega.

### Peamised funktsioonid

- Spring Frameworki integratsioon
- Tugev tüübikindlus
- Reaktiivne programmeerimine
- Ulatuslik veahaldus

Täieliku Java Spring rakenduse näite leiate [Java Spring näitest](samples/java/containerapp/README.md) näidiste kaustas.

## Näidisrakendus: JavaScript rakendus

JavaScript SDK pakub kerget ja paindlikku MCP rakendamise lähenemist.

### Peamised funktsioonid

- Node.js ja brauseri tugi
- Põhineb lubadustel (Promise-based API)
- Lihtne integratsioon Expressi ja muude raamistikudega
- Veebisokli tugi voogedastuseks

Täieliku JavaScript rakenduse näite leiate [JavaScript näitest](samples/javascript/README.md) näidiste kaustas.

## Näidisrakendus: Python rakendus

Python SDK pakub pythonilikku lähenemist MCP-le suurepäraste masinõppe raamistikute integratsioonidega.

### Peamised funktsioonid

- Async/await tugi asyncio abil
- FastAPI integratsioon
- Lihtne tööriistade registreerimine
- Loomulik integratsioon populaarsete ML teekidega

Täieliku Pythoni rakenduse näite leiate [Python näitest](samples/python/README.md) näidiste kaustas.

## API haldus

Azure API Management on suurepärane lahendus MCP serverite turvamiseks. Idee on panna Azure API Managementi instants MCP serveri ette ja lasta sellel hallata funktsioone, mida tõenäoliselt soovite, näiteks:

- kiiruspiirang
- tokenite haldus
- jälgimine
- koormuse tasakaalustamine
- turvalisus

### Azure näidis

Siin on Azure näidis, mis teeb täpselt seda, st [loob MCP serveri ja turvab selle Azure API Managementiga](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Vaadake alloleval pildil, kuidas toimub autoriseerimisvoog:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Ülaltoodud pildil toimub järgnevalt:

- Autentimine/autoriseerimine toimub Microsoft Entra abil.
- Azure API Management toimib väravana ja kasutab poliitikaid liikluse suunamiseks ja haldamiseks.
- Azure Monitor logib kõik päringud edasiseks analüüsiks.

#### Autoriseerimisvoog

Vaatame autoriseerimisvoogu detailsemalt:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP autoriseerimise spetsifikatsioon

Lisateavet leiate [MCP autoriseerimise spetsifikatsioonist](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Remote MCP serveri juurutamine Azure'i

Vaatame, kas suudame varasemalt mainitud näidist juurutada:

1. Kloonige hoidla

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Registreerige `Microsoft.App` ressursside pakkuja.

   - Kui kasutate Azure CLI-d, käivitage `az provider register --namespace Microsoft.App --wait`.
   - Kui kasutate Azure PowerShelli, käivitage `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Pärast mõnda aega kontrollige registratsiooni olekut käsuga `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`.

1. Käivitage see [azd](https://aka.ms/azd) käsk, et luua API haldusteenus, funktsioonirakendus (koos koodiga) ja kõik teised vajalikud Azure ressursid

    ```shell
    azd up
    ```

    See käsk peaks juurutama kõik pilveressursid Azure'is

### MCP Inspectoriga serveri testimine

1. Avage **uus terminali aken**, installige ja käivitage MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Peaksite nägema liidest sarnaselt:

    ![Connect to Node inspector](../../../translated_images/et/connect.141db0b2bd05f096.webp)

1. CTRL-klõpsake, et laadida MCP Inspector veebirakendus aadressilt, mille rakendus kuvab (näiteks [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Määrake transporditüübiks `SSE`
1. Sisestage URL oma jooksva API Management SSE lõpp-punkti aadress, mis kuvatakse pärast käsku `azd up`, ja **ühenduge**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Tööriistade nimekiri**. Klõpsake tööriista ja valige **Run Tool**.

Kui kõik sammud on õigesti tehtud, olete nüüd ühendatud MCP serveriga ja suutnud tööriista käivitada.

## MCP serverid Azure jaoks

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): See hoidlate kogum on kiire alguse mall kohandatud Remote MCP (Model Context Protocol) serverite ehitamiseks ja juurutamiseks Azure Functions abil Pythonis, C# .NET-s või Node/TypeScriptis.

Näidised pakuvad terviklikku lahendust, mis võimaldab arendajatel:

- Ehita ja käivita kohalikult: Arendada ja siluda MCP serverit lokaalses arvutis
- Juurutada Azure'i: Lihtne pilve juurutamine ühe azd up käsuga
- Ühenduda klientidelt: MCP serveriga ühenduse loomine mitmesugustest klientidest, sealhulgas VS Code Copilot agent režiim ja MCP Inspector tööriist

### Peamised funktsioonid

- Turvalisus disainist lähtuvalt: MCP server on turvatud võtmete ja HTTPS-iga
- Autentimisvalikud: Tugi OAuth-ile sisseehitatud autentimise ja/või API Managementi kaudu
- Võrgu isoleerimine: Võimaldab võrgu isoleerimist Azure Virtuaalvõrkude (VNET) abil
- Serverivaba arhitektuur: Kasutab Azure Functions'i skaleeritava sündmuspõhise täitmise jaoks
- Kohalik areng: Põhjalik tugi kohalikuks arendamiseks ja silumiseks
- Lihtne juurutus: Sujuv juurutamise protsess Azure'i

Hoidla sisaldab kõiki vajalikke konfiguratsioonifaile, lähtekoodi ja infrastruktuuri definitsioone, et kiiresti alustada tootmisvalmis MCP serveri rakendusega.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Näidisrakendus MCP-st Azure Functions abil Pythoni keeles

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Näidisrakendus MCP-st Azure Functions abil C# .NET keeles

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Näidisrakendus MCP-st Azure Functions abil Node/TypeScriptis.

## Peamised õppetunnid

- MCP SDK-d pakuvad keelespetsiifilisi tööriistu töökindlate MCP lahenduste rakendamiseks
- Silumine ja testimine on usaldusväärsete MCP rakenduste jaoks hädavajalikud
- Taaskasutatavad prompt mallid võimaldavad järjepidevaid AI interaktsioone
- Hästi kujundatud töövood võivad orkestreerida keerukaid ülesandeid mitmete tööriistadega
- MCP lahenduse rakendamisel tuleb arvestada turvalisuse, jõudluse ja veahaldusega

## Harjutus

Kujundage praktiline MCP töövoog, mis lahendab teie valdkonnas reaalmaailma probleemi:

1. Määrake 3-4 tööriista, mis oleksid selle probleemi lahendamisel kasulikud
2. Looge töövoo diagramm, mis näitab, kuidas need tööriistad omavahel suhtlevad
3. Rakendage ühe tööriista lihtne versioon oma eelistatud keeles
4. Looge prompt mall, mis aitaks mudelil teie tööriista tõhusalt kasutada

## Täiendavad ressursid

---

## Mis nüüd

Järgmine: [Edasijõudnud teemad](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahutuslause**:
See dokument on tõlgitud kasutades tehisintellekti tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, tuleb arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma algkeeles tuleks pidada usaldusväärseks allikaks. Kriitilise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste ega valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->