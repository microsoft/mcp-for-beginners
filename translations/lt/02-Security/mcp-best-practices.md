<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b2b9e15e78b9d9a2b3ff3e8fd7d1f434",
  "translation_date": "2025-08-26T16:42:33+00:00",
  "source_file": "02-Security/mcp-best-practices.md",
  "language_code": "lt"
}
-->
# MCP Saugumo Geriausios Praktikos 2025

Šis išsamus vadovas aprašo esmines saugumo geriausias praktikas, skirtas Model Context Protocol (MCP) sistemų įgyvendinimui, remiantis naujausia **MCP Specifikacija 2025-06-18** ir dabartiniais pramonės standartais. Šios praktikos apima tiek tradicinius saugumo klausimus, tiek AI specifines grėsmes, būdingas MCP diegimams.

## Kritiniai Saugumo Reikalavimai

### Privalomos Saugumo Kontrolės (MUST Reikalavimai)

1. **Tokenų Validacija**: MCP serveriai **NETURI** priimti jokių tokenų, kurie nebuvo aiškiai išduoti tam pačiam MCP serveriui.
2. **Autorizacijos Patikrinimas**: MCP serveriai, įgyvendinantys autorizaciją, **PRIVALĖTŲ** patikrinti VISUS gaunamus užklausimus ir **NETURI** naudoti sesijų autentifikacijai.
3. **Vartotojo Sutikimas**: MCP proxy serveriai, naudojantys statinius klientų ID, **PRIVALĖTŲ** gauti aiškų vartotojo sutikimą kiekvienam dinamiškai registruotam klientui.
4. **Saugūs Sesijos ID**: MCP serveriai **PRIVALĖTŲ** naudoti kriptografiškai saugius, nedeterministinius sesijos ID, generuojamus naudojant saugius atsitiktinių skaičių generatorius.

## Pagrindinės Saugumo Praktikos

### 1. Įvesties Validacija ir Sanitizacija
- **Visapusiška Įvesties Validacija**: Validuokite ir sanitizuokite visas įvestis, kad išvengtumėte injekcijos atakų, supainiotų tarpininkų problemų ir prompt injekcijos pažeidžiamumų.
- **Parametrų Schemos Užtikrinimas**: Įgyvendinkite griežtą JSON schemos validaciją visiems įrankių parametrams ir API įvestims.
- **Turinio Filtravimas**: Naudokite Microsoft Prompt Shields ir Azure Content Safety, kad filtruotumėte kenkėjišką turinį promptuose ir atsakymuose.
- **Išvesties Sanitizacija**: Validuokite ir sanitizuokite visas modelio išvestis prieš jas pateikdami vartotojams ar kitoms sistemoms.

### 2. Autentifikacijos ir Autorizacijos Tobulumas
- **Išoriniai Tapatybės Teikėjai**: Deleguokite autentifikaciją patikimiems tapatybės teikėjams (Microsoft Entra ID, OAuth 2.1 teikėjai), o ne kurkite savo autentifikacijos sprendimus.
- **Smulkios Leidimų Granuliacijos**: Įgyvendinkite detalius, įrankiams specifinius leidimus, laikydamiesi mažiausio privilegijų principo.
- **Tokenų Gyvavimo Ciklo Valdymas**: Naudokite trumpalaikius prieigos tokenus su saugiu rotavimu ir tinkamu auditorijos validavimu.
- **Daugiafaktorė Autentifikacija**: Reikalaukite MFA visiems administraciniams prisijungimams ir jautrioms operacijoms.

### 3. Saugios Komunikacijos Protokolai
- **Transporto Sluoksnio Saugumas**: Naudokite HTTPS/TLS 1.3 visoms MCP komunikacijoms su tinkamu sertifikatų validavimu.
- **Galo-Galo Šifravimas**: Įgyvendinkite papildomus šifravimo sluoksnius itin jautriems duomenims perduodant ir saugant.
- **Sertifikatų Valdymas**: Užtikrinkite tinkamą sertifikatų gyvavimo ciklo valdymą su automatizuotais atnaujinimo procesais.
- **Protokolo Versijos Užtikrinimas**: Naudokite dabartinę MCP protokolo versiją (2025-06-18) su tinkamu versijų derinimu.

