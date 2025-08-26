<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "057dd5cc6bea6434fdb788e6c93f3f3d",
  "translation_date": "2025-08-26T16:37:58+00:00",
  "source_file": "02-Security/mcp-security-best-practices-2025.md",
  "language_code": "lt"
}
-->
# MCP Saugumo Geriausios Praktikos - 2025 m. rugpjūčio atnaujinimas

> **Svarbu**: Šis dokumentas atspindi naujausius [MCP Specifikacijos 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/) saugumo reikalavimus ir oficialias [MCP Saugumo Geriausias Praktikas](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices). Visada remkitės dabartine specifikacija, kad gautumėte naujausią informaciją.

## Esminės Saugumo Praktikos MCP Įgyvendinimui

Model Context Protocol (MCP) kelia unikalius saugumo iššūkius, kurie peržengia tradicinio programinės įrangos saugumo ribas. Šios praktikos apima tiek pagrindinius saugumo reikalavimus, tiek MCP specifines grėsmes, tokias kaip prompt injekcija, įrankių užnuodijimas, sesijų užgrobimas, supainioto tarpininko problemos ir tokenų perdavimo pažeidžiamumai.

### **PRIVALOMI Saugumo Reikalavimai**

**Kritiniai Reikalavimai iš MCP Specifikacijos:**

> **NEGALI**: MCP serveriai **NEGALI** priimti jokių tokenų, kurie nebuvo aiškiai išduoti MCP serveriui  
> 
> **PRIVALOMA**: MCP serveriai, įgyvendinantys autorizaciją, **PRIVALOMA** patikrinti VISUS gaunamus užklausimus  
>  
> **NEGALI**: MCP serveriai **NEGALI** naudoti sesijų autentifikacijai  
>
> **PRIVALOMA**: MCP proxy serveriai, naudojantys statinius klientų ID, **PRIVALOMA** gauti vartotojo sutikimą kiekvienam dinamiškai registruotam klientui  

---

## 1. **Tokenų Saugumas ir Autentifikacija**

**Autentifikacijos ir Autorizacijos Kontrolė:**
   - **Griežta Autorizacijos Peržiūra**: Atlikite išsamias MCP serverio autorizacijos logikos peržiūras, kad užtikrintumėte, jog tik numatyti vartotojai ir klientai gali pasiekti resursus  
   - **Išorinių Tapatybės Teikėjų Integracija**: Naudokite patikimus tapatybės teikėjus, tokius kaip Microsoft Entra ID, vietoj savarankiškos autentifikacijos kūrimo  
   - **Tokenų Auditorijos Patikra**: Visada patikrinkite, ar tokenai buvo aiškiai išduoti jūsų MCP serveriui – niekada nepriimkite aukštesnės grandies tokenų  
   - **Tinkamas Tokenų Gyvavimo Ciklas**: Įgyvendinkite saugų tokenų rotavimą, galiojimo politiką ir užkirskite kelią tokenų pakartotiniam naudojimui  

**Apsaugotas Tokenų Saugojimas:**
   - Naudokite Azure Key Vault ar panašias saugias kredencialų saugyklas visoms paslaptims  
   - Įgyvendinkite tokenų šifravimą tiek ramybės būsenoje, tiek perduodant  
   - Reguliariai keiskite kredencialus ir stebėkite neautorizuotą prieigą  

## 2. **Sesijų Valdymas ir Transporto Saugumas**

**Saugios Sesijų Praktikos:**
   - **Kriptografiškai Saugūs Sesijų ID**: Naudokite saugius, nedeterministinius sesijų ID, generuojamus naudojant saugius atsitiktinių skaičių generatorius  
   - **Vartotojo Specifinis Susiejimas**: Susiekite sesijų ID su vartotojo tapatybėmis naudodami formatus, pvz., `<user_id>:<session_id>`, kad išvengtumėte tarp vartotojų sesijų piktnaudžiavimo  
   - **Sesijų Gyvavimo Ciklo Valdymas**: Įgyvendinkite tinkamą galiojimo pabaigą, rotavimą ir anuliavimą, kad sumažintumėte pažeidžiamumo langus  
   - **HTTPS/TLS Privalomumas**: Privalomas HTTPS visam bendravimui, kad būtų išvengta sesijų ID perėmimo  

