# Najbolje sigurnosne prakse za MCP - ažuriranje za rujan 2026.

Ovaj sveobuhvatni vodič prikazuje ključne sigurnosne najbolje prakse za
implementaciju Model Context Protocol (MCP) sustava temeljenih na
**MCP specifikaciji 2026-07-28** i trenutačnim industrijskim standardima. Ove
prakse adresiraju tradicionalne sigurnosne prijetnje kao i specifične prijetnje umjetne inteligencije
jedinstvene za MCP implementacije.

## Kritični sigurnosni zahtjevi

### Obavezne sigurnosne kontrole (ZAHTJEVI KOJI SE MORAJU ISPUNITI)

1. **Validacija tokena**: MCP serveri **NE SMIJU** prihvaćati nikakve tokene koji nisu izričito izdani za sam MCP server
2. **Provjera autorizacije**: MCP serveri koji implementiraju autorizaciju **MORAJU** provjeriti SVE dolazne zahtjeve i **NE SMIJU** koristiti sesije za autentifikaciju  
3. **Suglasnost korisnika**: MCP proxy serveri koji koriste statične ID-je klijenata trećih strana **MORAJU** dobiti izričitu suglasnost svakog MCP klijenta prije prosljeđivanja autorizacijskog tijeka
4. **Sigurnost upravljačke oznake stanja**: MCP serveri **NE SMIJU** tretirati posjedovanje
	upravljačke oznake stanja aplikacije kao autentifikaciju i **MORAJU** autorizirati svaki
	zahtjev koji koristi takvu oznaku

## Temeljne sigurnosne prakse

### 1. Validacija i sanitacija unosa
- **Sveobuhvatna validacija unosa**: Validirati i čistiti sve unose da bi se spriječili napadi ubrizgavanja, problemi zbunjenog pomagača i ranjivosti ubrizgavanja naredbi
- **Nametanje šeme parametara**: Implementirati strogu JSON šemu za validaciju svih parametara alata i API unosa
- **Filtriranje sadržaja**: Koristiti Microsoft Prompt Shields i Azure Content Safety za filtriranje malicioznog sadržaja u upitima i odgovorima
- **Sanitacija izlaza**: Validirati i čistiti sve izlaze modela prije prikaza korisnicima ili daljnjim sustavima

### 2. Izvrsnost u autentifikaciji i autorizaciji  
- **Vanjski pružatelji identiteta**: Prebaciti autentifikaciju na etablirane pružatelje identiteta (Microsoft Entra ID, OAuth 2.1 pružatelji), umjesto implementiranja prilagođene autentifikacije
- **Registracija klijenata**: Preferirati dokumente metapodataka ID klijenta ili pred-registraciju; koristiti zastarjelu dinamičku registraciju klijenata samo radi kompatibilnosti
- **Fino usklađena dopuštenja**: Implementirati granularna dopuštenja specifična za alat prema načelu najmanjih privilegija
- **Upravljanje životnim ciklusom tokena**: Koristiti kratkotrajne pristupne tokene s sigurnom rotacijom i ispravnom validacijom аудиторија
- **Višefaktorska autentifikacija**: Zahtijevati MFA za sav administrativni pristup i osjetljive operacije

### 3. Sigurni komunikacijski protokoli
- **Sigurnost transportnog sloja**: Koristiti HTTPS s ispravnom validacijom certifikata
	za udaljene HTTP MCP komunikacije; koristiti izolaciju procesa i vjerodajnice okruženja
	za lokalne stdio servere
- **End-to-End enkripcija**: Implementirati dodatne slojeve enkripcije za vrlo osjetljive podatke u prijenosu i mirovanju
- **Upravljanje certifikatima**: Održavati ispravan životni ciklus certifikata s automatiziranim procesima obnove
- **Nametanje verzije protokola**: Koristiti MCP `2026-07-28`, uključiti potrebne
	verzijske metapodatke pri svakom zahtjevu i odbiti nepodržane verzije

### 4. Napredno ograničavanje brzine i zaštita resursa
- **Višeslojno ograničavanje brzine**: Implementirati ograničenje brzine po korisniku, vjerodajnici,
  operaciji, alatu i resursu kako bi se spriječila zloupotreba
