# Einführung in die Integration der MCP-Datenbank

> [!NOTE]
> Diagramme oder Code in diesem Lernpfad, die HTTP/SSE oder Initialisierungs-
> optionen verwenden, spiegeln die Abhängigkeiten des Musters MCP `2025-11-25` wider. Für neue
> Implementierungen verwenden Sie bitte `2026-07-28` zustandslose Anfragen und Streamable HTTP.

## 🎯 Was dieses Labor abdeckt

Dieses Einführungs-Labor bietet einen umfassenden Überblick über den Aufbau von Model Context Protocol (MCP)-Servern mit Datenbankintegration. Sie erhalten ein Verständnis für den Business Case, die technische Architektur und reale Anwendungsfälle anhand des Zava Retail Analytics Use Case unter https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Überblick

**Model Context Protocol (MCP)** ermöglicht es KI-Assistenten, sicher in Echtzeit auf externe Datenquellen zuzugreifen und mit ihnen zu interagieren. In Kombination mit der Datenbankintegration eröffnet MCP leistungsstarke Möglichkeiten für datengesteuerte KI-Anwendungen.

Dieser Lernpfad zeigt Ihnen, wie Sie produktionsreife MCP-Server erstellen, die KI-Assistenten mit Verkaufsdaten im Einzelhandel über PostgreSQL verbinden und dabei Unternehmensmuster wie Row Level Security, semantische Suche und mandantenfähigen Datenzugriff umsetzen.

## Lernziele

Am Ende dieses Labors können Sie:

- **Definieren** des Model Context Protocol und seine Kernvorteile für die Datenbankintegration
- **Identifizieren** der Schlüsselfaktoren einer MCP-Serverarchitektur mit Datenbanken
- **Verstehen** des Zava Retail Use Case und seiner geschäftlichen Anforderungen
- **Erkennen** von Unternehmensmustern für sicheren und skalierbaren Datenbankzugriff
- **Auflisten** der in diesem Lernpfad verwendeten Werkzeuge und Technologien

## 🧭 Die Herausforderung: KI trifft reale Daten

### Traditionelle KI-Einschränkungen

Moderne KI-Assistenten sind äußerst mächtig, stoßen jedoch bei der Arbeit mit realen Geschäftsdaten auf erhebliche Einschränkungen:

| **Herausforderung** | **Beschreibung** | **Geschäftliche Auswirkungen** |
|---------------|-----------------|-------------------|
| **Statisches Wissen** | KI-Modelle, die auf festen Datensätzen trainiert wurden, haben keinen Zugriff auf aktuelle Geschäftsdaten | Veraltete Erkenntnisse, verpasste Chancen |
| **Datensilos** | Informationen, die in Datenbanken, APIs und Systemen eingeschlossen sind und für KI nicht zugänglich sind | Unvollständige Analyse, fragmentierte Arbeitsabläufe |
| **Sicherheitsbeschränkungen** | Direkter Datenbankzugriff birgt Sicherheits- und Compliance-Bedenken | Eingeschränkte Nutzung, manuelle Datenaufbereitung |
| **Komplexe Abfragen** | Geschäftsanwender benötigen technisches Know-how zur Datenanalyse | Geringe Akzeptanz, ineffiziente Prozesse |

### Die MCP-Lösung

Das Model Context Protocol adressiert diese Herausforderungen, indem es bietet:

- **Echtzeit-Datenzugriff**: KI-Assistenten fragen Live-Datenbanken und APIs ab
- **Sichere Integration**: Kontrollierter Zugriff mit Authentifizierung und Berechtigungen
- **Natürliche Sprachschnittstelle**: Geschäftsanwender stellen Fragen in klarem Englisch
- **Standardisiertes Protokoll**: Funktioniert plattform- und werkzeugübergreifend

## 🏪 Lernen Sie Zava Retail kennen: Unsere Fallstudie https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Im Verlauf dieses Lernpfads erstellen wir einen MCP-Server für **Zava Retail**, eine fiktive Heimwerker-Einzelhandelskette mit mehreren Filialstandorten. Dieses realistische Szenario zeigt eine MCP-Implementierung auf Unternehmensniveau.

### Geschäftskontext

**Zava Retail** betreibt:
- **8 stationäre Geschäfte** im Bundesstaat Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 Onlineshop** für E-Commerce-Verkäufe
- **Vielfältigen Produktkatalog** inklusive Werkzeuge, Hardware, Gartenzubehör und Baumaterialien
- **Mehrstufiges Management** mit Filialleitern, Regionalleitern und Führungskräften

### Geschäftliche Anforderungen

Filialleiter und Führungskräfte benötigen KI-gestützte Analysen, um:

1. **Verkaufsleistung analysieren** über Filialen und Zeiträume hinweg
2. **Lagerbestände überwachen** und Nachfüllbedarfe erkennen
3. **Kundenverhalten verstehen** und Kaufmuster erkennen
4. **Produktinformationen entdecken** durch semantische Suche
5. **Berichte erzeugen** mit natürlichsprachlichen Abfragen
6. **Datensicherheit gewährleisten** durch rollenbasierte Zugriffskontrolle

