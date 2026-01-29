# Basic Calculator MCP Service

Ova usluga pruža osnovne kalkulatorske operacije putem Model Context Protocol (MCP). Dizajnirana je kao jednostavan primjer za početnike koji uče o implementacijama MCP-a.

Za više informacija, pogledajte [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Značajke

Ova kalkulatorska usluga nudi sljedeće mogućnosti:

1. **Osnovne aritmetičke operacije**:
   - Zbrajanje dva broja
   - Oduzimanje jednog broja od drugog
   - Množenje dva broja
   - Dijeljenje jednog broja s drugim (uz provjeru dijeljenja s nulom)

## Korištenje `stdio` tipa
  
## Konfiguracija

1. **Konfigurirajte MCP servere**:
   - Otvorite svoj workspace u VS Code-u.
   - Kreirajte `.vscode/mcp.json` datoteku u mapi workspacea za konfiguraciju MCP servera. Primjer konfiguracije:

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

   - Bit ćete upitani da unesete root GitHub repozitorija, koji možete dohvatiti naredbom `git rev-parse --show-toplevel`.

## Korištenje usluge

Usluga izlaže sljedeće API endpoint-e putem MCP protokola:

- `add(a, b)`: Zbroji dva broja
- `subtract(a, b)`: Oduzmi drugi broj od prvog
- `multiply(a, b)`: Pomnoži dva broja
- `divide(a, b)`: Podijeli prvi broj s drugim (uz provjeru na nulu)
- isPrime(n): Provjeri je li broj prost

## Testiranje s Github Copilot Chat u VS Code-u

1. Pokušajte poslati zahtjev usluzi koristeći MCP protokol. Na primjer, možete pitati:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. Da biste bili sigurni da koristi alate, dodajte #MyCalculator u upit. Na primjer:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Verzija u kontejneru

Prethodno rješenje je odlično ako imate instaliran .NET SDK i sve potrebne ovisnosti. Međutim, ako želite podijeliti rješenje ili ga pokrenuti u drugom okruženju, možete koristiti verziju u kontejneru.

1. Pokrenite Docker i provjerite da radi.
1. U terminalu se premjestite u mapu `03-GettingStarted\samples\csharp\src`
1. Za izgradnju Docker slike za kalkulatorsku uslugu, izvršite sljedeću naredbu (zamijenite `<YOUR-DOCKER-USERNAME>` svojim Docker Hub korisničkim imenom):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Nakon što je slika izgrađena, učitajte je na Docker Hub. Pokrenite sljedeću naredbu:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Korištenje Dockerizirane verzije

1. U `.vscode/mcp.json` datoteci zamijenite konfiguraciju servera sa sljedećom:
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
   Iz konfiguracije je vidljivo da je naredba `docker`, a argumenti su `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Zastavica `--rm` osigurava da se kontejner ukloni nakon zaustavljanja, a `-i` omogućuje interakciju sa standardnim ulazom kontejnera. Posljednji argument je ime slike koju smo upravo izgradili i poslali na Docker Hub.

## Testiranje Dockerizirane verzije

Pokrenite MCP Server klikom na mali gumb Start iznad `"mcp-calc": {`, i kao i prije, možete tražiti od kalkulatorske usluge da obavi neke izračune za vas.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.