**Transporto Sluoksnio Saugumas:**
   - Konfigūruokite TLS 1.3, kai tik įmanoma, su tinkamu sertifikatų valdymu  
   - Įgyvendinkite sertifikatų prisegimą kritinėms jungtims  
   - Reguliariai keiskite sertifikatus ir tikrinkite jų galiojimą  

## 3. **AI-Specifinių Grėsmių Apsauga** 🤖

**Prompt Injekcijos Gynyba:**
   - **Microsoft Prompt Shields**: Naudokite AI Prompt Shields pažangiam kenkėjiškų instrukcijų aptikimui ir filtravimui  
   - **Įvesties Valymas**: Patikrinkite ir išvalykite visas įvestis, kad išvengtumėte injekcijos atakų ir supainioto tarpininko problemų  
   - **Turinio Ribos**: Naudokite ribotuvus ir duomenų žymėjimo sistemas, kad atskirtumėte patikimas instrukcijas nuo išorinio turinio  

**Įrankių Užnuodijimo Prevencija:**
   - **Įrankių Metaduomenų Patikra**: Įgyvendinkite įrankių apibrėžimų integralumo patikras ir stebėkite netikėtus pokyčius  
   - **Dinaminis Įrankių Stebėjimas**: Stebėkite vykdymo elgseną ir nustatykite įspėjimus dėl netikėtų vykdymo modelių  
   - **Patvirtinimo Procesai**: Reikalaukite aiškaus vartotojo patvirtinimo įrankių modifikacijoms ir galimybių pakeitimams  

## 4. **Prieigos Kontrolė ir Leidimai**

**Mažiausios Būtinos Prieigos Principas:**
   - Suteikite MCP serveriams tik minimalias reikalingas teises numatytai funkcionalumui  
   - Įgyvendinkite vaidmenimis pagrįstą prieigos kontrolę (RBAC) su smulkiomis leidimų detalėmis  
   - Reguliariai peržiūrėkite leidimus ir nuolat stebėkite privilegijų eskalavimą  

**Leidimų Kontrolė Vykdymo Metu:**
   - Taikykite resursų limitus, kad išvengtumėte resursų išsekimo atakų  
   - Naudokite konteinerių izoliaciją įrankių vykdymo aplinkoms  
   - Įgyvendinkite laikiną prieigą administracinėms funkcijoms  

## 5. **Turinio Saugumas ir Stebėjimas**

**Turinio Saugumo Įgyvendinimas:**
   - **Azure Content Safety Integracija**: Naudokite Azure Content Safety kenksmingo turinio, jailbreak bandymų ir politikos pažeidimų aptikimui  
   - **Elgsenos Analizė**: Įgyvendinkite vykdymo elgsenos stebėjimą, kad aptiktumėte anomalijas MCP serverio ir įrankių vykdyme  
   - **Išsamus Registravimas**: Registruokite visus autentifikacijos bandymus, įrankių iškvietimus ir saugumo įvykius su saugiu, nepažeidžiamu saugojimu  

**Nuolatinis Stebėjimas:**
   - Realaus laiko įspėjimai apie įtartinus modelius ir neautorizuotus prieigos bandymus  
   - Integracija su SIEM sistemomis centralizuotam saugumo įvykių valdymui  
   - Reguliarūs saugumo auditai ir MCP įgyvendinimų įsiskverbimo testavimas  

## 6. **Tiekimo Grandinės Saugumas**

