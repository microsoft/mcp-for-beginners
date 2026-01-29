# MCP Biztonsági Legjobb Gyakorlatok 2025

Ez az átfogó útmutató a Model Context Protocol (MCP) rendszerek megvalósításához szükséges alapvető biztonsági legjobb gyakorlatokat ismerteti a legfrissebb **MCP Specifikáció 2025-11-25** és a jelenlegi iparági szabványok alapján. Ezek a gyakorlatok mind a hagyományos biztonsági kérdéseket, mind az MCP telepítésekre jellemző, mesterséges intelligenciára specifikus fenyegetéseket kezelik.

## Kritikus Biztonsági Követelmények

### Kötelező Biztonsági Intézkedések (MUST Követelmények)

1. **Token Érvényesítés**: Az MCP szerverek **NEM FOGADHATNAK EL** olyan tokeneket, amelyeket nem kifejezetten az MCP szerver számára bocsátottak ki  
2. **Engedélyezés Ellenőrzése**: Az engedélyezést megvalósító MCP szerverek **MINDEN** bejövő kérést ellenőrizniük kell, és **NEM HASZNÁLHATNAK** munkameneteket hitelesítésre  
3. **Felhasználói Hozzájárulás**: Az MCP proxy szerverek, amelyek statikus kliensazonosítókat használnak, **KÖTELESEK** minden dinamikusan regisztrált kliens esetén kifejezett felhasználói hozzájárulást szerezni  
4. **Biztonságos Munkamenet Azonosítók**: Az MCP szerverek **KÖTELESEK** kriptográfiailag biztonságos, nem determinisztikus munkamenet-azonosítókat használni, amelyeket biztonságos véletlenszám-generátorokkal hoznak létre

## Alapvető Biztonsági Gyakorlatok

### 1. Bemenet Érvényesítés és Tisztítás
- **Átfogó Bemenet Érvényesítés**: Minden bemenetet ellenőrizni és tisztítani kell az injekciós támadások, a zavart helyettesítő problémák és a prompt injekciós sebezhetőségek megelőzése érdekében  
- **Paraméter Sémák Betartása**: Szigorú JSON séma érvényesítést kell alkalmazni minden eszközparaméter és API bemenet esetén  
- **Tartalomszűrés**: Microsoft Prompt Shields és Azure Content Safety használata a rosszindulatú tartalmak szűrésére a promptokban és válaszokban  
- **Kimenet Tisztítása**: Minden modellkimenetet ellenőrizni és tisztítani kell, mielőtt azt a felhasználóknak vagy további rendszereknek bemutatnák

### 2. Hitelesítés és Engedélyezés Kiválósága  
- **Külső Identitásszolgáltatók**: A hitelesítést megbízható identitásszolgáltatókra (Microsoft Entra ID, OAuth 2.1 szolgáltatók) kell delegálni, nem szabad egyedi hitelesítést megvalósítani  
- **Finomhangolt Jogosultságok**: Eszközspecifikus, részletes jogosultságokat kell alkalmazni a legkisebb jogosultság elve alapján  
- **Token Élettartam Kezelés**: Rövid élettartamú hozzáférési tokeneket kell használni biztonságos forgatással és megfelelő célközönség-ellenőrzéssel  
- **Többlépcsős Hitelesítés**: Minden adminisztratív hozzáféréshez és érzékeny művelethez MFA-t kell követelni

### 3. Biztonságos Kommunikációs Protokollok
- **Transport Layer Security**: Minden MCP kommunikációhoz HTTPS/TLS 1.3-at kell használni megfelelő tanúsítvány-ellenőrzéssel  
- **Végpontok Közötti Titkosítás**: Külön titkosítási rétegeket kell alkalmazni a rendkívül érzékeny adatok átvitelére és tárolására  
- **Tanúsítványkezelés**: Megfelelő tanúsítvány-élettartam-kezelést kell fenntartani automatizált megújítási folyamatokkal  
- **Protokoll Verzió Betartása**: A jelenlegi MCP protokoll verziót (2025-11-25) kell használni megfelelő verzióegyeztetéssel

