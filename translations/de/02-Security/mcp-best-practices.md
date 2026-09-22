# MCP Sicherheits-Best-Practices – Update September 2026

Dieser umfassende Leitfaden beschreibt wesentliche Sicherheits-Best-Practices für
die Implementierung von Model Context Protocol (MCP)-Systemen basierend auf
**MCP Spezifikation 2026-07-28** und aktuellen Industriestandards. Diese
Praktiken adressieren sowohl traditionelle Sicherheitsbedenken als auch KI-spezifische Bedrohungen,
die bei MCP-Einsätzen einzigartig sind.

## Kritische Sicherheitsanforderungen

### Obligatorische Sicherheitskontrollen (MUSS-Anforderungen)

1. **Token-Validierung**: MCP-Server **DÜRFEN KEINE** Tokens akzeptieren, die nicht explizit für den MCP-Server selbst ausgestellt wurden
2. **Autorisierungsprüfung**: MCP-Server, die Autorisierung implementieren, **MÜSSEN** ALLE eingehenden Anfragen verifizieren und **DÜRFEN NICHT** Sitzungen für die Authentifizierung verwenden  
3. **Nutzereinwilligung**: MCP-Proxy-Server, die statische Drittanbieter-Client-IDs verwenden, **MÜSSEN** vor Weiterleitung eines Autorisierungsflusses eine ausdrückliche Zustimmung für jeden MCP-Client einholen
4. **Sicherheit des State Handles**: MCP-Server **DÜRFEN** den Besitz eines
	Anwendungs-State Handles nicht als Authentifizierung betrachten und **MÜSSEN** jede
	Anfrage, die eines verwendet, autorisieren

## Kern-Sicherheitspraktiken

### 1. Eingabevalidierung & -bereinigung
- **Umfassende Eingabevalidierung**: Validieren und bereinigen Sie alle Eingaben, um Injektionsangriffe, verwirrte Stellvertreter-Probleme und Prompt Injection-Schwachstellen zu verhindern
- **Parameter-Schema-Durchsetzung**: Implementieren Sie eine strenge JSON-Schema-Validierung für alle Werkzeugparameter und API-Eingaben
- **Inhaltsfilterung**: Verwenden Sie Microsoft Prompt Shields und Azure Content Safety, um bösartigen Inhalt in Eingabeaufforderungen und Antworten zu filtern
- **Ausgabe-Bereinigung**: Validieren und bereinigen Sie alle Modellausgaben, bevor Sie sie Benutzern oder nachgelagerten Systemen präsentieren

### 2. Exzellente Authentifizierung & Autorisierung  
- **Externe Identitätsanbieter**: Delegieren Sie die Authentifizierung an etablierte Identitätsanbieter (Microsoft Entra ID, OAuth 2.1-Anbieter) anstatt eigene Authentifizierungen zu implementieren
- **Client-Registrierung**: Bevorzugen Sie Client-ID-Metadaten-Dokumente oder Vorregistrierung; verwenden Sie die veraltete dynamische Client-Registrierung nur zur Kompatibilität
- **Feingranulare Berechtigungen**: Implementieren Sie granulare, werkzeugspezifische Berechtigungen nach dem Prinzip der geringsten Privilegien
- **Token-Lebenszyklus-Management**: Verwenden Sie kurzlebige Zugriffstoken mit sicherer Rotation und ordnungsgemäßer Audience-Validierung
- **Multi-Faktor-Authentifizierung**: Erfordern Sie MFA für alle administrativen Zugriffe und sensible Operationen

### 3. Sichere Kommunikationsprotokolle
- **Transport Layer Security**: Verwenden Sie HTTPS mit ordnungsgemäßer Zertifikatsvalidierung
 für entfernte HTTP-MCP-Kommunikation; verwenden Sie Prozessisolation und Umgebungs-
 anmeldeinformationen für lokale stdio-Server
- **Ende-zu-Ende-Verschlüsselung**: Implementieren Sie zusätzliche Verschlüsselungsebenen für hochsensible Daten während der Übertragung und im Ruhezustand
- **Zertifikatsverwaltung**: Pflegen Sie einen ordnungsgemäßen Zertifikats-Lebenszyklus mit automatisierten Erneuerungsprozessen
- **Protokollversions-Durchsetzung**: Verwenden Sie MCP `2026-07-28`, fügen Sie die erforderlichen
	Versionsmetadaten bei jeder Anfrage hinzu und lehnen Sie nicht unterstützte Versionen ab

### 4. Fortschrittliche Ratenbegrenzung & Ressourcenschutz
- **Mehrschichtige Ratenbegrenzung**: Implementieren Sie Ratenbegrenzung nach Benutzer, Anmeldeinformationen,
  Vorgang, Werkzeug und Ressource, um Missbrauch zu verhindern
