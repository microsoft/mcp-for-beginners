# Dit voorbeeld uitvoeren

Het wordt aanbevolen om `uv` te installeren, maar het is niet verplicht. Zie [instructies](https://docs.astral.sh/uv/#highlights).

## -1- Installeer de afhankelijkheden

```bash
npm install
```

## -3- Voer het voorbeeld uit

```bash
npm run build
```

## -4- Test het voorbeeld

Met de server actief in één terminal, open een andere terminal en voer het volgende commando uit:

```bash
npm run inspector
```

Hiermee wordt een webserver gestart met een visuele interface waarmee je het voorbeeld kunt testen.

Zodra de server is verbonden:

- probeer tools op te sommen en voer `add` uit, met de argumenten 2 en 4. Je zou 6 in het resultaat moeten zien.
- ga naar resources en resource template en roep "greeting" aan, typ een naam in en je zou een begroeting moeten zien met de naam die je hebt opgegeven.

### Testen in CLI-modus

De inspector die je hebt uitgevoerd is eigenlijk een Node.js-app en `mcp dev` is een wrapper eromheen.

Je kunt deze direct in CLI-modus starten door het volgende commando uit te voeren:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Dit zal alle beschikbare tools in de server weergeven. Je zou de volgende output moeten zien:

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

Om een tool aan te roepen, typ:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Je zou de volgende output moeten zien:

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
> Het is meestal veel sneller om de inspector in CLI-modus uit te voeren dan in de browser.
> Lees meer over de inspector [hier](https://github.com/modelcontextprotocol/inspector).

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.