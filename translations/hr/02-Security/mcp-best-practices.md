# MCP Sigurnosne Najbolje Prakse 2025

Ovaj sveobuhvatni vodič opisuje ključne sigurnosne najbolje prakse za implementaciju Model Context Protocol (MCP) sustava temeljenih na najnovijoj **MCP Specifikaciji 2025-11-25** i trenutnim industrijskim standardima. Ove prakse pokrivaju i tradicionalne sigurnosne izazove i AI-specifične prijetnje jedinstvene za MCP implementacije.

## Kritični Sigurnosni Zahtjevi

### Obavezne Sigurnosne Kontrole (MORA Zahtjevi)

1. **Validacija Tokena**: MCP serveri **NE SMIJU** prihvaćati bilo kakve tokene koji nisu izričito izdani za sam MCP server
2. **Provjera Autorizacije**: MCP serveri koji implementiraju autorizaciju **MORAJU** provjeriti SVE dolazne zahtjeve i **NE SMIJU** koristiti sesije za autentikaciju  
3. **Korisnički Pristanak**: MCP proxy serveri koji koriste statične ID-jeve klijenata **MORAJU** dobiti izričit korisnički pristanak za svakog dinamički registriranog klijenta
4. **Sigurni ID-jevi Sesija**: MCP serveri **MORAJU** koristiti kriptografski sigurne, nedeterminističke ID-jeve sesija generirane sigurnim generatorima slučajnih brojeva

## Osnovne Sigurnosne Prakse

### 1. Validacija i Sanitizacija Ulaza
- **Sveobuhvatna Validacija Ulaza**: Validirajte i sanitizirajte sve ulaze kako biste spriječili injekcijske napade, probleme zbunjenog zastupnika i ranjivosti prompt injekcije
- **Provedba Sheme Parametara**: Implementirajte strogu JSON shemu validaciju za sve parametre alata i API ulaze
- **Filtriranje Sadržaja**: Koristite Microsoft Prompt Shields i Azure Content Safety za filtriranje zlonamjernog sadržaja u promptovima i odgovorima
- **Sanitizacija Izlaza**: Validirajte i sanitizirajte sve izlaze modela prije prikaza korisnicima ili downstream sustavima

### 2. Izvrsnost u Autentikaciji i Autorizaciji  
- **Vanjski Provajderi Identiteta**: Delegirajte autentikaciju etabliranim provajderima identiteta (Microsoft Entra ID, OAuth 2.1 provajderi) umjesto implementacije vlastite autentikacije
- **Detaljne Dozvole**: Implementirajte granularne, alat-specifične dozvole slijedeći princip najmanjih privilegija
- **Upravljanje Životnim Ciklusom Tokena**: Koristite kratkotrajne pristupne tokene sa sigurnom rotacijom i pravilnom validacijom publike
- **Višefaktorska Autentikacija**: Zahtijevajte MFA za sav administrativni pristup i osjetljive operacije

### 3. Sigurni Komunikacijski Protokoli
- **Transport Layer Security**: Koristite HTTPS/TLS 1.3 za svu MCP komunikaciju s pravilnom validacijom certifikata
- **End-to-End Enkripcija**: Implementirajte dodatne slojeve enkripcije za visoko osjetljive podatke u prijenosu i mirovanju
- **Upravljanje Certifikatima**: Održavajte pravilno upravljanje životnim ciklusom certifikata s automatiziranim procesima obnove
- **Provedba Verzije Protokola**: Koristite trenutnu verziju MCP protokola (2025-11-25) s pravilnim pregovorom verzije.

### 4. Napredno Ograničavanje Brzine i Zaštita Resursa
- **Višeslojno Ograničavanje Brzine**: Implementirajte ograničavanje brzine na razini korisnika, sesije, alata i resursa kako biste spriječili zloupotrebu
- **Adaptivno Ograničavanje Brzine**: Koristite ograničavanje brzine temeljeno na strojnome učenju koje se prilagođava obrascima korištenja i pokazateljima prijetnji
- **Upravljanje Kvotama Resursa**: Postavite odgovarajuće limite za računalne resurse, korištenje memorije i vrijeme izvršavanja
- **Zaštita od DDoS Napada**: Implementirajte sveobuhvatnu zaštitu od DDoS napada i sustave za analizu prometa

### 5. Sveobuhvatno Logiranje i Praćenje
- **Strukturirano Audit Logiranje**: Implementirajte detaljne, pretražive zapise za sve MCP operacije, izvršenja alata i sigurnosne događaje
- **Praćenje Sigurnosti u Stvarnom Vremenu**: Postavite SIEM sustave s AI-pokretanom detekcijom anomalija za MCP radna opterećenja
- **Logiranje u skladu s Privatnošću**: Zabilježite sigurnosne događaje poštujući zahtjeve i propise o privatnosti podataka
- **Integracija Odgovora na Incidente**: Povežite sustave logiranja s automatiziranim tijekovima rada za odgovor na incidente

