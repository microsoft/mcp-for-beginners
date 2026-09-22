# MCP Bezpečnostní nejlepší postupy – aktualizace září 2026

Tento komplexní průvodce shrnuje základní bezpečnostní nejlepší postupy pro
implementaci systémů Model Context Protocol (MCP) založené na
**MCP Specifikaci 2026-07-28** a současných průmyslových standardech. Tyto
postupy řeší jak tradiční bezpečnostní otázky, tak i specifické hrozby
umělé inteligence unikátní pro nasazení MCP.

## Kritické bezpečnostní požadavky

### Povinná bezpečnostní opatření (POŽADAVKY MUSÍ BÝT SPLNĚNY)

1. **Ověření tokenů**: MCP servery **NESMÍ** přijímat žádné tokeny, které nebyly výslovně vydány pro samotný MCP server
2. **Ověření autorizace**: MCP servery implementující autorizaci **MUSÍ** ověřit VŠECHNY příchozí požadavky a **NESMÍ** používat relace pro autentizaci  
3. **Souhlas uživatele**: MCP proxy servery využívající statická ID klientů třetích stran **MUSÍ** získat výslovný souhlas pro každého MCP klienta před přeposláním autorizace
4. **Bezpečnost stavového handle**: MCP servery **NESMÍ** považovat držení stavového handle aplikace za autentizaci a **MUSÍ** autorizovat každý
	požadavek, který ho používá


## Základní bezpečnostní postupy

### 1. Validace a sanitace vstupů
- **Komplexní validace vstupů**: Validujte a sanitujte všechny vstupy, aby se zabránilo injekčním útokům, problémům zmatku zprostředkovatele a zranitelnostem promptů
- **Vynucení schématu parametrů**: Implementujte přísnou validaci JSON schématu pro všechny parametry nástrojů a API vstupy
- **Filtrace obsahu**: Používejte Microsoft Prompt Shields a Azure Content Safety k filtrování škodlivého obsahu v promptech a odpovědích
- **Sanitace výstupů**: Validujte a sanitujte všechny výstupy modelu před jejich předložením uživatelům nebo dalším systémům

### 2. Perfektní autentizace a autorizace  
- **Externí poskytovatelé identity**: Delegujte autentizaci na zavedené poskytovatele identity (Microsoft Entra ID, OAuth 2.1 poskytovatelé) místo implementace vlastní autentizace
- **Registrace klientů**: Preferujte dokumenty metadat Client ID nebo předregistraci; použijte zastaralou dynamickou registraci klienta pouze pro kompatibilitu
- **Detailní oprávnění**: Implementujte granulární, na nástroj specifická oprávnění podle principu nejmenšího oprávnění
- **Správa životního cyklu tokenů**: Používejte krátkodobé přístupové tokeny se zabezpečenou rotací a správným ověřením publika
- **Vícefaktorová autentizace**: Vyžadujte MFA pro veškerý administrativní přístup a citlivé operace

### 3. Zabezpečené komunikační protokoly
- **Transport Layer Security**: Používejte HTTPS s řádnou validací certifikátu
	pro vzdálenou HTTP komunikaci MCP; používejte izolaci procesů a
	prostředíové přihlašovací údaje pro lokální stdio servery
- **End-to-End šifrování**: Implementujte další šifrovací vrstvy pro vysoce citlivá data během přenosu i v klidu
- **Správa certifikátů**: Udržujte řádnou správu životního cyklu certifikátů s automatizovanými procesy obnovy
- **Vynucení verze protokolu**: Použijte MCP `2026-07-28`, zahrňte požadovaná
	metadata verze u každého požadavku a odmítejte nepodporované verze

### 4. Pokročilé omezení rychlosti a ochrana zdrojů
- **Vícevrstvé omezení rychlosti**: Implementujte omezení rychlosti podle uživatele, přihlašovacích údajů,
  operace, nástroje a zdrojů, abyste předešli zneužití
- **Adaptivní omezení rychlosti**: Používejte strojově učené omezení rychlosti, které se přizpůsobuje vzorcům použití a indikátorům hrozeb
- **Správa kvót zdrojů**: Nastavte vhodné limity pro výpočetní zdroje, využití paměti a dobu běhu
- **Ochrana proti DDoS**: Nasazujte komplexní systémy ochrany proti DDoS a analýzy provozu

### 5. Komplexní protokolování a monitorování
- **Strukturované auditní protokolování**: Implementujte podrobné a vyhledatelné protokoly pro veškeré MCP operace, spuštění nástrojů a bezpečnostní události
- **Monitorování bezpečnosti v reálném čase**: Nasazujte SIEM systémy s AI zasilám detekcí anomálií pro MCP pracovní zátěže
- **Protokolování v souladu s ochranou soukromí**: Protokolujte bezpečnostní události při respektování požadavků na ochranu dat a regulace
- **Integrace reakce na incidenty**: Propojte protokolovací systémy s automatizovanými workflow pro reakci na incidenty