### 4. Pažangus Greičio Ribojimas ir Resursų Apsauga
- **Daugiasluoksnis Greičio Ribojimas**: Įgyvendinkite greičio ribojimą vartotojo, sesijos, įrankio ir resursų lygmenyse, kad išvengtumėte piktnaudžiavimo.
- **Adaptacinis Greičio Ribojimas**: Naudokite mašininio mokymosi pagrindu veikiančius greičio ribojimus, kurie prisitaiko prie naudojimo modelių ir grėsmių indikatorių.
- **Resursų Kvotų Valdymas**: Nustatykite tinkamas ribas skaičiavimo resursams, atminties naudojimui ir vykdymo laikui.
- **DDoS Apsauga**: Diegkite visapusiškas DDoS apsaugos ir srauto analizės sistemas.

### 5. Išsamus Žurnalavimas ir Stebėjimas
- **Struktūrizuotas Audito Žurnalavimas**: Įgyvendinkite detalius, ieškomus žurnalus visoms MCP operacijoms, įrankių vykdymams ir saugumo įvykiams.
- **Realaus Laiko Saugumo Stebėjimas**: Naudokite SIEM sistemas su AI pagrįsta anomalijų detekcija MCP darbo krūviams.
- **Privatumo Atitinkantis Žurnalavimas**: Žurnalizuokite saugumo įvykius, laikydamiesi duomenų privatumo reikalavimų ir reglamentų.
- **Incidentų Reagavimo Integracija**: Susiekite žurnalų sistemas su automatizuotais incidentų reagavimo procesais.

### 6. Pagerintos Saugios Saugojimo Praktikos
- **Aparatinės Įrangos Saugumo Moduliai**: Naudokite HSM pagrįstą raktų saugojimą (Azure Key Vault, AWS CloudHSM) kritinėms kriptografinėms operacijoms.
- **Šifravimo Raktų Valdymas**: Įgyvendinkite tinkamą raktų rotavimą, atskyrimą ir prieigos kontrolę šifravimo raktams.
- **Paslapčių Valdymas**: Saugojimo API raktus, tokenus ir kredencialus dedikuotose paslapčių valdymo sistemose.
- **Duomenų Klasifikacija**: Klasifikuokite duomenis pagal jautrumo lygius ir taikykite tinkamas apsaugos priemones.

### 7. Pažangus Tokenų Valdymas
- **Tokenų Perdavimų Prevencija**: Aiškiai drauskite tokenų perdavimo modelius, kurie apeina saugumo kontrolę.
- **Auditorijos Validacija**: Visada tikrinkite, ar tokenų auditorijos teiginiai atitinka numatytą MCP serverio tapatybę.
- **Teiginių Pagrįsta Autorizacija**: Įgyvendinkite detalią autorizaciją, pagrįstą tokenų teiginiais ir vartotojų atributais.
- **Tokenų Susiejimas**: Susiekite tokenus su konkrečiomis sesijomis, vartotojais ar įrenginiais, kai tai tinkama.

### 8. Saugus Sesijų Valdymas
- **Kriptografiniai Sesijos ID**: Generuokite sesijos ID, naudodami kriptografiškai saugius atsitiktinių skaičių generatorius (ne nuspėjamus sekas).
- **Vartotojui Specifinis Susiejimas**: Susiekite sesijos ID su vartotojui specifine informacija, naudodami saugius formatus, pvz., `<user_id>:<session_id>`.
- **Sesijos Gyvavimo Ciklo Kontrolė**: Įgyvendinkite tinkamą sesijų galiojimo pabaigą, rotavimą ir anuliavimo mechanizmus.
- **Sesijos Saugumo Antraštės**: Naudokite tinkamas HTTP saugumo antraštes sesijų apsaugai.

### 9. AI Specifinės Saugumo Kontrolės
- **Promptų Injekcijos Gynyba**: Naudokite Microsoft Prompt Shields su akcentavimu, ribotuvais ir duomenų žymėjimo technikomis.
- **Įrankių Užnuodijimo Prevencija**: Validuokite įrankių metaduomenis, stebėkite dinaminius pokyčius ir tikrinkite įrankių vientisumą.
- **Modelio Išvesties Validacija**: Tikrinkite modelio išvestis dėl galimo duomenų nutekėjimo, kenksmingo turinio ar saugumo politikos pažeidimų.
- **Konteksto Langų Apsauga**: Įgyvendinkite kontrolę, kad išvengtumėte konteksto langų užnuodijimo ir manipuliavimo atakų.

