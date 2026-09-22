# Najlepšie bezpečnostné praktiky MCP – aktualizácia september 2026

Tento komplexný sprievodca načrtáva základné bezpečnostné najlepšie praktiky pre
implementáciu systémov Model Context Protocol (MCP) založených na
**špecifikácii MCP 2026-07-28** a aktuálnych priemyselných štandardoch. Tieto
praktiky riešia tradičné bezpečnostné obavy aj špecifické hrozby AI,
ktoré sú jedinečné pre nasadenia MCP.

## Kritické bezpečnostné požiadavky

### Povinné bezpečnostné kontroly (POŽIADAVKY MUSIA BYŤ SPLNENÉ)

1. **Validácia tokenov**: MCP servery **NESMÚ** akceptovať žiadne tokeny, ktoré neboli výslovne vydané pre samotný MCP server
2. **Overovanie autorizácie**: MCP servery implementujúce autorizáciu **MUSIA** overiť VŠETKY prichádzajúce požiadavky a **NESMÚ** používať relácie na autentifikáciu  
3. **Súhlas používateľa**: MCP proxy servery používajúce statické ID klienta tretej strany **MUSIA** získať výslovný súhlas pre každého MCP klienta pred presmerovaním autorizácie
4. **Bezpečnosť stavového ukazovateľa**: MCP servery **NESMÚ** považovať držbu
	ukazovateľa stavovej aplikácie za autentifikáciu a **MUSIA** autorizovať každú
	požiadavku, ktorá ho používa

## Hlavné bezpečnostné praktiky

### 1. Validácia a sanitácia vstupov
- **Komplexná validácia vstupov**: Validujte a sanitizujte všetky vstupy, aby ste predišli útokom typu injection, problémom s zámenným proxy agentom a zraniteľnostiam prompt injection
- **Vynucovanie schémy parametrov**: Implementujte prísnu validáciu JSON schémy pre všetky parametre nástrojov a API vstupy
- **Filtrovanie obsahu**: Používajte Microsoft Prompt Shields a Azure Content Safety na filtrovanie škodlivého obsahu v promptoch a odpovediach
- **Sanitácia výstupov**: Validujte a sanitizujte všetky výstupy modelu pred ich zobrazením používateľom alebo ďalším systémom

### 2. Excelentná autentifikácia a autorizácia  
- **Externí poskytovatelia identity**: Delegujte autentifikáciu na etablovaných poskytovateľov identity (Microsoft Entra ID, poskytovatelia OAuth 2.1) namiesto implementácie vlastnej autentifikácie
- **Registrácia klienta**: Uprednostňujte metadokumenty Client ID alebo predregistráciu; použite zastaralú dynamickú registráciu klienta iba pre kompatibilitu
- **Granulárne oprávnenia**: Implementujte detailné, nástrojovo špecifické oprávnenia podľa princípu najmenších právomocí
- **Správa životného cyklu tokenov**: Používajte krátkodobé access tokeny s bezpečnou rotáciou a správnou validáciou audience
- **Multi-faktorová autentifikácia**: Vyžadujte MFA pre všetky administratívne prístupy a citlivé operácie

### 3. Bezpečné komunikačné protokoly
- **Bezpečnosť transportnej vrstvy**: Používajte HTTPS s riadnou validáciou certifikátov
	pre diaľkovú HTTP komunikáciu MCP; používajte izoláciu procesu a
	overovacie údaje prostredia pre miestne stdio servery
- **End-to-end šifrovanie**: Implementujte dodatočné vrstvy šifrovania pre vysoko citlivé dáta v prenose a v pokoji
- **Správa certifikátov**: Udržiavajte riadne spravovanie životného cyklu certifikátov s automatickými procesmi obnovy
- **Vynucovanie verzie protokolu**: Používajte MCP `2026-07-28`, zahŕňajte požadované
	verziové metadata v každej požiadavke a odmietajte nepodporované verzie

