# Ausführen dieses Beispiels

Es wird empfohlen, `uv` zu installieren, aber es ist nicht zwingend erforderlich, siehe [Anleitung](https://docs.astral.sh/uv/#highlights)

## -0- Erstelle eine virtuelle Umgebung

```bash
python -m venv venv
```

## -1- Aktiviere die virtuelle Umgebung

```bash
venv\Scrips\activate
```

## -2- Installiere die Abhängigkeiten

```bash
pip install "mcp[cli]"
```

## -3- Führe das Beispiel aus


```bash
python client.py
```

Du solltest eine Ausgabe ähnlich der folgenden sehen:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
                    INFO     Processing request of type ReadResourceRequest                                                                            server.py:534
CALL TOOL
                    INFO     Processing request of type CallToolRequest                                                                                server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.