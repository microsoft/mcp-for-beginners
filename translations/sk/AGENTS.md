# AGENTS.md

## Prehľad projektu

**MCP pre začiatočníkov** je open-source vzdelávací kurz na učenie sa Model Context Protocol (MCP) - štandardizovaného rámca pre interakcie medzi AI modelmi a klientskymi aplikáciami. Tento repozitár poskytuje komplexné učebné materiály s praktickými príkladmi kódu v rôznych programovacích jazykoch.

### Kľúčové technológie

- **Programovacie jazyky**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworky a SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databázy**: PostgreSQL s rozšírením pgvector
- **Cloud platformy**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Nástroje na zostavovanie**: npm, Maven, pip, Cargo
- **Dokumentácia**: Markdown s automatizovaným viacjazyčným prekladom (viac než 48 jazykov)

### Architektúra

- **11 základných modulov (00-11)**: Sekvenčná učebná cesta od základov po pokročilé témy
- **Praktické laboratóriá**: Praktické cvičenia so kompletným riešením v rôznych jazykoch
- **Ukážkové projekty**: Funkčné implementácie MCP servera a klienta
- **Prekladový systém**: Automatizovaný workflow GitHub Actions pre viacjazyčnú podporu
- **Obrázkové zdroje**: Centralizovaný adresár s obrázkami a ich preloženými verziami

## Príkazy na nastavenie

Toto je repozitár zameraný na dokumentáciu. Väčšina nastavenia prebieha v konkrétnych ukážkových projektoch a laboratóriách.

### Nastavenie repozitára

```bash
# Klonujte repozitár
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Práca s ukážkovými projektmi

Ukážkové projekty sa nachádzajú v adresároch:
- `03-GettingStarted/samples/` - príklady pre jednotlivé jazyky
- `03-GettingStarted/01-first-server/solution/` - Prvé implementácie servera
- `03-GettingStarted/02-client/solution/` - Implementácie klienta
- `11-MCPServerHandsOnLabs/` - Komplexné laboratóriá integrácie databáz

Každý ukážkový projekt obsahuje vlastné pokyny na nastavenie:

#### Projekty v TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Projekty v Pythone
```bash
cd <project-directory>
pip install -r requirements.txt
# alebo
pip install -e .
python main.py
```

#### Projekty v Jave
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Vývojový workflow

### Pripravenosť MCP 7-28

#### Kontrolný zoznam pripravenosti repozitára

- [x] **Jasnosť pre nových prispievateľov**: Tento súbor definuje účel repozitára,
  štruktúru, pravidlá prispievania a cesty pre nastavenie ukážok.
- [x] **Príkazy na build/test/lint s presnými parametrami**:
  - Lint dokumentácie repozitára:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit vzoru odkazov v dokumentácii repozitára:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validácia vzoriek v TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validácia vzoriek v Pythone:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validácia vzoriek v Jave:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Jeden realistický workflow, ktorý sa môže stať MCP nástrojom**:
  `validate_curriculum_change`
- [x] **Vstupy/výstupy sú explicitné** (pozri špecifikáciu nižšie).
- [x] **Oprávnenia a režimy zlyhania sú zdokumentované** (pozri špecifikáciu nižšie).
- [x] **Testovateľnosť CI je explicitná** (deterministické príkazy, explicitné
  návratové kódy a strojovo čitateľné výstupy).

#### Kandidátsky MCP nástroj workflow: `validate_curriculum_change`

##### Cieľ

Overiť zmeny dokumentácie kurikula a reprezentatívnu kvalitu vzorového kódu
pred zlúčením.

##### Vstupy

- `changed_paths: string[]` (povinné) - relatívne cesty zmenené v PR.
- `run_docs_lint: boolean` (predvolené `true`)
- `run_links_audit: boolean` (predvolené `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (predvolené všetko `false`)

##### Výstupy

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Oprávnenia

- Iba čítanie súborov pracovného priestoru a zápis artefaktov generovaných nástrojom (napr. lint
  reportov, logov testov); nie je povolený zápis do `translations/` alebo
  `translated_images/`.
- Spúšťanie lokálnych shell príkazov.
- Voliteľný prístup na sieť iba pre obnovu balíkov (`npm ci`,
  `python -m pip install`, vyriešenie závislostí `mvn`).
- Nie je dovolené push/merge alebo úpravy v `translations/` alebo
  `translated_images/`.

##### Režimy zlyhania

- `E_NO_INPUT_PATHS`: pole `changed_paths` je prázdne.
- `E_INVALID_PATH`: vstupná cesta vychádza mimo koreň repozitára.
- `E_LINT_FAILED`: markdown lint skončil s nenulovým kódom.
- `E_LINK_AUDIT_FAILED`: audit odkazov skončil s nenulovým kódom.
- `E_SAMPLE_TEST_FAILED`: test/výstavba vzorky skončila s chybou.
- `E_TIMEOUT`: príkaz prekročil nastavený časový limit.