### 4. Fejlett Korlátozás és Erőforrás Védelem
- **Többrétegű Korlátozás**: Felhasználói, munkamenet, eszköz és erőforrás szinten kell korlátozásokat alkalmazni a visszaélések megelőzésére  
- **Adaptív Korlátozás**: Gépi tanuláson alapuló korlátozást kell alkalmazni, amely alkalmazkodik a használati mintákhoz és fenyegetési jelekhez  
- **Erőforrás Kvóta Kezelés**: Megfelelő korlátokat kell beállítani a számítási erőforrásokra, memóriahasználatra és végrehajtási időre  
- **DDoS Védelem**: Átfogó DDoS védelem és forgalomelemző rendszerek telepítése

### 5. Átfogó Naplózás és Megfigyelés
- **Strukturált Audit Naplózás**: Részletes, kereshető naplókat kell vezetni minden MCP műveletről, eszközvégrehajtásról és biztonsági eseményről  
- **Valós Idejű Biztonsági Megfigyelés**: SIEM rendszereket kell telepíteni AI-alapú anomáliaészleléssel az MCP munkaterhelésekhez  
- **Adatvédelmi Megfelelő Naplózás**: A biztonsági eseményeket naplózni kell az adatvédelmi követelmények és szabályozások tiszteletben tartásával  
- **Eseménykezelés Integráció**: A naplózó rendszereket automatizált eseménykezelő munkafolyamatokhoz kell kapcsolni

### 6. Fejlett Biztonságos Tárolási Gyakorlatok
- **Hardveres Biztonsági Modulok**: Kritikus kriptográfiai műveletekhez HSM-alapú kulcstárolást kell használni (Azure Key Vault, AWS CloudHSM)  
- **Titkosítási Kulcskezelés**: Megfelelő kulcsforgatást, elkülönítést és hozzáférés-ellenőrzést kell alkalmazni a titkosítási kulcsok esetén  
- **Titkok Kezelése**: Minden API kulcsot, tokent és hitelesítő adatot dedikált titokkezelő rendszerekben kell tárolni  
- **Adatosztályozás**: Az adatokat érzékenységi szintek alapján kell osztályozni és megfelelő védelmi intézkedéseket kell alkalmazni

### 7. Fejlett Token Kezelés
- **Token Átengedés Megakadályozása**: Kifejezetten tilosak azok a token átengedési minták, amelyek megkerülik a biztonsági ellenőrzéseket  
- **Célközönség Ellenőrzése**: Mindig ellenőrizni kell, hogy a token célközönség állításai megfelelnek-e a szándékolt MCP szerver identitásának  
- **Állítás-alapú Engedélyezés**: Finomhangolt engedélyezést kell megvalósítani a token állítások és felhasználói attribútumok alapján  
- **Token Kötés**: A tokeneket adott munkamenetekhez, felhasználókhoz vagy eszközökhöz kell kötni, ahol ez indokolt

### 8. Biztonságos Munkamenet Kezelés
- **Kriptográfiai Munkamenet Azonosítók**: A munkamenet-azonosítókat kriptográfiailag biztonságos véletlenszám-generátorokkal kell létrehozni (nem előre jelezhető sorozatok)  
- **Felhasználó-specifikus Kötés**: A munkamenet-azonosítókat felhasználó-specifikus információkhoz kell kötni biztonságos formátumokkal, pl. `<user_id>:<session_id>`  
- **Munkamenet Élettartam Szabályozás**: Megfelelő munkamenet lejáratot, forgatást és érvénytelenítést kell megvalósítani  
- **Munkamenet Biztonsági Fejlécek**: Megfelelő HTTP biztonsági fejléceket kell használni a munkamenet védelmére

### 9. Mesterséges Intelligenciára Specifikus Biztonsági Intézkedések
- **Prompt Injekció Védelem**: Microsoft Prompt Shields alkalmazása spotlighting, elválasztók és adatjelölési technikákkal  
- **Eszköz Mérgezés Megelőzése**: Az eszköz metaadatokat ellenőrizni kell, dinamikus változásokat figyelni és az eszköz integritását ellenőrizni  
- **Modell Kimenet Érvényesítés**: A modell kimeneteket szkennelni kell esetleges adatkiszivárgás, káros tartalom vagy biztonsági szabályzat megsértése miatt  
- **Kontextus Ablak Védelem**: Intézkedéseket kell alkalmazni a kontextus ablak mérgezés és manipulációs támadások megelőzésére

