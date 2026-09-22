# Najboljše varnostne prakse MCP - posodobitev september 2026

> **Pomembno:** Ta dokument odraža
> [Specifikacijo MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> in uradne
> [Najboljše varnostne prakse MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## 🏔️ Praktična varnostna usposabljanja

Za praktične izkušnje z implementacijo priporočamo **[Delo na delavnici MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - celovita vodenje ekspedicija za varovanje MCP strežnikov v Azure. Delavnica pokriva vseh 10 glavnih tveganj OWASP MCP s pristopom "ranljivost → izkoriščanje → popravilo → validacija".

Vse prakse v tem dokumentu so usklajene s **[Vodičem za varnost MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/)** za smernice specifične za Azure.

## Osnovne varnostne prakse za implementacije MCP

Protokol Model Context uvaja edinstvene varnostne izzive, ki segajo
preko tradicionalne varnosti programske opreme. Te prakse obravnavajo temeljne
zahteve in specifične grožnje MCP, vključno z injiciranjem pozivov, zastrupitvijo orodij, prevzemom stanja,
problematiko zmedene delegacije in ranljivosti pri prehodu žetonov.


### **OBVEZNE varnostne zahteve** 

**Kritične zahteve iz specifikacije MCP:**

> **NE SMEJO:** MCP strežniki **NE SMEJO** sprejemati žetonov, ki niso bili izrecno izdani za MCP strežnik
> 
> **MORAJO:** MCP strežniki, ki izvajajo avtorizacijo, **MORAJO** preveriti VSE vhodne zahteve
>  
> **NE SMEJO:** MCP strežniki **NE SMEJO** uporabljati sej za avtentikacijo
>
> **MORAJO:** MCP proxy strežniki, ki uporabljajo statični ID odjemalca tretje osebe, **MORAJO**
> pridobiti soglasje za vsakega MCP odjemalca pred prenosom avtorizacije

---

## 1. **Varnost in avtentikacija žetonov**

**Kontrole avtentikacije in avtorizacije:**
   - **Natančen pregled avtorizacije**: Izvedite celovite revizije logike avtorizacije MCP strežnika, da zagotovite, da imajo dostop samo namenjeni uporabniki in odjemalci
   - **Integracija zunanjih ponudnikov identitete**: Uporabite uveljavljene ponudnike identitete, kot je Microsoft Entra ID, namesto lastnih avtentikacijskih rešitev
   - **Preverjanje občinstva žetona**: Vedno preverite, da so žetoni izrecno izdani za vaš MCP strežnik - nikoli ne sprejemajte žetonov od virov zgoraj
   - **Pravilno upravljanje življenjskega cikla žetonov**: Izvajajte varno rotacijo žetonov, politiko poteka veljavnosti in preprečujte ponovne napade z žetoni

**Zaščitena shramba žetonov:**
   - Uporabljajte Azure Key Vault ali podobne varne shrambene rešitve za vse skrivnosti
   - Izvajajte šifriranje žetonov med mirovanjem in prenosom
   - Redna rotacija poverilnic in nadzor nepooblaščenega dostopa

## 2. **Varnost statusov in transporta**

**Prakse za varno upravljanje stanja aplikacije:**

- **Neprozorne ročice stanja**: Uporabljajte varne, nedeterministične ročice za
   stanje aplikacije, ki sega preko zahtev
- **Povezanost z uporabnikom**: Povežite ročice strežniško z avtenticiranim
   uporabnikom in zavrnite meduporabniško ponovno uporabo
- **Upravljanje življenjskega cikla**: Potek in preklic ročic, da omejite ranljivost
   v določenem časovnem oknu
- **Avtorizacija za vsako zahtevo**: Nikoli ne obravnavajte ročice stanja kot avtentikacije;
   avtorizirajte vsako zahtevo, ki jo predloži

**Varnost transportne plasti:**

- Zahtevajte HTTPS za oddaljene HTTP prenose v produkciji
- Uporabljajte izolacijo procesov in poverilnice okolja za lokalne stdio strežnike
- Konfigurirajte sodoben TLS z ustrezno rotacijo in validacijo certifikatov

## 3. **Zaščita pred grožnjami specifičnimi za AI** 🤖

**Obramba proti injiciranju pozivov:**
   - **Microsoft Prompt Shields**: Uporabite AI Prompt Shields za napredno zaznavanje in filtriranje zlonamernih navodil
   - **Čiščenje vhodnih podatkov**: Preverite in očistite vse vhodne podatke, da preprečite injiciranje in težave zmedene delegacije
   - **Meje vsebine**: Uporabite ločilne in sistem za označevanje podatkov za razlikovanje zaupanja vrednih navodil od zunanje vsebine

**Preprečevanje zastrupitve orodij:**
   - **Validacija metapodatkov orodij**: Izvajajte integriteto preverjanja definicij orodij in spremljajte nepričakovane spremembe
   - **Dinamično spremljanje orodij**: Spremljajte obnašanje med izvajanjem in vzpostavite opozorilne mehanizme za nepričakovane vzorce
   - **Potrditveni postopki**: Zahtevajte izrecno odobritev uporabnika za spremembe orodij in zmogljivosti

## 4. **Kontrola dostopa in dovoljenja**

**Načelo najmanjših privilegijev:**
   - Dodelite MCP strežnikom samo minimalna dovoljenja, potrebna za namenjeno funkcionalnost
   - Izvajajte nadzor dostopa na podlagi vlog (RBAC) s finimi dovoljenji
   - Redni pregledi dovoljenj in neprekinjeno spremljanje eskalacije privilegijev

**Kontrole dovoljenj med izvajanjem:**
   - Uporabljajte omejitve virov za preprečevanje napadov z izčrpanjem virov
   - Uporabljajte izolacijo kontejnerjev za okolja izvajanja orodij  
   - Izvajajte dostop po potrebi za administrativne funkcije

## 5. **Varnost vsebine in nadzor**

**Izvedba varnosti vsebine:**
   - **Integracija Azure Content Safety**: Uporabite Azure Content Safety za odkrivanje škodljive vsebine, poskusov jailbreak in kršitev politik
   - **Analiza vedenja**: Izvajajte nadzor vedenja med izvajanjem za odkrivanje anomalij v izvajanju MCP strežnikov in orodij
   - **Celovito beleženje**: Zabeležite vse poskuse avtentikacije, klice orodij in varnostne dogodke z varnim in nepreklicnim shranjevanjem

**Neprekinjeno spremljanje:**
   - Opozorila v realnem času za sumljive vzorce in nepooblaščene dostopne poskuse  
   - Integracija s sistemi SIEM za centralizirano upravljanje varnostnih dogodkov
   - Redne varnostne revizije in penetracijsko testiranje MCP implementacij

## 6. **Varnost dobavne verige**

**Preverjanje komponent:**
   - **Skeniranje odvisnosti**: Uporabite avtomatizirano pregledovanje ranljivosti za vse programske odvisnosti in AI komponente
   - **Validacija izvora**: Preverite izvor, licenciranje in integriteto modelov, podatkovnih virov in zunanjih storitev
   - **Podpisani paketi**: Uporabljajte kriptografsko podpisane pakete in preverite podpise pred nameščanjem

**Varen razvojni proces:**
   - **Napredna varnost GitHub**: Izvajajte skeniranje skrivnosti, analizo odvisnosti in statično analizo CodeQL
   - **Varnost CI/CD**: Integrirajte preverjanje varnosti skozi avtomatizirane postopke nameščanja
   - **Integriteta artefaktov**: Izvajajte kriptografsko preverjanje nameščenih artefaktov in konfiguracij

## 7. **Varnost OAuth in preprečevanje zmede delegata**

**Implementacija OAuth 2.1:**
   - **Izvedba PKCE**: Uporabite Proof Key for Code Exchange (PKCE) za vse zahteve po avtorizaciji
    - **Registracija odjemalcev**: Prednost dajte dokumentom metapodatkov Client ID ali
       predregistraciji; zastarelo dinamično registracijo odjemalcev uporabljajte zgolj
       kot varnostno rezervno možnost kompatibilnosti
    - **Izrecno soglasje**: MCP proxy-ji, ki uporabljajo statični ID odjemalca tretje osebe, morajo
       pridobiti soglasje za vsakega MCP odjemalca pred prenosom avtorizacije
   - **Validacija URI za preusmeritev**: Izvedite strogo preverjanje URI za preusmeritev in identifikatorjev odjemalcev

**Varnost proxy strežnika:**
   - Preprečite zaobidenje avtorizacije z izkoriščanjem statičnega ID odjemalca
   - Izvedite pravilne postopke za pridobivanje soglasja za dostop do API-jev tretjih oseb
   - Spremljajte krajo avtorizacijskih kod in nepooblaščen dostop API-jev

## 8. **Odgovor na incidente in okrevanje**

**Hitre odzivne zmogljivosti:**
   - **Avtomatiziran odziv**: Uvedite avtomatizirane sisteme za rotacijo poverilnic in zajezitev groženj
   - **Postopki povračila**: Sposobnost hitrega vračanja na znane dobre konfiguracije in komponente
   - **Forenzične zmogljivosti**: Podrobni revizijski zapisi in beleženje za preiskave incidentov

**Komunikacija in koordinacija:**
   - Jasni postopki eskalacije varnostnih incidentov
   - Integracija z ekipami za odziv na incidente v organizaciji
   - Redne simulacije varnostnih incidentov in vaje za mizo

## 9. **Skladnost in upravljanje**

**Regulativna skladnost:**
   - Zagotovite, da implementacije MCP izpolnjujejo zahteve specifične za industrijo (GDPR, HIPAA, SOC 2)
   - Izvajajte klasifikacijo podatkov in nadzore zasebnosti za obdelavo AI podatkov
   - Vzdržujte celovito dokumentacijo za skladnost z revizijo

**Upravljanje sprememb:**
   - Formalni postopki varnostnih pregledov za vse spremembe MCP sistema
   - Upravljanje različic in postopki odobritve za spremembe konfiguracije
   - Redne ocene skladnosti in analize vrzeli

## 10. **Napredne varnostne kontrole**

**Arhitektura z ničelnim zaupanjem:**
   - **Nikoli ne zaupaj, vedno preverjaj**: Neprestano preverjanje uporabnikov, naprav in povezav
   - **Mikrosegmentacija**: Natančen mrežni nadzor, ki izolira posamezne komponente MCP
   - **Pogojni dostop**: Dostopne kontrole na podlagi tveganja, ki se prilagajajo trenutnemu kontekstu in vedenju

**Zaščita aplikacij med izvajanjem:**
   - **Samopreskrba aplikacij med izvajanjem (RASP)**: Uvedite RASP metode za zaznavanje groženj v realnem času
   - **Nadzor zmogljivosti aplikacij**: Spremljajte anomalije zmogljivosti, ki lahko kažejo na napade
   - **Dinamične varnostne politike**: Uvedite varnostne politike, ki se prilagajajo glede na trenutno krajino groženj

## 11. **Integracija Microsoft varnostnega ekosistema**

**Celovita Microsoft varnost:**
   - **Microsoft Defender za oblak**: Upravljanje varnostnega stanja oblaka za delovne obremenitve MCP
   - **Azure Sentinel**: Nativna SIEM in SOAR zmogljivost v oblaku za napredno zaznavanje groženj
   - **Microsoft Purview**: Upravljanje podatkov in skladnost za AI delovne procese in podatkovne vire

**Upravljanje identitete in dostopa:**
   - **Microsoft Entra ID**: Upravljanje podjetniške identitete s pogojnimi dostopnimi politikami
   - **Upravljanje privilegirane identitete (PIM)**: Dostop po potrebi in postopki odobritve za administrativne funkcije
   - **Zaščita identitete**: Pogojni dostop na podlagi tveganja in avtomatiziran odziv na grožnje

## 12. **Neprekinjeni razvoj varnosti**

**Ostanite na tekočem:**
   - **Spremljanje specifikacij**: Redni pregledi posodobitev MCP specifikacij in sprememb varnostnih smernic
   - **Obveščanje o grožnjah**: Integracija virov groženj specifičnih za AI in indikatorjev kompromisa
   - **Sodelovanje v varnostni skupnosti**: Aktivno sodelovanje v MCP varnostni skupnosti in programih za razkritje ranljivosti

**Prilagodljiva varnost:**
   - **Varnost strojnega učenja**: Uporaba detekcije anomalij na osnovi ML za prepoznavanje novih vzorcev napadov
   - **Napovedna varnostna analitika**: Uvedba napovednih modelov za proaktivno identifikacijo groženj
   - **Varnostna avtomatizacija**: Avtomatizirane posodobitve varnostnih politik na podlagi obveščanja o grožnjah in sprememb specifikacij

---

## **Kritični varnostni viri**

### **Uradna MCP dokumentacija**
- [Specifikacija MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Najboljše varnostne prakse MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Specifikacija avtorizacije MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP varnostni viri**
- [Vodič za varnost MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/) - Celovit OWASP MCP Top 10 z implementacijo za Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Uradna OWASP MCP varnostna tveganja
- [Delavnica MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktično usposabljanje varnosti za MCP na Azure

### **Microsoft varnostne rešitve**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID varnost](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Microsoft GitHub napredna varnost](https://github.com/security/advanced-security)

### **Varnostni standardi**
- [Najboljše varnostne prakse OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 za velike jezikovne modele](https://genai.owasp.org/)
- [NIST okvir za upravljanje tveganj AI](https://www.nist.gov/itl/ai-risk-management-framework)

### **Vodiči za implementacijo**
- [Vrata za avtentikacijo MCP Azure API Management](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID z MCP strežniki](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Varnostno obvestilo:** Varnostne prakse MCP se hitro razvijajo. Vedno preverite
> zadnjo [specifikacijo MCP](https://modelcontextprotocol.io/specification/2026-07-28/)
> in [uradno varnostno dokumentacijo](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> pred implementacijo.

## Kaj sledi

- Preberite: [MCP varnostne kontrole](./mcp-security-controls.md)
- Vrni se na: [Pregled varnostnega modula](./README.md)
- Nadaljujte na: [Modul 3: Uvod](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->