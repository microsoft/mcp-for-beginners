# MCP Bezpečnostné Najlepšie Praktiky 2025

Tento komplexný sprievodca načrtáva základné bezpečnostné najlepšie praktiky pre implementáciu systémov Model Context Protocol (MCP) založených na najnovšej **MCP Špecifikácii 2025-11-25** a aktuálnych priemyselných štandardoch. Tieto praktiky riešia tradičné bezpečnostné obavy aj špecifické hrozby AI jedinečné pre nasadenia MCP.

## Kritické Bezpečnostné Požiadavky

### Povinné Bezpečnostné Kontroly (POVINNÉ Požiadavky)

1. **Validácia Tokenov**: MCP servery **NESMÚ** akceptovať žiadne tokeny, ktoré neboli explicitne vydané pre samotný MCP server
2. **Overenie Autorizácie**: MCP servery implementujúce autorizáciu **MUSIA** overiť VŠETKY prichádzajúce požiadavky a **NESMÚ** používať relácie na autentifikáciu  
3. **Súhlas Používateľa**: MCP proxy servery používajúce statické klientské ID **MUSIA** získať explicitný súhlas používateľa pre každého dynamicky registrovaného klienta
4. **Bezpečné ID Relácií**: MCP servery **MUSIA** používať kryptograficky bezpečné, nedeterministické ID relácií generované pomocou bezpečných generátorov náhodných čísel

## Základné Bezpečnostné Praktiky

### 1. Validácia a Sanitizácia Vstupov
- **Komplexná Validácia Vstupov**: Validovať a sanitizovať všetky vstupy, aby sa zabránilo injekčným útokom, problémom s „confused deputy“ a zraniteľnostiam prompt injection
- **Vynucovanie Schémy Parametrov**: Implementovať prísnu validáciu JSON schémy pre všetky parametre nástrojov a API vstupy
- **Filtrovanie Obsahu**: Používať Microsoft Prompt Shields a Azure Content Safety na filtrovanie škodlivého obsahu v promptoch a odpovediach
- **Sanitizácia Výstupov**: Validovať a sanitizovať všetky výstupy modelu pred ich zobrazením používateľom alebo ďalším systémom

### 2. Excelentnosť v Autentifikácii a Autorizácii  
- **Externí Poskytovatelia Identity**: Delegovať autentifikáciu na etablovaných poskytovateľov identity (Microsoft Entra ID, OAuth 2.1 poskytovatelia) namiesto implementácie vlastnej autentifikácie
- **Granulárne Povolenia**: Implementovať detailné, nástrojovo špecifické povolenia podľa princípu najmenších právomocí
- **Správa Životného Cyklu Tokenov**: Používať krátkodobé prístupové tokeny s bezpečnou rotáciou a správnym overením publika
- **Viacfaktorová Autentifikácia**: Vyžadovať MFA pre všetky administratívne prístupy a citlivé operácie

### 3. Bezpečné Komunikačné Protokoly
- **Transport Layer Security**: Používať HTTPS/TLS 1.3 pre všetku komunikáciu MCP s riadnym overením certifikátov
- **End-to-End Šifrovanie**: Implementovať dodatočné vrstvy šifrovania pre vysoko citlivé dáta počas prenosu aj v pokoji
- **Správa Certifikátov**: Udržiavať správu životného cyklu certifikátov s automatizovanými procesmi obnovy
- **Vynucovanie Verzie Protokolu**: Používať aktuálnu verziu MCP protokolu (2025-11-25) s riadnym vyjednávaním verzie.

### 4. Pokročilé Obmedzovanie Rýchlosti a Ochrana Zdroja
- **Viacvrstvové Obmedzovanie Rýchlosti**: Implementovať obmedzovanie rýchlosti na úrovni používateľa, relácie, nástroja a zdroja, aby sa zabránilo zneužitiu
- **Adaptívne Obmedzovanie Rýchlosti**: Používať strojové učenie na obmedzovanie rýchlosti, ktoré sa prispôsobuje vzorom používania a indikátorom hrozieb
- **Správa Kvót Zdroja**: Nastaviť primerané limity pre výpočtové zdroje, využitie pamäte a čas vykonávania
- **Ochrana proti DDoS**: Nasadiť komplexné systémy ochrany proti DDoS a analýzy prevádzky

### 5. Komplexné Logovanie a Monitorovanie
- **Štruktúrované Auditné Logy**: Implementovať detailné, vyhľadávateľné logy pre všetky MCP operácie, vykonávanie nástrojov a bezpečnostné udalosti
- **Monitorovanie Bezpečnosti v Reálnom Čase**: Nasadiť SIEM systémy s AI-poháňanou detekciou anomálií pre MCP záťaže
- **Logovanie v Súlade s Ochrannou Súkromia**: Logovať bezpečnostné udalosti s rešpektovaním požiadaviek a regulácií ochrany údajov
- **Integrácia Reakcie na Incidenty**: Prepojiť logovacie systémy s automatizovanými pracovnými tokmi reakcie na incidenty

