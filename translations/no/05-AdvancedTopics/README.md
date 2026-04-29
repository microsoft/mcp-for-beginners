# Avanserte emner i MCP

[![Avansert MCP: Sikker, skalerbar og multimodale AI-agenter](../../../translated_images/no/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Klikk på bildet over for å se video av denne leksjonen)_

Dette kapittelet dekker en rekke avanserte emner innen implementering av Model Context Protocol (MCP), inkludert multimodal integrasjon, skalerbarhet, sikkerhets beste praksis og bedriftsintegrasjon. Disse emnene er avgjørende for å bygge robuste og produksjonsklare MCP-applikasjoner som kan møte kravene i moderne AI-systemer.

## Oversikt

Denne leksjonen utforsker avanserte konsepter i implementering av Model Context Protocol, med fokus på multimodal integrasjon, skalerbarhet, sikkerhets beste praksis og bedriftsintegrasjon. Disse emnene er essensielle for å bygge produksjonskvalitets MCP-applikasjoner som kan håndtere komplekse krav i bedriftsmiljøer.

## Læringsmål

Ved slutten av denne leksjonen vil du kunne:

- Implementere multimodale kapabiliteter innen MCP-rammeverk
- Designe skalerbare MCP-arkitekturer for scenarier med høy etterspørsel
- Anvende sikkerhets beste praksis i tråd med MCPs sikkerhetsprinsipper
- Integrere MCP med bedrifts-AI-systemer og rammeverk
- Optimalisere ytelse og pålitelighet i produksjonsmiljøer

## Leksjoner og eksempelprosjekter

| Link | Tittel | Beskrivelse |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Integrer med Azure | Lær hvordan du integrerer din MCP-tjener på Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCP Multimodale eksempler  | Eksempler for lyd, bilde og multimodale svar |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimal Spring Boot-app som viser OAuth2 med MCP, både som autorisasjons- og ressursserver. Demonstrerer sikker tokenutstedelse, beskyttede endepunkter, distribusjon til Azure Container Apps og API Management-integrasjon. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Rotkontekster  | Lær mer om rotkontekst og hvordan implementere dem |
| [5.5 Routing](./mcp-routing/README.md) | Rutetypper | Lær forskjellige typer ruting |
| [5.6 Sampling](./mcp-sampling/README.md) | Sampling | Lær hvordan man jobber med sampling |
| [5.7 Scaling](./mcp-scaling/README.md) | Skalering  | Lær om skalering |
| [5.8 Security](./mcp-security/README.md) | Sikkerhet  | Sikre din MCP-tjener |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Web Search MCP | Python MCP-server og klient som integrerer med SerpAPI for sanntidssøk på web, nyheter, produkter og Q&A. Demonstrerer multi-verktøyorchestration, ekstern API-integrasjon og robust feilbehandling. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming  | Sanntids datastrømming har blitt essensielt i dagens datadrevne verden, hvor bedrifter og applikasjoner krever umiddelbar tilgang til informasjon for å ta tidsriktige beslutninger.|
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Websøk | Sanntidssøk på web: hvordan MCP transformerer sanntidssøk gjennom en standardisert tilnærming til kontekstbehandling på tvers av AI-modeller, søkemotorer og applikasjoner.| 
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID-autentisering | Microsoft Entra ID tilbyr en robust skybasert løsning for identitets- og tilgangsstyring som sikrer at kun autoriserte brukere og applikasjoner kan samhandle med din MCP-tjener.|
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry-integrasjon | Lær hvordan man integrerer Model Context Protocol-tjenere med Azure AI Foundry-agenter, noe som muliggjør kraftig verktøyorkestrering og bedrifts-AI-muligheter med standardiserte tilkoblinger til eksterne datakilder.|
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Konsteknikk | Fremtidige muligheter med konsteknikk for MCP-tjenere, inkludert kontekstoptimalisering, dynamisk kontekststyring og strategier for effektiv promptengineering innenfor MCP-rammeverk.|
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Egendefinert transport | Lær hvordan implementere egendefinerte transportmekanismer for spesialiserte MCP-kommunikasjonsscenarier.|
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Protokollfunksjoner | Mestre avanserte protokollfunksjoner som fremdriftsvarsler, kansellering av forespørsler, maleressurser og feilhåndteringsmønstre.|
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Adversarielle agenter | Bruk to agenter med motstridende posisjoner, som deler en enkelt MCP-verktøykasse, for å avdekke hallusinasjoner, avdekke yttertilfeller og produsere bedre kalibrerte resultater gjennom strukturert debatt.|

> **Ny i MCP-spesifikasjonen 2025-11-25**: Spesifikasjonen inkluderer nå eksperimentell støtte for **Tasks** (langvarige operasjoner med fremdriftssporing), **Tool Annotations** (metadata om verktøyadferd for sikkerhet), **URL Mode Elicitation** (forespørsel om spesifikt URL-innhold fra klienter) og forbedrede **Roots** (for styring av arbeidsområdekontekst). Se [MCP Specification changelog](https://spec.modelcontextprotocol.io/) for fullstendige detaljer.

## Ytterligere referanser

For den mest oppdaterte informasjonen om avanserte MCP-emner, se:
- [MCP Dokumentasjon](https://modelcontextprotocol.io/)
- [MCP Spesifikasjon (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [OWASP MCP Topp 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Sikkerhetsrisikoer og mottiltak
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktisk sikkerhetstrening

## Viktige punkter

- Multimodale MCP-implementeringer utvider AI-kapasiteter utover tekstbehandling
- Skalerbarhet er essensielt for bedriftsdistribusjoner og kan løses med horisontal og vertikal skalering
- Omfattende sikkerhetstiltak beskytter data og sikrer riktig tilgangskontroll
- Bedriftsintegrasjon med plattformer som Azure OpenAI og Microsoft AI Foundry forbedrer MCP-kapasiteter
- Avanserte MCP-implementeringer drar nytte av optimaliserte arkitekturer og nøye ressursstyring

## Øvelse

Design en MCP-implementering i bedriftsklasse for en spesifikk brukstilfelle:

1. Identifiser multimodale krav for ditt brukstilfelle
2. Skisser sikkerhetskontroller som trengs for å beskytte sensitive data
3. Design en skalerbar arkitektur som kan håndtere varierende belastning
4. Planlegg integrasjonspunkter med bedrifts-AI-systemer
5. Dokumenter potensielle ytelsesflaskehalser og strategier for mitigering

## Ekstra ressurser

- [Azure OpenAI Dokumentasjon](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry Dokumentasjon](https://learn.microsoft.com/en-us/ai-services/)

---

## Hva er neste

Utforsk leksjonene i denne modulen med start på: [5.1 MCP Integration](./mcp-integration/README.md)

Når du er ferdig med denne modulen, fortsett til: [Modul 6: Community Contributions](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet har blitt oversatt ved hjelp av AI-oversettingstjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->