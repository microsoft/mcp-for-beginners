# MCP Saugumo Geriausios Praktikos 2025

Šis išsamus vadovas aprašo esmines saugumo geriausias praktikas Modelio Konteksto Protokolo (MCP) sistemų įgyvendinimui, remiantis naujausia **MCP Specifikacija 2025-11-25** ir dabartiniais pramonės standartais. Šios praktikos sprendžia tiek tradicines saugumo problemas, tiek AI specifines grėsmes, būdingas MCP diegimams.

## Kritiniai Saugumo Reikalavimai

### Privalomi Saugumo Kontrolės Elementai (PRIVALOMA)

1. **Žetonų Patikra**: MCP serveriai **NETURI** priimti jokių žetonų, kurie nebuvo aiškiai išduoti pačiam MCP serveriui
2. **Autorizacijos Patikra**: MCP serveriai, įgyvendinantys autorizaciją, **PRIVALO** patikrinti VISUS gaunamus užklausimus ir **NETURI** naudoti sesijų autentifikacijai  
3. **Vartotojo Sutikimas**: MCP proxy serveriai, naudojantys statinius kliento ID, **PRIVALO** gauti aiškų vartotojo sutikimą kiekvienam dinamiškai registruotam klientui
4. **Saugūs Sesijos ID**: MCP serveriai **PRIVALO** naudoti kriptografiškai saugius, nedeterministinius sesijos ID, sugeneruotus naudojant saugius atsitiktinių skaičių generatorius

## Pagrindinės Saugumo Praktikos

### 1. Įvesties Patikra ir Valymas
- **Išsami Įvesties Patikra**: Patikrinkite ir išvalykite visas įvestis, kad išvengtumėte injekcijų atakų, painiavos problemų ir užklausų injekcijos pažeidžiamumų
- **Parametrų Schemos Laikymasis**: Įgyvendinkite griežtą JSON schemos patikrinimą visiems įrankių parametrams ir API įvestims
- **Turinio Filtravimas**: Naudokite Microsoft Prompt Shields ir Azure Content Safety, kad filtruotumėte kenksmingą turinį užklausose ir atsakymuose
- **Išvesties Valymas**: Patikrinkite ir išvalykite visas modelio išvestis prieš pateikdami vartotojams ar tolesnėms sistemoms

### 2. Autentifikacijos ir Autorizacijos Tobulumas  
- **Išoriniai Tapatybės Tiekėjai**: Deleguokite autentifikaciją patikrintiems tapatybės tiekėjams (Microsoft Entra ID, OAuth 2.1 tiekėjai), o ne įgyvendinkite savo autentifikaciją
- **Smulkios Leidimų Kontrolės**: Įgyvendinkite smulkias, įrankiams specifines teises, laikydamiesi mažiausios privilegijos principo
- **Žetonų Gyvavimo Valdymas**: Naudokite trumpalaikius prieigos žetonus su saugiu rotavimu ir tinkamu auditorijos patikrinimu
- **Daugiaveiksnė Autentifikacija**: Reikalaukite MFA visam administraciniam prieigai ir jautrioms operacijoms

### 3. Saugūs Ryšio Protokolai
- **Transporto Sluoksnio Saugumas**: Naudokite HTTPS/TLS 1.3 visiems MCP ryšiams su tinkamu sertifikatų patikrinimu
- **Galo iki Galo Šifravimas**: Įgyvendinkite papildomus šifravimo sluoksnius itin jautriems duomenims perdavimo ir saugojimo metu
- **Sertifikatų Valdymas**: Užtikrinkite tinkamą sertifikatų gyvavimo ciklo valdymą su automatizuotais atnaujinimo procesais
- **Protokolo Versijos Laikymasis**: Naudokite dabartinę MCP protokolo versiją (2025-11-25) su tinkama versijų deryba.

### 4. Pažangus Greičio Ribojimas ir Išteklių Apsauga
- **Daugiapakopis Greičio Ribojimas**: Įgyvendinkite greičio ribojimą vartotojo, sesijos, įrankio ir išteklių lygiuose, kad išvengtumėte piktnaudžiavimo
- **Adaptuojamas Greičio Ribojimas**: Naudokite mašininio mokymosi pagrindu veikiančią greičio ribojimo sistemą, kuri prisitaiko prie naudojimo modelių ir grėsmių indikatorių
- **Išteklių Kvotų Valdymas**: Nustatykite tinkamas ribas skaičiavimo ištekliams, atminčiai ir vykdymo laikui
- **DDoS Apsauga**: Diegkite išsamią DDoS apsaugą ir srauto analizės sistemas

