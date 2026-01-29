# Kjøre dette eksemplet

Det anbefales å installere `uv`, men det er ikke nødvendig, se [instruksjoner](https://docs.astral.sh/uv/#highlights)

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
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.