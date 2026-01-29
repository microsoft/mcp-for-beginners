# Úvod do integrácie MCP s databázou

## 🎯 Čo tento lab pokrýva

Tento úvodný lab poskytuje komplexný prehľad o vytváraní serverov Model Context Protocol (MCP) s integráciou databázy. Prostredníctvom analytického prípadu Zava Retail na https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail pochopíte obchodný prípad, technickú architektúru a reálne aplikácie.

## Prehľad

**Model Context Protocol (MCP)** umožňuje AI asistentom bezpečne pristupovať k externým zdrojom dát a interagovať s nimi v reálnom čase. V kombinácii s integráciou databázy MCP odomyká silné schopnosti pre aplikácie poháňané dátami.

Táto vzdelávacia cesta vás naučí vytvárať produkčne pripravené MCP servery, ktoré prepájajú AI asistentov s údajmi o maloobchodnom predaji prostredníctvom PostgreSQL, pričom implementuje podnikové vzory ako Row Level Security, semantické vyhľadávanie a prístup k dátam pre viacerých nájomcov.

## Ciele učenia

Na konci tohto labu budete schopní:

- **Definovať** Model Context Protocol a jeho hlavné výhody pre integráciu databázy
- **Identifikovať** kľúčové komponenty architektúry MCP servera s databázami
- **Pochopiť** prípad použitia Zava Retail a jeho obchodné požiadavky
- **Rozpoznať** podnikové vzory pre bezpečný a škálovateľný prístup k databázam
- **Uviesť** nástroje a technológie použité v tejto vzdelávacej ceste

## 🧭 Výzva: AI stretáva reálne dáta

### Obmedzenia tradičnej AI

Moderné AI asistenty sú neuveriteľne výkonné, ale čelia významným obmedzeniam pri práci s reálnymi obchodnými dátami:

| **Výzva** | **Popis** | **Dopad na podnikanie** |
|-----------|-----------|-------------------------|
| **Statické znalosti** | AI modely trénované na fixných datasetoch nemôžu pristupovať k aktuálnym obchodným dátam | Zastaralé poznatky, zmeškané príležitosti |
| **Dátové silá** | Informácie uzamknuté v databázach, API a systémoch, ku ktorým AI nemá prístup | Neúplná analýza, roztrieštené pracovné postupy |
| **Bezpečnostné obmedzenia** | Priamy prístup k databáze zvyšuje bezpečnostné a regulačné riziká | Obmedzené nasadenie, manuálna príprava dát |
| **Komplexné dotazy** | Obchodní používatelia potrebujú technické znalosti na získanie dátových poznatkov | Znížená adopcia, neefektívne procesy |

### Riešenie MCP

Model Context Protocol rieši tieto výzvy poskytovaním:

- **Prístupu k dátam v reálnom čase**: AI asistenti dotazujú živé databázy a API
- **Bezpečnej integrácie**: Kontrolovaný prístup s autentifikáciou a povoleniami
- **Rozhrania v prirodzenom jazyku**: Obchodní používatelia kladú otázky v bežnej angličtine
- **Štandardizovaného protokolu**: Funguje naprieč rôznymi AI platformami a nástrojmi

## 🏪 Zoznámte sa so Zava Retail: Naša študijná prípadová štúdia https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Počas tejto vzdelávacej cesty vytvoríme MCP server pre **Zava Retail**, fiktívny DIY maloobchodný reťazec s viacerými predajňami. Tento realistický scenár demonštruje implementáciu MCP na podnikovej úrovni.

### Obchodný kontext

**Zava Retail** prevádzkuje:
- **8 kamenných predajní** v štáte Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 online predajňu** pre e-commerce predaj
- **Rozmanitý katalóg produktov** vrátane nástrojov, hardvéru, záhradných potrieb a stavebných materiálov
- **Viacúrovňové riadenie** s manažérmi predajní, regionálnymi manažérmi a vedúcimi pracovníkmi

### Obchodné požiadavky

Manažéri predajní a vedúci pracovníci potrebujú AI-poháňanú analytiku na:

1. **Analýzu predajnej výkonnosti** naprieč predajňami a časovými obdobiami
2. **Sledovanie úrovní zásob** a identifikáciu potrieb na doplnenie
3. **Pochopenie správania zákazníkov** a nákupných vzorcov
4. **Objavovanie produktových poznatkov** prostredníctvom semantického vyhľadávania
5. **Generovanie reportov** pomocou dotazov v prirodzenom jazyku
6. **Zachovanie bezpečnosti dát** s kontrolou prístupu na základe rolí

