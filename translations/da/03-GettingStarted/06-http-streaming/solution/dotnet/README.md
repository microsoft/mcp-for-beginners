# Kør denne prøve

## -1- Installer afhængighederne

```bash
dotnet restore
```

## -2- Kør prøven

```bash
dotnet run
```

## -3- Test prøven

Start en separat terminal, før du kører nedenstående (sørg for, at serveren stadig kører).

Med serveren kørende i én terminal, åbnes en anden terminal, og følgende kommando køres:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Dette bør starte en webserver med en visuel grænseflade, der giver dig mulighed for at teste prøven.

> Sørg for, at **Streamable HTTP** er valgt som transporttype, og URL'en er `http://localhost:3001/mcp`.

Når serveren er forbundet:

- prøv at liste værktøjer og kør `add` med argumenterne 2 og 4, du bør se 6 som resultat.
- gå til ressourcer og ressource-skabelon og kald "greeting", indtast et navn, og du bør se en hilsen med det navn, du har angivet.

### Test i CLI-tilstand

Du kan starte det direkte i CLI-tilstand ved at køre følgende kommando:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Dette vil liste alle værktøjer, der er tilgængelige på serveren. Du bør se følgende output:

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

For at kalde et værktøj skal du skrive:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Du bør se følgende output:

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
> Det er normalt meget hurtigere at køre inspektøren i CLI-tilstand end i browseren.
> Læs mere om inspektøren [her](https://github.com/modelcontextprotocol/inspector).

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.