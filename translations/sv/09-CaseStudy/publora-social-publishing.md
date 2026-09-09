# Fallstudie: Publicering till sociala nätverk från en agent med en fjärr-MCP-server

> **Ansvarsfriskrivning:** Flera tjänster och open-source-projekt kan publicera till sociala nätverk, och ett team kan också integrera varje nätverks API direkt. Scenariot nedan ges som ett arbets-exempel på hur en **skrivkapabel fjärr-MCP-server** kan designas och användas. Publora är en kommersiell tjänst med ett gratisnivå; mönstren som beskrivs här gäller för alla MCP-servrar som utför irreversibla åtgärder åt en användare.

## Översikt

Agenter är bra på att utarbeta innehåll men dåliga på att leverera det. En modell kan skriva ett pressmeddelande på några sekunder, och sedan upphör arbetet: att publicera det innebär ett API per nätverk, en OAuth-app per nätverk och olika uppsättningar medieregler för varje. De flesta team löser detta genom att kopiera texten till en webbläsare manuellt.

Denna fallstudie tittar på hur det sista steget stängs med en enda fjärr-MCP-server, och – mer användbart för alla som bygger en sådan – på designbesluten en **skrivkapabel** server måste få rätt. Att läsa data är förlåtande. Att publicera är det inte: ett felaktigt verktygsanrop syns för en publik och kan inte ångras.

## Scenario

Ett litet team för utvecklarrelationer skriver utkast till inlägg inuti en agent (Claude, VS Code, Cursor – klienten spelar ingen roll). De vill att agenten ska:

- se vilka sociala konton teamet har kopplat,
- skriva ett utkast till inlägg och hålla det som ett utkast för en människa att godkänna,
- bifoga en bild,
- schemalägga det till flera nätverk vid vald tidpunkt,
- och senare rapportera hur det presterade.

Avgörande är att de vill att agenten *inte ska kunna* publicera av misstag medan de fortfarande experimenterar.

## Använda verktyg