### 4. Pokročilé obmedzenie rýchlosti a ochrana zdrojov
- **Viacvrstvové obmedzovanie rýchlosti**: Implementujte limitovanie podľa používateľa, poverenia,
  operácie, nástroja a zdroja na zabránenie zneužitia
- **Adaptívne obmedzovanie rýchlosti**: Používajte limitovanie na báze strojového učenia, ktoré sa prispôsobuje vzorom používania a indikátorom hrozieb
- **Správa kvót zdrojov**: Nastavte primerané limity pre výpočtové zdroje, využitie pamäte a čas vykonávania
- **Ochrana proti DDoS**: Nasadzujte komplexnú ochranu proti DDoS a systémy analýzy prevádzky

### 5. Komplexné zaznamenávanie a monitorovanie
- **Štruktúrované auditné záznamy**: Implementujte podrobné, vyhľadávateľné záznamy o všetkých MCP operáciách, vykonávaniach nástrojov a bezpečnostných udalostiach
- **Monitorovanie bezpečnosti v reálnom čase**: Nasadzujte SIEM systémy s AI-poháňanou detekciou anomálií pre MCP pracovné zaťaženia
- **Logovanie v súlade s ochranou súkromia**: Zaznamenávajte bezpečnostné udalosti pri rešpektovaní požiadaviek a pravidiel ochrany údajov
- **Integrácia reakcie na incidenty**: Prepojte systém zaznamenávania so systémami automatizovanej reakcie na incidenty

### 6. Vylepšené bezpečné praktiky ukladania
- **Hardvérové bezpečnostné moduly**: Používajte ukladanie kľúčov podporované HSM (Azure Key Vault, AWS CloudHSM) pre kritické kryptografické operácie
- **Správa kľúčov na šifrovanie**: Implementujte správnu rotáciu kľúčov, segregáciu a kontrolu prístupu ku kľúčom
- **Správa tajomstiev**: Ukladajte všetky API kľúče, tokeny a poverovacie údaje v vyhradených systémoch na správu tajomstiev
- **Klasifikácia dát**: Klasifikujte dáta podľa úrovní citlivosti a aplikujte primerané ochranné opatrenia

### 7. Pokročilá správa tokenov
- **Zabránenie prenosu tokenov**: Výslovne zakážte vzory prenosu tokenov, ktoré obchádzajú bezpečnostné kontroly
- **Validácia audience**: Vždy overujte, či claim audience tokenu zodpovedá zamýšľanej identite MCP servera
- **Autorizácia založená na claisoch**: Implementujte detailnú autorizáciu založenú na token claims a atribútoch používateľa
- **Naviazanie tokenu**: Overte, že tokeny sú určené pre cieľový MCP zdroj a
	viažu stavové ukazovatele aplikácie na strane servera ku autentifikovanej entite

### 8. Bezpečný stav aplikácie

- **Kryptografické stavové ukazovatele**: Generujte nepriehľadné, nedeterministické ukazovatele
	stavov, ktoré pretrvávajú naprieč požiadavkami
- **Viazanie na používateľa**: Viažte každý ukazovateľ serverovo ku autentifikovanému
	subjektu; nedôverujte používateľskému ID dodanému klientom
- **Kontroly životného cyklu**: Vypršajte platnosť a odvolajte ukazovatele, definujte, ako volajúci
	obnovujú zastaralé stavy
- **Autorizácia pre každú požiadavku**: Pri každom použití ukazovateľa znovu skontrolujte autorizáciu;
	ukazovateľ je názov, nie poverenie

### 9. Špecifické bezpečnostné kontroly pre AI
- **Ochrana proti prompt injection**: Nasadzujte Microsoft Prompt Shields s technikami zvýrazňovania, oddeľovačmi a značením dát
- **Prevencia otravy nástrojov**: Validujte metadáta nástrojov, monitorujte dynamické zmeny a overujte integritu nástrojov
- **Validácia výstupov modelu**: Skenujte výstupy modelov na potenciálne úniky dát, škodlivý obsah alebo porušenia bezpečnostnej politiky
- **Ochrana okna kontextu**: Implementujte mechanizmy na zabránenie otravy a manipulácie okna kontextu

