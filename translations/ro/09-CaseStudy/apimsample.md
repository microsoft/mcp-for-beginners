# Studiu de caz: Expunerea unei API REST în API Management ca server MCP

Azure API Management este un serviciu care oferă un Gateway deasupra punctelor finale ale API-urilor tale. Funcționează ca un proxy în fața API-urilor tale și poate decide ce să facă cu cererile primite.

Prin utilizarea acestuia, adaugi o gamă largă de funcționalități, cum ar fi:

- **Securitate**, poți folosi totul, de la chei API, JWT până la identitate gestionată.
- **Limitarea ratei**, o funcționalitate excelentă este abilitatea de a decide câte apeluri trec într-o anumită unitate de timp. Acest lucru ajută la asigurarea unei experiențe bune pentru toți utilizatorii și la prevenirea supraîncărcării serviciului tău cu cereri.
- **Scalare și echilibrare a încărcării**. Poți configura mai multe puncte finale pentru a echilibra încărcarea și poți decide cum să "echilibrezi încărcarea".
- **Funcționalități AI, cum ar fi caching semantic**, limitarea token-urilor și monitorizarea token-urilor și altele. Acestea sunt funcționalități excelente care îmbunătățesc receptivitatea și te ajută să monitorizezi consumul de token-uri. [Citește mai multe aici](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## De ce MCP + Azure API Management?

Model Context Protocol devine rapid un standard pentru aplicațiile AI agentice și pentru modul de expunere a instrumentelor și datelor într-un mod consistent. Azure API Management este o alegere naturală atunci când ai nevoie să "gestionezi" API-uri. Serverele MCP se integrează adesea cu alte API-uri pentru a rezolva cererile către un instrument, de exemplu. Prin urmare, combinarea Azure API Management și MCP are foarte mult sens.

## Prezentare generală

În acest caz specific, vom învăța să expunem punctele finale ale API-urilor ca un server MCP. Prin aceasta, putem face cu ușurință ca aceste puncte finale să facă parte dintr-o aplicație agentică, beneficiind în același timp de funcționalitățile oferite de Azure API Management.

## Funcționalități cheie

- Selectezi metodele punctelor finale pe care dorești să le expui ca instrumente.
- Funcționalitățile suplimentare pe care le obții depind de ceea ce configurezi în secțiunea de politici pentru API-ul tău. Dar aici îți vom arăta cum poți adăuga limitarea ratei.

## Pas preliminar: importarea unui API

Dacă ai deja un API în Azure API Management, excelent, atunci poți sări peste acest pas. Dacă nu, verifică acest link, [importarea unui API în Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Expunerea API-ului ca server MCP

Pentru a expune punctele finale ale API-ului, urmează acești pași:

1. Accesează portalul Azure la următoarea adresă <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. Navighează la instanța ta de API Management.

1. În meniul din stânga, selectează **APIs > MCP Servers > + Create new MCP Server**.

1. În API, selectează un API REST pentru a-l expune ca server MCP.

1. Selectează una sau mai multe operațiuni API pentru a le expune ca instrumente. Poți selecta toate operațiunile sau doar operațiuni specifice.

    ![Selectează metodele pentru expunere](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Selectează **Create**.

1. Navighează la opțiunea de meniu **APIs** și **MCP Servers**, ar trebui să vezi următoarele:

    ![Vezi serverul MCP în panoul principal](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Serverul MCP este creat, iar operațiunile API sunt expuse ca instrumente. Serverul MCP este listat în panoul MCP Servers. Coloana URL arată punctul final al serverului MCP pe care îl poți apela pentru testare sau în cadrul unei aplicații client.

## Opțional: Configurarea politicilor

Azure API Management are conceptul de bază al politicilor, unde configurezi diferite reguli pentru punctele tale finale, cum ar fi limitarea ratei sau caching semantic. Aceste politici sunt scrise în format XML.

Iată cum poți configura o politică pentru a limita rata serverului MCP:

1. În portal, sub **APIs**, selectează **MCP Servers**.

1. Selectează serverul MCP pe care l-ai creat.

1. În meniul din stânga, sub MCP, selectează **Policies**.

1. În editorul de politici, adaugă sau editează politicile pe care dorești să le aplici instrumentelor serverului MCP. Politicile sunt definite în format XML. De exemplu, poți adăuga o politică pentru a limita apelurile către instrumentele serverului MCP (în acest exemplu, 5 apeluri la fiecare 30 de secunde per adresă IP client). Iată XML-ul care va cauza limitarea ratei:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Iată o imagine a editorului de politici:

    ![Editor de politici](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Testare

Să ne asigurăm că serverul MCP funcționează conform intenției.

Pentru aceasta, vom folosi Visual Studio Code și GitHub Copilot în modul Agent. Vom adăuga serverul MCP într-un fișier *mcp.json*. Prin aceasta, Visual Studio Code va acționa ca un client cu capabilități agentice, iar utilizatorii finali vor putea introduce un prompt și interacționa cu serverul respectiv.

Iată cum să adaugi serverul MCP în Visual Studio Code:

1. Folosește comanda MCP: **Add Server din Command Palette**.

1. Când ți se cere, selectează tipul de server: **HTTP (HTTP sau Server Sent Events)**.

1. Introdu URL-ul serverului MCP din API Management. Exemplu: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (pentru endpoint SSE) sau **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (pentru endpoint MCP), observă diferența între transporturi: `/sse` sau `/mcp`.

1. Introdu un ID de server la alegerea ta. Acesta nu este o valoare importantă, dar te va ajuta să îți amintești ce reprezintă această instanță de server.

1. Selectează dacă să salvezi configurația în setările workspace-ului sau în setările utilizatorului.

  - **Setările workspace-ului** - Configurația serverului este salvată într-un fișier .vscode/mcp.json disponibil doar în workspace-ul curent.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    sau dacă alegi HTTP streaming ca transport, ar fi ușor diferit:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Setările utilizatorului** - Configurația serverului este adăugată în fișierul global *settings.json* și este disponibilă în toate workspace-urile. Configurația arată similar cu următoarele:

    ![Setare utilizator](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. De asemenea, trebuie să adaugi o configurație, un header pentru a te asigura că se autentifică corect către Azure API Management. Folosește un header numit **Ocp-Apim-Subscription-Key**.

    - Iată cum poți să-l adaugi în setări:

    ![Adăugarea header-ului pentru autentificare](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), acest lucru va cauza afișarea unui prompt pentru a introduce valoarea cheii API pe care o poți găsi în portalul Azure pentru instanța ta de Azure API Management.

   - Pentru a-l adăuga în *mcp.json*, poți să-l adaugi astfel:

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

### Utilizarea modului Agent

Acum suntem pregătiți, fie în setări, fie în *.vscode/mcp.json*. Să încercăm.

Ar trebui să existe o pictogramă Tools, unde instrumentele expuse de serverul tău sunt listate:

![Instrumente de la server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Fă clic pe pictograma instrumentelor și ar trebui să vezi o listă de instrumente astfel:

    ![Instrumente](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Introdu un prompt în chat pentru a invoca instrumentul. De exemplu, dacă ai selectat un instrument pentru a obține informații despre o comandă, poți întreba agentul despre o comandă. Iată un exemplu de prompt:

    ```text
    get information from order 2
    ```

    Acum vei fi prezentat cu o pictogramă de instrumente care îți cere să continui apelarea unui instrument. Selectează să continui rularea instrumentului, ar trebui să vezi un rezultat astfel:

    ![Rezultat din prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ceea ce vezi mai sus depinde de instrumentele pe care le-ai configurat, dar ideea este că primești un răspuns textual ca cel de mai sus**

## Referințe

Iată cum poți afla mai multe:

- [Tutorial despre Azure API Management și MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Exemplu Python: Securizarea serverelor MCP remote folosind Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laborator de autorizare client MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Utilizarea extensiei Azure API Management pentru VS Code pentru a importa și gestiona API-uri](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Înregistrarea și descoperirea serverelor MCP remote în Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Un repo excelent care arată multe capabilități AI cu Azure API Management
- [Workshop-uri AI Gateway](https://azure-samples.github.io/AI-Gateway/) Conține workshop-uri folosind portalul Azure, o modalitate excelentă de a începe evaluarea capabilităților AI.

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru acuratețe, vă rugăm să aveți în vedere că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.