### 6. Vylepšené Praktiky Bezpečného Ukladania
- **Hardvérové Bezpečnostné Moduly**: Používať ukladanie kľúčov podporované HSM (Azure Key Vault, AWS CloudHSM) pre kritické kryptografické operácie
- **Správa Šifrovacích Kľúčov**: Implementovať správnu rotáciu kľúčov, segregáciu a prístupové kontroly pre šifrovacie kľúče
- **Správa Tajomstiev**: Ukladať všetky API kľúče, tokeny a poverenia v dedikovaných systémoch správy tajomstiev
- **Klasifikácia Dát**: Klasifikovať dáta podľa úrovne citlivosti a aplikovať primerané ochranné opatrenia

### 7. Pokročilá Správa Tokenov
- **Prevencia Prenosu Tokenov**: Explicitne zakázať vzory prenosu tokenov, ktoré obchádzajú bezpečnostné kontroly
- **Validácia Publika**: Vždy overovať, že nároky publika tokenu zodpovedajú zamýšľanej identite MCP servera
- **Autorizácia na Základe Nárokov**: Implementovať detailnú autorizáciu založenú na nárokoch tokenu a atribútoch používateľa
- **Väzba Tokenov**: Väzba tokenov na konkrétne relácie, používateľov alebo zariadenia, kde je to vhodné

### 8. Bezpečná Správa Relácií
- **Kryptografické ID Relácií**: Generovať ID relácií pomocou kryptograficky bezpečných generátorov náhodných čísel (nie predvídateľné sekvencie)
- **Väzba na Používateľa**: Väzba ID relácií na používateľsky špecifické informácie pomocou bezpečných formátov ako `<user_id>:<session_id>`
- **Kontroly Životného Cyklu Relácie**: Implementovať správne mechanizmy vypršania, rotácie a neplatnosti relácií
- **Bezpečnostné Hlavičky Relácie**: Používať vhodné HTTP bezpečnostné hlavičky na ochranu relácií

### 9. AI-špecifické Bezpečnostné Kontroly
- **Ochrana proti Prompt Injection**: Nasadiť Microsoft Prompt Shields s technikami spotlighting, delimiters a datamarking
- **Prevencia Otravy Nástrojov**: Validovať metadata nástrojov, monitorovať dynamické zmeny a overovať integritu nástrojov
- **Validácia Výstupov Modelu**: Skontrolovať výstupy modelu na potenciálne úniky dát, škodlivý obsah alebo porušenia bezpečnostnej politiky
- **Ochrana Kontextového Okna**: Implementovať kontroly na zabránenie otravy a manipulácie kontextového okna

### 10. Bezpečnosť Vykonávania Nástrojov
- **Sandboxing Vykonávania**: Spúšťať vykonávanie nástrojov v kontajnerizovaných, izolovaných prostrediach s limitmi zdrojov
- **Oddelenie Právomocí**: Vykonávať nástroje s minimálnymi potrebnými právomocami a oddelenými servisnými účtami
- **Sieťová Izolácia**: Implementovať sieťovú segmentáciu pre prostredia vykonávania nástrojov
- **Monitorovanie Vykonávania**: Monitorovať vykonávanie nástrojov na anomálne správanie, využitie zdrojov a porušenia bezpečnosti

### 11. Neustála Validácia Bezpečnosti
- **Automatizované Bezpečnostné Testovanie**: Integrovať bezpečnostné testovanie do CI/CD pipeline s nástrojmi ako GitHub Advanced Security
- **Správa Zraniteľností**: Pravidelne skenovať všetky závislosti vrátane AI modelov a externých služieb
- **Penetračné Testovanie**: Vykonávať pravidelné bezpečnostné hodnotenia špecificky zamerané na implementácie MCP
- **Bezpečnostné Kódové Revízie**: Implementovať povinné bezpečnostné revízie pre všetky zmeny kódu súvisiace s MCP

### 12. Bezpečnosť Dodávateľského Reťazca pre AI
- **Overenie Komponentov**: Overovať pôvod, integritu a bezpečnosť všetkých AI komponentov (modely, embeddingy, API)
- **Správa Závislostí**: Udržiavať aktuálne inventáre všetkého softvéru a AI závislostí s evidenciou zraniteľností
- **Dôveryhodné Repozitáre**: Používať overené, dôveryhodné zdroje pre všetky AI modely, knižnice a nástroje
- **Monitorovanie Dodávateľského Reťazca**: Neustále monitorovať kompromisy poskytovateľov AI služieb a repozitárov modelov

## Pokročilé Bezpečnostné Vzory

### Architektúra Zero Trust pre MCP
- **Nikdy Nedôveruj, Vždy Overuj**: Implementovať kontinuálne overovanie všetkých účastníkov MCP
- **Mikrosegmentácia**: Izolovať MCP komponenty s granulárnymi sieťovými a identitnými kontrolami
- **Podmienený Prístup**: Implementovať prístupové kontroly založené na riziku, ktoré sa prispôsobujú kontextu a správaniu
- **Kontinuálne Hodnotenie Rizika**: Dynamicky vyhodnocovať bezpečnostnú pozíciu na základe aktuálnych indikátorov hrozieb

