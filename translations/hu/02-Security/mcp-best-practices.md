# MCP Biztonsági legjobb gyakorlatok - 2026 szeptemberi frissítés

Ez az átfogó útmutató ismerteti az alapvető biztonsági legjobb gyakorlatokat a
Model Context Protocol (MCP) rendszerek megvalósításához, az
**MCP Specifikáció 2026-07-28** és a jelenlegi ipari szabványok alapján. Ezek a
gyakorlatok a hagyományos biztonsági aggályokat és az MCP telepítésekre jellemző,
mesterséges intelligenciára (AI) specifikus fenyegetéseket egyaránt kezelik.

## Kritikus biztonsági követelmények

### Kötelező biztonsági ellenőrzések (KÖTELEZŐ követelmények)

1. **Token érvényesítés**: Az MCP szervereknek **NEM SZABAD** elfogadniuk olyan tokeneket, amelyeket kifejezetten nem az adott MCP szerver számára bocsátottak ki  
2. **Engedélyezés ellenőrzése**: Az engedélyezést végrehajtó MCP szervereknek **MINDEN** bejövő kérést ellenőrizniük kell, és **NEM SZABAD** munkameneteket használniuk az hitelesítéshez  
3. **Felhasználói hozzájárulás**: Az MCP proxy szervereknek, amelyek statikus harmadik féltől származó kliensazonosítókat használnak, **kifejezett hozzájárulást kell szerezniük minden MCP kliens esetében az engedélyezési folyamat továbbítása előtt**  
4. **Állapotfoglaló biztonság**: Az MCP szerverek **NEM SZABAD** az alkalmazásállapot foglalójának birtoklását hitelesítésként kezelniük, és **MINDEN** kérést engedélyezniük kell, amely azzal él  



## Alapvető biztonsági gyakorlatok

### 1. Bemenet érvényesítés és tisztítás
- **Átfogó bemenet érvényesítés**: Érvényesítsen és tisztítson minden bemenetet, hogy megakadályozza az injekciós támadásokat, a zavart megbízó problémákat és a prompt injekciós sebezhetőségeket  
- **Paraméter séma betartása**: Alkalmazzon szigorú JSON séma érvényesítést minden eszközparaméter és API bemenet esetén  
- **Tartalomszűrés**: Használja a Microsoft Prompt Shields és az Azure Content Safety eszközöket a kártékony tartalom szűrésére a promptokban és válaszokban  
- **Kimenet tisztítása**: Érvényesítse és tisztítsa az összes modell kimenetet, mielőtt azt felhasználók vagy további rendszerek számára bemutatná  

### 2. Hitelesítés és engedélyezés kiválósága  
- **Külső identitásszolgáltatók**: Bízza a hitelesítést megalapozott identitásszolgáltatókra (Microsoft Entra ID, OAuth 2.1 szolgáltatók), ahelyett, hogy egyéni hitelesítést valósítana meg  
- **Kliens regisztráció**: Előnyben részesítse a kliensidentitás metaadat dokumentumokat vagy előregisztrációt; az elavult Dinamikus Kliens Regisztrációt csak kompatibilitási célokra használja  
- **Finoman hangolt jogosultságok**: Valósítson meg részletes, eszközspecifikus jogosultságokat a legkisebb jogosultság elve alapján  
- **Token életciklus-kezelés**: Használjon rövid élettartamú hozzáférési tokeneket biztonságos forgatással és megfelelő célközönség ellenőrzéssel  
- **Többtényezős hitelesítés (MFA)**: Minden adminisztratív hozzáférés és érzékeny művelet esetén kötelező az MFA  

### 3. Biztonságos kommunikációs protokollok
- **Transzport réteg biztonság (TLS)**: Távoli HTTP MCP kommunikációkhoz használjon HTTPS-t megfelelő tanúsítványellenőrzéssel; helyi stdio szerverekhez használjon folyamat izolációt és környezeti hitelesítő adatokat  


- **Végeztől végig titkosítás (E2E)**: Különösen érzékeny adatforgalom és adattárolás esetén valósítson meg további titkosítási rétegeket  
- **Tanúsítvány-kezelés**: Fenntartsa a megfelelő tanúsítvány életciklus kezelést automatizált megújítási folyamatokkal  
- **Protokoll verzió betartás**: Használja az MCP `2026-07-28` verziót, minden kérésben hozza magával a kötelező verzió metaadatot, és utasítsa el a nem támogatott verziókat  


