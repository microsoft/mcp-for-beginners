# Dit voorbeeld uitvoeren

## -1- Installeer de afhankelijkheden

```bash
dotnet restore
```

## -3- Voer het voorbeeld uit

```bash
dotnet run
```

## -4- Test het voorbeeld

Met de server actief in één terminal, open een andere terminal en voer het volgende commando uit:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Dit zou een webserver moeten starten met een visuele interface waarmee je het voorbeeld kunt testen.

Zodra de server is verbonden:

- probeer tools op te sommen en voer `add` uit, met argumenten 2 en 4, je zou 6 in het resultaat moeten zien.
- ga naar resources en resource template en roep "greeting" aan, typ een naam in en je zou een begroeting moeten zien met de naam die je hebt opgegeven.

### Testen in CLI-modus

Je kunt het direct in CLI-modus starten door het volgende commando uit te voeren:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Dit zal alle beschikbare tools in de server opsommen. Je zou de volgende output moeten zien:

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

Om een tool aan te roepen, typ:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Je zou de volgende output moeten zien:

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
> Het is meestal veel sneller om de inspector in CLI-modus te draaien dan in de browser.
> Lees meer over de inspector [hier](https://github.com/modelcontextprotocol/inspector).

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.