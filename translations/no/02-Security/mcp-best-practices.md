# MCP Sikkerhets beste praksis 2025

Denne omfattende guiden skisserer essensielle sikkerhets beste praksiser for implementering av Model Context Protocol (MCP) systemer basert på den nyeste **MCP Spesifikasjon 2025-11-25** og gjeldende industristandarder. Disse praksisene adresserer både tradisjonelle sikkerhetsbekymringer og AI-spesifikke trusler unike for MCP-distribusjoner.

## Kritiske sikkerhetskrav

### Obligatoriske sikkerhetskontroller (MÅ-krav)

1. **Token-validering**: MCP-servere **MÅ IKKE** akseptere noen tokens som ikke eksplisitt ble utstedt for MCP-serveren selv
2. **Autorisasjonsverifisering**: MCP-servere som implementerer autorisasjon **MÅ** verifisere ALLE innkommende forespørsler og **MÅ IKKE** bruke økter for autentisering  
3. **Brukersamtykke**: MCP-proxyservere som bruker statiske klient-IDer **MÅ** innhente eksplisitt brukersamtykke for hver dynamisk registrerte klient
4. **Sikre økt-IDer**: MCP-servere **MÅ** bruke kryptografisk sikre, ikke-deterministiske økt-IDer generert med sikre tilfeldige tallgeneratorer

## Kjerne sikkerhetspraksiser

### 1. Inndata validering & sanitering
- **Omfattende inndata validering**: Valider og saniter alle inndata for å forhindre injeksjonsangrep, forvirret stedfortreder-problemer og prompt-injeksjons sårbarheter
- **Parameter skjema håndhevelse**: Implementer streng JSON-skjema validering for alle verktøyparametere og API-inndata
- **Innholdsfiltrering**: Bruk Microsoft Prompt Shields og Azure Content Safety for å filtrere ondsinnet innhold i prompts og svar
- **Utdata sanitering**: Valider og saniter alle modellutdata før de presenteres for brukere eller nedstrøms systemer

### 2. Autentisering & autorisasjonsekspertise  
- **Eksterne identitetsleverandører**: Deleger autentisering til etablerte identitetsleverandører (Microsoft Entra ID, OAuth 2.1-leverandører) i stedet for å implementere egendefinert autentisering
- **Finmasket tillatelser**: Implementer granulære, verktøyspesifikke tillatelser i henhold til minste privilegium-prinsippet
- **Token livssyklusadministrasjon**: Bruk kortvarige tilgangstokens med sikker rotasjon og korrekt publikumvalidering
- **Multifaktorautentisering**: Krev MFA for all administrativ tilgang og sensitive operasjoner

### 3. Sikre kommunikasjonsprotokoller
- **Transport Layer Security**: Bruk HTTPS/TLS 1.3 for all MCP-kommunikasjon med korrekt sertifikatvalidering
- **Ende-til-ende kryptering**: Implementer ekstra krypteringslag for svært sensitiv data under overføring og i hvile
- **Sertifikatadministrasjon**: Oppretthold korrekt sertifikat livssyklusadministrasjon med automatiserte fornyelsesprosesser
- **Protokollversjon håndhevelse**: Bruk gjeldende MCP protokollversjon (2025-11-25) med korrekt versjonsforhandling.

### 4. Avansert ratebegrensning & ressursbeskyttelse
- **Flerlags ratebegrensning**: Implementer ratebegrensning på bruker-, økt-, verktøy- og ressursnivå for å forhindre misbruk
- **Adaptiv ratebegrensning**: Bruk maskinlæringsbasert ratebegrensning som tilpasser seg bruksmønstre og trusselindikatorer
- **Ressurskvotestyring**: Sett passende grenser for beregningsressurser, minnebruk og kjøretid
- **DDoS-beskyttelse**: Distribuer omfattende DDoS-beskyttelse og trafikkanalyse systemer

### 5. Omfattende logging & overvåking
- **Strukturert revisjonslogging**: Implementer detaljerte, søkbare logger for alle MCP-operasjoner, verktøykjøringer og sikkerhetshendelser
- **Sanntids sikkerhetsovervåking**: Distribuer SIEM-systemer med AI-drevet anomali-deteksjon for MCP arbeidsbelastninger
- **Personvernkompatibel logging**: Loggfør sikkerhetshendelser samtidig som du respekterer databeskyttelseskrav og regelverk
- **Integrasjon for hendelseshåndtering**: Koble loggsystemer til automatiserte hendelseshåndteringsarbeidsflyter

