# MCP OAuth2 Demo

> [!WARNING]
> Dies ist ein lokales Lernbeispiel, kein produktiver Autorisierungsdienst. Es
> verwendet einen internen Client und generiert beim Start einen neuen Signierschlüssel. Verwenden Sie niemals
> es mit einem geteilten, standardmäßigen oder quellcodekontrollierten Client-Geheimnis.

## Einführung

OAuth2 ist das branchenübliche Protokoll für Autorisierung, das sicheren Zugriff auf Ressourcen ermöglicht, ohne Anmeldeinformationen zu teilen. In MCP (Model Context Protocol)-Implementierungen bietet OAuth2 eine robuste Methode zur Authentifizierung und Autorisierung von Clients (wie KI-Agenten), um auf MCP-Server und deren Tools zuzugreifen.

Diese Lektion zeigt, wie man OAuth2-Authentifizierung für MCP-Server mit Spring Boot implementiert, ein gängiges Muster für Unternehmens- und Produktionseinsätze.

## Lernziele

Am Ende dieser Lektion werden Sie:
- Verstehen, wie OAuth2 in MCP-Server integriert wird
- Einen Spring Authorization Server für die Token-Ausgabe implementieren
- MCP-Endpunkte mit JWT-basierter Authentifizierung schützen
- Den Client-Credentials-Flow für die Maschine-zu-Maschine-Kommunikation konfigurieren

## Voraussetzungen

- Grundkenntnisse in Java und Spring Boot
- Vertrautheit mit MCP-Konzepten aus früheren Modulen
- Maven oder Gradle installiert

---

## Projektübersicht

Dieses Projekt ist eine **minimalistische Spring Boot-Anwendung**, die sowohl fungiert als:

* ein **Spring Authorization Server** (der JWT-Zugriffstoken über den `client_credentials`-Flow ausstellt), und  
* ein **Resource Server** (der seinen eigenen `/hello`-Endpunkt schützt).

Es spiegelt die Einrichtung wider, die im [Spring-Blogbeitrag (2. Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) gezeigt wird.

---

## Schnellstart (lokal)

```bash
# Verwenden Sie einen eindeutigen lokalen Wert und halten Sie ihn nach Möglichkeit aus der Shell-Historie fern.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# Token abrufen
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# geschützten Endpunkt aufrufen
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Testen der OAuth2-Konfiguration

Sie können die OAuth2-Sicherheitskonfiguration mit den folgenden Schritten testen:

### 1. Überprüfen Sie, ob der Server läuft und gesichert ist

```bash
# Dies sollte 401 Unauthorized zurückgeben und bestätigen, dass die OAuth2-Sicherheit aktiv ist
curl -v http://localhost:8081/
```

### 2. Ein Zugriffstoken mit Client-Anmeldeinformationen abrufen

```bash
# Hole und extrahiere die vollständige Token-Antwort
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Oder um nur das Token zu extrahieren (benötigt jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Stellen Sie in PowerShell das lokale Geheimnis ein, bevor Sie Maven ausführen:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Auf den geschützten Endpunkt mit dem Token zugreifen

```bash
# Verwendung des gespeicherten Tokens
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Oder direkt mit dem Tokenwert
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Eine erfolgreiche Antwort mit "Hello from MCP OAuth2 Demo!" bestätigt, dass die OAuth2-Konfiguration korrekt funktioniert.

---

## Container-Build

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Sicherheit im Produktivbetrieb

Für den Produktionseinsatz verwenden Sie einen dedizierten Identitätsanbieter statt
dieses in Prozess laufende Demo-Autorisierungssystem. Speichern Sie Anmeldeinformationen in einem verwalteten
Geheimnisspeicher, rotieren Sie sie, verwenden Sie persistente Signierschlüssel, beschränken Sie Scopes, und
setzen Sie einen expliziten Herausgeber. Platzieren Sie niemals ein Client-Geheimnis im Quellcode, Container
Images, Deployment-Manifeste oder Befehlsausgaben.

Für Azure Container Apps speichern Sie den Wert als Container Apps Geheimnis, das idealerweise von
Key Vault unterstützt wird, und geben Sie dann nur eine Geheimnisreferenz über die
Umgebungsvariable `OAUTH_CLIENT_SECRET` weiter.

---

## Deployment zu **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Der Ingress-FQDN wird Ihr **Issuer** (`https://<fqdn>`).  
Azure stellt automatisch ein vertrauenswürdiges TLS-Zertifikat für `*.azurecontainerapps.io` bereit.

---

## Integration in **Azure API Management**

Fügen Sie diese eingehende Richtlinie zu Ihrer API hinzu:

```xml
<inbound>
  <validate-jwt header-name="Authorization">
    <openid-config url="https://<fqdn>/.well-known/openid-configuration"/>
    <audiences>
      <audience>mcp-client</audience>
    </audiences>
  </validate-jwt>
  <base/>
</inbound>
```

APIM ruft JWKS ab und validiert jede Anfrage.

---

## Was kommt als Nächstes

- [5.4 Root-Kontexte](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->