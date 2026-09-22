# MCP saugumo gerosios praktikos – 2026 m. rugsėjo atnaujinimas

Ši išsami gidas aprašo svarbiausias saugumo gerąsias praktikas, skirtas
diegiant Model Context Protocol (MCP) sistemas, remiantis
**MCP specifikacija 2026-07-28** ir dabartinėmis pramonės standartais. Šios
praktikos sprendžia tiek tradicines saugumo problemas, tiek AI specifinius grėsmes,
būdingas MCP diegimams.

## Kritiniai saugumo reikalavimai

### Privalomi saugumo kontrolės (PRIVALOMA reikalavimai)

1. **Žetonų patikra**: MCP serveriai **NETURI** priimti jokių žetonų, kurie nebuvo aiškiai išduoti MCP serveriui pačiam
2. **Autorizacijos patikra**: MCP serveriai, įgyvendinantys autorizaciją, **PRIVALO** patikrinti VISUS gaunamus užklausimus ir **NETURI** naudoti sesijų autentifikacijai  
3. **Vartotojo sutikimas**: MCP tarpiniai serveriai, naudojantys statinius tretiesiems šalims priklausančius klientų ID, **PRIVALO** gauti aiškų sutikimą kiekvienam MCP klientui prieš perduodant autorizacijos srautą
4. **Valstybės valdiklio saugumas**: MCP serveriai **NETURI** traktuoti turėjimo aplikacijos valstybės valdiklio kaip autentifikacijos ir **PRIVALO** autorizuoti kiekvieną užklausimą, kuris jį naudoja



## Pagrindinės saugumo praktikos

### 1. Įvesties patikra ir valymas
- **Išsami įvesties patikra**: Tikrinkite ir išvalykite visas įvestis, kad išvengtumėte įpurškimo atakų, painiavos atstovo problemų ir užklausų įpurškimo pažeidžiamumų
- **Parametrų schemos laikymasis**: Įgyvendinkite griežtą JSON schemos patikrinimą visiems įrankių parametrams ir API įvestims
- **Turinio filtravimas**: Naudokite Microsoft Prompt Shields ir Azure Content Safety, kad filtruotumėte kenksmingą turinį užklausose ir atsakymuose
- **Išvesties valymas**: Patikrinkite ir išvalykite visus modelio išvestis prieš pateikdami vartotojams arba žemiau esantiems sistemoms

### 2. Autentifikacijos ir autorizacijos tobulinimas  
- **Išoriniai tapatybės tiekėjai**: Atiduokite autentifikaciją užtikrintiems tapatybės tiekėjams (Microsoft Entra ID, OAuth 2.1 tiekėjai), o ne įgyvendinkite pasirinktines autentifikacijas
- **Klientų registracija**: Pirmenybę teikite Kliento ID metaduomenų dokumentams arba išankstinei registracijai; naudokite pasenusią Dinaminę kliento registraciją tik suderinamumo tikslais
- **Smulkios granularumo teisės**: Įgyvendinkite griežtas, įrankiui specifines teises, vadovaudamiesi mažiausios privilegijos principu
- **Žetonų gyvavimo ciklo valdymas**: Naudokite trumpalaikius prieigos žetonus su saugiu sukimų ir tinkamu auditorijos patikrinimu
- **Daugiaveiksmė autentifikacija**: Reikalaukite MFA visam administraciniam prieigai ir jautrioms operacijoms

### 3. Saugūs komunikacijos protokolai
- **Perdavimo sluoksnio saugumas (TLS)**: Naudokite HTTPS su tinkama sertifikatų patikra nuotolinėms HTTP MCP komunikacijoms; naudokite proceso izoliaciją ir aplinkos kredencialus vietiniams stdio serveriams
 
 
- **Galinis šifravimas**: Įgyvendinkite papildomas šifravimo sluoksnius itin jautriems duomenims tranzite ir ramybės būsenoje
- **Sertifikatų valdymas**: Užtikrinkite tinkamą sertifikatų gyvavimo ciklo valdymą su automatizuotais atnaujinimo procesais
- **Protokolo versijos laikymasis**: Naudokite MCP `2026-07-28`, įtraukite privalomą versijos metaduomenį kiekviename užklausoje ir atminkite nepalaikomas versijas


