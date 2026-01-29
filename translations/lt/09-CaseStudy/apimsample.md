# Atvejo analizė: REST API eksponavimas API Management kaip MCP serveris

Azure API Management yra paslauga, kuri suteikia vartus jūsų API galiniams taškams. Ji veikia kaip tarpininkas prieš jūsų API ir gali nuspręsti, ką daryti su gaunamais užklausomis.

Naudodami ją, galite pridėti daugybę funkcijų, tokių kaip:

- **Saugumas** – galite naudoti viską nuo API raktų, JWT iki valdomos tapatybės.
- **Užklausų ribojimas** – puiki funkcija, leidžianti nustatyti, kiek užklausų gali būti apdorota per tam tikrą laiko vienetą. Tai padeda užtikrinti, kad visi naudotojai turėtų puikią patirtį ir kad jūsų paslauga nebūtų perkrauta užklausomis.
- **Mastelio keitimas ir apkrovos balansavimas** – galite nustatyti kelis galinius taškus apkrovos balansavimui ir nuspręsti, kaip „balansuoti apkrovą“.
- **Dirbtinio intelekto funkcijos, tokios kaip semantinis talpyklavimas**, užklausų limitas, užklausų stebėjimas ir kt. Tai puikios funkcijos, kurios pagerina atsako greitį ir padeda stebėti jūsų užklausų išlaidas. [Plačiau skaitykite čia](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Kodėl MCP + Azure API Management?

Model Context Protocol (MCP) greitai tampa standartu agentinėms AI programoms ir kaip nuosekliai eksponuoti įrankius bei duomenis. Azure API Management yra natūralus pasirinkimas, kai reikia „valdyti“ API. MCP serveriai dažnai integruojasi su kitais API, kad galėtų apdoroti užklausas įrankiams, pavyzdžiui. Todėl Azure API Management ir MCP derinys yra logiškas sprendimas.

## Apžvalga

Šiame konkrečiame naudojimo atvejyje išmoksime eksponuoti API galinius taškus kaip MCP serverį. Tai leis lengvai įtraukti šiuos galinius taškus į agentinę programą, tuo pačiu pasinaudojant Azure API Management funkcijomis.

## Pagrindinės funkcijos

- Galite pasirinkti galinių taškų metodus, kuriuos norite eksponuoti kaip įrankius.
- Papildomos funkcijos priklauso nuo to, ką konfigūruojate savo API politikos skyriuje. Čia parodysime, kaip pridėti užklausų ribojimą.

## Prieš pradedant: API importavimas

Jei jau turite API Azure API Management, puiku – galite praleisti šį žingsnį. Jei ne, peržiūrėkite šią nuorodą: [API importavimas į Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API eksponavimas kaip MCP serveris

Norėdami eksponuoti API galinius taškus, atlikite šiuos veiksmus:

1. Eikite į Azure Portal adresu <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. 
   Pasirinkite savo API Management instanciją.

1. Kairiajame meniu pasirinkite **APIs > MCP Servers > + Create new MCP Server**.

1. API skyriuje pasirinkite REST API, kurį norite eksponuoti kaip MCP serverį.

1. Pasirinkite vieną ar daugiau API operacijų, kurias norite eksponuoti kaip įrankius. Galite pasirinkti visas operacijas arba tik konkrečias.

    ![Pasirinkite metodus eksponavimui](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Pasirinkite **Create**.

1. Eikite į meniu parinktį **APIs** ir **MCP Servers**, turėtumėte matyti šį vaizdą:

    ![MCP serveris pagrindiniame lange](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP serveris sukurtas, o API operacijos eksponuojamos kaip įrankiai. MCP serveris rodomas MCP Servers lange. Stulpelyje URL pateikiamas MCP serverio galinio taško adresas, kurį galite naudoti testavimui arba klientinėje programoje.

## Pasirinktinai: Politikų konfigūravimas

Azure API Management turi pagrindinę politikų koncepciją, kur galite nustatyti įvairias taisykles savo galiniams taškams, pavyzdžiui, užklausų ribojimą ar semantinį talpyklavimą. Šios politikos rašomos XML formatu.

Štai kaip galite nustatyti politiką, ribojančią užklausų skaičių MCP serveriui:

1. Portale, skiltyje **APIs**, pasirinkite **MCP Servers**.

1. Pasirinkite sukurtą MCP serverį.

1. Kairiajame meniu, skiltyje MCP, pasirinkite **Policies**.

1. Politikų redaktoriuje pridėkite arba redaguokite politiką, kurią norite taikyti MCP serverio įrankiams. Politikos apibrėžiamos XML formatu. Pavyzdžiui, galite pridėti politiką, ribojančią užklausų skaičių MCP serverio įrankiams (šiuo atveju 5 užklausos per 30 sekundžių vienam kliento IP adresui). Štai XML, kuris nustatys užklausų ribojimą:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Štai politikų redaktoriaus vaizdas:

    ![Politikų redaktorius](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Išbandykite

Įsitikinkime, kad mūsų MCP serveris veikia kaip numatyta.

Tam naudosime Visual Studio Code ir GitHub Copilot su jo Agent režimu. Pridėsime MCP serverį į *mcp.json* failą. Tai leis Visual Studio Code veikti kaip klientui su agentinėmis galimybėmis, o galutiniai naudotojai galės įvesti užklausą ir sąveikauti su serveriu.

Štai kaip pridėti MCP serverį Visual Studio Code:

1. Naudokite MCP: **Add Server komandą iš Command Palette**.

1. Kai paprašoma, pasirinkite serverio tipą: **HTTP (HTTP arba Server Sent Events)**.

1. Įveskite MCP serverio URL API Management. Pavyzdys: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE galiniam taškui) arba **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP galiniam taškui), atkreipkite dėmesį į skirtumą tarp transportų `/sse` arba `/mcp`.

1. Įveskite serverio ID savo pasirinkimu. Tai nėra svarbi vertė, bet padės prisiminti, kas yra šis serverio instancija.

1. Pasirinkite, ar išsaugoti konfigūraciją darbo aplinkos nustatymuose, ar naudotojo nustatymuose.

  - **Darbo aplinkos nustatymai** – serverio konfigūracija išsaugoma .vscode/mcp.json faile, kuris pasiekiamas tik dabartinėje darbo aplinkoje.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    arba jei pasirinkote srautinį HTTP kaip transportą, tai atrodytų šiek tiek kitaip:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Naudotojo nustatymai** – serverio konfigūracija pridedama prie jūsų globalaus *settings.json* failo ir pasiekiama visose darbo aplinkose. Konfigūracija atrodo panašiai kaip ši:

    ![Naudotojo nustatymas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Taip pat reikia pridėti konfigūraciją – antraštę, kad būtų užtikrintas tinkamas autentifikavimas Azure API Management. Ji naudoja antraštę **Ocp-Apim-Subscription-Key**.

    - Štai kaip galite ją pridėti prie nustatymų:

    ![Antraštės pridėjimas autentifikavimui](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), tai sukels raginimą įvesti API rakto vertę, kurią galite rasti Azure Portal savo Azure API Management instancijoje.

   - Norėdami pridėti ją prie *mcp.json*, galite tai padaryti taip:

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

Dabar viskas paruošta tiek nustatymuose, tiek *.vscode/mcp.json*. Išbandykime.

Turėtų būti įrankių piktograma, kurioje rodomi eksponuoti įrankiai iš jūsų serverio:

![Įrankiai iš serverio](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Spustelėkite įrankių piktogramą ir turėtumėte matyti įrankių sąrašą:

    ![Įrankiai](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Įveskite užklausą pokalbyje, kad iškviestumėte įrankį. Pavyzdžiui, jei pasirinkote įrankį gauti informaciją apie užsakymą, galite paprašyti agento informacijos apie užsakymą. Štai pavyzdinė užklausa:

    ```text
    get information from order 2
    ```

    Dabar jums bus pateikta įrankių piktograma, prašanti tęsti įrankio vykdymą. Pasirinkite tęsti įrankio vykdymą, ir turėtumėte matyti rezultatą, panašų į šį:

    ![Rezultatas iš užklausos](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Tai, ką matote aukščiau, priklauso nuo to, kokius įrankius nustatėte, tačiau idėja yra gauti tekstinį atsakymą, kaip parodyta aukščiau.**

## Nuorodos

Štai kur galite sužinoti daugiau:

- [Pamoka apie Azure API Management ir MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python pavyzdys: Saugus nuotolinis MCP serverių naudojimas su Azure API Management (eksperimentinis)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP klientų autorizacijos laboratorija](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Naudokite Azure API Management plėtinį VS Code, kad importuotumėte ir valdytumėte API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Nuotolinių MCP serverių registravimas ir atradimas Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Puikus repo, rodantis daugybę AI galimybių su Azure API Management
- [AI Gateway dirbtuvės](https://azure-samples.github.io/AI-Gateway/) Apima dirbtuves naudojant Azure Portal – puikus būdas pradėti vertinti AI galimybes.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.