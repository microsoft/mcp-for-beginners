# A példa futtatása

Ajánlott telepíteni az `uv`-t, de nem kötelező, lásd [útmutató](https://docs.astral.sh/uv/#highlights)

## -1- A függőségek telepítése

```bash
npm install
```

## -3- A példa futtatása

```bash
npm run build
```

## -4- A példa tesztelése

Amíg a szerver fut az egyik terminálban, nyiss meg egy másik terminált, és futtasd az alábbi parancsot:

```bash
npm run inspector
```

Ez elindít egy webes szervert vizuális felülettel, amely lehetővé teszi a példa tesztelését.

Miután a szerver csatlakozott:

- próbáld meg listázni az eszközöket, és futtasd az `add`-ot, 2 és 4 argumentumokkal, az eredményben 6-ot kell látnod.
- menj a "resources" és "resource template" részhez, hívd meg a "greeting"-et, írj be egy nevet, és látnod kell egy üdvözlést az általad megadott névvel.

### Tesztelés CLI módban

Az általad futtatott inspector valójában egy Node.js alkalmazás, és az `mcp dev` ennek egy wrapperje.

Közvetlenül CLI módban is elindíthatod az alábbi parancs futtatásával:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Ez listázza az összes elérhető eszközt a szerveren. Az alábbi kimenetet kell látnod:

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

Egy eszköz meghívásához írd be:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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
> Általában sokkal gyorsabb CLI módban futtatni az inspectort, mint böngészőben.
> További információ az inspectorról [itt](https://github.com/modelcontextprotocol/inspector).

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.