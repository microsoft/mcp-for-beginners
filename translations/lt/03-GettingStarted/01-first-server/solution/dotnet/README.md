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

Tai turėtų paleisti interneto serverį su vizualine sąsaja, leidžiančia išbandyti pavyzdį.

Kai serveris prisijungia:

- pabandykite išvardyti įrankius ir paleisti `add`, su argumentais 2 ir 4, turėtumėte matyti rezultatą 6.
- eikite į resursus ir resursų šabloną, iškvieskite "greeting", įveskite vardą ir turėtumėte matyti pasisveikinimą su jūsų pateiktu vardu.

### Testavimas CLI režimu

Galite paleisti tiesiogiai CLI režimu, vykdydami šią komandą:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Tai išvardins visus įrankius, prieinamus serveryje. Turėtumėte matyti šį rezultatą:

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

> [!TIP]
> Paprastai daug greičiau paleisti inspektorių CLI režimu nei naršyklėje.
> Daugiau apie inspektorių skaitykite [čia](https://github.com/modelcontextprotocol/inspector).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.