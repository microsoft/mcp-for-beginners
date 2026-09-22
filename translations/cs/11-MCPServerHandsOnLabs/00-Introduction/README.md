# Úvod do integrace databáze MCP

> [!NOTE]
> Diagramy nebo kód v této výukové cestě, které používají HTTP/SSE nebo inicializační
> možnosti, odrážejí závislosti ukázkového MCP `2025-11-25`. Pro nové
> implementace používejte bezstavové požadavky `2026-07-28` a Streamable HTTP.

## 🎯 Co tento kurz pokrývá

Tento úvodní kurz poskytuje komplexní přehled o vytváření serverů Model Context Protocol (MCP) s integrací databáze. Pochopíte obchodní případ, technickou architekturu a reálné aplikace prostřednictvím případu použití Zava Retail analytiky na https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Přehled

**Model Context Protocol (MCP)** umožňuje AI asistentům bezpečný přístup a interakci s externími zdroji dat v reálném čase. V kombinaci s integrací databáze MCP odemyká silné schopnosti pro AI aplikace založené na datech.

Tato výuková cesta vás naučí vytvářet produkčně připravené MCP servery, které propojují AI asistenty s daty prodejů v maloobchodě přes PostgreSQL, implementují podnikové vzory jako Rolová bezpečnost na úrovni řádků, sémantické vyhledávání a přístup k datům v režimu multi-tenant.

## Výukové cíle

Po absolvování tohoto kurzu budete schopni:

- **Definovat** Model Context Protocol a jeho klíčové výhody pro integraci databáze
- **Identifikovat** klíčové komponenty architektury MCP serveru s databázemi
- **Pochopit** případ použití Zava Retail a jeho obchodní požadavky
- **Uvědomit si** podnikové vzory pro bezpečný, škálovatelný přístup k databázi
- **Vyjmenovat** nástroje a technologie použité v této výukové cestě

## 🧭 Výzva: AI potkává data ze skutečného světa

### Omezení tradiční AI

Moderní AI asistenti jsou nesmírně výkonní, ale čelí významným omezením při práci s reálnými obchodními daty:

| **Výzva** | **Popis** | **Obchodní dopad** |
|---------------|-----------------|-------------------|
| **Statické znalosti** | AI modely vyškolené na fixních datech nemají přístup k aktuálním obchodním datům | Zastaralé informace, promarněné příležitosti |
| **Datové silo** | Informace uzamčené v databázích, API a systémech, ke kterým AI nemůže přistupovat | Neúplné analýzy, rozdělené pracovní postupy |
| **Bezpečnostní omezení** | Přímý přístup k databázím zvyšuje bezpečnostní a shodové rizika | Omezené nasazení, manuální příprava dat |
| **Komplexní dotazy** | Obchodní uživatelé potřebují technické znalosti k získání datových poznatků | Snížené užití, neefektivní procesy |

### Řešení MCP

Model Context Protocol řeší tyto výzvy tím, že poskytuje:

- **Přístup k datům v reálném čase**: AI asistenti dotazují živé databáze a API
- **Bezpečná integrace**: Řízený přístup s autentizací a oprávněními
- **Rozhraní v přirozeném jazyce**: Obchodní uživatelé kladou otázky běžnou angličtinou
- **Standardizovaný protokol**: Funguje napříč různými AI platformami a nástroji

## 🏪 Poznejte Zava Retail: náš případ studie https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

V průběhu této výukové cesty postavíme MCP server pro **Zava Retail**, fiktivní řetězec DIY obchodů s více pobočkami. Tento realistický scénář demonstruje implementaci MCP na podnikové úrovni.

### Obchodní kontext

**Zava Retail** provozuje:
- **8 fyzických obchodů** ve státě Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 internetový obchod** pro e-commerce prodeje
- **Rozmanitý katalog produktů** včetně nářadí, hardwaru, zahradnických potřeb a stavebních materiálů
- **Víceúrovňové řízení** se správci obchodů, regionálními manažery a vedením

### Obchodní požadavky

Správci obchodů a vedení potřebují AI řízenou analytiku k:

1. **Analyzovat výkonnost prodeje** napříč obchody a časovými obdobími
2. **Sledovat stavy zásob** a identifikovat potřeby doplnění
3. **Pochopit chování zákazníků** a nákupní vzorce
4. **Objevovat produktové poznatky** pomocí sémantického vyhledávání
5. **Generovat reporty** s dotazy v přirozeném jazyce
6. **Udržovat bezpečnost dat** s řízením přístupu založeným na rolích