### Technische Anforderungen

Der MCP-Server muss bieten:

- **Mandantenfähigen Datenzugriff**, bei dem Filialleiter nur Daten ihrer eigenen Filiale sehen
- **Flexible Abfragen**, die komplexe SQL-Operationen unterstützen
- **Semantische Suche** zur Produktsuche und Empfehlungen
- **Echtzeitdaten**, die den aktuellen Geschäftsstatus abbilden
- **Sichere Authentifizierung** mit Row Level Security
- **Skalierbare Architektur** zur Unterstützung mehrerer gleichzeitiger Nutzer

## 🏗️ Überblick zur MCP-Server-Architektur

Unser MCP-Server implementiert eine Schichtenarchitektur, die für die Datenbankintegration optimiert ist:

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

### Hauptkomponenten

#### **1. MCP-Server-Schicht**
- **FastMCP Framework**: Moderne Python-Implementierung des MCP-Servers
- **Tool-Registrierung**: Deklarative Tool-Definitionen mit Typensicherheit
- **Anfragekontext**: Benutzeridentität und Sitzungsverwaltung
- **Fehlerbehandlung**: Robustes Fehler-Management und Protokollierung

#### **2. Datenbank-Integrations-Schicht**
- **Connection Pooling**: Effiziente Verwaltung von asyncpg-Verbindungen
- **Schema Provider**: Dynamische Entdeckung von Tabellenschemata
- **Query Executor**: Sichere Ausführung von SQL mit RLS-Kontext
- **Transaktionsmanagement**: ACID-Konformität und Rollback-Behandlung

#### **3. Sicherheitsschicht**
- **Row Level Security**: PostgreSQL RLS für mandantenfähige Datenisolation
- **Benutzeridentität**: Authentifizierung und Autorisierung von Filialleitern
- **Zugriffskontrolle**: Feingranulare Berechtigungen und Prüfungspfad
- **Eingabevalidierung**: Verhinderung von SQL-Injektionen und Abfragevalidierung

#### **4. KI-Erweiterungsschicht**
- **Semantische Suche**: Vektor-Embeddings zur Produktsuche
- **Azure OpenAI Integration**: Generierung von Text-Embeddings
- **Ähnlichkeitsalgorithmen**: pgvector Cosinus-Ähnlichkeitssuche
- **Suchoptimierung**: Indexierung und Leistungsoptimierung

## 🔧 Technologiestack

### Kerntechnologien

| **Komponente** | **Technologie** | **Zweck** |
|---------------|----------------|-------------|
| **MCP Framework** | FastMCP (Python) | Moderne MCP-Server-Implementierung |
| **Datenbank** | PostgreSQL 17 + pgvector | Relationale Daten mit Vektorsuche |
| **KI-Dienste** | Azure OpenAI | Text-Embeddings und Sprachmodelle |
| **Containerisierung** | Docker + Docker Compose | Entwicklungsumgebung |
| **Cloud-Plattform** | Microsoft Azure | Produktionsbereitstellung |
| **IDE-Integration** | VS Code | AI Chat und Entwicklungs-Workflow |

### Entwicklungstools

| **Tool** | **Zweck** |
|----------|-------------|
| **asyncpg** | Hochleistungs-PostgreSQL-Treiber |
| **Pydantic** | Datenvalidierung und Serialisierung |
| **Azure SDK** | Integration von Cloud-Diensten |
| **pytest** | Test-Framework |
| **Docker** | Containerisierung und Bereitstellung |

### Produktionsstack

| **Dienst** | **Azure-Ressource** | **Zweck** |
|-------------|-------------------|-------------|
| **Datenbank** | Azure Database for PostgreSQL | Verwalteter Datenbankdienst |
| **Container** | Azure Container Apps | Serverless Container-Hosting |
| **KI-Dienste** | Microsoft Foundry | OpenAI-Modelle und Endpunkte |
| **Überwachung** | Application Insights | Beobachtbarkeit und Diagnostik |
| **Sicherheit** | Azure Key Vault | Geheimnisse und Konfigurationsmanagement |

## 🎬 Realistische Anwendungsszenarien

Lassen Sie uns ansehen, wie unterschiedliche Nutzer mit unserem MCP-Server interagieren:

### Szenario 1: Performance-Review eines Filialleiters

**Benutzer**: Sarah, Filialleiterin Seattle  
**Ziel**: Analyse der Verkaufsleistung im letzten Quartal

**Natürliche Sprachabfrage**:
> "Zeige mir die Top 10 Produkte nach Umsatz für meine Filiale im Q4 2024"

**Ablauf**:
1. VS Code AI Chat sendet Anfrage an MCP-Server
2. MCP-Server ermittelt den Filialkontext für Sarah (Seattle)
3. RLS-Richtlinien filtern Daten nur für die Seattle-Filiale
4. SQL-Abfrage wird generiert und ausgeführt
5. Ergebnisse werden formatiert und an AI Chat zurückgegeben
6. KI liefert Analyse und Erkenntnisse

