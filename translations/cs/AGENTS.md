# AGENTS.md

## Přehled projektu

**MCP pro začátečníky** je otevřený výukový kurz pro učení Model Context Protocol (MCP) - standardizovaného rámce pro interakce mezi AI modely a klientskými aplikacemi. Toto repozitář poskytuje komplexní vzdělávací materiály s praktickými ukázkami kódu v několika programovacích jazycích.

### Klíčové technologie

- **Programovací jazyky**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworky & SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databáze**: PostgreSQL s rozšířením pgvector
- **Cloudové platformy**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Nástroje pro sestavení**: npm, Maven, pip, Cargo
- **Dokumentace**: Markdown s automatizovaným vícejazyčným překladem (48+ jazyků)

### Architektura

- **11 základních modulů (00-11)**: Postupná cesta učením od základů po pokročilá témata
- **Praktické laboratoře**: Praktická cvičení s kompletním řešením v několika jazycích
- **Ukázkové projekty**: Fungující implementace MCP serveru a klienta
- **Překladový systém**: Automatizovaný GitHub Actions workflow pro vícejazyčnou podporu
- **Soubory s obrázky**: Centralizovaný adresář obrázků s přeloženými verzemi

## Příkazy nastavení

Toto je repozitář zaměřený na dokumentaci. Většina nastavení probíhá v jednotlivých ukázkových projektech a laboratořích.

### Nastavení repozitáře

```bash
# Naklonujte repozitář
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Práce s ukázkovými projekty

Ukázkové projekty jsou umístěny v:
- `03-GettingStarted/samples/` - Ukázky specifické pro jazyk
- `03-GettingStarted/01-first-server/solution/` - První implementace serveru
- `03-GettingStarted/02-client/solution/` - Implementace klienta
- `11-MCPServerHandsOnLabs/` - Komplexní laboratoře integrace databáze

Každý ukázkový projekt obsahuje vlastní instrukce pro nastavení:

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
# nebo
pip install -e .
python main.py
```

#### Projekty Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Vývojový pracovní postup

### Připravenost MCP 7-28

#### Kontrolní seznam připravenosti repozitáře

- [x] **Jasnost pro nové přispěvatele**: Tento soubor definuje účel repozitáře,
  strukturu, pravidla příspěvků a cesty pro nastavení ukázek.
- [x] **Příkazy pro sestavení/testování/lintování s přesnými přepínači**:
  - Lintování dokumentace repozitáře:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit vzorců odkazů v dokumentaci repozitáře:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validace ukázky TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validace ukázky Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validace ukázky Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Jeden realistický pracovní postup, který může být nástrojem MCP**:
  `validate_curriculum_change`
- [x] **Vstupy/výstupy jsou explicitní** (viz specifikace níže).
- [x] **Oprávnění a režimy selhání jsou zdokumentovány** (viz specifikace níže).
- [x] **Testovatelnost CI je explicitní** (deterministické příkazy, explicitní
  návratové kódy a strojově čitelné výstupy).

#### Kandidátní pracovní postup nástroje MCP: `validate_curriculum_change`

##### Cíl

Ověřit změny dokumentace kurikula a stav reprezentativního ukázkového kódu
před sloučením.

##### Vstupy

