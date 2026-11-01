# Deze voorbeeld uitvoeren

Het wordt aanbevolen om `uv` te installeren maar het is niet verplicht, zie [instructies](https://docs.astral.sh/uv/#highlights)

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
pip install openai
```

## -3- Configureer Microsoft Foundry

Implementeer een actief model zoals `gpt-5.1` in Microsoft Foundry, stel dan in:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

`AZURE_OPENAI_DEPLOYMENT` is de naam van de implementatie, die kan verschillen van de
onderliggende modelnaam. Controleer de
[Microsoft Foundry model pensioenschema](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
voordat je een model selecteert.

## -4- Voer het voorbeeld uit


```bash
python client.py
```

Je zou een uitvoer moeten zien die lijkt op:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
Tool {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
CALLING LLM
TOOL:  {'function': {'arguments': '{"a":2,"b":20}', 'name': 'add'}, 'id': 'call_BCbyoCcMgq0jDwR8AuAF9QY3', 'type': 'function'}
[05/08/25 21:04:55] INFO     Processing request of type CallToolRequest                                                                                server.py:534
TOOLS result:  [TextContent(type='text', text='22', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->