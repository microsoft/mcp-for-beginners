<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "69ba3bd502bd743233137bac5539c08b",
  "translation_date": "2025-08-26T16:50:40+00:00",
  "source_file": "03-GettingStarted/05-sse-server/solution/python/README.md",
  "language_code": "lt"
}
-->
# Paleisti šį pavyzdį

Rekomenduojama įdiegti `uv`, tačiau tai nėra būtina, žr. [instrukcijas](https://docs.astral.sh/uv/#highlights)

## -0- Sukurkite virtualią aplinką

```bash
python -m venv venv
```

## -1- Aktyvuokite virtualią aplinką

```bash
venv\Scrips\activate
```

## -2- Įdiekite priklausomybes

```bash
pip install "mcp[cli]"
```

## -3- Paleiskite pavyzdį

```bash
uvicorn server:app
```

## -4- Išbandykite pavyzdį

Kai serveris veikia viename terminale, atidarykite kitą terminalą ir paleiskite šią komandą:

```bash
mcp dev server.py
```

Tai turėtų paleisti interneto serverį su vizualine sąsaja, leidžiančia išbandyti pavyzdį.

Kai serveris prisijungia:

- pabandykite išvardyti įrankius ir paleisti `add` su argumentais 2 ir 4, turėtumėte matyti rezultatą 6.
- eikite į išteklius ir išteklių šabloną, iškvieskite get_greeting, įveskite vardą ir turėtumėte matyti pasveikinimą su jūsų įvestu vardu.

### Testavimas CLI režimu

Inspektorius, kurį paleidote, iš tikrųjų yra Node.js programa, o `mcp dev` yra jos apvalkalas.

Galite paleisti jį tiesiogiai CLI režimu, vykdydami šią komandą:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:8000/sse --method tools/list
```

Tai išvardins visus serveryje esančius įrankius. Turėtumėte matyti šį išvestį:

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
npx @modelcontextprotocol/inspector --cli http://localhost:8000/sse --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Turėtumėte matyti šį išvestį:

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
> Paprastai inspektorių CLI režimu paleisti yra daug greičiau nei naršyklėje.  
> Plačiau apie inspektorių skaitykite [čia](https://github.com/modelcontextprotocol/inspector).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.