**Komponentų Patikra:**
   - **Priklausomybių Nuskaitymas**: Naudokite automatizuotą pažeidžiamumų nuskaitymą visoms programinės įrangos priklausomybėms ir AI komponentams  
   - **Kilmės Patikra**: Patikrinkite modelių, duomenų šaltinių ir išorinių paslaugų kilmę, licencijavimą ir integralumą  
   - **Pasirašyti Paketai**: Naudokite kriptografiškai pasirašytus paketus ir patikrinkite parašus prieš diegimą  

**Saugus Kūrimo Vamzdynas:**
   - **GitHub Advanced Security**: Įgyvendinkite paslapčių nuskaitymą, priklausomybių analizę ir CodeQL statinę analizę  
   - **CI/CD Saugumas**: Integruokite saugumo patikras visame automatizuotame diegimo procese  
   - **Artefaktų Integralumas**: Įgyvendinkite kriptografinę diegiamų artefaktų ir konfigūracijų patikrą  

## 7. **OAuth Saugumas ir Supainioto Tarpininko Prevencija**

**OAuth 2.1 Įgyvendinimas:**
   - **PKCE Įgyvendinimas**: Naudokite Proof Key for Code Exchange (PKCE) visoms autorizacijos užklausoms  
   - **Aiškus Sutikimas**: Gaukite vartotojo sutikimą kiekvienam dinamiškai registruotam klientui, kad išvengtumėte supainioto tarpininko atakų  
   - **Peradresavimo URI Patikra**: Įgyvendinkite griežtą peradresavimo URI ir klientų identifikatorių patikrą  

**Proxy Saugumas:**
   - Užkirskite kelią autorizacijos apeigoms per statinių klientų ID išnaudojimą  
   - Įgyvendinkite tinkamus sutikimo procesus trečiųjų šalių API prieigai  
   - Stebėkite autorizacijos kodų vagystes ir neautorizuotą API prieigą  

## 8. **Incidentų Reagavimas ir Atkūrimas**

**Greito Reagavimo Galimybės:**
   - **Automatizuotas Reagavimas**: Įgyvendinkite automatizuotas sistemas kredencialų rotavimui ir grėsmių suvaldymui  
   - **Atstatymo Procedūros**: Galimybė greitai grįžti prie patikrintų gerų konfigūracijų ir komponentų  
   - **Teismo Ekspertizės Galimybės**: Išsamūs audito pėdsakai ir registravimas incidentų tyrimui  

**Komunikacija ir Koordinavimas:**
   - Aiškios eskalavimo procedūros saugumo incidentams  
   - Integracija su organizacijos incidentų reagavimo komandomis  
   - Reguliarios saugumo incidentų simuliacijos ir mokymai  

## 9. **Atitiktis ir Valdymas**

**Reguliacinė Atitiktis:**
   - Užtikrinkite, kad MCP įgyvendinimai atitiktų pramonės reikalavimus (GDPR, HIPAA, SOC 2)  
   - Įgyvendinkite duomenų klasifikavimo ir privatumo kontrolę AI duomenų apdorojimui  
   - Palaikykite išsamią dokumentaciją atitikties auditams  

**Pakeitimų Valdymas:**
   - Formalūs saugumo peržiūros procesai visiems MCP sistemos pakeitimams  
   - Versijų kontrolė ir patvirtinimo procesai konfigūracijų pakeitimams  
   - Reguliarios atitikties vertinimai ir spragų analizė  

## 10. **Pažangios Saugumo Kontrolės**

**Zero Trust Architektūra:**
   - **Niekada Nepasitikėkite, Visada Tikrinkite**: Nuolatinis vartotojų, įrenginių ir jungčių tikrinimas  
   - **Mikrosegmentacija**: Smulkios tinklo kontrolės, izoliuojančios atskirus MCP komponentus  
   - **Sąlyginė Prieiga**: Rizika pagrįsta prieigos kontrolė, prisitaikanti prie dabartinio konteksto ir elgsenos  

