# Úvod do integrácie databázy MCP

> [!NOTE]
> Diagramy alebo kód v tejto vzdelávacej ceste používajúci HTTP/SSE alebo inicializačné
> možnosti odrážajú závislosti príkladu MCP `2025-11-25`. Pre nové
> implementácie používajte `2026-07-28` stavové požiadavky a Streamable HTTP.

## 🎯 Čo tento laboratórny cvičenie pokrýva

Tento úvodný lab poskytuje komplexný prehľad o budovaní serverov Model Context Protocol (MCP) s integráciou databázy. Pochopíte obchodný prípad, technickú architektúru a reálne aplikácie prostredníctvom použitia Zava Retail analytiky na https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Prehľad

**Model Context Protocol (MCP)** umožňuje AI asistentom bezpečne pristupovať a interagovať s externými zdrojmi dát v reálnom čase. V kombinácii s integráciou databázy MCP odomyká silné možnosti pre aplikácie založené na dátach AI.

Táto vzdelávacia cesta vás naučí budovať produkčne pripravené MCP servery, ktoré pripájajú AI asistentov k maloobchodným predajom dát cez PostgreSQL, implementujúc podnikové vzory ako Row Level Security, sémantické vyhľadávanie a prístup k dátam pre viac nájomcov.

## Ciele učenia

Na konci tohto laboratory sa budete vedieť:

- **Definovať** Model Context Protocol a jeho základné výhody pre integráciu databázy
- **Identifikovať** kľúčové komponenty architektúry MCP servera s databázami
- **Pochopiť** použitie Zava Retail a jeho obchodné požiadavky
- **Rozpoznať** podnikové vzory pre bezpečný a škálovateľný prístup k databáze
- **Vymenovať** nástroje a technológie používané počas celej vzdelávacej cesty

## 🧭 Výzva: AI stretáva sa so skutočnými dátami

### Tradičné obmedzenia AI

Moderné AI asistenti sú mimoriadne výkonné, ale čelia významným obmedzeniam pri práci so skutočnými obchodnými dátami:

| **Výzva** | **Popis** | **Obchodný dopad** |
|---------------|-----------------|-------------------|
| **Statické vedomosti** | AI modely trénované na fixných dátových sadách nemajú prístup k aktuálnym obchodným dátam | Zastaralé poznatky, nevyužité príležitosti |
| **Dátové silo** | Informácie uzavreté v databázach, API a systémoch, ku ktorým AI nemá prístup | Neúplné analýzy, fragmentované pracovné toky |
| **Bezpečnostné obmedzenia** | Priamy prístup do databázy vyvoláva bezpečnostné a regulačné problémy | Obmedzené nasadenie, manuálna príprava dát |
| **Zložité dotazy** | Obchodní používatelia potrebujú technické znalosti na získavanie dátových poznatkov | Znížené používanie, neefektívne procesy |

### Riešenie MCP

Model Context Protocol rieši tieto výzvy poskytovaním:

- **Prístup k dátam v reálnom čase**: AI asistenti dotazujú živé databázy a API
- **Bezpečná integrácia**: Riadený prístup s autentifikáciou a povoleniami
- **Rozhranie v prirodzenom jazyku**: Obchodní používatelia kladú otázky jednoducho po anglicky
- **Štandardizovaný protokol**: Funguje naprieč rôznymi AI platformami a nástrojmi

## 🏪 Spoznajte Zava Retail: Naša prípadová štúdia https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Počas celej tejto vzdelávacej cesty postavíme MCP server pre **Zava Retail**, fiktívnu DIY maloobchodnú sieť s viacerými pobočkami. Tento realistický scenár demonštruje podnikové implementácie MCP.

### Obchodný kontext

**Zava Retail** prevádzkuje:
- **8 kamenných predajní** po celom štáte Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 online obchod** pre elektronický predaj
- **Rôznorodý katalóg produktov** vrátane nástrojov, hardvéru, záhradného materiálu a stavebných materiálov
- **Viacúrovňové riadenie** s manažérmi predajní, regionálnymi manažérmi a vedením

### Obchodné požiadavky

Manažéri predajní a vedenie potrebujú AI-poháňanú analytiku na:

1. **Analyzovať predajné výsledky** naprieč predajňami a časovými obdobiami
2. **Sledovať stavy zásob** a identifikovať potreby doplnenia
3. **Pochopiť správanie zákazníkov** a nákupné vzory
4. **Objaviť poznatky o produktoch** pomocou sémantického vyhľadávania
5. **Generovať reporty** pomocou otázok v prirodzenom jazyku
6. **Zachovať bezpečnosť dát** pomocou riadenia prístupu na základe rolí

