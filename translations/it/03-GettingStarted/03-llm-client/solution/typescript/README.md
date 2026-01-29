# Esecuzione di questo esempio

Questo esempio prevede l’utilizzo di un LLM sul client. L’LLM richiede che tu esegua questo in un Codespaces oppure che configuri un token di accesso personale su GitHub per farlo funzionare.

## -1- Installa le dipendenze

```bash
npm install
```

## -3- Avvia il server

```bash
npm run build
```

## -4- Avvia il client

```sh
npm run client
```

Dovresti vedere un risultato simile a:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.