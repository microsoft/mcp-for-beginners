# Juhtumiuuring: Avalda REST API API Managementis kui MCP-server

Azure API Management on teenus, mis pakub väravat teie API lõpp-punktide kohale. See toimib nii, et Azure API Management käitub teie API-de ees nagu puhverserver ja saab otsustada, mida teha sissetulevate päringutega.

Selle kasutamisel lisate hulga funktsioone, nagu:

- **Turvalisus**, saate kasutada kõike alates API-võtmetest ja JWT-st kuni hallatud identiteedini.
- **Päringute piiramine**, suurepärane omadus on võimalus otsustada, mitu kutsumist mingis ajavahemikus lubada. See aitab tagada, et kõigil kasutajatel oleks hea kogemus ja et teie teenus ei muutuks päringutest ülekoormatuks.
- **Skaalimine ja koormuse tasakaalustamine**. Saate seadistada mitu lõpp-punkti koormuse jaotamiseks ning otsustada ka, kuidas "koormust tasakaalustada". 
- **Tehisintellekti funktsioonid nagu semantiline vahemällu salvestamine**, tokeni piirang ja tokeni jälgimine ning palju muud. Need on suurepärased funktsioonid, mis parandavad reageerimiskiirust ja aitavad teil tokeni kulutust kontrolli all hoida. [Loe lisaks](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities). 

## Miks MCP + Azure API Management?

Model Context Protocol muutub kiiresti agentsete tehisintellekti rakenduste jaoks standardiks ning selleks, kuidas tööriistu ja andmeid järjepideval viisil eksponeerida. Azure API Management on loomulik valik, kui peate API-sid "haldama". MCP-serverid integreeruvad sageli teiste API-dega, et näiteks lahendada päringud tööriistale. Seetõttu on Azure API Managementu ja MCP kombineerimine mõistlik.

## Ülevaade

Selles konkreetses kasutusjuhus õpime, kuidas avaldada API lõpp-punktid MCP-serverina. Nii saame need lõpp-punktid hõlpsasti muuta osa agentilisest rakendusest ja samal ajal kasutada Azure API Managementu funktsioone.

## Peamised funktsioonid

- Valite lõpp-punkti meetodid, mida soovite tööriistadena avaldada.
- Täiendavad funktsioonid sõltuvad sellest, mida te API poliitika sektsioonis konfigureerite. Siin näitame teile, kuidas lisada päringute piiramist (rate limiting).

## Eel-samm: API importimine