### 10. Eszköz Végrehajtás Biztonsága
- **Végrehajtás Homokozóban**: Az eszközök végrehajtását konténerizált, izolált környezetben kell futtatni erőforrás-korlátokkal  
- **Jogosultság Szétválasztás**: Az eszközöket minimális szükséges jogosultságokkal és elkülönített szolgáltatói fiókokkal kell futtatni  
- **Hálózati Izoláció**: Hálózati szegmentációt kell alkalmazni az eszköz végrehajtási környezetekben  
- **Végrehajtás Megfigyelés**: Az eszköz végrehajtását figyelni kell anomáliák, erőforrás-használat és biztonsági szabálysértések szempontjából

### 11. Folyamatos Biztonsági Érvényesítés
- **Automatizált Biztonsági Tesztelés**: A biztonsági tesztelést integrálni kell a CI/CD folyamatokba olyan eszközökkel, mint a GitHub Advanced Security  
- **Sebezhetőség Kezelés**: Rendszeresen szkennelni kell minden függőséget, beleértve az AI modelleket és külső szolgáltatásokat is  
- **Penetrációs Tesztelés**: Rendszeres biztonsági értékeléseket kell végezni kifejezetten az MCP megvalósításokra  
- **Biztonsági Kódellenőrzés**: Kötelező biztonsági kódellenőrzést kell alkalmazni minden MCP-vel kapcsolatos kódváltoztatás esetén

### 12. Ellátási Lánc Biztonság az AI számára
- **Komponens Ellenőrzés**: Ellenőrizni kell az összes AI komponens (modellek, beágyazások, API-k) eredetét, integritását és biztonságát  
- **Függőség Kezelés**: Naprakész nyilvántartást kell vezetni minden szoftver- és AI-függőségről sebezhetőség követéssel  
- **Megbízható Tárolók**: Ellenőrzött, megbízható forrásokat kell használni minden AI modellhez, könyvtárhoz és eszközhöz  
- **Ellátási Lánc Megfigyelés**: Folyamatosan figyelni kell az AI szolgáltatók és modell tárolók esetleges kompromittálódását

## Fejlett Biztonsági Minták

### Zero Trust Architektúra az MCP-hez
- **Sose Bízz, Mindig Ellenőrizz**: Folyamatos ellenőrzést kell megvalósítani minden MCP résztvevő esetén  
- **Mikroszegmentáció**: Az MCP komponenseket granuláris hálózati és identitásvezérléssel kell izolálni  
- **Feltételes Hozzáférés**: Kockázatalapú hozzáférés-vezérlést kell alkalmazni, amely alkalmazkodik a kontextushoz és viselkedéshez  
- **Folyamatos Kockázatértékelés**: Dinamikusan kell értékelni a biztonsági helyzetet a jelenlegi fenyegetési jelek alapján

### Adatvédelmet Támogató AI Megvalósítás
- **Adatminimalizálás**: Csak a minimálisan szükséges adatokat szabad kitenni minden MCP művelethez  
- **Differenciális Adatvédelem**: Adatvédelmi technikákat kell alkalmazni érzékeny adatok feldolgozásához  
- **Homomorf Titkosítás**: Fejlett titkosítási technikákat kell használni titkosított adatok biztonságos feldolgozásához  
- **Federált Tanulás**: Elosztott tanulási megközelítéseket kell alkalmazni, amelyek megőrzik az adat helyi jellegét és adatvédelmét

### Eseménykezelés AI Rendszerekhez
- **AI-specifikus Eseménykezelési Eljárások**: Olyan eseménykezelési eljárásokat kell kidolgozni, amelyek az AI és MCP-specifikus fenyegetésekhez igazodnak  
- **Automatizált Válasz**: Automatizált korlátozást és helyreállítást kell megvalósítani a gyakori AI biztonsági eseményekre  
- **Igazságügyi Képességek**: Igazságügyi készenlétet kell fenntartani AI rendszer kompromittálódás és adatvédelmi incidensek esetén  
- **Helyreállítási Eljárások**: Eljárásokat kell kidolgozni AI modell mérgezés, prompt injekciós támadások és szolgáltatás kompromittálódás helyreállítására

