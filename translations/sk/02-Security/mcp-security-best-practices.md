# Najlepšie bezpečnostné postupy MCP - aktualizácia september 2026

> **Dôležité:** Tento dokument odráža
> [špecifikáciu MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> a oficiálne
> [Najlepšie bezpečnostné postupy MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## 🏔️ Praktický bezpečnostný tréning

Pre získanie praktických skúseností s implementáciou odporúčame **[workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** – komplexnú riadenú expedíciu za zabezpečením MCP serverov v Azure. Workshop pokrýva všetky riziká OWASP MCP Top 10 cez metodiku „zraniteľný → zneužitie → oprava → overenie“.

Všetky postupy v tomto dokumente zodpovedajú **[sprievodcovi MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)**, ktorý poskytuje usmernenia špecifické pre Azure.

## Základné bezpečnostné postupy pre implementácie MCP

Model Context Protocol prináša jedinečné bezpečnostné výzvy, ktoré presahujú
tradičnú softvérovú bezpečnosť. Tieto postupy riešia základné
požiadavky a špecifické hrozby MCP vrátane injekcie promptov, otravy nástrojov,
prebratia stavových identifikátorov, problémov s nejednoznačnými správami (confused deputy) a
zraniteľností pri prenose tokenov.

### **POVINNÉ bezpečnostné požiadavky**

**Kritické požiadavky zo špecifikácie MCP:**

> **NESMIE**: MCP servery **NESMÚ** akceptovať žiadne tokeny, ktoré neboli explicitne vydané pre MCP server
>
> **MUSÍ**: MCP servery implementujúce autorizáciu **MUSIA** overovať VŠETKY prichádzajúce požiadavky
>  
> **NESMIE**: MCP servery **NESMÚ** používať relácie na autentifikáciu
>
> **MUSÍ**: MCP proxy servery používajúce statické klientské ID tretej strany **MUSIA**
> získať súhlas pre každý MCP klient pred odoslaním autorizácie

---

## 1. **Bezpečnosť tokenov a autentifikácia**

**Kontroly autentifikácie a autorizácie:**
   - **Dôkladná revízia autorizácie**: Vykonávajte komplexné audity autorizačnej logiky MCP servera, aby ste zabezpečili, že k zdrojom majú prístup iba zamýšľaní používatelia a klienti
   - **Integrácia s externým poskytovateľom identity**: Používajte zavedených poskytovateľov identity ako Microsoft Entra ID namiesto implementácie vlastnej autentifikácie
   - **Validácia publika tokenu**: Vždy overujte, že tokeny boli explicitne vydané pre váš MCP server – nikdy neprijímajte tokeny z iných zdrojov
   - **Správny životný cyklus tokenu**: Implementujte bezpečné rotovanie tokenov, politiky vypršania platnosti a predchádzajte opakovaniu útokov s tokenmi

**Chránené ukladanie tokenov:**
   - Používajte Azure Key Vault alebo podobné bezpečné úložiská pre všetky tajomstvá
   - Implementujte šifrovanie tokenov počas ukladania aj prenosu
   - Pravidelná rotácia poverení a monitorovanie neoprávneného prístupu

## 2. **Správa stavebných identifikátorov a bezpečnosť prenosu**

**Postupy zabezpečenia aplikačného stavu:**

- **Nepriehľadné stavebné identifikátory**: Používajte bezpečné, nedeterministické identifikátory pre
   aplikačný stav, ktorý pretrváva cez požiadavky
- **Väzba na používateľa**: Väzba identifikátorov na strane servera na autentifikovanú
   entitu a odmietanie opätovného použitia medzi používateľmi
- **Správa životného cyklu**: Vypršanie a odvolanie identifikátorov na obmedzenie
   zraniteľnosti
- **Autorizácia pri každej požiadavke**: Nikdy nespoľahlive na stavový identifikátor ako na autentifikáciu;
   autorizujte každú požiadavku, ktorá ho predstavuje

**Bezpečnosť vrstvy prenosu:**

- Vyžadujte HTTPS pre vzdialený HTTP prenos v produkcii
- Používajte izoláciu procesov a poverenia prostredia pre miestne stdio servery
- Konfigurujte moderné TLS s riadnou rotáciou a validáciou certifikátov


## 3. **Ochrana špecifická pre AI** 🤖

**Obrana proti Prompt Injection:**
   - **Microsoft Prompt Shields**: Nasadenie AI Prompt Shields pre pokročilú detekciu a filtrovanie škodlivých inštrukcií
   - **Sanitizácia vstupov**: Validácia a sanitizácia všetkých vstupov na prevenciu injekčných útokov a problémov s zmätenými zástupcami
   - **Obsahové hranice**: Použitie systémov oddeľovačov a označovania dát na rozlíšenie dôveryhodných inštrukcií a externého obsahu

**Prevencia pred otravovaním nástrojov:**
   - **Validácia metadát nástrojov**: Implementácia kontrol integrity definícií nástrojov a monitorovanie neočakávaných zmien
   - **Dynamické monitorovanie nástrojov**: Sledovanie správania v čase behu a nastavenie upozornení na neočakávané vzory vykonávania
   - **Schvaľovacie pracovné postupy**: Vyžadovanie explicitného súhlasu používateľa pri zmenách nástrojov a ich schopností

## 4. **Riadenie prístupu & oprávnenia**

**Princíp najmenších právomocí:**
   - Udeľovať MCP serverom iba minimálne oprávnenia potrebné na zamýšľanú funkcionalitu
   - Implementovať riadenie prístupu na základe rolí (RBAC) s jemnozrnnými oprávneniami
   - Pravidelné prehodnocovanie oprávnení a nepretržité monitorovanie eskalácie oprávnení

**Ovládanie oprávnení za behu:**
   - Použiť limity zdrojov na prevenciu útokov vyčerpania zdrojov
   - Použiť izoláciu kontajnerov pre prostredia vykonávania nástrojov  
   - Implementovať prístup presne na čas pre administratívne funkcie

## 5. **Bezpečnosť obsahu & monitorovanie**

**Implementácia bezpečnosti obsahu:**
   - **Integrácia Azure Content Safety**: Použiť Azure Content Safety na detekciu škodlivého obsahu, pokusov o jailbreak a porušení pravidiel
   - **Behaviorálna analýza**: Implementovať monitorovanie správania za behu na detekciu anomálií v MCP serveri a vykonávaní nástrojov
   - **Komplexné zaznamenávanie**: Logovať všetky pokusy o autentifikáciu, spustenia nástrojov a bezpečnostné udalosti s bezpečným, nezmeniteľným úložiskom

**Neustále monitorovanie:**
   - Upozorňovanie v reálnom čase na podozrivé vzory a neautorizované pokusy o prístup  
   - Integrácia so SIEM systémami pre centralizované riadenie bezpečnostných udalostí
   - Pravidelné bezpečnostné audity a penetračné testy implementácií MCP

## 6. **Bezpečnosť dodávateľského reťazca**

**Overovanie komponentov:**
   - **Skenovanie závislostí**: Použiť automatizované skenovanie zraniteľností všetkých softvérových závislostí a AI komponentov
   - **Validácia pôvodu**: Overiť pôvod, licencovanie a integritu modelov, dátových zdrojov a externých služieb
   - **Podpísané balíčky**: Použiť kryptograficky podpísané balíčky a overiť podpisy pred nasadením

**Bezpečný vývojový proces:**
   - **GitHub Advanced Security**: Implementovať skenovanie tajomstiev, analýzu závislostí a statickú analýzu CodeQL
   - **Bezpečnosť CI/CD**: Integrovať bezpečnostnú validáciu počas celého automatizovaného deploymentu
   - **Integrita artefaktov**: Implementovať kryptografické overovanie nasadených artefaktov a konfigurácií

## 7. **OAuth bezpečnosť a prevencia zmätených zástupcov**

**Implementácia OAuth 2.1:**
   - **Implementácia PKCE**: Použiť Proof Key for Code Exchange (PKCE) pri všetkých autorizačných požiadavkách
    - **Registrácia klienta**: Preferovať dokumenty metadát Client ID alebo
       predregistráciu; použitie zastaraného Dynamic Client Registration len ako
       záložnú kompatibilitu
    - **Explicitný súhlas**: MCP proxy používajúce statický third-party client ID musia
       získať súhlas pre každého MCP klienta pred odoslaním autorizácie
   - **Validácia URI presmerovania**: Implementovať prísne overovanie redirect URI a identifikátorov klientov

**Bezpečnosť proxy:**
   - Zabrániť obchádzaniu autorizácie zneužitím statického client ID
   - Implementovať správne pracovné postupy na súhlas pre prístup k API tretích strán
   - Monitorovať krádež autorizačných kódov a neautorizovaný prístup k API

## 8. **Reakcia na incidenty a obnova**


**Schopnosti rýchlej reakcie:** 

   - **Automatická odpoveď**: Implementovať automatizované systémy na rotáciu poverení a obmedzenie hrozieb
   - **Postupy vrátenia späť**: Schopnosť rýchlo sa vrátiť k overeným konfiguráciám a komponentom
   - **Forenzné schopnosti**: Podrobné auditné stopy a protokolovanie na vyšetrovanie incidentov

**Komunikácia a koordinácia:**
   - Jasné postupy eskalácie bezpečnostných incidentov
   - Integrácia s organizačnými tímami na reakciu na incidenty
   - Pravidelné simulácie bezpečnostných incidentov a cvičenia za stolom

## 9. **Zhodnosť a správa**

**Regulačná zhoda:**
   - Zabezpečiť, aby implementácie MCP spĺňali špecifické požiadavky odvetvia (GDPR, HIPAA, SOC 2)
   - Implementovať klasifikáciu dát a kontrolu súkromia pre spracovanie údajov AI
   - Udržiavať komplexnú dokumentáciu pre audit zhody

**Riadenie zmien:**
   - Formálne procesy bezpečnostného preskúmania všetkých zmien systémov MCP
   - Riadenie verzií a pracovné toky schválenia pre zmeny konfigurácie
   - Pravidelné hodnotenia zhody a analýza medzier

## 10. **Pokročilé bezpečnostné kontroly**

**Architektúra Zero Trust:**
   - **Nikdy neveriť, vždy overovať**: Neustála verifikácia používateľov, zariadení a pripojení
   - **Mikrosegmentácia**: Granulárne sieťové kontroly izolujúce jednotlivé komponenty MCP
   - **Podmienečný prístup**: Riadenie prístupu založené na riziku prispôsobujúce sa aktuálnemu kontextu a správaniu

**Ochrana aplikácií počas behu:**
   - **Runtime Application Self-Protection (RASP)**: Nasadenie techník RASP na detekciu hrozieb v reálnom čase
   - **Monitorovanie výkonu aplikácií**: Monitorovať výkonnostné anomálie, ktoré môžu indikovať útoky
   - **Dynamické bezpečnostné politiky**: Implementovať bezpečnostné politiky, ktoré sa prispôsobujú aktuálnemu bezpečnostnému prostrediu

## 11. **Integrácia s Microsoft bezpečnostným ekosystémom**

**Komplexná bezpečnosť Microsoft:**
   - **Microsoft Defender for Cloud**: Správa bezpečnostného postavenia cloudu pre pracovné záťaže MCP
   - **Azure Sentinel**: Nativný cloudový SIEM a SOAR pre pokročilú detekciu hrozieb
   - **Microsoft Purview**: Správa dát a zhoda pre AI workflowy a dátové zdroje

**Riadenie identity a prístupu:**
   - **Microsoft Entra ID**: Podnikové riadenie identity s pravidlami podmienečného prístupu
   - **Privileged Identity Management (PIM)**: Prístup „just-in-time“ a pracovné toky schválení pre administratívne funkcie
   - **Ochrana identity**: Podmienečný prístup založený na riziku a automatická odpoveď na hrozby

## 12. **Neustály vývoj bezpečnosti**

**Byť v obraze:**
   - **Monitorovanie špecifikácií**: Pravidelné prehliadanie aktualizácií špecifikácií MCP a zmien bezpečnostných odporúčaní
   - **Hrozbová inteligencia**: Integrácia špecifických hrozbových zdrojov AI a indikátorov kompromitácie
   - **Zapojenie do bezpečnostnej komunity**: Aktívna účasť v bezpečnostnej komunite MCP a programoch zverejňovania zraniteľností

**Adaptívna bezpečnosť:**
   - **Bezpečnosť strojového učenia**: Použiť detekciu anomálií založenú na ML na identifikáciu nových vzorov útokov
   - **Prediktívna bezpečnostná analytika**: Implementovať prediktívne modely pre proaktívnu identifikáciu hrozieb
   - **Automatizácia bezpečnosti**: Automatické aktualizácie bezpečnostných politík na základe hrozbovej inteligencie a zmien špecifikácií

---

## **Kritické bezpečnostné zdroje**

### **Oficiálna dokumentácia MCP**
- [MCP Špecifikácia (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Bezpečnostné najlepšie postupy](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Špecifikácia autorizácie](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP bezpečnostné zdroje**
- [OWASP MCP Azure bezpečnostný sprievodca](https://microsoft.github.io/mcp-azure-security-guide/) - Kompletný OWASP MCP Top 10 s implementáciou Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Oficiálne bezpečnostné riziká OWASP MCP
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktické bezpečnostné školenie pre MCP na Azure

### **Microsoft bezpečnostné riešenia**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID bezpečnosť](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Bezpečnostné štandardy**
- [OAuth 2.0 Najlepšie bezpečnostné postupy (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 pre veľké jazykové modely](https://genai.owasp.org/)
- [NIST AI rámec pre riadenie rizík](https://www.nist.gov/itl/ai-risk-management-framework)

### **Implementačné príručky**
- [Azure API Management MCP autentifikačná brána](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID s MCP servermi](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Bezpečnostné upozornenie:** Bezpečnostné praktiky MCP sa rýchlo vyvíjajú. Vždy overte
> podľa aktuálnej [špecifikácie MCP](https://modelcontextprotocol.io/specification/2026-07-28/)
> a [oficiálnej bezpečnostnej dokumentácie](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> pred implementáciou.

## Čo ďalej

- Prečítajte si: [MCP bezpečnostné kontroly](./mcp-security-controls.md)
- Vráťte sa na: [Prehľad bezpečnostného modulu](./README.md)
- Pokračujte na: [Modul 3: Začíname](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->