### Technické požadavky

MCP server musí poskytovat:

- **Multi-tenant přístup k datům**, kde správci obchodů vidí data pouze svého obchodu
- **Flexibilní dotazování** podporující složité SQL operace
- **Sémantické vyhledávání** pro objevování produktů a doporučení
- **Data v reálném čase** odrážející aktuální obchodní stav
- **Bezpečná autentizace** s rolovou bezpečností (RLS)
- **Škálovatelná architektura** podporující více současných uživatelů

## 🏗️ Přehled architektury MCP serveru

Náš MCP server implementuje vrstvenou architekturu optimalizovanou pro integraci databáze:

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
- **Kontext požadavku**: Správa identity uživatele a session
- **Zpracování chyb**: Robustní správa chyb a protokolování

#### **2. Vrstva integrace databáze**
- **Správa připojení**: Efektivní správa připojení asyncpg
- **Poskytovatel schématu**: Dynamické zjišťování schémat tabulek
- **Exekutor dotazů**: Bezpečné vykonávání SQL s RLS kontextem
- **Správa transakcí**: ACID kompatibilita a správa rollbacků

#### **3. Bezpečnostní vrstva**
- **Row Level Security**: PostgreSQL RLS pro izolaci multi-tenant dat
- **Identita uživatele**: Autentizace a autorizace správců obchodů
- **Řízení přístupu**: Jemnozrnná oprávnění a auditní stopy
- **Validace vstupů**: Prevence SQL injekce a validace dotazů

#### **4. Vrstva AI vylepšení**
- **Sémantické vyhledávání**: Vektorová embedding pro objevení produktů
- **Integrace Azure OpenAI**: Generování textových embeddingů
- **Algoritmy podobnosti**: pgvector vyhledávání podle kosinové podobnosti
- **Optimalizace vyhledávání**: Indexace a ladění výkonu

## 🔧 Technologický stack

### Klíčové technologie

| **Komponenta** | **Technologie** | **Účel** |
|---------------|----------------|-------------|
| **MCP Framework** | FastMCP (Python) | Moderní implementace MCP serveru |
| **Databáze** | PostgreSQL 17 + pgvector | Relační data s vektorovým vyhledáváním |
| **AI služby** | Azure OpenAI | Textové embeddingy a jazykové modely |
| **Kontejnerizace** | Docker + Docker Compose | Vývojové prostředí |
| **Cloud platforma** | Microsoft Azure | Produkční nasazení |
| **Integrace IDE** | VS Code | AI Chat a vývojový workflow |

### Vývojové nástroje

| **Nástroj** | **Účel** |
|----------|-------------|
| **asyncpg** | Vysoce výkonný PostgreSQL ovladač |
| **Pydantic** | Validace a serializace dat |
| **Azure SDK** | Integrace cloudových služeb |
| **pytest** | Testovací framework |
| **Docker** | Kontejnerizace a nasazení |

### Produkční stack

| **Služba** | **Azure zdroj** | **Účel** |
|-------------|-------------------|-------------|
| **Databáze** | Azure Database for PostgreSQL | Spravovaná databázová služba |
| **Kontejner** | Azure Container Apps | Serverless hosting kontejnerů |
| **AI služby** | Microsoft Foundry | OpenAI modely a endpointy |
| **Monitoring** | Application Insights | Pozorovatelnost a diagnostika |
| **Bezpečnost** | Azure Key Vault | Správa tajemství a konfigurace |

## 🎬 Použití v reálném světě

Prozkoumejme, jak různí uživatelé interagují s naším MCP serverem:

### Scénář 1: Přehled výkonu správce obchodu

**Uživatel**: Sarah, správkyně obchodu v Seattle  
**Cíl**: Analyzovat prodeje za poslední čtvrtletí

**Dotaz v přirozeném jazyce**:
> "Ukaž mi top 10 produktů podle tržeb za můj obchod ve 4. čtvrtletí 2024"

**Co se stane**:
1. VS Code AI Chat odešle dotaz MCP serveru
2. MCP server identifikuje kontext Sarahina obchodu (Seattle)
3. RLS pravidla filtrují data pouze pro obchod v Seattle
4. SQL dotaz je vytvořen a spuštěn
5. Výsledky jsou zformátovány a vráceny do AI Chatu
6. AI poskytne analýzu a poznatky

