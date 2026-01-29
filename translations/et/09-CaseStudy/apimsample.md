# Juhtumiuuring: REST API avaldamine API Managementis MCP serverina

Azure API Management on teenus, mis pakub väravat teie API lõpp-punktide peal. Selle tööpõhimõte seisneb selles, et Azure API Management toimib teie API-de ees puhvrina ja otsustab, mida sissetulevate päringutega teha.

Selle kasutamisega lisate hulgaliselt funktsioone, nagu:

- **Turvalisus** – saate kasutada kõike alates API võtmetest ja JWT-st kuni hallatud identiteedini.
- **Kvoodipiirangud** – suurepärane funktsioon, mis võimaldab määrata, kui palju päringuid saab teatud ajaühiku jooksul läbi. See aitab tagada, et kõik kasutajad saavad suurepärase kogemuse ja teie teenus ei ole ülekoormatud.
- **Mastaapsus ja koormuse tasakaalustamine** – saate seadistada mitu lõpp-punkti koormuse tasakaalustamiseks ning määrata, kuidas koormust tasakaalustada.
- **Tehisintellekti funktsioonid, nagu semantiline vahemällu salvestamine**, tokeni piirangud ja tokeni jälgimine ning palju muud. Need funktsioonid parandavad reageerimisvõimet ja aitavad teil tokeni kulutustel silma peal hoida. [Loe rohkem siit](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Miks MCP + Azure API Management?

Model Context Protocol (MCP) muutub kiiresti standardiks agentlike tehisintellekti rakenduste jaoks ning tööriistade ja andmete ühtseks avaldamiseks. Azure API Management on loomulik valik, kui vajate API-de haldamist. MCP serverid integreeruvad sageli teiste API-dega, et lahendada päringuid tööriistadele. Seetõttu on Azure API Managementi ja MCP kombineerimine väga loogiline.

## Ülevaade

Selles konkreetse kasutusjuhtumi näites õpime API lõpp-punkte MCP serverina avaldama. Sel viisil saame hõlpsasti muuta need lõpp-punktid agentlike rakenduste osaks, kasutades samal ajal Azure API Managementi funktsioone.

## Põhifunktsioonid

- Valite lõpp-punkti meetodid, mida soovite tööriistadena avaldada.
- Täiendavad funktsioonid sõltuvad sellest, mida te oma API poliitikasektsioonis konfigureerite. Siin näitame, kuidas lisada kvoodipiiranguid.

## Eeltingimus: API importimine

Kui teil on juba API Azure API Managementis, siis võite selle sammu vahele jätta. Kui ei, siis vaadake seda linki: [API importimine Azure API Managementi](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API avaldamine MCP serverina

API lõpp-punktide avaldamiseks järgige neid samme:

1. Minge Azure portaali aadressil <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. 
Avage oma API Managementi instants.

1. Vasakpoolses menüüs valige **APIs > MCP Servers > + Create new MCP Server**.

1. Valige API, mida soovite MCP serverina avaldada.

1. Valige üks või mitu API operatsiooni, mida soovite tööriistadena avaldada. Võite valida kõik operatsioonid või ainult konkreetsed operatsioonid.

    ![Valige meetodid avaldamiseks](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Valige **Create**.

1. Minge menüüvalikusse **APIs** ja **MCP Servers**, kus peaksite nägema järgmist:

    ![Vaadake MCP serverit peapaneelil](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server on loodud ja API operatsioonid on tööriistadena avaldatud. MCP server kuvatakse MCP serverite paneelil. Veeru **URL** all kuvatakse MCP serveri lõpp-punkt, mida saate testimiseks või kliendirakenduses kasutada.

## Valikuline: poliitikate konfigureerimine

Azure API Managementil on poliitikate põhimõiste, kus saate seadistada erinevaid reegleid oma lõpp-punktidele, näiteks kvoodipiirangud või semantiline vahemällu salvestamine. Need poliitikad kirjutatakse XML-is.

Siin on juhised, kuidas seadistada poliitikat MCP serveri kvoodipiiranguks:

1. Portaalis, **APIs** all, valige **MCP Servers**.

1. Valige loodud MCP server.

1. Vasakpoolses menüüs, **MCP** all, valige **Policies**.

1. Poliitikate redaktoris lisage või muutke poliitikaid, mida soovite MCP serveri tööriistadele rakendada. Poliitikad määratletakse XML-vormingus. Näiteks saate lisada poliitika, mis piirab päringuid MCP serveri tööriistadele (selles näites 5 päringut 30 sekundi jooksul ühe kliendi IP-aadressi kohta). Siin on XML, mis rakendab kvoodipiirangut:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Siin on poliitikate redaktori pilt:

    ![Poliitikate redaktor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Proovige järele

Veendume, et meie MCP server töötab ootuspäraselt.

Selleks kasutame Visual Studio Code'i ja GitHub Copilotit ning selle agentrežiimi. Lisame MCP serveri *mcp.json* faili. Sel viisil toimib Visual Studio Code kliendina agentlike võimekustega ja lõppkasutajad saavad sisestada päringu ning suhelda serveriga.

Siin on juhised MCP serveri lisamiseks Visual Studio Code'is:

1. Kasutage MCP: **Add Server käsku Command Palette'is**.

1. Kui küsitakse, valige serveri tüüp: **HTTP (HTTP või Server Sent Events)**.

1. Sisestage MCP serveri URL API Managementis. Näide: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE lõpp-punkti jaoks) või **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP lõpp-punkti jaoks), märkige, kuidas transpordi erinevus on `/sse` või `/mcp`.

1. Sisestage serveri ID oma valikul. See ei ole oluline väärtus, kuid aitab teil meeles pidada, mis serveri instants see on.

1. Valige, kas salvestada konfiguratsioon oma tööruumi seadistustesse või kasutaja seadistustesse.

  - **Tööruumi seadistused** – serveri konfiguratsioon salvestatakse .vscode/mcp.json faili, mis on saadaval ainult praeguses tööruumis.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    või kui valite voogesituse HTTP transpordiks, oleks see veidi erinev:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Kasutaja seadistused** – serveri konfiguratsioon lisatakse teie globaalsesse *settings.json* faili ja on saadaval kõigis tööruumides. Konfiguratsioon näeb välja järgmine:

    ![Kasutaja seadistus](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Peate lisama ka konfiguratsiooni, päise, et tagada autentimine Azure API Managementi vastu. Selleks kasutatakse päist nimega **Ocp-Apim-Subscription-Key**.

    - Siin on juhised, kuidas seda seadistustesse lisada:

    ![Päise lisamine autentimiseks](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), see kuvab päringu, kus küsitakse API võtme väärtust, mida leiate Azure portaalist oma Azure API Managementi instantsi jaoks.

   - Kui soovite selle lisada *mcp.json* faili, saate seda teha järgmiselt:

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

Nüüd on kõik seadistatud kas seadistustes või *.vscode/mcp.json* failis. Proovime seda.

Seal peaks olema tööriistade ikoon, kus kuvatakse serveri poolt avaldatud tööriistad:

![Serveri tööriistad](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klõpsake tööriistade ikooni ja peaksite nägema tööriistade loendit, mis näeb välja selline:

    ![Tööriistad](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Sisestage vestluses päring, et tööriista käivitada. Näiteks, kui valisite tööriista tellimuse kohta teabe saamiseks, võite agendilt tellimuse kohta küsida. Siin on näide päringust:

    ```text
    get information from order 2
    ```

    Teile kuvatakse tööriistade ikoon, mis palub teil tööriista käivitamist jätkata. Valige tööriista käivitamise jätkamine ja peaksite nägema tulemust, mis näeb välja selline:

    ![Päringu tulemus](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Ülaltoodud tulemus sõltub sellest, millised tööriistad olete seadistanud, kuid idee on, et saate tekstilise vastuse nagu ülaltoodud näites.**

## Viited

Siin saate rohkem õppida:

- [Azure API Managementi ja MCP juhend](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python näide: Turvaliste kaug-MCP serverite kasutamine Azure API Managementiga (eksperimentaalne)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP kliendi autoriseerimise labor](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Azure API Managementi laienduse kasutamine VS Code'is API-de importimiseks ja haldamiseks](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Kaug-MCP serverite registreerimine ja avastamine Azure API Centeris](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Suurepärane repo, mis näitab paljusid tehisintellekti võimalusi Azure API Managementiga
- [AI Gateway töötoad](https://azure-samples.github.io/AI-Gateway/) Sisaldab töötubasid Azure portaalis, mis on suurepärane viis tehisintellekti võimaluste hindamise alustamiseks.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.