# AGENTS.md

## Přehled projektu

**MCP pro začátečníky** je open-source vzdělávací program zaměřený na učení Model Context Protocol (MCP) - standardizovaného rámce pro interakce mezi AI modely a klientskými aplikacemi. Tento repozitář poskytuje komplexní výukové materiály s praktickými příklady kódu v různých programovacích jazycích.

### Klíčové technologie

- **Programovací jazyky**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworky a SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databáze**: PostgreSQL s rozšířením pgvector
- **Cloudové platformy**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Nástroje pro sestavení**: npm, Maven, pip, Cargo
- **Dokumentace**: Markdown s automatizovaným překladem do více jazyků (48+ jazyků)

### Architektura

- **11 základních modulů (00-11)**: Sekvenční učební cesta od základů po pokročilá témata
- **Praktické laboratoře**: Praktická cvičení s kompletními řešeními v různých jazycích
- **Ukázkové projekty**: Funkční implementace MCP serveru a klienta
- **Systém překladu**: Automatizovaný workflow GitHub Actions pro podporu více jazyků
- **Obrazové materiály**: Centralizovaný adresář obrázků s přeloženými verzemi

## Příkazy pro nastavení

Tento repozitář je zaměřen na dokumentaci. Většina nastavení probíhá v jednotlivých ukázkových projektech a laboratořích.

### Nastavení repozitáře

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Práce s ukázkovými projekty

Ukázkové projekty se nacházejí v:
- `03-GettingStarted/samples/` - Příklady specifické pro jednotlivé jazyky
- `03-GettingStarted/01-first-server/solution/` - Implementace prvního serveru
- `03-GettingStarted/02-client/solution/` - Implementace klienta
- `11-MCPServerHandsOnLabs/` - Laboratoře s komplexní integrací databáze

Každý ukázkový projekt obsahuje vlastní pokyny k nastavení:

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
# or
pip install -e .
python main.py
```

#### Projekty v Javě
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Workflow vývoje

### Struktura dokumentace

- **Moduly 00-11**: Základní obsah učebního programu v sekvenčním pořadí
- **translations/**: Jazykové verze (automaticky generované, neupravovat přímo)
- **translated_images/**: Lokalizované verze obrázků (automaticky generované)
- **images/**: Zdrojové obrázky a diagramy

### Změny v dokumentaci

1. Upravujte pouze anglické markdown soubory v hlavních adresářích modulů (00-11)
2. Aktualizujte obrázky v adresáři `images/`, pokud je to potřeba
3. GitHub Action co-op-translator automaticky vygeneruje překlady
4. Překlady se regenerují při každém push na hlavní větev

### Práce s překlady

- **Automatizovaný překlad**: Workflow GitHub Actions zajišťuje všechny překlady
- **NEUPRAVUJTE** soubory v adresáři `translations/`
- Metadata překladu jsou vložena do každého přeloženého souboru
- Podporované jazyky: 48+ jazyků včetně arabštiny, čínštiny, francouzštiny, němčiny, hindštiny, japonštiny, korejštiny, portugalštiny, ruštiny, španělštiny a dalších

## Pokyny k testování

### Validace dokumentace

Protože se jedná primárně o dokumentační repozitář, testování se zaměřuje na:

1. **Validace odkazů**: Ověřte, že všechny interní odkazy fungují
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Validace ukázek kódu**: Otestujte, zda ukázky kódu lze zkompilovat/spustit
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Linting Markdownu**: Zkontrolujte konzistenci formátování
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Testování ukázkových projektů

Každý ukázkový projekt specifický pro jazyk obsahuje vlastní přístup k testování:

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

## Pokyny ke stylu kódu

### Styl dokumentace

- Používejte jasný, srozumitelný jazyk vhodný pro začátečníky
- Zahrňte ukázky kódu v různých jazycích, kde je to možné
- Dodržujte nejlepší praktiky pro markdown:
  - Používejte hlavičky ve stylu ATX (`#` syntaxe)
  - Používejte ohraničené bloky kódu s identifikátory jazyků
  - Zahrňte popisný alt text pro obrázky
  - Udržujte rozumnou délku řádků (bez pevného limitu, ale buďte rozumní)

### Styl ukázek kódu

#### TypeScript/JavaScript
- Používejte ES moduly (`import`/`export`)
- Dodržujte konvence přísného režimu TypeScriptu
- Zahrňte anotace typů
- Cílujte na ES2022

#### Python
- Dodržujte pokyny stylu PEP 8
- Používejte typové nápovědy, kde je to vhodné
- Zahrňte docstringy pro funkce a třídy
- Používejte moderní funkce Pythonu (3.8+)

#### Java
- Dodržujte konvence Spring Boot
- Používejte funkce Java 21
- Dodržujte standardní strukturu projektu Maven
- Zahrňte komentáře Javadoc

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

Repozitář využívá GitHub Pages nebo podobné pro hosting dokumentace (pokud je to relevantní). Změny v hlavní větvi spouštějí:

