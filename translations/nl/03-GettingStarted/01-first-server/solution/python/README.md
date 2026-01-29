# Dit voorbeeld uitvoeren

Het wordt aanbevolen om `uv` te installeren, maar het is niet verplicht. Zie [instructies](https://docs.astral.sh/uv/#highlights).

## -0- Maak een virtuele omgeving

```bash
python -m venv venv
```

## -1- Activeer de virtuele omgeving

```bash
venv\Scripts\activate
```

## -2- Installeer de afhankelijkheden

```bash
pip install "mcp[cli]"
```

## -3- Voer het voorbeeld uit

```bash
mcp run server.py
```

## -4- Test het voorbeeld

Met de server actief in één terminal, open een andere terminal en voer het volgende commando uit:

```bash
mcp dev server.py
```

Dit zou een webserver moeten starten met een visuele interface waarmee je het voorbeeld kunt testen.

Zodra de server is verbonden:

- probeer tools op te sommen en voer `add` uit, met de argumenten 2 en 4. Je zou 6 in het resultaat moeten zien.

- ga naar resources en resource template en roep get_greeting aan, typ een naam in en je zou een begroeting moeten zien met de naam die je hebt opgegeven.

### Testen in CLI-modus

De inspector die je hebt uitgevoerd is eigenlijk een Node.js-app en `mcp dev` is een wrapper eromheen.

Je kunt deze direct in CLI-modus starten door het volgende commando uit te voeren:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
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
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.