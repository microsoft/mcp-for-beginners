# Pagpapatakbo ng sample na ito

Inirerekomenda kang mag-install ng `uv` ngunit hindi ito kailangang-kailangan, tingnan ang [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Gumawa ng virtual environment

```bash
python -m venv venv
```

## -1- I-activate ang virtual environment

```bash
venv\Scripts\activate
```

## -2- I-install ang mga dependencies

```bash
pip install "mcp[cli]"
```

## -3- Patakbuhin ang sample

```bash
python client.py
```

Makikita mo ang output na katulad ng:

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
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->