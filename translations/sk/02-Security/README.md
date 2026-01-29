# MCP Security: Komplexná ochrana pre AI systémy

[![MCP Security Best Practices](../../../translated_images/sk/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

Bezpečnosť je základom návrhu AI systémov, preto jej venujeme prioritu ako druhej sekcii. To korešponduje s princípom Microsoftu **Secure by Design** z [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) prináša výkonné nové schopnosti pre aplikácie riadené AI, pričom zároveň predstavuje jedinečné bezpečnostné výzvy, ktoré presahujú tradičné softvérové riziká. Systémy MCP čelia ako zavedeným bezpečnostným problémom (bezpečné kódovanie, princíp najmenších práv, bezpečnosť dodávateľského reťazca), tak aj novým špecifickým hrozbám AI vrátane prompt injection, otravy nástrojov, únosu relácií, útokov typu confused deputy, zraniteľností token passthrough a dynamickej modifikácie schopností.

Táto lekcia skúma najkritickejšie bezpečnostné riziká v implementáciách MCP — pokrýva autentifikáciu, autorizáciu, nadmerné oprávnenia, nepriame prompt injection, bezpečnosť relácií, problémy confused deputy, správu tokenov a zraniteľnosti dodávateľského reťazca. Naučíte sa praktické kontroly a osvedčené postupy na zmiernenie týchto rizík a zároveň využijete riešenia Microsoftu ako Prompt Shields, Azure Content Safety a GitHub Advanced Security na posilnenie nasadenia MCP.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- **Identifikovať špecifické hrozby MCP**: Rozpoznať jedinečné bezpečnostné riziká v systémoch MCP vrátane prompt injection, otravy nástrojov, nadmerných oprávnení, únosu relácií, problémov confused deputy, zraniteľností token passthrough a rizík dodávateľského reťazca
- **Použiť bezpečnostné kontroly**: Implementovať účinné opatrenia vrátane robustnej autentifikácie, prístupu na princípe najmenších práv, bezpečnej správy tokenov, kontrol bezpečnosti relácií a overovania dodávateľského reťazca
- **Využiť bezpečnostné riešenia Microsoftu**: Pochopiť a nasadiť Microsoft Prompt Shields, Azure Content Safety a GitHub Advanced Security na ochranu MCP záťaže
- **Overiť bezpečnosť nástrojov**: Uvedomiť si dôležitosť validácie metadát nástrojov, monitorovania dynamických zmien a obrany proti nepriamym útokom prompt injection
- **Integrovať osvedčené postupy**: Kombinovať zavedené bezpečnostné základy (bezpečné kódovanie, spevňovanie serverov, zero trust) so špecifickými kontrolami MCP pre komplexnú ochranu

# Architektúra a kontroly bezpečnosti MCP

Moderné implementácie MCP vyžadujú vrstvené bezpečnostné prístupy, ktoré riešia tradičnú softvérovú bezpečnosť aj špecifické hrozby AI. Rýchlo sa vyvíjajúca špecifikácia MCP neustále zlepšuje svoje bezpečnostné kontroly, čo umožňuje lepšiu integráciu s podnikateľskými bezpečnostnými architektúrami a zavedenými osvedčenými postupmi.

Výskum z [Microsoft Digital Defense Report](https://aka.ms/mddr) ukazuje, že **98 % nahlásených narušení by bolo zabránených dôslednou bezpečnostnou hygienou**. Najefektívnejšia ochrana kombinuje základné bezpečnostné praktiky so špecifickými kontrolami MCP — overené základné bezpečnostné opatrenia zostávajú najvýznamnejším faktorom znižovania celkového bezpečnostného rizika.

## Súčasná bezpečnostná situácia

> **Poznámka:** Tieto informácie odrážajú bezpečnostné štandardy MCP k **18. decembru 2025**. Protokol MCP sa naďalej rýchlo vyvíja a budúce implementácie môžu zaviesť nové vzory autentifikácie a vylepšené kontroly. Vždy sa odvolávajte na aktuálnu [špecifikáciu MCP](https://spec.modelcontextprotocol.io/), [MCP GitHub repozitár](https://github.com/modelcontextprotocol) a [dokumentáciu osvedčených bezpečnostných postupov](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) pre najnovšie usmernenia.

### Vývoj autentifikácie MCP

Špecifikácia MCP sa významne vyvinula vo svojom prístupe k autentifikácii a autorizácii:

- **Pôvodný prístup**: Skoré špecifikácie vyžadovali, aby vývojári implementovali vlastné autentifikačné servery, pričom MCP servery fungovali ako OAuth 2.0 autorizačné servery spravujúce autentifikáciu používateľov priamo
- **Súčasný štandard (2025-11-25)**: Aktualizovaná špecifikácia umožňuje MCP serverom delegovať autentifikáciu na externých poskytovateľov identity (napr. Microsoft Entra ID), čím sa zlepšuje bezpečnostná pozícia a znižuje zložitosť implementácie
- **Transport Layer Security**: Vylepšená podpora bezpečných transportných mechanizmov s vhodnými autentifikačnými vzormi pre lokálne (STDIO) aj vzdialené (Streamable HTTP) pripojenia

## Bezpečnosť autentifikácie a autorizácie

### Súčasné bezpečnostné výzvy

Moderné implementácie MCP čelia viacerým výzvam v oblasti autentifikácie a autorizácie:

### Riziká a hrozby

- **Nesprávne nakonfigurovaná autorizácia**: Chybné implementácie autorizácie v MCP serveroch môžu odhaliť citlivé údaje a nesprávne aplikovať prístupové kontroly
- **Kompromitácia OAuth tokenov**: Krádež tokenov lokálneho MCP servera umožňuje útočníkom vydávať sa za servery a pristupovať k downstream službám
- **Zraniteľnosti token passthrough**: Nesprávne spracovanie tokenov vytvára obchádzky bezpečnostných kontrol a medzery v zodpovednosti
- **Nadmerné oprávnenia**: MCP servery s príliš širokými právami porušujú princíp najmenších práv a rozširujú povrch útoku

#### Token passthrough: Kritický anti-vzor

**Token passthrough je v aktuálnej špecifikácii autorizácie MCP výslovne zakázaný** kvôli vážnym bezpečnostným dôsledkom:

##### Obchádzanie bezpečnostných kontrol
- MCP servery a downstream API implementujú kritické bezpečnostné kontroly (limitovanie rýchlosti, validácia požiadaviek, monitorovanie prevádzky), ktoré závisia od správnej validácie tokenov
- Priame použitie tokenov klientom voči API obchádza tieto nevyhnutné ochrany a podkopáva bezpečnostnú architektúru

##### Výzvy v zodpovednosti a audite  
- MCP servery nedokážu rozlíšiť klientov používajúcich tokeny vydané upstream, čo narušuje auditné stopy
- Logy downstream serverov zdrojov zobrazujú nesprávne pôvody požiadaviek namiesto skutočných MCP serverov ako sprostredkovateľov
- Vyšetrovanie incidentov a audit súladu sa výrazne sťažuje

##### Riziká exfiltrácie dát
- Nevalidované tvrdenia v tokenoch umožňujú útočníkom so skradnutými tokenmi používať MCP servery ako proxy na exfiltráciu dát
- Porušenie hraníc dôvery umožňuje neoprávnené prístupy, ktoré obchádzajú zamýšľané bezpečnostné kontroly

##### Viacnásobné vektory útokov
- Kompromitované tokeny akceptované viacerými službami umožňujú laterálny pohyb naprieč prepojenými systémami
- Predpoklady dôvery medzi službami môžu byť porušené, keď nie je možné overiť pôvod tokenov

### Bezpečnostné kontroly a opatrenia

**Kritické bezpečnostné požiadavky:**

> **POVINNÉ**: MCP servery **NESMÚ** akceptovať žiadne tokeny, ktoré neboli výslovne vydané pre daný MCP server

#### Kontroly autentifikácie a autorizácie

- **Dôkladná revízia autorizácie**: Vykonajte komplexné audity logiky autorizácie MCP servera, aby mali prístup len zamýšľaní používatelia a klienti k citlivým zdrojom
  - **Sprievodca implementáciou**: [Azure API Management ako autentifikačná brána pre MCP servery](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrácia identity**: [Použitie Microsoft Entra ID pre autentifikáciu MCP servera](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Bezpečná správa tokenov**: Implementujte [najlepšie praktiky validácie a životného cyklu tokenov Microsoftu](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validujte, že audience tokenu zodpovedá identite MCP servera
  - Zavádzajte správnu rotáciu a expiráciu tokenov
  - Predchádzajte opätovnému použitiu tokenov a neoprávnenému používaniu

- **Chránené ukladanie tokenov**: Bezpečne ukladajte tokeny s šifrovaním v pokoji aj počas prenosu
  - **Osvedčené postupy**: [Pokyny pre bezpečné ukladanie a šifrovanie tokenov](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementácia kontroly prístupu

- **Princíp najmenších práv**: Udeľujte MCP serverom len minimálne oprávnenia potrebné pre zamýšľanú funkcionalitu
  - Pravidelné revízie a aktualizácie oprávnení na zabránenie nárastu práv
  - **Dokumentácia Microsoftu**: [Bezpečný prístup s najmenšími právami](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Riadenie prístupu na základe rolí (RBAC)**: Implementujte jemnozrnné priradenie rolí
  - Obmedzte rozsah rolí na konkrétne zdroje a akcie
  - Vyhnite sa širokým alebo zbytočným oprávneniam, ktoré rozširujú povrch útoku

- **Kontinuálny monitoring oprávnení**: Zavádzajte priebežný audit a monitorovanie prístupu
  - Sledujte vzory používania oprávnení pre anomálie
  - Promptne odstraňujte nadmerné alebo nepoužívané práva

## Špecifické bezpečnostné hrozby AI

### Útoky prompt injection a manipulácie nástrojov

Moderné implementácie MCP čelia sofistikovaným AI-špecifickým útokom, ktoré tradičné bezpečnostné opatrenia nedokážu plne riešiť:

#### **Nepriama prompt injection (Cross-Domain Prompt Injection)**

**Nepriama prompt injection** predstavuje jednu z najkritickejších zraniteľností v AI systémoch s MCP. Útočníci vkladajú škodlivé inštrukcie do externého obsahu — dokumentov, webových stránok, e-mailov alebo dátových zdrojov — ktoré AI systémy následne spracovávajú ako legitímne príkazy.

**Scenáre útokov:**
- **Injekcia v dokumentoch**: Škodlivé inštrukcie skryté v spracovávaných dokumentoch, ktoré vyvolávajú nežiaduce AI akcie
- **Zneužitie webového obsahu**: Kompromitované webové stránky obsahujúce vložené prompt-y, ktoré manipulujú správanie AI pri scrapovaní
- **Útoky cez e-maily**: Škodlivé prompt-y v e-mailoch, ktoré spôsobujú, že AI asistenti unikajú informácie alebo vykonávajú neoprávnené akcie
- **Kontaminácia dátových zdrojov**: Kompromitované databázy alebo API poskytujúce kontaminovaný obsah AI systémom

**Reálny dopad**: Tieto útoky môžu viesť k exfiltrácii dát, porušeniu súkromia, generovaniu škodlivého obsahu a manipulácii používateľských interakcií. Pre podrobnú analýzu pozri [Prompt Injection v MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/sk/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Útoky otravy nástrojov**

**Otrava nástrojov** cieli na metadáta definujúce MCP nástroje, zneužívajúc spôsob, akým LLM interpretujú popisy nástrojov a parametre pre rozhodovanie o vykonaní.

**Mechanizmy útokov:**
- **Manipulácia metadát**: Útočníci vkladajú škodlivé inštrukcie do popisov nástrojov, definícií parametrov alebo príkladov použitia
- **Neviditeľné inštrukcie**: Skryté prompt-y v metadátach nástrojov, ktoré spracovávajú AI modely, ale sú neviditeľné pre ľudských používateľov
- **Dynamická modifikácia nástrojov („Rug Pulls“) **: Nástroje schválené používateľmi sú neskôr modifikované na škodlivé akcie bez vedomia používateľa
- **Injekcia parametrov**: Škodlivý obsah vložený do schém parametrov nástrojov, ktorý ovplyvňuje správanie modelu

**Riziká hostovaných serverov**: Vzdialené MCP servery predstavujú zvýšené riziká, pretože definície nástrojov môžu byť aktualizované po počiatočnom schválení používateľom, čím vznikajú scenáre, kde sa predtým bezpečné nástroje stanú škodlivými. Pre komplexnú analýzu pozri [Útoky otravy nástrojov (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/sk/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Ďalšie AI vektory útokov**

- **Cross-Domain Prompt Injection (XPIA)**: Sofistikované útoky využívajúce obsah z viacerých domén na obchádzanie bezpečnostných kontrol
- **Dynamická modifikácia schopností**: Zmeny schopností nástrojov v reálnom čase, ktoré unikajú počiatočným bezpečnostným hodnoteniam
- **Otrava kontextového okna**: Útoky manipulujúce veľké kontextové okná na skrytie škodlivých inštrukcií
- **Útoky zmätku modelu**: Využitie limitácií modelu na vytváranie nepredvídateľného alebo nebezpečného správania

### Dopad bezpečnostných rizík AI

**Vysoký dopad následkov:**
- **Exfiltrácia dát**: Neoprávnený prístup a krádež citlivých podnikových alebo osobných údajov
- **Porušenie súkromia**: Odhalenie osobných identifikovateľných informácií (PII) a dôverných obchodných údajov  
- **Manipulácia systémov**: Nezamýšľané modifikácie kritických systémov a pracovných tokov
- **Krádež poverení**: Kompromitácia autentifikačných tokenov a prihlasovacích údajov služieb
- **Laterálny pohyb**: Využitie kompromitovaných AI systémov ako pivotov pre širšie sieťové útoky

### Bezpečnostné riešenia Microsoft AI

#### **AI Prompt Shields: Pokročilá ochrana proti injection útokom**

Microsoft **AI Prompt Shields** poskytujú komplexnú obranu proti priamym aj nepriamym útokom prompt injection cez viacero bezpečnostných vrstiev:

##### **Základné ochranné mechanizmy:**

1. **Pokročilá detekcia a filtrovanie**
   - Algoritmy strojového učenia a NLP techniky detegujú škodlivé inštrukcie v externom obsahu
   - Analýza v reálnom čase dokumentov, webových stránok, e-mailov a dátových zdrojov na vložené hrozby
   - Kontextové rozlíšenie legitímnych a škodlivých vzorov promptov

2. **Techniky zvýrazňovania**  
   - Rozlišuje medzi dôveryhodnými systémovými inštrukciami a potenciálne kompromitovanými externými vstupmi
   - Metódy transformácie textu, ktoré zvyšujú relevantnosť modelu a izolujú škodlivý obsah
   - Pomáha AI systémom udržať správnu hierarchiu inštrukcií a ignorovať vložené príkazy

3. **Systémy oddeľovačov a označovania dát**
   - Explicitné definovanie hraníc medzi dôveryhodnými systémovými správami a externým vstupným textom
   - Špeciálne značky zvýrazňujú hranice medzi dôveryhodnými a nedôveryhodnými dátovými zdrojmi
   - Jasné oddelenie zabraňuje zmätku inštrukcií a neoprávnenému vykonávaniu príkazov

4. **Kontinuálna hrozbová inteligencia**
   - Microsoft neustále monitoruje vznikajúce vzory útokov a aktualizuje obrany
   - Proaktívne vyhľadávanie hrozieb nových techník injection a vektorov útokov
   - Pravidelné aktualizácie bezpečnostných modelov na udržanie účinnosti proti vyvíjajúcim sa hrozbám

5. **Integrácia Azure Content Safety**
   - Súčasť komplexného balíka Azure AI Content Safety
   - Dodatočná detekcia pokusov o jailbreak, škodlivého obsahu a porušení bezpečnostných politík
   - Jednotné bezpečnostné kontroly naprieč komponentmi AI aplikácií

**Implementačné zdroje**: [Dokumentácia Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/sk/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Pokročilé bezpečnostné hrozby MCP

### Zraniteľnosti únosu relácie

**Únos relácie** predstavuje kritický vektor útoku v stavových implementáciách MCP, kde neoprávnené strany získajú a zneužijú legitímne identifikátory relácií na vydávanie sa za klientov a vykonávanie neoprávnených akcií.

#### **Scenáre útokov a riziká**

- **Únos relácie a prompt injection**: Útočníci so skradnutými ID relácií vkladajú škodlivé udalosti do serverov zdieľajúcich stav relácie, čo môže vyvolať škodlivé akcie alebo prístup k citlivým údajom
- **Priama impersonácia**: Ukradnuté ID relácie umožňuje priame volania MCP servera, ktoré obchádzajú autentifikáciu a považujú útočníkov za legitímnych používateľov
- **Kompromitované obnoviteľné streamy**: Útočníci môžu predčasne ukončiť požiadavky, čo spôsobí, že legitímni klienti obnovia reláciu s potenciálne škodlivým obsahom

#### **Bezpečnostné kontroly pre správu relácií**

**Kritické požiadavky:**
- **Overenie autorizácie**: Servery MCP implementujúce autorizáciu **MUSIA** overiť VŠETKY prichádzajúce požiadavky a **NESMÚ** sa spoliehať na relácie pre autentifikáciu
- **Bezpečná generácia relácií**: Používajte kryptograficky bezpečné, nedeterministické ID relácií generované pomocou bezpečných generátorov náhodných čísel
- **Viazanie na používateľa**: Viažte ID relácií na informácie špecifické pre používateľa pomocou formátov ako `<user_id>:<session_id>`, aby ste zabránili zneužitiu relácií medzi používateľmi
- **Správa životného cyklu relácie**: Implementujte správne vypršanie platnosti, rotáciu a neplatnosť, aby ste obmedzili zraniteľné okná
- **Bezpečnosť prenosu**: Povinné HTTPS pre všetku komunikáciu, aby sa zabránilo zachyteniu ID relácie

### Problém zmäteného zástupcu

**Problém zmäteného zástupcu** nastáva, keď servery MCP pôsobia ako autentifikačné proxy medzi klientmi a službami tretích strán, čím vytvárajú príležitosti na obchádzanie autorizácie prostredníctvom zneužitia statických ID klientov.

#### **Mechanizmus útoku a riziká**

- **Obchádzanie súhlasu založené na cookie**: Predchádzajúca autentifikácia používateľa vytvára súbory cookie so súhlasom, ktoré útočníci zneužívajú prostredníctvom škodlivých autorizačných požiadaviek s upravenými URI presmerovania
- **Krádež autorizačného kódu**: Existujúce súbory cookie so súhlasom môžu spôsobiť, že autorizačné servery preskočia obrazovky so súhlasom a presmerujú kódy na koncové body ovládané útočníkom  
- **Neoprávnený prístup k API**: Ukradnuté autorizačné kódy umožňujú výmenu tokenov a impersonáciu používateľa bez výslovného schválenia

#### **Stratégie zmiernenia**

**Povinné kontroly:**
- **Výslovné požiadavky na súhlas**: Proxy servery MCP používajúce statické ID klientov **MUSIA** získať súhlas používateľa pre každého dynamicky registrovaného klienta
- **Implementácia bezpečnosti OAuth 2.1**: Dodržiavajte aktuálne bezpečnostné postupy OAuth vrátane PKCE (Proof Key for Code Exchange) pre všetky autorizačné požiadavky
- **Prísna validácia klienta**: Implementujte dôkladnú validáciu URI presmerovania a identifikátorov klientov, aby ste zabránili zneužitiu

### Zraniteľnosti pri prenose tokenov  

**Prenos tokenov** predstavuje explicitný anti-vzor, kde servery MCP prijímajú tokeny klientov bez riadnej validácie a posielajú ich ďalej do downstream API, čím porušujú špecifikácie autorizácie MCP.

#### **Bezpečnostné dôsledky**

- **Obchádzanie kontroly**: Priame použitie tokenov klientom k API obchádza kritické limity rýchlosti, validáciu a monitorovacie kontroly
- **Poškodenie audítorskej stopy**: Tokeny vydané upstream znemožňujú identifikáciu klienta, čím sa narúša schopnosť vyšetrovania incidentov
- **Exfiltrácia dát cez proxy**: Nevalidované tokeny umožňujú škodlivým aktérom používať servery ako proxy pre neoprávnený prístup k dátam
- **Porušenie hraníc dôvery**: Predpoklady dôvery downstream služieb môžu byť porušené, keď nie je možné overiť pôvod tokenov
- **Rozšírenie útokov na viaceré služby**: Kompromitované tokeny akceptované v rôznych službách umožňujú laterálny pohyb

#### **Povinné bezpečnostné kontroly**

**Neodvolateľné požiadavky:**
- **Validácia tokenov**: Servery MCP **NESMÚ** prijímať tokeny, ktoré neboli explicitne vydané pre server MCP
- **Overenie publika**: Vždy validujte, či nároky publika tokenu zodpovedajú identite servera MCP
- **Správny životný cyklus tokenov**: Implementujte krátkodobé prístupové tokeny s bezpečnými praktikami rotácie


## Bezpečnosť dodávateľského reťazca pre AI systémy

Bezpečnosť dodávateľského reťazca sa vyvinula za hranice tradičných softvérových závislostí a zahŕňa celý ekosystém AI. Moderné implementácie MCP musia dôkladne overovať a monitorovať všetky komponenty súvisiace s AI, pretože každý z nich predstavuje potenciálne zraniteľnosti, ktoré môžu ohroziť integritu systému.

### Rozšírené komponenty dodávateľského reťazca AI

**Tradičné softvérové závislosti:**
- Open-source knižnice a rámce
- Kontajnerové obrazy a základné systémy  
- Vývojové nástroje a build pipeline
- Infrastrukturné komponenty a služby

**Špecifické prvky dodávateľského reťazca AI:**
- **Základné modely**: Predtrénované modely od rôznych poskytovateľov vyžadujúce overenie pôvodu
- **Služby vkladania (embedding)**: Externé služby vektorovania a sémantického vyhľadávania
- **Poskytovatelia kontextu**: Zdrojové dáta, znalostné bázy a úložiská dokumentov  
- **API tretích strán**: Externé AI služby, ML pipeline a koncové body spracovania dát
- **Modelové artefakty**: Váhy, konfigurácie a jemne doladené varianty modelov
- **Zdrojové dáta na tréning**: Dataset-y používané na tréning a doladenie modelov

### Komplexná stratégia bezpečnosti dodávateľského reťazca

#### **Overenie komponentov a dôvera**
- **Overenie pôvodu**: Overte pôvod, licencovanie a integritu všetkých AI komponentov pred integráciou
- **Bezpečnostné hodnotenie**: Vykonajte skeny zraniteľností a bezpečnostné revízie modelov, zdrojov dát a AI služieb
- **Analýza reputácie**: Vyhodnoťte bezpečnostnú históriu a praktiky poskytovateľov AI služieb
- **Overenie súladu**: Zabezpečte, aby všetky komponenty spĺňali organizačné bezpečnostné a regulačné požiadavky

#### **Bezpečné deployment pipeline**  
- **Automatizované CI/CD zabezpečenie**: Integrujte bezpečnostné skenovanie v celom automatizovanom nasadzovacom pipeline
- **Integrita artefaktov**: Implementujte kryptografické overovanie všetkých nasadených artefaktov (kód, modely, konfigurácie)
- **Postupné nasadzovanie**: Používajte progresívne stratégie nasadzovania s bezpečnostnou validáciou v každom kroku
- **Dôveryhodné úložiská artefaktov**: Nasadzujte iba z overených, bezpečných registri a úložísk artefaktov

#### **Kontinuálny monitoring a reakcia**
- **Skenovanie závislostí**: Neustále monitorovanie zraniteľností všetkých softvérových a AI komponentov
- **Monitoring modelov**: Kontinuálne hodnotenie správania modelov, posunu výkonu a bezpečnostných anomálií
- **Sledovanie stavu služieb**: Monitorovanie dostupnosti, bezpečnostných incidentov a zmien politík externých AI služieb
- **Integrácia hrozieb**: Zahrnutie hrozbových feedov špecifických pre bezpečnostné riziká AI a ML

#### **Kontrola prístupu a princíp minimálnych práv**
- **Oprávnenia na úrovni komponentov**: Obmedzte prístup k modelom, dátam a službám na základe obchodnej potreby
- **Správa servisných účtov**: Implementujte vyhradené servisné účty s minimálnymi potrebnými oprávneniami
- **Segmentácia siete**: Izolujte AI komponenty a obmedzte sieťový prístup medzi službami
- **Kontroly API brány**: Používajte centralizované API brány na kontrolu a monitorovanie prístupu k externým AI službám

#### **Reakcia na incidenty a obnova**
- **Rýchle reakčné postupy**: Zavedené procesy na záplaty alebo výmenu kompromitovaných AI komponentov
- **Rotácia poverení**: Automatizované systémy na rotáciu tajomstiev, API kľúčov a servisných poverení
- **Možnosti návratu späť**: Schopnosť rýchlo vrátiť predchádzajúce známe dobré verzie AI komponentov
- **Obnova po narušení dodávateľského reťazca**: Špecifické postupy na reakciu na kompromitovanie upstream AI služieb

### Microsoft bezpečnostné nástroje a integrácia

**GitHub Advanced Security** poskytuje komplexnú ochranu dodávateľského reťazca vrátane:
- **Skenovanie tajomstiev**: Automatická detekcia poverení, API kľúčov a tokenov v repozitároch
- **Skenovanie závislostí**: Hodnotenie zraniteľností open-source závislostí a knižníc
- **CodeQL analýza**: Statická analýza kódu na bezpečnostné zraniteľnosti a chyby v kódovaní
- **Prehľad dodávateľského reťazca**: Viditeľnosť zdravia a bezpečnostného stavu závislostí

**Integrácia Azure DevOps & Azure Repos:**
- Bezproblémová integrácia bezpečnostného skenovania naprieč Microsoft vývojovými platformami
- Automatizované bezpečnostné kontroly v Azure Pipelines pre AI záťaže
- Vynucovanie politík pre bezpečné nasadzovanie AI komponentov

**Interné praktiky Microsoftu:**
Microsoft implementuje rozsiahle bezpečnostné praktiky dodávateľského reťazca vo všetkých produktoch. Viac o overených prístupoch nájdete v [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Najlepšie bezpečnostné praktiky základov

Implementácie MCP nadväzujú a rozvíjajú existujúcu bezpečnostnú pozíciu vašej organizácie. Posilnenie základných bezpečnostných praktík výrazne zvyšuje celkovú bezpečnosť AI systémov a nasadení MCP.

### Základné bezpečnostné princípy

#### **Bezpečné vývojové praktiky**
- **Súlad s OWASP**: Chráňte sa pred [OWASP Top 10](https://owasp.org/www-project-top-ten/) zraniteľnosťami webových aplikácií
- **Ochrany špecifické pre AI**: Implementujte kontroly pre [OWASP Top 10 pre LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Bezpečná správa tajomstiev**: Používajte vyhradené trezory pre tokeny, API kľúče a citlivé konfiguračné údaje
- **End-to-End šifrovanie**: Implementujte bezpečnú komunikáciu vo všetkých komponentoch aplikácie a dátových tokoch
- **Validácia vstupov**: Dôkladná validácia všetkých používateľských vstupov, API parametrov a zdrojov dát

#### **Zosilnenie infraštruktúry**
- **Viacfaktorová autentifikácia**: Povinná MFA pre všetky administratívne a servisné účty
- **Správa záplat**: Automatizované a včasné záplatovanie operačných systémov, rámcov a závislostí  
- **Integrácia poskytovateľov identity**: Centralizovaná správa identity cez podnikových poskytovateľov identity (Microsoft Entra ID, Active Directory)
- **Segmentácia siete**: Logická izolácia MCP komponentov na obmedzenie potenciálu laterálneho pohybu
- **Princíp minimálnych práv**: Minimálne potrebné oprávnenia pre všetky systémové komponenty a účty

#### **Monitorovanie a detekcia bezpečnosti**
- **Komplexné logovanie**: Detailné logovanie aktivít AI aplikácií vrátane interakcií klient-server MCP
- **Integrácia SIEM**: Centralizované riadenie bezpečnostných informácií a udalostí pre detekciu anomálií
- **Behaviorálna analytika**: AI-poháňané monitorovanie na detekciu nezvyčajných vzorcov v správaní systému a používateľov
- **Hrozbová inteligencia**: Integrácia externých hrozbových feedov a indikátorov kompromitácie (IOC)
- **Reakcia na incidenty**: Jasne definované postupy pre detekciu, reakciu a obnovu po bezpečnostných incidentoch

#### **Architektúra Zero Trust**
- **Nikdy neveriť, vždy overovať**: Neustále overovanie používateľov, zariadení a sieťových pripojení
- **Mikrosegmentácia**: Granulárne sieťové kontroly izolujúce jednotlivé záťaže a služby
- **Bezpečnosť zameraná na identitu**: Bezpečnostné politiky založené na overených identitách namiesto sieťovej lokality
- **Kontinuálne hodnotenie rizika**: Dynamické hodnotenie bezpečnostnej pozície na základe aktuálneho kontextu a správania
- **Podmienený prístup**: Kontroly prístupu prispôsobené na základe rizikových faktorov, lokality a dôvery zariadenia

### Vzory integrácie do podnikového prostredia

#### **Integrácia do Microsoft bezpečnostného ekosystému**
- **Microsoft Defender for Cloud**: Komplexné riadenie bezpečnostnej pozície cloudov
- **Azure Sentinel**: Cloud-native SIEM a SOAR schopnosti na ochranu AI záťaží
- **Microsoft Entra ID**: Podniková správa identity a prístupu s politikami podmieneného prístupu
- **Azure Key Vault**: Centralizovaná správa tajomstiev s podporou hardvérového bezpečnostného modulu (HSM)
- **Microsoft Purview**: Správa dát a súlad pre AI zdroje dát a pracovné postupy

#### **Súlad a riadenie**
- **Regulačné zosúladenie**: Zabezpečte, aby implementácie MCP spĺňali odvetvové regulačné požiadavky (GDPR, HIPAA, SOC 2)
- **Klasifikácia dát**: Správna kategorizácia a spracovanie citlivých dát spracovávaných AI systémami
- **Audítorské stopy**: Komplexné logovanie pre regulačný súlad a forenzné vyšetrovanie
- **Ovládanie súkromia**: Implementácia princípov ochrany súkromia už v návrhu AI systémov
- **Riadenie zmien**: Formálne procesy pre bezpečnostné revízie zmien AI systémov

Tieto základné praktiky vytvárajú robustný bezpečnostný základ, ktorý zvyšuje účinnosť MCP-špecifických bezpečnostných kontrol a poskytuje komplexnú ochranu pre AI aplikácie.

## Kľúčové bezpečnostné závery

- **Viacvrstvový bezpečnostný prístup**: Kombinujte základné bezpečnostné praktiky (bezpečné kódovanie, minimálne práva, overovanie dodávateľského reťazca, kontinuálny monitoring) s AI-špecifickými kontrolami pre komplexnú ochranu

- **Špecifické hrozby AI**: Systémy MCP čelia jedinečným rizikám vrátane injekcie promptov, otravy nástrojov, prevzatia relácií, problémov zmäteného zástupcu, zraniteľností pri prenose tokenov a nadmerných oprávnení, ktoré vyžadujú špecializované zmiernenia

- **Excelentnosť v autentifikácii a autorizácii**: Implementujte robustnú autentifikáciu pomocou externých poskytovateľov identity (Microsoft Entra ID), vynucujte správnu validáciu tokenov a nikdy neprijímajte tokeny, ktoré neboli explicitne vydané pre váš MCP server

- **Prevencia AI útokov**: Nasadzujte Microsoft Prompt Shields a Azure Content Safety na obranu proti nepriamym útokom injekcie promptov a otravy nástrojov, pričom validujte metadáta nástrojov a monitorujte dynamické zmeny

- **Bezpečnosť relácií a prenosu**: Používajte kryptograficky bezpečné, nedeterministické ID relácií viazané na identity používateľov, implementujte správnu správu životného cyklu relácií a nikdy nepoužívajte relácie na autentifikáciu

- **Najlepšie praktiky OAuth bezpečnosti**: Predchádzajte útokom zmäteného zástupcu prostredníctvom výslovného súhlasu používateľa pre dynamicky registrovaných klientov, správnej implementácie OAuth 2.1 s PKCE a prísnej validácie URI presmerovania  

- **Zásady bezpečnosti tokenov**: Vyhnite sa anti-vzoru prenosu tokenov, validujte nároky publika tokenov, implementujte krátkodobé tokeny s bezpečnou rotáciou a udržiavajte jasné hranice dôvery

- **Komplexná bezpečnosť dodávateľského reťazca**: Zaobchádzajte so všetkými komponentmi AI ekosystému (modely, embeddingy, poskytovatelia kontextu, externé API) s rovnakou bezpečnostnou prísnosťou ako s tradičnými softvérovými závislosťami

- **Kontinuálny vývoj**: Sledujte rýchlo sa vyvíjajúce špecifikácie MCP, prispievajte do bezpečnostných štandardov komunity a udržiavajte adaptívnu bezpečnostnú pozíciu s rastom protokolu

- **Integrácia Microsoft bezpečnosti**: Využívajte komplexný bezpečnostný ekosystém Microsoftu (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) pre zvýšenú ochranu nasadenia MCP

## Komplexné zdroje

### **Oficiálna dokumentácia MCP bezpečnosti**
- [Špecifikácia MCP (aktuálne: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Najlepšie bezpečnostné praktiky MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Špecifikácia autorizácie MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [GitHub repozitár MCP](https://github.com/modelcontextprotocol)

### **Bezpečnostné štandardy a najlepšie praktiky**
- [Najlepšie bezpečnostné praktiky OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 bezpečnosti webových aplikácií](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 pre veľké jazykové modely](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Výskum a analýza bezpečnosti AI**
- [Injekcia promptov v MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Útoky otravy nástrojov (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Bezpečnostný výskumný briefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Bezpečnostné riešenia**
- [Dokumentácia Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Služba Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Bezpečnosť](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Najlepšie postupy správy tokenov Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Pokročilá bezpečnosť](https://github.com/security/advanced-security)

### **Príručky a návody na implementáciu**
- [Azure API Management ako MCP autentifikačná brána](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID autentifikácia s MCP servermi](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Bezpečné ukladanie a šifrovanie tokenov (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps a bezpečnosť dodávateľského reťazca**
- [Azure DevOps Bezpečnosť](https://azure.microsoft.com/products/devops)
- [Azure Repos Bezpečnosť](https://azure.microsoft.com/products/devops/repos/)
- [Cesta Microsoft k bezpečnosti dodávateľského reťazca](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Ďalšia bezpečnostná dokumentácia**

Pre komplexné bezpečnostné usmernenia sa obráťte na tieto špecializované dokumenty v tejto sekcii:

- **[MCP Najlepšie bezpečnostné postupy 2025](./mcp-security-best-practices-2025.md)** - Kompletné najlepšie bezpečnostné postupy pre implementácie MCP
- **[Implementácia Azure Content Safety](./azure-content-safety-implementation.md)** - Praktické príklady implementácie integrácie Azure Content Safety  
- **[MCP Bezpečnostné kontroly 2025](./mcp-security-controls-2025.md)** - Najnovšie bezpečnostné kontroly a techniky pre nasadenia MCP
- **[Rýchla referencia najlepších postupov MCP](./mcp-best-practices.md)** - Rýchly referenčný sprievodca základnými bezpečnostnými praktikami MCP

---

## Čo ďalej

Ďalej: [Kapitola 3: Začíname](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->