# Osnovna kalkulator MCP storitev

Ta storitev omogoča osnovne kalkulator operacije preko Model Context Protocol (MCP). Namenjena je kot preprost primer za začetnike, ki se učijo o implementacijah MCP.

Za več informacij glej [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Značilnosti

Ta kalkulator storitev ponuja naslednje funkcionalnosti:

1. **Osnovne aritmetične operacije**:
   - Seštevanje dveh števil
   - Odštevanje enega števila od drugega
   - Množenje dveh števil
   - Deljenje enega števila z drugim (s preverjanjem deljenja z nič)

## Uporaba tipa `stdio`
  
## Konfiguracija

1. **Konfigurirajte MCP strežnike**:
   - Odprite svoj delovni prostor v VS Code.
   - Ustvarite datoteko `.vscode/mcp.json` v mapi delovnega prostora za konfiguracijo MCP strežnikov. Primer konfiguracije:

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

   - Zahtevalo vas bo, da vnesete koren GitHub repozitorija, ki ga lahko pridobite z ukazom `git rev-parse --show-toplevel`.

## Uporaba storitve

Storitev izpostavlja naslednje API končne točke preko MCP protokola:

- `add(a, b)`: Seštej dve števili
- `subtract(a, b)`: Odštej drugo število od prvega
- `multiply(a, b)`: Pomnoži dve števili
- `divide(a, b)`: Deli prvo število z drugim (s preverjanjem ničle)
- isPrime(n): Preveri, ali je število praštevilo

## Testiranje z Github Copilot Chat v VS Code

1. Poskusi poslati zahtevo storitvi preko MCP protokola. Na primer, lahko vprašaš:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. Da se prepričaš, da uporablja orodja, dodaj #MyCalculator v poziv. Na primer:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Verzija v kontejnerju

Prejšnja rešitev je odlična, če imaš nameščen .NET SDK in so vse odvisnosti urejene. Če pa želiš rešitev deliti ali jo zagnati v drugem okolju, lahko uporabiš verzijo v kontejnerju.

1. Zaženi Docker in preveri, da deluje.
1. V terminalu se premakni v mapo `03-GettingStarted\samples\csharp\src`
1. Za izdelavo Docker slike za kalkulator storitev zaženi naslednji ukaz (zamenjaj `<YOUR-DOCKER-USERNAME>` z uporabniškim imenom na Docker Hubu):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. Ko je slika izdelana, jo naloži na Docker Hub z naslednjim ukazom:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Uporaba Dockerizirane verzije

1. V datoteki `.vscode/mcp.json` zamenjaj konfiguracijo strežnika z naslednjo:
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
   Če pogledaš konfiguracijo, vidiš, da je ukaz `docker`, argumenti pa `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Preklop `--rm` poskrbi, da se kontejner odstrani po zaustavitvi, `-i` pa omogoča interakcijo s standardnim vhodom kontejnerja. Zadnji argument je ime slike, ki smo jo pravkar izdelali in naložili na Docker Hub.

## Testiranje Dockerizirane verzije

Zaženi MCP strežnik s klikom na majhno tipko Start nad `"mcp-calc": {`, in tako kot prej lahko prosiš kalkulator storitev, da opravi nekaj računskih operacij zate.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.