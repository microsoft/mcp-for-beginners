# A minta futtatása

## -1- A függőségek telepítése

```bash
dotnet restore
```

## -3- A minta futtatása

```bash
dotnet run
```

## -4- A minta tesztelése

Amikor a szerver egy terminálban fut, nyiss meg egy másik terminált, és futtasd az alábbi parancsot:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Ez elindít egy webes szervert vizuális felülettel, amely lehetővé teszi a minta tesztelését.

Miután a szerver csatlakozott:

- próbáld meg listázni az eszközöket, és futtasd az `add` parancsot a 2 és 4 argumentumokkal, az eredményben 6-ot kell látnod.
- menj a forrásokhoz és a forrássablonhoz, hívd meg a "greeting" funkciót, írj be egy nevet, és látnod kell egy üdvözlést az általad megadott névvel.

### Tesztelés CLI módban

Közvetlenül CLI módban is elindíthatod az alábbi parancs futtatásával:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Ez listázza az összes elérhető eszközt a szerveren. Az alábbi kimenetet kell látnod:

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

Egy eszköz meghívásához írd be:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Az alábbi kimenetet kell látnod:

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
> Általában sokkal gyorsabb az inspektort CLI módban futtatni, mint böngészőben.
> További információ az inspektorról [itt](https://github.com/modelcontextprotocol/inspector).

---

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.