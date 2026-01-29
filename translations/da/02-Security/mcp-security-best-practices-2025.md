# MCP Sikkerhedsbedste Praksis - Opdatering December 2025

> **Vigtigt**: Dette dokument afspejler de seneste [MCP Specifikation 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) sikkerhedskrav og officielle [MCP Sikkerhedsbedste Praksis](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Henvis altid til den aktuelle specifikation for den mest opdaterede vejledning.

## Væsentlige Sikkerhedspraksisser for MCP Implementeringer

Model Context Protocol introducerer unikke sikkerhedsudfordringer, der går ud over traditionel softwaresikkerhed. Disse praksisser adresserer både grundlæggende sikkerhedskrav og MCP-specifikke trusler, herunder prompt-injektion, værktøjsforgiftning, session kapring, forvirret stedfortræder-problemer og token-gennemgangssårbarheder.

### **OBLIGATORISKE Sikkerhedskrav** 

**Kritiske krav fra MCP Specifikation:**

### **OBLIGATORISKE Sikkerhedskrav** 

**Kritiske krav fra MCP Specifikation:**

> **MÅ IKKE**: MCP-servere **MÅ IKKE** acceptere nogen tokens, der ikke eksplicit er udstedt til MCP-serveren  
>  
> **MÅ**: MCP-servere, der implementerer autorisation, **MÅ** verificere ALLE indgående anmodninger  
>  
> **MÅ IKKE**: MCP-servere **MÅ IKKE** bruge sessioner til autentificering  
>  
> **MÅ**: MCP-proxyservere, der bruger statiske klient-ID'er, **MÅ** indhente brugerens samtykke for hver dynamisk registreret klient

---

## 1. **Token Sikkerhed & Autentificering**

**Autentificerings- & Autorisationskontroller:**
   - **Grundig Autorisationsgennemgang**: Udfør omfattende revisioner af MCP-serverens autorisationslogik for at sikre, at kun tilsigtede brugere og klienter kan få adgang til ressourcer  
   - **Integration med Eksterne Identitetsudbydere**: Brug etablerede identitetsudbydere som Microsoft Entra ID i stedet for at implementere brugerdefineret autentificering  
   - **Validering af Token Publikum**: Valider altid, at tokens eksplicit er udstedt til din MCP-server – accepter aldrig upstream tokens  
   - **Korrekt Token Livscyklus**: Implementer sikker token-rotation, udløbspolitikker og forhindre token replay-angreb

**Beskyttet Token Opbevaring:**
   - Brug Azure Key Vault eller lignende sikre legitimationsopbevaringssteder til alle hemmeligheder  
   - Implementer kryptering for tokens både i hvile og under overførsel  
   - Regelmæssig rotation af legitimationsoplysninger og overvågning for uautoriseret adgang

## 2. **Session Management & Transport Sikkerhed**

**Sikre Session Praksisser:**
   - **Kryptografisk Sikre Session IDs**: Brug sikre, ikke-deterministiske session IDs genereret med sikre tilfældige talgeneratorer  
   - **Bruger-specifik Binding**: Bind session IDs til brugeridentiteter ved brug af formater som `<user_id>:<session_id>` for at forhindre misbrug af sessioner på tværs af brugere  
   - **Session Livscyklus Management**: Implementer korrekt udløb, rotation og ugyldiggørelse for at begrænse sårbarhedsvinduer  
   - **HTTPS/TLS Håndhævelse**: Obligatorisk HTTPS for al kommunikation for at forhindre opsnapning af session IDs

**Transportlagssikkerhed:**
   - Konfigurer TLS 1.3 hvor muligt med korrekt certifikatstyring  
   - Implementer certifikat-pinning for kritiske forbindelser  
   - Regelmæssig rotation af certifikater og verifikation af gyldighed

## 3. **AI-Specifik Trusselsbeskyttelse** 🤖

**Forsvar mod Prompt Injection:**
   - **Microsoft Prompt Shields**: Implementer AI Prompt Shields for avanceret detektion og filtrering af ondsindede instruktioner  
   - **Input Rensning**: Valider og rens alle input for at forhindre injektionsangreb og forvirret stedfortræder-problemer  
   - **Indholdsgrænser**: Brug delimiter- og datamarkeringssystemer til at skelne mellem betroede instruktioner og eksternt indhold

**Forebyggelse af Værktøjsforgiftning:**
   - **Validering af Værktøjsmetadata**: Implementer integritetskontroller for værktøjsdefinitioner og overvåg for uventede ændringer  
   - **Dynamisk Værktøjsovervågning**: Overvåg runtime-adfærd og opsæt alarmer for uventede eksekveringsmønstre  
   - **Godkendelsesarbejdsgange**: Kræv eksplicit brugeraccept for værktøjsmodifikationer og kapabilitetsændringer

## 4. **Adgangskontrol & Rettigheder**

**Princippet om Mindste Privilegium:**
   - Tildel MCP-servere kun de minimale rettigheder, der kræves for den tilsigtede funktionalitet  
   - Implementer rollebaseret adgangskontrol (RBAC) med finmaskede rettigheder  
   - Regelmæssige gennemgange af rettigheder og kontinuerlig overvågning for privilegieeskalering

**Runtime Rettighedskontroller:**
   - Anvend ressourcebegrænsninger for at forhindre angreb med ressourceudtømning  
   - Brug container-isolering til værktøjsudførelsesmiljøer  
   - Implementer just-in-time adgang til administrative funktioner

## 5. **Indholdssikkerhed & Overvågning**

**Implementering af Indholdssikkerhed:**
   - **Azure Content Safety Integration**: Brug Azure Content Safety til at opdage skadeligt indhold, jailbreak-forsøg og politikovertrædelser  
   - **Adfærdsanalyse**: Implementer runtime adfærdsovervågning for at opdage anomalier i MCP-server og værktøjsudførelse  
   - **Omfattende Logning**: Log alle autentificeringsforsøg, værktøjskald og sikkerhedshændelser med sikker, manipulationssikker opbevaring

**Kontinuerlig Overvågning:**
   - Realtidsalarmer for mistænkelige mønstre og uautoriserede adgangsforsøg  
   - Integration med SIEM-systemer til centraliseret sikkerhedshændelsesstyring  
   - Regelmæssige sikkerhedsrevisioner og penetrationstest af MCP-implementeringer

## 6. **Supply Chain Sikkerhed**

**Komponentverifikation:**
   - **Afhængighedsscanning**: Brug automatiseret sårbarhedsscanning for alle softwareafhængigheder og AI-komponenter  
   - **Oprindelsesvalidering**: Verificer oprindelse, licensering og integritet af modeller, datakilder og eksterne tjenester  
   - **Signerede Pakker**: Brug kryptografisk signerede pakker og verificer signaturer før udrulning

**Sikker Udviklingspipeline:**
   - **GitHub Advanced Security**: Implementer hemmelighedsscanning, afhængighedsanalyse og CodeQL statisk analyse  
   - **CI/CD Sikkerhed**: Integrer sikkerhedsvalidering gennem automatiserede udrulningspipelines  
   - **Artefaktintegritet**: Implementer kryptografisk verifikation for udrullede artefakter og konfigurationer

## 7. **OAuth Sikkerhed & Forebyggelse af Forvirret Stedfortræder**

**OAuth 2.1 Implementering:**
   - **PKCE Implementering**: Brug Proof Key for Code Exchange (PKCE) for alle autorisationsanmodninger  
   - **Eksplicit Samtykke**: Indhent brugerens samtykke for hver dynamisk registreret klient for at forhindre forvirret stedfortræder-angreb  
   - **Validering af Redirect URI**: Implementer streng validering af redirect URIs og klientidentifikatorer

**Proxy Sikkerhed:**
   - Forhindre autorisationsomgåelse via udnyttelse af statiske klient-ID'er  
   - Implementer korrekte samtykkearbejdsgange for tredjeparts API-adgang  
   - Overvåg for tyveri af autorisationskoder og uautoriseret API-adgang

## 8. **Hændelsesrespons & Genopretning**

**Hurtige Responsmuligheder:**
   - **Automatiseret Respons**: Implementer automatiserede systemer til rotation af legitimationsoplysninger og trusselsinddæmning  
   - **Rollback Procedurer**: Mulighed for hurtigt at rulle tilbage til kendte gode konfigurationer og komponenter  
   - **Rettsmedicinske Muligheder**: Detaljerede revisionsspor og logning til hændelsesundersøgelser

**Kommunikation & Koordination:**
   - Klare eskaleringsprocedurer for sikkerhedshændelser  
   - Integration med organisatoriske hændelsesrespons teams  
   - Regelmæssige sikkerhedshændelsessimulationer og tabletop-øvelser

## 9. **Overholdelse & Styring**

**Regulatorisk Overholdelse:**
   - Sikre at MCP-implementeringer opfylder branchespecifikke krav (GDPR, HIPAA, SOC 2)  
   - Implementer dataklassificering og privatlivskontroller for AI databehandling  
   - Oprethold omfattende dokumentation til compliance-audit

**Ændringsstyring:**
   - Formelle sikkerhedsgennemgangsprocesser for alle MCP-systemændringer  
   - Versionskontrol og godkendelsesarbejdsgange for konfigurationsændringer  
   - Regelmæssige compliance-vurderinger og gap-analyser

## 10. **Avancerede Sikkerhedskontroller**

**Zero Trust Arkitektur:**
   - **Aldrig Stol på, Altid Verificer**: Kontinuerlig verifikation af brugere, enheder og forbindelser  
   - **Mikrosegmentering**: Granulære netværkskontroller, der isolerer individuelle MCP-komponenter  
   - **Betinget Adgang**: Risikobaserede adgangskontroller, der tilpasser sig den aktuelle kontekst og adfærd

**Runtime Applikationsbeskyttelse:**
   - **Runtime Application Self-Protection (RASP)**: Implementer RASP-teknikker til realtids trusselsdetektion  
   - **Applikationsperformanceovervågning**: Overvåg for performanceanomalier, der kan indikere angreb  
   - **Dynamiske Sikkerhedspolitikker**: Implementer sikkerhedspolitikker, der tilpasser sig baseret på det aktuelle trusselslandskab

## 11. **Microsoft Sikkerhedsøkosystem Integration**

**Omfattende Microsoft Sikkerhed:**
   - **Microsoft Defender for Cloud**: Cloud sikkerhedsstyring for MCP workloads  
   - **Azure Sentinel**: Cloud-native SIEM og SOAR kapaciteter til avanceret trusselsdetektion  
   - **Microsoft Purview**: Datastyring og compliance for AI workflows og datakilder

**Identitets- & Adgangsstyring:**
   - **Microsoft Entra ID**: Enterprise identitetsstyring med betingede adgangspolitikker  
   - **Privileged Identity Management (PIM)**: Just-in-time adgang og godkendelsesarbejdsgange for administrative funktioner  
   - **Identitetsbeskyttelse**: Risikobaseret betinget adgang og automatiseret trusselsrespons

## 12. **Kontinuerlig Sikkerhedsudvikling**

**At Holde Sig Opdateret:**
   - **Specifikationsovervågning**: Regelmæssig gennemgang af MCP specifikationsopdateringer og ændringer i sikkerhedsanbefalinger  
   - **Trusselsintelligens**: Integration af AI-specifikke trusselsfeeds og kompromitteringsindikatorer  
   - **Engagement i Sikkerhedsfællesskabet**: Aktiv deltagelse i MCP sikkerhedsfællesskabet og sårbarhedsafsløringsprogrammer

**Adaptiv Sikkerhed:**
   - **Maskinlæringssikkerhed**: Brug ML-baseret anomalidetektion til at identificere nye angrebsmønstre  
   - **Prediktiv Sikkerhedsanalytik**: Implementer prediktive modeller til proaktiv trusselsidentifikation  
   - **Sikkerhedsautomatisering**: Automatiserede opdateringer af sikkerhedspolitikker baseret på trusselsintelligens og specifikationsændringer

---

## **Kritiske Sikkerhedsressourcer**

### **Officiel MCP Dokumentation**
- [MCP Specifikation (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Sikkerhedsbedste Praksis](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Autorisationsspecifikation](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft Sikkerhedsløsninger**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Sikkerhed](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Sikkerhedsstandarder**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

### **Implementeringsvejledninger**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID med MCP Servere](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Sikkerhedsmeddelelse**: MCP sikkerhedspraksis udvikler sig hurtigt. Verificer altid mod den aktuelle [MCP specifikation](https://spec.modelcontextprotocol.io/) og [officielle sikkerhedsdokumentation](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) før implementering.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->