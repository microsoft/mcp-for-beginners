# Dit voorbeeld uitvoeren

## -1- Installeer de afhankelijkheden

```bash
dotnet restore
```

## -2- Voer het voorbeeld uit

```bash
dotnet run
```

## -3- Test het voorbeeld

Start een aparte terminal voordat je de onderstaande stappen uitvoert (zorg ervoor dat de server nog steeds draait).

Met de server actief in één terminal, open je een andere terminal en voer je het volgende commando uit:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Dit zou een webserver moeten starten met een visuele interface waarmee je het voorbeeld kunt testen.

> Zorg ervoor dat **Streamable HTTP** is geselecteerd als het transporttype, en de URL is `http://localhost:3001/mcp`.

Zodra de server is verbonden:

- probeer tools op te sommen en voer `add` uit met de argumenten 2 en 4. Je zou 6 als resultaat moeten zien.
- ga naar resources en resource template en roep "greeting" aan, typ een naam in en je zou een begroeting moeten zien met de naam die je hebt ingevoerd.

### Testen in CLI-modus

Je kunt het direct in CLI-modus starten door het volgende commando uit te voeren:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Dit zal alle beschikbare tools op de server weergeven. Je zou de volgende uitvoer moeten zien:

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

Om een tool aan te roepen, typ:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Je zou de volgende uitvoer moeten zien:

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
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.