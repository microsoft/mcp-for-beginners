# 🚀 MCP Server s PostgreSQL - Kompletný sprievodca učením

## 🧠 Prehľad učebnej cesty integrácie MCP databázy

Tento komplexný sprievodca učením vás naučí, ako vytvoriť produkčne pripravené **Model Context Protocol (MCP) servery**, ktoré sa integrujú s databázami prostredníctvom praktickej implementácie maloobchodnej analytiky. Naučíte sa vzory na podnikovej úrovni vrátane **Row Level Security (RLS)**, **semantického vyhľadávania**, **integrácie Azure AI** a **prístupu k dátam pre viacerých nájomcov**.

Či už ste backendový vývojár, AI inžinier alebo dátový architekt, tento sprievodca poskytuje štruktúrované učenie s príkladmi z reálneho sveta a praktickými cvičeniami, ktoré vás prevedú MCP serverom https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Oficiálne MCP zdroje

- 📘 [MCP Dokumentácia](https://modelcontextprotocol.io/) – Podrobné tutoriály a používateľské príručky
- 📜 [MCP Špecifikácia](https://modelcontextprotocol.io/docs/) – Architektúra protokolu a technické referencie
- 🧑‍💻 [MCP GitHub Repository](https://github.com/modelcontextprotocol) – Open-source SDK, nástroje a ukážky kódu
- 🌐 [MCP Komunita](https://github.com/orgs/modelcontextprotocol/discussions) – Pripojte sa k diskusiám a prispievajte do komunity

## 🧭 Učebná cesta integrácie MCP databázy

### 📚 Kompletná štruktúra učenia pre https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Lab | Téma | Popis | Odkaz |
|--------|-------|-------------|------|
| **Lab 1-3: Základy** | | | |
| 00 | [Úvod do integrácie MCP databázy](./00-Introduction/README.md) | Prehľad MCP s integráciou databázy a prípad použitia maloobchodnej analytiky | [Začnite tu](./00-Introduction/README.md) |
| 01 | [Základné koncepty architektúry](./01-Architecture/README.md) | Porozumenie architektúre MCP servera, databázovým vrstvám a bezpečnostným vzorom | [Učte sa](./01-Architecture/README.md) |
| 02 | [Bezpečnosť a multi-tenancy](./02-Security/README.md) | Row Level Security, autentifikácia a prístup k dátam pre viacerých nájomcov | [Učte sa](./02-Security/README.md) |
| 03 | [Nastavenie prostredia](./03-Setup/README.md) | Nastavenie vývojového prostredia, Docker, Azure zdroje | [Nastavte](./03-Setup/README.md) |
| **Lab 4-6: Budovanie MCP servera** | | | |
| 04 | [Návrh databázy a schéma](./04-Database/README.md) | Nastavenie PostgreSQL, návrh maloobchodnej schémy a ukážkové dáta | [Budujte](./04-Database/README.md) |
| 05 | [Implementácia MCP servera](./05-MCP-Server/README.md) | Budovanie FastMCP servera s integráciou databázy | [Budujte](./05-MCP-Server/README.md) |
| 06 | [Vývoj nástrojov](./06-Tools/README.md) | Tvorba nástrojov na dotazovanie databázy a introspekciu schémy | [Budujte](./06-Tools/README.md) |
| **Lab 7-9: Pokročilé funkcie** | | | |
| 07 | [Integrácia semantického vyhľadávania](./07-Semantic-Search/README.md) | Implementácia vektorových embeddingov s Azure OpenAI a pgvector | [Pokročte](./07-Semantic-Search/README.md) |
| 08 | [Testovanie a ladenie](./08-Testing/README.md) | Testovacie stratégie, nástroje na ladenie a validačné prístupy | [Testujte](./08-Testing/README.md) |
| 09 | [Integrácia VS Code](./09-VS-Code/README.md) | Konfigurácia VS Code MCP integrácie a používanie AI Chat | [Integrujte](./09-VS-Code/README.md) |
| **Lab 10-12: Produkcia a najlepšie praktiky** | | | |
| 10 | [Stratégie nasadenia](./10-Deployment/README.md) | Nasadenie pomocou Dockeru, Azure Container Apps a úvahy o škálovaní | [Nasadzujte](./10-Deployment/README.md) |
| 11 | [Monitorovanie a pozorovateľnosť](./11-Monitoring/README.md) | Application Insights, logovanie, monitorovanie výkonu | [Monitorujte](./11-Monitoring/README.md) |
| 12 | [Najlepšie praktiky a optimalizácia](./12-Best-Practices/README.md) | Optimalizácia výkonu, posilnenie bezpečnosti a tipy pre produkciu | [Optimalizujte](./12-Best-Practices/README.md) |

### 💻 Čo vytvoríte

Na konci tejto učebnej cesty budete mať kompletný **Zava Retail Analytics MCP Server**, ktorý obsahuje:

- **Viac-tabľovú maloobchodnú databázu** so zákazníckymi objednávkami, produktmi a inventárom
- **Row Level Security** na izoláciu dát podľa obchodov
- **Semantické vyhľadávanie produktov** pomocou embeddingov Azure OpenAI
- **Integráciu VS Code AI Chat** na dotazy v prirodzenom jazyku
- **Produkčne pripravené nasadenie** s Dockerom a Azure
- **Komplexné monitorovanie** pomocou Application Insights

## 🎯 Predpoklady pre učenie

Aby ste z tejto učebnej cesty získali maximum, mali by ste mať:

- **Skúsenosti s programovaním**: Znalosť Pythonu (preferovaný) alebo podobných jazykov
- **Znalosť databáz**: Základné porozumenie SQL a relačných databáz
- **Koncepty API**: Porozumenie REST API a HTTP konceptom
- **Vývojové nástroje**: Skúsenosti s príkazovým riadkom, Gitom a editormi kódu
- **Základy cloudu**: (Voliteľné) Základné znalosti Azure alebo podobných cloudových platforiem
- **Znalosť Dockeru**: (Voliteľné) Porozumenie konceptom kontajnerizácie

### Potrebné nástroje

- **Docker Desktop** - Na spustenie PostgreSQL a MCP servera
- **Azure CLI** - Na nasadenie cloudových zdrojov
- **VS Code** - Na vývoj a integráciu MCP
- **Git** - Na verzionovanie
- **Python 3.8+** - Na vývoj MCP servera

## 📚 Študijný sprievodca a zdroje

Táto učebná cesta obsahuje komplexné zdroje, ktoré vám pomôžu efektívne sa orientovať:

### Študijný sprievodca

Každý lab obsahuje:
- **Jasné učebné ciele** - Čo dosiahnete
- **Krok za krokom inštrukcie** - Podrobné implementačné príručky
- **Ukážky kódu** - Funkčné príklady s vysvetleniami
- **Cvičenia** - Príležitosti na praktické precvičenie
- **Príručky na riešenie problémov** - Bežné problémy a riešenia
- **Dodatočné zdroje** - Ďalšie čítanie a prieskum

### Kontrola predpokladov

Pred začatím každého labu nájdete:
- **Požadované znalosti** - Čo by ste mali vedieť vopred
- **Validácia nastavenia** - Ako overiť vaše prostredie
- **Odhady času** - Očakávaný čas na dokončenie
- **Výsledky učenia** - Čo budete vedieť po dokončení

### Odporúčané učebné cesty

Vyberte si cestu podľa vašej úrovne skúseností:

#### 🟢 **Cesta pre začiatočníkov** (Noví v MCP)
1. Uistite sa, že ste dokončili 0-10 z [MCP pre začiatočníkov](https://aka.ms/mcp-for-beginners)
2. Dokončite laby 00-03 na posilnenie základov
3. Nasledujte laby 04-06 na praktické budovanie
4. Skúste laby 07-09 na praktické použitie

#### 🟡 **Cesta pre pokročilých** (Niektoré skúsenosti s MCP)
1. Prejdite laby 00-01 na koncepty špecifické pre databázy
2. Zamerajte sa na laby 02-06 na implementáciu
3. Ponorte sa do labov 07-12 na pokročilé funkcie

#### 🔴 **Cesta pre expertov** (Skúsení s MCP)
1. Prejdite laby 00-03 na kontext
2. Zamerajte sa na laby 04-09 na integráciu databázy
3. Sústreďte sa na laby 10-12 na produkčné nasadenie

## 🛠️ Ako efektívne používať túto učebnú cestu

### Sekvenčné učenie (Odporúčané)

Prejdite laby postupne na komplexné porozumenie:

1. **Prečítajte si prehľad** - Porozumiete, čo sa naučíte
2. **Skontrolujte predpoklady** - Uistite sa, že máte potrebné znalosti
3. **Nasledujte krok za krokom príručky** - Implementujte počas učenia
4. **Dokončite cvičenia** - Posilnite svoje porozumenie
5. **Prejdite kľúčové poznatky** - Upevnite výsledky učenia

### Cielené učenie

Ak potrebujete konkrétne zručnosti:

- **Integrácia databázy**: Zamerajte sa na laby 04-06
- **Implementácia bezpečnosti**: Koncentrujte sa na laby 02, 08, 12
- **AI/Semantické vyhľadávanie**: Ponorte sa do labu 07
- **Produkčné nasadenie**: Študujte laby 10-12

### Praktické cvičenie

Každý lab obsahuje:
- **Funkčné ukážky kódu** - Kopírujte, upravujte a experimentujte
- **Scenáre z reálneho sveta** - Praktické prípady použitia maloobchodnej analytiky
- **Postupná komplexnosť** - Budovanie od jednoduchého k pokročilému
- **Kroky validácie** - Overte, že vaša implementácia funguje

## 🌟 Komunita a podpora

### Získajte pomoc

- **Azure AI Discord**: [Pripojte sa na odbornú podporu](https://discord.com/invite/ByRwuEEgH4)
- **GitHub Repo a ukážka implementácie**: [Ukážka nasadenia a zdroje](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP Komunita**: [Pripojte sa k širším diskusiám o MCP](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Pripravení začať?

Začnite svoju cestu s **[Lab 00: Úvod do integrácie MCP databázy](./00-Introduction/README.md)**

---

*Ovládnite budovanie produkčne pripravených MCP serverov s integráciou databázy prostredníctvom tejto komplexnej, praktickej učebnej skúsenosti.*

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.