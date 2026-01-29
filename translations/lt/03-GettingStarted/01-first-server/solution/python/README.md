# Paleisti šį pavyzdį

Rekomenduojama įdiegti `uv`, tačiau tai nėra būtina, žr. [instrukcijas](https://docs.astral.sh/uv/#highlights)

## -0- Sukurkite virtualią aplinką

```bash
python -m venv venv
```

## -1- Aktyvuokite virtualią aplinką

```bash
venv\Scripts\activate
```

## -2- Įdiekite priklausomybes

```bash
pip install "mcp[cli]"
```

## -3- Paleiskite pavyzdį

```bash
mcp run server.py
```

## -4- Išbandykite pavyzdį

Kai serveris veikia viename terminale, atidarykite kitą terminalą ir paleiskite šią komandą:

```bash
mcp dev server.py
```

Tai turėtų paleisti interneto serverį su vizualine sąsaja, leidžiančia išbandyti pavyzdį.

Kai serveris prisijungia:

- pabandykite išvardinti įrankius ir paleisti `add`, su argumentais 2 ir 4, turėtumėte matyti rezultatą 6.

- eikite į resursus ir resursų šabloną, iškvieskite get_greeting, įveskite vardą ir turėtumėte matyti pasveikinimą su jūsų pateiktu vardu.

### Testavimas CLI režimu

Inspektorius, kurį paleidote, iš tikrųjų yra Node.js programa, o `mcp dev` yra jos apvalkalas.

Jį galite paleisti tiesiogiai CLI režimu, vykdydami šią komandą:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

Tai išvardins visus įrankius, prieinamus serveryje. Turėtumėte matyti tokį rezultatą:

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

Norėdami iškviesti įrankį, įveskite:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Turėtumėte matyti tokį rezultatą:

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
> Paprastai inspektorių paleisti CLI režimu yra daug greičiau nei naršyklėje.
> Daugiau apie inspektorių skaitykite [čia](https://github.com/modelcontextprotocol/inspector).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.