### 5. Išsamus Žurnalas ir Stebėsena
- **Struktūruotas Audito Žurnalas**: Įgyvendinkite detalius, paieškai pritaikytus žurnalus visoms MCP operacijoms, įrankių vykdymams ir saugumo įvykiams
- **Realaus Laiko Saugumo Stebėsena**: Diegkite SIEM sistemas su AI pagrįsta anomalijų aptikimo funkcija MCP darbo krūviams
- **Privatumo Atitinkamas Žurnalas**: Registruokite saugumo įvykius gerbiant duomenų privatumo reikalavimus ir reglamentus
- **Incidentų Valdymo Integracija**: Sujunkite žurnalo sistemas su automatizuotais incidentų valdymo procesais

### 6. Patobulintos Saugios Saugojimo Praktikos
- **Aparatinės Saugumo Modulių Naudojimas**: Naudokite HSM pagrįstą raktų saugojimą (Azure Key Vault, AWS CloudHSM) kritinėms kriptografinėms operacijoms
- **Šifravimo Raktų Valdymas**: Įgyvendinkite tinkamą raktų rotaciją, atskyrimą ir prieigos kontrolę šifravimo raktams
- **Slapčių Valdymas**: Laikykite visus API raktus, žetonus ir kredencialus specializuotose slapčių valdymo sistemose
- **Duomenų Klasifikavimas**: Klasifikuokite duomenis pagal jautrumo lygius ir taikykite tinkamas apsaugos priemones

### 7. Pažangus Žetonų Valdymas
- **Žetonų Perdavimų Prevencija**: Aiškiai uždrauskite žetonų perdavimo modelius, kurie apeina saugumo kontrolės priemones
- **Auditorijos Patikra**: Visada tikrinkite, ar žetono auditorijos teiginiai atitinka numatytą MCP serverio tapatybę
- **Autorizacija Pagal Teiginius**: Įgyvendinkite smulkias autorizacijos kontrolės priemones, pagrįstas žetono teiginiais ir vartotojo atributais
- **Žetonų Susiejimas**: Susiekite žetonus su konkrečiomis sesijomis, vartotojais ar įrenginiais, kai tai tinkama

### 8. Saugus Sesijų Valdymas
- **Kriptografiniai Sesijos ID**: Generuokite sesijos ID naudodami kriptografiškai saugius atsitiktinių skaičių generatorius (neprognozuojamus sekas)
- **Vartotojui Specifinis Susiejimas**: Susiekite sesijos ID su vartotojui specifine informacija, naudodami saugius formatus, pvz., `<user_id>:<session_id>`
- **Sesijos Gyvavimo Valdymas**: Įgyvendinkite tinkamą sesijos galiojimo pabaigą, rotaciją ir nebegaliojimo mechanizmus
- **Sesijos Saugumo Antraštės**: Naudokite tinkamas HTTP saugumo antraštes sesijos apsaugai

### 9. AI Specifinės Saugumo Kontrolės
- **Užklausų Injecijos Gynyba**: Diegkite Microsoft Prompt Shields su išryškinimu, ribotuvais ir duomenų žymėjimo technikomis
- **Įrankių Nuodijimo Prevencija**: Patikrinkite įrankių metaduomenis, stebėkite dinamiškus pokyčius ir tikrinkite įrankių vientisumą
- **Modelio Išvesties Patikra**: Nuskaitykite modelio išvestis dėl galimų duomenų nutekėjimų, žalingo turinio ar saugumo politikos pažeidimų
- **Konteksto Langų Apsauga**: Įgyvendinkite kontrolės priemones, kad išvengtumėte konteksto langų užnuodijimo ir manipuliavimo atakų

### 10. Įrankių Vykdymo Saugumas
- **Vykdymo Izoliacija**: Vykdykite įrankius konteinerizuotose, izoliuotose aplinkose su išteklių apribojimais
- **Privilegijų Atskyrimas**: Vykdykite įrankius su minimaliai reikalingomis privilegijomis ir atskirais paslaugų paskyromis
- **Tinklo Izoliacija**: Įgyvendinkite tinklo segmentaciją įrankių vykdymo aplinkoms
- **Vykdymo Stebėsena**: Stebėkite įrankių vykdymą dėl anomalijų, išteklių naudojimo ir saugumo pažeidimų

