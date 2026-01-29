# AGENTS.md

## Projekti ülevaade

**MCP algajatele** on avatud lähtekoodiga hariduslik õppekava Model Context Protocol (MCP) õppimiseks – standardiseeritud raamistik AI mudelite ja kliendirakenduste vaheliseks suhtluseks. See repositoorium pakub põhjalikke õppematerjale koos praktiliste koodinäidetega mitmes programmeerimiskeeles.

### Peamised tehnoloogiad

- **Programmeerimiskeeled**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Raamistikud ja SDK-d**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Andmebaasid**: PostgreSQL koos pgvector laiendusega
- **Pilveplatvormid**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Ehitusvahendid**: npm, Maven, pip, Cargo
- **Dokumentatsioon**: Markdown koos automaatse mitmekeelse tõlkega (48+ keelt)

### Arhitektuur

- **11 põhikomponenti (00-11)**: Järjestikune õppeprotsess alustades põhitõdedest kuni keerukamate teemadeni
- **Praktilised laborid**: Praktilised harjutused koos täielike lahenduskoodidega mitmes keeles
- **Näidisprojektid**: Töötavad MCP serveri ja kliendi rakendused
- **Tõlkesüsteem**: Automaatne GitHub Actions töövoog mitmekeelse toe jaoks
- **Pildifailid**: Keskne pildikataloog koos tõlgitud versioonidega

## Seadistuskäsud

See on dokumentatsioonile keskenduv repositoorium. Enamik seadistust toimub individuaalsete näidisprojektide ja laborite sees.

### Repositooriumi seadistamine

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Näidisprojektidega töötamine

Näidisprojektid asuvad:
- `03-GettingStarted/samples/` - Keelepõhised näited
- `03-GettingStarted/01-first-server/solution/` - Esimese serveri rakendused
- `03-GettingStarted/02-client/solution/` - Kliendi rakendused
- `11-MCPServerHandsOnLabs/` - Põhjalikud andmebaasi integreerimise laborid

Igal näidisprojektil on oma seadistusjuhised:

#### TypeScript/JavaScript projektid
```bash
cd <project-directory>
npm install
npm start
```

#### Python projektid
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Java projektid
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Arendustöövoog

### Dokumentatsiooni struktuur

