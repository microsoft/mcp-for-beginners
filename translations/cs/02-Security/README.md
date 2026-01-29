# MCP Security: Komplexní ochrana AI systémů

[![MCP Security Best Practices](../../../translated_images/cs/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Klikněte na obrázek výše pro zobrazení videa této lekce)_

Bezpečnost je základem návrhu AI systémů, proto ji upřednostňujeme jako naši druhou sekci. To je v souladu s principem Microsoftu **Secure by Design** z [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) přináší výkonné nové schopnosti do aplikací řízených AI, zároveň však zavádí jedinečné bezpečnostní výzvy, které přesahují tradiční softwarová rizika. Systémy MCP čelí jak zavedeným bezpečnostním problémům (bezpečné kódování, princip nejmenších oprávnění, bezpečnost dodavatelského řetězce), tak novým hrozbám specifickým pro AI, včetně prompt injection, otravy nástrojů, únosu relace, útoků confused deputy, zranitelností token passthrough a dynamické modifikace schopností.

Tato lekce zkoumá nejkritičtější bezpečnostní rizika v implementacích MCP — pokrývá autentizaci, autorizaci, nadměrná oprávnění, nepřímý prompt injection, bezpečnost relací, problémy confused deputy, správu tokenů a zranitelnosti dodavatelského řetězce. Naučíte se praktická opatření a osvědčené postupy pro zmírnění těchto rizik a zároveň využijete řešení Microsoftu jako Prompt Shields, Azure Content Safety a GitHub Advanced Security ke zvýšení bezpečnosti vaší MCP implementace.

## Výukové cíle

Na konci této lekce budete schopni:

- **Identifikovat hrozby specifické pro MCP**: Rozpoznat jedinečná bezpečnostní rizika v systémech MCP včetně prompt injection, otravy nástrojů, nadměrných oprávnění, únosu relace, problémů confused deputy, zranitelností token passthrough a rizik dodavatelského řetězce
- **Aplikovat bezpečnostní kontroly**: Implementovat účinná opatření včetně robustní autentizace, přístupu s nejmenšími oprávněními, bezpečné správy tokenů, kontrol bezpečnosti relací a ověřování dodavatelského řetězce
- **Využít bezpečnostní řešení Microsoftu**: Porozumět a nasadit Microsoft Prompt Shields, Azure Content Safety a GitHub Advanced Security pro ochranu MCP workloadů
- **Ověřit bezpečnost nástrojů**: Uvědomit si důležitost validace metadat nástrojů, monitorování dynamických změn a obrany proti nepřímým prompt injection útokům
- **Integrovat osvědčené postupy**: Kombinovat zavedené bezpečnostní základy (bezpečné kódování, zpevnění serveru, zero trust) s kontrolami specifickými pro MCP pro komplexní ochranu

# Architektura a kontroly bezpečnosti MCP

Moderní implementace MCP vyžadují vrstvené bezpečnostní přístupy, které řeší jak tradiční softwarovou bezpečnost, tak hrozby specifické pro AI. Rychle se vyvíjející specifikace MCP nadále zdokonaluje své bezpečnostní kontroly, což umožňuje lepší integraci s podnikovými bezpečnostními architekturami a zavedenými osvědčenými postupy.

Výzkum z [Microsoft Digital Defense Report](https://aka.ms/mddr) ukazuje, že **98 % hlášených průniků by bylo zabráněno robustní bezpečnostní hygienou**. Nejefektivnější strategie ochrany kombinuje základní bezpečnostní praktiky s kontrolami specifickými pro MCP — osvědčená základní bezpečnostní opatření zůstávají nejúčinnější při snižování celkového bezpečnostního rizika.

## Současná bezpečnostní situace

> **Poznámka:** Tyto informace odrážejí bezpečnostní standardy MCP k **18. prosinci 2025**. Protokol MCP se rychle vyvíjí a budoucí implementace mohou zavést nové vzory autentizace a vylepšené kontroly. Vždy se odkazujte na aktuální [MCP Specification](https://spec.modelcontextprotocol.io/), [MCP GitHub repository](https://github.com/modelcontextprotocol) a [dokumentaci osvědčených bezpečnostních postupů](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) pro nejnovější pokyny.

### Vývoj autentizace MCP

Specifikace MCP se významně vyvinula ve svém přístupu k autentizaci a autorizaci:

- **Původní přístup**: Rané specifikace vyžadovaly, aby vývojáři implementovali vlastní autentizační servery, přičemž MCP servery fungovaly jako OAuth 2.0 autorizační servery spravující autentizaci uživatelů přímo
- **Současný standard (2025-11-25)**: Aktualizovaná specifikace umožňuje MCP serverům delegovat autentizaci na externí poskytovatele identity (např. Microsoft Entra ID), což zlepšuje bezpečnostní postoj a snižuje složitost implementace
- **Transport Layer Security**: Vylepšená podpora bezpečných transportních mechanismů s vhodnými autentizačními vzory pro lokální (STDIO) i vzdálená (Streamable HTTP) připojení

## Bezpečnost autentizace a autorizace

### Současné bezpečnostní výzvy

Moderní implementace MCP čelí několika výzvám v oblasti autentizace a autorizace:

### Rizika a vektory útoků

- **Chybně nakonfigurovaná logika autorizace**: Chybná implementace autorizace v MCP serverech může odhalit citlivá data a nesprávně aplikovat přístupová oprávnění
- **Kompromitace OAuth tokenů**: Krádež tokenů lokálního MCP serveru umožňuje útočníkům vydávat se za servery a přistupovat k downstream službám
- **Zranitelnosti token passthrough**: Nesprávné zacházení s tokeny vytváří obcházení bezpečnostních kontrol a mezery v odpovědnosti
- **Nadměrná oprávnění**: Přehnaně privilegované MCP servery porušují princip nejmenších oprávnění a rozšiřují povrch útoku

#### Token passthrough: Kritický anti-vzor

**Token passthrough je v současné specifikaci autorizace MCP výslovně zakázán** kvůli závažným bezpečnostním důsledkům:

##### Obcházení bezpečnostních kontrol
- MCP servery a downstream API implementují klíčové bezpečnostní kontroly (omezení rychlosti, validace požadavků, monitorování provozu), které závisí na správné validaci tokenů
- Přímé použití tokenů klientem k API obchází tyto nezbytné ochrany a podkopává bezpečnostní architekturu

##### Výzvy v odpovědnosti a auditu  
- MCP servery nemohou rozlišit klienty používající tokeny vydané upstream, což narušuje auditní stopy
- Logy downstream serverů zdrojů ukazují zavádějící původ požadavků místo skutečných MCP serverů jako prostředníků
- Vyšetřování incidentů a audit shody se výrazně ztěžuje

##### Rizika exfiltrace dat
- Nevalidované nároky tokenů umožňují škodlivým aktérům s ukradenými tokeny používat MCP servery jako proxy pro exfiltraci dat
- Porušení hranic důvěry umožňuje neoprávněné přístupové vzory, které obcházejí zamýšlené bezpečnostní kontroly

##### Víceslužbové vektory útoků
- Kompromitované tokeny akceptované více službami umožňují laterální pohyb napříč propojenými systémy
- Důvěryhodné předpoklady mezi službami mohou být porušeny, pokud nelze ověřit původ tokenů

### Bezpečnostní kontroly a mitigace

**Kritické bezpečnostní požadavky:**

> **POVINNÉ**: MCP servery **NESMÍ** přijímat žádné tokeny, které nebyly explicitně vydány pro daný MCP server

#### Kontroly autentizace a autorizace

- **Důkladná revize autorizace**: Proveďte komplexní audity logiky autorizace MCP serverů, aby měli přístup pouze zamýšlení uživatelé a klienti k citlivým zdrojům
  - **Průvodce implementací**: [Azure API Management jako autentizační brána pro MCP servery](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrace identity**: [Použití Microsoft Entra ID pro autentizaci MCP serverů](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Bezpečná správa tokenů**: Implementujte [nejlepší postupy Microsoftu pro validaci a životní cyklus tokenů](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validujte nároky audience tokenů odpovídající identitě MCP serveru
  - Implementujte správnou rotaci a expiraci tokenů
  - Zabraňte opakovanému použití tokenů a neoprávněnému použití

- **Chráněné ukládání tokenů**: Zabezpečte ukládání tokenů šifrováním v klidu i při přenosu
  - **Osvědčené postupy**: [Pokyny pro bezpečné ukládání a šifrování tokenů](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementace řízení přístupu

- **Princip nejmenších oprávnění**: Udělujte MCP serverům pouze minimální oprávnění potřebná pro zamýšlenou funkčnost
  - Pravidelné revize a aktualizace oprávnění k zabránění jejich nárůstu
  - **Dokumentace Microsoftu**: [Bezpečný přístup s nejmenšími oprávněními](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Role-based Access Control (RBAC)**: Implementujte jemně zrnité přiřazení rolí
  - Přesně omezte role na konkrétní zdroje a akce
  - Vyhněte se širokým nebo zbytečným oprávněním, která rozšiřují povrch útoku

- **Kontinuální monitorování oprávnění**: Zavádějte průběžný audit a monitorování přístupu
  - Sledujte vzory používání oprávnění pro anomálie
  - Okamžitě odstraňujte nadměrná nebo nepoužívaná oprávnění

## Bezpečnostní hrozby specifické pro AI

### Útoky prompt injection a manipulace s nástroji

Moderní implementace MCP čelí sofistikovaným AI-specifickým vektorům útoků, které tradiční bezpečnostní opatření nemohou plně řešit:

#### **Nepřímý prompt injection (Cross-Domain Prompt Injection)**

**Nepřímý prompt injection** představuje jednu z nejkritičtějších zranitelností v AI systémech s MCP. Útočníci vkládají škodlivé instrukce do externího obsahu — dokumentů, webových stránek, e-mailů nebo datových zdrojů — které AI systémy následně zpracovávají jako legitimní příkazy.

**Scénáře útoků:**
- **Injection založený na dokumentech**: Škodlivé instrukce skryté v zpracovávaných dokumentech, které spouštějí nechtěné AI akce
- **Využití webového obsahu**: Kompromitované webové stránky obsahující vložené prompty, které manipulují chování AI při scrapování
- **Útoky založené na e-mailech**: Škodlivé prompty v e-mailech, které způsobují únik informací nebo neautorizované akce AI asistenta
- **Kontaminace datových zdrojů**: Kompromitované databáze nebo API poskytující znečištěný obsah AI systémům

**Reálný dopad**: Tyto útoky mohou vést k exfiltraci dat, porušení soukromí, generování škodlivého obsahu a manipulaci s uživatelskými interakcemi. Pro podrobnou analýzu viz [Prompt Injection v MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/cs/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Útoky otravy nástrojů**

**Otrava nástrojů** cílí na metadata definující MCP nástroje, zneužívajíc způsob, jakým LLM interpretují popisy nástrojů a parametry pro rozhodování o vykonání.

**Mechanismy útoku:**
- **Manipulace s metadaty**: Útočníci vkládají škodlivé instrukce do popisů nástrojů, definic parametrů nebo příkladů použití
- **Neviditelné instrukce**: Skryté prompty v metadatech nástrojů, které zpracovávají AI modely, ale jsou neviditelné pro lidské uživatele
- **Dynamická modifikace nástrojů („Rug Pulls“) **: Nástroje schválené uživateli jsou později modifikovány k provádění škodlivých akcí bez vědomí uživatele
- **Injection parametrů**: Škodlivý obsah vložený do schémat parametrů nástrojů, který ovlivňuje chování modelu

**Rizika hostovaných serverů**: Vzdálené MCP servery představují zvýšená rizika, protože definice nástrojů mohou být aktualizovány po počátečním schválení uživatelem, což vytváří scénáře, kdy dříve bezpečné nástroje se stanou škodlivými. Pro komplexní analýzu viz [Útoky otravy nástrojů (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/cs/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Další AI vektory útoků**

- **Cross-Domain Prompt Injection (XPIA)**: Sofistikované útoky využívající obsah z více domén k obcházení bezpečnostních kontrol
- **Dynamická modifikace schopností**: Změny schopností nástrojů v reálném čase, které unikají počátečnímu bezpečnostnímu hodnocení
- **Poisoning kontextového okna**: Útoky manipulující velká kontextová okna k skrytí škodlivých instrukcí
- **Útoky zmatení modelu**: Využití omezení modelu k vytváření nepředvídatelného nebo nebezpečného chování

### Dopad bezpečnostních rizik AI

**Důsledky s vysokým dopadem:**
- **Exfiltrace dat**: Neoprávněný přístup a krádež citlivých podnikových nebo osobních dat
- **Porušení soukromí**: Únik osobních identifikovatelných informací (PII) a důvěrných obchodních dat  
- **Manipulace se systémy**: Nezamýšlené modifikace kritických systémů a pracovních postupů
- **Krádež přihlašovacích údajů**: Kompromitace autentizačních tokenů a přihlašovacích údajů služeb
- **Laterální pohyb**: Využití kompromitovaných AI systémů jako pivotů pro širší síťové útoky

### Bezpečnostní řešení Microsoft AI

#### **AI Prompt Shields: Pokročilá ochrana proti injection útokům**

Microsoft **AI Prompt Shields** poskytují komplexní obranu proti přímým i nepřímým prompt injection útokům prostřednictvím více bezpečnostních vrstev:

##### **Základní ochranné mechanismy:**

1. **Pokročilá detekce a filtrování**
   - Algoritmy strojového učení a NLP techniky detekují škodlivé instrukce v externím obsahu
   - Analýza v reálném čase dokumentů, webových stránek, e-mailů a datových zdrojů na vložené hrozby
   - Kontextuální porozumění legitimním vs. škodlivým vzorům promptů

2. **Techniky zvýraznění**  
   - Rozlišuje mezi důvěryhodnými systémovými instrukcemi a potenciálně kompromitovanými externími vstupy
   - Metody transformace textu, které zvyšují relevanci modelu a zároveň izolují škodlivý obsah
   - Pomáhá AI systémům udržet správnou hierarchii instrukcí a ignorovat vložené příkazy

3. **Systémy oddělovačů a datových značek**
   - Explicitní definice hranic mezi důvěryhodnými systémovými zprávami a externím vstupním textem
   - Speciální značky zvýrazňující hranice mezi důvěryhodnými a nedůvěryhodnými datovými zdroji
   - Jasné oddělení zabraňuje záměně instrukcí a neautorizovanému vykonání příkazů

4. **Kontinuální zpravodajství o hrozbách**
   - Microsoft průběžně monitoruje nové vzory útoků a aktualizuje obrany
   - Proaktivní vyhledávání hrozeb nových injection technik a vektorů útoků
   - Pravidelné aktualizace bezpečnostních modelů pro udržení účinnosti proti vyvíjejícím se hrozbám

5. **Integrace Azure Content Safety**
   - Součást komplexního balíčku Azure AI Content Safety
   - Dodatečná detekce pokusů o jailbreak, škodlivého obsahu a porušení bezpečnostních politik
   - Jednotné bezpečnostní kontroly napříč komponentami AI aplikací

**Implementační zdroje**: [Dokumentace Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/cs/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Pokročilé bezpečnostní hrozby MCP

### Zranitelnosti únosu relace

**Únos relace** představuje kritický vektor útoku v stavových implementacích MCP, kde neoprávněné strany získají a zneužijí legitimní identifikátory relací k vydávání se za klienty a provádění neautorizovaných akcí.

#### **Scénáře útoků a rizika**

- **Prompt injection při únosu relace**: Útočníci s ukradenými ID relací vkládají škodlivé události do serverů sdílejících stav relace, což může spustit škodlivé akce nebo přístup k citlivým datům
- **Přímé vydávání se za uživatele**: Ukradená ID relací umožňují přímé volání MCP serveru, které obchází autentizaci a chovají se jako legitimní uživatelé
- **Kompromitované obnovitelné streamy**: Útočníci mohou předčasně ukončit požadavky, což způsobí, že legitimní klienti obnoví relaci s potenciálně škodlivým obsahem

#### **Bezpečnostní kontroly pro správu relací**

**Kritické požadavky:**
- **Ověření autorizace**: Servery MCP implementující autorizaci **MUSÍ** ověřovat VŠECHNY příchozí požadavky a **NESMÍ** se spoléhat na relace pro autentizaci
- **Bezpečná generace relací**: Používejte kryptograficky bezpečné, nedeterministické ID relací generované pomocí bezpečných generátorů náhodných čísel
- **Vázání na uživatele**: Vázat ID relací na uživatelsky specifické informace pomocí formátů jako `<user_id>:<session_id>`, aby se zabránilo zneužití relací mezi uživateli
- **Správa životního cyklu relace**: Implementujte správné vypršení platnosti, rotaci a neplatnost, aby se omezila zranitelná okna
- **Zabezpečení přenosu**: Povinné HTTPS pro veškerou komunikaci, aby se zabránilo zachycení ID relace

### Problém zmateného zástupce

**Problém zmateného zástupce** nastává, když servery MCP fungují jako autentizační proxy mezi klienty a službami třetích stran, což vytváří příležitosti pro obejití autorizace prostřednictvím zneužití statických ID klientů.

#### **Mechanika útoku a rizika**

- **Obcházení souhlasu založené na cookies**: Předchozí autentizace uživatele vytváří cookies souhlasu, které útočníci zneužívají pomocí škodlivých autorizačních požadavků s upravenými URI pro přesměrování
- **Krádež autorizačního kódu**: Existující cookies souhlasu mohou způsobit, že autorizační servery přeskočí obrazovky souhlasu a přesměrují kódy na útočníkem kontrolované koncové body  
- **Neoprávněný přístup k API**: Ukradené autorizační kódy umožňují výměnu tokenů a impersonaci uživatele bez explicitního schválení

#### **Strategie zmírnění**

**Povinná opatření:**
- **Explicitní požadavky na souhlas**: Proxy servery MCP používající statická ID klientů **MUSÍ** získat souhlas uživatele pro každého dynamicky registrovaného klienta
- **Implementace bezpečnosti OAuth 2.1**: Dodržujte aktuální bezpečnostní postupy OAuth včetně PKCE (Proof Key for Code Exchange) pro všechny autorizační požadavky
- **Přísná validace klienta**: Implementujte důkladnou validaci URI pro přesměrování a identifikátorů klientů, aby se zabránilo zneužití

### Zranitelnosti přeposílání tokenů  

**Přeposílání tokenů** představuje explicitní anti-vzor, kdy servery MCP přijímají klientské tokeny bez řádné validace a přeposílají je do downstream API, čímž porušují specifikace autorizace MCP.

#### **Bezpečnostní dopady**

- **Obcházení kontrol**: Přímé použití tokenů klientem k API obchází kritická omezení rychlosti, validaci a monitorovací kontroly
- **Poškození auditních stop**: Tokeny vydané upstream znemožňují identifikaci klienta, což narušuje schopnost vyšetřování incidentů
- **Exfiltrace dat přes proxy**: Nevalidované tokeny umožňují škodlivým aktérům používat servery jako proxy pro neoprávněný přístup k datům
- **Porušení hranic důvěry**: Důvěra downstream služeb může být narušena, pokud nelze ověřit původ tokenů
- **Rozšíření útoků na více služeb**: Kompromitované tokeny akceptované napříč službami umožňují laterální pohyb

#### **Požadované bezpečnostní kontroly**

**Nezbytné požadavky:**
- **Validace tokenů**: Servery MCP **NESMÍ** přijímat tokeny, které nejsou explicitně vydány pro server MCP
- **Ověření publika tokenu**: Vždy validujte, že publikum tokenu odpovídá identitě serveru MCP
- **Správný životní cyklus tokenu**: Implementujte krátkodobé přístupové tokeny s bezpečnými postupy rotace


## Zabezpečení dodavatelského řetězce pro AI systémy

Zabezpečení dodavatelského řetězce se vyvinulo za hranice tradičních softwarových závislostí a zahrnuje celý AI ekosystém. Moderní implementace MCP musí důkladně ověřovat a monitorovat všechny AI součásti, protože každá představuje potenciální zranitelnost, která může ohrozit integritu systému.

### Rozšířené komponenty AI dodavatelského řetězce

**Tradiční softwarové závislosti:**
- Knihovny a frameworky s otevřeným zdrojovým kódem
- Kontejnerové obrazy a základní systémy  
- Vývojové nástroje a build pipeline
- Infrastrukturní komponenty a služby

**Specifické prvky AI dodavatelského řetězce:**
- **Základní modely**: Předtrénované modely od různých poskytovatelů vyžadující ověření původu
- **Služby vektorizace**: Externí služby pro vektorizaci a sémantické vyhledávání
- **Poskytovatelé kontextu**: Datové zdroje, znalostní báze a úložiště dokumentů  
- **API třetích stran**: Externí AI služby, ML pipeline a koncové body pro zpracování dat
- **Modelové artefakty**: Váhy, konfigurace a jemně doladěné varianty modelů
- **Zdrojová data pro trénink**: Datové sady používané pro trénink a doladění modelů

### Komplexní strategie zabezpečení dodavatelského řetězce

#### **Ověření komponent a důvěryhodnost**
- **Validace původu**: Ověřte původ, licencování a integritu všech AI komponent před integrací
- **Bezpečnostní hodnocení**: Provádějte skenování zranitelností a bezpečnostní revize modelů, datových zdrojů a AI služeb
- **Analýza reputace**: Hodnoťte bezpečnostní historii a postupy poskytovatelů AI služeb
- **Ověření souladu**: Zajistěte, že všechny komponenty splňují organizační bezpečnostní a regulační požadavky

#### **Bezpečné deployment pipeline**  
- **Automatizované CI/CD zabezpečení**: Integrujte bezpečnostní skenování v celém automatizovaném deployment pipeline
- **Integrita artefaktů**: Implementujte kryptografickou verifikaci všech nasazených artefaktů (kód, modely, konfigurace)
- **Postupné nasazení**: Používejte progresivní deployment strategie s bezpečnostní validací v každé fázi
- **Důvěryhodné repozitáře artefaktů**: Nasazujte pouze z ověřených, zabezpečených registrů a repozitářů artefaktů

#### **Kontinuální monitorování a reakce**
- **Skenování závislostí**: Průběžné monitorování zranitelností všech softwarových a AI komponent
- **Monitorování modelů**: Kontinuální hodnocení chování modelů, driftu výkonu a bezpečnostních anomálií
- **Sledování stavu služeb**: Monitorujte dostupnost, bezpečnostní incidenty a změny politik externích AI služeb
- **Integrace hrozeb**: Začleňte hrozebné zdroje specifické pro AI a ML bezpečnostní rizika

#### **Řízení přístupu a princip nejmenších oprávnění**
- **Oprávnění na úrovni komponent**: Omezte přístup k modelům, datům a službám na základě obchodní potřeby
- **Správa servisních účtů**: Implementujte dedikované servisní účty s minimálními potřebnými oprávněními
- **Segmentace sítě**: Izolujte AI komponenty a omezte síťový přístup mezi službami
- **Kontroly API gateway**: Používejte centralizované API brány pro řízení a monitorování přístupu k externím AI službám

#### **Reakce na incidenty a obnova**
- **Rychlé reakční postupy**: Zavedené procesy pro záplaty nebo výměnu kompromitovaných AI komponent
- **Rotace přihlašovacích údajů**: Automatizované systémy pro rotaci tajemství, API klíčů a servisních přihlašovacích údajů
- **Možnosti rollbacku**: Schopnost rychle vrátit předchozí známé dobré verze AI komponent
- **Obnova po narušení dodavatelského řetězce**: Specifické postupy pro reakci na kompromitace upstream AI služeb

### Microsoft bezpečnostní nástroje a integrace

**GitHub Advanced Security** poskytuje komplexní ochranu dodavatelského řetězce včetně:
- **Skenování tajemství**: Automatická detekce přihlašovacích údajů, API klíčů a tokenů v repozitářích
- **Skenování závislostí**: Hodnocení zranitelností open-source závislostí a knihoven
- **CodeQL analýza**: Statická analýza kódu pro bezpečnostní zranitelnosti a chyby v kódování
- **Přehledy dodavatelského řetězce**: Přehled o stavu zdraví a bezpečnosti závislostí

**Integrace Azure DevOps & Azure Repos:**
- Bezproblémová integrace bezpečnostního skenování napříč Microsoft vývojovými platformami
- Automatizované bezpečnostní kontroly v Azure Pipelines pro AI pracovní zátěže
- Vynucování politik pro bezpečné nasazení AI komponent

**Interní praktiky Microsoftu:**
Microsoft implementuje rozsáhlé bezpečnostní postupy dodavatelského řetězce napříč všemi produkty. Více o osvědčených přístupech najdete v [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Základní bezpečnostní osvědčené postupy

Implementace MCP dědí a staví na stávajícím bezpečnostním postoji vaší organizace. Posílení základních bezpečnostních praktik výrazně zvyšuje celkovou bezpečnost AI systémů a nasazení MCP.

### Základní bezpečnostní principy

#### **Bezpečné vývojové praktiky**
- **Soulad s OWASP**: Ochrana proti [OWASP Top 10](https://owasp.org/www-project-top-ten/) zranitelnostem webových aplikací
- **Specifické ochrany pro AI**: Implementace kontrol pro [OWASP Top 10 pro LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Bezpečná správa tajemství**: Používejte dedikované trezory pro tokeny, API klíče a citlivá konfigurační data
- **End-to-end šifrování**: Implementujte bezpečnou komunikaci ve všech aplikačních komponentách a datových tocích
- **Validace vstupů**: Přísná validace všech uživatelských vstupů, API parametrů a datových zdrojů

#### **Zpevnění infrastruktury**
- **Vícefaktorová autentizace**: Povinná MFA pro všechny administrativní a servisní účty
- **Správa záplat**: Automatizované a včasné záplatování operačních systémů, frameworků a závislostí  
- **Integrace poskytovatelů identity**: Centralizovaná správa identity přes podnikové identity providery (Microsoft Entra ID, Active Directory)
- **Segmentace sítě**: Logická izolace MCP komponent pro omezení laterálního pohybu
- **Princip nejmenších oprávnění**: Minimální potřebná oprávnění pro všechny systémové komponenty a účty

#### **Monitorování a detekce bezpečnosti**
- **Komplexní logování**: Detailní logování aktivit AI aplikací včetně interakcí klient-server MCP
- **Integrace SIEM**: Centralizované řízení bezpečnostních informací a událostí pro detekci anomálií
- **Behaviorální analýza**: AI-poháněné monitorování pro detekci neobvyklých vzorců v chování systému a uživatelů
- **Hrozebná inteligence**: Integrace externích zdrojů hrozeb a indikátorů kompromitace (IOC)
- **Reakce na incidenty**: Dobře definované postupy pro detekci, reakci a obnovu po bezpečnostních incidentech

#### **Architektura Zero Trust**
- **Nikdy nedůvěřuj, vždy ověřuj**: Kontinuální ověřování uživatelů, zařízení a síťových připojení
- **Mikrosegmentace**: Granulární síťové kontroly izolující jednotlivé pracovní zátěže a služby
- **Bezpečnost zaměřená na identitu**: Bezpečnostní politiky založené na ověřených identitách místo na síťové lokaci
- **Kontinuální hodnocení rizik**: Dynamické vyhodnocování bezpečnostního postoje na základě aktuálního kontextu a chování
- **Podmíněný přístup**: Přístupové kontroly přizpůsobující se na základě rizikových faktorů, lokace a důvěryhodnosti zařízení

### Vzory integrace do podniku

#### **Integrace do Microsoft bezpečnostního ekosystému**
- **Microsoft Defender for Cloud**: Komplexní řízení bezpečnostního postoje cloudů
- **Azure Sentinel**: Nativní cloudové SIEM a SOAR schopnosti pro ochranu AI pracovních zátěží
- **Microsoft Entra ID**: Podnikové řízení identity a přístupu s politikami podmíněného přístupu
- **Azure Key Vault**: Centralizovaná správa tajemství s podporou hardwarových bezpečnostních modulů (HSM)
- **Microsoft Purview**: Správa dat a souladu pro AI datové zdroje a workflow

#### **Soulad a správa**
- **Soulad s regulacemi**: Zajistěte, že implementace MCP splňují průmyslové regulační požadavky (GDPR, HIPAA, SOC 2)
- **Klasifikace dat**: Správná kategorizace a nakládání s citlivými daty zpracovávanými AI systémy
- **Auditní stopy**: Komplexní logování pro regulační soulad a forenzní vyšetřování
- **Ochrana soukromí**: Implementace principů privacy-by-design v architektuře AI systémů
- **Řízení změn**: Formální procesy pro bezpečnostní revize modifikací AI systémů

Tyto základní praktiky vytvářejí robustní bezpečnostní základnu, která zvyšuje účinnost specifických bezpečnostních kontrol MCP a poskytuje komplexní ochranu AI aplikací.

## Klíčové bezpečnostní poznatky

- **Vícevrstvý bezpečnostní přístup**: Kombinujte základní bezpečnostní praktiky (bezpečné kódování, princip nejmenších oprávnění, ověřování dodavatelského řetězce, kontinuální monitorování) s AI-specifickými kontrolami pro komplexní ochranu

- **Specifické hrozby AI**: Systémy MCP čelí unikátním rizikům včetně injekce promptů, otravy nástrojů, únosu relací, problému zmateného zástupce, zranitelností přeposílání tokenů a nadměrných oprávnění, které vyžadují specializovaná zmírnění

- **Excelence v autentizaci a autorizaci**: Implementujte robustní autentizaci pomocí externích poskytovatelů identity (Microsoft Entra ID), vynucujte správnou validaci tokenů a nikdy nepřijímejte tokeny nevydané explicitně pro váš MCP server

- **Prevence AI útoků**: Nasazujte Microsoft Prompt Shields a Azure Content Safety pro obranu proti nepřímé injekci promptů a otravě nástrojů, zároveň validujte metadata nástrojů a monitorujte dynamické změny

- **Bezpečnost relací a přenosu**: Používejte kryptograficky bezpečná, nedeterministická ID relací vázaná na uživatelské identity, implementujte správnou správu životního cyklu relace a nikdy nepoužívejte relace pro autentizaci

- **Nejlepší postupy OAuth bezpečnosti**: Zabraňte útokům zmateného zástupce explicitním souhlasem uživatele pro dynamicky registrované klienty, správnou implementací OAuth 2.1 s PKCE a přísnou validací URI pro přesměrování  

- **Principy bezpečnosti tokenů**: Vyhněte se anti-vzoru přeposílání tokenů, validujte publikum tokenů, implementujte krátkodobé tokeny s bezpečnou rotací a udržujte jasné hranice důvěry

- **Komplexní zabezpečení dodavatelského řetězce**: Zacházejte se všemi komponentami AI ekosystému (modely, embeddingy, poskytovatelé kontextu, externí API) se stejnou bezpečnostní přísností jako s tradičními softwarovými závislostmi

- **Kontinuální vývoj**: Sledujte rychle se vyvíjející specifikace MCP, přispívejte do bezpečnostních komunitních standardů a udržujte adaptivní bezpečnostní postoje s vývojem protokolu

- **Integrace Microsoft bezpečnosti**: Využívejte komplexní bezpečnostní ekosystém Microsoftu (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) pro zvýšenou ochranu nasazení MCP

## Komplexní zdroje

### **Oficiální dokumentace MCP bezpečnosti**
- [Specifikace MCP (aktuální: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Nejlepší bezpečnostní praktiky MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Specifikace autorizace MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [GitHub repozitář MCP](https://github.com/modelcontextprotocol)

### **Bezpečnostní standardy a osvědčené postupy**
- [OAuth 2.0 bezpečnostní osvědčené postupy (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 bezpečnost webových aplikací](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 pro velké jazykové modely](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Výzkum a analýza AI bezpečnosti**
- [Injekce promptů v MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Útoky otravy nástrojů (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Bezpečnostní výzkumné shrnutí (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Bezpečnostní řešení**
- [Dokumentace Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Služba Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Bezpečnost](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Nejlepší postupy správy tokenů Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Pokročilá bezpečnost](https://github.com/security/advanced-security)

### **Průvodci implementací a návody**
- [Azure API Management jako MCP autentizační brána](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID autentizace s MCP servery](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Bezpečné ukládání a šifrování tokenů (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps a bezpečnost dodavatelského řetězce**
- [Azure DevOps bezpečnost](https://azure.microsoft.com/products/devops)
- [Azure Repos bezpečnost](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft cesta k bezpečnosti dodavatelského řetězce](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Další bezpečnostní dokumentace**

Pro komplexní bezpečnostní pokyny se podívejte na tyto specializované dokumenty v této sekci:

- **[MCP Bezpečnostní nejlepší postupy 2025](./mcp-security-best-practices-2025.md)** - Kompletní nejlepší bezpečnostní postupy pro implementace MCP
- **[Implementace Azure Content Safety](./azure-content-safety-implementation.md)** - Praktické příklady implementace integrace Azure Content Safety  
- **[MCP Bezpečnostní kontroly 2025](./mcp-security-controls-2025.md)** - Nejnovější bezpečnostní kontroly a techniky pro nasazení MCP
- **[Rychlý přehled nejlepších postupů MCP](./mcp-best-practices.md)** - Rychlý referenční průvodce základními bezpečnostními postupy MCP

---

## Co dál

Další: [Kapitola 3: Začínáme](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->