### 10. Bezpečné vykonávanie nástrojov
- **Sandboxing vykonávania**: Spúšťajte nástroje v kontajnerizovaných izolovaných prostrediach s limitmi zdrojov
- **Oddelenie privilégií**: Vykonávajte nástroje s minimom potrebných právomocí a oddelenými servisnými účtami
- **Sieťová izolácia**: Implementujte segmentáciu siete pre prostredia vykonávania nástrojov
- **Monitorovanie vykonávania**: Sledujte vykonávanie nástrojov pre anomálne správanie, využitie zdrojov a porušenia bezpečnosti

### 11. Neustála bezpečnostná validácia
- **Automatizované bezpečnostné testovanie**: Integrujte testovanie bezpečnosti do CI/CD pipeline s nástrojmi ako GitHub Advanced Security
- **Správa zraniteľností**: Pravidelne skenujte všetky závislosti vrátane AI modelov a externých služieb
- **Penetračné testovanie**: Vykonávajte pravidelné bezpečnostné hodnotenia špecificky zamerané na implementácie MCP
- **Bezpečnostné kódové revízie**: Implementujte povinné bezpečnostné revízie pre všetky zmeny kódu súvisiace s MCP

### 12. Bezpečnosť dodávateľského reťazca pre AI
- **Overenie komponentov**: Overte pôvod, integritu a bezpečnosť všetkých AI komponentov (modely, embeddingy, API)
- **Správa závislostí**: Vedenie aktuálnych inventárov všetkého softvéru a AI závislostí s evidenciou zraniteľností
- **Dôveryhodné repozitáre**: Používajte overené, dôveryhodné zdroje pre všetky AI modely, knižnice a nástroje
- **Monitorovanie dodávateľského reťazca**: Neustále monitorujte kompromisy poskytovateľov AI služieb a úložísk modelov

## Pokročilé bezpečnostné vzory

### Architektúra Zero Trust pre MCP
- **Nikdy nedôveruj, vždy overuj**: Implementujte kontinuálne overovanie všetkých účastníkov MCP
- **Mikrosegmentácia**: Izolujte komponenty MCP s granulárnou kontrolou siete a identity
- **Podmienený prístup**: Implementujte prístupové kontroly založené na riziku, ktoré sa prispôsobujú kontextu a správaniu
- **Kontinuálne hodnotenie rizika**: Dynamicky vyhodnocujte bezpečnostný stav na základe aktuálnych indikátorov hrozieb

### Implementácia AI s ochranou súkromia
- **Minimalizácia údajov**: Poskytujte len minimum nevyhnutných údajov pre každú MCP operáciu
- **Diferenciálna ochrana súkromia**: Implementujte techniky zachovania súkromia pri spracovaní citlivých dát
- **Homomorfné šifrovanie**: Používajte pokročilé šifrovacie techniky na bezpečné spracovanie šifrovaných dát
- **Federatívne učenie**: Implementujte distribuované učenie, ktoré zachováva lokalitu dát a súkromie

### Reakcia na incidenty pre AI systémy
- **AI-špecifické postupy reakcie na incidenty**: Vyvíjajte postupy reakcie na incidenty prispôsobené AI a MCP špecifickým hrozbám
- **Automatizovaná reakcia**: Implementujte automatizované obmedzenie a nápravu bežných AI bezpečnostných incidentov  
- **Forenzné schopnosti**: Udržiavajte forenznú pripravenosť na kompromisy AI systémov a úniky dát
- **Postupy obnovy**: Zavádzajte postupy obnovy po otrave AI modelov, útokoch prompt injection a kompromisoch služieb

## Zdroje a štandardy implementácie

### 🏔️ Praktické školenia bezpečnosti
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** – komplexný praktický workshop na zabezpečenie MCP serverov v Azure
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** – referenčná architektúra a implementačné odporúčania OWASP MCP Top 10

### Oficiálna dokumentácia MCP
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) – aktuálna špecifikácia protokolu MCP
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) – oficiálne bezpečnostné usmernenia
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) – vzory HTTP autorizácie
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) – požiadavky na prenosové protokoly