- [Publora MCP Server](https://github.com/publora/mcp-server) — en fjärr-MCP-server (`streamable-http`) som exponerar publicering, schemaläggning, media och LinkedIn-analysverktyg. Registrerad i den officiella MCP-registret som `com.publora/mcp-server`.

## Steg-för-steg-arbetsflöde

1. **Anslut servern.** Klienter som använder OAuth genomför authorizationskodflödet med PKCE mot serverns egen samtyckesskärm; klienter som inte gör det, såsom headless CLI:er, använder en Publora API-nyckel i en header. Båda vägar stöds, och vilken du får beror på klienten, inte på servern.
2. **Lista anslutningar.** Agenten anropar `list_connections` och får tillbaka de anslutna kontona med deras identifierare.
3. **Utkast.** Agenten anropar `create_post` *utan* schemalagd tid. Inlägget sparas som ett utkast — ingenting publiceras.
4. **Bifoga media.** Offentliga bild-URL:er skickas med i samma anrop; servern laddar ner och validerar dem.
5. **Schemalägg.** Efter att en människa godkänt, sätter `update_post` status till schemalagt med en ISO 8601-tid.
6. **Mät.** För LinkedIn returnerar `linkedin_post_stats` engagemang när inlägget är aktivt.

## Exempelprompt

```text
Which social accounts do I have connected?
Draft a post announcing our new changelog page, attach the screenshot at
https://example.com/changelog.png, and keep it as a draft — do not publish it.
Once I approve, schedule it to LinkedIn and Bluesky for tomorrow at 09:00 UTC.
```

## Mermaid-flödesschema

```mermaid
flowchart TD
    A[Användarfråga i en MCP-klient] --> B[Klienten utför OAuth med servern]
    B --> C[lista_anslutningar]
    C --> D{Mål-nätverk anslutna?}
    D -- No --> E[Agent rapporterar vilka som saknas]
    D -- Yes --> F[skapa_inlägg utan schemalagtTid -> utkast]
    F --> G[Människa granskar utkastet]
    G -- Approved --> H[update_post: status=schemalagd]
    G -- Rejected --> I[ta_bort_inlägg]
    H --> J[Server publicerar vid schemalagd tid]
    J --> K[linkedin_inlägg_statistik för engagemang]
```

## Teknisk implementering

Lärdomarna nedan är den överförbara delen av denna fallstudie.

### Öppen upptäckt, autentiserad exekvering

`tools/list` tjänas ut utan inloggning; varje `tools/call` kräver en token och returnerar annars `401` med en `WWW-Authenticate`-header som pekar på metadata för skyddade resurser. (Servern svarar också på en oautentiserad `initialize`, vilket bara spelar roll för klienter på protokollversioner före `2026-07-28`; den revisionen tog helt bort handskakningen.)

Denna uppdelning spelar roll i praktiken. Register, kataloger och klienter kan utforska verktygsytan — namn, scheman, anteckningar — utan att hålla en hemlighet, medan ingenting kan *köras* anonymt. En server som kräver token för `initialize` är effektivt osynlig för verktyg; en server som tillåter anonym `tools/call` är en risk.

### Registrering: dynamisk klientregistrering och vad som ersätter den

Servern annonserar `/.well-known/oauth-protected-resource` och `/.well-known/oauth-authorization-server`, och stödjer authorizationskodflödet med PKCE (`S256`), refresh tokens och **dynamisk klientregistrering**.

Dynamisk registrering tar bort det manuella steget: utan den behöver varje klient en förutgiven `client_id`, vilket innebär en utanför-bandet-förfrågan till leverantören för varje ny klient.

Behandla detta som kompatibilitetsbeteende snarare än som en design att kopiera. `2026-07-28`-revisionen av specifikationen avvecklar dynamisk klientregistrering till förmån för Client ID Metadata Documents, där klienten hostar ett metadokument på en stabil HTTPS-URL och den URL:en *är* `client_id`. DCR fortsätter fungera för tillfället, men en server som byggs idag bör planera för CIMD och behålla DCR bara för äldre klienter.

### Verktygsanteckningar är inte dekoration

Varje verktyg bär en `title` och tillämpliga hints: `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`.

Två anledningar att satsa på dem. För det första använder klienter hints för att bestämma vad som ska bekräftas med användaren — en klient kan automatiskt köra en läs-nyckel och pausa för godkännande innan en radering. Specifikationen är tydlig att anteckningar är opålitliga hints, inte en auktorisationsmekanism: de formar vad en klient erbjuder att göra, de stoppar inget på servern, och servern måste fortfarande tillämpa sina egna regler. För det andra kräver nu stora anslutningskataloger dem för granskning; en server vars verktyg saknar titlar och hints kommer att skickas tillbaka oavsett hur väl den fungerar.

### Gör identifierare omöjliga att hitta på

Plattformidentifierare är opaka strängar som returneras av `list_connections`, och schema-beskrivningen säger uttryckligen att de ska kopieras ordagrant och aldrig gissas. Servern avvisar allt annat.

Modeller är flytande gissare. Alla skrivkapabla servrar bör anta att en identifierare så småningom kommer att hallucineras och låta den vägen faila högljutt och tidigt, snarare än att agera på ett trovärdigt utseende värde.

### Misslyckas före publicering, med ett åtgärdbart meddelande

Vissa nätverk vägrar bara textinlägg och kräver en bild eller video. Det valideras när inlägget schemaläggs, och felet namnger plattformen och det saknade kravet.

En agent kan återhämta sig från "Instagram kräver media — bifoga en bild eller video" utan en ny omgång. Den kan inte återhämta sig från ett generellt `400`.

### Gör omförsök säkra

De två verktygen som skapar innehåll, `create_post` och `update_post`, accepterar en idempotensnyckel: att återanvända den med en identisk förfrågan spelare upp det ursprungliga svaret istället för att skapa ett andra inlägg. Agentmiljöer gör omförsök vid timeout; utan idempotens blir ett långsamt svar en dublett-publicering. De andra skrivverktygen – borttagningar, mediasteg, LinkedIn-reaktioner och kommentarer – tar ingen nyckel, så omförsök där är inte automatiskt säkra. Värt att veta vilka av dina mutationer som är skyddade och vilka som inte är det.

### Erbjud ett sätt att testa som inte publicerar något

Servern accepterar ett reserverat mål, `publora-playground`, som valideras och bekräftas som en riktig destination och sedan kasseras – ingenting når ett levande konto. Det beskrivs i verktygsschemat självt, som vilken klient som helst kan läsa utan behörighet: `platforms`-fältet för `create_post` dokumenterar det som "ett testanslutningsmål som inte kräver någon verklig anslutning – inlägget bekräftas och kasseras, ingenting publiceras". Anropa det genom att skicka det som enda post: `platforms: ["publora-playground"]`.

Detta visade sig vara en av de mest användbara detaljerna i hela ytan. Granskare av anslutningskataloger, bidragsgivare och CI kan testa hela skrivvägen från början till slut utan risk för en verklig publik. Alla MCP-servrar med irreversibla åtgärder drar nytta av ett dokumenterat no-op-mål.

## Resultat och påverkan

- Publiceringssteget flyttades från en webbläsare till samma konversation där innehållet skrivs, och en vana att börja med utkast håller en människa i loopen. Var tydlig med vad det är: ett utkast är en konvention, inte en gräns. Samma behörighet kan schemalägga eller publicera, så den som behöver en riktig godkännandegrind måste tillämpa den utanför verktygsytan – separata behörigheter, eller ett policylager framför servern.
- Skillnader per nätverk — mediekrav, trådar, svarskontroller — hanteras en gång på servern istället för i varje agent som kommunicerar med den.
- Samma server stöder flera MCP-klienter utan per-klient-arbete, eftersom upptäckt är öppen och registrering dynamisk.
- Designbegränsningarna ovan formades lika mycket av granskning av anslutningskataloger som av användare: anteckningar, OAuth och ett säkert testmål krävdes av minst en av dem.

## Referenser

- [Publora MCP Server (källkod)](https://github.com/publora/mcp-server)
- [Publora API och MCP-dokumentation](https://docs.publora.com)
- [MCP Registry-post: `com.publora/mcp-server`](https://registry.modelcontextprotocol.io/v0/servers?search=com.publora/mcp-server)
- [MCP-specifikation — Auktorisation](https://modelcontextprotocol.io/specification/draft/basic/authorization)
- [MCP-specifikation — Verktygsanteckningar](https://modelcontextprotocol.io/docs/concepts/tools)

## Vad händer härnäst

- Ta en MCP-server du bygger och kontrollera de tre billigaste förbättringarna här: anteckningar på varje verktyg, en idempotensnyckel på varje skrivning och ett dokumenterat no-op-mål.
- Prova den öppna upptäcktsuppdelningen: anropa `tools/list` mot en offentlig fjärrserver utan behörighet, anropa sedan ett verktyg och inspektera `401`-utmaningen.
- Fundera på vad "ångra" betyder för din domän. Publicering har utkast och radering; om dina åtgärder saknar motsvarighet hör bekräftelse hemma i verktygsdesignen, inte i prompten.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->