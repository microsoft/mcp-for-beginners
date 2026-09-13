# Najbolje sigurnosne prakse MCP - ažuriranje za rujan 2026.

> **Važno:** Ovaj dokument odražava
> [MCP specifikaciju 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> i službene
> [najbolje sigurnosne prakse MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## 🏔️ Praktična sigurnosna obuka

Za praktično iskustvo implementacije preporučujemo **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - sveobuhvatnu vođenu ekspediciju za osiguranje MCP poslužitelja u Azureu. Radionica pokriva svih OWASP MCP Top 10 rizika kroz metodologiju "ranjivo → eksploatacija → popravak → validacija".

Sve prakse u ovom dokumentu usklađene su s **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** za smjernice implementacije specifične za Azure.

## Osnovne sigurnosne prakse za implementacije MCP-a

Model Context Protocol uvodi jedinstvene sigurnosne izazove koji nadilaze
tradicionalnu sigurnost softvera. Ove prakse obrađuju temeljne
zahtjeve i specifične prijetnje MCP-a uključujući ubrizgavanje upita, trovanje alata,
preuzimanje stanja, probleme zbunjenog zamjenika i ranjivosti prolaza tokena.


### **OBAVEZNI sigurnosni zahtjevi** 

**Kritični zahtjevi iz MCP specifikacije:**

> **NE SMIJEĆE**: MCP poslužitelji **NE SMIJU** prihvaćati nikakve token-e koji nisu izričito izdani za MCP poslužitelj
> 
> **MORA**: MCP poslužitelji koji implementiraju autorizaciju **MORAJU** provjeravati SVE dolazne zahtjeve
>  
> **NE SMIJEĆE**: MCP poslužitelji **NE SMIJU** koristiti sesije za autentifikaciju
>
> **MORA**: MCP proxy poslužitelji koji koriste statički ID klijenta treće strane **MORAJU**
> dobiti suglasnost za svakog MCP klijenta prije prosljeđivanja autorizacije

---

## 1. **Sigurnost tokena i autentifikacija**

**Kontrole autentifikacije i autorizacije:**
   - **Temeljita revizija autorizacije**: Provedite sveobuhvatne revizije logike autorizacije MCP poslužitelja kako biste osigurali da samo namjenski korisnici i klijenti imaju pristup resursima
   - **Integracija vanjskog pružatelja identiteta**: Koristite etablirane pružatelje identiteta poput Microsoft Entra ID umjesto implementacije vlastite autentifikacije
   - **Validacija publike tokena**: Uvijek provjerite jesu li tokeni izričito izdani za vaš MCP poslužitelj - nikada ne prihvaćajte tokene iz višeg sloja
   - **Ispravan životni ciklus tokena**: Implementirajte sigurnu rotaciju tokena, politike isteka i spriječite napade ponovne upotrebe tokena

**Zaštićeno pohranjivanje tokena:**
   - Koristite Azure Key Vault ili slična sigurna spremišta vjerodajnica za sve tajne
   - Implementirajte enkripciju tokena u mirovanju i tijekom prijenosa
   - Redovito rotirajte vjerodajnice i nadgledajte neuobičajeni pristup

## 2. **Sigurnost upravljanja stanjem i prijenosa**

**Sigurne prakse upravljanja stanjem aplikacije:**

- **Neprozirni upravljači stanja**: Koristite sigurne, nedeterminističke upravljače za
   stanje aplikacije koje se proteže preko zahtjeva
- **Povezanost s korisnikom**: Vežite upravljače na strani poslužitelja uz potvrđenog
   korisnika i odbacujte ponovnu uporabu među korisnicima
- **Upravljanje životnim ciklusom**: Uvijek istek i opoziv upravljača kako biste ograničili ranjivost
   u vremenskim intervalima
- **Autorizacija po zahtjevu**: Nikada nemojte tretirati upravljač stanja kao autentifikaciju;
   autorizirajte svaki zahtjev koji ga predstavlja

**Sigurnost sloja prijenosa:**

- Za produkciju zahtijevajte HTTPS za udaljene HTTP prijenose
- Koristite izolaciju procesa i vjerodajnice okruženja za lokalne stdio poslužitelje
- Konfigurirajte moderan TLS s ispravnom rotacijom i validacijom certifikata

## 3. **Zaštita od prijetnji specifičnih za AI** 🤖

**Obrana od ubrizgavanja upita:**
   - **Microsoft Prompt Shields**: Primijenite AI Prompt Shields za naprednu detekciju i filtriranje zlonamjernih uputa
   - **Sanitizacija unosa**: Validirajte i pročistite sve unose da spriječite napade ubrizgavanja i probleme zbunjenog zamjenika
   - **Granice sadržaja**: Koristite sustave razdjelnika i označavanja podataka za razlikovanje pouzdanih uputa i vanjskog sadržaja

**Prevencija trovanja alata:**
   - **Validacija metapodataka alata**: Provedite provjere integriteta definicija alata i pratite neočekivane promjene
   - **Dinamičko nadgledanje alata**: Nadgledajte ponašanje u radu i postavite upozorenja za neočekivane obrasce izvršenja
   - **Radni tokovi odobrenja**: Zahtijevajte izričita korisnička odobrenja za izmjene alata i promjene mogućnosti

## 4. **Kontrola pristupa i dozvole**

**Načelo najmanjeg privilegija:**
   - Dodijelite MCP poslužiteljima samo minimalne potrebne dozvole za planiranu funkcionalnost
   - Implementirajte kontrolu pristupa temeljenu na ulogama (RBAC) s finim razinama dozvola
   - Redovito pregledavajte dozvole i kontinuirano nadgledajte povećanje privilegija

**Kontrole dozvola tijekom izvršenja:**
   - Primijenite ograničenja resursa kako biste spriječili napade iscrpljivanja resursa
   - Koristite izolaciju kontejnera za okruženja izvršenja alata  
   - Implementirajte pristup po potrebi za administrativne funkcije

## 5. **Sigurnost i nadzor sadržaja**

**Implementacija sigurnosti sadržaja:**
   - **Integracija Azure Content Safety**: Koristite Azure Content Safety za otkrivanje štetnog sadržaja, pokušaja jailbreak i kršenja pravila
   - **Analiza ponašanja**: Implementirajte nadzor ponašanja u radu za otkrivanje anomalija u radu MCP poslužitelja i alata
   - **Sveobuhvatno bilježenje**: Zabilježite sve pokušaje autentifikacije, pozive alata i sigurnosne događaje sa sigurnim i nepromjenjivim pohranama

**Kontinuirani nadzor:**
   - Upozorenja u stvarnom vremenu za sumnjive obrasce i pokušaje neovlaštenog pristupa  
   - Integracija sa SIEM sustavima za centralizirano upravljanje sigurnosnim događajima
   - Redovite sigurnosne revizije i penetracijski testovi MCP implementacija

## 6. **Sigurnost lanca opskrbe**

**Verifikacija komponenti:**
   - **Skeniranje ovisnosti**: Koristite automatizirano skeniranje ranjivosti za sve softverske ovisnosti i AI komponente
   - **Validacija porijekla**: Provjerite podrijetlo, licenciranje i integritet modela, izvora podataka i vanjskih servisa
   - **Potpisani paketi**: Koristite kriptografski potpisane pakete i provjeravajte potpise prije uvođenja

**Sigurni razvojni proces:**
   - **GitHub Advanced Security**: Implementirajte skeniranje tajni, analizu ovisnosti i statičku analizu CodeQL
   - **CI/CD sigurnost**: Integrirajte sigurnosne validacije kroz automatizirane procese implementacije
   - **Integritet artefakata**: Implementirajte kriptografsku verifikaciju za uvezene artefakte i konfiguracije

## 7. **Sigurnost OAuth-a i prevencija zbunjenog zamjenika**

**Implementacija OAuth 2.1:**
   - **Implementacija PKCE**: Koristite Proof Key for Code Exchange (PKCE) za sve autorizacijske zahtjeve
    - **Registracija klijenata**: Prednost dajte dokumentima o metapodacima ID klijenta ili
       prethodnoj registraciji; dinamička registracija klijenta u opadanju smije se koristiti samo kao
       rezervna kompatibilnost
    - **Izričita suglasnost**: MCP proxy serverti koji koriste statički ID klijenta treće strane moraju
       dobiti suglasnost za svakog MCP klijenta prije prosljeđivanja autorizacije
   - **Validacija URI-a preusmjeravanja**: Implementirajte strogu validaciju URI-ova preusmjeravanja i identifikatora klijenata

**Sigurnost proxy servera:**
   - Spriječite zaobilaženje autorizacije iskorištavanjem statičkog ID klijenta
   - Implementirajte pravilne radne tokove suglasnosti za pristup API-ju treće strane
   - Nadgledajte krađu autorizacijskog koda i neovlašteni pristup API-ju

## 8. **Odgovor na incidente i oporavak**

**Sposobnosti brzog odgovora:**
   - **Automatizirani odgovor**: Implementirajte automatizirane sustave za rotaciju vjerodajnica i zadržavanje prijetnji
   - **Postupci vraćanja**: Mogućnost brzog povratka na poznate dobre konfiguracije i komponente
   - **Forenzičke sposobnosti**: Detaljni auditni tragovi i bilježenje za istragu incidenata

**Komunikacija i koordinacija:**
   - Jasni postupci eskalacije za sigurnosne incidente
   - Integracija s organizacijskim timovima za odgovor na incidente
   - Redovite simulacije sigurnosnih incidenata i vježbe za stolom

## 9. **Usklađenost i upravljanje**

**Regulatorna usklađenost:**
   - Osigurajte da MCP implementacije zadovoljavaju industrijske zahtjeve (GDPR, HIPAA, SOC 2)
   - Implementirajte klasifikaciju podataka i kontrole privatnosti za obradu AI podataka
   - Održavajte sveobuhvatnu dokumentaciju za reviziju usklađenosti

**Upravljanje promjenama:**
   - Formalni sigurnosni procesi za sve izmjene MCP sustava
   - Kontrola verzija i radni tokovi odobrenja za promjene konfiguracije
   - Redovite procjene usklađenosti i analiza praznina

## 10. **Napredne sigurnosne kontrole**

**Zero Trust arhitektura:**
   - **Nikad ne vjeruj, uvijek provjeri**: Kontinuirana provjera korisnika, uređaja i veza
   - **Mikrosegmentacija**: Granularne mrežne kontrole koje izoliraju pojedine MCP komponente
   - **Uvjetni pristup**: Kontrole pristupa temeljene na riziku koje se prilagođavaju trenutnom kontekstu i ponašanju

**Zaštita aplikacije u radu:**
   - **Runtime Application Self-Protection (RASP)**: Primijenite RASP tehnike za detekciju prijetnji u stvarnom vremenu
   - **Praćenje performansi aplikacije**: Nadgledajte anomalije u izvedbi koje mogu ukazivati na napade
   - **Dinamičke sigurnosne politike**: Implementirajte sigurnosne politike koje se prilagođavaju na temelju trenutnog pejzaža prijetnji

## 11. **Integracija Microsoft sigurnosnog ekosustava**

**Sveobuhvatna Microsoft sigurnost:**
   - **Microsoft Defender for Cloud**: Upravljanje sigurnosnim stanjem u oblaku za MCP radna opterećenja
   - **Azure Sentinel**: Izvorni SIEM i SOAR za naprednu detekciju prijetnji
   - **Microsoft Purview**: Upravljanje podacima i usklađenost za AI radne tokove i izvore podataka

**Upravljanje identitetima i pristupom:**
   - **Microsoft Entra ID**: Upravljanje identitetima za poduzeća s politikama uvjetnog pristupa
   - **Privileged Identity Management (PIM)**: Pristup po potrebi i radni tokovi odobrenja za administrativne funkcije
   - **Zaštita identiteta**: Kontrola pristupa temeljena na riziku i automatizirani odgovor na prijetnje

## 12. **Kontinuirani razvoj sigurnosti**

**Praćenje novosti:**
   - **Praćenje specifikacija**: Redoviti pregled ažuriranja MCP specifikacija i promjena sigurnosnih smjernica
   - **Obavještavanje o prijetnjama**: Integracija AI-specifičnih izvora prijetnji i indikatora kompromisa
   - **Angažman sigurnosne zajednice**: Aktivno sudjelovanje u MCP sigurnosnoj zajednici i programima prijave ranjivosti

**Prilagodljiva sigurnost:**
   - **Sigurnost temeljena na strojnome učenju**: Koristite ML za detekciju anomalija i prepoznavanje novih obrazaca napada
   - **Prediktivna sigurnosna analitika**: Implementirajte modele za proaktivno prepoznavanje prijetnji
   - **Automatizacija sigurnosti**: Automatizirani sigurnosni update-i temeljeni na obavijestima o prijetnjama i promjenama specifikacija

---

## **Kritični sigurnosni resursi**

### **Službena MCP dokumentacija**
- [MCP specifikacija (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Najbolje sigurnosne prakse](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP specifikacija autorizacije](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP sigurnosni resursi**
- [OWASP MCP Azure sigurnosni vodič](https://microsoft.github.io/mcp-azure-security-guide/) - Sveobuhvatni OWASP MCP Top 10 s implementacijom za Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Službeni OWASP MCP sigurnosni rizici
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktična sigurnosna obuka za MCP na Azureu

### **Microsoft sigurnosna rješenja**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID sigurnost](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Sigurnosni standardi**
- [OAuth 2.0 Najbolje sigurnosne prakse (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 za velike jezične modele](https://genai.owasp.org/)
- [NIST AI okvir za upravljanje rizicima](https://www.nist.gov/itl/ai-risk-management-framework)

### **Vodiči za implementaciju**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID s MCP poslužiteljima](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Sigurnosna obavijest:** Prakse sigurnosti MCP brzo se razvijaju. Uvijek provjerite
> najnoviju [MCP specifikaciju](https://modelcontextprotocol.io/specification/2026-07-28/)
> i [službenu sigurnosnu dokumentaciju](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> prije implementacije.

## Što dalje

- Pročitajte: [MCP sigurnosne kontrole](./mcp-security-controls.md)
- Vratite se na: [Pregled sigurnosnog modula](./README.md)
- Nastavite na: [Modul 3: Početak](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->