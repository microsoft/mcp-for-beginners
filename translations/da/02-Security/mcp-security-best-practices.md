# MCP Sikkerhed Bedste Praksis - Opdatering September 2026

> **Vigtigt:** Dette dokument afspejler
> [MCP Specifikation 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> og den officielle
> [MCP Sikkerhed Bedste Praksis](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## 🏔️ Praktisk Sikkerhedstræning

For praktisk implementeringserfaring anbefaler vi **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - en omfattende guidet ekspedition til sikring af MCP-servere i Azure. Workshoppen dækker alle OWASP MCP Top 10 risici gennem en "sårbar → udnyttelse → løsning → validering" metode.

Alle praksisser i dette dokument er i overensstemmelse med **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** for Azure-specifikke implementeringsvejledninger.

## Væsentlige Sikkerhedspraksisser for MCP Implementeringer

Model Context Protocol introducerer unikke sikkerhedsudfordringer, der går ud over traditionel softwaresikkerhed. Disse praksisser adresserer grundlæggende krav og MCP-specifikke trusler inkluderende promptinjektion, værktøjsforgiftning, overtagelse af state-handles, forvirrede forvalter-problemer og token passthrough-sårbarheder.





### **OBLIGATORISKE Sikkerhedskrav** 

**Kritiske Krav fra MCP Specifikationen:**

> **MÅ IKKE**: MCP servere **MÅ IKKE** acceptere nogen tokens, der ikke eksplicit er udstedt til MCP-serveren
> 
> **MÅ**: MCP servere, der implementerer autorisation, **MÅ** verificere ALLE indgående forespørgsler
>  
> **MÅ IKKE**: MCP servere **MÅ IKKE** anvende sessioner til autentificering
>
> **MÅ**: MCP proxy-servere, der bruger en statisk tredjeparts klient-ID, **MÅ**
> indhente samtykke for hver MCP-klient før videresendelse af autorisation

---

## 1. **Token Sikkerhed & Autentificering**

**Autentificering & Autorisationskontroller:**
   - **Grundig Autorisationsgennemgang**: Gennemfør omfattende audits af MCP servers autorisationslogik for at sikre, at kun tilsigtede brugere og klienter kan tilgå ressourcer
   - **Integration med Eksterne Identitetsudbydere**: Brug etablerede identitetsudbydere som Microsoft Entra ID fremfor at implementere brugerspecifikke autentificeringer
   - **Validering af Token Målgruppe**: Valider altid, at tokens er eksplicit udstedt til din MCP-server - accepter aldrig tokens fra opstrøm
   - **Korrekt Token Livscyklus**: Implementer sikker token-rotation, udløbspolitikker og forebyg replay-angreb

**Beskyttet Token Opbevaring:**
   - Brug Azure Key Vault eller lignende sikre credential-lagre til alle hemmeligheder
   - Implementer kryptering af tokens både i hvile og under transport
   - Regelmæssig udskiftning af credentials og overvågning for uautoriseret adgang

## 2. **State Handle & Transport Sikkerhed**

**Sikre Praksisser for Applikationsstate:**

- **Uigennemsigtige State Handles**: Brug sikre, ikke-deterministiske handles for applikationsstate, der spænder over forespørgsler
- **Bruger-specifik Binding**: Bind handles server-side til den autentificerede principal og afvis genbrug på tværs af brugere
- **Livscyklusstyring**: Udløb og tilbagekald handles for at begrænse sårbarhedsvinduer
- **Authorization per Forespørgsel**: Behandl aldrig en state handle som autentificering; autoriser hver forespørgsel, der præsenterer en

**Transportlagssikkerhed:**

- Kræv HTTPS for fjern HTTP-transporter i produktionsmiljøet

- Konfigurer moderne TLS med korrekt certifikatrotation og validering

## 3. **AI-specifik Trusselbeskyttelse** 🤖

**Forsvar mod Prompt Injection:**

   - **Inputsanering**: Valider og saner alle inputs for at forhindre injektionsangreb og forvirrede forvalter-problemer


**Forebyggelse af Værktøjsforgiftning:**
   - **Validering af Værktøjsmetadata**: Implementer integritetskontrol for værktøjsdefinitioner og overvåg for uventede ændringer
   - **Dynamisk Værktøjsmonitorering**: Overvåg runtime-adfærd og opret alarmer for uventede eksekveringsmønstre


## 4. **Adgangskontrol & Tilladelser**

**Princippet om Mindste Privilegium:**

   - Implementer rollebaseret adgangskontrol (RBAC) med finmaskede tilladelser


**Runtime Tilladelseskontroller:**
   - Anvend ressourcelimits for at forhindre udmattelsesangreb
   - Brug container-isolering til værktøjsudførelsesmiljøer  


## 5. **Indholdssikkerhed & Overvågning**

**Implementering af Indholdssikkerhed:**

   - **Adfærdsanalyse**: Implementer runtime adfærdsmonitorering for at opdage anomalier i MCP server og værktøjseksekvering


**Kontinuerlig Overvågning:**
   - Realtidsalarmering for mistænkelige mønstre og uautoriserede adgangsforsøg  
   - Integration med SIEM-systemer for centraliseret sikkerhedshændelsesstyring


## 6. **Supply Chain Sikkerhed**

**Komponentverifikation:**

   - **Oprindelsesvalidering**: Verificer oprindelse, licensering og integritet for modeller, datakilder og eksterne tjenester


**Sikker Udviklingspipeline:**
   - **GitHub Advanced Security**: Implementer scanning for hemmeligheder, afhængighedsanalyse og CodeQL statisk analyse
   - **CI/CD Sikkerhed**: Integrer sikkerhedsvalidering gennem automatiserede deploy-pipelines


## 7. **OAuth Sikkerhed & Forebyggelse af Forvirret Forvalter**

**OAuth 2.1 Implementering:**

    - **Klientregistrering**: Foretræk Client ID Metadata Dokumenter eller

       kompatibilitets-reserve
    - **Eksplicit Samtykke**: MCP proxyer, der bruger en statisk tredjeparts klient-ID, skal
       indhente samtykke for hver MCP-klient før videresendelse af autorisation
   - **Redirect URI Validering**: Implementer streng validering af redirect URI'er og klientidentifikatorer

**Proxy Sikkerhed:**
   - Forhindre autorisationsomgåelse gennem udnyttelse af statisk klient-ID
   - Implementer korrekte samtykkegange for adgang til tredjeparts API'er


## 8. **Hændelsesrespons & Genopretning**

**Hurtige Responsmuligheder:**

   - **Rollback Procedurer**: Mulighed for hurtigt at vende tilbage til kendte gode konfigurationer og komponenter


**Kommunikation & Koordination:**
   - Klare eskaleringsprocedurer for sikkerhedshændelser
   - Integration med organisatoriske hændelsesrespons teams


## 9. **Compliance & Styring**

**Regulatorisk Overholdelse:**

   - Implementer dataklassificering og privatlivskontroller for AI databehandling


**Ændringsstyring:**
   - Formelle sikkerhedsgennemgangsprocesser for alle MCP systemændringer
   - Versionskontrol og godkendelsesworkflow for konfigurationsændringer


## 10. **Avancerede Sikkerhedskontroller**

**Zero Trust Arkitektur:**

   - **Mikro-segmentering**: Granulære netværkskontroller, der isolerer individuelle MCP komponenter


**Runtime Applikationsbeskyttelse:**
   - **Runtime Application Self-Protection (RASP)**: Anvend RASP teknikker til realtids trusseldetektion
   - **Applikations Performance Monitorering**: Overvåg for performance-anomalier, der kan indikere angreb


## 11. **Microsoft Sikkerhedsøkosystem Integration**

**Omfattende Microsoft Sikkerhed:**

   - **Azure Sentinel**: Cloud-native SIEM og SOAR kapaciteter til avanceret trusseldetektion


**Identitet & Adgangsstyring:**
   - **Microsoft Entra ID**: Enterprise identitetsstyring med betingede adgangspolitikker
   - **Privilegeret Identitetsstyring (PIM)**: Just-in-time adgang og godkendelsesworkflows til administrative funktioner


## 12. **Kontinuerlig Udvikling af Sikkerhed**

**At Holde Sig Opdateret:**

   - **Trusselsintelligens**: Integration af AI-specifikke trusselsfeeds og kompromisdindikatorer


**Adaptiv Sikkerhed:**
   - **Maskinlæringssikkerhed**: Brug ML-baseret anomalidetektion til at identificere nye angrebsmønstre
   - **Prediktiv Sikkerhedsanalyse**: Implementer forudsigende modeller til proaktiv trusselsidentifikation


---

## **Kritiske Sikkerhedsressourcer**

---

## **Kritiske Sikkerhedsressourcer**

### **Officiel MCP Dokumentation**
- [MCP Specifikation (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Sikkerhedsbedste Praksis](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Autorisationsspecifikation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP Sikkerhedsressourcer**
- [OWASP MCP Azure Sikkerhedsguide](https://microsoft.github.io/mcp-azure-security-guide/) - Omfattende OWASP MCP Top 10 med Azure-implementering
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Officielle OWASP MCP sikkerhedsrisici
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktisk sikkerhedstræning for MCP på Azure

### **Microsoft Sikkerhedsløsninger**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Sikkerhed](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Avanceret Sikkerhed](https://github.com/security/advanced-security)

### **Sikkerhedsstandarder**
- [OAuth 2.0 Sikkerhedsbedste Praksis (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Store Sprogmodeller](https://genai.owasp.org/)
- [NIST AI Risikoledelsesramme](https://www.nist.gov/itl/ai-risk-management-framework)

### **Implementeringsguider**
- [Azure API Management MCP Autentificeringsgateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID med MCP Servere](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Sikkerhedsmeddelelse:** MCP sikkerhedspraksis udvikler sig hurtigt. Sørg altid for
> at sammenligne med den aktuelle [MCP specifikation](https://modelcontextprotocol.io/specification/2026-07-28/)
> og [officielle sikkerhedsdokumentation](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> før implementering.

## Hvad er Næste

- Læs: [MCP Sikkerhedskontroller](./mcp-security-controls.md)
- Vend tilbage til: [Oversigt over Sikkerhedsmodul](./README.md)
- Fortsæt til: [Modul 3: Kom i gang](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->