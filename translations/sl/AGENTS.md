# AGENTS.md

## Pregled projekta

**MCP za začetnike** je odprtokurni izobraževalni kurikulum za učenje Model Context Protocol (MCP) - standardiziranega okvira za interakcije med AI modeli in odjemalskimi aplikacijami. Ta repozitorij ponuja obsežne učne materiale s praktičnimi primeri kode v več programskih jezikih.

### Ključne tehnologije

- **Programski jeziki**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Okviri in SDK-ji**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Baze podatkov**: PostgreSQL z razširitvijo pgvector
- **Oblačne platforme**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Orodja za gradnjo**: npm, Maven, pip, Cargo
- **Dokumentacija**: Markdown z avtomatiziranim večjezičnim prevodom (več kot 48 jezikov)

### Arhitektura

- **11 jedrnih modulov (00-11)**: zaporedna učna pot od osnov do naprednih tem
- **Praktične vaje**: praktične naloge s popolno rešitvijo kode v več jezikih
- **Vzorec projektov**: delujoče implementacije MCP strežnika in odjemalca
- **Sistem prevajanja**: avtomatiziran potek dela prek GitHub Actions za podporo več jezikom
- **Slikovni viri**: centralizirana mapa slik z prevedenimi različicami

## Ukazi za nastavitev

Ta repozitorij je osredotočen na dokumentacijo. Večina nastavitev poteka znotraj posameznih vzorčnih projektov in vaj.

### Nastavitev repozitorija

```bash
# Klonirajte repozitorij
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Delo z vzorčnimi projekti

Vzorčni projekti so locirani v:
- `03-GettingStarted/samples/` - primeri za posamezne jezike
- `03-GettingStarted/01-first-server/solution/` - prve strežniške implementacije
- `03-GettingStarted/02-client/solution/` - odjemalske implementacije
- `11-MCPServerHandsOnLabs/` - obsežne vaje za integracijo baz podatkov

Vsak vzorčni projekt vsebuje navodila za nastavitev:

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
# ali
pip install -e .
python main.py
```

#### Projekti Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Razvojni potek

### Pripravljenost MCP 7-28

#### Kontrolni seznam pripravljenosti repozitorija

- [x] **Jasnost za nove prispevke**: ta datoteka opredeljuje namen repozitorija,
  strukturo, pravila prispevkov in poti za nastavitev vzorcev.
- [x] **Ukazi za gradnjo/testiranje/lint z natančnimi zastavicami**:
  - Lint dokumentacije repozitorija:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Pregled vzorca povezav dokumentacije:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validacija vzorca TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validacija vzorca Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validacija vzorca Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Ena realistična delovna poteza, ki lahko postane MCP orodje**:
  `validate_curriculum_change`
- [x] **Vhodi/izhodi so eksplicitni** (glej specifikacijo spodaj).
- [x] **Dovoljenja in načini napak so dokumentirani** (glej specifikacijo spodaj).
- [x] **Testabilnost CI je jasna** (deterministični ukazi, eksplicitni
  izhodni kodi in strojno berljivi izhodi).

#### Kandidat za MCP orodje delovni potek: `validate_curriculum_change`

##### Cilj

Validirati spremembe v dokumentaciji kurikuluma in zdravstveno stanje reprezentativne vzorčne kode
pred združitvijo.

##### Vhodi

