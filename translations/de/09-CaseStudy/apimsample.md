# Fallstudie: REST-API als MCP-Server im API Management bereitstellen

Azure API Management ist ein Dienst, der ein Gateway über Ihre API-Endpunkte bereitstellt. Azure API Management fungiert dabei wie ein Proxy vor Ihren APIs und entscheidet, wie mit eingehenden Anfragen verfahren wird.

Durch die Verwendung erhalten Sie eine Vielzahl von Funktionen, darunter:

- **Sicherheit**, Sie können alles verwenden, von API-Schlüsseln über JWT bis hin zu verwalteten Identitäten.
- **Rate Limiting**, eine großartige Funktion, mit der Sie festlegen können, wie viele Anrufe pro Zeiteinheit zugelassen werden. Dies sorgt dafür, dass alle Benutzer eine großartige Erfahrung machen und Ihr Dienst nicht von Anfragen überlastet wird.
- **Skalierung & Lastverteilung**. Sie können mehrere Endpunkte einrichten, um die Last zu verteilen, und auch festlegen, wie die Last verteilt wird.
- **KI-Funktionen wie semantisches Caching**, Token-Limits, Token-Überwachung und mehr. Diese großartigen Funktionen verbessern die Reaktionsfähigkeit und ermöglichen Ihnen außerdem die Kontrolle über Ihren Tokenverbrauch. [Hier erfahren Sie mehr](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Warum MCP + Azure API Management?

Das Model Context Protocol entwickelt sich schnell zum Standard für agentenbasierte KI-Anwendungen und um Werkzeuge und Daten konsistent bereitzustellen. Azure API Management ist eine naheliegende Wahl, wenn Sie APIs verwalten müssen. MCP-Server integrieren sich oft mit anderen APIs, um Anfragen beispielsweise an ein Werkzeug weiterzuleiten. Daher macht die Kombination von Azure API Management und MCP viel Sinn.

## Überblick

In diesem speziellen Anwendungsfall lernen wir, wie man API-Endpunkte als MCP-Server bereitstellt. Dadurch können wir diese Endpunkte einfach als Teil einer agentenbasierten Anwendung nutzen und gleichzeitig die Funktionen von Azure API Management verwenden.

## Hauptfunktionen

- Sie wählen die Endpunkt-Methoden aus, die Sie als Werkzeuge bereitstellen möchten.
- Die zusätzlichen Funktionen, die Sie erhalten, hängen davon ab, was Sie im Richtlinienbereich für Ihre API konfigurieren. Hier zeigen wir Ihnen, wie Sie Rate Limiting hinzufügen können.

## Vorbereitung: API importieren

Wenn Sie bereits eine API im Azure API Management haben, großartig, dann können Sie diesen Schritt überspringen. Wenn nicht, schauen Sie sich diesen Link an: [API in Azure API Management importieren](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API als MCP-Server bereitstellen

Um die API-Endpunkte bereitzustellen, befolgen Sie diese Schritte:

1. Navigieren Sie zum Azure-Portal unter folgender Adresse <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Navigieren Sie zu Ihrer API-Management-Instanz.

1. Wählen Sie im linken Menü APIs > MCP Servers > + Neuen MCP-Server erstellen.

1. Wählen Sie bei API eine REST-API aus, die Sie als MCP-Server bereitstellen möchten.

1. Wählen Sie eine oder mehrere API-Operationen aus, die Sie als Werkzeuge bereitstellen möchten. Sie können alle Operationen oder nur bestimmte auswählen.

    ![Methoden zum Bereitstellen auswählen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Wählen Sie **Erstellen**.

1. Navigieren Sie zu den Menüoptionen **APIs** und **MCP Servers**, Sie sollten Folgendes sehen:

    ![MCP-Server im Hauptfenster sehen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Der MCP-Server wurde erstellt und die API-Operationen werden als Werkzeuge bereitgestellt. Der MCP-Server wird im MCP-Servers-Bereich aufgelistet. Die Spalte URL zeigt den Endpunkt des MCP-Servers, den Sie für Tests oder in einer Client-Anwendung aufrufen können.

## Optional: Richtlinien konfigurieren

Azure API Management verwendet das Kernkonzept von Richtlinien, mit denen Sie verschiedene Regeln für Ihre Endpunkte festlegen, zum Beispiel Rate Limiting oder semantisches Caching. Diese Richtlinien werden in XML verfasst.

So können Sie eine Richtlinie einrichten, um Ihren MCP-Server zu begrenzen:

1. Wählen Sie im Portal unter APIs **MCP Servers** aus.

1. Wählen Sie den von Ihnen erstellten MCP-Server aus.

1. Wählen Sie im linken Menü unter MCP **Policys**.

1. Fügen Sie im Richtlinien-Editor Richtlinien hinzu oder bearbeiten Sie diese, die Sie auf die Werkzeuge des MCP-Servers anwenden möchten. Die Richtlinien werden im XML-Format definiert. Zum Beispiel können Sie eine Richtlinie hinzufügen, um die Aufrufe der Werkzeuge des MCP-Servers zu begrenzen (in diesem Beispiel 5 Aufrufe pro 30 Sekunden pro Client-IP-Adresse). Hier ist der XML-Code, der das Rate Limiting bewirkt:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Hier ein Bild des Richtlinien-Editors:

    ![Richtlinien-Editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Ausprobieren

Lassen Sie uns sicherstellen, dass unser MCP-Server wie vorgesehen funktioniert.

> [!NOTE]
> Azure API Management stellt diesen Server derzeit über den Streamable
> HTTP-`/mcp`-Endpunkt bereit. Der ältere HTTP+SSE `/sse`-Transport ist veraltet und
> sollte nur mit Legacy-Clients verwendet werden.

Dafür verwenden wir Visual Studio Code und GitHub Copilot in seinem Agent-Modus. Wir fügen den MCP-Server zu einer *mcp.json* hinzu. Auf diese Weise fungiert Visual Studio Code als Client mit agentenbasierten Fähigkeiten und Endbenutzer können eine Eingabeaufforderung eingeben und mit dem Server interagieren.

So fügen Sie den MCP-Server in Visual Studio Code hinzu:

1. Verwenden Sie den MCP: **Server hinzufügen-Befehl aus der Befehlspalette**.

1. Wählen Sie bei Aufforderung den Servertyp: **HTTP (HTTP oder Server Sent Events)**.

1. Geben Sie die Streamable HTTP-URL ein, die für den MCP-Server im API Management angezeigt wird.
    Zum Beispiel:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Geben Sie eine Server-ID Ihrer Wahl ein. Dieser Wert ist nicht wichtig, hilft Ihnen jedoch, sich an diese Serverinstanz zu erinnern.

1. Wählen Sie, ob die Konfiguration in den Arbeitsbereichseinstellungen oder in den Benutzereinstellungen gespeichert werden soll.

  - **Arbeitsbereichseinstellungen** - Die Serverkonfiguration wird in einer .vscode/mcp.json-Datei nur im aktuellen Arbeitsbereich gespeichert.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Benutzereinstellungen** - Die Serverkonfiguration wird zu Ihrer globalen *settings.json*-Datei hinzugefügt und ist in allen Arbeitsbereichen verfügbar. Die Konfiguration sieht ungefähr so aus:

    ![Benutzereinstellung](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Sie müssen auch eine Konfiguration hinzufügen, nämlich einen Header, der sicherstellt, dass die Authentifizierung bei Azure API Management korrekt erfolgt. Es wird ein Header namens **Ocp-Apim-Subscription-Key* verwendet.

    - So fügen Sie es den Einstellungen hinzu:

    ![Header zur Authentifizierung hinzufügen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), dadurch wird eine Eingabeaufforderung angezeigt, in der Sie den API-Schlüssel eingeben, den Sie im Azure-Portal für Ihre Azure API Management-Instanz finden.

   - Um ihn stattdessen zu *mcp.json* hinzuzufügen, können Sie ihn wie folgt ergänzen:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Agent-Modus verwenden

Jetzt sind wir sowohl in den Einstellungen als auch in *.vscode/mcp.json* eingerichtet. Probieren wir es aus.

Es sollte ein Werkzeuge-Symbol geben, ähnlich wie hier, wo die vom Server bereitgestellten Werkzeuge aufgeführt sind:

![Werkzeuge vom Server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klicken Sie auf das Werkzeuge-Symbol, und Sie sollten eine Liste von Werkzeugen sehen, wie hier:

    ![Werkzeuge](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Geben Sie eine Eingabeaufforderung im Chat ein, um das Werkzeug aufzurufen. Wenn Sie beispielsweise ein Werkzeug ausgewählt haben, um Informationen über eine Bestellung abzurufen, können Sie den Agenten dazu befragen. Hier ist ein Beispiel für eine Eingabe:

    ```text
    get information from order 2
    ```

    Ihnen wird jetzt ein Werkzeuge-Symbol angezeigt, das Sie auffordert, den Aufruf eines Werkzeugs fortzusetzen. Wählen Sie die Option zum Fortfahren, und Sie sollten die folgende Ausgabe sehen:

    ![Ergebnis der Eingabeaufforderung](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Was Sie oben sehen, hängt davon ab, welche Werkzeuge Sie eingerichtet haben, aber die Idee ist, dass Sie eine textuelle Antwort ähnlich wie oben erhalten**


## Referenzen

Hier erfahren Sie, wie Sie mehr lernen können:

- [Tutorial zu Azure API Management und MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-Beispiel: Sichere Remote-MCP-Server mit Azure API Management (experimentell)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-Client-Autorisierungslabor](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Verwenden Sie die Azure API Management-Erweiterung für VS Code zum Importieren und Verwalten von APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrieren und entdecken Sie Remote-MCP-Server im Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Tolles Repository, das viele KI-Funktionalitäten mit Azure API Management zeigt
- [AI Gateway Workshops](https://azure-samples.github.io/AI-Gateway/) Enthält Workshops mit Azure Portal, eine hervorragende Möglichkeit, KI-Funktionen zu evaluieren.

## Was kommt als Nächstes

- Zurück zu: [Übersicht Fallstudien](./README.md)
- Nächstes: [Azure AI Reiseagenten](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->