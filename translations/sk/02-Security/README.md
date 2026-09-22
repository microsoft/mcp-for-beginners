# MCP Security: Komplexná ochrana pre AI systémy

[![MCP Security Best Practices](../../../translated_images/sk/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

Bezpečnosť je základom návrhu AI systémov, preto jej venujeme prioritu ako druhej časti. To korešponduje s princípom Microsoftu **Secure by Design** z [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Protokol kontextu modelu (MCP) prináša výkonné nové možnosti pre aplikácie poháňané AI, zároveň však prináša jedinečné bezpečnostné výzvy, ktoré presahujú tradičné softvérové riziká. Systémy MCP čelia ako zavedeným bezpečnostným problémom (bezpečné kódovanie, princíp najmenších práv, bezpečnosť dodávateľského reťazca), tak aj novým špecifickým hrozbám AI vrátane injektáže promptov, otravy nástrojov, prevzatia relácie, útokov zmätku zástupcu, zraniteľností pri prenose tokenov a dynamickej modifikácie schopností.

Táto lekcia skúma najkritickejšie bezpečnostné riziká v implementáciách MCP — pokrýva autentifikáciu, autorizáciu, nadmerné oprávnenia, nepriame injektáže promptov, bezpečnosť relácií, problémy zmätku zástupcu, správu tokenov a zraniteľnosti dodávateľského reťazca. Naučíte sa účinné kontroly a najlepšie praktiky na zmiernenie týchto rizík pri využívaní riešení Microsoftu ako Prompt Shields, Azure Content Safety a GitHub Advanced Security na posilnenie vášho nasadenia MCP.

## Výučbové ciele

Po skončení tejto lekcie budete vedieť:

- **Identifikovať MCP-špecifické hrozby**: Rozpoznať jedinečné bezpečnostné riziká v MCP systémoch vrátane injektáže promptov, otravy nástrojov, nadmerných oprávnení, prevzatia relácie, problémov zmätku zástupcu, zraniteľností pri prenose tokenov a rizík dodávateľského reťazca
- **Použiť bezpečnostné kontroly**: Implementovať účinné zmiernenia vrátane robustnej autentifikácie, prístupu na základe najmenších práv, bezpečnej správy tokenov, kontrol bezpečnosti relácií a overovania dodávateľského reťazca
- **Využiť bezpečnostné riešenia Microsoftu**: Pochopiť a nasadiť Microsoft Prompt Shields, Azure Content Safety a GitHub Advanced Security na ochranu záťaže MCP
- **Overiť bezpečnosť nástrojov**: Uvedomiť si význam overenia metadát nástrojov, sledovania dynamických zmien a obrany proti nepriamym útokom injektáže promptov
- **Integrovať najlepšie praktiky**: Kombinovať zavedené bezpečnostné základy (bezpečné kódovanie, spevnenie serverov, zero trust) s MCP-špecifickými kontrolami pre komplexnú ochranu

# Architektúra a kontroly bezpečnosti MCP

Moderné implementácie MCP vyžadujú viacvrstvové bezpečnostné prístupy, ktoré riešia ako tradičnú softvérovú bezpečnosť, tak aj špecifické hrozby AI. Rýchlo sa vyvíjajúca špecifikácia MCP postupne zlepšuje svoje bezpečnostné kontroly, umožňujúce lepšiu integráciu s podnikových bezpečnostnými architektúrami a zavedenými najlepšími praktikami.

Výskum z [Microsoft Digital Defense Report](https://aka.ms/mddr) ukazuje, že **98 % nahlásených prienikov by bolo zabránených robustnou bezpečnostnou hygienou**. Najefektívnejšia ochrana kombinuje základné bezpečnostné praktiky s MCP-špecifickými kontrolami — osvedčené základné bezpečnostné opatrenia zostávajú najvýznamnejšie pre zníženie celkového bezpečnostného rizika.

## Súčasný bezpečnostný stav

> **Poznámka:** Táto kapitola kombinuje zavedené bezpečnostné kontroly MCP s
> aktuálnym **MCP Specification 2026-07-28** usmernením o autorizácii. Vždy sa odvolávajte
> na aktuálnu [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHub repository](https://github.com/modelcontextprotocol) a
> [dokumentáciu najlepších bezpečnostných praktík](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> pri implementácii bezpečnostne citlivého kódu.

> **Aktualizácia autorizácie:** MCP `2026-07-28` vyžaduje, aby klienti overovali
> parameter `iss` v odpovediach na autorizáciu (RFC 9207) a viazali registrované
> poverenia na vydávajúci autorizačný server. Dynamická registrácia klientov
> je zastaraná; nové implementácie by mali používať dokumenty metadát Client ID.
> Viď [Čo sa zmenilo v MCP: Špecifikácia 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> pre kompletný zoznam zmien v autorizácii.

## 🏔️ MCP Security Summit Workshop (Sherpa)

Pre **praktický bezpečnostný tréning** veľmi odporúčame **MCP Security Summit Workshop** (Sherpa) - komplexnú vedenú expedíciu za zabezpečením MCP serverov v Microsoft Azure.

### Prehľad workshopu

[MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) ponúka praktický, použiteľný bezpečnostný tréning cez osvedčenú metódu „zraniteľný → exploit → oprava → overenie“. Naučíte sa:

- **Učiť sa na chybách**: Zažiť zraniteľnosti na vlastnej koži cez exploit bezpečnostne nespoľahlivých serverov
- **Využiť natívnu Azure bezpečnosť**: Použiť Azure Entra ID, Key Vault, API Management a AI Content Safety
- **Dodržiavať obranu do hĺbky**: Postupovať cez tábory budujúc komplexné bezpečnostné vrstvy
- **Dodržiavať štandardy OWASP**: Každá technika je mapovaná na [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- **Získať produkčný kód**: Odísť s funkčnými, otestovanými implementáciami

### Trasa expedície

| Tábor | Zameranie | Pokryté riziká OWASP |
|------|----------|----------------------|
| **Základný tábor** | Základy MCP & zraniteľnosti autentifikácie | MCP01, MCP07 |
| **Tábor 1: Identita** | OAuth 2.1, Azure Managed Identity, Key Vault | MCP01, MCP02, MCP07 |
| **Tábor 2: Brána** | API Management, Private Endpoints, správa | MCP02, MCP06, MCP07, MCP09 |
| **Tábor 3: I/O bezpečnosť** | Injektáž promptov, ochrana PII, bezpečnosť obsahu | MCP03, MCP05, MCP06, MCP10 |
| **Tábor 4: Monitorovanie** | Log Analytics, dashboardy, detekcia hrozieb | MCP04, MCP08 |
| **Summit** | Red Team / Blue Team integračný test | Všetky |

**Začať môžete na**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 bezpečnostných rizík

[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) podrobne opisuje desať najkritickejších bezpečnostných rizík pre implementácie MCP:

| Riziko | Popis | Opatrenie v Azure |
|--------|-------|-----------------|
| **MCP01** | Nesprávna správa tokenov & únik tajomstiev | Azure Key Vault, Managed Identity |
| **MCP02** | Eskalácia práv cez Scope Creep | RBAC, Podmienený prístup |
| **MCP03** | Otrava nástrojov | Validácia nástrojov, overovanie integrity |
| **MCP04** | Útoky na dodávateľský reťazec softvéru & manipulácia závislostí | GitHub Advanced Security, skenovanie závislostí |
| **MCP05** | Injekcia príkazov & exekúcia | Validácia vstupov, sandboxing |
| **MCP06** | Porušenie toku zámerov | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Nedostatočná autentifikácia & autorizácia | Azure Entra ID, OAuth 2.1 s PKCE |
| **MCP08** | Nedostatok auditu a telemetrie | Azure Monitor, Application Insights |
| **MCP09** | Tieňové MCP servery | Správa API Centra, sieťová izolácia |
| **MCP10** | Injekcia kontextu & nadmerné zdieľanie | Klasifikácia dát, minimálna expozícia |

### Vývoj autentifikácie MCP

Špecifikácia MCP sa významne vyvinula v prístupe k autentifikácii a autorizácii:

- **Pôvodný prístup**: Skoré špecifikácie vyžadovali, aby vývojári implementovali vlastné autentifikačné servery, pričom MCP servery fungovali ako OAuth 2.0 autorizačné servery spravujúce priamo autentifikáciu používateľov
- **Súčasný štandard (`2026-07-28`)**: MCP servery môžu delegovať autentifikáciu
  na externých poskytovateľov identity, ako je Microsoft Entra ID. Klienti musia tiež
  uplatniť aktuálne požiadavky na overovanie vydavateľa a viazanie poverení.
- **Transportná bezpečnosť**: Vylepšená podpora bezpečných transportných mechanizmov s vhodnými vzormi autentifikácie pre lokálne (STDIO) aj vzdialené (Streamable HTTP) pripojenia

## Bezpečnosť autentifikácie a autorizácie

### Súčasné bezpečnostné výzvy

Moderné implementácie MCP čelia viacerým výzvam v autentifikácii a autorizácii:

### Riziká a hrozby

- **Nesprávne nakonfigurovaná autorizácia**: Chybné implementácie autorizácie v MCP serveroch môžu vystaviť citlivé údaje a nesprávne aplikovať prístupové kontroly
- **Ohrozenie OAuth tokenov**: Krádež tokenov lokálneho MCP servera umožňuje útočníkom vydávať sa za server a získať prístup k následným službám
- **Zraniteľnosti pri prenose tokenov**: Nesprávna manipulácia s tokenmi vytvára obchádzky bezpečnostných kontrol a medzery v účtovaní
- **Nadmerné oprávnenia**: MCP servery s príliš veľkými právami porušujú princíp najmenších práv a rozširujú útočné plochy

#### Prenos tokenov: Kritický anti-vzor

**Prenos tokenov je v aktuálnej špecifikácii autorizácie MCP výslovne zakázaný** kvôli závažným bezpečnostným dôsledkom:

##### Obchádzanie bezpečnostných kontrol
- MCP servery a následné API implementujú kritické bezpečnostné kontroly (obmedzovanie rýchlosti, validáciu požiadaviek, monitorovanie prevádzky), ktoré závisia od správneho overenia tokenov
- Priame používanie tokenov klientom pre API obchádza tieto nevyhnutné ochrany, čím oslabuje bezpečnostnú architektúru

##### Problémy s účtovaním a auditom  
- MCP servery nedokážu rozlíšiť klientov používajúcich tokeny vydané hore, čo narušuje auditné stopy
- Logy zdrojových serverov ukazujú zavádzajúci pôvod požiadaviek namiesto skutočných MCP serverov ako sprostredkovateľov
- Vyšetrovanie incidentov a súlad s predpismi sa stávajú výrazne náročnejšie

##### Riziká exfiltrácie dát
- Neoverené nároky tokenov umožňujú škodlivým aktérom s ukradnutými tokenmi použiť MCP servery ako proxy pre exfiltráciu dát
- Porušenia dôvery umožňujú neoprávnený prístup obchádzajúci zamýšľané bezpečnostné kontroly

##### Viacnásobné útočné vektory služieb
- Kompromitované tokeny akceptované viacerými službami umožňujú laterálny pohyb naprieč prepojenými systémami
- Predpoklady dôvery medzi službami môžu byť porušené, keď nie je možné overiť pôvod tokenov

### Bezpečnostné kontroly a zmiernenia

**Kritické bezpečnostné požiadavky:**

> **Povinné**: MCP servery **NESMÚ** akceptovať žiadne tokeny, ktoré neboli explicitne vydané pre daný MCP server

#### Kontroly autentifikácie a autorizácie

- **Dôkladná revízia autorizácie**: Vykonávať komplexné audity autorizácie MCP serverov, aby sa zabezpečilo, že citlivé zdroje pristupujú iba zamýšľaní používatelia a klienti
  - **Sprievodca implementáciou**: [Azure API Management ako autentifikačná brána pre MCP servere](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrácia identity**: [Použitie Microsoft Entra ID pre autentifikáciu MCP serverov](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Bezpečná správa tokenov**: Implementovať [najlepšie praktiky validácie a životného cyklu tokenov od Microsoftu](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Overiť, či nároky tokenu o publiku zodpovedajú identite MCP servera
  - Implementovať správnu rotáciu tokenov a politiky vypršania platnosti
  - Zabrániť opakovaniu útokov s tokenmi a neautorizovanému použitiu

- **Chránené ukladanie tokenov**: Bezpečné ukladanie tokenov s šifrovaním v pokoji aj pri prenose
  - **Najlepšie praktiky**: [Pokyny na bezpečné ukladanie a šifrovanie tokenov](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementácia kontroly prístupu

- **Princíp najmenších práv**: Poskytovať MCP serverom iba minimálne oprávnenia nevyhnutné na zamýšľanú funkcionalitu
  - Pravidelné prehliadky a aktualizácie oprávnení na zabránenie rozširovania práv
  - **Dokumentácia Microsoftu**: [Bezpečný prístup s najmenšími právami](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Riadenie prístupu na základe rolí (RBAC)**: Implementovať detailné prideľovanie rolí
  - Presne viazať role na konkrétne zdroje a akcie
  - Vyhýbať sa širokým alebo zbytočným oprávneniam, ktoré rozširujú útočné možnosti

- **Kontinuálne monitorovanie oprávnení**: Implementovať kontinuálny audit a monitorovanie prístupu
  - Sledujte vzory používania oprávnení pre anomálie
  - Okamžite opravujte nadmerné alebo nepoužívané práva

## Špecifické bezpečnostné hrozby AI

### Útoky injektáži promptov a manipulácie nástrojov

Moderné implementácie MCP čelia sofistikovaným AI-špecifickým útokovým vektorom, ktoré tradičné bezpečnostné opatrenia nedokážu plne riešiť:

#### **Nepriama injektáž promptov (Cross-Domain Prompt Injection)**

**Nepriama injektáž promptov** predstavuje jednu z najkritickejších zraniteľností v AI systémoch s podporou MCP. Útočníci vkladajú škodlivé inštrukcie do externého obsahu — dokumentov, webových stránok, e-mailov alebo zdrojov dát — ktoré AI systémy následne spracovávajú ako legitímne príkazy.

**Scenáre útokov:**
- **Injekcia do dokumentov**: Škodlivé inštrukcie skryté v spracúvaných dokumentoch vyvolávajú neplánované akcie AI
- **Zneužitie webového obsahu**: Kompromitované webové stránky obsahujúce vložené prompty manipulujú AI správanie pri scrapaní
- **Útoky cez e-mail**: Škodlivé prompty v e-mailoch spôsobujú, že AI asistenti unikajú informácie alebo vykonávajú neautorizované akcie
- **Kontaminácia zdrojov dát**: Kompromitované databázy alebo API poskytujú znečistený obsah AI systémom

**Reálny dopad**: Tieto útoky môžu spôsobiť exfiltráciu dát, narušenie súkromia, generovanie škodlivého obsahu a manipuláciu s interakciami používateľov. Pre detailnú analýzu viď [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/sk/prompt-injection.ed9fbfde297ca877.webp)

#### **Útoky otravy nástrojov**

**Otrava nástrojov** cieli na metadáta definujúce MCP nástroje, zneužívajúc spôsob, akým LLM interpretujú opisy nástrojov a parametrov pri rozhodovaní o vykonaní.

**Mechanizmy útokov:**
- **Manipulácia metadát**: Útočníci vkladajú škodlivé inštrukcie do popisov nástrojov, definícií parametrov alebo príkladov použitia
- **Neviditeľné inštrukcie**: Skryté prompty v metadátach nástrojov, ktoré AI modely spracovávajú, ale sú pre ľudských používateľov neviditeľné
- **Dynamická modifikácia nástrojov („Rug Pulls“) **: Nástroje schválené používateľmi sú neskôr modifikované na vykonávanie škodlivých akcií bez vedomia používateľa
- **Injektáž parametrov**: Škodlivý obsah vložený do schém parametrov nástrojov, ktorý ovplyvňuje správanie modelu


**Riziká hostených serverov**: Vzdialené MCP servery predstavujú zvýšené riziká, pretože definície nástrojov môžu byť aktualizované po pôvodnom schválení používateľom, čím vznikajú scenáre, kde sa predtým bezpečné nástroje stávajú škodlivými. Pre komplexnú analýzu pozri [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Diagram útoku injekcie nástroja](../../../translated_images/sk/tool-injection.3b0b4a6b24de6bef.webp)

#### **Ďalšie vektorové útoky AI**

- **Cross-Domain Prompt Injection (XPIA)**: Sofistikované útoky využívajúce obsah z viacerých domén na obídenie bezpečnostných kontrol
- **Dynamická modifikácia schopností**: Zmeny schopností nástrojov v reálnom čase, ktoré unikajú počiatočným bezpečnostným hodnoteniam
- **Otrava kontextového okna**: Útoky manipulujúce s veľkými kontextovými oknami na skrytie škodlivých inštrukcií
- **Útoky zmäteného modelu**: Využívanie obmedzení modelu na vytvorenie nepredvídateľného alebo nebezpečného správania


### Dopad bezpečnostných rizík AI

**Následky s vysokým dopadom:**
- **Únik údajov**: Neoprávnený prístup a krádež citlivých podnikových alebo osobných údajov
- **Porušenie súkromia**: Zverejnenie osobne identifikovateľných informácií (PII) a dôverných obchodných údajov  
- **Manipulácia so systémami**: Nezamýšľané zmeny kritických systémov a pracovných postupov
- **Krádež prístupových údajov**: Kompromitácia autentifikačných tokenov a prihlasovacích údajov služieb
- **Bočné pohyby**: Využitie kompromitovaných AI systémov ako odrazových mostíkov pre širšie sieťové útoky

### Bezpečnostné riešenia Microsoft AI

#### **AI Prompt Shields: Pokročilá ochrana proti injekčným útokom**

Microsoft **AI Prompt Shields** poskytujú komplexnú obranu proti priamym aj nepriamym injekčným útokom promptov prostredníctvom viacerých bezpečnostných vrstiev:

##### **Kľúčové ochranné mechanizmy:**

1. **Pokročilé detekovanie a filtrovanie**
   - Algoritmy strojového učenia a NLP techniky detekujú škodlivé inštrukcie v externom obsahu
   - Analýza dokumentov, webových stránok, e-mailov a dátových zdrojov v reálnom čase pre zabudované hrozby
   - Kontextuálne pochopenie legitímnych vs. škodlivých vzorov promptov

2. **Techniky zvýrazňovania**  
   - Rozlišovanie medzi dôveryhodnými systémovými inštrukciami a potenciálne kompromitovanými externými vstupmi
   - Metódy transformácie textov, ktoré zvyšujú relevantnosť modelu a zároveň izolujú škodlivý obsah
   - Pomáha AI systémom udržať správnu hierarchiu inštrukcií a ignorovať injektované príkazy

3. **Systémy oddelovačov a označovania dát**
   - Explicitné vyhradenie hranice medzi dôveryhodnými systémovými správami a externým vstupným textom
   - Špeciálne značky vyznačujú hranice medzi dôveryhodnými a nedôveryhodnými dátovými zdrojmi
   - Jasné oddelenie zabraňuje zmätku pri inštrukciách a neoprávnenému vykonávaniu príkazov

4. **Kontinuálne spravodajstvo o hrozbách**
   - Microsoft neustále monitoruje nové vzory útokov a aktualizuje obrany
   - Proaktívne hľadanie hrozieb pre nové injekčné techniky a vektorové útoky
   - Pravidelné aktualizácie bezpečnostných modelov pre udržanie účinnosti proti meniacim sa hrozbám

5. **Integrácia Azure Content Safety**
   - Súčasť komplexnej sady Azure AI Content Safety
   - Dodatočná detekcia pokusov o jailbreak, škodlivého obsahu a porušení bezpečnostných politík
   - Zjednotené bezpečnostné kontroly vo všetkých komponentoch AI aplikácií

**Zdroje implementácie**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Ochrana Microsoft Prompt Shields](../../../translated_images/sk/prompt-shield.ff5b95be76e9c78c.webp)


## Pokročilé bezpečnostné hrozby MCP

### Zraniteľnosti pre úlovok relácie

**Úlovok relácie** predstavuje kritický vektor útoku v stavových implementáciách MCP, kde neoprávnené subjekty získavajú a zneužívajú legitímne identifikátory relácií na zosobnenie klientov a vykonávanie neoprávnených akcií.

#### **Scenáre útokov a riziká**

- **Úlovok promptovej injekcie relácie**: Útočníci so ukradnutými ID relácií vkladajú škodlivé udalosti do serverov zdieľajúcich stav relácie, čo môže spustiť škodlivé akcie alebo prístup k citlivým dátam
- **Priame zosobnenie**: Ukradnuté ID relácií umožňujú priame volania MCP servera, ktoré obchádzajú autentifikáciu a správajú sa, akoby boli legitímnymi používateľmi
- **Kompromitované pokračovateľné toky**: Útočníci môžu predčasne ukončiť požiadavky, spôsobujúc, že legitímni klienti pokračujú s potenciálne škodlivým obsahom

#### **Bezpečnostné kontroly pre správu relácií**

**Kritické požiadavky:**
- **Overovanie autorizácie**: MCP servery implementujúce autorizáciu **MUSIA** overiť VŠETKY prichádzajúce požiadavky a **NESMÚ** sa spoliehať na relácie pre autentifikáciu
- **Bezpečná generácia relácií**: Používajte kryptograficky bezpečné, nedeterministické ID relácií generované bezpečnými generátormi náhodných čísel
- **Viazanie na používateľa**: Priraďte ID relácie k používateľsky špecifickým informáciám v formáte `<user_id>:<session_id>`, aby sa zabránilo zneužitiu relácie naprieč používateľmi
- **Správa životného cyklu relácie**: Implementujte správne vypršanie, rotáciu a neplatnosť na obmedzenie možnosti zraniteľností
- **Bezpečnosť prenosu**: Povinné HTTPS pre všetku komunikáciu, aby sa zabránilo zachyteniu ID relácie

### Problém zmäteného zástupcu

**Problém zmäteného zástupcu** nastáva, keď MCP servery fungujú ako autentifikačné proxy medzi klientmi a službami tretích strán, čím vznikajú príležitosti na obchádzanie autorizácie pomocou statickej exploatácie klientskych ID.

#### **Mechanika útokov a riziká**

- **Obídenie súhlasu založené na cookies**: Predchádzajúca autentifikácia používateľa vytvára súhlasné cookies, ktoré útočníci zneužívajú cez škodlivé autorizácie s vytvorenými URI presmerovaní
- **Krádež autorizačného kódu**: Existujúce súhlasné cookies môžu spôsobiť, že autorizačné servery preskočia obrazovky súhlasu a presmerujú kódy na útočníkom kontrolované koncové body  
- **Neoprávnený prístup k API**: Ukradnuté autorizačné kódy umožňujú výmenu tokenov a zosobnenie používateľa bez výslovného schválenia

#### **Stratégie zmiernenia**

**Povinné kontroly:**
- **Výslovné požiadavky na súhlas**: MCP proxy servery používajúce statické klientské ID **MUSIA** získať súhlas používateľa pre každý dynamicky registrovaný klient
- **Implementácia bezpečnosti OAuth 2.1**: Dodržiavať aktuálne bezpečnostné best practices OAuth vrátane PKCE (Proof Key for Code Exchange) pre všetky autorizačné požiadavky
- **Prísna validácia klienta**: Implementovať prísnu validáciu URI presmerovaní a identifikátorov klienta na zabránenie exploitácie

### Zraniteľnosti pri prenose tokenov  

**Prenos tokenov** predstavuje explicitný anti-vzor, keď MCP servery prijímajú klientove tokeny bez riadneho overenia a odosielajú ich do podriadených API, čím porušujú špecifikácie autorizácie MCP.

#### **Bezpečnostné dôsledky**

- **Obchádzanie kontroly**: Priame používanie klient-tokenu na API obchádza kritické obmedzenia rýchlosti, validácie a monitorovania
- **Poškodenie auditných záznamov**: Tokeny vydané navrchu znemožňujú identifikáciu klientov, čím sa narúša schopnosť vyšetrovania incidentov
- **Únik dát cez proxy**: Nevalidované tokeny umožňujú škodlivým aktérom používať servery ako proxy pre neoprávnený prístup k dátam
- **Porušenie dôveryhodnostnej hranice**: Dôverné predpoklady podriadených služieb môžu byť porušené, keď pôvod tokenov nemožno overiť
- **Rozšírenie útokov naprieč službami**: Kompromitované tokeny prijímané v rôznych službách umožňujú bočné pohyby

#### **Požadované bezpečnostné kontroly**

**Neodškriepiteľné požiadavky:**
- **Validácia tokenov**: MCP servery **NESMÚ** prijímať tokeny, ktoré neboli explicitne vydané pre MCP server
- **Overenie publika tokenov**: Vždy overujte, že token obsahuje nárok na publikum zodpovedajúci identite MCP servera
- **Správny životný cyklus tokenu**: Implementujte krátkodobé prístupové tokeny s bezpečnými praktikami rotácie


## Bezpečnosť dodávateľského reťazca pre AI systémy

Bezpečnosť dodávateľského reťazca sa vyvinula za hranice tradičných softvérových závislostí a zahrnuje celý ekosystém AI. Moderné implementácie MCP musia prísne overovať a monitorovať všetky AI-súvisiace komponenty, pretože každý zavádza potenciálne zraniteľnosti, ktoré môžu ohroziť integritu systému.

### Rozšírené komponenty dodávateľského reťazca AI

**Tradičné softvérové závislosti:**
- Open-source knižnice a rámce
- Kontajnerové obrazy a základné systémy  
- Vývojárske nástroje a build pipeline
- Infraštruktúrne komponenty a služby

**Špecifické prvky dodávateľského reťazca AI:**
- **Základné modely**: Predtrénované modely od rôznych poskytovateľov vyžadujúce overenie pôvodu
- **Embeddingové služby**: Externé služby vektorizácie a sémantického vyhľadávania
- **Poskytovatelia kontextu**: Dátové zdroje, vedomostné bázy a dokumentové úložiská  
- **API tretích strán**: Externé AI služby, ML pipeline a koncové body spracovania dát
- **Modelové artefakty**: Váhy, konfigurácie a varianty modelov s jemným doladením
- **Zdrojové dáta pre tréning**: Dataset-y použité pre tréning a jemné doladenie modelov

### Komplexná stratégia bezpečnosti dodávateľského reťazca

#### **Overenie komponentov a dôvera**
- **Overenie pôvodu**: Skontrolujte pôvod, licencovanie a integritu všetkých AI komponentov pred integráciou
- **Bezpečnostné hodnotenie**: Vykonajte skeny zraniteľností a bezpečnostné prehľady modelov, dátových zdrojov a AI služieb
- **Analýza reputácie**: Vyhodnoťte bezpečnostnú históriu a praktiky poskytovateľov AI služieb
- **Overovanie súladu**: Zabezpečte, že všetky komponenty spĺňajú organizačné bezpečnostné a regulačné požiadavky

#### **Bezpečné deployment pipeline**  
- **Automatická bezpečnostná kontrola CI/CD**: Integrujte bezpečnostné skenovanie naprieč automatizovanými deployment pipeline
- **Integrita artefaktov**: Implementujte kryptografické overovanie všetkých deployovaných artefaktov (kód, modely, konfigurácie)
- **Postupné nasadzovanie**: Používajte progresívne deployment stratégie s bezpečnostným overením v každom stupni
- **Dôveryhodné úložiská artefaktov**: Nasadzujte len z overených, bezpečných registrov a repozitárov artefaktov

#### **Kontinuálne monitorovanie a reakcia**
- **Skenovanie závislostí**: Neustále monitorovanie zraniteľností pre všetky softvérové a AI komponentové závislosti
- **Monitorovanie modelov**: Kontinuálne hodnotenie správania modelov, odchýlok výkonu a bezpečnostných anomálií
- **Sledovanie stavu služieb**: Monitorovanie externých AI služieb na dostupnosť, bezpečnostné incidenty a zmeny politík
- **Integrácia spravodajstva o hrozbách**: Zahrnutie bezpečnostných zdrojov špecifických pre AI a ML bezpečnostné riziká

#### **Kontrola prístupu a princíp najnižších práv**
- **Oprávnenia na úrovni komponentov**: Obmedzte prístup k modelom, dátam a službám na základe obchodnej potreby
- **Správa servisných účtov**: Implementujte vyhradené servisné účty s minimálnymi potrebnými oprávneniami
- **Segmentácia siete**: Izolujte AI komponenty a obmedzte sieťový prístup medzi službami
- **Kontroly API gateway**: Používajte centralizované API gateway na kontrolu a monitorovanie prístupu k externým AI službám

#### **Reakcia na incidenty a obnova**
- **Rýchle reakčné postupy**: Zavedené procesy pre záplaty alebo výmenu kompromitovaných AI komponentov
- **Rotácia prístupových údajov**: Automatizované systémy na rotáciu tajomstiev, API kľúčov a prihlasovacích údajov služieb
- **Možnosti návratu späť**: Schopnosť rýchlo revertovať na predchádzajúce známe dobré verzie AI komponentov
- **Obnova po narušení dodávateľského reťazca**: Špecifické postupy pre reakciu na kompromitácie AI služieb z navrchu

### Bezpečnostné nástroje Microsoft a integrácia

**GitHub Advanced Security** poskytuje komplexnú ochranu dodávateľského reťazca vrátane:
- **Skenovanie tajomstiev**: Automatizovaná detekcia prístupových údajov, API kľúčov a tokenov v repozitároch
- **Skenovanie závislostí**: Hodnotenie zraniteľností závislostí open-source a knižníc
- **Analýza CodeQL**: Statická analýza kódu pre bezpečnostné zraniteľnosti a problémy v kódovaní
- **Prehľady dodávateľského reťazca**: Viditeľnosť do stavu závislostí a bezpečnostného stavu

**Integrácia Azure DevOps & Azure Repos:**
- Bezproblémová integrácia bezpečnostných skenovaní naprieč Microsoft vývojovými platformami
- Automatizované bezpečnostné kontroly v Azure Pipelines pre AI záťaže
- Presadzovanie politík pre bezpečný deployment AI komponentov

**Interné praktiky Microsoft:**
Microsoft implementuje rozsiahle bezpečnostné praktiky dodávateľského reťazca vo všetkých produktoch. Viac informácií o overených prístupoch nájdete v [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Najlepšie praktiky základnej bezpečnosti

Implementácie MCP preberajú a stavajú na existujúcom bezpečnostnom postoji vašej organizácie. Posilnenie základných bezpečnostných praktík výrazne zvyšuje celkovú bezpečnosť AI systémov a nasadení MCP.

### Základné bezpečnostné princípy

#### **Bezpečné praktiky vývoja**
- **Súlad s OWASP**: Ochrana proti [OWASP Top 10](https://owasp.org/www-project-top-ten/) zraniteľnostiam webových aplikácií
- **AI-špecifické ochrany**: Implementujte kontroly pre [OWASP Top 10 pre LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Bezpečné spravovanie tajomstiev**: Používajte vyhradené trezory pre tokeny, API kľúče a citlivé konfiguračné údaje
- **End-to-end šifrovanie**: Implementujte bezpečnú komunikáciu vo všetkých komponentoch aplikácií a dátových tokoch
- **Validácia vstupov**: Prísna validácia všetkých užívateľských vstupov, API parametrov a dátových zdrojov

#### **Spevnenie infraštruktúry**
- **Viacfaktorová autentifikácia**: Povinná MFA pre všetky administratívne a servisné účty
- **Správa záplat**: Automatizované, včasné záplatovanie operačných systémov, rámcov a závislostí  
- **Integrácia poskytovateľov identity**: Centralizovaná správa identity cez podnikového poskytovateľa identity (Microsoft Entra ID, Active Directory)
- **Segmentácia siete**: Logická izolácia MCP komponentov na obmedzenie potenciálu bočných pohybov
- **Princíp najnižších práv**: Minimálne potrebné oprávnenia pre všetky systémové komponenty a účty

#### **Monitorovanie a detekcia bezpečnosti**
- **Komplexné zaznamenávanie**: Detailné logovanie aktivít AI aplikácií vrátane interakcií klient-server MCP
- **Integrácia SIEM**: Centralizované riadenie bezpečnostných informácií a udalostí pre detekciu anomálií
- **Behaviorálna analýza**: AI-poháňané monitorovanie na detekciu neobvyklých vzorcov správania systémov a používateľov
- **Spravodajstvo o hrozbách**: Integrácia externých zdrojov hrozieb a indikátorov kompromitácie (IOC)
- **Reakcia na incidenty**: Dobře definované postupy pre detekciu, reakciu a obnovu po bezpečnostnom incidente

#### **Architektúra Zero Trust**
- **Nikdy never, vždy overuj**: Neustále overovanie používateľov, zariadení a sieťových pripojení
- **Mikrosegmentácia**: Granulárna sieťová kontrola izolujúca jednotlivé pracovné záťaže a služby
- **Bezpečnosť zameraná na identitu**: Bezpečnostné politiky založené na overených identitách namiesto sieťovej lokality
- **Kontinuálne hodnotenie rizika**: Dynamické hodnotenie bezpečnostného postoja na základe aktuálneho kontextu a správania
- **Podmienený prístup**: Kontroly prístupu, ktoré sa prispôsobujú podľa rizikových faktorov, umiestnenia a dôvery zariadení

### Vzory integrácie do podnikov

#### **Integrácia do bezpečnostného ekosystému Microsoft**
- **Microsoft Defender for Cloud**: Komplexné riadenie bezpečnostného postoja cloudových služieb
- **Azure Sentinel**: Cloudovo natívne SIEM a SOAR schopnosti na ochranu AI záťaží
- **Microsoft Entra ID**: Podnikové riadenie identity a prístupu s podmienenými prístupovými politikami
- **Azure Key Vault**: Centralizovaná správa tajomstiev s podporou hardvérového bezpečnostného modulu (HSM)
- **Microsoft Purview**: Správa dát a súlad pre dátové zdroje a pracovné postupy AI

#### **Súlad a správa**
- **Regulačné dodržanie**: Zabezpečte, že implementácie MCP vyhovujú odvetvovým požiadavkám na súlad (GDPR, HIPAA, SOC 2)

- **Klasifikácia údajov**: Správna kategorizácia a zaobchádzanie s citlivými údajmi spracovávanými AI systémami
- **Auditné stopy**: Komplexné zaznamenávanie pre súlad s predpismi a forenzné vyšetrovanie
- **Ovládanie ochrany súkromia**: Implementácia princípov ochrany súkromia od návrhu v architektúre AI systémov
- **Riadenie zmien**: Formálne procesy na bezpečnostné kontroly úprav AI systémov

Tieto základné praktiky vytvárajú pevný bezpečnostný základ, ktorý zvyšuje efektivitu MCP-špecifických bezpečnostných opatrení a poskytuje komplexnú ochranu pre aplikácie poháňané AI.

## Kľúčové bezpečnostné zistenia

- **Viacvrstvový bezpečnostný prístup**: Kombinujte základné bezpečnostné praktiky (bezpečné kódovanie, princíp najmenej oprávnení, overovanie dodávateľského reťazca, kontinuálne monitorovanie) s AI-špecifickými kontrolami pre komplexnú ochranu

- **AI-špecifické bezpečnostné riziká**: MCP systémy čelia jedinečným hrozbám vrátane vkladania príkazov, otravy nástrojov, prevzatia relácie, problémov s nejasnými oprávneniami, zraniteľností pri prenose tokenov a nadmerných oprávnení, ktoré vyžadujú špecializované mitigácie

- **Výborná autentifikácia a autorizácia**: Implementujte robustnú autentifikáciu pomocou externých poskytovateľov identity (Microsoft Entra ID), zabezpečte správnu validáciu tokenov a nikdy neprijímajte tokeny, ktoré neboli výslovne vydané pre váš MCP server

- **Prevencia útokov na AI**: Používajte Microsoft Prompt Shields a Azure Content Safety na obranu proti nepriamemu vkladaniu príkazov a otravám nástrojov, zároveň validujte metadáta nástrojov a sledujte dynamické zmeny

- **Bezpečnosť relácií a prenosu**: Používajte kryptograficky bezpečné, nedeterministické ID relácií viazané na identity používateľov, implementujte správu životného cyklu relácie a nikdy nepoužívajte relácie na autentifikáciu

- **Najlepšie praktiky bezpečnosti OAuth**: Predchádzajte útokom typu confused deputy prostredníctvom explicitného súhlasu používateľa pre dynamicky registrovaných klientov, správnej implementácie OAuth 2.1 s PKCE a prísnej validácie URI presmerovania  

- **Zásady bezpečnosti tokenov**: Vyhnite sa anti-vzorom token passthrough, validujte nároky o publiku tokenu, implementujte krátkodobé tokeny s bezpečnou rotáciou a udržiavajte jasné hranice dôvery

- **Komplexná bezpečnosť dodávateľského reťazca**: Zaobchádzajte so všetkými komponentmi AI ekosystému (modely, embedovacie mechanizmy, poskytovatelia kontextu, externé API) s rovnakou bezpečnostnou prísnosťou ako s tradičnými softvérovými závislosťami

- **Kontinuálny vývoj**: Sledujte rýchly vývoj špecifikácií MCP, prispievajte do bezpečnostných štandardov komunity a udržiavajte adaptívny bezpečnostný prístup počas zrenia protokolu

- **Integrácia bezpečnosti Microsoft**: Využívajte komplexný bezpečnostný ekosystém Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) pre lepšiu ochranu MCP nasadení

## Komplexné zdroje

### **Oficiálna dokumentácia bezpečnosti MCP**
- [Špecifikácia MCP (Aktuálne: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Najlepšie bezpečnostné praktiky MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Špecifikácia autorizácie MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub úložisko](https://github.com/modelcontextprotocol)

### **OWASP zdroje pre bezpečnosť MCP**
- [OWASP MCP Azure bezpečnostný sprievodca](https://microsoft.github.io/mcp-azure-security-guide/) - Komplexný OWASP MCP Top 10 s návodmi na implementáciu v Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Oficiálne bezpečnostné riziká OWASP MCP
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktický bezpečnostný tréning pre MCP na Azure

### **Bezpečnostné štandardy a najlepšie praktiky**
- [Najlepšie praktiky bezpečnosti OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 pre webové aplikácie](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 pre veľké jazykové modely](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Výskum a analýza bezpečnosti AI**
- [Vkladanie príkazov v MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Útoky otravou nástrojov (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Výskumná správa o bezpečnosti MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft bezpečnostné riešenia**
- [Dokumentácia Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Bezpečnosť Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Najlepšie praktiky správy tokenov v Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Návody na implementáciu a tutoriály**
- [Azure API Management ako MCP autentifikačná brána](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID autentifikácia s MCP servermi](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Bezpečné ukladanie a šifrovanie tokenov (video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps a bezpečnosť dodávateľského reťazca**
- [Azure DevOps bezpečnosť](https://azure.microsoft.com/products/devops)
- [Azure Repos bezpečnosť](https://azure.microsoft.com/products/devops/repos/)
- [Cesta Microsoft k bezpečnosti dodávateľského reťazca](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Dodatočná bezpečnostná dokumentácia**

Pre komplexné bezpečnostné usmernenia sa obráťte na tieto špecializované dokumenty v tejto sekcii:

- **[Príklad autorizácie CIMD a DCR](./samples/cimd-dcr-auth/README.md)** - Spustiteľný TypeScript MCP server zdrojových prostriedkov `2026-07-28` porovnávajúci preferované klientské ID metaúdaje s zastaraným fallbackom dynamickej registrácie klienta
- **[Najlepšie bezpečnostné praktiky MCP](./mcp-security-best-practices.md)** - Kompletné bezpečnostné najlepšie praktiky pre implementácie MCP
- **[Implementácia Azure Content Safety](./azure-content-safety-implementation.md)** - Praktické príklady integrácie Azure Content Safety  
- **[MCP bezpečnostné kontroly](./mcp-security-controls.md)** - Najnovšie bezpečnostné kontroly a techniky pre nasadenia MCP
- **[Rýchly prehľad najlepších praktík MCP](./mcp-best-practices.md)** - Rýchly referenčný sprievodca k základným bezpečnostným praktikám MCP
- **[BlueHat 2026: Zabezpečenie budúcnosti AI: zabezpečenie MCP pomocou obrany v hĺbke](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Obranné vzory v hĺbke od Microsoft Security Response Center (MSRC)

### **Praktický bezpečnostný tréning**

- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Komplexný praktický workshop na zabezpečenie MCP serverov v Azure s progresívnymi kempmi od Base Camp po Summit
- **[OWASP MCP Azure bezpečnostný sprievodca](https://microsoft.github.io/mcp-azure-security-guide/)** - Referenčná architektúra a návod na implementáciu pre všetky OWASP MCP Top 10 riziká

---

## Čo ďalej

Ďalej: [Kapitola 3: Začíname](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->