### Implementácia AI s Ochrannou Súkromia
- **Minimalizácia Dát**: Zverejňovať iba minimálne nevyhnutné dáta pre každú MCP operáciu
- **Diferenciálna Súkromnosť**: Implementovať techniky ochrany súkromia pri spracovaní citlivých dát
- **Homomorfné Šifrovanie**: Používať pokročilé šifrovacie techniky pre bezpečné výpočty nad zašifrovanými dátami
- **Federované Učenie**: Implementovať distribuované učenie, ktoré zachováva lokalitu dát a súkromie

### Reakcia na Incidenty pre AI Systémy
- **AI-špecifické Postupy Incidentov**: Vypracovať postupy reakcie na incidenty prispôsobené AI a MCP špecifickým hrozbám
- **Automatizovaná Reakcia**: Implementovať automatizované zadržiavanie a nápravu bežných AI bezpečnostných incidentov  
- **Forenzné Schopnosti**: Udržiavať forenznú pripravenosť na kompromisy AI systémov a úniky dát
- **Postupy Obnovy**: Zaviesť postupy na obnovu po otrave AI modelov, útokoch prompt injection a kompromisoch služieb

## Zdroje a Štandardy pre Implementáciu

### Oficiálna MCP Dokumentácia
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Aktuálna špecifikácia MCP protokolu
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Oficiálne bezpečnostné usmernenia
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Vzory autentifikácie a autorizácie
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Požiadavky na bezpečnosť transportnej vrstvy

### Microsoft Bezpečnostné Riešenia
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Pokročilá ochrana proti prompt injection
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Komplexné filtrovanie AI obsahu
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Podnikové riadenie identity a prístupu
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Bezpečná správa tajomstiev a poverení
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Skúmanie bezpečnosti dodávateľského reťazca a kódu

### Bezpečnostné Štandardy a Rámce
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Aktuálne usmernenia bezpečnosti OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Riziká bezpečnosti webových aplikácií
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-špecifické bezpečnostné riziká
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Komplexné riadenie rizík AI
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Systémy riadenia informačnej bezpečnosti

### Sprievodcovia a Tutoriály pre Implementáciu
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Podnikové vzory autentifikácie
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integrácia poskytovateľa identity
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Najlepšie praktiky správy tokenov
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Pokročilé vzory šifrovania

### Pokročilé Bezpečnostné Zdroje
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Bezpečnostné praktiky vývoja
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-špecifické bezpečnostné testovanie
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodológia modelovania hrozieb AI
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Techniky ochrany súkromia AI

### Súlad a Riadenie
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Súlad s ochranou súkromia v AI systémoch
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Zodpovedná implementácia AI
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Bezpečnostné kontroly pre poskytovateľov AI služieb
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Požiadavky na súlad zdravotníckej AI

### DevSecOps a Automatizácia
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Bezpečné vývojové pipeline pre AI
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Neustála validácia bezpečnosti
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Bezpečné nasadenie infraštruktúry
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Bezpečnosť kontajnerizácie AI záťaží

### Monitorovanie a Reakcia na Incidenty  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Komplexné monitorovacie riešenia
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-špecifické postupy reakcie na incidenty
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Správa bezpečnostných informácií a udalostí
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Zdroje hrozbovej inteligencie pre AI

## 🔄 Neustále Zlepšovanie

### Zostaňte Aktuálni s Vyvíjajúcimi sa Štandardmi
- **Aktualizácie MCP Špecifikácie**: Monitorovať oficiálne zmeny MCP špecifikácie a bezpečnostné upozornenia
- **Hrozbová Inteligencia**: Prihlásiť sa na odbery AI bezpečnostných hrozbových kanálov a databáz zraniteľností  
- **Zapojenie Komunity**: Zúčastňovať sa diskusií a pracovných skupín MCP bezpečnostnej komunity
- **Pravidelné Hodnotenie**: Vykonávať štvrťročné hodnotenia bezpečnostnej pozície a podľa toho aktualizovať praktiky

### Príspevok k Bezpečnosti MCP
- **Bezpečnostný Výskum**: Prispievať k MCP bezpečnostnému výskumu a programom zverejňovania zraniteľností
- **Zdieľanie Najlepších Praktík**: Zdieľať implementácie bezpečnosti a získané skúsenosti s komunitou
- **Štandardný vývoj**: Účasť na vývoji špecifikácie MCP a tvorbe bezpečnostných štandardov
- **Vývoj nástrojov**: Vývoj a zdieľanie bezpečnostných nástrojov a knižníc pre ekosystém MCP

---

*Tento dokument odráža najlepšie bezpečnostné postupy MCP k 18. decembru 2025, na základe špecifikácie MCP 2025-11-25. Bezpečnostné postupy by mali byť pravidelne prehodnocované a aktualizované podľa vývoja protokolu a hrozobného prostredia.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->