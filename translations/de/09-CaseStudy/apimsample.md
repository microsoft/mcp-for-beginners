# Fallstudie: REST-API in API Management als MCP-Server bereitstellen

Azure API Management ist ein Dienst, der ein Gateway über Ihren API-Endpunkten bereitstellt. Dabei fungiert Azure API Management als Proxy vor Ihren APIs und kann entscheiden, was mit eingehenden Anfragen geschehen soll.

Durch die Nutzung dieses Dienstes erhalten Sie eine Vielzahl von Funktionen wie:

- **Sicherheit**: Sie können alles von API-Schlüsseln, JWT bis hin zu verwalteten Identitäten verwenden.
- **Ratenbegrenzung**: Eine großartige Funktion ist die Möglichkeit, zu entscheiden, wie viele Anfragen innerhalb einer bestimmten Zeiteinheit durchgelassen werden. Dies hilft sicherzustellen, dass alle Benutzer eine gute Erfahrung machen und Ihr Dienst nicht von Anfragen überlastet wird.
- **Skalierung & Lastverteilung**: Sie können mehrere Endpunkte einrichten, um die Last zu verteilen, und auch festlegen, wie die Last verteilt werden soll.
- **KI-Funktionen wie semantisches Caching**, Token-Limitierung und Token-Überwachung und mehr. Diese Funktionen verbessern die Reaktionsfähigkeit und helfen Ihnen, Ihre Token-Ausgaben im Blick zu behalten. [Mehr dazu hier](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Warum MCP + Azure API Management?

Das Model Context Protocol (MCP) wird schnell zum Standard für agentenbasierte KI-Anwendungen und zur konsistenten Bereitstellung von Tools und Daten. Azure API Management ist eine natürliche Wahl, wenn Sie APIs „verwalten“ müssen. MCP-Server integrieren oft andere APIs, um beispielsweise Anfragen an ein Tool zu lösen. Daher macht die Kombination von Azure API Management und MCP viel Sinn.

## Überblick

In diesem speziellen Anwendungsfall lernen wir, API-Endpunkte als MCP-Server bereitzustellen. Dadurch können wir diese Endpunkte leicht Teil einer agentenbasierten Anwendung machen und gleichzeitig die Funktionen von Azure API Management nutzen.

## Hauptfunktionen

- Sie wählen die Endpunktmethoden aus, die Sie als Tools bereitstellen möchten.
- Die zusätzlichen Funktionen hängen davon ab, was Sie im Richtlinienbereich für Ihre API konfigurieren. Hier zeigen wir Ihnen, wie Sie eine Ratenbegrenzung hinzufügen können.

## Vorbereitender Schritt: Eine API importieren

Wenn Sie bereits eine API in Azure API Management haben, können Sie diesen Schritt überspringen. Falls nicht, sehen Sie sich diesen Link an: [Eine API in Azure API Management importieren](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API als MCP-Server bereitstellen

Um die API-Endpunkte bereitzustellen, folgen Sie diesen Schritten:

1. Navigieren Sie zum Azure-Portal unter der folgenden Adresse: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. Navigieren Sie zu Ihrer API Management-Instanz.

1. Wählen Sie im linken Menü **APIs > MCP-Server > + Neuen MCP-Server erstellen**.

1. Wählen Sie eine REST-API aus, die als MCP-Server bereitgestellt werden soll.

1. Wählen Sie eine oder mehrere API-Operationen aus, die als Tools bereitgestellt werden sollen. Sie können alle Operationen oder nur bestimmte Operationen auswählen.

    ![Methoden auswählen, die bereitgestellt werden sollen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Wählen Sie **Erstellen**.

1. Navigieren Sie zu den Menüoptionen **APIs** und **MCP-Server**, Sie sollten Folgendes sehen:

    ![Den MCP-Server im Hauptbereich sehen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Der MCP-Server wurde erstellt und die API-Operationen wurden als Tools bereitgestellt. Der MCP-Server wird im MCP-Server-Bereich aufgelistet. Die Spalte „URL“ zeigt den Endpunkt des MCP-Servers, den Sie für Tests oder innerhalb einer Client-Anwendung aufrufen können.

## Optional: Richtlinien konfigurieren

Azure API Management hat das Kernkonzept der Richtlinien, bei denen Sie verschiedene Regeln für Ihre Endpunkte festlegen können, wie beispielsweise Ratenbegrenzung oder semantisches Caching. Diese Richtlinien werden in XML verfasst.

So richten Sie eine Richtlinie ein, um Ihren MCP-Server zu begrenzen:

1. Wählen Sie im Portal unter APIs **MCP-Server**.

1. Wählen Sie den MCP-Server aus, den Sie erstellt haben.

1. Wählen Sie im linken Menü unter MCP **Richtlinien**.

1. Fügen Sie im Richtlinien-Editor die Richtlinien hinzu oder bearbeiten Sie sie, die Sie auf die Tools des MCP-Servers anwenden möchten. Die Richtlinien werden im XML-Format definiert. Zum Beispiel können Sie eine Richtlinie hinzufügen, um die Anfragen an die Tools des MCP-Servers zu begrenzen (in diesem Beispiel 5 Anfragen pro 30 Sekunden pro Client-IP-Adresse). Hier ist XML, das eine Ratenbegrenzung bewirkt:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Hier ist ein Bild des Richtlinien-Editors:

    ![Richtlinien-Editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Ausprobieren

Lassen Sie uns sicherstellen, dass unser MCP-Server wie vorgesehen funktioniert.

Dazu verwenden wir Visual Studio Code und GitHub Copilot im Agent-Modus. Wir fügen den MCP-Server zu einer *mcp.json*-Datei hinzu. Dadurch fungiert Visual Studio Code als Client mit agentenbasierten Fähigkeiten, und Endbenutzer können eine Eingabeaufforderung eingeben und mit dem Server interagieren.

So fügen Sie den MCP-Server in Visual Studio Code hinzu:

1. Verwenden Sie den MCP: **Server hinzufügen-Befehl aus der Befehlspalette**.

1. Wenn Sie dazu aufgefordert werden, wählen Sie den Servertyp: **HTTP (HTTP oder Server Sent Events)**.

1. Geben Sie die URL des MCP-Servers in API Management ein. Beispiel: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (für SSE-Endpunkt) oder **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (für MCP-Endpunkt). Beachten Sie den Unterschied zwischen den Transporten: `/sse` oder `/mcp`.

1. Geben Sie eine Server-ID Ihrer Wahl ein. Dieser Wert ist nicht wichtig, hilft Ihnen jedoch, sich an diese Serverinstanz zu erinnern.

1. Wählen Sie aus, ob die Konfiguration in Ihren Arbeitsbereichseinstellungen oder Benutzereinstellungen gespeichert werden soll.

  - **Arbeitsbereichseinstellungen**: Die Serverkonfiguration wird in einer .vscode/mcp.json-Datei gespeichert, die nur im aktuellen Arbeitsbereich verfügbar ist.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    oder wenn Sie Streaming-HTTP als Transport wählen, sieht es etwas anders aus:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Benutzereinstellungen**: Die Serverkonfiguration wird Ihrer globalen *settings.json*-Datei hinzugefügt und ist in allen Arbeitsbereichen verfügbar. Die Konfiguration sieht ähnlich aus wie die folgende:

    ![Benutzereinstellung](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Sie müssen auch eine Konfiguration hinzufügen, einen Header, um sicherzustellen, dass die Authentifizierung ordnungsgemäß gegenüber Azure API Management erfolgt. Es wird ein Header namens **Ocp-Apim-Subscription-Key** verwendet.

    - So können Sie ihn zu den Einstellungen hinzufügen:

    ![Header für Authentifizierung hinzufügen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png). Dadurch wird eine Eingabeaufforderung angezeigt, die Sie nach dem API-Schlüsselwert fragt, den Sie im Azure-Portal für Ihre Azure API Management-Instanz finden können.

   - Um ihn stattdessen zu *mcp.json* hinzuzufügen, können Sie ihn wie folgt hinzufügen:

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

Jetzt sind wir entweder in den Einstellungen oder in *.vscode/mcp.json* eingerichtet. Lassen Sie uns das ausprobieren.

Es sollte ein Tools-Symbol wie folgt geben, wo die bereitgestellten Tools von Ihrem Server aufgelistet sind:

![Tools vom Server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klicken Sie auf das Tools-Symbol, und Sie sollten eine Liste von Tools wie folgt sehen:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Geben Sie eine Eingabeaufforderung im Chat ein, um das Tool aufzurufen. Zum Beispiel, wenn Sie ein Tool ausgewählt haben, um Informationen zu einer Bestellung zu erhalten, können Sie den Agenten nach einer Bestellung fragen. Hier ist ein Beispiel für eine Eingabeaufforderung:

    ```text
    get information from order 2
    ```

    Sie werden nun mit einem Tools-Symbol aufgefordert, ein Tool aufzurufen. Wählen Sie aus, das Tool weiter auszuführen, und Sie sollten nun eine Ausgabe wie folgt sehen:

    ![Ergebnis der Eingabeaufforderung](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Was Sie oben sehen, hängt davon ab, welche Tools Sie eingerichtet haben, aber die Idee ist, dass Sie eine textuelle Antwort wie oben erhalten.**

## Referenzen

Hier erfahren Sie mehr:

- [Tutorial zu Azure API Management und MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-Beispiel: Sichere Remote-MCP-Server mit Azure API Management (experimentell)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-Client-Autorisierungslabor](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Verwenden Sie die Azure API Management-Erweiterung für VS Code, um APIs zu importieren und zu verwalten](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Remote-MCP-Server in Azure API Center registrieren und entdecken](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway): Großartiges Repository, das viele KI-Funktionen mit Azure API Management zeigt.
- [AI Gateway Workshops](https://azure-samples.github.io/AI-Gateway/): Enthält Workshops mit dem Azure-Portal, eine großartige Möglichkeit, die KI-Funktionen zu evaluieren.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.