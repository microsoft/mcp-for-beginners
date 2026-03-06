# Implementare Practică

[![Cum să construiești, testezi și implementezi aplicații MCP cu unelte reale și fluxuri de lucru](../../../translated_images/ro/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Click pe imaginea de mai sus pentru a vedea videoclipul acestei lecții)_

Implementarea practică este locul unde puterea Model Context Protocol (MCP) devine tangibilă. Deși înțelegerea teoriei și arhitecturii din spatele MCP este importantă, valoarea reală apare atunci când aplici aceste concepte pentru a construi, testa și implementa soluții care rezolvă probleme reale. Acest capitol face legătura între cunoașterea conceptuală și dezvoltarea practică, ghidându-te prin procesul de aducere la viață a aplicațiilor bazate pe MCP.

Indiferent dacă dezvolți asistenți inteligenți, integrezi AI în fluxurile de lucru ale afacerii sau construiești instrumente personalizate pentru procesarea datelor, MCP oferă o fundație flexibilă. Designul său independent de limbaj și SDK-urile oficiale pentru limbaje de programare populare îl fac accesibil unui spectru larg de dezvoltatori. Folosind aceste SDK-uri, poți prototipa rapid, itera și scala soluțiile tale pe diverse platforme și medii.

În secțiunile următoare, vei găsi exemple practice, cod sursă și strategii de implementare care demonstrează cum să implementezi MCP în C#, Java cu Spring, TypeScript, JavaScript și Python. De asemenea, vei învăța cum să depanezi și să testezi serverele MCP, să gestionezi API-urile și să implementezi soluții în cloud folosind Azure. Aceste resurse hands-on sunt concepute pentru a accelera învățarea ta și pentru a te ajuta să construiești cu încredere aplicații MCP robuste, pregătite pentru producție.

## Prezentare Generală

Această lecție se concentrează pe aspectele practice ale implementării MCP în mai multe limbaje de programare. Vom explora cum să folosești SDK-urile MCP în C#, Java cu Spring, TypeScript, JavaScript și Python pentru a construi aplicații robuste, a depana și testa serverele MCP și a crea resurse, prompturi și unelte reutilizabile.

## Obiective de Învățare

La finalul acestei lecții, vei putea să:

- Implementezi soluții MCP folosind SDK-urile oficiale în diverse limbaje de programare
- Depanezi și testezi sistematic serverele MCP
- Creezi și folosești facilități ale serverului (Resurse, Prompturi și Unelte)
- Proiectezi fluxuri de lucru MCP eficiente pentru sarcini complexe
- Optimizezi implementările MCP pentru performanță și fiabilitate

## Resurse SDK Oficiale

Model Context Protocol oferă SDK-uri oficiale pentru mai multe limbaje (aliniate cu [Specificația MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [SDK C#](https://github.com/modelcontextprotocol/csharp-sdk)
- [SDK Java cu Spring](https://github.com/modelcontextprotocol/java-sdk) **Notă:** necesită dependență de [Project Reactor](https://projectreactor.io). (Vezi [discuția issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [SDK TypeScript](https://github.com/modelcontextprotocol/typescript-sdk)
- [SDK Python](https://github.com/modelcontextprotocol/python-sdk)
- [SDK Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk)
- [SDK Go](https://github.com/modelcontextprotocol/go-sdk)

## Lucrul cu SDK-urile MCP

Această secțiune oferă exemple practice de implementare MCP în mai multe limbaje de programare. Poți găsi coduri de exemplu în directorul `samples` organizate după limbaj.

### Exemple Disponibile

Repositorio-ul include [implementări de exemplu](../../../04-PracticalImplementation/samples) în următoarele limbaje:

- [C#](./samples/csharp/README.md)
- [Java cu Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Fiecare exemplu demonstrează concepte cheie MCP și modele de implementare pentru limbajul și ecosistemul respectiv.

### Ghiduri Practice

Ghiduri suplimentare pentru implementarea practică MCP:

- [Pagini și seturi mari de rezultate](./pagination/README.md) - Gestionarea paginării bazate pe cursor pentru unelte, resurse și seturi mari de date

## Funcționalități de Bază ale Serverului

Serverele MCP pot implementa orice combinație din aceste caracteristici:

### Resurse

Resursele oferă context și date pe care utilizatorul sau modelul AI le folosește:

- Repozitorii de documente
- Baze de cunoștințe
- Surse de date structurate
- Sisteme de fișiere

### Prompturi

Prompturile sunt mesaje și fluxuri de lucru șablon pentru utilizatori:

- Șabloane de conversație predefinite
- Modele ghidate de interacțiune
- Structuri specializate de dialog

### Unelte

Uneltele sunt funcții pe care modelul AI le poate executa:

- Utilitare de procesare date
- Integrări API externe
- Capacități computaționale
- Funcționalitate de căutare

## Implementări de Exemplu: Implementare în C#

Repositorio-ul oficial SDK C# conține mai multe implementări de exemplu care demonstrează diferite aspecte ale MCP:

- **Client MCP simplu**: Exemplu simplu care arată cum să creezi un client MCP și să apelezi unelte
- **Server MCP de bază**: Implementare minimă a serverului cu înregistrare de unelte de bază
- **Server MCP avansat**: Server complet cu înregistrare de unelte, autentificare și gestionare a erorilor
- **Integrare ASP.NET**: Exemple demonstrând integrarea cu ASP.NET Core
- **Modele de implementare a uneltelor**: Diverse modele pentru implementarea uneltelor cu diferite niveluri de complexitate

SDK-ul MCP C# este în previzualizare și API-urile pot suferi modificări. Vom actualiza continuu acest blog pe măsură ce SDK-ul evoluează.

### Caracteristici Cheie

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Construirea [primului tău Server MCP](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Pentru exemple complete de implementare în C#, vizitează [repositoriul oficial de exemple SDK C#](https://github.com/modelcontextprotocol/csharp-sdk)

## Implementare de Exemplu: Implementare Java cu Spring

SDK-ul Java cu Spring oferă opțiuni robuste de implementare MCP cu caracteristici enterprise.

### Caracteristici Cheie

- Integrare cu Spring Framework
- Siguranță puternică a tipurilor
- Suport pentru programare reactivă
- Gestionare cuprinzătoare a erorilor

Pentru un exemplu complet de implementare Java cu Spring, vezi [exemplul Java cu Spring](samples/java/containerapp/README.md) din directorul de exemple.

## Implementare de Exemplu: Implementare JavaScript

SDK-ul JavaScript oferă o abordare ușoară și flexibilă pentru implementarea MCP.

### Caracteristici Cheie

- Suport Node.js și browser
- API bazat pe promisiuni
- Integrare ușoară cu Express și alte framework-uri
- Suport WebSocket pentru streaming

Pentru un exemplu complet de implementare JavaScript, vezi [exemplul JavaScript](samples/javascript/README.md) din directorul de exemple.

## Implementare de Exemplu: Implementare Python

SDK-ul Python oferă o abordare Pythonică pentru implementarea MCP cu integrări excelente pentru framework-uri ML.

### Caracteristici Cheie

- Suport async/await cu asyncio
- Integrare FastAPI
- Înregistrare simplă a uneltelor
- Integrare nativă cu biblioteci ML populare

Pentru un exemplu complet de implementare Python, vezi [exemplul Python](samples/python/README.md) din directorul de exemple.

## Administrarea API-urilor

Azure API Management este o soluție excelentă pentru securizarea serverelor MCP. Ideea este să pui o instanță Azure API Management în fața serverului MCP și să o lași să gestioneze funcționalități pe care probabil le vei dori, precum:

- limitarea ratei
- managementul tokenurilor
- monitorizare
- echilibrare a încărcării
- securitate

### Exemplu Azure

Iată un exemplu Azure care face exact asta, adică [crearea unui server MCP și securizarea lui cu Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Vezi cum are loc fluxul de autorizare în imaginea de mai jos:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

În imaginea de mai sus, au loc următoarele:

- Autentificarea/Autorizarea se realizează folosind Microsoft Entra.
- Azure API Management acționează ca un gateway și folosește politici pentru a direcționa și gestiona traficul.
- Azure Monitor înregistrează toate cererile pentru analize ulterioare.

#### Fluxul de autorizare

Să aruncăm o privire mai detaliată asupra fluxului de autorizare:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Specificația autorizării MCP

Află mai multe despre [specificația de autorizare MCP](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Implementarea Serverului MCP Remote pe Azure

Să vedem dacă putem implementa exemplul menționat anterior:

1. Clonează repo-ul

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Înregistrează furnizorul de resurse `Microsoft.App`.

   - Dacă folosești Azure CLI, rulează `az provider register --namespace Microsoft.App --wait`.
   - Dacă folosești Azure PowerShell, rulează `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Apoi rulează `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` după un timp pentru a verifica dacă înregistrarea este completă.

1. Rulează această comandă [azd](https://aka.ms/azd) pentru a provisiona serviciul de management API, function app (cu cod) și toate celelalte resurse Azure necesare

    ```shell
    azd up
    ```

    Această comandă ar trebui să implementeze toate resursele cloud pe Azure

### Testarea serverului cu MCP Inspector

1. Într-o **fereastră de terminal nouă**, instalează și rulează MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Ar trebui să vezi o interfață asemănătoare cu:

    ![Connect to Node inspector](../../../translated_images/ro/connect.141db0b2bd05f096.webp)

1. CTRL click pentru a încărca aplicația web MCP Inspector de la URL-ul afișat de aplicație (exemplu [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Setează tipul de transport la `SSE`
1. Setează URL-ul către endpoint-ul SSE al Managementului API al serviciului tău afișat după `azd up` și **Conectează-te**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Listare Unelte**. Click pe o unealtă și **Rulează Unealta**.  

Dacă toate etapele au avut succes, acum ar trebui să fii conectat la serverul MCP și să fi putut apela o unealtă.

## Servere MCP pentru Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Acest set de repo-uri sunt template de start rapid pentru construirea și implementarea serverelor MCP remote personalizate folosind Azure Functions cu Python, C# .NET sau Node/TypeScript.

Exemplele oferă o soluție completă care le permite dezvoltatorilor să:

- Construiască și ruleze local: Dezvoltă și depanează un server MCP pe o mașină locală
- Implementează în Azure: Implementează ușor în cloud cu o simplă comandă azd up
- Conectează de pe clienți: Conectează-te la serverul MCP de pe diverse clienți, inclusiv modul agent Copilot din VS Code și uneltele MCP Inspector

### Caracteristici Cheie

- Securitate prin design: Serverul MCP este securizat folosind chei și HTTPS
- Opțiuni de autentificare: Suportă OAuth folosind autentificarea încorporată și/sau API Management
- Izolare de rețea: Permite izolarea rețelei folosind Azure Virtual Networks (VNET)
- Arhitectură serverless: Folosește Azure Functions pentru execuție scalabilă, eveniment-driven
- Dezvoltare locală: Suport cuprinzător pentru dezvoltare și depanare locală
- Implementare simplă: Proces simplificat de implementare pe Azure

Repositorio-ul include toate fișierele de configurare necesare, cod sursă și definiții de infrastructură pentru a începe rapid cu o implementare MCP pregătită pentru producție.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Implementare exemplu MCP folosind Azure Functions cu Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Implementare exemplu MCP folosind Azure Functions cu C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Implementare exemplu MCP folosind Azure Functions cu Node/TypeScript.

## Puncte Cheie

- SDK-urile MCP oferă unelte specifice limbajelor pentru implementarea soluțiilor MCP robuste
- Procesul de depanare și testare este esențial pentru aplicații MCP de încredere
- Șabloanele reutilizabile de prompturi permit interacțiuni AI consistente
- Fluxurile de lucru bine proiectate pot orchestra sarcini complexe folosind mai multe unelte
- Implementarea soluțiilor MCP necesită luarea în considerare a securității, performanței și gestionării erorilor

## Exercițiu

Proiectează un flux de lucru MCP practic care abordează o problemă reală din domeniul tău:

1. Identifică 3-4 unelte care ar fi utile pentru rezolvarea acestei probleme
2. Creează un diagram de flux care să arate cum interacționează aceste unelte
3. Implementează o versiune de bază a uneia dintre unelte folosind limbajul preferat
4. Creează un șablon de prompt care să ajute modelul să folosească eficient unealta ta

## Resurse Suplimentare

---

## Ce Urmează

Următorul capitol: [Subiecte Avansate](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat ca sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări eronate ce pot apărea ca urmare a utilizării acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->