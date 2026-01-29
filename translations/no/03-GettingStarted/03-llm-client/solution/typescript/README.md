# Kjøre dette eksemplet

Dette eksemplet innebærer å ha en LLM på klienten. LLM-en krever at du enten kjører dette i Codespaces eller at du setter opp en personlig tilgangstoken i GitHub for at det skal fungere.

## -1- Installer avhengighetene

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

Du bør se et resultat som ligner på:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.