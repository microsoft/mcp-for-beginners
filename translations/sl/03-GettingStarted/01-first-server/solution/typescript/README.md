# Zagon tega vzorca

Priporočljivo je namestiti `uv`, vendar ni nujno, glejte [navodila](https://docs.astral.sh/uv/#highlights)

## -1- Namestite odvisnosti

```bash
npm install
```

## -3- Zaženite vzorec

```bash
npm run build
```

## -4- Testirajte vzorec

Ko strežnik deluje v enem terminalu, odprite drug terminal in zaženite naslednji ukaz:

```bash
npm run inspector
```

To bi moralo zagnati spletni strežnik z vizualnim vmesnikom, ki vam omogoča testiranje vzorca.

Ko je strežnik povezan:

- poskusite našteti orodja in zaženite `add` z argumentoma 2 in 4, v rezultatu bi morali videti 6.
- pojdite na vire in predlogo virov ter pokličite "greeting", vnesite ime in videli boste pozdrav z imenom, ki ste ga navedli.

### Testiranje v načinu CLI

Inšpektor, ki ste ga zagnali, je dejansko aplikacija Node.js, `mcp dev` pa je ovojnica okoli nje.

Lahko ga zaženete neposredno v načinu CLI z naslednjim ukazom:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

To bo prikazalo seznam vseh orodij, ki so na voljo na strežniku. Videti bi morali naslednji izpis:

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

Za klic orodja vnesite:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Videti bi morali naslednji izpis:

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
> Običajno je veliko hitreje zagnati inšpektor v načinu CLI kot v brskalniku.
> Več o inšpektorju preberite [tukaj](https://github.com/modelcontextprotocol/inspector).

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.