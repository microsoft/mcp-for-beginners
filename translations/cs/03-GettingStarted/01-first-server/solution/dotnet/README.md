# Spuštění tohoto příkladu

## -1- Nainstalujte závislosti

```bash
dotnet restore
```

## -3- Spusťte příklad

```bash
dotnet run
```

## -4- Otestujte příklad

S běžícím serverem v jednom terminálu otevřete další terminál a spusťte následující příkaz:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Tím by se měl spustit webový server s vizuálním rozhraním, které vám umožní otestovat příklad.

Jakmile je server připojen:

- zkuste vypsat nástroje a spustit `add` s argumenty 2 a 4, měli byste vidět výsledek 6.
- přejděte na zdroje a šablonu zdroje, zavolejte "greeting", zadejte jméno a měli byste vidět pozdrav s uvedeným jménem.

### Testování v režimu CLI

Můžete jej spustit přímo v režimu CLI pomocí následujícího příkazu:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Tím se vypíší všechny dostupné nástroje na serveru. Měli byste vidět následující výstup:

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

Pro spuštění nástroje zadejte:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Měli byste vidět následující výstup:

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
> Obvykle je mnohem rychlejší spustit inspektor v režimu CLI než v prohlížeči.
> Přečtěte si více o inspektoru [zde](https://github.com/modelcontextprotocol/inspector).

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.