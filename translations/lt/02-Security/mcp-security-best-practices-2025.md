# MCP saugumo geriausios praktikos – 2025 m. gruodžio atnaujinimas

> **Svarbu**: Šis dokumentas atspindi naujausius [MCP specifikacijos 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) saugumo reikalavimus ir oficialias [MCP saugumo geriausias praktikas](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Visada kreipkitės į esamą specifikaciją dėl naujausių nurodymų.

## Esminės saugumo praktikos MCP įgyvendinimams

Modelio konteksto protokolas kelia unikalius saugumo iššūkius, kurie viršija tradicinio programinės įrangos saugumą. Šios praktikos apima tiek pagrindinius saugumo reikalavimus, tiek MCP specifines grėsmes, įskaitant užklausų injekciją, įrankių užnuodijimą, sesijų užgrobimą, painiavos tarpininko problemas ir žetonų perleidimo pažeidžiamumus.

### **PRIVALOMI saugumo reikalavimai**

**Kritiniai reikalavimai iš MCP specifikacijos:**

### **PRIVALOMI saugumo reikalavimai**

**Kritiniai reikalavimai iš MCP specifikacijos:**

> **NEGALI**: MCP serveriai **NEGALI** priimti jokių žetonų, kurie nebuvo aiškiai išduoti MCP serveriui  
>  
> **TURI**: MCP serveriai, įgyvendinantys autorizaciją, **TURI** patikrinti VISUS gaunamus užklausimus  
>  
> **NEGALI**: MCP serveriai **NEGALI** naudoti sesijų autentifikacijai  
>  
> **TURI**: MCP tarpiniai serveriai, naudojantys statinius kliento ID, **TURI** gauti vartotojo sutikimą kiekvienam dinamiškai registruotam klientui

---

## 1. **Žetonų saugumas ir autentifikacija**

**Autentifikacijos ir autorizacijos kontrolė:**
   - **Griežtas autorizacijos peržiūrėjimas**: Atlikite išsamius MCP serverio autorizacijos logikos auditą, kad užtikrintumėte, jog prieiga prie išteklių suteikiama tik numatytiems vartotojams ir klientams  
   - **Išorinių tapatybės tiekėjų integracija**: Naudokite patikimus tapatybės tiekėjus, tokius kaip Microsoft Entra ID, vietoje savos autentifikacijos įgyvendinimo  
   - **Žetonų auditorijos patikra**: Visada tikrinkite, ar žetonai buvo aiškiai išduoti jūsų MCP serveriui – niekada nepriimkite aukštesnio lygio žetonų  
   - **Tinkamas žetonų gyvavimo ciklas**: Įgyvendinkite saugų žetonų rotavimą, galiojimo pabaigos politiką ir užkirsti kelią žetonų pakartotiniam naudojimui

**Apsaugotas žetonų saugojimas:**
   - Naudokite Azure Key Vault arba panašias saugias kredencialų saugyklas visiems slaptažodžiams  
   - Įgyvendinkite žetonų šifravimą tiek saugojimo metu, tiek perdavimo metu  
   - Reguliariai rotuokite kredencialus ir stebėkite neautorizuotą prieigą

## 2. **Sesijų valdymas ir transporto saugumas**

**Saugios sesijos praktikos:**
   - **Kriptografiškai saugūs sesijos ID**: Naudokite saugius, nedeterministinius sesijos ID, sugeneruotus naudojant saugius atsitiktinių skaičių generatorius  
   - **Vartotojui pritaikytas susiejimas**: Susiekite sesijos ID su vartotojo tapatybe, naudodami formatus, pvz., `<user_id>:<session_id>`, kad išvengtumėte sesijų piktnaudžiavimo tarp vartotojų  
   - **Sesijos gyvavimo ciklo valdymas**: Įgyvendinkite tinkamą galiojimo pabaigą, rotaciją ir nebegaliojimą, kad sumažintumėte pažeidžiamumo langus  
   - **HTTPS/TLS privalomumas**: Privaloma naudoti HTTPS visam ryšiui, kad būtų išvengta sesijos ID perėmimo

**Transporto sluoksnio saugumas:**
   - Konfigūruokite TLS 1.3, kur įmanoma, su tinkamu sertifikatų valdymu  
   - Įgyvendinkite sertifikatų fiksavimą kritinėms jungtims  
   - Reguliariai rotuokite sertifikatus ir tikrinkite jų galiojimą

## 3. **Dirbtinio intelekto specifinė grėsmių apsauga** 🤖

**Užklausų injekcijos gynyba:**
   - **Microsoft užklausų skydai**: Diegkite AI užklausų skydus pažangiam kenksmingų nurodymų aptikimui ir filtravimui  
   - **Įvesties valymas**: Tikrinkite ir valykite visas įvestis, kad išvengtumėte injekcijos atakų ir painiavos tarpininko problemų  
   - **Turinio ribos**: Naudokite skyriklius ir duomenų žymėjimo sistemas, kad atskirtumėte patikimus nurodymus nuo išorinio turinio

**Įrankių užnuodijimo prevencija:**
   - **Įrankių metaduomenų patikra**: Įgyvendinkite vientisumo patikras įrankių apibrėžimams ir stebėkite netikėtus pakeitimus  
   - **Dinaminis įrankių stebėjimas**: Stebėkite vykdymo elgseną ir nustatykite įspėjimus dėl netikėtų vykdymo modelių  
   - **Patvirtinimo darbo srautai**: Reikalaukite aiškaus vartotojo patvirtinimo įrankių modifikacijoms ir galimybių pakeitimams

## 4. **Prieigos kontrolė ir leidimai**

**Mažiausių privilegijų principas:**
   - Suteikite MCP serveriams tik minimalius leidimus, reikalingus numatytai funkcijai  
   - Įgyvendinkite vaidmenimis pagrįstą prieigos kontrolę (RBAC) su smulkiais leidimais  
   - Reguliariai peržiūrėkite leidimus ir nuolat stebėkite privilegijų didinimą

**Vykdymo laiko leidimų kontrolė:**
   - Taikykite išteklių ribojimus, kad išvengtumėte išteklių išeikvojimo atakų  
   - Naudokite konteinerių izoliaciją įrankių vykdymo aplinkoms  
   - Įgyvendinkite prieigą „tik laiku“ administracinėms funkcijoms

## 5. **Turinio saugumas ir stebėjimas**

**Turinio saugumo įgyvendinimas:**
   - **Azure Content Safety integracija**: Naudokite Azure Content Safety kenksmingam turiniui, „jailbreak“ bandymams ir politikos pažeidimams aptikti  
   - **Elgsenos analizė**: Įgyvendinkite vykdymo laiko elgsenos stebėjimą, kad aptiktumėte anomalijas MCP serverio ir įrankių vykdyme  
   - **Išsamus žurnalas**: Registruokite visas autentifikacijos bandymus, įrankių kvietimus ir saugumo įvykius su saugiu, nepažeidžiamu saugojimu

**Nuolatinis stebėjimas:**
   - Realaus laiko įspėjimai apie įtartinus modelius ir neautorizuotus prieigos bandymus  
   - Integracija su SIEM sistemomis centralizuotam saugumo įvykių valdymui  
   - Reguliarūs saugumo auditai ir MCP įgyvendinimų įsilaužimo testavimas

## 6. **Tiekimo grandinės saugumas**

**Komponentų patikra:**
   - **Priklausomybių skenavimas**: Naudokite automatizuotą pažeidžiamumų skenavimą visoms programinės įrangos priklausomybėms ir DI komponentams  
   - **Kilmes patikra**: Patikrinkite modelių, duomenų šaltinių ir išorinių paslaugų kilmę, licencijavimą ir vientisumą  
   - **Pasirašyti paketai**: Naudokite kriptografiškai pasirašytus paketus ir patikrinkite parašus prieš diegimą

**Saugus kūrimo vamzdis:**
   - **GitHub Advanced Security**: Įgyvendinkite slaptažodžių skenavimą, priklausomybių analizę ir CodeQL statinę analizę  
   - **CI/CD saugumas**: Integruokite saugumo patikrinimus visame automatizuotame diegimo procese  
   - **Artefaktų vientisumas**: Įgyvendinkite kriptografinę patikrą diegiamiems artefaktams ir konfigūracijoms

## 7. **OAuth saugumas ir painiavos tarpininko prevencija**

**OAuth 2.1 įgyvendinimas:**
   - **PKCE įgyvendinimas**: Naudokite Proof Key for Code Exchange (PKCE) visiems autorizacijos užklausimams  
   - **Aiškus sutikimas**: Gaukite vartotojo sutikimą kiekvienam dinamiškai registruotam klientui, kad išvengtumėte painiavos tarpininko atakų  
   - **Redirect URI patikra**: Įgyvendinkite griežtą nukreipimo URI ir kliento identifikatorių patikrą

**Tarpinio serverio saugumas:**
   - Užkirsti kelią autorizacijos apeitimui naudojant statinius kliento ID  
   - Įgyvendinti tinkamus sutikimo darbo srautus trečiųjų šalių API prieigai  
   - Stebėti autorizacijos kodo vagystes ir neautorizuotą API prieigą

## 8. **Incidentų valdymas ir atkūrimas**

**Greitos reagavimo galimybės:**
   - **Automatizuotas reagavimas**: Įgyvendinkite automatizuotas sistemas kredencialų rotacijai ir grėsmių suvaldymui  
   - **Atstatymo procedūros**: Gebėjimas greitai grįžti prie žinomų gerų konfigūracijų ir komponentų  
   - **Teisėsaugos galimybės**: Išsamūs audito takai ir žurnalas incidentų tyrimui

**Komunikacija ir koordinacija:**
   - Aiškios eskalavimo procedūros saugumo incidentams  
   - Integracija su organizacijos incidentų valdymo komandomis  
   - Reguliarūs saugumo incidentų simuliacijos ir stalo pratybos

## 9. **Atitiktis ir valdymas**

**Reguliacinė atitiktis:**
   - Užtikrinkite, kad MCP įgyvendinimai atitiktų pramonės specifinius reikalavimus (GDPR, HIPAA, SOC 2)  
   - Įgyvendinkite duomenų klasifikavimą ir privatumo kontrolę DI duomenų apdorojimui  
   - Išlaikykite išsamią dokumentaciją atitikties auditui

**Pakeitimų valdymas:**
   - Formalūs saugumo peržiūros procesai visiems MCP sistemos pakeitimams  
   - Versijų valdymas ir patvirtinimo darbo srautai konfigūracijų pakeitimams  
   - Reguliarūs atitikties vertinimai ir spragų analizė

## 10. **Pažangios saugumo kontrolės**

**Nulinės pasitikėjimo architektūra:**
   - **Niekada nepasitikėk, visada tikrink**: Nuolatinė vartotojų, įrenginių ir jungčių patikra  
   - **Mikrosegmentacija**: Smulkios tinklo kontrolės, izoliuojančios atskirus MCP komponentus  
   - **Sąlyginė prieiga**: Rizika pagrįstos prieigos kontrolės, prisitaikančios prie dabartinio konteksto ir elgsenos

**Vykdymo laiko programų apsauga:**
   - **Vykdymo laiko programų savisauga (RASP)**: Diegti RASP metodus realaus laiko grėsmių aptikimui  
   - **Programų našumo stebėjimas**: Stebėti našumo anomalijas, kurios gali rodyti atakas  
   - **Dinaminės saugumo politikos**: Įgyvendinti saugumo politiką, kuri prisitaiko prie esamos grėsmių aplinkos

## 11. **Microsoft saugumo ekosistemos integracija**

**Išsamus Microsoft saugumas:**
   - **Microsoft Defender for Cloud**: Debesų saugumo būklės valdymas MCP darbo krūviams  
   - **Azure Sentinel**: Debesų gimtoji SIEM ir SOAR galimybės pažangiam grėsmių aptikimui  
   - **Microsoft Purview**: Duomenų valdymas ir atitiktis DI darbo srautams ir duomenų šaltiniams

**Tapatybės ir prieigos valdymas:**
   - **Microsoft Entra ID**: Įmonių tapatybės valdymas su sąlyginės prieigos politikomis  
   - **Privilegijuotos tapatybės valdymas (PIM)**: Prieiga „tik laiku“ ir patvirtinimo darbo srautai administracinėms funkcijoms  
   - **Tapatybės apsauga**: Rizika pagrįsta sąlyginė prieiga ir automatizuotas grėsmių reagavimas

## 12. **Nuolatinė saugumo evoliucija**

**Buvimas naujausiu:**
   - **Specifikacijos stebėjimas**: Reguliarus MCP specifikacijos atnaujinimų ir saugumo gairių pokyčių peržiūra  
   - **Grėsmių žvalgyba**: DI specifinių grėsmių srautų ir kompromiso indikatorių integracija  
   - **Saugumo bendruomenės įsitraukimas**: Aktyvus dalyvavimas MCP saugumo bendruomenėje ir pažeidžiamumų atskleidimo programose

**Adaptuojamas saugumas:**
   - **Mašininio mokymosi saugumas**: Naudokite ML pagrįstą anomalijų aptikimą naujiems atakų modeliams identifikuoti  
   - **Prognozuojamoji saugumo analizė**: Įgyvendinkite prognozinius modelius proaktyviam grėsmių identifikavimui  
   - **Saugumo automatizavimas**: Automatizuoti saugumo politikos atnaujinimai remiantis grėsmių žvalgyba ir specifikacijos pokyčiais

---

## **Kritiniai saugumo ištekliai**

### **Oficiali MCP dokumentacija**
- [MCP specifikacija (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP saugumo geriausios praktikos](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP autorizacijos specifikacija](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft saugumo sprendimai**
- [Microsoft užklausų skydai](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID saugumas](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Saugumo standartai**
- [OAuth 2.0 saugumo geriausios praktikos (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 dideliems kalbos modeliams](https://genai.owasp.org/)
- [NIST DI rizikos valdymo sistema](https://www.nist.gov/itl/ai-risk-management-framework)

### **Įgyvendinimo vadovai**
- [Azure API Management MCP autentifikacijos vartai](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID su MCP serveriais](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Saugumo pranešimas**: MCP saugumo praktikos sparčiai keičiasi. Visada tikrinkite pagal esamą [MCP specifikaciją](https://spec.modelcontextprotocol.io/) ir [oficialią saugumo dokumentaciją](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) prieš įgyvendinimą.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->