<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "07863f50601f395c3bdfce30f555f11a",
  "translation_date": "2025-08-26T16:46:10+00:00",
  "source_file": "03-GettingStarted/01-first-server/solution/dotnet/README.md",
  "language_code": "lt"
}
-->
# Paleisti šį pavyzdį

## -1- Įdiekite priklausomybes

```bash
dotnet restore
```

## -3- Paleiskite pavyzdį

```bash
dotnet run
```

## -4- Išbandykite pavyzdį

Kai serveris veikia viename terminale, atidarykite kitą terminalą ir paleiskite šią komandą:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Tai turėtų paleisti žiniatinklio serverį su vizualine sąsaja, leidžiančia išbandyti pavyzdį.

Kai serveris prisijungęs:

- pabandykite išvardyti įrankius ir paleisti `add` su argumentais 2 ir 4, rezultatuose turėtumėte matyti 6.
- eikite į išteklius ir išteklių šabloną, iškvieskite „greeting“, įveskite vardą ir turėtumėte pamatyti pasveikinimą su jūsų pateiktu vardu.

### Testavimas CLI režimu

Galite paleisti tiesiogiai CLI režimu, vykdydami šią komandą:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Tai išvardins visus serveryje esančius įrankius. Turėtumėte matyti šį rezultatą:

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

Norėdami iškviesti įrankį, įveskite:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Turėtumėte matyti šį rezultatą:

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

> ![!TIP]
> Paprastai inspektorių paleisti CLI režimu yra daug greičiau nei naršyklėje.
> Plačiau apie inspektorių skaitykite [čia](https://github.com/modelcontextprotocol/inspector).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.