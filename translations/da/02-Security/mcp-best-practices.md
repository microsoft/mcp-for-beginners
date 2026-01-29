# MCP Sikkerhedsbedste Praksis 2025

Denne omfattende guide skitserer væsentlige sikkerhedsbedste praksisser for implementering af Model Context Protocol (MCP) systemer baseret på den seneste **MCP Specification 2025-11-25** og aktuelle industristandarder. Disse praksisser adresserer både traditionelle sikkerhedsbekymringer og AI-specifikke trusler unikke for MCP-implementeringer.

## Kritiske Sikkerhedskrav

### Obligatoriske Sikkerhedskontroller (MUST Krav)

1. **Tokenvalidering**: MCP-servere **MÅ IKKE** acceptere nogen tokens, der ikke eksplicit er udstedt til MCP-serveren selv  
2. **Autorisation Verifikation**: MCP-servere, der implementerer autorisation, **SKAL** verificere ALLE indgående forespørgsler og **MÅ IKKE** bruge sessioner til autentificering  
3. **Brugersamtykke**: MCP-proxyservere, der bruger statiske klient-ID'er, **SKAL** indhente eksplicit brugersamtykke for hver dynamisk registreret klient  
4. **Sikre Session IDs**: MCP-servere **SKAL** bruge kryptografisk sikre, ikke-deterministiske session IDs genereret med sikre tilfældige talgeneratorer

## Kerne Sikkerhedspraksisser

### 1. Inputvalidering & Rensning
- **Omfattende Inputvalidering**: Valider og rens alle input for at forhindre injektionsangreb, confused deputy-problemer og prompt-injektionssårbarheder  
- **Parameter Skema Håndhævelse**: Implementer streng JSON-skema validering for alle værktøjsparametre og API-input  
- **Indholdsfiltrering**: Brug Microsoft Prompt Shields og Azure Content Safety til at filtrere ondsindet indhold i prompts og svar  
- **Outputrensning**: Valider og rens alle modeloutput før de præsenteres for brugere eller downstream-systemer

### 2. Autentificering & Autorisation Excellence  
- **Eksterne Identitetsudbydere**: Deleger autentificering til etablerede identitetsudbydere (Microsoft Entra ID, OAuth 2.1-udbydere) fremfor at implementere brugerdefineret autentificering  
- **Finkornede Rettigheder**: Implementer granulære, værktøjsspecifikke rettigheder efter princippet om mindst privilegium  
- **Token Livscyklusstyring**: Brug kortlivede adgangstokens med sikker rotation og korrekt målgruppevalidering  
- **Multi-faktor Autentificering**: Kræv MFA for al administrativ adgang og følsomme operationer

### 3. Sikre Kommunikationsprotokoller
- **Transport Layer Security**: Brug HTTPS/TLS 1.3 for al MCP-kommunikation med korrekt certifikatvalidering  
- **End-to-End Kryptering**: Implementer yderligere krypteringslag for højt følsomme data under overførsel og i hvile  
- **Certifikathåndtering**: Oprethold korrekt certifikatlivscyklusstyring med automatiserede fornyelsesprocesser  
- **Protokolversionshåndhævelse**: Brug den aktuelle MCP-protokolversion (2025-11-25) med korrekt versionsforhandling.

### 4. Avanceret Ratebegrænsning & Ressourcebeskyttelse
- **Flerlags Ratebegrænsning**: Implementer ratebegrænsning på bruger-, session-, værktøjs- og ressource-niveau for at forhindre misbrug  
- **Adaptiv Ratebegrænsning**: Brug maskinlæringsbaseret ratebegrænsning, der tilpasser sig brugsmønstre og trusselsindikatorer  
- **Ressourcekvotastyring**: Sæt passende grænser for beregningsressourcer, hukommelsesforbrug og eksekveringstid  
- **DDoS Beskyttelse**: Implementer omfattende DDoS-beskyttelse og trafik-analyssystemer

### 5. Omfattende Logning & Overvågning
- **Struktureret Revisionslogning**: Implementer detaljerede, søgbare logs for alle MCP-operationer, værktøjsudførelser og sikkerhedshændelser  
- **Realtids Sikkerhedsovervågning**: Implementer SIEM-systemer med AI-drevet anomalidetektion for MCP-arbejdsbelastninger  
- **Privatlivskompatibel Logning**: Log sikkerhedshændelser under hensyntagen til databeskyttelseskrav og regler  
- **Incident Response Integration**: Forbind logningssystemer til automatiserede hændelseshåndterings-workflows

