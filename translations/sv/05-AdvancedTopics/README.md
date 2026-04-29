# Avancerade Ämnen i MCP

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/sv/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Klicka på bilden ovan för att se videon av denna lektion)_

Detta kapitel täcker en serie avancerade ämnen inom implementeringen av Model Context Protocol (MCP), inklusive multimodal integration, skalbarhet, säkerhetsbästa praxis och företagsintegration. Dessa ämnen är avgörande för att bygga robusta och produktionsklara MCP-applikationer som kan möta kraven från moderna AI-system.

## Översikt

Denna lektion utforskar avancerade koncept inom implementering av Model Context Protocol med fokus på multimodal integration, skalbarhet, säkerhetsbästa praxis och företagsintegration. Dessa ämnen är viktiga för att bygga produktionsfärdiga MCP-applikationer som kan hantera komplexa krav i företagsmiljöer.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Implementera multimodala funktioner inom MCP-ramverk
- Designa skalbara MCP-arkitekturer för högbelastningsscenarier
- Tillämpa säkerhetsbästa praxis i linje med MCP:s säkerhetsprinciper
- Integrera MCP med företags-AI-system och ramverk
- Optimera prestanda och tillförlitlighet i produktionsmiljöer

## Lektioner och exempelprojekt

| Länk | Titel | Beskrivning |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Integrera med Azure | Lär dig hur du integrerar din MCP-server på Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCP Multimodala exempel | Exempel för ljud, bild och multimodala svar |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimal Spring Boot-app som visar OAuth2 med MCP, både som auktoriserings- och resurserver. Demonstrerar säker tokenutfärdande, skyddade endpoints, distribution på Azure Container Apps och API Management-integration. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Root contexts | Lär dig mer om root context och hur man implementerar dem |
| [5.5 Routing](./mcp-routing/README.md) | Routing | Lär dig olika typer av routing |
| [5.6 Sampling](./mcp-sampling/README.md) | Sampling | Lär dig att arbeta med sampling |
| [5.7 Scaling](./mcp-scaling/README.md) | Skalning | Lär dig om skalning |
| [5.8 Security](./mcp-security/README.md) | Säkerhet | Säkerställ din MCP-server |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Web Search MCP | Python MCP-server och klient som integrerar med SerpAPI för realtidswebb-, nyhets-, produkt-sökning och Q&A. Demonstrerar multi-verktygsorkestrering, extern API-integration och robust felhantering. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming | Realtidsdataströmning har blivit avgörande i dagens databaserade värld där företag och applikationer kräver omedelbar tillgång till information för att fatta snabba beslut. |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Web Search | Realtidswebbsökning och hur MCP förvandlar realtidswebbsök genom att erbjuda ett standardiserat tillvägagångssätt för kontexthantering över AI-modeller, sökmotorer och applikationer. |
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID Authentication | Microsoft Entra ID erbjuder en robust molnbaserad identitets- och åtkomsthanteringslösning som säkerställer att endast auktoriserade användare och applikationer kan interagera med din MCP-server. |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry Integration | Lär dig hur du integrerar Model Context Protocol-servrar med Azure AI Foundry-agenter, vilket möjliggör kraftfull verktygsorkestrering och företags-AI-funktioner med standardiserade externa datakällkopplingar. |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Context Engineering | Framtida möjligheter inom kontextteknik för MCP-servrar, inklusive kontextoptimering, dynamisk kontexthantering och strategier för effektiv promptutformning inom MCP-ramverk. |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Custom Transport | Lär dig hur du implementerar kundanpassade transportmekanismer för specialiserade MCP-kommunikationsscenarier. |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Protocol Features | Bemästra avancerade protokollfunktioner inklusive framstegsaviseringar, avbokning av förfrågningar, resursmallar och felhanteringsmönster. |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Adversarial Agents | Använd två agenter med motsatta positioner som delar en enda MCP-verktygssats för att upptäcka hallucinationer, framhäva kantfall och producera bättre kalibrerade resultat genom strukturerad debatt. |

> **Nytt i MCP-specifikationen 2025-11-25**: Specifikationen inkluderar nu experimentellt stöd för **Tasks** (långvariga operationer med framstegsuppföljning), **Tool Annotations** (metadata om verktygsbeteende för säkerhet), **URL Mode Elicitation** (begäran om specifikt URL-innehåll från klienter) och förbättrade **Roots** (för hantering av arbetsytans kontext). Se [MCP Specification changelog](https://spec.modelcontextprotocol.io/) för fullständiga detaljer.

## Ytterligare Referenser

För den mest aktuella informationen om avancerade MCP-ämnen, se:
- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Säkerhetsrisker och motåtgärder
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktisk säkerhetsträning

## Viktiga Insikter

- Multimodala MCP-implementationer utökar AI:s kapabiliteter bortom textbearbetning
- Skalbarhet är nödvändig för företagsdistribueringar och kan hanteras genom horisontell och vertikal skalning
- Omfattande säkerhetsåtgärder skyddar data och säkerställer korrekt åtkomstkontroll
- Företagsintegration med plattformar som Azure OpenAI och Microsoft AI Foundry förbättrar MCP-funktioner
- Avancerade MCP-implementationer gynnas av optimerade arkitekturer och noggrann resursförvaltning

## Övning

Designa en företagsklassad MCP-implementation för ett specifikt användningsfall:

1. Identifiera multimodala krav för ditt användningsfall
2. Skissera säkerhetskontroller som krävs för att skydda känslig data
3. Designa en skalbar arkitektur som kan hantera varierande belastning
4. Planera integrationspunkter med företags-AI-system
5. Dokumentera potentiella prestandaflaskhalsar och åtgärdsstrategier

## Ytterligare Resurser

- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry Documentation](https://learn.microsoft.com/en-us/ai-services/)

---

## Vad är nästa

Utforska lektionerna i denna modul med start från: [5.1 MCP Integration](./mcp-integration/README.md)

När du har slutfört denna modul, fortsätt till: [Modul 6: Community Contributions](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig observera att automatiska översättningar kan innehålla fel eller inkonsekvenser. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->