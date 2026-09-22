# AGENTS.md

## Pregled projekta

**MCP za početnike** je open-source obrazovni kurikulum za učenje Model Context Protocola (MCP) - standardiziranog okvira za interakcije između AI modela i klijentskih aplikacija. Ovaj repozitorij sadrži potpune materijale za učenje sa praktičnim primjerima koda na više programskih jezika.

### Ključne tehnologije

- **Programsko jezici**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Okviri i SDK-ovi**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Baze podataka**: PostgreSQL s pgvector ekstenzijom
- **Cloud platforme**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Alati za izgradnju**: npm, Maven, pip, Cargo
- **Dokumentacija**: Markdown s automatiziranim prijevodom na više jezika (48+ jezika)

### Arhitektura

- **11 glavnih modula (00-11)**: Sekvencijalni put učenja od osnova do naprednih tema
- **Praktični laboratoriji**: Praktične vježbe s kompletim rješenjima koda na više jezika
- **Primjeri projekata**: Funkcionalne implementacije MCP servera i klijenta
- **Sustav prijevoda**: Automatizirani GitHub Actions workflow za podršku više jezika
- **Slike**: Centralizirani direktorij slika s prevedenim verzijama

## Komande za postavljanje

Ovo je repozitorij fokusiran na dokumentaciju. Većina postavljanja odvija se unutar pojedinačnih primjera projekata i laboratorija.

### Postavljanje repozitorija

```bash
# Klonirajte repozitorij
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Rad s primjerima projekata

Primjeri projekata nalaze se u:
- `03-GettingStarted/samples/` - Primjeri specifični za jezik
- `03-GettingStarted/01-first-server/solution/` - Prve implementacije servera
- `03-GettingStarted/02-client/solution/` - Implementacije klijenta
- `11-MCPServerHandsOnLabs/` - Obuhvatni laboratoriji za integraciju baze podataka

Svaki primjer projekta sadrži vlastite upute za postavljanje:

#### TypeScript/JavaScript projekti
```bash
cd <project-directory>
npm install
npm start
```

#### Python projekti
```bash
cd <project-directory>
pip install -r requirements.txt
# ili
pip install -e .
python main.py
```

#### Java projekti
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Radni tok razvoja

### Spremnost MCP 7-28

#### Provjera spremnosti repozitorija

- [x] **Jasnoća za nove suradnike**: Ova datoteka definira svrhu repozitorija,
  strukturu, pravila doprinosa i putanje za postavljanje primjera.
- [x] **Komande za build/test/lint s točnim parametrima**:
  - Lint dokumentacije repozitorija:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Pregled linkova u dokumentaciji:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validacija primjera TypeScript-a:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validacija primjera Python-a:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validacija primjera Java-e:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Jedan realan radni tok koji može postati MCP alat**:
  `validate_curriculum_change`
- [x] **Ulazi/izlazi su eksplicitni** (vidi specifikaciju dolje).
- [x] **Dozvole i načini otkazivanja su dokumentirani** (vidi specifikaciju dolje).
- [x] **Testiranje u CI je eksplicitno** (determinističke komande, eksplicitni
  izlazni kodovi i strojno čitljivi izlazi).

#### Kandidat za MCP alatni radni tok: `validate_curriculum_change`

##### Cilj

Validirati promjene u dokumentaciji kurikuluma i reprezentativni uzorak koda
zdravlje prije spajanja.

##### Ulazi

- `changed_paths: string[]` (obavezno) - relativne putanje promijenjene u PR-u.
- `run_docs_lint: boolean` (zadano `true`)
- `run_links_audit: boolean` (zadano `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (zadano sve `false`)

##### Izlazi

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Dozvole

- Čitanje datoteka u radnom prostoru i pisanje artefakata generiranih alatom (npr., lint
  izvješća, zapisnici testova) samo; bez pisanja u `translations/` ili
  `translated_images/`.
- Izvršavanje lokalnih shell komandi.
- Opcionalan mrežni pristup samo za vraćanje paketa (`npm ci`,
  `python -m pip install`, `mvn` rješavanje ovisnosti).
- Nema dozvole za push, merge ili izmjenu u `translations/` ili
  `translated_images/`.

##### Načini otkazivanja

- `E_NO_INPUT_PATHS`: `changed_paths` je prazan.
- `E_INVALID_PATH`: ulazna putanja izlazi iz korijena repozitorija.
- `E_LINT_FAILED`: markdown lint je završio s ne-nultim kodom.
- `E_LINK_AUDIT_FAILED`: audit linkova komanda je završila s ne-nultim kodom.
- `E_SAMPLE_TEST_FAILED`: test/izgradnja primjera je završila s ne-nultim kodom.
- `E_TIMEOUT`: komanda je prekoračila konfigurirano vrijeme.

