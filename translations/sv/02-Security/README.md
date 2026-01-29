# MCP Security: Omfattande skydd för AI-system

[![MCP Security Best Practices](../../../translated_images/sv/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Klicka på bilden ovan för att se videon för denna lektion)_

Säkerhet är grundläggande för design av AI-system, vilket är anledningen till att vi prioriterar det som vår andra sektion. Detta överensstämmer med Microsofts princip **Secure by Design** från [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) tillför kraftfulla nya möjligheter till AI-drivna applikationer samtidigt som det introducerar unika säkerhetsutmaningar som sträcker sig bortom traditionella mjukvarurisker. MCP-system står inför både etablerade säkerhetsproblem (säker kodning, minsta privilegium, leverantörskedjesäkerhet) och nya AI-specifika hot inklusive promptinjektion, verktygsförgiftning, sessionkapning, confused deputy-attacker, token-passthrough-sårbarheter och dynamisk kapacitetsmodifiering.

Denna lektion utforskar de mest kritiska säkerhetsriskerna i MCP-implementationer—med fokus på autentisering, auktorisering, överdrivna behörigheter, indirekt promptinjektion, sessionssäkerhet, confused deputy-problem, tokenhantering och leverantörskedjesårbarheter. Du kommer att lära dig handlingsbara kontroller och bästa praxis för att mildra dessa risker samtidigt som du utnyttjar Microsoft-lösningar som Prompt Shields, Azure Content Safety och GitHub Advanced Security för att stärka din MCP-distribution.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- **Identifiera MCP-specifika hot**: Känna igen unika säkerhetsrisker i MCP-system inklusive promptinjektion, verktygsförgiftning, överdrivna behörigheter, sessionkapning, confused deputy-problem, token-passthrough-sårbarheter och leverantörskedjerisker
- **Tillämpa säkerhetskontroller**: Implementera effektiva mildrande åtgärder inklusive robust autentisering, minsta privilegium-åtkomst, säker tokenhantering, sessionssäkerhetskontroller och verifiering av leverantörskedjan
- **Utnyttja Microsofts säkerhetslösningar**: Förstå och distribuera Microsoft Prompt Shields, Azure Content Safety och GitHub Advanced Security för skydd av MCP-arbetsbelastningar
- **Validera verktygssäkerhet**: Känna igen vikten av validering av verktygsmetadata, övervakning av dynamiska förändringar och försvar mot indirekta promptinjektionsattacker
- **Integrera bästa praxis**: Kombinera etablerade säkerhetsgrunder (säker kodning, serverhärdning, zero trust) med MCP-specifika kontroller för omfattande skydd

# MCP Security Architecture & Controls

Moderna MCP-implementationer kräver lager av säkerhetsmetoder som adresserar både traditionell mjukvarusäkerhet och AI-specifika hot. Den snabbt utvecklande MCP-specifikationen fortsätter att mogna sina säkerhetskontroller, vilket möjliggör bättre integration med företags säkerhetsarkitekturer och etablerade bästa praxis.

Forskning från [Microsoft Digital Defense Report](https://aka.ms/mddr) visar att **98 % av rapporterade intrång skulle förhindras av robust säkerhetshygien**. Den mest effektiva skyddsstrategin kombinerar grundläggande säkerhetspraxis med MCP-specifika kontroller—beprövade baslinjemått för säkerhet förblir mest effektiva för att minska den totala säkerhetsrisken.

## Nuvarande säkerhetslandskap

> **Notera:** Denna information speglar MCP-säkerhetsstandarder per **18 december 2025**. MCP-protokollet fortsätter att utvecklas snabbt, och framtida implementationer kan introducera nya autentiseringsmönster och förbättrade kontroller. Hänvisa alltid till aktuell [MCP Specification](https://spec.modelcontextprotocol.io/), [MCP GitHub repository](https://github.com/modelcontextprotocol) och [säkerhetsbästa praxis-dokumentation](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) för senaste vägledning.

### Utveckling av MCP-autentisering

MCP-specifikationen har utvecklats avsevärt i sin metod för autentisering och auktorisering:

- **Ursprungligt tillvägagångssätt**: Tidiga specifikationer krävde att utvecklare implementerade egna autentiseringsservrar, där MCP-servrar agerade som OAuth 2.0-auktoriseringsservrar som hanterade användarautentisering direkt
- **Nuvarande standard (2025-11-25)**: Uppdaterad specifikation tillåter MCP-servrar att delegera autentisering till externa identitetsleverantörer (såsom Microsoft Entra ID), vilket förbättrar säkerhetsläget och minskar implementeringskomplexiteten
- **Transport Layer Security**: Förbättrat stöd för säkra transportmekanismer med korrekta autentiseringsmönster för både lokala (STDIO) och fjärranslutna (Streamable HTTP) anslutningar

## Autentisering & auktoriseringssäkerhet

### Nuvarande säkerhetsutmaningar

Moderna MCP-implementationer står inför flera autentiserings- och auktoriseringsutmaningar:

### Risker & hotvektorer

- **Felkonfigurerad auktoriseringslogik**: Bristfällig auktoriseringsimplementering i MCP-servrar kan exponera känslig data och felaktigt tillämpa åtkomstkontroller
- **OAuth-tokenkompromiss**: Stöld av lokala MCP-servertokens möjliggör för angripare att utge sig för servrar och få tillgång till nedströms tjänster
- **Token-passthrough-sårbarheter**: Felaktig tokenhantering skapar säkerhetskontrollbypassar och ansvarsgap
- **Överdrivna behörigheter**: MCP-servrar med för stora privilegier bryter mot principen om minsta privilegium och utvidgar attackytor

#### Token Passthrough: Ett kritiskt anti-mönster

**Token passthrough är uttryckligen förbjudet** i den nuvarande MCP-auktoriseringsspecifikationen på grund av allvarliga säkerhetskonsekvenser:

##### Omgåelse av säkerhetskontroller
- MCP-servrar och nedströms API:er implementerar kritiska säkerhetskontroller (hastighetsbegränsning, förfrågningsvalidering, trafikövervakning) som är beroende av korrekt tokenvalidering
- Direkt klient-till-API-tokenanvändning kringgår dessa viktiga skydd och undergräver säkerhetsarkitekturen

##### Ansvars- och revisionsutmaningar  
- MCP-servrar kan inte skilja mellan klienter som använder tokens utfärdade uppströms, vilket bryter revisionskedjor
- Loggar från nedströms resursservrar visar missvisande förfrågningskällor istället för faktiska MCP-servermellanled
- Incidentutredning och efterlevnadsrevision blir avsevärt svårare

##### Risker för dataexfiltrering
- Ovaliderade tokenpåståenden möjliggör för illvilliga aktörer med stulna tokens att använda MCP-servrar som proxys för dataexfiltrering
- Brott mot förtroendegränser tillåter obehöriga åtkomstmönster som kringgår avsedda säkerhetskontroller

##### Multi-tjänst attackvektorer
- Komprometterade tokens som accepteras av flera tjänster möjliggör lateral rörelse över anslutna system
- Förtroendeantaganden mellan tjänster kan brytas när tokenursprung inte kan verifieras

### Säkerhetskontroller & mildrande åtgärder

**Kritiska säkerhetskrav:**

> **OBLIGATORISKT**: MCP-servrar **FÅR INTE** acceptera några tokens som inte uttryckligen utfärdats för MCP-servern

#### Autentiserings- och auktoriseringskontroller

- **Noggrann auktoriseringsgranskning**: Genomför omfattande revisioner av MCP-serverns auktoriseringslogik för att säkerställa att endast avsedda användare och klienter kan nå känsliga resurser
  - **Implementeringsguide**: [Azure API Management som autentiseringsgateway för MCP-servrar](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identitetsintegration**: [Använda Microsoft Entra ID för MCP-serverautentisering](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Säker tokenhantering**: Implementera [Microsofts bästa praxis för tokenvalidering och livscykel](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validera att tokenpublikums påståenden matchar MCP-serverns identitet
  - Implementera korrekt tokenrotation och utgångspolicys
  - Förhindra tokenåterspelning och obehörig användning

- **Skyddad tokenlagring**: Säker tokenlagring med kryptering både i vila och under överföring
  - **Bästa praxis**: [Riktlinjer för säker tokenlagring och kryptering](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementering av åtkomstkontroll

- **Principen om minsta privilegium**: Ge MCP-servrar endast minimala behörigheter som krävs för avsedd funktionalitet
  - Regelbundna behörighetsgranskningar och uppdateringar för att förhindra privilegieutvidgning
  - **Microsoft-dokumentation**: [Säker minsta privilegierad åtkomst](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rollbaserad åtkomstkontroll (RBAC)**: Implementera finmaskiga rolltilldelningar
  - Begränsa roller strikt till specifika resurser och åtgärder
  - Undvik breda eller onödiga behörigheter som utvidgar attackytor

- **Kontinuerlig behörighetsövervakning**: Implementera löpande åtkomstrevision och övervakning
  - Övervaka behörighetsanvändningsmönster för avvikelser
  - Åtgärda snabbt överdrivna eller oanvända privilegier

## AI-specifika säkerhetshot

### Promptinjektion & verktygsmanipulationsattacker

Moderna MCP-implementationer står inför sofistikerade AI-specifika attackvektorer som traditionella säkerhetsåtgärder inte fullt ut kan hantera:

#### **Indirekt promptinjektion (Cross-Domain Prompt Injection)**

**Indirekt promptinjektion** utgör en av de mest kritiska sårbarheterna i MCP-aktiverade AI-system. Angripare bäddar in skadliga instruktioner i externt innehåll—dokument, webbsidor, e-post eller datakällor—som AI-system sedan behandlar som legitima kommandon.

**Attackscenarier:**
- **Dokumentbaserad injektion**: Skadliga instruktioner gömda i bearbetade dokument som triggar oavsiktliga AI-åtgärder
- **Webbinnehållsexploatering**: Komprometterade webbsidor med inbäddade prompts som manipulerar AI-beteende vid skrapning
- **E-postbaserade attacker**: Skadliga prompts i e-post som får AI-assistenter att läcka information eller utföra obehöriga åtgärder
- **Datakällkontaminering**: Komprometterade databaser eller API:er som levererar förorenat innehåll till AI-system

**Verklig påverkan**: Dessa attacker kan leda till dataexfiltrering, integritetsbrott, generering av skadligt innehåll och manipulation av användarinteraktioner. För detaljerad analys, se [Prompt Injection i MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/sv/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Verktygsförgiftningsattacker**

**Verktygsförgiftning** riktar sig mot metadata som definierar MCP-verktyg, och utnyttjar hur LLM:er tolkar verktygsbeskrivningar och parametrar för att fatta exekveringsbeslut.

**Attackmekanismer:**
- **Metadatatill manipulation**: Angripare injicerar skadliga instruktioner i verktygsbeskrivningar, parameterdefinitioner eller användningsexempel
- **Osynliga instruktioner**: Dolda prompts i verktygsmetadata som bearbetas av AI-modeller men är osynliga för mänskliga användare
- **Dynamisk verktygsmodifiering ("Rug Pulls")**: Verktyg som godkänts av användare modifieras senare för att utföra skadliga åtgärder utan användarens vetskap
- **Parameterinjektion**: Skadligt innehåll inbäddat i verktygsparameterscheman som påverkar modellbeteende

**Risker med hostade servrar**: Fjärr-MCP-servrar innebär förhöjda risker eftersom verktygsdefinitioner kan uppdateras efter initial användargodkännande, vilket skapar scenarier där tidigare säkra verktyg blir skadliga. För omfattande analys, se [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/sv/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Ytterligare AI-attackvektorer**

- **Cross-Domain Prompt Injection (XPIA)**: Sofistikerade attacker som utnyttjar innehåll från flera domäner för att kringgå säkerhetskontroller
- **Dynamisk kapacitetsmodifiering**: Realtidsförändringar av verktygskapaciteter som undkommer initiala säkerhetsbedömningar
- **Context Window Poisoning**: Attacker som manipulerar stora kontextfönster för att dölja skadliga instruktioner
- **Model Confusion Attacker**: Utnyttjande av modellbegränsningar för att skapa oförutsägbara eller osäkra beteenden

### AI-säkerhetsriskers påverkan

**Högpåverkande konsekvenser:**
- **Dataexfiltrering**: Obehörig åtkomst och stöld av känslig företags- eller personlig data
- **Integritetsbrott**: Exponering av personligt identifierbar information (PII) och konfidentiell affärsdata  
- **Systemmanipulation**: Oavsiktliga modifieringar av kritiska system och arbetsflöden
- **Stöld av autentiseringsuppgifter**: Kompromiss av autentiseringstokens och tjänstekredentialer
- **Lateral rörelse**: Användning av komprometterade AI-system som språngbrädor för bredare nätverksattacker

### Microsoft AI-säkerhetslösningar

#### **AI Prompt Shields: Avancerat skydd mot injektionsattacker**

Microsofts **AI Prompt Shields** erbjuder omfattande försvar mot både direkta och indirekta promptinjektionsattacker genom flera säkerhetslager:

##### **Kärnskyddsmekanismer:**

1. **Avancerad detektion & filtrering**
   - Maskininlärningsalgoritmer och NLP-tekniker upptäcker skadliga instruktioner i externt innehåll
   - Realtidsanalys av dokument, webbsidor, e-post och datakällor för inbäddade hot
   - Kontextuell förståelse av legitima kontra skadliga promptmönster

2. **Spotlighting-tekniker**  
   - Skiljer mellan betrodda systeminstruktioner och potentiellt komprometterade externa indata
   - Texttransformationsmetoder som förbättrar modellrelevans samtidigt som skadligt innehåll isoleras
   - Hjälper AI-system att upprätthålla korrekt instruktionshierarki och ignorera injicerade kommandon

3. **Avgränsare & datamarkeringssystem**
   - Tydlig gränsdragning mellan betrodda systemmeddelanden och extern indatatext
   - Specialmarkörer som framhäver gränser mellan betrodda och obetrodda datakällor
   - Klar separation förhindrar instruktionförvirring och obehörig kommandokörning

4. **Kontinuerlig hotintelligens**
   - Microsoft övervakar kontinuerligt framväxande attackmönster och uppdaterar försvar
   - Proaktiv hotjakt efter nya injektionstekniker och attackvektorer
   - Regelbundna säkerhetsmodelluppdateringar för att bibehålla effektivitet mot utvecklande hot

5. **Integration med Azure Content Safety**
   - Del av den omfattande Azure AI Content Safety-sviten
   - Ytterligare detektion för jailbreak-försök, skadligt innehåll och säkerhetspolicysbrott
   - Enhetliga säkerhetskontroller över AI-applikationskomponenter

**Implementeringsresurser**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/sv/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Avancerade MCP-säkerhetshot

### Sessionkapningssårbarheter

**Sessionkapning** utgör en kritisk attackvektor i stateful MCP-implementationer där obehöriga parter erhåller och missbrukar legitima sessionsidentifierare för att utge sig för klienter och utföra obehöriga åtgärder.

#### **Attackscenarier & risker**

- **Sessionkapnings-promptinjektion**: Angripare med stulna sessions-ID:n injicerar skadliga händelser i servrar som delar sessionsstatus, vilket potentiellt triggar skadliga åtgärder eller ger åtkomst till känslig data
- **Direkt utgivning**: Stulna sessions-ID:n möjliggör direkta MCP-serveranrop som kringgår autentisering och behandlar angripare som legitima användare
- **Komprometterade återupptagningsbara strömmar**: Angripare kan avbryta förfrågningar i förtid, vilket får legitima klienter att återuppta med potentiellt skadligt innehåll

#### **Säkerhetskontroller för sessionshantering**

**Kritiska krav:**
- **Verifiering av auktorisation**: MCP-servrar som implementerar auktorisation **MÅSTE** verifiera ALLA inkommande förfrågningar och **FÅR INTE** förlita sig på sessioner för autentisering  
- **Säker sessionsgenerering**: Använd kryptografiskt säkra, icke-deterministiska sessions-ID:n genererade med säkra slumptalsgeneratorer  
- **Användarspecifik bindning**: Binda sessions-ID:n till användarspecifik information med format som `<user_id>:<session_id>` för att förhindra missbruk av sessioner mellan användare  
- **Hantera sessionslivscykel**: Implementera korrekt utgång, rotation och ogiltigförklaring för att begränsa sårbarhetsfönster  
- **Transport säkerhet**: Obligatorisk HTTPS för all kommunikation för att förhindra avlyssning av sessions-ID:n  

### Problemet med förvirrad ombud

**Problemet med förvirrad ombud** uppstår när MCP-servrar agerar som autentiseringsproxyer mellan klienter och tredjepartstjänster, vilket skapar möjligheter för auktorisationsomgåelse genom exploatering av statiska klient-ID:n.

#### **Attackmekanik & risker**

- **Cookie-baserad samtyckesomgåelse**: Tidigare användarautentisering skapar samtyckes-cookies som angripare utnyttjar via skadliga auktorisationsförfrågningar med manipulerade redirect-URI:er  
- **Stöld av auktorisationskod**: Befintliga samtyckes-cookies kan få auktorisationsservrar att hoppa över samtyckesskärmar och omdirigera koder till angriparkontrollerade ändpunkter  
- **Obehörig API-åtkomst**: Stulna auktorisationskoder möjliggör tokenutbyte och användarförfalskning utan uttryckligt godkännande  

#### **Åtgärdsstrategier**

**Obligatoriska kontroller:**  
- **Explicit samtyckeskrav**: MCP-proxyservrar som använder statiska klient-ID:n **MÅSTE** inhämta användarsamtycke för varje dynamiskt registrerad klient  
- **OAuth 2.1 säkerhetsimplementering**: Följ aktuella OAuth-säkerhetsbästa praxis inklusive PKCE (Proof Key for Code Exchange) för alla auktorisationsförfrågningar  
- **Strikt klientvalidering**: Implementera rigorös validering av redirect-URI:er och klientidentifierare för att förhindra exploatering  

### Sårbarheter vid token-passthrough  

**Token passthrough** är ett uttryckligt anti-mönster där MCP-servrar accepterar klienttoken utan korrekt validering och vidarebefordrar dem till nedströms-API:er, vilket bryter mot MCP:s auktorisationsspecifikationer.

#### **Säkerhetskonsekvenser**

- **Omgång av kontroll**: Direkt klient-till-API-tokenanvändning kringgår kritiska begränsningar för hastighet, validering och övervakning  
- **Förstörd revisionskedja**: Token utfärdade uppströms gör klientidentifiering omöjlig och bryter utredningsmöjligheter vid incidenter  
- **Proxy-baserad dataexfiltrering**: Ovaliderade token möjliggör för illvilliga aktörer att använda servrar som proxy för obehörig dataåtkomst  
- **Brott mot förtroendegränser**: Nedströms-tjänsters förtroendeantaganden kan brytas när tokenursprung inte kan verifieras  
- **Expansion av attacker över flera tjänster**: Komprometterade token som accepteras över flera tjänster möjliggör laterala rörelser  

#### **Nödvändiga säkerhetskontroller**

**Icke-förhandlingsbara krav:**  
- **Tokenvalidering**: MCP-servrar **FÅR INTE** acceptera token som inte uttryckligen utfärdats för MCP-servern  
- **Verifiering av publik**: Validera alltid att token-publikumsanspråk matchar MCP-serverns identitet  
- **Korrekt tokenlivscykel**: Implementera kortlivade access-token med säkra rotationsrutiner  

## Leverantörskedjesäkerhet för AI-system

Leverantörskedjesäkerhet har utvecklats bortom traditionella mjukvaruberoenden till att omfatta hela AI-ekosystemet. Moderna MCP-implementationer måste noggrant verifiera och övervaka alla AI-relaterade komponenter, eftersom varje komponent introducerar potentiella sårbarheter som kan äventyra systemets integritet.

### Utökade AI-leverantörskedjekomponenter

**Traditionella mjukvaruberoenden:**  
- Öppen källkods-bibliotek och ramverk  
- Containerbilder och basystem  
- Utvecklingsverktyg och byggpipelines  
- Infrastrukturkomponenter och tjänster  

**AI-specifika leverantörskedjeelement:**  
- **Grundmodeller**: Förtränade modeller från olika leverantörer som kräver ursprungsverifiering  
- **Embedding-tjänster**: Externa vektoriseringsoch semantiska söktjänster  
- **Kontextleverantörer**: Datakällor, kunskapsbaser och dokumentarkiv  
- **Tredjeparts-API:er**: Externa AI-tjänster, ML-pipelines och dataprepareringsändpunkter  
- **Modellartefakter**: Vikter, konfigurationer och finjusterade modellvarianter  
- **Träningsdatasources**: Dataset som används för modellträning och finjustering  

### Omfattande strategi för leverantörskedjesäkerhet

#### **Komponentverifiering & förtroende**  
- **Ursprungsvalidering**: Verifiera ursprung, licensiering och integritet för alla AI-komponenter före integration  
- **Säkerhetsbedömning**: Genomför sårbarhetsskanningar och säkerhetsgranskningar för modeller, datakällor och AI-tjänster  
- **Rykteanalys**: Utvärdera säkerhetshistorik och praxis hos AI-tjänsteleverantörer  
- **Efterlevnadsverifiering**: Säkerställ att alla komponenter uppfyller organisatoriska säkerhets- och regulatoriska krav  

#### **Säkra distributionspipelines**  
- **Automatiserad CI/CD-säkerhet**: Integrera säkerhetsskanning i automatiserade distributionspipelines  
- **Artefaktintegritet**: Implementera kryptografisk verifiering för alla distribuerade artefakter (kod, modeller, konfigurationer)  
- **Stegvis distribution**: Använd progressiva distributionsstrategier med säkerhetsvalidering i varje steg  
- **Betrodda artefaktregister**: Distribuera endast från verifierade, säkra artefaktregister och arkiv  

#### **Kontinuerlig övervakning & respons**  
- **Beroendeskanning**: Löpande sårbarhetsövervakning för alla mjukvaru- och AI-komponentberoenden  
- **Modellövervakning**: Kontinuerlig bedömning av modellbeteende, prestandadrift och säkerhetsavvikelser  
- **Tjänstehälsospårning**: Övervaka externa AI-tjänster för tillgänglighet, säkerhetsincidenter och policyändringar  
- **Hotintelligensintegration**: Inkorporera hotflöden specifika för AI- och ML-säkerhetsrisker  

#### **Åtkomstkontroll & minsta privilegium**  
- **Komponentnivåbehörigheter**: Begränsa åtkomst till modeller, data och tjänster baserat på affärsbehov  
- **Hantera tjänstekonton**: Implementera dedikerade tjänstekonton med minimala nödvändiga behörigheter  
- **Nätverkssegmentering**: Isolera AI-komponenter och begränsa nätverksåtkomst mellan tjänster  
- **API-gateway-kontroller**: Använd centraliserade API-gateways för att kontrollera och övervaka åtkomst till externa AI-tjänster  

#### **Incidentrespons & återhämtning**  
- **Snabba responsrutiner**: Etablerade processer för patchning eller ersättning av komprometterade AI-komponenter  
- **Rotering av autentiseringsuppgifter**: Automatiserade system för rotation av hemligheter, API-nycklar och tjänsteautentiseringar  
- **Återställningsmöjligheter**: Förmåga att snabbt återgå till tidigare kända fungerande versioner av AI-komponenter  
- **Återhämtning vid leverantörskedjebrott**: Specifika rutiner för att hantera komprometteringar i uppströms AI-tjänster  

### Microsofts säkerhetsverktyg & integration

**GitHub Advanced Security** erbjuder omfattande skydd för leverantörskedjan inklusive:  
- **Hemlighetsskanning**: Automatisk upptäckt av autentiseringsuppgifter, API-nycklar och token i arkiv  
- **Beroendeskanning**: Sårbarhetsbedömning för öppen källkodsberoenden och bibliotek  
- **CodeQL-analys**: Statisk kodanalys för säkerhetssårbarheter och kodningsproblem  
- **Insikter om leverantörskedjan**: Synlighet i beroendehälsa och säkerhetsstatus  

**Integration med Azure DevOps & Azure Repos:**  
- Sömlös säkerhetsskanning över Microsofts utvecklingsplattformar  
- Automatiska säkerhetskontroller i Azure Pipelines för AI-arbetsbelastningar  
- Policys för säker distribution av AI-komponenter  

**Microsofts interna praxis:**  
Microsoft implementerar omfattande leverantörskedjesäkerhet över alla produkter. Läs om beprövade metoder i [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).  

## Grundläggande säkerhetspraxis

MCP-implementationer ärver och bygger vidare på din organisations befintliga säkerhetsläge. Att stärka grundläggande säkerhetspraxis förbättrar avsevärt den övergripande säkerheten för AI-system och MCP-distributioner.

### Kärnprinciper för säkerhet

#### **Säkra utvecklingspraxis**  
- **OWASP-efterlevnad**: Skydda mot [OWASP Top 10](https://owasp.org/www-project-top-ten/) webbapplikationssårbarheter  
- **AI-specifika skydd**: Implementera kontroller för [OWASP Top 10 för LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- **Säker hantering av hemligheter**: Använd dedikerade valv för token, API-nycklar och känslig konfigurationsdata  
- **End-to-end-kryptering**: Implementera säker kommunikation över alla applikationskomponenter och dataflöden  
- **Inmatningsvalidering**: Strikt validering av alla användarinmatningar, API-parametrar och datakällor  

#### **Hårdning av infrastruktur**  
- **Multifaktorautentisering**: Obligatorisk MFA för alla administrativa och tjänstekonton  
- **Patchhantering**: Automatiserad, snabb patchning för operativsystem, ramverk och beroenden  
- **Integration med identitetsleverantörer**: Centraliserad identitetshantering via företagsidentitetsleverantörer (Microsoft Entra ID, Active Directory)  
- **Nätverkssegmentering**: Logisk isolering av MCP-komponenter för att begränsa lateral rörelse  
- **Principen om minsta privilegium**: Minimala nödvändiga behörigheter för alla systemkomponenter och konton  

#### **Säkerhetsövervakning & detektion**  
- **Omfattande loggning**: Detaljerad loggning av AI-applikationsaktiviteter, inklusive MCP klient-server-interaktioner  
- **SIEM-integration**: Centraliserad säkerhetsinformations- och händelsehantering för avvikelsedetektion  
- **Beteendeanalys**: AI-driven övervakning för att upptäcka ovanliga mönster i system- och användarbeteende  
- **Hotintelligens**: Integration av externa hotflöden och kompromissindikatorer (IOC)  
- **Incidentrespons**: Väl definierade rutiner för upptäckt, respons och återhämtning vid säkerhetsincidenter  

#### **Zero Trust-arkitektur**  
- **Lita aldrig, verifiera alltid**: Kontinuerlig verifiering av användare, enheter och nätverksanslutningar  
- **Mikrosegmentering**: Granulära nätverkskontroller som isolerar individuella arbetsbelastningar och tjänster  
- **Identitetscentrerad säkerhet**: Säkerhetspolicys baserade på verifierade identiteter snarare än nätverksplats  
- **Kontinuerlig riskbedömning**: Dynamisk utvärdering av säkerhetsläge baserat på aktuell kontext och beteende  
- **Villkorad åtkomst**: Åtkomstkontroller som anpassas efter riskfaktorer, plats och enhetens förtroende  

### Mönster för företagsintegration

#### **Integration i Microsofts säkerhetsekosystem**  
- **Microsoft Defender for Cloud**: Omfattande hantering av molnsäkerhetsläge  
- **Azure Sentinel**: Molnbaserad SIEM och SOAR-funktionalitet för skydd av AI-arbetsbelastningar  
- **Microsoft Entra ID**: Företagsidentitets- och åtkomsthantering med villkorade åtkomstpolicys  
- **Azure Key Vault**: Centraliserad hantering av hemligheter med hårdvarubaserad säkerhetsmodul (HSM)  
- **Microsoft Purview**: Datastyrning och efterlevnad för AI-datakällor och arbetsflöden  

#### **Efterlevnad & styrning**  
- **Regulatorisk anpassning**: Säkerställ att MCP-implementationer uppfyller branschspecifika efterlevnadskrav (GDPR, HIPAA, SOC 2)  
- **Dataklassificering**: Korrekt kategorisering och hantering av känslig data som behandlas av AI-system  
- **Revisionsspår**: Omfattande loggning för regulatorisk efterlevnad och forensisk utredning  
- **Integritetskontroller**: Implementering av integritet-by-design-principer i AI-systemarkitektur  
- **Ändringshantering**: Formella processer för säkerhetsgranskning av AI-systemändringar  

Dessa grundläggande praxis skapar en robust säkerhetsbas som förbättrar effektiviteten hos MCP-specifika säkerhetskontroller och ger omfattande skydd för AI-drivna applikationer.  

## Viktiga säkerhetsinsikter

- **Lager-på-lager-säkerhetsstrategi**: Kombinera grundläggande säkerhetspraxis (säker kodning, minsta privilegium, leverantörskedjeverifiering, kontinuerlig övervakning) med AI-specifika kontroller för heltäckande skydd  

- **AI-specifik hotbild**: MCP-system står inför unika risker inklusive promptinjektion, verktygsförgiftning, sessionkapning, problem med förvirrade ombud, token-passthrough-sårbarheter och överdrivna behörigheter som kräver specialiserade motåtgärder  

- **Excellens i autentisering & auktorisation**: Implementera robust autentisering med externa identitetsleverantörer (Microsoft Entra ID), upprätthåll korrekt tokenvalidering och acceptera aldrig token som inte uttryckligen utfärdats för din MCP-server  

- **Förebygg AI-attacker**: Distribuera Microsoft Prompt Shields och Azure Content Safety för att försvara mot indirekt promptinjektion och verktygsförgiftningsattacker, samtidigt som verktygsmetadata valideras och dynamiska förändringar övervakas  

- **Sessions- & transport säkerhet**: Använd kryptografiskt säkra, icke-deterministiska sessions-ID:n bundna till användaridentiteter, implementera korrekt hantering av sessionslivscykel och använd aldrig sessioner för autentisering  

- **OAuth-säkerhetsbästa praxis**: Förhindra attacker med förvirrade ombud genom explicit användarsamtycke för dynamiskt registrerade klienter, korrekt OAuth 2.1-implementering med PKCE och strikt validering av redirect-URI:er  

- **Token-säkerhetsprinciper**: Undvik token-passthrough-anti-mönster, validera token-publikumsanspråk, implementera kortlivade token med säker rotation och upprätthåll tydliga förtroendegränser  

- **Omfattande leverantörskedjesäkerhet**: Behandla alla AI-ekosystemets komponenter (modeller, embeddingar, kontextleverantörer, externa API:er) med samma säkerhetsnoggrannhet som traditionella mjukvaruberoenden  

- **Kontinuerlig utveckling**: Håll dig uppdaterad med snabbt utvecklande MCP-specifikationer, bidra till säkerhetsgemenskapens standarder och upprätthåll adaptiva säkerhetslägen i takt med att protokollet mognar  

- **Microsofts säkerhetsintegration**: Utnyttja Microsofts omfattande säkerhetsekosystem (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) för förbättrat skydd vid MCP-distribution  

## Omfattande resurser

### **Officiell MCP-säkerhetsdokumentation**  
- [MCP-specifikation (Aktuell: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP:s säkerhetsbästa praxis](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP:s auktorisationsspecifikation](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  
- [MCP GitHub-repository](https://github.com/modelcontextprotocol)  

### **Säkerhetsstandarder & bästa praxis**  
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 Web Application Security](https://owasp.org/www-project-top-ten/)  
- [OWASP Top 10 för stora språkmodeller](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Microsoft Digital Defense Report](https://aka.ms/mddr)  

### **AI-säkerhetsforskning & analys**  
- [Prompt Injection i MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Verktygsförgiftningsattacker (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)  

- [MCP Security Research Briefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Security Solutions**
- [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management Best Practices](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Implementation Guides & Tutorials**
- [Azure API Management as MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Authentication with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Secure Token Storage and Encryption (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & Supply Chain Security**
- [Azure DevOps Security](https://azure.microsoft.com/products/devops)
- [Azure Repos Security](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Supply Chain Security Journey](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Ytterligare säkerhetsdokumentation**

För omfattande säkerhetsvägledning, se dessa specialiserade dokument i denna sektion:

- **[MCP Security Best Practices 2025](./mcp-security-best-practices-2025.md)** - Kompletta säkerhetsbästa praxis för MCP-implementeringar
- **[Azure Content Safety Implementation](./azure-content-safety-implementation.md)** - Praktiska implementeringsexempel för Azure Content Safety-integration  
- **[MCP Security Controls 2025](./mcp-security-controls-2025.md)** - Senaste säkerhetskontroller och tekniker för MCP-distributioner
- **[MCP Best Practices Quick Reference](./mcp-best-practices.md)** - Snabbreferensguide för viktiga MCP-säkerhetspraxis

---

## Vad händer härnäst

Nästa: [Kapitel 3: Komma igång](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->