### 4. Fejlett sebességkorlátozás és erőforrás-védelem
- **Többrétegű sebességkorlátozás**: Valósítson meg sebességkorlátozást felhasználó, hitelesítő adat, művelet, eszköz és erőforrás szerint az visszaélések megelőzésére  

- **Adaptív sebességkorlátozás**: Használjon gépi tanulási alapú sebességkorlátozást, amely alkalmazkodik a használati mintákhoz és a fenyegetési jelekhez  
- **Erőforrás-kvóta kezelés**: Állítson be megfelelő korlátokat a számítási erőforrásokra, memóriára és végrehajtási időre  
- **DDoS védelem**: Telepítsen átfogó DDoS védelmi és forgalomelemzési rendszereket  

### 5. Átfogó naplózás és megfigyelés
- **Strukturált audit naplózás**: Valósítson meg részletes, kereshető naplókat minden MCP műveletről, eszköz végrehajtásról és biztonsági eseményről  
- **Valósidejű biztonsági megfigyelés**: Telepítsen SIEM rendszereket AI-alapú anomália detektálással MCP munkákhoz  
- **Adatvédelmi szempontból megfelelős naplózás**: Naplózza a biztonsági eseményeket miközben betartja az adatvédelmi előírásokat és szabályozásokat  
- **Incidens reagálás integráció**: Kapcsolja össze a naplózó rendszereket automatizált incidens reagálási munkafolyamatokkal  

### 6. Fejlett biztonságos tárolási gyakorlatok
- **Hardveres biztonsági modulok (HSM)**: Használjon HSM-alapú kulcstárolást (Azure Key Vault, AWS CloudHSM) kritikus kriptográfiai műveletekhez  
- **Titkosítási kulcs kezelése**: Alkalmazzon megfelelő kulcs forgatást, elkülönítést és hozzáférés-vezérlést a titkosítási kulcsok esetén  
- **Titkos kezelése**: Tároljon minden API kulcsot, tokent és hitelesítő adatot dedikált titokkezelő rendszerekben  
- **Adat osztályozás**: Osztályozza az adatokat érzékenységük szerint és alkalmazzon megfelelő védelmi intézkedéseket  

### 7. Fejlett token kezelés
- **Token átvitel megakadályozása**: Kifejezetten tiltsa meg azokat a token átvitel mintákat, amelyek megkerülik a biztonsági ellenőrzéseket  
- **Célközönség érvényesítés**: Mindig ellenőrizze, hogy a token célközönség követelmények megfelelnek az MCP szerver azonosítónak  
- **Jogosultság követelmény-alapú engedélyezés**: Valósítson meg részletes engedélyezést token követelések és felhasználói attribútumok alapján  
- **Token kötés**: Ellenőrizze, hogy a tokenek az MCP cél erőforráshoz szólnak, és  
	kösse az alkalmazásállapot foglalókat szerveroldalon a hitelesített félhez  

### 8. Biztonságos alkalmazásállapot

- **Kriptográfiai állapot foglalók**: Generáljon átlátszatlan, nem-determinisztikus foglalókat  
	az állapothoz, amely a kérések között megmarad  
- **Felhasználó-specifikus kötés**: Kösse minden foglalót szerveroldalon a hitelesített félhez; ne bízzon a kliens által megadott felhasználói azonosítóban  
- **Életciklus ellenőrzések**: Járjon el a foglalók lejáratával és visszavonásával, és határozza meg, hogyan álljanak helyre a hívók az elavult állapotból  
- **Kérésenkénti engedélyezés**: Az engedélyezést ellenőrizze újra, amikor egy foglaló bemutatásra kerül; a foglaló egy név, nem hitelesítő adat  




### 9. AI-specifikus biztonsági ellenőrzések
- **Prompt injekció elleni védelem**: Alkalmazza a Microsoft Prompt Shields használatával a fókuszált, határoló és adatjelölési technikákat  
- **Eszköz mérgezés megelőzés**: Érvényesítse az eszköz metaadatokat, figyelje a dinamikus változásokat, és ellenőrizze az eszköz integritását  
- **Modell kimenet érvényesítés**: Szűrje le a modell kimeneteket potenciális adat szivárgás, káros tartalom vagy biztonsági szabályszegések ellen  
- **Kontextus ablak védelme**: Valósítson meg ellenőrzéseket a kontextus ablak mérgezés és manipulációs támadások megelőzésére  