### 4. Išplėstinis ribojimas pagal dažnį ir išteklių apsauga
- **Daugiasluoksnis dažnio ribojimas**: Įgyvendinkite dažnio ribojimą pagal vartotoją, kredencialą, operaciją, įrankį ir išteklius, kad būtų užkirstas kelias piktnaudžiavimui
  
- **Adaptacinis dažnio ribojimas**: Naudokite mašininio mokymosi pagrįstą dažnio ribojimą, kuris prisitaiko prie naudojimo modelių ir grėsmių indikatorių
- **Išteklių kvotų valdymas**: Nustatykite tinkamus apribojimus skaičiavimo ištekliams, atminčiai ir vykdymo laikui
- **DDoS apsauga**: Diegkite išsamią DDoS apsaugą ir srauto analizės sistemas

### 5. Išsamus žurnalavimas ir stebėsena
- **Struktūruotas audito žurnalavimas**: Įgyvendinkite detalius, paieškai pritaikytus žurnalus visoms MCP operacijoms, įrankių vykdymams ir saugumo įvykiams
- **Realiojo laiko saugumo stebėsena**: Diegkite SIEM sistemas su AI pagrįsta anomalijų aptikimu MCP darbo krūviams
- **Privatumo atitinkamas žurnalavimas**: Žurnaluokite saugumo įvykius, laikydamiesi duomenų privatumo reikalavimų ir reglamentų
- **Incidentų reagavimo integracija**: Sujunkite žurnalų sistemas su automatizuotais incidentų reagavimo srautais

### 6. Patobulintos saugios saugojimo praktikos
- **Aparatiniai saugumo moduliai**: Naudokite HSM pagrįstą raktų saugojimą (Azure Key Vault, AWS CloudHSM) kritinėms kriptografinėms operacijoms
- **Šifravimo raktų valdymas**: Įgyvendinkite tinkamą raktų sukimą, atskyrimą ir prieigos valdymą šifravimo raktams
- **Slapčių valdymas**: Saugojite visus API raktus, žetonus ir kredencialus skirtingose slapčių valdymo sistemose
- **Duomenų klasifikavimas**: Klasifikuokite duomenis pagal jautrumo lygius ir taikykite tinkamas apsaugos priemones

### 7. Išplėstinis žetonų valdymas
- **Žetonų perleidimo prevencija**: Aiškiai uždrauskite žetonų perleidimo schemas, kurios prasilenkia su saugumo kontrolėmis
- **Auditorijos tikrinimas**: Visada tikrinkite, kad žetonų auditorijos teiginiai atitiktų numatytą MCP serverio tapatybę
- **Autorizacija pagal teiginius**: Įgyvendinkite smulkią autorizaciją remiantis žetonų teiginiais ir vartotojų atributais
- **Žetonų siejimas**: Patikrinkite, kad žetonai yra skirti numatytiems MCP ištekliams ir
	pasirinkite aplikacijos valstybės valdiklius serverio pusėje prie autentifikuoto subjekto

### 8. Saugūs aplikacijos valstybės valdikliai

- **Kriptografiniai valstybės valdikliai**: Generuokite nepermatomus, nedeterministinius valdiklius
	valstybei, apimančiai užklausas
- **Vartotojui priskyrimas**: Priskirkite kiekvieną valdiklį serverio pusėje autentifikuotam
	subjektui; nepasitikėkite vartotojo ID, pateiktu klientui
- **Gyvavimo ciklo valdymas**: Pasibaigus ir atšaukus valdiklius, apibrėžkite, kaip kvietėjai
	atgauna pasenusią valstybę
- **Autorizacijos kiekvienam užklausimui**: Patikrinkite autorizaciją kiekvieną kartą, kai pateikiamas valdiklis; valdiklis yra vardas, ne kredencialas


### 9. AI specifinės saugumo kontrolės
- **Užklausų įpurškimo gynyba**: Diegkite Microsoft Prompt Shields su apšvietimu, ribotuvais ir duomenų žymėjimo technikomis
- **Įrankių užnuodijimo prevencija**: Tikrinkite įrankių metaduomenis, stebėkite dinamiškus pokyčius ir patikrinkite įrankių vientisumą
- **Modelio išvesties patikra**: Nuskaitykite modelio išvestis dėl galimo duomenų nutekėjimo, žalingo turinio arba saugumo politikos pažeidimų
- **Konteksto lango apsauga**: Įgyvendinkite kontrolės priemones, kad išvengtumėte konteksto lango užnuodijimo ir manipuliacijų atakų

