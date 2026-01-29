# Cele mai bune practici de securitate MCP - Actualizare decembrie 2025

> **Important**: Acest document reflectă cele mai recente cerințe de securitate din [Specificația MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) și [Cele mai bune practici oficiale de securitate MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Consultați întotdeauna specificația curentă pentru cele mai actualizate recomandări.

## Practici esențiale de securitate pentru implementările MCP

Model Context Protocol introduce provocări unice de securitate care depășesc securitatea software tradițională. Aceste practici abordează atât cerințele fundamentale de securitate, cât și amenințările specifice MCP, inclusiv injecția de prompturi, otrăvirea uneltelor, deturnarea sesiunii, problemele de tip „confused deputy” și vulnerabilitățile de trecere a token-urilor.

### **Cerințe de securitate OBLIGATORII**

**Cerințe critice din Specificația MCP:**

### **Cerințe de securitate OBLIGATORII**

**Cerințe critice din Specificația MCP:**

> **NU TREBUIE**: Serverele MCP **NU TREBUIE** să accepte niciun token care nu a fost emis explicit pentru serverul MCP
> 
> **TREBUIE**: Serverele MCP care implementează autorizarea **TREBUIE** să verifice TOATE cererile primite
>  
> **NU TREBUIE**: Serverele MCP **NU TREBUIE** să folosească sesiuni pentru autentificare
>
> **TREBUIE**: Serverele proxy MCP care folosesc ID-uri statice de client **TREBUIE** să obțină consimțământul utilizatorului pentru fiecare client înregistrat dinamic

---

## 1. **Securitatea token-urilor & Autentificarea**

**Controale de autentificare & autorizare:**
   - **Revizuire riguroasă a autorizării**: Efectuați audituri cuprinzătoare ale logicii de autorizare a serverului MCP pentru a asigura că doar utilizatorii și clienții intenționați pot accesa resursele
   - **Integrare cu furnizori externi de identitate**: Folosiți furnizori de identitate consacrați precum Microsoft Entra ID în loc să implementați autentificare personalizată
   - **Validarea audienței token-urilor**: Verificați întotdeauna că token-urile au fost emise explicit pentru serverul dvs. MCP - nu acceptați niciodată token-uri din amonte
   - **Ciclul de viață corect al token-urilor**: Implementați rotație sigură a token-urilor, politici de expirare și preveniți atacurile de redare a token-urilor

**Stocare protejată a token-urilor:**
   - Folosiți Azure Key Vault sau depozite securizate similare pentru toate secretele
   - Implementați criptarea token-urilor atât în repaus, cât și în tranzit
   - Rotație regulată a acreditărilor și monitorizare pentru acces neautorizat

## 2. **Gestionarea sesiunilor & Securitatea transportului**

**Practici sigure pentru sesiuni:**
   - **ID-uri de sesiune criptografic sigure**: Folosiți ID-uri de sesiune securizate, nedeterministe, generate cu generatoare de numere aleatorii sigure
   - **Legare specifică utilizatorului**: Legați ID-urile de sesiune de identitățile utilizatorilor folosind formate precum `<user_id>:<session_id>` pentru a preveni abuzul de sesiuni între utilizatori
   - **Gestionarea ciclului de viață al sesiunii**: Implementați expirare, rotație și invalidare corespunzătoare pentru a limita ferestrele de vulnerabilitate
   - **Impunerea HTTPS/TLS**: HTTPS obligatoriu pentru toate comunicațiile pentru a preveni interceptarea ID-urilor de sesiune

**Securitatea nivelului de transport:**
   - Configurați TLS 1.3 acolo unde este posibil cu gestionare corectă a certificatelor
   - Implementați certificate pinning pentru conexiuni critice
   - Rotație regulată a certificatelor și verificarea valabilității

## 3. **Protecție specifică amenințărilor AI** 🤖

**Apărarea împotriva injecției de prompturi:**
   - **Microsoft Prompt Shields**: Implementați AI Prompt Shields pentru detectarea și filtrarea avansată a instrucțiunilor malițioase
   - **Securizarea inputurilor**: Validați și curățați toate intrările pentru a preveni atacurile de injecție și problemele de tip „confused deputy”
   - **Frontiere de conținut**: Folosiți delimitatori și sisteme de marcare a datelor pentru a distinge între instrucțiuni de încredere și conținut extern

**Prevenirea otrăvirii uneltelor:**
   - **Validarea metadatelor uneltelor**: Implementați verificări de integritate pentru definițiile uneltelor și monitorizați modificările neașteptate
   - **Monitorizarea dinamică a uneltelor**: Monitorizați comportamentul la rulare și configurați alerte pentru modele neașteptate de execuție
   - **Fluxuri de aprobare**: Solicitați aprobarea explicită a utilizatorului pentru modificările uneltelor și schimbările de capabilități

## 4. **Controlul accesului & Permisiuni**

**Principiul privilegiului minim:**
   - Acordați serverelor MCP doar permisiunile minime necesare pentru funcționalitatea intenționată
   - Implementați controlul accesului bazat pe roluri (RBAC) cu permisiuni detaliate
   - Revizuiri regulate ale permisiunilor și monitorizare continuă pentru escaladarea privilegiilor

**Controale de permisiuni la rulare:**
   - Aplicați limite de resurse pentru a preveni atacurile de epuizare a resurselor
   - Folosiți izolare în containere pentru mediile de execuție ale uneltelor  
   - Implementați acces just-in-time pentru funcțiile administrative

## 5. **Siguranța conținutului & Monitorizare**

**Implementarea siguranței conținutului:**
   - **Integrare Azure Content Safety**: Folosiți Azure Content Safety pentru detectarea conținutului dăunător, încercărilor de jailbreak și încălcărilor politicilor
   - **Analiză comportamentală**: Implementați monitorizare comportamentală la rulare pentru a detecta anomalii în execuția serverului MCP și a uneltelor
   - **Jurnalizare cuprinzătoare**: Înregistrați toate încercările de autentificare, invocările uneltelor și evenimentele de securitate cu stocare securizată, rezistentă la modificări

**Monitorizare continuă:**
   - Alertare în timp real pentru modele suspecte și încercări neautorizate de acces  
   - Integrare cu sisteme SIEM pentru gestionarea centralizată a evenimentelor de securitate
   - Audituri regulate de securitate și teste de penetrare ale implementărilor MCP

## 6. **Securitatea lanțului de aprovizionare**

**Verificarea componentelor:**
   - **Scanare a dependențelor**: Folosiți scanare automată a vulnerabilităților pentru toate dependențele software și componentele AI
   - **Validarea provenienței**: Verificați originea, licențierea și integritatea modelelor, surselor de date și serviciilor externe
   - **Pachete semnate**: Folosiți pachete semnate criptografic și verificați semnăturile înainte de implementare

**Pipeline de dezvoltare securizat:**
   - **GitHub Advanced Security**: Implementați scanarea secretelor, analiza dependențelor și analiza statică CodeQL
   - **Securitate CI/CD**: Integrați validarea securității pe tot parcursul pipeline-urilor automate de implementare
   - **Integritatea artefactelor**: Implementați verificarea criptografică pentru artefactele și configurațiile implementate

## 7. **Securitatea OAuth & Prevenirea atacurilor „confused deputy”**

**Implementarea OAuth 2.1:**
   - **Implementare PKCE**: Folosiți Proof Key for Code Exchange (PKCE) pentru toate cererile de autorizare
   - **Consimțământ explicit**: Obțineți consimțământul utilizatorului pentru fiecare client înregistrat dinamic pentru a preveni atacurile „confused deputy”
   - **Validarea URI-urilor de redirecționare**: Implementați validare strictă a URI-urilor de redirecționare și a identificatorilor de client

**Securitatea proxy-ului:**
   - Preveniți ocolirea autorizării prin exploatarea ID-urilor statice de client
   - Implementați fluxuri corecte de consimțământ pentru accesul API-urilor terțe
   - Monitorizați furtul codurilor de autorizare și accesul neautorizat la API

## 8. **Răspuns la incidente & Recuperare**

**Capabilități de răspuns rapid:**
   - **Răspuns automatizat**: Implementați sisteme automate pentru rotația acreditărilor și limitarea amenințărilor
   - **Proceduri de revenire**: Capacitatea de a reveni rapid la configurații și componente cunoscute ca fiind sigure
   - **Capabilități judiciare**: Urmăriri detaliate și jurnalizare pentru investigarea incidentelor

**Comunicare & coordonare:**
   - Proceduri clare de escaladare pentru incidentele de securitate
   - Integrare cu echipele organizaționale de răspuns la incidente
   - Simulări regulate de incidente de securitate și exerciții de tip tabletop

## 9. **Conformitate & Guvernanță**

**Conformitate reglementară:**
   - Asigurați-vă că implementările MCP respectă cerințele specifice industriei (GDPR, HIPAA, SOC 2)
   - Implementați clasificarea datelor și controale de confidențialitate pentru procesarea datelor AI
   - Mențineți documentație cuprinzătoare pentru auditul conformității

**Managementul schimbărilor:**
   - Procese formale de revizuire a securității pentru toate modificările sistemului MCP
   - Controlul versiunilor și fluxuri de aprobare pentru modificările de configurare
   - Evaluări regulate de conformitate și analize ale lacunelor

## 10. **Controale avansate de securitate**

**Arhitectura Zero Trust:**
   - **Niciodată nu ai încredere, verifică întotdeauna**: Verificare continuă a utilizatorilor, dispozitivelor și conexiunilor
   - **Micro-segmentare**: Controale granulare de rețea care izolează componentele individuale MCP
   - **Acces condiționat**: Controale de acces bazate pe risc care se adaptează la contextul și comportamentul curent

**Protecția aplicațiilor la rulare:**
   - **Runtime Application Self-Protection (RASP)**: Implementați tehnici RASP pentru detectarea amenințărilor în timp real
   - **Monitorizarea performanței aplicațiilor**: Monitorizați anomaliile de performanță care pot indica atacuri
   - **Politici dinamice de securitate**: Implementați politici de securitate care se adaptează în funcție de peisajul actual al amenințărilor

## 11. **Integrarea ecosistemului de securitate Microsoft**

**Securitate Microsoft cuprinzătoare:**
   - **Microsoft Defender for Cloud**: Managementul posturii de securitate în cloud pentru sarcinile MCP
   - **Azure Sentinel**: Capacități SIEM și SOAR native în cloud pentru detectarea avansată a amenințărilor
   - **Microsoft Purview**: Guvernanța datelor și conformitatea pentru fluxurile de lucru AI și sursele de date

**Gestionarea identității & accesului:**
   - **Microsoft Entra ID**: Managementul identității enterprise cu politici de acces condiționat
   - **Privileged Identity Management (PIM)**: Acces just-in-time și fluxuri de aprobare pentru funcțiile administrative
   - **Protecția identității**: Acces condiționat bazat pe risc și răspuns automatizat la amenințări

## 12. **Evoluția continuă a securității**

**Menținerea la zi:**
   - **Monitorizarea specificațiilor**: Revizuiri regulate ale actualizărilor specificației MCP și schimbărilor în ghidurile de securitate
   - **Informații despre amenințări**: Integrarea fluxurilor de amenințări specifice AI și indicatorilor de compromitere
   - **Implicare în comunitatea de securitate**: Participare activă în comunitatea de securitate MCP și programele de divulgare a vulnerabilităților

**Securitate adaptivă:**
   - **Securitate bazată pe învățare automată**: Folosiți detectarea anomaliilor bazată pe ML pentru identificarea modelelor noi de atac
   - **Analitică predictivă de securitate**: Implementați modele predictive pentru identificarea proactivă a amenințărilor
   - **Automatizarea securității**: Actualizări automate ale politicilor de securitate bazate pe informații despre amenințări și modificări ale specificațiilor

---

## **Resurse critice de securitate**

### **Documentație oficială MCP**
- [Specificația MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Cele mai bune practici de securitate MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Specificația autorizării MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Soluții de securitate Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Securitatea Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Standarde de securitate**
- [Cele mai bune practici de securitate OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 pentru modele mari de limbaj](https://genai.owasp.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

### **Ghiduri de implementare**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID cu servere MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Notificare de securitate**: Practicile de securitate MCP evoluează rapid. Verificați întotdeauna conform specificației curente [MCP](https://spec.modelcontextprotocol.io/) și documentației oficiale de securitate [MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) înainte de implementare.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->