# Spustenie tejto ukážky

## -1- Nainštalujte závislosti

```bash
dotnet restore
```

## -3- Spustite ukážku

```bash
dotnet run
```

## -4- Otestujte ukážku

Keď server beží v jednom termináli, otvorte ďalší terminál a spustite nasledujúci príkaz:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Tým by sa mal spustiť webový server s vizuálnym rozhraním, ktoré vám umožní otestovať ukážku.

Keď je server pripojený:

- skúste zobraziť zoznam nástrojov a spustiť `add` s argumentmi 2 a 4, mali by ste vidieť výsledok 6.
- prejdite na zdroje a šablónu zdroja, zavolajte "greeting", zadajte meno a mali by ste vidieť pozdrav s menom, ktoré ste zadali.

### Testovanie v režime CLI

Môžete ho spustiť priamo v režime CLI pomocou nasledujúceho príkazu:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Tým sa zobrazí zoznam všetkých nástrojov dostupných na serveri. Mali by ste vidieť nasledujúci výstup:

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

Ak chcete spustiť nástroj, zadajte:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Mali by ste vidieť nasledujúci výstup:

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
> Zvyčajne je oveľa rýchlejšie spustiť inšpektor v režime CLI ako v prehliadači.
> Viac o inšpektore si môžete prečítať [tu](https://github.com/modelcontextprotocol/inspector).

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.