### 6. Poboljšane Prakse Sigurnog Pohranjivanja
- **Hardverski Sigurnosni Moduli**: Koristite pohranu ključeva podržanu HSM-om (Azure Key Vault, AWS CloudHSM) za kritične kriptografske operacije
- **Upravljanje Ključevima za Enkripciju**: Implementirajte pravilnu rotaciju ključeva, segregaciju i kontrole pristupa za ključeve enkripcije
- **Upravljanje Tajnama**: Pohranite sve API ključeve, tokene i vjerodajnice u namjenske sustave za upravljanje tajnama
- **Klasifikacija Podataka**: Klasificirajte podatke prema razinama osjetljivosti i primijenite odgovarajuće mjere zaštite

### 7. Napredno Upravljanje Tokenima
- **Sprečavanje Prosljeđivanja Tokena**: Izričito zabranite obrasce prosljeđivanja tokena koji zaobilaze sigurnosne kontrole
- **Validacija Publike**: Uvijek provjerite da tvrdnje o publici tokena odgovaraju identitetu namijenjenog MCP servera
- **Autorizacija Temeljena na Tvrdnjama**: Implementirajte detaljnu autorizaciju temeljenu na tvrdnjama tokena i atributima korisnika
- **Povezivanje Tokena**: Povežite tokene s određenim sesijama, korisnicima ili uređajima gdje je prikladno

### 8. Sigurno Upravljanje Sesijama
- **Kriptografski ID-jevi Sesija**: Generirajte ID-jeve sesija koristeći kriptografski sigurne generatore slučajnih brojeva (nepredvidive sekvence)
- **Povezivanje s Korisnikom**: Povežite ID-jeve sesija s korisnički specifičnim informacijama koristeći sigurne formate poput `<user_id>:<session_id>`
- **Kontrole Životnog Ciklusa Sesije**: Implementirajte pravilno istekanje, rotaciju i poništavanje sesija
- **Sigurnosni Zaglavlja Sesije**: Koristite odgovarajuća HTTP sigurnosna zaglavlja za zaštitu sesija

### 9. AI-specifične Sigurnosne Kontrole
- **Obrana od Prompt Injekcije**: Postavite Microsoft Prompt Shields s tehnikama spotlightinga, delimitera i označavanja podataka
- **Prevencija Trovanja Alata**: Validirajte metapodatke alata, pratite dinamičke promjene i provjeravajte integritet alata
- **Validacija Izlaza Modela**: Skenirajte izlaze modela na potencijalno curenje podataka, štetni sadržaj ili kršenja sigurnosnih politika
- **Zaštita Kontekstnog Prozora**: Implementirajte kontrole za sprječavanje trovanja i manipulacije kontekstnim prozorom

### 10. Sigurnost Izvršenja Alata
- **Izvršenje u Sandboxu**: Izvršavajte alate u kontejneriziranim, izoliranim okruženjima s ograničenjima resursa
- **Razdvajanje Privilegija**: Izvršavajte alate s minimalnim potrebnim privilegijama i odvojenim servisnim računima
- **Mrežna Izolacija**: Implementirajte mrežnu segmentaciju za okruženja izvršenja alata
- **Praćenje Izvršenja**: Pratite izvršenje alata zbog anomalnog ponašanja, korištenja resursa i sigurnosnih kršenja

### 11. Kontinuirana Sigurnosna Validacija
- **Automatizirano Sigurnosno Testiranje**: Integrirajte sigurnosno testiranje u CI/CD pipelineove s alatima poput GitHub Advanced Security
- **Upravljanje Ranljivostima**: Redovito skenirajte sve ovisnosti, uključujući AI modele i vanjske usluge
- **Penetracijsko Testiranje**: Provodite redovite sigurnosne procjene posebno usmjerene na MCP implementacije
- **Sigurnosne Revizije Koda**: Implementirajte obavezne sigurnosne preglede za sve promjene koda vezane uz MCP

### 12. Sigurnost Opskrbnog Lanca za AI
- **Verifikacija Komponenti**: Provjerite podrijetlo, integritet i sigurnost svih AI komponenti (modeli, embeddings, API-ji)
- **Upravljanje Ovisnostima**: Održavajte ažurne inventare svih softverskih i AI ovisnosti s praćenjem ranjivosti
- **Pouzdani Repozitoriji**: Koristite verificirane, pouzdane izvore za sve AI modele, biblioteke i alate
- **Praćenje Opskrbnog Lanca**: Kontinuirano pratite moguće kompromite kod AI pružatelja usluga i repozitorija modela

## Napredni Sigurnosni Obrasci

### Zero Trust Arhitektura za MCP
- **Nikad Ne Vjeruj, Uvijek Provjeri**: Implementirajte kontinuiranu provjeru za sve MCP sudionike
- **Mikrosegmentacija**: Izolirajte MCP komponente s granularnim mrežnim i identitetskim kontrolama
- **Uvjetni Pristup**: Implementirajte kontrole pristupa temeljene na riziku koje se prilagođavaju kontekstu i ponašanju
- **Kontinuirana Procjena Rizika**: Dinamički procjenjujte sigurnosni položaj na temelju trenutnih pokazatelja prijetnji