### 10. Įrankių Vykdymo Saugumas
- **Vykdymo Sandarinimas**: Vykdykite įrankius konteinerizuotose, izoliuotose aplinkose su resursų ribomis.
- **Privilegijų Atskyrimas**: Vykdykite įrankius su minimaliomis reikalingomis privilegijomis ir atskirtais paslaugų paskyromis.
- **Tinklo Izoliacija**: Įgyvendinkite tinklo segmentaciją įrankių vykdymo aplinkoms.
- **Vykdymo Stebėjimas**: Stebėkite įrankių vykdymą dėl anomalijų, resursų naudojimo ir saugumo pažeidimų.

### 11. Nuolatinė Saugumo Validacija
- **Automatizuotas Saugumo Testavimas**: Integruokite saugumo testavimą į CI/CD procesus su tokiais įrankiais kaip GitHub Advanced Security.
- **Pažeidžiamumų Valdymas**: Reguliariai tikrinkite visas priklausomybes, įskaitant AI modelius ir išorines paslaugas.
- **Penetracinis Testavimas**: Reguliariai vykdykite saugumo vertinimus, specialiai nukreiptus į MCP įgyvendinimus.
- **Saugumo Kodo Peržiūros**: Įgyvendinkite privalomas saugumo peržiūras visiems MCP susijusiems kodo pakeitimams.

### 12. AI Tiekimo Grandinės Saugumas
- **Komponentų Patikrinimas**: Patikrinkite visų AI komponentų (modelių, įterpimų, API) kilmę, vientisumą ir saugumą.
- **Priklausomybių Valdymas**: Palaikykite dabartinius visų programinės įrangos ir AI priklausomybių inventorius su pažeidžiamumų stebėjimu.
- **Patikimi Repozitoriumai**: Naudokite patikrintus, patikimus šaltinius visiems AI modeliams, bibliotekoms ir įrankiams.
- **Tiekimo Grandinės Stebėjimas**: Nuolat stebėkite AI paslaugų teikėjų ir modelių repozitoriumų kompromisus.

## Pažangūs Saugumo Modeliai

### Zero Trust Architektūra MCP
- **Niekada Nepasitikėkite, Visada Tikrinkite**: Įgyvendinkite nuolatinį visų MCP dalyvių tikrinimą.
- **Mikrosegmentacija**: Izoliuokite MCP komponentus su detaliomis tinklo ir tapatybės kontrolėmis.
- **Sąlyginė Prieiga**: Įgyvendinkite rizika pagrįstą prieigos kontrolę, kuri prisitaiko prie konteksto ir elgsenos.
- **Nuolatinis Rizikos Vertinimas**: Dinamiškai vertinkite saugumo būklę pagal dabartinius grėsmių indikatorius.

### Privatumo Išsaugojanti AI Įgyvendinimas
- **Duomenų Minimalizavimas**: Atskleiskite tik minimaliai reikalingus duomenis kiekvienai MCP operacijai.
- **Diferencinis Privatumas**: Įgyvendinkite privatumo išsaugojimo technikas jautrių duomenų apdorojimui.
- **Homomorfinis Šifravimas**: Naudokite pažangias šifravimo technikas saugiam skaičiavimui su šifruotais duomenimis.
- **Federuotas Mokymasis**: Įgyvendinkite paskirstytus mokymosi metodus, kurie išsaugo duomenų lokalumą ir privatumą.

### Incidentų Reagavimas AI Sistemoms
- **AI Specifinės Incidentų Procedūros**: Sukurkite incidentų reagavimo procedūras, pritaikytas AI ir MCP specifinėms grėsmėms.
- **Automatizuotas Reagavimas**: Įgyvendinkite automatizuotą izoliavimą ir atkūrimą dažniems AI saugumo incidentams.
- **Teismo Ekspertizės Galimybės**: Užtikrinkite pasirengimą AI sistemų kompromisų ir duomenų nutekėjimų tyrimams.
- **Atkūrimo Procedūros**: Nustatykite procedūras, skirtas atsigauti po AI modelių užnuodijimo, prompt injekcijos atakų ir paslaugų kompromisų.
- **Įrankių kūrimas**: Kurkite ir dalinkitės saugumo įrankiais bei bibliotekomis MCP ekosistemai

---

*Šis dokumentas atspindi MCP saugumo geriausią praktiką, galiojančią 2025 m. rugpjūčio 18 d., remiantis MCP specifikacija 2025-06-18. Saugumo praktikos turėtų būti reguliariai peržiūrimos ir atnaujinamos, kai protokolas ir grėsmių aplinka keičiasi.*

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.