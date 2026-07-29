# AGENTS.md

## Pregled Projekta

**MCP za početnike** je edukativni kurikulum otvorenog koda za učenje Model Context Protocol (MCP) — standardiziranog okvira za interakcije između AI modela i korisničkih aplikacija. Ovaj repozitorij pruža sveobuhvatne materijale za učenje s praktičnim primjerima koda na više programskih jezika.

### Ključne Tehnologije

- **Programsko Jezik**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Okviri i SDK-ovi**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Baze Podataka**: PostgreSQL s pgvector dodatkom
- **Cloud Platforme**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Alati za Izgradnju**: npm, Maven, pip, Cargo
- **Dokumentacija**: Markdown s automatiziranim prevođenjem na više jezika (48+ jezika)

### Arhitektura

- **11 Jezgrenih Modula (00-11)**: Sekvencijalni put učenja od osnova do naprednih tema
- **Praktične Radionice**: Praktični zadaci s kompletno rješenim kodom na više jezika
- **Primjerni Projekti**: Funkcionalne implementacije MCP servera i klijenta
- **Sustav Prevođenja**: Automatizirani GitHub Actions tok za podršku više jezika
- **Slikovni Resursi**: Centralizirani direktorij slika s prevedenim verzijama

## Naredbe za Postavljanje

Ovo je repozitorij fokusiran na dokumentaciju. Većina postavljanja odvija se unutar pojedinačnih primjera projekata i radionica.

### Postavljanje Repozitorija

```bash
# Klonirajte spremište
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Rad s Primjernim Projektima

Primjerni projekti nalaze se u:
- `03-GettingStarted/samples/` — Primjeri specifični za jezik
- `03-GettingStarted/01-first-server/solution/` — Prve server implementacije
- `03-GettingStarted/02-client/solution/` — Implementacije klijenata
- `11-MCPServerHandsOnLabs/` — Sveobuhvatne radionice s integracijom baza podataka

Svaki primjerni projekt sadrži svoje upute za postavljanje:

#### Projekti TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Projekti Python
```bash
cd <project-directory>
pip install -r requirements.txt
# ili
pip install -e .
python main.py
```

#### Projekti Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Radni Proces Razvoja

### Spremnost za MCP 7-28

#### Kontrolni popis spremnosti repozitorija

- [x] **Jasnoća za nove suradnike**: Ova datoteka definira svrhu repozitorija,
  strukturu, pravila doprinosa i putanje za postavljanje primjera.
- [x] **Naredbe za izgradnju/testiranje/lint s točnim zastavicama**:
  - Lint dokumentacije repozitorija:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Revizija obrasca poveznica u dokumentaciji:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validacija TypeScript primjera:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validacija Python primjera:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validacija Java primjera:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Jedan realan radni proces koji može postati MCP alat**:
  `validate_curriculum_change`
- [x] **Ulazi/izlazi su eksplicitni** (vidi specifikaciju dolje).
- [x] **Dozvole i načini neuspjeha su dokumentirani** (vidi specifikaciju dolje).
- [x] **Testabilnost CI je eksplicitna** (determinističke naredbe, eksplicitni
  izlazni kodovi i strojno čitljivi izlazi).

#### Kandidat za MCP alatni radni proces: `validate_curriculum_change`

##### Cilj

Validirati promjene u dokumentaciji kurikuluma i reprezentativni kod
njegovog zdravlja prije spajanja.

##### Ulazi

- `changed_paths: string[]` (obavezno) — relativne promijenjene putanje u PR-u.
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

- Čitati datoteke radnog prostora i pisati artefakte generirane alatom (npr., izvještaji o lintu,
  testni zapisi) samo; bez pisanja u `translations/` ili
  `translated_images/`.
- Izvršavati lokalne shell naredbe.
- Opcionalan mrežni pristup samo za vraćanje paketa (`npm ci`,
  `python -m pip install`, `mvn` rješavanje ovisnosti).
- Nema dozvole za push, merge ili izmjene `translations/` ili
  `translated_images/`.

##### Načini neuspjeha

- `E_NO_INPUT_PATHS`: `changed_paths` je prazno.
- `E_INVALID_PATH`: ulazna putanja izlazi izvan korijena repozitorija.
- `E_LINT_FAILED`: markdown lint završava s nenultim kodom.
- `E_LINK_AUDIT_FAILED`: naredba revizije poveznica završava s nenultim kodom.
- `E_SAMPLE_TEST_FAILED`: test/izgradnja primjera završava s nenultim kodom.
- `E_TIMEOUT`: naredba premašila konfigurirano ograničenje vremena.

##### Preporučeni CI ugovor

Za automatizaciju validacije, konfigurirajte CI zadatak koji:

- Pokreće se na pull request-ove koji uključuju `*.md`, primjerni kod ili ovu datoteku.
- Izvršava točno navedene naredbe gore.
- Čuva zapise kao artefakte.
- Neuspješno završava zadatak na bilo koji nenulti izlazni kod.

#### Ako isporučujete MCP server iz ovog repozitorija

- [ ] Pročitajte nacrt izvještaja promjena za MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Pokrenite svoj server s SDK beta verzijama:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Uklonite pretpostavke o sesiji i rukovanju; tretirajte svaki zahtjev kao
  samodostatan:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Pošaljite zaglavlja `Mcp-Method` i `Mcp-Name` za sirove HTTP zahtjeve:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Provjerite hardkodirane kodove grešaka (`missing resource` premješten s `-32002` na `-32602`).
- [ ] Označite i planirajte migraciju za zastarjele root-ove, uzorkovanje i
  zapisivanje:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrirajte s eksperimentalnog `2025-11-25` Tasks API-ja:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Pregledajte autorizaciju za OAuth i OpenID Connect pojačanja:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Struktura Dokumentacije

- **Moduli 00-11**: Jezgra sadržaja kurikuluma u sekvencijalnom redoslijedu
- **translations/**: Verzije specifične za jezik (automatizirano generirane, ne uređivati izravno)
- **translated_images/**: Lokalizirane verzije slika (automatizirano generirane)
- **images/**: Izvorne slike i dijagrami

### Izmjene Dokumentacije

1. Uredite samo engleske markdown datoteke u korijenskim direktorijima modula (00-11)
2. Ažurirajte slike u direktoriju `images/` ako je potrebno
3. GitHub Akcija co-op-translator automatski će generirati prijevode
4. Prijevodi se ponovno generiraju pri guranju na glavnu granu

### Rad s Prijevodima

- **Automatizirani Prijevod**: GitHub Actions tok upravlja svim prijevodima
- **NE uređujte ručno** datoteke u direktoriju `translations/`
- Metapodaci prijevoda su ugrađeni u svaku prevedenu datoteku
- Podržani jezici: 48+ jezika uključujući arapski, kineski, francuski, njemački, hindi, japanski, korejski, portugalski, ruski, španjolski i mnoge druge

## Upute za Testiranje

### Validacija Dokumentacije

Budući da je ovo prvenstveno repozitorij dokumentacije, testiranje se fokusira na:

1. **Reviziju Obrasca Poveznica**: Popis Markdown poveznica za pregled

   ```bash
   # Popis Markdown poveznica (revizija obrasca)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validaciju Primjera Koda**: Testirati da se primjeri koda kompajliraju/izvršavaju

   ```bash
   # Navigirajte do određenog uzorka i pokrenite njegove testove
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown Linting**: Provjeriti dosljednost formatiranja

   ```bash
   # Koristite markdownlint ako je potrebno
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testiranje Primjernih Projekata

