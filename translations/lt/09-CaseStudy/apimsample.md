# Atvejo analizė: REST API atskleidimas API valdyme kaip MCP serveris

Azure API Management yra paslauga, kuri teikia vartus virš jūsų API galinių taškų. Ji veikia taip: Azure API Management veikia kaip tarpinis serveris priešais jūsų API ir gali nuspręsti, ką daryti su gaunamais užklausomis.

Naudodami ją pridėsite daugybę funkcijų, tokių kaip:

- **Sauga**, galite naudoti viską nuo API raktų, JWT iki valdomos tapatybės.
- **Ribojimas pagal dažnį**, puiki funkcija yra galimybė nuspręsti, kiek skambučių leidžiama per tam tikrą laiko vienetą. Tai padeda užtikrinti puikią patirtį visiems vartotojams ir, kad jūsų paslauga nebūtų perkrauta užklausų.
- **Mastelio keitimas ir apkrovos balansavimas**. Galite nustatyti kelis galinius taškus apkrovai balansuoti ir taip pat pasirinkti, kaip „apkrovos balansuoti“.
- **DI funkcijos kaip semantinis kešavimas**, žetonų limitas ir žetonų stebėjimas ir daugiau. Tai puikios funkcijos, kurios pagerina reagavimą ir padeda sekti savo žetonų išlaidas. [Skaitykite daugiau čia](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Kodėl MCP + Azure API Management?

Model Context Protocol greitai tampa standartu agentinėms DI programėlėms ir būdu nuosekliai atskleisti įrankius ir duomenis. Azure API Management yra natūralus pasirinkimas, kai reikia „valdyti“ API. MCP serveriai dažnai integruojami su kitais API, kad, pavyzdžiui, išspręstų užklausas į įrankį. Todėl Azure API Management ir MCP derinys yra labai prasmingas.

## Apžvalga

Šiame konkrečiame pavyzdyje mokysimės atskleisti API galinius taškus kaip MCP serverį. Tai leis lengvai paversti šiuos galinius taškus agentinės programos dalimi, tuo pačiu pasinaudojant Azure API Management funkcijomis.

## Pagrindinės funkcijos

- Jūs pasirenkate galinių taškų metodus, kuriuos norite atskleisti kaip įrankius.
- Papildomos funkcijos priklauso nuo to, ką nustatote politikos skyriuje jūsų API. Čia parodyta, kaip pridėti ribojimą pagal dažnį.

## Parengiamasis žingsnis: importuoti API

Jei jau turite API Azure API Management, puiku, galite praleisti šį žingsnį. Jei ne, peržiūrėkite šią nuorodą, [API importavimas į Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API atskleidimas kaip MCP serveris

Norėdami atskleisti API galinius taškus, atlikite šiuos veiksmus:

1. Eikite į Azure portalą adresu <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Eikite į savo API valdymo egzempliorių.

1. Kairiajame meniu pasirinkite APIs > MCP Servers > + Create new MCP Server.

1. Skiltyje API pasirinkite REST API, kurį atskleisite kaip MCP serverį.

1. Pasirinkite vieną ar daugiau API operacijų, kurias norite atskleisti kaip įrankius. Galite pasirinkti visas operacijas arba tik konkrečias.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Pasirinkite **Create**.

1. Eikite į meniu opciją **APIs** ir **MCP Servers**, turėtumėte pamatyti štai ką:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP serveris sukurtas, API operacijos atskleistos kaip įrankiai. MCP serveris matomas MCP Servers skiltyje. URL stulpelis rodo MCP serverio galinį tašką, kurį galite iškviesti testavimui arba kliento programoje.

## Pasirinktina: Politikos konfigūravimas

Azure API Management pagrindinė sąvoka yra politikos, kur nustatote skirtingas taisykles savo galiniams taškams, pavyzdžiui ribojimą pagal dažnį ar semantinį kešavimą. Šios politikos rašomos XML formatu.

Štai kaip galite nustatyti politiką MCP serverio skambučių ribojimui pagal dažnį:

1. Portale, skiltyje APIs, pasirinkite **MCP Servers**.

1. Pasirinkite sukurtą MCP serverį.

1. Kairiajame meniu MCP skiltyje pasirinkite **Policies**.

1. Politikos redaktoriuje pridėkite arba redaguokite politiką, kurią norite taikyti MCP serverio įrankiams. Politikos apibrėžiamos XML formatu. Pavyzdžiui, galite pridėti politiką, ribojančią skambučius į MCP serverio įrankius (šiuo atveju 5 skambučiai per 30 sekundžių vienam kliento IP adresui). Štai XML, kuris nustatys ribojimą pagal dažnį:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Štai kaip atrodo politiko redaktoriaus vaizdas:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Išbandykime

Įsitikinkime, kad mūsų MCP serveris veikia kaip planuota.

> [!NOTE]
> Azure API Management šiuo metu šį serverį atskleidžia per Streamable
> HTTP `/mcp` galinį tašką. Senesnis HTTP+SSE `/sse` transportas yra nebevykdomas ir
> turėtų būti naudojamas tik su senoviniais klientais.

Tam naudosime Visual Studio Code ir GitHub Copilot bei jo Agent režimą. Pridėsime MCP serverį į *mcp.json*. Tai leis Visual Studio Code veikti kaip agentinis klientas, o galutiniai vartotojai galės įvesti užklausą ir bendrauti su šiuo serveriu.

Pažiūrėkime, kaip pridėti MCP serverį Visual Studio Code:

1. Naudokite komandų paletę MCP: **Add Server command**.

1. Kai bus paprašyta, pasirinkite serverio tipą: **HTTP (HTTP arba Server Sent Events)**.

1. Įveskite Streamable HTTP URL, rodytą MCP serverio Azure API Management.
    Pavyzdžiui:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Įveskite serverio ID pagal savo pasirinkimą. Tai nėra svarbi reikšmė, bet padės atsiminti, kas yra šis serverio egzempliorius.

1. Pasirinkite, ar konfigūraciją išsaugoti jūsų darbo aplinkos nustatymuose, ar naudotojo nustatymuose.

  - **Darbo aplinkos nustatymai** – serverio konfigūracija išsaugoma .vscode/mcp.json faile, kuris prieinamas tik dabartinėje darbo aplinkoje.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Vartotojo nustatymai** – serverio konfigūracija pridedama į globalų *settings.json* failą ir yra prieinama visose darbo aplinkose. Konfigūracija atrodo panašiai į žemiau pateiktą:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Taip pat turite pridėti konfigūraciją – antraštę, kad autentifikacija vyktų tinkamai su Azure API Management. Naudojama antraštė vadinama **Ocp-Apim-Subscription-Key**.

    - Štai kaip ją pridėti nustatymuose:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), tai sukels užklausimą įvesti API rakto vertę, kurią galite rasti Azure portale savo Azure API Management egzemplioriui.

   - Norėdami vietoj to pridėti į *mcp.json*, galite pridėti taip:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Naudokite Agent režimą

Dabar mes esame pasiruošę – tiek nustatymuose, tiek *.vscode/mcp.json*. Išbandykime.

Turėtų būti Įrankių piktograma, kur išvardyti jūsų serverio atskleisti įrankiai:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Spustelėkite įrankių piktogramą ir turėtumėte matyti įrankių sąrašą:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Įveskite užklausą pokalbyje, kad iškviestumėte įrankį. Pavyzdžiui, jei pasirinkote įrankį užsakymo informacijai gauti, galite paklausti agento apie užsakymą. Štai pavyzdinė užklausa:

    ```text
    get information from order 2
    ```

    Dabar gausite įrankių piktogramą, klausančią, ar tęsti įrankio kvietimą. Pasirinkite tęsti, ir turėtumėte pamatyti rezultatą:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ką matote aukščiau priklauso nuo to, kokius įrankius nustatėte, tačiau idėja tokia, kad gaunate tekstinį atsakymą kaip aukščiau**


## Nuorodos

Štai kaip galite sužinoti daugiau:

- [Pamoka apie Azure API Management ir MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python pavyzdys: Saugaus nuotolinio MCP serverių naudojimas su Azure API Management (eksperimentinis)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP kliento autorizacijos laboratorija](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Naudokite Azure API Management plėtinį VS Code API importavimui ir valdymui](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registruokite ir raskite nuotolinius MCP serverius Azure API Centre](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Puikus repo, demonstruojantis daug DI galimybių su Azure API Management
- [AI Gateway dirbtuvės](https://azure-samples.github.io/AI-Gateway/) Apima dirbtuves su Azure portalu, kas yra puikus būdas pradėti vertinti DI galimybes.

## Kas toliau

- Atgal į: [Atvejų tyrimų apžvalga](./README.md)
- Toliau: [Azure DI kelionių agentai](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->