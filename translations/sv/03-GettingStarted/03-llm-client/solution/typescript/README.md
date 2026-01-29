# Köra detta exempel

Det här exemplet innebär att ha en LLM på klienten. LLM kräver att du antingen kör detta i en Codespaces eller att du ställer in en personlig åtkomsttoken i GitHub för att det ska fungera.

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
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.