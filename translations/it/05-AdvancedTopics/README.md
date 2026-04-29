# Argomenti avanzati in MCP

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/it/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Fai clic sull'immagine sopra per vedere il video di questa lezione)_

Questo capitolo tratta una serie di argomenti avanzati nell'implementazione del Model Context Protocol (MCP), inclusa l'integrazione multi-modale, la scalabilità, le migliori pratiche di sicurezza e l'integrazione aziendale. Questi temi sono fondamentali per costruire applicazioni MCP robuste e pronte per la produzione che possono soddisfare le esigenze dei sistemi di intelligenza artificiale moderni.

## Panoramica

Questa lezione esplora concetti avanzati nell'implementazione del Model Context Protocol, concentrandosi sull'integrazione multi-modale, la scalabilità, le migliori pratiche di sicurezza e l'integrazione aziendale. Questi argomenti sono essenziali per costruire applicazioni MCP di livello produttivo che possono gestire requisiti complessi negli ambienti aziendali.

## Obiettivi di apprendimento

Al termine di questa lezione, sarai in grado di:

- Implementare capacità multi-modali all'interno dei framework MCP
- Progettare architetture MCP scalabili per scenari ad alta richiesta
- Applicare le migliori pratiche di sicurezza in linea con i principi di sicurezza di MCP
- Integrare MCP con sistemi e framework AI aziendali
- Ottimizzare le prestazioni e l'affidabilità negli ambienti di produzione

## Lezioni e progetti di esempio

| Link | Titolo | Descrizione |
|------|--------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Integrazione con Azure | Impara come integrare il tuo MCP Server su Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | Esempi MCP Multi-modale | Esempi per audio, immagini e risposte multi-modali |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | Demo MCP OAuth2 | Applicazione Spring Boot minima che mostra OAuth2 con MCP, sia come Authorization che Resource Server. Dimostra l'emissione sicura dei token, endpoint protetti, distribuzione su Azure Container Apps e integrazione con API Management. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Contesti radice | Approfondisci i contesti radice e come implementarli |
| [5.5 Routing](./mcp-routing/README.md) | Routing | Impara i diversi tipi di routing |
| [5.6 Sampling](./mcp-sampling/README.md) | Campionamento | Impara come lavorare con il campionamento |
| [5.7 Scaling](./mcp-scaling/README.md) | Scalabilità | Impara a scalare |
| [5.8 Security](./mcp-security/README.md) | Sicurezza | Proteggi il tuo MCP Server |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Ricerca Web MCP | Server e client MCP Python che integrano SerpAPI per ricerca web, notizie, prodotti e Q&A in tempo reale. Dimostra orchestrazione multi-tool, integrazione di API esterne e gestione robusta degli errori. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming | Lo streaming di dati in tempo reale è diventato essenziale nel mondo odierno orientato ai dati, dove aziende e applicazioni richiedono accesso immediato alle informazioni per prendere decisioni tempestive. |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Ricerca Web | Come MCP trasforma la ricerca web in tempo reale fornendo un approccio standardizzato alla gestione del contesto tra modelli AI, motori di ricerca e applicazioni. | 
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Autenticazione Entra ID | Microsoft Entra ID fornisce una soluzione robusta di gestione delle identità e degli accessi basata su cloud, aiutando a garantire che solo utenti e applicazioni autorizzati possano interagire con il tuo server MCP. |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Integrazione Azure AI Foundry | Impara come integrare i server Model Context Protocol con gli agenti Azure AI Foundry, abilitando potente orchestrazione di strumenti e capacità AI aziendali con connessioni standardizzate alle sorgenti dati esterne. |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Ingegneria del contesto | Opportunità future delle tecniche di ingegneria del contesto per i server MCP, inclusa l'ottimizzazione del contesto, la gestione dinamica del contesto e strategie per un efficace prompt engineering all'interno dei framework MCP. |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Trasporto Personalizzato | Impara come implementare meccanismi di trasporto personalizzati per scenari di comunicazione MCP specializzati. |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Funzionalità del Protocollo | Padroneggia funzionalità avanzate del protocollo tra cui notifiche di progresso, cancellazione delle richieste, template di risorse e modelli di gestione degli errori. |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Agenti avversari | Usa due agenti con posizioni opposte, condividendo un singolo set di strumenti MCP, per catturare allucinazioni, mettere in luce casi limite e produrre output meglio calibrati attraverso un dibattito strutturato. |

> **Novità nella specifica MCP 2025-11-25**: La specifica include ora il supporto sperimentale per **Tasks** (operazioni a lungo termine con tracciamento del progresso), **Annotazioni degli Strumenti** (metadata sul comportamento degli strumenti per la sicurezza), **Elicitazione in Modalità URL** (richiesta di contenuti URL specifici dai client) e **Radici** migliorate (per la gestione del contesto degli spazi di lavoro). Vedi il [registro delle modifiche della specifica MCP](https://spec.modelcontextprotocol.io/) per i dettagli completi.

## Riferimenti aggiuntivi

Per le informazioni più aggiornate sugli argomenti avanzati MCP, consulta:
- [Documentazione MCP](https://modelcontextprotocol.io/)
- [Specifiche MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Repository GitHub](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Rischi di sicurezza e mitigazioni
- [Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Formazione pratica sulla sicurezza

## Punti chiave

- Le implementazioni MCP multi-modali estendono le capacità AI oltre l'elaborazione del testo
- La scalabilità è essenziale per le distribuzioni aziendali e può essere affrontata tramite scalabilità orizzontale e verticale
- Misure di sicurezza complete proteggono i dati e garantiscono un controllo corretto degli accessi
- L'integrazione aziendale con piattaforme come Azure OpenAI e Microsoft AI Foundry potenzia le capacità MCP
- Le implementazioni MCP avanzate beneficiano di architetture ottimizzate e gestione attenta delle risorse

## Esercizio

Progetta un'implementazione MCP di livello aziendale per un caso d'uso specifico:

1. Identifica i requisiti multi-modali per il tuo caso d'uso
2. Delinea i controlli di sicurezza necessari per proteggere i dati sensibili
3. Progetta un'architettura scalabile in grado di gestire carichi variabili
4. Pianifica i punti di integrazione con i sistemi AI aziendali
5. Documenta i potenziali colli di bottiglia nelle prestazioni e le strategie di mitigazione

## Risorse aggiuntive

- [Documentazione Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Documentazione Microsoft AI Foundry](https://learn.microsoft.com/en-us/ai-services/)

---

## Cosa c'è dopo

Esplora le lezioni di questo modulo iniziando da: [5.1 MCP Integration](./mcp-integration/README.md)

Una volta completato questo modulo, passa a: [Modulo 6: Contributi della Comunità](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua originale deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->