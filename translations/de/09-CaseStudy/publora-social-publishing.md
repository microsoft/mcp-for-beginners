# Fallstudie: Veröffentlichen in sozialen Netzwerken von einem Agenten mit einem entfernten MCP-Server

> **Haftungsausschluss:** Mehrere Dienste und Open-Source-Projekte können in soziale Netzwerke veröffentlichen, und ein Team könnte auch die API jedes Netzwerks direkt integrieren. Das untenstehende Szenario wird als ein ausgearbeitetes Beispiel dafür bereitgestellt, wie ein **schreibfähiger entfernter MCP-Server** entworfen und genutzt werden kann. Publora ist ein kommerzieller Dienst mit einem kostenlosen Tarif; die hier beschriebenen Muster gelten für jeden MCP-Server, der irreversible Aktionen im Auftrag eines Benutzers durchführt.

## Übersicht

Agenten sind gut im Entwerfen von Inhalten und schlecht in der Übermittlung. Ein Modell kann in Sekundenschnelle eine Release-Ankündigung schreiben, und dann hört die Arbeit auf: das Veröffentlichen bedeutet eine API pro Netzwerk, eine OAuth-App pro Netzwerk und eine andere Reihe von Medienregeln für jedes. Die meisten Teams lösen dies, indem sie den Text per Hand in einen Browser kopieren.

Diese Fallstudie untersucht, wie dieser letzte Schritt mit einem einzigen entfernten MCP-Server abgeschlossen wird, und — hilfreicher für alle, die einen entwickeln — welche Designentscheidungen ein **schreibfähiger** Server richtig treffen muss. Das Lesen von Daten ist verzeihend. Das Veröffentlichen nicht: ein falscher Werkzeugaufruf ist vor einem Publikum sichtbar und kann nicht rückgängig gemacht werden.

## Szenario

Ein kleines Developer-Relations-Team entwirft Beiträge in einem Agenten (Claude, VS Code, Cursor — der Client ist egal). Sie wollen, dass der Agent:

- sieht, welche Social-Media-Konten das Team verbunden hat,
- einen Beitrag entwirft und als Entwurf für eine menschliche Freigabe speichert,
- ein Bild anhängt,
- ihn für mehrere Netzwerke zu einem gewählten Zeitpunkt plant,
- und später berichtet, wie er sich entwickelt hat.

Wichtig ist, dass der Agent *nicht* versehentlich veröffentlichen darf, während noch experimentiert wird.

## Eingesetzte Werkzeuge

