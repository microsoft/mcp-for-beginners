# Eseguire questo esempio

## -1- Installa le dipendenze

```bash
dotnet restore
```

## -2- Esegui l'esempio

```bash
dotnet run
```

## -3- Testa l'esempio

Avvia un terminale separato prima di eseguire il comando seguente (assicurati che il server sia ancora in esecuzione).

Con il server in esecuzione in un terminale, apri un altro terminale ed esegui il seguente comando:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Questo dovrebbe avviare un server web con un'interfaccia visiva che ti permette di testare l'esempio.

> Assicurati che **Streamable HTTP** sia selezionato come tipo di trasporto e che l'URL sia `http://localhost:3001/mcp`.

Una volta che il server è connesso:

- prova a elencare gli strumenti e a eseguire `add`, con argomenti 2 e 4, dovresti vedere 6 nel risultato.
- vai alle risorse e al modello di risorsa e chiama "greeting", inserisci un nome e dovresti vedere un saluto con il nome che hai fornito.

### Test in modalità CLI

Puoi avviarlo direttamente in modalità CLI eseguendo il seguente comando:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Questo elencherà tutti gli strumenti disponibili nel server. Dovresti vedere il seguente output:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

Per invocare uno strumento digita:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Dovresti vedere il seguente output:

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
> Di solito è molto più veloce eseguire l'inspector in modalità CLI rispetto al browser.
> Leggi di più sull'inspector [qui](https://github.com/modelcontextprotocol/inspector).

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.