# AGENTS.md

## Pregled projekta

**MCP za začetnike** je odprtokurri edukativni načrt za učenje Model Context Protocol (MCP) - standardiziran okvir za interakcije med AI modeli in odjemalskimi aplikacijami. Ta repozitorij zagotavlja obsežne učne materiale s praktičnimi primeri kode v več programskih jezikih.

### Ključne tehnologije

- **Programski jeziki**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Okviri in SDK-ji**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Podatkovne zbirke**: PostgreSQL z razširitvijo pgvector
- **Oblačne platforme**: Azure (Container Apps, OpenAI, Varnost vsebin, Application Insights)
- **Orodja za gradnjo**: npm, Maven, pip, Cargo
- **Dokumentacija**: Markdown z avtomatiziranim prevajanjem v več jezikov (več kot 48 jezikov)

### Arhitektura

- **11 osnovnih modulov (00-11)**: Zaporedna učna pot od osnov do naprednih tem
- **Praktične delavnice**: Praktične vaje s popolnimi rešitvami v več jezikih
- **Vzorec projektov**: Delujoče implementacije MCP strežnika in odjemalca
- **Sistem prevajanja**: Avtomatiziran GitHub Actions potek za podporo več jezikov
- **Slike**: Centralizirani imenik slik z prevedenimi različicami

## Ukazi za namestitev

To je repozitorij osredotočen na dokumentacijo. Večina nastavitev poteka znotraj posameznih vzorčnih projektov in delavnic.

### Nastavitev repozitorija

```bash
# Klonirajte repozitorij
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Delo z vzorčnimi projekti

Vzorčni projekti so locirani v:
- `03-GettingStarted/samples/` - Primeri po posameznih jezikih
- `03-GettingStarted/01-first-server/solution/` - Prve implementacije strežnika
- `03-GettingStarted/02-client/solution/` - Implementacije odjemalcev
- `11-MCPServerHandsOnLabs/` - Celovite delavnice z integracijo podatkovnih zbirk

Vsak vzorčni projekt vsebuje lastna navodila za nastavitev:

#### Projekti v TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Projekti v Pythonu
```bash
cd <project-directory>
pip install -r requirements.txt
# ali
pip install -e .
python main.py
```

#### Projekti v Javi
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Razvojni potek

### Priprava MCP 7-28

#### Kontrolni seznam pripravljenosti repozitorija

- [x] **Jasnost za nove prispevke**: Ta datoteka določa namen repozitorija,
  strukturo, pravila prispevkov in poti za nastavitev vzorcev.
- [x] **Ukazi za gradnjo/testiranje/lint z natančnimi zastavicami**:
  - Lint dokumentacije repozitorija:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Pregled vzorca povezav v dokumentaciji:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validacija vzorca v TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validacija vzorca v Pythonu:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validacija vzorca v Javi:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Eden realističen potek dela, ki lahko postane MCP orodje**:
  `validate_curriculum_change`
- [x] **Vhodi/izhodi so izrecni** (glej specifikacijo spodaj).
- [x] **Dovoljenja in načini za neuspeh so dokumentirani** (glej specifikacijo spodaj).
- [x] **Testabilnost v CI je izrecna** (deterministični ukazi, izrecne
  izhodne kode in za stroj berljivi izhodi).

#### Kandidat za MCP orodje poteka dela: `validate_curriculum_change`

##### Cilj

Validacija sprememb kurikuluma in splošno zdravje predstavitvene kode
pred združitvijo.

##### Vhodi

- `changed_paths: string[]` (obvezno) - relativne poti spremenjene v PR.
- `run_docs_lint: boolean` (privzeto `true`)
- `run_links_audit: boolean` (privzeto `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (privzeto vse `false`)

##### Izhodi

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Dovoljenja

- Branje datotek delovnega prostora in zapis orodjem ustvarjenih artefaktov (npr., poročila linterja,
  dnevniki testov) samo; brez zapisovanja v `translations/` ali
  `translated_images/`.
- Izvajanje lokalnih ukazov v shellu.
- Omrežni dostop je dovoljen samo za obnovitev paketov (`npm ci`,
  `python -m pip install`, reševanje odvisnosti `mvn`).
- Brez dovoljenja za potiskanje, združevanje ali spreminjanje `translations/` ali
  `translated_images/`.

##### Načini neuspeha

- `E_NO_INPUT_PATHS`: `changed_paths` je prazen.
- `E_INVALID_PATH`: vhodna pot izhaja izven korena repozitorija.
- `E_LINT_FAILED`: markdown lint se zaključi z napako.
- `E_LINK_AUDIT_FAILED`: ukaz pregleda povezav se zaključi z napako.
- `E_SAMPLE_TEST_FAILED`: test/gradnja vzorca se zaključi z napako.
- `E_TIMEOUT`: ukaz je presegel nastavljeni časovni limit.