- **Adaptivno ograničavanje brzine**: Koristiti ograničavanje brzine temeljeno na strojnome učenju koje se prilagođava obrascima korištenja i pokazateljima prijetnji
- **Upravljanje kvotama resursa**: Postaviti odgovarajuće limitacije za računalne resurse, korištenje memorije i vrijeme izvršavanja
- **Zaštita od DDoS napada**: Implementirati sveobuhvatne sustave zaštite od DDoS-a i analize prometa

### 5. Sveobuhvatno evidentiranje i nadzor
- **Strukturirano auditiranje**: Implementirati detaljno, pretraživo evidentiranje svih MCP operacija, izvršenja alata i sigurnosnih događaja
- **Nadzor sigurnosti u stvarnom vremenu**: Postaviti SIEM sustave s AI-pokretanom detekcijom anomalija za MCP opterećenja
- **Evidentiranje u skladu s privatnošću**: Evidentirati sigurnosne događaje poštujući zahtjeve i propise o privatnosti podataka
- **Integracija odgovora na incidente**: Povezati sustave evidentiranja sa automatiziranim tijekovima odgovora na incidente

### 6. Poboljšane prakse sigurnog pohranjivanja
- **Hardverski sigurnosni moduli**: Koristiti pohranu ključeva podržanu HSM-om (Azure Key Vault, AWS CloudHSM) za kritične kriptografske operacije
- **Upravljanje ključevima za enkripciju**: Implementirati odgovarajuću rotaciju, segregaciju i kontrole pristupa za enkripcijske ključeve
- **Upravljanje tajnama**: Pohraniti sve API ključeve, tokene i vjerodajnice u posvećene sustave za upravljanje tajnama
- **Klasifikacija podataka**: Klasificirati podatke prema razinama osjetljivosti i primijeniti odgovarajuće mjere zaštite

### 7. Napredno upravljanje tokenima
- **Sprečavanje prosljeđivanja tokena**: Izričito zabraniti obrasce prosljeđivanja tokena koji zaobilaze sigurnosne kontrole
- **Validacija publike**: Uvijek provjeriti podudarnost publike tokena s identitetom MCP servera za koji je namijenjen
- **Autorizacija temeljena na tvrdnjama**: Implementirati fino usklađenu autorizaciju na temelju tvrdnji tokena i atributa korisnika
- **Povezivanje tokena**: Validirati da tokeni ciljaju namijenjeni MCP resurs i
	vežu upravljačke oznake stanja aplikacije na strani servera uz autentificirani subjekt

### 8. Sigurno stanje aplikacije

- **Kriptografske upravljačke oznake stanja**: Generirati neprozirne, nedeterminističke oznake
	za stanje koje obuhvaća više zahtjeva
- **Povezivanje s korisnikom**: Svaku oznaku s vezati na strani servera uz autentificirani
	subjekt; ne vjerovati korisničkom ID-ju dobivenom od klijenta
- **Kontrole životnog ciklusa**: Istjecati i opozvati oznake te definirati načine na koje pozivatelji
	oporavljaju zastarjelo stanje
- **Autorizacija po zahtjevu**: Ponovno provjeriti autorizaciju kad god se prikaže oznaka;
	oznaka je naziv, a ne vjerodajnica

### 9. Specifične sigurnosne kontrole za umjetnu inteligenciju
- **Obrana od ubrizgavanja upita**: Primijeniti Microsoft Prompt Shields s osvjetljavanjem, delimiterima i tehnikama označavanja podataka
- **Sprečavanje trovanja alata**: Validirati metapodatke alata, nadzirati dinamičke promjene i provjeravati integritet alata
- **Validacija izlaza modela**: Skenirati izlaze modela na potencijalno curenje podataka, štetni sadržaj ili kršenja sigurnosnih pravila
- **Zaštita kontekstnog prozora**: Implementirati kontrole za sprječavanje trovanja i manipulacije kontekstnim prozorom

