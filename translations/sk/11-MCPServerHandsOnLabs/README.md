# 🚀 MCP Server s PostgreSQL - Kompletný návod na učenie

## 🧠 Prehľad učebnej cesty integrácie MCP databázy

Tento komplexný návod na učenie vás naučí, ako vytvoriť produkčne pripravené **Model Context Protocol (MCP) servery**, ktoré sa integrujú s databázami prostredníctvom praktickej implementácie maloobchodnej analytiky. Naučíte sa podnikové vzory vrátane **Row Level Security (RLS)**, **sémantického vyhľadávania**, **integrácie Azure AI** a **prístupu k dátam pre viac klientov**.

Či už ste backend vývojár, AI inžinier alebo dátový architekt, tento návod ponúka štruktúrované učenie s reálnymi príkladmi a praktickými cvičeniami, ktoré vás prevedú nasledujúcim MCP serverom https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Oficiálne MCP zdroje

- 📘 [MCP Dokumentácia](https://modelcontextprotocol.io/) – Podrobné návody a používateľské príručky
- 📜 [MCP Špecifikácia (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Architektúra protokolu a technické odkazy
- 🧑‍💻 [MCP GitHub Repozitár](https://github.com/modelcontextprotocol) – Open-source SDK, nástroje a príklady kódu
- 🌐 [MCP Komunita](https://github.com/orgs/modelcontextprotocol/discussions) – Zapojte sa do diskusií a prispejte do komunity
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Najlepšie bezpečnostné postupy a mitigácie rizík


## 🧭 Učebná cesta integrácie MCP databázy

### 📚 Kompletná štruktúra učenia pre https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Laboratórium | Téma | Popis | Odkaz |
|--------|-------|-------------|------|
| **Laboratóriá 1-3: Základy** | | | |
| 00 | [Úvod do integrácie MCP databázy](./00-Introduction/README.md) | Prehľad MCP s integráciou databázy a prípad použitia maloobchodnej analytiky | [Začať tu](./00-Introduction/README.md) |
| 01 | [Základné koncepty architektúry](./01-Architecture/README.md) | Pochopenie architektúry MCP servera, vrstiev databázy a bezpečnostných vzorov | [Naučiť sa](./01-Architecture/README.md) |
| 02 | [Bezpečnosť a multi-tenancy](./02-Security/README.md) | Row Level Security, autentifikácia a prístup k dátam pre viac klientov | [Naučiť sa](./02-Security/README.md) |
| 03 | [Nastavenie prostredia](./03-Setup/README.md) | Nastavenie vývojového prostredia, Docker, Azure zdroje | [Nastaviť](./03-Setup/README.md) |
| **Laboratóriá 4-6: Budovanie MCP servera** | | | |
| 04 | [Návrh databázy a schéma](./04-Database/README.md) | Nastavenie PostgreSQL, návrh maloobchodnej schémy a ukážkové dáta | [Budovať](./04-Database/README.md) |
| 05 | [Implementácia MCP servera](./05-MCP-Server/README.md) | Budovanie FastMCP servera s integráciou databázy | [Budovať](./05-MCP-Server/README.md) |
| 06 | [Vývoj nástrojov](./06-Tools/README.md) | Vytváranie nástrojov na dopytovanie databázy a introspekciu schémy | [Budovať](./06-Tools/README.md) |
| **Laboratóriá 7-9: Pokročilé funkcie** | | | |
| 07 | [Integrácia sémantického vyhľadávania](./07-Semantic-Search/README.md) | Implementácia vektorových vložení s Azure OpenAI a pgvector | [Pokročiť](./07-Semantic-Search/README.md) |
| 08 | [Testovanie a ladenie](./08-Testing/README.md) | Testovacie stratégie, nástroje na ladenie a validačné prístupy | [Testovať](./08-Testing/README.md) |
| 09 | [Integrácia VS Code](./09-VS-Code/README.md) | Konfigurácia VS Code pre integráciu MCP a používanie AI chatu | [Integrovať](./09-VS-Code/README.md) |
| **Laboratóriá 10-12: Produkcia a najlepšie praktiky** | | | |
| 10 | [Strategie nasadenia](./10-Deployment/README.md) | Nasadenie pomocou Docker, Azure Container Apps a úvahy o škálovaní | [Nasadiť](./10-Deployment/README.md) |
| 11 | [Monitorovanie a pozorovateľnosť](./11-Monitoring/README.md) | Application Insights, logovanie, monitorovanie výkonu | [Monitorovať](./11-Monitoring/README.md) |
| 12 | [Najlepšie praktiky a optimalizácia](./12-Best-Practices/README.md) | Optimalizácia výkonu, zabezpečenie a tipy pre produkciu | [Optimalizovať](./12-Best-Practices/README.md) |

### 💻 Čo vybudujete

Na konci tejto učebnej cesty budete mať vybudovaný kompletný **Zava Retail Analytics MCP server**, ktorý obsahuje:

- **Viactabuľkovú maloobchodnú databázu** so zákazníckymi objednávkami, produktmi a zásobami
- **Row Level Security** pre izoláciu dát na úrovni predajní
- **Sémantické vyhľadávanie produktov** pomocou Azure OpenAI vložení
- **Integráciu VS Code AI Chatu** pre dopyty v prirodzenom jazyku
- **Produkčné nasadenie** s Dockerom a Azure
- **Komplexné monitorovanie** pomocou Application Insights

## 🎯 Predpoklady na učenie

Aby ste z tejto učebnej cesty vytiahli maximum, mali by ste mať:

- **Skúsenosti s programovaním**: Znalosť Pythonu (preferované) alebo podobných jazykov
- **Znalosti databáz**: Základné porozumenie SQL a relačných databáz
- **Koncepty API**: Pochopenie REST API a HTTP konceptov
- **Vývojové nástroje**: Skúsenosti s príkazovým riadkom, Gitom a editorom kódu
- **Základy cloudu**: (Voliteľné) Základné znalosti Azure alebo podobných cloud platforiem
- **Znalosť Dockeru**: (Voliteľné) Porozumenie konceptom kontajnerizácie

### Povinné nástroje

- **Docker Desktop** - Na spustenie PostgreSQL a MCP servera
- **Azure CLI** - Na nasadenie cloudových zdrojov
- **VS Code** - Na vývoj a integráciu MCP
- **Git** - Na správu verzií
- **Python 3.8+** - Na vývoj MCP servera

## 📚 Študijný sprievodca a zdroje

Táto učebná cesta obsahuje komplexné zdroje, ktoré vám pomôžu efektívne sa orientovať:

### Študijný sprievodca

Každé laboratórium obsahuje:
- **Jasné ciele učenia** - Čo dosiahnete
- **Krok za krokom návody** - Podrobné inštrukcie na implementáciu
- **Príklady kódu** - Funkčné ukážky s vysvetlením
- **Cvičenia** - Príležitosti pre praktický nácvik
- **Riešenie problémov** - Bežné problémy a riešenia
- **Ďalšie zdroje** - Dodatočné materiály na štúdium a objavovanie

### Kontrola predpokladov

Pred začatím každého laboratória nájdete:
- **Povinné znalosti** - Čo by ste mali vedieť vopred
- **Overenie nastavenia** - Ako overiť prostredie
- **Odhad času** - Očakávaný čas dokončenia
- **Výsledky učenia** - Čo budete vedieť po ukončení

### Odporúčané učebné cesty

Vyberte si cestu podľa vašej úrovne skúseností:

#### 🟢 **Začiatočnícka cesta** (Nováčik v MCP)
1. Najprv dokončite lekcie 0-10 z [MCP pre začiatočníkov](https://aka.ms/mcp-for-beginners)
2. Dokončite laboratóriá 00-03 na prehĺbenie základov
3. Nasledujte laboratóriá 04-06 pre praktické budovanie
4. Vyskúšajte laboratóriá 07-09 pre praktické využitie

#### 🟡 **Stredne pokročilá cesta** (S istými skúsenosťami s MCP)
1. Prezrite si laboratóriá 00-01 pre koncepty databáz
2. Zamerajte sa na laboratóriá 02-06 pre implementáciu
3. Ponorte sa hlboko do laboratórií 07-12 pre pokročilé funkcie

#### 🔴 **Pokročilá cesta** (Skúsený v MCP)
1. Rýchlo si prečítajte laboratóriá 00-03 pre kontext
2. Zamerajte sa na laboratóriá 04-09 pre integráciu databázy
3. Koncentrujte sa na laboratóriá 10-12 pre produkčné nasadenie

## 🛠️ Ako efektívne používať túto učebnú cestu

### Sekvenčné učenie (odporúčané)

Prejdite laboratóriá v poradí pre komplexné pochopenie:

1. **Prečítajte si prehľad** - Pochopte, čo sa naučíte
2. **Skontrolujte predpoklady** - Uistite sa, že máte požadované znalosti
3. **Nasledujte návody krok za krokom** - Implementujte počas učenia
4. **Dokončite cvičenia** - Posilnite svoje pochopenie
5. **Prezrite si kľúčové závery** - Upevnite výsledky učenia

### Cielené učenie

Ak potrebujete konkrétne zručnosti:

- **Integrácia databázy**: Zamerajte sa na laboratóriá 04-06
- **Implementácia bezpečnosti**: Koncentrujte sa na laboratóriá 02, 08, 12
- **AI/Sémantické vyhľadávanie**: Ponorte sa do laboratória 07
- **Produkčné nasadenie**: Študujte laboratóriá 10-12

### Praktický nácvik

Každé laboratórium obsahuje:
- **Funkčné príklady kódu** - Kopírujte, upravujte a experimentujte
- **Reálne scenáre** - Praktické prípady použitia maloobchodnej analytiky
- **Postupná zložitosť** - Budovanie od jednoduchého po pokročilé
- **Overovacie kroky** - Overte, že vaša implementácia funguje

## 🌟 Komunita a podpora

### Získajte pomoc

- **Azure AI Discord**: [Pripojte sa pre odbornú podporu](https://discord.com/invite/ByRwuEEgH4)
- **GitHub Repozitár a ukážka implementácie**: [Ukážka nasadenia a zdroje](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP Komunita**: [Pripojte sa ku širším MCP diskusiám](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Pripravení začať?

Začnite svoju cestu s **[Lab 00: Úvod do integrácie MCP databázy](./00-Introduction/README.md)**

---

*Ovládnite budovanie produkčne pripravených MCP serverov s integráciou databázy prostredníctvom tejto komplexnej praktickej učebnej skúsenosti.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->