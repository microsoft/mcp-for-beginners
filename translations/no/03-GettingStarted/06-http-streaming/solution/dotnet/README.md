# Kjøre dette eksempelet

## -1- Installer avhengighetene

```bash
dotnet restore
```

## -2- Kjør eksempelet

```bash
dotnet run
```

## -3- Test eksempelet

Start et separat terminalvindu før du kjører kommandoen nedenfor (sørg for at serveren fortsatt kjører).

Med serveren kjørende i ett terminalvindu, åpne et annet terminalvindu og kjør følgende kommando:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Dette skal starte en webserver med et visuelt grensesnitt som lar deg teste eksempelet.

> Sørg for at **Streamable HTTP** er valgt som transporttype, og URL er `http://localhost:3001/mcp`.

Når serveren er koblet til:

- prøv å liste verktøy og kjør `add`, med argumentene 2 og 4, du bør se 6 som resultat.
- gå til ressurser og ressursmal og kall "greeting", skriv inn et navn, og du bør se en hilsen med navnet du oppga.

### Testing i CLI-modus

Du kan starte det direkte i CLI-modus ved å kjøre følgende kommando:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Dette vil liste alle verktøyene som er tilgjengelige på serveren. Du bør se følgende utdata:

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

For å bruke et verktøy, skriv:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Du bør se følgende utdata:

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
> Det er vanligvis mye raskere å kjøre inspektøren i CLI-modus enn i nettleseren.
> Les mer om inspektøren [her](https://github.com/modelcontextprotocol/inspector).

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.