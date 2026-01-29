# Pagpapatakbo ng sample na ito

## -1- I-install ang mga kinakailangan

```bash
dotnet restore
```

## -2- Patakbuhin ang sample

```bash
dotnet run
```

## -3- Subukan ang sample

Magbukas ng hiwalay na terminal bago patakbuhin ang nasa ibaba (siguraduhing tumatakbo pa rin ang server).

Habang tumatakbo ang server sa isang terminal, magbukas ng isa pang terminal at patakbuhin ang sumusunod na command:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Dapat itong magsimula ng isang web server na may visual na interface na magpapahintulot sa iyo na subukan ang sample.

> Siguraduhing ang **Streamable HTTP** ay napili bilang uri ng transportasyon, at ang URL ay `http://localhost:3001/mcp`.

Kapag nakakonekta na ang server:

- Subukang ilista ang mga tools at patakbuhin ang `add`, gamit ang mga argumento 2 at 4, dapat mong makita ang 6 sa resulta.
- Pumunta sa resources at resource template at tawagin ang "greeting", mag-type ng pangalan at dapat mong makita ang pagbati gamit ang pangalan na ibinigay mo.

### Pagsubok sa CLI mode

Maaari mo itong ilunsad nang direkta sa CLI mode sa pamamagitan ng pagpapatakbo ng sumusunod na command:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Ililista nito ang lahat ng tools na available sa server. Dapat mong makita ang sumusunod na output:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

Para tawagin ang isang tool, i-type:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
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
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.