### Szenario 2: Produktsuche mit semantischer Suche

**Benutzer**: Mike, Lagerverwalter  
**Ziel**: Produkte finden, die einer Kundenanfrage ähnlich sind

**Natürliche Sprachabfrage**:
> "Welche Produkte verkaufen wir, die ähnlich sind wie ‘wasserfeste elektrische Verbinder für den Außenbereich’?"

**Ablauf**:
1. Abfrage wird vom semantischen Suchwerkzeug verarbeitet
2. Azure OpenAI erstellt Embedding-Vektor
3. pgvector führt Ähnlichkeitssuche durch
4. Verwandte Produkte werden nach Relevanz bewertet
5. Ergebnisse enthalten Produktdetails und Verfügbarkeit
6. KI schlägt Alternativen und Bündelungsmöglichkeiten vor

### Szenario 3: Filialübergreifende Analysen

**Benutzer**: Jennifer, Regionalleiterin  
**Ziel**: Vergleich der Leistung aller Filialen

**Natürliche Sprachabfrage**:
> "Vergleiche den Umsatz nach Kategorien für alle Filialen in den letzten 6 Monaten"

**Ablauf**:
1. RLS-Kontext wird für den Zugriff der Regionalleiterin gesetzt
2. Komplexe Multi-Store-Abfrage wird generiert
3. Daten werden filialeübergreifend aggregiert
4. Ergebnisse enthalten Trends und Vergleiche
5. KI identifiziert Erkenntnisse und Empfehlungen

## 🔒 Sicherheit und Mandantenfähigkeit im Detail

Unsere Implementierung legt Wert auf Sicherheit auf Unternehmensniveau:

### Row Level Security (RLS)

PostgreSQL RLS gewährleistet Datenisolation:

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

### Benutzeridentitätsmanagement

Jede MCP-Verbindung enthält:
- **Filialleiter-ID**: Eindeutige Kennung für den RLS-Kontext
- **Rollenzuweisung**: Berechtigungen und Zugriffslevel
- **Sitzungsverwaltung**: Sichere Authentifizierungstokens
- **Audit-Protokollierung**: Vollständige Zugriffshistorie

### Datenschutz

Mehrstufige Sicherheitsmaßnahmen:
- **Verbindungsverschlüsselung**: TLS für alle Datenbankverbindungen
- **Verhinderung von SQL-Injektionen**: Nur parametrisierte Abfragen
- **Eingabevalidierung**: Umfassende Anfragvalidierung
- **Fehlerbehandlung**: Keine sensiblen Daten in Fehlermeldungen

## 🎯 Wichtige Erkenntnisse

Nach Abschluss dieser Einführung sollten Sie verstehen:

✅ **MCP-Wertversprechen**: Wie MCP KI-Assistenten und reale Daten verbindet  
✅ **Geschäftskontext**: Anforderungen und Herausforderungen von Zava Retail  
✅ **Architekturüberblick**: Hauptkomponenten und deren Zusammenspiel  
✅ **Technologiestack**: Werkzeuge und Frameworks im gesamten Lernpfad  
✅ **Sicherheitsmodell**: Mandantenfähiger Datenzugriff und Schutz  
✅ **Nutzungsmuster**: Reale Abfrageszenarien und Arbeitsabläufe  

## 🚀 Was als Nächstes kommt

Bereit für den nächsten Schritt? Fahren Sie fort mit:

**[Labor 01: Kernkonzepte der Architektur](../01-Architecture/README.md)**

Lernen Sie MCP-Server-Architekturmuster, Prinzipien der Datenbankgestaltung und die detaillierte technische Umsetzung kennen, die unsere Retail-Analytics-Lösung antreibt.

## 📚 Weitere Ressourcen

### MCP-Dokumentation
- [MCP-Spezifikation](https://modelcontextprotocol.io/docs/) – Offizielle Protokolldokumentation
- [MCP für Einsteiger](https://aka.ms/mcp-for-beginners) – Umfassender MCP-Lernleitfaden
- [FastMCP-Dokumentation](https://github.com/modelcontextprotocol/python-sdk) – Python SDK-Dokumentation

### Datenbankintegration
- [PostgreSQL-Dokumentation](https://www.postgresql.org/docs/) – Vollständige PostgreSQL-Referenz
- [pgvector-Anleitung](https://github.com/pgvector/pgvector) – Dokumentation zur Vektorerweiterung
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) – PostgreSQL RLS-Anleitung

### Azure-Dienste
- [Azure OpenAI-Dokumentation](https://docs.microsoft.com/azure/cognitive-services/openai/) – Integration von KI-Diensten
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) – Verwalteter Datenbankdienst
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) – Serverlose Container

---

**Haftungsausschluss**: Dies ist eine Lernübung mit fiktiven Einzelhandelsdaten. Befolgen Sie stets die Datenverwaltungs- und Sicherheitsrichtlinien Ihrer Organisation bei der Implementierung ähnlicher Lösungen in produktiven Umgebungen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->