### 6. Forbedrede Sikre Lagringspraksisser
- **Hardware Security Modules**: Brug HSM-baseret nøglelagring (Azure Key Vault, AWS CloudHSM) til kritiske kryptografiske operationer  
- **Krypteringsnøglehåndtering**: Implementer korrekt nøgle-rotation, adskillelse og adgangskontrol for krypteringsnøgler  
- **Secrets Management**: Opbevar alle API-nøgler, tokens og legitimationsoplysninger i dedikerede hemmelighedsstyringssystemer  
- **Dataklassificering**: Klassificer data baseret på følsomhedsniveauer og anvend passende beskyttelsesforanstaltninger

### 7. Avanceret Tokenstyring
- **Forhindring af Token Passthrough**: Forbyd eksplicit token passthrough-mønstre, der omgår sikkerhedskontroller  
- **Målgruppevalidering**: Verificer altid, at tokenets målgruppekrav matcher den tilsigtede MCP-serveridentitet  
- **Claims-baseret Autorisation**: Implementer finkornet autorisation baseret på tokenclaims og brugerattributter  
- **Token Binding**: Bind tokens til specifikke sessioner, brugere eller enheder, hvor det er relevant

### 8. Sikker Sessionstyring
- **Kryptografiske Session IDs**: Generer session IDs ved hjælp af kryptografisk sikre tilfældige talgeneratorer (ikke forudsigelige sekvenser)  
- **Brugerspecifik Binding**: Bind session IDs til brugerspecifik information ved hjælp af sikre formater som `<user_id>:<session_id>`  
- **Session Livscyklus Kontroller**: Implementer korrekt session udløb, rotation og ugyldiggørelsesmekanismer  
- **Session Sikkerhedsoverskrifter**: Brug passende HTTP-sikkerhedsoverskrifter til sessionsbeskyttelse

### 9. AI-specifikke Sikkerhedskontroller
- **Prompt Injection Forsvar**: Implementer Microsoft Prompt Shields med spotlighting, afgrænsere og datamærkningsteknikker  
- **Forebyggelse af Værktøjsforgiftning**: Valider værktøjsmetadata, overvåg dynamiske ændringer og verificer værktøjsintegritet  
- **Modeloutputvalidering**: Scan modeloutput for potentiel datalækage, skadeligt indhold eller overtrædelser af sikkerhedspolitikker  
- **Beskyttelse af Kontekstvindue**: Implementer kontroller for at forhindre kontekstvinduesforgiftning og manipulationsangreb

### 10. Værktøjsudførelsessikkerhed
- **Eksekveringssandboxing**: Kør værktøjsudførelser i containeriserede, isolerede miljøer med ressourcebegrænsninger  
- **Privilegieforskydning**: Udfør værktøjer med minimale nødvendige privilegier og adskilte servicekonti  
- **Netværksisolation**: Implementer netværkssegmentering for værktøjsudførelsesmiljøer  
- **Eksekveringsovervågning**: Overvåg værktøjsudførelse for unormal adfærd, ressourceforbrug og sikkerhedsovertrædelser

### 11. Kontinuerlig Sikkerhedsvalidering
- **Automatiseret Sikkerhedstest**: Integrer sikkerhedstest i CI/CD-pipelines med værktøjer som GitHub Advanced Security  
- **Sårbarhedsstyring**: Scan regelmæssigt alle afhængigheder, inklusive AI-modeller og eksterne tjenester  
- **Penetrationstest**: Udfør regelmæssige sikkerhedsvurderinger med fokus på MCP-implementeringer  
- **Sikkerhedskodegennemgang**: Implementer obligatoriske sikkerhedsgennemgange for alle MCP-relaterede kodeændringer

