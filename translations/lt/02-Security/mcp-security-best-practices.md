# MCP Saugumo Geriausios Praktikos – 2026 m. Rugsėjo Atnaujinimas

> **Svarbu:** Šis dokumentas atspindi
> [MCP Specifikaciją 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> ir oficialų
> [MCP Saugumo Geriausių Praktikų](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) rinkinį.

## 🏔️ Praktinis Saugumo Mokymas

Praktiniam įgyvendinimui rekomenduojame **[MCP Saugumo Viršūnių Dirbtuves (Sherpa)](https://azure-samples.github.io/sherpa/)** – išsamų ir vadovaujamą žygį, skirtą MCP serverių saugumui Azure užtikrinti. Dirbtuvėse yra aptariami visi OWASP MCP Top 10 rizikų aspektai per metodiką „pažeidžiamumas → išnaudojimas → taisymas → patikrinimas“.

Visos šiame dokumente pateiktos praktikos atitinka **[OWASP MCP Azure Saugumo Vadovą](https://microsoft.github.io/mcp-azure-security-guide/)**, kuris suteikia konkrečias įgyvendinimo gaires Azure aplinkai.

## Esminės Saugumo Praktikos MCP Įgyvendinimams

Model Context Protocol sukelia unikalius saugumo iššūkius, kurie viršija tradicinio programinės įrangos saugumą. Šios praktikos orientuotos į pagrindinius reikalavimus ir MCP specifines grėsmes, tokias kaip promptų įterpimas, įrankių užnuodijimas, būsenos valdiklio užgrobimas, klaidinančio tarpininko problemos ir tokenų perleidimo pažeidžiamumai.





### **PRIVALOMI Saugumo Reikalavimai**

**Kritiniai Reikalavimai iš MCP Specifikacijos:**

> **NEGALIMA:** MCP serveriai **NEGALI** priimti jokių tokenų, kurie nebuvo aiškiai išduoti šiam MCP serveriui
>
> **PRIVALOMA:** MCP serveriai, taikantys autorizaciją, **PRIVALO** patikrinti VISUS įeinančius užklausimus
>
> **NEGALIMA:** MCP serveriai **NEGALI** naudoti sesijų autentifikacijai
>
> **PRIVALOMA:** MCP tarpiniai serveriai, naudojantys statinį trečiosios šalies kliento ID, **PRIVALO**
> gauti sutikimą iš kiekvieno MCP kliento prieš perduodant autorizaciją

---

## 1. **Tokenų Saugumas ir Autentifikacija**

**Autentifikacijos ir Autorizacijos Kontrolės:**
   - **Griežtas Autorizacijos Peržiūrėjimas**: Atlikite išsamias MCP serverio autorizacijos logikos auditus, kad tik numatyti vartotojai ir klientai galėtų gauti prieigą prie išteklių
   - **Išorinių Tapatybės Teikėjų Integracija**: Naudokite patikimus tapatybės teikėjus, tokius kaip Microsoft Entra ID, o ne diegkite savarankišką autentifikaciją
   - **Tokenų Auditoriaus Validavimas**: Visada tikrinkite, ar tokenai buvo aiškiai išduoti jūsų MCP serveriui – niekada nepriimkite tokenų iš aukštesnio lygio serverių
   - **Tinkamas Tokenų Gyvavimo Ciklas**: Įgyvendinkite saugų tokenų sukimą, galiojimo pabaigos politiką ir užkirsti kelią tokenų pakartotinėms atakoms

**Apsaugotas Tokenų Saugojimas:**
   - Naudokite Azure Key Vault arba panašias saugias kredencialų saugyklas visiems slaptiems duomenims
   - Užtikrinkite tokenų šifravimą tiek saugojimo, tiek perdavimo metu
   - Reguliarus kredencialų sukimasis ir neautorizuotos prieigos stebėjimas

## 2. **Būsenos Valdiklis ir Transporto Saugumas**

**Saugios Programos Būsenos Praktikos:**

- **Nepermatomi Būsenos Valdikliai**: Naudokite saugius, nedeterministinius valdiklius programos būsenai, kuri tęsiasi per užklausas

- **Vartotojo Specifinis Ryšys**: Susiekite valdiklius pusės serverio autentifikuotam subjektui ir atminkite kryžminio vartotojo pakartotinį panaudojimą

- **Gyvavimo Ciklo Valdymas**: Nustatykite valdiklių galiojimo pabaigos ir atšaukimo mechanizmus, kad sumažintumėte pažeidžiamumo laikotarpius

- **Autorizacija Kiekvienai Užklausai**: Niekuomet neturėtų būti laikoma, kad būsenos valdiklis yra autentifikacijos priemonė; kiekviena užklausa, pateikusi jį, turi būti autorizuota





- Naudokite procesų izoliaciją ir aplinkos kredencialus vietiniams stdio serveriams



## 3. **Dirbtinio intelekto specifinė grėsmių apsauga** 🤖

**Užklausų injekcijos gynyba:**
   - **Microsoft Užklausų skydai**: Diegti AI Užklausų skydus pažangiam kenksmingų nurodymų aptikimui ir filtravimui
   - **Įvesties validacija**: Patikrinti ir išvalyti visas įvestis, kad būtų išvengta injekcijos atakų ir painiavos pavaldinio problemų
   - **Turinio ribos**: Naudoti ribotuvų ir duomenų žymėjimo sistemas, kad atskirtumėte patikimus nurodymus nuo išorinės informacijos

**Įrankių apsinuodijimo prevencija:**
   - **Įrankių metaduomenų validacija**: Įgyvendinti vientisumo patikras įrankių apibrėžimuose ir stebėti netikėtus pakeitimus
   - **Dinaminis įrankių stebėjimas**: Stebėti vykdymo metu elgseną ir įdiegti perspėjimus dėl netikėtų vykdymo modelių
   - **Patvirtinimo darbo eigos**: Reikalauti aiškaus vartotojo patvirtinimo įrankių modifikacijoms ir galimybių keitimams

## 4. **Prieigos kontrolė ir leidimai**

**Mažiausių teisių principas:**
   - Suteikti MCP serveriams tik minimalius leidimus, reikalingus numatytai funkcijai
   - Įgyvendinti vaidmenimis pagrįstą prieigos kontrolę (RBAC) su smulkiais leidimais
   - Reguliarūs leidimų peržiūrimai ir nuolatinė privilegijų didinimo stebėsena

**Vykdymo metu taikoma leidimų kontrolė:**
   - Taikyti išteklių ribojimus, kad būtų išvengta išteklių išeikvojimo atakų
   - Naudoti konteinerių izoliaciją įrankių vykdymo aplinkose  
   - Įdiegti „just-in-time“ prieigą administracinėms funkcijoms

## 5. **Turinio saugumas ir stebėsena**

**Turinio saugumo įgyvendinimas:**
   - **Azure turinio saugumo integracija**: Naudoti Azure turinio saugumą kenksmingam turiniui, išsilaisvinimo bandymams ir politikos pažeidimams aptikti
   - **Elgesio analizė**: Įgyvendinti vykdymo metu elgsenos stebėjimą MCP serveriuose ir įrankių vykdyme anomalijoms aptikti
   - **Išsami žurnalo vedimas**: Fiksuoti visas autentifikavimo bandymų, įrankių kvietimų ir saugumo įvykių informacija su saugiu, nenukreipiamu saugojimu

**Nuolatinė stebėsena:**
   - Realiojo laiko perspėjimai įtartinų modelių ir neleistinų prieigos bandymų atvejais  
   - Integracija su SIEM sistemomis centralizuotam saugumo įvykių valdymui
   - Reguliarūs saugumo auditai ir MCP įgyvendinimų įsilaužimo testavimas

## 6. **Tiekimo grandinės saugumas**

**Komponentų patikra:**
   - **Priklausomybių skanavimas**: Naudoti automatizuotą pažeidžiamumų skanavimą visoms programinės įrangos priklausomybėms ir DI komponentams
   - **Kilniosios kilmės tikrinimas**: Patikrinti modelių, duomenų šaltinių ir išorinių paslaugų kilmę, licencijas ir vientisumą
   - **Pasirašyti paketai**: Naudoti kriptografiškai pasirašytus paketus ir tikrinti parašus prieš diegiant

**Saugus kūrimo vamzdelis:**
   - **GitHub pažangi sauga**: Įgyvendinti slaptumo skanavimą, priklausomybių analizę ir CodeQL statinę analizę
   - **CI/CD saugumas**: Integruoti saugumo patikrą per visą automatizuotų diegimų vamzdelį
   - **Artefaktų vientisumas**: Įgyvendinti kriptografinį patikrinimą diegiamiems artefaktams ir konfigūracijoms

## 7. **OAuth saugumas ir painiavos pavaldinio prevencija**

**OAuth 2.1 įgyvendinimas:**
   - **PKCE įgyvendinimas**: Naudoti Įrodymo raktą kodo mainams (PKCE) visuose autorizacijos užklausimuose
    - **Kliento registracija**: Pirmenybę teikti kliento ID metaduomenų dokumentams ar
       išankstinei registracijai; naudoti pasenusią Dinaminę kliento registraciją tik kaip
       suderinamumo atsarginę priemonę
    - **Aiškus sutikimas**: MCP tarpininkai, naudojantys statinį trečiosios šalies kliento ID, privalo
       gauti sutikimą kiekvienam MCP klientui prieš perduodant autorizaciją
   - **Redirect URI validacija**: Įgyvendinti griežtą peradresavimo URI ir kliento identifikatorių patikrinimą

**Tarpinio serverio saugumas:**
   - Užkirsti kelią autorizacijos apeitimui naudojant statinį kliento ID
   - Įgyvendinti tinkamas sutikimo darbo eigos procedūras prieigai prie trečiųjų šalių API
   - Stebėti autorizacijos kodo vagystes ir neleistiną API prieigą

## 8. **Incidentų valdymas ir atkūrimas**


**Greito reagavimo galimybės:** 

   - **Automatinis atsakymas**: Įgyvendinti automatines sistemas autentifikacijos duomenų keitimui ir grėsmių valdymui
   - **Atstatymo procedūros**: Gebėjimas greitai grįžti prie žinomų gerų konfigūracijų ir komponentų
   - **Teisėsaugos galimybės**: Išsamūs audito takeliai ir žurnalai incidentų tyrimams

**Komunikacija ir koordinavimas:**
   - Aiškios saugumo incidentų eskalavimo procedūros
   - Integracija su organizacijos incidentų atsako komandomis
   - Reguliarūs saugumo incidentų simuliavimai ir stalo pratybos

## 9. **Atitiktis ir valdymas**

**Reguliacinė atitiktis:**
   - Užtikrinti, kad MCP įgyvendinimai atitiktų pramonės specifinius reikalavimus (GDPR, HIPAA, SOC 2)
   - Įgyvendinti duomenų klasifikaciją ir privatumo kontrolę AI duomenų apdorojimui
   - Išlaikyti išsamią dokumentaciją atitikčių auditui

**Pokyčių valdymas:**
   - Formalūs saugumo peržiūros procesai visiems MCP sistemos pakeitimams
   - Versijų valdymas ir patvirtinimo darbo srautai konfigūracijos pakeitimams
   - Reguliarūs atitikties vertinimai ir spragų analizė

## 10. **Pažangūs saugumo valdikliai**

**Nulinės pasitikėjimo architektūra:**
   - **Niekada nepasitikėk, visada tikrink**: Nuolatinis vartotojų, įrenginių ir jungčių tikrinimas
   - **Mikrosegmentacija**: Smulkios tinklo kontrolės atskiriantys atskirus MCP komponentus
   - **Sąlyginis prieinamumas**: Prieigos kontrolės, paremtos rizika, prisitaikančios prie dabartinio konteksto ir elgesio

**Vykdymo laiko programų apsauga:**
   - **Vykdymo laiko programų savisauga (RASP)**: Diegti RASP technikas realaus laiko grėsmių aptikimui
   - **Programų veikimo stebėseną**: Stebėti veiklos anomalijas, kurios gali rodyti atakas
   - **Dinaminės saugumo politikos**: Įgyvendinti saugumo politiką, kuri prisitaiko pagal dabartinį grėsmių kraštovaizdį

## 11. **Microsoft saugumo ekosistemos integracija**

**Išsamus Microsoft saugumas:**
   - **Microsoft Defender for Cloud**: Debesijos saugumo būklės valdymas MCP darbo krūviams
   - **Azure Sentinel**: Debesijos gimtoji SIEM ir SOAR galimybės pažangiam grėsmių aptikimui
   - **Microsoft Purview**: Duomenų valdymas ir atitiktis AI darbo srautams ir duomenų šaltiniams

**Tapatybės ir prieigos valdymas:**
   - **Microsoft Entra ID**: Įmonių tapatybės valdymas su sąlyginės prieigos politikomis
   - **Privilegijuotų tapatybių valdymas (PIM)**: Laiku suteikiama prieiga ir patvirtinimo darbo srautai administravimo funkcijoms
   - **Tapatybės apsauga**: Rizika paremtas sąlyginis prieinamumas ir automatinis grėsmių atsakas

## 12. **Nuolatinis saugumo vystymasis**

**Būti naujausiu:**
   - **Specifikacijų stebėjimas**: Reguliari MCP specifikacijų atnaujinimų ir saugumo gairių pokyčių apžvalga
   - **Grėsmių žvalgyba**: Integracija su AI specifinėmis grėsmių srautais ir pažeidžiamumo indikatoriais
   - **Saugumo bendruomenės įsitraukimas**: Aktyvus dalyvavimas MCP saugumo bendruomenėje ir pažeidžiamumo atskleidimo programose

**Adaptuojamas saugumas:**
   - **Mašininio mokymosi saugumas**: Naudoti mašininio mokymosi pagrindu veikiančią anomalijų aptikimą naujiems atakų modeliams identifikuoti
   - **Prognozuojamo saugumo analizė**: Įgyvendinti prognozuojamuosius modelius proaktyviam grėsmių nustatymui
   - **Saugumo automatizacija**: Automatizuoti saugumo politikos atnaujinimai, pagrįsti grėsmių žvalgyba ir specifikacijų pokyčiais

---

## **Svarbūs saugumo ištekliai**

### **Oficiali MCP dokumentacija**
- [MCP specifikacija (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP saugumo gerosios praktikos](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP autorizacijos specifikacija](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP saugumo ištekliai**
- [OWASP MCP Azure saugumo vadovas](https://microsoft.github.io/mcp-azure-security-guide/) - Išsamus OWASP MCP Top 10 su Azure įgyvendinimu
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Oficialios OWASP MCP saugumo rizikos
- [MCP saugumo viršūnių susitikimo dirbtuvės (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktinis saugumo mokymas MCP su Azure

### **Microsoft saugumo sprendimai**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID saugumas](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub pažangus saugumas](https://github.com/security/advanced-security)

### **Saugumo standartai**
- [OAuth 2.0 saugumo gerosios praktikos (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 dideliems kalbų modeliams](https://genai.owasp.org/)
- [NIST AI rizikos valdymo sistema](https://www.nist.gov/itl/ai-risk-management-framework)

### **Įgyvendinimo gairės**
- [Azure API Management MCP autentifikavimo vartai](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID su MCP serveriais](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Saugumo pranešimas:** MCP saugumo praktikos sparčiai vystosi. Visada tikrinkite
> dabartinę [MCP specifikaciją](https://modelcontextprotocol.io/specification/2026-07-28/)
> ir [oficialią saugumo dokumentaciją](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> prieš įgyvendinimą.

## Kas toliau

- Skaitykite: [MCP saugumo valdikliai](./mcp-security-controls.md)
- Grįžkite į: [Saugumo modulio apžvalga](./README.md)
- Tęskite į: [Modulis 3: Pradžia](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->