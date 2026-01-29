# Köra detta exempel

Det rekommenderas att du installerar `uv` men det är inte ett måste, se [instructions](https://docs.astral.sh/uv/#highlights)

## -1- Installera beroenden

```bash
npm install
```

## -3- Starta servern

```bash
npm run build
```

## -4- Starta klienten

```sh
npm run client
```

Du bör se ett resultat som liknar:

```text
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.