### 10. Eszköz végrehajtási biztonság
- **Végrehajtás izolálása**: Futassa az eszközök végrehajtását konténerizált, elszigetelt környezetben erőforrás korlátokkal  
- **Jogosultság szétválasztás**: Az eszközöket a minimálisan szükséges jogosultságokkal futtassa, és különálló szolgáltatói fiókokkal  
- **Hálózati elszigetelés**: Valósítson meg hálózati szeparációt az eszköz végrehajtási környezetekhez  
- **Végrehajtás megfigyelés**: Figyelje az eszköz végrehajtását anomáliák, erőforrás használat és biztonsági szabálysértések szempontjából  

### 11. Folyamatos biztonsági érvényesítés
- **Automatizált biztonsági tesztelés**: Integrálja a biztonsági tesztelést a CI/CD folyamatokba eszközökkel, mint a GitHub Advanced Security  
- **Sebezhetőség-kezelés**: Rendszeresen vizsgálja át az összes függőséget, beleértve az AI modelleket és külső szolgáltatásokat  
- **Penetrációs tesztelés**: Végeztessen rendszeres biztonsági értékeléseket, amelyek kifejezetten az MCP megvalósításokat célozzák  
- **Biztonsági kódfelülvizsgálatok**: Kötelezze el a biztonsági felülvizsgálatokat minden MCP-vel kapcsolatos kódváltoztatás esetén  

### 12. Ellátási lánc biztonság AI számára
- **Összetevő ellenőrzés**: Ellenőrizze az összes AI összetevő (modellek, beágyazások, API-k) eredetét, integritását és biztonságát  
- **Függőség kezelés**: Tartson naprakész nyilvántartást minden szoftver- és AI függőségről sebezhetőségi nyomon követéssel  
- **Meglátott tárak**: Használjon igazolt, megbízható forrásokat minden AI modellhez, könyvtárhoz és eszközhöz  
- **Ellátási lánc megfigyelése**: Folyamatosan figyelje az AI szolgáltatókat és modell tárhelyeket kompromittálódás ellen  

## Fejlett biztonsági minták

### Zéró bizalom architektúra MCP számára
- **Soha ne bízzon, mindig ellenőrizzen**: Valósítson meg folyamatos ellenőrzést minden MCP résztvevő esetében  
- **Mikroseparáció**: Szigeteljen el MCP komponenseket granuláris hálózati és identitás vezérlésekkel  
- **Feltételes hozzáférés**: Kockázatalapú hozzáférésvezérléseket alkalmazzon, amelyek alkalmazkodnak a környezethez és viselkedéshez  
- **Folyamatos kockázatértékelés**: Dinamikusan értékelje a biztonsági állapotot a jelenlegi fenyegetési jelek alapján  

### Adatvédelmi szempontokat érvényesítő AI megvalósítás
- **Adatminimalizálás**: Csak a szükséges minimum adatot tegye elérhetővé minden MCP művelethez  
- **Differenciális adatvédelem**: Alkalmazzon adatvédelmet biztosító technikákat az érzékeny adatfeldolgozás során  
- **Homomorf titkosítás**: Használjon fejlett titkosítási eljárásokat titkosított adatok biztonságos feldolgozásához  
- **Federált tanulás**: Valósítson meg elosztott tanulási megközelítéseket, amelyek megőrzik az adat helyi jellegét és védelmét  

### Incidens kezelési eljárások AI rendszerek számára
- **AI-specifikus incidens eljárások**: Fejlesszen ki olyan incidens kezelési eljárásokat, amelyek kifejezetten az AI és MCP specifikus fenyegetésekre fókuszálnak  
- **Automatizált válasz**: Valósítson meg automatizált tartózkodási és helyreállítási lépéseket gyakori AI biztonsági incidensekre  
- **Igazságügyi felkészültség**: Tartsa fenn a jogi eljárásokhoz szükséges igazságügyi felkészültséget AI rendszer kompromittálódása és adatvédelmi incidensek esetén  
- **Helyreállítási eljárások**: Állítson fel eljárásokat AI modell mérgezésből, prompt injekciós támadásokból és szolgáltatás kompromittálódásból való felépülésre  

