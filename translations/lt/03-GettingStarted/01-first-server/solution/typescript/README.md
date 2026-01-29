# Paleisti šį pavyzdį

Rekomenduojama įdiegti `uv`, tačiau tai nėra būtina, žr. [instrukcijas](https://docs.astral.sh/uv/#highlights)

## -1- Įdiekite priklausomybes

```bash
npm install
```

## -3- Paleiskite pavyzdį

```bash
npm run build
```

## -4- Išbandykite pavyzdį

Kai serveris veikia viename terminale, atidarykite kitą terminalą ir paleiskite šią komandą:

```bash
npm run inspector
```

Tai turėtų paleisti interneto serverį su vizualine sąsaja, leidžiančia išbandyti pavyzdį.

Kai serveris prisijungia:

- pabandykite išvardyti įrankius ir paleisti `add`, su argumentais 2 ir 4, turėtumėte matyti rezultatą 6.
- eikite į išteklius ir išteklių šabloną, iškvieskite „greeting“, įveskite vardą ir turėtumėte matyti pasisveikinimą su jūsų pateiktu vardu.

### Testavimas CLI režimu

Inspektorius, kurį paleidote, iš tikrųjų yra Node.js programa, o `mcp dev` yra jos apvalkalas.

Jį galite paleisti tiesiogiai CLI režimu, vykdydami šią komandą:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Tai išvardins visus įrankius, esančius serveryje. Turėtumėte matyti tokį rezultatą:

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
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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