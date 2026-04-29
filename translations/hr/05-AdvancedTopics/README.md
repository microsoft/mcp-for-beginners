# Napredne teme u MCP-u

[![Napredni MCP: Sigurni, skalabilni i multimodalni AI agenti](../../../translated_images/hr/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Kliknite na sliku iznad za pregled videa ove lekcije)_

Ovo poglavlje pokriva niz naprednih tema u implementaciji protokola Model Context Protocol (MCP), uključujući multimodalnu integraciju, skalabilnost, najbolje sigurnosne prakse i integraciju u poduzećima. Ove teme su ključne za izgradnju robusnih i spremnih za produkciju MCP aplikacija koje mogu ispuniti zahtjeve modernih AI sustava.

## Pregled

Ova lekcija istražuje napredne koncepte u implementaciji Model Context Protocola, s naglaskom na multimodalnu integraciju, skalabilnost, najbolje sigurnosne prakse i integraciju u poduzećima. Ove teme su bitne za izradu MCP aplikacija proizvodne kvalitete koje mogu podnijeti složene zahtjeve u poslovnim okruženjima.

## Ciljevi učenja

Do kraja ove lekcije moći ćete:

- Implementirati multimodalne sposobnosti unutar MCP okvira
- Dizajnirati skalabilne MCP arhitekture za scenarije s velikom potražnjom
- Primijeniti najbolje sigurnosne prakse usklađene s MCP sigurnosnim principima
- Integrirati MCP sa sustavima za AI u poduzećima i njihovim okvirima
- Optimizirati performanse i pouzdanost u produkcijskim okruženjima

## Lekcije i primjeri projekata

| Link | Naslov | Opis |
|------|--------|-------|
| [5.1 Integracija s Azure](./mcp-integration/README.md) | Integracija s Azure | Naučite kako integrirati vaš MCP Server na Azure |
| [5.2 Primjer multimodalnosti](./mcp-multi-modality/README.md) | MCP primjeri multimodalnosti | Primjeri za audio, sliku i multimodalne odgovore |
| [5.3 MCP OAuth2 primjer](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimalna Spring Boot aplikacija koja pokazuje OAuth2 s MCP, kao i Authorization i Resource Server. Demonstrira sigurnu izdaju tokena, zaštićene krajnje točke, Azure Container Apps implementaciju i integraciju upravljanja API-jem. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Root konteksti | Saznajte više o root kontekstu i kako ga implementirati |
| [5.5 Routing](./mcp-routing/README.md) | Usmjeravanje | Naučite različite vrste usmjeravanja |
| [5.6 Sampling](./mcp-sampling/README.md) | Uzorkovanje | Naučite kako raditi s uzorkovanjem |
| [5.7 Skaliranje](./mcp-scaling/README.md) | Skaliranje | Naučite o skaliranju |
| [5.8 Sigurnost](./mcp-security/README.md) | Sigurnost | Osigurajte svoj MCP Server |
| [5.9 Web Search MCP](./web-search-mcp/README.md) | Web pretraživanje MCP | Python MCP server i klijent integrirani sa SerpAPI-jem za pretraživanje weba, vijesti, proizvoda i Q&A u stvarnom vremenu. Demonstrira orkestraciju više alata, integraciju s vanjskim API-jem i robusno rukovanje pogreškama. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming | Streaming podataka u stvarnom vremenu postao je ključan u današnjem svijetu vođenom podacima, gdje posao i aplikacije zahtijevaju trenutni pristup informacijama za pravovremene odluke.|
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Web pretraživanje | Kako MCP transformira pretraživanje weba u stvarnom vremenu pružajući standardizirani pristup upravljanju kontekstom kroz AI modele, tražilice i aplikacije.|
| [5.12 Entra ID autentikacija za MCP servere](./mcp-security-entra/README.md) | Entra ID autentikacija | Microsoft Entra ID pruža robusno rješenje za upravljanje identitetom i pristupom u oblaku, pomažući osigurati da samo ovlašteni korisnici i aplikacije mogu komunicirati s vašim MCP serverom.|
| [5.13 Integracija Azure AI Foundry agenta](./mcp-foundry-agent-integration/README.md) | Integracija Azure AI Foundry | Naučite kako integrirati MCP servere s Azure AI Foundry agentima, omogućujući moćnu orkestraciju alata i AI mogućnosti za poduzeća sa standardiziranim vezama prema vanjskim izvorima podataka.|
| [5.14 Inženjering konteksta](./mcp-contextengineering/README.md) | Inženjering konteksta | Buduće mogućnosti kontekstnog inženjeringa za MCP servere, uključujući optimizaciju konteksta, dinamičko upravljanje kontekstom i strategije za učinkovito inženjerstvo promptova unutar MCP okvira.|
| [5.15 MCP prilagođeni transport](./mcp-transport/README.md) | Prilagođeni transport | Naučite kako implementirati prilagođene transportne mehanizme za specijalizirane komunikacijske scenarije MCP-a.|
| [5.16 Dubinska analiza značajki protokola](./mcp-protocol-features/README.md) | Značajke protokola | Ovladavanje naprednim značajkama protokola uključujući obavijesti o napretku, otkazivanje zahtjeva, predloške resursa i obrasce rukovanja pogreškama.|
| [5.17 Antagonističko višagentsko rezoniranje](./mcp-adversarial-agents/README.md) | Antagonistički agenti | Koristite dva agenta s oprečnim stavovima, dijeleći jedan MCP skup alata, kako biste uhvatili halucinacije, iznijeli rubne slučajeve i proizveli bolje kalibrirane rezultate kroz strukturirane debate.|

> **Novo u MCP specifikaciji 2025-11-25**: specifikacija sada uključuje eksperimentalnu podršku za **Zadatke** (dugotrajne operacije s praćenjem napretka), **Bilješke o alatima** (metapodaci o ponašanju alata radi sigurnosti), **URL način ishođenja** (zahtijevanje specifičnog sadržaja URL-a od klijenata) i proširene **Korijene** (za upravljanje kontekstom radne površine). Pogledajte [MCP specifikacijsku evidenciju promjena](https://spec.modelcontextprotocol.io/) za potpune detalje.

## Dodatne reference

Za najsvježije informacije o naprednim MCP temama pogledajte:
- [MCP dokumentaciju](https://modelcontextprotocol.io/)
- [MCP specifikaciju (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub repozitorij](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Sigurnosni rizici i mjere ublažavanja
- [MCP Security Summit radionica (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktična sigurnosna obuka

## Ključne spoznaje

- Multimodalne implementacije MCP-a proširuju AI mogućnosti izvan obrade teksta
- Skalabilnost je ključna za implementacije u poduzećima i može se osigurati horizontalnim i vertikalnim skaliranjem
- Sveobuhvatne sigurnosne mjere štite podatke i osiguravaju pravilnu kontrolu pristupa
- Integracija u poduzećima s platformama poput Azure OpenAI i Microsoft AI Foundry povećava mogućnosti MCP-a
- Napredne MCP implementacije koriste optimizirane arhitekture i pažljivo upravljanje resursima

## Vježba

Dizajnirajte MCP implementaciju razine poduzeća za specifičnu poslovnu primjenu:

1. Identificirajte multimodalne zahtjeve za vaš slučaj upotrebe
2. Nacrtajte sigurnosne kontrole potrebne za zaštitu osjetljivih podataka
3. Dizajnirajte skalabilnu arhitekturu koja može podnijeti različita opterećenja
4. Planirajte integracijske točke sa sustavima za AI u poduzećima
5. Dokumentirajte potencijalne uska grla u performansama i strategije ublažavanja

## Dodatni resursi

- [Azure OpenAI dokumentacija](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry dokumentacija](https://learn.microsoft.com/en-us/ai-services/)

---

## Što slijedi

Istražite lekcije u ovom modulu počevši od: [5.1 MCP Integracija](./mcp-integration/README.md)

Nakon dovršetka ovog modula nastavite na: [Modul 6: Doprinosi zajednice](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o odricanju odgovornosti**:
Ovaj dokument preveden je pomoću AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili krive interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->