# AGENTS.md

## Prehľad projektu

**MCP pre začiatočníkov** je open-source vzdelávací kurz pre učenie sa Model Context Protocol (MCP) - štandardizovaný rámec pre interakciu medzi AI modelmi a klientskymi aplikáciami. Tento repozitár poskytuje komplexné učebné materiály s praktickými príkladmi kódu v niekoľkých programovacích jazykoch.

### Kľúčové technológie

- **Programovacie jazyky**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworky & SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databázy**: PostgreSQL s rozšírením pgvector
- **Cloud platformy**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Nástroje na zostavovanie**: npm, Maven, pip, Cargo
- **Dokumentácia**: Markdown s automatizovaným prekladom do viacerých jazykov (48+ jazykov)

### Architektúra

- **11 jadrových modulov (00-11)**: Sekvenčná učebná cesta od základov po pokročilé témy
- **Praktické laboratóriá**: Praktické cvičenia s kompletnými riešeniami v niekoľkých jazykoch
- **Ukážkové projekty**: Fungujúce implementácie MCP servera a klienta
- **Systém prekladu**: Automatizovaný workflow GitHub Actions na podporu viacerých jazykov
- **Obrázkové zdroje**: Centralizovaný adresár obrázkov s preloženými verziami

## Príkazy na nastavenie

Toto je repozitár zameraný na dokumentáciu. Väčšina nastavení sa vykonáva v jednotlivých ukážkových projektoch a laboratóriách.

### Nastavenie repozitára

```bash
# Naklonujte repozitár
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Práca s ukážkovými projektmi

Ukážkové projekty sa nachádzajú v:
- `03-GettingStarted/samples/` - Príklady špecifické pre jazyk
- `03-GettingStarted/01-first-server/solution/` - Implementácie prvého servera
- `03-GettingStarted/02-client/solution/` - Implementácie klienta
- `11-MCPServerHandsOnLabs/` - Komplexné laboratória integrácie databázy

Každý ukážkový projekt obsahuje svoje vlastné inštrukcie na nastavenie:

#### Projekty TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Projekty Python
```bash
cd <project-directory>
pip install -r requirements.txt
# alebo
pip install -e .
python main.py
```

#### Projekty Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Vývojový pracovný tok

### MCP 7-28 pripravenosť

#### Kontrolný zoznam pripravenosti repozitára

- [x] **Jasnosť pre nových prispievateľov**: Tento súbor definuje účel repozitára,
  štruktúru, pravidlá pre prispievanie a cesty nastavenia vzorov.
- [x] **Príkazy na build/test/lint s presnými parametrami**:
  - Lintovanie dokumentácie repozitára:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit vzorov odkazov v dokumentácii:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Overenie ukážok TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Overenie ukážok Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Overenie ukážok Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Jeden realistický pracovný tok, ktorý môže byť MCP nástrojom**:
  `validate_curriculum_change`
- [x] **Vstupy/výstupy sú explicitné** (pozri špecifikáciu nižšie).
- [x] **Povolenia a režimy zlyhania sú zdokumentované** (pozri špecifikáciu nižšie).
- [x] **Testovateľnosť v CI je explicitná** (deterministické príkazy, explicitné
  návratové kódy a výstupy čitateľné strojom).

#### Kandidátsky workflow MCP nástroja: `validate_curriculum_change`

##### Cieľ

Validovať zdravie zmien v dokumentácii kurikula a reprezentatívneho ukážkového kódu
pred zlúčením.

##### Vstupy

- `changed_paths: string[]` (povinné) - relatívne cesty zmenené v PR.
- `run_docs_lint: boolean` (predvolené `true`)
- `run_links_audit: boolean` (predvolené `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (predvolené všetky `false`)

##### Výstupy

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Povolenia

- Čítať súbory pracovného priestoru a zapisovať artefakty generované nástrojom (napr. lint
  reporty, záznamy testov) iba; žiadne zápisy do `translations/` alebo
  `translated_images/`.
- Vykonávať lokálne shell príkazy.
- Voliteľný prístup na sieť iba pre obnovenie balíkov (`npm ci`,
  `python -m pip install`, riešenie závislostí `mvn`).
- Žiadne povolenie na push, merge alebo úpravy `translations/` alebo
  `translated_images/`.

##### Režimy zlyhania

- `E_NO_INPUT_PATHS`: `changed_paths` je prázdne.
- `E_INVALID_PATH`: vstupná cesta uniká z koreňa repozitára.
- `E_LINT_FAILED`: lint markdownu skončil s nenulovým kódom.
- `E_LINK_AUDIT_FAILED`: príkaz audit odkazu skončil s nenulovým kódom.
- `E_SAMPLE_TEST_FAILED`: testovanie/stavba ukážky skončila s nenulovým kódom.
- `E_TIMEOUT`: príkaz prekročil nastavený časový limit.

