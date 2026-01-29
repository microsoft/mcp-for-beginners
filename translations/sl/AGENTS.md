# AGENTS.md

## Pregled projekta

**MCP za začetnike** je odprtokodni izobraževalni program za učenje Model Context Protocol (MCP) - standardiziranega okvira za interakcije med modeli umetne inteligence in odjemalskimi aplikacijami. Ta repozitorij ponuja obsežne učne materiale z praktičnimi primeri kode v več programskih jezikih.

### Ključne tehnologije

- **Programski jeziki**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Okviri in SDK-ji**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Podatkovne baze**: PostgreSQL z razširitvijo pgvector
- **Oblačne platforme**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Orodja za gradnjo**: npm, Maven, pip, Cargo
- **Dokumentacija**: Markdown z avtomatiziranim prevajanjem v več jezikov (48+ jezikov)

### Arhitektura

- **11 osnovnih modulov (00-11)**: Zaporedna učna pot od osnov do naprednih tem
- **Praktične delavnice**: Praktične vaje s popolnimi rešitvami kode v več jezikih
- **Vzorčni projekti**: Delujoče implementacije MCP strežnika in odjemalca
- **Sistem za prevajanje**: Avtomatiziran GitHub Actions potek dela za podporo več jezikom
- **Slikovni viri**: Centraliziran imenik slik z prevedenimi različicami

## Ukazi za nastavitev

To je repozitorij, osredotočen na dokumentacijo. Večina nastavitev se izvaja znotraj posameznih vzorčnih projektov in delavnic.

### Nastavitev repozitorija

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Delo z vzorčnimi projekti

Vzorčni projekti se nahajajo v:
- `03-GettingStarted/samples/` - Jezikovno specifični primeri
- `03-GettingStarted/01-first-server/solution/` - Prve implementacije strežnika
- `03-GettingStarted/02-client/solution/` - Implementacije odjemalca
- `11-MCPServerHandsOnLabs/` - Obsežne delavnice za integracijo podatkovnih baz

Vsak vzorčni projekt vsebuje lastna navodila za nastavitev:

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
# or
pip install -e .
python main.py
```

#### Projekti Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Delovni proces razvoja

### Struktura dokumentacije

- **Moduli 00-11**: Osnovna vsebina učnega programa v zaporednem vrstnem redu
- **translations/**: Jezikovno specifične različice (avtomatsko generirane, ne urejajte neposredno)
- **translated_images/**: Lokalizirane različice slik (avtomatsko generirane)
- **images/**: Izvorne slike in diagrami

### Spreminjanje dokumentacije

1. Urejajte samo angleške markdown datoteke v korenskih imenikih modulov (00-11)
2. Po potrebi posodobite slike v imeniku `images/`
3. GitHub Action co-op-translator bo samodejno generiral prevode
4. Prevodi se regenerirajo ob potisku na glavno vejo

### Delo s prevodi

- **Avtomatizirano prevajanje**: GitHub Actions potek dela obravnava vse prevode
- **NE urejajte ročno** datotek v imeniku `translations/`
- Metapodatki prevodov so vgrajeni v vsako prevedeno datoteko
- Podprti jeziki: 48+ jezikov, vključno z arabščino, kitajščino, francoščino, nemščino, hindijščino, japonščino, korejščino, portugalščino, ruščino, španščino in mnogimi drugimi

## Navodila za testiranje

### Validacija dokumentacije

Ker je to predvsem repozitorij dokumentacije, testiranje vključuje:

1. **Validacija povezav**: Preverite, ali vse notranje povezave delujejo
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Validacija vzorcev kode**: Preverite, ali se vzorci kode prevedejo/izvedejo
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Linting Markdown**: Preverite skladnost formatiranja
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Testiranje vzorčnih projektov

Vsak jezikovno specifičen vzorec vključuje svoj pristop k testiranju:

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

- Uporabljajte jasen, začetnikom prijazen jezik
- Vključite primere kode v več jezikih, kjer je to primerno
- Upoštevajte najboljše prakse za markdown:
  - Uporabljajte glave v slogu ATX (`#` sintaksa)
  - Uporabljajte omejene bloke kode z identifikatorji jezika
  - Vključite opisni alt tekst za slike
  - Ohranjajte razumno dolžino vrstic (brez stroge omejitve, vendar bodite smiselni)

### Slog vzorcev kode

#### TypeScript/JavaScript
- Uporabljajte ES module (`import`/`export`)
- Upoštevajte stroge konvencije TypeScript
- Vključite anotacije tipov
- Ciljajte ES2022

#### Python
- Upoštevajte smernice sloga PEP 8
- Uporabljajte namige tipov, kjer je to primerno
- Vključite docstring za funkcije in razrede
- Uporabljajte sodobne funkcije Python (3.8+)

#### Java
- Upoštevajte konvencije Spring Boot
- Uporabljajte funkcije Java 21
- Upoštevajte standardno strukturo projektov Maven
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

