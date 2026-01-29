# Pokretanje ovog primjera

Ovaj primjer uključuje korištenje LLM-a na klijentu. LLM zahtijeva da ovo pokrenete u Codespaces ili da postavite osobni pristupni token na GitHubu da bi radilo.

## -1- Instalirajte ovisnosti

```bash
npm install
```

## -3- Pokrenite server

```bash
npm run build
```

## -4- Pokrenite klijenta

```sh
npm run client
```

Trebali biste vidjeti rezultat sličan ovom:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.