### Microsoft bezpečnostné riešenia
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) – pokročilá ochrana proti prompt injection
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) – komplexné filtrovanie AI obsahu
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) – riadenie identity a prístupu pre podniky
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) – bezpečné riadenie tajomstiev a poverení
- [GitHub Advanced Security](https://github.com/security/advanced-security) – skenovanie bezpečnosti dodávateľského reťazca a kódu

### Bezpečnostné štandardy a rámce
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) – súčasné bezpečnostné odporúčania OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) – riziká bezpečnosti webových aplikácií
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) – bezpečnostné riziká špecifické pre AI
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) – komplexné riadenie rizík AI
- [ISO 27001:2022](https://www.iso.org/standard/27001) – systémy riadenia informačnej bezpečnosti

### Implementačné návody a tutoriály
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) – vzory autentifikácie pre podniky
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) – integrácia poskytovateľa identity
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) – najlepšie praktiky správy tokenov
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) – pokročilé vzory šifrovania

### Pokročilé bezpečnostné zdroje
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) – bezpečné vývojové praktiky
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) – testovanie bezpečnosti špecifické pre AI
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) – metodika modelovania bezpečnostných hrozieb AI
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) – techniky na ochranu súkromia pre AI

### Súlad a správa
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) – súlad s ochranou súkromia v AI systémoch
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) – zodpovedná implementácia AI
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) – bezpečnostné kontroly pre poskytovateľov AI služieb
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) – požiadavky na súlad zdravotníckej AI

### DevSecOps a automatizácia
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) – bezpečné vývojové pipeline pre AI
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) – nepretržitá bezpečnostná validácia
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) – bezpečné nasadenie infraštruktúry
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) – bezpečnosť kontajnerizácie AI pracovného zaťaženia

### Monitorovanie a reakcia na incidenty  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) – komplexné monitorovacie riešenia
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) – AI-špecifické postupy reakcie na incident
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) – riadenie informácií a udalostí bezpečnosti

- [Hrozbová inteligencia pre AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - zdroje hrozbovej inteligencie AI

## 🔄 Neustále zlepšovanie

### Zostaňte aktuálni s vyvíjajúcimi sa štandardmi
- **Aktualizácie špecifikácie MCP**: Sledujte oficiálne zmeny špecifikácie MCP a bezpečnostné upozornenia
- **Hrozbová inteligencia**: Prihláste sa na odbery informačných kanálov o bezpečnostných hrozbách AI a databáz zraniteľností  
- **Spolupráca s komunitou**: Zapájajte sa do diskusií a pracovných skupín bezpečnostnej komunity MCP
- **Pravidelné hodnotenie**: Vykonávajte štvrťročné hodnotenia bezpečnostného stavu a aktualizujte postupy podľa potreby

### Príspevky do bezpečnosti MCP
- **Bezpečnostný výskum**: Prispievajte do MCP bezpečnostného výskumu a programov zverejňovania zraniteľností
- **Zdieľanie najlepších praktík**: Zdieľajte implementácie bezpečnosti a získané poznatky s komunitou
- **Vývoj štandardov**: Participujte na vývoji špecifikácie MCP a tvorbe bezpečnostných štandardov
- **Vývoj nástrojov**: Vyvíjajte a zdieľajte bezpečnostné nástroje a knižnice pre ekosystém MCP

---

*Tento dokument odráža najlepšie bezpečnostné praktiky MCP k 9. septembru 2026,
vychádzajúc zo špecifikácie MCP `2026-07-28`. Bezpečnostné postupy by mali byť pravidelne
prehodnocované v súlade s vývojom protokolu a hrozbovej situácie.*

## Čo nasleduje

- Prečítajte si: [Najlepšie bezpečnostné praktiky MCP](./mcp-security-best-practices.md)
- Návrat na: [Prehľad bezpečnostného modulu](./README.md)
- Pokračujte na: [Modul 3: Začíname](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->