## Începeți  

[![Construiți primul server MCP](../../../translated_images/ro/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.png)](https://youtu.be/sNDZO9N4m9Y)

_(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

Această secțiune constă din mai multe lecții:

- **1 Primul server**, în această primă lecție, veți învăța cum să creați primul server și să îl inspectați cu instrumentul de inspecție, o metodă valoroasă pentru testarea și depanarea serverului, [către lecție](01-first-server/README.md)

- **2 Client**, în această lecție, veți învăța cum să scrieți un client care se poate conecta la serverul dvs., [către lecție](02-client/README.md)

- **3 Client cu LLM**, o metodă și mai bună de a scrie un client este prin adăugarea unui LLM, astfel încât acesta să poată "negocia" cu serverul dvs. despre ce să facă, [către lecție](03-llm-client/README.md)

- **4 Consumarea unui server în modul GitHub Copilot Agent în Visual Studio Code**. Aici, vom analiza rularea serverului MCP din Visual Studio Code, [către lecție](04-vscode/README.md)

- **5 Server Transport stdio**. Transportul stdio este standardul recomandat pentru comunicarea server-client MCP în specificația actuală, oferind o comunicare sigură bazată pe subprocess, [către lecție](05-stdio-server/README.md)

- **6 Streaming HTTP cu MCP (HTTP Streamable)**. Aflați despre streamingul HTTP modern, notificările de progres și cum să implementați servere și clienți MCP scalabili, în timp real, utilizând HTTP Streamable, [către lecție](06-http-streaming/README.md)

- **7 Utilizarea AI Toolkit pentru VSCode** pentru a consuma și testa clienții și serverele MCP, [către lecție](07-aitk/README.md)

- **8 Testare**. Aici ne vom concentra în special pe modul în care putem testa serverul și clientul în diferite moduri, [către lecție](08-testing/README.md)

- **9 Implementare**. Acest capitol va analiza diferite moduri de a implementa soluțiile MCP, [către lecție](09-deployment/README.md)

- **10 Utilizare avansată a serverului**. Acest capitol acoperă utilizarea avansată a serverului, [către lecție](./10-advanced/README.md)

- **11 Autentificare**. Acest capitol acoperă cum să adăugați autentificare simplă, de la Basic Auth la utilizarea JWT și RBAC. Sunteți încurajat să începeți aici și apoi să analizați subiectele avansate din capitolul 5 și să efectuați măsuri suplimentare de securizare conform recomandărilor din capitolul 2, [către lecție](./11-simple-auth/README.md)

Protocolul Model Context (MCP) este un protocol deschis care standardizează modul în care aplicațiile oferă context LLM-urilor. Gândiți-vă la MCP ca la un port USB-C pentru aplicațiile AI - oferă o modalitate standardizată de a conecta modelele AI la diferite surse de date și instrumente.

## Obiective de învățare

Până la sfârșitul acestei lecții, veți putea:

- Configura medii de dezvoltare pentru MCP în C#, Java, Python, TypeScript și JavaScript
- Construi și implementa servere MCP de bază cu funcții personalizate (resurse, prompturi și instrumente)
- Crea aplicații gazdă care se conectează la serverele MCP
- Testa și depana implementările MCP
- Înțelege provocările comune de configurare și soluțiile acestora
- Conecta implementările MCP la servicii populare LLM

## Configurarea mediului MCP

Înainte de a începe să lucrați cu MCP, este important să pregătiți mediul de dezvoltare și să înțelegeți fluxul de lucru de bază. Această secțiune vă va ghida prin pașii inițiali de configurare pentru a asigura un început fără probleme cu MCP.

### Cerințe preliminare

Înainte de a începe dezvoltarea MCP, asigurați-vă că aveți:

- **Mediu de dezvoltare**: Pentru limbajul ales (C#, Java, Python, TypeScript sau JavaScript)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm sau orice editor modern de cod
- **Manageri de pachete**: NuGet, Maven/Gradle, pip sau npm/yarn
- **Chei API**: Pentru orice servicii AI pe care intenționați să le utilizați în aplicațiile gazdă

### SDK-uri oficiale

În capitolele următoare veți vedea soluții construite folosind Python, TypeScript, Java și .NET. Iată toate SDK-urile oficiale suportate.

MCP oferă SDK-uri oficiale pentru mai multe limbaje:
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Menținut în colaborare cu Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Menținut în colaborare cu Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Implementarea oficială TypeScript
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Implementarea oficială Python
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Implementarea oficială Kotlin
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Menținut în colaborare cu Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Implementarea oficială Rust

## Concluzii cheie

- Configurarea unui mediu de dezvoltare MCP este simplă cu SDK-uri specifice limbajului
- Construirea serverelor MCP implică crearea și înregistrarea instrumentelor cu scheme clare
- Clienții MCP se conectează la servere și modele pentru a valorifica capacități extinse
- Testarea și depanarea sunt esențiale pentru implementări MCP fiabile
- Opțiunile de implementare variază de la dezvoltare locală la soluții bazate pe cloud

## Practică

Avem un set de exemple care completează exercițiile pe care le veți vedea în toate capitolele din această secțiune. În plus, fiecare capitol are propriile exerciții și sarcini.

- [Calculator Java](./samples/java/calculator/README.md)
- [Calculator .Net](../../../03-GettingStarted/samples/csharp)
- [Calculator JavaScript](./samples/javascript/README.md)
- [Calculator TypeScript](./samples/typescript/README.md)
- [Calculator Python](../../../03-GettingStarted/samples/python)

## Resurse suplimentare

- [Construiți agenți folosind Model Context Protocol pe Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [MCP Remote cu Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [Agent MCP OpenAI .NET](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Ce urmează

Următorul: [Crearea primului server MCP](01-first-server/README.md)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.