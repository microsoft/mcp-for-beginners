# Selle näidise käivitamine

## -1- Paigalda sõltuvused

```bash
dotnet restore
```

## -2- Käivita näidis

```bash
dotnet run
```

## -3- Testi näidist

Enne alloleva käsu käivitamist ava eraldi terminal (veendu, et server töötab endiselt).

Kui server töötab ühes terminalis, ava teine terminal ja käivita järgmine käsk:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

See peaks käivitama veebiserveri visuaalse liidesega, mis võimaldab näidist testida.

> Veendu, et **Streamable HTTP** on transporditüübiks valitud ja URL on `http://localhost:3001/mcp`.

Kui server on ühendatud:

- proovi tööriistade loetlemist ja käivita `add`, argumentidega 2 ja 4, tulemuseks peaks olema 6.
- mine ressursside ja ressursimalli juurde ning kutsu "greeting", sisesta nimi ja peaksid nägema tervitust koos sisestatud nimega.

### Testimine CLI režiimis

Saad selle otse CLI režiimis käivitada, käivitades järgmise käsu:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

See loetleb kõik serveris saadaval olevad tööriistad. Peaksid nägema järgmist väljundit:

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

Tööriista käivitamiseks sisesta:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Peaksid nägema järgmist väljundit:

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
> Inspektori käivitamine CLI režiimis on tavaliselt palju kiirem kui brauseris.
> Loe inspektori kohta lähemalt [siit](https://github.com/modelcontextprotocol/inspector).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.