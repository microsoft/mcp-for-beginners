# Avancerede emner i MCP

[![Avanceret MCP: Sikker, skalerbar og multimodal AI-agenter](../../../translated_images/da/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Klik på billedet ovenfor for at se videoen af denne lektion)_

Dette kapitel dækker en række avancerede emner i implementeringen af Model Context Protocol (MCP), herunder multimodal integration, skalerbarhed, sikkerhedsbedste praksis og virksomheds-integration. Disse emner er afgørende for at opbygge robuste og produktionsklare MCP-applikationer, der kan imødekomme kravene i moderne AI-systemer.

## Oversigt

Denne lektion udforsker avancerede koncepter i implementeringen af Model Context Protocol med fokus på multimodal integration, skalerbarhed, sikkerhedsbedste praksis og virksomheds-integration. Disse emner er vigtige for at opbygge produktionsegnede MCP-applikationer, der kan håndtere komplekse krav i virksomhedsmiljøer.

## Læringsmål

Ved slutningen af denne lektion vil du kunne:

- Implementere multimodale kapaciteter inden for MCP-rammeværk
- Designe skalerbare MCP-arkitekturer til scenarier med høj efterspørgsel
- Anvende sikkerhedsbedste praksis i overensstemmelse med MCP’s sikkerhedsprincipper
- Integrere MCP med virksomheders AI-systemer og rammeværk
- Optimere ydeevne og pålidelighed i produktionsmiljøer

## Lektioner og eksempler på projekter

| Link | Titel | Beskrivelse |
|------|-------|-------------|
| [5.1 Integration med Azure](./mcp-integration/README.md) | Integrer med Azure | Lær hvordan du integrerer din MCP-server på Azure |
| [5.2 Multimodalt eksempel](./mcp-multi-modality/README.md) | MCP multimodale eksempler | Eksempler for lyd, billede og multimodale svar |
| [5.3 MCP OAuth2 eksempel](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimal Spring Boot-app der viser OAuth2 med MCP, både som autorisations- og ressource-server. Demonstrerer sikker token-udstedelse, beskyttede slutpunkter, Azure Container Apps-distribution og API Management-integration. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Root-kontekster | Lær mere om root-kontekst og hvordan man implementerer dem |
| [5.5 Routing](./mcp-routing/README.md) | Routing | Lær forskellige typer routing |
| [5.6 Sampling](./mcp-sampling/README.md) | Sampling | Lær hvordan man arbejder med sampling |
| [5.7 Scaling](./mcp-scaling/README.md) | Skalering | Lær om skalering |
| [5.8 Security](./mcp-security/README.md) | Sikkerhed | Sikr din MCP-server |
| [5.9 Web Search eksempel](./web-search-mcp/README.md) | Web Search MCP | Python MCP-server og klient der integrerer med SerpAPI for realtidsweb-, nyheds-, produkt-søgning og Q&A. Demonstrerer multi-tool orkestrering, ekstern API-integration og robust fejlhåndtering. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming | Realtidsdatastreaming er blevet essentielt i dagens datadrevne verden, hvor virksomheder og applikationer kræver øjeblikkelig adgang til information for at træffe rettidige beslutninger. |
| [5.11 Realtids Web Search](./mcp-realtimesearch/README.md) | Web Search | Realtids web-søgning og hvordan MCP transformer realtids web-søgning ved at tilbyde en standardiseret tilgang til kontekststyring på tværs af AI-modeller, søgemaskiner og applikationer. |
| [5.12 Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID Authentication | Microsoft Entra ID leverer en robust cloud-baseret identitets- og adgangsstyringsløsning, der hjælper med at sikre, at kun autoriserede brugere og applikationer kan interagere med din MCP-server. |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry Integration | Lær hvordan man integrerer Model Context Protocol-servere med Azure AI Foundry-agenter, hvilket muliggør kraftfuld tool-orkestrering og virksomheders AI-funktioner med standardiserede tilslutninger til eksterne datakilder. |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Kontext Engineering | Fremtidige muligheder for kontekstteknikker til MCP-servere, herunder kontekstoptimering, dynamisk kontekststyring og strategier for effektiv promptengineering inden for MCP-rammeværk. |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Brugerdefineret transport | Lær hvordan du implementerer brugerdefinerede transportmekanismer til specialiserede MCP-kommunikationsscenarier. |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Protokolfunktioner | Mestrer avancerede protokolfunktioner inklusive fremdriftsnotifikationer, anmodningsaflysning, ressourcetemplater og fejlhåndteringsmønstre. |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Adversarielle agenter | Brug to agenter med modstridende holdninger, som deler et enkelt MCP-værktøjssæt, til at fange hallucinationer, afdække kanttilfælde og producere bedre kalibrerede output gennem struktureret debat. |

> **Ny i MCP Specification 2025-11-25**: Specifikationen inkluderer nu eksperimentel understøttelse af **Tasks** (langvarige operationer med fremdriftssporing), **Tool Annotations** (metadata om værktøjets adfærd for sikkerhed), **URL Mode Elicitation** (anmodning om specifikt URL-indhold fra klienter) og forbedrede **Roots** (til arbejdsområdets kontekststyring). Se [MCP Specification changelog](https://spec.modelcontextprotocol.io/) for fulde detaljer.

## Yderligere referencer

For de mest opdaterede oplysninger om avancerede MCP-emner, henvis til:
- [MCP Dokumentation](https://modelcontextprotocol.io/)
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Sikkerhedsrisici og mitigeringer
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktisk sikkerhedstræning

## Vigtigste pointer

- Multimodale MCP-implementeringer udvider AI-kapaciteter ud over tekstbehandling
- Skalerbarhed er essentielt for virksomhedsudrulninger og kan adresseres gennem horisontal og vertikal skalering
- Omfattende sikkerhedsforanstaltninger beskytter data og sikrer korrekt adgangskontrol
- Virksomhedsintegration med platforme som Azure OpenAI og Microsoft AI Foundry forbedrer MCP-kapaciteter
- Avancerede MCP-implementeringer drager fordel af optimerede arkitekturer og omhyggelig ressourcehåndtering

## Øvelse

Design en virksomhedsklar MCP-implementering til et specifikt brugstilfælde:

1. Identificer multimodale krav for dit brugstilfælde
2. Skitser sikkerhedskontroller, der er nødvendige for at beskytte følsomme data
3. Design en skalerbar arkitektur, der kan håndtere varierende belastning
4. Planlæg integrationspunkter med virksomheders AI-systemer
5. Dokumenter potentielle præstationsflaskehalse og afbødningsstrategier

## Ekstra ressourcer

- [Azure OpenAI Dokumentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry Dokumentation](https://learn.microsoft.com/en-us/ai-services/)

---

## Hvad er det næste

Udforsk lektionerne i denne modul startende med: [5.1 MCP Integration](./mcp-integration/README.md)

Når du har gennemført dette modul, fortsæt til: [Modul 6: Community Contributions](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->