## Megvalósítási Források és Szabványok

### Hivatalos MCP Dokumentáció
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Jelenlegi MCP protokoll specifikáció  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Hivatalos biztonsági útmutató  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Hitelesítési és engedélyezési minták  
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Transport réteg biztonsági követelmények

### Microsoft Biztonsági Megoldások
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Fejlett prompt injekció elleni védelem  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Átfogó AI tartalomszűrés  
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Vállalati identitás- és hozzáférés-kezelés  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Biztonságos titok- és hitelesítő adatkezelés  
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Ellátási lánc és kódbiztonsági szkennelés

### Biztonsági Szabványok és Keretrendszerek
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Jelenlegi OAuth biztonsági útmutató  
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Webalkalmazás biztonsági kockázatok  
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-specifikus biztonsági kockázatok  
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Átfogó AI kockázatkezelés  
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Információbiztonsági irányítási rendszerek

### Megvalósítási Útmutatók és Oktatóanyagok
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Vállalati hitelesítési minták  
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Identitásszolgáltató integráció  
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Token kezelési legjobb gyakorlatok  
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Fejlett titkosítási minták

### Fejlett Biztonsági Források
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Biztonságos fejlesztési gyakorlatok  
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-specifikus biztonsági tesztelés  
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI fenyegetésmodellezési módszertan  
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Adatvédelmet támogató AI technikák

### Megfelelőség és Irányítás
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Adatvédelmi megfelelőség AI rendszerekben  
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Felelős AI megvalósítás  
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Biztonsági intézkedések AI szolgáltatók számára  
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Egészségügyi AI megfelelőségi követelmények

### DevSecOps és Automatizálás
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Biztonságos AI fejlesztési folyamatok  
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Folyamatos biztonsági érvényesítés  
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Biztonságos infrastruktúra telepítés  
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AI munkaterhelések konténerizációs biztonsága

### Megfigyelés és Eseménykezelés  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Átfogó megfigyelési megoldások  
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-specifikus eseménykezelési eljárások  
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Biztonsági információ- és eseménykezelés  
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI fenyegetés intelligencia források

## 🔄 Folyamatos Fejlesztés

### Maradjon Naprakész a Változó Szabványokkal
- **MCP Specifikáció Frissítések**: Figyelje az MCP hivatalos specifikáció változásait és biztonsági közleményeit  
- **Fenyegetés Intelligencia**: Iratkozzon fel AI biztonsági fenyegetés hírcsatornákra és sebezhetőség adatbázisokra  
- **Közösségi Részvétel**: Vegyen részt az MCP biztonsági közösségi beszélgetésekben és munkacsoportokban  
- **Rendszeres Értékelés**: Negyedéves biztonsági helyzetértékeléseket végezzen és ennek megfelelően frissítse a gyakorlatokat

### Hozzájárulás az MCP Biztonsághoz
- **Biztonsági Kutatás**: Vegyen részt MCP biztonsági kutatásokban és sebezhetőség bejelentési programokban  
- **Legjobb Gyakorlatok Megosztása**: Ossza meg a biztonsági megvalósításokat és tanulságokat a közösséggel
- **Szabványos fejlesztés**: Részvétel az MCP specifikáció fejlesztésében és a biztonsági szabványok létrehozásában  
- **Eszközfejlesztés**: Biztonsági eszközök és könyvtárak fejlesztése és megosztása az MCP ökoszisztéma számára  

---

*Ez a dokumentum az MCP biztonsági legjobb gyakorlatait tükrözi 2025. december 18-i állapot szerint, az MCP Specifikáció 2025-11-25 alapján. A biztonsági gyakorlatokat rendszeresen felül kell vizsgálni és frissíteni kell, ahogy a protokoll és a fenyegetettségi környezet változik.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->