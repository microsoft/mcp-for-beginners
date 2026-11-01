# Osnovna storitev kalkulator MCP

Ta storitev nudi osnovne kalkulator operacije preko Model Context Protocol (MCP). Namenjena je kot preprost primer za začetnike pri učenju o implementacijah MCP.

Za več informacij glejte [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Značilnosti

Ta kalkulator storitev ponuja naslednje zmogljivosti:

1. **Osnovne aritmetične operacije**:
   - Seštevanje dveh števil
   - Odštevanje enega števila od drugega
   - Množenje dveh števil
   - Deljenje enega števila z drugim (z preverjanjem deljenja z nič)

## Uporaba tipa `stdio`
  
## Konfiguracija

1. **Konfigurirajte MCP strežnike**:
   - Odprite delovni prostor v VS Code.
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

Storitev odpre naslednje API končne točke preko MCP protokola:

- `add(a, b)`: Seštej dve števili
- `subtract(a, b)`: Odštej drugo število od prvega
- `multiply(a, b)`: Pomnoži dve števili
- `divide(a, b)`: Deli prvo število z drugim (s preverjanjem ničle)
- isPrime(n): Preveri, če je število praštevilo

## Testirajte z Github Copilot Chat v VS Code

1. Poskusite poslati zahtevo storitvi z uporabo MCP protokola. Na primer, lahko vprašate:
   - "Seštej 5 in 3"
   - "Odštej 10 od 4"
   - "Pomnoži 6 in 7"
   - "Deli 8 z 2"
   - "Je 37854 praštevilo?"
   - "Katera so 3 praštevila pred in za 4242?"
2. Da zagotovite uporabo orodij, dodajte #MyCalculator k pozivu. Na primer:
   - "Seštej 5 in 3 #MyCalculator"
   - "Odštej 10 od 4 #MyCalculator


## Verzija z vsebnikom

Prejšnja rešitev je odlična, če imate nameščen .NET SDK in so vse odvisnosti urejene. Če pa želite deliti rešitev ali jo zagnati v drugem okolju, lahko uporabite verzijo z vsebnikom.

1. Zaženite Docker in preverite, da teče.
1. V terminalu se premaknite v mapo `03-GettingStarted\samples\csharp\src` 
1. Za izgradnjo Docker slike za kalkulatorsko storitev izvedite naslednji ukaz (zamenjajte `<YOUR-DOCKER-USERNAME>` z vašim uporabniškim imenom Docker Hub):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Ko je slika izdelana, jo naložite na Docker Hub. Zaženite naslednji ukaz:
   ```bash
   docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
   ```

## Uporaba verzije z Dockerjem

1. V datoteki `.vscode/mcp.json` zamenjajte konfiguracijo strežnika z naslednjo:
   ```json
    "mcp-calculator": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calculator"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Gledano konfiguracijo, ukaz je `docker` in argumenti so `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calculator`. Zastavica `--rm` zagotavlja odstranitev vsebnika po zaustavitvi, zastavica `-i` pa omogoča interakcijo z običajnim vhodom vsebnika. Zadnji argument je ime slike, ki smo jo pravkar zgradili in naložili na Docker Hub.

## Testirajte verzijo z Dockerjem

Zaženite MCP strežnik s klikom na majhen gumb Start nad `"mcp-calculator": {` in tako kot prej lahko zaprosite kalkulatorsko storitev za nekaj računskih operacij.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->