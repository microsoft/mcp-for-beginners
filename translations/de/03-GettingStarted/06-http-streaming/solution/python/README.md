<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c4da5949611d91b06d8a5d450aae8d6",
  "translation_date": "2025-07-13T21:16:39+00:00",
  "source_file": "03-GettingStarted/06-http-streaming/solution/python/README.md",
  "language_code": "de"
}
-->
# Ausführen dieses Beispiels

So starten Sie den klassischen HTTP-Streaming-Server und -Client sowie den MCP-Streaming-Server und -Client mit Python.

### Übersicht

- Sie richten einen MCP-Server ein, der Fortschrittsbenachrichtigungen an den Client sendet, während er Elemente verarbeitet.
- Der Client zeigt jede Benachrichtigung in Echtzeit an.
- Diese Anleitung behandelt Voraussetzungen, Einrichtung, Ausführung und Fehlerbehebung.

### Voraussetzungen

- Python 3.9 oder neuer
- Das Python-Paket `mcp` (Installation mit `pip install mcp`)

### Installation & Einrichtung

1. Klonen Sie das Repository oder laden Sie die Lösungsdateien herunter.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Erstellen und aktivieren Sie eine virtuelle Umgebung (empfohlen):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Installieren Sie die benötigten Abhängigkeiten:**

   ```pwsh
   pip install "mcp[cli]"
   ```

### Dateien

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Client:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Ausführen des klassischen HTTP-Streaming-Servers

1. Wechseln Sie in das Lösungsverzeichnis:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Starten Sie den klassischen HTTP-Streaming-Server:

   ```pwsh
   python server.py
   ```

3. Der Server startet und zeigt Folgendes an:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Ausführen des klassischen HTTP-Streaming-Clients

1. Öffnen Sie ein neues Terminal (aktivieren Sie dieselbe virtuelle Umgebung und das Verzeichnis):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Sie sollten die gestreamten Nachrichten nacheinander ausgegeben sehen:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### Ausführen des MCP-Streaming-Servers

1. Wechseln Sie in das Lösungsverzeichnis:  
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```  
2. Starten Sie den MCP-Server mit dem streamable-http-Transport:  
   ```pwsh
   python server.py mcp
   ```  
3. Der Server startet und zeigt Folgendes an:  
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Ausführen des MCP-Streaming-Clients

1. Öffnen Sie ein neues Terminal (aktivieren Sie dieselbe virtuelle Umgebung und das Verzeichnis):  
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```  
2. Sie sollten Benachrichtigungen in Echtzeit sehen, während der Server jedes Element verarbeitet:  
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### Wichtige Implementierungsschritte

1. **Erstellen Sie den MCP-Server mit FastMCP.**  
2. **Definieren Sie ein Tool, das eine Liste verarbeitet und Benachrichtigungen mit `ctx.info()` oder `ctx.log()` sendet.**  
3. **Starten Sie den Server mit `transport="streamable-http"`.**  
4. **Implementieren Sie einen Client mit einem Nachrichten-Handler, der Benachrichtigungen beim Eintreffen anzeigt.**

### Code-Durchgang
- Der Server verwendet asynchrone Funktionen und den MCP-Kontext, um Fortschrittsupdates zu senden.  
- Der Client implementiert einen asynchronen Nachrichten-Handler, der Benachrichtigungen und das Endergebnis ausgibt.

### Tipps & Fehlerbehebung

- Verwenden Sie `async/await` für nicht blockierende Operationen.  
- Behandeln Sie Ausnahmen sowohl im Server als auch im Client für mehr Stabilität.  
- Testen Sie mit mehreren Clients, um Echtzeit-Updates zu beobachten.  
- Bei Fehlern prüfen Sie Ihre Python-Version und stellen Sie sicher, dass alle Abhängigkeiten installiert sind.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.