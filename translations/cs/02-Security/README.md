# MCP bezpečnost: Komplexní ochrana pro AI systémy

[![MCP Security Best Practices](../../../translated_images/cs/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Klikněte na obrázek výše pro zobrazení videa této lekce)_

Bezpečnost je základem návrhu AI systémů, proto ji klademe na prioritu jako naši druhou sekci. To je v souladu s principem Microsoftu **Secure by Design** z [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) přináší silné nové schopnosti do aplikací řízených AI, přičemž zavádí jedinečné bezpečnostní výzvy, které přesahují tradiční softwarová rizika. Systémy MCP čelí jak zavedeným bezpečnostním problémům (bezpečný kód, princip nejmenších práv, bezpečnost dodavatelského řetězce), tak novým konkrétním hrozbám AI jako je injekce promptů, otrava nástrojů, únos sezení, útoky confused deputy, zranitelnosti přenosu tokenů a dynamické modifikace schopností.

Tato lekce zkoumá nejkritičtější bezpečnostní rizika v implementacích MCP—zahrnující autentizaci, autorizaci, nadměrná oprávnění, nepřímou injekci promptu, zabezpečení sezení, problémy confused deputy, správu tokenů a zranitelnosti dodavatelského řetězce. Naučíte se praktické kontroly a osvědčené postupy, jak tato rizika zmírnit a zároveň využít řešení Microsoftu jako Prompt Shields, Azure Content Safety a GitHub Advanced Security pro posílení vaší MCP nasazení.

## Výukové cíle

Na konci této lekce budete schopni:

- **Identifikovat specifické hrozby MCP**: Rozpoznat jedinečné bezpečnostní rizika v systémech MCP včetně injekce promptů, otravy nástrojů, nadměrných oprávnění, únosu sezení, problémů confused deputy, zranitelností přenosu tokenů a rizik dodavatelského řetězce
- **Aplikovat bezpečnostní kontroly**: Implementovat účinná zmírnění včetně robustní autentizace, přístupu s nejmenšími právy, bezpečné správy tokenů, bezpečnostních kontrol sezení a ověřování dodavatelského řetězce
- **Využít bezpečnostní řešení Microsoftu**: Rozumět a nasadit Microsoft Prompt Shields, Azure Content Safety a GitHub Advanced Security pro ochranu MCP pracovních zátěží
- **Ověřit bezpečnost nástrojů**: Rozpoznat význam validace metadat nástrojů, monitorování dynamických změn a obrany proti nepřímým injekčním útokům promptů
- **Integrovat osvědčené postupy**: Kombinovat zavedené základy bezpečnosti (bezpečné kódování, tvrzení serverů, zero trust) s MCP-specifickými kontrolami pro komplexní ochranu

# Architektura bezpečnosti MCP & kontroly

Moderní implementace MCP vyžadují vrstvené bezpečnostní přístupy, které řeší jak tradiční softwarovou bezpečnost, tak specifické hrozby AI. Rychle se vyvíjející specifikace MCP pokračuje v rozvoji svých bezpečnostních kontrol, umožňujících lepší integraci s podnikovými bezpečnostními architekturami a zavedenými osvědčenými postupy.

Výzkum z [Microsoft Digital Defense Report](https://aka.ms/mddr) ukazuje, že **98 % hlášených průniků by bylo zabráněno robustní bezpečnostní hygienou**. Nejefektivnější strategie ochrany kombinuje základní bezpečnostní praktiky s MCP-specifickými kontrolami—osvědčená základní bezpečnostní opatření zůstávají nejvlivnější v redukci celkového bezpečnostního rizika.

## Současná bezpečnostní situace

> **Poznámka:** Tato kapitola kombinuje zavedené bezpečnostní kontroly MCP s
> aktuálním **MCP Specification 2026-07-28** vedením k autorizaci. Vždy se odkazujte
> na aktuální [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHub repozitář](https://github.com/modelcontextprotocol) a
> [dokumentaci osvědčených bezpečnostních praktik](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> při implementaci kódu citlivého na bezpečnost.

> **Aktualizace autorizace:** MCP `2026-07-28` vyžaduje od klientů validaci
> parametru `iss` v odpovědích autorizace (RFC 9207) a svázání registrovaných
> přihlašovacích údajů s autorizačním serverem, který je vydal. Dynamická registrace klientů
> je zastaralá; nové implementace by měly používat dokumenty metadata klienta.
> Viz [Co se změnilo v MCP: Specifikace 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> pro úplný seznam změn v autorizaci.

## 🏔️ MCP Security Summit Workshop (Sherpa)

Pro **praktický bezpečnostní trénink** důrazně doporučujeme **MCP Security Summit Workshop** (Sherpa)—komplexní řízenou expedici k zabezpečení MCP serverů v Microsoft Azure.

### Přehled workshopu

[MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) poskytuje praktický, akcí řízený bezpečnostní trénink metodikou "zranitelnost → exploit → oprava → ověření". Budete:

- **Učit se prolomením**: Zažijete zranitelnosti přímo tím, že budete využívat úmyslně nezabezpečené servery
- **Používat nativní zabezpečení Azure**: Využijete Azure Entra ID, Key Vault, API Management a AI Content Safety
- **Dodržovat obranu do hloubky**: Projdete tábory budováním komplexních bezpečnostních vrstev
- **Aplikovat OWASP standardy**: Každá technika odpovídá [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- **Získat produkční kód**: Odejdete s funkčními, testovanými implementacemi

### Trasa expedice

| Tábor | Zaměření | Pokryté OWASP rizika |
|-------|----------|---------------------|
| **Základní tábor** | MCP základy & zranitelnosti autentizace | MCP01, MCP07 |
| **Tábor 1: Identita** | OAuth 2.1, spravovaná identita Azure, Key Vault | MCP01, MCP02, MCP07 |
| **Tábor 2: Brána** | API Management, soukromé endpointy, řízení | MCP02, MCP06, MCP07, MCP09 |
| **Tábor 3: I/O bezpečnost** | Injekce promptů, ochrana PII, bezpečnost obsahu | MCP03, MCP05, MCP06, MCP10 |
| **Tábor 4: Monitorování** | Log Analytics, panely, detekce hrozeb | MCP04, MCP08 |
| **Summit** | Integrace Red Team / Blue Team testování | Všechny |

**Začněte zde**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 bezpečnostních rizik

[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) popisuje deset nejkritičtějších bezpečnostních rizik pro implementace MCP:

| Riziko | Popis | Mitigace v Azure |
|--------|--------|------------------|
| **MCP01** | Nesprávná správa tokenů & expozice tajemství | Azure Key Vault, spravovaná identita |
| **MCP02** | Eskalace privilegii přes přidávání rozsahu | RBAC, podmíněný přístup |
| **MCP03** | Otrava nástrojů | Validace nástrojů, ověřování integrity |
| **MCP04** | Útoky na dodavatelský řetězec softwaru & manipulace závislostí | GitHub Advanced Security, skenování závislostí |
| **MCP05** | Injekce příkazů & exekuce | Validace vstupu, sandboxing |
| **MCP06** | Podvržení toku záměrů | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Nedostatečná autentizace & autorizace | Azure Entra ID, OAuth 2.1 s PKCE |
| **MCP08** | Nedostatek auditu a telemetrie | Azure Monitor, Application Insights |
| **MCP09** | Stínové MCP servery | Řízení API Center, izolace sítě |
| **MCP10** | Injekce kontextu & nadměrné sdílení | Klasifikace dat, minimální expozice |

### Vývoj autentizace MCP

Specifikace MCP se výrazně vyvinula ve svém přístupu k autentizaci a autorizaci:

- **Původní přístup**: Rané specifikace vyžadovaly, aby vývojáři implementovali vlastní autentizační servery, přičemž MCP servery fungovaly jako OAuth 2.0 autorizační servery, které přímo spravovaly autentizaci uživatelů
- **Současný standard (`2026-07-28`)**: MCP servery mohou delegovat autentizaci
  na externí identity poskytovatele jako Microsoft Entra ID. Klienti musí také
  aplikovat aktuální požadavky na validaci vydavatele a vázání přihlašovacích údajů.
- **Bezpečnost transportní vrstvy**: Vylepšená podpora bezpečných transportních mechanismů se správnými autentizačními vzory pro lokální (STDIO) i vzdálená (Streamable HTTP) spojení

## Bezpečnost autentizace & autorizace

### Současné bezpečnostní výzvy

Moderní implementace MCP čelí několika výzvám v autentizaci a autorizaci:

### Rizika a vektory hrozeb

- **Nesprávná logika autorizace**: Chybné provedení autorizace v MCP serverech může odhalit citlivá data a nesprávně aplikovat přístupové kontroly
- **Kompromitace OAuth tokenů**: Krádež tokenů lokálního MCP serveru umožňuje útočníkům vydávat se za server a získat přístup k následným službám
- **Zranitelností přenosu tokenů**: Nesprávné nakládání s tokeny vytváří obcházení bezpečnostních kontrol a mezery v odpovědnosti
- **Nadměrná oprávnění**: MCP servery s přílišnými právy porušují princip nejmenších práv a rozšiřují útočné povrchy

#### Přenos tokenu: Kritický anti-vzor

**Přenos tokenu je výslovně zakázán** v aktuální specifikaci autorizace MCP kvůli závažným bezpečnostním následkům:

##### Obcházení bezpečnostních kontrol
- MCP servery a následné API implementují kritické bezpečnostní kontroly (omezení rychlosti, validace požadavků, sledování provozu), které závisí na správné validaci tokenů
- Přímé používání tokenů klientem k API obchází tyto nezbytné ochrany a podrývá bezpečnostní architekturu

##### Výzvy k odpovědnosti a auditu  
- MCP servery nemohou rozlišit mezi klienty používajícími upstreamové tokeny, což porušuje auditní stopy
- Záznamy serverů zdrojových zdrojů vykazují mylné původy požadavků místo skutečných MCP serverů jako prostředníků
- Vyšetřování incidentů a audity shody jsou výrazně obtížnější

##### Rizika úniku dat
- Neověřené tokenové tvrzení umožňují škodlivým aktérům s ukradenými tokeny použít MCP servery jako proxy pro únik dat
- Porušení důvěrnostních hranic dovolují neautorizované vzory přístupu obcházející plánované bezpečnostní kontroly

##### Víceslužbové vektory útoku
- Kompromitované tokeny přijímané více službami umožňují laterální pohyb mezi propojenými systémy
- Důvěryhodné předpoklady mezi službami mohou být porušeny, když není možné ověřit původ tokenů

### Bezpečnostní kontroly a opatření

**Kritické bezpečnostní požadavky:**

> **POVINNÉ:** MCP servery **NESMÍ** přijímat žádné tokeny, které nebyly explicitně vydány pro daný MCP server

#### Kontroly autentizace a autorizace

- **Důkladné přezkoumání autorizace**: Proveďte komplexní audit logiky autorizace MCP serveru, aby měli přístup jen zamýšlení uživatelé a klienti k citlivým zdrojům
  - **Průvodce implementací**: [Azure API Management jako autentizační brána pro MCP servery](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrace identity**: [Použití Microsoft Entra ID k autentizaci MCP serveru](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Bezpečná správa tokenů**: Implementujte [Microsoftovy osvědčené postupy validace tokenů a životního cyklu](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validujte tvrzení audience tokenů odpovídající identitě MCP serveru
  - Uplatňujte správné politiky rotace a expirace tokenů
  - Zabraňte opakovanému použití tokenů a neautorizovanému použití

- **Chráněné uložení tokenů**: Bezpečné ukládání tokenů pomocí šifrování v klidu i při přenosu
  - **Osvědčené postupy**: [Pokyny k bezpečnému ukládání a šifrování tokenů](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementace řízení přístupu

- **Princip nejmenších práv**: Udělte MCP serverům pouze minimální oprávnění potřebná pro zamýšlenou funkčnost
  - Pravidelné revize a aktualizace práv k prevenci přidávání práv
  - **Dokumentace Microsoft**: [Bezpečný přístup s nejmenšími právy](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Řízení přístupu založené na rolích (RBAC)**: Implementujte jemně granulární přiřazení rolí
  - Přesně vymezte role na specifické zdroje a činnosti
  - Vyhněte se širokým nebo zbytečným oprávněním, která rozšiřují útočné povrchy

- **Nepřetržité monitorování oprávnění**: Implementujte průběžný audit a monitoring přístupu
  - Sledujte vzory používání oprávnění na anomálie
  - Okamžitě řešte nadměrná nebo nepoužívaná oprávnění

## Specifické bezpečnostní hrozby AI

### Útoky injekce promptu & manipulace nástrojů

Moderní implementace MCP čelí sofistikovaným AI-specifickým útočným vektorům, které tradiční bezpečnostní opatření nedokážou plně řešit:

#### **Nepřímá injekce promptu (Cross-Domain Prompt Injection)**

**Nepřímá injekce promptu** je jednou z nejkritičtějších zranitelností v systémech AI založených na MCP. Útočníci vkládají škodlivé instrukce do externího obsahu—dokumentů, webových stránek, e-mailů nebo zdrojů dat—které AI systémy následně zpracovávají jako legitimní příkazy.

**Scénáře útoků:**
- **Injekce založená na dokumentech**: Škodlivé instrukce skryté v zpracovávaných dokumentech, které spouštějí nechtěné AI akce
- **Využití webového obsahu**: Kompromitované webové stránky obsahující vložené promptové pokyny, které manipulují chování AI při sběru dat
- **Útoky založené na e-mailech**: Škodlivé promptové pokyny v e-mailech způsobující únik informací nebo neautorizované akce AI asistenta
- **Kontaminace zdrojů dat**: Kompromitované databáze nebo API dodávající nakažený obsah AI systémům

**Dopad ve skutečném světě**: Tyto útoky mohou vést k únikům dat, porušení soukromí, generování škodlivého obsahu a manipulaci uživatelských interakcí. Pro podrobnou analýzu viz [Prompt Injection v MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/cs/prompt-injection.ed9fbfde297ca877.webp)

#### **Útoky otravy nástrojů**

**Otrava nástrojů** cílí na metadata definující MCP nástroje, zneužívající způsob, jakým LLM interpretují popisy nástrojů a parametry pro rozhodování o exekuci.

**Mechanismy útoků:**
- **Manipulace s metadata**: Útočníci vkládají škodlivé instrukce do popisů nástrojů, definic parametrů nebo příkladů použití
- **Neviditelné instrukce**: Skryté promptové příkazy v metadatech nástrojů, které jsou zpracovávány AI modely, ale jsou neviditelné pro lidské uživatele
- **Dynamická modifikace nástrojů ("Rug Pulls")**: Nástroje schválené uživateli jsou později modifikovány, aby prováděly škodlivé akce bez vědomí uživatele
- **Injekce parametrů**: Škodlivý obsah vložený do schémat parametrů nástrojů, který ovlivňuje chování modelu


**Rizika hostovaných serverů**: Vzdálené MCP servery představují zvýšená rizika, protože definice nástrojů mohou být aktualizovány po počátečním schválení uživatelem, což vytváří scénáře, kdy se dříve bezpečné nástroje stanou škodlivými. Pro komplexní analýzu viz [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Diagram útoku na vkládání nástroje](../../../translated_images/cs/tool-injection.3b0b4a6b24de6bef.webp)

#### **Další vektory útoků AI**

- **Cross-Domain Prompt Injection (XPIA)**: Složené útoky využívající obsah z více domén k obejití bezpečnostních kontrol
- **Dynamická modifikace schopností**: Změny schopností nástrojů v reálném čase, které unikají počáteční bezpečnostní kontrole
- **Otrava kontextového okna**: Útoky, které manipulují s velkými kontextovými okny, aby skryly škodlivé instrukce
- **Model Confusion Attacks**: Využití omezení modelu k vytvoření nepředvídatelného nebo nebezpečného chování


### Dopady bezpečnostních rizik AI

**Vysoký dopad důsledků:**
- **Exfiltrace dat**: Neoprávněný přístup a krádež citlivých podnikových nebo osobních dat
- **Porušení soukromí**: Únik osobně identifikovatelných informací (PII) a důvěrných obchodních dat  
- **Manipulace se systémem**: Nezamýšlené změny kritických systémů a pracovních postupů
- **Krádež přihlašovacích údajů**: Kompromitace autentizačních tokenů a přístupových údajů ke službám
- **Laterální pohyb**: Využití kompromitovaných AI systémů jako odrazových můstků pro rozsáhlejší útoky v síti

### Bezpečnostní řešení Microsoft AI

#### **AI Prompt Shields: Pokročilá ochrana proti útokům vkládání**

Microsoft **AI Prompt Shields** poskytuje komplexní obranu proti přímým i nepřímým útokům vkládání promptů skrze více bezpečnostních vrstev:

##### **Základní ochranné mechanismy:**

1. **Pokročilá detekce a filtrování**
   - Algoritmy strojového učení a NLP techniky detekují škodlivé instrukce v externím obsahu
   - Analýza v reálném čase dokumentů, webových stránek, e-mailů a datových zdrojů na zanořené hrozby
   - Kontextuální porozumění legitimních vs. škodlivých promptů

2. **Spotlighting techniky**  
   - Rozlišuje důvěryhodné systémové instrukce od potenciálně kompromitovaných externích vstupů
   - Metody transformace textu, které zvyšují relevanci modelu a izolují škodlivý obsah
   - Pomáhá AI systémům udržet správnou hierarchii instrukcí a ignorovat vložené příkazy

3. **Systémy oddělování a označování dat**
   - Explicitní vymezení hranic mezi důvěryhodnými systémovými zprávami a externím vstupním textem
   - Speciální značky zvýrazňující hranice mezi důvěryhodnými a nedůvěryhodnými zdroji dat
   - Jasné oddělení zabraňuje záměně instrukcí a neoprávněnému vykonávání příkazů

4. **Kontinuální Threat Intelligence**
   - Microsoft kontinuálně sleduje nové vzory útoků a aktualizuje obranu
   - Proaktivní vyhledávání hrozeb pro nové techniky vkládání a vektory útoků
   - Pravidelné aktualizace bezpečnostních modelů pro zachování účinnosti vůči vyvíjejícím se hrozbám

5. **Integrace Azure Content Safety**
   - Součást komplexního balíčku Azure AI Content Safety
   - Dodatečná detekce pokusů o jailbreak, škodlivého obsahu a porušování bezpečnostních politik
   - Jednotné bezpečnostní kontroly napříč AI komponentami aplikací

**Implementační zdroje**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Ochrana Microsoft Prompt Shields](../../../translated_images/cs/prompt-shield.ff5b95be76e9c78c.webp)


## Pokročilá bezpečnostní rizika MCP

### Zranitelnosti převezmutí relace

**Převezmutí relace** představuje kritický vektor útoku ve stavových implementacích MCP, kde neoprávněné strany získají a zneužívají legitimní identifikátory relací k vydávání se za klienty a provádění neoprávněných akcí.

#### **Scénáře útoků a rizika**

- **Vkládání promptu při převezmutí relace**: Útočníci s ukradenými ID relace vkládají škodlivé události do serverů sdílejících stav relace, což může vyvolat škodlivé akce nebo přístup k citlivým datům
- **Přímé vydávání se za klienta**: Ukradené ID relace umožňují přímé volání MCP serveru, které obejde autentizaci, a útočníci jsou považováni za legitimní uživatele
- **Kompromitované přerušitelné streamy**: Útočníci mohou předčasně ukončovat požadavky, což způsobí, že legitimní klienti pokračují s potenciálně škodlivým obsahem

#### **Bezpečnostní kontroly pro správu relací**

**Kritické požadavky:**
- **Ověření autorizace**: MCP servery implementující autorizaci **MUSÍ** ověřovat VŠECHNY příchozí požadavky a **NESMÍ** spoléhat na relace pro autentizaci
- **Bezpečná generace relací**: Používat kryptograficky bezpečná, nedeterministická ID relace generovaná bezpečnými generátory náhodných čísel
- **Vazba na uživatele**: Vázat ID relace na uživatelská data pomocí formátu `<user_id>:<session_id>`, aby se zabránilo zneužití mezi uživateli
- **Správa životního cyklu relace**: Implementovat řádné vypršení, rotaci a neplatnost relací, aby se omezila doba zranitelnosti
- **Zabezpečení přenosu**: Povinné HTTPS pro veškerou komunikaci k zabránění zachycení ID relace

### Problém zmateného zástupce

**Problém zmateného zástupce** nastává, když MCP servery jednají jako autentizační proxy mezi klienty a službami třetích stran, což vytváří příležitosti pro obejití autorizace prostřednictvím využití statického ID klienta.

#### **Mechanika útoku a rizika**

- **Obcházení souhlasu založené na cookie**: Předchozí uživatelská autentizace vytváří cookies souhlasu, které útočníci zneužívají prostřednictvím škodlivých požadavků autorizace s upravenými přesměrovacími URI
- **Krádež autorizačního kódu**: Existující cookies souhlasu mohou způsobit, že autorizační servery přeskočí obrazovky souhlasu a přesměrují kódy na útočníkem kontrolované koncové body  
- **Neoprávněný přístup k API**: Ukradené autorizační kódy umožňují výměnu tokenů a vydávání se za uživatele bez explicitního schválení

#### **Strategie zmírnění**

**Povinné kontroly:**
- **Výslovné požadavky na souhlas**: MCP proxy servery používající statická ID klientů **MUSÍ** získat uživatelský souhlas pro každý dynamicky registrovaný klient
- **Implementace bezpečnosti OAuth 2.1**: Dodržovat aktuální bezpečnostní postupy OAuth včetně PKCE (Proof Key for Code Exchange) pro všechny autorizační požadavky
- **Přísná validace klientů**: Implementovat přísnou kontrolu přesměrovacích URI a identifikátorů klientů, aby se zabránilo zneužití

### Zranitelnosti přenosu tokenů  

**Přenos tokenů** představuje explicitní anti-vzor, kdy MCP servery přijímají klientské tokeny bez řádné validace a předávají je dále na downstream API, čímž porušují specifikace autorizace MCP.

#### **Bezpečnostní důsledky**

- **Obcházení kontrol**: Přímé užití klientských tokenů v API obchází kritická omezení rychlosti, validaci a monitorovací kontroly
- **Poškození auditní stopy**: Tokeny vydané upstream znemožňují identifikaci klienta, čímž se zhoršuje schopnost vyšetřování incidentů
- **Proxy exfiltrace dat**: Nevalidované tokeny umožňují škodlivým aktérům využívat servery jako proxy pro neoprávněný přístup k datům
- **Porušení stávajících hranic důvěry**: Downstream služby mohou mít porušeny předpoklady důvěry, pokud nelze ověřit původ tokenů
- **Šíření útoků přes více služeb**: Kompromitované tokeny přijímané napříč službami umožňují laterální pohyb

#### **Požadované bezpečnostní kontroly**

**Nepřekročitelné požadavky:**
- **Validace tokenů**: MCP servery **NESMÍ** přijímat tokeny, které nebyly explicitně vydány pro MCP server
- **Ověření audienčního účelu tokenu**: Vždy ověřovat, že audienční nároky tokenu odpovídají identitě MCP serveru
- **Řádný životní cyklus tokenů**: Implementovat krátkodobé přístupové tokeny s bezpečnými praktikami rotace


## Bezpečnost dodavatelského řetězce pro AI systémy

Bezpečnost dodavatelského řetězce se rozvinula za rámec tradičních softwarových závislostí a zahrnuje celý ekosystém AI. Moderní implementace MCP musí důkladně ověřovat a monitorovat všechny součásti související s AI, protože každá přináší potenciální zranitelnosti, jež mohou ohrozit integritu systému.

### Rozšířené komponenty AI dodavatelského řetězce

**Tradiční softwarové závislosti:**
- Knihovny a rámce s otevřeným zdrojovým kódem
- Obrazové kontejnery a základní systémy  
- Vývojové nástroje a build pipeline
- Infrastrukturní komponenty a služby

**Specifické prvky AI dodavatelského řetězce:**
- **Základní modely**: Předtrénované modely od různých poskytovatelů vyžadující ověření původu
- **Embedding služby**: Externí služby pro vektorizaci a sémantické vyhledávání
- **Poskytovatelé kontextu**: Datové zdroje, znalostní báze a úložiště dokumentů  
- **API třetích stran**: Externí AI služby, ML pipeline a datové koncové body
- **Modelové artefakty**: Váhy, konfigurace a doladěné varianty modelů
- **Zdroje tréninkových dat**: Datasetů použitých pro trénink a doladění modelů

### Komplexní strategie zabezpečení dodavatelského řetězce

#### **Ověření a důvěra komponent**
- **Ověření původu**: Prověřit původ, licence a integritu všech AI komponent před integrací
- **Bezpečnostní hodnocení**: Provádět skeny zranitelností a bezpečnostní revize modelů, datových zdrojů a AI služeb
- **Analýza reputace**: Posuzovat bezpečnostní historii a praktiky poskytovatelů AI služeb
- **Ověření souladu**: Zajistit, že všechny komponenty splňují organizační bezpečnostní a regulační požadavky

#### **Bezpečné nasazovací pipeline**  
- **Automatizované CI/CD skenování**: Integrovat bezpečnostní skeny v celém automatizovaném nasazovacím procesu
- **Integrita artefaktů**: Zavést kryptografické ověřování pro všechny nasazované artefakty (kód, modely, konfigurace)
- **Postupné nasazení**: Používat progresivní strategie nasazení s bezpečnostní validací v každé fázi
- **Důvěryhodné repozitáře artefaktů**: Nasazovat pouze z ověřených, zabezpečených repozitářů artefaktů

#### **Kontinuální monitorování a reakce**
- **Skenování závislostí**: Průběžné sledování zranitelností u všech softwarových a AI komponent
- **Monitorování modelu**: Kontinuální hodnocení chování modelu, posunu výkonu a bezpečnostních anomálií
- **Sledování stavu služeb**: Monitorovat dostupnost externích AI služeb, bezpečnostní incidenty a změny politik
- **Integrace Threat Intelligence**: Zahrnovat hrozbové kanály specifické pro AI a ML bezpečnostní rizika

#### **Řízení přístupu a princip minimálních oprávnění**
- **Oprávnění na úrovni komponent**: Omezit přístup k modelům, datům a službám na základě obchodní potřeby
- **Správa servisních účtů**: Zavést dedikované servisní účty s minimálními potřebnými oprávněními
- **Segmentace sítě**: Izolovat AI komponenty a omezit síťový přístup mezi službami
- **Kontroly API Gateway**: Používat centralizované API brány ke kontrole a monitorování přístupu k externím AI službám

#### **Reakce na incidenty a obnova**
- **Postupy rychlé reakce**: Zavedené procesy pro opravy nebo nahrazení kompromitovaných AI komponent
- **Rotace přihlašovacích údajů**: Automatizované systémy pro rotaci tajemství, API klíčů a přístupových dat
- **Možnosti návratu zpět**: Schopnost rychle obnovit předchozí ověřené verze AI komponent
- **Obnova z narušení dodavatelského řetězce**: Specifické postupy pro reakci na kompromitace upstream AI služeb

### Nástroje a integrace Microsoft bezpečnosti

**GitHub Advanced Security** poskytuje komplexní ochranu dodavatelského řetězce včetně:
- **Skenování tajemství**: Automatická detekce přihlašovacích údajů, API klíčů a tokenů v repozitářích
- **Skenování závislostí**: Hodnocení zranitelností u open-source závislostí a knihoven
- **CodeQL analýza**: Statická analýza kódu pro bezpečnostní zranitelnosti a chyby kodování
- **Přehled dodavatelského řetězce**: Viditelnost stavu zdraví a bezpečnosti závislostí

**Integrace Azure DevOps & Azure Repos:**
- Bezproblémová integrace bezpečnostních skenů v rámci Microsoft vývojových platforem
- Automatizované bezpečnostní kontroly v Azure Pipelines pro AI pracovní zátěže
- Vynucování politik pro bezpečné nasazení AI komponent

**Interní praktiky Microsoft:**
Microsoft zavádí rozsáhlé bezpečnostní praktiky dodavatelského řetězce napříč všemi produkty. Naučte se o ověřených postupech v [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Základní bezpečnostní osvědčené postupy

Implementace MCP dědí a staví na existující bezpečnostní postuře vaší organizace. Posílení základních bezpečnostních praktik výrazně zvyšuje celkovou bezpečnost AI systémů a nasazení MCP.

### Základní bezpečnostní principy

#### **Bezpečné vývojové postupy**
- **Soulad s OWASP**: Ochrana proti [TOP 10 zranitelnostem OWASP](https://owasp.org/www-project-top-ten/) webových aplikací
- **Specifické AI ochrany**: Implementace kontrol pro [OWASP Top 10 pro LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Bezpečná správa tajemství**: Používat dedikované trezory pro tokeny, API klíče a citlivé konfigurační údaje
- **End-to-End šifrování**: Zajistit bezpečnou komunikaci ve všech aplikačních komponentách a toků dat
- **Validace vstupů**: Přísná validace všech uživatelských vstupů, parametrů API a datových zdrojů

#### **Zpevnění infrastruktury**
- **Vícefaktorová autentizace**: Povinné MFA pro všechny administrativní a servisní účty
- **Správa záplat**: Automatizované a včasné záplatování operačních systémů, rámců a závislostí  
- **Integrace poskytovatele identity**: Centralizovaná správa identit přes podnikové identity poskytovatele (Microsoft Entra ID, Active Directory)
- **Segmentace sítě**: Logická izolace MCP komponent pro omezení laterálního pohybu
- **Princip minimálních oprávnění**: Minimální nutná oprávnění pro všechny systémové komponenty a účty

#### **Monitorování a detekce bezpečnosti**
- **Komplexní logování**: Detailní protokolování aktivit AI aplikací včetně interakcí MCP klient-server
- **Integrace SIEM**: Centralizované řízení bezpečnostních informací a událostí pro detekci anomálií
- **Behaviorální analýza**: AI-poháněné monitorování pro detekci neobvyklých vzorců v chování systému a uživatelů
- **Threat Intelligence**: Integrace externích hrozbových kanálů a indikátorů kompromitace (IOC)
- **Reakce na incidenty**: Definované postupy pro detekci, reakci a zotavení z bezpečnostních incidentů

#### **Zero Trust architektura**
- **Nikdy nevěř, vždy ověřuj**: Kontinuální ověřování uživatelů, zařízení a síťových připojení
- **Mikro-segmentace**: Detailní síťové kontroly izolující jednotlivé pracovní zátěže a služby
- **Bezpečnost orientovaná na identitu**: Bezpečnostní politiky založené na ověřené identitě místo umístění v síti
- **Kontinuální hodnocení rizik**: Dynamické vyhodnocování bezpečnostního postavení na základě aktuálního kontextu a chování
- **Podmíněný přístup**: Řízení přístupu adaptující se podle rizikových faktorů, polohy a důvěryhodnosti zařízení

### Vzory integrace do podniku

#### **Integrace do Microsoft bezpečnostního ekosystému**
- **Microsoft Defender for Cloud**: Komplexní správa bezpečnostního postavení v cloudu
- **Azure Sentinel**: Nativní SIEM a SOAR schopnosti pro ochranu AI pracovních zátěží
- **Microsoft Entra ID**: Podnikové řízení identit a přístupů s podmíněnými přístupovými politikami
- **Azure Key Vault**: Centralizovaná správa tajemství s podporou hardwarového bezpečnostního modulu (HSM)
- **Microsoft Purview**: Správa a compliance dat pro AI datové zdroje a pracovní postupy

#### **Soulad a správa**
- **Soulad s regulacemi**: Zajistit, že implementace MCP splňují průmyslové normy a požadavky na soulad (GDPR, HIPAA, SOC 2)

- **Klasifikace dat**: Správná kategorizace a zpracování citlivých dat v AI systémech
- **Auditní stopy**: Komplexní protokolování pro regulativní soulad a forenzní vyšetřování
- **Ovládání soukromí**: Implementace principů ochrany soukromí již v návrhu architektury AI systému
- **Řízení změn**: Formální procesy pro bezpečnostní přezkumy změn v AI systémech

Tyto základní postupy vytvářejí robustní bezpečnostní základnu, která zvyšuje účinnost bezpečnostních kontrol specifických pro MCP a poskytuje komplexní ochranu aplikací řízených AI.

## Klíčové bezpečnostní poznatky

- **Vícevrstvý bezpečnostní přístup**: Kombinujte základní postupy zabezpečení (bezpečné kódování, nejmenší práva, ověřování dodavatelského řetězce, kontinuální monitorování) s kontrolami specifickými pro AI pro komplexní ochranu

- **Specifická hrozební krajina AI**: Systémy MCP čelí unikátním rizikům jako injekce promptů, otravování nástrojů, únosy relací, problémy zmateného zástupce, zranitelnosti přeposílání tokenů a nadměrná oprávnění, které vyžadují specializovaná opatření

- **Vynikající autentizace & autorizace**: Implementujte robustní autentizaci pomocí externích poskytovatelů identity (Microsoft Entra ID), prosazujte správnou validaci tokenů a nikdy nepřijímejte tokeny, které nejsou výslovně vydány pro váš MCP server

- **Prevence útoků na AI**: Nasazujte Microsoft Prompt Shields a Azure Content Safety k obraně proti nepřímým útokům typu injekce promptů a otravování nástrojů, zároveň validujte metadata nástrojů a sledujte dynamické změny

- **Bezpečnost relací & přenosu**: Používejte kryptograficky bezpečné, nedeterministické ID relací svázané s identitami uživatelů, implementujte správné řízení životního cyklu relací a nikdy nepoužívejte relace pro autentizaci

- **Nejlepší postupy zabezpečení OAuth**: Prevence útoků zmateného zástupce pomocí explicitního uživatelského souhlasu pro dynamicky registrované klienty, správná implementace OAuth 2.1 s PKCE a přísná validace přesměrovacích URI  

- **Principy zabezpečení tokenů**: Vyvarujte se anti-vzorům přeposílání tokenů, validujte audience tokenu, implementujte krátkodobé tokeny s bezpečnou rotací a udržujte jasné hranice důvěry

- **Komplexní zabezpečení dodavatelského řetězce**: Zacházejte se všemi komponentami AI ekosystému (modely, embeddings, poskytovatelé kontextu, externí API) se stejnou bezpečnostní přísností jako s tradičními softwarovými závislostmi

- **Nepřetržitý vývoj**: Buďte v obraze s rychle se vyvíjejícími specifikacemi MCP, přispívejte do bezpečnostních komunitních standardů a udržujte adaptivní bezpečnostní postoje, jak se protokol vyvíjí

- **Integrace s Microsoft Security**: Využívejte komplexní bezpečnostní ekosystém Microsoftu (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) pro zvýšenou ochranu nasazení MCP

## Komplexní zdroje

### **Oficiální dokumentace MCP bezpečnosti**
- [Specifikace MCP (Aktuální: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP bezpečnostní nejlepší postupy](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Autorizace MCP specifikace](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Github repozitář MCP](https://github.com/modelcontextprotocol)

### **OWASP MCP bezpečnostní zdroje**
- [OWASP MCP Azure bezpečnostní průvodce](https://microsoft.github.io/mcp-azure-security-guide/) - Komplexní OWASP MCP Top 10 s pokyny pro implementaci v Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Oficiální OWASP MCP bezpečnostní rizika
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktický bezpečnostní trénink pro MCP na Azure

### **Bezpečnostní standardy a nejlepší postupy**
- [OAuth 2.0 bezpečnostní nejlepší postupy (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 zabezpečení webových aplikací](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 pro velké jazykové modely](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Výzkum a analýza AI bezpečnosti**
- [Injekce promptu v MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Útoky otravy nástrojů (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Zpráva o výzkumu MCP bezpečnosti (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft bezpečnostní řešení**
- [Dokumentace Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID bezpečnost](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure nejlepší postupy správy tokenů](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Průvodce implementací a tutoriály**
- [Azure API Management jako autentizační brána MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID autentizace s MCP servery](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Bezpečné ukládání tokenů a šifrování (video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & zabezpečení dodavatelského řetězce**
- [Azure DevOps bezpečnost](https://azure.microsoft.com/products/devops)
- [Azure Repos bezpečnost](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft cesta k zabezpečení dodavatelského řetězce](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Další dokumentace o bezpečnosti**

Pro komplexní bezpečnostní pokyny se odkazujte na tyto specializované dokumenty v této sekci:

- **[Ukázka autorizace CIMD a DCR](./samples/cimd-dcr-auth/README.md)** - Spustitelný TypeScript MCP `2026-07-28` resource server porovnávající preferované dokumenty metadata klienta s zastaralým fallbackem dynamické registrace klienta
- **[MCP bezpečnostní nejlepší postupy](./mcp-security-best-practices.md)** - Kompletní bezpečnostní nejlepší postupy pro implementace MCP
- **[Implementace Azure Content Safety](./azure-content-safety-implementation.md)** - Praktické příklady implementace pro integraci Azure Content Safety  
- **[MCP bezpečnostní kontroly](./mcp-security-controls.md)** - Nejnovější bezpečnostní kontroly a techniky pro nasazení MCP
- **[Rychlý přehled MCP nejlepších praktik](./mcp-best-practices.md)** - Rychlý referenční průvodce základními bezpečnostními praktikami MCP
- **[BlueHat 2026: Zajištění budoucnosti AI: Zabezpečení MCP s obranou do hloubky](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Obranné vzory do hloubky od Microsoft Security Response Center (MSRC)

### **Praktický bezpečnostní trénink**

- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Komplexní praktický workshop pro zabezpečení MCP serverů v Azure s progresivními kempy od Base Camp po Summit
- **[OWASP MCP Azure bezpečnostní průvodce](https://microsoft.github.io/mcp-azure-security-guide/)** - Referenční architektura a pokyny implementace pro všechna OWASP MCP Top 10 rizika

---

## Co dál

Další: [Kapitola 3: Začínáme](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->