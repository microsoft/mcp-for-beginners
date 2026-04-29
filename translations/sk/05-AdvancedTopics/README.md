# Pokročilé témy v MCP

[![Pokročilé MCP: Bezpeční, škálovateľní a multimodálni AI agenti](../../../translated_images/sk/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

Táto kapitola pokrýva sériu pokročilých tém v implementácii Model Context Protocolu (MCP), vrátane multimodálnej integrácie, škálovateľnosti, najlepších praktík bezpečnosti a integrácie do podnikového prostredia. Tieto témy sú kľúčové pre vytváranie robustných a produkčne pripravených MCP aplikácií, ktoré môžu spĺňať požiadavky moderných AI systémov.

## Prehľad

Táto lekcia skúma pokročilé koncepty implementácie Model Context Protocolu, so zameraním na multimodálnu integráciu, škálovateľnosť, najlepšie praktiky bezpečnosti a integráciu do podnikového prostredia. Tieto témy sú nevyhnutné pre tvorbu produkčných MCP aplikácií, ktoré dokážu zvládnuť komplexné požiadavky v podnikových prostrediach.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Implementovať multimodálne schopnosti v rámci MCP frameworkov
- Navrhnúť škálovateľné MCP architektúry pre scénare s vysokou záťažou
- Aplikovať najlepšie bezpečnostné praktiky v súlade s bezpečnostnými princípmi MCP
- Integrovať MCP so systémami a frameworkami podnikovej AI
- Optimalizovať výkon a spoľahlivosť v produkčných prostrediach

## Lekcie a ukážkové projekty

| Odkaz | Názov | Popis |
|------|-------|-------------|
| [5.1 Integrácia s Azure](./mcp-integration/README.md) | Integrácia s Azure | Naučte sa, ako integrovať svoj MCP Server na Azure |
| [5.2 Multimodálny príklad](./mcp-multi-modality/README.md) | MCP Multimodálne ukážky | Ukážky pre audio, obrázok a multimodálnu odozvu |
| [5.3 MCP OAuth2 ukážka](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimálna Spring Boot aplikácia ukazujúca OAuth2 s MCP, ako Autorizačný aj Zdrojový Server. Demonštruje bezpečné vydávanie tokenov, chránené koncové body, nasadenie na Azure Container Apps a integráciu s API Management. |
| [5.4 Koreňové kontexty](./mcp-root-contexts/README.md) | Koreňové kontexty | Dozviete sa viac o koreňovom kontexte a ako ich implementovať |
| [5.5 Smerovanie](./mcp-routing/README.md) | Smerovanie | Naučte sa rôzne typy smerovania |
| [5.6 Výber vzoriek](./mcp-sampling/README.md) | Výber vzoriek | Naučte sa pracovať s výberom vzoriek |
| [5.7 Škálovanie](./mcp-scaling/README.md) | Škálovanie | Naučte sa o škálovaní |
| [5.8 Bezpečnosť](./mcp-security/README.md) | Bezpečnosť | Zabezpečte svoj MCP Server |
| [5.9 Webové vyhľadávanie MCP](./web-search-mcp/README.md) | Webové vyhľadávanie MCP | Python MCP server a klient integrujúci SerpAPI pre vyhľadávanie na webe, správach, produktoch a Q&A v reálnom čase. Demonštruje orkestrovanie viacerých nástrojov, integráciu externých API a robustné spracovanie chýb. |
| [5.10 Streaming v reálnom čase](./mcp-realtimestreaming/README.md) | Streaming | Streaming dát v reálnom čase sa stal nevyhnutným v dnešnom dátami riadenom svete, kde podniky a aplikácie potrebujú okamžitý prístup k informáciám pre včasné rozhodovanie. |
| [5.11 Webové vyhľadávanie v reálnom čase](./mcp-realtimesearch/README.md) | Webové vyhľadávanie | Reálny čas webového vyhľadávania — ako MCP transformuje vyhľadávanie v reálnom čase poskytovaním štandardizovaného prístupu k správe kontextu naprieč AI modelmi, vyhľadávacími enginmi a aplikáciami. |
| [5.12 Overovanie Entra ID pre Model Context Protocol Servers](./mcp-security-entra/README.md) | Overovanie Entra ID | Microsoft Entra ID poskytuje robustné cloudové riešenie na správu identity a prístupu, ktoré pomáha zabezpečiť, že len autorizovaní používatelia a aplikácie môžu komunikovať s vaším MCP serverom. |
| [5.13 Integrácia agenta Azure AI Foundry](./mcp-foundry-agent-integration/README.md) | Integrácia Azure AI Foundry | Naučte sa ako integrovať MCP servery s agentmi Azure AI Foundry, čo umožňuje silné orkestrovanie nástrojov a podnikové AI možnosti so štandardizovanými pripojeniami na externé dátové zdroje. |
| [5.14 Inžinierstvo kontextu](./mcp-contextengineering/README.md) | Inžinierstvo kontextu | Budúce príležitosti techník inžinierstva kontextu pre MCP servery, vrátane optimalizácie kontextu, dynamickej správy kontextu a stratégií efektívneho prompt engineeringu v MCP frameworkoch. |
| [5.15 Vlastný transport MCP](./mcp-transport/README.md) | Vlastný transport | Naučte sa implementovať vlastné transportné mechanizmy pre špecializované komunikačné scenáre MCP. |
| [5.16 Hĺbkový pohľad na funkcie protokolu](./mcp-protocol-features/README.md) | Funkcie protokolu | Ovládnite pokročilé funkcie protokolu vrátane upozornení o priebehu, zrušenia požiadaviek, šablón zdrojov a vzorov spracovania chýb. |
| [5.17 Adverzné viacagentné uvažovanie](./mcp-adversarial-agents/README.md) | Adverzní agenti | Použite dvoch agentov s protichodnými stanoviskami, ktorí zdieľajú jeden MCP nástrojový set, aby odhalili halucinácie, povrchové okrajové prípady a vyprodukovali lepšie kalibrované výstupy cez štruktúrovanú debatu. |

> **Novinka v špecifikácii MCP 2025-11-25**: Špecifikácia teraz obsahuje experimentálnu podporu pre **Úlohy** (dlhotrvajúce operácie so sledovaním priebehu), **Anotácie nástrojov** (metadata o správaní nástroja pre bezpečnosť), **URL režim vyžiadania** (žiadanie konkrétneho URL obsahu od klientov) a rozšírené **Koreňe** (pre správu pracovného kontextu). Viac informácií nájdete v [MCP changelogu špecifikácie](https://spec.modelcontextprotocol.io/).

## Ďalšie odkazy

Pre najaktuálnejšie informácie o pokročilých témach MCP sa odkazujte na:
- [Dokumentácia MCP](https://modelcontextprotocol.io/)
- [Špecifikácia MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub repo](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - bezpečnostné riziká a opatrenia
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - praktický bezpečnostný tréning

## Kľúčové body

- Multimodálne implementácie MCP rozširujú možnosti AI nad rámec spracovania textu
- Škálovateľnosť je nevyhnutná pre podnikové nasadenia a rieši sa horizontálnym a vertikálnym škálovaním
- Komplexné bezpečnostné opatrenia chránia dáta a zabezpečujú správnu kontrolu prístupu
- Podniková integrácia s platformami ako Azure OpenAI a Microsoft AI Foundry zlepšuje schopnosti MCP
- Pokročilé MCP implementácie profitujú z optimalizovaných architektúr a starostlivého manažmentu zdrojov

## Cvičenie

Navrhnite podnikové MCP riešenie pre konkrétny prípad použitia:

1. Identifikujte multimodálne požiadavky pre svoj prípad použitia
2. Načrtnite bezpečnostné kontroly potrebné na ochranu citlivých dát
3. Navrhnite škálovateľnú architektúru zvládajúcu premenlivé zaťaženie
4. Naplánujte integračné body so systémami podnikovej AI
5. Zdokumentujte možné výkonové úzke miesta a stratégie ich zmiernenia

## Ďalšie zdroje

- [Dokumentácia Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Dokumentácia Microsoft AI Foundry](https://learn.microsoft.com/en-us/ai-services/)

---

## Čo ďalej

Preskúmajte lekcie v tomto module začínajúc: [5.1 MCP integrácia](./mcp-integration/README.md)

Po dokončení tohto modulu pokračujte na: [Modul 6: Príspevky komunity](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek neporozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->