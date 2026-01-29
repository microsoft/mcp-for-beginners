# Kørsel af dette eksempel

Det anbefales at installere `uv`, men det er ikke et krav, se [instructions](https://docs.astral.sh/uv/#highlights)

## -1- Installer afhængighederne

```bash
npm install
```

## -3- Start serveren

```bash
npm run build
```

## -4- Start klienten

```sh
npm run client
```

Du burde se et resultat, der ligner:

```text
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.