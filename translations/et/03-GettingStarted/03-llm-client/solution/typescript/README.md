# Selle näite käivitamine

See näide eeldab, et kliendil on LLM. LLM nõuab, et kas käivitaksite selle Codespaces'is või seadistaksite GitHubis isikliku juurdepääsutunnuse, et see töötaks.

## -1- Sõltuvuste installimine

```bash
npm install
```

## -3- Serveri käivitamine

```bash
npm run build
```

## -4- Kliendi käivitamine

```sh
npm run client
```

Te peaksite nägema tulemust, mis on sarnane järgmisega:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.