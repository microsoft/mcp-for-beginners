# Spuštění tohoto příkladu

Doporučuje se nainstalovat `uv`, ale není to nutné, viz [instrukce](https://docs.astral.sh/uv/#highlights)

## -1- Instalace závislostí

```bash
npm install
```

## -3- Spuštění příkladu

```bash
npm run build
```

## -4- Testování příkladu

S běžícím serverem v jednom terminálu otevřete další terminál a spusťte následující příkaz:

```bash
npm run inspector
```

Tím by se měl spustit webový server s vizuálním rozhraním, které vám umožní testovat příklad.

Jakmile je server připojen:

- zkuste vypsat nástroje a spustit `add` s argumenty 2 a 4, měli byste vidět výsledek 6.
- přejděte k prostředkům a šabloně prostředků a zavolejte "greeting", zadejte jméno a měli byste vidět pozdrav s jménem, které jste zadali.

### Testování v režimu CLI

Inspektor, který jste spustili, je ve skutečnosti aplikace Node.js a `mcp dev` je obal kolem ní.

Můžete ji spustit přímo v režimu CLI pomocí následujícího příkazu:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Tím se vypíší všechny nástroje dostupné na serveru. Měli byste vidět následující výstup:

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

Pro spuštění nástroje zadejte:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.