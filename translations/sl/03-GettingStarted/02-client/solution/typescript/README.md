# Zagon tega primera

Priporočamo, da namestite `uv`, vendar ni nujno, več informacij najdete v [navodilih](https://docs.astral.sh/uv/#highlights)

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

Videli bi morali rezultat, podoben temu:

```text
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.