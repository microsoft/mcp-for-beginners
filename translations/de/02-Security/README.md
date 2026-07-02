# MCP-Sicherheit: Umfassender Schutz für KI-Systeme

[![MCP Security Best Practices](../../../translated_images/de/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

Sicherheit ist grundlegend für das Design von KI-Systemen, weshalb wir ihr als zweiten Abschnitt Priorität einräumen. Dies entspricht dem Microsoft-Grundsatz **Secure by Design** aus der [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Das Model Context Protocol (MCP) bringt leistungsstarke neue Funktionen für KI-gesteuerte Anwendungen, während es einzigartige Sicherheitsherausforderungen einführt, die über traditionelle Software-Risiken hinausgehen. MCP-Systeme sehen sich sowohl etablierten Sicherheitsbedenken (sicheres Programmieren, geringstmögliche Rechte, Sicherheit der Lieferkette) als auch neuen KI-spezifischen Bedrohungen gegenüber, darunter Prompt Injection, Tool Poisoning, Session Hijacking, Confused Deputy Attacken, Token-Passthrough-Schwachstellen und dynamische Fähigkeitsänderungen.

Diese Lektion untersucht die kritischsten Sicherheitsrisiken in MCP-Implementierungen—mit Fokus auf Authentifizierung, Autorisierung, übermäßige Berechtigungen, indirekte Prompt Injection, Sitzungs­sicherheit, Confused Deputy-Probleme, Token-Verwaltung und Lieferketten­angriffe. Sie lernen umsetzbare Kontrollen und bewährte Praktiken kennen, um diese Risiken zu mindern und gleichzeitig Microsoft-Lösungen wie Prompt Shields, Azure Content Safety und GitHub Advanced Security zur Stärkung Ihrer MCP-Einführung zu nutzen.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- **MCP-spezifische Bedrohungen identifizieren**: Einzigartige Sicherheitsrisiken in MCP-Systemen erkennen, einschließlich Prompt Injection, Tool Poisoning, übermäßige Berechtigungen, Session Hijacking, Confused Deputy-Problemen, Token-Passthrough-Schwachstellen und Risiken in der Lieferkette
- **Sicherheitskontrollen anwenden**: Effektive Gegenmaßnahmen implementieren, darunter robuste Authentifizierung, Zugriff mit geringsten Rechten, sichere Token-Verwaltung, Sitzungs­sicherheits­kontrollen und Verifikation der Lieferkette
- **Microsoft-Sicherheitslösungen nutzen**: Microsoft Prompt Shields, Azure Content Safety und GitHub Advanced Security zum Schutz von MCP-Workloads verstehen und einsetzen
- **Toolsicherheit validieren**: Bedeutung der Validierung von Tool-Metadaten, Überwachung dynamischer Änderungen und Abwehr gegen indirekte Prompt Injection-Angriffe erkennen
- **Best Practices integrieren**: Etablierte Sicherheitsgrundlagen (sicheres Programmieren, Server-Härtung, Zero Trust) mit MCP-spezifischen Kontrollen für umfassenden Schutz verbinden

# MCP-Sicherheitsarchitektur & Kontrollen

Moderne MCP-Implementierungen erfordern geschichtete Sicherheitsansätze, die sowohl traditionelle Software-Sicherheit als auch KI-spezifische Bedrohungen adressieren. Die sich rasch entwickelnde MCP-Spezifikation reift weiter und verbessert ihre Sicherheitskontrollen, um eine bessere Integration in Unternehmenssicherheitsarchitekturen und etablierte Best Practices zu ermöglichen.

Forschung aus dem [Microsoft Digital Defense Report](https://aka.ms/mddr) zeigt, dass **98 % der gemeldeten Sicherheitsvorfälle durch robuste Sicherheits­hygiene verhindert werden könnten**. Die effektivste Schutzstrategie kombiniert grundlegende Sicherheitspraktiken mit MCP-spezifischen Kontrollen—bewährte Basisschutzmaßnahmen sind weiterhin am wirkungsvollsten zur Reduzierung des Gesamtrisikos.

## Aktuelle Sicherheitslage

> **Hinweis:** Diese Informationen spiegeln den Stand der MCP-Sicherheitsstandards vom **5. Februar 2026** wider, abgestimmt auf die **MCP Specification 2025-11-25**. Das MCP-Protokoll entwickelt sich schnell weiter, und zukünftige Implementierungen können neue Authentifizierungsmuster und erweiterte Kontrollen einführen. Konsultieren Sie stets die aktuelle [MCP Specification](https://spec.modelcontextprotocol.io/), das [MCP GitHub-Repository](https://github.com/modelcontextprotocol) und die [Sicherheits-Best-Practices-Dokumentation](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) für die neuesten Empfehlungen.

> **Ausblick:** Der Release Candidate vom `2026-07-28` verschärft die Autorisierung weiter — Clients müssen den `iss`-Parameter in Autorisierungsantworten validieren (RFC 9207), während der dynamischen Client-Registrierung einen OpenID Connect `application_type` angeben und registrierte Anmelde­informationen an den ausstellenden Autorisierungs­server binden. Details finden Sie in [Was ändert sich in MCP: Der Release Candidate 2026-07-28](../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

## 🏔️ MCP Security Summit Workshop (Sherpa)

Für **praktische Sicherheitsschulungen** empfehlen wir den **MCP Security Summit Workshop** (Sherpa) – eine umfassende geführte Expedition zur Absicherung von MCP-Servern in Microsoft Azure.

### Workshop-Übersicht

Der [MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) bietet praktische, umsetzbare Sicherheitsschulungen mit einer bewährten Methodik „anfällige Systeme → Angriff → Behebung → Validierung“. Sie:

- **Lernen durch Fehler:** Erleben Sie Sicherheitslücken direkt durch das Ausnutzen absichtlich unsicherer Server
- **Nutzen Azure-eigene Sicherheit:** Verwenden Sie Azure Entra ID, Key Vault, API Management und AI Content Safety
- **Folgen einer Defense-in-Depth-Strategie:** Vorrücken durch Camps zur Etablierung umfassender Sicherheitsschichten
- **Übernehmen OWASP-Standards:** Jede Technik ist mit dem [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) abgestimmt
- **Erhalten produktionsfähigen Code:** Gehen Sie mit funktionierenden, getesteten Implementierungen ab

### Die Expeditionsroute

| Camp | Fokus | Abgedeckte OWASP-Risiken |
|------|-------|--------------------------|
| **Basislager** | MCP-Grundlagen & Authentifizierungs-Schwachstellen | MCP01, MCP07 |
| **Camp 1: Identität** | OAuth 2.1, Azure Managed Identity, Key Vault | MCP01, MCP02, MCP07 |
| **Camp 2: Gateway** | API Management, Private Endpoints, Governance | MCP02, MCP06, MCP07, MCP09 |
| **Camp 3: I/O-Sicherheit** | Prompt Injection, PII-Schutz, Content Safety | MCP03, MCP05, MCP06, MCP10 |
| **Camp 4: Überwachung** | Log Analytics, Dashboards, Bedrohungserkennung | MCP04, MCP08 |
| **Der Gipfel** | Red Team / Blue Team Integrationstest | Alle |

**Jetzt starten**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 Sicherheitsrisiken

Der [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) beschreibt die zehn kritischsten Sicherheitsrisiken für MCP-Implementierungen:

| Risiko | Beschreibung | Azure-Minderung |
|--------|--------------|-----------------|
| **MCP01** | Fehlmanagement von Token & Offenlegung von Geheimnissen | Azure Key Vault, Managed Identity |
| **MCP02** | Privilegieneskalation durch Scope Creep | RBAC, Conditional Access |
| **MCP03** | Tool Poisoning | Tool-Validierung, Integritätsprüfung |
| **MCP04** | Software-Lieferketten-Angriffe & Manipulation von Abhängigkeiten | GitHub Advanced Security, Abhängigkeits-Scan |
| **MCP05** | Befehls-Injektion & Ausführung | Eingabevalidierung, Sandboxing |
| **MCP06** | Subversion des Intent-Flows | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Unzureichende Authentifizierung & Autorisierung | Azure Entra ID, OAuth 2.1 mit PKCE |
| **MCP08** | Mangel an Audit und Telemetrie | Azure Monitor, Application Insights |
| **MCP09** | Schatten-MCP-Server | API-Center-Governance, Netzwerkisolation |
| **MCP10** | Kontextinjektion & Überfreigabe | Datenklassifizierung, minimale Exposition |

### Entwicklung der MCP-Authentifizierung

Die MCP-Spezifikation hat sich bei Authentifizierung und Autorisierung deutlich weiterentwickelt:

- **Ursprünglicher Ansatz**: Frühe Spezifikationen verlangten, dass Entwickler eigene Authentifizierungsserver implementieren, während MCP-Server als OAuth 2.0 Authorization Server direkt die Benutzer­authentifizierung verwalteten
- **Aktueller Standard (2025-11-25)**: Die aktualisierte Spezifikation erlaubt MCP-Servern, die Authentifizierung an externe Identitätsanbieter (wie Microsoft Entra ID) zu delegieren, was die Sicherheitslage verbessert und die Komplexität der Implementierung reduziert
- **Transportschicht-Sicherheit**: Verbesserte Unterstützung für sichere Transportmechanismen mit passenden Authentifizierungs­mustern für lokale (STDIO) und entfernte (Streamable HTTP) Verbindungen

## Sicherheitsaspekte von Authentifizierung & Autorisierung

### Aktuelle Herausforderungen

Moderne MCP-Implementierungen sehen sich mehreren Herausforderungen bei Authentifizierung und Autorisierung gegenüber:

### Risiken & Angriffsvektoren

- **Fehlkonfigurierte Autorisierungs-Logik**: Fehlerhafte Implementierungen der Autorisierung in MCP-Servern können sensible Daten preisgeben und Zugriffs­kontrollen fehlerhaft anwenden
- **Kompromittierung von OAuth-Token**: Diebstahl von Token des lokalen MCP-Servers ermöglicht Angreifern, Server zu imitieren und Zugriff auf nachgelagerte Dienste zu erlangen
- **Token-Passthrough-Schwachstellen**: Unsachgemäße Token-Handhabung erlaubt Sicherheitskontrollen zu umgehen und erschwert Verantwortlichkeit
- **Übermäßige Berechtigungen**: MCP-Server mit zu vielen Rechten verstoßen gegen das Prinzip der geringsten Rechte und vergrößern Angriffsflächen

#### Token Passthrough: Ein kritisches Anti-Pattern

**Token Passthrough ist in der aktuellen MCP-Autorisierungs­spezifikation ausdrücklich verboten** aufgrund schwerwiegender Sicherheits­auswirkungen:

##### Umgehung von Sicherheitskontrollen
- MCP-Server und nachgelagerte APIs implementieren wichtige Sicherheits­kontrollen (Rate Limiting, Anfragenvalidierung, Verkehrsüberwachung), die von korrekter Token-Validierung abhängen
- Direkte Client-zu-API-Token-Nutzung umgeht diese essentiellen Schutzmaßnahmen und untergräbt die Sicherheitsarchitektur

##### Herausforderungen bei Verantwortlichkeit & Audit  
- MCP-Server können nicht zwischen Clients unterscheiden, die mit Upstream ausgestellten Tokens agieren, was Prüffähigkeit und Nachvollziehbarkeit bricht
- Protokolle nachgelagerter Resource-Server zeigen irreführende Ursprünge der Anfragen statt der tatsächlichen MCP-Server-Intermediäre
- Untersuchung von Vorfällen und Compliance-Prüfungen werden deutlich erschwert

##### Risiko der Datenexfiltration
- Unvalidierte Token-Claims ermöglichen es Angreifern mit gestohlenen Tokens, MCP-Server als Proxies für Datenabfluss zu nutzen
- Vertrauensgrenzen werden verletzt, wodurch unautorisierte Zugriffsmuster die beabsichtigten Sicherheitskontrollen umgehen

##### Angriffsmöglichkeiten über mehrere Dienste
- Akzeptierte kompromittierte Tokens, die von mehreren Diensten akzeptiert werden, erlauben laterale Bewegungen über verbundene Systeme
- Vertrauensannahmen zwischen Diensten können verletzt werden, wenn Token-Herkünfte nicht verifiziert werden können

### Sicherheitskontrollen & Gegenmaßnahmen

**Kritische Sicherheitsanforderungen:**

> **VERPFLICHTEND:** MCP-Server **DÜRFEN NICHT** Tokens akzeptieren, die nicht ausdrücklich für den MCP-Server ausgestellt wurden

#### Authentifizierungs- & Autorisierungskontrollen

- **Sorgfältige Überprüfung der Autorisierung**: Umfassende Audits der Autorisierungslogik in MCP-Servern, um sicherzustellen, dass nur beabsichtigte Nutzer und Clients auf sensible Ressourcen zugreifen können
  - **Implementierungsleitfaden**: [Azure API Management als Authentifizierungs-Gateway für MCP-Server](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identitätsintegration**: [Microsoft Entra ID zur MCP-Server-Authentifizierung nutzen](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Sichere Token-Verwaltung**: Umsetzung von [Microsofts Best Practices für Token-Validierung und Lebenszyklus](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validierung der Token-Audience-Claims zur Übereinstimmung mit der MCP-Server-Identität
  - Angemessene Token-Rotation und Ablaufstrategien
  - Verhinderung von Token-Wiederholungsangriffen und unbefugter Verwendung

- **Geschütztes Token-Storage**: Sichere Speicherung von Tokens mit Verschlüsselung im Ruhezustand und während der Übertragung
  - **Best Practices**: [Sicheres Token-Storage und Verschlüsselungsrichtlinien](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Umsetzung von Zugriffskontrollen

- **Prinzip der geringsten Rechte**: MCP-Server erhalten nur die minimal notwendigen Berechtigungen für die vorgesehene Funktionalität
  - Regelmäßige Überprüfung und Aktualisierung der Berechtigungen, um Privilegienausweitungen zu verhindern
  - **Microsoft-Dokumentation**: [Sicherer Zugriff mit geringsten Privilegien](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rollenbasierte Zugriffskontrolle (RBAC)**: Implementierung fein granulärer Rollen­zuweisungen
  - Rollen eng auf spezifische Ressourcen und Aktionen einschränken
  - Breite oder unnötige Berechtigungen vermeiden, die Angriffsflächen vergrößern

- **Kontinuierliche Berechtigungsüberwachung**: Laufende Überwachung und Auditierung des Zugriffs
  - Überwachung von Berechtigungsnutzungsmustern auf Anomalien
  - Rasche Behebung von übermäßigen oder ungenutzten Rechten

## KI-spezifische Sicherheitsbedrohungen

### Prompt Injection & Tool-Manipulationsangriffe

Moderne MCP-Implementierungen sind komplexen, KI-spezifischen Angriffsvektoren ausgesetzt, die traditionelle Sicherheitsmaßnahmen nicht vollständig adressieren können:

#### **Indirekte Prompt Injection (Cross-Domain Prompt Injection)**

**Indirekte Prompt Injection** zählt zu den kritischsten Schwachstellen in MCP-gestützten KI-Systemen. Angreifer betten bösartige Anweisungen in externe Inhalte ein—Dokumente, Webseiten, E-Mails oder Datenquellen—die von KI-Systemen anschließend als legitime Befehle verarbeitet werden.

**Angriffsszenarien:**
- **Dokumentenbasierte Injection**: Bösartige Anweisungen versteckt in verarbeiteten Dokumenten, die unerwünschte KI-Aktionen auslösen
- **Ausnutzung von Web-Inhalten**: Kompromittierte Webseiten mit eingebetteten Prompts, die das KI-Verhalten beim Scrapen manipulieren
- **E-Mail-basierte Angriffe**: Bösartige Prompts in E-Mails, die KI-Assistenten dazu bringen, Informationen preiszugeben oder unautorisierte Aktionen durchzuführen
- **Kontaminierung von Datenquellen**: Kompromittierte Datenbanken oder APIs liefern verseuchte Inhalte an KI-Systeme

**Reale Auswirkungen**: Diese Angriffe können zu Datenabfluss, Datenschutzverletzungen, Erzeugung schädlicher Inhalte und Manipulation von Benutzerinteraktionen führen. Eine detaillierte Analyse finden Sie unter [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/de/prompt-injection.ed9fbfde297ca877.webp)

#### **Tool Poisoning-Angriffe**

**Tool Poisoning** zielt auf die Metadaten ab, die MCP-Tools definieren, und nutzt aus, wie große Sprachmodelle Tool-Beschreibungen und Parameter interpretieren, um Ausführungsentscheidungen zu treffen.

**Angriffsmechanismen:**
- **Manipulation von Metadaten**: Angreifer injizieren schädliche Anweisungen in Tool-Beschreibungen, Parameterdefinitionen oder Anwendungsbeispiele
- **Unsichtbare Anweisungen**: Versteckte Prompts in Tool-Metadaten, die von KI-Modellen verarbeitet werden, aber für Menschen unsichtbar bleiben
- **Dynamische Tool-Änderungen („Rug Pulls“) **: Werkzeuge, die von Nutzern genehmigt wurden, werden später modifiziert, um ohne Wissen der Nutzer schädliche Aktionen auszuführen
- **Parameter-Injektion**: Bösartiger Inhalt in Tool-Parameterschemata, der das Modellverhalten beeinflusst
**Risiken gehosteter Server**: Remote-MCP-Server bergen erhöhte Risiken, da Tool-Definitionen nach der anfänglichen Benutzerfreigabe aktualisiert werden können, was Szenarien schafft, in denen zuvor sichere Tools bösartig werden. Für eine umfassende Analyse siehe [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/de/tool-injection.3b0b4a6b24de6bef.webp)

#### **Zusätzliche AI-Angriffsvektoren**

- **Cross-Domain Prompt Injection (XPIA)**: Hochentwickelte Angriffe, die Inhalte aus mehreren Domänen nutzen, um Sicherheitskontrollen zu umgehen
- **Dynamische Fähigkeitsänderung**: Echtzeitänderungen an Tool-Fähigkeiten, die anfängliche Sicherheitsbewertungen umgehen
- **Context Window Poisoning**: Angriffe, die große Kontextfenster manipulieren, um bösartige Anweisungen zu verbergen
- **Model Confusion Attacks**: Ausnutzung von Modellbeschränkungen zur Erzeugung unvorhersehbarer oder unsicherer Verhaltensweisen


### Auswirkungen der AI-Sicherheitsrisiken

**Folgen mit hoher Auswirkung:**
- **Datenexfiltration**: Unbefugter Zugriff und Diebstahl sensibler Unternehmens- oder persönlicher Daten
- **Verletzungen der Privatsphäre**: Offenlegung personenbezogener Daten (PII) und vertraulicher Geschäftsdaten  
- **Systemmanipulation**: Unbeabsichtigte Änderungen an kritischen Systemen und Arbeitsabläufen
- **Diebstahl von Zugangsdaten**: Kompromittierung von Authentifizierungstokens und Dienstanmeldedaten
- **Laterale Bewegung**: Nutzung kompromittierter AI-Systeme als Sprungbrett für weiterreichende Netzwerkangriffe

### Microsoft AI-Sicherheitslösungen

#### **AI Prompt Shields: Fortschrittlicher Schutz gegen Injection-Angriffe**

Microsoft **AI Prompt Shields** bieten umfassenden Schutz gegen direkte und indirekte Prompt Injection-Angriffe durch mehrere Sicherheitsebenen:

##### **Kernschutzmechanismen:**

1. **Fortgeschrittene Erkennung & Filterung**
   - Machine-Learning-Algorithmen und NLP-Techniken erkennen bösartige Anweisungen in externen Inhalten
   - Echtzeitanalyse von Dokumenten, Webseiten, E-Mails und Datenquellen auf eingebettete Bedrohungen
   - Kontextuelles Verständnis legitimer vs. bösartiger Prompt-Muster

2. **Spotlighting-Techniken**  
   - Unterscheidet vertrauenswürdige Systemanweisungen von potenziell kompromittierten externen Eingaben
   - Texttransformationen, die die Relevanz für das Modell erhöhen und bösartige Inhalte isolieren
   - Unterstützt AI-Systeme dabei, die korrekte Anweisungshierarchie einzuhalten und eingebettete Befehle zu ignorieren

3. **Trennzeichen- & Datenmarkierungssysteme**
   - Explizite Abgrenzung zwischen vertrauenswürdigen Systemnachrichten und externem Eingabetext
   - Spezielle Marker markieren Grenzen zwischen vertrauenswürdigen und nicht vertrauenswürdigen Datenquellen
   - Klare Trennung verhindert Anweisungsverwirrung und unbefugte Befehlsausführung

4. **Kontinuierliche Bedrohungsintelligenz**
   - Microsoft überwacht kontinuierlich neue Angriffsmuster und aktualisiert die Schutzmechanismen
   - Proaktives Threat Hunting nach neuen Injection-Techniken und Angriffsvektoren
   - Regelmäßige Aktualisierungen der Sicherheitsmodelle zur Aufrechterhaltung der Wirksamkeit gegen sich entwickelnde Bedrohungen

5. **Integration von Azure Content Safety**
   - Teil der umfassenden Azure AI Content Safety Suite
   - Zusätzliche Erkennung von Jailbreak-Versuchen, schädlichen Inhalten und Sicherheitsrichtlinienverletzungen
   - Einheitliche Sicherheitskontrollen über AI-Anwendungskomponenten hinweg

**Implementierungsressourcen**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/de/prompt-shield.ff5b95be76e9c78c.webp)


## Erweiterte MCP-Sicherheitsbedrohungen

### Schwachstellen durch Session Hijacking

**Session Hijacking** stellt einen kritischen Angriffsvektor in zustandsbehafteten MCP-Implementierungen dar, bei dem unbefugte Parteien legitime Sitzungs-IDs erlangen und missbrauchen, um sich als Clients auszugeben und unbefugte Aktionen auszuführen.

#### **Angriffsszenarien & Risiken**

- **Session Hijack Prompt Injection**: Angreifer mit gestohlenen Sitzungs-IDs injizieren bösartige Ereignisse in Server, die den Sitzungszustand teilen, was potenziell schädliche Aktionen auslöst oder Zugriff auf sensible Daten erlaubt
- **Direkte Nachahmung**: Gestohlene Sitzungs-IDs ermöglichen direkte MCP-Serveraufrufe, die die Authentifizierung umgehen und Angreifer als legitime Benutzer behandeln
- **Kompromittierte Resume-Streams**: Angreifer können Anfragen vorzeitig beenden, wodurch legitime Clients mit potenziell bösartigen Inhalten fortsetzen

#### **Sicherheitskontrollen für Session-Management**

**Kritische Anforderungen:**
- **Autorisierungsprüfung**: MCP-Server, die Autorisierung implementieren, **MÜSSEN** ALLE eingehenden Anfragen prüfen und **DÜRFEN NICHT** für die Authentifizierung auf Sessions vertrauen
- **Sichere Session-Erstellung**: Verwendung kryptographisch sicherer, nicht-deterministischer Sitzungs-IDs, die mit sicheren Zufallszahlengeneratoren erzeugt werden
- **Benutzerspezifische Bindung**: Bindung von Sitzungs-IDs an benutzerspezifische Informationen mittels Formaten wie `<user_id>:<session_id>`, um eine missbräuchliche Nutzung zwischen Benutzern zu verhindern
- **Sitzungslebenszyklusverwaltung**: Implementierung von Ablauf, Rotation und Ungültigmachung, um Angriffsfenster zu beschränken
- **Transportsicherheit**: Obligatorisches HTTPS für die gesamte Kommunikation zur Verhinderung von Sitzungs-ID-Abgriff

### Confused Deputy Problem

Das **Confused Deputy Problem** tritt auf, wenn MCP-Server als Authentifizierungs-Proxy zwischen Clients und Drittanbieterdiensten agieren und Möglichkeiten zur Umgehung der Autorisierung durch Ausnutzung statischer Client-IDs schaffen.

#### **Angriffsmechanismen & Risiken**

- **Cookie-basierte Zustimmungsumgehung**: Vorherige Benutzer-Authentifizierung erzeugt Zustimmungs-Cookies, die Angreifer über manipulierte Autorisierungsanfragen mit gestalteten Redirect-URIs ausnutzen
- **Diebstahl von Autorisierungscodes**: Bestehende Zustimmungs-Cookies können dazu führen, dass Autorisierungsserver Zustimmungsschirme überspringen und Codes an angreiferkontrollierte Endpunkte senden  
- **Unbefugter API-Zugang**: Gestohlene Autorisierungscodes ermöglichen Token-Austausch und Benutzer-Imitation ohne explizite Zustimmung

#### **Minderungsstrategien**

**Verpflichtende Kontrollen:**
- **Explizite Zustimmungsanforderungen**: MCP-Proxy-Server mit statischen Client-IDs **MÜSSEN** für jeden dynamisch registrierten Client eine Benutzerzustimmung einholen
- **OAuth 2.1 Sicherheitsimplementierung**: Befolgen der aktuellen OAuth-Sicherheitsbest practices inklusive PKCE (Proof Key for Code Exchange) für alle Autorisierungsanfragen
- **Strenge Client-Validierung**: Umsetzung rigoroser Validierung von Redirect-URIs und Client-IDs zur Verhinderung von Exploits

### Token-Passthrough-Schwachstellen  

**Token Passthrough** stellt ein explizites Anti-Pattern dar, bei dem MCP-Server Client-Token ohne ordnungsgemäße Validierung akzeptieren und an nachgeschaltete APIs weiterleiten, was den MCP-Autorisierungsspezifikationen widerspricht.

#### **Sicherheitsimplikationen**

- **Umgehung von Kontrollen**: Direkte Nutzung von Client-Token bei APIs umgeht wesentliche Ratenbegrenzungen, Validierungen und Überwachungen
- **Korruption des Audit-Trails**: Tokens, die upstream ausgestellt wurden, machen Client-Identifikation unmöglich und verhindern Vorfallsuntersuchungen
- **Proxy-basierte Datenexfiltration**: Unvalidierte Tokens erlauben böswilligen Akteuren, Server als Proxys für unbefugten Datenzugriff zu verwenden
- **Verletzungen von Vertrauensgrenzen**: Downstream-Dienste verlassen sich auf überprüfbare Tokenherkunft, die hier verletzt werden kann
- **Erweiterung von Multi-Service-Angriffen**: Kompromittierte Tokens, die von mehreren Diensten akzeptiert werden, ermöglichen laterale Bewegungen

#### **Erforderliche Sicherheitskontrollen**

**Unverhandelbare Anforderungen:**
- **Token-Validierung**: MCP-Server **DÜRFEN NICHT** Tokens akzeptieren, die nicht explizit für den MCP-Server ausgestellt wurden
- **Audience-Überprüfung**: Immer überprüfen, ob die Audience-Ansprüche des Tokens mit der Identität des MCP-Servers übereinstimmen
- **Ordnungsgemäßer Tokenlebenszyklus**: Implementierung kurzlebiger Zugriffstoken mit sicheren Rotationsverfahren


## Supply Chain-Sicherheit für AI-Systeme

Die Sicherheit der Lieferkette hat sich über traditionelle Softwareabhängigkeiten hinausentwickelt und umfasst das gesamte AI-Ökosystem. Moderne MCP-Implementierungen müssen alle AI-bezogenen Komponenten streng prüfen und überwachen, da jede potenzielle Schwachstellen einführen kann, die die Systemintegrität gefährden.

### Erweiterte Komponenten der AI-Lieferkette

**Traditionelle Softwareabhängigkeiten:**
- Open-Source-Bibliotheken und Frameworks
- Container-Images und Basissysteme  
- Entwicklungstools und Build-Pipelines
- Infrastrukturkomponenten und Dienste

**AI-spezifische Lieferkettenelemente:**
- **Foundation Models**: Vorgefertigte Modelle verschiedener Anbieter, die Herkunftsprüfung erfordern
- **Embedding-Dienste**: Externe Vektorisierungs- und semantische Suchdienste
- **Context-Provider**: Datenquellen, Wissensdatenbanken und Dokumenten-Repositorys  
- **Drittanbieter-APIs**: Externe AI-Dienste, ML-Pipelines und Datenverarbeitungsschnittstellen
- **Modell-Artefakte**: Gewichte, Konfigurationen und feinabgestimmte Modellvarianten
- **Trainingsdatensätze**: Daten, die für Modelltraining und Feinabstimmung verwendet werden

### Umfassende Supply-Chain-Sicherheitsstrategie

#### **Komponentenverifizierung & Vertrauen**
- **Herkunftsprüfung**: Verifizieren von Ursprung, Lizenzierung und Integrität aller AI-Komponenten vor der Integration
- **Sicherheitsbewertung**: Durchführung von Schwachstellenscans und Sicherheitsüberprüfungen für Modelle, Datenquellen und AI-Dienste
- **Reputationsanalyse**: Bewertung der Sicherheitsbilanz und Praktiken von AI-Dienstanbietern
- **Compliance-Prüfung**: Sicherstellen, dass alle Komponenten organisationalen Sicherheits- und Regulierungsanforderungen entsprechen

#### **Sichere Deployment-Pipelines**  
- **Automatisierte CI/CD-Sicherheit**: Integration von Sicherheitsscans durch automatisierte Deployment-Pipelines
- **Artefaktintegrität**: Kryptographische Prüfung aller bereitgestellten Artefakte (Code, Modelle, Konfigurationen)
- **Gestuftes Deployment**: Verwendung progressiver Deployment-Strategien mit Sicherheitsvalidierung in jeder Phase
- **Vertrauenswürdige Artefakt-Repositorys**: Deployment ausschließlich aus verifizierten, sicheren Artefakt-Registries und Repositories

#### **Kontinuierliche Überwachung & Reaktion**
- **Abhängigkeits-Scanning**: Fortlaufende Schwachstellenüberwachung für alle Software- und AI-Komponentenabhängigkeiten
- **Modellüberwachung**: Kontinuierliche Bewertung von Modellverhalten, Leistungstrends und Sicherheitsanomalien
- **Überwachung von Dienstgesundheit**: Beobachtung externer AI-Dienste hinsichtlich Verfügbarkeit, Sicherheitsvorfällen und Richtlinienänderungen
- **Threat-Intelligence-Integration**: Einbindung von Bedrohungsfeeds speziell zu AI- und ML-Sicherheitsrisiken

#### **Zugriffskontrolle & Minimale Berechtigung**
- **Komponentenbezogene Berechtigungen**: Beschränkung des Zugriffs auf Modelle, Daten und Dienste nach betrieblicher Notwendigkeit
- **Service-Account-Management**: Implementierung dedizierter Service-Konten mit minimal erforderlichen Berechtigungen
- **Netzwerksegmentierung**: Isolierung von AI-Komponenten und Einschränkung des Netzwerkanzugriffs zwischen Diensten
- **API-Gateway-Kontrollen**: Nutzung zentralisierter API-Gateways zur Steuerung und Überwachung des Zugriffs auf externe AI-Dienste

#### **Vorfallreaktion & Wiederherstellung**
- **Schnelle Reaktionsverfahren**: Etablierte Prozesse für die Behebung oder den Austausch kompromittierter AI-Komponenten
- **Anmeldeinformationsrotation**: Automatisierte Systeme zur Rotation von Geheimnissen, API-Schlüsseln und Dienstanmeldedaten
- **Rollback-Fähigkeiten**: Möglichkeit zum schnellen Zurücksetzen auf vorherige, bekannte gute Versionen von AI-Komponenten
- **Supply Chain-Hackerholungsverfahren**: Spezielle Prozeduren zur Reaktion auf Kompromittierungen in Upstream-AI-Diensten

### Microsoft-Sicherheitswerkzeuge & Integration

**GitHub Advanced Security** bietet umfassenden Schutz der Lieferkette, einschließlich:
- **Secret Scanning**: Automatisierte Erkennung von Anmeldedaten, API-Schlüsseln und Tokens in Repositories
- **Dependency Scanning**: Schwachstellenbewertung für Open-Source-Abhängigkeiten und Bibliotheken
- **CodeQL-Analyse**: Statische Codeanalyse zur Erkennung von Sicherheitslücken und Programmierfehlern
- **Supply Chain Insights**: Sichtbarkeit hinsichtlich Abhängigkeitsgesundheit und Sicherheitsstatus

**Azure DevOps- & Azure Repos-Integration:**
- Nahtlose Integration von Sicherheitsscans über Microsoft-Entwicklungsplattformen hinweg
- Automatisierte Sicherheitsprüfungen in Azure Pipelines für AI-Arbeitslasten
- Richtliniendurchsetzung für sicheres Deployment von AI-Komponenten

**Microsoft interne Praktiken:**
Microsoft setzt umfangreiche Supply-Chain-Sicherheitspraktiken über alle Produkte hinweg um. Erfahren Sie mehr über bewährte Ansätze in [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Beste Sicherheitspraktiken für Grundlagen

MCP-Implementierungen übernehmen und erweitern die bestehende Sicherheitslage Ihrer Organisation. Die Stärkung der grundlegenden Sicherheitspraktiken verbessert erheblich die Gesamtsicherheit von AI-Systemen und MCP-Einsätzen.

### Grundlegende Sicherheitsprinzipien

#### **Sichere Entwicklungspraktiken**
- **OWASP-Konformität**: Schutz vor [OWASP Top 10](https://owasp.org/www-project-top-ten/) Webanwendungsschwachstellen
- **AI-spezifische Schutzmaßnahmen**: Umsetzung von Kontrollen für [OWASP Top 10 für LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Sicheres Geheimnismanagement**: Verwendung dedizierter Tresore für Tokens, API-Schlüssel und sensible Konfigurationsdaten
- **End-to-End-Verschlüsselung**: Sichere Kommunikation über alle Anwendungskomponenten und Datenflüsse hinweg
- **Eingabevalidierung**: Strenge Validierung aller Benutzereingaben, API-Parameter und Datenquellen

#### **Härtung der Infrastruktur**
- **Multi-Faktor-Authentifizierung**: Obligatorisches MFA für alle administrativen und Dienstkonten
- **Patch-Management**: Automatisierte und zeitnahe Patchversorgung für Betriebssysteme, Frameworks und Abhängigkeiten  
- **Identitätsanbieter-Integration**: Zentrale Identitätsverwaltung über Unternehmens-Identitätsanbieter (Microsoft Entra ID, Active Directory)
- **Netzwerksegmentierung**: Logische Isolierung von MCP-Komponenten zur Begrenzung lateralem Bewegungspotenzials
- **Prinzip der geringsten Rechte**: Minimal erforderliche Berechtigungen für alle Systemkomponenten und Konten

#### **Sicherheitsüberwachung & Erkennung**
- **Umfassende Protokollierung**: Detaillierte Logs von AI-Anwendungsaktivitäten, einschließlich MCP Client-Server-Interaktionen
- **SIEM-Integration**: Zentralisierte Sicherheitsinformations- und Ereignisverwaltung zur Anomalieerkennung
- **Verhaltensanalytik**: KI-gestützte Überwachung zur Erkennung ungewöhnlicher Muster im System- und Nutzerverhalten
- **Bedrohungsintelligenz**: Einbindung externer Bedrohungsfeeds und Kompromittierungsindikatoren (IOCs)
- **Vorfallreaktion**: Definierte Abläufe zur Erkennung, Reaktion und Wiederherstellung von Sicherheitsvorfällen

#### **Zero Trust Architektur**
- **Nie vertrauen, immer verifizieren**: Kontinuierliche Überprüfung von Benutzern, Geräten und Netzwerkverbindungen
- **Mikrosegmentierung**: Granulare Netzwerkkontrollen, die einzelne Arbeitslasten und Dienste isolieren
- **Identitätszentrierte Sicherheit**: Sicherheitsrichtlinien basierend auf überprüften Identitäten statt Netzwerkstandorten
- **Kontinuierliche Risikoabschätzung**: Dynamische Sicherheitsbewertung basierend auf aktuellem Kontext und Verhalten
- **Bedingter Zugriff**: Zugriffskontrollen, die sich basierend auf Risikofaktoren, Standort und Gerätevertrauen anpassen

### Integrationsmuster für Unternehmen

#### **Integration des Microsoft-Sicherheitsökosystems**
- **Microsoft Defender for Cloud**: Umfassendes Cloud-Posture-Management
- **Azure Sentinel**: Cloud-native SIEM- und SOAR-Funktionalitäten zum Schutz von AI-Arbeitslasten
- **Microsoft Entra ID**: Unternehmensweite Identitäts- und Zugriffsverwaltung mit bedingten Zugriffsrichtlinien
- **Azure Key Vault**: Zentrales Geheimnismanagement mit Hardware-Sicherheitsmodul (HSM) Unterstützung
- **Microsoft Purview**: Datenverwaltung und Compliance für AI-Datenquellen und Arbeitsabläufe

#### **Compliance & Governance**
- **Regulatorische Konformität**: Sicherstellung, dass MCP-Implementierungen branchenspezifische Compliance-Anforderungen erfüllen (GDPR, HIPAA, SOC 2)
- **Datenklassifizierung**: Korrekte Kategorisierung und Handhabung sensibler Daten, die von KI-Systemen verarbeitet werden  
- **Audit-Trails**: Umfassende Protokollierung zur Einhaltung von Vorschriften und forensischen Untersuchungen  
- **Datenschutzkontrollen**: Umsetzung von Privacy-by-Design-Prinzipien in der Architektur von KI-Systemen  
- **Change Management**: Formale Prozesse für Sicherheitsprüfungen von Änderungen an KI-Systemen  

Diese grundlegenden Praktiken schaffen eine robuste Sicherheitsgrundlage, die die Effektivität MCP-spezifischer Sicherheitskontrollen erhöht und umfassenden Schutz für KI-gesteuerte Anwendungen bietet.

## Wichtige Sicherheitserkenntnisse

- **Geschichteter Sicherheitsansatz**: Kombination grundlegender Sicherheitspraktiken (sicheres Codieren, Least Privilege, Lieferkettenüberprüfung, kontinuierliche Überwachung) mit KI-spezifischen Kontrollen für umfassenden Schutz

- **KI-spezifische Bedrohungslandschaft**: MCP-Systeme sind einzigartigen Risiken ausgesetzt, darunter Prompt Injection, Tool Poisoning, Session Hijacking, Confused Deputy-Probleme, Token-Passthrough-Schwachstellen und übermäßige Berechtigungen, die spezialisierte Gegenmaßnahmen erfordern

- **Exzellenz bei Authentifizierung & Autorisierung**: Robuste Authentifizierung über externe Identitätsanbieter (Microsoft Entra ID) implementieren, korrekte Tokenvalidierung erzwingen und niemals Tokens akzeptieren, die nicht explizit für Ihren MCP-Server ausgestellt wurden

- **KI-Angriffsprävention**: Einsatz von Microsoft Prompt Shields und Azure Content Safety zur Abwehr von indirekten Prompt Injection- und Tool Poisoning-Angriffen, dabei Metadaten von Tools validieren und dynamische Änderungen überwachen

- **Sitzungs- & Transportsicherheit**: Verwendung kryptografisch sicherer, nicht-deterministischer Sitzungs-IDs, die an Benutzeridentitäten gebunden sind; ordnungsgemäßes Sitzungslebenszyklus-Management implementieren; niemals Sitzungen für Authentifizierung verwenden

- **OAuth Sicherheitsbest Practices**: Vermeidung von Confused Deputy-Angriffen durch explizite Benutzerzustimmung für dynamisch registrierte Clients, korrekte OAuth 2.1-Implementierung mit PKCE und strikte Validierung von Redirect-URIs

- **Token-Sicherheitsprinzipien**: Vermeidung von Token-Passthrough-Anti-Patterns, Validierung von Token-Audience-Claims, Implementierung kurzlebiger Tokens mit sicherer Rotation und klare Vertrauensgrenzen pflegen

- **Umfassende Lieferkettensicherheit**: Alle Komponenten des KI-Ökosystems (Modelle, Embeddings, Kontextanbieter, externe APIs) mit derselben Sicherheitsexzellenz wie traditionelle Software-Abhängigkeiten behandeln

- **Kontinuierliche Weiterentwicklung**: Auf dem neuesten Stand der sich schnell entwickelnden MCP-Spezifikationen bleiben, zur Sicherheitscommunity beitragen und adaptive Sicherheitsstrategien während der Protokollreife pflegen

- **Integration in Microsoft Sicherheit**: Das umfassende Sicherheitssystem von Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) für verbesserten Schutz bei der MCP-Bereitstellung nutzen

## Umfassende Ressourcen

### **Offizielle MCP Sicherheitsdokumentation**  
- [MCP Spezifikation (Aktuell: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP Sicherheits-Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP Autorisierungsspezifikation](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)  

### **OWASP MCP Sicherheitsressourcen**  
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) – Umfassende OWASP MCP Top 10 mit Implementierungsleitfaden für Azure  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) – Offizielle OWASP MCP Sicherheitsrisiken  
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) – Praktische Sicherheitsschulung für MCP auf Azure  

### **Sicherheitsstandards & Best Practices**  
- [OAuth 2.0 Sicherheits-Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 Web-Anwendungssicherheit](https://owasp.org/www-project-top-ten/)  
- [OWASP Top 10 für Large Language Models](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Microsoft Digital Defense Report](https://aka.ms/mddr)  

### **KI-Sicherheitsforschung & Analyse**  
- [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Tool Poisoning Angriffe (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)  
- [MCP Security Research Briefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)  

### **Microsoft Sicherheitslösungen**  
- [Microsoft Prompt Shields Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [Microsoft Entra ID Sicherheit](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)  
- [Azure Token-Management Best Practices](https://learn.microsoft.com/entra/identity-platform/access-tokens)  
- [GitHub Advanced Security](https://github.com/security/advanced-security)  

### **Implementierungsleitfäden & Tutorials**  
- [Azure API Management als MCP Authentifizierungsgateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)  
- [Microsoft Entra ID Authentifizierung mit MCP-Servern](https://den.dev/blog/mcp-server-auth-entra-id-session/)  
- [Sichere Token-Speicherung und Verschlüsselung (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)  

### **DevOps & Lieferkettensicherheit**  
- [Azure DevOps Sicherheit](https://azure.microsoft.com/products/devops)  
- [Azure Repos Sicherheit](https://azure.microsoft.com/products/devops/repos/)  
- [Microsoft Supply Chain Security Journey](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)  

## **Zusätzliche Sicherheitsdokumentation**

Für umfassende Sicherheitsanleitungen, siehe diese spezialisierten Dokumente in diesem Abschnitt:

- **[MCP Sicherheits-Best Practices 2025](./mcp-security-best-practices-2025.md)** – Vollständige Sicherheits-Best Practices für MCP-Implementierungen  
- **[Azure Content Safety Implementierung](./azure-content-safety-implementation.md)** – Praktische Implementierungsbeispiele für Azure Content Safety Integration  
- **[MCP Sicherheitskontrollen 2025](./mcp-security-controls-2025.md)** – Neueste Sicherheitskontrollen und Techniken für MCP-Bereitstellungen  
- **[MCP Best Practices Kurzübersicht](./mcp-best-practices.md)** – Schnelle Referenz für wesentliche MCP-Sicherheitspraktiken  
- **[BlueHat 2026: Sicherung der Zukunft der KI: MCP-Sicherung mit Defense-in-Depth-Patterns](https://www.youtube.com/watch?v=cVWB58kEt-Y)** – Defense-in-Depth-Pattern vom Microsoft Security Response Center (MSRC)  

### **Praktische Sicherheitsschulung**

- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** – Umfassender praktischer Workshop zur Absicherung von MCP-Servern in Azure mit progressiven Trainingslagern vom Base Camp bis zum Summit  
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** – Referenzarchitektur und Implementierungshilfe für alle OWASP MCP Top 10 Risiken  

---

## Was als Nächstes kommt

Weiter: [Kapitel 3: Erste Schritte](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->