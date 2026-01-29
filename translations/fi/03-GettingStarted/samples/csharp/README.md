# Basic Calculator MCP Service

Tämä palvelu tarjoaa peruslaskutoimituksia Model Context Protocolin (MCP) kautta. Se on suunniteltu yksinkertaiseksi esimerkiksi aloittelijoille, jotka opettelevat MCP:n toteutuksia.

Lisätietoja löytyy osoitteesta [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Ominaisuudet

Tämä laskinpalvelu tarjoaa seuraavat toiminnot:

1. **Peruslaskutoimitukset**:
   - Kahden luvun yhteenlasku
   - Yhden luvun vähentäminen toisesta
   - Kahden luvun kertolasku
   - Yhden luvun jakaminen toisella (nollalla jakamisen tarkistus)

## `stdio`-tyypin käyttö

## Konfigurointi

1. **Määritä MCP-palvelimet**:
   - Avaa työtila VS Codessa.
   - Luo työtilakansioon tiedosto `.vscode/mcp.json` MCP-palvelimien määrittämistä varten. Esimerkkikonfiguraatio:

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

   - Sinulta pyydetään GitHub-repositorion juurihakemisto, jonka saat komennolla `git rev-parse --show-toplevel`.

## Palvelun käyttö

Palvelu tarjoaa seuraavat API-päätepisteet MCP-protokollan kautta:

- `add(a, b)`: Laskee kahden luvun summan
- `subtract(a, b)`: Vähentää toisen luvun ensimmäisestä
- `multiply(a, b)`: Kertoo kaksi lukua keskenään
- `divide(a, b)`: Jakaa ensimmäisen luvun toisella (nollalla jakamisen tarkistus)
- isPrime(n): Tarkistaa, onko luku alkuluku

## Testaa Github Copilot Chatilla VS Codessa

1. Kokeile tehdä pyyntö palvelulle MCP-protokollaa käyttäen. Esimerkiksi voit kysyä:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. Varmistaaksesi, että työkaluja käytetään, lisää kehotteeseen #MyCalculator. Esimerkiksi:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Konttiversio

Edellinen ratkaisu toimii hyvin, kun sinulla on .NET SDK asennettuna ja kaikki riippuvuudet kunnossa. Jos kuitenkin haluat jakaa ratkaisun tai ajaa sen eri ympäristössä, voit käyttää konttiversiota.

1. Käynnistä Docker ja varmista, että se on käynnissä.
1. Siirry terminaalissa kansioon `03-GettingStarted\samples\csharp\src`
1. Rakenna Docker-kuva laskinpalvelulle suorittamalla seuraava komento (korvaa `<YOUR-DOCKER-USERNAME>` omalla Docker Hub -käyttäjänimelläsi):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. Kun kuva on rakennettu, lataa se Docker Hubiin suorittamalla seuraava komento:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Docker-versio käyttöön

1. Korvaa `.vscode/mcp.json` -tiedostossa palvelimen konfiguraatio seuraavalla:
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
   Konfiguraatiosta näet, että komento on `docker` ja argumentit `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. `--rm`-lipuke varmistaa, että kontti poistetaan, kun se pysähtyy, ja `-i`-lipuke mahdollistaa vuorovaikutuksen kontin standardisyötteen kanssa. Viimeinen argumentti on juuri rakentamamme ja Docker Hubiin työntämämme kuvan nimi.

## Testaa Docker-versiota

Käynnistä MCP-palvelin napsauttamalla pientä Käynnistä-painiketta kohdan `"mcp-calc": {` yläpuolella, ja kuten aiemmin, voit pyytää laskinpalvelua tekemään laskutoimituksia puolestasi.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.