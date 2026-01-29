# Úvod do integrace MCP s databázemi

## 🎯 Co tento lab pokrývá

Tento úvodní lab poskytuje komplexní přehled o vytváření serverů Model Context Protocol (MCP) s integrací databází. Porozumíte obchodnímu případu, technické architektuře a reálným aplikacím prostřednictvím případu analýzy Zava Retail na https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Přehled

**Model Context Protocol (MCP)** umožňuje AI asistentům bezpečně přistupovat k externím datovým zdrojům a interagovat s nimi v reálném čase. V kombinaci s integrací databází MCP odemyká silné možnosti pro aplikace poháněné daty.

Tato vzdělávací cesta vás naučí vytvářet produkčně připravené MCP servery, které propojují AI asistenty s daty o maloobchodním prodeji prostřednictvím PostgreSQL, implementují podnikové vzory jako Row Level Security, sémantické vyhledávání a přístup k datům pro více nájemců.

## Cíle učení

Na konci tohoto labu budete schopni:

- **Definovat** Model Context Protocol a jeho hlavní přínosy pro integraci databází
- **Identifikovat** klíčové komponenty architektury MCP serveru s databázemi
- **Porozumět** případu Zava Retail a jeho obchodním požadavkům
- **Rozpoznat** podnikové vzory pro bezpečný a škálovatelný přístup k databázím
- **Vyjmenovat** nástroje a technologie použité v této vzdělávací cestě

## 🧭 Výzva: AI a reálná data

### Omezení tradiční AI

Moderní AI asistenti jsou neuvěřitelně silní, ale čelí významným omezením při práci s reálnými obchodními daty:

| **Výzva** | **Popis** | **Dopad na podnikání** |
|-----------|-----------|-----------------------|
| **Statické znalosti** | AI modely trénované na fixních datových sadách nemohou přistupovat k aktuálním obchodním datům | Zastaralé poznatky, zmeškané příležitosti |
| **Datové silo** | Informace uzamčené v databázích, API a systémech, ke kterým AI nemá přístup | Neúplná analýza, roztříštěné pracovní postupy |
| **Bezpečnostní omezení** | Přímý přístup k databázím zvyšuje bezpečnostní a regulační rizika | Omezené nasazení, manuální příprava dat |
| **Komplexní dotazy** | Obchodní uživatelé potřebují technické znalosti k získání datových poznatků | Snížené přijetí, neefektivní procesy |

### Řešení MCP

Model Context Protocol řeší tyto výzvy tím, že poskytuje:

- **Přístup k datům v reálném čase**: AI asistenti dotazují živé databáze a API
- **Bezpečnou integraci**: Kontrolovaný přístup s autentizací a oprávněními
- **Rozhraní v přirozeném jazyce**: Obchodní uživatelé kladou otázky v běžné angličtině
- **Standardizovaný protokol**: Funguje napříč různými AI platformami a nástroji

## 🏪 Seznamte se s Zava Retail: Naše případová studie https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Během této vzdělávací cesty vytvoříme MCP server pro **Zava Retail**, fiktivní maloobchodní řetězec pro kutily s několika prodejnami. Tento realistický scénář demonstruje implementaci MCP na podnikové úrovni.

### Obchodní kontext

**Zava Retail** provozuje:
- **8 kamenných prodejen** ve státě Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 online obchod** pro e-commerce prodej
- **Rozmanitý katalog produktů** zahrnující nástroje, hardware, zahradní potřeby a stavební materiály
- **Víceúrovňové řízení** s vedoucími prodejen, regionálními manažery a vedením

### Obchodní požadavky

Vedoucí prodejen a vedení potřebují AI poháněnou analytiku k:

1. **Analýze prodejní výkonnosti** napříč prodejnami a časovými obdobími
2. **Sledování úrovní zásob** a identifikaci potřeb doplnění
3. **Porozumění chování zákazníků** a nákupním vzorcům
4. **Objevování produktových poznatků** prostřednictvím sémantického vyhledávání
5. **Generování reportů** pomocí dotazů v přirozeném jazyce
6. **Zajištění bezpečnosti dat** s kontrolou přístupu na základě rolí

### Technické požadavky

MCP server musí poskytovat:

