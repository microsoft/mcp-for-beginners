# Kørsel af dette eksempel

Dette eksempel involverer at have en LLM på klienten. LLM'en kræver, at du enten kører dette i en Codespaces eller opsætter et personligt adgangstoken i GitHub for at få det til at fungere.

## -1- Installer afhængighederne

```bash
npm install
```

## -3- Kør serveren

```bash
npm run build
```

## -4- Kør klienten

```sh
npm run client
```

Du bør se et resultat, der ligner:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.