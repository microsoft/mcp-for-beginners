# MCP sikkerhets beste praksis – september 2026 oppdatering

Denne omfattende veiledningen skisserer viktige sikkerhets beste praksiser for
implementering av Model Context Protocol (MCP)-systemer basert på
**MCP-spesifikasjonen 2026-07-28** og gjeldende industristandarder. Disse
praksisene adresserer både tradisjonelle sikkerhetsbekymringer og AI-spesifikke trusler
som er unike for MCP-distribusjoner.

## Kritiske sikkerhetskrav

### Obligatoriske sikkerhetskontroller (MÅ-krav)

1. **Token-validering**: MCP-servere **MÅ IKKE** akseptere noen token som ikke uttrykkelig er utstedt for MCP-serveren selv
2. **Autorisasjonsverifisering**: MCP-servere som implementerer autorisasjon **MÅ** verifisere ALLE innkommende forespørsler og **MÅ IKKE** bruke økter for autentisering  
3. **Brukersamtykke**: MCP-proxyservere som bruker statiske tredjeparters klient-IDer **MÅ** innhente eksplisitt samtykke for hver MCP-klient før de videresender en autorisasjonsflyt
4. **Sikkerhet for state handle**: MCP-servere **MÅ IKKE** behandle besittelse av en
	applikasjons state handle som autentisering og **MÅ** autorisere hver
	forespørsel som bruker en slik

## Kjerne sikkerhetspraksiser

### 1. Validering og sanitering av input
- **Omfattende inputvalidering**: Valider og saniter all input for å hindre injeksjonsangrep, misledende representasjon og sårbarheter for promptinjeksjon
- **Påtvinge parameterskjema**: Implementer streng JSON-skjema validering for alle verktøyparametere og API-input
- **Innholdsfiltrering**: Bruk Microsoft Prompt Shields og Azure Content Safety for å filtrere ondsinnet innhold i prompts og svar
- **Sanitering av output**: Valider og saniter all modelloutput før den presenteres til brukere eller nedstrøms systemer

### 2. Fremragende autentisering og autorisasjon  
- **Eksterne identitetsleverandører**: Deleger autentisering til etablerte identitetsleverandører (Microsoft Entra ID, OAuth 2.1-leverandører) i stedet for å implementere egendefinert autentisering
- **Klientregistrering**: Foretrekk Client ID Metadata-dokumenter eller forhåndsregistrering; bruk foreldet dynamisk klientregistrering kun for kompatibilitet
- **Finkornede tillatelser**: Implementer granulære, verktøyspesifikke tillatelser etter minste privilegiums-prinsippet
- **Administrasjon av tokenlivssyklus**: Bruk kortvarige tilgangstoken med sikker rotasjon og korrekt målgruppevalidering
- **Multifaktorautentisering**: Krev MFA for all administrativ tilgang og sensitive operasjoner

### 3. Sikre kommunikasjonsprotokoller
- **Transportlagssikkerhet**: Bruk HTTPS med korrekt sertifikatvalidering
	for fjern HTTP MCP-kommunikasjon; bruk prosessisolasjon og miljø
	legitimasjon for lokale stdio-servere
- **Ende-til-ende kryptering**: Implementer ekstra krypteringslag for svært sensitiv data under overføring og i hvile
- **Sertifikatadministrasjon**: Oppretthold korrekt sertifikatlivssyklus med automatiserte fornyelsesprosesser
- **Protokollversjonskontroll**: Bruk MCP `2026-07-28`, inkluder påkrevd
	versjonsmetadata i hver forespørsel, og avvis ikke-støttede versjoner

### 4. Avansert ratebegrensning og ressursbeskyttelse
- **Flerlags ratebegrensning**: Implementer ratebegrensning etter bruker, legitimasjon,
  operasjon, verktøy og ressurs for å forhindre misbruk
- **Adaptiv ratebegrensning**: Bruk maskinlæringsbasert ratebegrensning som tilpasser seg bruksmønstre og trusselindikatorer
- **Ressurskvoteadministrasjon**: Sett passende grenser for beregningsressurser, minnebruk og kjøretid
- **DDoS-beskyttelse**: Distribuer omfattende DDoS-beskyttelse og trafikkanalyse-systemer

### 5. Omfattende logging og overvåking
- **Strukturert revisjonslogging**: Implementer detaljerte, søkbare logger for alle MCP-operasjoner, verktøykjøringer og sikkerhetshendelser
- **Sikkerhetsovervåking i sanntid**: Distribuer SIEM-systemer med AI-drevet anomalideteksjon for MCP arbeidsbelastninger
- **Personvernkompatibel logging**: Loggfør sikkerhetshendelser samtidig som personvernkrav og regelverk respekteres
- **Integrasjon av hendelsesrespons**: Koble loggsystemer til automatiserte hendelsesrespons-arbeidsflyter