### 10. Įrankių vykdymo saugumas
- **Vykdymo smėlio dėžės**: Vykdykite įrankių operacijas konteinerizuotose, izoliuotose aplinkose su išteklių ribojimu
- **Privilegijų atskyrimas**: Vykdykite įrankius su minimaliomis reikiamomis privilegijomis ir atskirais paslaugų paskyromis
- **Tinklo izoliacija**: Įgyvendinkite tinklo segmentavimą įrankių vykdymo aplinkoms
- **Vykdymo stebėsena**: Stebėkite įrankių vykdymą dėl anomalios elgsenos, resursų naudojimo ir saugumo pažeidimų

### 11. Nuolatinė saugumo patikra
- **Automatizuotas saugumo testavimas**: Integruokite saugumo testavimą į CI/CD procesus su tokiais įrankiais kaip GitHub Advanced Security
- **Pažeidžiamumo valdymas**: Reguliariai tikrinkite visas priklausomybes, įskaitant AI modelius ir išorines paslaugas
- **Proveržimo testavimas**: Reguliariai vykdykite saugumo vertinimus, skirtus MCP įgyvendinimams
- **Saugumo kodo peržiūros**: Įgyvendinkite privalomas saugumo peržiūras visiems MCP susijusiems kodo pakeitimams

### 12. Tiekimo grandinės saugumas AI
- **Komponentų patikra**: Patikrinkite visų AI komponentų (modelių, įterpimų, API) kilmę, vientisumą ir saugumą
- **Priklausomybių valdymas**: Laikykite atnaujintas visų programinės įrangos ir AI priklausomybių apskaitas su pažeidžiamumo stebėsena
- **Patikimos saugyklos**: Naudokite patikrintus, patikimus šaltinius visiems AI modeliams, bibliotekoms ir įrankiams
- **Tiekimo grandinės stebėsena**: Nuolat stebėkite AI paslaugų tiekėjų ir modelių saugyklų kompromitavimus


## Pažangūs saugumo modeliai

### Nulinės pasitikėjimo architektūra MCP
- **Niekada nepasitikėti, visada tikrinti**: Įgyvendinkite nuolatinį patvirtinimą visiems MCP dalyviams
- **Mikrosektuotė**: Izoliuokite MCP komponentus naudodami smulkias tinklo ir tapatybės kontrolės priemones
- **Sąlyginis prieigos valdymas**: Įgyvendinkite rizika pagrįstas prieigos kontrolės priemones, kurios prisitaiko prie konteksto ir elgesio
- **Nuolatinė rizikos vertinimas**: Dinamiškai vertinkite saugumo būklę remdamiesi esamais grėsmių rodikliais

### Privatumą saugančios dirbtinio intelekto įgyvendinimas
- **Duomenų minimalizavimas**: Atverkite tik minimumą reikalingų duomenų kiekvienam MCP veiksmui
- **Diferencinė privatumas**: Įgyvendinkite privatumą saugančias metodikas jautriems duomenų apdorojimams
- **Homomorfinis šifravimas**: Naudokite pažangias šifravimo technikas saugiam skaičiavimui užšifruotuose duomenyse
- **Federuotas mokymasis**: Įgyvendinkite paskirstyto mokymosi metodus, kurie saugo duomenų vietiškumą ir privatumą

### Incidentų reagavimas dirbtinio intelekto sistemoms
- **Dirbtinio intelekto specialios incidentų procedūros**: Sukurkite incidentų reagavimo procedūras, pritaikytas dirbtinio intelekto ir MCP grėsmėms
- **Automatinis reagavimas**: Įgyvendinkite automatizuotą užkardymą ir pašalinimą dažnoms dirbtinio intelekto saugumo incidentų situacijoms  
- **Teisėsaugos galimybės**: Palaikykite teisėsaugos pasirengimą dirbtinio intelekto sistemų pažeidimams ir duomenų nutekėjimams
- **Atstatymo procedūros**: Nustatykite procedūras atstatymui po dirbtinio intelekto modelių užnuodijimo, užklausų injekcijų atakų ir paslaugų pažeidimų

## Įgyvendinimo ištekliai ir standartai

