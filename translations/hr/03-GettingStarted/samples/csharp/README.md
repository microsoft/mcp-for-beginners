# Osnovna MCP usluga kalkulatora

Ova usluga pruža osnovne operacije kalkulatora putem Model Context Protocol (MCP). Dizajnirana je kao jednostavan primjer za početnike koji uče o MCP implementacijama.

Za više informacija pogledajte [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Značajke

Ova usluga kalkulatora nudi sljedeće mogućnosti:

1. **Osnovne aritmetičke operacije**:
   - Zbrajanje dva broja
   - Oduzimanje jednog broja od drugog
   - Množenje dva broja
   - Dijeljenje jednog broja drugim (s provjerom dijeljenja s nulom)

## Korištenje `stdio` tipa
  
## Konfiguracija

1. **Konfigurirajte MCP servere**:
   - Otvorite svoj radni prostor u VS Code.
   - Napravite `.vscode/mcp.json` datoteku u mapi radnog prostora za konfiguraciju MCP servera. Primjer konfiguracije:

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

   - Bit ćete upitani da unesete root GitHub repozitorija, koji se može dohvatiti naredbom `git rev-parse --show-toplevel`.

## Korištenje usluge

Usluga izlaže sljedeće API krajnje točke putem MCP protokola:

- `add(a, b)`: Zbrojite dva broja
- `subtract(a, b)`: Oduzmite drugi broj od prvog
- `multiply(a, b)`: Pomnožite dva broja
- `divide(a, b)`: Podijelite prvi broj drugim (s provjerom nule)
- isPrime(n): Provjerite je li broj prost

## Testirajte s Github Copilot Chat u VS Code

1. Pokušajte poslati zahtjev usluzi koristeći MCP protokol. Na primjer, možete pitati:
   - "Zbroji 5 i 3"
   - "Oduzmi 10 od 4"
   - "Pomnoži 6 i 7"
   - "Podijeli 8 s 2"
   - "Je li 37854 prost?"
   - "Koja su 3 prosta broja prije i poslije 4242?"
2. Da biste bili sigurni da se koriste alati, dodajte #MyCalculator u prompt. Na primjer:
   - "Zbroji 5 i 3 #MyCalculator"
   - "Oduzmi 10 od 4 #MyCalculator


## Verzija u kontejneru

Prethodno rješenje je izvrsno kad imate instaliran .NET SDK i sve ovisnosti su na mjestu. Međutim, ako želite podijeliti rješenje ili ga pokrenuti u drugom okruženju, možete koristiti verziju u kontejneru.

1. Pokrenite Docker i provjerite da radi.
1. Iz terminala se navigirajte u mapu `03-GettingStarted\samples\csharp\src` 
1. Za izgradnju Docker slike za kalkulatorsku uslugu, izvršite sljedeću naredbu (zamijenite `<YOUR-DOCKER-USERNAME>` svojim Docker Hub korisničkim imenom):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Nakon što je slika izgrađena, prenesite je na Docker Hub. Pokrenite sljedeću naredbu:
   ```bash
   docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
   ```

## Korištenje Docker verzije

1. U datoteci `.vscode/mcp.json` zamijenite konfiguraciju servera sa sljedećim:
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
   Gledajući konfiguraciju, možete vidjeti da je naredba `docker`, a argumenti su `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calculator`. Zastavica `--rm` osigurava da se kontejner ukloni nakon što se zaustavi, a zastavica `-i` omogućuje interakciju sa standardnim ulazom kontejnera. Posljednji argument je ime slike koju smo upravo izgradili i postavili na Docker Hub.

## Testirajte Docker verziju

Pokrenite MCP Server klikom na mali gumb Start iznad `"mcp-calculator": {`, i kao i prije, možete tražiti da vam kalkulatorska usluga obavi neke matematičke operacije.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->