## Megvalósítási források és szabványok

### 🏔️ Gyakorlati biztonsági képzés
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Átfogó gyakorlati műhely az MCP szerverek biztonságossá tételéhez az Azure környezetben  
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Referencia architektúra és az OWASP MCP Top 10 megvalósítási útmutatója  

### Hivatalos MCP dokumentáció
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Jelenlegi MCP protokoll specifikáció  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Hivatalos biztonsági útmutató  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP engedélyezési minták  
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Transzport követelmények  

### Microsoft biztonsági megoldások
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Fejlett prompt injekció elleni védelem  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Átfogó AI tartalomszűrés  
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Vállalati identitás- és hozzáférés-kezelés  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Biztonságos titok- és hitelesítő adat kezelés  
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Ellátási lánc és kód biztonsági elemzés  

### Biztonsági szabványok és keretrendszerek
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Jelenlegi OAuth biztonsági útmutató  
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Webalkalmazás biztonsági kockázatok  
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-specifikus biztonsági kockázatok  
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Átfogó AI kockázatkezelés  
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Információbiztonsági irányítási rendszerek  

### Megvalósítási útmutatók és oktatóanyagok
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Vállalati hitelesítési minták  
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Identitásszolgáltató integráció  
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Token kezelési legjobb gyakorlatok  
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Fejlett titkosítási minták  

### Fejlett biztonsági források
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Biztonságos fejlesztési gyakorlatok  
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-specifikus biztonsági tesztelés  
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI fenyegetés modellezési módszertan  
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Adatvédelmet megőrző AI technikák  

### Megfelelőség és irányítás
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Adatvédelmi megfelelőség AI rendszerekben  
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Felelős AI megvalósítás  
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Biztonsági ellenőrzések AI szolgáltatók számára  
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Egészségügyi AI megfelelőségi követelmények  

### DevSecOps és automatizálás
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Biztonságos AI fejlesztési folyamatok  
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Folyamatos biztonsági érvényesítés  
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Biztonságos infrastruktúra telepítés  
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AI munkaterhelés konténerizálás biztonsága  

### Megfigyelés és incidens reagálás  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Átfogó megfigyelési megoldások  
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-specifikus incidens eljárások  
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Biztonsági információ- és eseménykezelés  

- [Fenyegetési hírszerzés az MI-hez](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - MI fenyegetési hírszerzési források

## 🔄 Folyamatos fejlesztés

### Maradj naprakész a változó szabványokkal
- **MCP specifikáció frissítések**: Kövesd az MCP hivatalos specifikációváltozásait és biztonsági értesítéseit
- **Fenyegetési hírszerzés**: Iratkozz fel MI biztonsági fenyegetési hírcsatornákra és sérülékenységi adatbázisokra  
- **Közösségi részvétel**: Vegyél részt az MCP biztonsági közösségi beszélgetéseken és munkacsoportokon
- **Rendszeres értékelés**: Végezzen negyedéves biztonsági helyzetértékelést és ennek megfelelően frissítsd a gyakorlatokat

### Hozzájárulás az MCP biztonsághoz
- **Biztonsági kutatás**: Vegyél részt az MCP biztonsági kutatásokban és sérülékenység-bejelentési programokban
- **Legjobb gyakorlat megosztása**: Oszd meg a biztonsági megvalósításokat és tanulságokat a közösséggel
- **Szabványfejlesztés**: Vegyél részt az MCP specifikáció fejlesztésében és biztonsági szabványok kialakításában
- **Eszközfejlesztés**: Fejlessz és ossz meg biztonsági eszközöket és könyvtárakat az MCP ökoszisztéma számára

---

*Ez a dokumentum az MCP biztonsági legjobb gyakorlatokat tükrözi 2026. szeptember 9-én,
az MCP `2026-07-28` specifikációja alapján. A biztonsági gyakorlatokat rendszeresen felül kell vizsgálni,
ahogy a protokoll és a fenyegetési környezet változik.*

## Mi következik

- Olvasd el: [MCP biztonsági legjobb gyakorlatok](./mcp-security-best-practices.md)
- Térj vissza ide: [Biztonsági modul áttekintése](./README.md)
- Folytasd itt: [3. modul: Kezdő lépések](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->