### 6. Forbedrede sikre lagringspraksiser
- **Maskinvare sikkerhetsmoduler**: Bruk HSM-støttet nøkkellagring (Azure Key Vault, AWS CloudHSM) for kritiske kryptografiske operasjoner
- **Krypteringsnøkkeladministrasjon**: Implementer korrekt nøkkelrotasjon, separasjon og tilgangskontroller for krypteringsnøkler
- **Hemmelighetshåndtering**: Lagre alle API-nøkler, tokens og legitimasjon i dedikerte hemmelighetshåndteringssystemer
- **Dataklassifisering**: Klassifiser data basert på sensitivitet og anvend passende beskyttelsestiltak

### 7. Avansert token-administrasjon
- **Forhindring av token-gjennomgang**: Forbud eksplisitt token-gjennomgangsmønstre som omgår sikkerhetskontroller
- **Publikumvalidering**: Verifiser alltid at token-publikum samsvarer med den tiltenkte MCP-serveridentiteten
- **Autorisasjon basert på claims**: Implementer finmasket autorisasjon basert på token claims og brukerattributter
- **Token-binding**: Bind tokens til spesifikke økter, brukere eller enheter der det er hensiktsmessig

### 8. Sikker øktadministrasjon
- **Kryptografiske økt-IDer**: Generer økt-IDer ved bruk av kryptografisk sikre tilfeldige tallgeneratorer (ikke forutsigbare sekvenser)
- **Brukerspesifikk binding**: Bind økt-IDer til brukerspesifikk informasjon ved bruk av sikre formater som `<user_id>:<session_id>`
- **Økt livssyklus kontroller**: Implementer korrekt øktutløp, rotasjon og ugyldiggjøringsmekanismer
- **Sikkerhetsoverskrifter for økter**: Bruk passende HTTP sikkerhetsoverskrifter for øktbeskyttelse

### 9. AI-spesifikke sikkerhetskontroller
- **Forsvar mot prompt-injeksjon**: Distribuer Microsoft Prompt Shields med spotlighting, avgrensere og datamerkingsteknikker
- **Forebygging av verktøyforgiftning**: Valider verktøymetadata, overvåk for dynamiske endringer, og verifiser verktøyintegritet
- **Validering av modellutdata**: Skann modellutdata for potensiell datalekkasje, skadelig innhold eller brudd på sikkerhetspolicyer
- **Beskyttelse av kontekstvindu**: Implementer kontroller for å forhindre forgiftning og manipulasjonsangrep på kontekstvinduet

### 10. Sikkerhet ved verktøykjøring
- **Kjøring i sandkasse**: Kjør verktøykjøringer i containeriserte, isolerte miljøer med ressursbegrensninger
- **Privilegium-separasjon**: Kjør verktøy med minimale nødvendige privilegier og separate tjenestekontoer
- **Nettverksisolasjon**: Implementer nettverkssegmentering for verktøykjøringsmiljøer
- **Overvåking av kjøring**: Overvåk verktøykjøring for unormal oppførsel, ressursbruk og sikkerhetsbrudd

### 11. Kontinuerlig sikkerhetsvalidering
- **Automatisert sikkerhetstesting**: Integrer sikkerhetstesting i CI/CD-pipelines med verktøy som GitHub Advanced Security
- **Sårbarhetsstyring**: Skann regelmessig alle avhengigheter, inkludert AI-modeller og eksterne tjenester
- **Penetrasjonstesting**: Gjennomfør regelmessige sikkerhetsvurderinger spesielt rettet mot MCP-implementasjoner
- **Sikkerhetskodegjennomganger**: Implementer obligatoriske sikkerhetsgjennomganger for alle MCP-relaterte kodeendringer

### 12. Leverandørkjede-sikkerhet for AI
- **Komponentverifisering**: Verifiser opprinnelse, integritet og sikkerhet for alle AI-komponenter (modeller, embeddings, APIer)
- **Avhengighetsstyring**: Oppretthold oppdaterte oversikter over all programvare og AI-avhengigheter med sårbarhetssporing
- **Pålitelige arkiver**: Bruk verifiserte, pålitelige kilder for alle AI-modeller, biblioteker og verktøy
- **Overvåking av leverandørkjeden**: Overvåk kontinuerlig for kompromitteringer hos AI-tjenesteleverandører og modellarkiver

## Avanserte sikkerhetsmønstre

### Zero Trust-arkitektur for MCP
- **Aldri stol, alltid verifiser**: Implementer kontinuerlig verifisering for alle MCP-deltakere
- **Mikrosegmentering**: Isoler MCP-komponenter med granulære nettverks- og identitetskontroller
- **Betinget tilgang**: Implementer risikobaserte tilgangskontroller som tilpasser seg kontekst og atferd
- **Kontinuerlig risikovurdering**: Evaluer dynamisk sikkerhetsstatus basert på gjeldende trusselindikatorer