##### Preporučeni CI ugovor

Za automatizaciju validacije, konfigurirajte CI posao koji:

- Pokreće se na pull requeste koji diraju `*.md`, primjere koda ili ovu datoteku.
- Izvršava točne komandne linije navedene gore.
- Čuva zapisnike kao artefakte.
- Neuspjeh na bilo koji ne-nulti izlazni kod.

#### Ako distribuirate MCP server iz ovog repozitorija

- [ ] Pročitajte završni MCP `2026-07-28` changelog:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Provjerite podržava li odabrano SDK izdanje MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Uklonite pretpostavke o sesiji i rukovanju; tretirajte svaki zahtjev kao
  samostalan:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Pošaljite zaglavlja `Mcp-Method` i `Mcp-Name` za raw HTTP zahtjeve:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Provjerite hardkodirane šifre pogrešaka (`missing resource` premješteno s `-32002` na `-32602`).
- [ ] Migrirajte deprecated Roots, Sampling, Logging i Dynamic Client
  Registration:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migrirajte s eksperimentalnog `2025-11-25` Tasks API-ja:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Pregledajte autorizaciju za jačanje OAuth i OpenID Connect:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Struktura dokumentacije

- **Moduli 00-11**: Glavni sadržaj kurikuluma u sekvencijalnom redoslijedu
- **translations/**: Jezične specifične verzije (automatski generirane, ne uređivati direktno)
- **translated_images/**: Lokalizirane verzije slika (automatski generirane)
- **images/**: Izvorne slike i dijagrami

### Izmjene u dokumentaciji

1. Uredite samo engleske markdown datoteke u korijenskim direktorijima modula (00-11)
2. Ažurirajte slike u direktoriju `images/` ako je potrebno
3. co-op-translator GitHub akcija automatski će generirati prijevode
4. Prijevodi se regeneriraju pri pushu na glavnu granu

### Rad s prijevodima

- **Automatizirani prijevod**: GitHub Actions workflow upravlja svim prijevodima
- **Nemojte ručno uređivati** datoteke u direktoriju `translations/`
- Metapodaci prijevoda ugrađeni su u svaku prevedenu datoteku
- Podržani jezici: 48+ jezika uključujući arapski, kineski, francuski, njemački, hindi, japanski, korejski, portugalski, ruski, španjolski i mnoge druge

## Upute za testiranje

### Validacija dokumentacije

Kako je ovo prvenstveno repozitorij za dokumentaciju, testiranje se fokusira na:

1. **Pregled uzorka linkova**: Popis Markdown linkova za pregled

   ```bash
   # Popis Markdown poveznica (audit uzorka)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validacija primjera koda**: Testirati da se primjeri koda kompajliraju/pokreću

   ```bash
   # Navigirajte do određenog uzorka i pokrenite njegove testove
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown linting**: Provjeriti dosljednost formata

   ```bash
   # Koristite markdownlint ako je potrebno
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testiranje primjera projekata

Svaki primjer za specifični jezik ima svoj pristup testiranju:

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

## Smjernice za stil koda

### Stil dokumentacije

- Koristite jasan, pristupačan jezik za početnike
- Uključite primjere koda na više jezika gdje je primjenjivo
- Slijedite najbolje prakse za markdown:
  - Koristite ATX stil zaglavlja (`#` sintaksa)
  - Koristite fenced code blockove s označenim jezikom
  - Uključite opisne alt tekstove za slike
  - Držite duljine redaka razumne (bez stroge granice, ali budite razboriti)

### Stil primjera koda

#### TypeScript/JavaScript
- Koristite ES module (`import`/`export`)
- Slijedite TypeScript strogi način rada konvencija
- Uključite tipne anotacije
- Ciljajte ES2022

#### Python
- Slijedite PEP 8 smjernice za stil
- Koristite tipne nagovještaje gdje je prikladno
- Uključite docstringove za funkcije i klase
- Koristite moderne Python značajke (3.8+)

#### Java
- Slijedite Spring Boot konvencije
- Koristite Java 21 značajke
- Slijedite standardnu Maven strukturu projekta
- Uključite Javadoc komentare

### Organizacija datoteka

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

## Izgradnja i implementacija

### Implementacija dokumentacije

Repozitorij koristi GitHub Pages ili slično za hosting dokumentacije (ako je primjenjivo). Promjene na glavnoj grani pokreću:

1. Workflow prijevoda (`.github/workflows/co-op-translator.yml`)
2. Automatizirani prijevod svih engleskih markdown datoteka
3. Lokalizaciju slika prema potrebi

### Nije potreban proces izgradnje

Ovaj repozitorij prvenstveno sadrži markdown dokumentaciju. Nije potreban korak kompilacije ili izgradnje za glavni sadržaj kurikuluma.

### Implementacija primjera projekata

Pojedinačni primjeri projekata mogu imati upute za implementaciju:
- Pogledajte `03-GettingStarted/09-deployment/` za smjernice implementacije MCP servera
- Primjeri implementacije Azure Container Apps u `11-MCPServerHandsOnLabs/`

## Smjernice za doprinos

### Proces za Pull Request

1. **Fork i kloniraj**: Forkaj repozitorij i kloniraj svoj fork lokalno
2. **Kreiraj granu**: Koristi opisne nazive grana (npr., `fix/typo-module-3`, `add/python-example`)
3. **Napravite izmjene**: Uredite samo engleske markdown datoteke (ne prijevode)
4. **Testirajte lokalno**: Provjerite ispravno renderiranje markdowna
5. **Pošaljite PR**: Koristite jasne naslove i opise PR-a
6. **CLA**: Potpišite Microsoft Contributor License Agreement kada se zatraži

### Format naslova PR-a

Koristite jasne, opisne naslove:
- `[Module XX] Kratak opis` za izmjene specifične za modul
- `[Samples] Opis` za izmjene primjeraka koda
- `[Docs] Opis` za opće izmjene dokumentacije

### Što doprinijeti

- Ispravke grešaka u dokumentaciji ili primjerima koda
- Novi primjeri koda za dodatne jezike
- Pojašnjenja i poboljšanja postojećeg sadržaja
- Novi studiji slučaja ili praktični primjeri
- Prijave problema za nejasan ili netočan sadržaj

### Što NE raditi

- Nemojte direktno uređivati datoteke u direktoriju `translations/`
- Nemojte uređivati direktorij `translated_images/`
- Nemojte dodavati velike binarne datoteke bez rasprave
- Nemojte mijenjati datoteke workflowa za prijevod bez koordinacije

## Dodatne napomene

### Održavanje repozitorija

- **Changelog**: Sve značajne promjene dokumentirane su u `changelog.md`
- **Studijski vodič**: Koristite `study_guide.md` za pregled navigacije kurikuluma
- **Predlošci za probleme**: Koristite GitHub predloške za prijavu grešaka i zahtjeva za značajke
- **Kodeks ponašanja**: Svi suradnici moraju poštovati Microsoft Open Source Code of Conduct

### Put učenja

Slijedite module u sekvencijalnom redu (00-11) za optimalno učenje:
1. **00-02**: Osnove (Uvod, Temeljni koncepti, Sigurnost)
2. **03**: Početak rada s praktičnom implementacijom
3. **04-05**: Praktična implementacija i napredne teme
4. **06-10**: Zajednica, najbolje prakse i primjene u stvarnom svijetu
5. **11**: Sveobuhvatni laboratoriji za integraciju baze podataka (13 uzastopnih laboratorija)

### Resursi za podršku

- **Dokumentacija**: https://modelcontextprotocol.io/
- **Specifikacija**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Zajednica**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord server
- **Povezani tečajevi**: Pogledajte README.md za druge Microsoft putove učenja

### Uobičajene poteškoće

**P: Moj PR ne prolazi provjeru prijevoda**
O: Provjerite jeste li uređivali samo engleske markdown datoteke u korijenskim direktorijima modula, a ne prevedene verzije.

**P: Kako dodati novi jezik?**
O: Podrška za jezike upravlja se kroz co-op-translator workflow. Otvorite issue za raspravu o dodavanju novih jezika.

**P: Primjeri koda ne rade**
O: Provjerite jeste li slijedili upute za postavljanje u README datoteci konkretnih primjera. Provjerite imate li ispravne verzije zavisnosti.

**P: Slike se ne prikazuju**

A: Provjerite jesu li putanje slika relativne i koriste li kosa crta prema naprijed. Slike bi trebale biti u direktoriju `images/` ili `translated_images/` za lokalizirane verzije.

### Razmatranja vezana uz performanse

- Radni tijek prevođenja može potrajati nekoliko minuta
- Velike slike treba optimizirati prije commitanja
- Održavajte pojedinačne markdown datoteke fokusirane i razumno veličine
- Koristite relativne poveznice radi bolje prenosivosti

### Upravljanje projektom

Ovaj projekt slijedi Microsoftove prakse otvorenog koda:
- MIT licenca za kod i dokumentaciju
- Microsoftov Kodeks ponašanja za otvoreni kod
- CLA potreban za doprinose
- Sigurnosna pitanja: Slijedite upute iz SECURITY.md
- Podrška: Pogledajte SUPPORT.md za resurse pomoći

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->