### 11. Nuolatinė Saugumo Patikra
- **Automatizuotas Saugumo Testavimas**: Integruokite saugumo testavimą į CI/CD procesus su įrankiais, pvz., GitHub Advanced Security
- **Pažeidžiamumų Valdymas**: Reguliariai tikrinkite visas priklausomybes, įskaitant AI modelius ir išorines paslaugas
- **Įsiskverbimo Testavimas**: Atlikite reguliarius saugumo vertinimus, skirtus MCP įgyvendinimams
- **Saugumo Kodo Peržiūros**: Įgyvendinkite privalomas saugumo peržiūras visiems MCP susijusiems kodo pakeitimams

### 12. Tiekimo Grandinės Saugumas AI
- **Komponentų Patikra**: Patikrinkite visų AI komponentų (modelių, įterpimų, API) kilmę, vientisumą ir saugumą
- **Priklausomybių Valdymas**: Palaikykite atnaujintą visų programinės įrangos ir AI priklausomybių inventorių su pažeidžiamumų stebėsena
- **Patikimi Saugyklos Šaltiniai**: Naudokite patikrintus, patikimus šaltinius visiems AI modeliams, bibliotekoms ir įrankiams
- **Tiekimo Grandinės Stebėsena**: Nuolat stebėkite AI paslaugų tiekėjų ir modelių saugyklų kompromitavimo atvejus

## Pažangūs Saugumo Modeliai

### Nulinės Pasitikėjimo Architektūra MCP
- **Niekada Nepasitikėkite, Visada Tikrinkite**: Įgyvendinkite nuolatinę patikrą visiems MCP dalyviams
- **Mikrosegmentacija**: Izoliuokite MCP komponentus su smulkia tinklo ir tapatybės kontrole
- **Sąlyginė Prieiga**: Įgyvendinkite rizika pagrįstą prieigos kontrolę, kuri prisitaiko prie konteksto ir elgesio
- **Nuolatinė Rizikos Vertinimas**: Dinamiškai vertinkite saugumo būklę pagal esamus grėsmių indikatorius

### Privatumo Saugojimo AI Įgyvendinimas
- **Duomenų Minimalizavimas**: Atverkite tik būtiniausius duomenis kiekvienai MCP operacijai
- **Diferencinė Privatumas**: Įgyvendinkite privatumo saugojimo technikas jautrių duomenų apdorojimui
- **Homomorfinis Šifravimas**: Naudokite pažangias šifravimo technikas saugiam skaičiavimui su užšifruotais duomenimis
- **Federuotas Mokymasis**: Įgyvendinkite paskirstytas mokymosi metodikas, kurios saugo duomenų lokalumą ir privatumą

### Incidentų Valdymas AI Sistemoms
- **AI Specifinės Incidentų Procedūros**: Parengkite incidentų valdymo procedūras, pritaikytas AI ir MCP specifinėms grėsmėms
- **Automatizuotas Atsakas**: Įgyvendinkite automatizuotą užkardymą ir šalinimą dažniausiems AI saugumo incidentams  
- **Teisėsaugos Galimybės**: Užtikrinkite teisėsaugos pasirengimą AI sistemų kompromisams ir duomenų nutekėjimams
- **Atkūrimo Procedūros**: Nustatykite procedūras AI modelių užnuodijimo, užklausų injekcijos atakų ir paslaugų kompromisų atvejams

## Įgyvendinimo Ištekliai ir Standartai