### 6. Vylepšené bezpečné ukládání
- **Hardwarové bezpečnostní moduly**: Používejte ukládání klíčů podpořené HSM (Azure Key Vault, AWS CloudHSM) pro kritické kryptografické operace
- **Správa šifrovacích klíčů**: Implementujte řádnou rotaci klíčů, segregaci a přístupová oprávnění k šifrovacím klíčům
- **Správa tajemství**: Uchovávejte všechny API klíče, tokeny a přihlašovací údaje v dedikovaných systémech správy tajemství
- **Klasifikace dat**: Klasifikujte data podle úrovně citlivosti a aplikujte odpovídající opatření ochrany

### 7. Pokročilá správa tokenů
- **Prevence přesměrování tokenů**: Výslovně zakazujte vzory přesměrování tokenů, které obcházejí bezpečnostní kontroly
- **Validace publika**: Vždy ověřujte, zda claims tokenu odpovídají zamýšlené identitě MCP serveru
- **Autorizace založená na claims**: Implementujte detailní autorizaci podle claims tokenu a atributů uživatele
- **Binding tokenu**: Ověřte, že tokeny cílí na zamýšlený MCP zdroj a
	propojujte stavové handle aplikace serverově na autentizovaného uživatele

### 8. Zabezpečený stav aplikace

- **Kryptografické stavové handle**: Generujte neprůhledné, nedeterministické handle
	pro stav, který zahrnuje více požadavků
- **Uživatelsky specifické propojení**: Propojujte každý handle serverově s autentizovaným
	subjektem; nevěřte uživatelskému ID dodanému klientem
- **Řízení životního cyklu**: Vypršete a zrušte handle a definujte, jak klienti
	obnovují zastaralý stav
- **Autorizace na požadavek**: Při každém použití handle znovu ověřte autorizaci; handle je jméno, ne pověření


### 9. Bezpečnostní kontroly specifické pro AI
- **Obrana proti prompt injection**: Nasazujte Microsoft Prompt Shields s technikami zvýraznění, oddělovačů a datového označení
- **Prevence otravy nástrojů**: Validujte metadata nástrojů, monitorujte dynamické změny a ověřujte integritu nástrojů
- **Validace výstupů modelu**: Prohlížejte výstupy modelů na případné úniky dat, škodlivý obsah nebo porušení bezpečnostních politik
- **Ochrana kontextového okna**: Implementujte kontroly, které zabraňují otravení a manipulaci s kontextovým oknem

### 10. Bezpečnost spuštění nástrojů
- **Sandboxing spuštění**: Spouštějte nástroje v kontejnerizovaných a izolovaných prostředích s omezením zdrojů
- **Oddělení oprávnění**: Spouštějte nástroje s minimálními nezbytnými oprávněními a oddělenými servisními účty
- **Síťová izolace**: Implementujte segmentaci sítí pro prostředí spuštění nástrojů
- **Monitorování spuštění**: Sledujte spuštění nástrojů na anomální chování, využití zdrojů a bezpečnostní porušení

### 11. Neustálé ověřování bezpečnosti
- **Automatizované bezpečnostní testy**: Integrujte bezpečnostní testování do CI/CD pipeline s nástroji jako GitHub Advanced Security
- **Správa zranitelností**: Pravidelně skenujte všechny závislosti včetně AI modelů a externích služeb
- **Penetrační testování**: Provádějte pravidelné bezpečnostní audity zaměřené na implementace MCP
- **Bezpečnostní revize kódu**: Zavádějte povinné bezpečnostní revize pro všechny změny kódu vztahující se k MCP

### 12. Bezpečnost dodavatelského řetězce pro AI
- **Ověření komponent**: Ověřujte původ, integritu a bezpečnost všech AI komponent (modely, embeddingy, API)
- **Správa závislostí**: Udržujte aktuální inventáře všech softwarových a AI závislostí s evidencí zranitelností
- **Důvěryhodné repozitáře**: Používejte ověřené a důvěryhodné zdroje pro všechny AI modely, knihovny a nástroje
- **Monitorování dodavatelského řetězce**: Průběžně monitorujte kompromisy poskytovatelů AI služeb a repozitářů modelů

## Pokročilé bezpečnostní vzory

### Architektura Zero Trust pro MCP
- **Nikdy nevěř, vždy ověřuj**: Implementujte kontinuální ověřování pro všechny účastníky MCP
- **Mikrosegmentace**: Izolujte komponenty MCP pomocí granulární sítě a kontrol identity
- **Podmíněný přístup**: Implementujte přístupová pravidla založená na riziku, která se přizpůsobují kontextu a chování
- **Kontinuální hodnocení rizik**: Dynamicky vyhodnocujte bezpečnostní stav na základě aktuálních indikátorů hrozeb

