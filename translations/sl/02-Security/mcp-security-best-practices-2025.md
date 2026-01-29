# Najboljše varnostne prakse MCP - posodobitev december 2025

> **Pomembno**: Ta dokument odraža najnovejše varnostne zahteve [MCP specifikacije 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) in uradne [MCP varnostne najboljše prakse](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Vedno se sklicujte na trenutno specifikacijo za najsodobnejša navodila.

## Ključne varnostne prakse za implementacije MCP

Model Context Protocol uvaja edinstvene varnostne izzive, ki presegajo tradicionalno varnost programske opreme. Te prakse obravnavajo tako temeljne varnostne zahteve kot tudi specifične grožnje MCP, vključno z vbrizgavanjem pozivov, zastrupljanjem orodij, prevzemom sej, težavami z zmedeno pooblaščenko in ranljivostmi pri prenosu žetonov.

### **OBVEZNE varnostne zahteve**

**Kritične zahteve iz MCP specifikacije:**

### **OBVEZNE varnostne zahteve**

**Kritične zahteve iz MCP specifikacije:**

> **NE SME**: MCP strežniki **NE SMEJO** sprejemati nobenih žetonov, ki niso izrecno izdani za MCP strežnik  
>  
> **MORA**: MCP strežniki, ki izvajajo avtorizacijo, **MORAJO** preveriti VSE dohodne zahteve  
>  
> **NE SME**: MCP strežniki **NE SMEJO** uporabljati sej za avtentikacijo  
>  
> **MORA**: MCP proxy strežniki, ki uporabljajo statične ID-je odjemalcev, **MORAJO** pridobiti soglasje uporabnika za vsakega dinamično registriranega odjemalca

---

## 1. **Varnost žetonov in avtentikacija**

**Nadzor avtentikacije in avtorizacije:**  
   - **Stroga revizija avtorizacije**: Izvedite obsežne preglede logike avtorizacije MCP strežnika, da zagotovite dostop do virov samo za namenjene uporabnike in odjemalce  
   - **Integracija zunanjih ponudnikov identitete**: Uporabljajte uveljavljene ponudnike identitete, kot je Microsoft Entra ID, namesto lastnih rešitev avtentikacije  
   - **Preverjanje občinstva žetonov**: Vedno preverite, da so žetoni izrecno izdani za vaš MCP strežnik – nikoli ne sprejemajte žetonov od zgornjih nivojev  
   - **Pravilno upravljanje življenjskega cikla žetonov**: Uvedite varno rotacijo žetonov, politike poteka in preprečevanje ponovnih napadov z žetoni

**Zaščiteno shranjevanje žetonov:**  
   - Uporabljajte Azure Key Vault ali podobne varne shrambe za vse skrivnosti  
   - Uvedite šifriranje žetonov tako v mirovanju kot med prenosom  
   - Redna rotacija poverilnic in nadzor nepooblaščenega dostopa

## 2. **Upravljanje sej in varnost prenosa**

**Varnostne prakse sej:**  
   - **Kriptografsko varni ID-ji sej**: Uporabljajte varne, nedeterministične ID-je sej, ustvarjene z varnimi generatorji naključnih števil  
   - **Povezava z uporabnikom**: Povežite ID-je sej z identitetami uporabnikov z uporabo formatov, kot je `<user_id>:<session_id>`, da preprečite zlorabo sej med uporabniki  
   - **Upravljanje življenjskega cikla sej**: Uvedite pravilno potekanje, rotacijo in razveljavitev za omejitev ranljivosti  
   - **Zahteva HTTPS/TLS**: Obvezna uporaba HTTPS za vso komunikacijo, da preprečite prestrezanje ID-jev sej

**Varnost sloja prenosa:**  
   - Konfigurirajte TLS 1.3, kjer je mogoče, z ustreznim upravljanjem certifikatov  
   - Uvedite pinning certifikatov za kritične povezave  
   - Redna rotacija certifikatov in preverjanje veljavnosti

## 3. **Zaščita pred grožnjami, specifičnimi za AI** 🤖

**Obramba pred vbrizgavanjem pozivov:**  
   - **Microsoft Prompt Shields**: Uporabite AI Prompt Shields za napredno zaznavanje in filtriranje zlonamernih navodil  
   - **Čiščenje vhodnih podatkov**: Preverite in očistite vse vnose, da preprečite napade z vbrizgavanjem in težave z zmedeno pooblaščenko  
   - **Meje vsebine**: Uporabite ločila in sisteme označevanja podatkov za razlikovanje med zaupanja vrednimi navodili in zunanjimi vsebinami

**Preprečevanje zastrupljanja orodij:**  
   - **Preverjanje metapodatkov orodij**: Uvedite preverjanja integritete definicij orodij in spremljajte nepričakovane spremembe  
   - **Dinamično spremljanje orodij**: Spremljajte vedenje med izvajanjem in nastavite opozorila za nepričakovane vzorce izvajanja  
   - **Delovni tokovi odobritve**: Zahtevajte izrecno uporabniško odobritev za spremembe orodij in zmogljivosti

## 4. **Nadzor dostopa in dovoljenja**

**Načelo najmanjših privilegijev:**  
   - MCP strežnikom dodelite samo minimalna dovoljenja, potrebna za predvideno funkcionalnost  
   - Uvedite nadzor dostopa na podlagi vlog (RBAC) z natančnimi dovoljenji  
   - Redni pregledi dovoljenj in stalno spremljanje za eskalacijo privilegijev

**Nadzor dovoljenj med izvajanjem:**  
   - Uporabite omejitve virov za preprečevanje napadov izčrpavanja virov  
   - Uporabite izolacijo kontejnerjev za okolja izvajanja orodij  
   - Uvedite dostop po potrebi za administrativne funkcije

## 5. **Varnost vsebine in spremljanje**

**Izvedba varnosti vsebine:**  
   - **Integracija Azure Content Safety**: Uporabite Azure Content Safety za zaznavanje škodljive vsebine, poskusov jailbreaka in kršitev politik  
   - **Analiza vedenja**: Uvedite spremljanje vedenja med izvajanjem za zaznavanje anomalij v MCP strežniku in izvajanju orodij  
   - **Celovito beleženje**: Beležite vse poskuse avtentikacije, klice orodij in varnostne dogodke z varnim, neizbrisnim shranjevanjem

**Neprekinjeno spremljanje:**  
   - Opozorila v realnem času za sumljive vzorce in nepooblaščene poskuse dostopa  
   - Integracija s sistemi SIEM za centralizirano upravljanje varnostnih dogodkov  
   - Redni varnostni pregledi in penetracijsko testiranje implementacij MCP

## 6. **Varnost dobavne verige**

**Preverjanje komponent:**  
   - **Skeniranje odvisnosti**: Uporabite avtomatizirano skeniranje ranljivosti za vse programske odvisnosti in AI komponente  
   - **Preverjanje izvora**: Preverite izvor, licenciranje in integriteto modelov, virov podatkov in zunanjih storitev  
   - **Podpisani paketi**: Uporabite kriptografsko podpisane pakete in preverite podpise pred namestitvijo

**Varen razvojni proces:**  
   - **GitHub Advanced Security**: Uvedite skeniranje skrivnosti, analizo odvisnosti in statično analizo CodeQL  
   - **Varnost CI/CD**: Integrirajte varnostno preverjanje skozi avtomatizirane procese nameščanja  
   - **Integriteta artefaktov**: Uvedite kriptografsko preverjanje nameščenih artefaktov in konfiguracij

## 7. **Varnost OAuth in preprečevanje zmedene pooblaščenke**

**Izvedba OAuth 2.1:**  
   - **Izvedba PKCE**: Uporabite Proof Key for Code Exchange (PKCE) za vse zahteve avtorizacije  
   - **Izrecno soglasje**: Pridobite uporabniško soglasje za vsakega dinamično registriranega odjemalca, da preprečite napade z zmedeno pooblaščenko  
   - **Preverjanje URI za preusmeritev**: Uvedite strogo preverjanje URI-jev za preusmeritev in identifikatorjev odjemalcev

**Varnost proxyja:**  
   - Preprečite obhod avtorizacije z izkoriščanjem statičnih ID-jev odjemalcev  
   - Uvedite ustrezne delovne tokove soglasij za dostop do API-jev tretjih oseb  
   - Spremljajte krajo avtorizacijskih kod in nepooblaščen dostop do API-jev

## 8. **Odgovor na incidente in okrevanje**

**Hitre odzivne zmogljivosti:**  
   - **Avtomatiziran odziv**: Uvedite avtomatizirane sisteme za rotacijo poverilnic in zajezitev groženj  
   - **Postopki povrnitve**: Zmožnost hitrega vračanja na znane dobre konfiguracije in komponente  
   - **Forenzične zmogljivosti**: Podrobni revizijski sledovi in beleženje za preiskavo incidentov

**Komunikacija in koordinacija:**  
   - Jasni postopki eskalacije za varnostne incidente  
   - Integracija z organizacijskimi ekipami za odziv na incidente  
   - Redne simulacije varnostnih incidentov in vaje za mizo

## 9. **Skladnost in upravljanje**

**Regulatorna skladnost:**  
   - Zagotovite, da implementacije MCP izpolnjujejo industrijske zahteve (GDPR, HIPAA, SOC 2)  
   - Uvedite klasifikacijo podatkov in nadzor zasebnosti za obdelavo podatkov AI  
   - Vzdržujte celovito dokumentacijo za revizijo skladnosti

**Upravljanje sprememb:**  
   - Formalni postopki varnostnih pregledov za vse spremembe MCP sistema  
   - Nadzor različic in delovni tokovi odobritve za spremembe konfiguracij  
   - Redne ocene skladnosti in analiza vrzeli

## 10. **Napredni varnostni nadzori**

**Arhitektura ničelnega zaupanja:**  
   - **Nikoli ne zaupaj, vedno preverjaj**: Neprestano preverjanje uporabnikov, naprav in povezav  
   - **Mikrosegmentacija**: Natančni omrežni nadzori, ki izolirajo posamezne komponente MCP  
   - **Pogojni dostop**: Nadzor dostopa na podlagi tveganja, prilagojen trenutnemu kontekstu in vedenju

**Zaščita aplikacij med izvajanjem:**  
   - **Runtime Application Self-Protection (RASP)**: Uporabite RASP tehnike za zaznavanje groženj v realnem času  
   - **Nadzor zmogljivosti aplikacij**: Spremljajte anomalije zmogljivosti, ki lahko kažejo na napade  
   - **Dinamične varnostne politike**: Uvedite varnostne politike, ki se prilagajajo glede na trenutno varnostno stanje

## 11. **Integracija Microsoftovega varnostnega ekosistema**

**Celovita Microsoftova varnost:**  
   - **Microsoft Defender for Cloud**: Upravljanje varnostnega stanja v oblaku za delovne obremenitve MCP  
   - **Azure Sentinel**: Nativne SIEM in SOAR zmogljivosti v oblaku za napredno zaznavanje groženj  
   - **Microsoft Purview**: Upravljanje podatkov in skladnost za AI delovne tokove in vire podatkov

**Upravljanje identitet in dostopa:**  
   - **Microsoft Entra ID**: Upravljanje identitet podjetja s politikami pogojevanega dostopa  
   - **Privileged Identity Management (PIM)**: Dostop po potrebi in delovni tokovi odobritve za administrativne funkcije  
   - **Zaščita identitete**: Pogojevan dostop na podlagi tveganja in avtomatiziran odziv na grožnje

## 12. **Neprekinjena varnostna evolucija**

**Ostanite na tekočem:**  
   - **Spremljanje specifikacij**: Redni pregledi posodobitev MCP specifikacij in sprememb varnostnih navodil  
   - **Obveščanje o grožnjah**: Integracija virov groženj, specifičnih za AI, in indikatorjev kompromisa  
   - **Sodelovanje v varnostni skupnosti**: Aktivno sodelovanje v MCP varnostni skupnosti in programih razkritja ranljivosti

**Prilagodljiva varnost:**  
   - **Varnost strojnega učenja**: Uporaba ML za zaznavanje anomalij in prepoznavanje novih vzorcev napadov  
   - **Napovedna varnostna analitika**: Uvedba napovednih modelov za proaktivno prepoznavanje groženj  
   - **Avtomatizacija varnosti**: Avtomatizirane posodobitve varnostnih politik na podlagi obveščanja o grožnjah in sprememb specifikacij

---

## **Kritični varnostni viri**

### **Uradna MCP dokumentacija**  
- [MCP specifikacija (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP varnostne najboljše prakse](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP specifikacija avtorizacije](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  

### **Microsoftove varnostne rešitve**  
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [Microsoft Entra ID varnost](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)  
- [GitHub Advanced Security](https://github.com/security/advanced-security)  

### **Varnostni standardi**  
- [OAuth 2.0 varnostne najboljše prakse (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 za velike jezikovne modele](https://genai.owasp.org/)  
- [NIST okvir za upravljanje tveganj AI](https://www.nist.gov/itl/ai-risk-management-framework)  

### **Vodniki za implementacijo**  
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)  
- [Microsoft Entra ID z MCP strežniki](https://den.dev/blog/mcp-server-auth-entra-id-session/)  

---

> **Varnostno obvestilo**: Varnostne prakse MCP se hitro razvijajo. Vedno preverite trenutno [MCP specifikacijo](https://spec.modelcontextprotocol.io/) in [uradno varnostno dokumentacijo](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) pred implementacijo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->