### Technické požiadavky

MCP server musí poskytovať:

- **Prístup k dátam pre viac nájomcov**, kde manažéri vidia len dáta svojej predajne
- **Flexibilné dotazovanie** podporujúce zložité SQL operácie
- **Sémantické vyhľadávanie** pre objavovanie produktov a odporúčania
- **Dáta v reálnom čase** odrážajúce aktuálny stav obchodu
- **Bezpečná autentifikácia** s Row Level Security
- **Škálovateľná architektúra** podporujúca viacerých súčasných používateľov

## 🏗️ Prehľad architektúry MCP servera

Náš MCP server implementuje vrstvenú architektúru optimalizovanú pre integráciu databázy:

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### Kľúčové komponenty

#### **1. Vrstva MCP servera**
- **FastMCP Framework**: Moderná implementácia MCP servera v Pythone
- **Registrácia nástrojov**: Deklaratívne definície nástrojov s typovou bezpečnosťou
- **Kontext požiadavky**: Identita používateľa a správa relácie
- **Riadenie chýb**: Robustné spracovanie a zaznamenávanie chýb

#### **2. Vrstva integrácie databázy**
- **Pooling pripojení**: Efektívna správa pripojení pomocou asyncpg
- **Poskytovateľ schémy**: Dynamické zisťovanie schém tabuliek
- **Vykonávač dotazov**: Bezpečné vykonávanie SQL s kontextom RLS
- **Správa transakcií**: Dodržiavanie ACID a spracovanie rollbacku

#### **3. Bezpečnostná vrstva**
- **Row Level Security**: PostgreSQL RLS pre izoláciu dát viacerých nájomcov
- **Identita používateľa**: Autentifikácia a autorizácia manažéra predajne
- **Riadenie prístupu**: Granulárne povolenia a auditné záznamy
- **Validácia vstupov**: Prevencia SQL injection a validácia dotazov

#### **4. Vrstva AI rozšírení**
- **Sémantické vyhľadávanie**: Vektorové embeddingy pre vyhľadávanie produktov
- **Integrácia Azure OpenAI**: Generovanie tekstových embeddingov
- **Algoritmy podobnosti**: pgvector vyhľadávanie podľa kosínovej podobnosti
- **Optimalizácia vyhľadávania**: Indexovanie a ladenie výkonu

## 🔧 Technologický stack

### Jadrové technológie

| **Komponent** | **Technológia** | **Účel** |
|---------------|----------------|-------------|
| **MCP Framework** | FastMCP (Python) | Moderná implementácia MCP servera |
| **Databáza** | PostgreSQL 17 + pgvector | Relačné dáta s vektorovým vyhľadávaním |
| **AI služby** | Azure OpenAI | Textové embeddingy a jazykové modely |
| **Kontajnerizácia** | Docker + Docker Compose | Vývojové prostredie |
| **Cloud platforma** | Microsoft Azure | Produkčné nasadenie |
| **Integrácia IDE** | VS Code | AI chat a vývojový pracovný tok |

### Vývojové nástroje

| **Nástroj** | **Účel** |
|----------|-------------|
| **asyncpg** | Vysokovýkonný PostgreSQL ovládač |
| **Pydantic** | Overovanie a serializácia dát |
| **Azure SDK** | Integrácia cloudových služieb |
| **pytest** | Testovací rámec |
| **Docker** | Kontajnerizácia a nasadenie |

### Produkčný stack

| **Služba** | **Azure zdroj** | **Účel** |
|-------------|-------------------|-------------|
| **Databáza** | Azure Database for PostgreSQL | Manažovaná databázová služba |
| **Kontajner** | Azure Container Apps | Serverless hostovanie kontajnerov |
| **AI služby** | Microsoft Foundry | OpenAI modely a endpointy |
| **Monitoring** | Application Insights | Sledovanie a diagnostika |
| **Bezpečnosť** | Azure Key Vault | Správa tajomstiev a konfigurácií |

## 🎬 Scenáre používania v reálnom svete

Preskúmajme, ako rôzni používatelia interagujú s naším MCP serverom:

### Scenár 1: Hodnotenie výkonu manažéra predajne

**Používateľ**: Sarah, manažérka predajne v Seattle  
**Cieľ**: Analyzovať predajné výsledky za posledný kvartál

**Dotaz v prirodzenom jazyku**:
> "Ukáž mi top 10 produktov podľa tržieb za moju predajňu v Q4 2024"

**Čo sa deje**:
1. VS Code AI Chat odošle dotaz na MCP server
2. MCP server identifikuje kontext Sarahinej predajne (Seattle)
3. RLS politiky filtrovali dáta len pre predajňu v Seattle
4. SQL dotaz je vygenerovaný a vykonaný
5. Výsledky sú naformátované a vrátené do AI Chatu
6. AI poskytne analýzu a poznatky