### Technické požiadavky

MCP server musí poskytovať:

- **Prístup k dátam pre viacerých nájomcov**, kde manažéri predajní vidia iba dáta svojej predajne
- **Flexibilné dotazovanie** podporujúce komplexné SQL operácie
- **Semantické vyhľadávanie** na objavovanie produktov a odporúčania
- **Dáta v reálnom čase** odrážajúce aktuálny stav podnikania
- **Bezpečnú autentifikáciu** s Row Level Security
- **Škálovateľnú architektúru** podporujúcu viacerých súčasných používateľov

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
- **Kontext požiadavky**: Správa identity používateľa a relácie
- **Spracovanie chýb**: Robustná správa chýb a logovanie

#### **2. Vrstva integrácie databázy**
- **Pooling pripojení**: Efektívna správa pripojení asyncpg
- **Poskytovateľ schémy**: Dynamické objavovanie schém tabuliek
- **Executor dotazov**: Bezpečné vykonávanie SQL s kontextom RLS
- **Správa transakcií**: Dodržiavanie ACID a spracovanie rollbackov

#### **3. Bezpečnostná vrstva**
- **Row Level Security**: PostgreSQL RLS na izoláciu dát pre viacerých nájomcov
- **Identita používateľa**: Autentifikácia a autorizácia manažérov predajní
- **Kontrola prístupu**: Jemne zrnité povolenia a auditné stopy
- **Validácia vstupov**: Prevencia SQL injekcií a validácia dotazov

#### **4. Vrstva AI vylepšení**
- **Semantické vyhľadávanie**: Vektorové embeddingy na objavovanie produktov
- **Integrácia Azure OpenAI**: Generovanie textových embeddingov
- **Algoritmy podobnosti**: pgvector vyhľadávanie pomocou kosínovej podobnosti
- **Optimalizácia vyhľadávania**: Indexovanie a ladenie výkonu

## 🔧 Technologický stack

### Základné technológie

| **Komponent** | **Technológia** | **Účel** |
|---------------|----------------|----------|
| **MCP Framework** | FastMCP (Python) | Moderná implementácia MCP servera |
| **Databáza** | PostgreSQL 17 + pgvector | Relačné dáta s vektorovým vyhľadávaním |
| **AI služby** | Azure OpenAI | Textové embeddingy a jazykové modely |
| **Kontajnerizácia** | Docker + Docker Compose | Vývojové prostredie |
| **Cloudová platforma** | Microsoft Azure | Nasadenie do produkcie |
| **Integrácia IDE** | VS Code | AI Chat a pracovný tok vývoja |

### Nástroje vývoja

| **Nástroj** | **Účel** |
|-------------|----------|
| **asyncpg** | Vysoko výkonný PostgreSQL driver |
| **Pydantic** | Validácia dát a serializácia |
| **Azure SDK** | Integrácia cloudových služieb |
| **pytest** | Testovací framework |
| **Docker** | Kontajnerizácia a nasadenie |

### Produkčný stack

| **Služba** | **Azure Resource** | **Účel** |
|------------|--------------------|----------|
| **Databáza** | Azure Database for PostgreSQL | Spravovaná databázová služba |
| **Kontajner** | Azure Container Apps | Hosting kontajnerov bez servera |
| **AI služby** | Azure AI Foundry | OpenAI modely a endpointy |
| **Monitoring** | Application Insights | Pozorovateľnosť a diagnostika |
| **Bezpečnosť** | Azure Key Vault | Správa tajomstiev a konfigurácie |

## 🎬 Scenáre reálneho použitia

Pozrime sa, ako rôzni používatelia interagujú s naším MCP serverom:

### Scenár 1: Prehľad výkonnosti manažéra predajne

**Používateľ**: Sarah, manažérka predajne v Seattli  
**Cieľ**: Analyzovať predajnú výkonnosť za posledný štvrťrok

**Dotaz v prirodzenom jazyku**:
> "Ukáž mi top 10 produktov podľa príjmov pre moju predajňu v Q4 2024"

**Čo sa stane**:
1. VS Code AI Chat pošle dotaz na MCP server
2. MCP server identifikuje kontext predajne Sarah (Seattle)
3. RLS politiky filtrujú dáta iba pre predajňu Seattle
4. SQL dotaz je vygenerovaný a vykonaný
5. Výsledky sú naformátované a vrátené do AI Chatu
6. AI poskytne analýzu a poznatky

### Scenár 2: Objavovanie produktov pomocou semantického vyhľadávania