### 12. Supply Chain Sikkerhed for AI
- **Komponentverifikation**: Verificer oprindelse, integritet og sikkerhed for alle AI-komponenter (modeller, embeddings, API'er)  
- **Afhængighedsstyring**: Vedligehold opdaterede inventarer over al software og AI-afhængigheder med sårbarhedssporing  
- **Betroede Repositorier**: Brug verificerede, betroede kilder til alle AI-modeller, biblioteker og værktøjer  
- **Supply Chain Overvågning**: Overvåg løbende for kompromitteringer hos AI-tjenesteudbydere og modelrepositorier

## Avancerede Sikkerhedsmønstre

### Zero Trust Arkitektur for MCP
- **Aldrig Stol på, Altid Verificer**: Implementer kontinuerlig verifikation for alle MCP-deltagere  
- **Mikrosegmentering**: Isoler MCP-komponenter med granulære netværks- og identitetskontroller  
- **Betinget Adgang**: Implementer risikobaserede adgangskontroller, der tilpasser sig kontekst og adfærd  
- **Kontinuerlig Risikovurdering**: Evaluer dynamisk sikkerhedsholdning baseret på aktuelle trusselsindikatorer

### Privatlivsbevarende AI-Implementering
- **Dataminimering**: Eksponer kun det minimale nødvendige data for hver MCP-operation  
- **Differential Privacy**: Implementer privatlivsbevarende teknikker til behandling af følsomme data  
- **Homomorf Kryptering**: Brug avancerede krypteringsteknikker til sikker beregning på krypterede data  
- **Federated Learning**: Implementer distribuerede læringstilgange, der bevarer datalokation og privatliv

### Incident Response for AI-Systemer
- **AI-specifikke Incident Procedurer**: Udarbejd hændelseshåndteringsprocedurer tilpasset AI- og MCP-specifikke trusler  
- **Automatiseret Respons**: Implementer automatiseret inddæmning og udbedring for almindelige AI-sikkerhedshændelser  
- **Rettsmedicinske Kapaciteter**: Oprethold retsmedicinsk beredskab for AI-systemkompromitteringer og databrud  
- **Genopretningsprocedurer**: Etabler procedurer for genopretning fra AI-modelforgiftning, promptinjektionsangreb og tjenestekompromitteringer

## Implementeringsressourcer & Standarder

### Officiel MCP Dokumentation
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Aktuel MCP protokolspecifikation  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Officiel sikkerhedsguide  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Autentificerings- og autorisationsmønstre  
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Krav til transportlagsikkerhed

### Microsoft Sikkerhedsløsninger
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Avanceret promptinjektionsbeskyttelse  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Omfattende AI-indholdsfiltrering  
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Enterprise identitets- og adgangsstyring  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Sikker hemmeligheds- og legitimationsstyring  
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Supply chain og kode-sikkerhedsscanning

### Sikkerhedsstandarder & Rammeværk
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Aktuel OAuth sikkerhedsguide  
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Webapplikationssikkerhedsrisici  
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-specifikke sikkerhedsrisici  
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Omfattende AI risikostyring  
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Informationssikkerhedsledelsessystemer

### Implementeringsguider & Tutorials
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Enterprise autentificeringsmønstre  
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Identitetsudbyderintegration  
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Bedste praksis for tokenstyring  
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Avancerede krypteringsmønstre

### Avancerede Sikkerhedsressourcer
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Sikker udviklingspraksis  
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-specifik sikkerhedstest  
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI trusselsmodellering  
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Privatlivsbevarende AI-teknikker

### Overholdelse & Styring
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Privatlivsoverholdelse i AI-systemer  
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Ansvarlig AI-implementering  
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Sikkerhedskontroller for AI-tjenesteudbydere  
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Sundhedssektorens AI-overholdelseskrav

### DevSecOps & Automatisering
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Sikker AI-udviklingspipeline  
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Kontinuerlig sikkerhedsvalidering  
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Sikker infrastrukturudrulning  
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Sikker containerisering af AI-arbejdsbelastninger

### Overvågning & Incident Response  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Omfattende overvågningsløsninger  
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-specifikke hændelsesprocedurer  
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Sikkerhedsinformations- og hændelsesstyring  
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI trusselsintelligenskilder

## 🔄 Kontinuerlig Forbedring

### Hold Dig Opdateret med Udviklende Standarder
- **MCP Specifikationsopdateringer**: Overvåg officielle MCP-specifikationsændringer og sikkerhedsmeddelelser  
- **Trusselsintelligens**: Abonner på AI-sikkerhedstrusselsfeeds og sårbarhedsdatabaser  
- **Fællesskabsengagement**: Deltag i MCP sikkerhedsfællesskabsdiskussioner og arbejdsgrupper  
- **Regelmæssig Vurdering**: Udfør kvartalsvise sikkerhedsvurderinger og opdater praksisser i overensstemmelse hermed

### Bidrag til MCP Sikkerhed
- **Sikkerhedsforskning**: Bidrag til MCP sikkerhedsforskning og sårbarhedsafsløringsprogrammer  
- **Deling af Bedste Praksis**: Del sikkerhedsimplementeringer og erfaringer med fællesskabet
- **Standardudvikling**: Deltag i udviklingen af MCP-specifikationer og oprettelse af sikkerhedsstandarder  
- **Værktøjsudvikling**: Udvikl og del sikkerhedsværktøjer og biblioteker til MCP-økosystemet

---

*Dette dokument afspejler MCP's bedste sikkerhedspraksis pr. 18. december 2025, baseret på MCP-specifikation 2025-11-25. Sikkerhedspraksis bør regelmæssigt gennemgås og opdateres, efterhånden som protokollen og trusselslandskabet udvikler sig.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->