# AGENTS.md

## Prehľad projektu

**MCP pre začiatočníkov** je open-source vzdelávací program na učenie Model Context Protocol (MCP) - štandardizovaného rámca pre interakcie medzi AI modelmi a klientskými aplikáciami. Tento repozitár poskytuje komplexné vzdelávacie materiály s praktickými ukážkami kódu v rôznych programovacích jazykoch.

### Kľúčové technológie

- **Programovacie jazyky**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworky a SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databázy**: PostgreSQL s rozšírením pgvector
- **Cloudové platformy**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Nástroje na zostavenie**: npm, Maven, pip, Cargo
- **Dokumentácia**: Markdown s automatizovaným prekladom do viacerých jazykov (48+ jazykov)

### Architektúra

- **11 hlavných modulov (00-11)**: Sekvenčná vzdelávacia cesta od základov po pokročilé témy
- **Praktické cvičenia**: Praktické úlohy s kompletným riešením kódu v rôznych jazykoch
- **Ukážkové projekty**: Funkčné implementácie MCP servera a klienta
- **Systém prekladov**: Automatizovaný workflow GitHub Actions na podporu viacerých jazykov
- **Obrazové materiály**: Centralizovaný adresár obrázkov s preloženými verziami

## Príkazy na nastavenie

Toto je repozitár zameraný na dokumentáciu. Väčšina nastavení sa vykonáva v rámci jednotlivých ukážkových projektov a cvičení.

### Nastavenie repozitára

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Práca s ukážkovými projektmi

Ukážkové projekty sa nachádzajú v:
- `03-GettingStarted/samples/` - Ukážky špecifické pre jazyk
- `03-GettingStarted/01-first-server/solution/` - Implementácie prvého servera
- `03-GettingStarted/02-client/solution/` - Implementácie klienta
- `11-MCPServerHandsOnLabs/` - Komplexné cvičenia na integráciu databázy

Každý ukážkový projekt obsahuje vlastné pokyny na nastavenie:

#### Projekty v TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Projekty v Python
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Projekty v Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Workflow vývoja

### Štruktúra dokumentácie

