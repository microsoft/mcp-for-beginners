# A minta futtatása

## -1- A függőségek telepítése

```bash
dotnet restore
```

## -2- A minta futtatása

```bash
dotnet run
```

## -3- A minta tesztelése

Indíts el egy külön terminált, mielőtt az alábbi parancsot futtatnád (győződj meg róla, hogy a szerver még fut).

Amíg a szerver fut az egyik terminálban, nyiss meg egy másik terminált, és futtasd az alábbi parancsot:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Ez elindít egy webes szervert vizuális felülettel, amely lehetővé teszi a minta tesztelését.

> Győződj meg róla, hogy a **Streamable HTTP** van kiválasztva szállítási típusnak, és az URL `http://localhost:3001/mcp`.

Miután a szerver csatlakozott:

- próbáld meg listázni az eszközöket, és futtasd az `add` parancsot a 2 és 4 argumentumokkal, az eredményben 6-ot kell látnod.
- menj a forrásokhoz és a forrássablonhoz, és hívd meg a "greeting" funkciót, írj be egy nevet, és látnod kell egy üdvözlést az általad megadott névvel.

### Tesztelés CLI módban

Közvetlenül elindíthatod CLI módban az alábbi parancs futtatásával:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Ez listázza az összes elérhető eszközt a szerveren. Az alábbi kimenetet kell látnod:

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

Egy eszköz meghívásához írd be:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Az alábbi kimenetet kell látnod:

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
> Általában sokkal gyorsabb az inspektort CLI módban futtatni, mint böngészőben.
> További információ az inspektorról [itt](https://github.com/modelcontextprotocol/inspector).

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.