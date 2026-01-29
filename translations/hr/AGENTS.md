# AGENTS.md

## Pregled projekta

**MCP za početnike** je otvoreni edukacijski kurikulum za učenje Model Context Protocol (MCP) - standardiziranog okvira za interakcije između AI modela i klijentskih aplikacija. Ovaj repozitorij pruža sveobuhvatne materijale za učenje s praktičnim primjerima koda u više programskih jezika.

### Ključne tehnologije

- **Programski jezici**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Okviri i SDK-ovi**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Baze podataka**: PostgreSQL s pgvector ekstenzijom
- **Cloud platforme**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Alati za izgradnju**: npm, Maven, pip, Cargo
- **Dokumentacija**: Markdown s automatskim prijevodom na više jezika (48+ jezika)

### Arhitektura

- **11 osnovnih modula (00-11)**: Sekvencijalni put učenja od osnova do naprednih tema
- **Praktične radionice**: Vježbe s kompletnim rješenjima koda u više jezika
- **Primjerni projekti**: Funkcionalne implementacije MCP servera i klijenta
- **Sustav za prijevod**: Automatski GitHub Actions tijek rada za podršku više jezika
- **Slike**: Centralizirani direktorij slika s prevedenim verzijama

## Postavljanje repozitorija

Ovo je repozitorij fokusiran na dokumentaciju. Većina postavljanja odvija se unutar pojedinačnih primjernih projekata i radionica.

### Postavljanje repozitorija

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Rad s primjernim projektima

Primjerni projekti nalaze se u:
- `03-GettingStarted/samples/` - Primjeri specifični za jezik
- `03-GettingStarted/01-first-server/solution/` - Implementacije prvog servera
- `03-GettingStarted/02-client/solution/` - Implementacije klijenta
- `11-MCPServerHandsOnLabs/` - Sveobuhvatne radionice za integraciju baza podataka

Svaki primjerni projekt sadrži vlastite upute za postavljanje:

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
# or
pip install -e .
python main.py
```

#### Java projekti
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Radni tijek razvoja

### Struktura dokumentacije

- **Moduli 00-11**: Osnovni sadržaj kurikuluma u sekvencijalnom redoslijedu
- **translations/**: Verzije na različitim jezicima (automatski generirane, ne uređivati izravno)
- **translated_images/**: Lokalizirane verzije slika (automatski generirane)
- **images/**: Izvorne slike i dijagrami

### Izmjene dokumentacije

1. Uređujte samo engleske markdown datoteke u glavnim direktorijima modula (00-11)
2. Ažurirajte slike u direktoriju `images/` ako je potrebno
3. GitHub Action co-op-translator automatski će generirati prijevode
4. Prijevodi se ponovno generiraju pri svakom pushu na glavnu granu

### Rad s prijevodima

- **Automatski prijevod**: GitHub Actions tijek rada upravlja svim prijevodima
- **NE uređujte** datoteke u direktoriju `translations/`
- Metapodaci prijevoda ugrađeni su u svaku prevedenu datoteku
- Podržani jezici: 48+ jezika uključujući arapski, kineski, francuski, njemački, hindi, japanski, korejski, portugalski, ruski, španjolski i mnoge druge

## Upute za testiranje

### Validacija dokumentacije

Budući da je ovo prvenstveno repozitorij dokumentacije, testiranje se fokusira na:

1. **Validacija poveznica**: Provjerite rade li sve interne poveznice
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Validacija primjera koda**: Testirajte da se primjeri koda kompajliraju/pokreću
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Linting Markdowna**: Provjerite dosljednost formatiranja
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Testiranje primjernih projekata

Svaki primjerni projekt specifičan za jezik uključuje vlastiti pristup testiranju:

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

- Koristite jasan, jednostavan jezik prilagođen početnicima
- Uključite primjere koda u više jezika gdje je primjenjivo
- Slijedite najbolje prakse za markdown:
  - Koristite ATX-stil zaglavlja (`#` sintaksa)
  - Koristite ograđene blokove koda s identifikatorima jezika
  - Uključite opisni alt tekst za slike
  - Održavajte razumnu duljinu linija (bez stroge granice, ali budite praktični)

### Stil primjera koda

#### TypeScript/JavaScript
- Koristite ES module (`import`/`export`)
- Slijedite konvencije stroge mode u TypeScriptu
- Uključite anotacije tipova
- Ciljajte ES2022

#### Python
- Slijedite PEP 8 smjernice za stil
- Koristite tipne oznake gdje je primjenjivo
- Uključite docstringove za funkcije i klase
- Koristite moderne značajke Pythona (3.8+)

#### Java
- Slijedite konvencije Spring Boota
- Koristite značajke Java 21
- Slijedite standardnu strukturu Maven projekata
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

Repozitorij koristi GitHub Pages ili slične alate za hosting dokumentacije (ako je primjenjivo). Promjene u glavnoj grani pokreću:

1. Tijek rada za prijevod (`.github/workflows/co-op-translator.yml`)
2. Automatski prijevod svih engleskih markdown datoteka
3. Lokalizaciju slika prema potrebi

### Nije potrebna izgradnja

Ovaj repozitorij prvenstveno sadrži markdown dokumentaciju. Nije potrebna kompilacija ili korak izgradnje za osnovni sadržaj kurikuluma.

### Implementacija primjernih projekata

Pojedinačni primjerni projekti mogu imati upute za implementaciju:
- Pogledajte `03-GettingStarted/09-deployment/` za upute o implementaciji MCP servera
- Primjeri implementacije na Azure Container Apps u `11-MCPServerHandsOnLabs/`

## Smjernice za doprinos

### Proces pull requesta

1. **Fork i kloniranje**: Forkajte repozitorij i klonirajte svoj fork lokalno
2. **Kreirajte granu**: Koristite opisne nazive grana (npr. `fix/typo-module-3`, `add/python-example`)
3. **Izvršite promjene**: Uređujte samo engleske markdown datoteke (ne prijevode)
4. **Testirajte lokalno**: Provjerite da se markdown pravilno prikazuje
5. **Podnesite PR**: Koristite jasne naslove i opise PR-a
6. **CLA**: Potpišite Microsoft Contributor License Agreement kada se to zatraži

### Format naslova PR-a

Koristite jasne, opisne naslove:
- `[Module XX] Kratak opis` za promjene specifične za module
- `[Samples] Opis` za promjene primjernog koda
- `[Docs] Opis` za opća ažuriranja dokumentacije

### Što doprinijeti

- Ispravci grešaka u dokumentaciji ili primjernom kodu
- Novi primjeri koda u dodatnim jezicima
- Pojašnjenja i poboljšanja postojećeg sadržaja
- Nove studije slučaja ili praktični primjeri
- Prijave problema za nejasan ili netočan sadržaj

### Što NE raditi

- Ne uređujte datoteke u direktoriju `translations/`
- Ne uređujte direktorij `translated_images/`
- Ne dodajte velike binarne datoteke bez prethodne rasprave
- Ne mijenjajte datoteke tijeka rada za prijevod bez koordinacije

## Dodatne napomene

### Održavanje repozitorija

- **Changelog**: Sve značajne promjene dokumentirane su u `changelog.md`
- **Vodič za učenje**: Koristite `study_guide.md` za pregled navigacije kurikulumom
- **Predlošci za probleme**: Koristite GitHub predloške za prijavu grešaka i zahtjeve za značajke
- **Kodeks ponašanja**: Svi suradnici moraju slijediti Microsoft Open Source Code of Conduct

### Put učenja

Slijedite module u sekvencijalnom redoslijedu (00-11) za optimalno učenje:
1. **00-02**: Osnove (Uvod, Osnovni koncepti, Sigurnost)
2. **03**: Prvi koraci s praktičnom implementacijom
3. **04-05**: Praktična implementacija i napredne teme
4. **06-10**: Zajednica, najbolje prakse i primjene u stvarnom svijetu
5. **11**: Sveobuhvatne radionice za integraciju baza podataka (13 sekvencijalnih radionica)

### Resursi za podršku

- **Dokumentacija**: https://modelcontextprotocol.io/
- **Specifikacija**: https://spec.modelcontextprotocol.io/
- **Zajednica**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord server
- **Povezani tečajevi**: Pogledajte README.md za ostale Microsoftove putove učenja

### Česta pitanja

**P: Moj PR ne prolazi provjeru prijevoda**
O: Provjerite jeste li uređivali samo engleske markdown datoteke u glavnim direktorijima modula, a ne prevedene verzije.

**P: Kako dodati novi jezik?**
O: Podrška za jezike upravlja se putem tijeka rada co-op-translator. Otvorite problem za raspravu o dodavanju novih jezika.

**P: Primjeri koda ne rade**
O: Provjerite jeste li slijedili upute za postavljanje u README specifičnom za primjer. Provjerite imate li instalirane ispravne verzije ovisnosti.

**P: Slike se ne prikazuju**
O: Provjerite jesu li putanje slika relativne i koriste li kosu crtu. Slike bi trebale biti u direktoriju `images/` ili `translated_images/` za lokalizirane verzije.

### Razmatranja performansi

- Tijek rada za prijevod može potrajati nekoliko minuta
- Velike slike treba optimizirati prije predaje
- Održavajte pojedinačne markdown datoteke fokusiranim i razumno velikim
- Koristite relativne poveznice za bolju prenosivost

### Upravljanje projektom

Ovaj projekt slijedi Microsoftove prakse otvorenog koda:
- MIT licenca za kod i dokumentaciju
- Microsoft Open Source Code of Conduct
- CLA potreban za doprinose
- Sigurnosni problemi: Slijedite smjernice u SECURITY.md
- Podrška: Pogledajte SUPPORT.md za resurse pomoći

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.