### Implementace AI s ochranou soukromí
- **Minimalizace dat**: Zveřejňujte pouze minimální nezbytná data pro každou MCP operaci
- **Diferenciální soukromí**: Implementujte techniky ochrany soukromí pro zpracování citlivých dat
- **Homomorfní šifrování**: Používejte pokročilé šifrovací techniky pro bezpečné výpočty na zašifrovaných datech
- **Federované učení**: Implementujte distribuované přístupy učení, které zachovávají lokalitu a soukromí dat

### Reakce na incidenty pro AI systémy
- **Postupy reakce na AI specifické incidenty**: Vyvíjejte postupy reakce na incidenty uzpůsobené hrozbám AI a MCP
- **Automatizovaná reakce**: Implementujte automatizovanou izolaci a nápravu běžných bezpečnostních incidentů AI  
- **Forenzní schopnosti**: Udržujte forenzní připravenost pro kompromisy AI systémů a úniky dat
- **Postupy obnovy**: Zaveďte procedury obnovy po otrávení AI modelů, útocích prompt injection a kompromitaci služeb

## Implementační zdroje a standardy

### 🏔️ Praktický bezpečnostní trénink
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** – Komplexní praktický workshop zaměřený na zabezpečení MCP serverů v Azure
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** – Referenční architektura a implementační pokyny OWASP MCP Top 10

### Oficiální MCP dokumentace
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) – Aktuální specifikace MCP protokolu
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) – Oficiální bezpečnostní pokyny
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) – Vzory HTTP autorizace
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) – Požadavky na transporty

### Microsoft bezpečnostní řešení
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) – Pokročilá ochrana proti prompt injection
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) – Komplexní filtrování obsahu AI
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) – Podnikové řízení identity a přístupu
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) – Bezpečná správa tajemství a přihlašovacích údajů
- [GitHub Advanced Security](https://github.com/security/advanced-security) – Skenování bezpečnosti dodavatelského řetězce a kódu

### Bezpečnostní standardy a rámce
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) – Aktuální pokyny k bezpečnosti OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) – Rizika webových aplikací
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) – Specifická bezpečnostní rizika AI
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) – Komplexní řízení rizik AI
- [ISO 27001:2022](https://www.iso.org/standard/27001) – Systémy řízení informační bezpečnosti

### Implementační průvodce a tutoriály
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) – Vzory autentizace podnikové úrovně
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) – Integrace poskytovatele identity
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) – Nejlepší postupy správy tokenů
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) – Pokročilé šifrovací vzory

### Pokročilé bezpečnostní zdroje
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) – Bezpečné vývojové postupy
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) – Testování bezpečnosti specifické pro AI
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) – Metodologie modelování hrozeb AI
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) – Techniky ochrany soukromí v AI

### Soulad a správa
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) – Soulad s ochranou soukromí v AI systémech
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) – Rámec odpovědného AI
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) – Bezpečnostní kontroly pro poskytovatele AI služeb
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) – Požadavky na dodržování HIPAA v AI pro zdravotnictví

### DevSecOps a automatizace
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) – Bezpečné vývojové pipeline AI
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) – Nepřetržité ověřování bezpečnosti
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) – Bezpečné nasazení infrastruktury
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) – Bezpečnost kontejnerizace AI zátěže

### Monitorování a reakce na incidenty  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) – Komplexní řešení monitorování
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) – Postupy reakce na incidenty specifické pro AI
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) – Řízení bezpečnostních informací a událostí

- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Zdroje hrozeb inteligence AI

## 🔄 Neustálé zlepšování

### Sledujte aktuální vývoj standardů
- **Aktualizace specifikace MCP**: Sledujte oficiální změny specifikace MCP a bezpečnostní upozornění
- **Threat Intelligence**: Přihlaste se k odběru zdrojů AI bezpečnostních hrozeb a databází zranitelností  
- **Zapojení komunity**: Účastněte se diskuzí a pracovních skupin bezpečnostní komunity MCP
- **Pravidelné hodnocení**: Provádějte čtvrtletní hodnocení bezpečnostního stavu a podle toho aktualizujte postupy

### Přispívání k bezpečnosti MCP
- **Bezpečnostní výzkum**: Přispívejte do výzkumu bezpečnosti MCP a programů zjevení zranitelností
- **Sdílení nejlepších praktik**: Sdílejte bezpečnostní implementace a získané zkušenosti s komunitou
- **Vývoj standardů**: Podílejte se na vývoji specifikace MCP a tvorbě bezpečnostních standardů
- **Vývoj nástrojů**: Vyvíjejte a sdílejte bezpečnostní nástroje a knihovny pro ekosystém MCP

---

*Tento dokument odráží nejlepší bezpečnostní praktiky MCP ke dni 9. září 2026,
na základě specifikace MCP `2026-07-28`. Bezpečnostní postupy by měly být pravidelně
přezkoumávány s vývojem protokolu a hrozeb.*

## Co dál

- Přečtěte si: [MCP Security Best Practices](./mcp-security-best-practices.md)
- Vraťte se na: [Security Module Overview](./README.md)
- Pokračujte na: [Module 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->