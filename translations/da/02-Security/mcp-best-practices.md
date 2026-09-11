# MCP Sikkerhed Bedste Praksis - Opdatering September 2026

Denne omfattende vejledning skitserer væsentlige sikkerhedsbedste praksis for
implementering af Model Context Protocol (MCP) systemer baseret på
**MCP Specification 2026-07-28** og aktuelle industristandarder. Disse
praksisser adresserer både traditionelle sikkerhedsbekymringer og AI-specifikke trusler
unikke for MCP-implementeringer.

## Kritiske Sikkerhedskrav

### Obligatoriske Sikkerhedskontroller (MUST Krav)

1. **Tokenvalidering**: MCP-servere **MÅ IKKE** acceptere nogen tokens, der ikke eksplicit er udstedt til MCP-serveren selv
2. **Autorisation Verifikation**: MCP-servere, der implementerer autorisation, **SKAL** verificere ALLE indgående forespørgsler og **MÅ IKKE** anvende sessioner til autentifikation  
3. **Brugersamtykke**: MCP proxy-servere, der bruger statiske tredjeparts klient-ID'er, **SKAL** indhente eksplicit samtykke for hver MCP-klient før videresendelse af en autorisationsflow
4. **State Handle Sikkerhed**: MCP-servere **MÅ IKKE** betragte besiddelse af et
	application state handle som autentifikation og **SKAL** autorisere hver
	forespørgsel, der bruger et sådant

## Kerne Sikkerhedspraksis

### 1. Inputvalidering & Sanitering
- **Omfattende Inputvalidering**: Valider og saniter alle inputs for at forhindre injektionsangreb, forvirret stedfortræder-problemer og prompt-injektionssårbarheder
- **Parameter Skema Håndhævelse**: Implementer streng JSON-skema validering for alle værktøjsparametre og API-inputs
- **Indholdsfiltrering**: Brug Microsoft Prompt Shields og Azure Content Safety til at filtrere ondsindet indhold i prompts og svar
- **Output Sanitering**: Valider og saniter alle modeloutputs inden præsentation for brugere eller downstream systemer

### 2. Fremragende Autentifikation & Autorisation  
- **Eksterne Identitetsudbydere**: Deleger autentifikation til etablerede identitetsudbydere (Microsoft Entra ID, OAuth 2.1 udbydere) fremfor at implementere brugerdefineret autentifikation
- **Klientregistrering**: Foretræk Client ID Metadata Dokumenter eller præ-registrering; brug kun forældet Dynamic Client Registration for kompatibilitet
- **Finmasket Tilladelse**: Implementer granulære, værktøjsspecifikke tilladelser efter princippet om mindst privilegium
- **Token Livscyklus Håndtering**: Brug kortlivede adgangstokens med sikker rotation og korrekt audiencesvalidering
- **Multi-Faktor Autentifikation**: Kræv MFA for al administrativ adgang og følsomme operationer

### 3. Sikre Kommunikationsprotokoller
- **Transportlagssikkerhed**: Brug HTTPS med korrekt certifikatvalidering
	for fjern HTTP MCP-kommunikation; brug procesisolation og miljø-
	legitimationsoplysninger for lokale stdio-servere
- **End-to-End Kryptering**: Implementer yderligere krypteringslag for højsensitive data under transit og i hvile
- **Certifikathåndtering**: Vedligehold korrekt livscyklus for certifikater med automatiserede fornyelsesprocesser
- **Protokolversionshåndhævelse**: Brug MCP `2026-07-28`, inkluder den krævede
	versionsmetadata ved hver forespørgsel, og afvis understøttede versioner

### 4. Avanceret Ratebegrænsning & Ressourcebeskyttelse
- **Flersidet Ratebegrænsning**: Implementer ratebegrænsning efter bruger, legitimationsoplysninger,
  operation, værktøj og ressourcer for at forhindre misbrug
- **Adaptiv Ratebegrænsning**: Brug maskinlæringsbaseret ratebegrænsning, der tilpasser sig brugsmønstre og trusselindikatorer
- **Ressourcekvotastyring**: Sæt passende grænser for beregningsressourcer, hukommelsesbrug og køretid
- **DDoS Beskyttelse**: Implementer omfattende DDoS beskyttelse og trafik analyse systemer

### 5. Omfattende Logning & Overvågning
- **Struktureret Revisionslogning**: Implementer detaljerede, søgbare logs for alle MCP operationer, værktøjsudførelser og sikkerhedshændelser
- **Realtids Sikkerhedsovervågning**: Implementer SIEM-systemer med AI-drevet anomalidetektion for MCP belastninger
- **Privatlivscompliant Logning**: Log sikkerhedshændelser mens data-privatlivskrav og reguleringer respekteres
- **Incident Response Integration**: Forbind logningssystemer til automatiserede hændelsesrespons workflows