### 6. Forbedrede sikre lagringspraksiser
- **Maskinvarebaserte sikkerhetsmoduler**: Bruk HSM-støttet nøkkellagring (Azure Key Vault, AWS CloudHSM) for kritiske kryptografiske operasjoner
- **Administrasjon av krypteringsnøkler**: Implementer korrekt nøkkelrotasjon, segregasjon og tilgangskontroller for krypteringsnøkler
- **Håndtering av hemmeligheter**: Lagre alle API-nøkler, token og legitimasjoner i dedikerte hemmelighetshåndteringssystemer
- **Dataklassifisering**: Klassifiser data basert på sensitivitet og anvend passende beskyttelsestiltak

### 7. Avansert tokenadministrasjon
- **Forhindre token-gjennompassing**: Eksplisitt forby token-gjennompassing som omgår sikkerhetskontroller
- **Validering av målgruppe**: Verifiser alltid at tokenets målgruppeklager stemmer overens med den tiltenkte MCP-serveridentiteten
- **Autorisasjon basert på claims**: Implementer finkornet autorisasjon basert på token claims og brukerattributter
- **Tokenbinding**: Verifiser at token retter seg mot tiltenkt MCP-ressurs og
	bind applikasjons state handles på serversiden til den autentiserte prinsippalen

### 8. Sikker applikasjonsstatus

- **Kryptografiske state handles**: Generer ugjennomsiktige, ikke-deterministiske handles
	for status som strekker seg over forespørsler
- **Brukerspesifikk binding**: Bind hver handle på serversiden til den autentiserte
	prinsippalen; stol ikke på en bruker-ID levert av klienten
- **Livssyklus-kontroller**: Utløp og tilbakekall handles, og definer hvordan anroperne
	gjenoppretter fra utdatert status
- **Autorisasjon per forespørsel**: Gjenta autorisasjonskontroll hver gang en handle
	blir presentert; en handle er et navn, ikke en legitimasjon

### 9. AI-spesifikke sikkerhetskontroller
- **Forsvar mot promptinjeksjon**: Distribuer Microsoft Prompt Shields med spotlighting, avgrensere og datamerkingsteknikker
- **Forebygging av verktøyforgiftning**: Verifiser verktøymetadata, overvåk for dynamiske endringer og bekreft verktøyets integritet
- **Validering av modelloutput**: Skann modelloutput for potensiell datalekkasje, skadelig innhold eller brudd på sikkerhetspolitikk
- **Beskyttelse av kontekstvindu**: Implementer kontroller for å forhindre forgiftning og manipulasjonsangrep på kontekstvinduet

### 10. Sikker kjøring av verktøy
- **Ekskjørings-sandboxing**: Kjør verktøykjøringer i containeriserte, isolerte miljøer med ressursgrenser
- **Privilegie-separasjon**: Utfør verktøy med minimale nødvendige privilegier og separerte tjenestekontoer
- **Nettverksisolasjon**: Implementer nettverkssegmentering for verktøykjøringsmiljøer
- **Overvåking av kjøring**: Overvåk verktøykjøring for unormal oppførsel, ressursbruk og sikkerhetsbrudd

### 11. Kontinuerlig sikkerhetsvalidering
- **Automatisert sikkerhetstesting**: Integrer sikkerhetstesting i CI/CD-pipelines med verktøy som GitHub Advanced Security
- **Sårbarhetsadministrasjon**: Skann jevnlig alle avhengigheter, inkludert AI-modeller og eksterne tjenester
- **Penetrasjons-testing**: Utfør regelmessige sikkerhetsvurderinger rettet spesielt mot MCP-implementasjoner
- **Sikkerhetsgjennomgang av kode**: Implementer obligatoriske sikkerhetsgjennomganger for alle MCP-relaterte kodeendringer

### 12. Sikkerhet i leverandørkjeden for AI
- **Verifisering av komponenter**: Verifiser opphav, integritet og sikkerhet for alle AI-komponenter (modeller, embeddings, APIer)
- **Avhengighetsadministrasjon**: Oppretthold oppdaterte oversikter over all programvare og AI-avhengigheter med sårbarhetssporing
- **Pålitelige arkiver**: Bruk verifiserte, pålitelige kilder for alle AI-modeller, biblioteker og verktøy
- **Overvåking av leverandørkjede**: Overvåk kontinuerlig for kompromittering i AI-tjenesteleverandører og modellarkiver

## Avanserte sikkerhetsmønstre

### Zero Trust-arkitektur for MCP
- **Aldri stol på, alltid verifiser**: Implementer kontinuerlig verifisering for alle MCP-deltakere
- **Mikrosegmentering**: Isoler MCP-komponenter med granulære nettverks- og identitetskontroller
- **Betinget tilgang**: Implementer risikobaserte tilgangskontroller som tilpasser seg kontekst og atferd
- **Kontinuerlig risikovurdering**: Evaluer dynamisk sikkerhetsstatus basert på nåværende trusselindikatorer

