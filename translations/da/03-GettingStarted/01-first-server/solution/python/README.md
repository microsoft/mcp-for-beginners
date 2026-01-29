# Kør denne prøve

Det anbefales at installere `uv`, men det er ikke nødvendigt, se [instruktioner](https://docs.astral.sh/uv/#highlights)

## -0- Opret et virtuelt miljø

```bash
python -m venv venv
```

## -1- Aktiver det virtuelle miljø

```bash
venv\Scripts\activate
```

## -2- Installer afhængighederne

```bash
pip install "mcp[cli]"
```

## -3- Kør prøven

```bash
mcp run server.py
```

## -4- Test prøven

Med serveren kørende i én terminal, åbne en anden terminal og kør følgende kommando:

```bash
mcp dev server.py
```

Dette bør starte en webserver med en visuel grænseflade, der giver dig mulighed for at teste prøven.

Når serveren er forbundet:

- prøv at liste værktøjer og kør `add` med argumenterne 2 og 4, du bør se 6 som resultat.

- gå til ressourcer og ressource-skabelon og kald get_greeting, indtast et navn, og du bør se en hilsen med det navn, du har angivet.

### Test i CLI-tilstand

Den inspektør, du kørte, er faktisk en Node.js-app, og `mcp dev` er en wrapper omkring den.

Du kan starte den direkte i CLI-tilstand ved at køre følgende kommando:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

Dette vil liste alle værktøjer, der er tilgængelige på serveren. Du bør se følgende output:

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

For at kalde et værktøj skal du skrive:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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