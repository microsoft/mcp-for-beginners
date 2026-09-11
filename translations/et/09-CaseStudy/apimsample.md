# Juhtumiuuring: Ava REST API API halduses MCP serverina

Azure API Management on teenus, mis pakub teie API lõpp-punktide kohale väravat. Selle toimimispõhimõte on see, et Azure API Management toimib teie API-de ees proksina ja saab otsustada saabuvate päringutega, mida teha.

Selle kasutamisel lisate hulga võimalusi, nagu:

- **Turvalisus**, saate kasutada kõike alates API võtmetest, JWT-st kuni hallatava identiteedini.
- **Kutsu piiramine**, suurepärane funktsioon on võimalus määrata, mitu päringut teatud ajaühiku jooksul lubatakse. See aitab tagada kõigile kasutajatele hea kogemuse ja et teie teenust ei koormata ülemäära.
- **Skaalamine ja koormuse tasakaalustamine**. Saate seadistada mitu lõpp-punkti, et koormust jagada, ning määrata, kuidas "koormust tasakaalustada".
- **Tehisintellekti funktsioonid nagu semantilise vahemälu kasutamine**, märgi piirmäär ja jälgimine ning palju muud. Need on suurepärased funktsioonid, mis parandavad reageerimiskiirust ning aitavad teil tokenite kasutust paremini jälgida. [Loe lähemalt siit](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Miks MCP + Azure API Management?

Mudelikonteksti protokoll (Model Context Protocol) saab kiiresti standardiks agentsetele tehisintellekti rakendustele ning tööriistade ja andmete järjepidevaks avaldamiseks. Azure API Management on loomulik valik, kui peate API-sid "haldama". MCP serverid integreeruvad sageli teiste API-dega, et lahendada päringuid näiteks tööriista jaoks. Seetõttu on Azure API Managementu ja MCP kombineerimine väga mõistlik.

## Ülevaade

Selles konkreetse juhtumi näites õpime API lõpp-punktide avaldamist MCP serverina. Selle kaudu saab neid lõpp-punkte hõlpsasti teha agentse rakenduse osaks ning samal ajal kasutada Azure API Managementu võimalusi.

## Põhifunktsioonid

- Valite, millised lõpp-punktide meetodid soovite tööriistadena avaldada.
- Täiendavad funktsioonid sõltuvad teie API poliitikate osas seadistatud konfiguratsioonist. Siin näitame, kuidas lisada kutsete piiramine.

## Eelnev samm: API impordimine

Kui teil on Azure API Managementus juba API olemas, siis võite selle sammu vahele jätta. Kui ei, siis vaadake seda linki, [API importimine Azure API Managementusse](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API avaldamine MCP serverina

API lõpp-punktide avaldamiseks järgime neid samme:

1. Minge Azure portaalile aadressil <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Minge oma API Managementu eksemplari juurde.

1. Vasakpoolses menüüs valige APIs > MCP Servers > + Create new MCP Server.

1. API-st valige REST API, mida soovite MCP serverina avaldada.

1. Valige üks või mitu API operatsiooni tööriistadena avaldamiseks. Võite valida kõik või ainult konkreetsed operatsioonid.

    ![Valige meetodid avaldamiseks](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Valige **Create**.

1. Navigeerige menüüs valikutele **APIs** ja **MCP Servers**, peaksite nägema järgmist:

    ![Vaade MCP serverile põhiaknas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server on loodud ja API operatsioonid on avaldatud tööriistadena. MCP server ilmub MCP Servers paanis. URL veerg näitab MCP serveri lõpp-punkti, mida saate testimiseks või kliendirakenduses kasutada.

## Vabatahtlik: poliitikate seadistamine

Azure API Managementu põhikontseptsiooniks on poliitikad, kus saate oma lõpp-punktidele määrata erinevaid reegleid, näiteks kutsete piiramine või semantilise vahemälu kasutamine. Need poliitikad on XML-is.

Siin on, kuidas seadistada poliitika MCP serveri kutsede piiramiseks:

1. Portaalis, APIs alt, valige **MCP Servers**.

1. Valige loodud MCP server.

1. Vasakul menüüs, MCP alt, valige **Policies**.

1. Poliitika redaktoris lisage või muutke poliitikaid, mida soovite MCP serveri tööriistadele rakendada. Poliitikad määratakse XML-formaadis. Näiteks saate lisada poliitika, mis piirab MCP serveri tööriistade kutsed (siinkohal 5 kutsumist 30 sekundi jooksul ühe kliendi IP-aadressi kohta). Järgnevalt on XML, mis selle piirangu paneb:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Siin on poliitika redaktori pilt:

    ![Poliitika redaktor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Proovime seda

Veendume, et meie MCP Server töötab ootuspäraselt.

> [!NOTE]
> Azure API Management avaldab praegu seda serverit Streamable
> HTTP `/mcp` lõpp-punkti kaudu. Vanem HTTP+SSE `/sse` transpordimehhanism on aegunud ja
> seda tuleks kasutada ainult pärandkliendiga.

Selleks kasutame Visual Studio Code’i ja GitHub Copiloti ning selle agendi režiimi. Lisame MCP serveri *mcp.json* faili. Sellega hakkab Visual Studio Code tegutsema agendina ning lõppkasutajad saavad tüüpida päringu ja suhelda selle serveriga.

Vaatame, kuidas MCP server Visual Studio Code’is lisada:

1. Kasutage käsku MCP: **Add Server Command Command Palette'ist**.

1. Kui küsitakse, valige serveri tüüp: **HTTP (HTTP või Server Sent Events)**.

1. Sisestage Streamable HTTP URL, mis on näidatud MCP serveri jaoks API halduses.
    Näiteks:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Sisestage serveri ID meelepäraselt. See väärtus ei ole oluline, kuid aitab teil selle serveri eksemplari meeles pidada.

1. Valige, kas salvestada konfiguratsioon tööruumi seadetesse või kasutaja seadistustesse.

  - **Tööruumi seadistused** - serveri konfiguratsioon salvestatakse ainult praeguses tööruumis olevasse .vscode/mcp.json faili.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Kasutaja seadistused** - serveri konfiguratsioon lisatakse teie ülemaailmsesse *settings.json* faili ja on saada kõigis tööruumides. Konfiguratsioon näeb välja umbes järgmiselt:

    ![Kasutaja seade](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Peate lisama ka konfiguratsiooni, pealkirja, et autentimine Azure API Managementu poole korralikult toimiks. Kasutatakse päist nimega **Ocp-Apim-Subscription-Key**.

    - Nii saate selle sisestada seadistustesse:

    ![Päise lisamine autentimiseks](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), see põhjustab, et küsitakse API võtme väärtust, mille leiate Azure portaalist oma Azure API Managementu instantsi alt.

   - Kui soovite seda lisada *mcp.json* faili, saate selle lisada järgmiselt:

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

### Kasutage agentrežiimi

Nüüd oleme seadistanud kas seadistustes või *.vscode/mcp.json* failis. Proovime seda.

Peaks ilmuma tööriistade ikoon, kus kuvatakse teie serveri avaldatud tööriistad:

![Tööriistad serverist](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klõpsake tööriistade ikoonil ja peaksite nägema nimekirja tööriistadest:

    ![Tööriistad](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Sisestage vestlusesse käsk tööriista käivitamiseks. Näiteks kui valisite tööriista, mis annab infot tellimuse kohta, võite agendilt tellimuse kohta küsida. Näide päringust:

    ```text
    get information from order 2
    ```

    Teile kuvatakse nüüd tööriista ikoon, mis palub teil valida tööriista käivitamise. Valige, et tööriist jookseks edasi. Nüüd peaksite nägema sellist tulemust:

    ![Päringu tulemus](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **see, mida ülalpool näete, sõltub sellest, milliseid tööriistu olete seadistanud, kuid põhimõte on, et saate tekstilise vastuse nagu näidatud**


## Viited

Siin on, kuidas saate rohkem teada:

- [Õpetus Azure API Managementust ja MCP-st](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python näidis: Remote MCP serverite turvamine Azure API Managementu abil (katsetus)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP kliendi autoriseerimise labor](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Kasuta Azure API Management laiendust VS Code’is API-de importimiseks ja haldamiseks](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registreeri ja avasta kauged MCP serverid Azure API Centeris](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Suurepärane hoidla, mis demonstreerib mitmeid AI võimalusi koos Azure API Managementuga
- [AI Gateway töötoad](https://azure-samples.github.io/AI-Gateway/) Sisaldab töötoa materjale Azure portaaliga, mis on suurepärane viis AI võimaluste hindamiseks.

## Mis edasi

- Tagasi: [Juhtumiuuringute ülevaade](./README.md)
- Järgmine: [Azure AI reisiagentuurid](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->