### Personvernbevarende AI-implementering
- **Dataminimering**: Eksponer kun minimalt nødvendig data for hver MCP-operasjon
- **Differensialt personvern**: Implementer personvernbevarende metoder for behandling av sensitiv data
- **Homomorf kryptering**: Bruk avanserte krypteringsteknikker for sikker beregning på kryptert data
- **Federated læring**: Implementer distribuerte læringstilnærminger som bevarer datalokalisering og personvern

### Hendelsesrespons for AI-systemer
- **AI-spesifikke hendelsesprosedyrer**: Utvikle hendelsesresponsprosedyrer tilpasset AI- og MCP-spesifikke trusler
- **Automatisk respons**: Implementer automatisert innkapsling og utbedring for vanlige AI-sikkerhetshendelser  
- **Rettsmedisinske kapasiteter**: Oppretthold beredskap for rettsmedisinske undersøkelser ved kompromittering av AI-systemer og datainnbrudd
- **Gjenopprettingsprosedyrer**: Etabler prosedyrer for gjenoppretting fra forgiftning av AI-modeller, promptinjeksjonsangrep og tjenestekompromisser

## Implementeringsressurser og standarder

### 🏔️ Praktisk sikkerhetstrening
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Omfattende praktisk workshop for sikring av MCP-servere i Azure
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Referansearkitektur og OWASP MCP Topp 10 implementeringsveiledning

### Offisiell MCP dokumentasjon
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Gjeldende MCP-protokollspesifikasjon
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Offisiell sikkerhetsveiledning
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP autorisasjonsmønstre
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Transportkrav

### Microsoft sikkerhetsløsninger
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Avansert forsvar mot promptinjeksjon
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Omfattende AI-innholdsfiltrering
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Bedriftsidentitet og tilgangsstyring
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Sikker håndtering av hemmeligheter og legitimasjoner
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Sikkerhetsskanning av leverandørkjede og kode

### Sikkerhetsstandarder og rammeverk
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Gjeldende OAuth sikkerhetsveiledning
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Sikkerhetsrisikoer for webapplikasjoner
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-spesifikke sikkerhetsrisikoer
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Omfattende AI risikostyring
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Ledelsessystemer for informasjonssikkerhet

### Implementeringsveiledninger og opplæringer
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Bedriftsautentiseringsmønstre
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integrasjon av identitetsleverandør
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Beste praksis for tokenadministrasjon
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Avanserte krypteringsmønstre

### Avanserte sikkerhetsressurser
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Sikker utviklingspraksis
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-spesifikk sikkerhetstesting
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodikk for trusselmodellering for AI
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Personvernbevarende AI-teknikker

### Samsvar og styring
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Personvern-samsvar i AI-systemer
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Ansvarlig AI-implementering
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Sikkerhetskontroller for AI-tjenesteleverandører
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Samsvarskrav for AI i helsevesenet

### DevSecOps og automatisering
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Sikre AI-utviklingspipelines
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Kontinuerlig sikkerhetsvalidering
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Sikker infrastrukturdistribusjon
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Sikkerhet ved containerisering av AI-arbeidsbelastninger

### Overvåking og hendelsesrespons  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Omfattende overvåkingsløsninger
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-spesifikke hendelsesprosedyrer
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Sikkerhetsinformasjon og hendelseshåndtering

- [Trusselintelligens for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI-kilder for trusselintelligens

## 🔄 Kontinuerlig forbedring

### Hold deg oppdatert med utviklende standarder
- **Oppdateringer av MCP-spesifikasjon**: Overvåk offisielle endringer i MCP-spesifikasjonen og sikkerhetsråd
- **Trusselintelligens**: Abonner på AI-sikkerhetstrusselstrømmer og sårbarhetsdatabaser  
- **Fellesskapsengasjement**: Delta i MCP-sikkerhetsfellesskapsdiskusjoner og arbeidsgrupper
- **Regelmessig vurdering**: Utfør kvartalsvise vurderinger av sikkerhetsstatus og oppdater praksis deretter

### Bidra til MCP-sikkerhet
- **Sikkerhetsforskning**: Bidra til MCP-sikkerhetsforskning og programmer for sårbarhetsavsløring
- **Deling av beste praksis**: Del sikkerhetsimplementeringer og erfaringer med fellesskapet
- **Standardutvikling**: Delta i utvikling av MCP-spesifikasjoner og opprettelse av sikkerhetsstandarder
- **Utvikling av verktøy**: Utvikle og del sikkerhetsverktøy og biblioteker for MCP-økosystemet

---

*Dette dokumentet gjenspeiler MCP sikkerhets beste praksiser per 9. september 2026,
basert på MCP-spesifikasjonen `2026-07-28`. Sikkerhetspraksis bør jevnlig
gjennomgås etter hvert som protokollen og trussellandskapet utvikler seg.*

## Hva nå

- Les: [MCP Security Best Practices](./mcp-security-best-practices.md)
- Tilbake til: [Security Module Overview](./README.md)
- Fortsett til: [Modul 3: Komme i gang](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->