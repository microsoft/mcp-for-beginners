# Juhtumiuuring: Avaldamine sotsiaalvõrgustikes agendi kaudu kaug- MCP serveriga

> **Märkus:** Mitmed teenused ja avatud lähtekoodiga projektid saavad avaldada sotsiaalvõrgustikes ning meeskond võiks ka integreerida iga võrgu API otse. Alljärgnev stsenaarium on esitatud kui üks töötav näide sellest, kuidas saab kavandada ja kasutada **kirjutamisvõimelist kaug-MCP serverit**. Publora on kommertsteenus tasuta astmega; siin kirjeldatud mustrid kehtivad mis tahes MCP serveri kohta, mis teeb kasutaja nimel pöördumatuid toiminguid.

## Ülevaade

Agendid on head sisu loomisel, kuid halvad selle edastamisel. Mudel suudab pressiteate sekunditega kirjutada, kuid siis töö peatub: avaldamine tähendab iga võrgu puhul eraldi API-d, iga võrgu jaoks OAuth rakendust ja erinevate meediapoliitikate komplekti. Enamik meeskondi lahendab selle, kopeerides teksti käsitsi brauserisse.

See juhtumiuuring vaatleb, kuidas see viimane samm lahendatakse ühe kaug-MCP serveriga ja — kasulikum kõigile, kes sellist loovad — disainivalikuid, mida **kirjutamisvõimeline** server peab õigesti tegema. Andmete lugemine on andestav. Avaldamine mitte: vale tööriistakõne on publikule nähtav ja seda ei saa tagasi võtta.

## Stsenaarium

Väike arendussuhete meeskond koostab postitusi agendi sees (Claude, VS Code, Cursor — klient ise ei ole oluline). Nad tahavad, et agent:

- näeks, millised sotsiaalkontod meeskonnal on ühendatud,
- koostaks postituse ja hoiaks seda mustandina inimese kinnitamiseks,
- lisaks pildi manustaks,
- ajastaks selle valitud ajal mitmesse võrku,
- ja hiljem annaks aru selle tulemustest.

Otsustavalt tahavad nad, et agent *ei saaks* katsetamise ajal kogemata postitada.

## Kasutatavad tööriistad

