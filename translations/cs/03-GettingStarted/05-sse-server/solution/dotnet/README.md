<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b97c5e77cede68533d7a92d0ce89bc0a",
  "translation_date": "2025-05-17T11:58:31+00:00",
  "source_file": "03-GettingStarted/05-sse-server/solution/dotnet/README.md",
  "language_code": "cs"
}
-->
# Spuštění tohoto příkladu

## -1- Instalace závislostí

```bash
dotnet run
```

## -2- Spuštění příkladu

```bash
dotnet run
```

## -3- Testování příkladu

Než spustíte níže uvedené, otevřete samostatný terminál (ujistěte se, že server stále běží).

Se spuštěným serverem v jednom terminálu otevřete další terminál a spusťte následující příkaz:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

To by mělo spustit webový server s vizuálním rozhraním, které vám umožní otestovat příklad.

Jakmile je server připojen:

- zkuste vypsat nástroje a spusťte `add` s argumenty 2 a 4, měli byste vidět 6 jako výsledek.
- přejděte k zdrojům a šabloně zdrojů a zavolejte "greeting", zadejte jméno a měli byste vidět pozdrav se zadaným jménem.

### Testování v režimu CLI

Můžete jej spustit přímo v režimu CLI pomocí následujícího příkazu:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

To vypíše všechny nástroje dostupné na serveru. Měli byste vidět následující výstup:

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

Pro vyvolání nástroje napište:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Měli byste vidět následující výstup:

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

> ![!TIP]
> Obvykle je mnohem rychlejší spustit inspektor v režimu CLI než v prohlížeči.
> Přečtěte si více o inspektoru [zde](https://github.com/modelcontextprotocol/inspector).

**Upozornění**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, uvědomte si, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.