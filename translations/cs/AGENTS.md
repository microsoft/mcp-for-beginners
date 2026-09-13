# AGENTS.md

## Přehled projektu

**MCP pro začátečníky** je open-source vzdělávací kurikulum pro získání znalostí o Model Context Protocol (MCP) – standardizovaném rámci pro interakce mezi AI modely a klientskými aplikacemi. Tento repozitář poskytuje komplexní výukové materiály s praktickými příklady kódu v několika programovacích jazycích.

### Klíčové technologie

- **Programovací jazyky**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworky a SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databáze**: PostgreSQL s rozšířením pgvector
- **Cloudové platformy**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Nástroje pro build**: npm, Maven, pip, Cargo
- **Dokumentace**: Markdown s automatizovaným překladem do 48+ jazyků

### Architektura

- **11 základních modulů (00-11)**: Sekvenční učební plán od základů po pokročilá témata
- **Praktické laby**: Praktická cvičení s kompletními řešeními ve více jazycích
- **Ukázkové projekty**: Funkční implementace MCP serveru a klienta
- **Překladový systém**: Automatizovaný GitHub Actions workflow pro vícejazyčnou podporu
- **Obrázkové zdroje**: Centralizovaná složka s obrázky a jejich překlady

## Příkazy pro nastavení

Toto je repozitář zaměřený na dokumentaci. Většina nastavení probíhá v jednotlivých ukázkových projektech a labech.

### Nastavení repozitáře

```bash
# Naklonujte repozitář
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Práce s ukázkovými projekty

Ukázkové projekty jsou umístěny v:
- `03-GettingStarted/samples/` - Příklady specifické pro jazyk
- `03-GettingStarted/01-first-server/solution/` - První implementace serveru
- `03-GettingStarted/02-client/solution/` - Implementace klienta
- `11-MCPServerHandsOnLabs/` - Rozsáhlé laby integrace databází

Každý ukázkový projekt obsahuje vlastní instrukce pro nastavení:

#### Projekty v TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Projekty v Pythonu
```bash
cd <project-directory>
pip install -r requirements.txt
# nebo
pip install -e .
python main.py
```

#### Projekty v Javě
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Vývojový workflow

### MCP 7-28 připravenost

#### Kontrolní seznam připravenosti repozitáře

- [x] **Jasnost pro nové přispěvatele**: Tento soubor definuje účel repozitáře,
  strukturu, pravidla přispívání a cesty nastavení ukázek.
- [x] **Příkazy build/test/lint s přesnými flagy**:
  - Lint dokumentace repozitáře:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit vzoru odkazů v dokumentaci:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validace TypeScript ukázek:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validace Python ukázek:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validace Java ukázek:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Jeden realistický workflow, který může být MCP nástrojem**:
  `validate_curriculum_change`
- [x] **Vstupy/výstupy jsou explicitní** (viz specifikace níže).
- [x] **Oprávnění a režimy selhání jsou zdokumentovány** (viz specifikace níže).
- [x] **Testovatelnost CI je explicitní** (deterministické příkazy, explicitní
  návratové kódy a strojově čitelné výstupy).

#### Kandidátní MCP workflow nástroje: `validate_curriculum_change`

##### Cíl

Ověřit změny dokumentace kurikula a reprezentativní ukázkový kód
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

- Čtení souborů ve workspace a zápis artefaktů generovaných nástrojem (např. lint
  reporty, testovací logy) pouze; žádné zápisy do `translations/` nebo
  `translated_images/`.
- Spouštění lokálních shell příkazů.
- Volitelný přístup k síti pouze pro obnovu balíčků (`npm ci`,
  `python -m pip install`, řešení závislostí `mvn`).
- Žádné oprávnění k push, merge nebo úpravám `translations/` ani
  `translated_images/`.

##### Režimy selhání

- `E_NO_INPUT_PATHS`: prázdný `changed_paths`.
- `E_INVALID_PATH`: vstupní cesta uniká mimo kořen repozitáře.
- `E_LINT_FAILED`: markdown lint skončil s nenulovým kódem.
- `E_LINK_AUDIT_FAILED`: příkaz auditu odkazů skončil s nenulovým kódem.
- `E_SAMPLE_TEST_FAILED`: test/kompilace ukázky skončila s nenulovým kódem.
- `E_TIMEOUT`: příkaz překročil nastavený timeout.

##### Doporučená CI smlouva

Pro automatizaci validace nakonfigurujte CI job, který:

- Spouští se při pull requestech měnících `*.md`, ukázkový kód nebo tento soubor.
- Spouští přesné příkazy uvedené výše.
- Ukládá logy jako artefakty.
- Neuspěje job při jakémkoliv nenulovém návratovém kódu.

#### Pokud vypouštíte MCP server z tohoto repozitáře

- [ ] Přečtěte si finální changelog MCP `2026-07-28`:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Ověřte, že vybrané SDK vydání podporuje MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Odstraňte předpoklady o session a handshake; každý požadavek považujte za
  samostatný:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Posílejte hlavičky `Mcp-Method` a `Mcp-Name` pro raw HTTP požadavky:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Auditujte hardcoded chybové kódy (`missing resource` bylo přesunuto z `-32002` na `-32602`).
- [ ] Migrujte deprecated Roots, Sampling, Logging a Dynamic Client
  Registration:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migrujte z experimentálního Tasks API `2025-11-25`:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Zkontrolujte autorizaci pro posílení OAuth a OpenID Connect:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Struktura dokumentace

- **Moduly 00-11**: Základní obsah kurikula v sekvenčním pořadí
- **translations/**: Verze specifické pro jazyk (automaticky generované, neupravovat ručně)
- **translated_images/**: Lokalizované verze obrázků (automaticky generované)
- **images/**: Zdrojové obrázky a diagramy

### Provádění změn v dokumentaci

1. Editujte pouze anglické markdown soubory v kořenových modulech (00-11)
2. Pokud je potřeba, aktualizujte obrázky ve složce `images/`
3. GitHub Action co-op-translator automaticky vygeneruje překlady
4. Překlady jsou regenerovány při push do hlavní větve

### Práce s překlady

- **Automatický překlad**: GitHub Actions workflow se stará o všechny překlady
- **Neupravujte ručně** soubory ve složce `translations/`
- Metainformace o překladu jsou vloženy v každém přeloženém souboru
- Podporované jazyky: více než 48 včetně arabštiny, čínštiny, francouzštiny, němčiny, hindštiny, japonštiny, korejštiny, portugalštiny, ruštiny, španělštiny a dalších

## Instrukce pro testování

### Validace dokumentace

Jelikož jde zejména o repozitář dokumentace, testování se zaměřuje na:

1. **Audit vzoru odkazů**: Výpis Markdown odkazů k revizi

   ```bash
   # Vypsat odkazy v Markdownu (audit vzoru)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validace ukázek kódu**: Ověření, že se příklady kódu kompilují/spouští

   ```bash
   # Přejděte ke konkrétnímu vzorku a spusťte jeho testy
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown linting**: Kontrola formátovací konzistence

   ```bash
   # Použijte markdownlint, pokud je to potřeba
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testování ukázkových projektů

