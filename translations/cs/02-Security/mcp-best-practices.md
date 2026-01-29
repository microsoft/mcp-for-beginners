# MCP Bezpečnostní osvědčené postupy 2025

Tento komplexní průvodce popisuje základní bezpečnostní osvědčené postupy pro implementaci systémů Model Context Protocol (MCP) založené na nejnovější **MCP Specifikaci 2025-11-25** a aktuálních průmyslových standardech. Tyto postupy řeší jak tradiční bezpečnostní problémy, tak i specifické hrozby AI unikátní pro nasazení MCP.

## Kritické bezpečnostní požadavky

### Povinné bezpečnostní kontroly (POVINNÉ požadavky)

1. **Ověření tokenu**: MCP servery **NESMÍ** přijímat žádné tokeny, které nebyly explicitně vydány pro samotný MCP server
2. **Ověření autorizace**: MCP servery implementující autorizaci **MUSÍ** ověřit VŠECHNY příchozí požadavky a **NESMÍ** používat relace pro autentizaci  
3. **Souhlas uživatele**: MCP proxy servery používající statická ID klientů **MUSÍ** získat explicitní souhlas uživatele pro každého dynamicky registrovaného klienta
4. **Bezpečné ID relace**: MCP servery **MUSÍ** používat kryptograficky bezpečná, nedeterministická ID relací generovaná pomocí bezpečných generátorů náhodných čísel

## Základní bezpečnostní postupy

### 1. Validace a sanitace vstupů
- **Komplexní validace vstupů**: Validovat a sanitizovat všechny vstupy, aby se zabránilo útokům typu injection, problémům s confused deputy a zranitelnostem prompt injection
- **Vynucení schématu parametrů**: Implementovat přísnou validaci JSON schématu pro všechny parametry nástrojů a API vstupy
- **Filtrování obsahu**: Používat Microsoft Prompt Shields a Azure Content Safety k filtrování škodlivého obsahu v promtech a odpovědích
- **Sanitace výstupů**: Validovat a sanitizovat všechny výstupy modelu před jejich prezentací uživatelům nebo následným systémům

### 2. Excelence v autentizaci a autorizaci  
- **Externí poskytovatelé identity**: Delegovat autentizaci na zavedené poskytovatele identity (Microsoft Entra ID, poskytovatelé OAuth 2.1) místo implementace vlastní autentizace
- **Detailní oprávnění**: Implementovat granulární, nástrojově specifická oprávnění podle principu nejmenších práv
- **Správa životního cyklu tokenů**: Používat krátkodobé přístupové tokeny s bezpečnou rotací a správným ověřením publika
- **Vícefaktorová autentizace**: Vyžadovat MFA pro veškerý administrativní přístup a citlivé operace

### 3. Bezpečné komunikační protokoly
- **Transport Layer Security**: Používat HTTPS/TLS 1.3 pro veškerou komunikaci MCP s řádným ověřením certifikátů
- **End-to-End šifrování**: Implementovat další vrstvy šifrování pro vysoce citlivá data během přenosu i v klidu
- **Správa certifikátů**: Udržovat správnou správu životního cyklu certifikátů s automatizovanými procesy obnovy
- **Vynucení verze protokolu**: Používat aktuální verzi MCP protokolu (2025-11-25) s řádným vyjednáváním verze.

### 4. Pokročilé omezení rychlosti a ochrana zdrojů
- **Vícevrstvé omezení rychlosti**: Implementovat omezení rychlosti na úrovni uživatele, relace, nástroje a zdroje, aby se zabránilo zneužití
- **Adaptivní omezení rychlosti**: Používat strojově učené omezení rychlosti, které se přizpůsobuje vzorcům používání a indikátorům hrozeb
- **Správa kvót zdrojů**: Nastavit vhodné limity pro výpočetní zdroje, využití paměti a dobu běhu
- **Ochrana proti DDoS**: Nasadit komplexní ochranu proti DDoS a systémy analýzy provozu

### 5. Komplexní protokolování a monitorování
- **Strukturované auditní protokolování**: Implementovat detailní, vyhledávatelné logy pro všechny MCP operace, spuštění nástrojů a bezpečnostní události
- **Monitorování bezpečnosti v reálném čase**: Nasadit SIEM systémy s AI-poháněnou detekcí anomálií pro MCP pracovní zátěže
- **Protokolování v souladu s ochranou soukromí**: Protokolovat bezpečnostní události s respektem k požadavkům a předpisům na ochranu dat
- **Integrace reakce na incidenty**: Propojit protokolovací systémy s automatizovanými workflow pro reakci na incidenty

