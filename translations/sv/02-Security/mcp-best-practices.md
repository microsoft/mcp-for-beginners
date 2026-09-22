# MCP Säkerhetsrutiner - Uppdatering september 2026

Denna omfattande guide beskriver viktiga säkerhetsrutiner för
implementering av Model Context Protocol (MCP) system baserade på
**MCP Specification 2026-07-28** och aktuella branschstandarder. Dessa
rutiner adresserar både traditionella säkerhetsrisker och AI-specifika hot
unika för MCP-installationer.

## Kritiska säkerhetskrav

### Obligatoriska säkerhetskontroller (MÅSTE-krav)

1. **Token-validering**: MCP-servrar **FÅR INTE** acceptera några tokens som inte uttryckligen utfärdats för MCP-servern själv
2. **Behörighetsverifiering**: MCP-servrar som implementerar auktorisering **MÅSTE** verifiera ALLA inkommande förfrågningar och **FÅR INTE** använda sessioner för autentisering  
3. **Användarsamtycke**: MCP-proxyservrar som använder statiska tredjepartsklient-ID:n **MÅSTE** erhålla uttryckligt samtycke för varje MCP-klient innan en auktoriseringsflöde vidarebefordras
4. **Säkerhet för state-handle**: MCP-servrar **FÅR INTE** behandla innehav av ett
	application state handle som autentisering och **MÅSTE** auktorisera varje
	förfrågan som använder en sådan

## Kärnsäkerhetspraxis

### 1. Indatavalidering & Sanitering
- **Omfattande indatavalidering**: Validera och sanera all indata för att förhindra injektionsattacker, confused deputy-problem och prompt-injektionssårbarheter
- **Parameter-schema-implementering**: Implementera strikt JSON-schema validering för alla verktygsparametrar och API-indata
- **Innehållsfiltrering**: Använd Microsoft Prompt Shields och Azure Content Safety för att filtrera skadligt innehåll i prompts och svar
- **Utdata-sanitering**: Validera och sanera all modellutdata innan presentation till användare eller efterföljande system

### 2. Autentisering & Auktoriseringsexcellens  
- **Externa identitetsleverantörer**: Delegera autentisering till etablerade identitetsleverantörer (Microsoft Entra ID, OAuth 2.1-leverantörer) istället för att implementera egen autentisering
- **Klientregistrering**: Föredra Client ID Metadata Documents eller förregistrering; använd föråldrad Dynamic Client Registration endast för kompatibilitet
- **Finkorniga behörigheter**: Implementera granulära, verktygsspecifika behörigheter enligt principen om minsta privilegium
- **Token livscykelhantering**: Använd kortlivade access tokens med säker rotation och korrekt målgruppsvalidering
- **Multi-faktorautentisering**: Kräv MFA för all administrativ åtkomst och känsliga operationer

### 3. Säker kommunikationsprotokoll
- **Transport Layer Security**: Använd HTTPS med korrekt certifikatvalidering
	för fjärr-HTTP MCP-kommunikation; använd processisolering och miljö-
	behörigheter för lokala stdio-servrar
- **End-to-End-kryptering**: Implementera ytterligare krypteringslager för mycket känsliga data under överföring och i vila
- **Certifikathantering**: Underhåll korrekt certifikatlivscykelhantering med automatiska förnyelseprocesser
- **Protokollversionshantering**: Använd MCP `2026-07-28`, inkludera obligatorisk
	versionsmetadata på varje förfrågan, och avvisa icke-stödda versioner

### 4. Avancerad begränsning av takthastighet & Resursskydd
- **Flerlagrig takthastighetsbegränsning**: Implementera takthastighetsbegränsning per användare, behörighet,
  operation, verktyg och resurs för att förhindra missbruk
- **Adaptiv takthastighetsbegränsning**: Använd maskininlärningsbaserad takthastighetsbegränsning som anpassar sig till användningsmönster och hotindikatorer
- **Resurskvotshantering**: Sätt lämpliga gränser för beräkningsresurser, minnesanvändning och exekveringstid
- **DDoS-skydd**: Implementera omfattande DDoS-skydd och trafikanalysystem

### 5. Omfattande loggning & övervakning
- **Strukturerad revisionsloggning**: Implementera detaljerade, sökbara loggar för alla MCP-operationer, verktygskörningar och säkerhetshändelser
- **Säkerhetsövervakning i realtid**: Distributera SIEM-system med AI-driven avvikelsedetektering för MCP-arbetsbelastningar
- **Integritetsskyddad loggning**: Logga säkerhetshändelser samtidigt som krav och regler för dataskydd följs
- **Incidenthantering integration**: Koppla loggsystem till automatiserade incidenthanteringsarbetsflöden

### 6. Förbättrade säkra lagringsrutiner
- **Hardware Security Modules**: Använd HSM-backad nyckellagring (Azure Key Vault, AWS CloudHSM) för kritiska kryptografiska operationer
- **Hantera krypteringsnycklar**: Implementera korrekt nyckelrotation, segregation och åtkomstkontroller för krypteringsnycklar
- **Hantering av hemligheter**: Lagra alla API-nycklar, tokens och behörigheter i dedikerade hemlighetshanteringssystem
- **Dataklassificering**: Klassificera data baserat på känslighetsnivåer och tillämpa lämpliga skyddsåtgärder

