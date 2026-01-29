# Pagtakbo ng halimbawang ito

Inirerekomenda na i-install ang `uv` pero hindi ito kinakailangan, tingnan ang [mga tagubilin](https://docs.astral.sh/uv/#highlights)

## -1- I-install ang mga kinakailangang dependency

```bash
npm install
```

## -3- Patakbuhin ang halimbawa

```bash
npm run build
```

## -4- Subukan ang halimbawa

Habang tumatakbo ang server sa isang terminal, magbukas ng isa pang terminal at patakbuhin ang sumusunod na utos:

```bash
npm run inspector
```

Dapat nitong simulan ang isang web server na may visual na interface na magpapahintulot sa iyo na subukan ang halimbawa.

Kapag nakakonekta na ang server:

- Subukang ilista ang mga tool at patakbuhin ang `add`, gamit ang mga argumento na 2 at 4, dapat mong makita ang 6 bilang resulta.
- Pumunta sa mga resources at resource template at tawagin ang "greeting", mag-type ng isang pangalan at dapat mong makita ang pagbati gamit ang pangalang ibinigay mo.

### Pagsubok sa CLI mode

Ang inspector na pinatakbo mo ay aktwal na isang Node.js app at ang `mcp dev` ay isang wrapper nito.

Maaari mo itong patakbuhin nang direkta sa CLI mode gamit ang sumusunod na utos:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Ili-lista nito ang lahat ng mga tool na available sa server. Dapat mong makita ang sumusunod na output:

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

Upang tawagin ang isang tool, i-type:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi eksaktong interpretasyon. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.