- **Moduly 00-11**: Obsah hlavného kurikula v sekvenčnom poradí
- **translations/**: Jazykovo špecifické verzie (automaticky generované, neupravovať priamo)
- **translated_images/**: Lokalizované verzie obrázkov (automaticky generované)
- **images/**: Zdrojové obrázky a diagramy

### Zmeny v dokumentácii

1. Upravujte iba anglické markdown súbory v hlavných adresároch modulov (00-11)
2. Aktualizujte obrázky v adresári `images/`, ak je to potrebné
3. GitHub Action s názvom co-op-translator automaticky vygeneruje preklady
4. Preklady sa regenerujú pri pushnutí do hlavnej vetvy

### Práca s prekladmi

- **Automatizovaný preklad**: Workflow GitHub Actions spracováva všetky preklady
- **NEUPRAVUJTE manuálne** súbory v adresári `translations/`
- Metaúdaje prekladu sú vložené v každom preloženom súbore
- Podporované jazyky: 48+ jazykov vrátane arabčiny, čínštiny, francúzštiny, nemčiny, hindčiny, japončiny, kórejčiny, portugalčiny, ruštiny, španielčiny a mnohých ďalších

## Pokyny na testovanie

### Validácia dokumentácie

Keďže ide primárne o repozitár dokumentácie, testovanie sa zameriava na:

1. **Validáciu odkazov**: Overte, že všetky interné odkazy fungujú
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Validáciu ukážok kódu**: Otestujte, či ukážky kódu sa dajú skompilovať/spustiť
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Lintovanie Markdown**: Skontrolujte konzistenciu formátovania
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Testovanie ukážkových projektov

Každá jazykovo špecifická ukážka obsahuje vlastný prístup k testovaniu:

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

## Štýlové pokyny pre kód

### Štýl dokumentácie

- Používajte jasný, priateľský jazyk pre začiatočníkov
- Zahrňte ukážky kódu vo viacerých jazykoch, kde je to možné
- Dodržiavajte najlepšie praktiky pre Markdown:
  - Používajte hlavičky štýlu ATX (`#` syntax)
  - Používajte ohraničené bloky kódu s identifikátormi jazykov
  - Zahrňte popisný alt text pre obrázky
  - Udržujte rozumnú dĺžku riadkov (bez pevného limitu, ale buďte rozumní)

### Štýl ukážok kódu

#### TypeScript/JavaScript
- Používajte ES moduly (`import`/`export`)
- Dodržiavajte konvencie prísneho režimu TypeScript
- Zahrňte anotácie typov
- Cieľová verzia ES2022

#### Python
- Dodržiavajte štýlové pokyny PEP 8
- Používajte typové anotácie, kde je to vhodné
- Zahrňte docstringy pre funkcie a triedy
- Používajte moderné funkcie Pythonu (3.8+)

#### Java
- Dodržiavajte konvencie Spring Boot
- Používajte funkcie Java 21
- Dodržiavajte štandardnú štruktúru projektu Maven
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

Repozitár používa GitHub Pages alebo podobné na hosting dokumentácie (ak je to relevantné). Zmeny v hlavnej vetve spúšťajú:

1. Workflow pre preklad (`.github/workflows/co-op-translator.yml`)
2. Automatizovaný preklad všetkých anglických markdown súborov
3. Lokalizáciu obrázkov podľa potreby

### Nie je potrebný proces zostavenia

Tento repozitár primárne obsahuje dokumentáciu v markdown. Nie je potrebná kompilácia ani krok zostavenia pre obsah hlavného kurikula.

### Nasadenie ukážkových projektov

Jednotlivé ukážkové projekty môžu mať pokyny na nasadenie:
- Pozrite si `03-GettingStarted/09-deployment/` pre pokyny na nasadenie MCP servera
- Príklady nasadenia Azure Container Apps v `11-MCPServerHandsOnLabs/`

## Pokyny pre prispievanie

### Proces Pull Request

1. **Fork a klonovanie**: Forknite repozitár a klonujte svoj fork lokálne
2. **Vytvorte vetvu**: Používajte popisné názvy vetiev (napr. `fix/typo-module-3`, `add/python-example`)
3. **Urobte zmeny**: Upravujte iba anglické markdown súbory (nie preklady)
4. **Testujte lokálne**: Overte, že markdown sa správne zobrazuje
5. **Odošlite PR**: Používajte jasné názvy a popisy PR
6. **CLA**: Podpíšte Microsoft Contributor License Agreement, keď budete vyzvaní

### Formát názvu PR

Používajte jasné, popisné názvy:
- `[Module XX] Stručný popis` pre zmeny špecifické pre modul
- `[Samples] Popis` pre zmeny ukážkového kódu
- `[Docs] Popis` pre všeobecné aktualizácie dokumentácie

### Čo prispievať

- Opravy chýb v dokumentácii alebo ukážkovom kóde
- Nové ukážky kódu v ďalších jazykoch
- Spresnenia a vylepšenia existujúceho obsahu
- Nové prípadové štúdie alebo praktické príklady
- Hlásenia problémov s nejasným alebo nesprávnym obsahom

### Čo NEROBIŤ

- Neupravujte priamo súbory v adresári `translations/`
- Neupravujte adresár `translated_images/`
- Nepridávajte veľké binárne súbory bez diskusie
- Nezmeňte súbory workflow prekladu bez koordinácie

## Dodatočné poznámky

### Údržba repozitára

- **Changelog**: Všetky významné zmeny sú zdokumentované v `changelog.md`
- **Študijný sprievodca**: Použite `study_guide.md` na prehľad navigácie kurikula
- **Šablóny problémov**: Použite šablóny GitHub problémov na hlásenie chýb a požiadaviek na funkcie
- **Kódex správania**: Všetci prispievatelia musia dodržiavať Microsoft Open Source Code of Conduct

### Vzdelávacia cesta

Nasledujte moduly v sekvenčnom poradí (00-11) pre optimálne učenie:
1. **00-02**: Základy (Úvod, Základné koncepty, Bezpečnosť)
2. **03**: Začiatok s praktickou implementáciou
3. **04-05**: Praktická implementácia a pokročilé témy
4. **06-10**: Komunita, najlepšie praktiky a aplikácie v reálnom svete
5. **11**: Komplexné cvičenia na integráciu databázy (13 sekvenčných cvičení)

### Podporné zdroje

- **Dokumentácia**: https://modelcontextprotocol.io/
- **Špecifikácia**: https://spec.modelcontextprotocol.io/
- **Komunita**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Discord server Microsoft Azure AI Foundry
- **Súvisiace kurzy**: Pozrite si README.md pre ďalšie vzdelávacie cesty Microsoftu

### Bežné problémy

**Otázka: Môj PR zlyháva pri kontrole prekladu**
Odpoveď: Uistite sa, že ste upravili iba anglické markdown súbory v hlavných adresároch modulov, nie preložené verzie.

**Otázka: Ako pridám nový jazyk?**
Odpoveď: Podpora jazykov je spravovaná cez workflow co-op-translator. Otvorte problém na diskusiu o pridávaní nových jazykov.

**Otázka: Ukážky kódu nefungujú**
Odpoveď: Uistite sa, že ste dodržali pokyny na nastavenie v README konkrétnej ukážky. Skontrolujte, či máte nainštalované správne verzie závislostí.

**Otázka: Obrázky sa nezobrazujú**
Odpoveď: Overte, že cesty k obrázkom sú relatívne a používajú lomky. Obrázky by mali byť v adresári `images/` alebo `translated_images/` pre lokalizované verzie.

### Výkonnostné úvahy

- Workflow prekladu môže trvať niekoľko minút na dokončenie
- Veľké obrázky by mali byť optimalizované pred commitom
- Udržujte jednotlivé markdown súbory zamerané a rozumne veľké
- Používajte relatívne odkazy pre lepšiu prenosnosť

### Správa projektu

Tento projekt dodržiava praktiky open source od Microsoftu:
- MIT licencia pre kód a dokumentáciu
- Microsoft Open Source Code of Conduct
- CLA požadované pre príspevky
- Bezpečnostné problémy: Dodržiavajte pokyny v SECURITY.md
- Podpora: Pozrite si SUPPORT.md pre zdroje pomoci

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.