### Personvernbevarende AI-implementering
- **Dataminimering**: Eksponer kun minimum nødvendig data for hver MCP-operasjon
- **Differensiell personvern**: Implementer personvernbevarende teknikker for sensitiv databehandling
- **Homomorf kryptering**: Bruk avanserte krypteringsteknikker for sikker beregning på krypterte data
- **Federert læring**: Implementer distribuerte læringstilnærminger som bevarer datalokalisering og personvern

### Hendelseshåndtering for AI-systemer
- **AI-spesifikke hendelsesprosedyrer**: Utvikle hendelseshåndteringsprosedyrer tilpasset AI- og MCP-spesifikke trusler
- **Automatisert respons**: Implementer automatisert inneslutning og utbedring for vanlige AI-sikkerhetshendelser  
- **Rettsmedisinske kapasiteter**: Oppretthold beredskap for rettsmedisinsk analyse ved AI-systemkompromitteringer og datainnbrudd
- **Gjenopprettingsprosedyrer**: Etabler prosedyrer for gjenoppretting fra AI-modellforgiftning, prompt-injeksjonsangrep og tjenestekompromitteringer

## Implementeringsressurser & standarder

### Offisiell MCP-dokumentasjon
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Gjeldende MCP protokollspesifikasjon
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Offisiell sikkerhetsveiledning
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Autentiserings- og autorisasjonsmønstre
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Transportlagssikkerhetskrav

### Microsoft sikkerhetsløsninger
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Avansert beskyttelse mot prompt-injeksjon
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Omfattende AI-innholdsfiltrering
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Enterprise identitets- og tilgangsstyring
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Sikker hemmelighets- og legitimasjonshåndtering
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Leverandørkjede- og kodesikkerhetsskanning

### Sikkerhetsstandarder & rammeverk
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Gjeldende OAuth sikkerhetsveiledning
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Sikkerhetsrisikoer for webapplikasjoner
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-spesifikke sikkerhetsrisikoer
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Omfattende AI risikostyring
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Informasjonssikkerhetsstyringssystemer

### Implementeringsguider & opplæringer
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Enterprise autentiseringsmønstre
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integrasjon av identitetsleverandør
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Beste praksis for token-administrasjon
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Avanserte krypteringsmønstre

### Avanserte sikkerhetsressurser
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Sikker utviklingspraksis
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-spesifikk sikkerhetstesting
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI trusselmodellering metodikk
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Personvernbevarende AI-teknikker

### Samsvar & styring
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Personvern samsvar i AI-systemer
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Ansvarlig AI-implementering
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Sikkerhetskontroller for AI-tjenesteleverandører
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Helsevesen AI samsvarskrav

### DevSecOps & automatisering
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Sikker AI-utviklingspipeline
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Kontinuerlig sikkerhetsvalidering
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Sikker infrastrukturdistribusjon
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Sikkerhet ved containerisering av AI-arbeidsbelastninger

### Overvåking & hendelseshåndtering  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Omfattende overvåkingsløsninger
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-spesifikke hendelsesprosedyrer
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Sikkerhetsinformasjon og hendelseshåndtering
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI trusselintelligenskilder

## 🔄 Kontinuerlig forbedring

### Hold deg oppdatert med utviklende standarder
- **MCP Spesifikasjonsoppdateringer**: Overvåk offisielle MCP spesifikasjonsendringer og sikkerhetsvarsler
- **Trusselintelligens**: Abonner på AI sikkerhetstrusselstrømmer og sårbarhetsdatabaser  
- **Fellesskapsengasjement**: Delta i MCP sikkerhetsfellesskapets diskusjoner og arbeidsgrupper
- **Regelmessig vurdering**: Gjennomfør kvartalsvise sikkerhetsvurderinger og oppdater praksiser deretter

### Bidra til MCP-sikkerhet
- **Sikkerhetsforskning**: Bidra til MCP sikkerhetsforskning og sårbarhetsavsløringsprogrammer
- **Deling av beste praksis**: Del sikkerhetsimplementeringer og erfaringer med fellesskapet
- **Standardutvikling**: Delta i utviklingen av MCP-spesifikasjoner og opprettelse av sikkerhetsstandarder
- **Verktøyutvikling**: Utvikle og dele sikkerhetsverktøy og biblioteker for MCP-økosystemet

---

*Dette dokumentet gjenspeiler MCPs beste sikkerhetspraksis per 18. desember 2025, basert på MCP-spesifikasjon 2025-11-25. Sikkerhetspraksis bør jevnlig gjennomgås og oppdateres ettersom protokollen og trussellandskapet utvikler seg.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->