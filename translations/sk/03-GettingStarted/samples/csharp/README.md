# Základná kalkulačka MCP služba

Táto služba poskytuje základné kalkulačné operácie prostredníctvom Model Context Protocol (MCP). Je navrhnutá ako jednoduchý príklad pre začiatočníkov, ktorí sa učia o implementáciách MCP.

Pre viac informácií pozrite [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funkcie

Táto kalkulačková služba ponúka nasledujúce možnosti:

1. **Základné aritmetické operácie**:
   - Sčítanie dvoch čísel
   - Odčítanie jedného čísla od druhého
   - Násobenie dvoch čísel
   - Delenie jedného čísla druhým (s kontrolou delenia nulou)

## Použitie typu `stdio`
  
## Konfigurácia

1. **Nastavenie MCP serverov**:
   - Otvorte svoj pracovný priestor vo VS Code.
   - Vytvorte súbor `.vscode/mcp.json` vo vašom pracovnom priečinku na konfiguráciu MCP serverov. Príklad konfigurácie:

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

   - Bude vás vyzvaný na zadanie koreňového adresára GitHub repozitára, ktorý môžete získať príkazom `git rev-parse --show-toplevel`.

## Použitie služby

Služba sprístupňuje nasledujúce API endpointy cez MCP protokol:

- `add(a, b)`: Sčíta dve čísla
- `subtract(a, b)`: Odčíta druhé číslo od prvého
- `multiply(a, b)`: Vynásobí dve čísla
- `divide(a, b)`: Vydelí prvé číslo druhým (s kontrolou delenia nulou)
- isPrime(n): Skontroluje, či je číslo prvočíslo

## Testovanie s Github Copilot Chat vo VS Code

1. Skúste poslať požiadavku na službu pomocou MCP protokolu. Napríklad môžete požiadať:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. Aby ste sa uistili, že sa používajú nástroje, pridajte do promptu #MyCalculator. Napríklad:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Verzia v kontajneri

Predchádzajúce riešenie je skvelé, keď máte nainštalovaný .NET SDK a všetky závislosti sú pripravené. Ak však chcete riešenie zdieľať alebo spustiť v inom prostredí, môžete použiť verziu v kontajneri.

1. Spustite Docker a uistite sa, že beží.
1. V termináli prejdite do priečinka `03-GettingStarted\samples\csharp\src`
1. Na zostavenie Docker image pre kalkulačkovú službu spustite nasledujúci príkaz (nahraďte `<YOUR-DOCKER-USERNAME>` vaším používateľským menom na Docker Hub):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. Po zostavení image ho nahrajte na Docker Hub pomocou tohto príkazu:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Použitie Docker verzie

1. V súbore `.vscode/mcp.json` nahraďte konfiguráciu servera týmto:
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
   Pri pohľade na konfiguráciu vidíte, že príkaz je `docker` a argumenty sú `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Prepínač `--rm` zabezpečuje, že kontajner sa po zastavení odstráni, a prepínač `-i` umožňuje interakciu so štandardným vstupom kontajnera. Posledný argument je názov image, ktorý sme práve zostavili a nahrali na Docker Hub.

## Testovanie Docker verzie

Spustite MCP server kliknutím na malý tlačidlo Štart nad `"mcp-calc": {`, a rovnako ako predtým môžete požiadať kalkulačkovú službu, aby pre vás vykonala nejaké výpočty.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.