- **Adaptive Ratenbegrenzung**: Verwenden Sie maschinelles Lernen-basierte Ratenbegrenzung, die sich an Nutzungsmuster und Bedrohungsindikatoren anpasst
- **Ressourcenquotenverwaltung**: Setzen Sie angemessene Grenzen für Rechenressourcen, Speichernutzung und Ausführungszeit
- **DDoS-Schutz**: Setzen Sie umfassenden DDoS-Schutz und Verkehrsanalysesysteme ein

### 5. Umfassende Protokollierung & Überwachung
- **Strukturierte Audit-Protokollierung**: Implementieren Sie detaillierte, durchsuchbare Protokolle für alle MCP-Operationen, Werkzeugausführungen und Sicherheitsereignisse
- **Echtzeit-Sicherheitsüberwachung**: Setzen Sie SIEM-Systeme mit KI-gestützter Anomalieerkennung für MCP-Workloads ein
- **Datenschutzkonforme Protokollierung**: Protokollieren Sie Sicherheitsereignisse unter Einhaltung von Datenschutzanforderungen und -vorschriften
- **Integration der Vorfallreaktion**: Verbinden Sie Protokollierungssysteme mit automatisierten Vorfallreaktionsabläufen

### 6. Verbesserte sichere Speicherpraktiken
- **Hardware-Sicherheitsmodule**: Verwenden Sie HSM-gestützte Schlüsselspeicherung (Azure Key Vault, AWS CloudHSM) für kritische kryptografische Operationen
- **Verwaltung von Verschlüsselungsschlüsseln**: Implementieren Sie ordnungsgemäße Schlüsselrotation, Trennung und Zugriffskontrollen für Verschlüsselungsschlüssel
- **Geheimnisverwaltung**: Speichern Sie alle API-Schlüssel, Tokens und Zugangsdaten in dedizierten Geheimnis-Management-Systemen
- **Datenklassifizierung**: Klassifizieren Sie Daten basierend auf Sensitivitätsstufen und wenden Sie angemessene Schutzmaßnahmen an

### 7. Fortschrittliches Token-Management
- **Verhinderung von Token-Passthrough**: Verbieten Sie ausdrücklich Token-Passthrough-Muster, die Sicherheitskontrollen umgehen
- **Audience-Validierung**: Verifizieren Sie stets, dass die Audience-Ansprüche des Tokens mit der beabsichtigten MCP-Server-Identität übereinstimmen
- **Claims-basierte Autorisierung**: Implementieren Sie feingranulare Autorisierung basierend auf Token-Ansprüchen und Benutzerattributen
- **Token-Bindung**: Validieren Sie, dass Tokens auf die beabsichtigte MCP-Ressource abzielen und
 binden Sie Anwendungs-State Handles serverseitig an die authentifizierte Principal

### 8. Sicherer Anwendungsstatus

- **Kryptographische State Handles**: Erzeugen Sie undurchsichtige, nicht-deterministische Handles
 für Zustände, die Anfragen überdauern
- **Benutzerspezifische Bindung**: Binden Sie jedes Handle serverseitig an die authentifizierte
 Principal; vertrauen Sie nicht auf vom Client bereitgestellte Benutzer-IDs
- **Lebenszykluskontrollen**: Lassen Sie Handles verfallen und widerrufen Sie sie, und definieren Sie, wie Anrufer
 vom veralteten Zustand wiederherstellen können
- **Autorisierung pro Anfrage**: Überprüfen Sie die Autorisierung immer dann neu, wenn ein Handle
 präsentiert wird; ein Handle ist ein Name, kein Nachweis

### 9. KI-spezifische Sicherheitskontrollen
- **Prompt Injection-Abwehr**: Setzen Sie Microsoft Prompt Shields mit Spotlighting, Delimiter- und Datenmarkierungstechniken ein
- **Vermeidung von Werkzeugvergiftung**: Validieren Sie Werkzeug-Metadaten, überwachen Sie dynamische Änderungen und überprüfen Sie die Werkzeugintegrität
- **Validierung der Modellausgaben**: Scannen Sie Modellausgaben auf potentielle Datenlecks, schädliche Inhalte oder Verstöße gegen Sicherheitsrichtlinien
- **Schutz des Kontextfensters**: Implementieren Sie Kontrollen, um Kontextfenster-Vergiftung und Manipulationsangriffe zu verhindern