### 🏔️ Praktiniai saugumo mokymai
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Išsamus praktinis dirbtuvės MCP serverių apsaugai Azure
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Referencinė architektūra ir OWASP MCP Top 10 įgyvendinimo gairės

### Oficialūs MCP dokumentai
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Dabartinė MCP protokolo specifikacija
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Oficialios saugumo gairės
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP autorizacijos modeliai
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Transporto reikalavimai

### Microsoft saugumo sprendimai
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Pažangus užklausų injekcijų apsaugos sprendimas
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Išsamus dirbtinio intelekto turinio filtravimas
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Įmonių tapatybės ir prieigos valdymas
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Saugus slaptažodžių ir kredencialų valdymas
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Tiekimo grandinės ir kodo saugumo nuskaitymas

### Saugumo standartai ir sistemos
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Dabartinės OAuth saugumo gairės
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Interneto programų saugumo rizikos
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Dirbtiniam intelektui specifinės saugumo rizikos
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Išsamus dirbtinio intelekto rizikos valdymas
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Informacijos saugumo valdymo sistemos

### Įgyvendinimo vadovai ir pamokos
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Įmonių autentifikacijos modeliai
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Tapatybės tiekėjo integracija
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Geriausios žetonų valdymo praktikos
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Pažangūs šifravimo modeliai

### Pažangūs saugumo ištekliai
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Saugios programinės įrangos kūrimo praktikos
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - Dirbtinio intelekto specifinis saugumo testavimas
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Dirbtinio intelekto grėsmių modeliavimo metodika
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Privatumą saugančios dirbtinio intelekto technikos

### Atitiktis ir valdymas
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Privatumo atitiktis dirbtinio intelekto sistemose
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Atsakingo dirbtinio intelekto įgyvendinimas
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Saugumo kontrolės dirbtinio intelekto paslaugų tiekėjams
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Sveikatos priežiūros dirbtinio intelekto atitikties reikalavimai

### DevSecOps ir automatizavimas
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Saugūs dirbtinio intelekto vystymo vamzdynai
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Nuolatinė saugumo patikra
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Saugus infrastruktūros diegimas
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Dirbtinio intelekto darbo konteinerių saugumas

### Stebėjimas ir incidentų valdymas  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Išsamūs stebėjimo sprendimai
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Dirbtiniam intelektui skirtos incidentų procedūros
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Saugumo informacijos ir įvykių valdymas

- [Grėsmės žvalgyba dirbtiniam intelektui](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - DI grėsmių žvalgybos ištekliai

## 🔄 Nuolatinis tobulinimas

### Sekite besikeičiančius standartus
- **MCP specifikacijos atnaujinimai**: stebėkite oficialius MCP specifikacijos pakeitimus ir saugumo rekomendacijas
- **Grėsmės žvalgyba**: prenumeruokite DI saugumo grėsmių srautus ir pažeidžiamumų duomenų bazes  
- **Bendruomenės įsitraukimas**: dalyvaukite MCP saugumo bendruomenės diskusijose ir darbo grupėse
- **Reguliarus įvertinimas**: vykdykite ketvirtinius saugumo būklės įvertinimus ir atitinkamai atnaujinkite praktiką

### Indėlis į MCP saugumą
- **Saugumo tyrimai**: prisidėkite prie MCP saugumo tyrimų ir pažeidžiamumų atskleidimo programų
- **Gerosios praktikos dalijimasis**: dalinkitės saugumo įgyvendinimais ir įgytomis pamokomis su bendruomene
- **Standartų kūrimas**: dalyvaukite MCP specifikacijos kūrime ir saugumo standartų rengime
- **Įrankių kūrimas**: kurkite ir dalinkitės saugumo įrankiais bei bibliotekomis MCP ekosistemai

---

*Šis dokumentas atspindi MCP saugumo gerąją praktiką nuo 2026 m. rugsėjo 9 d.,
remiantis MCP specifikacija `2026-07-28`. Saugumo praktikas reikėtų reguliariai
peržiūrėti pagal protokolo ir grėsmių kraštovaizdžio pokyčius.*

## Kas toliau

- Skaitykite: [MCP saugumo gerosios praktikos](./mcp-security-best-practices.md)
- Grįžkite į: [Saugumo modulio apžvalga](./README.md)
- Toliau: [3 modulis: Pradžia](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->