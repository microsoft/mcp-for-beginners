# MCP Sikkerhetsbeste praksis - Oppdatering desember 2025

> **Viktig**: Dette dokumentet gjenspeiler de nyeste [MCP-spesifikasjon 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) sikkerhetskravene og offisielle [MCP sikkerhetsbeste praksis](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Henvis alltid til gjeldende spesifikasjon for den mest oppdaterte veiledningen.

## Essensielle sikkerhetspraksiser for MCP-implementasjoner

Model Context Protocol introduserer unike sikkerhetsutfordringer som går utover tradisjonell programvaresikkerhet. Disse praksisene adresserer både grunnleggende sikkerhetskrav og MCP-spesifikke trusler inkludert prompt-injeksjon, verktøyforgiftning, sesjonskapring, confused deputy-problemer og token-passthrough-sårbarheter.

### **OBLIGATORISKE sikkerhetskrav** 

**Kritiske krav fra MCP-spesifikasjonen:**

### **OBLIGATORISKE sikkerhetskrav** 

**Kritiske krav fra MCP-spesifikasjonen:**

> **MÅ IKKE**: MCP-servere **MÅ IKKE** akseptere noen tokens som ikke eksplisitt er utstedt for MCP-serveren  
>  
> **MÅ**: MCP-servere som implementerer autorisasjon **MÅ** verifisere ALLE innkommende forespørsler  
>  
> **MÅ IKKE**: MCP-servere **MÅ IKKE** bruke sesjoner for autentisering  
>  
> **MÅ**: MCP-proxyservere som bruker statiske klient-IDer **MÅ** innhente brukerens samtykke for hver dynamisk registrerte klient  

---

## 1. **Token-sikkerhet og autentisering**

**Autentiserings- og autorisasjonskontroller:**  
   - **Grundig autorisasjonsgjennomgang**: Utfør omfattende revisjoner av MCP-serverens autorisasjonslogikk for å sikre at kun tiltenkte brukere og klienter får tilgang til ressurser  
   - **Integrasjon med eksterne identitetsleverandører**: Bruk etablerte identitetsleverandører som Microsoft Entra ID i stedet for å implementere egendefinert autentisering  
   - **Validering av token-målgruppe**: Valider alltid at tokens er eksplisitt utstedt for din MCP-server – aksepter aldri tokens fra upstream  
   - **Korrekt token-livssyklus**: Implementer sikker token-rotasjon, utløpspolicyer og forhindre token-replay-angrep  

**Beskyttet token-lagring:**  
   - Bruk Azure Key Vault eller lignende sikre credential-lagre for alle hemmeligheter  
   - Implementer kryptering for tokens både i hvile og under overføring  
   - Regelmessig credential-rotasjon og overvåking for uautorisert tilgang  

## 2. **Sesjonshåndtering og transport-sikkerhet**

**Sikre sesjonspraksiser:**  
   - **Kryptografisk sikre sesjons-IDer**: Bruk sikre, ikke-deterministiske sesjons-IDer generert med sikre tilfeldige tallgeneratorer  
   - **Brukerspesifikk binding**: Bind sesjons-IDer til brukeridentiteter med formater som `<user_id>:<session_id>` for å forhindre misbruk av sesjoner på tvers av brukere  
   - **Sesjonslivssyklusadministrasjon**: Implementer korrekt utløp, rotasjon og ugyldiggjøring for å begrense sårbarhetsvinduer  
   - **HTTPS/TLS-pålegg**: Obligatorisk HTTPS for all kommunikasjon for å forhindre avlytting av sesjons-IDer  

**Transportlagssikkerhet:**  
   - Konfigurer TLS 1.3 der det er mulig med korrekt sertifikathåndtering  
   - Implementer sertifikat-pinning for kritiske tilkoblinger  
   - Regelmessig sertifikatrotasjon og gyldighetsverifisering  

## 3. **AI-spesifikk trusselbeskyttelse** 🤖

**Forsvar mot prompt-injeksjon:**  
   - **Microsoft Prompt Shields**: Distribuer AI Prompt Shields for avansert deteksjon og filtrering av ondsinnede instruksjoner  
   - **Input-sanitærisering**: Valider og rens all input for å forhindre injeksjonsangrep og confused deputy-problemer  
   - **Innholdsgrenser**: Bruk skilletegn og datamerkingssystemer for å skille mellom betrodde instruksjoner og eksternt innhold  

**Forebygging av verktøyforgiftning:**  
   - **Validering av verktøymetadata**: Implementer integritetskontroller for verktøydefinisjoner og overvåk for uventede endringer  
   - **Dynamisk verktøyovervåking**: Overvåk kjøretidsatferd og sett opp varsling for uventede kjøringsmønstre  
   - **Godkjenningsarbeidsflyter**: Krev eksplisitt bruker-godkjenning for verktøymodifikasjoner og endringer i kapasiteter  

## 4. **Tilgangskontroll og tillatelser**

**Prinsippet om minste privilegium:**  
   - Gi MCP-servere kun minimumstillatelser som kreves for tiltenkt funksjonalitet  
   - Implementer rollebasert tilgangskontroll (RBAC) med finmaskede tillatelser  
   - Regelmessige tillatelsesgjennomganger og kontinuerlig overvåking for privilegieeskalering  

**Kjøretidstillatelseskontroller:**  
   - Påfør ressursbegrensninger for å forhindre ressursuttømmingsangrep  
   - Bruk containerisolasjon for verktøykjøremiljøer  
   - Implementer just-in-time-tilgang for administrative funksjoner  

## 5. **Innholdssikkerhet og overvåking**

**Implementering av innholdssikkerhet:**  
   - **Integrasjon med Azure Content Safety**: Bruk Azure Content Safety for å oppdage skadelig innhold, jailbreak-forsøk og policybrudd  
   - **Atferdsanalyse**: Implementer kjøretidsovervåking av atferd for å oppdage anomalier i MCP-server og verktøykjøring  
   - **Omfattende logging**: Logg alle autentiseringsforsøk, verktøypårop og sikkerhetshendelser med sikker, manipulasjonssikker lagring  

**Kontinuerlig overvåking:**  
   - Sanntidsvarsling for mistenkelige mønstre og uautoriserte tilgangsforsøk  
   - Integrasjon med SIEM-systemer for sentralisert sikkerhetshendelsesadministrasjon  
   - Regelmessige sikkerhetsrevisjoner og penetrasjonstesting av MCP-implementasjoner  

## 6. **Sikkerhet i forsyningskjeden**

**Komponentverifisering:**  
   - **Avhengighetsskanning**: Bruk automatisert sårbarhetsskanning for alle programvareavhengigheter og AI-komponenter  
   - **Opprinnelsesvalidering**: Verifiser opprinnelse, lisensiering og integritet av modeller, datakilder og eksterne tjenester  
   - **Signerte pakker**: Bruk kryptografisk signerte pakker og verifiser signaturer før distribusjon  

**Sikker utviklingspipeline:**  
   - **GitHub Advanced Security**: Implementer hemmelighetsskanning, avhengighetsanalyse og CodeQL statisk analyse  
   - **CI/CD-sikkerhet**: Integrer sikkerhetsvalidering gjennom automatiserte distribusjonspipelines  
   - **Integritetskontroll av artefakter**: Implementer kryptografisk verifisering for distribuerte artefakter og konfigurasjoner  

## 7. **OAuth-sikkerhet og forebygging av confused deputy**

**OAuth 2.1-implementering:**  
   - **PKCE-implementering**: Bruk Proof Key for Code Exchange (PKCE) for alle autorisasjonsforespørsler  
   - **Eksplisitt samtykke**: Innhent brukerens samtykke for hver dynamisk registrerte klient for å forhindre confused deputy-angrep  
   - **Validering av redirect URI**: Implementer streng validering av redirect URIer og klientidentifikatorer  

**Proxy-sikkerhet:**  
   - Forhindre autorisasjonsomgåelse gjennom utnyttelse av statiske klient-IDer  
   - Implementer korrekte samtykkearbeidsflyter for tredjeparts API-tilgang  
   - Overvåk for tyveri av autorisasjonskoder og uautorisert API-tilgang  

## 8. **Hendelseshåndtering og gjenoppretting**

**Raske responsmuligheter:**  
   - **Automatisert respons**: Implementer automatiserte systemer for credential-rotasjon og trusselinneslutning  
   - **Rollback-prosedyrer**: Mulighet for rask tilbakeføring til kjente gode konfigurasjoner og komponenter  
   - **Rettsmedisinske kapasiteter**: Detaljerte revisjonsspor og logging for hendelsesundersøkelser  

**Kommunikasjon og koordinering:**  
   - Klare eskaleringsprosedyrer for sikkerhetshendelser  
   - Integrasjon med organisasjonens hendelseshåndteringsteam  
   - Regelmessige sikkerhetshendelsessimuleringer og bordøvelser  

## 9. **Overholdelse og styring**

**Regulatorisk overholdelse:**  
   - Sørg for at MCP-implementasjoner oppfyller bransjespesifikke krav (GDPR, HIPAA, SOC 2)  
   - Implementer dataklassifisering og personvernkontroller for AI-databehandling  
   - Oppretthold omfattende dokumentasjon for revisjon av overholdelse  

**Endringshåndtering:**  
   - Formelle sikkerhetsgjennomgangsprosesser for alle MCP-systemendringer  
   - Versjonskontroll og godkjenningsarbeidsflyter for konfigurasjonsendringer  
   - Regelmessige overholdelsesvurderinger og gap-analyser  

## 10. **Avanserte sikkerhetskontroller**

**Zero Trust-arkitektur:**  
   - **Aldri stol, verifiser alltid**: Kontinuerlig verifisering av brukere, enheter og tilkoblinger  
   - **Mikrosegmentering**: Granulære nettverkskontroller som isolerer individuelle MCP-komponenter  
   - **Betinget tilgang**: Risikobaserte tilgangskontroller som tilpasses nåværende kontekst og atferd  

**Kjøretidsapplikasjonsbeskyttelse:**  
   - **Runtime Application Self-Protection (RASP)**: Distribuer RASP-teknikker for sanntids trusseldeteksjon  
   - **Applikasjonsytelsesovervåking**: Overvåk for ytelsesanomalier som kan indikere angrep  
   - **Dynamiske sikkerhetspolicyer**: Implementer sikkerhetspolicyer som tilpasses basert på gjeldende trussellandskap  

## 11. **Integrasjon med Microsofts sikkerhetsekosystem**

**Omfattende Microsoft-sikkerhet:**  
   - **Microsoft Defender for Cloud**: Cloud security posture management for MCP-arbeidsbelastninger  
   - **Azure Sentinel**: Cloud-native SIEM og SOAR-funksjoner for avansert trusseldeteksjon  
   - **Microsoft Purview**: Datastyring og overholdelse for AI-arbeidsflyter og datakilder  

**Identitets- og tilgangsstyring:**  
   - **Microsoft Entra ID**: Enterprise identitetsstyring med betingede tilgangspolicyer  
   - **Privileged Identity Management (PIM)**: Just-in-time-tilgang og godkjenningsarbeidsflyter for administrative funksjoner  
   - **Identitetsbeskyttelse**: Risikobasert betinget tilgang og automatisert trusselrespons  

## 12. **Kontinuerlig sikkerhetsevolusjon**

**Holde seg oppdatert:**  
   - **Spesifikasjonsovervåking**: Regelmessig gjennomgang av MCP-spesifikasjonsoppdateringer og endringer i sikkerhetsveiledning  
   - **Trusselintelligens**: Integrasjon av AI-spesifikke trusselstrømmer og kompromissindikatorer  
   - **Engasjement i sikkerhetsmiljøet**: Aktiv deltakelse i MCP-sikkerhetsmiljøet og programmer for sårbarhetsavsløring  

**Adaptiv sikkerhet:**  
   - **Maskinlæringsbasert sikkerhet**: Bruk ML-basert anomalideteksjon for å identifisere nye angrepsmønstre  
   - **Prediktiv sikkerhetsanalyse**: Implementer prediktive modeller for proaktiv trusselidentifikasjon  
   - **Sikkerhetsautomatisering**: Automatiserte oppdateringer av sikkerhetspolicyer basert på trusselintelligens og spesifikasjonsendringer  

---

## **Kritiske sikkerhetsressurser**

### **Offisiell MCP-dokumentasjon**  
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  

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
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)  

---

> **Sikkerhetsvarsel**: MCP sikkerhetspraksiser utvikler seg raskt. Verifiser alltid mot gjeldende [MCP-spesifikasjon](https://spec.modelcontextprotocol.io/) og [offisiell sikkerhetsdokumentasjon](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) før implementering.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->