Repozitorij uporablja GitHub Pages ali podobno za gostovanje dokumentacije (če je primerno). Spremembe v glavni veji sprožijo:

1. Potek prevajanja (`.github/workflows/co-op-translator.yml`)
2. Avtomatizirano prevajanje vseh angleških markdown datotek
3. Lokalizacija slik po potrebi

### Gradnja ni potrebna

Ta repozitorij primarno vsebuje markdown dokumentacijo. Za osnovno vsebino učnega programa ni potrebna nobena kompilacija ali korak gradnje.

### Uvajanje vzorčnih projektov

Posamezni vzorčni projekti lahko vsebujejo navodila za uvajanje:
- Glejte `03-GettingStarted/09-deployment/` za navodila za uvajanje MCP strežnika
- Primeri uvajanja Azure Container Apps v `11-MCPServerHandsOnLabs/`

## Smernice za prispevanje

### Postopek za Pull Request

1. **Fork in kloniranje**: Forkajte repozitorij in klonirajte svoj fork lokalno
2. **Ustvarite vejo**: Uporabljajte opisna imena vej (npr. `fix/typo-module-3`, `add/python-example`)
3. **Naredite spremembe**: Urejajte samo angleške markdown datoteke (ne prevodov)
4. **Testirajte lokalno**: Preverite, ali se markdown pravilno prikazuje
5. **Oddajte PR**: Uporabljajte jasne naslove in opise PR
6. **CLA**: Podpišite Microsoft Contributor License Agreement, ko vas pozove

### Format naslova PR

Uporabljajte jasne, opisne naslove:
- `[Module XX] Kratek opis` za spremembe, specifične za module
- `[Samples] Opis` za spremembe vzorčne kode
- `[Docs] Opis` za splošne posodobitve dokumentacije

### Kaj prispevati

- Popravki napak v dokumentaciji ali vzorcih kode
- Novi primeri kode v dodatnih jezikih
- Pojasnila in izboljšave obstoječe vsebine
- Nove študije primerov ali praktični primeri
- Poročila o težavah za nejasno ali napačno vsebino

### Kaj NE storiti

- Ne urejajte neposredno datotek v imeniku `translations/`
- Ne urejajte imenika `translated_images/`
- Ne dodajajte velikih binarnih datotek brez razprave
- Ne spreminjajte datotek poteka prevajanja brez usklajevanja

## Dodatne opombe

### Vzdrževanje repozitorija

- **Changelog**: Vse pomembne spremembe so dokumentirane v `changelog.md`
- **Študijski vodič**: Uporabite `study_guide.md` za pregled navigacije po učnem programu
- **Predloge za težave**: Uporabite predloge GitHub za poročila o napakah in zahteve za funkcije
- **Kodeks ravnanja**: Vsi prispevki morajo upoštevati Microsoft Open Source Code of Conduct

### Učna pot

Sledite modulom v zaporednem vrstnem redu (00-11) za optimalno učenje:
1. **00-02**: Osnove (Uvod, osnovni koncepti, varnost)
2. **03**: Začetek z praktično implementacijo
3. **04-05**: Praktična implementacija in napredne teme
4. **06-10**: Skupnost, najboljše prakse in aplikacije v resničnem svetu
5. **11**: Obsežne delavnice za integracijo podatkovnih baz (13 zaporednih delavnic)

### Viri podpore

- **Dokumentacija**: https://modelcontextprotocol.io/
- **Specifikacija**: https://spec.modelcontextprotocol.io/
- **Skupnost**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord strežnik
- **Povezani tečaji**: Glejte README.md za druge učne poti Microsofta

### Pogoste težave

**V: Moj PR ne uspe pri preverjanju prevoda**
O: Prepričajte se, da ste urejali samo angleške markdown datoteke v korenskih imenikih modulov, ne prevedenih različic.

**V: Kako dodam nov jezik?**
O: Podpora za jezike se upravlja prek poteka dela co-op-translator. Odprite težavo za razpravo o dodajanju novih jezikov.

**V: Vzorci kode ne delujejo**
O: Prepričajte se, da ste sledili navodilom za nastavitev v specifičnem README vzorca. Preverite, ali imate nameščene pravilne različice odvisnosti.

**V: Slike se ne prikazujejo**
O: Preverite, ali so poti slik relativne in uporabljajo poševnice. Slike morajo biti v imeniku `images/` ali `translated_images/` za lokalizirane različice.

### Premisleki o zmogljivosti

- Potek prevajanja lahko traja več minut
- Velike slike je treba optimizirati pred potrditvijo
- Posamezne markdown datoteke naj bodo osredotočene in razumno velike
- Uporabljajte relativne povezave za boljšo prenosljivost

### Upravljanje projekta

Ta projekt sledi praksam odprte kode Microsofta:
- MIT licenca za kodo in dokumentacijo
- Microsoft Open Source Code of Conduct
- CLA zahtevan za prispevke
- Varnostne težave: Sledite smernicam v SECURITY.md
- Podpora: Glejte SUPPORT.md za vire pomoči

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.