### 7. Avancerad tokenhantering
- **Förebyggande av token-passthrough**: Explicit förbjuda token-passthrough-mönster som kringgår säkerhetskontroller
- **Validering av målgrupp**: Verifiera alltid att token-målgruppsanspråk stämmer överens med den avsedda MCP-serverns identitet
- **Auktorisering baserad på anspråk**: Implementera finkornig auktorisering baserad på token-anspråk och användarattribut
- **Tokenbinding**: Validera att tokens riktar sig mot avsett MCP-resurs och
	binda application state handles server-side till den autentiserade huvudmannen

### 8. Säker applikationsstat

- **Kryptografiska state handles**: Generera opaka, icke-deterministiska handles
	för stat som sträcker sig över förfrågningar
- **Användarspecifik bindning**: Binda varje handle server-side till den autentiserade
	huvudmannen; lita inte på användar-ID som tillhandahålls av klienten
- **Livscykelkontroller**: Låt handles löpa ut och återkallas, och definiera hur anropare
	återhämtar sig från föråldrad stat
- **Auktorisering per förfrågan**: Kontrollera auktorisering igen varje gång en handle
	uppvisas; en handle är ett namn, inte en referens

### 9. AI-specifika säkerhetskontroller
- **Försvar mot prompt-injektion**: Använd Microsoft Prompt Shields med spotlighting, avgränsare och datamarkeringstekniker
- **Förebyggande av verktygsförgiftning**: Validera verktygsmetadata, övervaka dynamiska förändringar och verifiera verktygsintegritet
- **Validering av modellutdata**: Genomsök modellutdata för potentiellt dataläckage, skadligt innehåll eller brott mot säkerhetspolicy
- **Skydd av kontextfönster**: Implementera kontroller för att förhindra förgiftning och manipuleringsattacker mot kontextfönstret

### 10. Säker verktygsexekvering
- **Exekvering i sandlåda**: Kör verktygsexekveringar i containeriserade, isolerade miljöer med resursbegränsningar
- **Behörighetsseparering**: Kör verktyg med minimala nödvändiga privilegier och separata tjänstekonton
- **Nätverksisolering**: Implementera nätverkssegmentering för verktygsexekveringsmiljöer
- **Exekveringsövervakning**: Övervaka verktygsexekvering för avvikande beteende, resursanvändning och säkerhetsöverträdelser

### 11. Kontinuerlig säkerhetsvalidering
- **Automatiserad säkerhetstestning**: Integrera säkerhetstestning i CI/CD-pipelines med verktyg som GitHub Advanced Security
- **Sårbarhetshantering**: Skanna regelbundet alla beroenden, inklusive AI-modeller och externa tjänster
- **Penetrationstestning**: Utför regelbundna säkerhetsbedömningar specifikt riktade mot MCP-implementationer
- **Säkerhetsgranskning av kod**: Inför obligatoriska säkerhetsgranskningar för alla MCP-relaterade kodändringar

### 12. Leverantörskedjesäkerhet för AI
- **Komponentverifiering**: Verifiera ursprung, integritet och säkerhet för alla AI-komponenter (modeller, embeddings, API:er)
- **Beroendehantering**: Underhåll aktuella inventarier över all programvara och AI-beroenden med sårbarhetsspårning
- **Betrodda arkiv**: Använd verifierade, betrodda källor för alla AI-modeller, bibliotek och verktyg
- **Övervakning av leverantörskedja**: Övervaka kontinuerligt för komprometteringar hos AI-tjänsteleverantörer och modellarkiv

## Avancerade säkerhetsmönster

### Zero Trust-arkitektur för MCP
- **Lita aldrig, verifiera alltid**: Implementera kontinuerlig verifiering för alla MCP-deltagare
- **Mikrosegmentering**: Isolera MCP-komponenter med granulära nätverks- och identitetskontroller
- **Villkorlig åtkomst**: Implementera riskbaserade åtkomstkontroller som anpassar sig till kontext och beteende
- **Kontinuerlig riskbedömning**: Utvärdera dynamiskt säkerhetsläget baserat på aktuella hotindikatorer

### Sekretessbevarande AI-implementering
- **Dataminimering**: Exponera endast minsta nödvändiga data för varje MCP-operation
- **Differential privacy**: Implementera sekretessbevarande tekniker för känslig databehandling
- **Homomorf kryptering**: Använd avancerade krypteringstekniker för säker beräkning på krypterad data
- **Federerat lärande**: Implementera distribuerade lärandeapproacher som bevarar datalokalisering och sekretess