1. Workflow překladu (`.github/workflows/co-op-translator.yml`)
2. Automatizovaný překlad všech anglických markdown souborů
3. Lokalizaci obrázků podle potřeby

### Není potřeba proces sestavení

Tento repozitář primárně obsahuje dokumentaci v markdownu. Pro základní obsah učebního programu není potřeba žádná kompilace nebo krok sestavení.

### Nasazení ukázkových projektů

Jednotlivé ukázkové projekty mohou mít pokyny k nasazení:
- Viz `03-GettingStarted/09-deployment/` pro pokyny k nasazení MCP serveru
- Příklady nasazení Azure Container Apps v `11-MCPServerHandsOnLabs/`

## Pokyny pro přispěvatele

### Proces pull requestu

1. **Fork a klonování**: Forkněte repozitář a klonujte svůj fork lokálně
2. **Vytvořte větev**: Používejte popisné názvy větví (např. `fix/typo-module-3`, `add/python-example`)
3. **Proveďte změny**: Upravujte pouze anglické markdown soubory (ne překlady)
4. **Otestujte lokálně**: Ověřte, že markdown se správně vykresluje
5. **Odešlete PR**: Používejte jasné názvy a popisy PR
6. **CLA**: Podepište Microsoft Contributor License Agreement, když budete vyzváni

### Formát názvu PR

Používejte jasné, popisné názvy:
- `[Module XX] Stručný popis` pro změny specifické pro moduly
- `[Samples] Popis` pro změny ukázkového kódu
- `[Docs] Popis` pro obecné aktualizace dokumentace

### Co přispívat

- Opravy chyb v dokumentaci nebo ukázkách kódu
- Nové ukázky kódu v dalších jazycích
- Upřesnění a vylepšení stávajícího obsahu
- Nové případové studie nebo praktické příklady
- Hlásit problémy s nejasným nebo nesprávným obsahem

### Co NEDĚLAT

- Neupravujte přímo soubory v adresáři `translations/`
- Neupravujte adresář `translated_images/`
- Nepřidávejte velké binární soubory bez předchozí diskuse
- Neměňte soubory workflow překladu bez koordinace

## Další poznámky

### Údržba repozitáře

- **Changelog**: Všechny významné změny jsou dokumentovány v `changelog.md`
- **Studijní průvodce**: Použijte `study_guide.md` pro přehled navigace učebním programem
- **Šablony problémů**: Použijte šablony GitHub pro hlášení chyb a požadavky na funkce
- **Kodex chování**: Všichni přispěvatelé musí dodržovat Microsoft Open Source Code of Conduct

### Učební cesta

Postupujte podle modulů v sekvenčním pořadí (00-11) pro optimální učení:
1. **00-02**: Základy (Úvod, základní koncepty, bezpečnost)
2. **03**: Začínáme s praktickou implementací
3. **04-05**: Praktická implementace a pokročilá témata
4. **06-10**: Komunita, nejlepší praktiky a aplikace v reálném světě
5. **11**: Komplexní laboratoře integrace databáze (13 sekvenčních laboratoří)

### Zdroje podpory

- **Dokumentace**: https://modelcontextprotocol.io/
- **Specifikace**: https://spec.modelcontextprotocol.io/
- **Komunita**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Discord server Microsoft Azure AI Foundry
- **Související kurzy**: Viz README.md pro další vzdělávací programy Microsoftu

### Časté problémy

**Q: Můj PR neprošel kontrolou překladu**
A: Ujistěte se, že jste upravili pouze anglické markdown soubory v hlavních adresářích modulů, nikoli přeložené verze.

**Q: Jak přidám nový jazyk?**
A: Podpora jazyků je spravována prostřednictvím workflow co-op-translator. Otevřete problém a diskutujte o přidání nových jazyků.

**Q: Ukázky kódu nefungují**
A: Ujistěte se, že jste postupovali podle pokynů k nastavení v konkrétním README ukázky. Zkontrolujte, zda máte nainstalované správné verze závislostí.

**Q: Obrázky se nezobrazují**
A: Ověřte, že cesty k obrázkům jsou relativní a používají dopředné lomítka. Obrázky by měly být v adresáři `images/` nebo `translated_images/` pro lokalizované verze.

### Výkonnostní úvahy

- Workflow překladu může trvat několik minut
- Velké obrázky by měly být optimalizovány před commitováním
- Udržujte jednotlivé markdown soubory zaměřené a rozumně velké
- Používejte relativní odkazy pro lepší přenositelnost

### Řízení projektu

Tento projekt dodržuje praktiky open source Microsoftu:
- MIT License pro kód a dokumentaci
- Microsoft Open Source Code of Conduct
- CLA vyžadováno pro přispěvatele
- Bezpečnostní problémy: Dodržujte pokyny v SECURITY.md
- Podpora: Viz SUPPORT.md pro zdroje pomoci

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.