### 10. Sigurnost izvršenja alata
- **Izolacija izvršenja**: Pokretati izvršenja alata u kontejneriziranim, izoliranim okruženjima s ograničenjima resursa
- **Odvajanje privilegija**: Izvršavati alate s minimalno potrebnim privilegijama i odvojenim servisnim računima
- **Mrežna izolacija**: Implementirati segmentaciju mreže za okruženja izvršenja alata
- **Nadzor izvršenja**: Nadzirati izvršenje alata radi anomalnog ponašanja, korištenja resursa i kršenja sigurnosti

### 11. Kontinuirana sigurnosna validacija
- **Automatizirano sigurnosno testiranje**: Integrirati sigurnosno testiranje u CI/CD procese korištenjem alata poput GitHub Advanced Security
- **Upravljanje ranjivostima**: Redovito skenirati sve ovisnosti, uključujući AI modele i vanjske usluge
- **Penetracijsko testiranje**: Provoditi redovite sigurnosne procjene usmjerene na MCP implementacije
- **Pregled sigurnosnog koda**: Provoditi obavezne sigurnosne preglede za sve promjene koda vezanog uz MCP

### 12. Sigurnost opskrbnog lanca za umjetnu inteligenciju
- **Verifikacija komponenti**: Provjeravati podrijetlo, integritet i sigurnost svih AI komponenti (modeli, ubacivanja, API-ji)
- **Upravljanje ovisnostima**: Održavati aktualni inventar svih softverskih i AI ovisnosti s praćenjem ranjivosti
- **Pouzdani repozitoriji**: Koristiti provjerene, pouzdane izvore za sve AI modele, biblioteke i alate
- **Nadzor opskrbnog lanca**: Kontinuirano nadzirati kompromitacije u pružateljima AI usluga i repozitorijima modela

## Napredni sigurnosni obrasci

### Arhitektura nulte povjerenja za MCP
- **Nikad ne vjeruj, uvijek provjeri**: Implementirati kontinuiranu provjeru za sve MCP sudionike
- **Mikrosegmentacija**: Izolirati MCP komponente uz granularne mrežne i identitetske kontrole
- **Uvjetni pristup**: Implementirati kontrolu pristupa temeljenu na riziku koja se prilagođava kontekstu i ponašanju
- **Kontinuirana procjena rizika**: Dinamički vrednovati sigurnosni položaj temeljem trenutačnih pokazatelja prijetnji

### Implementacija AI koja štiti privatnost
- **Minimizacija podataka**: Izlagati samo minimalno potrebne podatke za svaku MCP operaciju
- **Diferencijalna privatnost**: Implementirati tehnike očuvanja privatnosti pri obradi osjetljivih podataka
- **Homomorfna enkripcija**: Koristiti napredne enkripcijske tehnike za sigurno izvođenje računa nad šifriranim podacima
- **Federirano učenje**: Implementirati distribuirane pristupe učenju koji očuvaju lokalitet i privatnost podataka

### Odgovor na incidente za AI sustave
- **Postupci za incidente specifične za AI**: Razviti procedure odgovora na incidente prilagođene prijetnjama specifičnim za AI i MCP
- **Automatizirani odgovor**: Implementirati automatizirano zadržavanje i sanaciju za uobičajene sigurnosne incidente AI-a  
- **Forenzičke sposobnosti**: Održavati spremnost za forenzičku analizu kompromisa AI sustava i proboja podataka
- **Postupci oporavka**: Uspostaviti postupke za oporavak od trovanja AI modela, napada ubrizgavanjem upita i kompromisa usluga

## Resursi i standardi za implementaciju

### 🏔️ Praktična sigurnosna edukacija
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Sveobuhvatna praktična radionica za zaštitu MCP servera u Azureu
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Referentna arhitektura i upute za implementaciju OWASP MCP Top 10

### Službena MCP dokumentacija
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Trenutačna MCP specifikacija protokola
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Službene sigurnosne smjernice
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - Obrasci autorizacije preko HTTP-a
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Zahtjevi za prijenos podataka

### Microsoft sigurnosna rješenja
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Napredna zaštita od ubrizgavanja upita
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Sveobuhvatno filtriranje AI sadržaja
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Upravljanje identitetom i pristupom za poduzeća
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Sigurno upravljanje tajnama i vjerodajnicama
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Skeniranje sigurnosti lanca opskrbe i koda

