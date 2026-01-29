# Pagsubok ng halimbawang ito

## -1- I-install ang mga kinakailangang dependency

```bash
dotnet restore
```

## -3- Patakbuhin ang halimbawa

```bash
dotnet run
```

## -4- Subukan ang halimbawa

Habang tumatakbo ang server sa isang terminal, magbukas ng isa pang terminal at patakbuhin ang sumusunod na utos:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Dapat nitong simulan ang isang web server na may visual na interface na magpapahintulot sa iyong subukan ang halimbawa.

Kapag nakakonekta na ang server:

- Subukang ilista ang mga tool at patakbuhin ang `add`, gamit ang mga argumento 2 at 4, dapat mong makita ang 6 bilang resulta.
- Pumunta sa resources at resource template at tawagin ang "greeting", maglagay ng pangalan at dapat mong makita ang pagbati gamit ang pangalang ibinigay mo.

### Pagsubok sa CLI mode

Maaari mo itong ilunsad nang direkta sa CLI mode sa pamamagitan ng pagpapatakbo ng sumusunod na utos:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Ipakikita nito ang lahat ng tool na magagamit sa server. Dapat mong makita ang sumusunod na output:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

Upang tawagin ang isang tool, i-type ang:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Dapat mong makita ang sumusunod na output:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
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
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.