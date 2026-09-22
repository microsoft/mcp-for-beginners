# MCP sikkerhets beste praksis - Oppdatering september 2026

> **Viktig:** Dette dokumentet gjenspeiler
> [MCP-spesifikasjonen 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> og den offisielle
> [MCP sikkerhets beste praksis](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## 🏔️ Praktisk sikkerhetstrening

For praktisk implementeringserfaring anbefaler vi **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** – en omfattende guidet ekspedisjon for å sikre MCP-servere i Azure. Workshopen dekker alle OWASP MCP Top 10-risikoer gjennom en "sårbar → utnytt → fiks → valider"-metodikk.

Alle praksiser i dette dokumentet er i samsvar med **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** for Azure-spesifikk implementeringsveiledning.

## Essensielle sikkerhetspraksiser for MCP-implementasjoner

Model Context Protocol introduserer unike sikkerhetsutfordringer som går utover tradisjonell programvaresikkerhet. Disse praksisene dekker grunnleggende krav og MCP-spesifikke trusler, inkludert promptinjeksjon, verktøytoksinering, kapring av tilstandshåndtak, forvirret fullmektig-problemer og sårbarheter ved token-gjennomgang.





### **PÅLAGTE sikkerhetskrav**

**Kritiske krav fra MCP-spesifikasjonen:**

> **MÅ IKKE**: MCP-servere **MÅ IKKE** akseptere noen tokens som ikke eksplisitt er utstedt for MCP-serveren
> 
> **MÅ**: MCP-servere som implementerer autorisasjon **MÅ** verifisere ALLE innkommende forespørsler
>  
> **MÅ IKKE**: MCP-servere **MÅ IKKE** bruke økter for autentisering
>
> **MÅ**: MCP-proxyservere som bruker en statisk tredjepartsklient-ID **MÅ**
> innhente samtykke for hver MCP-klient før autorisasjon videresendes

---

## 1. **Token-sikkerhet og autentisering**

**Autentiserings- og autorisasjonskontroller:**
   - **Grundig autorisasjonsgjennomgang**: Utfør omfattende revisjoner av MCP-serverens autorisasjonslogikk for å sikre at bare tiltenkte brukere og klienter får tilgang til ressurser
   - **Integrasjon med ekstern identitetsleverandør**: Bruk etablerte identitetsleverandører som Microsoft Entra ID i stedet for å implementere tilpasset autentisering
   - **Verifisering av token-målgruppe**: Valider alltid at tokens eksplisitt er utstedt for din MCP-server – aksepter aldri oppstrøms tokens
   - **Korrekt token-livssyklus**: Implementer sikker token-rotasjon, utløpspolicyer, og forhindre token-gjenbrukangrep

**Beskyttet tokenlagring:**
   - Bruk Azure Key Vault eller tilsvarende sikre nøkkellagre for alle hemmeligheter
   - Implementer kryptering av tokens både i ro og under overføring
   - Regelmessig rotasjon av legitimasjon og overvåking for uautorisert tilgang

## 2. **Tilstandshåndtak og transport-sikkerhet**

**Sikre praksiser for applikasjonstilstand:**

- **Ugjennomsiktige tilstandshåndtak**: Bruk sikre, ikke-deterministiske håndtak for
   applikasjonstilstand som strekker seg over forespørsler
- **Brukerspesifikk binding**: Bind håndtak server-side til den autentiserte
   prinsipal og avvis bruk på tvers av brukere
- **Livssyklushåndtering**: Utløp og tilbakekallelse av håndtak for å begrense eksponering
   vinduer
- **Autorisasjon per forespørsel**: Behandle aldri et tilstandshåndtak som autentisering;
   autoriser hver forespørsel som presenterer ett

**Transportlagssikkerhet:**

- Krev HTTPS for ekstern HTTP-transport i produksjon
- Bruk prosessisolasjon og miljølegitimasjon for lokale stdio-servere
- Konfigurer moderne TLS med riktig sertifikatrotering og validering

## 3. **AI-spesifikk trusselbeskyttelse** 🤖

**Forsvar mot promptinjeksjon:**
   - **Microsoft Prompt Shields**: Deploy AI Prompt Shields for avansert deteksjon og filtrering av ondsinnede instruksjoner
   - **Inndatasanering**: Verifiser og saner all inndata for å forhindre injeksjonsangrep og forvirret fullmektig-problemer
   - **Innholdsgrenser**: Bruk skilletegn og datamerkingssystemer for å skille mellom betrodde instruksjoner og eksternt innhold

**Forebygging av verktøytoksinering:**
   - **Validering av verktøymetadata**: Implementer integritetskontroller for verktøydefinisjoner og overvåk for uventede endringer
   - **Dynamisk verktøymonitorering**: Overvåk kjøretidsoppførsel og sett opp varsling for uventede utførelsesmønstre
   - **Godkjenningsarbeidsflyter**: Krev eksplisitt brukerbekreftelse for verktøyendringer og kapabilitetsendringer

## 4. **Tilgangskontroll og tillatelser**

**Prinsippet om minst privilegium:**
   - Gi MCP-servere kun minimum tillatelser som kreves for tiltenkt funksjonalitet
   - Implementer rollebasert tilgangskontroll (RBAC) med finmaskede tillatelser
   - Regelmessige tillatelsesgjennomganger og kontinuerlig overvåking for privilegieeskalering

**Kjøretidstillatelseskontroller:**
   - Påfør ressursbegrensninger for å forhindre ressursuttømmingsangrep
   - Bruk containerisolasjon for verktøyutførelsesmiljøer  
   - Implementer just-in-time-tilgang for administrative funksjoner

## 5. **Innholdssikkerhet og overvåking**

**Innholdssikkerhetsimplementering:**
   - **Azure Content Safety-integrasjon**: Bruk Azure Content Safety for å oppdage skadelig innhold, jailbreak-forsøk og policybrudd
   - **Atferdsanalyse**: Implementer kjøretidsovervåking for å oppdage unormale mønstre i MCP-server- og verktøyutførelse
   - **Omfattende logging**: Logg alle autentiseringsforsøk, verktøyinitialiseringer og sikkerhetshendelser med sikker, manipulasjonssikker lagring

**Kontinuerlig overvåking:**
   - Varsling i sanntid for mistenkelige mønstre og uautoriserte tilgangsforsøk  
   - Integrasjon med SIEM-systemer for sentralisert sikkerhetshendelseshåndtering
   - Regelmessige sikkerhetsrevisjoner og penetrasjonstesting av MCP-implementasjoner

## 6. **Sikkerhet i leverandørkjeden**

**Komponentverifisering:**
   - **Avhengighetsskanning**: Bruk automatisert sårbarhetsskanning for alle programvareavhengigheter og AI-komponenter
   - **Opprinnelsesvalidering**: Verifiser opprinnelse, lisensiering og integritet av modeller, datakilder og eksterne tjenester
   - **Signerte pakker**: Bruk kryptografisk signerte pakker og verifiser signaturer før distribusjon

**Sikker utviklingspipeline:**
   - **GitHub Advanced Security**: Implementer hemmelighetsskanning, avhengighetsanalyse og CodeQL statisk analyse
   - **CI/CD sikkerhet**: Integrer sikkerhetsvalidering gjennom automatiserte distribusjonspipelines
   - **Integritet for artefakter**: Implementer kryptografisk verifisering for distribuerte artefakter og konfigurasjoner

## 7. **OAuth-sikkerhet og forebygging av forvirret fullmektig**

**OAuth 2.1-implementering:**
   - **PKCE-implementering**: Bruk Proof Key for Code Exchange (PKCE) for alle autorisasjonsforespørsler
    - **Klientregistrering**: Foretrekk Client ID Metadata Documents eller
       forhåndsregistrering; bruk avskrevet dynamisk klientregistrering kun som
       bakoverkompatibilitet
    - **Eksplisitt samtykke**: MCP-proxyer som bruker en statisk tredjepartsklient-ID må
       innhente samtykke for hver MCP-klient før autorisasjon videresendes
   - **Validering av Redirect URI**: Implementer streng validering av redirect URIer og klientidentifikatorer

**Proxy-sikkerhet:**
   - Forhindre autorisasjonsomgåelse gjennom utnyttelse av statisk klient-ID
   - Implementer riktige samtykke-arbeidsflyter for tredjeparts API-tilgang
   - Overvåk for tyveri av autorisasjonskode og uautorisert API-tilgang

## 8. **Håndtering av hendelser og gjenoppretting**

**Rask responsevne:**

   - **Automatisert respons**: Implementer automatiserte systemer for credential-rotasjon og trusselinneslutning
   - **Tilbakerulleringsprosedyrer**: Evne til raskt å gå tilbake til kjente gode konfigurasjoner og komponenter
   - **Rettsmedisinske kapasiteter**: Detaljerte revisjonsspor og logging for hendelsesundersøkelser

**Kommunikasjon og koordinering:**
   - Klare eskaleringsprosedyrer for sikkerhetshendelser
   - Integrasjon med organisatoriske hendelsesresponsteam
   - Regelmessige sikkerhetshendelsessimuleringer og bordøvelser

## 9. **Etterlevelse og styring**

**Regulatorisk etterlevelse:**
   - Sikre at MCP-implementeringer oppfyller bransjespesifikke krav (GDPR, HIPAA, SOC 2)
   - Implementere dataklassifisering og personvernkontroller for AI-databehandling
   - Opprettholde omfattende dokumentasjon for samsvarrevisjon

**Endringshåndtering:**
   - Formelle sikkerhetsvurderingsprosesser for alle MCP-systemendringer
   - Versjonskontroll og godkjenningsarbeidsflyter for konfigurasjonsendringer
   - Regelmessige samsvarsvurderinger og gap-analyser

## 10. **Avanserte sikkerhetskontroller**

**Zero Trust-arkitektur:**
   - **Aldri stol på, alltid verifiser**: Kontinuerlig verifisering av brukere, enheter og tilkoblinger
   - **Mikrosegmentering**: Granulære nettverkskontroller som isolerer individuelle MCP-komponenter
   - **Betinget tilgang**: Risikobaserte tilgangskontroller som tilpasses gjeldende kontekst og atferd

**Kjøretidsbeskyttelse av applikasjoner:**
   - **Runtime Application Self-Protection (RASP)**: Distribuer RASP-teknikker for sanntids trusseldeteksjon
   - **Applikasjonsytelsesovervåking**: Overvåk ytelsesanomalier som kan indikere angrep
   - **Dynamiske sikkerhetspolicyer**: Implementer sikkerhetspolicyer som tilpasses basert på gjeldende trussellandskap

## 11. **Integrasjon med Microsofts sikkerhetsekosystem**

**Omfattende Microsoft-sikkerhet:**
   - **Microsoft Defender for Cloud**: Cloud Security Posture Management for MCP-arbeidsbelastninger
   - **Azure Sentinel**: Cloud-native SIEM- og SOAR-funksjoner for avansert trusseldeteksjon
   - **Microsoft Purview**: Datastyring og samsvar for AI-arbidsflyter og datakilder

**Identitets- og tilgangsstyring:**
   - **Microsoft Entra ID**: Enterprise identitetsadministrasjon med betingede tilgangspolicyer
   - **Privileged Identity Management (PIM)**: Just-in-time-tilgang og godkjenningsarbeidsflyter for administrative funksjoner
   - **Identity Protection**: Risikobasert betinget tilgang og automatisert trusselrespons

## 12. **Kontinuerlig sikkerhetsutvikling**

**Hold deg oppdatert:**
   - **Spesifikasjonsovervåkning**: Regelmessig gjennomgang av MCP-spesifikasjonsoppdateringer og endringer i sikkerhetsveiledninger
   - **Trusselintelligens**: Integrasjon av AI-spesifikke trusselstrømmer og kompromissindikatorer
   - **Engasjement i sikkerhetsmiljøet**: Aktiv deltakelse i MCP-sikkerhetsmiljøet og programmer for sårbarhetsrapportering

**Adaptiv sikkerhet:**
   - **Maskinlæringssikkerhet**: Bruk ML-basert anomalideteksjon for å identifisere nye angrepsmønstre
   - **Prediktiv sikkerhetsanalyse**: Implementer prediktive modeller for proaktiv trusselidentifikasjon
   - **Sikkerhetsautomatisering**: Automatiserte sikkerhetspolicyoppdateringer basert på trusselintelligens og spesifikasjonsendringer

---

## **Kritiske sikkerhetsressurser**

### **Offisiell MCP-dokumentasjon**
- [MCP Specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP sikkerhetsressurser**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Omfattende OWASP MCP Topp 10 med Azure-implementasjon
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Offisielle OWASP MCP sikkerhetsrisikoer
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktisk sikkerhetstrening for MCP på Azure

### **Microsoft sikkerhetsløsninger**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Sikkerhetsstandarder**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

### **Implementeringsguider**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID med MCP-servere](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Sikkerhetsmerknad:** MCP sikkerhetspraksis utvikler seg raskt. Alltid verifiser
> mot gjeldende [MCP-spesifikasjon](https://modelcontextprotocol.io/specification/2026-07-28/)
> og [offisiell sikkerhetsdokumentasjon](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> før implementering.

## Hva er neste steg

- Les: [MCP Security Controls](./mcp-security-controls.md)
- Gå tilbake til: [Security Module Overview](./README.md)
- Fortsett til: [Module 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->