##### Odporúčaný kontrakt CI

Pre automatizáciu validácie nastavte CI job, ktorý:

- Spúšťa sa na pull requesty zasahujúce do `*.md`, ukážkový kód alebo tento súbor.
- Spúšťa presné vyššie uvedené príkazy.
- Ukladá záznamy ako artefakty.
- Zlyháva job pri akomkoľvek nenulovom návratovom kóde.

#### Ak vydávate MCP server z tohto repozitára

- [ ] Prečítajte si návrh changelogu pre MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Otestujte váš server s beta verziami SDK:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Odstráňte predpoklady týkajúce sa relácie a handshake; považujte každý request za
  samostatný:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Odosielajte hlavičky `Mcp-Method` a `Mcp-Name` pre surové HTTP požiadavky:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Skontrolujte pevne zakódované chybové kódy (`missing resource` sa presunul z `-32002` na `-32602`).
- [ ] Označte a naplánujte migráciu pre zastarané roots, sampling a
  logging:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrujte z experimentálneho API Tasks `2025-11-25`:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Prezrite autorizáciu pre spevnenie OAuth a OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Štruktúra dokumentácie

- **Moduly 00-11**: Jadro obsahu kurikula v sekvenčnom poradí
- **translations/**: Jazykovo špecifické verzie (automaticky generované, neupravujte priamo)
- **translated_images/**: Lokalizované verzie obrázkov (automaticky generované)
- **images/**: Zdrojové obrázky a diagramy

### Úpravy dokumentácie

1. Upraviť iba anglické markdown súbory v koreňových adresároch modulov (00-11)
2. Aktualizovať obrázky v adresári `images/`, ak je to potrebné
3. GitHub Action co-op-translator automaticky vytvorí preklady
4. Preklady sa regenerujú pri pushi do hlavnej vetvy

### Práca s prekladmi

- **Automatický preklad**: GitHub Actions workflow riadi všetky preklady
- **NEUPRAVUJTE ručne** súbory v adresári `translations/`
- Metaúdaje prekladu sú vložené v každom preloženom súbore
- Podporované jazyky: 48+ jazykov vrátane arabčiny, čínštiny, francúzštiny, nemčiny, hindčiny, japončiny, kórejčiny, portugalčiny, ruštiny, španielčiny a mnohých ďalších

## Pokyny na testovanie

### Validácia dokumentácie

Pretože ide predovšetkým o repozitár dokumentácie, testovanie sa zameriava na:

1. **Audit vzorov odkazov**: Výpis Markdown odkazov na kontrolu

   ```bash
   # Zoznam odkazov v Markdowne (audit vzorov)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validácia ukážok kódu**: Testovanie, že príklady kódu sa kompilujú/spúšťajú

   ```bash
   # Prejdite na konkrétny príklad a spustite jeho testy
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Lintovanie markdownu**: Kontrola konzistencie formátovania

   ```bash
   # Použite markdownlint, ak je to potrebné
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testovanie ukážkových projektov

Každý jazykovo špecifický príklad obsahuje vlastný prístup k testovaniu:

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

## Pokyny pre štýl kódu

### Štýl dokumentácie

- Používajte jasný, pre začiatočníkov zrozumiteľný jazyk
- Zahrňte príklady kódu vo viacerých jazykoch tam, kde je to vhodné
- Dodržiavajte najlepšie praktiky markdownu:
  - Používajte ATX štýl nadpisov (syntax `#`)
  - Používajte ohraničené bloky kódu so špecifikáciou jazyka
  - Zahrňte popisný alt text pre obrázky
  - Dbajte na rozumnú dĺžku riadkov (žiadne tvrdé obmedzenie, ale buďte rozumní)

### Štýl ukážok kódu

#### TypeScript/JavaScript
- Používajte ES moduly (`import`/`export`)
- Dodržiavajte konvencie prísneho režimu TypeScript
- Zahrňte anotácie typov
- Cieľte na ES2022

#### Python
- Dodržiavajte štýlové usmernenia PEP 8
- Používajte typové nápovedy tam, kde je vhodné
- Zahrňte docstringy pre funkcie a triedy
- Používajte moderné funkcie Pythonu (3.8+)

#### Java
- Dodržiavajte konvencie Spring Boot
- Používajte funkcie Java 21
- Dodržiavajte štandardnú štruktúru Maven projektov
- Zahrňte komentáre Javadoc

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

## Zostavenie a nasadenie

### Nasadenie dokumentácie

Repozitár používa GitHub Pages alebo podobné na hosťovanie dokumentácie (ak je to relevantné). Zmeny v hlavnej vetve spustia:

1. Workflow prekladov (`.github/workflows/co-op-translator.yml`)
2. Automatizovaný preklad všetkých anglických markdown súborov
3. Lokalizáciu obrázkov podľa potreby

### Nepotrebný proces zostavovania

Tento repozitár primárne obsahuje markdown dokumentáciu. Nie je potrebný žiadny krok kompilácie alebo zostavovania pre jadrový obsah kurikula.

### Nasadenie ukážkových projektov

Jednotlivé ukážkové projekty môžu obsahovať inštrukcie k nasadeniu:
- Pozrite `03-GettingStarted/09-deployment/` pre návody na nasadenie MCP servera
- Príklady nasadenia Azure Container Apps v `11-MCPServerHandsOnLabs/`

## Pokyny pre prispievanie

### Proces pull requestov

1. **Forknite a sklonujte**: Vytvorte fork repozitára a sklonujte ho lokálne
2. **Vytvorte vetvu**: Používajte popisné názvy vetiev (napr. `fix/typo-module-3`, `add/python-example`)
3. **Urobte zmeny**: Upraviť iba anglické markdown súbory (nie preklady)
4. **Otestujte lokálne**: Overte správne zobrazenie markdownu
5. **Odošlite PR**: Používajte jasné názvy a popisy PR
6. **CLA**: Podpíšte Microsoft Contributor License Agreement, keď o to budete požiadaní

### Formát názvu PR

Používajte jasné, popisné názvy:
- `[Module XX] Krátky popis` pre moduly
- `[Samples] Popis` pre zmeny v ukážkovom kóde
- `[Docs] Popis` pre všeobecné aktualizácie dokumentácie

### Čo prispievať

- Opravy chýb v dokumentácii alebo ukážkach kódu
- Nové príklady kódu v ďalších jazykoch
- Vyjasnenia a vylepšenia existujúceho obsahu
- Nové prípadové štúdie alebo praktické príklady
- Hlásenia chýb pre nejasný alebo nesprávny obsah

### Čo nerobiť

- Neupravujte priamo súbory v adresári `translations/`
- Neupravujte adresár `translated_images/`
- Nepridávajte veľké binárne súbory bez diskusie
- Nemeniť workflowy prekladov bez koordinácie

## Ďalšie poznámky

### Údržba repozitára

- **Changelog**: Všetky významné zmeny sú zdokumentované v `changelog.md`
- **Študijný sprievodca**: Použite `study_guide.md` pre prehľad navigácie kurikula
- **Šablóny issues**: Používajte GitHub šablóny na hlásenia chýb a žiadosti o funkcie
- **Kód správania**: Všetci prispievatelia musia dodržiavať Microsoft Open Source Code of Conduct

### Učebná cesta

Postupujte podľa modulov v sekvenčnom poradí (00-11) pre optimálne učenie:
1. **00-02**: Základy (Úvod, Jadro konceptov, Bezpečnosť)
2. **03**: Začiatky s praktickou implementáciou
3. **04-05**: Praktická implementácia a pokročilé témy
4. **06-10**: Komunita, najlepšie praktiky a reálne využitie
5. **11**: Komplexné laboratóriá integrácie databázy (13 sekvenčných laboratórií)

### Podporné zdroje

- **Dokumentácia**: https://modelcontextprotocol.io/
- **Špecifikácia**: https://spec.modelcontextprotocol.io/
- **Komunita**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord server
- **Súvisiace kurzy**: Pozrite README.md pre ďalšie Microsoft vzdelávacie cesty

### Bežné riešenie problémov

**Otázka: Môj PR neprešiel kontrolou prekladu**
Odpoveď: Uistite sa, že ste upravovali iba anglické markdown súbory v koreňových adresároch modulov, nie preložené verzie.

**Otázka: Ako pridať nový jazyk?**
Odpoveď: Podpora jazykov je riadená workflowom co-op-translator. Otvorte issue na diskusiu o pridanie nových jazykov.

**Otázka: Ukážky kódu nefungujú**

A: Uistite sa, že ste postupovali podľa inštrukcií na nastavenie v README konkrétneho príkladu. Skontrolujte, či máte nainštalované správne verzie závislostí.

**Otázka: Obrázky sa nezobrazujú**
A: Overte, či cesty k obrázkom sú relatívne a používajú lomky dopredu. Obrázky by mali byť v adresári `images/` alebo `translated_images/` pre lokalizované verzie.

### Výkonnostné úvahy

- Prekladový pracovný tok môže trvať niekoľko minút
- Veľké obrázky by mali byť optimalizované pred commitom
- Uchovávajte jednotlivé markdown súbory zamerané a rozumnej veľkosti
- Používajte relatívne odkazy pre lepšiu prenosnosť

### Správa projektu

Tento projekt dodržiava otvorené praktiky Microsoftu:
- Licencia MIT pre kód a dokumentáciu
- Microsoft Open Source Kód Správania
- Pre príspevky je potrebná CLA
- Bezpečnostné problémy: Dodržiavajte pokyny SECURITY.md
- Podpora: Pozrite si SUPORT.md pre zdroje pomoci

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->