### 10. Sicherheit bei der Ausführung von Werkzeugen
- **Ausführungs-Sandboxing**: Führen Sie Werkzeuge in containerisierten, isolierten Umgebungen mit Ressourcenbeschränkungen aus
- **Rechte-Trennung**: Führen Sie Werkzeuge mit minimal erforderlichen Privilegien und separaten Dienstkonten aus
- **Netzwerk-Isolierung**: Implementieren Sie Netzsegmentierung für Werkzeug-Ausführungsumgebungen
- **Überwachung der Ausführung**: Überwachen Sie die Werkzeugausführung auf anomales Verhalten, Ressourcennutzung und Sicherheitsverletzungen

### 11. Kontinuierliche Sicherheitsvalidierung
- **Automatisierte Sicherheitstests**: Integrieren Sie Sicherheitstests in CI/CD-Pipelines mit Werkzeugen wie GitHub Advanced Security
- **Verwaltung von Schwachstellen**: Scannen Sie regelmäßig alle Abhängigkeiten, einschließlich KI-Modelle und externe Dienste
- **Penetrationstests**: Führen Sie regelmäßige Sicherheitsbewertungen speziell für MCP-Implementierungen durch
- **Sicherheits-Code-Reviews**: Implementieren Sie obligatorische Sicherheitsprüfungen für alle MCP-bezogenen Codeänderungen

### 12. Lieferkettensicherheit für KI
- **Komponentenverifikation**: Verifizieren Sie Herkunft, Integrität und Sicherheit aller KI-Komponenten (Modelle, Einbettungen, APIs)
- **Abhängigkeitsmanagement**: Pflegen Sie aktuelle Inventare aller Software- und KI-Abhängigkeiten mit Schwachstellenverfolgung
- **Vertrauenswürdige Repositorien**: Verwenden Sie verifizierte, vertrauenswürdige Quellen für alle KI-Modelle, Bibliotheken und Werkzeuge
- **Überwachung der Lieferkette**: Überwachen Sie kontinuierlich Kompromittierungen bei KI-Dienstanbietern und Modell-Repositorien

## Erweiterte Sicherheitsmuster

### Zero-Trust-Architektur für MCP
- **Niemals vertrauen, immer verifizieren**: Implementieren Sie kontinuierliche Verifizierung für alle MCP-Teilnehmer
- **Mikrosegmentierung**: Isolieren Sie MCP-Komponenten mit granularem Netzwerk- und Identitätskontrollen
- **Bedingter Zugriff**: Implementieren Sie risikobasierte Zugriffskontrollen, die sich an Kontext und Verhalten anpassen
- **Kontinuierliche Risikobewertung**: Bewerten Sie dynamisch die Sicherheitslage basierend auf aktuellen Bedrohungsindikatoren

### Datenschutz-freundliche KI-Implementierung
- **Datenminimierung**: Geben Sie nur die minimal erforderlichen Daten für jede MCP-Operation frei
- **Differential Privacy**: Implementieren Sie datenschutzfreundliche Techniken für die Verarbeitung sensibler Daten
- **Homomorphe Verschlüsselung**: Verwenden Sie fortgeschrittene Verschlüsselungsmethoden für sichere Berechnungen auf verschlüsselten Daten
- **Föderiertes Lernen**: Implementieren Sie verteilte Lernansätze, die Datenlokalität und Datenschutz bewahren

### Vorfallmanagement für KI-Systeme
- **KI-spezifische Vorfallverfahren**: Entwickeln Sie Vorfallreaktionsverfahren, die speziell auf KI- und MCP-spezifische Bedrohungen zugeschnitten sind
- **Automatisierte Reaktion**: Implementieren Sie automatisierte Eindämmung und Behebung für häufige KI-Sicherheitsvorfälle  
- **Forensische Fähigkeiten**: Halten Sie forensische Bereitschaft für KI-Systemkompromittierungen und Datenpannen bereit
- **Wiederherstellungsverfahren**: Etablieren Sie Verfahren zur Wiederherstellung von KI-Modellvergiftung, Prompt Injection-Angriffen und Dienstkompromittierungen

## Implementierungsressourcen & Standards

### 🏔️ Praktische Sicherheitsschulungen
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** – Umfassender praktischer Workshop zur Absicherung von MCP-Servern in Azure
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** – Referenzarchitektur und OWASP MCP Top 10 Implementierungsanleitungen

### Offizielle MCP-Dokumentation
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) – Aktuelle MCP-Protokollspezifikation
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) – Offizielle Sicherheitsempfehlungen
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) – HTTP-Autorisierungsmuster
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) – Transportanforderungen

