# AGENTS.md

## Projekti ülevaade

**Alustajate MCP** on avatud lähtekoodiga hariduslik õppekava Model Context Protocol'i (MCP) õppimiseks – standardiseeritud raamistik tehisintellekti mudelite ja kliendirakenduste vaheliseks suhtluseks. See hoidla pakub põhjalikke õppematerjale ja praktilisi koodi näiteid mitmes programmeerimiskeeles.

### Peamised tehnoloogiad

- **Programmeerimiskeeled**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Raamistikud ja SDK-d**:
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Andmebaasid**: PostgreSQL koos pgvector laiendusega
- **Pilveplatvormid**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Build-tööriistad**: npm, Maven, pip, Cargo
- **Dokumentatsioon**: Markdown koos automatiseeritud mitmekeelse tõlkega (48+ keelt)

### Arhitektuur

- **11 põhimoodulit (00-11)**: Järjestikune õppeteekond alates alustaladest kuni edasijõudnuteni
- **Praktilised töötoad**: Praktikad täielike lahenduskoodidega mitmes keeles
- **Näidisprojektid**: Töötavad MCP serveri ja kliendi rakendused
- **Tõlkesüsteem**: Automatiseeritud GitHub Actions töövoog mitmekeelse toe jaoks
- **Pildivarad**: Keskne piltide kataloog tõlgitud versioonidega

## Seadistus käsud

See on dokumentatsioonile keskenduv hoidla. Enamik seadistamist toimub individuaalsetes näidisprojektides ja töötubades.

### Hoidla seadistus

```bash
# Kopeeri hoidla
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Töö näidisprojektidega

Näidisprojektid asuvad:
- `03-GettingStarted/samples/` - keeltespetsiifilised näited
- `03-GettingStarted/01-first-server/solution/` - Esimeste serveri rakenduste lahendused
- `03-GettingStarted/02-client/solution/` - Kliendi rakendused
- `11-MCPServerHandsOnLabs/` - Kõik kaetavad andmebaasi integreerimise töökodad

Igas näidisprojektis on oma seadistusjuhised:

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
# või
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

### MCP 7-28 Valmidus

#### Hoidla valmiduse kontrollnimekiri

- [x] **Uue kaasautorina selgus**: See fail määratleb hoidla eesmärgi,
  struktuuri, panustamise reeglid ja näidisprojektide seadistusrajad.
- [x] **Build/test/lint käsud täpsete lippudega**:
  - Hoidla dokumentatsiooni lint:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Hoidla dokumentatsiooni lingipatterni audit:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript näidiste valideerimine:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python näidiste valideerimine:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java näidiste valideerimine:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Üks realistlik töövoog, mis võib saada MCP tööriistaks**:
  `validate_curriculum_change`
- [x] **Sisendid/väljundid on eksplicitseeritud** (vt allpool spetsifikatsiooni).
- [x] **Õigused ja vearežiimid on dokumenteeritud** (vt allpool spetsifikatsiooni).
- [x] **CI testitavus on eksplicitne** (deterministlikud käsud, eksplicitseid
  väljumiskoodid ja masinalugemise väljundid).

#### Kandidaat MCP tööriista töövoog: `validate_curriculum_change`

##### Eesmärk

Valideerida õppekava dokumentatsiooni muudatused ja esinduslik näidiskood
seisundi kontroll enne liitmist.

##### Sisendid

- `changed_paths: string[]` (nõutud) - PR-i muudetud suhtelised teed.
- `run_docs_lint: boolean` (vaikimisi `true`)
- `run_links_audit: boolean` (vaikimisi `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (vaikimisi kõik `false`)

##### Väljundid

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Õigused

- Lugeda tööruumi faile ja kirjutada tööriista genereeritud artefakte (nt lint
  aruanded, testilogid); ei tohi kirjutada `translations/` ega
  `translated_images/` kaustadesse.
- Käivitada kohalikke shell käske.
- Võimalik võrguühendus ainult pakettide taastamiseks (`npm ci`,
  `python -m pip install`, `mvn` sõltuvuste lahendus).
- Ei ole õigust pushida, merge'ida ega muuta `translations/` ega
  `translated_images/` kaustu.

##### Vearežiimid

- `E_NO_INPUT_PATHS`: `changed_paths` tühi.
- `E_INVALID_PATH`: sisendtee väljaspool hoidla juurkausta.
- `E_LINT_FAILED`: markdown lint väljub mitte-null koodi.
- `E_LINK_AUDIT_FAILED`: linkide auditi käsk väljub mitte-null koodiga.
- `E_SAMPLE_TEST_FAILED`: näidistest või build ebaõnnestub.
- `E_TIMEOUT`: käsk ületas lubatud ajalimiidi.

##### Soovitatav CI leping

Automaatseks valideerimiseks seadista CI töö, mis:

- Käivitub pull request'ide puhul, mis puudutavad `*.md`, näidiskoodi või seda faili.
- Käivitab täpselt ülaltoodud käsud.
- Salvestab logid artefaktidena.
- Töö nurjub mistahes mittenull väljundkoodi korral.

#### Kui te tarnite MCP serveri sellest hoidlast

- [ ] Lugege MCP 7-28 mustandi muudatustelogit:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Käivitage oma server SDK beeta versioonide vastu:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Eemaldage sessiooni ja käepigistuse eeldused; käsitlege iga päringut
  iseseisvana:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Saada `Mcp-Method` ja `Mcp-Name` päised toorete HTTP päringute puhul:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Auditige kõvakodeeritud veakoodid (`missing resource` liigutati `-32002` pealt `-32602` peale).

- [ ] Märgista ja planeeri üleminek aegunud juurtele, proovivõtule ja
  logimisele:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Üleminek eksperimenteelsest `2025-11-25` Tasks API-st:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Vaata üle autoriseerimine OAuth ja OpenID Connect tugevdamiseks:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Dokumentatsiooni struktuur

- **Moodulid 00-11**: Tuumikõppekava sisu järjekorras
- **translations/**: Keele-spetsiifilised versioonid (automaatselt genereeritud, mitte otseselt redigeerida)
- **translated_images/**: Lokaliseeritud pildiversioonid (automaatselt genereeritud)
- **images/**: Allikapildid ja skeemid

### Dokumentatsioonimuudatuste tegemine

1. Muuda ainult ingliskeelseid markdown-faile juurmoodulite kataloogides (00-11)
2. Värskenda vajadusel pilte kaustas `images/`
3. co-op-translator GitHub Action genereerib automaatselt tõlked
4. Tõlked uuenevad automaatselt, kui tehakse push main harule

### Tõlketega töötamine

- **Automaatne tõlkimine**: GitHub Actions töökäik haldab kõiki tõlkeid
- **Ära käsitsi muuda** faile kataloogis `translations/`
- Tõlke metaandmed on iga tõlgitud faili sees
- Toetatud keeled: üle 48 keele, sh araabia, hiina, prantsuse, saksa, hindi, jaapani, korea, portugali, vene, hispaania ja paljud teised

## Testimise juhised

### Dokumentatsiooni valideerimine

Kuna tegemist on peamiselt dokumentatsiooni hoidla, keskendub testimine järgnevatele:

1. **Linkide mustri audit**: Loetle Markdown lingid ülevaatamiseks

   ```bash
   # Loetle Markdowni lingid (mustri audit)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Koodinäidiste valideerimine**: Kontrolli, et koodinäited kompileeruvad/jooksevad

   ```bash
   # Navigeeri konkreetse näidise juurde ja käivita selle testid
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdowni lintimine**: Kontrolli vorminduse järjepidevust

   ```bash
   # Kasutage vajadusel markdownlinti
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Näidise projekti testimine

Iga keele-spetsiifiline näidis sisaldab oma testimismeetodit:

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

## Koodi stiili juhised

### Dokumentatsiooni stiil

- Kasuta selget, algajasõbralikku keelt
- Lisa koodinäited mitmes keeles, kus see asjakohane
- Järgi markdowni parimaid praktikaid:
  - Kasuta ATX-stiilis päiseid (`#` süntaks)
  - Kasuta resstringitud koodiplokke koos keelemääranguga
  - Lisa kirjeldav alternatiivtekst piltidele
  - Hoia ridade pikkus mõistlikuna (ei ole ranget limiiti, kuid ole mõistlik)

### Koodinäidiste stiil

#### TypeScript/JavaScript
- Kasuta ES mooduleid (`import`/`export`)
- Järgi TypeScript range režiimi konventsioone
- Lisa tüübisildid
- Siht ES2022

#### Python
- Järgi PEP 8 stiilijuhiseid
- Kasuta tüübisõnumeid, kus sobib
- Lisa funktsioonide ja klasside docstringid
- Kasuta kaasaegseid Pythoni võimalusi (3.8+)

#### Java
- Järgi Spring Boot konventsioone
- Kasuta Java 21 võimalusi
- Järgi standardset Maven projekti struktuuri
- Lisa Javadoc kommentaarid

### Failide korraldus

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

## Koostamine ja juurutamine

### Dokumentatsiooni juurutamine

Hoidla kasutab dokumentatsiooni majutamiseks GitHub Pages'i või sarnast teenust (kui kohaldatav). Muudatused main harule käivitavad:

1. Tõlketöövoo (`.github/workflows/co-op-translator.yml`)
2. Kõigi ingliskeelsete markdown-failide automaatse tõlkimise
3. Piltide lokaliseerimise vastavalt vajadusele

### Koostamisprotsessi ei ole vaja

See hoidla sisaldab peamiselt markdown-dokumentatsiooni. Tuumikõppekava sisu jaoks ei ole vaja kompileerimise ega koostamise sammu.

### Näidisprojekti juurutamine

Üksiknäidise projektidel võivad olla juurutamise juhised:
- Vaata `03-GettingStarted/09-deployment/` MCP serveri juurutamise juhiste jaoks
- Azure Container Apps juurutamise näited kaustas `11-MCPServerHandsOnLabs/`

## Panustamise juhised

### Pull Requesti protsess

1. **Forka ja klooni**: Forki hoidla ja klooni oma fork lokaalselt
2. **Loo haru**: Kasuta kirjeldavaid harunimesid (nt `fix/typo-module-3`, `add/python-example`)
3. **Tee muudatused**: Muuda ainult ingliskeelseid markdown-faile (mitte tõlkeid)
4. **Testi lokaalselt**: Kontrolli, et markdown joonistub õigesti
5. **Esita PR**: Kasuta selgeid PR pealkirju ja kirjeldusi
6. **CLA**: Allkirjasta Microsoft Contributor License Agreement, kui küsitakse

### PR pealkirja formaat

Kasuta selgeid, kirjeldavaid pealkirju:
- `[Module XX] Lühikirjeldus` moodulispetsiifiliste muudatuste jaoks
- `[Samples] Kirjeldus` näidis koodimuudatuste jaoks
- `[Docs] Kirjeldus` üldiste dokumentatsiooni värskenduste jaoks

### Mida panustada

- Veaparandused dokumentatsioonis või koodinäidetes
- Uued koodinäited täiendavates keeltes
- Selgitused ja täiustused olemasolevas sisus
- Uued juhtumiuuringud või praktilised näited
- Teated ebaselge või valesti oleva sisu kohta

### Mida mitte teha

- Ära muuda otse faile kataloogis `translations/`
- Ära muuda `translated_images/` kataloogi
- Ära lisa suuri binaarfailide ilma eelneva aruteluta
- Ära muuda tõlketöövoo faile ilma kooskõlastuseta

## Täiendavad märkused

### Hoidla hooldus

- **Muudatuste logi**: Kõik olulised muudatused on dokumenteeritud failis `changelog.md`
- **Õpi juhend**: Kasuta `study_guide.md` õppekava navigeerimise ülevaate jaoks
- **Probleemitemplid**: Kasuta GitHubi issue malle vea- ja funktsioonipäringute jaoks
- **Käitumiskoodeks**: Kõik panustajad peavad järgima Microsofti avatud lähtekoodi käitumiskoodeksit

### Õppeteekond

Järgi mooduleid järjest (00-11) optimaalseks õppimiseks:
1. **00-02**: Alused (Sissejuhatus, põhimõisted, turvalisus)
2. **03**: Käed-külge algus ja praktiline rakendamine
3. **04-05**: Praktiline rakendamine ja edasijõudnud teemad
4. **06-10**: Kogukond, parimad praktikad ja reaalse maailma rakendused
5. **11**: Põhjalikud andmebaasi integreerimise töötoad (13 järjestikust töötuba)

### Tugiteenused

- **Dokumentatsioon**: https://modelcontextprotocol.io/
- **Spetsifikatsioon**: https://spec.modelcontextprotocol.io/
- **Kogukond**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord server
- **Seotud kursused**: Vaata README.md teisi Microsofti õppeteid

### Tavalised tõrkeotsingu juhised

**K: Minu PR ei läbi tõlkekontrolli**
V: Veendu, et muutsid ainult ingliskeelseid markdown-faile juurmoodulite kataloogides, mitte tõlkeid.

**K: Kuidas lisada uus keel?**
V: Keeletoetus on hallatud co-op-translator töövoo kaudu. Ava arutelu uue keele lisamise üle.

**K: Koodinäited ei tööta**

V: Veenduge, et olete järginud konkreetse näidise README seadistusjuhiseid. Kontrollige, et teil on paigaldatud õiged sõltuvuste versioonid.

**K: Pildid ei kuvata**
V: Kontrollige, et pilditeed on suhtelised ja kasutavad kaldkriipsu. Pildid peaksid olema `images/` kataloogis või lokaliseeritud versioonide puhul `translated_images/` kataloogis.

### Jõudluslikud kaalutlused

- Tõlkekäigus võib minna mitu minutit
- Suured pildid tuleks enne seotud tegemist optimeerida
- Hoidke üksikud markdown-failid sihipärased ja mõõdukalt mahukad
- Kasutage parema kaasaskantavuse huvides suhtelisi linke

### Projekti juhtimine

See projekt järgib Microsofti avatud lähtekoodi tavasid:
- Koodi ja dokumentatsiooni puhul MIT litsents
- Microsofti avatud lähtekoodi käitumiskoodeks
- Panustamiseks on vajalik CLA
- Turvalisuse probleemid: Järgige juhiseid failis SECURITY.md
- Toetus: Vt failist SUPPORT.md abiressursse

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->