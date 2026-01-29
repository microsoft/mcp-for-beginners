# MCP Sigurnosne Najbolje Prakse - Ažuriranje za prosinac 2025.

> **Važno**: Ovaj dokument odražava najnovije sigurnosne zahtjeve [MCP specifikacije 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) i službene [MCP Sigurnosne Najbolje Prakse](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Uvijek se pozivajte na trenutnu specifikaciju za najnovije smjernice.

## Osnovne Sigurnosne Prakse za MCP Implementacije

Model Context Protocol uvodi jedinstvene sigurnosne izazove koji nadilaze tradicionalnu sigurnost softvera. Ove prakse adresiraju i temeljne sigurnosne zahtjeve i MCP-specifične prijetnje uključujući prompt injection, trovanje alata, preuzimanje sesije, probleme zbunjenog zamjenika i ranjivosti prosljeđivanja tokena.

### **OBAVEZNI Sigurnosni Zahtjevi**

**Kritični Zahtjevi iz MCP Specifikacije:**

### **OBAVEZNI Sigurnosni Zahtjevi**

**Kritični Zahtjevi iz MCP Specifikacije:**

> **NE SMIJE**: MCP serveri **NE SMIJU** prihvaćati bilo kakve tokene koji nisu izričito izdani za MCP server  
>  
> **MORA**: MCP serveri koji implementiraju autorizaciju **MORAJU** provjeriti SVE dolazne zahtjeve  
>  
> **NE SMIJE**: MCP serveri **NE SMIJU** koristiti sesije za autentikaciju  
>  
> **MORA**: MCP proxy serveri koji koriste statičke ID-jeve klijenata **MORAJU** dobiti korisnički pristanak za svakog dinamički registriranog klijenta

---

## 1. **Sigurnost Tokena i Autentikacija**

**Kontrole Autentikacije i Autorizacije:**  
   - **Temeljita Revizija Autorizacije**: Provedite sveobuhvatne revizije logike autorizacije MCP servera kako biste osigurali da samo namijenjeni korisnici i klijenti mogu pristupiti resursima  
   - **Integracija Vanjskog Davatelja Identiteta**: Koristite etablirane davatelje identiteta poput Microsoft Entra ID umjesto implementacije vlastite autentikacije  
   - **Validacija Publike Tokena**: Uvijek provjerite da su tokeni izričito izdani za vaš MCP server - nikada ne prihvaćajte tokene iz viših slojeva  
   - **Ispravan Životni Ciklus Tokena**: Implementirajte sigurnu rotaciju tokena, politike isteka i spriječite ponovnu upotrebu tokena

**Zaštićeno Pohranjivanje Tokena:**  
   - Koristite Azure Key Vault ili slične sigurne spremišta vjerodajnica za sve tajne  
   - Implementirajte enkripciju tokena u mirovanju i tijekom prijenosa  
   - Redovita rotacija vjerodajnica i nadzor za neovlašteni pristup

## 2. **Upravljanje Sesijama i Sigurnost Prijenosa**

**Sigurne Prakse Sesija:**  
   - **Kriptografski Sigurni ID-jevi Sesija**: Koristite sigurne, nedeterminističke ID-jeve sesija generirane sigurnim generatorima slučajnih brojeva  
   - **Povezivanje sa Specifičnim Korisnikom**: Povežite ID-jeve sesija s identitetima korisnika koristeći formate poput `<user_id>:<session_id>` kako biste spriječili zloupotrebu sesija između korisnika  
   - **Upravljanje Životnim Ciklusom Sesije**: Implementirajte ispravan isteka, rotaciju i poništavanje kako biste ograničili ranjivosti  
   - **Primjena HTTPS/TLS**: Obavezni HTTPS za svu komunikaciju kako bi se spriječilo presretanje ID-jeva sesija

**Sigurnost Transportnog Sloja:**  
   - Konfigurirajte TLS 1.3 gdje je moguće uz pravilno upravljanje certifikatima  
   - Implementirajte pinning certifikata za kritične veze  
   - Redovita rotacija certifikata i provjera valjanosti

## 3. **Zaštita od Prijetnji Specifičnih za AI** 🤖

**Obrana od Prompt Injection:**  
   - **Microsoft Prompt Shields**: Primijenite AI Prompt Shields za napredno otkrivanje i filtriranje zlonamjernih uputa  
   - **Sanitizacija Ulaza**: Validirajte i sanitizirajte sve ulaze kako biste spriječili injekcijske napade i probleme zbunjenog zamjenika  
   - **Granice Sadržaja**: Koristite sustave za razgraničenje i označavanje podataka kako biste razlikovali pouzdane upute od vanjskog sadržaja

**Prevencija Trovanja Alata:**  
   - **Validacija Metapodataka Alata**: Implementirajte provjere integriteta definicija alata i pratite neočekivane promjene  
   - **Dinamičko Praćenje Alata**: Nadzirite ponašanje u runtime-u i postavite upozorenja za neočekivane obrasce izvršavanja  
   - **Radni Tokovi Odobrenja**: Zahtijevajte izričito korisničko odobrenje za izmjene alata i promjene mogućnosti

## 4. **Kontrola Pristupa i Dozvole**

**Načelo Najmanjih Povlastica:**  
   - Dodijelite MCP serverima samo minimalne dozvole potrebne za namijenjenu funkcionalnost  
   - Implementirajte kontrolu pristupa temeljenu na ulogama (RBAC) s detaljnim dozvolama  
   - Redovite revizije dozvola i kontinuirani nadzor za eskalaciju privilegija

**Kontrole Dozvola u Runtime-u:**  
   - Primijenite ograničenja resursa kako biste spriječili napade iscrpljivanja resursa  
   - Koristite izolaciju kontejnera za okruženja izvršavanja alata  
   - Implementirajte pristup po potrebi za administrativne funkcije

## 5. **Sigurnost Sadržaja i Nadzor**

**Implementacija Sigurnosti Sadržaja:**  
   - **Integracija Azure Content Safety**: Koristite Azure Content Safety za otkrivanje štetnog sadržaja, pokušaja jailbreaka i kršenja politika  
   - **Analiza Ponašanja**: Implementirajte runtime nadzor ponašanja za otkrivanje anomalija u izvršavanju MCP servera i alata  
   - **Sveobuhvatno Logiranje**: Zabilježite sve pokušaje autentikacije, pozive alata i sigurnosne događaje uz sigurnu, nepromjenjivu pohranu

**Kontinuirani Nadzor:**  
   - Upozorenja u stvarnom vremenu za sumnjive obrasce i neovlaštene pokušaje pristupa  
   - Integracija sa SIEM sustavima za centralizirano upravljanje sigurnosnim događajima  
   - Redovite sigurnosne revizije i penetracijsko testiranje MCP implementacija

## 6. **Sigurnost Lanca Opskrbe**

**Verifikacija Komponenti:**  
   - **Skeniranje Ovisnosti**: Koristite automatizirano skeniranje ranjivosti za sve softverske ovisnosti i AI komponente  
   - **Validacija Podrijetla**: Provjerite podrijetlo, licenciranje i integritet modela, izvora podataka i vanjskih usluga  
   - **Potpisani Paketi**: Koristite kriptografski potpisane pakete i provjeravajte potpise prije implementacije

**Siguran Razvojni Proces:**  
   - **GitHub Advanced Security**: Implementirajte skeniranje tajni, analizu ovisnosti i statičku analizu CodeQL  
   - **Sigurnost CI/CD-a**: Integrirajte sigurnosnu validaciju kroz automatizirane pipelineove za implementaciju  
   - **Integritet Artefakata**: Implementirajte kriptografsku verifikaciju za implementirane artefakte i konfiguracije

## 7. **OAuth Sigurnost i Prevencija Zbunjenog Zamjenika**

**Implementacija OAuth 2.1:**  
   - **PKCE Implementacija**: Koristite Proof Key for Code Exchange (PKCE) za sve zahtjeve autorizacije  
   - **Izričiti Pristanak**: Dobijte korisnički pristanak za svakog dinamički registriranog klijenta kako biste spriječili napade zbunjenog zamjenika  
   - **Validacija Redirect URI-ja**: Implementirajte strogu validaciju redirect URI-ja i identifikatora klijenata

**Sigurnost Proxyja:**  
   - Spriječite zaobilaženje autorizacije iskorištavanjem statičkog ID-ja klijenta  
   - Implementirajte ispravne radne tokove pristanka za pristup API-jima trećih strana  
   - Nadzirite krađu autorizacijskih kodova i neovlašteni pristup API-ju

## 8. **Odgovor na Incident i Oporavak**

**Sposobnosti Brzog Odgovora:**  
   - **Automatizirani Odgovor**: Implementirajte automatizirane sustave za rotaciju vjerodajnica i suzbijanje prijetnji  
   - **Postupci Povratka**: Mogućnost brzog vraćanja na poznate dobre konfiguracije i komponente  
   - **Forenzičke Sposobnosti**: Detaljni audit trailovi i logiranje za istragu incidenata

**Komunikacija i Koordinacija:**  
   - Jasni postupci eskalacije za sigurnosne incidente  
   - Integracija s organizacijskim timovima za odgovor na incidente  
   - Redovite simulacije sigurnosnih incidenata i vježbe za stolom

## 9. **Usklađenost i Upravljanje**

**Regulatorna Usklađenost:**  
   - Osigurajte da MCP implementacije zadovoljavaju industrijske zahtjeve (GDPR, HIPAA, SOC 2)  
   - Implementirajte klasifikaciju podataka i kontrole privatnosti za obradu AI podataka  
   - Održavajte sveobuhvatnu dokumentaciju za reviziju usklađenosti

**Upravljanje Promjenama:**  
   - Formalni sigurnosni pregledi za sve izmjene MCP sustava  
   - Kontrola verzija i radni tokovi odobrenja za promjene konfiguracije  
   - Redovite procjene usklađenosti i analiza nedostataka

## 10. **Napredne Sigurnosne Kontrole**

**Zero Trust Arhitektura:**  
   - **Nikad Ne Vjeruj, Uvijek Provjeri**: Kontinuirana provjera korisnika, uređaja i veza  
   - **Mikrosegmentacija**: Granularne mrežne kontrole koje izoliraju pojedine MCP komponente  
   - **Uvjetni Pristup**: Kontrole pristupa temeljene na riziku koje se prilagođavaju trenutnom kontekstu i ponašanju

**Zaštita Aplikacija u Runtime-u:**  
   - **Runtime Application Self-Protection (RASP)**: Primijenite RASP tehnike za otkrivanje prijetnji u stvarnom vremenu  
   - **Praćenje Performansi Aplikacija**: Nadzirite anomalije u performansama koje mogu ukazivati na napade  
   - **Dinamičke Sigurnosne Politike**: Implementirajte sigurnosne politike koje se prilagođavaju na temelju trenutnog sigurnosnog krajolika

## 11. **Integracija Microsoft Sigurnosnog Ekosustava**

**Sveobuhvatna Microsoft Sigurnost:**  
   - **Microsoft Defender for Cloud**: Upravljanje sigurnosnim položajem u oblaku za MCP radna opterećenja  
   - **Azure Sentinel**: Izvorni SIEM i SOAR u oblaku za napredno otkrivanje prijetnji  
   - **Microsoft Purview**: Upravljanje podacima i usklađenost za AI radne tokove i izvore podataka

**Upravljanje Identitetom i Pristupom:**  
   - **Microsoft Entra ID**: Upravljanje identitetom poduzeća s politikama uvjetnog pristupa  
   - **Privileged Identity Management (PIM)**: Pristup po potrebi i radni tokovi odobrenja za administrativne funkcije  
   - **Zaštita Identiteta**: Uvjetni pristup temeljen na riziku i automatizirani odgovor na prijetnje

## 12. **Kontinuirani Razvoj Sigurnosti**

**Ostati Ažuran:**  
   - **Praćenje Specifikacije**: Redoviti pregled ažuriranja MCP specifikacije i promjena sigurnosnih smjernica  
   - **Obavještavanje o Prijetnjama**: Integracija AI-specifičnih feedova prijetnji i indikatora kompromisa  
   - **Angažman Sigurnosne Zajednice**: Aktivno sudjelovanje u MCP sigurnosnoj zajednici i programima otkrivanja ranjivosti

**Adaptivna Sigurnost:**  
   - **Sigurnost Temeljena na Strojnom Učenju**: Koristite ML za otkrivanje anomalija i identifikaciju novih obrazaca napada  
   - **Prediktivna Sigurnosna Analitika**: Implementirajte prediktivne modele za proaktivno otkrivanje prijetnji  
   - **Automatizacija Sigurnosti**: Automatizirana ažuriranja sigurnosnih politika na temelju obavještavanja o prijetnjama i promjena specifikacije

---

## **Kritični Sigurnosni Resursi**

### **Službena MCP Dokumentacija**  
- [MCP Specifikacija (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP Sigurnosne Najbolje Prakse](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP Specifikacija Autorizacije](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  

### **Microsoft Sigurnosna Rješenja**  
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [Microsoft Entra ID Sigurnost](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)  
- [GitHub Advanced Security](https://github.com/security/advanced-security)  

### **Sigurnosni Standardi**  
- [OAuth 2.0 Sigurnosne Najbolje Prakse (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 za Velike Jezične Modele](https://genai.owasp.org/)  
- [NIST AI Okvir za Upravljanje Rizicima](https://www.nist.gov/itl/ai-risk-management-framework)  

### **Vodiči za Implementaciju**  
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)  
- [Microsoft Entra ID s MCP Serverima](https://den.dev/blog/mcp-server-auth-entra-id-session/)  

---

> **Sigurnosna Napomena**: MCP sigurnosne prakse brzo se razvijaju. Uvijek provjerite prema trenutnoj [MCP specifikaciji](https://spec.modelcontextprotocol.io/) i [službenoj sigurnosnoj dokumentaciji](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) prije implementacije.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->