- **Přístup k datům pro více nájemců**, kde vedoucí prodejen vidí pouze data své prodejny
- **Flexibilní dotazování** podporující komplexní SQL operace
- **Sémantické vyhledávání** pro objevování produktů a doporučení
- **Data v reálném čase** odrážející aktuální stav podnikání
- **Bezpečnou autentizaci** s Row Level Security
- **Škálovatelnou architekturu** podporující více současných uživatelů

## 🏗️ Přehled architektury MCP serveru

Náš MCP server implementuje vrstvenou architekturu optimalizovanou pro integraci databází:

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

### Klíčové komponenty

#### **1. Vrstva MCP serveru**
- **FastMCP Framework**: Moderní implementace MCP serveru v Pythonu
- **Registrace nástrojů**: Deklarativní definice nástrojů s typovou bezpečností
- **Kontext požadavků**: Správa identity uživatele a relací
- **Zpracování chyb**: Robustní správa chyb a logování

#### **2. Vrstva integrace databází**
- **Pooling připojení**: Efektivní správa připojení asyncpg
- **Poskytovatel schématu**: Dynamické objevování schématu tabulek
- **Executor dotazů**: Bezpečné provádění SQL s kontextem RLS
- **Správa transakcí**: Dodržování ACID a zpracování rollbacků

#### **3. Bezpečnostní vrstva**
- **Row Level Security**: PostgreSQL RLS pro izolaci dat více nájemců
- **Identita uživatele**: Autentizace a autorizace vedoucích prodejen
- **Kontrola přístupu**: Jemně granulovaná oprávnění a auditní stopy
- **Validace vstupů**: Prevence SQL injekcí a validace dotazů

#### **4. Vrstva AI vylepšení**
- **Sémantické vyhledávání**: Vektorové embeddingy pro objevování produktů
- **Integrace Azure OpenAI**: Generování textových embeddingů
- **Algoritmy podobnosti**: pgvector vyhledávání pomocí kosinové podobnosti
- **Optimalizace vyhledávání**: Indexování a ladění výkonu

## 🔧 Technologický stack

### Základní technologie

| **Komponenta** | **Technologie** | **Účel** |
|----------------|-----------------|----------|
| **MCP Framework** | FastMCP (Python) | Moderní implementace MCP serveru |
| **Databáze** | PostgreSQL 17 + pgvector | Relační data s vektorovým vyhledáváním |
| **AI služby** | Azure OpenAI | Textové embeddingy a jazykové modely |
| **Kontejnerizace** | Docker + Docker Compose | Vývojové prostředí |
| **Cloudová platforma** | Microsoft Azure | Nasazení do produkce |
| **Integrace IDE** | VS Code | AI Chat a pracovní postup vývoje |

### Vývojové nástroje

| **Nástroj** | **Účel** |
|-------------|----------|
| **asyncpg** | Vysoce výkonný PostgreSQL driver |
| **Pydantic** | Validace a serializace dat |
| **Azure SDK** | Integrace cloudových služeb |
| **pytest** | Testovací framework |
| **Docker** | Kontejnerizace a nasazení |

### Produkční stack

| **Služba** | **Azure Resource** | **Účel** |
|------------|--------------------|----------|
| **Databáze** | Azure Database for PostgreSQL | Spravovaná databázová služba |
| **Kontejner** | Azure Container Apps | Serverless hosting kontejnerů |
| **AI služby** | Azure AI Foundry | OpenAI modely a endpointy |
| **Monitoring** | Application Insights | Observabilita a diagnostika |
| **Bezpečnost** | Azure Key Vault | Správa tajemství a konfigurace |

## 🎬 Scénáře reálného použití

Podívejme se, jak různí uživatelé interagují s naším MCP serverem:

### Scénář 1: Přehled výkonnosti vedoucího prodejny

**Uživatel**: Sarah, vedoucí prodejny v Seattlu  
**Cíl**: Analyzovat prodejní výkonnost za poslední čtvrtletí

**Dotaz v přirozeném jazyce**:
> "Ukaž mi 10 nejlepších produktů podle příjmů pro mou prodejnu ve 4. čtvrtletí 2024"

**Co se stane**:
1. VS Code AI Chat odešle dotaz na MCP server
2. MCP server identifikuje kontext prodejny Sarah (Seattle)
3. RLS politiky filtrují data pouze pro prodejnu Seattle
4. SQL dotaz je vygenerován a proveden
5. Výsledky jsou naformátovány a vráceny do AI Chatu
6. AI poskytne analýzu a poznatky

