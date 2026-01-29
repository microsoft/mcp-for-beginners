# Zagon tega vzorca

## -1- Namestite odvisnosti

```bash
dotnet restore
```

## -3- Zaženite vzorec

```bash
dotnet run
```

## -4- Preizkusite vzorec

Ko strežnik deluje v enem terminalu, odprite drug terminal in zaženite naslednji ukaz:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

To bi moralo zagnati spletni strežnik z vizualnim vmesnikom, ki vam omogoča testiranje vzorca.

Ko je strežnik povezan:

- poskusite našteti orodja in zaženite `add` z argumentoma 2 in 4, v rezultatu bi morali videti 6.
- pojdite na vire in predlogo virov ter pokličite "greeting", vnesite ime in videli boste pozdrav z imenom, ki ste ga vnesli.

### Testiranje v načinu CLI

Lahko ga neposredno zaženete v načinu CLI z naslednjim ukazom:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

To bo prikazalo seznam vseh orodij, ki so na voljo na strežniku. Videti bi morali naslednji izpis:

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

Za uporabo orodja vnesite:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Videti bi morali naslednji izpis:

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
> Običajno je veliko hitreje zagnati inšpektor v načinu CLI kot v brskalniku.
> Več o inšpektorju preberite [tukaj](https://github.com/modelcontextprotocol/inspector).

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.