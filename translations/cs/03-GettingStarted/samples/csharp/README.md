# Základní kalkulační služba MCP

Tato služba poskytuje základní kalkulační operace prostřednictvím Model Context Protocol (MCP). Je navržena jako jednoduchý příklad pro začátečníky, kteří se učí o implementacích MCP.

Pro více informací viz [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funkce

Tato kalkulační služba nabízí následující možnosti:

1. **Základní aritmetické operace**:
   - Sčítání dvou čísel
   - Odečítání jednoho čísla od druhého
   - Násobení dvou čísel
   - Dělení jednoho čísla druhým (s kontrolou dělení nulou)

## Použití typu `stdio`
  
## Konfigurace

1. **Nastavení MCP serverů**:
   - Otevřete svůj workspace ve VS Code.
   - Vytvořte soubor `.vscode/mcp.json` ve složce workspace pro konfiguraci MCP serverů. Příklad konfigurace:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - Budete vyzváni k zadání kořenové složky GitHub repozitáře, kterou lze získat příkazem `git rev-parse --show-toplevel`.

## Použití služby

Služba zpřístupňuje následující API endpointy přes MCP protokol:

- `add(a, b)`: Sečte dvě čísla
- `subtract(a, b)`: Odečte druhé číslo od prvního
- `multiply(a, b)`: Vynásobí dvě čísla
- `divide(a, b)`: Vydělí první číslo druhým (s kontrolou nulového dělení)
- isPrime(n): Zjistí, zda je číslo prvočíslem

## Testování s Github Copilot Chat ve VS Code

1. Zkuste poslat požadavek na službu pomocí MCP protokolu. Například můžete požádat:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. Aby bylo jisté, že se používají nástroje, přidejte do promptu #MyCalculator. Například:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Verze v kontejneru

Předchozí řešení je skvělé, pokud máte nainstalované .NET SDK a všechny závislosti jsou připravené. Pokud však chcete řešení sdílet nebo spustit v jiném prostředí, můžete použít verzi v kontejneru.

1. Spusťte Docker a ujistěte se, že běží.
1. V terminálu přejděte do složky `03-GettingStarted\samples\csharp\src`
1. Pro sestavení Docker image kalkulační služby spusťte následující příkaz (nahraďte `<YOUR-DOCKER-USERNAME>` svým uživatelským jménem na Docker Hubu):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. Po sestavení image ji nahrajte na Docker Hub pomocí příkazu:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Použití Docker verze

1. V souboru `.vscode/mcp.json` nahraďte konfiguraci serveru tímto:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   V konfiguraci vidíte, že příkaz je `docker` a argumenty jsou `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Přepínač `--rm` zajistí odstranění kontejneru po jeho zastavení a `-i` umožňuje interakci se standardním vstupem kontejneru. Poslední argument je název image, kterou jsme právě sestavili a nahráli na Docker Hub.

## Testování Docker verze

Spusťte MCP Server kliknutím na malé tlačítko Start nad `"mcp-calc": {` a stejně jako dříve můžete požádat kalkulační službu, aby pro vás provedla nějaké výpočty.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.