- **Moodulid 00-11**: Põhiõppekava sisu järjestatud kujul
- **translations/**: Keelepõhised versioonid (automaatselt genereeritud, mitte otse redigeerida)
- **translated_images/**: Lokaliseeritud pildiversioonid (automaatselt genereeritud)
- **images/**: Algupärased pildid ja diagrammid

### Dokumentatsiooni muudatuste tegemine

1. Redigeeri ainult ingliskeelseid markdown-faile juurmoodulite kataloogides (00-11)
2. Uuenda vajadusel pilte kataloogis `images/`
3. GitHub Action nimega co-op-translator genereerib automaatselt tõlked
4. Tõlked genereeritakse uuesti, kui muudatused lükatakse põhiharusse

### Tõlgetega töötamine

- **Automaatne tõlge**: GitHub Actions töövoog haldab kõiki tõlkeid
- **Ära muuda käsitsi** faile kataloogis `translations/`
- Tõlkemetaandmed on iga tõlgitud faili sees
- Toetatud keeled: 48+ keelt, sealhulgas araabia, hiina, prantsuse, saksa, hindi, jaapani, korea, portugali, vene, hispaania ja paljud teised

## Testimisjuhised

### Dokumentatsiooni valideerimine

Kuna tegemist on peamiselt dokumentatsioonirepositooriumiga, keskendub testimine järgmistele:

1. **Linkide valideerimine**: Kontrolli, et kõik sisemised lingid töötavad
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Koodinäidete valideerimine**: Testi, et koodinäited kompileeruvad/töötavad
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown lintimine**: Kontrolli vorminduse järjepidevust
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Näidisprojektide testimine

Igal keelepõhisel näidisel on oma testimisjuhised:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Koodistiili juhised

### Dokumentatsiooni stiil

- Kasuta selget, algajasõbralikku keelt
- Lisa koodinäiteid mitmes keeles, kui võimalik
- Järgi markdowni parimaid tavasid:
  - Kasuta ATX-stiilis päiseid (`#` süntaks)
  - Kasuta piiritletud koodiblokke koos keele identifikaatoritega
  - Lisa piltidele kirjeldav alt-tekst
  - Hoia rea pikkused mõistlikud (ei ole ranget piirangut, kuid ole mõistlik)

### Koodinäidete stiil

#### TypeScript/JavaScript
- Kasuta ES mooduleid (`import`/`export`)
- Järgi TypeScripti rangete režiimide konventsioone
- Lisa tüübimärkused
- Sihtmärgiks ES2022

#### Python
- Järgi PEP 8 stiilijuhiseid
- Kasuta tüübivihjeid, kui sobilik
- Lisa funktsioonidele ja klassidele docstringid
- Kasuta kaasaegseid Python funktsioone (3.8+)

#### Java
- Järgi Spring Boot konventsioone
- Kasuta Java 21 funktsioone
- Järgi standardset Maven projekti struktuuri
- Lisa Javadoc kommentaarid

### Failide organiseerimine

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Ehitus ja juurutamine

### Dokumentatsiooni juurutamine

Repositoorium kasutab dokumentatsiooni majutamiseks GitHub Pages või sarnast (kui rakendatav). Muudatused põhiharus käivitavad:

1. Tõlketöövoo (`.github/workflows/co-op-translator.yml`)
2. Kõigi ingliskeelsete markdown-failide automaatse tõlke
3. Piltide lokaliseerimise vastavalt vajadusele

### Ehitusprotsessi pole vaja

See repositoorium sisaldab peamiselt markdown-dokumentatsiooni. Põhiõppekava sisu jaoks pole vaja kompileerimist ega ehitusetappi.

### Näidisprojektide juurutamine

Individuaalsetel näidisprojektidel võivad olla juurutusjuhised:
- Vaata `03-GettingStarted/09-deployment/` MCP serveri juurutamise juhiseid
- Azure Container Apps juurutamise näited kataloogis `11-MCPServerHandsOnLabs/`

## Kaastöö juhised

### Pull Request protsess

1. **Fork ja kloonimine**: Forki repositoorium ja klooni oma fork lokaalselt
2. **Loo haru**: Kasuta kirjeldavaid harunimesid (nt `fix/typo-module-3`, `add/python-example`)
3. **Tee muudatused**: Redigeeri ainult ingliskeelseid markdown-faile (mitte tõlkeid)
4. **Testi lokaalselt**: Kontrolli, et markdown kuvatakse õigesti
5. **Esita PR**: Kasuta selgeid PR pealkirju ja kirjeldusi
6. **CLA**: Allkirjasta Microsofti kaastöö litsentsileping, kui seda küsitakse

### PR pealkirja formaat

Kasuta selgeid, kirjeldavaid pealkirju:
- `[Module XX] Lühikirjeldus` moodulispetsiifiliste muudatuste jaoks
- `[Samples] Kirjeldus` näidiskoodi muudatuste jaoks
- `[Docs] Kirjeldus` üldise dokumentatsiooni uuenduste jaoks

### Mida panustada

- Dokumentatsiooni või koodinäidete veaparandused
- Uued koodinäited täiendavates keeltes
- Olemasoleva sisu täpsustused ja täiustused
- Uued juhtumiuuringud või praktilised näited
- Probleemide aruanded ebaselge või vale sisu kohta

### Mida mitte teha

- Ära muuda otse faile kataloogis `translations/`
- Ära muuda kataloogi `translated_images/`
- Ära lisa suuri binaarfaile ilma aruteluta
- Ära muuda tõlketöövoo faile ilma kooskõlastuseta

## Täiendavad märkused

### Repositooriumi hooldus

- **Muudatuste logi**: Kõik olulised muudatused dokumenteeritakse failis `changelog.md`
- **Õpijuhend**: Kasuta `study_guide.md` õppekava navigeerimise ülevaateks
- **Probleemimallid**: Kasuta GitHubi probleemimalle veaaruannete ja funktsioonisoovide jaoks
- **Käitumisjuhend**: Kõik kaastöötajad peavad järgima Microsofti avatud lähtekoodi käitumisjuhendit

### Õppimisrada

Järgi mooduleid järjestatud kujul (00-11) optimaalseks õppimiseks:
1. **00-02**: Põhitõed (Sissejuhatus, Põhimõisted, Turvalisus)
2. **03**: Praktiline alustamine
3. **04-05**: Praktiline rakendamine ja keerukamad teemad
4. **06-10**: Kogukond, parimad tavad ja reaalsed rakendused
5. **11**: Põhjalikud andmebaasi integreerimise laborid (13 järjestikust laborit)

### Tugimaterjalid

- **Dokumentatsioon**: https://modelcontextprotocol.io/
- **Spetsifikatsioon**: https://spec.modelcontextprotocol.io/
- **Kogukond**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord server
- **Seotud kursused**: Vaata README.md teisi Microsofti õpiradasid

### Tavalised tõrkeotsingud

**K: Minu PR ei läbi tõlke kontrolli**
V: Veendu, et redigeerisid ainult ingliskeelseid markdown-faile juurmoodulite kataloogides, mitte tõlgitud versioone.

**K: Kuidas lisada uut keelt?**
V: Keeletuge hallatakse co-op-translator töövoo kaudu. Ava probleem, et arutada uue keele lisamist.

**K: Koodinäited ei tööta**
V: Veendu, et järgiksid konkreetse näidise README seadistusjuhiseid. Kontrolli, et sul on õiged versioonid sõltuvustest paigaldatud.

**K: Pildid ei kuvata**
V: Kontrolli, et pilditeed oleksid suhtelised ja kasutaksid kaldkriipse. Pildid peaksid olema kataloogis `images/` või `translated_images/` lokaliseeritud versioonide jaoks.

### Jõudluse kaalutlused

- Tõlketöövoog võib võtta mitu minutit
- Suured pildid tuleks enne commitimist optimeerida
- Hoia individuaalsed markdown-failid keskendunud ja mõistliku suurusega
- Kasuta suhtelisi linke parema teisaldatavuse jaoks

### Projekti juhtimine

See projekt järgib Microsofti avatud lähtekoodi praktikaid:
- MIT litsents koodi ja dokumentatsiooni jaoks
- Microsofti avatud lähtekoodi käitumisjuhend
- Kaastöö litsentsileping (CLA) on nõutav
- Turvalisuse küsimused: Järgi SECURITY.md juhiseid
- Tugi: Vaata SUPPORT.md abiressursside jaoks

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.