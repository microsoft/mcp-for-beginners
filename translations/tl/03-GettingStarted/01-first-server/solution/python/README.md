# Pagpapatakbo ng sample na ito

Inirerekomenda na i-install ang `uv` pero hindi ito kinakailangan, tingnan ang [mga tagubilin](https://docs.astral.sh/uv/#highlights)

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
mcp run server.py
```

## -4- Subukan ang sample

Habang tumatakbo ang server sa isang terminal, magbukas ng isa pang terminal at patakbuhin ang sumusunod na command:

```bash
mcp dev server.py
```

Dapat magsimula ito ng isang web server na may visual interface na magpapahintulot sa iyo na subukan ang sample.

Kapag nakakonekta na ang server:

- Subukang i-lista ang mga tools at patakbuhin ang `add`, gamit ang args 2 at 4, dapat mong makita ang 6 sa resulta.

- Pumunta sa resources at resource template at tawagin ang get_greeting, mag-type ng pangalan at dapat mong makita ang pagbati gamit ang pangalan na ibinigay mo.

### Pagsubok sa CLI mode

Ang inspector na pinatakbo mo ay aktwal na isang Node.js app at ang `mcp dev` ay isang wrapper nito.

Maaari mo itong patakbuhin nang direkta sa CLI mode sa pamamagitan ng pagpapatakbo ng sumusunod na command:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

Ili-lista nito ang lahat ng tools na available sa server. Dapat mong makita ang sumusunod na output:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

Para mag-invoke ng tool, i-type:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Dapat mong makita ang sumusunod na output:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Karaniwang mas mabilis patakbuhin ang inspector sa CLI mode kaysa sa browser.
> Magbasa pa tungkol sa inspector [dito](https://github.com/modelcontextprotocol/inspector).

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.