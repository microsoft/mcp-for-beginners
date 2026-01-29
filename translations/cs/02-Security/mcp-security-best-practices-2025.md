# MCP Bezpečnostní osvědčené postupy - aktualizace prosinec 2025

> **Důležité**: Tento dokument odráží nejnovější bezpečnostní požadavky [MCP specifikace 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) a oficiální [MCP bezpečnostní osvědčené postupy](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Vždy se odkazujte na aktuální specifikaci pro nejnovější pokyny.

## Základní bezpečnostní postupy pro implementace MCP

Model Context Protocol přináší jedinečné bezpečnostní výzvy, které přesahují tradiční bezpečnost softwaru. Tyto postupy řeší jak základní bezpečnostní požadavky, tak MCP-specifické hrozby včetně injekce promptů, otravy nástrojů, únosu relací, problémů s „confused deputy“ a zranitelností při předávání tokenů.

### **POVINNÉ bezpečnostní požadavky**

**Kritické požadavky ze specifikace MCP:**

### **POVINNÉ bezpečnostní požadavky**

**Kritické požadavky ze specifikace MCP:**

> **NESMÍ**: MCP servery **NESMÍ** přijímat žádné tokeny, které nebyly explicitně vydány pro MCP server  
>  
> **MUSÍ**: MCP servery implementující autorizaci **MUSÍ** ověřovat VŠECHNY příchozí požadavky  
>  
> **NESMÍ**: MCP servery **NESMÍ** používat relace pro autentizaci  
>  
> **MUSÍ**: MCP proxy servery používající statická ID klientů **MUSÍ** získat souhlas uživatele pro každého dynamicky registrovaného klienta

---

## 1. **Bezpečnost tokenů a autentizace**

**Kontroly autentizace a autorizace:**  
   - **Důkladná revize autorizace**: Provádějte komplexní audity logiky autorizace MCP serveru, aby měli přístup pouze zamýšlení uživatelé a klienti  
   - **Integrace externího poskytovatele identity**: Používejte zavedené poskytovatele identity jako Microsoft Entra ID místo vlastních autentizačních řešení  
   - **Validace publika tokenu**: Vždy ověřujte, že tokeny byly explicitně vydány pro váš MCP server – nikdy nepřijímejte tokeny z vyšších vrstev  
   - **Správný životní cyklus tokenů**: Implementujte bezpečnou rotaci tokenů, politiky expirace a zabraňte opakovanému použití tokenů

**Chráněné ukládání tokenů:**  
   - Používejte Azure Key Vault nebo podobné bezpečné úložiště pro všechny tajné klíče  
   - Implementujte šifrování tokenů v klidu i při přenosu  
   - Pravidelná rotace přihlašovacích údajů a monitorování neoprávněného přístupu

## 2. **Správa relací a bezpečnost přenosu**

**Bezpečné praktiky správy relací:**  
   - **Kryptograficky bezpečná ID relací**: Používejte bezpečná, nedeterministická ID relací generovaná bezpečnými generátory náhodných čísel  
   - **Vazba na uživatele**: Vazba ID relace na identitu uživatele pomocí formátů jako `<user_id>:<session_id>` pro zabránění zneužití relace mezi uživateli  
   - **Správa životního cyklu relace**: Implementujte správnou expiraci, rotaci a neplatnost pro omezení zranitelných období  
   - **Vynucení HTTPS/TLS**: Povinné HTTPS pro veškerou komunikaci, aby se zabránilo zachycení ID relace

**Bezpečnost transportní vrstvy:**  
   - Konfigurujte TLS 1.3 kde je to možné s řádnou správou certifikátů  
   - Implementujte pinning certifikátů pro kritická spojení  
   - Pravidelná rotace certifikátů a ověřování platnosti

## 3. **Ochrana proti AI-specifickým hrozbám** 🤖

**Obrana proti injekci promptů:**  
   - **Microsoft Prompt Shields**: Nasazení AI Prompt Shields pro pokročilou detekci a filtrování škodlivých instrukcí  
   - **Sanitizace vstupů**: Validujte a sanitizujte všechny vstupy, aby se zabránilo injekčním útokům a problémům „confused deputy“  
   - **Obsahové hranice**: Používejte oddělovače a systémy datamarkingu k rozlišení důvěryhodných instrukcí od externího obsahu

**Prevence otravy nástrojů:**  
   - **Validace metadat nástrojů**: Implementujte kontroly integrity definic nástrojů a monitorujte neočekávané změny  
   - **Dynamické monitorování nástrojů**: Sledujte chování za běhu a nastavte upozornění na neočekávané vzory vykonávání  
   - **Schvalovací workflow**: Vyžadujte explicitní schválení uživatelem pro změny nástrojů a jejich schopností

## 4. **Řízení přístupu a oprávnění**

**Princip nejmenších oprávnění:**  
   - Udělujte MCP serverům pouze minimální oprávnění potřebná pro zamýšlenou funkčnost  
   - Implementujte řízení přístupu založené na rolích (RBAC) s jemně zrnkovanými oprávněními  
   - Pravidelné revize oprávnění a kontinuální monitorování eskalace oprávnění

**Kontroly oprávnění za běhu:**  
   - Aplikujte limity zdrojů, aby se zabránilo útokům vyčerpáním zdrojů  
   - Používejte izolaci kontejnerů pro prostředí vykonávání nástrojů  
   - Implementujte přístup „just-in-time“ pro administrativní funkce

## 5. **Bezpečnost obsahu a monitorování**

**Implementace bezpečnosti obsahu:**  
   - **Integrace Azure Content Safety**: Používejte Azure Content Safety k detekci škodlivého obsahu, pokusů o jailbreak a porušení politik  
   - **Behaviorální analýza**: Implementujte monitorování chování za běhu pro detekci anomálií v MCP serveru a vykonávání nástrojů  
   - **Komplexní logování**: Logujte všechny pokusy o autentizaci, volání nástrojů a bezpečnostní události s bezpečným, nezměnitelným uložením

**Kontinuální monitorování:**  
   - Upozornění v reálném čase na podezřelé vzory a neoprávněné pokusy o přístup  
   - Integrace se SIEM systémy pro centralizovanou správu bezpečnostních událostí  
   - Pravidelné bezpečnostní audity a penetrační testování implementací MCP

## 6. **Bezpečnost dodavatelského řetězce**

**Ověření komponent:**  
   - **Skenování závislostí**: Používejte automatizované skenování zranitelností pro všechny softwarové závislosti a AI komponenty  
   - **Validace původu**: Ověřujte původ, licencování a integritu modelů, datových zdrojů a externích služeb  
   - **Podepsané balíčky**: Používejte kryptograficky podepsané balíčky a ověřujte podpisy před nasazením

**Bezpečný vývojový pipeline:**  
   - **GitHub Advanced Security**: Implementujte skenování tajemství, analýzu závislostí a statickou analýzu CodeQL  
   - **Bezpečnost CI/CD**: Integrujte bezpečnostní validace do automatizovaných nasazovacích pipeline  
   - **Integrita artefaktů**: Implementujte kryptografickou verifikaci nasazených artefaktů a konfigurací

## 7. **OAuth bezpečnost a prevence „confused deputy“**

**Implementace OAuth 2.1:**  
   - **Implementace PKCE**: Používejte Proof Key for Code Exchange (PKCE) pro všechny autorizační požadavky  
   - **Explicitní souhlas**: Získejte souhlas uživatele pro každého dynamicky registrovaného klienta, aby se zabránilo útokům „confused deputy“  
   - **Validace redirect URI**: Implementujte přísnou validaci redirect URI a identifikátorů klientů

**Bezpečnost proxy:**  
   - Zabraňte obcházení autorizace zneužitím statických ID klientů  
   - Implementujte správné workflow souhlasu pro přístup třetích stran k API  
   - Monitorujte krádeže autorizačních kódů a neoprávněný přístup k API

## 8. **Reakce na incidenty a obnova**

**Schopnosti rychlé reakce:**  
   - **Automatizovaná reakce**: Implementujte automatizované systémy pro rotaci přihlašovacích údajů a omezení hrozeb  
   - **Postupy rollbacku**: Schopnost rychle vrátit konfigurace a komponenty do známého dobrého stavu  
   - **Forenzní schopnosti**: Detailní auditní stopy a logování pro vyšetřování incidentů

**Komunikace a koordinace:**  
   - Jasné postupy eskalace bezpečnostních incidentů  
   - Integrace s organizačními týmy pro reakci na incidenty  
   - Pravidelné simulace bezpečnostních incidentů a cvičení

## 9. **Soulad a správa**

**Regulační soulad:**  
   - Zajistěte, aby implementace MCP splňovaly požadavky specifické pro odvětví (GDPR, HIPAA, SOC 2)  
   - Implementujte klasifikaci dat a kontrolu soukromí pro zpracování AI dat  
   - Udržujte komplexní dokumentaci pro audity souladu

**Řízení změn:**  
   - Formální bezpečnostní revize všech změn MCP systémů  
   - Verzování a schvalovací workflow pro změny konfigurací  
   - Pravidelné hodnocení souladu a analýza mezer

## 10. **Pokročilé bezpečnostní kontroly**

**Architektura Zero Trust:**  
   - **Nikdy nedůvěřuj, vždy ověřuj**: Kontinuální ověřování uživatelů, zařízení a připojení  
   - **Mikrosegmentace**: Granulární síťové kontroly izolující jednotlivé MCP komponenty  
   - **Podmíněný přístup**: Řízení přístupu založené na riziku přizpůsobující se aktuálnímu kontextu a chování

**Ochrana aplikací za běhu:**  
   - **Runtime Application Self-Protection (RASP)**: Nasazení RASP technik pro detekci hrozeb v reálném čase  
   - **Monitorování výkonu aplikací**: Sledujte výkonnostní anomálie, které mohou indikovat útoky  
   - **Dynamické bezpečnostní politiky**: Implementujte bezpečnostní politiky, které se přizpůsobují aktuální hrozbové situaci

## 11. **Integrace s Microsoft bezpečnostním ekosystémem**

**Komplexní Microsoft bezpečnost:**  
   - **Microsoft Defender for Cloud**: Správa bezpečnostního postavení cloudu pro MCP workloady  
   - **Azure Sentinel**: Nativní cloudové SIEM a SOAR schopnosti pro pokročilou detekci hrozeb  
   - **Microsoft Purview**: Správa dat a soulad pro AI workflowy a datové zdroje

**Správa identity a přístupu:**  
   - **Microsoft Entra ID**: Podnikové řízení identity s podmíněnými přístupovými politikami  
   - **Privileged Identity Management (PIM)**: Přístup „just-in-time“ a schvalovací workflow pro administrativní funkce  
   - **Ochrana identity**: Řízení přístupu založené na riziku a automatizovaná reakce na hrozby

## 12. **Kontinuální vývoj bezpečnosti**

**Udržování aktuálnosti:**  
   - **Monitorování specifikace**: Pravidelná kontrola aktualizací MCP specifikace a změn bezpečnostních pokynů  
   - **Hrozbová inteligence**: Integrace AI-specifických hrozbových zdrojů a indikátorů kompromitace  
   - **Zapojení bezpečnostní komunity**: Aktivní účast v MCP bezpečnostní komunitě a programech zveřejňování zranitelností

**Adaptivní bezpečnost:**  
   - **Bezpečnost strojového učení**: Používejte ML založenou detekci anomálií pro identifikaci nových vzorů útoků  
   - **Prediktivní bezpečnostní analytika**: Implementujte prediktivní modely pro proaktivní identifikaci hrozeb  
   - **Automatizace bezpečnosti**: Automatizované aktualizace bezpečnostních politik na základě hrozbové inteligence a změn specifikace

---

## **Kritické bezpečnostní zdroje**

### **Oficiální dokumentace MCP**
- [MCP specifikace (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP bezpečnostní osvědčené postupy](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP autorizace specifikace](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft bezpečnostní řešení**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID bezpečnost](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Bezpečnostní standardy**
- [OAuth 2.0 bezpečnostní osvědčené postupy (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 pro velké jazykové modely](https://genai.owasp.org/)
- [NIST rámec řízení rizik AI](https://www.nist.gov/itl/ai-risk-management-framework)

### **Průvodce implementací**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID s MCP servery](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Bezpečnostní upozornění**: Bezpečnostní postupy MCP se rychle vyvíjejí. Vždy ověřujte podle aktuální [MCP specifikace](https://spec.modelcontextprotocol.io/) a [oficiální bezpečnostní dokumentace](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) před implementací.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->