### Microsoft Sicherheitslösungen
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) – Fortschrittlicher Schutz vor Prompt Injection
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) – Umfassende KI-Inhaltsfilterung
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) – Unternehmensweite Identitäts- und Zugriffsverwaltung
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) – Sichere Geheimnis- und Zugangsdatenverwaltung
- [GitHub Advanced Security](https://github.com/security/advanced-security) – Scannen von Lieferketten und Codesicherheit

### Sicherheitsstandards & Frameworks
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) – Aktuelle OAuth Sicherheitsrichtlinien
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) – Sicherheitsrisiken bei Webanwendungen
- [OWASP Top 10 für LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) – KI-spezifische Sicherheitsrisiken
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) – Umfassendes KI-Risikomanagement
- [ISO 27001:2022](https://www.iso.org/standard/27001) – Managementsysteme für Informationssicherheit

### Implementierungsleitfäden & Tutorials
- [Azure API Management als MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) – Enterprise-Authentifizierungsmuster
- [Microsoft Entra ID mit MCP-Servern](https://den.dev/blog/mcp-server-auth-entra-id-session/) – Integration von Identitätsanbietern
- [Implementierung sicherer Token-Speicherung](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) – Best Practices im Token-Management
- [Ende-zu-Ende-Verschlüsselung für KI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) – Fortgeschrittene Verschlüsselungsmuster

### Erweiterte Sicherheitsressourcen
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) – Sichere Entwicklungspraktiken
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) – KI-spezifische Sicherheitstests
- [Threat Modeling für KI-Systeme](https://learn.microsoft.com/security/adoption/approach/threats-ai) – Methodik zur Bedrohungsmodellierung für KI
- [Privacy Engineering für KI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) – Datenschutzschützende KI-Techniken

### Compliance & Governance
- [DSGVO-Compliance für KI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) – Datenschutzkonformität in KI-Systemen
- [KI-Governance-Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) – Verantwortungsbewusste KI-Implementierung
- [SOC 2 für KI-Dienste](https://learn.microsoft.com/compliance/regulatory/offering-soc) – Sicherheitskontrollen für KI-Dienstanbieter
- [HIPAA-Compliance für KI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) – Anforderungen zur Einhaltung im Gesundheitswesen für KI

### DevSecOps & Automatisierung
- [DevSecOps-Pipeline für KI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) – Sichere KI-Entwicklungspipelines
- [Automatisierte Sicherheitstests](https://learn.microsoft.com/security/engineering/devsecops) – Kontinuierliche Sicherheitsvalidierung
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) – Sichere Infrastruktur-Bereitstellung
- [Container-Sicherheit für KI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) – Sicherheit für KI-Workload-Containerisierung

### Überwachung & Vorfallmanagement  
- [Azure Monitor für KI-Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) – Umfassende Überwachungslösungen
- [KI-Sicherheitsvorfallreaktion](https://learn.microsoft.com/security/compass/incident-response-playbooks) – KI-spezifische Vorfallverfahren
- [SIEM für KI-Systeme](https://learn.microsoft.com/azure/sentinel/overview) – Sicherheitsinformations- und Ereignismanagement

- [Bedrohungsinformationen für KI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - KI-Bedrohungsinformationsquellen

## 🔄 Kontinuierliche Verbesserung

### Mit den sich entwickelnden Standards Schritt halten
- **MCP-Spezifikationsupdates**: Offizielle Änderungen der MCP-Spezifikation und Sicherheitswarnungen überwachen
- **Bedrohungsinformationen**: Abonnieren Sie KI-Sicherheitsbedrohungsfeeds und Schwachstellendatenbanken  
- **Community-Engagement**: Teilnahme an MCP-Sicherheitsgemeinschaftsdiskussionen und Arbeitsgruppen
- **Regelmäßige Bewertung**: Vierteljährliche Bewertungen der Sicherheitslage durchführen und Praktiken entsprechend aktualisieren

### Beitrag zur MCP-Sicherheit leisten
- **Sicherheitsforschung**: Beitrag zur MCP-Sicherheitsforschung und Schwachstellenoffenlegungsprogrammen leisten
- **Best-Practice-Teilung**: Sicherheitsimplementierungen und Erkenntnisse mit der Community teilen
- **Standardentwicklung**: Teilnahme an der Entwicklung der MCP-Spezifikation und Erstellung von Sicherheitsstandards
- **Werkzeugentwicklung**: Entwicklung und Teilen von Sicherheitswerkzeugen und Bibliotheken für das MCP-Ökosystem

---

*Dieses Dokument spiegelt die besten Sicherheitspraxen von MCP zum 9. September 2026 wider,
basierend auf der MCP-Spezifikation `2026-07-28`. Sicherheitspraxen sollten regelmäßig
überprüft werden, da sich das Protokoll und die Bedrohungslage weiterentwickeln.*

## Was als Nächstes kommt

- Lesen Sie: [MCP Security Best Practices](./mcp-security-best-practices.md)
- Zurück zu: [Security Module Overview](./README.md)
- Weiter zu: [Modul 3: Erste Schritte](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->