# Köra detta exempel

Det rekommenderas att installera `uv`, men det är inte ett krav, se [instruktioner](https://docs.astral.sh/uv/#highlights)

## -0- Skapa en virtuell miljö

```bash
python -m venv venv
```

## -1- Aktivera den virtuella miljön

```bash
venv\Scripts\activate
```

## -2- Installera beroenden

```bash
pip install "mcp[cli]"
```

## -3- Kör exemplet

```bash
mcp run server.py
```

## -4- Testa exemplet

Med servern igång i en terminal, öppna en annan terminal och kör följande kommando:

```bash
mcp dev server.py
```

Detta bör starta en webbserver med ett visuellt gränssnitt som låter dig testa exemplet.

När servern är ansluten:

- Försök att lista verktyg och kör `add` med argumenten 2 och 4, du bör se 6 som resultat.

- Gå till resurser och resursmall och anropa get_greeting, skriv in ett namn och du bör se en hälsning med det namn du angav.

### Testa i CLI-läge

Inspektorn du körde är faktiskt en Node.js-app och `mcp dev` är ett omslag runt den.

Du kan starta den direkt i CLI-läge genom att köra följande kommando:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

Detta kommer att lista alla verktyg som finns tillgängliga på servern. Du bör se följande output:

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

För att anropa ett verktyg, skriv:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Du bör se följande output:

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
> Det är vanligtvis mycket snabbare att köra inspektorn i CLI-läge än i webbläsaren.
> Läs mer om inspektorn [här](https://github.com/modelcontextprotocol/inspector).

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.