- `changed_paths: string[]` (povinné) - relativní cesty změněné v PR.
- `run_docs_lint: boolean` (výchozí `true`)
- `run_links_audit: boolean` (výchozí `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (výchozí všechny `false`)

##### Výstupy

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Oprávnění

- Číst soubory pracovního prostoru a zapisovat výstupy generované nástrojem (např. lint
  reporty, testovací logy) pouze; není povoleno zapisovat do `translations/` ani
  `translated_images/`.
- Spouštět lokální příkazy shellu.
- Volitelný přístup k síti pouze pro obnovení balíčků (`npm ci`,
  `python -m pip install`, řešení závislostí `mvn`).
- Není povoleno pushovat, sloučit nebo měnit `translations/` ani
  `translated_images/`.

##### Režimy selhání

- `E_NO_INPUT_PATHS`: prázdné `changed_paths`.
- `E_INVALID_PATH`: vstupní cesta uniká z kořenového adresáře repozitáře.
- `E_LINT_FAILED`: lint.md skončil chybou.
- `E_LINK_AUDIT_FAILED`: audit odkazů skončil chybou.
- `E_SAMPLE_TEST_FAILED`: test/sestavení ukázky skončilo chybou.
- `E_TIMEOUT`: příkaz překročil nastavený časový limit.

##### Doporučená smlouva pro CI

Pro automatizaci ověření nakonfigurujte CI úlohu, která:

- Spouští se na pull requesty ovlivňující `*.md`, ukázkové kódy nebo tento soubor.
- Spouští přesně uvedené příkazy výše.
- Uchovává logy jako artefakty.
- Selže úloha při jakémkoli nenulovém návratovém kódu.

#### Pokud dodáváte MCP server z tohoto repozitáře

- [ ] Přečtěte si koncept změnového záznamu pro MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Otestujte svůj server proti beta verzím SDK:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Odstraňte předpoklady relace a handshake; každý požadavek považujte za
  samostatný:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Posílejte hlavičky `Mcp-Method` a `Mcp-Name` pro surové HTTP požadavky:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Zkontrolujte tvrdě kódované chybové kódy (`missing resource` se přesunul z `-32002` na `-32602`).

- [ ] Označit a naplánovat migraci pro zastaralé kořeny, vzorkování a
  protokolování:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrovat z experimentálního API úkolů `2025-11-25`:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Přezkoumat autorizaci pro zpřísnění OAuth a OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Struktura dokumentace

- **Moduly 00-11**: Základní obsah kurikula v pořadí
- **translations/**: Jazykové verze (automaticky generované, neupravovat přímo)
- **translated_images/**: Lokalizované verze obrázků (automaticky generované)
- **images/**: Zdrojové obrázky a diagramy

### Provádění změn v dokumentaci

1. Upravit pouze anglické markdown soubory v kořenových složkách modulů (00-11)
2. Aktualizovat obrázky v adresáři `images/`, pokud je potřeba
3. Akce co-op-translator na GitHubu automaticky vygeneruje překlady
4. Překlady se znovu generují při pushi do hlavní větve

### Práce s překlady

- **Automatický překlad**: Workflow GitHub Actions zajišťuje všechny překlady
- **NEupravit ručně** soubory v adresáři `translations/`
- Metadata překladu jsou vložena v každém přeloženém souboru
- Podporované jazyky: 48+ jazyků včetně arabštiny, čínštiny, francouzštiny, němčiny, hindštiny, japonštiny, korejštiny, portugalštiny, ruštiny, španělštiny a dalších

## Instrukce pro testování

### Validace dokumentace

Protože se jedná primárně o repozitář s dokumentací, testování se zaměřuje na:

1. **Audit vzoru odkazů**: Vypsat Markdown odkazy ke kontrole

   ```bash
   # Vypsat odkazy v Markdownu (audit vzoru)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validace ukázek kódu**: Otestovat, že se příklady kódu sestaví/spustí

   ```bash
   # Přejděte ke konkrétnímu vzorku a spusťte jeho testy
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Lintování Markdownu**: Zkontrolovat konzistenci formátování

   ```bash
   # Použijte markdownlint, pokud je to potřeba
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testování ukázkových projektů

Každý jazykový vzorek má svůj vlastní testovací přístup:

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

## Směrnice stylu kódu

### Styl dokumentace

- Používat jasný jazyk přívětivý pro začátečníky
- Zahrnout příklady kódu ve více jazycích, kde je to vhodné
- Dodržovat nejlepší praktiky Markdownu:
  - Používat nadpisy stylu ATX (`#` syntax)
  - Používat ohraničené bloky kódu s identifikátory jazyka
  - Přidávat popisný alternativní text k obrázkům
  - Udržovat rozumnou délku řádek (žádný tvrdý limit, ale rozumně)

### Styl ukázek kódu

#### TypeScript/JavaScript
- Používat ES moduly (`import`/`export`)
- Dodržovat přísný režim TypeScriptu
- Přidávat typové anotace
- Cílit na ES2022

#### Python
- Dodržovat PEP 8 stylové směrnice
- Používat typové nápovědy tam, kde je vhodné
- Přidávat docstringy pro funkce a třídy
- Používat moderní funkce Pythonu (3.8+)

#### Java
- Dodržovat konvence Spring Boot
- Používat funkce Java 21
- Dodržovat standardní strukturu Maven projektu
- Přidávat komentáře Javadoc

### Organizace souborů

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

## Sestavení a nasazení

### Nasazení dokumentace

Repozitář používá GitHub Pages nebo obdobné řešení pro hostování dokumentace (pokud je to relevantní). Změny v hlavní větvi vyvolávají:

1. Překladový workflow (`.github/workflows/co-op-translator.yml`)
2. Automatický překlad všech anglických markdown souborů
3. Lokalizaci obrázků podle potřeby

### Není vyžadován žádný proces sestavení

Tento repozitář primárně obsahuje markdownovou dokumentaci. Nevyžaduje se žádný krok kompilace nebo sestavení pro základní obsah kurikula.

### Nasazení ukázkového projektu

Jednotlivé ukázkové projekty mohou mít pokyny k nasazení:
- Viz `03-GettingStarted/09-deployment/` pro pokyny k nasazení MCP serveru
- Příklady nasazení Azure Container Apps v `11-MCPServerHandsOnLabs/`

## Směrnice pro přispívání

### Proces pull requestu

1. **Fork a klonování**: Vytvořte fork repozitáře a naklonujte si ho lokálně
2. **Vytvoření větve**: Používejte popisné názvy větví (např. `fix/typo-module-3`, `add/python-example`)
3. **Provedení změn**: Upravujte pouze anglické markdown soubory (ne překlady)
4. **Testování lokálně**: Ověřte správné zobrazení markdownu
5. **Odeslání PR**: Používejte jasné názvy a popisy PR
6. **CLA**: Při vyzvání podepište Microsoft Contributor License Agreement

### Formát názvu PR

Používejte jasné, popisné názvy:
- `[Module XX] Krátký popis` pro změny specifické pro modul
- `[Samples] Popis` pro změny v ukázkovém kódu
- `[Docs] Popis` pro obecné aktualizace dokumentace

### Co přispívat

- Opravy chyb v dokumentaci nebo ukázkách kódu
- Nové příklady kódu v dalších jazycích
- Upřesnění a vylepšení stávajícího obsahu
- Nové případové studie nebo praktické příklady
- Nahlášení problémů s nejasným nebo nesprávným obsahem

### Co NEdělat

- Neupravovat přímo soubory v adresáři `translations/`
- Neupravovat adresář `translated_images/`
- Nepřidávat velké binární soubory bez diskuse
- Neměnit překladový workflow bez koordinace

## Dodatečné poznámky

### Údržba repozitáře

- **Changelog**: Všechny významné změny jsou dokumentovány v `changelog.md`
- **Studijní průvodce**: Používejte `study_guide.md` pro přehled navigace kurikula
- **Šablony problémů**: Používejte GitHub šablony pro hlášení chyb a požadavky na funkce
- **Kodex chování**: Všichni přispěvatelé musí dodržovat Microsoft Open Source Kodex chování

### Studijní cesta

Následujte moduly v pořadí (00-11) pro optimální učení:
1. **00-02**: Základy (Úvod, Základní pojmy, Bezpečnost)
2. **03**: Začínáme s praktickou implementací
3. **04-05**: Praktická implementace a pokročilá témata
4. **06-10**: Komunita, nejlepší praktiky a reálné aplikace
5. **11**: Komplexní laboratoře integrace databáze (13 sekvenčních laboratoří)

### Zdroj podpory

- **Dokumentace**: https://modelcontextprotocol.io/
- **Specifikace**: https://spec.modelcontextprotocol.io/
- **Komunita**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord server
- **Související kurzy**: Viz README.md pro další Microsoft učební cesty

### Běžné potíže

**Q: Můj PR selhává na kontrole překladu**
A: Ujistěte se, že jste upravovali pouze anglické markdown soubory v kořenových modulech, nikoliv přeložené verze.

**Q: Jak přidám nový jazyk?**
A: Podpora jazyků je spravována workflow co-op-translator. Otevřete issue k projednání přidání nových jazyků.

**Q: Ukázky kódu nefungují**

A: Ujistěte se, že jste postupovali podle pokynů pro nastavení v README konkrétní ukázky. Zkontrolujte, že máte nainstalované správné verze závislostí.

**Q: Obrázky se nezobrazují**
A: Ověřte, že cesty k obrázkům jsou relativní a používají lomítka. Obrázky by měly být v adresáři `images/` nebo `translated_images/` pro lokalizované verze.

### Výkonnostní úvahy

- Překladový proces může trvat několik minut
- Velké obrázky by měly být optimalizovány před nahráním
- Zachovejte jednotlivé markdown soubory zaměřené a rozumných rozměrů
- Používejte relativní odkazy pro lepší přenositelnost

### Správa projektu

Tento projekt se řídí zásadami otevřeného zdroje Microsoftu:
- Licence MIT pro kód a dokumentaci
- Microsoft Open Source Code of Conduct
- Pro příspěvky je vyžadována CLA
- Bezpečnostní problémy: řiďte se pokyny v SECURITY.md
- Podpora: Viz SUPPORT.md pro zdroje pomoci

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->