# MCP Biztonsági Legjobb Gyakorlatok - 2025 Decemberi Frissítés

> **Fontos**: Ez a dokumentum tükrözi a legfrissebb [MCP Specifikáció 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) biztonsági követelményeit és a hivatalos [MCP Biztonsági Legjobb Gyakorlatokat](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Mindig a jelenlegi specifikációra hivatkozzon a legfrissebb útmutatásért.

## Alapvető Biztonsági Gyakorlatok MCP Implementációkhoz

A Model Context Protocol egyedi biztonsági kihívásokat vezet be, amelyek túlmutatnak a hagyományos szoftverbiztonságon. Ezek a gyakorlatok mind az alapvető biztonsági követelményeket, mind az MCP-specifikus fenyegetéseket kezelik, beleértve a prompt injekciót, eszközmérgezést, munkamenet eltérítést, összezavarodott helyettes problémákat és token átviteli sérülékenységeket.

### **KÖTELEZŐ Biztonsági Követelmények**

**Kritikus követelmények az MCP specifikációból:**

### **KÖTELEZŐ Biztonsági Követelmények**

**Kritikus követelmények az MCP specifikációból:**

> **NEM SZABAD**: Az MCP szerverek **NEM SZABAD** elfogadniuk olyan tokeneket, amelyeket nem kifejezetten az MCP szerver számára bocsátottak ki  
>  
> **KÖTELEZŐ**: Az MCP szerverek, amelyek engedélyezést valósítanak meg, **KÖTELEZŐ** minden bejövő kérést ellenőrizniük  
>  
> **NEM SZABAD**: Az MCP szerverek **NEM SZABAD** munkameneteket használniuk hitelesítésre  
>  
> **KÖTELEZŐ**: Az MCP proxy szerverek, amelyek statikus kliensazonosítókat használnak, **KÖTELEZŐ** megszerezniük a felhasználói hozzájárulást minden dinamikusan regisztrált klienshez

---

## 1. **Token Biztonság & Hitelesítés**

**Hitelesítési & Engedélyezési Ellenőrzések:**
   - **Alapos Engedélyezési Áttekintés**: Végezzen átfogó auditokat az MCP szerver engedélyezési logikáján, hogy csak a szándékolt felhasználók és kliensek férhessenek hozzá az erőforrásokhoz  
   - **Külső Identitásszolgáltató Integráció**: Használjon bevált identitásszolgáltatókat, mint a Microsoft Entra ID, ahelyett, hogy egyedi hitelesítést valósítana meg  
   - **Token Célközönség Érvényesítés**: Mindig ellenőrizze, hogy a tokeneket kifejezetten az Ön MCP szervere számára bocsátották-e ki – soha ne fogadjon el upstream tokeneket  
   - **Megfelelő Token Élettartam**: Valósítson meg biztonságos token forgatást, lejárati szabályokat, és akadályozza meg a token visszajátszásos támadásokat

**Védett Token Tárolás:**
   - Használjon Azure Key Vault-ot vagy hasonló biztonságos hitelesítő tárolókat minden titokhoz  
   - Valósítson meg titkosítást a tokenek számára mind tároláskor, mind átvitelkor  
   - Rendszeres hitelesítő forgatás és jogosulatlan hozzáférés figyelése

## 2. **Munkamenet Kezelés & Átvitel Biztonság**

**Biztonságos Munkamenet Gyakorlatok:**
   - **Kriptográfiailag Biztonságos Munkamenet Azonosítók**: Használjon biztonságos, nem determinisztikus munkamenet azonosítókat, amelyeket biztonságos véletlenszám-generátorokkal hoznak létre  
   - **Felhasználóhoz Kötött Munkamenet**: Kösse a munkamenet azonosítókat a felhasználói identitásokhoz olyan formátumokkal, mint `<user_id>:<session_id>`, hogy megakadályozza a felhasználók közötti munkamenet visszaélést  
   - **Munkamenet Élettartam Kezelés**: Valósítson meg megfelelő lejáratot, forgatást és érvénytelenítést a sérülékenységi ablakok korlátozására  
   - **HTTPS/TLS Kötelező Használat**: Kötelező HTTPS minden kommunikációhoz a munkamenet azonosítók elfogásának megakadályozására

**Átvitel Réteg Biztonság:**
   - Konfigurálja a TLS 1.3-at, ahol lehetséges, megfelelő tanúsítványkezeléssel  
   - Valósítson meg tanúsítvány rögzítést kritikus kapcsolatokhoz  
   - Rendszeres tanúsítvány forgatás és érvényesség ellenőrzés

## 3. **AI-Specifikus Fenyegetések Elleni Védelem** 🤖

**Prompt Injekció Védelem:**
   - **Microsoft Prompt Shields**: Telepítsen AI Prompt Shields-t a rosszindulatú utasítások fejlett felismerésére és szűrésére  
   - **Bemenet Tisztítás**: Érvényesítse és tisztítsa meg az összes bemenetet az injekciós támadások és az összezavarodott helyettes problémák megelőzésére  
   - **Tartalom Határok**: Használjon elválasztó és adatjelölő rendszereket a megbízható utasítások és külső tartalom megkülönböztetésére

**Eszközmérgezés Megelőzése:**
   - **Eszköz Metaadat Érvényesítés**: Valósítson meg integritás ellenőrzéseket az eszközdefiníciókra, és figyelje a váratlan változásokat  
   - **Dinamikus Eszközfigyelés**: Figyelje a futásidejű viselkedést, és állítson be riasztásokat váratlan végrehajtási mintákra  
   - **Jóváhagyási Munkafolyamatok**: Kérjen kifejezett felhasználói jóváhagyást az eszköz módosításaihoz és képességváltozásaihoz

## 4. **Hozzáférés-vezérlés & Jogosultságok**

**Legkisebb Jogosultság Elve:**
   - Csak a szükséges minimális jogosultságokat adja meg az MCP szervereknek a szándékolt funkciókhoz  
   - Valósítson meg szerepalapú hozzáférés-vezérlést (RBAC) finomhangolt jogosultságokkal  
   - Rendszeres jogosultság felülvizsgálatok és folyamatos megfigyelés a jogosultságok növekedésének megelőzésére

**Futásidejű Jogosultság Ellenőrzések:**
   - Alkalmazzon erőforrás-korlátokat az erőforrás kimerüléses támadások megelőzésére  
   - Használjon konténer izolációt az eszközök futtatási környezetéhez  
   - Valósítson meg just-in-time hozzáférést adminisztratív funkciókhoz

## 5. **Tartalom Biztonság & Megfigyelés**

**Tartalom Biztonság Megvalósítása:**
   - **Azure Content Safety Integráció**: Használja az Azure Content Safety-t káros tartalmak, jailbreak kísérletek és szabályzati megsértések felismerésére  
   - **Viselkedéselemzés**: Valósítson meg futásidejű viselkedésfigyelést az MCP szerver és eszközök végrehajtásának anomáliáinak felismerésére  
   - **Átfogó Naplózás**: Naplózza az összes hitelesítési kísérletet, eszköz meghívást és biztonsági eseményt biztonságos, hamisításbiztos tárolóban

**Folyamatos Megfigyelés:**
   - Valós idejű riasztás gyanús mintákra és jogosulatlan hozzáférési kísérletekre  
   - Integráció SIEM rendszerekkel a központosított biztonsági eseménykezeléshez  
   - Rendszeres biztonsági auditok és penetrációs tesztek az MCP implementációkon

## 6. **Ellátási Lánc Biztonság**

**Komponens Ellenőrzés:**
   - **Függőség Vizsgálat**: Használjon automatizált sérülékenységvizsgálatot minden szoftverfüggőségre és AI komponensre  
   - **Eredet Érvényesítés**: Ellenőrizze a modellek, adatforrások és külső szolgáltatások eredetét, licencelését és integritását  
   - **Aláírt Csomagok**: Használjon kriptográfiailag aláírt csomagokat, és ellenőrizze az aláírásokat telepítés előtt

**Biztonságos Fejlesztési Folyamat:**
   - **GitHub Advanced Security**: Valósítson meg titokkeresést, függőség elemzést és CodeQL statikus elemzést  
   - **CI/CD Biztonság**: Integrálja a biztonsági ellenőrzéseket az automatizált telepítési folyamatokba  
   - **Artefakt Integritás**: Valósítson meg kriptográfiai ellenőrzést a telepített artefaktumok és konfigurációk számára

## 7. **OAuth Biztonság & Összezavarodott Helyettes Megelőzés**

**OAuth 2.1 Megvalósítás:**
   - **PKCE Megvalósítás**: Használja a Proof Key for Code Exchange (PKCE) mechanizmust minden engedélyezési kéréshez  
   - **Kifejezett Hozzájárulás**: Szerezze be a felhasználói hozzájárulást minden dinamikusan regisztrált klienshez az összezavarodott helyettes támadások megelőzésére  
   - **Redirect URI Érvényesítés**: Valósítson meg szigorú érvényesítést a redirect URI-kra és kliensazonosítókra

**Proxy Biztonság:**
   - Megakadályozza az engedélyezés megkerülését statikus kliensazonosító kihasználásával  
   - Valósítson meg megfelelő hozzájárulási munkafolyamatokat harmadik fél API hozzáféréshez  
   - Figyelje az engedélyezési kód lopást és jogosulatlan API hozzáférést

## 8. **Incidens Válasz & Helyreállítás**

**Gyors Reagálási Képességek:**
   - **Automatizált Válasz**: Valósítson meg automatizált rendszereket hitelesítő forgatásra és fenyegetés korlátozására  
   - **Visszaállítási Eljárások**: Képesség gyors visszaállításra ismert jó konfigurációkra és komponensekre  
   - **Forenzikus Képességek**: Részletes audit nyomvonalak és naplózás az incidens kivizsgáláshoz

**Kommunikáció & Koordináció:**
   - Világos eszkalációs eljárások biztonsági incidensekhez  
   - Integráció a szervezeti incidens válasz csapatokkal  
   - Rendszeres biztonsági incidens szimulációk és asztali gyakorlatok

## 9. **Megfelelőség & Irányítás**

**Szabályozói Megfelelőség:**
   - Biztosítsa, hogy az MCP implementációk megfeleljenek az iparági követelményeknek (GDPR, HIPAA, SOC 2)  
   - Valósítson meg adat osztályozást és adatvédelmi kontrollokat az AI adatfeldolgozáshoz  
   - Tartson fenn átfogó dokumentációt a megfelelőségi auditokhoz

**Változáskezelés:**
   - Formális biztonsági felülvizsgálati folyamatok minden MCP rendszer módosításhoz  
   - Verziókezelés és jóváhagyási munkafolyamatok konfigurációs változtatásokhoz  
   - Rendszeres megfelelőségi értékelések és hiányelemzések

## 10. **Fejlett Biztonsági Ellenőrzések**

**Zero Trust Architektúra:**
   - **Sose Bízz, Mindig Ellenőrizz**: Folyamatos felhasználó-, eszköz- és kapcsolatellenőrzés  
   - **Mikro-szegmentáció**: Finom hálózati kontrollok az egyes MCP komponensek izolálására  
   - **Feltételes Hozzáférés**: Kockázatalapú hozzáférés-vezérlés, amely alkalmazkodik az aktuális kontextushoz és viselkedéshez

**Futásidejű Alkalmazásvédelem:**
   - **Runtime Application Self-Protection (RASP)**: Telepítsen RASP technikákat valós idejű fenyegetés felismeréshez  
   - **Alkalmazás Teljesítmény Monitorozás**: Figyelje a teljesítmény anomáliákat, amelyek támadásokra utalhatnak  
   - **Dinamikus Biztonsági Szabályzatok**: Valósítson meg olyan biztonsági szabályzatokat, amelyek az aktuális fenyegetési helyzethez igazodnak

## 11. **Microsoft Biztonsági Ökoszisztéma Integráció**

**Átfogó Microsoft Biztonság:**
   - **Microsoft Defender for Cloud**: Felhőbiztonsági helyzetkezelés MCP munkaterhelésekhez  
   - **Azure Sentinel**: Felhőalapú SIEM és SOAR képességek fejlett fenyegetés felismeréshez  
   - **Microsoft Purview**: Adatirányítás és megfelelőség AI munkafolyamatokhoz és adatforrásokhoz

**Identitás & Hozzáférés Kezelés:**
   - **Microsoft Entra ID**: Vállalati identitáskezelés feltételes hozzáférési szabályokkal  
   - **Privileged Identity Management (PIM)**: Just-in-time hozzáférés és jóváhagyási munkafolyamatok adminisztratív funkciókhoz  
   - **Identitás Védelem**: Kockázatalapú feltételes hozzáférés és automatizált fenyegetés válasz

## 12. **Folyamatos Biztonsági Fejlődés**

**Naprakészség:**
   - **Specifikáció Figyelés**: Rendszeres áttekintés az MCP specifikáció frissítéseiről és biztonsági útmutatás változásairól  
   - **Fenyegetés Intelligencia**: AI-specifikus fenyegetési hírcsatornák és kompromittálódási indikátorok integrálása  
   - **Biztonsági Közösségi Részvétel**: Aktív részvétel az MCP biztonsági közösségben és sérülékenység bejelentési programokban

**Adaptív Biztonság:**
   - **Gépi Tanulás Biztonság**: ML-alapú anomália felismerés új támadási minták azonosítására  
   - **Előrejelző Biztonsági Analitika**: Prediktív modellek alkalmazása proaktív fenyegetés azonosításhoz  
   - **Biztonsági Automatizálás**: Automatizált biztonsági szabályzat frissítések fenyegetés intelligencia és specifikáció változások alapján

---

## **Kritikus Biztonsági Források**

### **Hivatalos MCP Dokumentáció**
- [MCP Specifikáció (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Biztonsági Legjobb Gyakorlatok](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Engedélyezési Specifikáció](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft Biztonsági Megoldások**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Biztonság](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Biztonsági Szabványok**
- [OAuth 2.0 Biztonsági Legjobb Gyakorlatok (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Nagy Nyelvi Modellekhez](https://genai.owasp.org/)
- [NIST AI Kockázatkezelési Keretrendszer](https://www.nist.gov/itl/ai-risk-management-framework)

### **Implementációs Útmutatók**
- [Azure API Management MCP Hitelesítési Átjáró](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID MCP Szerverekkel](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Biztonsági Figyelmeztetés**: Az MCP biztonsági gyakorlatok gyorsan fejlődnek. Mindig ellenőrizze a jelenlegi [MCP specifikáció](https://spec.modelcontextprotocol.io/) és a [hivatalos biztonsági dokumentáció](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) alapján a megvalósítás előtt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->