### Sigurnosni standardi i okviri
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Trenutačne sigurnosne smjernice za OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Rizici sigurnosti web aplikacija
- [OWASP Top 10 za LLM-ove](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Sigurnosni rizici specifični za umjetnu inteligenciju
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Sveobuhvatan okvir upravljanja rizicima za AI
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Sustavi upravljanja informacijskom sigurnošću

### Vodiči za implementaciju i tutorijali
- [Azure API Management kao MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Obrasci autentifikacije za poduzeća
- [Microsoft Entra ID s MCP serverima](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integracija pružatelja identiteta
- [Implementacija sigurne pohrane tokena](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Najbolje prakse upravljanja tokenima
- [End-to-End enkripcija za AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Napredni obrasci enkripcije

### Napredni sigurnosni resursi
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Prakse sigurnog razvoja
- [Vodič za AI Red Team](https://learn.microsoft.com/security/ai-red-team/) - AI-specifično sigurnosno testiranje
- [Modeliranje prijetnji za AI sustave](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologija modeliranja prijetnji za AI
- [Inženjerstvo privatnosti za AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Tehnike očuvanja privatnosti u AI-u

### Usklađenost i upravljanje
- [Usklađenost s GDPR za AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Usklađenost privatnosti u AI sustavima
- [Okvir upravljanja AI](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Odgovorna implementacija AI
- [SOC 2 za AI usluge](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Sigurnosne kontrole za pružatelje AI usluga
- [Usklađenost s HIPAA za AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Zahtjevi za usklađenost zdravstva i AI-a

### DevSecOps i automatizacija
- [DevSecOps pipeline za AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Sigurni ciklusi razvoja AI
- [Automatizirano sigurnosno testiranje](https://learn.microsoft.com/security/engineering/devsecops) - Kontinuirana sigurnosna validacija
- [Sigurnost infrastrukture kao koda](https://learn.microsoft.com/security/engineering/infrastructure-security) - Sigurna implementacija infrastrukture
- [Sigurnost kontejnera za AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Sigurnost kontejnerizacije AI opterećenja

### Nadzor i odgovor na incidente  
- [Azure Monitor za AI opterećenja](https://learn.microsoft.com/azure/azure-monitor/overview) - Sveobuhvatna rješenja za nadzor
- [Odgovor na sigurnosne incidente AI](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Postupci za incidente specifične za AI
- [SIEM za AI sustave](https://learn.microsoft.com/azure/sentinel/overview) - Upravljanje informacijama i događajima sigurnosti

- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Izvori obavještajnih podataka o prijetnjama za AI

## 🔄 Kontinuirano unapređenje

### Budite u toku s razvijajućim standardima
- **Ažuriranja MCP specifikacija**: Pratite službene promjene MCP specifikacija i sigurnosne savjete
- **Obavještajni podaci o prijetnjama**: Pretplatite se na sigurnosne feedove prijetnji AI i baze podataka ranjivosti  
- **Sudjelovanje zajednice**: Sudjelujte u MCP sigurnosnim diskusijama i radnim skupinama zajednice
- **Redovita procjena**: Provedite tromjesečne procjene sigurnosnog stanja i prema tome ažurirajte prakse

### Doprinoseći sigurnosti MCP-a
- **Sigurnosna istraživanja**: Doprinesite MCP sigurnosnim istraživanjima i programima otkrivanja ranjivosti
- **Dijeljenje najboljih praksi**: Dijelite sigurnosne implementacije i naučene lekcije sa zajednicom
- **Razvoj standarda**: Sudjelujte u razvoju MCP specifikacije i stvaranju sigurnosnih standarda
- **Razvoj alata**: Razvijajte i dijelite sigurnosne alate i knjižnice za MCP ekosustav

---

*Ovaj dokument odražava najbolje sigurnosne prakse MCP-a od 9. rujna 2026.,
na temelju MCP specifikacije `2026-07-28`. Sigurnosne prakse trebaju se redovito
pregledavati kako se protokol i prijeteći krajolik razvijaju.*

## Što slijedi

- Pročitajte: [Najbolje sigurnosne prakse MCP-a](./mcp-security-best-practices.md)
- Vratite se na: [Pregled sigurnosnog modula](./README.md)
- Nastavite na: [Modul 3: Početak rada](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->