Svaki primjer za pojedini jezik uključuje vlastiti pristup testiranju:

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

## Smjernice za Stil Koda

### Stil Dokumentacije

- Koristite jasan, pristupačan jezik za početnike
- Uključite primjere koda na više jezika gdje je primjenjivo
- Slijedite najbolje prakse za markdown:
  - Koristite ATX stil zaglavlja (`#` sintaksa)
  - Koristite ograničene blokove koda s oznakama jezika
  - Uključite opisni alt tekst za slike
  - Održavajte razumne duljine redaka (bez stroge granice, ali budite razboriti)

### Stil Primjera Koda

#### TypeScript/JavaScript
- Koristite ES module (`import`/`export`)
- Slijedite TypeScript konvencije strogog moda
- Uključite anotacije tipa
- Ciljajte ES2022

#### Python
- Slijedite smjernice za stil PEP 8
- Koristite pokazivače tipova kada je primjenjivo
- Uključite docstrings za funkcije i klase
- Koristite moderne Python značajke (3.8+)

#### Java
- Slijedite Spring Boot konvencije
- Koristite Java 21 značajke
- Slijedite standardnu Maven strukturu projekta
- Uključite Javadoc komentare

### Organizacija Datoteka

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

## Izgradnja i Implementacija

### Implementacija Dokumentacije

Repozitorij koristi GitHub Pages ili slično za hosting dokumentacije (ako je primjenjivo). Promjene na glavnoj grani pokreću:

1. Tok prevođenja (`.github/workflows/co-op-translator.yml`)
2. Automatizirani prijevod svih engleskih markdown datoteka
3. Lokalizaciju slika po potrebi

### Nije Potreban Proces Izgradnje

Ovaj repozitorij uglavnom sadrži markdown dokumentaciju. Nije potreban nikakav korak kompajlacije ili izgradnje za sadržaj osnovnog kurikuluma.

