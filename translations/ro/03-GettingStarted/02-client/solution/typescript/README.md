# Rularea acestui exemplu

Se recomandă să instalezi `uv`, dar nu este obligatoriu, vezi [instrucțiunile](https://docs.astral.sh/uv/#highlights)

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
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.