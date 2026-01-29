# Paleisti šį pavyzdį

## -1- Įdiekite priklausomybes

```bash
dotnet restore
```

## -2- Paleiskite pavyzdį

```bash
dotnet run
```

## -3- Išbandykite pavyzdį

Prieš vykdydami žemiau pateiktą komandą, atidarykite atskirą terminalą (įsitikinkite, kad serveris vis dar veikia).

Kai serveris veikia viename terminale, atidarykite kitą terminalą ir paleiskite šią komandą:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Tai turėtų paleisti žiniatinklio serverį su vizualine sąsaja, leidžiančia išbandyti pavyzdį.

> Įsitikinkite, kad **Streamable HTTP** yra pasirinktas kaip transportavimo tipas, o URL yra `http://localhost:3001/mcp`.

Kai serveris prisijungia:

- pabandykite išvardyti įrankius ir paleisti `add` su argumentais 2 ir 4, rezultatuose turėtumėte matyti 6.
- eikite į išteklius ir išteklių šabloną, iškvieskite "greeting", įveskite vardą ir turėtumėte pamatyti pasveikinimą su jūsų įvestu vardu.

### Testavimas CLI režimu

Galite paleisti tiesiogiai CLI režimu, vykdydami šią komandą:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Tai išvardins visus serveryje esančius įrankius. Turėtumėte matyti šį rezultatą:

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

Norėdami iškviesti įrankį, įveskite:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Turėtumėte matyti šį rezultatą:

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
> Plačiau apie inspektorių skaitykite [čia](https://github.com/modelcontextprotocol/inspector).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.