### 6. Vylepšené bezpečné postupy ukládání
- **Hardwarové bezpečnostní moduly**: Používat úložiště klíčů založené na HSM (Azure Key Vault, AWS CloudHSM) pro kritické kryptografické operace
- **Správa šifrovacích klíčů**: Implementovat správnou rotaci klíčů, segregaci a přístupové kontroly pro šifrovací klíče
- **Správa tajemství**: Ukládat všechny API klíče, tokeny a přihlašovací údaje v dedikovaných systémech pro správu tajemství
- **Klasifikace dat**: Klasifikovat data podle úrovně citlivosti a aplikovat odpovídající ochranná opatření

### 7. Pokročilá správa tokenů
- **Prevence průchodu tokenů**: Explicitně zakázat vzory průchodu tokenů, které obcházejí bezpečnostní kontroly
- **Ověření publika**: Vždy ověřovat, že nároky publika tokenu odpovídají zamýšlené identitě MCP serveru
- **Autorizace založená na nárocích**: Implementovat detailní autorizaci založenou na nárocích tokenu a atributech uživatele
- **Vazba tokenů**: Vázat tokeny na konkrétní relace, uživatele nebo zařízení, kde je to vhodné

### 8. Bezpečná správa relací
- **Kryptografická ID relací**: Generovat ID relací pomocí kryptograficky bezpečných generátorů náhodných čísel (nepředvídatelných sekvencí)
- **Vazba na uživatele**: Vázat ID relací na uživatelsky specifické informace pomocí bezpečných formátů jako `<user_id>:<session_id>`
- **Kontroly životního cyklu relace**: Implementovat správné mechanismy vypršení, rotace a neplatnosti relací
- **Bezpečnostní hlavičky relace**: Používat vhodné HTTP bezpečnostní hlavičky pro ochranu relací

### 9. Specifické bezpečnostní kontroly pro AI
- **Ochrana proti prompt injection**: Nasadit Microsoft Prompt Shields s technikami spotlighting, delimiters a datamarking
- **Prevence otravy nástrojů**: Validovat metadata nástrojů, monitorovat dynamické změny a ověřovat integritu nástrojů
- **Validace výstupů modelu**: Prohledávat výstupy modelu na možné úniky dat, škodlivý obsah nebo porušení bezpečnostních politik
- **Ochrana kontextového okna**: Implementovat kontroly zabraňující otravě a manipulaci kontextového okna

### 10. Bezpečnost spuštění nástrojů
- **Sandboxing spuštění**: Spouštět nástroje v kontejnerizovaných, izolovaných prostředích s omezením zdrojů
- **Oddělení oprávnění**: Spouštět nástroje s minimálními potřebnými oprávněními a oddělenými servisními účty
- **Síťová izolace**: Implementovat segmentaci sítě pro prostředí spuštění nástrojů
- **Monitorování spuštění**: Monitorovat spuštění nástrojů na anomální chování, využití zdrojů a bezpečnostní porušení

### 11. Kontinuální validace bezpečnosti
- **Automatizované bezpečnostní testování**: Integrovat bezpečnostní testování do CI/CD pipeline s nástroji jako GitHub Advanced Security
- **Správa zranitelností**: Pravidelně skenovat všechny závislosti včetně AI modelů a externích služeb
- **Penetrační testování**: Provádět pravidelné bezpečnostní audity zaměřené specificky na implementace MCP
- **Bezpečnostní revize kódu**: Implementovat povinné bezpečnostní revize pro všechny změny kódu související s MCP

### 12. Bezpečnost dodavatelského řetězce pro AI
- **Ověření komponent**: Ověřovat původ, integritu a bezpečnost všech AI komponent (modely, embeddingy, API)
- **Správa závislostí**: Udržovat aktuální inventáře všech softwarových a AI závislostí s evidencí zranitelností
- **Důvěryhodné repozitáře**: Používat ověřené, důvěryhodné zdroje pro všechny AI modely, knihovny a nástroje
- **Monitorování dodavatelského řetězce**: Nepřetržitě monitorovat kompromisy u poskytovatelů AI služeb a repozitářů modelů

## Pokročilé bezpečnostní vzory

### Architektura Zero Trust pro MCP
- **Nikdy nedůvěřuj, vždy ověřuj**: Implementovat kontinuální ověřování všech účastníků MCP
- **Mikrosegmentace**: Izolovat MCP komponenty s granulárními síťovými a identitními kontrolami
- **Podmíněný přístup**: Implementovat řízení přístupu založené na riziku, které se přizpůsobuje kontextu a chování
- **Kontinuální hodnocení rizik**: Dynamicky vyhodnocovat bezpečnostní postoj na základě aktuálních indikátorů hrozeb