Kui teil on Azure API Managementis juba API olemas, siis suurepärane — võite selle sammu vahele jätta. Kui mitte, vaadake seda linki: [API importimine Azure API Managementi](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Avalda API MCP-serverina

API lõpp-punktide avaldamiseks järgige neid samme:

1. Avage Azure'i portaal ja minge aadressile <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Navigeerige oma API Managementi instantsi juurde.

1. Vasakpoolses menüüs valige APIs > MCP Servers > + Create new MCP Server.

1. APIs valige REST API, mida soovite avaldada MCP-serverina.

1. Valige üks või mitu API toimingut, mida soovite tööriistadena avaldada. Võite valida kõik toimingud või ainult konkreetsed toimingud.

    ![Vali meetodid, mida avaldada](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Valige **Create**.

1. Navigeerige menüüvalikusse **APIs** ja **MCP Servers**, te peaksite nägema järgmist:

    ![Vaadake MCP-serverit põhivaates](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-server on loodud ja API toimingud on avaldatud tööriistadena. MCP-server on loetletud MCP Servers paanis. Veeru URL näitab MCP-serveri lõpp-punkti, mida saate kutsuda testimiseks või kliendirakenduses.

## Valikuline: poliitikate seadistamine

Azure API Managementil on põhimõtteliselt poliitikate kontseptsioon, kus saate määrata erinevaid reegleid oma lõpp-punktidele, näiteks päringute piiramine või semantiline vahemälu. Need poliitikad kirjutatakse XML-is.

Siin on, kuidas saate seadistada poliitika MCP-serveri päringute piiramiseks:

1. Portaalis, APIs all, valige **MCP Servers**.

1. Valige loodud MCP-server.

1. Vasakus menüüs, MCP all, valige **Policies**.

1. Poliitika redaktoris lisage või muutke poliitikaid, mida soovite MCP-serveri tööriistadele rakendada. Poliitikad on määratletud XML-vormingus. Näiteks saate lisada poliitika, mis piirab kutsed MCP-serveri tööriistadele (selles näites 5 kutsumist 30 sekundi jooksul ühe kliendi IP-aadressi kohta). Järgnev XML põhjustab päringute piiramise:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Siin on pilt poliitika redaktorist:

    ![Poliitikate redaktor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Proovige seda

Veendume, et meie MCP-server töötab nii, nagu ette nähtud.

> [!NOTE]
> Azure API Management praegu eksponeerib seda serverit läbi Streamable
> HTTP `/mcp` lõpp-punkti. Vanem HTTP+SSE `/sse` transport on aegunud ja
> tuleks seda kasutada ainult pärandklientide puhul.

Selleks kasutame Visual Studio Code'i ja GitHub Copiloti agentrežiimi. Lisame MCP-serveri *mcp.json* faili. Nii toimides hakkab Visual Studio Code käituma kliendina agendivõimekusega ja lõppkasutajad saavad sisestada prompti ning suhelda nimetatud serveriga.

Vaatame, kuidas MCP-server Visual Studio Code'i lisada:

1. Käivitage käsk MCP: **Add Server** Command Palette'ist.

1. Kui küsitakse, valige serveri tüüp: **HTTP (HTTP or Server Sent Events)**.

1. Sisestage Streamable HTTP URL, mis on näidatud MCP-serveri jaoks API Managementis.
    Näiteks:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Sisestage serveri ID vastavalt soovile. See ei ole tähtis väärtus, kuid aitab teil meeles pidada, mis see serveri instants on.

1. Valige, kas salvestada konfiguratsioon tööruumi seadistustesse või kasutaja seadistustesse.

    - **Workspace settings** - Serveri konfiguratsioon salvestatakse `.vscode/mcp.json` faili, mis on saadaval ainult praeguses tööruumis.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **User settings** - Serveri konfiguratsioon lisatakse teie globaalsesse *settings.json* faili ja on saadaval kõigis tööruumides. Konfiguratsioon näeb välja sarnaselt järgmisele:

      ![Kasutaja seadistus](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Peate lisama ka konfiguratsioonipäise, et tagada korrektne autentimine Azure API Managementi suunas. See kasutab päist nimega **Ocp-Apim-Subscription-Key**.

    - Siin on, kuidas saate selle seadetesse lisada:


    ![Päise lisamine autentimiseks](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), see kuvab dialoogi, kus küsitakse API võtme väärtust, mille leiate Azure'i portaalist oma Azure API Managementi instantsi jaoks.

   - Kui soovite selle lisada hoopis *mcp.json* faili, saate seda teha järgmiselt:

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

### Kasutage agendi režiimi

Nüüd oleme kõik seadistatud kas seadetes või *.vscode/mcp.json* failis. Proovime seda.

Peaks olema olemas Tööriistad ikoon, kus on loetletud teie serveri avaldatud tööriistad:

![Tööriistad serverist](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klõpsake tööriistade ikooni ja peaksite nägema tööriistade loendit, nagu allpool:

    ![Tööriistad](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Sisestage vestlusesse prompt, et tööriist käivitada. Näiteks kui valisite tööriista tellimuse info saamiseks, võite küsida agendilt tellimuse kohta. Siin on näide promptist:

    ```text
    get information from order 2
    ```

    Teile kuvatakse nüüd tööriistade ikoon, mis küsib, kas soovite jätkata tööriista kutsumist. Valige jätkamine, peaksite nüüd nägema sellist väljundit:

    ![Tulemus päringust](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Mida te näete üleval sõltub sellest, milliseid tööriistu olete seadistanud, kuid põhimõte on see, et saate sarnase tekstilise vastuse nagu ülaltoodud.**


## Viited

Siit saate lisainfot:

- [Juhend Azure API Managementi ja MCP kohta](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python näide: turvalised kaug-MCP-serverid Azure API Managementiga (eksperimentaalne)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP kliendi autoriseerimise labor](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Kasutage Azure API Management laiendust VS Code'i jaoks API-de importimiseks ja haldamiseks](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registreerige ja avastage kaug-MCP-serverid Azure API Centeris](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Suurepärane hoidla, mis demonstreerib mitmeid tehisintellekti võimalusi Azure API Managementiga
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Sisaldab töötubasid, mis kasutavad Azure Portali, mis on suurepärane viis alustada tehisintellekti võimekuste hindamist.

## Mis järgmiseks

- Tagasi: [Juhtumiuuringute ülevaade](./README.md)
- Järgmine: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->