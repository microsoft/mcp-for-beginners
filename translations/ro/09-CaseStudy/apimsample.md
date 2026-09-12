# Studiu de caz: Expunerea REST API în API Management ca un server MCP

Azure API Management este un serviciu care oferă un Gateway deasupra punctelor finale API. Modul în care funcționează este că Azure API Management acționează ca un proxy în fața API-urilor dvs. și poate decide ce să facă cu solicitările primite.

Prin utilizarea acestuia, adăugați o gamă largă de funcționalități cum ar fi:

- **Securitate**, puteți folosi orice, de la chei API, JWT până la identitate gestionată.
- **Limitarea ratei**, o caracteristică excelentă este posibilitatea de a decide câte apeluri să treacă într-o anumită unitate de timp. Aceasta ajută să se asigure că toți utilizatorii au o experiență excelentă și, de asemenea, că serviciul dvs. nu este copleșit de cereri.
- **Scalare și echilibrare a încărcării**. Puteți configura mai multe puncte finale pentru a echilibra încărcarea și puteți decide și cum să faceți această "echilibrare".
- **Funcții AI cum ar fi caching semantic**, limită de tokeni și monitorizarea tokenilor și altele. Acestea sunt caracteristici excelente care îmbunătățesc răspunsul și ajută să fiți la curent cu consumul de tokeni. [Citiți mai mult aici](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## De ce MCP + Azure API Management?

Model Context Protocol devine rapid un standard pentru aplicații AI agentice și modul de expunere a uneltelor și datelor într-un mod consecvent. Azure API Management este o alegere naturală atunci când trebuie să „gestionați” API-uri. Serverele MCP se integrează adesea cu alte API-uri pentru a rezolva cereri către un instrument, de exemplu. Prin urmare, combinarea Azure API Management cu MCP are mult sens.

## Prezentare generală

În acest caz de utilizare specific vom învăța să expunem punctele finale API ca un Server MCP. Procedând astfel, putem face cu ușurință aceste puncte finale parte dintr-o aplicație agentică, valorificând în același timp funcționalitățile din Azure API Management.

## Caracteristici cheie

- Selectați metodele endpoint pe care doriți să le expuneți ca unelte.
- Funcționalitățile suplimentare pe care le primiți depind de ceea ce configurați în secțiunea de politici pentru API-ul dvs. Dar aici vă vom arăta cum să adăugați limitarea ratei.

## Pas prealabil: importarea unui API

Dacă aveți deja un API în Azure API Management, grozav, puteți să săriți acest pas. Dacă nu, consultați acest link, [importarea unui API în Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Expunerea API ca Server MCP

Pentru a expune punctele finale API, urmați pașii următori:

1. Accesați Portalul Azure și următoarea adresă <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Navigați la instanța dvs. de API Management.

1. În meniul din stânga, selectați APIs > MCP Servers > + Creare server MCP nou.

1. La API, selectați un REST API pentru a-l expune ca un server MCP.

1. Selectați una sau mai multe operații API pentru a le expune ca unelte. Puteți selecta toate operațiile sau doar anumite operații specifice.

    ![Selectați metodele de expus](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Selectați **Creează**.

1. Navigați la opțiunea de meniu **APIs** și **MCP Servers**, ar trebui să vedeți următoarele:

    ![Vezi serverul MCP în panoul principal](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Serverul MCP este creat, iar operațiile API sunt expuse ca unelte. Serverul MCP este listat în panoul MCP Servers. Coloana URL arată endpoint-ul serverului MCP pe care îl puteți apela pentru testare sau dintr-o aplicație client.

## Opțional: Configurarea politicilor

Azure API Management are conceptul de bază al politicilor unde setați diferite reguli pentru punctele finale, cum ar fi limitarea ratei sau caching semantic. Aceste politici sunt scrise în XML.

Iată cum puteți seta o politică pentru limitarea ratei serverului MCP:

1. În portal, sub APIs, selectați **MCP Servers**.

1. Selectați serverul MCP pe care l-ați creat.

1. În meniul din stânga, sub MCP, selectați **Policies**.

1. În editorul de politici, adăugați sau editați politicile pe care doriți să le aplicați uneltelor serverului MCP. Politicile sunt definite în format XML. De exemplu, puteți adăuga o politică pentru a limita apelurile către uneltele serverului MCP (în acest exemplu, 5 apeluri la 30 de secunde per adresă IP client). Iată XML-ul care va cauza limitarea ratei:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Iată o imagine a editorului de politici:

    ![Editor de politici](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Încearcă-l

Să ne asigurăm că Serverul MCP funcționează conform intenției.

> [!NOTE]
> Azure API Management expune în prezent acest server prin endpoint-ul Streamable
> HTTP `/mcp`. Transportul mai vechi HTTP+SSE `/sse` este depreciat și
> ar trebui folosit doar cu clienți vechi.

Pentru aceasta, vom folosi Visual Studio Code și GitHub Copilot și modul său Agent. Vom adăuga serverul MCP într-un *mcp.json*. Procedând astfel, Visual Studio Code va acționa ca un client cu capabilități agentice și utilizatorii finali vor putea scrie un prompt și interacționa cu serverul menționat.

Haideți să vedem cum să adăugăm serverul MCP în Visual Studio Code:

1. Folosiți comanda MCP: **Add Server din Command Palette**.

1. Când vi se cere, selectați tipul serverului: **HTTP (HTTP sau Server Sent Events)**.

1. Introduceți URL-ul Streamable HTTP afișat pentru serverul MCP în API Management.
    De exemplu:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Introduceți un ID de server la alegere. Aceasta nu este o valoare importantă, dar vă va ajuta să vă amintiți ce instanță de server este.

1. Selectați dacă doriți să salvați configurația în setările workspace-ului sau în setările utilizatorului.

  - **Setările workspace-ului** - Configurația serverului este salvată într-un fișier .vscode/mcp.json disponibil doar în workspace-ul curent.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Setările utilizatorului** - Configurația serverului este adăugată în fișierul global *settings.json* și este disponibilă în toate workspace-urile. Configurația arată similar cu următorul exemplu:

    ![Setare utilizator](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. De asemenea, trebuie să adăugați o configurație, un antet pentru a vă asigura că autentificarea către Azure API Management este corectă. Se folosește un antet denumit **Ocp-Apim-Subscription-Key**.

    - Iată cum îl puteți adăuga în setări:

    ![Adăugare antet pentru autentificare](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ceea ce va face să apară un prompt care vă cere valoarea cheii API pe care o puteți găsi în Portalul Azure pentru instanța Azure API Management.

   - Pentru a-l adăuga în *mcp.json*, îl puteți adăuga astfel:

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

### Folosește modul Agent

Acum suntem gata, fie în setări, fie în *.vscode/mcp.json*. Să-l încercăm.

Ar trebui să existe o pictogramă Tools astfel, unde uneltele expuse de serverul dvs. sunt listate:

![Unelte de la server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Faceți clic pe pictograma unelte și ar trebui să vedeți o listă de unelte astfel:

    ![Unelte](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Introduceți un prompt în chat pentru a invoca unealta. De exemplu, dacă ați selectat o unealtă pentru a obține informații despre o comandă, puteți întreba agentul despre o comandă. Iată un exemplu de prompt:

    ```text
    get information from order 2
    ```

    Veți vedea acum o pictogramă de unelte care vă întreabă dacă doriți să continuați apelând o unealtă. Selectați pentru a continua rularea uneltei, ar trebui să vedeți un rezultat astfel:

    ![Rezultat prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ceea ce vedeți mai sus depinde de uneltele pe care le-ați configurat, dar ideea este că primiți un răspuns textual ca cel de mai sus**


## Referințe

Iată cum puteți afla mai multe:

- [Tutorial despre Azure API Management și MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Exemplu Python: Securizarea serverelor MCP remote folosind Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laborator autorizare client MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Folosește extensia Azure API Management pentru VS Code pentru importarea și gestionarea API-urilor](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Înregistrarea și descoperirea serverelor MCP remote în Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Repo excelent ce arată multe capabilități AI cu Azure API Management
- [Ateliere AI Gateway](https://azure-samples.github.io/AI-Gateway/) Conține ateliere folosind Portalul Azure, o metodă excelentă de a începe evaluarea capabilităților AI.

## Ce urmează

- Înapoi la: [Prezentarea Studiilor de caz](./README.md)
- Următorul: [Agenți de călătorie AI Azure](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->