### Implementacija Primjernog Projekta

Pojedini primjerni projekti mogu imati upute za implementaciju:
- Pogledajte `03-GettingStarted/09-deployment/` za upute o implementaciji MCP servera
- Primjeri implementacije Azure Container Apps u `11-MCPServerHandsOnLabs/`

## Smjernice za Doprinos

### Proces Pull Request-a

1. **Fork i Kloniraj**: Napravite fork repozitorija i klonirajte vaš fork lokalno
2. **Napravite Granu**: Koristite opisne nazive grana (npr. `fix/typo-module-3`, `add/python-example`)
3. **Napravite Izmjene**: Uredite samo engleske markdown datoteke (ne prijevode)
4. **Testirajte Lokalno**: Provjerite pravilno prikazivanje markdowna
5. **Pošaljite PR**: Koristite jasne naslove i opise PR-a
6. **CLA**: Potpišite Microsoft Contributor License Agreement kad se zatraži

### Format Naslova PR-a

Koristite jasne, opisne naslove:
- `[Modul XX] Kratki opis` za promjene vezane uz modul
- `[Primjeri] Opis` za izmjene primjernog koda
- `[Dokumentacija] Opis` za opća ažuriranja dokumentacije

### Što Doprinijeti

- Ispravke pogrešaka u dokumentaciji ili primjerima koda
- Novi primjeri koda na dodatnim jezicima
- Pojašnjenja i poboljšanja postojećeg sadržaja
- Nove studije slučaja ili praktični primjeri
- Prijave problema za nejasan ili netočan sadržaj

### Što NE Raditi

- Nemojte izravno uređivati datoteke u direktoriju `translations/`
- Nemojte uređivati direktorij `translated_images/`
- Nemojte dodavati velike binarne datoteke bez rasprave
- Nemojte mijenjati datoteke za tok prijevoda bez koordinacije

## Dodatne Napomene

### Održavanje Repozitorija

- **Izvještaj Promjena**: Sve značajne promjene su dokumentirane u `changelog.md`
- **Vodič za Učenje**: Koristite `study_guide.md` za pregled navigacije kurikuluma
- **Predlošci za Probleme**: Koristite GitHub predloške za prijave bugova i zahtjeve za značajke
- **Kodeks Ponašanja**: Svi suradnici trebaju slijediti Microsoft Open Source Kodeks Ponašanja

### Put Učenja

Slijedite module u sekvencijalnom redoslijedu (00-11) za optimalno učenje:
1. **00-02**: Osnove (Uvod, Jezgrene Koncepte, Sigurnost)
2. **03**: Početak s praktičnim implementacijama
3. **04-05**: Praktične implementacije i napredne teme
4. **06-10**: Zajednica, najbolje prakse i stvarne primjene
5. **11**: Sveobuhvatne radionice za integraciju baza podataka (13 uzastopnih radionica)

### Resursi za Podršku

- **Dokumentacija**: https://modelcontextprotocol.io/
- **Specifikacija**: https://spec.modelcontextprotocol.io/
- **Zajednica**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord server
- **Povezani Tečajevi**: Pogledajte README.md za druge Microsoft puteve učenja

### Uobičajeni Problemi i Rješenja

**P: Moj PR ne prolazi provjeru prijevoda**
O: Provjerite da ste uređivali samo engleske markdown datoteke u korijenskim direktorijima modula, a ne prevedene verzije.

**P: Kako dodajem novi jezik?**
O: Podršku za jezike upravlja tok co-op-translator. Otvorite issue za raspravu o dodavanju novih jezika.

**P: Primjeri koda ne rade**

A: Provjerite jeste li slijedili upute za postavljanje u README datoteci specifičnog uzorka. Provjerite imate li instalirane ispravne verzije ovisnosti.

**P: Slike se ne prikazuju**
A: Provjerite jesu li putanje do slika relativne i koriste li kosa crta. Slike bi trebale biti u direktoriju `images/` ili `translated_images/` za lokalizirane verzije.

### Razmatranja izvedbe

- Proces prevođenja može trajati nekoliko minuta
- Velike slike treba optimizirati prije predaje
- Održavajte pojedinačne markdown datoteke fokusiranima i umjerene veličine
- Koristite relativne poveznice za bolju prenosivost

### Upravljanje projektom

Ovaj projekt slijedi Microsoftove prakse otvorenog koda:
- MIT licenca za kod i dokumentaciju
- Microsoftov Kodeks ponašanja za otvoreni kod
- Za doprinose je potreban CLA
- Sigurnosni problemi: Slijedite smjernice iz SECURITY.md
- Podrška: Pogledajte SUPPORT.md za izvore pomoći

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->