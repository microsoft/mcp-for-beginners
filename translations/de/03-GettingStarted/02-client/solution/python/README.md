# Ausführen dieses Beispiels

Es wird empfohlen `uv` zu installieren, ist aber nicht zwingend erforderlich, siehe [Anleitung](https://docs.astral.sh/uv/#highlights)

## -0- Erstellen Sie eine virtuelle Umgebung

```bash
python -m venv venv
```

## -1- Aktivieren Sie die virtuelle Umgebung

```bash
venv\Scripts\activate
```

## -2- Installieren Sie die Abhängigkeiten

```bash
pip install "mcp[cli]"
```

## -3- Führen Sie das Beispiel aus

```bash
python client.py
```

Sie sollten eine ähnliche Ausgabe sehen:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
INFO Processing request of type ListToolsRequest server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
INFO Processing request of type ReadResourceRequest server.py:534
CALL TOOL
INFO Processing request of type CallToolRequest server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->