### Scénář 2: Objevování produktů s pomocí sémantického vyhledávání

**Uživatel**: Mike, manažer inventáře  
**Cíl**: Najít produkty podobné požadavku zákazníka

**Dotaz v přirozeném jazyce**:
> "Jaké produkty prodáváme, které jsou podobné 'vodotěsným elektrickým konektorům pro venkovní použití'?"

**Co se stane**:
1. Dotaz je zpracován nástrojem sémantického vyhledávání
2. Azure OpenAI generuje vektor embeddingu
3. pgvector provádí vyhledávání podle podobnosti
4. Související produkty jsou seřazeny podle relevance
5. Výsledky obsahují detail produktu a dostupnost
6. AI navrhuje alternativy a příležitosti k balení produktů

### Scénář 3: Analýza napříč obchody

**Uživatel**: Jennifer, regionální manažerka  
**Cíl**: Porovnat výkon všech obchodů

**Dotaz v přirozeném jazyce**:
> "Porovnej prodeje podle kategorií za posledních 6 měsíců ve všech obchodech"

**Co se stane**:
1. RLS kontext je nastaven pro přístup regionální manažerky
2. Generuje se složitý dotaz napříč obchody
3. Data jsou agregována napříč jednotlivými pobočkami
4. Výsledky obsahují trendy a porovnání
5. AI identifikuje poznatky a doporučení

## 🔒 Hloubkový pohled na bezpečnost a multi-tenancy

Naše implementace klade důraz na bezpečnost na úrovni podniku:

### Rolová bezpečnost na úrovni řádku (RLS)

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
- **ID správce obchodu**: Unikátní identifikátor pro RLS kontext
- **Role assignment**: Oprávnění a přístupové úrovně
- **Správa session**: Bezpečné autentizační tokeny
- **Auditní logování**: Kompletní historie přístupů

### Ochrana dat

Více vrstev bezpečnosti:
- **Šifrování připojení**: TLS pro všechna databázová připojení
- **Prevence SQL injekce**: Pouze parametrizované dotazy
- **Validace vstupu**: Komplexní kontrola požadavků
- **Zpracování chyb**: Bez citlivých dat ve zprávách o chybách

## 🎯 Klíčové poznatky

Po dokončení tohoto úvodu byste měli rozumět:

✅ **Hodnotová nabídka MCP**: Jak MCP propojuje AI asistenty a data ze skutečného světa  
✅ **Obchodní kontext**: Požadavky a výzvy Zava Retail  
✅ **Přehled architektury**: Klíčové komponenty a jejich interakce  
✅ **Technologický stack**: Použité nástroje a frameworky  
✅ **Bezpečnostní model**: Multi-tenant přístup k datům a ochrana  
✅ **Použité vzory**: Reálné scénáře dotazů a pracovní postupy  

## 🚀 Co dál

Připraveni jít hlouběji? Pokračujte v:

**[Lab 01: Základní architektonické koncepty](../01-Architecture/README.md)**

Naučte se o vzorech architektury MCP serverů, zásadách návrhu databází a podrobné technické implementaci, která pohání naše maloobchodní analytické řešení.

## 📚 Další zdroje

### Dokumentace MCP
- [Specifikace MCP](https://modelcontextprotocol.io/docs/) - Oficiální dokumentace protokolu
- [MCP pro začátečníky](https://aka.ms/mcp-for-beginners) - Komplexní průvodce učením MCP
- [FastMCP Dokumentace](https://github.com/modelcontextprotocol/python-sdk) - Dokumentace Python SDK

### Integrace databáze
- [PostgreSQL Dokumentace](https://www.postgresql.org/docs/) - Kompletní reference PostgreSQL
- [pgvector Průvodce](https://github.com/pgvector/pgvector) - Dokumentace vektorového rozšíření
- [Rolová bezpečnost na úrovni řádků](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Průvodce PostgreSQL RLS

### Azure služby
- [Azure OpenAI Dokumentace](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integrace AI služeb
- [Azure Database pro PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Spravovaná databázová služba
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverless kontejnery

---

**Prohlášení**: Toto je výukové cvičení využívající fiktivní maloobchodní data. Vždy dodržujte datovou správu a bezpečnostní politiky vaší organizace při implementaci podobných řešení v produkčním prostředí.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->