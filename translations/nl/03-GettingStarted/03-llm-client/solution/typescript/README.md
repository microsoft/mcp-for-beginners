# Dit voorbeeld uitvoeren

Dit voorbeeld gaat over het gebruik van een LLM aan de clientzijde. De LLM vereist dat je dit uitvoert in een Codespaces-omgeving of dat je een personal access token instelt in GitHub om het te laten werken.

## -1- Installeer de dependencies

```bash
npm install
```

## -3- Start de server

```bash
npm run build
```

## -4- Start de client

```sh
npm run client
```

Je zou een resultaat moeten zien dat lijkt op:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.