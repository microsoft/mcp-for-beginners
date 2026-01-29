# Dit voorbeeld uitvoeren

Het wordt aanbevolen om `uv` te installeren, maar het is niet verplicht, zie [instructies](https://docs.astral.sh/uv/#highlights)

## -0- Maak een virtuele omgeving aan

```bash
python -m venv venv
```

## -1- Activeer de virtuele omgeving

```bash
venv\Scrips\activate
```

## -2- Installeer de afhankelijkheden

```bash
pip install "mcp[cli]"
```

## -3- Voer het voorbeeld uit


```bash
python client.py
```

Je zou een output moeten zien die lijkt op:

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

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.