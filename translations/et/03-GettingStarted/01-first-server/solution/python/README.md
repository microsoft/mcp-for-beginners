# Selle näidise käivitamine

Soovitatav on paigaldada `uv`, kuid see pole kohustuslik, vaata [juhiseid](https://docs.astral.sh/uv/#highlights)

## -0- Loo virtuaalne keskkond

```bash
python -m venv venv
```

## -1- Aktiveeri virtuaalne keskkond

```bash
venv\Scripts\activate
```

## -2- Paigalda sõltuvused

```bash
pip install "mcp[cli]"
```

## -3- Käivita näidis

```bash
mcp run server.py
```

## -4- Testi näidist

Kui server töötab ühes terminalis, ava teine terminal ja käivita järgmine käsk:

```bash
mcp dev server.py
```

See peaks käivitama veebiserveri visuaalse liidesega, mis võimaldab näidist testida.

Kui server on ühendatud:

- proovi tööriistade loendamist ja käivita `add`, argumentidega 2 ja 4, tulemuseks peaks olema 6.

- mine ressursside ja ressursimalli juurde ning kutsu välja get_greeting, sisesta nimi ja peaksid nägema tervitust koos sisestatud nimega.

### Testimine CLI režiimis

Inspektor, mille käivitasid, on tegelikult Node.js rakendus ja `mcp dev` on selle ümbris. 

Seda saab otse CLI režiimis käivitada järgmise käsuga:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

See loetleb kõik serveris saadaval olevad tööriistad. Väljund peaks olema järgmine:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

Tööriista käivitamiseks sisesta:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Väljund peaks olema järgmine:

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
> Tavaliselt on inspektorit CLI režiimis käivitada palju kiirem kui brauseris.
> Loe inspektori kohta rohkem [siit](https://github.com/modelcontextprotocol/inspector).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.