### Implementace AI šetřící soukromí
- **Minimalizace dat**: Zveřejňovat pouze nezbytná data pro každou MCP operaci
- **Diferenciální soukromí**: Implementovat techniky zachovávající soukromí pro zpracování citlivých dat
- **Homomorfní šifrování**: Používat pokročilé šifrovací techniky pro bezpečné výpočty nad zašifrovanými daty
- **Federované učení**: Implementovat distribuované přístupy k učení, které zachovávají lokalitu dat a soukromí

### Reakce na incidenty pro AI systémy
- **Postupy specifické pro AI incidenty**: Vyvinout postupy reakce na incidenty přizpůsobené AI a MCP specifickým hrozbám
- **Automatizovaná reakce**: Implementovat automatizované zadržení a nápravu běžných AI bezpečnostních incidentů  
- **Forenzní schopnosti**: Udržovat forenzní připravenost pro kompromisy AI systémů a úniky dat
- **Postupy obnovy**: Zavést postupy pro obnovu po otravě AI modelů, útocích prompt injection a kompromitacích služeb

## Zdroje a standardy pro implementaci

### Oficiální dokumentace MCP
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Aktuální specifikace MCP protokolu
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Oficiální bezpečnostní doporučení
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Vzory autentizace a autorizace
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Požadavky na bezpečnost transportní vrstvy

### Microsoft bezpečnostní řešení
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Pokročilá ochrana proti prompt injection
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Komplexní filtrování AI obsahu
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Podnikové řízení identity a přístupu
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Bezpečná správa tajemství a přihlašovacích údajů
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Skenování bezpečnosti dodavatelského řetězce a kódu

### Bezpečnostní standardy a rámce
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Aktuální doporučení pro bezpečnost OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Rizika webových aplikací
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-specifická bezpečnostní rizika
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Komplexní řízení rizik AI
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Systémy řízení bezpečnosti informací

### Průvodce implementací a tutoriály
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Vzory podnikové autentizace
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integrace poskytovatele identity
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Osvědčené postupy správy tokenů
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Pokročilé vzory šifrování

### Pokročilé bezpečnostní zdroje
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Bezpečné vývojové postupy
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-specifické bezpečnostní testování
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologie modelování hrozeb AI
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Techniky zachování soukromí v AI

### Soulad a správa
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Soulad s ochranou soukromí v AI systémech
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Odpovědná implementace AI
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Bezpečnostní kontroly pro poskytovatele AI služeb
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Požadavky na soulad zdravotnických AI systémů

### DevSecOps a automatizace
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Bezpečné vývojové pipeline pro AI
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Kontinuální validace bezpečnosti
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Bezpečné nasazení infrastruktury
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Bezpečnost kontejnerizace AI zátěže

### Monitorování a reakce na incidenty  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Komplexní monitorovací řešení
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-specifické postupy reakce na incidenty
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Správa bezpečnostních informací a událostí
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Zdroje hrozeb pro AI

## 🔄 Kontinuální zlepšování

### Zůstaňte aktuální s vyvíjejícími se standardy
- **Aktualizace specifikace MCP**: Sledujte oficiální změny specifikace MCP a bezpečnostní upozornění
- **Hrozbová inteligence**: Přihlašujte se k odběru AI bezpečnostních hrozeb a databází zranitelností  
- **Zapojení komunity**: Účastněte se diskuzí a pracovních skupin MCP bezpečnostní komunity
- **Pravidelné hodnocení**: Provádějte čtvrtletní hodnocení bezpečnostního stavu a aktualizujte postupy podle potřeby

### Přispívání k bezpečnosti MCP
- **Bezpečnostní výzkum**: Přispívejte do výzkumu bezpečnosti MCP a programů zveřejňování zranitelností
- **Sdílení osvědčených postupů**: Sdílejte implementace bezpečnosti a získané zkušenosti s komunitou
- **Standardní vývoj**: Účast na vývoji specifikace MCP a tvorbě bezpečnostních standardů  
- **Vývoj nástrojů**: Vývoj a sdílení bezpečnostních nástrojů a knihoven pro ekosystém MCP

---

*Tento dokument odráží nejlepší bezpečnostní postupy MCP k 18. prosinci 2025, založené na specifikaci MCP 2025-11-25. Bezpečnostní postupy by měly být pravidelně přezkoumávány a aktualizovány s vývojem protokolu a hrozeb.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->