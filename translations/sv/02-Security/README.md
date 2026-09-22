# MCP Säkerhet: Omfattande Skydd för AI-System

[![MCP Säkerhet Bästa Praxis](../../../translated_images/sv/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Klicka på bilden ovan för att se video av denna lektion)_

Säkerhet är grundläggande för design av AI-system, vilket är anledningen till att vi prioriterar det som vår andra sektion. Detta ligger i linje med Microsofts **Secure by Design**-princip från [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) tillför kraftfulla nya möjligheter till AI-drivna applikationer samtidigt som det introducerar unika säkerhetsutmaningar bortom traditionella programvarurisker. MCP-system möter både etablerade säkerhetsbekymmer (säker kodning, minst privilegium, leverantörskedjesäkerhet) och nya AI-specifika hot såsom promptinjektion, verktygsförgiftning, sessionskapning, confused deputy-attacker, sårbarheter i token-omgång, och dynamisk kapacitetsmodifiering.

Denna lektion utforskar de mest kritiska säkerhetsriskerna i MCP-implementationer—täckande autentisering, auktorisering, överdrivna behörigheter, indirekt promptinjektion, sessionssäkerhet, confused deputy-problem, tokenhantering och leverantörskedjesårbarheter. Du kommer att lära dig handlingsbara kontroller och bästa praxis för att mildra dessa risker samtidigt som du utnyttjar Microsoft-lösningar som Prompt Shields, Azure Content Safety och GitHub Advanced Security för att stärka din MCP-distribution.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- **Identifiera MCP-specifika hot**: Känna igen unika säkerhetsrisker i MCP-system inklusive promptinjektion, verktygsförgiftning, överdrivna behörigheter, sessionskapning, confused deputy-problem, sårbarheter i token-omgång och leverantörskedjerisker
- **Tillämpa säkerhetskontroller**: Implementera effektiva åtgärder inklusive robust autentisering, minst privilegium-åtkomst, säker tokenhantering, sessionssäkerhetskontroller och verifiering av leverantörskedjan
- **Utnyttja Microsofts säkerhetslösningar**: Förstå och implementera Microsoft Prompt Shields, Azure Content Safety och GitHub Advanced Security för MCP-arbetsbelastningsskydd
- **Validera verktygssäkerhet**: Känna vikten av validering av verktygsmetadata, övervakning av dynamiska förändringar och försvar mot indirekta promptinjektionsattacker
- **Integrera bästa praxis**: Kombinera etablerade säkerhetsfundament (säker kodning, serverhärdning, zero trust) med MCP-specifika kontroller för omfattande skydd

# MCP Säkerhetsarkitektur & Kontroller

Moderna MCP-implementationer kräver lager-på-lager säkerhetsmetoder som adresserar både traditionell programvarusäkerhet och AI-specifika hot. Den snabbt utvecklande MCP-specifikationen fortsätter att mogna sina säkerhetskontroller, vilket möjliggör bättre integration med företags säkerhetsarkitekturer och etablerade bästa praktiker.

Forskning från [Microsoft Digital Defense Report](https://aka.ms/mddr) visar att **98% av rapporterade intrång skulle kunna förhindras med robust säkerhetshygien**. Den mest effektiva skyddsstrategin kombinerar grundläggande säkerhetspraxis med MCP-specifika kontroller—beprövade baslinjemått för säkerhet förblir de mest effektiva för att minska den totala säkerhetsrisken.

## Nuvarande säkerhetslandskap

> **Notera:** Detta kapitel kombinerar etablerade MCP-säkerhetskontroller med
> nuvarande **MCP Specification 2026-07-28** auktoriseringsvägledning. Hänvisa alltid
> till den aktuella [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHub repository](https://github.com/modelcontextprotocol), och
> [dokumentation för bästa säkerhetspraxis](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> när du implementerar säkerhetskritisk kod.

> **Auktoriseringsuppdatering:** MCP `2026-07-28` kräver att klienter validerar
> `iss`-parametern i auktoriseringssvar (RFC 9207) och binder registrerade
> autentiseringsuppgifter till den utfärdande auktoriseringsservern. Dynamisk klientregistrering
> är föråldrad; nya implementationer bör använda klient-ID metadata-dokument.
> Se [Vad som ändrats i MCP: Specifikationen 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> för fullständig lista över auktoriseringsändringar.

## 🏔️ MCP Säkerhets-Summit Workshop (Sherpa)

För **praktisk säkerhetsutbildning** rekommenderar vi starkt **MCP Security Summit Workshop** (Sherpa)—en omfattande guidad expedition för att säkra MCP-servrar i Microsoft Azure.

### Workshop-översikt

[MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) erbjuder praktisk och handlingsbar säkerhetsutbildning genom en beprövad "sårbar → exploatera → åtgärda → validera"-metodik. Du kommer att:

- **Lära dig genom att bryta saker**: Upplev sårbarheter i praktiken genom att exploatera avsiktligt osäkra servrar
- **Använda Azure-inbyggd säkerhet**: Utnyttja Azure Entra ID, Key Vault, API Management och AI Content Safety
- **Följa Defense-in-Depth**: Gå igenom läger för att bygga omfattande säkerhetslager
- **Tillämpa OWASP-standarder**: Varje teknik kopplas till [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- **Få produktionskod**: Lämna med fungerande, testade implementationer

### Expeditionsrutten

| Läger | Fokus | OWASP Risker täckta |
|------|-------|---------------------|
| **Basläger** | MCP-grunder och autentiseringssårbarheter | MCP01, MCP07 |
| **Läger 1: Identitet** | OAuth 2.1, Azure Managed Identity, Key Vault | MCP01, MCP02, MCP07 |
| **Läger 2: Gateway** | API Management, Privata Endpunkter, styrning | MCP02, MCP06, MCP07, MCP09 |
| **Läger 3: I/O Säkerhet** | Promptinjektion, PII-skydd, innehållssäkerhet | MCP03, MCP05, MCP06, MCP10 |
| **Läger 4: Övervakning** | Logganalys, instrumentpaneler, hotdetektion | MCP04, MCP08 |
| **Summiten** | Red Team / Blue Team integrationstest | Alla |

**Kom igång**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Topp 10 Säkerhetsrisker

[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) detaljerar de tio mest kritiska säkerhetsriskerna för MCP-implementationer:

| Risk | Beskrivning | Azure Åtgärd |
|------|-------------|------------------|
| **MCP01** | Felhantering av token & exponering av hemligheter | Azure Key Vault, Managed Identity |
| **MCP02** | Privilegieförhöjning via omfattningsutvidgning | RBAC, Villkorlig åtkomst |
| **MCP03** | Verktygsförgiftning | Validering av verktyg, integritetsverifiering |
| **MCP04** | Leverantörskedjeattacker & beroendetampering | GitHub Advanced Security, beroendeskanning |
| **MCP05** | Kommandoinjektion & exekvering | Inmatningsvalidering, sandboxing |
| **MCP06** | Avledning av avsiktsflöde | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Otillräcklig autentisering & auktorisering | Azure Entra ID, OAuth 2.1 med PKCE |
| **MCP08** | Brist på revision och telemetri | Azure Monitor, Application Insights |
| **MCP09** | Skymda MCP-servrar | API Center-styrning, nätverksisolering |
| **MCP10** | Kontextinjektion & överdelning | Dataklassificering, minimal exponering |

### Evolution av MCP Autentisering

MCP-specifikationen har utvecklats avsevärt vad gäller autentisering och auktorisering:

- **Ursprungligt tillvägagångssätt**: Tidiga specifikationer krävde att utvecklare implementerade egna autentiseringsservrar, där MCP-servrar fungerade som OAuth 2.0 Auktoriseringsservrar som direkt hanterade användarautentisering
- **Nuvarande standard (`2026-07-28`)**: MCP-servrar kan delegera autentisering
  till externa identitetsleverantörer såsom Microsoft Entra ID. Klienter måste även
  tillämpa aktuella krav för utfärdarvalidering och bindning av autentiseringsuppgifter.
- **Transport Layer Security**: Förbättrat stöd för säkra transportmekanismer med korrekta autentiseringsmönster för både lokala (STDIO) och fjärranslutningar (Streamable HTTP)

## Autentisering & Auktoriseringssäkerhet

### Nuvarande säkerhetsutmaningar

Moderna MCP-implementationer står inför flera autentiserings- och auktoriseringsutmaningar:

### Risker & Hotvektorer

- **Felkonfigurerad auktoriseringslogik**: Bristfällig auktoriseringsimplementering i MCP-servrar kan exponera känslig data och felaktigt tillämpa åtkomstkontroller
- **OAuth-tokenkompromettering**: Stöld av token från lokal MCP-server gör att angripare kan utge sig för att vara servrar och få åtkomst till underliggande tjänster
- **Sårbarheter vid token-omgång**: Felaktig hantering av token skapar omgåenden av säkerhetskontroller och ansvarsgap
- **Överdrivna behörigheter**: MCP-servrar med för många privilegier bryter mot principen om minst privilegium och ökar attackytorna

#### Token-omgång: Ett kritiskt antipatron

**Token-omgång är uttryckligen förbjudet** i nuvarande MCP-auktoriseringsspecifikation på grund av allvarliga säkerhetsimplikationer:

##### Omgående av säkerhetskontroller
- MCP-servrar och nedströms API:er implementerar kritiska säkerhetskontroller (hastighetsbegränsning, begäranvalidering, trafikövervakning) som är beroende av korrekt tokenvalidering
- Direkt klient-till-API-tokenanvändning kringgår dessa viktiga skydd, vilket underminerar säkerhetsarkitekturen

##### Ansvar och revisionsutmaningar  
- MCP-servrar kan inte skilja på klienter som använder upstream-utfärdade tokens, vilket bryter revisionsspår
- Loggar från nedströms resurser visar missvisande begärande ursprung istället för faktiska MCP-servermellanled
- Händelseutredning och efterlevnadsrevision blir avsevärt svårare

##### Risk för dataexfiltration
- Ovaliderade tokenpåståenden möjliggör att illasinnade aktörer med stulna tokens kan använda MCP-servrar som proxys för dataexfiltration
- Brott mot förtroendegränser tillåter obehöriga åtkomstmönster som kringgår avsedda säkerhetskontroller

##### Multi-tjänst attackvektorer
- Komprometterade tokens accepterade av flera tjänster möjliggör lateral rörelse över sammankopplade system
- Förtroendeförutsättningar mellan tjänster kan brytas när token-ursprung inte kan verifieras

### Säkerhetskontroller & Åtgärder

**Kritiska säkerhetskrav:**

> **OBLIGATORISKT**: MCP-servrar **FÅR INTE** acceptera några tokens som inte uttryckligen utfärdats för MCP-servern

#### Autentiserings- och auktoriseringskontroller

- **Noggrann auktoriseringsgranskning**: Genomför omfattande revisioner av MCP-serverns auktoriseringslogik för att säkerställa att endast avsedda användare och klienter kan få åtkomst till känsliga resurser
  - **Implementeringsguide**: [Azure API Management som autentiseringsgateway för MCP-servrar](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identitetsintegration**: [Använda Microsoft Entra ID för MCP-serverautentisering](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Säker tokenhantering**: Implementera [Microsofts tokenvalidering och livscykel-bästa praxis](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validera att token-målgruppspåståenden matchar MCP-serverns identitet
  - Implementera korrekta policys för tokenrotation och utgångsdatum
  - Förhindra replay-attacker och obehörig användning av token

- **Skyddad tokenlagring**: Säkerställ lagring av tokens med kryptering både i vila och under överföring
  - **Bästa praxis**: [Riktlinjer för säker tokenlagring och kryptering](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementation av åtkomstkontroll

- **Principen om minst privilegium**: Ge MCP-servrar endast de minimala behörigheter som krävs för avsedd funktionalitet
  - Regelbunden granskning och uppdatering av behörigheter för att förhindra privilegiekrypning
  - **Microsoft-dokumentation**: [Säkra minst-behörighetsåtkomst](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rollbaserad åtkomstkontroll (RBAC)**: Implementera finmaskiga rolltilldelningar
  - Begränsa roller noga till specifika resurser och åtgärder
  - Undvik breda eller onödiga behörigheter som utökar attackytor

- **Kontinuerlig behörighetsövervakning**: Implementera kontinuerlig åtkomstrevision och övervakning
  - Övervaka användningsmönster av behörigheter för avvikelser
  - Åtgärda snabbt överflödiga eller oanvända privilegier

## AI-Specifika säkerhetshot

### Promptinjektion och verktygsmanipulationsattacker

Moderna MCP-implementationer står inför sofistikerade AI-specifika attackvektorer som traditionella säkerhetsåtgärder inte fullt ut kan hantera:

#### **Indirekt promptinjektion (Cross-Domain Prompt Injection)**

**Indirekt promptinjektion** är en av de mest kritiska sårbarheterna i MCP-aktiverade AI-system. Angripare bäddar in illvilliga instruktioner i externt innehåll—dokument, webbsidor, e-post eller datakällor—som AI-system sedan behandlar som legitima kommandon.

**Attackscenarier:**
- **Dokumentbaserad injektion**: Illvilliga instruktioner gömda i bearbetade dokument som triggar oavsiktliga AI-åtgärder
- **Webbinnehållsexploatering**: Komprometterade webbsidor med inbäddade prompts som manipulerar AI-beteende vid dataskrapning
- **E-postbaserade attacker**: Illvilliga prompts i e-post som får AI-assistenter att läcka information eller utföra obehöriga handlingar
- **Kontaminering av datakällor**: Komprometterade databaser eller API:er som levererar förorenat innehåll till AI-system

**Påverkan i verkligheten**: Dessa attacker kan resultera i dataexfiltration, integritetsbrott, generering av skadligt innehåll och manipulation av användarinteraktioner. För detaljerad analys, se [Prompt Injection i MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/sv/prompt-injection.ed9fbfde297ca877.webp)

#### **Verktygsförgiftningsattacker**

**Verktygsförgiftning** är riktad mot metadatan som definierar MCP-verktyg och utnyttjar hur LLM:er tolkar verktygsbeskrivningar och parametrar för att fatta exekveringsbeslut.

**Attackmekanismer:**
- **Metadata-manipulation**: Angripare injicerar skadliga instruktioner i verktygsbeskrivningar, parameterdefinitioner eller användningsexempel
- **Osynliga instruktioner**: Gömda prompts i verktygsmetadata som behandlas av AI-modeller men är osynliga för mänskliga användare
- **Dynamisk verktygsmodifiering ("Rug Pulls")**: Verktyg godkända av användare ändras senare för att utföra skadliga handlingar utan användarens vetskap
- **Paramterinjektion**: Skadligt innehåll inbäddat i verktygsparameterscheman som påverkar modellbeteende


**Risker med värdserver**: Fjärropererade MCP-servrar innebär förhöjda risker då verktygsdefinitioner kan uppdateras efter användarens initiala godkännande, vilket skapar scenarier där verktyg som tidigare var säkra blir skadliga. För en omfattande analys, se [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/sv/tool-injection.3b0b4a6b24de6bef.webp)

#### **Ytterligare AI-attacksvektorer**

- **Cross-Domain Prompt Injection (XPIA)**: Sofistikerade attacker som använder innehåll från flera domäner för att kringgå säkerhetskontroller
- **Dynamisk kapacitetsmodifiering**: Realtidsändringar av verktygsfunktioner som undgår initiala säkerhetsbedömningar
- **Context Window Poisoning**: Attacker som manipulerar stora kontextfönster för att dölja skadliga instruktioner
- **Modellförvirringsattacker**: Utnyttjande av modellbegränsningar för att skapa oförutsägbara eller osäkra beteenden


### AI-säkerhetsriskers påverkan

**Konsekvenser med hög påverkan:**
- **Dataexfiltrering**: Obehörig åtkomst och stöld av känslig företags- eller personlig data
- **Integritetsbrott**: Exponering av personliga identifierbara uppgifter (PII) och konfidentiell affärsdata  
- **Systemmanipulation**: Oavsiktliga ändringar i kritiska system och arbetsflöden
- **Stöld av autentiseringsuppgifter**: Kompromettering av autentiseringstoken och tjänsteuppgifter
- **Laterala rörelser**: Användning av komprometterade AI-system som språngbrädor för bredare nätverksattacker

### Microsofts AI-säkerhetslösningar

#### **AI Prompt Shields: Avancerat skydd mot injektionsattacker**

Microsofts **AI Prompt Shields** ger heltäckande försvar mot både direkta och indirekta promptinjektionsattacker genom flera säkerhetslager:

##### **Kärnskyddsmekanismer:**

1. **Avancerad upptäckt och filtrering**
   - Maskininlärningsalgoritmer och NLP-tekniker som identifierar skadliga instruktioner i externt innehåll
   - Realtidsanalys av dokument, webbsidor, e-post och datakällor för inbäddade hot
   - Kontextuell förståelse av legitima vs. skadliga promptmönster

2. **Spotlighting-tekniker**  
   - Skillnad mellan betrodda systeminstruktioner och potentiellt komprometterad extern input
   - Textomvandlingsmetoder som förbättrar modellens relevans samtidigt som skadligt innehåll isoleras
   - Hjälper AI-system att bibehålla rätt instruktionshierarki och ignorera injicerade kommandon

3. **Avgränsare och datamarkeringssystem**
   - Tydlig gränsdragning mellan betrodda systemmeddelanden och extern inmatningstext
   - Specialmarkörer som framhäver gränser mellan betrodda och obetrodda datakällor
   - Klar separation förhindrar förvirring i instruktioner och obehörig körning av kommandon

4. **Kontinuerlig hotintelligens**
   - Microsoft övervakar ständigt nya attackmönster och uppdaterar försvar
   - Proaktiv hotjakt efter nya injektionstekniker och attackvektorer
   - Regelbundna uppdateringar av säkerhetsmodeller för att behålla effektivitet mot utvecklade hot

5. **Integration med Azure Content Safety**
   - Del av den omfattande sviten Azure AI Content Safety
   - Ytterligare upptäckt av jailbreak-försök, skadligt innehåll och brott mot säkerhetspolicyer
   - Enhetliga säkerhetskontroller över AI-applikationskomponenter

**Implementeringsresurser**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/sv/prompt-shield.ff5b95be76e9c78c.webp)


## Avancerade MCP-säkerhetshot

### Sårbarheter för sessionkapning

**Sessionkapning** utgör en kritisk attackvektor i stateful MCP-implementationer där obehöriga parter får tag på och missbrukar legitima sessionsidentifierare för att utge sig för att vara klienter och utföra obehöriga handlingar.

#### **Attackscenarier och risker**

- **Sessionkapningspromptinjektion**: Angripare med stulna sessions-ID injicerar skadliga händelser i servrar som delar sessionsstatus, vilket potentiellt triggar skadliga handlingar eller ger tillgång till känsliga data
- **Direkt imitation**: Stulna sessions-ID möjliggör direkta MCP-serveranrop som kringgår autentisering och behandlar angripare som legitima användare
- **Komprometterade återupptagningsbara strömmar**: Angripare kan avbryta förfrågningar i förtid, vilket orsakar att legitima klienter återupptar med potentiellt skadligt innehåll

#### **Säkerhetskontroller för sessionshantering**

**Kritiska krav:**
- **Verifikation av auktorisation**: MCP-servrar som implementerar auktorisation **MÅSTE** verifiera ALLA inkommande förfrågningar och **FÅR INTE** förlita sig på sessioner för autentisering
- **Säker sessionsgenerering**: Använd kryptografiskt säkra, icke-deterministiska sessions-ID genererade med säkra slumpgeneratorer
- **Användarspecifik bindning**: Binda sessions-ID till användarspecifik information med format som `<user_id>:<session_id>` för att förhindra missbruk mellan användare
- **Hantering av sessionslivscykel**: Implementera korrekt utgång, rotation och ogiltigförklaring för att begränsa sårbarhetsfönster
- **Transportssäkerhet**: Obligatorisk HTTPS för all kommunikation för att förhindra avlyssning av sessions-ID

### Confused Deputy-problemet

**Confused deputy-problemet** uppstår när MCP-servrar agerar autentiseringsproxyer mellan klienter och tredjepartstjänster, vilket skapar möjligheter för kringgående av auktorisation genom exploatering av statiska klient-ID:n.

#### **Attackmekanismer och risker**

- **Cookie-baserad samtyckesomgång**: Tidigare användarautentisering skapar samtyckeskakor som angripare utnyttjar genom skadliga auktorisationsförfrågningar med förfalskade redirect-URI:er
- **Stöld av auktorisationskod**: Befintliga samtyckeskakor kan få auktorisationsservrar att hoppa över samtyckesskärmar och dirigera koder till angriparkontrollerade ändpunkter  
- **Obehörig API-åtkomst**: Stulna auktorisationskoder möjliggör tokenutbyte och användarförfalskning utan uttryckligt godkännande

#### **Motstrategier**

**Obligatoriska kontroller:**
- **Explicit samtyckeskrav**: MCP-proxyservrar som använder statiska klient-ID:n **MÅSTE** inhämta användarens samtycke för varje dynamiskt registrerad klient
- **OAuth 2.1 säkerhetsimplementering**: Följ aktuella bästa praxis för OAuth-säkerhet inklusive PKCE (Proof Key for Code Exchange) för alla auktorisationsförfrågningar
- **Strikt klientvalidering**: Implementera rigorös validering av redirect-URI och klientidentifierare för att förhindra exploatering

### Token Passthrough-sårbarheter  

**Token passthrough** är ett explicit anti-mönster där MCP-servrar accepterar klienttoken utan korrekt validering och vidarebefordrar dem till nedströms-API:er, vilket strider mot MCP:s auktorisationsspecifikationer.

#### **Säkerhetskonsekvenser**

- **Kringgående av kontroll**: Direkt klient-till-API-tokenanvändning kringgår viktiga hastighetsbegränsningar, valideringar och övervakningskontroller
- **Förstörd revisionskedja**: Token utfärdade uppströms gör klientidentifiering omöjlig och bryter utredningsmöjligheter vid incidenter
- **Proxy-baserad dataexfiltrering**: Ovaliderade token gör det möjligt för skadliga aktörer att använda servrar som proxyer för obehörig dataåtkomst
- **Brott mot förtroendegränser**: Nedströms-tjänsters förtroendeantaganden kan brytas när tokenursprung inte kan verifieras
- **Expansion av multi-service-attacker**: Komprometterade token som accepteras i flera tjänster möjliggör laterala rörelser

#### **Nödvändiga säkerhetskontroller**

**Icke-förhandlingsbara krav:**
- **Tokenvalidering**: MCP-servrar **FÅR INTE** acceptera token som inte uttryckligen är utfärdade för MCP-servern
- **Verifiering av publik**: Validera alltid att token-publiken matchar MCP-serverns identitet
- **Korrekt tokenlivscykel**: Implementera kortlivade access-tokens med säkra rotationsmetoder


## Säkerhet i leveranskedjan för AI-system

Säkerhet i leveranskedjan har utvecklats bortom traditionella mjukvaruberoenden och omfattar hela AI-ekosystemet. Moderna MCP-implementationer måste noggrant verifiera och övervaka alla AI-relaterade komponenter, eftersom varje introducerar potentiella sårbarheter som kan kompromettera systemets integritet.

### Utökade komponenter i AI-leveranskedjan

**Traditionella mjukvaruberoenden:**
- Öppen källkod-bibliotek och ramverk
- Container-bilder och basystem  
- Utvecklingsverktyg och byggpipelines
- Infrastrukturkomponenter och tjänster

**AI-specifika leveranskedjeelement:**
- **Grundmodeller**: Förtränade modeller från olika leverantörer som kräver ursprungsverifiering
- **Embedding-tjänster**: Externa vektorisering- och semantiska söktjänster
- **Context Providers**: Datakällor, kunskapsdatabaser och dokumentarkiv  
- **Tredjeparts-API:er**: Externa AI-tjänster, ML-pipelines och dataprosesseringsendpunkter
- **Modellartefakter**: Vikter, konfigurationer och fintjusterade modellvarianter
- **Träningsdatakällor**: Datasätt som används för modellträning och finjustering

### Omfattande strategi för säkerhet i leveranskedjan

#### **Verifikation och förtroende för komponenter**
- **Ursprungsvalidering**: Verifiera ursprung, licensiering och integritet för alla AI-komponenter innan integration
- **Säkerhetsbedömning**: Utför sårbarhetsscanning och säkerhetsgranskningar för modeller, datakällor och AI-tjänster
- **Rykteanalys**: Utvärdera säkerhetshistorik och praxis hos AI-tjänsteleverantörer
- **Efterlevnadsverifiering**: Säkerställ att alla komponenter uppfyller organisatoriska säkerhets- och regulatoriska krav

#### **Säkra deployeringspipelines**  
- **Automatisk CI/CD-säkerhet**: Integrera säkerhetsscanning i automatiserade deployeringspipelines
- **Artefaktintegritet**: Implementera kryptografisk verifiering för alla deployerade artefakter (kod, modeller, konfigurationer)
- **Etappvis deployering**: Använd progressiva deployeringsstrategier med säkerhetsverifiering i varje steg
- **Betrodda artefaktregister**: Deployera endast från verifierade, säkra artefaktregister och arkiv

#### **Kontinuerlig övervakning och respons**
- **Beroendesökning**: Pågående sårbarhetsövervakning för alla mjukvaru- och AI-komponentberoenden
- **Modellövervakning**: Kontinuerlig bedömning av modellbeteende, prestationsglidning och säkerhetsavvikelser
- **Tjänstehälsokontroll**: Övervaka externa AI-tjänster för tillgänglighet, säkerhetsincidenter och policyförändringar
- **Integrering av hotintelligens**: Inkorporera hotflöden specifika för AI- och ML-säkerhetsrisker

#### **Behörighetskontroll och minst privilegium**
- **Komponentnivåbehörigheter**: Begränsa åtkomst till modeller, data och tjänster baserat på affärsbehov
- **Hantera tjänstekonton**: Implementera dedikerade tjänstekonton med minimala nödvändiga behörigheter
- **Nätverkssegmentering**: Isolera AI-komponenter och begränsa nätverksåtkomst mellan tjänster
- **API-gateway-kontroller**: Använd centraliserade API-gateways för att kontrollera och övervaka åtkomst till externa AI-tjänster

#### **Incidenthantering och återställning**
- **Snabba responsprocedurer**: Etablerade processer för patchning eller ersättning av komprometterade AI-komponenter
- **Rotation av autentiseringsuppgifter**: Automatiserade system för rotation av hemligheter, API-nycklar och tjänsteuppgifter
- **Återställningsmöjligheter**: Möjlighet att snabbt återgå till tidigare fungerande versioner av AI-komponenter
- **Återhämtning vid leveranskedjebrott**: Specifika procedurer för respons vid komprometteringar i uppströms AI-tjänster

### Microsofts säkerhetsverktyg och integration

**GitHub Advanced Security** tillhandahåller heltäckande skydd för leveranskedjan inklusive:
- **Secretscanning**: Automatisk upptäckt av autentiseringsuppgifter, API-nycklar och tokens i repositorier
- **Beroendesökning**: Sårbarhetsbedömning för öppen källkod-beroenden och bibliotek
- **CodeQL-analys**: Statisk kodanalys för säkerhetsbrister och kodningsproblem
- **Insikter om leveranskedjan**: Synlighet i beroendehälsa och säkerhetsstatus

**Integration med Azure DevOps & Azure Repos:**
- Sömlös integration av säkerhetsscanning över Microsofts utvecklingsplattformar
- Automatiska säkerhetskontroller i Azure Pipelines för AI-arbetsbelastningar
- Policys för säker implementering av AI-komponenter

**Microsofts interna praxis:**
Microsoft implementerar omfattande säkerhetspraxis i leveranskedjan över alla produkter. Läs om beprövade metoder i [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Grundläggande säkerhetspraxis

MCP-implementationer ärver och bygger vidare på din organisations befintliga säkerhetsställning. Att stärka grundläggande säkerhetspraxis förbättrar avsevärt helhetssäkerheten för AI-system och MCP-implementationer.

### Kärnfundament för säkerhet

#### **Säkra utvecklingspraxis**
- **OWASP-överensstämmelse**: Skydda mot [OWASP Top 10](https://owasp.org/www-project-top-ten/) säkra webbapplikationssårbarheter
- **AI-specifika skydd**: Implementera kontroller för [OWASP Top 10 för LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Säker hantering av hemligheter**: Använd dedikerade valv för tokens, API-nycklar och känslig konfigurationsdata
- **End-to-end-kryptering**: Implementera säkra kommunikationer över alla applikationskomponenter och dataflöden
- **Inmatningsvalidering**: Noggrann validering av all användarinmatning, API-parametrar och datakällor

#### **Förstärkning av infrastruktur**
- **Multifaktorsautentisering**: Obligatorisk MFA för alla administrativa och tjänstekonton
- **Patchhantering**: Automatiserad och snabb patchning för operativsystem, ramverk och beroenden  
- **Integration med identitetsleverantörer**: Centraliserad identitetshantering genom företagsidentitetsleverantörer (Microsoft Entra ID, Active Directory)
- **Nätverkssegmentering**: Logisk isolering av MCP-komponenter för att begränsa möjligheter till laterala rörelser
- **Principen om minsta privilegium**: Minimala nödvändiga behörigheter för alla systemkomponenter och konton

#### **Säkerhetsövervakning och upptäckt**
- **Omfattande loggning**: Detaljerad loggning av AI-applikationsaktiviteter, inklusive interaktioner mellan MCP-klient och server
- **SIEM-integration**: Centraliserad säkerhetsinformations- och händelsehantering för avvikelsedetektering
- **Beteendeanalys**: AI-drivna övervakningar för att upptäcka ovanliga mönster i system- och användarbeteenden
- **Hotintelligens**: Integrering av externa hotflöden och kompromissindikatorer (IOCs)
- **Incidentrespons**: Väldefinierade rutiner för upptäckt, respons och återställning vid säkerhetsincidenter

#### **Zero Trust-arkitektur**
- **Lita aldrig, verifiera alltid**: Kontinuerlig verifiering av användare, enheter och nätverkskopplingar
- **Mikrosegmentering**: Detaljerade nätverkskontroller som isolerar individuella arbetsbelastningar och tjänster
- **Identitetscentrerad säkerhet**: Säkerhetspolicys baserade på verifierade identiteter snarare än nätverksplats
- **Kontinuerlig riskbedömning**: Dynamisk säkerhetsställningsutvärdering baserat på aktuell kontext och beteende
- **Villkorad åtkomst**: Åtkomstkontroller som anpassas baserat på riskfaktorer, plats och enhetens tillit

### Integrationsmönster för företag

#### **Integration i Microsofts säkerhetsekosystem**
- **Microsoft Defender for Cloud**: Omfattande hantering av säkerhetsställning för moln
- **Azure Sentinel**: Molnbaserade SIEM- och SOAR-funktioner för skydd av AI-arbetsbelastningar
- **Microsoft Entra ID**: Företagsidentitet och åtkomsthantering med villkorade åtkomstpolicyer
- **Azure Key Vault**: Centraliserad hantering av hemligheter med hårdvarusäkerhetsmodul (HSM)
- **Microsoft Purview**: Datastyrning och efterlevnad för AI-datakällor och arbetsflöden

#### **Efterlevnad och styrning**
- **Regulatorisk anpassning**: Säkerställ att MCP-implementationer uppfyller branschspecifika efterlevnadskrav (GDPR, HIPAA, SOC 2)

- **Dataklassificering**: Korrekt kategorisering och hantering av känslig data som bearbetas av AI-system
- **Revisionsspår**: Omfattande loggning för regleringsuppfyllelse och rättsmedicinsk utredning
- **Integritetskontroller**: Implementering av integritet-som-standard-principer i AI-systemarkitektur
- **Ändringshantering**: Formella processer för säkerhetsgranskning av ändringar i AI-system

Dessa grundläggande metoder skapar en robust säkerhetsbas som förbättrar effektiviteten av MCP-specifika säkerhetskontroller och ger omfattande skydd för AI-drivna applikationer.

## Viktiga säkerhetsinsikter

- **Flerlagers säkerhetsstrategi**: Kombinera grundläggande säkerhetspraxis (säker kodning, minsta privilegium, leveranskedjeverifiering, kontinuerlig övervakning) med AI-specifika kontroller för komplett skydd

- **AI-specifika hotlandskapet**: MCP-system står inför unika risker inklusive promptinjicering, verktygsförgiftning, sessionskapning, förvirrad mellanhand-problem, token-passthrough-sårbarheter och överdrivna rättigheter som kräver specialiserade motåtgärder

- **Excellens i autentisering & auktorisering**: Implementera robust autentisering med externa identitetsleverantörer (Microsoft Entra ID), tillämpa korrekt tokenvalidering och acceptera aldrig tokens som inte uttryckligen har utfärdats för din MCP-server

- **Förebyggande av AI-attacker**: Använd Microsoft Prompt Shields och Azure Content Safety för att skydda mot indirekta promptinjicerings- och verktygsförgiftningattacker, samtidigt som verktygsmetadata valideras och dynamiska förändringar övervakas

- **Sessions- och transportsekretess**: Använd kryptografiskt säkra, icke-deterministiska sessions-ID:n bundna till användaridentiteter, implementera korrekt hantering av sessionslivscykel och använd aldrig sessioner för autentisering

- **OAuth-säkerhetsbästa praxis**: Förhindra förvirrad mellanhand-attacker genom uttryckligt användarsamtycke för dynamiskt registrerade klienter, korrekt OAuth 2.1-implementering med PKCE och strikt validering av redirect URI  

- **Token-säkerhetsprinciper**: Undvik token-passthrough-anti-mönster, validera token-målgrupps-påståenden, implementera kortlivade tokens med säker rotation, och upprätthåll tydliga förtroendegränser

- **Omfattande leveranskedjesäkerhet**: Behandla alla AI-ekosystemets komponenter (modeller, inbäddningar, kontextleverantörer, externa API:er) med samma säkerhetssaklighet som traditionella mjukvaruberoenden

- **Kontinuerlig utveckling**: Håll dig uppdaterad med snabbt utvecklande MCP-specifikationer, bidra till säkerhetsgemenskapens standarder och bibehåll adaptiva säkerhetsposturer när protokollet mognar

- **Microsofts säkerhetsintegration**: Använd Microsofts omfattande säkerhetsekosystem (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) för förbättrat skydd vid MCP-distribution

## Omfattande resurser

### **Officiell MCP-säkerhetsdokumentation**
- [MCP-specifikation (Aktuell: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Säkerhetsbästa Praxis](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Auktorisationsspecifikation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

### **OWASP MCP Säkerhetsresurser**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Omfattande OWASP MCP Topp 10 med Azure-implementeringsvägledning
- [OWASP MCP Topp 10](https://owasp.org/www-project-mcp-top-10/) - Officiella OWASP MCP-säkerhetsrisker
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktisk säkerhetsträning för MCP på Azure

### **Säkerhetsstandarder & bästa praxis**
- [OAuth 2.0 Säkerhetsbästa Praxis (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Topp 10 Webbsäkerhet](https://owasp.org/www-project-top-ten/)
- [OWASP Topp 10 för Stora Språkmodeller](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **AI Säkerhetsforskning & Analys**
- [Promptinjicering i MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Verktygsförgiftningattacker (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Säkerhetsforskningsgenomgång (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsofts säkerhetslösningar**
- [Microsoft Prompt Shields Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Säkerhet](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Tokenhantering Bästa Praxis](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Implementeringsguider & Tutorials**
- [Azure API Management som MCP Autentiseringsgateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Autentisering med MCP-servrar](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Säker tokenlagring och kryptering (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & leveranskedjesäkerhet**
- [Azure DevOps Säkerhet](https://azure.microsoft.com/products/devops)
- [Azure Repos Säkerhet](https://azure.microsoft.com/products/devops/repos/)
- [Microsofts Leveranskedjesäkerhetsresa](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Ytterligare säkerhetsdokumentation**

För omfattande säkerhetsanvisningar, se dessa specialiserade dokument i detta avsnitt:

- **[CIMD och DCR Auktorisationsprov](./samples/cimd-dcr-auth/README.md)** - Körbar TypeScript MCP `2026-07-28` resursserver som jämför föredragna Client ID Metadata-dokument med föråldrat Dynamic Client Registration-fallbak
- **[MCP Säkerhetsbästa Praxis](./mcp-security-best-practices.md)** - Komplett bästa praxis för säkerhet vid MCP-implementeringar
- **[Azure Content Safety Implementering](./azure-content-safety-implementation.md)** - Praktiska implementeringsexempel för integration av Azure Content Safety  
- **[MCP Säkerhetskontroller](./mcp-security-controls.md)** - Senaste säkerhetskontroller och tekniker för MCP-distributioner
- **[MCP Bästa Praxis Snabbreferens](./mcp-best-practices.md)** - Snabbreferensguide för viktiga MCP-säkerhetspraxis
- **[BlueHat 2026: Säkerställa AI:s framtid: Säkerställa MCP med djupförsvarsmönster](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Djupförsvarsmönster från Microsoft Security Response Center (MSRC)

### **Praktisk säkerhetsträning**

- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Omfattande praktisk workshop för att säkra MCP-servrar i Azure med progressiva läger från Base Camp till Summit
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Referensarkitektur och implementeringsvägledning för alla OWASP MCP Topp 10 risker

---

## Vad är nästa steg

Nästa: [Kapitel 3: Komma igång](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->