# MCP-Sicherheit: Umfassender Schutz für KI-Systeme

[![MCP Security Best Practices](../../../translated_images/de/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

Sicherheit ist grundlegend für das Design von KI-Systemen, weshalb wir sie als unseren zweiten Abschnitt priorisieren. Dies entspricht dem **Secure by Design**-Prinzip von Microsoft aus der [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Das Model Context Protocol (MCP) bringt leistungsstarke neue Fähigkeiten für KI-gesteuerte Anwendungen mit sich und führt gleichzeitig einzigartige Sicherheitsherausforderungen ein, die über traditionelle Softwarerisiken hinausgehen. MCP-Systeme sehen sich sowohl etablierten Sicherheitsbedenken (sichere Programmierung, geringste Berechtigungen, Sicherheit der Lieferkette) als auch neuen, KI-spezifischen Bedrohungen gegenüber, darunter Prompt Injection, Werkzeugvergiftung, Sitzungsübernahme, Confused Deputy-Angriffe, Token-Passthrough-Schwachstellen und dynamische Fähigkeitsänderungen.

Diese Lektion behandelt die kritischsten Sicherheitsrisiken bei MCP-Implementierungen—einschließlich Authentifizierung, Autorisierung, übermäßige Berechtigungen, indirekte Prompt Injection, Sitzungsicherheit, Confused Deputy-Probleme, Token-Verwaltung und Schwachstellen in der Lieferkette. Sie lernen umsetzbare Kontrollen und Best Practices kennen, um diese Risiken zu mindern und dabei Microsoft-Lösungen wie Prompt Shields, Azure Content Safety und GitHub Advanced Security zur Stärkung Ihrer MCP-Bereitstellung zu nutzen.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- **MCP-spezifische Bedrohungen identifizieren**: Einzigartige Sicherheitsrisiken in MCP-Systemen erkennen, einschließlich Prompt Injection, Werkzeugvergiftung, übermäßige Berechtigungen, Sitzungsübernahme, Confused Deputy-Probleme, Token-Passthrough-Schwachstellen und Risiken in der Lieferkette
- **Sicherheitskontrollen anwenden**: Effektive Gegenmaßnahmen umsetzen, darunter robuste Authentifizierung, Zugriff nach dem Prinzip der geringsten Berechtigung, sichere Token-Verwaltung, Sitzungssicherheitskontrollen und Verifikation der Lieferkette
- **Microsoft-Sicherheitslösungen nutzen**: Microsoft Prompt Shields, Azure Content Safety und GitHub Advanced Security zum Schutz von MCP-Workloads verstehen und einsetzen
- **Werkzeugsicherheit validieren**: Die Bedeutung der Validierung von Werkzeugmetadaten erkennen, Überwachung dynamischer Änderungen und Abwehr von indirekten Prompt Injection-Angriffen
- **Best Practices integrieren**: Etablierte Sicherheitsgrundlagen (sichere Programmierung, Server-Härtung, Zero Trust) mit MCP-spezifischen Kontrollen für umfassenden Schutz verbinden

# MCP-Sicherheitsarchitektur & Kontrollen

Moderne MCP-Implementierungen erfordern mehrschichtige Sicherheitsansätze, die sowohl traditionelle Softwaresicherheit als auch KI-spezifische Bedrohungen adressieren. Die sich schnell weiterentwickelnde MCP-Spezifikation verbessert kontinuierlich ihre Sicherheitskontrollen, ermöglicht eine bessere Integration in Unternehmenssicherheitsarchitekturen und etablierte Best Practices.

Untersuchungen im [Microsoft Digital Defense Report](https://aka.ms/mddr) zeigen, dass **98 % der gemeldeten Sicherheitsverletzungen durch robuste Sicherheitsdisziplin verhindert worden wären**. Die effektivste Schutzstrategie kombiniert grundlegende Sicherheitspraktiken mit MCP-spezifischen Kontrollen—bewährte Basissicherheitsmaßnahmen bleiben die wirkungsvollste Methode zur Senkung des allgemeinen Sicherheitsrisikos.

## Aktuelle Sicherheitslage

> **Hinweis:** Dieses Kapitel kombiniert etablierte MCP-Sicherheitskontrollen mit der
> aktuellen **MCP Specification 2026-07-28**-Autorisierungsleitlinie. Beziehen Sie sich stets
> auf die aktuelle [MCP-Spezifikation](https://modelcontextprotocol.io/specification/2026-07-28/),
> das [MCP GitHub-Repository](https://github.com/modelcontextprotocol) sowie die
> [Dokumentation der Sicherheits-Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices),
> wenn Sie sicherheitskritischen Code implementieren.

> **Autorisierungs-Update:** MCP `2026-07-28` verlangt von Clients, den
> `iss`-Parameter bei Autorisierungsantworten (RFC 9207) zu validieren und registrierte
> Anmeldedaten an den ausstellenden Autorisierungsserver zu binden. Die dynamische Client-Registrierung
> ist veraltet; neue Implementierungen sollten Client-ID-Metadokumente verwenden.
> Siehe [Was sich in MCP geändert hat: Die Spezifikation von 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> für die vollständige Liste der Änderungen in der Autorisierung.

## 🏔️ MCP Security Summit Workshop (Sherpa)

Für **praxisbezogenes Sicherheitstraining** empfehlen wir den **MCP Security Summit Workshop** (Sherpa) – eine umfassende geführte Expedition zur Sicherung von MCP-Servern in Microsoft Azure.

### Workshop-Übersicht

Der [MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) bietet praktisches, umsetzbares Sicherheitstraining anhand einer bewährten „verwundbar → ausnutzen → beheben → validieren“-Methodik. Sie werden:

- **Durch Fehler lernen**: Verwundbarkeiten selbst erleben, indem Sie absichtlich unsichere Server angreifen
- **Azure-native Sicherheit nutzen**: Azure Entra ID, Key Vault, API Management und AI Content Safety einsetzen
- **Verteidigung in der Tiefe anwenden**: Fortschritt durch Lager, die umfassende Sicherheitsschichten aufbauen
- **OWASP-Standards befolgen**: Jede Technik entspricht dem [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- **Produktionscode erhalten**: Funktionierende, getestete Implementierungen mitnehmen

### Die Expeditionsroute

| Lager | Fokus | Abgedeckte OWASP Risiken |
|------|-------|-------------------------|
| **Basislager** | MCP-Grundlagen & Authentifizierungsschwachstellen | MCP01, MCP07 |
| **Lager 1: Identität** | OAuth 2.1, Azure Managed Identity, Key Vault | MCP01, MCP02, MCP07 |
| **Lager 2: Gateway** | API Management, Private Endpoints, Governance | MCP02, MCP06, MCP07, MCP09 |
| **Lager 3: I/O-Sicherheit** | Prompt Injection, PII-Schutz, Content Safety | MCP03, MCP05, MCP06, MCP10 |
| **Lager 4: Überwachung** | Log-Analyse, Dashboards, Bedrohungserkennung | MCP04, MCP08 |
| **Der Gipfel** | Red Team / Blue Team-Integrationstest | Alle |

**Starten Sie hier:** [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 Sicherheitsrisiken

Der [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) beschreibt die zehn kritischsten Sicherheitsrisiken für MCP-Implementierungen:

| Risiko | Beschreibung | Azure-Minderung |
|--------|-------------|-----------------|
| **MCP01** | Fehlmanagement von Tokens & Geheimnisoffenlegung | Azure Key Vault, Managed Identity |
| **MCP02** | Privilegieneskalation durch Umfangserweiterung | RBAC, Conditional Access |
| **MCP03** | Werkzeugvergiftung | Werkzeugvalidierung, Integritätsprüfung |
| **MCP04** | Angriffe auf die Software-Lieferkette & Manipulation von Abhängigkeiten | GitHub Advanced Security, Dependency Scanning |
| **MCP05** | Kommandoinjektion & -ausführung | Eingabevalidierung, Sandboxing |
| **MCP06** | Umleitung des Intent-Flusses | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Unzureichende Authentifizierung & Autorisierung | Azure Entra ID, OAuth 2.1 mit PKCE |
| **MCP08** | Mangel an Audit- und Telemetriedaten | Azure Monitor, Application Insights |
| **MCP09** | Schatten-MCP-Server | API-Center-Governance, Netzwerkisolation |
| **MCP10** | Kontextinjektion & Überfreigabe von Daten | Datenklassifizierung, minimale Exposition |

### Entwicklung der MCP-Authentifizierung

Die MCP-Spezifikation hat sich in Bezug auf Authentifizierung und Autorisierung erheblich weiterentwickelt:

- **Ursprünglicher Ansatz**: Frühere Spezifikationen verlangten von Entwicklern, eigene Authentifizierungsserver zu implementieren, wobei MCP-Server als OAuth 2.0-Autorisierungsserver fungierten, die die Benutzer-Authentifizierung direkt verwalten
- **Aktueller Standard (`2026-07-28`)**: MCP-Server können die Authentifizierung
  an externe Identitätsanbieter wie Microsoft Entra ID delegieren. Clients müssen außerdem
  die aktuellen Anforderungen zur Aussteller-Validierung und Anmeldedatenbindung erfüllen.
- **Transportschicht-Sicherheit**: Verbesserte Unterstützung für sichere Übertragungsmechanismen mit geeigneten Authentifizierungsmustern für lokale (STDIO) und entfernte (Streamable HTTP) Verbindungen

## Authentifizierungs- & Autorisierungssicherheit

### Aktuelle Sicherheitsherausforderungen

Moderne MCP-Implementierungen sehen sich verschiedenen Herausforderungen bei Authentifizierung und Autorisierung gegenüber:

### Risiken & Bedrohungsvektoren

- **Fehlkonfigurierte Autorisierungslogik**: Fehlimplementierungen der Autorisierung in MCP-Servern können sensible Daten offenlegen und Zugriffsrechte fehlerhaft anwenden
- **Kompromittierung von OAuth-Tokens**: Der Diebstahl von lokalen MCP-Server-Tokens ermöglicht Angreifern, Server zu imitieren und auf nachgelagerte Dienste zuzugreifen
- **Token-Passthrough-Schwachstellen**: Unsachgemäße Token-Verarbeitung führt zu Umgehungen von Sicherheitskontrollen und mangelnder Verantwortlichkeit
- **Übermäßige Berechtigungen**: Überprivilegierte MCP-Server verletzen das Prinzip der geringsten Berechtigung und vergrößern die Angriffsfläche

#### Token-Passthrough: Ein kritisches Anti-Pattern

**Token-Passthrough ist in der aktuellen MCP-Autorisierungsspezifikation ausdrücklich verboten** aufgrund schwerwiegender Sicherheitsfolgen:

##### Umgehung von Sicherheitskontrollen
- MCP-Server und nachgelagerte APIs implementieren kritische Sicherheitskontrollen (Ratenbegrenzung, Anforderungsvalidierung, Verkehrsüberwachung), die auf ordnungsgemäßer Token-Validierung basieren
- Direkte Token-Verwendung zwischen Client und API umgeht diese essenziellen Schutzmaßnahmen und untergräbt die Sicherheitsarchitektur

##### Herausforderungen bei Verantwortung & Audit  
- MCP-Server können nicht zwischen Clients unterscheiden, die upstream ausgestellte Tokens verwenden, was Audit-Trails unterbricht
- Nachgelagerte Ressourcenserver-Logs zeigen irreführende Ursprünge der Anfragen statt tatsächlicher MCP-Server als Vermittler
- Vorfalluntersuchungen und Compliance-Prüfungen werden erheblich erschwert

##### Risiken der Datenexfiltration
- Nicht validierte Token-Claims ermöglichen es Angreifern mit gestohlenen Tokens, MCP-Server als Proxy für Datenexfiltration zu verwenden
- Verletzungen der Vertrauensgrenzen erlauben unautorisierte Zugriffsmuster, die beabsichtigte Sicherheitskontrollen umgehen

##### Angriffsmuster über mehrere Dienste
- Kompromittierte Tokens, die von mehreren Diensten akzeptiert werden, ermöglichen laterale Bewegungen über verbundene Systeme
- Vertrauensannahmen zwischen Diensten können verletzt werden, wenn die Token-Herkunft nicht verifiziert werden kann

### Sicherheitskontrollen & Gegenmaßnahmen

**Kritische Sicherheitsanforderungen:**

> **VERPFLICHTEND:** MCP-Server **DÜRFEN KEINE** Tokens akzeptieren, die nicht explizit für den MCP-Server ausgestellt wurden

#### Authentifizierungs- & Autorisierungskontrollen

- **Gründliche Überprüfung der Autorisierung**: Umfassende Audits der Autorisierungslogik von MCP-Servern durchführen, um sicherzustellen, dass nur beabsichtigte Benutzer und Clients auf sensible Ressourcen zugreifen können
  - **Implementierungsleitfaden**: [Azure API Management als Authentifizierungsgateway für MCP-Server](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identitätsintegration**: [Microsoft Entra ID zur MCP-Server-Authentifizierung nutzen](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Sichere Token-Verwaltung**: [Microsofts Best Practices zur Token-Validierung und Lebenszyklusmanagement](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens) umsetzen
  - Prüfen, ob Audience-Claims des Tokens mit der MCP-Server-Identität übereinstimmen
  - Richtige Token-Rotation und Ablaufregeln implementieren
  - Token-Replay-Angriffe und unautorisierte Nutzung verhindern

- **Geschützte Token-Speicherung**: Token-Speicherung sicher verschlüsseln, sowohl ruhend als auch bei der Übertragung
  - **Best Practices**: [Sichere Speicherung und Verschlüsselung von Tokens](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Zugriffskontrolle implementieren

- **Prinzip der geringsten Berechtigung**: MCP-Server nur die minimal notwendigen Berechtigungen für die beabsichtigte Funktionalität gewähren
  - Regelmäßige Überprüfung und Anpassungen der Berechtigungen zur Vermeidung von Privilegienausweitung
  - **Microsoft-Dokumentation**: [Sicherer Zugriff mit geringsten Privilegien](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rollbasierte Zugriffskontrolle (RBAC)**: Fein granulare Rollenzuweisungen implementieren
  - Rollen eng auf spezifische Ressourcen und Aktionen beschränken
  - Breite oder unnötige Berechtigungen vermeiden, die Angriffsflächen erweitern

- **Kontinuierliche Berechtigungsüberwachung**: Laufende Überprüfung und Überwachung der Zugriffe einführen
  - Nutzungsmuster von Berechtigungen auf Anomalien überwachen
  - Übermäßige oder ungenutzte Berechtigungen schnell beseitigen

## KI-spezifische Sicherheitsbedrohungen

### Prompt Injection & Angriff auf Werkzeuge

Moderne MCP-Implementierungen sehen sich ausgefeilten, KI-spezifischen Angriffsmustern gegenüber, die traditionelle Sicherheitsmaßnahmen nicht vollständig abdecken können:

#### **Indirekte Prompt Injection (Cross-Domain Prompt Injection)**

**Indirekte Prompt Injection** ist eine der kritischsten Schwachstellen in MCP-fähigen KI-Systemen. Angreifer betten bösartige Anweisungen in externe Inhalte ein – Dokumente, Webseiten, E-Mails oder Datenquellen –, die von KI-Systemen anschließend als legitime Befehle verarbeitet werden.

**Angriffsszenarien:**
- **Dokumentbasierte Injektion**: In verarbeiteten Dokumenten versteckte bösartige Anweisungen, die unerwünschte KI-Aktionen auslösen
- **Ausnutzung von Webinhalten**: Kompromittierte Webseiten mit eingebetteten Prompts, die das Verhalten der KI beim Abrufen manipulieren
- **Angriffe per E-Mail**: Bösartige Prompts in E-Mails, die KI-Assistenten dazu bringen, Informationen preiszugeben oder unautorisierte Aktionen auszuführen
- **Verunreinigung von Datenquellen**: Kompromittierte Datenbanken oder APIs, die belastete Inhalte an KI-Systeme liefern

**Reale Auswirkungen**: Diese Angriffe können zu Datenexfiltration, Datenschutzverletzungen, Erstellung schädlicher Inhalte und Manipulation von Benutzerinteraktionen führen. Eine detaillierte Analyse finden Sie unter [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Diagramm eines Prompt Injection Angriffs](../../../translated_images/de/prompt-injection.ed9fbfde297ca877.webp)

#### **Angriffe durch Werkzeugvergiftung**

**Werkzeugvergiftung** zielt auf die Metadaten, welche die MCP-Werkzeuge definieren, und nutzt aus, wie LLMs Werkzeugbeschreibungen und Parameter interpretieren, um Ausführungsentscheidungen zu treffen.

**Angriffsmechanismen:**
- **Manipulation von Metadaten**: Angreifer injizieren bösartige Anweisungen in Werkzeugbeschreibungen, Parameterdefinitionen oder Anwendungsbeispiele
- **Unsichtbare Instruktionen**: Versteckte Prompts in Werkzeugmetadaten, die von KI-Modellen verarbeitet werden, aber für Benutzer unsichtbar sind
- **Dynamische Werkzeugänderungen („Rug Pulls“) **: Werkzeuge, die von Nutzern freigegeben wurden, werden später ohne deren Wissen zu böswilligen Zwecken modifiziert
- **Parameter-Injektion**: Bösartiger Inhalt, der in Werkzeugparameter-Schemata eingebettet ist und das Modellverhalten beeinflusst


**Risiken bei gehosteten Servern**: Remote MCP-Server bergen erhöhte Risiken, da Tool-Definitionen nach der ersten Benutzerfreigabe aktualisiert werden können, was Szenarien schafft, in denen zuvor sichere Tools bösartig werden. Für eine umfassende Analyse siehe [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagramm](../../../translated_images/de/tool-injection.3b0b4a6b24de6bef.webp)

#### **Zusätzliche Angriffspfade für KI**

- **Cross-Domain Prompt Injection (XPIA)**: Anspruchsvolle Angriffe, die Inhalte aus mehreren Domänen nutzen, um Sicherheitskontrollen zu umgehen
- **Dynamische Fähigkeitsänderung**: Echtzeit-Änderungen an Tool-Fähigkeiten, die anfängliche Sicherheitsbewertungen umgehen
- **Context Window Poisoning**: Angriffe, die große Kontextfenster manipulieren, um bösartige Anweisungen zu verbergen
- **Model Confusion Angriffe**: Ausnutzen von Modellbegrenzungen, um unvorhersehbares oder unsicheres Verhalten zu erzeugen


### Auswirkungen von KI-Sicherheitsrisiken

**Folgen mit hoher Auswirkung:**
- **Datenexfiltration**: Unbefugter Zugriff und Diebstahl sensibler Unternehmens- oder persönlicher Daten
- **Verletzung der Privatsphäre**: Offenlegung persönlich identifizierbarer Informationen (PII) und vertraulicher Geschäftsdaten  
- **Systemmanipulation**: Unbeabsichtigte Änderungen an kritischen Systemen und Arbeitsabläufen
- **Diebstahl von Zugangsdaten**: Kompromittierung von Authentifizierungstokens und Dienstanmeldeinformationen
- **Laterale Bewegung**: Nutzung kompromittierter KI-Systeme als Ausgangspunkt für weiterreichende Netzwerkangriffe

### Microsoft KI-Sicherheitslösungen

#### **AI Prompt Shields: Erweiteter Schutz vor Injection-Angriffen**

Microsoft **AI Prompt Shields** bieten umfassenden Schutz sowohl gegen direkte als auch indirekte Prompt Injection Angriffe durch mehrschichtige Sicherheitsmechanismen:

##### **Kernschutzmechanismen:**

1. **Fortschrittliche Erkennung & Filterung**
   - Maschinelle Lernalgorithmen und NLP-Techniken erkennen bösartige Anweisungen in externen Inhalten
   - Echtzeitanalyse von Dokumenten, Webseiten, E-Mails und Datenquellen auf eingebettete Bedrohungen
   - Kontextuelles Verständnis legitimer vs. bösartiger Prompt-Muster

2. **Hervorhebungstechniken**  
   - Unterscheidet zwischen vertrauenswürdigen Systemanweisungen und potenziell kompromittierten externen Eingaben
   - Texttransformationsmethoden, die die Modellrelevanz erhöhen und gleichzeitig bösartige Inhalte isolieren
   - Hilft KI-Systemen, eine korrekte Anweisungshierarchie aufrechtzuerhalten und injizierte Befehle zu ignorieren

3. **Trennzeichen- & Datenmarkierungssysteme**
   - Explizite Grenzdefinition zwischen vertrauenswürdigen Systemnachrichten und externem Eingabetext
   - Spezielle Markierungen heben Grenzen zwischen vertrauenswürdigen und nicht vertrauenswürdigen Datenquellen hervor
   - Klare Trennung verhindert Verwirrungen bei Anweisungen und unbefugte Befehlsausführungen

4. **Kontinuierliche Bedrohungsinformationen**
   - Microsoft überwacht fortlaufend neue Angriffsmuster und aktualisiert die Abwehrmechanismen
   - Proaktive Bedrohungssuche nach neuen Injection-Techniken und Angriffspfaden
   - Regelmäßige Aktualisierung der Sicherheitsmodelle zur Aufrechterhaltung der Effektivität gegen sich entwickelnde Bedrohungen

5. **Azure Content Safety Integration**
   - Teil der umfassenden Azure AI Content Safety Suite
   - Zusätzliche Erkennung von Jailbreak-Versuchen, schädlichen Inhalten und Sicherheitsverletzungen
   - Vereinheitlichte Sicherheitskontrollen über alle KI-Anwendungskomponenten hinweg

**Implementierungsressourcen**: [Microsoft Prompt Shields Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Schutz](../../../translated_images/de/prompt-shield.ff5b95be76e9c78c.webp)


## Erweitere MCP-Sicherheitsbedrohungen

### Session-Hijacking-Schwachstellen

**Session Hijacking** stellt einen kritischen Angriffsvektor in zustandsbehafteten MCP-Implementierungen dar, bei dem unbefugte Parteien legitime Sitzungskennungen erlangen und missbrauchen, um sich als Clients auszugeben und unerlaubte Aktionen durchzuführen.

#### **Angriffsszenarien & Risiken**

- **Session Hijack Prompt Injection**: Angreifer mit gestohlenen Sitzungs-IDs injizieren bösartige Ereignisse in Server, die Sitzungszustand teilen, wodurch potenziell schädliche Aktionen ausgelöst oder sensible Daten abgerufen werden können
- **Direkte Nachahmung**: Gestohlene Sitzungs-IDs ermöglichen direkte MCP-Server-Aufrufe, die Authentifizierung umgehen und Angreifer als legitime Benutzer behandeln
- **Kompromittierte fortsetzbare Streams**: Angreifer können Anfragen vorzeitig beenden, sodass legitime Clients mit potenziell bösartigem Inhalt fortsetzen

#### **Sicherheitskontrollen für Sitzungsmanagement**

**Kritische Anforderungen:**
- **Autorisierungsüberprüfung**: MCP-Server, die Autorisierung implementieren, **MÜSSEN** ALLE eingehenden Anfragen überprüfen und **DÜRFEN NICHT** auf Sitzungen zur Authentifizierung vertrauen
- **Sichere Sitzungs-ID-Erzeugung**: Verwendung kryptografisch sicherer, nicht-deterministischer Sitzungs-IDs, die mit sicheren Zufallszahlengeneratoren erstellt werden
- **Benutzerspezifische Bindung**: Verknüpfung von Sitzungs-IDs mit benutzerspezifischen Informationen im Format `<user_id>:<session_id>`, um Sitzungsmissbrauch zwischen Benutzern zu verhindern
- **Sitzungslebenszyklus-Management**: Implementierung von korrekter Ablaufzeit, Rotation und Ungültigmachung, um Angriffsfenster zu begrenzen
- **Transportsicherheit**: Obligatorisches HTTPS für alle Kommunikationen zum Schutz vor Abfangen von Sitzungs-IDs

### Confused Deputy Problem

Das **Confused Deputy Problem** tritt auf, wenn MCP-Server als Authentifizierungs-Proxy zwischen Clients und Drittanbieterdiensten fungieren und so Möglichkeiten für Autorisierungsumgehungen durch die Ausnutzung statischer Client-IDs entstehen.

#### **Angriffsmechanik & Risiken**

- **Cookie-basierte Consent-Umgehung**: Vorherige Benutzerauthentifizierung erzeugt Consent-Cookies, die Angreifer durch bösartige Autorisierungsanfragen mit manipulierten Redirect-URIs ausnutzen
- **Diebstahl von Autorisierungscodes**: Vorhandene Consent-Cookies können bewirken, dass Autorisierungsserver Consent-Bildschirme überspringen und Codes an angreiferkontrollierte Endpunkte leiten  
- **Unbefugter API-Zugriff**: Gestohlene Autorisierungscodes ermöglichen Token-Austausch und Benutzer-Imitation ohne explizite Zustimmung

#### **Minderungsstrategien**

**Verpflichtende Kontrollen:**
- **Explizite Zustimmungserfordernisse**: MCP-Proxy-Server mit statischen Client-IDs **MÜSSEN** für jeden dynamisch registrierten Client die Zustimmung des Nutzers einholen
- **OAuth 2.1 Sicherheitsimplementierung**: Befolgen der aktuellen OAuth-Sicherheitspraktiken einschließlich PKCE (Proof Key for Code Exchange) für alle Autorisierungsanfragen
- **Strikte Client-Validierung**: Umfangreiche Validierung von Redirect-URIs und Client-IDs zur Verhinderung von Ausnutzung

### Token Passthrough-Schwachstellen  

**Token Passthrough** stellt ein explizites Anti-Pattern dar, bei dem MCP-Server Client-Tokens ohne ordnungsgemäße Validierung akzeptieren und sie an nachgelagerte APIs weiterleiten, was gegen MCP-Autorisierungsspezifikationen verstößt.

#### **Sicherheitsimplikationen**

- **Umgehung von Kontrollen**: Direkte Nutzung von Client-zu-API-Tokens umgeht wichtige Rate-Limiting-, Validierungs- und Überwachungskontrollen
- **Beschädigung der Prüfpfade**: Tokens, die upstream ausgegeben wurden, machen die Client-Identifikation unmöglich und beeinträchtigen die Untersuchung von Vorfällen
- **Proxy-basierte Datenexfiltration**: Unvalidierte Tokens ermöglichen es Angreifern, Server als Proxy für unberechtigten Datenzugriff zu verwenden
- **Verletzung der Vertrauensgrenzen**: Vertrauenserwartungen downstream-Dienste können verletzt werden, wenn Token-Ursprünge nicht überprüfbar sind
- **Erweiterung von Mehrfachdienst-Angriffen**: Akzeptierte kompromittierte Tokens über mehrere Dienste ermöglichen seitliche Bewegungen

#### **Erforderliche Sicherheitskontrollen**

**Unverhandelbare Anforderungen:**
- **Token-Validierung**: MCP-Server **DÜRFEN NICHT** Tokens akzeptieren, die nicht explizit für den MCP-Server ausgestellt wurden
- **Prüfung der Audience**: Immer sicherstellen, dass Audience-Ansprüche des Tokens mit der Identität des MCP-Servers übereinstimmen
- **Korrektes Token-Lifecycle-Management**: Implementierung kurzlebiger Zugriffstokens mit sicheren Rotationsmechanismen


## Sicherheit der Lieferkette für KI-Systeme

Die Sicherheit der Lieferkette hat sich über traditionelle Softwaresabhängigkeiten hinaus entwickelt und umfasst das gesamte KI-Ökosystem. Moderne MCP-Implementierungen müssen alle KI-bezogenen Komponenten rigoros verifizieren und überwachen, da jede potenzielle Schwachstellen einführen kann, die die Systemintegrität gefährden.

### Erweiterte KI-Lieferkettenkomponenten

**Traditionelle Softwareabhängigkeiten:**
- Open-Source-Bibliotheken und Frameworks
- Container-Images und Basissysteme  
- Entwicklungstools und Build-Pipelines
- Infrastrukturkomponenten und Dienste

**KI-spezifische Lieferkettenelemente:**
- **Foundation Models**: Vorgefertigte Modelle von verschiedenen Anbietern, deren Herkunft geprüft werden muss
- **Embedding-Services**: Externe Vektorisierungs- und semantische Suchdienste
- **Context Providers**: Datenquellen, Wissensdatenbanken und Dokumentenablagen  
- **Drittanbieter-APIs**: Externe KI-Dienste, ML-Pipelines und Datenverarbeitungspunkte
- **Modell-Artefakte**: Gewichte, Konfigurationen und feinabgestimmte Modellvarianten
- **Trainingsdatensätze**: Datensätze, die für Modelltraining und Feinabstimmung verwendet werden

### Umfassende Lieferkettensicherheitsstrategie

#### **Komponentenverifizierung & Vertrauen**
- **Herkunftsvalidierung**: Überprüfen Sie Herkunft, Lizenzierung und Integrität aller KI-Komponenten vor der Integration
- **Sicherheitsbewertung**: Durchführung von Schwachstellenscans und Sicherheitsprüfungen für Modelle, Datenquellen und KI-Dienste
- **Reputationsanalyse**: Bewertung der Sicherheitsbilanz und Praktiken von KI-Dienstanbietern
- **Konformitätsprüfung**: Sicherstellen, dass alle Komponenten die Sicherheits- und regulatorischen Anforderungen der Organisation erfüllen

#### **Sichere Bereitstellungspipelines**  
- **Automatisierte CI/CD-Sicherheit**: Integration von Sicherheitsscans in automatisierte Bereitstellungspipelines
- **Integritätsprüfung von Artefakten**: Kryptografische Verifizierung aller bereitgestellten Artefakte (Code, Modelle, Konfigurationen)
- **Gestufte Bereitstellung**: Einsatz progressiver Bereitstellungsstrategien mit Sicherheitsprüfungen auf jeder Stufe
- **Vertrauenswürdige Artefakt-Repositories**: Bereitstellung nur aus verifizierten, sicheren Artefakt-Registern und -Repositorien

#### **Kontinuierliche Überwachung & Reaktion**
- **Abhängigkeitsprüfung**: Laufende Schwachstellenüberwachung aller Software- und KI-Komponentenabhängigkeiten
- **Modellüberwachung**: Kontinuierliche Bewertung von Modellverhalten, Leistungsverschiebungen und Sicherheitsanomalien
- **Service-Gesundheitsüberwachung**: Überwachung externer KI-Dienste auf Verfügbarkeit, Sicherheitsvorfälle und Richtlinienänderungen
- **Integration von Bedrohungsinformationen**: Einbindung von Bedrohungsfeeds speziell für KI- und ML-Sicherheitsrisiken

#### **Zugriffskontrolle & Mindestprivilegien**
- **Komponentenebene Berechtigungen**: Zugang zu Modellen, Daten und Diensten nur nach geschäftlichem Erfordernis beschränken
- **Verwaltung von Dienstkonten**: Nutzung dedizierter Dienstkonten mit minimal notwendigen Berechtigungen
- **Netzwerksegmentierung**: Isolierung von KI-Komponenten und Einschränkung des Netzwerkzugangs zwischen Diensten
- **API-Gateway-Kontrollen**: Nutzung zentralisierter API-Gateways zur Kontrolle und Überwachung des Zugangs zu externen KI-Diensten

#### **Vorfallreaktion & Wiederherstellung**
- **Schnelle Reaktionsverfahren**: Etablierte Prozesse für das Patchen oder Ersetzen kompromittierter KI-Komponenten
- **Rotation von Anmeldeinformationen**: Automatisierte Systeme zur Rotation von Geheimnissen, API-Schlüsseln und Dienstanmeldedaten
- **Rollback-Fähigkeiten**: Möglichkeit, schnell auf vorherige bekannte gute Versionen von KI-Komponenten zurückzusetzen
- **Wiederherstellung bei Lieferkettenverletzungen**: Spezifische Verfahren zur Reaktion auf Kompromittierungen upstream KI-Dienste

### Microsoft Sicherheitswerkzeuge & Integration

**GitHub Advanced Security** bietet umfassenden Schutz der Lieferkette, einschließlich:
- **Secret Scanning**: Automatisierte Erkennung von Zugangsdaten, API-Schlüsseln und Tokens in Repositories
- **Dependency Scanning**: Schwachstellenbewertung für Open-Source-Abhängigkeiten und Bibliotheken
- **CodeQL-Analyse**: Statische Codeanalyse auf Sicherheitslücken und Codierungsprobleme
- **Supply Chain Insights**: Sichtbarkeit der Abhängigkeitsgesundheit und Sicherheitslage

**Azure DevOps & Azure Repos Integration:**
- Nahtlose Sicherheits-Scan-Integration über Microsoft-Entwicklungsplattformen
- Automatisierte Sicherheitsprüfungen in Azure Pipelines für KI-Workloads
- Richtliniendurchsetzung für sichere Bereitstellung von KI-Komponenten

**Microsoft interne Praktiken:**
Microsoft implementiert umfassende Sicherheit der Lieferkette über alle Produkte hinweg. Erfahren Sie mehr über bewährte Ansätze in [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Beste Sicherheitspraktiken für die Basis

MCP-Implementierungen erben und bauen auf der bestehenden Sicherheitslage Ihrer Organisation auf. Die Stärkung grundlegender Sicherheitspraktiken verbessert die Gesamtsicherheit von KI-Systemen und MCP-Bereitstellungen erheblich.

### Kernfundamente der Sicherheit

#### **Sichere Entwicklungspraktiken**
- **OWASP-Konformität**: Schutz gegen [OWASP Top 10](https://owasp.org/www-project-top-ten/) Webanwendungs-Schwachstellen
- **KI-spezifischer Schutz**: Implementierung von Kontrollen für [OWASP Top 10 für LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Sicheres Geheimnismanagement**: Verwendung dedizierter Tresore für Tokens, API-Schlüssel und sensible Konfigurationsdaten
- **Ende-zu-Ende-Verschlüsselung**: Sichere Kommunikation über alle Anwendungskomponenten und Datenflüsse hinweg implementieren
- **Eingabevalidierung**: Strenge Validierung aller Benutzereingaben, API-Parameter und Datenquellen

#### **Härtung der Infrastruktur**
- **Multi-Faktor-Authentifizierung**: Obligatorische MFA für alle administrativen und Dienstkonten
- **Patch-Management**: Automatisiertes, zeitnahes Patchen von Betriebssystemen, Frameworks und Abhängigkeiten  
- **Integration von Identitätsanbietern**: Zentralisiertes Identitätsmanagement über Unternehmens-Identitätsanbieter (Microsoft Entra ID, Active Directory)
- **Netzwerksegmentierung**: Logische Isolierung von MCP-Komponenten zur Begrenzung lateraler Bewegungsmöglichkeiten
- **Prinzip der minimalen Rechte**: Minimal erforderliche Berechtigungen für alle Systemkomponenten und Konten

#### **Sicherheitsüberwachung & Erkennung**
- **Umfassende Protokollierung**: Detaillierte Aufzeichnung von KI-Anwendungsaktivitäten, einschließlich der Interaktionen zwischen MCP-Client und Server
- **SIEM-Integration**: Zentralisierte Sicherheitsinformationen und Ereignismanagement zur Anomalieerkennung
- **Verhaltensanalyse**: KI-basierte Überwachung zur Erkennung ungewöhnlicher Muster im System- und Benutzerverhalten
- **Bedrohungsinformationen**: Integration externer Bedrohungsdaten und Indikatoren für Kompromittierung (IOCs)
- **Vorfallreaktion**: Gut definierte Verfahren für Erkennung, Reaktion und Wiederherstellung bei Sicherheitsvorfällen

#### **Zero Trust Architektur**
- **Nie vertrauen, immer verifizieren**: Kontinuierliche Verifikation von Benutzern, Geräten und Netzwerkverbindungen
- **Mikrosegmentierung**: Feingranulare Netzwerkkontrollen, die einzelne Workloads und Dienste isolieren
- **Identitätszentrierte Sicherheit**: Sicherheitsrichtlinien basierend auf verifizierten Identitäten statt auf Netzwerkstandorten
- **Kontinuierliche Risikoanalyse**: Dynamische Bewertung der Sicherheitslage basierend auf aktuellem Kontext und Verhalten
- **Bedingter Zugriff**: Zugriffskontrollen, die sich basierend auf Risikofaktoren, Standort und Gerätevertrauen anpassen

### Enterprise-Integrationsmuster

#### **Integration in das Microsoft-Sicherheitsökosystem**
- **Microsoft Defender for Cloud**: Umfassendes Cloud-Sicherheits-Posture-Management
- **Azure Sentinel**: Cloud-native SIEM- und SOAR-Fähigkeiten zum Schutz von KI-Workloads
- **Microsoft Entra ID**: Enterprise Identitäts- und Zugriffsmanagement mit bedingten Zugriffsrichtlinien
- **Azure Key Vault**: Zentralisiertes Geheimnismanagement mit Hardware-Sicherheitsmodul (HSM) Unterstützung
- **Microsoft Purview**: Datenverwaltung und Compliance für KI-Datenquellen und Arbeitsabläufe

#### **Compliance & Governance**
- **Regulatorische Ausrichtung**: Sicherstellen, dass MCP-Implementierungen branchenspezifische Compliance-Anforderungen (GDPR, HIPAA, SOC 2) erfüllen

- **Datenklassifizierung**: Ordungsgemäße Kategorisierung und Handhabung sensibler Daten, die von KI-Systemen verarbeitet werden
- **Audit-Trails**: Umfassende Protokollierung für regulatorische Compliance und forensische Untersuchungen
- **Datenschutzkontrollen**: Implementierung von Privacy-by-Design-Prinzipien in der Architektur von KI-Systemen
- **Change Management**: Formale Prozesse für Sicherheitsüberprüfungen von KI-Systemänderungen

Diese grundlegenden Praktiken schaffen eine robuste Sicherheitsbasis, die die Wirksamkeit MCP-spezifischer Sicherheitskontrollen verbessert und umfassenden Schutz für KI-gesteuerte Anwendungen bietet.

## Wichtige Sicherheits-Schlüsselelemente

- **Geschichteter Sicherheitsansatz**: Kombination grundlegender Sicherheitspraktiken (sicheres Programmieren, geringste Privilegien, Lieferkettenüberprüfung, kontinuierliche Überwachung) mit KI-spezifischen Kontrollen für umfassenden Schutz

- **KI-spezifische Bedrohungslandschaft**: MCP-Systeme sind einzigartigen Risiken ausgesetzt, einschließlich Prompt Injection, Tool Poisoning, Session Hijacking, Confused Deputy-Problemen, Token-Passthrough-Schwachstellen und übermäßigen Berechtigungen, die spezielle Gegenmaßnahmen erfordern

- **Exzellenz bei Authentifizierung & Autorisierung**: Robuste Authentifizierung mit externen Identitätsanbietern (Microsoft Entra ID) implementieren, ordnungsgemäße Token-Validierung durchsetzen und niemals Tokens akzeptieren, die nicht ausdrücklich für Ihren MCP-Server ausgegeben wurden

- **KI-Angriffsprävention**: Einsatz von Microsoft Prompt Shields und Azure Content Safety zum Schutz vor indirekter Prompt Injection und Tool Poisoning-Angriffen, während Tool-Metadaten validiert und dynamische Änderungen überwacht werden

- **Sitzungs- & Transportsicherheit**: Verwendung kryptographisch sicherer, nicht-deterministischer Session-IDs, die an Benutzeridentitäten gebunden sind, ordnungsgemäße Verwaltung des Sitzungslebenszyklus implementieren und Sitzungen niemals zur Authentifizierung verwenden

- **Best Practices für OAuth-Sicherheit**: Schutz vor Confused Deputy-Angriffen durch ausdrückliche Benutzerzustimmung für dynamisch registrierte Clients, ordnungsgemäße OAuth 2.1-Implementierung mit PKCE und strikte Validierung von Redirect-URIs  

- **Token-Sicherheitsprinzipien**: Vermeidung von Token-Passthrough-Anti-Patterns, Validierung von Audience-Claims der Tokens, Implementierung kurzlebiger Tokens mit sicherer Rotation und klare Vertrauensgrenzen einhalten

- **Umfassende Lieferkettensicherheit**: Behandlung aller KI-Ökosystemkomponenten (Modelle, Embeddings, Kontextanbieter, externe APIs) mit der gleichen Sicherheitsstrenge wie traditionelle Softwareabhängigkeiten

- **Kontinuierliche Weiterentwicklung**: Auf dem neuesten Stand der sich schnell entwickelnden MCP-Spezifikationen bleiben, zur Sicherheitsgemeinschaft Standards beitragen und adaptive Sicherheitsstrategien beibehalten, während das Protokoll reift

- **Microsoft Sicherheitsintegration**: Nutzung des umfassenden Sicherheitssystems von Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) zum erweiterten Schutz von MCP-Bereitstellungen

## Umfassende Ressourcen

### **Offizielle MCP-Sicherheitsdokumentation**
- [MCP-Spezifikation (Aktuell: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP-Sicherheits-Best-Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP-Autorisierungsspezifikation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

### **OWASP MCP Sicherheitsressourcen**
- [OWASP MCP Azure Sicherheitsleitfaden](https://microsoft.github.io/mcp-azure-security-guide/) - Umfassende OWASP MCP Top 10 mit Azure-Implementierungsempfehlungen
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Offizielle OWASP MCP Sicherheitsrisiken
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktisches Sicherheitstraining für MCP auf Azure

### **Sicherheitsstandards & Best Practices**
- [OAuth 2.0 Sicherheits-Best-Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Web Application Security](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 für große Sprachmodelle](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Forschung & Analyse zur KI-Sicherheit**
- [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Tool Poisoning Angriffe (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Sicherheitsforschung Briefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Sicherheitslösungen**
- [Microsoft Prompt Shields Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Dienst](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Sicherheit](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management Best Practices](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Implementierungsleitfäden & Tutorials**
- [Azure API Management als MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Authentifizierung mit MCP Servern](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Sichere Token-Speicherung und Verschlüsselung (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & Lieferkettensicherheit**
- [Azure DevOps Sicherheit](https://azure.microsoft.com/products/devops)
- [Azure Repos Sicherheit](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Lieferkettensicherheitsreise](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Weitere Sicherheitsdokumentation**

Für umfassende Sicherheitsanleitungen siehe diese spezialisierten Dokumente in diesem Abschnitt:

- **[CIMD und DCR Autorisierungsbeispiel](./samples/cimd-dcr-auth/README.md)** - Ausführbarer TypeScript MCP `2026-07-28` Ressourcenserver, der bevorzugte Client-ID-Metadatendokumente mit veraltetem Dynamic Client Registration Fallback vergleicht
- **[MCP Sicherheits-Best Practices](./mcp-security-best-practices.md)** - Vollständige Sicherheits-Best-Practices für MCP-Implementierungen
- **[Azure Content Safety Implementierung](./azure-content-safety-implementation.md)** - Praktische Implementierungsbeispiele für Azure Content Safety Integration  
- **[MCP Sicherheitskontrollen](./mcp-security-controls.md)** - Neueste Sicherheitskontrollen und -techniken für MCP-Bereitstellungen
- **[MCP Best Practices Schnellreferenz](./mcp-best-practices.md)** - Schnellreferenz für wesentliche MCP-Sicherheitspraktiken
- **[BlueHat 2026: Sicherung der Zukunft der KI: Absicherung von MCP mit Defense-in-Depth-Patterns](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Defense-in-Depth-Strategien vom Microsoft Security Response Center (MSRC)

### **Praktisches Sicherheitstraining**

- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Umfassender praktischer Workshop zum Absichern von MCP-Servern in Azure mit progressiven Camps von Base Camp bis Summit
- **[OWASP MCP Azure Sicherheitsleitfaden](https://microsoft.github.io/mcp-azure-security-guide/)** - Referenzarchitektur und Implementierungsempfehlungen für alle OWASP MCP Top 10 Risiken

---

## Was kommt als Nächstes

Nächstes: [Kapitel 3: Erste Schritte](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->