### Implementacija AI koja Čuva Privatnost
- **Minimizacija Podataka**: Izlažite samo minimalno potrebne podatke za svaku MCP operaciju
- **Diferencijalna Privatnost**: Implementirajte tehnike očuvanja privatnosti za obradu osjetljivih podataka
- **Homomorfna Enkripcija**: Koristite napredne enkripcijske tehnike za sigurno računanje nad šifriranim podacima
- **Federativno Učenje**: Implementirajte distribuirane pristupe učenju koji čuvaju lokalitet i privatnost podataka

### Odgovor na Incidente za AI Sustave
- **AI-specifične Procedure za Incident**: Razvijte procedure odgovora na incidente prilagođene AI i MCP specifičnim prijetnjama
- **Automatizirani Odgovor**: Implementirajte automatizirano suzbijanje i sanaciju za uobičajene AI sigurnosne incidente  
- **Forenzičke Mogućnosti**: Održavajte forenzičku spremnost za kompromite AI sustava i curenja podataka
- **Postupci Oporavka**: Uspostavite postupke za oporavak od trovanja AI modela, napada prompt injekcije i kompromita usluga

## Resursi za Implementaciju i Standardi

### Službena MCP Dokumentacija
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Trenutna MCP specifikacija protokola
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Službene sigurnosne smjernice
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Obrasci autentikacije i autorizacije
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Zahtjevi za sigurnost transportnog sloja

### Microsoft Sigurnosna Rješenja
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Napredna zaštita od prompt injekcije
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Sveobuhvatno filtriranje AI sadržaja
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Upravljanje identitetom i pristupom za poduzeća
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Sigurno upravljanje tajnama i vjerodajnicama
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Skeniranje sigurnosti opskrbnog lanca i koda

### Sigurnosni Standardi i Okviri
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Trenutne sigurnosne smjernice za OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Rizici sigurnosti web aplikacija
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-specifični sigurnosni rizici
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Sveobuhvatno upravljanje rizicima AI
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Sustavi upravljanja informacijskom sigurnošću

### Vodiči za Implementaciju i Tutorijali
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Obrasci autentikacije za poduzeća
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integracija provajdera identiteta
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Najbolje prakse upravljanja tokenima
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Napredni obrasci enkripcije

### Napredni Sigurnosni Resursi
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Prakse sigurnog razvoja
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-specifično sigurnosno testiranje
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologija modeliranja prijetnji za AI
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Tehnike očuvanja privatnosti u AI

### Usklađenost i Upravljanje
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Usklađenost privatnosti u AI sustavima
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Odgovorna implementacija AI
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Sigurnosne kontrole za AI pružatelje usluga
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Zahtjevi usklađenosti za AI u zdravstvu

### DevSecOps i Automatizacija
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Sigurni AI razvojni pipelineovi
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Kontinuirana sigurnosna validacija
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Sigurna implementacija infrastrukture
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Sigurnost kontejnerizacije AI radnih opterećenja

### Praćenje i Odgovor na Incidente  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Sveobuhvatna rješenja za praćenje
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-specifične procedure za incidente
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Upravljanje sigurnosnim informacijama i događajima
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Izvori obavještajnih podataka o prijetnjama za AI

## 🔄 Kontinuirano Unapređenje

### Budite Uvijek Ažurni s Razvijajućim Standardima
- **Ažuriranja MCP Specifikacije**: Pratite službene promjene MCP specifikacije i sigurnosne obavijesti
- **Obavještajni Podaci o Prijetnjama**: Pretplatite se na feedove prijetnji AI sigurnosti i baze ranjivosti  
- **Sudjelovanje u Zajednici**: Sudjelujte u MCP sigurnosnim zajednicama i radnim skupinama
- **Redovite Procjene**: Provodite kvartalne procjene sigurnosnog položaja i ažurirajte prakse u skladu s tim

### Doprinos MCP Sigurnosti
- **Sigurnosna Istraživanja**: Doprinesite MCP sigurnosnim istraživanjima i programima otkrivanja ranjivosti
- **Dijeljenje Najboljih Praksi**: Dijelite sigurnosne implementacije i naučene lekcije sa zajednicom
- **Standardni razvoj**: Sudjelovanje u razvoju MCP specifikacija i stvaranju sigurnosnih standarda
- **Razvoj alata**: Razvijanje i dijeljenje sigurnosnih alata i biblioteka za MCP ekosustav

---

*Ovaj dokument odražava najbolje sigurnosne prakse MCP-a od 18. prosinca 2025., na temelju MCP specifikacije 2025-11-25. Sigurnosne prakse trebaju se redovito pregledavati i ažurirati kako se protokol i prijetnje budu razvijali.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->