# Rularea acestui exemplu

Acest exemplu implică utilizarea unui LLM pe client. LLM-ul necesită fie să rulezi acest lucru în Codespaces, fie să configurezi un token de acces personal în GitHub pentru a funcționa.

## -1- Instalează dependențele

```bash
npm install
```

## -3- Pornește serverul

```bash
npm run build
```

## -4- Pornește clientul

```sh
npm run client
```

Ar trebui să vezi un rezultat similar cu:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.