- [Publora MCP Server](https://github.com/publora/mcp-server) — kaugrežiimil MCP server (`streamable-http`), mis pakub avaldamise, ajastamise, meedia ja LinkedIni analüütika tööriistu. Registreeritud ametlikus MCP registris kui `com.publora/mcp-server`.

## Samm-sammult töövoog

1. **Ühenda server.** OAuth-toega kliendid lõpetavad autoriseerimiskoodi voogude PKCE-ga vastavalt serveri enda nõusolekuekraani vastu; kliendid, kes ei toeta seda, nt pea- CLI-d, kasutavad Päraora API võtit päises. Mõlemad meetodid on toetatud ja valiku määrab klient, mitte server.
2. **Tõmba ühendused.** Agent kutsub välja `list_connections` ja saab ühendatud kontod koos identifikaatoritega.
3. **Koosta mustand.** Agent kutsub `create_post` *ilma* ajastamata aja määramata. Postitus salvestatakse mustandina — midagi ei avaldata.
4. **Lisa meedia.** Avalikud pildi URL-id edastatakse samas kõnes; server laeb need alla ja valideerib.
5. **Ajasta.** Kui inimene kinnitab, määrab `update_post` staatuseks ajastatud ISO 8601 vormingus ajaga.
6. **Mõõda.** LinkedIni puhul tagastab `linkedin_post_stats` kaasatuse, kui postitus on avalik.

## Näite päring

```text
Which social accounts do I have connected?
Draft a post announcing our new changelog page, attach the screenshot at
https://example.com/changelog.png, and keep it as a draft — do not publish it.
Once I approve, schedule it to LinkedIn and Bluesky for tomorrow at 09:00 UTC.
```

## Mermaid vooskeem

```mermaid
flowchart TD
    A[Kasutaja päring MCP kliendis] --> B[Klient teostab OAuthi serveriga]
    B --> C[list_connections]
    C --> D{Kas sihtvõrgud on ühendatud?}
    D -- No --> E[Agent teatab, millised puuduvad]
    D -- Yes --> F[create_post ilma scheduledTime-ta -> mustand]
    F --> G[Inimene vaatab mustandi üle]
    G -- Approved --> H[update_post: status=scheduled]
    G -- Rejected --> I[delete_post]
    H --> J[Server avaldab määratud ajal]
    J --> K[linkedin_post_stats seotuse kohta]
```

## Tehniline teostus

Alljärgnevad õppetunnid on selle juhtumiuuringu ülekantavad osad.

### Avatud avastus, autentitud täitmine

`tools/list` on pakutav ilma mandaadita; iga `tools/call` nõuab tokenit
ning vastasel korral tagastab `401` koos `WWW-Authenticate` päisega, mis osutab
kaitstud ressursside metakirjeldusele. Serveri vanem otsapunkt vastab ka
autentimata `initialize` päringule klientidelt enne
`2026-07-28` versiooni; tänapäeva kliendid seda kättesaadet ei kasuta.

See serveripõhine jagunemine võimaldab registritel, kataloogidel ja klientidel tööriistu
nime, skeemi ja annotatsioonide põhjal uurida ilma saladuseta, kuid takistab anonüümset
täitmist. Avatud avastus on juurutamisvalik, mitte MCP nõue; kaitstud juurutus
võib samuti nõuda autoriseerimist `tools/list` jaoks.

### Registreerimine: dünaamiline kliendiregistreerimine ja selle asendus

Server reklaamib `/.well-known/oauth-protected-resource` ja `/.well-known/oauth-authorization-server` ning toetab


Dünaamiline registreerimine eemaldas käsitsi sammu pärandkliendid: ilma selleta




























Server aktsepteerib reserveeritud sihtmärki `publora-playground`, mida valideeritakse ja tunnistatakse nagu tõelist sihtkohta ning seejärel visatakse ära — midagi ei jõua tõelisse kontosse. See on kirjeldatud tööriista skeemis endas, mida igal kliendil on võimalik lugeda ilma volitusteta: `create_post` dokumentide väli `platforms` kirjeldab seda kui "ühenduse-testimise sihtmärk, mis ei vaja tegelikku ühendust — postitus võetakse vastu ja visatakse ära, midagi ei avaldata". Kutsu seda, andes selle ainsa kirjena: `platforms: ["publora-playground"]`.

See osutus üheks kasulikumaks detailiks kogu kasutajaliidese juures. Ühenduskaustade vaatlejad, kaasautorid ja CI saavad kogu kirjutamistee lõpuni läbi proovida ilma riskita tõelise publikuni jõudmiseks. Iga MCP server, millel on pöördumatud toimingud, saab kasu dokumenteeritud mitte-operatiivsest sihtmärgist.

## Tulemused ja mõju

- Avaldamisetapp liikus brauserist samasse vestlusesse, kuhu sisu kirjutatakse, ja esmalt mustandiga harjumus hoiab inimest protsessis kaasatuna. Ole täpne selle kohta, mis see on: mustand on kokkulepe, mitte piiriäär. Sama volitus saab ajastada või avaldada, nii et kellel iganes on tõeline kinnituse silt vaja, peab selle jõustama väljaspool tööriistaliidest — eraldi volitused või poliitikakiht serveri ees.
- Võrgupõhised erinevused — meedia nõuded, lõimimine, vastuste kontroll — lahendatakse korra serveris, mitte igas kõneleva agendi sees.
- Sama server teenindab mitut MCP klienti ilma eelväljastatud volitusteta.
    Praegused kliendid saavad kasutada kliendi ID metaandmete dokumente; DCR jääb varuplaaniks
    vanematele klientidele.
- Ülaltoodud disainipiiranguid vormisid nii ühenduskaustade vaatlused kui ka kasutajad: annotatsioonid, OAuth ja turvaline test-sihtriik nõudis igaüks vähemalt üks neist.

## Viited

- [Publora MCP server (allikas)](https://github.com/publora/mcp-server)
- [Publora API ja MCP dokumentatsioon](https://docs.publora.com)
- [MCP registrikirje: `com.publora/mcp-server`](https://registry.modelcontextprotocol.io/v0/servers?search=com.publora/mcp-server)
- [MCP spetsifikatsioon — Autentimine](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP spetsifikatsioon — Tööriista annotatsioonid](https://modelcontextprotocol.io/docs/concepts/tools)

## Mis Järgmiseks

- Võta MCP server, mida sa ehitad, ja kontrolli siit kolme odavaimat võitu: annotatsioonid igal tööriistal, idempotentsusvõti igal kirjutamisel ja dokumenteeritud mitte-operaalne sihtmärk.
- Proovi avatud-avastamise jagunemist: tee `tools/list` päring avaliku kaugrešiimiga serveri vastu ilma volitusteta, seejärel kutsu tööriista ja vaata üle `401` väljakutse.
- Mõtle, mida tähendab "tühistamine" sinu domeenis. Avaldamisel on mustandid ja kustutamine; kui sinu toimingutel pole vastet, kuulub kinnitamine tööriista disaini, mitte viibale.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->