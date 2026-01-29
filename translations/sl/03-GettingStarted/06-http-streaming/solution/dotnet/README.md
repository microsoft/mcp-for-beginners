# Zagon tega vzorca

## -1- Namestite odvisnosti

```bash
dotnet restore
```

## -2- Zaženite vzorec

```bash
dotnet run
```

## -3- Preizkusite vzorec

Preden zaženete spodnje ukaze, odprite ločen terminal (prepričajte se, da strežnik še vedno deluje).

Ko strežnik deluje v enem terminalu, odprite drug terminal in zaženite naslednji ukaz:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

To bi moralo zagnati spletni strežnik z vizualnim vmesnikom, ki vam omogoča testiranje vzorca.

> Prepričajte se, da je **Streamable HTTP** izbran kot vrsta prenosa, in da je URL `http://localhost:3001/mcp`.

Ko je strežnik povezan:

- poskusite našteti orodja in zaženite `add` z argumentoma 2 in 4; v rezultatu bi morali videti 6.
- pojdite na vire in predlogo virov ter pokličite "greeting", vnesite ime in videli boste pozdrav z vnesenim imenom.

### Testiranje v načinu CLI

Lahko ga neposredno zaženete v načinu CLI z naslednjim ukazom:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

To bo prikazalo seznam vseh orodij, ki so na voljo na strežniku. Videti bi morali naslednji izpis:

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

Za uporabo orodja vnesite:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
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
> Na splošno je veliko hitreje zagnati inšpektor v načinu CLI kot v brskalniku.
> Več o inšpektorju preberite [tukaj](https://github.com/modelcontextprotocol/inspector).

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.