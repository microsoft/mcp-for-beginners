# Esecuzione di questo esempio

Si consiglia di installare `uv` ma non è obbligatorio, vedi [istruzioni](https://docs.astral.sh/uv/#highlights)

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
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.