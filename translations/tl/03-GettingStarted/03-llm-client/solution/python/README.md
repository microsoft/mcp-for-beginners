# Pagpapatakbo ng halimbawang ito

Inirerekomenda kang i-install ang `uv` ngunit hindi ito kinakailangan, tingnan ang [mga tagubilin](https://docs.astral.sh/uv/#highlights)

## -0- Lumikha ng isang virtual na kapaligiran

```bash
python -m venv venv
```

## -1- I-activate ang virtual na kapaligiran

```bash
venv\Scrips\activate
```

## -2- I-install ang mga dependencies

```bash
pip install "mcp[cli]"
pip install openai
```

## -3- I-configure ang Microsoft Foundry

I-deploy ang isang aktibong modelo tulad ng `gpt-5.1` sa Microsoft Foundry, pagkatapos itakda:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

Ang `AZURE_OPENAI_DEPLOYMENT` ay ang pangalan ng deployment, na maaaring magkakaiba mula sa
pangalan ng pangunahing modelo. Tingnan ang
[Microsoft Foundry na iskedyul ng pagretiro ng modelo](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
bago pumili ng modelo.

## -4- Patakbuhin ang halimbawa


```bash
python client.py
```

Dapat kang makakita ng output na katulad ng:

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
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->