### 6. Forbedrede Sikre Lagringspraksisser
- **Hardware Security Modules**: Brug HSM-understøttet nøglelagring (Azure Key Vault, AWS CloudHSM) til kritiske kryptografiske operationer
- **Krypteringsnøglehåndtering**: Implementer korrekt nøglerotation, adskillelse og adgangskontrol til krypteringsnøgler
- **Hemmelighedshåndtering**: Opbevar alle API-nøgler, tokens og legitimationsoplysninger i dedikerede hemmelighedsstyringssystemer
- **Dataklassificering**: Klassificer data efter følsomhedsniveau og anvend passende beskyttelsesforanstaltninger

### 7. Avanceret Tokenhåndtering
- **Forebyggelse af Token Passthrough**: Forbyd eksplicit token passthrough-mønstre, der omgår sikkerhedskontroller
- **Audience Validation**: Verificer altid at token audience claims matcher den tilsigtede MCP-serveridentitet
- **Claims-baseret Autorisation**: Implementer finmasket autorisation baseret på token claims og brugerattributter
- **Token Binding**: Valider at tokens er rettet mod den tilsigtede MCP-ressource og
	binder applikationens state handles server-side til den autentificerede principal

### 8. Sikker Applikationsstate

- **Kryptografiske State Handles**: Generer uigennemsigtige, ikke-deterministiske handles
	for state, der spænder over forespørgsler
- **Brugerspecifik Binding**: Bind hver handle server-side til den autentificerede
	principal; stol ikke på et bruger-ID leveret af klienten
- **Livscyklus Kontroller**: Udgå og tilbagekald handles, og definer hvordan kaldere
	genvinder fra forældet state
- **Per-forespørgsel Autorisation**: Genverificer autorisation når en handle
	præsenteres; en handle er et navn, ikke en legitimationsoplysning

### 9. AI-Specifikke Sikkerhedskontroller
- **Prompt Injektionsforsvar**: Implementer Microsoft Prompt Shields med spotlighting, afgrænsere og datamarkeringsmetoder
- **Forebyggelse af Værktøjsforgiftning**: Valider værktøjsmetadata, overvåg dynamiske ændringer, og verificer værktøjsintegritet
- **Modeloutputvalidering**: Scan modeloutput for potentielt datalæk, skadeligt indhold eller brud på sikkerhedspolitikker
- **Context Window Beskyttelse**: Implementer kontroller for at forhindre context window-forgiftning og manipulationsangreb

### 10. Sikker Værktøjsudførelse
- **Udførelses Sandboxing**: Kør værktøjsudførelser i containeriserede, isolerede miljøer med ressourcebegrænsninger
- **Privilegieadskillelse**: Udfør værktøjer med minimale nødvendige privilegier og separate servicekonti
- **Netværksisolation**: Implementer netværkssegmentering for værktøjsudførelsesmiljøer
- **Udførelsesovervågning**: Overvåg værktøjsudførelser for unormal adfærd, ressourceforbrug og sikkerhedsbrud

### 11. Kontinuerlig Sikkerhedsvalidering
- **Automatiseret Sikkerhedstestning**: Integrer sikkerhedstestning i CI/CD pipelines med værktøjer som GitHub Advanced Security
- **Sårbarhedsstyring**: Scann regelmæssigt alle afhængigheder, inklusive AI-modeller og eksterne tjenester
- **Penetrationstest**: Udfør regelmæssige sikkerhedsvurderinger med fokus på MCP-implementeringer
- **Sikkerhedskodegennemgang**: Implementer obligatoriske sikkerhedsgennemgange for alle MCP-relaterede kodeændringer