**Apsauga Vykdymo Metu:**
   - **Runtime Application Self-Protection (RASP)**: Naudokite RASP metodus realaus laiko grėsmių aptikimui  
   - **Programų Veikimo Stebėjimas**: Stebėkite veikimo anomalijas, kurios gali rodyti atakas  
   - **Dinaminės Saugumo Politikos**: Įgyvendinkite saugumo politikas, kurios prisitaiko prie dabartinio grėsmių kraštovaizdžio  

## 11. **Microsoft Saugumo Ekosistemos Integracija**

**Išsamus Microsoft Saugumas:**
   - **Microsoft Defender for Cloud**: Debesų saugumo pozicijos valdymas MCP darbo krūviams  
   - **Azure Sentinel**: Debesų gimtoji SIEM ir SOAR galimybės pažangiam grėsmių aptikimui  
   - **Microsoft Purview**: Duomenų valdymas ir atitiktis AI darbo srautams ir duomenų šaltiniams  

**Tapatybės ir Prieigos Valdymas:**
   - **Microsoft Entra ID**: Įmonės tapatybės valdymas su sąlyginės prieigos politikomis  
   - **Privileged Identity Management (PIM)**: Laiku suteikiama prieiga ir patvirtinimo procesai administracinėms funkcijoms  
   - **Tapatybės Apsauga**: Rizika pagrįsta sąlyginė prieiga ir automatizuotas grėsmių reagavimas  

## 12. **Nuolatinė Saugumo Evoliucija**

**Buvimas Atnaujintu:**
   - **Specifikacijos Stebėjimas**: Reguliari MCP specifikacijos atnaujinimų ir saugumo gairių peržiūra  
   - **Grėsmių Žvalgyba**: AI specifinių grėsmių srautų ir kompromisų indikatorių integracija  
   - **Saugumo Bendruomenės Dalyvavimas**: Aktyvus dalyvavimas MCP saugumo bendruomenėje ir pažeidžiamumų atskleidimo programose  

**Prisitaikantis Saugumas:**
   - **Mašininio Mokymosi Saugumas**: Naudokite ML pagrįstą anomalijų aptikimą naujų atakų modelių identifikavimui  
   - **Prognozuojamoji Saugumo Analitika**: Įgyvendinkite prognozuojamus modelius proaktyviam grėsmių identifikavimui  
   - **Saugumo Automatizavimas**: Automatizuoti saugumo politikos atnaujinimai, pagrįsti grėsmių žvalgyba ir specifikacijos pokyčiais  

---

## **Kritiniai Saugumo Ištekliai**

### **Oficiali MCP Dokumentacija**
- [MCP Specifikacija (2025-06-18)](https://spec.modelcontextprotocol.io/specification/2025-06-18/)  
- [MCP Saugumo Geriausios Praktikos](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices)  
- [MCP Autorizacijos Specifikacija](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)  

### **Microsoft Saugumo Sprendimai**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [Microsoft Entra ID Saugumas](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)  
- [GitHub Advanced Security](https://github.com/security/advanced-security)  

### **Saugumo Standartai**
- [OAuth 2.0 Saugumo Geriausios Praktikos (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 Dideliems Kalbos Modeliams](https://genai.owasp.org/)  
- [NIST AI Rizikos Valdymo Sistema](https://www.nist.gov/itl/ai-risk-management-framework)  

### **Įgyvendinimo Gidai**
- [Azure API Management MCP Autentifikacijos Vartai](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)  
- [Microsoft Entra ID su MCP Serveriais](https://den.dev/blog/mcp-server-auth-entra-id-session/)  

---

> **Saugumo Pranešimas**: MCP saugumo praktikos greitai evoliucionuoja. Visada patikrinkite pagal dabartinę [MCP specifikaciją](https://spec.modelcontextprotocol.io/) ir [oficialią saugumo dokumentaciją](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices) prieš įgyvendinimą.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.