Každý vzorový příklad v jazyce obsahuje vlastní přístup k testování:

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

## Směrnice pro styl kódu

### Styl dokumentace

- Používejte jasný, pro začátečníky přívětivý jazyk
- Zařazujte příklady kódu ve více jazycích tam, kde to je vhodné
- Dodržujte osvědčené postupy pro markdown:
  - Používejte nadpisy v ATX stylu (`#` syntaxe)
  - Používejte ohraničené bloky kódu s určením jazyka
  - Zahrnujte popisné alt texty k obrázkům
  - Udržujte rozumnou délku řádků (není tvrdý limit, ale buďte rozumní)

### Styl ukázek kódu

#### TypeScript/JavaScript
- Používejte ES moduly (`import`/`export`)
- Dodržujte konvence přísného režimu TypeScriptu
- Zahrnujte typové anotace
- Cílová verze ES2022

#### Python
- Dodržujte stylové směrnice PEP 8
- Používejte typové náznaky tam, kde to má smysl
- Zahrnujte docstringy pro funkce a třídy
- Používejte moderní funkce Pythonu (3.8+)

#### Java
- Dodržujte konvence Spring Bootu
- Používejte funkce Javy 21
- Dodržujte standardní strukturu Maven projektů
- Zahrnujte Javadoc komentáře

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

Repozitář používá GitHub Pages nebo podobné řešení pro hostování dokumentace (pokud je relevantní). Změny v hlavní větvi spouštějí:

1. Překladový workflow (`.github/workflows/co-op-translator.yml`)
2. Automatizovaný překlad všech anglických markdown souborů
3. Lokální verze obrázků dle potřeby

### Není potřeba build proces

Tento repozitář obsahuje především markdown dokumentaci. Není potřeba žádný krok kompilace nebo build pro základní obsah kurikula.

### Nasazení ukázkových projektů

Jednotlivé ukázkové projekty mohou obsahovat vlastní instrukce pro nasazení:
- Viz `03-GettingStarted/09-deployment/` pro návod na nasazení MCP serveru
- Příklady nasazení Azure Container Apps v `11-MCPServerHandsOnLabs/`

## Pokyny pro přispívání

### Proces pull requestu

1. **Fork a klonování**: Vytvořte fork repozitáře a naklonujte si jej lokálně
2. **Vytvořte větev**: Používejte popisné názvy větví (např. `fix/typo-module-3`, `add/python-example`)
3. **Proveďte změny**: Editujte pouze anglické markdown soubory (ne překlady)
4. **Testujte lokálně**: Ověřte správné vykreslení markdownu
5. **Odešlete PR**: Použijte jasné názvy a popisy PR
6. **CLA**: Podepište Microsoft Contributor License Agreement, když budete vyzváni

### Formát názvu PR

Používejte jasné, popisné názvy:
- `[Module XX] Krátký popis` pro úpravy modulů
- `[Samples] Popis` pro změny ukázkového kódu
- `[Docs] Popis` pro obecné aktualizace dokumentace

### Co přispívat

- Opravy chyb v dokumentaci nebo ukázkách kódu
- Nové příklady kódu v dalších jazycích
- Upřesnění a vylepšení stávajícího obsahu
- Nové případové studie nebo praktické příklady
- Hlásení problémů s nejasným nebo chybným obsahem

### Co nedělat

- Needitujte přímo soubory ve složce `translations/`
- Neopakujte změny v `translated_images/`
- Nepřidávejte velké binární soubory bez předchozí domluvy
- Neměňte překladový workflow bez koordinace

## Další poznámky

### Údržba repozitáře

- **Changelog**: Všechny významné změny jsou dokumentovány v `changelog.md`
- **Studijní příručka**: Použijte `study_guide.md` pro přehled navigace kurikula
- **Issue šablony**: Používejte GitHub šablony pro hlášení bugů a žádosti o funkce
- **Kodex chování**: Všichni přispěvatelé musí dodržovat Microsoft Open Source Code of Conduct

### Učební cesta

Postupujte moduly v sekvenčním pořadí (00-11) pro optimální učení:
1. **00-02**: Základy (úvod, základní koncepty, bezpečnost)
2. **03**: Začínáme s praktickou implementací
3. **04-05**: Praktická implementace a pokročilá témata
4. **06-10**: Komunita, nejlepší praktiky a reálné aplikace
5. **11**: Rozsáhlé laby integrace databází (13 po sobě jdoucích labů)

### Podpůrné zdroje

- **Dokumentace**: https://modelcontextprotocol.io/
- **Specifikace**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Komunita**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord server
- **Související kurzy**: Viz README.md pro další Microsoft učební cesty

### Časté problémy a jejich řešení

**Otázka: Můj PR neprošel kontrolou překladu**
O: Ujistěte se, že jste měnili pouze anglické markdown soubory v kořenových modulech, ne přeložené verze.

**Otázka: Jak přidám nový jazyk?**
O: Podpora jazyků je řízena workflow co-op-translator. Otevřete issue pro diskusi o přidání nových jazyků.

**Otázka: Ukázky kódu nefungují**
O: Ujistěte se, že jste postupovali podle instrukcí v README konkrétní ukázky. Zkontrolujte, že máte správné verze závislostí.

**Otázka: Obrázky se nezobrazují**

A: Ověřte, že cesty k obrázkům jsou relativní a používají lomítka. Obrázky by měly být v adresáři `images/` nebo `translated_images/` pro lokalizované verze.

### Výkonové aspekty

- Překladový proces může trvat několik minut
- Velké obrázky by měly být optimalizovány před commitem
- Udržujte jednotlivé markdown soubory zaměřené a rozumné velikosti
- Používejte relativní odkazy pro lepší přenositelnost

### Správa projektu

Tento projekt se řídí open source praktikami Microsoftu:
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