**Používateľ**: Mike, manažér zásob  
**Cieľ**: Nájsť produkty podobné požiadavke zákazníka

**Dotaz v prirodzenom jazyku**:
> "Aké produkty predávame, ktoré sú podobné 'vodotesným elektrickým konektorom na vonkajšie použitie'?"

**Čo sa stane**:
1. Dotaz je spracovaný nástrojom semantického vyhľadávania
2. Azure OpenAI generuje vektor embedding
3. pgvector vykoná vyhľadávanie podobnosti
4. Súvisiace produkty sú zoradené podľa relevantnosti
5. Výsledky zahŕňajú detaily produktov a dostupnosť
6. AI navrhne alternatívy a možnosti balíčkovania

### Scenár 3: Analytika naprieč predajňami

**Používateľ**: Jennifer, regionálna manažérka  
**Cieľ**: Porovnať výkonnosť naprieč všetkými predajňami

**Dotaz v prirodzenom jazyku**:
> "Porovnaj predaje podľa kategórií pre všetky predajne za posledných 6 mesiacov"

**Čo sa stane**:
1. RLS kontext je nastavený na prístup regionálneho manažéra
2. Vygenerovaný je komplexný dotaz pre viaceré predajne
3. Dáta sú agregované naprieč lokalitami predajní
4. Výsledky zahŕňajú trendy a porovnania
5. AI identifikuje poznatky a odporúčania

## 🔒 Hĺbkový pohľad na bezpečnosť a multi-tenancy

Naša implementácia kladie dôraz na bezpečnosť na podnikovej úrovni:

### Row Level Security (RLS)

PostgreSQL RLS zabezpečuje izoláciu dát:

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

Každé pripojenie MCP zahŕňa:
- **ID manažéra predajne**: Jedinečný identifikátor pre kontext RLS
- **Priradenie rolí**: Povolenia a úrovne prístupu
- **Správa relácií**: Bezpečné autentifikačné tokeny
- **Auditné logovanie**: Kompletná história prístupu

### Ochrana dát

Viacero vrstiev bezpečnosti:
- **Šifrovanie pripojení**: TLS pre všetky pripojenia k databáze
- **Prevencia SQL injekcií**: Iba parametrizované dotazy
- **Validácia vstupov**: Komplexná validácia požiadaviek
- **Spracovanie chýb**: Žiadne citlivé dáta v chybových správach

## 🎯 Kľúčové poznatky

Po dokončení tohto úvodu by ste mali rozumieť:

✅ **Hodnota MCP**: Ako MCP prepája AI asistentov s reálnymi dátami  
✅ **Obchodný kontext**: Požiadavky a výzvy Zava Retail  
✅ **Prehľad architektúry**: Kľúčové komponenty a ich interakcie  
✅ **Technologický stack**: Nástroje a frameworky použité počas cesty  
✅ **Bezpečnostný model**: Prístup k dátam pre viacerých nájomcov a ich ochrana  
✅ **Vzory použitia**: Scenáre dotazov a pracovné postupy v reálnom svete  

## 🚀 Čo ďalej

Pripravení ísť hlbšie? Pokračujte s:

**[Lab 01: Základné koncepty architektúry](../01-Architecture/README.md)**

Naučte sa o vzoroch architektúry MCP servera, princípoch návrhu databázy a podrobnej technickej implementácii, ktorá poháňa naše riešenie maloobchodnej analytiky.

## 📚 Dodatočné zdroje

### Dokumentácia MCP
- [Špecifikácia MCP](https://modelcontextprotocol.io/docs/) - Oficiálna dokumentácia protokolu
- [MCP pre začiatočníkov](https://aka.ms/mcp-for-beginners) - Komplexný sprievodca MCP
- [Dokumentácia FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Dokumentácia Python SDK

### Integrácia databázy
- [Dokumentácia PostgreSQL](https://www.postgresql.org/docs/) - Kompletný referenčný materiál PostgreSQL
- [Sprievodca pgvector](https://github.com/pgvector/pgvector) - Dokumentácia rozšírenia pre vektory
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Sprievodca PostgreSQL RLS

### Služby Azure
- [Dokumentácia Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integrácia AI služieb
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Spravovaná databázová služba
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Kontajnery bez servera

---

**Upozornenie**: Toto je vzdelávacie cvičenie využívajúce fiktívne maloobchodné dáta. Pri implementácii podobných riešení v produkčnom prostredí vždy dodržiavajte pravidlá správy dát a bezpečnostné politiky vašej organizácie.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.