- [Publora MCP Server](https://github.com/publora/mcp-server) — ein entfernter MCP-Server (`streamable-http`), der Veröffentlichungs-, Planungs-, Medien- und LinkedIn-Analysewerkzeuge bereitstellt. Registriert im offiziellen MCP-Register als `com.publora/mcp-server`.

## Schritt-für-Schritt-Arbeitsablauf

1. **Server verbinden.** Clients, die OAuth unterstützen, durchlaufen den Autorisierungscode-Austausch mit PKCE über den eigenen Zustimmungsbildschirm des Servers; Clients, die das nicht tun, wie etwa Headless-CLIs, verwenden einen Publora-API-Schlüssel im Header. Beide Wege werden unterstützt, welcher genutzt wird, hängt vom Client ab, nicht vom Server.
2. **Verbindungen auflisten.** Der Agent ruft `list_connections` auf und erhält die verbundenen Konten mit deren Identifikatoren.
3. **Entwerfen.** Der Agent ruft `create_post` *ohne* eine geplante Zeit auf. Der Beitrag wird als Entwurf gespeichert — nichts wird veröffentlicht.
4. **Medien anhängen.** Öffentliche Bild-URLs werden im selben Aufruf mitgegeben; der Server lädt sie herunter und validiert sie.
5. **Planen.** Nach Freigabe durch einen Menschen setzt `update_post` den Status auf geplant mit einer ISO 8601-Zeit.
6. **Messen.** Für LinkedIn gibt `linkedin_post_stats` Engagement-Daten zurück, sobald der Beitrag live ist.

## Beispiel-Aufforderung

```text
Which social accounts do I have connected?
Draft a post announcing our new changelog page, attach the screenshot at
https://example.com/changelog.png, and keep it as a draft — do not publish it.
Once I approve, schedule it to LinkedIn and Bluesky for tomorrow at 09:00 UTC.
```

## Mermaid-Flussdiagramm

```mermaid
flowchart TD
    A[Benutzeraufforderung in einem MCP-Client] --> B[Client führt OAuth mit dem Server durch]
    B --> C[list_connections]
    C --> D{Zielnetzwerke verbunden?}
    D -- No --> E[Agent meldet, welche fehlen]
    D -- Yes --> F[create_post ohne scheduledTime -> Entwurf]
    F --> G[Mensch überprüft den Entwurf]
    G -- Approved --> H[update_post: status=scheduled]
    G -- Rejected --> I[delete_post]
    H --> J[Server veröffentlicht zur geplanten Zeit]
    J --> K[linkedin_post_stats für Engagement]
```

## Technische Umsetzung

Die folgenden Erkenntnisse sind der übertragbare Teil dieser Fallstudie.

### Offene Entdeckung, authentifizierte Ausführung

`tools/list` wird ohne Anmeldeinformationen bereitgestellt; jeder `tools/call` benötigt einen Token
und gibt sonst `401` mit einem `WWW-Authenticate`-Header zurück, der auf die Metadaten
der geschützten Ressource verweist. Der legacy Endpunkt des Servers antwortet auch auf eine
nicht authentifizierte `initialize`-Anfrage für Clients vor Protokollversion
`2026-07-28`; aktuelle Clients nutzen diesen Handshake nicht.

Diese Serverspezifische Aufteilung erlaubt es Registern, Katalogen und Clients, Werkzeug-
namen, Schemata und Anmerkungen ohne Geheimnisse einzusehen, verhindert jedoch anonyme
Ausführung. Offene Entdeckung ist eine Deployment-Entscheidung, keine MCP-Anforderung; ein
geschütztes Deployment kann auch eine Autorisierung für `tools/list` verlangen.

### Registrierung: dynamische Client-Registrierung und was sie ersetzt

Der Server bietet `/.well-known/oauth-protected-resource` und `/.well-known/oauth-authorization-server` an und unterstützt den Autorisierungscode-Flow mit PKCE (`S256`), Refresh Tokens und **dynamische Client-Registrierung**.

Die dynamische Registrierung hat den manuellen Schritt für ältere Clients entfernt: ohne sie
benötigte jeder Client eine vorab ausgegebene `client_id` vom Anbieter.

Betrachte dies als Kompatibilitätsverhalten, nicht als Design, das man kopieren sollte. Die Revision der Spezifikation vom `2026-07-28` deprekiert die dynamische Client-Registrierung zugunsten von Client ID Metadata Documents, bei denen der Client ein Metadaten-Dokument unter einer stabilen HTTPS-URL hostet, und diese URL *ist* die `client_id`. DCR funktioniert vorerst weiter, aber ein heute gebauter Server sollte CIMD planen und DCR nur für ältere Clients behalten.

### Werkzeug-Anmerkungen sind keine Dekoration

Jedes Werkzeug trägt einen `title` und zutreffende Hinweise: `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`.

Zwei Gründe, in sie zu investieren. Erstens nutzen Clients die Hinweise, um zu entscheiden, was sie mit dem Benutzer bestätigen — ein Client kann eine schreibgeschützte Abfrage automatisch ausführen und vor einem Löschen um Erlaubnis bitten. Die Spezifikation macht klar, dass Anmerkungen unzuverlässige Hinweise sind, keine Autorisierung: Sie gestalten, was ein Client anzubieten versucht, sie stoppen aber nichts auf dem Server, der Server muss seine eigenen Regeln durchsetzen. Zweitens verlangen die wichtigsten Connector-Verzeichnisse mittlerweile *verbindlich* Anmerkungen für eine Überprüfung; ein Server, dessen Werkzeuge keine Titel und Hinweise haben, wird zurückgewiesen, egal wie gut er funktioniert.

### Identifikatoren nicht erfindbar machen

Plattform-Identifikatoren sind undurchsichtige Strings, die von `list_connections` zurückgegeben werden, und die Schemabeschreibung sagt explizit, dass sie wortwörtlich kopiert und nie erraten werden dürfen. Der Server lehnt alles andere ab.

Modelle sind gewandte Rater. Jeder schreibfähige Server sollte annehmen, dass ein Identifikator irgendwann halluziniert wird und diesen Pfad laut und früh fehlschlagen lassen, statt auf einen plausibel aussehenden Wert zu reagieren.

### Vor Veröffentlichen scheitern, mit einer umsetzbaren Meldung

Einige Netzwerke lehnen rein Text-Beiträge ab und verlangen ein Bild oder Video. Das wird validiert, wenn der Beitrag geplant wird, und der Fehler nennt die Plattform und die fehlende Voraussetzung.

Ein Agent kann von "Instagram verlangt Medien — hänge ein Bild oder Video an" ohne eine weitere Anfrage genesen. Von einem generischen `400` kann er nicht genesen.

### Wiederholungen sicher machen

Die zwei Werkzeuge, die Inhalt erzeugen, `create_post` und `update_post`, akzeptieren einen Idempotenz-Schlüssel: Wird er bei einer identischen Anfrage wiederverwendet, wiederholt sich die ursprüngliche Antwort, anstatt einen zweiten Beitrag zu erstellen. Agent-Laufzeiten wiederholen bei Timeouts; ohne Idempotenz wird eine langsame Antwort zur doppelten Veröffentlichung. Die anderen Schreibwerkzeuge — Löschungen, Medien-Schritte, LinkedIn-Reaktionen und Kommentare — nehmen keinen an, daher ist eine Wiederholung dort nicht automatisch sicher. Es ist gut zu wissen, welche eigenen Mutationen geschützt sind und welche nicht.

### Einen Weg bieten, der nichts veröffentlicht

Der Server akzeptiert ein reserviertes Ziel, `publora-playground`, das validiert und wie ein echtes Ziel bestätigt wird und dann verworfen wird — nichts erreicht ein Live-Konto. Es ist im Werkzeug-Schema selbst beschrieben, das jeder Client ohne Anmeldeinformationen lesen kann: das `platforms`-Feld von `create_post` dokumentiert es als "ein Verbindungstest-Ziel, das keine echte Verbindung erfordert — der Beitrag wird bestätigt und verworfen, nichts wird veröffentlicht". Man ruft es auf, indem man es als einzigen Eintrag angibt: `platforms: ["publora-playground"]`.

Das hat sich als eines der nützlichsten Details der ganzen Oberfläche erwiesen. Prüfer von Connector-Verzeichnissen, Mitwirkende und CI können den gesamten Schreibpfad Ende-zu-Ende ohne Risiko für ein echtes Publikum testen. Jeder MCP-Server mit irreversiblen Aktionen profitiert von einem dokumentierten No-Op-Ziel.

## Ergebnisse und Auswirkungen

- Der Veröffentlichungs-Schritt wanderte vom Browser in dasselbe Gespräch, in dem der Inhalt geschrieben wird, und die Entwurf-zuerst-Gewohnheit hält einen Menschen im Prozess. Sei genau darüber, was das heißt: ein Entwurf ist eine Vereinbarung, keine Grenze. Dieselbe Berechtigung kann planen oder veröffentlichen, daher muss jeder, der ein echtes Freigabetor braucht, das außerhalb der Werkzeugoberfläche durchsetzen — separate Berechtigungen oder eine Policy-Schicht vor dem Server.
- Netzwerk-spezifische Unterschiede — Medienanforderungen, Threading, Antwortkontrollen — werden einmalig im Server gehandhabt statt in jedem Agenten, der mit ihm spricht.
- Derselbe Server unterstützt mehrere MCP-Clients ohne vorab ausgegebene Berechtigungsdaten.
    Aktuelle Clients können Client ID Metadata Documents nutzen; DCR bleibt eine Rückfallebene
    für ältere Clients.
- Die oben genannten Design-Einschränkungen wurden von Connector-Verzeichnis-Reviews ebenso geprägt wie von Benutzern: Anmerkungen, OAuth und ein sicherer Testziel waren jeweils von mindestens einer gefordert.

## Verweise

- [Publora MCP Server (Quellcode)](https://github.com/publora/mcp-server)
- [Publora API- und MCP-Dokumentation](https://docs.publora.com)
- [MCP-Registereintrag: `com.publora/mcp-server`](https://registry.modelcontextprotocol.io/v0/servers?search=com.publora/mcp-server)
- [MCP-Spezifikation — Autorisierung](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP-Spezifikation — Werkzeug-Anmerkungen](https://modelcontextprotocol.io/docs/concepts/tools)

## Was kommt als Nächstes

- Nimm einen MCP-Server, den du baust, und überprüfe die drei einfachsten Verbesserungen hier: Anmerkungen auf jedem Werkzeug, ein Idempotenz-Schlüssel bei jedem Schreibvorgang und ein dokumentiertes No-Op-Ziel.
- Versuche die offene Entdeckung: rufe `tools/list` an einem öffentlichen entfernten Server ohne Anmeldeinformationen auf, dann ein Werkzeug und untersuche die `401`-Herausforderung.
- Überlege, was „Rückgängig“ für deine Domäne bedeutet. Veröffentlichen hat Entwürfe und Löschungen; wenn deine Aktionen kein Äquivalent haben, gehört die Bestätigung in das Werkzeugdesign, nicht in die Eingabeaufforderung.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->