##### Odporúčaná CI zmluva

Na automatizáciu validácie nastavte CI job, ktorý:

- Spúšťa sa na pull requesty zasahujúce do `*.md`, vzorových kódov alebo tohto súboru.
- Spúšťa presné vyššie uvedené príkazy.
- Ukladá logy ako artefakty.
- Neúspech jobu pri akomkoľvek nenulovom návratovom kóde.

#### Ak nasadzujete MCP server z tohto repozitára

- [ ] Prečítajte si konečný changelog MCP `2026-07-28`:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Overte, že zvolená verzia SDK podporuje MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Odstráňte predpoklady o relácii a handshake; každý request spracúvajte ako
  samostatný:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Posielajte hlavičky `Mcp-Method` a `Mcp-Name` pre čisté HTTP požiadavky:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Revízia hardcoded kódov chýb (`missing resource` bolo presunuté z `-32002` na `-32602`).
- [ ] Migrujte z deprecated Roots, Sampling, Logging a Dynamic Client
  Registration:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Odstráňte experimentálne API `2025-11-25` Tasks:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Preskúmajte autorizáciu pre zlepšenie bezpečnosti OAuth a OpenID Connect:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Štruktúra dokumentácie

- **Moduly 00-11**: Základný obsah kurikula v poradí
- **translations/**: Jazykové verzie (automaticky generované, neupravujte priamo)
- **translated_images/**: Lokalizované verzie obrázkov (automatizované)
- **images/**: Zdrojové obrázky a diagramy

### Ako vykonať zmeny v dokumentácii

1. Upraviť len anglické markdown súbory v koreňových adresároch modulov (00-11)
2. Ak je potrebné, aktualizovať obrázky v adresári `images/`
3. GitHub Action co-op-translator automaticky vytvorí preklady
4. Preklady sa regenerujú pri pushi do vetvy main

### Práca s prekladmi

- **Automatizovaný preklad**: GitHub Actions workflow spravuje všetky preklady
- **NEUpravujte manuálne** súbory v adresári `translations/`
- Metaúdaje o preklade sú vložené v každom preloženom súbore
- Podporované jazyky: viac než 48, vrátane arabčiny, čínštiny, francúzštiny, nemčiny, hindčiny, japončiny, kórejčiny, portugalčiny, ruštiny, španielčiny a mnohých ďalších

## Inštrukcie na testovanie

### Validácia dokumentácie

Keďže ide primárne o repozitár dokumentácie, testovanie je zamerané na:

1. **Audit vzoru odkazov**: Zoznam Markdown odkazov na kontrolu

   ```bash
   # Zoznam Markdown odkazov (kontrola vzoru)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validácia príkladov kódu**: Test, že príklady kódu sa kompilujú/spúšťajú

   ```bash
   # Prejdite na konkrétny vzor a spustite jeho testy
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Lintovanie Markdownu**: Kontrola konzistencie formátovania

   ```bash
   # Použite markdownlint podľa potreby
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testovanie ukážkových projektov

Každá jazyková ukážka má vlastný prístup k testovaniu:

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

## Pravidlá štýlu kódu

### Štýl dokumentácie

- Používajte jasný, priateľský jazyk pre začiatočníkov
- Začleňte príklady kódu v rôznych jazykoch, kde je to vhodné
- Dodržiavajte markdownové osvedčené postupy:
  - Používajte hlavičky ATX štýlu (`#` syntax)
  - Používajte ohraničené bloky kódu s označením jazyka
  - Pridajte popisné alt texty k obrázkom
  - Zachovajte primeranú dĺžku riadkov (bez tvrdého limitu, no zmysluplne)

### Štýl ukážkového kódu

#### TypeScript/JavaScript
- Používajte ES moduly (`import`/`export`)
- Dodržiavajte prísne pravidlá TypeScriptu
- Začleňte anotácie typov
- Cieľte ES2022

#### Python
- Dodržiavajte štýlové pravidlá PEP 8
- Používajte typové nápovedy tam, kde je to vhodné
- Začleňte docstringy pre funkcie a triedy
- Používajte moderné funkcie Pythonu (3.8+)

#### Java
- Dodržiavajte konvencie Spring Boot
- Používajte funkcie Java 21
- Dodržiavajte štandardnú štruktúru Maven projektov
- Začleňte Javadoc komentáre

### Organizácia súborov

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

## Kompilácia a nasadenie

### Nasadenie dokumentácie

Repozitár používa GitHub Pages alebo podobné riešenie pre hosting dokumentácie (ak je to potrebné). Zmeny v hlavnej vetve spúšťajú:

1. Prekladový workflow (`.github/workflows/co-op-translator.yml`)
2. Automatický preklad všetkých anglických markdown súborov
3. Lokálne zmeny obrázkov podľa potreby

### Nie je potrebný build proces

Tento repozitár primárne obsahuje markdown dokumentáciu. Nie je potrebné žiadne kompilovanie alebo build kroky pre core obsah kurikula.

### Nasadenie ukážkových projektov

Jednotlivé ukážkové projekty môžu obsahovať pokyny na nasadenie:
- Pozrite `03-GettingStarted/09-deployment/` pre nasadenie MCP servera
- Príklady nasadenia Azure Container Apps v `11-MCPServerHandsOnLabs/`

## Pravidlá prispievania

### Proces pull requestu

1. **Forknite a naklonujte si repozitár**: Forknite ho a lokálne si sklonujte svoj fork
2. **Vytvorte vetvu**: Používajte popisné názvy vetiev (napr. `fix/typo-module-3`, `add/python-example`)
3. **Vykonajte zmeny**: Upraviť len anglické markdown súbory (nie preklady)
4. **Otestujte lokálne**: Overte správne zobrazenie markdownu
5. **Odošlite PR**: Použite jasné názvy a popisy PR
6. **CLA**: Podpíšte Microsoft Contributor License Agreement, keď sa zobrazí výzva

### Formát názvu PR

Používajte jasné, popisné názvy:
- `[Module XX] Krátky popis` pre zmeny špecifické pre modul
- `[Samples] Popis` pre zmeny vo vzorovom kóde
- `[Docs] Popis` pre všeobecné aktualizácie dokumentácie

### Čo prispievať

- Opravy chýb v dokumentácii alebo vzorových kódoch
- Nové príklady kódu v ďalších jazykoch
- Vysvetlenia a vylepšenia existujúceho obsahu
- Nové štúdie prípadov alebo praktické príklady
- Hlásenia nejasného alebo nesprávneho obsahu

### Čomu sa vyhnúť

- Neupravujte priamo súbory v adresári `translations/`
- Neupravujte adresár `translated_images/`
- Nepridávajte veľké binárne súbory bez predchádzajúcej diskusie
- Nezmieňujte prekladový workflow bez koordinácie

## Ďalšie poznámky

### Údržba repozitára

- **Changelog**: Všetky významné zmeny sú zdokumentované v `changelog.md`
- **Študijný sprievodca**: Používa sa `study_guide.md` na prehľad navigácie kurikula
- **Šablóny issue**: Používajte GitHub šablóny issue pre nahlasovanie chýb a požiadavky na funkcie
- **Kód správania**: Všetci prispievatelia musia dodržiavať Microsoft Open Source Code of Conduct

### Učebná cesta

Postupujte podľa modulov v poradí (00-11) pre optimálne učenie:
1. **00-02**: Základy (Úvod, Základné koncepty, Bezpečnosť)
2. **03**: Začínajúce praktické implementácie
3. **04-05**: Praktická implementácia a pokročilé témy
4. **06-10**: Komunita, osvedčené postupy a reálne aplikácie
5. **11**: Komplexné laboratóriá integrácie databáz (13 postupných labov)

### Zdroje podpory

- **Dokumentácia**: https://modelcontextprotocol.io/
- **Špecifikácia**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Komunita**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord server
- **Súvisiace kurzy**: Pozrite README.md pre ďalšie Microsoft učebné cesty

### Bežné riešenie problémov

**Otázka: Môj PR zlyháva kontrolu prekladu**
Odpoveď: Uistite sa, že ste upravili iba anglické markdown súbory v koreňových adresároch modulov, nie preložené verzie.

**Otázka: Ako pridať nový jazyk?**
Odpoveď: Podpora jazykov sa spravuje cez co-op-translator workflow. Otvorte issue na diskusiu o pridávaní nových jazykov.

**Otázka: Príklady kódu nefungujú**
Odpoveď: Uistite sa, že ste postupovali podľa inštrukcií na nastavenie v README konkrétnej ukážky. Skontrolujte, či máte správne verzie závislostí.

**Otázka: Obrázky sa nezobrazujú**

A: Overte, či sú cesty k obrázkom relatívne a používajú lomky vpred. Obrázky by mali byť v priečinku `images/` alebo `translated_images/` pre lokalizované verzie.

### Úvahy o výkone

- Prekladový pracovný tok môže trvať niekoľko minút
- Veľké obrázky by mali byť optimalizované pred odovzdaním
- Jednotlivé markdown súbory by mali byť zamerané a primerane veľké
- Používajte relatívne odkazy pre lepšiu prenosnosť

### Správa projektu

Tento projekt nasleduje praktiky open source Microsoftu:
- Licencia MIT pre kód a dokumentáciu
- Microsoft Open Source Kód správania
- CLA je požadovaná pre príspevky
- Bezpečnostné problémy: Dodržiavajte pokyny v SECURITY.md
- Podpora: Pozrite si SUPORT.md pre zdroje pomoci

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->