### 12. Supply Chain Sikkerhed for AI
- **Komponentverifikation**: Verificer oprindelse, integritet og sikkerhed af alle AI-komponenter (modeller, embeddings, API'er)
- **Afhængighedsstyring**: Oprethold opdaterede oversigter over al software og AI-afhængigheder med sårbarhedsovervågning
- **Betroede Repositorier**: Brug verificerede, betroede kilder til alle AI-modeller, biblioteker og værktøjer
- **Supply Chain Overvågning**: Overvåg kontinuerligt for kompromittering af AI-tjenesteudbydere og modelrepositories

## Avancerede Sikkerhedsmønstre

### Zero Trust Arkitektur for MCP
- **Aldrig Stol, Altid Verificer**: Implementer kontinuerlig verifikation for alle MCP-deltagere
- **Mikrosegmentering**: Isoler MCP-komponenter med granulære netværks- og identitetskontroller
- **Betinget Adgang**: Implementer risikobaserede adgangskontroller, der tilpasser sig kontekst og adfærd
- **Kontinuerlig Risikovurdering**: Dynamisk evaluér sikkerhedsstilling baseret på aktuelle trusselindikatorer

### Privatlivsbevarende AI-Implementering
- **Dataminimering**: Udstil kun minimum nødvendige data for hver MCP-operation
- **Differential Privacy**: Implementer privatlivsbevarende teknikker til behandling af følsomme data
- **Homomorf Kryptering**: Brug avancerede krypteringsteknikker til sikker beregning på krypterede data
- **Federated Learning**: Implementer distribuerede læringstilgange, der bevarer datalokalisering og privatliv

### Hændelsesrespons for AI-Systemer
- **AI-Specifikke Hændelsesprocedurer**: Udarbejd hændelsesresponsprocedurer skræddersyet til AI- og MCP-specifikke trusler
- **Automatiseret Respons**: Implementer automatiseret inddæmning og udbedring for almindelige AI-sikkerhedshændelser  
- **Retfærdighedskapaciteter**: Vedligehold retfærdighedsklarhed for AI-systemkompromitteringer og databrud
- **Genopretningsprocedurer**: Etabler procedurer for genopretning efter AI modelforgiftning, promptinjektionsangreb og tjenestekompromitteringer

## Implementeringsressourcer & Standarder

### 🏔️ Hands-On Sikkerhedstræning
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Omfattende hands-on workshop til sikring af MCP-servere i Azure
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Referencearkitektur og OWASP MCP Top 10 implementeringsvejledning

### Officiel MCP Dokumentation
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Nuværende MCP protokolspecifikation
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Officiel sikkerhedsguidance
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP autorisationsmønstre
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Transportkrav

### Microsoft Sikkerhedsløsninger
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Avanceret promptinjektionsbeskyttelse
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Omfattende AI indholdsfiltrering
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Enterprise identitets- og adgangsstyring
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Sikker hemmeligheds- og legitimationshåndtering
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Supply chain og kode-sikkerhedsscanning

### Sikkerhedsstandarder & Rammeværk
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Aktuel OAuth sikkerhedsguidance
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Webapplikationssikkerhedsrisici
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-specifikke sikkerhedsrisici
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Omfattende AI risikostyring
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Informationssikkerhedsledelsessystemer

### Implementeringsvejledninger & Tutorials
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Enterprise autentifikationsmønstre
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integration af identitetsudbyder
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Bedste praksis for tokenhåndtering
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Avancerede krypteringsmønstre

### Avancerede Sikkerhedsressourcer
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Sikker udviklingspraksis
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-specifik sikkerhedstestning
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI trusselmodelmetodik
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Privatlivsbevarende AI teknikker

### Overholdelse & Styring
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Privatlivsoverholdelse i AI-systemer
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Ansvarlig AI-implementering
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Sikkerhedskontroller for AI tjenesteudbydere
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Sundhedssektorens AI-overholdelseskrav

### DevSecOps & Automation
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Sikker AI-udviklingspipeline
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Kontinuerlig sikkerhedsvalidering
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Sikker infrastrukturdeployment
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Sikker containerisering af AI belastning

### Overvågning & Hændelsesrespons  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Omfattende overvågningsløsninger
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-specifikke hændelsesprocedurer
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Sikkerhedsinformations- og hændelsesstyring

- [Trusselsintelligens for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI trusselsintelligenskilder

## 🔄 Kontinuerlig Forbedring

### Hold dig Opdateret med Udviklende Standarder
- **MCP Specifikation Opdateringer**: Overvåg officielle ændringer i MCP specifikationen og sikkerhedsmeddelelser
- **Trusselsintelligens**: Abonner på AI-sikkerhedstrusselstrømme og sårbarhedsdatabaser  
- **Fællesskabsengagement**: Deltag i MCP sikkerhedsfællesskabsdiskussioner og arbejdsgrupper
- **Regelmæssig Vurdering**: Gennemfør kvartalsvise sikkerhedsstatusvurderinger og opdater praksis derefter

### Bidrag til MCP Sikkerhed
- **Sikkerhedsforskning**: Bidrag til MCP sikkerhedsforskning og programmer for afsløring af sårbarheder
- **Deling af Bedste Praksis**: Del sikkerhedsimplementeringer og erfaringer med fællesskabet
- **Standardudvikling**: Deltag i udvikling af MCP specifikation og oprettelse af sikkerhedsstandarder
- **Værktøjsudvikling**: Udvikl og del sikkerhedsværktøjer og biblioteker til MCP økosystemet

---

*Dette dokument afspejler MCP sikkerheds bedste praksis pr. 9. september 2026,
baseret på MCP Specifikation `2026-07-28`. Sikkerhedspraksisser bør løbende
gennemgås, efterhånden som protokollen og trusselslandskabet udvikler sig.*

## Hvad er Næste

- Læs: [MCP Security Best Practices](./mcp-security-best-practices.md)
- Vend tilbage til: [Security Module Overview](./README.md)
- Fortsæt til: [Module 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->