### Scénář 2: Objevování produktů pomocí sémantického vyhledávání

**Uživatel**: Mike, manažer zásob  
**Cíl**: Najít produkty podobné požadavku zákazníka

**Dotaz v přirozeném jazyce**:
> "Jaké produkty prodáváme, které jsou podobné 'vodotěsným elektrickým konektorům pro venkovní použití'?"

**Co se stane**:
1. Dotaz je zpracován nástrojem sémantického vyhledávání
2. Azure OpenAI generuje vektor embedding
3. pgvector provádí vyhledávání podobnosti
4. Související produkty jsou seřazeny podle relevance
5. Výsledky zahrnují detaily produktů a dostupnost
6. AI navrhne alternativy a možnosti balíčků

### Scénář 3: Analytika napříč prodejnami

**Uživatel**: Jennifer, regionální manažerka  
**Cíl**: Porovnat výkonnost napříč všemi prodejnami

**Dotaz v přirozeném jazyce**:
> "Porovnej prodeje podle kategorií pro všechny prodejny za posledních 6 měsíců"

**Co se stane**:
1. RLS kontext je nastaven pro přístup regionálního manažera
2. Vygenerován komplexní dotaz pro více prodejen
3. Data jsou agregována napříč lokalitami prodejen
4. Výsledky zahrnují trendy a porovnání
5. AI identifikuje poznatky a doporučení

## 🔒 Detailní pohled na bezpečnost a multi-tenancy

Naše implementace klade důraz na bezpečnost na podnikové úrovni:

### Row Level Security (RLS)

PostgreSQL RLS zajišťuje izolaci dat:

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

### Správa identity uživatele

Každé připojení MCP zahrnuje:
- **ID vedoucího prodejny**: Unikátní identifikátor pro kontext RLS
- **Přiřazení rolí**: Oprávnění a úrovně přístupu
- **Správa relací**: Bezpečné autentizační tokeny
- **Auditní logování**: Kompletní historie přístupů

### Ochrana dat

Více vrstev bezpečnosti:
- **Šifrování připojení**: TLS pro všechna připojení k databázi
- **Prevence SQL injekcí**: Pouze parametrizované dotazy
- **Validace vstupů**: Komplexní validace požadavků
- **Zpracování chyb**: Žádná citlivá data ve zprávách o chybách

## 🎯 Klíčové poznatky

Po dokončení tohoto úvodu byste měli rozumět:

✅ **Hodnotě MCP**: Jak MCP propojuje AI asistenty s reálnými daty  
✅ **Obchodnímu kontextu**: Požadavkům a výzvám Zava Retail  
✅ **Přehledu architektury**: Klíčovým komponentám a jejich interakcím  
✅ **Technologickému stacku**: Nástrojům a frameworkům použitým v průběhu  
✅ **Bezpečnostnímu modelu**: Přístupu k datům pro více nájemců a jejich ochraně  
✅ **Vzorům použití**: Scénářům dotazů a pracovním postupům v reálném světě  

## 🚀 Co dál

Připraveni se ponořit hlouběji? Pokračujte s:

**[Lab 01: Základní koncepty architektury](../01-Architecture/README.md)**

Naučte se o vzorech architektury MCP serveru, principech návrhu databází a podrobné technické implementaci, která pohání naše řešení maloobchodní analytiky.

## 📚 Další zdroje

### Dokumentace MCP
- [Specifikace MCP](https://modelcontextprotocol.io/docs/) - Oficiální dokumentace protokolu
- [MCP pro začátečníky](https://aka.ms/mcp-for-beginners) - Komplexní průvodce MCP
- [Dokumentace FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Dokumentace Python SDK

### Integrace databází
- [Dokumentace PostgreSQL](https://www.postgresql.org/docs/) - Kompletní referenční příručka PostgreSQL
- [Průvodce pgvector](https://github.com/pgvector/pgvector) - Dokumentace rozšíření pro vektory
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Průvodce PostgreSQL RLS

### Služby Azure
- [Dokumentace Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integrace AI služeb
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Spravovaná databázová služba
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverless kontejnery

---

**Upozornění**: Toto je vzdělávací cvičení využívající fiktivní maloobchodní data. Při implementaci podobných řešení v produkčním prostředí vždy dodržujte zásady správy dat a bezpečnosti vaší organizace.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.