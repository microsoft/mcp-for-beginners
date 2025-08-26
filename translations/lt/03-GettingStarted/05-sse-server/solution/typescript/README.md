<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fab17bf59e2eb82a5aeef03ad977d31",
  "translation_date": "2025-08-26T16:50:20+00:00",
  "source_file": "03-GettingStarted/05-sse-server/solution/typescript/README.md",
  "language_code": "lt"
}
-->
# Paleisti šį pavyzdį

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

Tai turėtų paleisti žiniatinklio serverį su vizualine sąsaja, leidžiančia išbandyti pavyzdį.

Kai serveris prisijungęs:

- pabandykite išvardyti įrankius ir paleisti `add` su argumentais 2 ir 4, rezultatuose turėtumėte matyti 6.
- eikite į išteklius ir išteklių šabloną, iškvieskite „greeting“, įveskite vardą ir turėtumėte pamatyti pasveikinimą su jūsų pateiktu vardu.

### Testavimas CLI režimu

Inspektorius, kurį paleidote, iš tikrųjų yra Node.js programa, o `mcp dev` yra jos apvalkalas.

- Paleiskite serverį naudodami komandą `npm run build`.

- Atskirame terminale paleiskite šią komandą:

    ```bash
    npx @modelcontextprotocol/inspector --cli http://localhost:3000/sse --method tools/list
    ```

    Tai išvardins visus serveryje esančius įrankius. Turėtumėte matyti šį rezultatą:

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

- Iškvieskite įrankio tipą įvesdami šią komandą:

    ```bash
    npx @modelcontextprotocol/inspector --cli http://localhost:3000/sse --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
    ```

Turėtumėte matyti šį rezultatą:

    ```text
    {
        "content": [
        {
        "type": "text",
        "text": "3"
        }
        ]
    }
    ```

> ![!TIP]
> Paprastai inspektorių CLI režimu paleisti yra daug greičiau nei naršyklėje.
> Daugiau apie inspektorių skaitykite [čia](https://github.com/modelcontextprotocol/inspector).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.