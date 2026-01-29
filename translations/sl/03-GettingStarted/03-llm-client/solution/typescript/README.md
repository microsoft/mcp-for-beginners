# Zagon tega primera

Ta primer vključuje uporabo LLM na odjemalcu. LLM potrebuje, da to zaženete bodisi v Codespaces ali pa si nastavite osebni dostopni žeton v GitHubu, da bo delovalo.

## -1- Namestite odvisnosti

```bash
npm install
```

## -3- Zaženite strežnik

```bash
npm run build
```

## -4- Zaženite odjemalca

```sh
npm run client
```

Videli boste rezultat, podoben temu:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.