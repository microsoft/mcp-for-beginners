# Subiecte Avansate în MCP

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/ro/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

Acest capitol acoperă o serie de subiecte avansate în implementarea Model Context Protocol (MCP), inclusiv integrarea multi-modală, scalabilitatea, cele mai bune practici de securitate și integrarea în întreprinderi. Aceste subiecte sunt esențiale pentru construirea unor aplicații MCP robuste și gata de producție care pot satisface cerințele sistemelor moderne de AI.

## Prezentare generală

Această lecție explorează concepte avansate în implementarea Model Context Protocol, concentrându-se pe integrarea multi-modală, scalabilitate, cele mai bune practici de securitate și integrarea în întreprinderi. Aceste subiecte sunt esențiale pentru construirea unor aplicații MCP de nivel de producție care pot gestiona cerințe complexe în mediile enterprise.

## Obiective de învățare

La finalul acestei lecții, vei putea:

- Implementa capabilități multi-modale în cadrul structurilor MCP
- Proiecta arhitecturi MCP scalabile pentru scenarii cu cerere ridicată
- Aplica cele mai bune practici de securitate aliniate cu principiile de securitate MCP
- Integra MCP cu sisteme și cadre AI enterprise
- Optimiza performanța și fiabilitatea în mediile de producție

## Lecții și proiecte exemplu

| Link | Titlu | Descriere |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Integrare cu Azure | Învață cum să integrezi Serverul tău MCP pe Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | Exemple MCP Multi modal | Exemple pentru răspunsuri audio, imagine și multimodale |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | Demo MCP OAuth2 | Aplicație minimă Spring Boot demonstrând OAuth2 cu MCP, atât ca Server de Autorizare, cât și ca Server de Resurse. Demonstrează emiterea securizată a token-urilor, endpointuri protejate, implementarea în Azure Container Apps și integrarea cu API Management. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Contexte rădăcină | Află mai multe despre contextul rădăcină și cum să îl implementezi |
| [5.5 Routing](./mcp-routing/README.md) | Rutare | Învață diferite tipuri de rutare |
| [5.6 Sampling](./mcp-sampling/README.md) | Eșantionare | Învață cum să lucrezi cu eșantionarea |
| [5.7 Scaling](./mcp-scaling/README.md) | Scalare | Învață despre scalare |
| [5.8 Security](./mcp-security/README.md) | Securitate | Asigură securitatea Serverului tău MCP |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Căutare Web MCP | Server și client MCP Python care integrează SerpAPI pentru căutare web, știri, produse și Q&A în timp real. Demonstrează orchestrarea mai multor instrumente, integrarea API extern, și gestionarea robustă a erorilor. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming | Streaming de date în timp real a devenit esențial în lumea orientată pe date din prezent, unde business-urile și aplicațiile necesită acces imediat la informații pentru a lua decizii în timp util. |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Căutare Web | Căutare web în timp real – cum MCP transformă căutarea web în timp real prin furnizarea unei abordări standardizate pentru gestionarea contextului între modele AI, motoare de căutare și aplicații. |
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Autentificare Entra ID | Microsoft Entra ID oferă o soluție solidă de gestionare a identității și accesului bazată pe cloud, ajutând la asigurarea faptului că doar utilizatorii și aplicațiile autorizate pot interacționa cu serverul tău MCP. |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Integrare Azure AI Foundry | Învață cum să integrezi serverele Model Context Protocol cu agenții Azure AI Foundry, permițând orchestrarea puternică a instrumentelor și capabilități AI enterprise cu conexiuni standardizate la surse externe de date. |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Ingineria Contextului | Oportunitatea viitoare a tehnicilor de inginerie a contextului pentru serverele MCP, inclusiv optimizarea contextului, gestionarea dinamică a contextului și strategii pentru o inginerie efectivă a prompturilor în cadrul structurilor MCP. |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Transport personalizat | Învață cum să implementezi mecanisme de transport personalizate pentru scenarii speciale de comunicare MCP. |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Funcții Protocol | Stăpânește funcții avansate ale protocolului incluzând notificări de progres, anularea cererilor, șabloane de resurse și modele de gestionare a erorilor. |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Agenți adversari | Folosește doi agenți cu poziții opuse, partajând un singur set de instrumente MCP, pentru a prinde halucinații, a evidenția cazuri excepționale și a produce rezultate mai bine calibrate prin dezbatere structurată. |

> **Noutăți în Specificația MCP 2025-11-25**: Specificația include acum suport experimental pentru **Task-uri** (operațiuni de durată lungă cu urmărirea progresului), **Anotări ale Instrumentelor** (metadate despre comportamentul instrumentului pentru siguranță), **Elicitare Mod URL** (solicitarea de conținut specific URL de la clienți) și **Rădăcini** îmbunătățite (pentru gestionarea contextului spațiului de lucru). Vezi [istoricul modificărilor specificației MCP](https://spec.modelcontextprotocol.io/) pentru detalii complete.

## Referințe suplimentare

Pentru cele mai actualizate informații despre subiecte avansate MCP, consultă:
- [Documentația MCP](https://modelcontextprotocol.io/)
- [Specificația MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Repository GitHub](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Riscuri de securitate și măsuri de atenuare
- [Atelierul MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Instruire practică în securitate

## Concluzii cheie

- Implementările MCP multi-modale extind capabilitățile AI dincolo de procesarea textului
- Scalabilitatea este esențială pentru implementările enterprise și poate fi abordată prin scalare orizontală și verticală
- Măsurile cuprinzătoare de securitate protejează datele și asigură controlul corect al accesului
- Integrarea enterprise cu platforme ca Azure OpenAI și Microsoft AI Foundry îmbunătățește capabilitățile MCP
- Implementările avansate MCP beneficiază de arhitecturi optimizate și o gestionare atentă a resurselor

## Exercițiu

Proiectează o implementare MCP de nivel enterprise pentru un caz de utilizare specific:

1. Identifică cerințele multi-modale pentru cazul tău de utilizare
2. Schițează controalele de securitate necesare pentru protejarea datelor sensibile
3. Proiectează o arhitectură scalabilă care să poată gestiona sarcini variabile
4. Planifică punctele de integrare cu sistemele AI enterprise
5. Documentează eventualele blocaje de performanță și strategii de atenuare

## Resurse suplimentare

- [Documentația Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Documentația Microsoft AI Foundry](https://learn.microsoft.com/en-us/ai-services/)

---

## Următorul pas

Explorează lecțiile din acest modul începând cu: [5.1 MCP Integration](./mcp-integration/README.md)

După ce ai terminat acest modul, continuă cu: [Modulul 6: Contribuții Comunitare](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări eronate rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->