### Scenár 2: Objavovanie produktov pomocou sémantického vyhľadávania

**Používateľ**: Mike, manažér zásob  
**Cieľ**: Nájsť produkty podobné požiadavke zákazníka

**Dotaz v prirodzenom jazyku**:
> "Aké produkty predávame, ktoré sú podobné 'vodotesné elektrické konektory na vonkajšie použitie'?"

**Čo sa deje**:
1. Dotaz spracovaný sémantickým vyhľadávacím nástrojom
2. Azure OpenAI generuje embedding vektor
3. pgvector vykoná vyhľadávanie podľa podobnosti
4. Súvisiace produkty sú zoradené podľa relevantnosti
5. Výsledky obsahujú detaily produktu a dostupnosť
6. AI navrhuje alternatívy a možnosti balíčkovania

### Scenár 3: Analytika naprieč predajňami

**Používateľ**: Jennifer, regionálna manažérka  
**Cieľ**: Porovnať výkon všetkých predajní

**Dotaz v prirodzenom jazyku**:
> "Porovnaj predaje podľa kategórií vo všetkých predajniach za posledných 6 mesiacov"

**Čo sa deje**:
1. RLS kontext nastavený pre prístup regionálnej manažérky
2. Vygenerovaný komplexný dotaz pre viaceré predajne
3. Dáta agregované naprieč lokáciami predajní
4. Výsledky zahŕňajú trendy a porovnania
5. AI identifikuje poznatky a odporúčania

## 🔒 Hĺbkový pohľad na bezpečnosť a multi-tenancy

Naša implementácia stavia na podnikovom bezpečnostnom štandarde:

### Row Level Security (RLS)

PostgreSQL RLS zaisťuje izoláciu dát:

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### Správa identity používateľa

Každé MCP pripojenie obsahuje:
- **ID manažéra predajne**: Jedinečný identifikátor pre RLS kontext
- **Priradenie rolí**: Povolenia a úrovne prístupu
- **Správa relácie**: Bezpečné autentifikačné tokeny
- **Auditné záznamy**: Kompletná história prístupu

### Ochrana dát

Viacvrstvová bezpečnosť:
- **Šifrovanie pripojení**: TLS pre všetky databázové pripojenia
- **Prevencia SQL injection**: Iba parameterizované dotazy
- **Validácia vstupov**: Komplexné overovanie požiadaviek
- **Spracovanie chýb**: Žiadne citlivé dáta v chybových hláseniach

## 🎯 Kľúčové závery

Po dokončení tohto úvodu by ste mali rozumieť:

✅ **Hodnota MCP**: Ako MCP prepája AI asistentov a reálne dáta  
✅ **Obchodný kontext**: Požiadavky a výzvy Zava Retail  
✅ **Prehľad architektúry**: Kľúčové komponenty a ich interakcie  
✅ **Technologický stack**: Použité nástroje a rámce  
✅ **Bezpečnostný model**: Prístup a ochrana dát pre viac nájomcov  
✅ **Vzory používania**: Scenáre dotazov z praxe a pracovné toky  

## 🚀 Čo ďalej

Ste pripravení ísť hlbšie? Pokračujte s:

**[Lab 01: Základné architektonické koncepty](../01-Architecture/README.md)**

Naučte sa o vzoroch architektúry MCP servera, princípoch návrhu databázy a podrobnej technickej implementácii, ktorá poháňa naše riešenie maloobchodnej analytiky.

## 📚 Ďalšie zdroje

### Dokumentácia MCP
- [Špecifikácia MCP](https://modelcontextprotocol.io/docs/) - Oficiálna dokumentácia protokolu
- [MCP pre začiatočníkov](https://aka.ms/mcp-for-beginners) - Komplexný sprievodca učením MCP
- [Dokumentácia FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Dokumentácia Python SDK

### Integrácia databázy
- [Dokumentácia PostgreSQL](https://www.postgresql.org/docs/) - Kompletný referenčný manuál PostgreSQL
- [Príručka pgvector](https://github.com/pgvector/pgvector) - Dokumentácia rozšírenia pre vektory
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Príručka PostgreSQL RLS

### Azure služby
- [Dokumentácia Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integrácia AI služieb
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Manažovaná databázová služba
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverless kontajnery

---

**Upozornenie**: Toto je vzdelávacie cvičenie využívajúce fiktívne maloobchodné dáta. Pri implementácii podobných riešení v produkčnom prostredí vždy dodržiavajte pravidlá správy a bezpečnosti dát vašej organizácie.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->