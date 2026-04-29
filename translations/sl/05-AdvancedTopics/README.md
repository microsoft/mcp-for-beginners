# Napredne teme v MCP

[![Napredni MCP: Varnostni, razširljivi in večmodalni AI agenti](../../../translated_images/sl/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Kliknite zgornjo sliko za ogled videa te lekcije)_

To poglavje zajema vrsto naprednih tem pri implementaciji Model Context Protocol (MCP), vključno z večmodalno integracijo, razširljivostjo, najboljšimi praksami za varnost in integracijo v podjetja. Te teme so ključne za gradnjo robustnih in produkcijsko pripravljenih MCP aplikacij, ki lahko izpolnijo zahteve sodobnih AI sistemov.

## Pregled

Ta lekcija raziskuje napredne koncepte implementacije Model Context Protocol, s poudarkom na večmodalni integraciji, razširljivosti, najboljših varnostnih praksah in integraciji v podjetja. Te teme so bistvene za gradnjo MCP aplikacij proizvodne kakovosti, ki lahko obvladujejo kompleksne zahteve v poslovnih okoljih.

## Cilji učenja

Do konca te lekcije boste:

- Implementirali večmodalne zmogljivosti znotraj MCP okvirov
- Oblikovali razširljive MCP arhitekture za scenarije z velikim povpraševanjem
- Uporabljali najboljše varnostne prakse v skladu z varnostnimi načeli MCP
- Integrirali MCP s podjetniškimi AI sistemi in okviri
- Optimizirali zmogljivost in zanesljivost v produkcijskem okolju

## Lekcije in vzorčni projekti

| Povezava | Naslov | Opis |
|------|-------|-------------|
| [5.1 Integracija z Azure](./mcp-integration/README.md) | Integracija z Azure | Naučite se, kako integrirati vaš MCP strežnik na Azure |
| [5.2 Večmodalni primer](./mcp-multi-modality/README.md) | MCP večmodalni primeri  | Primeri za avdio, sliko in večmodalne odzive |
| [5.3 MCP OAuth2 primer](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimalna Spring Boot aplikacija, ki prikazuje OAuth2 z MCP, kot avtorizacijski in virni strežnik. Prikazuje varno izdajo žetonov, zaščitene končne točke, uvajanje Azure Container Apps in integracijo upravljanja API-jev. |
| [5.4 Glavni konteksti](./mcp-root-contexts/README.md) | Glavni konteksti  | Naučite se več o glavnem kontekstu in kako ga implementirati |
| [5.5 Usmerjanje](./mcp-routing/README.md) | Usmerjanje | Spoznajte različne vrste usmerjanja |
| [5.6 Vzorečenje](./mcp-sampling/README.md) | Vzorečenje | Naučite se, kako delati z vzorečenjem |
| [5.7 Razširjanje](./mcp-scaling/README.md) | Razširjanje  | Spoznajte razširjanje |
| [5.8 Varnost](./mcp-security/README.md) | Varnost  | Zavarujte vaš MCP strežnik |
| [5.9 MCP spletno iskanje](./web-search-mcp/README.md) | MCP spletno iskanje | Python MCP strežnik in odjemalec, integriran s SerpAPI za iskanje po spletu, novicah, izdelkih in Q&A v realnem času. Prikazuje upravljanje več orodij, integracijo zunanjih API-jev in robustno obravnavo napak. |
| [5.10 Prenos v realnem času](./mcp-realtimestreaming/README.md) | Pretakanje  | Pretakanje podatkov v realnem času je postalo bistveno v današnjem svetu, ki temelji na podatkih, kjer podjetja in aplikacije zahtevajo takojšen dostop do informacij za pravočasno odločanje.|
| [5.11 Spletno iskanje v realnem času](./mcp-realtimesearch/README.md) | Spletno iskanje | Kako MCP preoblikuje spletno iskanje v realnem času z zagotavljanjem standardiziranega pristopa k upravljanju konteksta med AI modeli, iskalniki in aplikacijami.| 
| [5.12 Avtentikacija Entra ID za MCP strežnike](./mcp-security-entra/README.md) | Avtentikacija Entra ID | Microsoft Entra ID nudi robustno rešitev za upravljanje identitet in dostopa v oblaku, ki pomaga zagotoviti, da lahko z vašim MCP strežnikom komunicirajo le pooblaščeni uporabniki in aplikacije.|
| [5.13 Integracija Azure AI Foundry agentov](./mcp-foundry-agent-integration/README.md) | Integracija Azure AI Foundry | Naučite se, kako integrirati MCP strežnike z Azure AI Foundry agenti, kar omogoča močno orkestracijo orodij in podjetniške AI zmogljivosti z standardiziranimi povezavami do zunanjih virov podatkov.|
| [5.14 Inženiring konteksta](./mcp-contextengineering/README.md) | Inženiring konteksta | Prihodnost možnosti tehnik inženiringa konteksta za MCP strežnike, vključno z optimizacijo konteksta, dinamičnim upravljanjem konteksta in strategijami za učinkovito inženirstvo pozivov znotraj MCP okvirov.|
| [5.15 Prilagojeni prenos MCP](./mcp-transport/README.md) | Prilagojeni prenos | Naučite se, kako implementirati prilagojene transportne mehanizme za specializirane komunikacijske scenarije MCP.|
| [5.16 Poglobljeno o protokolnih funkcijah](./mcp-protocol-features/README.md) | Protokolne funkcije | Obvladajte napredne funkcije protokola, vključno z obvestili o napredku, preklicem zahtev, predlogami virov in vzorci za upravljanje napak.|
| [5.17 Protivložna večagentna razprava](./mcp-adversarial-agents/README.md) | Protivložni agenti | Uporabite dva agenta z nasprotnimi stališči, ki delita en nabor MCP orodij, da ujamete halucinacije, izpostavite robne primere in proizvedete bolje kalibrirane izhode skozi strukturiran razpravo.|

> **Novo v MCP specifikaciji 2025-11-25**: Specifikacija zdaj vključuje eksperimentalno podporo za **Naloge** (dolgotrajne operacije s sledenjem napredka), **Oznake orodij** (metapodatki o vedenju orodij za varnost), **URL način izzivanja** (zahtevajo specifično vsebino URL od odjemalcev) in izboljšane **korene** (za upravljanje delovnega okolja konteksta). Za celotne podrobnosti glejte [MCP Specificiation changelog](https://spec.modelcontextprotocol.io/).

## Dodatne reference

Za najnovejše informacije o naprednih temah MCP glejte:
- [MCP Dokumentacija](https://modelcontextprotocol.io/)
- [MCP Specifikacija (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub Repozitorij](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Varnostna tveganja in omilitve
- [MCP Varnostni vrh delavnica (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktično varnostno usposabljanje

## Ključne ugotovitve

- Večmodalne MCP implementacije razširjajo AI zmogljivosti preko obdelave besedila
- Razširljivost je ključna za podjetniške uvajanja in jo lahko naslovimo s horizontalnim in vertikalnim skaliranjem
- Celovite varnostne ukrepe varujejo podatke in zagotavljajo ustrezno kontrolo dostopa
- Podjetniška integracija s platformami, kot so Azure OpenAI in Microsoft AI Foundry, izboljšuje zmogljivosti MCP
- Napredne MCP implementacije imajo korist od optimiziranih arhitektur in natančnega upravljanja virov

## Vaja

Oblikujte produkcijsko MCP implementacijo za specifičen primer uporabe:

1. Opredelite večmodalne zahteve za vaš primer uporabe
2. Opredelite varnostne kontrole potrebne za zaščito občutljivih podatkov
3. Oblikujte razširljivo arhitekturo, ki lahko obvladuje spreminjajoče se obremenitve
4. Načrtujte integracijske točke s podjetniškimi AI sistemi
5. Dokumentirajte možne ozka grla zmogljivosti in strategije omilitve

## Dodatni viri

- [Azure OpenAI Dokumentacija](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry Dokumentacija](https://learn.microsoft.com/en-us/ai-services/)

---

## Kaj sledi

Raziskujte lekcije v tem modulu, začenši z: [5.1 MCP Integracija](./mcp-integration/README.md)

Ko zaključite ta modul, nadaljujte z: [Modul 6: Prispevki skupnosti](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v maternem jeziku velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitna nerazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->