##### Priporočena pogodba za CI

Za avtomatizacijo validacije konfigurirajte CI opravilo, ki:

- Zažene ob pull requestih, ki posegajo v `*.md`, vzorčno kodo ali to datoteko.
- Izvede natančno zgoraj navedene ukaze.
- Shrani dnevnike kot artefakte.
- Opravilo se označi kot neuspešno ob kateri koli ne-nični izhodni kodi.

#### Če iz tega repozitorija izpeljete MCP strežnik

- [ ] Preberite končni MCP `2026-07-28` dnevnik sprememb:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Preverite, da izbrana izdaja SDK podpira MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Odstranite predpostavke seje in potrditve; obravnavajte vsak zahtevek kot
  samostojen:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Pošljite glavi `Mcp-Method` in `Mcp-Name` za surove HTTP zahtevke:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Preglejte trdo kodirane kode napak (`missing resource` premaknjena iz `-32002` na `-32602`).

- [ ] Migrirajte zastarele korenine, vzorčenje, beleženje in dinamično registracijo odjemalcev
  Registracija:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Prestavite s preizkusnega API-ja opravil `2025-11-25`:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Pregled avtorizacije za okrepitev OAuth in OpenID Connect:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Struktura dokumentacije

- **Moduli 00-11**: Vsebina osnovnega kurikuluma v zaporednem vrstnem redu
- **translations/**: Jezikovno specifične različice (samodejno ustvarjene, ne urejajte neposredno)
- **translated_images/**: Lokalizirane različice slik (samodejno ustvarjene)
- **images/**: Izvorne slike in diagrami

### Spreminjanje dokumentacije

1. Urejajte samo angleške markdown datoteke v korenskih modulnih imenikih (00-11)
2. Po potrebi posodobite slike v imeniku `images/`
3. GitHub Action co-op-translator bo samodejno ustvaril prevode
4. Prevodi se samodejno regenerirajo ob pushu v glavno vejo

### Delo s prevodi

- **Samodejni prevod**: delovni tok GitHub Actions upravlja vse prevode
- **Ne urejajte ročno** datotek v imeniku `translations/`
- Metapodatki prevodov so vgrajeni v vsako prevedeno datoteko
- Podprti jeziki: več kot 48 jezikov, vključno z arabščino, kitajščino, francoščino, nemščino, hindijščino, japonščino, korejščino, portugalščino, ruščino, španščino in mnogimi drugimi

## Navodila za testiranje

### Preverjanje dokumentacije

Ker gre predvsem za repozitorij dokumentacije, se testiranje osredotoča na:

1. **Pregled povezav**: Izpiši Markdown povezave za pregled

   ```bash
   # Naštej Markdown povezave (revizija vzorcev)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Preverjanje vzorcev kode**: Preverite, da se primeri kode sestavijo/izvedejo

   ```bash
   # Pomaknite se do določenega vzorca in zaženite njegove teste
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Lintanje Markdowna**: Preverite skladnost oblikovanja

   ```bash
   # Po potrebi uporabite markdownlint
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testiranje vzorčnega projekta

Vsak jezikovno specifični vzorec vključuje lasten pristop k testiranju:

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

## Smernice za slog kode

### Slog dokumentacije

- Uporabljajte jasno, začetnikom prijazno jezikovno obliko
- Vključite primere kode v več jezikih, kjer je primerno
- Upoštevajte najboljše prakse za markdown:
  - Uporabljajte naslove v ATX slogu (`#` sintaksa)
  - Uporabljajte ograjene bloke kode z označbami jezika
  - Vključite opisne alt tekste za slike
  - Ohranite razumne dolžine vrstic (brez stroge meje, a bodite razumni)

### Slog vzorcev kode

#### TypeScript/JavaScript
- Uporabljajte ES module (`import`/`export`)
- Upoštevajte stroge konvencije TypeScript načina
- Vključite tipne anotacije
- Ciljajte ES2022

#### Python
- Upoštevajte smernice sloga PEP 8
- Uporabite namige za tipe, kjer je primerno
- Vključite docstringe za funkcije in razrede
- Uporabljajte sodobne funkcionalnosti Pythona (3.8+)

#### Java
- Upoštevajte konvencije Spring Boot
- Uporabljajte funkcije Java 21
- Sledite standardni strukturi Maven projekta
- Vključite komentarje Javadoc

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

## Gradnja in uvajanje

### Uvajanje dokumentacije

Repozitorij uporablja GitHub Pages ali podoben sistem za gostovanje dokumentacije (če je primerno). Spremembe v glavni veji sprožijo:

1. Delovni tok prevajanja (`.github/workflows/co-op-translator.yml`)
2. Samodejni prevod vseh angleških markdown datotek
3. Lokalizacijo slik po potrebi

### Ni potrebnega gradbenega postopka

Ta repozitorij vsebuje predvsem markdown dokumentacijo. Za vsebino osnovnega kurikuluma ni potrebna sestava ali gradnja.

### Uvajanje vzorčnega projekta

Posamezni vzorčni projekti morda imajo navodila za uvajanje:
- Glejte `03-GettingStarted/09-deployment/` za navodila za uvajanje MCP strežnika
- Primeri uvajanja Azure Container Apps v `11-MCPServerHandsOnLabs/`

## Smernice za prispevanje

### Postopek pull requesta

1. **Fork in kloniranje**: naredite fork repozitorija in lokalno klonirajte svoj fork
2. **Ustvarite vejo**: uporabite opisna imena vej (npr. `fix/typo-module-3`, `add/python-example`)
3. **Naredite spremembe**: uredite samo angleške markdown datoteke (ne prevode)
4. **Testirajte lokalno**: preverite pravilno upodabljanje markdowna
5. **Pošljite PR**: uporabite jasne naslove in opise PR-jev
6. **CLA**: podpišite Microsoft Contributor License Agreement, ko se od vas zahteva

### Format naslova PR

Uporabljajte jasne, opisne naslove:
- `[Module XX] Kratek opis` za spremembe, specifične za modul
- `[Samples] Opis` za spremembe primerov kode
- `[Docs] Opis` za splošne posodobitve dokumentacije

### Kaj prispevati

- Popravki napak v dokumentaciji ali primerih kode
- Novi primeri kode v dodatnih jezikih
- Razjasnitve in izboljšave obstoječe vsebine
- Novi primeri študij primerov ali praktični primeri
- Poročila o težavah zaradi nejasne ali napačne vsebine

### Česa NE početi

- Ne urejajte neposredno datotek v imeniku `translations/`
- Ne urejajte imenika `translated_images/`
- Ne dodajajte velikih binarnih datotek brez usklajevanja
- Ne spreminjajte datotek delovnega toka prevajanja brez koordinacije

## Dodatne opombe

### Vzdrževanje repozitorija

- **Dnevnik sprememb**: Vse pomembne spremembe so dokumentirane v `changelog.md`
- **Vodnik za študij**: uporabite `study_guide.md` za pregled navigacije po kurikulumu
- **Predloge za vprašanja**: uporabite GitHub predloge za poročila o napakah in zahteve za funkcije
- **Kodeks vedenja**: vsi sodelujoči morajo upoštevati Microsoft Open Source kodeks vedenja

### Učilna pot

Sledite modulom v zaporednem vrstnem redu (00-11) za optimalno učenje:
1. **00-02**: Osnove (Uvod, osnovni koncepti, varnost)
2. **03**: Začetek s praktično implementacijo
3. **04-05**: Praktična implementacija in napredne teme
4. **06-10**: Skupnost, najboljše prakse in aplikacije v resničnem svetu
5. **11**: Celoviti laboratoriji za integracijo podatkovnih baz (13 zaporednih laboratorijev)

### Podporni viri

- **Dokumentacija**: https://modelcontextprotocol.io/
- **Specifikacija**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Skupnost**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord strežnik
- **Sorodni tečaji**: glejte README.md za ostale Microsoft učne poti

### Pogoste težave in reševanje

**V: Moj PR ne prestane preverjanja prevoda**
O: Preverite, da ste uredili samo angleške markdown datoteke v korenskih modulnih imenikih, ne prevedene različice.

**V: Kako dodam nov jezik?**
O: Podporo jezikov upravlja delovni tok co-op-translator. Odprite vprašanje za razpravo o dodajanju novih jezikov.

**V: Primeri kode ne delujejo**
O: Preverite, da ste sledili navodilom za nastavitev v README-ju specifičnega vzorca. Preverite, da imate nameščene pravilne različice odvisnosti.


**V: Slike se ne prikazujejo** 

A: Preverite, ali so poti do slik relativne in uporabljajo poševnice naprej. Slike naj bodo v imeniku `images/` ali `translated_images/` za lokalizirane različice.

### Premisleki glede zmogljivosti

- Prevodni potek lahko traja več minut
- Velike slike je treba pred potrditvijo optimizirati
- Posamezne markdown datoteke naj bodo osredotočene in razmeroma velike
- Uporabljajte relativne povezave za boljšo prenosljivost

### Vodenje projekta

Ta projekt sledi Microsoftovim praksam odprte kode:
- Licenca MIT za kodo in dokumentacijo
- Microsoftova Kodeks ravnanja odprte kode
- Za prispevke je potreben CLA
- Varnostni problemi: upoštevajte smernice iz SECURITY.md
- Podpora: glejte SUPPORT.md za vire pomoči

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->