- `changed_paths: string[]` (zahtevano) - relativne poti, spremenjene v PR.
- `run_docs_lint: boolean` (privzeto `true`)
- `run_links_audit: boolean` (privzeto `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (privzeto vsi `false`)

##### Izhodi

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Dovoljenja

- Branje datotek delovnega prostora in pisanje artefaktov, ki jih ustvari orodje (npr. poročila o lintu,
  dnevniške datoteke testov) le; brez zapisov v `translations/` ali
  `translated_images/`.
- Izvajanje lokalnih ukazov shell.
- Izbiren dostop do mreže samo za obnovitev paketov (`npm ci`,
  `python -m pip install`, reševanje odvisnosti `mvn`).
- Ni dovoljenja za push, merge ali spreminjanje `translations/` ali
  `translated_images/`.

##### Načini napak

- `E_NO_INPUT_PATHS`: `changed_paths` prazen.
- `E_INVALID_PATH`: vhodna pot beži iz korena repozitorija.
- `E_LINT_FAILED`: lint markdowna se zaključi z nenicelno kodo.
- `E_LINK_AUDIT_FAILED`: ukaz za pregled povezav se zaključi z nenicelno kodo.
- `E_SAMPLE_TEST_FAILED`: testiranje/gradnja vzorca se zaključi z nenicelno kodo.
- `E_TIMEOUT`: ukaz je presegel nastavljeni časovni limit.

##### Priporočena pogodba CI

Za avtomatizacijo validacije nastavite CI opravek, ki:

- Sproži ob pull requestih, ki se dotikajo `*.md`, vzorčne kode ali te datoteke.
- Izvede zgoraj navedene natančne ukaze.
- Shrani dnevnike kot artefakte.
- Neuspeh opravka ob kateri koli nenicelni izhodni kodi.

#### Če omogočite MCP strežnik iz tega repozitorija

- [ ] Preberite osnutek zapisnika sprememb za MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Preverite vaš strežnik z SDK betami:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Odstranite domneve o sejah in stiskanju rok; vsak zahtevek obdelujte kot
  samostojen:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Pošljite glave `Mcp-Method` in `Mcp-Name` za surove HTTP zahteve:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Preglejte trdo kodirane kode napak (`missing resource` je bil prestavljen iz `-32002` v `-32602`).

- [ ] Označi in načrtuj migracijo za zastarele korenine, vzorčenje in
  beleženje:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migriraj s poskusnega `2025-11-25` Tasks API:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Preglej avtorizacijo za ojačitev OAuth in OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Struktura dokumentacije

- **Moduli 00-11**: Jedrna vsebina učnega načrta v zaporednem vrstnem redu
- **translations/**: Jezikovno specifične različice (samodejno generirane, ne urejajte neposredno)
- **translated_images/**: Lokalizirane različice slik (samodejno generirane)
- **images/**: Izvorne slike in diagrami

### Spreminjanje dokumentacije

1. Urejajte samo angleške markdown datoteke v korenskih modulnih imenikih (00-11)
2. Po potrebi posodobite slike v imeniku `images/`
3. GitHub Action co-op-translator bo samodejno generiral prevode
4. Prevajanja se ponovno ustvarjajo ob potisku v glavno vejo

### Delo s prevodi

- **Samodejni prevod**: Potek dela GitHub Actions upravlja vse prevode
- **Ne urejajte ročno** datotek v imeniku `translations/`
- Metapodatki prevajanja so vključeni v vsako prevedeno datoteko
- Podprti jeziki: več kot 48 jezikov, vključno z arabščino, kitajščino, francoščino, nemščino, hindijščino, japonščino, korejščino, portugalščino, ruščino, španščino in mnogimi več

## Navodila za testiranje

### Validacija dokumentacije

Ker gre pretežno za repozitorij dokumentacije, testi zajemajo:

1. **Pregled vzorcev povezav**: Seznam povezav Markdown za pregled

   ```bash
   # Naštej Markdown povezave (preverjanje vzorca)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validacija primerov kode**: Testiranje, da primeri kode uspešno sestavijo/izvedejo

   ```bash
   # Pomaknite se do določenega vzorca in zaženite njegove teste
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Preverjanje sintakse Markdown**: Preverjanje skladnosti oblikovanja

   ```bash
   # Uporabite markdownlint, če je potrebno
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testiranje vzorčnega projekta

Vsak jezikovno specifični vzorec vključuje svoj pristop k testiranju:

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

## Smernice stila kode

### Stil dokumentacije

- Uporabljajte jasen jezik, prijazen začetnikom
- Vključite primere kode v več jezikih kjer je primerno
- Upoštevajte najboljše prakse za markdown:
  - Uporabljajte naslove v slogu ATX (`#` sintaksa)
  - Uporabljajte ograjene bloke kode z označbami jezika
  - Vključite opisni nadomestni tekst za slike
  - Ohranjajte razumne dolžine vrstic (ni stroge omejitve, a bodite razumni)

### Stil primerov kode

#### TypeScript/JavaScript
- Uporabljajte ES module (`import`/`export`)
- Upoštevajte stroge konvencije TypeScript-a
- Vključite oznake tipov
- Ciljajte ES2022

#### Python
- Upoštevajte smernice stila PEP 8
- Uporabljajte tipizirane namige kjer je primerno
- Vključite docstringe za funkcije in razrede
- Uporabljajte sodobne Python funkcije (3.8+)

#### Java
- Upoštevajte konvencije Spring Boot
- Uporabljajte funkcije Java 21
- Sledite standardni strukturi Maven projektov
- Vključite Javadoc komentarje

### Organizacija datotek

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

## Gradnja in nameščanje

### Namestitev dokumentacije

Repozitorij uporablja GitHub Pages ali podobno za gostovanje dokumentacije (če je primerno). Spremembe v glavni veji sprožijo:

1. Potek dela prevajanja (`.github/workflows/co-op-translator.yml`)
2. Samodejni prevod vseh angleških markdown datotek
3. Lokalizacijo slik po potrebi

### Ni potrebno graditi

Ta repozitorij vsebuje pretežno markdown dokumentacijo. Za jedrno vsebino učnega načrta ni potrebna kompilacija ali gradnja.

### Namestitev vzorčnih projektov

Posamezni vzorčni projekti imajo lahko navodila za nameščanje:
- Glej `03-GettingStarted/09-deployment/` za usmeritve za namestitev strežnika MCP
- Primeri namestitve Azure Container Apps v `11-MCPServerHandsOnLabs/`

## Smernice prispevkov

### Postopek za Pull Request

1. **Fork in Kloniranje**: Naredite fork repozitorija in klonirajte vaš fork lokalno
2. **Ustvarite vejo**: Uporabljajte opisna imena vej (npr. `fix/typo-module-3`, `add/python-example`)
3. **Naredite spremembe**: Urejajte samo angleške markdown datoteke (ne prevedene)
4. **Testirajte lokalno**: Preverite, da markdown pravilno upodablja vsebino
5. **Oddajte PR**: Uporabljajte jasne naslove in opise PR-jev
6. **CLA**: Podpišite Microsoft Contributor License Agreement, ko ste pozvani

### Oblika naslova PR-ja

Uporabljajte jasne, opisne naslove:
- `[Module XX] Kratek opis` za modulsko specifične spremembe
- `[Samples] Opis` za spremembe vzorčne kode
- `[Docs] Opis` za splošne posodobitve dokumentacije

### Kaj prispevati

- Popravki napak v dokumentaciji ali primerih kode
- Novi primeri kode v dodatnih jezikih
- Pojasnila in izboljšave obstoječe vsebine
- Novi primeri primerov ali študij primerov
- Poročila o težavah glede nejasne ali napačne vsebine

### Česa NE delati

- Ne urejajte neposredno datotek v imeniku `translations/`
- Ne urejajte imenika `translated_images/`
- Ne dodajajte velikih binarnih datotek brez predhodnih pogovorov
- Ne spreminjajte datotek potekov prevajanja brez koordinacije

## Dodatne opombe

### Vzdrževanje repozitorija

- **Zapis sprememb**: Vse pomembne spremembe so dokumentirane v `changelog.md`
- **Vodnik za študij**: Uporabite `study_guide.md` za pregled navigacije po učnem načrtu
- **Predloge za težave**: Uporabite GitHub predloge za prijavo napak in zahtev funkcij
- **Kodeks vedenja**: Vsi sodelujoči morajo slediti Microsoftovemu kodeksu vedenja za odprto kodo

### Pot učenja

Sledite modulom zaporedno (00-11) za optimalno učenje:
1. **00-02**: Osnove (Uvod, jedrne koncepte, varnost)
2. **03**: Začetek z aktivno implementacijo
3. **04-05**: Praktična implementacija in napredne teme
4. **06-10**: Skupnost, najboljše prakse in aplikacije v resničnem svetu
5. **11**: Celovite laboratorijske vaje za integracijo podatkovnih baz (13 zaporednih vaj)

### Viri podpore

- **Dokumentacija**: https://modelcontextprotocol.io/
- **Specifikacija**: https://spec.modelcontextprotocol.io/
- **Skupnost**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord strežnik
- **Sorodni tečaji**: Glejte README.md za ostale Microsoft učne poti

### Pogoste težave

**V: Moj PR ne uspe pri preverjanju prevoda**
O: Prepričajte se, da ste urejali samo angleške markdown datoteke v korenskih modulnih imenikih, ne prevedenih verzij.

**V: Kako dodam nov jezik?**
O: Podporo jezikom upravlja potek dela co-op-translator. Odprite težavo za pogovor o dodajanju novih jezikov.

**V: Primeri kode ne delujejo**

A: Prepričajte se, da ste sledili navodilom za namestitev v README za določen primer. Preverite, da imate nameščene pravilne različice odvisnosti.

**V: Slike se ne prikazujejo**
A: Preverite, da so poti do slik relativne in uporabljajo poševnice naprej. Slike morajo biti v mapi `images/` ali `translated_images/` za lokalizirane različice.

### Premisleki glede uspešnosti

- Postopek prevajanja lahko traja več minut
- Velike slike je treba optimizirati pred potrditvijo sprememb
- Posamične markdown datoteke naj bodo osredotočene in razumno velike
- Uporabljajte relativne povezave za boljšo prenosljivost

### Upravljanje projekta

Ta projekt sledi Microsoftovim praksam odprte kode:
- MIT licenca za kodo in dokumentacijo
- Microsoftov kodeks ravnanja za odprto kodo
- Za prispevke je potrebna podpisana pogodba o prispevku (CLA)
- Varnostna vprašanja: Sledite smernicam v SECURITY.md
- Podpora: Glejte SUPPORT.md za vire pomoči

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->