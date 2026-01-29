# Kjøre dette eksemplet

## -1- Installer avhengighetene

```bash
dotnet restore
```

## -3- Kjør eksemplet

```bash
dotnet run
```

## -4- Test eksemplet

Med serveren kjørende i én terminal, åpne en annen terminal og kjør følgende kommando:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Dette skal starte en webserver med et visuelt grensesnitt som lar deg teste eksemplet.

Når serveren er tilkoblet:

- prøv å liste verktøyene og kjør `add` med argumentene 2 og 4, du bør se 6 som resultat.
- gå til ressurser og ressursmal, og kall "greeting", skriv inn et navn, og du bør se en hilsen med navnet du oppga.

### Testing i CLI-modus

Du kan starte det direkte i CLI-modus ved å kjøre følgende kommando:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Dette vil liste alle verktøyene som er tilgjengelige på serveren. Du bør se følgende output:

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

For å bruke et verktøy, skriv:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Du bør se følgende output:

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
> Det er vanligvis mye raskere å kjøre inspektøren i CLI-modus enn i nettleseren.
> Les mer om inspektøren [her](https://github.com/modelcontextprotocol/inspector).

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.