### Oficialūs MCP Dokumentai
- [MCP Specifikacija 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Dabartinė MCP protokolo specifikacija
- [MCP Saugumo Geriausios Praktikos](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Oficialios saugumo gairės
- [MCP Autorizacijos Specifikacija](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Autentifikacijos ir autorizacijos modeliai
- [MCP Transporto Saugumas](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Transporto sluoksnio saugumo reikalavimai

### Microsoft Saugumo Sprendimai
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Pažangi užklausų injekcijos apsauga
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Išsamus AI turinio filtravimas
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Įmonių tapatybės ir prieigos valdymas
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Saugus slapčių ir kredencialų valdymas
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Tiekimo grandinės ir kodo saugumo skenavimas

### Saugumo Standartai ir Sistemų Rėmai
- [OAuth 2.1 Saugumo Geriausios Praktikos](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Dabartinės OAuth saugumo gairės
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Tinklalapių programų saugumo rizikos
- [OWASP Top 10 LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI specifinės saugumo rizikos
- [NIST AI Rizikos Valdymo Sistema](https://www.nist.gov/itl/ai-risk-management-framework) - Išsami AI rizikos valdymo sistema
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Informacijos saugumo valdymo sistemos

### Įgyvendinimo Vadovai ir Mokymai
- [Azure API Management kaip MCP Autentifikacijos Vartai](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Įmonių autentifikacijos modeliai
- [Microsoft Entra ID su MCP Serveriais](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Tapatybės tiekėjo integracija
- [Saugus Žetonų Saugojimas](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Žetonų valdymo geriausios praktikos
- [Galo iki Galo Šifravimas AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Pažangūs šifravimo modeliai

### Pažangūs Saugumo Ištekliai
- [Microsoft Saugumo Kūrimo Gyvavimo Ciklas](https://www.microsoft.com/sdl) - Saugios kūrimo praktikos
- [AI Raudonosios Komandos Gairės](https://learn.microsoft.com/security/ai-red-team/) - AI specifinis saugumo testavimas
- [Grėsmių Modeliavimas AI Sistemoms](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI grėsmių modeliavimas
- [Privatumo Inžinerija AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Privatumo saugojimo AI technikos

### Atitiktis ir Valdymas
- [GDPR Atitiktis AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Privatumo atitiktis AI sistemose
- [AI Valdymo Sistema](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Atsakingas AI įgyvendinimas
- [SOC 2 AI Paslaugoms](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Saugumo kontrolės AI paslaugų tiekėjams
- [HIPAA Atitiktis AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Sveikatos priežiūros AI atitikties reikalavimai

### DevSecOps ir Automatizavimas
- [DevSecOps Vamzdis AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Saugūs AI kūrimo vamzdynai
- [Automatizuotas Saugumo Testavimas](https://learn.microsoft.com/security/engineering/devsecops) - Nuolatinė saugumo patikra
- [Infrastruktūra kaip Kodo Saugumas](https://learn.microsoft.com/security/engineering/infrastructure-security) - Saugus infrastruktūros diegimas
- [Konteinerių Saugumas AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AI darbo krūvių konteinerizacijos saugumas

### Stebėsena ir Incidentų Valdymas  
- [Azure Monitor AI Darbo Krūviams](https://learn.microsoft.com/azure/azure-monitor/overview) - Išsamūs stebėjimo sprendimai
- [AI Saugumo Incidentų Valdymas](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI specifinės incidentų procedūros
- [SIEM AI Sistemoms](https://learn.microsoft.com/azure/sentinel/overview) - Saugumo informacijos ir įvykių valdymas
- [Grėsmių Žvalgyba AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI grėsmių žvalgybos šaltiniai

## 🔄 Nuolatinis Tobulinimas

### Sekite Besikeičiančius Standartus
- **MCP Specifikacijos Atnaujinimai**: Stebėkite oficialius MCP specifikacijos pakeitimus ir saugumo pranešimus
- **Grėsmių Žvalgyba**: Prenumeruokite AI saugumo grėsmių srautus ir pažeidžiamumų duomenų bazes  
- **Bendruomenės Įsitraukimas**: Dalyvaukite MCP saugumo bendruomenės diskusijose ir darbo grupėse
- **Reguliarūs Vertinimai**: Atlikite ketvirtinius saugumo būklės vertinimus ir atnaujinkite praktikas pagal poreikį

### Indėlis į MCP Saugumą
- **Saugumo Tyrimai**: Prisidėkite prie MCP saugumo tyrimų ir pažeidžiamumų atskleidimo programų
- **Geriausių Praktikų Dalijimasis**: Dalinkitės saugumo įgyvendinimais ir pamokomis su bendruomene
- **Standartinis vystymas**: Dalyvauti MCP specifikacijos kūrime ir saugumo standartų kūrime  
- **Įrankių kūrimas**: Kurti ir dalintis saugumo įrankiais bei bibliotekomis MCP ekosistemai

---

*Šis dokumentas atspindi MCP saugumo geriausias praktikas 2025 m. gruodžio 18 d., remiantis MCP specifikacija 2025-11-25. Saugumo praktikos turėtų būti reguliariai peržiūrimos ir atnaujinamos, atsižvelgiant į protokolo ir grėsmių kraštovaizdžio pokyčius.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->