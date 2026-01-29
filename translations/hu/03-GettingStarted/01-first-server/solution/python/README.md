# A példa futtatása

Ajánlott telepíteni az `uv`-t, de nem kötelező, lásd [utasítások](https://docs.astral.sh/uv/#highlights)

## -0- Hozz létre egy virtuális környezetet

```bash
python -m venv venv
```

## -1- Aktiváld a virtuális környezetet

```bash
venv\Scripts\activate
```

## -2- Telepítsd a függőségeket

```bash
pip install "mcp[cli]"
```

## -3- Futtasd a példát

```bash
mcp run server.py
```

## -4- Teszteld a példát

Amíg a szerver fut az egyik terminálban, nyiss egy másik terminált, és futtasd az alábbi parancsot:

```bash
mcp dev server.py
```

Ez elindít egy webes szervert vizuális felülettel, amely lehetővé teszi a példa tesztelését.

Miután a szerver csatlakozott:

- Próbáld ki az eszközök listázását, és futtasd az `add`-et, 2 és 4 argumentumokkal. Az eredményben 6-ot kell látnod.

- Menj a forrásokhoz és a forrássablonhoz, és hívd meg a `get_greeting`-et. Írj be egy nevet, és látnod kell egy üdvözlést az általad megadott névvel.

### Tesztelés CLI módban

Az általad futtatott inspector valójában egy Node.js alkalmazás, és a `mcp dev` ennek egy wrapperje.

Közvetlenül CLI módban is elindíthatod az alábbi parancs futtatásával:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

Ez felsorolja az összes elérhető eszközt a szerveren. A következő kimenetet kell látnod:

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
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

A következő kimenetet kell látnod:

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
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.