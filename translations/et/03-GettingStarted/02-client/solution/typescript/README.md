# Selle näidise käivitamine

Soovitatav on paigaldada `uv`, kuid see pole kohustuslik, vaata [juhiseid](https://docs.astral.sh/uv/#highlights)

## -1- Paigalda sõltuvused

```bash
npm install
```

## -3- Käivita server

```bash
npm run build
```

## -4- Käivita klient

```sh
npm run client
```

Sa peaksid nägema tulemust, mis on sarnane järgmisele:

```text
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.