### Incidenthantering för AI-system
- **AI-specifika incidentprocedurer**: Utveckla incidenthanteringsprocedurer anpassade för AI och MCP-specifika hot
- **Automatiserad respons**: Implementera automatiserad innehållning och åtgärd för vanliga AI-säkerhetsincidenter  
- **Rättsmedicinska möjligheter**: Upprätthåll rättsmedicinsk beredskap för AI-systemkompromisser och dataintrång
- **Återhämtningsprocedurer**: Etablera procedurer för återhämtning från AI-modelförgiftning, prompt-injektionsattacker och tjänstekompromisser

## Implementeringsresurser & standarder

### 🏔️ Praktisk säkerhetsträning
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Omfattande praktisk workshop för att säkra MCP-servrar i Azure
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Referensarkitektur och OWASP MCP Top 10-implementeringsanvisningar

### Officiell MCP-dokumentation
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Aktuell MCP protokollspecificering
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Officiell säkerhetsvägledning
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP-auktoriseringsmönster
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Transportkrav

### Microsoft säkerhetslösningar
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Avancerat skydd mot prompt-injektion
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Omfattande AI-innehållsfiltrering
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Företagsidentitet och åtkomsthantering
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Säker hantering av hemligheter och behörigheter
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Säkerhetsskanning av leverantörskedja och kod

### Säkerhetsstandarder & ramverk
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Aktuell OAuth-säkerhetsvägledning
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Säkerhetsrisker för webbapplikationer
- [OWASP Top 10 för LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-specifika säkerhetsrisker
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Omfattande AI-riskhantering
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Informationssäkerhetssystem

### Implementeringsguider & handledningar
- [Azure API Management som MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Företagsautentiseringsmönster
- [Microsoft Entra ID med MCP-servrar](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integration med identitetsleverantör
- [Implementering av säker tokenlagring](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Bästa praxis för tokenhantering
- [End-to-End-kryptering för AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Avancerade krypteringsmönster

### Avancerade säkerhetsresurser
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Säker utvecklingspraxis
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-specifik säkerhetstestning
- [Hotmodellering för AI-system](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI-hotmodelleringmetodik
- [Sekretessingenjörskap för AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Sekretessbevarande AI-tekniker

### Efterlevnad & styrning
- [GDPR-efterlevnad för AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Sekretessöverensstämmelse i AI-system
- [AI-styrningsramverk](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Ansvarsfull AI-implementering
- [SOC 2 för AI-tjänster](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Säkerhetskontroller för AI-tjänsteleverantörer
- [HIPAA-efterlevnad för AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Hälso- och sjukvårds AI-efterlevnadskrav

### DevSecOps & automatisering
- [DevSecOps-pipeline för AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Säkra utvecklingspipelines för AI
- [Automatiserad säkerhetstestning](https://learn.microsoft.com/security/engineering/devsecops) - Kontinuerlig säkerhetsvalidering
- [Infrastruktur som kod-säkerhet](https://learn.microsoft.com/security/engineering/infrastructure-security) - Säker infrastrukturdistribution
- [Containersäkerhet för AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Säkerhet vid containerisering av AI-arbetsbelastning

### Övervakning & incidenthantering  
- [Azure Monitor för AI-arbetsbelastningar](https://learn.microsoft.com/azure/azure-monitor/overview) - Omfattande övervakningslösningar
- [AI-säkerhetsincidenthantering](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-specifika incidentprocedurer
- [SIEM för AI-system](https://learn.microsoft.com/azure/sentinel/overview) - Information och händelsehantering av säkerhet

- [Hotintelligens för AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Källor för AI-hotintelligens

## 🔄 Kontinuerlig förbättring

### Håll dig uppdaterad med utvecklande standarder
- **MCP-specifikationsuppdateringar**: Övervaka officiella ändringar i MCP-specifikationen och säkerhetsmeddelanden
- **Hotintelligens**: Prenumerera på AI-säkerhetshotflöden och sårbarhetsdatabaser  
- **Community-engagemang**: Delta i MCPs säkerhetscommunityns diskussioner och arbetsgrupper
- **Regelbunden utvärdering**: Genomför kvartalsvisa bedömningar av säkerhetsläget och uppdatera praxis därefter

### Bidra till MCP-säkerheten
- **Säkerhetsforskning**: Bidra till MCP-säkerhetsforskning och program för sårbarhetsrapportering
- **Delning av bästa praxis**: Dela säkerhetsimplementeringar och lärdomar med communityn
- **Standardutveckling**: Delta i utvecklingen av MCP-specifikationen och skapande av säkerhetsstandarder
- **Verktygsutveckling**: Utveckla och dela säkerhetsverktyg och bibliotek för MCP-ekosystemet

---

*Det här dokumentet speglar MCP:s bästa säkerhetspraxis per 9 september 2026,
baserat på MCP-specifikationen `2026-07-28`. Säkerhetspraxiser bör regelbundet
ses över i takt med protokollets och hotlandskapets utveckling.*

## Vad händer härnäst

- Läs: [MCP Safety Best Practices](./mcp-security-best-practices.md)
- Gå tillbaka till: [Översikt av säkerhetsmodul](./README.md)
- Fortsätt till: [Modul 3: Komma igång](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->