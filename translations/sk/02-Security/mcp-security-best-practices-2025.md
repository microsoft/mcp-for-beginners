# MCP Bezpečnostné Najlepšie Praktiky - Aktualizácia December 2025

> **Dôležité**: Tento dokument odráža najnovšie bezpečnostné požiadavky [MCP Špecifikácie 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) a oficiálne [MCP Bezpečnostné Najlepšie Praktiky](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Vždy sa odvolávajte na aktuálnu špecifikáciu pre najnovšie usmernenia.

## Základné Bezpečnostné Praktiky pre Implementácie MCP

Model Context Protocol prináša jedinečné bezpečnostné výzvy, ktoré presahujú tradičnú softvérovú bezpečnosť. Tieto praktiky riešia základné bezpečnostné požiadavky aj MCP-špecifické hrozby vrátane prompt injection, tool poisoning, session hijacking, confused deputy problémov a token passthrough zraniteľností.

### **POVINNÉ Bezpečnostné Požiadavky**

**Kritické Požiadavky zo Špecifikácie MCP:**

### **POVINNÉ Bezpečnostné Požiadavky**

**Kritické Požiadavky zo Špecifikácie MCP:**

> **NESMIE**: MCP servery **NESMÚ** akceptovať žiadne tokeny, ktoré neboli explicitne vydané pre MCP server  
>  
> **MUSÍ**: MCP servery implementujúce autorizáciu **MUSIA** overiť VŠETKY prichádzajúce požiadavky  
>  
> **NESMIE**: MCP servery **NESMÚ** používať sessions na autentifikáciu  
>  
> **MUSÍ**: MCP proxy servery používajúce statické klientské ID **MUSIA** získať súhlas používateľa pre každého dynamicky registrovaného klienta

---

## 1. **Bezpečnosť Tokenov & Autentifikácia**

**Kontroly Autentifikácie & Autorizácie:**  
   - **Dôkladná Kontrola Autorizácie**: Vykonávajte komplexné audity logiky autorizácie MCP servera, aby mali prístup len zamýšľaní používatelia a klienti  
   - **Integrácia Externých Poskytovateľov Identity**: Používajte zavedených poskytovateľov identity ako Microsoft Entra ID namiesto vlastnej autentifikácie  
   - **Validácia Publikum Tokenov**: Vždy overujte, že tokeny boli explicitne vydané pre váš MCP server - nikdy neprijímajte upstream tokeny  
   - **Správny Životný Cyklus Tokenu**: Implementujte bezpečnú rotáciu tokenov, politiky expirácie a zabráňte opakovaniu tokenov

**Chránené Ukladanie Tokenov:**  
   - Používajte Azure Key Vault alebo podobné bezpečné úložiská pre všetky tajomstvá  
   - Implementujte šifrovanie tokenov v pokoji aj počas prenosu  
   - Pravidelná rotácia poverení a monitorovanie neoprávneného prístupu

## 2. **Správa Sessions & Bezpečnosť Prenosu**

**Bezpečné Praktiky Sessions:**  
   - **Kryptograficky Bezpečné ID Sessions**: Používajte bezpečné, nedeterministické ID sessions generované bezpečnými generátormi náhodných čísel  
   - **Viazanie na Používateľa**: Viažte ID sessions na identity používateľov pomocou formátov ako `<user_id>:<session_id>`, aby ste zabránili zneužitiu sessions medzi používateľmi  
   - **Správa Životného Cyklu Sessions**: Implementujte správnu expiráciu, rotáciu a neplatnosť na obmedzenie zraniteľných okien  
   - **Vynútenie HTTPS/TLS**: Povinné HTTPS pre všetku komunikáciu, aby sa zabránilo zachyteniu ID sessions

**Bezpečnosť Prenosovej Vrstvy:**  
   - Konfigurujte TLS 1.3 kde je to možné s riadnym manažmentom certifikátov  
   - Implementujte pinovanie certifikátov pre kritické spojenia  
   - Pravidelná rotácia certifikátov a overovanie platnosti

## 3. **Ochrana proti AI-špecifickým Hrozbám** 🤖

**Obrana proti Prompt Injection:**  
   - **Microsoft Prompt Shields**: Nasadzujte AI Prompt Shields pre pokročilú detekciu a filtrovanie škodlivých inštrukcií  
   - **Sanitizácia Vstupov**: Validujte a sanitizujte všetky vstupy, aby ste zabránili injection útokom a confused deputy problémom  
   - **Obsahové Hranice**: Používajte delimiter a datamarking systémy na rozlíšenie dôveryhodných inštrukcií od externého obsahu

**Prevencia Tool Poisoning:**  
   - **Validácia Metadát Nástrojov**: Implementujte kontroly integrity definícií nástrojov a monitorujte neočakávané zmeny  
   - **Dynamické Monitorovanie Nástrojov**: Sledujte runtime správanie a nastavte upozornenia na neočakávané vzory vykonávania  
   - **Schvaľovacie Procesy**: Vyžadujte explicitné schválenie používateľa pre zmeny nástrojov a schopností

## 4. **Kontrola Prístupu & Povolenia**

**Princíp Najmenších Právomocí:**  
   - Udeľujte MCP serverom len minimálne povolenia potrebné pre zamýšľanú funkcionalitu  
   - Implementujte riadenie prístupu na základe rolí (RBAC) s jemnozrnnými povoleniami  
   - Pravidelné revízie povolení a kontinuálne monitorovanie eskalácie právomocí

**Kontroly Povolení za Behu:**  
   - Aplikujte limity zdrojov na zabránenie útokom vyčerpania zdrojov  
   - Používajte izoláciu kontajnerov pre prostredia vykonávania nástrojov  
   - Implementujte prístup na vyžiadanie pre administratívne funkcie

## 5. **Bezpečnosť Obsahu & Monitorovanie**

**Implementácia Bezpečnosti Obsahu:**  
   - **Integrácia Azure Content Safety**: Používajte Azure Content Safety na detekciu škodlivého obsahu, pokusov o jailbreak a porušení pravidiel  
   - **Behaviorálna Analýza**: Implementujte runtime monitorovanie správania na detekciu anomálií v MCP serveri a vykonávaní nástrojov  
   - **Komplexné Logovanie**: Logujte všetky pokusy o autentifikáciu, volania nástrojov a bezpečnostné udalosti s bezpečným, nezmeniteľným úložiskom

**Kontinuálne Monitorovanie:**  
   - Upozornenia v reálnom čase na podozrivé vzory a neoprávnené pokusy o prístup  
   - Integrácia so SIEM systémami pre centralizované riadenie bezpečnostných udalostí  
   - Pravidelné bezpečnostné audity a penetračné testovanie implementácií MCP

## 6. **Bezpečnosť Dodávateľského Reťazca**

**Overovanie Komponentov:**  
   - **Skenovanie Závislostí**: Používajte automatizované skenovanie zraniteľností pre všetky softvérové závislosti a AI komponenty  
   - **Validácia Pôvodu**: Overujte pôvod, licencovanie a integritu modelov, dátových zdrojov a externých služieb  
   - **Podpísané Balíčky**: Používajte kryptograficky podpísané balíčky a overujte podpisy pred nasadením

**Bezpečný Vývojový Pipeline:**  
   - **GitHub Advanced Security**: Implementujte skenovanie tajomstiev, analýzu závislostí a statickú analýzu CodeQL  
   - **CI/CD Bezpečnosť**: Integrujte bezpečnostné overenia v celom automatizovanom nasadzovacom pipeline  
   - **Integrita Artefaktov**: Implementujte kryptografickú verifikáciu nasadených artefaktov a konfigurácií

## 7. **OAuth Bezpečnosť & Prevencia Confused Deputy**

**Implementácia OAuth 2.1:**  
   - **PKCE Implementácia**: Používajte Proof Key for Code Exchange (PKCE) pre všetky autorizačné požiadavky  
   - **Explicitný Súhlas**: Získajte súhlas používateľa pre každého dynamicky registrovaného klienta, aby ste zabránili confused deputy útokom  
   - **Validácia Redirect URI**: Implementujte prísnu validáciu redirect URI a identifikátorov klientov

**Bezpečnosť Proxy:**  
   - Zabráňte obchádzaniu autorizácie cez zneužitie statického klientského ID  
   - Implementujte správne schvaľovacie procesy pre prístup tretích strán k API  
   - Monitorujte krádež autorizačných kódov a neoprávnený prístup k API

## 8. **Reakcia na Incidenty & Obnova**

**Rýchle Reakčné Schopnosti:**  
   - **Automatizovaná Reakcia**: Implementujte automatizované systémy pre rotáciu poverení a obmedzenie hrozieb  
   - **Postupy Návratu**: Schopnosť rýchlo vrátiť známe dobré konfigurácie a komponenty  
   - **Forenzné Schopnosti**: Detailné auditné stopy a logovanie pre vyšetrovanie incidentov

**Komunikácia & Koordinácia:**  
   - Jasné eskalačné postupy pre bezpečnostné incidenty  
   - Integrácia s organizačnými tímami pre reakciu na incidenty  
   - Pravidelné simulácie bezpečnostných incidentov a cvičenia

## 9. **Súlad & Riadenie**

**Regulačný Súlad:**  
   - Zabezpečte, aby implementácie MCP spĺňali odvetvové požiadavky (GDPR, HIPAA, SOC 2)  
   - Implementujte klasifikáciu dát a kontrolu súkromia pre spracovanie AI dát  
   - Udržiavajte komplexnú dokumentáciu pre audity súladu

**Riadenie Zmien:**  
   - Formálne bezpečnostné revízne procesy pre všetky zmeny MCP systémov  
   - Riadenie verzií a schvaľovacie procesy pre zmeny konfigurácií  
   - Pravidelné hodnotenia súladu a analýza medzier

## 10. **Pokročilé Bezpečnostné Kontroly**

**Architektúra Zero Trust:**  
   - **Nikdy Neveriť, Vždy Overovať**: Kontinuálne overovanie používateľov, zariadení a spojení  
   - **Mikrosegmentácia**: Jemnozrnné sieťové kontroly izolujúce jednotlivé MCP komponenty  
   - **Podmienený Prístup**: Riadenie prístupu založené na riziku prispôsobujúce sa aktuálnemu kontextu a správaniu

**Ochrana Aplikácií za Behu:**  
   - **Runtime Application Self-Protection (RASP)**: Nasadzujte RASP techniky pre detekciu hrozieb v reálnom čase  
   - **Monitorovanie Výkonu Aplikácií**: Sledujte výkonnostné anomálie, ktoré môžu indikovať útoky  
   - **Dynamické Bezpečnostné Politiky**: Implementujte bezpečnostné politiky, ktoré sa prispôsobujú na základe aktuálneho bezpečnostného prostredia

## 11. **Integrácia s Microsoft Bezpečnostným Ekosystémom**

**Komplexná Microsoft Bezpečnosť:**  
   - **Microsoft Defender for Cloud**: Manažment bezpečnostnej pozície cloudu pre MCP záťaže  
   - **Azure Sentinel**: Cloud-native SIEM a SOAR schopnosti pre pokročilú detekciu hrozieb  
   - **Microsoft Purview**: Riadenie dát a súlad pre AI workflowy a dátové zdroje

**Riadenie Identity & Prístupu:**  
   - **Microsoft Entra ID**: Podnikové riadenie identity s podmienenými prístupovými politikami  
   - **Privileged Identity Management (PIM)**: Prístup na vyžiadanie a schvaľovacie procesy pre administratívne funkcie  
   - **Ochrana Identity**: Podmienený prístup založený na riziku a automatizovaná reakcia na hrozby

## 12. **Kontinuálny Vývoj Bezpečnosti**

**Byť Aktuálny:**  
   - **Monitorovanie Špecifikácie**: Pravidelné prehliadanie aktualizácií MCP špecifikácie a zmien bezpečnostných usmernení  
   - **Hrozbová Inteligencia**: Integrácia AI-špecifických hrozbových feedov a indikátorov kompromitácie  
   - **Zapojenie Bezpečnostnej Komunity**: Aktívna účasť v MCP bezpečnostnej komunite a programoch zverejňovania zraniteľností

**Adaptívna Bezpečnosť:**  
   - **Bezpečnosť Strojového Učenia**: Používajte ML založenú detekciu anomálií na identifikáciu nových vzorov útokov  
   - **Prediktívna Bezpečnostná Analytika**: Implementujte prediktívne modely pre proaktívnu identifikáciu hrozieb  
   - **Automatizácia Bezpečnosti**: Automatizované aktualizácie bezpečnostných politík na základe hrozbovej inteligencie a zmien špecifikácie

---

## **Kritické Bezpečnostné Zdroje**

### **Oficiálna MCP Dokumentácia**
- [MCP Špecifikácia (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Bezpečnostné Najlepšie Praktiky](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Špecifikácia Autorizácie](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft Bezpečnostné Riešenia**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Bezpečnosť](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Bezpečnostné Štandardy**
- [OAuth 2.0 Bezpečnostné Najlepšie Praktiky (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 pre Veľké Jazykové Modely](https://genai.owasp.org/)
- [NIST AI Rámec Riadenia Rizík](https://www.nist.gov/itl/ai-risk-management-framework)

### **Implementačné Príručky**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID s MCP Servermi](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Bezpečnostné Upozornenie**: Bezpečnostné praktiky MCP sa rýchlo vyvíjajú. Vždy overujte podľa aktuálnej [MCP špecifikácie](https://spec.modelcontextprotocol.io/) a [oficiálnej bezpečnostnej dokumentácie](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) pred implementáciou.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->