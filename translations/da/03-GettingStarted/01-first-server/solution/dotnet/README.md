# Kør denne prøve

## -1- Installer afhængighederne

```bash
dotnet restore
```

## -3- Kør prøven

```bash
dotnet run
```

## -4- Test prøven

Med serveren kørende i én terminal, åbne en anden terminal og kør følgende kommando:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Dette bør starte en webserver med en visuel grænseflade, der giver dig mulighed for at teste prøven.

Når serveren er forbundet:

- prøv at liste værktøjer og kør `add` med argumenterne 2 og 4, du bør se 6 som resultat.
- gå til ressourcer og ressource-skabelon og kald "greeting", indtast et navn, og du bør se en hilsen med det navn, du har angivet.

### Test i CLI-tilstand

Du kan starte den direkte i CLI-tilstand ved at køre følgende kommando:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Dette vil liste alle de værktøjer, der er tilgængelige på serveren. Du bør se følgende output:

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

For at kalde et værktøj skal du skrive:

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
> Det er normalt meget hurtigere at køre inspektøren i CLI-tilstand end i browseren.
> Læs mere om inspektøren [her](https://github.com/modelcontextprotocol/inspector).

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.