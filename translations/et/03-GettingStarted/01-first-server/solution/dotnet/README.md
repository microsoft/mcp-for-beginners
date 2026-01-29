# Selle näite käivitamine

## -1- Paigalda sõltuvused

```bash
dotnet restore
```

## -3- Käivita näide

```bash
dotnet run
```

## -4- Testi näidet

Kui server töötab ühes terminalis, ava teine terminal ja käivita järgmine käsk:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

See peaks käivitama veebiserveri visuaalse liidesega, mis võimaldab näidet testida.

Kui server on ühendatud:

- proovi loetleda tööriistu ja käivita `add`, argumentidega 2 ja 4, tulemuseks peaks olema 6.
- mine ressursside ja ressursimalli juurde ning kutsu "greeting", sisesta nimi ja peaksid nägema tervitust sisestatud nimega.

### Testimine CLI režiimis

Sa saad selle otse CLI režiimis käivitada, kasutades järgmist käsku:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

See loetleb kõik serveris saadaval olevad tööriistad. Näed järgmist väljundit:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
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
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Näed järgmist väljundit:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Tavaliselt on inspektori käivitamine CLI režiimis palju kiirem kui brauseris.
> Loe inspektori kohta rohkem [siit](https://github.com/modelcontextprotocol/inspector).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.