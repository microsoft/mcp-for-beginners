# Beispiel: Basis-Host

Eine Referenzimplementierung, die zeigt, wie man eine MCP-Host-Anwendung erstellt, die sich mit MCP-Servern verbindet und Tool-Benutzeroberflächen in einer sicheren Sandbox rendert.

Dieser Basis-Host kann auch verwendet werden, um MCP-Apps während der lokalen Entwicklung zu testen.

## Wichtige Dateien

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React-UI-Host mit Werkzeugauswahl, Parametereingabe und Iframe-Verwaltung
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Äußerer Iframe-Proxy mit Sicherheitsvalidierung und bidirektionaler Nachrichtenweiterleitung
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Kernlogik: Serververbindung, Werkzeugaufruf und AppBridge-Einrichtung

## Erste Schritte

```bash
npm install
npm run start
# Öffnen Sie http://localhost:8080
```

Standardmäßig versucht die Host-Anwendung, eine Verbindung zu einem MCP-Server unter `http://localhost:3001/mcp` herzustellen. Dieses Verhalten kann durch Setzen der Umgebungsvariable `SERVERS` mit einem JSON-Array von Server-URLs konfiguriert werden:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architektur

Dieses Beispiel verwendet ein Doppel-Iframe-Sandbox-Muster zur sicheren UI-Isolierung:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Warum zwei Iframes?**

- Der äußere Iframe läuft auf einer separaten Origin (Port 8081) und verhindert den direkten Zugriff auf den Host
- Der innere Iframe erhält HTML über `srcdoc` und ist durch Sandbox-Attribute eingeschränkt
- Nachrichten fließen durch den äußeren Iframe, der sie validiert und bidirektional weiterleitet

Diese Architektur stellt sicher, dass selbst wenn der Code der Werkzeug-UI bösartig ist, er keinen Zugriff auf das DOM, Cookies oder den JavaScript-Kontext der Host-Anwendung hat.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir um Genauigkeit bemüht sind, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in der Ausgangssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->