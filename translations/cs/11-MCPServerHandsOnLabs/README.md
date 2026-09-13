# 🚀 MCP server s PostgreSQL – Kompletní průvodce učením

## 🧠 Přehled učební cesty integrace databáze MCP

Tento komplexní učební průvodce vás naučí, jak postavit produkčně připravené **server MCP (Model Context Protocol)** integrované s databázemi prostřednictvím praktické implementace analytiky maloobchodu. Naučíte se podnikové vzory včetně **Row Level Security (RLS)**, **sémantického vyhledávání**, **integrace Azure AI** a **víceuživatelského přístupu k datům**.

Ať už jste backendový vývojář, AI inženýr nebo datový architekt, tento průvodce poskytuje strukturované učení s reálnými příklady a praktickými cvičeními, která vás provedou následujícím serverem MCP https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Oficiální zdroje MCP

- 📘 [Dokumentace MCP](https://modelcontextprotocol.io/) – Detailní tutoriály a uživatelské příručky
- 📜 [Specifikace MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Architektura protokolu a technické reference
- 🧑‍💻 [MCP GitHub repository](https://github.com/modelcontextprotocol) – Open-source SDK, nástroje a ukázkový kód
- 🌐 [Komunita MCP](https://github.com/orgs/modelcontextprotocol/discussions) – Přidejte se k diskuzím a přispívejte komunitě
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Nejlepší bezpečnostní postupy a mitigace rizik


## 🧭 Učební cesta integrace databáze MCP

### 📚 Kompletní struktura učení pro https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Laboratoř | Téma | Popis | Odkaz |
|--------|-------|-------------|------|
| **Laboratoře 1-3: Základy** | | | |
| 00 | [Úvod do integrace databáze MCP](./00-Introduction/README.md) | Přehled MCP s integrací databáze a případem použití maloobchodní analytiky | [Začít zde](./00-Introduction/README.md) |
| 01 | [Základní architektonické koncepty](./01-Architecture/README.md) | Porozumění architektuře serveru MCP, databázovým vrstvám a bezpečnostním vzorům | [Naučit se](./01-Architecture/README.md) |
| 02 | [Bezpečnost a víceuživatelský přístup](./02-Security/README.md) | Row Level Security, autentizace a přístup k datům více zákazníků | [Naučit se](./02-Security/README.md) |
| 03 | [Nastavení prostředí](./03-Setup/README.md) | Nastavení vývojového prostředí, Docker, Azure zdroje | [Nastavit](./03-Setup/README.md) |
| **Laboratoře 4-6: Budování MCP serveru** | | | |
| 04 | [Návrh databáze a schéma](./04-Database/README.md) | Nastavení PostgreSQL, návrh maloobchodního schématu a ukázková data | [Vytvořit](./04-Database/README.md) |
| 05 | [Implementace MCP serveru](./05-MCP-Server/README.md) | Budování FastMCP serveru s integrací databáze | [Vytvořit](./05-MCP-Server/README.md) |
| 06 | [Vývoj nástrojů](./06-Tools/README.md) | Vytváření nástrojů pro dotazy do databáze a introspekce schématu | [Vytvořit](./06-Tools/README.md) |
| **Laboratoře 7-9: Pokročilé funkce** | | | |
| 07 | [Integrace sémantického vyhledávání](./07-Semantic-Search/README.md) | Implementace vektorových embeddingů s Azure OpenAI a pgvector | [Pokročilé](./07-Semantic-Search/README.md) |
| 08 | [Testování a ladění](./08-Testing/README.md) | Strategie testování, nástroje pro ladění a přístupy k validaci | [Testovat](./08-Testing/README.md) |
| 09 | [Integrace s VS Code](./09-VS-Code/README.md) | Konfigurace integrace MCP ve VS Code a využití AI chatu | [Integrovat](./09-VS-Code/README.md) |
| **Laboratoře 10-12: Produkce a nejlepší praxe** | | | |
| 10 | [Strategie nasazení](./10-Deployment/README.md) | Nasazení pomocí Dockeru, Azure Container Apps a škálování | [Nasadit](./10-Deployment/README.md) |
| 11 | [Monitoring a observabilita](./11-Monitoring/README.md) | Application Insights, logování, monitorování výkonu | [Monitorovat](./11-Monitoring/README.md) |
| 12 | [Nejlepší praxe a optimalizace](./12-Best-Practices/README.md) | Optimalizace výkonu, zabezpečení a tipy pro produkci | [Optimalizovat](./12-Best-Practices/README.md) |

### 💻 Co postavíte

Na konci této učební cesty budete mít postavený kompletní **Zava Retail Analytics MCP server** obsahující:

- **Více-tabulkovou maloobchodní databázi** s objednávkami zákazníků, produkty a skladovými zásobami
- **Row Level Security** pro izolaci dat podle prodejen
- **Sémantické vyhledávání produktů** pomocí Azure OpenAI embeddingů
- **Integraci VS Code AI chatu** pro dotazy v přirozeném jazyce
- **Produkční nasazení** s Dockerem a Azure
- **Komplexní monitoring** pomocí Application Insights

## 🎯 Předpoklady pro učení

Aby vám tato učební cesta co nejvíce pomohla, měli byste mít:

- **Zkušenosti s programováním**: Znalost Pythonu (preferováno) nebo podobných jazyků
- **Znalosti databází**: Základní porozumění SQL a relačním databázím
- **Koncepty API**: Porozumění REST API a HTTP principům
- **Vývojové nástroje**: Zkušenost s příkazovou řádkou, Gitem a editory kódu
- **Základy cloudu**: (volitelné) Základní znalost Azure nebo podobných cloudových platforem
- **Znalost Dockeru**: (volitelné) Porozumění kontejnerizaci

### Požadované nástroje

- **Docker Desktop** – Pro spuštění PostgreSQL a MCP serveru
- **Azure CLI** – Pro nasazení cloudových zdrojů
- **VS Code** – Pro vývoj a integraci MCP
- **Git** – Pro správu verzí
- **Python 3.8+** – Pro vývoj MCP serveru

## 📚 Studijní průvodce a zdroje

Tato učební cesta obsahuje komplexní zdroje, které vám pomohou efektivně se zorientovat:

### Studijní průvodce

Každá laboratoř obsahuje:
- **Jasné učební cíle** – Co dosáhnete
- **Krok za krokem instrukce** – Podrobné průvodce implementací
- **Ukázky kódu** – Funkční příklady s vysvětlením
- **Cvičení** – Možnosti praktického procvičování
- **Průvodce řešením problémů** – Časté problémy a řešení
- **Další zdroje** – Další čtení a prohlubování znalostí

### Kontrola předpokladů

Před zahájením každé laboratoře najdete:
- **Požadované znalosti** – Co byste měli znát předem
- **Validace nastavení** – Jak ověřit své prostředí
- **Odhady času** – Očekávaná doba dokončení
- **Výsledky učení** – Co budete umět po dokončení

### Doporučené učební cesty

Vyberte si cestu podle své úrovně zkušeností:

#### 🟢 **Začátečnická cesta** (nováček MCP)
1. Nejprve si dokončete 0-10 modulu [MCP pro začátečníky](https://aka.ms/mcp-for-beginners)
2. Dokončete laboratoře 00-03 pro posílení základů
3. Následujte laboratoře 04-06 pro praktické budování
4. Vyzkoušejte laboratoře 07-09 pro praktické použití

#### 🟡 **Středně pokročilá cesta** (nějaké zkušenosti s MCP)
1. Prohlédněte si laboratoře 00-01 pro databázové koncepty
2. Zaměřte se na laboratoře 02-06 pro implementaci
3. Ponořte se hluboko do laboratoří 07-12 pro pokročilé funkce

#### 🔴 **Pokročilá cesta** (zkušený s MCP)
1. Prohlédněte si laboratoře 00-03 pro kontext
2. Zaměřte se na laboratoře 04-09 pro integraci databáze
3. Soustřeďte se na laboratoře 10-12 pro produkční nasazení

## 🛠️ Jak efektivně používat tuto učební cestu

### Sekvenční učení (doporučené)

Projděte laboratoře v pořadí pro komplexní pochopení:

1. **Přečtěte si přehled** – Pochopte, co se naučíte
2. **Zkontrolujte předpoklady** – Ujistěte se, že máte potřebné znalosti
3. **Následujte průvodce krok za krokem** – Implementujte při učení
4. **Dokončete cvičení** – Posilte své znalosti
5. **Zopakujte klíčové poznatky** – Upevněte výsledky učení

### Cílené učení

Pokud potřebujete specifické dovednosti:

- **Integrace databáze**: Zaměřte se na laboratoře 04-06
- **Implementace zabezpečení**: Soustřeďte se na laboratoře 02, 08, 12
- **AI/sémantické vyhledávání**: Dopodrobna laboratoř 07
- **Produkční nasazení**: Studujte laboratoře 10-12

### Praktické cvičení

Každá laboratoř obsahuje:
- **Funkční ukázky kódu** – Kopírujte, upravujte a experimentujte
- **Reálné scénáře** – Praktické případy použití maloobchodní analytiky
- **Postupnou složitost** – Budování od jednoduchých po pokročilé
- **Validace** – Ověřte, že vaše implementace funguje

## 🌟 Komunita a podpora

### Získejte pomoc

- **Azure AI Discord**: [Připojte se pro odbornou podporu](https://discord.com/invite/ByRwuEEgH4)
- **GitHub repozitář a ukázka implementace**: [Ukázka nasazení a zdroje](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **Komunita MCP**: [Přidejte se k širším diskuzím MCP](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Připraven začít?

Začněte svou cestu s **[Laboratoří 00: Úvod do integrace databáze MCP](./00-Introduction/README.md)**

---

*Ovládněte tvorbu produkčně připravených MCP serverů s integrací databází díky tomuto komplexnímu, praktickému vzdělávacímu zážitku.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->