# Spuštění tohoto příkladu

## -1- Instalace závislostí

```bash
dotnet restore
```

## -2- Spuštění příkladu

```bash
dotnet run
```

## -3- Testování příkladu

Před spuštěním níže uvedeného příkazu otevřete samostatný terminál (ujistěte se, že server stále běží).

S běžícím serverem v jednom terminálu otevřete další terminál a spusťte následující příkaz:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Tím by se měl spustit webový server s vizuálním rozhraním, které vám umožní testovat příklad.

> Ujistěte se, že jako typ přenosu je vybrán **Streamable HTTP** a URL je `http://localhost:3001/mcp`.

Jakmile je server připojen:

- zkuste vypsat nástroje a spustit `add` s argumenty 2 a 4, měli byste vidět výsledek 6.
- přejděte na zdroje a šablonu zdrojů, zavolejte "greeting", zadejte jméno a měli byste vidět pozdrav s jménem, které jste zadali.

### Testování v režimu CLI

Můžete jej spustit přímo v režimu CLI pomocí následujícího příkazu:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Tím se vypíší všechny nástroje dostupné na serveru. Měli byste vidět následující výstup:

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

Pro spuštění nástroje zadejte:

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

> [!TIP]
> Obvykle je mnohem rychlejší spustit inspektor v režimu CLI než v prohlížeči.
> Přečtěte si více o inspektoru [zde](https://github.com/modelcontextprotocol/inspector).

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.