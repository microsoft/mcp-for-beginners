# Köra detta exempel

## -1- Installera beroenden

```bash
dotnet restore
```

## -3- Kör exemplet

```bash
dotnet run
```

## -4- Testa exemplet

Med servern igång i en terminal, öppna en annan terminal och kör följande kommando:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Detta bör starta en webbserver med ett visuellt gränssnitt som låter dig testa exemplet.

När servern är ansluten:

- prova att lista verktyg och kör `add` med argumenten 2 och 4, du bör se 6 som resultat.
- gå till resurser och resursmall och anropa "greeting", skriv in ett namn och du bör se en hälsning med namnet du angav.

### Testa i CLI-läge

Du kan starta det direkt i CLI-läge genom att köra följande kommando:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Detta kommer att lista alla verktyg som är tillgängliga på servern. Du bör se följande output:

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

För att anropa ett verktyg, skriv:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Du bör se följande output:

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
> Det är vanligtvis mycket snabbare att köra inspektorn i CLI-läge än i webbläsaren.
> Läs mer om inspektorn [här](https://github.com/modelcontextprotocol/inspector).

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.